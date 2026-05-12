SIG: Entities SIG
Date: 2026-05-11
Duration: 66 minutes
============================================================

## Zoom Recording Transcript

Josh Suereth 00:04:44 Hey, everybody.
Martin Kuba 00:04:48 Hey, Josh.
I think it's just you and I.
Oh, Daniel 2.
Daniel Dyla (Dynatrace) 00:04:53 And a bunch of note-takers.
Josh Suereth 00:05:01 Does it make you feel popular that there's so many note-takers?
Daniel Dyla (Dynatrace) 00:05:07 One of them left with the leave command.
The other person… the other… there's two that are the same one, I assume this is the same person. Not a very common name spelling.
Josh Suereth 00:05:19 Yeah.
Daniel Dyla (Dynatrace) 00:05:21 I'm too lazy to log into the thing to get the keys to kick these note-takers.
Josh Suereth 00:05:30 Yeah, it's all good.
I mean, this whole thing is recorded, so just watch the recording, you know?
Anyway, you weren't here to… we were outnumbered by bots for a little bit.
Ted Young 00:05:44 Jesus. By the same bot, even.
Daniel Dyla (Dynatrace) 00:05:48 Yeah.
Josh Suereth 00:05:51 There were, there were more before.
Ted Young 00:05:56 Yeesh. Yeah.
I feel like maybe we need to update our policy on this, because I don't… I think…
Daniel Dyla (Dynatrace) 00:06:06 the only… way to stop it is to require logins for Zoom, which would be very impactful to a lot of real people.
Ted Young 00:06:16 Yeah.
Bienie…
Daniel Dyla (Dynatrace) 00:06:22 I wonder how many note-takers… Go to read the notes, and it's like, for the first 5 minutes of the meeting, they talked about how much they don't like you.
Josh Suereth 00:06:38 Come on.
Ted Young 00:06:45 Are you kicking them, or are we giving up on that?
Daniel Dyla (Dynatrace) 00:06:48 One of them left.
Josh Suereth 00:06:50 None of us care, but if you want to kick them, feel free, yeah.
Ted Young 00:06:54 I don't care.
Josh Suereth 00:06:57 This is recorded anyway, so it's just funny.
But I do hate the, user agreement that they send you in chat of, like, you agree to have me record you if you stay in the meeting? It's like, no.
Well, that's not how this works.
Ted Young 00:07:11 Yeah.
Daniel Dyla (Dynatrace) 00:07:11 Yeah. I think a couple of high-profile lawsuits will likely come down the road, but we'll have to see.
It won't be me.
Josh Suereth 00:07:26 Yeah.
Yeah, we have an issue where, Some of the documents that Tigrin wrote when he was at Splunk are now deleted.
Sorry.
Some of the documents Tibern wrote when Splunk still paint for Google Drive are now deleted, that they don't pay for Google Drive anymore.
Ted Young 00:07:56 Right.
We went through the same thing when LightStep blipped out of existence.
Josh Suereth 00:08:03 Yeah.
Alright, cool. I think… thank you for adding something, Martin. I actually want to, Maybe we'll jump into yours quicker.
Dimitri, you want to talk about… I put this at the top, the SDK spec?
4836, or did you want to talk about yours, which is 5067?
Dmitrii Anoshin 00:08:30 I'm good. We can talk about identity first.
We can start in the order that you put here, so we start with this SDK, I guess.
Josh Suereth 00:08:41 Yeah, so I didn't have a chance to read comments in, like, the past 2 weeks, apologies, it's been a bit busy.
Okay, so we have, let's see… Do comments show up, or they're all resolved?
This is the entity event specification, never mind, this is not the SDK one I was thinking of.
This one never got merged?
Okay, interesting.
I'm seeing that now, sorry.
I'll call out, this one needs some attention, then.
We should get at least one more approval so we can merge this. We have three.
Which one?
Daniel Dyla (Dynatrace) 00:09:30 4836.
Josh Suereth 00:09:31 4836, yeah, this is not the one I wanted to talk about, which is I want to talk about yours, Daniel.
Dmitrii Anoshin 00:09:37 We can only see your Google Doc if you share.
Josh Suereth 00:09:40 Oh.
Okay.
Hold on, let me click the share this tab instead, once I get the… this up. Okay, so this is the SDK specification one, which is actually 5057.
That's what I want to talk about, so let's reminder.
to view that. Okay.
So, in this one, can you see what I'm rendering now?
Daniel Dyla (Dynatrace) 00:10:10 Yeah.
Josh Suereth 00:10:12 Okay. We had a discussion about, like, entity detection, and specifically it was about, how you can't have identifying attributes discovered synchronously.
Unfortunately, I think that's how all the GCP resource detectors work, because you have to hit an HTTP server to get your identifying attributes from GCP. It's a, there's, like, this local metadata server that you hit with HTTP to get your data.
I think we even do that in JavaScript today.
So… like, I understand this concern.
I don't know what we do about that, though. Like, that basically means… We'd have to stop doing… Resource detection.
in JavaScript for TCP, and move it only into the collector.
Daniel Dyla (Dynatrace) 00:11:06 Yeah, which, that's a no-go.
I mean, it's not something that can't be overcome, it's just the whole pipeline becomes asynchronous, and then, like.
your spam processors and stuff are potentially useless, because certainly in the case of things like, Cloud Functions, or whatever the Lambda equivalent is called.
Like, you may only get run one time, so… The… if the resource isn't resolved when the span starts, the span processor is only looking at promises and doesn't see any actual resolved attributes.
And then… The spans end, and the… it's exported, and… The function shuts down.
And it's essentially impossible to write an on-start for that process.
a reliable one, because it's a race condition. Does the… Resource resolved before the span started.
Josh Suereth 00:12:09 Yeah, I mean… I understand. I… I think that we probably need a startup spec that allows us to do that before… In some… in some reasonable fashion, you know what I mean?
Daniel Dyla (Dynatrace) 00:12:26 I mean, this is what the JavaScript SDK does today. It just… some attributes, if they're asynchronous, you can't see them. Like, you just see it's a promise, it's not resolved yet. It's up to the export pipeline To wait on those before exporting data.
and if you have a spam processor that needs to read those data, like, those… Attributes.
You may not get them for the first… a couple of spans, and you just have to live with that. And we don't get complaints about it all that often.
But it has come up.
Josh Suereth 00:13:05 Yeah, you do get complaints about it. I'm just curious what those use cases are.
Daniel Dyla (Dynatrace) 00:13:11 It's usually people who want to write spam processors that… are either doing, like, some PII stripping or something, you know, some sort of, I want to process every attribute.
And the ones coming from the GCP names, the GCP servers.
Are, you know, usually not the type of thing that you would want stripped anyways.
But when somebody's making something that's like, I want to strip data from every single attribute, they get concerned when they can't read You know, some attributes or promises, they get confused.
Josh Suereth 00:13:50 Alright, this is gonna sound crazy, but… Maybe. I'm just ideating. So… I do feel like there should probably be a resource processor.
That lets you do… like, if you're talking about, like, stripping things, something that lets you see resource attributes, right?
like, does it make sense to put it in the span, or should the span just have, like, a link that says, I'm from this resource, and then when we go to grab that resource, there's a processor… when we go to create the resource and finish the async, there's a processor that can, like, look at it and do filtration and crap, like, in the SDK. Would that make more sense?
Daniel Dyla (Dynatrace) 00:14:34 I mean, that solves that use case for sure, yeah.
You would still have the case that you know.
Yeah.
Ted Young 00:14:48 How much is this JavaScript Specific, in the sense that in other languages, it's just… if you… Want to, like, do all of your you know, entity detection and resource resolution, and then just await that completing before continuing on, because it matters to you, right? My… you know, I'm… out of the loop with the latest JS, but I know, like, that's traditionally just harder to… it's just a bigger pain in the ass to do that in that language than in other languages.
Daniel Dyla (Dynatrace) 00:15:24 Yeah, I mean, it's essentially impossible in JavaScript. You can do that in other languages, But then you're, like, you're just making different trade-offs that aren't necessarily any better. Like, you're blocking the application response.
Ted Young 00:15:42 Right, but that's a, a choice you could make in other languages, I guess I'm saying this. You can say, like, we're going to await resource resolution up to a certain timeout.
And then you can choose to, like, bail because you don't want observability matters that much to you, or you can carry on without some of those resources resolving.
Josh Suereth 00:16:07 I actually think we don't even have a timeout in Java. I think it just waits.
Ted Young 00:16:11 Right. It's just there.
Josh Suereth 00:16:13 Right. But one of our… yeah, our early demo had it, yeah.
Ted Young 00:16:17 Yeah.
Right, that's what we tend to choose, I think, in most languages, right? Is that they… they… you know, they won't… you block startup until you've resolved these things.
And I think JavaScript might be the only SDK that does it the way you're currently describing.
Daniel Dyla (Dynatrace) 00:16:35 Yeah, I… well, I think the… the main sticking point is that… In the specification, both the start and end span processors specify this must be called synchronously with the application code. So, like, the… when the instrumentation calls, like, start span.
The span process, like, the whole pipeline is run synchronously all the way to the span processor.
So you can't do any sort of asynchronous awaiting in there at all, and be specification compliant.
Josh Suereth 00:17:09 If you're really dirty.
And it's probably too late for this in your API, but could you make it be an async await to get access to a meter, or a tracer, or a logger?
Daniel Dyla (Dynatrace) 00:17:22 I mean, maybe, but then you're just pushing the asynchronous work off onto the application.
Josh Suereth 00:17:28 Yeah, but it's specifically, we're pushing it to the application because that's your startup async.
So, if startup has an async thing in it in JavaScript, right, we would say, cool, starting an OTEL collector, or sorry, starting an OTel SDK is an async operation. So, we're gonna force you to make an await to get access to it.
Daniel Dyla (Dynatrace) 00:17:46 Yeah, we had a, like, an SDK… helper, I guess what you would call a distribution, something that set up tracing metrics and logs for you that handle all of this, and it did have an asynchronous start method.
And everybody complained.
It was the, like, our number one complaint for, like, 6 months, until we got rid of it.
Josh Suereth 00:18:08 Async is so… it bleeds. Well, I get, I get you, yeah.
Ted Young 00:18:12 Yeah, that's the thing, right? If people have synchronous startup, and you're like, aha, Yeah.
Daniel Dyla (Dynatrace) 00:18:18 Yeah, in order to use OpenTelemetry, you have to change your entire application to start up asynchronously.
I apologize.
Yeah.
It's a no-go for a lot of people.
Josh Suereth 00:18:32 Yeah.
Ted Young 00:18:36 But, but it…
Daniel Dyla (Dynatrace) 00:18:37 Most of the time, the actual outcome was not that they would await startup and be mad that they had to make their application startup async. It was that they wouldn't do that.
And they would miss a bunch of spans when the application started up. They would miss a bunch of telemetry, because it wasn't finished starting yet.
Josh Suereth 00:18:57 Because they didn't await for it. Gotcha.
Daniel Dyla (Dynatrace) 00:18:59 Yeah.
Because they, they viewed that as, like, a better trade-off.
then… making a, like, startup async. And the most… the issues that we actually got were primarily Lambda, and it, like, it would be, like, bug, no tracing in Lambda. That's what the issue would look like. And then when you started looking into it, it'd be like, oh, they didn't await the startup.
And the Lambda finished before the SDK even started.
Josh Suereth 00:19:31 Nice, okay.
Alright. I mean, we… Do you have the ability to wait, though, during export?
Daniel Dyla (Dynatrace) 00:19:44 Yeah, because the export is fundamentally asynchronous. It's like an HTTP call, right? Or a gRPC, or whatever it is.
once it's passed to the spam processor, I think we actually do the awaiting.
in the sp… we… the span processor on end, I think, is actually where we do the asynchronous resolving, if I remember correctly, because… It doesn't have to… Like, guarantee anything when… when the on-end callback returns.
there can still be work going on. That's totally fine. It just has to be called synchronously with the application code.
Josh Suereth 00:20:33 What are the things we're sending into span processor? We have on start, onEnd, shutdown, and forced flush, but on start is the one I'm most worried about. We actually send the full span, right?
Daniel Dyla (Dynatrace) 00:20:44 Yeah. It's… We also have on starting, which is read-write, and then on end, it's read-only.
Josh Suereth 00:20:53 Well, unstarting isn't in the spec, I don't think.
Daniel Dyla (Dynatrace) 00:20:57 Oh, I thought it did. I guess it never got there.
Josh Suereth 00:21:00 No.
But I was just trying to see, like.
Does the spec require res… because we might have some shenanigans where we could, We could give you a lot of freedom with your spin.
spec for what you can do on these processors for resource, if it's not fully specified, right? Because then you have freedom to change your implementation in ways that will make this not be so janky for users.
Daniel Dyla (Dynatrace) 00:21:35 And that's more or less what we did, we just… some attributes, when you go to look at their values, instead of being a string, it's a promise.
In your spam processor.
Josh Suereth 00:21:45 Yeah.
Andy.
Daniel Dyla (Dynatrace) 00:21:47 You can await those, but you can't modify that span in the on start, because… You can't do any… you have to do all your work synchronously.
Josh Suereth 00:21:57 Yeah, I don't think we actually have a method to get the resource off of a spin that's live.
Because I don't remember seeing that in any other implementation.
Daniel Dyla (Dynatrace) 00:22:08 It's definitely… I mean, you can read the resource attributes In the span processor, for sure. At least in JavaScript.
Ted Young 00:22:18 Great.
But it… again, in other, implementations, because they have a… they're blocking startup. I think in almost all of our implementations, we block startup.
Until resources are resolved.
It's… I think, prob… JS is probably the only place where Where this is a little confusing.
Daniel Dyla (Dynatrace) 00:22:43 Might be the only place where that's impossible to do.
Ted Young 00:22:46 Yeah.
Josh Suereth 00:22:48 Yeah, well, the thing I'm thinking about is, A function receiving this argument must be able to access instrumentation scope and resource information. Yeah, okay, so here's where it is. So readable span, we do require as of 1.10. Okay, it was added.
Yeah. Somewhat later.
For practice currently must be able to access interpretation library, but that's deprecated.
Having the same name first matters, interpretation scope, right, okay.
So yeah, you're right, we do require that you have resource information.
I was gonna say, like, if it's not fully specified, it gives us some design options, because it's in the SDK.
But not many design options. Like, I'd love if maybe we had… your access to resource information is in an await block or something. Like, maybe you could get away with that, I don't know.
But if.
Daniel Dyla (Dynatrace) 00:23:38 Well, then you would not be able to… You wouldn't be able to modify it if it was asynchronous, because… If you're… if you want to do something when the span starts.
And the span ends in a synchronous loop, it will end before your async code is ever even called.
Josh Suereth 00:23:57 I don't think you have ride access to it here, though.
Daniel Dyla (Dynatrace) 00:24:01 You do… and OnStar is a re…
Josh Suereth 00:24:03 This is a readable span, which is readable, but read-write, it doesn't guarantee you have right access to resource.
Again, that's why I'm surprised, like, when I was thinking about this from, like, a Rust or a Java or a Go perspective, like, I don't think you get right access to resource in span processor.
Ted Young 00:24:25 Oh, there's no writing to resources at all, because they're immutable.
Josh Suereth 00:24:28 That's… that's true.
Daniel Dyla (Dynatrace) 00:24:30 That's true.
Josh Suereth 00:24:35 Yeah.
Daniel Dyla (Dynatrace) 00:24:35 I can see what the GIS maintainers would think about making… resource not accessible.
From there.
Josh Suereth 00:24:45 Well, no, I think you want an accessible… what I'm kind of curious about… like, I'm just trying to understand the design space, like, we're in a hard spot, and I don't want to screw over the JS implementation to say, hey.
you have to support async any possible place and resource, because we have some resource detectors which are async, right? So, you know, really.
The reality is some resource detection requires async loadouts.
we need a way to support that without killing the whole API and ecosystem.
So what are the real requirements here? Like, what do we really have to provide and support? But the notion that you would scrub resource attributes in a span processor, you can't do that in other languages.
Ted Young 00:25:32 I'm a little confused, what are we trying to change here?
Oh, this…
Josh Suereth 00:25:36 This is the SDK startup spec. So, Daniel wrote a startup spec that basically adds a new requirement that, identifying attributes have to be looked up synchronously. And I don't think we can add that as a requirement.
Daniel Dyla (Dynatrace) 00:25:52 It's because it's required for, like, the merge algorithms and stuff. So you could make it… you could do it asynchronously.
Ted Young 00:25:59 Well.
Daniel Dyla (Dynatrace) 00:26:00 But everything… the whole pipeline would be asynchronous all the way down to… you know, wherever you do the awaiting, which right now in JS is in the on-end spam processor. So… your first handful of spans that start might not be able to see those attributes, but if you're not supposed to be able to see them anyway, then maybe that's not a problem.
Ted Young 00:26:26 Yeah, if we're writing, you know, a startup spec, I think it should reflect you know, how the SDKs currently work. And it's also, I think, fine to carve out an exception for JavaScript, would be kind of my… like, everywhere else, we… right from the get-go, we said, resource detection is synchronous. Like, you have to resolve all of your resource stuff.
Before booting the SDK. And with entities, now, okay, maybe a resource could potentially change, but… That… would just mean, like, you're getting a different pointer back when you're asking for things, so rather than handing the pointer around, you know, you're handing a getter that will get you the latest pointer.
And so maybe there's… there's an opportunity for there to be, like, a mis… slight mismatch there, but we're saying, like.
That's probably not a big deal.
for… for most SDKs.
Josh Suereth 00:27:28 Yeah, honestly, yeah, the language here, the entity detector must detect synchronously. For most other SDKs, we just make that HTTP lookup synchronous. We're fine, yeah.
Dmitrii Anoshin 00:27:39 What do we currently do? Do we emit spans with… without, like, stable resources? So, let's say first spend currently emitted with no resources, or less resource attribute than the other ones going forward?
Ted Young 00:27:55 He's jaw.
Daniel Dyla (Dynatrace) 00:27:55 JavaScript?
Dmitrii Anoshin 00:27:56 Yeah.
Daniel Dyla (Dynatrace) 00:27:58 It awaits all of the attributes on… The first export.
Dmitrii Anoshin 00:28:05 Okay, so how is that different if we are… if we are, like, queuing them on the export?
Why can't we queue… Until we have identified attributes.
Daniel Dyla (Dynatrace) 00:28:18 We can, it just complicates the implementation. Like I said, it was… it's something that we can do, it just makes it more complicated, and you can't access the resolved values until that's completed. So you won't be able to… Read any of these attributes until the first export.
Dmitrii Anoshin 00:28:37 Yeah, I think.
Josh Suereth 00:28:38 It also means spend processor is problematic, right? SPAN processor is not asynchronous, and you might not have access to the attributes in the span processor, which we just saw, by specification, you're supposed to.
Dmitrii Anoshin 00:28:51 But we can… we can queue somewhere closer today.
Emitter, before the processor, is that an option?
Daniel Dyla (Dynatrace) 00:29:00 No, because the spec says specifically that it must be called synchronously with the application code. I don't remember the exact wording, but, like, when the user calls span start, it has to go all the way to the spam processor synchronously, and when they call span end, that has to go all the way to the spam processor synchronously.
Ted Young 00:29:21 And again, like.
Josh Suereth 00:29:23 The spend processor is actually how the tracer's implemented. So if you needed to replace the SDK, you can do it just by replacing the spend processor, and the whole SDK behavior is almost complete, like, the important bits of the behavior, the performance of it, swap out, right?
Ted Young 00:29:36 Great.
And this is a place where, again, like, JavaScript could maybe go its own way. The reason why that stuff is called out as being synchronous is you need those spam processors to be running on the same thread as, you know, the application code in order for them to grab the right context and all of that stuff.
Josh Suereth 00:29:56 Yep.
Ted Young 00:29:57 But I could see, again, like, JavaScript being its own unique… You know, runtime.
with regard to how asynchronous code works, if life is better, like, if you can still get the correct context and run that stuff asynchronously, and that just makes everyone happier.
You know, if you wanted to redo it that way, I wouldn't be opposed.
Josh Suereth 00:30:23 What… yeah, I think… I think it's time to call a resolution to this, because we spent, like, 30 minutes on that discussion. It's a good discussion. I think we have a bunch of design decisions. There is a piece of me that would like to make the spec a little looser to be exactly what we need.
You know, so the spend pro… like, instead of saying it has to be synchronous, saying you have to have access to local context so you can implement the processor correctly, but we actually don't care if it's synchronous, as long as you have context.
Anyway, that's… yeah.
Dmitrii Anoshin 00:30:53 That's exactly what I want to suggest, just to avoid going into the implementation details with the requirements. Because for the collector, I'm not sure if it's written somewhere in the spec, but… or not yet, but the thing is, is that we allow, let's say, invalid entities being propagated within the collector, but Like, it's important that what goes outside goes over the wire, that part's supposed to be Supposed to have all of the proper entities, and, like.
And properly formatted and have unique identities.
Because… we have these companies, right? We have resource detection processor, and we have some receivers, and it's possible that receivers don't emit proper entities, don't emit fully, like, identifying resources. It can be only identified within the collective instance somehow, but resource detection processor adds additional information.
And when it goes out of the collector, it should have… it should be compliant with the specification, so maybe something like that can be… utilized in this SDK as well.
Josh Suereth 00:32:17 Just… yeah, yeah, I, I… that… Dimitri, just to call that out specifically, like, because the SDK has so many extension points, we have less flexibility than you do in the collector.
I think, because you're putting more controls around the bounds. But I do think we could call that out. I don't know… we don't have a collector spec, but if we did, I would put that in the collector specification of, like, the bounds have to be… Accurate. For… to put a cap on this discussion, though.
Just to put out some of the, I think, the most important things that we called out here. Almost all SDKs are gonna have synchronous startups. So, like, the spec as it is for almost every SDK is totally fine. It's JS that we might need to carve out for.
And Daniel, do you have enough information that you can provide that callout for JS as needed?
Daniel Dyla (Dynatrace) 00:33:09 Yeah, I can. I was just… I was trying to think really quickly while you were… you mentioned the context issue, and, like, that's why it had to be on the same thread, and that's definitely true, but I think there's other… There are potentially other reasons to have it synchronous.
But… I don't… yeah, I can't think.
Josh Suereth 00:33:32 There are many reasons to have it synchronous, like, in an abstract sense, but, like, hard requirements we'd have to think through, yeah.
Like, I don't really want to make it be asynchronous, because I think that's a huge break and change for you as well, but it's, It's what it is. Because asynchronous is viral, right? Like, if we made it asynchronous, you have to have an await everywhere.
Daniel Dyla (Dynatrace) 00:33:57 Yeah, it absolutely is, unless you didn't make it awaitable, like… You could, in the span, end, call, the span processor asynchronously, but… not… Like, tell your caller that you're doing that, but then you're leaving… you essentially have a hanging promise, which is its own problem.
Yeah. And then I think you're inviting things like race conditions.
Josh Suereth 00:34:28 And, and timing issues, yeah.
Daniel Dyla (Dynatrace) 00:34:31 Yeah.
Josh Suereth 00:34:31 Okay.
We have… we have 30 minutes left, we have, like, 3 things. Let's… Let's look… if you're okay following up on that, Daniel, I'm gonna…
Daniel Dyla (Dynatrace) 00:34:40 Yeah, I can. I can do two things. I can try to relax the wording and make the entity's version of what the JavaScript resource SDK already does, which is, like, on the first export, these might be asynchronous, too bad. Like, you might be able… you might not be able to read them.
Which, especially if there's a resource processor, that helps.
And I can look through the wording to see, like, what are the actual requirements, because it just says resource information. Technically, we could just say, yes, there is a resource, that is information.
Heh.
Josh Suereth 00:35:19 Yeah, yeah.
Daniel Dyla (Dynatrace) 00:35:20 And I will also try to make a version that… a version of the spec that relaxes the wording.
That allows, you know, potentially… To see what an asynchronous export pipeline would look like.
and maybe prototype that in JS and see if it's totally broken or not.
I think you will run into orchestration challenges, though, so I… yeah, I'm not entirely sure that that's a reasonable But we could try.
Josh Suereth 00:35:51 Yeah, I think it's probably worth trying. I mean, that was what our early prototypes really ran into. Okay, let's jump into identity a little bit. What I wanted to do, like, Dimitri, I don't know if you wanted to drive this discussion quick. Let's limit it to about 10 minutes.
Yeah, I had two big questions. I don't know if they were addressed yet or not, or if you want to talk through stuff.
Dmitrii Anoshin 00:36:13 Yeah, I replied to them.
So… So, the idea is that, yes, it is a relationship, but it's… I think it's… the most… like, the important and the only required relationship to specify the global identity and help with the identifying of the… of the entity on the resource. And, if we have that relationship first.
this is the only one needed to be passed on the resource with the outside channel. I don't think there is another use case when we need that. And second.
It doesn't conflict with the other relationships, because the other relationships has… we can call it, like, solving completely separate problems.
The… Scope-defining relationship is important and needed to define the identity of an entity.
And other relationships, they are… Just needed to… build the topology graph, pretty much. And I don't think they should conflict. You can have Context entity being the parent.
being the same as the parent, but it might be not the case, it might be something else. I don't know, Ranzone, for example, or… Like, contains, or part of, or something like that.
Josh Suereth 00:37:38 So for context for, like, I'm gonna put this in browser language for Martin and Ted, right? If you have a notion of an application.
That has an ID, which in OpenTelemetry, let's call it Service instance ID, right? So you'd have a service instance ID, which is unique, and you know that that's part of a service that has a name, that that's part of a namespace, right? So there's a chain there. But you would also have, like, this is the browser ID.
as an entity, and that might be a unique identity as well. And so, you'd actually have two unique identities, one for the browser, or even the page on the browser, if you're… or session on the browser, right? So you'd have a session as part of a browser.
those two make an ID, and then the service things would make an ID, and those would be unique IDs, and there's a relationship between them where you know that this session is part of this application, in some fashion.
But we're not explicitly putting that in the relationship. What Dimitri proposed here was, like, when you make session, you would say, by the way, session needs a browser to know its full identity.
So I'm gonna have a session ID, but I need to know what browser I'm a part of. Maybe that doesn't work, because maybe you don't model it that way. The better one is when we talk about, I think, containers and processes. So, like, a process is part of a host, right? Or a process is part of a container, or a container is part of a host.
And so, if you identify a container by just a pure name, you could have host be, like, the rest of its identity. For process, PID is not unique enough, right? PIDs are reused all over the place, they're very short digits, but if you have the host ID and the PID, that's more unique. That makes a… that makes a better name.
Ted Young 00:39:25 I mean, we also do, like, compound… IDs, right? Like, for a service, right, you have, like.
you have, like, your service ID, right? Your service instance ID, you also have, like, service name and, you know, maybe service namespace, right? And name and namespace are definitely not unique, but we're saying the compound is unique. So is that what we're saying here? Service name is local?
Versus…
Josh Suereth 00:39:53 Yeah, so service name is a local ID in the context of the namespace.
And so, service name, when you report it, you say, my context is the namespace.
And so that you can build the bridge independently, and there might be more than one in a resource.
Right? Because, like, service is, like, the logical grouping, whereas, like, process is more of a physical grouping, right?
So, so the, the, we had a few open questions. I think the, the one… The one was that, I still have some concerns, Dimitri, with, like.
you… I think you called us out somewhere, I was looking for it, where… process ID, right? A process ID… The outer wrapper might be a container or a host.
But we don't know which.
Yeah. So do I say both? Do I… how do I know which one to put? That's… like, if we've solved that, I think this is beautiful, the design.
Dmitrii Anoshin 00:40:54 So, the thing is, specification doesn't tell you what is your, context.
context entity type. It can be only… only emitter can tell. So if you run, let's say, like, a collector, receiver, or SDK in the… in the process, and you have a detector for the container.
In that case, that combination will tell you that this process is part of the container, or this process is part of the host.
But in semantic conventions, we can only… This… describe, let's say, possible?
context types for particular rankings? Yeah.
Josh Suereth 00:41:39 So that's not my… my question is actually on the detection, right? So, think of it this way. I write a resource detector that detects process ID.
Dmitrii Anoshin 00:41:48 Yep.
Josh Suereth 00:41:49 And all it knows how to do is, like, run the TS command, or whatever the equivalent syscall is to get process ID of myself, or look at my, you know, runtime variables to find my process ID.
That's all it does. Then I write another detector that detects my container ID, and that's where it does whatever calls it needs to do to get to container ID. I write another one to do host ID, which will look at the Etsy hostname, right, or the Windows equipment.
Dmitrii Anoshin 00:42:12 Yeah. So we… yeah, I guess we…
Josh Suereth 00:42:15 How do I know… Yeah.
How do I write that code?
Dmitrii Anoshin 00:42:19 Yeah, we're missing the glue between the detectors, essentially, that would put that relationship in place.
Josh Suereth 00:42:25 Yep.
Dmitrii Anoshin 00:42:26 This is something that…
Josh Suereth 00:42:28 I'm fine if you want to put this as a config thing, like, maybe… maybe we… the way we define NC detected and config things, it's like…
Dmitrii Anoshin 00:42:36 Yeah.
Josh Suereth 00:42:36 you list the hierarchy in order, you know? Maybe we do it that way.
Dmitrii Anoshin 00:42:40 That makes sense, I guess, yeah.
Or… Or it can be implicitly… implicitly… detected by the configuration, by the set of the detectors that the user configures, and some kind of… some sort of, like, implicit SDK implementation. What's the… I don't know how is it implemented in SDK, but detectors are applied by something, by some other piece of logic, right? And that piece of logic potentially can just ingest into detector. Let's say it'll ingest into the process detector an information that, hey, you are running as part of this container. So here, this container is gonna be your identity type.
like, at the startup, essentially. When it reads the configuration, it sees that there are several detectors, and it, like, injects that information to the detector, to the child detector, in that case. Does that make sense?
Josh Suereth 00:43:42 Sure.
Yeah.
Yeah.
Should that be done?
Dmitrii Anoshin 00:43:48 In words?
Josh Suereth 00:43:50 Well, I… I think so, but I… like, two things to think about. So, so, like, let's flesh out that idea, but two things to think about there. Like, one is make sure that we can write the code in the SDK and the collector, and then two would be, how does it interact with the environment variable?
Dmitrii Anoshin 00:44:09 it doesn't matter whether it's environmental variable or configuration. At the end of the day, you will get some, like, internal representation of the configuration supplied to the SDK, right? And it doesn't matter whether it's… no?
Josh Suereth 00:44:24 The environment variable will have to have the scope defined on it, right?
In some fashion.
Remember, if I'm using the environment variable, here's one of the ideas behind the environment variable. I want Kubernetes to have a clear way that it just dumps an environment variable that gives you your identity.
I want GCP to have a way where I give you an environment variable and you get your identity. And you don't have to make that HTTP call, right? So in JS, it's just an environment variable lookup. That's the idea behind that, is I can propagate my identity to you.
Dmitrii Anoshin 00:44:55 Yeah, okay, I think, like, the grammar for putting hotel entities into environmental variables needs to be updated, and that probably… that grammar will take precedence over everything else, but if it's not supplied, if those entities are not defined, and we have Just plain detectors configured somewhere else.
We still need to figure that out, and I guess that logic can be…
Josh Suereth 00:45:22 The plane detectors are where I think you should write up the config idea and see what that looks like.
Okay. Yeah.
Dmitrii Anoshin 00:45:27 I got it.
Yeah.
Josh Suereth 00:45:29 I remember that… you're dealing with the configuration specification that already exists, too. Like, one of my hopes was configuration already has this notion of resource detectors, and I… and it's specified loosely enough that we can just update them to support entities.
Dmitrii Anoshin 00:45:45 Yeah. Actually, I was thinking about putting this as a follow-up, and specifically updating the grammar as a follow-up, because I haven't seen any blockers or anything that would change this proposal, but if we want to support, like, backward If you provide… you want to provide backward compatibility and support existing configuration interfaces that don't have entities.
In that case, yeah, I need to think more and provide some, like, some kind of guidance. But is that the goal? By the way, I… I, I… do we want to emit entities?
For existing detectors with existing configuration interface without, like, talking about entities at all.
That's actually… I wasn't even sure about that.
Josh Suereth 00:46:39 So, the way that the configuration thing works right now.
is… it's literally just, like, a named list, it's not… it's not real configuration. So the way you define your resource detectors is… is there are, like, 4 reserved strings of, like, hosts, process.
I forget what the other ones are, but you, like, you specify those string names. So all I want is those string names to be legit, and the config to be legit, that's all. And yeah, I'd like to do that, because again, like, think about the friction and adoption of entities. If we require people to change their config, to change everything, it's gonna be really hard to get entities out the door.
high friction-wise.
Dmitrii Anoshin 00:47:21 So…
Josh Suereth 00:47:22 Yeah, I… I think maybe we've had enough, like, we're at our time box, and I think you have enough information to kind of think through it. I like the ideas you have, like, if you can write it up so we can see it all written down, that'd be ideal.
Dmitrii Anoshin 00:47:37 Yeah, so just to confirm the requirement and expectations from the SDK configuration, when you specify the list of those detectors, we want to emit entities out of the box, with specified list of detectors.
Josh Suereth 00:47:50 Ideally, yeah.
Dmitrii Anoshin 00:47:51 Okay, because I don't think that's even… that's even mentioned somewhere else. And in that case, yeah, I'll… I'll keep that in mind and update the proposal. Thank you.
Josh Suereth 00:48:03 Jeez, yeah.
Okay, cool. Martin?
Sorry, you have 15 minutes.
Martin Kuba 00:48:12 Okay, yeah. Yeah, I just wanted to, just a quick, quick update and, get your, input on a few things we've been working on in browser. I'm gonna share my screen, hold on.
Josh Suereth 00:48:27 Yeah, go for it.
Martin Kuba 00:48:37 Okay, so I, I have created, actually, two discussion topics in the browser repo. One is to, specifically about handling these entities, like, that, that change.
state during the lifetime of the SDK.
Accessions, and we also think page views, or documents, browser documents would be a candidate also.
And… There's a separate discussion that I created for just, like, to discuss whether we want to support the metrics SDK in the browser, in browser.
I… originally, we were going in the direction that no.
But with the idea that we would just, generate metrics in the backend.
Which I think is still… Probably the right thing to do, like, in, probably covers, like, 90% of the use case… use cases. But surprisingly, like, we're getting some… some pushback on this, like, some people, like, in the client SIG, client instrumentation sick, like, even from mobile folks, are now rethinking this, and, like, they would like to support Metrix SDK, so we still need to, like, you know, figure out how to move forward.
Here, but, So anyway, that's why I have these two discussion topics, and I kind of separated them, because they… they, I think, I don't… they are… Big enough on their own.
On this one, on the handling mutable entities.
I would appreciate… I actually posted this link in the Slack channel, I would appreciate if… you have… you have a chance to look it over and… and just see if I captured, the… the problem correctly. In… from what I can tell, it's not really an issue for logs and traces, like we've discussed it in the past, and I actually have a prototype for logs that I have updated. It's essentially the same as what I shared, I think, you know, a while ago, about a month ago, but to support multiple entities.
It's, it's this link, and just a quick, quick reminder that, you know, we have… We have… the issue that we have in browser, in the client… client SDKs, is that, when the entity changes, like a session.
It needs to apply to all instrumentations, or all the things that are emitting, telemetry, not just, like, that one place. So, like, the four entity.
method that was just added to the spec recently. Like, that doesn't really solve the whole problem for browser.
So, this… this prototype is… is… is, like, basically like the… the only thing that I can think of how to… how to make this work in browser, which is essentially having, this… this… For the sake of… the prototype, I just used the logger provider, so there would be a provider that's, that's aware of entities.
And it has… Essentially what it, what it does, it has a setEntity method.
So it's, it's got, like, a, you know, collection of entities that it's, that it's aware of, and every time you set an entity, it rebuilds, rebuilds, like, a delegate provider in the background.
that that provider… Is, you know, is created using, like, the merge.
Entities into resource, algorithm that you have defined.
And then, all consumers of this, like, instrumentations.
They're getting… When they talk to this entity over provider, they… they get back a proxy logger, and that proxy logger essentially is just delegates loggers to the, to the current provider that was created.
And… Yeah, I mean, we can still use, like, to actually create the delegate provider, we can use the for entity.
Implementation, but I guess, like, the main thing that I wanted to point out is that, it needs to, like, when… When an entity changes, like, it needs to, you know, update For all… all… all consumers, or all of all users of the logger provider, or all instrumentations that actually already have Loggers, you know.
Logger… logger instances.
So… I guess… here… I think this should work, but I wonder, like, if this is something that we can just go ahead and implement in the browser SDK, or if you think that there's something here that would require us to make, like, a proposal to the spec.
Yeah, this is, like, what I'm looking for your guidance on.
Josh Suereth 00:54:00 Yeah, the mutable entity proposals we had looked at this, and where we got blocked is basically metrics.
Martin Kuba 00:54:07 metrics, yeah.
Josh Suereth 00:54:07 Yeah, so if you're like, hey, we want to do this and we don't care about metrics, I have no problem personally.
And I would, you know, be willing to advocate for that, but if it was, like.
If you were gonna say, oh, and we're also gonna support metrics, the spec gets really awkward.
So I think, like, if we talk about this strategically, there's, like, two ways to think about this going forward. One is, We can have a bunch of call-outs for… what I would call, kind of, edge compute, like browsers, phone, that sort of thing. Stuff way the heck at the edge, like Internet of Things even, of, here's what the SDK and API should look like for that.
And that SDK would be slightly different than a server SDK, which would allow more of this mutatable stuff.
And maybe not support metrics the way it does today.
that's the way I would like to go, because honestly, if you do metrics, I would give you a whole new metric spec, right? I would make sure that when you go to report your span batch.
at some safe time, that you're able to collect metrics at that interval, and that you're not locked to any of the crazy-ass stuff we have to do for our current metrics SDK, that you can actually do this kind of efficiently for your use case. And I would give you a new SDK spec. I mean, we might be able to keep OTLP, Right? We could probably optimize the crap out of it, but we can… like, let's stick with that for now.
We might be able to keep the API, But I would give you a new SDK spec that gives you all the things you need, because I don't think what we have today works well for you. So, so part one would be we start having this carve-out for, like, browsers, phones, that sort of thing, for SDK behavior, for you to have this work.
Right?
Option number two is, you can try to make a blended SDK spec that does all things.
And I… that's what we went down before, and, like, I… my brain started to get muddled with, like, what the metrics SDK would look like that supports both servers and you. So, like, in my opinion, we should divide the problem. That's why I think option one's better, and I think that should be your path forward here. Go ahead, Dimitri.
Dmitrii Anoshin 00:56:27 Yeah, I think I… you covered that some way, but my proposal was, can we maybe introduce, within this new entity, like, additional block, can we introduce some information that would say which attributes can actually mutate, because having descriptive attribute doesn't mean it's always mutable. Typically, most of the descriptive attributes based on examples I have in my head, they don't mutate over the… over the lifespan of the entity.
But if we can have an option to specify that particular attribute is mutable, actually, and make metrics backends or, like, just metric specifications to say that those that are marked as mutable should not be part of metric identity.
No, they are.
Josh Suereth 00:57:21 They have to be part of metric identity. Like, like, these… first of all, these are identified attributes, they are mutating, and they're part of the identity. And that's, like, that's a key to this use case.
Dmitrii Anoshin 00:57:33 We're talking about mutable identifiable attribute.
Josh Suereth 00:57:37 These are mutable identifi… yeah, the identity actually is changing.
for the lifetime of the SDK. Not only that, like, we don't have good spatial aggregation in the collector yet, but you can imagine if you were to actually collect these high cardinality things and create, like, a Prometheus metric, you'd actually want to aggregate away some of these entities, possibly.
Dmitrii Anoshin 00:57:59 Yeah.
Josh Suereth 00:58:00 to make, like, different types of metrics. Yeah. But yeah, this is identifying. Like, that's the thing we all have to understand, yeah.
Dmitrii Anoshin 00:58:07 And that should be allowed for any metrics, for any entities. If you, like, decide to drop that entity and do special aggregation, you just drop all of the attributes for that entity, and you get new MTS, and I guess that we should allow that in the collector.
Josh Suereth 00:58:28 Go ahead, Ted, sorry I jumped in front of her.
Ted Young 00:58:30 No, no, no. Yeah, I just wanted to… it's like, separating the problems. We have, like, how do we deal with entities, immutable entities, in tracing and logs?
And it turns out that's just a simpler problem than how we would deal with it in metrics, whether it's in the browser, the collector, anywhere else.
And so I think the feedback Martin's looking for here is, like, based on how we think we should implement entities for tracing and logs, does this look like a reasonable implementation?
There's a separate problem of, like, how would we deal with entities for metrics anywhere? And then, beyond that, just for clients, they probably need a different metrics SDK Period from what we do in the collector, or on the server, or anywhere else. So I just wanted to clarify, it's like 3… 3 things.
And we're avoiding the two hard things, for this case. We're not worrying about, like, how do we deal with entities in metrics, and we're also not worrying about, like, what kind of metrics SDK would a client need, because that's probably way different than what anyone else would want.
Josh Suereth 00:59:44 Yeah, yeah, and for context, the prototype we did before, what you're doing for logs and traces, we can do in an SDK much easier, but it's the same gist of, like, whenever you create a span, right, you create the span, and then we late-bind the resource.
So, like, we will… we'll go look up the current set of resource entities when we report the span. That worked really well in our prototypes, that worked for logs, that looked for… that worked for spans.
And sorry, we can… we can early bind, not late bind, but you get what I'm saying. Like, when we go make a spend, we just look up what the current one is. That works great.
You don't have to go through all the pedantics here if we can get the SDK to be that, but I don't know if you're gonna be able to change the SDK spec.
without dealing with metrics, and so that's why I'm suggesting, let's just make a carve-out for you, of, we want… we want an SDK that lets us do this with logs and traces.
And we don't care about metrics for now, so, like, let's just, you know.
call this a different SDK if we have to to get it through the spec, because I think you're gonna end up with better code. But what you're doing is exactly what all our prototypes were. So it's in line with what I'd expect, yeah.
Ted Young 01:00:58 But I also think, like, in terms of, you know, when we had different, OTEPs, it just turned out it's, like, how you implement this in tracing and logs is just different than what you do in your metrics SDK.
Josh Suereth 01:01:11 Absolutely.
Ted Young 01:01:11 I'm not sure that we need a spec carve-out for what Martin's doing here.
Right? Like, because we're saying we're just sticking to tracing and logs, and it's not really… other than, like, JavaScript has, like, await issues that are different than other languages, like, I don't think we're…
Josh Suereth 01:01:29 Well, yeah, I guess, do you want the SDK to do this for you? I guess is the question. Because if you don't want the… like, all your code was about managing the SDK itself, versus getting done what you want to get done.
where we could make the SDK do the work for you. That's… so if you want the second, then we would make an SDK spec change, right?
Ted Young 01:01:51 I lost you there.
Martin Kuba 01:01:54 Yeah, I mean, we're… we're essentially… we're working on our own browser SDK at the moment. So, like, we were kind of envisioning, like, all this, like.
All this, like, configuration, like, using this specific implementation of the logger provider would just happen behind the scenes for the user.
Josh Suereth 01:02:12 Yeah, yeah, that's… I guess that's my point. Okay.
like, do you want a specification of the SDK?
That matches the API you want to give people, right?
For this, and then the SDK would actually support it natively for you.
Or are you okay continuing to… like, if you want to wrap things, what you… what you had looks exactly like what I expect, and I think works well for logs and traces.
But I would… like, if you're trying to get to the point where the SDK gives this to you out of the box, I was exploring paths for how that could happen. Yeah.
And that's where I think there would be some kind of spec work, and that's where I don't want you to run into the blocker of dealing with metrics immediately.
But I still think we could say, hey, a browser-specific SDK just makes sense.
Right? And we could carve out an SDK that's like, here's how we deal with logs and traces.
here's the specification for it, here's how you mutate entities and resource in that spec for that SDK. We can ignore metrics for now and come back to it later, right? I think that that might be really powerful.
Ted Young 01:03:17 The reality is we're gonna need to probably just go our own way in the browser in general, for the SDK. For example, like, one thing, all of the SDKs presume context. They're all very focused on context, and we literally don't have that in the browser.
in a performant manner, right? Like, that will eventually get into… JavaScript in the browser in some form one year, but today you have to use zones or some… some, you know, userland implementation, and that's, like, so inefficient that… that on so many levels, like, it doesn't work in the browser. So… And at the same time, the stuff we're looking at in the browser is not, like, like, tracing and spans are just really not that important, right? Like, it just, like… so, like, I think the whole browser implementation is just gonna end up being its own weird thing that's even weird compared to the other clients, just because that's… That's how fucked up the environment is.
Josh Suereth 01:04:31 Yeah, like, again, I want you to be able to be productive here and not get wrapped up into our current specification and stuff, because I think we should anticipate a lot of changes there, yeah.
Ted Young 01:04:42 Okay, so we're just gonna go our own way, and we're gonna try to, as best we can, you know, be like, by the time you hit OTLP, coming out of a collector.
It looks normal.
But… Yeah.
Yeah. Until then, it might be something weird and browser-specific, just to deal with the fact that browser.js is missing fundamental pieces that we have everywhere else, like…
Josh Suereth 01:05:12 Yep.
Ted Young 01:05:13 some place to put the context, for example. We just don't have that.
Daniel Dyla (Dynatrace) 01:05:18 And reliable clocks.
Ted Young 01:05:20 clocks, yeah, just all the things.
Josh Suereth 01:05:23 It's a clock. That's crazy talk.
Why do you measure stuff? Anyway, yeah, yeah, I gotcha. I see this as layers, by the way, like, as long as your OTLP is solid, it's open telemetry, right? And then… the SDK is just a layer on top of that, so we can figure that out later. We can have… I'm fine with multiple specifications, personally, for SDKs. That makes sense for different contexts. Like, I don't… I think maybe we need to pull that trigger sooner rather than later. So… cool.
Alright.
Martin Kuba 01:05:51 Could I… could I ask you, just really quick, could I ask you to look at this… look at this write-up, when you have a moment, and just, like, see, like, if I'm… if I'm just, like, completely off on something, because I… I… I feel like I… I was trying to understand, like, where the issues lie.
So this is, like, that's the… that's the section, like, under metrics. And then I was… as I was thinking about approaches for… for, you know, solving that for metrics, you know, I… I could think of, like, these options, but, you know, I think what you're proposing is, like, another one.
But if you have a moment and take a look at this, and maybe even, like, comment and reply to me in Slack, that would be great.
Josh Suereth 01:06:32 Yeah, yeah, I can do that.
Martin Kuba 01:06:34 Cool. Thank you.
Josh Suereth 01:06:35 All right, thanks.
