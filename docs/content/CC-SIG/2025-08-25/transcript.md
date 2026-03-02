SIG: OpenTelemetry C/C++ SIG
Date: 2025-08-25
Duration: 64 minutes
Zoom Recording URL: https://zoom.us/rec/share/JWnCjMxSx-AKcy-lj54sUN0AfdYROLW6sM0aej9owoYqB_0l3rk8bSr48Qn_hH4p.EAzRf22SYEj-QGal
============================================================

## Zoom Recording Transcript

malff 00:01:33 Hi, everyone.
Ehsan 00:01:38 Hi.
malff 00:02:05 Hi, Tom.
Tom Tan 00:02:07 Hi, Mark.
Yassan, and then Mikhail.
Nikhil Bhatia 00:02:12 Hi, Tom.
malff 00:02:24 I saw Doog, online earlier, so I think he would join.
Tom, do you know if Lady is coming?
Tom Tan 00:02:33 Let me check…
Yes, hey, hey, watch on? I need to watch on.
malff 00:02:46 Okay, great.
By the way, do you see my screen?
Ehsan 00:03:31 Yep.
malff 00:03:32 Okay, good.
Hi, Duke.
And how does it.
Lalit 00:03:41 Hi, hi Mark. Hi, guys.
malff 00:03:48 Okay, so… As you can see, I'm back from vacation.
So…
I have not been there for quite some time during the summer, so good to see all of you again.
I don't have a lot of things, I just, you know, added a few notes to the agenda based on what I've seen.
But, let me know if you have any specific
specific topic you would like to discuss? And, Nikhil, do you have any things you want to discuss as well?
Nikhil Bhatia 00:04:18 Yeah, actually, I want to ask something on a particular issue.
I will pause it if you're looking forward.
So, in this issue, I wanted to know that Whoa.
There is this… attribute processes, so…
Should I create a totally new attribute processor, or just add an extra, feature, like, it adds an exclude list process?
malff 00:04:48 Okay, …
I don't know if it's just from me or not, but the sound is not very loud for you, so we have trouble hearing you.
Nikhil Bhatia 00:04:58 Oh, sorry.
Can you hear me now?
malff 00:05:01 Yes, it's better.
Nikhil Bhatia 00:05:03 So, I was asking that, … In this issue.
it needs, totally, we need a new attribute processor, or else should I, just add an exclude list feature in that
Existing attribute process.
malff 00:05:23 Well, I'm not familiar with the context to… What issue is that?
Nikhil Bhatia 00:05:29 I shared that issue in the group chat.
malff 00:05:42 I see.
Nikhil Bhatia 00:06:15 Yeah, this one.
malff 00:06:16 Okay.
Nikhil Bhatia 00:06:18 So, it requires a totally new attribute processor, or else, like, in the existing one only, just add and exclude list feature.
malff 00:06:30 …
I don't recall the context, so I cannot answer it right now, but I can look at it and make some comments in the issue itself for later, then.
Nikhil Bhatia 00:06:42 Oh, okay.
malff 00:06:54 Oh.
Yeah, sorry, I cannot be more specific, but, anyone else? Do you have any topics to discuss?
Before we go into the… Typical, routine.
I guess not. So, …
As I said, I was away for some time in summer, so just coming back and looking at the different triples.
One thing I noticed that will affect us is that on the specs.
We have this spec compatibility matrix, which is maintained currently as a huge, markdown document.
Which is not very convenient, because every time one, language updates, a row,
It can cause merge conflicts with… if another language updates the same rule for the same feature.
So it's not very easy to maintain. And this is being broken down with a YAML file so that every language implementation, so OpenTelemetry, C++ is one of them.
will have its dedicated YAML file, to update the spec matrix. So…
The long story short, whenever we need to update that matrix, we no longer need to update the MD file, we need to update something else, so the process will be just a bit different.
When submitting a PR to respects to a bidvat.
Otherwise, it just looks exactly the same way.
…
Next item, I just also noticed that Semantic Conventions is doing a new release, and Weaver has done a new release as well, so…
I'm guessing that pretty soon, we also need to update the semantic conventions, which are generated from that.
So, just to be aware of it, when it is time, I would probably, …
file a PR for that just to update the vicinity conventions in OpenTeametry CPP.
And on the configuration side, still no news on when, the configuration repo itself will go to GA and, with a 1.00 release, so it's still in RC1 right now.
on the miscellaneous… so, the PR, I would say, for later, when we discuss the issues and PRs. One thing I noticed,
Duke also tried to update the dependencies that we have in OpenTelemetry CPP for
different third-party dependencies, like Google Test and Benchmark and whatnot.
And the question is then, doing that broke,
the CIA for C++14, because newer packages are expecting C++17, especially for Google Test and France.
So, it brings the question, how to organize CI so that we can Test booth.
And… I was hoping we can discuss that to have some…
See if there are some ideas on, what to do exactly.
Doug Barker 00:10:31 Well, we do have the files now in the install folder that specify the minimum version, so we could give better guidance and say, like, we support C++14, but only
with these minimum… Dependencies, and then everything else we would test against.
the later dependencies in C++17, but I think…
Probably the bigger question is, like, do we still need to support C++14? I think at some point, we'll have to drop it, right? Like, Google Test already has, and all the Google dependencies already have.
malff 00:11:08 So, the latest dependencies for Google tests now require C++17.
So, yes, if you take the latest Google test, you have to be on 17.
But there will still be people still using 14 for a while, I guess.
So, the question is.
Doug Barker 00:11:25 ….
malff 00:11:26 Instead of having, like, one, … Third-party dependency file, … for all of OpenTelemetry.
I'm wondering if we can have one file for C++14,
which lists all the minimum or latest requirements, one file for C++17, and so on.
So that when we… When we do a building CI for C++17, we use
one list of tags, and when we do a build for C++14, we use a different list of tags, something like that.
Doug Barker 00:12:08 Yeah, I think… I think that sounds reasonable. You're basically saying, like, what we have now with those, different version files, we would just set the expectation of what can be built with 14, and what with 17. Yeah.
It would probably take a reorganization of the CI.
malff 00:12:26 Yes, possibly, because the…
Well, there are a lot of… first of all, there are a lot of different CI's jobs right now, and possibly some overlap between them.
Doug Barker 00:12:39 And I don't know if anybody on the call is familiar with Basil, but, like.
Basil, we… we, specify versions for the dependencies, but in looking at it, they're not using those dependencies, it's pulling in, like, the absolute latest, Absol, and that's why, like, my, Google test, PR failed. So…
I don't know how to get Basil to…
Pull in the specific dependencies we're gonna look for, but….
malff 00:13:05 Okay. So, for Bazel, I've been looking at that, as part of a file configuration project, actually. So, there is one thing first… so, let me see if I can find the code so that we can follow that.
…
Where is this file that lists all the versions for every dependencies we use?
But the thing is, the dependencies which are mentioned here, for example, for Absal,
they're not correct in the first place, because if you look closely at the Basel build.
The first thing Bazel says… the Bazel tool itself says is that, hey, you told me to use version so-and-so, but looking at every other dependency, for example, looking at the dependencies for gRPC, I just found another version of Bazel, so there's a conflict, so I'm using the most recent.
So, the first thing I think we need is to fix the warnings reported by Bazel and actually put the actual version of each dependency, each third party that we actually use.
So that we would have a clearer picture.
And then, the next thing is, … For CMake.
We can decide in CMake to bid with whatever we like.
So it's… the choice of dependencies, in fact, in the CI job.
For Bazel, it's in this file.
So, … I guess the question is…
It's a matter of policy. Do we want to maintain the Bazel build, which is always up-to-date with the latest, no matter what?
In which case, Bazel would be only C++17 then.
Or do we want to, say, stay on, some older version, like the most recent C++14 or things like that?
But the issue being, We have only a choice of one.
One version for each dependency, so we cannot have different breeds concurrently on that.
And on top of that, this file is used by the Bazel Central repository itself to make a build.
And there, there is also only one neighbor there, so…
I think that for Bazel, we can decide to use the latest.
Doug Barker 00:15:26 I think that makes sense.
malff 00:15:27 Yeah.
Doug Barker 00:15:28 Because it seems like if somebody's going to be using Bazel, they'll be pulling the latest Google test or whatever, which already depends on C++17 anyways.
malff 00:15:37 So, I think that the issues you have seen,
in your PR is that this line, this line is a lie, because other dependencies are building a more recent version of Absol.
And that more recent version itself may require C++17 already.
Doug Barker 00:16:01 That makes sense.
malff 00:16:02 Okay.
Doug Barker 00:16:10 So I guess, Mark, just to summarize, so the idea is that we're not going to try to move to a C++17 minimum anytime soon. We'll keep supporting C++14, but we need to work on partitioning out CI and probably some documentation to say.
We're gonna test with the latest versions of the dependencies on C++17, and we'll test with the minimum versions on C++14.
malff 00:16:36 Yes, I would think.
We're stretched out.
Doug Barker 00:16:39 Okay.
malff 00:16:40 We've… Yes, Large.
Lalit 00:16:43 Yeah, sorry, I think I was not in… I was not in the complete discussions, I was… I mean, so just probably just wanted to talk about this.
I mean, so we agree that we're not moving to C++17, right?
We'll support C++ 14.
malff 00:17:00 Yes.
But we need to see how to support both in CI, because right now it's, … It's unclear.
Lalit 00:17:08 Yeah, I mean, I think I agree to that. I mean, just because that… if we see the dependencies, protobuf and gRPC, they are basically the dependencies of OTLP exporter.
malff 00:17:22 Yes. So somebody who is using….
Lalit 00:17:25 a non-OTLP exporter, with the OpenTelemetry C++, they should not be bound to use C++19, just because
OTLP exporter has the dependency of C++14, so…
So, I mean, I want to say that we should support C++14.
For anybody who is using a non-OTLP, I'm not saying….
malff 00:17:49 And even for OTLP, People should be up-to-date, but some people will not be.
So, there's also the question of supporting even the OTLP exporter with an older version of gRPC, for example.
Lalit 00:18:05 I think I…
I mean, I'll be okay if we support just for the latest versions and not C++14, and….
malff 00:18:14 Okay.
Lalit 00:18:15 With the assumption that people are going to upgrade to the latest versions of gRPC and Protob if they want to use our…
our open telemetry with OTLP. I mean, that would be a bit complicated, I mean, I think that if you're going to support the old versions.
And also the new versions, and then have the separate CI for C++14 and C++19.
malff 00:18:34 Huh.
Lalit 00:18:35 with OTLP in….
Tom Tan 00:18:37 Hmm. I think that….
malff 00:18:41 Can I wait on.
Tom Tan 00:18:42 I mean, the requirement comes from, like, Google Test, which maybe is more basic than
like a gRPC thing around, so….
Lalit 00:18:50 I mean, Google Tests and Benchmark, I mean, I probably don't want to upgrade our application code just because the testing frameworks are…
Using C++. I mean, should be okay to use the older versions for…
Testing the OpenTelemetry SDK and, …
With the older versions, which support C++14, right? Go for global test and benchmark.
malff 00:19:14 Yeah, that should be okay. And these are still a development dependency.
Lalit 00:19:18 Yeah, exactly true.
malff 00:19:18 resulting most is AppSear, because gRPC will need Absol, and AppSear itself will need C++17 now.
Lalit 00:19:28 Yeah, okay, yeah, with Dexcel, if…
They want to use with Epsil, and then…
That means that SDK is going… is going to use Epsil.
Yeah, that would be tricky.
malff 00:19:41 Well, the… so, the SDK itself is still using the internal web server, …
Code, because we split it apart.
Lalit 00:19:51 Oh, yeah.
malff 00:19:52 But my point is, yeah, but my point is, someone who wants to use the latest version of gRPC,
will, because of gRPC, we'll have to use the latest version of Absol, and therefore C++17.
Lalit 00:20:06 Okay, … Which should be fine, right? I mean, if we use the latest versions of gRPC,
if we support the latest version of gRPC… I mean, if we support C++17 with
With OpenTelement 3 OTLP exporter, so that means that
They would be using the latest version of GRPC.
malff 00:20:34 So, I think we can make it work. The only thing… the only question I see remaining is, we have submodules in third party.
And a submodule can only point to one label at a time, I guess. So, the question is,
What version do we, do we use for those submodules?
And, assuming we use the latest version for,
I don't know, EnnumenJSON, or whatever, or OpenTelemetry Portal. If we want to do a build with a different version.
would have an NCI to explicitly install the.
Lalit 00:21:11 Thank you.
malff 00:21:12 Proper package, as opposed to depend on submodules.
Doug Barker 00:21:16 Yeah, and the same thing exists now, because we're only reading that third-party release tags file, so we're… and that… that's just fixed in CMake, so if the submodules aren't checked out, then it's going to fetch those tags from the repository, so we would need to add some kind of logic.
at least in the CMake side, to say, like, if you're building for C++14, then pull down these tags. If not, then pull down these other ones.
malff 00:21:41 Nope.
Doug Barker 00:21:41 So that adds some complexity.
malff 00:21:45 So, yeah, so could we have…
instead of one third-party release file having one third-party C++14 file, one third-party release C++17 file.
With the proper tags that are compatible with C++14 and 17.
Doug Barker 00:22:06 We could, but it does get complicated with the submodules if you want to still use submodules. We could also just not have submodules, that's what Protobuff did. So they just went to the fetch content model and got rid of all their submodules, which is… I think it's nice.
malff 00:22:25 Yeah, using either a local package or fetch contents directly, at least that would allow to have
different builds in parallel in CI, totally independently.
Okay.
Doug Barker 00:22:41 I guess if I ask, …
you know, just a general question about what do you guys think is the right policy? Because at some point, you know, we'll have to drop C++14. I'm sure at some point you drop C++11. Like, what is the….
malff 00:22:55 Yes.
Doug Barker 00:22:55 what is the policy for the project on this? Like, what… how do we communicate, even to our… ourselves and to others?
And will C++14 be dropped?
malff 00:23:08 …
I don't think it's clearly defined anywhere, but I would guess that is related to the support in all the different platforms that we have.
So, the day Ubuntu so-and-so finally drops the latest
the oldest version that is using… that was using C++14, then by that time, we would no longer support C++14.
And… but… I think there's a difference between
adopting C++17, that can happen right now, and in fact, we already do support that, it's just that we don't fully test in CI.
We've got the latest version, but we do support it.
Like, we support even 20, 25, and so on.
But the… Removing support for an old, …
C++ standard, that takes more time, because we have to wait for all the different usage to die.
Namely, all the different platforms to upgrade to.
To a place which is sufficiently new, so that we no longer need to support that.
Doug Barker 00:24:20 Yeah, I think that's… that's…
in principle, I think that's similar to the Google policy. I think that they tie it to…
Some latest, release of, of, or supported long-term release of,
Ubuntu, or one of the Linux platforms.
So, maybe we could look at that and see if there's some way to document it.
Lalit 00:24:41 Yeah, probably good to have some kind of consolidation to see all the, I mean, mostly use Linux distributions, their LTS versions, what's the current default.
C++, I mean, our current, default C++ mode they use.
Try to see if all have, all the, all the…
current LTS with the default C++ GCC installed, what's the C++ mode? If all have moved to C++17, then at some time we can start thinking about that.
malff 00:25:16 Yeah.
Doug Barker 00:25:19 Yeah.
That makes sense, because just looking at what Google tested, there was just a PR real quick, just change it to C++17. I think Benchmark did it on a point release, too, so, you know, they moved pretty quickly. I think they probably just leaned on having that policy, you know, up for a while, so people will expect it.
malff 00:25:46 You know, it gets complicated, because the…
Where is the platform, first of all, like Ubuntu, so-and-so? Then…
to at least the, the worker,
job in GitHub. The worker image provides several compilers, like GCC version this, that, and that.
And then, a given version of GCC itself will support different, C++ standards. So it's…
Just keeping track of what is the latest standard, …
He's by himself, following the breadcrumb, of the breadcrumb trail, but, …
Eventually, when we get to the point that we…
not only we no longer need to support it, but also there will be a question of, to support it, we would need to test it, which means we need to find a compiler somewhere that will still supports E++14 and so on.
Lalit 00:26:46 Other thing would be, like, once we decide not to…
once we decide not to support C++14, does it mean that we'll start using C++17 features there, or just mean that we're not going to test it?
But then we won't be even using C++17 features.
malff 00:27:03 Yeah.
Probably that we are not going to test it, the same way we don't explicitly test C++11 right now.
Lalit 00:27:12 Excellent.
malff 00:27:13 But we all know that it will still work for a while, and…
We also know that there are some people who are still using C++ even today, so….
Lalit 00:27:23 It's just that it's not reported, but ….
malff 00:27:26 I don't see… I mean, we'll have to…
Write some special code using a special feature to…
use a special syntax only in C++17.
Trying to really break the code itself.
And this is not likely to happen soon.
Okay, so, for the… for the basal part?
I think we can… we can agree that Bezel will be on the most up-to-date.
And I think this is consistent with the way people are using Bazel anyway.
So, in that case, we can move all the Bazel builds to C++17.
and know you support C++14 on Bazel. And for CMake, I think we can, can support both, just to have good test coverage.
Assuming that we… each CI job will know how to install the proper package.
To, to test with a proper version.
Doug Barker 00:28:36 Yeah, maybe we, start a thread in the repo or something about the, what to do with the submodules, because that'll be something we need to decide on, like you said, Mark.
malff 00:28:45 Yes.
Doug Barker 00:28:46 set the submodules to the latest versions, or the C++14 versions, or get rid of them altogether.
malff 00:28:54 Yeah, that could be a possibility too, I mean… But…
It will be… it will be forcing people to install all the dependencies.
But it will also simplify a lot of complexity as well.
So, yeah, to discuss, …
Any… I also had another topic, which is to decide if we need to do an X release.
Which raised the question of when, and the second question is, do we want to wait on a specific PR to be merged before doing that release?
I guess if we have a lot of CMake changes.
I think I would prefer to have the CMAC changes done first, and wait until the CI is stable before making a release.
Because if we do a release in the middle of some manufacturing, it's more risky, and…
And we risk breaking something, and we will have something that…
People we use, and then by the time they first report some defects, we will have some code that has changed already, so it would be harder to
To troubleshoot and investigate.
So, my preference would be to
finish whatever we need to do with CMake.
And where is after that?
Any… any comment on that, or…?
Doug Barker 00:30:26 I think I missed it. What is the scope of the CMake changes that you want to get in, Mark?
malff 00:30:30 Well, the… just that upgrade to C++ 14 or 17, and the upgrading versions.
To finish that before we make a release.
Doug Barker 00:30:42 That one, yeah, I'll have to think about it. That could get complicated, like I said, based on the submodules, and then having to handle
the two different cases, which is adding some kind of, like, an introspection of what people are setting for the C++ version, and what do we default to.
malff 00:30:58 Yeah, okay.
Doug Barker 00:30:59 So…
I guess my thought was, like, if we're gonna… we could either not do the upgrades of the dependencies in this release, or if we do, just do them to C++14, whatever the latest version
support C++14.
malff 00:31:14 Okay. And….
Doug Barker 00:31:15 I think then the only blocker at this point is to figure out why… or how to fix the Bazel build.
malff 00:31:22 Okay.
So we…
This is still August, so I'm guessing that… I haven't looked at how many PRs were emerged this summer, but I guess we can wait a bit, and wait until maybe, like, mid or late September to do a release, so we have time to figure this out.
… Any other general topics before we dive into issues and peers?
Okay, I'll start with the PRs, and we'll see if we have time remaining for issues at the end.
That should be quick.
So, the first one is, yes, what we just discussed, basically updating CI to the latest release for Google Test Benchmark and France, including gRPCN and everything else.
So, … We… we… We'll figure this out, …
I'm sure we can… we can clarify things. …
The next one, so, as you may remember, I have this…
very old PR with a lot of things for the file configuration.
This is actually… so let me show you…
This pair used to be huge, it only has 2,000 lines remaining.
And the things which are remaining are basically to add some tests.
So…
as a reminder, these are all the parts which have been merged now. The part which is currently for review is to add some functional tests.
So it's purely testing, there is not even code change involved.
Apart from two minor cleanup.
And the next PR I will have is to…
enable the CMake build and CI, for all that, and the one after that will be to enable the Bazel build.
But BazelBuild is a bit delayed because, there is a dependency on Rapid YAML, which by itself, does not… itself does not support Bazel yet, so we have to, to…
support Bazel Vare, and Rapid YAML also has a dependency on C4 Core, which is a different module.
in a different repo, and this one also will have to be ported to Bazel.
So this is… this is in progress. I actually have this, all working locally.
So, I can do a full CMake bit locally, even with RapidDML, but this needs to be pushed to the Bazel Central repository, so that we can use it in CI in our make files.
So… long story short, for this…
For VPR, no, this PR.
Sorry, for this PR…
this is just to, to add some testing, and that… it should be, very easy to, to review, I hope. And the two PRs coming after that will be purely CMake and Bazel, and then, the whole thing will be done. So it's… it's getting close.
Yes, this one, Duke, so thanks for the, for the PR, I've seen this as well. So…
It looks okay to me. I didn't, approve yet, but, I will, I will do this soon. For my first reading, it looks okay.
I've seen that you have done a lot of cleanup to…
In various places for that, so thanks. And indeed, it also improves, troubleshotting, when we… people need to understand what everybody's doing, so I think it's a good change.
Doug Barker 00:36:01 Thanks.
malff 00:36:05 Yeah, this, … I will take a second look, but this should be ready to go.
Resource detectors, so yes, … Let's sweet.
Oh, Nikila, I didn't realize it was you, sorry, so…
So thanks, thanks for the PR, first of all, and yes, this is making good progress, so that we have all the…
More resource detectors.
… I don't remember who… Lalit, Tom Morduque, do you remember who…
did the review for Nikhil, for the… all the peers related to… resource detectors.
If you could take a look at this one as well.
Lalit 00:36:59 Yeah, I think we all did that, so I think we can continue, and….
malff 00:37:03 Okay, and I would take a look as well.
And likewise, when this is done, most likely there will be some things to add to the YAML configuration itself, because then we will need to
Support resource detectors, which we don't have right now.
Well, that should be easy to analyze.
So, Nikib, yes, thanks, and we'll look at VPR.
Oh, so those are two old experiments with, Copilot.
So… In the co-pilot story, I think, EZCLE has finally been fixed, so, those are not…
Those PRs are not blocked anymore by EZCRA.
You know, it's pressing.
… I've not looked at this for a while, so…
a lot, it was… yeah, I think it was you playing with that. Do you still….
Lalit 00:38:18 Yeah, I can… I can….
malff 00:38:19 I can move.
Lalit 00:38:20 Yeah, yeah, I'll do that, yeah.
malff 00:38:22 Okay. But just to clarify, so were you looking at what Copilot can do to see if it can be useful, or….
Lalit 00:38:30 Which is….
malff 00:38:30 Is this an experiment, or…?
Lalit 00:38:32 I have been doing it in the… not in C++, but definitely in Rust. I've been doing it extensively, and it has been definitely productive.
malff 00:38:41 Okay.
Lalit 00:38:43 So… But that means… that doesn't mean that we just, …
I mean, anything coming from Copilot, I think we definitely review it more thoroughly.
Just to ensure that it is something which is… which… it should not add something which is not…
Part of the fix, or anything which changes something, something else, so yeah.
But definitely, for more… most of the routine things, it's more helpful, and for simple, small features, it has been helpful.
malff 00:39:09 Okay.
Lalit 00:39:12 Yep.
malff 00:39:14 Yeah, I've never used it, so I'm…
I think for things which are very repetitive, like, okay, write some unit tests to test an API call and things like that, it probably can be useful if it can automate some things very repetitive.
I'm a bit concerned about changing the production code, and to make sure that we really, really review what's going on.
Lalit 00:39:40 Yeah, I mean, for the code, which… I mean, like, for me, like, if I… I'll want something…
to be implemented by Copilot, if I know what has to be implemented, and I really don't want to create a PR specifically for that, and do all the groundwork.
malff 00:39:57 So, not for anything which I am not sure.
Lalit 00:40:00 how to implement. I don't want Pia to do that, or I don't want CoPiri to do that.
But anything which I know what changes are required in VETL files, then I can…
something, instead of me creating a PR, if I can directly ask Copilot to do those changes along with the unit test, I think it should be good to do that.
malff 00:40:18 Yeah, so basically you have to know what to do, and then guide Copilot.
Lalit 00:40:22 No, yeah, as of now, I think that's… that's the right, right set of…
tasks which we should give to Copilot?
malff 00:40:30 Okay.
Yeah, well, let's, let's try it and see how it goes.
Lalit 00:40:36 Hmm.
malff 00:40:37 So, yeah, so the, the previous… so…
the… when this thing was announced, like, I think it was, maybe May or June, I don't even remember.
There was absolutely no…
discussion or no explanation about what Copilot was and how to use it. And one thing which has been clarified since then is that using Copilot is only for people who have alright access to the repo in the first place.
Which means maintainers.
So, my initial concern was that,
Well, if we can… if someone, just do… does a random PR instructing Copilot to do random things, it will just,
increase not only the workload that we have on us to do the review, but also the risk to the repo. But this is, … this is not a concern, because this is only used by maintainers, in fact, so…
I made my piece with Copilot, basically.
Lalit 00:41:40 Yeah, thanks, Mark. Thanks for raising a valid point at a valid time, yeah. I agree.
malff 00:41:50 I guess for next PR is exactly the same thing, it's a compiler thing.
Yes.
Lalit 00:41:55 Nope.
malff 00:41:56 So, yeah, likewise, let's, let's see how it goes.
There is also VPR from Owent, so this is… so…
as far as I understand, there is a problem, because if, say, you've, …
you record a span, and you put some attributes there as a string which are not properly rotated strings, then the string is bogus, and by the time we send it on the wire, typically to an OTLP exporter, then there will be some issues.
And, of course, this is difficult to… to investigate.
Because it's an issue with the instrumented code, which is producing bogus data.
But by the time we see it on the Y, it's way too late, and it's also difficult to find out where it is coming from.
So…
My understanding of VSPR is that Owent added some code to actually help debug things and test the validity of things.
… So, which is good, my concern is on the… First of all.
The possible, performance, impact of that, because we don't really know.
And also, …
I don't recall where he put, actually, he did put the check on, … the UTF8 validity itself.
Basically, what I was thinking to Tesla to say.
So the issue was found with the OTLP exporter, Let's see, SDK…
Yes, so we just changed the OTLP exporter.
But…
If someone produced a bad attribute using the console exporter and output stream, it's equally broken. And in this case, it would not be detected, because it would be only checked when using OTLP.
So I am wondering what is the proper place to push those checks, and whether it is really
Down at the exporter level, or if it's at the top, on the processor level, when the application is actually
Recording a trace, or recording another event, and things like that.
So, to discuss. I will put some notes and some comments. I was just wondering if any of you had some chance to look at it and had some comments on the…
On the general, design of it, not even looking at the code yet.
Lalit 00:44:44 It's for a non-UTF8 character set, which can… which, which somebody can add? Is that….
malff 00:44:50 Basically, when you add a string, you can add anything. It's a chart pointer, but you… it doesn't say exactly if it's only ASCII or if it can be UTF8.
Lalit 00:45:03 Hmm.
malff 00:45:03 And if it is UTF-8, it needs to be properly,
properly form UTF-8, just not… not random bytes.
Lalit 00:45:12 Okay, … Hmm.
Okay, yeah, let me go through this, I think, probably anywhere.
Saw the CR and the need for this, yeah.
malff 00:45:27 So, I think, I think there is a need for it.
the question is where to put that code, and I was more thinking, like.
At the top level, like at the… at the processor?
Especially because when the error is found, you still are in context in the application call stack, so it's easier to find out where in the application the data is coming from.
And also, it will work with any exporter, just not the OTLP exporter.
Lalit 00:45:58 Hmm.
At the processor level, only, only, I mean, I'll be a bit cautious if it is coming in the hot part of, …
… Of the, of the app… at the application context.
I mean, in case of something which is added in an exporter, we know that it's not something in the hot part of application, because application is just going to give it to the batch exporter, and then batch exporter. It would be… this would be executed in the thread of batch exporter.
malff 00:46:27 Oh, yeah, because food.
Lalit 00:46:29 That way, that way, I think this gives a benefit in terms of performance, that the case application would not be blocked for that.
malff 00:46:36 Okay, yeah.
Lalit 00:46:37 So, for that….
malff 00:46:39 Because the battery exporter has its own thread, so it would be… the thread will be in the exporting thread itself.
Lalit 00:46:45 Yes, it would be.
malff 00:46:48 Okay.
Lalit 00:46:49 But yeah, let me, I think, go through this PR, I think let's… probably I can put some comments here.
malff 00:46:55 And, I think I went to find it.
Why the goal?
Yeah, early dry, so….
We should take a look and not forget it.
Oh… What was that?
Tom, do you know if that PR is still valid, and…
What we should do about it?
Tom Tan 00:47:26 I haven't looked at it for a while, so I need to… Take some of those turns.
malff 00:47:32 Okay, thanks.
Tom Tan 00:47:35 Thanks.
malff 00:47:41 And this one, yeah, so I guess… I haven't seen any….
Lalit 00:47:49 No, no update on that, I think.
malff 00:47:52 Yeah, no updates since Fiverr.
Lalit 00:47:54 probably… probably we need to pick… I think, Tom, you already picked what.
Tom Tan 00:47:58 Yeah, I plan to pick up this one, yeah.
Lalit 00:48:00 Yeah, so with the co-pilot, I think one of the, this… one of the items which is fixed by this PR, I think.
Tom has.
malff 00:48:07 Yeah, because Cop… yeah, Copilot is looking at the Carolina TT limit, one of them, yes.
Lalit 00:48:14 Yeah, which is important, actually, I think, from this PR, that's pretty important to have coordinated limits configurable, so….
malff 00:48:20 Okay, so let's…
I think we can keep it open so that we don't forget it, but we'll probably need to pick the…
cherry-pick the different code that we need from it, because the PR itself is too old and has conflicts, so it's not likely to be merged as….
Tom Tan 00:48:38 Yeah, yeah. I will create a new one, let me cherry-pick some changes from here, yeah.
malff 00:48:43 Okay, yeah.
Tom Tan 00:48:45 Thanks.
malff 00:48:56 No, excuse me.
I know.
Lalit 00:49:01 Phew.
malff 00:49:03 And this one is on me, but I'm making progress on it. It's, thanks to Duke for all the reviews, and it's, it's coming a long way, so…
I'm hoping to… to close that once the make files are fixed.
… Any PR missed that you want to discuss?
Nope.
So, which brings us to existing issues.
This one was filed today. It is, raising an interesting point, like, okay, someone has a…
A metric exporter, which is exporting things periodically, and the application is shutting down, and it wants to have a last export.
Before going away. And the question is, how do you do that?
Lalit 00:50:05 We support it, right? I mean, as part of meter provider shutdown, we'll do one last export.
malff 00:50:15 I think we flush the queue of whatever has been collected, but we don't collect one more round.
Lalit 00:50:21 Okay, we do a plush, okay, okay.
Then, probably, we should see if that can be supported instead of
providing some manual trigger meter reader to run. Yeah, I think if it is not there, then probably we should… we should…
Or, or they can manually do a force flush, right? They can always do that.
Just invoke the… Yeah, no, even, even, yeah, sorry, yeah, even Force Plus will not….
malff 00:50:46 It will not collect things.
Lalit 00:50:48 Collect the things you.
malff 00:50:51 Absolutely.
Lalit 00:50:51 Can you answer it?
malff 00:50:52 I, I think… this… so… There is a use case there, or is some… so, …
The question is what the spec says about it, and if we should file an issue on the spec to clarify this.
Lalit 00:51:07 Yeah. Aww.
malff 00:51:08 Possibly, like, having a…
A parameter on the flush to say whether we do a last collection or not, or things like that to, ….
Lalit 00:51:16 No.
malff 00:51:18 To clarify the behavior, but it's, … it's interesting.
Lalit 00:51:22 Yeah, I think I remember that initially we did support that, like, as part of shutdown, do a one last
X….
malff 00:51:30 No, that's correction.
Lalit 00:51:32 We did say, I think we did report one last collection, and…
Then, I need to check the code, probably, I just lost the context, just let me see.
….
malff 00:51:43 So the issue with that is that, because of callback, it can take forever.
Because when you invoke the callback on each instrument, you don't know
How much it can take, and the application may not respond by then.
Lalit 00:51:57 A callback will be for async, async, async thing, and… okay, yeah, so… Hmm.
Okay, yeah, possible. I agree, yeah.
malff 00:52:09 Okay. So yeah, I think it would be better if…
If the spec could clarify what we should do, and….
Lalit 00:52:16 Hmm.
malff 00:52:17 And probably that should be an issue in spec, so that every language does something… consistent.
If we do that.
So… I'll keep it open for now, but we…
I'll make some notes to see if, well, to mention the spec.
… Boris process, yes, so…
Duke, as you mentioned, so today, I don't even remember in which version we have, we are, but, …
So today, we must be on version 22-something, and…
some people could take the 1.22 release, which is the latest tag, or they could take the content of the branch in main, and it's hard to make the difference, because both are using the same version number.
And so, maybe we should…
name the branch 23 by the time we, we make a release, so that…
It will be 23 in Maine, and by the time we make all of these, it will be 23 with a label.
So that can, … makes things…
Better for clarity, because then it would be easier to make the difference between
A label and a bid from the main branch.
So yeah, I think we can do that.
The only minor thing, is that…
If we do that, we will need to make… to change the version about twice, when making all these.
Lalit 00:54:02 Yeah.
malff 00:54:03 And then one more time with a different commit, when we…
open the… the branch… opened the tree for the next release, basically. So it's, it's two PRs, it's not for the two PRs, it's two…
Reviews that will need to be approved right away.
Otherwise we… because we should not have PRs that just gets… get in the middle.
But, you know, we can… we can do that.
… Duke, was it a correct summary, or…?
Or did I miss also something else?
And yeah, there is also the question of having a dev suffix or not, so that will increase even more locality, because if we ever see a bug report with something dev.
Even in 6 months from now, we'll know that 23Dev actually meant the main code, as opposed to 23…
Which is a… Could eventually be released.
So, yeah, we can… we can do that. It would just make two commits that would… both of them will have to be approved by the time we do all these.
Doug Barker 00:55:26 Yeah, and this approach for the dev, I think, is similar to what the Python project does, so when you get the telemetry, you can see that it's definitely on the dev branch versus an actual release.
malff 00:55:42 Yeah, huh.
Basically, I'm a Freud, … Any… Comments and concerns?
From other people, if we… if we do that.
Lalit 00:55:53 No, I think I agree on this, yeah, that's the right approach.
malff 00:56:05 Okay.
This one, I didn't…
I had a chance to look at it, so I don't know what it is.
…
Or maybe it's a surprise people need to mess with the metric storage. I would think this is just internal to the SDK itself.
I'm a bit surprised what, what Vanid is.
Lalit 00:56:42 No, even I haven't gone through that, I'll go… I'll have a redone this year.
malff 00:56:47 I think this is our…
So, we have this cardinality limit, …
And I guess at some point, people want to just purge very old… Records, so that we…
The metric storage is not poisoned by very old labels, never used again.
Lalit 00:57:10 Deletion from the… or expired, unused labels, or just deletion from the storage. Yeah, I think that's…
That's one of the limitations of the storage. It does not really do any purge.
Yes. So, probably, yeah, it's something…
I know it's not just C++, I know there are other languages also which does not do this.
malff 00:57:33 Yeah, it should be common for everyone.
Lalit 00:57:34 Yeah, it's… It's mostly Korea. I think it's kind of a valid issue, yeah.
malff 00:57:39 Yes.
Lalit 00:57:40 Sometimes, yeah.
malff 00:57:43 Yeah, or Persia. Some kind of time.
Lalit 00:57:45 I think that's… that's… have been lots of discussions on this TTL expiration policy and all those things, but yeah.
malff 00:57:51 Yeah. Have to see something on… So, yeah, so likewise, I mean, we need to… to have respect for that, so to know…
What to do.
Lalit 00:57:58 Yeah, I don't think it's more of an internal implementation.
Specs will not talk.
When we should… expire the old…
Labels, and… it's more of an implementation, but yeah, no harm in asking.
there are any… Comments on it, it's discussions which can be
But ideally, most of these languages are taken as an internal implementation.
malff 00:58:27 Okay.
Lalit 00:58:28 Just that their memory keeps on increasing because the old…
Labels, or… I mean, they're not getting removed, so….
malff 00:58:35 Well, I guess first memory was increasing forever, then cardinality limit was invented to prevent that.
But then, everything goes to the default entry in Cardinality Limit now, so… Yeah, exactly.
So this is the next step, to actually purge very old records.
Okay.
So, to, yeah, to discuss.
… This one, which is actually older… …
I'm very surprised that we see that using the C++ code, so…
I'm wondering whether there's a badcast somewhere, and…
Whether it's a usage issue, or if we already have a bug, like, very similar in the code.
Lalit 00:59:45 That looks to me some kind of use after free, or…
I mean, something like this is happening here, probably, that… …
Some handler has gone out of scope, and we're still trying to use it.
So it's not able to find the actual implementation.
malff 01:00:03 Oh, you mean the callback has gone out of scope itself?
Lalit 01:00:05 Yes, it looks like.
malff 01:00:07 Oh….
Lalit 01:00:07 Would you consider?
malff 01:00:08 Yeah, and oh, and we have also… so this is, using asynchronous instruments, so yes, there is also the question of when you create an asynchronous instrument, you need to hold on the….
Lalit 01:00:20 Yeah, the callback….
malff 01:00:21 Return itself for a while, otherwise it goes away, and then you no longer can call it.
Lalit 01:00:27 Yeah, so the callback should remain the… in scope, the handler, I mean.
The handle to the callback till… till the program is… It's running here.
malff 01:00:39 Okay.
Lalit 01:00:42 I think it's documented somewhere, it is… we have documented also this… this requirement.
malff 01:00:52 Okay, to investigate, I guess.
Lalit 01:00:55 I can… I can just… probably you can assign it to me if you want, I can just have a look into this.
malff 01:00:59 Okay, thanks.
And there is this very old one, we discussed it a couple of times. …
At some point, we had one behavior with Prometheus and timestamps that we fixed, and this reporter wants to get the old behavior back.
And I'm not quite sure which one is the proper one, because I'm…
I'm assuming that if… when we fixed it, it was to…
To be more compliant with respects, so…
I guess to… we need to still take a look and investigate.
Lalit 01:02:01 Hmm.
malff 01:02:12 Maybe this is really… well, we have to see the proper use case, but…
Yeah, maybe this is related to adding metrics twice.
Which seems to be what David, mentioned.
And so… … I'm accepting it just because we need to…
investigate, not sure if this is, … Either a usage issue, Oh, come on.
I have a usage issue recording now.
In, OpenTelemetry.
And… You know.
Mitars with Davis 1.
Should we discuss it?
And I think this is it for, new issues.
Lalit 01:03:21 You're….
malff 01:03:21 I haven't seen any comments on old ones.
An issue that either I missed or you want to discuss?
Lalit 01:03:36 Not from my side.
malff 01:03:38 Okay.
So, I hope you had some, a good summer as well, and some vacation for the one of you who
Took some.
So, Heimbach.
And, … I guess we'll see you, all of you online.
-Oh.
Lalit 01:04:05 Yep.
malff 01:04:06 Very soon, so…
Thanks all for attending. This is getting late here for me, because it's 11 PM now, so….
Lalit 01:04:13 I guess it's time to close the call.
Okay.
Tom Tan 01:04:17 Thanks, everyone.
malff 01:04:19 Well, thanks, everyone.
Nikhil Bhatia 01:04:20 Everyone.
Tom Tan 01:04:22 later. Bye.
Ehsan 01:04:22 Thank you, right?
