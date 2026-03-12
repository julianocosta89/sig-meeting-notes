SIG: Arrow SIG
Date: 2025-07-15
Duration: 13 minutes
============================================================

## Zoom Recording Transcript

**Drew Relmas** 02:33 Hey, Jake and Ukash?
Sorry. I'm just a minute late.
Let's see.
**Utkarsh** 02:43 No worries.
**Drew Relmas** 02:50 I know that.
Well, I believe both Josh and Laurent are on vacation this week. So we might actually depending on what topics everyone has. This might be a very short meeting.
**Utkarsh** 03:14 I don't have any topics.
**Drew Relmas** 03:19 Don't sorry, Jake, please go.
**Jake Dern** 03:24 Oh, I was just gonna say I did have one small topic. But please go ahead.
**Drew Relmas** 03:32 Well, I I'll share my screen and I can drive the Can I share my screen?
Oh, I've had zoom issues sharing screen as well on this machine.
Not too critical, I but you know we have the word, Doc as well. If you need anything, putting my name in it. Send the link again in the chat.
I didn't have any other topics besides something for for Laurent a question about the Boberg reference implementation that's sitting in the repo on, if we need to continue maintaining that in terms of like renovate and dependency updates. But since Laurence not here. I guess that'll be deferred.
I think they're I'm I'm not sure if he was, he's going to be able to join, but I know. Go, con. One of our other peers here at Microsoft had a topic about the cargo bench runs, but again without around. And Josh here, maybe not the best time to get an authoritative answer on that.
all that said, I guess, Jake, if you want to talk about your one issue, this would be a good time. I don't know who cars, and I can answer it, but we.
**Jake Dern** 05:08 Yeah, I I think I might be in the same boat as you. I think this is probably a a question, maybe for Albert or or Josh, or somebody, but basically, I'm I'm kind of kicking the tires on standing up a full o tap pipeline mostly using just the rest otap implementation and then just standing up kind of my own bare bones, you know, like very basic Grpc server that you know, with with the goal of exporting to parquet, basically but without, you know, necessarily taking a dependency on the the upstream, like, you know, full pipeline being ready to go, even though I know it's getting kind of close. Something I noticed was that there's not support for delta dictionaries within the the otap crate for rust.
And this is something that I'm I'm kind of looking to get in the short term. And so my my topic was going to see if if anybody was actively working on this, and if not the folks were were okay with me, taking a crack at it, but I I don't know if that's maybe a question for for Josh or Laurent, or Albert, or.
**Drew Relmas** 06:19 Yeah, at least. Personally, I don't feel prepared to answer that. Unfortunately. I'm not, you know. I I know they have a close idea of who's doing what in the otap flow? My best recommendation would be waiting Ukarsh, unless you know any different.
**Utkarsh** 06:38 yeah, not much. I don't think I can offer much help here. But, Jake, is this about the message that you also put on the Hotel Arrow Channel.
**Jake Dern** 06:49 Yeah, it's it's related. It's the same thing that I've been working on. I I was able to answer most my questions. There.
**Utkarsh** 06:55 Okay.
**Jake Dern** 06:55 Myself. But yeah, it's it's the same project.
**Utkarsh** 06:58 I I think, won't be able to answer the other general logistics part of stuff. But I think I have also tried something similar with like having a thread per core Syslog receiver. And I tried something of like testing something like that, and a few of the things that you mentioned in your chat, like the Arrow exporter, is establishing 11 connections. So that's basically you have your own test. Gc. Grpc. Server, and it sees that there are 11 connections made from that same process. Is that is that what you're referring to like.
**Jake Dern** 07:36 Yeah. Yeah. And I did find there's a setting on the the Arrow exporter for controlling it. I I think now my question is more of I'm I'm just curious, like, why, 11 and like, why is that the default? And also why is it the default to reestablish them every 30 seconds. I'm just trying to understand if it's like a an intentional thing that they found like is is actually pretty good and you maybe you want more than one connection, and maybe it's 11 for a reason. You know, like an odd number or something. But.
**Utkarsh** 08:04 Oh, so you saw, like the actual number 11, hard coded 11 somewhere, something.
**Jake Dern** 08:08 I think it's a default.
I didn't actually go dig to where it was coming from, but if I don't override it, it's set to 11. Yeah.
**Utkarsh** 08:15 Oh, weird cause I from what I know like I mean, if you're running that otap thing from the repo, then every thread depending on the number of cores there are, then you have.
Each of them would have an exporter instance running so like. If you have 8 threads, then 8 cores. Then you'll have 8 instances of the exporter running, and each of them would create a dedicated connection for themselves to the whoever.
**Jake Dern** 08:44 I see. Is that so? By, and you're talking about the the arrow export of the go implementation.
**Utkarsh** 08:50 No, I'm just talking about the the implementation in the repo. I don't know if there is a yeah, I don't know about the go go exporter. But yeah, like, with the current at least the threat per core design that Laurent talks about. And so they're like, the idea is that every depending on the number of cores you have, those many pipeline instances created one for each core and each of them will open or establish a connection for themselves. And so I don't know if, like, maybe the go thing is not doing that, so I can't say much about the go based export if you're using that. And then I also see something about like 11 connections ending up on the same listening socket.
So I had a similar thing in my Syslog testing, where I saw like, even though I had, like 4 different clients connect, trying to send to my Syslog server, I, and like my Syslog server had like, let's say, 4 cores. Only one of them was able to process these incoming requests, and because all of them were just going to that?
Is that something that you're facing like all.
**Jake Dern** 10:01 Yeah, it's it's it's the same thing, and and I think I don't know. I mean, I got my answer from from a robot. But it sounds like, maybe when you have multiple listening, sockets on the same port that the operating system just load balances between them. But the load balancing is deterministic, based on like the clients, IP and Port.
**Utkarsh** 10:23 Yeah.
**Jake Dern** 10:24 The servers IP important, so it'll just be the same.
**Utkarsh** 10:27 Yeah, that's that, is it? So? Yeah, I mean for me, I had to like use different client Ips to basically load, test my Sys lock server. Otherwise all of them, all of the requests are going to the same.
But yeah, you found that answer.
**Jake Dern** 10:45 Yeah, no, that makes perfect sense, and and on the like, you know, 11 connections thing. Now that you mention it.
I wonder if it's the case that the the hotel arrow exporter, the go implementation if it also creates one stream per core, because now that you mentioned it the laptop that I have it. It reports the number of cores that it has.
**Utkarsh** 11:06 Or is it Macbook? Is it cause they usually have like these.
**Jake Dern** 11:09 It's a surface book, but it reports as or it's a service, but it reports the number of cores is 22, and so like the the server implementation is my own but the client implementation. I'm just using the hotel aero exporter. And so I was trying to figure out why, it was making exactly 11 connections. I couldn't figure that out, but it could just be the number of like half the number of of threads that it's seeing that are available, cause that that could be one way to get 1122 And then the other thing that I couldn't figure out, though, is why reestablishing the connection every 30 seconds. I mean, there's another setting to to tweak that. But I don't know. I wonder if there's a reason to have it so short by default.
**Utkarsh** 11:51 Not bad, I don't know. Yep.
**Jake Dern** 11:52 Yeah.
**Utkarsh** 11:56 Cool.
**Jake Dern** 12:03 Yeah, I think that's it for for my topic.
**Drew Relmas** 12:06 If that's all good, then I will. Then we will just end here very early, and.
**Jake Dern** 12:13 Yeah.
**Drew Relmas** 12:13 Back, next time.
**Utkarsh** 12:15 Sounds good.
**Jake Dern** 12:15 Do you know, by the way, when everybody's back in office like.
**Drew Relmas** 12:19 I believe next week. To my knowledge.
**Utkarsh** 12:24 Yeah, Josh is definitely back next week at least. That's what his status says. But yeah.
Laurent, as well.
**Drew Relmas** 12:37 And Jake. Just so I accurately represent it. I was. Gonna I don't know if you're in the drive, Doc, or not. But would you be able to document the question and the best language that you can just on the agenda? So it's recorded that we talked about it.
**Jake Dern** 12:52 Yeah, absolutely. Let me. Yeah, let me put that in there. I'll I'll put the topic separately. The the implementation question, and then the question about adding support for the Delta dictionaries. Yeah.
**Drew Relmas** 13:04 Okay, sounds good. Thank you so much.
**Jake Dern** 13:06 Yeah, no, thank you.
**Utkarsh** 13:08 Thank you. Guys.
**Drew Relmas** 13:09 Great bye-bye.
**Utkarsh** 13:10 Bye.
