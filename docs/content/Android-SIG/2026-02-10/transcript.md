SIG: Android SIG
Date: 2026-02-10
Duration: 57 minutes
============================================================

## Zoom Recording Transcript

**Jason Plumb** 00:16 Good morning.
**Hanson Ho** 00:18 Hello?
**Jason Plumb** 00:23 How are you?
**Hanson Ho** 00:25 Not bad, how about yourself?
**Jason Plumb** 00:27 Hanging in there.
**Hanson Ho** 00:33 How many hours do you spend a week in hotel meetings?
**Jason Plumb** 00:38 In community meetings, like SIG meetings, under 3.
**Hanson Ho** 00:42 Oh, it's not bad.
**Jason Plumb** 00:43 Yeah, yeah.
It used to be a little bit worse, but, I mean, it used to be a little bit more, but,
No, now it's pretty much this, and the JavaSig, and it's sometimes client, and sometimes I get pulled into a few other things, but it's like…
I'd say on average it's under 3-0.
**Hanson Ho** 01:00 It's not bad.
**Jason Plumb** 01:02 No.
**Hanson Ho** 01:04 A lot of interesting ones, but simply, simply do not have the time.
**Jason Plumb** 01:08 I know, it's really tough to do it all.
Let's see…
**Hanson Ho** 01:14 How many days until… until spring? 38 days!
**Jason Plumb** 01:17 Oh my god.
Yeah, 38. It's right around the corner. I can feel it.
**Hanson Ho** 01:24 I'm going to Mexico at the end of the month for, like, 5 or 6 days, and… Good fall. Yeah.
**Jason Plumb** 01:31 Yeah.
**Hanson Ho** 01:33 Oh, God.
Hello, by then, that'd be pretty warm.
Hey, Cesar. Hey, Jamie.
**Jason Plumb** 01:42 Hello.
**Cesar Munoz** 01:45 All good things.
**Jason Plumb** 01:58 I guess we can get started. It's a pretty light agenda today. I have been a little bit busy and not giving this repo much attention.
So…
I just carried this one over from last time. I know that, Hanson, I saw some update from you that I didn't give more than one second to, so…
I know that you had worked with Severin, it looks like, right?
**Hanson Ho** 02:23 Yeah, submitted PR, that adds a bit of metadata, that, one merge and one release next time.
Google will pick it up and say, hey, this is something, and we can… we should be able to log on to the Play Dashboard with,
some account that has access to that app and see some stats. So right now, it's only tied to the admin atopentelemetry.io email address, but you can certainly create, you could… I know there's a way to delegate it,
admin and basically assign, other people, to have access to that, once logged on. So, I think once we get the approval email, I can talk to Severin to basically go in the… go in there and just, add,
At least the maintainers, if not the approvers as well, so we can take a look.
**Jason Plumb** 03:19 Very cool, okay, awesome. Yeah, because being able to, like, having the metadata there and having it be incorporated is great, but then also being able to see the results is the other half of it, right?
**Hanson Ho** 03:29 Yeah, I don't… I… but we'll see how… what the data that comes in. It's… it's…
In the past, it hasn't exactly been, like, super useful. Like, it doesn't comprehensively say, hey, this is how many people actually
use the app which has this SDK installed, at least the last time I looked for Embrace. We know we have a lot more users than what the Play Console gives credit for, so…
**Jason Plumb** 03:56 Yeah, and it's probably not a good way to project that either.
**Hanson Ho** 04:00 No.
**Jason Plumb** 04:00 It is.
**Cesar Munoz** 04:02 Yeah, but I agree, as you said.
That, you know, it's better… it's nice to have something, so…
**Hanson Ho** 04:08 Exactly, exactly.
**Cesar Munoz** 04:10 That's great. I wasn't aware of this.
tool that the Play Console provided.
But see, maybe, maybe it's how to… More metrics, let's see.
**Hanson Ho** 04:20 It's… you're gonna get some crashes and some, quote-unquote A&Rs, but they're not actually gonna be real, because, you know, the way Google does A&Rs is, where are you in the 5-second mark? And if it happens to be in one of our code, it'll kind of be, like.
And then somebody will complain and be like, hey, why are you causing A&Rs? And you explain for the millionth time, that's not how that works.
Yeah, Google has a lot of things that they don't really promote, or, or, or, or, make aware, people aware. People know that you can use, Play Console, Android Vitals for apps, but not a lot of people know about the SDK thing, so…
**Jason Plumb** 05:01 Yeah, I certainly didn't prior to this, so this is great.
**Cesar Munoz** 05:07 Yeah, it's very cool.
And… and what I like is that, in order to add it.
It's only that, you know, properties file.
So that… because I know that there are some stuff related to the Play Store that, when you add it into an app, or…
Well, I guess it's just only an app.
I think it kind of makes it difficult.
Or, it just won't work when…
the app is installed in a device that doesn't have Google
Play Store or, or, you know, things like that, but it's like, if it's just this,
Properties file, then… then… Then you shouldn't have any issues, and… I think it's great.
And, and to your point, Of the actual number of users that have this SDK running.
I guess that's also a valid, I guess…
Way to look at it, in the sense that…
users who might be using those applications that contain this app, but they didn't get that application from the Play Store.
then I'm guessing they won't… Count for these metrics, so…
**Hanson Ho** 06:24 Yeah, and also the Elastic and the, Honeycomb and the Splunk distros that have, like, you know, a different…
you know, module that includes it. I don't think that will be listed.
Not 100%, but we will see.
But yeah, it's… it's… it's something.
**Manoel** 06:48 Yes.
**Cesar Munoz** 06:49 I'd think…
**Manoel** 06:50 I think if it's a transitive dependence from any other library, it still counts, because what Play Services does is, like, unpack everything, and check for the resources, and check the IDs, and count as installed. Even if it's out… even if it's not installed through the…
to the, store, I think, because actually this is Google Play service is doing at runtime on the device, so what matters is actually that you have Google Play service installed, so Chinese devices most likely not.
**Hanson Ho** 07:24 Okay. That, that, that, that, that, that's, that's slightly better.
I was worried.
**Cesar Munoz** 07:31 That's interesting.
**Hanson Ho** 07:32 part of the app bundle that gets downloaded, if you use bundle architecture, and they count it, like, through that, but if it's, like, you know, runtime, play services, that's… it's better.
**Cesar Munoz** 07:42 Based on…
**Manoel** 07:43 Where's…
**Cesar Munoz** 07:43 So, Manuel.
**Manoel** 07:45 Yep.
**Cesar Munoz** 07:47 Do you think, well, based on what you said, if it doesn't matter, you know, how the SDK got there, I mean, if it's transitively, or directly or whatever.
would it mean that it… and also, because I'm thinking of a question that Jamie added into that.
We'll request that you open handsome.
then would it make sense to add this ID into the API module? You know, something that's
Contain in all of other modules, so that we can count Whatever users have installed.
So let's… let's say I use her. Yeah.
**Manoel** 08:30 I think just, like, the most core module would make sense, because everyone else would have this most core module as a dependence anyway, right? But if there are modules that people could install.
directly, and let's say you have two. Sometimes it's one, sometimes it's the second, sometimes it's both, then maybe it makes sense to have both, because the stat is going to be more complete.
**Cesar Munoz** 08:54 That's true.
**Manoel** 08:55 If it's an undrided library, and everyone depends on car anyway, then just a car would be enough.
**Cesar Munoz** 09:02 And that's why I was mentioning API, because I think that's the one that's Embedded in all of…
The other modules.
But then again, it's what you say, we wouldn't get, like.
Specific details for each, if we go this… this way.
**Hanson Ho** 09:20 I mean, if the data looks good, and the count looks like, hey, wow, this is pretty decent, then, you know, if we have, you know, certain use cases, like.
you know, that require people to pull in specific modules, then we can kind of include it. But if it's transitively included, like, I was thinking, hey, you know, we can put in core, and then if people explicitly include it, then we can know how many people explicitly include core. But if it's… if it's transitive, then that doesn't… that doesn't do anything. It won't give us additional information. So let's… let's see what this data comes… comes back with, and…
And then we can decide.
**Manoel** 09:55 Yeah, I mean, the SDK is already a transcript evidence from the final app, right? The hosting app, so it has to be recursive until everything.
**Hanson Ho** 10:03 Yeah, but the register… the registration was, like, directly with the SDK module, so that's what I thought there would be a…
**Manoel** 10:10 Yeah.
**Hanson Ho** 10:11 special, but who knows? Sometimes Google is very opaque, when it comes to how this stuff is calculated, anyway.
**Manoel** 10:20 Yeah, it's closed source, so it's…
I did reverse engineer one Space Services, and yeah, it's quite hard.
**Hanson Ho** 10:26 It's… there's a lot of implications in the,
the actual dashboard, they don't actually say. Like, you know, when they measure startups, it's… it's actually, they take one instance from each device, each day. So if you have multiple startups, that gets, like, kind of normalized. Not normalized is the wrong word, it gets flattened. There's a lot of, like… which is why, like, in small numbers, if you try to, like, make the numbers match, it becomes really weird. It only becomes useful when you have, like, you know, large numbers, and you want to look at trends.
Good for monitoring, not really great for observability, so…
**Manoel** 10:58 Nope.
it's been zero days that someone compared Google Play services data, you know, with some other observability.
**Hanson Ho** 11:10 How come they don't match? Do you know the timestamps I have? No, no? Okay.
So, yeah, I don't know when we're gonna release 1.2 next, but, you know, when we merge this, when we do, it'll be… it'll be, it'll be there. It'll take a few, seven days, they say, to… to actually get the approval email, and that's when the data starts coming in, so…
**Jason Plumb** 11:33 I think we should get into the next release. Next release is 1.2, right?
**Hanson Ho** 11:36 Yup.
**Jason Plumb** 11:37 Okay.
Yeah, so I think, I think instrumentation has not released yet. I think that'll happen Friday, probably, or… they've been doing it on the weekends, so it's either this coming Friday…
Yeah, so Jan 16th, so it'll probably be Friday or Saturday.
And then, we can do our release immediately after that. That's kind of been the cadence. Like, they're following a week behind Java Core.
So, Java SDK does its release, then they do their release, and then us.
And one day, We may not be so strongly coupled.
to these upstream? Well, it'll just be a different upstream. Yeah, that's the dream, one day.
**Hanson Ho** 12:20 One upstream, instead of…
**Jason Plumb** 12:23 Yeah.
Well, yeah, we gotta figure out instrumentation, but we don't have a huge dependency on instrumentation, which is great.
I saw Santos pop up, I thought, for a little bit. I've reached out to him on our internal chat, because I haven't seen him around in a while, and I was wondering if he had a question or something, but he… I think he dropped off.
**Hanson Ho** 12:45 he was the one that was, that was writing the, the metrics, thing, supposedly, for, client and user-facing apps. And, you know, our recommendation for metrics.
**Jason Plumb** 13:01 Okay.
Got it, got it, got it.
Cool, sounds like he's got some other questions. He said he'll rejoin at 8.30.
That is, if we're still here. We will be. Okay, so what, are there any other pull requests that people definitely want to see in the release next week that we should focus on?
From this blue line, you can tell how far behind I am.
**Hanson Ho** 13:26 I think all the ones that are, like, convert stuff to Kotlin, the more trivial stuff.
**Jason Plumb** 13:31 Yeah.
**Cesar Munoz** 13:34 Yeah.
**Jason Plumb** 13:34 These are all nice-to-haves, right? Like, that's not gonna… hopefully, no functionality change.
**Hanson Ho** 13:40 No.
**Jason Plumb** 13:41 What's… Oh, there's that one, okay, and then… So I put it.
**Cesar Munoz** 13:46 I think the most crucial was the one that you created, Jason, which I think is Merge.
**Jason Plumb** 13:52 Fix, yeah, yeah.
Cool, cool.
The clock bug fix, specifically, yeah. Okay, cool. And…
I think it's been a little while since, Cesar, since you've run the release. Do you want to do it this time, just to be fresh on it?
**Cesar Munoz** 14:08 Sounds good.
**Jason Plumb** 14:09 Okay, cool.
**Cesar Munoz** 14:11 Yeah.
I'm guessing it'll be next week, too.
Cheers.
That is great.
**Jason Plumb** 14:19 Yeah, probably Monday is my… is my… probably my guess, yeah.
**Manoel** 14:24 I just noticed that I've been away for a while, and the way they came back, now the version 1 is out, so maybe I should be away again for the.
**Hanson Ho** 14:36 Well, when I talk…
**Manoel** 14:38 done.
**Hanson Ho** 14:38 When Kotlin is out, we can cut ver… and we're… we're, we're okay with it. We can do version 2.
**Jason Plumb** 14:46 Yeah, oh, well, so… This is just my gut. I suspect we'll do version 2 before…
Kotlin is stable, but do you think… you think Colin will go stable before we do 2-0?
**Hanson Ho** 15:00 Oh, not stable. Like, release and, like, the pseudo-stable that we're like, hey, there's, you know, embrace is productionized on it, the API has been vetted, and all the API compatibility tasks have gone. And in fact, we could probably just initially just use a compat implementation, to make it even that much safer. But,
we found, anecdotally, that even using the Compat implementation in Brace, app startup is a lot faster.
Because, we're a lot lazier when loading stuff. So, it's, it's… the… the actual SDK startup time during app startup is, you know.
double… it's quite a bit faster, but we're talking about, like, you know, 20, 30 milliseconds, on, like, an average device. So, people will notice that, or rather, developers who pay attention will notice that, but people generally won't.
Still, good win.
**Jason Plumb** 15:55 Yeah, yeah. Okay. And then, Manuel, to your point about us hitting 1.0, just to be clear, and maybe we could do a better job about having some sort of stability statement, like in the README or something, but right now.
The only artifact that we're publishing that has a non-alpha suffix. Like, everything else in here is publishing with an alpha suffix, except for the agent. So, this is the one that we're considering stable.
All of the other modules, including the core module, and all of the instrumentations, and even the BOM, are still considered alpha.
**Manoel** 16:31 Thank you.
**Jason Plumb** 16:31 So they're a 1.0, but they're a 1-0 alpha, and so that we think that the next package
that we can trend toward stability is probably the instrumentation API.
Which I think is this.
Is it… is this the right package?
**Cesar Munoz** 16:46 Oh, like… Skull and Android.
This one. Okay, yeah.
**Jason Plumb** 16:52 This one.
**Cesar Munoz** 16:53 Which.
**Manoel** 16:54 By the way.
depend on everything else? Or…
**Jason Plumb** 16:59 Ask again, please?
**Manoel** 17:00 So does the agent…
**Cesar Munoz** 17:02 and everything.
**Manoel** 17:03 Exactly.
**Jason Plumb** 17:04 Yeah, Aiden's kind of the topmost, yeah.
**Manoel** 17:06 Exactly, because if the topmost is stable, technically everything underneath is kind of stable as well, or at least…
I mean, if it's installed by default.
**Jason Plumb** 17:20 Yeah, we've been so…
**Cesar Munoz** 17:21 depends on how you look at it. It's, like, stable, it's API stable.
**Jason Plumb** 17:26 Exactly.
**Manoel** 17:27 Yeah, gotcha, gotcha, gotcha.
Now I got it.
**Cesar Munoz** 17:30 No.
**Jason Plumb** 17:30 the… behaviorally, like, we always will consider stuff stable, like, we're not gonna crash your app. Anything that is, like, risky or, like, has some amount of, like.
risk to it, I think we should put behind an experimental flag, or have experimental in the name.
But yeah, everything should not crash your app. Like, it should be stable in that regard. It's really API stability for developers that we're focused on. So anybody who's, like, building an app and using the agent, when they upgrade version to version, they shouldn't have to change their code.
**Hanson Ho** 18:04 What was.
**Jason Plumb** 18:04 Yeah, that makes sense.
**Hanson Ho** 18:05 What's the official statement on attribute stability?
**Jason Plumb** 18:11 There are groups, there are collections of attributes which have a stability level of stable.
It's still, if you look at the semantic conventions, it's the minority.
In order to declare an instrumentation stable, I believe its attributes also need to be stable.
And anything that's not needs to be opt-in. So that is… that is a block… I don't want to say a blocker, but that is a requirement of making it to stability. So, for example, if we wanted just to pick one… if we wanted to make fragment instrumentation stable.
then it would need to be emitting stable telemetry, meaning the names and attributes on this data should also be stable in the semconf.
If that makes sense.
**Hanson Ho** 18:58 Yep.
**Cesar Munoz** 18:59 I think it makes sense. Yeah.
**Jason Plumb** 19:02 And over in Java, you know, they're doing a pretty good job now of, like.
Chunking out every few months a little group of behaviors that become stable.
So I think HTTP was first, and now there's, like, database semantic conventions are becoming stable, and there's, like, I think there's, like, 3 or 4 others now that are… that are coming along.
**Cesar Munoz** 19:23 I've seen, I've seen a couple of, Issues regarding stability.
And, in, and upstream, repos.
where… My understanding is that there seems to be an idea going around where
Instrumentations will have some sort of fly.
That will allow… You know, when enabled, it will send both stable and non-stable attributes, or something like that.
**Jason Plumb** 20:00 That's right.
**Cesar Munoz** 20:02 I find it a bit confusing, because…
So my understanding is that if that flag is disabled.
Does that mean that you only get to send stable attributes only?
even if… you know… Even if you want… you might want to send an attribute that
Only has an unstable version.
Because it's too new, for example.
**Jason Plumb** 20:29 Yeah.
**Cesar Munoz** 20:31 Then you will still have to wait until it becomes stable.
**Jason Plumb** 20:36 Unless you can actually…
**Cesar Munoz** 20:36 use it.
**Jason Plumb** 20:37 Unless you opt in, right? Unless you opt into these additional parameters, yeah, these additional attributes, yeah.
**Cesar Munoz** 20:44 Maybe, okay, maybe we might have to have some sort of flag implemented here for that use case, probably.
In the future.
**Jason Plumb** 20:56 Yeah, it's true, and I don't know, you know, given our current state of our API, do we have a way to pass configuration?
Generically, to instrumentations?
**Hanson Ho** 21:09 It should be part of the API, the instrumentation API. If we don't, it ought to be.
But then… then you're talking about, hey, what about instrumentation-specific configuration, and down that road, but…
**Jason Plumb** 21:23 Yeah, so ignoring statics, right, this is the API that we currently are sitting on, and so you… each instrumentation, when you call install, will get a context.
And that context has the app that you're running inside of, the clock.
the… oh, what is this context? I don't know what that is. That's the answer.
**Cesar Munoz** 21:43 context.
**Jason Plumb** 21:44 Which I thought we replaced app with that, but now we have both?
**Cesar Munoz** 21:50 No, the app, it's,
it's a method that casts the context. So the context is the only field that you have to provide there, if I remember correctly.
**Hanson Ho** 22:02 So it's a convenience method, then, basically, for access.
**Jason Plumb** 22:05 Got it, got it, got it. Okay, yeah, okay. And then we have the OpenTelemetry instance, and then we have the session provider, so really…
Unless there are configuration APIs that we're not yet using in context or app.
Then there's not a great way currently to pass configuration, whatever that looks like, right?
**Cesar Munoz** 22:25 There… there is a way you can configure a specific instrumentation implementation.
via its own, methods. But it's not… it's not something…
you know, generic for all instrumentations. It's like, each implementation will expose some methods.
**Hanson Ho** 22:43 Well, what we're talking here is basically an app-specific thing, concept, being passed down to the instrumentation.
So, I think a new concept on instrumentation context that is specifically tied to, you know, this, this, not, sorry, not app, but, SDK, specifically this SDK is, is perfectly fine.
it's probably something we want to genericize into, like, a whole Asian API for instrumentation, but that's… that's…
that's the next step, so I don't think we need to,
use any of the instrumentation-specific level of configuration. It's just, just, hey, the app says do this, you know, then do this. But we don't have to actually get there until we have enough stable.
attributes, to actually differentiate between the two. But when we do, you know, we can certainly add that, I think.
**Cesar Munoz** 23:38 Yeah, I think it makes sense. Now that we're talking about this topic, I just wanted to…
Add a quick reminder that… I'm actually gonna add the link here.
I created these… Issue… As a proposal for some enhancements to the.
**Jason Plumb** 23:59 Yeah, yeah, yeah, yeah.
**Cesar Munoz** 24:00 this instrumentation API, because right now we're doing some
A bit of an ugly workaround to make it all work, and ideally, what's proposed here should help with, you know, not having to do that.
I'm not married to any of the proposals here, so if you have a better idea…
please let me know there. I know that, Jamie already added some comments, and
You also created a PR with some enhancements, so thanks for that, Jamie.
But, you know… Regarding everything else.
If you have any, any ideas, please let me know. Otherwise… You know.
I might think that, you know.
you love the two approaches that I… that I'm proposing here, so…
I can go with either, so…
Just… just so you know,
Yeah, I think it's important to address these workarounds before marking it stable.
**Hanson Ho** 25:08 I'll comment today, like I said, the last 2-3 weeks, that I'll comment. It's one of the… one of the tabs in that window. I just have to make my way… way there, and now I've opened a new window.
**Cesar Munoz** 25:19 That's… thank you.
**Hanson Ho** 25:20 I've also had…
**Cesar Munoz** 25:22 Pretty busy week, so… yeah, I understand.
Yeah, that was it.
**Jason Plumb** 25:33 Great.
**Hanson Ho** 25:35 So, David, on chat had a question about, how deprecation of span events affect, some of our instrumentation, specifically the fragment instrumentation, and I think that that's part and parcel with
If we want to stabilize instrumentation, we should make sure that the data modeling we use is acceptable.
I feel, I feel like it, you know, this is one of those things that's gonna be another interesting thing when span events are gotten rid of, how much more,
fragmented, no pun intended. The data could be, so, I think…
if we want to take a look at, you know, not just this, but frankly, the activity one probably suffers the same issue.
Whether or not those timestamps should be attributes, or… or… or, hotel events, which are logs.
it may be… it may be a good time to… to discuss that. Not right now, but, like, certainly when we get to… when we get to stabilization of instrumentation.
**Jason Plumb** 26:45 It's definitely fair game to discuss this, yeah, so…
I think, probably because I had this on screen, people were thinking about it, and David, thanks for raising that. I think…
Yeah, this is, you know, the clock is ticking on this one. We still have the Span Events API. I don't think that will go away. There was a decision, like, oh god, more than, like, a year ago, about how to handle this, because,
The API wants to stay around.
And I think the idea was to provide
a mechanism for bridging, meaning if you call span.addEvent, it would automatically create
an actual OpenTelemetry event that then has span context. So I think that was the… the idea. I don't know if that's been implemented or what the default is, because they haven't kept up with it, but, it's definitely worth…
Talking about.
**Hanson Ho** 27:40 Yeah, the… I mean.
that's, I think, perfectly doable from an implementation's perspective, you know, basically just modify the tracer, to effectively take, some sort of log or auto-initialize, and then do the right thing under the hood. The problem is that
Each timestamp generating an event means we, like, for that fragment, we have a span that could potentially, create, does it create child spans,
Maybe it does, but it creates, like, you know, 10, 12 events, which.
**Jason Plumb** 28:15 Which is what it… which is what it could do today. They're just span events and not OTEL events. There's really not…
Or there shouldn't be a huge distinction between those.
**Hanson Ho** 28:24 Right. The problem is that… how many of those actually make it back to the server side? And if the collector… and if it's… some of them are delayed, will the collector, like, discard it because it's not coming in the same, you know, window? Oh, yeah. There's the old mobile, hey, the data comes in different chunks, it's difficult to handle.
And, and frankly.
do we even care about a lot of these timestamps if it… if it has to be, like, modeled as a separate telemetry and separate log? So…
It's a good discussion.
**Jason Plumb** 28:58 Yeah, I think for this project particularly, though, it's not a good look to have documented telemetry that's still using span events, and we should… we really do need to migrate away from this.
**Hanson Ho** 29:09 Yeah, I feel like attributes is the easiest way, to go.
**Jason Plumb** 29:18 But then you lose timestamp… or you mean, make these all timestamp attributes?
**Hanson Ho** 29:22 Exactly.
**Jason Plumb** 29:25 You can bikes show that sometimes.
**Hanson Ho** 29:26 It's basically the same problem Servi has.
**Jason Plumb** 29:30 Yeah, totally.
**Hanson Ho** 29:31 the events.
**Jason Plumb** 29:32 I think it is, yeah.
**Cesar Munoz** 29:39 Of… If you don't mind, I'll create an issue, at least, so that we don't…
**Hanson Ho** 29:45 Yeah.
**Cesar Munoz** 29:46 lose track of it.
**Hanson Ho** 29:47 Do we have, like, an instrumentation stabilization, like, issue or milestone or something like that, where we can, like, basically dump all these things there?
**Jason Plumb** 29:56 Like a milestone for instrumentation stability, or for what?
**Hanson Ho** 30:00 For… either for stability or for instrumentation stability, like…
like, these are basically things about existing code that we have to refactor in order to be stable.
**Jason Plumb** 30:11 No. No, and we should probably…
Have a milestone that tracks that.
**Hanson Ho** 30:20 Is Milestone good for this?
**Jason Plumb** 30:23 We could also have a project, you know, that's also a thing.
**Hanson Ho** 30:26 Or a tag? Like, I don't know what the best way of…
**Jason Plumb** 30:38 I personally like the milestones,
in this, like, in this current state, they're numbered, they certainly don't have to correspond with release milestones. These could just be kind of conceptual grouping milestones that you can put issues into. But labels would also, if we can come up with a reasonable label that
encapsulates this concept, then I think it's great.
Yeah, we… I think it's… I think it's good to do that, but, like, what name would you give to this, Hanson?
**Hanson Ho** 31:12 Either, like, in an overall heading, like instrumentation stability, or simply, like, you know, semantic…
consistency, or… I suck with names.
**Jason Plumb** 31:29 No, I'm not awake yet either. This is West Coast, okay?
**Hanson Ho** 31:34 What's… what's the one on Kotlin that we have about, like, specs… spec…
**Jamie Lynch** 31:41 spec compliance.
**Hanson Ho** 31:43 Spec compliance, yeah.
**Jason Plumb** 31:44 Well, that's a label, right?
**Hanson Ho** 31:45 Yeah, it's a label.
**Jason Plumb** 31:46 Yeah, yeah.
this one.
**Hanson Ho** 31:54 Yeah, it'd be, like, model compliance or something like that.
Yeah, sure, why not?
**Jason Plumb** 32:06 Yeah, okay.
**Hanson Ho** 32:09 Pick one. Compliance.
Although that makes it sound like it's, like, SOC 2 or whatever.
**Jason Plumb** 32:14 I mean, I also think, like, I like the word stability in here, but it's, like, stability goals, but that might be too generic.
So maybe there's, like, one for, like, instrumentation… API stability.
And then we keep, like, new ones for each of these other ones. Like, I don't know, we're talking about fragments here, so…
You know, maybe we… that one's probably too small, though. Yeah, I don't know.
**Hanson Ho** 32:44 So, it's really… you can probably group it along with, like, like, attributes using the stable semantic convention attributes, as well as the right, like.
modeling, kind of, atom, which span events are not now.
So you can either have their own thing, which is, like, you know, use the appropriate, thing, and not span events, or just group that into, like, in order for us to have a stable instrumentation, you know, that stuff, there's, like, a checklist of things that has to happen, that being one of them.
**Jason Plumb** 33:22 Yeah, and I think that's why I like milestones in general, is because
you can see the list of things that then burn down. I mean, these are maybe all bad examples, because we…
**Hanson Ho** 33:32 like, this just should be closed, but… Yep. Like, you can see the list here, and you know that, like, when it burns down, and then it kind of closes and goes away, right?
**Jason Plumb** 33:40 Which is kinda nice.
And so you don't really have that… I don't know, I like the grouping, the orderly grouping of, I think, milestones.
**Hanson Ho** 33:49 Yeah, milestones are more a category, so an issue will have to, you know, fall into one of them. I don't think you can have more than one milestone, right? You have to belong to one issue, or sorry, one milestone, versus, I think, the tags or, or, you know… Labels, yeah. Lists are labels, you can label anything, anything.
So, I'm honestly okay with either, as long as it's tracked.
**Jason Plumb** 34:10 Yeah.
Cool.
**Hanson Ho** 34:18 To Santosh?
**Jason Plumb** 34:20 Yeah, Santosh, she's back.
**Santosh** 34:23 Long time no see! Yeah, yeah, I… and bear with me, my questions are, may not be entirely Android-specific, or could be very basic, so I don't work on, these instrumentations,
**Jason Plumb** 34:37 Is it related to Service PRs?
**Santosh** 34:42 Let's see, I just… I'm curious about this event signal. Does the Android instrumentation emit events today? I believe it does, right?
**Jason Plumb** 34:51 It does, yeah.
**Santosh** 34:53 Okay. The… Nope.
**Jason Plumb** 34:54 Sorry, just to show you where that is, too, and for anybody watching the recording, it's on the OpenTelemetry ROM.
interface… There is a method, or several methods, called.
**Santosh** 35:07 Emmett event, okay.
**Jason Plumb** 35:08 event.
**Santosh** 35:09 Okay. What about logs? Do you also emit, application logs?
**Jason Plumb** 35:14 No, but you can… you can emit them through the OpenTelemetry instance. So, through the OpenTelemetry instance, you can get a log provider, I think is the class name, and then from the log provider, you can emit log records.
**Santosh** 35:25 Okay, and then is the exporter a common exporter, or you will have to… Be careful.
**Jason Plumb** 35:30 It is.
**Santosh** 35:31 Set up.
**Jason Plumb** 35:32 Is that the same exporter for both.
**Santosh** 35:34 Hmm…
**Hanson Ho** 35:35 EmitEvent is basically syntactic Sugar to basically call the logger and set the event name, and set the body to whatever this is, so it…
Yeah, it's the same thing.
**Santosh** 35:47 I think my, in that case, then my…
Question is kind of valid then, because typically, when we… Want to…
set up the backend pipelines for these two logs and events, you know, they are separate. You know, the application logs go to a…
a different… they are… they are processed, you know, and viewed through a different interface. The events…
are typically, you know, in a different location, in a different data store, and processed and analyzed differently.
So…
in a default setup, do you have only one exporter where both of them are sent to the same location, or are logs are turned off by default anyway, so it's not a concern.
**Hanson Ho** 36:38 So, I don't think we have any underlying application logs that we fire through the bridge. I think when all the logs that we create are… are very OTEL-y, and they probably should all be events, if they have them properly defined. Like, so I don't think we're, like, bridging LogCat over. I think…
somebody might have added that somewhere. I can't honestly imagine anybody would want that in their telemetry. So,
the concept of log we expose, basically, as an API.
for… for others, for, like, apps that use the SDK to create them, and I think some of our instrumentation create them as well. But… but they… but they… I believe they go through the same pipeline, as events, except they just… just don't have an event name.
**Cesar Munoz** 37:29 Yeah. Okay. Yeah, true. By the way, we do have…
Just for completeness, we do have an instrumentation that Sense, look at logs.
**Hanson Ho** 37:40 Off by default.
**Cesar Munoz** 37:41 But… It's off, by default, yeah. It's opting, but…
But yeah, it's, I mean, we treat logs and events as a single thing, so it's all the same pipeline.
**Santosh** 37:54 Okay, okay. And I, I believe, the event suspect
doesn't explicitly talk about a separate exporter, right? Because it's, only the API is different.
And so, even if we consider, you know, the server-side Java applications, or server-side apps.
there, if… if at all. I think I'm…
I briefly saw somewhere that the exceptions are now being modeled as events instead of, you know, span events.
In that case.
**Jason Plumb** 38:28 In this spec, right?
**Santosh** 38:30 Y-yeah.
**Jason Plumb** 38:31 Yeah.
**Santosh** 38:31 Yeah, in that case,
You will have to be, like, whoever, is setting things up, you know, they'll have to be careful if…
If they don't want the exceptions and the general logs to end up in the same location, they have to
Configure the exporters carefully.
**Jason Plumb** 38:50 Yeah, and I would say… I would say that's true of any telemetry signal. If you need them to be partitioned or exported
differently depending on some internal criteria, one of which could be, does it have an event name, does it not have an event name? If you need to route or send those to different locations based on the internal characteristics of that telemetry, then that is…
That is something that you would need to pay attention to. It's not something that we make easy or encourage out of the box. We expect… most users, we expect to either use a collector somewhere else, or to have a backend that's smart enough to do that… that routing.
**Santosh** 39:27 I see.
I see. Okay, so collector can be used to…
Detect that, hey, these log records are events, and then for, you know, send them to a different destination.
**Jason Plumb** 39:38 Yeah, I mean, that's what the collector's really good at, right? It's, like, setting up pipelines that know how to do different things with telemetry.
**Santosh** 39:44 Okay, okay.
**Jason Plumb** 39:45 Okay.
**Santosh** 39:46 then…
**Jason Plumb** 39:46 I have this up because I think it shows how you might be able to accomplish this. Like, it's not… it's not easy, but I think there… I think that you can leverage the Rum Builder.
And I think that you can set up your own…
You could set up your own log record exporter customizer that has an exporter that is, like,
Event Aware. So, you could set up your own exporter that is aware of events and delegates to one or the other.
But you would need to… you would need to set this up. It's, like, not a small amount of lifting, right? It's, like.
**Santosh** 40:20 Right.
**Jason Plumb** 40:20 It's a page of code.
**Hanson Ho** 40:22 Like, on-the-wire, events and logs are effectively the same thing, so on the client, we treat them the same way, so that we batch them the same way, you know, we don't… we don't.
**Jason Plumb** 40:30 Right.
**Hanson Ho** 40:30 differentiate the two. You can potentially set up two pipelines and two batches, but then you might be doing some duplication. If you're going to send it to the same destination, like, server anyway, then, you know, unpacking it on server size is probably more efficient. But if you do want to, you know, send your application logs, you know.
To, to some… somewhere that's, you know, that basically dumps it out, and…
do that filtering. It's all configurable on the client side. It's just in the exporter. When you get it, you just say, hey, where does this go?
Send it there.
And the good part is you're saying the logs are off by default.
**Santosh** 41:10 It's only the events.
**Hanson Ho** 41:11 the application… so the bridge log cat stuff is off by default, and we… so we… so we basically… and if you turn it on, we just treat it like a regular hotel log anyway.
Mike, there's no differentiation in the export layer, how we treat events and logs. They are log records, and we treat them as log records.
**Santosh** 41:33 Okay.
**Jason Plumb** 41:33 Yeah, so I think Hanson's touching on this specific instrumentation, right? We have…
We have built-in instrumentation that's not turned on by default.
Around the Android login code.
**Santosh** 41:45 Okay.
**Jason Plumb** 41:46 So an application… if an application wants to send its logs to a backend, like, in OpenTelemetry format, then it would need to either opt into using this bridge…
and then rely on just the Android logging facilities, or they can use the OpenTelemetry APIs.
Right, so they could get the OpenTelemetry instance and manually call their own logging functions, but we don't provide a direct logging API.
In Android. But the… the underlying APIs, OpenTelemetry APIs, do.
If they want to write a bridge for timber, or, you know, whatever favorite logging library is… Open an issue or a PR.
**Hanson Ho** 42:28 It's pretty easy.
**Santosh** 42:31 But whatever API you use, they would eventually come back and use the same SDK experience.
**Jason Plumb** 42:38 They would. Yeah, yeah, they would use the same exporter, yeah. Yeah, yeah. Yep.
**Santosh** 42:43 Okay, so, so, so very good. So I think on the server side, the collector is to be, you know, made use of to, you know, fork off the destination.
And on the client side, it's not an issue, right? Because… at least in the default setup.
From what I see.
**Hanson Ho** 43:02 At one point, they talked about separate pipelines for, like, events for processors and exporters, but I think, you know, at the end of the day, they just collapsed everything and basically said, go through the same thing, and have some differentiation in your processor and your exporter if you want to treat events differently.
**Jason Plumb** 43:18 There were some of us who… there were some of us who felt strongly about that, and we did not die on that hill, fighting that battle.
**Hanson Ho** 43:23 I think the API should be different, but internally, I don't give a shit.
**Santosh** 43:29 Yeah, I think that exception moving to an event is more disruptive, in my opinion, because people have been sending something as spans, and suddenly…
You know, they will now have to set up a receiver on their backends to accept events.
**Jason Plumb** 43:48 Do you… do you have a… do you have a PR for that? Do you know what it is?
Cause I think I agree with you.
Yeah, the third one, yeah. This one.
**Santosh** 44:04 No, I know.
**Hanson Ho** 44:05 It's optional, so…
**Santosh** 44:07 No, no, it's not this.
**Jason Plumb** 44:08 Okay.
**Santosh** 44:17 Or maybe… yeah, yeah, yeah, the… is that… oh, it's an OTEP, the Recording Exceptional Log Records. You know, it's there. If you scroll down.
Recording, except… yeah.
Okay.
**Jason Plumb** 44:29 Just not seeing it.
**Santosh** 44:30 Yeah, yeah, yeah. Search for recording exceptions as log records.
There's just two items above. Yeah, correct.
**Jason Plumb** 44:40 Okay.
**Santosh** 44:41 It's closed.
**Hanson Ho** 44:43 Stale. 270, oh my god.
**Jason Plumb** 44:46 Yeah, look at this combo. Yeah, look at when it was opened!
Yeah, so there's been a lot of traction on this.
But how did it ultimately end up, right? That's what I want to know.
**Santosh** 45:00 So this is not happening, then, then… oh.
**Jason Plumb** 45:04 So, there's this.
**Santosh** 45:05 Yeah, so that's what I thought. I saw it recently somewhere, so maybe she opened a new issue. Let's see.
**Jason Plumb** 45:11 Yeah, it looks like this kind of went stale, or got.
**Santosh** 45:13 Yeah, yeah.
**Jason Plumb** 45:14 encumbered, and so maybe there was probably some conversations that…
And here's this one as well. Okay, so let's follow these, right? So this first one is what we saw before. Add an optional exception parameter to the emit log record. So that's in the API, right? That's gonna say, when you call emit on log record, it can now take an optional exception.
Somewhere in here.
**Santosh** 45:37 Okay, so this is… this is in addition to, you know, logging exceptions in the span event.
Like, you…
**Cesar Munoz** 45:46 I think this is… no, but I think this is only for logs.
for Deluxe API.
**Santosh** 45:50 Yeah, yeah, but let's say an application detects an exception.
**Jason Plumb** 45:54 Yeah.
**Santosh** 45:54 Then… Let's say it's in response to a… A network request, then.
it… Puts that exception in… in a span event.
But in addition, you also have an option
To put that in a log record, too.
**Jason Plumb** 46:13 So if it's user code, we would discourage them from using span events, because span events are deprecated.
In favor of using events.
And when you emit, if you need an event.
to contain this exception, then you could use that mechanism for doing that. We don't have a first-class API yet in Android that…
That creates an event with an exception.
But it looks like, based on this PR that's on screen, that we should be leaning toward that, right?
But this is specifically for logs, and not events. This is also why I wanted events to be a first-class API, so that we can talk about them as different things. Yeah.
**Santosh** 46:51 Even if they ride on the same signal, I know it's so frustrating, but okay, I'm not gonna revisit that, I promise.
**Jason Plumb** 46:58 This is specifically around logs, so if you need to log the fact that an exception happened, this is your go-to. If you want to generate an event that indicates that an exception happened, then you can do that, and that event will have some kind of name.
And it will then also have this exception.
Does that make sense?
So here's this.
Still in.
**Santosh** 47:24 Yeah, yeah, I think the…
**Jason Plumb** 47:26 But this sounds like what she's working toward.
**Santosh** 47:28 Hmm.
**Jason Plumb** 47:34 And I think, is the Log6 still meeting? Like, is that special interest group still…
**Santosh** 47:39 I think so. I see it on the calendar. I plan to… Join it sometime.
**Jason Plumb** 47:45 Cool, yeah, I haven't joined in quite a while, but getting clarity around that would be good. Cesar.
**Cesar Munoz** 47:50 Just wanted to say… I don't know if you… Where…
you know, earlier when Jason mentioned something that
Apparently, the, existing API to send spanned events Might be changed.
in the future, to… serves as a bridge to, instead of, you know, creating the same span event that it's doing now, it's going to create a log event.
So… I guess, in that sense, product users Who are currently sending
error events, they might not have to change their code. It's now that the outcome will be a log event.
That will reach the backend.
That's my understanding.
**Hanson Ho** 48:41 Yeah, this was, I think, what we were talking about before, 2023.
**Jason Plumb** 48:45 I know.
**Hanson Ho** 48:46 I think this is the one where it's a shim API where you actually call add span event, on a span, and it'll create a log with that span as the context. So the implementation… what will be emitted will be a log, but the API doesn't change.
I believe that's still what… It is meant to happen.
That the thing going away is the actual span event.
thing in the OTLP, but the API remains, because you still want to create an event associated with the span.
So if people are using that, then, you know, they're good to go. Or at least they're at the mercy of the implementation.
**Jason Plumb** 49:33 Yeah, and this is… I think this is the one that deprecates it.
Yeah.
So this is the kind of umbrella… umbrella deprecation.
**Hanson Ho** 49:46 I think I started following this initially, and then I had to give up, because it was just going back and forth and back and forth, and…
**Jason Plumb** 49:54 Yeah, I have also been keeping it a little bit at arm's distance after I stopped going to the logging sig, because it's like, consumers, users, like, I feel like we're layered on top of this stuff, and so we can kind of wait for the dust to settle, and that's where I'm at, is like, I'm not…
I guess maybe I am opinionated, but you have to pick and choose your battles, and so…
**Santosh** 50:14 Yeah, I was thinking from a user perspective, too, like, if I'm looking at a trace, you know, in any product's trace visualization, you know, you would expect, you know, a related exception to be seen there, but then, you know, pulling it from a logs
Backend, you know, would be…
You know, totally extra work.
**Jason Plumb** 50:37 Yeah, the correlate… yeah, it's expected that the back end that needs to display those two things on the same pane of glass can do the correlation.
**Santosh** 50:44 Hmm.
**Jason Plumb** 50:46 Yeah.
**Hanson Ho** 50:47 There should be an ID, span ID associated with the log event, so in theory, if the data applies in time, it should all be…
shown, you know, hey, this is related to this, so it shows, you know, these are linked in terms of data. So if the tooling doesn't show it, it's actually probably the tooling needs to be updated to know the relationship and have things pooled together.
But, you know, that's the whole ecosystem.
Yeah, totally. If you're looking at a given trace.
**Jason Plumb** 51:18 in any product, you have a trace ID. You're looking at a single trace ID, and that is a key that you should be able to pull all the logs for that have context.
Anyway…
**Santosh** 51:31 Okay, alright, yeah.
**Jason Plumb** 51:32 We have a few minutes.
**Santosh** 51:32 So I have a few more topics, but I'll come back, you know, next time.
**Jason Plumb** 51:36 Yeah, Santosh, welcome, yeah, it's good to have you. It's been a while.
I wanted to bring up one, stupid thing that I was chasing a little bit, and I'm wondering if anybody has any other insight on this.
It's this, serialization thing.
Where is it?
**Cesar Munoz** 51:59 Is it a PR or a niche?
**Jason Plumb** 52:01 I think it's an issue, and it's a bug. It's this one, yeah.
So I know that Jamie and I were looking at this. This person gave this kind of strange JSON format, but they're like, look.
Look at how bad this is, and look at how bad this is.
And we've gone back and forth, and I, you know, I thought I repro'd it, but all I did was, like, repo the problem with the timestamps, but…
And they're able… where were they seeing this? Was that… were they seeing that JSON in a collector or something?
**Hanson Ho** 52:38 Is it a compression issue? Is there a double compress… actually, no, it can't be, it's just one.
specific value.
**Jason Plumb** 52:49 Jamie, have you attempted to reproduce this?
**Jamie Lynch** 52:53 I haven't, no.
**Jason Plumb** 52:54 Okay, okay.
**Jamie Lynch** 52:55 It definitely looks like something's…
going wrong in a decent civilization somewhere. It does. But I'm not sure where in the system it's gonna be, whether it's an SDK or collector issue.
**Jason Plumb** 53:09 Yeah. Well, also…
**Cesar Munoz** 53:11 Wasn't that the issue that you fixed, Jason?
**Jason Plumb** 53:14 You know what?
**Cesar Munoz** 53:15 VR?
**Jason Plumb** 53:15 No, I think… I think I fixed a different thing.
So, I was looking at the timestamps, which are not even doubles. This person's problem is about doubles.
**Hanson Ho** 53:29 Why would timestamps be a dub?
**Jason Plumb** 53:32 I think those are two diff… they're not. I think there's two different things happening here, so that's probably on me for adding confusion. I didn't actually reproduce this, I just was able to see, oh, the timestamps are screwy, which is a different problem, so that's… sorry for that confusion.
Yeah, I want to look at this again and see if I can see doubles, but when I looked at my collector output, for example, like, their original thing said when they get jank events, they see… so there's two things here. They're, like, bad timestamp.
So that's what I initially started looking at. I was like, oh, I also got a bad timestamp.
But I think it's a different issue, because then they bring in the fact that, like, doubles look weird, right? They're like…
I think, like here, every time I send a double, it's getting serialized strangely, so that…
it's not a timestamp, because a timestamp is a long and not a double, right? So that's…
The first kind of confusing bit.
But then this double field, long field, I… I don't know if any of these are doubles. I think they're… I think none of these… oh, this one is. Like, so, that looked fine to me, right? Like, their threshold up here was screwy.
Right, like this, whatever that is.
But I also don't know what's rendering this JSON. It could just be the thing that's printing out this JSON doesn't know how to… what to do with a double.
**Hanson Ho** 54:51 Do they have, like, an exporter, just the outputs, to… to text, and, like, there's, like, an encoding issue?
**Jason Plumb** 54:58 Yeah, so given these numeric prefixes, I suspect that this is protobuf being swizzled over to JSON.
But I don't… I don't know.
Okay, well, it sounds like no one else has the insight on this, it's fine, I'll keep chasing it, but…
I really don't want us to have a problem serializing doubles, and I don't think we do. I mean, this is what my collector says the double looks like. That looks pretty good to me.
The thing that did not look good was this, and that's been fixed, so…
**Hanson Ho** 55:32 There could be something with the instrumentation that's, like, the data gets back before it casts, maybe, you know, we're not… we're not looking at, you know, maybe it could be, like, a…
weird code path that casts implicitly to a double. I… It would be the instrumentation.
**Cesar Munoz** 55:51 I think it's really… it's probably mostly what this person used to… serializes as a JSON.
**Jason Plumb** 55:59 That's… that's kind of what I smell as well, but I don't… they haven't been clear about what they're using. Well, they… I asked, and they said… what did they say? I'm like, how did you do that? And they said…
It's the SDK doing it. I'm like, no, it's not. What is this?
Capturing the HTTP requests JSON body. So, I mean, we're not sending a JSON, so that's weird.
Yeah, maybe I'll just… I'll circle back on that point, because… Anyway… Great. Okay, cool.
I think we did it.
Cesar.
**Cesar Munoz** 56:35 In the… in the last 3 minutes, probably…
I think it's fine to say that the… Plans for Jamie?
**Jason Plumb** 56:44 Yeah, I think so, yeah.
**Cesar Munoz** 56:46 Yeah, I mean, it's already… we all agree, so…
**Jason Plumb** 56:49 Yeah, and I will get to that today.
But yeah, Jamie is being promoted to maintainer of OpenTelemetry Android.
**Hanson Ho** 56:55 Nice!
**Jamie Lynch** 56:58 That's cool.
**Cesar Munoz** 56:59 Yeah.
**Hanson Ho** 56:59 You've got 2 now, from 0 to 2!
**Cesar Munoz** 57:05 Yeah, that's pretty much it, so…
**Jason Plumb** 57:07 Yeah, no, I think your help has been tremendous on this project, and greatly appreciated, definitely well deserved. So, thanks.
**Cesar Munoz** 57:15 Yeah, thank you.
**Jamie Lynch** 57:16 Duke.
**Jason Plumb** 57:17 And we will get that permission stuff set up today.
**Jamie Lynch** 57:21 Awesome.
**Jason Plumb** 57:22 Cool.
Well, thanks, everyone.
Let's do it again in a week.
We'll look for the release
Monday, and Cesar, reach out if you need help or an assist on any of that release stuff.
**Hanson Ho** 57:33 You have two people in European time zones to give you approvals, so…
**Jason Plumb** 57:37 True. Yeah, that's great.
Alright, see everyone.
**Cesar Munoz** 57:42 Thanks, bye.
**Jason Plumb** 57:43 Bye.
