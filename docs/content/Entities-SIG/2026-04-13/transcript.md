SIG: Entities SIG
Date: 2026-04-13
Duration: 26 minutes
Zoom Recording URL: https://zoom.us/rec/share/sObPVOkUpQfoGrc9RrAhnMKm9_KERDX24u4GnvQk41ZtxYSG0oAFmb4KM0ROKu9C.gvzRu0PzD8T5zrFt
============================================================

## Zoom Recording Transcript

**Michele Mancioppi** 00:08 So, this is the fight to take.
Very spicy.
You could say it's the bomb. It's the bomb. What I would have… why would I wish that the project would have done differently is to have a common core for language SDK, so that we would have to go and run around and take semantic conventions all over the place.
It was yesterday, I was yesterday years old, but I find out that, no jazz… has not noticed that HTTP has gone stable, and then the metrics look entirely different.
notice, it doesn't need more hands. And if you're watching this, and you would like an exciting career in open source maintainership, apply to the OpenTelemetry Node.js6. All right. You get no compensation, but you might get to come to CubeSpot and eat really hot, chicken. Do it for the glory. And you're gonna have a lot of AI PRs to review. Alright, so a big applause for my guests who went through hell and back. Nice.
**Daniel Dyla (Dynatrace)** 05:57 Hello.
**Arve Knudsen** 06:01 Hello.
**krajo Krajcsovits** 06:03 Alright, dude.
**Daniel Dyla (Dynatrace)** 06:05 I didn't see Josh Surith in the… SEMCOM meeting today, which he normally joins.
I don't know if he's working today, let me send him a message.
Josh said he will be late to the meeting today.
I don't see anything on the agenda so far.
I was going to discuss, the SDK startup, but before that, Martin, do you have any update on the, Browser… Prototype for entities, or is there no change there?
**Martin Kuba** 07:45 So I was actually out last week, but I know that it's… the SIG is working on the prototype.
I don't know the exact state. I think we're… We should probably have something, something… Demoable soon.
But I had to check on the status from last week.
**Daniel Dyla (Dynatrace)** 08:06 Okay.
Yeah, so sounds like no update there. I also have no real update on the SDK startup specification. I did start a draft of that.
But I have some questions that I… need Josh for, to be completely honest.
He said his daughter is sick today, so he's home taking care of her, and he'll be late to the meeting.
Dimitri will also not be here, apparently.
Ted, is there anything that you wanted to raise today?
If not, it might be better to just cancel this iteration without Josh and Dimitri.
**Michele Mancioppi** 08:56 I have a couple of questions about, the… the entities, that came up from a discussion with Dimitri at KubeCon.
Yeah.
**Daniel Dyla (Dynatrace)** 09:07 Go ahead.
**Michele Mancioppi** 09:08 Who's not here, maybe it's worth entertaining.
So, something that I'm missing from, the OTABs and, the minutes and what I'm… what I could find, at least online, about entities, is… How backends are supposed to reconcile the overlapping information That is coming through entities and resource attributes.
**Daniel Dyla (Dynatrace)** 09:34 Yeah, so… ideally, I think this is covered in the data model, spec, but ideally, or not ideally, that there is no overlap Specifically.
Attributes should be… Either a part of an entity, or they're a part of, like, an… The resource without, without an entity associated.
But… The way that the data model is constructed, Entities are… essentially named… portions of the resource. So the resource contains all of the attributes.
And then, like, these 5 attributes belong to this entity, and these 5 attributes belong to this entity, but it's all still the same attributes. And we built it that way mostly to retain backwards compatibility.
But each attribute is assigned only to a single entity, but it is still in the, like, the main collection of attributes on the resource.
**Michele Mancioppi** 10:40 From the point of view of the SDK, yes. But, It's sometimes the case that there is only one source of information about a system generating telemetry, and I know for a fact that in practice, it is going to be extremely likely that agents, or SDKs that report about, let's say.
one pod.
They do not exactly agree on all the resource attributes describing that part.
There is going to be overlaps, there is going to be potentially conflicts.
If I go and look up the host name inside the pod, it's gonna be different than what I find.
With fluentity at the node level.
So, I am under the impression that we would need to specify some rules for how conflicting information among entities is supposed to be addressed.
**Ted Young** 11:39 I believe that's the merge rules you want to look at.
**Daniel Dyla (Dynatrace)** 11:44 Yeah, but that's a little different, because that's merging… like, into a single data point. I think what… what Michelle is… Michele? I don't know how to pronounce your name, I'm sorry. Michele, is… is referring to is the case that, like, you have an SDK reporting some… traces with a resource that has some entities, and then you have a resource, or a collector that's, like, also monitoring that process externally from some way that's also reporting some data with a resource with entities. What happens if those Don't have the exact same attributes for each entity.
and the… the merge would not happen… I mean, you could merge them on your backend using our existing merge algorithm.
which is in the OTEP. There is a merge algorithm for, merging two entities together.
And there's an open PR by Joshuareth on the specification to make that a part of the specification as well, but it's already defined in the OTEP.
So you could do that on your backend.
But also, they could be just represented as separate entities.
I guess it will depend exactly on the type of conflict you're talking about, because if two entities have… the same… Identifying attributes, but different descriptive attributes, they could be merged.
But if the identifying attributes don't match.
They are logically separate entities, even if you're trying to monitor the same thing.
I can't immediately, off the top of my head, think of a situation where that would be the case, and I think we would strive to… make identifying attributes such that that is as unlikely as possible, if not completely, you know, never the case. But I can't envision a situation in which that's possible.
**Michele Mancioppi** 13:54 For example, I don't know if this is the case, because I've not tried The merging algorithm yet.
But, Veterinary Industrial, we have a system for entities, which is calculated entirely in the backend before entities were ever a thing.
And, we have the terzero.resource.type.
Which has names that you would recognize, like cates.pod, kits.deployment, host.
And, something that we found a lot… is that, for example, in Kubernetes, on pods.
The pod is not fine-grained enough.
as a resource. In reality, you need to start talking about processes in containers.
And, we had to implement a, semantic convention aware conflict resolution algorithm.
So, if the resource comes in with a different PID, Then, you cannot inherit the container name, because you don't know if it's the same process.
And, I find, from experience, that those are actually very tricky things that make or break the usefulness of a concept like this.
That's why I'm raising the, issue.
**Ted Young** 15:13 It's one of the core things I think Entities was trying to solve, which is that if you are going to be merging these things, you want to have some knowledge within our structure of entities of which of these sources we believe gives the most accurate information.
And to make sure that's the one that takes priority, and to also make sure you're not mixing identifying attributes, right? You're not taking some identifying attributes from one source and some from another source, and mixing them together and getting some mixed identity. That was… that was one of the motivators for… for the whole project.
So, the two parts of it are, like, if you are just looking at resources, at least resources would be cleaned up due to the merge algorithm, so you wouldn't be getting that mix anymore. And two, if you do have the full entity's information, you are entity aware, then you would be able to know more of those details about, like, where that entity came from. As far as being able to… in the same batch, record multiple versions of the same key. That part, I'm a little confused about.
But I think the idea is, like, the most… if a more specific source for an entity comes in, that thing takes priority, and the assumption is you're kind of ignoring the other sources on the back end. You'd always want the highest priority source.
**Michele Mancioppi** 16:45 I'm not from the top of my head.
when you're running EKS on EC2, and you have a collector on the node that is going to identify Cloud.platform as EC2, AWS as Core EC2, but the collector is going to identify, the, the, the node that's coming from a cloud platform, AWS. underscore ES.
So that, is where I think there is… Significant potential for, conflicting information and stuff that we would consider identifying, like, clouded platform.
**Ted Young** 17:24 I mean, I think one approach is to make sure they're not using the same keys, if we think they're going to be reporting different information, right? Like, you don't want two sources using the same keys and reporting different information.
That's, like, one approach to deduping.
**Daniel Dyla (Dynatrace)** 17:39 Yeah, I think this is a modeling concern.
**Ted Young** 17:42 part of what I want us to get through is, like, get through this basic ness of, like, having our model in place, because I think so much is in the weeds, like you're saying, around, like, going back through all the semantic adventures for resources, and now grouping them up as being, like, this… this is the set of identities, but then also for each one of those things, identifying these potential data source problems.
But that was one of the original motivators, is that you've got a collector, right? You've got these different things, and they have access to some additional information, but it might be different from the information that you got reported from another level, like the SDK or something like that.
But I think we… I kind of want to get into it on a case-by-case basis in the… the modeling of these actual entities. I think that's where we're gonna flush all these problems out.
**krajo Krajcsovits** 18:42 I wanted to follow up on that, just a quick question. When you talk about more specific entity, where does that information come from? Like, in Mikael's case, is it… In the entity definition somehow, or is it, like, in the collector configuration, or, like, how do you… Where do you say?
Or is there, like, a, you know, a plan for that?
**Daniel Dyla (Dynatrace)** 19:14 There is no, like, defined, like, Specificity, of the entity.
I think during modeling, like Ted said, you're not going to have keys that are shared between two different types of entities. So if you have… two different entities that have different levels of specificity, they would have two separate keys. And on your backend, you would choose to interpret them, you know, depending on your definition of the level of specificity.
Likely that's not even done in the collector, that's… the collector will ship everything through to your backend as is, and it'll be up to your backend to determine what is the most appropriate data to display it.
A given time.
**Ted Young** 20:02 I think another way of saying it, like, what we've been doing in the past is you have an SDK, and you don't want that SDK to be grabbing at a ton of information, especially with asynchronous calls and stuff like that. You'd rather have a local collector be… be grabbing additional resource information about Cates, for example.
and then appending that information onto the resources batches coming out of the different SDKs running in those pods.
And… That's fine, but, the one… there are some edge cases, like Mike Kelly's pointing out, where, for whatever reason, different tiers might actually genuinely report different information.
for whatever reason, when they're grabbing at the same APIs, or because of their perspective.
So it's not just a matter of, like, decorating with additional information. You would ideally want to just replace things completely.
Oh, sorry, whoop! If a collector later has a more complete view, you want to make sure the collector is, like.
using… if it's like, I have a more complete definition of this entity, I want to replace what was reported to me, rather than kind of do a sloppier merge of the two data sources. Yeah.
**Daniel Dyla (Dynatrace)** 21:31 Yeah, but if they…
**Ted Young** 21:32 One of the issues that… that we want to solve, because that is one of the motivating issues, is, like, sometimes That information doesn't agree with itself.
**Daniel Dyla (Dynatrace)** 21:40 But if it's identifying attributes that don't agree with themselves, there's no way to match those together programmatically. Like, you would have to… One of the restrictions we have is you can't have two entities of the same type in a resource. So… if you had… if you tried to merge in a new entity with a pre-existing type, but different identifying attributes, that results in a failure. The way to resolve that is to disable the detection on the one that is less accurate.
**Ted Young** 22:20 Or completely replace it, I think is the other thing, right? You don't want to merge them together. You would be like, I prefer this… I've got two versions of this entity, somehow.
you know, you don't want to be merging them together, you want to be like, well, I'm dropping that one and adding this one. If they're, like… in this case we were describing, where the identifying information doesn't match, you would not want to be like, well, here's some new identifying information, but I'm gonna, like.
keep some… of the old information for some reason. You would want to be able to not do that, because I think mixing them together is where you could really run into some trouble.
But I'm not sure exactly where these edge cases live. I think that's a thing.
**Michele Mancioppi** 23:09 Something that we found in the serum?
Is that, different semantic convention namespaces.
Tend to depend on one another.
And we use that to decide Which information can be shared between entities, let's say.
For example, if you have a different container name, you cannot share anything about the process, because it's a different container, it's a different process.
There are a few rules like this that are identified, especially in Kubernetes.
they kind of tend to logically, like, lower levels, like the Kubernetes pod UID, different pod UID, it's a different container even if the name is the same.
Different container name in the same pod.
the process ID doesn't work. It's a diff… it's a different, it's a different process.
Those tend to be helpful.
**Ted Young** 24:08 How about this, just to make sure we get your question answered, do you want to take that example, or a similar one, and just post it to Slack? Since we're probably not going to get…
**Michele Mancioppi** 24:18 Oh, I don't know if I have it properly documented anywhere, let me check.
**Ted Young** 24:22 Because it would be good to have one of these use cases right now, and…
**Daniel Dyla (Dynatrace)** 24:26 Yeah. And it's just rude.
**Ted Young** 24:27 View it against what we're building.
**Daniel Dyla (Dynatrace)** 24:29 Or a GitHub issue would probably be sufficient as well.
**Michele Mancioppi** 24:33 I could share a snippet of the PRD that I wrote, that we… that was part of this implementation.
Let me see if I find it.
**Ted Young** 24:45 Because I know that's something Josh Surith has been thinking a lot about, because they have similar issues at Google.
**Michele Mancioppi** 24:59 Where do you want me to put it?
**Daniel Dyla (Dynatrace)** 25:03 I think a GitHub issue is probably the best way to do it, so that we don't lose it in the future.
**Michele Mancioppi** 25:10 Gitavision, which repo?
**Daniel Dyla (Dynatrace)** 25:13 specification.
**Michele Mancioppi** 25:14 Alright.
**Daniel Dyla (Dynatrace)** 25:16 There is no entity-specific repo.
**Ted Young** 25:19 But you can tag it with entities, or we'll do that.
**Daniel Dyla (Dynatrace)** 25:22 Yeah, and I'll put it on the entity's board so it doesn't get lost.
**Michele Mancioppi** 25:31 I'll do.
**Daniel Dyla (Dynatrace)** 25:32 Okay, thank you.
I think we still… yeah, we don't have any agenda. I'll… I'll type up a quick summary for the agenda here, too, so that Josh knows what we talked about, but… I still don't see anything else on the agenda.
I think maybe we'll call it early?
**Ted Young** 26:06 Sounds good.
**Daniel Dyla (Dynatrace)** 26:07 Okay.
In that case, I'll talk to everybody later.
