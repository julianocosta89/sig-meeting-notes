SIG: .NET SIG
Date: 2025-09-02
Duration: 32 minutes
============================================================

## Zoom Recording Transcript

**Rajkumar Rangaraj** 02:15 Hello, everyone.
**Martin Costello** 02:18 8.
**Matthew Hensley** 02:20 Hello?
**Rajkumar Rangaraj** 02:22 Hey Martin, just want to check. I never gave a chance to the other approvers to drive. If you want to drive the meeting, please feel free to let me know. I can even today pass on the control, if you want to drive.
**Martin Costello** 02:36 Really short notice to throw me at it, so maybe next time.
**Rajkumar Rangaraj** 02:39 Yeah. Yeah, just normally earlier the approvals used to drive also, so yeah, I mean.
I did not ask you at all.
**Martin Costello** 02:53 No, that's cool. I'll consider it in the future.
**Rajkumar Rangaraj** 02:57 Sure. Goldman.
**Alan West** 03:05 Hang on.
**Martin Costello** 03:08 And…
**Rajkumar Rangaraj** 04:09 We'll wait for one more minute to see if anyone shows up. If not, I think we are… Enough agenda to drive here.
Okay, we'll get started. Martin, you have two topics. Do you want to go first?
**Martin Costello** 05:01 Yeah, so the first one's just a quick one. That's a follow-on from when we had the discussion last week. I've put a file into the PR, that's the body that would be an issue. It isn't intended to be part of the pull request, but I've put it in there so it's easy to do review on it. So I've distilled everything into that file if, People can take a look and give feedback.
**Alan West** 05:24 as relevant.
**Martin Costello** 05:27 It's the one that's called… it's the one that's called Issue Summary, it's the second file on the left.
**Rajkumar Rangaraj** 05:33 Yeah, I saw that you added a commit to that. So, yeah, it makes it easier, and we had a… we discussed about this one also, having something like this in the repo.
We'll review this one.
**Martin Costello** 05:46 Yep, cool, yeah, yeah, once that's reviewed and everyone's happy, I'll take it out of the PR, and I'll open an issue and put that text into it.
**Alan West** 05:58 Perfect, yeah, and we can make that an announcement.
So it kind of shows up at the top.
Of the issues, as well.
**Martin Costello** 06:09 Well, yeah, in the process of distilling that as well, it answered a question Peter had, which was about, like, the V9 stuff, and I remembered that we subsequently discussed when it first came up that it was just the one package that was going to be special, which was the… I always forget the name. System Diagnostics Diagnostic Source. So all the others would stay, pinned.
To the runtime, but that one would just move to pick up whatever the changes are.
So it's, like, the least possible churn in terms of the different bit. Which… so that should resolve the questions he had and we discussed last week that were related to the security patches.
Because when 9 goes out of support next year.
Everything will be 9, apart from that 1, so that will just… that will be wholesale out of support, and any… and the 8 stuff will be using 10, which won't go out of support, and we'll still get patches anyway.
**Rajkumar Rangaraj** 07:18 Cool. That makes sense. That speaks the tracing story also, yeah.
Hmm, this is one.
if that's all we have on that one, I think we will review it offline and provide feedback on… especially, we will provide the feedback first on that file, and then you can move that as an issue, and then we'll work on to merge that PR.
**Martin Costello** 07:43 Yep, sure.
**Rajkumar Rangaraj** 07:44 Yeah, The next one, I like the way you pointed out. I kind of feel the integration tests are missing in the open telemetry for OTLP.
We have it completely covered in the auto-instrumentation repo, but it's a very big gap here.
I think this is a very good one to cover.
**Martin Costello** 08:09 Okay, cool, yeah, cause, it… I found this issue… well, I found the first of those two issues to be quite a long, convoluted sequence of steps, and there's a… disagreement as to whether it's an OpenTelemetry collector bug, or if it's a bug in the .NET OTEL SDK.
But they have changed the collector so that the incompatibility I've found has gone away.
But, it did highlight that it had to go through quite a few repositories until it effectively ended up in a personal repository of mine. So, end user hat. So… there's a test gap somewhere, so… and then there was the recent PR that I fixed, which was to do with gRPC, so I figured I'd just raise it with a… that we did have anything already, and I've just not seen it, and if not, would it be open to adding some level of… End-to-end slash integration, however you want to call it, tests that validate that what the collector submits is actually accepted by one or more collectors that it's… that end users would really use.
Because if we're testing it with unit tests, then we're sort of… Validating our own assumptions, rather than checking it actually works with something that's outside.
**Alan West** 09:39 We definitely have integration tests today, but I mean, they're very simple. They don't… Test, you know.
everything. What is your thoughts, like, basically expanding our current integration test?
**Martin Costello** 09:55 Yeah, because this… the first of the two issues was specifically to do with HTTP protobuf.
And that just happened to be how I'd configured my personal app. So, a bunch of other stuff that did have integration tests, so it just sort of did, like, all the defaults, and those passed. But if you happen to change that one setting, you fell into the bad code path, and then it was… all of metrics was broken.
**Alan West** 10:23 Gotcha.
Yeah, that'd be great. I almost wonder, like, I haven't studied this issue very closely, but… Do we have any suspicion that maybe this… Is it all related to… the manual is serializing that we're now doing with the OTLP exporter?
**Martin Costello** 10:42 It could be because manual serialization is what caused the bug in the first place on the other side.
They wrote a hand-rolled serializer, sorry, deserializer, and they implemented it on this… what looked like a stricter version of the spec.
And our one is doing something that's a should.
And they hadn't catered for the should in their spec, so that's why the payloads were being rejected?
**Alan West** 11:11 I see. Yeah, I wonder if, like, I wonder if we threw, like, an older version of the otel.net SDK at that version of the collector, if we sent some data from an older version of our SDK.
If it would have just worked.
In either case, yeah, it sounds like y'all dug into the spec, and if it's a should, then yeah, it's probably just a… Sounds like maybe more on their side than… than us.
**Martin Costello** 11:41 Yeah, I didn't want to get in a finger-pointing discussion with them. I was just sort of like, hey, I'm an end user and it broke.
And the change that broke it happened to be yours.
**Alan West** 11:53 Yeah.
I mean, in some sense, it's probably, like, kind of… it's both projects, right? Like, we're not the only ones that have, like, done the manual serialization, right?
I know Java has done the thing, too, and probably went through some… some pains there. Sounds like the collector's now doing it. So, as more and more hotel projects kind of follow that path. It's… it's really, like, an hotel broadly… broad problem, not, like, a specific project.
**Matthew Hensley** 12:27 So in this case, the, part that they skipped to the spec is actually a must be able to.
And they just assumed people weren't using it because it's… theoretically less efficient, but I think it's faster to serialize.
But it's more, efficient over the wire. So, this is one that, in their custom… Serializer on the collector side, they just missed a step.
**Martin Costello** 12:53 Oh, I missed that. The comment I saw was suggesting it was a should.
**Matthew Hensley** 12:59 Yes, it… that is what they suggested, but if you look… on the PR where it was fixed, in the quote, it says, protocol buffer parsers must be able to parse repeated fields.
So… It's, it all comes down to, like, how arrays are represented in Protobuff, and there's… You know, a good way, and then a lazy way, and they only did the… Good one.
**Martin Costello** 13:26 Right, okay.
What I'll do tomorrow is I'll spin up an issue to track doing something about this, and then I'll look into what we can do to… Probably catch issues without going too… too far down the rabbit hole.
**Rajkumar Rangaraj** 13:49 I 100% agree there. I've been always thinking about it. At some point in time, I thought even I would dedicate my time also on this one.
So, definitely, the integration test gap is causing a lot of issues. Even when we switched to manual instrumentation in the .NET framework, we introduced some smaller bug, and we fixed later. Those and all could have been captured with integration tests.
So, I think it's must to have the integration test. If we have enough… if we need to… if it's not tracked, we definitely need to have an issue to track this out.
**Martin Costello** 14:27 Okay, cool. I'll look at that tomorrow.
**Rajkumar Rangaraj** 14:33 Alan, you want to go next.
**Alan West** 14:36 Sure, yeah, you just want to click on the link. Yeah, I just wanted to touch base because, I know, Martin, you… have been commenting on some issues and whatever. I don't have anything necessarily Specific to say about any of this, but I guess… for the group here, Raj, while you were out.
I met with, Steve Gordon and Martin.
About picking up some of this work.
And… I know Steve has already jumped in, did some stuff with the query summary. Martin, it looks like you're working on some stuff, too.
So, thank you for all of that.
Steve pinged us on Slack just today, and… I guess I just want to touch base to kind of, like, get a… Get a sense for… we're… where we're… With some of these, maybe… Maybe the top two… Martin, do you… Are those… are those ones that you're looking to work on, or you've already analyzed them and…
**Martin Costello** 15:51 So, the top two are both resolved in a PR that's open.
**Alan West** 15:56 Oh, okay. So there's an open PR. Sorry, I was just catching up with all this, so I hadn't seen that yet.
**Rajkumar Rangaraj** 16:04 Yeah, I see there is a PR link, yeah.
**Alan West** 16:10 Perfect. Yeah, I will take a look at those, that PR, then.
That's cool.
And then, I saw you responded to Steve, it sounded like he tossed out, like, the idea of working on the batch size, maybe.
The other one here that I opened… It's… Raj, if you want to click on that, consider removing as setDB statementText.
So… This has been a question on my mind for a little while now.
And what I'm proposing Is… currently, we have this configuration parameter.
It only affects… Traces… actually, I think it affects traces and metrics, which is a little funky, because… Right now, it's just sitting on this, like, trace instrumentation Options class. We don't have a metric instrumentation Options class, we haven't introduced one.
Because the only reason why we would introduce one is for this specific Setting. There are no other settings that are relevant for… for metrics.
So… One… Thought on my mind is… This setting basically gates, currently.
kind of two things, so it gates… the sanitization?
of DBQuery text, so, you know, replacing all literals with, like, a question mark so that it's, you know, no sensitive information is leaked. So it does the sanitization, and then it also generates the DB query summary.
And furthermore, it is currently default off.
However, db query summary is a required attribute, like, we need to be producing it, so… At a bare minimum, I feel strongly that it should be default on.
But I'm going even further than that.
And suggesting that, for the… at least the initial release, and it… and only if somebody actually, like.
demands to be able to turn it off.
I'm suggesting that we just get rid of the… the… Configuration option altogether, for now.
And I wanted to get people's thoughts on that.
**Martin Costello** 18:57 I don't have a strong opinion on it, but one of the other issues is about renaming the option, so we'll… whichever option's chosen, it'll be sort of two birds with one stone.
Because it's either rename the options or get rid of them.
**Alan West** 19:14 Yep.
Yeah, I feel like if, we do this, then there is no, like.
Naming problem anymore for any of the options.
**Martin Costello** 19:23 I think the only thing I thought of that's a possible thing to bear in mind if it's removed is… If, for some reason there's a bug in the sanitization, There isn't an escape hatch.
If you've, like, accident… if you're accidentally logging something that should be redacted that isn't being redacted due to a bug, there's no way to stop it.
**Alan West** 19:48 Yeah, and I think we did encounter… of something, somebody had hit, like, a null reference, or, like, an array out of bounds, or something like that exception. One thing that we could do, that would, I think, Make that a little bit better would be to… Catch any exceptions, and, like, log a message that says, like.
You know, fatal hair and instrumentation.
**Martin Costello** 20:15 Oh, I was, I was thinking more, like, there was something wrong in the parsing, and, you know, it was, like, someone's password was still in the SQL when it shouldn't be.
**Alan West** 20:24 Oh, I see, I see.
I see.
Yeah, I guess that's a consideration.
That… I don't feel… super… Strongly.
About.
But…
**Martin Costello** 20:49 I don't think it would block removing it, I think it's just a factor to consider, and there may be Write down that it was considered, but we're removing it anyway.
**Alan West** 21:00 Yeah.
I've spoken with some other languages, and they don't… have an option for disabling this today. I mean, Java is actually the one that I've… that I've spoken to.
**Rajkumar Rangaraj** 21:12 I would say, as it's not released, Helen, it makes sense to go without it. If there is a need, we could consider later. It's so simple. Instead of… but if we introduce it, taking it out is very, very difficult.
**Alan West** 21:25 Yep.
That was my thought as well.
**Martin Costello** 21:29 So yeah, I mean, if…
**Alan West** 21:30 If people don't feel strongly about keeping it, then I, yeah, I think that's what we should do. And yeah, Raj, we can totally add it later. When we do, if we were to add it later, there's gonna be, like, some interesting questions to answer, like.
Should it be separately configurable for traces and metrics?
it would be kind of funky to, like, do all this work to generate the DB query summary and say, I only want it on traces, but I don't want it on metrics, you know?
**Rajkumar Rangaraj** 22:03 Yeah.
**Alan West** 22:05 And… That… that was one of… that was one of the elements that was kind of, like, driving me to, like, let's just get rid of this and, like.
Punt on this, like, deal with these kinds of questions, like, some other time.
If needed.
**Rajkumar Rangaraj** 22:19 Yeah, even if we need to consider it later, we need to have a strong justification from whoever requests for it to explain, like, what's the exact need for this. So, I think we will understand the business scenario for which it is needed, and based on that, we can brainstorm around that point in time.
**Alan West** 22:39 Cool.
then… let's just make that the decision. Let's, let's… let's do this PR, and then to your point, Martin, I mean, this issue, let's… to your point, with that other issue.
Can we find that one real quick? I just want to make sure that…
**Martin Costello** 23:01 number 3019.
**Rajkumar Rangaraj** 23:10 You said 3090, right?
**Martin Costello** 23:11 19.
**Alan West** 23:23 Okay, okay. This is just talking about, specifically this option. Yeah, so this would… To your point, two birds with one stone.
I think for stabilization, the options that we do still have for tracing, like the enrich and filter, there probably will still be a question of, like, are those the right names?
I think in some other instrumentation, we named them slightly differently, I think… I think we, like, added… like, additional language to the name of the option, like, enrich with What it's being enriched.
by, so there may still be some naming considerations for those options, but… this suite of options, yeah, I think… I think for the EF core and for the SQL client, we can just… We can just dump them.
Simplify our lives.
**Rajkumar Rangaraj** 24:34 Cool, going back to the milestone again.
Do you have anything else, Alan, to cover here, or we are good?
**Alan West** 24:44 I don't think so. I think we're pretty good. I think… I think we're really close.
that batch size one, I think… is something that needs to be considered by somebody, but then, at least for the SQL client instrumentation, there might be a little bit more work for EF Core, but at least for the SQL client instrumentation, I really think it's mostly just documentation at that point.
And… And then just kind of like a final review, and I think we're… I think we can release it as stable.
Once we kind of close out all these issues.
**Rajkumar Rangaraj** 25:21 Do you have any timeline in your mind?
And then for the stable release.
I spoke to the Java folks, and I don't think they're planning to do anytime soon. If we plan it, we may go before Java or any other languages.
**Alan West** 25:36 Yeah, I suspect we might be first. I think Java was originally targeting July, but I think that that… They… their… their release started growing, and… So they, they delayed it.
I actually don't… I don't know about the timeline because, I brought in Martin and Steve to… kind of collaborate on this, and I've not had a ton of bandwidth, I think, but… Like, I can… I'll review the PR that is open now, I can help out with, like, writing documentation and whatnot, if needed.
I think the batch size thing is the one thing that I've not spent any time, like, really thinking about, so… I… without knowing what that needs to look like, I don't know what the timeline, would be for that.
Quite yet, but… assuming we can get, like.
We can settle whatever that needs to be.
We'll probably have a clear picture of… When we could get this out.
**Martin Costello** 26:46 Another thing I did on, Friday is I… excuse me… is I had a look through all the open issues that were against the F-Core and C-Core client, and I think… I… marked a few as, this is probably fixed, can you check? There's a few that didn't have a repro on them. And then I assigned one to this, milestone, which is the last one, which you opened, Alan. I think that was just tracking stability anyway. But yeah, I think there's no lurking issues that are on the milestone… should go on the milestone either, unless I missed anything.
**Alan West** 27:24 Yeah, no, that sounds great. And then, actually, you just reminded me, I… I got a GitHub, like, notification from you the other day, and I was out, so I… I just spaced… it was about some issue that was… somebody was asking for, like… Not sanitizing comments.
From… from SQL?
I don't remember what issue.
**Martin Costello** 27:49 Oh, yeah, that was when I was doing my run-through, doing triage.
And I didn't know the answer, so I figured I'd just ping you, because you probably did.
**Alan West** 28:00 I will find that issue again, and I will comment on it, but, anyways, my take on it is… We can leave the issue open, but for stabilization, I don't personally want to consider it. It's… The reasoning why we're stripping out the comments is because comments could have sensitive information.
and so, I think it's a conservative move to, like, basically just strip them all out.
But if somebody wants… You know, in the future, to have some option to, like, not strip out comments or something like that, that may be something that we could entertain.
But… It's not related to stabilization in my mind. Or it shouldn't block stabilization in my mind.
Oh yeah, thanks, Matt. I will… I will comment on this issue.
**Matthew Hensley** 29:02 One thing that might be… bringing this up is, SQL commenter is getting some momentum behind it.
So, somebody might have noticed, like, doing debugging or something, that… The attribute was missing the comments used for correlation purposes.
**Alan West** 29:18 Yeah, and I think that at the point that we support, like, SQL Commenter is mainly about, like, propagating information, not so much about sanitization.
So, like… from… if the instrumentation ultimately needs to support SQL commenter for the… for the purpose of propagating information, like.
It should be able to… parse that out of the… of the raw thing, but that doesn't necessarily mean that we should also expose it in the db query text attribute, right? I kind of see those issues as… is… separate wants, you know what I mean?
**Matthew Hensley** 29:59 Definitely, I was just, mentioning, might come up a few times, like I said, if someone was, like, debugging.
That… They're probably going to wonder where… The comments are… But they were just, you know… Looking at the traces that were coming out, and… Trying to debug all this, so… It's not the first time I've seen, this raised.
**Alan West** 30:21 Yeah, that makes sense.
Cool.
Yeah, that's… that's all I had.
And thank you, Martin, for going through all these issues. That's…
**Martin Costello** 30:47 Absolutely.
**Rajkumar Rangaraj** 30:51 to… I don't think there is any progress from the last week, I think it's all still the same.
We need to take… go ahead and take a look at the PRs and move it. I went to the… there are two things I did to the repo. One is the… added some bypass rule in the admin repo for renovate. I think that unblocks this one.
And I also enabled the co-pilot for this repo by creating an issue in the community, but still, we cannot use co-pilot with this one. Bypass rule needs to be added to the admin.
the… really, in the admin repo, the configuration for the .NET especially is super complex. It has some ID related to every, tools. So, I have a hard time figuring it out what is the ID for that, because I don't have an admin access on the admin repo.
So, I'm gonna check with Trask or someone, whoever is maintaining that admin report, to see if we can change that approach, like, and use Approach like every other repo uses there.
So that's something I need to follow up.
So, apart from that, PRC needs a normal review.
**Alan West** 32:11 Okay.
**Rajkumar Rangaraj** 32:17 Anything else to bring up?
**Alan West** 32:22 Not from my end.
**Rajkumar Rangaraj** 32:24 Kun.
then I think we could end the meeting. Thank you, everyone. Bye.
**Martin Costello** 32:29 Bye.
**Alan West** 32:29 See y'all soon!
