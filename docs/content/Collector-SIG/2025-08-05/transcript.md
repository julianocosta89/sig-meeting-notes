SIG: Collector SIG
Date: 2025-08-05
Duration: 36 minutes
============================================================

## Zoom Recording Transcript

**Andrew Wilkins @ Elastic Observability** 01:46 Antoine.
**Antoine Toulme** 01:47 Hello!
Good!
Hmm!
Hello!
**Dmitrii Anoshin** 03:02 That works.
**Andrew Wilkins @ Elastic Observability** 03:03 Hey dimitri.
**Antoine Toulme** 04:18 Oh, no, because they just upgraded our slack and they turned on AI in slack.
It's happening, Andrew. Do you want to start.
**Andrew Wilkins @ Elastic Observability** 04:34 Yep.
okay, so I've been working on some changes related to service telemetry. There's a long standing issue to to make it possible to override the telemetry providers.
This is important for us to be able to inject.
**Antoine Toulme** 04:48 Additional dimensions into metrics, that.
**Andrew Wilkins @ Elastic Observability** 04:52 That are produced from internal telemetry.
just fyi. The the plan I have in mind is and I'm it's already underway is to split the service telemetry package into 2. So there'll be one for the implementation which currently lives in service telemetry. Which is using hotel Conf and using the the standard SDK, as you would probably expect. And then there will be a separate package for the interface, which is only exposing the Ap. The open telemetry go Api go ahead.
**Antoine Toulme** 05:31 That make? I mean, sure. Yeah, makes sense.
**Andrew Wilkins @ Elastic Observability** 05:33 Makes sense so far. So I guess my question was, do either of if either of you care do you have any suggestions on the naming. My my intention was to call the the Interface Package Service telemetry as it is today, and then a new package service telemetry, or till Conf telemetry. But my one, I guess open question for me is whether or not it even the interface belongs under the service package.
because it it probably should be used by OP. Amp. Supervisor as well. It's not currently oh, sorry OP. Amp. Supervisor kind of does its own telemetry but it uses the config struct.
**Antoine Toulme** 06:16 So I'm just thinking, maybe it doesn't really belong under service.
**Andrew Wilkins @ Elastic Observability** 06:20 So it can be more reusable.
**Dmitrii Anoshin** 06:25 One question. You said you wanted to have to be able to add additional dimensions. Are those dimensions supposed to be dynamic? Because, oh, I see, because already we still you can add, like any static dimensions, too.
**Andrew Wilkins @ Elastic Observability** 06:41 Yeah, yeah. Yeah. I'm aware that we can inject them through config. But we want dynamic attributes based on basically a tenant id that we want to attach to request through port, and so on.
**Dmitrii Anoshin** 06:53 So is it can that be done through the pipeline in in one of the processors.
**Andrew Wilkins @ Elastic Observability** 07:05 no, not at the moment. So I mean, not. As far as I'm aware. We looked into various options. Couldn't come up with any any option that would work. So for one thing, we would need to be able to inject it in very early on so like for the Hotel Http and Hotel Grpc. Metrics.
We want to add dimensions to those.
We could hypothetically extract some information from the headers in Middleware.
but there was no way to no way to add attributes dynamically in those instrumentations.
**Dmitrii Anoshin** 07:46 Yeah, okay, I understand. I was thinking that if you can. If you send the internal telemetry through another pipeline like, for example, you send the telemetry to a Tlp. Receiver, and then you have another pipeline. If you don't do that. In that case.
**Andrew Wilkins @ Elastic Observability** 07:59 I see. No, no, we're not doing that even if we could.
I don't know if we would, because we may have thousands of these, and that would imply having thousands of pipelines. If I understand your suggestion.
**Dmitrii Anoshin** 08:14 Yeah, but you can have another processor that would do it dynamically. Somehow, like custom process.
**Andrew Wilkins @ Elastic Observability** 08:22 Yes.
but I think we would have the same problem, because we would need to still convey that metadata somehow to the other pipeline. Right?
**Dmitrii Anoshin** 08:32 Yeah, yeah, you need to send that metadata, and there is no, there is no like.
But I mean oh, by metadata, you mean, probably client request, or something.
**Andrew Wilkins @ Elastic Observability** 08:45 Yes, yeah, exactly. Yeah.
Yeah. So the idea is would override the meter provider, and then ex when a when a metric is and when the add method is called on one of the metrics that, like adding a data point measurement.
we would extract some some additional attributes from the context object.
**Dmitrii Anoshin** 09:14 Makes sense. Yeah, ensure to prioritize this and make it before 1.0. Because this goes against 1 point. Oh, I mean it. That doesn't go against 1.0. But if a service telemetry is 1 point, oh, it will be much more complicated to introduce that change.
**Andrew Wilkins @ Elastic Observability** 09:32 Yeah, I I think the service package was exempt from one dot. O Oh, really, I think so. I'm not.
You're right. You're right. That's my recollection as well.
**Antoine Toulme** 09:45 That means. So this is probably just dumb advice, but it looks like the service package is kind of the it's kind of a catch-all of a number of concerns.
If you were to do anything such as finding interfaces or things like that.
you might really be well served by kind of separating your concerns into a new package outside of service.
so so that you can also mature it on its own. And so people don't have to bring in the whole service package like you mentioned. Opm. Supervisor could be a good candidate for that if it works right. So I think you're on the money. You just move your stuff out into a separate package and then, make it clean. Do an implementation service by default. Maybe not even a separate package something.
And then the yeah.
**Andrew Wilkins @ Elastic Observability** 10:36 Okay. Oh, how about what I'll I'll do is I'll what I'll do is I'll continue with what I'm doing in the service package so keep it there for now. But I'll open an issue to propose moving it out to a new one.
and then we can continue the discussion there.
**Antoine Toulme** 10:51 Maybe start with just that.
**Andrew Wilkins @ Elastic Observability** 10:54 Are you easy, new one?
**Antoine Toulme** 10:58 Just like just You said that you wanted to split into. Have Api somewhere this the other side from experience. Anything in core. Just want to do one thing in your Pr.
**Andrew Wilkins @ Elastic Observability** 11:10 Yep. Yep.
**Antoine Toulme** 11:12 But you know.
**Andrew Wilkins @ Elastic Observability** 11:13 I've learned that.
**Antoine Toulme** 11:14 Yes, cool.
**Andrew Wilkins @ Elastic Observability** 11:17 Cool. Thank you.
**Antoine Toulme** 11:19 I'll just go over something here. So okay. So I'm a little worried about something, is I? It's not like the 5th issue that I write about some component that is shipping in country, but some other distribution, and just not actually documenting it.
I'm thinking we should have like a Ci. For this.
but I don't know what that would look like, and I'm open to suggestion. Or maybe I'm overthinking this. But the point is, if you go to the log data processor today and you open it with me. It says it's not being shipped with any distribution. That's just not true. And in some way I think it hinders adoption, and we want to make sure that people try stuff out, and and we want to make it easy for them to find it, and we're just doing ourselves a big disservice.
So you tell me what you what you think I should do.
or should I? Just, you know. Keep keep fighting issues one by one till the end of times.
**Dmitrii Anoshin** 12:20 Yeah, I think we have this idea of having, like some checks against all of the components and checks, and which would be our defined in the metadata yaml, or some exemption from that checks will be defined in metadata Yaml.
I believe this. This is just one of the checks. We potentially can synchronize the data from from releaser repo to this one. We might actually want to have source of truth for that section.
Having from the releaser strip, instead of defining it manually as well, or at least at least some ci check to synchronize.
**Antoine Toulme** 13:07 Yeah, is there? Are you aware of any open issue or work that's going into this? Or is it just so.
**Dmitrii Anoshin** 13:14 I think we discussed that in general idea, but I don't remember we have anything.
**Antoine Toulme** 13:19 Okay.
**Dmitrii Anoshin** 13:22 Start with an issue, and then we can look for volunteers to work on that.
**Antoine Toulme** 13:27 Alright. I'll find an issue about this. It's not. It's not huge, but it's just annoying.
I think I caught a few I just stopped fixing it myself because it got it's getting to me.
I don't wanna do this all the time.
**Dmitrii Anoshin** 13:43 Makes sense.
**Andrew Wilkins @ Elastic Observability** 13:45 So the only thing I have to add is that if we make the I I think it sounds like a good idea to automate it. If we made the releases repo the source of truth, then if someone updates, that's gonna break the contribute repo, if if it's out of sync. So maybe we should automate updating the metadata Yaml as well.
And then.
**Antoine Toulme** 14:06 You'd have to rely on maintainers to to do that.
Yeah. So in the past, what I have done is, I have a We have a check in Rci that checks that. We are building a report for what goes in country, and Kate, as and a few others.
I don't think we're actually completing that. And if you go in the reports distributions, you go to contribute ammo.
We have a list of what ships in what and I I mean, I don't know. This is, I think this is actually a central place where you could sync everything.
Maybe we need to stop doing that instead.
yeah, I'm I'm not sure.
There, you just calling for ideas. I can open an issue, and we can take it from there.
Okay, so I have another one. I was just looking at this because I don't know. I don't. Wanna I don't wanna do my day job today. Something like that don't tell anybody component status. Has a an issue up, and it's like there's there's a number of trucks that could be moved out to other bases that would make more sense. There are 2 trucks. One of them is the the watcher, struct and one of them is the instance Id.
the watch restructure. I was going to propose that we move it under extension capabilities.
Bear in mind, this is not urgent. I'm just bringing that up because you're here, and it's nice to have a meeting. So let's talk right. But if you think this is not good use our time, let me know. So, under extension capabilities, I think we could move watcher, because that would be a nice addition to that package which is supposed to capture what extension.
what extensions can do? Right? So if you implement that type, then we do some something like that. I don't think it needs to be in its own package. I think it should be part of that package instance. Id remains find this to be a bit of a it's a bit complex for what it does.
So instance, Id has component id a kind and pipeline ids, which is the agglomeration of where it's used just to identify where it's used.
and it's supposed to be used as a map key in a graph for status reporting.
I wonder if it's if it's sipping a little bit, some of it like. The fact that it's used as a key in a map is kind of irrelevant to the discussion, and I don't know that it needs to be something that people see in the Api Some of that. It's kind of not really getting that much love, so I can remove the getters like component id getter and kind getter. We can just expose the the fields instead. There's no point.
I just wonder what to do with the.
The. The only method that really makes sense is all pipelines id or pipeline ids, because it allows you to traverse the pipelines on which the instance is present that's only used in one place in contrib.
So I don't know I so doing. The the sense that this this truck is a little wheel.
**Dmitrii Anoshin** 18:11 Where is being used in country.
**Antoine Toulme** 18:13 It's used in the status aggregator in one place.
package that is aggregator dot go. Where do you iterate to record the status.
And I think it's to update the status of the pipelines.
So you get an event from some instance that's running right of a component.
and you find out that it's you want to see which pipelines it's on, so you can report that.
And so the the choice that he made was that you're going to have one event per component, for instance, right? Instead of having many different events, one per pipeline, for example, which maybe is fine.
and so you can notify subscribers for particular pipeline.
I'm betting. This is then used in health check. V. 2.
This is complicated. But I don't know. Something's wrong with it.
So, okay, so let me look at this another way. I think what sure could move right now to extension capabilities and be deprecated and removed in one version, and we don't have to move. Instance Id right away.
But eventually we need to find it a better home, or at least call it something that makes sense, because, instance Id.
it's like the worst like it's a really weird name. In the 1st place, right.
**Dmitrii Anoshin** 19:56 Yep.
**Antoine Toulme** 19:58 I'm not. I'm not fond of this whole thing. It's sending vibes of like something is off.
**Dmitrii Anoshin** 20:08 Yeah.
**Antoine Toulme** 20:09 Another thing I could do here is we could also inline like the instance, Id is kind of a internal truck. Maybe we don't care. Maybe we could just in line that in the function of the watcher, instead of having source being the instance Id, we could just have source kind of component name of component, all the pipelines its own in the event.
and we don't need to expose instance Id at all to the external, to the to the surface.
I like that.
**Dmitrii Anoshin** 20:46 And he if you can.
I do idea in the comment and and that issue. But I'm not up to speed to that yet. So.
**Antoine Toulme** 20:57 Yeah, I'm sorry. This this is weird.
okay, that's fine. It's okay. If you don't know.
Okay.
are we still moving components to stable? Or is that kind of on pause waiting for config, optional.
**Dmitrii Anoshin** 21:22 I don't remember. I believe we are config optional waiting for them.
**Antoine Toulme** 21:30 Okay.
**Dmitrii Anoshin** 21:31 Is there a dependency from component to config optional.
**Antoine Toulme** 21:36 That's a good question.
I don't know let me.
So no, I mean I don't know anything let me see, component is stable.
That's your answer.
It's it's it's more like a so config Http configure. PC, they might need to have some level of a new level. Field.
So the config optional came to play. Because you need those 2. If you want to make a Tlp exporter, a Tlp receiver stable right?
So there's this, this big game of this graph of dependencies, where you can see that we have so many ways that we can tie yourself up. I just opened a a Pr. To make pipeline stable, because I don't know everything is ready to go in there. I don't have any reason not to think so.
so I have a Pr. Up for that, and I'd love to have maybe a conversation about it. But I'll put it in the in the dark as an additional item.
Sorry, Andrew, let's go back to Andrew. He's got something to talk about.
**Andrew Wilkins @ Elastic Observability** 22:56 Yeah, no worries. I don't have anything to add on that topic is, I don't know all those things. I guess I've had this issue open for quite a while. 3, 9, 1, 9, 9. Proposing a new component or partitioning the idea here is so it's quite closely related to the batching changes that have been going in recent recently to batch by client metadata, or some kind of partition in the Kafka exporter. We have kind of bespoke partitioning where you can partition by trace. Id. And I think, a resource attribute. I recall correctly this will be relevant to other other exporters and potentially other components as well. But they don't like we don't have a generic way of doing it. So my proposal here is to introduce a new component that will inspect data in a batch. So you know, P. Log logs, P metric metrics, and so on. Depending. And and we'll use ottl, and then depending on the ottl context, it will sort of go to the right depth.
extract some kind of some expression. So when I say depth, I mean, could be scope level could be resource level could be data point whatever depending on what you're accessing.
And then it'll evaluate an expression so ottl value and then use that as the partition.
the partition key, I mean, and then, finally, it will group all of the the results by that partition key.
Finally, the partition key would be added as client metadata. It's a kind of a misnomer, but it's more request, metadata, and then that you would be able to send that to a batcher and then batch by that request Metadata
**Antoine Toulme** 24:56 Okay.
**Andrew Wilkins @ Elastic Observability** 24:57 Does that make sense? But so far.
**Dmitrii Anoshin** 24:59 That that all makes sense. We have this thing.
that plan in for the Batcher exporter, Batcher, to provide this kind of an interface. So you you'd not just specify one particular metadata key, but that you currently have in the Batch processor. But you can do complex ottl batching kind of request.
So if we if you can look into that Cindy is working on that. I believe I'm aware of the partitioner interface in export a voucher.
So we would need to bring your configuration interface. So like, 1st of all, that's gonna be optional. Not all of the exporters have to implement that. But we would need that like, let's say, example implementation in Otlp exporter.
And this is where your interface, your configuration interface will come and play, and we can maybe expose that in exporter helper as well. So if other exporters want to have something like that, they would just take that whole helper thing and introduce that.
So you would have like complex and logic to any complex logic to have partition and key. But I don't think we consider it how this partition and key will be propagated. So this is part of your another question. You want that partition key to somehow be added to the payload right.
**Andrew Wilkins @ Elastic Observability** 26:39 Not to the payload, but to the client metadata. Yeah, I mean again, it's a bit of a misnomer. It's more like request. Metadata.
**Dmitrii Anoshin** 26:48 I understand, understand.
**Andrew Wilkins @ Elastic Observability** 26:49 Awesome. 3.
**Dmitrii Anoshin** 26:49 That definitely makes sense. So I believe this play play well with the original proposal. Original proposal tells you, hey? You can configure in the configuration interface, how you would split the batches, how you partition, whether it be by resource, attribute, whether it be by metadata keys. Wherever you can combine, you can use anything, but it doesn't tell anything about how that partition and key will be used after after creating the batch, so I believe it it can. It makes sense just to put it in the context essentially. And we can have another like configuration line. How it will be called or I don't know it doesn't matter, so I believe that functionality will fulfill your needs.
Do you need it to be as a separate processor once we, if we have that.
**Andrew Wilkins @ Elastic Observability** 27:46 It doesn't have to be.
Okay. So 1 1 thing I've added in the description of this issue is, I believe if we had this, we could replace a couple of other processes. So there's a group by trace and group by, I think it's called this partitioning could do that as well.
**Dmitrii Anoshin** 28:05 All of them can be replaced by yeah.
**Andrew Wilkins @ Elastic Observability** 28:08 On the other hand, if we did what Josh Mcdonald proposes, and
**Dmitrii Anoshin** 28:16 No, that's my.
**Andrew Wilkins @ Elastic Observability** 28:17 Batch, processor.
**Dmitrii Anoshin** 28:18 That's my question. Why do you need that? So I understand. Know what he wants to do. He wants to adopt interface in the in the Batch processor. But I'm I'm just curious. Do you need that.
**Andrew Wilkins @ Elastic Observability** 28:31 Do I personally need it? No, I don't personally need it.
**Dmitrii Anoshin** 28:34 Once we have the implementation that I that I just explained, and the export will help you, would you wouldn't need that also right?
**Andrew Wilkins @ Elastic Observability** 28:44 Not that I can think of at the moment. I don't think so. Yeah, because.
**Dmitrii Anoshin** 28:48 We're pretty much trying to solve a similar issue, like the idea is to provide a way to batch data and send them with different like metadata.
**Andrew Wilkins @ Elastic Observability** 28:59 Yep.
**Dmitrii Anoshin** 29:00 So it's pretty much the same use case.
**Andrew Wilkins @ Elastic Observability** 29:02 Yeah. Okay. Only question I have then is, how would you configure so different partitioner, though, because at the moment the partitioner Api is oh, entirely programmatic. There's no way to inject.
**Dmitrii Anoshin** 29:16 That's what I said. We have it 1st programmatic, and then we have a like implementation for Otlp. With the configuration it can be. We need to come up with with that configuration, and I believe what you have in your issue is pretty good one. I haven't looked deeply, but you can you can suggest that as a as a like.
let's say, ideal, like whatever generic solution that can be applied to open telemetry or Tlp exporter.
So that programmatic interface is for custom exporters. They would programmatically set how they partition. But we don't have that need in otop Otlp. Exporter is generic. So we would, we would have to provide some kind of user user configuration interface for the Otlp exporter, anyway. Right?
So. And I think and I think it's important to give like a lot of flexibility, not just picking one metadata key from from the context.
**Andrew Wilkins @ Elastic Observability** 30:17 Yeah, agreed.
Okay. Alright, I'll have a think about that. Maybe it could exist as an extension which provides an like an implementation of that partitioner, so rather than it being of its own standalone processor, it just provides an implementation of the partitioner that can be used with the exporter helper.
Maybe. No, maybe we don't. Don't even need the export. Maybe we have generic implementation right in the exporter helper that would expose configuration, interface and utilp.
**Dmitrii Anoshin** 30:50 And it will be fully Ottp driven. We just need to provide some like. It can be a bit different schema, because, like it's, it has to have particular needs for like specifying one key like not specifying one key but getting one. Let's say partitioner identifier. And that identifier somehow needs to be like needs to be passed down the down to the export request.
But my idea is that implementation can live in the exporter helper with the configuration interface based on language.
**Andrew Wilkins @ Elastic Observability** 31:32 Okay, so. But the problem then, is, Ojtl is in contrib.
**Dmitrii Anoshin** 31:37 Right? Right? Right? Yeah, you're right. You're right. In that case we cannot depend. Then what can we do?
Probably implementation can leave. In that case I don't know. As you said, maybe extension.
**Andrew Wilkins @ Elastic Observability** 31:57 So the other thing we could do, which is sort of what I had in mind is that we could have a a default implementation of the partitioner in core, which is just based on client metadata. So you specify some metadata keys similar to what you were doing in the Batcher. The Batch processor. And then we have a new component, like like I was proposing originally.
**Dmitrii Anoshin** 32:22 And okay, I see what you mean. So we we for now we keep exportable helper, simple.
**Andrew Wilkins @ Elastic Observability** 32:30 Yeah.
**Dmitrii Anoshin** 32:32 That's also a potential solution. I'm I'm thinking of performance implications.
So let let's say we want to have pipeline, which doesn't block right and doesn't introduce any asynchronous behavior.
Would you be able to batch? No, you wouldn't be so you, your your partition and processor, would only can split split batches.
**Andrew Wilkins @ Elastic Observability** 33:08 Yeah, it would split, and I think it would need to concurrently export or like, send to the next consumer.
**Dmitrii Anoshin** 33:15 Concurrently export and only return success when all of the concurrent exports succeed.
Yeah, the thing is, I believe it's still gonna be more performant from if it's implemented in exporter helper. But, as you said, it brings dependence on Otto, which is not ideal.
I mean, my my idea is that it would require many. If you have queue configured, it would require more queue ports and more queue queue retrievals.
**Andrew Wilkins @ Elastic Observability** 34:01 And if we have that implementation in in.
**Dmitrii Anoshin** 34:04 Exporter helper. It would be one queue put and one queue retrieval.
I'm not. I'm not saying that that is expensive, but it'll likely be less latency for the incoming request from the outside to the collector.
**Andrew Wilkins @ Elastic Observability** 34:25 Yeah, that's what you mean.
Yeah. Actually, when I wrote this, I had in mind that the there were going to be multiple queues, one per partition, but I think it happens after it's dequeed. Is that right?
**Dmitrii Anoshin** 34:38 Multiple queues. We don't have multiple queues. We still.
**Andrew Wilkins @ Elastic Observability** 34:41 No, yeah. I thought they were instanced per partition.
**Dmitrii Anoshin** 34:45 We, we still considering that option, but it it was like never implemented. Yet we.
**Andrew Wilkins @ Elastic Observability** 34:51 Okay.
**Dmitrii Anoshin** 34:53 Yeah, but I I we can maybe go with this approach with the partition first, st and then then we'll see, maybe, which deal would go to core or with Trigger something else.
I'll also think about it. But I I definitely like, I agree that, like the the goal itself, makes sense. And we need to have solution for that.
**Andrew Wilkins @ Elastic Observability** 35:22 Well, if you have a think about it, if you think it makes sense to proceed, would you mind sponsoring, or do I need to find someone else.
**Dmitrii Anoshin** 35:30 No, you let's let's work on on that. I'll be happy to sponsor if we.
assuming that we don't have any other alternative for the short term which I cannot think of at this point. Given the Ottl restrictions.
Well, then, yeah, give like, maybe I don't know.
**Andrew Wilkins @ Elastic Observability** 35:54 Do you want? Do you want to start working on this? This?
It's not. It's not urgent. So you just have a think about it, and if you, if you think it's fine, then.
**Dmitrii Anoshin** 36:03 By the next week I'll I'll let you know on Monday. I'll I'll sponsor it or provide an alternative suggestion.
**Andrew Wilkins @ Elastic Observability** 36:11 Perfect. Thank you.
**Dmitrii Anoshin** 36:12 Thank you.
**Antoine Toulme** 36:19 Right?
Okay. I think we're done anything else.
Alright, have a good day, folks.
**Dmitrii Anoshin** 36:36 Thanks. See you later.
