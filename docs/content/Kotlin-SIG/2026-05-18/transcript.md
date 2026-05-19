SIG: Kotlin SIG
Date: 2026-05-18
Duration: 30 minutes
Zoom Recording URL: https://zoom.us/rec/share/3HbsmjNLRKB5YCkEN5REX2ZuPyMnHJzbQDlhcNdGwSmy747o0R7UERsySW7l6hsz.MYypHV417NXz_Pf6
============================================================

## Zoom Recording Transcript

**valexandrescu** 02:40 Hi, everyone.
**Jason Plumb** 02:43 Hello!
**valexandrescu** 02:56 Hey, guys, I have a question. Is it appropriate if I smoke with you guys on the call?
**Jason Plumb** 03:03 It's rough, because it just is gonna make me want to.
I quit, like, 15 years ago.
**valexandrescu** 03:08 Oh, damn, I'm sorry.
**Jason Plumb** 03:10 No, I think it's fine.
**Jamie Lynch** 03:12 Yeah, that doesn't bother me.
**Jason Plumb** 03:15 It's hard to complain about secondhand smoke over Zoom, you know?
**valexandrescu** 03:21 Yeah, the thing is that I think it's appropriate to show by self, but at the same time.
I just brought myself a cup of coffee, and just thought, hmm… I think I'll just have one while during the call, but I wasn't sure if it's professional or not, or… I don't know.
But yeah, thanks.
**Jason Plumb** 03:41 okay with it. If someone wants to complain, they can complain.
**valexandrescu** 03:44 Hmm.
**Jamie Lynch** 03:46 Yeah, that's right by me. We have the occasional beer on a… call it and breaks, so…
**valexandrescu** 03:54 To each his own vice, I guess.
But damn, 15 years ago, well…
**Jason Plumb** 04:03 I still miss it.
**valexandrescu** 04:05 really.
**Jason Plumb** 04:06 Oh, yeah. Yeah.
**valexandrescu** 04:07 Oh.
Okay.
I don't know, some of, some of my friends quit, and… they don't really miss it. I mean, one of them is, I don't know.
He said he doesn't want to smoke anymore, but from time to time, he buys a cigar for a barbecue or something, or someone's birthday or anything, and he just pops it while we meet up.
But it doesn't really have cravings for cigarettes, so I kind of find that weird.
I mean, do you ever quit, you know?
**Jason Plumb** 04:42 Right.
Yep.
Well, so, tell us a little bit… I think… is this your first time joining the sitcall?
**valexandrescu** 04:53 No, no, no, it's actually the second time, but I haven't been on for a while, because… I mean, I've had a couple of things going on, and I haven't been in the loop with what's been going on with the project. I know I picked up some issues to work on, and I haven't gone around doing anything for that, so I thought I'd just jump back with you guys on a call, see how things are going, and… see where I can pick up from, because I have some free time.
Nowadays.
**Jason Plumb** 05:18 Great.
So, Jamie, do you want to share?
**Jamie Lynch** 05:28 Yeah, sure. Sorry, I'm just getting up to speed here.
**Jason Plumb** 05:32 That's fine.
**Jamie Lynch** 05:34 Both.
Popped the meeting notes link in the chat, so please do add topics if anyone has one.
Yeah, I had, like, a couple of topics, but I think it'll be quite quick if nobody else has something to discuss.
**valexandrescu** 05:53 I started working some time ago on the file export issue that we talked about at some point, and I really wanted some pointers on that, if you have the time.
But other than that, I'm not really sure. That's why I wanted to jump on the call, so I can see if I… if someone already started working on this, or if I can continue working on it, you know.
**Jamie Lynch** 06:22 Cool.
Yeah, we can talk about the power export.
So, Oh, we could just start from the top. Just… I think I mentioned this a couple of weeks ago, but I'm gonna be out for the next 6 weeks on parental leave.
From next Monday, hopefully.
**valexandrescu** 06:44 Congratulations.
**Jamie Lynch** 06:45 Thanks. So, I think… Handsome, should be… joining most of the calls, but I think he's out next week. We might have… another Jason from Embrace, popping along as well. He's probably gonna get involved in, Kotlin and Android 6, once he's a bit more up to speed.
**Jason Plumb** 07:09 Well, so you're… you're due, like, in the next week, basically.
**Jamie Lynch** 07:13 Yeah, yeah, it's like, it's coming out by next Tuesday.
**Jason Plumb** 07:18 Welcome back.
**Jamie Lynch** 07:19 That's the backstop, but anytime before then.
**Jason Plumb** 07:23 Well, I probably won't have a chance to see you, like, at least on Zoom until then, so good luck with everything, it's exciting.
**Jamie Lynch** 07:29 Thanks. Yeah. Well, hopefully we'll see each other on the Android seg tomorrow.
**Jason Plumb** 07:35 Oh yeah, okay. Yeah.
Cool, good luck anyway, it's gonna be…
**Jamie Lynch** 07:42 Yeah.
**Jason Plumb** 07:43 An adventure, as always.
**Jamie Lynch** 07:44 Oh yeah, for sure.
Right, we can, chat about the file export if you wanted to.
**valexandrescu** 07:58 Yeah, well, with regards to that, so I started working on it in, in the… in the project, in the TLP export, I think, module.
Might take some time for me to start it all up.
But, still… I'm not really sure. I mean, yeah, that's what I went on, and I saw that there are some standardized things we can, We actually were supposed to export, and I think it's… somewhere down… the thing is that it says that we're supposed to support, exporting Traces, logs, and… That's about it, I guess.
Yeah, and that, yeah, exactly. Traces data, metrics data, and logs data, yeah, that's it, yeah.
So I started creating some interfaces, there's some things here and there to support receiving that.
But what I wanted some pointers on was if I'm on the right way, like, if I started working in the right place.
And… well… the whole idea of this issue is that I suppose that the library is supposed to, at some point.
be expected to export this to a JSON file somewhere, right?
**Jamie Lynch** 09:19 Hmm.
Yeah, so I think that's probably the first obstacle to tackle, so… If I remember correctly, there's… 2… two kind of ways you can do OTLP. It can be in binary encoding or JSON encoding. I think right now we only support the binary encoding, so… yeah, supporting JSON encoding would definitely be the first step, and then… Writing to a file would probably be… a logical next step for Matt.
**Jason Plumb** 09:59 And the tricky… The tricky part about that is that there isn't a reference implementation for Java to even borrow from, because Java doesn't have a JSON exporter.
at all.
**valexandrescu** 10:09 It's not… that's not… that's not the issue, actually, it's the fact that by design, being a, well, multi-platform project, the core doesn't really export to anything, because not all platforms might support it.
But, yeah, this mechanism to export to a JSON format won't be an issue, because from what I saw, we're expected to use, what's it called? .
**Jason Plumb** 10:36 Protobuff?
**valexandrescu** 10:38 No, no, no. KTOR, yeah, KTOR.
**Jason Plumb** 10:41 Okay, Tora, okay.
**valexandrescu** 10:42 I mean, I saw that we're not actually adding too many libraries to the project, and if we do, it should be pretty well documented why, and especially it needs to be a multi-platform library. I thought about what KTOR gives us already in terms of serialization, but that's the thing, that's why I wanted to chat about, because I wasn't really sure if it's the right way to do it in this case. And… Later on, that's the fiddly part, because… depending on which target we're supporting, where do we write it? Because, I mean, for the Java target, it's fairly straightforward. It says in the documentation it's supposed to, default to STD out.
And if not configured somewhere else, I guess.
But the other ones, I mean, mobile and native, that's… that… I mean, native, yeah, that's also the same… the same thing, but the mobile targets, I'm not really sure how they're supposed to work.
**Jamie Lynch** 11:51 Makes sense.
So… I've not actually used KTOR that much. Do you know what it uses for serialization under the hood? Is it relying on another Kotlin library, or does it roll its own serialization?
**valexandrescu** 12:07 Not really sure, but if it does rely on something, it might be KotlinX, like…
**Jamie Lynch** 12:12 Yeah.
**valexandrescu** 12:12 JetBrains' official library for serialization.
That won't be an issue, but what I really wanted to shed some light on is… I can't really just add any module I find, any dependency I find. I need to use something that is widely supported for the whole library, right?
**Jamie Lynch** 12:42 Yeah, I think that would be… the ideal case.
Although… Having said that, if… If we can kind of, like, confine… Like, confine, platform-specific bits to, like, one… one function or, like, a couple of interfaces, but… and the core logic is all in Kotlin multiplatform, then that would make it possible for… Other folks to kind of, like, add an implementation later on.
**valexandrescu** 13:20 Yeah, exactly. My thought process was that I don't really want to reinvent the wheel here, and if I can use KTOR, which already gives me everything out of the box, I would just add it to the build, but… Okay That's, that's what I wasn't really sure about, because I saw that most modules have a really slim list of dependencies.
**Jamie Lynch** 13:47 Yeah, I think… My take on this is, I think it would be fine to add either KTOR or… Kotlin X civilization, which I suspect Katal might be using under the hood.
It is.
Yeah, because I think the OTLP stuff is in its own separate module anyway, so you could… you're basically opting into including that in your build, so that feels like a reasonable ask.
Yeah, Jason, do you have any thoughts on that?
**Jason Plumb** 14:23 No, I mean, KTOR seems like a safe approach. I also don't know how they do serialization, I think we can also take other libraries kind of as a case-by-case basis if we need to, but keeping it, you know, heavily Kotlin-based seems like the right move.
**valexandrescu** 14:41 from what I looked up, there's no need to invest that much in researching options, because out of all that's available right now as a multi-platform solution.
Kater is kind of the only one that gives us that, but being part of a framework.
well, they have their own way of doing it, so that's why I wasn't.
**Jason Plumb** 15:04 Pretty sure.
**valexandrescu** 15:04 it's a good idea, because I don't really want to pull in their mechanisms into the library.
**Jamie Lynch** 15:11 Yes.
**Jason Plumb** 15:11 If you can keep those abstracted, that's ideal.
**valexandrescu** 15:14 Yeah, exactly.
**Jamie Lynch** 15:21 Cool. So… Yeah, I think… I think we've kind of got, like, a vague consensus on that, but, like, KTOR or COLINX Civilization.
would be appropriate to use for this, and… But supporting JSON encoding of OTLP is probably the first step towards Completing this.
**valexandrescu** 15:48 Okay, thanks.
**Jamie Lynch** 15:51 Cool.
Was there anything else on that that you wanted to discuss?
**valexandrescu** 15:58 No, not really. If I have anything else, I can just, send you… send you a message in private for, like, specific things. But no, that… that was the whole idea, yeah.
**Jamie Lynch** 16:09 Sure. Yeah, it might be worth, dumping it in the OTL Kotlin channel, just because I'm going to be out for a few weeks. Ordinarily, I'd be happy to apply, but you might not get a response.
**Jason Plumb** 16:23 Best to put in the channel anyway, that way other people can chime in or search for it later.
**valexandrescu** 16:28 Yeah, yeah, yeah, absolutely.
**Jason Plumb** 16:29 If it's not appropriate, we could also just do it in the issues, that way it's contained to the… To the issue, but.
**valexandrescu** 16:35 Yeah.
**Jason Plumb** 16:35 I would say in general, you know, this is a… this is a big, this is a big issue. We might consider splitting it up into different… different issues per signal, like, let's do tracing first, or whatever, and, like, keep… maybe we could, like, peel off a separate issue.
and do whatever we can to keep those pull requests for implementations, like, small. So if we're starting with, like, the interface, that can be a self-contained PR, and then if you have implementations, like, for the JVM or for native Kotlin, like, doing those as separate, you know… separate PRs as you can. I mean, sometimes it's hard to, but… Incremental's better for reviewers.
**valexandrescu** 17:16 Yeah, yeah, yeah.
What do you mean by separate signals?
**Jason Plumb** 17:26 Metrics, traces, and logs.
**valexandrescu** 17:30 Okay, in that sense, okay.
**Jason Plumb** 17:33 Yeah.
**Jamie Lynch** 17:42 Cool. We can move on to the next topic. I just put something about the Attributes API, to see if we can… Kind of recap where we are then.
If anyone else does have topics, please feel free to add them.
So, basically, this issue was just around gaining consensus on the API that we use to add attributes.
And I think there are a few differences, which we discussed last time.
And… from what I remember.2… is V… Only one that's remaining.
**Jason Plumb** 18:28 Yep, and there's $4.99 that I opened.
**Jamie Lynch** 18:31 Yeah.
**Jason Plumb** 18:32 Yep.
**Jamie Lynch** 18:33 So, potentially, we could close out this one.
As if the only remaining issue on this is tracked by this ticket.
Is that correct?
Or do we have one?
**Jason Plumb** 18:51 So, yeah, yeah, yeah. And then the milestone, it's just… it's just those two issues. That's all that's left, so…
**Jamie Lynch** 18:57 Yeah.
Cool.
Cool. And then… this issue… I haven't had a chance to get around to… this. I might get a chance sometime this week to kind of sketch something out, solve a PR forward, if so.
**Jason Plumb** 19:31 Cool.
Well, doesn't always have to all be on you.
**Jamie Lynch** 19:36 True. If anyone else does want to, take it up, yeah, more than welcome.
**Jason Plumb** 19:43 I mean, I'm more than thankful that you've been doing the lion's share of this work, but… Would be cool to get other… other help.
**Jamie Lynch** 19:52 Yes.
Yeah, I think we're hoping to get a bit more time from Hanson and Jason, but we just need to discuss that internally, and… There may be argument for it.
**Jason Plumb** 20:05 Yep.
**Jamie Lynch** 20:09 Okay, so… starting out.
**Jason Plumb** 20:15 So, when's the next release?
My favorite topic, when's the next release?
**Jamie Lynch** 20:22 It's, like, the question.
**Jason Plumb** 20:24 So the last one was April 21st, so we're about a month out now.
So we might need to… we might need to cut one. I think I haven't done it yet.
So maybe I should just do it this week, even if we don't have attributes being stable.
We'll pick it up in the next one.
We're trying to do it every two weeks, right?
**Jamie Lynch** 20:48 I think… I think we kind of settled on around a month? Okay.
Good.
**Jason Plumb** 20:56 I bet we wrote it down, didn't we write it down?
**Jamie Lynch** 20:59 We probably did write it down somewhere.
**Jason Plumb** 21:01 Okay.
**Jamie Lynch** 21:01 Let's see…
**Jason Plumb** 21:05 Monthly, yeah.
It's in the releasing MD. It's monthly.
**Jamie Lynch** 21:09 Cool.
**Jason Plumb** 21:11 Alright, so, do you think this is the week, though? We should probably do it this week, or next week?
This week.
**Jamie Lynch** 21:18 I'd say this week is probably a good… good one.
**Jason Plumb** 21:22 Alright, is there anything else that we want to sneak into this release, though?
Or that we think should be in there.
The only open PRs right now are dependencies.
So, that's probably not that important. So, I will… I will try and do the release this month, like, this week, and if I encounter any troubles, I will send you a message.
**Jamie Lynch** 21:46 Awesome.
Script.
**Jason Plumb** 21:51 Given that it's pretty similar to Android, hopefully no… no hiccups. And the fact that it's based on Android, and we've done it a few times.
**Jamie Lynch** 21:59 Yeah, hopefully all the CI issues have been ironed out now.
**Jason Plumb** 22:04 Yep.
**Jamie Lynch** 22:10 Okay, cool.
Did anyone else have anything they wanted to discuss?
**Jason Plumb** 22:16 I think Carlos joined. Hey, Carlos.
**Carlos Alberto Cortez** 22:20 Hey, hey, sorry, I was listening to something else, yes, better than ever, yes, yeah.
**Jason Plumb** 22:25 Yeah, you know, you're cool. Do you have any… we're kind of… we're running short on agenda.
And basically concluded that we have the one issue remaining around the Attributes API. We think once we get any value in there, it will be mostly to our liking, unless you have anything that you've identified as being problematic. And then we'll also be cutting, separate from that, we'll be cutting a release, this week.
**Carlos Alberto Cortez** 22:48 Yeah.
**Jason Plumb** 22:48 Just to keep that release process going.
**Carlos Alberto Cortez** 22:50 Yeah, that's good. Yeah, okay, I can do a late review of the rest of the API, but I think if this group is happy with the current state, probably we are good. I will double-check.
**Jason Plumb** 23:02 Cool, thank you, that would be helpful. And also, I don't think I said it outright to you, but, congratulations on graduation, that's huge.
**Carlos Alberto Cortez** 23:11 Yeah, that was a good one. Yeah, it took forever, you know, like, I know. Yeah, good, good. So much…
**Jason Plumb** 23:16 Yeah.
It's cool.
**Carlos Alberto Cortez** 23:18 Likewise, I have a comment on the previous point on OTLP JSON support.
**Jason Plumb** 23:24 Yeah.
**Carlos Alberto Cortez** 23:25 That's interesting. Out of curiosity, how does Android work? Like, what's the preferred exporter?
There.
**Jason Plumb** 23:34 I think I can address that. So, we, by default, have this disk buffering exporter. We write protobuf-based files into one directory per signal type.
And files accumulate until another exporter comes on and reads those off the disk to export it. So there's a buffering, we call it disk buffering, where we're accumulating these OTLP files on disk, on device.
And then they're harvested later.
**Carlos Alberto Cortez** 24:03 Yeah, and what about the OTLP version? Like, what's the preferred one between the, HTTP, Grpc or JSON? Which one do you prefer there?
**Jason Plumb** 24:15 We default to the OpenTelemetry default, which is HTTP.
**Carlos Alberto Cortez** 24:19 Okay.
**Jason Plumb** 24:21 So I'm sure there are some… I know that there are people that have asked for the other one, for GRPC.
**Carlos Alberto Cortez** 24:26 Okay, I'm asking because I see that, yeah, you're saying that you will probably need to support JSON and calling first.
So, is that because that's more… used in Android, after all.
**Jason Plumb** 24:36 No, we're not doing anything with JSON in Android.
**Carlos Alberto Cortez** 24:41 Okay, so in that case, why did you… why do… why does this group think that JSON Encoding first is a thing to do.
Let's go through it.
**Jamie Lynch** 24:51 Fists.
**Carlos Alberto Cortez** 24:53 Crazy, yeah.
**Jamie Lynch** 24:55 Currently, I think I can reword this. We already support binary encoding for OTLP right now.
I think within the scope of implementing OTLP file export, we need to support JSON coding as a first step, and then… Support writing to a file, if that makes sense.
**Carlos Alberto Cortez** 25:16 Okay?
Okay. Yep.
Okay, thank you, yeah, I just wanted to, to have a theory at the end of one, yeah, that makes sense.
**Jason Plumb** 25:27 We had a contributor in Android, I'm just remembering this by looking right now, we had a contributor in Android submit GRPC implementation, but it got stalled out. It's like, it's hung up, and they haven't come back around.
**Carlos Alberto Cortez** 25:41 Yeah, on that front, this is probably not related entirely to seek, but that's something I have seen in other SEEKs, that somebody comes with a PR and nobody takes that,
**Jason Plumb** 25:52 Yeah, there's this new thing that keeps happening, not keeps, but we've seen it more than one time now, where people come in with a very powerful hammer called AI tooling.
And they think that they can just submit PRs and, like, and they can't just, like, fling it and ignore it. They have to, like, help, you know, see it through, and… I feel like this might be one of those cases.
**Carlos Alberto Cortez** 26:15 Yeah.
**Jason Plumb** 26:17 Yeah.
**Carlos Alberto Cortez** 26:18 Okay, yeah, good to know, yeah, because I was actually wondering about that. I didn't check, and I didn't want to generalize, but in other reports, indeed, it's like, a lot of those PRs implementing some big chunk of work, it's AI, and it's not really polished. Didn't review that.
But yeah. Okay. Because, for example, you know that in Python, there was, I mean, we don't have to discuss that here, but they also wanted to support, OTSP JSON, And it took forever, but mostly because original author Having enough cycles to work on that, and at the same time, the maintainers grows busy.
So it's like, a situation like that, you know?
Yeah, I was trying to get, like, how often this is happening. But yeah, okay, good to know.
**Jason Plumb** 27:02 You know, Java doesn't have JSON.
**Carlos Alberto Cortez** 27:05 Right.
**Jason Plumb** 27:06 Yeah.
**Carlos Alberto Cortez** 27:08 Yeah, that's why I was curious, like, about this one first. I know, for example, JavaScript, I think that it's super important for them to have JSON.
**Jason Plumb** 27:15 Yeah.
**Carlos Alberto Cortez** 27:15 Yeah.
But other than that, yeah.
It's optional.
**Jamie Lynch** 27:25 Cool. Any further topics?
**Jason Plumb** 27:30 Not for me.
**Jamie Lynch** 27:33 Okay, we can leave it there for today and get a bit of time back.
**Carlos Alberto Cortez** 27:37 Yeah, perfect. So, James, you are going 6 weeks… 6 weeks away, right? Starting next week?
Or the week after? Next week, okay?
**Jamie Lynch** 27:45 Yeah, that's correct.
**Jason Plumb** 27:45 Yeah, so I can, I can run the meetings in that time, too.
**Carlos Alberto Cortez** 27:48 Great, that would be amazing, yeah.
Yeah, okay, so yeah, enjoy the time, and family, second child, if I remember correctly, so see you around.
Don't think too much about work, because you just take corporate time off.
**Jason Plumb** 28:02 Exactly.
**Jamie Lynch** 28:03 Yeah, I'll try my best.
**Jason Plumb** 28:05 Alright, cool. Cool. Thanks, everyone.
**Carlos Alberto Cortez** 28:07 So what you do.
**valexandrescu** 28:09 Have a good one.
**Carlos Alberto Cortez** 28:11 So…
