SIG: Go Auto-Instrumentation SIG
Date: 2025-09-16
Duration: 17 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn** 00:38 Hey.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 00:40 Okay.
**Tyler Yahn** 00:42 How's it going?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 00:44 Alright.
Yeah?
**Tyler Yahn** 00:47 Yeah, going pretty well. Just, like, 20 things to do, not enough time to do any of them.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 00:55 Yeah, exactly.
**Tyler Yahn** 00:56 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 00:57 It's a total loss for me.
Trying to catch up on things today.
**Tyler Yahn** 01:08 Yeah, I'm saying, I'm just trying to… Get everything picked up, but yeah.
Hey, Mike.
**Mike Dame** 01:36 Hey, guys.
**Tyler Yahn** 01:38 How's it going.
**Mike Dame** 01:40 Good, thanks.
**Tyler Yahn** 01:42 Nice.
Do you know if Ron's able to make it today?
**Mike Dame** 01:50 I'll check, let's see, what's he up to?
He might be on a call that should be wrapping up.
**Tyler Yahn** 01:59 Oh, okay.
Yeah, not… oh, there he is.
Answers that question.
Well, cool. Well, we can probably jump in here in just a second. I don't have too much on the agenda right now, so if you have agenda items, you wanted to talk about, or, ideas, go ahead and add them there. If you haven't yet, please also go ahead and add your name to the attendees list. I think everyone's on there.
Yeah, And so, yeah, we can start off… I just wanted to, I guess maybe just start off, so we did have the last release, the V0, 23.0, last week, so, happy to get that out. There was a few, nice fixes and, features. I think the, auto-detect thing got released last time, so… yeah, dropped support for the Go 123 as well, in this next release, so… Yeah, that's coming up. There's a little bit of a bug that went out yesterday for the auto SDK, Turns out 386 architecture, or just 32-bit architecture in general, is something we need to support for the SDK. If you weren't following along, it's not something we… plan to support for the auto instrument rotation, so that wasn't, like, added. It's just for the SDK itself, and that's more for OTEL, because OTEL does, like, the upstream needs to support Well, it does support 32-bit architecture, so, yeah.
Anyways, that's a lot of catching up on things that already existed.
Okay, so looking at the open PRs, that's on the agenda, I think this just needs, I think, another review for me hasn't yet. It's just a linting one. I think the only real issue, or one here is from Ron around, Improving the decoding events, reading the profile for instead of just copying the bytes itself, it's actually just doing a type change, using an unsafe pointer here to point at the raw memory.
This seems, fair. Rafael pointed out that, there may be a good idea to do a type check itself, and Rod, you looked into, like, using some sort of zero-value type check, but noticed that it was causing an allocation?
**Ron Federman** 04:28 And, yeah, that, piece of, like, the link that Rafael, put there.
So, I looked at the… Like, size, check… Like, I'm not sure, it looks like it does an allocation, but probably it's, like, a local stock stuff, so maybe it's… it's not really a HIPAA location, so… It's not that bad.
Yes.
**Tyler Yahn** 04:55 Oh, did you… oh, okay. I… yeah, because I was kind of surprised to hear that this was actually doing an allocation, so did you not, run a benchmark to validate this?
**Ron Federman** 05:04 No, I haven't checked it.
**Tyler Yahn** 05:07 Oh, okay. I… yeah, the compiler is usually pretty smart to see that this isn't actually gonna leave the scope, and it won't actually do an allocation, and usually, I mean, you can go look at the actual instruction sets, but yeah, I'd be very surprised if… this did an allocation, although I guess I'm not completely as surprised, because sometimes the unsafe package does some unique things.
Also, that it's gonna… depend on, like, the version as well, but, like, yeah, I think that that'd be… Yeah, I think that that seems like something that wouldn't actually happen, but I was kind of surprised it did.
Otherwise, I, I, yeah, I, I don't… I mean, I can… I can… I can validate that as well, like, if you wanted some help looking at a benchmark for that.
**Ron Federman** 05:54 yeah, sure. I can also double-check this.
allocation stuff.
**Tyler Yahn** 06:04 Yeah, I mean, okay, yeah. I mean, I would definitely be interested to do that, I mean, because it's just a nice… you know, sanity check before just blindly doing this, because… I mean, in theory, like, it should get caught in our CI system if things change.
And we should never release it, which is kind of, like, the whole point of, like, panics and stuff. But I guess this is just, like, being very defensive and saying, like.
hey, even if this does get past our CI system, like, we'll still have something to catch this.
Yeah.
I guess also, maybe the only other thing, now that I'm seeing it again, is we might want to use this unslake slice data, here.
it's not the end of the world. It's just, it simplifies this. But anyways, that's not… that's just a minor point. I think that this actually seems fine the way it is, if we wanted to add that, type check, I think that makes sense. I… yeah, like I said, like, we can take a look at the allocation, though. I'd be interested to see if that actually is getting allocated. It would be a little surprising, but… So yeah, I… I'll let you… take a look closer at that, Ron. If you need some help, just ping me, I'm happy to help on that as well.
It should be pretty straightforward to look at something like even the Go Playground to find something out like that.
But otherwise, yeah, if you have time, please take a look at Ron's PR. I think that's really the only PR we have open that is, not an update. This probably needs to get closed.
So, yeah.
Okay.
Mike, you wanted to make a request to join the LLM?
Do you say observability?
**Mike Dame** 07:51 Yeah, I just wanted to make another shout-out to this. Tyler, I don't know if you were on the call a couple weeks ago when I mentioned this. LMD is a fairly new project that's going on. It's a Kubernetes, kind of sub-project, a lot of people from the Cates community going there. It's kind of a control plane for running, LLMs on Kubernetes, deploying them and scheduling them. The SIG observability there, is starting up, and they're looking for how they can observe this control plane. It's, it's, you know, all written in Go, so I think it's pretty relevant to people here. I think, Tyler, maybe you specifically, because they're, they're interested in, using eBPF.
to, you know, take advantage of, I think, mostly the overhead benefits of you know, LLM calls are… the, like, overhead is very costly to them, so offloading that. But they also have a lot of questions about manual instrumentation, how manual instrumentation can connect and link into the auto instrumentation. It's actually, Sally, who I think you probably remember from when we did our DevConf talk, is the SIG lead over there, so… Yeah, it's not moving very quickly. We've got a couple proposals. I'm not sure if I put the links to those proposals in here. I'll add those links to the proposals that they have. They have a couple open issues where there's been a lot of questions, you know, even just… just open telemetry experts is really what they need, people that can talk about, you know, semantic conventions, they're looking at the types of attributes they should be adding, the types of spans they should be making, reporting the status of those spans, but… I could use some backup, because there's some questions that I don't even really know the answer to, and a lot of doubt in does the EVPF stuff really work? I think a big benefit to this project for us getting involved there is because I think that they are a good candidate for using this projects repo, the OpenTelemetry Go instrumentation, the library itself, and I know that we've been looking for some more use cases to kind of help drive, kind of, parallel design that API as someone else using it.
Because I think that they aren't really looking to pull in a full dependency from, you know, one of the bigger projects like OB or Odagos that, you know, provides a lot more than they need, and I think that it would be good for them to kind of tailor it, or at least try to see how it looks if they do try to tailor and import this themselves.
But yeah, any more feedback and input, and, you know, we're the experts here in the OpenTelemetry eBPF space, and even the manual SDK space, too, we have, so, check it out. I'll add the links to those specific proposals. There's another one for VLLM itself, so it's also a good way, too, if you've been interested in… some of the AI stuff, I mean, I haven't really, myself, hopped on the AI bandwagon much, but this seems like a cool way to get in and learn a little bit about what running these looks like. So, I know we usually kind of wrap up with, has anyone seen any, you know, cool use cases of OpenTelemetry VPF? I think this is probably one of the coolest ones so far.
And yeah, there's gonna be, I'm actually gonna be at DevConf again on Friday, and I'm sure there'll be some more talks about LLMD there, so, anything that we find from that. I think that there's still some virtual tickets available, but… it's always a good… good conference, as… as Tyler knows. It's a… it's a fun, small thing in Boston, but yeah, this… this group in particular, I think, would be a really good fit for, joining that… that SIG over there and lending them a hand. And, you know, it's… very early in the project, so you get to really help shape it. That's my pitch.
That they meet.
**Tyler Yahn** 11:53 Yeah, I noticed that Thursday, it's 12.30 Eastern Time, right? So that's, 9.30 Pacific time, right?
**Mike Dame** 12:03 Yeah, see…
**Tyler Yahn** 12:04 That, of course, overlaps with the GoSig meeting on alternate weeks as well. But it's every other week, so I'll try to, join, I guess, every other week, maybe.
**Mike Dame** 12:16 Yeah, and honestly, if that's the case, we could… I think it's still at the point where they were even talking about trying to find, you know, different times that work for people for the SIG, and especially if it's overlapping with the Go OpenTelemetry SIG, like, there's a lot of people, like, they're not just looking at eBPF stuff, they're trying to say, okay, what if we do manual instrumentation? I've been trying to explain the Auto SDK to them, and… sort of explain, like, yes, you know, these… these spans will link in with the auto spans, too, and you can optionally provide… set up a tracer provider or not, whatever you're looking for. So, they… they really need people that know a lot about this, so, yeah, that's always something that we could bring up, but even if on the alternating weeks, if you could join, that'd be great.
**Tyler Yahn** 13:00 Yeah, I, I… I will… I'll put it… I'll… actually, is there a calendar invite for it?
**Mike Dame** 13:07 Yeah, I think, so the link that I put in that one's meeting notes, if you join this, Google group… Yeah. …is in there. You join the Google group, you'll get an invitation to the LMD, calendar.
Yeah. And… Yeah, that… it takes a little bit sometimes with Google Group invites. I don't know how often they go out, but… and I do have one of the distributed tracing proposals linked in here. It's on the September 2nd notes.
**Tyler Yahn** 13:35 Yeah, okay, yeah, I'm sorry, I just looked through, like, a few links, but I'll look more after the meeting, and try to get signed up.
**Mike Dame** 13:42 Paste them back up in there. Yeah.
Yeah, check it out. Yeah, like I said, there's not too much going on in it right now, but they have some ideas, and we're kind of trying to put together some proof of concepts, and try to figure out what is the end path for tracing. They're really… they are also really interested in metrics, too. They're obviously, you know, trying to get metrics out of this, so they've been asking about eBPF for metrics, eBPF for hardware metrics from, like, GPUs that are running the LLMs, so, I think this could be a really interesting space for us to get into and, mutually benefit that project and this project by helping us Get some feedback.
**Tyler Yahn** 14:23 Yeah, and I think, like, the LLM semantic conventions right now are still pretty… Early in development, as well, so having… having some feedback from, like, this platform would help, I think, shape some of that. There's also that SIG as well, but yeah.
**Mike Dame** 14:39 Yeah, yeah, and like I said, it's also just general, like, they're not… they don't have, I don't think, a whole lot of… deep open telemetry experience, and so even some of the higher level concepts of, like, you know, there was some feedback in the proposals of, like, you don't need to add your own attribute for status, like, status can be reported in the span. So those kinds of things that, you know, like, I can't think of a better group to help out there, so…
**Tyler Yahn** 15:07 Well, cool, yeah, thanks for, it out. I'll try to make it in everyone else as well. There's definitely some more expertise that could be needed there, it sounds like.
**Mike Dame** 15:16 Absolutely.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 15:17 Sounds like… yeah, thanks for mentioning it, yeah.
I mean, OBDISC collect GPO metrics, for CUDA.
Oh, okay.
**Mike Dame** 15:25 Yeah, I mean… That could be something that we definitely… or, you know.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 15:29 But it's only CUDA, it's only NVIDIA, we don't have support for other graphic cards, but… It was a picture.
**Mike Dame** 15:36 I mean, I think that they were talking about getting some of the CUDA, you know, metrics out of there, but that… that's… so if you can… like, I don't know anything about what OB does for metrics, so, like, even just you joining one of these calls and being able to talk about what we do for metrics would be great.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 15:51 Yeah, I'm actually giving a talk on that, for SRECon, on OB and the GPU metrics.
Yeah, it's quite interesting what, what you can do if you optimize your GPU workloads, and it's like night and day. You show the metrics, and it's like, there's an obvious problem, you're not able to use the GPU, and then you run these optimizers on top, and then night and day. It's like, latency goes half, and… And you… you were effectively using 100% of the GPU you paid for.
**Mike Dame** 16:24 Please share that talk, and, you know, come join the SIG, too, because I think that that's right on the line.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 16:29 Yeah, talk is in October, so… but I can, I can give a preview, for sure.
**Mike Dame** 16:33 Yeah, cool.
Thanks, guys.
**Tyler Yahn** 16:36 Awesome.
Well, cool. Alright, that's the end of the agenda. Any other cool projects or fun things, people are working on?
Or other topics related to the SIG.
If not, I guess we can end it early here.
Yeah, well, I'll definitely check out those links, so thanks again, Mike, for bringing that up, and I'll see you all probably tomorrow, otherwise, see you in a week's time, or asynchronously. Alright, bye.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 17:10 Bye.
