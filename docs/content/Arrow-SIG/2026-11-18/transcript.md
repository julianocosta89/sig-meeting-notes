SIG: Arrow SIG
Date: 2026-11-18
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Laurent Querel** 00:49 Through Pierre.
**Pierre Mariani** 00:50 Et l'en serious.
**Laurent Querel** 00:52 But et cetera.
**Pierre Mariani** 00:57 Oh, cool. Nikhil.
**Laurent Querel** 01:06 mais je vu changer.
Les contributions sa pas, mais je le conne pas l'avoir en contrait qu'u venue a Seattle en contra l'equipe le reler.
**Pierre Mariani** 01:19 Bonsai au coin.
**Laurent Querel** 01:23 But… Hi, everyone.
**Pierre Mariani** 01:26 Hey, everybody.
**Tatiana Ermolaeva** 01:34 Hello, you can keep going, it sounds great.
**Laurent Querel** 01:39 Okay, I think we… we are waiting for more people, I can share my screen.
Let's see what… No, that's not what I want to share, sorry. What annoys?
Here we are. Okay, so do we have, Josh MacDonald with us?
Not yet Okay, so first, I encourage everyone to… Add their name to the attendees list here.
We already have a big agenda.
So, I think we have, probably more than what we need.
And I think we can, maybe start on the triage aspect.
Probably be faster than usual on this part, and then move to the values topic.
Okay, so let's start with the… So yeah, we are on the… yeah, okay, need, triage need discussion. Header capture support for RFC… HTTP extension, I think that will be something from Josh.
So there is a big effort right now on, the PDATAC context, header based on HTTP headers.
Based on, security plan and other things like that.
I don't think it's, necessarily to discuss that. It's definitely important for us to support, contacts coming from outside.
Not hesitate to, add, additional, Information, if you think that there is something interesting about this topic.
at OTLP event, receive rates, Geneva Exporter, do we have with us, I'm not sure how to pronounce… Sata, or… So let's open that… But tell Arrow that F1 gene dashboard does not display OTIP event receive rates, Geneva Exporter. Okay, it's about more instrumentation. It looks like it's more specific to the Geneva Exporter.
Again, I don't think it's…
**Drew Relmas** 04:31 comment down at the bottom, that I think this can be answered with the generic metrics, the shared metrics we already have. So, Josh, I'm not sure if we meant to add needs discussion here, but…
**Laurent Querel** 04:43 Okay, yeah, definitively, we are encouraging people, definitively, to look at the existing generic metric, and when There is a good match to use that instead of creating new ones.
That's definitively great.
Thank you, Drew, so let's remove the… We had, constant output log lines at shutdown are suddenly dropped after the right door closed.
Yeah, I think we already did, some improvement in this space that looks like it's, Categorized as a bug.
Do you have any, insight, on that, Drew or others in the… on the… Microsoft side.
**Drew Relmas** 05:33 I don't think so. I know we've made a bunch of improvements there, like Josh just did.
Josh also had a needs discussion. I'm not sure what he was thinking.
**Joshua MacDonald (Microsoft)** 05:44 Okay, anyway, I don't think it's… My last comment on this issue was that there was some… The added complexity of the solution proposed in, The PR link there, 4375, made me feel uneasy about the feature itself.
**Laurent Querel** 06:02 Oh.
**Joshua MacDonald (Microsoft)** 06:03 How do we flush a log at the end of the process lifetime? I don't have a good answer, and I think we should talk about it.
**Laurent Querel** 06:10 Okay, so let's, so, yeah, maybe… Went a little bit too… First… So I will, keep this one open and take the time to look at it.
**Joshua MacDonald (Microsoft)** 06:28 Thank you. It's not a big deal, I will say that, but… but I couldn't approve the PR that was proposed without more discussion.
**Laurent Querel** 06:37 Okay, so I will let open this one, and maybe we can have this discussion on the hotel element now.
Shouldn't on smoke.
**Joshua MacDonald (Microsoft)** 06:45 Sure.
**Laurent Querel** 06:46 Okay.
So, the stems, so, Josh, I was saying that we have to be very fast on the…
**Joshua MacDonald (Microsoft)** 06:54 Yes.
**Laurent Querel** 06:54 Classic initial triage, because we have so much I don't think we will be able to address everything there, but let's try.
Still, so status conditions semantic for intentional pipeline.
I see what it is, Yeah, I think we are not entirely… I mean, we… we… probably, if I remember well, we fixed some of those, some of the elements, so I don't think we've… we… fix everything there, so I will, for now, remove the stale.
For me, it's still something on which we need to… Finalize the… The fix, revert commits in future, when next we were…
**Drew Relmas** 07:47 This is probably old, considering it's from May 11th. We've definitely… it was probably a cargo denied type thing, which I did another update of them this morning. I'm pretty sure we can close this.
**Laurent Querel** 08:00 Okay, yeah.
Right.
Implement staff protocol.
Yeah.
**Joshua MacDonald (Microsoft)** 08:10 I haven't heard anyone ask about Steph in a while, say that much.
**Laurent Querel** 08:16 I still have this, open, branch on this staff experiment.
Yeah, I agree. For now, we didn't get any, Ask for it.
I think, to be fair, it's probably something interesting. Personally, I will remove the style. It's definitely not a top priority, but I think that's something that, at some point, we should, integrate.
What do you think? Yeah, it looks like you are in agreement with me?
Use Weaver, life check, and CI to ensure, yeah, that definitively is something we want to achieve.
And, in fact, there is, currently, a branch where I have some, Make some improvement, in this area.
So it's definitively not sterile.
I stone… Yeah, so I think that that is one of the topics that we need to reopen to In a slightly different context, but… In fact, related to this future discussion that we have.
to have with the governance committee.
We had, Josh and I, we had a lot of discussion during KubeCon with various persons from the governance committee.
From the OpenTelemetry.
And we definitely need to have, another set of discussion and… defining the… how the… our project is, positioned against the GoCollector.
So that, will be redefined.
Maybe we can close this one.
And reopened based on the conversation. What do you think?
**Joshua MacDonald (Microsoft)** 10:15 Yeah, there is an issue about declaring Phase 3 and what the scope might be there, and you're right, we did talk with quite a few people that seems like there's generally becoming a platform of support for So I would call it the side-by-side build of OpenTelemetry, where you have both a collector and a data flow engine, capable of being built and started Essentially, through the same… distribution pipeline, or just release schedules, and so on. People like the idea, but we… I think we should call it Phase 3.
**Laurent Querel** 10:51 Yeah, okay, so, Okay, so I'm not closing it, just remaining the still, and we, we will, use that as a basis for Phase 3.
some elements are already implemented, and we, we figure out what needs to be part of Phase 3, what could be done later.
Okay.
Honestly.
I think we were at the end of this study list, yes.
Okay, next one… Need deciding which is the last one.
I don't think we will do everything there.
So that's the new… GitHub issues, Is there… Let's sit up here. I took a look at.
**Joshua MacDonald (Microsoft)** 11:56 this list earlier. I don't think we have anything urgent or… that needs to be called out right now.
**Laurent Querel** 12:01 Okay. Just a lot of…
**Joshua MacDonald (Microsoft)** 12:02 Work orders, basically.
**Laurent Querel** 12:04 Is there anyone, that wants to discuss something there?
Otherwise, like suggested by Joshua, we would move to the… To the various topics that we want to analyze today.
Okay, so go back here… Agenda. So, on my side, I have two topics. They are not super urgent, but one is… an idea, I think we… we start to have a nice momentum around this project. We need to be a little bit more visible.
We already have an OpenTelemetry.io blog.
But those… this blog is… is something that is, in my opinion, something that we can use when we have a big announcement.
It will be interesting to have our own more technical oriented.
Blog that could be part of the project.
So we can discuss that. The other one is what we just discussed regarding the future conversation with the governance committee.
I did the first, improvement regarding the landing page.
Just to… put the focus on what we really do today, the focus on the engine itself, and less on the various phases of the project, where we, that was present in the previous iteration of this REME.
a landing page.
I think, it was about the policy, the policies, Albert. I don't know if Albert is with us.
entities, so is there any, Topic that, you think are more important?
Honestly, I don't have any preference.
**Joshua MacDonald (Microsoft)** 14:03 Well, I put the link in policies just to give, like, since we were… some of us were at KubeCon last week, we did have a lot of conversation about the OpenTelemetry Policies proposal, and I was surprised upon reviewing the open PRs today that there are already some… there's already been some work.
on a pure Rust implementation of that. So, stepping back, I think probably not everybody in the room knows what the policies proposal is, and that's been around for more than a year, I think, but has been an interest of Google and at least one other company.
And this is essentially… Calling for a… I guess, more comprehensive transformation language for OpenTelemetry signal data.
That's how I would describe it.
And, there's been an emphasis on allowing composition of You know, thousands of rules in a single processor, or… and also having the ability to push the implementation of the policies as far as you can.
Or put it into different locations. So you can imagine implementing a policy in the SDK or in the collector, for example. So this has been underway for a while, but it just seemed like recently we got a lot of attention from Google, and this is something Google is passionate about, and so here we have Essentially, proof that we can do this.
**Laurent Querel** 15:29 Yeah, and I think it's a very good fit for this engine.
Because the… the overall… I discuss a lot with, with Josh and David Ashbold and Jacob Aronoff.
About those policies during KubeCon.
Not research, but not research during COVID before. And, definitively, one of the… The main driver, or beyond that… is, performance. They had… They had to find some solution to apply many, many Publish thousands of policies, on telemetry streams.
So how to… Let's say, compile, figure out what are the shared conditions across multiple policies, and figure out a way to apply them efficiently.
And it's definitively a nice fit for the… the OTAP model, because we have a columnar-oriented model, and… And we could, definitively.
accelerate the matching of those, various conditions without traversing a big, gigantic, Object 3.
And we already have, some, pre-benchmark that, Mr. Albert did, and then, we… looks like we have, another, attempt, in the same space on, David Dashboard, which is one of these guys from Google.
Doing also a lot of benchmark.
I don't know if we have the, do we have Albert with us?
**Albert Albert** 17:12 Yeah, I'm here. Okay.
**Laurent Querel** 17:14 Albert, I'll let you maybe talk a little bit more on the work that you lead on policies.
**Albert Albert** 17:20 Yeah, sure. So, I haven't had time to go all the way through David's PR yet, but I took a stab at implementing the, the, an engine that can execute these OTEP policies. Interestingly, the OTEP is number 4738, and so is my PR, so that is a incredible coincidence.
And I opened the PR on Friday the 13th.
**Laurent Querel** 17:46 Yeah.
**Albert Albert** 17:47 this way.
Yeah, so, So there is a, already a Rust implementation of, of something that can execute these policies called PolicyRS, and as a… and if you… yeah, this is the crate.
And if you scroll down a little bit on this… on… on the mysterious PR that I had opened.
You can see that, like… Ethiopia, or…
**Laurent Querel** 18:13 or you're,
**Albert Albert** 18:14 My PR, yeah. If you scroll down a little bit on this one, you see that we basically blow it out of the water in all the categories. And then, so the PR that David opened is actually even better and faster than this attempt that I did. So, we're gonna have a really good policy engine here. I need to review David's PR tomorrow and just, you know, understand… understand how it works, but… Yeah, I'm not really sure, what else to say about this. It's, it's… we've got two work in progresses and good performance either way.
**Laurent Querel** 18:53 Yeah, it's… I think what we could say… oh, Joshua, you want to say something before?
**Joshua MacDonald (Microsoft)** 18:58 Well, I sort of have a remark that's a little bit of a tangent. Why don't you go ahead, Laurent, first?
**Laurent Querel** 19:04 Okay, so, I think, I'd like to mention two things on those policies.
So, first, I think, There is, part of those policies, there is, renailing policies.
Which are already supported in this, in this PR. They are the kind of very fundamental set of operations that, in fact, anyone needs to use to do some schema migration. And, with the discussion I had with, Trask.
We determined that having a very good support for that will be extremely valuable for the project.
And also, we'll be a very good demonstrator of why it's so important to have an end-to-end representation, which is columnar-based, because we can definitely leverage this representation and get him a very huge speedup.
The third one thing is… The philosophy behind these telemetry policies.
In the collector, the GoCollector, or in the data flow engine.
the configuration is based on a DAG, so we have a… A bunch of receivers, processors, and connector, exporters connected together, forming a graph.
In our case, we support live reconfiguration, which is nice, but it's not the… the way that those DAGs are designed, the idea is not to update them every 10 seconds.
we offer this flexibility in the data for engine, but it's more when you have a complex reconfiguration of the DAG itself that you want to live or configure it.
The, the PUDYC are, intentionally, small objects that are self-contained, and you have a bag of policies, and this bag of policies could be Let's say, this bag could belong to the security people, or to data quality people, or privacy people.
Or database people. So they… you could imagine the way that those chemistry policies are designed, you could have multiple, source of policy set.
And, with their own life cycle.
And really, the idea is to have, a collector slash gateway, sending, requests to those different, providers of policy sets.
And when there is something new, you download them, they are compiled, combined together with some rules in terms of composition, and then you don't have to update the entire DAG. It's just a new set, and it's implemented either by a telemetry policy processor, or integrated into the transform processor with the OPL language. There is a proposal in the GitHub it's an issue I initially created to initiate this effort.
So that's… that's very interesting, because it's… it's more a dynamic approach to work configure pipelines without changing the… the topology of those pipelines.
Bonsai?
**Joshua MacDonald (Microsoft)** 22:32 Yeah, so I was gonna add that, let's see, so the spec came from this company called Taro, you can see the link to Taro's spec there at the top. I just wanted to pass along that, that that was a very small company, and it has been acquired by a larger company in our industry, so that… there's definitely becoming more support for that… for that system. It was Cribble that has purchased Taro, as far as I know.
**Laurent Querel** 22:57 Yes.
**Joshua MacDonald (Microsoft)** 22:58 I wanted to add a tangent that's quite related, and I'm going to throw it out right now. Here's a link to an issue I filed this morning. And if you're following, you may know that Prometheus has taken an interest in our project, and it's really great to see such progress. So this, So the contributions that we've had already in the past week and a half or so have added a Prometheus receiver, and I filed this issue asking for something that turns out is already almost implemented. So if you're familiar with Prometheus.
The relabel configs and metric relabel configs are the same structure, but they are applied at different points in the pipeline. So the relabel configs is something that only a receiver kind of cares about. This is taking what comes from service discovery and turning it into targets.
And then what happens is, after the target is scraped, the resulting metrics are passed through the same translation again, called metric relabel configs.
And when I was filing the issue, it occurred to me that in our philosophy of the hotel era, we've tried to decompose functionality into the pieces that exist.
In the case of this metric relabel configs option for Prometheus, it is really a generic metric translation library. It's just taking, you know.
a bunch of relabeling rules and applying them all at once. So I see a strong connection with policies, and I was asking Bartek in this change. I put two part… a two-part question here. He answered my question quickly that that, in fact, this is implemented, but it's implemented in the REST code that does the receiver scraping logic, and I wouldn't object to seeing a standalone relabel config, metric relabel config processor.
And then my question becomes something like, do we benefit by using, could we benefit by having a OTEP native implementation of metric relabel configs? And is this starting to blur into other translation library support that we have?
It's not very different than OPL or OTTL, and it's not very different from what I'm seeing of policies either, in that… so I kind of see it all moving towards a… processor, I guess, except that traditionally, Prometheus has done this on its own, and it wouldn't become an OpenTelemetry processor.
**Laurent Querel** 25:25 Yeah, I totally see the… The… the relation between these two things, and we… I think we… it's not because, Prometheus was doing something in one way that we necessarily need to do it, the same way inside the hotel project. We did that many times. We… we… when we see a good, A nice benefit of externalizing something in order to To be more modular, and… Compose a specific function with, other things.
in order to then multiply the effect, we are, I think, trying to do that every time. We did that, for example, for the codec infrastructure, and codec can be used now by a different receivers.
And it's not… it's no longer, oh, you are integrating, Kafka receiver, a C-slug, receiver, or whatever receiver, even a file but receiver.
we can compose with the existing codec and no longer creating or reinventing the wheel each time. I think that's exactly a similar thing. If we are spending the time If we are putting effort to implement very efficiently those policies.
Then we need to figure out a way to call those policies, and part of those policies are about renaming matrix.
We need to figure out a way to reuse those, this integration, deep integration into a tap.
related to matrix, should be leveraged by, what Vertec is doing into this Prometus receiver.
And, just to finish, on the… The policy engine on which, Albert and David are working.
Will be, in fact, integrated into a telemetry policy processor, or integrated for more advanced capabilities into the transform processor.
The reason behind that is… Fundamentally, the… the telemetry policies, they are, like, a bag of policies that are self-contained, and there is no real, way to express different custom stages to apply those telemetry policies. There is some kind of order that are implicit, but explicitly.
the spec is not specifying, okay, I want to apply this telemetry policy set, and then this one.
But OPL can do that, and in fact, in the proposal that we created, there is an example of that. So… Yeah, I totally agree. We need to, to use the… what we will optimize for metric renaming inside this, inside this effort.
**Joshua MacDonald (Microsoft)** 28:28 Cool, yeah, maybe we can just consider this a sort of translation from relabel configs into the… The query engine's natural abstract syntax tree.
**Laurent Querel** 28:41 Yes.
**Joshua MacDonald (Microsoft)** 28:42 Very good.
**Laurent Querel** 28:44 You mentioned, all the work that, is currently done, by the Promotives community and us, For people that were on the present last week.
That's a good representation. We are in a very good spot right there.
Which is really cool.
And we… that's another element on which we need to… Make sure that we are extremely responsive.
Because that's another way to get a lot of momentum around this project.
Okay, so… We talk about policies, this one and this one, what about talking about entities?
**Jake Dern (F5, Inc.)** 29:27 Yeah, I'd be happy to jump into it. Maybe it's worth talking about the qualified metric names. I think it might be a smaller topic, and it also does relate to entities a little bit.
**Laurent Querel** 29:38 Right, let's go.
**Joshua MacDonald (Microsoft)** 29:42 I can speak to this. So I picked this up just because I was looking at all the open PRs that Bartek has. I want to help him move fast, so I was looking at this one, and… I can see why he's done it, I can see that it will be breaking for users, and so we want to ask, essentially, the group here how they'd like to see that handled. But I did bring up… to me, this brings up, sort of, very old questions in OpenTelemetry about when you use the same metric name And whether you don't use… when you don't use the same metric name.
And with regards to when you have a scope. So, do you… can you use the same metric name in different scopes? This has been debated in OpenTelemetry, and it kind of settled a long time ago. So, the idea that when we use the same metric name in OpenTelemetry, we're trying to say, I have an alternative implementation of the same exact thing.
And that if you can replace one scope with another scope, and you see the same metric name, what you're saying is I have a different way of instrumenting the same thing.
But what we're doing… is not… it's like, it's sensible, but it's not what OpenTelemetry decided to do a long time ago, which would be to say that when you have this metric scope, it's a namespace, and therefore, anytime you put a metric name inside that scope, it is effectively a different metric.
And that… that is sort of not the direction that OpenTelemetry went. So, what I'm seeing here is an effort to restore the sort of… sort of normalness, normal in OpenTelemetry.
But I could see how it would disrupt things, and so I wanted to talk about how we might Do this safely or slowly, or even offer multiple ways to configure metrics at runtime.
**Laurent Querel** 31:28 My reaction is, if we are doing a change.
And that's why it's a very nice, also, position for the next topic. We need to do it in… coordination with what Jake wants to introduce.
Because that will also imply some changes in the self-calibratory.
And, ideally, we should have One transition, not, two transitions.
Just to minimize the effort on any dependencies.
that we have, either inside Microsoft or i5.
Because I think right now we are the only, company really using this, stuff, in production, so we… Yeah, I'm just, advocating for… Thinking about these two things as one transition, if we need to transition, and minimizing the effort on the team that are depending on this work.
**Joshua MacDonald (Microsoft)** 32:32 That sounds good.
**Laurent Querel** 32:35 Jake, so, do you want to add something to that, or we go directly to your… quantity stuff.
I agree, relative, relatively related.
**Jake Dern (F5, Inc.)** 32:47 Yeah, let's, let's just move over to entities. I think this will come up naturally at some point, and it'll just be helpful to have in the background minds.
**Laurent Querel** 32:54 Oh, okay, so I don't remember where I… okay, I've seen…
**Jake Dern (F5, Inc.)** 33:06 All right, yeah, so I just published this draft, right before the SIG meeting here, barely got it done, and so… Or folks that, that don't know, basically the DFE, I mean, we have a nice entity model, and a nice metrics model, and sort of all of our rules for how those two things interact and how we report these, you know, using open telemetry signals.
And we've been developing that over the last, you know, year or so. Kind of at the same time, the OpenTelemetry entity SIG has been working on the entity model, and sort of what that means in abstract, and how that's communicated over signals.
And so recently, I've been kind of examining what's there in the entity SIG today, and then kind of looking at what we have in the engine in more detail, and then trying to see how we can align the two more closely. And so the goal of this RFC, it kind of does three different things.
The first thing it does is it tries to redefine the DFE's concepts of entity in OpenTelemetry terms. So it's just redefining some existing stuff that we already have.
It also proposes a few changes, to the existing model for closer alignment to entity semantics. So there's a handful of things in here.
One of those is, some scope changes that relate to, the stuff that we were just talking about. So, one reason why We might also want to make this change where our metrics have a different name prefixed by the metric set, and then suffixed by the actual metric in that set, is because we might want to change how we use scope name today. One possible use for that could be to place an entity type there.
And say, things within this scope, signals within this scope belong to this entity specifically. So that's… that's one… one change that's proposed here.
And then another thing, that this RFC does is that it proposes a few extensions.
So, things like, entity events.
And how we can use those to communicate the relationships between entities, are also proposed in here.
So it's kind of a whole bunch of different entity-related things in this RFC.
I think we can talk about each of these things individually, as much or as little as we want. One caveat I do want to mention is that the goal of this RFC is really just to kind of be a starting point. I think the OpenTelemetry entity stuff is still under development, and so this PR is sort of a… a best effort at aligning the DFE's entity model with the OpenTelemetry one, as it exists today. I think it would be nice, and I've been, you know, showing up to the entity SIG meetings and talking with Josh Sareth and others.
I think it would be nice to sort of use this proposal and some of the drawbacks in it to try to influence the ongoing entity work, particularly thinking about how we can allow for more than one entity per resource, how we can leverage scopes in order to communicate entities, things of this nature. So… I'll pause there, but that's… that's kind of the context for this RFC.
**Laurent Querel** 36:30 Yeah, I'm super excited about it.
**Jake Dern (F5, Inc.)** 36:34 And one thing I'll also mention is, sorry to interrupt, there were a bunch of proposed potential changes to existing metrics, so just changing what the metric sets are, and potentially some of their dimensions.
Those I took out of this RFC on purpose. I think we can litigate each of those separately. They're kind of an orthogonal thing. This is really just meant to be more of a guideline for, okay, how do we think about entities?
In general, in the Dataflow engine, and how do we communicate them?
**Laurent Querel** 37:05 Yeah.
Maybe for people that are not necessarily super familiar with this new set of entities, I think something I have found interesting into your, RFC is this distinction between Trying to find, yeah, here.
Between the ambient entities and the internal entities, so the… what… some of you know from entities was mostly ambient entities. So that's something that could be discovered by the resource detector.
There are the… the entities that are referenced into the resource section.
What was less, in my opinion, identified or well-defined before.
was the… this concept of internal entities, so inside your process, and that's what we did, from the digging into the data flow engine.
In order to really implement a safe telemetry system. We basically reify every internal entity, a pipeline, a pipeline group, a node, a channel.
I think you mentioned those existing internal entities here.
And they, they come with, What you named here the identifying attributes and descriptive attributes?
And, and we attach to each of those entities, matrix or event.
And… and… The nice thing about that is… Just to show you… The reason why we have been able to do this pipeline topology, which is super simple in this screenshot, but could be much more complicated.
We are deriving this entire, topology pipeline topology.
From observation only, not from configuration file.
And, and we are observing entities.
And we are connecting those entities by some invention.
And we are able, when we click on the receiver.
We can just figure out, okay, all the metrics, all the events that are, in fact.
emitted by this entity. We have a generic way to retrieve them, and that's how we created this, very generic UI.
So if someone comes with a new, a new nud.
Does that matter if, this not follow the… The convention that we are using in terms of entity and attachment to this entity, in terms of other signal.
it's automatically integrated into the UI. So that's why I'm very excited to… to see the… This concept of internal entity.
Finally well integrated into the entity, a fourth part of OpenTelemetry.
Because that… even if we have to do some changes on our side, We are… we know that it's extremely valuable, and I'm super happy to see the… Some… some rationalization there.
**Jake Dern (F5, Inc.)** 40:36 Yeah, and just to be clear, this, you know, distinction between what the proposal calls ambient and internal entity. I completely made that up, but I'm hoping that we can get a similar notion in OpenTelemetry, and I think it's a logical line to sort of draw. And I think this idea of placing ambient entities on the resource and perhaps using Ben's scope in order to communicate internal entities that you have more control over and Know things about and want to attach signals to.
is potentially a nice idea and a good direction to go. Yeah, there's a lot to talk about with entities, and I think a lot of exciting things, especially regarding entity relationships. Folks that maybe haven't been thinking about this before.
But the idea that, like, composition, for example, can help you construct, like, a full compound identifier for an entity is really exciting. Other kinds of relationships, including containment or belonging, you know, can also give you spatial reaggregation boundaries.
And define what meaningful boundaries for that can be. So there's a lot of possibilities here, to communicate a lot of information about your system, using entities and relationships, so… It's very interesting stuff. I'm, like, very excited to be working on it.
**Laurent Querel** 41:53 Did you, Had a demo, maybe, of the… this, this SIG, just to maybe, to the SIG meeting, I mean?
Just to give them an idea of how we are leveraging this concept in a generic way.
**Jake Dern (F5, Inc.)** 42:12 Yeah, I have not yet, but I see Josh has his hand up, so maybe before we get on that tangent, is there something you'd like to say?
**Joshua MacDonald (Microsoft)** 42:19 I was going to ask a question about this ambient versus internal, because I know that there's an open PR in the spec SIG about identity scope, or.
**Jake Dern (F5, Inc.)** 42:27 Yes.
**Joshua MacDonald (Microsoft)** 42:28 scope.
And they've got local and global, so are those similar or different concepts?
**Jake Dern (F5, Inc.)** 42:34 different concepts, and so that PR that you're referring to that's open, I think that one is kind of the hot topic in the NED SIG right now, and I've left a lot of comments on it, and we discussed it quite a bit on Monday, and I think there, you know, there may be some changes that would be nice to make there.
But I do try to define, actually, identity scope as well.
In this, in this RFC. So yeah, that's more about, you know, given some, identifier for an entity, Is that identifier local or global?
And if it is only local, in the sense that that identifier does not uniquely identify the entity in the system by itself, how do you get to a global ID? And the way that you do that is sort of still being defined. The way that we do it in the data flow engine is by walking the containment chain.
They sort of define it slightly differently, and more explicitly, really, by saying specifically for a given entity, what is its, you know, what entity is its ID unique within?
And so there… there's kind of a decoupling between relationship and the current proposal, and that PR that you linked, and, you know, this notion of local and global identity. In the data flow engine, it's more fused. Ambient versus internal is… is… at least in this RFC, more about where does this entity live? So, ambient entities are things that sort of enclose the data flow engine, the process, the host, the pod, container, you know, that hierarchy, things that you're sort of detecting and discovering through You know, resource detectors or entity detectors, that kind of thing. And then the… those are reported on the resource in the data flow engine today. And then internal entities are reported on the scope and are things that are under the data flow engine's control, in terms of life cycle. So that… that's the distinction that I'm trying to make here.
**Joshua MacDonald (Microsoft)** 44:40 Got it, I think I understand.
Does this imply changes in the OTAP protocol?
**Jake Dern (F5, Inc.)** 44:47 No, no changes in the OTEP protocol. Unless there end up being changes for,
**Joshua MacDonald (Microsoft)** 44:53 But I know that the resource has a field called Entity.
And I don't remember seeing it in any of our code. Is that…
**Jake Dern (F5, Inc.)** 45:02 Yep.
This is a good point, yeah. So today… yes, okay, so I follow your question. Yes, we don't support entity refs in OTAP today, and we do need to at some point, if we want to communicate ambient entities. Additionally.
there is no way to communicate entities on a scope today in open telemetry, and that's something that I'm hoping maybe we can work to add, and if that were added, we would also need changes to OTAP to accommodate it.
**Joshua MacDonald (Microsoft)** 45:33 Do you see this as another table?
**Jake Dern (F5, Inc.)** 45:37 Probably.
**Joshua MacDonald (Microsoft)** 45:40 I'm familiar with the missing schema entity relationship, anyway. I will take a look at your RFC. Thanks, Jake.
**Jake Dern (F5, Inc.)** 45:48 Yeah, for sure. And I, I… mentioned that I was writing this to Josh and other… the other Josh, and the entity SIG and others on Monday. They said they'd also be very curious to take a look and work with us and try to see the challenges that we're having and how we can improve the OpenTelemetry entity model.
**Laurent Querel** 46:09 Great.
Any other reaction to this work?
Otherwise… So, what else?
We have, 15 minutes.
So, what about the… So, either in the… so, first, regarding this idea of having a dedicated blog for the hotel Arrow, I'd like to get your feedback, guys. What do you think about this idea?
**Albert Albert** 46:47 I think it'd be great.
**Joshua MacDonald (Microsoft)** 46:49 I found myself asking if any other OpenTelemetry group has a dedicated blog, and I couldn't find any that does.
That…
**Drew Relmas** 46:58 That would be my question as well.
**Joshua MacDonald (Microsoft)** 47:01 And only… the only other thought I have is that it's a pretty big commitment to keep a blog fresh. I, you know, I just worry about… All of a sudden, we have a blog, and now we're pushing to find posts for it all the time, or something like that.
Go ahead, Drew.
**Drew Relmas** 47:22 Instead of having an external block, could we imagine Just having it checked into the repo here.
**Laurent Querel** 47:29 Oh, that's the easiest.
**Drew Relmas** 47:32 Okay.
**Laurent Querel** 47:32 That's, yeah, that's…
**Drew Relmas** 47:34 blog site versus…
**Laurent Querel** 47:35 It's a… for me, it's a set of GitHub pages, part of the repo, just a MacDonald file.
And we use it…
**Drew Relmas** 47:46 It's slightly different if it's repo internal.
**Laurent Querel** 47:49 Probably 3 points on all, yeah, yeah.
**Joshua MacDonald (Microsoft)** 47:51 Yeah, you can definitely make a blog from the GitHub Actions pushes the content to the site.
It would be nice to have a landing page on our GitHub site anyway, because right now, if you've noticed, the… all the benchmarks and the comparisons are sort of, like, at some mystery URL underneath the root of the site.
And there's nothing at the top of the site, so I can see putting the blog there. You're probably still gonna have I would worry about kind of driving content and, like, regularity, you know, but that's just a minor fear that we will have… eventually it will go stale, and maybe we're done by then, so…
**Laurent Querel** 48:34 Yeah, just a feedback on that.
The reason why I was thinking that is often thinking that it was interesting to to go, on this path of having a repo-level blog post, set of blog posts. I don't think we need a regularity.
I mean, there are multiple technical-oriented blog posts that don't necessarily post every week.
It's not a news-royalty, blog post.
It's more, if we have something interesting to say, we just say it, otherwise we don't say anything.
But at the same time, if we look at the OpenTelemetry.io blog.
And if you look at what Most of the time, we see there are more big announcements on a new project, or a new phase of the project.
I was more thinking about, in my case, okay, we… We are working on a nice optimization, and we want to show some benchmark rates, just focus on this nice optimization.
So, some… some elements that are highly technical, and where, we think there is a… Some interest for people, but not necessarily people that are interested by open telemetry, but more interested by design, architecture, algorithm.
And obviously they will be related to a tailor, but I think that's more or less the… my goal here.
**Joshua MacDonald (Microsoft)** 50:08 Yeah, that makes sense to me. I can… I've definitely seen the make docs command be used for making blogs with, you know, minimal RSS support. That seems like something that shouldn't take too much to set up, I would be glad to see it.
**Laurent Querel** 50:24 Yeah, and, I started to look at, just basic solutions, like, you go to, to basically take a MacDon file with some convention, and I'm from there, generating… A nice, blog post integrated into the repo.
As a GitHub page, and, also updating the LSS feed.
So I don't think that will be a massive effort. I think there are many, many examples of that already, and that could be integrated into GitHub Actions.
**Joshua MacDonald (Microsoft)** 50:59 I would… I will say, I think we should run this by the… Governance Committee, as far as communication strategy.
**Laurent Querel** 51:08 I mean?
**Joshua MacDonald (Microsoft)** 51:09 there is already this entire repo full of blog management tools for OpenTelemetry. I wonder if You know, we should think about consistency with the OpenTelemetry blog style, maybe?
**Laurent Querel** 51:22 Yeah.
**Joshua MacDonald (Microsoft)** 51:23 I was just gonna propose I file an issue in the OpenTelemetry Community Repository, saying we plan to make a content, page, blog type thing in the GitHub Action site for our repo, and… Get people's comments.
**Laurent Querel** 51:42 Yeah, but to precise that we… we are thinking about something that is…
**Joshua MacDonald (Microsoft)** 51:48 Technical.
**Laurent Querel** 51:48 Yeah, technical. It's not, like, element-oriented.
**Joshua MacDonald (Microsoft)** 51:53 I will propose something, I'll run it by you first, Laurent, that we can post in the community repository.
**Laurent Querel** 52:00 Yep, cool.
Hi, Bill.
**Albert Albert** 52:05 I… If we're gonna move off, blog, and we have 10 minutes left, I have a topic.
Okay, cool. Go ahead. Cool. Shoot, okay, I can't share my screen.
**Laurent Querel** 52:20 I can…
**Albert Albert** 52:21 again.
**Laurent Querel** 52:22 Stop sharing, and you can share your screen, yes.
**Albert Albert** 52:24 Oh, maybe I can share. Okay, let me see here… desktop 2… Okay, here we go. So, this PR, was opened, yesterday, and it brings up something that I think is, like, like.
kind of an interesting question. The issue in the PR, and I won't go too deep into it, is basically, like, if you're encoding OTAP using the OTEL Arrow, like, Golang exporter. One of the things, like, that that exporter does, is it will… Like, try to… big, like… if there's two scopes that belong to different resources while it's encoding, and those two scopes are exactly the same, they have the exact same name, the exact same attributes, it will assign the same scope ID to those two different scopes, even if they belong to two different attributes. And it just so happens that, like, it will do it, only if, like, the batch is sorted in a certain way. And so, part of me thought, like, okay, we should definitely, like, handle this, because otherwise, like, the Go exporter can encode something that is, that we won't be able to decode correctly. But then it got me thinking, like, Should, like, should… we be doing that in Otel Arrow, in the Rust, and is that the proper behavior? Basically, like, should we be assigning a unique, ID for a certain scope?
like, if that scope has the same name, the same version, the same attributes, even if that scope belongs to different resources. And, you know, that might seem a little bit weird, but you think, like, maybe there was a reason we did it in the Go exporter so we didn't have to, like, duplicate scope attributes, for example.
So I guess what I'm thinking here is, like, does anyone remember, A, if that behavior in the Golang exporter was intentional.
Or B, is it something that we want to adopt on the Rust side?
Yeah.
**Laurent Querel** 54:40 So, I remember, seeing there.
What I remember is not exactly what you described, but close.
**Albert Albert** 54:52 Bring up the code if it does.
**Laurent Querel** 54:53 So, let's imagine that you have an OTLP batch.
Today, an ATIP batch could be multiple.
resource, then inside each resource, multiple scope.
And then multiple signals.
And, when we batch things.
It's entirely possible that we batch, in fact.
Multiple Russells that belong to exactly the same origin.
And potentially inside multiple scopes that belong to the exact same scope, and so on. So, the… one of the optimization And it was, like, something that was… Optional, but, for me, it was… okay to combine resources that are exactly the same, or scope that are exactly the same. And they are the same because At least if a cop has exactly the same attributes, key value pairs, plus the same name, same version.
Then we could… we could basically merge the signal into a single scope.
That has exactly the same definition, and we can avoid this way.
To have multiple declaration.
So that's why we… when we… we did some… Comparison.
The comparison function is a semantically… Equivalent comparison, and not a strictly equivalent… a strictly equal.
Because of this kind of optimization that we did.
Structurally, it's not exactly the same.
Because you can merge two scopes that are exactly the same.
So that's what I remember, why we did that. It was like an optimization, But it's optional, so the… And a tapped receiver should be able to interpret And a tap batch, which contains this optimization, or not.
**Albert Albert** 57:05 Got it. Okay. That was my… that was my question. Was it intentional, or is it not? And it sounds like it was, so… Okay, cool. Alright, appreciate that. So, okay, that answers my question, but you said it's optional, so we don't necessarily need to do it.
**Laurent Querel** 57:19 No, yeah, yeah, yeah, yeah, it's, No, it was, because, like you said, it requires, sometimes you are in a position where this optimization does not It's not, complicated to implement.
And then, why not using it, but sometimes it's… It's not worth it, so you don't have to do it.
**Albert Albert** 57:49 Sounds good. Okay, cool. That was all I had. I yield my time, to the next speaker.
**Laurent Querel** 57:56 I think that we have, new people, today, I see, Narine, I don't think, Is there, maybe some people that want to talk and maybe explain their interests for the project? Just to, to, It's interesting to see new people in this project, and try to figure out why they are there, and what they have to say.
**Narine Mossikyan** 58:24 Yeah, hi everyone, my name is Narine, I'm from Microsoft. I will be contributing to this project, and I'm here to just learn and see what's happening right now, and the current issues, and where I can possibly help.
Yeah, that's all, but I don't have any updates for today.
**Laurent Querel** 58:47 Great. Is there anyone that, I see also, I don't know, but I don't remember if we… Bhala, Are you new to the project, or… Yeah.
Downloads.
**Bhala Ranganathan (Microsoft)** 59:01 Yeah, I'm also… I joined the last SIG meeting as well, but I am new to the team in Microsoft, and work with Aaron, like, Kennedy, and, you know, Utkarsh, those folks.
Yeah, same as Narine, I'm also, like, trying to understand what is happening, and then contribute wherever possible.
Grace? Yeah, that's fair.
**Joshua MacDonald (Microsoft)** 59:28 All those new people. Thank you very much.
**Laurent Querel** 59:30 Yeah, thank you. Have a good day.
See you next week.
**Bhala Ranganathan (Microsoft)** 59:34 Yeah, thank you.
**Pierre Mariani** 59:35 Thank you.
**Joshua MacDonald (Microsoft)** 59:36 Cheers.
