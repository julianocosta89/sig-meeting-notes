SIG: CI/CD SemConv SIG
Date: 2026-11-03
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 00:44 Well, hello.
**Robert Pająk (Splunk Inc.)** 00:51 Is the finishing… hello, hello!
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 00:54 How are y'all?
**Robert Pająk (Splunk Inc.)** 00:56 I'm fine, I'll need to drop in 15 minutes.
I think I'm good.
How about you?
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 01:04 Alright, thank you.
**Christophe Kamphaus** 01:09 Hello?
**Robert Pająk (Splunk Inc.)** 01:11 Hello?
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 01:49 We can get started whenever you're ready.
**Robert Pająk (Splunk Inc.)** 01:53 Can you start pre-stop, maybe, today? Because I will need to drop in 15 minutes, so…
**Christophe Kamphaus** 01:58 Sure, I can shout.
**Robert Pająk (Splunk Inc.)** 02:01 Yeah, I… Yeah, this mic for 5 minutes, but just to gather feedback.
Those two topics.
**Christophe Kamphaus** 02:11 It should be this screen.
Can you see it?
**Robert Pająk (Splunk Inc.)** 02:19 Yes, we can see Google Docs and tabs, which we already opened.
Okay, so… Perkins one.
I wanted to just ask if you have any input. First of all, I think, if I remember, Christophe, you already replied, I do not remember, Adriel, if you had the chance to see this one.
Yeah, it was only Kamphaus. So, I'll per… I'm not sure about… the SDK, I'll probably see language by language. The thing is that the context sometimes can be passed implicitly, sentences explicitly passed, and I'm just worried that, you know, for the SDK experience, it might be, it might be, I don't know, background, if people do not explicitly just extract this context through Carrier, but maybe I'm wrong.
I'm just not convinced right now if it's good to do it, you know, inside SDK, that it will try to guess, you know, it will try to guess the context through environment variables always, so I'm just worried about this, this behavior for the SDKs.
But for any automatic instrumentation, like Python, Java.NET, and others, I think Having that automatically will be good.
I also, Christophe, agree with you that the parents should be the default, and I also think that, by default, we should also inject when spamming any processes. The thing is that without injecting, you will not extract anything. If you have, you know, auto-instrumentation and anybody, well, it doesn't matter if you extract, if you don't start injecting.
I'm just a little bit worried about the thing that this environmental purpose will be always injected, you know, from a security perspective, but on the other hand, we do the same when we are making HTTP calls, we are also adding baggage to, you know, when having HTTP instrumentation, so I think… it's a similar kind of trust, I don't know, you know, trust boundary.
**Christophe Kamphaus** 04:32 I would disagree here, because.
**Robert Pająk (Splunk Inc.)** 04:33 Okay.
**Christophe Kamphaus** 04:34 If you inject it automatically, You would also have to start injecting all the other hotel headers, namely where to send it to. And if you have authentication headers there, that could be a security issue.
**Robert Pająk (Splunk Inc.)** 04:50 Why would… why… why do you mean authentication headers? Could you give me an example?
**Christophe Kamphaus** 04:56 If you send your telemetry to a SaaS service.
You usually have an authentication token for your telemetry.
**Robert Pająk (Splunk Inc.)** 05:07 Yes.
**Christophe Kamphaus** 05:08 And so if you Spawn processes, and… Forward the status, set the status for new processes.
**Robert Pająk (Splunk Inc.)** 05:17 You're quick?
**Christophe Kamphaus** 05:18 You could have processes that you don't trust completely, and you could leak your credentials that way.
**Robert Pająk (Splunk Inc.)** 05:26 But why would you have credentials in HTP headers?
**Christophe Kamphaus** 05:30 not HTTP headers, the environment variables for hotel.
**Robert Pająk (Splunk Inc.)** 05:35 I see.
**Christophe Kamphaus** 05:39 So that's why it's different from HTTP.
**Robert Pająk (Splunk Inc.)** 05:42 Okay, but right now, what happens automatically? You only pass the… It's… I think I… right now, I think what I thought is only adding the environmental variables, only appending the ones that are set via the propagators, you know, like W3C, etc. So, you know, the default config.
Not everything.
**Christophe Kamphaus** 06:12 I guess…
**Robert Pająk (Splunk Inc.)** 06:13 That's appendage.
**Christophe Kamphaus** 06:14 Yeah, I guess if you just forward all the environment variables by default, then the others would be part of it anyway.
**Robert Pająk (Splunk Inc.)** 06:22 Yes. Yep.
So I thought about only appending and overriding the ones which are.
**Christophe Kamphaus** 06:28 Yeah.
**Robert Pająk (Splunk Inc.)** 06:29 Which are taking… which are part of the propagation.
Oh, And the problem of, you know, leaking… It's still present in all the instrumentation libraries, HTTP, etc, and it's always have been a problem for the propagators, that sometimes people do not want to propagate through some stuff.
And I think this is a common problem. I'm not sure if we need to address this for this kind of thing.
For sure, it needs to be possible to disable this mechanism. It cannot be, you know, like, it always works.
Yeah, I'm considering to make a prototype in .NET for it.
Do you have any other comments, Christophe, for this one?
**Christophe Kamphaus** 07:14 Yeah, it's something I sort of just, know.
the order of the propagators. If you instrument an HTTP server, and it would get the environment variable.
Transparent.
Then it should be extracted last.
So, by default, it would get the HTTP context.
But if it has some internal telemetry that it sent out.
Those would be parented to the… environment context.
**Robert Pająk (Splunk Inc.)** 07:45 Agree.
**Christophe Kamphaus** 07:49 And I guess since there, it would be a long-running process, it might make sense to ZR Use the link.
option instead of CParent.
**Robert Pająk (Splunk Inc.)** 07:59 I thought about this one as well, so it depends how the… how you make expense in a long-running process.
For instance, I remember that, when we were making some worker, I was usually just creating spans for, you know, a unit of work, not for the whole process. Because otherwise, you have a long-running span which never… which never ends. And in this context.
Can be still apparent.
it doesn't have to be a link. If it's a short-living span, which, you know, decreased something from a capture, whatever, I'm just guessing, or some other stuff, then I… even for the long-riding process.
If it's doing some, you know, multiple jobs, I think it doesn't need to be even a link.
Yes, sir.
**Christophe Kamphaus** 08:48 It would… if it was consuming messages from a queue, there you would also rather use the link to the…
**Robert Pająk (Splunk Inc.)** 08:55 Yes.
**Christophe Kamphaus** 08:56 Contacts from the queue.
**Robert Pająk (Splunk Inc.)** 08:57 That's true.
**Christophe Kamphaus** 09:00 Yeah, I was thinking, really, it's a distinction between a long-running process, like some server.
or CLI utilities that you launch in the pipeline.
Even if the work it does is… could be long.
**Robert Pająk (Splunk Inc.)** 09:14 It's better to have a child.
**Christophe Kamphaus** 09:16 Yeah, I won't.
**Robert Pająk (Splunk Inc.)** 09:17 I agree.
**Christophe Kamphaus** 09:18 relationship.
**Robert Pająk (Splunk Inc.)** 09:20 Yeah, I think it can be configurable as proposed by, I think, everyone.
**Christophe Kamphaus** 09:24 Yup.
Yeah, so if you have any comments, you can put it here in this.
Issue.
And the other issue you wanted to discuss was this one?
**Robert Pająk (Splunk Inc.)** 09:45 Yeah, I want to just ask, where are you here? And I see Carlos is here, also, Nicole. I also had… so maybe first status update, and then I also had some discussions with other people, and I also just want to forward some feedback.
**Carlos Alberto Cortez (Dash0)** 10:03 Yeah, the PR that you see there, that is red, that was closed, that was a PR for the specification, redirected on this a little while.
So, the problem is that Java wanted to take a different path, Instead of soul.
So basically, the thing is, what happened is that this… in this way, you just have a set of methods, you know, for these specific operations, but in Java, I think it was Jack that they wanted to have a single method with an enum.
passing stuff, you know? And then I was supposed to massage the specification so you would allow the two variants to exist.
**Robert Pająk (Splunk Inc.)** 10:43 I see. Language specific.
**Carlos Alberto Cortez (Dash0)** 10:45 Yeah, and then that never happened, because, you know, I joined a company, and I have been ever since busy with a lot of stuff.
And honestly, I will not have time to work on this, even it's kind of small.
because I'm working on something else that, like, you may have heard of scope attributes.
Which I don't need, but there's no tips, so I'm working on that. So, yeah, if you have time to work on this, it's possible.
**Robert Pająk (Splunk Inc.)** 11:15 So, Christophe, could you just unassign, Carlos from this, and maybe even assign… oh, there's no… nobody assigned?
**Christophe Kamphaus** 11:22 Oh, it's a spec issue, so I cannot change.
**Robert Pająk (Splunk Inc.)** 11:25 And it's also… and it's still community feedback. Yeah, I was saying to myself, regarding feedback that I… I received, some people think that this might be an overkill, having this prop… propagator, and they were thinking, they were thinking, And I'm not sure, it's just, you know, it's just, you know, kind of alternative way how to address it. If… if there is… if this… the question is if it's… if it's a problem for long-running operations, or is it a problem for All spans, because from the issues that we have been looking, it was mostly for long-running spans, that people knew that something would take very long, and it was just, you know, a problem to have any visibility on this, you know, upfront, known long-running spans.
So, kind of the hack or proposal around it, without doing this.
is just to admit an event when it started, you know, kind of business operation, you know, I'm starting, and it will have the span ID anyway, which is started, but it's not finished, so people in the backend can see.
That they have an event with a span which is started, but has not… has not, you know, has not reached the backend.
this is one… and they could also, I don't know, also separate this business logic maybe into separate spans, into separate steps also. This is also an alternative. If it's applicable, just, you know, have it more, you know.
So, I'm not sure if it was ever discussed, Carlos, or have you got any thoughts on that?
**Carlos Alberto Cortez (Dash0)** 13:05 Yeah.
So, long story short, from the top of my mind, the way you're describing to have a spanse representing another span, like meta spans, that's something that we had in LightStep.
And that's how we solved this, back in the day. But it was, of course, implementation-specific, you know, based on open tracing and all that. So, yeah, it's possible. I think that the thing about this spam processor is that that's how the initial discussion on the spec level was defined.
Yep.
The other thing is that, this is, yeah, mostly, I think the main motivation has been long-running spans, although Josh Zurith have some… ideas, and give us, some, like, side project to… To, put, like, long-running spans, or probably any span, in some kind of local buffer that is written to disk.
and you can recover it, like, primitive style, so you can, like, you know, in case the process crashes, you can just recover that, or something like that. And for that kind of stuff, this could be useful for him.
But it's… it's, it's, what do you think?
**Robert Pająk (Splunk Inc.)** 14:16 I see.
**Carlos Alberto Cortez (Dash0)** 14:17 Currently, so nice to have, but yeah, I would say we are, technically speaking, the only real potential user as of now.
**Christophe Kamphaus** 14:26 Yeah, I remember that Josh mentioned something like that.
His would also be a more generic solution.
So, Robert, what you proposed was that we could send log events.
Explicitly, anytime we know that we start a long, potentially long-running span.
**Robert Pająk (Splunk Inc.)** 14:52 Yep.
**Christophe Kamphaus** 14:53 And we could potentially also define them In SemConv.
**Robert Pająk (Splunk Inc.)** 15:01 Yes, I think we called.
Not sure if it's, you know, you're this… Symmetry commercial, you know, kind of specialists, so you know you know, where is the place, how to name it, etc. So, if you have any ideas on this, you can just, you know…
**Christophe Kamphaus** 15:16 I would say it depends on do we want to define them as a generic solution?
Then we could say, spend started.
whatever the spend ID, right? It's, rates that we now have spend types as well.
So, that helps with that.
And, any additional information, like span started, would be an event we would have span in progress.
**Robert Pająk (Splunk Inc.)** 15:44 So what you say… what you say is that, if I try to just think it through, we can just… because there is a separate issue in semantic conventions to define this.
you say that maybe we should just start with specifying these events. If you click the part off.
for A4883, I think there will be a hyperlink somewhere.
**Christophe Kamphaus** 16:07 Yeah, almost… Thinking about it…
**Robert Pająk (Splunk Inc.)** 16:11 Ends as well, yeah.
So we could start even here, and people who need it may even just explicitly create these events even without the processor, if they know that there's a long-running span, without having the overkill, and we could probably start here instead of Doing the other, you know, making a… Peace.
big canon. First, let's just have something small.
**Christophe Kamphaus** 16:40 Yeah, and if we have defined it in SemConv, we could also create an, Processor in the collector to transform them back into a span.
**Robert Pająk (Splunk Inc.)** 16:50 Yep.
**Carlos Alberto Cortez (Dash0)** 16:53 Out of curiosity, could you be updating or reporting, like, for example, when the span name changed, or a new attribute was added?
Or we go… Is that, like… considered.
**Robert Pająk (Splunk Inc.)** 17:06 Yeah, that was considered as well.
**Carlos Alberto Cortez (Dash0)** 17:08 Okay, good.
**Christophe Kamphaus** 17:10 Yeah, I think we discussed it last week?
**Robert Pająk (Splunk Inc.)** 17:13 Yeah, last week we decided that it would be even at the end.
it could be, you know, it could be intermediate, but probably when the span is ending, probably you will need to just have everything as an aggregate. We know when the span finishes, probably we should make sure that everything is in the event.
**Carlos Alberto Cortez (Dash0)** 17:33 Wait, okay, so, so silly question. Let's say that one span lasts 10 minutes, and then you send an event saying, like, hey, the span started. Yep.
Menu number 5.
10 attributes were added. Are you reporting that, or waiting till it ends later on to report everything?
**Robert Pająk (Splunk Inc.)** 17:52 We thought about both approaches.
Maybe configurable, we are not sure, but probably easier would be first to start with when it's ended.
**Carlos Alberto Cortez (Dash0)** 18:07 Okay.
**Robert Pająk (Splunk Inc.)** 18:08 We had no strong opinion on that one.
**Christophe Kamphaus** 18:10 Yep.
I think… Our agreement was that mostly what you would be interested in is that the span has started.
a span of a certain ID, with some initial attributes that are sampling relevant, maybe.
That it's still in progress is very important.
And then, when it's done, so that you have all the information, and less… Relevant would maybe be, if attributes change partway.
I don't see such… You said often, or… What is your opinion on that?
**Robert Pająk (Splunk Inc.)** 19:03 mine, or Carlos, or all of us.
**Christophe Kamphaus** 19:06 All of you.
**Robert Pająk (Splunk Inc.)** 19:08 I have no strong preference. I need to run. I will try to look at the recordings later. See you guys!
**Christophe Kamphaus** 19:14 See you!
I guess one reason you would want to have the attributes early, while the span is still in progress.
is… if you would lose it afterwards, so it's never completed, so you would lose those attributes. So if you know some attributes were added and or changed.
You might want to send that information early.
In case you lose the span afterwards.
But I think for the use case that you want to know when it started and that it's still in progress.
There, it's not that useful.
You could also take the health check, the in-progress event, and just say.
It always has all the attributes that are known about that span.
But then you start duplicating information.
And you increase the bandwidth requirements.
**Carlos Alberto Cortez (Dash0)** 20:26 Well, I mean, if you're to… I don't know, yeah, it's very interesting, but anyway, yeah.
I think there's no perfect solution, The, the question is what, what trade-off works well?
**Christophe Kamphaus** 20:42 Yeah, I guess you could also do a mix, or make it configurable.
But then you have to be specific for your environment. If you say, I always send the in-progress event with just the span ID trace ID, That you know You don't have C other attributes.
And then you require the completed event To know the exact attributes of that span.
And I think… It makes sense here to define generic events in SemConv.
Instead of saying, span X requires, Z events.
I think it's a bit like, for spans and metrics.
We have the discussion at the moment where we have Metric durations that match to a span.
And we are now aligning Spend types and metric, metric types.
So, same match.
You could say we do it similarly for the event, span started, span completed.
Or we say we have a generic spend started, in progress, completed.
Vince.
As for where to put some… I know that we have the reserved registry for hotel.
We could maybe create… events in here.
**Carlos Alberto Cortez (Dash0)** 22:44 Yeah, I mean, we needed the events for the sound processor part in any way, way down the road, so yeah, it's great.
**Christophe Kamphaus** 22:53 I think I will discuss that next Monday.
We see also some conf maintainers.
Then we can get started on it.
Anything else on this topic?
Overlook.
With a summary of what we discussed today here.
Correct me if I'm wrong, Carlos.
Anything to add?
**Carlos Alberto Cortez (Dash0)** 25:05 You can say, well, I don't know if it's important, but basically, even if we go the spam processor way, eventually, these events could be useful, because, you know, somebody has to report them anyway.
**Christophe Kamphaus** 25:18 Yes, he… initial processor, Would then, could have used those.
conventions.
**Carlos Alberto Cortez (Dash0)** 25:26 Yep.
**Christophe Kamphaus** 26:21 Great.
Alright, next topic, Adriel, you had an update?
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 26:28 Yeah, I just wanted to let you know where I'm at with that, So, right now, the infrastructure is, ready to go. I just gotta configure the Cloudflare, tunnel configuration.
And then turn on, one of the… one of the instances, or one of the repos that use the shared workflow for PR Dashboard. We just need to enable the, hotel exporter in there, and then we'll start to see, sub-span traces, or sub-step traces from Using environment variable context propagation, from GitHub Actions.
So, pretty close to being able to showcase that. Should have it definitely done in time for y'all's the KubeCon talk that they've got going on for environment variable context propagation.
It's still gonna be in our, current vendor?
So, like, we're not opening the door for it, but there… I will be scheduling a meeting with, some of the folks, who have another project in mind as well, from getting telemetry from the OTEL website.
Thanks for putting that together, Christophe. We'll be scheduling a meeting with them, though, to discuss the proposal and consolidate, so we can figure out what, like, opening the door for a non-vendor solution, you know, being able to analyze telemetry from our systems, from our project here.
will look like. But for now, I'm just gonna keep it where it's at, and then once we have that meeting, we can move… move it over, for a long-term thing. But it'll still be demoable, for the… for the talk.
That's… that's my update. We're just pretty close, so…
**Christophe Kamphaus** 28:09 Yeah, sounds great.
Yeah, so you said it will be ready for KubeCon.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 28:21 Yes.
**Christophe Kamphaus** 28:22 And white.
So, one week to go.
Or is it 2 weeks?
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 28:28 I don't know. I think it's… I'll probably have one week. I'm hoping here happens.
**Dotan Horovits (Amazon Web Services, Inc.)** 28:32 It's been away, guys, we're nearly there. It's next week.
**Christophe Kamphaus** 28:56 Alright, next topic.
**Carlos Alberto Cortez (Dash0)** 29:00 Yeah, this one was created by you, Christophe, but I wanted to talk about that again. This was in the context that, we were discussing before.
That they had posted, a comment in Slack about… how to represent the queue time for response, and the… specifically, the… the case I was mentioning was that you have, for example, I'm reading now, like, the message in Slack, is that you have built and test rules span.
And then you have the individual tasks, like pre-job, skip individual, you know, like, whatever you have. But then, it could be a new span called queued.
Which would try to represent the… the actual, time that Spanish, like, just waited, you know?
Yeah, basically that stuff, you know, like, my employer has a GitHub action for that, and we got this request.
But, I am a little bit… I don't think this is, like, the right or the best approach, especially that, we don't have anything, so if you have any feedback on that front or something, just let me know.
But basically, the problem for me is that like, the root span has, you know, start and span time, then you have QT, which has, let's say, it starts at 8 in the morning, it starts at 8 in the morning at 00000, And then you have all the tasks, all the other, sorry, subtasks, and they have the very same start time. So they are sharing, like, kind of duplicating the stuff, you know? That was my main problem. I don't know if it makes sense.
**Christophe Kamphaus** 30:49 What is it you want to solve? Do you want to optimize your pipeline runtime? Do you want to reduce your queuing time?
**Carlos Alberto Cortez (Dash0)** 30:59 I could say no, like, it's just more about reporting the queue time, if possible, if this is humanly possible, with whatever, you know, the vendor is giving you, in this case, GitHub.
And general guidelines on how to do this, you know?
I think that probably other, like, you know, systems may report this differently.
Yeah.
So, general guidelines, if you have, like, anything… well, to be honest, I don't think this can be easily be standardized, you know? But probably general guidelines would be good to have.
**Christophe Kamphaus** 31:37 No.
I know that at the moment, we don't have general guidelines on it, I just know… For GitHub queues, we have the span that is reported.
So you could find all spans of, that contain that.
And do statistics on those.
Then for other systems, like Argo Workflows, there is typically… Container, startup times.
Where you would require those spans from Kubernetes.
**Carlos Alberto Cortez (Dash0)** 32:13 Hmm.
**Christophe Kamphaus** 32:14 Image pull times.
for example.
Yeah, so at the moment, we don't have general… Guidance on it.
Are you looking for defining semantic conventions on it?
**Carlos Alberto Cortez (Dash0)** 32:39 I don't think we can do that easily at that moment. It's just, like, more, like, preliminary, opinions on this one. As I said before, I don't… I don't know how much We could define on this so-called queue… Q response.
Yeah, I would need to go and check what's happening there.
**Christophe Kamphaus** 33:03 Yeah, so it's a bit like… For our pipeline run duration metric, Well, we do have… An attribute to subdivide Into queuing, executing, and finalizing phases.
So we could define… Spans for these phases, and then do the mapping between these faces aren't symmetric.
But yeah, it's not something that's… Commonly done in semantic conventions.
**Carlos Alberto Cortez (Dash0)** 33:39 Right. Yeah.
**Christophe Kamphaus** 33:40 We are just now working on doing the mapping between span and… metric durations.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 33:51 Carlos, have you seen the use spans from the GitHub receiver and the hotel collector?
**Carlos Alberto Cortez (Dash0)** 33:57 Yeah, I was checking that. I think you do something like, actually, sorry, wait, the way you have them there, that's the way we are reporting.
The queue, you know?
It's the same way.
And I was thinking, that's good enough.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 34:17 I can show a quick visualization of that, and from our hotel projects, if you want to see it.
**Carlos Alberto Cortez (Dash0)** 34:23 Yeah.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 34:25 I'm gonna hijack the screen share.
Go ahead. Ignore where these are stored at.
But this is a dashboard that calculates key span durations by repository.
So you can see, like, these are the iterations here. And so, like, if we click into a trace.
You can see what it's actually calculating is just durations, span… just normal span duration, Of the queue, spans that are named, right?
Of course, we do also have, CICD pipeline run queue duration as a attribute.
That's been, computed and sent and attached.
But yeah, this is how it shows up from the GitHub receiver.
This one's a good example, right? Because it was, like, 3 minutes of queue, and then it finally started, doing its stuff.
**Carlos Alberto Cortez (Dash0)** 35:24 Yeah.
Yeah, that's what I would expect more to see, and this is, if I remember correctly, how we are trying to solve this.
Yeah.
I think that's good enough, I think. If you're… yeah, that makes sense.
Good.
Okay, I think that's all from my side for now. I will go and play more, probably bring some new findings next week.
But yeah, that's good, good stuff to see there.
**Christophe Kamphaus** 36:01 On White, Dotan, you're up.
**Dotan Horovits (Amazon Web Services, Inc.)** 36:07 Yeah, so, you mentioned the KubeCon, so I just, I know that I posted on Slack, but wanted to use the opportunity that everyone's here just to, sync.
for next, week, who's going to be there, and, maybe plan how we can… they're not going to… from what I gathered, they're not going to have the observatory, this time around, so, we won't have the, I guess, the… that format that we plugged in the SIG, but there is the project pavilion, so it should be a good place as well to maybe hang out a bit and provide people with time to approach and ask questions, so I wanted to bring it up and see, A, who's around, and B, any thoughts or any information that you have that we can, I guess, work around.
And thanks, Crystal, for forwarding the email, by the way.
**Christophe Kamphaus** 37:01 Yeah, you're welcome.
So I won't be there, but I have some information.
mainly the, observatory, it was always sponsored, but not anymore, so we have to make do with what we see Project Pavilion.
However, usually the maintainers will come early and will grab a bench next to the project pavilion, so there will always be a place to meet and discuss things.
Of course, someone… it could be you, that, comes early and gets the place.
Also in Slack, I saw in the hotel maintainers, channel.
It seems like not too many people have, volunteered yet, so… I think they are looking for people.
As well as time slots to, to broadcast when a specific SIG will be available at the Project Pavilion.
So you could reserve a time slot.
So if anyone is interested in CICDs, they would know when to come there.
**Dotan Horovits (Amazon Web Services, Inc.)** 38:19 Okay, so it's very similar to what we had with the observatory in terms of allocating the times and then publicizing it. That's good to know.
So I'll, If you have it at hand, then you can just forward me the… that message over Slack, and I will jump then on that thread, and Dig in some more.
I'll look into that, but that sounds like the perfect chance. I know that Alan is also going to be, Around, and hopefully to have maybe, someone else, so this would be a good opportunity for… for us to maybe… Publicize the slot for that.
**Christophe Kamphaus** 39:00 Yeah, I just forwarded you the message.
**Dotan Horovits (Amazon Web Services, Inc.)** 39:04 Thanks.
And if you come across anyone else from the, from our circle that, you hear that they're going to be there, even if they're not here on the call, but, feel free to, let me know, let them know, and, like, I will connect the dots and, get the relevant folks in touch.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 39:25 Just a heads up, I won't be there.
**Dotan Horovits (Amazon Web Services, Inc.)** 39:28 You… you won't?
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 39:31 Correct, I will not be there.
**Dotan Horovits (Amazon Web Services, Inc.)** 39:33 Oh, okay, okay. Well, no, I'm ashamed that you're not going to be there, but thanks for letting us know.
**Christophe Kamphaus** 39:42 And maybe a question about next week?
I guess a lot of people will be at QCOM, so… Will there be anyone, should we have some meeting next week, or should we cancel it in advance?
**Dotan Horovits (Amazon Web Services, Inc.)** 39:56 look like most of it. Definitely, this forum doesn't have many that are joining KubeCon, so at least as far as you're concerned, it should be business, like.
this as usual, I guess, or not be disturbed by KubeCon?
But if you… if you're uncertain, maybe you want to post a question whether people see a need to, cancel.
Whatever you think.
Less, less KubeCon attendees than we were hoping for, so on the other hand, maybe more, ability to attend.
**Christophe Kamphaus** 40:32 Yeah, I will just start the meeting and see who shows up.
**Dotan Horovits (Amazon Web Services, Inc.)** 40:37 Sounds good.
**Christophe Kamphaus** 40:41 On Whitesun, have fun at KubeCon.
**Dotan Horovits (Amazon Web Services, Inc.)** 40:44 Thank you.
**Christophe Kamphaus** 40:49 See you, everyone!
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 40:51 Take care.
**Christophe Kamphaus** 40:51 Have a great week.
**Dotan Horovits (Amazon Web Services, Inc.)** 40:53 You too. Thanks, Christophe, for leading the meeting. Thank you.
**Christophe Kamphaus** 40:57 Bye-bye.
