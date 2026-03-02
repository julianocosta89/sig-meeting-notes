SIG: Service and Deployment SemConv
Date: 2025-10-09
Duration: 51 minutes
============================================================

## Zoom Recording Transcript

**Janhvi** 00:28 Heatrask.
**Trask Stalnaker** 00:35 Hey, Genji. Jenvy, how are you?
**Janhvi** 00:38 I'm good, how are you?
**Trask Stalnaker** 00:42 So… Waking up.
What time is it there? Is it 8am? 8 AM. 8 AM, yeah.
I've been at my desk half an hour, so I should be awake now, but…
**Janhvi** 01:00 I see.
How many folks, usually attend these SIG meetings? Do we usually have, like, good attendance?
Or no.
**Trask Stalnaker** 01:13 I would say good attendance for SEMCOM SIGS is 4 people.
**Janhvi** 01:21 I see, okay.
**Trask Stalnaker** 01:23 So, if we get 4 people, That will be… Good.
Especially if we keep 4 people, sort of, over the long term, but…
Sometimes more, sometimes less.
**Joao G. (Dynatrace)** 01:48 Hello.
**Trask Stalnaker** 01:49 Hey, Zhao.
**Janhvi** 01:50 Hello.
**Joao G. (Dynatrace)** 01:59 This is the first meeting of the cigarette.
**Trask Stalnaker** 02:02 Yes.
**Joao G. (Dynatrace)** 02:03 Nice.
I wasn't sure if I missed one already or not.
**Janhvi** 02:10 No, I think there was one scheduled for last week, but we then postponed it to this week, so this is the first one.
**Joao G. (Dynatrace)** 02:17 Cool.
**Janhvi** 02:21 We'll probably wait for a few more minutes, but everybody can join, and then we can get started.
It got thick.
**Kartik** 02:36 Hey, hey everyone.
**Janhvi** 03:47 Hey, Josh.
**Josh Suereth** 03:56 So, Al, you're supposed to share snacks, didn't they?
**Janhvi** 03:59 the…
**Josh Suereth** 04:00 Don't they.
**Janhvi** 04:01 It's cool.
**Josh Suereth** 04:02 Sir?
How's everybody doing?
**Janhvi** 04:14 All good, thank you.
**Trask Stalnaker** 04:20 Yep.
**Josh Suereth** 04:23 Sue.
Am I right that you took the shortest vacation ever?
**Trask Stalnaker** 04:30 I was… In Pittsburgh.
**Josh Suereth** 04:35 What? And he didn't say hi?
**Trask Stalnaker** 04:39 Visiting colleges with my kid.
**Josh Suereth** 04:42 Oh, nice! Yeah, yeah, good. Yeah. Good.
I may have been on campus when you were there, we were… Anyway, interesting.
Cool.
Sure, we have other people coming? I was gonna say, we normally start these about 5 minutes late for people joining, but I was just curious.
**Janhvi** 05:00 Cool.
We'll… we can wait one more minute, and then we can get started.
I had added a few things to the agenda, but please, everyone, take a look, feel free to add your points as well.
Okay, I think we have 5 minutes in already, should we get started?
Yeah.
Cool. Thanks, first of all, everybody, for joining the first official meeting for this group. Happy to meet, all of you. I know, I think I've met a few of you, but given this is the first meeting, maybe we can do a quick round of introductions.
And then we can get started. I can go first. My name is Janvi. I'm a TL at Google. I mostly work on the Google Cloud Platform side of things, and yeah, excited to work with all of you.
Josh, do you want to go next?
**Josh Suereth** 06:37 Sure.
I'm Josh, I'm also a TL at Google, but I'm on the, technical committee and the semantic convention maintainers, so I'm… actually think that service and deployment have been long overdue for stabilization and actually figuring out what they mean, since they are probably the most used semantic conventions in all of OpenTelemetry.
**Kartik** 06:58 Hey, hey everyone, I'm Kartik, I'm the third person from Google in this call. I'm also a TL in Google. So both Janvi and I work in the tags team in Google, and
So we are interested in, kind of, leveraging, you know, some of these OpenTelemetry attributes, for, you know, for use in tagging resources and, you know, giving, like, a standardized semantic meaning to the tags. So yeah, so look forward to this collaboration and, driving this standardization forward.
**Trask Stalnaker** 07:32 I'm Trask, I'm at Microsoft, I'm also a semantic convention maintainer, and, Java maintainer.
And I like marking semantic conventions stable.
**Joao G. (Dynatrace)** 07:52 So that's why I'm here.
Okay, I'm the last. I… my name is Shuao. I work for Dynatrace. Dynatrace is a,
Back in for… telemetry data.
And I work in a… in a team that is… Basically, working on… Upstream, hotel contributions, so…
Yeah, we have our, our…
Or focusing in helping driving the project, and also help enable people to send hotel data to us.
Or enabling people to stay hotel data to us.
SML, I'm also a maintainer in the SimConf repo.
And yes, I was excited to… To see the service.
service area beams.
Worked on and developed.
**Janhvi** 08:53 Cool. Nice to meet all of you. Okay, I think we can… we can get started with the agenda. I think…
the way we've tried to… I'll quickly share my screen as well.
Hope my screen is visible.
Okay, so as part of this meeting, I kind of wanted to…
give, like, an overview of how we've tried to divide, this project into multiple phases, and then discuss around the first two phases, which is how do we stabilize and add more
attributes to service and deployment, and see if, you know, there are any reservations or any known feedback concerns around that area, and then kind of discuss around that. As part of the SIG proposal, we've tried to divide the whole project in three phases.
So phase one would be extending the service entity, which is already present today with newer attributes, like service.owner and service.criticality.
Phase 2 is…
So we have deployment entity as well in Hotel today. We'd like to see how we can get to stabilize this. I know there are a couple of tickets already around the naming convention. There's some concerns around that area, so we'd like to discuss that and see what is required to finally stabilize the deployment.environment attribute.
And…
The third one is, so we have a variety of… a different variety of attributes around the sensitivity side of things, which are already used today to annotate resource to tell, hey, is this, like, a PI data, customer health data, stuff like that? So we… eventually, we also want to talk to this group and see how do we formulate a group
a new entity, related to data, and kind of add these attributes there. So that would be, like, the phase three, of this project.
So today, at least in this call, and I've been talking to Josh around that as well, first, I think we wanted to kind of…
discuss
what exactly service and deployment really mean, and kind of form a common definition in all of our heads, so that if we are consistent around that definition, right, then we can kind of discuss more on, hey, what are these attributes? Are the namings okay? Are there concerns around namings and stuff like that?
So, I think, Josh, you had a few questions and areas you'd wanted to cover around the service and deployment, right? Do you want to go for that?
**Josh Suereth** 11:33 Yeah, yeah, so I went through, if you, like, if you open up the project link there, this is, like, the second thing I have, but I went through all of the open issues around deployment or service in semantic convention and just threw them in there, so we have a set of things to kind of look at initially. But what I'm noticing is I think.
Service is so generic in OpenTelemetry that we have a risk
that we need to kind of figure out a litmus test of when is something a service, and when is it not a service. Similarly, for deployment, I think we need a litmus test of, like, what is a deployment?
There was… there was a request in here, I think, for service pool name, of like, oh, yeah, so a service is, like, you know, a thing that I run, and there might be, like, 50 different resources of it, so I want to name the pool of resources within a service.
But isn't that the service itself?
Or, the other thing I saw with some of these is the ability to specify a purpose, category, or function.
parts of a service. Like, a service is composed of a database, a service is composed of a web server, a service is composed of a, you know, deployment in Kubernetes. And, so…
Is a deployment a service? Is a Kubernetes service a service? I think we need to start answering some of that question around it.
like…
So, okay, I can give you my thoughts on answering that, but I just wanted to make you aware of these things. Deployment is also interesting. Someone wanted to add data center to deployment.
So you would know what data center something is running in. Well.
Should we be modeling data center itself as a thing where we say, hey, this deployment is in a data center?
Or is, yeah, anyway, so these are kind of some open questions that we see from semantic conventions over time.
The thing I want us to agree on is, like, what is the boundary of a service? And so we can start answering these, like, should we have service pool name?
Can a service be composed of services?
Right? Is it possible that you have one service?
that is made up of several other services. Is that a thing we have, or is that a different concept?
Those are some of the things that I think we need, and when we do… if you go back to the notes of the things we want to add.
when we talk about, like, service owner, right, or service criticality, that might make sense. So, if my deployment environment is production.
and I am service, you know, checkout service. And my deployment environment is test, and I'm service, you know, checkout service. One of these might have a criticality where I don't care about it. One of them might be, like, this is production critical, I need all my alerts firing right away, all that kind of stuff.
So…
Anyway, that's kind of the discussion I wanted to kick off a bit, about, like, what do we think a service is, and do we have a definition?
Unfortunately, I didn't bring my own definition.
Of what a service is. But I thought maybe it'd be useful for all of us to kind of talk through what we think a service is. Does that sound like a good use of time?
**Janhvi** 14:53 I think, Josh, I had a question on that, right? So, at least for service, basic definition is a group of sources, right, doing something could be categorized as a service. And have we heard any feedback or any concerns around
modeling, like, one service which could potentially have multiple services as well. Because this is something we've, at least in GCP, have seen that there's, like, a bigger service, and then it would have smaller… basically, the pool thing, right? Could be another microservice under the umbrella service category.
I don't know how this is done in, like, other clouds or other vendors, but at least in GCP, I've seen that concept.
**Trask Stalnaker** 15:35 So right now, we have service namespace, service name, service ID.
I… Think it… Really complicates things if we…
Tried to say services can be… sub-services.
And… So… I… my initial…
I think… thought is to try to stay within that…
**Janhvi** 16:09 You know…
**Trask Stalnaker** 16:10 We've got service namespace, service name, service instance, and so that kind of constrains our definition.
Already, And if we need to model something else.
Like, a data center, a deployment, something else that would be… A… an orthogonal, you know.
concept that we could sort of layer… layer in, but not really mess with that kind of key namespace name ID.
**Joao G. (Dynatrace)** 16:54 for the… for the pool thing, if I got it right, wouldn't that already be kind of modeled with the service instance ID?
Because… Because you could see, like, a process and a process group, more or less, like…
**Josh Suereth** 17:08 Yeah, no, that's why I called that one out specifically.
Because both service.roll, which was a proposal, and service.pool.
are this notion that service is a bigger thing than what we were… what we're calling now. So, for example, when traffic is seeing service namespace, service name, service instance, right? Service name and service instance would be… service name is the pool.
Service instance is the thing, and then service namespace is the thing that actually all of these people would be calling service name.
And that, that… so, what this says to me, just, just, you know.
off-the-cuff thinking. We have a thing called a service namespace, which is some sort of grouping of services together.
Then we have a service name, then we have a service instance, and that's our, that's our initial data model.
Pool should not exist. Service name should be pool.
Which means people who are trying to do this, like, role-based thing, and like, I want to understand if this instance is my database in the service.
That's not quite what we want in our data model.
The thing I'll say, though, is, Trask, if you look at how service namespace is used in OpAMP,
We just broke it.
**Trask Stalnaker** 18:30 How is… I don't know how it's used in op-amp.
**Josh Suereth** 18:33 the intention behind Service Namespace was… and I gotta… I have to remember this, but it's… it's like,
you could have a namespace be, I have an OpenTelemetry collector.
as the namespace, and so it's only OpenTelemetry Electra instances can be the service, and then the service name would be like, okay, this is my, you know, trace collection pipeline, and the other service name would be, this is my X collection pipeline. So, like.
namespace was supposed to almost tell you, like, what the implementation was. It was pretty… I…
I think that PR got killed, but I remember that was the intention from OpAmp.
It was basically a way to know what configuration you can push down to a service.
**Trask Stalnaker** 19:27 Okay, see.
Yeah, that seems overly constraining.
**Josh Suereth** 19:36 Yeah, I, I, I think we should… if… if, I brought it up, but…
Let's ignore that for now, and just come up with a model that makes sense.
Okay, so we have a service namespace, we have a service name, we have an instance.
**Janhvi** 19:52 Are these… these are different entities that have a relationship with each other?
So if you don't have, let's say, a service under a service, right, it's just one single service.
Then, what is the difference between service namespace and service name?
Basically, what is namespace signifying in that case?
**Trask Stalnaker** 20:16 That's sort of your… your…
**Janhvi** 20:18 Your grouping.
**Trask Stalnaker** 20:20 That you're looking for, like, it's basically one le- it gives you one level of nesting of services.
I see. If you think of it that way, but it basically, as Jess said, the service name
This is your… This is your pool.
**Janhvi** 20:40 Got it.
**Trask Stalnaker** 20:41 So, service instance ID is the specific running process… Pod, Whatever.
Service name is that… cluster.
And service namespace is… gives you one level
Only of grouping these services together into a…
A really, a logical service, a real… service.
**Janhvi** 21:16 So basically, service namespace to service name is, like, one-to-many mapping, and then service name to service IDs, again, 101 mapped.
**Trask Stalnaker** 21:26 One to many.
**Janhvi** 21:29 I see, okay.
**Joao G. (Dynatrace)** 21:37 Yeah, like, the service namespace, nothing is directly attached to it, like, you can't just say service.
But it's just like a grouping thing.
So, like, the service and the service name can be… can be think of, like, they are more or less at the same level. Like, the top entity, top level thing is the service.
**Kartik** 21:58 Bing.
**Joao G. (Dynatrace)** 22:02 And then, I guess, if you have multiple instances of the same service, then that you can think that this service instance ID is under it, more or less nested in it.
**Josh Suereth** 22:14 I just added a demographic.
Sorry, it was real slow there. So basically, like, service namespace can have many services within it.
And this is almost the entity architecture, I'm thinking, is, like, there's a service namespace that is a grouping of services.
there's a service name, which is, like, specific things that happen, and then service instance under it would be, like, you know, this is a specific process running in Kubernetes, or this is a VM, or a process on a VM, possibly, right?
So, service name is… service would be… actually, I shouldn't call it service name, I should call it service.
**Kartik** 22:51 You must first understand that it is a.
**Josh Suereth** 22:55 extent.
Yeah, so if we… if this is, like, the… the thing we're going with,
Service is where we'd, like, track, like, okay, who owns this thing.
This is where the notion of whether it's critical or, you know, kind of off to the side.
That would make sense to track there.
Service namespace is just a grouping of these things.
service instances, specifically an SDK. Like, every SDK creates a service instance ID, so we can uniquely identify this instance within a overall service.
Service would have an owner, an instance, you know.
I push a Kubernetes deployment, I get, like, 12 instances. Each one has an instance, the service itself is the Kubernetes deployment.
Is that fair?
Now, here's the hard part.
**Kartik** 23:47 So, actually, one question, if you don't mind, Josh. So, I mean, if you just take it, try to map it to, like, an example, right? Like, the shopping cart application that you were talking about.
So supposing there's, like, a shopping cart application, it has, like, a front end, and it has, like, a database, and a few other components.
So it's basically like a composite thing, which has, like, Multiple, sort of.
I don't know, like, services within that, doing different things.
So, in that, if I try to map that to this model, would…
Would the shopping cart be the namespace?
And then, like, you know, the front-end component of that shopping cart application be one service within that namespace.
And, like, a backend database could be another sort of component within that namespace. Like, is that roughly what we are saying at this point?
**Josh Suereth** 24:40 Yeah, let me update the… I'm updating the diagram to say that, but yeah, that's kind of what I'm thinking.
So we'd have Shopping CartDB,
I haven't… I didn't have a chance to put an instance there, but, like, maybe you don't have an instance for the database, maybe the… it's a different entity, but,
Yeah, there'd be, like, I have a shopping cart server, I have a shopping cart database, and that's in the namespace of shopping cart.
Or whatever.
Or my shopping thing.
Just to confirm, this is what you're thinking, Trask, as well? Like, when you said there's… okay.
Yao, how about you, from, the Dynatrace side?
**Joao G. (Dynatrace)** 25:23 Yes, that makes sense to me as well, yes.
**Josh Suereth** 25:26 Okay.
**Joao G. (Dynatrace)** 25:28 In Dynatrace, we have this, there's this concept of process in process group.
Instance, or there's a… yeah, there's a process group and a process group instances, and it maps more or less one-to-one to this, so…
The process group instance is the service instance, and the process group is the service.
**Josh Suereth** 25:48 Okay.
And then the… the two fields that we want to add of,
Owner, right? Owner makes sense at a service level, even here.
As opposed to a namespace.
**Trask Stalnaker** 26:08 I think so, I mean… You… Could potentially say that…
You know, if it was important to have a… like, if it was a useful shortcut to have an owner at the namespace level that propagated down or something?
But, ultimately, I think you want that flexibility of… Defining it at a service.
**Joao G. (Dynatrace)** 26:29 Actually, even the description of the service namespace field says that
distinguish a group of services. For example, the teammate that owns a group of services.
So that's the description of… I posted a link to the brand page today.
**Josh Suereth** 26:52 The, the thing I'm… I'm curious about
like, the hard question here is, if we look at Kubernetes, Kubernetes has a thing called namespace. Kubernetes has a thing called service.
While namespace in Kubernetes tends to be used the way we're implying here, it doesn't have to.
And the way Kubernetes uses the word service is absolutely not at all.
What this is.
Right.
So I think there's,
I think there's some parallelization, like, I'm still comfortable with this, I just think we'll need to…
figure out that, you know, when… what is a service, what constitutes a service, and give people guidance on how to model it. So I think maybe that's the task from here, to write that up. Like, take these definitions and things.
what do we expect people to put namespace as? A team? A,
A larger body of stuff, you know?
**Trask Stalnaker** 27:57 I see that… I see it as a pretty flexible umbrella, the namespace.
**Janhvi** 28:03 Yeah. Beast.
**Trask Stalnaker** 28:04 It… it only gives you the one level of hierarchy, which… is limiting.
But it gives you a level of hierarchy to use at your discretion.
**Josh Suereth** 28:22 That does mean we probably want to stabilize it. Does anyone have any concerns with this… this hierarchy in terms of entities, though? Like, one of the open bugs is whether service instance and service are different things.
in the entity world, right? Where you can have a service instance that's an instance ID, and then there's a service entity that… yeah, that's right here.
So the idea would be, like, a service has an identifying thing about it, and a service instance is something different.
**Joao G. (Dynatrace)** 28:55 I think it's again… I think it's again about grouping, right? So, you could have an entity that is the service grouping all the instances.
Whether this entity has… Other value, other than that, that is a bit, yeah.
**Josh Suereth** 29:13 Yeah, but I am thinking, though, that given the discussion we just had.
A service is identified only by its name.
A service namespace is identified by its name, and a service instance is identified by its ID.
Right? That's how we know what these things are.
**Joao G. (Dynatrace)** 29:32 I guess the service must be also identified by its namespace, right? Otherwise, you have… The same service name?
**Josh Suereth** 29:40 This is… this is where, if you read the entity modeling guide, there's a,
We have a telescoping identity, so the idea would be you would report the namespace, the service, and the instance all at the same time if you care that a service is in a namespace. If you don't care that there's namespaces, you just report service name and service instance.
**Joao G. (Dynatrace)** 29:59 Okay, okay, gotcha.
**Josh Suereth** 30:01 Right, so if I ever need to report services where there's namespace capability, I'd have both tags at the same time.
But where… where I only care about the two, because I'm reporting inside of the namespace or something, right, I would only have those two.
Okay.
I think we're getting some answers to stuff. Alright, so… Let's move on.
I think that…
there's an AI to write up some of that discussion and feed through there. Since I opened the bug on the service instance ID thing, I can take a crack at that.
Because I think the next one is also important. What's a deployment?
Right? What do we tag with deployment? What does deployment mean?
We haven't… we have deployment name.
Is there anything else besides, like, it being test and prod we want to… we need.
that… I'll call out, there are literally only 5 open bugs total around service and deployment.
Which is the least number of bugs I've ever seen for any SEMCOF area.
Okay.
Which means, I think keeping this abstract and simple is better.
This notion of deployment data center, I think we can close that, and just say, you know what, a deployment is just the environment.
that you're pushing to
And if we need to add other things, like build ID, right, is a deployment, like, a build? Is…
what do we want to model in deployment today? Do you mind opening the deployment, name that we have today, John V?
Yeah.
**Trask Stalnaker** 31:56 Cozy.
**Josh Suereth** 31:57 Examples are bad.
Yeah, aren't they? Like, I feel like we can just close that bug.
**Janhvi** 32:07 Sorry, this one.
**Josh Suereth** 32:09 No worries, no worries.
**Janhvi** 32:18 Yeah, wha…
**Josh Suereth** 32:19 you know, while in service, I think there's still some things for us to hash out. I think for deployment.
I don't see any evidence that we need further sophistication.
I don't see any evidence that there are issues with what we have today.
And so, the question is, if we look at this.
Do we think there's anything we have to do with this?
**Trask Stalnaker** 32:48 Oh, the example's there,
Oh, yeah, deployment… oh, I see, we have deployment environment name, I see, and deployment name.
**Josh Suereth** 32:59 NID and status, yeah.
**Trask Stalnaker** 33:02 Team, the deployment…
**Joao G. (Dynatrace)** 33:04 Other status might be dubious, but…
**Trask Stalnaker** 33:09 I see, and this has been kind of built out by the CICD foal?
**Josh Suereth** 33:15 I think some of it has come from the CICD folks, yeah. The environment name is the thing that everyone depends on today, and I think the other stuff they've been building out as part of CICD pipelines.
Yeah.
**Trask Stalnaker** 33:31 So what do we place here?
**Janhvi** 33:33 Sorry. I have a quick question on this, right? So, if you talk about deployment.environment.name, and we see that… we say that it can potentially have 3 to 4 values, staging, production, test, whatever.
In open telemetry, how do we, like, model that? We say these are the values that should always be there for these attributes? Like, if I see it here, right, it says these are just examples of values.
That could associate with these attributes, or we clearly say these are the values that we always… like, we have a curated list of values for an attribute, if we know them beforehand.
**Josh Suereth** 34:07 Yeah, so… so we… we model things in, what are called entities now, for resource, or in a signal. So, the way it would work, and again, I think we're only talking about entity modeling in this SIG,
But if you're firing a log event or a metric event or something, you can say, here are the things that are required for that event. And deployment ID, name, and status are all from a specific metric that's coming out of the CICD metrics that OpenTelemetry has.
if you actually click on a different… so that's in the registry for deployment. If you go to… let me send you the link. If you look at the resource description for deployment, which I think is what the SIG would be driving, here's the link.
it only has deployment environment name. That's it. That's the only thing that we define as a resource attribute.
And here, there's, we have to figure out, kind of.
two dimensions. One is, what's the identity of the thing? Like, how do I identify a deployment?
And that would be name, staging, production, whatever. And then what is the, set of descriptive attributes?
So what can describe it beyond just the identity? So for service, the name is identifying, but, like, owner would be descriptive. Criticality would be descriptive, right?
**Janhvi** 35:31 Then, additionally, you have a layer here that's the requirement level, where you can say, I require this, or this is recommended.
**Josh Suereth** 35:38 I, I expect that we would actually, for deployment, we would say the,
We would actually say the name is required every time you want to report about deployment.
**Janhvi** 35:51 Yep.
**Trask Stalnaker** 35:52 Deployment name or deployment environment name?
**Josh Suereth** 35:54 Sorry, Deployment Environment Name. I actually think that this probably should be called Deployment Environment, given that we have…
A different notion of deployment.
**Trask Stalnaker** 36:04 Yeah. Okay, so the entity would be deployment environment.
**Josh Suereth** 36:08 Yeah.
**Trask Stalnaker** 36:11 Okay, and that's what this… that's what we would care about.
**Janhvi** 36:13 That's the only thing we care about.
**Trask Stalnaker** 36:15 Not in this group.
Not…
**Josh Suereth** 36:17 I think…
**Trask Stalnaker** 36:18 employment itself.
**Josh Suereth** 36:20 I mean, that's… that's, I think, the thing we need to stabilize, right? We need to get this deployment environment name stable.
And that's the thing that a whole bunch of people are using.
**Trask Stalnaker** 36:31 So, to, I think, John B's question earlier,
If I understood, Johnvi, you were asking if.
**Josh Suereth** 36:39 like this.
**Trask Stalnaker** 36:40 deployment environment name should be, an open enum, like, where we.
**Janhvi** 36:46 Yup.
have… Yeah, something on that.
Right, right. Because if I look at it, it kind of feels like these are just examples, and people can put in whatever value they want, but I wanted to understand if we kind of specify, like, an enum kind of structure, saying, hey, these are the values that I always expect for an attribute like this.
**Josh Suereth** 37:14 I mean, folks today are using this to mean staging and production.
And I do think there's value in locking… in creating an en… so in OpenTelemetry, all enums are open, just by the way. So, even if we define specific things, people can put whatever they want in there as well.
**Janhvi** 37:31 Nope.
**Josh Suereth** 37:32 But, I do think it'd be valuable to say, here's what staging means, here's what production means, and be able to use that in observability.
So do we have, okay, I'm gonna… I've been failing at taking notes, probably the only…
To recap, probably the only entity we need here… Stabilize is a deployment environment.
We're gonna leave deployment for the CICD SIG, although they did mention they're interested in this SIG, and they might want to talk to us about deployment.
And then, I think we… we have an action item.
Define deployment.environment.name as an Enum, where we can reliably… Understand.
Production.
Versus, tests.
etc.
Is that fair?
Okay.
I forgot to write down the AI for the service one.
That's for me. Does anyone have… does anyone want to take that AI of,
Do we think we're ready to put together, like, a PR proposal, or should we open an issue about this first and have more discussion other places?
**Joao G. (Dynatrace)** 39:12 That's probably an issue, right? Maybe we can also then invite the CI folks.
We'll discuss on it.
**Josh Suereth** 39:20 Okay, define as an enum.
Open an issue for discussion and broadcasts.
Across SimConv community… Okay.
Does anyone want to take that?
**Joao G. (Dynatrace)** 39:38 Again, great issue.
**Josh Suereth** 39:40 Okay. Thanks, Yao.
**Janhvi** 39:44 Quick question, just trying to understand the process, right? So, once we create the issue, we try to get buy-in from everybody, and after that, we create a PR to actually do the change? Is that how it is?
**Josh Suereth** 39:58 Yep, so we're gonna have the discussion just to see if anyone has any major concerns. Changing deployment environment name, will be interesting. So they're, like, specifically, we'll probably have to ping Splunk, because they were very grumpy last time we made any changes.
But we just want to get, like, folks who are using it and depending on it to, like, comment on, cool, if we call this production and tests, like.
It's still an opening noom, so they can still do whatever. I think it's not… it won't be…
immensely breaking, but it will mean that they're, like, people will expect deployment environment name to be specific strings going forward. I think that's good, I think everybody will kind of benefit from that, but we might have a, you know, painting the doghouse problem of,
what color should the, enums be? You know, like, what's the specific string?
I personally don't really care what the specific string is, as long as the meaning's clear.
You know, new product, test, whatever, that's fine. If it's production, if it's test, I don't care. But I have a feeling people might.
**Joao G. (Dynatrace)** 41:04 It's gonna be still open, so it's not like it's breaking immediately, right, so…
**Janhvi** 41:12 Okay.
**Josh Suereth** 41:14 Aptitude split.
Okay, I'm gonna put a PR together around splitting service instance service and service namespace entity.
That was another AI quick, and then this, this next topic.
Do we have any concerns around stabilizing, let's say, service instance that we need to address, that we think we need to walk through?
Like, are there any open questions we have? I listed all those bugs that were there. We kind of talked through them briefly.
Is there anything we're worried about?
**Joao G. (Dynatrace)** 42:01 I don't know where anything… we worked, there was this, like, big work, right, at some point where we defined what the algorithm for the service instant ID and stuff, and after that, I didn't hear anything, or I didn't see anybody complaining, so…
**Josh Suereth** 42:18 No, I also don't think, because it's not stable, I don't think the SDKs are using their implementation of it yet, by default.
So, there's that, but, okay.
Alright, I don't want to take all the time. We only have, what, 2 minutes or so left?
**Joao G. (Dynatrace)** 42:37 I think Tras wanted to say something, sorry, maybe, maybe I have cut you, sorry.
**Trask Stalnaker** 42:41 Oh, no, just for service instance ID, yeah, I agree there was a bunch of,
around that, and we should confirm where it's been implemented. That would be, like, which SDKs do we… have we… has it been implemented in FDKs? Are those maintainers…
**Josh Suereth** 43:00 Onboard.
**Trask Stalnaker** 43:01 With it going stable.
**Josh Suereth** 43:04 Okay.
Can do.
**Joao G. (Dynatrace)** 43:10 Did it implemented in Java, do you know?
**Trask Stalnaker** 43:13 That's where I was going to look.
**Josh Suereth** 43:15 It is, it is, yeah. I've been doing prototyping on entity stuff, and I found Service instance ID. It is in Contrib, or somewhere weird, if I recall correctly. It's, like, not anywhere easy to get to.
But it is there.
**Joao G. (Dynatrace)** 43:30 Okay.
Yeah, if it wasn't humidity one, I would expect to be in…
**Trask Stalnaker** 43:35 Oh my god.
**Josh Suereth** 43:35 to it.
**Trask Stalnaker** 43:36 It's in the…
**Josh Suereth** 43:37 repo, but it's in an incubating module. That's what it was, okay. But in Java, it's literally one method call. You call UUID get instance.
**Joao G. (Dynatrace)** 43:46 Okay.
**Josh Suereth** 43:48 It's different, it's different depending on…
like, the collector, I think, is where it's the most interesting. I can ask, yeah, where… not Yahoo, Jirassi.
Where it ended up.
Okay.
I don't know if we're gonna… with 2 minutes left, I don't know if we want to run the full hour, but I don't think we're gonna have time to do this extending service entity in 2 minutes, and I do think this is the…
the big… the next question I want to just ask briefly… of,
Are we comfortable stabilizing components of service, and then adding attributes to stable things, or do we want to do the whole shebang all at once?
So, like, are we comfortable kind of marking pieces stable? So we could stabilize deployment, we could stabilize pieces of service, and then we can add in owner, add in criticality.
Two stable pieces, or do you want to, like, take this…
**Janhvi** 44:48 Wholesale.
**Josh Suereth** 44:49 How do we feel?
**Joao G. (Dynatrace)** 44:55 I think incremental sounds good, yeah.
**Trask Stalnaker** 44:58 I'd like to at least… I mean, I don't think we have to do it all at once, but I would like to…
See that we have a path forward before we mark
the… anything as stable, so at least I think we should have the discussions around owner and criticality.
**Janhvi** 45:20 Yeah, okay.
**Josh Suereth** 45:20 So, for next week, John V, what do you think about, we take this namespace service instance model.
And we talk about how criticality and owner interact with it.
**Janhvi** 45:35 Yep.
Yeah, we can start the discussion with that.
**Josh Suereth** 45:39 Beautiful, beautiful. And then we can dive real deep into that, because I… I think that when we get answers to that, I…
Given what I saw in the issues, and everyone correct me if I'm wrong here, but I don't feel like we have a lot of blocking things on service. It's mostly just making sure we have a flexible enough design, and there's not a lot of…
Hate for what we have now.
**Trask Stalnaker** 46:05 Yeah, I think service namespace and service name are very widely used.
**Josh Suereth** 46:15 Cool.
**Janhvi** 46:19 Cool, so I think we have a few AIs, and next thing, when we meet, we can just start with criticality and owner. And if we have some consensus there, then we can start thinking about stabilizing some of them.
**Trask Stalnaker** 46:33 And we're meeting every other week.
**Janhvi** 46:35 Yes, so next week, there is, there's an Asia-friendly, call. I think a few folks are in from Japan, I'll talk to them. I'll run them through the same thing, and then the week after that, we can meet again.
**Trask Stalnaker** 46:49 Sounds good.
**Janhvi** 46:51 Cool. Thanks, everyone.
**Josh Suereth** 46:53 Thank you.
**Janhvi** 46:56 Bye.
