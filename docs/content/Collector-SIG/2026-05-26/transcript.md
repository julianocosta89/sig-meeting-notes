SIG: Collector SIG
Date: 2026-05-26
Duration: 23 minutes
============================================================

## Zoom Recording Transcript

**Blake Rouse** 02:37 Hey, how's it going?
**jmacdonald** 02:39 Hey, buddy.
This song, can you hear me?
**Blake Rouse** 02:42 Yeah, I can hear.
**jmacdonald** 02:43 Oh.
I'd like to come to these.
I'm not sure.
We have much for today.
**Blake Rouse** 02:52 Yeah, I didn't have anything either. I was just showing up to be here, so…
**jmacdonald** 02:55 Same, same.
I did review Andrew's PR earlier today, one that adds the, Extension for Scraper.
Controller?
And I was… if he was here, I was gonna talk to him about it, but if he's not, then I… I, you know, I gave him some feedback, so… that's cool.
**Blake Rouse** 03:18 See, he's online up there.
**jmacdonald** 03:19 a couple minutes, I will propose that we… perhaps don't have a meeting. If you have anything you want to ask for my help with, I'd be glad to try.
**Blake Rouse** 03:28 Yeah, let me just see, I'll ask Andrew if he was gonna join, Real quick, because, yeah, he normally does join this time zone.
**jmacdonald** 03:54 We just got back from a… well, U.S. holiday yesterday, so it's been a, like, kind of a slow day start with everything backlogged. Maybe affected other U.S. employees.
**Blake Rouse** 04:07 Yeah, I'm in the US as well, so yeah.
**jmacdonald** 04:09 Oh, you are? Okay, I… Imagining you are working with Andrew somewhere far away.
**Blake Rouse** 04:16 Nope, nope, he's not actually on my team, we're on separate teams, but, yeah, he.
**jmacdonald** 04:23 Are all the TRs that you have…
**Blake Rouse** 04:25 We worked together a long time. We worked together on Ubuntu, too, so I've worked with Andrew now, like…
**jmacdonald** 04:30 Are all your PRs in a good state, or need any kind of, review assistance?
**Blake Rouse** 04:36 Not mine right now. I don't know if you saw, but the RFC did get merged, so that was… that was good to see.
We can chat for a minute if you got time. I was looking at that… I know you reviewed that gate PR I was working on, where it was, like, the gates, and…
**jmacdonald** 04:52 Yep.
**Blake Rouse** 04:53 And there's one issue that I'm trying to understand if I'm overthinking it, or if… if this would work. So, the big problem I have right now with the gate system is that if there's a call, like a… like, some… an event going through the pipeline, right? They're just function calls, right? So it's just like a function call, and it's waiting for the return. So… What the gate does is that it calls the function, and, like, you can pause, and basically it prevents, basically, the flow of any events from continuing, but the current events have to return.
And my thought is, is that if you're in a state where you have, like, a batch processor, or you have, like, the export helper, and the export helper is in a retry loop, right? And, like, try and get these events out, and it's kind of blocked.
Right? It's gonna sit there, that pause is like a blocking pause, until either that finishes or returns an error. And I'm just wondering, like.
is that okay, or should I be really worried about that, like, that blocking amount of time? So I was thinking about maybe putting a timeout there, like, we'll try to pause and, like, give it, like, a timeout, and then if the timeout fails, the question is, what do you do then? Do you… just rebuild, like, tear it all down and rebuild? Or do you, you know, go fall back to the original design, where you just kind of stop what you need to start and restart? But then it's like, why do you have the gates for if you do that?
And then, you know, and then the other case is… you know.
it seems to be that, like, standard way the export helper works is that, as soon as you call to send, it kind of returns immediately. It doesn't actually wait for it to return. So I think in those cases, it's not a problem, but when you're in the… there's an option, I believe, to kind of be, like, in this, like.
And I feel like the file log receiver would run that way, because you'd want to know that your event From Elastic's standpoint, we want to know that the event is there before we say.
**jmacdonald** 06:52 Yeah. Update the plan.
**Blake Rouse** 06:54 and the file to say you've recovered the log, so it's very important to kind of have that, like, one-time guarantee.
And so I just don't know, like, what's your opinion on it? Do you think I'm, like, overthinking it? Do you think… We should have.
**jmacdonald** 07:08 Oh, no, no.
**Blake Rouse** 07:10 Like…
**jmacdonald** 07:11 I, in fact, I mean, my background with this group started with me getting into trouble with exactly this type of problem, and back a few years ago, there was no Feature that you, that you now know of wait for result.
We also didn't have block-on overflow.
So, that was a related matter. And then, I have a PR open that I'll, you know, I can share with you, because I want… I want… I don't need any more reviews, I just need to do more work on it, but I'll share so that you know some context for me.
I… I sort of became a prover in the collector over a year ago, mainly because I was passionate about the problems with batching, and had, for the OTEL Aero project, had written with a couple of people, this thing called concurrent Batch Processor.
And then I tried to write an RFC once, and now I have another RFC open a year later, because it moves slowly, but we're making progress. So the batch processor and the exporter helper were kind of coupled, like you just described.
Because the default was to accept and return quickly, it was fine that the batch processor had no concurrency. But if you wanted wait for result, you would break the batch processor.
And so that was related with Anyway, my interests.
So… I heard the basis of what you were saying about the gate was that when you close the gate, there's still active requests And if your… if your shutdown is blocked because of active requests, what is it really for? And as you know, there is a timeout in the exporter helper that's sort of default. However, I don't know what the file log receiver does as far as putting a timeout on its own request. There's no mechanism that we have Today.
that I'm aware of that's, like, a blanket deadline enforcer. Like, you must have a deadline on all requests back at the receiver, because otherwise my answer would be, you should… Consider the timeout.
when you're… when you're in that gate on the client side, like, you're gonna go into a… I assume… I can't remember the detail, but I think you have a channel.
And so, like, you go into a select statement on getting admitted to the channel, which means the gates open again.
Or waiting for your contacts to be canceled, which means waiting for contacts done, or whatever.
So that at least when the receiver sets a timeout, which the OTLP receiver for gRPC does by default.
Don't know whether HTTP does.
And I don't know about file log, but then you'd get, like, consistently controlled timeouts at the gate in case The gate doesn't open fast enough.
But… I… I… That's more or less what I… what I would say on the client side to do a deadline. On the server side.
You can get one from the exporter helper.
Which should help.
**Blake Rouse** 10:27 Yeah.
Yeah, I just… and so… and then I was looking at this one case where what I… what we could do is we could have the gate… when you call pause, it could… It could, you know, like, close the gate, allow the current ones to finish, and then after a certain time, if that doesn't finish.
it could cancel… so every call… every consume call has… passes a context. So it could actually cancel the context.
at the final timeout. The downside of that, though, is it creates a new context It wraps the current… it wraps the past context with the new context for every gate it passes through. And the overhead of that is not great. It's, like, it's going from, like, what I calculated in my current, like, no op one was, like.0001%, no allocations.
like, one picosecond of CPU time to go through this gate. But if we put in this context cancellation flow in there, it's like.
6X that. It's like, you know, an allocation and, like, a general, like.
based on small batching, if you like a 100 event batch, it's like a 6% overhead. Bigger the batch, smaller the overhead, but it is adding overhead through these gates. And so I was like, well, is it worth adding this context cancellation, where you could say, hey, pause the gate.
And then if you hit, like, a 5-second timeout, like, in the gate, and all the function calls don't return, then we just cancel the context, and that means… the canceling contacts means the callers get the error, and the exporters stop their work, which is great. And actually, the better flow, but the overhead Of adding that, Just for a case of a config reload seems high.
**jmacdonald** 12:18 I mean, there's all… there's already the cost of the gate itself, so… .
**Blake Rouse** 12:24 Just the cost of the gate right now is very, very small, and this is making it… Much higher.
**jmacdonald** 12:29 Is the gate implemented using a channel or a lock?
**Blake Rouse** 12:34 It's actually using atomics. It's a.
**jmacdonald** 12:36 Oh, okay, right, right.
**Blake Rouse** 12:37 double atomic game, right? The channel is only used when it's paused.
So, it's very low effort. When a pause occurs, the channel is used, because that's what causes the block.
right, of the colors. But when you're non-blocked in its flow, it's just too autonomous. It's too autonomic, so it's very low. But if we do it where you're using these context creations, it's creating the context.
**jmacdonald** 13:04 I understand. Yeah, there's at least one allocation there, as well as some resource in another thread somewhere.
to time you up. But I do think that if you set a timeout, it's the same as canceling. Like, that's just… they take care of it for you.
So you could, Those are just, like, you can tie the context together in a bunch of different ways.
That's… But it sounds like you might want to be able to, like… I remember the comment I put on, I think, on your RFC was that maybe just making an option to not use the gate everywhere, and only where you need it, and then what maybe you could also do is only where you have a… only have a timeout or a Cancelable… a newly cancelable context when someone asks for it.
Otherwise, you're… you'll just… Assume that the exporter helper is going to put a timeout for you.
I think.
**Blake Rouse** 13:58 Yeah, yeah, they export hell of a wood, but it's like a… if you're in that… what she said… I can't remember what you… I can't remember the option where, like… It's blocking batching.
**jmacdonald** 14:07 Oh, I see. So yeah, if you… It's up to, like.
**Blake Rouse** 14:09 5 minutes before you finally… like, it could take up to 5 minutes before it's… like, in the worst case scenario, it's 5 minutes.
**jmacdonald** 14:16 You're right, that's the default, and… and if you set… Block on overflow and wait for a result. Then you get this worst, worst timeout case.
Because it's a 30-second individual timeout, but the retry processor is enabled, so you get 5 minutes, I think, from there.
I would suggest, let's see… I don't think you need to add an additional mechanism in the gate. You should keep it simple and cheap, and basically tell the user, we assume either you have a downstream queue, which means it'll return success immediately to the gate, hopefully.
You should set block on overflow.
Or not, because if you want your gate to be quick, then walk on overflow, and you're going to drop some data during the switchover.
**Blake Rouse** 15:04 Correct.
**jmacdonald** 15:05 But if you set block on overflow, you'll… you'll delay the gate, which might delay the config change, which might create a big hiccup. And for live traffic, that might be a problem, but for file… file logging, you might… it's not a big deal, I think.
**Blake Rouse** 15:17 Right.
That sounds right.
**jmacdonald** 15:20 And then you say, if you really want that Behavior of having a timeout that will automatically cancel the gate cancel the request to reopen the gate or whatever. It's a good metaphor.
Then you would, set weight… Sorry, wait for result.
And then you get the timeout and the retry.
Behind the gate.
**Blake Rouse** 15:48 Okay. Yeah.
**jmacdonald** 15:50 In other words, exports.
**Blake Rouse** 15:51 I think, I think, yeah, so I think, I think the overall conclusion is that I was maybe probably over-complicating and overthinking the…
**jmacdonald** 15:58 Well, I had to think about it for a sec, so yeah, I think you're good leaving it out. On the client side, though, since you have the Atomic.
Yeah.
Yeah, you know what? I think you need to keep it low cost, and based on everything we just said, the gate's gonna respect the downstream back pressure. If you let it wait, it will. If you get the default configuration, it won't.
And the default configuration also is not the block, so you'll get failures and… If the queue is full.
when the gate… when the gate closes. Does that make sense?
**Blake Rouse** 16:34 Yeah, no, it makes sense.
No, that helps. I appreciate it. Thank you.
**jmacdonald** 16:41 You're welcome.
Yeah, my batch processor PR, just in case you want to take a look at it, I do have feedback enough to work on. Nothing new is needed. Hello, Andrew. Hello, Antoine.
**Blake Rouse** 16:54 Take a look at it.
**Andrew Wilkins @ Elastic Observability** 16:55 Hey, sorry I was late.
**jmacdonald** 16:58 Cool, no worries.
I didn't have much to say or to run a meeting with… meeting on. I mentioned earlier that I'd reviewed a PR of yours today.
And… I… I'm not, a hardliner on anything that was said there, but I had written that RFC trying to get some consistency, mainly to explain what I learned when I read the code.
For extension, and it occurred to me that the… you know.
one way of looking at it is these APIs are so simple, we're never going to change them, so it's fine to make every interface open. But if… if… Once you do that, you can never change it safely, unless you lock it down now, so… Just a few recommendations that I would be totally… you know, I recommend it, but I wouldn't stop you.
**Andrew Wilkins @ Elastic Observability** 17:48 Sorry, this is… you're talking about the scraper controller?
**jmacdonald** 17:51 Sorry, yeah, I'm sure you have more than one PR open. Yes, the scraper Controller Extension Implementation PR.
**Andrew Wilkins @ Elastic Observability** 17:57 Alright, so you left some comments, I'll get to them.
**jmacdonald** 17:59 I did. I think I did. I should have.
**Andrew Wilkins @ Elastic Observability** 18:01 No, I just haven't got to my emails yet. Thank you.
**jmacdonald** 18:03 Oh yeah, oh yeah, your first thing in the morning. Haha! Yes.
So yeah, I'd be pleased to help with that on Slack or whatever, after you read the… read through it, but it's pretty easy. You'll see… you'll see what I said.
**Andrew Wilkins @ Elastic Observability** 18:17 Cool, thank you.
**jmacdonald** 18:23 Hello, Antoine. Do you have any pressing items? Usually, we've skipped over the triage at this point.
**atoulme** 18:28 Nope.
**jmacdonald** 18:29 And, it's just been the four of us.
**atoulme** 18:31 No, I don't have anything for y'all, but you should know that, next week at 8am Pacific Time, so a bit of the night for Australians.
There will be an update on a project given by Alex Button regarding Collector $1. This is a bit of a new ceremony now. The maintainer's sink is going to be used to help, kind of, organize status updates for different sigs.
I went.
I think a week ago?
To talk about the packaging SIG, which is new.
Just to make sure it was top of mind for people, and now we're doing this for Collector, and then we'll just make sure everybody kind of gets a turn. I think it's very healthy to do this type of stuff.
So if you have anything that you think you would like to contribute, or if there's anything that you think is missing, Let me know, or just go to Slack and… Ask hard questions.
That's the situation.
**jmacdonald** 19:29 Thank you. You know, I have, so I think I missed a little bit, because my volume wasn't up quite right, but I think you said next week, Tuesday, June 2nd, I believe, there will be talk at the specification SIG, Which I think is really hard for Andrew to make, but Blake could, and I will be there. And I'm glad to hear it. I think that was discussed today as well, that that would be next week. For the record, the O'Til Arrow project that, I've been working with over in the other AeroSIG, is going to try to present on June 9th, because we've reached the end of our Phase 2, more or less. It's, and we'll get a performance, report and a… kind of what we did, June 9th, by Laurent on the project.
**atoulme** 20:18 Cool Good idea.
Aye.
Looking forward to it.
**jmacdonald** 20:22 Thank you. I'm also, just by the way, really excited for the packaging SIG. Thank you for, you know, taking that effort up.
**atoulme** 20:30 Thank you.
Right now the collector is not quite in phase one. We… we just want to make sure we get the injector right.
But we, we'll try to… if you're interested, it's in the community project, there's, under projects, the packaging.md, you can read about it.
Very… I'm trying to find a good convention to create a structure of dependencies and meta-dependencies for people to be able to use this and swap packages with a vendor package of choice for some of the stuff.
So there's some good discussions happening under the OpenTeometry Packaging SIG. That's also something that we meet early in the day, Pacific time. Sorry, folks, because we have a lot of Europeans working on this, so right now we're trying to make them happy.
So… yeah, that's… that's ongoing. It's very early, I just put up a submission for KubeCon to go talk about it at some point, so maybe, maybe it gets accepted.
**jmacdonald** 21:32 Cool. Congratulations. I'm putting a link to the… Packaging, project definition.
**Andrew Wilkins @ Elastic Observability** 21:40 Sort of tangentially related to packaging, there's a proposal in the Open Symmetry Collector Core repo for adding SD Notify support for SystemD, and the proposal is basically to make OTel Collector a bit of a better citizen in SystemD systems.
If anyone's interested in that, have a look. I can link it in the… in the…
**atoulme** 22:07 Yeah, this one. We're doing something special for Windows already, because the collector can run as a service there, so… seems in line with the approach.
I think we serve… I think our RPM right now already has this service file, even though it's very simple.
So, that makes a lot of sense.
**Blake Rouse** 22:35 The meeting y'all were talking about on Tuesday, which collector meeting is that? Call meeting?
**atoulme** 22:40 The collector meeting, it's the maintainers, sync meeting and specification meeting.
Supposed to be a good place for maintainers to kind of get a… a feel for, where things are at, and the TC is organizing and maintaining that meeting.
Oh, okay. So it's a, it's a… Supposedly, everybody.
**jmacdonald** 23:10 I'm putting a note about that.
**atoulme** 23:15 Yep.
That's it.
Looking for that.
**jmacdonald** 23:20 Thank you all.
Thank you. I'll see you next time.
**atoulme** 23:24 Have a good… good day.
**Andrew Wilkins @ Elastic Observability** 23:26 Catch you later.
