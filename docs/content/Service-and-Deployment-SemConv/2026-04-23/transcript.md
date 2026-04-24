SIG: Service and Deployment SemConv
Date: 2026-04-23
Duration: 37 minutes
Zoom Recording URL: https://zoom.us/rec/share/X0xoUSvyyrujl-cJfguM96c2U6_LeXSS4thP6joMYKkR_9ZeUqg6H20W_q32TT_1.4gkJoAge3Q3oY8_l
============================================================

## Zoom Recording Transcript

**Ayushi Asthana** 03:17 Hey, hi folks.
We'll wait for another 2 minutes, and then we'll start.
**Anthony Mirabella** 03:26 Maybe I have a hardware mute on? I… I'm not hearing it.
**Ayushi Asthana** 03:31 Sonya, I did not catch that.
I am.
Oh, it's true.
So, I have added some items to the agenda. If there is anything else that folks would like to discuss, please add that as well. There is a few FYI items.
I have raised some PRs. One is for adding data as an area for service and deployment SIG.
Because I was adding data as an attribute group, parallel to service, so we… I realized we needed to do that as well. Thanks, Josh, for pointing that out.
So I think that conversation needs to be, concluded first. After that, we can add data attribute group, right?
**Josh Suereth** 05:24 Yeah, yeah. I mean, so, this, this just goes into, for everyone's context, Basically, when the PR against data as a group was opened, it's automatically closed because of the semantic convention policy where we want a group of owners for any particular namespace. And so, the second one is basically saying, hey.
you know, this SIG would own the data namespace and all the rationale in there. I don't know, do you want to cover the rationale, Ayusha? Because I just want to make sure folks in the SIG, know what we're signing up for and know what the ownership means and implies.
**Ayushi Asthana** 05:59 Yeah, sure.
So, I have added some context here, but the TLDR is that data introduces some semantics.
about the cargo that is dealt by the services and the deployments in question. So, data can be affected, or it sort of adds context to a service criticality.
It can also be derived from deployment environments. So, basically, data is going to be affected by these two categories. It will enrich the context of these two categories.
Which is why this group is best suited to own the semantics that should exist within data, mainly because of the synergy of these three concepts together, and how they describe the infrastructure.
Right? Josh, would you like to add anything that I've missed, or any additional thoughts?
**Josh Suereth** 07:07 No, I just… I know, so Trask isn't here, but, I know that we're… there was a discussion in the semantic convention maintainers chat about this, So, let me check the status of that quick.
I think it's mostly just about the scope of… and the role of this SIG to make sure we're comfortable with this proposal, and then the SMED Convention maintainers need to kind of approve the PR. I don't… I don't think I have anything to add. I think, like, I understand the rationale. Just wanted to check with everyone here first before we, Proceed and push it. What do those said here?
Yeah, I think mostly it was just a few maintainers didn't know what we were trying to do with, With the data thing, and they saw your proposal to add the data group before they saw the other proposal.
So I… it looks like folks have not responded to my comments yesterday yet, so we'll see. Probably we'll get… we'll get some activity later today.
**Ayushi Asthana** 08:14 Okay.
**Anthony Mirabella** 08:15 to make sure I understand what we're proposing here, then, the data.whatever namespace is new to semantic conventions. So this first bureau would be saying that the service and deployment SIG is responsible for that namespace within the conventions.
the second PR adds detail about that namespace, adds it to all of the issue templates and things like that, as well as the initial category and sensitivity attributes.
It…
**Ayushi Asthana** 08:46 That's great.
**Anthony Mirabella** 08:47 Is there any expectation that other working groups within Semitic conventions might have attributes that need to go in here? Would they come through this group then, or do we expect it to be fairly cleanly separated?
**Ayushi Asthana** 09:03 I'm not aware if there is anything that's in progress at this point.
That should be added to this group.
Oh, Josh, are you aware of any such conversations in battle that are happening?
**Josh Suereth** 09:19 No, but I think your question, Anthony, is why, it's being discussed in the SEMCOM maintainers group, basically, of, like.
So… If we are the owners of that.
Namespace, and another use case does show up, it would come through us.
**Anthony Mirabella** 09:39 Okay.
**Josh Suereth** 09:39 Right? And so if, like, if Semantic Convention says, yes, the SIG owns that namespace, then we become the arbiters of that namespace, and, like, the… the… we own the scope of it, we own, like, its importance, and why it's used, and all that kind of stuff. And so, I don't know… I don't know of any… I'm not aware of any other efforts in that space that are active, but I do expect folks to be there, and it's possible we could decide later.
that if there's enough other use cases around data, we actually spin up a SIG with the folks from here who care about data, and the new folks to deal with data. Like, that… I think that's still on the realm of possibility, but in the interim, it would all flow through us.
**Anthony Mirabella** 10:25 Right, yeah, that was gonna be my other question, was that this isn't a one-way door, right? We're deciding right now, this is where it seems to make sense. If it becomes a bigger scope and no longer makes sense to stay here, it can be split out.
Yeah, I think that's all good then.
**Josh Suereth** 10:38 Yeah, yeah, we're trying to make more things in, in semantic conventions be not one-way doors.
So… Because there's too many that work. So, yeah, this should not be a one-way door.
**Ayushi Asthana** 10:54 Whoa, okay.
So I have… the other thing I had was I have opened a proposal to stabilize service.criticality. I know we discussed adding some more documentation around it, I'm working on that right now.
But the proposal is open, so if this needs to be floated in certain areas where people would be interested in providing their feedbacks, opinions about this, please do share this proposal in those groups.
But this is open now, and I'll continue to add more, you know, docs around what we are doing with criticality and other attributes that we have added in service and deployment in the last couple of months. I know that was a discussion last time around.
That was also an FYI. So the open discussion thing that I had was on Service.cost center. This PR is closed because of inactivity, but I see the comments, and I feel like there were some open things by, James, over here, so I had a few…
**Anthony Mirabella** 12:09 Real quick before we go too far to that, Tyler, did you have a… A question about the data scope, or…
**Tyler Kight** 12:16 Yeah, super quick, if it's not useful, let's move on. This is an ignorant question, I'm more trying to listen and learn here. You mentioned namespace. I'm just curious.
whether or not the scope of this SIG includes, like, cross-service dependencies, where, very, very simple scenario, you've got, like, a Kubernetes-hosted, application, where you have an application team working with a Kubernetes team, where the Kubernetes team has a Kubernetes namespace concept for isolation.
Then the application team is using the OpenTelemetry concept of namespace, while the Kubernetes is using Prometheus.
Maybe Prometheus migrates to OpenTelemetry, but now you have two different teams trying to use the same resource attributes for classification.
Is that, you know, I know that's a little complex, but is that part of the scope of this, or is this kind of like Happy Path, we just focus on, you know, one single, you know, service scenario, and then, you know, multi-service interactions are like a different SIG or a different forum?
**Josh Suereth** 13:17 I can step into that if you want. So, that is a problem we need to discuss and figure out, but that is also a cross-sig discussion to some extent. Like, we probably want to be talking to the folks who are doing the Kubernetes stuff.
I'll give you my own thoughts here, because this has been a problem in OpenTelemetry since Surface.namespace was added, ever, right?
I think there are teams where the Kubernetes namespace and the service namespace are the same thing.
and we want to make sure they're successful. There are places where that's not true. Like, one namespace can have multiple service namespaces, and so… I think we want to make it so you can make them the same thing.
And there are times where they're not.
if we can make that second use case not be confusing as hell for the whole world, that would be ideal. And I think that is on the SIG to kind of discuss and figure out. But yeah, it should, like… We need a way to model your service and deployments.
Right? And how you're running. And then we need a way to make that be magical and easy on Kubernetes.
whether or not the things are exactly the same is TBD, you know?
**Tyler Kight** 14:38 Yeah, and just, like, very small. There's Kubernetes, and then there's also VMs, right, where there isn't that concept of namespace, and that's what I've owned, is the open swimming perf counter, so I'm doing my best to try to connect the dots, bridge the gap, make this less confusing, but I'm only one person, you know, so I appreciate knowing that at least this is on the roadmap, if not right now.
Yeah.
**Josh Suereth** 14:59 He wanted to raise things that you're running into that are hard to deal with as, like, issues for us to talk about and discuss and figure out how to resolve.
That… that's awesome. Like, we… I think that that's a good use of time for us to kind of sort through it, because, you know, the… the whole idea of this is… this is in service of the actual instrumentation and the actual code that's generating data.
So we want to make sure that, like, we're looking at real-life use cases, that we're resolving those things. You know, I mean, if you look at the documents, like, Ayushi's put together for some of these things, or some of the other folks with, like, how, you know, how are we going to use the data? We want to really focus on that. So if you have a real-life use case, we run into problems.
Open the issue, let's discuss it.
**Tyler Kight** 15:43 Admittedly, most of my customers aren't… as advanced, like, some of them are excited, some of them, you know, want to go into this, it's just that they… they kind of need an example to follow, they need someone to kind of handhold them, and so I'm not there yet. I don't… I don't… I haven't really met anyone yet. I hope there'll be roll out there, but but it's good to know this is… this is… a part of the discussion in the future. I don't want to add more until I have something to contribute, so I appreciate it. I'll just listen. Thank you.
**Ayushi Asthana** 16:11 I, I think that my, my question was… kind of similar. We were stuck… the cost center… service.cost center debate, got stuck on that point. I feel like.
Josh, where we were talking about multiple service instances, it's, like, not related directly, but similar. In a sense, multiple instances of services, different instances of services, maybe running in different clouds.
And how do we define cost center for them? And the question of identifying attributes, that's the point I wanted to come to.
Yeah, so this is… this is the confusion I had. First was that deployment is being proposed in the pull request repeatedly.
Does it make sense for cost center to be in deployment?
And the concern about identifying attributes within service. So, the specific case that, I think James mentioned was a call center being reset if multiple instances of the service restart.
And from the documentation, I could understand that there is some concept of identifying attributes within service, resource, and so that should not happen.
But I'm still not sure if my understanding is right, to, like, make a concrete opinion about whether this makes sense or not.
So, Josh, if you have any insights on identifying attributes specifically for services.
**Josh Suereth** 17:49 Yeah, I mean, so… I'm gonna be very, careful with how I phrase this, but effectively, The identity in an entity… there's a lot of misconception coming from a particular commenter around When identity is safe to change.
And what… when we can change the identity and all that kind of stuff. So, in reality, we need to ground on real-life use cases and how people are using these things in practice, and what it means to the experience of you consuming the data when identity changes. So, like, I'll give you some examples, okay?
Process ID. There was a discussion about what the ID… what the identifying attributes for a process are.
Can you uniquely identify a process ID by the… by the PID that, like, the operating system defines? The answer, theoretically, is no.
Because, guess what? Process IDs get recycled.
So you need a timestamp, right?
But could we reasonably assume that you kind of have a timestamp from your data?
that you could use to uniquely identify the PID?
Actually, we probably could.
So should we include process timestamp as a required attribute or not? That was a huge debate in OpenTelemetry. In practice.
Look at what people are actually doing.
When they try to identify things, right? They might use contextual clues of, like, that process is part of this host, and it came at this timestamp. So I know exactly what process it is, you know? Similarly, we had discussions, about using name versus ID in, like, Kubernetes, you know? Name is not unique, name can change.
So, there was a point in time where, folks were adding Restart count.
to a particular, like, pod in Kubernetes, so every time it restarted, it would get a new identity.
And actually, like, there was a question of should the identity of the thing you're observing change if it reboots?
Like, is it physically a different thing or not?
This gets… the reason I'm mentioning that is it gets into the discussion here around cost center of, I loaded in, I'm reporting data. Somebody change… changes, like, where that thing is cost center, because that's actually an orthogonal thing to me.
Do I need to start reporting against a different call center immediately?
A related problem we have on Google Cloud.
people usually look at VMs by the VM name.
So, the VM name is the important thing that they use to filter their data and look at stuff. I can change VM name of a running instance.
Does OpenTelemetry actually change the VM name?
when I change it in the thing, or do they keep reporting against the VM name they looked up once?
For the… until the VM reboots.
It's actually the latter.
Right?
**Ayushi Asthana** 20:58 Yeah, yeah.
**Josh Suereth** 20:59 And why is it the latter? Because practically, it's insane for us to constantly be querying for the VM name all the time.
That's crazy talk, right? That, like, you wouldn't do that. That's a very inefficient, ineffective system, and in practice, you're getting good enough observability to answer questions. If you need the granularity to know exactly you would actually do a join, so you would have something else that tells you, here's when the VM changed, and I would join to something that is more stable. So, what we've tried to do with Entity And with descriptive attributes specifically, they are mutable, so that if you wanted to change it live, you can. But if you report the same cost center for the lifetime of a process, that's totally fine.
Because if you really care fine-grained, and you need to… and you're doing it for, like… if you're tracking this to just get a general estimate of what your costs are, great. If you're tracking this to figure out exactly what your bill will be, you need to be more perfectionist.
Which means you actually need to track at a more fine-grained level, which means you need to actually have a thing that tells you, like, cost center to… you need something that tracks the cost center, you know, API that's changing how things are allocated all the time, and you have to be querying that to get something useful here.
So… It comes down to… the use case.
what is the use cases of cost center? Are we trying to be exact, or are we trying to be relatively accurate to give you a notion of what's going on? And some level of fudge is okay, because efficiency matters.
like, think about me running a service where I literally, to be accurate, I decide, you know, I have to be accurate within one second of what cost center this thing's allocated to. It means I'm pinging the API every second to say, what cost center am I a part of?
that… who's gonna run that in production, in practice? Like, who thinks that's a good idea? So there's a level of fudge there that's fine. So when it comes to entities, that's why I think cost center is A a descriptive attribute.
And then B, folks who care about the granularity of when that event occurs to make a change, they will create a feed That will give you the cost center.
to service instance mapping, right? Or it'll probably be cost-centered to some sort of infrastructure mapping, and then we'll have some analytics thing downstream that does all the joins to make the data be 100% accurate.
That's not the use case we have here. Our use case is to give you a good enough observability to say, cool, this cost center suddenly spiked 10K in terms of usage. And that move happens very rarely.
And when it does, your graphs will be kind of out of date for a bit until things reboot.
That's fine. Like, so… so I… that whole argument, that whole big discussion about cost center changing and how we have to move stuff around, I don't buy at all.
Personally. Like, I think it's bunk, I don't think it's grounded in reality.
**Ayushi Asthana** 24:09 That's fair. I think the other thing that was mentioned there, was about two parallel services that belong to different cost centers. So, basically, there was one use case mentioned where there is a service running in, for example.
some US region in some cloud, and it is… The same service is running in EU, and they both are allotted different cost centers.
And the contention was that if this service that's hosted in US reports some cost center ABC, and then we bring up a service in EU, and it starts reporting some other cost center, XYZ, the feed is going to overwrite and start reporting XYZ for everything.
I… somehow feel like that is not how it would work, because there would be some attributes that are going to differ for both of these services hosted, and so there should be two feeds that should be present at any point. One from the service that's hosted in U… with Cost Center ABC, and the other one with Cost Center XYZ. So, is that, like, the right understanding?
**Josh Suereth** 25:35 Yeah, actually, can you go back to the graph we have of our model, our data model?
**Ayushi Asthana** 25:40 Yep. Yep, yep.
**Josh Suereth** 25:43 So, if you look at it in this fashion.
One of the things that we expect people to assume is not what you're saying, which is, like, if I have service name DB, I kind of expect the descriptive attributes for service ID to be relatively the same.
For that… for anything that's in that service.
So, in my mind, a lot of the discussion around cost center is actually, where in this hierarchy do we put cost center allocation?
Do we put cost center on the instance?
do we put cost center on the service, which can include a couple instances, or do we put it on service namespace? And the thing about, like, oh, I want to run a service across multiple, you know.
regions.
you know, how do we want to ask people to model that? Is it that the service namespace will actually be different, that will tell us it's a different region?
Because again, in this model.
The service name is only unique within a namespace.
Right, yep. So we could say, if cost centers associated with service name, and then all instances are unique within just that service name, great, would have… the same service name would be called DB, And the cost center will be… whatever.
For that region, but the service namespace might be different in the other region.
And our identity is layered, right? So you can, like, if I want to know… if my service namespace is different, the service name, I can filter by that and have it match the same stuff.
But the actual entity identity is different. Does that make sense? Like, I don't know if I'm describing that well. I can show you, like, the telescoping identity stuff we talk about, no tell for entities, but it's kind of a way for you to think about this, of if I'm gonna group cost center data, I need to group it in the hierarchy.
So if we were to put cost center in service namespace, I think we have a huge problem. If we keep it in service name, what it implies is service namespace would have to change by region.
I don't know if I like that, honestly. So it might be that we decide we want to move cost center into service instance.
So that you have fine-grain tracking.
I, you know, I… I think those… that's the kind of discussion I want to have, is like, what granularity do we need to be looking up cost center at in this… in this hierarchy?
**Ayushi Asthana** 28:18 Right.
**Anthony Mirabella** 28:18 Yeah, I would want to echo that point about service namespace not changing just because some attribute, like cost center, lower in the structure has changed, like.
If you've got Blogsite here, as an example, and you're operating it across multiple regions, you don't have Blogsite US and Blogsite EU. You've got your blog for that site.
And some of the instances may live in the US or the EU, but they're even probably part of the same service. Like, you've got US and EU databases.
So… The information about the region would be instance-scoped, because you've got, you know, multiple regions even within those larger geographical regions, and it feels like the cost center probably is the same as well.
Another way of looking at that also would be the cost center is… should be as closely tied to the thing that drives cost as possible, and that gets down to the infrastructure layer, right? The service itself doesn't drive cost. The instances within the service have a cost.
**Ayushi Asthana** 29:26 Yeah.
I actually like that argument, that moving it down one, layer closer to instances might… solve, or might solve this debate once and for all, because there is no logical reason for… two instances of the service to have the same ID.
And service.instance.id is supposed to be unique for, like, on, on, like, a hardware level, as far as I can tell from, the documentation. So, what, what do you think, what do you guys think about, moving cost center to… instance.cotsender. Does that sound like something that would make more sense than having it at a service layer?
Yep.
I'm, I'm just… Thinking out loud.
Yeah.
**Josh Suereth** 30:33 I think so. Yeah, like, that's… I… you know, I didn't think deeply about this before the meeting, so this is my off-the-cuff response, but yeah, like, it… given the discussion we just had, it feels more like it belongs on Instance ID, and it gives us all the power we want, and to Tyler's question in chat, which I think is a good one, you know, we still have a lot of flexibility with having service and namespace abstract between clouds and between craziness, but instance ID is always going to be on a specific thing, right? Like, Anthony just said that. So, tying it there gives us the most flexibility, and all the use cases we initially talked about for cost center.
we can still do, so that's… Yeah, I'm a fan.
**Ayushi Asthana** 31:17 Okay, let's, so I'll take an action item to look into this a little bit more, see, see some evidences in billing for different providers, and we can come up with a new PR for, or a new proposal for this one.
Oh, I like the spooning… I think this is all I had for today. Is there anything else we'd like to discuss?
I think… I think we can have this… that discussion if it's going to be id.cost center or instance.cost center, when we raise, the PR or the issue, but for now, this is… this is what we are sort of narrowing down on.
Good.
I will pause here if there's any other open questions, or… Any other topics for discussion?
**Anthony Mirabella** 32:22 I… I guess maybe one question kind of related to that is… is there any situation in which a service… Would not have instances, but would have a cost center that needs to be associated with it.
like, I'm thinking of, you know, Lambda functions. Do you necessarily associate an instance ID with With the function, with the function execution environment.
Or do you just have service name and no particular instance, because the instance is kind of irrelevant?
**Josh Suereth** 32:57 I know on GCP, we actually, we do care about instance when it comes to disambiguating. So, for example.
if I'm writing metrics from a whole bunch of Lambda functions, and they kind of auto-scaled, I actually need to aggregate away instance to get back to, like, what does this look like overall? And I might get… otherwise, I get, like, the same metric written from multiple things, and I can't figure out that they're different.
So, you know, if a Lambda is reporting, you know, here's how long the HTV latency was, and the resource is exactly the same between every single scaled instance, you get duplicate write failures, because it's like, oh.
I can't tell the difference between the HTTP latency from this one versus that one, so you actually do need instance on Lambda.
**Anthony Mirabella** 33:46 Sure, but there's the fast instance attribute, which may be…
**Josh Suereth** 33:50 So, again, shots fired, possibly. Service instance ID and fast instance ID, we should make them be the same thing. Like, there's no reason it needs to be different. So it would be the same thing there, right?
**Anthony Mirabella** 34:04 Yeah, and that's potentially fair, then. Just saying that there needs to be service instance ID, and… Regardless what your underlying system looks like. If that's the same as fast instance, well, maybe we don't need fast instance then.
Yeah, dude.
**Josh Suereth** 34:21 There's a bunch of instances that, if I could get rid of on the GCP side, like the GCE instance ID, if I could just make that be service instance, because service instance had stabilized prior to that, I would have gotten rid of it, you know. I think Fast Instance is another one where… having it be the separate, but it's probably gonna be the exact same value as service instance, that's probably what we're gonna see in practice for a while, yeah.
**Ayushi Asthana** 34:46 So is it… is it right to, basically… the mental model is going to be instance does not need to be, like, a… Physical… persistent machinery, it's just the unique, entity that's running the application at any given point in time, right? It doesn't need to be, like, a persistent machine that's reporting, these metrics.
**Anthony Mirabella** 35:14 Yeah, and I think even the SDK spec says that if it's not provided in the resource, it should be generated. It's been a while since I've looked at that part of the spec, but I think that's the case.
**Josh Suereth** 35:26 That… yeah, that spec… I… I don't remember if it sta… I think we just stabilized it, but yeah, you're absolutely right, Anthony. Like, the… the… So basically the SDK, if you don't provide one from your hardware, the SDK will actually synthesize its own UUID.
And it does it as a fallback, which is… here's how I'll phrase it. It gives you enough information to uniquely identify where something came from, but it's not a great idea.
Like, you really don't want it to get to the fallback, because it does limit, you know, things that you can do.
you want an identity that's slightly better, you want service name, you want service instance ID pushed down in some fashion, where, like, you're using FASID, and you're using, you know, the AWS Lambda name for service name, like, because that's what people are going to expect. But as a fallback, if we're in an environment where we can't get anything else.
That at least gives you good enough observability, so that's how the spec's written.
**Ayushi Asthana** 36:37 Aye.
Tank… We do not have anything else to discuss.
I'll pause if there's more questions, so it's a good discussion about service.instance.
Global, mate.
Don't think… There's anything else.
Okay, do we want to get some time back and drop off early?
**Josh Suereth** 37:11 Sounds good, thank you.
**Tyler Kight** 37:12 Thanks, folks.
**Ayushi Asthana** 37:13 Thank you.
