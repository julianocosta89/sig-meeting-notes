SIG: Semantic Convention SIG
Date: 2025-08-04
Duration: 61 minutes
============================================================

## Zoom Recording Transcript

Josh Suereth 00:01:46 Good day, everybody!
Christophe Kamphaus 00:01:49 Hello!
Josh Suereth 00:01:53 This is gonna check with the other Maintainers who would like to run the meeting today
before I just start.
Trask Stalnaker 00:02:03 It's been a while I can. I can drive it.
Josh Suereth 00:02:07 Okay. Thanks. Trask.
Trask Stalnaker 00:02:11 Yeah. Just removing our note, taking friend.
Oh, yes, we are in August now.
Attendance is even slower, and this is our peak of summer.
Alright, let's start with the trashboard.
So we've got a couple ready to merge
cool
more briefs and a policy to require briefs.
Does this going forward
requiring briefs? Or did does everything now have a brief.
Liudmila Molkova 00:04:06 And was this Pr. Every attribute and a metric, and
every attribute and group has a brief.
and they are still not required on the members
because a lot of members doesn't have them. I think James has a bunch of Prs to fill them in, but they are not required in the regal.
Trask Stalnaker 00:04:35 I see. And these were. This was a enum yes, great.
I was worried that was going to cause conflicts between the 2, so we can merge
all right. Needs more approvals.
Let's see, this is, I think, has been here for a while. The mainframe folks.
I'm not quite sure what this status should we ask?
the mainframe Sig, if they are still.
if this is still in that Sig versus, if they're just waiting on us now.
Liudmila Molkova 00:05:38 Let me ping them and ask. I I think I've left a bunch of comments, and I'm not sure if
they.
Trask Stalnaker 00:05:46 Oh!
Josh Suereth 00:05:47 You know the the last status I just looked at this this morning when I was triaging
Trask Stalnaker 00:05:51 Okay.
Josh Suereth 00:05:52 It looks like they were going to go back to the Sig and talk about entities and resource attributes, instead of throwing everything into metrics. So that was from the comment. So that was, that was still 2 weeks ago. I don't know if there's like a
yeah. Anyway, I would throw this. Maybe it back to awaiting cone order, approval, or something.
I don't know if we have a back to Sig for discussion, bucket.
but there's a there's a comment from Rudiger on that.
I forget where it is, but it's off of one of Ludmilla's comments that so that's when I stopped
Updating my triage on this one, and moved on. When I saw that.
Trask Stalnaker 00:06:31 Makes sense I'm just thinking of. I guess we can. Yeah, in the triage discussion, was there anything
I forget? If we had an action item for breaking this down.
Joao G. (Dynatrace) 00:06:53 I think so. Yeah, I think we had. There's some ideas in the like the triage workflow.
That we have here, but but not not implemented.
Trask Stalnaker 00:07:07 That's.
Just leave it. Then hardware metric.
To yaml.
We have an approval from Josh.
All right.
Yes.
cool any open James. It looks like you have a open comment.
James Thompson 00:07:44 No, all, all mine's closed out.
Trask Stalnaker 00:07:48 What's that?
James Thompson 00:07:49 Mine aren't open anymore.
Trask Stalnaker 00:07:52 Oh, okay, can I resolve this? Yeah, great.
All right, let's merge it.
It's.
Liudmila Molkova 00:08:08 Not their approval right.
Trask Stalnaker 00:08:12 I don't it? Let me merge birdie. Oh, Birdie is not approver. Okay.
Liudmila Molkova 00:08:23 And I can take a look. I promise to take a look, and I didn't. I can take a look and approve, and then it will get in.
Trask Stalnaker 00:08:32 Yeah, no, I was just. Oh, oh, it's Bertie's. No, it's it's Alexandra's. Pr.
Do we? We probably don't have a hardware code owners.
Liudmila Molkova 00:08:44 You're right.
Trask Stalnaker 00:08:47 Should we create a hardware code owners and add, pretty
is this more? For I mean, this would be like, it's not really a sig.
Liudmila Molkova 00:09:02 I think it's a great idea.
Trask Stalnaker 00:09:23 Okay, I will just leave that to do later.
More informative. Oh, let's see. Chat time check. Let's just look at these last 2 real, quick, more informative container
runtime from James.
Alright, we've got Josh, and we've got a Sig approval.
Linilla, do you want to follow up on this.
Liudmila Molkova 00:10:13 Yeah, let's follow up. I didn't see the comment. But I I don't understand. If we
what would it go into the Runtime description.
Okay, let's pull up.
Trask Stalnaker 00:10:28 Sounds good, and last, one guidance.
an info metric for Cicd runtime metrics. We've got Sig approvals. But no, okay.
Christophe Kamphaus 00:10:42 Still open discussions, and I have it on the agendas.
Liudmila Molkova 00:10:48 Wonderful.
Trask Stalnaker 00:10:48 Awesome. Alright, that is triage.
Let us go on to topics.
And Christophe so yes.
Christophe Kamphaus 00:11:03 Yeah. So that was the discussion on the pr, so related. Issue there was a comment on it. We discussed it previously in some conf
in April, if I remember right, and the question was about infometrics.
I wanted to ask now if it has been a few months, is now.
has there been any update on how to define infometrics?
Josh Suereth 00:11:37 I don't think so. I don't. Who? Yeah. So basically, info metrics is a property of Prometheus. But it is not part of the open to entry. Spec.
I don't know who would be working on infometrics and opentelemetry at this point.
I'm not aware of a task to do that.
but I might be misremendering some of our because we were talking about basically info metrics that get
generated from entities. That work is also kind of like a phase. 2
of entities work so that entities has kind of been focused more on how to generate entities and resources to begin with.
So I don't think that work is actually actively happening right now.
It. It depends on how blocked you are on info metrics like what what we can do.
Christophe Kamphaus 00:12:25 Not at all.
Josh Suereth 00:12:26 Not at all.
Christophe Kamphaus 00:12:27 I took your suggestion from April to justify an engagement metric.
Josh Suereth 00:12:32 Yep.
Christophe Kamphaus 00:12:33 And that works.
I also checked the Prometoy specs. And actually they don't talk about infometrics at all. It's just a regular metric with attributes.
Josh Suereth 00:12:45 Yeah, only only open metrics had info metrics, if I recall correctly. So
I honestly think what you have here is fine for us to go forward. We shouldn't block on either of those, because either of those have to adapt to what you did.
So it's kind of like a it. I.
I don't expect this to be significantly different from what gets designed, and I think that you know, if you need this information now, a gauge metric called info would be acceptable if we feel like this is the right naming convention for semantic conventions. So I think we can have that discussion independently around info metrics in semantic conventions. When entity stuff catches up we'll have the discussion, and that needs to adapt to what has been done in some, not the other way around.
Christophe Kamphaus 00:13:32 Yeah, sounds right to me. And yeah, I also named it.info, because I saw there are
actually a lot of metrics that use that convention.
What I also found in the spec of open telemetry. There was one page. Got it.
It was the give me a second, it was
I don't have it in mind anymore.
No, there was one page about translating open metrics into
yeah. Sorry. Huh!
It fell out of my mind.
Trask Stalnaker 00:14:25 I have a question. Cicd pipeline run. I was just surprised to see this being modeled as an entity.
Can you kind of explain that.
Christophe Kamphaus 00:14:38 Yeah, it's because, we defined it as a resource.
And that's why we put it as an entity.
And I think here, these attributes that are defined here, they would also be identifying. And we actually don't have
descriptive attributes, for now there could be some later.
Trask Stalnaker 00:15:07 So I mean, it seems very.
I haven't been following the entity work closely on, but it seems very fine grained
to me to be an entity like, why wouldn't this make like a
Http request could be modeled as an entity.
Christophe Kamphaus 00:15:32 I think there were some fine great entities like for processes.
I remember right, Josh.
Josh Suereth 00:15:40 Yeah, yeah, I.
Christophe Kamphaus 00:15:42 So this would be on the same level.
Josh Suereth 00:15:45 I'm curious to your comment, Trask, like a pipeline run, would be like a instance of something that's running a pipe like a task like a cron job and Cron. Job is already an entity or job as an entity in Kubernetes. Right? So in my mind, like Job or Cron, Job and pipeline run are kind of similar levels of
abstraction.
Trask Stalnaker 00:16:06 Pipe. I agree with Pipeline, I mean, I don't see any issue with pipeline being an entity.
but a singular execution, right like, if I go to
That's gonna be, you know, each one of these right? If I'm understanding correctly.
Christophe Kamphaus 00:16:30 Yeah, we defined it on that level.
Josh Suereth 00:16:34 Render this without that identity like
like like, go back to like, think about a Kubernetes Cron job, right? Or a job. It's the id of the job, not like the name of of all possible jobs that you're actually tracking. So if you want to actually have observability of like, what's an instance of a job versus the job itself. You need to have the the thing. Does that make sense.
Trask Stalnaker 00:16:58 Yeah, yeah, I I guess I would naively model that as either a span or an event.
Christophe Kamphaus 00:17:09 Actually, that's exactly why we do it this way, because one pipeline run can emit multiple spans.
And it's actually more efficient to put it on the resource also spends.
Josh Suereth 00:17:25 Yeah. So trust the litmus test is, if you have multiple pieces of of signal associated with an entity that's that. That's what makes sense. So if you go back to the Github example like click on click on any of those pipeline runs right.
Trask Stalnaker 00:17:37 Yeah, yeah.
Josh Suereth 00:17:38 And then click on an instance of it. And you see the logs, for that instance, that run
right. All of those logs are associated with with that that run by its Id, and that's that's an example of when you have an entity versus when you have a signal. Right?
if you're going to attach a lot of things
that has one source, and you want to aggregate and group that source.
That's that's our litmus test. For when you have an entity versus when you don't.
Trask Stalnaker 00:18:09 Good morning!
Josh Suereth 00:18:10 Let them know.
Liudmila Molkova 00:18:11 I have a related concern. I brought in the comments. So I, okay, it's an entity fine.
But if you use it as an entity, and everything will have this entity. Right? Specific metric cannot pick and choose whether
it carries this entity or not, and then their run duration
would also have the run entity, and we'll have high cardinality.
And how would we deal with this.
Josh Suereth 00:18:49 How do you get high cardinality with run duration.
Christophe Kamphaus 00:18:53 Here as a metric as it is defined.
It's on the pipeline, not on pipeline. Run.
Liudmila Molkova 00:19:01 But you cannot choose. You would have a pipeline run entity globally on every signal.
Christophe Kamphaus 00:19:08 No.
Liudmila Molkova 00:19:09 See you.
Josh Suereth 00:19:11 I think this is not coming from an SDK. These metrics come from something that externally reads the Cicd, and then synthesizes the metrics from it so like
in. If this were a normal open telemetry SDK, where you like, provide an entity in it, as you know, a resource, and then everything gets attached to that same resource. That's not really true for Cicd.
right? That's also something that is interesting and open telemetry.
Liudmila Molkova 00:19:38 So if you.
if you wanted to instrument it on Api and SDK level, you would not be able to.
Josh Suereth 00:19:45 You would have to have multiple instances of the SDK one that reports against a pipeline one that reports against something else. Yeah, we don't have a good multi tenancy story
in opentelemetry of like, Hey, I want to split data by. This is actually about this thing. This is about that thing.
But you would. Yeah, you would have multiple sdks. We actually have people internally here that have to do that.
Christophe Kamphaus 00:20:09 It's exactly like such that we have to do it
because basically we don't observe ourselves like in a single SDK instance, we do it.
We observe something else, observes the pipeline runs externally in the Ci CD controller.
Josh Suereth 00:20:31 But the other thing I can imagine is when you have a pipeline running.
and I have instrumentation in like the worker for that pipeline run.
I could push down the identity of the entity with that environment variable we're proposing, and then the SDK will attach to that pipeline run for like a given worker, and all the information will be associated with that pipeline run
right? So in that case it it's working as intended.
Christophe Kamphaus 00:20:59 Yeah, and that's exactly how we do it. On this, on the pipeline, I proposed. If we want to attach this, I entity
the pipeline run info to any metrics emitted on the worker that we observe.
So, for example, host metrics for just that specific worker executing a single pipeline run.
Trask Stalnaker 00:21:26 So I think this connects something for me on how the cause the browser has been talking about modeling the session as an entity.
This is correct.
then are you there.
Josh Suereth 00:21:50 Do you know.
Daniel Dyla (Dynatrace) 00:21:51 I'm sorry. Yes, I I'm here. Do I know what I I was a little bit distracted.
Trask Stalnaker 00:21:58 No worries, no worries the session id or session in the browser sig is being gonna be modeled as an entity.
Daniel Dyla (Dynatrace) 00:22:11 Yes. So the the plan, I believe, currently is to model session as an entity. Right now there's a prototype for a component called the session manager, which is what like the Api for that will be
but it's
yes, the session will be an entity. And then, like the logged in state would be a descriptive attribute of that entity.
Trask Stalnaker 00:22:35 Okay, okay, that yeah, I I just hadn't really connected. I was under this idea that entities were these sort of as, yeah, I was saying in chat like sort of longer lived things that you would.
That aren't high cardinality.
Daniel Dyla (Dynatrace) 00:22:53 The session is longer lived. But it may be high cardinality, because you have one per user, obviously, or one per one per session more than one per user.
Trask Stalnaker 00:23:04 Right, and pipelines can be longer run. Also, if they trigger lots of associated things.
Daniel Dyla (Dynatrace) 00:23:15 Yeah. And entities can also be very short lived as well. I mean, you look at the example of like a lambda function.
The whole entity may live for only a few 100 ms
right, and could potentially also be quite high. A cardinality.
Trask Stalnaker 00:23:37 There's not.
Liudmila Molkova 00:23:38 Can. Oh, Christopher, can you remind me? Why are we modeling it as a metric at all? What is the benefit? Why can't we just say it's a span
pipeline run span.
and it would carry all the high cardinality information. It will serve as a correlation. There will be exemplars to correlate it to the run. Duration, metric. Why do we need a metric here?
Christophe Kamphaus 00:24:04 We actually do define a pipeline run span.
We need it as a metric. So was that we can query in metric dashboards one from the other.
I'm not sure if exemplos would work in for that.
Josh Suereth 00:24:23 But, Ludmilla, I'd like to counter that. Why do we have Http. Client duration and Http. Server duration.
Liudmila Molkova 00:24:29 No, the run, duration, metric fine, but run info. The sole purpose of it is to correlate.
run, if I understand correctly, run duration to all the other entities, and run id.
Josh Suereth 00:24:43 I see? Yeah, okay, you're talking about run info.
Liudmila Molkova 00:24:46 Right.
Josh Suereth 00:24:48 Yeah. So the
thing we have to sort out here. If you haven't seen like how cube state metrics are used, and like the the idea behind that is, people actually track configuration changes and shapes of entities in metric time series, and they do alerts on them. If you go through like how cube state metrics is used and what people look for. We need a response to that. The question I would have, and I think to get to what you're asking.
Cic pipeline run info! How will someone use this in a dashboard?
How would someone alert on this? What value does it give them? That's the question we should be answering with this Christoph. So like.
it's okay to say, Hey, this link shows how things link.
But if the only reason it exists there is to do joins. It's not a super strong
rationale, but if it's like, Hey, if somebody changes these entity things and it causes brokenness in Cicd, then it's worth actually monitoring that relationship as a time series, which is what we do in Cube state. So I guess that's that's the question to you, then.
Christophe Kamphaus 00:25:52 Yeah. So we did actually investigate a few different ways of including this information.
One way that we managed to gather a run metrics was by adding it to the resource of all the metrics. So for host metrics we use the node exporter
and added, See all the attributes of the pipeline run to it.
That's what I also added in the description above, that additional entry entities as appropriate may be associated to a matrix. That's what I meant with that sentence that we can add it to OS port or container
metrics.
However, on Kubernetes that doesn't work well or at all. We have secure State metrics that are gathered in a standard way, and we cannot easily add
additional attributes to them.
So, for example, we cannot say matrix or a given pot.
Now have additional attributes to denote the pipeline run.
and that's why we need this additional metric.
Ci, CD. Pipeline run info to make the link between both.
Liudmila Molkova 00:27:14 So it sounds to me that they are optimizing for someone who only consumes metrics, and you would want to provide some information for them as a metric.
In other conventions we follow a different principle. We say, Okay, the combination of signals gives you observability. We don't try to pervade everything through one signal.
Well, maybe it's response, but some, anyway, the
different approach could be that this is emitted as event or span or
run starts event that without given slightly different information, it would start when it when it starts. So it's already there when the pipeline runs. But anyway.
and then you can join across different signals. Many backends don't allow you to join across signals. Some backends don't support different signals at all, but that would be more
idiomatic way, and I I don't object that maybe we will end up in the situation. That yes, this is needed because people want to consume it this way.
but from semantic conventions we would probably start by defining this pen or
saying that you can use span information to join things together.
Josh Suereth 00:28:39 We? We actually do plan to call out that you can use entity information to join this together and have an entity to time series. Conversion, so like what Christoph is is proposing here is directly in line with what we see from cube State metrics directly in line with what we see from metrics, heavy users trying to track resource changes in their system
and alert on them. Right? So. I am. I agree with you, Lydmila, though it might make sense, Christophe, for us to hold on making this a semantic convention, you should feel free to have it an opt in feature of, like the collector for people to leverage because they need it
from a metric standpoint like, let's not make the whole industry suffer because we have to figure out some details here, but I do think that this is this is coming, and the the whole, like. Entity. Relationship to metric thing is already something that is out and heavily used the Kubernetes ecosystem, so I think we will have to respond to it in kind and make something that works here in some conf.
When you look at all the Kubernetes metrics coming in from Cube State.
They they all look like this, so I don't think we we can just say no blanketly from semcom, but we will have to sort out our thinking here.
Liudmila Molkova 00:29:50 I'm I'm not saying no, I'm I'm just saying that it's best to be.
I don't know what, anyway, so I'm.
Trask Stalnaker 00:30:00 I have a similar thought just that, like, I think what would help me is to see this pattern because it does feel like a pattern that we would and how this would apply to other parts of semantic conventions and kind of codify that
like is this a general event to metrics. Kind of pipeline span the metrics pipeline.
or, you know, kind of specific or different semantic conventions. Having this.info.
Josh Suereth 00:30:41 I. So my my thinking is again, I I'm comfortable allowing these kinds of metrics to start to exist, to represent that relationship. I would like if we had consistency between what Cscd is doing and what we're doing in Kate's around cube. Steady type metrics that are showing up.
I believe Kristoff has done that. So like. Personally, I'm comfortable. But if we want to have a broader discussion with, like some kind of maintainers about what's our position going forward. That's fine, right? I don't think the entities
by default, metric or entity relationship to metric signal will be available for at least another year
would be my guess at how long it's going to take that group to get through some of the stuff browsers doing. But again, imagine there, there will be a world at some point where this metric would be just a feature of an SDK, where, I say, give me metrics instead of entity signals the same way you could say, Hey, I don't actually want spans. I just want duration metrics, that's all I want.
We give. We give people that flexibility. I mean to Lamila's point. Yes, we want you to use different signals. Best signal for best. Cuj.
but it's possible that, like you know, people won't have a system that understands entity relationships. But they do have a metric system that understands time series and can join them. And that's what they want to use. So we give that to them as an option.
Right? So I do think that this is coming. Will Semcom have to specify all those metrics. Maybe not if we come up with a standardized way to do it from the entity signal to
a info metric.
That's that's kind of the open question in my mind. Yeah.
Trask Stalnaker 00:32:20 How does how does this relate? You mentioned to state metrics? Because like, I've seen state metrics popping up more broadly than just Kubernetes
Josh Suereth 00:32:32 Yeah, so state metric just tracks the state of your system. So, for example, if an entity represents like a pipeline has run right, you can actually use a state metric to see when pipelines run. But you can also push like the the notion that like this.
Here's here's the version
of the Github action of this run right? Or here's the. And then I can check and see when the configuration has changed to say, Oh, when I moved from version A to version B of this Github action. All of my Ci CD. Has failed.
and so, by actually pushing the State as a time series. I can correlate with alerts because I know when the state changes have happened.
So, in other words.
Trask Stalnaker 00:33:20 Configuration state. Okay, I've seen State popping up in a different other ways, like just like your server state like stopped started fail.
Josh Suereth 00:33:31 That's that's also configuration in Kubernetes. So it gets blended. But yeah, that's another thing, because you want to see if, like, you have pods flapping like things are going
on and off quickly or anyway, there's there's a
because Kubernetes is basically a big gitopsy, you know, configuration as infrastructure thing tracking configuration state is tracking infrastructure, and it gets a little blended. But the tracking of the configuration is where the power really comes in, because you can track like, hey? This thing is crashing, and you push the config here, and that led to it. But you can also track, hey? This configuration is not being applied
because my state is like, I'm failing to come into an okay status. Right? So there's a lot of value you get from state tracking and Kubernetes.
but I think the value is partly the pure state, and partly pushing into configuration state.
Trask Stalnaker 00:34:26 So maybe just to try to move on for as follow up one of the things that was brought up was just writing out specific use case, like, specifically like, how how does this help users cause like, maybe if we see that that value that can help
kind of convince people to move along with this.
Liudmila Molkova 00:34:55 And I would love to see a state here like started.
What what is this running for? When is it reported, or
should it have any attributes at all.
Trask Stalnaker 00:35:08 I was surprised not to see any attributes. It's just like a pure linking. But I mean, I I also like I'm starting to understand the pure linking, but.
Christophe Kamphaus 00:35:20 Basically how it was computed. We use the open telemetry collector to transform our pipeline run
spans into this metric.
And that's also why we couldn't easily add additional attributes to it.
Josh Suereth 00:35:39 Trask and Ludmilla. Are you familiar with Prometheus info metrics today?
Trask Stalnaker 00:35:45 Somewhat little bit.
Josh Suereth 00:35:47 Okay, cause all they are is basically every time I hit an endpoint I get a 1. If it succeeded and I get a 0. If it didn't.
Liudmila Molkova 00:35:56 Wonderful. But here there is.
Josh Suereth 00:35:59 So so it's basically the existence of the thing is the info. So it reports. So you report it every N seconds. As you report all your metrics, but you actually use it to say, Hey, this thing still exists or doesn't. And you're you're basically, it's either a poll or it's a periodic push.
But it's the existence metric, right? It's telling you this thing exists, and that actually has some value. When you do like alert denominator. So you can say like, I don't want to alert when this thing is not active. I only want to alert when it's active, because actually otherwise, I get bugs that say, Hey, this thing dropped to 0. But technically it should not have been there, to begin with.
because I'm tracking the life cycle with the metric that's that's like an example behind info. Anyway, I just want to call out, there's like a lot of usage of info metrics in the metric world
that I don't think Christoph should have to do all of it, but I think some of it would be good.
Trask Stalnaker 00:36:54 It would be nice to oh, go ahead.
Daniel Dyla (Dynatrace) 00:36:57 Is that particular use case potentially obsoleted by entity. State events.
Josh Suereth 00:37:05 I I think it will be in the in the future of time. But today, if I'm using Prometheus and it doesn't use entity, state events. What I'll probably do is take my entity, state events, turn them back into an info metric, and then continue to do the use case. The way I do today. Right? So it's it's yes, like, later on, I would expect if you're engaging with entities. And you have this like configuration, observability, storage thing for entity states cool.
But today that's not not the case in some systems. And so we do need to support them.
Whether or not Semcom officially writes, what that metric is
I that that I'm less bothered with. But is this a real use case that that, like actual metrics, people will want and need to leverage, I totally believe.
Trask Stalnaker 00:37:57 Cool for sake of time. Let's move on.
I I but Christoph feel free to bring this topic back in future meetings. It's very interesting.
Liudmila Molkova 00:38:12 Yeah, thank.
Christophe Kamphaus 00:38:12 Yeah, I didn't expect to be as that much discussion around it. But you're exactly right. It's good
to move forward on that in the future to make progress here. On this Pr. You mentioned, adding some
specific use cases improving the description a bit
would unblock it. Is that right?
Trask Stalnaker 00:38:36 At least that would, I think, give us a next topic to discuss
sort of the use cases and to see the importance, because that's 1 of the things that we would weigh like.
The other thing that I'm kinda interested if you have thoughts about how this can apply more broadly like, are there examples in Http or database, or messaging, or any other areas where this type of info metric would be useful. Kind of.
Christophe Kamphaus 00:39:08 In chromatoes. If you monitor a Kubernetes cluster, there's tons of state metrics info matrix, which is basically the same.
It's basically just adding attributes to a metric which is either always one or 0.
Trask Stalnaker 00:39:26 Yeah. So I mean in Kubernetes, because, as just said, everything is modeled as configure, like configuration is state. That but is
is this something that also would work outside of the Kubernetes domain?
Christophe Kamphaus 00:39:43 I don't see why not.
Trask Stalnaker 00:39:45 Yeah. So maybe it like to bring some examples of how that would could apply.
Christophe Kamphaus 00:39:56 Is there.
Trask Stalnaker 00:39:57 Sorry. I'm just vague.
Christophe Kamphaus 00:39:59 Yeah, no problem. I think it's a good topic to discuss. Is there an issue around it
where we could start the discussion.
Trask Stalnaker 00:40:13 Pr.
Josh Suereth 00:40:13 I don't. There. There was some in the entities stuff about how to do entities and metrics, but I think that was a open AI from the Otep. I don't know if we ever created an issue around this, so I think it'd be good to create a specific issue.
That, said, I am.
I am a little surprised at Pushback around infometrics generally. I do think we we should be supporting that in some way, especially how prevalent they are in Prometheus.
Trask Stalnaker 00:40:42 Oh, I I think it's just. I don't feel like we're for me. At least it's not so much push back as education.
I need I need I? I need to be educated a little bit more. I would like to be educated a little bit more on this topic. Sorry.
Josh Suereth 00:41:01 So so maybe what we need then is is an issue that just says, How are we going to handle info metrics in semantic conventions, and then just a bunch of links to how info metrics are used in Prometheus and cube. State that sort of thing, Christoph, if you want to kick off the issue. Ping me, and I'll see if I can fill out some data on it.
Christophe Kamphaus 00:41:18 No problem. I can do that.
Trask Stalnaker 00:41:23 Cool. Thank you.
Alright, James, we got a few topics from you, and a topic from Laudmila. So looks like we have almost enough time based on the timings. But let's see how it goes.
James Thompson 00:41:41 Yep. So those 1st 2 are relating to the discussion we had probably a month ago regarding the OS's right. How do we want to model an OS.
So the changes have been done that we discussed about.
There's links to.net, prototype, etc. But effectively, it's following the Linux OS file model, right? So that
similar naming, etc. So what needed to unblock that now.
Trask Stalnaker 00:42:21 It's like Yahoo was probably the most involved, but he had to drop.
James Thompson 00:42:32 Yeah.
so effectively, the OS type becomes your unix and your windows. And then we add in the additional attributes right for
your OS id stuff like that.
Trask Stalnaker 00:42:51 Okay, yeah. Why don't for sake of time here? Why not?
Will you re-raise that next week? When yao is.
Liudmila Molkova 00:43:05 Also, we would be looking for the review from system approvals.
and we would. It would be great if James, you could
either ping them to review it, or in the slack channel, or join their call if you can.
Either would work.
James Thompson 00:43:27 Yep.
Trask Stalnaker 00:43:30 Good point. Lydmila
alright default. Behavior of attributes.
James Thompson 00:43:46 Yep. So this came up in the.net discussion right about what we should
should required attributes be able to be opted out of I'm excluded.
and what what should be the default? Inclusion of attributes so effectively? I've just put together a summary table. I'm looking for feedback.
so is it included by default? Can it be included by config? Can it be excluded by config just summarizing it at that high level?
What the recommendations are.
Trask Stalnaker 00:44:35 Yeah, we've literally just like what you've added, Okay.
James Thompson 00:44:38 Just that table.
Trask Stalnaker 00:44:39 Included by default
included via config additionally required.
recommended.
So I mean, I'm excluded by config
like I'm just thinking from the you know Java instrumentation, for example, like for opt in yes. This
make sense included via config, and I guess, exclude to be a config is just not including it.
James Thompson 00:45:17 Yeah, because the clarity of config type says, exclude takes preference. So if you include it by config and then exclude it, the excluded will take preference. That's already part of the clarity configuration.
Trask Stalnaker 00:45:32 So what does for? Recommended, though, like, I know, for Java instrumentation, we don't do this. We don't have exclusions.
James Thompson 00:45:43 But wouldn't be coming part of the declarative configuration where attributes can be specified as excluded, especially on the resource side.
It's part of the data model.
Trask Stalnaker 00:45:55 Although, oh, okay, so this is specifically for resources. Then.
James Thompson 00:46:00 It's I say it is.
It could be I. I took the resource focus of it. But on spans we have. Yeah.
Liudmila Molkova 00:46:13 I think that every configuration comes with me in semantic conventions.
So, if so, opt-in attribute may be, the instrumentation may support opt-in attributes, and everywhere we have
yes, or around configuration. It should probably be maybe depending on the instrumentation.
James Thompson 00:46:42 Yep.
Daniel Dyla (Dynatrace) 00:46:45 Is this something that
maybe should exist in the specification right now? We don't have anywhere, I think, where we.
Liudmila Molkova 00:46:56 It's right here. It's I think it's a summary of the text below. It's documented here.
James Thompson 00:47:02 Yeah, that's what I've tried to do. I've tried to summarize that
what perks in a high level
right? And mapping it to the declarative configuration side of things.
Daniel Dyla (Dynatrace) 00:47:12 Yeah, okay, so it's just summary of the alright. Never mind.
Liudmila Molkova 00:47:18 Which raises the question, why do we need a summary?
Maybe we can clarify text. I'm not objecting. I'm just asking why.
James Thompson 00:47:25 It like for me, having the the table is a quick, easy way to look at it right, and with the introduction of the clarity, configuration. It helps having
alright. Can these, should these attributes be able to be included
because the topic came up? Is, should this actually be configurable?
Yeah.
Trask Stalnaker 00:47:51 But that's very specifically for resources. Right?
James Thompson 00:47:57 That's where it started the discussion from. Yes.
Trask Stalnaker 00:48:00 Okay, cause. I'm not sure that I don't see the connection to declarative config for spans, events, metric.
maybe metrics because of metric views.
James Thompson 00:48:14 Alright. So what we're saying is on a span. If an attribute is opt in.
there shouldn't be a configuration for it to be opted in.
Trask Stalnaker 00:48:26 There may be.
James Thompson 00:48:27 Yeah, yes. So that so that include by config. So that's where it comes in. Can this be configured.
Trask Stalnaker 00:48:39 Yeah. So maybe to just Lyn Miller's point on changing. Yes, to May.
James Thompson 00:48:45 Yep or yes, provided to it is supported but by the instrumentation.
Yep.
Trask Stalnaker 00:49:02 Cool in the interest of time. Let's go. Keep going. Prototype of updated Doc. Oh, yes, yes.
James Thompson 00:49:12 So. So I've been working around on this. So what I've done is if you swap the description
alright so effectively, there's 2 parts to it. There's the namespaces, is what we've previously spoken about, which you can go to Rpc. You can see all the events you can see the spans, attributes, etc. That's 1 part.
The feedback last week was wanting to more focus around the domains. Right?
Alright. And that's where this second part comes in.
Alright. So this is this. That's the second paragraph, and there's a new demo of that.
So you can go to the Rpc. Page.
Alright, actually, you you've got. That's the namespace that hasn't changed since last week.
but this one is all new.
Alright. So that's designed to be that page we looked at last week.
so you can go to the Rpc. You can see the G grpc. Etc.
Alright, and then if you click on it, so you click on grpc.
all right. You can see the details of the Grpc.
Alright, you have the scope
all right. I only forward across Grpc.
Trask Stalnaker 00:50:26 Oh, okay.
James Thompson 00:50:27 Like right. But you can see.
Trask Stalnaker 00:50:30 These are the vendor, the sort of vendor specific.
James Thompson 00:50:34 Yeah.
Trask Stalnaker 00:50:35 Ones.
Do we have? Links, like, if we look at the current.
I think we've got links to spans. And yeah, like these do we have links.
James Thompson 00:51:03 Yes, so I can. I can add. So
from that page I can add links to the namespace where everything is defined.
Right? That's an easy to do. That's fine.
Trask Stalnaker 00:51:18 Oh!
James Thompson 00:51:18 Alright!
Trask Stalnaker 00:51:19 And what let's see. So I mean, honestly, this
looking at this, and maybe just because I'm used to the existing. But looking at this was kind of more confusing to me than looking at.
Yes.
like, I'm not sure all this extra is providing value here.
like what? What's on? What? What is this page missing that you are trying to add into this page?
James Thompson 00:51:57 So so this page is very little. The focus, the main focus is if you click on something like the Grpc.
Trask Stalnaker 00:52:06 Yeah.
James Thompson 00:52:07 Alright. So this is where the main focus is
right. So you have the attributes that must be set for all this instrumentation. So you have a clear spot to see that at the start.
Right? So so the Rpc system must be Grpc.
Trask Stalnaker 00:52:36 Yes.
James Thompson 00:52:38 Right, and then you can see the Grpc.
Trask Stalnaker 00:52:41 Is this? Is this changed? Is this page changed from our.
James Thompson 00:52:44 That page is totally new.
Trask Stalnaker 00:52:47 Gotcha. Let me look at the existing.
So our existing we have. Grpc, so that's replacing this page.
James Thompson 00:53:06 Yes.
Liudmila Molkova 00:53:09 Wait. Do we need to replace it in a new location?
James Thompson 00:53:13 The idea would be to move to an automated, generated page.
Alright. So it'd be at the same location.
Liudmila Molkova 00:53:21 I kind of feel it will be much easier to understand if we just replaced more handwritten Markdown
in the same place with auto generated things.
James Thompson 00:53:33 It would be in the same place.
Liudmila Molkova 00:53:36 Would be in the same place.
James Thompson 00:53:37 Yes.
Trask Stalnaker 00:53:39 Right now. It's I mean, it's under. It's kind of been reorganized all the whole thing under domains. Maybe it's.
James Thompson 00:53:46 It's it's only done like that, so so that I didn't have to break it for the Poc. I didn't have to break anything.
Everything has been done in isolation.
Trask Stalnaker 00:53:57 Maybe I'm thinking of how to, you know. Cause this is a this is a math, a very big project.
I'm trying to think if there's like pieces that.
James Thompson 00:54:08 Yep.
Trask Stalnaker 00:54:09 If it could be done iteratively.
Yeah, go ahead.
James Thompson 00:54:16 Bit like for me originally. I started off. Let's start small and
focus on building out a registry of
everything being automatically generated. So, looking at events
right? And now it's grown to incorporating everything.
Right? So yes, this is just to get the idea of it. Then we will be picking out pizza pieces of it!
Trask Stalnaker 00:54:40 Okay. So I think one of the potentially uncontroversial
pieces would be just taking this page and auto generating more of it.
James Thompson 00:54:57 Yep.
Trask Stalnaker 00:54:58 Like it's not, you know, not changing structure, not doing any of that stuff there. There might be like small wins that
we could get along that way.
and then sort of building out because I know you were interested in this, the namespacing side. But I think from past discussions. We were kind of more interested in the domain side.
To the point where in the website registry?
We've discussed
kind of suppressing this like right now, it's top and center. So people, a lot of people click on it. But we actually want people to be thinking of holist like domain
holistically, instead of just, you know, picking and choosing different pieces of it.
James Thompson 00:55:57 Yeah, but effectively, that that Grpc, page you're looking at is this same page you have now just restyled.
That's the key key thing, right? And.
Trask Stalnaker 00:56:10 Sure.
So why, why don't you? Just if you want a small step forward, just take that piece out. Now that you know, like this. Leave this Pr. As is, as you say, like. It's helpful for the big overview
but maybe now we can take out some
implement. Some of the uncontroversial aspects.
James Thompson 00:56:35 Right? Yeah. So like, I think.
I think 1 1 thing that's worth discussing, right is
one of the pain points with that. A page like that. Grpc is. It's massive, right?
Right? Right? And everything is. There's a lot of repetition, right? So if you have a look at what I have
all right in the my sample one. What I did was I reduced that readme page
right to focus on the required and the conditioning required. But you have a link where you can see the full definition
that way, you can quickly look through the page.
Right? Is that of value, or do we keep it as the big long, every all the long tables.
Trask Stalnaker 00:57:27 Sorry we're kind of running short on time today.
I did want to give a couple of minutes to Laudmila's.
Liudmila Molkova 00:57:37 I I can. We can take it as a just the announcement to James point James. I think it could be super useful if there was a summary in front of metric definitions. Or let's say
you have this overview page, the readme page. If we had a a list of metrics, a list of spans reported there, I think that would be useful
like under this instead of Rpc. Span we could have
like this list could be auto generated, and it can contain all of the metrics.
Or if we look into the metrics, we usually have a table of contents. We can generate the table of contents like this right?
And then there are a lot of repetitions. But this repetitions are important, because when you look into specific metric. You get all the information about this metric. There should be full metric definitions somewhere.
We can also have a summary of it.
James Thompson 00:58:40 Yeah, right? Right? And and that I'm fine with, it's about
if we have the readme page right for the Rpc. For all right. And we have alright.
The each of the metrics listed right? And and then, if you want the full definition, you can click on it.
Alright.
Yeah.
I mean. Just have have a look at the demo, and and provide feedback by the demo.
Alright, alright! And have all the actual information in there.
Liudmila Molkova 00:59:23 Yeah, thank, you.
Trask Stalnaker 00:59:40 Cool did you want to say something about this, Lydmilla?
Liudmila Molkova 00:59:45 Yeah, I just this is something we talked about last time. So in in Jenny, I seek, we're actually moving forward to the 1st complex attribute on events.
Well, maybe not the 1st one, but relatively complex that we would like to reuse and spend.
So I'm proposing to relax the policies and
our regal policies to allow them on Spence.
And I'm looking for this group to see if there are any high level objections. And if we wanted to wait longer I would push back on this. But I'm curious if you think we should wait longer.
Trask Stalnaker 01:00:32 I mean, I'm in favor of this is how we get more information.
Yeah.
And I think we have a
pretty definitive answer that we are
pursuing it short of uncovering major problems.
Josh Suereth 01:00:52 The the Otep is merged right.
Liudmila Molkova 01:00:55 Yeah.
Josh Suereth 01:00:55 Yeah. So you, I mean, that's the design, Doc. That's the the decision. You can start.
You can start moving. Let go.
That's that's why the Otep took forever.
You should take that as a this is the direction the community is moving, and let's go so.
Or that's why you yeah, anyway.
Otherwise, what's the point of an Otep.
Liudmila Molkova 01:01:16 It tells us to wait longer, but on the on the Otlp side this is not the Otlp. This is a producer site.
Josh Suereth 01:01:24 Yeah.
Daniel Dyla (Dynatrace) 01:01:26 As one of the people who was kind of responsible, I think, for reset that Otep. That took a long time. I agree with Josh, I think when the Otep merges like that's the decisions made.
Liudmila Molkova 01:01:39 Thank you.
Trask Stalnaker 01:01:41 All right hot. We're over time.
Wow!
Armin (Dynatrace) 01:01:47 Okay.
