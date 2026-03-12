SIG: Arrow SIG
Date: 2025-07-24
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**albertlockett** 00:36 Hey, guys.
**Drew Relmas** 00:43 Hello!
Later on.
**Michael Salib (F5)** 00:45 Hey!
**Laurent Quérel** 00:53 Hey, guys.
can you hear me?
**David Dahl** 01:13 Yeah.
**Laurent Quérel** 01:14 Okay, great.
Yes, we can wait a little bit for Joshua.
I encourage everyone to to add their name in the that on this list, and and optionally add some item into the agenda Drew or Jake. Do you know if Joshua will join today.
**Drew Relmas** 02:57 I actually do not. I've not heard from him.
That's okay.
**Laurent Quérel** 03:03 Account. Yeah.
**Jake Dern** 03:04 Yeah. I was chatting with him yesterday a little bit, and it sounded like he was going to come. But I haven't heard from him this morning, either.
**Laurent Quérel** 03:11 Yeah, I don't see him connected on on slack.
So so I suggest that we start without Joshua. It's already 8 4.
Okay, so hi, everyone I was not present during the last 2 weeks, so I don't know if there are some pending questions in previous agenda. Let me know if that's the case.
Okay? So I guess there, there are no questions. I remember one question from from Jake, but that has been answered regarding the the the behavior of the the Gpc. Protocol on which we are relaying for the hotel protocol.
So for people that don't know.
I created a documentation describing the the values, changes and solution some of them have been implementing in the go implementation. And some of those. Are interesting approach that could go further in terms of improvement, resolving challenges or inputting performance in general, any question on that or comments.
Okay, okay, let's look at the the agenda. So I put a 1st operational a demo of the 1st operational Mini pipeline.
So that there is an unapproved Pr, but ready for review. Let me share my screen. That will be, I think, or someone is already sharing a screen.
Perfect?
Okay? So I can share my screen and show you resizing the windows for you will, it will be a more comfortable to read. Okay, so the oldest Pr, this one on which I work now for many weeks.
Basically, that's the 3rd round of implementing the the data flow. Engine?
So we already have a lot of pieces individual pieces. We have a value. So Tlp, receiver, exporter processor or something for tap.
There are efforts to now converge to a single P data abstraction, so that we will have a single type of pipeline with different type of countries and different type of output.
And can you put output? And and now we we have at least we validated an approach where for us.
having a pure otip pipeline.
and in parallel a pure tap. Pipeline does not really make sense because we have a conversion, otlp, to a tap that is either very close in terms of performance for the visualization, or even better, for bigger batch. And we we have a strong I personally strongly believe that we we could be faster and then much faster for value size, even medium sized batches.
So in that case that would simplify the the creation of this one gene, because we would not have to support different type of P data. A single type would be enough.
So the but that's not what is in this pr in this pr, there is, still the option to there is a parameter for the pipeline, and this parameter is a P data type. And and right now, we we basically have in this Pr 2 type of pipeline pipeline with otap batch and a batch and we have values component nodes as they are named into the configuration file implementing value things. And and you can obviously combine in in this peer.
That would no longer be the case later.
But the you can combine only Otlp based nodes with Otlp based pipeline, similarly same thing for tap.
so this Pr is able to.
So basically what this Pr is doing. Take a configuration file.
so for people that were not necessarily present from the beginning of this project. The the idea is regarding configuration for this system.
Obviously, we want to be compatible with Google collector in terms of configuration.
But at the same time we want to be able to support some more advanced capabilities in the pipeline definition.
So we? We have a superset configuration model.
We have a configuration mode that is a superset of the go collector configuration with them.
and we will implement translators to translate.
The go collector configuration file into this superset configuration file right now, this convert translator converter does not exist yet, but unfair way that should be possible.
So we we have this configuration file. I can show you. Let's see some example.
In fact, in the Demo, you will that you will see this configuration file more clearly. But here it's just a representation of this configuration. But you will see the the Jason, the corresponding Jason configuration. The Yaml is not done because I didn't implemented it yet, but it's it's a it's a no brainer so in this pipeline. So we have a pipeline config builder. So if we want to inter to to use the configuration in a more programmatic way, we have this pipeline config builder, and we can add receiver exporters. We have different type of node and we connect them. In that case we connect the otlp receiver with an otlp exporter.
I could spend more time on on the the meaning of those values things, but right now we'll just go to the. I just want to go to the the very high level overview and then we we build the the configuration we get a pipeline config and and basically we, we use this there is this concept of a pipeline factory with a build method. And and then we get from the config. We get a runtime pipeline something that is able to to to be let's say, to to run into a Tokyo runtime or multiple Tokyo runtime.
And then we started So so that's basically what we have. We have a way to define the configuration. We have a way to translate, but to to desire to interpret this configuration, then we have a way to interpret the configuration and and when we and there is a better description there when we once the the configuration file has been read and converted into rust.
Scripts. There is.
let's say, a builder of this pipeline one time that will analyze the topology of this pipeline and basically, the system is analyzing each tuple of nodes that are interconnected together by an hyper edge.
More specifically, one one node, that is the the node that is at the source extremity of the hyper edge and one or multiple nerves at the destination extremity of this hyper edge.
So the Api is something that could have one source and multiple destination. And what we name a dispatch strategy?
What is the behavior? Basically of the message traversing this hyper edge? Is it some kind of phone robin to the destination some kind of random distribution, or is it something that will broadcast and the message will be duplicated for each destination?
This kind of a behavior can be defined with the the hyper edge mechanism that we introduced.
And so the system take the dog.
Analyze the topology, extract each tuple of source and destinations analyze the configuration. Do we have both side? Only local nodes.
the one that are able to run on a single threaded runtime without synchronization at all? Or do we have one of those nodes on both extremity?
Which is something we name shared, node.
or shared exporter share something. That will require synchronization. And then we need to do some wrapping mechanism around that and and depending on on this configuration.
If we have local. Everywhere. We can use channels that are purely local without synchronization, super fast. If we have one of those components that is shared, then we have to. We the the engine switch automatically to a different implementation of the of the channels which is compatible with this type of constraint and and there are various other consideration that the at this point of time, the the system that is building the the runtime pipeline will do to decide exactly the the correct configuration. The type of channel also is decided at this point.
and then we we get a fully connected dag of features features that represent each of the the nodes connected with channels.
and then the the next step is assigning individual task for each of the the node of this dag and then, and that is started inside. In this current implementation a single, single, a single Australia Tokyo and gin.
we don't. In this Pr create one engine per core. But that's the next step. It's not a big deal. My goal was. It's already super huge in terms of Pr, so I decided to to stop the the work there and but that's multiple limitation. The the limitation, I think, are summarized. Maybe I forgot some of them. But right now there is no controller that will start multiple engine one per core. It's just one core and there is no controller. Basically, it's just the low, level interface. There is no support for hyper edge with broadcast strategy. Mostly because I need to do some evaluation of broadcast channel and and and there are some subtle complexities there, because what happened if one of the destination is slower or does not answer. What is the impact on the rest of the destination, and how the retry mechanism will will will be combined with that. But that's something that will be included later.
And there is currently also no support for more than one output. Port so back to this concept, I think it's could be valuable if I let's see.
can create a new, a new file.
I like to show you the so what is an exporter in this specific engine.
It's mess with me.
An exporter is always there is a control channel.
Year.
Yeah.
Okay, okay with you. And there is a P data chin in.
So for an exporter, and obviously we could have. It's not necessarily the case, but something that the exporter itself define in terms of my screen just is now black. Okay, back?
So sometimes you have an external an external on 3 pounds.
which is well, what happened with my screen?
Sorry guys?
Okay, that's so. Sometimes you have some external entries like a socket Tcp, Udp, whatever.
But sometimes you don't. For example, what is doing right now. The the fake fake signal generator, which is a also it's not an exporter. It's a receiver. Yeah.
so this fake signal generator is a receiver and there is no external entries. It's basically just generating signal from a configuration file.
So we we have now policy soils processor and and the processor the main difference is, there is a second channel.
and there is an abstraction on that. But there is basic. No Oh, look, no, I don't know. I don't. I'm not able to use a receipt shop today.
so p data channel.
**jmacdonald** 20:31 Lauren. I think the there's a teams or or a zoom bug here happening here. Your screen hasn't changed much.
**Laurent Quérel** 20:39 Oh!
**jmacdonald** 20:40 I say teams, because this was happening in teams earlier this week for me as well. And so, hey, everything's broken.
**Laurent Quérel** 20:46 Okay, so let me reshare maybe
**jmacdonald** 20:56 While you do, you're reminding me that the the go collector does have mechanisms for for what's called fan out. And the the collector graph mechanism builds it up for you so that you don't really think about fan out. But everywhere there's a processor to exporter in the standard configuration.
**Laurent Quérel** 21:12 Yeah.
**jmacdonald** 21:12 Any number of exporters can be on the end of a processor chain. And I don't have the details in my head, but I know that there's such a thing as a routing processor which was old, and it was replaced by the routing connector, which was newer, and the routing connectors have the ability, if you know what you're doing, and you dive down deep to choose your output channels much like you're talking about.
**Laurent Quérel** 21:37 Yeah. The the main difference to be honest is the fact that it's a generalization here, because you can have also.
Oh, I don't know what happened. My screen is again black.
**jmacdonald** 21:48 Sure.
We see 2 copies of a processor that you just copied and pasted. At least I do.
**Laurent Quérel** 21:57 Okay. And but do you see? Something moving on the screen.
**jmacdonald** 22:05 No.
**Laurent Quérel** 22:06 Okay. So that's again, each time that my that's very strange. I don't know what happened.
Okay, you know what? I think I will change my Let's go back to the maybe. I just want to explain the the remaining things without the screen. So the what I'm seeing is it's generalization. Because that could happen at any level of the dag. You could have those hyper edge everywhere.
between processors, between receiver and a processor, between processor and exporters. That doesn't really matter.
And it's not only a fan out, but it's It's something where you can define the the semantic of how the the message dispatching will really be implemented. Is it? Some kind of round robin, or broadcasting like the fan out stuff that you explain with the the exporter.
so you could totally imagine, to load balance between 2 exporter.
That that will be a semantic that you could express. I I don't think that it's something easy to express with the the existing collector, but I can be totally wrong. Let me know.
So back to the the description of this. Pr, so now I can what I like at least to do in terms of sharing. I like to show just a basic demo. And then I will be done on this point, and I will let other people discuss other topics.
it's Sue cross my finger, and I hope that this time this bug will not happen.
Sure.
Okay.
so we have this. So I have an example at the roots of the project. The configuration is the following super, basic it's an Otlp pipeline, like I said before. Soon we will have a single type of pipeline. So this type will no longer be a thing, and then we have a list of nodes one otlp receiver, one otlp exporter and they have their own. What in user configuration? The the type, the field that you have there are common type across all the the receivers I'm seeing for exporters, and what is inside config is purely specific to the the type of nodes receiver exporter processors that you you are configuring. And as you can see, the receiver is connected to one destination here, otlpx, and that's what we see here. We we could have, and we have a dispatch strategy type one robin. So basically, blood balancing classic load balancing?
So that's what I will run on this side of the terminal here I'm I'm starting?
so my goal is to have this data flow engine running with this very basic configuration, and the exporter will be connected to an Otap server. So I'm using a tool for people that know this tool, its name, hotel, weaver, and hotel weaver is able to run in what we name a live check mode.
So it's basically listening to an A Grpc Otlp, Grpc port and showing the the compliance of what for the the compliance of the Otp signal received against a specific registry semantic convention registry. So I'm just running this this thing adjust for the purpose of adding something to connect on the for this and for this engine, for the Otap exporter that is, as you see that will try to connect to the Grpc. Endpoint 1235, and that's what this one, I think. If I'm not. I think I started on the this port.
Oh, it is, yes, 1235. Okay?
So now, I can run the the example. It's basically a main using the configuration and and starting the pipeline.
I did some modification. So it's not compelling. Okay, so it's it's now listening and exporting or listening to the port. 43 17 and again. I think I lost the connection.
Yes, I need to share again. Sorry.
It's a nightmare today.
Okay, so it's listening. And now I'm using again weaver. But in a different manner. We can also use a 17 conventional history to emit random otap traffic that comply with the registry. So that's what the the registry meet common. Do and you will see that, and it's by by default, sending on the port 43 7 so we run this command.
and we should see something happening in this.
We should. Oh, yeah, we we so except that I I need to score so that is a report of okay, how well align or compliance what is received by the this command, how it's compliant with the registry, and there is a report. So it's a demonstration that when we send that to the receiver here.
the pipelines, and the corresponding messages to the exporter, the exporter export to this command, and then we see the result. So it's super basic, nothing very fancy but 1st demonstration that we have now. A rest. Pipeline working based on this new version of the engine.
Okay, guys.
**jmacdonald** 29:10 Super cool congratulations on that. That's great.
**Laurent Quérel** 29:13 Yeah, so.
**jmacdonald** 29:14 Did you say that the weaver was receiving data and validating it as well as synthesizing it?
**Laurent Quérel** 29:19 Yes.
**jmacdonald** 29:20 Cool. Nice. Very neat.
Yeah. Man.
**Laurent Quérel** 29:23 Yeah, that's what we parentheses. But we wrote an article on the open telemetry dot iu a blog post, talking about observability by design leveraging and hotel weaver. And that's exactly so the the goal with this live check is to include weaver into your Ci CD pipeline so you can check that. What you produce into your environment is compliant with your specifications. That's the.
**jmacdonald** 29:55 Very nice.
**Laurent Quérel** 29:56 And the emit is more to decouple teams. If you you create your your spec, then you can have a team that create a dashboard on one side and another team that is really instrumenting the application.
**jmacdonald** 30:11 Great.
Okay? And what this tool help us replace some of our bespoke load generator code?
Or is that independent.
**Laurent Quérel** 30:22 no generator, yeah. So weaver is right now.
Does not in, does not try to do some load generation. That could be indeed an option. That's something that we will discuss so, as you know, Charlie is working on this fake signal generator right now, it's really random in terms of what is produced. but we we could also drive the what is produced by a registry, as as you said, that's also an option.
And we could leverage River to generate the what we name reserve schema and use this reserve schema as an input for the the fax signal generator.
**jmacdonald** 31:11 Yeah, it sounds cool. I mean, maybe not a priority. But I guess the the problem you were aiming to to improve upon with the generator was that you've got these random distributions which are totally not realistic and won't help us test compression. But you could imagine, with a semantic conventions repository.
maybe either knowing or just sort of like configuring somewhere else. Well, this distribute. This is a small distribution, 5 different values. This is 100 values like that kind of information is what we're adding right?
**Laurent Quérel** 31:38 Yeah, it's that's funny, because I didn't thought about this approach when I discussed that yesterday with But I discussed that in the past with someone else, and I just forgot. But yes, I totally agree. And and we have which we name annotation for each signal and each attribute. It's a it's a it's an open format to describe whatever you want. So we could describe the the distribution with a notation and and just Leverage River to generate the the fully resolved schema, and use that for the fake senior generator.
**jmacdonald** 32:22 Yeah, I bet everyone in this room is at 1 point made a custom signal generator for load.
**Laurent Quérel** 32:27 Testing. I don't know.
Everyone is like to to create some simulation at some point.
**jmacdonald** 32:36 Well, this is really really good. Thanks. Laurent, I think. Then, what you're asking implicitly is, we should all go review. Pr. 5, 32. I noticed it changed name, but it's been there for a long time. It's the oldest one.
And I will go do that.
**Laurent Quérel** 32:52 Yep, great!
So I'm done.
**jmacdonald** 32:55 No.
**Laurent Quérel** 32:55 If you have any question, let me know.
Otherwise we can go to the next topic.
**jmacdonald** 33:04 Anybody.
Well, this is super great, and I we'll get to that code review soon. So let's see, I think, Drew, you're up on the agenda.
If I recall.
**Drew Relmas** 33:22 Yeah. Josh, I don't know if you're gonna share your screen, but I can as well.
**jmacdonald** 33:27 I wasn't planning to unless you want me to.
**Drew Relmas** 33:29 I got it.
**jmacdonald** 33:31 Today, so no.
**Drew Relmas** 33:33 Yes, hopefully, it works.
assuming you can see my browser window. So topic I had is kind of repo maintenance. But I wanted to talk about our release process as we're getting to a higher level of maturity with rust components as well as wanting to obviously keep releasing our go components as well on a cadence. I wrote down a couple of thoughts about things we could improve like right now, when we release go components? It's a lot of manual work using make file. And because we've done go only in the past, we were using the multi MoD from opentometry. Go build tools, which is a little heavy for the 2 go modules we're releasing right now. I'm trying to figure out what this looks like when we bring rust crates into the picture as well. There's a couple of open points that I mean. Some people have left opinions on, but I wanted to talk about here as well. The 1st thing is, should we be versioning consistently across the whole repo? Do we call right now, we're at version 0 dot 39 for our go modules. Are, we gonna say, rust code living in this repo versions together, and we have a unified release. Or should these be separate processes? The, there's a couple other kind of implementation detail points like the way go, modules are released is basically get tagging, and it goes automatically to package. Dot dev dot go, whereas crates depend on running a cargo, publish and versioning in your cargo files directly as opposed to just get tags. There are some. There is an opportunity for us to automate the rust side as well. Thanks to Cjo, who commented actually on this as coming from the open telemetry rust Maintainer side of things, they're actually doing some manual publishing. They have a script to do it, and they use their own credentials. But there's an opportunity for us to talk with the open telemetry Admins, and actually automate this with a bespoke secret managed by the open telemetry organization. So I have a draft out that does a couple of initial improvements not tackling the rust publishing yet, but at least making a couple of manually run workflows that we could obviously schedule as well to take away a lot of this manual work. Also using hotel bot, which is a a bot owned by the open telemetry Admin group that has permission to, you know, push, pull requests, and tag and things like that. So I know, Josh, this is actually in draft mode. But Josh reviewed it. I I do plan on kind of moving forward with this, if there's no huge objections. But I wanted to raise it to the group.
If there's any thoughts about specifically the versioning thing?
How? How are people feeling about that?
**Laurent Quérel** 36:58 Personally, I think we should separate the the release cadence between the go and the roast.
Because I don't think that we will have a lot of modification in the go, we will have massive amount of modification and potentially potentially future releases in in the rest.
So I I think that will be totally artificial if we synchronize the both and and regarding the the publication on Cratesio, I think it's way too early to publish our credits on Cratesio right now.
Because and if we the the risk, there is So first, st we have a workspace based rest project. So each crate will end up into a specific credits. That are you entry?
I'll pitch the men matter right now. I think it's still in flux in terms of naming in terms of.
**Drew Relmas** 38:05 It's.
**Laurent Quérel** 38:09 compartmenting, or or organizing those crates altogether which would be a mess to manage if it's already published, in my opinion. So we, I think we we should decide at some point. Okay, we are in a situation where we are comfortable to publish, and then we we can do that right now. I think it's which really that's my 2 feedback. Otherwise, although the rise that you mentioned, I think it's it's good.
**jmacdonald** 38:42 Yeah, I I did review just in the sense that I I really don't like the manual process of releasing and anything that makes it more automatic and safe would be would be great. I did read it. I didn't i i don't know if I understood it completely, but I would be willing to put up with a few broken releases to get to where it's easy to release
**Drew Relmas** 39:05 Okay, I think the the main thing I'm taking away from this, then, is, let me try and improve our automation, at least for go, and we will defer a lot of the rust work until a point where we're looking to release actual crates. I think if we can figure out like the cadence and the hotel Bot automation to make a release, etc. For the go components. It won't be too much more if we are adding a separate release train for rest at the same time.
Okay.
**jmacdonald** 39:39 I also, I don't think it matters very much to like release. More often. It wouldn't be a problem if every time we needed to change our rust create. We also released the air, the go, the go versions. I think there's too much fear of versioning, commanding in this whole world.
I like how arrows on 55. I like how data fusions on 47 or whatever like. We don't need to to like hold back versions is my, in my opinion.
**Drew Relmas** 40:08 Well, I know the collector collector contribute runs on a 2 week cadence. Right, Josh.
**jmacdonald** 40:15 That's right.
**Drew Relmas** 40:15 So there's not a re a huge reason why we can't just mimic that we can. In fact.
some of the automation I was thinking about like, prepare release. I can run this on a cron. It doesn't need to be a workflow dispatch, right? We can just have it go every 2 weeks.
**jmacdonald** 40:33 Next week. I'm the release coordinator for the collector. So I'm going to learn a lot about how it works. It's very. It's manual at some level, so I don't. I don't know the answers yet.
**Drew Relmas** 40:42 Okay.
**Laurent Quérel** 40:43 And I think it would be It's not because we are not publishing on credit that we can't create release, just archive, containing the zip file that that could be done right away.
I think that is fine.
But So if we want to do in the automation of the release. I think we we could also exercise that for us without publishing on.
**Drew Relmas** 41:15 I see.
**jmacdonald** 41:18 That sounds like a simplification at least. We could I. I feel like it would be nice to just like release everything, and we don't have to release crates that I owe until we're ready, I guess. But weak. That's the weak opinion.
**Laurent Quérel** 41:34 Yeah, but the between the go modules and the worst stuff I think it's my fear is, if if you have really this.
so do you have modification in the side? No modification on the go, and but you have a new release just artificially on the on. Go people that are using these go modules.
We look at the release.
Sure need nursing. And I think that would be already deceptive. So that's why I think it's having these 2 things separated? Because they are not really connected. I mean logically.
**jmacdonald** 42:11 Sure.
**Laurent Quérel** 42:13 Yeah.
**jmacdonald** 42:17 So sure, whatever's easy then. For now sounds like thanks for doing this.
**Laurent Quérel** 42:27 Yeah, that's true.
**Drew Relmas** 42:29 Yeah, you're welcome. I think I have insight. But if anyone has other thoughts feel free to DM me, but that's it.
**jmacdonald** 42:39 Yeah, I'll be glad to help.
Well, I know. Jake, you have one on the agenda, and I'm curious about this one.
**Jake Dern** 42:52 I was on mute. Yep, yeah. So this one for folks that don't know what I've been doing recently is standing up. My own otap server? Just so. I don't have to take a dependency on you know anything that's going on with the rust pipeline end to end just for testing right. My colleague, Rocky and I were very interested in taking opentelemetry, arrow, protocol, and then creating a pipeline that can flush that to parquet as quickly as possible. And so that's what I've been doing. Something that I noticed was the go implementation the hotel arrow exporter. It produces delta dictionaries. And apparently arrow Rs does not support those is something that I ran into initially. I thought it was something on the hotel arrow implementation like it was something that we did. I thought the rust implementation of of arrow was more mature than the go one, but it it seems that they're still missing some things. Which includes the Delta dictionary support. So I did a little bit of digging. It seems like I'm not the 1st person to come across. This actually looks like somebody else was doing exactly what I was doing, which was taking the the go stuff for for Hotel arrow and then trying to consume it from like some rust code. And they said they were working on a solution. But that was like 8 months ago, so I don't think they are. I did link a github issue in the doc here. But I'm not sure if there's a reason that this hasn't been implemented after so long. And and arrow rs, it could be the case that there's something that's like more complicated than than meets the eye here. But I was looking at it, and it doesn't seem like just based on how the go implementation does it. It doesn't seem like it should be anything too complicated.
But that's like one big blocker for, you know, sending data from go to to rust that I encountered.
**Laurent Quérel** 44:44 So I will be to be honest, very, very, very surprised if the data dictionary is not supported into the rest implementation.
So can you.
**jmacdonald** 44:54 Yeah. And yet there's this error message that Jake links to. That makes it look very clearly like an error. I also wondered if there's some misinterpretation happening here like, are there different kinds of delta dictionaries? Are there different places where a Delta dictionary could be used? And so on. That's just the level of question. I'm feeling right now.
**Laurent Quérel** 45:14 Yeah. Is Albert also present in this? Yes, yeah, I'm I'm here.
**albertlockett** 45:21 Yeah, I I think, yeah, I'm not. I'm not sure about this.
I find surprising. But then again, like we see, we see the error message that Jake shared. And it's it's extremely clear it says Delta dictionary delta badges are not supported. We could, I think, a good place to ask could be the Arrow Rs discord. We could just throw a question in there and say, You know, like.
what like is there a reason this isn't supported. Are there any, you know, technical challenges that are preventing, like, you know, this implementation moving forward? And if not, I mean, like, maybe, like, Jake said, if it's straightforward we could just do the implementation for the ars folks. That'd be.
**Laurent Quérel** 46:08 Where did you see the by the way, the this I would put? Because I didn't see. Maybe it was room.
**albertlockett** 46:15 Oh, it's in the in the Google, Doc. There's a link to.
**Laurent Quérel** 46:20 Oh, okay. Okay. Okay.
**albertlockett** 46:22 Yeah, yeah.
**Jake Dern** 46:24 I linked a couple of things in there where the code is, and then also somebody else that seemed to hit the same issue, and and the setup that I'm running. I'm just running you know, the Hotel Arrow exporter from the go collector with some like fake data that I had generated. And then, I'm just sending it to a Grpc. Server that just has a a consumer from the the crate with the implementation, the rust one.
**jmacdonald** 46:46 Hotel Arrow rust. We ought to be able to put a validation test in, you know. Have that framework to like. Run the go collector and read it and send it through a round trip and get the same data back. So it'd be cool if we knew exactly how to trigger this in a validation test, because I haven't seen this before. And that's curious to me.
That this is a new issue, a new, a new item coming up where we're all a little bit confused by it.
**Laurent Quérel** 47:14 Okay? So that's unfortunate.
because I did a rest implementation before the go implementation. I don't remember if a distance.
**jmacdonald** 47:28 Yeah, Lauren, I remember, like 2 or 3 years ago we were. You were sort of like waiting for the go implementation to implement delta dictionaries as I recall. And I. That's why in my my head it was already implemented in rust 3 years ago, or whatever.
**Laurent Quérel** 47:43 Yeah. And I was already aware of that a long time ago. So I'm it's it's super strange to be honest.
**jmacdonald** 47:51 Yeah, there's something weird about this that feels like, not quite right.
**Laurent Quérel** 47:54 No.
okay, maybe. Or maybe I was used. No, I don't see. I think I was using the OS, because there is also our 2.
**jmacdonald** 48:04 I thought those were sort of merged now.
**Laurent Quérel** 48:08 Yeah, I think they they have been merged.
okay, so that's an interesting to to manage different theory.
**jmacdonald** 48:20 We should follow up. I think Albert's suggestion of of dropping into discord is good. I I need to get discord on this machine, anyway.
so yeah, my my goal. Then Jake would be to answer these questions and fix them. And maybe that's maybe that's hard. But maybe it's not. And then maybe we're just there's some sort of confusion happening. Work around it somehow. Ideally, we would end up with some test coverage in the validation, so that we can be sure that go and the rest talk to each other, which I'd like to maintain. Going forward. I I this isn't quite my time on the agenda, but I did wanna ask or remind us that there's these 2 crates, at least the ones that we know about. There's the data flow crate that Laurent has been working in. And then there's this Otiller rust which we Albert and I and others have worked in. It has a validation test. It has, you know, data flow pipeline free, just like you want to read some some of this data and turn it into otlp, or vice versa, that that has that support. And I think we want that going forward. So I I do see us bringing the hotel arrow rust code along with us when we migrate it into a single great hierarchy, I guess, is what I'm trying to say. And so I do value that code, and I want to keep it healthy.
The other item that came up over the last couple of weeks in the same place is that I had started working with those procedural macros to make it easier to write and read Otlp, testing there's there's Chen Lee was working with Otlp tests and ran into essentially the problem I was hoping to work around. So there, there is valuable stuff in that hotel error. Rust repuls crate is all I'm trying to say.
and the more we advance I think we will bring some of it along. So don't worry about creating tests. If in that directory we'll keep them.
I think.
Jake, I'd be glad to follow up, or, you know, help follow up on this. I'm I'm okay asking dumb questions in discords as well.
**albertlockett** 50:32 The other the other resource that we can maybe run this by could be matthias Lobel from.
**jmacdonald** 50:39 Yes!
**albertlockett** 50:39 Month, because he's in the Hotel Arrow Dev Slack Channel, and I know that like their their company Frederick, from their company, has done a bit of work improving the dictionary support for arrow, Ipc and the rest implementation, so they might have some insights as well.
**Laurent Quérel** 51:00 Yeah.
**jmacdonald** 51:01 That's an easier, much easier approach to seeing if anyone at polar signals knows the answer to this one would be useful. They. They also have been trying to do what we're doing. So maybe they've run into this and know know it.
That's a very easy, Jake. I'd be glad to help if you want to, but to figure out what we just said. But, they're in the slack for, and we can ask not to.
**Jake Dern** 51:22 Yeah, definitely. Yeah, if you know those folks. Yeah, that sounds great.
**Laurent Quérel** 51:28 Another I try to connect the dot because the the arrow flight is the the I for the based, using the the Ro Ipc stream framework across languages.
And it's obviously leveraging data dictionary. So that's incredible that the so it means that we could get a go client with the rest clients using our flight.
which is crazy.
Yeah, okay, that's yeah, definitely.
**jmacdonald** 52:11 I just learned about Nano Arrow, and don't know exactly what that is. But now I do. Now I know it exists. Alright! We'll get to the bottom of this. I'm sure.
Alright, duck, dB, related. Okay, Gotcha. I like duck. dB, I think we've reached the end of that topic. I've said what I wanted to say about hotel arrow rust and the the way I want to keep it. And then but it's not urgent.
my item on the agenda. Since we're almost at the end here, I'll just kind of be quick about it. But so I put up a Pr. In the Collector Repository, and began speaking to that group about the rust. Go interoperability. Yesterday at the Collector Sig. This was discussed. You have a link to my pr, there it is.
I think it's enough depth to like. Lay out a plan. It's pretty still pretty hazy on a lot of the details. It steps through builder integration. configuration integration, runtime sort of like lifecycle integration data, pipeline integration context, integration. And then we get to what I'm calling the fallback which is, which is, we know that ffi, and linking and plugins and all that stuff. Sometimes it's hard sometimes. You can't use Sigo.
All kinds of reasons why you might not be able to do what we're trying to do. There. Falling back means creating 2 separate processes and connecting them with additional edges. You know Otlp export receiver, and so on. So that's the step 6 in my plan, which is to like. At that point we should have a standalone rust collector, and I like to be very clear about that, that we're kind of getting that place and step 7 is one that there's definitely a strong interest in for Microsoft.
and and I think the the wider community has seen. You know, there's a lot of different agents that can do telemetry these days still. And we're we're one of them, and many of them support plugins. So that's that's what our the end of our ambition was discussed yesterday, and so, anyway, the what I thought I would get was a lot of fear and uncertainty. There was a little bit of that. There's the 1st question is always, what about Seago?
And are we sure? Because there's a lot of you know, fear of, of see, go and go like. One of the reasons why people like go is, you can just build this thing once, and it doesn't even link against Libc. It's statically linked. And so it will be fairly portable across all Linux environments. You don't have to build one for Debian, and one for ubuntu, and one for red Hat, and so on because of different lib. C's so as soon as you go to see go and start doing ffi, and calling to to those Ffi C libraries. Then you have trouble.
You have to do more release work. You have to be careful about which versions you're building your releases for and so on. And yet those were the challenges that we knew we were going to face when we talked talked about plugins, no matter what plugins are hard, you're going to always have dependency mismatch problems. And that's that's sort of the nature of that problem. Space.
So what I've so what I'm trying to say is that there there was the natural question about Sigo, and yet we but but it wasn't surprising. We know what it means to do, Sigo. We know that it means that our release process will be harder, that we have to release per architecture, binaries, maybe, and so on.
What was nice about this conversation is that I immediately picked up a lot of support. Google was present in the meeting, Google, meaning a representative from Google, who has a hand in their Google Cloud Platform Hotel collectors. And they build exactly what I just described because they need Seago. And that was what was interesting to learn. So Google is running hotel collectors. They provide pre-built, but hotel collectors for the customers. That means that you can choose a Gce with different. You can choose different images on your Gce, therefore they have different hotel collector built for different images for the different Gce, and so on.
It means that they've already tackled the Cgo problem. And the reason why is that they are running Nvidia drivers for Gpu enabled clusters. You. You know this is a piece of code that Nvidia gives you. It's a c library, and it has to run in a collector. That's why we need Cgo. And so it's nice to find that we have existing requirements, existing experience and a lot of support. That's what I found. So I thought that was all very positive.
I didn't get any objections in the sense of this is bad, or this won't work.
and all it means is, there's a lot of work ahead. My, if you haven't figured this, if you haven't seen it yet, I am very involved with a go collector right now. I've been much more work in the Go side, just to make sure that that effort is healthy and doesn't have concerns with what we're doing. And so far so good. I'll be the release coordinator for that group next week. And I promise you that that group has bigger problems than what we are doing so there's not a lot of like fear of rust happening at all. So I think everything looks good right now. That's my report, and we're almost at time anybody else want to say anything about that or anything else.
I will tell you what I do want to hear about at the next meeting.
I want to hear about our testing work. I'm gonna try and get C. Joe to come to our next meeting, but I also will catch up with him before the next meeting, so that we can.
Now that we have the 1st collector standing, I want to have a 1st collector test.
That'll be great.
Well, anyway, I think we're at the end.
Thank you all, and next Tuesday we'll do this again, and find me on slack. Everybody find us on slack.
**Laurent Quérel** 58:24 Okay.
**jmacdonald** 58:26 So.
**Laurent Quérel** 58:26 My.
