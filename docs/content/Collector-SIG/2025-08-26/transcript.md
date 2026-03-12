SIG: Collector SIG
Date: 2025-08-26
Duration: 37 minutes
============================================================

## Zoom Recording Transcript

**Antoine Toulme** 01:04 Hello!
**Andrew Wilkins @ Elastic Observability** 01:06 Hello.
**So Koide** 01:07 I know.
**Antoine Toulme** 01:18 Where do we have to stand?
Okay.
Complete.
I got you here… Alright, please, if you get a chance, add your name.
In the dock here.
It's always great. It's great to see good attendance for this meeting so late, so… So, late PST, it's actually early.
It's your time.
So… It's great to see more people.
If you have any agenda items, add them in here. Right now, we have one.
Feel free to add more.
Okay, I'll just, read the first one.
So, this is an announcement which has been made by Pablo Bay and related to a component.
And I think I just messed up the block, sorry about that. So… … This is a standard operating procedure. Whenever we want to stabilize a module, meaning that we're going to go from beta to stable, which means that we will be making sure that the Go API of it is stable, does not change.
We make announcements on a variety of channels, including a SIG meeting, to make sure it's been addressed, that people know about this. If you have any reservations about this, please voice it on the issue.
And so Pablo just wants to make sure that everybody knows that he wants to, stabilize the config middleware module.
Well, that's it for this one. Feel free to go to the issue.
Ask any questions.
Andrew, you got….
**Andrew Wilkins @ Elastic Observability** 05:53 Alright, thanks. Yeah, so last time we all met, a few weeks ago, we talked about partitioning, so I have a processor proposal up, I've had it up for quite a while, about doing partitioning within a batch of data. So, for example, we might want to partition by trace ID or something else, and my proposal is to use OTTL to select the partitioning key.
… Dimitri made a point that this should probably be integrated with the partitioning support that's being added to Exporter Helper Batch Sender.
And I tend to agree with that, but if we're to do it with OTTL, that either implies that the partitioner needs to have support for extensions.
or OTTL, if we're… yeah, if we were to do it with OTTL. Either we need some extension support in the partitioner, or we need to have OTTL in core. … I raised that on the issue that Cindy has been working on, which is basically extending Batcher to support partitioning, and we haven't really made any progress. Basically, she understands that, we need to either do one or the other. So I'm just wondering if anyone has opinions on this, if moving OTTL to core is even something we would ever consider.
And if there's been any discussions about that. Dimitri?
**Dmitrii Anoshin** 07:22 Yeah, I think moving RTL to Core is something that we want to do in the future, but I don't think it's ready at this point, unfortunately. So, what if we have this partitioning as a Go API only, for now?
Like, you would provide some kind of a function interface that would, … Implement that, and we have implementation in country.
And for the user interface, it would be configurable only as a, let's say, experimental features.
And contribute for now, if that's okay.
**Andrew Wilkins @ Elastic Observability** 08:01 What does that… Does that mean each exporter would need to implement that function? How would you configure it, I guess, is my question.
**Dmitrii Anoshin** 08:10 Yeah, I, I mean, I mean, the… implementation, along with OTTL language in configuration interface, can live in Contrib.
And that thing, let's… it's gonna be a package that would satisfy the Go API interface that we implement on Core.
It means that it won't be able to use that implementation in Core.
So, for example, it would be some kind of an option with partitioning, similar to have with battery and everything.
And, it won't be able to have it… we won't be able to have it in core for now.
But only have it… like, for example, you would… you probably would like to have it in Elastic Exporter, right? Elasticsearch Exporter.
**Andrew Wilkins @ Elastic Observability** 09:00 Yeah, I get… I had in mind that it would be in all of them, anything that supports the batcher, it would just have some kind of extension configuration, but we can make it per exporter as well.
**Dmitrii Anoshin** 09:12 It's just the… not only this particular problem, it's how we, in general.
distinguish between stable and unstable APIs, and if we bring configuration interface to OTL… OTTL, configuration interface to core, it means that core configuration interface in general.
would be blocked by OTTL, going for 1.0.
**Andrew Wilkins @ Elastic Observability** 09:44 Yeah.
So, to be clear, what I meant was, the alternative would be, in core, we would have an extension point in the batch sender, and then we would implement that in an extension in… contrib. That extension would use OTTL, but Core doesn't need to care about that.
**Dmitrii Anoshin** 10:01 Yeah, it can be an extension, like, actual extension component, but I was thinking that we don't really need an extension here. It can be… we just expose an API, like, API… kind of point. So, like, I don't know, like, it can be interfaced called, … get partition key, or partition key, or wherever. And if you provide that kind of function, like that, anything that implements that interface to match your API, Export or helper API, And that would implement it.
**Andrew Wilkins @ Elastic Observability** 10:43 I think that sounds okay. The only problem, though, is we wouldn't be able to use it in OT… like, the OTLP exporter.
**Dmitrii Anoshin** 10:51 Right, that's what I'm saying. If we… if we was able to use it, it means that OTTL would block 1.0 work of the collector, because 1.0… Does need, exporter helper to be stabilized.
And if we bring it there, it means that, … we would… block 1.0 work by OTTL stabilization.
**Andrew Wilkins @ Elastic Observability** 11:24 Yeah, but not if we just do it with the extension approach, right?
If we have an extension in Batcher.
**Dmitrii Anoshin** 11:31 Yes.
**Andrew Wilkins @ Elastic Observability** 11:32 core… OT… OTLP exporter could use it, and then we can do everything else in.
**Dmitrii Anoshin** 11:37 Right, right, right. Yes, I believe so, yeah, I believe we can do it with an extension in that case.
**Andrew Wilkins @ Elastic Observability** 11:45 Maybe I'll open a separate issue to propose this, and then we can discuss a bit further.
**Dmitrii Anoshin** 11:50 Yeah.
**Andrew Wilkins @ Elastic Observability** 11:51 Tweet.
**Dmitrii Anoshin** 11:51 If you want… if you want it to be available in all of the exporters, the extension would be the….
**Andrew Wilkins @ Elastic Observability** 11:57 Yeah, I need to think about that a bit more. I'm not 100% sure if we need that. If we don't need it, then I agree that just having a Go API would be simple, and simpler, and ….
**Dmitrii Anoshin** 12:06 Producted.
**Andrew Wilkins @ Elastic Observability** 12:07 enough.
**Dmitrii Anoshin** 12:07 I was thinking if Go API is… like, we can have it as an experimental feature, and … for now, we can implement it however we want, and then we can change it in the future. It can be extension in the future, or it can be, like, actual OTTL embedded into it.
into the exporter interface. But if we go with extension first, there is no other option.
**Andrew Wilkins @ Elastic Observability** 12:36 We would have….
**Dmitrii Anoshin** 12:38 Go with that.
**Andrew Wilkins @ Elastic Observability** 12:39 Yep.
Okay, well, I'll think about some more, see if there's actually a need for that.
**Dmitrii Anoshin** 12:45 Your filters….
**Andrew Wilkins @ Elastic Observability** 12:46 exploit.
**Dmitrii Anoshin** 12:46 Feel free to ping me in Slack, I'm maybe not… quickly to reply on GitHub, but if Slack, I will….
**Andrew Wilkins @ Elastic Observability** 12:55 Sounds good. Okay, thank you.
That's all.
from me.
**Antoine Toulme** 13:09 Next up, Kiyosuke.
**Kyosuke Kariya** 13:15 Yeah, thank you, so… Can I share my screen?
**Antoine Toulme** 13:20 Of course, you… go ahead.
**Kyosuke Kariya** 13:22 Cute.
Yeah, so… not this one.
Can you see the diagram?
**Antoine Toulme** 13:33 Yes.
**Kyosuke Kariya** 13:34 Okay, okay.
So this one is about the, this pull request, this one is about the enrichment processor. So, what it does is enrich the attribute based on CSV data or JSON data, and a related issue is… This one, the new component enrichment processor. So, and as described in here, this one is kind of type 2 and type 3 enrichment for the attribute.
So, I mean, the reference data lookup and the dynamic external… dynamic external enrichment?
And… … Also, this one is related to, I think, this one, and reach attribute based on the key matching of Yamo Power CSP definition.
And… there is similar, … I forget where it is, but someone created the lookup.
Processor, which can enrich the… attribute based on CSV file using one index.
So what I want to propose here is… … this… Enrichment processor, which again, the functionality is almost same, but, this one's… the architecture for this, processor is like this.
So… Inside the enrichment processor, there is 3 types of components, data source and the enrichment rules in the enrichment store.
So… We separate this component because… Sometimes we want to get the data from the local file, or HTTP, or some kind of way, so we segregate the data source, and also how to store the data, and this enrichment… and we store the data in this enrichment store, and… Also, we, this enrichment rule to, you know, sometimes we want to say, There he is.
Maybe… Oh.
Oh, shit, wait a sec.
Processor… Yeah, so say… We have telemetry, like… We are.
Like this one, so… There's, you know, of course.
one… I mean, this one is the one data point for the metrics, so if one data point has a name, then sometimes we want to look up the, you know, CSV file by hostname at the data center.
But sometimes we have another attribute, to… We want to use another attribute to look up.
So, we create this, you know, under the enrichment rules.
So, the configuration I'm proposing looks like this. So, there is two sections, data sources.
And also enrichment rules.
So, data sources for… how to… You know, get… those data to enrich, the CSV or JSON.
now this component just supporting CACP and JSON, maybe… future, we can support YAML, but… and… so, this is how to collect data.
And this is… How to enrich.
the data.
So, we can define, which data source I'm in.
Which data source we will use for this enrichment, and also which… Field to look up, and which attribute key to look up.
And… Which, field.
To, you know, enrich the attribute, and what is the key name for that one?
So… And currently, in this implementation, everything, the… all data of the CSV file is loaded to memory. Yeah, so… Dmitry, am I pronouncing your name correctly?
**Dmitrii Anoshin** 18:27 Yeah, I… if I… that's okay to ask questions right now, I'm just… don't want to interrupt you.
**Kyosuke Kariya** 18:34 Of course, of course.
**Dmitrii Anoshin** 18:35 Yeah, the question, you're looking at attributes, it doesn't specify which particular attributes you're… is it data point attributes, or resource attributes?
**Kyosuke Kariya** 18:46 So, I'm planning to support both.
….
**Dmitrii Anoshin** 18:49 What was the reason? Because, like, it's… data point attributes should not… like, if you add additional attributes to data point, it doesn't change the FTS and etc. What's the point of adding that to… because this seems like a resource enrichment, not a data point or look record enrichment.
**Kyosuke Kariya** 19:11 Mmm… Why do we need data point enrichment?
**Dmitrii Anoshin** 19:21 Yeah, that's what I'm.
**So Koide** 19:24 Yeah, for example, data center should be a data attribute, right? Not a resource.
**Kyosuke Kariya** 19:29 I don't want to….
**Dmitrii Anoshin** 19:30 Data centers.
**Kyosuke Kariya** 19:31 Resource attribute. Data center.
**Dmitrii Anoshin** 19:33 Exactly.
**Kyosuke Kariya** 19:36 Mmm….
**Dmitrii Anoshin** 19:39 Also, I would encourage you to look into the entity work that is happening in OpenTelemetry, because… like, first of all, it's likely resource enrichment, we shouldn't… because if it's resource enrichment, it's gonna be same logic, exactly same logic applied to all of the signals, so it will be much easier to implement, and….
**Kyosuke Kariya** 20:02 Yeah, true. But, you know, sometimes, so, in our use case.
One database server containing the multiple, … Database?
And those databases are owned by the, you know, different team.
So, we want to, you know, enrich the attribute based on, you know, not resource attribute. I think that one is, … The data point attribute.
**Dmitrii Anoshin** 20:31 So you would, like, for example, it would be the case if you have metrics, particular MTSs per data center, and then you have data points per database, which typically is not the case. Typically, you have metrics peer database. So you have, I don't know how, like, database, read, writes, whatever. So it's pure database, and you have another entity associated with that would be data center, and another entity, like, I don't know, region.
And all of those are resource attributes. And resource attribute, speaking in old terms of Ubuntu Lem, the new terms would be entities. So I would encourage you to look into that, because, like, you would probably need to implement this with entities in, … From the beginning, because otherwise it has to be added going forward anyway, because we will have to support entities for all the components.
**Kyosuke Kariya** 21:32 What do you mean by entities?
**Dmitrii Anoshin** 21:33 Yeah, you can take a look at the results, and upon the line to a specification, there is, like, it's a new working group, and there is a note tab for that, and everything. So, yeah, I suggest you do some, like, some investigation about that.
And, yeah, definitely, I don't believe, like, there is any reason to complicate that and go to log record, data point level, etc, because….
**Kyosuke Kariya** 22:04 Hmm… I see.
**Dmitrii Anoshin** 22:06 You're enriching NGTS with some additional metadata, as far as I understand.
**Kyosuke Kariya** 22:11 So you mean, say if there is one database server and multiple databases inside there, so we need to….
**Dmitrii Anoshin** 22:21 Yeah, is that.
**Kyosuke Kariya** 22:21 There is, like, exporter… For each database, you mean?
**Dmitrii Anoshin** 22:26 I'm sorry, can you repeat the question?
**Kyosuke Kariya** 22:28 So if there is a database server, and we have multiple databases in there, we need to, you know, create the exporter 4… Each of the database?
**Dmitrii Anoshin** 22:41 No, you don't need an exporter. It's… Like, if you are aware of OpenTelemetry.
data model. An open telemetry signal, every, every signal in OTLP, it starts with the resource, resource fans, then resource management.
**Kyosuke Kariya** 23:02 Coach spans.
**Dmitrii Anoshin** 23:04 So, and that data is sent to whenever it… it doesn't… Doesn't have anything to do with the exporter.
It's just how we represent the data, and how we enrich the data here.
**Kyosuke Kariya** 23:17 Well, sometimes, you know, when we use the exporter, … No one defines which attribute we will use to resource the attribute, and… if we use one exporter for one database server, and that one contains multiple database, I think the one used for all the Oh, wait a sec. Maybe I'm misunderstanding. Okay, let me take a look.
Mmm… Okay, then I will clarify what is the use case for this one. Thank you.
**Dmitrii Anoshin** 23:54 Sure. And another suggestion I have here, to simplify it a bit more, so you have data sources to specify where you're taking the… actually, where are you scraping… … data source… So you referenced that data source somewhere else, right?
**Kyosuke Kariya** 24:19 Yeah.
**Dmitrii Anoshin** 24:20 data sources, and then you reference them. Okay, yeah. So, here you can actually have Instead of having another section called data source, you can actually use config sources here.
So, for… for example.
We have this thing called config sources, when you can expand particular parts of the configuration.
with, other, like, sources, let's say. So instead of config service inventory, you would say, … like… Dollar sign… bracket, then you would say your URL, I believe. We have different config providers, and one of them being S3, for example, another one would be HTTP.
So you can reference section you can, yeah, you can replace a section of one configuration with some references outside of this, and the reference can be HTTP, S3, etc, so look for config providers.
That would potentially just replace the whole section you would need it.
**Kyosuke Kariya** 25:34 I see.
**Andrew Wilkins @ Elastic Observability** 25:38 Dimitri, wouldn't that resolve once?
We're….
**Dmitrii Anoshin** 25:41 No, it's open.
**Andrew Wilkins @ Elastic Observability** 25:42 Periodically?
**Dmitrii Anoshin** 25:42 It depends on the config source. I believe we do support periodic reloads for some config sources, as far as I understand.
But we don't support it for file, for sure.
But I think for HTTP, we might support that, so we would need to check that.
**Kyosuke Kariya** 26:09 Okay, thank you, then, you know, let me clarify, you know, use case for the… I mean, the data point, or each individual level enrichment, whether those enrichment is required, I'm a little bit confused whether, you know, which information should be resource attribute, and which will be… Individual attribute by, you know, exporter.
So… Okay, thank you.
**Dmitrii Anoshin** 26:37 Sure, thank you.
**Kyosuke Kariya** 26:42 So, and… can I go to another one?
**Antoine Toulme** 26:45 Sure.
**Kyosuke Kariya** 26:46 Thank you. So… next one is about the goodby attribute connector. This one is just, you know, proposal for the new component. This one is related to the, these… issues. So this one is originally, originally from the unable to, you know, set XScope org ID, I mean, the tenant ID, dynamically, using header setter extension, for the… Or maybe. Attribute, I think?
Which I think each… Long record, or… Wait a sec… Sorry, I need to clarify here, but… … So this one is for setting the tenant ID from the resource attribute, In my underst… when I proposed this one, … This is for… extracting tenant ID from attribute, or both attribute, I mean the resource attribute, or each… individual attribute?
But… Yeah, so… we need to… we need the discussion here, maybe just resource attribute is enough?
But, why I'm proposing this is… The… now the look exporter is deprecated.
And look exporter has functionality to, … Rebatch the request based on the attribute.
So that we can select, you know, 10 and 30 dynamically.
But now the Look Explorer is deprecated. And we're planning to use this feature, so we need an alternative. So that is why I'm proposing this one.
I'm proposing this one as a connector, because, the processor cannot create the, you know, … P-logs logs, or Ptrace trace, multiple P-logs.logs.logs, or, you know, this level instance.
And… No… for… after… Nope.
decommissioning the low key exporter, I think the alternative is OTLP exporter. And in OTLP Exporter, it is using the… it is creating a HTTP request based on one instance of this component.
And… tenant ID header… go ahead.
**Dmitrii Anoshin** 29:33 Sorry, I didn't want to interrupt you, you can finish if you want, but I believe I just want to say that this is something that Andrew is looking as well.
**Kyosuke Kariya** 29:42 Oh!
**Dmitrii Anoshin** 29:42 I just discussed this. This particular use case, actually. Andrew, can you clarify if that's correct?
**Andrew Wilkins @ Elastic Observability** 29:49 Yeah, exactly, I was just waiting for Kioska to finish.
So, I mentioned before partitioning, we're… I'm looking into exactly the same thing. So, for example, we want to… Route… Data….
**Kyosuke Kariya** 30:06 So we use the Kafka exporter, for example, and we want to send Kafka data to different.
**Andrew Wilkins @ Elastic Observability** 30:13 Topics, but we might want to extract certain data within a batch of data send that subset of the data to one topic, another subset to another topic. So, my proposal is to use OTTL to extract a partitioning key from the data.
we might end up with multiple batches of data, each with a different partition key. And that partition key could be a topic… a tenant ID, for example.
And… and yeah, then you could use that with OTLP Exporter, or Kafka Exporter, or whatever.
But I'll link an issue in the chat in a moment, but we're looking to something very, very similar, if not exactly.
**Kyosuke Kariya** 30:56 I see.
Oh, thank you, thank you. I need to take a look.
on that one. I do not know. There is… those kind of similar issues. Yeah.
Thank you, yeah, so just let me finish, just… this one is for selecting tenant ID dynamically, and re… Budgeting based on this… P logs, P trace, P metric level.
So that we can just use the header setter extension as… You know, now how we are using it, because header setter extension is… You know, implemented by the roundtripper, which is inserting, header when we… create, … HTTP request?
So… I think if you have this type of connector, like, creating Multiple… P-logs from one P-Log, then we can just reuse the header setter or OTLP exporter to you know, have the same functionality with the Loki Exporter, so… That is what I wanna propose, but… If there is a similar issue, please share it. Yeah, happy if you share the one.
**Andrew Wilkins @ Elastic Observability** 32:17 So, Kosuke, I, added a link in the chat.
**Kyosuke Kariya** 32:21 Oh, thank you.
**Andrew Wilkins @ Elastic Observability** 32:22 issue that I opened. As we discussed earlier, this probably wouldn't go ahead as it is described in that issue, but we may have an extension or just configuration in the exporters, we'll see. The other thing that I had proposed is to add support to the… to the transform processor.
**Kyosuke Kariya** 32:45 For doing metadata level.
**Andrew Wilkins @ Elastic Observability** 32:48 changes. So, there's… are you familiar with OTTL already?
**Kyosuke Kariya** 32:52 No, no.
**Andrew Wilkins @ Elastic Observability** 32:53 Okay, so OTTL, or the transform processor, can operate at different contexts, so….
**Kyosuke Kariya** 32:59 ODTO is… do you mean Transform Processor?
**Andrew Wilkins @ Elastic Observability** 33:02 So this transform processor, and it uses something called OTTL, Open Telemetry Transformation Language.
**Kyosuke Kariya** 33:08 language,
**Andrew Wilkins @ Elastic Observability** 33:09 And it can operate on different levels, context levels, so one may be at the resource level, then it may be at the, … Like, the level of a span, or a metric, or a data point.
And also instrumentation scope, but it doesn't have the capability to operate on a… A batch, which is, like, the….
**Kyosuke Kariya** 33:33 I see….
**Andrew Wilkins @ Elastic Observability** 33:35 the resource… sorry, the metadata level. So you can't inject… you can't inject headers. That's something I have proposed additionally. If we had that in the transform processor, then you could Manipulate the, the client metadata and inject additional headers.
So I think that.
**Kyosuke Kariya** 33:51 It would be needed again as well.
Are you planning to create the multiple plog.logs, I mean, for example, if… We are dealing with logs. Are you planning to create.
**Andrew Wilkins @ Elastic Observability** 34:03 That's what the partitioner would do, yes.
**Kyosuke Kariya** 34:06 Interesting. Is it processor? Is it possible to create the multiple P-Logs.logs by the processor?
**Andrew Wilkins @ Elastic Observability** 34:12 Not curr- no, no, not currently, so, ….
**Kyosuke Kariya** 34:15 Yeah, right.
**Andrew Wilkins @ Elastic Observability** 34:17 So the processor I proposed would… But the way it would work would… would be that… It would split a batch into multiple batches, and then it would concurrently send each batch to the next consumer.
The partitioner, if we do this in the batch sender, we would do something similar.
We'd, we'd split it, and then….
**Kyosuke Kariya** 34:42 Is it new component, like… Processor or exporter, those levels?
**Andrew Wilkins @ Elastic Observability** 34:47 That's part of… that's part of core in the Exporter Helper.
**Kyosuke Kariya** 34:49 Oh… Particular. Oh… That's something that's been in development recently.
I see.
Thank you, then… yeah, obviously we need to use that one.
I think, don't… maybe… same… Completely same topic.
**Andrew Wilkins @ Elastic Observability** 35:09 I'll, I'll comment on your issue, and just so with… so they're linked, and then if anyone… Comes across that they can… they can, … Provide their own opinion on which way to go.
**Kyosuke Kariya** 35:22 Thank you.
**Antoine Toulme** 35:36 Alright, awesome, thank you. … Is there anything else?
Happening.
Another topic? Any other topics that you'd like to discuss, folks?
**Andrew Wilkins @ Elastic Observability** 35:52 If anyone here cares about overriding telemetry providers, I have a PR up on Core Collector that's waiting for a review.
Basically the gist of it is… I've separated the interface from the implementation of telemetry in the service package.
I'm now supporting… working on abstracting the interface so you can create multiple provider implementations.
Yeah, if you have time to review, that'd be great.
And if there's any changes I can make to the PR to make it easier to review, please let me know.
**Antoine Toulme** 36:30 You're good.
**Andrew Wilkins @ Elastic Observability** 36:33 Thanks.
**Antoine Toulme** 36:40 Alright.
Going on 3.
1, 2… Sri?
Thanks, everybody. Have a great day, have a good night. Take care.
