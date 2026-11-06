SIG: System Sem Conv Stability SIG
Date: 2026-11-05
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Pablo Baeyens (Datadog)** 00:45 8.
Like, you're working twice as hard today, you don't know.
**Donal O'Sullivan** 00:55 Yeah, I joined via the browser, and I…
**Pablo Baeyens (Datadog)** 00:58 I can't hear you, I'm not sure if it's me or…
**Donal O'Sullivan** 01:03 And…
**Igor Peschinskii** 01:04 I can't hear you, though.
**Donal O'Sullivan** 01:07 You, you, you can hear me… No.
**Pablo Baeyens (Datadog)** 01:09 doesn't work. Could you try and speak, Igor? To see if…
**Igor Peschinskii** 01:13 Do you hear me?
**Donal O'Sullivan** 01:16 I can hear you, yeah? Can you hear me?
**Igor Peschinskii** 01:20 Yes.
**Pablo Baeyens (Datadog)** 01:20 No, I cannot hear anything. It's probably me.
I'll be right back.
**Donal O'Sullivan** 01:28 Yeah, I… I use the Zoom browser app, so when I joined, I closed the tab, so I rejoined, but it seems like it keeps the old, The old, the old connection there.
**Igor Peschinskii** 01:39 Yeah, typical.
**Pablo Baeyens (Datadog)** 01:47 Okay, I think… Baby, no, it should work.
**Donal O'Sullivan** 01:52 Can you hear me now?
**Pablo Baeyens (Datadog)** 01:53 Yep, yeah, I can hear you now.
Cool. Cool.
I… haven't had the time to look into the… filter package thing that you sent me.
Probably I won't have time tomorrow either, but I'll take a look next week.
**Donal O'Sullivan** 02:18 Yeah, that… that's… yeah, there's no rush. I… I… yeah, I guess the issue was just the name, so I just thought, like, yeah, it's… it's… the issue is it's a generic name, and if… Like, should it be a, I guess, a more precise name? So it's just a name change, like… Yeah, look, just to… Okay.
Yep. That's all it is.
Yeah, the only other things I had was, there's an open issue in CollectorContrib to make the process metrics Feature gates… beta, so they'd be turned on by default. I don't think we should do that yet, should we?
Because it'll probably break a lot of, customer, well, end users,
**Pablo Baeyens (Datadog)** 03:05 Yeah, I don't think we should do it yet,
**Donal O'Sullivan** 03:14 Given all the discussions, you probably want to wait for V2… Before we even consider, like.
turning on RC metrics now, right? Wasn't that kind of the idea?
**Pablo Baeyens (Datadog)** 03:25 Yo.
Yeah, we can talk about it with the others, but yeah, probably…
**Donal O'Sullivan** 03:37 I know, I know just for ourselves, like, at Elastic, if we did that, it would, like, it would break our… I know, obviously, we'd be able to turn our, like, turn off the RC metric, but it would break, break at least one dashboard do we have, but
**Pablo Baeyens (Datadog)** 03:50 Yeah, same here. It would break her.
**Braydon Kains (Google LLC)** 04:01 Hello.
Sorry, I joined the automatically attached Google Meet to the room booking, and just sat there empty.
Wondering where everyone was.
**Donal O'Sullivan** 04:13 Nice.
**Pablo Baeyens (Datadog)** 04:22 And have you checked anything about the configuration yourself, or…
**Donal O'Sullivan** 04:29 Yeah, so I briefly looked at it, and Yeah, like, my understanding is we just… we need to look at all the configuration settings at the base for the receiver, and also, I assume, for each scraper, because each scraper has its own… configuration setting. There's a couple that have quite a few fields, so I guess, like, that's… yeah, probably just… I haven't, like, gone through it and looked at, like, which ones are… I guess, which ones could be deprecated or not, but Yeah, I don't know, do we want to discuss that? Maybe not. Maybe I could probably find some time and go through them, and if there's anything that can be… removed, I could probably just raise it in the next, in the next SIG meeting, maybe.
just, like, from looking at the stability dock, our guidance, you know, the item we spoke about stable for… Was it March next year?
**Pablo Baeyens (Datadog)** 05:27 Yep.
**Donal O'Sullivan** 05:28 item.
**Pablo Baeyens (Datadog)** 05:31 Yeah, Yeah, maybe it makes sense.
If you have the time for you to…
**Donal O'Sullivan** 05:41 Yeah.
**Pablo Baeyens (Datadog)** 05:42 take a general look, and then we discuss it. Yes.
Are we meeting next week?
Or…
**Donal O'Sullivan** 05:48 Oh, you're being QConed, I guess, what are you?
**Pablo Baeyens (Datadog)** 05:51 I will be here, but I don't know if…
**Braydon Kains (Google LLC)** 05:55 I think, me… and Roger… And… Dimitri and Christos will be… at KubeCon.
**Pablo Baeyens (Datadog)** 06:07 Okay.
**Braydon Kains (Google LLC)** 06:08 I don't know if we were gonna put time on the… like, in-person meeting calendar, not…
**Pablo Baeyens (Datadog)** 06:17 Maybe we should.
**Braydon Kains (Google LLC)** 06:19 We can, we can probably cancel, so this meeting will be at… 8.30?
AM?
In Utah? I'm trying to… I'm doing the time zone math, I think. So, I mean, it'll be… it would be happening at a time slot that would be, like, before I'd probably go to the conference center, so I would be okay.
**Pablo Baeyens (Datadog)** 06:41 Yeah. Yeah, it's a fairy, so…
**Braydon Kains (Google LLC)** 06:44 I'd be okay with joining a meeting if we did want to meet next week, if, like, if we did have something substantial to talk about, then… I probably could before I head out to the conference.
**Pablo Baeyens (Datadog)** 06:59 Mmm… I'll see you all.
**Braydon Kains (Google LLC)** 07:02 Anyway…
**Donal O'Sullivan** 07:03 Yeah, I don't mind, you know, maybe we'll just skip it, will we? Is that easier.
**Pablo Baeyens (Datadog)** 07:07 Yeah, I don't mind skipping 8 if, like…
**Braydon Kains (Google LLC)** 07:10 Sure.
**Pablo Baeyens (Datadog)** 07:11 I don't know. I don't want people to wake up earlier than usual.
**Donal O'Sullivan** 07:14 Yeah.
**Braydon Kains (Google LLC)** 07:15 Yeah.
If the primary thing that we'd talk about is the config stuff.
I'm planning… I actually… once I saw Donal's comment, I started, like, slowly looking through, and I plan to make a comment for each one.
Yeah.
I've just been… I've been too distracted with stuff I'm trying to wrap up before… before I leave, so I haven't gotten to it yet, but…
**Donal O'Sullivan** 07:38 Yeah, no panic at all, like, I was more just trying to get the ball rolling, I guess, you know?
**Braydon Kains (Google LLC)** 07:42 Yeah, thank you for doing that, because,
**Donal O'Sullivan** 07:44 roadmap.
**Braydon Kains (Google LLC)** 07:45 I lose track of this type of thing, so I don't initiate it when I should.
**Donal O'Sullivan** 07:50 Yeah, it's no worries. If I get a bit of time myself, I'll take a look, and I'll just… I'll go through them, and…
**Braydon Kains (Google LLC)** 07:58 Offhand, the only thing I can think of is there's a feature I'd like to add to all the scrapers, which is to allow them to independently set a scrape time, but I don't think that's a stability blocker, because that's an, like, an added feature.
Yeah. So…
**Donal O'Sullivan** 08:16 Yeah, I think it's more so just take, like, removing features is a bit of an issue, isn't it? Yeah.
**Braydon Kains (Google LLC)** 08:22 I can say the one big thing that exists in the config right now that pisses me off is these mute flags for specific errors in the process scraper. That has bugged me so much, and I was the first person who wrote one, but that was just because, like.
There was no… there still is no mechanism to easily suppress those errors other than config flags, so…
**Donal O'Sullivan** 08:46 Hmm.
We could remove them.
I don't think we…
**Braydon Kains (Google LLC)** 08:51 I don't know the right way to, like, introduce proper muting like that.
**Donal O'Sullivan** 08:56 Yeah.
**Pablo Baeyens (Datadog)** 08:57 stir away on the Clarity config to, like.
tweak the logger, maybe that is the way, but I don't.
**Braydon Kains (Google LLC)** 09:05 Yeah, so there… there is… I don't know if we expose it, but there is, like, in the SDK in general, there's this idea of, like, views.
which I think is usually used for metrics more, but I think it works for logs, that maybe if there was a way to, like, exclude logs with a view or something, I don't know if that would work, though.
**Pablo Baeyens (Datadog)** 09:25 I think views are specific to metrics, but I may be wrong.
**Braydon Kains (Google LLC)** 09:29 Yeah, yeah. I've only ever heard of it, specifically metrics, so that might be the case. I don't work with the SDK as much.
**Pablo Baeyens (Datadog)** 09:41 Yeah, I don't see anything on the… sorry, go ahead.
**Braydon Kains (Google LLC)** 09:45 I was just gonna say, I, like, when… To deal with this problem on our own, like, collector build.
I had actually, like, written… a ZAP core.
That filtered out these logs specifically.
Like, with a… with a regex, I think?
And that… because, like, it was pre-OCB, so we wrote our own main, so, like, I just, like, took the collector's logger and wrapped it in a bunch of cores that excluded logs and stuff.
And I don't know how to generalize a feature like that, but it would be good, because actually there's more cases of Filtering out error spam, That would be really nice, especially with, like, GRPC… has some super spammy errors when you use, like, Round Robin, for example.
**Pablo Baeyens (Datadog)** 10:39 Hmm.
**Braydon Kains (Google LLC)** 10:40 That's a… that's another case where, like, it would be good to come up with a core… a core way to fix this, but I don't know what that would look like.
**Donal O'Sullivan** 10:50 It's almost like using the… Processor on the collector.
remove the logs, but not do it after they're being emitted. Do it, like, in the actual.
**Braydon Kains (Google LLC)** 10:59 Yeah.
**Donal O'Sullivan** 10:59 Yeah, yeah.
**Braydon Kains (Google LLC)** 11:00 It's like, do it so that the log never gets emitted at all.
**Donal O'Sullivan** 11:02 Yeah, yeah, exactly, like, yeah.
No.
Could we use the processor in the… Receiver. It's like, you know.
It's gotta be rotten.
**Braydon Kains (Google LLC)** 11:14 The only… the only thing I can think of is that, like, the way the logger… the way the process scraper takes a logger is it takes it out of, like, the component settings that are passed in.
if… in, like, mDataGen, we could have some sort of log filter config.
**Donal O'Sullivan** 11:32 when you…
**Braydon Kains (Google LLC)** 11:33 Use that from internal metadata, and you wrap Basically, for this scraper, you wrap the… the… Logger in another Like, pre-step that filters out logs.
**Donal O'Sullivan** 11:45 Yeah, yeah, and that's done the components, instead of… After it's window. Yeah.
**Braydon Kains (Google LLC)** 11:49 Yeah.
don't 100% know if that would work, because with ZAP, the whole, like, the order of things when you, like, wrap cores is always confusing, like, I think it's… the outer… it runs from outermost wrap to innermost, but I can't remember the exact steps. Anyways, that's… Might be worth looking into.
if it's… I don't know if it's urgent enough to, like.
Try and force something before we stabilize.
**Donal O'Sullivan** 12:20 Yeah.
**Pablo Baeyens (Datadog)** 12:27 Yeah, I don't see anything on the… spec. Like… So this is the way to filter. I think that would be the best, like, the…
**Braydon Kains (Google LLC)** 12:37 Yeah.
So we use a bridge, right? Like, we use a ZAP bridge from the SDK, and that's how the self-logger works?
**Pablo Baeyens (Datadog)** 12:51 Yep.
Yeah, there's… it's a fairly complicated bridge, because… Yeah. Well, to support the old and the new stuff.
And also to support, like, Logging before you hopped.
Parse the configuration so that you can.
**Braydon Kains (Google LLC)** 13:09 Oh, yes.
**Pablo Baeyens (Datadog)** 13:10 customized the booker, but yeah, in the end, it's… Yeah, actually.
**Donal O'Sullivan** 13:20 I don't know how it works at all.
Haven't looked into it.
**Braydon Kains (Google LLC)** 13:26 I remember looking into it at one point just to figure out, like, if we could log from a custom provider we were writing.
And that's how I found the whole, like, buffered logger before the service starts, and it's…
**Donal O'Sullivan** 13:38 Yeah.
**Pablo Baeyens (Datadog)** 13:40 Fun stuff.
**Donal O'Sullivan** 13:45 Would that… would that be an issue? Like, could we do that after going V1?
Remove that, then? Would that be a bigger problem?
**Pablo Baeyens (Datadog)** 13:53 I think we after V1.
**Braydon Kains (Google LLC)** 13:55 We could add the feature after V1, and yeah, yeah, I think so. We could add the feature… after V1, and, like, recommend people use it, and then in V2, remove all the mutes.
**Donal O'Sullivan** 14:04 Yeah, makes sense, yeah, add it to, like, the configuration, then make it, like, a default or whatever, yeah.
Yeah, makes sense.
Yeah, cool.
The only other thing I was talking to Pablo about before you joined, Braydon, there was a PR open to make the process metrics RC, Feature gates beta, so they'd be on by default.
I think that's… I don't think we want to do that yet, do we?
**Braydon Kains (Google LLC)** 14:37 No, I don't… I don't think we should do that before V1. And I think the explanation for that is in, like, the strategy document that I still have to write and haven't gotten to yet.
**Donal O'Sullivan** 14:48 Yeah, fair enough, no worries. Yeah, I think I tagged you guys in the issue, there's an issue in Contrib about it.
**Braydon Kains (Google LLC)** 14:56 I'll try and find it.
**Donal O'Sullivan** 14:57 Yeah, I can… I have it here, actually. I'll just put it in the, Put it in the meeting notes. Oh, no, sorry, it's the first… yeah, it's the first item in the agenda, actually.
Should be that one.
I don't have the same, wave the e-guys would have on their replies, so…
**Braydon Kains (Google LLC)** 15:35 Let me close the agenda document.
There it is.
Yeah, I'll comment on the issue that we don't actually want to.
I don't think I have any other topics, I don't know if anybody else does.
**Donal O'Sullivan** 16:59 Oh, I have no sense.
**Pablo Baeyens (Datadog)** 17:02 Nothing from me. I want to spend some time on the resource detection processor, I think for this sake, maybe, like.
the system detector is the thing that we care most about, unlike host ID.
But yeah, I'll let you know.
Next week, or, well, in a couple of weeks.
**Braydon Kains (Google LLC)** 17:25 Yeah.
I think I'm interested in this idea of, like, the new… default list for host ID.
Yeah, let's… Keep an eye out for it. There's some… I think, like, right now there is no empty default, so there being an empty default, it's not like people are gonna start getting unexpected behavior or something.
I do think there's some cases where, like, people might have configured a resource detector when they shouldn't have, when it's, like, a gateway collecting from lots of sources, like, those should already come with resource stuff anyway, but…
**Pablo Baeyens (Datadog)** 18:04 Well, there's a… default, right, Igor?
**Igor Peschinskii** 18:09 Yeah, it's nth detector.
environment.
**Braydon Kains (Google LLC)** 18:13 Well, there is a default. So, like, just for… So… If you don't specify anything, it's just the info detector, then?
**Igor Peschinskii** 18:23 Alright.
**Braydon Kains (Google LLC)** 18:24 Okay, I didn't know that.
So we would be.
**Pablo Baeyens (Datadog)** 18:28 I think it'.
**Braydon Kains (Google LLC)** 18:28 Any kind of default.
**Pablo Baeyens (Datadog)** 18:29 Yeah, I am skeptical that… people are using DOT, I don't think.
**Braydon Kains (Google LLC)** 18:33 I don't think people would care that much, to be honest.
Like, if anything, people who configure Resource Detector and then don't… put anything, probably don't really know what exactly they're getting, and they're just gonna start getting better data, and it's just gonna be fine? I don't know, that's my… expectation, but… That's fine, though, I'll keep an… I'll keep an eye out for the… For any activity on the issue. Did I comment on the issue already?
**Igor Peschinskii** 19:09 Yeah, it's.
**Braydon Kains (Google LLC)** 19:10 supported? Okay.
**Igor Peschinskii** 19:14 There are some comments from David to fix the default behavior of Kubernetes detectors.
**Braydon Kains (Google LLC)** 19:19 Oh, okay.
**Pablo Baeyens (Datadog)** 19:22 Yeah, I asked, David and Pablo to comment.
I think they already did, right? Or at least one of them?
**Igor Peschinskii** 19:35 David created an issue, and someone volunteered to… to make a PR, but it seems like it's still in problems.
**Pablo Baeyens (Datadog)** 19:44 Okay.
Cool. Then… I guess enjoy CubeCon if you're going, and see you in two weeks.
**Braydon Kains (Google LLC)** 20:06 Thanks.
See you in two weeks.
**Donal O'Sullivan** 20:09 There you go.
