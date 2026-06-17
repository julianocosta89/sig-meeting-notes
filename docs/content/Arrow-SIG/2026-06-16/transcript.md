SIG: Arrow SIG
Date: 2026-06-16
Duration: 50 minutes
============================================================

## Zoom Recording Transcript

**jmacdonald** 01:56 Hi, everybody.
**kennedybushnell** 02:00 Whoa.
**jmacdonald** 02:04 I'm gonna pull up our notes.
I've been talking all day, I'm starting to lose my voice.
Okay, here we are.
And I'm checking on the list of… people… who appear to be all very familiar with each other. Very good.
So I know that the F5 side may be not very present today. It might be just a bunch of us.
And we can do the usual things. Feel free to raise your hand.
I'm gonna fix this up.
**Tom Tan** 02:57 Power entry.
Today's reading.
**jmacdonald** 03:00 Say again?
**kennedybushnell** 03:11 I think that may have been an accident.
**jmacdonald** 03:23 Just realized I had the wrong microphone. Maybe you can hear me better.
So I will pull up the issues list in just a moment.
First, I'm going to start this new meeting notes section.
And let's open up the… issues.
What do we do here? We do this.
And I missed a few meetings, so this will be refreshing for me.
I… since I was out of the office last week, don't know exactly where we ended up, but my guess is that a lot of this was opened after the meeting last week.
So, let's see… I was… I'm going to assume that we've spoken about the… wit… WebAssembly interface… Something, something, in several meetings ago.
And we're looking for the ones that don't have… Triage on them.
**Aaron Marten** 04:44 So, Josh, I put a link in the chat for the ones that we've already labeled as Triage Needs Discussion.
So we want to start with those.
**jmacdonald** 04:52 Thank you, thank you.
I was about to get there, but we'll just use the link.
Ha! This is gonna be very easy. You have only 5.
Alright, let's see what we can see. So, Lauren is on vacation now, but he's posted some thoughts on Phase 3.
This may be the topics that he removed from the blog post, my guess.
So these are the things that he has in mind. We should be free to ask or add things that are on our mind.
I know that I was the one who added profiles, because I made a comment on his blog post. So, I generally agree with all the things that he put on this list, But I don't feel like this is anywhere near settled. Would anyone like to discuss?
**kennedybushnell** 05:50 We did talk about this in the last meeting, and there was no… push back on any of it. I think that you wanted to dive deeper into the… the extensibility, the WASM stuff?
But now that he's gone, Probably wait till he gets back.
**jmacdonald** 06:08 Right.
**kennedybushnell** 06:13 Sure.
**jmacdonald** 06:16 Okay, this is looking at which features are considered part of a stable collector. Yeah, I think we should, keep this issue open. We should keep the needs discussion label as well.
I feel like I don't quite yet know what we should call Phase 3, and it's not necessary that we immediately get that charter from OpenTelemetry, in my opinion. It's sort of like… we… we are… we still have some momentum without starting… formally starting a new phase.
I would say.
Let's see… Anish… Who is on the call?
It's joined us, and let's see, we're talking about… Better fed… okay, so push credentials.
So, a method of receiving new credentials, I take it.
**Manish Goel** 07:08 That is correct, and I can provide a summary of the issue and the solution I'm proposing. It's documented in the issue as well, but I can.
**jmacdonald** 07:20 I say, please go, yeah.
**Manish Goel** 07:21 Okay, so, currently, when we try to integrate the OTEP data flow, right, in a host, which is running many pipelines.
What happens, like, for every exporter.
that is running, it tries to acquire and refresh its own token from the backend.
So, that has, two implications currently. So, the first one is, like, at scale.
That basically, multiplies the control plane traffic. So depending upon the number of exporters, the, control plane traffic increases exponentially instead of, increasing, based on the host ride.
And the second issue that happens, which is more fundamental, is in deployments, where the credential is, It comes from, like, A mechanism, like a non-exportable cert, In those cases, the certificates are in the custody of the OS key store, for example, Windows.
And, the exporter… exporter doesn't have a way to load those, certificates.
So, the exporter cannot self-acquire the token.
So, we need a mechanism for, like, the agent to push, fed the exporter the token.
And, the proposal, I have in this is… There was a OTAP extension-based framework that, Gokan had, has created.
And, as part of that framework, there is an initial version of, like, a bearer token provider extension.
So I'm recommending that we extend that, Such that it, supports, credential once-per-scope, mechanism.
So that it can be pushed to the, extension, or to the exporter.
And, what will happen is exporters will keep on consuming the token from the same, methods that they have, so that the Mechanism will be trans, like, transparent to them.
So, that's one of the parts, and other is, like, as part of this, we require other interfaces. For example, along with the token, we require, like, Other parameters, for example, the, endpoint details, and maybe the, moniker details, which are, like, internal to some vendors. So those need to be, passed along as well to the exporter, as well.
So, another interface can be added, which can be implemented via another extension, or the same extension. So, one extension can maybe implement, like, multiple capabilities here, one with the bearer token, and other for the, like, the vendor-agnostic payload, that can be fed to the exporter.
So that's… that's the, like, the issue and the proposal, like, yeah.
**kennedybushnell** 10:40 You're muted, Josh.
**jmacdonald** 10:41 Sounds very good. I take it you have in mind, sort of a shared extension that interacts with the operating system, and then that shared component will We'll distribute the authentication material to each of the exporters, basically.
**Manish Goel** 10:59 Long-term, yes, but the current extension framework doesn't, support, like, purely shared extension. So, right now.
for each exporter, an extension will be required, but going forward, yes, once the shared extension is supported by the framework, that will be the way to go for it, yeah.
**jmacdonald** 11:21 Got it.
I would love to hear if others think, it sounds like there's a decision being made about whether to combine features into the bearer token extension, or whether to have sort of separate extension for pushbearer token or something like that.
**kennedybushnell** 11:43 Yeah, I think… He's trying to make sure that we're aligned on a way that we can do this.
using, like, kind of an abstract concept around how we can push these credentials rather than be pure poll-based, and then also tie additional information to it, for making that request. For example, like, in a multi-tenant scenario, you might have a bearer token that only works with, like, 2 out of your 5 Extensions, or your pipelines, because, like, it's for, like, a specific backend, say.
So your… your auth grants are only valid for those. So you need a way to, like, say, hey, I need a bear token that's good for this backend versus this other one, and… and have a mechanism to do that. And then we have the same problem with certs, kind of, in general.
so, still, like, kind of a lookup key-based… way to do that, I guess.
**jmacdonald** 12:37 So the key distinction is that you're making a subscription for the details over which you need these off tokens, or provided to you. You're not pulling them, therefore you must register your query somehow.
**kennedybushnell** 12:52 Yeah, basically, because we… that was what he was talking about at the beginning, where we don't want to explode the number of calls going to the backend to go grab these tokens, which is what would happen right now if you just attached an exportr. They'd all go and, like, go get their own token.
We want the… like, we have the agent that it's going to be living in already making that call, and if we can just, like, tie those together and say, hey, I've already got the token for you, you just need to tell me you need it.
**jmacdonald** 13:23 Gotcha. Cool. Well, I think we can remove the needs discussion, Manish, are you interested in this being assigned to you?
**Manish Goel** 13:31 Yes, please.
**jmacdonald** 13:33 Okay, cool.
Very good.
I will do that.
If I… if it can tell me, yes, there we are.
Cool.
Okay, I'm gonna go back to that list we had, now it's shorter.
**kennedybushnell** 13:50 I suggest skipping to the first one listed, because it's very related, the 3307.
**jmacdonald** 13:56 Gotcha. That's what you're saying, yeah.
**kennedybushnell** 13:58 Yeah, so Henry's not able to make it, so I'm gonna kind of talk on his behalf here, but this is a very similar pivot of that, except, kind of related to the whole OS platform keystore, only like, the… The problem that we have here is we have to use a very specific library in some environments to get the certificate.
So… there's kind of two things. We need the ability to use that library, which the extension API allows you to do pretty nicely. We'll just have to build our own kind of internal extension for that. But we also need the exporter to support not accepting just from a cert file and a key file, but also accepting from extensions more generally, saying.
Just give me a cert, and then we can tie that extension to it.
**jmacdonald** 14:55 I see.
So… I am definitely taking away that we need more auth extension work here.
And I'm sure there's a… the connection with tenant identifiers is present, here as well. Correct.
And so, I'm definitely taking away a kind of need to design around, tenant configuration and auth configuration, whether it's push or pull, auth, and whether it's error token or not.
I, do we feel that… Other than… that the tenant issues that I sort of alluded to are perhaps separable, and that we could begin working on this, should we assign this to Henry, for example.
I'm mostly taking away that we need to work with Goken and also Manish now about making sure that the auth extension interface is solid.
**kennedybushnell** 16:00 Yeah, it sounds like there's… there's three things. Extending auth in general, like you're talking about, the ability to look up by, like, a key that… in some kind of, like, a request fashion, and then, I think this one is more specifically about Moving the exporter to… Use the extension.
**jmacdonald** 16:23 Hmm, you know.
**kennedybushnell** 16:23 Which is just what's missing right now that ties it specifically to certify keyfile. If it was using extension, we'd at least be unblocked, and then we can go build the other things, yeah.
**jmacdonald** 16:36 I see, I see. Okay, so this TLS configuration is not nearly sophisticated enough to have a per-tenant certain mechanism to begin with. And moreover, we would need to… it sounds like the functionality of this TLS block is… would ideally be replaced by a an off… by TOS mechanism that tells you where your MTLS certificates come from according to the tenant identifier.
**kennedybushnell** 17:07 Yeah.
**jmacdonald** 17:08 Cool.
Very good. I think, At least I'm able to understand this now.
Some good details here.
I understand, so, another extension mechanism I said off earlier, but it does seem like off is different than TOS provider.
Does anybody want to talk about that?
**kennedybushnell** 17:41 It… This is AW. This is the exporter, so I think it's MTLS is really what is being discussed here, so it's AW. On a receiver, it may be TLS, and just, you know, what cert you present.
**jmacdonald** 18:00 Okay, that makes sense, yeah, what I said was more relevant for receivers. Okay, well, we should definitely remove the needs discussion label.
I don't think we need to discuss this more. Shall I assign this?
Would you say?
**kennedybushnell** 18:15 Yes, Henry is prepared to work on that.
**jmacdonald** 18:17 Okay, great.
**kennedybushnell** 18:18 Accepted, so…
**jmacdonald** 18:19 Very good, very good.
I am glad to hear that. And I'm also happy to hear that we're doing this. If we need more discussion, of course, we can do that here, or in Teams, if you will.
We're down to only 3.
I know Drew wanted to discuss this one, and he's not here, so I can definitely take this one, and explain, what I know about it.
It's a long issue that Drew filed. There has been some discussion. I wanted to see if there's anything new. So, this is more or less calling out the chaos that we have created for ourselves with metric names, and Drew did a pretty good job, I think, of clarifying it. The idea that we have for many of our components, we followed a sort of, like, I would say instinctive, like, like, the natural thing to do in metrics is to have one per signal type, per per verb and per… or something. And the… the confusion comes in because we are counting both requests in some places, but we're also counting items in different places.
Moreover, we know that we want to count bytes sometimes, that's a good option.
And that the… Units we use in our metric metadata are also very chaotic.
So… this is quite comprehensive. I appreciate this. And then… Drew kind of called out the common element of these metric names, at least the apparent pattern that you see.
And… was proposing A consistent update to them.
Which is a good proposal, However.
I mean, it's worth talking about this alternatives considered, and you'll see why I mentioned it below.
Is that there… I'm starting to see that there are just so many ways that you can instrument something. I've been working in this area for quite a while now, and there's never a best answer. So you come up with one solution that works for you, and then somebody else will come in and say, oh, I don't want that level of detail, or I would prefer, because of the way my query system works, to use attributes instead of separate metrics.
And that's really what we're talking about here, is attributes versus separate metrics.
And I've stopped believing that anything is… there's one truth in this. So… One thing I'll say is that I agree with the pros.
I sort of disagree with the cons, because So, in some sense, my… I've worked with metric systems that were very natural when you had attributes, and, like.
If you want to make a query that's, like, comparing, like, computing the rate of dropped data.
If you're using attributes, you can make that query be all about one metric, which simplifies the backend query.
Versus if you've got several metrics, you have to write complex queries over several metrics. Kennedy.
**kennedybushnell** 21:24 You can finish the thought.
**jmacdonald** 21:26 Oh, really just to say that it always depends on which metric system you're using, whether you're ending… whether you end up writing The signal type in your metric name or not.
But the… one of the cons that I see is that, well, we're gonna add profiles at some point, and currently, you have to remember.
Like, if I'm looking at the entire performance of the collector, that there are three signals, and so I will write metrics, and I'll write logs, and I'll write traces, and I'll have metric dashboards for each, and then along comes profiles, and now you need a fourth dashboard, or a fourth element in every query.
And in some sense, the idea behind the attributes in OpenTelemetry is that you can Aggregate in very many natural ways, and if you just want to remove the outcome, then you've got the total number of elements that were processed, ignoring success and failure, for example, without having to think of two metric names.
You know, you can wildcard your attributes and so on. But I know that not everyone agrees with that.
I don't want to keep talking. Kennedy, I'd love to hear your thoughts. I do have this PR that I could relate, but I'd like to hear your thoughts.
**kennedybushnell** 22:32 Yeah, so I… I agree with most of that very strongly. So, like.
back-end is very important for the way that you prefer your attribute versus naming, I agree 100%. So I think that the… The way that would be… Reasonable for us to solve that type of problem is to be consistent in our own use of metrics, and logs and traces for that matter, and then allow for you to like.
cheaply convert between them. So, like, if we use the form of metric where we use attributes heavily, we just do that everywhere, and we make that part of our process, and then we have a, here's how you use our attribute processor, or whatever transform to go and make that for your other backend, then we don't have to be in this world where Like, the inconsistency makes it extra painful right now, because you.
**jmacdonald** 23:27 Yeah.
**kennedybushnell** 23:28 on the back end that prefers one or the other, and then half of our metrics are one way, half of our another, so you transform, like, the half as you find them. So if we can kind of solve that, especially if we can solve it in a way that's backed by tooling, so we can enforce that.
That that would be pretty solid. And then… Similarly for units, although… we discussed this a little bit in the previous SIG, it's very natural in metrics to just define your unit, and then you convert between units as appropriate. Milliseconds, nanoseconds, seconds is a very common one. And… that really is a per-emission choice. Like, us picking one number, or one unit, or maybe three units that we use everywhere, is just… it's gonna box us into these scenarios that I don't think that we want to do. So, we should probably… Have some guidance on, like.
Try to fit in these, but if you can't, then use the thing that makes the most sense, and not box ourselves into just, like, always using Nanoseconds, because that's the lowest granularity we want, or something.
**jmacdonald** 24:45 Yeah.
I mean, yeah, you remind me that the… one of the reasons why people fret over units conversion is that when it's a histogram, now power of 10 conversions are lossy, unfortunately.
So, yes, thank you, Kennedy. I have very, very much agree with you on that, but I want to go even further. So, firstly, I will say.
This document here, this that I'm hovering over, I could show you, is like… there's this document that hasn't changed in a while. It's actually… pretty old, and the… it's arguing for this attribute-focused way of doing things, but it was clearly written by someone who favors the OpenTelemetry style, not the Prometheus style, and it's almost like… yes, we've written this document, it's nice, but no one's done it. It's not… no one's jumping up to do this. It is actually implemented behind a feature flag, and I'm not sure it's moving very fast. So it's sort of like there is evidence that there is resistance to this, just because it hasn't happened very fast.
So, I kind of like it, but getting back to what Kennedy said about tooling and making it cheap for processing, I guess, that… this… this… this link here, this PR that I put together.
what, a month and a half? Two months ago, right? I was unable to make any progress on, because it's a big piece of work. And it was… it was really just a design document.
But I will say that it was very much targeted towards this conversation. My belief is now that there is no one good solution. Like, we can't take an answer and stick to it, because the feature of this is that it keeps changing. Like, we might find a good answer today, and then query languages will change, and tomorrow we maybe want something different. And I guess maybe the original kind of founding vision for OpenTelemetry has to do with this idea that you can separate your API from your production… from your SDK. And what I think… and in metrics, we did very long… originally in OpenTelemetry was to create this Views SDK.
feature. So views is a way, a nice way, I guess, of, manipulating the metric name that you emit, so it's done, essentially, at the moment you build your… your metric like, your metric meter object, you will apply a mapping that's in your views. Then after, your metrics are inexpensively converted to exactly what you want.
The problem that we have in the, the, the Dataflow Engine codebase is that there are no attributes right now.
There are only… structs?
multivariate structs that have counters in them, and that's one reason that we ended up with the other pattern, where you have one metric for everything, is because we started with structs, where you have one field for everything. There's no, concept of a multidimensional metric in the code right now.
And this document was sort of talking about all the ways that we could begin to, First of all, have control over what happens when you take that struct of metric observations and turn it into metric data.
One thing is you can apply your views right there. So, what I'm sort of pushing towards here is the idea, and I'll see if I can find the document where I put it.
this is an idea that you would have some YAML somewhere.
you're… we're still gonna have these structs in the code that are three separate fields. Like, you have a counter for logs, Well, sorry, this is not the right example. You have… this is a… a different example that I use with 3 outcomes instead of signal type is just outcome type. So you have a counter for success, a counter for failed, and a counter for refused. And right now, they come out as 3 metrics with 3 separate time series. One time series per metric.
And what we're saying is that some users might like to reconfigure this to have one metric with an attribute and three values, so 3 time series per metric. And… the idea that I had was to use the Weaver tooling, basically, to have static configuration in YAML, basically, to say.
We have some instrumentation. We create some structs, those structs have some measurements, and you can choose what you want to happen with those structs. You can choose the first choice, which is the flat metric name. The metric name has the outcome in it, or the signal name in it, and that's called the V1 schema, or the V0 schema.
And then we came out with a different way of doing things, and it's… It's written as a different configuration in the schema, and then you would… you would compile it with multiple supports, potentially, or choose your support, which, like, which schemas you want support for. And then when you begin runtime, you'll choose which schema you want, and then control, like, do you get the old way of doing things, or the new way of doing things?
That would be configurable. So the idea, essentially, is to put some configuration that says how the instrumentation is translated into metrics.
That could give us both options.
it's sort of an ambitious project, that's why it hasn't moved, why I closed it. But I still believe that this is a good approach, that you would eventually end up with configuration that says, for this metric scope named Metrics OTAP consumer, I want schema URL V1. That means I want the flat attribute namespace, maybe. And then V2 would be the The attributes version of that.
Essentially trying to say that the instrumentation is separate from the view that you use. You can choose the view at runtime, you can choose which views to compile at compile time, and it's a bunch of YAML. That's all I got.
So, I am sort of looking or sponsoring this type of work, but I know that I have higher priorities. Kennedy.
**kennedybushnell** 30:30 Yeah, so I did want to clarify an understanding. So you… when you gave that example of, the outcome-based metric with, like, success, failed, rejected, I think were the three.
That's… you said something that I didn't quite follow about how when you combine those, it would be a single metric with 3 attributes that have the value. That's… did you… this is really a multivariant metric that you're talking about there, right?
**jmacdonald** 30:59 Well, y-yes, and… Thank you for asking. So… I am referring to a struct that has 3 variables in it.
And what I'm saying is that it could be a… Compile time slash runtime decision, whether you convert that into 3 metrics with one time series each, or to convert that into one metric with 3 time series.
Yeah.
**kennedybushnell** 31:27 Okay, cool.
**jmacdonald** 31:28 That was the concept, at least.
that you would still have 3 physical counters in your instrumentation, and you would still have these structs.
I was actually going a little bit further, and I'm not sure anyone likes this idea. This was to say that, you know, you could have, So, like, considering this… hypothetical consumer items metric. This is my version of the… of it having attributes.
So this is my V2 schema, we'll call it. I wanted to say that you could have a configurable metric level, because I think a lot of times people sort of want a little bit of freedom to choose, like, you know, high, medium, or low. And the idea of having attributes focused for your metrics is that you can kind of do that.
Without changing the metric. So you have consumer items, it's either 0 or 1 or 2 dimensions, and this gives you the ability to control at runtime whether you output 0 or 1 or 2 dimensions. And I was gonna have that be YAML, but this was a… this was just a sketch.
Samir.
**sjmsft** 32:37 Yeah, I was wondering, like, the consumer in this case, the consumer of the metric could even be off-node. So, in which case, like, the schema information, is it transmitted with the metric?
How does that get conveyed?
**jmacdonald** 32:52 It would be sent with the metric, and I've been discussing with Metric's extension team how we start integrating their work, so I'm definitely tracking, like, you know, off-site metrics aggregation. But the reason why these three diagrams are here is sort of to help us answer the question, in OTAP, what does it look like when you have this choice? How do you represent an attribute in OTAP? And there were a couple ways you could do it.
I don't think we should dwell too carefully on the details here, but this is one where you focus on putting the attributes into the scope. It comes out nicer in OTAP that way, so you would… you're essentially duplicating some scope entries in order to have a single, time series per scope.
So this is a 3-table form of metric data, and then this is the 4-table version of metric data, where you have scope deduplicated, but you have 3 attribute tables and three metrics. This is 3 time series with an attribute, this is 3 time series with scope attributes. Kennedy.
**kennedybushnell** 34:00 Yeah, I just wanted to say, like, I agree with the goal of this in giving you the ability to go between… flat and attribute-based. I just… it feels like we already have the tools in the system, largely, to do this via, like, transforms and stuff, so it feels like it'd be more natural to do that than… like, especially then tie us to, like, a V1, V2, V3, like, structure that we then have to backward compat support forever, where if we just did it, like, here's what the shape of our internal metrics are, and if you want them in a different shape, use our… Full-fledged transform engine to get them in the shape that you want, and then you have full control over, like, how detailed they are, how you aggregate them as we put the aggregation engine in place, and all of that.
**jmacdonald** 34:45 Yeah.
Yeah, I… I will accept that position. I also have been on the fence, I didn't say it earlier, about the hotel views SDK stuff.
It always felt, like, heavyweight and not quite useful enough at the same time.
And what I heard you say just now is essentially a sort of vote against it.
Which I don't disagree with.
So, yeah, and hopefully the transforms are so inexpensive that… that you won't want that. I would say, sort of stepping back from this specific stuff here on the screen here, but, you know, looking at the… I don't think I have any examples.
again, in YAML. But the idea that, we have Weaver, and that Weaver is able to sort of look at first-class schema definitions, and that we can encode those in files, the idea then of having a runtime choice was one perhaps fanciful idea, that you could choose to emit V1 or V2.
I… and I was thinking, like, you would really choose that at compile time. Like, at compile time, you just list the set you want, because you might want to have more than one compiled in for a migration.
But most of the time, you'll want only one compiled in. So then the question is, okay, you know, you've got most of your fleet converted to V2, and so now most of the fleet is converted and has been recompiled with only V2 support.
But there's this, like, set of stragglers out there who are still running V1, and, you know, you don't even know how to update those. So now your problem is that most of your instrumentation is being done using the new schema originally, which means it's a little bit less expensive if you produce the right data from the start instead of having a transform.
But you've got that long tail. I think the idea behind using Weaver is that you might… begin auto-generating the conversion you want. So we'll produce the transform processor from the two schema files, we'll compile that into a transform definition, and then you can also do it as a transform. I don't know. When I look back at this proposal, it's pretty heavy weight. I don't think we should do this, but it's worth looking at for some ideas, perhaps.
**kennedybushnell** 36:56 Yeah, bringing Weaver in, or any, like, compile time component, changes the game entirely. Like, if you can tell me at compile time, and then we can start like, you know, doing, like, LLM or LLVM-type magic to go and convert everything on the fly, and it's still compile time structured and enforced, we can do crazy stuff, and, like, cool, crazy, not crazy, don't do it.
**jmacdonald** 37:24 Thank you. Yeah, I look forward to figuring out more about this.
It doesn't seem impossible that we would just compile the code to do one or the other by generation, but… Yeah, LOVM for the win.
Okay, well, I know we had one… left on our list that we… okay, so I… I'm gonna remove the needs discussion. It does need design work, I think, but, we've definitely discussed it.
Cool. So, lastly…
**Aaron Marten** 37:57 Josh, would you mind going back to that one? Can we have the needs info label?
**jmacdonald** 38:02 Thank you, thank you, thank you, keeping me honest. Okay.
This is… This one, still.
needs… Needs what? Wait, some wants?
**Aaron Marten** 38:18 We were using needs… needs info. Needs Info.
**jmacdonald** 38:20 There it is.
**Aaron Marten** 38:21 For, yeah, the opener should… Provide some additional clarification, if that's just needed.
**jmacdonald** 38:26 Yeah, I would like to hear what Drew thinks, yes. And he may listen to this conversation.
Okay, and then… the last one… oh, that was the wrong direction to go.
There it is.
Changelog rules and copilot instructions.
Go Ken, with us.
**Utkarsh** 38:50 No.
**jmacdonald** 38:51 Talk soon.
put…
**Utkarsh** 38:53 Yeah, hi, Josh. So, this was, created when, I was reviewing one of the PRs sent by Gokhan.
And, he has added, ever since we put this changelog check in, the BPR pretty much adds a YAML file.
He had… Added a braking change for… for one of his extensions API that he was working on. He wanted to, like, just update some method signature.
And that's when the conversation started, that… I asked, like, this is not really a breaking change, even though it's changing the public API, but, like, we haven't really released, there's no… there's no way any user could have accessed, what you're breaking, so we don't really have to call it breaking.
And that led to the creation of this issue.
So that we have, like, a more formal, guideline on… When do we call something breaking, and… Yeah, when do you use these labels. Got it.
Oh yeah, that context is this thread, that thread probably points to the…
**jmacdonald** 39:59 Gotcha.
**Utkarsh** 39:59 No.
**jmacdonald** 40:00 Well, thank you, you've summarized it well enough. I, definitely need such documentation. It's… but you're right, it doesn't sort of… usually when I see breaking, it means your user configuration that we promised with stable.
isn't really stable, or, you know, we're a major version release 1.0 or something afterwards, and we're breaking up a contract that we have to break for some reason. If it's a minor release… well, I mean, if it's a v0.x release.
I think you can still say breaking or not, but, like, I'm not sure it matters, there's not a strict definition.
So, yeah, I kind of agree that this is a hazy… Definition to begin with.
I wonder if the Go Collector has a document explaining this. That would be good to look for. Not gonna look for it in the moment here.
**Utkarsh** 40:58 Yeah, also, and I think we need to, probably think about Like, what are, support… Guarantee is, like, are we free to break stuff?
Are we gonna follow the technical SMBER definition of, like, you're free to break U1 till we do 1.0?
Or, like, are we… Like, like, how most trust rates, even though they don't have a 1.0 release, even the 0.5, 0.6 are considered pretty… stable from a usage standpoint, so they don't really go around breaking just because SIMBER allows it.
So, we need to probably think about that as well.
**jmacdonald** 41:38 Yes, and I also, in the Go Collector environment, I have… I know that we have special documents on extension Compatibility, essentially, which is a sort of special case, usually, because you want those to be open interfaces, you just have to promise not to break them.
For users who want to implement them.
So I'll add these… this comment, but I have, I generally agree.
So… what should we do? Do we think we need data so that we can write a document on this?
use info.
**Utkarsh** 42:19 Yeah.
**jmacdonald** 42:22 I agree with that.
Alright.
We did triage through… Something like… Issue number, whatever.
3250A is the last one with the needs discussion.
We don't need to… do this anymore.
No more agenda items. Does anybody have a topic they'd like to discuss?
No need to answer. Sounds like no.
I appreciate you all being here with me today. Oh, Aaron, hello.
**Aaron Marten** 43:04 Sorry, I just had… I had a quick question on the whole, like, Phase 3 thing. My understanding is there was some kind of discussion that happened regarding a review of Phase 2.
So I just was wondering if you could, like, Relay any kind of… You know, status update.
**jmacdonald** 43:23 Well, all I know… I was out last week… all I know about is that we published our blog post.
Which is to say we published something, but I don't know about a review, so to speak, which would sound like something the hotel governance committee might do. That might be a question Trask could answer, or… maybe some of my unread Slack threads could answer, but I doubt it.
So I'm not sure I have an answer.
**Aaron Marten** 43:51 Okay, sounds good. Yeah, I'm not aware of anything. I was just… I had heard there would be some kind of, you know, discussions happening with the various committees at some point. I'm not.
**jmacdonald** 44:00 reviewed any of that?
**Aaron Marten** 44:01 paying attention, I was just wondering.
**jmacdonald** 44:03 Yeah, no, okay, I understand. So I think what your real question is sort of, like, how do we sort out what it means to be Phase 3?
And I break it down to two questions. You know, OpenTelemetry tries to keep a limit on the current number of projects. So, if you don't have a current project, then what are you doing? So we want to create a new project definition, which we would call Phase 3, just to give us a sort of right to take space in the OpenTelemetry, like, headspace.
Because there's a list of them, and you don't want it to grow too big.
So we should create a project definition, I will say, before long. If we haven't done this by the end of the semester, though.
we should do this by the end of the semester, in my opinion, but we don't have to rush for it. And secondly, the second part of this is we should, not just within ourselves, but between F5 and other open source members of the community, like, discuss this in a more broad way, because I think what we want for Russ is also… not what's really on the mind of all those governance committee members and so on, which is really that we have to talk about the Go Collector, we have to talk about interoperability, we have to talk about WebAssembly, we have to talk about the collector builder, we have to talk about publishing crates, and how we bring Go and collect… Go and Rust together, and so, we need to be very intentional. And so the issue that Laurent opened is, to me, a good starting point, but it's really just saying, we want to discuss this, we've got months to do so, I would say.
**Aaron Marten** 45:38 Cool, thanks.
**jmacdonald** 45:40 Thanks, Aaron.
Alright, I'm gonna write down… that, but otherwise, I think we've reached the end of the meeting.
That's what I think.
**kennedybushnell** 46:05 I concur.
**jmacdonald** 46:05 Great, thank you all.
**kennedybushnell** 46:06 Thanks, all.
**jmacdonald** 46:07 Thanks, Al. See you next time.
