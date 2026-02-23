# OTel SIG Meeting Transcripts

Downloads OpenTelemetry SIG meeting transcripts from Zoom recordings and saves them as plain-text files organized by SIG and date.

## How it works

1. Fetches the public [OTel recordings Google Sheet](https://docs.google.com/spreadsheets/d/1SYKfjYhZdm2Wh2Cl6KVQalKg_m4NhTPZqq-8SzEVO6s) as CSV
2. Navigates to each Zoom recording page using a headless Chromium browser
3. Scrolls the transcript panel to defeat Zoom's virtual-list rendering
4. Saves transcripts to `transcripts/{sig-slug}/YYYY-MM-DD.txt`

## Setup

Requires Python 3.12+ and [uv](https://github.com/astral-sh/uv).

```bash
make install
```

## Usage

```bash
# Fetch transcripts from the start of the current month
make fetch

# Fetch from a specific date through today
make fetch SINCE=2026-02-01

# Fetch within a date range
make fetch BETWEEN=2026-01-01/2026-02-28

# Fetch a specific SIG only
make fetch SIG=Community-Demo-App-SIG

# Combine date and SIG filters
make fetch SINCE=2026-02-01 SIG=collector
make fetch BETWEEN=2026-01-01/2026-02-28 SIG=collector
```

`SIG` is a case-insensitive substring match against the SIG slug. The following shorthands are expanded automatically before matching:

| Shorthand | Expands to |
|-----------|------------|
| `otel` | `opentelemetry` |
| `gc` | `cc` |
| `tc` | `technical-committee` |
| `semconv`, `sem-conv`, `semantic-convention`, `semantic-conventions` | `semantic-convention`, `semconv`, `sem-conv` |
| `devex` | `developer-experience` |
| `browser` | `client` |
| `cc`, `c`, `cpp`, `c++` | `cc` |
| `k8s` | `kubernetes`, `k8s` |
| `js` | `javascript` |
| `dotnet`, `.net` | `net` |
| `lambda`, `serverless` | `faas` |

If the string matches more than one SIG, you will be prompted to pick one:

```
Multiple SIGs match 'go'. Please choose one:

  1. Go-Auto-Instrumentation-SIG
  2. Go-Compile-Time-Instrumentation-SIG
  3. Go-SIG
  4. Governance-Committee

Enter number:
```

Some SIGs appear under multiple names in the spreadsheet. The script normalises these to a single canonical directory:

| Spreadsheet name | Stored under |
|------------------|--------------|
| OpenTelemetry CC SIG | `CC-SIG` |

Already-downloaded transcripts are skipped on subsequent runs.

## Output

```
transcripts/
  Collector-SIG/
    2026-02-05.txt
  Specification-SIG/
    2026-02-10.txt
  ...
```

Each file starts with a header containing the SIG name, date, duration, and source URL, followed by transcript lines in `Speaker Name: utterance` format.
