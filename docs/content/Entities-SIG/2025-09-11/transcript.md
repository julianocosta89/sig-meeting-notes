SIG: Entities SIG
Date: 2025-09-11
Duration: 33 minutes
Zoom Recording URL: https://zoom.us/rec/share/X35zRvQUj87CBc6zMFbKlFmDMw8B-LI5KDRLCx-rmPHhfWqyKH9rYygxTimFTjgH.YsLPfem4KSddIwzD
============================================================

## Zoom Recording Transcript

**Josh Suereth** 01:08 Hey, everybody.
**Ted Young** 01:12 Yo!
**Daniel Dyla (Dynatrace)** 01:13 Hello there!
**Josh Suereth** 01:28 Alright, so… Added one topic to the agenda, but please feel free to add other things we need to talk through. Mostly what I want to do is continue… we had a discussion a little bit last week.
on, communicating entity and breaking change, and going through the current OTEP, and kind of addressing comments together. I think we didn't finish that discussion, so I kind of want to talk through it, first, and kind of go through the OTEP overall.
other folks have things they want to talk through, like, feel free to insert your topics. This might take… a good bit, so I want to make sure we get through high-priority things first.
**Daniel Dyla (Dynatrace)** 02:09 In my mind, this is the high priority thing.
**Josh Suereth** 02:12 Okay, okay. I mean, I didn't have anything else I thought was higher priority, but in case someone does, like, I just wanted to call that out. Alright, let's take a look at the comment.
Again, actually, Daniel, I think you had a lot of really good points. Do you wanna, Do you want to kick us off while I find the comment?
**Daniel Dyla (Dynatrace)** 02:33 I can, yeah. So, if you're referring to what I think you're referring to, there was a comment on the OTEP that, adding… Allowing mutation on resource was a breaking change.
Right? Is that what you're referring to?
**Josh Suereth** 02:56 Yes.
**Daniel Dyla (Dynatrace)** 02:58 So, in practice, people have been really doing this for a long time. You have a lot of situations where it comes up naturally, like on Lambda, for example, each startup of a Lambda may have different resources. You have people who modify the resource in collectors, and you have people who, even in SDKs, have found ways to, especially on some of the dynamically typed languages, to get in and fiddle around with resource during the run of the process. The specification states that resource is immutable.
In practice, not always 100% true. But Josh brought up a handful of cases where the immutable resource is actually quite useful.
Which is why the identifying attributes are still immutable. But in order to take advantage of that.
Receivers have to be updated to, you know, understand resource.
to know which… or to understand entities, to know which resource attributes are immutable and which are not. So if you have an existing receiver, which is using the immutability In important ways.
and we update the SDK to now allow mutating entity descriptive attributes, which then mutates the resource, because all entity attributes are resource attributes, you have potentially broken those receivers.
Is that a reasonable summary, Josh?
**Josh Suereth** 04:44 Yes, I would also add… I'll add this here.
There's a… there's an inverse problem.
Right? So, update sklint uses entity, now mutable attributes… Impact resource… breaking receiver.
So, problematic case number one. We also have the second issue.
Problematic case number 2, which is, for example, host.ip is now… A descriptive attribute.
Existing users that put this on resource.
would be unable to.
in entity world, right? So, like, existing people.
Are using attributes that we think are descriptive, or that mutate, or change.
**Daniel Dyla (Dynatrace)** 05:40 And they're using them as identifying attributes.
**Josh Suereth** 05:43 they're putting them in resource, which implicitly means that they are identified. I think, in general.
They are either using them as identifying, or they don't actually use resource as identifying attributes. One of those two is true.
**Ted Young** 05:56 I don't think that resource in any way, shape, or form indicates something is identifying, and how people use it practically, right?
**Daniel Dyla (Dynatrace)** 06:05 It certainly is, at least in metrics.
**Josh Suereth** 06:08 In metrics. In metrics it is, and in op-amp it is.
**Ted Young** 06:11 Yeah, I would absolutely disagree with that, Ted.
**Josh Suereth** 06:15 I think it's split. I think there are people who don't give a crap about whether resource is identifying, but they also don't understand why we have resource at all. And then there are people who heavily rely on it being identifying in various weird ways that are awkward.
**Ted Young** 06:30 Yeah.
Right, like, I do… I just want to emphasize that some resources are identifying, but the net effect is, like, resources is essentially MV, right? In practical purposes, the attributes that are repeated everywhere and are more closely associated with M than with this operation or this metric.
Like, that all just gets crammed into resource.
And some of those things are, you know, good, high quality, low cardinality, identifying whatevers, and other things are IP address.
**Daniel Dyla (Dynatrace)** 07:05 Yeah, that's what we're trying to sort of fix. But the point is that in, you know, the current state of the world, what we have said, the stability guarantees that we've made, and all of that stuff, is that we are breaking at least some assumptions around resource.
So… I don't remember exactly how far we got in the conversation, But there are a few possible ways to handle this. The first, and most obvious, and I think most, straightforward way, and kind of what we've been doing, if we just keep doing what we're doing, is just accept the change. Just say, we know this is breaking for some people.
And… it is what it is.
**Josh Suereth** 08:00 I…
**Daniel Dyla (Dynatrace)** 08:02 don't think that I love that idea. I could maybe be convinced of it, but I.
**Josh Suereth** 08:09 Can I rephrase it?
Can I rephrase it? Yeah, go for it, yes. Like, to Ted's point, I would say there's a class of people that don't care about resource identity. At all.
And what we're saying is, those people are blissfully unaware of entities. They don't have to care, everything continues to work for them, we don't break them.
What we do break is people who do care about identity now have to pay attention to the new thing. So that class of users would break, but it's also… those are our target users. Those are the ones who are driving entities who are complaining about the existing state of resource. They're the ones who need the identity.
So, it's like… the people who would pay attention to us are the ones we're targeting with a breaking change, is how I would phrase it. And yeah, I'd agree, like, they're the ones that would need to update their receivers to pay attention to identity from entity quickly, but I think they're also the ones who would benefit the most from entity, generally.
Right? So I'm hoping that there… that's the bounce we took when we designed the protocol, right?
**Daniel Dyla (Dynatrace)** 09:11 But… from a strict reading of the spec, it is a breaking change. I guess that's all I'm saying, is like, is to just accept that.
**Josh Suereth** 09:19 Yep.
**Daniel Dyla (Dynatrace)** 09:21 Another possibility that I think we talked about was, only putting… Identifying attributes on resource attributes, and putting descriptive attributes somewhere else.
It might be a new bag of attributes called descriptive resource attributes. It might be entity signal only and not included in the resource at all. The implementation of that, I think, isn't important. The important part is put them somewhere else new.
And then… People who are reading resource attributes and do not upgrade to understand entities.
Miss out on those attributes.
**Josh Suereth** 10:09 Well, this is where I think there's some nuance, alright? So, here's my straw man, based on our discussion last time.
the default behavior in OpenTelemetry with entities is only identifying attributes make it on resource. So, when I… when I'm putting entities on resource, the identifying attributes go there, by default.
When I have opt-in configuration, which is how people get descriptive attributes on resource today.
if I have any kind of opt-in way of doing that, or, like, extra environment things that I provide, right?
That would be when I get descriptive attributes on resource. So, if I am opting in to using host IP address, like in Go, you know, I have to have an explicit host IP thing.
Then I get post IP address, I get the descriptive attributes and entities, but it's user choice. So, like, by default, we would try to make sure the SDK and the entity detectors and things are providing just the identifying attributes, and there's some configuration where I can say, grab these extra descriptive ones. So people who don't care.
Throw the descriptive in, but that's a choice they've made on top of the baseline behavior.
**Daniel Dyla (Dynatrace)** 11:19 Is that… Written down anywhere?
**Josh Suereth** 11:23 No, no, this is, this is what I knew, like, this was a shower thought.
That I didn't learn to write down, but based on our discussion last week, that's kind of what I'm thinking is a possible path forward. I think there's still some holes in it.
And I do… we do need to evaluate it against existing resource detectors to make sure we know what would be lost. Like, what does default look like today?
If you use the Java agent today, for example, there's a bunch of crap that goes into the resource, by default.
Process command line?
is the one that I find the most offensive, a little bit. That is, I think, by default, thrown on resource.
yeah, and that's one that could change, right, over time.
if we want to track a specific process, I think it's okay, but that's one that I think would be a descriptive attribute.
So, if we go with that strawman proposal I have, that would become a configuration flag that the agent would have to have in some fashion of, yes, include the process command line argument when you report resource.
So we're actually proposing changing the default behavior.
**Daniel Dyla (Dynatrace)** 12:35 Interesting. Okay. I… from that perspective, that would make… mutable attributes and opt-in configuration, which is a new configuration. I guess that is one way to address… this is only a breaking change if you opt into it.
making it not a breaking change, I guess. It requires user… Intervention, consent, whatever you want to call it.
I would… I would argue that there is a separate class of attributes then, as long as we're talking about defaults, and we can get into the specifics later. But there are attributes which are descriptive.
But… don't change.
The process command line is actually one of them. Like, it never changes. You only start the process once.
And I would argue not that those should be on by default, but that they should be candidates for on by default. Like, that may be one of the, You know, when we're making policies, we say, which… which entity attributes are on by default? Certainly, you need the identifying ones, which are immutable, and you must not have any which… are mutable and descriptive. But the immutable descriptive ones, I think we could allow those to be on by default, without any real problems.
I don't, you know, I can't think of any exact examples right now, but I think it's worth considering.
**Josh Suereth** 14:17 Yeah.
Yeah, I hear… basically, a host IP address would be one that we would probably want you to opt into.
But, like, process command line would be one that you could include. Yeah, that makes sense. Kubernetes status attributes, like the status of the thing, that's something that there's kind of discussions about, restart count is also one that I think should be descriptive and not included by default. That's another fun debate. I don't know if you were part of that semantic convention discussion.
Yeah So, Anyway, there's a few attributes that I think could fit in here. The other thing I think we're saying, too, with this straw man is when you mutate a resource to add a new identity, that's fine, because again, we're not breaking open telemetry, we're actually expanding capabilities. So, in the browser sig, if I attach session to resource.
It's actually a different resource, it's a different thing, and that's by design. So we're not breaking anything there, we're just allowing a use case that didn't happen before, and if you treat session A different than Session B, that's exactly what we want.
That's the whole point.
Right.
**Daniel Dyla (Dynatrace)** 15:36 Yeah.
I guess, I mean, treating… saying… saying it's a separate resource… is… I'm… I understand the argument that that is technically true, you can have it be a separate resource, but I think that you could use that argument for any resource mutations you wanted to do, always.
Sure.
Okay.
Yeah.
**Josh Suereth** 16:09 That gets to the other discussion we had last week about using instrumentation scope instead with entities.
But that's a different… I don't want to open that can of worms just yet, because I think we have to resolve this one first, yeah.
**Daniel Dyla (Dynatrace)** 16:21 It also gets to the multi-tenancy topic we talked about 2 weeks ago, 3 weeks ago, right? Where you have, instead of having multiple tracer providers, you have the tracer provider assigning telemetry to different resources.
**Josh Suereth** 16:37 Yeah.
**Daniel Dyla (Dynatrace)** 16:44 Okay.
**Josh Suereth** 16:49 I think there are a lot of descriptive attributes.
**Daniel Dyla (Dynatrace)** 16:54 that… people will… want, even ones that are mutable, like, things that people are currently today just throwing onto resource. I think there are a lot that people… will be… people will be annoyed if host IP is not included by default on the host entity detector.
**Josh Suereth** 17:16 Hmm.
I, I think you're right, yeah.
Yeah, that's why this was a straw man, that was a shower thought, it was something to think through, what to do there.
**Daniel Dyla (Dynatrace)** 17:27 Yeah.
**Josh Suereth** 17:27 I… you know, it might be that we just have to accept there will be some breakage here because of entities, but in practice, my thinking is, if I'm throwing host IP on.
I don't care about stable identity in this way that entities do, right?
or I'm in a system where host IP doesn't churn.
**Ted Young** 17:53 Just for clarity, and I'm sorry that I missed last week, I haven't been able to be, like, consistently here, but you're trying to preserve the idea that resource, the collection of resource, could be turned into, like, a fingerprint, and, like, essentially that is your identifier, is what's in resource, and we want to strip everything else out Yeah.
Somewhere else.
**Daniel Dyla (Dynatrace)** 18:15 Yeah, somebody, somebody brought up that in the specification, in a stable document, it says, resource is immutable.
**Ted Young** 18:27 I'm… it's hard not to kill something.
Right now.
If we've gone back to that as, like, the most important thing, a little bit.
**Josh Suereth** 18:37 No, it's more… we're going… like, I think… I think what we need to do, because… How do I want to phrase this? I think we're going to accept this breaking change. This is what I'm going to propose to the TC, and like, Tiger and I have talked about this a bit. In practice, like, this is what the specification says. In practice, people are not using it in this way today.
So, like, what's more important, that we keep our specification for braking, or we keep existing usage from braking? And I think the second's the important bit.
**Ted Young** 19:10 Second one, yes.
**Daniel Dyla (Dynatrace)** 19:11 I think, Ted, we're not talking about… I think nobody's saying we shouldn't do this. I think what we're talking about is how do we message this, and what mechanisms do we put in place to assuage users who are worried about it.
**Ted Young** 19:26 How do we break the spec, not how do we break… the users.
Right, like…
**Josh Suereth** 19:32 Yeah.
**Ted Young** 19:32 Like, we essentially made a mistake in this spec, which was we were like, all swans are white.
You know, and now we're trying to do some tricky stuff here.
to solve some of this, right? We said all swans are white, mainly resources are immutable, they don't change. The other thing we said is, like, resources are identifiable, and then proceeded to create a ton of resources that were not, and put them in there. You know, also in our spec, in, like, our semantic conventions, right?
Yep. So… that's the reality we live in, is right now everyone gets all of those resources, and it's, like, very valuable data, but it's definitely not, as a collection, like, an identifier. And that's, like, the reality that, like, our users have been living with, basically, since the beginning.
**Josh Suereth** 20:19 Right, I think… To all of these points is… We're going to have to break this part of the spec and communicate it.
**Ted Young** 20:27 Okay.
**Josh Suereth** 20:28 Do we need controls to… for people who depended on that portion of the spec?
You know, the… again, the one thing… the one thing, if you're not aware of this, I think… I think it's here. Let me find OpAmp… Specification, if you haven't read through this one, I don't know if I can find it quickly.
But… Yeah, it's just in the proto, isn't it?
Oh, here's the specification.
**Daniel Dyla (Dynatrace)** 21:00 Are you looking for where it says that it uses resource to identify the…
**Josh Suereth** 21:06 Yeah.
**Daniel Dyla (Dynatrace)** 21:08 Ginter, whatever they call it.
**Ted Young** 21:10 Yeah.
**Josh Suereth** 21:11 Yep, so agent-identifying attributes are attributes that identify the agent.
Now, it does actually split into identifying and non-identifying, so honestly, that fits… entities so well.
**Daniel Dyla (Dynatrace)** 21:26 Right, but they called out resource as identifying.
**Josh Suereth** 21:30 Which I think we can also fix.
**Daniel Dyla (Dynatrace)** 21:35 This isn't stable yet, I don't think it's even… I think it's all beta.
**Josh Suereth** 21:39 Yeah, actually, look at this, man. They do call out some resource attributes are not identifying, and they literally were picky and choosy, so it's probably… it actually might be in better shape. I am, I just knew that this existed. I didn't… I should have looked at the details a bit more.
Hey.
**Ted Young** 21:56 So in practice, we've looked around historically to be like, who is actually, like, making a fingerprint out of these resources? Like… Because it's not… it's not that, like, individual users would be doing something here, it's more like the database that people are using, or whatever. Is anybody doing that? And I think it came back that, ironically, we were doing that somewhere in the collector.
**Josh Suereth** 22:21 We are doing that in the collector, and everyone else seems to do this kind of shenanigan, where they're saying, here's the resource attributes that I care about for identity, and everything else I don't.
It's…
**Ted Young** 22:33 Right, because in practice… That's what we do. Yeah, in practice, every vendor, database, whatever, has a concept of identity, right? Like, every analysis tool is like, identity in this world is these 8 things, no matter where your data came from. And then they kind of map whatever those eight things are to… you know, what they can get out of that data source. Like, in practice, yes, everyone already has, like, a list somewhere separate that they keep about which keys… They count as identifying.
**Josh Suereth** 23:04 Right, and now, with entities, we're being explicit, so we can just go to those places and say, hey, instead of your magical list, use this instead, and we give you the set of identifying keys.
Cool.
So I still think we need to communicate this as a breaking specification change, but again, when I think of breaking change, generally, I think of, like, users… users feeling the breakage. Like, you know, if a tree falls in the forest and no one's there to hear it.
did it… did it happen, kind of a thing. But it's more, if I make a change that no one notices, it's not breaking. If I make a change, people notice, it's breaking. So even if I fix a bug.
if it destroys, like, a whole bunch of people using OpenTelemetry, that's a breaking change.
and needs to be communicated as such. So, in this case, I think we have to communicate it as such, and communicate the rationale that we think most people aren't, depending on this part of the spec.
We can call out a bunch of usages where it's obvious… this is a perfect example. Our own specification does not rely on that part of the OpenTelemetry specification, because it can't, right? So I think we can actually call that out as, like, the rationale, but to your point, Daniel, let's just communicate this broadly and widely.
**Daniel Dyla (Dynatrace)** 24:21 Yeah.
**Josh Suereth** 24:22 Lend.
**Daniel Dyla (Dynatrace)** 24:23 I can think of at least one other place where it's definitely used. As far as I know, the, the load balancing The collector load balancing uses resource to make sure that telemetry from, you know, from this resource always goes to the same backend.
**Josh Suereth** 24:43 Is that an extension?
**Daniel Dyla (Dynatrace)** 24:46 No, I think it's a processor, or…
**Dmitrii Anoshin** 24:49 It must be a connector.
**Daniel Dyla (Dynatrace)** 24:51 It's a, yeah, connector, okay.
**Josh Suereth** 24:53 It's a connector. I knew it was one of the new fancy things.
**Daniel Dyla (Dynatrace)** 24:57 As far as I know, it uses resource as its, like, identity key, which makes sense, it's the only thing that you really can use.
**Josh Suereth** 25:04 Is that the routing one, or is it…
**Dmitrii Anoshin** 25:06 The routing is the load balancer?
That's what you mean, right, Daniel?
**Daniel Dyla (Dynatrace)** 25:13 No, there's a low, there's a separate component.
**Josh Suereth** 25:20 I know, I know what you're talking about, Daniel.
**Daniel Dyla (Dynatrace)** 25:24 There's a load balancing exporter.
**Josh Suereth** 25:27 Exporter, that's right. Okay.
**Daniel Dyla (Dynatrace)** 25:28 an exporter.
**Josh Suereth** 25:30 Yeah, where was that?
**Daniel Dyla (Dynatrace)** 25:31 And it, I guess, exports to… you would… Probably most often.
to a connector that then goes to a different pipeline that then would go to an OTLP exporter. I'm not entirely sure how the configuration there works, but yeah, it uses… the resource.
**Josh Suereth** 25:50 Well, it… yeah, the resource is an option.
**Daniel Dyla (Dynatrace)** 25:53 The, yeah, the option, yeah, options for routing key.
**Josh Suereth** 25:57 Yeah.
It also… it's weird that it… where's… where's res… oh, here's resource. Can only be used for metrics. Interesting.
That's weird, and then service is used for spans and metrics.
but not… resources and used for spans. Attributes would be the attributes of the span, I guess?
**Daniel Dyla (Dynatrace)** 26:23 I assume so?
I guess we don't have to specifically probably worry about the details of this, other than to know that it exists for this conversation.
**Josh Suereth** 26:37 Yeah, mostly what I want to see, because if you look here, yeah, when they say service is used, it uses.
**Daniel Dyla (Dynatrace)** 26:42 I'm sure it's the service name, yeah.
**Josh Suereth** 26:44 Yeah, exactly. So it's the same kind of shenanigans.
That we see with resource. And using resource for metrics makes sense. We know that metrics and identity, it's, like, really correlated, but the fact it's only used for metrics also is in line with what I would expect. Okay, this is cool.
Good call out.
**Daniel Dyla (Dynatrace)** 27:03 Yeah, it's, it's most important because if you're using this, with anything that requires like, the same trace to be on the… on the same backend instance. Like, if you're doing tail sampling or anything like that, you can't use a resource, but it looks like it's not even possible, so…
**Josh Suereth** 27:24 Yeah.
Well… For routing key, it looks.
**Daniel Dyla (Dynatrace)** 27:28 clicking.
**Josh Suereth** 27:29 Can you use more than one?
**Daniel Dyla (Dynatrace)** 27:31 I'm just curious.
**Josh Suereth** 27:38 Oh yeah, what is stream ID? That's the last thing to check out.
What do they include? Ross users, data point, the unique cache of all attributes, plus identifying attributes of its resource scope, and metric data. Yeah, okay.
**Daniel Dyla (Dynatrace)** 27:50 Wow.
**Josh Suereth** 27:52 Well, that one… that one… that one also makes sense. That's, Internally.
**Daniel Dyla (Dynatrace)** 27:56 Because with…
**Josh Suereth** 27:57 We do this for…
**Daniel Dyla (Dynatrace)** 27:58 That's essentially what the metric stream, you know, that's how you identify a stream of metrics. If you send, you know, deltas, like, add 3 to this metric, that's what you need.
**Josh Suereth** 28:08 Yeah, yeah, like I said, internally, we do that to try to shard metrics into various storage locations and stuff, yeah.
So that makes sense. Okay, cool. Not that… well, anyway, this all makes sense. So this…
**Daniel Dyla (Dynatrace)** 28:22 Would likely need to be updated to use only… Identifying attributes from the resource, which…
**Josh Suereth** 28:31 Yeah.
**Daniel Dyla (Dynatrace)** 28:32 Is, you know, that's what you want anyway in that case.
**Josh Suereth** 28:39 update, and that was the routing exporter, right? Routing exporter, collector… to have…
**Dmitrii Anoshin** 28:46 Load balancing exporting.
**Josh Suereth** 28:51 E, update.
Upanish specification.
directly interact with entities. Medicare braking. Spec change.
Widely. I'll… I'll discuss with the spec maintainers about, like, what… how we want to communicate that breaking change, and how we want to handle that. So…
**Daniel Dyla (Dynatrace)** 29:19 Yep, there's one more… I think in the Prometheus, exporter specification, we say that resource… should just be added as attributes. That should be most likely updated to only take identifying attributes, right?
**Josh Suereth** 29:39 I think that might already be the case. I was just talking to David today about Prometheus status, Let's take a quick gander… that would be…
**Daniel Dyla (Dynatrace)** 29:48 How would that be the case? Because right now, we don't have any way to mark identifying and non-identifying.
**Josh Suereth** 29:55 So today, it specifically, I think, relies on service attributes, service instance ID.
**Daniel Dyla (Dynatrace)** 30:02 Oh, it doesn't take the full resource?
**Josh Suereth** 30:04 It… no, I don't…
**Daniel Dyla (Dynatrace)** 30:06 And so, I thought, I thought it…
**Josh Suereth** 30:07 Stop.
Yeah, I can hear.
**Daniel Dyla (Dynatrace)** 30:09 wrong, I guess.
**Josh Suereth** 30:10 What's great for Prometheus endpoints, resource attributes must be added to this great metric to distinguish them from other Prometheus endpoints, in particular service name, server instance today, need to ensure Prometheus Explorer can disambiguate. What happens is all the resource attributes get added to a target info metric, and these are kind of, like, the key things that you use.
to create target info. So, like, there ends up being two metrics that are written, one with the metric time series and service name, service instance ID, and the other one with all the resource labels. And if you want the resource labels, you join the two.
**Daniel Dyla (Dynatrace)** 30:42 Got it, okay.
**Josh Suereth** 30:44 Yeah.
Oh.
**Daniel Dyla (Dynatrace)** 30:46 And should that infometric have… Mutable resources or not?
Or is it just those 3?
**Josh Suereth** 30:54 The infometric would have actually descriptive attributes in it as well, yeah.
**Daniel Dyla (Dynatrace)** 31:00 Yeah, okay.
**Josh Suereth** 31:00 Because the idea is you join it. I think there's a, there was a proposal from, I think, Arthur or David from the Prometheus group.
around entities and, resource attributes, where we actually might end up with, instead of a target underscore info metric, there would be an entity underscore info metric, but entity info would be, like, entity name info, right? So it'd be, like, Kate's… Kate's pod info, host info.
And that would have the identifying attribute, descriptive ones, and you can keep track of descriptive attributes over time. So if you wanted to look for IP address changes, you could see that in a time series. If you wanted to check status changes on, like, deployments, like, pod flapping, that kind of stuff, that's part of, like… anyway.
Jose, question on that. I don't…
**Daniel Dyla (Dynatrace)** 31:51 I'm late for that browser sig. There is one more quick one I want to mention before I leave. I believe right now… Resource is… part of metric identity. That'll have to be updated to be only the identifying attributes, but I think that's obvious enough. Alright, I gotta go.
That actually motivated this SIG, by the way. Yeah.
**Josh Suereth** 32:17 Started driving it, yeah.
**Daniel Dyla (Dynatrace)** 32:20 Awesome. Alright, see you next week.
**Josh Suereth** 32:21 See ya, see you guys next week.
Real quick, if folks have time, the updated project status and trackers, just wanted to share, we… every week I want to make sure we're doing this, we're still marking ourselves as on track.
And the target date for a delivery of stabilizing our current, parts of the spec and getting SDKs to kind of kick off with prototypes and things is actually the end of the year.
25, 12, 21. So, I don't think we have enough time to talk about whether we update the status, but just wanted to call out I do want to update this every meeting. For now, we'll leave it as on track. I think we have some… still things to progress.
please take a look at the in-progress and, potential things to do, pick up tasks if you're able, and let's keep making progress. That target delivery date, by the way, is Phase 1.
So, getting out the entity manager OTEP, getting out entity manager specification, and making sure that we can land things in the spec.
Cool.
Thanks, everybody.
**Dmitrii Anoshin** 33:27 Thank you.
