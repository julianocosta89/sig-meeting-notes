SIG: Arrow SIG
Date: 2025-08-07
Duration: 64 minutes
============================================================

## Zoom Recording Transcript

Laurent Quérel 00:00:48 And there's.
Chris Hain 00:00:52 Morning.
Laurent Quérel 00:02:19 That's an issue to share one. Soon I'm coming log out and log in again.
Laurent Quérel 00:03:07 Okay.
Hi, everyone.
I guess Joshua will join us soon.
The stump.
I can start to share my screen in between.
Okay, soon.
If you have any item to add into the agenda, don't hesitate.
Okay? And we are okay.
Pleasure.
jmacdonald 00:04:39 Oh!
Laurent Quérel 00:04:41 Hello! I was just sharing my screen and asking people to to feed the agenda.
jmacdonald 00:04:52 Sounds good. Let me pull it up.
Last week. You had recommended that we do a triage.
Laurent Quérel 00:05:16 Yeah.
jmacdonald 00:05:17 My work.
Laurent Quérel 00:05:17 Indeed, and to simplify it, I think the these 3 h. What I did is creating a milestone in detail.
Label Demo, September 2025, where I'm trying to group all the task, I think, related to this milestone.
So I think what we can do this morning is maybe talk about what people are doing or what they they, they think that they will achieve during the next week.
So we are sure that there is no duplicated work.
It doesn't good.
jmacdonald 00:06:16 Yeah, I would say, you have a better picture of this than I do at the moment. And I. I came to to the meeting to tell you that after our last talk I I am interested in picking up the work I've been doing on rate limiting since. It seems pretty important to the whole effort across. Go and rust and until now I've been doing a lot of design work and and looking at the go code, but but I think it's time for me to dive into the otap and I will be that would be my agenda once we come up with something higher priority.
Laurent Quérel 00:06:49 So in that case, rate limiting components.
I'm not. I mean, I did that open that could be a processor. Maybe it's something else. So right now it's a component and I would just attach that to to the auto tap engine.
It's a task project Arrow and or the mason was already there.
Okay.
jmacdonald 00:07:28 Yeah. It followed you from wherever you were, I guess.
Laurent Quérel 00:07:30 Okay.
What did you say?
jmacdonald 00:07:33 That. That milestone followed you from wherever you were previously.
Laurent Quérel 00:07:38 Okay. Okay? Oh, nice.
Okay.
And you said that you will do that.
jmacdonald 00:07:47 Yeah, this is actually a great way for me to carry my my work forward. I've got a proposal on how I would change the Yaml file based on the envoy model at this point. But I think it's time just to try and apply it somewhere else. And I I feel like I need to catch up. And Russ, anyway.
Laurent Quérel 00:08:03 We can.
So I just added that to the milestone list of tasks. So right now we have a a bunch of tasks. I don't know how many tasks we have in this milestone. Let's see my stone.
We have 23 open 5 closed already.
And we have a bunch of those tasks where people are already working on that. So, for example, the this one, I know that Albert is working on providing a set of methods to basically rename, insert delete, attribute, independently of the underlying representation of the the open telemetry batch.
So that this task is a dependency of the attribute processor and David, also from a 5 is working on skeleton for the attribute processor. So basically taking the existing configuration model used by the attribut processor part of the Google Connector and basically mimicking the the same thing for for us.
with the addition of a native rename action which is not supported by default by the attribute processor. The idea is to the recommendation inside the the the go. Documentation for this attribute processor is to delete, insert.
but probably because there is no way to to be to be faster than that.
But we by exposing a rename method on action on our side, we know that we can leverage some optimization. So that's why I suggested to to have this additional action.
regarding the Ota P data based batch processor maker mentioned yesterday during a conversation that he will. He will work on that. So they had some discussion between between him and and Albert.
So Albert will focus on the mobile processing part, and and Michael will focus more on combining those batches.
And then that will be used by the Batch processor, which will be also something most likely that will speed in 2 main tasks, the the one where we have the the creation of the the processor itself, with the interpretation of the the configuration and the low level part, the pillar part.
the signal type router. It's something that already. On which let's see if there is an assignment on that.
David perfect. So David is already working on that based on So I think there is a documentation. Let's see.
I don't remember. Where is the this configuration specification?
Maybe it's part of the just like to show you guys the configuration side of that. So yeah, I think it's you.
So so this just just as a reminder, the senior router is a processor that give the option to roots based on the signal type.
If it's a metric the the corresponding batch will go to this output port if it's the log in this one, and so on. So it's just a way to to route things based on the signal type inside the dagger and that can be achieved without requiring the serialization for Tlp batch.
So the way that it's designed right now.
Based on the the native configuration model used by the data flow engine which is slightly different from the go collector. And we know that we have a translation mechanism that we will have to implement at some point.
because this configuration model used by the data flow. Engine is like a superset of the the Google Connector configuration with it.
So in this specific case, we are leveraging some element of the configuration model that are specific part of the superset and more specifically, we we mapped so here we have a a map describing, okay for traces we want to.
We want to send the information to those destinations with the corresponding dispatch strategy.
So we, the the mapping where to send a specific signal type is described in this in this section.
And the the pure custom configuration for this processor is booked inside this section config. In that case, we we we don't have many things. We just have something saying, Okay, if there is signal type arriving to this processor, and we don't have any description of where to send this signal. We just ignore all we we. We can define the behavior right now. It's not well defined. But that's the idea.
So again, David is working on that and there are some elements that are missing into the tap engine itself to achieve the the.
the, the signal type router. So we what is missing right now is a way to send a specific tab P data object to a specific port right now we can only send information to to the default part, so that's most likely will be my my next dust in order to to unblock the this signal type hotel, data flow and gene example performance.
Yeah, this one has to be to be updated. We we, we made a lot of progress in this area.
I think Chris will will update that soon.
So basically, we you probably saw that that we.
we have been able to to compare the go collector with the rice data, flow engine on a very basic scenario, otlp to Otlp and the the result I've been summarized into, I think if I go back there we should see the and closed and oh.
message!
But I'm not the with the don't remember how that works.
Maybe it does.
Yes, yeah. So the these tables summarize the the current result.
So I'm pretty aware that a lot of information are missing in this table. It was just a quick and dirty table, generated with chat dpt from the the results.
But the so the the idea here is to compare the good collector and the rest of the tap engine for a basic scenario, otlp to Otlp with multiple calls.
So it's leveraging the new engine implementation that is able to based on a configuration parameter. Or if this configuration parameter is not provided we use the entire all the calls of the corresponding machine and So the way that this new version of the engine is working, we use the the number of core on which we want to run pipelines.
We provide a pipeline configuration, and we create one thread per call up to the the maximum number of call provided by the parameter.
and each thread are pinned to the, to the specific core, and then inside this thread we use the the produce type hydrogen which is started with a single threaded, I think, one time, Tokyo.
And and then we we just start the the event loop each socket created by the otap receiver, or using the the sou sport option, which means that externally, this entire thing looks like a single pipeline, but internally they are independent pipeline, one per call and this table also, when when I run the the corresponding scenario which is based on the the benchmark benchmark framework that has been implemented by Chris and and Cj.
So that we have a traffic generator sending logs as fast as possible and and then the output of the Otip receiver is captured by a python back end that will measure the number of logs received and and the the log rate is measured on that and we have a bunch of metrics that are also kept to you like CPU usage.
and the memory usage and the the value scenarios benchmark scenario that I've been testing. I try just to to start with one core and what I observed, is the the go collector. When we we are full speed is saturated with one call.
which is not the case, and and it's visible here. The the O dot 95 plus to one mean that we we use the Ontario call and it. It's not represented here, but The log rates was smaller than significantly smaller than the the rest of that engine which confirmed that we were saturated with this specific one core configuration.
which is not the case when we have to call so the bottleneck here was the go collector starting with 2 core the buttons the the python back end.
or I don't. I'm not sure of that. It's a combination between the the Titan back end or the traffic generator. So that's 1 of the next steps that we we want to to achieve is improving the the traffic generation and the the back end used by the benchmark infrastructure.
Or in multiple ways. First, st having something that when we run a single instance of the back end or a single instance of the the traffic generation, we have better results and then being able to to deploy multiple traffic generator and multiple back end in order to to scale as much as we want.
So a any maybe feedback or question on that. I think it's it's marking a really cool milestone for us.
jmacdonald 00:22:07 Yeah, this is great. I am. I'm really interested in this imaginary reality. You've described where we have multiple load producers, multiple back ends so that they can scale effectively to to really place the collector under test. It seems like we ought to be able to monitor the those things, using an observability signal like making sure that the load generators are are not saturated themselves, making sure that the load receivers are not saturated themselves, and so on so there's an interesting opportunity. There.
Laurent Quérel 00:22:41 Yeah. And and Chris, maybe you can discuss a little bit about that.
Chris Hain 00:22:46 Yeah, sure. So the the framework supports what we just generically call monitoring strategies. Right now, there's 2 of them. One of them will look at process. Well, I guess there's 3 so just look at the process table. Give utilization metrics. Look at Docker to do the same. And then, Prometheus scraper. Basically.
So all of those just generate internally using the hotel sdks, metrics or logs or traces.
And then internally, they write to a in memory table that we can query to do the reporting and stuff, but it also allows you to output it.
So I've pointed it at like a click house instance and put a grafana on top of it. And yeah, we can definitely do all kinds of cool stuff with it. Demo wise.
Laurent Quérel 00:23:33 Yeah, and and but the, I think that the problem that's also Joshua was raising about having a mechanism, a generic mechanism to determine where are the bottlenecks?
Just to make sure that what we see is the limit is assigned to the right component. So so, for example, for the ideally for the one core, we should see all the the bottleneck in this specific scenario is the go collector for all the other, we should see either the back end or the the traffic generator. To be honest, I I did some manual evaluation to try to notify that the way I did it. It's not perfect.
far from that. But I think that's where we we need to to improve and and to think about some kind of methodology into the benchmark infrastructure. But the way I did it is I changed my knowing that the the worst data flow and gene was not the bottleneck. I replaced the I use an otlp to perf exporter configuration.
and then I started again. The the benchmark infrastructure in order to observe if the traffic generator in Python was able to reach a much higher level in terms of log per seconds, and that that was the case. So that inform me that most likely the bottleneck was more the back end.
Chris Hain 00:25:22 Yeah, I think as long as we can get the telemetry in all of the places that it needs to be to show us when things are, you know, queues are full, or whatever you, the front is ready to expose those. I think.
Laurent Quérel 00:25:36 Yeah, to the degree.
Okay.
jmacdonald 00:25:39 I love the idea of us actually recording telemetry into files that are perhaps otap.
we might call them, and then.
Chris Hain 00:25:48 Right now. They're.
jmacdonald 00:25:48 Some queries of our own to like do that. That'd be cool.
Chris Hain 00:25:52 Totally right now. They're my very dumbed down Otlp rk files, but it's it's working. So we're we're ready to translate it over and do the Otap version.
jmacdonald 00:26:03 I like the idea of Click House. But I even like the idea of data data fusion queries over parquet more.
Chris Hain 00:26:09 Yeah, somebody's gonna have to teach me how to do this, because I think that sounds cool, too. I've I put duck dB, in now on top of the parquet.
But if there's other better ways.
jmacdonald 00:26:18 I suspect Jake has has some experience with this that he might be able to share. I also like Duck TV for the record.
Chris Hain 00:26:24 Sweet.
Laurent Quérel 00:26:29 Okay. Great.
jmacdonald 00:26:30 Thank you.
Laurent Quérel 00:26:35 So let's see on on this list, I know.
But the the Syslog receiver we had a very nice pr recently from I made some some suggestion, but it's more or less ready to be tested.
Is there any other? I remember that there is each we should see something like the the Delta dictionary. I think I created.
I created a task for that just to to yeah, add support for the dictionary, and I think I already know I I so, Jake. I think you are working on this task right.
Jake Dern 00:27:27 Yeah, I have a Pr open upstream for it. I'm just kind of waiting to hear back with some feedback from those folks about what I did with the in particular, the dictionary builders. I think I mentioned last week, or maybe the week before that kind of the circumstances under which you can omit a delta dictionary are pretty limited, just due to the architecture. Currently. With an arrow. And so I made some changes there with an arrow. Rs, as well to try to improve that situation a bit. But there'll probably be some future work as well. But yeah, I'm just waiting to hear some feedback from the Maintainers. There.
Laurent Quérel 00:28:02 Okay.
Why, I'm not able to assign you to this.
jmacdonald 00:28:10 I think Jake may need to join the hotel community, and Github first.st
Laurent Quérel 00:28:13 Oh, okay. Okay.
jmacdonald 00:28:14 We should, we should get that going because, Jake, you've earned it, and I will sign that we need one of the F 5 people to agree to that easy, Peasy. I'll I'll let you know how to do that, Jake.
Jake Dern 00:28:25 Awesome. Thank you.
Laurent Quérel 00:28:25 That's right.
Great is there anything I missed in this list or that you'd like to to add, just trying to let you.
jmacdonald 00:28:43 Very organized.
Laurent Quérel 00:28:45 Yeah.
I'm also looking at the the telemetry instrumentation started to think about it. I will most likely write inside this bit of issue, a little bit more detail.
We already have the tracing proposal. But I think, we we need some thought regarding the matrix, and how that could be connected with the rest. Open telemetry. SDK, so I I will. Most likely end of this week, or beginning of next week starts to to add some some thought about that here.
and I will notify on the the slack channel just to make sure that I have people looking at that which are a lot familiar with this area
jmacdonald 00:29:41 Make sure that we get C. Joe in the room for that as well as, and have some an opinion as well.
Laurent Quérel 00:29:47 True.
Yeah, the signals generator. So we we are making good progress also there. So currently I don't remember if it's already emerged. I'm not sure.
But so basically, we, we have this it's still named fake data generator but so in in this list, it's a signal generator. But it's basically the same thing.
The idea is to leverage semantic convention and generate synthetic otap traffic and So it's a receiver that can can be combined with whatever you want. So the the idea is you know, we we could replace what I mentioned before the the python based traffic generator by a signal generator combined with either an Otap exporter or a no tap exporter.
and these 2 connected if you run the the data flow engine with this pipeline, then you have a traffic generator for a specific protocol and and based on what? Joshua, will.
you will do we could integrate this rate limiting mechanism inside the pipeline, and then we have something able to generate strategic traffic.
That's comply with a specific rates.
I mean.
jmacdonald 00:31:33 I mean.
you know, the the idea that we're gonna start using our own components as the producers and the consumers. Then we can use our own rate limiters and our own instrumentation to make observability, to see whether it's all working. Yeah.
Laurent Quérel 00:31:45 Yeah, there are still limitation in terms of how realistic is the the traffic that is generated. It's much better than before, because now we have real signal with real names, with list of attributes that are meaningful. And we and we have some make some correlation already in place that should make the the measurement of the compression rate, for example, much more realistic than something that is purely random.
What is missing? And and there are some efforts in the other project. Open telemetry. We were to add annotation, to specify a little bit more an attribute type. So okay, we know that it's a string. But what is the semantic of this string? Is it a new URL? Is it a pass this kind of stuff?
So at some point we will leverage what weaver is doing in this space.
To improve again the the the quality of the the synthetic otip traffic generated.
yeah, this one. Most likely I will not work on that before few weeks, but I think that's super important as a demonstration point at least for 5. It's super important. Being able to demonstrate that we are able. Once we have a pipeline running showing that we can update specifically a node configuration live.
So an example, we have a batch processor with some some value for the maximum size for the batch and maximum duration, and we decide to change that.
And without that allows.
we we apply the change and and we have said that we have a different size for the batch.
We should be able to apply that to most of the the net configuration.
I'm sure that we will have some limitation that we should be able to create some kind of protocol between the the node and the the engine itself.
to to report when a liable configuration is not possible.
yeah, the the integration of so for all the scenario that we we discussed last time.
I think we it would be very nice to have some kind of page, maybe github pages.
That show the current performance for each scenarios between the go collector and the rest the tefu engine.
That's the idea. Behind this thing.
there are some very basic stuff not necessarily super useful to This one is already that we already have a Pr.
oh, yeah, just one thing about this one, because, yeah, so we have a a very basic cli tool now in in the repo that give a way for the the benchmark infrastructure to run. Basically the rest of the fluently.
Mostly 2 parameters are already available. You can press, specify a pipeline configuration and the maximum number of call to you to use but what I also did yesterday is adding, this information, which is, I think, a useful so when you you call the this command with Dash dash out, you, you know, if the binary that you are using has been compiled in debug or release mode, it's especially super important if you, if you want to to run the benchmark, making sure that we have a release mode.
The difference is gigantic, I don't remember, but at least one order of magnitude, if not more.
the number of CPU core is also displayed. So you can determine. You know, in which range you can play with this parameter.
And and finally, I think that this one also is interesting because this list will evolve the the available plugins. You run so that basically, the this rest of that engine discover dynamically, not dynamically, discover during the the the link.
jmacdonald 00:37:36 Dynamic linking, static.
Laurent Quérel 00:37:39 Yeah, static linking so the discover the the different components that are available. And I just put this list there for the risk. So right now, we don't have a tap processors. But we know that people we have the attribute processor and the Batch processor that we have and the signal type processor that will be integrated soon, so that this list will will we will see progressively those elements into the the processor sub item there.
But we already have those receivers. We already have those exporters. So it's it's informative. Because when people want to create some pipeline, they will have a list there that will grow.
okay.
yeah, I think that's more or less what I had in mind to to discuss regarding the the milestone. I think it's I already took a lot, so maybe we can open the floor for them that maybe wants to Talk about. There are specific tasks or question, or whatever they want to discuss.
jmacdonald 00:39:00 Well, I see that Ukrash has a a topic on the agenda.
Great!
I'd like to talk about it, too.
Utkarsh Umesan Pillai 00:39:08 Yeah, sure. So like right now in the Pr that I sent out there's no like support for Dls, and it's not a priority for now, like I think, for Udp. Anyway, it doesn't really matter. I don't believe we have users even trying to like encrypt data over Udp. But I'm not sure. But mostly we would have to support Tls over the Tcp. Reception.
So I was wondering, like similar to how we have the engine support for like creating a socket. And are we also gonna have something for Tls support, and like the certificate quotation, or whatever things that come up with it. Come with it.
Yeah.
Laurent Quérel 00:39:54 Yeah, yeah. Yeah. I definitely agree. That's a topic that we need to.
most likely. Like you said in into this question.
That would be something that would be managed by the at the engine level, exposed with the the effect handler.
To be honest, I don't know yet the the detail.
But we defensively have to work on that. Maybe we can create not necessarily for this next one, but just for to keep track on that we could create a task.
Yeah, there's support, and
jmacdonald 00:40:56 So let's see, Tls, support means that there's extra control messaging just to initialize a Tcp connection.
Laurent Quérel 00:41:04 Yeah, for? Tcp.
okay.
just I mean, okay.
jmacdonald 00:41:46 Right.
I don't have any topics to discuss except a little request for a review on a go component. Pr, I recently started running and catching up on a backlog of collector contribute issues assigned to hotel arrow, so that we keep those components alive. And I found a pretty major regression. And I went and fixed it as well as went, to find the root cause, and fixed it, or have proposed fixing it. So this is like not much to see here, except we've got 2 broken versions and nobody reported it. I think it means that that nobody's really using this anymore. It was my old employer who was so or they're not using the newest versions. But I want to keep them working so.
Laurent Quérel 00:42:30 I like it.
jmacdonald 00:42:30 In addition to this, Drew noticed a regression in one of our tests which I've now gotten to the bottom of, and I'll follow up with that in a bit.
I apologize. Drew's not here. He mentioned it. By the way, there has been some recent success on our side with the Kql implementation, which they're rushing to get something in front of a customer for. But has been successful. So at this point we know that we have some reasonably robust code to parse these expressions, which can give us a language for renaming, and I think that we'll bring these pieces, together with the the attributes processor stuff that you mentioned earlier.
Laurent Quérel 00:43:07 That's excellent.
great. And and right now, the so this demonstration is passing the the queries and and doing implementing some processing basically executing the corresponding plan on some otap object or if I remember well what Drew and I'm not good with the his name, Michael.
you were saying that for the yeah. So the the their intent was to just come with a very basic implementation of the the query engine.
Yeah, so to to prove the plants right?
jmacdonald 00:43:52 That's right, and they've they've done that. So there's a a sort of non arrow based. It's not. It's it starts with an Otlp object, and then it parses it, and it it. It goes into some pretty sort of dedicated territory where you know Kql. Expressions that he's he's interested in have some like richer types that they need to kind of like process. So like making a date time out of a number, for example, is is something they're they're doing, and I don't quite see how it comes together yet in in the in the end. But there is. But but we understand that there would be an arrow based data fusion based idea. Eventually, it's just much further out. And then I would be, I think there's a short path to getting a a Kql parser expression that can be just be literally a renaming translation. And we should be able to compare that with the attributes processor syntactically, it's just like this is a shorter way of saying the same thing.
Laurent Quérel 00:44:49 Yeah.
Okay.
Yeah. Because what Albert is doing exposing some data manipulation at the pdata level?
But when they are ready, and they have something working based on their Otlp model.
Switching to this wrapper should be fairly easy, because we will expose some, at least for for those transformation.
We will expose directly the the high level operation to to implement or in to implement, insert, and so on.
jmacdonald 00:45:31 Which should just touch the dictionary. Yeah.
Laurent Quérel 00:45:33 Done.
jmacdonald 00:45:34 Yeah, that that'll be great. I just. I wanted to share that. They are still moving forward. With The robustness of their of their records. It's called the record set engine.
Laurent Quérel 00:45:47 Great. So that means that we is. Do you think that it's reasonable to where it is?
To put a Kql.
pick your task into this milestone.
jmacdonald 00:46:09 I think we could stretch goal that. Yeah, I do. I mean, like, I form of the attribute processor that is Kql based is that sort of like what you're thinking.
Laurent Quérel 00:46:20 Yeah, because I don't think.
jmacdonald 00:46:23 Reasonable.
Laurent Quérel 00:46:25 Yeah, I think what we can do. Okay, I will update the the milestone based on this feedback and include include that as a switch rule.
jmacdonald 00:46:35 Sure I feel like I can. I can create it.
Laurent Quérel 00:46:38 Okay? Yeah, I I didn't use any kind of convention to represent stretch goal. Maybe we can create a label for that.
So that will be super visible.
jmacdonald 00:47:01 Yes, I will. I'll mark it that way somehow.
Laurent Quérel 00:47:06 Right?
Okay, okay. Any other topic to discuss.
jmacdonald 00:47:21 I do not have one myself.
I will say, if anyone wants me to review some code, and it seems like I'm not getting to it, feel free to ping me. I am absolutely willing to interrupt myself, to help you all.
Laurent Quérel 00:47:38 Yeah, there is on my side there is.
I don't know if I already got some reviews there.
Yeah, on this specific. Pr, 8, 8, 7.
If someone is ready to to review it. That would be nice. It's a small one.
jmacdonald 00:48:05 I will do that.
Laurent Quérel 00:48:07 Rates, and I will take also time for to to review this this year.
jmacdonald 00:48:19 Yeah, yeah.
Laurent Quérel 00:48:20 And that you yeah, the the the the batch.
jmacdonald 00:48:24 There's been a bunch of churn. This is actually relevant to batching. So I may as well explain what's been happening. The batch processor is an ancient component. We've been trying to tell people not to use it, but it's that, and that's a sold its own topic. The the design of the the exporter helper it's called, is a library of like common code used by all exporters.
and it sort of doesn't, doesn't need to be an exporter. Logically. It's just a efficiency concern to to make it be in the exporter only. So there, there's batching, and there's queuing, and they're integrated so the queue.
It can accept data, and it can return quickly with success. That's the in memory queue. If it's a persistent queue, it'll write it to disk before it returns success, or you can disable the queue, which means it will pass through. Now, if you enable batching.
it works in all those cases, and but it's quite a bit more complicated now, so you can bat you can. You can have a queue be sized with with a sizer sort of a queue request Sizer, like counting requests. There's an item sizer counting items, and there's a bite sizer. So then you say I want my queue to have a hundred 1,000 items in it, or whatever and then you can go configure batching. Well, 2 versions ago someone called out saying, I want to have different sizers for my queue and for my batch, and and it and they did, they justified it, and they went and added it so. But when it was added a a sort of a few bugs inspired to to make a problem here. Basically, I ended up with an empty version, sorry an empty sizer in my batch configuration.
and that was causing an obscure failure.
If you happened to set the Sizer field it would work. It's just that it's set to an empty, and there's a missing validation. But there's a bug in validation, so it's a combination of a bug and a missing field. I wouldn't say it was actually broken. It's just that it won't start, and it will give you a very obscure message. Why.
so that's that's where we are. What what I've done here is just to to set the default. And and this it turns out, actually, we did have tests that caught it. But in the sort of haze of late July, and I was just back from a vacation.
The the the release caught caught this with some of our contribut tests, and then I just said, Go ahead and skip them. So it was my fault for letting us skip the tests. The tests didn't actually expose. Why, the failure was happening without investigating a little bit, so I wouldn't blame the Maintainer who did it, either. My fault.
anyway, small fix here.
Laurent Quérel 00:50:54 Okay, could could you describe in more detail the the queuing system that? Oh, some question, maybe.
Utkarsh Umesan Pillai 00:51:05 Sorry have a very separate topic to discuss. I just thought like, I mean, I don't know know, you were gonna follow up with the question. So yeah, please, before.
jmacdonald 00:51:17 Okay, so open open discussion about queuing and batching the and and of course, I do want to talk about queuing in this context here and engine the the queue has persistent and memory options, and it has there's a way to disable it as well.
So so, okay, that's not even quite true.
There, there are a couple of options that were have been added to the queue to facilitate a a range of behaviors. And I'm not sure I like the defaults, which is part of the reason why I was fiddling with them in Hotel Arrow. So the the behaviors that you can configure are to block when the queue is full.
and then there's a separate configuration that you can configure, which is to wait for the result. Now, I think not waiting for the result is a pretty bad idea. If you're a memory queue, it means it means you can lose data very easily.
but it is off by default. Which means that out of the box you get a memory queue. You won't wait for responses. You're gonna get success to the client. If if you crash, you lose some data, so we now have this wait for result. True bit that we can set, and that will cause it to have error, propagation, and back pressure.
especially when you combine it with the block on full option. So those 2 options let the let us have back pressure and error propagation as we push into the queue.
and then the act of pulling out of the queue can have batching or not, and it's sort of like on the on the, on the retrieval side that the batching happens. If that makes sense.
and I don't know. I've definitely studied and tested this code. I have some faith in it, but it's pretty complicated is that I don't know if that answers any of your questions.
Laurent Quérel 00:53:10 Yeah, that my, my my interest there was to understand. If this concept of queuing and batching are combined into a single processor, or there are 2 concepts that are implemented in different parts of the system, maybe with 2 processors, or maybe with some a combination of processors and and and helpers, you know, or awesome.
jmacdonald 00:53:41 Yeah, they're. They're pretty.
Laurent Quérel 00:53:42 Of the engine itself.
jmacdonald 00:53:43 At this point.
And I don't.
I don't think we should copy the design. The coupling is I'm not sure if it's fundamental, or whether it's sort of like a premature optimization, maybe, or And I I don't really want to be responsible for the design either. So how does that sound?
the the fundamental like trickiness? I guess here is that the data comes in to a sort of shared pool, and then the data is pulled from the shared pool. And it's the there's this concept of a consumer which is the the active element that goes into the queue to pull data out, and if it's a batcher it will pull lots of data out to form a batch and then send it, and if it's not batching it will just pull one item or one request out and send it.
so so so is this sort of like, a place where you combine, push and pull disciplines in the same same spot, I guess, and this num consumers control. It's a configuration that determines how much export concurrency comes out of the queue, so you can set that to one, and then you'll only get one exporter.
Laurent Quérel 00:55:10 Okay? And and you also mentioned the the system that doesn't wait for the response.
So I guess it's related to the acknowledge mechanism that is sent back to the to whatever client is communicating with.
jmacdonald 00:55:30 Early acknowledgement, or like a you know.
Laurent Quérel 00:55:33 So how is it achieved? I mean, what is the mechanism between dispatch processor and the underlying gu engine to determine how to inform the receiver that? Okay, you can send your your mechanism
jmacdonald 00:55:54 Are synchronous. So the receiver has got a go routine that's called into a processor, and that processor is called into an exporter. If the exporter has a queue, it will, and it has space for that.
It will return a success immediately. Basically.
Laurent Quérel 00:56:09 Okay. Okay. Okay.
Okay. I see.
jmacdonald 00:56:14 So and and so there's this complicated like decision logic at the start of the queue to say, if I'm if I'm disabled, then I'm going to Call through directly. If I'm if I'm if the if the queue is full.
it depends on whether that Boolean is set or not, which case I can either fail fast or block, and if the if the the user has asked to wait for the result, I have to block further until there's a response which which is a whole separate apparatus of getting that like the signal passed backwards through the queue essentially.
and that only works when you're in the in memory. Queue not the storage queue, the persistent queue.
Laurent Quérel 00:56:58 Okay.
jmacdonald 00:56:59 Yeah, I have to say that the this code has evolved in a rather organic way, and it's not not clear. That was.
you know, like you.
Laurent Quérel 00:57:09 Yeah, but it's very interesting for us to to learn from it and try to to see if there are other options with all the the shortcuts that we we have to to avoid, and the the various issues that have been observed, I mean everything is super informative in that case, for us.
jmacdonald 00:57:28 Yeah, I think the interesting thing that we should pay attention to is just that there. So the beginning of this story was, there was a batch processor. And the problem is that it receives P data in and it gets P data out. So the the no matter what you do, you're still handling these objects. And the I guess the thinking was that, well, you're going to get this P data object passing all the way to an Otlp exporter, and then it's going to serialize it. Well, if it fails, it's going to serialize it again.
Well, that's silly. Maybe we should serialize it once, and then only try to export it the same bytes again and again, and then and then you're like, Okay, well, if it's a persistent queue, well, then you're gonna pull this these bytes out of the queue. You're gonna pass into an exporter. Do you have to unmartial them from the persistent queue and then marshall them to get into the exporter. So there was a start of a facility that lets us imagine that that the data gets serialized on its way into the queue, persisted as serialized data, pulled out of the queue with serialized data, and then sent directly through the exporter as serialized data.
and all that is theoretically possible and yet not done for the Otlp case, which the thing I'm set by a little bit right now is that all this tremendous amount of refactoring and redesign of the exporter helper and the queue and the batch has all been done in service of getting that efficiency, and it's not been done for the common case, like the users, don't benefit yet, because the Otlp exporter doesn't have it.
And so I have this like like sense that there are vendors who are just trying to optimize for themselves that, you know, like, while ignoring the common community performance, and that's that's upsetting to me but it it, you know. We can move forward.
Laurent Quérel 00:59:15 Interesting.
jmacdonald 00:59:17 And I feel like.
Laurent Quérel 00:59:18 And the.
jmacdonald 00:59:18 In the in arrow. We have this notion that, like 0 0 copy is a thing now. So we shouldn't really need to couple the queue in the in the batch so much. But that's just the concept.
Laurent Quérel 00:59:29 Yeah, I agree. I think they could play and and opening composition scenarios. I mean.
for example, the queuing could be could be used in a scenario where there is not necessarily batching.
if the goal is to to acknowledge messages as soon as possible.
but still doing that in a very secure way we just need to couple, I mean in the pipeline that's as a component.
But to create a pipeline where we have a receiver combined with this queuing mechanism.
And then we have a system to very quickly and securely or in a reliable way to return an acknowledge message to the data producer as soon as possible, still being able to, in a in another part of the pipeline to process the the queued messages and and the batching could be done later in a different way. It's totally independent and and and being able to to queue the message at different level.
Because it's it's like a policy depending on your on on your scenario.
Maybe you will prefer to queue the reform, to never queue or to queue that as soon as possible as late as possible. Maybe in the middle. I mean, it's something that could be decided based on the on the use case.
jmacdonald 01:01:09 Yeah, I totally agree that that there's there's not a reason, a fundamental reason that you wouldn't wanna sometimes queue right after the receiver say before an expensive process.
Laurent Quérel 01:01:17 Yeah.
And and once again, I think it's a nice example of why it's so important to have this.
basically, we have 2 channel of communication into this new engine.
We have the P data channel and the control channel, both direction for the control channel, not for the the P. Data is always going from receiver to exporters. But the control and it's part now of the it's already now in the main. But we we have what I named Node control message and pipeline control message. The Node control message are the control message poll used by nerds with and targeting the pipeline engine.
The pipeline control message are produced by the no. Sorry. The Node control message are targeting nodes and the pipeline control message are targeting the pipeline itself. And and so a node, for example, when a node is requiring a timer and and and, for example, it's a request to receive a timer tick every X millisecond it's it's translated, in fact, behind the scene into a pipeline control message sending the request to the pipeline. The pipeline engine will record this information. Maintain a priority queue for the values timers, and we'll generate based on on this information, we generate the timer messages to the right node and and that will will be used also for acknowledgement mechanism.
So saying that let's say an exporter say, Okay, I received the acknowledgement for this batch.
the acknowledgement message will be translated into a pipeline control message and the control. The controller of this engine will dispatch the corresponding event to nodes in upstream in the pipelines, some node that are upstream to the, to the exporter that have interest for this acknowledge mechanism. This way we we will have something that will be very composable. And that's the general idea behind that I think we are already.
We are at the end of the meeting. Thank you so much, guys.
And we. We have a clear plan now for for September.
jmacdonald 01:04:10 Thank you. Thank you. All time's up. Gotta run. See? You soon.
Laurent Quérel 01:04:15 Yeah. See you soon. Bye.
Chris Hain 01:04:16 You guys.
Michael Salib (F5) 01:04:18 Bye, bye.
