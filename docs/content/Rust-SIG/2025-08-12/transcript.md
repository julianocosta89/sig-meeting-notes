SIG: Rust SIG
Date: 2025-08-12
Duration: 87 minutes
============================================================

## Zoom Recording Transcript

**Zhongyang** 02:28 Hey, CJ. Morning.
**Cijo Thomas (Microsoft)** 02:30 Hey, good morning. How are you?
**Zhongyang** 02:33 Being good.
I think we missed each other in…
In those, weekly syncs a lot.
**Cijo Thomas (Microsoft)** 02:40 Yeah, I think, I joined, like, last week, but before that, yeah, I was missing for some time.
Yeah, we don't have, like, much things going on. I… the only thing which I'm actively tracking, or there are only two things, one is working on distributed tracing.
And then, SCOT is helping with OTLP exporter stabilization, that's…
pretty much it. I don't think we are actively working on anything else.
Yeah, it's slow progress, but at least it's making, some progress every week, like OTLB is improving. Hopefully, we should be able to get it to the table soon.
**Zhongyang** 03:19 I see, there's, …
212… Triage maybe your active issues.
**Cijo Thomas (Microsoft)** 03:32 Yeah, let me share my screen. One second…
Yes, Court just messaged about this one, so still in draft, but that's an important step towards OTLP stabilization.
There are a few small PRs…
I think it may be okay to go over this one. I opened it, like, a week ago.
Let me see… yeah, put it as, like, work in progress. It's mostly…
making sure we have a clear direction for end users, like, what should they do for logs, metrics, and tricks. I mean, for metrics, there is no confusion, it's just OpenTelemetry API all the way.
So this was opened specifically in the context of the bridge between Tokyo and Tokyo Tracing and us.
So… the logs one should be…
I mean, only intent here is we are conveying, making an explicit thing. It's already mentioned in the docs, but we are making it, again, explicit that the bridge is not for…
end users.
It's simply, access to…
people write bridges, so it's not a replacement for tracing log or any other logging solution. That's the main message, and second is, like, we want to make some recommendation, either tracing out log or something else, and due to the fact that we already have
bridge for tracing, and tracing has a support for, capturing, like, low crate things. Put, like, use tracing crate, like, one-liner recommendation.
And these are, like, details, like, name and target.
We recommend people to explicitly provide it. I think I'm still, like, figuring out whether we should recommend underscore, because I read earlier today from OpenTelemetry's own guidelines that
It should be dot separated rather than underscores, so I'll need to, like, work on those things, but generally, we want people to provide name and target instead of relying on the defaults which tracing provides.
That's the only recommendation for, like, logs. It's expected to be, like, very, simple and lightweight.
For traces, things are… Obviously, more complicated, …
main recommendation is EIB. I mean, our…
TLDR version, or, like, recommendation for summer new is, like, we just recommend OpenTelemetry API for distributed traces.
It supports everything from the spec, so this should be obvious, but we were forced to list it.
Due to the unusual nature of our report.
And then… Or… events or point-in-time things, we are reiterating the
message from the log statement, like, we are asking people, like, use tracing info, event macros.
So this is, like, so far is, like, existing things, and then I'm talking about something which do not exist today, which is, what if someone wants to entrance logs with extra context, and they can use, like, span macros to do that, but as of today, it's…
going to be broken, because there is no way we'll enrich the logs with that, but once we add a capability to the appender itself to extract span attributes and attest them to each individual logs.
So the… this is more like a…
futuristic thing, I think. I mentioned it somewhere, yeah, I think I…
Should have mentioned that. Will be enhanced, yeah. Should maybe make it very clear that this is a capability that don't exist today.
Now, there is a….
**Zhongyang** 07:44 Don't mention it if it's not exists today.
**Cijo Thomas (Microsoft)** 07:47 Sorry, could you repeat?
**Zhongyang** 07:49 Maybe just don't mention it if it does not exist today, and look at it.
**Cijo Thomas (Microsoft)** 07:53 Yeah, this is only to set the direction, like, I… that's why I put it… that entire document as work in progress. Because, yeah, once we have that feature, I want to make sure, like, the maintainers and approvers in the community
we at least have to agree within each other, before we actually work on such feature. So this is just to make sure we all agree on the direction, and then we can go about implementing. Like, implementing this shouldn't be, like, that hard, like, it's…
It's just that we need to first agree that that's the right thing to do, and then we can go ahead and implement, yeah.
And then, this is the most controversial or most challenging part, like, what if I use, like, span macros from tracing, and then I still want to see them as spans itself, in Jaeger or other tools?
So this is where, like, our hands are tied, like, we don't offer anything from OpenTelement for itself. We point them to a…
third-party bridge Oh.
And then that links to it. And then…
This should, like, take care of most of the aspects, like, for example, if you create spans this way, and use the Tracing OpenTelemetry bridge, they appear as normal spans, but there are some limitations, which I believe, like, we should really be, coding them out here.
It has no ability to set remote parent, span kind, span links. I think there are a few other things, like scope and other things, but again, these are the most critical ones.
… And then, this is even more challenging, like… So, these… these are, like, limitations of tracing itself, and…
the Tracing Open Elementary Bridge offered, like, some…
Extensions with some magic strings to… work around these limitations.
that's the part which I'm not very sure, like, what should our association be. Like, we can completely, like, not mention anything about it, or we can make a recommendation about, like, avoiding that, because if a library order or a application order wants to instrument, and they are going to bet on
the bridge and the extension from it, then it's not following any standard. It's not open telemetry standard, it's not tracing either.
So it's, there is no spec backing tracing OpenTelemetry, so it could be putting them in trouble for long term.
So that's why I'm not…
very comfortable recommending it. In fact, I would prefer if we make a recommendation against using that, and this is a place where I want, like, everyone to chime in with their opinion. Or another option is we can completely
avoid any mention of tracing open telemetry. That would be another option, because just like every other repo, we can only worry about things we support, we don't need to worry about anything else, but due to the historical reasons, many people were using it, and the fact that our repo did some special casing to support
pressing open telemetry, it feels like we should be mentioning something, but that's when things get tricky.
Yeah, so this is what, like, everyone, like, I recommend, like, go ahead and read it, and, like, criticize it, support it, like, feel free to add comments, or we can discuss in the subsequent meetings.
And then there is a small section at the end, which is…
This is a place where
I believe people can use either OpenTelemetry or Tracing Spans.
without any limitations, which is specifically creating internal spans, which is to just wrap a… in proc work, they consider it important enough to be worthy of creating a span out of it.
So in those cases, like, they can either use, like, OpenTelemetry API called an internal span, or they can use the tracing span.
In this case, they're not going to be affected by any of the limitations, because it's an internal span.
So there is no question of, like, remote parent, it's in-proc internal span. There is no need of spanking, it's all, like, defaulting to internal. And usually for such internal span, there is no question of links either. It's usually for producer-consumer spans.
So in those cases, like, it's okay to create spans either way. The bridge will take care of proper activation.
Again, like, this is something we can completely avoid if you want, but I feel like this is a very good strength of
tracing, like, it's very easy to, represent and in proc internal span via tracing. We could make OpenTelemetry also for, like, such macros to make it easy, but at this stage, most people are comfortable this way.
Yeah, so I'm just mentioning it again, it's up to us to decide whether we even want to mention that.
The Rusty's more like… …
How to mitigate the pain if people are not happy with 4.
Because 4 is basically saying, like, use…
Or, sorry, like, 192. Like, we are basically asking people to use our own API, not the tracing one.
… We kind of, like… Giving them a workaround, because most likely, people were using
Manual spans for edge spans, which are either
at the receiving side of a server, or the client span for HTTP client or GRPC client. This should be very rare, because once we have instrumentation libraries, we already have for Actix and Tower. We don't have anything for
gRPC, I think, …
But once you have that instrumentation library, which is the case for, like, every other OpenTelemetry clients, like .NET or Java or any other language.
Then, it's very, very…
rare for a inducer to manually create those kinds. It'll be already automatically created by those instrumentation libraries, and they take care of the, context propagation, like, remote parent, propagating the headers, all those things. So, most likely, like, one… again, this is also future-looking, because we don't have that many instrumentation libraries.
Once we have that, like, most likely people would never need to create a span by hand.
accept the internal spans to do some important work, which they can use, like, either APIs with the same interest result.
**Zhongyang** 14:06 I mean…
even need instrument library for this, right? If you are… if you're gonna set up some kind of, …
Network proxy going along with your application, then you can do it in the…
on the proxy level, that's the… if I have Envoy set up.
**Cijo Thomas (Microsoft)** 14:23 Oh, we cannot assume people are using any of those things, like, that will solve it for a specific scenario if they are using those things, but…
We cannot assume that everyone is using that, but instrumentation Library is going to work for old scenarios, as long as you are using the
instrumented library, be it Axum or, like, whatever, like, tower, middleware, whatever is the library we are using, or the users are using, and if there is an instrumentation library for it, then it should work, no matter how they deploy their application.
That's why this is more universally applicable than, like, setting up proxies or doing something with NVOE and Istio kind of things to generate spans automatically.
Or, again, propagation.
**Zhongyang** 15:08 Yeah, that's fair, but I guess if you… what I'm trying to say, if you already have one voice set up, it should be pretty easy to just wire up.
**Cijo Thomas (Microsoft)** 15:14 Yeah, I think those are customers who don't really care about instrumenting it from the application, right? For them, they don't really care about anyway, like, OpenTelemetry APIs, because they are anyway doing it from out-of-proc mechanisms.
I think Lilith also explored the eBPF idea. Hey, Lilith, like, can you, like, give some idea, like, is it possible that once we have it, I know we don't have it, but once the eBPF-based solution gets funded and worked on, that should take care of
Producing spans automatically, like, without user having to ever touch it.
**lalit** 15:51 Oh, yeah, yeah, that's… that would be the responsibility of…
eBPF layer to create the spans. So, so, so no changes in application. It's kind of auto-instrumenting.
to get approval.
**Cijo Thomas (Microsoft)** 16:03 Yeah, I mean, most other languages, some of the other languages have auto-instrumentations. I think Java and .NET use, like, some language-specific mechanism to instrument, but eBPF… eBPF would be more, like, language agnostic, but it's somewhat OS-specific.
Yeah, I think we can mention something like that, like, in some future date, when eBPF-based technology
matures, we might be able to, recommend that to the users. Because anyway, this document has a lot of
Future-looking statement, so no harm mentioning that.
Let's wait for Ladith to finish his talk in the Rustconf, which is next month, right?
Hey, Yongyang, I think you probably don't know, like, Lilith is giving a talk on cross-const…
Next month, I bought EBPF to instrumentalist applications.
**lalit** 16:50 Yeah, understood.
**Zhongyang** 16:53 Westcon, or….
**Cijo Thomas (Microsoft)** 16:56 Rusconf, right? It's called Rusconf, the one in Seattle, next month.
Yeah, I think it's RushConf itself.
Not the opportunity.
**lalit** 17:06 Rest, yeah, REST configure.
**Cijo Thomas (Microsoft)** 17:08 This conflict, yeah, yeah.
**Zhongyang** 17:10 I didn't know it's, it's in Seattle this year.
**Cijo Thomas (Microsoft)** 17:13 Yes, oh yeah, you didn't do that, okay. I think I mentioned it in one of the Slack conversations, but yeah, maybe I posted in a different place, yeah.
Okay, yeah, so these are, like, some more, like, setting the directions. I mean, a lot of these are, like, feature-looking, so…
please take a look, like, see if anything look old. Like, completely, I understand that this is not the ideal state. In fact, no other language has such a need to write this document. It's very special for us because we want to, like, make sure inducers are given, like, enough
document and guidance, when they want to do their instrumentation. So, yeah, we have to do it. It's a question of, like, how much we touch areas which we don't directly own. Yeah. Once we have, like, reasonable confidence, then we can ask, like, others to comment on it. I have only asked, like.
David, Tracy, Mindy, and I haven't asked anyone from
pressing OpenTelemetry itself yet, but let's give another week or two, and then we can ask for more feedback from them.
Alright, yeah, let's just look at open… any other open PRs. This is draft, this is Copilot instructions created by Copilot.
Symbol peers, … I think this is also approved, like, very minor things.
This one is a Copilot PR, I didn't have time to review it. This one looks like it's approved. Oh, okay.
We're available….
**Zhongyang** 18:45 confused.
**Cijo Thomas (Microsoft)** 18:46 Oh, okay. Oh, we didn't have to….
**Zhongyang** 18:49 Yeah.
**Cijo Thomas (Microsoft)** 18:50 Yeah, because they had made some mistakes in the… MSRV earlier.
**Zhongyang** 18:56 Oh, the wine, the tomo file.
**Cijo Thomas (Microsoft)** 18:58 Yeah. No, no, like, the Tonic folks, they bumped MSRV to, like, very, very new version in .14, and they reverted in 0.14.1, so I… okay, sorry, I…
It's pretty… You see, no? Because…
When it occurred, like, bumping MSRV, then we had to, like, make a more conscious decision, but this looks like a typical update. There are some breaking changes which seem to be taken care of. I believe the build is already passing.
Oh, perfect. Oh, yeah. Oh, you, you uploaded, like, very recently. Thank you.
Okay.
There are, like, old PRs, I don't think we need to….
**Zhongyang** 19:37 go over it? Oh, I want to, like, go over….
**Cijo Thomas (Microsoft)** 19:40 This one, because it's… Would require, like, some attention from people who have some experience here.
I think this is something which most people should be already familiar in the code. Like, we've been, like, fighting this problem for quite a while, where, like, in… we created a mechanism to
suppressed telemetry by putting a Boolean flag in our context. So if context is flowing, then we can always consult the context. Hey, are we in a telemetry suppressed context or not? But that only worked if we know that context is propagated properly, but in case of
OTLP exporters, we use this request client and Tony Klein, and they…
generally jump across thread boundaries, and they don't do… they don't know anything about open telemetry context, so obviously they don't propagate it, so our suppression wouldn't work, when we are in OTLP context. So we provided some, like, temporary workaround, like, just suppress it, using, like, normal filters.
But this obviously had the side effect that if users were using Tony Core, H2, or Rickus for their business purposes, that also gets dropped.
So that is more like a hacky workaround.
So what I showed here is… it's still a workaround, but I would say it's not a hack anymore, it's still, like…
It's not hack in the sense we're not, like, building
rules or anything. It's just that when we create an HTTP client or gRPC client for use, within…
Open Elementary's OTLP exporter, … The client will capture a…
Tokyo Runtime, because GRP… the tonic does not work without Tokyo Runtime, so it has to have it. So we…
create a… Separate runtime, different from the normal one.
with just one thread, and we… I mean, technically, it doesn't matter whether it's one thread or not.
So we can… what we do, the critical part is…
We intercept the thread start and thread stop to Start a suppression context.
And this runtime is what gets used by the OTLP clients, like gRPC.
So even if they create more threads, it's fine, because we are going to suppress telemetry from that, and since this runtime is specifically created only for the OTLP exporter, it shouldn't have any impact on the rest of their application. So if they use electronic from their normal business logic.
That will continue to be instrumented as before.
Yeah, so this is the, like…
I don't know, it's more like a better workaround than before. It's not ideal. I would say the ideal situation is when everyone has a…
common context to follow, like, it need not be OpenTelementary, like, Rust language, or, like, OpenTelementary and tracing could…
Come up with a…
neutral thing called context, which everyone can respect and propagate, but that's much, much longer a time solution. Lilith, you were saying something?
**lalit** 22:48 No, no. I mean, I just reached office, so probably sitting on it.
**Cijo Thomas (Microsoft)** 22:52 Got it, yeah. Yeah, so, bearing, like, any such dramatic change in, like, Rustlang or, like, something, like, very different, this is, in my opinion, the best bet we can. Again, this
There's no change in our code, it's just, like, telling users, how to…
achieve this themselves. If they don't want to do this semi-sophisticated setup, they can do what they are doing already, like the…
Turning off based on filters.
…
Yeah, I mean, any… I think one of the comments which was left in the comment, PR was, can OTLP exporter offer this magic helper ourselves? Technically, yes, but I was trying to avoid, like, expanding OTLP's exporters public API, for solving this problem.
I mean, it's… if people really feel strong about it, we can revisit that, but I think this is quite reasonable for a GI time frame where users can… anywhere they need to create runtimes for their business, they either do it with macros, or they create it by hand, but we can ask them, create one more for OTLP.
And copy this code there.
Any comments on it, or, like, I'll.
**Utkarsh Umesan Pillai** 24:04 Yeah, so CJ, I was wondering, like, so I saw that you had to comment out Tokyo Main, so I believe then…
Is it that, like, one runtime cannot be created under another runtime issue that is forcing you to…
Move this example from async main to regular main.
**Cijo Thomas (Microsoft)** 24:22 Yeah, the problem is, if I do this macro, then I cannot…
control the thread start or thread stop thing. It'll… -oh.
**Utkarsh Umesan Pillai** 24:31 That's the only… I thought even the runtime building itself, it might have lost a few, but okay.
**Cijo Thomas (Microsoft)** 24:36 I'll have to try whether there are any issues, because I believe, generally, you cannot create
a Tokyo runtime, once you're inside another runtime.
**Utkarsh Umesan Pillai** 24:44 the, ….
**Cijo Thomas (Microsoft)** 24:45 Most likely, you'll have to do it this way, and then the user's normal application.
Like, which will be…
after… yeah, I think this is a normal application logic. If they want it to be, running in a Tokyo runtime, then they'll have to do, like, rt.runtime.blowcon.
Which is what, like, this will translate into, right? This is more like a…
Helper, which takes your normal main and.
**Utkarsh Umesan Pillai** 25:12 Inducted sugar, yes, yes.
**Cijo Thomas (Microsoft)** 25:13 Yeah.
**Utkarsh Umesan Pillai** 25:13 So, I was wondering, like, so this approach, like, your line 69 to…
87, or… yeah, so that one, like…
is that, like, basically saying that your OpenTelemetry setup has to be called under a regular FN main? Like, because this would need… like, I'm wondering, like, if our users who are just using Tokyo main, like, how do they integrate it into their.
**Cijo Thomas (Microsoft)** 25:37 Oh, no, they have to, like, strip it and, like, do it by hand.
They wouldn't be able to… use…
This technique, unless they can, like.
Fall back to a normal mean.
create a separate runtime for OTLP, and then create a normal runtime, which would be the equivalent of what they were doing in their Tokyo main. In certain sense, this is already the case. If you think of, like, let's say the user is using gRPC Exporter.
We actually require them
to use a Tokyo, threat to begin with. It won't work with normal main, because the gRPC client requires a
took your runtime. So the user has to do it, create the
OTLP exporter inside Tokyo Main, or they had to manually create a runtime themselves and do it, which is covered in our thing.
**Utkarsh Umesan Pillai** 26:28 But that part, I think, is more like, …
Less problematic, probably, because most users must be….
**Cijo Thomas (Microsoft)** 26:35 Oh, yeah.
**Utkarsh Umesan Pillai** 26:36 This one identifies them to…
Yeah, I don't know, like, how with, like, the server apps, how simple is it, or, like, how much of a change would that be? Like, Axiom or whatever that would be, like, I don't know.
**Cijo Thomas (Microsoft)** 26:50 Yeah, there would be, like, some changes required, because they cannot rely on, like, So….
**Utkarsh Umesan Pillai** 26:56 The syllactic sugar.
**Cijo Thomas (Microsoft)** 26:58 Anymore? Yeah.
**Zhongyang** 26:59 It should be fine. Tokami internally does this.
The whole building, building runtime thing anyways, you just have to do it manually.
**Cijo Thomas (Microsoft)** 27:08 I think….
**Zhongyang** 27:09 That… the only improvement we can…
probably pursue, maybe ask if the Tokyo team can add, parameters in the Tokyo main.
To configure the interceptor on threat start and threshold stop.
**Cijo Thomas (Microsoft)** 27:25 I don't think it's available in the market configuration. The only thing I think….
**Zhongyang** 27:29 It's available now, these have parameters as unhandled panic, where you can configure how to handle unhandled panic.
But even that is still unstable.
**Cijo Thomas (Microsoft)** 27:41 Oh, okay.
**Zhongyang** 27:42 So there is a way to do it. If token names are not, we can definitely add a parameter to just put whatever the interceptor into the part of token name marker, but I doubt it will happen.
**Cijo Thomas (Microsoft)** 27:53 Oh, actually, no, there is an issue, because then, like, the entire telemetry would get suppressed, right? Because we want it to be…
we want to, like, put the suppression into the on-start only for the runtime used specifically for the OTLP exporter. So if they do it in Tokyo Main, then it will pretty much suppress the entire telemetry from the application.
**Zhongyang** 28:15 Oh….
**Cijo Thomas (Microsoft)** 28:16 Yeah, so that's more challenging, yeah. So it's somewhat inevitable that users… again, let's take it step by step. So let's assume that a user is doing…
HTTP, which is also our default. They don't have this problem, actually. I verified it yesterday. I think that's actually a good point to clarify. So, if I look at our OTLP exporters.
And look at our OTLP, which is our HCDP.
This is our default, like, we don't…
Why did we have to enable request blocking client? I don't think so, because this was the default anyway. So, even though in our example.
we show this thing. It's actually not required, because we know that we are using blocking client.
We know we have a dedicated threat.
In the batch processor, so this shouldn't be required. I tried removing this one, and there was no
issue with, like, telemetry-induced telemetry at all here.
The only issue is with gRPC. So, again, like, to take a step back, most people could go for their default, they don't need to do anything. If they go for gRPC, then even today, they have, like, one problem, because the problem is they have to do it… they have to create OTLP exporter from a Tokyo context.
But now we are asking them, you have to not only create ODLP exporter in a Tokyo context, but that has to be a separate Tokyo runtime, which has these extra hooks.
So it's… it's bad, it's slightly worse than the previous, but it's not, like, completely bad, because it's… like, we already have, like, some, like, procurement on gRPC customers, so we are just making it slightly harder.
So that's why I feel like it's not that bad. You should be able to manage.
And also, like, users, if they don't like this…
Like, ugliness, they can always just suppress it.
Using the normal filter, which…
Yeah, again, depending on the usage, what they want, they can pick it.
Yeah, another option I was thinking, which is something which I've been, like, trying to solve in .NET also, is…
the…
The reason why we are having this problem is Tonic as a client, or the hyper… the underlying clients.
They are all instrumented with tracing.
And when we create a client, there is no option to
Specify that for that instance of the client.
I don't need telemetry, or I don't need instrumentation. So there is no such ability in any of the clients.
Which is the root of the problem, because if those libraries provide a way to create a client without telemetry enabled.
then we can use that in the OTLP exporter, like, when we create the request client, or hybrid client, we can start in with no telemetry flags.NET did something like that recently in their HTTP client, when you
create an HTTP client, you have an option to say that, or don't do any instrumentations.
But that required, like, working with each
library we don't, like, maybe, like, HyperTony can request, or maybe, like, Hyper and Tony is sufficient, since request is on top. I think we'll have to, like, figure out if there is a way, but again, that would not solve anything in the immediate time.
That definitely would require us to work with those people to add such support and then incorporate that.
Yeah, so that's my other alternate, which I can think of.
But yeah, if anyone finds, like, any better ways, like, we can explore it, but other ways, like, see…
If this is worth documenting and, like.
For now, as a OTLP GA release, let's unblock the GA by simply documenting this problem and not spending any more resources on that.
**Zhongyang** 32:12 I'm not solace at all.
One solution that can fix the problem.
We can improve it.
After the J.
**Cijo Thomas (Microsoft)** 32:22 Yep, yep. In fact, that's the one beauty of this solution, which is this requires no API change from our side. OTLP exporter is not exposing anything, so that's one good thing.
So even if we introduce something, it'll be, like, purely additive change. Yeah, of course, like, users have to, like, rearrange their main method, but it's not as bad as…
like, asking every library others to provide some mechanism to opt out. So this should be, like.
Relatively easy.
**Zhongyang** 32:51 Yeah, and as the application owner, you're always gonna have access to the main functions.
So, like, it's a facial hidden, you know, dependency that you may take on.
implicitly.
**Cijo Thomas (Microsoft)** 33:07 Yeah. Anyway, like, I'll do one thing, I'll first clean up the HTTP one, say, interesting.
**Utkarsh Umesan Pillai** 33:21 So, CJ was wondering another thing, maybe, like, if we want to make it simpler and not have the users worry about the…
removing the Tokyo main syntactic sugar, like, can we, like, spawn a new regular thread, like, standard library thread?
within the Tokyo main function, and then within that thread, we can create a new runtime in which
sets up the SDK.
**Cijo Thomas (Microsoft)** 33:47 Yeah, I think it didn't work, because if you're already inside the Tokyo main, then creating a new thread
would panic.
**Utkarsh Umesan Pillai** 33:54 Like, standard thread, not the….
**Cijo Thomas (Microsoft)** 33:57 Yeah, that's… I think I did try that, like.
some time ago. So if you are… you're basically saying, let the main function be normal Tokyo main, and grab this thing inside a…
Normal, standard threat.
**Utkarsh Umesan Pillai** 34:10 Yeah, it's 100 Thread Spawn, yes.
**Cijo Thomas (Microsoft)** 34:13 Yeah, based on my understanding, no, it wouldn't work. It worked for the request. In fact, request has to be done inside a normal thread, not from Tokyo, so here we have the opposite problem.
Based on my testing at that point, it didn't allow. But anyway, I'll check once again.
Yeah, that would, like, ease some pain, because then we don't have to ask.
**Utkarsh Umesan Pillai** 34:43 Mmm.
**Cijo Thomas (Microsoft)** 34:43 To strip down the, … Nice, easy-to-use.
Tokyoamine macros, yeah.
Okay, any other comments? Otherwise, like, please take a look, and, like, if you find, like, some ideas, let's…
discuss that in the PRI. I'll just leave it open for a few moments. We need to close it before we call OTLPS table, so we have, like, some time.
… Where were we? Oh, we are looking at… yeah, let's see if there are any open issues.
I responded to this one, and…
This one I created, like, last week when I saw some…
PRs in OTLP, we are quite heavy in terms of allocations.
It's… possible, To reuse some buffers to avoid these allocations.
So, hey, Yongyang, like, you have some… Go ahead.
**Zhongyang** 35:41 Yeah, I just want to look at another PR, so if you go to, after, maybe after it finishes.
issues.
**Cijo Thomas (Microsoft)** 35:48 Oh, okay. Let's do it up at the end, yeah. Yeah, so this one, we… we do, like, quite heavy allocation, like, in the sense, our in-memory representation of
Log span metric is…
different than the Tokyo… sorry, the Tonic generated struct. So, first thing is, we convert this into
Destructs, and the… generally, like, tonic-generated code, they all require, like, ownership. There's no…
way around. There is no way we can pass a slice or anything. They always require a vector or anything. So for each span, each log, every attribute, everything has to be, like, quite literally cloned.
Into a heap-allocated vector. So there are a lot of cloning and coping, which…
Goes on, simply by converting our in-memory state into The tone extracts.
And then we do a… serialization, either JSON or TUNIC, that we… the APA we use.
is the one which requires a brand new vector. So it internally creates a brand new vector and serializes into the vector.
And then, when we do compression, which I only looked at HTTP, so this vector is copied into a completely new vector.
And then… The… the compressed…
Vector is passed to the exporting client, which means we give up
the vector. So the next export, we had to repeat the whole thing.
So that's a, like, gist of the issue. I think the actual task would be to first figure out whether the exporting client, do they actually need ownership, or can they operate on slice? And then compression, can they operate on in-memory compression, or, like, can they reuse? And then the serial… this one I have… I did look at, like, the…
serialization can actually be done into a pre-provided vector. It need not be the one which internally is created by the serialization library. So we should be able to, like, create our own vector, use it. Again, it won't directly solve the allocation that comes from
the related API, which someone showed, like, earlier, how to…
Potentially use that, so you create a…
offer from the pool, use it at the end. Nobody needs ownership, so you still retain, so you return it back, and then… So it's just a, like, placeholder, to see it. Again, I don't know whether it's a…
I don't think it's a blocker for GA, like, we can… I mean, as long as functionality is there, we should be able to do GA or TLP Exporter, but it's more like a nice-to-have thing, to avoid these allocations.
Yeah, if anyone has, like, comments, or ideas or interest in… this would be a very, like, challenging program to work on, so if anyone has, like.
interested in doing it, like, please feel free to comment on it, or take it. This can be done in, like, very, very small stages, like, we can do…
try to optimize, like, one stage, either the compression or the serialization, or the actual exporting client. Like, we can do it in different, places, again, differently for HTTP and gRPC, so we should be able to, like, try something in a very small scale, and then expand it.
Yeah, I'm not tagging it with anything, I'll let it sit there, and depending on the interest, we can consider it part of GA, or we just let it sit there.
-Oh.
Yongyang, you wanted to go to a PR, right? So….
**Zhongyang** 39:15 Yeah, could you scroll down a little bit? There's one talking about, the 30… 7, 6….
**Cijo Thomas (Microsoft)** 39:30 Update….
**Zhongyang** 39:32 basically told them we're not doing anything to promises at this point, so I think we just can just close this one out.
**Cijo Thomas (Microsoft)** 39:38 Oh, okay, yeah, yeah, we actually marked it as duplicated… oh, okay, you already requested changes, yeah.
**Zhongyang** 39:44 But I won't flag it, see if there's a…
There's a… there's a discussion in the… in the PR descriptions, there's discussion that people seem to have
I don't know how should I call it, but it seems to have problems.
**Cijo Thomas (Microsoft)** 40:02 Yeah, I think one, like, we already covered in our deprecation note, like, about…
Yeah, it's already marked, let's see, in the crates, what do we… Mentioned….
**Zhongyang** 40:19 We mentioned the same thing, so basically with me.
**Cijo Thomas (Microsoft)** 40:21 Okay.
I think we have done, like, enough warnings.
So it should be okay to generally flow. Most likely, the reason people are still using it is they're not aware of the fact that OTLP can be used in a stable Prometheus. It used to be an experimental thing, but it's now GA since Prometheus 3, which is at least a year old.
So I don't see, like, strong reasons for us to continue.
Prometheus.
**Zhongyang** 40:49 This just goes to PR, then. There's no objections here.
**Cijo Thomas (Microsoft)** 40:54 Let me open it once more….
**Zhongyang** 40:57 0076.
**Cijo Thomas (Microsoft)** 41:36 Okay, any other things worth looking at?
**Zhongyang** 41:42 I think there's some old PRs, been trying to gooze through them, but I haven't… Oh, I said, also?
**Cijo Thomas (Microsoft)** 41:48 I want to see what everyone thinks of, like, some tutorials, which…
I'm not sure how much…
Of these, we should invest in.
the reason why I started this was, like, our… almost all of our…
Examples are, like, focused on, like, one signal, and again, it's not… it doesn't go beyond the simple SD-out.
So that's where I feel like maybe we should have a, like, all-in-one example.
Again, it's not super easy, because we'll need one for normal console applications.
And one for, like, web servers, so you need to, like, maintain two sets of pretty much everything.
Which shows all 3 signals using OTLP, and some backend of
our choice. So for Traces, most likely Jaeger.
Matrix, Prometheus, and Grafana should do the job, but logs, I think we'll need to use, like, OpenSearch. That's the one which Open Delimited demo is also using.
It is quite a large number of things we have to maintain if we choose to go with this.
But if you look at it, it's… it's already the case for many languages. I was just looking at .NET.
So, metrics that are… console-based example, and web server-based example.
And… Also, we showcase the one with a particular backend. These are, like, simple, like, SD-outs, but…
The one we maintain for… specifically for Prometheus, and same for Tracers, we have it…
console SPNET Core, then, like, using Acre.
…
So it's there for, like, other languages, but I don't know. Just because other languages have it, we don't have to have it. Yeah, I don't want us to, like, make a decision, like, on this call, but I'll just, let everyone, like, see if these are useful, then…
I can spend some more time, like, adding to it, because at some point in the future, we'll also have…
exemplars in matrix. And at that point, we'll be able to have a nice end-to-end working solution where
You have metrics, logs, and tracers, and all of them correlated with each other very nice, so you can go from metrics dashboard to logs and tracers. Such a thing do not exist in any language. I did check, like, quite detailed, and there was no language.
Which had, like, such demo.NET came very close, with our exemplars.
But no other language had, like, such detailed things. I feel like this is a useful thing. Many people don't know how to use, like, exemplars, how to navigate from one signal to
Another, but to add such a, proper tutorial, we need to
have a base which shows old signals. We cannot have, like, 3 independent documents for each signal, and then show how to correlate.
So there is some, like, value, which I see here, because we can make it, like, incremental, like, you start with, basics, add it, then add logs, add metrics, and then on the advanced section, we can talk about how do you achieve, like, correlation across signals, and more intelligent things.
It'll be a lot of effort to maintain, like, no objects, no costing in that, so we'll need to decide whether we want to maintain it or not.
And in terms of, like.
writing, I think I'll be very happy to write it. I wrote it for .NET, like, long ago, and it…
It's not, like, overnight, like, we did it, like…
like, over time, like, I started one, then other people started contributing, and eventually we had a lot of end-to-end document internet, so I hope that we can have it. But if you think it's too much to maintain, then, like, please review a, leave a comment, then we can see how to address that, or we can decide, okay, it's not worth it, worth it.
**Zhongyang** 45:38 I think it would be nice to provide such a tutorial to the user, so I'm in favor of maintaining it.
events, sounds like a word.
Only for comment.
**Cijo Thomas (Microsoft)** 45:55 Oh, yeah, yeah.
Just put a note here for people who are not in the call.
Yeah, or, like, other thing which I observed is, like, some languages, like Java, they even spun up a completely new repo just for maintaining examples.
They have a, like, this is a… yeah, this is full repo with several, … Like, examples.
This is also, like, quite a significant thing to maintain.
Yeah, I think we don't want to go, like, that extreme. We can at least do, like, something better than the current state, which is 3 independent tutorials, or 3 independent, like, examples.
So it should be, like, much better to have a unified thing. It's more like storytelling. We start with, something simple, then add on to it. Anyway, like, leave, comments.
on feedback, like, more like I'm looking for direction, like, are we okay with this? If yes, we'll work on it, but otherwise, we'll abandon, so leave comments with the general
Support our objection.
Okay, I think that's all the topics we heard.
Yeah, if there is anything else, we'll meet next week.
**Zhongyang** 47:45 Have a good week.
**Cijo Thomas (Microsoft)** 47:47 Yeah, you too, bye-bye.
**Zhongyang** 47:48 Pardon?
