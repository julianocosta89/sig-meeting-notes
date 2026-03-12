SIG: CI/CD SemConv SIG
Date: 2026-02-03
Duration: 41 minutes
Zoom Recording URL: https://zoom.us/rec/share/H0pQOIeP716K9VpTYK4_n7cEPuQZ1bUv4qiqqoGdMwaPykFovtQ4KRRLSqN9WpI._DV9IUU0D0Jgv3kU
============================================================

## Zoom Recording Transcript

**Christophe Kamphaus** 00:24 Hello.
**Adriel Perkins** 01:15 Good day.
**neil yashinsky** 01:27 Microphone slash audio, Chuck, good morning.
**Christophe Kamphaus** 01:31 Good morning!
**neil yashinsky** 01:32 Hey, Christoph, how's it going? Good to see you again, or hear you again?
I think I was on the Symantec Convention's working group for, like, 5 minutes yesterday, and everybody was just very, polite and very quiet to the point that after about 4 minutes or something, 5 minutes, someone's like, wait, is my audio even on? And theirs was, but the guy who was talking was not, and it was… it was just a little, what do I call it? An anti-pattern, I guess, I didn't want to follow.
**Adriel Perkins** 02:09 We'll give everyone a few minutes to run through the dock. I would turn my camera on, except that it seems to be in its… Not working state again, which means I need to restart my computer, because drivers are hard.
Anywho, we'll give… we'll give folks a few minutes to update, and then we can get started.
**neil yashinsky** 02:30 Yeah, well, I'm sudden. Oh, no, go ahead.
**Christophe Kamphaus** 02:34 If I'm suddenly gone, then I had some issues with audio just a few minutes before, so you know my laptop might have crashed then.
**neil yashinsky** 02:42 I was thinking about the… Oh, sorry, Adriel, I didn't mean to interrupt. Go ahead.
**Adriel Perkins** 02:47 No, you're good, go ahead.
**neil yashinsky** 02:49 I was gonna say, I was thinking about the brain overhead of having my camera on, just sometimes it's like, I just worry about what it's showing, just candidly, and I hadn't even thought about the hardware overhead of, you know, running microphone and camera and all that stuff. I mean, I don't think these days it should be too much of a… of a problem too often, but, you know, here I am, wrong on two fronts in some ways, yeah.
**Adriel Perkins** 03:15 Yeah, I use, external mics and cameras, because I keep my MacBook in clamshell mode, so…
**neil yashinsky** 03:21 Interesting, yeah. That makes sense. I should probably… I've been pondering doing that.
I have a good keyboard, I just haven't found the right setup to use it as such.
**Adriel Perkins** 03:41 It's not for everyone, but it makes me feel like a podcaster, so…
**neil yashinsky** 03:44 Oh, that's double the reason to do it, honestly, yeah.
Very much less a vlogger.
You know?
Have a good setup for that, if you make you feel like a big boy or a big girl. Or at least for me.
**Adriel Perkins** 04:20 Sorry I wasn't here last week. Time got away from me.
I completely forgot to, by the time I remembered to post in the chat, I was, like… it was, like, way late evening, you know, I was like, well, you know, they figured I wasn't there, so…
**neil yashinsky** 04:36 Yeah, the time blindness is real, your struggle's real, you can say that, at least.
**Adriel Perkins** 04:40 Well, we can get started going through the board, as people enter any agenda items they have in the doc. Just on the front, of the SDK support for environment variable context propagation.
The Python PR has been approved. I'm just waiting to figure out if it's gonna be merged or not, but all checks have run, and I've got two approvals on it, so… That is… is good. Hopefully, hopefully we'll get merged soon.
**Christophe Kamphaus** 05:16 I've reviewed Alan's proposal for Go.
**Adriel Perkins** 05:19 Okay.
**Christophe Kamphaus** 05:21 There was some progress there.
**Adriel Perkins** 05:24 Awesome.
Was Alan able to get feedback from, the SDK owners on Go on some of his questions?
**Christophe Kamphaus** 05:33 Yes, he, received answers, and I think, And made good progress.
There's one question open about, And what was it again? Yes. If we extract… the context from the environment variables twice, and the environment variables change in the meantime. The spec says we should get the same results anyway.
So that implies we need to store it as a context at first load.
Globally or somewhere.
So…
**Adriel Perkins** 06:07 Is that still an open point?
Okay.
Well, I'll see if I can't… Read through that question, at some point this week.
To fully grok it for myself. But yeah, like, the intent behind the spec was certainly, like.
When the process gets spawned.
it's got a copy of, so if you're spawning processes, that's why we don't support it, right?
But if you're spawning a process from another process, then you should be passing that, into the dedicated. Because they're not, processes that are interesting, on the file system. So, yeah, I'll read through that, though. I appreciate the call out there. There is a, let's see, there is someone in the CCPP SDK that has started working on it for C++.
He's left some questions.
Or Dave left some questions.
I don't know the answers to them.
I think some of them are very C++ specific.
But, it might be good to just take a look at it from a… From a wider arching view.
**Christophe Kamphaus** 07:28 I think the part about limiting the length That's already in the spec, so…
**Adriel Perkins** 07:35 Yes.
**Christophe Kamphaus** 07:36 That should be part of it, and it's not in Go, if I remember right, in the Go implementation.
**Adriel Perkins** 07:44 Yeah, I don't know that it's in the Python implementation, to be honest with you.
I don't know if I added that or not.
I feel like I didn't, In part because… well… I think it's because of the… carriers that are supported, but I could be wrong. I need to, like, remember. I'll have to go look. But yeah, to your point, absolutely, the spec calls out the character limit. The… thread safety examples and the pointer examples for C++, though. I'm hoping that the C++ developers on the SDK chime in.
Chime in on that, so…
**Christophe Kamphaus** 08:34 No, for sure.
**Adriel Perkins** 08:36 But, you know, people are excited. I was actually watching… I didn't realize this, but I was watching, a KubeCon talk from Netflix that they gave over in NA, last year.
On… it's, it's called Where's My Pod? And about halfway through, they, they were, instrumenting the CNI directly, I think that's what they said, and the way they did that was through, by using the information from the OTEP, and they called out OTEP258, and was like, oh, that's cool! So there's… there's a lot of different use cases, for it, so it's nice to see it's, making progress.
**neil yashinsky** 09:14 Like, like that Leonardo DiCaprio meme or whatever.
You know, the pointing at the screen or whatever.
Sorry, I couldn't help myself.
**Adriel Perkins** 09:24 I don't know that one, actually.
**neil yashinsky** 09:26 I'll find it, so everyone can have closure on that anecdote, including me.
Thanks.
**Adriel Perkins** 09:33 I have not caught up on last week's meeting. I see that there's some notes that were talking about this, but is there anything that anyone wants to talk about with regards to CICD producing long-running traces?
**Carlos Alberto Cortez** 09:44 Yeah, I can probably provide an update since you were indeed not here. Basically, and actually, I was asking this group for their opinion.
Because the latest from the spec side, after this was discussed there, is that we will attempt to provide out-of-the-box, decorating spam processor that would be reporting what's happening with the spam? Like, so basically, you could be sending some events for start, end, and hoard tweet.
And there are some related things to do with that, which actually have a prototype based on something that Chris and Neummuller from Denatrace have.
But, his implementation wasn't that great, or he was trying to do both Batch Plus, plus actually doing the exporting. And, basically that's it. The question here is, like.
That's the… the desired way for the community after months of discussions, or years of discussions, along with providing SEMCOM for that. But is that something that would be enough for the group, or not?
**neil yashinsky** 10:57 Sorry, was that a question to the group, Christoph? I missed the very end, I apologize.
**Carlos Alberto Cortez** 11:02 Yeah, it was mostly for AREL, because, yeah, but yeah, it was a question. The question is whether that, like, that approach of having, log events reporting the life cycle of a span would be enough for this group.
**neil yashinsky** 11:17 disturbing.
**Carlos Alberto Cortez** 11:17 with, you know?
**neil yashinsky** 11:18 Thank you for repeating.
**Adriel Perkins** 11:21 What's, what's the, what's the perceived… Impact to observability backends as they exist today.
**Carlos Alberto Cortez** 11:31 Basically, that could mean that they could have to optionally support, events.
And then basically ingest those events that Are specific to, to a specific number of SEM comp.
Values that would be reporting that your lifetime is in flight, you know?
That's it, pretty much.
If you don't support these events, then you cannot be… you cannot tell the user that this span is still on flight, or, you know… Basically, what, like, for example, one of the cases there is that you are sending a heartbeat of a span analog with, you know, the trace ID and span ID. So, You, as a backend, you could optionally, like, be taking those pieces of information.
And now, keep track of them, like, these are happening, but they are not… they have been sent to me.
Because they are still in flight. So if you don't receive them, and you stop getting the heartbeats, then it's like, hey, I can report to the users that this spans Well, first of all, first of all, you could have reported that Span was in flight, and, like, they are in flight, they're not coming yet, but it's what's coming.
And then you could… If you stop receiving the hard beats, it's like, hey, these events, like, they crashed or something, you know, and send a report or something of those ones.
That's something that a vendor could optionally do, and then they could report to the users, like, what's happening. If you don't support it as a vendor, you simply… you wouldn't be impacted, but you could be missing this functionality.
**Adriel Perkins** 13:11 So… I guess, are we thinking that, like, So let's say, like, you know, a workflow starts, and an event is emitted that says it's started, right? Maybe that's one of the events.
Are we thinking that the backends would, like, create a span directly out of that event, and leave it open until the heartbeat event says, okay, now we've completed, or closed, or failed?
Or do you… are you thinking that the backends would, just create the span once all events have been sent?
after the effect.
**Carlos Alberto Cortez** 13:52 Yeah, actually, that's a great question, and I actually… I was actually wondering whether backends could use a collector to create such events, you know, such spans based from the events, you know, which could be the same or similar enough.
**neil yashinsky** 14:03 Right. That's…
**Carlos Alberto Cortez** 14:05 Yeah, that's a question, that's a question, that actually I would like to ask vendors, these days, I don't know what, like… I honestly don't know that any of them support these, and I think that mostly I haven't seen many vendors trying to offer these functionalities, mostly coming from the users, and I don't think they have spent some time thinking about that. That's my impression.
**neil yashinsky** 14:34 Agree.
**Carlos Alberto Cortez** 14:34 And my… yeah, and my impression is that they could be forced to think about that later on.
Yeah.
And I think that my impression is also that the only way to get the ball rolling, after years of discussion on this, is to get anything out there that can help… that can force users to… or people, or vendors, or both, to pay attention to these, you know?
**neil yashinsky** 14:56 Agreed.
**Carlos Alberto Cortez** 15:00 Yeah.
**Christophe Kamphaus** 15:02 So is the current spec… If we did something to create spams based on the events in the collector.
We could only do it after the span has finished.
**Carlos Alberto Cortez** 15:14 That's correct, yes, that's correct.
**Christophe Kamphaus** 15:18 So it would need to be in the backend itself, that they have an internal way Of creating in-progress bands and representing them in the observability backend itself.
**Carlos Alberto Cortez** 15:31 But there are ways in the collector to actually keep track, or, like, buffering spans, but yeah, probably the backend would be a better place for other reasons as well, you know.
**Adriel Perkins** 15:41 Did y'all discuss at all the, Dagger implementation of… in-flight, in-progress spans that I've not completed yet.
**Carlos Alberto Cortez** 15:55 No, we haven't. There was a related discussion on the issue itself in hotel, yeah.
about sending in complete spans, you know?
And there was initial agreement, for whatever reason, but this was 2021, I think, or 2022.
There was initial agreement on being able to support getting, like, incomplete spans in general.
And one of the pushbacks is that many vendors, back in the day, don't remember now, is that they said they don't support these update modes, they only support these append modes. And Jaeger was one of them, for example, you know?
**Adriel Perkins** 16:36 Yeah, I mean, that tracks. I think, like, the only one that I know of, really, that does it, that supports update is… is Dagger, and it's a custom implementation.
But I thought it was pretty nifty, just because from, like, the user standpoint, you actually, like, if you go into their dashboard as you're running, like, these… because they do stuff with agents and work… like, agent workflows.
If you go under their dashboard, you're actually, like, seeing the span in real life.
As it's… as it's tracked, which is actually… I mean, it's pretty cool. Like, from a understanding perspective of, like, some of these longer-running type things, especially in the Agentic world, it's pretty neat. So, are you all having more conversations this week on the spec side about this at all, or…
**Carlos Alberto Cortez** 17:24 Yeah, I was planning to do that today, but I… I had a prototype for this, which is very easy. It was just very small, but I haven't wrapped up the PR portion, because we need also to have all six implement these, you know?
**Adriel Perkins** 17:40 Yeah.
**Carlos Alberto Cortez** 17:40 Yeah, otherwise there's no point. So, yeah, I will grab that up, between today and tomorrow, that PR, and yeah, hopefully we'll have some discussions. I didn't make it for today, you know? Okay.
**Adriel Perkins** 17:53 I know.
**Carlos Alberto Cortez** 17:54 Yet…
**neil yashinsky** 17:55 Yeah, yeah, but the idea, of course, is to get the ball rolling, as I said before, because this has been in stock forever.
**Carlos Alberto Cortez** 18:00 And in theory, there was initial agreement on this, last autumn, but nobody has been working on that. And yeah, we need to get things moving, you know? So, yeah.
**Adriel Perkins** 18:11 Okay.
**neil yashinsky** 18:11 Is there a link in the August notes from what you described, Christoph? About the initial… Effort? Do you know? I would assume so.
**Adriel Perkins** 18:23 What do you mean, Carlos?
**neil yashinsky** 18:25 Oh, did that was Carlos? Oh, I apologize, yes, yes, Carlos, thank you so much, for keeping.
**Carlos Alberto Cortez** 18:30 Carlos.
Yes. I think we… I think we didn't. It's in the recorded… in the recorded call, probably, only.
**neil yashinsky** 18:39 Okay.
**Carlos Alberto Cortez** 18:39 Yeah, we should probably, yeah, or I don't remember whether we took notes, I honestly, I…
**neil yashinsky** 18:44 Maybe I'll send a robot or two and see if I can tease out a little of some of those details.
**Christophe Kamphaus** 18:50 itself, I put some notes from the SAMConf meeting on… actually, it was already from 2024.
In December.
**neil yashinsky** 19:01 Perfect.
**Carlos Alberto Cortez** 19:01 Right, yes, right, you remember now, yeah.
**neil yashinsky** 19:12 Oh, here, this 373 one?
No.
**Christophe Kamphaus** 19:19 No, the issue is number 1648.
**neil yashinsky** 19:26 Did you say it was in the notes?
**Adriel Perkins** 19:28 Is that in the spec?
Repo.
**Christophe Kamphaus** 19:32 I posted it in the chat.
**neil yashinsky** 19:34 Oh, oh, oh, I see, I see, I see. Thank you.
**Adriel Perkins** 19:36 Thank you.
**neil yashinsky** 19:37 What too many skirts.
**Adriel Perkins** 19:40 Oh, yes, this one.
So, I guess from the perspective of, getting the ball rolling, is your thought here that, like, we start with this kind of event approach, but we're able to actually, like, be… For a lack of better word, nimble, and iterate on changes, and potentially support, Different things as time moves on.
**Carlos Alberto Cortez** 20:16 Yeah, there's a blend, at least for now, yeah.
**Adriel Perkins** 20:20 Okay.
**Carlos Alberto Cortez** 20:21 One of the things that, honestly, it could be nice to have, but, it could be to have, like, once this… and I think that there's agreement on this one, and especially this… it could be an external… sorry, an additional processor, which means that it's an opt-in, so it should be relatively easy to have that accepted into the spec.
But it would be nice to have some, open source, or any vendor support that in Jager. I don't know, I don't think we… yeah, we could… we could try to persuade them, and to… so they… they start playing with that.
That could be also part of the plan, by the way, but that's, like, long-term.
Well, medium term, I would say, probably.
**Christophe Kamphaus** 21:00 They have an issue, I linked it also.
I think it's pretty long. I think they were just discussing potential ways of implementing it, but I don't see any recent activity.
**Carlos Alberto Cortez** 21:15 Yeah, exactly, that's the thing. I think that these days, they need people to drive that, implement that, mostly. Yeah.
At least there's, yeah, some discussion happening, instead of just, you know, No.
No, no discussion at all.
**Adriel Perkins** 21:36 Okay.
I'll look forward to your PR. I'll do… I'll try to do a, I need to write this stuff down for me, forget it.
Try to take a in-depth look, and kind of re… rejig myself on… on all the… implementation detail things, and I guess on the spec call, I'll try to attend that as well this week. I just stopped listening.
**Alan Clucas** 22:05 Can I ask some details of… so the plan is to have an event for start, event for stop.
Are… other… are we gonna have any other events for, like, It's Not Dead Yet?
**Carlos Alberto Cortez** 22:18 Well, yeah. Like a heartbeat.
Yeah, yeah.
**Alan Clucas** 22:22 is going to be parked there, okay, cool. And, Span events can also be part of, and A span that is being defined by events, is that correct?
**Carlos Alberto Cortez** 22:33 Could you elaborate on that one?
**Alan Clucas** 22:36 You can currently put events into a span, is that the name of them?
**Carlos Alberto Cortez** 22:42 Yes, Greg.
**Alan Clucas** 22:44 Lines in the sand.
**Carlos Alberto Cortez** 22:46 Yeah, the only problem, actually, with Span events is that they have been deprecated in favor of actual, like, events or logs outside the span.
**Alan Clucas** 22:54 Okay, I didn't realize that.
**neil yashinsky** 22:57 Yeah, I think.
**Carlos Alberto Cortez** 22:59 Yeah. Makes sense.
However, I was thinking, because in the company where I was working before, there was an implementation similar to this, and we were reporting other stuff, like, for example, if a user is setting an attribute, I think we were reporting that, you know? So you get, basically, All the visibility into what's happening in the span, you know, including set attributes.
Which could be useful, you know? So basically, you're actually getting Stuff that, you know, that is being said, so you don't… because having the hard beats, the start and the end is… can be kind of empty, you know?
And, more to your… to your point as well, there is an implementation from a company which is, somewhere in the issue, in the… not the issue that, Christoph posted, but the other one, the previous one.
in the spec, and they mentioned that they allow… and I need to check that, actually, but that can be probably as an improvement, that the user would be able to put any payloads in the heartbeat, you know?
**Alan Clucas** 24:05 a pay… okay, so… Payloads in the heartbeat.
**Carlos Alberto Cortez** 24:11 I don't know how that looks. I read about that now, now that you're mentioning that, into trying to provide more information, like, contextual, you know?
**Alan Clucas** 24:19 And in the current SDK for a span, you can set attributes late, because nothing gets emitted until the end.
Are we only gonna… how… when are we going to omit attributes in this model?
**Carlos Alberto Cortez** 24:34 I don't know, I think that that could be the plan, if users want that. I think that having a start, end, and heartbeat is a good start.
set attributes, if that's your question, like, whether we will be sending events, that could be the next thing, once we have the initial, portion in the spec, you know, as approved, and, you know, even if it's experimental.
Do you have any feeling yourself about how important it would be to have said attributes?
Calls, events there.
**Alan Clucas** 25:04 I… I… I know all my attributes that I think I need to know.
at the start of every span, so I'm, like, I don't care. And I'll know them at the end.
So… I was just… it occurred to me that that's a… it's a problem if you're representing a span at multiple points, what if they disagree on a value or an attribute? That's… Obviously nuts.
**Christophe Kamphaus** 25:29 At least identifying attributes need to be, stay the same.
**Alan Clucas** 25:34 Yeah.
**Carlos Alberto Cortez** 25:34 Yep.
**Alan Clucas** 25:36 Well, they say… presumably the idea… the thing that links all this… these events is going to be the span ID, and nothing else, because… If you try and link it by any other means, it's… All kinds of fraughtness.
That's not a real word.
**neil yashinsky** 25:54 I liked it, though, but I feel like, at the risk of being pedantic or whatever, like, but isn't baggage there? And not that you're saying that that wasn't the case, but aren't there other, you know, legitimate uses of baggage or what have you, annotation, etc?
To… to… to create that, whatever it is, traceability, not, you know, lowercase t or whatever.
**Christophe Kamphaus** 26:16 Package is for context propagation. So in the context of a span, you would have the span attributes.
**neil yashinsky** 26:24 And so.
**Christophe Kamphaus** 26:25 have the sampling-relevant attributes, where we basically recommend to specify them from the start, in case you want to decide whether to sample the trace or not, the span or not, based on those attributes.
**neil yashinsky** 26:39 I think I was referring… oh, thanks for stuff. I think I was… I was trying to refer specifically to, like, if you use a log event.
Instead of a span event.
Then, do you still maintain… what's the word I'm looking for? Well, I mean, I guess it's like, I guess it is baggage, but the ability to… to… trace back the… again, wrong word, you know, connect the dots of the… you know, in the same way that you could with span events with attribute mismatch, I guess. That's what I…
**Christophe Kamphaus** 27:14 You can use the same context as AnySpan.
**neil yashinsky** 27:18 Right, right. Yes.
**Christophe Kamphaus** 27:20 Those would also include any baggage attributes, so you could map the baggage attributes into log attributes.
**neil yashinsky** 27:28 Yes, like a propagate… I should have said propagation, I feel like, but… but yes, I think… I think you… you… thank you for… turning my thoughts into actual cogent words.
If that was possible.
Challenging mission.
**Adriel Perkins** 27:46 Just on the note of span events being deprecated, I'm… I remember seeing it.
I think one of the things I didn't correctly grok, or… Is whether or not, like.
the name span events was being deprecated versus the ability to attach an event to a span as being deprecated. Which one of those is it?
**Carlos Alberto Cortez** 28:10 the API call, you can still… you should be able to configure, in theory, stuff in this decade that actually tries to put the logs in the active span, if they match some information there.
Okay, so then…
**Adriel Perkins** 28:25 That still can be done.
**Carlos Alberto Cortez** 28:26 Yeah, correct. On the wire, let's say. Yeah, but not from the API side, yeah.
**Adriel Perkins** 28:31 Got it, got it, got it, got it.
**Christophe Kamphaus** 28:35 And in SAMConf, you would define events, which are basically named log records.
**Carlos Alberto Cortez** 28:43 Yep.
**Adriel Perkins** 28:45 Yep, and if you just choose to attach that to the span, that's up to you.
But can't be done through the API anymore.
**Carlos Alberto Cortez** 28:53 Yeah, it won't. Yeah, I mean, it's possible now, but yeah, it won't.
So I'm guessing that if we were to say we want to send, events regarding span events.
We will say… we will be told that no, because they have been deprecated.
But yeah, they're still working, but they will be. They will be gone.
I don't know when, but yeah.
That's.
**Adriel Perkins** 29:16 Yep.
**Carlos Alberto Cortez** 29:18 It's been…
**Adriel Perkins** 29:18 It's okay, it's okay.
**Carlos Alberto Cortez** 29:21 Yeah.
**Adriel Perkins** 29:21 Woliff.
Alright, thank you for that clarification. Anything else?
Y'all wanna talk about there?
**Christophe Kamphaus** 29:29 Yeah, just, to know… what you saw in DEGO, we see in progress spans. Do you have some references for that?
Because I don't see it linked anywhere on our…
**neil yashinsky** 29:41 Oh, shoot.
**Carlos Alberto Cortez** 29:42 Yeah, I think you shared that with me, in Slack, Adriel, but it's not posted anywhere, I think.
**Adriel Perkins** 29:49 Oh, you're right, I did. Okay. Good shout. I'll, I'll share that on the… I'll post that today, too.
**Christophe Kamphaus** 29:56 I'm wondering, do they directly transmit from their agent to their backend? Because then you… they can basically do whatever they want?
**Adriel Perkins** 30:05 Yeah, they own their records.
**Christophe Kamphaus** 30:07 Okay, so they don't use standard OpenTelemetry collectors in between.
**Adriel Perkins** 30:12 I don't know if they use an OpenTelemetry collector in between or not, but I definitely know that they're using the SDK from their Jaeger, I'm sorry, not Jaeger, but, within their codebase.
I will…
**Christophe Kamphaus** 30:27 Okay, it would be interesting to know how Isa implemented it.
**Adriel Perkins** 30:32 Yeah, it's, quite, quite interesting.
Yeah.
I'll… I'll post it. I'll post it.
But this is basically the code, in the SDK.
**Christophe Kamphaus** 30:55 I will take a look.
**Adriel Perkins** 30:59 I had, Cool. Anything else?
**Christophe Kamphaus** 31:16 Nope.
**Carlos Alberto Cortez** 31:19 Well, for now, yeah, hopefully next week, there's more information on what's happening there.
**Adriel Perkins** 31:30 Alright.
Awesome.
**neil yashinsky** 31:32 Good conversation, though, I really, I really appreciate, chatting that through, Adriel, with, especially about the semantic, span… sorry.
The span events slash log events, I think that's a… was worth chatting about. I certainly benefited from it.
Hopefully others do, too.
**Carlos Alberto Cortez** 31:51 Yeah.
**Adriel Perkins** 31:55 So those are the main two in-progress ones. We've still got the same to-do, and no status columns. Anyone's welcome to pick it up. There… I don't think anyone's picked up, this one, though. There has been offers to do it, or, like, it was offered to… Maybe it was this one, sorry.
I don't know, it was one of them.
now I'm forgetting things, so, it is what it is. But, anyone's welcome to just pick up stuff.
I don't see any other agenda items on here, so I guess, before we give the time back, is there any, like, open topic anyone needs to discuss that they just forgot to write down, or…
**Alan Clucas** 32:35 I can check with Christoph. I was gonna make the Golang, carrier… not use a global, because I don't think that's the right way.
and store it within the carrier, so that you can model… do what the Python one allows you to do, which is Break the… break the system if you actually want to, if you run separate carriers, but…
**Christophe Kamphaus** 33:00 Yeah, so you would have the option of keeping the same carrier alive for the whole process execution, and then it would be almost global.
**Alan Clucas** 33:09 Yeah.
**Christophe Kamphaus** 33:10 But if you recreate a new career, you could… Read the updated environment variables.
**Alan Clucas** 33:16 Yes, because the… I looked at the Python implementation, that… that… Explicitly does allow that second model for some, Some specific scenarios where it's sort of… Needed, so…
**Christophe Kamphaus** 33:30 Sounds good to me.
**Alan Clucas** 33:33 Alright, I'll put that in.
**Christophe Kamphaus** 33:39 Yes, I don't know if you were there at the start, we basically thought about the… length limit of environment variables. It's specified in the spec, but I didn't see it in the implementations.
**Alan Clucas** 33:56 No, I haven't done anything about it, I can do something about it, yeah. Okay.
Is that missing from other implementations as well?
I think it's.
So…
**Christophe Kamphaus** 34:14 I think the main Go propagator?
it basically uses the HTTP header and coding algorithm. So I don't know if they do any length limitation there. I think they limit it to a number of… Keys?
Yeah, I don't remember.
**Alan Clucas** 34:38 Okay.
We're not… are we setting the environment?
not…
**Adriel Perkins** 34:47 Maybe the carrier pattern?
**Alan Clucas** 34:49 The carrier could be used to set the environment if you've packed it, but, because I'm a… you can use it… you can provide… you provide your int go, you provide your own function to do setting, so that a setter can do whatever you like it to do.
But in general, that should be used to spawn a child process.
And be used to set the environment for the child, rather than… Setting your own environment.
If that's the question you were asking, which I'm not sure it was now.
**Adriel Perkins** 35:24 Yeah.
So the… the… look, I'm reading… rereading the spec on size limitations. I think the thing that we, made sure of was that we are not responsible for pro- spawning processes.
**Alan Clucas** 35:40 Yeah.
**Adriel Perkins** 35:43 And usually process… Process spawning.
Is when you set the environment.
like, you will, if you're calling, like, examples and Python, right? Like, it's, you know, os.
dot process, whatever, and then you pass in your environment variables there, right? Since that is not an SDK responsibility, that is a user responsibility, technically.
Technically, you could make an argument that the size limitation would need to be validated there.
Like, that's when you would want to make sure that your carriers Don't have, or, like, the environment variables you're setting are, within that size limitation for the operating system they exist within.
I didn't add it in the Python, I… we can definitely… talk about it, but I don't think we're respon- like… like, yeah, just because of how processes get spawned from within coding systems, I'm not sure if it's our responsibility or not to directly Make… ensure truncation.
And, let's see…
**Alan Clucas** 37:06 Is there ever a valid truncation?
It's either we're gonna fail, because we can't pass the information requested.
**Christophe Kamphaus** 37:13 He's back mentioned to… Truncated… at a full baggage variable. So you basically don't truncate in the middle of a value.
You just include, An, key and value, or a card of full key and value.
**Adriel Perkins** 37:36 Yeah, because it's following the W3C trace context, limit.
**Alan Clucas** 37:41 Alright.
**Adriel Perkins** 37:41 Verbage for that?
Entry should be removed starting from the end of the trace date.
But their entries are significantly less than ours, than, like, OS system.
limitations, right? Like, OS system limitations is, like, I don't know, $331,000 for… Oh, I should share my screen. Let me share my screen. Sorry, I stopped doing that.
on Windows, it's, like, 32,000, and on Unix, it's variable.
But, like, trace state limits, which I might already be handled by carriers, like… Like, 128.
Oh, no, that's wrong. Sorry, that's entries longer… larger than 128.
So this is the verbiage that it linked out to for that. I guess the question is whether or not we should make sure it's handled in the carriers or not.
**Alan Clucas** 38:49 I don't know.
Feels messy.
But somebody's gotta do it.
Well, that's the point of libraries, to do the messy stuff for you, so…
**Adriel Perkins** 39:04 You also have to put a ton of information in an environment variable to make it hit that limit.
**Alan Clucas** 39:09 Yeah.
**Christophe Kamphaus** 39:12 And then you would need to have a way of defining the limit that should apply.
**Adriel Perkins** 39:20 Yep.
And library… the library is, like, you know, really OS agnostic.
**Alan Clucas** 39:27 the Go knows what it's being compiled for, so it's… possible… well, you definitely know if you're being built for Windows, Darwin, or Linux.
**Adriel Perkins** 39:36 Yeah, for sure.
**Alan Clucas** 39:37 Those are the ones I… Build for normally, but… Yeah.
**Adriel Perkins** 39:53 I guess, how do we want to proceed on that? Does someone want to take, like, a stab, or do you want to take a stab at thinking about it in… in, in your implementation on the Go side, or…
**Alan Clucas** 40:07 I can have a look, yeah, see if I can work out what all the bits mean. Be good for me.
**Adriel Perkins** 40:14 Thanks for doing all the hard work.
**Alan Clucas** 40:17 That's right.
**neil yashinsky** 40:19 Yeah, it's good for it.
**Alan Clucas** 40:21 It feels like there should be, somebody somewhere should have already implemented The priming part of this.
Because it should be… If it's done for something else, then… trimming it correctly. Yeah, the truncation algorithm sounds unfun.
If it's not just a blind cut at 32,000 characters.
But somebody should have done that already, so I'll have to look for that.
**neil yashinsky** 40:50 I've had that feeling a lot lately, and I don't know… I don't know if I am right in the same way that you are right now, but you are definitely right now, that this is, like, something… And I think we all know, like, so many problems have been solved in isolation or whatever, and just people not ever got around to sharing it, etc. So it's like, yes, definitely has been done, but hasn't been done and shared in a way, like, an hotel-like fashion.
**Alan Clucas** 41:14 That's okay.
**neil yashinsky** 41:15 Slightly differently. Sorry.
**Christophe Kamphaus** 41:19 I would take a look at… the OpenTelemetry Co-SDK, the propagation algorithms there.
If they do it already or not.
**Alan Clucas** 41:31 Yeah, I will have a look at that.
It feels like if they've had to do it for… W3C, then it should be… Written somewhere.
Hopefully. I'm… I'm planning on that.
I'll tell you next week.
**Adriel Perkins** 41:47 Sounds good.
Alright, well, if there's nothing else, I'll thank you all for joining, and we'll see you next week.
**neil yashinsky** 41:54 Same. Cheers, everyone.
**Christophe Kamphaus** 41:56 See you.
