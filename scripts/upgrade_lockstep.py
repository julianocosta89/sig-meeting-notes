"""Upgrade dependencies that must move in lockstep, which Dependabot cannot do.

The OpenTelemetry contrib packages (``opentelemetry-distro``,
``opentelemetry-instrumentation-*``) each pin ``opentelemetry-instrumentation``
to their own exact version.  Dependabot resolves every dependency on its own,
so each single bump is unsatisfiable and it silently skips them all.

This script lets uv resolve the whole family at once:

1. Relax every exact ``==`` pin whose name starts with one of the prefixes to
   ``>=`` in ``pyproject.toml``.
2. Run ``uv lock --upgrade-package`` for every locked package with that prefix
   (transitive ones such as ``opentelemetry-sdk`` included), leaving the rest
   of the lock alone.
3. Write the resolved versions back as exact pins and re-lock.

``pyproject.toml`` and ``uv.lock`` are restored when any step fails.

Usage:
    uv run python scripts/upgrade_lockstep.py [--prefix opentelemetry-]
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess  # noqa: S404 — runs uv with fixed arguments
import sys
import tomllib
from pathlib import Path

DEFAULT_PREFIXES = ("opentelemetry-",)

# A quoted exact pin inside pyproject.toml, e.g. "opentelemetry-distro==0.66b2"
_PIN_RE = re.compile(r'"(?P<name>[A-Za-z0-9][A-Za-z0-9._-]*)==(?P<version>[^"\s;,]+)"')


def _normalize(name: str) -> str:
    """PEP 503 name normalization (uv.lock stores normalized names)."""
    return re.sub(r"[-_.]+", "-", name).lower()


def _matches(name: str, prefixes: tuple[str, ...]) -> bool:
    normalized = _normalize(name)
    return any(normalized.startswith(_normalize(p)) for p in prefixes)


def find_pins(pyproject: str, prefixes: tuple[str, ...]) -> dict[str, str]:
    """Return {name: version} for every exact pin matching one of the prefixes."""
    return {
        m["name"]: m["version"]
        for m in _PIN_RE.finditer(pyproject)
        if _matches(m["name"], prefixes)
    }


def relax_pins(pyproject: str, prefixes: tuple[str, ...]) -> str:
    """Turn matching ``name==X`` pins into ``name>=X``."""

    def repl(m: re.Match[str]) -> str:
        if not _matches(m["name"], prefixes):
            return m.group(0)
        return f'"{m["name"]}>={m["version"]}"'

    return _PIN_RE.sub(repl, pyproject)


def repin(pyproject: str, versions: dict[str, str], prefixes: tuple[str, ...]) -> str:
    """Turn matching ``name>=X`` specifiers back into exact pins at the locked version."""
    relaxed_re = re.compile(r'"(?P<name>[A-Za-z0-9][A-Za-z0-9._-]*)>=(?P<version>[^"\s;,]+)"')

    def repl(m: re.Match[str]) -> str:
        name = m["name"]
        if not _matches(name, prefixes):
            return m.group(0)
        locked = versions.get(_normalize(name))
        if locked is None:
            raise KeyError(f"{name} is not in uv.lock")
        return f'"{name}=={locked}"'

    return relaxed_re.sub(repl, pyproject)


def locked_versions(lock_text: str) -> dict[str, str]:
    """Return {normalized name: version} for every package in uv.lock."""
    lock = tomllib.loads(lock_text)
    return {_normalize(p["name"]): p["version"] for p in lock.get("package", []) if "version" in p}


def _uv(*args: str) -> None:
    uv = shutil.which("uv")
    if uv is None:
        raise RuntimeError("uv not found on PATH")
    subprocess.run([uv, *args], check=True)  # noqa: S603 — fixed executable, no shell


def upgrade(root: Path, prefixes: tuple[str, ...]) -> dict[str, tuple[str, str]]:
    """Upgrade the matching pins in ``root``; return {name: (old, new)} for changed pins."""
    pyproject_path = root / "pyproject.toml"
    lock_path = root / "uv.lock"
    original_pyproject = pyproject_path.read_text()
    original_lock = lock_path.read_text()

    pins = find_pins(original_pyproject, prefixes)
    if not pins:
        return {}

    try:
        pyproject_path.write_text(relax_pins(original_pyproject, prefixes))
        family = sorted(n for n in locked_versions(original_lock) if _matches(n, prefixes))
        upgrade_args = [arg for name in family for arg in ("--upgrade-package", name)]
        _uv("lock", "--directory", str(root), *upgrade_args)

        versions = locked_versions(lock_path.read_text())
        pyproject_path.write_text(repin(pyproject_path.read_text(), versions, prefixes))
        _uv("lock", "--directory", str(root))
    except BaseException:
        pyproject_path.write_text(original_pyproject)
        lock_path.write_text(original_lock)
        raise

    new_pins = find_pins(pyproject_path.read_text(), prefixes)
    return {name: (pins[name], new_pins[name]) for name in pins if pins[name] != new_pins[name]}


def main(argv: list[str] | None = None) -> int:  # pragma: no cover
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--prefix",
        action="append",
        dest="prefixes",
        help="Package name prefix to upgrade together (repeatable). "
        f"Default: {', '.join(DEFAULT_PREFIXES)}",
    )
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Project directory")
    args = parser.parse_args(argv)
    prefixes = tuple(args.prefixes or DEFAULT_PREFIXES)

    changes = upgrade(args.root, prefixes)
    if not changes:
        print("Already up to date.")
        return 0
    for name, (old, new) in sorted(changes.items()):
        print(f"{name}: {old} -> {new}")
    return 0


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
