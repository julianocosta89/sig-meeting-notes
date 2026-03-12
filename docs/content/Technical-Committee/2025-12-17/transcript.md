SIG: Technical Committee
Date: 2025-12-17
Duration: 14 minutes
Zoom Recording URL: https://zoom.us/rec/share/Vw9wTNkcv54P9fjTuaDwBWco5qyi7bSmL6a6_W8s7jGyEN-3cFzosw_fTcp8f1k.zirfWn5n3yf67j7w
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 00:49 There's just two of us here.
**Josh Suereth** 00:51 Yeah, did they cancel?
**Liudmila Molkova** 00:54 Did they?
**Josh Suereth** 00:56 I don't know, I'm looking.
Oh.
**Liudmila Molkova** 01:02 Carlos will be 5 minutes late.
**Josh Suereth** 01:05 Yeah.
**Liudmila Molkova** 01:22 So let's maybe give them a few minutes to join, and if just Carlos joins, then we'll probably call it.
**Josh Suereth** 01:29 Sounds good to me.
**Liudmila Molkova** 03:15 Josh, did you bring mechanical keyboards with you?
**Josh Suereth** 03:19 Where I am now, I'm at home.
My flight's tomorrow, but, like, we're supposed to do, yeah, we, the Time Shift app, I don't know if you've seen this. It's like, I'm supposed to avoid bright light until noon.
It tells you when you can have coffee and when you can be in the light, but, like, I'm supposed to be in bright light then until midnight tonight.
To help with the transition. And then my flight tomorrow, basically I'm supposed to board the flight, immediately put on dark sunglasses, and go to sleep.
**Liudmila Molkova** 03:54 I fly in business class?
**Josh Suereth** 03:57 And then… and then, or at least try to sleep. It says, like, if you can't, just stay in the dark. And then, then you're supposed to, like, have bright lights at particular times to help you transition into the new time zone. So, I'm trying it out to see if it works.
**Liudmila Molkova** 04:15 I hope it will.
**Josh Suereth** 04:18 Yeah. For context, Jack, I'm in a dark room with sunglasses on.
Trying to pretend like I'm in a different time zone.
**Jack Berg** 04:26 Are you gonna disclose where you are in the world?
**Josh Suereth** 04:29 I'm still… still in pit.
**Jack Berg** 04:30 Oh, right, you're still at home, you're coming back from somewhere, right?
No, no, no, I'm getting ready to go. I'm going somewhere… tomorrow's my flight, so I'm going somewhere tomorrow. Okay, okay.
**Josh Suereth** 04:38 Yeah, so this is my last working day of the… of the year.
**Jack Berg** 04:45 We might actually get, quorum, despite this, slow start, because Carlos said he'd be joining 5 minutes late.
**Liudmila Molkova** 04:53 And it's already 6 minutes.
Do we have an agenda?
**Jack Berg** 05:00 Yeah, there's no agenda.
**Josh Suereth** 05:07 Yeah, I have absolutely nothing urgent, because I'm in vacation mode. I know that David Ashpole already is on… is out for the holidays.
**Jack Berg** 05:17 there is an item in the TC inbox.
**Josh Suereth** 05:23 Let's… that's exciting, let's look at it.
**Liudmila Molkova** 05:27 Markets.
**Jack Berg** 05:50 What would it mean to deprecate Jaeger propagation in OpenTelemetry?
in Java, we bundle all of our propagation formats, or propagators, in a single package.
And so, where we could… end of life, the Jaeger exporter and the Zipkin exporter, because they have their own packages, and so while we don't delete any code ever, we can stop publishing a package ever. We can stop publishing a package. We're not obligated to keep… we've convinced ourselves that we're not obligated to keep publishing packages forever.
But since the Jaeger propagator is bundled in with a bunch of other propagators, which are not Being deprecated.
I think that we have no route forward to actually remove this.
**Liudmila Molkova** 06:49 No, remember, but you can deprecate the API.
**Jack Berg** 06:53 That's true.
**Carlos Alberto Cortez** 07:03 Yeah, if I remember correctly, I think the organization you have in the Java repo, regarding the packages, one package having multiple propagators, it's something I saw in other repos, like Python, for example, you know.
But yeah, they being able to… even if they cannot remove that propagator, being able to say.
That, you know, these… don't use this, this deprecated products, good enough for them, so they don't have to implement new features or anything like that.
**Jack Berg** 07:31 Yeah, and notably, Yuri has, no objections. He commented with no objections on the issue.
**Liudmila Molkova** 07:45 Should we just mark it as accepted? Is there any… are there any objections?
**Jack Berg** 07:59 No objections. Okay, we can… I mean, it's not merged until it's merged, right? So, like, we can proceed with opening the PR to deprecate it, and if anybody has objections, they can raise them at the PR. So it's not like this is set in stone. We're just telling them, giving them a soft approval to continue.
**Carlos Alberto Cortez** 08:20 Yep.
By the way, probably the open tracing propagation should also be deprecated, you know?
**Liudmila Molkova** 08:32 Mainly maintained.
**Carlos Alberto Cortez** 08:35 Yet.
OpenCensus, I'm not sure. So, long story… long story short, the open tracing propagation was something that we were trying to use, see how that would work, but that was before W3C came.
that's from the, very early days from open tracing. I don't think many people are using that, and even when I was adding that, the, that support in the specification, Judy had opposed that, because he said he's not widely adopted.
And I think we can do that now. Even if… Even if you don't remove it, also saying, like, don't use this one, you know? Or if you're using that, just move to W3C, there's no reason not to move there.
**Liudmila Molkova** 09:25 Okay, yeah, this makes sense. What do we do here? Accepted needs sponsor, right?
And it's probably Treyville enough.
**Jack Berg** 09:39 Yeah, why don't we say accept a new sponsor, and then, I can assign Robert to be the sponsor, because he volunteered.
**Liudmila Molkova** 09:48 Oh, he volunteered, nice.
Okay.
Then, it doesn't need to be a need sponsor, it's ready.
**Jack Berg** 10:00 Yeah, okay, good point.
**Liudmila Molkova** 10:02 Ready this sponsor.
Carlos, do you want to create an issue for open tracing propagator?
**Carlos Alberto Cortez** 10:18 Yep, I can do that.
**Liudmila Molkova** 10:22 Yeah.
Thanks.
Done. That's it.
Does anyone have any agenda?
**Armin (Dynatrace)** 10:44 When is our next TC meeting? We will have the two weeks of quiet period, right? So it will be the 7th of January?
Am I right?
**Liudmila Molkova** 10:56 Yep, you're right.
**Armin (Dynatrace)** 10:59 I'll put that in the… in the chat now.
You're already on mute.
**Carlos Alberto Cortez** 11:04 Since… since we have all three.
Oh, never mind. I thought it was a new issue, just the holidays, the January 7th. Notice.
I have a small question, it's not super formal, since we have free time. Now that the Kotlin, Multi-platform codebase will be, donative, and we'll start working on that.
I wonder what's… how… I don't… I'm not familiar how eBPF did that, like, whether they could bring their entire history of the project.
Or you would rather start fresh. I'm saying that because if you bring the entire history of the repo, that will include a lot of embrace stuff.
I think it's okay, but I don't know if you, have an opinion about that.
**Josh Suereth** 11:50 For, simplicity, when we did Weaver, we had everything from scratch. That was actually a… I don't remember if that was a formal donation or not. I think my concern here is just, if you force all of the people who had the original commits to sign the CLA, that could be awkward.
like, it might actually… you might run into tooling-related problems. So, like, if they want to do that with all that history, and say that code is now, like, copyright by CNCF because they've signed the CLA, and all the authors have done so, great.
if they're not willing to do that, then having one person verify all the code is okay to sign over to CNCF, and have one person sign the CLA and send it in, like, a big commit that's, like, the initial import.
From a tooling standpoint, that is easier.
Right? But in terms of preference, like, you know, whatever works there. I… personally, I would, I'm kind of a, like, give up and don't fight the tools guy, so make one person from Embrace, look at everything and say, this is acceptable to give the CNCF, sign the CLA, and have one commit that brings it in without the history.
And then just… evolved from there in OTEL, but if we think the history is valuable to keep.
for various reasons, or, like, there's justification in the Git commits that we're gonna want.
Cool. That, you know, go with the harder option and try to make it work. It's possible to do so.
**Carlos Alberto Cortez** 13:29 Okay, perfect, yeah, that's great, that's good information, yeah. Okay, I will ask them, and we will decide how that goes.
Sweet.
**Jack Berg** 13:41 Just another… Bit of prior art with the injector we did what Josh is describing as well.
Where a single commit seeded the repo.
**Carlos Alberto Cortez** 13:53 That's good. Okay, good to know. That's totally fine, then.
**Liudmila Molkova** 14:09 Okay, so then should we call it?
**Jack Berg** 14:17 Alright.
See you all in a couple weeks.
**Carlos Alberto Cortez** 14:20 But…
**Josh Suereth** 14:20 Everybody have a good holiday.
**Carlos Alberto Cortez** 14:21 Okay.
**Josh Suereth** 14:23 Or a vacation, if you have one.
Yeah.
