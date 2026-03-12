SIG: Entities SIG
Date: 2026-01-12
Duration: 48 minutes
Zoom Recording URL: https://zoom.us/rec/share/5xnT3Ar_uDL32j1OHmJRztXt-VhNlqNtOUOvIPIb3z_5sdYkWjUpNZhOfwPvrWW_.4jqYLGFflc1C_995
============================================================

## Zoom Recording Transcript

**Josh Suereth** 01:26 P.
**Dmitrii Anoshin** 01:32 Hi, Josh.
**Endre Sara** 01:37 Hi, Josh.
**Dmitrii Anoshin** 01:42 Happy New Year, I guess.
**Josh Suereth** 01:47 Yeah, Happy New Year!
Hope you had a good one.
**Dmitrii Anoshin** 01:52 Did a good… I had a good break, at least.
**Josh Suereth** 01:58 Yeah.
Sorry, I'm just getting everything spun up here.
Great.
Right.
Alright, should we get started? What do you think? Think we're gonna have more people?
**Dmitrii Anoshin** 02:40 You can get started.
**Josh Suereth** 02:42 Okay.
Oh, I'm not presenting.
Okay.
Give me a sec… tab… Resource submitted, here we go.
Cool.
Yeah, so you want to talk about the event spec?
**Dmitrii Anoshin** 03:02 Sure. I assume this is hot off the press.
Yeah, I do.
And, yeah, the… it's pretty much nothing… like, no surprises here. And here I specified why do we need that. First is that when there is no telemetry associated with it, or users don't want telemetry is not important as comparing to entities themselves. Complex distributive information, for example, config maps, when you don't want to send the whole payload as an attribute value. Relationships, which is something that we are missing In the resource attribute and lifecycle tracking, if entity has been changed, like.
quicker than telemetry, reporting interval.
Yeah, so… We can scroll down, I guess. And here's the data model. I'm not sure if we need to stop Yeah, like… spend more… much time on it, we can… it's probably something that we can discuss offline. The biggest thing here is, I won't discuss on this call, is how we send relationships. I've been thinking about if we can send them as a separate event.
But, eventually, I don't think that's, like, maybe necessary, because… Aww.
Typically, when a relationship Has… when relationship changes, it means the entity changes itself as well. It's very… I think it's pretty rarely that relationships… relationship would change outside of the entity lifecycle. So I think it makes sense to keep it simpler and have entity relationship as an array, specific to Particular entity, which potentially can be, like, either either of them. If it's two, like, entities relationship, it can be reported on the either side, but typically, potentially, it can be, like, the entity that's kind of responsible for that… established that relationship, in a way. So, yeah, go ahead, Josh.
**Josh Suereth** 05:25 I think you're kind of answering my question, but basically, yeah, so what I'm getting is there's a… there's an idea that an entity owns the relationship between two.
**Dmitrii Anoshin** 05:35 What?
**Josh Suereth** 05:36 That entity would report the relationship, as opposed to both entities reporting the relationship, right?
**Dmitrii Anoshin** 05:41 Yeah.
I can put it in words, but that was, like, implicit assumption here, is, like, whether the entity that has, let's say, more information, like, whether established the relationship or owns the relationship, sometimes it might not be, like, apparent, and in that case, either of them And if… If both of the entities report a relationship, that also should be fine. We should not restrict… we should not have an, like, assumption that only one of the entities always report a relationship.
**Josh Suereth** 06:15 Yeah, we just… we need an idea in the model for how we design this thing for, like, rules and all that kind of junk, right? Because we're… you're reporting edges here.
the related question… I, like… I agree with you that we should be flexible, but I also think you should, like.
give people guidance, like, prefer to send the relationship from the owner, or the person who's, like, responsible for forming the relationship. If that's not apparent, you could send it from either, that's fine.
If both people have access to it, right?
But this, so this array of string to any value, Right, I want to dive into that a little bit. So the string would be, like… the role of the relationship, like, this is my parent, or this is my… if I'm a deployment, like, I'm the owner, like, this is one of my… instances or something. And then the any value is a reference to the entity, which is your… that you have a relationship with.
**Dmitrii Anoshin** 07:14 You can click on the Edit Relationship, I go into more details about that.
You can click on the link.
**Josh Suereth** 07:21 Let me… let me do this, let me view the file raw, because then the links will work.
Okay.
**Dmitrii Anoshin** 07:28 So I covered that part.
**Josh Suereth** 07:30 Yeah. Yeah, relationship has a type.
**Dmitrii Anoshin** 07:33 This, like, explicitly separate, attribute field, kind of.
And that type would be scheduled to contains dependencies, etc. And entity type and entity ID is the, let's say, target entity.
I kept the same field names as we have for the entity itself. I don't think it's gonna provide any confusion, but if it… if you think it's confusing, we can call it, like, target.entity.type or something like that.
**Josh Suereth** 08:04 Right, right, right. Because the relationship's defined on the entity, so you already have an implicit from, and this is the to, because it's in a relationship. Yeah, yeah, yeah, gotcha.
**Dmitrii Anoshin** 08:16 And also, I added attributes to the relationship. We probably never will need that, maybe I just remove it for now, but I was thinking, like, potentially, if we want to have, like, same, let's say, like, additional metadata to the relationship, we potentially Right?
have it.
**Josh Suereth** 08:36 Yeah, so basically, this, this, I think, the relationship, I would… I would almost call it the… the role of the relationship.
**Dmitrii Anoshin** 08:46 Okay.
**Josh Suereth** 08:47 But type works. I'm just trying to figure out, you know, because this might differentiate these a little bit.
And then you have standard relationship like, types of roles. Runs on, schedule on, contains, part of, depends on, manages, hosts. Don't we have, like, same as, as well, or what did we call it? .
**Dmitrii Anoshin** 09:08 Yeah, I haven't mentioned those. They are kind of… the list… obvious, I would say, but yeah, probably need to mention them as well.
Same as.
**Josh Suereth** 09:22 Okay.
**Dmitrii Anoshin** 09:24 So you want relationship, role, or type? I use type because we have entity type, so kind of keep it a bit more consistent, I don't know.
**Josh Suereth** 09:32 Oh, that's fine, yeah. I, I, I'm just… I'm trying to think of, like, how to think about this and, like, what these are. This… is this meant to be an open set where people can add more, but maybe this is a thing that we have in, like, semantic conventions of, like, here's the ones O hotel has agreed to?
**Dmitrii Anoshin** 09:49 Yeah, that's what I actually mentioned. Semantic relations must define standard relationship type, and the custom relations… relationship type may be defined by the… to represent domain-specific relationships.
**Josh Suereth** 10:01 Okay.
Yeah, this is why, like, there's an alternative in my head here of, whether relationships are the same or not. From a semantic convention standpoint, right, what I'm asking is.
would I model this as a semantic convention?
Independently of an entity.
Like, how do I add new ones to this list?
**Dmitrii Anoshin** 10:31 I guess there should be some kind of… Separate… Set of types, and then each entity would reference those.
**Josh Suereth** 10:44 Yeah. Okay.
**Dmitrii Anoshin** 10:46 Well, we have examples like that in semantic conventions, I believe.
**Josh Suereth** 10:51 We… we don't have as many as you'd think. Okay.
Yeah, yeah, I… sorry, I'm going from a standpoint of, like, you know, I always ask the question.
how do I define this in the model so that it all fits together, right? Because, like, this makes sense naturally, but now I'm thinking of, cool, if I have to expand this, what does that look like? Who makes that decision? And how generic does it have to be, right?
Because hosts right now is just any infrastructure to workload of… I have a workload that is hosted on something.
Cool.
How is that different than scheduled on?
**Dmitrii Anoshin** 11:30 I see what you meant.
**Josh Suereth** 11:32 Because one is one direction, the other one's the other direction.
**Dmitrii Anoshin** 11:35 Yeah, we would definitely prob- we probably need to define the, like, the opposite types.
in the semantic conventions as well. So schedule tone would be… Ma.
Like, host or scheduled by?
As a, as a, as an opposite.
A relationship.
**Josh Suereth** 11:55 Yeah.
**Dmitrii Anoshin** 11:56 So, it's potentially something that we would need to… Oh.
**Josh Suereth** 12:01 Managed and managed by could also be a relationship, right?
**Dmitrii Anoshin** 12:05 Yeah.
I probably would add this to the docs to make it clear that we have, like, both parts.
Defined.
this example.
**Josh Suereth** 12:20 Yeah, it could… It still… it still makes me wonder… Because the other alternative here is whether or not relationship is its own thing, where you'd have a relationship type, and then you'd have a… like, this would become entity ref, and you'd have a, like, from to.
rape.
**Dmitrii Anoshin** 12:40 Yeah, I couldn't think about an example, but in theory, it's possible that the relationship can be between more than two entities, right?
In that case, we are…
**Josh Suereth** 12:56 Well, actually, yeah, here's an example for you. Replica set to pod.
One replica set can manage multiple pods.
Because it's a replica set, right?
**Dmitrii Anoshin** 13:10 I mean, there's several types of the… several types of entities. Let's say, like, a three-way dimension, three-way relationships, not this one.
**Josh Suereth** 13:21 Oh, oh, I see, I see. So, like, yeah, would we need to have…
**Dmitrii Anoshin** 13:25 So what's… Promptu would be restrictive. In that case, if we go with the separate things, potentially would be, like, kind of a list of entities, and then… I don't know if we even need that, but…
**Josh Suereth** 13:42 Well, this, yeah, I guess this here, this doesn't support.
**Dmitrii Anoshin** 13:46 This also doesn't support that, but that's what I was thinking. If we have a separate, let's say, event for the relationship specifically, what would we gain by that? I was thinking, potentially, we can have, like, a three-way relationship can be supported by that. Also, we can have like… Different life cycle, separate life cycle.
And then, another, another benefit is that we don't need to worry too much where the relationship is, set by, like, whether it's by host or host by, so we have one relationship to cover both of them, both of the entities, kind of, equally.
But at the same time, like, I was… I think the… this simplified approach provides more, like… Let's say, easier to handle, and by the backend, and easier to data model.
So… Cool.
**Josh Suereth** 14:57 Is that… is that… that's true? So, I'm thinking of… maybe I'm thinking too much about a graph database.
I'll give you an example. Like, I envision the entity event Having, like, a state section.
**Dmitrii Anoshin** 15:11 Or, like.
**Josh Suereth** 15:13 Almost like a dictionary section of, like, here's all the entities and their current state, and then have a relationship section.
And when, like, when you use, like, the more formal graph algorithms, basically, those graph algorithms, you record nodes and you record edges.
And that's… that's the equivalent of this message, right? Of, like, here's the nodes, here's the edges.
And then when you do queries, you basically do graph queries on, you know, give me an edge that has these attributes to it, and that sort of thing. So I'm… I'm looking at your data model, and I keep seeing that.
And I keep thinking that we should have nodes and edges separate.
But, like, I… let me… I haven't thought deeply about this. This is just, like, you know, off the cuff, how I'm thinking about it compared to things. So, and I'm… you know, if I were to throw this into a graph database, I know that I would basically convert this into its own Edge structure, anyway.
**Dmitrii Anoshin** 16:09 Right, right. That's gonna be… that's the case, I'm pretty sure, on the backend. But here, we are specifically thinking about data collection, but we… I think we should abstract from how it's gonna be stored, and take more into account how this data modeled and how it's being collected.
And, like, let's say in Kubernetes, in Kubernetes, whenever… it's an ideal example. Whenever something is changed, it's always been changed with all the relationships.
**Josh Suereth** 16:41 That's true in Kubernetes. Yeah, I don't know if that's necessarily true everywhere, though, but I'd have to… again, that's… I think… let's… let's take an AI… I'll add that to the notes, AI.
Let's… Look into relationships as their own thing.
And determine which way… We want to model this. Like, I'm… I'm fine going the direction of… this, once we kind of think through it. What I want to do is find out, like, okay, we know in Kubernetes this will always be true.
What other systems are we going to model? Will it be true for those systems?
And, you know, will it make sense to be able to report the relationship separate from the the entities. Like, it… will there be a case where, like.
someone might own the relationship, but not own the entity itself. That second thing, I think, is more likely to be true.
Where someone might, like… you know, I might own part of the entities, but not all of them.
I guess your thing would work here, because I could report the entities I own, and then the relationships from one direction, and you would infer that the other direction is there, too.
Yeah.
Okay.
Anything else have thoughts, by the way? I don't want to monopolize the conversation.
Okay. Go ahead, Dimitri.
**Dmitrii Anoshin** 18:20 Yeah, Nothing to add from my side. We… this is something we can discuss more on the PR. I can maybe submit… let's say, I'll put in words what pros and cons I considered between both approaches, because, yeah, I considered this as a separate… initially, actually, I was thinking that that should be a separate, let's say, state, that is… Separate, yeah, separate state, type of state. But at the same time, whenever I ended up that I would need to how I would need to model… this is how it went for me. So, when I defined the relationship state, like, we have event state, event delete. Oh, sorry, entity state, entity, entity delete, event. Then I added entity relationship, and then I was like, you know, should I support, like.
three-way relationship, maybe not. In that case, it will be two from, only two, entities.
But then, like, hey, whenever this relationship changed, what should I do? I need to re… I need to introduce Entity Relationship Delete Event. And in that case, entity relationship delete event would be… I would need to have, like, let's say, identity for the relationship would be… which would be pretty complicated. First entity, second entity, ID, type, etc.
So, it… it went… pretty complex.
After that.
And at that point, I was like, why, like, specifically for cobranes being, like, as a primary example, it's not gonna happen anyway. Like, life cycle is pretty much aligned with the entity lifecycle.
So I went with this one, just for simplicity and data collection. But if we have examples, good examples.
When entity lifecycle… entity relationship lifecycle completely decoupled from the entity themselves, and, like, owner, whatever, isn't clear.
So, yeah, I'm happy to change it back.
**Josh Suereth** 20:24 I do have an example of that.
let me convert it into OpenTelemetry, but let's imagine you have… You have a system like, so we have one in GCP called AppHub. We have, let's say you have ServiceNow.
let's say you, you have something that manages, like, what it means to be a service in OpenTelemetry, right? Let's pretend like I have a system that does this, and I actually register things, and I say, cool, this service is composed of these 5 things.
And then I want to unregister one of them.
That is something that you can do. You can say, like, cool, I, like, in my, in, in my, in my visualization tool, I can add and remove an entity from being part of some, like, application or service, like the logical group, right?
So this would be like an OpenTelemetry service, or an OpenTelemetry service namespace. I could add or remove things to it.
In a visual standpoint, right?
**Dmitrii Anoshin** 21:21 And when you remove a service, what does it mean? Do you just make it, like, part of none of the namespace, or you are…
**Josh Suereth** 21:28 Yeah, basically, I would take a workload, and I would just remove it from being part of the service.
So, I just unregister it. But all it does is remove that one connection. It doesn't do anything else.
**Dmitrii Anoshin** 21:39 And that's… that's in the, like… What could remove that? It's an action made by the user, right?
**Josh Suereth** 21:46 By the user, yeah.
**Dmitrii Anoshin** 21:48 So, in that case, I think this model also works pretty well.
**Josh Suereth** 21:53 This model works, but there's some downsides that we'll have to call out. Basically, like, you're saying, cool, when I update a relationship, I emit the entire entity in every relationship. When I delete a relationship, I admit the entire entity with the relationship removed.
If it's the case where, like.
I don't want to omit every single relationship, because there's a lot of them.
**Dmitrii Anoshin** 22:15 Yep.
**Josh Suereth** 22:16 It's a much cheaper message to send to say, cool, just delete this one thing as a diff.
And then the next time I get state, like, when I do my… Rolling update, I'll get everything.
**Dmitrii Anoshin** 22:30 I see.
**Josh Suereth** 22:31 That would be… but I don't… like, in the instances I'm talking about, those aren't frequent occurrences. Like, they don't happen that often.
**Dmitrii Anoshin** 22:39 Yeah, and here we need to keep in mind that entity state is being sent periodically.
**Josh Suereth** 22:45 Yep. So you're gonna… you're gonna get updated state no matter what, eventually, yeah.
**Dmitrii Anoshin** 22:49 In the middle of those two updates, you potentially just send one more, with removed relationship. For example, you remove this workload from a service that, let's say, entity workload.
would be updated state, and nothing else needs to be changed. And then you can potentially… depends on the implementation, but you can delay the next… next state after that.
So, the… from the payload perspective, it's not… it's not that much.
Oh… For change. But if we have, entity relationships, we would need to send entity relationship delete event.
And it'll be another additional event.
And we will not be sending, those entity relationship state events anymore for that specific relationship.
**Josh Suereth** 23:47 Right, right, right. Like, I… Yeah. I still… I see what you're saying. We need… so for entities, we have a… here's all the known… like, here's all the state of everything.
For relationships, we need a, here's the state of everything that we sync to. Like, it has to be all-encompassing in some fashion. Yeah. Because you need to know what's there and what's not there. And deletes are an optimization to allow things to happen faster.
**Dmitrii Anoshin** 24:12 Yep, right. Right.
**Josh Suereth** 24:13 I… There's still a piece of me that wants updates, like you to have a fast update in addition to a status of everything.
like, an efficient way to do that, but I… I… I have to think about it.
Like, I think I want this for entity update as well. Do you know what I mean?
Like, just this piece of the entity change. Like, Kubernetes watch events, right?
Do they re… they return the whole thing, or they just tell you something changed?
I'm trying to remember.
**Dmitrii Anoshin** 24:45 I don't… I think… Hmm.
In which event, you actually get the full payload of particular.
**Josh Suereth** 24:52 This will be alone, okay.
**Dmitrii Anoshin** 24:55 And, given that, we… And I believe you should… you should have a conversation with Tigran about that. I believe there are some… there should be a lot of discussion based on whether we do have… do have patch updates or not.
And, I believe the decision is to have states being sent periodically, but if we have only states for the entities.
And do not have.
Like, the same thing for the relationship, it kind of doesn't…
**Josh Suereth** 25:29 we have to have the relationships, too. It's just like… And this is something we could layer on later. It… like, I think that that's not a one-way door, so if we… if we send all the state and just delete events, and we eventually want to layer on an event that occurs between state updates to have faster resolution, we could actually do that without breaking the model, if I'm… if I'm…
**Dmitrii Anoshin** 25:51 It's already implied. I believe. If it's not set in words here, I implied, like, implicitly meant that entity states can be sent quicker if something is changed. Maybe… if I missed it, I'll put it in words, for sure. But that's the case. If something… like, in… in… changed, we need to send state away right away. State event right away.
**Josh Suereth** 26:18 Right. What we need, though, is we need, like, so, when you get a report of all the entities and relationships, right, we need to know if that list is comprehensive or not.
So, am I getting all of the entities? Am I getting all of the relationships that I'm aware of for you as a thing?
**Dmitrii Anoshin** 26:38 And…
**Josh Suereth** 26:39 like, that way we can know what to delete. Like, that's where we do the hard sync.
if you send something in the middle that's partial, we need to know that it's partial, and just, okay, update this thing without re-syncing your state. So… That… that… Right now, if I read this and I'm thinking through it, it's the full state.
**Dmitrii Anoshin** 27:00 Yes, exactly.
**Josh Suereth** 27:00 It's easier to get the relationships. Great.
**Dmitrii Anoshin** 27:02 Always full state. If we… if you get an update, like, entity state with less relationship, it means that some relationship has been removed.
**Josh Suereth** 27:12 Yeah, yeah. Whereas we could, in the future, if we want… if we decide it's a problem.
We still need to update everything. We need the ability to do that. Like, I think that's fundamental to how we've been thinking about this. If we wanted to add update later, we could do so, actually, on top of this model. It would be an event that occurs that says, hey, this is just an update.
And it would occur faster, like, immediately when the update happens, as opposed to at the regular interval when you get your syncs.
**Dmitrii Anoshin** 27:38 Yeah, but that's the idea. Like, if it happens faster, we send it right away here. That's what I…
**Josh Suereth** 27:45 But you're citing the whole state. What I'm saying is, if we consider the whole state to be too expensive.
to send all at once. Like, let's say… let's say you're… you're managing a giant Kubernetes cluster, and I can't… I don't actually want to put all that state in one message, because it's too big.
How do I send it in chunks?
To avoid having that one big sink.
I would send the sync, but I'd send it infrequently, and I would have, like, little updates along the way to prevent so much churn, or so much network traffic tracking state, right?
**Dmitrii Anoshin** 28:17 We actually already have that implemented in Collector, like, an experimental similar.
**Josh Suereth** 28:26 How are you doing it today?
**Dmitrii Anoshin** 28:27 We… we do it in a way that if some… like, we don't track… we don't send the whole state for the full cluster. We only send wherever hasn't been let's say, like, there is… for every object, there is a, let's say, TTL, right? And if that object changed.
Let's say we send every 15 minutes, right? But if pod got changed, within those 15 minutes, we don't send it on the next, on the next sync.
So we delay that, and then we send it after.
If that makes sense. So we, like… like, every… let's say there is a loop, right?
some ticker, and… which is smaller than that kind of TTL. And that ticker would send entity events only for something that has, like, passed the time.
When we have had an… We haven't sent that particular object.
**Josh Suereth** 29:27 I got… so… so in this… in the design of this, you should be able to send, like, the granularity at which you can send Something.
**Dmitrii Anoshin** 29:36 is the entity.
**Josh Suereth** 29:37 is an entity. One entity, yes. And all of the relationships of that entity.
**Dmitrii Anoshin** 29:41 Right, right.
**Josh Suereth** 29:43 So I have to send all of them, but as long as that doesn't grow.
unreasonable, I could send just those independently, and I could split them and batch them separately, right? Like, if we were to have batching or… a batching processor on entities, we could basically take specific entity events, or entities within an entity event, split them apart.
to make a batch and send it out, if we needed to, like, pare down it.
**Dmitrii Anoshin** 30:07 Yes, right, right, right, it can be done. Yeah, it's possible already.
**Josh Suereth** 30:14 You mean in what you already have in the collector?
**Dmitrii Anoshin** 30:16 Yeah, yeah, in the collector's possible. We just specify a split capability in the batcher, and then you'll batch it by the max maximum like, size.
**Josh Suereth** 30:30 Okay.
Last question is, does this… is this important here?
**Dmitrii Anoshin** 30:36 Yeah, this is…
**Josh Suereth** 30:37 is.
**Dmitrii Anoshin** 30:37 I don't think we ever actually put it in the spec, but this is, like, its context of the… entity emitter, let's say. So, like, all of those entities are emitted within the context of a cluster.
**Josh Suereth** 30:55 Cheers.
**Dmitrii Anoshin** 30:55 On top of those entity events is a… is a cluster.
**Josh Suereth** 31:02 Can I… let's see, for example… Oh, gosh.
relationship between… entities in keyed clusters. So let's say I have two Kubernetes clusters, right?
And let's say I want to report a relationship between two entities within Kubernetes clusters.
**Dmitrii Anoshin** 31:25 Yeah.
**Josh Suereth** 31:27 I have to be reporting from the Kubernetes cluster about the… and I have to understand the full entity to report that relationship.
Right? Because only the owner can report that. But if I'm trying to report between the two clusters, first of all.
How do I do that?
Because I… the… the pod itself might not be uniquely identified. Like, if we think about this here, right?
This is…
**Dmitrii Anoshin** 31:54 the ID for the pod on that cluster.
**Josh Suereth** 31:57 So how do I report it between… this is where that whole local ID thing gets awkward, where we have, like.
**Dmitrii Anoshin** 32:03 Entities are only…
**Josh Suereth** 32:05 Unique within some context?
**Dmitrii Anoshin** 32:08 I see.
**Josh Suereth** 32:09 was… yeah, go ahead.
**Dmitrii Anoshin** 32:11 You mean relationships between, Entities which are part of different contexts, like, within different clusters.
**Josh Suereth** 32:20 Yep.
**Dmitrii Anoshin** 32:21 What would be a real-world example for Kubernetes in that case?
**Josh Suereth** 32:28 Let me… I gotta think of something that's open source. Hold on.
Let's say you have a load balancer in front of two Kubernetes clusters.
**Dmitrii Anoshin** 32:42 Right.
**Josh Suereth** 32:43 And I wanted to find the relationship between the services on the two Kubernetes clusters and that load balancer.
**Dmitrii Anoshin** 32:50 I guess the load balancer would report it, but how does the load balancer tell you which service on which…
**Josh Suereth** 32:56 Right? Because the entity would be, I'm load balancing between these clusters, but I'm also load balancing this service between these clusters.
**Dmitrii Anoshin** 33:05 Hmm, this.
**Josh Suereth** 33:05 service. So how do I get to the Cates service when I need the Cates cluster to identify which service I'm talking about, right?
**Dmitrii Anoshin** 33:13 Yeah, that's where it goes when it comes… becomes complicated with this particular approach. In that case, it's having separate separate, like, let's say eventful relationships would be cleaner, I guess.
**Josh Suereth** 33:31 It might be… it might be clear… it… We actually don't even need that, because the load balancer itself could be the one reporting the relationship, right? Because the load balancer knows about the two. But how does the load balancer describe the entities. So load… Balancer. Balancing.
**Dmitrii Anoshin** 33:50 I would think that it's gonna be, as you said, relationship between two load balancers, and how… Anyway, potentially, for those complex use cases, we can always have a separate, let's say, or we can actually have We can utilize attributes of a relationship, I guess.
Does make sense.
**Josh Suereth** 34:19 Yeah. Two different clusters… services in there. Well, this is where I'm wondering if, if we go back to… I'm just taking notes and such, If we go… if we… Look at this relationships, right?
And this is a relationship to a particular entity.
**Dmitrii Anoshin** 34:40 We could make this be a group of entities.
**Josh Suereth** 34:44 So that you have context. And I know that that kind of sucks a little bit, but… So, basically, what I would have is, if I'm trying to define a relationship to a Cates node on a different cluster, I would have… the first entity would be the Cates node, and the second entity would be the Cates cluster. And I'd say the relationship is, like, from me to that two… those two things together as an identity.
**Dmitrii Anoshin** 35:08 Yeah, something like that, or… yeah.
**Josh Suereth** 35:12 But, like, this would essentially be a resource instead of an entity, right?
**Dmitrii Anoshin** 35:16 Or we can have a separate set of fields, like, let's say, entity.
that context.type, entity.context.ad, or something like that, maybe.
**Josh Suereth** 35:25 Yeah, you could have… you could just have, context, and it would be, like, an array of other entities that are the contextual coloration of that entity. That… that could work, yeah.
Okay.
**Dmitrii Anoshin** 35:36 And that would be optional, if it doesn't exist, it means that the same context as this particular entity.
**Josh Suereth** 35:41 Yeah, which is what we expect to be the default, and we don't want to make it too complicated.
**Dmitrii Anoshin** 35:45 Yeah.
**Josh Suereth** 35:46 Yeah.
Yeah, I like that. Okay, Very cool. This is a great start, man. Any other things to discuss here?
**Dmitrii Anoshin** 35:56 No, I guess… we… good? Like, so we… we'll keep it offline to decide on, like.
eventual? Or maybe you can have a comment on the PR.
**Josh Suereth** 36:09 I'll make some comments, based on what we talked about. The main thing that I… so this is just the data model, right?
Justin… Okay, good, because we still need to then figure out how we're going to send the data model.
And I also noticed on here that there's no instrumentation scope.
Which doesn't make me sad.
But… there's two things to think about there. One is, the schema URL that defines, like, the version and the schema of what the contents of the events will be. We need some place to hang that.
and instrumentation scope is how we do that for all the other signals.
**Dmitrii Anoshin** 36:55 Yeah, that sounds good, that's a good place for…
**Josh Suereth** 36:59 Yeah.
**Dmitrii Anoshin** 37:00 Before this.
**Josh Suereth** 37:01 The second is, you know, this here… doesn't look like… like, this is an example, but this isn't like OTLP. This is like a raw log entry, right?
**Dmitrii Anoshin** 37:13 Yeah, I need to put it in, probably, yeah.
Maybe I'd add an… at the… entity here, NDDRef as well.
But, you mean it's like, it's a map, not key-value pairs and attributes?
**Josh Suereth** 37:30 Yeah, I'm wondering if you need, because you have attributes here, and then you have the entity description.
Oh, this is… you were just taking what the collector does today, got ya.
**Dmitrii Anoshin** 37:44 Yeah, it's an attributes of the lock record. Yeah, it's not ideal. I need to No GLPs, like, is it just, like, for… Kind of.
More like to put a…
**Josh Suereth** 37:57 Yeah, this makes it real. Yeah, this is… that's fine, I got… I got what you're saying. Okay.
Cool. So… I do think we want to do a to-do to figure out if scope is useful enough for us to use it for anything.
I have thoughts, but I don't… Yeah.
If we don't use it, I'm not sad.
**Dmitrii Anoshin** 38:17 I mean, it will be used, it's just not in the focus here, but I guess we would need to, like, prepare.
Schema version, and scope.
Name.
**Josh Suereth** 38:35 Scope, name, and version, and schema version, yeah.
Okay.
Instrumentation scope's an interesting one, because it does have modeling implementation… modeling, like, ramifications. So, like, you could say that this is the instrumentation scope tells you that the data's coming from the Kubernetes API, versus it's coming from some other API, for example. So you could interpret things appropriately that way.
If you needed more insight, but, yeah. Okay.
Cool. I will review that one.
That looks awesome.
Thanks for pushing this out.
Anything else we want to talk about there? Can we move on to the AI, or the merge algorithm quick?
**Dmitrii Anoshin** 39:22 Yeah, let's move.
**Josh Suereth** 39:24 Okay.
I don't think I actually had a chance to make changes to this recently, what was the last change?
I just removed the still label. Okay.
So, let's take a quick gander at the state of this. I want to see if there's any remaining blocking changes.
Right. Priority of entities is going to be resource detection, so the model has priority, but we don't talk about it there. And then… Yeah.
So, this was a discussion we had about, should we keep highest priority entities on key conflicts, drop lowest priority entities, and should we have dropped attributes and entities count that we track?
For when we drop things. I actually have a to-do to figure out drop counts, but I wasn't gonna add that to the specification or the data model. That would be a proto-change if and when we add that.
That's the update on this one.
The last comment here was, should we have a failure if you have two entities that use the same attribute key, but have And they both have the same value.
Do you remember we were talking about.
**Dmitrii Anoshin** 40:44 making sure entity keys are completely disjoint from each other? Yeah.
**Josh Suereth** 40:49 Yeah.
Do we have any updated thoughts on that? I did not update this to make it a failure, I still was thinking through that myself.
**Dmitrii Anoshin** 40:58 I haven't… I don't have any new ideas about that. I still believe that we should always… We should clearly separate ownership of the attributes of per entity.
**Josh Suereth** 41:11 Okay. Otherwise, like, processing of that data would be…
**Dmitrii Anoshin** 41:15 overly complicated.
**Josh Suereth** 41:17 Okay.
I do think it makes things pretty ugly, so I'm with you there. Alright.
are pretty ugly if we allow this. I'm just… I'm… there's a principle I have that I think some of the other TC members have too, which is, like.
If the user does something that is, like.
not super crazy, and we think we can limp around and make things work. Let's at least try to make things work, as opposed to literally fail or crash.
Right?
So this is, if somebody's defining a new entity and they do something funky, should we let it through?
Or not? Like, should we hard crash, or should we let it through? There's two ways people view observability. One is that it's absolutely critical, and I should get failures, and I should get failures early, so I don't accidentally design systems that are broken. The second is that observability is like, Kind of a, you know.
Not something you initially start out to do, and that we have a very complicated ecosystem where people are pulling in dependencies, and this kind of a conflict can come from your dependencies, not from you, and you need some way to resolve it yourself.
So, us allowing you to limp along with something that works.
While you, like, open bugs against dependencies that don't work together is better than just having a broken experience.
**Dmitrii Anoshin** 42:38 Because you're not the one who made the decision, you don't own the decision.
**Josh Suereth** 42:42 And so we should let you limp along. Like, those are kind of the two philosophies there.
**Dmitrii Anoshin** 42:47 No.
we… at least we need to define the expectation from the specification and from open parameter specification, right? If you… We can report the error message, log record, log error message, and still, like, allow sending it, but whatever happens after that, like in the collector or whatever, it's just, like, undefined behavior.
**Josh Suereth** 43:15 Okay.
Let me update to say that, then. So, what I'll do is I'll make it so this is considered an error.
And you may see data that looks like this from users, and you can choose to allow it through, but it's undefined behavior.
**Dmitrii Anoshin** 43:32 And.
**Josh Suereth** 43:34 you know, if someone wants to crash, they crash. If they don't want to crash, they don't have to, but at a minimum, they have to issue a warning.
**Dmitrii Anoshin** 43:40 Yeah, I need to think about, like, scenarios when that undefined behavior can crash the collector.
potentially, I can maybe write it in a way that it never crashes, but it's just… like, mixed ownership will just… mess up with your data instead. I guess that should be feasible.
**Josh Suereth** 44:01 Yeah, I think… There's two ways to think about this. I would rather have us issue warnings as early as possible, and then limp along as long as possible. Okay. With things just not crashing and working as best as possible. So you get a warning that you know you need to fix it, but if it's not your fault that it's a problem.
you're not crippled. You know, like, if I'm depending on Library A and Library B, and they don't work together because they are fighting.
I don't want to be screwed.
**Dmitrii Anoshin** 44:34 Okay.
Sounds good.
**Josh Suereth** 44:37 The other option, by the way, here, is we could… offer enough capabilities in, like, the SDKs and the collector to fix this issue.
If it runs… so we can say, and from a merge algorithm standpoint, this is always a bug, but then we need to add other features that let you correct that mistake if you run into it, so that you're not…
**Dmitrii Anoshin** 44:59 I would like to avoid that, to be honest.
Potentially, we can have, like, in the collector, we can have… we already have, let's say, low-level capabilities to change your data. So, for example, OTTL would provide you, like, two ways to…
**Josh Suereth** 45:20 Yeah.
**Dmitrii Anoshin** 45:20 mess up with your data however you want. You can make it, like, valid, invalid, make it… different, right? In that case, yeah, potentially possible, but, like, let's say entity-specific processors and, like, entity-specific functionality would always rely on that.
assumption that… Attributes are owned only by one entity.
But those low-level kind of processors, they can… Have… give you ways to correct invalid data.
**Josh Suereth** 45:58 Okay.
What… I guess what I mean is, if you have those low-level ways to do this, Can we rely on those and make the merge algorithm just fail, and then give people documentation for how to deal with the failure?
**Dmitrii Anoshin** 46:18 Mmm. Like…
**Josh Suereth** 46:19 collector has a way to do that, the SDKs don't.
**Dmitrii Anoshin** 46:22 Yeah, that's the problem, right? If we have merged algorithm in the SDK, they don't have a scheme hatch. They don't… will not be able to send data that they collect if it fails.
**Josh Suereth** 46:32 Yeah, so we'd have to actually update… alright. I'm gonna leave this here for the SDKs, then. And we'll update, like, the description of what it does and why.
**Dmitrii Anoshin** 46:40 Okay.
**Josh Suereth** 46:41 Cool.
Any other thoughts here? Because otherwise, I think we might call it today. My plan, by the way, I'm… I've been 100% on the stability by default and semantic convention, federation work with Weaver.
So I haven't had a lot of time to work on entities, so my plan was to get this merge algorithm PR done.
with, a matching set of SDK implementations, because the next thing I want to do is start actually getting, prototype implementations in the SDK.
Like, as soon as possible.
**Dmitrii Anoshin** 47:20 Fantastic.
**Josh Suereth** 47:21 Yeah, I don't… Daniel's not here. I'll have to ping him offline to see how far the Node.js prototype's going, but, If you keep focusing on the event stuff from the collector, we'll keep focusing on the SDK stuff, and hopefully we can get something out pretty quickly.
**Dmitrii Anoshin** 47:37 Sounds great.
**Josh Suereth** 47:38 Cool.
Awesome.
Anyone else have any topics they wanna… Discuss.
Alright.
Well, have a good week, man. See ya.
**Dmitrii Anoshin** 47:55 Perfect one, right.
