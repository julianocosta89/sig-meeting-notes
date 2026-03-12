SIG: Collector SIG
Date: 2026-01-21
Duration: 35 minutes
Zoom Recording URL: https://zoom.us/rec/share/Ss8T2MLSTmuVCOV3f4b_PePvq3VQGU1Ac0OQCtI_XJmi0IewVeaf0wVCOLbUtN0b.Xwj_FrCGjxzUBQvW
============================================================

## Zoom Recording Transcript

**Andrew Wilkins @ Elastic Observability** 07:02 Hey, Dimitri.
**Dmitrii Anoshin** 07:03 Hi, Andrew.
**Andrew Wilkins @ Elastic Observability** 07:04 How we doing?
I'm good, thanks, how are you?
**Dmitrii Anoshin** 07:09 I guess it's been not that many people.
**Andrew Wilkins @ Elastic Observability** 07:13 Nope, just you and me.
**Dmitrii Anoshin** 07:16 Yeah.
Not very popular time zone.
**Andrew Wilkins @ Elastic Observability** 07:19 No, do you have any recommendations for how we can make it more palatable?
If it were an hour earlier, would that be better, or…
**Dmitrii Anoshin** 07:31 For me, maybe we'll catch more people from the West Coast if we do it an hour earlier, because right now it's 5PM, which is still fine, but some people may be… Would like to.
**Andrew Wilkins @ Elastic Observability** 07:43 I'm illegal.
**Dmitrii Anoshin** 07:43 At 4pm, but I don't know. What's your time now?
**Andrew Wilkins @ Elastic Observability** 07:47 Right now it's… it's just after 9am.
**Dmitrii Anoshin** 07:50 No.
**Andrew Wilkins @ Elastic Observability** 07:51 I could go an hour earlier, easily.
**Dmitrii Anoshin** 07:53 it'll be, like, maybe less convenient for Australian people, but I guess, who from your time zone is joining this call? No one else, right?
**Andrew Wilkins @ Elastic Observability** 08:03 Just me, at the moment. Sean is… I think an hour and a half, later than me.
**Dmitrii Anoshin** 08:13 Later.
**Andrew Wilkins @ Elastic Observability** 08:14 He's in the middle of Australia.
**Dmitrii Anoshin** 08:16 Okay. So…
**Andrew Wilkins @ Elastic Observability** 08:17 That would be okay for him, I'm sure.
Yeah. But anyway, just, just me.
**Dmitrii Anoshin** 08:25 We can try, we can try, like, make an announcement somewhere in, like, Open… Collector Dev, maybe, or a Slack channel, and see if people, like, if there are… if there are some people that would rather join. If we… if we switch them, then it makes sense. Otherwise, if, like, no one replies, I don't think we should… it makes sense to bother.
**Andrew Wilkins @ Elastic Observability** 08:46 Okay.
Alright, well, I just had that… well, I did have two items on the agenda, I'm not sure if you're interested in the other one. Maybe we can start with the Exporter Helper one first.
So, first of all, did you have a chance to read the proposal I wrote on the issue?
So last… I don't know, it was maybe a month or two ago, we talked about, A pull request one of my colleagues put up, which is, basically adding metadata keys to…
**Dmitrii Anoshin** 09:22 the exporter helper QBatch config, and that would mean that we could do.
**Andrew Wilkins @ Elastic Observability** 09:28 Batching by… unique combinations of metadata, so we could do multi-tenant batching, but it would be limited to metadata. It wouldn't allow us to do, like, batching by resource attributes or whatever. Then we talked about maybe we could do it as some kind of extension point in Exporter Helper, and I looked into it. The problem I see with this is that Exporter Helper is based around the request interface.
And the request interface is… it might… by default, it's PData-based, but it might not necessarily be P data based. And as soon as you move away from P data, then that means you can't use OTTL or… or whatever.
So that, to me, means that it's a non-starter.
**Dmitrii Anoshin** 10:18 Yeah, but it's also based on the exporter, right? Like, for example.
if request is anything other than P data, it's, like, explicitly It's explicitly developed in the component.
We don't even have any example like that, but it's explicitly there. And, not… Extension mechanism.
That you mentioned. That still has to be enabled through the… by the exporter, like, exporter… developer, right? So we currently have with batch queue, or options, like, or options to the factory of the exporter. So, if they use something else other than P data, they just ignore that. They cannot use that capability, right, that extension point.
That we would introduce. That extension to bash by PData would be only available if request is PDATA-based, I would say.
And I think that would… potentially… Address your concern?
But, other than that, if you have any, like, other concerns related to that, for example, request still is kind of generic, like, wrapper over to data, right? So, potentially, I can see it being problematic to… introduce a TTL interface, even if it's, P data only, but otherwise, if it's, like, if it's… if it's custom requests, we just don't bother.
I will say that.
What do you think?
**Andrew Wilkins @ Elastic Observability** 12:08 We could, but then that means that your pipeline is gonna be… different depending on what your exporter is, which doesn't seem great. Like, you wanna…
**Dmitrii Anoshin** 12:20 So you're saying it's… it's, it's not that ideal that we'll limit?
Delete the exporter, okay. And if we have metadata, it would be available for all of the exporters, essentially.
**Andrew Wilkins @ Elastic Observability** 12:34 Exactly.
**Dmitrii Anoshin** 12:35 Okay, is there a way to have an extension point that would be… would provide limited capability in that case, like metadata only, for those that don't implement PDATA-based requests?
**Andrew Wilkins @ Elastic Observability** 12:50 Yeah, so client metadata would be available Regardless of whether it's PDATA-based requests. So that will always be available.
For every exporter.
**Dmitrii Anoshin** 13:01 So in that case, like, this extension point, when the user… the component developer, export the develop… when it… adds that to the factory. The factory… that option, the factory would be… whether you expose for tracing metrics, logs, and SP data, or it's just for metadata in that case.
**Andrew Wilkins @ Elastic Observability** 13:26 Not sure I followed, but, sorry, could you repeat that?
**Dmitrii Anoshin** 13:32 I mean, like, that extension point would be an option to the factory, right? With, let's say, with something, with, I don't know, with the batch and, I don't know how to call it at this point, but yeah. That option can accept arguments as well, and the argument would be, like.
How you configure that extension, whether it's only based on metadata, or it also allows you to manipulate the data.
**Andrew Wilkins @ Elastic Observability** 14:09 Yeah. Yes, that… I mean, I think that could work, it just means that it's only going to work for some exporters and not others. Whereas, if we do the… partitioning by…
**Dmitrii Anoshin** 14:22 pay data.
**Andrew Wilkins @ Elastic Observability** 14:23 Earlier in the pipeline, it's gonna apply for everything.
**Dmitrii Anoshin** 14:27 Likewise.
**Andrew Wilkins @ Elastic Observability** 14:27 Just naturally. So just any kind of… any other kind of processor.
**Dmitrii Anoshin** 14:31 Okay.
Makes sense.
Yeah, I guess it's fine. Like, do you have any… like, you looked into this more than I did.
there are people that are interested in this capability. Do you see anyone interested in… Other… Like, ways to split, partition, not only by metadata, by some other, like, request.
**Andrew Wilkins @ Elastic Observability** 15:02 Yeah, so the… the Kafka receiver… no, sorry, Kafka exporter?
Kafka Exporter has various options for… actually, let me see if I can bring it up real quick. But the Kafka Exporter has a config built into it for partitioning by various things, and that could all go away if we had something like this. I'm just gonna see if I can find it quickly… But the same sort of thing would apply to any other kind of streaming, Here we go, so in… Let me just share my screen for a sec.
So in the Kafka exporter, we have… partitioned by… alright, trace ID… resource attributes, yeah, just trace ID and resource attributes. I think there were some other requests, requests for other types of partitioning as well, but I've pushed back on them until we had a more general solution. But this is really not specific to Kafka, right? It's… it could… you could do the same thing with Pulsar, or RabbitMQ, or whatever.
Other than that, I can't think off the top of my head of requests, but there's also processes for group by adders, and… group by resource or something or other. There's a couple of group-by processes that could be replaced with a more general purpose partitioning processor.
**Dmitrii Anoshin** 16:39 By the way, do you know the group by… how do they work? Are they synchronous or asynchronous? Do they have any queues inside of it? By the queue, I mean… Life.
**Andrew Wilkins @ Elastic Observability** 16:50 paper.
Yeah, I don't think it's stateful, if that's what you mean. Oh, no, sorry, that one is stateful, apparently.
**Dmitrii Anoshin** 16:59 And it means that they have some kind of internal state.
**Andrew Wilkins @ Elastic Observability** 17:05 Apparently, yes, I'm not familiar with the details of how this one works.
**Dmitrii Anoshin** 17:09 The thing is, what we saw with the exporter queue is that if you enable persistent queue, you ensure that your pipeline is resilient, right? Yeah. But if we include those kind of root processors, and the one that you suggest.
we lose that capability, right? Users cannot introduce resilient anymore, unless you have it synchronous, right? Unless.
**Andrew Wilkins @ Elastic Observability** 17:36 So, that's If it's synchronous, yeah, so for the partitioning processor, I have in mind that it would be entirely synchronous.
**Dmitrii Anoshin** 17:43 Okay.
**Andrew Wilkins @ Elastic Observability** 17:43 So there'll be no statefulness. It will partition per batch that it's processing.
And it'll send down the line with metadata attached to it that means that it could persist that… That, multi-tenant batching through the, the, persistent queue.
**Dmitrii Anoshin** 18:02 Okay.
Do you think… will it introduce any slowness to the client of the collector pushing data? Because, like, you have one request, the request would be blocked until it splits and all of the requests comes to the queue, I guess.
It shouldn't be that…
**Andrew Wilkins @ Elastic Observability** 18:22 would do it concurrently, so that's… that's what I had in mind.
**Dmitrii Anoshin** 18:25 Yeah.
**Andrew Wilkins @ Elastic Observability** 18:25 So it should not… it might… there'll be some overhead, but it wouldn't be like we would send each one, and each one would block serially.
**Dmitrii Anoshin** 18:34 We would send them all at once.
Okay, yeah, given that this approach that I, I was proposing, it would require this new framework, right? Attach an extension to the exporters.
And it'll introduce significant complication in general, like, collective config is already pretty complex, and this would be another layer of complexity.
I'm thinking if we don't have any use cases like that, potentially we just can… Avoid that, and then go with your approach. By use cases like that, I mean, do you have any other problems that potentially can be solved with this, like, approach, with this extensible exporter?
pluggable exporter capabilities, I would put that. Are you aware of anything like that?
**Andrew Wilkins @ Elastic Observability** 19:27 So there's an unrelated one, which I… I have been reviewing, what's it called? The Arc extension, so you may recall someone was working on that. I, I guided the author towards introducing a met… like, a middleware.
**Dmitrii Anoshin** 19:46 Extension interface for the exporter helper.
**Andrew Wilkins @ Elastic Observability** 19:48 But that is… That's independent of the request implementation. It doesn't care about what request is. It's just, like, looking at how long the request takes, and whether it responds with an error, or a retryable error, that kind of thing.
**Dmitrii Anoshin** 20:07 Because the attachment point for this pluggable capability is different, right?
**Andrew Wilkins @ Elastic Observability** 20:12 Yeah, yeah.
Does it need to know about the data.
**Dmitrii Anoshin** 20:15 And where is that attachment point? Is it after all of the SKU senders? Like, at the end, or…
**Andrew Wilkins @ Elastic Observability** 20:23 Ehhh… Let me think… I think it would be before… I don't… I actually don't recall. I think it would be before the queue sender.
Ssm, sorry, I don't recall.
**Dmitrii Anoshin** 20:43 Yeah, if we don't have… solution that would suit both problems, this one and that one, I guess it doesn't make any sense to go with the idea of extensible.
Departitioning.
**Andrew Wilkins @ Elastic Observability** 21:03 Okay.
So are you comfortable with the… The change to add metadata keys.
**Dmitrii Anoshin** 21:11 Yeah, I guess that's fine. I would like to have some, like, at least another approver to go, maybe maintainer to… to agree on that, because it's gonna be additional configuration interface, which we would have to support forever, essentially. Like, stability work, etc. But I guess it's fine. Given that all of the discussion we have, and given that this, like the… more, attachment point for the acknowledgement?
Or was that? Gonna be separate?
**Andrew Wilkins @ Elastic Observability** 21:45 Yep.
**Dmitrii Anoshin** 21:46 So I think it's fine.
**Andrew Wilkins @ Elastic Observability** 21:48 Okay, cool. Well, I'll, I'll raise it in the leads channel, just ask for another approver or maintainer to have a look, and mention that we've talked about it. I'll also, assuming that that goes ahead, I'll also put up, I'll probably create a… processor, as I described before, in another repository, just to go through the donation process, and then we can discuss. So, for the partitioning processor that I described.
**Dmitrii Anoshin** 22:18 Oh, they…
**Andrew Wilkins @ Elastic Observability** 22:18 more extensible one. I'll create that in another repository, and then we can discuss whether it looks good, and whether we should put it into contribib.
**Dmitrii Anoshin** 22:27 Sounds great, and if we can, deprecate the others, group by things, that would be amazing. Because I don't think group by, how it works right now with the statefulness is an ideal. I think, like.
Potentially, we can introduce a statefulness as an option, but I don't believe it's ever needed.
**Andrew Wilkins @ Elastic Observability** 22:48 Yeah, I agree. Given that we have a queue.
**Dmitrii Anoshin** 22:51 which is completely asynchronous, it's pretty quick at the end, right? It has to be… Synchronized, I think.
**Andrew Wilkins @ Elastic Observability** 23:01 I agree.
Cool. Thanks for the discussion.
**Dmitrii Anoshin** 23:04 Yeah, and another one is also pretty interesting to me, to be honest.
**Andrew Wilkins @ Elastic Observability** 23:08 Yeah, actually, I raised it at KubeCon with Antoine, and he mentioned that you had some interest in this topic. So… I don't recall if we discussed this before, but, my goal is sort of to enable something along the lines of a Kubernetes cron job to start up a collector.
run a scrape, and then exit, so you don't have a lot of idle compute. So you might have some… you might want to do some collection every hour, or something like that, and you don't necessarily need a container running every… like, constantly, just for that.
**Dmitrii Anoshin** 23:43 Okay, okay, I see.
**Andrew Wilkins @ Elastic Observability** 23:45 So the idea I have in mind here is to… I guess I can share my screen again. The idea is basically to make the… controller for the scraper.
Pluggable.
So I… I spend a little bit of time Playing around with the config.
I have an example.
Yeah, so it would look something like… it would be an extension, so it'd be some kind of scraper controller extension. I got some AI to implement two options. One would be equivalent to the built-in controller, which is just a simple timer interval.
And the other one is an HTTP webhook approach, where you would hit an endpoint, and then it will run the scrapers, and then respond with success or failure after they complete.
Then you would attach them to a scraper with this new config, and you can disable the built-in Timer-based approach by setting that to 0 seconds.
That's sort of it as far as configuration goes, so I think it's pretty… it's about as minimal as we could get.
And the extension itself is just, like, something that you can register scrapers with, and then it… it takes over, when it… when it invokes them.
**Dmitrii Anoshin** 25:17 I'm curious how does it solve your problem if you want to have a cron job? It, like, starts the collector, so for your use case, the collector would need to start and just do one scrape, essentially.
**Andrew Wilkins @ Elastic Observability** 25:28 Yeah, so in our use case, I think we would probably end up with a custom distribution of the collector, where we would have a new subcommand. And this could go into core or contribib or whatever, but we would have a new subcommand that would install a extension.
That can be… triggered somehow. So then the subcommand would run the collector with just the scraper, receiver, and this extension, and an exporter.
It would wait for it to be running, and then it would trigger the extension, and the extension would trigger the scraper.
It's a little bit… Maybe a little bit more complicated than it could be, but on the other hand, this approach means that you could have scraper controllers that are not triggered externally, but they might be consuming from a queue, or…
**Dmitrii Anoshin** 26:19 Whatever.
Yeah, I'm not sure I fully understand this approach. I mean… How specifically you want to solve this problem.
**Andrew Wilkins @ Elastic Observability** 26:29 So let me… oh, I could try again if you…
**Dmitrii Anoshin** 26:32 Right.
**Andrew Wilkins @ Elastic Observability** 26:33 Okay, so you… there'll be a new command, like, hotel coal… Scrape, and then you give it the name of a pipeline and a scraper within that pipeline.
**Dmitrii Anoshin** 26:43 And it would…
**Andrew Wilkins @ Elastic Observability** 26:45 Start the collector.
And then send an event to a scraper controller extension, which would then Run the scraper in that pipeline.
Of that name, with that name, and that's it. It would just wait for the scraper to do its job, send to the collect… to the exporter. Once it's done, it would return back to the scraper.
Return back to the extension, and then back to the command.
And then it connects it.
**Dmitrii Anoshin** 27:15 So we need some kind of a… some kind of a proxy between CLI and the extension, essentially.
**Andrew Wilkins @ Elastic Observability** 27:22 Exactly, yeah, exactly.
**Dmitrii Anoshin** 27:23 Because you want to know when the scrape data is… scraping is done, essentially, and data is… Yeah.
**Andrew Wilkins @ Elastic Observability** 27:31 Once it's durable in the destination.
**Dmitrii Anoshin** 27:36 I think that should go to one trip as well, at least, because it's like… It's pretty common. In general, people are already running collectors in… And likewise, So, like, scraping is essentially pretty much… ideal for lambda… another lambda function, right?
Yeah, that definitely makes sense. I'm just thinking, like, for this particular use case, do we really need an extension that would control the scraper?
Or it can be just potentially something else, like, I don't know.
**Andrew Wilkins @ Elastic Observability** 28:19 I think it could be something else. I sort of went with this approach for more flexibility. Like I was describing before, you might want additional controllers that could do… could fade off a queue or something.
**Dmitrii Anoshin** 28:31 Yeah, if we need those controls, if we need those capabilities, right?
Potentially, we can have something, something like… In general, for the collector, like… kind of… so you need an event when collector is done.
I'm thinking, like… We can have something like idle timeout for the collector, right?
Okay, another, let's say, command line interface, maybe?
option. So, like, let's say idle timeout, 1 second.
And that would be part of the extension that needs to control it. The extension would just watch all the pipelines and see if any data on the receivers are if any receivers are busy, they would need to somehow report that, if they are processing data or not. And reporting… that is also pretty important. Like, we have this health… Of the… of the companies when they report health, but we… I think it's important to report when they process something. It's even possible through the metrics right now, you can just watch for the metrics if we have anything.
**Andrew Wilkins @ Elastic Observability** 29:40 Or not. But potentially, like, another mechanism to report that would be…
**Dmitrii Anoshin** 29:45 Would be good to have.
And that extension, we just see if, like, Elecard doesn't get any… Doesn't have any, like.
activity within, like, let's say a couple seconds, it just would… Turning off.
Something like that.
And in that case, you don't need a controller extension, but you would need to only just… Let's say we… If we say collection interval to zero.
it means that… I don't know what currently we… probably currently.
**Andrew Wilkins @ Elastic Observability** 30:18 That's a fa… that errors out, if you're trying to…
**Dmitrii Anoshin** 30:20 If we allow it, let's say, it means that collectors just don't do anything.
Except for the first one. The first one would be initial timeout, initial… initial interval, something like that.
**Andrew Wilkins @ Elastic Observability** 30:34 Cool.
**Dmitrii Anoshin** 30:34 But that one would be zero as well. In that case, if everything is zero, it just does one scrape and doesn't do anything after that.
So, does make sense?
**Andrew Wilkins @ Elastic Observability** 30:43 Yeah, that can definitely work. I suppose it comes down to whether or not we would want more flexibility.
For how the controlling… works.
**Dmitrii Anoshin** 30:53 If you are putting some kind of an RFC, let's put that as an option as well, and let people think about and… like, let's say, give… provide some feedback whether this needs or not. Maybe… I'm just… I just don't know about other, like, use cases when you would need to control scraper externally.
But if you have any ideas, when it really, like, makes sense, and there are maybe some people that need it… in that case, it's fine. But at the same time, I do agree that actually running a collector.
as a current job is a great example. It's something that a lot of people would probably need, for sure.
**Andrew Wilkins @ Elastic Observability** 31:42 Cool. It's a special…
**Dmitrii Anoshin** 31:44 Yup. Yeah.
**Andrew Wilkins @ Elastic Observability** 31:45 One other way you might want to invoke scrapers is as some kind of like, an action off a… an alert. So you might want to… say your CPU's gone up, you might want to perform an on-demand profile.
So, maybe continuous profiling's too expensive, or whatever. So you could, you could, hit a HTTP webhook.
**Dmitrii Anoshin** 32:11 Hmm.
**Andrew Wilkins @ Elastic Observability** 32:11 invoke a profile scraper for 10 seconds, and then grab the profile and export it. That would be another use case. And I don't think that would fit well with I mean, I suppose you could have an external HTTP process server that would start the collector, but that feels a bit… heavy weight, whereas you might have a collector that's just capturing the CPU metrics, and then has a dormant profiling receiver.
Scrape on demand.
**Dmitrii Anoshin** 32:43 That makes sense, yeah, that's a good… that's a good use case.
And the profiling scrapers are essentially the same kind of scrapers. They… They would, You use the same scraping controller?
**Andrew Wilkins @ Elastic Observability** 33:00 I don't think… I don't… I actually… I don't know. I don't know if that, looks like that at the moment. That was a hypothetical.
**Dmitrii Anoshin** 33:08 Yeah, but if we think about the whole flow, right, how would you make that? You cannot make it inside the collector.
It would still need some kind of external… external helpers.
**Andrew Wilkins @ Elastic Observability** 33:24 Yeah, you would still need some kind of alerting system, some event.
System, which can look at the metrics, make a decision about Yeah, basically some kind of work, yeah, workflow engine to… to do all that.
**Dmitrii Anoshin** 33:40 In that case, you need to have backward connectivity to the collector, which is also complicated.
**Andrew Wilkins @ Elastic Observability** 33:46 Potentially, this might go to the…
**Dmitrii Anoshin** 33:50 Obam.
Extension.
**Andrew Wilkins @ Elastic Observability** 33:53 Good to…
**Dmitrii Anoshin** 33:55 And because we have pump extension established the WebSocket anyway.
Otherwise, if you… if you do it separately, you would need to… some kind of exposed webhook of the collector, and back and be able to connect with it. It's gonna be pretty complicated.
**Andrew Wilkins @ Elastic Observability** 34:11 Yeah, it's a good point. It could be a custom message or something with op-amp.
**Dmitrii Anoshin** 34:16 Okay.
Yeah, maybe let's put that as an example, and again, I think we need to explore.
If there is a need for the… Scraper… scraper extensions.
I just, again, I don't want to introduce complexity for hypothetical use cases, which are never… will be needed for.
**Andrew Wilkins @ Elastic Observability** 34:40 Okay, understood.
Okay, well, I will write an RFC sometime, I'm not…
**Dmitrii Anoshin** 34:45 I'm not sure when, but I'll put that up sometime and…
**Andrew Wilkins @ Elastic Observability** 34:48 I'll ping you for review.
**Dmitrii Anoshin** 34:50 Sounds great. Cool.
Yes.
**Andrew Wilkins @ Elastic Observability** 34:54 What?
**Dmitrii Anoshin** 34:54 That's, that's it, right? For today.
**Andrew Wilkins @ Elastic Observability** 34:57 That's it on my end, yep.
**Dmitrii Anoshin** 34:58 Yeah, I don't have anything either from my side. Yeah, thank you, thank you, Andrew.
**Andrew Wilkins @ Elastic Observability** 35:03 Alright, thanks, Dmitri. Goodbye.
