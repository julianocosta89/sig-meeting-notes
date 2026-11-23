SIG: Resources and Entities SIG
Date: 2026-11-16
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**krajo (Grafana Labs)** 01:57 I just…
**Josh Suereth (Google LLC)** 01:57 Yeah, go on.
**krajo (Grafana Labs)** 01:59 Can you hear me?
**Josh Suereth (Google LLC)** 02:00 Yeah.
**krajo (Grafana Labs)** 02:01 Oh, awesome. Yeah, I'm in a hotel room in Toronto, and… But different setup.
I'm trying to fix my video at the moment.
**Josh Suereth (Google LLC)** 02:11 No worries, no worries.
Inc.
Don't think I'm presenting yet. Yeah, looks like everyone's joining in.
Alright.
Folks, feel free to add your agenda items and your name to the attendees list.
We have, D.
Then here we want… Alright.
Sorry, I was a little delayed on getting the agenda together.
Welcome, everyone. Hope you all had fun at KubeCon.
All right, in terms of getting started, I want to start with, talking a little bit more about Dmitrii's PR.
**Dmitrii Anoshin (Individual – No  Account)** 04:15 Piper.
**Josh Suereth (Google LLC)** 04:16 You're good.
**Dmitrii Anoshin (Individual – No  Account)** 04:18 Yeah, I just wanna say hi, everyone.
Sounds good to me. Let's talk about it.
**Josh Suereth (Google LLC)** 04:26 Oh, if you're new to the SIG and you want to introduce yourself, feel free. Sorry, I didn't see who was talking. Was that just Dmitrii?
**Dmitrii Anoshin (Individual – No  Account)** 04:32 It's me, it's me.
**Josh Suereth (Google LLC)** 04:34 Okay, okay, I couldn't tell. Sorry, I couldn't tell your voice, my bad, yeah.
**Dmitrii Anoshin (Individual – No  Account)** 04:39 I got sick at the Cube Quarter.
**Josh Suereth (Google LLC)** 04:43 Okay, was there… was that a super spreader event? Because everyone on my team who went is now sick.
**Dmitrii Anoshin (Individual – No  Account)** 04:49 I guess so, yeah.
Something, something.
Something that was there.
**Josh Suereth (Google LLC)** 04:54 What were you guys doing at QCon?
Alright, well, I hope you… I hope you feel better soon.
**Dmitrii Anoshin (Individual – No  Account)** 05:02 Thank you.
**Josh Suereth (Google LLC)** 05:03 Yeah, okay. Am I… I don't think I'm actually presenting the right thing here, am I?
**Dmitrii Anoshin (Individual – No  Account)** 05:10 Oh, we see your, doc.
**Josh Suereth (Google LLC)** 05:13 Okay.
**Dmitrii Anoshin (Individual – No  Account)** 05:14 Of course, yeah, here we go.
**Josh Suereth (Google LLC)** 05:16 I think we've gone through this. There are a few… issues now here that were just raised, that we can walk through, and I think… I don't remember if we went through all of Jake's issues previously, I think these are somewhat new as well, so…
**Dmitrii Anoshin (Individual – No  Account)** 05:29 Yeah, Daniel.
**Josh Suereth (Google LLC)** 05:31 Okay, for some reason, GitHub's not giving me them in context where we can, like, add notes to them.
Is that because I'm not logged in anymore? Did it log me out?
It did. Okay.
Hold on, I will, let me log in at another…
**Dmitrii Anoshin (Individual – No  Account)** 05:48 And you also have…
**Josh Suereth (Google LLC)** 05:49 I'll show you for me.
What?
**Dmitrii Anoshin (Individual – No  Account)** 05:50 We also have Old UI, which is… more familiar.
**Josh Suereth (Google LLC)** 05:56 Oh, there's a new UI now? -Oh.
**Dmitrii Anoshin (Individual – No  Account)** 05:58 Yeah, there is a new UI, and you're probably not in the A-B test yet, but… I guess many of us already use that.
**Josh Suereth (Google LLC)** 06:10 And just gotta get my passkey here.
It'll probably pop me into the new UI. I'm generally grumpy about new UIs, unless I'm the one who's actually trying to, like.
You know, get people to use them.
**Dmitrii Anoshin (Individual – No  Account)** 06:25 There are plenty of things to be grumpy about in the UI of GitHub, for sure.
There are some good parts, but… yeah.
**Josh Suereth (Google LLC)** 06:33 Oh, come on.
We'll do a big reload.
Skip the content.
Alright, and my cat just decided she wants attention, so she might disconnect me again, because she loves playing with my USB cable. Alright.
Cool. So I think we're here now, where things are in context.
Let's move down to the new ones.
Okay.
So I was thinking that we can walk through these one at a time and kind of address them?
Just to…
**Dmitrii Anoshin (Individual – No  Account)** 07:10 Yeah.
**Josh Suereth (Google LLC)** 07:11 Go ahead.
**Dmitrii Anoshin (Individual – No  Account)** 07:12 Yeah, I just want to say I haven't had a chance to go through them, so we can maybe go through them right now.
**Josh Suereth (Google LLC)** 07:19 Yeah, I… because I think this… this particular proposal is, like, the major blocker for our future work, so I want to make sure that we are addressing it. So I was thinking we could all do silent reading for, like, 30 seconds, minute, however long it takes you to get through it, and then have a quick discussion on each topic.
Just to get this thing through.
Okay.
So…
**Dmitrii Anoshin (Individual – No  Account)** 07:39 Sounds good.
**Josh Suereth (Google LLC)** 07:40 Yeah, everybody take about a minute, and then when you're ready, raise your hand if you have, like, a response or something to this.
Okay.
So hopefully everyone had a chance to read this. Jake, I see you're here.
Because if it helps, you could re-describe the question you're asking, but I think it's written pretty well here.
I can respond briefly with this, this particular thing. I, I think what you're reading here with the data model and the, the resource. Our… We have this notion of how to merge entities into a resource, because today, in OpenTelemetry, all signals are basically, you know, resource signal attachment.
So, it's like this fundamental thing in OpenTelemetry. We are trying to detach it a little bit, where we want the attachment to kind of be signal to entity.
The reality, though, is, is, like, how is that kind of a non-breaking change?
And… Yeah.
I guess… If you could, like, elucidate specifically your concern here.
What kind of coupling do you think we have too much?
in this PR that you'd want to change?
**Jake Dern (F5, Inc.)** 10:26 Yeah, I think I'm just more trying to understand, one, like, sort of how the SIG is thinking about resources and entities, just in the sense of, are these orthogonal things, or do we feel like entities are sort of the next evolution of a resource, and that kind of thing?
And then the other thing I'm trying to find out is, you know, is it required that we always sort of… Couple the identity of, some, some entity, to a resource, in the sense that You know, the statement here that jumped out at me is, like, a scoping entity is found by type, this is unambiguous because a resource holds.
at most one entity of a given type. To me, that puts a lot of restrictions in terms of how you can represent Or communicate an entity. Because if you're always saying, like, oh, okay, well… Things are unambiguous because I have at most one entity of a given type, you know, in whatever data model I'm using to communicate them.
Then that requires that you then define multiple resources if you have multiple entities of some type, and it… it feels like there's sort of, like, an implication there, and so I'm curious if that's, like, intentional or, Yeah, what the thinking is.
Because we're looking a lot at, for Hotel Arrow, like, how do we define, like, our internal entities versus, like, the ambient ones?
And I think I mentioned we're leveraging scope for that, to try to give us some way to, you know, to not have to repeat all of our resource attributes, all of the time for every single internal entity. And so, you know, this would almost sort of require, hey, if I've got… 5 node entities, I'm going to have to define five resources, and therefore, you know, then also communicate all of the attributes for those resources every single time.
**Josh Suereth (Google LLC)** 12:22 Yeah, so that second thing you were talking about there, of if I have 5 nodes and I have to report them as resources, that is a… A problem that we had with profiling, where.
**Jake Dern (F5, Inc.)** 12:34 Yep.
**Josh Suereth (Google LLC)** 12:35 You're trying to report on, like, 2,000 processes?
Yeah. And so, just the cost of putting them in resource was, like, 50% overhead on the signal itself.
**Jake Dern (F5, Inc.)** 12:44 Yep.
**Josh Suereth (Google LLC)** 12:45 So, alright. I… I don't know if you want to take a crack at this, Dmitrii, before I… take a crack at it. I have thoughts here, but I want to make sure everyone has a chance to talk, and since this is your submission, Dmitrii, do you want to jump on that, or is your throat okay?
**Dmitrii Anoshin (Individual – No  Account)** 13:02 Yeah, I'm not sure I fully understand the problem, and how is the VIN currently solved in the profiling sequence, instead of reporting all of those as a resource? Because, like, resource is a kind of higher level, even on top of scope, so you can aggregate as much as possible if you want to.
So, I don't really understand the problem.
**Josh Suereth (Google LLC)** 13:25 Oh, so in profiling, what they do is you have a dictionary that you encode things with.
**Dmitrii Anoshin (Individual – No  Account)** 13:30 Oh, yeah, yeah, yeah.
**Josh Suereth (Google LLC)** 13:32 Most of the attributes. So, like, the sub-resources, only the things that are changed.
**Dmitrii Anoshin (Individual – No  Account)** 13:37 Yeah, I remember that, and it brings a lot of problems in the data processing, essentially, in the collector, because we cannot easily split resources and aggregate them and everything.
Okay.
**Jake Dern (F5, Inc.)** 13:51 We have that problem in Arrow as well, for other reasons, but yeah.
**Josh Suereth (Google LLC)** 13:55 This gets into a little bit, like, if we talk about, like, how resources are used in OTEL, right? Like, the one interesting thing to me is the logical and the physical are blurred together, right? So, the notion of a service name and, like, the service layer is right beside, like, what pod and, like, container ID you are, and they're blended all in the same thing.
But in, if you're thinking of these, like, in a left-hand navigational panel, you would actually, like, have them separate.
And you have this, like, relationship between them. And so what we're trying to do is bridge those two models, because I think the flat version of resource is really, really useful for modern databases, and modern, you know, like, querying across these, you know, NoSQL or, Apache, you know, Parquet-type files and iceberg and all that kind of crap, right? That's the way people want to structure their data.
So… We don't want to force you to change out your databases, but what we want to do is have a layer On top, that lets you have this… resource model.
or entity model, I should say, for how you do, like, your left-hand nav panels, and figure out what to filter ahead of time, so you can write more efficient queries, so you can see things in a different view.
In practice, though, in our data model, that's where it becomes problematic, because we have this thing of, I have a resource, and I need an identity.
Yeah, yeah, I'll give some examples, because I've been looking at, like, DuckDB and, like, ClickHouse and their OpenTelemetry integrations, because I've been trying to look at, like, the more… things that aren't traditional time series or, you know, trace databases, like Jaeger and Prometheus, to get a better handle on how we design OpenTelemetry overall, right? So those are kind of two open source.
databases that have OpenTelemetry integrations that we can take a look at. And one of the interesting things is they're doing, like, they're computing for metrics. They'll compute, like, a city hash across the resource attributes, and that's how they do joins and, like, understand time series and that kind of crap.
With entities, what we want… what we're trying to do.
Is give you the ability to ignore a lot of the fluff in a resource that is for efficient filtering, but is not needed for actually doing time series.
And so, what Dmitri has here with this PR, with Identity Scope, is the ability for us to kind of uniquely identify, here's the exact set of attributes to get an ID that means a thing.
Right?
And I hear what you're saying about contextually, like, how do I… how would I understand the Entity data model if I'm not inside of a resource?
The reality in OTEL today is even when we send, like, entity data model events, those events come from a resource.
**Jake Dern (F5, Inc.)** 16:45 Right.
**Josh Suereth (Google LLC)** 16:46 And we're implicitly putting this hierarchical relationship on them, yeah.
**Jake Dern (F5, Inc.)** 16:51 Yum.
I think that… I'm glad you brought that up, because then I think, yeah, my next question is highly related, and maybe this will lend some clarity, but I… you know, my immediate follow-up was like, okay, then how do I, like, using an entity event, like, leverage this idea? Because it… at least my interpretation of the entity events was that, okay, they're entirely self-describing, and they're not communicating in terms of resource, at least today. Maybe there's, like, some kind of modification or something that we're imagining after this proposal to entity events, or to entity refs, or both.
But, yeah, if that event is not leveraging this, this concept at all, yeah, I'm curious about that.
**Josh Suereth (Google LLC)** 17:33 Can I… can I rephrase the question? Yeah, please, please. So, like, if you have… if I have an entity scope for an entity.
**Jake Dern (F5, Inc.)** 17:43 Yep.
**Josh Suereth (Google LLC)** 17:44 or for an identity of an entity. Then, in the entity event that reports relationships, I would expect the type that my scope is to can somehow contain me in the set of relationships SIG reports. And that there… that needs to be a strong, strict thing. Is that… Is that, like, an implication of what you're asking?
**Jake Dern (F5, Inc.)** 18:05 Yeah, I think I'm asking that question, like, is the entity event itself entirely self-describing, or is the entity event meant to be interpreted in the concept, or in the context of its scope and resource that that signal is attached to?
**Josh Suereth (Google LLC)** 18:21 dmitrii, do you have thoughts?
**Dmitrii Anoshin (Individual – No  Account)** 18:25 Yes, I think we agreed that Entity Events would, keep the data structure, and it would keep resource, as well. So, entity… its event itself would have its local AD.
And, the reference… scope would be part of the resource in that case. That's my initial thought, but I think we need to actually properly define that in entity events as well, so… given that we have entity events data model already defined, the spec, I think that's a good gap.
to highlight.
And, yeah, I think it should be addressed within, probably, this PR.
**Josh Suereth (Google LLC)** 19:15 Yeah, what's the example you've been using, Dmitrii? Because I want to draw this out. I think there's an important thing to understand here. Is it… is it host, the one that we… that is the really problematic one that's relative?
Or is it another one?
**Dmitrii Anoshin (Individual – No  Account)** 19:27 Hmm.
**Josh Suereth (Google LLC)** 19:27 That you've been using.
Oh, you can use a container, right?
**Dmitrii Anoshin (Individual – No  Account)** 19:32 Container, yes.
**Josh Suereth (Google LLC)** 19:33 Yeah, it's relative… And then, it points… does that… that points at pod, or that points somewhere else?
**Dmitrii Anoshin (Individual – No  Account)** 19:41 Yes, it's both, it's pot, yes.
**Josh Suereth (Google LLC)** 19:44 Absolute.
Yeah.
Okay.
So, the thing I want to call out here, and I need to figure out how to draw this, right?
So we have, in our, in our data model, we have this notion of a, kate's Container, and a pod… do I have the… I have the arrow wrong, isn't it? It's the other way, it's runs on, right?
**Dmitrii Anoshin (Individual – No  Account)** 20:07 It's probably the other, yes.
**Josh Suereth (Google LLC)** 20:09 Yeah, okay.
So… Here's… here's the problem that we have right now, is that the identity for Kate's container is not unique. So the only way you can describe it uniquely is if you know what pod it's a part of.
However, when I report relationships for Kate's pod in our event model, what I'm gonna do is I'm gonna say, here's a Kate's pod with its ID, and then underneath it, here's all the containers, right?
Or I'm gonna report, like, I'm a Keats, I'm a Keats, container, and my parent is this pod. Like, I run on this pod, right?
So… no matter… in the event data model, I'm gonna put both of these together.
and give you the relationship so you can follow it to where there's hopefully a unique thing. If I send you an event data model.
that ends on a relative node, this whole, like, this relationship is reported in an event. And, let me… I'm a little bit rough. It's been a long time since I've done, like, shenanigans with Google Drawing Live, so apologies. So, like, if there's an event here, this would be a, Why are you so annoying to use? This is the relationship.
Right? This is good… this gets reported in the context of something. So this is the observer.
So, if, if I end with, with a, like, relative here.
where I don't know the rest of my identity.
In an entity relationship, but I know who's observing it.
And that observer, I can figure out, like, the rest of its chain of identity there. I can… The problem we have that we're trying to solve is this, I don't have a unique identity, and I can't synthesize one that I can observe from outside and from inside.
So, what we're doing, and this is the complexity that everyone has to deal with because of how we modeled it.
Is… we need a way to try to synthesize a unique identity for any particular entity.
The implication of what Dmitrii's doing here is… If I need to talk about this Kate's… oh, let me put this in the back. If I need to talk about this Kate's container here.
Whichever instance that is.
I need to have the pod identity to uniquely identify it. And if I store it in a database, I would synthesize, like, this id… the full ID for that row.
would include both the container name and the pod ID, unique ID, to have a unique ID to store that entity and talk about it individually.
Because I… otherwise I can't.
Right? The ID is relative. The CADS container could be called foo, and there might be a thousand foos across all my different Cates clusters. But since a pod has a UUID, when I put container name and pod UUID, I can now uniquely talk about containers in my ecosystem.
We need that unique ID both for the relationship data model and for the resource data model to, like, understand what the thing is.
So, it… the… This is more about the fact that we have things that are relative IDs, and we haven't… we don't think there's a solution to give them unique IDs that actually works.
Without doing this kind of bridging between two entities thing.
**Jake Dern (F5, Inc.)** 23:50 Yeah. I think the bridging between two entities makes a ton of sense to me. I think where I'm, like, questioning the existing model is sort of the… Like, the… the abstract definition of an entity being defined such that, you know, its ID is either local or global, and it having a relationship to another entity where it gets, a globally unique ID by unioning those attributes makes a lot of sense.
I think… but then, like, defining that, and we're sort of saying, like, oh, okay, you have to have a resource now in order to communicate it. It feels like more of, like, an implementation detail, like, okay, I could communicate an entity that I have efficiently using a resource, and it's unambiguous in an open telemetry signal, because a resource has at most one entity in it.
So that seems like, oh, okay, that's like a OpenTelemetry signal-specific way I can communicate this entity model, but it doesn't feel inherent that, like, oh, I'm not gonna describe my entities in terms of resource, I'm going to say I have a Kubernetes pod, I have a Kubernetes container, blah blah blah. Container is a local thing, I don't need to talk about resource, sort of, to, to lay that out. Does that make sense?
**Josh Suereth (Google LLC)** 24:59 Yeah, yeah, another way to phrase it, let me go back to here, to your comment.
I think… I think the reality is that, like, this sounds too much like it's reliant on resource. What we actually have as a requirement is that to communicate the identity of a relative identity, you also have to communicate the other entity at the same time.
Whether or not that's in a resource isn't the important bit, it's the fact that you have to communicate the two together.
To… to get a real identity.
**Jake Dern (F5, Inc.)** 25:32 Yeah, and maybe this is, like, the most feasible way to do it in the existing, like, OpenTelemetry signals, but it would also be nice to, you know, sort of leave room for, hey, maybe I've got some data model, it conforms to the abstract idea of an OpenTelemetry entity, but… Maybe I have a way to more hierarchically represent it such that, you know, hey, I could have more than one entity of the same type communicated at one time, and have some way to sort of normalize the attributes. You know, we have, like, an endpoint, for example.
On the data flow engine that has, like, status for entities, and then we could imagine, like, that endpoint, you know, you could scrape some JSON or something. It has a representation of the entity model.
**Josh Suereth (Google LLC)** 26:13 Yes.
**Jake Dern (F5, Inc.)** 26:14 Yeah.
**Josh Suereth (Google LLC)** 26:14 Yeah, yeah, that's the idea behind, just, like, exporting the relationships separately.
But you're saying you could scrape it, or push it, or… yeah.
**Jake Dern (F5, Inc.)** 26:24 Yeah, yeah, exactly, exactly. But, you know, not being necessarily tied to the, the constraints of the existing telemetry signals.
**Josh Suereth (Google LLC)** 26:32 Right.
Anyone else have anything they want to say? I know that you have to leave in, like, 4 minutes, so I don't want to hold you too long.
Anyone else have anything they want to add, quick?
**Dmitrii Anoshin (Individual – No  Account)** 26:50 Yeah, I think it all makes sense that we should set them both to get the global idea. I still… it's still unclear to me, like.
If it has to be sent as a relationship, or it can be specifically for NTT events, or it can be… like, potentially set on the resource as well, because if Kubernetes container changes, for example, and pod doesn't change, we don't want to send pod as an entity, as a full entity with it. We just want to set, like, identify and attributes part of it, but more, like, implementation… not implementation, but more… Specific to the… Data modeling to answer this question on, HD events, I guess.
Maybe I'll… I can follow up on this.
**Josh Suereth (Google LLC)** 27:39 Yeah, yeah, I think… I think the… the thing I'm getting from this is we probably, and I don't remember if you have this, let me go to the other view.
It probably would have been easier if I'd done this to begin with. I don't know if… we didn't change the entity event part of the.
**Dmitrii Anoshin (Individual – No  Account)** 27:58 No.
**Josh Suereth (Google LLC)** 27:58 Right?
**Dmitrii Anoshin (Individual – No  Account)** 27:59 No, that's the thing, yes, it's a gap. I guess we probably need to change it within this proposal as well.
**Josh Suereth (Google LLC)** 28:06 Yeah, I think, I think to clarify it, so that we understand the implication of this with events. Yep.
**Dmitrii Anoshin (Individual – No  Account)** 28:11 Right.
**Josh Suereth (Google LLC)** 28:13 Okay, and does this show me your comment? No, it doesn't. Of course it doesn't.
**Jake Dern (F5, Inc.)** 28:17 Yeah, no. Imagine.
**Josh Suereth (Google LLC)** 28:21 conversation.
Okay, so that's a, that's a great to-do, good conversation. You had, you had another, I don't know if it's better for us to read this or read this comment, Jake, while you're still here.
**Jake Dern (F5, Inc.)** 28:37 Probably, I think, just that next one. There's not too much to say, I think about it. I think we already flagged that maybe there's some, some more information we need in the proposal about, how this interacts with events.
The next one there, I, you know, I was just kind of reviewing some of the past discussion, and just raising some observations about, you know, entity relationships, and, just asking the question of, you know, whether or not those relationships would be a decent way to describe identity as well.
I think I had made another comment about it, but just thinking more about relationships and things, you know, I just made another couple observations here about different problems that Relationships seem to solve, or help solve.
**Josh Suereth (Google LLC)** 29:20 Yeah, this thing you call out here is absolutely one of the things I want to use entities for in our, like, V2 prototypes for aggregation. I'd love if we could spatially aggregate by entities, just trivially.
You know, of saying, cool, I want this metric, but I want you to aggregate at the pod level, or the namespace level, or whatever, and we just… we can make that happen in our systems. Yeah.
**Jake Dern (F5, Inc.)** 29:43 Yeah, yeah, I gotta jump. The only last thing I was gonna mention, something else that I didn't find a good place to comment on it here, but I'm curious about is, and, like, our data flow engine, we're… we're trying to explicitly tie every single signal, to an entity, and so it's not, like, entirely clear, I guess, with the existing, like, entity refs, like, hey, how do I know which entity or something, you know, internal or sort of, like, ambient and containing, like, does this signal belong to? So that's something that I'm kind of curious what the thoughts are about.
And then we… I'm about to publish an RFC for the data flow engine, just kind of describing how we're approaching this with the existing OpenTelemetry Entity Model. It'll very much be a draft, but maybe worth discussing and, you know, talking about some of the challenges that we have there.
I think the idea of scope entities that I wanted to bring up a couple weeks ago, but realized I had not done my homework about might be reasonable.
**Josh Suereth (Google LLC)** 30:43 Please, please, share that draft here so we can all review it, because I think that's, that's awesome. Yeah.
**Jake Dern (F5, Inc.)** 30:49 Definitely. Yeah, sorry, I gotta run, but thank you guys so much. I didn't realize we would discuss all this stuff today, but I'm so happy to. This is all very interesting, and I'm very new, so if I'm saying something stupid, just tell me.
**Josh Suereth (Google LLC)** 31:01 No, new perspectives and fresh questions always help us get better design, so thank you.
**Jake Dern (F5, Inc.)** 31:06 Alright, thank you.
**Josh Suereth (Google LLC)** 31:10 Cool.
**Dmitrii Anoshin (Individual – No  Account)** 31:11 And the last question reminded me of the problem that we still had to fix. Like, what's the actual, like.
this more specific entity do the telemetry is associated to that resource.
Remember that, Josh, we discussed that some time ago, and I don't believe we ever… Made that.
**Josh Suereth (Google LLC)** 31:33 No, no, and we… yeah. It's, it's, it's rough because there's, like.
how OTEL is used in practice, like, we… We kind of half care about resources, and then the people who care really care.
And so, we're in this awkward place of, I would say, 50% of people… no, I would say 80% of people just want it to work and don't want to think about it, and then 20% of the people care very deeply and have very specific semantics they want all this to do.
And we're caught in the middle.
So that one, that one is a, anyway, okay.
Let's… let's go through the rest of the questions here. Was there another… was there a hand or anything? No.
Alright.
I have strong feelings about this. This is in Prometheus.
When Corleyan signals, knowing what should be used for identity seems useful, local versus global.
Left-hand navigation, though. Yeah, left-hand navigation isn't the… Okay, this here, to answer this question, krajo, the… the thing that Dmitrii is solving is in left-hand nav, it's so that you can have each item in a left-hand nav have a unique identity, so you know when there needs to be two versus one.
So, like, if you're grouping in that fashion. So it's like knowing that, actually, this container is a different container than the other one, and we don't really know if they're the same.
Just by the Kate's name, for example.
**krajo (Grafana Labs)** 33:07 Yeah, in my head, Left-hand navigation is a way to kind of show you a hierarchy, right?
So, in my head, I would imagine that I can have… the, like, Kubernetes cluster on top, then, I don't know, node, then con- pod, container, blah blah blah.
But… The globals and the unknowns are kind of… Throwing that off.
So I feel like I will end up having to have some extra knowledge anyway. Like, this is not going to be truly self-contained, but maybe that's right, I'm just, you know, pointing that out.
**Josh Suereth (Google LLC)** 33:49 So, I see what you mean. Yeah, the… in context of this particular PR, and what we were just saying, without the relationship signal, building the left-hand nav is kind of really, really hard or impossible, because you need extra information.
So, if you take this identity plus the entity relationship signal, then you can build a left-hand nav.
**krajo (Grafana Labs)** 34:11 Oh, yeah, I haven't looked deeply into the… relationship signal, so the events, I think you call them, right? Entity events?
Because you said that we don't need them in Prometus. And to be fair, we don't need them in Prometus, like, it's more of a UI thing. And actually, there is a… some thinking in Grafana about, yeah, the, you know, storing semantic conventions, and probably then this data in a common place outside specific databases, because they will be relevant for everybody anyway.
So, yeah, okay.
But that's… that's clear to me that this is not… That… that specific case isn't in scope here, basically.
**Josh Suereth (Google LLC)** 35:00 It's… it should be supported by this PR, but it's not the purpose of this PR, yeah.
**krajo (Grafana Labs)** 35:04 I see. Yeah. Okay, fair enough.
**Josh Suereth (Google LLC)** 35:07 Okay, let's go into this one. This doesn't seem… this is about the scope of the ID, from how the ID is generated, not from where the system that assigns it documents its guarantee.
Treated Diaz Global Inc.
**krajo (Grafana Labs)** 35:48 Yeah, I just want to say that I learned the hard way that You know, if you write something in the documentation, people tend to… depend on that, and give you problems when you don't do them, so I think… I think it's fair to say something about the documentation here, and, you know, what it… what the actual thing is doing, what's the de facto uniqueness of something, but… I… I think it's… it reads a little bit strong to… to me to… to just ignore the documentation, basically, and do something else. Like, I think it's fair to say that You know, if the implantation de facto gives you like, more uniqueness than the dog, then that's fine, but I don't think… like, this would… seems to open the door to do something that's less specific, less unique, and then I think that's bug, either in documentation or somewhere.
So, that… I would just rephrase this a little bit.
But otherwise, I wouldn't remove it.
**Josh Suereth (Google LLC)** 36:51 Yeah, so to rephrase what you're saying is the, If we get an ID that is global, we should not mark it as local or unspecified.
**krajo (Grafana Labs)** 37:04 Yeah, I think that's fine, even if it goes… I'm specifically talking about, you know, the relationship between what an entity is declaring as global, and whether the documentation of that thing in, like, in Kubernetes says, no, it's not global. Like, that's… that's a conflict between the documentation and the entity, right?
**Josh Suereth (Google LLC)** 37:26 Yeah.
**krajo (Grafana Labs)** 37:27 But then… and I think… If we know for sure.
that, yeah, it's global, and the documentation is kind of shy about it, or whatever, then that's fine. But the other way around, it's probably not fine, so… And reading this text is saying that, oh, you can basically ignore the documentation. I think That's a bit too much.
**Josh Suereth (Google LLC)** 37:52 I see.
I think… Yeah, we should rephrase this, but I… Dmitrii, tell us what the… you can tell us what the intention was. The way I read this was that the… you shouldn't, like, read ketst.pod.uid and just assume it's global. You should, like, if this is marked as local, and it says it's a UID, that means treat it as local. Like.
The ultimate authority for whether you treat it as global or local is the flag that we set on the data model.
In the thing, like, you don't have to go read docs. I read it, like, the inverse of what you're saying, right?
**krajo (Grafana Labs)** 38:30 Doctor.
**Josh Suereth (Google LLC)** 38:35 What was the intention here, Dmitrii?
**Dmitrii Anoshin (Individual – No  Account)** 38:39 Yeah, I guess it's that we should, see what's the… what we said… on the… on the wire. Instead of looking at semantic conventions, that probably was the… was the intention here.
Or is, another note? Let me check. Sorry, I just… I got dropped.
**Josh Suereth (Google LLC)** 39:04 Yeah, no worries, no worries.
Yeah, this was the other important bit, which, like, I know that you're focused more on the top bit, which is just…
**Dmitrii Anoshin (Individual – No  Account)** 39:14 Oh, okay.
**Josh Suereth (Google LLC)** 39:14 Don't guess. Like, if you have an ID and you don't know if it's global, don't say it's global, just mark it unspecified, right?
**Dmitrii Anoshin (Individual – No  Account)** 39:26 Yeah, here the point mostly is that, Like, you… Kubernetes use your ID, and it makes sense to… it may make it as global, because UAID, we can… To some certain degrees, be confident that they are globally unique.
And, even if, potentially, somewhere, it can be stated that they can change within Kubernetes cluster. And it's just a note specifically to that use case, like, when… when you… if you want to make UUID of Kubernetes within… unique within the cluster, like, make them local.
you… there is no really good way to do that, because KTAS cluster also doesn't have… also uses your UID, which is part of Which is generated.
which is taken from cube system namespace name, which is also UID, so, like, there's no… A real, really good way to… to make that… more… Globally unique than it already is.
So, sorry for Emlin, that's… Boost.
Pretty much the idea.
**Josh Suereth (Google LLC)** 40:49 Okay. It sounds to me like we should reword this, then.
Because the, like, the way you're phrasing it, I understand, I think this needs to stay of, like, don't guess if you don't know.
But the way, the way it was interpreted, so, yeah.
Okay, let's take an AI to rephrase this. I… didn't capture what you were saying while you were saying it. I probably should have in a comment, so apologies.
I might grab the transcript from this and pull it in, or if you remember, take a crack at that, please.
Okay.
I think this is the last comment to go through.
Component must not set or modify either field on an entity it did not produce.
Program exposes its own identity, but doesn't know or bother to implement detecting where it's running. BK for its container overwrite unknown scope with its own scope.
**krajo (Grafana Labs)** 41:52 Yeah, I'm not… I don't have a strong feeling about this, actually, but it's… I imagine the case where somebody Does, like, a quick job of it, and… Either that, or just doesn't know. And then we have this weird association that Look, a human looks at it and that, oh, it's obviously inside something, but the entity model is just not capable of reflecting that.
**Josh Suereth (Google LLC)** 42:19 I think the intention here is that if you are doing detection on behalf of someone else, and it gave you, like, a half-assed entity.
you can just blow it away and put a new one in. That you're like, no, this is who you are.
Right.
**krajo (Grafana Labs)** 42:35 Oh, you mean that… Like, somebody… Does some very… very… something very simple.
Provides an unknown thing, and then you generate a new… from that, just take it and… Hmm.
**Josh Suereth (Google LLC)** 42:50 Right, right, like, but the idea would be, you were producing, like.
you're basically redoing the resource detection, if you will, or the entity detection, and saying, no, here's what you are, I figured out who you are, here's what you are, I'll stamp it on top.
Right?
That… that's like a… kind of like an advanced use case we have, but the idea would be, if I… if I don't know who you are, and you're coming through.
and I get this entity, I don't touch it unless I know. And if I know, I'm gonna blow away what you have and put in the, like, real thing, you know?
**krajo (Grafana Labs)** 43:26 yeah. Is that something that we want to add in the text, then? Because I didn't think of that, but… I mean, and by that, I mean this idea that… but it is okay to just generate a new identity.
Basically.
**Josh Suereth (Google LLC)** 43:46 Yeah, I don't know, what… what do you… like, Dmitrii, do you think we should add, text on that?
**Dmitrii Anoshin (Individual – No  Account)** 43:55 So instead… instead of editing a different entity, we generate new ones?
**Josh Suereth (Google LLC)** 44:01 This would be the idea of, like, somebody reports information about themselves that's kind of like.
somewhat broken, but let's say I'm the collector, and I'm using the Cates attribute processor, where I use the IP address to look up your real entities, and I'm gonna stamp them on. And I have an upsert, so I'm gonna force them in anyway. That should still be allowed, right? We're not, like, this rule is not saying you can't do that.
**Dmitrii Anoshin (Individual – No  Account)** 44:25 Right.
**Josh Suereth (Google LLC)** 44:26 Right.
**Dmitrii Anoshin (Individual – No  Account)** 44:27 I think it should be part of entity merging algorithm that we already have, isn't it? I remember we have some cases described there.
Like that, right?
**Josh Suereth (Google LLC)** 44:39 Yeah, I think that you're right, this would be… because what happens is, if you report the entity, because of the way you specified this.
The new entity from the collector will conflict with the old one, and if the new one has upsert, it's higher priority, so it'll blow away the previous one.
And replace it.
**Dmitrii Anoshin (Individual – No  Account)** 44:56 Yep.
**Josh Suereth (Google LLC)** 44:57 Yeah, okay. So this is handled with Entity Merge.
**krajo (Grafana Labs)** 45:01 Okay, I'll take a look. Okay. If you can make a comment so I don't forget.
**Josh Suereth (Google LLC)** 45:05 Yeah.
**krajo (Grafana Labs)** 45:06 Thank you.
**Josh Suereth (Google LLC)** 45:07 this.
This is… this envelope button.
Let's see, merge. Simple, example, deployment… reports a, or… you know.
Each container, or, it's pod.
Not 9, come on. It's pawn with, entity Scope, it's not.
Specifying… What your best keeps attribute processor.
Installed and used to really be… Entities via IP local.
P-dress lookups.
on the pods, collector, hang on.
absurd.
Entity… With conflicting identity.
bored.
algorithm.
What is the, lord.
System. Okay.
Right.
Either as comments, And I think that's everything for… For this, we have a few things… we have this one, this thing to clarify, we have this to clarify, and I know, Dmitrii, you are heading to a new job, so let me know what you want to pass off, or what you have time to do.
**Dmitrii Anoshin (Individual – No  Account)** 47:02 I can follow up offline on all of the comments here. Maybe I'll take another pass offline, but unlikely I'll be joining the SIG going forward, and will be actively involved. It's also unclear, maybe it will change going forward, but for now, I would say that I will not be.
I have to enroll, so… but I'll try to wrap this up to some extent, so… I guess it's pretty close, right? If I address all the comments, and I'll be responding offline to the feedback.
should be…
**Josh Suereth (Google LLC)** 47:35 Yeah, I…
**Dmitrii Anoshin (Individual – No  Account)** 47:35 to…
**Josh Suereth (Google LLC)** 47:36 I think it's very close, personally, yeah. So if you can respond offline, I think we could talk about it even tomorrow at the Spec SIG. And yeah, like we said last… like, 2 weeks ago, we're gonna miss you, man.
Hopefully.
**Dmitrii Anoshin (Individual – No  Account)** 47:47 Thank you, I'll go in.
**Josh Suereth (Google LLC)** 47:48 If it's your company, this is their top priority.
**Dmitrii Anoshin (Individual – No  Account)** 47:51 We'll see. Vietnamese as well. It was amazing, Jordan.
**Josh Suereth (Google LLC)** 47:56 Okay, alright, we have, we have, like, 10 minutes left. I wanted to kind of talk through next steps to get to, like, a beta or an RC from our current set of milestones. So, if you want, I can pull up the project, Where we can see what we had listed previously.
But this is, for context, this is around the resource entity mapping phase and trying to get this into a state where we feel like we can, start marking things, as… the next… you know, life cycle level. Actually, what I should do… just to remind everyone, because I don't know if everyone here is as familiar with spec processes, let's go through the lifecycle thing quick.
Is it in here? Oh, here's maturity levels.
Okay, so we are currently in development, which is that not all pieces are in place, might not be available for users, bugs, performance issues are expected, etc, etc, etc.
Alpha is where the default level for components with no explicit maturity level should be assumed to be alpha.
Component is ready to be used for limited non-critical production workloads, and authors of this component welcome feedback. Bugs and performance problems are encouraged to be reported. Components might not work on them immediately, but our interface configuration options might change without backwards compatibility guarantees, etc. I think this is a pretty low bar.
I would like to get to beta.
where we start to treat some of our stuff as stable, I don't think we're there yet, but what I wanted to have a discussion of is, is there anything outside of Dmitri's PR which I think we need to get through, and do all the follow-through on his PR?
That we consider blocking for marking our current state as alpha.
For context, I can go back to the Entities list, and we can walk through issues that we have reported, and issues in our backlog, and we can decide if there's anything we think is a, an alpha blocker. Otherwise, I'd like to start moving towards, marking the specification, marking the proto changes, all that is alpha, so we can start, you know, progressing down the ranks. Okay. So, support for new resource entity references, proto-Message, that is, Dmitrii, that's part of your PR, right?
Or no, this is the overall collector work, right?
**Dmitrii Anoshin (Individual – No  Account)** 50:30 Yeah, this overall collective work, and I have someone from my Splunk's team to help with that, so hopefully they will be able to continue.
**Josh Suereth (Google LLC)** 50:40 Pick it up, okay.
Cool.
Right.
We have the SDK startup specification from, Nope.
We moved it off the declarative Config Board.
I think this one actually… Didn't… didn't we land the spec BRs from Dan?
Were they just not accounted to this issue?
I'll take a look, because I think… I think this is merged, if I… if I recall correctly. I thought… I thought, Dan sent a PR, and we merged it.
For startup issues.
Okay.
Strategy for asynchronous, yeah, because he did start up an asynchronous at the same time, and there was a PR that was merged for both.
I thought. I'll take a look.
Alright, and then show demo of how collector processors differentiate remote and local.
This was… we wanted to do a demo.
Do we have that demo, Dmitrii?
**Dmitrii Anoshin (Individual – No  Account)** 51:57 Not really. I don't think so.
**Josh Suereth (Google LLC)** 52:00 Okay.
I'm gonna assign this back to me, if that's okay?
**Dmitrii Anoshin (Individual – No  Account)** 52:04 Yeah, sure.
**Josh Suereth (Google LLC)** 52:06 Okay.
I'll take a look at what we have and see if I can put a demo together for… because I think this would, what we can do is we can do a demo of what is live with what's in Java and what's in the collector, and then we can, We can use that to determine if we go to alpha.
How's that sound?
**Dmitrii Anoshin (Individual – No  Account)** 52:26 Sounds good. Thank you.
**Josh Suereth (Google LLC)** 52:28 Okay.
Cool.
We'll walk through… those are things for entity as a signal.
Spence Conventions for Virtual Machine Resources. This is, I think this is starting to make some progress.
Already.
No, this is different. This is ESX and Hyper-V, and all those crazy things, and Proxbox, and… yeah. Okay.
That is… I don't know if that's a blocker for this, but that's an interesting one. Classes of entity types.
Do we need to differentiate between infrastructure and logical entities?
**Dmitrii Anoshin (Individual – No  Account)** 53:16 I think that's maybe… if it's a concern, it's definitely not blocking, and it should just go to, like… In semantic conventions as a description, probably.
**Josh Suereth (Google LLC)** 53:29 Yeah.
**Dmitrii Anoshin (Individual – No  Account)** 53:29 Does that make sense? I don't believe it's needed for a product or anything.
**Josh Suereth (Google LLC)** 53:35 No, and I think we have enough design flexibility in the future, given what I've seen you do with the identity scope stuff, that we can actually layer this in without breaking people.
**Dmitrii Anoshin (Individual – No  Account)** 53:46 Yeah, it's probably would end up on relationships if we want to.
differentiate.
**Josh Suereth (Google LLC)** 53:54 Okay. Clarify cross-telemetry journeys. We call it potential interaction with metrics, consistent signals. Larger question for our expected users to interact in today's architecture.
someone who's leaving OpenTelemetry with Jaeger for tracing, Prometheus for metrics, and Elasticsearch for logs, where should they be sending the entity signal? This is the entity relationship.
This one, I think, has some interesting answers today. Like, there's an Apache project for consuming the signal and actually surfacing a queryable API for it. I don't know if you saw that.
It was in the chat. So, it's literally like a data store that stores the entity relationship signal.
**Dmitrii Anoshin (Individual – No  Account)** 54:32 Interesting.
**Josh Suereth (Google LLC)** 54:33 Yeah.
I'll see if I can find a link for that. I… I don't think this is a blocker for Alpha. I do think this gets into getting more beta… for beta, I'd like to see more demos and actual, like, architectures and user guides and that kind of crap, you know, like, telling people how to use it.
Mdatagen generate links to configuration interface for metric scrapers. This one, I think a lot has changed in how mdataGen and stuff work. Is this still something we need to do?
**Dmitrii Anoshin (Individual – No  Account)** 55:03 It's, actually been worked on by one of my… previous team members, I did that for Entities… entity references, so currently you can control entity references already and emit them, but entity events is probably something else.
okay. Yeah. Actually, maybe we can even close this one, or… generate… Anyway, yeah, I believe we already sent Entity events from that receiver, and it would make sense to make it, like.
Entity… control entity from the same configuration interface that is being generated by MDGEN, if that makes sense. Mdata Jan allows you to generate config… user configuration interface, where you define, disable this entity, enable that metric and everything.
**Josh Suereth (Google LLC)** 56:02 This gets into some of the other cool stuff I wanted to build. Yeah, I don't think this is a blocker. If you think.
**Dmitrii Anoshin (Individual – No  Account)** 56:07 Yeah, press start.
**Josh Suereth (Google LLC)** 56:08 Could have moved it to in progress, but yeah, that's cool.
**Dmitrii Anoshin (Individual – No  Account)** 56:11 It's definitely not a blocker for the phase one.
**Josh Suereth (Google LLC)** 56:14 Yeah.
**Dmitrii Anoshin (Individual – No  Account)** 56:15 I would maybe remove it from the board if… If that makes sense.
**Josh Suereth (Google LLC)** 56:19 Oh, yeah, I can just remove it from the board, remove it from projects.
It's still a cool idea, and I'm glad someone's working on it. Okay.
This was about merge logic preventing fine-grained resource detectors. This is around the Go implementation.
If you remember this one, this is where Go wants to detect one res… one attribute at a time.
And, like, this is… man, wow, a long time ago. I think we can solve this and go, we just need someone to build a prototype. Dashpole had a prototype, Interesting. I will, and then there was… I'll follow up with, the GO SIG on this, and see if we can get, reboot the prototype here.
I think with, with the changes that were made for configuration-based SDKs.
I have a feeling that the whole situation is, is, like, different. So, I'll follow up with that. I don't… this is a blocker, actually.
for, I would say, beta, but I don't think for alpha.
I'm gonna move it into here, and not here.
Here, and we'll track it going forward.
Last one… Hotel Entities and maturity level.
Hmm… Oh, this is… they want… they want it to be considered experimental.
I think we had a bunch of discussions about this one.
And I think the… what we resolved on… I'm gonna move this over, and I know that we only have one minute left, so we probably don't have time, but just for context, I think what we did with this… and Dmitrii, I know you had concerns, so I want to make sure those get addressed, but, inside of OTelconfig, if you specify the env resource detector, it will look at OTEL Entities, and you have to manually add that for now, it's not on by default. So we don't have a path to have it on by default right now, we have to sort that out.
I think that's okay for Alpha, we need to figure that out for Beta, I would say. I'm gonna move it into the blocking list.
But I also don't think I'm gonna have that as a blocker for beta, so I'm not gonna move it… or Alpha. So I'm not gonna move it in progress.
I think these are the things for… in progress that we work on before we mark entities alpha.
And I'm gonna put that as a straw man out for it. If anyone has concerns around this list or marking alpha when this list is done, let me know. Otherwise, I'll put some updates and send out notification to people and open some PRs around that.
How's that sound?
**Dmitrii Anoshin (Individual – No  Account)** 59:37 Sounds good.
**Josh Suereth (Google LLC)** 59:40 Cool.
Alright, thanks everybody. Hope you all had a good KubeCon, and that you recover from KubeCon soon.
**Dmitrii Anoshin (Individual – No  Account)** 59:46 Yeah, thank you. Hey folks, bye.
**Josh Suereth (Google LLC)** 59:49 See ya.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 59:50 See ya.
