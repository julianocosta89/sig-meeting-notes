SIG: Android SIG
Date: 2026-03-17
Duration: 66 minutes
============================================================

## Zoom Recording Transcript

Cesar Munoz 00:04:54 Hello.
Good.
Afternoon.
And good morning Share my screen… Okay.
See, good day, baby.
Okay… So we have one item on the agenda.
And it doesn't look like… Mmm… Too many people are gonna join today.
But for starters, let's just add our names here.
And, let's… Let's give it a time for a survey.
I'm guessing she shall join.
Let me check the… Send any message in the group chat or something.
Nope.
One sec, I'm gonna write here.
Surbhi Agarwal 00:07:37 Hello, good morning.
Cesar Munoz 00:07:40 Hey, Survey!
Welcome.
Good morning.
Surbhi Agarwal 00:07:47 there has been some important tasks that I was working into, so this issue that we were discussing got delayed, but I am back on it now.
Cesar Munoz 00:08:00 Got it Let's open it up.
Do you have any specific comments right now for.
Surbhi Agarwal 00:08:07 y'all.
Cesar Munoz 00:08:07 Or you're… yeah, go ahead.
Surbhi Agarwal 00:08:10 I wanted to touch on a few things. So, basically.
In one of the previous calls, Jason mentioned about using complex attribute type instead of having them as multiple simple attributes. So, I wanted to understand exactly what was he proposing. Is there something, some groundwork already done there? If not, that would be another battle, right, with the semantic conventions.
Can we separate that out to this? Like, take it as a second step to this?
But I'm not sure if complex attributes are already there or not.
Cesar Munoz 00:08:52 Well, that's a good question. My understanding is that complex attributes are there, but only for log events.
a list in Java.
So… Okay.
it's… I mean, I… it's been a while since I took a look at this issue. My… I think… I don't know if we decided on going with log events, or was it… gonna be extra attributes for the same… for the HTTP span or something?
I don't know if we already made that decision, or I don't remember.
Surbhi Agarwal 00:09:27 Yeah, so, like, okay, some pointers there are… I do know that… Based on my work on the OKHTTP3 instrumentation, I found out that it wasn't possible to capture response, body, and timestamp if we were to do it in the span itself.
Some of these, they happen outside of the span, so we are not able to capture those. That's why I proposed an event.
But you and Hansen did mention that that doesn't seem likely to you guys, but that has been my, experience. But I will revisit that and try to showcase that to you as well.
One of the reasons was that, and second reason to go with an event is for the browser use case, if we were to unify semantics across browser and mobile. So, browser has some other types of requests, which they do not have span instrumentations for, and there is this browser API that gives them the this kind of timing breakdown, so they also want to capture these events outside of span instrumentations, so the event fits better in their use case.
Cesar Munoz 00:11:00 Got it.
Yeah, it's been a while since I took a look at this. I think what I can remember right now is that The, the… so… I'm just trying to remember as we speak, but what comes to my mind right now is that We were talking about a lot of attributes that we needed for a span, for an HTTP span.
That… I know that some of them were possible to be added as span attributes.
But others were not, such as the, body… what's it, the body size?
Something like that.
Surbhi Agarwal 00:11:48 Yeah, yeah, you do not… span ends before the response body end callback is called.
Cesar Munoz 00:11:56 Got it. So… I think if I remember correctly, and please, you know, double-check that later, if you like.
is that… It's kind of, like, a lot of stuff that we want to add.
And… It, it… I guess we could add it right away.
But it's kind of as… It's a bit strange to me, because if I remember correctly, you know, we're essentially trying to extend the information that we provide for an HTTP request.
And, like, the first thing that comes to my mind, at least.
To do so will be by adding more attributes to the same HTTP request span.
But then because one… or two of them, if I understand correctly.
Are not possible to be added.
to the span as more attributes, then we decide that all of them have to be an event.
an event attribute.
that… Has to start… after the… HTTP span has finished.
So then… I… and I think that's why one of my questions was… You know, how we make sure that this event is linked to this band's context.
I haven't checked your answer here.
But it seems like we need to store the context in memory.
Surbhi Agarwal 00:13:29 Yup.
Cesar Munoz 00:13:30 You know, kinda sounds… Surbhi Agarwal 00:13:34 Oh, let me, yeah, I got, your confusion. So, basically, these This data is… 4 metrics.
So, we want to capture the timing of various network phases, like how much DNS took, how much connection setup took, how much SSL took, how much the payload download took, or the request payload upload took. So, this is really… different kind of data than what we receive in the HTTP span. We couldn't go forward with using the metrics signal because there you lose one-to-one correlation with the actual HTTP request.
We wanted to preserve that.
This, is sort of… Like, supplemental data to the HTTP data.
And, like.
like, if it was… event was modeled, inspired from the browser world, right? So, the browser API there that asynchronously, there is an API that gives them all these timestamps. Asynchronous to the original request, they received this.
data. Similar is the… for us, it's synchronous. The event callbacks happen synchronously. But then, yeah, this… this sort of is only for folks who require to gather those metrics.
And gather those histograms and charts on their backend.
Yeah, we do need to store the span context so we can correlate one-to-one. So, from the metric charts, somebody can jump to the direct span.
Where the issue occurred, where, let's say, the response download took a lot of time. So, that's why we store the span context, yeah, and we put it in here in the event.
Cesar Munoz 00:15:48 Got it.
Okay, I mean, yeah, I know that there are a lot of limitations.
That you need to address, you know, across platforms and… I think it's… I mean, it does sound strange, But… I guess that if, you know, If we, you know, somehow explain… in the docs, or I don't know where, that the… it's because of its head of limitations.
It's probably fine. I think one of the stuff that I remember as well was that, ideally, this implementation should be something that's opt-in.
For users who only want to have… to want to actually enable these metrics.
And, I mean… You, you, you know best than… than all of us here about it, so… If, at the end of the day, that's, you know, the best approach available that works across platforms.
I guess, I guess it's fine. Were you planning, if I understand correctly, were you planning to create a… like a POC, or… or something to… Yeah. Draft BR? Okay.
Surbhi Agarwal 00:17:08 So, I wanted to also touch base upon another point, right? So, your confusion is genuine, right? So, the ideal way would have been to have span events, right?
For this kind of a data, but span events are deprecated in favor of a standalone event, so it fits that paradigm also. It's a standalone event that correlates back to the span. That's what span events are supposed to be now, right?
Like, to answer the… like, to put one more argument for the previous question.
Cesar Munoz 00:17:46 That could be. I know that there seemed to be a confusion about how… what's going to happen to span events, because I remember reading some comments from Jason somewhere that… at least the Java SDK, I think it's gonna… keep the API to create span events, but when users call it, it's gonna instead create a log event that it's gonna get attached to the span.
Surbhi Agarwal 00:18:13 Yo.
Cesar Munoz 00:18:14 So, in that sense, I guess the span events are kind of… Just… they're just, replaced, but… but the idea is still… is still there, although the data won't be inside the spans, you know, product data, or something like that. It's confusing.
Surbhi Agarwal 00:18:36 So this sort of achieves the same. Like, instead of going via that API and have that API emit that standalone event for us, and multiple events, we have this one event which correlates back to the span, similar to how that API would do.
Cesar Munoz 00:18:53 Got it. I think it would be nice to see the, the, the prototype, yeah.
Surbhi Agarwal 00:18:59 We do have that PR.
There are some challenges in there as well.
Would you, like, mind if, like, if you… look at that PR and tell me how you think about it. It is attached to this issue. On the top, if you go, the first In, yeah, below one, the below one. This is the browser implementation, this is the, yeah… You know, these things, these decisions are documented in between two issues, but yeah, they are not in one place, and the discussion has been very long.
Cesar Munoz 00:19:41 Okay, and so, just to double check, this PR already does… the… what's this called? As events, and… Surbhi Agarwal 00:19:49 Yo.
So here, what I am having to do is, so I introduced another set of APIs for the tracing interceptor and connection error span interceptor, if you go there.
So, the other API, this includes a Boolean, which is store context for event listener. So, and to go from the top, if you go to the OKHTTP telemetry.
There… no, not this one, actually. I wanted to go to… Some place wherein, where the… there is an API that the user calls to get the instance of instrumented OKHTTP client. So there, we have introduced another API wherein the customer can get the OKHTTP instrumented client with the network listener added, network timing event listener added.
And if they were to call that API, the tracing interceptor and the connection error span, yeah, this one. So here, the connection error and tracing interceptor that gets injected is the one which has that true Boolean.
So, it would tell both of these span interceptors to store the span context for the network event listener to use. That's what exactly happens.
And then, in the network event listener, some events happen outside of the span context, so we store them in a buffer. We have a call to span map. Whenever the span is available.
Because in network timing event listener, we have the call object, so whenever the span context is available, we empty out the buffer, we create a log event, we dump the, received timing attributes in there, and going forward, we add all the timing attributes to the Newly created log event. And finally, when the call concludes, and the call end.
callback, we emit the event. So that's how the implementation is, like, in brief.
Cesar Munoz 00:22:05 Got it. So just to make sure, this PR is the prototype one that you were mentioning earlier, or is it gonna be a new one for… Surbhi Agarwal 00:22:15 This is the PR.
Cesar Munoz 00:22:16 Andrea. Got him.
Surbhi Agarwal 00:22:18 There are some challenges here. So, some challenges here are Network Listener was implemented in OKHTTP 3.11, but the current, OKHTTP version used in this library is 3, and because Java agent, for Java agent also depends on the library instrumentation. The Java agent instrumentation depends on the library instrumentation, that's why we can't really change that. So, I might have to rework it and create another instrumentation, just… which is 3.11 onwards.
So the Java agent still… because I was trying to separate these things out, but it wasn't possible. There's a comment on my PR to elaborate more on that.
Cesar Munoz 00:23:10 Got it.
I'm just gonna add the link here.
the… Got it. So, I mean, okay.
I'll have a look.
Yeah. Later.
the, I'm guessing probably one solution to that issue that you mentioned is just… Avoiding using the… listener… you know, when they're… maybe when they're… during runtime, you cannot find it. Well, but that.
Surbhi Agarwal 00:23:45 Yeah. Likewise.
Cesar Munoz 00:23:45 fire.
Surbhi Agarwal 00:23:46 Using component only?
And running the test cases in a separate test suit that uses 3.11, right?
Cesar Munoz 00:23:57 Well, I was gonna say checking at runtime if the glass was available, but then that will require reflection, and that won't work with… Surbhi Agarwal 00:24:07 That is not good.
Cesar Munoz 00:24:09 You know, obfuscated code.
But maybe, okay, let's, okay. It's… I just wanted to… let you know, survey, that at least to me.
Surbhi Agarwal 00:24:22 Yo.
Cesar Munoz 00:24:22 I think I understand the need for these metrics. It's just that the implementation looks a bit… Surbhi Agarwal 00:24:31 Weird.
Cesar Munoz 00:24:32 forced, in a way. I don't know how to explain it. It's kind of like… To be honest, since we're talking about metrics, Ideally, we should use metrics.
this metric signal for this, but I know… I understand the… the issue with the linking it to the… to the spans, so… I guess I would… Surbhi Agarwal 00:24:54 a lot of data with metrics, right? Like, the filtering… for filtering and aggregation, we use a lot of original HTTP span data as well. All those things are lost with the metric signal.
Cesar Munoz 00:25:06 Yeah.
I, to be honest, I wish there was a way that natively, metrics Could get this.
Ability to get linked to SPANs.
By nature, it's very difficult.
Anyway… I'll have a look.
I… I… hope there won't be… I mean, I think if you explain the reasons why we had to go with this approach.
Like, in a, in a, kind of like a bullet list.
Where it's very clear, that's probably gonna help you land this, because from, high-level point of view, I think it's gonna be tough to… to sell this, to get merged in the instrumentation repo. So… Surbhi Agarwal 00:25:54 I guess he would… Yeah, there are all these limitations, that's why we are having to go with this, and it sort of fits the browser world and helps us unify, so that's my strongest argument now. The… all these… I have had to discuss this with a lot of people, so different people are aware of different… reasons why, but yeah, I will… I have tried to, in a way.
have it… like, I'll try to capture all of these reasons as well, more in today, what we discussed in the issue.
Cesar Munoz 00:26:31 Got it. Thank you.
Yeah, I mean, it's a tough work that you have to do, too.
Surbhi Agarwal 00:26:37 Yeah, but the goal.
Cesar Munoz 00:26:39 For taking a look at it.
Surbhi Agarwal 00:26:41 Yeah. Now I do feel browser is in line on this, browser is aligned on this, and, like, now we… mobile folks and semantic folks have to align with it, yeah. I think if we align with it, we'll be able to convince the semantic folks as well.
Cesar Munoz 00:27:00 Got it. Okay, thanks for the details, Survey. I'll have a look later.
By the way, I don't know if you're aware, but I think next week.
Well, this week and next week.
Jason won't join. Also, it seems like Hanson won't join.
So just… just so that, you know, I think it's because they're in… in Kubekong or, or… Something else, so maybe if you don't get feedback.
For this week or next week, maybe it's because… because of that.
I'm… I'm actually planning, I mean… It seems like… next week… Are you… Do you know if you are joining next week, Jamie?
Jamie Lynch 00:27:51 No, I'm out, and… yeah, I think Hanson is just busy with Embrace stuff for the next couple of weeks, at least.
So neither of us will be her.
Cesar Munoz 00:28:02 Got it.
To be honest, I'm thinking really hard about just canceling the meeting next week.
Surbhi Agarwal 00:28:10 Okay.
Cesar Munoz 00:28:11 Just because, you know, we can discuss it, but it's probably gonna be something that we'll have to do it again.
Surbhi Agarwal 00:28:20 Yeah, with.
Cesar Munoz 00:28:21 When everybody's back, so… Just wanted to mention that.
But yeah?
Thanks for sharing.
Surbhi Agarwal 00:28:30 Yeah, David, I think you had a question in the chat.
Cesar Munoz 00:28:36 I haven't checked.
Surbhi Agarwal 00:28:37 Yeah, I… did not understand it.
DavidGrath 00:28:54 Can you hear me clearly?
Surbhi Agarwal 00:28:57 Megan.
DavidGrath 00:28:59 Okay, yeah. So my idea was that I think the core issue that's trying to be solved with the entire issue of tracking the user's DNS and TLS is whether or not the User is having… user has a slow connection, a bad connection.
So, if that is the question I'm trying to solve, doesn't that mean that maybe he or she would be an outlier within a sample of 1,000 or 2,000 people?
And so, instead… and so, instead of focusing… so if we do use metrics.
Then, how do I explain it?
Let's say if we do use metrics, then that means that if we were to use something like a histogram quantile to try and get the distribution of most users, then they wouldn't be on that… they wouldn't be on that, distribution, and so it means that you have to find them through something else, like a trace query. I don't know if that makes sense.
Surbhi Agarwal 00:29:59 No, it cannot be… like, if I understand this correctly.
There are other things also, right? Like, we are trying to solve for all the different kind of metrics, one of them being time to TTFB.
So, basically, when… the entire time the server… let's say server processing time, so when the… finally the request body reached the server up till the time it sent us the first response header byte.
So these other things are also there that metrics doesn't solve for, and then we would like to jump into the exact span that, from those metric charts, the use cases, you should be able to jump to the exact session and the exact request.
Where that server processing time was horrible, right?
It is not an outlier user.
Yaw.
Like, it is opt-in, We do not create this event unless somebody opts into it.
Does that answer your question?
DavidGrath 00:31:17 Yes, yes it does, thank you.
Surbhi Agarwal 00:31:20 Awesome.
Y'all?
Therefore… There were these other questions from Hanson. I'll try to… we can, like, talk to him about those. So, he mentioned, why do we even need a span? Because we are sticking in some of the HTTP attributes in the event that are needed for slicing and dicing those metric charts.
So, he mentioned, why not, stick all the HTTP attributes in this event, so somebody can just get the event and get rid of the span. But I think that… I'm, like, I'm, doesn't… the event is to provide the extra data, right? For an extra, thing, so that doesn't fit the requirement.
So, I'll discuss this with him.
Cesar Munoz 00:32:17 Got it.
Surbhi Agarwal 00:32:19 Yo.
Cesar Munoz 00:32:19 But by the way, Serby, maybe if you have already done this?
But I think it would also be nice to… Like, explained in… When building your case, The reasons why it's important for For these metrics to… be linked to… to the span.
Surbhi Agarwal 00:32:46 Run.
Cesar Munoz 00:32:47 You know?
Surbhi Agarwal 00:32:47 I can… yeah?
Cesar Munoz 00:32:49 Yeah, because maybe some people might say, well, you know, but I can see that there are some HTTP requests, you know, getting too slow.
And I just need to see the number, probably don't need to follow it.
upwards to the span, or… I don't know, maybe just… So that you have a reason there.
Surbhi Agarwal 00:33:10 Yeah, I do have a strong use case for that, I'll share that.
Cesar Munoz 00:33:14 Add it. Thank you.
Do… is there something else you would like to discuss on that topic, survey?
Surbhi Agarwal 00:33:22 No, today I'm good.
Cesar Munoz 00:33:25 Awesome.
Thank you. Well, I just wanted to quickly mention there is, currently… There is an effort for us to stabilize, OtterAndre as much as possible. For those who might not be aware, we have… Different modules in the project, and only one of them is stable right now.
Or at least public. I already… Public, published stable artifact.
The next step that we wanted to… the next module that we wanted to stabilize was… instrumentations, or the instrumentation API.
And… but there's some work… Left there.
And the latest… One is this PR?
That has, you know, it's… it seems to be a bit, Updates… I don't know, complicated to learn?
It's got some… well, it… you might find… you can find there, links to other PRs and issues that we've discussed, and this, essentially, we want to try to make It's stable in a way that users Won't have to… You know, resort to work… workarounds or hacks to make instrumentations work.
There are different options to work on that.
This is the second PR that I opened with another option, but the first one was blocked, so… it's a bit of a fun topic right now, and I think that… It's something that I would have liked to discuss with Jason, who was the one with concerns on it.
But he won't be here next week, so it's probably something that will continue the week after.
In case somebody has some feedback, please add it there.
And probably, until this is sorted, Hmm… I'm not sure if we will be able to create a new release.
Because if we do so before this is sorted, it might cause other issues, because We might make some stuff stable that then we will have to rollback, but we couldn't, because it's stable, so I'd rather fix the… just, you know, settle on an ideal API first.
So, yeah, I guess, just wanted to mention that, in case somebody wanted to have a look.
And, sorry?
Surbhi Agarwal 00:36:36 I'm glad you brought this up. I do have some questions here, but I'll, sorry, I cut you. I'll go ahead and finish, and then I can ask my question.
Cesar Munoz 00:36:48 No, I think I said it, I said it all. If you have questions right away, we can… we can discuss this.
Surbhi Agarwal 00:36:53 Yeah, let me share my screen quickly, so I… share what I'm saying.
Oh… Are you able to see my screen now?
Cesar Munoz 00:37:10 Yes.
Surbhi Agarwal 00:37:12 Okay.
And let me know if you, see anything else other than what I'm planning to show. So, Splunk Hotel Android, right? You're seeing that.
Cesar Munoz 00:37:22 Yeah, the browser, yeah.
Surbhi Agarwal 00:37:24 Okay. So, what I was saying was, we do… bypass the OpenTelemetry RAM, and directly leverage the instrumentations. We create our own OpenTelemetry SDK instance. So, for example, one example I would like to show you is, let's say, this one.
So, that could be a problem for us. So, what we are doing is… Hmm… So, we have created the installation context with a dummy session manager instance. We do our own session management as well.
And we initialize the instrumentation using that. It's here.
with that context. So, it is the OKHTTP instrumentation that we are using from upstream, and we are providing… we are installing it using the context. So I… we do… so that would mean we would have to… There should… would there be a way for us to still utilize the instrumentations by bypassing the OpenTelemetry RAM SDK?
Cesar Munoz 00:38:41 Yes, yes, it should still be possible. I can show you weekly how.
Surbhi Agarwal 00:38:47 Yeah.
Cesar Munoz 00:38:48 I'll share this, screen.
So… We're essentially… so, right now, the instrumentations they need that installation context, because I need… I think… here's the, API? No.
Here.
Here.
They need, probably a bunch of the objects that are provided there.
Yeah. Such as the OpenTelemetry vanilla instance, session provider, and Cloud.
and context. So… It's something that you will still have to build, and you will still have to pass all of that stuff.
what… I'm proposing here is to, instead of having to build that new Object, where, essentially, we will be kind of, like.
kind of duplicating the state that we add to our OpenTelemetry ROM instance, which is past the OpenTelemetry ROM instance.
And the context is high.
And then the Open Dynamics VRAM instance should essentially provide the same stuff that's here, in this case, session provided in the clock.
But since it's, it's an interface, what you could do is… actually, let me… Let's see… That's right here.
Essentially, what you could do is to create an implementation of this.
Interface, and providing the getters the same values that you were passing to the installation context.
so you wouldn't have to… build OpenTelemetry ROM using the agent, From this repo.
Instead, you will create your, you know, simple OpenTelemetry ROM implementation or something, and just return the same objects. You were saying that you were using a dummy session provider? Well.
You can do so here as well.
Surbhi Agarwal 00:41:02 Yeah.
Cesar Munoz 00:41:02 Ideally, you should provide the clock that you're using to… in… in the Splunk OpenTelemetry object that you guys are creating.
To make sure everything is consistent. But the idea is that… We wouldn't have to duplicate the dependencies for instrumentations that we already set into the OpenTelemetry ROM.
object.
And that will reduce the API surface, and Frankly, I mean, one of the ideas That we've discussed was to turn installation context into an interface, because that will At least make it… easier to… extend without having to break stuff in the future, because we could, you know, add new getters and make them, you know, have default Bodies, or something like that.
But in the end, we will… Carol, I just… duplicate these dependencies across these two APIs. So it's kind of like, it's a bit simpler just having one, which is OpenTelemetry ROM.
Surbhi Agarwal 00:42:17 Hmm.
Cesar Munoz 00:42:18 And that will be it.
If you have more questions, You know, we can discuss it in the comments, but… Essentially, you will create your… Simple implementation, and just pass all these objects.
Surbhi Agarwal 00:42:32 Yeah, that works for us, yeah.
That makes sense. In a way, sort of, for us, like, installation context got renamed to OpenTelemetry RAM.
Like, for us.
Cesar Munoz 00:42:46 Yeah, I guess that's a way to look at it, yeah.
Surbhi Agarwal 00:42:49 Yeah, but I understood your point as well, that, OpenTelemetry RAM already has all of it, so you don't want to create two different interfaces.
With redundant stuff, and instead directly use that.
Cesar Munoz 00:43:06 Yeah.
Surbhi Agarwal 00:43:09 Yo.
Cesar Munoz 00:43:10 There's also more comments on this approach.
these approaches and ideas. I'll also link this other PR for… Yes. More context.
And, not a comma. And, there's also an issue… I mean, this discussion has gone… A while, for a while now.
So… But I… hopefully, once it's done.
I'm hoping that, why did this? Okay.
After this is done, I think… To be honest, for me, that would be the… At least the foundation of the whole… You know, agents plus instrumentation architecture should be done.
At least the bare bones.
And to me, that would be great news, because that would mean that The, you know, what would we… what would come next?
We'll be just extending it and adding more stuff, but the, you know, on top of the same architecture, so… It will be more… much more easier, but this is kind of like, at least to me, the last thing that we have to figure out before just getting into a… Place where all we have to do is just create new instrumentations.
That would be it.
Do you know what?
Jamie Lynch 00:44:47 remaining parts of… of, on that PR that are looking at. Was it just the session provider interface being present, and that being unstable?
Or are there additional points.
Cesar Munoz 00:45:02 JSON's… yeah, I think it was related to, yeah, session provider.
Yeah, I think this is why I wanted… I wanted him to, chime in, but essentially, it looks like he's concerned about providing session provider.
Because we still don't know where sessions will go in the future in the semantic conventions. Now, my argument is that session provider only provides a session ID.
So it's probably… that probably won't change.
But then, he mentioned something like, maybe… we do need to stabilize session, and also Session Publisher.
Which is… allows to observe sessions, and… to me, I mean, that's kind of like going from not wanting to stabilize one interface to now being fine with stabilizing more.
Jamie Lynch 00:46:06 Hmm.
Cesar Munoz 00:46:06 And that's a bit confusing to me, so I… I think I… yeah.
Jamie Lynch 00:46:11 Yeah, I mean… I guess, from my perspective.
Is there an option of not including that?
In the initial… Stable interface that we release, and… Because… Yeah, I guess it depends on how many instrumentations are actually using Session Provider right now, but I assume it's just a couple.
Could we provide some sort of internal way of getting that until we stabilize it?
Cesar Munoz 00:46:40 I think it's only one.
Which is this one, I think.
Surbhi Agarwal 00:46:45 Session change instrumentation.
Cesar Munoz 00:46:49 Yeah.
Surbhi Agarwal 00:46:50 Spot event, and… yeah.
Cesar Munoz 00:46:55 Which, I also have some questions about this instrumentation.
But yeah.
Yeah, let's see.
Jamie Lynch 00:47:09 I will add my thoughts onto that comment chain, and we'll see where it goes.
Cesar Munoz 00:47:15 Got it. Thank you.
Sorry, Survey, you wanted to say something?
Surbhi Agarwal 00:47:20 Yeah, so another question popped up in my head.
So, we did a ton of work to isolate ourselves from the core, right? We pulled out the services, so we can depend on just the services module, and not depend on the core module. But when… The OpenTelemetry RAM interfaces, I'm not wrong, depends on the core… is in the core module. So we'll have to depend on the code just to define that interface, right?
Cesar Munoz 00:47:48 You mean the session of internet RAM, if it's in core?
Surbhi Agarwal 00:47:52 Yo.
Cesar Munoz 00:47:54 It was, but I think it was Hanson who extracted it from Core, so it's now in its own module.
Surbhi Agarwal 00:48:04 Okay, that works then, yeah, because Core brings in a lot of other dependencies, like disk buffering and stuff, which we don't use, so we do not want to depend on core.
Cesar Munoz 00:48:16 Got it. Yeah, here it is.
It's in, Agent API.
Surbhi Agarwal 00:48:22 Okay, yeah, that works. Yeah, awesome.
Cesar Munoz 00:48:28 Nice.
Well, that's what I wanted to mention, if there's nothing else, You would like to discuss?
then I think we have some… some time back.
Thanks for… For your input, and I'll send a message in the group chat to cancel next week's SIG meeting.
And, yeah.
DavidGrath 00:48:54 Sorry. Thank you.
Cesar Munoz 00:48:57 David?
DavidGrath 00:48:58 Okay, I don't know if this is the correct place, or if I should just wait, but I do have an issue that I wanted a bit of clarity and direction on.
Cesar Munoz 00:49:11 Sorry, come again? Do you have a… do you have an issue?
DavidGrath 00:49:14 Make sure that I opened it, I wanted clarity and direction on it.
Cesar Munoz 00:49:19 Got it. Do you have a… do you have the link?
DavidGrath 00:49:23 Yes, I do. Okay, sharp pieces in shards or in the documents, I don't know.
Cesar Munoz 00:49:29 Well, both will work, I can add it.
DavidGrath 00:49:34 To the document later.
Cesar Munoz 00:49:35 Okay, this is the one.
DavidGrath 00:49:38 Yes, this is… So it's essentially somebody opened a PR earlier that tries to implement gesture… that tries to register detection.
So now it appears that initially, there is securing gesture detection into the… instrumentation, and so the discussion was generally that it involves a lot of discussion and involves a lot of work, and so you need to be broken down into the various gestures. And so I volunteered for DoubleTap to start with the first leg of this instrumentation.
So I decided to… check out the codebase, and then give out my initial thoughts before I decided to do any actual work.
Cesar Munoz 00:50:19 Got it.
DavidGrath 00:50:20 She's a license that you know… Cesar Munoz 00:50:23 So you've been doing some tests, locally of this instrumentation?
DavidGrath 00:50:29 No, not yet. This is all basically concepts.
Cesar Munoz 00:50:34 Got it.
DavidGrath 00:50:35 Yeah.
Cesar Munoz 00:50:38 Okay, so… so, just to make sure I understand, are you planning to take on this, this, work for this new instrumentation?
DavidGrath 00:50:48 Yes, that is the ground.
Cesar Munoz 00:50:51 Okay.
Well, I mean, we're always open to, any contributions. I haven't… I haven't kept track of this discussion particularly. I think the last thing I saw was that There might be many things that you may instrument from Tops.
And I think what… I understood from one of the threads was that we should, you know, split those and try to tackle each at a time, and to have an instrumentation for each. So I'm guessing this one is one of those you know, specific instrumentation, right? This is only for double tap.
DavidGrath 00:51:32 Yes, it is.
Cesar Munoz 00:51:34 Okay, I think it sounds good, then. Do you have any, any… Questions on… on how to get started, or do you have… do you need some help?
DavidGrath 00:51:50 I'll see for now, though. Let's just know if I was mini-headed in the right direction for now.
Cesar Munoz 00:51:58 Got it.
I mean, where I know we don't have… And it's probably a good thing to create an issue on.
First, let me add… You're… your issue here… Yeah, that's true.
Where is it? Here.
And… We should probably add… Mmm… I think we don't have good documentation on how to create a new instrumentation. Essentially, what we told everybody so far is to just take a look at how other instrumentations are created. They usually follow the same… the same structure, they have, And a library… a library and… and… That's pretty much it. If you need… if you don't need bycode instrumentation, but if you do, then you need other modules.
I think this one probably doesn't need PyCon instrumentation, but if it does, let us know, and I can help you with that.
But yeah, I think it's… I'll take a look at creating a guide on it.
DavidGrath 00:53:21 Okay, thank you very much.
Cesar Munoz 00:53:24 Thank you.
Surbhi Agarwal 00:53:27 Can I ask a quick question?
Cesar Munoz 00:53:30 Yeah, go ahead.
Surbhi Agarwal 00:53:31 In your experience, have you found this that… because OpenTelemetry surface is large, right? For something like our SDK, for instance, we depend on OpenTelemetry, Android, OpenTelemetry, Java, all the SDK API, and then bits of Java instrumentation as well. The instrumenter API that is being used lives there, right?
And then there are exporters and stuff, which are in the OpenTelemetry, repo. So… It causes all this surface, when a SDK is an OTEL SDK, all this surface causes a lot of class loading and class linking pressure when the app starts, and that could cause Android to do certain things differently, because Android would not have enough resources Because the class loading and class linking kicks in during the app startup, and it, diverts the way some activities are initialized, and we are seeing a flicker on one of our customers' apps due to this very reason. So, have you guys have had any experience with such a thing, or any suggestions you would have for such a thing?
Cesar Munoz 00:54:51 Just to make sure, you're saying that there are a lot of static stuff coming from OpenTelemetry that causes Android start an Android to… to have to load too many things on startups, so… Surbhi Agarwal 00:55:07 I am… Cesar Munoz 00:55:07 Too much.
Surbhi Agarwal 00:55:08 I am also not sure if there are a lot of static work that comes into play, but I'm thinking just the class loading.
and class linking. That happens in the starting, right? It doesn't have to be static initializers. There are a ton of classes, like this OpenTelemetry surface is huge, right? So… like… in… when the app starts, it does… it loads everything, right? Like, there are no static initialization right now that I'm talking about, just by the presence of these classes.
Cesar Munoz 00:55:45 Yes.
Jamie Lynch 00:55:46 I mean, our experience own braces, but… the Java… SDK… dominates the startup of our SDK. Like, it's taking up the majority of startup time due to Class loading and doing lots of heavy things easily.
Surbhi Agarwal 00:56:07 It does some verification and stuff, yeah, it does some jazz, and that sort of occupies the Android runtime art.
For some time during the startup.
Jamie Lynch 00:56:22 Yeah, I think that's definitely part of it. It loads a lot of classes up, and… I think… quite a lot of the Java SDK seems to initialize things eagerly, which I guess makes sense, given that it was originally throughout, for… backend.
Surbhi Agarwal 00:56:43 Yo.
Jamie Lynch 00:56:46 It doesn't really matter if it's gonna take a little bit of time for… the backend SCP.
Surbhi Agarwal 00:56:54 Yeah, there is no visual flicker and stuff, you don't see the jank in the UI.
Cesar Munoz 00:57:03 ain't… Surbhi Agarwal 00:57:04 So… Jamie Lynch 00:57:05 Sorry, you're gone.
Cesar Munoz 00:57:08 No, I was just gonna say, do you mean is it… is it, Java normal stuff, or is it Java having to initialize OTEL stuff that makes it… work too much, or… I mean, because if it's just Java's regular initialization, then… You know, it will affect… All apps, regardless.
Right?
If OpenTelemetry been there or not.
Jamie Lynch 00:57:39 I'll see if I can find… Got a flame graph of invasives.
startup time, and it kind of demonstrates that the Java SDK is taking quite a lot of time in certain things.
Cesar Munoz 00:57:55 Got it.
Surbhi Agarwal 00:57:58 Hmm… Cesar Munoz 00:57:58 Got it, thank you.
Surbhi Agarwal 00:58:01 I'm not sure if R8 minification helps here. I do think it is on, but yeah, there are… I was thinking if there are some tools to, make it… Like, less priority, it being loaded lazily, stuff like that.
Without code changes.
Cesar Munoz 00:58:22 The reason I asked if you're talking about static stuff brought by OpenTelemetry Survey is because To be honest, I need to… take a deeper look at how the Java… Runtime works.
Which, I'm not sure if it's the same as… the way Google made it work.
But regardless, my understanding is that Only statics are initialized when an application starts.
The rest of classes, Are only loaded.
Surbhi Agarwal 00:59:03 Yo.
Cesar Munoz 00:59:03 When there are… when there's a reference to them, when somebody… When somebody… when something in the code you know, actually creates an instance of them, or something like that, so… based on that, not everything that comes with OpenTelementary should get loaded just by launching the app, you know?
That's why… that's why I'm saying, if… if it's that, maybe there's too many statics.
But the rest of them should be lazily loaded, my understanding, at least.
Surbhi Agarwal 00:59:35 Hmm, so maybe somehow we are loading some classes that in turn is loading the entire stream of classes from hotel, that could happen.
There is this thing that you mentioned, Jamie, in the chat. We came across that as well. So… the context storage happens on the main thread, and there's a stick mode violation there.
Is there a solution for that?
Jamie Lynch 01:00:13 So… I don't know.
the exact details of this, as Hanson looked into it, but I know that setting up property, alters the behaviour.
So it avoids a street mode violation.
Which I shine improves performance.
Surbhi Agarwal 01:00:31 Okay, yeah, that doesn't do disk IU on the main thread and improves the performance by a few milliseconds, it would do that, and if it would be more if it worked, a lot of telemetry being emitted in the start, yeah.
Jamie Lynch 01:00:45 Hmm.
Cesar Munoz 01:00:47 Okay, thanks for sharing this, Jamie.
I think I understand then. Okay, so… okay, surveys, so… My understanding is that There might be some issues.
Of running stuff in the main thread.
But that doesn't necessarily… it's because of Java runtime having to load too many classes, but instead, it's because of, well, in this case, SPIs that are loaded For… well, we do so for… for Android, for instrumentations.
And OpenTelemetry does it for the context storage.
So, in this case, I think we discussed about it at some point, and we decided that there are some stuff, such as, you know, fetching glasses.
via SPI load.
Or fetching stuff from… from… From the, cache, from the, Yeah, from the cache, from the device, maybe we store, you know, the… the device, the installation ID, or something like that, and then we need to retrieve it.
Because it's needed for the resources, or something like that.
In those cases, I think we even mentioned somewhere in some docs that in those cases, there's… there's nothing to do. I mean, it's like… We do need to read these properties.
Just to initialize OpenTelemetry. Probably, we could… I don't even know where's to document right now, but anyway.
Probably we could, in the future, somehow try to… Moved some parts of the initialization to a secondary thread.
But… Yeah, we'll have to take a look at that. I mean, we're talking about optimizing stuff to the fullest.
And, I think we haven't done so yet, because we still haven't managed to have, you know, an idea of at least how things should work first, so that then we can think about optimization, but… I think we're getting there with the API stabilization.
Surbhi Agarwal 01:03:15 That… Cesar Munoz 01:03:15 Awesome.
Surbhi Agarwal 01:03:17 I did have another quick question. I, like, this is a new question, so, like.
the service provider interface. So, basically, in OpenTelemetry Android also, we have a lot of at auto-service annotation, and we discover those when we call service loader.load. So, if suppose, a customer app also has some of these things, and they are called calling serviceLoader.load.
And OpenDesometry, Android, some of those instrumentations are part of my SDK. Would it automatically have them load those classes as well via them calling serviceloader.load, but not via our internal serviceloader.load being called? Does that make sense?
Cesar Munoz 01:04:11 I'm not sure I fully understand. You mean that by a customer calling it, that will initialize yours? Your, internal stuff?
Surbhi Agarwal 01:04:19 Yeah, so our SDK depends on OpenTelemetry Android, some of the instrumentations that have at the rate auto-service annotation on them, but we do not call serviceloader.load. We initialize them separately via a separate install call.
But let's say the customer has some auto services, and they are calling serviceloader.load in their app. Would that initiate this also?
Cesar Munoz 01:04:46 Well, no, my understanding is… my understanding is that service loaded… load… Instantiates the classes that it finds in the class path.
And so it will, like, create new… new objects for those classes, which won't be related to the ones that you create yourself for… for your own initialization. So, it will kind of duplicate the instrumentation in this case, if anything.
Surbhi Agarwal 01:05:15 Yeah, that makes sense, yeah. Okay, yeah, I just got that confusion. So, why are we service provider interface? Is that something different than this?
We talked about, because of SPIA.
Cesar Munoz 01:05:31 Yeah, yeah.
Surbhi Agarwal 01:05:32 It was exaggerated, so, .
Cesar Munoz 01:05:36 Most likely, it's because of that, right now.
Surbhi Agarwal 01:05:42 Is it different than the auto service thing that we were talking about? It's the same, right? Service provider interface?
Cesar Munoz 01:05:49 Yeah, that's the way we automatically load them.
Surbhi Agarwal 01:05:52 Yo.
Cesar Munoz 01:05:52 in the SPI.
Surbhi Agarwal 01:05:54 Yo.
Cesar Munoz 01:05:56 They are.
But anyway, sorry, survey, I'm conscious of time.
Surbhi Agarwal 01:06:02 Yes, yes.
Cesar Munoz 01:06:03 We hit the timer.
But, you know, we can continue in the chat.
Surbhi Agarwal 01:06:09 Yeah, I did not have other questions. Thank you so much for the time today. It was a nice discussion.
Cesar Munoz 01:06:15 Yeah, it was. Thank you all, and talk to you in a couple of weeks.
Surbhi Agarwal 01:06:20 Thank you, bye-bye.
