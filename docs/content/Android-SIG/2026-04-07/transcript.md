SIG: Android SIG
Date: 2026-04-07
Duration: 55 minutes
============================================================

## Zoom Recording Transcript

**Cesar Munoz** 01:01 Hello.
**Surbhi Agarwal** 01:04 Hello?
**Cesar Munoz** 01:11 I see people are… Still joining.
**Surbhi Agarwal** 01:23 I'll add the agenda item I had for today.
**Cesar Munoz** 01:29 You have one?
Sorry, come back, I didn't surveyed? I didn't get it.
**Surbhi Agarwal** 01:37 I'm saying I'll add the agenda item I had for today quickly.
**Cesar Munoz** 01:42 Oh, got it, got it. Thank you.
**Jason Plumb** 02:01 Cesar, I will miss next week. Are you around to run it next time?
**Cesar Munoz** 02:07 Next week, yes.
Cool. Yeah.
**Jason Plumb** 02:14 Thank you very much.
**Cesar Munoz** 02:16 No worries.
By the way, I won't be able to stay until the end of the meeting today. Need to… Late earlier, so… Probably half.
an hour.
From now.
**Jason Plumb** 02:40 Okay, cool, if you have anything that you want to prioritize, feel free to jump in there and boost it up.
**Surbhi Agarwal** 02:46 I have a question as well for Cesar, so please, include me as well.
**Jason Plumb** 02:52 Cool.
**Cesar Munoz** 02:53 Yeah, I really just wanted to follow up on the, the block PR… we talk… the last week's meeting, Jason, if you have any inputs on that.
Well, I mean, it's something that you can… Also, check out offline.
Unless, I mean, if you have any… comments or something that we should discuss over here, just let me know.
**Jason Plumb** 03:21 Was it this one?
**Cesar Munoz** 03:25 I think so. I have two… I think that's the one, yeah.
**Jason Plumb** 03:29 Yeah, okay.
**Cesar Munoz** 03:29 You must… And, survey. Sorry, which question?
**Surbhi Agarwal** 03:37 So, there was this new requirement wherein there was a need to ignore URLs from being instrumented by the OKHTTP3 instrumentation. So, I looked around in the Java instrumentation repo as well. There are some issues, and There are a few ways, right?
The suppression… using a suppression key in that context is a way, but that has downsides.
Particularly if there is another request within those interceptors that is, generated within that same context that is supposed to be suppressed, those downstream… Requests which aren't the same URL as that needed to be ignored would also be suppressed, so suppression key doesn't work here. Samplers is another way.
So, what samplers do is, like, you can tell that record, but don't export. So they still propagate the context to the server with the flag that… this flag of sampling as 0, that this should not be sent to the server.
They work, but the downside there is samplers are at trace level, so not just for OKHTTP3, they would run for all the instrumentations. We can have a flag there that it checks the URL and only samples HTTP spans out, but that is not ideal, to have the sampler, all the traces go through the sampler unnecessarily. So, like, the best ideal way here is to add a config to ignore URLs that can directly be used in our connection error and tracing interceptor directly to be able to not create spans out of any specific URLs. So, I'm not sure why… maybe Java did not need it. Samplers was a good enough, solution for them, but I do not… I think that's not ideal. So, like, I wanted to see, have you looked into it before? Do you have an idea of what it should be?
**Cesar Munoz** 05:49 Well, what I remember, the context, parameter that you mentioned.
It's something that we added because we… you know, The exporters that are in…
**Surbhi Agarwal** 06:03 Yeah, the offspring…
**Cesar Munoz** 06:04 repo, they use OKHTTP to export data, or at least the ones that I was using, so… that was a way to avoid the exporter to export the data for that, you know, for the URL queries that they would make themselves, so it's kind of like, to avoid creating this telemetry of the telemetry exporters.
So, so… I think that's expected, that the full kind of downstream Http queries that start from there are avoided as well.
**Surbhi Agarwal** 06:44 Yes.
**Cesar Munoz** 06:44 Aside from that, It's kind of like the config that you mentioned, where we can add a sampler Or maybe just a processor with, with, With some logic to escape some… some stuff.
I think that would be the right approach, but I'm kind of confused why… it has to be targeted only to the URL Only if it's… queried.
from OKCP, you know? It's kind of this targeting of just OKTTP, It's kind of… it's kind of odd.
I mean, why would it be a problem to filter that URL regardless of what's the HTTP client tool?
**Jason Plumb** 07:38 I'm also curious of what the use case is, because I don't fully understand why we're trying to ignore URLs on the client side.
**Surbhi Agarwal** 07:45 Oh… like, certain URLs, which could be… internal, and customers might not want to… and they do that often, like, maybe some permission requests, some of their internal requests that they do not… I do not know the specific use case, but I'm just, thinking here that that could be it.
And, like, they do not want only specific URLs. Any other URLs originating… inside of that URL… like, any other URLs, they don't want to, like, if, say, interceptors are there that call another request.
they would… if the URL there is okay to be intercepted, they would want it to be, traced.
I do not.
**Cesar Munoz** 08:41 Got it, so…
**Surbhi Agarwal** 08:42 exact use case, yeah. I'll try to, gather that.
**Jason Plumb** 08:46 I think the reason this doesn't exist elsewhere is that it probably is expected that people actually want to see what their clients are doing, instead of ignoring some requests. And then the second part is, I think most people would just set up a rule to drop this in the collector.
**Surbhi Agarwal** 09:04 There is a way, like, you can use span interceptors also.
But, like, then you have done all the work.
And you are dropping it in the end.
That is not.
**Jason Plumb** 09:18 True.
**Surbhi Agarwal** 09:19 Like, you want to stop it before, tracing in the very big… wherever possible, quickest.
**Hanson** 09:27 So, I guess…
**Cesar Munoz** 09:28 I can think of a…
**Hanson** 09:31 Go ahead, Cesar. Sorry.
**Cesar Munoz** 09:34 Thanks, Hanson. Yeah, and I was just gonna say, I can think of probably a security use case, a customer wouldn't want specific endpoints to show up in the logs or something.
But if that's the case, in that case, it would be strange for me to see it working only when I hit that URL using a specific library, you know, rather than… you know, just when I hit that URL, regardless of whether I use OKHTTP or… whatever. So… so… that's why I was asking that. And I mean, there's also, in a general… general… For a context-wise, it's useful to ignore some URLs.
Which is the case of ignoring the… traces the spans for the internal URLs that exports data, because otherwise you will create, like, a… kind of like an infinite loop Of, you know, spans that are, you know, creating spans for each exporting, that then creates another span, and so on. So… There are some use cases, I just don't see them… I just don't see the need to target a specific client's HTTP.
to… to filter those, only for that client. That's why I was asking why only OKHTTP Filters are needed.
**Surbhi Agarwal** 10:56 Could it be seen similar to, like, say we have, let's say, known methods config, right? We have it separately on HTTP URL and OKHTTP3 instrumentations. Going via that logic, shouldn't this also a configuration go into… you are right, but the downside of that… Like, samplers would help here with the… use case that you are suggesting, that no matter what the HTTP client I'm using, I want to drop the spans But, thinking in terms of, like, when you set up these instrumentations, you set up certain configs for them, that's where we are setting other configs as well, per instrumentation level.
Why should this config live separately? Yeah, Hanson, go ahead.
**Hanson** 11:49 Sorry, I'll go back a little bit. So I think there are two separate issues here. One is whether there's use cases here, and two is how do we configure if we have use cases. And I actually do think there's definitely a use case here, because there are some URLs that you, like, for security reasons, for other reasons, it… could be too chatty with certain URLs, and they don't provide enough signal, and HTT requests can be a large majority of the data being recorded. So, having certain URLs being filtered out, I think, is a reasonable thing. We already do it, like Cesar said, with the OTLP endpoint that we do. So, I think there are use cases. Embrace supports this. I think other people are very careful about what they want to record from the client side. There's also potentially identifying information when you record, certain requests being made to certain URLs. So there's… there's implications there. So I think we can come up with use cases for it. In terms of how you configure it, If we're talking about configuring instrumentation, then these are instrumentation-level configurations. So conceptually, it should be applying to all URLs and everything, but the SDK only has so much control, in terms of you know, get rid of all HTTP spans, with this particular URL. We could do that at the, at the, at the exporter level, but you're still going through the thing. So… it is more convenient to send it in one place and basically apply it SDK-wide, but it kind of breaks a bit of the encapsulation that the instrumentations have in terms of what it records and what it doesn't record.
So…
**Surbhi Agarwal** 13:37 So, I also came across a counter-argument while you were, saying that, Hansen. So, basically, when I use a sampler, at least to the server, I am telling that this is sampled out.
But when I am using a span interceptor as the SDK level to, in the end, just not send the… export the span, I lose that information, right? Server still sees it as sampled, because the trace context has already propagated to the server.
So, sampler is perhaps better than using a span interceptor in the end of a span processing lifecycle, right, just before.
**Jason Plumb** 14:21 Yeah, I mean, this is why… sorry to jump in, Serbia, but this is why I'm asking about the use case. Like, you're suggesting that maybe, in some cases, you don't want to create a span on the server side, and in other cases, some other people might want to have a span on the server side. I don't know what the use case is.
**Surbhi Agarwal** 14:38 Yeah, to clarify, like.
Yeah, so yeah, you guys are right that I need to figure out the use case. There are a few nuances here. So basically, what I was saying was, let's say, A request is going on, and underneath that request, Client itself creates another request.
But the use case I am thinking is the first request they want to ignore.
But they do not want to ignore the other request that arises in the context of the first request. So, like, that's why I thought context suppression wasn't a good strategy. But, yeah. And then the server part, I do think that the server request should also be ignored.
And the flag should be sent to the server. Samplers help there.
Yeah, I think I'm a bit confused about the use case myself, I need to figure that out.
**Jason Plumb** 15:36 Okay.
I mean, feel free to open an issue on this, I feel like it's a reasonable thing to ask for, and for us to track.
**Surbhi Agarwal** 15:43 Yeah.
**Cesar Munoz** 15:44 Yeah, definitely. I mean, there's many ways to… Addresses, it's just that… Yeah, I agree with Jason, and unless we have a concrete use case, we probably won't make the best decision.
**Surbhi Agarwal** 15:57 Yeah, that sounds good. I'll figure that out and create a issue.
**Cesar Munoz** 16:03 Thank you.
**Jason Plumb** 16:10 Thanks, Serby.
Clever Chuck, it's good to see you back. It's been a few weeks, I think.
**Hanson** 16:28 Sorry, before we move on to the one, I just saw the… whoever posted the, filtering span exporter build… builder, that… that would… that would accomplish the use case I think we should support. So, anything, above and beyond, yeah, some concrete use case would be nice.
**Jason Plumb** 16:47 That's kind of why this exists. I think this goes all the way back to, like, the Splunk days, and I think we just wanted to allow users of the SDK to be able to not include spans based on whatever criterias they wanted to.
So that's why this exists, but it doesn't address the sampling case where you don't want to propagate context, or that you want to let the server side know that you've been sampled. This doesn't address that. And you still have to do the work, right? You still have to create the span.
put attributes on it, stop the span, and then throw it away, right? So, if those are concerns, then this doesn't fit that, but… Yeah, that's why… I think that's why this exists.
I don't know what it takes to wire this up these days, probably you can't with the agent, I'm guessing.
**Surbhi Agarwal** 17:35 I think it would probably also, like, I'll try to figure out the exact use case we have, but it would perhaps help for all of us also to think of what should be the general use case, right?
**Jason Plumb** 17:47 Yeah.
**Surbhi Agarwal** 17:48 Yo.
There are a few things here, I'll lay them down in the issue.
**Jason Plumb** 17:53 But I'm not sure that the… I mean, only looking at OKHTTP, like, if we wanted to address it at the instrumentation level, I don't even think that the instrument… the instrumentation API is set up very well to do this kind of filtering.
Because we're still using the Java Instrumentation API for those things, right?
**Surbhi Agarwal** 18:12 Yo.
**Cesar Munoz** 18:12 Yeah.
**Jason Plumb** 18:13 And I don't think there's a good mechanism for not starting a span, or not creating a span.
**Surbhi Agarwal** 18:18 Sampler and the, context suppression are the two ways that the instrumenter offers, yeah.
**Jason Plumb** 18:24 Yeah, exactly.
It's, like, in this thing… this thing, right?
Yeah, anyway… Okay, we'll have a tracking issue.
**Surbhi Agarwal** 18:38 Yeah, we definitely have to change the tra… the multiple places, like, we have to change the Java instrumentation codebase if we were to go the instrumentation-specific way.
**Jason Plumb** 18:50 Yep.
**Surbhi Agarwal** 18:52 Yeah.
I also wanted to bring up, like, the unified semantic convention issue, if we had time.
Do you guys think we can bring that up?
**Jason Plumb** 19:14 Yeah, which issue?
**Surbhi Agarwal** 19:16 I'll share that.
So… I wanted to ask Hansen to… help us. So, last time we chatted about it, I added the link in the converse… in the chat, so… Jason, you added the complex attribute, how they should look like, and…
**Jason Plumb** 19:40 Yeah.
**Surbhi Agarwal** 19:41 So, we can discuss that as well. So, I checked with our backend, the Splunk backend, and they are able to consume it.
As long as everything comes in one span, they do not care about what kind it comes in. Like, here, a complex attribute is workable. So I wanted to ask from Hansen and Caesar, what do they think their backends can consume such a complex attribute or not?
**Hanson** 20:13 So complex attributes, I think we're still figuring out. So… It doesn't really matter if I'm abrasive or it doesn't have, So, this is almost aside from the embrace backend, but I think complex attributes, I don't know how well supported they are right now, because I feel like they're pretty new.
supported in all SDKs, or at least a handful of them?
**Jason Plumb** 20:36 I think a handful of them.
**Hanson** 20:39 So if… if… if that's the case, then putting, and are there any semantic conventions that leverages, complex attributes right now?
**Jason Plumb** 20:49 I… let's see, I… Yes, okay, so I think some of these, like, Gen AI ones I found, but it's still, it's still very fresh, so, like, the way it looks like in the semantic conventions are…
**Hanson** 21:03 Oh, yeah.
**Jason Plumb** 21:03 here's this thing, and this is in the registry. Type… so they just do type any, and then they throw examples in here, so it's like… It's a pretty broad stroke here, like, there's no real way to say what the schema for this looks like.
in the semantic conventions yet, and that's a shortcoming of Weaver, I believe.
**Hanson** 21:23 it's basically saying there's a blob with stuff, so… That's all it is.
**Cesar Munoz** 21:27 How did that get merged?
**Hanson** 21:29 it… I… so, given… given that… we're using a complex attribute the Unless there are use cases where, a complex attribute is explicitly spelled out in terms of these are the five things you would expect inside this payload of this shape, you're almost saying there are no there are no semantic conventions. Here are some recommendations we could dump in there. And if that's the case, I would… at least prefer, at this point, straight-up attributes, because they are easier to reference.
Now, if there's a push that is strongly saying, you know, if things are together, please clump them in a complex attribute, maybe we should do that, but I don't know if there's a recommendation there yet. And maybe this is me being conservative.
but rather have this be defined in a place where everybody could use it, everybody's understood… understands it, and Weaver supports it as well. Because, going, like, you know, being the first mover here doesn't buy us anything in terms of advantages. And going to something people used to, like, already understand, I think makes a lot of sense.
**Jason Plumb** 22:45 Yeah, I mean, I understand where you're coming from. The guidance, the reason why… This constraint, or the fact that Originally, only logs had these rich, kind of any type semantic conventions, these, whatever we're calling them, these attributes.
structured, or what… I forget, what are we calling these?
Complex attributes, yeah. So, I think only logs had it, and that was relaxed, so that it could be anywhere, both for consistency's sake, but I think exactly to handle use cases like this, where you have an attribute of something, that's something, in this case maybe being a span.
and it has characteristics that, you know, would be clumsy to flatten, right? Like, we saw up above in this same issue, like, it's just a pile of text there, and it's all attributes, and there's a lot of, you know.
There's a lot of structure that gets flattened.
So, I think I'd be curious to check in with the Semantic Convention folks and see what they'd recommend at this point. Like, are we ready for people to start using like, speccing out complex attributes, and if not, like, what do we think the timeline on that is, or when… when… like, what needs to happen for that to… to move forward?
I… I hate to block… this idea, waiting for… like, I think it's… I think it's probably a bad idea.
to block any sort of progress on this, based on Weaver or semantic conventions not yet, like, allowing for kind of, like, this schema to be spec'd out. I think we should move forward, spec… probably just spec it as flat, and then circle back if… if needed, if desired later, because it's not going to be stable for a while.
**Surbhi Agarwal** 24:35 This also, like, makes me think, like, the example we looked at, maybe complex attributes are meant for scenarios wherein you don't know beforehand what the structure could look like.
And you want to throw in any attribute where people can dump in stuff.
And backend can accordingly process it, like, have their own internal contract. Here, we do know what the, like, what value does it add for us to use complex attributes here?
We would, like, we could have the same argument for, like, the HTTP span. Why not have… why have them flattened? Why not have a attribute containing all the HTTP attributes inside of it?
**Jason Plumb** 25:20 Well, because there is structure to this, right? This isn't just a bag of attributes, it's not just a collection of things, like, the start time and the end time for the DNS query are related to each other.
**Surbhi Agarwal** 25:31 There is also… there is also, like.
**Jason Plumb** 25:36 Tender.
**Surbhi Agarwal** 25:36 implementation issue. So, like, in HTTP, the argument could be you receive those at different points, and you add them at different points in the code. Similarly, here, we receive them at different points, so we want to add different… at different times. Otherwise, I'll need to keep a track of a map of the call and this complex attribute, and finally dump it into the log. Rather, I could have done it one by one whenever I received them.
**Jason Plumb** 26:08 Yeah, I think I see what you're saying, but you can always replace the attribute value. So, right, so if you had an object that represented this.
You could… you could just re… you could set that.
every… like, anytime you get, like… now you get the TLS handshake end time, you can update your object and then set it into the attributes.
then maybe it's… maybe it's challenging. Like, maybe that's a lot of…
**Cesar Munoz** 26:33 it would be Re-adding a full set of attributes.
**Jason Plumb** 26:37 Yeah, do you have to walk the tree? Maybe you have to walk the tree and do all the type trickery? I hate it so much.
That's a good point, though, Servi.
**Hanson** 26:45 you'd probably want to synchronize it, and then grab the latest, modify, slop it back in, da-da-da-da. So, there are, I think, implementation limitations, especially if it's not supported by the SDK level. Like, is the SDK gonna support, like, modify attribute, for complex attribute? like, you know, to make this a little bit ergonomic? Or is it just gonna be, like, writing once as a big blob? But… I think modeling it is complex.
if all else being equal, SDK support, and, you know, Weaver support, tooling support, I think it is nice to be able to group together, things, especially when you don't want to have one there and not one there, and you want to tell that, hey, they both coexist, and they really should be logically a thing.
I mean, this could be one attribute, this could be three attributes, one for a request, one for response, you know, however you want to shape it. So there is… there is benefits to grouping it together. I think the reason why right now I'm saying flatten it is I worry about tooling support and how much work it's gonna be to, like, go back and forth and make sure people actually, are able to use this. If you have a very specific platform use case in mind, and you don't mind going through the, the, being the guinea pig for this, I think it'd be interesting to go with, the complex attribute. But…
**Jason Plumb** 28:19 Yeah, I don't think… I don't think we should hold it up for this.
**Surbhi Agarwal** 28:21 Yeah, it has been long held up. I have.
**Jason Plumb** 28:25 Yeah.
**Surbhi Agarwal** 28:25 with this one.
**Jason Plumb** 28:28 I know, like, this has been a while.
**Surbhi Agarwal** 28:30 Yaw.
**Jason Plumb** 28:30 Yeah.
Yeah, I think we just… I think we just do something like this. This is great, I think. Yeah. Yeah.
**Surbhi Agarwal** 28:37 For now, yeah.
Okay.
**Hanson** 28:40 We can always deprecate this and move to the structured one when that's ready.
**Jason Plumb** 28:45 Yeah.
**Surbhi Agarwal** 28:47 Yeah, and another thing that I wanted to bring up was, Hanson, you mentioned that you would instead like all the original HTTP attributes to be replicated here as well, whereas I proposed only the ones that are needed for filtering and aggregating the metrics that can come out of it should be there. So, like.
My… your point of view was that… why create two signals? Just dump everything in one signal, right? And the backend can process that one signal. And my point of view was, this is an additional signal for a very specific reason, and, like, people can enable it as needed, right?
So, like, this is a separate use case, and the HTTP span still stays anyway, right? So, like, I wanted to understand the rationale.
**Hanson** 29:40 Oh, I think my, my, my viewpoint is just eventually, hopefully, we can move to something where, the, the actual excuse me, signal is irrelevant if all the data's in the same place. I don't want to block this.
So this would be, like, we could easily just get this in, and then, modify in the future if we want to, say, just forget about the span, we just want to log an event that basically says there's a successful HTTP request here, or a failed HTTP request here, these are all the attributes, and not have to, like, bring together, two different signals, from two separate pipelines, just to do, one thing, but I don't want to hold this up. As you said, it's been long enough, so I'm okay with just, you know.
Doing, going with this.
**Surbhi Agarwal** 30:26 Yup.
**Jason Plumb** 30:26 One interesting aspect that I hadn't thought about is that if we do it, if we model it as an event.
and instead of these just being attributes on the HTTP span, then you kind of… need this to be required, right? You almost want to say.
that the span context is necessary, because if you imagine this event without any HTTP context, it's kind of misleading and maybe worthless.
**Hanson** 30:52 Yeah, this is effectively, like, an async baggage that goes with the span, that we only…
**Jason Plumb** 30:58 Right.
**Hanson** 30:59 After, because sub…
**Jason Plumb** 31:01 Yeah, and I haven't seen any prior art of requiring a span context, at least according to the data model, it's certainly optional. And you could build… you could certainly build code that makes this event without span context, but it's a mistake to do that.
**Surbhi Agarwal** 31:15 Yo.
That… that is… yeah, that makes sense. I will add that it is required as well in the spec.
I think those were the open questions I have, so I'm glad we could have a consensus.
Now, there is another problem. Earlier, BrowserSig was on board. Now, I think because it was delayed, or I don't know, now they want to… or maybe they think that some of these naming is confusing for the browser world. So, they are thinking, should we have a separate, semantics, rather than rely on the same one. So, I'll talk to the browser sick this Thursday and get their opinion and get this through.
**Jason Plumb** 32:03 That's cool. I mean, the… part of the reason why they split off is so that they could have some variance and not be encumbered by the rest of the client world. So, I mean, if it's duplicated, it's duplicated. Like, if there's different things for browser and mobile, then I think it's fine. It's not… I think none of us love it, but there are differences.
**Surbhi Agarwal** 32:23 Yo.
**Hanson** 32:24 For mobile, we would… we would want to have some interesting, Like, I think this, if you scroll back up.
**Jason Plumb** 32:33 Yeah, yeah.
**Hanson** 32:33 Yeah, so, like, right now, like, call start time is about the HTTP request being set. So, for mobile, it would be nice to have, a start time, where it's, like, when it's enqueued. So this is not included, but that's fine. We could always add it on top of that. So if the browser folks have something that is completely, like, redefining these, then it might be an issue, but if they have something like new lifecycle events, that happen before, after, or during.
then it's just an addition. So.
**Jason Plumb** 33:05 And these should correspond to span start and span end, but I also understand, like, because we're talking about these very fine-grained network timings, that they may not be identical, right? The time with… the time at which the app requests to initiate an HTTP request might be different from… When? Yeah, yeah.
**Surbhi Agarwal** 33:24 That happens. They are a bit different, yeah. And I need to look into what should… like, the… right now, this request duration is governed by the span duration.
Which is probably correct, because people have thought through it, and that's why it exists, right? But I am not very convinced. Should it be the call start and call end time difference, that should be the duration of the request, or should it be the span duration?
Right? Like, they are a bit different.
**Hanson** 33:57 they… they should be virtually the same. It's whether the network library's determination of execution time and the actual execution time of the underlying requests. I know OKHDP does something interesting, in that…
**Jason Plumb** 34:14 Westcue, maybe, right?
**Hanson** 34:15 No, no, even funnier, the actual server time, so the actual start time of the request is actually… the most accurate one is obtained from the response, because it goes down so many levels. It actually records at a time where you don't actually have access to it, so that is a more accurate time, versus, the time where you think you sent it to be executed is not quite the right time, and that's separate from the in-queue time. The in-queue time is, like, a totally different concept. This is purely, like, when did I actually start the request thing? And I think the span, it depends on how you're logging it, could be the earlier time, and… but you could also probably get the later time if you want. And what this time would be.
It depends on the implementation.
**Surbhi Agarwal** 35:05 What I… that is interesting. There are, I think, multiple things here. I, what I noticed was, like, the span starts after, the call start time, and it ends before the request for the end time.
So, yeah, there are some, like, nuances here that needs to be looked into. If there could be a conclusive thing to say here, I'm not sure.
**Hanson** 35:33 Yeah, so the important part is what we're… Having the implementation is like a separate issue, almost, but the important thing is what we actually say the description is. So if we say, network call starts or fetches begins, then that should equal, or roughly equal, to what the span, because for the span, that start time is about, like, execution. So if we, in the description, basically match the start and end time.
then it's just a job for the implementation to get as close as possible. And if you want to introduce different concepts, like queue time, that's something separate.
The end time thing, though, is, again, the response end time, so the la- so the connection, is closed, and the last byte is… is kind of, you know.
**Surbhi Agarwal** 36:20 On the Zoom.
**Jason Plumb** 36:21 The action does not necessarily have to close.
**Hanson** 36:22 So, not the connection. No, no, the request, the last byte has been, has been sent. The TCP connection could still be alive.
**Jason Plumb** 36:31 You mean the response. You mean the last bite of the response has been read?
**Hanson** 36:36 Yes. Just… just… just read. Not parsed, and… and not, like, deserialized. Just read. Just…
**Jason Plumb** 36:43 It's.
**Hanson** 36:44 wire.
**Jason Plumb** 36:45 There are plenty of cases where an HTTP client will send a request and not even bother to read the response.
**Surbhi Agarwal** 36:51 Yo.
**Hanson** 36:53 yes.
**Jason Plumb** 36:58 I mean, it's complicated, for sure.
**Hanson** 37:00 Yeah, yeah.
Yep.
**Surbhi Agarwal** 37:04 We sort of end the response as soon as the last network interceptor is done with its work, right, in a finally block, and the, like.
They could still be reading, like, there could be other network interceptors that the consuming apps have, where they are parsing the body So that goes in the response body, but that does… that goes in the response body end time, I guess, but that doesn't go in the span duration, that time difference.
So, should that be included? That…
**Hanson** 37:39 So spam body doesn't get, locked down until all the, all the interceptors are done.
This is what you're saying.
Versus the span duration ends at the interceptor that has basically sucked up the last byte.
**Surbhi Agarwal** 37:54 That's true, yeah, that's true.
**Jason Plumb** 37:57 And isn't there also some complicated nonsense with, like, trailing headers?
Like, there can be headers that exist, like, after the body or something?
I'm not saying we need to account for that, I'm just… I think… I think the spec has, like, some… 8, like, trailing headers.
**Hanson** 38:17 I feel like this… the attributes defined right here are very, in line with OKHTP and its lifecycle, so it has some kind of, you know, very specific client weirdness to it. So it's almost like… we should define these as agnostic to implementation as possible, and then get as close as possible, when it comes to, the actual implementation. So…
**Surbhi Agarwal** 38:48 That makes sense, yeah.
Can I request both of you to, like, put your concluding thoughts and give me a sort of approval, so I can take it to the semantic SIG and tell them, hey, see, Android is on board?
So can we get this merged?
**Jason Plumb** 39:07 Well, that's just an issue, right?
Is it a PR?
**Surbhi Agarwal** 39:11 It's an issue, like, this is for getting the semantic conventions in. I'll get there, go ahead to create the.
**Jason Plumb** 39:18 But you're talking about this PR.
**Surbhi Agarwal** 39:20 No, I actually, I did not create a PR for Symantec Convention's repo. First, I didn't create that.
**Jason Plumb** 39:25 Okay.
**Surbhi Agarwal** 39:27 So, but if you guys can give me a go-ahead on the issue, I can talk to Symantec folks and see if I'm ready to create a semantic convention PR for this.
**Hanson** 39:39 Yeah, part of me thinks, we shouldn't be too tied to a HTTP, but I think it's harder for us to do that, because that's where we're getting the events from. And that's how the implementation's gonna work. So how do you define something that is agnostic.
generic, but require an implementation that doesn't provide that specific information. So we may have to just kind of, like, you know, do some little hammering, but I'll try to take a look.
**Surbhi Agarwal** 40:09 Okay.
That sounds great, yeah.
**Jason Plumb** 40:17 Cool.
**Surbhi Agarwal** 40:17 From my side, yeah.
**Jason Plumb** 40:21 Do you know that Cesar wanted to come back to this one and get it approved because… specifically because we have this milestone.
And we… need to do a release. Like, we are behind.
Right, so we haven't released since February, we're already in April now, so we're definitely behind schedule.
And that's one of the things remaining.
For the 1.3 milestone.
So, I think that we should probably merge this. I think we're getting very close. I think he was just probably waiting on me, and I've been dragging my feet.
And then no one, I think, has started stabilizing session yet, which we… I think talked about and said it'd probably be fine.
And this happened, so we got the new contribib, which had some changes to disk buffering. I think there was a fix in there, actually. And then… Where are we with this now?
Did those get merged?
**Surbhi Agarwal** 41:21 1pr is open.
**Jason Plumb** 41:25 Which one?
**Surbhi Agarwal** 41:27 It should say something regarding Nav… no.
Let me find out.
**Hanson** 41:35 Are we just doing compile only? Is that… Is that what that's about?
**Surbhi Agarwal** 41:40 I removed a dependency preferences for a dependency AndroidX fragment, because that's what was actually used. So, preferences was a bigger one.
**Jason Plumb** 41:51 Did we merge it?
**Jamie Lynch** 41:52 I think Sazaar might have merged her.
I appreciate that, yeah.
**Jason Plumb** 41:56 Was it this one? It was 6 hours ago, yeah.
**Jamie Lynch** 41:58 Yeah.
**Jason Plumb** 41:59 Okay.
Yeah, Serby, that got merged.
**Hanson** 42:02 So it's just a leftover dependency that we don't need anymore.
**Jason Plumb** 42:05 Yeah.
**Hanson** 42:06 Okay, cool, that's easy.
**Surbhi Agarwal** 42:08 Yeah, we needed a different dependency that was coming from inside of it.
And we instead added that. So, like, there are some next steps to this issue.
I am talking to my team of when I should pick those up, so basically, or if I should pick those up, right? There's a debate going on right now.
**Jason Plumb** 42:30 Yeah, so I… sorry, Serby, I threw this into the 1.3 milestone, though. Do you think that… so, if this is still open.
then that's gonna hold… that's gonna hold up us releasing 1.3, because I think it is important that we don't… Force our dependencies down users' throats.
Right? That's not… being a good… citizen.
So what's… what's… I'm not clear on what's remaining on this.
**Surbhi Agarwal** 42:56 Yeah, let me, lay that down. So, like, based on what we discussed, what's remaining is We last time discussed that we want to… the solution for removing some of the dependencies from the services module is to extract those services to only the instrumentations that need them. So, one of the contenders for that is the visible service screen, that is the.
**Jason Plumb** 43:20 Right, okay, the one we talked about last time.
**Surbhi Agarwal** 43:22 We talked about last time.
**Jason Plumb** 43:24 Got it.
**Surbhi Agarwal** 43:24 moved to its own independent module. It would separate out the AndroidX navigation and fragment dependencies to it individually. And then there is the network module that uses the AndroidX codependency, the network monitor module. So, like, that can perhaps live there, right? That could be separated out, and then there is app lifecycle, which I think ties to everything, so probably that has a reason for it to be there in the services module itself.
**Jason Plumb** 43:54 Yeah.
**Surbhi Agarwal** 43:54 That brings in the AndroidX lifecycle dependency, but we can discover… we can… for all of these as well, in addition to separating them out into separate modules, we have to also figure out what minimum version we can keep them at.
And Cesar pointed out that there could be an inverse problem where newer versions are not backward compatible.
So we have to do some research there of where it makes sense to keep them at a lower version, which libraries we can trust to be backward compatible and which we can't, right?
**Jason Plumb** 44:24 Yeah, okay. Thank you for that recap. Yeah, I completely spaced out.
**Surbhi Agarwal** 44:30 There is also a few other things, like, there are these com. This is not priority, so it probably is okay if it doesn't go in 130 milestone, but it's doable right now. So, like, some dependencies I suggested could be compiled only, like those server, service provider API ones, SPI dependencies, the com. The find bug, and the auto service one, right? So they can be compiled only, they are only needed at the compile time.
So that is… that can be done. And there is… AndroidX Core right now is available in all the modules, but it is only used in network monitor module, is my understanding, so that needs to be tried out and removed from all the modules.
**Jason Plumb** 45:16 Where is this declared? Like, why is it in all modules?
**Surbhi Agarwal** 45:20 Yeah, so I'm not sure it… I don't think it is used. I think it can be removed from all the modules. It is, like, all, I'm not sure, most, I can say. Okay. Yeah.
**Jason Plumb** 45:31 Gross.
**Surbhi Agarwal** 45:33 Y'all.
These are some quick wins that can be achieved, perhaps.
**Jason Plumb** 45:39 Yeah.
**Surbhi Agarwal** 45:40 But I'm not sure if I'll get the bandwidth to do all of this.
**Jason Plumb** 45:44 Yeah, I get it.
**Surbhi Agarwal** 45:46 Yes, and yeah.
**Jason Plumb** 45:51 Okay.
What's in there? Quite a few.
**Jamie Lynch** 45:57 Is this a block perf, or… the next release.
**Jason Plumb** 46:02 I mean, that is a great question. So, we… we currently have this problem. I… I aggressively put it into 1.3, because I thought it was something we would want to have fixed for this release, because it's a… it's a pretty crappy problem to have.
But it's also crappy to not release, so… I am inclined to maybe remove it from 1.3.
**Hanson** 46:27 I'm curious what people think.
**Jason Plumb** 46:29 about this.
**Hanson** 46:29 the May release is just around the corner, right? So, I think if we can't get it done now, we should remove… like, this week, we should remove and release. And then, by the time we get that done, maybe it's… will be time for the next release already, so…
**Jason Plumb** 46:45 Okay, what do other folks think?
**Surbhi Agarwal** 46:47 Yeah, I agree, I'm not sure if this can be… like, there is enough time to get this through.
**Jason Plumb** 46:53 Okay.
So we're gonna err on the side of getting another release out, even if it doesn't quite address this one yet.
**Surbhi Agarwal** 46:59 Yeah.
**Jason Plumb** 47:00 Okay.
Alright, I think that's a… I think that's a completely reasonable approach.
I will make a note of it here.
Just so that we have some form of record of this. It's probably in the issue itself, yeah, okay.
**Surbhi Agarwal** 47:19 Right now, there is a solution, right? The apps can, like, pin the lower version, so we are not at all in a pickle in that sense.
**Jason Plumb** 47:35 Yep, okay.
So what's left, then, on the 1.3 milestone is just the instrumentation API, I wish there was a better way to get to the milestone, or I guess what I'm saying is, I don't know of a better way of getting to the milestone, but Right, so this one, which I'm inclined to say we go forward with, and then the work to stabilize session.
And this one, has there been… I don't… okay, this can happen after this meeting, but I think there has not been any additional commits to this? Oh, man.
Carnage.
I think there has not been any additional… work on this. And this exposes the session. That was the main… that was the main hang-up, right, is that… In order to do this, you have to stabilize the session.
Yes, okay.
Yep, I think we moved forward with that.
Cool, and I think, Jamie, you did some legwork on cleaning up some of the session stuff, so I think… That looked great to me, and I think we're in… Pretty good shape to do that, so… Awesome.
Alright, anything else from anyone?
**Hanson** 49:14 Well, Cesar finally updated and answered your question, for the, crash semantic convention. I've been off of that stuff for about a month, so, or three weeks, so, Yeah, FYI. Sorry, took so late. Oh, Cesar's gone, so never mind.
**Jason Plumb** 49:30 I mean, you're… I have a little to-do list over on my other monitor, and it's number 4 is review CrashSunConf PR for Hansen.
Bill at number 4!
**Hanson** 49:41 It's… yeah, I feel like it's perpetually number 4 or 5, which is why it never gets the attention it's due, so…
**Jason Plumb** 49:53 Yeah.
**Hanson** 49:55 I'm picking up my flight.
**Jason Plumb** 49:58 Okay, cool, and I believe this is not a… I believe this is not a client sign week. Alright, so I will be out starting Thursday, and out all next week, returning the… the 20th, or whatever. Let me look at a calendar.
**Hanson** 50:16 I'm back on 420, nice.
**Jason Plumb** 50:20 Not by design.
If that's true, I might be relying. Let's see.
Yeah, I will be back on the 20th. Okay, so I'll see you at the Kotlin SIG on the 20th.
Alright, thanks everyone!
**Surbhi Agarwal** 50:37 Thank you.
**DavidGrath** 50:53 No clever truck, are you there?
Fair enough.
