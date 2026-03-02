SIG: Python SIG
Date: 2025-08-14
Duration: 52 minutes
============================================================

## Zoom Recording Transcript

**Riccardo Magliocchetti** 05:00 Hello, everyone.
**tammy.baylis** 05:05 Hi, Ricardo.
**John Scancella** 05:07 Hello!
**Riccardo Magliocchetti** 06:15 We're going to wait a few more minutes in order to get more people to join. In the meantime, please, if you haven't already done so, please add yourself, the…
Autosignotes document?
As an attendee, … Yep.
Just a few more minutes.
Okay, we have 5 minutes in, so I think we can start. Again, welcome everyone to this week's Python C call.
Also, let me share my screen, but I forget.
Nope.
You're on….
**Aaron Abbott** 09:10 You're back, Cardo, nice.
**Riccardo Magliocchetti** 09:12 Good to see you.
Okay, can you see my screen?
**tammy.baylis** 09:21 Yes.
**Riccardo Magliocchetti** 09:23 Okay, thank you. Okay, so again, welcome everyone. First topic for today is from Tammy.
**tammy.baylis** 09:32 Yeah, thanks.
**Riccardo Magliocchetti** 09:33 level.
**tammy.baylis** 09:34 Welcome back.
Thanks.
Yeah, so this… I've created a prototype PR for a new instrument or feature. I don't think this would need to change the core SDK at all.
I also don't think this exists in the spec, but it's inspired by an existing where there's a new labeler class in the Go HTTP instrumenter.
Where if you add, key values to it, then it will write them as custom attributes on two metrics. So I thought it'd be cool
to introduce this in the Python instrumenters, but our, of course, the languages are different. We don't have a single HTTP instrumenter. Instead, we have, like, several utils that are shared by individual… several individual instrumenters for…
like Flask, Django, Falcon, ASCII, and WSGI, so… …
This is more of a PSA, please take a look. If you've ever wanted to add custom attributes to the HTTP metrics that some of the instrumenters generated, I'd love to get your thoughts on this.
And, yeah, it would have to… this is a prototype, it introduces the labeler class, and usage of it by only the flask instrumenter. I think if I submitted this for official approval, it would have to be several smaller PRs.
Yeah, that's me.
**Aaron Abbott** 11:28 Oh, sorry.
**Riccardo Magliocchetti** 11:29 Go ahead through the ends.
**Aaron Abbott** 11:31 Yeah, I was gonna ask, so does this basically use, like, context keys? I'm sorry if I missed that.
**tammy.baylis** 11:36 Oh, yeah, I didn't talk about it. It uses context vars so that the attributes added are only within the current request and the current context.
**Aaron Abbott** 11:48 Oh, I see.
**tammy.baylis** 11:49 Yeah, that's the one.
**Aaron Abbott** 11:51 Okay.
… So what happens, like, … Is this…
So, like, if you add to them before or after the, … The metric is written.
Right, like, … If you want it to be stamped on, like, the duration, like http.server.duration, right?
Is there a specific requirement for, like, when you have to add the labels?
**tammy.baylis** 12:20 Yeah, if… if you could please scroll up to the… the flat… yeah, there we are, sorry. So that's…
there's two ways that I've identified so far, and it's not exhaustive. If a user's doing manual instrumentation like this example.
Then they can do, like, getLabeler, and then labeler.add, before returning the final response. And that would add…
Those attributes to, … right now, the… exactly the duration, request duration, histogram.
Yeah, if you scroll a bit down, the way it does this is…
Not my favorite, because there's, … oh, scroll up a little bit.
Thank you, yeah, there. So, because we're doing the split in SEMCONV for the request duration histogram.
It's, a call to enhance a new… a new util called Enhance Metric Attributes in two different places, whether it's new or old.
… And that'll merge with the, other H… that'll merge the custom.
attributes from the add calls, to the HTTP regular attributes to this histogram.
And that's one way. The other way, you can also do it in a custom distro, in various places. You could do it…
I don't think you can do it on end, I haven't actually tried it, but you can do it, during, like, SDK calls,
Anytime before the span has ended.
Or the response has been made, I should say.
**Aaron Abbott** 14:21 Yeah, I see.
So yeah, just, like, maybe one quick question is, does the semantic convention say anything about adding additional attributes that aren't, aren't part of the semantic conventions to this instrument? Like, …
Is it considered okay? Is it, you know, like a…
Good practice, bad practice kind of thing.
**tammy.baylis** 14:44 I should check that. I didn't see it linked to the Go PR issues, but I should definitely check that for current state of things, yeah.
**Aaron Abbott** 14:55 Yep.
Yeah, I mean, I'm curious about the Go, like, the use case and everything. I'm guessing that…
They did their due diligence here, just because I see a couple of the maintainers there on the issue, but…
Yeah, it seems useful, like, we have people asking for this a lot. I think in some places we have…
Instrumentations that have, like, a callback option that lets you, modify, like, span attributes, but this seems kind of like a, …
a better way to inject them from the layer that has the actual information. So, like.
You don't have to, … you know, reparse JSON or something like that, right?
… So, yeah.
Seems cool, thank you.
**tammy.baylis** 15:39 Thanks, Erin, that's really helpful.
Okay, what I'll do then, I'll double-check the spec, I'll comment on, my PR, and I think I'll create, like, a single… a new issue to kind of encapsulate, smaller issues that are already out there making the request.
Yeah, thank you again.
**Aaron Abbott** 16:03 Nice. And, just two other, kind of, like, maybe pointers would be…
Sorry if I'm talking a lot, does anybody else have any comments on this one?
Okay, I'll just keep talking unmuted. So, the… there's also baggage.
It's something that's part of, like, the spec. …
And if you read, like, the baggage spec, OTEL doesn't really implement it this way, but it seems like the intention is to inject additional attributes
So you put the kind of key values in baggage, but the kind of special case of them is that they would be propagated, like, across the wire, right?
Since there's a W3C propagator for baggage.
**tammy.baylis** 16:44 Yes. That's right.
**Aaron Abbott** 16:46 Maybe, yeah, maybe, I don't know if you can cover that in the issue.
Because I don't think baggage does what we need today.
And there's definitely cases where you don't want to, … You know, propagate the…
additional labels across the wire, but, you know, sometimes you do, like, a common one we see is, like, some higher level ID that you want, or, like, a feature flag.
And I think Sergey…
was asking about this, actually, in a couple groups, about use cases for baggage. So, if you have a specific use case in mind, and it relates to baggage, I think it would be good to explore that.
**tammy.baylis** 17:27 Okay, I'll check the baggage, W3C baggage as well. Good idea.
**Aaron Abbott** 17:35 Bye.
Awesome, thank you.
**Riccardo Magliocchetti** 17:42 Thank you.
Also, Aaron, please double-check the notes, if I had to… done correctly.
**Aaron Abbott** 17:51 Sounds good, thanks.
**Riccardo Magliocchetti** 17:53 Okay, and then next toppings for me. Also, this one will be a quick one.
I opened a PR some times ago, in draft, and I kind of forget about that, but, I think this is something I would like, to get merged, and so…
Yeah, I just made it, like, ready for review and update it a bit.
And… the point is that some colleagues, …
I'll have started a discussion on the specification of SIG.
About, like, permitting to override, …
I think this time it's only the user agent option.
in exporters, like, there is some consensus, but for some reason… … like… the actual…
text where you're adding, like, specifies some implementation details, but I'm not sure why. For example, like, what must not be available as environment variable to update.
Yeah, like, my current proposal is about, like, permitting to, … override the…
the HTTP address we set, at the moment we set the user agent, and, … content type, headers…
And, yeah, like, while I understand that
… having this, like, made freely…
Changeable by users may be an issue, but on the other hand, like.
as a distro developer, like, I don't see any other way to…
To have a way to update them?
So… Yep.
Like, if you have any opinion on the specification side, or on, … our DPR there.
Please write them, and… yeah, that's it.
**Aaron Abbott** 20:23 Cool. Okay.
Ricardo, did you, … Did you resolve, like, the technical issue with the gRPC one?
**Riccardo Magliocchetti** 20:33 Yeah, like, the gRPC one is fine, because at the moment we are, like, merging the parameter we are passing through the exporter with our default ones.
That's so… Okay.
Yeah, but, like, on the gRPC side, we are only able to override the…
What we can append to the user agent.
And… So, yeah.
**Aaron Abbott** 21:01 Bye-bye.
You were able to, like, test it with a… make sure that the server's receiving it, or…
See, I know… I know that there's that weird thing where you have to… you can't use the actual Marvin variable, you'd have to…
Set it in the, … the config that gets passed to the C code.
There's C++ code.
**Riccardo Magliocchetti** 21:22 Yeah, yeah, but, like, the gRPC stuff have already been released and merged, so…
We're fine. It's just the HTTP that behaves differently, because we are not, … we're not able to override our defaults. It's just a….
**Aaron Abbott** 21:42 Okay so do you just need reviews, or…?
**Riccardo Magliocchetti** 21:47 Yeah, reviews, opinions, because, like, as far as I understand, like, the specification…
Probably does not explicitly allow it.
**Aaron Abbott** 21:57 But….
**Riccardo Magliocchetti** 21:58 Like, I really don't see… Why it would be, like, a problem to override the user agent?
Because, like, We had adjusted, like, an SDK, like… It's not that… But, yeah, like….
**Aaron Abbott** 22:16 Yep.
Yep, okay, makes sense to me, and … Yeah.
You mentioned, sorry, you mentioned concatenating to the user agent also, right?
**Riccardo Magliocchetti** 22:28 Yeah, the specification talks about appending.
**Aaron Abbott** 22:31 Yeah.
**Riccardo Magliocchetti** 22:32 Like, but… like, personally, like… oh my gosh.
There is a comment… Which I agree with, but he's asking, but…
It probably makes more sense to pretend.
As in, you really like HTTP libraries and…
consumers of libraries and does. Blue? Yeah.
But, yeah.
So, like, for example, in my distro, what I'm implementing is, like, adding hours version, and then the SDK one.
**Aaron Abbott** 23:06 Okay, perfect, yeah.
**Riccardo Magliocchetti** 23:07 Yeah, so probably, like, we can probably, like…
just simplify this, that I could probably just add a comment there, that
we should keep, like, the original SDK version, and we can just add the upper pen and whatever we want.
They should be fine survivors, yeah.
**Aaron Abbott** 23:25 Okay, cool.
**Riccardo Magliocchetti** 23:27 Thank you.
Okay, next topic, next topics from Redeemer?
on the Langchain LMM LLM sponsor port.
**Ridhima Satam** 23:41 Yes, so, yeah, I've already brought this up in a couple of other meetings, LLM semantic conventions, and I'm just asking for reviews from the maintainers. I'm not sure if just posting it on the channel is sufficient.
But, yeah, just want a review from the… there was this GenAI system attribute, which was replicated that I have removed from it, but it's… yeah, that's the ready for review state.
If anyone has taken a look at it already, or any concerns about it, please let me know.
**Aaron Abbott** 24:16 Yeah, actually, I wanted to get Ricardo's opinion on this, just since, …
we were in, like, the Gen AI SIG, but Ricardo wasn't there, and…
He's got some experience with this stuff, but …
like, one thing in this… in this PR is it's adding the, you know, like, the request-response logging.
And, … since Langchain is kind of a framework, and then there's gonna be a call.
actually to the LLM through, like, a client library after whatever link chain … instruments, right?
You'll get, like, duplicate spans with the… or duplicate events with the prompt and response.
Possibly in, like, slightly different formats.
So, on the one hand, you know, it's, like, showing you what's happening, but on the other hand, it's, …
Double… doubling the instrumentation for pretty expensive stuff, so… … like…
I wonder… I guess two options. One is just go ahead with this, and then work on a way to have
You know, different layers cooperate, kind of like the context things that… that we just saw earlier on with the…
from, from the, from Tammy's PR with the labels.
Or, alternatively, like a, … Another… another thing would be to just not… do…
The prompt and response in the learning chain level, and tell people that they should, you know, install an instrumentation for the client library that's used under the hood.
… So yeah, does anybody have any thoughts on that?
**Sergey Sergeev** 25:48 Yeah, I was thinking about it on the back of my, mind, since the LMC, and I just realized, so, this, generative AI telemedic, so the calls are so expensive to LM that probably.
Overproducing telemetry is the least available at this point, and… Probably a vegan.
Overdue here, and just accept…
That duplication, but let people to see, okay, this is, …
This is what I see from Wangchain framework side, and this is what I see from the underlying OpenAI library.
And potentially, you'll see… … Some discrepancy, which may be the source of the problem.
But, for optimization, we can provide, later…
some instructions, like, do not install OpenAI instrumentation if you install LandChain.
Or, probably, we can configure Langchain to not include, token usage, or request response.
data in one chain instrumentation specifically, because
Customer wants to use, Like, the deepest instrumentation
possible, which will be OpenAI, instrumentation.
**Aaron Abbott** 27:25 Yeah, I mean, … I think double, maybe, is okay for now. I would, like…
You know, just because we ship kind of, like, a…
Instrument… all instrumentations library, and, you know, typically, like.
people install all the instrumentations that they need. It'd be nice if they could cooperate, and, you know, we can definitely make that work, I think.
… the… Yeah, it's kinda like, it's kind of like a… ORM, right, like…
do you want your ORM to emit its kind of intermediate representation, and then if it uses a SQL client under the hood.
you could see the actual, you know, SQL query that it's doing. And then, like you mentioned, if something's lost in translation, you can see it there.
But on the other hand, you could have, you know, like, 2MB of Base64.
So… Yeah.
**Sergey Sergeev** 28:19 It gets also funky when you try to figure out, on that.
… trace what, … Which interactions, which spans you want to evaluate.
If you use our message approach, which we also discussed.
There, and here in Gen AO2, so…
duplication will definitely be a problem, but I propose we solve it, …
Farther down the road, when we make it work in first.
And, probably propagating something like, a root level.
… Token which will prevent… duplication.
So instrumentation can check if I had Like, parent span already… Providing some better… …
telemetry, maybe I can skip emitting this telemetry, but I then convenient to make it work first with duplication.
Therefore, they optimize.
**Aaron Abbott** 29:34 Yep.
Does anybody else have any… yeah, go ahead, Ricardo, please.
**Riccardo Magliocchetti** 29:38 Yeah, I have a question about this.
Like, … like, I don't have any experience
With line chains, so my question is.
There will be, like, cases, where language, like,
language and, attributes, for example, for tokens and stuff like that would be different when,
On the… of the underlying client library.
So it's just like a wrapper, or it's just something else under the wood, but….
**Sergey Sergeev** 30:10 Yeah, it's, it's a wrapper, basically, they should match, or, some information may be not in the framework callback, which will be more detailed in OpenAI.
instrumentation callback. Example can be server address, for example. Which server did you send,
Request 2, which is present in…
OpenAI instrumentation, but not necessarily in
length chain, the benefits of having more verbose, telemetry when you have, LM invocation length chain span, and for example, from that invocation, you see that OpenAI… OpenAI URL
is pointing to your custom endpoint. And then from… open EA,
invocation, you can probably see, somehow, it can be changed by some
AI defense library, or whatever, to point to a different endpoint, so…
I think there is value in seeing both Framework… Span.
With information it captures.
and OpenA, level… That's plan, … to find…
those discrepancies. I don't know about the token usage. I think it was a bad example from me. I don't know when it may be different.
**Aaron Abbott** 31:48 Okay, thank you, because I like….
**Riccardo Magliocchetti** 31:50 I was wondering if maybe, like…
Like, if we know that the underlying… underlying client,
Instrumentation will have more data as…
When the language chain stimulation, maybe we can start slim at the language chain level.
Just, add, stuff when… you know, just add new attributes when we see that…
Like, very useful for tracing and stuff like that, but…
So, like, to me, it was like a micro, you know.
It's easier to add attributes later when removed, I think.
So, probably, you know, We could probably just start with just, …
The one we know will be useful, and add by use case, or something like that.
**Sergey Sergeev** 32:46 Yeah, and that's… Another use case is… oh, sorry, go ahead.
**Aaron Abbott** 32:52 Oh, no, please, reply to that, yeah.
**Sergey Sergeev** 32:54 Yeah, another use case is, basically a webchin, provides that high-level abstraction tries to abstract from actual implementation, so you can use, actually, calls to different providers using
different libraries, and I think they will be represented the same way, so you can use AWS Bedrock, not OpenAI compatible.
APIs, but native APIs, I think, is the same for Google, and potentially a customer doesn't have those specific instrumentations.
In some cases, and 1 chain span is important. And also, if you try to analyze one chain.
Invocation workflow graph.
You need that span.
To basically, come in from a blank chain.
But OpenAI, spans, may be important to monitoring.
like, all OpenAI, compatible APIs and token usage.
Which target those spaces.
Sorry, for variables… And random examples, go ahead there.
**Aaron Abbott** 34:11 Yeah, … I was gonna say…
One thing on the token counts is, at least, like, our backend, it just counts the… if you want the overall token usage of an invocation, it just looks at all of the genai.token
attributes. So if you, if, you know, you double…
double emit spans, then those get double counted, and are, like, I'm just speaking for Google's UI,
And from, like, a high level, I'm not sure how you would work around that, unless, for example, you thread, like, invocation ID through.
And then you deduplicate based on invocation ID to the…
to the LLM, which is separate from, …
Which is separate from, like, the invocation ID and the agent level, right? So… …
I don't know, that's… that's one thought. I know, like, TraceLoop already does this. I think they have some way to coordinate between… if you're using, like, OpenAI and…
LingChain.
It seems like the main use case here is, like, if you're using a…
A more exotic backend we don't have instrumentation for, you can still get
The telemetry out, just from the higher level.
… Which might be valuable for at least, like, eval purposes, right?
**Ridhima Satam** 35:20 One point I want to raise here is, and I'm not sure if it's the answer for what you just said, Aaron, is, last time we were proposing AI… sorry, genai.framework.
attribute which we would be adding, a new attribute which we'd be adding on the line chain generated spans. So, if that would help us to differentiate between the count, right? Token usage, sorry. So….
**Aaron Abbott** 35:48 Yeah, that's if we consider, ….
**Ridhima Satam** 35:52 Only the one of them, yeah.
And not duplicate token usages.
**Aaron Abbott** 35:57 Yep.
So, unfortunately, I gotta drop. I'll take a look at the other issues here, but yeah, like, please continue this conversation.
like, for me, the main thing I'm interested in on the link chain one is the, kind of, framework level stuff, so, you know, seeing the conversation ID and stuff like that, I don't know if that's in this PR.
But I also don't want to block this, like, …
So, I don't know. Ricardo, please, you know, continue, but I gotta drop. Sorry.
**Riccardo Magliocchetti** 36:28 Okay, no problem.
**Ridhima Satam** 36:30 Yeah, if any other concerns, if we have, to add anything, we can always add in the follow-up PR.
Yeah, that would be helpful, like, if, like, just add and center it, if we need any conversation ID. Right now, it's not there, but, we can add it, like, as a follow-up here. Because this is, like, we are splitting up
in small PRs. Right now, it's just the span implementation for LLM invocation. We would get in metrics and events as well, and any other enhancement, if we want to do, we can always do this. We're continuing work on this.
Yeah. And then the next thing I want to move is to the, the other PR, which is still, asking for review. So this is from my colleague, Keith Decker, who couldn't join today. It's just the boilerplate code for starting the GenAI util structure.
I think Aaron, is aware of this, but yeah, just asking for review on that.
**Riccardo Magliocchetti** 37:33 Okay, thank you.
So, this is, like, a new package, or…? Yeah.
Okay. I'll try to take a look.
Thank you Thanks. By the way, back on the… what's cool.
On the long-chain instrumentation, like, to me, like, it's fine to apply the double span, but…
It's just, like, probably, like.
The issue for me would be, like, to have, like, a ton of attributes on the line chain span, but my…
may just have, like, again, duplication for the anina… client library instrumentation spot.
But yeah, like, I'll probably just take a look at the PR and comment there.
So, thank you again.
Anyone has other comments on Vision AI things?
Okay, so we'll move to the next topic from Sergeye.
**Sergey Sergeev** 38:52 Yeah, sorry, I, noticed some opportunity to ask questions, probably I could,
dig deeper myself and try to figure it out, but wanted to ask this group of
Python OpenTelement experts, what can be the direction of… …
What are the approach, to…
have TraceHoop instrumentation, so we have 26 packages of TraceHoop, instrumentation libraries, which, are being donated to OpenTelemetry Project.
And LAMPChain is there for… to rebuild it, basically in the OpenTelemet project. We are working on it, but you can see there are questions and, …
challenges to move fast. So, we were doing… we were thinking as a stopgap solution, 2…
Implement some translator adapter, which will,
as part of the OpenTelemetry stack, so if you're using zero-code instrumentation from the OpenTelemetry distro package.
And you launch your application as OpenTelemet instrument.
And then your, application, and second, you install one of the TraceWoob Labor is.
How can we convert that telemet emitted by TraceWhoop instrumentation package?
int, … So you might see a convention format, so we can…
still benefit from semantic conventions.
and use JSOOP, instrumentations with zero-cut instrumentation.
Basically through… instrument applications until we move it to the OpenTelemator project and change to emit semantic conventions.
Have I confused this group?
**Riccardo Magliocchetti** 41:07 Yeah, that's a big question.
**Sergey Sergeev** 41:12 But, do you understand the problem? We are trying to.
**Riccardo Magliocchetti** 41:16 Yeah.
Yeah, probably, like… for tracing, probably a spam processors, a spam processors may be useful.
But I don't think we have the same for metrics.
**Sergey Sergeev** 41:31 So, yeah, basically, a span processor… is Span Processor a Python implementation, or is it an OpenTelemetry Collector concept?
**Riccardo Magliocchetti** 41:43 Yeah, but I think we have one also… into our SDK.
But, yeah, probably, like, something at the OpenTable collector level, maybe…
the right solution, I guess.
Selected.
When you need it, You had, you know, you had the proper translation on the collector's side, yeah.
**Sergey Sergeev** 42:12 ….
**Riccardo Magliocchetti** 42:12 like, this will also be shared with the JS implementation, I guess, so….
**Sergey Sergeev** 42:18 But if we do it, in the Python stack, what are the options? Just wanted to…
Document, what is the potential to… Intercept or the telemedi.
from… …
From the TraceWhoop instrumentation library and remap it to a different attribute values, or convert some of the complex
values, like JSON, structure, serialized testing.
into… To flatten it, to… Attributes in semantic convention.
**Riccardo Magliocchetti** 43:01 like, as far as I know, I don't think we have, like, a generic… way to handle beast, so…
Other than the spam processors, maybe, but…
Other than that, like, I don't know if you have something else in place already.
**tammy.baylis** 43:23 Will this be, … will you be doing, manual instrumentations of all these libraries during the transition, or will be… will you be using something like a custom distro? Like, what…
What else can you, describe about the use case, Sergei?
**Sergey Sergeev** 43:45 Yeah, let me, probably, show, how it looks like, No…
Let me share this game.
So, those are basically… T-Swoop.
Packages.
Notice that, basically TraceWhoop, already thought of them as OpenTelemetry projects, so even the naming here
is might just, … open telemetry project, the challenge is, that, Basically, the attribute names here.
All sitting on Facebook.
attribute.
So, you can install… Basically… One chain instrumentation from here.
And use it with zero-chord instrumentation.
…
Me.
Yeah, so you can use it with zero-quote instrumentation.
Sorry.
I definitely didn't prepare well, …
Cisco, let me find an example.
… Give me… ….
**Ridhima Satam** 45:33 Basically, you can….
**Sergey Sergeev** 45:35 you can definitely run it, like this, just after installing the Facebook package.
You can run it, and, you will get, Telematy from JSW, OpenOMT, into…
the traceable format. So, the question was, can we…
implement something in the Python stack of OpenTelemet, something like a callback, which will be mutating Telemet
Specifically spans, emitted by trace hoop, and, Changing it from Format of TraceWhoop Instrumentation Library.
into… basically, semantic conventions.
Which I defined currently in LMSIG.
**tammy.baylis** 46:33 Oh, okay.
Yeah, thanks for sharing.
…
Yeah, I don't have too much more to add on top of what Ricardo already mentioned. Like, if you had services that were only running with these dedicated instrumenters and not anything else in regular open telemetry.
then, setting up some sort of, transformer or processor in an OTel collector instance is an option.
I don't know of any specific, processors that add attributes. There, there might be, or you could implement
a new one. But if you're doing the, the zero code, …
and you're hoping to use both regular OTEL SDK and instrumenters with, these, OpenLelementary instrumenters, then…
Yeah, you could, … inherit from OTel Python's existing span processor.
And, let me see… Yeah, that's…
That's the main span processor. If you want to add attributes to a span, I've found that you should do it at the on start, function.
Because once a span has ended in OpenTelemetry Python, it's immutable, and you can't add attributes, so the on starts…
one place to add attributes, but yeah, as Ricardo mentioned, I don't know what kind of support there is
For, metrics attributes, …
and the… the metrics readers are… are more complicated, than I… I think I can explain right now, but that's… that's one way. If… if you… or you can, …
Look also into… hang on.
I was thinking for a moment, oh, you can specify an entry point for your custom span processor class, but I don't know if that's possible, like, it is for exporters.
…
And I… I don't know… I don't know if that's helped. I feel like I've been rambling, but that's… that's one…
the on-start method is one place, one way you can add custom attributes.
**Sergey Sergeev** 49:14 Oh, so basically just implementing your own spend processor, …
Releasing it as a package, and basically configuring custom spend processor in that zero-code instrumentation.
And then that custom spend processor can… Do this dirty job of… Changing… …
attributes. So, basically instrumentation will be…
Trying to report telemetry using that spent processor.
**tammy.baylis** 49:52 play.
**Sergey Sergeev** 49:53 Build a beer.
Yeah, I think I need to look into it, …
How we can transform it here.
Yeah, I think I got an idea, and sorry.
**tammy.baylis** 50:08 Okay.
**Sergey Sergeev** 50:09 I could do a better research. It was kind of open, and that new big question, because…
I wasn't sure what, the options we have.
**tammy.baylis** 50:21 Oh, yeah, that's totally fine.
**Riccardo Magliocchetti** 50:25 But way, for our experimentation and… the setup of the SDK.
Just take a look at the SCON configuration module.
inside OpenTender SDK directory, and you see… Our stuff is loaded, …
Because by default, I think.
Yeah, like, by default, … We had, … Only this path for cells.
So you'll probably need some work around that code also.
Too wavy to work, like… Magically.
**Sergey Sergeev** 51:21 Okay.
Thank you for the suggestion.
Yeah, if you can add this link to… yeah.
And second was a jazzpen processor.
Okay.
**Riccardo Magliocchetti** 51:54 Yup.
Okay, thank you.
So, yeah, this was the last topic for today, and it's the last email topic, or…
Something to add on the previous ones.
Okay.
So, thank you everyone for participating, and see you next week.
Bye, right?
**tammy.baylis** 52:24 Thanks, everyone. Bye.
**Ridhima Satam** 52:26 Goodbye.
