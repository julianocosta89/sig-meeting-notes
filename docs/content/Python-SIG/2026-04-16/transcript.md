SIG: Python SIG
Date: 2026-04-16
Duration: 50 minutes
============================================================

## Zoom Recording Transcript

**Aaron Abbott** 01:13 Alright, hello folks, how's it going?
**Ridhima Satam** 01:18 Erin, that's good.
**Erdenesaikhan Tserendavga** 01:27 Hello, everyone.
**Aaron Abbott** 02:06 We'll just wait another minute or so.
Ricardo's still gonna join.
If not, I'll get started running the meeting.
**Riccardo Magliocchetti** 02:38 Hello?
**Aaron Abbott** 02:40 Oh, pericardo.
Ricardo, do you want to run, or…
**Riccardo Magliocchetti** 03:41 Yeah, I'm trying to set up. Fantastic one moment… Okay, can you see the screen?
**Aaron Abbott** 03:54 Yeah, here we can.
It's pretty wide, but yeah, there we go. Thank you.
**Riccardo Magliocchetti** 04:04 Okay, so welcome, everyone, to this week's Python SIG call.
Please have yourself as an attendee to the emitting notes.
I'm sharing the link in the chat if you want it to attend.
Also, please feel free to add any topic you want to discuss.
Yeah, let me write myself… And we can start… Okay, so triage.
I have to say this week, I haven't look at March.
Into the… pictures we got… Biz… what I think are old ones. We already seen that, this, like, last week.
Okay, then we have a bunch of… we think… PR's done from, automation?
Or maybe not.
But… Yeah, I see this. Got a list of reviews.
Or interaction?
Oops, sorry.
And… bumps from the PandaBot, okay, oh, this is interesting, from Uldamila.
I lost this one… Oof.
Jenna.
Okay. If you haven't seen this, the Mila, openAppR, creating a… a weaver helper, so we can… test the exported, telemetry against Weaver.
I think me and Lucas already approved.
Yeah, I think I'm… I've still left a comment about the… That's the situation, because, like, ins… well, I can show a bit.
Unless the Demilizer and… She wants to… No, presentier.
So, yeah.
So, like, in CI, we're installing Weaver, the binary version from the… Where it is this?
And if Weaver is installed… We should run some… test, but they… the fact is that when it started, we were only on Linux?
And… I think we have issue with, And, like, we were, by default, I think at least in our… on… as a JetBC server?
And so, like, for testing that, we also need the gRPC exporter.
When testing, but I think the issue is that… We don't have binary wheels for all the platforms.
And so, what is the common? Okay.
**Aaron Abbott** 07:47 You mean for gRPC or for Weaver?
**Riccardo Magliocchetti** 07:50 For gRPC. For Weaver, we have the binaries also for Windows, I feel.
There's a com… well, there was a comment somewhere, but, like, I was, like.
as Ludmila configured right now, I think we are not running the… this Weaver integration test.
Like, we are not testing this locus?
**Lukas** 08:18 Oh, sorry, I didn't mean to interrupt. You can… I was just gonna say, we can… once we have the JSON exporter that doesn't have any dependencies, we can just use that for the Weaver tests.
If we wanted to avoid gRPC.
**Riccardo Magliocchetti** 08:39 Yeah, like, I don't remember if we've, I've had the HTTP… Listen?
Maybe Yasmin, or… like, is…
**Lukas** 08:53 I think it also… It's reading from files, so once we have a file exporter, we can also just do that. That would be even better.
**Mike Goldsmith** 09:04 Yeah, I think Weaver does have a HTTP JSON receiver, too.
**Riccardo Magliocchetti** 09:12 Nice.
Okay, bye.
Again, not a big issue, but if you're interested in testing instrumentation against Weaver, please take a look.
The thing is… Oh, strange VSYS does not move to… Approved already?
Okay.
And then we have this one.
Do you have an idea what this is about?
Improved documentation, I think.
Okay.
Yeah. I think this… we started to get some documentation PRs. This is not… is not the only one.
But, like, at least in another case, the changes… We're not doing anything, so if anyone is willing to review this.
We have to build the documentation of our set, because… Otherwise, like, we can't verify anything.
Even if the CI is good.
**Mike Goldsmith** 10:34 Yeah, I can look at this. I've looked at one of the other ones and was able to give some feedback on it.
**Riccardo Magliocchetti** 10:39 Thank you.
When we have, auto-log level support, Yeah, like, the OSDK… I'm sorry, is not handling the auto-lock level to, I think, configure The level, I don't know what is controls, if it's the… The level of the logs we emit.
Probably.
But, yeah.
Okay.
I should not believe that.
And then, this one, that I think is the… from a contributor that is, like, leaning on AI.
Yeah.
I think, like, you, Mike, had a… Someone else tried to have a shot, like, via comments on Gita, but… I'm not sure the…
**Mike Goldsmith** 11:50 Yeah.
**Riccardo Magliocchetti** 11:50 the call.
**Mike Goldsmith** 11:51 I think… Timing-wise, so we obviously saw quite a number of these come up, and it looks very automated in generation, and then replies to the comments and the threads for the feedback.
I haven't noticed a great deal since we've added our agent's MD to the repo, which we got merged yesterday, I think it was, and I think that's probably slowed it down a little bit, so hopefully we'll… Hopefully these won't just go still and not be continued, but hopefully they'll be able to contribute directly instead of just through automation.
**Riccardo Magliocchetti** 12:27 And let's stop, let's stop that.
**Mike Goldsmith** 12:29 Yeah.
**Riccardo Magliocchetti** 12:32 And anyone want to point out some issues we want to… Discuss or review?
Yeah, right.
accumulating quite a bit of stuff in approved PRs.
But, like, as for myself, like, lately, like, I feel I'm a bit overwhelmed with stuff to review, like, the contact switch is killing me, so… so yeah, I'm a bit slow this day, but…
**Mike Goldsmith** 13:05 Yeah, there's a lot both in car and country over a lot, recently, so definitely understand the, the extra load. Yazdankhah,
**Mani** 13:17 I'm not reviewing PRs, but I think one of my PRs is ready to merge. I've addressed all the comments. It's 4863… approved PRs that needs fixes.
New API yet, that one.
**Aaron Abbott** 13:33 Yeah, yeah, I can take a look at this one. Yazdankhah,
**Mani** 13:36 Thank you.
**Riccardo Magliocchetti** 13:41 I think you already approved.
**Aaron Abbott** 13:43 Yeah, I approved. I think… okay, you addressed, yeah.
**Riccardo Magliocchetti** 13:47 Yep.
Probably, I should take another look, yeah.
**Aaron Abbott** 13:51 Yeah, yeah. Somebody else took… had some reviews, so we could just get one more and then merge it.
**Riccardo Magliocchetti** 13:59 Okay, thanks.
Okay, let me keep the tab open, then.
Okay.
And then let's move to the topics for today.
Okay, the first one is for me, and… We have a regression.
Well, a couple of regressions, from the abruptity changes.
The issues that, we convert the sum of, of, like.
previous, like, Aldram versus true.
WebT object proxy… Object Proxy users.
to the… Object-based object proxy instead, and the difference between these But the base one does not implement the ITER protocol?
And so, some stuff that, like… some stuff we wrapped that, did implement the ITA protocol, did lose that.
One user is… The DPF instrumentation.
we have, PR for that, but I think it's… not correct.
Like, I've already reviewed that, I'm waiting for the reporter to update that.
But, like, the fix is trivial, and, like, in this case, it's just to move back to the old class.
And then, like, I audited the other base object proxies user, the bedrock instrumentation is… the bedrock instrumentation inside the water package is fine.
We have another user that is, GRPC.
but doesn't implement the ITER protocol, but I'm not sure.
If it should, we are wrapping, something context, a service context?
And so if anyone with some GLPC clue can take a look.
Like, I don't expect a context to be high trouble, but… Who knows?
And also, we have another user that is the PICA, and here, I think this needs to be fixed as well.
Because we are wrapping a deck.
And the deck is, iterable.
So, yeah.
**Aaron Abbott** 16:49 if you use this and it's adding the iter protocol, like, what does the implementation do? Just return nothing?
**Riccardo Magliocchetti** 16:58 It's… Raises an exception if you try to iterate.
**Aaron Abbott** 17:04 Oh, okay, I see.
**Riccardo Magliocchetti** 17:07 So, like, and yeah, I think the issue we have is that In our test, we usually test the instrumentation, But don't test, but… The, you know… At least, we don't cover all cases where the, you know, the API, what… I don't know if it's Chemical API, but the… You know, the stuff we instrument behaves the same.
For example, yeah, as I noted here, like, for example, on the DB API instrumentation, we are not testing, but you can iterate over the cars, so… But we have a… we test ordered part of the… Of the stuff we instrument, but not this one.
So yeah, maybe our testing can be improved as well.
**Aaron Abbott** 18:04 Okay, yeah.
So, for this specific issue, do we want to… Like, roll back the change and wait, or do we want to just kind of fix them?
**Riccardo Magliocchetti** 18:15 However, since these are trivia to fix, I think let's… We should probably fix that, and I… if, like, if I'm able to do the fixer soon as, like, if I'm able to merge the fixes, I'll cut a patch release next week.
**Aaron Abbott** 18:33 Alright, yeah, all… Is there, like, a full write-up of the issue somewhere? Is it just this issue here?
**Riccardo Magliocchetti** 18:42 Nope. I think, like, The reporter, like, just opened the…
**Aaron Abbott** 18:51 I see.
**Riccardo Magliocchetti** 18:51 Like, PR right away, so… Yep.
**Mike Goldsmith** 18:58 I think if we've got other instrumentations that may need it, it would be nice to get issues for those, and then we can at least try and track them that way.
**Aaron Abbott** 19:08 Yep.
I wonder, also… I'm looking at the docs for wrap to see why they made this change, but, it sounds intentional, so we probably can't have it fixed there.
**Riccardo Magliocchetti** 19:27 Yeah, like… I think that the issue has been… like, when we added the wrap… True support.
We probably overlooked this thing.
And… Like, because, like, we introduced the base object proxy intentionally, because, previously, like, every object wrapped with the object proxy were made iterable when the original one was not.
And so, I think the fault is on our side when we switched to the… To this new class.
Because, like, Some of his object… needs to be iterable so that the previous code was fine.
**Aaron Abbott** 20:18 Okay.
Thanks.
**Riccardo Magliocchetti** 20:22 Nope.
Yeah, like, speaking of being a bit overwhelming, I think, like, We tend to work on our own, on… Different stuff, but it's expected and fine.
But, like… It would be nice if we maybe can have, like, just a bit of coordination.
So, like… If you have plans to work on something.
Or if you're working on something, or… Or, yeah, like… you have some itches to scratch, and you want to open some PRs.
I would appreciate if you maybe, like, don't need to share, like, overshare, whatever you plan to do, but… if you're, like, working on something, I would appreciate if you maybe can just write a note here, like, after the call, and just say, like, add your name, and maybe… What's your plan?
Or what you're working on.
And so that maybe, like, we can… Direct our energies more on the same direction instead of… Of, like, starting… Doing, like, a… A lot of stuff, Again, like, this is, like, for me, probably to try to save some context switching, like… If possible, though.
Thanks.
**Aaron Abbott** 21:53 Yeah, and Ricardo, is it… is… is it good in this dock? Just be, like, would it be better to do it in the issue tracker somehow? Like, we could add labels, or, Do a better job with the issue tracking, or it's just more helpful to have it in the dock for you?
**Riccardo Magliocchetti** 22:14 like… like, I'd expect an issue to go, like.
out of date very easily, so, like, probably just, like, was more to get, like, a sneak peek, like, of right now, what… if you have any plan, On what you're doing, like, in the next few weeks.
So… Yeah.
So, so, like…
**Mike Goldsmith** 22:47 I think it's a… sorry, go ahead.
I think it's a good idea. I think it's a good idea to sort of, like, indicate what area of the functionality you might be interested in doing and working on. Issues are probably a good place to keep that as, like, a… A place to keep all of the contacts, because you can obviously add trick tracking, subtasks. You can do more comments on it, you can sort of, like, put feedback as, like, where you are up to, and so you can… relate to that. Maybe if we've got, like, concerted effort in a particular direction or focus, we could keep a track of them in here. I think that would be good, like, we'll just, like, I can see Ricardo and I have both put in, like, the issues that we're both interested in, which is, like, a top-level one, and then has a plan or an idea of where we want to go and what sort of things we want to do, so it's not super intense in the doc, but it's a good place to track, like, where we're… Wanting to spend our time.
**lechen** 23:42 Yeah, I wouldn't be opposed to adding a section Every week, as well.
So this doesn't get…
**Riccardo Magliocchetti** 23:55 Yeah, we'll come to that.
**Mike Goldsmith** 24:01 Just at the top there, I know we've recently added the triage section, and I think maybe just a small section that we add at the top of each weekly meet would be good, just to sort of highlight areas that we are interested in working or have spent time in.
**Riccardo Magliocchetti** 24:32 Okay, thanks.
And… okay. Next topic is from Lucas.
**Lukas** 24:43 Yeah, I don't need to spend a lot of time on this, but yeah, just, Yeah, I'm currently working on just trying to get the OTLP JSON exporter out, so yeah, this is one of the dependencies.
So, yeah, I understand you're busy, though, so… no worries.
**Riccardo Magliocchetti** 25:08 like, I think I've already… I commented about, you can drop… yeah.
**Lukas** 25:14 Yeah, I fixed the… I fixed all that.
**Riccardo Magliocchetti** 25:16 Okay, I'll take another look.
Thank you.
Like, this is, like, the last bit before the exporter, right? Oh, no, this is the export.
**Lukas** 25:29 This is…
**Riccardo Magliocchetti** 25:29 There's a couple.
**Lukas** 25:30 There's gonna be one more to actually add the exporter, but… This is just the, like… code to go from SDK objects to the… Actual, JSON objects.
**Riccardo Magliocchetti** 25:50 Okay, cool.
Thank you.
This topic is also from you.
**Lukas** 26:01 Yeah, so I just wanted to bring this… this… I was looking at one of these issues, Just curious if we wanted to… Explore it, but… It seems like a lot of people have been complaining about the protobuf dependency for the exporters.
So… I guess… Yeah, I mean, there's a few reasons, but, like, I think one of them is that it's a pretty hefty package, and then having to manage the dependencies can be a pain, so… Yeah, so I guess one solution to this is, like, just writing a Rust extension.
Which is what I did in this little repo. This is kind of just a POC.
And, yeah, based on this, like, if you scroll to the bottom.
It seems pretty promising, like, we get pretty decent performance gains.
And the package size is, like, about 50%.
So… Yeah, I was just curious, like, if… That this is, like, a direction we'd be interested in going in, or not?
**Aaron Abbott** 27:09 Yeah, I think this came up before, so there's, like, a repo floating around. Maybe I shared it with you already, Lucas, but… This definitely came up before in the context of cold starts.
like, people running on Lambda or whatever, Even if you remove the protodependency.
You know, the native extensions are just a little bit faster to import, because there won't be any You know, like, recursive transitive dependency walking, so… It seems kind of interesting.
I guess my question is, like, the… the Protobuf team did some work with allowing… The generated code to work with multiple versions.
of the Protabove Library.
So hopefully that part of the friction will be solved now. So, like, you know, the ecosystem doesn't get bifurcated each time that they do a major version release of the protobuf core library.
So yeah, I… yeah, and I guess, like.
there's obviously downsides to native code, I think.
For example, in the operator.
We have the JSON stuff you're working on, so maybe it's not super applicable, but… You know, generally speaking, we have to ship wheels, and maybe mature in, or however you say it, makes this pretty easy, but, you know, there's… the Python API versions, and then each platform.
And then each operating system, so… Yeah. I'm guessing you thought about this already, though, right?
**Lukas** 28:41 Yeah, yeah, that would… so yeah, obviously that, yeah, that's one of the downsides. So… Yeah. I might end up… yeah, if… I was just, you know, curious, but it sounds like… once… Protobuff is able to implement those improvements, then maybe this isn't as necessary.
**Aaron Abbott** 29:06 Yeah, I mean, I think it should be implemented already, like, So next time they do a major version release, we can keep we'll basically keep the generated code, or we'll bump it, so say they… I think they just released 5 or 6, I don't remember.
We just continue generating the code with the lowest supported version, and then that means that the… there's a window of two major version releases that would always work.
Oop, Unmoila. Hi.
**Liudmila Molkova** 29:36 I have a naive question. So, I've heard in the past two things that This is a very toxic dependency that really complicates onboarding, for users on different platforms, and I know that there were some previous attempts to remove it.
cat, cat.
Is it important? Is it… like, am I wrong? Did I read something wrong? I have, like, almost zero context.
**Lukas** 30:07 Yeah, that's right, that's the motivation, I think. It's like…
**Liudmila Molkova** 30:14 So, essentially, the goal is to remove it? Is this where discussion is going, or, What, what is… sorry, what is the con… the story here?
**Aaron Abbott** 30:31 I think the.
**Liudmila Molkova** 30:32 Are we solving it? Yeah, that's the question.
**Aaron Abbott** 30:35 Yeah, I, I think… I think Lucas has a PR here which would solve it via shipping some native Rust code. What I was trying to raise is, and I just shared this link here on the right, I think this is from… and it might be on the issue as well, I think this is from, like, 2024, maybe, that they started doing this, or 2025.
It should make the dependency a little bit less toxic, in theory.
**Liudmila Molkova** 31:04 But maybe let's just… Try to remove it, if… It's just a little bit less toxic.
**Aaron Abbott** 31:13 Yeah.
I mean, I think we can talk about the downsides more, if that… if that helps.
**Lukas** 31:23 Yeah, we can keep discussing it, we don't need to make a final decision now, but yeah, just thought I would…
**Aaron Abbott** 31:30 Yeah, I mean… question, Lucas, right? Like, in the… in this PR, does the… like, one of the issues with Protobuff is that you have to have one version installed, generally, for all of the process, because it expects, like, the shared library to be the same or whatever, and… I'm guessing this Rust implementation is hopefully not having that problem, but would this just move the… kind of toxicity into the Rust world, where if you had two native extensions that had Bertabuf with different versions, they would then conflict, and you'd have the same issue.
**Lukas** 32:02 So… Essentially, this would just kind of move the dependency management to us, and from… this is using Prost, so from what I understand, like, everything you need is already in this library, so you could actually have any version of… you wouldn't… You could either have Protob installed or not. I don't think it actually dynamically links to anything, so… So, like, it would just work. Again, but yeah, the downside is, yeah, we'd have to build wheels for every… every OS and architecture, but… Maturin makes it pretty easy to do that. So, yeah.
That's, I can, yeah, look into it a little more, but, yeah, that, that would… And then, obviously, the downside would be is that, you know, if you have… A lot of packages that are… Doing stuff like this, then, you know, the… Aggregate size could… will definitely eventually exceed the protobuf dependency itself, but…
**Aaron Abbott** 33:07 Right.
Okay. No, that's helpful. Should we… should we take it offline and keep discussing on the issue?
**Lukas** 33:20 Nope.
**Aaron Abbott** 33:21 Okay, thank you, this is cool.
**Lukas** 33:24 Yeah, and then, these, I can… maybe I can just take these offline. I'm not sure if it's worth me posting these, but yeah, these are just two, kind of.
old PRs.
That… Can probably get merged.
So…
**Riccardo Magliocchetti** 33:51 And he's been open since a few years.
What?
for the GRPC code, I'm really, like, not an expert, so… I don't think I can do a proper review.
I just need to take a look again at the point flex.
And thanks for your patience.
**Lukas** 34:23 Thanks, everyone.
**Riccardo Magliocchetti** 34:29 Next one, yeah, from Shuning.
**Shuning Chen** 34:34 Yes, so I refactored the embedding metrics after the API refactoring change merge. It becomes a much simpler change right now.
Paying for more, approvals.
**Liudmila Molkova** 34:53 Nice, thank you, I'll review in a sec. It's great to hear it became Smaller.
**Shuning Chen** 34:58 Yeah, thank you.
**Riccardo Magliocchetti** 35:05 Next one is for, Josh.
**Josh Winerman** 35:11 Hey everyone, so sort of the same for me, just waiting on more approvals on this. It's a relatively small PR, so hopefully it shouldn't be too much of a hassle.
**Aaron Abbott** 35:27 Cool. Looks like we actually have approvals. Was there anything, just waiting for this to merge, or…
**Josh Winerman** 35:33 Yeah, just waiting for it to merge, yeah.
**Aaron Abbott** 35:36 Okay, cool.
I can… You can do that unless, Anybody else have comments on this?
**Riccardo Magliocchetti** 35:46 Yeah, like, this is for, What is configuring?
**Josh Winerman** 35:56 I think it's the OTEL log handler in auto instrumentation.
It's been a sec.
**Riccardo Magliocchetti** 36:10 Okay.
Okay, I can probably take a look.
**Josh Winerman** 36:14 Okay, thanks, Ricardo.
**Riccardo Magliocchetti** 36:17 Thank you.
Okay, next one is from Kif.
But…
**Keith Decker** 36:28 Yeah, so after the GenAI utilization… Rework. This is just a new PR for the tool invocations to add metrics, and so… the old PR is kind of invalidated for the rework, so just looking for reviews on this.
It's also a minor change after the… the API freeler.
**Riccardo Magliocchetti** 36:58 Nice, thank you.
And this one is from… Irvin?
**Erdenesaikhan Tserendavga** 37:06 Hi, everyone. Yes, this PR is, related to the agent indication type for the, GNI UTs.
As of now, I have applied the, new API change from the Midas PR, and there is a one, I can say blocker, which is tool definitions, semantic connection, Is Tiege pending?
Which is meshed here.
**Liudmila Molkova** 37:42 Looking in the semantic conventions right now, maybe we can finally merge it,
**Erdenesaikhan Tserendavga** 37:49 Awesome.
**Liudmila Molkova** 37:50 I didn't check yet, sorry.
Okay. The moment I have the two approvals on it, I can merge it, but not be free.
**Erdenesaikhan Tserendavga** 38:02 Sure, once it's merged, I can apply that change in this PR again.
**Liudmila Molkova** 38:07 Okay, we have two approvals, and I am going to merge it right now.
So… The semantic conventions are not released, but I would be more than happy to approve the deals change anyway.
**Erdenesaikhan Tserendavga** 38:26 Sure, thank you.
**Riccardo Magliocchetti** 38:32 Thank you, Ruth.
And… yeah, last one from Yuri de Mila.
**Liudmila Molkova** 38:39 Yeah, so, Ricardo, you posted that there is a problem with open telemetry version of a stream invitation, and… I burned some tokens asking AI to investigate if it applies to ours. It does.
And it said to fix. Fixing it, it's pretty straightforward, and… Good job, but… So, actually, the new Rupt was released with Major Version 2, it had some breaking changes, and the fix is essentially to adapt to API version that stayed consistent across versions, and to add tests for the latest version of the Warped.
Very trivial.
**Riccardo Magliocchetti** 39:34 Yeah, like, oddly enough, like… only the GNA instrumentation were passing the keyword arguments.
Like…
**Liudmila Molkova** 39:46 I think we copied it from somewhere.
Yes.
**Riccardo Magliocchetti** 39:50 Yeah.
**Liudmila Molkova** 39:52 Yeah.
**Aaron Abbott** 39:54 Oh, I was just gonna say, I… Personally.
Prefer the named argument, so this makes me a little sad, but that's all.
**Liudmila Molkova** 40:03 Yeah, having said this, I think Java has some cool workflow that every night they check that there are, like, for the new releases.
of… the dependencies.
And they run tests against latest releases.
So, it would be interesting to automate, this latest thing.
So that the job would just go and… Update the… either the… Latest test dependencies for all packages.
Or, it'll just run tests against them.
And we would see failures.
It's, again, yet another… Good idea, good task for AI to go automate, because it's just plumbing things through, it's no human judgment, just… Make it happen.
**Riccardo Magliocchetti** 41:16 So, so, like, the idea would be, like, to, Like, rebuild the test requirements every night, using the latest packages, just run tests against that.
**Liudmila Molkova** 41:30 Yeah, so some, some form of a bot, maybe we can do something with Dependable bot or Renovate that will… based… when the library, the new library releases, the new version of a dependency releases, it would go and update this test latest dependencies. That's how we test against it, and we will see failures on the PR.
Another approach would be to have, like, the batched nightly job to go check the latest versions.
Test against them, or, just update the latest versions, and we will again need to look at the PR of its failures. Hopefully, it will not be… There will not be a lot of them.
But… we need some discipline to actually fix this.
I think at this, just the, like, I'm throwing in ideas, I should probably come up with the proposal on how we can fix it, and then we can evaluate it.
**Riccardo Magliocchetti** 42:40 That would be great, but, yeah.
Like, queer… Yeah, but, like, a lot of opportunities to improve our CI, I think, our testing story, yeah.
**Liudmila Molkova** 42:56 Yeah, it's kind of sad that we cannot, We don't know when we break users, right?
they are broken with somebody releasing a new version of Warped.
**Riccardo Magliocchetti** 43:11 Yep.
Okay, what's the last topic for today? By the way, I think before you joined, Mila, I talked briefly about your… we've, Pr.
Yeah, like, maybe… You want to also… talk about that, or maybe… I'm not sure I did a good job, but…
**Liudmila Molkova** 43:43 I'm pretty sure you did a good job, but essentially… Oh, are there… this… we had this discussion a few months ago over, Ricardo, you played with it, I played with it during the, I think Christmas holidays.
And independently, not knowing that we're both playing with it, the goal here is to put an utility for the viewer life check and the core repo, and then leverage it in the instrumentations, where we would, just write an integration test for some library, and we will feed the telemetry into the Weaver LifeCheck. It will check the compliance of the telemetry emitted by this library against the semantic conventions.
And, it does not cover everything, right? It just listens to the telemetry it received, and it notices if things are deprecated, where there are some attributes that are not documented or used, or that metrics have an expected shape and whatnot.
you can do more checks with it. And I have very high hopes of leveraging it first in all instrumentations, but Gen AI would be the first ones to start with. It can help us with the preview process, when we get… when we read the code and we don't know if it follows semantic conventions, guess what? This will tell you with… it's not perfect, but with some level of confidence, you can tell, at least there are no obvious mistakes here.
And this is where I got into the JRPCIO dependency as well.
Beyond hearing from the customers that it's a big problem for adoption.
It was a big problem for our pipelines to…
**Riccardo Magliocchetti** 45:40 By the way, The issue here is gRPC or protobuf?
**Liudmila Molkova** 45:50 The JPCIO, at least. It tried to build it on Windows, and it couldn't.
**Riccardo Magliocchetti** 45:55 Okay, I… Maybe can we try switching to HTTP?
Sorry? HTTP… can we try switching to the HTTP exporter, maybe?
**Liudmila Molkova** 46:06 Unfortunately, Weaver only supports gRPC as an input, that's not great, but yeah. I can send the feature request to Weaver, maybe eventually it will support HTTP as well.
**Riccardo Magliocchetti** 46:22 Thank you.
**Liudmila Molkova** 46:24 I'll get to the comments.
**Riccardo Magliocchetti** 46:28 but, like, it's, like… For me, it's good enough, but, like, it's a bit sad that… We are not able to find a solution, but… we'll have, like, coverage in CI, and we'll be, like, not, Annoying for… for you on your machine, but yeah.
Sorry.
**Liudmila Molkova** 46:50 You're saying… huh? Go ahead.
**Aaron Abbott** 46:53 Sorry, I was just gonna say, don't… don't we run the actual exporter, OTLP exporter test on Windows, though, for gRPC?
**Liudmila Molkova** 47:03 There are some tricks in… in the… Ci for this.
**Aaron Abbott** 47:09 Okay.
**Liudmila Molkova** 47:10 But I don't think we do all the combinations.
**Aaron Abbott** 47:16 Okay, yeah. I mean, it's definitely… Happens. Sorry about that.
**Liudmila Molkova** 47:24 Yeah, that's nothing to be sorry for. It's just… it sounds like it's a… like, this dependency is a problem for users. I don't care if it's a problem for MIPR, but if it's a problem for users, we should try to solve it in one way or another.
**Lukas** 47:39 As Weaver, can it take, like… Otlp JSON… Files, and just check that.
**Liudmila Molkova** 47:48 It, it can.
But… Do… do we want to build something complicated around it? Like, we… I don't think it's useful to test the sun windows, it doesn't… Increase any coverage.
As long as we test this specific feature on.
No. Whatever Ubuntu, that's fine.
**Riccardo Magliocchetti** 48:24 Okay, thank you, Limila.
Any other last-minute topic, or…
**Liudmila Molkova** 48:32 I wanted to throw in another PR that, Makes things a little bit more consistent in… Duh.
Janeo Tios?
I'm adding it to the agenda here… So this is the completion hook, that… can be provided to telemetry handler in the GenAIOTUs.
R… Maybe tell me if I should break this pure down, but it also… updates OpenAI to the latest version, and there were some problems. So it, like, plumps things through OpenAI, so it affects both Tilsen and OpenAI, and it also fixes some issues with the latest up-in-the-air version. So there are effectively 3, Trivial changes across this pure.
If I have to split it, let me know, I will split it, but it's really not huge anyway.
**Aaron Abbott** 49:46 I can take a look, doesn't look too bad.
**Liudmila Molkova** 49:51 Take care.
Thanks, Dad, that's all I had.
**Riccardo Magliocchetti** 50:02 Thank you. Yeah, that's Nick again.
Yeah. So, thank you, everyone.
We have 10 minutes back.
**Aaron Abbott** 50:14 Yeah, thank you.
**Riccardo Magliocchetti** 50:15 you.
**Liudmila Molkova** 50:15 Thank you!
**Lukas** 50:18 Thanks, everyone.
**Keith Decker** 50:19 Thank you.
**Erdenesaikhan Tserendavga** 50:20 Thank you.
