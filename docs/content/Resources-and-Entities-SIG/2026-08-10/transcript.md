SIG: Resources and Entities SIG
Date: 2026-08-10
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**krajo Krajcsovits** 00:31 Hi, Don.
**Josh Suereth (Google LLC)** 00:35 Hey, how's it going?
**krajo Krajcsovits** 00:37 I'm good, how are you?
**Josh Suereth (Google LLC)** 00:39 Not bad, not bad, just getting… Booted up here.
**Matthieu Noirbusson (Sensor Factory)** 00:54 Hello, Josh.
**Josh Suereth (Google LLC)** 00:55 Wait.
**Matthieu Noirbusson (Sensor Factory)** 00:56 Hello, Greg.
**krajo Krajcsovits** 00:58 I hate it.
**Josh Suereth (Google LLC)** 01:38 So, I don't see any agenda yet. Oh, I don't have my camera on.
I think We have, two things from last time.
We should take a look at some of these.
But I think we're just sort of in a… A bit of a stasis as we talk to the specification, folks, about one of the PRs. Let's see… Yeah.
trying to figure out what the best use of our time here is. We have the two open spec PRs that we're trying to push forward to get things through in the spec. We have a bunch of open issues to go through. I'm thinking about… the… we talked about the one in the spec meeting last week. That's the one about, what to do about schema URL, and whether or not we consider schema URL changes breaking, It's this one here.
I think… We still don't have folks from the SIG approving this, but we do have approval from some of the TC Yeah, I don't think any of that discussion actually got recorded outside of Daniel's comment here.
Which is just, we talked about this in the spec meeting, and basically.
protocol will be backwards compatible, and we're planning to kind of let Steam ERL change what it means for resource, because we don't think people should depend on it, because it actively causes breakages today, and that the schema URL you really want is the one that's on entity.
We talked for a long time about it at the SPEC meeting, and it wasn't clear what the path forward is. So I think there's going to be a discussion about it tomorrow.
Is my… my guess as to, like, how we make progress here.
Because I don't see anyone else having approved this.
The big… the big question in my mind for, like, next is, right now we have this notion of a… Experimental Entities Enabled flag.
And if you read, some of the discussion from, like, Jack on the Java implementation, it's basically, what does this do?
So, where's the one from? It's coming from Daniel on this, I think.
I'll just pull it up.
We have to update our current prototype for this, but effectively what this says is when this is enabled, we enable entity support in the SDK, And the way that they wanted this to work in Java was that resource detectors always report entities, but if you don't enable this flag, then the, SDK doesn't emit it no TLP.
But what Daniel and I have been pushing for is we don't think admitting it notes OP is actually going to be breaking for anyone.
So we kind of want to actually expand resource detection to understand entities as a non-breaking change we can make to SDKs, where, we kind of move forward with it.
So there would not be, like, an experiment flag to enable it or disable it.
Or at least the experiment flag is default true.
Kind of curious if anyone here has thoughts on that. That was, like, the other discussion in here that I think needs a little bit of progress, or at least I need to write up, you know, what we plan to do going forward here.
This would be how the hotel community engages with entities. Do they just start showing up?
And you had to do nothing. That's kind of, like, the goal.
The risk is, if we make any kind of mistakes, then we have a bug.
**krajo Krajcsovits** 06:14 I'm the noob here, but just a question. So… If it's not a feature flag.
I… I vaguely remember the APIs shown in the… in the prototype.
changing… I mean, basically the prototype changing the APIs. Or was that… was the API backward compatible? Like… I remember adding new… Yep.
**Josh Suereth (Google LLC)** 06:40 So, what do you mean by which API?
**krajo Krajcsovits** 06:43 The programming API, so in the code. Or is that out of scope? Like, what do we mean by non-breaking? On what level?
**Josh Suereth (Google LLC)** 06:50 The 100%, coat.
So this would be the… I mean… When we talk about breaking changes, it's if I take a version of the client libraries, for example, and I move to the new version, does my system still work, or is it broken?
if it's broken, we consider that a breaking change. Like, that's what it's really meant to be. But we have finer-grained rules around that, of like, you know, do I still compile, or do I have to change method names? If I have to change method names, it's, you know, a compatibility breaking change on the signatures, right?
So, but there's all kinds of braking changes. Like, if I have a working system.
that I configured a certain way, and we make your working system stop working, like, labels don't show up, that would also be considered break-in.
So, in the prototypes as they are now, like, where we got to with the Java prototype, and I think we can do this for all prototypes, there is no actual change to the API.
To get entities to work.
for, various portions of the API. So, like, I can show you… If you want to see the Java prototype, hopefully it's still open.
Sorry, I'm pulling this up, Yeah, this, this, this one is, this is approved.
And we're just waiting for the spec to kind of make some decisions before we commit. But effectively, if we look at the changes here.
I believe… where are the… Resource entity parsing, that's not the right one.
Maybe it's on the other changes? Nope.
sometimes I rely on AI too much, you know? It's not helping me here.
Here they are.
So, the service resource detector is the thing in Java that detects service?
And if you look at the signatures and things, we were able to change code without having to change the signature at all.
And we do have a flag that enables entities or not, but honestly, the resulting resource is the same, regardless of if you have the entity's flag on. The only difference is whether the entity extra information or OTLP is produced.
Like, the entity has the same attributes, right?
**krajo Krajcsovits** 09:26 I guess… I think I mixed it up with… because, again, vague memory of seeing, like, an API where you created a resource and you had now had an additional Entities thing, but I don't see it here now, so…
**Josh Suereth (Google LLC)** 09:40 Oh, yeah, we, we, so we did extend the… Where are they?
On resource, we did make some changes to resource, where you can, when you create a resource, you can actually also add a set of entities.
**krajo Krajcsovits** 09:57 That's a new one, not a changed one, okay.
**Josh Suereth (Google LLC)** 09:58 Yeah, so we did it in a non… basically what I'm saying is we made the SDK changes in a non-breaking way.
**krajo Krajcsovits** 10:05 I gotcha, gotcha.
**Josh Suereth (Google LLC)** 10:07 we actually think we can, in a non-breaking way, just lift all the resource detectors to the entity aware, and then we can fix the broken spec around schema URL in kind of one fell swoop.
So that's kind of what we want to go forward with here, to have a very lightweight Entities opt-in.
And it's just, I think there's gonna be some… concerns around whether this is really going to be breaking, and if we… as we go through SDK by SDK, if one of them finds, that they can't implement entities without having a breaking change.
That will change the discussion, right?
but, yeah, we… I don't know, I… I'm actually talking to… to Daniel, about this, I'm actually kind of comfortable with us moving forward without the opt-in flag. Like, we can have the opt-in flag for safety's sake, but I actually think if you look at the… if you look at this that we proposed for Java, if you look at, what Jack wants to do.
And if you look at the, current shape of the spec.
I don't know if we need an opt-in. I think we might be able to just layer this in, because it's, you know… again, the only thing that manifests is we have a bug in the spec that we're fixing, so we have behavior that's not defined by the spec that will change.
So that might be considered a breaking change, but in almost all cases where it breaks, we're actually, making the behavior better for users.
So, If you weren't there for the spec discussion, there's an issue right now where anyone who abides by the spec is dropping resource attributes when users don't want them to, and so almost every implementation currently violates the resource merge spec.
On purpose, because it's better for users.
And the entity merge algorithm is the thing that Will actually match the behavior of what everyone's doing, even if it doesn't match the spec.
As today. So we want to make a breaking change to the spec that we think doesn't break users. We think that this isn't going to be a breaking change for people. The only thing that's a little weird is, there will be additional crap in your LTLP that you, like, don't see if you're not engaging with entities. So, do we need a flag to turn that on and off?
I'm fine either way, just… but that's… that's the… the only open issue right now on the 1PR, is… is do we keep that flag? And what does that flag mean? I think, let me see if I can find this.
Yeah, this particular here, I'm gonna go to the conversation with Jack.
Because he did a bunch of crap.
There's a comment for me, still.
No, he made the last changes.
Okay, anyway.
Let me see if I can find it… Let me… it's in the spec. I'll just open up the spec. Issues.
Hmm.
Here it is.
So, what Jack was proposing here was, we have this NVER, And what he was proposing was basically whether or not, entities show up on OTLP is what this environment variable does, but it actually doesn't change behavior of the SDK in any way, because we found a way to make the SDK non-breaking with entities.
So, the question is, do we want that, and, like, do we think we need that NVER for safety's sake? Jack would like us to have it. I'm inclined to be conservative, but I also, daniel and I talked, and we don't think we actually need it. We think we could just… go forward, and everything will be fine, and people shouldn't be broken. But, you know, I've learned that that could be hubris, so I'm fine leaving it.
But it does mean we might need to update the prototypes.
**krajo Krajcsovits** 14:14 And would that be opt-in or opt-out?
**Josh Suereth (Google LLC)** 14:18 I think what Daniel and I were saying is this could be opt-out.
Again, we don't… we don't see… Breaking changes in our prototypes right now, where things become entity aware.
**krajo Krajcsovits** 14:34 Yeah, I mean, from a two side, from my side, obviously, we ignore them, so that's not going to… do anything, and OTLP is pretty verbose already, so… Yeah, I don't know.
**Josh Suereth (Google LLC)** 14:52 That's actually one reason why we think it's not a breaking change, because most people will ignore it until you actually gave it.
**krajo Krajcsovits** 14:59 I mean, it's nice to have something opt-out as bray-glass kind of thing, just in case it happens to go over some size limit or whatever.
Like, who knows? You just never know.
**Josh Suereth (Google LLC)** 15:12 Yeah, I think that's reasonable.
Okay.
So, if we were to just do a quick straw poll of folks here, basically leave it, but have it be opt-out.
Is then I can update the current, entity. Yeah, if we come back here.
We would change this to have a default of true.
And we would say, if true, preserve entity information detective resources, otherwise the SDK erases it, and then I can update the SDK to, like, propagate that config to exporters.
And that aligns with what Daniel's saying here.
Okay.
Anyone disagree with that and want to speak up? Or I'll make that a path going forward.
Cool!
Alright, we'll do reply.
That shouldn't be too hard to build. I think that's… that's actually the only, like, major… Issue we have, right.
going on. Daniel has his, startup specification for the SDK that's supposed to be more flexible for async, so please read that. Go ahead, Crave.
**krajo Krajcsovits** 17:13 There's a comment in the chat you want to read.
**Josh Suereth (Google LLC)** 17:17 Oh, I didn't… yeah, I don't have chat up.
With default true, the only thing left to watch is attribute parity between Xiwater sector and the old ones, as resources and consumers now get it without opting in. Yeah, okay. Oh, sorry, Matthew. Yeah, yeah, that's, that's a good point. That's, again, what I was saying in the beginning, I don't know if you were here for that, the, current behavior of the resource detector merge algorithm is a little aggressive by spec. And so it's actually dropping attributes where we consider that a bug.
And so, if we are more flexible and allow attributes to show up, that's what most like, Go just actually started violating the specs so that it could merge and add more attributes, which is now in line with what we do in the entity merge algorithm. So I think the only… when… if you look at the survey that, Robert Paycheck did, the only, SDK where you would see a change in behavior would be Python, and we consider its current behavior actually problematic. Like, we consider it a bug, and it should be fixed.
So, you know, whether that fixes through entities or independent, Robert would like to do it independently. My thinking is we're so close with entities, like, we can just fix them at the same time.
But if we fix the spec to change what the behavior is stated, I think we're fine too. The main… yeah. Anyway.
Cool.
Alright, with that, I don't think we have anything else on the agenda.
I don't have anything else prepared, because I've still been a bit wrapped up on some of the Weaver-related issues that we've been running into.
as we roll out multi-dependencies, which is not surprising, and whole federated SENCOG, So, I haven't had a lot of time to dedicate to this outside of trying to land this, current SDK spec. So, does anyone else have anything they want to talk about?
Alright.
I think we're gonna call it, Ben.
Thanks everybody, and we'll see you all next week. Please, if you haven't reviewed the two PRs, though, like, review Daniel's, review mine, it'd be nice to get more approvals from the SIG.
So, just folks reviewing, making comments, that sort of thing. So, with this extra, like, 20 minutes you have now or so from not having the meeting, please review the PRs. Thank you.
