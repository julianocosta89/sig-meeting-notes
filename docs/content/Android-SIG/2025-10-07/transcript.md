SIG: Android SIG
Date: 2025-10-07
Duration: 42 minutes
Zoom Recording URL: https://zoom.us/rec/share/HAXXKNTnpI0FfBbjsxVO3tRgxuD3xpx-BfFY3OGtJ6kiLM-lXM5_Y-k3PdvjAmI_.aL5pWyosfsbQbaF6
============================================================

## Zoom Recording Transcript

**Hanson Ho** 00:53 Hello? Wha!
**Mustafa Haddara** 00:55 Hello.
**Hanson Ho** 00:58 Let's see if Jason's coming or not… We didn't say he wasn't.
Oh, boy.
one minute, and I guess I could share the doc if, if he's not there.
Caesar… Hey, Cesar.
**Cesar Munoz** 01:31 Hello, good morning.
And good afternoon.
**Hanson Ho** 01:34 good.
Almost evening for you. It's just afternoon, I guess.
Is Spain… is Spain the same as the UK, or is it one hour offset?
**Cesar Munoz** 01:45 I think it's one hour… ahead, I think.
**Hanson Ho** 01:50 Okay.
**Jamie Lynch** 01:51 Yeah, I think so.
**Hanson Ho** 01:57 Hey, Jason.
**Jason Plumb** 02:01 Hey, sorry, I'm still getting set up here.
**Hanson Ho** 02:03 No worries.
**Cesar Munoz** 02:06 It's no rush.
**Jason Plumb** 02:07 Remember when meetings used to be at, like, 2PM, or, like… 4PM, or… 11 a.m, you know, like, literally any other time.
**Mustafa Haddara** 02:20 I don't know what you're talking about, it's 11 AM here.
**Jason Plumb** 02:22 See!
**Hanson Ho** 02:26 Or 7AM! Those are fun! Those are fun!
**Jason Plumb** 02:31 Yeah, few and far between, luckily for me. It's, like, almost not doable. Like, I'm already barely conscious at 8, so… Whew! Okay, there's a… There's a document that goes with this, okay, almost there.
**Hanson Ho** 02:47 Or rather, I had 7AM meetings at the office.
**Jason Plumb** 02:50 Oh, man.
**Hanson Ho** 02:51 Really? Yeah. Oh yeah, because we had to talk to people, like, in India, and then China, and also in Europe at the same time, so…
**Jason Plumb** 02:59 That's right.
**Hanson Ho** 03:01 Especially in your 20s! Well, I mean, yes and no. In your 20s, you all stay up late, but your body also is, like, able to do whatever, so…
**Jason Plumb** 03:08 Yeah.
Alright, there's a thing.
Okay… Thank you for whoever got this started.
Light agenda compared to last time.
**Cesar Munoz** 03:26 quite lighter.
**Jason Plumb** 03:40 Yeah, we've been busy, like, I feel like we've merged a lot of pull requests in the last week, but they just keep coming. It's great.
**Hanson Ho** 03:47 Holy crap, last week was… yeah, that's 8 topics, or 6 topics? 7 topics?
**Jason Plumb** 03:52 Oh yeah, it was very active last week, Hanson.
But mostly I was just, like, front-loading stuff and thinking about, you know, stable.
**Hanson Ho** 04:01 And you probably saw the blog post. I did.
Excellent.
**Jason Plumb** 04:06 So we're on… we're on the road. I don't know if that issue has gained any new comments. I haven't seen any, or I didn't get notified yesterday about any. Looks like there are.
Yeah, so I think… I think I left off here, so that, yeah, it's just like… It's us, it's still us, but, you know, at least we're inviting people to comment on this.
Since the agenda's light, and maybe not everybody saw this, I also want to… How do I find it? Let's see… From this issue, I think I can get there. I just want to point out that we changed some stuff in the registry.
So… Let's see if I can find it… this thing.
So, we've talked about this in the past, I think everyone on the call is probably aware of this, donation.
By Embrace for Kotlin multiplatform, like, pure Kotlin API and SDK implementation.
And I was like, hey, there is already something in the registry.
that if you go here and pull down Kotlin.
There was, until last week, a different project, that was basically abandonware.
So, I think I pointed out that that existed… Somewhere. Different, different issue.
Yeah, this one.
Somewhere… yeah, sorry. But yeah, this thing… And, yeah, basically abandonware. So we went ahead and got it removed, and the only one that shows up now is the current Embrace multiplatform. So for those that didn't see it, you know, I'll just make a link to it.
And it looks like there was some support, from some people who had… I don't think I've ever joined this call, but I'm expressing interest in helping, so that's great, I saw that.
Alright, what else do people want to talk about?
**Hanson Ho** 06:36 Serbi has, a, I'll square it down the agenda.
**Jason Plumb** 06:43 Okay.
**Hanson Ho** 06:46 Where is it?
Oops.
So, Cesar has a topic.
**Cesar Munoz** 07:11 I've just added it.
but we can go first with the… we wanted to talk about service.
**Hanson Ho** 07:18 Oh, no, we'll talk about yours first.
**Cesar Munoz** 07:19 Son?
**Hanson Ho** 07:19 You put it in at first.
**Cesar Munoz** 07:22 Well, okay, it's probably quick, it's, So, not for… not necessarily something for the first stable release, but I think we should seriously consider publishing a Gradle plugin for… the agent. There will be a bunch of a bunch of… You know, pros of having one.
A couple of them that come to my mind are, one, we could… we could somehow… I mean, by having greater plugins, maybe not the default behavior, but By just having one.
We could allow, like, a one-liner Kind of a installation of the agents in an application where Maybe somebody wants to get… All of the instrumentations, which is something that someone has created a PR for it recently.
And, I think it's something that… it's a cool idea, but it… Doesn't work well unless we provide them all as a plugin, and this is because of the fact that some instrumentations rely on bycode instrumentation.
Which… itself relies on another grade of blogging, which is By Body.
And, you know, there's a lot of setup that might be… needed for everything to work, which is not something that just one dependency, regular dependency, can… can add into a project. So the plugin is, like, more powerful in terms of what… how… how it can Configure a full project.
Also, another benefit that I see From having a plugin is… that somebody… I realized that recently somebody created an issue about the, OKHTTP… This is the first one.
So, for those who might not be aware, so in version 5 of HTTP, they changed the… their coordinates.
Four, and they split it, like, kind of, like, into two… projects, one for Android, one for plain Java. Yeah. And they rely on… cradles, metadata.
To find the right one, depending on where the dependency is added.
Now, this causes problems for projects that don't use Gradle.
So that's why, in the upstream repo, they will just switch to the plain Java.
coordinates.
Now, the thing about that is that… the plain Java.
is not compatible with the Android, kind of, version of OKCDB, So, what I did… And that was, you know, breaking auto laundry. What I did was… So this person added a link to my PR. What I did in that PR to make Auto Android work.
was to do some small griddle config, so that… every OKHTTP Java dependency that it finds, it will replace it by just OKTP, which Which will instead, you know, turn into the Android-specific version of it.
Now, that may hotel angry work.
But what I'm seeing with this issue that was created is that This issue… the same issue that we had here.
It's also happening on the host projects, because, of course, it is. They are still getting the upstream dependencies As transitive dependencies, so… and this brings, you know, the Java version of KHCP. So, it looks like that's what's going on here.
And it's something that we could also address with a greater plugin of our own.
In which we will do these kind of replacements on behalf of our users. Right now, the only answer that… the answer that I'm planning to give this person is that they will have to do the same.
in their project, to configure Gradle to replace the Java version of HTTP by the Android, so… Just wanted to mention that.
**Jason Plumb** 11:57 So, is it the case, then, that this didn't seem to work?
Or is it that they've got two dependencies now? Like, one… like, it's coming in in two different ways. One's coming in from the upstream, and one's coming in from us, and we don't… this doesn't pass the transitive, is what I'm hearing.
**Cesar Munoz** 12:13 Correct.
**Jason Plumb** 12:14 Okay.
**Cesar Munoz** 12:14 Yeah, it's the latter.
**Jason Plumb** 12:17 Yeah, that sucks. Okay.
**Hanson Ho** 12:21 They basically need to do this at their app level, when they pull everything in and resolve dependencies like that. We're just doing this… At our level, which…
**Mustafa Haddara** 12:33 Is it… is it even our job to fix this?
like, I see it being, like, helpful and stuff, but if OKHCCP is gonna introduce two breaking, like, two incompatible versions, one's a Java version, one's an Android version, they're gonna have this problem whether or not they're using our SDK, right?
**Cesar Munoz** 12:58 Yeah, that's a good point.
**Hanson Ho** 13:00 I feel like it's the instrumentation's problem. The instrumentation is assuming that the JVM version should always be used, and we're saying, not for us, we're gonna use the other one. But it's almost like it should be a different dependency, in terms of, OKHTTP Java, OKHVM, OKHTP Android, in terms of the instrumentation. And it's at the instrumentation level that, you know, we should be pulling one versus the other.
**Jason Plumb** 13:25 Really, when you say instrumentation, you mean, like, core SDK exporter?
**Hanson Ho** 13:30 Or the… I thought the dependency was actually in the OKHTP instrumentation, like that package, that one was saying JVM.
**Jason Plumb** 13:40 No.
**Hanson Ho** 13:41 Nope.
**Jason Plumb** 13:42 I don't think so, correct me if I'm wrong, Cesar, but I think…
**Cesar Munoz** 13:46 And I think that's one…
**Hanson Ho** 13:51 Cause… cause I… does the ju… who pulls in the OKC dependency?
I was the instrumentation.
**Cesar Munoz** 14:00 Well, two, yeah.
But also, the exporter… core dependency…
**Hanson Ho** 14:08 What the exporter also does?
**Jason Plumb** 14:10 Yeah.
**Hanson Ho** 14:12 Okay.
**Cesar Munoz** 14:12 That's used by the HTTP exporter.
**Jason Plumb** 14:14 So, our instrumentation for OKHTTP just uses the vanilla. It doesn't specify, right? It depends on the module system to resolve that.
Which is, I think, what we want, but do you remember why the upstream core didn't want to do it this way? It's for non-Gradle projects?
**Cesar Munoz** 14:33 Because it breaks non-Gradle projects.
So, in a way, that's why I kind of understand what Mustafa was mentioning.
And this problem is caused by the, you know, that decision in OKCP.
**Jason Plumb** 14:51 It is, yeah. I mean, it's a good question to be thinking about, So this was merged 2 weeks ago as the most recent.
**Hanson Ho** 15:04 So if… So, if our exporter is saying, OKHTP.
**Jason Plumb** 15:12 Yeah, they're doing this.
**Hanson Ho** 15:14 And that's… Y-yeah, and that's… That's in… our code.
hour as a.
**Cesar Munoz** 15:23 This is upstream.
**Hanson Ho** 15:24 Hotel, yeah.
**Jason Plumb** 15:26 Yeah, this is… this is when… Core is being published, so it's detecting this and replacing it with this.
So that if, like, if you go out there and peek in the palm, I think it's gonna have this.
**Hanson Ho** 15:37 So core is basically saying, our OKHTP is a JVM.
And… but that doesn't work for Android. We need the Android. So we need the resolution to be done a little further down, or we need to, like, override this.
Somehow.
**Jason Plumb** 15:54 Or they let the module system do its thing, and say in the cases where it's non-Gradle, you have to specify explicitly which one.
Right?
**Hanson Ho** 16:02 Yep, that… Yep.
**Jason Plumb** 16:05 Should we… should we think about bringing this up again, then, on Thursday?
Like, on the SIG meeting, I mean, I can bring it up, but…
**Hanson Ho** 16:14 I mean.
**Cesar Munoz** 16:15 They're gonna ask.
then what… what they're… what they'll do about the Maven projects that… are broken.
If they switch this back.
**Jason Plumb** 16:27 They will, and isn't… isn't… isn't my answer then just, that we can document that users need to specify which one?
I mean, it does make it harder to use, I suppose. What if we had, What if there was another artifact that was, like, exporter's OTLP?
Kotlin, or, you know… Android. Yeah, Android, like, what if there was another module in here that all… it exists only to fix this problem?
And then we could depend on…
**Cesar Munoz** 17:00 work.
**Jason Plumb** 17:00 And then we can depend on it, right?
**Hanson Ho** 17:03 Yeah, it feels like… it feels like the issue is… is… is, the… our modules upstream isn't… As specific as it ought to be.
**Jason Plumb** 17:12 Yeah, sure.
**Cesar Munoz** 17:15 That'll work, yeah.
**Jason Plumb** 17:17 I will ask on Thursday…
**Hanson Ho** 17:26 Like, if you use the default.
Java OTLP exporter, it'll pull in the JVM one, and then if we could not use that explicitly, but implicitly, but use, you know… the Android version of that, which is basically the same thing, but, you know, for a different dependency on HTTP.
**Cesar Munoz** 17:45 Yes, in a way, that split that they did in OKHTP is kind of like…
**Jason Plumb** 17:51 I'm propagated.
I think I'm typing Kotlin here, but is it… is it Android? It's… it's Android, right?
**Hanson Ho** 17:57 Yeah.
**Cesar Munoz** 17:57 boundaries, specifically.
**Jason Plumb** 17:58 Okay.
I mean, if it's in the name, then it's very clear to anybody using it, like, which flavor you're getting, I guess.
it just sort of perpetuates what OKHTTP did upstream, like, into our stuff, and fortunately, hopefully, it stops at Android.
Like, you know… We don't have to publish a JVM version of the Android whatevers. Seems silly.
Okay.
**Cesar Munoz** 18:45 Yeah, at least in the auto side, the default will be the JVM version in this case, right?
**Jason Plumb** 18:51 Yeah, so we got a little bit far afield with this. So, Cesar, you were talking about, like, making a plugin, publishing a plugin, which you have some experience with.
**Cesar Munoz** 19:02 Yeah, basically anything that we might want to help. I mean, we will be able to do more on behalf of the users.
if we provided a plugin. Like, in this case, we could… Provide a fix for them, even without, you know.
neither OKSDP nor Hotel Core doing anything about it. Now.
still… it's… it's still, something I guess, we should Like, properly addressed with what you mentioned. This could be an option, but… I guess that's my point, that in order to have a fully, you know.
helpful, you know, one-liner thingy to install Autel Android, it's probably… Gradle plugin is probably the best way.
It doesn't have to be the first release, though.
**Jason Plumb** 20:01 And it sounds like Android developers are pretty comfortable with this approach about using plugins. I mean, AGP is, like, the penultimate Android plugin, so, like, it's just part of… it's part of the workflow anyway, so, yeah, okay.
**Cesar Munoz** 20:16 Yeah, it's quite common.
**Jamie Lynch** 20:19 Yeah, I think it would be a pretty good idea, Yeah, because then we could kind of, like, do build time by good instrumentation to install stuff.
I guess in future, it might also make sense to upload mapping files.
If we can kind of come up with some sort of convention for… What that should look like.
**Jason Plumb** 20:43 Oh, interesting.
**Hanson Ho** 20:46 There's also… we could also take, the file configuration approach, basically, because if we're doing… if file configuration is a bigger thing, we could actually, you know, get the configuration like that and configure at the Gradle plugin level, you know, what features are enabled and not.
So we don't have to have, like, you know, code that basically interprets Yeah, we use one at Embrace, and we do a ton of stuff in it, and it's quite nice. It's not… it's not not complex, we'll say that, but it's good, powerful.
**Jason Plumb** 21:19 of this, I mean, that's the whole thing, I think, right? It's like, Gradle is very complicated, and getting it right It's often complicated.
**Hanson Ho** 21:28 It's so easy to fuck up, it's very easy to blow up configuration caches and all that stuff, so, it has to be used with care, and with the appropriate testing to make sure that, you know, things don't fuck up unintentionally.
**Jason Plumb** 21:45 The thing that's maybe the most consistently infuriating thing about Gradle for me is every… like, I'm using it and I make a change, like, I add in a bunch of code, and it's effectively a no-op. There's no warnings, there's no build failure, it's just like… just, like, didn't… didn't run, or I had it at the wrong phase, you know? There's, like, it's very… it's very modal, like… configuration phase versus whatever, now there's, like, the whole caching phase. Anyway… I, I just, like, I write… I put in a bunch of Gradle code, and it does nothing. And then I change it, and it still does nothing.
It's like… just give me something, give me some sign that it, like, is even recognized. Like, I'm, like, restarting the demons, because I'm like, maybe they have a cached copy of my build scripts, like, I don't trust them now, and so it's defeating the whole, whatever, that's it. This is partially me.
**Cesar Munoz** 22:40 No, but it's a fair point. Actually, also… They change quite often, or at least they have done so.
like, their APIs, so… Yeah, yeah. So you also kind of have, like, sometimes multiple ways to do the same thing, and that's also… but, you know, not all of them are the recommended ones, so that can also be confusing at times.
I heard that Gradle is kind of like the… the peril of…
**Jason Plumb** 23:08 today's work.
Well, I'd love to write some more Pearl. I'm looking for a reason. It's been years.
Okay.
Alright, so I took this as an action item. Can we think of any other cons here? Like, I mean, I just said it's like, you know, another module to maintain is complicated.
I don't really know of any other cons.
Those are… those are… Pretty sizable ones already.
Okay.
Let's leave it at that.
Semkov.
Yes.
Yeah.
**Hanson Ho** 23:53 So there is basically a bunch of discussion about how to actually encode this information, so there was talk of attributes, there was talk of events, I specifically proposed span events.
Particularly because, having things on the span itself is great, so you don't have to wait for, like, some other object that may or may not arrive to actually get the information.
**Jason Plumb** 24:20 Unfortunately, you know you've lost that battle, right?
**Hanson Ho** 24:23 Well, I mean, the API for span events are not there, but…
**Jason Plumb** 24:26 It's true.
**Hanson Ho** 24:27 But Serbia's…
**Jason Plumb** 24:28 I mean, the API is there, but, like, the underlying data model will at some point change.
**Hanson Ho** 24:33 But I thought the underlying data model is to have span events.
**Jason Plumb** 24:37 No, it's the other way around it. It's to get rid of events on the spam model in favor of context-linked Log events, yeah.
**Hanson Ho** 24:45 But what… but what if… What… okay.
Alright, I got that flipped, then.
**Jason Plumb** 24:51 It's alright. This, yeah, it was a big topic, like, a year ago.
**Hanson Ho** 24:55 Yeah, I thought it landed the other side, but yeah, okay.
**Jason Plumb** 24:59 No, it's… it's… they want to use logs for… they want to use the log signal for events, and get rid of the confusion that events currently live in two places. Right? There's the data model with spans hanging off… events hanging off of spans, and there's also events.
And those events can have, you know, trace context on them. Like, those are first-class fields of logs.
**Hanson Ho** 25:25 What if you want second-class events that are basically as cheap as possible, that is completely unaddressable, individually, is tied to… I mean, it's the same as having an attribute timestamp, but then you can't have attributes with it unless you hack and say, hey, look at this namespace.
So, span events seem like a… I get the idea of wanting to disambiguate, but there is utility in a second-class event that is completely and wholly tied to, you know, the span, rather than being a separate addressable entity, but…
**Jason Plumb** 26:00 Yep.
Yeah, I think there was a lot of discussion around that, like, a year ago, when… like, when the decision was made. I think there's an O… I think there's an OTEP around this.
**Hanson Ho** 26:11 Yeah, I remember, but… I remember it incorrectly about how it landed, I guess.
**Jason Plumb** 26:22 This thing, yeah, 265.
Whoa! That's cool.
That's just… You don't see that every day.
**Hanson Ho** 26:39 It's just GitHub being GitHub, right? There we go.
**Jason Plumb** 26:42 It's eventually consistent.
Anyway, yeah, so… I think to your point, Hanson, there's a lot of discussion, and does it… because I'm not caught up on this, does it feel like it's progressing, or does it feel like it's kind of stalling out because everyone has opinions?
**Hanson Ho** 27:01 No, I think it's progressing. I think… I think… I would say most people are in favor of… of… Well, I think I… I think it's progressing. I don't think… I don't think there's an impasse or anything. It's just deciding how to encode it.
I think the utility of having things within the span, motivated putting things on the span, rather than, like, a separate log event.
At the same time, I think that's, that… oh.
what's that username mapped to? I forgot his, Santosh, I think? This is Santosh, right? Yeah, Santosh, yeah.
Mentioned that there is already a browser, resource timing event, that is asynchronous, that fires. We can take a look at that and see what it is, because if that's effectively, an event mapped to a span that contains a bunch of timing info, we can just piggyback off of that, in terms of… If we want to go with an event, that is separate from the span. But if we go the other way and just say, have an attribute that is a timestamp.
Then, then, you know, then we could go both. I mean.
it could also be both, like, this… the implementation could be one, and, you know, somebody else could want to do the other. But I think… I think we'll settle on a… on something that… that is reasonable. But I think… I think for, for, for mobile clients, Adding another thing.
For every network request is gonna increase the data volume probably by 90%.
Just a number of objects, because the network request is… is often the most… recorded signal out there, because there's so many hap… so many that happens, versus, like, any other ROM events or performance things, so…
**Jason Plumb** 28:55 Yeah, like, opting into these is not inexpensive, I think is what you're saying. Like, if you choose to… If you choose to get this level of detail on every request. Although, you know, in fairness, like, you're not gonna get TLS stuff for every request. That's just gonna be the setup first on the connection. You're not gonna get connection timing on everything because of pipelining, right? Like, a bunch of this stuff isn't with every request, necessarily.
**Hanson Ho** 29:21 There's actually events for, request, and response body.
**Jason Plumb** 29:26 Yeah.
**Hanson Ho** 29:26 So that stuff will all be there.
**Jason Plumb** 29:29 Jeez, oof, yeah, okay.
**Hanson Ho** 29:32 Which is why…
**Jason Plumb** 29:33 Very granular.
**Hanson Ho** 29:36 Which, which is, which is, which is, you know, I'm gonna take a look at, what, what Santosh has proposed, but if we're saying it's this much, I can't, I can't.
I can't in good conscience say, let's every network request create, 10 logs, or at least 8 logs.
that would be way too much. The juice is not worth the squeeze at that point. So… But one event that captures everything, maybe that's okay.
But then, that's still kind of almost double, so…
**Jason Plumb** 30:14 Yeah, you still got a lot of data.
**Hanson Ho** 30:17 in a high entropy, you know, thing with ID, so it's… it's… It's not just attached to something, it's its own thing.
**Jason Plumb** 30:27 I guess what I come to is, like, how do you use this data? Like, how does it… what problem does it help you to solve?
And if it's… like, I understand, like, if… if you're using a custom DNS server and your DNS is slow, then this helps you to understand that, or if, like.
your TLS is, like, using a heavyweight algorithm, or your device is struggling to do that setup, then… I mean, I don't know, but, like.
on every request, I don't know that this helps you that much.
**Hanson Ho** 30:59 At, edit.
**Jason Plumb** 30:59 Like, headers, especially, like, oh, okay.
**Hanson Ho** 31:03 so at Embrace, we're thinking about, like, the DNS stuff as… Does it exist? Is useful.
Whether the connection times are super long, it's useful, but whether it's 1 millisecond, 2 milliseconds, 3 milliseconds, it doesn't really matter. It's almost like, if it exists, it's a good signal. If it's, like, ridiculously long, it's a good signal. So you can almost bucket that into an attribute, saying, hey, this existed, or this is really long, by some definition.
So, I don't know if raw timing for the TCP stuff is… is… incredibly useful. And with the… with the request stuff, I think having semantic conventions around it is useful, but I don't know if it's useful to have that on all requests, so it… but then you basically have to structure your modeling based on the fact that you can potentially do it. So, it's almost like there's what we want to do, and there's practically what… so I think there's some discussion, but I don't think we're at an impasse. I just want to kind of raise this up to everybody's, to see everybody's, you know, their take on it.
**Jason Plumb** 32:15 Yeah, I think these are… I mean, these would be great semantic conventions to have available, and if there's a way to opt into these, like, for troubleshooting, or, like, with a high sampling rate, like, okay, only, you know, 1 out of 1,000 user sessions does this, or whatever, like… I think it… I think it could be useful… I don't know, I mean, it's new, so no backends are gonna support this out of the box, but it'll start to trickle in, probably.
**Hanson Ho** 32:42 I will leave a comment that some of these are not HTTP-specific, like…
**Jason Plumb** 32:47 like, these four are not necessarily… like, these could be generalized, right? I think to any, like, socket TLS start, socket TLS end, socket connection start and end… DNS is its own thing, right? Like, it sits outside of HTTP entirely, so there's some tweaking, I think, that needs to happen, but… These are powerful.
**Hanson Ho** 33:08 Yeah, I think I mentioned, you know, you could actually model the TCP connection stuff completely separately, and then just relate it. But then, you know, there is utility to having everything in one place.
So, you know, that browser timing event, the web folks would need, because everything's asynchronous for them, so they cannot put it in the same span, so they have to put it in a separate log.
So, if our convention just does this.
that may not be bad, as an alternative, but then also having something on the SPAN itself is also good. So, I don't know where Serby wants to land eventually. I think both are… I can see use cases for both, basically. This is the verbose one, and the other one's a quick and dirty one.
**Jason Plumb** 33:50 Cool.
**Hanson Ho** 33:53 They have a look.
**Jason Plumb** 33:55 Okay.
Jamie, you've got a bunch of pull requests open, like, are… we're just getting through these, like, you know, as we can, and Is anything contentious? Are you waiting for answers, or is there an ongoing discussion on anything?
**Jamie Lynch** 34:11 I think there was a bit of discussion on using context Rather than application in the initialization, so we can discuss that if folks want to. But having said that, I think we kind of ended up with a way forward.
**Jason Plumb** 34:26 Okay.
**Hanson Ho** 34:27 Is there a reason not to use context, if context is all that's needed? Application seems unnecessarily heavyweight, if, If we don't actually need it.
**Jamie Lynch** 34:41 So…
**Cesar Munoz** 34:41 He's… he is in a couple of places.
I added more details in my comments.
And…
**Jason Plumb** 34:48 Not it.
**Cesar Munoz** 34:48 according to Manuel, because sometimes we can get the application out of a context, if that's needed.
But, apparently there are some cases where Might not be able to do so.
So… And if that happens, Then, you know, some stuff won't work.
Right now, the only thing that I… that comes to my head… my mind is the… activity and fragment lifecycle instrumentations, because they rely on activity, listeners, Which is, Something that has to be done via the application.
But, I mean, it's not.
**Jason Plumb** 35:30 Oops.
But Cesar, could we change the instrumentation, then, to do this trick? To get the application?
from the conference?
**Cesar Munoz** 35:39 Yeah, we can, but it's like, in the case where we cannot, because apparently.
There might be some instances in which it's not possible then, that… You know, instrumentation one… one… one run.
**Jason Plumb** 35:53 Right, but that's.
**Cesar Munoz** 35:54 Now…
**Jason Plumb** 35:54 It's not the norm.
**Cesar Munoz** 35:56 It's probably an edge case, definitely.
So… But I would like you to… at least, you know, bring some luck, which I think Jamie already did.
So… Yeah, my only concern is somebody just… Crazing issues, saying, yeah, you know, this isn't working, or things like that, and… Or, you know, maybe not even realizing it, that it's not working, because it's not a compilation issue that's gonna happen. It's just something that won't work at runtime.
So… I'm not, like… Really opposed to this, but it's like, if we're gonna do it.
I would like to, you know, put all the… Bells and whistles, as they say, in terms of notification, logging, stuff, something that users can look at.
End the logs, and see if it's not working.
**Jamie Lynch** 36:54 Yeah, I definitely agree on that side of things.
Yeah, my understanding is it's just kind of, like.
The potential edge case is basically, like, a timing issue, like, if you're calling If you're initializing from within attached-based context, that's much earlier on in, like, the lifecycle, so… the application context could potentially be null . I think as long as we dissuade folks from doing that.
It feels like it would be okay for me.
**Hanson Ho** 37:27 That happens, like, super early on in the application init lifecycle, right?
**Jason Plumb** 37:33 It does.
**Hanson Ho** 37:36 I don't think we're even initialized at that point, probably, because I think… Unless somebody does. Anyway, you guys have the discussion there, so I'll just go and read it.
**Cesar Munoz** 37:51 And there are also PRs for, DSL enhancing.
That I really like, to be honest. I think that will… they will bring really great, you know, user intuitiveness and… And, you know, overall ease of use and extendability, so…
**Jason Plumb** 38:08 Yeah, yeah.
Yeah, this is nice.
**Cesar Munoz** 38:11 for that.
**Jason Plumb** 38:16 What does this look like?
**Cesar Munoz** 38:19 Now, this PR, it's, like, it depends on the previous one, right? So it's… in the end, it's not 25s. It's gonna be, like, the remaining after the other is… okay.
**Jamie Lynch** 38:30 Yeah, yeah, I think, I've got everything into one commit so folks can see it, yep.
**Jason Plumb** 38:38 Yep, that's cool.
So this, at least from a usability standpoint, this is, like, pretty similar to what we have today.
**Hanson Ho** 38:49 Yep.
It just looks better.
**Cesar Munoz** 38:54 And it's easier to extend, I think.
**Jason Plumb** 38:57 Cool.
**Hanson Ho** 38:59 There isn't a whole… parameters set that you have to, like, you know, do things. It's like… Drop it in. Context, just call those methods.
**Jason Plumb** 39:07 Yeah, so do we know… do we know which… is it the second commit, then, that we should be looking at here?
**Jamie Lynch** 39:13 Yeah, it's the last commit, to… You have to look at best bets specifically.
**Jason Plumb** 39:27 Oh, okay, yeah, I'm not awake yet. This is… this is great, yeah. Okay.
Awesome.
We'll take a look at that.
**Jamie Lynch** 39:43 Thank you.
**Jason Plumb** 39:46 there was some… there was some comment I left on one of these PRs, which I… I think… I don't know that I blocked it, but was it… no, I don't… I want to say it was one of yours, Jamie, but I can't remember… it was like, oh, someone was getting rid of a feature… Maybe in the DSL, I was like, oh, I think people asked for that.
But I don't remember which PR it was.
**Cesar Munoz** 40:14 Slowly with that one, removing all the wrong comp.
**Jason Plumb** 40:19 Well, in terms of removing, I think that's the only one.
Well, I look at a lot of repos, maybe I'm confusing with something else. I'm definitely not awake yet. Still a first cup of coffee.
**Cesar Munoz** 40:37 Alright.
**Jason Plumb** 40:43 Cool. Well, yeah. Anybody else have any other topics?
Okay.
Oh, Cesar, last week, you had mentioned looking into… the publishing suffixes.
**Cesar Munoz** 41:11 Alright, yeah, I agree with FPR for that.
**Jason Plumb** 41:13 You did.
**Cesar Munoz** 41:16 It's, it essentially mimics what's done In-contrip, where you… you will have to set a… Create a property in the module that you want to mix.
**Jason Plumb** 41:27 stable. Okay.
**Cesar Munoz** 41:28 So…
**Jason Plumb** 41:28 Is it one of these?
**Cesar Munoz** 41:30 Yeah, it's the… it's up… It's kind of, like, in the middle of the screen.
**Jason Plumb** 41:36 This one, yeah, okay. Great. You can tell I'm behind. I'm also time zone challenged, so I'm behind some of you.
Cool, yeah, so this one, awesome, great, awesome.
Cool?
Sounds like we don't really have anything else.
**Cesar Munoz** 42:01 Not from my side.
**Jason Plumb** 42:02 I'm gonna go volunteer.
Doing a volunteer day.
**Hanson Ho** 42:07 Nice! What are you doing?
**Jason Plumb** 42:09 There's a spot here in Portland called Project Lemonade, and they have a retail store in the shopping mall.
For foster kids, so kids that are fostered can go twice a year and do a little shopping spree, and it's all new stuff, because, like, foster kids always get garbage hand-me-down clothing, and they get to, like, go and choose out their own stuff. So, they're either gonna have us working in the store, or we're doing projects, I don't know which.
But, that'll be fine.
I was bagging apples at the food bank yesterday, so I'm gonna keep… Keep doing this stuff.
**Hanson Ho** 42:44 Cool.
**Jason Plumb** 42:44 Everyone, appreciate you, thanks for being here.
**Cesar Munoz** 42:48 Thank you, I'll talk to you later.
**Jason Plumb** 42:50 Right.
