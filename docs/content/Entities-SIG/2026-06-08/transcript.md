SIG: Entities SIG
Date: 2026-06-08
Duration: 49 minutes
============================================================

## Zoom Recording Transcript

**Daniel Dyla (Dynatrace)** 04:08 Are we waiting for Josh, or should we… Get started.
I don't see anything on the agenda today except that… Crazio? Krajio? I'm sorry, I don't know how to pronounce your name.
Has a Prometheus topic?
**krajo Krajcsovits** 04:37 What's…
**Daniel Dyla (Dynatrace)** 05:12 Yeah, I think we don't necessarily need to wait for Josh. I think Crejcio, if you want to get started, you can go ahead.
I'm sorry, I had my finger off today because I'm eating during the meeting.
**krajo Krajcsovits** 05:25 Oh, okay.
So, yeah. Hi. The pronunciation is cryo, but anything we'll do, it's… Simpler than my, like, real name.
Anyway… Anyway, so this is just… came out of the… of this issue that I was looking at, and I'm trying to… contribute to the stabilization of the Prometus.
related… Specification and… and projects.
I'm a maintainer in Prometus, by the way. And, Yeah, I was looking at this part, which was about resource attributes, where we say that When we are converting from Prometus to OpenTometry?
We're taking… two special labels as special, so we are turning the Joe Bendo instance label into service name and service instance ID.
And, it occurred to me that Wait a second, this is basically a convention, because we don't have anything to go on, like, we don't know Like, there's no… information in Prometus.
Output, or in the model, about… What's supposed to be… a resource.
attribute.
Unless we can't.
target info.
But, Kind of the question that came up in my mind was that, okay, when we have the entities.
And, assuming that we model entities, In Prometus.
Will that conflict with this convention of using Joband label? And what happens if the entities somebody defines, say, that, oh, I want to have, I don't know, full bar as the… as my identifying resource attribute.
build that conflict? How do we handle the conflict? To be fair, I haven't thought it through totally. Like, I was looking at this today.
But I was wondering if anyone has thought about this aspect.
And, Prep a bit more for… for next time.
That's cool.
**Daniel Dyla (Dynatrace)** 07:55 As far as I know, nobody has done any specific, Prometheus Compatibility, work related to entities?
Part of what we're trying to do is reduce the cardinality of… or control the cardinality of, identifying attributes so that they can be used.
In metrics.
They're also, immutable and such, and then you have the non-identifying or descriptive attributes.
Which are a little bit less restricted.
So off the top of my head, I would say that at least Prometheus should consider that distinction. But honestly, I'm not familiar enough with the current mechanisms to, Really say much about it.
**Josh Suereth** 08:52 Hey, sorry I'm a little late, Can… do you mind if you rephrase the question quick? I'm kind of curious.
**krajo Krajcsovits** 09:00 Yeah, I… to be honest, it wasn't well thought through, but I was looking at this issue, in the spec.
stabilization, Where the question was, okay, should we… maybe stop turning the job and instance label from Prometus into service name and service instance ID.
And, that led me to this question of, okay, assuming that we have entities in the primitives model in the future, which I think Like, I'm actually working on that to some extent, because the… The capability of having, you know, some kind of navigation and providing more context for people and other things.
It's great. So, assuming we have half entities, It sounds like it would… it might conflict with this convention of using the job and the instance label.
And I was wondering if anyone thought about this before, or… You know, what's your gut feeling?
More research, yeah.
**Josh Suereth** 10:04 This, this, this…
**Daniel Dyla (Dynatrace)** 10:05 I misunderstood the question when you first asked it. I thought you were… this is the opposite direction. This is, Kubernetes job and instance you're using as the service name and service instance ID when you're doing… you do that within Prometheus.
**krajo Krajcsovits** 10:23 Yeah, this is the direction of… Prometus to open telemetry.
**Daniel Dyla (Dynatrace)** 10:29 Got it, okay.
**krajo Krajcsovits** 10:31 Yep.
**Daniel Dyla (Dynatrace)** 10:33 I didn't know that that conversion was being done. Is that specified anywhere?
**Josh Suereth** 10:37 Yeah.
Yeah, there's… so, Dana, this… so, sorry if I mispronounced your name, Creo? Krajio?
**krajo Krajcsovits** 10:45 Yeah, perfect.
**Josh Suereth** 10:46 Okay, the, this was part of the initial entity proposal.
Just for context of, like, how to think about this bi-directional. Daniel, there's a Prometheus spec, Prometheus conversion spec, David Ashpole's the one.
On the TC who's been driving that. But it… it talks about how to make sure that service instance name and service instance label, job and instance kind of line up. That's… that was the decision we made, was that those two line up.
I think there's two things to think about here, basically, around job and instance. Like, job and instance are the two identifying labels in Prometheus. Every single entity… every single resource has to only be identified by those two in Prometheus, effectively.
And so, what we've done in this SIG, is first to unblock Prometheus compatibility initially.
we know that for SDKs, service name and service instance ID will always exist. It's like a requirement.
And we've updated the spec to kind of reflect that over time. So, that is how you get data from, like, a client that is an SDK.
how do you get data from a client that is not an SDK? This is where the rug started coming in. So the second problem would be, you might not be talking to something that is part of a service that has an instance ID.
You might be looking at something, like, where the resource is something different. This is where entities can help.
Because what you can do is you can actually fully synthesize an instance ID from, the identifying labels of entities. You would have to actually take them all and hash them.
to create that instance ID, in some fashion. You can make, like, a UUID or something like that, but that's kind of, like, one of the things you can do to get instance ID. For the name, I'm not really sure what you would want to have the name be.
That, that gets more awkward, or sorry, for the job, I should say.
You know, given this is Prometheus, if it's push-based.
we have problems getting you a job name. We'll have to, like, come up with heuristics for that.
at least you get the instance ID, though, so the time series are unique.
For pool-based, obviously, job and instance, you have a default if you need it.
So, you know, the job is named in the service discovery, so… I don't know if that really answers your question.
But if we look at this particular issue.
I think what David was looking at… at one point in time, we were thinking that we could start dropping some things from Prometheus.
compatibility.
around entities. So, for context, if folks haven't seen the Prometheus and OpenMetric spec, right now they are synthesizing a target info metric. So the way… the way that we are modeling OpenTelemetry to work in Prometheus, job and instance are unique, and then the metric labels come after that.
And then the metric value, right? And that makes your unique time series. Then, we synthesize this metric called Target Info, that has all of the resource labels in it, and a value of 1.
And if you need to get resource labels reattached to a metric, you join.
Because the resource labels are kind of the same, right?
for every instance of that resource, but the metrics are different, and this is the efficient way to store it in Prometheus.
it kind of matches the OpenTelemetry data model. Going forward with entity, again, the identity of the resource, if you will, is the entity identifying attributes. I think with, one of the changes Dimitri's making for, entity identity, we might even be able to shrink it further, by the way, for how you would create this instance ID, but we can talk about that in a little bit.
But you get a smaller identity than just the entire resource, effectively.
But yeah, so there's that instance, and then I think what they were talking about doing, at least this was a proposal from David, and I don't remember where the state of it is, instead of target info, we would actually have an entity info that would have the same ID as the resource that it came from.
so that I can do joins across entities now, instead.
Right? Was one of the things that was possibly coming.
I think, basically, target info gets a little… Interesting.
Anyway, so there were questions about how to stabilize this to make this work.
there have been cases of users being confused as to why they can't use processors and job and instance labels. Not convinced that breaking users would be worth the effort of trying to figure out how to do that. So, when this, this discussing one is, job and instance labels, when they come in in Prometheus in the collector, we are converting them to service name and service instance ID. Effectively, we're giving anything that comes from Prometheus an entity of service and service instance, implicitly.
Okay.
**krajo Krajcsovits** 16:12 Yep.
**Josh Suereth** 16:12 No, I mean…
**krajo Krajcsovits** 16:15 No, I think, you know, the point I'm trying to make is that Job and instance.
isn't coming… like, these two label names that you need to process and put them into service name, service name, so… this is not coming from the… from the Prometus model, it's coming from a convention.
It's… it's from outside, right?
it's… it's just the way that we… It's kind of how it works, and and as you said.
when you scripted parameters, you always get the job instance, so we kind of depend on that. But as soon as we implement an entities model.
in Providus, that might conflict with… With what you have.
Well, not even conflict, but, like.
It's a little bit weird to… to follow… Convention, and also the specific Model that we get from entities.
They may or may not conflict, prob… they will probably not conflict, but, like, That's… that's just my… Question, which one takes precedence, if you have the entities?
Information.
**Josh Suereth** 17:30 Oh, you mean… If you have the entity for service name and service instance, or if you have… I think you should always… if service name and service instance exist, you should always use it, even in the presence of entities. It's always going to be… give you a better Prometheus experience.
when you have entities, you can make smarter decisions, and we should figure out what those smarter decisions are and make them. I think that's kind of what this is kind of looking at.
but yeah, I would say that this should always be your default.
And if we can make smarter decisions on top of that, then we can.
**krajo Krajcsovits** 18:11 Yeah, I mean, I commented on this issue, and I kind of said the same, that, first of all, I don't think we should drop this default, because it's working, The alternative is giving you kind of the same things, but, like, a little bit different, so I don't see a point of actually making the change. Like, why would you? What's actually better if we don't do this?
And then my question came up, like, okay, but then what happens with entities? But, I hear you about the smarter decisions.
**Josh Suereth** 18:45 Right, the reality is, right now, with, with, Prometheus, and, you know, this is an overall thing with the OpenTelemetry data model, right, is we have this notion of resource, and a resource is kind of shared between signals, and whether or not we duplicate all of the labels everywhere or join is a rather hard decision to make.
And OpenTelemetry was throwing labels on early that were not super useful to Prometheus. One of the things that David Ashpole's getting at here with this proposal, because we had this discussion, if you think about, you know, Kate's namespace labels.
and Kate's cluster labels, and Kate's, you know, deployment name labels, and those kinds of things, those are on OpenTelemetry Resource. So today, if I'm using OpenTelemetry with Prometheus, and I want to filter based on the namespace resource, it is a join.
And that is actually a really ugly experience in Prometheus today, unless, like, joins become better and more efficient. So the main reason to delete this would be If we were to say, all identifying labels come into Prometheus straight up, and we stop relying on job and instance completely.
you might get a better experience, actually. Like, because the Kate's namespace label Well, depending on how we define Kate's namespace and identifying attributes, right? But if you ask yourself, how do I make the Kate's namespace label be on every metric so I can filter by it without doing a join in Prometheus? That is what this bug is intended to answer.
**krajo Krajcsovits** 20:29 Okay.
Yeah, I mean, there's a parallel work that I'm doing with, another colleague about making… This kind of… we call them metadata first-class citizen in Prometheus.
And, like… our current… Thinking is that like, one goal is to make the join easier. There's already a kind of a solution for that, which is the info function, but also explore the idea of not having to do a join, just If you specify something on the… In your query as a label that we… Figure out it's a resource attribute, then we will just fetch it for you.
But, like, Promoting… all these identifying attributes to series labels isn't really on the table. Like, that's, people were… So far against it.
So either we use the info function or make some magic and make them available on the fly at query time, but… Not put them on series.
**Josh Suereth** 21:47 I mean, as long… to me, as long as the underlying use case is answered, I think it's fine to go either way here, right?
**krajo Krajcsovits** 21:53 Yeah, exactly. I mean, we will be coming out with our proposal for Prometu soon. We have to agree between ourselves, but, like, my main goal with it is to… not even look at too much at the implantation, but just agree on the use cases. Agree on the use cases of OpenTermity UX being better, and also LLM use cases, because that's a hot thing right now. But yeah, and this is for sure one of the I think it's the top one, actually, in our use case list, like, make it easier to use the resource attributes.
Okay. Okay. Alright, thank you.
**Josh Suereth** 22:34 They're all ears.
Yes, sir.
Let's say you use… Oops, space.
service.
training metrics, and currently this… okay.
Cool.
So, I haven't had a chance to check my latest, research into this, but I want to talk a little bit about, big and entity changes. I want to talk a little bit about status of, entity SDK proposals and things. I don't know if there are any other updates from Dimitri or Daniel on Some of the spec PRs you guys had open?
Do you have anything before we jump into this?
**Daniel Dyla (Dynatrace)** 23:19 I do not have any updates. I've been, a little bit… Yeah, doing other things.
**Josh Suereth** 23:28 No, no worries. Okay, by the same…
**Daniel Dyla (Dynatrace)** 23:31 And we've canceled this meeting a couple of times. It's been a little bit out of sight, out of mind for me, unfortunately. I feel a little bit guilty about that, but it is what it is.
**Josh Suereth** 23:40 Apologies, yeah, I, I… we had a holiday in the U.S, and then I did a, like, summit at work, and then I got sick from the summit at work.
And so I know I haven't been here for quite some time because of that, from the follow-on, right? So, yeah.
Okay, let me, let me pull up what I'm thinking here, so we can talk about it. But basically, what I am trying to do right now, I have a prototype of Java that I'm refreshing.
For the SDK that produces entities. I have entity detection working, I have the environment variable parsing working, that's all, like, well-tested, everything works, resources are generated. Where I'm running into fun issues now… is actually around, config. So, I believe if we look here under our specification.
under Resource, if you look at what was stabilized for the SDK, right?
All we talk about is you need to be able to create resources. Either create or merge.
And then, that you should be able to detect things from the environment.
there's this notion of a resource detector package.
That has to return a resource? Mandatory.
And there's a notion that we have… this is the new thing that Config added, okay, where there has to be a specific set of resource detector names.
Container, host, process, service.
what I would like to do Is, add environment here.
That uses the entity environment resource variable, and detects from that.
But also, I want to change this to, instead of saying populates container attributes, that it populates specific entity types from semantic conventions.
How do folks feel about that change?
I think it should be 100% non-breaking.
**Dmitrii Anoshin** 26:03 So, how's it different from what we had, in this, like, spec?
How we read entities from the environmental variable?
I missed that part, sorry.
**Josh Suereth** 26:22 Oh, oh, oh, so, I want to add… so, I want to add a ENV name here that you have to support, and what that thing does is… I'll open up another tab so I don't lose it. That would, we do have entities, right?
**Dmitrii Anoshin** 26:40 Beautiful.
**Josh Suereth** 26:41 That would be responsible for pulling in this environment variable.
**Dmitrii Anoshin** 26:47 Oh…
**Josh Suereth** 26:48 Yeah.
**Dmitrii Anoshin** 26:49 Okay.
**Josh Suereth** 26:49 We're talking about this NVD detector that you're supposed to have and all that. What I want to do is basically, you know, this format would be fully supported, but it would show up in this resource detector name as ENV.
So, we start mandating that you can start specifying that resource detector, and it would pull in the entity bits.
**Dmitrii Anoshin** 27:16 And currently, ANV supported, but it checks, hotel underscore service name and everything.
**Josh Suereth** 27:23 You know, this is where it gets really confusing. Currently, ENV is not configurable in this way. I see. With the name. It is not configurable at all. There is an OTEL resource attributes, which you must use.
**Dmitrii Anoshin** 27:38 Hmm.
**Josh Suereth** 27:40 That, that is totally not, like, it's not a configuration thing. So, I think what I want to do is basically just not touch it.
Like, leave that as is, the spec.
Right? And this… this is… this is not… this is actually part of the stable specification.
This is part of the development specification, but since this doesn't have a qualifier, this is considered stable, so we can't break whatever this is.
**Dmitrii Anoshin** 28:03 Okay. But why do we have to… what would be the value behind that? Is it Boolean?
**Josh Suereth** 28:11 Behind having ENV in here?
**Dmitrii Anoshin** 28:14 Yes.
**Josh Suereth** 28:15 The value is… remember we were talking about how we wanted to specify what order the environment variable thing is specified, and, like, whether it's pulled in? So, first of all, it makes pulling in the environment variable opt-in, but second, it gives the user full config.
over when the environment variable takes precedence, like, order of operations. So if I specify the end detector first, anything from the environment variable would, like, get sucked in first before other things can override it.
**Dmitrii Anoshin** 28:41 Oh, I see. This is the list, this is not a map. There is no way to… okay.
**Josh Suereth** 28:47 Yeah, yeah, this is just the that we'll have, yeah, yeah, so I would put Envir as an option, like…
**Dmitrii Anoshin** 28:53 Yeah, go ahead. The thing is that in the collector, we actually have an end detector, and… When that detected, it reads auto underscore service underscore name, and others. Because in the collector, it's kind of, like, pretty much opt-in behavior, because you don't want that to be said.
Out of the box. But here, I… for me, like, long-term, North Star, I think that environmental variable for entities should be also red.
Always.
Yes. If it's being said, I don't… to be honest, I don't see why is that it… Why it can be…
**Josh Suereth** 29:40 So, so, this is just the names of the resource detectors, okay?
Some of these will be default on.
like, services actually needs to be default on for the SDK.
Like, that's also part of the spec. So, I'm gonna add it as a named thing that you can control the order, but then we also have another thing to make it be default on.
Because I agree with you, it should be default on as well.
So initially, maybe you configure it, but, like, long-term, we want it default on.
**Dmitrii Anoshin** 30:13 Yeah, I'm just… I'm a bit confused. Like, we have hotel resource attributes read by default all the time. We have hotel service name, environmental variable read by default all the time, and we have some built-in priority.
Why can't we add another environmental variable with a built-in priority? I don't understand.
**Josh Suereth** 30:35 No, no, no, this is not defining the environment variable. This is the… so, this is, again, this is for declarative configuration.
This is defining that there will be a resource detector called ENV, which does the environment variable detection. That's all it's saying.
And then we would make the default set of resource detectors include service and ENV.
Again, if you're not familiar with what the configuration folks did, right?
There's now a YAML-based config file for how SDKs will behave, and this is the part of the specification that interacts with us. So what I'm suggesting is I want to make some changes to this. I'll put together a full proposal for it, but I was prototyping, and this is what I ran into in terms of issues that I had to resolve, is first of all.
they have named resource detectors, right? That, I want to transparently make them entity aware.
without breaking anyone using config. So what I'd like to do is actually, since this is still in development too, change this to say it populates the container resource. Change this to say it populates the host resource. The OS we have to figure out, right?
process, say that this populates the process resource. Service, say that it populates the service and service instance, entity. Sorry, I keep saying research. Service and service instance entity, right? And then I want to add end that says it populates, you know, entities based on the… this environment variable.
Right? The same way it says this is based on that environment variable.
So I just want to change this to be kind of entity aware.
is basically what I'm proposing.
**Dmitrii Anoshin** 32:15 Yeah, that makes sense, like, changing that to entity, the only… the thing that I still don't quite understand, why do we need to have another one for… why do we need to have n, essentially, here?
**Josh Suereth** 32:27 Oh, do you want to… do we not want to be able to control the priority event?
**Dmitrii Anoshin** 32:32 But is the priority… priority event is strictly defined in the specification.
**Josh Suereth** 32:39 Oh, is it? Already?
**Dmitrii Anoshin** 32:40 It is, yes, we, we merged that. Maybe, maybe it was removed from my PR eventually, but I remember… oh, here we go.
But, yeah, is this list priority?
**Josh Suereth** 32:56 Let's scroll, scroll down.
The SDK must provide…
**Dmitrii Anoshin** 33:05 Maybe it was removed, or… Yeah, I think.
**Josh Suereth** 33:08 we removed it.
**Dmitrii Anoshin** 33:09 Before it was merged, yes.
**Josh Suereth** 33:11 Yeah.
**Dmitrii Anoshin** 33:11 But I was under impression that that's still the goal that we want to have predefined, because if we put it… As part of… detector, it'll be… maybe… But it'll be too much of the unnecessary interface exposed to the users, because if they don't want a particular entity to take precedence, why don't they change that environmental variable instead?
**Josh Suereth** 33:41 Well, what if they don't have access to the environment variable? What if someone else is filling it out? How do I say I don't want to use it?
Right? How do I turn it off?
**Dmitrii Anoshin** 33:49 Yeah, but we don't have that right now for other environmental variables.
Control.
**Josh Suereth** 33:56 which I think is a problem with the current environment variables, but we do have… we actually do have that control.
**Dmitrii Anoshin** 34:04 Do we? How do we help?
**Josh Suereth** 34:06 So, effectively, there's play… most of the SDKs have a way to ignore the environment variables. Like, they have a way of starting up that will use them, and they have a way of starting up that ignores them.
**Dmitrii Anoshin** 34:19 Hmm.
**Josh Suereth** 34:20 Which, which is… weird.
But they do.
So, I was gonna… I was gonna take that as… as, how things work. What… what I mostly want to get to eventually is when we look here, and we look at… is it… do I want to go to schema? I forget what the… shh, maybe this one.
I want to get to the point where, resource detector… yeah. So then there's experimental resource detection, right?
This one makes me a little nervous, because they have this notion of including and excluding attributes, which… really, really, really makes our entity merge algorithm hellish, if it's not, like, including and excluding entities, right? Because we have to then look and say, are they removing identifying attributes and kill the entity and all that kind of crap? But, you know, it's what it is.
But this thing here is the mo- the thing I want to go after of… There's this notion of an experimental resource detector that I can configure.
And there is a set of these, right? And they don't have, It's not required, which means there would be a default of what is included, but users can override it.
And I want to make sure that the things listed here, which is that list of strings we saw on the other side.
that are required for SDKs to provide, but people can provide new ones. I want to make sure that these are entity.
resource detectors, so they're detecting resources with entities, that's my goal.
And I'm trying to figure this out with, with, with the implementation. So if we click on, like, Experimental Resource Detector, right, you can see that basically it's an SDK extension plugin. They talk about how there's container, host, process, service, and then they show, like, what the config is for each one. This is where I want one called env, which pulls in from the environment.
And if we look at, like, the experimental container one.
There are no additional properties, it's just, hey, this thing exists in the schema.
**Dmitrii Anoshin** 36:21 Okay. Yeah, as long as we have, like, consistent behavior in the NGD detector, so it… if it's not there, if it's not in the list, we don't even take Hotel underscore service underscore name.
I think that makes sense, because it will match collector behavior, which is good, I guess.
**Josh Suereth** 36:41 Yeah, well, so OTEL service name is already handled by the service one, by the way, not by the environment one.
**Dmitrii Anoshin** 36:47 Oh, okay, but it'll be, in that case, Hotel Resource Resource… Hotel Resource?
**Josh Suereth** 36:53 It won't be hotel resource attributes, I actually want it to be the entity thing that you defined here, so it would be… this hotel entities.
**Dmitrii Anoshin** 37:01 But we do have resource now. We need to keep it for backward compatibility, at least.
**Josh Suereth** 37:08 The collector… well, so, the collector would…
**Dmitrii Anoshin** 37:12 No, not collector, we… don't we have hotel resource here as well?
**Josh Suereth** 37:17 We do, but that's why I was going into the specification to show you how frickin' crazy this is. In the specification.
This behavior is a… what?
**Dmitrii Anoshin** 37:27 Yeah, resource attributes, that's what I was referring to.
**Josh Suereth** 37:30 Yeah, yeah.
**Dmitrii Anoshin** 37:31 comfortable.
**Josh Suereth** 37:31 This is be… this is defined as a… like, you can't turn this off.
According to the spec.
**Dmitrii Anoshin** 37:38 Yeah.
is it possible to change it? Because that's the way where it becomes pretty inconsistent.
**Josh Suereth** 37:50 Yeah, I think we can actually… we could actually… I think we can make changes here, but we have to do so in a backwards-compatible way, that's all.
So, right now, the good news is, it says, this is a secondary resource with any information the user provided taking higher priority, which is how most SDKs get around kind of disabling this by default, where you can configure it not to exist, to say, oh, my stuff takes higher priority. So I think there's room with the way that's phrased for us to change this behavior.
To say, like, we… you must extract this by default and merge it, and instead of this as secondary resource, we can actually say, you know, here's how you specify where how, you know, whether or not to include it, and where it is in the priority order, right? So I think this gives us enough room to change it in a non-breaking way, because of this thing, but that's what I was looking at in my prototype. I was running into… All kinds of crazy, hard-coded assumptions in resource detection.
And it was rather exciting.
**Dmitrii Anoshin** 38:57 Yeah. Like, my concern was… it's actually that, for example, let's say I have an app, and I don't have any, it's not introduced. I have host process, and I also have A resource underscore attributes, something.
But now I want to move it to the entities, and I want to… like, keep… let's say… I'll introduce another entity's environmental variable, but it will not work, because I have have not added enough into the list, but hotel underscore resource attribute still works. Still works.
**Josh Suereth** 39:40 here.
**Dmitrii Anoshin** 39:41 Which is pretty… not ideal, right?
**Josh Suereth** 39:46 Yeah, so I guess we have two ways of doing this. One is we… Alright, I think this probably needs to get written down, but my thinking is we use this and update this in some fashion to be the behavior we want.
But we know… what you just mentioned, I also want to be true, which is we want people to be able to move from hotel resource attributes to hotel entities freely, without issue, with it working out of the box.
I also would like it to be configurable so I can turn it on and off, right? Like, this… the way this is phrased and what people have actually done, I think this sentence has been abused to hell.
to actually be configurable for users. So I'm not happy with that sentence, and I think we could consider it possibly a bug, or, like, there's enough English twist that we can you know, turn this into something we want that will be better for users. But again, if you look at the way people have implemented this, it's 100% optional in every single SDK.
Right? There's not an SDK that I'm aware of that doesn't give you an option to turn it off.
And yet, it says you have to do it, right?
So, I think there's… I think that's a problem with spec is actually problematic.
**Dmitrii Anoshin** 41:02 Yeah, so we can go, like, up… Yeah. Adjust the spec according to the real world, essentially.
**Josh Suereth** 41:10 That's effectively what I want to do. Yeah, we'll have to justify it and things, but that's… that's what I'd like to propose. Okay. So, getting back to this a little bit, Daniel.
I know it's been a while. Your prototype in the SDK with entities, did you interact with config yet, and how far is config in the JavaScript world?
**Daniel Dyla (Dynatrace)** 41:32 Config is moved along quite a bit, in JavaScript, Mary Leah's been doing a lot of work there. I did not specifically interact with config in any way, no.
**Josh Suereth** 41:46 Okay.
that's, like I said, that's what I'm experimenting with now with Java, because to finish my prototype to the point where I felt like we could merge it.
in Java, I needed to interact with this… this piece of the spec.
**Daniel Dyla (Dynatrace)** 42:02 Yeah, I think config is the last missing part that I have as well. When I started working on the prototype, there was no config 6 months ago, but it has moved a lot since then.
**Josh Suereth** 42:14 Yeah, so I think we need to kind of catch up. If you have time to kind of look at that as well, I will send you, Right now, I'm kind of tickling an agent to fix up some crap with mine, but as I, when I have a better, PR status, I can send you the one before I started interacting with config, but the branches I have that are interacting with config have been really gross so far.
I can send you what those look like, but I'm also thinking about putting together a… PR for the spec that changes this aspect of the SDK.
My question would be, your SDK spec, Daniel.
should we use that to include the interaction with config, or do we think a separate PR makes more sense?
**Daniel Dyla (Dynatrace)** 43:04 I think a separate… they feel like separate concerns to me.
And I don't think that there's any, like, strong dependency one way or the other.
Right. Like, the config in… in JavaScript is not, I think, likely to cause any problems. I'd be interested to hear why you had issues with config in yours, because you said it was a little bit messy. That indicates to me that there might be some… There might be something that I'm not thinking about that is causing the interaction to be a little bit weird.
**Josh Suereth** 43:41 It's mostly that there are a whole bunch of blocks of code in SDK extensions that do resource detection.
And that code is hard to touch, because that component is considered stable, but all the extensions are unstable.
**Daniel Dyla (Dynatrace)** 43:58 Yeah.
**Josh Suereth** 43:59 extend stable behavior of… with unstable components, it's… Yeah. Yeah, got it.
**Daniel Dyla (Dynatrace)** 44:06 Okay, we don't really have that problem as much, We… have gone the route of… Just documenting unstable, like, additions.
with, like, code documentations to say, like, that this is an experimental, component, but it's within… within a stable module, that's fine. We've been doing that, and I don't think I'm likely to have the same problem.
**Josh Suereth** 44:34 Okay.
That's good. I need to do some experimentation in Go, then, to, like, really nail this, because Go also is gonna have a lot of fun with… I don't know how they're doing config, and I've heard a lot of fun angst with their config, because I know how they do resource detection, and I can't imagine them supporting config without breaking changes, so I think we're probably no worse for wear there. Anyway… The only thing I need from your PR is actually this piece of the spec.
Where you talk about entities.
**Daniel Dyla (Dynatrace)** 45:07 Yeah, okay.
**Josh Suereth** 45:10 Oh, and this is where we talk about detecting entity information from the environment. So this might be the one you were thinking about, Dimitri.
Oh, no, no, this doesn't have environment variable, this is just how to detect it from the environment. Yeah, like.
**Daniel Dyla (Dynatrace)** 45:25 This is not environment… I was gonna say, I don't remember writing anything about environment variables. No, this… that's using environment in a more general… just as a general term.
**Josh Suereth** 45:35 Yeah, like, this is the bit where I think our PRs would conflict, right? Because you have NC detectors should follow the naming conventions of resource detectors, where what I'm planning to do is actually, instead of calling out detecting entity, in fact, instead of calling that out, I'm actually just gonna go hijack the defined resource detectors and say they have to detect entities.
**Daniel Dyla (Dynatrace)** 45:57 Yeah, you told me that, a few weeks ago, I think, last time we talked, and I said that was fine. I just put that line in there because it seemed the most expedient. I don't think that it's important that that stays unchanged.
And I guess I was waiting for the PR that you now have open, so that I can rectify this to match what you have.
**Josh Suereth** 46:22 You mean the… the prototype against Java?
**Daniel Dyla (Dynatrace)** 46:26 No, I mean the environment variable.
**Josh Suereth** 46:32 No, no, no, I, I haven't, I haven't opened… oh, the Environment Variable Detection PR? That's, that, that is already merged.
Or, you know, the thing I'm talking about right now. I haven't opened a PR yet, because I was curious, like, I need, basically, to copy-paste this section of your PR.
Right here.
Or I feel like it should be there, because it's weird to have resource detectors talk about entities without having entities show up in the SDK yet.
Like, we have a dependency hell thing going on. Okay. So, this is just, like, in terms of precedence, I can make my…
**Daniel Dyla (Dynatrace)** 47:09 The last thing we talked about that's blocking this one is the synchronous versus asynchronous, and I just haven't made the change that we already talked about, so I'll do that today, and .
**Josh Suereth** 47:20 get this merged, I will base mine on the SPR.
**Daniel Dyla (Dynatrace)** 47:23 Yeah, I think that works.
**Josh Suereth** 47:24 Okay, beautiful.
That would be awesome. Okay, cool. Anything else folks want to talk about? We only have, like, 10 minutes left.
All right.
Rather productive. Okay, so, alright, let me just add this quick here, Darla.
We'll get, PR updated.
Let's… This one merged before next PR. Dimitri, was there anything you wanted to talk about with the, NCID PR you had open?
**Dmitrii Anoshin** 48:01 No, I didn't have a lot of time to… I just started… I have a PR in Proto, which is in just a draft, and I'm gonna experiment with, on the collector, how it's gonna be used, but not updates from my site yet.
**Josh Suereth** 48:17 Cool. I'm looking forward to trying that out, or if you need prototypes, let me know.
**Dmitrii Anoshin** 48:22 But,
**Josh Suereth** 48:22 and Java, I can start prototyping.
**Dmitrii Anoshin** 48:24 Yeah, there is a proto… draft PR, you can, you can already use it if you want.
**Josh Suereth** 48:32 Okay.
I'll see if I can get a prototype of that. Probably not by next week, because I'm going to try to sort this config thing out, but I'll put that on my to-do list.
**Dmitrii Anoshin** 48:41 I'll post in the chat.
**Josh Suereth** 48:43 Okay, awesome.
Well, thanks, everybody. I guess we'll hopefully see y'all next week, unless we have another one of those, you know, months where everyone can't make it.
Alright, we'll see ya.
**Dmitrii Anoshin** 48:57 Fucks.
**Matthieu Noirbusson** 48:58 Did you, right?
