SIG: OpenTelemetry on Mainframes Weekly Sync
Date: 2026-09-30
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Jim Porell (Rocket Software, Inc.)** 03:02 Hey, Matt. Sorry again about your pet and your dad.
**Matt Hogstrom** 03:07 Hey, thanks, Jim. It's like I said, he was 96. It was Yeah.
Not a shock, and you know, he's as he told me, he goes, I'm ready any day. Well, you know, he said that you know about a year ago, so.
**Jim Porell (Rocket Software, Inc.)** 03:24 My dad said it for 40 years.
**Matt Hogstrom** 03:29 Well, he said ready, not prepared.
**Jim Porell (Rocket Software, Inc.)** 03:32 Yeah, right, right.
**Matt Hogstrom** 03:33 Yeah.
**Jim Porell (Rocket Software, Inc.)** 03:34 the.
**Matt Hogstrom** 03:36 How are things going with you?
**Jim Porell (Rocket Software, Inc.)** 03:37 Oh, good. I'll put in Zoom, I'll put a camera on at the hospital, and outdoor lunchroom.
So, I got a blurry book there.
So I gotta, I gotta, I gotta be at the doctor in 45 minutes. So, you know, my guess is we'll be done by then anyways, but.
**Matt Hogstrom** 03:56 Yeah, it'll probably be pretty short.
**Jim Porell (Rocket Software, Inc.)** 03:58 Yep.
So… As these meetings typically are.
**Matt Hogstrom** 04:04 Yeah, I, you know, I still owe Rudiger some direct feedback, and I didn't get it to him before the 25th, so I assume if we can push it out a week, that'd be great. I did want to just work on the namespace before we had a whole bunch of other stuff in, and I think there was… Just some inconsistencies. Did you go through it in detail?
**Jim Porell (Rocket Software, Inc.)** 04:23 No, no, I had some other guys do it, but I don't think they gave me any feedback either.
**Matt Hogstrom** 04:28 Yeah, well, it's kind of like, here's Warren Beat, give me a one paragraph summary. It's a little hard to ask people to do that, right?
**Jim Porell (Rocket Software, Inc.)** 04:37 Yeah, right. Well, I, I think part of the conversation we have to have is how do we break that up into multiple PRs so it's a little bit more manageable to reach.
**Matt Hogstrom** 04:44 Yeah, I think that that's it's almost like the omnibus of of commits, right? So much stuff in it.
**Jim Porell (Rocket Software, Inc.)** 04:54 What line item veto power? Yeah.
**Matt Hogstrom** 04:56 Yeah, a lot of US politics could go into that.
**Jim Porell (Rocket Software, Inc.)** 05:01 Exactly.
**Matt Hogstrom** 05:03 So, I heard the, EU just started the digital EU, or, not the EU, the, Euro this week.
**Jim Porell (Rocket Software, Inc.)** 05:12 Oh, no kidding, wow.
**Matt Hogstrom** 05:13 Yeah, I don't know if that's their version of.
**Jim Porell (Rocket Software, Inc.)** 05:15 Like, crypto alternative, almost, or…
**Matt Hogstrom** 05:18 I I can't tell. It it sounded like you know, it's one of those things that nobody likes to have all their stuff looked at.
And so, I expect they're selling it right now as a way for banks to quickly reconcile and settle transactions.
Which sounds good. I mean, who doesn't want that? I think we're doing.
**Jim Porell (Rocket Software, Inc.)** 05:36 Oh, yeah.
**Matt Hogstrom** 05:36 Same with FedRAMP.
**Jim Porell (Rocket Software, Inc.)** 05:37 Yeah, instead of doing Swift or something like that behind the scenes or whatever.
**Matt Hogstrom** 05:41 Yeah.
**Jim Porell (Rocket Software, Inc.)** 05:42 They're doing today, okay.
**Matt Hogstrom** 05:44 Yeah, and they started the same process here. They did, they had what they call it Fed, not FedRAMP.
It was Fed now or something like that.
**Jim Porell (Rocket Software, Inc.)** 05:50 Yeah, FedRAMP is,
**Matt Hogstrom** 05:52 That's a standards thing. Yeah, no, it's, I think there's FedNow or something like that, but it was basically a way to settle US dollar transactions between banks instantaneously.
**Jim Porell (Rocket Software, Inc.)** 06:02 Yes.
**Matt Hogstrom** 06:03 You know, that's.
**Jim Porell (Rocket Software, Inc.)** 06:03 Hey, listen, we got… we got digital checks, that's a huge improvement, so… Yeah. No.
**Matt Hogstrom** 06:10 I think the clearinghouse.
**Jim Porell (Rocket Software, Inc.)** 06:11 Bob is in the car.
**Matt Hogstrom** 06:14 Oh, there he goes. That Rudiger Rudiger.
**Jim Porell (Rocket Software, Inc.)** 06:17 Yeah.
**Matt Hogstrom** 06:17 Yeah.
**Jim Porell (Rocket Software, Inc.)** 06:19 Still allows a connection.
**Rüdiger Schulze (International Business Machines Corporation)** 06:20 Hey there, I'm… Yeah, I'm sitting in a… Carl, am I audible? Can you understand me?
**Jim Porell (Rocket Software, Inc.)** 06:28 Yeah, we can hear you. I'm gonna turn off, I'm gonna turn off,
**Matt Hogstrom** 06:32 I'll do the same.
**Jim Porell (Rocket Software, Inc.)** 06:32 something.
**Rüdiger Schulze (International Business Machines Corporation)** 06:33 Yeah, okay.
**Jim Porell (Rocket Software, Inc.)** 06:34 Yeah.
**Rüdiger Schulze (International Business Machines Corporation)** 06:35 Okay, maybe it's at least enough that we can briefly talk.
**Jim Porell (Rocket Software, Inc.)** 06:40 You came on video, it immediately froze, so I could tell it was a bandwidth issue right away.
**Matt Hogstrom** 06:44 Yeah.
**Rüdiger Schulze (International Business Machines Corporation)** 06:46 Yeah, yeah, it is.
Just one thing that I wanted to briefly discuss, So, there's a proposal out there of how we could do the virtualization and mainframe, and obviously the PR is huge, that's… Right. Surely something which we can split up.
There was a little bit.
You know, around… Do this best, and there's two approaches.
One is, we first define all entities.
And then subsequently at the metrics. The other approach is to… go one by one, right? Define one entity, more or less complete, define the next one. I have two charts here to show you a little bit what virtualization and Mainframe from an entity perspective will look like… I will try to share my screen. If this doesn't work, I will put it to the Google Docs document, and maybe you can look at this from there.
Okay, let's try that.
Can you see my screen?
**Jim Porell (Rocket Software, Inc.)** 08:02 That's working, yep.
**Rüdiger Schulze (International Business Machines Corporation)** 08:08 Okay.
So.
And actually, Matt, from a virtualization point of view, I would also be interested, as your company is also in the virtualization business, maybe this is something that you can run with your colleagues from the VMware side. So this is based on… so… Just to maybe recap, you know, when we started, we kind of, like, put everything into Mainframe, and… for one way.
But… Beltway actions to keep your own domain model small, and try to base as much as possible on base semantic conventions.
or on, you know, more common concepts, which virtualization would be, obviously. So the idea is, there's base semantic conventions. If you can use them, use them. If you can just go with refinement, refine… What's in the base? Refinement could be for what's in the base and go visit or create your own entity or metric.
And… In our case, this would mean, if you look at the… from a mainframe side of this, we actually would have virtualization in place as a common concept, and then build on for… from a mainframe perspective. And in a similar way.
Member Translation.
Don't… What is there, like the host, then try to go with a refinement, or with a new definition of an entity, if this is required.
And… The basic idea is that, if you look at this, that we define, first of all, all entities that are in the virtualization space, and we try to make great use, and this is given here where it says… Fine bye.
Oh.
That we have, you know, use of the base semantic conventions where possible, and then, you know, make your own definitions.
on, you know, concepts that are in the virtualization domain, or in the namespace of virtualization, and similar than for the mainframe side. And where this is leading, just FYI, the depiction here, as part of this diagram, it's not exactly from the naming, like, it's… in the… semantic conventions definitions. Obviously, there's different ways of how this needs to be defined. This is more just conceptual view of what needs to be in the model. I also see there's a typo, that's obviously easy to fix. But the idea is to kind of, like, model, you know.
from the cluster to the resource pool, platform, partition versus virtual machine, also the storage pool.
Obviously.
And then, the hypervisor, and get those entities in place first, and then build the mainframe concept, and obviously mainframe partition, and so on, on top of that.
So far, so good.
**Matt Hogstrom** 11:15 Yeah, I'm… I guess, yeah, I mean, I understand what you're saying. I'm just curious, what… You know, we talked about earlier about Focusing on who the consumer of all the data would be.
And, you know, from an observability standpoint, and this is a lot of, you know, very domain-specific… well, actually, it's not domain-specific, but it is in the virtualization space. Do you think all of this data needs to be pushed out as part of, you know, OTEL signals, or it's just you're looking for the kind of structure So that when you start putting in specific semantic conventions, you use this as a framework to identify them.
**Rüdiger Schulze (International Business Machines Corporation)** 12:03 So, I guess in the first place, it's the framework, so that we have kind of, like, the names for it, that we have the concepts defined, and that we… if we want to do that, actually, that kind of… Define how the respective mainframe concepts would be represented in this?
**Matt Hogstrom** 12:25 really.
**Rüdiger Schulze (International Business Machines Corporation)** 12:25 And, If we, I mean, this is not about the consumer, right? This is more about getting the concepts in place.
**Matt Hogstrom** 12:34 Yeah, okay.
**Rüdiger Schulze (International Business Machines Corporation)** 12:35 From the perspective, if products, vendors would support all or parts of it, I think that would be a separate discussion.
**Matt Hogstrom** 12:45 Did you do any work to test this against Kubernetes framework?
And what I mean by that is if you have, like, a virtualization storage…
**Rüdiger Schulze (International Business Machines Corporation)** 12:57 try…
**Matt Hogstrom** 12:58 That almost could be a PVC.
Right? Could be a volume.
**Rüdiger Schulze (International Business Machines Corporation)** 13:05 Yeah.
I didn't go too far into the Kubernetes space.
We had that part of the consideration.
But I think I started more from, you know, look at VMware, look at KVM.
**Matt Hogstrom** 13:23 CVS.
**Rüdiger Schulze (International Business Machines Corporation)** 13:23 Yeah, I'll pass more from this side, to start with.
**Matt Hogstrom** 13:29 Okay.
**Jim Porell (Rocket Software, Inc.)** 13:30 The other thing too is it's kind of recursive because you've got an LPAR, you've got ZVM.
You've got ZOS… Inside ZVM, you have Docker within ZVM, you know, or Linux.
**Matt Hogstrom** 13:45 Right.
**Jim Porell (Rocket Software, Inc.)** 13:46 And so the host might change, because in some cases, the host might be the platform or something for the lower level, but… But back to your point, Matt, you could say like, if I had this for LPARs, then it would be somebody off the HMC, you know, maybe monitoring this in a consistent way.
**Matt Hogstrom** 14:06 away.
**Jim Porell (Rocket Software, Inc.)** 14:06 And then somebody at ZVM level.
Monitoring all their guests.
I don't know, but I think there's a… should be very synergistic.
But the host, like… The host for LPAR would be the Z17.
the host for ZBM would be an LPAR.
Inside, you know, Prism.
That makes sense, I don't know.
**Matt Hogstrom** 14:40 Yeah, so almost what you're.
**Rüdiger Schulze (International Business Machines Corporation)** 14:41 Yeah, but that's…
**Matt Hogstrom** 14:42 companies.
**Rüdiger Schulze (International Business Machines Corporation)** 14:43 We logic.
**Jim Porell (Rocket Software, Inc.)** 14:44 Yeah.
**Matt Hogstrom** 14:45 Yeah, and that would fit here, too, because you host a virtualization platform would be Prism.
**Jim Porell (Rocket Software, Inc.)** 14:50 Right.
**Matt Hogstrom** 14:51 Right? And then your hypervisor would be ZVM.
although well, then you got the partition, yeah, okay.
I have to think about it a little bit.
Is this, is this,
**Jim Porell (Rocket Software, Inc.)** 15:03 Well see, that's where I get, I get confused between the partition and the hypervisor and the platform. It's.
**Matt Hogstrom** 15:08 Right.
**Jim Porell (Rocket Software, Inc.)** 15:09 you know, The rest of it kind of makes sense, but… It's almost too many things, maybe.
**Matt Hogstrom** 15:21 Yeah, well, it's like the virtualization switch, right?
That could be in.
The like I would say like Sysplex, right? There's a certain level of you know, virtual networking and DVIPA and whatnot.
So, that concept fit can fit in a number of different places, so it's not the only place it would fit.
**Jim Porell (Rocket Software, Inc.)** 15:45 Is it a sub-component of the virtualization platform, or is it its own entity?
**Matt Hogstrom** 15:50 Yeah.
**Jim Porell (Rocket Software, Inc.)** 15:50 That's kind of where I was coming from.
**Matt Hogstrom** 15:52 Yeah.
Is this linked off of the, the pull request?
**Rüdiger Schulze (International Business Machines Corporation)** 15:58 2 is… I think this one not, because this one I just generated this week, but I can put this somewhere to add it. I also have a document with a mapping. I will add this… I will put this to our meeting notes, and then also post it to the Slack channel.
And and let me see I.
Let me find a place to place this and I will add it there.
But the idea was, and I was running through this, I tried to have the mappings for these different concepts for the different hypervisors, so… that… Kind of like, it's rational, Why these things exist.
And yeah, I I will put it out there would be good to to get feedback on that.
**Jim Porell (Rocket Software, Inc.)** 16:58 and.
**Rüdiger Schulze (International Business Machines Corporation)** 16:58 Right and.
**Jim Porell (Rocket Software, Inc.)** 16:59 I'm thinking fast.
**Rüdiger Schulze (International Business Machines Corporation)** 17:00 Attention to this is… it's getting more… Yeah, go ahead.
**Jim Porell (Rocket Software, Inc.)** 17:06 No, no, no, you go ahead, Roger. Sorry.
**Rüdiger Schulze (International Business Machines Corporation)** 17:10 Yeah. So the extension of this, I hope this is still readable, is I think there's the virtualization part kind of like continues to be in the picture, obviously.
**Matt Hogstrom** 17:19 you.
**Rüdiger Schulze (International Business Machines Corporation)** 17:21 Of adding the mainframe entities, which could not be created through… Because they don't have a representation, essentially, so that's why they got in here. And you also have these refinements, like the mainframe host. This needs to be understood in a way, this is essentially just adding additional attributes.
to the host entity. There were reasons why to include it in an additional… as an additional definition, but it's a refinement.
**Matt Hogstrom** 17:58 is.
**Rüdiger Schulze (International Business Machines Corporation)** 17:59 So it's important to read the, you know, the relationship here on these, right?
**Matt Hogstrom** 18:05 Yeah.
You know, maybe, This, maybe this is nitpicking, but you kind of reversed it, right? You had host on the left.
And I guess maybe you're just looking at the mapping differently here, but, is node a better term than host?
Oh, is it?
**Jim Porell (Rocket Software, Inc.)** 18:24 Hotel word.
**Matt Hogstrom** 18:26 Is it the OTEL word? Okay.
**Rüdiger Schulze (International Business Machines Corporation)** 18:27 Yeah, that's the point. They used host in their definitions today. Okay. Yeah.
**Jim Porell (Rocket Software, Inc.)** 18:41 I'm going back to the Google Drive, Rudiger. You and I had done some things probably almost 3 years ago.
Where we had, done some drawings.
of, how the cell could fit.
But I'm trying to look for it.
Because we did some specific, drawings for OpenTelemetry, for VM.
**Rüdiger Schulze (International Business Machines Corporation)** 19:07 Right.
**Jim Porell (Rocket Software, Inc.)** 19:09 Yeah.
Because I do kind of think… That, the diagram.
I don't really think the switch And the partition.
Really fit in there, because the partition to me is the host.
And, you know, if you're looking at those recursive ways, I'm just thinking out loud here, but…
**Rüdiger Schulze (International Business Machines Corporation)** 19:38 Yeah, I've… Think.
I think if the partition is just a refinement, as it's… at least I think that's how it's described here.
Then I guess it's really just about… it remains a host, but it's about getting the additional attributes on it.
**Jim Porell (Rocket Software, Inc.)** 19:57 Right, well, I think you have no parameters.
**Rüdiger Schulze (International Business Machines Corporation)** 19:59 not.
**Jim Porell (Rocket Software, Inc.)** 19:59 You have ZVM attributes.
Yeah.
**Rüdiger Schulze (International Business Machines Corporation)** 20:04 And… And the way how that would come out also as data is actually you get a host entity, so what is reported to the backend is a host entity, but with these refinements, you get the… within the context of the semantic conventions, this there's, essentially, you are allowed then to add additional attributes which are not on the base host being defined. Right. It remains a host, but the refinement gives you The… kind of like the contract that you can add these… these attributes.
But it's all good questions, so I think the point is that, I mean, this is really just the high-level.
Visualization, but, I guess what I take from this is.
Can we have, you know, additional materials which kind of, like, support the way of how it's modeled, better visualized?
And go over these type of materials, then… to… Kind of, like, agree, okay, it's a host, but it's a host with additional attributes, for instance.
**Matt Hogstrom** 21:16 Yeah.
**Rüdiger Schulze (International Business Machines Corporation)** 21:16 Taking this example.
And the virtualization piece, which, I mean, this has… I think this came in from VMware and it came in from DPM, in fact.
**Jim Porell (Rocket Software, Inc.)** 21:31 Oh, okay. Alright.
I want to go review what they said then to see how it maps to what we have.
**Matt Hogstrom** 21:43 Do you happen to know who in VMware is the rep?
I mean, I can find it if you know it off the top of your head, that would be helpful.
**Rüdiger Schulze (International Business Machines Corporation)** 21:50 No, actually not. I know there is… it's part of the VMware receiver, and I tried to build a little bit on the SD… the OpenTelemetry collector receiver.
Which has a… let's say it has a data model, it's not, you know, name-wise, not directly mapping to this year, but conceptually, I try to consider that.
But I don't know who the contact would be. Bye.
**Matt Hogstrom** 22:22 Okay, I'll find out.
**Rüdiger Schulze (International Business Machines Corporation)** 22:24 Yeah.
**Matt Hogstrom** 22:25 They can't be that far away.
**Rüdiger Schulze (International Business Machines Corporation)** 22:27 Right.
Okay, but what I take from this, let's put more… let's kind of, like, stay on this model perspective for a moment. Let's add more content to that.
Review that.
And, kind of like… Get the agreement on this, and then we can go into the definitions.
Okay. And that, I guess, you know, the point was, I mean, obviously you can read this, but I mean, AI is really your friend on this.
**Matt Hogstrom** 23:05 No.
**Rüdiger Schulze (International Business Machines Corporation)** 23:06 get it right of how to do semantic conventions with the AI, that helps, and then you can actually nicely start to model things out.
That's why, actually, it became everything in one PR, because it's kind of, like, comprehensive, and it's now easier once we decided what the model is, and the complete model, to split it out into specific pieces to… to review it. So.
It will be obviously, you know, why we even then want to review each of these pieces separately. It will be… probably not a big thing to split it into different PRs, so it's more important that we agree on kind of, like, these model views overall, and then we can… Can work on the entities, or, you know, one by one, or… You know, the approach we can decide.
**Matt Hogstrom** 23:58 So, would it be helpful to put this into, like, a mermaid format?
**Rüdiger Schulze (International Business Machines Corporation)** 24:03 It's actually a mermaid. I just put it on a slide because… Okay.
**Matt Hogstrom** 24:09 I was gonna say, then, that could be edited easier, so if you've.
**Rüdiger Schulze (International Business Machines Corporation)** 24:12 Yeah, yeah, yeah.
**Matt Hogstrom** 24:13 Is that in the PR?
**Rüdiger Schulze (International Business Machines Corporation)** 24:15 Not yet, I will put it there. That's the thing that I just created this week. I will put it there, I will post it on the… on the Slack, and I will let you know once I have these things out there.
**Matt Hogstrom** 24:27 Okay.
Alright, perfect.
**Jim Porell (Rocket Software, Inc.)** 24:31 I just learned something, so thank you, because I didn't know what MerMed was.
**Rüdiger Schulze (International Business Machines Corporation)** 24:35 Mermaid is great, actually. Yeah.
**Matt Hogstrom** 24:38 We use it all the time.
**Rüdiger Schulze (International Business Machines Corporation)** 24:40 Yeah.
**Jim Porell (Rocket Software, Inc.)** 24:40 Yeah, no, it's cool.
Right.
**Rüdiger Schulze (International Business Machines Corporation)** 24:45 Good. Anything else for today? Let's just update the meeting notes and… Say that we, that we spoke initially on the… On the data model for virtualization.
**Matt Hogstrom** 25:05 Okay, that sounds good.
**Rüdiger Schulze (International Business Machines Corporation)** 25:10 Oh.
Just doing this quickly.
Okay.
Okay, so… Actually, we reviewed… 3.
was actually the entity model.
And the conclusion was, Oh… And, an additional… Mappings to hypervisor or to virtualization managers.
And… This is… And then… Next step.
Love you, and a new… Love you.
Entertain with her.
Okay.
Good.
Yeah, let me get these materials tomorrow to you, and then, We can… we can have another discussion next week.
**Jim Porell (Rocket Software, Inc.)** 27:19 Alright.
**Matt Hogstrom** 27:20 Okay, that sounds good.
**Jim Porell (Rocket Software, Inc.)** 27:21 Sounds like a plan, yeah.
**Rüdiger Schulze (International Business Machines Corporation)** 27:22 Thanks a lot.
**Matt Hogstrom** 27:24 All right, thanks Rudiger.
**Jim Porell (Rocket Software, Inc.)** 27:25 Have a good day.
**Rüdiger Schulze (International Business Machines Corporation)** 27:25 Thank you.
**Matt Hogstrom** 27:27 Bye.
**Rüdiger Schulze (International Business Machines Corporation)** 27:27 Thank you.
