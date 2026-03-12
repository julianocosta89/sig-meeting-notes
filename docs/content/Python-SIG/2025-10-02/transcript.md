SIG: Python SIG
Date: 2025-10-02
Duration: 60 minutes
Zoom Recording URL: https://zoom.us/rec/share/OmheNl8UEdKgTgXtZ-ceLIBPTW50NmqeejERDn6NoxzBv9oHjBScIn108p-ZcdTM.CucMtlDfH7BV7KnL
============================================================

## Zoom Recording Transcript

**Riccardo Magliocchetti** 05:48 Hello.
**John Scancella** 05:54 Hello.
**Emídio** 05:57 Okay.
**Riccardo Magliocchetti** 06:29 So, welcome to this week's Python Weber Call.
And… pleaser yourself.
to the notes, what I'm sharing in the chat… And… we're waiting a few more minutes for more people to join.
And if you have any topic, feel free to add them. And please as a member to add the name before the topic, so we know.
Who submitted it, thanks.
**lechen** 07:35 Hello.
**Riccardo Magliocchetti** 07:38 Hey, Latham.
Okay, I think we can start.
Welcome again, everyone.
Hi.
**Nagkumar Arkalgud (Microsoft)** 09:06 I'm Na Kumar, I'm from Microsoft. We're working on a bunch of, Tracing, things.
So, I wanted to bring this pull request that I linked, into a conversation here.
What we are trying to do is add a tracing SDK, so the new GenAI semantic convention which was updated recently, is reflected for agents. Invoke agent span, and the tool calls, and all those things.
data goes through according to the specs, so that's the TLDR.
I'm… on this.
the.
**Riccardo Magliocchetti** 09:59 Okay, thank you.
like, I haven't looked closely at the PR, like, I haven't looked at the PR at all, actually, but, I see there are already some… Comments?
**Nagkumar Arkalgud (Microsoft)** 10:15 Yes, there was one comment which is a little complex for me to understand, given my lack of, like, 100% context, and Especially the last one, where there were 2 or 3 replies.
But yeah… The bigger question to get answered here is that, should this be a separate new package, or are we… can we reuse the OpenAI V2 package, which already exists, the GenAI instrumenters?
**Riccardo Magliocchetti** 10:53 Yeah.
**Aaron Abbott** 10:56 Oh, sorry, Ricardo.
I, I was just gonna say…
**Riccardo Magliocchetti** 11:00 Yeah, that's right.
**Aaron Abbott** 11:03 Yeah, sorry, I was just gonna say, I'm not too familiar with OpenAI agents, but are they in the same package as the OpenAI SDK, or is it, like, a separate dependency?
**Nagkumar Arkalgud (Microsoft)** 11:13 It's a separate one, but the OpenAI agents depend on the OpenAI SDK.
**Aaron Abbott** 11:21 Got it, I see. Ricardo, sorry, wanna go ahead.
**Riccardo Magliocchetti** 11:25 Yeah, or just… Telling this that it is a separate package.
But I don't know…
**Nagkumar Arkalgud (Microsoft)** 11:32 what we are…
**Riccardo Magliocchetti** 11:34 What we wrap our instrument?
Yeah, seems like Alzheimer.
**lechen** 11:41 Well, you still need to create an OpenAI client to utilize, the functionality of OpenAI agents.
I believe, the OpenAI V2 only instruments, like, track completion functionality?
While this instrumentation instruments, like.
Like, talking to an agent, and all the… All the signals and events that come from that.
steady.
**Nagkumar Arkalgud (Microsoft)** 12:13 Yes.
**lechen** 12:13 Nakumar, you can correct me if I'm wrong.
**Nagkumar Arkalgud (Microsoft)** 12:17 Yep, that was perfect.
**lechen** 12:21 Yeah, so they essentially instrument different functionalities. Openai agents still depends on OpenAI.
So However, it still uses the client, but it does seem like the components that it patches are within… OpenAI agents, so it's kind of like the, I think the URL lib to… Requests, kind of.
Oh, sorry, no, it's, one of the HTTP, interactions. It's kind of similar to that.
**Riccardo Magliocchetti** 13:07 So, like, my question is, like, I'm not able to… first thing is, I'm not able to find the actual Functional meters we are patching.
out of.
**lechen** 13:23 Yeah, I think, openAI Agents provides the, Add trace processor API?
Line number… You go down.
In the instrumentation.
9 number 108.
In the, init py file.
**Riccardo Magliocchetti** 13:48 Okay.
I understood that.
**lechen** 13:51 So it's their… like, OpenAI has an API to add This is not the same trace as, like, OpenTelemetry trace. I think they just know concepts of, like.
Being able to generate telemetry and everything.
So they provide this convenience API.
Yeah, I would have to… I haven't looked at it too closely from a functionality point of view, but more from a structure review.
At least from my preliminary findings, it seems, like, okay to be a separate instrumentation, in my opinion.
I just hope that, like, the, The marketing of it doesn't confuse people.
Like, how… how… our naming, like, for V2 confused people, customers back then.
Yeah.
I think the, the… that answer can be quickly found after review, but I think the… the second kind of blocker is, the… the fact that we're using the old events SDK, As part of this implementation.
I think, if you… if you click on the… the… there's a conversation between, I think me, Aaron, and Dylan, talking about whether we should should or shouldn't use the deprecated events SDK, so, I think Dylan is… Pushing the effort for deprecating it, and it might be blocked on that… If we… choose to use the new login SDK, or sorry, login API.
**Dylan Russell** 15:57 For that, I think, I think if you upgrade to the latest API and SDK, you can use the logger.
And, yeah, do logger.emit with a log record, and it should work.
**lechen** 16:18 Right. So we would just have to pin, like, the latest, versions of OpenTelempture API, pretty much.
Nakumar, just for context, you're probably taking this implementation directly from the already existing GenAI instrumentations.
Open telemetry, semantic conventions, like.
have decided to make a push towards deprecating the events API and SDK, and instead just merging that into a a field, Within the log API. So it's simply, we're… we're just… not… trying not to use the Events API SDK for new components now.
So it's just gonna be a… Small API change, that's pretty much it.
**Nagkumar Arkalgud (Microsoft)** 17:09 Sounds good.
**lechen** 17:11 Yeah.
And I think, Dylan, I think we also have come to a decision for your Or event CPA deprecation? Or was it, Ricardo's? I can't remember.
But yeah, I think we can move forward with that, with the emit overload and everything.
If everyone's in agreement.
**Dylan Russell** 17:38 Yep.
**Riccardo Magliocchetti** 17:41 Yeah.
**Dylan Russell** 17:41 I think we merged it, right?
**Riccardo Magliocchetti** 17:42 Yeah, I merged yesterday, they meet over.
**lechen** 17:45 Oh, nice time.
**Riccardo Magliocchetti** 17:47 Like, everyone approved that, so…
**lechen** 17:52 Awesome, awesome.
I think we're… The good headwinds for… Logging SDK stability.
**Riccardo Magliocchetti** 18:04 Yep.
Like, I have two comments on these two issues. The first one… is on… regarding a separate package, I think we don't have any other option.
Because otherwise, like… It will be hard to define the… the version of the library U instrument?
**lechen** 18:28 Yeah, it's gonna mess up auto-instrumentation, for sure.
**Riccardo Magliocchetti** 18:32 And then…
**lechen** 18:33 Thanks.
**Riccardo Magliocchetti** 18:35 But, like, it's already a separate package, so it's fine. And, for the events, yeah, I agree that probably we should just go through logs, Another baseline, a recent baseline.
**lechen** 18:48 Nice.
So yeah, I guess we're just looking for more reviews.
for this year.
Are you sorry, Aaron, you have your hand up?
**Aaron Abbott** 19:00 Yeah, yeah. So, for example, for, like, that telemetry… a GenAI semantic processor that converts whatever If I understand right, that converts whatever OpenAI's internal tracing data model is into the OTAL one? Sorry.
**Nagkumar Arkalgud (Microsoft)** 19:19 Yes.
**Aaron Abbott** 19:21 Okay.
maybe just because the PR's a little big, do you think some of that could be moved to, like, a later PR, so… You know, usually we do, like.
a boilerplate… I mean, it's good to see the kind of end state.
But, you know, we could split this into maybe, like, a boilerplate PR, which just has… you know.
License files, pipe project files, blah blah blah.
And then another PR that adds instrumentation, and then that seems like a completely separate thing, the, semantic processor.
Does that seem like a… doable thing. Just split it up into maybe 3 PRs.
**Nagkumar Arkalgud (Microsoft)** 19:59 Yeah, I can do that.
**Sergey Sergeev** 20:06 One more question, so it looks like there is a list of attributes just hard-coded in In the events.py.
So, where are we with just using semantic conventions from the package?
Why do we have to have this list here?
**lechen** 20:34 Yeah, I think I left a comment on that, too.
**Nagkumar Arkalgud (Microsoft)** 20:40 Yeah, I can, pull them from somewhere else.
That's what, find the right place to get those lists, get those attributes from.
**lechen** 20:53 Yeah, I think, one more thing regarding constants, I think you have a bunch of… Environment variables that, I asked about, I might have missed a discussion for this, but, like, was this… Defined anywhere, or is this just something that's being chosen by you that you think is appropriate?
**Nagkumar Arkalgud (Microsoft)** 21:15 I just added them, but I've removed them now.
Oh, okay. They were never discussed, so, like… I just added them. Things like, you know, capture stuff or don't capture stuff, but…
**lechen** 21:27 Yeah, yeah. Yeah, I think it'd be great to, let's get the basic functionality out. I think it's a pattern for us to kind of Follow what the community is doing, and what other languages are doing, and not introduce anything that could possibly conflict.
Without the semantic conventions. But if there's a need for, like.
custom language-specific environment variables. That could be a separate discussion, but… Yeah, open to that.
**Nagkumar Arkalgud (Microsoft)** 21:58 That's good. Thank you.
**lechen** 22:01 Yeah, thanks for this PR, man. We'll take a look at it.
**Riccardo Magliocchetti** 22:15 Okay.
**lechen** 22:16 Ricardo, the next one is, the one that we just merged, so thank you.
**Riccardo Magliocchetti** 22:21 Okay, so we can skip that.
The next topic is from me, and, like, speaking of Gen AI instrumentation, I was converting, an out of, three, GINA instrumentation to use the… the log API instead of using the event one.
And what I found is that, We print a lot of warnings every time we emit, A log record.
And so, like, I created this PR, which is, like, trivial.
That is, instead of printing every time.
Veterice ID, span ID, or trace flags used.
Only print the warning if context is not used.
because the conversion from API log record full towards the Kellogg record, pass, all the parameters.
Because otherwise, the current, instrumentation using the event API will brack otherwise.
So, like, once we move everyone out of Event API, probably we can revise this, but… Like, seem trivial, You know, brings enough value for me to all.
To take a look at that.
So please take a look.
Then, next topic is from Kit.
Jenai IoT's PR review.
**Keith Decker** 24:06 Yep, looking for more reviews on… So… Janai's inference type. We've got Dawn and Aaron, I believe, have already looked at it. I think, Aaron, you said you were gonna take a look Tuesday.
And just… need more ice?
**Aaron Abbott** 24:28 Okay, yeah.
Do you mind sending a message in the Slack channel, just with a link to it?
**Keith Decker** 24:36 Sure.
**Aaron Abbott** 24:39 Cool.
Yeah, thank you.
**Riccardo Magliocchetti** 24:53 Okay, by the way, let me add a generic comment on these GenAI IPRs.
He's up?
I don't maintainer that doesn't have much time to look at GenAI stuff these days.
I would appreciate if, people that are working on instrumentation to review, other instrumentation PR.
So maybe we can learn from each other, and also, like, We can have more eyes.
not rely on, you know, general AI.
approvers or photo maintainers, like, because, like.
We have a list of Gen A approvers, but not many of them are very active in reviewing, so… Every help is, really appreciated, thank you.
**Sergey Sergeev** 25:42 Yeah, this is a problem. A lot of people who work on GenAI stuff are kind of new to OpenTelemetry Project overall as well, so we cannot… A bruvoy.
Just… we need more help, brother help, from a bigger group.
Just one standard, see if we're doing something weird, and so on.
**Riccardo Magliocchetti** 26:04 What?
It's enough for me, like, really, it's… It's really helpful. So, if you have time, please do, again.
Thanks.
**Aaron Abbott** 26:15 Yeah, yeah, I think just one more thing to that effect is, like.
Working up to being an approver.
It's, it's also helpful, so reviewing You know, stuff.
you know, other GenAIPRs that maybe you're not interested in, but also just, like, You know, you could… you could help out in approving or reviewing.
Just, like, other Python SDK or API, issues.
**Sergey Sergeev** 26:44 Definitely makes sense.
Good idea.
**Riccardo Magliocchetti** 26:58 Okay, so this… What's the last topic for today?
Any last meso to one.
Or any comments?
**Dylan Russell** 27:13 I actually have a small PR.
We could… And, let me post it, sorry, give me a sec. It's in OpenSelemetry Python.
Yeah, so this is to make the auth… package that I… Recently, I had to contribib, like, an optional dependency on the… the OTLP exporters.
So if someone wanted to, like, send telemetry to, like.
GCP, they would be able to say, like, pip install… OTLP exporter, and then that… Like, auth provider thing.
So yeah, Sean, do you have people's thoughts on… If that sounds reasonable.
**Aaron Abbott** 28:44 Yeah, I think this is kind of… I like it, because it's nice for the installation. It's definitely, obviously, a new thing, just looking at the PR. Yeah, I don't think we've done this, Any… anywhere else, but just, like, in the Python ecosystem, it's definitely a common pattern.
I don't know, what do you think, Ricardo and Leighton?
God.
We obviously don't want to have, like, a thousand things here.
**lechen** 29:13 Yeah, I think installation purposes, it makes it pretty simple. I don't mind this.
**Riccardo Magliocchetti** 29:19 Yeah, same. I don't see any problem with that.
**Dylan Russell** 29:28 Cool.
Maybe we should wait for a release of the… the… contribute now.
**lechen** 29:37 Oh, just, I kind of maybe I've been out of the loop a little bit, what does the credential provider do exactly?
**Dylan Russell** 29:45 So, for auto instrumentation, It will… inject… channel credentials into the gRPC OTLP exporter, and… A… a session into the HTTP one.
So that, like, the old TLP exporters have auth stuff.
like… Pre-configured.
Hmm.
**lechen** 30:21 Is there a reason why that only works for auto-instrumentation?
**Dylan Russell** 30:26 It's… yeah, so it'd also work for manual.
**lechen** 30:31 Oh, nice.
**Dylan Russell** 30:32 Yeah.
**lechen** 30:33 No.
Let's see… Okay, yeah, that sounds good. We… we do have the… I'm not super, clear on how the install optional dependencies functionality works. We do have that, like, pip install, OpenTelemetry, OTLP exporters, like, generic package.
Would I be able to put, like, a bracket GCP in there, and would it auto-install the optional dependencies if it's, like, a secondary dependency?
Just, just, just something to maybe…
**Dylan Russell** 31:24 Yeah.
**lechen** 31:25 test out. I don't know the behavior, yeah.
**Dylan Russell** 31:28 Yeah.
Aaron's saying no.
**lechen** 31:32 Oh, it doesn't.
**Aaron Abbott** 31:34 Yeah, I don't think so. I think… I think the extras… slash optional dependencies, they only apply directly to the package that the dependency is… optional dependency is defined in.
Yeah.
**lechen** 31:47 That would make sense. It's like, you don't want to be installing some random stuff you don't know about.
I think that's fine, though. It's, like, just something I was curious about.
Okay, cool, thanks.
**Sergey Sergeev** 32:10 Okay.
If we don't have any topics in the group.
is willing to hang out for, like, 5 more minutes. Just wanted to get some immediate feedback on that, Utugen AI.
And the whole idea of, Puagambo… It's telemetry of waivers.
And separates an instrumentation from telemetry producers.
Can I add this topic quickly?
**Riccardo Magliocchetti** 32:44 Shu, do you want to share the screen, maybe?
**Sergey Sergeev** 32:47 Yes, give me a second… Again, I really appreciate help from Dune and Aaron already on this topic.
But again, it's good to quickly… Vintage this idea with the broader group.
And… The whole idea is that, right now we have semantic conventions which are behind of what some open source libraries, including TraceWhoop, are doing with telemetry.
And we have a set of semantic conventions, Which is, smaller scope, what, attributes set by tracewoop memory. So now, we have, the trace hoop, instrumentations.
Oops, sorry.
a lot of them, and they produce, basically, a tracewoop telemet, which is mostly semantic convention, plus some tracewoop attributes.
Mia.
Show an example… What was that telemetry?
So, in general, it will be mostly semantic conventions, but occasionally it will be some trace hoop attributes, which not yet defined in semantic conventions.
So, the whole idea, of, OTHEN AI that we separate instrumentation from, telemedic data types. So, for example, we introduce something like OM invocation object, which can be reported by instrumentation, let's say, blank chain. In Wank chain instrumentation, we don't create a span, a metric, and event. Instead, we create this LM invocation data type coming from, GenAA types.
And we put, named attributes for… named arguments for those attributes defined in semantic convention. Everything else passed as a dictionary, request response or context.
From instrumentation, and the idea is that we can have, Basically, a semantic convention, emitter.
Which will produce a telemet and semantic convention form, or we can have pluggable traceable perimeter, which Can use entry point, group, to register itself if a customer basically installs, it, to… if a customer installs this package, this is just a POC, so it doesn't have a particular… it's a separate package, but we know we can do it. So, first of all, what do you think about this idea? Because I heard, Suggestions, like, why can't you just, install something like, span… well, it's telemetry processor, and just… Change the telemetry which is already produced.
So, I wanted to hear from this group with this approach, because it's probably not what this group was doing before.
But specifically, does it make sense for the broader group, If we do it this way.
Oops.
With mute.
show, for example, how… This utility function will be used from LAMP chain instrumentation, for example.
So, Ian… in, WANKChain instrumentation, so we have that callback handler, which we register to WankChain. So here, instead of, basically, creating telemetry.
Here, we will create that, UTU LM invocation, where we, pass, basically, all the needed information As named, arguments to this, unnamed fields on this data… class, and attributes are passed as a dictionary here. So, attributes is something which traceable emitter Can extract text information.
But, for… Everything with the named fields, it will be set to semantic conventions by standard emitter.
So this way, again, we just, We can allow, TraceWhoop to use to move their instrumentation into OpenTelemet, Python content.
And just maintain that mapping for extra… Extra attributes which are not yet defined.
Any feedback so far?
**lechen** 39:36 Sorry, can you repeat the last part, what you just said, how it interacts with Traceloop?
**Sergey Sergeev** 39:41 Yeah, the trace loop, again, so… oh, I'm on vacation, so if we have, in the Python country, we will have just, one, one emitter by default, which will, set.
Those fields to semantic convention attributes.
And this is it, and ignore the extra, details for trace hoop. So, again, similarly how we… Sorry, give me a second.
again, in semantic convention, we only care about those GenAI types, and for LM, Invocation.
yeah, they need to improve it, so it's a little bit messy, but basically here, for the start, for everyone on vacation, We can, basically put, semantic convention attributes using a helper function, and this is where we create, basically, a span from LM invocation data type.
So what's different in trace hoop? It will be this, and plus some of the trace hoop, attributes.
So again, it's, above the same.
And, we need to instruct, basically, from invocation attributes, if it was a terrace hoop instrumentation, we can just filter on those trace hoop, but, the goal is to change it, basically, to be, not vendor-specific, so it will be something like extra attribute, or whatever the instrumentation can set it to. But, for example, callback name, Maybe, an extra field on that attribute.
And the whole idea is that we can, later… When we have that defined in semantic convention, we can move it to the named field of LM invocation from the attribute's key-value dictionary.
In this way, we can both support third-party ahead of semantic convention, telemetry emitters.
And the standard semantic convention emitter, which will be… a limited, Set of attributes we set.
**lechen** 42:58 What?
Why… is there an interest to support third-party attributes?
**Sergey Sergeev** 43:06 Yes, specifically from TraceHub, because, the challenge, so they donate their instrumentation.
We can move for 26 of them, but the challenge, those instrumentations will report telemet with a lot of vendor-specific trace-woop attributes, which are not yet defined in semantic convention.
So, we can build a new one just for semantic convention in OpenTelemetry Python Contrib.
But, it will never swim.
**lechen** 43:39 Right.
**Sergey Sergeev** 43:39 Trace Hubensumentation.
To use that, because it will always be.
**lechen** 43:44 Very interesting.
It's interesting that you brought this up. Have you reached out to the TraceLoop people?
**Sergey Sergeev** 43:49 We chatted with a near… about it.
**lechen** 43:54 Oh, interesting. Yeah, this might be… Pretty good. I've been kind of stepping away from Gen AI recently, so I haven't been caught up with the latest developments. Aaron Ricardo, you might have more context, but where were we in terms of, like, the migration of, like.
and donation of the instrumentations from TraceLoop to… To OpenTelemetry.
Was there any developments in the past few months?
**Aaron Abbott** 44:22 I don't know about the past few months, except that we've, we've had, like, agreement to keep doing the split versioning thing, instead of doing, like, the OpenAI V2. So, instead, we'll publish to a different version number, and we can kind of have shared ownership of these packages, which, Which is, like, the intent that eventually Tracelib would move to just the controversions, the 2.X ones.
I… last time I talked with TraceLoop, I didn't know that they were interested in keeping, like, backward compatibility like this.
So, I… I thought… I thought they were… they were, like, you know.
On board with moving to the conventions as we're defining them in semantic conventions.
**Sergey Sergeev** 45:08 Yeah, it's, yeah, the challenge is, that, The problem, we may be not above Ever to catch up here, because semantic conventions take a lot of time to agree, and etc, and… Specifically, it's… it's a long road, so… and we were helping, we were trying to help with, migrating TraceWoop, and this is what we discovered, the whole idea of that U2 function.
on top of additional, LM as a GH evaluations on instrumentation side, but, on top of it, what we realized, so, how can we… keep, so, how can we avoid that, Situation when we never, reach The piracy with semantic conventions.
And, what do you think about this, approach, where we can just… maintain background compatibility with what TraceWhoop has now.
move the two swoop instrumentation, which will be separated from, actual telemetes. So, in this case, We can just, maintain, as community all the instrumentations in Python country, And same, we can maintain, semantic convention emitters, so we will make sure it's just semantic conventions. And finally, we will let,
**Aaron Abbott** 46:50 We will create that.
**Sergey Sergeev** 46:53 Emitter for trace hoop, which will be… Which will include some set of attributes which is not yet defined in semantic convection.
just, again, my goal is just to make sure everybody first understands the idea, and second, to get some feedback. And I know that we are still working on cleaner POC than what I just demoed.
To give a better end-to-end with the separate package.
Example of how it can be used.
**lechen** 47:36 I think as the first, use case, I think we need TraceLoop's direct buy-in if we want to support this.
**Sergey Sergeev** 47:44 At least some representative from them.
**lechen** 47:46 We don't want to add vendor-specific Stuff.
and have… like, no one support this, like, in the future, right? If this is the case, then… Any trace loop attributes that get added, like, we constantly have to add this to the… this emitter, I guess, right?
**Sergey Sergeev** 48:07 Yeah, the emitter will be a separate package living on Trace website.
Basically, and, and… So, first thing, what we will need to do when we move… so, once we have the types developed in the UTL function, what we can do, we can basically switch the instrumentation.
**lechen** 48:29 Yeah.
**Sergey Sergeev** 48:30 buy one from emitting jest. Yeah, let me be very clear.
**lechen** 48:33 Makes total sense, makes total sense, yeah. Similarly, like, how any other can create their own emitters. I'm just saying, like, in order for us to introduce this pattern.
We want to have a… like, a buy-in from TraceLoop first, at least.
**Sergey Sergeev** 48:50 Yeah, it might make sense. I'll try to bring Knir to the next sync.
And, second, for Splunk, for example, we also need some specially designed television results.
Schema, which, we proposed to the community, but it's a little bit specific to our data store, so we want evaluation results to be combined with some of the extended APM attributes and all the evaluation results on a single log record.
So, again, I don't think we… it makes sense for a community to standardize this schema. It's a little bit vendor-specific, and I think it will be more use cases like that. So, for us, it will be super useful to be able to just… to create an emitter for a specific gen AI type.
So, we want to convert evaluation result to a different schema. So, we definitely are one of the use cases for this.
And just in general, it's… it's… I think it's a challenge for everybody, so… This is why we have, separate, messages, GenAI messages, can be attribute on a span, or… GenAI messages can be events, so… It's just that never-ending story, which was haunting the LMC for months. And Ludmilo even joked that we need to rename the channel into Span or Events for messengers. So, I think…
**lechen** 50:47 Yeah, if you could just, yeah, if you could just, like, maybe bring Nir on, for next meeting, to at least discuss the Trace Loop,
**Sergey Sergeev** 50:55 Okay.
**lechen** 50:56 Use case? Great, thanks. Yeah.
Another thing… sorry, Sergey, is that… was that it? I have one more topic, actually, that brought up.
**Sergey Sergeev** 51:05 No, no, no, please go ahead. I think, yeah, I wanted to hear the feedback, because it's a little bit different from what OpenClemati community was doing, and, just the concepts I knew, so… I want to hear more feedback on it.
**lechen** 51:30 Yeah, at least for the… the invocation kind of pattern, yeah, I don't think we will… commit to it until we have a, like, clear desire from TraceLoop to Because our understanding of the migration, story was different until you brought this up.
We have to get.
**Sergey Sergeev** 51:54 I think I understand the desire to get to simantic convention. Is it achievable? It's… and I… Just don't see it's happening, and we don't get enough, adoption of, Python control, how can we get there? I think it's one of the options.
How to solve it.
**lechen** 52:22 Right.
Right, so one more thing I want to bring up.
So, we actually saw… I actually saw, while you were scrolling, Sergey, that the OpenAI agents instrumentation actually already exists in Traceloop. So this is, like, another kind of, like, you know, we've always had this kind of problem where they're developing their own stuff right now.
I think?
at least what Aaron was saying, or how we left off, we're going to be doing the, kind of.
major version kind of differentiation for now, Nakamar.
So, you can just continue… I think the… the recommendation is just continue with your, implementation.
But just change the version so that it's, like, the next major version, if that makes sense. We can talk offline if it's, if you want more context about that.
**Sergey Sergeev** 53:26 Yeah, and we are doing the same with, WANK chain as well, so we're building just Wangk chain with creating telemetry directly, but at the same time, we have a prototype, because we are working, full types definition on UTL gen AI required, but just think about it, that, it's the same UTO GNEI type for agent invocation for LLM invocation. Once we switch, we will be able to both build way faster new instrumentations, and second.
Hopefully we can just, at some point, bring more, instrumentation from TraceWoop.
And to get, the adoption of it.
Yeah, I agree, we need Mir, or somebody from TraceHoop.
To commit… to confirm.
**lechen** 54:30 Makes sense.
Cool, yeah, that's everything for me.
**Sergey Sergeev** 54:36 And by the way, I am so open to any other ideas, so if we can get there.
Sooner than that, in any different ways, I will be super happy.
**Riccardo Magliocchetti** 54:55 Okay, thank you. I see when Dylan added an FOI for us.
**Dylan Russell** 55:04 Yeah, we're planning to move the GCP resource detector up into Contrib.
Choice.
There are, like, some already there, right? So I think… should be… Straightforward.
**Riccardo Magliocchetti** 55:22 Yes, thank you.
**lechen** 55:24 Yeah, there's some… there's some reason effective with this race, so go for it.
**Dylan Russell** 55:29 Cool. Yeah.
Alright.
**Riccardo Magliocchetti** 55:36 Okay, I think these were the topic for today.
So… Thank you, everyone.
And… see you next week's… next week?
**lechen** 55:49 That's real.
