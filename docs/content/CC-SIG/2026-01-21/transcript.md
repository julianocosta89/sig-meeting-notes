SIG: C/C++ SIG
Date: 2026-01-21
Duration: 8 minutes
============================================================

## Zoom Recording Transcript

**malff** 01:34 Hi, Tom.
**Tom Tan** 01:38 Hi, Mark.
**malff** 03:34 Yeah, so, Tom, thanks for the reviews on this, Bazel thing.
So CI is finally working now, and all the pending PRs that were blocked because of that
I've been merged today in the main branch.
**Tom Tan** 03:51 Thank you for the fix.
**malff** 03:54 Yep.
So, actually, I wanted to discuss that, because with that fix, I saw a couple of interesting things.
So…
GitHub itself was broken, so that it picked up a different… this version of Bazel, even though we don't want it, so this is… there is a workaround for that.
But the other thing is, OpenTelemetry CPP, the build is broken with Bazel 9.
And this has, it's working in many places.
My understanding is that Bazel9 changes a lot of things to, related to C++ in general, and on top of that, also changes things related to protobuf.
Because it has a Prodo-C compiler embedded in Bazel and things like that, so…
All that to say, by the time we need to migrate to Bazel 9,
we… we may have some, some work to do to clean that up. It will be just…
Just not a straightforward upgrade.
And the other part which is, affecting us is that…
Because you need the most… very recent package for a lot of things, including gRPC and protoperf, all the recent packages only support C++17 and not C++14.
So… we… at some point, I think we'll have to…
to see what we do for C++14.
Because,
It's likely that we won't be able to support it anymore with Bayes on 9 in the long term.
**Tom Tan** 05:35 Okay.
**malff** 05:37 So… No, nothing to decide now, but just to be aware of that.
And…
With Terzovia, basically.
Especially this part.
Boom.
I don't have specific items to discuss otherwise,
Do you have, anything special?
**Tom Tan** 06:19 I think I have one request. There's a fake about,
building protobuf library into… into shared library from O, and there's a PR there, and I think it will… it will be great to include… include that for the next release.
I think the PR is still under caution review. I took a look, and it mostly looks good to me.
I think that will become a real issue once the user starts to…
To, use our library from multiple components.
In the same process, yeah.
**malff** 07:05 Okay.
So it's probably both as a shared library, a VSPR?
**Tom Tan** 07:16 I think so, yeah.
**malff** 07:19 Okay, let me trade.
Okay, I will take a look at it.
**Tom Tan** 07:31 Thanks, and yeah, that's all from my side, and I need to drop off early today for…
**malff** 07:37 Okay, and likewise, I need to drop early as well.
**Tom Tan** 07:40 Let me…
**malff** 07:41 Let me mug this.
You have…
I need to be gone at 6.30, so I need to leave sooner today. Otherwise, I haven't seen anything recent,
Someone reported several issues on the ETW exporter.
Ready to clean up.
**Tom Tan** 08:08 Yeah, I will take a look at the HTTS, by the way. Thank you.
**malff** 08:13 Okay, so nothing urgent anyway.
**Tom Tan** 08:15 Okay.
Okay.
**malff** 08:20 Okay, talk to you later, Van.
**Tom Tan** 08:22 Thanks, Tom. Yeah, no problem.
Bye.
