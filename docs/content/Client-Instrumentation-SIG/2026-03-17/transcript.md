SIG: Client Instrumentation SIG
Date: 2026-03-17
Duration: 29 minutes
Zoom Recording URL: https://zoom.us/rec/share/XRwkHrIKATgud9kLx4LU2aRLWVPqw6fQbFQJpbGNKnBzBp86pXbBFdyXFs9noGXE.zR9Hh2KSICXebtLB
============================================================

## Zoom Recording Transcript

**Martin Kuba** 00:49 Santosh.
**Santosh** 00:52 Hey Martin, how are you?
**Martin Kuba** 00:54 I'm fine, how are you?
**Santosh** 00:57 Good, good. One second, I'm doing.
Alright.
I, I have a… One, one, one topic to discuss.
Let's see if other folks join. I think it is affecting the OpenTelemetry demo app.
Because that server timing is not a standard.
It is not… Widely implemented.
And, yeah, I think I'll give more context when… purple joint, yeah.
Actually, it's Alti902, I don't know.
**Martin Kuba** 01:57 Sandosh, I don't know if you've seen, but we… we had… we finally had our first release in browser.
**Santosh** 02:03 Oh, fantastic.
**Martin Kuba** 02:05 Something.
**Santosh** 02:06 Fantastic. I would like to catch up on that. You know, are you, available sometime outside of these hotel meetings, you know, we could quickly go over, yeah, okay, I'll ping you sometime. Yeah, basically, I wanted to understand more about how to transition, how to migrate from The existing instrumentations to the new one.
**Martin Kuba** 02:30 Yeah.
**Santosh** 02:30 Where can I… can you point me to the release? Is it in that new browser?
**Martin Kuba** 02:38 Yeah, it is. We're still kind of… It was the first reads we had to do manually because of NPM publishing.
So, we don't have, like, a release in GitHub, but if you go to NPM… hold on… There's… I'll just, send you that link.
**Santosh** 02:59 Okay, yeah.
**Martin Kuba** 03:04 And so far, it's only instrumentations, like, like, we still… Need to work on… Santosh 03:12 the SDK.
**Martin Kuba** 03:13 The SDK, yeah.
**Santosh** 03:14 It's fine, yeah.
I mean, the instrumentations are the… 3 anyways.
**Martin Kuba** 03:23 Yeah.
**Santosh** 03:38 I think, it might be helpful to also Write, like, a blog post or something, some article, describing How one should go about You know, migrating from the existing implementations to the new ones.
**Martin Kuba** 03:57 Yeah.
Yeah, it just… this just happened, like, last Thursday, so… Damn.
**Santosh** 04:05 Yeah, yeah, yeah, yeah, I think, Do you guys also plan to… Update the documentation page.
RR over time, once you have more usage.
At least between… among the, you know, guys who are actively participating, you guys can start using it, and… You know, make sure it is…
**Martin Kuba** 04:32 Yeah, you mean the documentation?
**Yeah, you mean, like, the documentation in… on the website, or on the… Santosh** 04:38 telemetry IO.
**Martin Kuba** 04:39 Yeah.
Yeah, we need to do that, yeah.
**Santosh** 04:43 Yeah. Basically, how should, developers consider… between the two options. Like, when should they use the current ones? When should they use the new ones? Is there anything they're going to miss with the new ones?
is that any… Like, what are the list of semantic convention changes?
**Martin Kuba** 05:05 Damn.
**Santosh** 05:06 the event model, you know, document, like, what are the… and these are all event-based instrumentation, they all emit events, right? Right.
**Martin Kuba** 05:15 Unlike… Santosh 05:16 you know, the previous ones.
**Martin Kuba** 05:19 That's right.
**Santosh** 05:20 Okay.
And you have also split between the XHR span versus the timing… event for the timing.
**Martin Kuba** 05:31 Right. Yeah.
**Santosh** 05:32 Right.
**Martin Kuba** 05:34 So far, we have, we don't have the resource timing instrumentation yet.
We have… we have the navigation timing.
**Santosh** 05:42 Okay. Oh man, I think I remember we talking about these things with Nev.
I don't know if it was a year ago or two years ago. It's.
**Martin Kuba** 05:53 Yeah.
**Santosh** 05:54 But, congratulations, I think your effort paid off. I think you are the only one who's, you know, who's sticking around from the original…
**Martin Kuba** 06:02 Yeah.
**Santosh** 06:03 of people.
**Martin Kuba** 06:05 Yeah, that's… this was, like, one of the… one of the reasons that I… that I switched, you know, I went to Grafana, because I could continue working on this. You know, Ted… Ted Young, who's… Santosh 06:18 Yeah.
**Martin Kuba** 06:19 one of the GC, MGC, like, he also went to Grafana from… from Lightstep, and… And, he, like… like, he think, like… he really wants this to happen, like, he really wants the browser to be successful, so… Oh.
**Santosh** 06:37 No, that's really nice.
**Martin Kuba** 06:38 Yeah.
**Santosh** 06:39 Nice, yeah.
**Martin Kuba** 06:43 I don't know if anybody else is joining, it seems… Santosh 06:47 Okay, let me get at least your thoughts on the server timing. Basically, what is happening is… let me share my screen… Okay, there is this, issue, that was opened, 2 years ago.
Okay, two years now. Which talks about standardizing, you know, the server priming.
based trace parent propagation in the reverse direction, from the backend to the clients. And the issue is, I think mostly with… just the initial browser navigation when you type the URL.
Right? You… you don't have… You know, your instrumentation loaded in the browser yet, so you don't have the opportunity to inject your trace context in your request.
And therefore, the browser makes the request.
You know, On its own, and then when you… when the backend gets the request, you know, it initiates the trace. The backend instrumentations, they initiate the trace. Now.
In that race, you know, we miss… The span for the request the browser made.
This is not an issue with the XHR and fetch calls, because there you have already loaded Your instrumentations in the browser, and they have the opportunity to You know, insert this header.
But it's just for the initial, document load, initial page load.
Page navigation.
**Martin Kuba** 08:42 Yeah.
**Santosh** 08:42 And not just when you type the URL in the browser, but anytime you navigate.
I think the browser doesn't… give an opportunity to your instrumentations to inject data. So every time you do a base page, so not… I use the term base page, that's, Wrong. But every time you do a navigation, as you click through links, but The links are not… You know, your route changes, but hard navigations. You know, you, you miss… You don't have the opportunity to insert, insert the ye.
**Martin Kuba** 09:17 Damn.
**Santosh** 09:18 header.
And so, what, these guys came up with… Is that let the server Propagate the trace context in the reverse direction.
And then have the browser generate a span after the fact.
So imagine… The browser made the request, the page loads, your instrumentations load.
And now, you know, they can look at the server timing header.
Get the, you know, trace context that the backend has used.
take the trace ID, generate another span with the same trace ID, There is a… There is… there is a spe… there is a span ID in the… in that, transparent header, but that span ID refers to the span of the APM side span, the server side span. That, ideally, should be your child.
Unfortunately, that is not, possible. I, I think… I don't know, you know, that part very clearly, but… It's hard to make that, you know, your span's child, because that span needs to have your span as a parent, and… you have lost that opportunity as well during the process. So all you can do is at least keep the server-side span in, let's say, in the span link.
**Martin Kuba** 10:58 So this, this applies only to the document… Correct. Document load span, right?
**Santosh** 11:02 Correct, correct.
**Martin Kuba** 11:04 So, like, the… Santosh 11:04 initial page navigation.
**Martin Kuba** 11:06 So the thing is, like, with the document load span, like, we… we can't… You can't… that span is generated after.
**Santosh** 11:14 Yeah.
**Martin Kuba** 11:14 Anyway… Santosh 11:16 Yeah.
**Martin Kuba** 11:16 And I think… Santosh 11:18 But now, it is orphan. It doesn't have any linkage to the backend spans. So we are trying to at least establish some form of linking.
What about?
**Martin Kuba** 11:29 What about the meta tag? Like, was… isn't that implemented?
**Santosh** 11:34 It's the same. So basically, it's the same. So, the… The intent is the same.
You can either propagate the, trace context via a meta tag, R… Via the server timing header.
**Martin Kuba** 11:51 Yeah.
**Santosh** 11:52 And I think the server timing header was… Preferred for some reason, so that…
**Martin Kuba** 11:59 Okay.
**Santosh** 11:59 you know, it is not HTML-specific, you know, it can be used. Actually, that part, I should read more. I don't know the… full… context. Like, is this concept required for other situations, too? If it is only for the document load, you know, you're right, that meta tag Can be, a way to…
**Martin Kuba** 12:24 Boom.
**Santosh** 12:25 But turns out that, you know, John, who opened this issue, he has linked a few links at the bottom.
where I see, you know, Grafana had donated you know…
**Martin Kuba** 12:40 Hmm.
**Santosh** 12:41 A plugin kind of a thing to… the PHP instrumentations.
Okay. You know, where you propagate the server timing as a header, the transparent in the server timing header.
**Martin Kuba** 12:56 Okay.
**Santosh** 12:57 And, and, and of course, you know, Splunk has, you know, their own distributions, like, some add-ons on top of what OTEL provides in there.
You know, we do the same thing.
**Martin Kuba** 13:15 Damn.
**Santosh** 13:16 So… That's what led To making an attempt to standardize this.
process.
But I think what I noticed later is… There's a second link here, I think I… I don't know what this… I think he… Jurassi, yeah. Jurassi… I think he used to be in Grafana, too. I think he had prototyped like, the context propagation to plant instrumentations via, I think, a different approach. He used… One second.
I think… I think he… he tried to introduce something called response propagators.
Hmm… Yeah, I don't remember now, but basically he tried to introduce a response, a formal response propagator.
Yeah, I see. As an API.
But I think this got closed, I think.
This… this was, again, how long ago?
Very long ago, so let's see when it closed.
**Martin Kuba** 14:59 Yeah.
**Santosh** 15:02 It's, that's also 2 years ago.
So the question now… okay, the reason I'm bringing this up is, in OpenTelemetry Demo.
The demo app, that is there.
it has… a proxy, an Envy proxy-based, component.
That is… That is not implementing this server timing.
propagation.
For all the, language-based apps, like the Python Go, you know, I think you can, you know.
Instrument with your vendor.
Proprietary, instrumentations, implementing the server timing adult propagation.
But for the Envoy proxy, I think it's not in our control. I think it is… It is coming from the Envoy proxy itself, I have to double-check. So that demo app, you know, breaks the flow.
Unless we disabled tracing entirely in that, in that proxy.
Service in that demo app.
**Martin Kuba** 16:18 Okay.
But it's only… but it's only for, like, the, like, very narrow use case of… of, like, the document load being linked to the, the server.
**Santosh** 16:28 I don't know if we should call it narrow, Because, like I said, every time I click on links, right, every time I, I click on… You know, a new link.
That, that applies.
**Martin Kuba** 16:48 Yeah.
Right.
**Santosh** 17:04 So, I think we need to get some advice from, Daniel… do. If we… so, one question is, does he join the browser sig? If so, I can… I can join and check with him, too, on what his latest thinking is.
**Martin Kuba** 17:27 Yeah, you mean Daniel the tailor? Yeah, yeah.
**Santosh** 17:30 Yeah.
**Martin Kuba** 17:31 He, he, he comes there sometimes, yeah, like… Santosh 17:34 Okay.
**Martin Kuba** 17:35 Yeah.
He's not, like, actively… he's not that they're, like, actively involved in the SIG itself, but he comes there from, like, the JS perspective, because they overlap, yeah.
**Santosh** 17:45 Okay, or I can join, the JSC too. I think the, it would be helpful if you get Caught up with this topic.
**Martin Kuba** 17:55 Yeah.
**Santosh** 17:55 And then, you know.
**Martin Kuba** 18:02 I wonder if you are… Santosh 18:02 hold on to this thought too, then I think we could approach together.
**Martin Kuba** 18:07 Yeah, I wonder if… I wonder if it'd be… Goods open… either move this issue log to the browser.
Repo, or, like, open a new one.
**Santosh** 18:17 It's up to you, I think.
**Martin Kuba** 18:19 God, I, I… Santosh 18:22 put both the links here. The main issue… the reason it is in the spec is… This is… this indeed needs to go into the spec anyway, because we do want to standardize it so that everyone implements this.
**Martin Kuba** 18:40 Right.
**Okay, yeah, I'll… I'll have to think about it somewhere, to be honest. But yeah, it's, I just call it… Yeah. Okay. Yeah, I think… Santosh** 18:58 my… I would also recommend that you… Get a perspective from… you know, from Grafana as well, like, your internal teams, the browser teams, as to how they are handling this situation, because they, you know, they seem to have added this, this functionality, right, here in the PHP…
**Martin Kuba** 19:23 Right. Yeah, I'm actually very curious about this, because, like, I don't know how that applies to back-end services.
**Santosh** 19:31 It doesn't, but it is the backend service that needs to, you know, inject that header.
**Martin Kuba** 19:38 Oh, good.
**Santosh** 19:39 So that the browser receives it.
Right. But, but, let's say… You know, some inter, you know, services communication, one back-end service.
**Martin Kuba** 19:50 Understood.
**Santosh** 19:51 corresponding to another backend service. There, this is not needed.
Which is needed only when you're… You know, backend services responding to browser.
**Martin Kuba** 20:02 Okay, yeah, that makes sense. Yeah, I… I'll have to look into it, because, like, so I work on the browser SDK that Grafana has, Pharaoh.
And I don't think that we handle that, but I'll have to double-check.
**Santosh** 20:16 Yeah, yeah.
**Martin Kuba** 20:20 Okay, yeah, thanks for bringing it up, bringing it up, so… Santosh 20:24 No problem.
**Martin Kuba** 20:30 Hansen's not here. I had, I had a topic, And maybe, like, I think I would like to… talk to the Android folks about this one, maybe next time, but I can… Just give you, like, a quick summary if you want.
I don't know if you remember, there's, There's a… there's been a discussion about, using sessions or modeling sessions as resource attributes.
**Santosh** 21:05 Right.
**Martin Kuba** 21:06 as entities.
So, that's… the entity's SIG is trying to figure that out right now.
It's very much related to… The metrics discussions we've had.
Which… which is, like, we don't want to have… we don't want to generate metrics. I think we have… And agreed that you don't want to generate metrics from the client, right?
**Santosh** 21:31 Aye.
**Martin Kuba** 21:32 And actually, part of the reason that That actually, like, supports this.
is, is, like, if we… if we model certain things as entities.
Like, the session, or even other things that, you know, apply to, you know, a lot of different signals, but they can change during the lifetime of the SDK, then that complicates the metrics.
Because every time you change resource attributes, then, like, the, you know, the dimensions change for the metrics SDK.
**Santosh** 22:12 Right.
**Martin Kuba** 22:13 So, the thinking right now is that… we… We could model sessions as entities, but But we would focus on spans and logs only.
And just, you know, say that, like, we would not handle it as metrics in the SDK right now, in the client SDKs.
**Santosh** 22:36 Okay.
That makes sense to me, and I… on the topic of metrics, I need to do some… some more research. I… I… where I'm at right now is… I think Jason… Pose this question that… You know, there are, counters that people Build in the client apps that… that… Sound like metrics, then why not emit like metrics?
Yeah. And, and I… I think I did some… brainstorming with ChatGPT, actually. So… I don't know how valid that is, but it… ChatGPT suggests that Unlike, server-side Applications. The client applications are more unreliable.
So you will often have to do retries.
Many times, your apps are offline, so you'll send data later.
You know, many hours later, and And, and we have to see… and if you do a retry, you know, typically metrics, unlike events and spans, you know, spans have an ID, right? So if you send the same span again, you know, you know, hey, I received a duplicate, but with the metric data point.
I don't know.
**Martin Kuba** 24:10 Yeah.
**Santosh** 24:10 any item pertinent.
P.
That tells your server that, hey, I received this data point previously.
So… .
**Martin Kuba** 24:25 Yeah, that's another complication, yeah.
**Santosh** 24:27 Yeah, so… so they also… so it's… ChatGPT ultimately recommends against, and it basically supports, you know, the direction, I was suggesting that, yes, I think this is best.
**Martin Kuba** 24:39 Yeah.
**Santosh** 24:40 Sent as events, and then converted to metrics in the backend.
**Martin Kuba** 24:44 Yeah.
And one of the suggestions, like, that, I think actually Daniel had… Was that if it's… if it's about, like, the… Like, the semantics, like, of the API.
Then we could have, like, a… kind of a, like, a… And you could still have metrics API, but that would just generate events in the background.
**Santosh** 25:08 Yeah, yeah, yeah. Yeah, so the API remains, but the SDK will change it to events, yeah.
**Martin Kuba** 25:21 So I need to… yeah, I would like to discuss this with the… with the Android folks, because they… Santosh 25:26 Yeah, I think, what?
I think we need to couple this thought with your other idea.
off… you know, there is a processor in the collector, right, which converts spans to metrics. If we are able to come up with conventions.
Even if… it doesn't have to be a standard, but at least, you know, some… Briefly agreed conventions that, hey, if an event comes in this form.
And if it turns to this… Processor, you know, this is how we create metrics automatically for you.
You don't need to… you just need to configure this processor in your pipeline, and boom, you get metrics.
**Martin Kuba** 26:09 Yeah.
**Santosh** 26:09 So, if such a software exists.
Then these two, you know, could be… Presented together as a complete solution, and then… And remember, this collector processor is only a reference implementation, because for most client Telemetry, you don't use collectors.
In most situations, so it serves as a reference for vendors to implement in their backends.
**Martin Kuba** 26:41 Yeah.
**Santosh** 26:42 Yeah, and one more thing that I need to go validate, and you could help there too, that if we were to send metrics directly from the client instrumentations.
Does the existing metrics backend that all vendors have, do they support Receiving a large number of, you know, metric data points.
They are not built for… Such a high volume.
on, you know, metric data punch.
**Martin Kuba** 27:14 Yeah.
**Santosh** 27:15 Typically, you know, you would aggregate them and send a far smaller number.
to Dimitrix back-end, so it may not even be… more than the support, I would say they may not be ready, today. Like, even Prometheus, you know.
We have to do some, You know, research on how ready, you know, these metric, platforms are.
On the contrary, though, there is, this… Sentry, this vendor sentry, they, they, Support sending metrics right from the client.
**Martin Kuba** 28:06 Okay.
**Santosh** 28:06 Client… from the clients.
But we don't know what happens under the hood.
**Martin Kuba** 28:16 Okay.
**Santosh** 28:16 Yeah.
**Martin Kuba** 28:20 Yeah. The next step, like, for the browser's sake, is to actually work on, like, end-to-end demo.
**Santosh** 28:28 Yeah.
**Martin Kuba** 28:29 So… and I think this should be part of it, just, like, the backend generation.
**Santosh** 28:34 When does the browser SIG, meeting happen?
**Martin Kuba** 28:37 It's on Thursdays at 8.30.
**Santosh** 28:40 Okay, yeah, yeah, okay, I have a conflict.
Okay, I'll try.
**Martin Kuba** 28:47 You can watch the recordings, and we can also catch up on Slack.
**Santosh** 28:50 Correct.
**Martin Kuba** 28:51 Got it.
**Santosh** 28:51 Yeah.
**Martin Kuba** 28:54 Alright, I need to drop, but yeah, I do.
Sounds good. Good talking to you.
**Santosh** 29:01 Who cares.
**Martin Kuba** 29:01 See you later.
