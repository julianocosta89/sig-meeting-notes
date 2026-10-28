SIG: K8s Semantic Convention SIG
Date: 2026-10-27
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Tyler Helmuth** 00:23 Lope.
**Christos Markou** 00:25 Hey there.
Thanks for handling the release.
Yesterday.
**Tyler Helmuth** 00:33 No problem. I really wanted that one to go out, because I wanted to release a blog today for… OCTL 1.0, which is why I was, like, watching it so closely.
**Christos Markou** 00:45 Okay, yeah, nice.
Good.
I think also the time… it's this weird week of the year that the time changes in the… In Europe, but not.
I think.
Wow.
**Tyler Helmuth** 01:08 Did you ch- did you… Switch already.
**Christos Markou** 01:12 Yeah, it, switched to 1 hour… I think forward.
So, it, it gets, dark one hour earlier.
**Tyler Helmuth** 01:27 Yeah, that's annoying.
**Christos Markou** 01:30 Yeah.
**Tyler Helmuth** 01:33 Ours is next Sunday.
5 days, 6 days.
**Christos Markou** 01:56 Nope.
I think we can start, let's see if… And, I should join later.
I… have added for today the… to discuss the… the issue around the volume metrics and the PVC metrics that… We're discussing on the issue.
Thank you, Gina, for… The po- the comments there.
I think my only open question, my own concern is So, right now, we have the… I can actually share my screen.
Due.
Okay, so… For these volume metrics that we are discussing here, There was this discussion if we should keep them or remove them, and instead… Replace them with some persistent volume-specific metrics, so as to only report PVC-related metrics.
And… It seems that it makes sense to have metrics that are provided for the scope of the pod.
Because it can be useful If you want to know How much available volume, for example, a pod has.
And how the metrics are, evolving with regard to the pod specifically. So… and we also have these metrics in place for a while now, and we also… they are also implemented in the receiver already. The name is different, but still, those are there. We just need to change the names during the migration.
So… the only open question I have is that, for the pod volumetrics.
that… we want… to relate them to a persistent volume, to a PVC, essentially. I'm not sure if we have a way to represent this in Semantic conventions, because… in… In the collector, what we were doing is that The persistent volume claim name was added as a resource attribute.
And actually, everything was added as a resource attribute, the volume name, the type.
But in the modeling that we have for these metrics in Semantic conventions now, is that volume name and volume type is the… is a metric attribute on the metric scope, and then the association is on the Kubernetes pod.
So… In theory, if we had the way to represent To actually say that an association to a per… to a PVC exists, If conditions apply, probably we could model it like that, but I'm not sure if this is supported today, probably it's not, because not all of these metrics would be associated to persistent volume claims.
That's my, let's say, what bugs me there.
If that makes sense.
**Jina Jain** 06:02 Yeah, that makes sense, I'm just thinking, isn't there… so, I guess we can just correct it, firstly, this should just be metric attributes, to be honest, because even if we tried modeling as, like, entity relationship, this is one of those, you know, situation where a PVC can technically be claimed by multiple pods, because… Because of the read-write many sort of PVs, right?
Somebody might want to go check this with EFS or something, but I do think there is a possibility that the same PVC can get associated with multiple pods, so it won't even be, like, a 1 is to one relationship.
So, I think, like, we could go with metric attributes, and there is a conditionally required type for metric attributes, if I'm not mistaken.
Can you go back to my comment? Because, like, while I was digging into this, I was… I was a little confused, so the first Yeah, in that comment, the first thing, if we did that, if we fixed our receiver to always you know, have that metric attribute PVC name as the metric attribute on those metrics.
For a volume type of PVC from the pod spec.
I think that conditionally required… the thing which I'm thinking should work on metric… as a metric attribute.
**Christos Markou** 07:32 So…
**Jina Jain** 07:34 Does that make sense?
**Christos Markou** 07:35 Yeah, I think the conditionally required attribute, yeah, it's… it is supported, we can use this.
But we, we lose.
The entity association, because technically, a persistent volume claim is also a Kubernetes entity at the same time. But in that case, we could cover it with, Like, with additional metrics that we were discussing, and potentially add them in the future, if we want to… Actually relate them to… The actual objects, or the identities.
**Jina Jain** 08:13 Yeah, I say it remains very easy. Dmitrii… do you remember where we left with the entity relationship modeling in case cluster receiver?
Because, like, do we… can we support this sort of entity modeling here? Could I say that a PVC object is part of XYZ pods?
**Dmitrii Anoshin (Splunk Inc.)** 08:38 as a separate channel, as entity events, right? Because I'm not sure how we…
**Jina Jain** 08:45 Work with resource attribute, yeah, I…
**Dmitrii Anoshin (Splunk Inc.)** 08:47 Resource attributes.
Yeah, phone resource attribute, I'm not sure if it'll work.
**Jina Jain** 08:52 I bet.
**Dmitrii Anoshin (Splunk Inc.)** 08:53 In resource attribute, we can only… What entities, like, let's… Static kind of definition of entities, so… One resource attribute with several entities.
How they are related, and we don't… not gonna actually… put relationship information in the resource anymore. It'll be only a scope kind of relationship. So, like, if there is one entity clearly identifiable only within a particular scope of another entity, let's say, like, Kubernetes container name.
only identifiable within a pod, and that's where we will have clear distinction, clear definition within the resource. But other than that, like, no relationships on the resource. It has to go through Separate channel prologues.
Entity events. And that's where you can put anything, all… any relationships between entities.
**Jina Jain** 10:00 Yep.
Garden.
**Dmitrii Anoshin (Splunk Inc.)** 10:03 So, I think last time… sorry to interrupt, I think last time we ended up specifying those as attributes of an entities, or sorry, attributes of the metrics.
Because that's, like, the cleanest solution we were able to get right.
**Christos Markou** 10:21 So, you would say that the proper way to represent this is that for this metric, the pod volume available metric, we associate this with a pod entity at first place, and then on the attributes, yeah, these attributes are mostly descriptive for the pod.
**Dmitrii Anoshin (Splunk Inc.)** 10:39 Yeah.
**Christos Markou** 10:39 But we add an additional one, which is the PVC name.
**Dmitrii Anoshin (Splunk Inc.)** 10:44 Yes, I think that's the right way, and it's gonna be metric attribute, not the resource attribute.
**Christos Markou** 10:50 Yeah, yeah, okay.
**Dmitrii Anoshin (Splunk Inc.)** 10:51 Okay. Yeah, these are…
**Christos Markou** 10:52 Metric… metric attributes here.
**Dmitrii Anoshin (Splunk Inc.)** 10:54 Jen, that's what we ended up when we were looking into that, like, some time ago, right?
**Jina Jain** 11:00 So, I have a feeling we have had this discussion about PVC2 pod because of this many-to-one situation which might come up, and we agreed upon similar situation.
**Dmitrii Anoshin (Splunk Inc.)** 11:11 Yep.
**Christos Markou** 11:16 Should we use both the name and the, unique ID of the PVC as conditionally required there?
**Jina Jain** 11:25 So, The thing is, if you try to put in the UID, we will have to make an extra call, because, from what I was looking at, Puplet only had the PVC def, in stats summary.
So, if… so we would be back, you know, to that receiver config, extra receiver config option, then, which somebody has to… tell, okay, make this extra call, look up the UID, and this thing.
I, I'm of the opinion we can… name plus namespace should be enough, even though it won't tell you when the PVC itself changed.
But a PVC, like, I don't know if a PVC change could actually propagate to a pod while it is still running or something, so I'm not sure.
Oh.
Yep.
**Christos Markou** 12:21 Okay.
**Jina Jain** 12:21 And if we end up, you know, wanting to add the UID, I guess we'll have to…
**Christos Markou** 12:31 Yeah, maybe another component.
Because I'm thinking now, if we add the persistent volume claim there, here, as an attribute.
At an additional step, potentially the CH attributes processor, or something like that.
Could do the correlation and, like, correlate entities somehow, or if it is another component that emits entities, has log events.
Yeah, that would also work, using the name and the namespace of the pod.
Okay.
I think, that mostly covers my… concerned.
So… if I get this correctly, we say that we want to keep these metrics as they are today.
And the association will remain the pod.
And we… add the PVC name as an additional metric attribute, and we also need to rename There is the suggestion from my side to rename these attributes to gauge.pod.volumeName, because cage volume is something that conceptually, that does not exist, I mean… It's very weird. It's, the volume of the pod, not, like, a volume in general.
Does this… Sounds okay to everybody? Any concern? Anything I missed?
**Jina Jain** 14:03 So, if you, go back to my comment, I did have a suggestion for the volume type also, because It is blurring the meaning, again, because of that extra API config.
It's… depending on whether that API config was actually set, it can be, you know, the type could be from PodSpec, or it could be somebody went and looked in the PV for the actual type.
CSI, or… Etc.
So I think we should… I don't know, how would we… like, again, this is, like, just to be receiver's configuration bleeding into semantics.
**Christos Markou** 14:48 Can we have the attributes as optional? I think.
You can have them.
**Jina Jain** 14:56 Yeah, we can… we can have them optional, but I think just… Defining the attribute K as volume type is difficult, because you will have to then say that, okay, it is this pod spec field, but if you did this extra magic somewhere, it is these values.
That's what I'm trying to get to.
But, yeah.
I know we can… we can discuss this. I… I don't… I feel like we could go with the current form also, but maybe just adding that caters.pod Is better.
**Christos Markou** 15:45 Yeah, okay, I will… Have a closer look to this, persistent volume type.
thing that you mentioned here, and see. I can start with doing the rename here for now. The reason I want to progress this is that these metrics are The… the only leftover… That is, still in development, and we have introduced them already, they are in development.
If we manage to progress them, promote them to release candidate, then the whole list will be… essentially release candidate, apart from the metrics that we introduced, like, in the past two months, because we need to wait for a release to happen first in Semat Conventions. But let's say that from this list, if nothing changes, these metrics are the only It's the critical part now, that, if we complete this, the whole… set of metrics that the component emits will be in a list candidate, and that means that we can port them already using the feature gauge back to the component. And, yeah, there is the suggestion to actually work towards promoting the component to V1 in a few months from now, hopefully by KubeCon Europe in March.
So that is the, like, the bigger picture here.
But, yeah, this doesn't mean that we need to compromise, if we're not sure.
Okay.
I will… try to summarize this, post back on the issue. I will send the PR, the following days to do the rename, and let's see how we can handle the… The thing with the… PVC types.
Sounds good from my side. Anything… anything else from… Hang on.
Nope.
So, can get… 10 minutes back then. Thank you, folks.
**Jina Jain** 18:20 Thank you.
**Christos Markou** 18:21 See you. Bye-bye.
