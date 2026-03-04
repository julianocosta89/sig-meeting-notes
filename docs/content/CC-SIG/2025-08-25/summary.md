## Key Topics
- Discussion on whether to create a new attribute processor or add an exclude list feature to the existing one.
- Transition from a markdown spec compatibility matrix to a YAML file for easier maintenance.
- Upcoming updates required for semantic conventions and configuration repo status.
- Challenges in maintaining CI for C++14 and C++17 due to dependency updates, particularly with Google Test and gRPC.
- Strategies for managing third-party dependencies in CI, including potential partitioning for C++14 and C++17.

## Action Items
- Nikhil to clarify the context of the attribute processor issue for further discussion.
- Mark to file a PR for updating semantic conventions when ready.
- Team to explore partitioning CI jobs for C++14 and C++17 dependencies.
- Doug to investigate Bazel dependency management issues and propose solutions.

## Participants
malff, Ehsan, Tom Tan, Nikhil Bhatia, Lalit, Doug Barker
