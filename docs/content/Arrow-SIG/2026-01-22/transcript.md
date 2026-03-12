SIG: Arrow SIG
Date: 2026-01-22
Duration: 61 minutes
============================================================

## Zoom Recording Transcript

Laurent Querel 00:00:33 True.
But only when the, yeah, the video… Luido.
jmacdonald 00:02:32 This morning.
Laurent Querel 00:02:36 Good morning.
drewrelmas 00:02:37 Or evening.
Laurent Querel 00:02:42 We… I was going to share the…
jmacdonald 00:02:47 buddy. Oh, there it is.
Laurent Querel 00:03:02 Can you hear me?
jmacdonald 00:03:03 Yes.
Albert Lockett 00:03:05 Cheers.
Laurent Querel 00:03:05 Okay.
jmacdonald 00:03:06 Good morning.
Laurent Querel 00:03:08 Good morning, Josh.
Everyone… So, my side, I just added in the agenda two topics, I think there is a new one, probably from Josh. So the first one is about the… Great naming distribution we had yesterday.
The other one is about the stabilization of the configuration model V1.
These two things are going in the same direction, stabilizing the project in order to be, Yeah, more stable and ready for publication.
And start to have some users, and that's the case for us, for example, for F5 internally.
And, we have this ongoing work regarding the internal telemetry system, also known ITS, sometimes.
Which is, something on which, multiple, Contributor maintainers are working right now.
Any other topic to discuss?
jmacdonald 00:04:24 I have one I want to add that's sort of open topic. I don't have… I don't quite know where it will go, but I've seen the Slack discussion about global channels and multi-tenancy, and I'd like us to just talk about what we all kind of want in multi-tenant worlds.
Laurent Querel 00:04:40 Ridiculous.
jmacdonald 00:04:41 about how would you do rate limiting, and that sort of thing, especially. But that's… I put that at the bottom, and… and thank you.
Well, I would say that, sometimes we lead off by looking through all the open issues, but what you've… the top of the agenda here has, like, a bunch of new issues that have been filed, so I would propose that we just move right into your stabilization, item here.
Laurent Querel 00:05:07 Yeah, I was doing some type boxing, Just to try to keep that as… as short as possible, but we'll see where that goes. So the renaming, so try… I'm trying to retrieve the… do you remember the number of the, the GitHub issue under which we have this, oh, pro…
jmacdonald 00:05:33 There was a pull request where some discussion started, and it links to an issue that may not have the.
Laurent Querel 00:05:39 Oh, okay, so we can go directly to this, right, yes.
jmacdonald 00:05:46 Organize OTAP create by complete.
Laurent Querel 00:05:48 Okay…
jmacdonald 00:05:49 That looks important.
Laurent Querel 00:05:51 I think that's this one, then we have this, okay.
Yeah, so during the last SIG meeting, I think last week, we discussed this, needs to, at some point, to publish crates on crates.io.
And, and during this discussion, we… So we define some, basically, some condition to do it. The fact that, at least on my side, I think it's too early to have a stabilization around the API. That doesn't prevent us to prevish on crest.io.
But, that need to be, flexible, and the versioning needs to reflect that.
Other discussion around crate renaming, like the, OTAP, crate?
Which is, right now, a place where we have all the… the nodes… On the different receivers, processors, exporters.
Either, core or, currently named experimental.
And, and we, and OTAP as is, for our crate name, and… Knowing that for every cred that we have in terms of folder, we have those prefix, a common prefix, to, to solve the… some scoping into the credits.io, so I'm not specifying the prefix each time, but consider that the prefix is there.
So the… the idea, or what we discussed at some point, was what about having, core nodes and contribute nodes? And, I probably did a bad job when I was suggesting this approach, because we end up with something that looks like that, but it's not exactly like I had in mind, which is not necessarily a big deal.
But the approach described here is a crate with some folders.
Where basically, like, in the Go Collector, there is a… A categorization per node type, and then contribute at the same level with exactly the same organization.
And, someone in the community, thank you, already work on that.
And I didn't read this GitHub issue in time, unfortunately.
I, I saw the PR first.
And I was surprised of the… the… the solution, retained.
And then we entered into some discussion, and I just want to spend one or two minutes to specify what was, for me, the… The right approach, or an alternative proposal, So instead of splitting, The idea… the main idea is to have two distinct crates, one for core nodes and one for control nodes.
with exactly the same organization. So it's not a big change, except that the boundaries are different. It's not a boundary that is purely a directory, but really a crate on which we can apply some constraint.
And I'm trying to explain here why I think it's, it's a better approach.
Either in terms of ownership and rule that we can apply to a crate, which we could not illegally apply to a subdirectory.
So that's the alternative proposal.
I was also saying that, For me, the concept of experimental is orthogonal to core and contribute, so we could, Have a core node, which is experimental.
And we could have a control node, which is experimental.
Then, I think, I didn't read the last feedback, so I like to get maybe some feedback live, live feedback from people based on that, and, the idea at the end is to decide, What will be the… the direction that we will, retain, and And then work with this, contributor. I don't know if this contributor is with us today.
But to… to make that happen.
drewrelmas 00:10:35 Yeah, I want to chime in, just because it was my issue that I opened. I agree, Laurent, I probably slightly misremembered what we discussed in the stake. I didn't have access to the chat. I think that's where you had sent the… contrib, and nodes being separate crates. I really like your rationale, it all makes sense.
The one other thing I'll add is, I see we have Tom in the room, I don't believe we have this contributor in the room. Tom, maybe a follow-up for you and I here is perhaps one of the labels we're talking about when we're… when we discuss issue management is… a label for, like, under review, indicating that something isn't quite, you know, discussed with the group yet, and isn't quite ready for work. So that might help, avoid this. Not that this situation is a bad one, but it might, facilitate better Coordination going forward, so, that's something we could do.
Laurent Querel 00:11:35 Yeah, definitely really great idea.
And the review, maybe, is, not clear enough, something like, like you said, not ready for a contribution, or is it… Not ready for work.
drewrelmas 00:11:51 can also work.
Laurent Querel 00:11:52 Not ready for work, yes, yeah.
Yeah, something like that. Super clear, and I totally agree, because we will have more and more things like that.
Another example, which is not labeled, Where we could, definitively see exactly the same problem. People going super fast and implementing what we started to describe is about the configuration model V1, the stabilization.
task that I started a few days ago.
same, same problem. So, yeah, definitively, we need to, to make that, clear.
So, is there any other feedback regarding this, this one?
I forgot something, The discussion regarding core versus component.
I don't remember if I put that there, or if it's on the… I think it's on the, the Slack channel.
One of the selection in, but So my rational… so that's another, thing we need to decide, and soon, because, the implications are, are relatively, Deep.
Until now, for the OTAP data flow engine, we are using the term node.
To represent anything that is a receiver, processor, exporter, and only that.
So, basically, everything that played the role of a node inside the graph.
Because we, we are basically, We have an engine, that, implements a graph of transformation, a graph of, Producting information, exporting information.
It's, fundamentally, it's a DAG, and the approach is slightly different from the GoCollector, on this, It's a little bit more general in terms of way of thinking the… this graph of transformation. There is no implicit things, there is no implicit connection between Receivers and the processor stage.
Similarly, there is no implicit connection between processors and exporters.
It seems, not so important, but the importance is we can, by being explicit, we can specify Clearly, the… The… the expectation of those connections.
We obviously have default.
But, nothing prevents us to have, different dispatch… dispatch strategy, different delivery of guarantee, the guarantee of delivery, and many other things that could be attached as a policy to… what we name hyper-edge into this system.
It's not just edges, they are hyper edges, meaning that they could have… the same channel could have multiple source, multiple destination, multiple sender, multiple receiver.
it's an important distinction. And that is currently supported by the system. That's why I was using the term node instead of component, because components, in my view.
is super generic, not necessarily related to a graph, and I think, maybe I'm wrong, but I think it's used inside the GoCollector for everything, not only processors, receivers, exporters, but also for extension, and probably some other concepts.
So that's why, I had… a preference for NUD, but, we also have this… obviously strong connection with the GoCollector, so I'd like to open the discussion on that.
jmacdonald 00:15:57 You just made a very convincing argument. I hadn't thought about that detail. The components includes extensions. Those are not nodes, in the sense, and now I see it, so I'm on board with nodes.
Laurent Querel 00:16:11 Okay.
Cool. Any other, feedback?
drewrelmas 00:16:21 If there is not, I can go ahead and document on this issue that we'd like to go in the direction that you stated, but again, last call.
Laurent Querel 00:16:34 Yeah, okay, I think, so feel free to raise your hand, but, I think… oh, Albert, oh, Albert, you just said yes, okay, but also. So I think, you know, we decided that, we will go with two, create, We will use the term nodes.
For the term node, and in that case, core nodes and control nodes.
With the rational that we, we discussed there.
I think we made the good decision. Cool.
So let's move to the next topic.
Which is a big one.
And it's an open topic, because I don't think I was able to… To talk about, or to explore all the… the thing that we have to achieve there. So, right now, we… So, until a few days ago, the… this, OTAPDF engine was able to take A pipeline configuration as a parameter.
And the pipeline, like we discussed, is basically a description of a DAG where you have nodes connected together, plus a few other things related to settings and general policies.
A few days ago, we added the option to And it was already part of the, The configuration model, but not leverage.
We… we have something, into this, configuration model that is a little bit higher level.
We have the concept of pipeline groups, and pipelines.
So, in this model, it's a hierarchical model. A pipeline group is a group of pipelines.
And on the same… OTAPDF engine instance, we can run, now, multiple pipeline groups, so… Each of them having multiple pipelines, potentially.
And we will have an API to manage the lifecycle of those groups and pipelines. A group could be mapped to a tenant.
For some deployment, or to a product, to whatever the user of the system wants to map this notion of pipe and group with.
Something external, like a tenant or a product.
Oh, team.
Or an environment, like dev, and so it's very flexible, like the namespace that we have in Kubernetes, things like that.
So, really, the goal is to have a multi-tenant ready or very flexible infrastructure that will, that people could use to run many pipelines all together. Obviously, multiple of those, processes, DF engine could run in parallel, multiple pods, part of the same service. That's entirely, feasible.
But we, we want to offer this, flexibility. So… That's one thing. The other thing is… the, Now that we… we use this system now for several months, we also, got, We can refine the model in how we specify things, like, for example, the output for a node.
And many other things in order to optimize a little bit the user experience. So, I put here a set of, critical points to consider.
In order to achieve, a V1, To stabilize the first version of this thing, which is fundamental, because that's the main Point of interaction with the future user of this system.
So I put the, user experience as a super important, critique… criteria?
We need to define the supported format. I think that is relatively flexible.
But we just need to enumerate them. A critical one, which is far from ideal today, is the quality and the usability of the messages returned by the system when The configuration file is not valid for any reason.
Right now, it's… it's, let's say an error written by CRD, which is not… Which is a fantastic library, but not the best in the world regarding error messages. We need to talk about versioning, how to evolve the system, the extensibility, that's an important one.
So… like you know, F5 is, contributing, like Microsoft, a lot on this system.
But we want also to be able to extend it for our own internal usage, which will not necessarily be, things that we want to put into the open source project. So, having a way to make extensible the configuration model to support such, integration.
And that's true for us, that's true for Microsoft.
I think for many others, we'll make this configuration model really cool. I think I have some ideas regarding that, it's not specified yet.
We need to clarify the advanced concept, so that this one is now clarified a little bit more, but, this one that we started to discuss, it's also related to the multi-tenancy discussion. At least it's a general concept that could be used for that.
the concept of Qatar, we… I think the… The architectural decision we made a long time ago now.
prove that not only we can get really cool performance, but also, from that, we can derive a lot of very nice properties. The ability to monitor per pipeline instance.
Without any, mix, is, is a super strong property. So, being able to apply coda or, limits per pipeline instance.
So if you translate that to… imagine you have one pipeline instance per tenant, or sometimes multiple, depending on the size of this tenant.
and you are able to apply limits to pertinent. It's a very complicated thing to achieve with… Something that has not been designed the way that we design it.
For example, if you want to repeat that for the GoCollector, good luck.
to specify how much CPU usage you are able to use for a specific, instance, or tenant, except if you have a tenant per GoCollector instance, then yes, you can. But if you are in a sharing approach, that's very hard.
we have a mess, a little bit of mess in the URL mechanism, which is the way to To identify, nodes that need to be, instantiated into the DAG.
And, there is not only some lack of consistency, and there is also some friction in terms of usage. It's super long, it's not super nice.
So I have a proposal for that.
we need to define the control API. I didn't, create any proposal there, and we also need to make sure that this configuration model will support something that is super fundamental for us.
And I guess for many people in the community, live updates.
So I really like to get a solution where we don't have to restart something just to change the configuration of a node, or even to change slightly the… the topology of a DAG.
That's fundamental, for many, many use cases.
So that's the goal, and then I started to create a bunch of proposals, So maybe, I don't think that we will have enough time to review all of those proposals, and for sure we will add more.
I think we need to start with the one where I will suggest to start with the urine, because that's one that we can very easily, I think, on which we could decide quickly, and make some, adjustments that will not, be, That could be done incrementally, and then we can go, With the next one, with a similar, type of constraint.
But if you have one that you want to talk first, let me know.
Okay.
So I think that's for no, there is no… Or the proposal, to discuss first.
Here, and so let's see the… here is the… migration table, and also, sorry, first. The… the URN, the common pattern I'm, for which, I like to… that I like to target is the… this one, URN column namespace.
Our namespace could be hotel, so every per component will be hotel, obviously.
Contrib will have a different namespace, and… Could be, Microsoft, could be F5, could be whatever.
Id is the main ID of the node, and kind could be receiver, processor, exporter.
For the namespace, I'm suggesting to either use the vendor name.
I'm using the term vendor, but obviously it could be something that is not necessarily a vendor.
Or a combination vendor with product names for a company that are being imagine Microsoft, or even F5, which is much smaller, but still, we have multiple products. So, something like Microsoft underscore Azure, or something like F5 underscore Big IP.
But it's… it's a… it's an Mspace that will… should be unique.
And then I described the naming rule, and I suggested a mechanism to make things a little bit nicer for the users.
A shortcut form.
which basically removed the URN and namespace for everything that is core, which is hotel. So, which… so, for example, instead of going and, say, a URN, hotel, OTLP, receiver, we will have OTLP receiver.
That will be, so, OTLP receiver.
That will be, in my opinion, much nicer than what we have today. And based on the rules that are enumerated there.
I don't think that we will have any problem, current or future.
maybe I'm wrong, but I think it's… I tried to put the rationale here.
And, and then, if we agree on that.
Here is the migration table, where that's an inventory of everything we have. We start to have a lot.
The proposal, what could be the target, and I have here a column named change, where you can see where when there is a cross, that's where we have an inconsistency and we need to fix it. Otherwise, we are already following the model.
And, when shortcuts are possible, there is this column where, we, I summarized what will… so, OTLP receiver, that's exactly the toolkit I was discussing.
Yeah, so, what do you think?
jmacdonald 00:29:34 Oh, this is a great improvement. I've had to guess at URN so many times, and gotten them wrong so many times. Every time I create one, the pipeline tells me I'm doing it wrong, so this is great.
I like the shortcut as well.
Andres Borja 00:29:50 I didn't get the shortcut. When is it used?
Laurent Querel 00:29:56 So the top, so back to this, list of, critical points to consider, user experience is one that I, enumerated, and I think… If you look at the GoCollector configuration, you will see things simple like OTLP receiver to describe a node.
In… in the current situation, we have to enter that URN hotel OTLP receiver, which is… For most of the use cases where we… you just use core components.
It looks, like, super redundant to add URN and hotel, so in terms of user experience, it's not great. What I'm saying is, by following the rules that are described here, people will be free to either use the fully qualified URN or the chocolate.
And there are rules to… and it's only open and authorized for… Things that are under the hotel namespace.
So that's the original to read the… The full description.
Andres Borja 00:31:04 Is it, like, what you would put in the configurations, is what you mean?
Laurent Querel 00:31:09 Oh, yes, yeah.
Andres Borja 00:31:10 Gotcha.
Laurent Querel 00:31:12 Yeah.
Yeah, that's what we will put in the configuration, and in the… when we declare a new node, with the plugin mechanism that we have in place, we will specify the entire, URL, the fact that we authorize, we accept shortcuts will be something that will follow the rules that are defined here.
It's not something that the component, the node itself, will have to specify. It's something that will be automated.
Any other feedback?
Utkarsh Umesan Pillai 00:31:57 Yeah, I had a question, Laurent. So, like, you said hotel would be the reserved, namespace, so are we also trying to, like, do some kind of enforcement for it? Like… If a third-party component just decides to use OTL as the namespace, would we reject it?
Laurent Querel 00:32:14 I think so. Yeah.
Utkarsh Umesan Pillai 00:32:16 Yeah, I think we… yeah, I agree, we should.
jmacdonald 00:32:20 There are already rules, like, they have to end in a known name, like receiver, processor, exporter, and they have to start with hotel, as far as I can tell, or it won't work. That's what I was referring to, the confusion, I keep getting it wrong, having to, like, change it.
Laurent Querel 00:32:33 Yeah, that's true. We already had some kind of world raves.
We need to update them, obviously, based on this proposal.
And we need to enforce… so, for example, we should not see any hotel namespace into the, contrib… dash… Nodes create that we specified.
That's, and that could be achieved in various ways.
A basic one is to run some control during the CI, so we can check that.
Maybe there are ways to do it at the API level. I'm not sure that we need to go there. I don't know. We definitely need to put control in place.
Utkarsh Umesan Pillai 00:33:25 Okay.
jmacdonald 00:33:30 Do you want to look at some of the more controversial proposals in your listing?
Tuesday, yeah.
Laurent Querel 00:33:35 Yeah, it was… So which one do you want to go next, Joshua?
jmacdonald 00:33:41 I… let's see, good question. I didn't have it, I don't have that, let's see. I just wondered if you had, The one that I think interests me, as far as irritation and frustration and friction I've felt in the past, would be the outputs representation. Like, it started to worry me that I have to list, like, round robin every single time I specify a component. I think that was the one that I felt a lot of warmth for, but.
Laurent Querel 00:34:11 Yes.
jmacdonald 00:34:12 So let's… let's talk about that one briefly.
Laurent Querel 00:34:15 Yeah, I totally agree. I think that's typically one where we don't, follow this principle, optimizing the user experience. I mean, it's, it's, the system in place the output, field that we have, Bernard.
At least for the receiver and the processors, we don't have that for the exporters, obviously.
And, it is… it's super annoying, because… It's basically, showing what are the internals without taking care of that the most common use case is where, basically, you have a NUD. So, most of the use cases are the following. You have a receiver connected to a processor.
And you just described a link between these two things, or same thing between two processors.
Processor and exporter also.
And, because we have things like output ports, then you have to name a… there is a default name that you have to specify, then you have to specify a list of, node ID, even if you have one, and then you have to specify the dispatch strategy.
Which, everyone is using their own robin right now, because that's the only one that is implemented when we have multiple destinations.
Super annoying. So, I'm suggesting the following updates. So, first, we rename output to output. So we have a node, there is output, and when it's output, we just specify the node ID, Of the next, up into the… this subgraph.
So, we are into… For example, a very, very basic situation, we have a receiver connected to an exporter.
We can't make things simpler than that. So the receiver will have an output to the name of this exporter.
Then, when we have multiple destinations.
And when we have multiple destinations, that thing that happens, for different reasons, Evan, you… either you want to replicate The telemetry stream traversing this node to different destinations, or you want to… A load balance, or to do some more advanced way of dispatching those messages across multiple destinations.
So… When we have multiple destinations, we have outputs, and then we enumerate the list of IDs.
For the destination.
And we, consider that the… what was named dispatch strategy come with default, so you don't have to specify it, and the default is balance. So it means that, by default, we just load balance. We can revise the default, but, That's how I specified it right now. And… and then we have named output, which is a really cool, in my opinion, capability of the system.
Which does not exist at all in the Go Collector, as far as I know, but we leverage it for many things, like the signal, the signal type router that we need to rename. The failover processor that we need to implement, that's the kind of thing that, for example, here.
So, you have the failover.
And we will have a default, output.
And, let's say a fallback output here, I have the success and failures. But, we… the name of those outputs is totally free.
So you specify a name for the output, and you say, okay, when has… so the node using this configuration, could use the sendMessageTo, method offered by the effect handler.
specify the name of the output.
and the message. And then, automatically, under the, under the hood, the system will send the message to the right destination. So that's a way, basically, to wire very precisely what you want to achieve. And the semantic of that, is decided by the node. So that opens a lot of patterns that we can implement, and that's how we will implement, for example, the failover.
That's how we implement the router basin type, because we have basically an output for each type, like, logs, metrics, and spam, and so on.
And I finish, and then I let, Andres, ask a question. So the… the… the next thing that is not, I should have had, A comment at the end saying that it's not alone, it's going with the policy.
proposal, and, I, I saw, Drew, having some trouble about that initially, and then, you saw the, the 1830. It's basically…
drewrelmas 00:39:52 I just looked at the next one, yes.
Laurent Querel 00:39:54 Oh, I mean, I mean, I will do the exact… I mean, that's my fault, because I should have the… It's hard to decorate them, but, so the… The… the thing is, how can… how, with this proposal, can we, now specify that for this specific case.
we need either to load balance to the different destinations, or we want to replicate the traffic. And that's the purpose of this policy as a first-class concept.
Proposal 3 that we can discuss after.
Zoom voice.
Andres Borja 00:40:36 Yeah, so… I'm still trying to understand the use case.
for… these kind of services of the balanced one, right? So… It makes sense when you want to do some… Load balancing, but… I'm having a hard time to understand a loan balancing situation.
For a single… engine running, you know, and… What does it mean for the limited… I don't get much, so that's why… Yeah, I don't understand the balance one, and… And also, why is the default, right? For me, the default is purely Sending it to multiple destinations, the same thing that you do in the regular collector.
Laurent Querel 00:41:30 Yeah, so that, I totally agree with you.
Andres Borja 00:41:34 They, you know…
Laurent Querel 00:41:35 There is, in fact, beyond that, there is, an implementation reality, or a current limitation that make me define the balance default, but, soon will be… will become broadcast.
Andres Borja 00:41:52 That's not nice, but…
Laurent Querel 00:41:55 So that's why it's currently balanced, because if we… currently, we rely on… Channels?
Either, channel that we implemented ourselves, or channel that we reuse, from the… I think, ecosystem.
each of them, so that… the one at least that we use, for example, Flume and Tokyo channels.
We use the MPMC, sometimes some other variant of that.
so that's what… and currently, we don't support broadcasts. Broadcasts come with a little bit more complicated situation.
It's much more complicated to implement a broadcast than it is to implement an MPMC.
The reason is… What, you, you always have more complication with the broadcast, because the destination… destinations could be slower. Some of them could be slower.
So, what are the behaviors that you want to see with your broadcast channel when, you have such complicated situation, one of the destinations is broken, one of the destinations is much slower than the others. So you need to come with policies And they are not necessarily easy to define.
And to implement. So, we started simple. We started with basic MPMC, basic MPSC, But I think once we have the broadcast, we should revise the default and say, okay.
For the specific context in which we are, like you said.
It makes more sense to default on broadcasts, because that's the most common situation.
and let people do the balance when they want. But right now, I should say that it's a temporary, default.
If that makes sense.
Andres Borja 00:43:59 Yeah, I mean… My concern is that… We… we should, implement the features more with the user in mind, you know, and the use case in mind.
More than, hey, this is what we have, and this is… The reason why we wanted to do it like that, to… to prove.
Laurent Querel 00:44:20 Yeah, but we are perfectly aware of that. That's exactly why we are doing this, this effort.
the… The reason why we moved to, to, to the current situation to this one, is with the user in mind. So, yes, I agree with that. Now…
Andres Borja 00:44:39 That's true.
Laurent Querel 00:44:40 I'm just advocating for…
Andres Borja 00:44:42 something not broadcast… broadcast, right? Something like… more like balance. I don't understand that use case. What is the use case of that?
Laurent Querel 00:44:51 But there are use cases, I mean.
It's like any project. You start with, you want to prove and deliver something. Maybe the other option will be, oh, we don't support multiple destinations.
And and you will be more satisfied, maybe.
But.
Andres Borja 00:45:11 That's clearly not…
Laurent Querel 00:45:14 Sorry?
Andres Borja 00:45:15 That's clearly not the main use case, so… so again, let's… don't go into the trap of, this is the technology we have, how can we use it, but the other way…
Laurent Querel 00:45:23 So, do you want to implement the broadcast? Or, I mean, I'm totally okay with your requests. I'm just trying to achieve something that takes into consideration what we have today.
And I also recognize the fact that we need to implement the broadcast. In fact, I'm already working on it, but it's taking more time than I was expecting.
Andres Borja 00:45:47 That's okay, John.
the… the other kind of, like, related question or thing that I have is.
It looks like we are combining the boat, like, the name and the… broadcast strategy, right? So, the naming is… for me, it's like different levels, right? One thing is that you decide to route your Events or your messages, you know, your payload in… to different destinations, that's… that's one thing, which is great, I like it. I like it a lot, by the way. The use case that you present there is… it's… is the use case that I think is super powerful.
But then the other decision is what happens after that, right? If you, inside your component, decide that this is a failure, and this is a… Success?
The decision of what happens after is, again, going back to the other question.
How do we want to send it? Do you want to send it to one single one? To multiple of those?
How to do the multiple destinations.
So I think it's two levels. I don't think they should be combined.
Laurent Querel 00:47:01 For this one, I'm not sure to follow, because… I explicitly, separated the… the routine.
And what we see here is only routine, by the way. There is no broadcast, there is no, load balancing or more advanced way of… when we have multiple destinations, what we do.
That is not part of this, Proposal 2. That's part of Proposal 3.
So, can you maybe reformulate what you…
Andres Borja 00:47:36 So…
Laurent Querel 00:47:36 I have to express their own.
Andres Borja 00:47:38 For example, in the name outputs, room.
When you say success, That is multiple destinations.
So you have You need to define that.
broadcast or something. So that's what I'm saying, that is two levels. One thing is to… the size… What is going to be the destination, independent on if it's one or many?
I mean… the…
Laurent Querel 00:48:05 I see.
Andres Borja 00:48:07 One thing is to decide the name output, and the other thing is, okay, now that it's in this.
Name output.
how it's gonna look like? Is it gonna be single or multiple, and if it's multiple, what is the… broadcast strategy or the… I don't know what you're calling it.
Laurent Querel 00:48:24 Yeah, so let's put…
jmacdonald 00:48:25 about…
Andres Borja 00:48:26 Two things, that's what I'm saying, is two things. One thing is to use the name things to route it, and then… The second thing is once that is there in that channel, or in that…
Laurent Querel 00:48:38 Amazing.
Andres Borja 00:48:39 We'll be doing it, you know?
Laurent Querel 00:48:45 Is that true?
drewrelmas 00:48:47 We've graduated to talking about the number 3, I think would make things clear.
Laurent Querel 00:48:54 Yes, but I think the… I agree.
But I think the point that Andres raised is… not exactly about the Proposal 3, which, Deal with the DISPAS strategy and many other policies, but… More the lack of consistency.
between, if I reformulate what Andres is saying, and that I understood, I hope.
Here, we did, something like, oh, we can specify one output And… or two, or multiple outputs, and… and we don't pay the cost of this… syntax and approach when we have to just specify one. We have something that is natural and simple.
Which is not the case here.
When we enter into the named output world.
Then we… we enter, and my default was always, oh, we can… we always have to specify, even if we have one, to specify the… the syntax with the multiple.
So, maybe, in order to be more… aligned and consistent, between the… the unnamed output versus named output. Maybe we need to It's adding a little bit of override, in my opinion, but we could have something like that.
Or, something…
Andres Borja 00:50:26 I think… I think it's two… if you want to talk in terms… I think it's two different concepts, and they should be treated by a separate problem with different concepts, because they have different concepts, right? So if you want to… Think on an analogy for the transportation things, right? One is the port.
So I'm sending these things to this port, and the other thing is the destination. Once they are in that port, they are… their destinations might be different.
Laurent Querel 00:50:53 Can you, take the time to add a comment, Andres, to this, 1829, and come with a proposal that will refine that?
Andres Borja 00:51:03 Sounds good.
Laurent Querel 00:51:04 And I think that, that will be, great.
Joshua?
jmacdonald 00:51:11 Thank you. I just want to do a little time check. I, I do… I think there's some confusion here. I think I'm feeling confused as well about… about how Ack and NAC wouldn't be handled in a broadcast scenario, but I think we're gonna run out of time to have this… this debate, or this conversation at length.
And I want to reserve a little bit of time for the other two items on the agenda. I can accelerate just a quick note about what's been happening in internal telemetry, if that's okay with everybody. I think it's worth sharing in the group so, the… I… I will… I'll try and cut this from 10 minutes down to 2 minutes, just to say that we have done a sort of quick, I would say maybe a little bit faster than comfortable for me, redesign of the internal telemetry configuration and setup across the entire codebase.
This PR that is in front of us right now is essentially the last in a long series that gets us to a place where we can begin using the pipeline to process its own telemetry.
There is a, you know, because this is sort of the last in a, at least in a sequence, there's an update in the README file here explaining how to configure it. There's an example configuration of how to configure it, and it uses this new console debugger. So there's a configuration right in front of us, using the And it has both nodes for the first class pipeline, and it has internal for the internal pipeline. The internal pipeline is using the internal telemetry receiver and a console exporter, nothing more.
So this is, like, a basic demonstration of what we have. Notice at the very bottom, the service telemetry section, that's, like.
in the OpenTelemetry declarative space, I've added stuff that's not part of OpenTelemetry declarative, so there's some configuration confusion that we've got now. And I wanted to treat that as separate, but now you can say that you want your global Tokyo Tracer to use the ITS, you want your engine to use the ITS, even administrative threads can use ITS. The only thing that can't use ITS is then the internal login configuration, so we have an internal setup to make sure we don't have feedback loops and so on.
This is, This is open with the internal telemetry receiver component, and I'm waiting for reviews. This basically modifies the controller to start an engine thread if we need one, but all the prerequisites were done earlier in the week and last week, so this is not a very large PR, and I'm ready for y'all to review it. Once this goes in, we can begin running whatever you want, KQL processor on your internal logs or something like that.
Or, OPL processor, transform processor, whatever you want. That was the goal we were trying to get to. I… I know there's more to do. In my next, sort of, sprint forward, what I'm planning to… to get to, is to complete the The telemetries, were missing attributes from the scope or the component-level attributes.
Laurent has been putting them into thread local variables for me, and task local variables, so that, in theory, this won't be a very tricky one, and we're just going to start having those variables, those attributes on scopes.
next week.
I think that's my summary. I don't want to belabor it. If anyone has questions, we can talk.
Andres Borja 00:54:32 My comment, I added in the previous VR, but I still want to mention it. I think it works.
What looks to me, like, very similar is, like, it looks like we are defining a separate graph for the internal one, so… Same question I have, now that we have support for multiple graphs, multiple pipeline groups.
Why is this just not yet another pipeline group?
jmacdonald 00:54:58 I have kind of the same question, In fact, when I got to doing this PR after Laurent's recent work, I real… like, I have to choose a pipeline to find the internal nodes, and I just find the first one.
It's confusing, and it's incomplete. I don't know what to do here exactly, but Laurent was gonna take over the question from me. Having put the internal nodes there, I'm using it, it's not in the right place.
Laurent Querel 00:55:24 Yeah, I think if we follow the model of a very mature and robust model, like relational databases, for example.
They already answered this question, and we need to follow the same principles, in my opinion. So, yes, now that we have… and it's very recent, it's a few days ago, so we are reacting very quickly, but I agree, we need to reuse the same mechanism.
And by the way, that's what already we are doing. We are reusing the pipeline. Now we are… we have to go one step further and reuse the pipeline group mechanism. So we will have an internal A pipeline group that will be always there, which will be, reserved, and on which we will put the various pipelines. For now, only one, the internal telemetry system pipeline.
We could imagine some others.
we discuss, for example, why… another… probably that will be part also of ITS, but maybe that will be part of a different pipeline, that's something we need to discuss, but this concept of observed state.
That we already have, which is not reusing the pipeline mechanism, which is… Something very powerful that we need to finalize.
And, and basically, which is, providing the output for the, status endpoint, and any variation around that. The really easy, liveZ, blah blah blah.
So it's, it's basically taking, the important, engine-level pipeline from low-level, but, well-defined event of this engine.
combine that on a topology in order to derive what is the real status of the engine, or per pipeline group, or per pipeline, and so on. So that, this… Smart aggregation of events in order to end up with… real, definition of status and judgment on where the system is, is something that could be also implemented as a pipeline, either in the ITS or into the… a different one.
jmacdonald 00:57:47 That makes sense. But I really like the…
Laurent Querel 00:57:49 Yeah.
jmacdonald 00:57:50 Right now, we have a single global admin thread that does that status page, and I think what you're imagining is that we would have numerous regional, like, aggregations of events Which would then have a channel to the admin, so, like.
But I think what you're saying is, I've seen this dream alive in the collector world as well. It's like, we'd like to have a page where you can go see, like, snippets of status information, including recent log events, and we're closer to that than we were, you know, yesterday or last week now, to where you could imagine having the status show recent logs, which is, I think, a good requirement when you're running headless services that are collecting their own logs. Like, if the logs collection is broken.
and I'm just gonna go directly to the status page to figure out why.
Yes.
So, thank you. We hit almost the end of the hour. I had a, like, kind of open discussion at the end of the agenda. I'll just say what I wanted to hear us talk about so that we can think for next time. It's that there's been some talk of multi-tenancy, and how that would look, and there's so many ways that that could look.
But I've started talking with the team here about, like, there's some discussion in Slack about global channels or named channels. I'm starting to want to know how we would take an overload situation, like one core is getting too much work.
And it… it's… it's not because of network-level load balancing, it's just one thread is getting too much data. How could we distribute data from one thread to n threads?
In a… in a proper way. And I… and I think that global channels are involved. That's where I'm… I'm kind of interested in talking about for the, you know, just the telemetry pipelines need the global channels.
Laurent Querel 00:59:36 Exactly. I encourage everyone also to read, for people that really want to go deep in this kind of discussion regarding the how a search engine can work. There is a paper that I copy-passed, but I put a link on it into the… I think it was in Controller.
So yeah, there is this graph that is updated, and there is… this paper.
jmacdonald 01:00:05 More so… okay, yes. Oh, you've shown me.
Laurent Querel 01:00:07 Yeah, okay. Read it. It's, the last evolution of the thread per core.
Slightly modified to address, speed and more flexibility, and I think we have all the components to do it, which is really cool.
And the name… the name channel mechanism was part of the option. So we have an engine that is flexible to address various, various situations.
jmacdonald 01:00:38 I'm not sure I like the word morsel, but okay.
Laurent Querel 01:00:41 Yeah, I mean, I didn't decide the term morsel. That they are their thing, but anyway, the paper is nice. And done by people that are very well known in this space.
jmacdonald 01:00:53 Yeah, I recognize some of those names. Okay, cool.
Laurent Querel 01:00:55 Yeah, the…
jmacdonald 01:00:56 That's a great start. We can talk about that in our next meeting.
Which will be Tuesday?
Good. Thank you all.
Good one. Alright, next to you. Next time.
Utkarsh Umesan Pillai 01:01:08 Dude.
Albert Lockett 01:01:14 Hi, everyone.
