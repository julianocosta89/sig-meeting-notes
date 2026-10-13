SIG: Resources and Entities SIG
Date: 2026-10-12
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**krajo (Grafana Labs)** 00:19 Okay.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 00:20 Hello, Kyle.
**krajo (Grafana Labs)** 00:27 It usually takes a while for people to gather.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 00:30 Okay.
**Josh Suereth (Google LLC)** 03:24 Hey, how we doing?
**krajo (Grafana Labs)** 03:27 I hear you.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 03:28 Hey, Josh. Hey.
**Dmitrii Anoshin (Splunk Inc.)** 03:29 Okay.
**Josh Suereth (Google LLC)** 03:30 Sorry, I'm a little late.
**Dmitrii Anoshin (Splunk Inc.)** 03:31 8.
**Josh Suereth (Google LLC)** 03:34 We got a full crowd.
**Dmitrii Anoshin (Splunk Inc.)** 03:37 the.
**Josh Suereth (Google LLC)** 03:38 Good.
**Dmitrii Anoshin (Splunk Inc.)** 03:44 Surprisingly, it's a… it's a holiday in… In Canada, I think.
Maybe in the US.
**Josh Suereth (Google LLC)** 03:52 It's a holiday in some places in the US, yeah.
**Dmitrii Anoshin (Splunk Inc.)** 03:56 Yeah.
**Josh Suereth (Google LLC)** 03:58 I wish it were a holiday here, that's for sure.
**Dmitrii Anoshin (Splunk Inc.)** 04:03 Do I have those?
Right.
**Josh Suereth (Google LLC)** 04:08 Related, I'm actually out next week because it's not a holiday, but it's like a school off day.
And so I'm just taking that week and doing stuff.
Okay.
**Dmitrii Anoshin (Splunk Inc.)** 04:20 I'm not…
**Josh Suereth (Google LLC)** 04:20 Presenting it, am I? How are we all doing?
**Dmitrii Anoshin (Splunk Inc.)** 04:24 Very well.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 04:26 Good. How are you doing?
**Josh Suereth (Google LLC)** 04:29 busy.
**Dmitrii Anoshin (Splunk Inc.)** 04:30 you.
**Josh Suereth (Google LLC)** 04:30 Yeah.
In a good way.
So, let's get to this, and then we're gonna talk about… So SDK prototype.
I was actually just pulling in a bunch of stuff. Prototype and.
Okay.
Long discussion about translational OTP and Prometheus and vice versa here. My mind is the relationship between identifying labels for Prometheus called job and instance and entities until collectors use job and place for Prometheus.
Do you want to just talk through this, Graham?
**krajo (Grafana Labs)** 05:08 Yeah, this question was inspired by Something we talked about last time, I guess 2 or 3 weeks ago now.
When you mentioned that, Sometimes some services would define service name, service instance ID as a way to identify themselves.
And then, you know, resource detectors would come in, and… Attach.
Another, or other identifying attributes.
To… to something.
And, came up that… the… the service, creating its own service name and services, as I see, is kind of a logical identity.
And that… The resource detectors could be viewed as something like a physical identity.
And I took it as, Meaning that these kind of overlap.
Right? And then, what does that mean?
Umm.
And the reason this… Oh.
And yeah, and unrelated to this, there's a discussion in the OTAL to Prometheus and Prometheus to OTAL spec.
About what to do with job instance.
There are some… Use cases where some people want to keep.
Jobby stands all the way through, which would make make them identifying.
There are other use cases.
I mean, preferably, we wouldn't do that. Preferably, we would just use the declared identity of Whatever the service is declaring, and then that goes through.
But in case… You know, do brainstorms.
Is used, and these… Not defined by the… The service, but it's, defined by the scraper.
Then we get into this situation again, where you have something like… Jobinstones are identifying, but there are other identifying attributes, and what does that mean, then?
So.
Basically, what happens when somebody uses that setup. Like, is it… would it be allowed, even, to say that, oh, I'm going to ignore whatever the service is saying, and I'm just going to use job and instances identifying?
**Josh Suereth (Google LLC)** 07:35 So what I, one of our goals is to make it not matter. I, I wanna call out just for context, one of the reasons why job and instance or service instance ID and service name is actually around, other signals with Prometheus. So this is around joining data between traces and logs.
In Prometheus, I open a port that you scrape, so instance can have the port name in it, right?
However… if I am pushing data from OpenTelemetry, there's no port that I can attach to. And so, just like an IP address and a port, or a name and a port, are no longer identified in that way. And we had this issue with Prometheus compatibility around being able to look at a metric and know what… how to query for the Corresponding logs, or the corresponding traces.
Right? And if… and so that's why, like, we want the instance ID to actually come from the SDK itself or from the process?
in Prometheus, even when you guys are pulling data, so that we can do joins to other signals.
So, I don't… I want to make sure that's not lost. Of, like, that's a… a actual real use case here of, hey, I'm looking at Prometheus data, I'm looking at logs, I want to be able to have a dashboard in Grafana or whatever that shows the metrics and the logs for the same thing, and if I change what I'm looking at, I want to make sure that the two dashboards line up.
Okay.
that's just a reminder, right, of, like, some of the complication that led to where we are today. Now, Dmitrii's probably the best one to actually talk about this, so I don't know if you want to jump in now, but the thing that we're discovering with Entities and Resources and Open Telemetry is we were really sloppy with resource.
Okay? There is possibly more than one unique identity in a resource for different types of things. Service and instance ID is a logical identity, right?
The Kubernetes attributes make a Kubernetes identity.
But they might not make a completely unique identity, they might just be unique to Kubernetes. There could also be, like, the container ID, a name, which might be, like, this random UUID made by Container D or by Docker, you know? So there's, like, different levels of identity that fit in the resource, and that is something that we haven't really… lined up super well. We have, like, theories of what we want this to look like, but I don't think we've actually built this in practice where, like, we're happy with it end-to-end. But one of the things Dmitrii's pushing on that I really like Is… we have this notion that we could have a layer of identity, so this would be, like, the service set of identifying attributes, this would be the Prometheus set of identifying attributes, this would be… and we know that those things are the same thing.
Like, we have, like, job and instance, we have a way to resolve that job and instance are the same as service name, service instance ID, even if the values are different. We would have this relationship that would say job and instance of X is the same as service name and service instance.
But in terms of actually solving this problem, I don't think we've really solved it. Anyway, Dmitrii, you had your hand up forever. I think you should… Yeah, from there.
**Dmitrii Anoshin (Splunk Inc.)** 10:50 First of all, I wanted to comment on your first, topic is that, ideally, Prometheus should always propagate wherever is set by the instrumentation, and I think we need to make this as a, like, prescribed guidance for all of the instrumented applications.
no matter how that data for scraping being emitted, whether it's through Prometheus, or for example, let's call… let's take.
MySQL receiver as an example, it gets data from the actual database table, right, to get some… to have some internal metrics. So, ideally, if it's ever being instrumented.
The, those instrumentation identifying attributes should be also exposed through the same interface if possible. So, and it's, it's much easier to apply to Prometheus in this case, I guess, but I think we should make it as a, as a rule and, as a like guidance going forward. Yeah.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 11:54 Dmitrii, could you please just repeat what you said, that Prometheus should always propagate, like, what exactly? I kind of lost the detail there.
**Dmitrii Anoshin (Splunk Inc.)** 12:04 Yes, it's exactly what Josh said. So, for example, if we have an application that is instrumented with OpenTelemetry collector, and it also emits Prometheus metrics to be scraped.
It's probably through the same instrumentation, actually. And those identifying attributes, like service ID, service name, service namespace, should be exposed through the same interface, through the Prometheus, as a… I guess as a target, as a job, somehow.
So, we use the same values.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 12:39 So.
**Dmitrii Anoshin (Splunk Inc.)** 12:39 Same identified attributes, both for traces and for metrics.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 12:43 So what should be propagated by Prometheus is the subset of identifying resource attributes? Is that what you're saying?
**Dmitrii Anoshin (Splunk Inc.)** 12:53 Service id. Yes. Logical identity should be propagated. So.
In that case, we have proper correlation available right through between metrics and traces.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 13:03 Okay, so just propagate logical service ID, but is logical service ID different from the identifying resource attributes? That's what I'm trying to understand.
**Dmitrii Anoshin (Splunk Inc.)** 13:15 It's logical instance ID, it's one of these different sets of identifying attributes, so this specific one is a service identity.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 13:26 Okay, but potentially, that would not be among the identifying attributes as declared by entities. It all depends on what the entities declare, right, as identifying.
**Dmitrii Anoshin (Splunk Inc.)** 13:39 What do you mean?
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 13:41 The… What, I mean, what if, when Prometheus receives a resource with entities, the entities contained in the resource, they will define which resource attributes are identifying right.
**Dmitrii Anoshin (Splunk Inc.)** 14:02 Yes, I'm trying to…
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 14:04 step.
**Dmitrii Anoshin (Splunk Inc.)** 14:04 What do you mean by received?
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 14:07 I mean, like, I mean, Prometheus receives an OTLP payload of metrics, right?
**Dmitrii Anoshin (Splunk Inc.)** 14:13 Okay.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 14:13 And the payload contains one resource, for simplicity.
And then, the resource, it contains one identity, for simplicity, that says which resource attributes are identifying.
Do you follow me so far?
**Dmitrii Anoshin (Splunk Inc.)** 14:28 Okay. You are talking about the different path, like ingestion path into the Prometheus.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 14:33 Yeah, okay, I thought you were talking about… okay, then, I thought you were talking about that.
**Dmitrii Anoshin (Splunk Inc.)** 14:39 I'm talking about like the collection layer mostly here. So like an application that emits metrics, through Prometheus and emits traces, like Prometheus pull model, metrics push model.
My idea was that we should always ensure that identifying attributes match. And typically, it's a service entity.
with, like service identifying attributes. But you're talking about ingestion, the Prometheus.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 15:13 Yes, but I think it kind of corresponds to what you're saying, because you were saying that we should make sure that the identifying research attributes remain consistent, right? That's how I understood.
**Dmitrii Anoshin (Splunk Inc.)** 15:24 Yes.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 15:24 Yes. Yes, that's also what I'm saying, that, I mean, the, which resource attributes are identifying is actually defined by the entities.
**Dmitrii Anoshin (Splunk Inc.)** 15:36 Right.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 15:36 Okay, so then I think we understand each other.
**Dmitrii Anoshin (Splunk Inc.)** 15:40 Okay.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 15:41 Because my point was just that you were saying that a logical service ID should remain consistent throughout, was my understanding. But I'm just pointing out that in practice.
That should mean which resource attributes are defined as identifying by the entities.
**Dmitrii Anoshin (Splunk Inc.)** 16:03 Yes, and in this case, a logical ID typically is a service entity.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 16:06 Yeah, okay.
**Dmitrii Anoshin (Splunk Inc.)** 16:07 And… And if they are being sent in OpenTelemetry format to the Prometheus backend, like, service ID should be marked.
in the Otlp data that has identified an attribute of a service entity.
Does that make sense?
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 16:29 Yes, I think so. I think I understand you greatly. So I'm just noting that Prometheus should always propagate identifying resource attributes, as… Defined by entities.
to… Because what you mentioned about logical, service identity, I think that's… I think that's just like a typical example of which attributes would be identifying. Then I think I have like the exact understanding of what you are saying.
Yeah, that.
**Dmitrii Anoshin (Splunk Inc.)** 17:03 is.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 17:03 Very helpful, thank you very much.
**Dmitrii Anoshin (Splunk Inc.)** 17:05 Sure. The thing is, we can, as George mentioned, we can have several entities in one resource. It can be logical, it can be infrastructure entities as well, like Pod and others. And how Prometheus translate that to the target.
I guess that's another question.
Like, because… can we have a target as a superset of all the entities?
Or something else, and ensure that whenever we scrape, we understand that this superset is, like.
represent different entities. So that question still needs to be, like, kind of resolved. I don't have a clear answer, but I think that this.
End to end.
data flow through Prometheus.
So, let's say we send the TLP to Prometheus, and Prometheus exposes metrics, in the pool model.
if there's a collector that's pulling data from that Prometheus endpoint.
It should be able to reconstruct all of the entities.
I'm not sure how to mechanically do that if we rely on target info.
Or something else, but this is the problem with.
That we need to solve within.
Prometheus interoperability working group. Does that make sense?
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 18:32 Yes, I think so. I just wanted to answer to your last point about, How we can, you know, Precisely represent… All, all the, all this, information.
Because you said, like, you were not sure whether that should be in Target Info?
**Dmitrii Anoshin (Splunk Inc.)** 18:52 Yes.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 18:53 And so my, yeah, so the, the, so what I want to mention is that, krajo and I were actually trying to implement a more, a more, precise, let's say, encoding of metadata in Prometheus. So it's like a project we have called Native Metadata.
And it was… we just reached consensus within the developer group, the Prometheus developer group, that we are going to work towards getting this into Prometheus, although in experimental format first.
So, when… so one big benefit of this native metadata model in Prometheus is that, we can losslessly, represent, hotel metadata, like resource attributes.
Entity, or, you know, aspects of entities and scope attributes, so… Yeah, I hope that kind of, like, answers your question as to how we might do this in the future.
**Dmitrii Anoshin (Splunk Inc.)** 19:54 Yeah, as long as we have end-to-end lossless data translation, that would… that's perfect.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 19:59 Yes, that's the idea. So this is like still like future technology, let's say. But the hope, at least from my side, is that we can phase out target info in favor of native metadata in the future.
**Dmitrii Anoshin (Splunk Inc.)** 20:16 Sounds great. Thank you.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 20:20 And Kaio, you raised your hand.
**krajo (Grafana Labs)** 20:22 Yeah, yeah, I 100% agree. I, like, native metadata will… Solve… You know, all of this, we hope.
And, however, right now, the… The way of working is that we do have target info, and target info is joined with metrics with via the job and instance labels.
And, you know, the fact that we have Joban Instance, which is Something that you can join on, and the particular value in it.
today… Means that if you change any of it, it's a breaking change.
So… the There is a kind of use case, another end-to-end use case, where you want to have Prometheus as a drop-in replacement.
You have… you want to have the Open Thematic Collector as a drop-in replacement for Prometheus, right? That's the stated goal of the Prometheus receiver, in fact, in its README, that you drop and replace it.
And, it seems that today there is a kind of a… Setup.
Where you… where you do this topical replacement.
Where the… Job and instance.
Oh.
As generated by the… By the collector, basically the… in the… from the script configuration, which contains the name of the job, and as Josh mentioned, the IP address and the port number.
That's a use case where this End to end goes through, meaning that You scrape your service, and when you with the collector, and when you send it over OTRP to Prometheus, OPR… Prometheus unpacks it, and the Joban instance are the same. This… The job name, and the… IP address and port.
which means that the truly identifying attributes, your service name, service instance ID, only live inside the target info, but they are not… they are not the ones that are joined on.
Meaning, in fact, Like, they are not… They are not the identifying attributes, because they are not the attributes on this, on the, on your time series.
And that's… Begins consistency.
Oh.
Because in some other configurations, this doesn't happen.
So, that kind of sucks.
And the question is, like, what do we do with this?
Oh.
Should we break it, or is it okay that Basically, you are using a different set of identifiers for the same thing.
**Dmitrii Anoshin (Splunk Inc.)** 23:26 I think if… Just quickly mention, if we have… if we have those available, like, service and other identifying attributes, entities, and entities with the new solution that.
What are we suggested? We should prioritize them instead of job. That's my, that's, that's my understanding. Sorry, Josh. That I think, yeah. Does that make sense?
**Josh Suereth (Google LLC)** 23:49 I'm gonna go up a layer here, because I think that's somewhat true, but I think we need to talk about, like, principles.
A little bit, so we can agree to, like, what our goals are.
Here. So, like, one of our goals is we want to be able to join signals between, Logs, metrics, and traces.
I actually don't care what you use as your identifying attributes, as long as I can easily query and get the identifying attributes that I'm using for logs and traces. Like, if we… like, that's the principle, right? It's like, it doesn't matter. If you make it easy to join, I don't care.
The second problem we have, and this is where I think things get interesting, is I think we're learning there's more than one identity that is reasonable in any OpenTelemetry resource.
Right? Because if we put job and instance in there, that's a reasonable identity for Prometheus. If we put service service instance ID, that's a reasonable for all open telemetry data. And we and to Dmitrii's point, that second thing, we have to make sure we can join back to logs and traces with that.
Now.
The thing that I'm envisioning, and this goes into some of Dmitri's pull requests that are still pending, around, like, tracking the identity context.
I'm starting to think that we have this craziness and resource that we have to deal with today, where there will be more than one viable identity inside of it.
And what we want to do give to you and Prometheus is say, here is the minimum number of attributes you can use.
to get yourself a hash that is, like, the thing that is the identity of this resource that you can then join against. And as long as I can join back all those other attributes to do the cross-correlation, I don't care how you store it, but you need the hash.
Right? You need that ID.
And right now, the way things are with Entities, we're improving the situation where less attributes are needed.
But we actually still have too many, right? Because I think if we have service and service instance ID, we could ignore all the Kate's attributes, because the service and instance ID should be globally unique. If we have the Kate's attributes, we could ignore service and service instance ID. We could pick one of the two, because both are unique.
And that's… that's, I think, the next decision the SIG has to make. Like, this is… honestly, like, I didn't put an agenda on.
because we're in the, like, prototype phase, where we have entities showing up in the SDK. I think this is the next big topic for the sake. Dmitrii, I know you have a proposal around, like, the proto, and some of the things we can do here, but… I… what I'm hearing is, if we agree to this, we should find a way to minimize the number of attributes you need.
You should be able to make a hash.
That uniquely identifies the resource.
Or the source of the data, the target, if you will.
And then, as long as we can join all of the other attributes from the entities together against that, in a way that allows us to do cross-signal correlation, that's our goal.
I'm gonna… I'm gonna stop there and just make… confirm with everybody.
**Dmitrii Anoshin (Splunk Inc.)** 27:00 That makes sense.
**krajo (Grafana Labs)** 27:02 I think that makes a lot of sense, and especially in the native metadata context where we want to get rid of the join and hide it, meaning that whatever hash.
Makes things unique and identifiable, we're good with.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 27:17 I basically agree totally with this, Josh, but what I didn't quite understand was, like, Rhys saying that.
For a resource, There could be several, several different identities, each of which is uniquely identifying.
For the resource?
**krajo (Grafana Labs)** 27:38 moved.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 27:39 You're muted, Josh.
**Josh Suereth (Google LLC)** 27:42 Yeah, I think what we're finding out as we're using the Entities thing we have, we have less attributes in the Identify thing, but we still think it's too big.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 27:51 Yes, absolutely.
**Josh Suereth (Google LLC)** 27:53 If you look at… yeah, yeah, if you look at what I'm writing here, like, with Logical, right?
If you were to use Service Namespace Service and Service Instance.
You could get away with just hashing those 3 and get something fully unique.
And I think the same is true for Prometheus, if you use job instance, for that Prometheus instance, right? So, like, if both of these show up in resource, or if all of these show up in resource.
What do you make be your unique ID today?
Today, it would be all of those attributes.
But I think we can do better.
It's just figuring out how to… how to do that is kind of the.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 28:35 So what my question is, are you suggesting that there should be some way of finding or picking one of the different sets of identifying attributes?
Like, in this example, there's logical, there's Kates and Holst and so on, and it should be possible for Prometheus, for example, to pick… to enumerate those sets and pick one of them.
**Josh Suereth (Google LLC)** 28:59 That's kind of what I'm thinking, yeah. That's like… like, again, this isn't fully formed, I haven't done designs, I haven't done prototyping, but based on Dmitri's PR, updating Proto with some of this, it's the thing that's been running through my head, of like, would it make sense for us to do this or not?
As, as, like, a phase… as part of phase two.
Because again, we're better than we were before. There's less attributes you have to have here, but… You know, given the discussions we're having and some of this confusion, maybe we need to go even deeper.
I'm curious, I do need to drop in about 5 minutes, but I'm curious what other people think.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 29:37 I guess what is on my mind is that the when converting from OTLP to Prometheus, we just need a way to kind of determine the subset of identifying attributes, you know, when entities are involved, so that Prometheus can generate a hash.
to put on each time series, because that's necessary to keep the time series unique. They need to kind of be identified by the resource.
And I also want to just add that.
assuming we have native metadata in the future, there will no longer be the need to join. That Prometheus will kind of, like, connect each time series to the native metadata set automatically.
And as a follow-up, In that future, we might introduce another label than job and instance to contain the resource hash.
How does that sound?
**Josh Suereth (Google LLC)** 30:47 Yeah, I… so, I mean, like… For… maybe I'm thinking of making things perfect, and perfect is the enemy of good enough. If you use all of these, you'll get an ID, and that ID will be unique, because the reality is, if you have service instance ID, and you have container.
This doesn't add any cardinality, because this has all the cardinality, and the two are fully unique.
kind of together. So if you treated one as descriptive and one as identifying, or vice versa, and if you treat both of them as identifying, it shouldn't actually change the behavior of the system.
So, you're totally fine there. I'm just, like, there's a piece… there's something in the back of my head that's wondering if we should actually just go straight at, you guys only need these 3, and you could index on that, or you only need these, and you can index on that.
Umm.
As opposed to indexing on.
The whole kit and caboodle.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 31:46 Yes.
But I think the question in my mind is then.
how do you correlate with other signals? Is it maybe that you would know that you can correlate on the Kates, the subset of identifying attributes? You could correlate with traces, for example, using that? Yep.
Yeah, I think it's, like, abstractly makes sense, at least.
**Josh Suereth (Google LLC)** 32:11 Yeah, yeah, yeah. Go ahead, Craig.
**krajo (Grafana Labs)** 32:13 I was literally going to say the same thing as you did, Josh, that from Prometheus' perspective, we just want to have something that identifies unique identifiers, so if we hash on the… all the entities, that's good for us. If it's redundant information inside the hash, that's lost in the hash, so we don't care.
So, I think that's fine. But Arve's question is very relevant, like, yeah, it… it becomes… It might become tricky how to correlate, although Again, with native method, or… And even with Target Info, you get all the attributes in Target Info.
Of course, you have to jump, like, a hoop, because you have to go from your time series to target info, and then correlate, but, like, the data is there.
**Josh Suereth (Google LLC)** 33:03 Yeah.
Okay, I do need to drop. I think this was a good discussion. I think we agreed Agreeing to the principles is kind of what I think matters, so that we can get to something. It sounds like if you use what we have now, where you use all of these and have a join, we get what we want in both cases.
And then maybe for the Entities sake, like those of us pushing on proposals like Dmitrii, your proposal.
We might be able to do better with this layout, but that shouldn't block Prometheus if we're able to do that. Is that fair?
**Dmitrii Anoshin (Splunk Inc.)** 33:44 Yeah, sounds good. Prometheus would potentially need to just use that additional information that we pass.
To represent those… this chain, right?
**Josh Suereth (Google LLC)** 33:54 Yeah.
**Dmitrii Anoshin (Splunk Inc.)** 33:55 This makes sense.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 33:57 Yeah, I was just going to say that, I was just getting this idea that, maybe, like, if this comes into fruition, like, Prometheus could perhaps, like, store the individual subsets of identifying research attributes, like, it could store that there's a logical subset, there's case subset, and then It could surface that either through PromQL or API, perhaps?
So, like, like, maybe you know that, there's, like, a CATES subset of identifying attributes, and then you, you, then you kind of, like, you, you, query Prometheus on that. Does that make sense?
**Josh Suereth (Google LLC)** 34:39 Yeah, that 100% makes sense to me. That's kind of why I'm thinking of it's something we need to kind of tease out.
Okay, I have to drop now, but, I think this was a great discussion, thanks for raising this. I think it gives us some next steps. For context, you can now, produce entities in Java.
So, if you're using Java and you use config for resource, you'll get entities coming out of the OTLP. So that is now as of the latest launch.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 35:08 I was wondering whether Prometheus should already start implementing support for Entities.
**Josh Suereth (Google LLC)** 35:14 Yeah, like, give it… so… We we normally have this phase where we go implement it in the SDKs and then wait for people to use it and then stabilize. But if you since Prometheus, you have that experimental flag support.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 35:27 I.
**Josh Suereth (Google LLC)** 35:28 I think you should totally do that. Yeah. Because you could support ingesting them. Java can produce it, so you can test it end to end with Java ready to Prometheus. We can see what things look like.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 35:37 Okay, I'll keep that in mind, like, I might go ahead and do it.
**Josh Suereth (Google LLC)** 35:42 Yeah, I'm gonna follow up with, like, David Ashpole was working on the Entity Go prototype, I might take that over from him, work on that next. And then Dmitrii, I think we need to start talking about the… Both this multi-layer identity and the Entity events.
**Dmitrii Anoshin (Splunk Inc.)** 36:01 the.
**Josh Suereth (Google LLC)** 36:01 There's, I don't have time to get into it, but we had in the Semantic Convention discussion today.
There was a discussion around.
Loaded packages, and the relationship between a process and loaded package, and they're creating events that look similar to an entity relationship events for what pack… like, what packages were loaded on a project.
Okay, so if you're dynamically loading in things in Java or.net or whatever, that they're using to track instrumentation, whether or not something fits up, and it feels like we should start making some progress on that next, if if we're ready to start moving while we stabilize the SDKs. Okay.
**Dmitrii Anoshin (Splunk Inc.)** 36:41 Makes sense. Yeah, I've… I was… I tried to revamp the work on the HTCS today, and I have, like, some ideas. I believe that the last time we discussed whether, like, my proposal kind of still makes sense, but whether it's.
attribute of a parent to the child, or not, that's probably something that we still need to figure out, and I'll maybe submit another.
Proposal, and at least, like, revamp my previous one for the specification.
**Josh Suereth (Google LLC)** 37:14 Cool. Well, I'm excited to start… now that we have actual prototypes, we can start using this stuff live, too, so we can…
**Dmitrii Anoshin (Splunk Inc.)** 37:19 Yeah.
**Josh Suereth (Google LLC)** 37:20 Actually talk with real everything working. It'll be great. All right.
**Dmitrii Anoshin (Splunk Inc.)** 37:24 Sounds good.
**Josh Suereth (Google LLC)** 37:24 I'll see y'all. Thanks.
**Dmitrii Anoshin (Splunk Inc.)** 37:25 Cool. Thank you, folks. Bye.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 37:30 Do you…
