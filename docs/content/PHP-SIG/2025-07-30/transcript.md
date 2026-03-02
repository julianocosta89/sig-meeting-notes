SIG: PHP SIG
Date: 2025-07-30
Duration: 95 minutes
Zoom Recording URL: https://zoom.us/rec/share/3Wu9_JmDbgxIXnuaEgczyg4EhVr7W-iOqeSRoXXYviTMNA-B1N_VD4gMxtEcm2DR.7b6NYZNxIksC90wh
============================================================

## Zoom Recording Transcript

Chris Lightfoot-Wild 00:00:20 Hey! Bob!
Bob Strecansky 00:00:22 Hello, Mr. Lightfoot! Wild, how are you today?
Chris Lightfoot-Wild 00:00:25 Oh, I think, yeah, you well.
Bob Strecansky 00:00:28 I'm doing well.
Chris Lightfoot-Wild 00:00:30 Nice.
Bob Strecansky 00:00:33 It is a. It is balmy here right now.
Chris Lightfoot-Wild 00:00:37 Yeah.
Bob Strecansky 00:00:38 Yeah, it's I'm trying to
think of what the High was yesterday. Let me see, I think it was our higher. Yesterday was around 40, see?
And it was like 35 c. At like 8 Pm.
Chris Lightfoot-Wild 00:00:54 What?
Hey? That's short.
That is very hot, I mean, have you got a pool like you just gonna have a dip.
Bob Strecansky 00:01:03 So I don't have a pool at my house, but we belong to a gym that has a pool, and we belong to like this little family pool, too. That's kind of cool.
Chris Lightfoot-Wild 00:01:14 Nice.
Bob Strecansky 00:01:15 Yeah, so very necessary and very expensive heating ventilation and air conditioning bills in the summer.
Chris Lightfoot-Wild 00:01:24 I imagine.
Bob Strecansky 00:01:26 But we're you know what they say. Water's expensive in the desert.
PAL Sergey. How are we doing today?
Pawel Filipczak 00:01:41 I'm okay.
Hmm.
it's 9, 19 here. So it's not too bad.
Bob Strecansky 00:01:52 19 is better than 40. Yes.
Pawel Filipczak 00:01:56 I agree.
Bob Strecansky 00:01:58 I'm
I'm a competitive tennis player, and I look like I'm moving out when I go for my matches in the summer I have like 6 shirts, and I sweat through shoes, and I go through 5 or 6 liters of water, and ugh!
It is.
Sweaty.
Sergey 00:02:18 Do you guys measure when you drink in the waters, or do you use on ounces like it? Do you use liters just for our sake, or.
Bob Strecansky 00:02:24 Yeah, I was trying to not use the freedom units for you, Sergey, but.
Sergey 00:02:29 Between yourself, you'll use something different. I'm just wondering, like, where we have.
Bob Strecansky 00:02:34 Oh, so, yeah.
Sergey 00:02:36 Use tons, right? You don't have measure of weight that is really high, like a ton. Right? You will not smaller measures. Yeah.
Bob Strecansky 00:02:43 In my everyday like a couple good examples. Temperature is always in Fahrenheit everywhere. I measured. I weigh a hundred 95 pounds and I usually drink a gallon of water a day.
Sergey 00:03:01 Right, but but you will not use gallons like for smaller amounts. Then you will use ounces right.
Bob Strecansky 00:03:06 Then we use ounces. Yeah. And yeah, so there's 128 ounces in the gallon. The conversions just don't make any sense. What's that.
Sergey 00:03:17 100 and 8. You said.
Bob Strecansky 00:03:19 100 and 28.
Sergey 00:03:20 Mate, which.
Bob Strecansky 00:03:21 Makes it makes a ton of sense. Right? That's a.
Sergey 00:03:23 Power of 2.
Bob Strecansky 00:03:24 Number. Yeah, yeah, that's technically true. No, the free, the freedom unit system is absolutely like. And then you start doing, you start getting into even more bespoke dumb freedom unit stuff like
when you have a 10 socket on most European cars, and for, like the same bolt on American cars is like a 3 eighths inch socket. I'm like, Yeah, that makes sense. Let's just make 3 eighths of an inch socket.
Hey, Brett.
Brett McBride 00:03:55 Everybody.
Bob Strecansky 00:03:57 We were just talking about freedom units versus the metric system.
Brett McBride 00:04:02 Very good.
Bob Strecansky 00:04:07 Alright.
Let's see, do we expect anybody else today?
Okay, let me share my screen.
Yeah, I'll see in my beautiful safari window.
Brett McBride 00:04:42 Yes.
Bob Strecansky 00:04:43 Alright.
So we discussed having our special discussion week about spi this week. So everybody still want to do that this week.
Sergey 00:04:53 Yeah, yeah, I'm I prepared a couple of questions so it'll be really useful for me personally.
Okay, hope for everybody else as well.
Bob Strecansky 00:05:03 Alright. Sounds good. Does anybody have
Does anybody have any any like pressing agenda items before we dive into that conversation?
Sergey 00:05:14 I want to skip all the usual Walkthrough.
Bob Strecansky 00:05:18 Yeah, I think we're that was, that was the original plan. But I'm very happy to do like a speed run of that. If people feel like it's prudent.
Chris Lightfoot-Wild 00:05:27 Yeah, I think we skipped it last week because both Brett and Sergey were off. And I think you were.
So you, Sergey. We're interested party in that
Sergey 00:05:37 So whatever you prefer, guys, I'm fine either way. So would you like to jump straight into it?
Bob Strecansky 00:05:42 Yeah, yeah.
Brett McBride 00:05:43 Sure.
Sergey 00:05:44 So essentially would you mind if I share? I have a couple.
Bob Strecansky 00:05:48 Yeah, please.
Sergey 00:05:49 Okay.
So please let me know when you can see my screen.
Chris Lightfoot-Wild 00:05:56 So let's make it big.
Sergey 00:05:59 You can see it right.
Pawel Filipczak 00:06:00 Yes.
Sergey 00:06:01 Okay.
So I wanted to start. So we just canceled ball and I, and we saw that
Pr, that Pr, that you're Chris working on. It looks good. It should allow us to do what we want. But
in a perfect world we had like a 1st thing that we encountered, and I think we discussed it a couple of times in our weeklies is essentially, I think, what we're missing is ability to essentially configure multiple sources
in multiple files right? Like we discussed last time. So, for example, default sources that come with SDK, they will probably be defined in
one of the composer Json's that come with SDK. But then, let's say, if on top of it, we want to add the additional composer, Json, for our distro that will contain OP. Hopefully, it will later on migrate upstream. But let's say, for now that's going to be the case, and maybe some other sources, maybe other users would want to add. So I was wondering, how do we solve the problem of deciding what's the order between them? Right?
Because, if I understood correctly
there is some wait for for this Plugin for the Spi to enumerate this composer plot to enumerate all the entries.
but then we're not 100 sure. How will it? What order they will be presented, because, according to this
Api that we see here, it returns at least right? So it should be fine.
So
so it should be possible to configure multiple entries here, right? And we. And we see that in some cases spi does allow configuring multiple entries, not in the case of this resolver. But in other, if for other interfaces there are multiple entries right? For example, like this one.
So essentially, the the 1st question is, what did you guys think about the issue of the order
like, if we have, this will be default entry, then we want to add another entry. So one of the things that we thought. Maybe we can add some kind of priority to it. But maybe there are. There are simpler solutions.
Brett McBride 00:08:06 No, I think that's the way to do it. Spi allows for that, and there's prior art in the SDK somewhere off the top of my head. I can't remember
where we do it, but we do basically add extra extra data to spi entries to allow them to have an order and
add extra, add extra data about them. So I think pro.
Sergey 00:08:30 Okay. So it's it's already nice to do it
not even needs to be added.
Brett McBride 00:08:34 Yeah, it's not. It's not officially part of spi, but
but we I made it part of the interface that spi is providing
or that things provide through spi
So yes.
Sergey 00:08:53 So what we will need to change then, if I understand it correctly, this syntax should be supported. So the only place that we need to change is this place where it's red. We just need to account for additional fields, sort by them and just use the resulted order. But we don't need.
Brett McBride 00:09:08 Yeah, I mean, we'd probably we'd probably extend resolver interface to have things provide a priority.
Sergey 00:09:18 You want to treat it as part of the resolver itself.
Brett McBride 00:09:21 I think so.
Chris Lightfoot-Wild 00:09:23 I'm just. I've I was looking at. I've just found where it is. It's on the V 2.
Brett McBride 00:09:27 That's Chris.
Chris Lightfoot-Wild 00:09:29 I'll put a link in the Channel in a second. Sorry
Sergey 00:09:34 In the, in, the, in, the slack.
Chris Lightfoot-Wild 00:09:37 Sorry, no. And on the zoom, yeah. Hang on.
Sergey 00:09:40 On the chat.
Chris Lightfoot-Wild 00:09:44 There we go.
So this is, yeah. This is, the bit doesn't exist in the mainline branch yet. But.
Brett McBride 00:09:51 I guess.
Chris Lightfoot-Wild 00:09:52 It's only the thing we want.
Yeah. But basically the does. The interface implements, the priority as well.
I mean audible.
Sergey 00:10:08 Oh, okay, so.
Chris Lightfoot-Wild 00:10:12 I guess there's some examples of that. I could provide it one second.
Sergey 00:10:19 So it's kind of like then incorporated in today. So it's like, when each instance is loaded, then it's provided to it like.
where is this used here like so essentially, you're saying that the way it will work is that this class will be provided this additional like as a parameter to this. When this will instance of this class will be constructed, something like that.
Chris Lightfoot-Wild 00:10:42 Yeah, that's right. Yeah,
let me. Just yeah. So if you.
Brett McBride 00:10:48 So I think, as it as it stands, the priorities aren't
configurable. They're they're sort of baked into the each implementation.
Sergey 00:11:00 Sorry implementation of what?
Brett McBride 00:11:04 So if we were to look here, there's his mom.
there's a there's a common interface.
I think it might be called spi loadable interface.
That each of these.
Sergey 00:11:18 Loader.
spare, loadable, and.
Brett McBride 00:11:23 There we go, spi loadable interface.
Sergey 00:11:26 Okay, is it part of?
So it's already inside. So if I.
Brett McBride 00:11:31 Well, it's it's in. It's probably in version 2, because that's where we're we're looking.
Sergey 00:11:35 So it's not part of this Pr yet.
oh, it's it's it's a main version. 2 app up
the the Pr. That Chris working on. It's prior to version 2. It's
it's before it relies on version one of the SDK.
Chris Lightfoot-Wild 00:11:53 I mean, we could port this across obviously, if we needed it sooner. But I don't know what the plan is with.
Brett McBride 00:11:58 Thank you.
Chris Lightfoot-Wild 00:11:59 This extra functionality going into v. 2, or being ported across to one or
Sergey 00:12:05 So so that so that loadable
is this is what allows to inject this additional parameters to it.
Priority? It's hard coded thing priority.
Okay. So it's I see. Okay, got it?
yeah. Let's go ahead.
Chris Lightfoot-Wild 00:12:29 I was just going to suggest the syntax you've, I guess, proposed in that composer is
not supported by the spi package, which is the Neva's
think so. It just expects just a a list of clusterings and.
Sergey 00:12:45 How does it derive this? It's only exists in this interface. But there is no, there is no connection between Composer Json and setting this priority
extra.
Chris Lightfoot-Wild 00:12:56 No, the the SDK, when it loads them, it then does the order in itself, and then chooses.
Sergey 00:13:02 Oh, okay.
so you can query it. But you cannot, unless you change the order. And how does it decide between files like a file somehow ordered between. Like, does it understand?
Brett McBride 00:13:13 No like.
Sergey 00:13:14 Dependency.
Brett McBride 00:13:14 It gets them all, and you would have seen, I think, there was an iterator to an array in the previous class. You were you were looking at. So it takes everything that implements that, and then does an array sort based on what each one claims is its priority.
Sergey 00:13:32 Right. But I wonder like
if I understand correctly if you mentioned this interface like, if we go back to Composer Json, if I have a section that maps something to this interface in this file, and then I also have this section
the same interface. In another file. It will concatenate those 2 arrays. Right? It will return. Still, one array. Yeah. Somehow concatenated. I'm just wondering, how will it concatenate those arrays for multiple files? Does it decide on some traversal order of those files like, does it always start with the leafs
like the composer Jason's? They don't. Nobody depends on them like, I wonder like, if or it's just not not defined that that specifically said that rehearsal of them.
And we don't want to depend on it too much.
Chris Lightfoot-Wild 00:14:16 I think this has the same order as the composer. File order, where we register them.
Brett McBride 00:14:22 So.
Sergey 00:14:23 Sorry, but.
Brett McBride 00:14:24 Go to them.
Composer processed them in. But is that well defined? I'm not sure it could be alphabetical.
I don't know.
But provided there are actually provided, 2 things don't actually have the same Fqn.
They're not going to clobber each other, and it'll just be one array, and and the order doesn't matter, and that's
that's probably.
Sergey 00:14:48 I mean alphabetical. This line. It sorts it somehow sorts these lines potentially.
Brett McBride 00:14:54 I'm I'm just gonna say it's it's undefined, and it shouldn't. It shouldn't matter.
Sergey 00:15:02 Well, in this case, that's right.
So we do want to control this all.
Brett McBride 00:15:05 That's why we add priority.
Sergey 00:15:08 But if I understood correctly.
is that this priority is only derived from order, you cannot explicitly set it between multiple files right.
Brett McBride 00:15:18 No, the priority is defined in the implementation of
a class. So we've added a priority and a type method here. And so
the things that implement that say my priority is 100. My priorities.
Sergey 00:15:41 So you you propose into hard code, into this class.
Brett McBride 00:15:44 Yeah, it. Just.
Sergey 00:15:44 Assign 100 to this class, and that's it.
Brett McBride 00:15:47 Yep.
Sergey 00:15:49 I see. Well, it's a it can also be a solution. I guess I guess it will allow less flexibility to users like. For example, I remember we had the support cases in classic agent that some people wanted I and I file to be higher priority. And some people wanted environment variables. Right?
So with allowing this priority syntax, we can in the worst case, we can tell people, okay, you want. And I then go to this file and just change the order, and then you will have whatever you want. Not the order, but priorities, right? They can always in their composer, Json, but I guess, in their composer, Json. They they can just explicitly set the order to those sources that they want to use. Then they will achieve
the same effect as well. So I guess we can say that those use cases.
Brett McBride 00:16:32 Yeah, possibly, although I mean you, you've seen some code there where we
we explicitly get some things and then use spi to to sort of iterate over.
A list as well.
Sergey 00:16:48 Which code do you mean?
Brett McBride 00:16:49 The thing Chris said before was like that would be a change to to spi and the reason that it's
those interfaces were added in v. 2, was because Nivey, the author said.
this is what the upstream Java Spi
proposes, and then he pointed me to the spec, for you know spi in Java of which this is a clone.
Sergey 00:17:18 I see. Okay? The idea of spi came from Java.
Got it? Okay? So.
Brett McBride 00:17:25 Yes, yes, ours is very, very similar to Java's.
Sergey 00:17:29 Got it. So what do you? What would you suggest is a kind of like the solution for now. So let's assume that we want. So let's say, Chris merges the Pr. Now we have these sources for the so in the like, what we assume, we can always implement the same approach as this. SDK configuration. Implemented right? We can just explicitly call other sources. And essentially, we will always kind of like shadow them right essentially is done here.
So May. Maybe we can start with that. And then you say, when we arrive to the version 2, then we can implement sorting by priority.
and then right?
No but then we still have a problem. Please go ahead.
Brett McBride 00:18:15 I said, let's talk about. Let's talk about OP. Am. Because I have questions. And that's really
why we're talking about Sp.
Sergey 00:18:22 Yes, yes, let's go ahead.
Brett McBride 00:18:23 Incorrectly. Yep, so so OP-amp will do remote configuration, and
it will do it at least in our implementation. It'll do it once immediately on. Start up cool
of ample
we will go and call a remote configuration source, and we'll get some sort of structured data back.
is that I guess my 1st question is is that opt in by a variable, you know, hotel use OP. Amp and or OP amp, address and which will tell which is a a an indication to us to go and check OP. Amp for remote configuration. So
that's the 1st question. The second one is, once we've got this remote configuration. What is it?
Is it a complete configuration by itself that replaces
or is used in in its entirety instead of environment, variables or yaml declarative configuration.
Or is it some variables? And that's.
you know, placed on top of what we get from the environment.
Sergey 00:19:41 I understand. So, Pavel, would you like to take the 1st 2 questions regarding the when we read the Configuration? And when it's enabled.
Pawel Filipczak 00:19:50 So we are reading the configuration on early Startup. So in the module we need, we are starting the threat which is fetching the configuration during the initialization of the connection. So it's opening connection to the collector or some remote source.
And then it's fetching config.
So the feature is native. The endpoint is set up. So if if you set up the the endpoint with the environment variable, then
the pump will be automatically enabled. If not, it will be disabled.
So what's going next with the with the configs?
If the so it's fetching the config and storing the config in the in the cache?
And what happens next, the request in it
and in the request you need.
So the open piece.
I will explain it later. So in the request in it. The the agent is bootstrapped, and then the config is applied by the Php. Part.
and previously it's it's also applied by the native part. So if the native part is using some values from the config. It's it's also applied on the native side.
But if the if the config does not arrive, be before the request. Then it's not applied.
So in my local test with the local collector, it was always fast enough to get the config from the from the local collector.
So it was applied, and it was working from the from the request Startup.
and going back to the or going going forward to the second question, what what is in the the what is opamp opamp is just a protocol to transfer some data. So you can get that data blob
from the collector.
So.
for example, for elastic, we have our own values. So you have the Kibana ui, and you have a a a bit of options that you can set up in the Ui.
and those options are translated from the elastic
namespace to the open element namespace. So, for example, we have the different name for the logging level, and we are translating this with the with the logging level.
So
also the data format. It might be different. It might be Json, it might be Yaml. It may be binary data protobuf, whatever. So
hmm
in. In case of of opamp, we need to provide the mechanism of the translators of of some Api for for the
plugins, which will translate the data
from the OP. To the to the open telemetry
and apply it somehow. Right? So it it's not.
you know. It's it's it's nothing, you know, which is end to end. And it's it's not strict to the open telemetry or or done some namespaces. It's just a transport layer. And
and and that's it.
So
it requires a bit of effort. Now we are doing the elastic translation from the of the elastic data.
And we are applying this by trans, we are translating, translating this local level to the auto lock level. And because we decide to
go on with the very basic implementation.
We are just changing the environment variable on the fly. So the and that's it. But as we discussed it earlier we should implement some kind of
a additional configuration source which can be moved. Then we will be able to know, to, to
to make it, to to do some smarter logic in in the instrumentation and in the SDK to change the to change the behavior of the agent. So we can then decide which options are static and which are dynamic.
Sergey 00:23:58 Right but to answer, yes, sorry I missed, Paul answered it, but so essentially we merge right? So the it's explicitly mentioned by Opalm that local configuration. I think this is what Brent you mean by environment, even though even though you don't only mean environment variables, we also mean the 10 file and any file right in. I
so everything that you collectively is called here local configuration that is supposed to be merged with the with OP result, with configuration that comes from OP with OP having higher priority. So essentially, we 1st try the OP. Then it doesn't. If that doesn't have that option name, or I think you call it variable. If it doesn't have that variable, then we drop into the local configuration.
But if Opm brought that option, then we should use that one
so that it essentially shade those. Whatever local configuration has.
Brett McBride 00:24:52 Doesn't bring anything.
Sergey 00:24:54 Local configuration is used.
Brett McBride 00:24:55 Yeah, any any given thing that we're interested in? We preferentially check OP. Amp.
Sergey 00:25:03 And only then. Yes, yes, right.
What you said about the configuration file. That's interesting question. I probably should raise it to ask other teams, because I understand that this feature of configuration file the all day languages have it right. It's not something specific to pitch. So I wonder how they?
No, it's in spec. Yeah.
Yeah, because you may. I remember you mentioned previous meeting that I attended that it has special treatment. This configuration file? Right? It has a richer kind of like options and more options available to configure there. And it. It has kind of like exclusive priority right? When it said, then any other sources are not used at all.
So it's different. In that case it's different in that sense from any other configuration sources which are usually always merged in some priority order, right.
Brett McBride 00:25:54 Yes, that's right.
Sergey 00:25:55 So I quickly searched this spec for the configuration file. But I think the only mention of this wording of configuration files. It's only in the context of the pump itself. So those pieces of data that been brought what Pavel mentioned, it's kind of like they call them configuration files, but they essentially maps of key values, right? And one is on which we decided to. So you can just bring multiple. Essentially, you can call them files.
So you can bring multiple maps. Well, I guess they don't have to be maps. We consider a specific entry, this configuration file that we give it a name that we predefined, which we call the elastic, or whatever right, since it's elastic, specific. But it doesn't have to be like. When we merge this upstream we will have to decide, because the way we implemented Opm, everything that was left for the vendor to be vendor specific in the spec.
We obviously went with something less specific. We will have to decide how we make it vendor neutral when we contribute it upstream. But currently the way it's implemented for elastic distribution. It's it looks so essentially opamp can bring multiple what they call here configuration files.
and they map to names. So we search for this elastic name, and then we assume that its format is, I think we we already assume that it's supposed to be Jason, or we we can read which format it is, Paul. Do you remember what? What is the case? There.
Pawel Filipczak 00:27:20 We have. We have hard coded that it's it's Json. But it might be another, you know, format, and I think it should be, you know, implemented by providing some kind of processors. Then you are just getting the access to this, to this file, name to the file content map.
And if I call, that might be anything. So if you if you encounter some fine name, then you you have to parse it somehow. It depends on on
on on the processor right? And the the issue here is also what will happen if if the if there will be multiple files arrived, what's the order of processing, of applying the configuration, because
in in that files it might be, you know, configuration which will change the config for the environment. I mean how we how we name how it is for today? Right? So we are just assuming that it will be a configuration for the replacing the the environment or config files or Pspi 9 values whatever.
But it may contain any different configuration
in the future. So it might be many different configuration files inside by default.
It's it's it should contain contain only one file. Even the the file name might it? It can be empty
by by this spec. But we need. We have to be aware that
in the future it may change so it may contain many different
files in many different packages. So it it may change so once it it can send you, I mean the open server may send you one file on the on the other, heartbeat or polling during the next poll. It may send you totally different configuration file. So it's not specified that it will always send one file or or or this specific file. So it. The the protocol is designed to send you anything.
Sergey 00:29:21 And
right. So just to. But but for the way we implemented, currently, we do assume some pre, we have assumptions about the the back end and what it's supposed to send it will not crash if it doesn't send. But we will not look for anything else. Right? So currently, we're in this map, we only look for for a particular name. In this case, elastic and then I think we assume that this thing will have here a Json content type
if it's
doesn't that we don't know how to process it and then obviously, we assume that this body is a string Jason string of Json.
and then we process it as Json
and the. And it's A, and we assume that Json is essentially a map from name of the of the option or variable, and to the value.
Brett McBride 00:30:08 Okay. So once that transports done it, it ends up as a map which looks something like a you know, the contents of our any file, or or, you know, key value pairs.
Pawel Filipczak 00:30:20 It might be.
Brett McBride 00:30:22 Yep.
Okay.
Sergey 00:30:25 Yeah. So so again, it's a little bit allows flexibility. So we'll need to decide how we make it vendor neutral so it can be adapted. We will. Obviously it will be good if we will have additional vendor to, you know, to to see that we are in the right direction. But we can go with what Paul suggested. We can.
Whatever is smart code currently for elastic will make it kind of like. Instead, we'll be replace it with the ability to register processor right? And then each vendor can just register different processor. That will be specific to the. And then we can even
have in country processors for elastic, and if other vendors will have like for data, dog, or whoever else implements it
so we can already. Now I'm I'm not sure it will be easy to detect it on the fly right excuse me.
Pawel Filipczak 00:31:10 I think that the spi is quite nice to to add the processor here to to.
Sergey 00:31:14 Best of the would be if it was.
if it was possible to detect right. Because then users won't need to know.
Yeah. In spi, we can register all of them. But the question which processor do you apply like, I don't know if, during this communication, can we understand, like, what is the who is on the other side? Like what collector like? What is the vendor for collector? Then we can.
Pawel Filipczak 00:31:35 But you know, if if you are, if you are delivering the elastic distribution, then you need to modify the composer. License.
Sergey 00:31:41 No, no, yeah. For us. It's it's not an issue. Yeah, I agree with you. But I'm talking about like, let's say, people want to use vanilla hotel right? Not the specific vendor distribution. And they want to connect it automatically to data dog or to elastic. And they also want for it to work right then
Pawel Filipczak 00:31:57 They can include everything and we can. It's just about the implementation. So we will look for.
Sergey 00:32:03 Yeah. But how we know which processor should process right? Like. So we can give all of them. I think we can discuss it like, maybe you are right. Maybe we can just see all of the. But it seems to me that we the best would be some way to detect. Excuse me, Brad, please go ahead.
Brett McBride 00:32:20 I was. Gonna say, you should be able to query them all, you know, if if you went through Spi and said, Give me give me everything that understands OP. Amp, that I have installed, and then just pass it to them. Do you understand this? Yes or no? Okay, process it. Whoever whoever gets in 1st wins, perhaps, but
Pawel Filipczak 00:32:39 Right.
Sergey 00:32:40 Right? Yeah, maybe maybe it will be possible, like, because like, we said we would like to have a specific thing here. That should be license specific. So if other vendors did some. So because the implementation until this point, I think it should not be vendor specific, it can be vendor neutral, and at this point we can just have some pluggable instances that will run on this map, and whatever will detect that it comes from the corresponding vendor. They can then, parse it according to the vendor specification. So so yeah.
did it answer your question, Brett, regarding the OP.
Working. So how to work.
Brett McBride 00:33:16 I think so. Yeah. And so what? What it sounds like now, is that?
yeah, the the can be implemented as a a thing that we check.
Sergey 00:33:37 You're thinking how we, how it would it be possible to implant in your user land in Php.
Brett McBride 00:33:42 Yeah, yeah, yeah. Cause I feel I feel like the
at least the interface, if not any implementation, should exist in the SDK.
Sergey 00:33:51 Oh, for example, this interface that will find the how to parse the resulting file. Yeah, we can definitely do it.
Do the all the networking.
Brett McBride 00:34:01 And.
Sergey 00:34:02 That would be more challenging because you don't want for it to block your application right.
Pawel Filipczak 00:34:06 But but anyway, we can. We can anyway implement the you know, the open protocol, I mean the trans transport player, right connection in the Php. And replace it with the background communication, as we are doing for the for the events right? So.
Sergey 00:34:25 Yeah, it will be a little bit of duplicate effort, because, like, you know, like we have with this Grpc thing or Protobuff serialization, that native implementation is much more effective. So
so obviously doing it in native will have a lot of advantages, right? Especially blocking, like the biggest problem here and doing it in user land, because you cannot cache it like, at least if you assume that there is some kind of like external caching that you can cache the result, because otherwise you will have at the beginning of each request you will have to ping the external. This external entity and fetch configuration. You will essentially add latency to each request.
Pawel Filipczak 00:35:03 So that will be a really bad thing at the beginning. If you want to apply the configuration at the beginning.
Sergey 00:35:10 So, but we can think about it like if doing it in kind of like a pure Php is
might be interesting challenge, but we can think about it. Then might be challenged.
Pawel Filipczak 00:35:23 For the current extension. Right? So that that is what Brett want to achieve right now. I guess
so. Just.
Brett McBride 00:35:33 What do I want to share.
Pawel Filipczak 00:35:34 And it will, it would not require our extension right? So it will, just.
and before the contribution of the or applying our our proposal
and finalizing the contribution. Then it will work.
But just wanted to let you know, guys, that the
the backends are just few companies are using open so far as as far I know, so it's still, you know.
in baby early stage.
Sergey 00:36:08 You saw other vendors
Pawel Filipczak 00:36:10 Yeah, there's some vendors, and they're controlling some components. So I I saw some, some vendors are using the Yaml configuration files. And yeah, the control other. This components, not the not the agents
components. So you can, you know, distribute a
many different configurations to many different components with the open. So it's not only related to the to the agency.
Sergey 00:36:37 No, although the in this protocol they always call the other entity that receives this thing as agent. But yeah, what we call agent is a bit different. The lingo here calls it agent. Yeah.
Chris Lightfoot-Wild 00:36:47 So can you ask for a specific
value back from the config map, from OP. Amp. So.
Sergey 00:36:54 Yeah, after you had received this, this is essentially a map like environment variable. So after you parse it.
you can. Then, yeah, you can come. So the way we thought, we will implement this interface is this resolver thing.
So this can be completely implemented.
Chris Lightfoot-Wild 00:37:13 The 1st the key, the string, you said you've gone for like something elastic or something for that. You're.
Sergey 00:37:20 2 maps so sorry for confusion. So 1st map this one is, it should be always string.
1st of all, option names are always strings. Right? So here we also assume. But those are 2 different maps. I just want to clarify
this 1st map.
This is we. We search here for a hard coded string. We search only for specific for elastic. We search a key elastic here, and then we assume that whatever is mapped, this configuration file which has this format, this this is what will contain this remote configuration, and then.
Chris Lightfoot-Wild 00:37:51 We go, and the configuration.
Sergey 00:37:52 Himself, is here.
Chris Lightfoot-Wild 00:37:54 Yeah. So in in the SDK, if you wanted to get that 1st config map. But the the string was like, Give me the open telemetry, configuration format. Is that possible? Or do you just get everything back
from offer server.
Sergey 00:38:09 I I think this is where this what Brett mentioned, this processors will come in right? So essentially when we will have up upstream vendor mutual implementation. It will just run all the registered processors on this
and whatever processor detects that this came from its vendor, then it will then take it, and fetch and extract configuration from it.
Chris Lightfoot-Wild 00:38:30 So it just gets a a bunch of stuff back and iterates it, deciding whether or not you should do anything with it.
Sergey 00:38:38 Yeah, yes, technically, technically, it might have something that we don't know what to do with. Then we will just drop it.
because if it's some kind of like advanced. Maybe it sends something that we don't we, in the version of this particular SDK, maybe we'll edit later, but
maybe it will send something that we currently don't understand right.
whatever it might be in the future. Not just configuration.
Chris Lightfoot-Wild 00:39:00 A different.
Sergey 00:39:00 Configuration and all, and one of the processors understands what key he or it should look for.
and if it finds it, then it will understand that this thing contains configuration
from that particular vendor, then it will know if that particular vendor sends it in Yaml. And it's just not the problem. Is not that content type? Right? Obviously, you can read it from here. The problem is understanding what Pavel mentioned is okay. So even if you know that it's Jason and all the vendors use Json. But you still need to know how to map the keys in this, because the keys themselves might also be vendor specific
you need to know how to map them back to SDK. Variable names right?
Pawel Filipczak 00:39:38 -
Sergey 00:39:39 So that you need, so that processor will have to do that work.
It will have to detect if the that vendor is the one that it's looking for, and then it will it. Then it knows how to map everything back to the vendor neutral SDK lingua.
Brett McBride 00:39:55 So can you just just clarify when you're talking about different vendors? Are you talking about
different vendors? Might have their own implementation of an OP. Amp.
Sergey 00:40:04 Yeah, we're talking about different.
Brett McBride 00:40:05 It doesn't implement.
Sergey 00:40:06 Ui part.
because essentially this thing will come from ui, right? So you will have a ui that allows user to configure this remote configuration.
So
if the options are already exist, let's say why, it's even an issue, right? So obviously, if all the options namings already exist in in all the Sdks of different languages already aligned, and use the same name.
It probably would be the easiest to use that name, and that's it right. But usually it's not the case. Different language might have different names. So that's where it comes from. So usually. What will people do is then in that ui of that vendor. Let's say, data dog. Right? They implement, they have a ui for their back end.
So they will allow users to enter those options. They will create this map
here, that. And they, let's say, the key here will be data, dog configuration or whatever they decide to name it. So this processor, the data drug specific to data dog, you know, vendor specific, remote configuration. It will look for the data dog string if it exists. And it will say, Okay, I can handle that thing.
and then it will know how to parse this, and it will know how to map
all the keys that came from that ui, that is data, Doc, specific.
So what I mean. But dender specific, I mean, back end components
special ui, but it will usually be done in tandem with collector collector will probably will also have some vendor specific thing that will be able to give the agents back this, but maybe it will also be eventually contributed upstream. I don't know what the elastic plans to do with currently, I think it's implemented as additional kind of like Plugin for the upstream collector. There's a pump implementation.
If it will be contributed upstream again, it will have to be then made the vendor neutral, because, like I said, it sets it explicitly. Now, when it generates this map, it sets explicitly to elastic, so it will also have to be made vendor neutral on the server side
eventually, if it's all done. Then maybe there will be some something that will be shared between all the vendors. But
still I think the more flexible approach would be a start. We will need to see like what Paul mentioned. We'll need to see what is the current state of affairs like, what? How different vendors implemented this on their backends.
and then we'll have to find, you know, implement an SDK when the usual way that allows, you know, automatically
fetch it from any vendor.
Pawel Filipczak 00:42:34 Yeah, so.
Brett McBride 00:42:35 Yeah. So if there can be multiple, I think I'll call them OP. Amp servers, which are these vendor implementations. And we are an OP. Amp. Client, open telemetry. Php.
SDK.
Sergey 00:42:47 This link will be.
Brett McBride 00:42:48 It's going to connect to a server. Say, give me some remote configuration. It might get some back.
Pawel Filipczak 00:42:53 Hmm.
Brett McBride 00:42:54 So would would there only have to be one
one like our client would only ever talk, could be configured to talk to one back end server.
one remote configuration server, or one type.
Yes, so.
Sergey 00:43:13 Yeah, I think we should be be able to work to to talk to any type. But
when you configured at any point, because you provided some endpoint at any point in time you will talk to only one server. But, like like Collector, right? Currently, we don't care if it's data dog collector. Let's say it's upstream collector with that dog additions. Or if it's elastic collector, whatever, we just know how to send to collector right?
Yeah, using a.
Brett McBride 00:43:40 But we do need to care a bit because different
different OP. Amp. Servers may send different payloads to us, and that's why we need different processes to understand that payload and map it to
whatever SDK.
Pawel Filipczak 00:44:00 Needs to know.
Yes, that's true. And even that collector. If you are talking to one particular vanilla, open telemetric collector, it might get the config from other many different front ends. For example, if, if if the source of the config, they
may be configured with the different sources, so it may also, you know, send you and attach many different configurations. So it's not
in the protocol. So
the the only thing in protocol that you are getting some data with with some content type. It, I think, can be. And anything in. When I was starting implementing that, I thought that it that those configuration files will be, you know, just a plain file with the environment variable names and and and the values right? Right? So like like a dot and file.
But then I realized that making changes in the ui, it's it's too complicated to pass it everywhere. And you know, a reimplement. The the kibana and configuration options
so.
Sergey 00:45:08 By the way, I'm not sure all the guys on the call do you know what Skibana is? It's essentially elastic. Ui!
Brett McBride 00:45:13 I know. Cabana. Yep.
Sergey 00:45:14 Particular, allows it as an option to configure.
Pawel Filipczak 00:45:19 So make it.
Sergey 00:45:20 It was a classic agents, but now it can also configure open telemetry agents.
Pawel Filipczak 00:45:24 So, basically, speaking, we can't be sure what is the source of the configuration, I mean, is it the collector? Is this? It may be not correct, or it may be some some back end.
you know, somewhere remote back end in. Not I. I mean, not local collector. It may be anything from any vendor, right?
And it's just about probably simple Protobuff. And it may contain any data. And we just need to to implement some smart machines which will register any processor which will iterate through the
to the agent config map as on this, this, 1st on the screenshot.
then decide, based on the on the key from this map is a string. It may be empty, or it may be contained the file name.
and then decide what whatever we need to do with with this
file. It can be empty by name. So maybe each processor should take a look what's inside and check the content type and try to parse it.
And and that's it. So yeah, it's some I know. Notice that some one of the vendors which implemented the open in the in in the front end, they they allowing just to put any data there just to copy, paste the the file.
and it will be sent to the, to the to the component. It might be Php agent, right.
Sergey 00:46:52 So what is the content type? In this case? Text.
Pawel Filipczak 00:46:55 Whatever you you, you will, you? I don't remember exactly what they allowing, but it may be, you know, Yam Json, whatever maybe you you are also allowed to set the content type or choose the content time. I I don't remember because I I was looking into that few months ago, so.
Sergey 00:47:13 But anyway.
Pawel Filipczak 00:47:15 It's just about the protocol. So we, if you want to parse something, if you want to add the support for the vendor specific specific configuration, we we need to
enabled by the smart Api which you allow to to register anything, just anything, and they, and then decide how to apply the configuration.
So yep.
We know from the Java colleagues
that they are allowing the remote options, so they are not replacing the current environment variables as we are doing for the
for the local level. They are allowing some kind.
They they implemented some kind of random runtime options. Those runtime options can be changed in the in the runtime.
So we, if we want to.
to, to allow to change the options in on the fly during the lifetime of the process for the Php for the cli. It it it it's the most important. Then we have to implement additional Api, which is which will allow to to get the option
which is which can change in the during the lifetime of the of the of the process.
So that's the second thing.
Sergey 00:48:28 Yeah, we discussed it in the past, this ability to react of options changing. Yeah, currently, we assume that we only set options per request lifecycle. So we assume classical lifecycle.
Pawel Filipczak 00:48:40 So why I'm bringing it on again. Because this processor is, it must be also aware that there will be some additional
source of the remote options. Right? So if we are, we have the config source right now. But we will. We? We have to implement the runtime options
or or the the Api for the for the runtime options, and also these processors
should have access to to those runtime options and modify them.
So yeah.
Sergey 00:49:12 You mean processors that process this map.
Pawel Filipczak 00:49:15 Yes.
Sergey 00:49:16 You. You're saying those processors in the implementation. They can themselves be configured some way.
Pawel Filipczak 00:49:22 I don't get you.
Sergey 00:49:24 I'm not. I'm not sure you follow. Why do you think, process the way I understood that this processors the only purpose is to detect essential to be to be able to detect which vendor sent us the information right that, and then they know how to convert this into the map
which has this interface right? So essentially.
Pawel Filipczak 00:49:43 Yes.
Sergey 00:49:44 It will create an instance of this interface, which is a snapshot of that configuration, and that's it. They they themselves don't care. You can call them multiple times during even one request. They don't have any state, even those processors. So not sure. I understood. Why would they care about the runtime options? They themselves.
Pawel Filipczak 00:50:01 Because if you, if you have some control for you are starting the span, and then you are changing the option. And the instrumentation basically will
do. Every open span should be closed ended right.
Sergey 00:50:16 Because otherwise it will lead to, to, to issues.
Pawel Filipczak 00:50:20 So if if the config change in the meantime.
and your instrumentation will decide not to close the span, but it it was open previously right.
then it should at least drop it. So it it should be aware that the.
Sergey 00:50:35 So you're saying that instrumentation needs to be aware if it wants to be using the runtime options. Right?
Yes. Yes. So okay, that's.
Pawel Filipczak 00:50:42 Now we should I? In my opinion, we should work on some kind of snapshots, right? So, though all of those options, and are mostly
implemented with with the knowledge that they won't change in the during the runtime of the of the process right?
But if if there is a remote option source, then it may change during the run time. So if the
cli process is long, long running, then it may change, and it may totally change the behavior. So if you are trying to
make the it correct, I mean, implement some instrumentation correctly, then you have to be aware that you are.
Sergey 00:51:26 Yeah, I agree with you. I was just confused when you say processors, I thought you meant this processors that we discussed. Now that know how to extract.
Pawel Filipczak 00:51:35 Yeah, but.
Sergey 00:51:35 Parse this configuration.
Pawel Filipczak 00:51:37 But yeah, but what? What? But how they should apply this configuration? Because if they are applying this configuration.
Sergey 00:51:43 Okay, so you're talking about applying. But we can. We don't need them to know how to apply. They. We can just ask them to produce instance of this type, and then we will be responsible to apply it. They because, like you said, we currently applying the configuration like we currently setting it during as environment variables. That is just a hack. It will not like the moment Chris merges the Pr, we will change that implementation to use the our implementation will just produce instance of this type, right?
And that's it. And from that point on we just need to know how to insert this type into
chain of the configuration sources. So the con, the converter itself, that thing that knows how to extract configuration from the whatever received from Opa, it only needs to know how to create this kind of instance. It doesn't need to know how to apply right? So we will then have a vendor neutral implementation that knows how to apply. So from that point on, it's it should be vendor neutral. We don't need to reimplement it in each processor.
Pawel Filipczak 00:52:44 But what what about the the Runtime.
Sergey 00:52:47 But I yes, I agree with you, but all the rest that you said it. We discussed it in the previous meetings. Yeah, definitely, if we want to support ability of changing options during the same life cycle, then yeah, whatever wants to have this ability, they need to understand that they need to be aware that options can change, so they need to adopt their functionality so that it doesn't create inconsistent results like you said, unclose spans or whatever.
Pawel Filipczak 00:53:13 So, in my opinion. Now we should not modify any of the options. We should.
Sergey 00:53:18 Right? Right? We're not going to. The the way it will work now is that we will only provide. So if we go back to the the way we envisioned.
If this is what let's say, this Pr is merged. So we essentially will introduce additional implementer of this interface
currently, as we said, because we don't have priority ability. So we will go with the same approach as done here. We will just go and hide the all the other sources by calling them directly, including this source.
Right? So our new implementation will just call directly in the 3 sources and does, it will essentially hide them, because it will 1st check the remote configuration, then it will. Then it will drop back. Essentially. Use those as a fallbacks and and then, that's it. We will just in use this bi.
Pawel Filipczak 00:54:10 One question here. How many times it can be queried for the option value, I mean, is it cached.
Sergey 00:54:15 It can, it can, many times, but but it doesn't matter, because the the option will be coming from the snapshot. That that map that we will use it will not change you from the start of the request. Right? We'll load that map at the start of the request, and then we will not read it again.
Pawel Filipczak 00:54:30 Updates, yes. Okay.
Sergey 00:54:31 Right. So for the whole request. So the for classical model.
it will work fine. It will also work correctly for the long running. Like you, said Cli. Right? Let's say, if somebody uses react. HP, and they're serving sounds of requests
during the life cycle of one request, which is from Php point of view.
they will not be able to see new options right? So if you ever react application, that runs the same process for our you will see. See you will still continue using the same configuration that was at the beginning of the tower. You will not see any changes.
Pawel Filipczak 00:55:05 Okay.
Sergey 00:55:06 So if you want them to meet to be able to see changes, then we need to change like you said all the all the instrumentations that want to be able to update, they will need to implement this new interface and be aware that if they need read now, a new snapshot.
using some new interface that they say, Okay, give me the most up to date snapshot. Then, yeah, they need to be themselves being able to cope with the fact that this new snapshot can be completely different from the old snapshot. Right? So whatever is they have in flight, like
not close spans, or whatever they will need to. So probably the obvious solution to that will be for them to read those new steps at the point where they don't have anything in flight right when they closed all the spans and everything else, so they that will make it easier for them to apply this new configuration.
Pawel Filipczak 00:55:53 Got it.
Chris Lightfoot-Wild 00:55:55 You mentioned in the past about like a configuration object, because currently, probably you expect a scale of value like you do a billion check in your instrumentation, and then you just keep it because it's never changed before, whereas you probably do need like a new object.
But you can introspect when you need it.
Pawel Filipczak 00:56:14 Yeah.
Chris Lightfoot-Wild 00:56:15 So that that does make sense.
But to me at least.
Sergey 00:56:19 Sorry. Did you say, Boolean? Value.
Chris Lightfoot-Wild 00:56:22 Pardon.
Sergey 00:56:24 Sorry. I don't think I heard you correctly. Did you say Boolean value, or.
Chris Lightfoot-Wild 00:56:29 Well at the moment, in in instrumentation, you might query configuration, for you know, Flag, is this feature on or off.
and you just get a Boolean back, and then you might have just, you know, stored that as an instance, variable saying, I I'm not in this mode.
but that might change later.
And and if you've already kind of, that's the kind of cash you were talking about. If you've already kept that value somewhere.
it's not dynamic anymore.
Brett McBride 00:56:54 That's true. But but all of our Sdks not currently like it's set up once and stays that way forever. Which is what Sergey was talking about with the.
Sergey 00:57:04 Right. So, for example, the most obvious thing that we can easily implement to be responsive to the changes is background thing, right ambient, like, for example. And this is what was my. My second question. Kind of brings me, because essentially what we want to achieve.
what I mentioned, the 1st option that we implement is login level, right? It seems that it should be easy. It's even should be transparent, like we don't need much changes, because, like login level can change, and all the components that call. They don't assume that login level is the same as it was at the beginning of the request, right. So they call this methods. And even if you call the 1st this method first, st and then you call this method. If if login login level change between those 2 calls.
That's fine, like, okay? So obviously, you will like if you log in during one request. Yes, you. Maybe you will have logs on info level during the 1st half of the request, and then suddenly, the second half of the request, you will suddenly still start seeing debug log levels because the log level was increased to debug right?
But that's fine. That's what we want to happen. But currently it will not happen. Because, like you, said Brett, we are catching that value. So if you go to the login, so that was my next question is so more immediate one, since we sorry, let me log in.
so I don't know if it was on purpose, or a login.
or if there is, maybe some issue with this. But currently login level here is read explicitly from the sources. We don't use this new spi ability to read from the configured sources.
I wondered, what is that? You don't know, guys? Why? Why, it's like that, is it just because it was not important to change? Or is there some issue of having login also use
spi?
So essentially reading from the configuration, instead of explicitly for configuration sources directly.
Brett McBride 00:59:05 Don't remember. But my best guess is that because logging happens
much earlier, we want to log things from as soon as possible. Then we? Then we've bypassed Spi, but also this predates spi.
Sergey 00:59:20 Right?
Yeah. So this is what I wrote to myself.
Brett McBride 00:59:23 Fix it.
Sergey 00:59:24 Oh, yeah. So the so what you're saying is that we might have a chicken and egg issue right? So login might be kicking in much earlier so, and it will cache it like we explicitly see that it will cache it in the in the static thing right? And then it will not read it later.
So we need to find. So if we want ability to change the login level from remote, we need to find some way then to reset it. So at least at the beginning, like So
so I wonder, like, okay, so I guess
I wonder how it can be done so. I guess we can maybe contribute a separate Pr, I was just wondering we can read. We can set it to some default if we well, it will automatically probably happen.
I wonder, how do we? By the way, how does it work with defaults? Currently, with this.
Brett McBride 01:00:15 I don't see why that couldn't use spi. Similarly, it's just like it's.
Sergey 01:00:20 Yeah, it could. But like you said.
Brett McBride 01:00:21 Not configured. Logging lives in the Api as well remember. So logging is is sort of
not part of that SDK auto loading code, because
things. Yeah, because logging is part of the Api
and not the SDK, I think.
Sergey 01:00:42 All right.
but this one is hard coded. So are you saying that you can register different implementation for this? Because I thought this whole mechanism for login is currently it's all it's not like. You cannot inject a different implementation via spy. Not not that I think it will be right. Approach here. I just, I just thought only to be able to change
the level we are. So we are the the same way as we change it. Like we are, this composer resolve, composite, composite resolver. So essentially, I was thinking, how can we make login current login implementation to use
a composite resolver to read this log level, and also not only read it once, but like, I said, because it might be called at very early stages, so the 1st time it will ask for the level. Maybe the remote configuration will not be available yet, but maybe if we can
oh, I think it will, because
but maybe other sources might not be able. But so, if we want to, I wonder, like what would be the point, that at which we can ask the Login to reread the the level.
So we can kind of like reset the level. So it will start at the beginning, probably using default because it it can be called the really early stages, even maybe by one of the configuration sources implementation itself. Right?
So we don't want to create this chicken and egg problem. So we need some initial level that will not depend on the configuration.
But then we need to find some point in the control flow where we can ask this login. Okay, let's reread
the level. So it will be from the most up to date source at that point we we can assume that we already have all the configuration sources registered or loaded up.
Brett McBride 01:02:27 Yep.
Sergey 01:02:28 So.
Brett McBride 01:02:29 That seems simple enough for that example.
And I suppose that is a good thing to to be able to change remotely.
yeah. But I mean, I I feel like it's it's gonna be a lot of work to have runtime modification of
a lot of the rest of the SDK,
you know, if I want to change the batch, spam processes
queue length, or something like that is
Sergey 01:03:00 You know, like I said.
Brett McBride 01:03:01 I'm sure I don't worry about
be done, but it just it sounds right right, like a lot of work.
Sergey 01:03:07 Let's keep in mind that again, it's only relevant to the models such as react Php, right? So classical models like laravel, symphony, or whatever Wordpress
the model uses classical Bp. Lifecycle, where each request is, runs. Once, you know, one HP request runs one logical request
that will automatically work correctly with remote configuration, because on each Php request we will, we will use when we inject so essentially, let's say, assume that we implemented this additional resolve. Interface. So this resolver interface will use new we'll use new snapshot for each HP request. Right?
So this snapshot will only survive during the life cycle of this request right? So it will stay constant, immutable, but on the next request it will use the most recent one.
so it will see the new values like. If the so, each request will see the most recent values
for normal applications, like, let's call them normal, and so on. So yes, for applications such as react Php, those that run many logical requests during the one Php request that gonna be an issue.
But yeah.
Brett McBride 01:04:22 Beautiful.
Sergey 01:04:23 So in order to support that model, we will need to somehow decide how we
have kind of like some kind of like a session concept right? And then when you run multiple sessions, because obviously that react PP, thing, it can have it can have multiple sessions in flight, existing at the same time in memory, like with classical Php model.
you cannot have that. You only have one logical request. Right? You work with particular client at the other side. So there is one session. So you don't need that ability of having, you know, multiple. But
so if but Reactp can have multiple requests at the same time some requests might last for a really long time. Right? So you don't want to affect them, so you cannot just globally change the configuration for all the in flight requests. So then, you need to somehow scope them separately. So whatever globals we use like, for example, this static here, right
that becomes like in login case it doesn't matter, because login is ambient service. So even if you change it for all the in-flight requests.
they don't care because it's just login. They are not aware what is the level, anyway. So if it changed in the middle of the request that they will be fine with that. So ambient services login is actually will be okay. We can even change them. You know, being able to do that. But let's say, in order to apply runtime we need.
So we need for the login to ask for the new value at some point every time.
But let's put that aside. But yes, things like instrumentations, like the ones that create spawns and all that.
We cannot just go and change the whatever statical globals they use, because if we do that, then it will affect all the in-flight requests
that are currently happening. So if you're in the middle of creating spans like Paul mentioned, and you suddenly change your configuration. Then maybe you will not close spans because your configuration says it. You're not supposed to create that span, anyway. So you will assume that you didn't create it. So you will not close it. So the whole thing becomes, yeah. So you essentially need to be whatever globals you use, you now need to make all of them to be somehow pure. Request right?
Scope them per request. You cannot have any globals almost, unless it's like.
Brett McBride 01:06:39 I know we're out of time. But but I was just having an idea while you were talking, which is that perhaps we could replace, let's say, an entire rebuild, and replace an entire trace of provider with a new tracer provider.
Oh.
so we've changed. We've changed some things. We've changed the batch span processes queue length which I just mentioned before. We've got an old tracer provider.
We create a new one that is configured differently and contains new everythings.
Can we just globally register that one? Anything that's got a reference to the old one? We'll keep using that. It'll still use the traces that was using.
but anything that starts again like any new.
Sergey 01:07:32 Let's discuss that, unfortunately, myself not familiar. But, for example, will trace a provider account for the instrumentations like, do they keep? Each of them keeps like, because, like, for example, let's say you have my sqlite instrumentation, and it has some values there that define how it should behave right should it capture this span, or whatever? Right? So it says, some configuration options.
Now, I don't think it uses trace provider in the sense that so the moment you change one of the options, and you have only one global instance of Mysql instrumentation.
Then you have problem. Right? So what happens like if you have my sqlite polls in one request and another, so the moment you will change it, it will affect all of those requests that are currently in flight, because you only have one instance of Mysql instrumentation.
So maybe trace. But I'm not familiar with, like what state this provider keeps.
Brett McBride 01:08:28 Well, also tracer providers sorry instrumentation should get things from the globally registered tracer provider. But we also have a
what's called a cached instrumentation.
So we could probably clear that cached instrumentation.
there probably are instrumentations that are being lazy, and I probably wrote some of them, and just have a static.
try. Let's say tracer provider
But they could be updated to to not do that like I I'm I'm sure it's actually in the spec
that you should do this.
Sergey 01:09:10 You're saying that, for example, if you, if we have some, have some configuration that affects instrumentation, behavior like tells it, which spans to create which spans not to create.
You're saying that this configuration should be kept inside tracer provider, and then instrumentation should query it via tracer.
Brett McBride 01:09:26 Instead of keeping it.
Sergey 01:09:28 Directly.
Brett McBride 01:09:29 No, I'm not saying that. No, but I'm saying that if
some of the things we're changing at Runtime relate to traces.
then that's all encapsulated in a tracer provider.
No trying to change the runtime configuration of an auto instrumentation module, different problem.
Sergey 01:09:52 Yeah, I guess I need to look at it. Maybe you're right, like, I'm not 100%. But yeah. But the is the question, where? Where? When? We want to? Work on that like, what is the importance of this use case? Because, like I said it, it's really specific use case, right? It's for applications such as use like frameworks like Php, right? The ones that try to run multiple logical request and say inside the same. Php. One.
So we need to decide like, if it's something that is with priority of that.
But yeah, it will come.
Brett McBride 01:10:22 I feel like the easiest thing is just.
you know. If you, if you notice configuration changing, hit the self, destruct button.
start yourself up again, reload configuration.
Sergey 01:10:33 When you say use who should hit this button is the key.
Brett McBride 01:10:39 yeah. Well, I'm I'm not sure what the what the mechanism is, but it just feels like that's gonna be significantly easier.
Sergey 01:10:46 Yeah, you're right. Probably like, if you
to finish processing all of your requests.
But then you need to ask
yourself how frequently those process leave like 4 h like, and do people care like, maybe people will say, Okay, yeah, my application. Use crack. Php, and I change some options. But I'm fine like if I have lifetime of each process 1 h, and I only see new values been reflected after 1 h when processor is started.
I can live with that like.
Brett McBride 01:11:15 Yes.
Sergey 01:11:15 How frequently do people, you even change the configuration? Right? So it's, I think, like you said, because it will require such a not small amount of effort. Maybe it's 1st seen.
What are the use cases when people start complaining like using this remote configuration? Because, you know, multiple, it should be confluence of multiple, you know, to construct this use case. It should be like people use reactp or something, and they want to change remote configuration. And they want to. You know, the changes to be reflected really quickly.
So maybe it's non-existent a combination of all these factors. So then we don't.
Brett McBride 01:11:51 I'm using.
Sergey 01:11:51 Spend that effort right?
Brett McBride 01:11:54 Yeah.
Sergey 01:11:55 Yeah. The last thing I wanted to ask, though, how much out of time we are.
Brett McBride 01:12:00 A little bit. That's something that.
Sergey 01:12:04 Will.
I guess
the last thing I just wanted to ask. Maybe all the rest is maybe less. Yes, I wanted to understand, because I saw that there was mentioned that the instrumentation themselves should be registered using spi. Because why? Why? I encountered that because in in in this implementation I saw that we have. Still, we have this additional type that's called. So. We have this resolver that is kind of like a snapshot of configuration right? And then we also have this. Component.
let let me quickly find it. I think it comes from out the loader. So it's SDK.
Chris Lightfoot-Wild 01:12:42 Provider.
Sergey 01:12:44 Excuse me.
Chris Lightfoot-Wild 01:12:46 The component provider.
Sergey 01:12:48 No, it's not provider. It's something to do with the options, something like. So it so when we load the configuration, this load, let me see.
So here we're in this configuration, and it implements a different interface. It implements config properties here.
So I was just wondering, and then it is passed to the instrumentations. But if I understand correctly, this will be passed only to instrumentations that implement this that are being loaded via spi, not the old way. When you have this relying on the when you rely on the composer to load them, using this register file right? Essentially using this global loading.
Brett McBride 01:13:30 That's related to Yaml. Configuration.
Pink.
Sergey 01:13:38 It will. It's I thought, that it will be possible to register.
So for instrumentations, we don't have any plan. So the way the way instrumentations loaded currently using this register file underscore register, I mean.
where? Where do I have it here?
So do we have any plan of changing that, or it will, and make it via the Spi, or will it stay like this? So currently, the search file is mentioned in Composer Json, right? And this is how it's being loaded.
But then we don't control the order. Right? The issue was the order.
Brett McBride 01:14:16 I don't think the order of
instrumentations being loaded is a problem. The the race condition that's problematic is
Sergey 01:14:31 Because the instrumentation will reference. SDK, right? So it's really whatever instrumentation
references SDK for in this sequence it's not gonna in any way invoke that race condition
or that it will basically the first.st The 1st thing to get a tracer.
Brett McBride 01:14:53 Or emitter span, because we've sort of got some lazy.
What are they called late binding traces or tracer providers?
Basically, as soon as something tries to create a a span
that causes the SDK auto loading to run.
and then any anything that hasn't been loaded yet through composer auto loading is
is too late at that point.
Sergey 01:15:32 So. So let me ask you, for example, this. So here the instrumentation at this point already wants to know if it should be loaded right? So it already reads configuration at this point
do we know that at this point the sequence that is being run by Spi to create this chain of configuration sources.
All this Spi sequence of, you know, traversing all the composer Jsons. At this point. It's already done like we can assume that this will not be run before Spi already created. The right sequence of the configuration sources.
Brett McBride 01:16:05 Yeah, because spi runs on composer auto load dump. So a
it's pre-done before a request even runs before phps run.
Chris Lightfoot-Wild 01:16:17 Well, there's both, if you enable the plugin yes, if you don't enable the plugin no, it won't have happened.
Brett McBride 01:16:24 That's great!
Chris Lightfoot-Wild 01:16:24 The race condition that we were trying to avoid.
Sergey 01:16:29 Okay, but are we? We also want this pi to work, even if you don't enable Plugin.
Is that not a absolute precondition like
Spi, should also be able to work without enabling it.
Brett McBride 01:16:40 Does work without it, but it still could suffer from a race condition, because it's
it's now generating things at Runtime, because it wasn't allowed to pre-generate them.
Sergey 01:16:54 So if we if we switch this way into spi, then we will solve that right. So whatever. So if spi, if if so, you saying spi can work without the plugin being enabled.
But in this case, whatever is registered with spi, the order will be correct. Right? So so if we. Instead of using this mechanism, we'll also register instrumentations using Spi, then
we it doesn't matter if Plugin is enabled or not, it will work correctly. There will be no race, right?
Brett McBride 01:17:27 Yes, I think so.
Sergey 01:17:30 I was just wondering. Let me ask you different differently, like I'm seeing in the code that it does assume. Maybe I misunderstood it. But here I see that it loads all the instrumentations.
and then using spi right.
So that means that there are instrumentations that you that are registered themselves using spi, or it's completely different workflow. And it's not for the I misunderstood it. It's not for the instrumentation my sqlite.
Chris Lightfoot-Wild 01:17:58 I was. Gonna say, I've got a draft quite an old, maybe outdated. Now, draft Pr, that I put a link to for the Laravel instrumentation to use Sbi
as an early proof of concept
which shifts to using this instrumentation provider stuff.
Brett McBride 01:18:15 Yeah, I think I think we do want to get to using spi but we don't
currently use spi for for instrumentations. And the code that you're looking at. Sergey is related to configuring
components through yaml config.
But it's it's theoretical, because until
like that, there's an example of how it works in in our tests, Directory or Examples Directory. But it's not.
It's not implemented.
Sergey 01:18:50 So this is the way to do it via yaml configure, I thought, it's done via the code, or is it in conjunction with some yaml file?
Brett McBride 01:19:00 So you can configure instrumentations through through Yaml. That's part of the declarative configuration spec. And there's there's a section there for it. And so we've
done some of the work
so that you can do that. You can set any any configuration that you like
to configure any auto instrumentation.
but no auto instrumentations in the wild. Use this yet it's it's still
a thing that we can theoretically do.
Sergey 01:19:34 Okay, I see so essentially what? The only for now I think it only matters in the sense. So do we know, like it's if I followed the code, I think it still will use the correct flow for creating this config properties. They will be based on the composer, not composer, on the composite resolver. Right? If I'm following the code correctly, or maybe I not like I was just wondering.
Chris, maybe you will. You know the answer to that like is this flow the the way this config? Because it's it's quite this interface, quite similar to the
to this resolver interface. Right? Essentially represents configuration snapshot.
Am I right? So this interface, it's just done instead of 2 methods. It's just here. There's 1 method, but essentially the same thing, right?
Chris Lightfoot-Wild 01:20:27 It was. Is this slightly different, though? Is this for the configuration file that it was added in? And then that was first, st and then this other things happened later.
Feel like there's probably a bit of consolidation to do here.
Sergey 01:20:40 But the question other than the
to yeah, to, to maybe consolidate the files that have very similar interfaces. But the way it will work. Now, will it load the configuration also? That comes
1st of all, like, what
if you look at this flow like it's it's only used correctly. Are you saying that this flow will only invoke when your configuration file is like this? Configuration declared. Your configuration file is.
excuse me, is configured.
Brett McBride 01:21:07 Yeah, think that's right?
Sergey 01:21:10 Oh, yeah, you're right about that. Maybe plus exist.
Brett McBride 01:21:14 Yeah, yeah, cause cause implementations don't currently
implement instrumentation class or or have that register method. So.
Sergey 01:21:26 Now, you don't have any instrumentations to actually implement this interface.
This one.
Brett McBride 01:21:30 One testing one example, one in
Yep. So if you were to look up things that implement that you'll find one in the core repository in examples, that one example is.
Sergey 01:21:45 No only example, no production, that I do.
Brett McBride 01:21:47 That's right. So that's that's theoretically how it can work.
But no, nothing, nothing influenced that yet.
Sergey 01:21:55 And then people will register it the way you register the in what you sent Chris, the way you will register when you implement this interface, you will register it, using that discode.
and then.
Chris Lightfoot-Wild 01:22:09 Yeah.
Sergey 01:22:09 Okay, I see.
Oh, so we have a production one in this Pr in this branch.
Chris Lightfoot-Wild 01:22:16 Yeah, it's it's quite sterile now. So need to pick up on it. But yes, it's the that interface there and then the liable instrumentation is using that Yaml based config.
Sergey 01:22:28 Right? So, okay. But it seems that again, like, if I'm seeing it correctly, those things don't necessarily like the orthogonal. You can have this interface. Without even Yaml, this declarative, you can get this configuration, even if this option is not set
like I see, going to the flow it works in either case.
Brett McBride 01:22:48 But we but yes, or they need to have sensible defaults, because I guess we're going for
so to read it from here.
Configuration as well. So we do do some configuration of
auto instrumentations. And people just invent an environment variable for that purpose.
And yes, we could do that as well.
Sergey 01:23:13 Right? Okay, okay, no. I was just wondering essentially my question. Maybe I maybe misunderstood me. My question is essentially, let's say
we don't have this option set right. So we don't have declarative configuration file. But we have. We do have instrumentation that implements that interface the way Chris implemented. Let's say that lot of will change will make it to the to the main.
So my my question, then, is
the configuration that then will be passed to the lateral? Will it be read, using the same chain of configuration sources?
The way, like with this composite like, will it read, the configuration will be read using the same sources based on spi.
Like. Judging by this flow, it seems that it will be read using this branch right.
Brett McBride 01:24:01 Yep.
Sergey 01:24:02 But then I'm not sure I follow like, then we do load something from spi, but we load different interface, like, I don't see that we use this composite resolver, and I wonder why, like, if the purpose is to so I guess I'm missing maybe some understanding like, why, if this represents the configuration.
Why we not just call
composite resolver, get whatever it. Maybe we need to change it to a different interface. And that's it right? I see that we explicitly call in the resolver right instead of using composing. But that's a different one.
That's not okay.
So maybe I'm missing. Why this flow
should this flow use the composite resolver
to get the configuration, or it's not configuration in the same sense.
Brett McBride 01:24:48 It's not the same configuration that is very much coded to work with, and only with
the Yaml configuration file.
Okay, so you're saying this, if here is a little bit misleading.
Sergey 01:25:01 So the fact that we can drop into the flow where Yaml is not configured
that's it will still try to somehow simulate Yaml is is the purpose of.
because this, if I understand correctly, this is the branch where where we go when
this variable is not set right.
But you know, if we're out of time we can. We can get to it later like that.
Brett McBride 01:25:34 Yeah, yeah.
Sergey 01:25:35 I don't think it's that important, because, like you, said, we at the moment, we don't have
any instrumentations that follow this work, this flow. So
I guess it's I was just wondering. I've tried to see like if whatever I saw configuration being passed around. I was just wanted to make sure.
Yeah, you're right.
Goes through the same workflow.
Brett McBride 01:25:56 Didn't write this, and I don't
completely understand it, and I haven't looked at it for quite some time.
It does look like it's getting
something from the environment. But I'm not sure how. Not sure how that works.
Sergey 01:26:11 Yeah, I I will. I will take a look at it. Maybe I will have some answers for our next meeting, but I don't think it should be
stopper, for now, I think. Thank you very much. I think I got answers to most of my questions.
So what guys are your plan with the Pr. That, Chris you are working on? Is that something that you plan to merge in and release SDK with it?
And like, what is your guys plan like we? You have this 2 weeks branch. And then this pr, like, what is the near term plan? Do you want to merge this into the one X branch, and then later
have it as part of 2 x. But for now it will be part of the one x. And will be released.
Brett McBride 01:26:54 Think Chris's branch probably can go into 1 point X.
It didn't introduce any breaking changes. Is that
think that's right, Chris, like it. It predates 2 point X. So it it must have originally been written against
what our current main line.
Chris Lightfoot-Wild 01:27:14 Yeah, I think the main thing it gives is the support for dot M. Files for
symphony and V. Lucas packages.
Which a few users have kind of asked for, I guess.
Brett McBride 01:27:28 Yeah, I think.
Chris Lightfoot-Wild 01:27:29 And obviously the more.
Brett McBride 01:27:30 Talking about.
Chris Lightfoot-Wild 01:27:31 What's that? Sorry?
Brett McBride 01:27:32 Which pull request are we talking about? Because you are also just looking at spi, for which was.
Chris Lightfoot-Wild 01:27:40 I don't mean that one sorry I mean the the one in
of the men in the Api SDK.
Brett McBride 01:27:46 Oh, yeah. Yeah.
Chris Lightfoot-Wild 01:27:48 In core, I guess. Sorry. Yeah. So that one
adds that support. And then obviously, our pump is like a
newer concept to me at least.
that makes sense to build on it.
Now that you've got support for it in the distribution.
Sergey 01:28:07 Right? Yeah. So the way you implemented that the Pr it should be compatible like, obviously, it's not the perfect in the sense like, we said, we miss the priority thing, but
it still can be done right. We can follow this example like you did.
which is completely shade all the rest of it. So we'll always know what is the sequence.
That, or at least we don't need to know what local is composed. So essentially, we will rely on the fact that this SDK instrumentation will.
this class will know?
It will essentially be responsible for loading local. So we'll defer to it. So if it's not in the remote, then we will defer to this, and that's it.
and there will essentially will be 2 sources. Right? We will consider this to be a local source.
whatever is not on in a pump, then we will fall back to this source.
So this way, we will enforce the the order.
We'll just explicitly call this class.
if it's not a good mode.
Chris Lightfoot-Wild 01:29:06 So I guess, already reviewed it then, unless there's any changes on that like, I've not touched it for a while. So it's I guess it's kind of up to you, Brett, if you happy for it to go in or not. But.
Brett McBride 01:29:17 Probably. Yeah. I just haven't looked at it for a while.
Sergey 01:29:21 I remember we also discussed like, if you you wanted to adopt it, to be able to work outside, like if it's called from distribution instead of from the application.
So I wonder if you we I mean
I can try it and give you feedback I didn't try it yet. So it would be interesting to try. Maybe it works like, maybe
I was just wondering like, when you please go ahead.
Bob Strecansky 01:29:47 So sorry, so sorry. I got a 9 30 meeting. Thanks for discussion today.
Sergey 01:29:51 Thanks, Bill.
If you need to drop, we can discuss it again. It's not so, since it's already different topic. It's the implementation of dot and been able to load it
for the destroy kind of like deployment use case when we essentially deploy the the open telemetry outside the application. It's not. It's not deployed as part of the composer of the application.
Right? It's not a vendor inside the vendor folder of the application. It comes. This, the case comes from vendor folder that we distribute with the elastic distro.
So then I guess what will happen is that you will have multiple. So I don't know how you search. I need to look at your code. How do you even know how to find the root of the application where the 10 files should be located like, if it's based on the location of
vendor out alone, like for composer.
then maybe there will be issues, because we will have multiple instance of the composer, one that comes with the application, and one that comes with the istro right.
So I can. I can try it out. And if it doesn't work, I continue. Maybe I can create a a simple docker for you if you want to look at the docker and reproduce it
about the.
Brett McBride 01:31:05 I mean.
Sergey 01:31:06 If you want to match it as it is.
Brett McBride 01:31:08 Yeah, I've I've been playing with.in files something like he described there. That that help
at my work. We have just one big Apache server, and just everything's in a directory. So you know.
So you get a service slash app one service, slash app 2
and the way I was thinking about doing dot inv.
for that is just like literally in the the script.
But extract a script file, name
or the pair, whatever the current Php script is. Look in that directory.
Sergey 01:31:50 are you? Are you asking me or Chris like? Chris? How do you? What do you use to locate that token file.
Chris Lightfoot-Wild 01:31:58 What does the.in file come from? Well, the Spi stuff loads from the local vendor directory.
Sergey 01:32:06 Alright, identify.
Chris Lightfoot-Wild 01:32:10 Oh, oh, sorry! Just the the route, the current directory.
Sergey 01:32:15 You see, who's going direct, is there?
That's interesting point.
Chris Lightfoot-Wild 01:32:21 It's only because that was copied off whatever Nive's SDK was doing, so it might be changes in that.
Sergey 01:32:28 Okay, it might even work like, it's interesting question. I don't. We can try it on like larval. And
it might even work like.
yeah, I don't know what, Brett your example you gave when you have the supply chains you want to use the script name like, will it also work the current directory thing.
Brett McBride 01:32:51 I don't know.
What would the current working directory be if you were running something in a subdirectory?
Maybe I'll have to have a look at that.
Sergey 01:33:03 Good question like, I don't know what Apache, if Apache does. CD like to the Directory?
Brett McBride 01:33:09 Yeah.
Sergey 01:33:11 Good question.
Brett McBride 01:33:11 For the average application I'm trying to get to. You know, it's public directory where index dot Php is, which is the gateway to to everything. So I'm kind of
assuming that the.in file should be in the same places.
Your index file.
Sergey 01:33:32 Yeah, that's that's true. But the question becomes like,
do you do? CD, like, or do you provide the pass to that index file, like, so, yeah, we need to check like that will be interesting if it will work without distor, like in
normal. So then, if you just use the those index files. So you install SDK separately you install it like, and you load it using preload like, how do you load the open elementary? SDK, if you have
multiple index files.
Brett McBride 01:34:06 And you any any single application, should just have one index file
or at least any modern one.
But in in the situation I'm describing on one of our, you know, our old servers.
each subdirectory is a completely self-contained app. I don't think they have any shared resources or anything, so probably should be using V hosts. But isn't
Sergey 01:34:38 So you install SDK, also, you have a separate install installation of SDK in each subdirectory.
Yeah, they've all got their own vendor. Folder. Yeah.
Oh, okay.
okay, interesting. I mean, should work. And then it doesn't not care if it's a subdirectory. But yeah, we need to test it to see if there will be some corner cases. Yeah.
but that's it for me. Like, if you guys need to go. Thank you very much. It was very helpful.
Chris Lightfoot-Wild 01:35:09 Thanks. Getting quite late. Here. So.
Sergey 01:35:12 Okay. Thank you.
Brett McBride 01:35:14 I'm fighting.
Chris Lightfoot-Wild 01:35:16 Thanks very much. See you later.
Brett McBride 01:35:17 All right.
Sergey 01:35:18 Bye.
Brett McBride 01:35:19 File.
