## Key Topics
- **Resource detection processor:** Go contrib detectors are now selected via build tags, so only needed detectors are included. Release size is unchanged, and all resource detection runs through the Go SDK.
- **Node.js SDK switch:** Moving to SDK v3 and the Node SDK removes about 200 lines of custom wrapper code. Deprecated hooks will be removed in a later release. The change is a breaking one, covered by the Node.js 22 major version bump.
- **Performance benchmarking:** Lambda's uncontrolled environment makes timing results unreliable, though they still indicate large regressions. Options for storing results were discussed: Venture (automated charts and cleanup), Bencher (the benchmarking SIG's possible tool), or a GitHub Pages branch (needs manual cleanup).
- **Release plan:** Merge the Node version update first, then the other PRs, and cut a release. Users who hit issues can stay on the previous release.

## Action Items
- James Thompson: Update the README to document the new hook in the Node.js SDK switch PR.
- Tyler Benson: Review and merge the Node version update PR (add Node 26, remove Node 20).
- Tyler Benson: Review the resource detection PR and the Node.js SDK switch PR.
- James Thompson: Explore storing benchmark results in Venture or Bencher and share findings.
- Tyler Benson: Possibly absent next meeting; others may need to cover.

## Participants
Tyler Benson, James Thompson
