SIG: System Sem Conv Stability WG
Date: 2026-02-19
Duration: 19 minutes
============================================================

## Zoom Recording Transcript

**neil yashinsky** 02:03 Hello, how's it going?
**Donal O'Sullivan** 02:06 Not too bad.
What's this?
James, follow notaker.
**neil yashinsky** 02:13 Yeah, I've seen a few of these in some of the other ones, and I think almost universally they've been getting booted, because it's like, there's already notes, there's already recordings, like, how many notes and recordings do you need?
**Donal O'Sullivan** 02:29 How do we disable this?
**Christos Markou** 02:33 I can kick this out. I'll try doing this now.
**Donal O'Sullivan** 02:39 That AI note-taker was back as well, I kicked it out, said Bogdan Nicole added read.ai meeting notes to the meeting.
**neil yashinsky** 02:50 Yeah, I wonder even how often people are explicitly doing that versus, like, you know, it's like bloatware or whatever. They opted in, and they don't even… people don't really… I don't think people are intentionally sending a lot of bots to meetings without attending. Certainly some, though, certainly some…
**Donal O'Sullivan** 03:06 Yeah, yes, for sure.
**Christos Markou** 03:37 Okay, done.
**Dmitrii Anoshin** 03:42 Hi, everyone.
**neil yashinsky** 03:45 Hello.
**Christos Markou** 03:49 Seems, we don't expect anybody else any topics for today.
Seems the agenda is pretty much empty today.
**Braydon Kains (Google)** 04:03 Yep, I've unfortunately been… sidetracked with unrelated stuff recently. I haven't been able to make any… Any progress?
**Christos Markou** 04:16 Cool. I guess in that case, if we don't have anything else, we can keep it short today.
**neil yashinsky** 04:21 Yeah, your struggle is real, I know the feeling, so, yeah.
**Braydon Kains (Google)** 04:24 Wow.
I'm bursting at the seams a little bit.
**Christos Markou** 04:29 Oh, we have Josh, yeah.
I'm not sure if he joined for a specific reason, or…
**Josh Suereth** 04:38 Oh, this is just… I'm… I'm your liaison, so I'm just checking in every once in a while, and I haven't been here in, like, a month or so? Maybe two? So, just want to see how things are going. Nothing… nothing…
Nothing urgent on my side. But everyone seems to be wanting to launch crap for KubeCon, and so… just checking in.
That's all.
**Braydon Kains (Google)** 04:58 Yeah.
**Christos Markou** 04:58 Nice.
**Braydon Kains (Google)** 05:00 So, we… we've been looking at the process namespace release candidate. That's… that's been our… our, sort of, North Star.
The,
Some of the… some of the… a lot of the blockers are… are relying on me, and I've been…
Stuck in other… in other ways that I haven't been able to dedicate the necessary time.
**Christos Markou** 05:28 I think since last time we clarified, though, the plan, so…
Yeah, but we didn't manage so far to…
like, get into this, I guess, but yeah, that's fine.
**Braydon Kains (Google)** 05:56 I do have a… a Weaver question, if we have a second, Josh.
Part of the…
semantic convention stability stuff in the collector, which is related to this, is… I was working on making, like.
semantic convention,
unit tests, like, that validate the… whatever metrics and attributes you produce are correct according to Weaver, and that…
uses Weaver as a test container under the hood.
The thing I found is that
Weaver's registry live check is not super well designed for that. Like, the current solution is, like…
have Weaver output to a file, and, like, FS notify when the file is written, and then parse from that.
So, I don't know if Weaver would be… okay with introducing JSON ingestion?
Because if we could do that, then we could make our JSON request, get an answer back that has a bunch of stuff. It does?
**Josh Suereth** 07:00 It already supports JSON ingestion, yeah.
**Braydon Kains (Google)** 07:02 The registry life check does.
**Josh Suereth** 07:04 Yeah, live check, you can pass it a JSON file as input instead of OTLP.
**Braydon Kains (Google)** 07:08 Oh, I was thinking of a JSON, like, request, like a web request.
**Josh Suereth** 07:13 at JSON web request.
You mean, so, LiveCheck will open an OpenTelemetry endpoint, and you write in?
**Braydon Kains (Google)** 07:20 Which is gRPC.
**Josh Suereth** 07:22 Which, oh, oh, you need it to be HTTP, not just gRPC.
**Braydon Kains (Google)** 07:27 So what I was… what I was thinking of is, if we could… if we could pass, like, have a JSON endpoint and receive a JSON response.
then Weaver could also
include the findings in a JSON response. Like, doing that as part of a proto-response is prohibitively difficult, but as a JSON response, just chunking a bunch of data in there.
**Josh Suereth** 07:46 Yeah, like, there's…
There's been some… so what I would recommend is I just open a feature request. Jeremy's usually really responsive with these things, and we've been trying to make improvements. So, one of the… one of the recent changes that was made is, instead of it outputting a file.
of the findings, you can actually give it an OTLP endpoint, and it will fire back at that.
So you could spin this thing up, and it will… and you write in your OTLP, and it will fire back its findings as OTLP logs back to you.
**Braydon Kains (Google)** 08:19 Oh…
**Josh Suereth** 08:21 If you wanted.
**Braydon Kains (Google)** 08:21 Didn't see that. That might work.
**Josh Suereth** 08:23 Well, that's new, that's, like, the latest release.
**Braydon Kains (Google)** 08:25 Okay, okay.
Okay, I'm… let me think about that, I'm… yeah.
**Josh Suereth** 08:30 your, your issue…
was already a… like, somebody already proposed a, you know, like, hey, this is a problem, can you fix this? I like what you're suggesting as an option, too, so I still think you should make a feature request of, like, hey, could I post to it and get back a response that's just a JSON of all the violations? That would be pretty cool.
But yeah, like, like, I think still open your issue asking for the feature, but you're not alone, like, everyone who's been trying to use Weaver in that case is making feature requests and trying to improve it, and we're trying to sort out the details, so…
**Braydon Kains (Google)** 09:05 Yep. Yeah.
**Josh Suereth** 09:09 And in terms of turnaround time, we're trying to cut releases every month, so, if you have something that's urgent, and you want us to get it out quicker, not a problem.
**Braydon Kains (Google)** 09:21 Okay, awesome, I will… I will do that then. But the…
That… the fact that there's already something that will, like, send gRPC back, that already is better than what we were trying to do. So, I'll talk to… I'm collaborating with someone upstream in the collector on this, so I will… I'll talk to her and see.
If she can take a look at that.
**Josh Suereth** 09:40 Yeah, I posted the fixed issue, where we were trying to do Weaver in test containers in Python.
**Braydon Kains (Google)** 09:50 Yep.
**Josh Suereth** 09:50 And that's where…
**Braydon Kains (Google)** 09:51 It'll be the same problem as we're experiencing now.
**Josh Suereth** 09:54 Very similar, yeah, yeah. And this is, you can follow the PR that Jeremy put to kind of add some health checks and stop endpoints and that kind of stuff here for how that works. Okay.
there's a proposal for more things. Anyway, just open feature requests, please. Like, the…
it can get better, we need to know what problems you're having and how you're using it. So just open a feature request, and don't be afraid to.
**Braydon Kains (Google)** 10:21 Sure, sounds good.
**Josh Suereth** 10:45 By the way, if you haven't saw, did you see that we have a Weaver packages now that we're building out?
**Braydon Kains (Google)** 10:52 Oh, I did… I did hear about it. I've… I don't fully understand what it is. This is the, like, the allowing, like, separate repos to create their…
Their own, like, semantic conventions with policy enforcement.
Yeah. Like, a federated project, basically.
**Josh Suereth** 11:10 Yeah, so, like, in the collector, if you want to use the exact same backwards compatibility checks that we use in Weaver, this is exposing those policies that you can just reuse them in your build, instead of having to, like, pull them from Sumcov, and they don't actually work, because your definitions are different.
We're abstracting everything so it can work generically across any repository.
And then, like, the idea would be, in OpenTelemetry, there'd be a set of enforced policies you have to abide by, like our naming conventions, stability requirements, and backwards compatibility.
And you would… we'd make sure that you have all three in your repo, and from there, you can do whatever you want, right? Because you're… you're… we're enforcing the compliance that we need.
And then, if you ever decide to take your local collector stuff and feed it back into SEMCOV,
you're already compliant with the rules. Like, it just… it's trivial for us to take that back in if we wanted to make it a broader thing.
**Braydon Kains (Google)** 12:12 Cool. I can… I can… I can see the vision a little bit from… It's…
Yeah.
**Christos Markou** 12:26 So that means that if we include these, require… as requirements in the collector, Anything new,
Should abide by these rules, and…
If we eventually… whatever we add from that point will be semantic conventions, let's say, compatible, right?
**Josh Suereth** 12:46 That's the idea, yeah. I mean, there's a chance we don't get it right, but theoretically, that's what the goal is.
**Christos Markou** 12:56 Cool. Yeah, I was also wondering about the naming issue. For example, I've seen that people are trying to add things, and they don't necessarily check if something similar exists in some other conventions already.
And most of the times, PRs are merged, they claim that, okay, it is experimental, I can check this out later. Yeah, maybe one check would be to, I don't know.
how we could ensure this, with something like a registry or something. To ensure that we uniquely identify… we uniquely define something somewhere, and from that point on, we know that we should either follow this or revisit this and change this.
That's, that's my idea.
**Josh Suereth** 13:42 Yeah, my thought there, and you can hate me for this, but
My thought there is to actually try to use Copilot for it. One of the things that LLMs are very good at is, turning semantics into…
a vector, where when you're close enough in vector space, you know that they have same semantics. So, actually, using that kind of an algorithm to detect if you're defining a new thing that's similar to something that exists.
**Christos Markou** 14:09 Alright.
**Josh Suereth** 14:10 we might actually have really good coverage from an LM. I don't know… the problem is, I expect tons of false positives.
But if we're comfortable with that as, like, just a, you know, an initial review, so anytime someone makes a change to YAML separately, we have, you know, an AgentMD that describes how to look at SemComp and do the comparison, just to give you a little bit of coverage, right?
I think as long as the… we don't get false negatives, I think that would be ideal, because it… it would help, and then you don't have to…
We have a level of baseline…
attempt to abide by that, but I don't think there's an automated way we can do it without something that actually turns, you know.
English into semantics, and then does vector comparisons of them, so… That's LM.
**Christos Markou** 14:59 Yeah, I see. Yeah, interesting.
**Braydon Kains (Google)** 15:13 One thing we'll have to handle if we're… if we were using Weaver packages, or if we were, like.
starting to use LLMs to check this sort of thing is that the… the…
metric definitions in mDataGen YAML files is…
Similar, but not the same, necessarily.
So, like, exact automated checks might be difficult, or we would need to write some sort of adapter.
For, policy checks, if we wanted to automate them that way.
**Christos Markou** 15:45 I think, somebody tried that, I think it was Antoine. He… use the…
the spec file that, he used the spec file, and then Weaver to produce the mdata gen YAML file, or something like that.
**Braydon Kains (Google)** 16:01 Oh, right, yeah.
**Christos Markou** 16:02 something like a transition. That was, that was a smart idea, I think.
At least as a transition phase, or something.
**Braydon Kains (Google)** 16:27 I don't think I have…
**Josh Suereth** 16:28 No agenda items? Yeah, I was just gonna check. Sorry.
**Braydon Kains (Google)** 16:31 Yeah, there… there wasn't.
**Josh Suereth** 16:33 Okay.
**Braydon Kains (Google)** 16:35 I've been too busy.
**Christos Markou** 16:38 Yeah, I know I've been, like, pushing for these jobs, but if we can have a release, we'll… I will be glad for this. I want to port back the KHCMAT conventions to the collector.
Yeah.
Is this hard to have the releases? I wonder if we could help somehow. I guess we don't have permissions, but, yeah, I would be glad to help if I could.
**Josh Suereth** 17:03 Yeah, yeah, yeah, so it's not, it's not hard, it's just not automated.
So, yeah, it's more a matter of us paying attention and then getting to enough folks. One of the things we have right now is there's a lot of… a lot of our maintainers are on vacation.
**Christos Markou** 17:21 Okay, okay.
**Josh Suereth** 17:22 So, yeah, but I… thank you for reminding me. I was gonna do that this morning, and I totally forgot, so I am going to start that now. I pinged all the maintainers, and we're okay cutting and released today, so, I'm going to start working on that now.
**Christos Markou** 17:38 Cool, cool. Great. Thank you.
**Josh Suereth** 17:41 If you're curious about the process, by the way, and like, and you wanted to help us automate it, feel free, because that would be amazing. Let me give you the link to the releasing. Everything's document… oh man, come on, Zoom, where are you actually? I hate these embedded windows that everyone does.
**neil yashinsky** 17:58 I know, no, you're 100% right. Like, doesn't matter how many times you've used this, and then they just go ahead and move things.
**Josh Suereth** 18:06 Yep. So there's the, there's the link. It's, so that's our releasing instructions. It's not… it's not too bad, it's just, it's a little bit of work.
I think the main thing is, a human, has to send the PR today,
Yeah, interesting, we have to create a release milestone now. We… it looks like Trask did automate it, so there's an OpenTelemetry I.O. workflow. Oh, right.
So you have to check whether or not we've broken the website, then we have to, notify them if there's a problem, then we can create the release, and then once we create the release, everything's kind of trivial.
it's mostly that first thing can be very problematic if, there's some sort of disconnect between the, like, all the Hugo stuff from OpenFilmTree.io and what's happened locally.
it's very easy to put bad markdown in YAML, it turns out.
**Christos Markou** 19:04 Yeah, I see.
Cool, okay, thanks for that.
Yeah, I guess if there's nothing else, we can… I'll keep it short today.
Okay.
Thank you, folks. See you next week. Bye.
**neil yashinsky** 19:25 See you, Christos. See ya.
