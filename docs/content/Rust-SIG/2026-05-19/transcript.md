SIG: Rust SIG
Date: 2026-05-19
Duration: 26 minutes
============================================================

## Zoom Recording Transcript

**Björn Antonsson** 00:59 Hi there.
**Cijo Thomas (Microsoft)** 01:01 Hey, Bjorn, how are you?
**Björn Antonsson** 01:04 Fine, how are you?
**Cijo Thomas (Microsoft)** 01:06 Good. Finding it very difficult to catch the morning meetings because of our return to office thing.
**Björn Antonsson** 01:13 Yeah, okay.
**Cijo Thomas (Microsoft)** 01:14 I'll have to find some alternate proposals. It's going to be very tricky for me to join either 8 o'clock or 9 o'clock in the morning Pacific time, because I'll be on On either driving or a bus to the office.
**Björn Antonsson** 01:29 Yeah.
**Cijo Thomas (Microsoft)** 01:29 Yeah, but today I'm working from home.
Relatively seen today.
Yeah, I think we don't have many people attending. I was just looking at the previous notes, it's been, like, very quiet the last few weeks.
But things are, like, moving.
Slowly, but… yeah.
Anyway, now that we both are here, let's spend some time, Let me share my screen or two.
I should be shedding something now.
**Björn Antonsson** 02:15 Yep.
**Cijo Thomas (Microsoft)** 02:20 Oops, can you still see my browser with the repo open?
**Björn Antonsson** 02:25 I can see… I can see the browser.
**Cijo Thomas (Microsoft)** 02:27 Thank you.
Alright.
The main, issue which I want to discusses we need to close the API for OpenTelemetry tracing.
We have, like, a lot of open issues there.
I started writing it into a single dock to power everything.
I never had the time to, like, publish it, but I think we discussed this in the past as well. So I'm going to be working on that document, like, pretty soon. I have also spoke to, like, another person, like, Brian. He might also help there a little bit.
So that's the only thing which… Actively working on this week.
So, you were saying… go ahead.
**Björn Antonsson** 03:20 No, I have, there are, like, I have not been… I've been occupied with other things as well, so I have not had the time to clean things up, but there are a number of things around context and this little context deck where I think we can do some… smaller API changes, and also get some performance benefits out of it, that I'm thinking of. And I don't know if you know that there is this, profiling, Oh, initiative, within OpenTelemetry.
**Cijo Thomas (Microsoft)** 04:01 Yeah, yeah, I'm generally aware of it, anything in particular? Yeah, yeah, anything in…
**Björn Antonsson** 04:05 Yeah, so, so…
**Cijo Thomas (Microsoft)** 04:06 looking at.
**Björn Antonsson** 04:07 So, yes, I'm working with the people from Datadog who are involved in the spec.
And… What we would need for the thread-level context sharing, or… really the… connection between… profiling samples from eBPF and the current trace band ID would be some kind of mechanism to hook in to… when the context is changing, you can… and maybe this could be behind the feature flag, I'm not sure yet, I haven't really optimized away, but I've been thinking a bit about it, and that… it would be great if that, was something… I mean, it's not in the spec, because that's for… for the… What do you say?
That's for the language runtimes, or the language-specific parts to figure out how to do this.
But it would be an interesting thing if we could get that in before the API becomes stable.
Or maybe have that parked as a… an experimental part.
**Cijo Thomas (Microsoft)** 05:24 This, this pier, which is.
**Björn Antonsson** 05:26 That's… that's perfectly fine.
**Cijo Thomas (Microsoft)** 05:28 Is that still open? Like, is this…
**Björn Antonsson** 05:31 Yes, that's one thing, that's the process context.
That's, Sort of, like, which application is running, whatever, and other things. But the other, spec, which is not fully, stat… it's… it's not… accepted yet. It's about the thread-level information, like… Got it. You can use that to see, like, which traces and spans were active at which point in time, so… and connect that with the, like, profile.
**Cijo Thomas (Microsoft)** 06:10 Yeah, makes sense. Yeah, I think, like, we are quite open to add things under feature flag, so it won't, like, affect anyone else, to begin with, and once spec stabilizes, we can, remove it from the feature flag and make it follow the spec itself. So I think, like, Lilith has most experience on this side of things, and he also did a lot of experiment with EBPF profiling for… Rust, let me ask him to help here as well. He probably has a conference talk next week or something about same topic, prevailing BPF, Rust using a BPF.
So he may have, like, more inputs to share. So, let's use the, like, maintainers or approver Slack channel, to bring this, and I can ask Lilith to help there. He has the most context and passion.
on that area.
**Björn Antonsson** 07:06 Yes.
**Cijo Thomas (Microsoft)** 07:08 So on the tracing API thing, I think, this is really much the summary of the issue, like, all these issues are, like, rearranged a few weeks ago.
I'm, like, trying to get that document, like, this one is the most important thing, in my opinion. When there is no recording, there is no listener, we are… taking a lot of performance in, which I think I quantified it in one of the… contrip PRs, which I don't think it's marched yet.
Yeah, in the benchmark for power. I discussed this with, like, few people, yeah.
**Björn Antonsson** 07:48 Yes, I agree. We discussed this in a previous call way back, so I completely understand the… I mean, we would need to, like, change the API in some way to make this better.
I think, so… Yep, definitely.
**Cijo Thomas (Microsoft)** 08:06 the, Let me actually do this thing. I have, like, a partially working, summary of, like, what needs to be done. Like, it mostly boils down to don't require any owned data until sampling decision is known, so until then, operate with the slices of… yeah.
So let me, like, create that into a, like, broader issue, and see.
**Björn Antonsson** 08:31 Yeah, I think that's… that's also part of the, like… I think I have one ticket assigned to me, which is the builder API thing.
Somewhere…
**Cijo Thomas (Microsoft)** 08:45 Is this the one, the Spend Builder?
**Björn Antonsson** 08:48 Hmm…
**Cijo Thomas (Microsoft)** 08:51 I think this is also where we discussed a lot of the ideas, like.
**Björn Antonsson** 08:57 Yeah.
**Cijo Thomas (Microsoft)** 08:58 Yeah, we, like, started with this, like, 2 years ago.
**Björn Antonsson** 09:02 There are, like, there are multiple, you said… oh, you tagged me in one of these there.
**Cijo Thomas (Microsoft)** 09:10 This is one of you here.
**Björn Antonsson** 09:14 I think I actually assigned one of them to me, but anyway, so I started looking at it slightly, but, it's.
**Cijo Thomas (Microsoft)** 09:32 We don't need to, like, solve it right now, but I think, like, this is the right direction for us to move. And then we had some bigger changes in the tracing SDK. So this was for API, but then there were, like, a bunch of issues, and some of them are already in pull request mode.
A lot of them, actually, not one or two, like, three or four PRs, and… That one also requires some more design, because I… the main reason… I'm not comfortable with any of them is we have to first close the API, because there's a possibility that changes in API might, ripple into the SDK.
As well, so for example, what we pass to processors, what we pass to exporters, and specifically within processor, what do we pass to the start, stop, and ending, and then samplers, what do we pass to, the… whatever we do to improve performance at the API level, we'll definitely It'll pull through to the… SDK side as well. So I'm being, like, a bit conservative here, because the next release, whenever we do that, we want to, like.
**Björn Antonsson** 10:44 50 feet.
**Cijo Thomas (Microsoft)** 10:44 indoor.
**Björn Antonsson** 10:45 No, I, I, I, I mean… Once you decide that you're recording, you have to… have a copy, or, like, static, or you need to have your own copy.
**Cijo Thomas (Microsoft)** 10:58 ownership, yeah.
**Björn Antonsson** 10:59 And the… that, I don't think, will… the API on the other end, with the spam data, I don't think it will… Change.
Really?
**Cijo Thomas (Microsoft)** 11:13 Oh, no, I didn't mean, like, just that part.
**Björn Antonsson** 11:14 Okay, but exporters, fine, but for the processor, yes, and the sampling API, in that case, will change.
**Cijo Thomas (Microsoft)** 11:26 But… Yeah.
**Björn Antonsson** 11:27 Yep.
**Cijo Thomas (Microsoft)** 11:28 Yeah, I mean, my goal is not to… Oh… breaking changes over two releases, if at all possible. We'll do it in, like, one release, so absorb the pain, like, in one shot. It's been hard because we… we were hoping to do this, but unfortunately.
**Björn Antonsson** 11:45 I'm sort of, like, wondering… I'm… More used to having like, a feature branch when there is bigger work, instead of, like, continuously merging things to main, and then not merging large things for a long while, because we want to merge a lot of large things. I mean, and they're gonna… build on top of each other, so either you end up with stacked PRs, or you end up with a feature branch that tracks main.
**Cijo Thomas (Microsoft)** 12:21 Yeah, that's also something we tried long ago, like, different brands. It also introduces a lot of extra maintenance overhead.
**Björn Antonsson** 12:29 Yes, absolutely.
**Cijo Thomas (Microsoft)** 12:31 Yeah, yeah, that's why I wasn't very passionate about creating separate branch, because then we need to redirect CIs to both and instruct the.
**Björn Antonsson** 12:39 Oh, okay.
**Cijo Thomas (Microsoft)** 12:39 distributors, right? So it's, it's.
**Björn Antonsson** 12:41 in December.
**Cijo Thomas (Microsoft)** 12:42 It's doable, like, I have done it in .NET 4, Matrix 4, we were trying not to interfere with tracing, so we created Matrix branch and worked on it.
But it was painful, like, it's… it's not super simple.
**Björn Antonsson** 12:53 Yeah, I mean, there are… I agree, there are trade-offs for all of these things, so…
**Cijo Thomas (Microsoft)** 12:59 So my, think the best way we can proceed is, like, get to the API stability issues soon, so that will give us a… good idea about whether we need to make further changes into SDK.
That's the best way, because we'll also owe to our users that we haven't had a stable API for a while, so that would also solve, like, most of the concerns.
Yeah, anyway, I'll create that issue, which is going to be, like, summarizing, different discussions from various open issues into a single one, and… See how we can tackle it.
And then there are, like, few logistics things which I probably should get some help, so there are… certain components in the contribut which never had proper owners, so I try to… Add… Oh, sorry, I created an issue for that, not PR.
Yeah, we don't have, like, active, maintenance for several crates. It's just, like, orphaned, and this is generally bad because we, we don't know whom to call.
**Björn Antonsson** 14:09 If there is an issue.
We are, working on Datadog OpenTelemetry, which is sort of, like, just flipping the names, because it lives in our repository, and that's what we consider the, the sort of, like, the blast, integration.
**Cijo Thomas (Microsoft)** 14:29 I think Scott also mentioned something like that. Yeah. Yeah. Okay.
Does it mean, like, we can start marking the existing one as deprecated, and then in the next.
**Björn Antonsson** 14:41 Definitely think so. We support more than the existing one does.
**Cijo Thomas (Microsoft)** 14:46 Okay.
Yeah, so I can… I mean, these are, like, really easy things to implement once there is agreement, so… So one less component is… yeah, and for AWS, I think someone… started looking at the PRs.
Yeah, I mean, looking at the existing open PR, so I'll give you, like, some more time. For Stackdriver, I don't have anyone, it's… it never had, like, anyone. It was, like, temporarily maintained by DJC, but I don't think he's actively looking at it either. He mentioned, like, long ago that he had some need of it in the past.
But since then, yeah, I never heard anyone, so… Yeah, I'll leave that issue open for 2, maybe 3 weeks. It's already 1 week, so another 2 weeks, and then start Doing the actual removal work.
**Björn Antonsson** 15:47 So I think, maybe I should take a look at what is existing for AWS.
We are doing… some… some AWS work as well in the same repository, integration work.
**Cijo Thomas (Microsoft)** 16:08 Yeah, it has, like, some detectors for… yeah, a lot of things, actually. See, Lambda detector, then… and there are open PRs also.
which is touching AWS, but it never got merged because there is no one Taking ownership, so there is.
**Björn Antonsson** 16:23 you know.
**Cijo Thomas (Microsoft)** 16:23 a trace ID thing, there is something else, and there is a span exporter for X-Ray. But yeah, it's been open for quite a while, and I tried to tag the… the original AWS owners, but they don't respond at all. So that's why I started wondering, like.
We should not keep components. So this is also a, like, auto-level initiative. You may have seen a few weeks ago that there was a bunch of automated PRs which removed inactive approvers and maintainers.
So similarly, I expect, like, if any things are, like, not maintained, like, we would want it to be, cleaned up, because we don't want security issues to show, yeah.
So that's, like, if you have time, like, I'll just tag you on a couple of… PRs, like, this one is just… Simple thing, very straightforward, I'll just request a review from you, so if you can approve it, I'll get it in. It's just, like, closing state PRs. We did it for the main report, this is just adding it here.
There is another thing… Which actually is somewhat related to the facing API side of things.
Let me actually open that. So there is a PR in the main report, which… yeah, I should have opened this earlier, but let me get it.
Yeah, so this is something we discussed, like, long ago. We never had the proper guidance on what APA to use, so finally I get back to this with some ideas. I think Scott just uploaded last week, so I need, like, more people to review this one before I marches, because this is, like, a huge, like, top-level decision we are… or more, like, recommendation to our end users, what you should do.
So please take a look at this one, yeah, and one of the things which we mentioned in this document is we encourage people to Start with an instrumentation library instead of creating spans by hand, and try to see if those are sufficient. If not, just enrich the existing pants, and only in the edge cases, you would need to do something manual. So this PR, now why… now I can explain, like, why I opened this one. So this is basically a somewhat new idea, which is to add CI check.
Using the tool Weaver LifeCheck.
So what it does is… Take, say, example application.
It instruments with our instrumentation library. In this case, it uses the tower instrumentation, and it just exports telemetry to OTLP.
And Beaver has a OTLP listener, and it confirms that, okay, it claims that you are doing version 1.4.1 of the semantic convention, and it verifies, hey, are we actually, producing that? So this is more like a confidence-building thing, so you'll prove that our instrumentations are, confirming to the compliance or version there.
I kept it as a draft, the reason is.
There's a lot of boilerplate code here.
**Björn Antonsson** 19:25 Yeah.
**Cijo Thomas (Microsoft)** 19:25 Just to get the weaver set up. But I have a PR in the… Weaver report to make it, like, much easier.
So I'll be able to, like, come back to this when the viewer thing is shipped, but I think if you can, like, give some directional feedback, whether this is something we… because I hope that this is going to make our lives easier as approvers, because whenever there is a PR, we can instantly confirm using an independent tool, which is Weaver. It confirms that whether we are going to break or not, from the semantic convention standpoint, so that should make it relatively easy for us to review PRs.
**Björn Antonsson** 20:01 Yeah, that sounds, sounds really good.
**Cijo Thomas (Microsoft)** 20:04 Yeah, so I'll tag you here, so if you can give some, Yeah, again, it's not fully Polish, but at least I just need some directional guidance, and some people have initially mentioned the people who are working on tower instrumentation.
They will expand on it, so all I did is just a very simple thing.
But we can expand it once the direction… it should be, like, somewhat mechanical once we do the initial thing, and hopefully we'll get more people to, continue.
Okay, I think that's pretty much the things which I have, and there is something which Scott asked, which is.
like, in the next release, along with the tracing API, we really want to get OTLP exporter To be stable, and the…
**Björn Antonsson** 20:53 Yes.
**Cijo Thomas (Microsoft)** 20:53 couple of things blocking that. One is the runtime abstraction, so he…
**Björn Antonsson** 20:57 Exactly.
**Cijo Thomas (Microsoft)** 20:58 asked me to.
Yeah.
**Björn Antonsson** 21:00 Yeah, I, review that as well. It's… it's on the list. Oh, God.
**Cijo Thomas (Microsoft)** 21:05 Yeah, I just sent a message to him today that I'll start looking at it, but then after I sent the message, I realized I kind of lied, because I won't be able to do much this week, because I'm traveling to the Observability Summit tomorrow.
**Björn Antonsson** 21:19 Oh, okay.
So you're going there.
**Cijo Thomas (Microsoft)** 21:22 Yeah, yeah, I think I'll be meeting some… get to the folks. I spoke to Amanda, you probably know her, Amanda, yeah, yeah, so… We'll be meeting.
Yeah, so most likely next 3 days is, like, complete wash. I won't be touching any first, things. But yeah, like, after that, I'll get back.
**Björn Antonsson** 21:42 Yeah, no, it, it unfortunately collides with, I'm… I'm going away, like, this week, and then early next week, for personal travel, so that was sort of like a no-go. Otherwise, I would have, liked to go there, definitely.
**Cijo Thomas (Microsoft)** 22:00 Do you know if anyone else from Datadog is coming, apart from Amanda?
**Björn Antonsson** 22:05 Yeah, I think, isn't… isn't Pablo going?
**Cijo Thomas (Microsoft)** 22:12 Oh, okay.
**Björn Antonsson** 22:13 Okay, yeah, I think so. I'm not sure.
**Cijo Thomas (Microsoft)** 22:17 Okay, yeah, I'll give him a ping, so we can plan to meet there. I met him, like, in KubeCon last year.
**Björn Antonsson** 22:23 Yep.
**Cijo Thomas (Microsoft)** 22:26 Alright, I think, that's pretty much it. We don't have anything else.
We still have, like, a lot of open PRs, but a lot of them have been, like, stale, so I put that workflow in place, so after 14 days, things get closed, or that remains the author, hey, continue working on it, or something, so…
**Björn Antonsson** 22:49 Yep.
**Cijo Thomas (Microsoft)** 22:49 Yeah, that should clear some of the backlogs as well. One last thing before we end. I hope you have noticed, like, we shipped something called Bound Instruments in the last release as an experimental feature flag, because the spec was just recently added.
For bound instruments.
So that itself is, like, mostly for inducers, but there is an interesting use case within the SDK, which is to self-instrument ourselves.
We could not do that earlier because it was too expensive. Our metrics API is, like, quite expensive because of the hash lookup sorting.
**Björn Antonsson** 23:22 And, you know.
**Cijo Thomas (Microsoft)** 23:23 Yeah, but with ground instruments, We actually have the ability to self-instrument without paying a fortune.
So I'm going to be, like, doing a lot of instrumentation work, in the SDK itself. I'm doing this for other projects as well.
So I have that fresh context in my mind, so that's why I'm actively doing it in the SDK. I'll also tag you there, see if you can review it. It's very straightforward, like, for… I'm only doing it for our processors, so whenever an item is being Processed, or draw.
because Q is full, we emit a metric.
So very simple, and it follows the existing convention. So the reason is, like, there are people complaining about, like, data… silent data loss. We don't have a consistent way of letting users know that we are losing data. So this is just, like, one step towards it.
I'm not sure whether that dog has seen such complaints, but I'm seeing, like, such complaints, in many places, like.
extremely public places, like LinkedIn, Reddit forums.
**Björn Antonsson** 24:25 Oh, yeah, I mean, we definitely, we definitely are very mindful of, sort of, like, tracking how many things, We think that people have produced, and how many we process, and how many we send, and how many we drop, and sort of, like, just making that as transparent as possible, so you can early on notice if you have problems.
So, yeah.
**Cijo Thomas (Microsoft)** 24:50 Okay, yeah, I tagged you there also. It's a very small PR, like, probably takes, like, a couple of minutes, so we can start doing that, yeah. And I also started a design document for observability, which is starting with a very minimal thing.
But yeah, hopefully we can expand that and give the users, like, full visibility whenever we do, drop things.
**Björn Antonsson** 25:11 Excellent.
**Cijo Thomas (Microsoft)** 25:13 Alright, I don't have any other topics, so let's meet again next week. I'll try to find a different slot. I'll do a poll in the Slack to see whether there is any better time that works for folks.
What time is it for you? Yeah, I forget, like, which… you're somewhere in Europe, but so, what is the time for you right now?
**Björn Antonsson** 25:32 It's right now 6.30.
**Cijo Thomas (Microsoft)** 25:34 Okay, so it's already too late, so most likely we'll have to do something much earlier in the Pacific time zone, like 7 to 8. My time would be somewhat, I think, 4 o'clock for you.
**Björn Antonsson** 25:45 Yeah.
**Cijo Thomas (Microsoft)** 25:46 Yeah, I'll probably have to stick with that, because 8 to 9 is very hard. That's where my buses go, so 7 to 8 is… Relatively easy, I can just, join early and then go to OFI. So, anyway, I'll do a poll and see what everyone thinks.
**Björn Antonsson** 26:00 Cool.
**Cijo Thomas (Microsoft)** 26:02 Yeah, alright then, thank you, see you next week. Bye-bye.
**Björn Antonsson** 26:05 See ya. Bye.
