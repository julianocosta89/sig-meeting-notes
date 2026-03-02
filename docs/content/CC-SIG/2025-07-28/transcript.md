SIG: OpenTelemetry C/C++ SIG
Date: 2025-07-28
Duration: 41 minutes
Zoom Recording URL: https://zoom.us/rec/share/eE4gvopltjpwwPLKKr5GDBwUVHzFnwdim709KElNzwNwE_KYcuLldNlAEsWitznf.5iYwwB4oijvuVjue
============================================================

## Zoom Recording Transcript

**Marc Alff [MySQL]** 00:17 Hi doug.
**Doug Barker** 00:20 Hey, Mark, how's it going.
**Marc Alff [MySQL]** 00:22 Not too bad!
I see you have been busy.
**Doug Barker** 00:27 Little bit. Yeah, you are you, too? You have a tough?
Yeah, I know yours.
**Marc Alff [MySQL]** 00:38 Let's see if I can share my screen.
Okay, you see, it.
**Doug Barker** 01:10 Yeah, I can see it.
**Marc Alff [MySQL]** 01:15 Well for once I don't have any anything special, so I didn't put any notes yet.
So yes, I meant to say thanks a lot for all the good reviews.
**Doug Barker** 01:40 No problem. Yeah, hopefully, it's the right level and helpful.
**Marc Alff [MySQL]** 01:45 Yeah. Oh, it definitely is. And
you are now officially the second
the second best for people knowledgeable about the Yaml configuration file.
Hi, Victor.
**Victor Lu** 02:19 Hello!
I'm just here to see what's happening to the them.
The memory language.
**Marc Alff [MySQL]** 02:33 Sorry I missed that. The memory! What.
**Victor Lu** 02:36 Oh, no, I I heard a lot about the
memory safe versus memory and save language.
Just want to see what's happening to this site.
**Marc Alff [MySQL]** 02:52 Okay.
I think that it was
online earlier. So hope he would join.
And I have no idea if Ethan or Tom can join today or not.
Oh.
**Victor Lu** 03:48 Just notice your mark. You're from oracle.
**Marc Alff [MySQL]** 03:52 Yes.
**Victor Lu** 03:53 Okay, yeah, I. I'm ex oracle.
**Marc Alff [MySQL]** 03:56 Oh, okay.
it's a. It's a small world.
**Victor Lu** 04:03 Yeah, yeah.
**Marc Alff [MySQL]** 04:10 Do good. You had any special topic to discuss or.
**Victor Lu** 04:15 I'm a generalist. I'm or I was a database consultant. Turn a generalist right now. Just anything.
Anything AI, and and security being one of it. The reason I'm interested in
this meeting is, there are still a lot of it
applications still written in CC. Plus, you know, oracle being one of it.
**Marc Alff [MySQL]** 04:39 Okay.
**Victor Lu** 04:40 For good reason, like, high performance.
Yeah. So I'm just seeing what is the what is the best practice? Basically.
**Doug Barker** 04:57 I don't have anything special for this meeting, mark.
**Marc Alff [MySQL]** 05:00 Okay, Hi Hassan.
**Ehsan** 05:10 Hi! Everyone.
**Marc Alff [MySQL]** 05:22 Okay? So just for clarity, this is the open telemetry C plus plus team meeting.
where we discuss mostly the implementation of open telemetry. Cpp itself.
But of course we can also discuss things like in open telemetry in general, because it's part of a bigger project.
And with that I don't. Yeah, I don't know if Lady Tom will join. So I guess we can start.
Typically, what we do is go over the issues that we have the different Prs that need to have good review
to see what to do about them, and then some general discussions.
And of course we can also have some
general question, if you, if if we need so feel free to ask
Isan anything you want to discuss in particular.
**Ehsan** 06:34 No, no, nothing special for me from my side.
**Marc Alff [MySQL]** 06:37 Okay.
**Victor Lu** 06:38 I have a general question about maybe not even just open telemetry in general.
So the in in the database world there is a concept of aggregation
right to to get performance. Matrix
in the open telemetry already there is such a
like, get a aggregation of a of a performance matrix.
**Marc Alff [MySQL]** 07:07 Well, there's in open telemetry in general. There is the metric signal, which is meant to collect things about the system.
so especially if you have a database. Yes, it can be used to actually collect data from the database
and to record that in the back end, so that you can do some.
and graphing, trending alarms whatever you need, based on those metrics. So yes.
**Victor Lu** 07:36 So so in in the for example, in the Orca system, called oracle weight interface
which is in memory aggregation of the of the matrix to give you
like detailed. Let's say how how much time is spent on CPU versus I/O versus memory networking right those weight classes.
Is it possible? Using open telemetry to pretty similar
aggregated weight classes for an application.
**Marc Alff [MySQL]** 08:12 So. In general. Yes, this is what the the metric signal gives you.
as far as instrumentation in the oracle database itself. I cannot answer that directly, because I don't, even though I'm part of Oracle, I don't work in the on the Oracle database itself. I happen to work on the Mysql database.
**Victor Lu** 08:38 Yeah, but actually, that's probably I think it's probably true for every database
like you, you can have a
have a like a like kind of view of
of how how the database is running right. You can find out pretty.
**Marc Alff [MySQL]** 08:55 Tools.
**Victor Lu** 08:56 Session.
**Marc Alff [MySQL]** 08:57 Yes, definitely so. First, st
there, there is one for any system, whether it's a database or something else. There is one part which is to actually instrument the code for the application itself.
even when the application is the database engine.
So you instrument the application to
to produce metrics and then open telemetry will collect that.
put that into a back end and then allow us to do some
every transformation in it that you want, like, okay, some average graph whatever.
so that you can actually consume the metric in the back end.
**Victor Lu** 09:36 Is there any documentation with what you just described.
**Marc Alff [MySQL]** 09:44 yeah, I think we can refer to the open telemetry website. In general, it covers a lot of things
as far as specific systems from specific vendors. It's up to every one of them to
describe what metric or are not available.
**Victor Lu** 10:06 Okay.
**Marc Alff [MySQL]** 10:29 Unless there are other general questions, can we? We can start by looking at the different issues that we have? We just do that to
basically just sort them out and decide what to do about them.
So the 1st one here is related to see, make and do get. See that you
reply to it already with some asking for some information.
It looks like it's related to
what packages are or are not needed to compile open trimetry, Cpp.
And from what I understood as well as this this request.
the the reporter is asking for Grpc.
And of course Jpc. Needs a lot of things, including portal perf.
And the question was whether the dependency on portability is seen or not. So
yeah, that was the the issue itself.
So I think we can wait for clarification from the from the reporter.
I'm not sure at this point. If this is a bug in the cmake files themselves, or if
or if it's a bug in the cmake from the application calling open telemetry.
**Doug Barker** 12:01 Yeah, I don't think it's a bug. I think the original issue was
user was installing the dependencies in one path and then open telemetry in another path, but in their application they were only giving C. Make the path to open telemetry and not to the dependencies. So when it
tries to find open telemetry. Open telemetry will will try to find the dependencies, but they're not in the path, so it can't find them. And that was the underlying issue. So.
**Marc Alff [MySQL]** 12:27 Oh, okay, I see.
**Doug Barker** 12:29 So hopefully. Just adding both to the path.
resolves the issue. I think there's a common misconception with C. Make that if you have a private dependency, and it's static that
C make doesn't need to find it. But it's it was still needs to find it in order to set the include path. And if it's a shared library to set the the path to the shared library. So that's basically how
you know, we link to to Grpc, even though it's private, it still needs to be found when they find open phone entry.
**Marc Alff [MySQL]** 13:01 Okay, I see.
Okay, so looks like it will be sorted out.
**Doug Barker** 13:11 Yeah, I think, so, okay.
**Marc Alff [MySQL]** 13:13 Sounds good.
Another one that we have was basically a question from Michael.
I don't remember exactly, but I think he joined some open telemetry Cbp. Meetings a while ago
coming from Mojila, I think.
And he's asking, basically, we have a new feature which is some scope configuration that can be attached to a tracer for a trace signal
geometrics and logs.
And he's basically asking how to to make use of art.
And the thing that surprised me in is good. Is that
The configuration in my understanding the configuration is made is meant to be
as simple as possible, so that the the tracer provider can decide very quickly what to do.
And in this case it's, it seems like the the opposite path is taken. The tracer provider will invoke that code, and that code will try to go fish left and right to see. Okay, what should I do with that? That scope?
And the problem is not so much with the code itself, but with the pattern. So I think I
I describe that to to explain a bit more how it. It's meant to be used.
and we are still waiting on his feedback. So
I'm expecting that this issue will not, will not turn into a bug.
because this is not the way it's intended to be used.
But maybe we should clarify, maybe with example, maybe with documentation, or to actually use that
configuration feature, because it's
Apparently it's not trivial to make use of it.
Another thing that came up is related to metrics and synchronous instruments.
The code in that case ends up crushing a purely pure visual method.
guessing. But there is no proof of that. But I'm guessing that this is because
when creating an instrument, verification is supposed to keep.
keep a reference of that instrument for for the lifetime of it. But
and if the application doesn't. Then the instrument is destroyed, and
that could cause problem when the callback is invoked.
So I I will
provide some comments and some description. But I'm guessing this is the root cause of it.
So typically the the issue seems to be that the the instrument.
the instrument which is created is not preserved long time for a time long enough to for the thing to work.
and the rest issue is something that was found a while ago.
Still unresolved. There is some discussion about
for the Prometheus exporter for metrics where the timestamp timestamp should come from, and I don't have a definite adventure for that yet.
still needs to to be investigated.
The thing which is special about that that bug report is that something was changed to actually
remove what the so so something that was used by this
this reporter was actually removed, and the question is whether it was right to delete it or not, and whether it should be included back.
So it's a matter of
looking at respect exactly, and to find out what what respect requires, exactly in in detail.
and as far as new issues
this is pretty much it. So it's a
we haven't seen a lot of
lot of new things recently. So it's a good sign, I guess, or it also could be a sign of summer vacation. You never know
any issues that you are aware of. That need some discussion or anything.
Well, in that case we can look at existing existing Pr train.
Pr wise. A lot of thing happened recently. So
I've raised a lot of prs for the
Yaml configuration projects which Duke has also reviewed. So we have a lot had a lot of merger activity there.
going to a main branch
there is a new Pr from someone actually trying open telemetry the 1st time, which is related to some documentation to to clarify things.
So it is adding details for
minimum version required for different packages. And I saw that Ladita to comment on that here.
one thing which is unclear formality is whether this.
if it's just a comment. But it's okay, or if it's a comment, and it needs to be changed. So I was hoping it would be present to to clarify about.
But otherwise the Pr itself looks okay to go.
So let's hope that they can clarify his comments, and then we can
either adjust it or or just merge it.
But in any case, in any case, it's always good to have some new people coming in in open, elementary, and
and if we find something which is not clear in the documentation.
report it, and then we can fix it.
Or in that case we can also submit a Pr to fix it, which is even better.
Oh, this is a Pr that I filed so very just.
I think it's a temporary failure.
Yeah, I wouldn't. So one, Val again. But it's some cleanup.
So a while ago some parameter was added to a view
to have a unit in value.
and it turned out that it was not necessary, because this is not good for it. Respect.
And now, with Yabl Configuration project. I'm finding that.
I have no input parameter to map to that specific attribute. So and it. After looking at it, it turns out that it should not be there. So this is a clean up to.
to come back to the previous state, where we don't
have a unit parameter in the view, we have a unit in the
instrument selector which is expected and which has been implemented.
But we shouldn't have not have a unit in the view. So minor cleanup.
it would be a breaking change because there is a parameter change in a in a public SDK class. But that should be okay, because it's SDK, only
Next item is some cleanup from a went.
The cleanup itself looks. Okay. I just had some
some question about the exact meeting of meaning of that sentence.
It wasn't clear to me whether this is actual failure in production code, where we have a race that needs to be fixed.
or if it's a Federal in Tessan that should be ignored because it's those are 2 different things.
So I had a question from Tool went from that.
and I'm waiting on his reply to
to be sure that we can actually merge that, hey?
If he can clarify this, then this Pr would be okay to go and would be merged.
And then the Prs that we have are very old things.
So those are cooperative AI experiments.
The problem with those experiments is that
the easy Cla is still not clarified for co-pilot. So
whatever Copayote says to raise the Pr, the problem is that
easy is not is not perfect for that.
So it's missing some integration and missing some clarification about how to do that.
And then, after that, we have some some of the old things. One Pr is from
moment also as well to
validate. It's basically where it is to validate every data that comes inside open territory from the application.
I've some questions that I have some comments that I need to to write
about the right place to do that, whether it's
inside the SDK. Itself inside an exporter, if it's
if it would be an hour, please.
So we need to.
I guess, since we discussed the for Id to to implement some validity and validity. Check is good.
The question is, where to put that
and voiced is pretty much old, so nothing nothing new about that.
And I've been talking around for at least 10 min. So does anyone. Has any comments on Prs or
anything.
Doug Esan, any any comment.
**Ehsan** 25:32 No comment from me.
**Marc Alff [MySQL]** 25:34 Okay.
**Doug Barker** 25:35 Yep, nothing here.
Yeah. So well, most of these Prs are are aging, so there's nothing new about them.
**Marc Alff [MySQL]** 25:45 it's just the the normal flow things, I mean some. Some. The thing is with good reviews, some pr's like extremely simple, so they can. They can go very fast, and some Pr's are more
needs more attention, either for the for the spec itself to know what should be done.
or either for implementation, to need to see how it could be done, or maybe both.
So in some cases some Pr's takes much more time to review because of a
underlying complexity of either. The context of the code.
**Victor Lu** 26:23 So if there's no at the bottom of the screen, there is a Pr for implementing configurable aggregation cardinality.
But start from the bottom.
**Marc Alff [MySQL]** 26:37 This one. So this has nothing to do with aggregation. This is to know.
**Victor Lu** 26:41 Not not the bottom one, the 3rd from the bottom.
**Marc Alff [MySQL]** 26:46 Refresh from the bottom. Okay.
**Victor Lu** 26:48 Yeah, that one. Yeah.
**Marc Alff [MySQL]** 26:49 Okay.
**Victor Lu** 26:49 So so just as a generic question. In open telemetry. I know actual aggregation, of course, depend on the actual use case. Right, so is there any like default, aggregation.
mechanism, or.
**Marc Alff [MySQL]** 27:07 so I'm not the not the best expert on this subject, so I will go only for my understanding.
Open telemetry defines many different kinds of metrics, and for each of them many different kind of aggregation.
So you can have something like an aggregation, which is a term you can have some histograms, you can have a lot of things.
And in that case the issue is, if you have a system where open time matrix takes a lot of measurements on
it would generate a lot of data.
And in some case. So let's say, you're measuring an Http server, and you're counting the number of get post, and and that's it. So
you have a metric which I have a category of to get and post, and nothing more.
But in some cases you have a system where the metric itself has a lot of attributes, and we can have a lot of values.
and it becomes challenging in that case to do some meaningful aggregation, because it's using a lot of memory.
which is where the cardinality limit come from.
That whole feature is meant to
to say, if you have a metric where one attribute can have, say, foreign values where we are not not counting
values for every
every single 1,000 of attributes, we are only counting for the, say, the 1st 100 or the 1st 50.
So the aggregation there the the cardinality limit, is meant to
to cut down on the memory consumption for a metric where the range of values measured can be extremely wide.
And
so this helps at the the data collection part. When we collect metrics from the system and and send them.
and I guess it also helps later down the stream in, say, open telemetry collector, or in the back end.
When you actually make some computation on the metric itself.
**Victor Lu** 29:17 Yeah, so so is there any like, say.
this is true for almost everybody. So this will be by default aggregated. Is there such a list.
**Marc Alff [MySQL]** 29:32 So the the way to aggregate a metric is part of the configuration you can you? You can have a metric, for example, which is just
the the current value.
So the backend system would just measure the current value of what it is.
or you can have metrics which are agreed, getting different ways, whether it's summer, Instagram and whatnot.
and all that should be defined in the specs. In the, in the metrics part
in respect. There is a a lot of explanation about how aggregation works in general.
and what did I to expect between the measurement and the well?
So you have a system where we take a measurement, and we have a point of entry and the back end. You have a matrix which which appear so there's a lot of explanation there about what, how it works and what to expect.
So.
**Victor Lu** 30:51 So basically, open telemetry doesn't dictate actual matrix which matrix to collect and how to aggregate.
**Marc Alff [MySQL]** 30:58 So when you description.
So
when you instrument an application in the code, a developer will write some code to instrument a specific part.
to actually produce some data.
But then there's a configuration part where you can say that measurement
either occupy as is. And this is the last schedule.
or maybe I do an Instagram of it. And so I build a different metric on on that.
And this is where all the complexity comes in for the for the metric stream, because the metric stream can be transformed in the pipeline.
**Victor Lu** 31:38 Okay? So I actually have a this kind of a
use case. You can say let's say, if I
have a C plus 5 program, and it's running on both. It's the same application. But it's running on both CPU and Gpu.
I just want to find out overall.
What? How much time is spending on CPU versus Gpu?
I guess. Question number one is this use case that telemetry is for, and if not.
**Marc Alff [MySQL]** 32:14 So as long as there is, as long as there is instrumentation to report that. Yes.
but the the instrumentation has to be instrumented to actually produce the data by calling opentelemetry Api to raise the metric value.
**Victor Lu** 32:34 So so the the difficult part. So the the reason, or could database is able to aggregate information?
Not easily, but at least possible. It's it's it's a single. Everything is in in memory in 1 1 server. So aggregation happened in a circular
memory fashion.
So in the distributed applications.
And it's a multiple processes running on multiple servers how to aggregate it
in a way that can give you a overall picture of how much time is spending on, like CPU versus Gpu.
**Marc Alff [MySQL]** 33:15 Well, typically, if you have
the application running on different servers, each server will report report its own metric stream to the back, to another open telemetry backend.
While doing that each server also disclose its identity, which is part of resources.
So a server will say, Hey, this is my matrix stream with such and such measurement. And, by the way, I am server XYZ.
And a different server will also report a mixture stream with different measurement and saying, Hey, I'm Server ABC,
and in the open telemetry back end.
Then what you receive is 2 metric streams with measurement coming from 2 different places.
and at that point, on top of that you can also
do another aggregation to present another results, or you can drill down into a specific server or things like that.
**Victor Lu** 34:17 Okay. So so basically on, each server do its own aggregation.
And then.
**Marc Alff [MySQL]** 34:22 Yeah. So each yeah, each server will produce its own metric stream. But while doing so, it will also use a resource that unique uniquely identify where the data is coming from.
**Victor Lu** 34:39 So. So the the keyword, if I search for information related to this topic.
the the matrix stream is the keyword.
**Marc Alff [MySQL]** 34:48 Yes.
**Victor Lu** 34:49 Yeah, thank, you.
**Marc Alff [MySQL]** 34:53 In in details. This is the the part of the spec you you want to look at.
**Victor Lu** 34:59 Alright! Thanks.
**Marc Alff [MySQL]** 35:13 Knowing respects.
So I guess this is it for existing issues and Prs, do just to let you know.
I will update the integration Pr. For so this one for
the Yaml Configuration project. And now that we have a lot of files
part of SDK and exporters, I expect.
I expect that number and that number to go down significantly, because the only thing remaining then will be
like to review examples, which is on xpr.com.
And so that part is done and the threshold test with a couple of test files.
So the good news is all the all the SDK code and all the exporter code which is the production code itself, is actually emerged.
The only thing remaining is examples. And of course, we make files. After that.
**Doug Barker** 36:24 Awesome. That sounds good. I probably have a few comments on the make file, or the C make file, so I might add them here just to give you a heads up of what I'll look for in those, because that sounds like it's probably 2 or 3 Prs down the road.
**Marc Alff [MySQL]** 36:38 Yeah. And so just so, you know, I started to look at it again. I'm
I'm migrating to components, which I've done for the exporters, but not for everything yet.
and I will also try to look at the cmake install tests to see what needs to be done there. So I probably have a lot of questions from you
for you at that time.
**Doug Barker** 37:01 Yeah, sweet.
**Marc Alff [MySQL]** 37:03 Good thanks.
Anyone. So before we close the call, just as a reminder also.
this is the summertime, so I will also take some vacation, so don't expect me to be around in August.
so I don't know if
if we will maintain the community meeting or not, it just depends on the tenants.
So if you, if you know you are going to be away or present, just update the
where's it?
Yeah. Please update the the agenda. If you know you are going to be away, so that we we know if we can have a meeting or not
in for August and.
**Doug Barker** 38:06 Hey, Mark, as far as a release plan. Are you thinking? Then the next release would be sometime after everybody gets back. So maybe September.
**Marc Alff [MySQL]** 38:14 Most likely September, because
personally I will be away in August. Of course, other people can do this as well, but I don't know if you will be available.
so I guess it's better to. It's better to to bet on early September.
**Doug Barker** 38:32 Okay.
**Marc Alff [MySQL]** 38:34 Unless you absolutely need something, and then we can see what to do.
**Doug Barker** 38:40 No, I don't. I don't think I do.
**Marc Alff [MySQL]** 38:49 Okay, so thanks everyone for joining the call in in this hour.
Other things to discuss. I guess we can close it now.
I'm sorry this is your last chance. If you have a question.
**Ehsan** 39:09 Thanks. Everyone.
**Doug Barker** 39:10 Thanks. Everyone.
**Marc Alff [MySQL]** 39:12 Yeah. Thanks. Everyone.
Wind.
**Ehsan** 39:14 Yeah, bye.
