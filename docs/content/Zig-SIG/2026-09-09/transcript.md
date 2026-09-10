SIG: Zig SIG
Date: 2026-09-09
Duration: 45 minutes
============================================================

## Zoom Recording Transcript

**Francesco Gualazzi (OpenTelemetry)** 08:48 Hello.
Today.
**Giovanni Panice** 08:51 Ayy.
**Francesco Gualazzi (OpenTelemetry)** 08:54 How you doing, Giovanni?
**Giovanni Panice** 09:00 I check, the preview… I checked the other meeting, but Anton was unable… was not there, so maybe we are only… me and you, so…
**Francesco Gualazzi (OpenTelemetry)** 09:14 Could be that this is the Tuesday where he has the clash with another company.
**Giovanni Panice** 09:18 Out of curiosity, but, how did you get this link? So… because, I mean, I was not able to do anything about that.
**Francesco Gualazzi (OpenTelemetry)** 09:26 It's in the Linux Foundation calendars that Pablo sent in the Autumn Maintainers channel.
**Giovanni Panice** 09:34 Oh, okay…
**Francesco Gualazzi (OpenTelemetry)** 09:36 Oh, let me, let me… I miss I did yours, so…
**Giovanni Panice** 09:41 I want to give you last regarding… previous meeting regarding the spreadsheet. Okay, and you said, thanks for checking… okay, because, I mean, yeah, I was totally… yeah, because we discussed about that,
**Francesco Gualazzi (OpenTelemetry)** 09:57 Long time ago, yeah. But immigration is now happening, and Yeah, everything should be sorted out.
**Giovanni Panice** 10:03 Okay, calendars.
**Francesco Gualazzi (OpenTelemetry)** 10:04 It's already been updated. The OpenTelemetry calendar, the official one, is already updated, but if you had copied the event, that doesn't.
**Giovanni Panice** 10:12 Okay.
**Francesco Gualazzi (OpenTelemetry)** 10:13 But that's… that's what happened to me, so…
**Giovanni Panice** 10:16 Okay, okay, cool. Okay, so, what do we have today in the agenda?
**Francesco Gualazzi (OpenTelemetry)** 10:23 No, nothing special, just checking the open issues and the border.
By the way, Antoine just messaged me that he is not available this week.
**Giovanni Panice** 10:32 Okay, it's okay. You know, it's still, you know, holiday period, so we should wait for the… the end of September, I guess.
Okay.
**Francesco Gualazzi (OpenTelemetry)** 10:47 So, let me open the board and present my screen.
And also, let me say that we have a handful of new collaborators that have… Yeah, yeah, so…
**Giovanni Panice** 11:03 Mmm.
**Francesco Gualazzi (OpenTelemetry)** 11:03 drink.
Yes. So, it was good.
**Giovanni Panice** 11:07 I have a question related to the Copilot, but it's something that we have activated, or is something more related to the organization?
**Francesco Gualazzi (OpenTelemetry)** 11:14 I think it's done by the org. I didn't activate it, but we can request reviews from Copilot, which is good.
**Giovanni Panice** 11:23 -
**Francesco Gualazzi (OpenTelemetry)** 11:24 And honestly, the one that caught yesterday, I didn't even see it, I don't know.
I don't know why it was so precise, and back, you know, contrary to what I had thought, said the compiler was right, and I trusted him, but I didn't double-check, but at first, it seemed like a hallucination, because The insert method is not used for retrieving the keys, it's just used for updating, or, like, adding one.
**Giovanni Panice** 11:58 - alright.
**Francesco Gualazzi (OpenTelemetry)** 11:59 Do you see the screen?
**Giovanni Panice** 12:01 Yes.
**Francesco Gualazzi (OpenTelemetry)** 12:02 So… Yeah, I'm reviewing, this too?
**Giovanni Panice** 12:09 Hmm?
**Francesco Gualazzi (OpenTelemetry)** 12:10 No, this one is not assigned to me, I don't know why, let me try. Oh yeah, it is assigned to me.
Okay, and this is opened by… Yeah, this is the iterator that Antoine and I discussed in the last meeting. Very good. Thanks, Antoine. I will merge later.
Then, the attributes builder, this is connected to this one, so I asked him to…
**Giovanni Panice** 12:33 Yeah, yeah, yeah.
**Francesco Gualazzi (OpenTelemetry)** 12:33 Because in the… because in the attributes builder, he was using this, parsing of key value, and it's also what we do in the resource, for other components, I asked him to factor out and he extracted here, very good. This one… I replied to the man, the woman, I don't know, I replied to them that they should be free to… Yeah, to propose. They replied, but I haven't seen it back, but it's on my radar, and this is a bug that we need to fix.
And I know Antwan is also working actively on the gRPC, which…
**Giovanni Panice** 13:14 Yeah.
**Francesco Gualazzi (OpenTelemetry)** 13:14 That's great. Have you seen the PRs?
**Giovanni Panice** 13:17 Briefly, because, I mean, it's huge, so…
**Francesco Gualazzi (OpenTelemetry)** 13:23 And then this one is long time open, and there was an initial PR that fixed it, but the PR… let's say Antoine and I reviewed, and even if the PR does fix it, The problem is that… as per Jacob's suggestion, we would like to fix it at a layer that is in the library, so in Zig Protobuff.
He has an outstanding PR, very long… the outdated PR, I think it's the date at March.
for… in Zig Protob, that is not reviewed, and I tried to contact Laurent, which is the main maintainer and the.
**Giovanni Panice** 14:03 Yeah, no, no.
**Francesco Gualazzi (OpenTelemetry)** 14:04 Zig Protov to ask him if I could join the maintainers just to help with the reviews.
**Giovanni Panice** 14:10 excuse me.
stupid.
**Francesco Gualazzi (OpenTelemetry)** 14:12 Because, again, Zig part of office is…
**Giovanni Panice** 14:13 Some gasoline.
**Francesco Gualazzi (OpenTelemetry)** 14:15 Yeah, no, it's… I think part of us is so critical for our project, that when something.
**Giovanni Panice** 14:21 Yeah, I know, buddy.
**Francesco Gualazzi (OpenTelemetry)** 14:21 funding.
**Giovanni Panice** 14:22 So you should understand that some stuff in the open source world go very slowly, so…
**Francesco Gualazzi (OpenTelemetry)** 14:28 I know, I know, we've had a nice chat, Logan and I, and I… I don't pretend, I don't not pretend, I don't.
**Giovanni Panice** 14:34 No, no, no.
**Francesco Gualazzi (OpenTelemetry)** 14:35 asking that I am joining the mentorship, but at least that, you know.
**Giovanni Panice** 14:39 you want.
**Francesco Gualazzi (OpenTelemetry)** 14:40 No.
**Giovanni Panice** 14:40 Genuinely, generally, so, no, I don't know what you mean, so…
**Francesco Gualazzi (OpenTelemetry)** 14:44 At least give me a chance.
**Giovanni Panice** 14:45 I knew you.
**Francesco Gualazzi (OpenTelemetry)** 14:45 You know, I don't have time… how much time to dedicate it, but…
**Giovanni Panice** 14:50 Yes, I understand.
**Francesco Gualazzi (OpenTelemetry)** 14:51 So, until then, I think this is still open, but if… if the review there is still dragging, I… I think I'm gonna… Be happy to accept the changes here, because they do fix the issue.
There are a couple of, you know, misplaced things, but we can fix that.
The problem is that I didn't hear back from the original contributor, so I don't know what happened.
Yeah, you see, the gRPC implementation using lib gRPC is something that Antoine is working on, and lib gRPC, as you know.
**Giovanni Panice** 15:26 draft.
**Francesco Gualazzi (OpenTelemetry)** 15:26 He's gonna be using this wrapper by Antoine himself.
And then using the C library, as a… main component to deliver the GRPC transport.
**Giovanni Panice** 15:41 Yeah, it's a trade-off that it's okay for now.
**Francesco Gualazzi (OpenTelemetry)** 15:44 And this one, I think we… not this one, I think we… There's a notebook?
No, I think… yeah, I think this one is, open, but… almost… ready to be merged, I guess?
Yeah, I.
**Giovanni Panice** 16:06 Yeah, so, yeah, go, boom. So…
**Francesco Gualazzi (OpenTelemetry)** 16:09 No, I mean, this one… This one just… let's just imagine.
**Giovanni Panice** 16:13 Okay.
**Francesco Gualazzi (OpenTelemetry)** 16:18 So this one was on my radar, but I haven't had time to do it today. So, basically, this one gets closed. Right.
Okay. So… Yeah, not… not too many… not too many open things, which is good.
And the next thing is, this back is working on it.
It's in the implementation, so thank you, Bach, if you're listening.
And… and this tool. So basically, a couple of bugs in the trace. There has been another one reported today.
Which, is from our friend, Giuseppe.
**Giovanni Panice** 16:58 Giuseppe, let me check, or, Kossitz, Kotzice.
**Francesco Gualazzi (OpenTelemetry)** 17:02 Is it in his zipper?
Wait, wait, wait.
It disappeared.
**Giovanni Panice** 17:09 Maybe he closed a date.
Freaky.
**Francesco Gualazzi (OpenTelemetry)** 17:14 No, I swear it was here, wait.
No, no, no, it's GitHub that is misbehaving, okay.
**Giovanni Panice** 17:20 Yeah, of course, it's, yeah, he chatted with me yesterday, asked me, because he's doing some GST, to, to the library, and he found another bug, and he wants, wanted to report to me. I said, don't worry, you can open an issue, even if it's a false positive, false positive, don't worry, we can take a look, without any issues.
Oh, don't be… I said, don't be shy, don't be shy, it's not an issue, even if it's a false positive, okay? So…
**Francesco Gualazzi (OpenTelemetry)** 17:53 Okay, so this needs to be verified, because it's a fazin,
**Giovanni Panice** 17:57 Yeah, yeah, exactly, so…
**Francesco Gualazzi (OpenTelemetry)** 18:00 I think we have to test coverage for that.
**Giovanni Panice** 18:03 Yeah, what?
we have in our backlog, we can give a low priority, okay? So, because, I mean, The library is not so used, so actually, if we have… bugs, it's okay, it's even okay, okay, to have them So… I don't know if you get to my bond.
**Francesco Gualazzi (OpenTelemetry)** 18:29 Yeah, yeah, yeah. Well.
We still try to make it functional for whoever wants to use it.
**Giovanni Panice** 18:37 Obviously, yes.
**Francesco Gualazzi (OpenTelemetry)** 18:38 And, and, this bug here about the histograms, I didn't expect.
But, thanks, Daisuke.
**Giovanni Panice** 18:47 That's okay, I think that he joined, he joined also the Slack channel, no?
**Francesco Gualazzi (OpenTelemetry)** 18:52 Alright, Jose, is it? Okay, good.
**Giovanni Panice** 18:54 Oh, I think yes.
**Francesco Gualazzi (OpenTelemetry)** 18:57 Yeah, so he will be working on Pierre, let's see what he comes up with.
**Giovanni Panice** 19:01 I'm a bit curious, because, I mean, I would like to see in which project they are using OpenTerm, if the, the library, if some, if something is open source, because I know that, Jakob, Jakob, yeah, is using Jacob, yes, sorry, because I, I have a friend that is Jakob. he's using it in, proxy.
In a… in a…
**Francesco Gualazzi (OpenTelemetry)** 19:29 Okay, yeah, yeah, yeah.
**Giovanni Panice** 19:31 Yeah, interesting project.
**Francesco Gualazzi (OpenTelemetry)** 19:32 It's not open source.
**Giovanni Panice** 19:34 No, no, it's open source, sir. You can… Okay.
Then, please.
**Francesco Gualazzi (OpenTelemetry)** 19:38 Shouldn't we be able to just do this with the power of, of Aww. Is it…
**Giovanni Panice** 19:46 Yeah, I mean, you said…
**Francesco Gualazzi (OpenTelemetry)** 19:47 there must be some build… Zig build zone… build a Zig zone that contains this, no?
**Giovanni Panice** 19:55 Yeah, because I saw APR that, I mean, I… I found the project because I… Okay.
**Francesco Gualazzi (OpenTelemetry)** 20:05 Outbox? This one?
**Giovanni Panice** 20:06 No, it's… it's me? No?
**Francesco Gualazzi (OpenTelemetry)** 20:09 Lucas?
**Giovanni Panice** 20:12 No, no, it's not this one.
**Francesco Gualazzi (OpenTelemetry)** 20:14 This tapaga?
**Giovanni Panice** 20:16 He's inside the… his, organization.
If I remember well.
**Francesco Gualazzi (OpenTelemetry)** 20:21 This guy cloned it?
**Giovanni Panice** 20:23 No, no, no, so, so, so, go to the, Go to the profile. Go in his profile.
Not the pretty good, but, the profile of, Jacob.
**Francesco Gualazzi (OpenTelemetry)** 20:40 Haha!
Okay.
So…
**Giovanni Panice** 20:44 When, going…
**Francesco Gualazzi (OpenTelemetry)** 20:44 Yarnov79.
**Giovanni Panice** 20:46 Yeah, search on November 11th Zig, go back in November 11th Zig, you can find.
**Francesco Gualazzi (OpenTelemetry)** 20:52 Yaronov, 97.
**Giovanni Panice** 20:55 Omo, well, if you remember,
**Francesco Gualazzi (OpenTelemetry)** 20:58 Yeah. Wow. All by heart, I know everyone.
**Giovanni Panice** 21:01 Yeah, exactly. He, he works in this user, yes. Yeah, I think this one is using, the library, if we can check.
**Francesco Gualazzi (OpenTelemetry)** 21:13 Should be able to see from the dependencies.
**Giovanni Panice** 21:16 Yes.
**Francesco Gualazzi (OpenTelemetry)** 21:19 No, that's a lie.
**Giovanni Panice** 21:23 Huh, alright, so…
**Francesco Gualazzi (OpenTelemetry)** 21:26 dimension, I don't know.
Yeah, Jacob believes…
**Giovanni Panice** 21:30 It goes heavy, because heavy.
**Francesco Gualazzi (OpenTelemetry)** 21:31 We don't blame you.
**Giovanni Panice** 21:32 Yeah, because I remember that he made the PR and linked this, I don't know.
**Francesco Gualazzi (OpenTelemetry)** 21:40 Maybe, maybe some other things? I don't know. But whatever.
Next time. But again, a quick, a quick, gitHub search didn't reveal… Anything? Maybe, I don't know, other repositories have it, I don't know.
But, you know, that is not too bad.
**Giovanni Panice** 22:02 Aww.
**Francesco Gualazzi (OpenTelemetry)** 22:03 Because again… We have a lot of things to be done and improved before even doing the.
**Giovanni Panice** 22:09 No, no, no.
**Francesco Gualazzi (OpenTelemetry)** 22:10 No?
**Giovanni Panice** 22:11 You know, indeed, indeed, I have a point, okay? If there are anything else in the agenda.
**Francesco Gualazzi (OpenTelemetry)** 22:24 No, it… no, it does not, so please…
**Giovanni Panice** 22:26 Okay, my point is, maybe, we can start thinking about, I don't know, well, there are no ma… there are no… there are so many libraries or framework around Zig, but I don't know if you start think… you know what I'm trying to, talk about. Maybe we should start thinking about some instrumentation, you know, for some… The dedicated stuff, no?
I don't know.
**Francesco Gualazzi (OpenTelemetry)** 22:58 I understand what you mean.
**Giovanni Panice** 23:00 So, You know, with event telemetry, there are also, you know, some, already in place instrumentation, no? Like, for frameworks, for, think about other,
**Francesco Gualazzi (OpenTelemetry)** 23:17 Instrumentation.
**Giovanni Panice** 23:18 Exactly, yes.
**Francesco Gualazzi (OpenTelemetry)** 23:20 Okay.
**Giovanni Panice** 23:21 So, I don't know in Zig, is there something that is meaningful and can be, you know.
decorated with an auto instrumentation.
**Francesco Gualazzi (OpenTelemetry)** 23:30 There is, there is one thing that is done with Zig, and that's the… The attacher, no? The attacher is done with Zig.
**Giovanni Panice** 23:41 Yeah, that's it.
**Francesco Gualazzi (OpenTelemetry)** 23:42 Telemetry, yeah, yeah, yeah, open telemet.
**Giovanni Panice** 23:43 Can you share the screen?
**Francesco Gualazzi (OpenTelemetry)** 23:46 Am I not sharing?
**Giovanni Panice** 23:47 No, sorry, I mean, can you share the project? So I'm seeing your… yeah, I'm…
**Francesco Gualazzi (OpenTelemetry)** 23:52 Oh, okay.
**Giovanni Panice** 23:53 I mean, you're…
**Francesco Gualazzi (OpenTelemetry)** 23:53 symmetry… That chair… I don't even… Injector, sorry, no, no, no, injector, injector. The OpenTeameter injector is a library that, is, built with Zig.
**Giovanni Panice** 24:10 Oh.
**Francesco Gualazzi (OpenTelemetry)** 24:11 Subway, and to make that.
**Giovanni Panice** 24:12 ealing.
**Francesco Gualazzi (OpenTelemetry)** 24:13 Yeah, yeah. And this one is a…
**Giovanni Panice** 24:20 Whoa.
**Francesco Gualazzi (OpenTelemetry)** 24:20 It's a library that you load with a deeper load, and it automatically injects the configuration for your life. Whoa!
**Giovanni Panice** 24:31 Yes.
**Francesco Gualazzi (OpenTelemetry)** 24:33 On top of this, there is zero-code instrumentation, that is, dearo code instrumentation, not all.
This one, huh?
I know this one has… been… done for, say, interpreted languages, or via BPF formative languages.
So Java, Python, JavaScript, USP.NET, and Go, which all have a runtime, they can do this, because you can… swap in their time.
the… the components. And if you are not… running a language with runtime, which is, you know, probably .NET, no.
**Giovanni Panice** 25:21 Yes.
**Francesco Gualazzi (OpenTelemetry)** 25:21 Sharp, see, sharp.
F-sharp, I don't remember. Well, it's Rasten Zig, which compiles to native binaries.
**Giovanni Panice** 25:30 With that.
**Francesco Gualazzi (OpenTelemetry)** 25:31 out runtime, you can use the OpenTeameter VFS augmentation.
Not yet.
Wee… If your question is, should we do something in this regard?
Yes, we… of course we could.
Why? When you already have the BPF1?
**Giovanni Panice** 25:54 No, no, no, no, no, yeah. No, well, I was, I mean, let me check, for example, yeah, maybe, yes, you are right, so it's not necessary.
So…
**Francesco Gualazzi (OpenTelemetry)** 26:10 This is an interesting project, though.
I don't even know what the repo is.
When we built the EBBF profiler.
**Giovanni Panice** 26:24 Oh, yeah.
**Francesco Gualazzi (OpenTelemetry)** 26:25 We're thinking, we were thinking.
**Giovanni Panice** 26:26 Yes, because, I mean, I'm used to use the auto instrumentation, for example, no?
**Francesco Gualazzi (OpenTelemetry)** 26:32 Java.
**Giovanni Panice** 26:34 Yeah, for Java, yes, obviously, and yeah, for some framework and so on, so I was thinking about…
**Francesco Gualazzi (OpenTelemetry)** 26:40 How do you control, though?
the metric names, which metrics, the latency, the buckets, and all of that. Do you have, like, a configuration file, or…
**Giovanni Panice** 26:50 Well, for example, to… let me show you, for example, you know, for Rakuteno, So… So let's, let me show you,
**Francesco Gualazzi (OpenTelemetry)** 27:15 Oops.
**Giovanni Panice** 27:16 Do you see the screen?
**Francesco Gualazzi (OpenTelemetry)** 27:18 Yep.
**Giovanni Panice** 27:19 Okay, so these are, like, the, the portal library, so for, auto-strementation, no, for Java, okay? Okay. So, for example, you use, for example, I don't know, the HTTP client, no?
And it comes with some automatic metrics, okay?
**Francesco Gualazzi (OpenTelemetry)** 27:38 Okay.
**Giovanni Panice** 27:39 So, things like that, or use, for example, Kafka, okay?
**Francesco Gualazzi (OpenTelemetry)** 27:43 That,
**Giovanni Panice** 27:44 I mean, automatically, move… copy the span, okay?
Through the… the consumer and producer.
**Francesco Gualazzi (OpenTelemetry)** 27:53 Nice.
**Giovanni Panice** 27:54 Okay, okay, things like that, okay?
So, this… this is what I was talking about. So, you know, in this instrumentation, no, for example, for Java, but for Gov or anything else, no, there are many other, you know.
**Francesco Gualazzi (OpenTelemetry)** 28:11 Yeah.
**Giovanni Panice** 28:12 Yeah, auto-instrumentation stuff, no? And, yeah.
I don't know if there is, I mean,
**Francesco Gualazzi (OpenTelemetry)** 28:22 By far, Sorry, sorry about this.
Talk about this.
**Giovanni Panice** 28:30 No, no, no, I know, no, the problem is that, yes, as you said, it's…
**Francesco Gualazzi (OpenTelemetry)** 28:37 This is recorded, huh?
**Giovanni Panice** 28:39 Yeah, you should, you should ask the…
**Francesco Gualazzi (OpenTelemetry)** 28:43 Oh, my God.
**Giovanni Panice** 28:43 You can't do anything. Okay.
**Francesco Gualazzi (OpenTelemetry)** 28:45 I will… I would have to close my door, but my daughter… But where we would find the backup gear.
**Giovanni Panice** 28:53 Fuck.
**Francesco Gualazzi (OpenTelemetry)** 28:54 Anyway, sorry, I get what it is.
**Giovanni Panice** 28:58 Yeah.
**Francesco Gualazzi (OpenTelemetry)** 28:58 I now understand what you were referring to.
Amazing.
There are no many libraries, right? So…
**Giovanni Panice** 29:07 Now, you know, I think there is an HTTP client for, for, you know, for, Zig, there is probably a web framework, for example, something like that, and we can, you know, expose some metrics.
Nope.
**Francesco Gualazzi (OpenTelemetry)** 29:26 Yeah, Woodland, yes.
**Giovanni Panice** 29:27 But I don't know, you know…
**Francesco Gualazzi (OpenTelemetry)** 29:29 The problem is… There is not a definitive one solution for HTTP.
But okay, people would like to do what… Whatever people.
**Giovanni Panice** 29:43 Yeah.
**Francesco Gualazzi (OpenTelemetry)** 29:44 Zoom.
**Giovanni Panice** 29:44 Yeah, you know, there are, 1,000 clients per Java, you know, okay? So… So… Yeah, I mean, I understand that, I mean, we are, like, a few people, but…
**Francesco Gualazzi (OpenTelemetry)** 30:01 No, it's okay. For me, the priority is always… Yeah, no, getting… no, no, no, the protocol buff, I'm doing okay.
**Giovanni Panice** 30:10 Good night.
**Francesco Gualazzi (OpenTelemetry)** 30:11 Providing something stable.
Something that will work.
And then we can figure it out, you know. So first, let's get a solid foundation.
And then we… and then we see what to do.
**Giovanni Panice** 30:28 Okay, okay. Anything else?
**Francesco Gualazzi (OpenTelemetry)** 30:33 Nope, not that, not that I… Nothing, nothing comes to mind right now.
**Giovanni Panice** 30:40 Okay, okay, so… let's close here, so thanks, Francesco. See you.
**Francesco Gualazzi (OpenTelemetry)** 30:46 Oh, thank you, Giovanni. I will try to close the door next time.
Get ready for when your daughter lives there.
**Giovanni Panice** 30:54 Yeah,
**Francesco Gualazzi (OpenTelemetry)** 30:55 Yeah, yeah, yeah.
**Giovanni Panice** 30:56 One day, I'll explain you my configuration to avoid this kind of problem.
**Francesco Gualazzi (OpenTelemetry)** 31:01 Sounds good.
die.
**Giovanni Panice** 31:03 As you see, I mean, my… my webcam is not, is.
**Francesco Gualazzi (OpenTelemetry)** 31:09 Yeah, yeah, yeah.
**Giovanni Panice** 31:09 Whoa, okay.
**Francesco Gualazzi (OpenTelemetry)** 31:11 Giovanni streak.
**Giovanni Panice** 31:13 Okay. Anyway, to you.
Bye.
**Francesco Gualazzi (OpenTelemetry)** 31:17 Bye, my man.
