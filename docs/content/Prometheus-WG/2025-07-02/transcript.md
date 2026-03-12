SIG: Prometheus WG
Date: 2025-07-02
Duration: 56 minutes
============================================================

## Zoom Recording Transcript

**Cyrille Le Clerc, PM @ Grafana Labs** 00:56 Hello!
**krajo Krajcsovits** 00:58 To close the blinds.
**Cyrille Le Clerc, PM @ Grafana Labs** 01:01 To be taught.
**krajo Krajcsovits** 01:16 Yeah, it's very hot in Hungary, and the sun is coming around and shining in. I can take. I need to turn on the A/CI try not to use it just to be like, you know, environment conscious. But like today and tomorrow, I think I'll just have to run it.
**Cyrille Le Clerc, PM @ Grafana Labs** 01:34 What temperature do you have in your home at the moment.
**krajo Krajcsovits** 01:38 I think it's around.
It got around 30 because I really feel it.
It's 33 outside feels like 34.
But yeah, tomorrow is going to be around 38, or 40 outside.
**Cyrille Le Clerc, PM @ Grafana Labs** 01:53 Oh!
**Arve Knudsen** 01:53 I have 30 degrees in my office.
**Cyrille Le Clerc, PM @ Grafana Labs** 01:58 In the room. You have 30. Yeah, it's unpleasant.
**Arve Knudsen** 02:03 I guess. Are, are we? Are we an exclusive club? Here.
**krajo Krajcsovits** 02:09 You know.
Yeah.
**Arve Knudsen** 02:11 I don't know about the I don't know about the others we have. We have air conditioning upstairs so.
**krajo Krajcsovits** 02:23 Got it right here. I just turned it on.
**Arve Knudsen** 02:25 Okay, is that panasonic? It looks like.
**krajo Krajcsovits** 02:29 Yeah, it was super expensive. But it's like.
**Arve Knudsen** 02:32 It looks exactly like the heat pump we have in Norway.
**krajo Krajcsovits** 02:38 Yeah, it's just regular A/C, with like heating option as well. But we never use it.
I meant, yeah.
**Cyrille Le Clerc, PM @ Grafana Labs** 02:45 Hopefully, we'll an alternative eating solution.
**krajo Krajcsovits** 02:50 Yeah, we are in blocks of flats. So it's like, kind of a small community or and we have central heating so. But if it that works on gas, natural gas, but if that fails, we can switch to.
Yeah, just maybe, although you know.
depends on where the gas is cut.
**Arthur Silva Sens** 03:16 Meanwhile it's below 10 degrees right for me.
**krajo Krajcsovits** 03:21 What? Where are you?
**Arthur Silva Sens** 03:24 South other side of the planet.
**krajo Krajcsovits** 03:27 Okay.
**Arthur Silva Sens** 03:32 Okay, should we get started?
I I noticed only I added topics, but if anybody else has it, I'm happy to skip some of mine.
**Revere Beach (us-cam-5cc)** 03:45 I have one topic. I just need to put it on.
**Arthur Silva Sens** 03:48 All right, then maybe I can start with my 1st topic, and you can take over the next. Maybe.
**Revere Beach (us-cam-5cc)** 04:01 Okay, so.
**Arthur Silva Sens** 04:04 One thing that we are noticing Grafana is that we are struggling to correlate. Customers are struggling to correlate metrics with hotel logs and traces.
**Revere Beach (us-cam-5cc)** 04:18 The way we are.
**Arthur Silva Sens** 04:20 Telling people to do it is to correlate service, name, service, namespace, and service instance Id.
Which are all resource attributes intermediaries. We have a configuration option that keeps it, but when translating from Otlp to Prometheus, but the default is that they are translated to Job and instance labels if they are translated. To Java instance, we lose the original resource attributes, and it's impossible to correlate them with logs and traces.
So we are wondering if this is something that we wanna promote in this pack and make sure everybody implements it. So all the signals are relatable.
Any thoughts on this.
**krajo Krajcsovits** 05:14 Do you mean to say that you would require always to keep these attributes?
Or what are you saying? Exactly.
**Arthur Silva Sens** 05:22 Oh, I would start with optional the sdks. The permits remote right export at the premises export, and the collector they have, at they at least have this option.
**krajo Krajcsovits** 05:37 And I would love to do this through this pack.
**Arthur Silva Sens** 05:40 So this configuration is.
It's consistent everywhere, and not only in Prometheus.
**Arve Knudsen** 05:51 Do you mean to make this mandatory.
**Revere Beach (us-cam-5cc)** 05:57 Is that what you're asking.
**Arthur Silva Sens** 06:00 I I would say optional, at least at that I would love that the option exists at least mandatory. I think I'm concerned. If it's a breaking change or not, Cyril.
**Cyrille Le Clerc, PM @ Grafana Labs** 06:17 So yeah, I prepared this with Arthur on. What came to my mind is that we already have this config flags that I like very much which is keep identifying resource attributes on. That is a feature to go to capture service, name, service, namespace, service, instance, id on target info.
on. Maybe we could expand the scope of this feature to also promote service, name namespace on instance, id on the metric themselves, and then make this config flag optional to start with on every exporter.
**Arve Knudsen** 06:54 But still that that overlaps with the promotion I mean you. You add those as labels via promotion.
**Cyrille Le Clerc, PM @ Grafana Labs** 07:04 But the prime of promotion is that it does not promote on it does not promote.
it. Yeah, it's not a config flag to get a service name service namespace on instance, id on target info. So maybe if keep identify identifying resource attributes in hotels, there are name namespace on instant Id, until, if we have a config flag, that is, keep.
it makes sense to me that it keeps on every Prometheus metrics, whatever they are these info metrics, or the metrics themselves.
**Arve Knudsen** 07:43 Yes, but I mean it. It has a semantics, I mean, it's a permit use parameter, and it has a semantics which is specific to targeting under screen tool.
But what I don't quite understand it is how how the spec is supposed to be updated. Wilson.
if if we update the spec. What is it supposed to do?
What's it supposed? What's it supposed to say? I mean.
**Arthur Silva Sens** 08:11 The the spec can clarify that the sdks and exporters have this configuration option.
**Arve Knudsen** 08:19 Okay.
Okay? So that that's what you're.
That's what you're asking.
I see.
**Cyrille Le Clerc, PM @ Grafana Labs** 08:26 In addition, what we discussed with Arthur is today. You have a a a misalignment or a difference of capabilities between the promitive Otlp endpoint that supports keep identifying resource attributes on the Prometheus exporter or the Prometheus remote right exporter in the hotel collector in your agent that don't support the equivalent of keep identifying resource attributes.
And so, if we may keep identifying resource, attribute part of the spec on saying it's also updating promoting on the metric itself that could be a solution to get back to consistency across all exporters.
and also to add this very valuable attribute, resource attributes maybe answer.
**Arve Knudsen** 09:20 It sounds as if it makes sense to to propose so that it so so that we achieve feature parity between hotel exporters and Prometheus Ltlp. Endpoints.
**Revere Beach (us-cam-5cc)** 09:38 Tweet.
I think it makes sense. Do we have a good like? I remember this was kind of added as like a Hey, here's a reasonable list of resource attributes.
Is that list still evolving? Or has that pretty much been like like? Are we happy with the current list? The only thing I wouldn't want is like to add this to Sdks at different points in time, and like, have 6 different lists floating around of what we think. The identifying ones are.
**Arve Knudsen** 10:07 I think I think you're referring to resource, attribute promotion. David.
**Revere Beach (us-cam-5cc)** 10:13 Well.
it. He's talking about the keep. Identifying resource attributes flag. Don't we have to choose which ones are identifying right as part of the the challenge with that.
**Arve Knudsen** 10:25 Okay. Okay.
**Cyrille Le Clerc, PM @ Grafana Labs** 10:27 And.
**Arve Knudsen** 10:27 Maybe I misunderstood you because I thought you were talking about the the list that we promote. Are you not talking about? Instead, which we consider identifying.
**Arthur Silva Sens** 10:37 Yeah, I think there's a confusion. I.
The Prometheus maintainers usually think as in the identifying the job. In instance, labels.
**Revere Beach (us-cam-5cc)** 10:49 Yeah.
**Arthur Silva Sens** 10:51 And then keep identifying resources. Builds is only about service, name, service, namespace, and service instance Id.
But in hotel identifying attributes is more related to entities is a totally different thing.
**Revere Beach (us-cam-5cc)** 11:04 Yeah.
**Arthur Silva Sens** 11:06 Poor choice of.
**Revere Beach (us-cam-5cc)** 11:07 Okay, that makes more sense. So this is just about adding service attributes to SDK. Prometheus. Exporters essentially.
**Cyrille Le Clerc, PM @ Grafana Labs** 11:17 3 service attributes among more.
**Arve Knudsen** 11:23 You know.
So the.
**Revere Beach (us-cam-5cc)** 11:30 That makes sense.
**Arve Knudsen** 11:31 I guess the thing to keep in mind is that, like like the starting point here is that Prometheus Otlp endpoint hard calls. These 3 resource attributes us, identifying. Maybe that clarifies it for you, David.
**Revere Beach (us-cam-5cc)** 11:50 Yep, yep know that.
**Arve Knudsen** 11:51 So.
**Revere Beach (us-cam-5cc)** 11:51 I remember now.
**Arve Knudsen** 11:53 There was a different feature, I think.
So that so that's point number. That's the like point number one here, so that that those 3 particular resource attributes are considered identifying by primitive otop input. Even even if not all of the hotel ecosystem might may agree.
So that's the 1st point. And the second point is that it? That primitive otop endpoint con translates those 3 attributes into job done, instance labels.
And so so they keep identifying resource, attributes it. It it makes Prometheus preserve the the those 3 resource attributes as labels on target info. So that's kind of like the. That's the semantics.
because because there are use cases where where users they kind of need to to. They need to to retain the the those original resource attributes and and not just use, not just use your job and instance. So that's sort of the problem being solved. There.
**Arthur Silva Sens** 13:03 And so if if we are happy with this change, we can start by opening an issue at the hotel specification repository.
and then we can discuss with the maintainers.
If this name is also make. If this name the name of the configuration option, also makes sense to them. I am a little bit concerned that they will ask to change because identifying attributes and hotel is different from Prometheus. But that's something that we can work with right.
**Arve Knudsen** 13:40 Probably so I I associate. I think it makes sense to kind of a if if I understand correctly, I think it makes sense to kind of achieve a parity between auto exporters and permitted. So, tlp.
that's sort of what you we're trying to achieve, right, Arthur.
**Arthur Silva Sens** 13:59 Yep.
**Arve Knudsen** 14:00 That Prometheus, when it converts audiometrics, it has this functionality, but other like hotel exporters, may not.
**Arthur Silva Sens** 14:12 Correct soup.
**Cyrille Le Clerc, PM @ Grafana Labs** 14:16 I am brainstorming with with some colleagues on how to correlate traces matrix logs, as Arthur said on We look mostly at Prometheus low key tempo. But there are other stores to store these signals.
and I would be very interested to understand if we have some surveys on what promiss practitioners use frequently to store logs on traces.
and I guess it could be helpful to have an understanding of what are the popular logs and tracer storage so that we can verify our hypothesis on how to correlate stuff together.
Maybe it's elasticsearch. Maybe it's Planck. Maybe it's Jaeger on typically, a problem. I'm working on at the moment with some other colleagues, is when a resource attribute is not defined like service namespace, because it's optional. People commonly don't use it to get started with on how to correlate, how to have visualization that supports both the absence or the existence of such attributes on different programming languages. Query, languages will have different requirements, so.
**Arthur Silva Sens** 15:37 I I think this is a little bit unrelated to the this group. But I I've done researches through the Prometheus website before we can come up with a form. We create a banner at the website.
People can answer through the website. If that works for you, I can. I can help you with that.
Okay? Srill.
can I ask you to open an issue for for this in the hotel? Spec I can have work with you on this.
**Cyrille Le Clerc, PM @ Grafana Labs** 16:09 Yeah.
Keep identifying resource attributes.
**Arthur Silva Sens** 16:13 Yeah, yeah, we we don't need to. We we can mention that for me just already has this this option. It's and it's named like this.
But we should focus more on the problem we are solving instead of like choosing the name.
**Cyrille Le Clerc, PM @ Grafana Labs** 16:28 Yeah.
**Arthur Silva Sens** 16:29 Yeah, our food.
**Arve Knudsen** 16:33 I just want to to ask whether resource attribute promotion is in the spec.
**Arthur Silva Sens** 16:41 Not not yet, but we want to to put it there as well.
**Arve Knudsen** 16:45 Okay, because keep identifying attributes is a very similar feature, and they work in primitives. They work in tandem because I guess, as sort of serene was saying that if you, if you enable, keep identifying resource, attributes you, you probably want to.
You probably want to promote the same attributes to to metric tables.
**Cyrille Le Clerc, PM @ Grafana Labs** 17:13 At least these 3 of these 3, yeah, which otherwise are not promoted. But then, when you do promotion, you are probably also interested in promoting Kubernetes, attributes, or host attributes.
**Arve Knudsen** 17:27 So.
Yeah, so I guess I guess just my point that if is that if if you're going, if you're going to make, if you're going to propose. Adding, keep identifying resource attributes to to the spec. We we probably want also to propose promotion right.
**Revere Beach (us-cam-5cc)** 17:46 I think the name might be a little funky, because, like, we're only dropping service resource attributes at the like scraper side. Right? It's only the Prometheus receiver or the Otlp endpoint on Prometheus. That's actually doing the dropping like for Sdks.
They don't expose Java. Instance right.
**Arve Knudsen** 18:14 I thought I thought we were talking about exporters. That convert autometrics to Prometheus metrics.
**Revere Beach (us-cam-5cc)** 18:24 Right. So like the SDK Prometheus exporters.
they behave like a Prometheus client, though right like you don't have a job and instance defined there you do have service, instance id on your target info metric.
But you don't have it like there's the dropping happens usually in the collector, or something like.
**Arve Knudsen** 18:44 Okay.
**Revere Beach (us-cam-5cc)** 18:45 When it decides to find those, convert it to resource, and then put them in and then change it to job and instance from service. Instance id.
**Arve Knudsen** 19:01 I see I'm not familiar with that list. I don't know if Arthur is, for example.
**Revere Beach (us-cam-5cc)** 19:07 Arthur, do you get what I'm saying like it makes sense for things that are receiving like the equivalent of remote right. But it doesn't make as much sense for things that are scrape or that are exposing like a Prometheus endpoint.
That's non-federated.
**Arthur Silva Sens** 19:24 But like, if we are exposing, for, for example, open metrics, format.
**Revere Beach (us-cam-5cc)** 19:30 We? Of course we don't add the job and instance labels to the metrics that I expose.
**Arthur Silva Sens** 19:37 That's added by default, by permitives. But we can expose service namespace service. Id right.
**Revere Beach (us-cam-5cc)** 19:44 We we could. So this, I guess maybe it's like.
maybe this is a request to change the name. If the idea is that we're going to add the service labels to all metrics.
Like, yeah, I think maybe just like the keep I keep implies that we would otherwise drop them, whereas this is something somewhat different.
**Arthur Silva Sens** 20:12 I, I agree that the naming doesn't make much sense in hotel context. So that's why I asked Cyril to to focus on the problem we are trying to solve. Instead of the name of the configuration option.
**Revere Beach (us-cam-5cc)** 20:26 Sure.
**Arve Knudsen** 20:34 Do they ex?
Do they? Do do this SDK exporters? David? Export sort of expose the target info metric.
**Revere Beach (us-cam-5cc)** 20:43 Yes, they do so. That will have all of your resource attributes today.
**Arve Knudsen** 20:48 It has all.
**Revere Beach (us-cam-5cc)** 20:49 Including sir.
**Arve Knudsen** 20:50 Is it.
**Revere Beach (us-cam-5cc)** 20:50 It's.
**Arve Knudsen** 20:52 Alright and and target info. Does it also have job and instance labels.
**Revere Beach (us-cam-5cc)** 20:59 No, so on SDK. Prometheus. Exporters like Prometheus clients generally. You don't put Job in instance.
**Arve Knudsen** 21:06 Okay, so then.
**Revere Beach (us-cam-5cc)** 21:07 Thank you very much.
**Arve Knudsen** 21:08 Okay? So they they don't follow. Follow this behavior like The job releases are part of the hotel spec for conversion to Prometheus metrics.
Does that not apply to the clients? Sorry to the SDK. SDK clients.
**Revere Beach (us-cam-5cc)** 21:27 It does not apply to SDK clients.
**Arve Knudsen** 21:30 Okay, yeah, I I really don't know. This is gonna be on my knowledge
**Revere Beach (us-cam-5cc)** 21:37 There is no dropin instance at that point to alright.
No, you're right. That is somewhat confusing.
**Arve Knudsen** 21:46 Yeah, because so this, this SDK clients, they they will generate target info from the hotel resource attributes.
But then then they would also they would be able to generate job and instance, same as Prometheus.
**Revere Beach (us-cam-5cc)** 22:07 In theory they could generate job and instance. You would then have to set like honor labels to true, when you scrape it, to not have that be overridden by your.
**Arve Knudsen** 22:19 Correct.
**Revere Beach (us-cam-5cc)** 22:20 Config.
**Arve Knudsen** 22:20 All right.
Okay, okay, maybe that's.
**Revere Beach (us-cam-5cc)** 22:24 It's a little weird, because.
**Arve Knudsen** 22:25 Maybe they'll see something.
**Revere Beach (us-cam-5cc)** 22:26 Really the intended use case of honor labels.
**Arve Knudsen** 22:28 Yeah, okay, maybe that's the issue here.
**Arthur Silva Sens** 22:33 But
**Revere Beach (us-cam-5cc)** 22:34 We.
**Arthur Silva Sens** 22:36 Is this something that you would.
**Revere Beach (us-cam-5cc)** 22:38 Try and be simple.
I'm sorry. Go ahead, Arthur.
**Arthur Silva Sens** 22:42 I was just gonna ask if this is something that you you think it's valuable to keep discussing here, or if we should discuss on the issue.
**Revere Beach (us-cam-5cc)** 22:51 I'm fine to discuss on the issue.
We've talked about it for 20 min.
I think it's just wording and stuff, so we can resolve that.
**Arthur Silva Sens** 23:01 Cool.
Alright. Do you wanna talk about your your topic, David?
**Revere Beach (us-cam-5cc)** 23:11 Yeah, sure. Well, it's kind of the same as your topic. So I lump them in together. But I tried to pick up your Otlp type unit label, Pr and I. I rebased it and had it open and then decided I didn't.
It seemed like a weird thing to do the implementation of the type and unit feature in the translation layer.
But that's really the only place we can do it, because after it's converted to remote right. v. 1. We sort of lose metadata, at least today.
So I talked with Bartek, and it seemed like it would be a good idea long term to have the translation go from Otlp to remote right. V. 2. Because most of the new features that we're implementing for Prometheus are getting implemented for remote right? V, 2, like, that's where most of the developments happening.
I implemented that over a couple days, and it turns out that, like the late, the way labels are represented, how they're symbolized and going like symbolizing. And then back from symbolized labels, is just really expensive. I've done some like profiling and benchmarking.
and it it almost doubles allocations. I've made some optimizations that bring the CPU usage down to essentially the same as the previous one. But there's still a pretty significant bump in mem, bytes and allocations like.
I think it's like 40%.
So my latest thought is that we should probably just.
I looked at the remote right handler code.
and it doesn't do very much. It's actually pretty simple.
like, in terms of feeding points to the appender. And right now, I kind of think that we should just write the translation layer to take an appender and that that will solve a lot of these problems. It does mean that, like, we will have to implement features separately.
like type in unit and so and I think, Arthur, to your question we should probably just in just add that to the translator, as is the way that you had it, and that I had rebased. So one of us can reopen that. Pr. But I'll probably start working on moving it to write directly to the appender, which probably won't be that much more work than what I've already done to be honest.
But I wanted to get people's thoughts and what like? The main question I want to answer is, what do we think the right long term implementation is? And then we can figure out how to make sure that we unblock the Delta working group and others.
so I'll open the floor for others.
**Arthur Silva Sens** 26:14 Right.
**krajo Krajcsovits** 26:15 Yeah, So I'm not sure what the right long term solution is. But I wanted to point out that at least, for now it would be nice to retain the option of using a conversion to remote right one with like additional features, because in Mimir we do need to like, send the data around usually. So it's not like we are writing directly to Tsdb, so we need something that is a carrier which is remote right one. Now.
**Revere Beach (us-cam-5cc)** 26:51 We use that package. The Otlp translator package directly.
**krajo Krajcsovits** 26:56 Or do you have a.
**Revere Beach (us-cam-5cc)** 26:57 Yeah, here we are.
**krajo Krajcsovits** 26:59 I think it's like copied to some extent from from promiss, but Arva would probably know better.
**Arve Knudsen** 27:08 Where are we using Ltlp translator.
**Revere Beach (us-cam-5cc)** 27:12 Be a mute.
**Arve Knudsen** 27:14 Yeah. The Mimir has has a fork of it.
**Arthur Silva Sens** 27:21 Think the there are 2 translators, one that translates names, and one that translates Otlp to remote right? I think what the one David is asking if Mimir is using the remote right translator.
**Arve Knudsen** 27:39 I mean me actually copies the the Otlp translation code from Prometheus.
**Arthur Silva Sens** 27:49 And then it uses its own for Cozlp translator, which should be as close as possible to the upstream.
**Arve Knudsen** 27:56 I don't know. If does that answer the question?
**Revere Beach (us-cam-5cc)** 28:00 So the question is.
I'll put it this way. I'm willing to do. I'm willing to either push forward and try and rewrite. Continue the rewrite of the Otlp endpoint to produce remote right? 2.0 instead of remote right? 1 point. Oh, I I think there's a few more optimizations. I can make that will make it less painful.
I can pursue those, or I can rewrite this Otlp Translator library in Prometheus to directly write to the Tsdb. Or like the right to the appender.
That will be significantly better performance than either the translation to remote right one, or the translation to remote right 2 but may make it harder for Mimir to reuse that code.
**Arve Knudsen** 28:55 Yes, I think I think that would make it significantly harder. But I mean.
are you sure you would do this in in the do you? Do you mean like the Otlp translator lib library? Or do you mean like if I can jump.
**Revere Beach (us-cam-5cc)** 29:10 Let me see this.
**Arve Knudsen** 29:10 Oh, yeah, the packaging permit is okay. Then I understand. Then I understand.
Yes, it. That would.
That would make it much more difficult for for Mimir. I don't think because what Mimir does is we we just copy the premises code automatically, and we we just refactor it on the on the command line to to to use mimere protobuf types.
So so we just like, do do we just do an automatic refactoring from Prometheus code to Mimi equivalents.
**krajo Krajcsovits** 29:47 Actually, maybe using Tsdb up. And there might be a way to get around that automatic conversion.
because if we had an upbender that built the remote right one from the input. Then you know it. Then you would depend on what upbender you are using, and the upbender is already an interface. So.
**Arve Knudsen** 30:10 Hmm.
**krajo Krajcsovits** 30:12 I mean It would be interesting to do a poc on on that.
Oh.
**Arthur Silva Sens** 30:22 I know that Jesus was when when he was working mostly on the Otlp stuff. This is something that he wanted to do for a long, long time, but never had the time to do it.
**krajo Krajcsovits** 30:34 Hmm.
**Arthur Silva Sens** 30:36 Maybe he he knows something.
**krajo Krajcsovits** 30:39 I'm sure he knows a lot.
**Arthur Silva Sens** 30:40 Yeah.
**krajo Krajcsovits** 30:42 No, because but I mean that would be an option, so that the translation from Otip Protocol to the storage is via the upender and the upender either writes directly to Tsdb or writes remote right? And then we reuse that.
I mean, I have to look at the code, but and that could be a way forward. Yeah.
**Arve Knudsen** 31:09 So you you'd be interested in doing I mean your Poc trial.
**krajo Krajcsovits** 31:12 Yeah, yeah, for sure. I'm already working on the remote right?
I mean the Otrp 2 remote right?
Translation, because we are missing the creative timestamp handling. We are currently doing this weird things and like.
I started working on it. And by just adding the creative timestamp to remote right one Protobuff definition, because it's backward compatible. You can just slap it on but that doesn't happen with metadata.
So what? What?
And I guess the does the appender? Yeah, the appender has metadata interface as well. Right open metadata. Would you use that.
**Revere Beach (us-cam-5cc)** 31:59 E.
I assume I would. I haven't looked at the appender interface, but I one sec. I'll double check. I have it open in front of me.
**Arthur Silva Sens** 32:12 I think it has update metadata or something like this.
**Revere Beach (us-cam-5cc)** 32:21 Yeah, update metadata.
**krajo Krajcsovits** 32:26 Hmm.
**Revere Beach (us-cam-5cc)** 32:28 Yes.
**krajo Krajcsovits** 32:33 I mean, as long as we're, you know, using some kind of interfaces, I think we should be fine.
So I I'd like to, you know.
I'll work on that with you, David, if you're if you're okay with that.
**Arve Knudsen** 32:50 Do you think we could kind of?
Do you think we could sort of like keep the the otop ingestion pipeline? We have now sort of hidden behind the appendra interface.
**krajo Krajcsovits** 33:05 That's what the Poc is about. I mean, I assume it's going to be fine, like you're moving data from one format to another. It's just the interface between the 2 is changing.
**Arve Knudsen** 33:15 Hmm.
**krajo Krajcsovits** 33:15 But like that's as far as I have, you know. Thought about it.
**Arve Knudsen** 33:22 I mean, if that's you don't need, that'd be great.
**Revere Beach (us-cam-5cc)** 33:25 If going to remote right, one should be trivial, because the append metadata, like where everyone just has, like a list of metadata, right?
going to remote right? 2 might be tricky because you need to reassociate metadata inside of time series. But you get a label Ref, which you can easily.
**krajo Krajcsovits** 33:47 Who would go to remote right to I mean right now. Nobody right.
**Revere Beach (us-cam-5cc)** 33:51 I I assume right. My assumption is that someday Mimir will want to support remote right, too. But
**krajo Krajcsovits** 33:57 We already re, we already I I implemented that we already support remote right to it converts to remote right one internally.
**Arthur Silva Sens** 34:06 I see. Okay.
**krajo Krajcsovits** 34:08 But you're right. I mean down the line. But actually the I also have to look at the interface. But like, I don't.
Yeah. That's you know. We'll turn that bridge when we cross it.
**Revere Beach (us-cam-5cc)** 34:29 We don't.
Okay, I'll I'll work on that. I will not be able to make much progress later this week because of the 4th of July. But, I'll start on it today. We'll see how far I go.
**krajo Krajcsovits** 34:44 Okay, I can take over. Then also, I guess we are in different time zones right? Like in different. You're in the Us. I guess okay, that works out fine.
**Revere Beach (us-cam-5cc)** 34:55 I still have 4 h left of work today.
**Arthur Silva Sens** 35:00 You look sad.
I'm just kidding.
I will reopen my old Pr. Then with the type of units, and then I can unblock Carrie and Fiona, with with the deltas.
**Revere Beach (us-cam-5cc)** 35:20 I think I had already rebased your Pr. Do you want me to just reopen that, or you can also.
**Arthur Silva Sens** 35:25 I can do it. No problems.
**Revere Beach (us-cam-5cc)** 35:27 Okay, you can do it.
Great.
**Arthur Silva Sens** 35:32 All right.
**Revere Beach (us-cam-5cc)** 35:33 All right.
**Arthur Silva Sens** 35:34 Next topic, spec changes. We have a lot I just wanted to recap of like.
see where we are and what's left to get them to finish to the finish line.
I have 2 2 spec changes and one pr. Of a Poc.
Looking at the spec change for the histograms, it looks ready to me.
so I wonder if it's just a matter of approving and merging.
**Revere Beach (us-cam-5cc)** 36:16 Did we decide if we were gonna scale down or a drop points outside the range.
**Arthur Silva Sens** 36:26 I think you made a good point. There.
**Revere Beach (us-cam-5cc)** 36:29 Right now it's unspecified. What you do with points that are outside the range. So dropping is allowed.
I could specify it as you have to drop it just means we have to update the spec. If we ever want to change that.
**krajo Krajcsovits** 36:44 Are you talking about the the I mean the scale or the schema between the yeah. So in the or is it d?
So in the promitives, remote right exporter, and by extension in the Otip endpoint in promitives. We already implanted the downscaling. So I think it would be kind of weird for people to not have the same experience the other way around.
Or do you.
**Revere Beach (us-cam-5cc)** 37:16 Wait
**Arthur Silva Sens** 37:18 Like prometues, remote right, explore, support, yet.
**Revere Beach (us-cam-5cc)** 37:23 So the the thing to keep in mind here is that only Prometheus has a limit.
The the range of scale that's allowed in the park call. So one way you have to scale down to abide by Prometheus's restrictions. But the other way, in theory there should be no need to scale up or scale down, or let's go down.
**krajo Krajcsovits** 37:45 But we are.
**Revere Beach (us-cam-5cc)** 37:46 But we're using special value.
**krajo Krajcsovits** 37:49 So so we are you. We are talking about Promi to store. Tell right.
**Arthur Silva Sens** 37:53 Yes.
**krajo Krajcsovits** 37:53 Okay. Sorry. Yeah. I'm like, I'm doing 10 things. And like, I'm getting confused.
Or maybe it's by age. I don't know. So we in the spec and also in open metrics, will reserve the schema values that are above 8 for future use.
So I don't think you should drop them So if we follow from Prometheus, right? So in theory, if it's.
**Revere Beach (us-cam-5cc)** 38:34 We can special case any of the other schema values in the spec later or like.
In theory, it should only ever be in that range right? We're talking about a case that Prometheus has said should be impossible.
with with exceptions, and the exceptions, is like minus 53, right.
**krajo Krajcsovits** 39:02 Yeah. So I, basically, last week I updated the native histogram in open metrics back. And and I talked to Bjorn, and we reserved the numbers from like minus 9 to I don't know 50 something. I have to look at the Pr. And those those should be fine, and the other. Anything else you can just drop until we specify the minus 53.
So I I would suggest to just look at the native program Pr in in open metrics, too, and you will see the range that we reserved. And I think if you take that as as input that should be good an otherwise dope.
Let me look it up for you. Just a sec.
**Arthur Silva Sens** 39:57 I'm I'm not understanding exactly where we're going. There. I I I understand that native Instagrams has. I think we reserve like 1,000 schemas in the Pr.
But we are no.
**krajo Krajcsovits** 40:15 Let me double check.
I'm so the schema, minus 9 to 52 are called standard express.
So this is the sentence that we have in the spec right now let me copy it.
Where is the zoom?
I don't get? Why, zoom sometimes minimizes, sometimes puts things somewhere else. Okay?
So, yeah, so this is it.
So if you.
**Revere Beach (us-cam-5cc)** 40:54 So good.
**krajo Krajcsovits** 40:56 Sorry. What?
Alright I I put it in the door.
**Revere Beach (us-cam-5cc)** 41:00 Yeah, thank, you.
**krajo Krajcsovits** 41:04 If I can find vendor, how this is.
Okay.
Thank you.
Right? So as the spec I mean, if you don't want to update the spec later, you can use this minus 9 to 52 number and say, drop anything else.
If you if you if you are okay with updating the schema. I mean the the spec, or like. Don't think that we are serious about this. Then just say, drop anything outside, you know.
Minus 4 and 8.
**Revere Beach (us-cam-5cc)** 41:42 Well, I guess right now it doesn't say anything right now. It just says if it's between 4 and 8, then you translate it to an exponential histogram and doesn't say anything else. So it doesn't tell you what to do. If it's 53 that that's my preference, because then it's not if you decide, if we decide that minus 27 is the new special value that we want to handle.
it's legal to implement that and do something different with it.
Right? Like. We're not forcing people to drop it right right.
**Arthur Silva Sens** 42:18 Living.
**Revere Beach (us-cam-5cc)** 42:18 We didn't.
**Arthur Silva Sens** 42:19 Specified as well, leaves the option for folks to decide what to do.
and if we decide something different in the in the future, that would be breaking changes, breaking changes to those who decided something differently.
**Revere Beach (us-cam-5cc)** 42:36 Right. So I guess it would be safest to say that we drop everything.
because then we can add something to the spec like it's non-breaking to say that you should except something that you previously dropped.
Oh.
**Arthur Silva Sens** 42:52 Yeah.
**krajo Krajcsovits** 42:53 Yep.
**Revere Beach (us-cam-5cc)** 42:55 But then, yeah, every time the open metric spec adds a new special number for something, we'll have to go update the hotel spec if we want to support it.
which is at least backwards compatible, but a little bit toilsome.
**Arthur Silva Sens** 43:11 It would be tilesome if we expect to add a lot of stuff in the future. Which I think we don't right.
**krajo Krajcsovits** 43:21 I would ex. I mean, there's 2 things in the future summaries.
probably. So the summary type. And we talked about a different kind of or at least, or maybe even 2 different kind of distributions based on on other parameters. So we have the standard exponential. But there are other ideas.
but they have been around for years. So Looking at how hard it was to add native storms.
I wouldn't think I think this would change like on on a timeframe of years.
**Revere Beach (us-cam-5cc)** 44:00 Okay. Then I think it's fine to say we drop.
**krajo Krajcsovits** 44:03 Yeah, I think so, too.
Yep.
**Arthur Silva Sens** 44:08 All right.
**krajo Krajcsovits** 44:08 Kind of right away. We will change it when we add the Nhcb. You know the custom buckets the minus 53, but at least we know that.
**Revere Beach (us-cam-5cc)** 44:16 Yep.
**krajo Krajcsovits** 44:17 Okay.
Cool.
**Arthur Silva Sens** 44:18 I was hoping that we could start a custom buckets right after merging this one.
Actually.
**Revere Beach (us-cam-5cc)** 44:25 What do you? Oh, a. Pr. About custom buckets.
**Arthur Silva Sens** 44:29 For the spec. Yeah.
**Revere Beach (us-cam-5cc)** 44:34 I would love to.
Hmm.
It's weird because it the custom bucket native histogram is only in which one is it in only in the proto format it. It's in the proto and remote right.
or where is it?
**krajo Krajcsovits** 44:51 It's in.
Well, it's in remote right.
It's not in any script format at the moment.
**Revere Beach (us-cam-5cc)** 44:58 Okay.
**krajo Krajcsovits** 44:59 So we, what we are doing is we're scraping the classic, whatever classic histogram. And then we are converting on the fly.
For now.
**Revere Beach (us-cam-5cc)** 45:07 I would love to just add, like a note like, if remote right to the in this in the histogram section, because, like the main readers of this document are going to be people writing SDK. Exporters.
**krajo Krajcsovits** 45:24 -
**Revere Beach (us-cam-5cc)** 45:24 And this is not really for them. So I would love to just make it like a footnote or a note somewhere that like hey?
You should translate for for this specific protocol and this specific schema number translate to an Nhcb, but it's like very protocol specific. When most of the document right now is trying to be protocol agnostic.
**Arthur Silva Sens** 45:51 Like we are working open metrics, 2 dot 0, which will have a native histogram representation. If I understand correctly, that includes custom buckets.
So we will have a exposition format. Right? Cryo. I see you doing this.
**krajo Krajcsovits** 46:10 Maybe we will have that sorry.
**Revere Beach (us-cam-5cc)** 46:16 Right. I thought it was just going to be a structured histogram rather than like a exponential, but with schema equal to 53, or minus 53.
**krajo Krajcsovits** 46:25 Yeah, I don't. I don't know. The native store on Pr on open metrics is huge, as you see, and there's like a thousand things to get through. I want to do this in a second step.
like I want And right now there, like, we hadn't identified the use case for it really, although Bartek mentioned it like a year ago already in Dev Summit. But yeah, I I think I agree with David that for now you should just say that it's for remote right, too. That's the official kind of way that you will get an Http right now.
**Arthur Silva Sens** 47:07 Alright, sounds good.
**krajo Krajcsovits** 47:15 Although if, since we are reusing primitives to scrape, you can set, promise to scrape whatever and turn it into an Hcb so you could potentially get.
So you potentially could get it there as well.
**Arthur Silva Sens** 47:39 I don't. I'm not sure if I got it. You mean the Federated endpoint.
**krajo Krajcsovits** 47:44 No, you use the promis receiver. That's promis right that has the promitive script code in it, and that.
**Arthur Silva Sens** 47:51 Yeah.
**krajo Krajcsovits** 47:52 Code. You can make it convert classic histograms into an Hcb. On the fly.
and then you will suddenly see an Hcb in auto auto collector.
Yeah, parameters. So it's actually not.
It doesn't have anything to do with the exporters.
I mean, yeah.
**Revere Beach (us-cam-5cc)** 48:13 If you turn on an Hcb. In the Prometheus receiver.
I thought we made it so that you get the exact same thing in terms of the Otlp like it's just a more convenient like. It just uses the append histogram path. I don't even know if we handle Nhcv. Today.
To be honest.
**krajo Krajcsovits** 48:30 Yeah, that's a very good point. Probably not.
**Revere Beach (us-cam-5cc)** 48:34 Yeah, I assume it's actually probably not.
**krajo Krajcsovits** 48:36 Let's correct.
Broken, yeah.
**Arthur Silva Sens** 48:41 All right.
**krajo Krajcsovits** 48:44 I mean.
You know, maybe an option is to just not say where it comes from, because then, like, if you never see it, then you never see it.
**Revere Beach (us-cam-5cc)** 48:56 Fine if we want to add a note somewhere.
That's protocol specific.
But yeah, if we can, I just don't want to confuse people who read it.
You could like a scheme with minus 53. And yeah, it won't apply to most most people.
**Arthur Silva Sens** 49:19 All right.
Anything else to discuss about this spec change.
if the next one is about the translation modes is the work that Owen and I have been doing for quite a few months.
Again I think it's in a similar to the native Hisgrams.
All comments were addressed.
I'm just wondering if it's there's anything in that I'm missing, or if it's just a proven version.
we don't need to review the Pr. Right now, like, if people need time to review. That's also okay.
**Revere Beach (us-cam-5cc)** 50:18 I'm I'm pretty sure I'll I'll approve it. But I'm gonna take another look.
**Arthur Silva Sens** 50:23 Yeah. And then, after your approval, is anything anything else that we need to do?
Or it's just your approval is enough to merge.
**Revere Beach (us-cam-5cc)** 50:35 I think usually you're encouraged to get 2 approvals. But hopefully, some of the other spec sponsors or Tc people will stop by worst case, I can just raise it at the spec meeting and say, I think this is a good thing to do.
review and and approve, and people will stamp it.
**Arthur Silva Sens** 50:56 i. 1 thing that I can see them asking is links to prototypes. I know that Prometheus already does this. So is the Prometheus enough as a prototype? Or do we need to open Pr test case.
**Revere Beach (us-cam-5cc)** 51:12 I think that's a good question.
It would be nice to have a prototype, but I I strongly suspect that this will be easy to implement in language sdks, we already essentially have the 2.
We we sort of right now have 2 independent config options, right like, Allow Utf. 8. And without units, and this is just changing it to an enum right.
**Arthur Silva Sens** 51:51 Yep.
**Revere Beach (us-cam-5cc)** 51:52 So I think it's okay to merge without without a prototype.
**Arthur Silva Sens** 52:07 All right.
I can also implement this in the collector.
Go. SDK, I'm not that familiar, but I can help alright. The the next. The last one is about a open Pr that I have for ages. I'm really struggling to get this ready. I am.
I'm not sure what I to be fair. It's been some weeks that I haven't touched this, but I remember that the collector would not even run with my changes, although the the unit test pass.
Kind of weird twest for help on on this. But yeah, I really need help.
**Revere Beach (us-cam-5cc)** 53:05 This generated code is out of date, run, make, generate.
**Arthur Silva Sens** 53:14 Yeah, the the the last. The last commit was, I think, a month ago, and the Pr. Was close and reopened, and then the Ci ran again.
I think I need to to rebase and we'll fix it.
But, like the problem is is, I am, I'm seeing some weird data databases when reading, reading some some maps like we definitely don't have time to discuss this, but like is Oh, I see, cryo has a raised hand.
**krajo Krajcsovits** 53:52 Yeah, I I've worked a a bunch of times on promiss receiver. So I take a look but that's going to be next week. Monday, Tuesday will be my open source days for the rest of the week. I'm looking at the creative timestamp and the and the Poc with David.
**Arthur Silva Sens** 54:11 Yeah, no problems.
**krajo Krajcsovits** 54:12 Okay.
**Arthur Silva Sens** 54:14 I'll ping you on Monday, Monday. Then I'll try to clean up this the the Pr. As well.
That's that's.
**krajo Krajcsovits** 54:22 Appreciate it. Yeah.
**Arthur Silva Sens** 54:24 Thank you.
Any other topics we have like 5 min.
Yep.
**krajo Krajcsovits** 54:41 Yeah, I wanted to like.
maybe I'm just a noob. But for some reason, you know, trying to compile the open to entry collector from Maine, and like from branch. I just cannot get it working like this. Open energy collector builder works fine if I'm like very close to the but I'm very close to a release like 1, 28. But like recently, I tried to build something with the with the fix, and it was just dependency help? What did you? What was that make auto country call? What? What does that do?
**Arthur Silva Sens** 55:27 This is a big file command that builds the collector.
**krajo Krajcsovits** 55:31 And that would that works better than the that.
**Arthur Silva Sens** 55:35 I, if I'm I, if I want to build the collector with the changes from Ipr, I just check out my branch and I run this command, and it works.
**krajo Krajcsovits** 55:47 Okay, perfect. I'll try that.
**Arthur Silva Sens** 55:59 Cool. If there's nothing else, I'll see you all in 2 weeks.
Thanks all for the discussion.
Bye-bye.
