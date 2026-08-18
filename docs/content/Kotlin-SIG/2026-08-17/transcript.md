SIG: Kotlin SIG
Date: 2026-08-17
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Jason Plumb** 01:16 Viorel, you found it, you found the link.
**Viorel Alexandrescu** 01:18 Meetings.
Yeah, finally. It's been… it's been really hectic with the new, LFX links, because another SIG I'm part of also… Could not join meetings for a week.
**Jason Plumb** 01:32 Yep.
Same.
**Viorel Alexandrescu** 01:39 I just realized that we have this meeting at 9 in the morning Pacific time, right?
**Jason Plumb** 01:46 Yep, on a Monday morning, Monday morning, first thing, yeah.
**Viorel Alexandrescu** 01:51 I see.
**Jason Plumb** 01:53 I love it.
I mean, it's not 8 AM, at least there's that.
**Viorel Alexandrescu** 01:59 I don't know, I'm a pretty early, early guy. I wake up at 5.30 every morning.
**Jason Plumb** 02:07 It's too early.
That's way too early.
I'm not a morning person.
**Viorel Alexandrescu** 02:20 Thank you.
**Jason Plumb** 02:22 Hey, good morning, good evening.
Hello.
**Viorel Alexandrescu** 02:28 Oh, bye.
**Ilia Liferov** 02:29 Kind of new here, joined for the first time.
Just to say hi, and… well, my name is Ilia.
Oh.
And I'm really interested in… in what are… you're working on right now, Wentz?
Hopefully.
I could be helpful or contribute eventually.
**Jason Plumb** 02:56 Cool, yeah, welcome. Yeah, it's nice to have you. Thank you. We always welcome new faces, new talent, We have a… we have a doc here that we can share. If you don't have it, we can put it in the… I'll put it.
**Ilia Liferov** 03:08 Sure.
**Jamie Lynch** 03:08 system.
**Ilia Liferov** 03:09 I have it, yeah. Thank you.
**Jason Plumb** 03:12 Cool. Yeah, feel free to add yourself to the attendees and any agenda items, if you have a topic of… a specific topic of interest, feel free to add it. It's just nice to know also, like, who we have representation from, as far as, like, different vendors or company interest. If you're just an independent contributor, that's awesome, too. We have… we have those.
**Ilia Liferov** 03:33 Great, thank you. Yeah, just follow along for now, and… Thanks.
**Jason Plumb** 03:38 Cool. Yeah.
**Jamie Lynch** 03:40 Cool. I will leave a couple more minutes for folks to join and add items to the agenda, and then we can make a stop.
**Jason Plumb** 04:00 Or poor GitHub. Oh my god. It's…
**Viorel Alexandrescu** 04:04 Oh, yeah.
**Jason Plumb** 04:04 Sure.
**Viorel Alexandrescu** 04:05 I swear to God, it's… I mean.
I got off work at 4.
So, like, for 2 hours, I couldn't do absolutely anything.
And right now, I tried working on what PRs I had open for… for our library.
I can't even see Jamie's comments anymore.
**Jason Plumb** 04:27 Yeah, it's… it's bad. Nothing's rendering.
**Hanson Ho** 04:33 I'm surprised I was able to sync this morning. I couldn't point someone to a file, but I could at least sync, so… random.
**Viorel Alexandrescu** 04:44 I like it, though, how Google… with the brilliance of AI tends to say, yeah, no, sure, GitHub is up and running, and it's all fine, and then you go on the first link, it reads from… with githubstatus.com, and everything is on fire.
**Jason Plumb** 04:59 Oh, yeah. Yeah.
They're having problems, like, every other day, it seems like. This is one of the worst.
Like, everything is broken.
**Jamie Lynch** 05:14 Well, I guess we'll see how it goes with loading up GitHub. Hopefully they fix it in the next few minutes, because otherwise it might be quite hard to discuss some of this.
**Hanson Ho** 05:23 Right?
**Jason Plumb** 05:25 Yup.
Like, for example, just, like, click on the first pull request, like, does it even render?
**Viorel Alexandrescu** 05:31 Nope.
**Jamie Lynch** 05:32 I'll render a unicorn, probably. Oh no, there we go.
**Hanson Ho** 05:35 Ayyy!
**Jason Plumb** 05:37 Right.
**Jamie Lynch** 05:38 I might be render bees.
**Jason Plumb** 05:41 Yeah, definitely been getting a bunch of unicorns. And other weird stuff too, like… like, latest commit can't be fetched, like, you can see the repo codebase, but, like, it has an error that's, like, can't fetch the commit history. Okay.
**Jamie Lynch** 06:00 Cool. Shall we make a stop? If folks do have more items to discuss, or if something comes up during the meeting, please feel free just to dump it in my doc, and we'll… Try and make an attempt to discuss it.
So, first thing is, do we want to release this week? I think we last released about 3 weeks ago.
**Hanson Ho** 06:27 I think we have a bunch of stabilization stuff in there, so yeah.
If GitHub allows us to, of course.
**Jason Plumb** 06:35 Right, those PRs haven't been merged yet, though. Do we want to wait for those before releasing, or just pick it up in the next one?
I don't have a sense of, like, what's in there that's beefy. It just doesn't… Doesn't seem like it's too beefy, in which case, waiting is okay by me.
**Jamie Lynch** 06:54 I guess we could delay another week, if those don't get merged?
Bull.
**Jason Plumb** 07:03 I like that idea.
**Jamie Lynch** 07:04 to, like, if one or two of them get… Get merged, then we could kind of ship, those two.
Oh, yeah, I don't mind.
**Jason Plumb** 07:17 That sounds good to me.
And you ran it last time, I think?
Do you want to run it again, or do you care?
Do you want me to run it?
**Jamie Lynch** 07:29 I'm happy to run it again, and I've probably got the bandwidth to do it, but…
**Jason Plumb** 07:33 Okay.
**Jamie Lynch** 07:34 If you want to do it, you're also welcome to.
**Jason Plumb** 07:36 I got my plate pretty full.
I'd prefer not to, if you're willing to do it.
**Jamie Lynch** 07:44 Yeah, I'm happy.
**Jason Plumb** 07:45 Thank you.
**Jamie Lynch** 07:51 Cool. So that's… But… item done… I just want to skip to this one quickly so we don't… forget it. So, working on PR comments for the JSON encoding feature, did you want to chat a bit about that?
**Viorel Alexandrescu** 08:10 Yeah, so, yeah, you left some comments regarding the implementation. Some of them were based on Hanson's suggestions initially, but when I started writing the unit tests, I feel that the intent diverged a little bit, and I think I could Amend that, amend the current implementation to work well better, at least with the sequences and everything.
But yeah, I'd like to tackle that this week and get it, get it out the door as soon as possible. I feel like I've been postponing this way too much.
But other than that, once the PR for JSON encoding is done, I'll merge the branch into the file export one.
And that should be done pretty fast, I guess? I haven't found many examples in the repository which could help me understand how we're supposed to actually export to a file. I just looked up whatever works in a multi-platform context, and… I hope it's okay.
**Jamie Lynch** 09:19 Yeah, I think… I think OpenTelemetry Java might have, like, some file exporters for OTLP, so there might be some Viore up there, and… there's… I don't think there's too many places where we actually write to a file within the… their current project, either.
**Viorel Alexandrescu** 09:39 I'll leave a note on that,
**Jason Plumb** 09:46 Java definitely doesn't have JSON encoding.
The file? I'm not… I'm not actually sure about that one.
**Jamie Lynch** 09:55 Oh, okay. I might have hallucinated that.
**Jason Plumb** 09:58 I mean, we have a contribib module that writes… to a set of files for disk buffering for Android, but I don't… I mean, it could be in there, and I just don't remember it, because I never use it.
But I'm… yeah, it's worth looking once GitHub heals itself.
**Jamie Lynch** 10:17 Cool. Yeah, and if you need, like, any help with that, or pointers, yeah, feel free just to…
**Viorel Alexandrescu** 10:25 Yeah, yeah, thanks for all the… for all the support. It's just been an issue of finding time to tackle them. But no, otherwise, it's pretty straightforward. I'll hit you up on Slack if I need anything. Thanks.
**Jamie Lynch** 10:37 Awesome.
Okay, so let's talk about the package, context and logger stabilization PRs.
So… Carlos, I see you've left some comments.
I'm the dock.
**Carlos Alberto Cortez** 11:00 Yeah, I was going… long story short, I was going through the specification, doing some stuff, and I cannot get the latest, the very latest… from Kotlin because of GitHub issues as we speak.
But I think it looks fine. The only thing that I wanted to double-check is that there's an implementation in the API for package, you know? You can keep that as an interface, that's what ZVA does as well, but the actual implementation must not rely on the SDK. If that's the case, we are good to go.
**Jamie Lynch** 11:35 Yeah, I think that's not the case.
Right now, so, I guess we can discuss… But, a bit further… If needed on this call. But… Just to, go back to… the, logger and contacts APIs where you… Pretty happy with those.
**Carlos Alberto Cortez** 12:00 Yeah, logger, I remember I was checking that, last month for… I don't remember for what, and it looked fine, you know, and it's a smaller surface, so I think it looks good. For context, for propagation and context, I think it looks, in general, good.
there's also something… well, there are two things, the global… the globality thing, which we can discuss on a follow-up, you know, which I still need to do, and there's a separate point on that. But the only thing that the spec really wants it is that you allow users, you know, to group propagators.
And that can be done.
Either in the API or the SDK, but I think that it makes more sense in the API. It's not a lot of more work.
That could be my thing. I know at the same time, that's also related to the… No op, and actually, that's kind of interesting, because… Most APIs, they have the API, no op.
And then they have the composite propagation and the baggage implementation, which is not really API, so it's kind of… You know, so in this regard, yeah, I am a little bit mixed about the grouping of propagators, but at the same time.
I don't think you would need… and as I said before, I know it's kind of weird, but we are supposed to allow propagation, even if there's no SDK. That's why Bagash has in the API, and it makes sense that we offer, like, grouping of propagators at the API level.
**Jamie Lynch** 13:38 Okay.
So, I think… I think we've got an API that does group propagators, so we have a concept of a composite propagator, which I assume is.
**Carlos Alberto Cortez** 13:53 Yeah, so if that's there, as I said before, I get onto GitHub as we speak, but if it's there, then we are fine.
**Jamie Lynch** 13:59 Okay.
**Carlos Alberto Cortez** 14:00 Yeah.
**Jamie Lynch** 14:14 Okay, so I'll just start an action to check whether Composite propagate a Zoom API service, and… I think… as another action, I'll create an issue to… Move the, like.
no-op implementation of public cases to actually do something.
And have that as the API by default, and… I think I'll probably ping back to you just to get clarification on the requirements for that.
If that's okay.
**Carlos Alberto Cortez** 14:49 Sounds good.
**Jamie Lynch** 14:49 Awesome.
**Jason Plumb** 14:55 Yeah, this is one of those unfortunate situations, right, where we're favoring consistency over correctness.
Because, like, conceptually, this stuff doesn't belong in there, but I get it, you know.
Yeah.
**Carlos Alberto Cortez** 15:10 But it's something similar to how some languages include propagators and context in the API, some others split that.
Yeah, I don't know, it's… Anyway…
**Jason Plumb** 15:24 Oh, you want it in there. You think it should be in there.
**Carlos Alberto Cortez** 15:28 Yep.
**Jason Plumb** 15:28 Yeah.
Yep.
**Jamie Lynch** 15:33 Cool. I think those sound like good actions.
Was there anything else to discuss on B's fee, or should we move on to the next topic?
**Carlos Alberto Cortez** 15:44 I think that's all for now, yeah.
Next point is mine, though, and it's mostly an update. I didn't have time to… Jack. You may remember we were discussing on the global thing, and as you may remember as well, Java, they are not happy with having this global object, but I mentioned that there's value in having the get global.
That's something that, for example, like, the agent, when, you know, it auto-injects the SDK, you need to have the user, you know, able to get whatever SDK you register, you know, even if he shouldn't be able to set it.
So, I need to discuss that with him. One thing that I started checking, something that Lyudmila mentioned, is that how native instrumentation looks. Like, let's say some Kotlin library that we are, like, user is bringing, they already have the hooks internally.
So, how… that may change how… because usually, those ones, they need to get the existing… the running SDK from somewhere.
Right? So if it's native, it's like, just consume whatever the user is using. And that… means that it's a single place where it's… you are… they are fetching that. And that's where also no OP can be useful. Less useful, probably. And this is why I was, like… so once I have that case done completely, like, analyze and compare between different… native implementations, I will go to Jack and talk about this. But this has been slow, and now I want to work on that, because I have nothing to do with my… well, kind of nothing to do with my job for now, so I will try to put myself as a deadline Wednesday, you know?
So, yeah, I have some initial outcome from that. Initial results, sorry.
If that makes sense.
**Jamie Lynch** 17:33 That makes sense. Yeah, yeah, thanks for looking at that. That should be helpful to get clarity on… Like, what the requirements are there.
**Jason Plumb** 17:43 So, Carlos, the… The concern… the… the topic of, like.
native library instrumentations sharing the same SDK instance as, like, user manual instrumentation, for example. There's an implicit race condition there, right? Like, you… the ordering in which the SDK gets created is… is uncertain, right?
**Carlos Alberto Cortez** 18:05 Yep, correct.
Yeah, that's correct. And, yes.
I think that this is also the reason about why you're not providing a set for the user, but still, you know?
**Jason Plumb** 18:15 Yeah.
**Carlos Alberto Cortez** 18:16 The condition there is just less painful.
**Jason Plumb** 18:22 Yeah, so what I would expect, and this is just me kind of riffing, is that if there was a native library, a library that has native OpenTelemetry baked into it, as part of your initialization code for that library, you should also pass the SDK. Like, that's the way I see these things working. Auto-instrumentation complicates that a little bit as well.
But, I mean, that… that's kind of my mental model.
**Carlos Alberto Cortez** 18:46 Yeah, I think that that's actually the last thing I need to put together, because exactly, if you're passing always like, if you're initializing anything that supports OpenTelemetry, you just pass the providers that you need, and that's it, you know?
**Jason Plumb** 18:59 Yep.
But if that library is written with calls to get global open telemetry, then… then who knows, right? Then they're gonna get whatever instance. If it's been set, then they'll get the good one, and if it hasn't been set, they'll get the no-op one, and… Yeah, confusing. I mean, I wish that… I mean, I think… In general, I think a lot of us wish that that global set wasn't there at all.
**Carlos Alberto Cortez** 19:21 Right.
**Jason Plumb** 19:21 As of, yeah.
**Carlos Alberto Cortez** 19:23 Yeah, only to get… but on that point, by the way, is Android doing some kind of… Auto-plogging or something?
**Jason Plumb** 19:31 What do you mean?
**Carlos Alberto Cortez** 19:32 Like, are you relying on the global object in Android when doing… no. Okay.
**Jason Plumb** 19:37 No, we're creating the SDK instance, and we own it.
**Carlos Alberto Cortez** 19:41 Okay, good to know, okay.
**Jason Plumb** 19:43 So if, again, from user code, you initialize OpenTelemetry Android, and then from that you can get the SDK.
Or the hotel instance.
**Carlos Alberto Cortez** 19:53 So… Okay, so this is a tough question. I mean, I will have to keep digging just in case, but…
**Jason Plumb** 19:59 Yeah.
**Carlos Alberto Cortez** 20:00 Are you… are you feeling confident?
That you will never need such a global object, like, not for setting.
From the user perspective, but getting?
**Hanson Ho** 20:11 Well, right now, we don't have any instrumentation for Kotlin, so by not having this, people can't build on it. And if there are scenarios where they can't do anything but get the global.
then I think we can talk about it. But not a permiss… not permitting it, you know, from the start, I think, is… is good. So make them work for it if they really want it and really need it, in terms of, like, justifying the use case.
just because Java does it, because, you know, there's historically instrumentation that requires that.
Let's… let's not repeat that, unless… unless… We have to.
**Carlos Alberto Cortez** 20:51 Yeah.
**Jason Plumb** 20:53 Were you… Carlos, you were asking about Kotlin, or were you asking about Android?
**Carlos Alberto Cortez** 20:56 About Kotlin, yeah.
**Jason Plumb** 20:58 Okay. Okay.
**Carlos Alberto Cortez** 20:59 Yeah, if Andrew… I mean, if you don't have it, it means that, yeah, like, most… odds are you will not need it in Kotlin as well.
**Jason Plumb** 21:09 I agree with Hanson. Like, it seems like we should only… we should only do it if we're really forced to.
**Carlos Alberto Cortez** 21:15 Yeah.
**Hanson Ho** 21:16 With an app, you're pretty deliberate in what instrumentation you offer. There's no, drop this in, or magically, it'll get detected.
app developers generally want full control, and when they have full control, initialization is required, then, you know, attaching it to some API that gets passed in is very reasonable. So, I think, at least if we're just talking about Android.
you know, I don't think we need this. Now, there are other use cases for Kotlin. That's not Android. Those are where I am not 100% sure, but at the same time, let's… let's make them justify it before adding it.
**Carlos Alberto Cortez** 21:54 Okay, yeah, that's good context. Okay, thank you so much for that. Yeah, that's useful.
**Jamie Lynch** 22:05 Boom.
Any additional topics?
**Carlos Alberto Cortez** 22:15 I'm fine for no.
**Jason Plumb** 22:18 I can't remember any without clicking on GitHub. That's not working too well for me.
**Carlos Alberto Cortez** 22:22 Yeah, correct.
**Jamie Lynch** 22:25 Yeah, so I suspect we can just call it a bit early today, given GitHub is not that reliable.
**Jason Plumb** 22:33 Yeah.
**Viorel Alexandrescu** 22:34 Yep, sounds good.
**Jason Plumb** 22:36 Okay.
**Jamie Lynch** 22:37 Awesome. Thanks for coming, everyone.
**Viorel Alexandrescu** 22:40 I think one more thing to bring up, I remember just now, Jamie, you said once to raise a PR with a request for membership?
And I think Jason was left to leave a comment, I'm not sure.
**Jason Plumb** 23:01 Oh, is it… is it open currently?
**Viorel Alexandrescu** 23:05 Oh, yeah, I know I tagged you there.
**Jason Plumb** 23:09 I'm so sorry, I thought I did that, but… What is your GitHub handle?
**Viorel Alexandrescu** 23:14 Viorel dash, my surname.
**Jason Plumb** 23:20 I'm not gonna find it. Let me… let me see.
The problem with these kind of outages is, like, you kind of can't trust what you see. Like, you do a search, and you can't find it, and you're like.
Am I doing it wrong, or is it just not finding it?
This was in Slack, right?
**Viorel Alexandrescu** 23:42 No. No, I followed the procedure and put it on GitHub.
**Jason Plumb** 23:48 Alright, someone found it. Okay. Thanks.
**Viorel Alexandrescu** 23:51 Oh, yeah.
**Jason Plumb** 23:53 Let me… and it's in the community repo, right?
**Viorel Alexandrescu** 23:56 Oh, yeah, yeah, yeah.
**Jason Plumb** 24:00 And it's probably an issue.
VR.
Hmm…
**Viorel Alexandrescu** 24:09 Yeah, no, yeah, you're right.
**Jason Plumb** 24:13 Let me see, I'm almost there.
**Viorel Alexandrescu** 24:17 I think I found it.
Because somehow the URL got cached.
**Jason Plumb** 24:22 Yeah.
**Viorel Alexandrescu** 24:24 And it loads. Wow.
**Jason Plumb** 24:26 I know. We're getting lucky here.
Yeah, sorry about that. So, I did not see this. So, the way that GitHub works is that you… it does not allow you to notify a random user on GitHub just by mentioning them in an issue. So, I never saw… I never saw a notification for this.
I mean, I follow the community repo, but I mostly don't look at it, because it's too much traffic.
**Viorel Alexandrescu** 24:53 I guess it's one of those things, if you don't follow me and I don't follow you, it's not gonna send anything, because it's like we don't know each other.
**Jason Plumb** 25:01 Exactly, and so this could be abused to spam people, you know, and so they don't allow it, but, yeah, obviously… Your help is greatly appreciated here.
**Viorel Alexandrescu** 25:11 Yes.
**Jason Plumb** 25:12 That should move it forward.
**Viorel Alexandrescu** 25:14 Thanks.
**Jason Plumb** 25:15 Yeah.
Alright, everyone, thank you.
**Viorel Alexandrescu** 25:22 Thanks, everyone. Thank you, everybody.
**Ilia Liferov** 25:24 Dave.
