SIG: System Sem Conv Stability WG
Date: 2025-12-11
Duration: 26 minutes
Zoom Recording URL: https://zoom.us/rec/share/SSe5Os6QtIIADEvTN53vboPnueLs0FX1SdCQ4lk7PtoKQNez8qmwK6niT66I8YNb.rKqWL2bXjBwpIhv8
============================================================

## Zoom Recording Transcript

**Christos Markou** 00:27 Hey there.
**Pablo Baeyens** 00:29 Ayy Food.
Afternoon, evening…
**Christos Markou** 00:36 It's almost night here, 5.30, though.
**Pablo Baeyens** 00:41 What time does the sun set over there?
**Christos Markou** 00:44 it's… it's not bad, it's, like, around 5… 5 PM during winter.
But still, it's not… it's not ideal.
**Pablo Baeyens** 00:55 Right, yeah.
I mean… Here, it's closer to 6pm when the sun sets, but we have a weird time zone.
**Christos Markou** 01:05 Yeah, yeah, I know.
I've been there, so… I can remember.
**Pablo Baeyens** 01:18 I haven't had the time to go through your comments on the RFC, but thank you,
I only took a look at the first one, and I haven't been able to find anything where the semantic conventions repository formally says, this is the…
Autel SEMCOM stability opt-in environment variable that we're going to use for everything. There's only, like, the specific guides for the different areas.
**Christos Markou** 01:52 Yeah, yeah, okay, I see, I see.
Yeah, I think it's not… it's mostly a need, or just to clarify the word.
**Pablo Baeyens** 02:00 Yeah, it would be nice to have something, but yeah, I'll clarify.
Okay, and when you talk, you say, can we specify what conventions can be introduced behind the alpha feature gates?
**Christos Markou** 02:45 I think, if I remember correctly, This might be, about the… what level? What…
Yeah, what stability level Semat conventions should have reached?
And… So, one comment is, what we should allow.
Behind these feature gates, because I guess it doesn't make sense to have…
A migration that is based on non… stable, or…
At least some other conventions that are planned to become stable soon, so…
maybe we need to clarify what is, like, the alignment between the two projects, and in the comment, I tried to explain this, like,
In another discussion, we, like.
kind of decided… we discussed this a little bit, and we said that, in alpha, you can have
maybe some other conventions that are still in development. Then, in order for the feature gate to go to beta, probably you need to have them first stable. I think that's the safest option.
Because it's kind of… in beta, it's kind of enforced, the migration, unless users opt out.
So, maybe that, alignment makes sense to be clarified.
**Pablo Baeyens** 04:14 Yeah.
**Christos Markou** 04:16 I can clarify.
**Pablo Baeyens** 04:17 Yeah. I mean.
**Christos Markou** 04:20 Yeah, go ahead.
**Pablo Baeyens** 04:21 like, Some of these things… I would…
I prefer if it's something that is defined by semantic conventions instead of
decided by the collector developers. Like, the semantic conventions sake for a specific area, I would say, like.
These are the ones that we are migrating to.
that we are waiting, and anything else is…
out of scope, I guess, for the migration.
**Christos Markou** 04:55 Yeah.
**Pablo Baeyens** 04:56 Not exactly the same that you said… as you said, that there's still going to be some things that, I need to clarify, but, like, ideally, semantic dimensions, is…
The people owning… Dots.
**Christos Markou** 05:11 The reality, however, is that, at least for system and Kubernetes, it's mostly the same people that also work on the collector, so it's mostly us. I don't expect that. Fair enough, yeah.
**Pablo Baeyens** 05:24 Then my point is, like, we should write that on the semantic conventions repository, even if it's the same people. We should not write it on the collector side. I see, I see.
**Christos Markou** 05:33 Yeah.
And, also, another point, maybe the one that you mentioned initially, I think it's about… I don't have the PR in front of me, so I'm just trying to…
**Pablo Baeyens** 05:43 I sent a, a link on…
**Christos Markou** 05:47 Yeah.
**Pablo Baeyens** 05:48 That's future.
**Christos Markou** 05:56 Yeah, right. So, I think…
Yeah, so this one specifically is about,
Yeah, so in Alpha Feature Gate, we will select a specific set of Samad conventions. This can be still in development, but my quest… my concern is mostly,
how we select those. Should this be coming from the Samad Conventions group?
Or… and if so, what is the criteria? Because maybe a component, in another comment I mentioned an example, maybe a component has, for example, 30 metrics, and only 20 of those will become stable soon.
So…
The plan should be specific that, okay, this… we're focusing on this 20 for this migration wave, and we don't know what we want to do for the rest of the 10.
For the rest of them, the other 10. And another question is, should we have more additional… should we have additional criteria, like, all default metrics should become stable, this sort of stuff? Maybe that's taking it too further, too far.
But I was just… having… I just had these thoughts while reading this. Right, yep.
**Pablo Baeyens** 07:17 Do you think it makes sense, let's say, for the system metrics, do you think it makes sense that we…
we as the Systematic Convention, define
Like, we're going to focus on these, 10 metrics. These other ones are not part of the migration.
**Christos Markou** 07:33 Yeah, I think this would be… this should be explicit, and, have some sort of decision that, this migration will cover this set of semantic conventions, so as, this to be clear between the two different projects, something like this.
**Pablo Baeyens** 07:56 I'm good to make a note about that.
Okay, yep, so I'll try to, reply to your comments, Tomorrow…
Mark it as ready for review tomorrow.
And, well, if anybody else wants to take a look, we're talking about, dot PR, that is.
Tangentially related to the same.
**Christos Markou** 08:46 I guess we can move to…
**Pablo Baeyens** 08:48 Power.
Thanks, Jason.
**Christos Markou** 08:50 Yeah, we have a topic, okay, yeah, and Google News.
**Pablo Baeyens** 08:58 Yeah, so…
**Dmitrii Anoshin** 08:59 later on.
So let me share my screen.
A bit easier.
So… Yeah, while working on introducing the entities definition in the…
in receivers and in some processors as well. So we, like, entities…
needs to be associated with a particular set of resource attributes, and essentially, entity kind of own the resource attributes, so ideally, it…
Like, we would need to ask user to not specify any resource attributes, so, like, disabling, enabling, for example, in the configuration interface, but we would need to… them…
like, treat them as entity attributes, and manipulate entities instead of attributes, instead of resource attributes. Because right now, for example, they can go ahead and disable, let's say, Kubernetes node UID,
And in that case, if they enable Kubernetes node UID, Kubernetes Kubernetes node entity associated with the resource would be broken, because a set of identifying attributes will be empty. It will only have,
Descriptive attribute, which is, which is wrong.
So, like, first stop, how to resolve that is just make the identifying attributes defined in metadata YAML, like this.
To make them… this is actually incorrect, so let me quickly fix that. The identifying should be your ID.
And descriptions should be not named.
So…
Yeah, we can just make them required, and so users cannot disable them through the resource attributes section.
it's probably gonna be the first thing I can do before, like, resolving this issue. But going forward.
I think we… we need to give them, users, generate an interface to manipulate entities, like, separately. So, for example, they can… I described two options how we can do it here. We can either deprecate and remove this section and have, like, entity section instead, and each, like.
Peace.
it will… this section will have a set of entities, like KubernetesNote, community support, and inside KubernetesNote will be a description where they can disable a particular descriptive attribute, but they cannot manipulate, identify an attribute. Instead.
They can disable the whole entity.
Like, because if you're disabling…
identifying attribute is invalid, but disabling the whole entity is pretty valid, right? In that case, they can, for example, disable the whole port entity, and in that case, I believe it should mean that
we don't emit any metric… metrics for that entity. But this is still, like, an open question, but I think that would translate to, like, that entity is just… just ignore it, and we don't… we don't even watch, for example, Kubernetes cluster receiver, we don't even watch for pods anymore.
Yeah, but this is one of the options which would deprecate this one. But if we want to keep this one, we can also introduce, like, additional interface. And here, we can also enable, disable entities as a whole, but, for example, description…
can be just a little bit different interface, because I heard that people sometimes like to be explicit about a particular set of
Identifying attributes that they want to emit.
So, potentially, we can… it'll be, like, essentially redundant, right? It'll be two separate ways to…
Disable, enable particular attributes.
And we can have some, like, prioritization rules here.
Yeah, but I don't know, this is two options we have I wanted to bring in for discussion. What do you think about it?
Maybe we have some other… Suggestions.
What do they think?
Any ideas?
**Christos Markou** 13:50 Does this mean that the… The metric model will change.
**Dmitrii Anoshin** 13:56 metric model will not change. Metric section will stay the same as this. I was under… initially, I was thinking that we can even put metrics here. So, for example, like, this particular node section, right, we can define a set of
descriptive attributes, and also a set of metrics here. But, like, thinking more about it.
It's not like… it's not one-to-many relationship from entities. Essentially, one metric can be emitted with several entities instead. For example.
Like, we… we would…
well, like, pod metric would be… would go with pod entity and Kubernetes cluster entity, for example, which is, like, a higher, higher entity. So we need to provide both, right?
So that's why I just removed any association… any association with the metrics, but association with the metric will be defined in metadata YAML.
And, it'll be same as it's defined in Vivier, where you have… each metric has… is associated with this particular entity in metadata amplif.
**Christos Markou** 15:05 Yeah, yeah.
**Roger Coll** 15:13 So basically, the new entities section…
Will be, like, a new way of defining which resource attributes will be on the final metrics, right?
**Dmitrii Anoshin** 15:24 Right, a new way of defining resource attribute, because entity,
like, descriptive identifying attributes, they are…
present in resource attribute anyway, for backward compatibility, and it's gonna stay that forever. But yeah, it's another way to define…
Attribute, but additionally, we have this option to disable the whole entity.
**Roger Coll** 15:49 Oh, dude.
then for me, I think I… I prefer option 2.
Just to not confuse, let's say, users about, and also to simplify, I would say.
**Dmitrii Anoshin** 16:05 The end that.
**Roger Coll** 16:07 Let's say a builder, because if we have both resource attributes plus entities.
So, like, a lot of additional, I think, conditional between enabled and disabled.
**Dmitrii Anoshin** 16:19 Yeah. And probably with just entities, we can have all the… all the use cases as well.
**Roger Coll** 16:25 That makes sense.
**Dmitrii Anoshin** 16:26 In that case, with the stabilization effort, I think we would need to… have this…
soon, soon? I can prepare PR probably this week, and we should deprecate resource attributes.
Section. And then, whenever… We approached stable.
particular company, we can remove resource attribute section.
**Roger Coll** 16:57 Yeah, sounds good, and looks good to me.
Thank you.
**Dmitrii Anoshin** 17:01 Pablo, what do you think?
**Pablo Baeyens** 17:06 I… don't have a strong opinion, because I haven't thought about this too much. I mean, option 2 sounds…
good at first Lund, but I… I don't want to, like, Say anything definitive without having…
Okay. Read more about entities, like, I don't know enough about entities, sorry.
**Dmitrii Anoshin** 17:27 Yeah, it's just probably not… like, this is something that has to be done in one way or another anyway, but the question here, more like, if we go with the first option, we don't really block anything related to stability effort, right? It'll be just an additional configuration option generated
Out of the box.
But if we go with the second option, this means that we are replacing this one, and like, we…
**Pablo Baeyens** 17:59 Right, and .
**Dmitrii Anoshin** 18:01 it interferes with the stabilization effort. I think the cleaner… I also agree the cleaner way is second one, because, like, dealing with this kind of…
Like, conflict's also not ideal.
Potentially, as a third option, we can just remove this one.
And keep it, like, disabling full entities.
as the third option, right? In that case, we will have resource attributes, but the thing is.
I'm a bit, like… I don't like that one, because… Essentially, It's better for users to… have…
like, understanding that attributes are… attributes belong to entities, not to a resource. So a resource kind of, let's say, kind of deprecated, in a way.
**Pablo Baeyens** 19:01 Concept.
**Dmitrii Anoshin** 19:02 So, if we keep this one specifically for entities and everything else under resource attributes, it's not kind of… not ideal.
**Pablo Baeyens** 19:12 How…
how established is it that entities are going to work like this? I mean, this seems pretty fundamental to entities, so I guess it's not going to change, but that would be one.
One of my worries.
If this changes on the entity's side.
**Dmitrii Anoshin** 19:29 Oh, I see what you're saying. I don't expect any changes to this… Same.
**Pablo Baeyens** 19:39 Okay.
**Dmitrii Anoshin** 19:39 But maybe we can break it down, actually, maybe we can… but, like, maybe we can start with this thing only, like, avoiding description for now. We keep using resource attributes, and to not block…
**Pablo Baeyens** 19:57 I like that, I… I think that… Seems to be…
valuable, still? Like, you… you can disable whole entities.
On… Yeah, I guess
At some point, we'll have to face whether we want to remove the resource attributes section, but maybe…
We'll just have to deprecate it and not remove it, I don't know.
**Dmitrii Anoshin** 20:28 Okay So, yeah, probably it… it would make sense to take it in a, you know, like, in a…
Gradual approach, and let's see how… how the stabilization effort goes, so it's not like we are rushing something.
But maybe, we'll see. I mean, even after, like, companies are declared stable, what does it mean? Does it mean that the configuration
like, some particular configuration sections will never go away. I think we need to clarify that. We still need to make our, like, make it possible to replace some configuration option, even if component is stable. It just may be, like, the deprecation period is, like.
extensively long, like, for a year or something like that. Have you thought about it?
**Pablo Baeyens** 21:23 I guess… My thoughts were, like, we would release a new
Major version of the component, or major version of the configuration.
**Dmitrii Anoshin** 21:33 Okay, okay.
You can deprecate the…
**Pablo Baeyens** 21:37 The previous one, and yeah, have a long period, as you said.
**Dmitrii Anoshin** 21:40 Okay, yeah, okay, that makes sense. So, I'll start with this one, with this thing.
whenever, like, the stabilization effort will go in parallel, I'm not gonna block anything. And if, like, we decide that
for example, this approach should be… we should go this approach and deprecate resource attributes. We can deprecate it even in the stable component and keep it deprecated until the next major version release, right?
**Pablo Baeyens** 22:12 Right, yep.
**Dmitrii Anoshin** 22:13 Sounds good.
**Pablo Baeyens** 22:14 Yeah, that's…
**Dmitrii Anoshin** 22:16 Okay.
Sounds good. Cool. Thank you.
Yeah, okay, I'll update this issue based on the discussion that we had. Also, I'll bring into the…
entities seek, maybe they'll have some insight as well.
**Christos Markou** 22:34 It would be nice, though, to, at least have this, like, verified with
Two different types of components, one receiver and one processor, maybe.
The tricky part is that the KH attributes processor is a bit… it's not controlled through the metadata.yaml file, right?
Sure.
**Dmitrii Anoshin** 22:57 It, it is.
**Christos Markou** 22:59 It is controlled, because we only enable it… we only…
We have this extract, configuration option.
That we…
**Dmitrii Anoshin** 23:09 Okay.
**Christos Markou** 23:09 Enable or disable research attributes, right?
**Dmitrii Anoshin** 23:15 Oh, Kubernetes, you mean Kubernet processor.
**Christos Markou** 23:17 Yes, KHI.
**Dmitrii Anoshin** 23:18 Yeah, that one is a bit tricky, yes. So, I mean, this is clearly mostly about scraping receivers, but for processors, it'll be a bit more complicated. So, yeah, I think I got your idea, you're right. We probably need to, kind of.
prototype and see how it'll go with… I'm… I guess the resource detection process is the most important to adopt this.
And resource, like, Kubernetes Attributes Processor, potentially, as well.
That's a young boy.
**Christos Markou** 23:50 Both are in the first wave, of…
**Dmitrii Anoshin** 23:53 Oh, I see, that's right. Yeah, that's a good, good input, thank you.
Cool, that's pretty much it from my side.
I got some feedback. Thank you.
**Pablo Baeyens** 24:21 Alright, any other topics?
**Braydon Kains (Google)** 24:26 Nothing from me. Sorry I was late. I got pulled into something last minute, so I… I lost track of time. Was there… was there anything…
That was needed for me.
**Pablo Baeyens** 24:43 There's a PR that we discussed with the conditional required,
thing. I think we agreed on…
on how to move forward, but we didn't put it on the… on the PR,
But, yeah, I guess that one I'm talking about.
**Braydon Kains (Google)** 25:03 Okay.
**Pablo Baeyens** 25:03 It's beer.
We can… we can move forward with.
Removing the… Description?
There?
**Braydon Kains (Google)** 25:14 Sure. That's fine by me.
**Pablo Baeyens** 25:21 Okay.
**Braydon Kains (Google)** 25:24 I'll make that change.
**Pablo Baeyens** 25:26 Cool. And otherwise, well, we discussed the… the issue that Dimitri was talking about, I think you…
You caught that one? Before that, we discussed this…
PR from the collector with an RFC, from me.
I'll mark it as great for review.
Tomorrow, if I'm… Able to find their time.
**Braydon Kains (Google)** 25:48 Okay, sounds good.
It looks like merging this RFC will degrade performance by 29%, so we should definitely fix that.
**Pablo Baeyens** 25:59 Right, yeah, still… still some work to do to know.
**Braydon Kains (Google)** 26:03 Yep.
**Pablo Baeyens** 26:08 Alright, I… I'm going to be out starting next week, so… I guess…
Enjoy happy holidays, if you… if you're taking any time off, and… We'll see you… In January.
**Braydon Kains (Google)** 26:28 Sounds good.
**Dmitrii Anoshin** 26:29 Gender.
**Roger Coll** 26:29 Cooling.
Enjoy. Enjoy. Enjoy.
**Pablo Baeyens** 26:33 See ya.
