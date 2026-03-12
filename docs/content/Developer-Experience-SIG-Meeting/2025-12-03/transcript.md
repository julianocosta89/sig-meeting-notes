SIG: Developer Experience SIG Meeting
Date: 2025-12-03
Duration: 46 minutes
============================================================

## Zoom Recording Transcript

**Juliano Costa | Datadog** 00:46 Hello, hello.
**Damien Mathieu** 00:54 Looks like we are not getting increased down today.
**Juliano Costa | Datadog** 00:58 Okay. I haven't checked the Slack yet.
**Michele Orlandi** 01:10 No, I'm on.
**Juliano Costa | Datadog** 01:15 Hello, Pavel. Hello, Michelle.
**PL Pavol Loffay** 01:18 Hello, everyone.
**Juliano Costa | Datadog** 01:20 Michele… I'm not sure how to pronounce her name, sorry.
**Michele Orlandi** 01:23 Yeah, that's… that's right. That's right.
**Juliano Costa | Datadog** 01:26 Michele?
**Michele Orlandi** 01:27 Yes, I'm from Italy, yes.
**Juliano Costa | Datadog** 01:31 Bongiorno.
**Michele Orlandi** 01:32 So… Where are you guys from?
**Juliano Costa | Datadog** 01:35 Austria?
Well… I'm from Brazil, but I live in Austria, yeah.
**Michele Orlandi** 01:40 Oh, okay.
**Damien Mathieu** 01:42 Prints and firm prints.
**Juliano Costa | Datadog** 01:48 Cool.
So… Usually, we do not have many… folks other than Damien, myself, and Tristan in the call.
So let's start a bit different today. Pavel, Mikel, is there something you guys would like to discuss, or are you just joining to see how the SIG goes, and what we are doing?
**PL Pavol Loffay** 02:17 Yeah, I have, one agenda item to discuss here on the call. There is a proposal in the community repo to… To start a new SICK for the MCP server for OpenTelemetry. And… there's been some discussions in the… in the GC, about whether this should be a separate SIC, like a standalone one, or should it be part of other SICK that we already have in OpenTelemetry.
The… the reason for being… part of existing SIG is the MCP server will most likely… or the implementation will be most likely in different parts of the ecosystem, so there will be maybe some MCP parts in the collector.
then maybe there will be standalone MCP for the configuration use cases and instrumentation. But what we are trying to do, and what we need to solve, is to find a place for the MCP SICK, and Not sure if you're aware, but, yeah, they tried to propose to have the MCP SICK in the developer experience.
or kind of discussed the MCP things in the developer experience seg. So I wonder if you are aware, or if you saw the request, and what are your thoughts?
**Damien Mathieu** 03:49 I personally was not aware, Yeah, I don't think we have anyone… involved in the SIG, also involved in MCP, so… Yeah, I would… I personally, very personally, have strictly no interest in anything AI-related, so I'm not interested in helping there. But maybe it makes sense, maybe it doesn't, If it's just the three of us, the DevEx, as we have been so far, we definitely don't have the bandwidth.
**PL Pavol Loffay** 04:29 No, it's not about, kind of, putting more work on your shoulders, it's about finding a place where people that are interested in building MCP capabilities in OTEL could meet and have, kind of, a common place to collaborate, right? So it's, like.
We are trying to find, like, kind of official body in OpenTelemetry to host our… our agenda, let's put it this way. The…
**Michele Orlandi** 04:58 OpenLLEM entry. Would that… would that be a good place, maybe? In the OpenLeometry SIG? I don't know. Just, it's a question.
**PL Pavol Loffay** 05:09 Yeah, yeah, I don't know either. I think the developer experience was proposed because the whole idea of the MCP server is to… simplify… work or simplify user experience with OpenTelemetry, right? So what it can do for you is… It can configure the collector, It can instrument your application, It can really kind of simplify all the day-to-day tasks that we do for maintaining, you know, telemetry pipelines in our organization.
**Juliano Costa | Datadog** 05:53 I… I do see some overlap on the… on the goal of the developer experience sig. The… My main concern is that we have some ongoing things that we are currently working.
So, just to give you a couple of context. So, we ran a survey at the beginning of the year, asking users what were their pain points whenever using OTAL and whatever.
the initial goal was to focus on SDK, but the results of the survey showed that users were struggling more on getting real examples of hotel collector in, like, how to deploy the collector in production, what recommendations and stuff. So, from the survey, we decided to run a couple of end users, interviews, and then write about it as… So, this kind of overlapped a bit with the proposal from Dan, the blueprints thingy. But, like, this is a… already an ongoing thing. We already have done 6 or 5 interviews, so we are in the write-up process to actually get this, published.
And, to be honest, I don't know what would be our next steps. I don't think we have, decided that, Damien, right?
**Damien Mathieu** 07:31 No, we have not, but I, wanted to discuss the hotel blueprint, thing, just after.
**Juliano Costa | Datadog** 07:38 Yeah, so… with that, I'm not sure… I'm not sure if we should… bring the MC… again, I do see a area where we… Where both SIGs, kind of, converge.
And the idea of simplifying onboarding of Votel?
So, yeah, I'm in the fence.
**Damien Mathieu** 08:08 Yeah.
I think maybe where there is a way is, if the work we have started is, moving towards the Hotel Blueprints project, then maybe what we have already started can, like.
slowly, or not that slowly, move, into the end user SIG, for hotel blueprints.
And then maybe the DevExec can, onboard the MCP project.
**PL Pavol Loffay** 08:39 end users.
**Damien Mathieu** 08:41 For hotel blueprints, not MCP.
Thanks so much.
**PL Pavol Loffay** 08:46 Sir, can you maybe.
**Damien Mathieu** 08:48 What I'm saying is, the work we're doing right now, the idea is we're doing it now, which is interviews for blog posts with, end users of, open telemetry to, like.
basically, as Juliano said, to better help people who are struggling with OpenTelemetry by showing them how others are doing it.
that's the approach that we've taken now. But our long-term vision is that we should not own that, because it's really an end-user thing. So we are kind of kick-starting it at the moment, and are seeing us, like, off-ball it to the end-user SIG, who would probably be better owners long-term, for VAT. Then, with the Hotel Blueprints project kicking off, maybe, we can start offboarding VAT to Hotel Blueprints slash end user, like, sooner.
And then Weitmin Swissik could onboard the MCP project.
**PL Pavol Loffay** 09:52 So which sync could onboard the onset.
**Damien Mathieu** 09:54 Devix.
**Juliano Costa | Datadog** 09:55 us.
**PL Pavol Loffay** 09:56 This one, okay, this one. I think it's a very valuable, problem that you are looking at, and it's… it's aligned… it's literally aligned to what we are trying to do, right, with the MCP server, is to simplify user experience when they are onboarding, either collector or instrumentation or SDK, or they deal with data operations.
For instance, there is, like, a lot of… the collector, it moves quite fast. There is a lot of changes in the components, there is a lot of changes in the… in the configuration.
Oh.
And users, A, don't know even what components to use in some cases.
and B, the… it's hard to catch up with all the changes across the versions, right? And… the… I build a proof of concept for MCP, and there is a lot of things to improve in Autel, like, there is no, like, schema for the collector component configuration, which is, like, a very fundamental feature that the collector should have, right? Because otherwise, as an end user.
how I'm gonna configure the collector. I need to… right now, I need to literally, like, look at the source code, right, to the config object, and understand what is there.
So yeah, so there's a lot of things… to be done… to support the MCP well, But I think what is as well very important is to understand these issues that you are looking at, like, what users actually are struggling with, because we can take this as an input for the MCP to design the tools and the capabilities it will offer.
Right? Because it's the same workflow, it's just gonna be enabled for the AI agent to execute.
there is, so there is this proposal, and I, as well… I work for Red Hat, I'm maintainer of the OpenTelemetry operator.
And some parts of the collector. I've been working in OpenTelemetry for… since the beginning, I think, and… In the operator SIG, we are very close to the end user as well, so if there is something broken, we sometimes see it first, because users will… they use operator, right? And then, if something fails, they will go to our project and open the ticket.
And what is even worse for us is we do the collector, but we as well do OANP, we as well do instrumentation, right? So users can deploy a collector, can configure instrumentation, so it's, like, entire open telemetry stack, and we are sometimes flooded with a lot of issues that we… even we don't know how to solve, right? Because I don't maintain Python instrumentation, and if they change something, for me, it's… equally hard to understand what has changed. So the scope is large, but we need to find, I think, a good programmatic approach how to enable users to manage AutoStack with ease.
**Juliano Costa | Datadog** 13:26 Yeah, I've seen the MCP proposal before, you sharing here.
I follow closely the hotel… Ripple, so, yeah, I was already… I missed the notification to the developer experience approvers, but, like, the proposal, I got it. And I do, again, I do think it fits here.
maybe it's just the timing, but I think it will take some time to actually… the proposal to actually be approved, right? It goes through GC, and .
**PL Pavol Loffay** 14:14 Yeah, I think… I don't… I should meet with them as well. What we have right now is, kind of, initial set of ideas, what we want to build.
what kind of user workflows you want to support, right? Like, one is to configure the collector as a day one operation, and then to manage it over time, you know, change the… like, enable a user to catch up with all the changes in the collector config to, you know, spot deprecated fields in their configs that they're using, and things like that. So we have that initial Goals, which obviously can change as well, based on your input, what you think, what you find out is important.
And then we have, sort of, sort of.
Users, not users, sort of developers that would like to help build it.
Right, so there's a bunch of people that already built MCP for a hotel in their… their projects, and… they seem to be keen there on the proposal. They would like to join, and… And help this, initiative to… to create something.
Which is, I think, great, because, like, many times it's hard to find people that like to actually do the work.
Sometimes we have… A lot of, kind of, requests, but very few volunteers to actually help to maintain and build.
**Damien Mathieu** 15:59 What would be… the next step, I mean… we… I don't think we can just say, yes, we're going to take this on right now. So should we talk with the folks involved in the MCP and see if that would make sense to… for them to join VSIC, or… How would you like to proceed?
**PL Pavol Loffay** 16:22 We can… so there is another, on the proposal as the project lead for the MCP, there is one guy from Ollie Garden that would like to help a lot, because he's building their product as well.
So we can… I can talk to him, and maybe we can join next week, or on your next meeting, to… to discuss what we… what we want from you, right? I think… Mostly what we will need is… is the common place to meet and discuss, and I don't know how, kind of, full is your agenda, and there will be, you know, time in the meetings to kind of have a scene for the MCP, so that's maybe one thing that we will require, and then collaborate with you as well. As I mentioned, like, all this research that you did is probably a very valuable input for us to… To understand, and then we can… kind of implement these capabilities in the MCP, because, again, it's… The same workflow, pretty much.
**Damien Mathieu** 17:34 Yeah, I mean, yes, that sounds good to me. We will definitely add it to the agenda, then, for next week, and ensure that at least I'll be there.
And maybe Tristan and Giuliano.
**Juliano Costa | Datadog** 17:53 Yeah, I'm adding some notes to the agenda. I don't know if Tristan will take a look at that, but, our…
**Damien Mathieu** 18:00 I'll… I think I'll post on Slack.
**Juliano Costa | Datadog** 18:02 Oh, okay, cool. And we, we also have, hotel-devX Slack channel level, so we're free to join.
**PL Pavol Loffay** 18:12 Okay, I'll already share it there as well, so people can have a look, before the meeting, and if there's any, like, kind of follow-up questions.
**Juliano Costa | Datadog** 18:21 Awesome.
**PL Pavol Loffay** 18:23 I see there is as well a meeting today in the evening, like, 8pm. I'm based in Europe as well. I'm not sure if that's a good place to as well join and give, like, a heads up.
**Juliano Costa | Datadog** 18:34 So, basically, this… it's the same SIG, but we… we run twice, one in EU time zone and one in the US. I haven't seen folks join the, North America time zone in the last… 3 months, so I'm not sure… I'm not sure if… There will be anyone there.
But, yeah. Yeah, I'm not.
**Damien Mathieu** 18:58 I'm sure the U.S. meeting is very much attended. To be fair, I think this SIG is, a bit… not unmaintained, but struggling to find interested folks in joining it. So maybe doing the MCP project can give it a second, breath, and kick things back on again.
I think we are, like, it's different approaches, but it's the same thing, as you mentioned. Providing an MCP server is a good way for folks to get started easily by using an LLM.
We have taken the documentation approach and interviews approach, but the ID, I think, is similar. It's to provide ways and tools for folks to To, yeah, better, quick start.
**PL Pavol Loffay** 19:54 Yeah, yeah, it's just… it's the same thing, just in a programmatic way.
**Damien Mathieu** 19:58 Yeah, different, different, for different brains, I suppose.
**PL Pavol Loffay** 20:04 Awesome, yeah, it's good that this city is as well, like, in Europe.
**Damien Mathieu** 20:08 Yeah, I've, I've posted on Slack, and, we, will be happy to share, to discuss it more next week.
**PL Pavol Loffay** 20:16 Awesome. Thank you.
**Juliano Costa | Datadog** 20:18 Awesome. Thank you.
**Damien Mathieu** 20:21 Michele, did you have something that you wanted to bring up, to this sig?
Or were you joining out of curiosity?
**Michele Orlandi** 20:29 Oh, yeah, well, I'm joining just out of curiosity, but in reality, now I remember why I had this curiosity, and oh, sorry, do you want me to turn on my cam?
**Juliano Costa | Datadog** 20:45 If you feel comfortable about it, we don't mind.
**Damien Mathieu** 20:48 Yeah, that's up to you.
**Michele Orlandi** 20:50 Can you see… can you see me?
**Juliano Costa | Datadog** 20:51 Yes, you're at the beach.
**Damien Mathieu** 20:53 Yes, very nice outset.
**Michele Orlandi** 20:55 Okay, okay. Yeah, so, Yeah, I remember now why I'm… so I'm using mostly… I've been using OpenTelemetry, so I don't know if this is the right one, because this is more development, so I don't know if I'm more of an end user, but, well, I do develop, but not in OpenTelemetry, actually, but, Actually, just to, yeah, just to cut it short, I have this, use case coming up next, where I need to, like, do, like, an end-to-end transaction, follow-up of, of a transaction that is going through multiple, applications, and so we… I need to do, like, a workflow, and have, like, a trace ID in OpenTelemetry, hopefully.
that I can… unique trace ID that I can trace back to the same… initial transaction. It's like a document workflow.
It's for a… it's actually for a… it's for a client project.
So, I don't know if this is the right, maybe it's more of an end-user question.
But in any case, I was just curious to know how to implement OpenTelemetry. Well, I've been using mostly on Instana.
And, but mostly just the HTTP endpoint.
And so, I was just curious to know… I was following the podcast on, I think it was Don Orovitz, or the guy from Israel, he was talking about open LLMetry. Also, that would… was kind of interesting to me. I don't know if this is the right, if it's the right signal, I might be… I just chose this one, because I was free now, and I like development, and I'm based in Europe, so… But I'm just happy to, you know, listen to you guys, or… I was looking… I find very interesting the… I looked at the example that you posted, Pabel, on the MCP… hotel, I think it would be very interesting to have, so, something that can actually configure open telemetry For you.
But, yeah, mostly I'm just interested in the… Also, what the semantic, rules mean.
So, maybe… Yeah, that's it, basically, and…
**Juliano Costa | Datadog** 23:53 Okay, I think we have a bunch of questions here, but I'll try to go over. So, like.
When we say developer experience, we actually, aim on end users, so you would be on the right place.
The goal of the SIG, though, is… improve the end user experience whenever using OpenTelemetry. So, like, the developers that are using OpenTelemetry, the goal of our work is to improve that workflow.
Okay, but then going through one of… a couple of points that you… you brought up, I think you have an end-to-end, application that you would like to track the transaction, and… as long as you instrument everything with hotel, and… I don't know, depending on how you are instrumenting your code, the… let's say that you are doing auto-instrumentation, or using instrumentation libraries.
the context will be propagated between services, and then you get, like, the same trace ID for all the requests going through. So all these spans will be part of the same trace. So then, linking all the spans to one trace. This is something that hotel kind of… brings to you.
**Michele Orlandi** 25:23 Out of the box, yeah.
**Juliano Costa | Datadog** 25:24 Yeah, exactly. And when we talk about distributed tracing, if you don't If you don't have proper context propagation, then, distributed tracing is worthless. So, this would be one thing.
Then, I don't know if you are asking us about, like, how to test that, because then this would be, like, the other way. But you also mentioned that you were sending in to Mistana, but another great point of Hotel is that OTEL produces OTLP, which is the OpenTelemry Protocol, and most of the vendors out there support OTLP nowadays, so you can basically send OTLP to anywhere.
If you want to do some processing in the data before sending to a vendor, you can also use the collector, or the project that Pavel shared, the OpenTelemetry Operator.
And the operator would even, like, take care of auto-instrumenting a couple of languages. So all the languages that have, like, auto-instrumentation, the operator would take care of Doing the instrumentation for you.
**Michele Orlandi** 26:41 Okay, sorry, Pavel, did you… the operator, did you… I can… yeah, I can look for it, I can Google it, because I think you posted only the stuff about the MCP.
**Juliano Costa | Datadog** 26:55 But I can, I can look, I can, I can search it, I can search it.
Well, I think if you navigate to OpenTelemetry, github slash open dash telemetry, then you are, like, you can find everything there.
What else? Did I miss any… any…
**Michele Orlandi** 27:19 No, the question is, how does OpenTelemetry know, for example, if I have a transaction starting from a document server, and then it's going to, like, an integration server, and then it's going to… for example, an LLM, well, in my case, you might have guessed it then from IBM, in, in What's the next, whatever, AI… How does it, link… no… how does it know that it's coming from the same transaction? Is there a way… is this what the operator you would be doing in the operator place?
**Damien Mathieu** 28:06 No, the way it works is, it's, there is a standard in W3C which is called trace context, and, basically, that standard defines how, trace, data is passed around components.
Especially around HTTP requests. So, you will have a specific HTTP header passed to every request. OpenTelemetry does that, the passing and the reading. You can see there are propagator interfaces in SDKs that will allow you to define custom ones if you wish.
And… in HTTP requests, it's going to pass the VAT trace context for other systems. It's also going to pass them. Like, if you are using Kafka instrumentation, it's going to add that to the message headers.
That's how, when you create a span, you can know which parent it has, even if it's coming from a different system.
**Michele Orlandi** 29:06 But, okay, yeah, sorry, actually, we are using Kafka in this project. But do I have to, do I have to specify within Kafka, a Kafka, that, do I have to configure that, for example, within Kafka, or is it, OpenTelemetry is out of the box, is recognizing that,
**Damien Mathieu** 29:32 I don't think… Kafka itself does an instrumentation. What's going to happen is, if you add instrumentation to your app, then anything that adds data to Kafka is going to also add that metadata to messages, and everything that reads from Kafka is going to get those messages and also get that tracing context.
But, I don't think Kafka itself is instrumented, so you wouldn't need to add anything to Kafka itself. It's just to the applications. And the way you add instrumentation on Kafka really depends on your language.
**Juliano Costa | Datadog** 30:11 There is a caveat there, and something that you may face later, is that… If you do parent-child, so, like.
service A, called Kafka, and then, service C.
consume the message from Kafka, and then if you do A and C are together, like parent-child.
then you may get, like, a gap in your trace, where this time was spent in Kafka. So you never know how, you never know when the consumer will actually consume the queue or the message. And this, will just kind of… whenever seeing the trace, you may see this gap. In hotel, what we recommend for messaging is creating spend links. So, when the producer produces the message.
It ends the trace.
But it passes the information via context, and then whenever the consumer is reading this and creating and doing whatever it needs to do, instead of, creating it as a child of the incoming request, it creates as another trace, but it links these two traces together. So you can navigate from one trace to the other, but they are not part of the same trace.
**Michele Orlandi** 31:41 And…
**Juliano Costa | Datadog** 31:42 But again, this is, like, a second two problems. The two problems.
**Damien Mathieu** 31:46 Most instrumentation libraries will do that for you.
**Juliano Costa | Datadog** 31:49 Yeah, exactly.
**Michele Orlandi** 31:52 Oh, so I should get all this out of the box, basically. No, nothing, no… I don't need to… I mean, this context thing that you were saying, I don't have to configure that, I guess. I'm not sure which application… there's probably some enterprise application, for example, that is on top of Kafka, for example, in this project, but… for example, I… we have, integration bus, which is another IBM application.
And this has, like, an open telemetry, output connector thing.
And, so I have to check, if, If this is actually, going to propagate, and, I can see… I understand what you were talking about, the traces, when there is, like, a gap between traces, because… I was looking for a screenshot, I have a… I have a similar… I had a similar example.
In… in another… with another integration tool.
And, for example, in, because there was a component in this, that was not being monitored by, was not being seen by OpenTelemetry, so there was, like, an empty space between the traces.
**Juliano Costa | Datadog** 33:28 Yeah, so this… in this case, you have an uninstrumented service, but, with Kafka, it's not… it's not about not having a, missing a service. In Kafka, it's actually the time that the… the… The message or the queue is… staying there in Kafka till it's processed. So… depending on your configuration, let's say that you do, like, batch processing once a day. So you'll have a bunch of, messages being sent, and then this Processing will only happen once a day.
So, you don't want… you don't want to have… you don't want to have, like, a one-day-long trace with a bunch of batches being processed just at the end of the day.
You would split that into two different traces, and then whenever you are doing the batch, then you link to the… whoever created the messages.
this is just an example, but yeah, this is, as Damien said, you will get out of the box if you're using instrumentation libraries that are available. So, if you rely on Java.NET, PHP, JavaScript, Python, What else do we have, all to its rotation, Damien?
Ruby…
**Michele Orlandi** 34:56 Yeah, Rust, maybe?
**Juliano Costa | Datadog** 34:58 No, then you're…
**Michele Orlandi** 35:00 Oh, no, I guess?
**Damien Mathieu** 35:02 It's not that there is nothing, it's that, like, for REST and Go, there is no metaprogramming, and so auto-instrumentation cannot really be done, because in, like, in JavaScript or in Ruby, it's going to inject things, on your behalf.
And Go and Rust cannot do that. I mean, in Go, we can do it, but with eBPF, it's a bit different. And so, there is no auto-instrumentation there. It's, plugins that you connect to your app, but you have to add them manually. Like, for HTTP requests, you have to manually add a middleware.
**Michele Orlandi** 35:39 Yeah, yeah, yeah, like a library. Additional libraries.
**Juliano Costa | Datadog** 35:44 Yup.
And for us, depending on the framework you're using, you may need to do it manually.
So, I think for us, the only instrumentation library we have is Actix Web.
And then, other than that, you were, like, on your own?
**Michele Orlandi** 36:07 Yeah, actually, I don't know why I mentioned Rust, I don't even have any.
**Juliano Costa | Datadog** 36:11 Oh, okay. Then you're okay.
**Michele Orlandi** 36:13 Yeah, yeah, yeah, yeah. So, okay, Probably, for example, yeah, going back to Kafka, what would be if I didn't have any, now I'm thinking about, yeah, there is this IBM application called Evan Streams.
I don't know if it has, if this one has a collector. It's like a… it's a wrapper around the Kafka.
What would you suggest that I put, on top, or… or… to… to instrument Kafka, for example, if I didn't have any, any co- any, you know… plug, or open telemetry, that I can… that I can connect to the OpenTelemetry collector.
Like, you're right, rightly so, you said earlier, I think it was Damien?
That, basically, Kafka itself cannot be instrumented.
Is there, like, a… maybe there is, like, an application, Java application, that, Yeah, could probably… there's… they could… that can… Provide this, What's it called?
They're…
**Damien Mathieu** 37:44 I mean, there could be Kafka plugins, I don't know. I'm not saying that Kafka cannot be instrumented, I'm saying that, by default, Kafka is…
**Michele Orlandi** 37:53 instrumented.
**Damien Mathieu** 37:54 with OpenTelemetry. Maybe Kafka has plugins that can do that. I have no idea about that.
**PL Pavol Loffay** 38:01 There's, like, think about Kafka as a database, right? It's like a system that you use to store and read data from.
And… when you… For tracing use cases, you are interested in understanding when you read and when you write, right?
from N2 Kafka. So you instrument only these entry and exit points, and this is essentially your client in your application Reading and writing, so your client needs to be instrumented, not the Kafka. If you were to instrument the Kafka itself.
you would probably would like to understand what the Kafka is doing, like, what are the internals of Kafka doing?
And this is a different kind of… data. This data would help you to kind of debug the issues inside the Kafka and optimize the Kafka, which is something you probably don't want to do, because you are not trying to optimize your database system, right? It's not a database, but… yeah. For instance, there is a tracing in Cassandra, you can enable tracing, it will give you trace data.
But it's not valuable for a normal user, because a normal user doesn't understand, you know, the Cassandra code, and it shouldn't even kind of debug the internals of Cassandra, right? Normal user should only understand when it writes and reads from a database.
So think of it this way, like, every tracing integration happens in your application, so your application needs to have Code to generate trace data, so you need to use these instrumentation, auto-instrumentation libraries.
**Juliano Costa | Datadog** 39:52 Basically, the data that you get out of hotel is… or the data that is important to you, that you get out of hotel, is the data that you can act on.
So, like, if you see, like, a query that is taking too long, for instance, in a database scenario, the query is on your application side and not on the database. If… if you get the internals from Kafka or from Cassandra, as Pavel said, you won't be able to go to Cassandra and fix it. This is not… owned by you. I mean, if it's an open source tool, maybe you can send up PR to fix something, but I don't think that's what you are actually looking for.
So, you just take care of instrumenting your application, and then, everything else will just, Give you insights on the things that you can… Improve.
**Michele Orlandi** 40:49 Yeah, it's kind of, yeah, it's kind of… in this way, in this sense, it's kind of like an Instana Datadog application performance, what's it called, APM.
Yeah, yeah, so it's focused on applications.
**Damien Mathieu** 41:01 It's exactly the same thing, except it's open source, it's not proprietary, and so.
**Michele Orlandi** 41:07 Don't work out.
**Damien Mathieu** 41:07 And, it's basically all the vendors working together.
**Michele Orlandi** 41:11 Yeah, yeah, yeah, yeah, yeah, yeah, exactly.
**Damien Mathieu** 41:12 on proprietary UIs rather than proprietary agents.
So, Michele, I'm thinking that if you have further questions, maybe the end-user SIG would be better for you. I think, they have more, folks asking those kind of questions.
If you have, like, specific SDK language questions, there are also specific, language agents, SIGs.
You probably want to ask on Slack before joining their SIG meetings, because the SIG meetings are more for, development of the SDKs, rather than, like, getting started, even though we'll probably be happy to, have a user. Yeah, is there any further question?
**Michele Orlandi** 42:06 No, no, no, no, that's it, that's it for me, thank you.
**Juliano Costa | Datadog** 42:12 Awesome. Cool. So… Damien, regarding the work that we are doing, I haven't heard anything back from Masudon.
So I'm not sure here if I… I will try to reach out to Hano and see if he can… Ping… ugh.
team internally, maybe I get some… some luck?
And, yeah.
**Damien Mathieu** 42:41 I need to ping them, too, because, I agreed to co-lead the Hotel Blueprints, project, with, sorry, I forgot, his name.
So I agreed to call it the Hotel Blueprints project, and we want to reach out to them to ensure we also have reference architectures to leads, to point in Hotel Blueprints.
Okay. So I need to check with them and the others that we've interviewed so far.
But yeah, I… if… if it doesn't answer, I'd also reach out to Bruno.
**Juliano Costa | Datadog** 43:16 Okay, okay, so that.
**Damien Mathieu** 43:18 I hope it doesn't come to that, but I will also be at FostDem, and Rono will be at FostDem, I'm pretty sure, so, but I really hope that we can get an answer before February.
**Juliano Costa | Datadog** 43:30 Yeah, I'll be there as well. Well, I don't know if I'll attend phones them, or only the hotel.
**Damien Mathieu** 43:37 I'll be there, the full time, all three days.
**Juliano Costa | Datadog** 43:41 Cool, okay, yeah.
Are you joining, Pavel? The… the hotel unplugged?
**PL Pavol Loffay** 43:48 I don't know yet.
**Juliano Costa | Datadog** 43:50 Okay.
Cool.
**PL Pavol Loffay** 43:52 I would like to, but, let's see.
**Juliano Costa | Datadog** 43:55 Awesome.
Yeah, I'm always, pushing, Austin to get hotel events in EU. I hope we get, like, sold out and fully booked rooms and, like.
I mean, I hope that can…
**Damien Mathieu** 44:12 I, I hope, Hotel Unplugged can be, the start of maybe having a, an observability dev room at FostDam next year.
**Juliano Costa | Datadog** 44:23 Yup.
**PL Pavol Loffay** 44:25 Was it removed this year? There used to be observability, the rule.
**Damien Mathieu** 44:29 There, isn't any this year.
**Juliano Costa | Datadog** 44:33 there's no.
**Damien Mathieu** 44:33 Yeah, I've not seen any in the CFP. Maybe because there is Hotel Unplugged, they maybe even made a choice. I didn't know there was one for years before.
**PL Pavol Loffay** 44:41 There was, usually grafana was organism.
**Damien Mathieu** 44:44 Yvet didn't have enough, attendance, or talks, proposals?
**PL Pavol Loffay** 44:48 It was packed. I was there… I wasn't there last year, or… well, this year, but 2 years before, it was packed, always.
**Damien Mathieu** 44:57 Yeah, like, for the search room, for example, I mean, Elastic is interested in that room. I think we have a lot of folks in the CFP, I think, and it's like, there are 7 talks and 10 proposals, so it's… Yeah.
We're a bit disappointed.
**Juliano Costa | Datadog** 45:21 Yeah, there was, I think, on dev rooms, just performance, application performance, or something like that, that could fit some observability talks, but yeah, not the same as having an observability dev rooms. Yeah, I agree. I was also sad, to not see it there.
But anyways.
**Damien Mathieu** 45:44 Okay.
**Juliano Costa | Datadog** 45:46 That's it from my end. Not… nothing… nothing else.
**Damien Mathieu** 45:50 See you all next week, then.
**Juliano Costa | Datadog** 45:54 Thanks, Pavel, for the link.
Fair.
