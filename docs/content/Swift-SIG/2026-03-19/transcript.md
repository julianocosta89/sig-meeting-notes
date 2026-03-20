SIG: Swift SIG
Date: 2026-03-19
Duration: 11 minutes
============================================================

## Zoom Recording Transcript

**Ariel Demarco** 03:31 maybe not… Vinod Vydier 03:33 Hey, Ari, how are you?
**Ariel Demarco** 03:35 That's about… Vinod Vydier 03:38 Yeah, we are, all, I think… Getting conflicting meetings at the same time.
**Ariel Demarco** 03:46 No worries.
I'm also on the car park, waiting for my wife from camp to… From the doctor, so… so don't worry.
**Vinod Vydier** 03:59 I see.
**Ariel Demarco** 04:00 You know, you should… Vinod Vydier 04:01 As a solution.
**Ariel Demarco** 04:02 He's.
**Vinod Vydier** 04:05 No, that is a big change, right? Because, I think we are moving towards, Events API, so I think we gotta… that's why the span events is getting deprecated.
**Ariel Demarco** 04:17 Yeah, that's in favor of the events API, isn't it?
**Vinod Vydier** 04:22 Yeah, yeah, yeah, yeah. Events API or logs.
One of the two. I mean, in case of mobile, of course, Events is better.
Because it's hard to collect the logs, yeah.
**Ariel Demarco** 04:33 Yeah. Yeah, yeah, yeah.
I'll send you.
**Vinod Vydier** 04:36 Yeah.
**Ariel Demarco** 04:37 It's going to still be supported as far as I read, on the collector side yet.
Still.
**Vinod Vydier** 04:43 On the collector side, I think collector already is, supporting Yeah, it is already supporting, events.
**Ariel Demarco** 04:54 Okay.
**Vinod Vydier** 04:54 Yeah, yeah. Because I… Ariel Demarco 04:56 to read the events plan API type of place.
**Vinod Vydier** 05:01 Beautiful.
**Ariel Demarco** 05:01 to be honest.
**Vinod Vydier** 05:02 Yeah, yeah, yeah. And because, you know, a lot of, there are a lot of other telemetry signals that you can send, right? So, I think events is kind of a catch-all.
**Ariel Demarco** 05:14 Okay.
We also have to implement that.
**Vinod Vydier** 05:20 Yeah, yeah, yeah, exactly.
I think, Bryce?
**Ariel Demarco** 05:25 Right.
**Vinod Vydier** 05:26 Yeah, yeah, something, you know.
**Ariel Demarco** 05:28 Yeah, but he did it prior to… before we changed the repository structure, so I think it was a draft PR on the OpenTelemetry Swift.
And when we migrated from telemetry.
core. I don't think he… he recreated.
**Vinod Vydier** 05:49 Oh, okay.
**Ariel Demarco** 05:51 I think it's a matter of recreating it and… I started.
**Vinod Vydier** 05:55 Yo, you know.
Oh, you're right, right, right, because of the… After the repos are split, I think we need to add some of that here.
**Ariel Demarco** 06:07 Yeah. So, I think that, regarding the issue that you submitted, it's both… Vinod Vydier 06:14 Both.
**Ariel Demarco** 06:14 adding to the docs, and also… Like, linked to the… the other… what do you say, how you said, to the other… Thing that is missing that is… basically the… Do you have its API. Construction.
**Vinod Vydier** 06:33 No, I, yeah, I think after the repos got, split, I haven't really, no… I need to actually start, building it with both, yeah, I think I should… I just put it in the Swift, because that was a… That's kind of the… repo that I used to be more familiar with. So now that we only have the Now you have the core, and then you have the instrumentation here. Yeah, I need to start… Yeah, we should… we have to put it in core, right, first.
Before we… And you're helpful.
So if, yeah, if it's just the two of us, I think, you know, we can, Meet next week.
And.
**Ariel Demarco** 07:24 When this occurs to Instagram, so… Vinod Vydier 07:26 Okay.
**Ariel Demarco** 07:28 Why?
Payback.
Okay.
**Vinod Vydier** 07:34 Okay, sounds good. We'll talk next week, then.
**Ariel Demarco** 07:36 I'll… I'll write that down on the GitHub issue, so… We also have that in place, that we had to do that.
**Vinod Vydier** 07:45 Yep.
**Ariel Demarco** 07:46 I'll use this time to basically upload PRs, merge the ones from Renovate, and… Yeah, and see. There's no other issue, as far as I can see. Just the one that you opened, and… In terms of PRs.
I don't know if you met last week, because I haven't seen an entry for last week.
**Vinod Vydier** 08:09 Last week we briefly met, Nacho was also, I think he had to jump off, so we briefly met, and we said, okay, we'll… Meet up next week, and Yeah, I don't think we did a whole lot, so yeah, we can… Ariel Demarco 08:25 Okay, there's a… there's a… there's a new PR on OMPA Telemetry… On the normal PR?
**Vinod Vydier** 08:31 Okay.
**Ariel Demarco** 08:32 Distributed Tracing Bridge.
**I have… I have to read it… read it through, but… Vinod Vydier** 08:39 Okay.
**Ariel Demarco** 08:39 It's also linking to some other issues.
So… Yeah, I'll take a look at that one. Okay.
I haven't seen it, to be honest.
**Vinod Vydier** 08:50 Nope, nope.
**Ariel Demarco** 08:52 Anyways… Vinod Vydier 08:55 Okay.
**Ariel Demarco** 08:57 Well, I… you have another meeting right now?
**Vinod Vydier** 09:00 Yeah, yeah, I have some… another meeting that is running in parallel, so I said, okay.
**Ariel Demarco** 09:05 Okay, go there, go there, no worries.
**Vinod Vydier** 09:07 Alright. Excellent.
See ya. Bye.
