SIG: OpenTelemetry on Mainframes Weekly Sync
Date: 2026-11-18
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Rüdiger Schulze (International Business Machines Corporation)** 02:47 Hey, Matt. Today, again, from the car.
**Matt Hogstrom (Broadcom Corporation)** 03:00 I'm on mute.
**Rüdiger Schulze (International Business Machines Corporation)** 03:02 Aye.
**Matt Hogstrom (Broadcom Corporation)** 03:03 Are you driving, or are you waiting for kids?
**Rüdiger Schulze (International Business Machines Corporation)** 03:07 I'm waiting for kids, they are at the soccer training right now, so just turn For the boys.
**Matt Hogstrom (Broadcom Corporation)** 03:14 Yeah, I got it.
**Rüdiger Schulze (International Business Machines Corporation)** 03:15 Okay, so… Let me just update the meeting notes.
One second… Let me share my screen.
So there's a couple of things, maybe to mention. I've seen you commented on one of the… DPRs, so, As we said earlier, right, to split this big PR, sorry, 20, this is now being split into 37 small PRs.
**Matt Hogstrom (Broadcom Corporation)** 04:48 I started going through them, I'm sorry, I should have done it earlier.
**Rüdiger Schulze (International Business Machines Corporation)** 04:55 Yeah, glad that you, that you get on it now. All good. The… the interesting one to start with is, as follows, so… the… the PR, 47. That's actually kind of like the… the entry PR, where certain other things then depend on.
So, if… if we could, actually make progress with this one, that… that would be good.
Okay. Let me put this here.
And, The other one, so 43, I think, I think the 44 you commented on, that was really about, because we started from the Gen AI, Sure. Federate, so this was kind of like the base.
43, I think, is about the tooling, so that should be straightforward, and might be that we have to go back to that one anyway at some point. And, Then… 46 is… Yeah, this is something… I don't know, actually, how much this is a discussion generally, but… You know, obviously LPAR is a standing name, but there are also discussions around more aligning with the ecosystem. LPAR wears this partition as one of these examples. I suppose there will be more coming in future, I think of… storage versus memory, so… and I guess as we go, we will see some of this, maybe, to be also discussed here on the CIC in terms of which of these names to use moving forward. And, Partitions seem to be a better fit here from a… From alignment with the ecosystem.
**Matt Hogstrom (Broadcom Corporation)** 07:05 Yeah.
**Rüdiger Schulze (International Business Machines Corporation)** 07:06 D… Right. Then there was this AI-generated comments from… from Pellaret, he was on, I think, 2 weeks ago.
Obviously, again, AI is our friend here, so… the… so AI responding to AI, apparently, but, incorporate them.
**Matt Hogstrom (Broadcom Corporation)** 07:31 Okay.
**Rüdiger Schulze (International Business Machines Corporation)** 07:32 So we've… I mean, as we review, and I will also take some time to read through each of them again, but… Sure.
that's, that should be incorporated, and there will be more. I don't know if you have seen the latest comment from, Antoine on the Mainframe Slack channel. He was actually offering options, either go with a big one or split it up, and then… I have it reviewed, also to you guys over his redshot. So, I will post a couple of comments on the Slack channel.
And, I also need to include you, this just came up yesterday. There is a new Slack channel now, which is, I think it's from the governance committee, somebody contacted us, and Craig is still on the Slack channel, so I will swap you with Craig.
Okay. I think this is more about, actually.
having, a contact also with the… with the GC to… Sure.
You know, stay in contact, and also there's somebody in from… from the semantic conventions, where I worked earlier with, so I had at least some exchange, and I think we really need to get him to, also look at virtualization, because he had a point of view at that time when we spoke.
So I will post a couple of comments on these two Slack channels, and then I think we are actually on a good way now to get things done.
Okay, that's it for today, Matt.
**Matt Hogstrom (Broadcom Corporation)** 09:07 Okay, the only… I think one… one comment I've made a couple times, I don't know when to do this, but before we, like, even make the one change, I'd rather change Mainframe to S390X.
Because it's consistent, and then it's… I think all the other sub-data kind of… starts to make better sense. But, so I'll go through the ones that you, provided. I'll make that comment in one of them, and we'll see where to go from there.
**Rüdiger Schulze (International Business Machines Corporation)** 09:37 Yeah, and it's an easy change, apparently.
**Matt Hogstrom (Broadcom Corporation)** 09:40 Yeah.
**Rüdiger Schulze (International Business Machines Corporation)** 09:41 Yeah, please make this comment, because then also others can take a point of view on that, if this is…
**Matt Hogstrom (Broadcom Corporation)** 09:47 Sure. Do you want me to just put this… where do you want me to place that comment? In the…
**Rüdiger Schulze (International Business Machines Corporation)** 09:52 I would like for you to, the virtualization is… yeah, maybe I either just put it here, but I also would like to ask you to put that on Now I need to apparently go to the… Well, no, this is wrong. Well, this is wrong.
Let me just… Damn.
Let me go to… The respective pull request where we start to discuss mainframe.
So this is documentation.
I guess… That should be here when we start… look here, 54.
**Matt Hogstrom (Broadcom Corporation)** 10:49 Okay.
**Rüdiger Schulze (International Business Machines Corporation)** 10:50 potentially a good one. When we start to talk about mainframe concepts, then we really…
**Matt Hogstrom (Broadcom Corporation)** 10:55 Sure.
**Rüdiger Schulze (International Business Machines Corporation)** 10:56 Make clear what we want to do here.
**Matt Hogstrom (Broadcom Corporation)** 10:59 Okay, I'll do that in 54 today. Yeah, okay. And I'll start looking at the others.
**Rüdiger Schulze (International Business Machines Corporation)** 11:04 Yeah, okay. Thanks, Matt, and again, if you can get some folks from the VMware organization in your company to take a look at the virtualization, that would be, I think, would be valuable to have a reflection if this works also for their…
**Matt Hogstrom (Broadcom Corporation)** 11:20 Sure. Okay, I'll do that, and You had made a, just to shift gears real quick, back to Opeliano.
Ibm has actually made available, I'm assuming there's ZVDT instances, to open Mainframe projects.
So, I think we have to make a request to the TAC, for a Z instance.
And then they would work with IBM to get that instance allocated for the team.
**Rüdiger Schulze (International Business Machines Corporation)** 11:50 Yeah.
Just let me put that also here, a play on a…
**Matt Hogstrom (Broadcom Corporation)** 12:00 Yeah, because I spoke with Mark Ackert, who works on the ZOE project, and they basically moved away, or are moving away from Marist.
individual instances, so it seems like we should just follow that same pattern.
**Rüdiger Schulze (International Business Machines Corporation)** 12:15 Okay, sounds good, yeah. And, apparently, I was still, you know, at the, you know, everybody to the GitHub repo and everything will happen tomorrow.
Good. Yeah, thanks, Matt. Then,
**Matt Hogstrom (Broadcom Corporation)** 12:29 Alright.
**Rüdiger Schulze (International Business Machines Corporation)** 12:30 I think we are good for today. Thank you. Bye.
**Matt Hogstrom (Broadcom Corporation)** 12:32 All right, thank you, Rudiger.
