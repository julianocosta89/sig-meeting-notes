SIG: LLM Semantic Convention WG
Date: 2025-09-30
Duration: 62 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 02:43 Hello, hi everybody.
**Sergey Sergeev** 02:46 Hey.
**Josh Bonczkowski** 02:48 Hello.
**Liudmila Molkova** 02:50 Okay, so let's get started.
Let me share my screen… Okay, so while we're waiting for folks to join, let's do some triage. I've been, trying to clean this board a little bit before we… before this call.
But there are plenty of things, to clean up.
So what do we have in progress?
So, the common appeals, I think, Sergey, you have something on the agenda to talk about it? That's wonderful.
And by the way, while we are doing the triage, folks, please go ahead and add things to the agenda.
The reasoning… we have a PR… For… this… But I believe there were no updates.
Okay, we have example… And we have… No… We have the… Code sample for the model.
So this one is… Pretty close… So I'll take a look, and if there is no problem with it, and if nobody else raises any concerns, I would like to merge it, By the end of this week.
Okay, what else do we have in progress?
I think there was no update on… This one… Hmm.
Okay, there are still some discussions, so let's… Move on… MCP, I didn't do any progress since last week, so it's still in progress.
and the OpenAI embedding instrumentation.
Okay, we still need some approvals here.
So let's just go through the least of in progress things, and then we'll move on to the main agenda.
Attributes Virginia External Storage Reference. Is Aaron here? Yeah, you're here.
**Aaron Abbott** 06:27 Yep, I'm here.
**Liudmila Molkova** 06:30 I think we… we discussed that we are… Probably need some real… usage, feedback.
From it, or intense system, Do you feel we should park this for now, or, like, do you want to proceed with the proposal?
**Aaron Abbott** 06:50 I'm okay to park it for now. There is, like, the PR, and I have… Like, an implementation.
I'm happy to kind of show how it works a little bit later, but definitely not ready to do that right now.
And.
**Liudmila Molkova** 07:07 Okay.
**Aaron Abbott** 07:08 Yep.
**Liudmila Molkova** 07:09 So I'll just move it to to-do then.
**Aaron Abbott** 07:12 Well, I mean, I do have a PR.
**Liudmila Molkova** 07:15 Oh.
Okay.
**Aaron Abbott** 07:18 Tara, what do you think?
**Liudmila Molkova** 07:24 I think we are… not ready to merge this PR, right? And, Staleboat will come and try to close it, so we should either convert it to draft.
Or, right, so, like, I would rather convert it to draft until we feel confident we… We are ready to go with it.
**Aaron Abbott** 07:50 Okay, that sounds good to me.
Do you wanna just hit the… Draft button for me.
**Liudmila Molkova** 07:56 Yeah, I can never find what it is.
**Aaron Abbott** 07:59 It's at the top, yeah.
**Liudmila Molkova** 08:00 Yeah.
Okay, what do we have? So we have… JSON schema for blob and file in the agenda.
We will talk about it more.
And just, let's take a quick look… This one… So, Alibaba folks would like to add, They're, constant names, but we don't recommend adding constants only.
And we ask them to… add, the document that describes Alibaba semantic conventions, even if it's just slightly, different than the generic one. I think they didn't follow up on this yet, so we'll keep it in progress.
Okay, moving on to the main agenda… Intro for new members! So, if you are new to this group, or if you're not new, but you would like to introduce yourself and tell us what brings you here, the stage is yours.
**Michael He** 10:00 Yeah, I can give a quick intro. Hey everyone, I'm Michael. I'm from AWS. I think my team is in CloudWatch, and we own the AWS distro for OpenTelemetry SDKs. I think, recently, we've kind of started moving more into the GenAI instrumentation space as well, so… I guess that's kind of, my reason for being here. I have some work budget, but I think almost… I'm also just, like, interested as well. So, yeah, looking forward to being a part of the community and contributing.
**Liudmila Molkova** 10:29 Awesome, great to have you.
**Joseph Wang** 10:33 Hi, this is Joseph, from Roblox. So, I'm working on the ILM of the VT solution for Roblox internally, and as Roblox has been building a lot of AI applications, we are trying to What kind of the solution, following the official semantic combination? Yeah, so… starting from this week, I will try to join this meeting and try to contribute and also discuss, any potential topics.
Yeah, thank you, and nice to meet you guys.
**Liudmila Molkova** 11:11 Nice to meet you. Thanks for coming.
Okay, anybody else?
Okay. If you would like to discuss anything, the agenda is up and anybody can add things. You're more than welcome to bring your topics and… Where's this?
Let's move on to… the… things… to review. So I think there is not much discussion on the embedding instrumentation, and Drew is not here, so we probably… Don't need to talk about it.
The reasoning part is also probably just something to review quickly.
I wanted to spend some time talking about the, blob and file parts.
And also… GenAI inference… Pierre… Sergey, is it the same one as your topic?
**Sergey Sergeev** 12:22 Slightly different, so…
**Liudmila Molkova** 12:24 Oh, okay.
**Sergey Sergeev** 12:25 is here to chat about inference. Mine is more, design level.
**Liudmila Molkova** 12:33 Okay, so I'm going to take these two friends and put them… At the end here, so for.
**Sergey Sergeev** 12:41 Yeah.
**Liudmila Molkova** 12:41 Yes.
**Sergey Sergeev** 12:41 My only ask, if I can, probably go before kids, I will need to drop off to a different meeting in 20 minutes.
**Liudmila Molkova** 12:52 Yeah, you're the first one in the agenda now.
So, do you want to go ahead? Do you want to share? Do you want me to share?
**Sergey Sergeev** 13:02 Yeah, yeah, I can probably… Sure, you, you, you, you… oh, oops.
Yeah, if you can add letter T to the URL.
**Liudmila Molkova** 13:16 I apologize.
Oh.
**Sergey Sergeev** 13:23 Yeah, it's a bit, you know…
**Liudmila Molkova** 13:26 I did it before I got my coffee.
10 hours.
**Sergey Sergeev** 13:29 Yeah, in general, so, what we are doing, and I really appreciate, Aaron's and, Dylan's, help.
from the Python instrumentation side.
So, I tried to put together, me and my friend, we created this, Read Me Doc, basically the latest idea on… Utivision AI design, and, specifically, I wanted, to briefly chat about different flavors of, OpenTelemetry.
We have an semantic convention and how to support it.
And, how do we want to support, traceful background compatibility?
If you can go… so, telemetry of waivers is one of the topics, to which degree you want to support all those different, Kind of modular… Telemetry emitters from utility function.
I think, Aaron brought it up that we really want to chat about this topic in this group.
Specifically, Is the telemet a… do we expect more divergence in… Telemetry we produce as part of this semantic convention.
Or is it only about, Evaluation… sorry, or is it about, conversation data, or, messages.
Which can be a part of span attributes.
Or, which can be… events. That's, the biggest divergence right now in telemetry flavors? And second, do we have use cases when some providers we need only spans without metrics, and MetX can be optional. That's my two questions, and third, I wanted to discuss about TraceWhoop compatibility emitter for background compatibility with TraceWoop.
So we can start really moving, trace hoop instrumentations to buy 10 gun trip.
And, maintain background compatibility with JShoop.
We have, effort bytes here.
It's a meteor.
Sorry, it's a lot of information. Ludmila, does it make sense to you, at least?
**Liudmila Molkova** 16:18 Yeah, so let's take things one by one. So let's start.
**Sergey Sergeev** 16:22 Yeah, if you go back to the agenda, I think I… Poised, the specific questions.
There. Okay. The first is, OpenTelematy Foreverse.
**Liudmila Molkova** 16:34 Yeah, so, this usually is not a choice of instrumentation. Instrumentation emits what it wants, and users configure what they want, right? If users don't want metrics, they just don't enable metrics SDK.
And we have relatively cheap ways to know when it happens.
So, if metrics are not configured, you just don't emit metrics, like.
users don't need to make any additional choices, except not configuring metrics SDK.
For events, things are a bit more interesting.
So, we currently give users a choice to opt in into spans, span attributes or events attributes.
We… Can… like, I think that we will have to keep some of configuration here, and it's also an explicit configuration. We ask users to opt in into Prompts and completions anyway.
Right? And then, when they opt in, they can choose, what… where they want them to be. Sorry.
So… for… for the first… I… I don't… like, this is very unconventional for open telemetry to have this concept of a meter, and to have a configuration that helps users configure the signals. It's not necessary.
**Sergey Sergeev** 18:10 So, basically, if customers don't want metric, they just disable metric provider, or they not configure it.
**Liudmila Molkova** 18:17 They just not configure it, yes.
**Sergey Sergeev** 18:19 Yes.
Makes sense, And second, for events, again, I agree with, Aaron's overall feedback. We should not over-complicate it until really necessary, so it can be basically semantic conventions, emitter… which can be completely swapped with tracewoop-compatible emitter, and we can, achieve the use and basically some composition approaches by using some utility functions, like semantic convention attributes.
so, again, the key is to have some option to move trace loop instrumentation into Python can tape.
have.
**Liudmila Molkova** 19:19 So, where does this goal come from? I don't think we ever had a goal to support trace-loop semantic conventions in OpenTelemetry.
**Sergey Sergeev** 19:28 Yeah, yeah, yeah. We want to support only semantic conventions, but we want to have, basically, TraceHoop. We want to leverage TraceHoop instrumentation libraries. They have a good coverage, and they are willing to donate it to OpenTelematy, so…
**Liudmila Molkova** 19:45 Users who want to keep traceloop conventions can keep using traceloop libraries. They don't need to upgrade open telemetry instrumentations.
**Sergey Sergeev** 19:55 Yeah, it's a bigger question, so, why we don't get, adoption here in this group, with Python vanilla instrumentation. So, the challenge is that TraceWhoop is a little bit ahead of defining what they need in terms of setting up proprietary TraceWhoop, attributes, for example, and so on. And we don't have a semantic convention for it, it will take some time to develop it. So, the whole idea of, separating instrumentation from the actual telemetry in Utilogen AI is that, We can, have instrumentation We can have trace loop instrumentation separated from Telemetry, so we can produce, Semantic conventions with emitters we have in Python can type in OpenTelemetry project. But, in order to have, basically, to avoid, maintaining both Tyswoop instrumentation and OpenTelemetry manual instrumentations, we need to provide some way, for Tyswoop to maintain their own telemetry, so the whole idea of TradeWhoop compatible Emitter is that we can have, And tracewoop basically follows semantic conventions, but it has some extra attributes. So, if we have that tracewoop-compatible emitter, we will have a way to use all the TriShoop instrumentation libraries, Once we switch it, To use in Utilogen AI. And TraceWoop will have a way to produce background-compatible telemet, which will be coming from an external package.
Does it make sense?
**Liudmila Molkova** 22:02 So what you're saying, that the trace loop has extra features that are not specified in semantic conventions, and you would like To instrumentations that we have to have enough extensibility to support these additional scenarios if somebody wants to implement them on top of open telemetry instrumentations.
**Sergey Sergeev** 22:23 Yep.
**Liudmila Molkova** 22:24 Alex brings a great point in the chat. Alex, do you want to go ahead and say it out loud?
**Alex Hall** 22:31 Just could we use requester response hooks that were, like.
You know, it seems like we'd want this kind of extensibility in general.
And if request-response talks don't work here, maybe that's a sign that we need to think about why.
**Sergey Sergeev** 22:46 Yeah, specifically, Utilogen AI, so it, also defines some data types which will let, basically, in-house, instrument… in-house agentic frameworks, for example, to be instrumented.
Using those, data types.
And, the whole idea is that you will simplify both instrumentation side development, manual instrumentation of your application.
And, we should not overcomplicate background compatibility. So, for example, if you want to support LM invocation, if you want to add, some additional attributes to it, and we have only that many attributes defined in semantic convention.
So, we should add, basically, instrumentation to pass, the request response, As an additional, argument, to that LM annotation data type, so instrumentations ahead of semantic convention can do it, hopefully it makes sense, Alex.
**Alex Hall** 24:06 No, I didn't follow what you meant by request data type, so you're talking about setting the request as a spam attribute?
**Sergey Sergeev** 24:13 Yeah, if… if we go to, back to the arrhythmia, maybe I should…
**Alex Hall** 24:21 like, will there be request and response hooks? Because, for example, Logfi would also like to add Logfire-specific attributes.
And be able to use this.
**Sergey Sergeev** 24:33 Yeah, I… I would like to explore more about request-response hooks, so.
**Liudmila Molkova** 24:41 Again, we, in the current design, so instrumentation, if you go back to the README, so it will be an example of the usage, Where is it?
**Sergey Sergeev** 24:56 8.
Yeah, let me probably, take over… the documentation.
Yeah, let me share the screen quickly.
**Liudmila Molkova** 25:10 Yeah, sorry. I'm trying.
**Sergey Sergeev** 25:12 Yep.
Dim, Okay, never mind, I changed a little bit.
**Alex Hall** 25:30 What is extensibility summary have?
**Sergey Sergeev** 25:35 Say it again?
**Alex Hall** 25:37 Extensibility summary, what's that?
**Sergey Sergeev** 25:40 That's where we can, in the current design, basically, where we can put different, telemetry… emitters, which operate, importantly, with GenAI types and so on, so you don't have to… To get to the span level, for example, and you operate, with specific data types, So, this is an example, basically how, the UTL GenA, may be used, so you create a handler.
Which is, basically acquired, from Utilogen AI, and, you can use types, like OM and vacation.
And basically, some named, arguments to those types of fields, are those which defined in semantic convention, but OM anniversation is not telemet yet.
And, basically, you, you submit, the start LOM and stop LOM, you can, add more, data to this type, but importantly, Ignore this one, it's just for testing, but importantly is that user can configure which emitters to use, so if you use default semantic convention emitter, it will basically turn this LM invocation into a semantic convention compatible telemetry, and based on how you configure it.
which environment variables you used. It will put, for example, conversation data to spy an attribute, or to an event. It will produce metrics if you configure automatic provider, and so on.
So, as instrumentation developer, you don't have to think about, Actual telemetry, so it should simplify The development of instrumentations. And second, if TraceWoop wants to maintain their own telemetry, so they don't have to just copy all the instrumentation, all they need to do is to provide a different, telemetry emitter.
Again, which should be coded to Utiogen AI Type's API.
And operate with this, model.
**Alex Hall** 28:20 So, look, let's suppose that the OpenAI instrumentation uses these utils.
I think it should be possible for trace loop, or pedantic log fire.
or Open Influence arise to essentially create a wrapper around the OpenAI instrumentation.
which uses some kind of extensibility API to add custom attributes or whatever else it might need.
without having to reach into the internals of utils. So, it passes some kind of request-to-response hook to OpenAI, or some other hook, maybe, like, which takes an LLM invocation object.
**Sergey Sergeev** 29:01 Yeah, so, basically, all you need for this development is, oh, I'm on vacation from this utility function. Again, it's optional. If you, as a developer of instrumentation, if you find it helpful, you can use those APIs and make sure… and this utility function will make sure that it will produce telemetry in semantic convention.
And these…
**Alex Hall** 29:30 I do have to admit that it's a bad sign if the way to add extra attributes is to have something inside. If it's not doable from the outside, it's a problem.
**Sergey Sergeev** 29:42 Inside, outside, so, again, LM on vacation will have just, a dictionary of attributes, so, the only name fields which are part of semantic convention. Everything else comes as a dictionary. It may be request response.
We need to figure out, how to make it helpful. And again, we strive, we will strive to… Name all those attributes helpful.
That's… I will have to jump in a minute to a different meeting. Sorry, Aaron, if you want to add something, but Keith and Aaron and Pablo, I think, can continue this discussion.
I think we can just… we have some of the packages in the repo, and I think Aaron and Dune already started on the Google instrumentation.
to use Retail Gen AI, just… To see if it fits or not.
But, yeah, the key… Questions to answer… to answer, If this extensibility model makes sense, or… If you guys think we should take a different approach for this.
**Aaron Abbott** 31:23 Finally.
**Sergey Sergeev** 31:24 I have to learn.
**Aaron Abbott** 31:26 Yeah, yeah.
No worries, see you later.
Okay, well, I was gonna say, I think, I didn't quite understand what you meant by inside and outside, Alex, but… It seems like the difference between hooks and what's proposed here is, what's proposed here is more… one or the other, and not necessarily additive, whereas the hooks would be additive. Like, you get the hotel instrumentation no matter what you do, and then you can do stuff with the hooks, but you can't… change the implementation wholesale, right?
**Alex Hall** 31:59 Yeah, I mean, the environment variable with the tracelope emitter, whatever, I don't know what exactly it did.
**Aaron Abbott** 32:06 Hmm.
**Alex Hall** 32:07 If… If it did something that couldn't easily be accomplished by some external-facing API, That's where I'm worried.
**Liudmila Molkova** 32:19 I think it's complementary, right? So, assuming… we use hooks. What we don't have in the completion hook today is extra information.
Right, we have the chat history, and that's it.
So we probably need to add more information about request parameters and response properties.
**Alex Hall** 32:41 Yeah, I think that it should be possible for hooks to take you know, vendor-specific things, like the OpenAI instrumentation should accept an OpenAI Request slash response.
or whatever.
What actually makes sense, but…
**Liudmila Molkova** 32:56 Oh, interesting, yeah.
That makes sense. And then, If it happens, then somebody who configures this hook Can build anything additional.
Based on this extra data.
But the hook will be called with vendor-specific APIs, right?
So you would need to build, something that That's specific to every instrumentation as well.
**Alex Hall** 33:32 And you can also have a hook at the utils level, That has utils-only objects, but… which I imagine would be useful for some things, like, for example, if there's a trace loop.
attribute name for the request model, and it's somehow useful to use that attribute name instead of the current OTAR ones. I don't know what a good example is, but you can imagine that there might be some generic things that TraceLoop would still like, but I think that, ultimately, you know, like, for example, in Pydantic AI, I think we'd want to be able to take you know, the agent run results or whatever, by identifying specific objects and… Add, for example, I don't know, parts that haven't been defined yet in a hotel.
**Liudmila Molkova** 34:16 Right, so essentially what you want to do, like, all the extra is something that it's not in conventions yet, and therefore it's not in the deals yet.
It's, like, if you want to just rename the attribute, you can use a span processor for it, you don't really need any hooks or anything complicated.
So all the interesting things, all the additive things are not… that are not in the API yet.
**Alex Hall** 34:44 Yeah, a spam processor will only work for attributes that are already in the spam.
**Liudmila Molkova** 34:49 Right.
So you can rename attributes easily, but what you miss is the… Information that's not on the SPENS yet.
**Alex Hall** 34:59 Sure, let's to say there's some other information in the request and the response that isn't in spans at all.
**Liudmila Molkova** 35:03 Right.
**Aaron Abbott** 35:05 Yeah, I mean, I think it would still be good… like, it does seem a little risky to have each hook tied to an instrumentation. Seems like kind of a nightmare in terms of…
**Alex Hall** 35:15 That's how hooks generally are, like, you know, hooks for Django and… HTTPX and so long they take.
library-specific objects.
**Aaron Abbott** 35:25 Yeah.
**Liudmila Molkova** 35:26 But there's, like, a 30…
**Aaron Abbott** 35:28 instrumentations in, Traceloop, for example, right? Like, I think we have about 45 in Contrib.
just, is gonna… gonna be a big number of them, I guess, but… Like, it seems like it would be nice if people could contribute to the instrumentation and add a generic thing to the hook.
Instead of having to reinvent it over and over again. So you have, like, you know, Pydantic hook or the Google hook, and they all go in and, for example, read the some property that's not defined yet in the Semitic conventions.
**Alex Hall** 36:07 I think it would be a matter of the tracing group.
**Aaron Abbott** 36:09 instrumentations, like, the libraries that are in TraceLoop, and that…
**Alex Hall** 36:13 are ahead of OTAL in their own way.
They will make use of… the… The OpenTelemetry one.
with GenAI Utils.
And then they would extend it, they would wrap around it.
With some hook.
**Liudmila Molkova** 36:38 So you would, like, let's say in the lockfire, you would actually build a wrapper that's specific to OpenAI, and a wrapper that's specific to Langchain, and so on.
**Alex Hall** 36:57 Yeah.
**Aaron Abbott** 37:06 So would you prefer to just, like, subclass the instrumentation, and have hooks in the instrumentation to use?
**Alex Hall** 37:19 Our hooks tend to be passed as functions.
No, it's subclassic.
**Aaron Abbott** 37:25 Yeah, yeah, I… yeah, either way is fine. I meant more, like, is the thing that you want to expose a separate instrumentation class, like an instrumenter, which would be used instead of the hotel one.
**Alex Hall** 37:40 We generally expose just a method like logfy.instrumentOpenai.
**Aaron Abbott** 37:55 Yeah, I guess I'm asking more in the context of, like, the auto instrumentation, where we load stuff from entry points.
And maybe that's not super important to you guys, that's totally valid as well.
**Liudmila Molkova** 38:21 Should we move on to the… Relevant PR from Keith?
**Aaron Abbott** 38:31 Yeah, sure.
**Liudmila Molkova** 38:38 Kiss, do you want to guide us through?
**Keith Decker** 38:41 Sure, so this is the… the first start of the GenA tools for inference, we've been working with Dylan and Aaron to Get this in a place for merging, So it's kind of a early adaptation of what Sergey's talking about there, though in this case, we're just adding the ability to extract the span creation from from instrumentation and put it into the Gen AI utils. So, follow-up PRs will have metrics and events.
And more attributes, so… Just need more eyes on this, yes.
**Liudmila Molkova** 39:27 Is there any discussions that, worth having here?
And it's, it's already introduced to some of the things for you.
Just discuss trade.
**Keith Decker** 39:38 Right.
**Aaron Abbott** 39:44 I mean, does this add the separate emitters, or is this just, kind of like the default implementation? Like, the default…
**Keith Decker** 39:51 Just the… just the default, we took all that.
**Aaron Abbott** 39:55 And is there any, like, entry point loading? So it's just the… this is the implementation that gets used kind of thing?
**Keith Decker** 40:02 Just implementation that gets used.
**Aaron Abbott** 40:07 Okay.
I mean, in that case, this seems like… Just a pretty straightforward internal implementation detail thing, like a utils, so…
**Keith Decker** 40:17 Crump.
**Aaron Abbott** 40:18 Yeah, I'm happy to just review this then.
That makes sense, Lydnola, that seems… Kind of separate from the other topic.
**Liudmila Molkova** 40:28 Yeah, I think the intersection is that if we're introducing something like LLM and Vacation, right.
Then, it would be… Eventually accessible through hooks.
Right?
And, we'll need to… evolved over the time, but yeah, it seems orthogonal.
**Keith Decker** 41:00 Yeah, for that hook discussion, right now the LMM location in this PR has an attributes field, which is just where you stash any extra XDX roots on the span you want, and that will get added to the span. This is basically just a data class for people to Throw everything they want, and then we… Use the named attributes for semantic convention.
Span attributes, everything else just gets tacked on as extra span attributes.
So we don't have hooks per se, it's just, it's a dictionary of attributes.
**Aaron Abbott** 41:40 Okay, yeah, I'll, I'll try to review… Maybe… it might be tomorrow?
**Keith Decker** 41:46 Okay.
**Liudmila Molkova** 41:53 Cool, thank you.
Moving on to the next one.
Michael PR review request, agent spend support to link chain.
**Michael He** 42:15 Yeah, I think this one kind of just, I know folks at Splunk and Cisco already put up, like, the skeleton and the LLM span support, so this is kind of, just building on top of that to add the Asian span support. I think, pretty much just follows the same pattern where we hook into the callback manager.
for Langchain, the on-chain start, on-chain end.
Yeah, I guess… Main thing is the, chain, or the, operation semantic convention value for the chain start.
it is a custom value, just because, I didn't see any, explicit value called out in the, spec, but yeah, I just wanted to call that out in case that was a point of contention. But, yeah, other than that, I think, yeah, mostly just an extension of what already exists.
**Aaron Abbott** 43:14 I actually have a… I don't want to distract too much, but I'm guessing we're using, like, the agent invocation… the agent ID, agent name.
attributes, right?
Okay.
Yeah, I was a little confused by those as I read through the semantic conventions again, because they're defined as, like.
server event, like, execute Remote Agent.
I don't know if that's how people are using it in practice, but… Do people know what I'm talking about?
**Liudmila Molkova** 43:50 Oh, I think I, I've, I've seen it. You're, you mentioned, Dan, I agree.
Yeah, I agree it's confusing that the invoke agent is a client spin, right?
**Aaron Abbott** 44:01 Yeah, yeah, exactly.
**Liudmila Molkova** 44:08 So, it's actually pro- probably should be… Good question. So we need to have more, more language here, saying whether it's Client, if it's a remote agent or internal, if it's the… What should it be?
**Alex Hall** 44:25 This is Create Agent, and I think invoke agent is the name, but CreateAgent, I don't even know what that means in general.
**Liudmila Molkova** 44:32 Good.
**Aaron Abbott** 44:36 Yes, too.
**Alex Hall** 44:38 Yeah.
**Aaron Abbott** 44:38 There's still this first line, also, underneath status, it says, invocation is usually applicable when working with remote agent services.
And I… I feel like, I don't really understand what that's supposed to mean. I remember discussing this when we merged the PR, and there was, like, a white paper, but I don't know if that's necessarily the most commonly used, terminology anymore.
**Alex Hall** 44:59 Yep, we're trying to follow this convention in Pydantic AI, which is all local.
I don't know why it says that.
**Liudmila Molkova** 45:10 I think it was the straightforward thing to do for things like OpenAI Assistance.
And… We had some discussion on whether it's applicable to the, local agents, and we didn't know.
So that's why it's limited to the remote agents. It sounds like it can be extended, but it's… there is some work to be done.
**Alex Hall** 45:45 Is there any part of it that's not applicable to local agents?
**Liudmila Molkova** 45:49 Like, these tiny details, right? What should be the spent kind,
**Aaron Abbott** 46:01 Do we typically have, like, two separate entries and semantic conventions for client and server, or would we just say, like, it could be either type?
I think we usually have separate, right?
**Liudmila Molkova** 46:12 Well, it's not a server either, right? It's… we don't know.
So, if it's a client-to-server, and it should be two separate entries here.
It sh… it's… it's…
**Alex Hall** 46:27 If it's local, it would be internal, right?
**Liudmila Molkova** 46:30 If it's slow… yeah, probably yes.
Unless you're, expose the agent.
as the API, and then your urgent invocation matches your incoming request or something.
So, it's… Very key.
**Aaron Abbott** 46:53 Yeah, so if you had, like, say, an A to A server.
Running over this, you would have a server span maybe for… A to A, and then you would have an internal for whatever the actual internal, like, LaneChain or whatever actual agent framework you're using runs the agent. Is that kind of what you're saying?
**Liudmila Molkova** 47:12 Right.
And you probably would have a different set of attributes, right? So, for example, we have server address and server port somewhere here.
Which makes sense if you invoke something remote, but if you work with local legend, then probably it doesn't make much sense.
**Aaron Abbott** 47:33 Yep.
Okay, so maybe for this PR, like.
If you don't set it, it's internal, right?
**Liudmila Molkova** 47:41 If you don't set it, it's in… Sure, no, yes.
**Aaron Abbott** 47:45 Okay, so maybe just… That makes sense to me, and maybe as, like, a follow-up to this PR.
I don't know, Michael, if you'd be interested in And doing any work in the actual conventions, but maybe we should, loosen the wording a little bit.
**Michael He** 47:59 Yeah, sure.
**Liudmila Molkova** 48:21 Let's, let's do this. Let me add a comment here.
And, Let's create an issue.
So I don't forget… oh, I'm sorry.
Erin, you didn't create an issue about it, right?
**Aaron Abbott** 49:02 No, I haven't done it yet.
Perfect.
**Liudmila Molkova** 49:31 Yeah, I'll add labels later.
So you, Michael, you mentioned the chain name, is kind of missing,
**Michael He** 49:41 Yes, for the, let me pull up… I think, in that genai.operation.name, it says, if… there's a value in the list of well-known values, I should add it. I think only invoke agent was there, and I think LaneChain kind of has this concept of, like, chain executions, which is kind of like their linked list model of agent workflow execution.
So, yeah, I don't think, any of the existing values really fit that, so I kind of just added a custom value and called it chain. I'm not sure if that's, what everyone else thinks would make sense as well.
**Liudmila Molkova** 50:21 Does it result in… what attribute name would it have?
**Michael He** 50:24 I would have the, genai.operation.name.
And then also the span name would also be a chain, and then with the, Chain, like, workflow name.
**Liudmila Molkova** 50:41 But the… I see the operation name set is set to invoke agent here.
**Michael He** 50:46 Oh yeah, there should also be a chain as well, somewhere in there.
C.
**Liudmila Molkova** 51:06 Okay, so… I don't see chain, but I see some custom attributes, so I probably will need to talk about it.
Oh… Leave some comments.
**Michael He** 51:19 In the, create chain span on, in the span manager on line 119, that's, where I have the span image chain as a custom value.
**Liudmila Molkova** 51:32 119…
**Michael He** 51:42 -Oh.
in the, spanmanager.py file.
**Liudmila Molkova** 51:49 Oh.
Oh, so you're setting the custom spend name, but you are not… Setting those as attributes.
Okay, well… That's something we'll need to talk about more, so we… Want to make sure that the spend name contains only the things that are available in the structured form and attributes.
And, I think the chain name… Maybe a better candidate for the… than the agent name.
So… I think we need to… Figure out how to represent these things in semantic conventions.
first.
**Michael He** 52:52 Yeah, I think it makes sense. I was a little iffy on this part.
**Liudmila Molkova** 53:05 Okay, I'll take a look at the PR, I'll try to come up maybe with some suggestions. I'm not completely confident I will be able to do it, but I'll try to do it today or tomorrow.
And, let's… Try to figure it out.
**Michael He** 53:25 Okay, sure, sounds good. Thank you so much.
**Liudmila Molkova** 53:28 Thank you.
Okay, so the last, but not the least, and we only have 8 minutes for this, is blob and file parts.
I think we have some good discussion on the PR.
But I wonder if we… if we can… If you need any time, synchronous time to discuss things.
**Aaron Abbott** 54:11 Yeah, I think that might be good.
I think… so there's a lot of discussion I wasn't super sure where you stand on it, Alex, with the current things, but I'm thinking maybe to just cut, like, PDFs from the scope of this PR.
So… like, what will… I don't know if it's explicitly scoped here, but I kind of like the proposal with image, video, audio, which are pretty well defined.
But we can leave out PDF or document for now.
**Alex Hall** 54:52 I guess, yeah, I'll just leave them out for now. I think that if you know somehow that it's a PDF, you should have mine type application PDF.
I don't know what it means to know that it's a document that may or may not be a PDF.
**Aaron Abbott** 55:06 Yeah, again, so I think… I think Anthropic… You can do text slash part.
as a quote-unquote document. So, for that one, again, I think the mime type, they could just set.
**Alex Hall** 55:18 Yeah, okay, so if the type, the top-level part type, is image, audio, video, or something, that doesn't really leave room for Other files, and as we create types for each one.
Whereas if the type was… You know, file, blob, or even more generically, media.
Then we can have… arbitrary types of media inside, and even leave the media type out, but provide a MIME type if we have one.
**Aaron Abbott** 55:50 Yeah, so I think that's pretty much what Lamila proposed, right?
**Liudmila Molkova** 55:57 Yeah, pretty much, yeah.
**Aaron Abbott** 56:00 So not use it on the part type. Instead, we'll keep, like, file and blob.
Which will have the like, whichever format the thing is stored in, either URI or Base64, and then we'll have some subtype key for… Image, video, audio.
**Alex Hall** 56:20 Yeah, because sometimes it sounds like we know that it's an image, but we don't know what the mind type is.
**Aaron Abbott** 56:26 Yep.
So, again, like, naming becomes kind of hard.
So I guess I can leave some proposals, but the biggest problem is media underscore type is actually… the, like, technical name for MimeType.
**Liudmila Molkova** 56:42 Hmm.
**Aaron Abbott** 56:43 And within that, there's type and subtype. So the thing before the slash is the type, the thing after is the subtype.
So that pretty much leaves us with not a lot of good options.
We could… we could just call it, you know, like, media type, and then say this is the… the part before the slash.
Or something like that, but then that kind of forces you to use application for PDF when we do support that, which I think kind of sucks.
So… I don't know, what do you think of, like, modality?
**Alex Hall** 57:17 Yeah.
**Liudmila Molkova** 57:20 Matches the terminology, the domain terminology.
**Alex Hall** 57:24 Very nice.
**Aaron Abbott** 57:28 Okay.
Cool, I think that's… that pretty much would resolve it. I'll… So I'll update to modality, and then I'll make a follow-up issue for file slash PDF, or whatever.
That sounds good.
**Liudmila Molkova** 57:50 Sounds good to me.
It turns out it's complicated, right?
**Aaron Abbott** 57:58 Yeah, and naming is hard.
**Liudmila Molkova** 58:02 Yeah.
Cool, so we have 4 minutes left. I will be happy to return them back to you, unless you have any additional Topics are less thoughts.
Okay, then have a great day, everybody. See you around.
**Aaron Abbott** 58:23 Yep.
**Shuwen Pan** 58:24 Thank you. Thank you.
