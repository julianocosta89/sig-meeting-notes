SIG: Android SIG
Date: 2026-08-20
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Vishwan aranha** 00:16 Jason, how are you doing?
**Jason Plumb** 00:21 Hey, Vishwan.
I'm doing alright, how about you?
**Vishwan aranha** 00:26 Pretty good. It's just one day close to Friday.
**Jason Plumb** 00:31 It's true.
We'll give it a little bit more time for people to show up.
I'm still very much just waking up.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 00:47 Where are you located, Jason?
**Jason Plumb** 00:49 What's that?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 00:50 Where are you located?
**Jason Plumb** 00:52 I'm in Portland, so West Coast…
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 00:55 Okay.
**Vishwan aranha** 00:56 Must be 8 AM for you.
**Jason Plumb** 00:58 It is, yeah, it's pretty early.
But usually we're pretty outnumbered with European folks on this call, so… how about you guys?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 01:08 I'm in Toronto.
**Vishwan aranha** 01:10 Yeah, I'm from Saratoga Springs, New York.
**Jason Plumb** 01:12 Oh, cool.
**Vishwan aranha** 01:13 I always say Saratoga Springs, because if I say New York, people think I'm from the city, I'm not. Yeah.
**Jason Plumb** 01:20 Those are both… is Toronto also, the Eastern time zone?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 01:24 Yes, it is.
**Jason Plumb** 01:28 But you got a head start on me.
Sounds like David won't be able to join, but, well, yeah, there's Jamie. Hey!
Let's give it about 49 more seconds.
**Jamie Lynch** 01:58 I know that Hansen's out this week.
**Jason Plumb** 02:01 He is, okay.
Probably the last hurrah before school starts, if I had to guess.
**Jamie Lynch** 02:12 Something like that.
**Jason Plumb** 02:27 Alright, well, we've been kicking around this thing a little bit, and I think Vishwan was nice enough to be here to… Talk about some of this.
This is super awesome, I think bringing this back in is, like, gonna be really helpful, especially when it comes to the… some of the version conflict stuff that we might have, or we want to prove out. Hey, Cesar.
**Cesar** 02:50 you know, Hello, everybody.
**Jason Plumb** 02:56 And, so I put this on the agenda because, you know, through this discussion.
I think I was able to clone this branch and run the tests, and they run.
But if I remember correctly, and again, I'm still waking up, the way that these run or at the time that I did it, at least last week, was that everything was, like, running on device. Like, the… the server and the test and the app were all running on device. And what I was proposing was a slightly different architecture, where we just have… Only the app running on the device, and hopefully, like, more of a… kind of a more standard architecture where the fake backend, whatever that looks like, is running off-device, and then the test harness is also running off-device on the host.
And so I hacked some stuff up, I have a… I put it together there, and the discussion now is, do we like that? I didn't… I didn't do any sort of, like, drawing or anything, but effectively.
there's 4 components in this draft PR that I put together, and I don't know how much it's gonna help to look at the code, but I can talk through it.
The first component is the test runner, right? There's a JUnit test at some point.
Then there's two parts of the backend. One is this, Smoke test fake backend.
which is a component that comes from OpenTelemetry Java instrumentation. And that's what's used in all of their smoke tests. This is a little server that you can send metrics, traces, and logs, and OTLP to.
And it stores them in memory, and then there's endpoints to fetch them back.
When you fetch them back, you can then make assertions about The telemetry that was received.
In the case here, there's an additional component of the OpenTelemetry collector And that is unfortunate. This only exists, as a component to do the translation between gRPC and HTTP. So the Android exporters use OTLP, HTTP with protobufs.
The fake backend, for whatever reason, only right now supports gRPC.
So, I… for… in an hour from now, as the Android SIG meet… or the, Java SIG meeting.
And I also have something on the agenda there, to ask if an OTLP HTTP edition would be welcome to that thing.
If we add that, I think it's not going to be a problem, but we'll talk about it in an hour.
If we can add that, then we can drop that one component.
Anyway, and then the app, right? The Instrumented minified app runs on the device, does its thing, and then we can make assertions, Which is what this PR was doing. So I think… Correct me if I'm wrong, but I think where the question lies now is, what do we want to do with this PR? Should we merge it as is, and then take this as, like, a follow-up item? Do we like this architecture at all? Have people thought about this, or where do we stand?
**Jamie Lynch** 06:13 Yeah, so I'd definitely be in favor of having something running on CI, so… I'd be pretty happy to merge it as is, and then do all this as, like, follow-up work.
**Cesar** 06:30 I think it's the same for me, but I do really like this approach that you mentioned, Jason, because the, I've had issues in the past, which I think it's what… What Vishwan probably mentioned.
there. It's been a while since I took a look… I took a look at this, but I do remember issues where… because the app is minified, I wanted to you know, mock some stuff that might be already part of the… of what was minified, and then for the tests, that code was kind of, like, not found or something, so I had to kind of, like, ignore that code, which was OKCDP-related classes and stuff.
But then, that kind of defeats the purpose, because then you are kind of, like, ignoring some classes.
And you want to test the Binify path, so… it's… I like… well, as Jamie said, it's nice to have something that… nothing, but… I do like the smoke test approach the better. I didn't know that this existed.
And I'm surprised that it only supports gRPC right now, but let's see how it goes. So, thanks for the tip.
On April.
**Jamie Lynch** 07:57 I'd also add that I do definitely like this approach, And I think it's, yeah, something we should work towards,
**Jason Plumb** 08:10 Cool, I guess, so the, like, a big part of this is that server component, right? Wherever that is?
There's this HTTP server, right? Somewhere? Is it this thing?
Yeah, this thing.
So, long term, so we can merge it as is, get these tests started on the device, and then do the swap out with the fake backend, and then maybe eventually drop that collector as well.
Which is… that's probably a month or two out, but okay, so I can… I think I'm on board with that. I will… look at approving and merging this, and then there will be no hard feelings, hopefully, when this component gets deleted. Vishwan, is that cool?
**Vishwan aranha** 09:01 Oh, that's perfectly fine with me. Like, we can always, like, remove the collector later if, like, OTLP or, like, HTTP support plans. Yeah, yeah.
**Jason Plumb** 09:10 Yeah, I don't want to build a gRPC into Android necessarily, so I think doing the other thing would be better.
I mean, that's… I'm sure that someone will ask this in an hour, it's like, why don't you just use gRPC, since then, like, because no one on Android wants that, I think is the short answer.
But… okay, cool, so I will take a… I will take an action item… To create follow-up issues.
**Cesar** 09:37 Thank you.
**Jason Plumb** 09:46 It's so hard to write AI, but okay, I'm gonna do it.
Okay, I think that is good for that discussion.
Again, Vishwan, thanks for putting this together, I think this is great. We've needed this for a while.
Is there an issue that this is tied to? There is… what else is on this issue?
I think that's it.
Now, okay, let's, let's, let's go through the agenda. I might have one more thing that I just thought of.
That'll be vague enough. Okay, on to the next thing, which is talking about native… Stack trace stuff.
**Vishwan aranha** 10:44 This requires just a decision, so I wanted to run by you guys. If you click on that, there's, like, some discussion between me and, I believe, Jamie?
And yeah, just wanted to get the team's eyes on what, the next step should be, like, today we capture the native crash, like, it happened, but not the CEO C++ frames, like, showing where it happened. So, just going over… I also tried that lib unwind stack approach.
But it isn't available through the public Android NDK, so we would need, like, to copy and maintain it ourselves. And I also added some of the observations that came across.
**Cesar** 11:27 So, I… thanks for putting this up, Vishwan. I added a comment there.
that I thought it was nice to talk about in here, because… I don't have experience with these kinds of crashes in Android.
And I would like to better understand What you mean, or what the discussion… revolves around, which, so far, it seems to me that So, in order to collect these, I don't know if it's correct to call them stack traces, I guess, but that's… the wording that I kind of get from Java.
There is no native way to do so, and we have to rely on a library Or a tool that does that for us. And then, so the decision comes down to which tool we choose. Is that correct?
**Vishwan aranha** 12:22 Yeah, so when, like, native code crashes, like, Android gives us, like, very small emergency callback, like, I think it's called a signal handler, and the process may, like, already be corrupted, so that callback needs to do as little as possible. So, and I think we need enough information to, like, later show which native functions were running.
And, one option that I could think of is, like, to build the full stack trays inside the callback.
But the, available, like, unwinding code, like, allocates memory, and the user… and the users, like, it locks. But, so it may, like, hang or fail during the crash. That's one of my fear. And, the safer option that I could think of is, like, quickly save a fixed amount of raw information, like CPU registers, and, like.
loaded library, and then, like, rebuild, the stack after the app restarts. So, the basic question I had, like, is whether this snapshot gives us enough, like, reliable information across Android versions, and, like, any of the device types, so, I also thought of CrashPad as the third option, but as, like, it already solves, like, much of this using, like, a separate process, but it adds, like, large dependency work and, like, more integration work, so it will be, like, a huge PR, so I didn't want to go with that approach, but I'm, like, leaning towards, like, testing a small snapshot approach first.
Like, while keeping the crash Bright as a fallback, but I wanted to get everybody's opinion on which approach would be better before implementing anything. And that's why I, like, added, like, some comments and questions, yeah, if that makes sense.
**Cesar** 14:04 Yeah, do you know what's the difference with the one that… options that you mentioned, and the one that Jamie mentioned? I think he… there was another one.
Yeah, it…
**Vishwan aranha** 14:15 This one that Jamie mentioned was good, but it was, like, not publicly available, so we will have to maintain it ourselves if we, like, copy-paste the whole code. That was lib unwindstack, something like that. And the one for CrashPad, which was the third option, was, like, as I mentioned, like.
It does solve it, but it's, like, it adds, like, a large dependency. There's, like, a lot of integration work involved. It would be, like… I'd probably do it in small chunks, but still, it's… it's heavy work, so I didn't want to, like, add, like, unnecessary… crap, for lack of a bit of a better word, like, into the code. So, the main decision, like, I had, like, is not only, like, which library we should use, it's whether we unwind inside the crashing process, like, say raw state and, like, unwind after restart. So, like.
once we, like, agree on that safety model, like, I think based on choosing the… Like, tool would become easier, in my opinion.
**Jason Plumb** 15:15 So I'm almost hearing, like, 3 approaches before you go, Jamie, I'm hearing three. One is, like, using CrashPad or a separate process that you just pass the work to, which should be pretty fast and lightweight.
from your signal handler. The… which I haven't used CrashPad, but that's the way I understand it, after you just described it. The second approach is… in the… in the signal handler, actually do the unwinding, and then do something with the data. And the third one being just write the bare minimum, and then do the unwinding on read. Is that… do I have that right? There's three approaches?
Or am I conflating the last two?
**Vishwan aranha** 15:54 I think, you're conflating the last two, so…
**Jason Plumb** 15:57 Okay.
**Vishwan aranha** 15:58 So, basically, I can explain, like, crash padlet, like, is, like, signal handler. Like, hands work to a separate process, but it's, like…
**Jason Plumb** 16:04 Yep.
**Vishwan aranha** 16:05 Lot of work involved, and in, like, in Handler Unwind, like, it builds the stack immediately with, like, lib unwind stack, as I mentioned, but, like, you have to maintain. And there's a snapshot approach, which, like, saved, like, the bounded raw, crash date, and then unwind after restart. So… Right.
**Jason Plumb** 16:23 Right, yeah.
**Vishwan aranha** 16:25 I'm in favor of Snapshot, but I'm open to any suggestions or anything.
**Cesar** 16:30 Based on what, how you mentioned, I think Snapshot sounds good, too. Yeah.
**Jamie Lynch** 16:38 I think there's also a consequence to… What the data would look like in terms of, like, photometry, I think Snapshot probably is the most robust way of doing this. I think one of the trade-offs is, like, I'm pretty sure that brake pad and crash pad require mini-dump files.
So you then need to kind of, like, upload that effectively, unless you're passing that on device.
**Jason Plumb** 17:06 Can you clarify for a dumb guy like me what mini-dump is?
Is it, like, a symbol lookup table, or…
**Jamie Lynch** 17:14 I'm not super familiar with the format, I just know it contains crash information.
True.
Yeah, I think… I've touched, like, libunwind and LibUnwind Stack, which kind of, like, work in the signal handler itself.
And I'm not too familiar with the brake pad solution.
But… Yeah, I do know that folks use it on mobile, but I think… Firebase, Crashlytics, used it, or used to use it.
**Jason Plumb** 17:52 Cool, and there's… I mean, would it ever make sense to have options, like, both approaches implemented, and the user can pick between them, depending on the pros and cons, or is that probably over… is it overkill? And most… I think that's… that's where I would… That's how I would go… that's how I would approach answering the question of which one do we want to go with? Which one… which one do we think The users want and get value from.
And… If there's… if it's, like, there's value in both, and there's pros and cons, there's, like, a trade-off there, then maybe eventually we… Work towards supporting both, but certainly not to start.
**Vishwan aranha** 18:32 I can cue my opinion, if that's okay, like,
**Jason Plumb** 18:35 Fucker.
**Vishwan aranha** 18:35 Yeah, I think exposing both would be, like, overkill initially, like, we would have to maintain and, like, test two crash handlers across, like, every Android version and ABI, and, like, handler, inter… like, interoperability, and, like, it's, like, already sensitive, so that would be a pain to maintain, in my opinion, but…
**Jason Plumb** 18:55 Yeah, okay.
**Jamie Lynch** 18:56 I'd say this is definitely enough of a pain maintaining this sort of thing.
**Jason Plumb** 19:00 Okay.
**Jamie Lynch** 19:01 on implementation.
**Jason Plumb** 19:02 Okay.
Go ahead.
**Vishwan aranha** 19:05 We can choose, like, one safe default first, but keep the implementation, like, behind an internal interface, so, like, CrashPad could be added later, like, without redesigning everything and everything, so we could, like, make it more optimal, the code itself. Like, if you find, like, a real customer who needs Like, if you need, like, who needs, like, both of the approaches, we can expose, like.
The choice then, but for now, we can go by the safe default, if it makes sense.
**Jason Plumb** 19:34 Okay, so what I'm hearing is probably in the signal handler, writing the snapshot to the device, to storage.
And then, on restart, we detect that that snapshot has been written, we read it, and then we… use lib unwind, or something like that.
That's where my understanding is falling short. We detect it on disk, then what do we do with that snapshot?
**Cesar** 20:04 I think that's probably where the abstraction comes in that Vishwan mentioned, where… Maybe you'll take that snapshot and… unwind it, I guess, if that's the term, and… And for that, that's where you have to choose which would be the unwinder tool, I don't know.
**Vishwan aranha** 20:26 Yeah, I think… Yeah, like, after, like, restart, we basically validate the snapshot and, like, use the saved register as, like, the starting point for an, like, offline unwinder.
**Jason Plumb** 20:37 Got it.
Okay.
And then we emit that as an event.
**Vishwan aranha** 20:42 Yep.
**Jason Plumb** 20:45 And the snapshot that we write has enough information to determine the prior session and all that stuff, right, if I remember? Yeah, yeah.
**Vishwan aranha** 20:52 Yeah, it will have, like, basic information that is needed, so… Yeah, we can use that.
**Jason Plumb** 20:59 Okay, and what was the challenge around using lib unwind?
It wasn't available.
**Vishwan aranha** 21:04 It's, like, not publicly available, we'll have to maintain it ourselves, like, we have to copy-paste the entire library, and, like, yeah, it's… it's a pain.
**Jason Plumb** 21:12 Okay.
**Cesar** 21:16 It sounds like the, the, the, the one that has to… Offers a least resistant path Is the… is it brake… brake pad?
From what you mentioned, Vishwan?
**Vishwan aranha** 21:31 Yes.
**Cesar** 21:35 Okay.
Which could be swapped by… trash valve or leave on… on wine stack in the future, based on this abstraction that you mentioned.
**Vishwan aranha** 21:46 Yeah, we can always update it, optimize it as we need, and like, initial, like, could be a safety fault, then we can, like, update it, or refactor it, like, to make it, like, use any fallbacks you want, if… in case we find, like, some better approach for this.
**Jamie Lynch** 22:03 Have you used Wakepub before?
Just one thing that kind of, like, comes to mind is… I thought you had to use it out of process, so I was just wondering how… We'd approach that in terms of instrumentation.
That could be wrong as well. That's, just what I've… That's just what I last heard a few years ago.
**Jason Plumb** 22:38 I haven't used it. I don't know the answer.
**Jamie Lynch** 22:49 We can go Google that.
**Jason Plumb** 22:51 It sounds like… well, it sounds like we're in agreement, though, on the first step, which is, like, write the snapshot, and…
**Cesar** 22:57 Yeah.
**Jason Plumb** 22:58 And then worry later about the… symbolication problem.
I really, am not inclined to maintain a copy of LibUn Winestack. That sounds not fun to me as a maintainer.
**Vishwan aranha** 23:17 Yeah.
**Cesar** 23:17 than for me.
**Vishwan aranha** 23:21 I, like, I haven't directly used, like, BrickPad before, but I can, like.
verify, like, the Android behavior before, like, recommending it, for sure.
Cross-check everything.
**Jason Plumb** 23:34 And there's nothing that Google provides.
I'm assuming.
**Vishwan aranha** 23:37 Yeah, I didn't find anything, but if you guys know of anything…
**Jason Plumb** 23:42 Okay.
**Vishwan aranha** 23:46 Yeah, I didn't want to implement anything without, like.
getting the team's decision, like, otherwise, like, it would be, like, you know, if another better approach exists, we could probably go with that instead.
**Jason Plumb** 23:57 Yeah.
And it sounds like Embrace is maintaining a copy.
Is that true?
**Jamie Lynch** 24:04 of Liberstack, yeah. Yeah. And… I'll definitely agree, but it is a pain.
**Jason Plumb** 24:11 Does Embrace want to publish that, with an Apache license to the world, and we can consume it?
**Jamie Lynch** 24:18 I believe it's all open source.
already…
**Jason Plumb** 24:24 That's not my point.
**Jamie Lynch** 24:25 Yeah, and… I can ask a question.
**Jason Plumb** 24:32 Yeah.
Yeah, I don't know what we do on our end. I can… I can look into that as well. Cesar, do you…
**Jamie Lynch** 24:40 Certainly, sorry.
**Jason Plumb** 24:43 Do you have a native crash handler?
**Cesar** 24:46 No, no, we don't have it at the moment.
I mean, I'm… I think it's… Like, since we are… it seems to me that we already decided on the one Thing that was, not, that they didn't have.
many options, I guess.
Which is this snapshot thing. And the other seems like it's swappable.
So… if that's the case, I guess we can just go with whatever the easiest One is to use right now.
But, you know, based on what Vishwan said, that it's like, we can always swap it by another tool, so… I don't see why… Like, if it's swappable, then it's fine, whichever we go with at the beginning, that's what I think.
**Vishwan aranha** 25:45 Yeah, my opinion was, like, lazy and easy.
Approach first, which was… will be safe as well, so then we can always, like, updated.
And modify as needed.
**Jason Plumb** 25:56 That sounds good to me, too.
Okay.
**Jamie Lynch** 26:02 I'd be happy with that, yeah.
I think… We may also want to think about how the… I know we had discussions about this in the past, about whether we need some sort of build ID that lets you associate an ABK with The telemetry that got sent out, I think… That may be a requirement for this, depending on how we try and symbolicate stack frames.
Because, yeah, with a native crash like this, you're just getting Warframe addresses, so… unless you're symbolicating it on device.
Where the symbols might not be, you're not gonna get anything useful back.
**Jason Plumb** 26:48 Yeah, this… this is ringing a bell…
**Cesar** 26:54 The convention exists.
**Jason Plumb** 26:56 Yeah.
**Cesar** 26:57 I don't remember if we…
**Jason Plumb** 26:58 I think Servi worked on that.
**Cesar** 27:05 I don't remember.
**Jason Plumb** 27:07 Yeah… What's this? Look at this. What's this? Oh, it's a dupe. What's this?
This person disappeared. Have you noticed this? Anyone? Like, they were helping out for a while, and they just kind of went away. I guess that's the way open source works sometimes.
**Cesar** 27:27 Yeah.
**Jason Plumb** 27:33 Yeah, os.buildid… an API level, and then… I guess, yeah, this is just sitting there open, so we don't have an implementation yet, I guess.
Okay, that would be a good thing to pick up.
**Jamie Lynch** 27:51 Yeah, and I wouldn't consider this, like, to be blocking, like, stat trace unwinding or anything.
**Jason Plumb** 27:56 Totally.
**Jamie Lynch** 27:56 That's just, like, another part of a puzzle that we'll need to solve, along with… Yeah.
**Jason Plumb** 28:02 Yep.
Because as soon as someone starts the app on the next version of the app, everything's different again. Yeah, I get it.
I'm 95% certain that's why Serbi added this.
Was to support this use case.
Like, that's why she added the build ID at all.
**Cesar** 28:26 It's also useful, well, For regular crashes.
When you want to map them to the, R8 map, so… Yeah, it's nice to have that.
Pretty nice.
**Jason Plumb** 28:40 Yep.
Okay, are we ready to move on to the next topic?
**Vishwan aranha** 28:47 One last thing I want to mention is, like, I'm currently working on session management work, and I might need some Android hotel updates, so I will probably put issues or, like, tickets, or, like, PRs as necessary, and, check with you guys, probably in the next couple of SIGs, or, like, in the messages.
**Jason Plumb** 29:07 Can you elaborate on what you mean by working on session management?
**Vishwan aranha** 29:10 So, session management for Grafana,
**Jason Plumb** 29:13 Okay.
**Vishwan aranha** 29:13 So, where we have, like, to maintain session replay and, like, all the IDs necessary for, like, any crash rates or anything, so that… I will add more context on this.
I'll share with you guys in the issue that I create, or I created.
**Jason Plumb** 29:30 Cool. Be aware that there is a parallel discussion happening around… The idea of maybe having a session working group within OpenTelemetry that is short-lived, that includes folks from the Android SIG, the JavaScript SIG, Dart and Flutter and iOS, and to come together to come to a real, actual spec definition of what a session is.
what its constituent components are, and how users interact with it. It hasn't really been kicked off yet, because everyone's pretty busy, but that work is… is being discussed, and I would expect it to start Happening in the next month or two.
**Vishwan aranha** 30:14 Great. Sounds good.
**Jason Plumb** 30:15 Cool.
And certainly everyone on this call, and anyone else, is welcome to take part in that working group if you have an interest in, like, helping define, like, what a session is, because.
**Vishwan aranha** 30:29 Is there an invite or something? I don't know, like, will we be able to find it on Slack or somewhere?
**Jason Plumb** 30:36 Hopefully we'll be in the client… in the client, whatever it is, the client channel. Let me get you the correct name.
**Vishwan aranha** 30:43 Okay.
**Jason Plumb** 30:45 in the OTEL client-side telemetry. I'm sure there will be a mention of it in there. But then also, check out the, this thing. Oh, maybe I don't have it in my… I don't have it handy, but if you go to the community, repo.
My client, this thing… And this group meets every two weeks, and…
**Vishwan aranha** 31:12 Yeah, I joined as well, so yeah. Cool. I think I dropped before they mentioned anything about the session, so…
**Jason Plumb** 31:21 Yeah, so I think Martin's creating an issue, so that's probably in the community, I don't know if that's been done yet.
Guess I could just sort of look for it.
**Vishwan aranha** 31:35 I can follow up with Martin as well, so that, yeah, he can walk me through it.
**Jason Plumb** 31:40 Oh yeah, because you're coworkers, right? Yes.
**Vishwan aranha** 31:42 Yes, it works with Grafana too, so…
**Jason Plumb** 31:44 I keep forgetting that.
You know, originally, Martin and I also worked together at New Relic.
**Vishwan aranha** 31:51 Oh.
**Jason Plumb** 31:52 Small world. Okay.
It looks like… it looks like that has not been done yet, but okay, he's on it. I'm sure he'll do that. Okay.
**Vishwan aranha** 31:59 Perfect, yeah, thanks.
**Jason Plumb** 32:08 whatever it was, however you spell that, client side telemetry. Okay, Ben.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 32:15 Yeah, My item was, like, user attribution. I just wanted to take a quick pulse on, like, are we interested in having some sort of, convenience API, for adding user information?
Have we discussed this before? My current thoughts are, like, just adding a global attribute, if you don't want to support… add anything upstream.
But, like, before doing that, I wanted to understand if,
**Jason Plumb** 32:43 These are two separate topics here.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 32:46 Two separate, yes, two separate topics.
**Jason Plumb** 32:49 So, this is the idea, like, if your app has a user login screen or something, and the user logs in, you want to be able to, like, have that session… have the telemetry associated with that session also indicate what user is logged in when certain things happen. The user might log out, different user could log back in. Is that the idea?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 33:10 Yes, pretty much.
**Jason Plumb** 33:11 And so, by user attribute…
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 33:13 Some way to… yeah, some way to link a user to an app instance. Like, you have… probably have app installation ID or whatever, but, like, you do not know which user this, user account it is related to.
So that's… that's the goal.
**Jason Plumb** 33:29 Yeah, I don't think we… I mean, I'm… I'm confident we don't have that presently. It has been discussed, I don't know that we have an issue for it.
And I'm not sure, I don't remember where we left off with the semantic conventions.
**Cesar** 33:48 But just to… see if I understand. So, this will essentially kind of map a user account.
You know, from any kind of backend.
into… to… into OpenTelemetry, so… that… So… I mean, there's a prerequisite of having authentication in an app first, right, to… To have… to need this.
Which, I think we haven't… we haven't considered that scenario in Auto Landry so far.
And… and then… I'm just trying to find out if this is something that can be… it's standardized, or if it's just something that… a specific use case that somebody just wants to tie, like, somebody just wants, like, an API that allows them to know when a session starts or ends, or something like that.
And then they want to stick some extra… attributes there.
For their own context, in which case would be the user stuff.
So, I'm trying to think if it's case-specific, or we can do something in Auto Android for it, you know.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 35:14 I definitely hope we can do something in not Landroid. This would be a use case for a lot of people. Login is a pretty common use case. Say, if you are, like, if a user is reporting an issue.
and you want to, you know, look into the session information for that particular user, it would be helpful to narrow that search by email or, like, some sort of ID on the observability dashboard.
So that's where this requirement is coming from.
**Jason Plumb** 35:44 It definitely ties in very closely with sessions, because when you're doing real user monitoring, that's the user part of RUM, right? And sessions… I think you even said the word, user sessions.
We don't have a definition yet that indicates that a session is tied to a user at all, and there are certainly cases where they're not, right? Like, apps that have no authentication still get used, there's no user.
But maybe part… maybe part… I'm just throwing… I'm just speaking off the top of my head, but maybe something this working group comes up with is a standard that says, you know, if there's no user on a session, then you put no user. You know, like, maybe it's a first-class field of a session, like, as an entity or something, right? Like, we don't… We don't yet have that definition, so it's a little bit tricky to give you a strong direction, I think without having session dialed in.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 36:39 I… I don't see that necessarily tied to a session, or… I feel like this can be part of, any, any, any sort of signals, right?
Session, like, as soon as you open an app, like, SDK slices, and then you have a session.
So even, like, there are apps that might let you, you know, use, some functionality without a login. So, that's where I see it not being… technically part of the session, not strictly tried, tried. Session can be independent, and the user information, I, I think.
That can be an additional attribute, like, at least… From a… from a, observability point, like, at least when you're debugging, it can be an additional attribute on any kind of signal.
That's valuable, in my opinion.
Sorry, I think David had his hands up.
You wanted to add something?
**Jason Plumb** 37:48 David?
Okay, false alarm. Another answer. Okay, yeah. What do you got?
**DavidGrath** 37:58 Okay, I'm currently outside, so I may not be able to talk for them, but I actually… I'm just surprised that, the users in contact, so I thought there was a debris around GDPR when it comes to… So, what they call the traveling usernames and user emails within same code. And those triggers very emotional visibility.
**Jason Plumb** 38:20 I think you're calling in on a cell phone, and it sounds pretty terrible. It has nothing to do with your accent, it's just your data connection, I think, is pretty bad, so let's try one more time.
**DavidGrath** 38:33 What do you have optional?
**Jason Plumb** 38:35 About the same, but let's try.
**DavidGrath** 38:39 Okay, so my… I was… I'm just curious about the rationale behind putting user email within, attributes, because I thought that, generally speaking, people don't like How I put it? Inserting user data into telemetry. Also, priority concerns.
**Jason Plumb** 38:56 Totally.
Yeah, so I'm gonna try and… I'm gonna try and summarize. The question is, what's the strong desire to have this in the telemetry? Does it pose a privacy concern? I think that's… I think every time user information has come up.
It definitely gets flagged as a privacy concern, and… Users that see this may balk at this idea.
**Cesar** 39:21 Yeah, I agree, and I also wanted to add, on top of what was Discussed with, session and this data.
I also think that… I mean, I do believe that session and user data They help a lot each other, but they… but they… They probably don't depend on one another.
Either, as Ben is mentioning, I guess my… I also had that concern from David, about… Privacy?
But aside from that, to be honest, I'm just trying to find a way that we could… provide these from Autel Android, like, an automated way, like we do with Sessions, for example.
And I just don't see that, because it's… I mean, we could probably provide an API that maybe users can call when, you know, a user of their own has been logged in, probably.
And then we start tracking that, but it will have to be manual.
So, like, the thing is, I'm not quite clear of what exactly you're looking for, Ben. Is it something automatic, or it's just APIs, or… Or just to see if we're okay with that, adding that.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 40:43 Yeah, I'm not sure, like, if automatic is a good idea, like, apps would have, definitely they want to have this choice, like, what kind of information, user information is associated with the telemetry. Some might have a decide to add just the plain email, others who are, like, more privacy-conscious, or, like, they might, prefer a de-anonymized, internal identifier.
You know, to mitigate any sort of PII risk.
So, definitely a manual API, So my desire was, like, can we, like, unify this? Like, if we provide a convenience API, then we can make sure that, okay, this is handled in a standard fashion. If we decide to add it to multiple signals, then we can, like, add it from that single source, like, so… the users call an API, and then we have that information, and then we add it to whichever signals that we feel like it's valuable. Otherwise, like, the crude way I was thinking of implementing it is… would have been, like, a global attribute.
say, user.id, and then, like, add it to every single signal out there. So, something that's more flexible and, like, more standardized than that is, what I'm honestly looking for.
**Cesar** 42:03 I see.
**Jason Plumb** 42:04 We certainly don't have it defined yet.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 42:07 And there aren't… By the way…
**Jason Plumb** 42:09 Go ahead.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 42:10 But, yeah, I think my question is, like, do we have a desire for that? Like, and if there are any arguments against it?
**Cesar** 42:19 I… I wouldn't want to do… any smart thing, like, automatically promoted Android.
And… mostly because I wouldn't know, it's kind of like also designing when an app has been fully displayed.
I think we had this conversation a couple of times, and it's not really clear.
So, I think this is kind of like a similar issue, where we don't know.
When a user has been logged in or logged out.
So, I think the manual API is the one that makes the most sense, and… and… I… I think… I… I think it does make a lot of sense that this is a… common enough feature.
Across a lot of apps that… Probably it grants its own, first… Party.
API.
And, so I'm open to the idea of adding an API.
And that users will call when a user is there, and probably They will also choose which of the attributes that Jason mentioned… that Jason showed from the semantic conventions they want to populate, if they are all optional.
And I think that would pretty much be it. The one question that I don't know is… whether this will be something just like sessions, IDEs, where we just… Putting in every… Span or log.
expand and block, sorry, or if it's… if it's something that would be more like an event, you know? Like, user has been logged in, then that gets tracked there.
**Jason Plumb** 44:00 So let… so I will… I will say, I think the, like, session being on every piece of telemetry.
is… historically, like, a stopgap measure, like, that's not the right design, right? Like, from a data modeling standpoint, I think no one has ever loved that. I know the web, like, the browser folks hate that, because they're so crunched on payload size.
I think we will end up seeing session become an entity, and that's a newer OpenTelemetry concept that relates to the resource. And those two things go hand in hand, and entities can be modified, the resource kind of cannot.
But you can produce a new resource at runtime from an entity change.
That's… that's new work. Martin has a prototype for JS. We don't have a prototype in Android yet.
And that's another thing that I think a working group would want to flesh out. There is a use case around… I mean, I wrote this question, like, how… how tied is a user to a session? Like, we've definitely had users who say.
I need to be able to change the session. They want an API to make a new session.
And I forget if we implemented it or not, but the main use case for that was, if I have a user that logs out and a different user logs back in, or even the same user, I want to treat those as two separate sessions. And so, one user logs in, you're doing session stuff, and as soon as they log out, that session is expired, and they get a new session.
When a new user logs in. That use case has definitely been asked for multiple times, and I think is kind of expected.
**Cesar** 45:43 I… I see what you mean. I don't think they're that tight, though. I mean, I think they… it helps.
But in regular scenarios, I think usually an user Information will outlive a session.
Especially since we have a timing on sessions.
Time limit, so… like, regularly speaking, I guess the app will just have a user log in once, and then probably never again, and then a lot of sessions will Come and go, so… And you still can have the same information without a session, if you… all you have to… all you want to do is which user is using the app, so… I think they help… it helps to have both, but I wouldn't block each other.
**Jason Plumb** 46:35 So I think my short answer to this topic is we don't have anything great today. There's not a normal client-side, like, spec around user stuff and how it should be represented.
I think in the short term, if you need it to, like, tomorrow for your distro or for your offering, I think you can do one of a couple of things. You can generate an event.
At login time, and then on the back end, you know that this user is associated with this session.
And if they log out, you generate a logout event, and that's custom, like, we don't… I don't… I don't think we have events spec'd for that.
But that would be a thing, or add it to the global attributes, right? There's a supplier that you can give to the global attributes of Pender, and then just do, like, do it that way, like, in your distro. That's kind of the short-term thing, but I think you should expect that to change, much like you should expect the session handling to change.
And then I wrote the question here, like, maybe… maybe we've stumbled onto something, like, maybe the user should also be an OpenTelemetry entity, like, kind of similar to the session. That way you have… Two different entities in play, and they're not the same thing, but they do relate to each other.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 47:48 Right.
**Jason Plumb** 47:49 I don't know what that looks like in practice yet, because we're not doing anything with entities in Android yet, but… I think, I think it's interesting.
**Cesar** 47:58 I've allowed to have a…
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 48:00 Sorry, guard, God's sakes.
**Cesar** 48:02 sentences. Thanks, Ben. Sure, it will just help a lot if… if you have a… an existing use case, at least you know which would be the delivery method that best works for it, you know? It's, like, slapping everything in every signal or events.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 48:21 I… I only wanted a way to track back. So, like Jason mentioned, like, if we have an event for login, and then I can put a user ID in there, and then it would have the session information as well, then I can, like, look back, like, identify that session, and then, like.
look up all the sessions for that user. So, that way I have… when I'm looking at a specific signal, I know which user it relates to. I just need some way to correlate these signals to a user.
So the user would be the user would correlate to the user ID, and user ID would tie to the session ID, and then session ID would tie into everything else, and that's… that should be enough.
That might be the least invasive, or like, you know, without spamming it on every signal.
**Jason Plumb** 49:12 Yeah, like, even… Go ahead.
**Cesar** 49:16 I was just gonna say, based on what you said, it sounds like… The best option is… To do something similar as we do with sessions.
But… as Jensen said, what we do with sessions is wrong, so, it's probably a best case for an entity, but to be honest, entities have been I don't know what's the status of entities right now. I know years ago, they were an idea, and then… it went back and forth, I lost track of it, I don't even know if the Java SDK supports them yet, which will be something that we will have to wait for, so… Yeah.
I don't know if we can block things based on that, because I don't know how far away it is.
**Jason Plumb** 50:09 Right, that's basically what I was saying, like, if you need this today, there's a couple of approaches, just expect those to be the wrong approach, and… and by that, all I mean is, like, it will probably change when we align with the vision that entities are providing.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 50:23 Okay, yeah, this is not an immediate requirement, but, like, this is one of the gaps that we noticed, and, like, yeah, I, I… we can figure out an internal solution in the meantime, but, like, I want a direction on, like, if we have a decide to do this in Android, like, you know, get a sense of direction so that, like, I can also align the internal work in that.
**Jason Plumb** 50:45 Yeah.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 50:46 Yeah, I would think I…
**Jason Plumb** 50:47 Go ahead.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 50:49 And I meant to say, like, I… we are almost out of time, but, like, I'm… I think I have a general idea. I'll also try to look at, like, what entity… I… I do not completely, grasp the concept yet. I'll… I'll look it up.
And then maybe come back with a prototype, or even if it's just a convenience API, like, how we can do this today.
**Jason Plumb** 51:11 Check with Martin on his prototype. He has a… he has a draft PR for JS that has entities wired up In a pretty cool way, and I've had… I've had a mental to do… to do the same thing in Android, and I haven't ever taken the time to do it.
But it's pretty, it's pretty interesting how he's done it.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 51:31 Alright, sure, I'll talk to him.
**Jason Plumb** 51:33 I was looking to see if we have an API that allows the session to be rolled over or changed.
It doesn't look like we do, unless it's on the main… Is it some… like, none of these provide that, right? Session just gets you the ID and the time.
The publisher provides you the session, and allows you to observe it, and then… That's it.
**Cesar** 51:55 I think this, this would be the one, the provider.
But you will have to create your own.
**Jason Plumb** 52:01 Yeah, you'd make your own that was aware of users, or whatever.
Yeah. If you want, yeah, okay.
So we don't have a way to make that easy for folks yet. That's… I'm just thinking about it. Okay, because we're almost out of time, let's go ahead to this one.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 52:17 Yeah, I brought it up because somebody expressed interest in picking that up.
I know we discussed this, before, and, like, we wanted to have a more thorough discussion, and, like, also the concept of what a screen is versus what a destination is.
Especially, given the visible screen tracker stamping on all the logs and spans.
Yeah, any, any thoughts on… On the side.
**Jason Plumb** 52:53 Yeah, we probably don't have enough time to really thoroughly ask this out today. So maybe we roll this over to next week, but yeah, so please review this issue and provide some comments, and I will look at it and try and do the same.
We do kind of have this split-brain mode now, right? Where we've got two different attributes that are kind of representing the screen.
So, getting those kind of shored up might be nice.
I'll just put a note here to please review and put comments.
And the other thing that we also will not have time for… because I don't have the issue handy, but I thought of it earlier. Someone… filed, I think, a bug.
I think someone filed a bug, but maybe it's not marked a bug, obviously, about there being a version mismatch.
like, they… they went through the docs, and they said, our… like, our README or our docs say that you can use this version of the SDK with, this version of the API level on this minimum version of Android, and, like, they tried it, and it didn't work. Do you know this issue I'm talking about?
**Cesar** 54:29 No.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 54:31 Don't remember seeing one.
**Jason Plumb** 54:32 Okay, well, clearly I'm not prepared to talk about this either, but it occurred to me earlier, and I want to circle back on it.
**Cesar** 54:40 But if you, like…
**Jason Plumb** 54:43 This one.
**Cesar** 54:43 You can sit… oh, okay.
**Jason Plumb** 54:47 So we have a document of minimum requirements.
And they did an experiment, and… Found some incompatibilities.
So a test, and now that we have smoke tests, I think we might be able to start leveraging the smoke test to at least, you know, pair up these combos of things.
in an actual app with an APK and make sure that it doesn't crash, right? Like, that it actually works.
**Cesar** 55:17 Makes sense.
**Jason Plumb** 55:18 Yeah.
**Cesar** 55:25 It's probably the, the tests… Maybe that could be a second iteration for those?
Could be to… Set up the… Tommy project, or if you will, to the minimum… Requirements, and see if this.
**Jason Plumb** 55:43 Yeah. Yeah. Yeah.
**Jamie Lynch** 55:45 So… This is Fan, so he actually wrote a test that basically does what It basically does that. So, it has a… Like, minimal example app, but… Gradle test kit runs against our minimum versions, and I think that's how we detected this.
**Jason Plumb** 56:11 Cool.
What's the footprint like on that thing? Do you think it's something that could be added? And that we could…
**Jamie Lynch** 56:19 It is in the repo, I think? It is. But maybe I'm getting this confused with OpenTelemetry Kotlin. We definitely have it.
**Cesar** 56:27 I added some… I added a comment there, I don't remember.
cases?
**Jason Plumb** 56:33 Well, it was back in January, I mean…
**Cesar** 56:35 Oh, I see.
Yeah, no, I don't remember any yet, please.
**Jason Plumb** 56:39 Yeah, I know.
So you think it's in Android? I mean, you think it's in Kotlin, maybe?
**Jamie Lynch** 56:45 Yeah, it's definitely a Kotlin repo, I've just added a link. I can search Android, too.
But yeah, it's been very useful.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 56:58 So would this run against a generated artifact, or against a source?
**Cesar** 57:06 The other issue, like, is the source.
**Jason Plumb** 57:10 We can catch early when we break stuff, yeah.
**Cesar** 57:13 Yeah.
**Jamie Lynch** 57:16 It's either the source or publishing to a local Maven repo.
**Jason Plumb** 57:22 There's the link. I mean…
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 57:24 Against the source, we would run into more issues when we are, like, trying to mix old and new versions, like, whatever we have in the current repo.
So I was thinking maybe, like, just how, And then a developer would be consuming the library. I think a published artifact would be a cleaner approach.
**Cesar** 57:47 But it will be then already be published, so we already messed up by then, I guess.
Yeah, it's not…
**Jason Plumb** 57:54 Go ahead.
**Cesar** 57:55 It's complicated to make it from source, but Gradle can help with some, Like, multi-separate projects within the same repo.
Which, in the end, it's a bit tricky to make it work, but… I mean, it's possible, and I think the benefits of Knowing what… that… what things will break before we created these.
R.
are worth it.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 58:20 I was thinking we could, like, do a local publish, and then… consume something from their, local Maven.
**Cesar** 58:32 Or maybe snapshots, probably, we can use, too. And, like, a nightly…
**Jason Plumb** 58:37 Yeah, no.
**Cesar** 58:38 Yeah, yeah.
**Jason Plumb** 58:39 interesting.
**Jamie Lynch** 58:42 Okay, well, that's hope.
**Cesar** 58:43 I'll… I'll take a look.
**Jason Plumb** 58:45 Jamie.
**Jamie Lynch** 58:46 I was just asking if there is an issue or not for this, because I can… I'll post this… But I'll post the link and give a bit of context on what Van's done here.
**Jason Plumb** 58:58 I mean, I would say that this is the jumping-off point, but if you want a separate one for specifically for doing the testing around this, then I don't think there is one.
It would make sense to create one, I think.
**Cesar** 59:13 Yeah.
**Jamie Lynch** 59:14 I will.
**Jason Plumb** 59:15 We're at time… Thanks, everyone!
**Vishwan aranha** 59:20 Thanks, guys.
**Cesar** 59:20 Thank you.
**Jason Plumb** 59:21 Let's do it again.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 59:21 Yo.
**Cesar** 59:23 Right.
**Jason Plumb** 59:23 Right.
