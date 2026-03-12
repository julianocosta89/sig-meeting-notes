SIG: CI/CD SemConv SIG
Date: 2026-02-10
Duration: 40 minutes
Zoom Recording URL: https://zoom.us/rec/share/hTT2l9hc85-TH5TzLTq2jCYzPMz_QpvkoE5JBI4sidZuDnei4Nw3--I8-EXM3G8p.EKgTQe7X7M0THfCI
============================================================

## Zoom Recording Transcript

**Dotan Horovits** 03:38 Hey, Ellen.
Morning.
**Alan Clucas** 03:43 Hello.
**Dotan Horovits** 03:43 No, I'm.
**Alan Clucas** 03:44 Afternoon for me, morning for you.
**Dotan Horovits** 03:46 I'm not… yeah, I'm also, your time zone, I'm just used to, the folks in the US, but, Yeah. How's it going?
**Alan Clucas** 03:56 Alright, yeah.
**Dotan Horovits** 03:58 You know about, only today.
**Alan Clucas** 04:01 Yeah, I haven't seen anyone else. I was about to log off, but I thought I'd give it till 5 minutes passed.
**Dotan Horovits** 04:08 Yeah, I know, apologies for being late. I'm also, traveling, actually, on my way to a doctor's appointment. This is why I'm also without the camera, and also unable to share the, the screen or lead the meeting properly, so, I guess if it's just the two of us, maybe we'll, Heh, we'll call it off for today.
Yeah. Did you have anything in particular that you wanted to bring up?
**Alan Clucas** 04:36 No, I don't have anything, specific, I was just, showing my face and seeing if I could… help at the moment with anything, rather than… I haven't made any progress on anything over the last week, so, Apart from internally getting tracing into a good state for other workflows. So, yeah, I'm hoping to have a PR up for that.
but yeah, that does not include any SEMCOM… Conformance yet, but…
**Dotan Horovits** 05:05 Oh, okay.
**Alan Clucas** 05:05 yeah, it's just trying to get something in, and I call it beta, and get it out the door so people can give me feedback on what I've done, which can then feed back into, you know, SEMCOM and stuff.
**Dotan Horovits** 05:20 No, no, it's definitely an important step in its own right, and as a step leading up to SEMCON, so glad to hear the progress, and also on the opportunity, also, congratulations for getting your Well-deserved, recognition as an OpenTelemetry contributor. Sorry for my late, response, but sounds like you're, you're anyway good to go. But, really happy to… really happy to see that. I was also chatting about that with Christoph, I forced them, and, yeah, really good, good news for, for you and for, for, for the team. So, happy this, went through.
**Alan Clucas** 05:59 Yeah, thank you, that's, it's great. Yeah, pleased with that one.
**Dotan Horovits** 06:03 And also saw you, you got some, a talk that you're going to deliver, right, at KubeCon, in Europe, in Amsterdam?
**Alan Clucas** 06:11 I'm…
**Dotan Horovits** 06:11 Is that the, is that the, project update, or is it something else?
**Alan Clucas** 06:15 I think I found another victim for the project update, so I'm gonna do… well, I'm gonna give a KubeCon lightning talk on, like, the state of workflows, and I'm giving a specific talk at ArgoCon.
on… what is it? Artifacts, plugins that we've implemented.
System 4.
you to bring your own artifact drivers to other workflows, and so that's what I'm going to talk about, yeah.
**Dotan Horovits** 06:43 Nice. No, it's great, first of all, very difficult to get, talks in in general, and, you're definitely an authority there, and, ArgoCon is your, Go home turf, so.
**Alan Clucas** 06:57 Yeah. It's a good thing to, to have.
**Dotan Horovits** 07:00 I'll be at, Observability Day, probably, on the Colo Day, so I'm not sure if I'll be able to pop by, but, definitely looking forward to, catching up when we're there.
Yeah. Either at the colo or the main event, but, it'd be great to catch up.
**Alan Clucas** 07:15 Yeah. Aha, we've got some more people.
**Dotan Horovits** 07:18 Oh, okay.
Nice.
**Alan Clucas** 07:21 Hi, Alan. Hi, Alan.
**Dotan Horovits** 07:23 Hey, Neil, how's it going?
**neil yashinsky** 07:25 Good, you're safe.
**Dotan Horovits** 07:26 I don't know if Safety College is also here.
**Carlos Alberto Cortez** 07:30 Hey, hey!
**Dotan Horovits** 07:33 Hey, how's it going, folks?
**neil yashinsky** 07:35 Very good.
**Carlos Alberto Cortez** 07:37 Good, sweet.
**Dotan Horovits** 07:40 Great. Glad to have you. We're just about to wrap up and started chatting about KubeCorn and non-related stuff, because we were the only ones there, and and I'm also, On my way to the doctor, so I can't really share the screen, I'm in the car.
to properly lead the, the.
**neil yashinsky** 07:57 Anything there.
**Dotan Horovits** 07:58 But, if there's someone that wants to, to take the lead, we can maybe do that.
**Alan Clucas** 08:08 Screen sharing for me is… very difficult, unless I've pre-prepared.
**neil yashinsky** 08:13 I can… I can share my screen, I just… I'm not gonna offer value on the content, but I mean, you know, it's still so new.
**Dotan Horovits** 08:20 No, no.
**neil yashinsky** 08:20 I can share the screen, I mean, it seems like it's a bit of a formality if we're getting ready to wrap up anyway. Let me narrate the screen for a moment, and then, if there's anything you want me to click into, if you will, or show on screen, I'd be.
**Dotan Horovits** 08:33 No, the regular brief is… I think you attended at least one time with us, right? You know, it's not a few of them, but usually we do triage, so, I think we're less equipped to do that at the moment, and then, topics that are around the table, so maybe we'll jump straight to seeing if anyone has any particular updates to share, or topics that they wanted to bring up. I think this would be a good point now that we have all of you folks.
Anyone have any topic to suggest for the agenda?
**neil yashinsky** 09:07 I do not.
**Dotan Horovits** 09:09 Okay. Carlos, anything on your end? Any updates?
**Carlos Alberto Cortez** 09:13 Yeah, probably something that I was discussing in the last two weeks. This is regarding long, long-running spans, and how the specification group has been trying to, you know, come with a solution with that. The chosen solution being, for the time being at least.
That you actually have some, decorator processor.
**Dotan Horovits** 09:39 Sorry to interrupt, just one ask, maybe, if, either Neil or Alan, could you… would you mind taking the notes on the… this is an important update from Carlos, and I can't really take if any one of you is able to, just, type it into the shared doc for today's meeting, and, we can capture that.
Thanks, Neil.
Sorry, Carlos, please go ahead.
**Carlos Alberto Cortez** 10:02 Yeah, so, actually there is a reference to that, issue in the last week, or maybe two weeks ago, like, issues. Oh yeah, it's somewhere there. Anyway, I can paste that. But basically, one…
**Dotan Horovits** 10:18 Yeah, we talked about it, and you wanted to take it with the, with the team and, check it, so, yeah. We have the open item, yeah.
**Carlos Alberto Cortez** 10:26 Yeah, so essentially, one of the interesting things is that, There are a few challenges there, I think to solve, but one of the things that I was thinking is… And maybe, Alan, maybe you have specific, Context on this.
But… Essentially, when you're doing this, you want to get as much information from the span as you have at the moment, which basically means that you kind of are… Serializing the entire span and sending that as an event.
Is that… is that correct? I don't think that… I can totally imagine that having information during the hard bits, for example, of all the query attributes would be important. Like, all the attributes, all the events, like, literally everything. Even if that's, like, a lot of information to process, but you would like to see everything.
**Alan Clucas** 11:21 I would certainly like, yes, I mean, my long-running… in general, I feel long-running spans are more likely to contain valuable attributes than shorter ones in a CI or a workflow-based context.
Yeah. They are the, like, there's going to be one for the workflow run.
whatever it is, the CI run, and that's going to be… contain all of those like… all of the input parameters, you know, what git commit are we dealing with, or what, you know, where were we triggered, what workflow are we running at this… at this stage? You know, all of that information is… needs… To end up in the… In the user's display.
If… at some point, because even if you… even if you've got the span, you know, the top-level span is stored in the workflow, you can get to it from the workflow, you still want to be able to query the other direction.
Because it's going to be held all workflow runners persist their data for a while. So you can go and get it from the source in a way, but you do need some way of getting back to the source.
**Carlos Alberto Cortez** 12:35 Yeah.
Yeah, that's what I was thinking, because initially I saw some prototypes, I don't know where… but that could include, like, general information about the span during the, start span event.
But then, during the hard beats, you could get a span context in identifying that span and intricity.
But not necessarily all the information during the hard beats.
And that can be, of course, an overload of information, but probably that's something that you require. And if otherwise, there, you know, like… it's like, you know that Spanish started? You know how it look… how it looked at the start?
And then you know it's still running, but you have no information about any update, you know?
Which can be a problem.
**Alan Clucas** 13:21 Yeah, I mean, I… for my case, I know all the information at every stage in the span, so at heartbeat, at start, at heartbeat, and at end, I could emit all the attributes, so it doesn't bother me, and I can imagine that's the case for Any implementation?
because, as I say, they're going to have a store, so if… If a long running span is the only point at which you can add… well, no, you want to be able to add them… if you want to be able to query whilst it's running.
you… And you don't want to load it… the start is the obvious point to put them in, because if we're not gonna transmit them in every heartbeat and at the end, then the start is the joining point. I don't mind. I mean, we could transmit them at every heartbeat as well.
for… I don't care, honestly.
**neil yashinsky** 14:18 like… And I'm so new, I really hesitate to answer here, but I do think, like, the… I understand the challenge if I do, which is kind of like, there's really… I feel like, in a process standpoint, not a trace standpoint, there's a parent and many children that you're trying to keep track of, right, through this long-running trace is happening. Is it… can we say with certainty that it's within a single process?
Or could it be, because it's a CICD task, there's, like, other things that it's calling as well? You know, it's… it's… has, what's it called? Operations delayed by some other process that maybe it spawned or itself?
**Alan Clucas** 15:06 Certainly for me, I do not expect to transmit all of the span events, for long-running spans, from the… a single long-lived process. I will definitely want to restart. That was my original problem.
**neil yashinsky** 15:21 was I tried to use the SDK, and I can do it as long as my controller runs for the entire length of.
**Alan Clucas** 15:27 time, but I expect my controller to restart. That's… I'm dead.
**neil yashinsky** 15:31 Right. Yeah, so I guess that's what I'm, again, from the layman's perspective, trying to figure out if there's a… if there's a hierarchy of tasks, in a sense, that with good baggage and or exemplars, you can… you can find what you need to find.
Without duplicating all the details in every event heartbeat, or what have you.
**Alan Clucas** 15:52 Hmm.
**neil yashinsky** 15:52 and with proper correlation, or, I don't think that's the right word, Well, maybe it is, it'll work, but being able to tie in the logs and the traces… together across the processes, I think, should give you what you need without having to send a bunch of chatty data all the time. I imagine, or in my mind at least, it seems that… creating that… hierarchy, parent-child-esque thing, it would be the best way to go, because you can still get all the details that you want from the process that's running, and be able to correlate that back with the… With the thing that you kicked off that's really, like, the thing that's taking a long time to run. Maybe we need an example or two here to help flush this out. Does that make sense, at least, what I said?
**Carlos Alberto Cortez** 16:45 Yeah, I would say that in that regard.
the way to find, let's say, the span topology, that can be done with the span context, which is not a big problem, and then you have, like, many events, and then, you know, you can correlate that with the logs.
I would say that the big problem is sending all the attributes, you know, and all the events, even though they are deprecated now, the span events, but it can still be too challenging, you know?
Yep.
**neil yashinsky** 17:15 Oh, I was just gonna, I was just gonna ask, would it be difficult or impossible, or is it a matter of implementation to do those instead as log events, instead of span events? Or logs, I guess.
**Carlos Alberto Cortez** 17:24 Oh, that's a different question, but I would say that, well, basically, span events are deprecated, so… Right. They are the same as events, so now, most of the events will have no… most of the actual spans won't have events.
**neil yashinsky** 17:38 Right. Only it's for legacy reasons.
**Carlos Alberto Cortez** 17:41 So, we can forget about them for the time being. Okay. She could be… she could be mostly attributes.
But I don't remember seeing spans that have, like, hundreds of attributes.
And that's kind of the point, you know? Like, if you're sending… and every second, let's say, one option is that you only send the upset, but that means that you keep track of the differences, which can complicate such processor very fast, yeah.
Other… the other thing that we could do, like, other things have done in the SDK is that we just provide a Boolean value, like a setting is, like, send me… send me the bare bones in each heartbeat, or send me everything, you know? And that's why I was asking, maybe, like, how important it is how, like, having all the attributes, you know? There are things that are small, like, for example, span name, you can just send that, you know, in case it was updated. Span context doesn't change, so it could be very, very compact, you know? The only problem is the attributes, mostly, yeah.
**neil yashinsky** 18:45 Yeah, I… Oh, I… I want to make sure I'm not cutting Alan off, because I… But I was… I was thinking that… In many senses, the most important thing is less about How you send it, and more about how you find it.
Because you can easily create so much data that you'll have everything you need, but finding it becomes more difficult because you've been, if you will, exhaustive. And so that's why I was wondering if the right balance of, like.
logging things, rather than, like… if you're… if you're simply tracking, like, counts or whatever, like, maybe you… maybe you need a metric so that you are deriving that value from the log, and now you're incrementing the thing, so you don't have to… You don't have to put the load on the client, if you will, to aggregate any of that information. You can just extract it, metrics from the logs.
And that way you can… you know, the key pieces of information that you need to track for the health of these jobs, I feel like… Can be readily… derived from… from the log events into metrics. And so, that way, you… you can still have everything you want, I think, packaged together, but you're not… Overloading the sending of the data.
Which, in and of itself, is not so important, more of the inferences of the results, if you will, that the data shows. And so that's why if you can… if you can… You know, generate the right metrics from those log events, then you'll be able to see, you know, how long this has been running, or how many, you know, how many whatever parts of the job, you know, that'll be all readily accessible within the… within wherever you're querying from, it'll just be… your query will not rely entirely on… on traces and span events or span attributes. There'll be some metrics in there along the way, and some logs in there along the way.
**Dotan Horovits** 20:46 Carlos, I actually wanted to… so you started with a question after checking with the team about the… so how heavy, the stands are going to be. Is there any… first of all, I guess two questions. One, do you see that… more, I guess, present in long-running spans than in regular spans? That creates, because this is obviously, obviously, the heavy spans are a general problem that we need to address, but just trying to go back to the context of long-running spans, and secondly, were there any other types of feedback that, that you would like to share from the, from the Thank you.
**Carlos Alberto Cortez** 21:26 No, that could be all, like, how heavy… How… I mean, based on the fact that hard beats can be heavy in this context, like, how useful it is… how required it is, you know, to get all that information, instead of the bare bones.
That's mostly a thing for now.
**Dotan Horovits** 21:45 Okay, okay. I think it's a good point, and maybe we can even comment that on the, on the, on GitHub.
To maybe solicit some more, more commenting and more, opinions about what's the… what… what would be considered, I guess, the, the bare-bones baggage required. Obviously, Alan provided us with some initial thoughts from his end, but to make this discussion go beyond, I think this would be a good, good idea.
**Carlos Alberto Cortez** 22:19 Yeah, I think that… so, basically, bottom line, I am trying to prepare a PR for the spec.
Okay.
Basically, this could be marked if accepted, and it should, because it was initial agreement in the spec group.
as acceptive, but it will be experimental. So we still have time to… to iterate on that one. But down the line, I want to keep, you know, getting feedback from people. Probably we'll need some actual backends to implement support for this.
Before we go stable, so we can see how that would, you know, look. But yeah, anyway, so, there's time to discuss that, but yeah, I just need, like, this to be on the back of the mind of people here, so, you know, when they see something related.
**neil yashinsky** 23:06 Yeah. Oh, sorry for interrupting. Oh, go ahead, Dosan.
**Alan Clucas** 23:11 So, is your…
**neil yashinsky** 23:12 Sure.
**Alan Clucas** 23:14 I'm sorry.
**neil yashinsky** 23:16 We don't.
**Alan Clucas** 23:16 Question, really, around whether Those attributes can change.
or be… Appended to… more than… more than just the quantity of them? Is it… is the worry over updating attributes or… or anything like that?
**Carlos Alberto Cortez** 23:38 No, the worry is that you are, like, even if you have, like, let's say, a few attributes, and they don't change, you keep getting them. And if you have, like, more than, like, a few dozen long-running spans, you are basically sending too much information.
Which is fine, if it's useful, you know? But many times… and actually, that's probably… that takes me to the next question, which is a long… how often long-running spans get extra attributes?
Now, now that span events are going out of spans, you are not supposed to be getting Spun events.
what attributes, I don't know. Actually, that's a great question. How often do they change, and how often do they offer value, you know?
**Alan Clucas** 24:24 What we… so the… the SIG has… Documented what attributes we want on CICD, which mirror those… so there is also a SIG proposal to make them less CICD-specific, which I think I… I need to… Contribute to, because that's… Workflows is not a CI-specific tool, so my… my… my specific interest is around something that runs workflows for many different purposes, so I… I support the idea of trying to migrate from CI-specific to CD-specific, but there aren't that many CI-CD-specific attributes, I definitely don't think I need… I could certainly live with them being fixed in time, and I don't care.
when they get emitted. And so for something like the GitHub version, or probably the Jenkins version, having used both of those tools.
in quite a lot of anger, quite literally sometimes with those ones, then I, I think they could all… they all have all the static information.
a single point in time that they could emit it. So if what we wanted was that we can log a start A heartbeat, and an end, and one… At one point, bind the attributes to that span.
I could certainly live with that, and I think everybody could. If that point was flexible, that would probably be for the the most flexible, but I think if we can't… if we're not allowed to… I can understand trying to… The idea of turning a bunch of events into a long-running span And to be honest, there aren't that many of them overlapping… no, there are. There can be a lot of them overlapping in time, but they tend to be… because they're long-running, they also are long. So you… you have… there aren't going to be As many spans in flight as there would be, for example, or as many spans to look at as there would be for some Web events, where there's huge numbers of very dense spans.
**neil yashinsky** 26:42 You know, there's not a lot happening, but what is happening generates a lot of spans.
**Alan Clucas** 26:47 Yeah, so these are… these are generally much more sparse, even though they are… In times, time… thoughts, and so there are far fewer spans from the beginning to the end of, you know, in a one-hour period, we're going to generate far fewer spans in a CICD context than we are in a… in a busy web service.
And I'm expecting for most users, they would not want to.
Drop many spans because,
**neil yashinsky** 27:17 most of them turn out to be useful. Right. But yeah, I think I'm… I'm saying we can… we could…
**Alan Clucas** 27:23 We could annotate one of these spans at one point, and that would be my favourite, so that there's no need for the back-end processor to try and work out from this sea of attributes, what one is to present to the user.
**neil yashinsky** 27:38 Yeah, because I think… oh, go ahead, Carlos.
**Carlos Alberto Cortez** 27:41 No, no, I want to say that that makes sense. So yeah, I think that that's a good, compromise for now.
**neil yashinsky** 27:51 It might be nice, one, I guess, request that I have is, Carlos and or Alan, if there's, like, a poster child, I don't know if that, that, that word translates, well overseas, if there's, like, an ideal candidate job that would be useful for us to kind of use as a straw person to, like, hey, we're tracking long-running span A, you know, A does these things.
You know, just to kind of have some specifics that we could work around for the types of use cases that this should cover.
That would help me, at least.
**Alan Clucas** 28:31 Yeah, I mean, we've got the implementations of GitHub and Jenkins, and… that's our GitLab one, and I've got my one, which is a… draft PR somewhere that you could look at if you wanted to, but I'm… that's why I'm coming to the meetings, to digest…
**neil yashinsky** 28:47 to deliver.
**Alan Clucas** 28:47 my feedback, rather than somebody having to look at my code.
**neil yashinsky** 28:52 Right, maybe just post it here or in the notes or something, just for people who wanted to come and contribute, can, like… it's more readily accessible.
**Alan Clucas** 28:59 Yeah, at the moment, I don't deal with the long-running spans, apart from attempting to… well, because… for each… for each run of my work… for each reconcile on the workflow, which happens, like, once every 10 seconds or something, I have to… re… Conjure up which band, which is in memory.
is associated with my span that I'm currently running, so that I can, like, reattach my Go context to it. So yeah, I can… I can provide you a link. I'll pop that in too.
**neil yashinsky** 29:34 Yeah, yeah, I mean, honestly, I was most concerned with Carlos, because he seemed to be… well, I mean, both. I don't want to give preference, but yeah, I mean, I think that would be… it would just be useful, like, rhetorically, I suppose, to have, like, here's the example that we're talking about.
You know, here's the… especially because I feel like, early on, I was offered advice about cardinality, that, as you said, Alan, may not really be the… it's not unimportant, but cardinality in the context of a CICD pipeline, because you're gonna have… fewer numbers of jobs, and thus fewer job IDs, the cardinality profile is just gonna be different than what I was thinking about, so… it was really my bad, but…
**Alan Clucas** 30:12 We… we… I think we, as CICD SEMCOM, have accepted that for some attributes.
There will only… those attributes will have very high… or those… that type of span would have a very high cardinality of basically one per workflow run, which sounds high, but because, you know, even a really busy CICD system is going to be running at.
Yeah, in the tens of thousands an hour, rather than the millions an hour.
it's a different scale underlying. Right.
So you're still… you do want One of your attributes to point back.
uniquely to the workflow run that's invoked it. You… we ask for the SHAR for the Git commit that invoked it.
And those are necessarily unique.
**neil yashinsky** 31:10 Right, right. Yeah, I mean, it's a value trade-off, right? Yeah, that's why you… cardinality is as important as your… what it is you're trying to be cardinal with, or whatever. Sorry.
**Alan Clucas** 31:20 And it makes no sense to, like, with, you know, metric aggregation makes… it makes no sense to aggregate over some of these dimensions.
**neil yashinsky** 31:28 Right. You lose all the value of the data by… by… Watering them down, it becomes to no value.
**Alan Clucas** 31:34 Yeah.
**Carlos Alberto Cortez** 31:35 By the way, I have to drop, I have some other call to attend, too, but thank you, this was really helpful. Yeah, this will help me to grab, you know, to massage the prototype and, you know, the initial proposal for the spec.
It has been taking a little bit longer than expected, but this was very helpful, so hopefully we can make progress on this front. I hope to jump. Thank you so much.
**Dotan Horovits** 31:55 Thanks, Carlos, for checking it out with the team for us. Really appreciate that.
**Carlos Alberto Cortez** 32:01 Perfect. See you around! Stay safe, cha ciao.
**neil yashinsky** 32:04 Hi, Chopper.
**Dotan Horovits** 32:05 Actually, I need to drop off, but, Alan, if you want to carry on, do go ahead.
**Alan Clucas** 32:18 Can't really make out what you're saying. You've gone very robot now.
**neil yashinsky** 32:21 I heard he has to go, though.
Yeah, me and Alan will carry on if we need to, if I have to torture poor Ellen anymore.
Thank you, Dotando, too.
**Alan Clucas** 32:30 Thank you.
**Dotan Horovits** 32:34 Yeah, and I just took as best…
**neil yashinsky** 32:36 Oh, yep, sorry, go ahead.
Oh, I just was gonna say, I took as best notes as I could. So some of them are pretty good. I think there was a quote or two that I missed.
But I feel like, if you know my style of notes, it's like, it gives a sense of, like, the conversation as much as, like, all the details. Let me know if it's… if it's… if it needs improving, and I'll go back and review the call and improve them.
**Alan Clucas** 33:05 Yeah, that's, that makes sense.
**neil yashinsky** 33:08 Great.
**Alan Clucas** 33:24 There we go.
**neil yashinsky** 33:24 Typing in front of people.
Alright, great. I think I'm gonna run too, Alan, but I just highlighted this one section above where I totally missed your, didn't get your quote. So if you have a moment after that, you wanna just… Maybe I lost everyone?
The video… your video is frozen, Alan, at least. Or you're very, very still. Oh, okay. Hey, Marco, how's it going? I think I'm gonna jump.
Have a good day.
**Marco (Gjed)** 34:32 Alright, you too. Cheers!
**neil yashinsky** 34:33 Yeah, oh, there you are. Oh, yeah. Oh, okay, Alan, you're back.
**Alan Clucas** 34:37 Sorry, my internet cut out briefly.
**neil yashinsky** 34:39 You carry on. No problem.
Yeah, yeah. No, great, I think we were just wrapping it up, but I was just gonna highlight, if you see this one section above here, where I have Alan's Challenge blank.
So, if you wanted to fill in the mystery there, about 6 or 7 lines up from your cursor.
**Alan Clucas** 34:54 I… I can see the line, I just can't remember what I was talking about at that point.
**neil yashinsky** 34:59 If it's not important, you can just say, Alan has no challenges worth reporting. No, totally fine. I think it was, Yeah, it was related to, like… No, I guess I can't remember. Alright, well, I'll take it out, but if it comes back or seems relevant, we can always put it back. We'll probably copper it.
**Alan Clucas** 35:15 Okay.
**neil yashinsky** 35:16 Thanks.
Cheers, everyone.
**Alan Clucas** 35:19 Cheers.
**Marco (Gjed)** 35:21 Dude.
**Alan Clucas** 35:22 too.
