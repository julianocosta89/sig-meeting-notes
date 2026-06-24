SIG: Android SIG
Date: 2026-06-23
Duration: 40 minutes
============================================================

## Zoom Recording Transcript

**Hanson Ho** 05:18 Hello, David. Let's see if anybody else joins today.
**DavidGrath** 05:28 Good deed.
**Hanson Ho** 05:31 How's it going?
**DavidGrath** 05:34 It's going good. Yeah, it's going fine, thanks.
**Hanson Ho** 05:40 I forgot to ask where you're based.
Let's see…
**DavidGrath** 05:51 Nigeria.
**Hanson Ho** 05:53 Oh, cool.
Oh, what's hot? Oh, it must be pretty late over there right now.
**DavidGrath** 05:59 No, it's not bad, it's 4PM right now.
**Hanson Ho** 06:02 Okay. Oh, right, it is only 8 o'clock.
Let me copy the agenda.
I'm gonna see if.
**João Oliveira** 06:26 Thanks, folks.
**Hanson Ho** 06:29 Hey, Joao!
I'll give you David's name in there.
We have a pretty light agenda today, hey, Cesar!
**Cesar Munoz** 06:46 Hello?
**Hanson Ho** 06:48 Jason is out, do you want to run the meeting today?
Good morning, or good afternoon.
**Cesar Munoz** 06:54 Thank you. Yeah, I'll… Perfect. I'll take care of it.
**Hanson Ho** 07:01 created the.
**Cesar Munoz** 07:01 sick.
**Hanson Ho** 07:02 No worries.
So, for the new folks, hi Ben, I have, there's a doc that we have that, for our agenda that you can take a look at. Feel free to type anything in there and put your name, if you choose, for attendance. We'll get started in a couple minutes, I guess, when… Cesar's ready!
**Cesar Munoz** 07:27 Almost there.
Okay. Nope.
Here it is… So, for those who might… Be the first time joining.
Welcome.
As Anson was mentioning, and also please, if you can add your name here… That'll be nice.
Yeah, save that.
Okay, so… We have an empty agenda for today.
Maybe usually what we do is… Take a look at some issues.
Let's see… Let's see…
**Hanson Ho** 08:26 Couple of updates, or one update, still waiting for the Play SDK index.
Gonna get Severin to talk to them again.
**Cesar Munoz** 08:40 Oh, the Play Store…
**Hanson Ho** 08:42 Yep, you guys have all been added, or the maintainers have all been added to the, if you log into Google Play, you should see yourself. Or you have to maybe accept the invitation. But, but still not… well, you know what? I didn't check this morning. How about that? I'll check right now.
**Cesar Munoz** 08:56 Can you imagine? It's just, just to, like… The magic happened.
**Hanson Ho** 09:03 entirely possible.
But not today. Got it.
**Cesar Munoz** 09:12 So, it's right.
Thanks for taking care of that.
Hansen. I didn't know it was gonna take that long, to be honest.
Well, you guys already had to go through that.
**Hanson Ho** 09:23 Waiting. All we did was wait.
**Cesar Munoz** 09:27 Oh, for this… also, you're still waiting for Embrace as well?
**Hanson Ho** 09:31 Oh, no, for Embrace? Oh, Em, we, we, we, I don't recall, but I don't recall waiting this long. It was, like, fairly standard. You submit it, they look at it, they approve it, and on they go. But it took two attempts. The first one, they kind of got lost, and then they got it immediately, and then we filled in a bunch of forms, and then… And then, and then we submit it again, and then that's been, 3 weeks, 4 weeks. Feels like it's been forever.
**Cesar Munoz** 09:59 Yeah, I guess. Anyway… Let's keep waiting.
I'm gonna take a look at the issues, but in the meantime, if somebody wants to add something into the agenda, please feel free to do so. I'll take a look at it.
After… Checking some issues.
So this one… Okay, so I'm not gonna go through all the details. You can have a look at it offline if you like, but it's kind of like… what I understand is that Ben said, I don't know if I pronounced it correctly. It's proposing, adding more configuration options for the periodic exporter, because right now, if I'm not mistaken, it's hard-coded to 10 seconds to export data, and by export data.
It's kind of weird, because we have a… Disk buffering, which has exporters, but in reality, they actually export into the disk.
So it's actually just storing stuff in the disk, but then this one is related to actually exporting it over to the internet, so… I think we're currently fixing it to every 10 seconds.
So, they're providing a way to override that config.
I think it's fine. Now, apart from just… thinking that it's fine. Oh, somebody had created a PR for it.
Haven't taken a look yet.
But I guess usually the problems… the problem with this comes to where to put that config, and what name to set to that config, so… If somebody's interested, probably can take a look at the PR.
And, I can also have a look later.
But essentially, that's what this is about.
And this is… Kind of similar thing of adding more config options.
But in this case, it's to add a config to the DSL, That allows to… Tweak how this buffering works.
But in a way, if I understood correctly, that… this configuration. So, for those who might not know, we have essentially two ways of initializing the engine.
So there's a, RAM builder way, which is… Kind of like the, the… the most… The lowest level of configuration that you can… that you can use.
And then we have the DSL, which is in the… what we call the agent.
that… It's more Kotlin-friendly, and it should also be… like, more friendly in general. Like, you should have to, you know, provide some conflicts You know, without… without… Too many details, or too many… too much, you know, cold.
And I think that's what Benza is proposing here.
Kinda like, you know.
for those who might not know, this buffering, it's a tool that is available in the construct repo of the OpenDelemetry Java construct repo, and it's very low level, and it has a lot of config options.
what Vince is saying that we shouldn't expose those directly, and instead we should make it simple, something like, you know.
exporting frequency and discard the stale data after X amount of time. It seems pretty straightforward enough to me. I like that idea.
If somebody… it's probably addressed in this NPR?
I haven't checked this, sorry.
So, if somebody has… Like, an idea for this kind of config names, or… Or if somebody wants to take a look at the PR, please. Please do.
And if there's any questions, please just… you know, ask it right away. I don't mind, interrupt me… interrupting me.
**Hanson Ho** 14:25 It is kind of weird… it is kind of weird to depend on… or have a configuration, at the Android agent level for a package that is external to it. So the dependency that we create is… is… hard. Directly exposing the interface, I guess, well, somewhat directly. So, are we okay with that? Because… we're effectively saying, like, I think most of the other configuration, it has to do with projects or instrumentation, or the agent itself, that live inside, this repo, and arguably could be considered part of, like, the OpenTelemetry Android project.
This one is… is… Kinda not. It lives elsewhere.
like, do we provide, like, are we going forward, gonna provide, other configuration settings via DSL for, For modules that are not part of the project?
**Cesar Munoz** 15:33 I think… I think, if I underst… yeah, I think I see what you mean in the sense that… we… And it's probably related to the name, actually, now that I think about it. So… It's true, it's a separate, library, this offering.
But I think what it provides, it's something that… I… I would say it's core to… to… Any kind of telemetry source or agent.
for mobile.
Because you should have to store data in this.
First, so, so… Maybe, and I think this is probably something that… adds to what Benza is pro… is suggesting here.
In the sense that, okay, so let's not use specifically the names and stuff from this third-party library.
But regardless of what's… you know.
behind the scenes, we still need to, you know, store some stuff in disk, and then we want to control you know, How that works.
In this case, it's providing these two… options, like, it doesn't have to be only those two. And probably now that you're mentioning this, maybe we don't even have to use the same name as the library. Like, maybe if we do something like cache, or something like that, in the DSL, That could, you know, that kind of abstraction could make it, you know, less tied to the… to the underlying library. Will that… will that kind of work in this case?
Yeah, but in the end, what I'm trying to say is that storing stuff on disk.
like, it's… it's core to, I think, what we want, you know, to laundering.
**Hanson Ho** 17:37 I'll take a look at this PR, but yeah, no, I 100% agree. If we effectively make this a local persistence mechanism, and have… have… have basically… fairly high-level, configuration that we then, currently will set on the disk buffering package, but in the future, if we use, say, like, the Kotlin SDK, then that gets built in, so we don't have to use that, but we effectively preserve the API for So, I just…
**Cesar Munoz** 18:09 swap the, the.
**Hanson Ho** 18:11 I do like that.
**Cesar Munoz** 18:12 Yeah. So, so I think this is a great opportunity, then, now to… because nothing is defined right now.
Perfect. To specifically chime in, in terms of namings, I think it's… Key part here.
So, yeah. Yeah, I agree.
Feathering?
**Hanson Ho** 18:34 Great, fantastic.
**Cesar Munoz** 18:35 federated semantic conventions, Okay, so I think… What Jason was saying here is that The, idea is to not… Hard code semantic conventions.
But also not define them in the semantic conventions repo yet.
But still use the same kind of mechanism used in the cementing conventions repo.
That being, you know, the YAML structure and the… Weaver? Weaver? I don't know what's the name of that tool to generate those files.
Apparently it's something that is already being done in the, Kotlin SDK.
So, if I understood him correctly.
So, I think it sounds good. He already started to… to work on that.
But my understanding is that Jason is gonna be away for a week, if I understood correctly, so… you know, we're not gonna hear much on that right now, but yeah, I think it's good. Sounds good.
**Hanson Ho** 19:46 he has a PR, I think, open that demonstrates, how some of this stuff could be moved over.
I'm not sure if it's public or if it's just still a draft.
Yeah.
Phase 2.
**Cesar Munoz** 20:05 to… Yeah. Yeah, the Phase 1 got already merged.
The Phase 2, I think I got a comment.
**Hanson Ho** 20:13 Okay.
**Cesar Munoz** 20:18 Thanks, yeah.
See what I'm for some feedback from him.
**Hanson Ho** 20:26 Cool.
**Cesar Munoz** 20:28 But yeah, I mean, feel free to have a look as well.
Okay, kotlin semantic event classes… I think this is kind of related, is it?
or… Or no, or this is done already? I know he already used some Kotlin semantic conventions.
Here.
**Hanson Ho** 20:52 Yes, but I don't think Kotlin's released, a release that has the semantic event… convention, events defined yet. So, so I think, yeah.
we have to wait till that lands and that is released, before we could do that. But, in theory, everything in semantic conventions, that comes from there could be referenced from the, the Cotton Semantic Conventions. So even event names. And also even the, I think the, the event, The thing that does the emission.
**Cesar Munoz** 21:31 Got it.
So the stuff that he wants to add here… It's definitely, Android-specific, and I'm guessing what's defined in Kotling is, like.
you know, platform agnostic, probably, if I understand correctly.
**Hanson Ho** 21:49 Yep, it's basically just… so instead of defining… depending on the Java semantic convention repo, we're depending on the Kotlin.
So, it's the same thing, it all comes from the same YAML, it's just generating classes that are available from the Kotlin repo, or from the Java repo. So, effectively, we're just inlining the same string, but the source is different.
But all generated from the same YAML, from the semantic conventions.
**Cesar Munoz** 22:23 Got it.
Thank you.
**Hanson Ho** 22:24 I think… I think the… the… the… this event stuff, doesn't exist in, in Java. It only exists in Kotlin, because I think that's the stuff that, Jason put in, to actually do that generation of, of events.
**Cesar Munoz** 22:39 events.
Yeah, I haven't taken a look at it, at the Java one in a while, so… Yeah.
I haven't checked this one.
Hmm.
I've heard people call profiling another signal.
**Hanson Ho** 23:07 Yes.
**Cesar Munoz** 23:08 And I know that we've had some issues in the past where People want to generate this kind of data.
for mobile, I'm still a bit confused, because every time I see this kind of data.
it's… it's… it always seems a lot, you know? So… so I'm not sure… I mean, it almost kind of feels like it's… kind of… should be only used for debugging purposes, like… locally.
Like, I don't see, you know, this kind of data you know.
going into a production database, in millions of devices at the same time. I don't know.
Seems like a lot.
But.
**Hanson Ho** 23:54 So, the interesting thing, I think, here is just to play with it a bit, because I have no idea what the overhead is, especially in how much data it generates. One can imagine that any meaningful amount of profiling is going to generate a lot of data.
but the idea of hotel profiling is to basically, radically reduce the amount from typical profiles, but I actually don't know what the runtime implications are, so I think before… taking on this. Someone should play with it, and just, you know.
see if it actually even works, because there's no guarantee that the Android process is able to provide the same amount of information, given the runtime permission restrictions as one… as a Java process that runs on the backend, so…
**Cesar Munoz** 24:51 Yeah, it sounds kind of like a bit of an intrusive process, at least when it comes to Android and their… their rules, yeah?
**Hanson Ho** 25:01 It'd be interesting. I mean, if someone wants to take a look, I think that'd be excellent to have a look at.
**Ben Joseph** 25:08 Does this kind of data make a lot of sense in mobile? Like, if you're, you know, collecting this kind of data from a large set-up, but this, I feel like, makes more sense for, when you're, like, monitoring servers.
limited number of machines, but, like, a large fleet of Android devices sending these kind of data in great detail, I don't think that can, you know, make meaningful, I don't know if it's data collected versus actionable insights.
**Hanson Ho** 25:39 given the heterogeneity of Android devices, and also the randomness at which processes are throttled, even by the scheduler, depending on resources, battery, and the fact that we don't have the ability to have high cardinality dimensions.
means that there's no way to contextualize this data. But… just like metrics, there… there… there could be some use cases. If… for… if not for general usage. So I think it'd be interesting just to see, A, the data that we get from this from Android, if it's possible, and B, how much overhead there is in terms of both runtime and also, like, how big the data is generated. So, I think… Being able to answer those questions could definitively make us… say, yeah, we want to look at this, or we don't. So, I don't… I actually… I agree with you, Ben. I don't know how useful this data will be, given the limitations of… of… pre-aggregated data that we can't disambiguate on the server side. But it… there could still be some usages, so I would support anybody looking to do some exploration. I'll make a comment on this later.
**Ben Joseph** 26:59 Yeah, any, any, actual use case for this? Also, like, if you… if you have ever seen any community comment or any user requesting this kind of feature, I think that… that also… would be a strong, evidence, but, like, this is, you know, pushed down from a different environment altogether, I feel.
**Hanson Ho** 27:19 Yeah, there's a lot of, like, I think, desire for Android to support various things that the backend supports, so EEPF and things like that.
it's one of those things where I can tell definitively that for 80% of or more of use cases, it's just not going to apply because of the runtime restrictions. But there may still be some… applicable ones. So anybody who wants to explore, like, the frontiers of this, I think, is more than welcome to, in my opinion.
**Cesar Munoz** 27:54 I agree. Thank you, Ben. I don't have any use case for that right now. Like, like, not a, like, Observability, right?
And I, I think it's… it's probably a good thing to… It's probably a way to start taking a look at these kind of issues, like, from, you know, in a kind of in a backwards way.
Which is, like, okay, what's… what's the value that it will provide? And… If there is, then we'll… we'll work it backwards and try to make it work.
But I guess my… what I've… heard so far about eBBF is that It's, you know, Android is Linux, then it should work, so it… Might just work out of the, out of the box.
And… and I guess that's fine, but then… but then we get to that.
Part of the equation, which is, okay, but then… what's this useful for? And I don't have anything for now, so…
**DavidGrath** 29:06 Good.
**Hanson Ho** 29:08 Oh, go ahead, David.
**DavidGrath** 29:10 I was going to ask, I'm not certain, but wouldn't you need router access for that?
**Cesar Munoz** 29:16 Probably.
**Hanson Ho** 29:17 We don't have the ability to provision processes. The OS gives launches. I think I made a comment in that issue, or on the Slack, saying that, you basically need, AOSP custom setup and built-in support at the OS level, and then having a way for apps, to enable the instrumentation. So, like, the end-to-end kind of pull-through is, requires a number of things that I think are difficult to achieve at this point, certainly for general usage. So, with profiling, I mean, profiling would probably even be closer to be useful, because if we could populate the profile in a different way, and just use the structure of the profile, signal, to put thread information.
But it wouldn't be necessarily the same type of profile that you would expect. It's gonna be like a span, where, yeah, it's shaped like a profile, but it's gonna look… different. So, I think there are potential use cases for this, but… it's farther off ahead and requires a bit more work. It's not simply about turning on the profiler and say, hey, here you go, here's some information.
But I'll turn that all on, or I'll up… I'll put that all in my comment.
**Cesar Munoz** 30:45 Thanks, Hans.
**Hanson Ho** 30:48 It was today's catch-up day.
**Cesar Munoz** 30:51 I think the rest of the issues, if I'm not mistaken, we already discussed them in the past.
Sick meetings?
**Hanson Ho** 31:01 We can take a look at the, the milestone for the release and see what's left over, because, I think Jason was talking about doing a release, but we weren't sure, what, well, he didn't have time before he went on vacation, so it'd be good to look at,
**Cesar Munoz** 31:18 Yep.
So… is this the master?
**Hanson Ho** 31:25 Feels like there's a… oh, oh, yeah.
**Cesar Munoz** 31:28 Update also core, yes. I already created a PR for that.
I think David already approved it.
So… yeah… yeah.
So, yeah, I was planning to… I created a couple of PRs today to prepare for the next release.
And once those are merged, I'll, I'll… kick it off. I think I can start it right now, right after the SIG meeting.
**Hanson Ho** 31:58 Weren't we waiting for instrumentation to release?
And they've done that?
**Cesar Munoz** 32:03 Or… You mean upstream Java instrumentation?
**Hanson Ho** 32:07 Yeah, I thought… I thought Jason last week was… oh yeah, you weren't here last week, but Jason, I think, last week was talking about he was waiting for the instrumentation to be updated so he can update that, because there's something in here that requires it. But if… if… if it passes, then it must have… it must have… it must have been fine.
**Cesar Munoz** 32:25 No, no, you're right, and I already updated it.
**Hanson Ho** 32:27 Perfect.
**Cesar Munoz** 32:28 In this PR, so… yeah, we got the instrumentation, constrip, and… Core, upstream.
**Hanson Ho** 32:35 Nice.
**Cesar Munoz** 32:36 updated in this PR. So my PRs are this one, and then one for the, change log?
You wanna have a look? Where is it? I'm all lost here.
This one, I'll put it in the… in the dock.
And so, once that's spiritual… Just kick the, the release.
**Hanson Ho** 33:02 Excellent.
**Cesar Munoz** 33:04 What else? That's for the release.
There's a lot of stuff there, please have a look.
Sorry about that. Have a look at the, changelog changes.
**Hanson Ho** 33:20 Oh, maybe before we release, we should, update Android to 37. I'll take a look at that today.
Where am I? I'll add it to the, to the agenda. We can talk about it a little bit. Android 37 was released, so it… or, sorry, Android 17, so SDK37.
But… Hot light. Oh, whatever.
Any objections of trying to get this in today, so that we can be part of the release?
**Cesar Munoz** 34:12 No, I mean, it's just updating the… Compile is decay, is that?
**Hanson Ho** 34:18 Yeah, just to compile SDK. There isn't even… because we're not an app, so we don't even have a target SDK. All the issues that potentially could come… come about is with Target SDK. And that's up to the apps to do, and not us. So, I think for us, this ought to be a… there should be no difference. Like, it should be very safe.
**Cesar Munoz** 34:42 I mean, well… Yeah, I think it's… it's mostly just… probably… how long was that release? Because probably the only thing… I think it's fine. It's mostly… it's gonna be kind of annoying, I guess, if I remember correctly, and a consumer of the… Android agent will have to also bump there.
Compile CK before they can add the new version.
Right now, right?
**Hanson Ho** 35:08 No, 36 could use it, because, because, we're not changing the minimum supported, compile SDK version, right? So if we change that… so right now, you can even… you can compile this with probably, like, 35, 34, whatever it is, lower. So, this, this does not, this does not take away from, a minimum, compiler version, minimum Android version, it doesn't change any of that, or it ought not to.
**Cesar Munoz** 35:43 Got it. I mean, if it's… if it's not gonna cause any… annoyances, then I think it's fine. Are you planning to create a PR for that?
**Hanson Ho** 35:52 Yeah, it should just be a one-line change, in theory, so…
**Cesar Munoz** 35:57 And I think there was a PR that was blocked because we still didn't have that.
number, version.
was for an Android X… related to an AndroidX library that… Was it? Or maybe I don't play this stuff.
**Hanson Ho** 36:16 Yeah, no, it's Android… it's AndroidX, Core, 1.
111.9, or 1.11.19, or something like that.
**Cesar Munoz** 36:26 This one.
**Hanson Ho** 36:29 And I don't know if… I forgot if it's for this project or for Kotlin, but we can't update to, Kotlin 2.4. I will… I'll put this in.
**Cesar Munoz** 36:43 I've already, I already merged Kotlin 2.4.
**Hanson Ho** 36:46 Oh. Oh, really?
**Cesar Munoz** 36:48 Yeah.
**Hanson Ho** 36:49 Oh, I thought we couldn't do it because, CodeQL didn't support 2.4.
**Cesar Munoz** 36:58 Yeah, but CodeQL is not… is not blocking, because it usually doesn't support the latest version of Kotlin for… Oh, for a while.
**Hanson Ho** 37:06 Oh, okay, Oh, okay. All right, cool. Last time I checked, it was, it was, it was, it was red, so, I was talking to, to, to Jason, so I didn't, I didn't… merge it, but okay. I mean, if it's merged, then it's fine. I think we… we already set the, target, API and the target, standard live to 2.0, so… or… or something lower. So, again, it shouldn't change anything.
**Cesar Munoz** 37:35 Yeah, I mean, the compatible Kotlin API should still be, I think, 2.0.
Cool. It should be fine.
So, this is what I meant when I said, if we raised our number.
People were targeting this message in their projects?
**Hanson Ho** 37:53 Nope.
They shouldn't…
**Cesar Munoz** 37:55 Okay.
**Hanson Ho** 37:56 Android X is just requiring this, because Google wants everybody to use the latest SDKs, because they want not only the SDKs to be used, but they want the new OS to be supported, and they want they want apps to target new OS within a year. Like, I think if you're… if you target anything below 30, 5, you would have been, like, kicked out of the Play Store, like, a year ago. They'll give you a few months of grace, but then you have to basically target 37.
**Cesar Munoz** 38:32 Got it. So if you do land this PR, Then that could cause that because of the transitive.
dependency… Of this library.
**Hanson Ho** 38:44 Yes. Unlimited, right.
**Cesar Munoz** 38:45 Okay, so.
**Hanson Ho** 38:45 Yes.
**Cesar Munoz** 38:46 We find not to merge this for this release?
**Hanson Ho** 38:49 I believe so. Yeah, so we don't want to export transitively a dependency update, but frankly, within a few months, everybody will be using 37. Most people will be using 37 anyway, but we shouldn't… there's no reason we should do this at this point.
**Cesar Munoz** 39:08 Yeah.
Sounds good. Okay, so please let me know when you have the PR.
And I'll approve it right away. And, we can move on.
**Hanson Ho** 39:19 Yep.
**Cesar Munoz** 39:20 with the release.
**Hanson Ho** 39:22 I might just try to do it now, because I know it's late.
So if we're done early, I can… I can try to do it.
**Cesar Munoz** 39:30 Apart from that, is there anything anybody else would like to discuss?
I mean, we have some time left, but… If there's nothing, we can also take some time back.
So…
**Hanson Ho** 39:45 We have the client, the client sig is also at 9 o'clock, if any… or in about 25 minutes, if anybody's just enjoying that.
**Cesar Munoz** 39:55 Client sake meeting.
It seems like not for today.
So I think we should take some time back.
**Hanson Ho** 40:06 Sounds good.
**Cesar Munoz** 40:07 in the meeting. Thanks for joining.
And… talk to you later.
**Hanson Ho** 40:12 Good ones.
Right.
