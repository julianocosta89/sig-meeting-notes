SIG: OpenTelemetry on Mainframes Weekly Meeting
Date: 2026-07-29
Duration: 34 minutes
============================================================

## Zoom Recording Transcript

**Ruediger Schulze (IBM)** 03:05 Hi, Matt. Hi, Greg.
**Matt Hogstrom** 03:07 Hello, Ruediger.
**Greg Shriver** 03:08 How are you?
**Ruediger Schulze (IBM)** 03:09 Good.
**Matt Hogstrom** 03:13 Bostante bien.
**Ruediger Schulze (IBM)** 03:17 Okay, let's maybe give it another minute, and then we can start. There's something to discuss today.
From a semantic convention point of view.
**Greg Shriver** 03:27 Let's see that.
**Ruediger Schulze (IBM)** 03:29 Right.
**Greg Shriver** 03:32 Were you, expecting… Ruediger, were you expecting to, talk about the PR20?
**Ruediger Schulze (IBM)** 03:41 Yes, right.
**Greg Shriver** 03:42 Okay.
Very good.
**Ruediger Schulze (IBM)** 04:21 So, looks like it's just us today. Let me share my screen, and, there's a couple of things which probably we want to do for… And I'll just… Getting started, Mrs. So… If you look at the PR20, and I see I still need to do a little bit of cleanup here, Whereas his name?
One more long.
A second… So… Where is it? There it is, right time.
So, obviously, I missed to update here the description section. This is still to be done. I had quite some falls and back on that one.
But, just from a hygienic point of view, the community is moving to what they call Definition Language Version 2. So, the PR is now written in the version 2 language.
Also, there is something that is being, you know, described as the reusable templates for the formatting. This is also being adopted. And then, obviously, we get into the interesting, you know, aspects of what is being covered. And the focus is currently on HMC.
And, metric groups, and a couple of other, data points, which are available from the HMC. Essentially, what you get with a Prometoise, exporter, which is there for the HMC. And, when we look at this, and this is definitely, you know, first of all, I mean, we generally want to review now in the community, this proposal here. First of all, from a SICK point of view, but also I think we want to get input from the… from the semantic convention SICK, more with a focus from a distributed side. And, if we look at the PR, and how this comes out, and that's why I want to go back, actually, to the repository. There's lots of files on this. It's probably better readable if you go to the output.
So let me just go back here.
Yeah, right. And under documentation, there is the output generated. The… And this is something that I really want to discuss, not just here, I guess, you know, with the group, as part of the CAIC, I think we also need to take this to the distributed, side.
Lots of these entities, metrics, actually all of them, as of now, they come out with a namespace.
Mainframe in front. But on the other hand, there are definitions also being made by the semantic conventions, which start with hardware, as an example.
But the reason why I choose to go ahead with Mainframe for now is that, It's not always a perfect fit, right? Or then there is something missing in the base semantic conventions. So, then the question is actually.
How far do we want to go with extending what is there in the base semantic conventions? And how much do we want to refine that and then reuse namespaces, like hardware. Same example is, for instance, system CPU utilization.
When you look at the fine print of system CPU utilization, then it talks about a virtual… the utilization of a virtual CPU, but obviously, from a hardware perspective, we get also the physical CPU utilization on the HMC. And that's essentially… where I think we need to find a consens you know, among the different vendors here on the SIC, but also, I think, across the ecosystem.
And… what is here on this… on these definitions now is, as I said, right, HMC, I think it comes down to, it's currently, like, 77 metrics with respective attributes.
It's quite a lot, but what I really would like to ask you is then, you know, to take the time to commend on this PR and, Obviously, you know, as a vendor in this space, you maybe also have a point of view. Share that, please. And then, I guess we get the same from, you know, the others in the ecosystem, and then we need to somehow come to a joint view.
**Matt Hogstrom** 09:40 Okay, have you evaluated the distributed side already?
**Ruediger Schulze (IBM)** 09:46 For that distributor.
**Matt Hogstrom** 09:47 good at hardware.
**Ruediger Schulze (IBM)** 09:48 Not in… let's say not with the semantic conventions, you know, that was more focused on the distributed side. I joined their meeting, usually, but Recently, it was more about learning of where are they with the tooling and mechanics, as I mentioned, right? They are also in the process of upgrading. And, But it will be good to get this feedback, right? Should… or maybe this general agreement. Use hardware as a namespace, use system as a namespace, even if maybe the current definition of system… It's not a perfect fit for these hardware aspects, right?
**Matt Hogstrom** 10:32 Damn.
**Greg Shriver** 10:34 So, I like… I like the… I mean… I like the fact that it is all namespaced, and I, you know, I don't have any… I don't necessarily have any issues with the mainframe as being a high-level namespace. I think it's probably good and separates it, you know. I mean, I think we've… we've gone back and forth on this group, where should we, you know, combine our stuff with… with stuff that's not in a separate namespace like Mainframe? And I think, you know, after really thinking about it, I think, That it makes more sense to be appropriately namespaced.
So the fact that it's segregated off into a mainframe container, or mainframe namespace, isn't necessarily… I don't view it as necessarily a bad thing.
I guess… so, I didn't get a chance to go through your entire PR. I did notice that… that you moved it into a ready-for-review status.
One of the things I like about what you've done is, in the description, it looks like in many of the descriptions, you've really… you've really tried to describe the main… describe what it is, and then also provide the non-mainframe equivalent of it, you know? So, to make it understandable for someone that's maybe walking up to the mainframe.
you know, new, like I would expect, you know, many SREs would be.
So…
**Ruediger Schulze (IBM)** 12:09 That was one point, but in all fairness, I also want to mention, I mean, in today's world, AI is our friend helping to get to this Yeah.
**Greg Shriver** 12:20 I wanted to ask that, too, because I noticed that you… I noticed in the PR that you… you requested a review from Copilot, and I read the stuff that came back from Copilot, and it was kind of interesting how… I mean, it was mostly about the bank file and the tooling.
Like, it looks like it was, assuming Podman as opposed to Docker or something like that.
**Ruediger Schulze (IBM)** 12:43 Yeah, This is… yeah, just maybe let me briefly cover that. It's also something that I just recently learned.
Let me just go back to the piano here.
Right, so, I mean, this is something that the community, obviously, has been enabling. If you go to these PRs, you can request this. You can also repeat this. It's, you know, it's just like any review, you can add this.
And obviously, the semantic convention CIC is also using this, I was thinking, going ahead with this.
The… What was the other thought that I had?
I dropped my mind.
But yeah, it's Mainframe?
**Matt Hogstrom** 13:30 already approved?
summit.
**Ruediger Schulze (IBM)** 13:34 as a namespace, yes, I think we used that before, because we had the mainframe helpline name introduced earlier, but also just to… to say of how that works, so… what we had earlier in the base, this will be deprecated. Also, the COS one, the few that we had will be deprecated. This will move all in our domain-specific or, federated repository. And, so what the community is still looking at of how they will be referencing these, these federated, repositories or definitions.
But the… the aim is here, and we actually talked about that on the semantic conventions, like, they… now that they introduced these, federated repositories, like, for instance, for GenAI, they still need to go through the release process.
And ideally, you know, if we could manage to not take too long reviewing this PR, even, you know, we want to do this right and solid, if we could kind of, like, go along with them, then we can actually benefit from also learning on how to release as a sick, Kind of, like, have a version zero.
0.01.
Coming out, right?
**Greg Shriver** 14:55 Sure.
Actually, I thought about that a little bit. Oh, sorry. Go ahead, Matt.
**Matt Hogstrom** 14:59 No, no, go ahead, Greg.
**Greg Shriver** 15:01 I was just gonna throw this out there, I mean, I know that you just put this in ready for review mode.
I'm thinking that… it would be good is if we could at least have a couple weeks, because one of the things that I'd like to do is, you know, communicate this internally in our chats, and say, hey, we have this PR, I'd like for other people to take a look at it.
And to get some additional scrutiny, you know, from… at least, you know, from within Broadcom.
And before, before we just go ahead and approve it, and I know we probably don't need everyone to approve, we only need one, so… But I… I guess I would ask that we have… I know… I know that it makes… that… that there's a push that would like to get this out as soon as possible, and I get the… the… the urge.
**Ruediger Schulze (IBM)** 15:55 Interesting.
**Greg Shriver** 15:55 for that. But I'd like at least, you know, I think at least a couple weeks.
You know, just to… just to let everyone have a decent look at it before it just, you know, hits the street.
So… because basically, once we approve this PR, it's… I mean, it's… It's set in stone, right?
**Ruediger Schulze (IBM)** 16:15 No, yeah, it's… yeah. So, two things on this. So, I'm planning to do the same, actually, to also get the different SMEs on this, and at least get some feedback on that. And in terms of setting stone, this goes by, if you look at the definitions, there is, there's a maturity level, stability, it's the tech. So, everything is being defined in development, and we probably would take a, I assume, probably at least another year until we would move anything into stable. That makes sense.
So, it's not like that we, you know, once we put it out there, we can't change it. Obviously, we are then asked to follow the process of deprecating names or, you know, clearly showing what the change is. That's also something we need them to learn.
And I think I agree on, you know, I think we need to have a couple of weeks. It would be good if we somehow, maybe by end of September, could have at least a consolidated view of what the result of, you know, the revenue is, so that we can get it in.
**Greg Shriver** 17:30 Yeah.
**Matt Hogstrom** 17:31 curiosity, did you, just for… Mainframe is, like, recognizable, but it's also kind of legacy antiquated. Did you consider just S390X?
**Ruediger Schulze (IBM)** 17:43 So it's more of an argument.
**Matt Hogstrom** 17:43 texture statement.
**Ruediger Schulze (IBM)** 17:45 Yeah, that's a good one.
we… we had some discussions around that, but none of them were somehow leading to a conclusion. I think it's… it's mainframe currently, where, because I think this CIC started, and it's kind of like an… a name that is being recognized by some, but it's actually… so… On a side note, I will also run this with our folks who look on terminology.
And I had this question, actually, should this be mainframe, or should this be something else already once out, but I didn't get any… any special feedback on it.
**Matt Hogstrom** 18:31 The only reason I think of it is, if you're doing anything with Linux or Red Hat OCP, you're gonna see your container say, I'm on S398.
Right? And so there's almost a correlation to… That terminology, but… Do you see the namespace I'm just trying to understand what you're thinking about as extensions, right? So you got… The S390 is the hardware, like, you're talking about really kind of the CAK here.
Yeah. And then you have ZOS is probably the primary operating system that you would be using, right? So would it be S390x.zos, or would ZOS be a parallel structure to S390X, or Madeframe, whatever?
**Ruediger Schulze (IBM)** 19:19 So, as of now, we have CUS as a high-level qualifier.
**Matt Hogstrom** 19:25 Okay.
**Ruediger Schulze (IBM)** 19:26 And, we had this long debate about using TPS as a… For transaction processing system, obviously.
**Matt Hogstrom** 19:36 Hmm.
**Ruediger Schulze (IBM)** 19:37 So, and this is something which we can revisit. This is probably one of the next activities, then, to look at these spans.
But, where I'm going, I just wanted to go backtest this once… It's essentially… can see that already here. I need to go back to documentation.
So if we… yeah, right now it's just Mainframe and COS, right? And it's… it's, I guess, up to this secure to decide of what namespace we would be claiming.
And if he… if he would be… intending to lead with the architecture as a… I think there's no much other examples in the semantic conventions, which kind of, like.
clarify that, if… if we… if we would lead this platform, maybe cloud is an example where… where they start. I would have to check that. Probably cloud is a namespace on its own.
**Matt Hogstrom** 20:40 That's probably more cloud architecture, right?
**Ruediger Schulze (IBM)** 20:42 Yeah.
So… I mean, you know, we can put that for discussion if this is one consideration to go with.
**Matt Hogstrom** 20:53 Hmm.
**Ruediger Schulze (IBM)** 20:54 with the architecture.
What we should be doing is, I think we should be leaving space in all these considerations then.
And it might actually be straightforward, the way our community has been defining this, but probably every vendor also has its vendor-specific extensions to some.
**Matt Hogstrom** 21:20 Yeah.
**Ruediger Schulze (IBM)** 21:20 Right? And they should at some point also appear here, but I think the current convention is actually you have the vendor name and then the extension underneath, but we somehow should model it that this this relation between vendor extension and concept is then, obvious, right? This is something we.
**Matt Hogstrom** 21:40 Right.
**Ruediger Schulze (IBM)** 21:40 to look at some point.
**Greg Shriver** 21:44 I'm sorry, I missed that, Ruediger. What's the connection between… Namespaces and vendors, and…
**Ruediger Schulze (IBM)** 21:52 Yeah, so if you look, for instance, at the definitions, which are also there for cloud, you have AWS, you have GCP, and, you know, but I assume we get into the same at some point, right?
And, we… what we want to make sure is that, you know, whatever we put out there, somehow there's this flexibility and also… You know, that somehow this is an easy-to-follow.
**Greg Shriver** 22:23 Sure.
**Matt Hogstrom** 22:25 Yes, and she could even look at the Z as a platform, right, that's distinct from the AWS or Azure, right? They've got a bunch of APIs against it, but…
**Ruediger Schulze (IBM)** 22:38 Yeah.
**Matt Hogstrom** 22:39 I… I'm just… I'm spitballing. I need to look at it and think about it a little bit.
**Ruediger Schulze (IBM)** 22:45 Right, okay. Yeah, I think that's all what we have for today. If you could, you know, I think I will do a couple of cosmetic updates, which I just realized they were missing. But, then let's go into a review cycle, get feedback from, you know, different sides of ecosystem, and let's form that. And Matt, I said that earlier, right, in the end, you know, the idea was to start with the HMC as the lowest layer, as we… assuming that somehow this would define our base of how we would name things.
And that then should help us to grow to the higher levels on, you know, how to name this also on, you know, when we get into the COS space, and…
**Matt Hogstrom** 23:32 This is what I was trying to think through, it's kind of the… I think if you look at Z architecturally, that all makes perfect sense, and if you're a Mainframe guy, that's how you'd think it. I was just trying to think of it as a consumer.
Like, I'm looking at this data, I'm probably primarily interested in ZOS data, because there's lots of instances of ZOS, and I probably don't… worry as much about the aggregated data about the CAIC.
But I was just trying to look at it from both sides, right? The consumer versus the raw technical architecture.
**Ruediger Schulze (IBM)** 24:07 I just had also a discussion with maybe somebody who is, while being mainframe, also very much open for the other platforms.
He was actually of the point of view we should try to actually extend hardware as a concept in the base semantic conventions, or at least being additive in our… in our, domain, just using the namespaces like hardware and so on. I think this is something what I would like to understand from maybe, you know.
The… The other vendors in this space of how they would treat that.
Yeah, I think this is one of the main questions, right? What's the names?
**Matt Hogstrom** 24:53 Yeah.
**Ruediger Schulze (IBM)** 24:53 That we want to use, right?
Yeah.
**Matt Hogstrom** 24:57 I agree.
**Greg Shriver** 25:00 Yeah, and another sort of related question, Ruedigo, but… So, this… you mentioned the Prometheus Exporter.
So, the Prometheus exporter currently uses the HMC APIs to take, you know, scrape data? Is, is that, is that accurate?
**Ruediger Schulze (IBM)** 25:24 That's accurate. And if you look at the doc, it's… Largely maps to what you have on the semantic… sorry, on the, HMC metric groups.
But it's also, you know, there's the CPC object, there's also DPM mode, certain, you know, more configurational data.
L power weights, right? They… they live on different objects, but they are of interest, obviously. And, yeah.
**Greg Shriver** 25:58 And do you have any thoughts, or, on the, you know, the primary users of the Prometheus exporter, like, for example, our… you know, is Splunk using that to go either through an OpenTelemetry collector or directly into Splunk?
Are they… are, you know, elastic… Datadog, any of the other kind of, observability platforms.
**Ruediger Schulze (IBM)** 26:28 I think it's actually… so, I can't tell… I can't tell you about the other observability vendors, obviously, but the heritage of where this actually generates from… it generates from these, cloud environments that make use of IBMC, different types of offerings.
Okay. And… So, it's more in this space of… managing your infrastructure and having a direct monitoring feed from the HMC. Obviously, you can get the data through REST API, but it's just a, you know, a way to… To… to… to use it, right?
**Greg Shriver** 27:10 Okay.
**Ruediger Schulze (IBM)** 27:12 And I referred to the… to the… to the Ax portal. It's a specific implementation, obviously, it gives permit or its format. The naming is not… Yeah, open Telemetry aligned.
So, using… it's more like a reference point to… to… You know, look at, you know, what data is actually, for a starting point, reasonable to look at, and then, you know, to develop the… the framework, and then, like I said, grow up the stack.
**Greg Shriver** 27:49 Okay.
Thank you.
So, like I said, you know, we can take… We can take this and sort of, Socialize this through you know, on the Broadcom side, and I assume… You know, we'll probably be also pumping this up on the, you know, on the OpenTelemetry Mainframe SIG group to asking people for comment, and… Things like that as well, right?
**Ruediger Schulze (IBM)** 28:27 Yeah, so, let me finish the, kind of like, the hygienic things that are there, but I would definitely ask some of the key persons on the semantic convention seg to take a look at that. I think they, Would surely have input on this, in terms of what their expectations of in naming certain concepts is.
**Greg Shriver** 28:56 And I… I suspect that… That when we do have feedback, it probably makes most sense to do it directly in the PR so that everyone can see it, right?
**Ruediger Schulze (IBM)** 29:08 I mean…
**Matt Hogstrom** 29:08 Cool.
**Ruediger Schulze (IBM)** 29:09 As I had this discussion as well, just to share this here for this group, I think if you… kind of like, from your organization, gather a collective… input, right, and you bring it to the PR, I think that's fine.
If somebody doesn't want or can't you know, for whatever reason, comment directly on the PR, I think that's okay.
**Greg Shriver** 29:32 Yep.
**Ruediger Schulze (IBM)** 29:32 What we want is to have a broad set of feedback, obviously, to…
**Matt Hogstrom** 29:38 Sure.
**Greg Shriver** 29:41 Yeah, agreed.
Alright, well, this is exciting.
I mean…
**Ruediger Schulze (IBM)** 29:48 Yeah, I think now we are there. This is, I think this decision from the community to go for federated, I think this is really helpful.
and also the community side of this took a couple of other, you know, steps to help also ring this, and so, yeah, this is good. And now we, you know, it's on us to… Take this to the next level.
**Greg Shriver** 30:16 Right.
Right.
**Ruediger Schulze (IBM)** 30:21 Okay, good. I think, as much as I have seen, Craig, I think you took a couple of notes here, so, yeah, I think this.
**Greg Shriver** 30:28 Yeah, not many. Not many.
**Ruediger Schulze (IBM)** 30:30 Yeah,
**Greg Shriver** 30:31 But yeah, I'll add some notes.
**Ruediger Schulze (IBM)** 30:34 It just is actually not a consumer yet, it's more like, as input for data modeling.
**Greg Shriver** 30:43 That's cool.
**Ruediger Schulze (IBM)** 30:44 Cough.
Right.
Okay, good. That's good.
**Greg Shriver** 30:48 One of the things we probably should do in here is at least, you know, maybe jot down the, sort of, the milestone dates. I mean, you mentioned, what, like, the end of September?
**Ruediger Schulze (IBM)** 31:00 Sure.
**Greg Shriver** 31:00 I mean, the target date to get this thing… to get this thing approved… Okay.
Well, we're aiming to get feedback hopefully long before end of September.
Hoping to, like, close it by…
**Ruediger Schulze (IBM)** 31:24 Yeah.
**Greg Shriver** 31:24 September, right?
**Ruediger Schulze (IBM)** 31:25 let's say. I mean, I'm calculating in that there's vacation period, but get feedback, let's say.
by… by early September, targeting flow… targeting approval by end of… By end of September, maybe that's…
**Greg Shriver** 31:42 I like that.
Does that feel achievable?
**Ruediger Schulze (IBM)** 31:47 I hope so, right?
**Greg Shriver** 31:50 I mean, so we're August, September, that's, what, 2 months.
**Ruediger Schulze (IBM)** 31:54 Yeah.
the term, 7 comma.
Sick.
**Matt Hogstrom** 32:11 Does BMC attend these on a regular basis?
**Ruediger Schulze (IBM)** 32:14 Yeah, yeah, so it's the four big ones, if you will, just want to express it this way. Okay, yeah. And then, you know, a couple of the observability vendors join as well.
And we had a couple of in and outs of people over the time as well, but I think it's… my OTSD, you know, probably well-known people, Matt. I mean, Jim Porrell is joining, which I assume you know very well from history.
Yeah. And, Richard, Nicola, you may actually also know, so…
**Greg Shriver** 32:52 soon.
**Ruediger Schulze (IBM)** 32:53 Yeah.
**Matt Hogstrom** 32:55 Well, I'll see how the pool isn't all that big.
**Ruediger Schulze (IBM)** 32:58 Yeah, right.
**Greg Shriver** 33:00 And Antoine, am I… it's Antoine from Splunk, right?
**Ruediger Schulze (IBM)** 33:03 Yeah, it's Antoine from Splunk, and he seemed to have taken over from Morgan, who was with us earlier, and
**Greg Shriver** 33:11 Oh, I wasn't aware of that, okay.
**Ruediger Schulze (IBM)** 33:13 Yeah, it's my interpretation. It's… I mean, Antoine was actually more recently on these calls. I think Morgan is still following. I think also Antoine is trying to, you know.
I mean, the other thing which we, you know, you may be aware of is we tried to get an agreement that there is community, or there are GitHub action runners for Linux on S390.
This is nothing technical at this stage, it's really about agreements on Ts and C's, and… We tried to do this on the… on, just OpenTelemetry project with IBM and the open source office to realize, but that somehow didn't work out. Now it's with the CNCF to agree the T's and C's.
And… That would definitely be helpful to do certain porting activities and… and… you know, also validate, at least from a Linux perspective, certain things, right?
But, yeah.
Okay.
**Greg Shriver** 34:30 Alright.
**Ruediger Schulze (IBM)** 34:31 Yeah, then, let's go for… let's go forever.
**Matt Hogstrom** 34:38 Very good.
**Greg Shriver** 34:39 Thanks.
**Ruediger Schulze (IBM)** 34:40 Thanks. Bye. Thanks, Ruediger.
**Greg Shriver** 34:41 See you next week.
**Ruediger Schulze (IBM)** 34:42 That's fine.
**Greg Shriver** 34:43 Thanks, Matt. Bye.
