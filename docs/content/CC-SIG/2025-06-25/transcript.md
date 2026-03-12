SIG: C/C++ SIG
Date: 2025-06-25
Duration: 49 minutes
Zoom Recording URL: https://zoom.us/rec/share/MKvQi5BrBKkMc7gOHRhEYM5mRH-BhnZWxj_GBqg5zDdVxwmWCzc3hjyRl1Rx8IT3.rWrn0gQ6W51i2TGf
============================================================

## Zoom Recording Transcript

**Doug Barker** 00:14 Hey, Raphael.
**Rafael Roquetto** 00:16 Hey, Doug, how's it going.
**Doug Barker** 00:17 Pretty good. How are you.
**Rafael Roquetto** 00:19 I'm good. Thanks.
**Marc Alff [MySQL]** 00:29 Hi! Everyone.
**Rafael Roquetto** 00:32 Hi, mark.
**Doug Barker** 00:33 Hey, Mark.
**Marc Alff [MySQL]** 01:11 Do you see my screen.
**Doug Barker** 01:13 Just in case, okay, good.
**Marc Alff [MySQL]** 01:18 And Hi, Raphael! Welcome back!
**Rafael Roquetto** 01:22 Thank you.
**Marc Alff [MySQL]** 01:26 Yeah.
I saw that it online. So I'm assuming he will join also. And Tom said, he cannot attend while we wait for Nat any specific topic you want to discuss profile. Maybe.
**Rafael Roquetto** 02:07 Now I'm just watching for the time being. I'm gonna start play more with the C plus plus stuff this next week. And then, hopefully, I'll have something constructive to say. But for now I'm just watching.
**Marc Alff [MySQL]** 02:20 Okay. Thanks.
**Doug Barker** 02:40 So, and Tom just message, said, they, have a conflict.
**Marc Alff [MySQL]** 02:44 Both of them.
**Doug Barker** 02:45 Yeah.
**Marc Alff [MySQL]** 02:46 I missed that.
Okay, well, I guess we can start then.
We have a couple of issues some of them mainly discussions. We just didn't accept them right away.
And also we have quite a few prs to look at.
especially the cleanup here for ceiling tidy, and a lot of cleanup for cmake.
Do you have any preference on what to start to look at?
**Doug Barker** 03:26 No preference for me.
**Marc Alff [MySQL]** 03:33 Okay, let's do the the pr's in order. Then from top to bottom.
So Duke, so this is yours. I'm actually quite amazed that the number of issues drops very quickly. It's it seems to be less painful compared to include what you use.
**Doug Barker** 03:54 Yeah, some of them are easy. I'm fine. Think I tackled the easy ones first, st just to get them out of the way a little bit but the
**Marc Alff [MySQL]** 04:02 Yeah.
**Doug Barker** 04:03 I'm gonna do a revert on on the Grpc changes because I'm actually finding that the interface to the Grpc client probably needs to change, or it does need to change, because it has, like moving the arena which allocates the memory for the messages to a lower scope. That would that if we actually implement the move, it's gonna delete the arena before the or destroy the arena before the messages which shouldn't be allowed. So revert it in this Pr, and then it's gonna take a little bit of a A minor interface refactor to get that working properly.
**Marc Alff [MySQL]** 04:36 So I'm assuming you're referring to this part. Then.
**Doug Barker** 04:40 Yeah, that part. And then I think there's several other methods. Now that I'm understanding how it was designed. But basically we can't. We cannot destroy the arena before we destroy the messages. That's just not allowed.
**Marc Alff [MySQL]** 04:54 Okay?
So for the joke, once you understand it, please explain it to us.
because I'm not familiar with the Grpc code itself.
**Doug Barker** 05:05 Yeah.
**Marc Alff [MySQL]** 05:06 I'm somewhat, but not not to an extreme.
Okay? So yes. So well.
if this one needs to be to be looked at separately. We can leave it as is, and and clear all the simple stuff first.st I mean, there is no.
**Doug Barker** 05:22 Yeah, that's that's my plan. So after the meeting I'll do a revert on on the Grpc stuff. So the commits here for the Grpc. And then I'll mark this one ready for review. And hopefully, it's easy to to look at.
**Marc Alff [MySQL]** 05:34 Okay?
And the only comment I had on this.
So of course, I don't remember on which file I did that.
Yeah, I saw that in in some cases, especially for the Jpc. Code, your tree took the the parameter and did a steady move on it, and in this case it's just not used for anything, and I was wondering if we if we don't do anything, if we don't move the parameter which is given, whether that will cause some memory leaks or something nasty for for test later.
So I'm wondering if we should just always do a move instead, just so that we have a correct implementation, but takes the parameter, moves it, even if it doesn't do anything with it.
**Doug Barker** 06:26 Yeah, I think that's a good idea. I think it depends on if somebody's calling a city move when they when they call the function. But it's a good point like we should just expect that they're always gonna do that. So they're expecting to take ownership in the function.
**Marc Alff [MySQL]** 06:39 No.
and that should avoid. Also, we need to have tags like that in the source code. So it would be cleaner as well.
**Doug Barker** 06:46 Yeah.
**Marc Alff [MySQL]** 06:47 Good point.
Yeah. So that was my my only comment, or everything else looks good to me.
So yeah, thanks for the cleanup this one was a good cleanup for moment. Related to how we serialize a ways of basically how we serialize a string.
And we're portable could.
And so this is this is really related to protob itself on developers.
The way it's fun.
Yeah, it has to do with how to serialize data into the photograph message, and I saw that it it looked okay to me when I read the the Pr. But Lalit had some some comments with that especially related to the compliance with the spec.
So I guess we have to wait for Lalit, and I went to to resolve that.
I see that.
Yeah. He he looked at it.
**Doug Barker** 08:02 This is an interesting one, mark. I looked into it. So the opentelemetry proto actually implements and a key value, and the value is any which includes bytes for all attributes.
**Marc Alff [MySQL]** 08:14 Okay.
**Doug Barker** 08:14 Across the board so uniformly.
So. That's why I approved it. Because Owen Owen's actually calling the set bytes method, which means that somebody explicitly put it in there, and it's a valid entry in proto in the Protobuf message itself.
So I think the misalignment with the spec is at the open telemetry, proto level or or but they're they allow bytes for basically any attribute like key value value.
**Marc Alff [MySQL]** 08:44 Okay, interesting. Yeah.
I've never used fancy attributes. I typically use rings, and I don't try to put a binary object inside some attribute or things like that. So I've never been exposed to using any of things like that. In fact.
So yeah, needs needs clarification. But they will figure this out. We're looking at the I'm not aware there's some limitation on in the spec itself compared to Portal, because also the spec was written a very long time ago in the stack report. But then there is the Portal Repository as well, that contain the the portable definition.
and it also could be that things got turned out in the in the portal definition that we are not reflecting this in the spec, or things like that. Sometimes there is also some some historical drift. We look at add specs, so we have to to check that as well.
**Doug Barker** 09:52 Yeah, fair enough.
**Marc Alff [MySQL]** 10:02 Also for patents also. So 1st of all, thanks a lot for the for the Pr.
I think I think it makes a lot of sense to have.
Well, where is it?
Yes, to have the list of all the dependencies together like you have. You've done.
Because otherwise we were picking like. Oh, I want this flavor of Jpc. With this flavor of upsell and this flavor of Portob, and of course those we don't work together. And it was indeed a major problem to just try to keep that in sync.
So with that, I think we have a much better consistency, and it will be much easier for us to to maintain that.
because there are indeed some some dependencies between between some of those.
**Doug Barker** 11:09 Yeah, I'm hoping that it helps because it removes the versions from the bash scripts and the github.
**Marc Alff [MySQL]** 11:17 Oh, yes, yes, that, too.
so that we don't have to to work the Ci all over the place again and again.
Voicemail.
**Doug Barker** 11:29 Mark, I think the question not necessarily to block this Pr. But in the future, like how many versions do we want to test? I think it may make sense to test at least the minimum versions we want to support in the latest. But right now, like this, Pr will add 4 files with all the get tags.
and that may not be necessary, you know, going forward.
**Marc Alff [MySQL]** 11:51 Yeah, boom.
The thing is, we don't in open telemetry. Cpp itself. We don't require a given version for dependency.
So it's not like, oh, you have to. You have absolutely to use your PC version. So and so.
So it's more like the the application that decides. Okay, well, I'm leaking with Jpc. For something else. So I would like to use this Jpc. Jpc. Version with open telemetry, for example.
So we we try to test a bunch of different version just to make sure it works. But then, of course, this just creates so many combination in Ci that it's not worth it.
And so having less combination like that is much, much better, I think.
and in any case we also end up taking whatever is the default for the distro on the platform we use. So if you have a distribution which is using a given version.
most likely people will be using that version on ubuntu, anyway. So we might as well just take the default, therefore, for testing, to make sure it works, at least in the in the basic case.
**Doug Barker** 13:12 Okay. Sounds good.
**Marc Alff [MySQL]** 13:20 Just to know who went as some very strange requirements when it come to version.
I don't know if it's still the case. But he, he used to have open telemetry deployed with Gcc version 4.8, if you can believe it.
Using this was even before C plus plus 11. I think he.
I'm not even sure if if he's using C plus plus 11 today, or if he or if you move to C plus plus 14, for example. But he has some very strange requirements from very old platforms.
What he's using in production I don't know the full story behind it, but I know that it exists.
So this is why Ci also had some part of the Ci. Was testing some very weird use cases with an extremely old version of Gcc. And an extremely old version of Jpc. Portograph and whatnot.
**Doug Barker** 14:20 Interesting. It's good to know.
**Marc Alff [MySQL]** 14:23 Yeah.
So so this one is nothing special for for windows. Right? It's only I don't remember because there is another pr, as well.
Okay. So I think this one we can merge.
I think there is another Pr. Where I went and had some question about some possible review from Lalit and Tom on windows.
Yes, the Google test and benchmark.
Okay.
**Doug Barker** 15:04 Yeah. And I don't know, Mark, if you, if this changes before you, if you know the history of that when install windows, depths function. But basically, what would happen.
**Marc Alff [MySQL]** 15:12 Calendar.
**Doug Barker** 15:13 Is, if you configure open telemetry. Cpp, no matter if you're just trying to build and install the Api, which requires no dependencies, or if you're trying to build everything. But no matter what, if it doesn't find the Google test package installed on windows, it will install all the dependencies, including Grpc. And protobuf at configure time. So it'll launch a external process.
Run Vc. Package and then install all the dependencies at configure time. No matter how you've configured.
See? Make for open. So it seems like that's really unexpected. But I don't know if I obviously wasn't there for.
**Marc Alff [MySQL]** 15:53 It's so. I don't know the full story for that. I know it's very old. It has been there, like.
probably from the start.
It is unexpected behavior, like.
instead of instead of a make file saying, Hey, I need this need this, and I haven't found it. So I'm failing, and please provide it. The the make file is going out of his way to try to to make something work, regardless of whether you you want it or not. So, including installing a lot of things behind your back.
And I think this is.
I think the motivation is to to make sure that it builds so that someone using open telemetry and trying open telemetry for the 1st time, typically on a windows machine at something working as opposed to have wall of failure, saying, Oh, you need this. You need that. You need that. And spending 2 days just installing dependencies and having people give up on on open telemetry altogether.
So I'm I'm assuming that the intent was to to simplify well, to to have some ease of use, but unfortunately it's ease of use for a developer trying to build locally. It's not. It's not improving things for packaging and everything else. It's it's getting in the way instead.
So I think it's a very good cleanup to actually remove that and have the make file behave without surprises.
So this is I. I think this is why uhm should look at that? Because I think they know that part much better.
And also they would know why it was done this way.
But I'm suspecting that this is just to try to have open telemetry building out of the box, even if you don't have anything else.
**Doug Barker** 17:59 Sounds good, and the one that we, the Pr. That we looked at before this, since it will install all the dependencies from those tag files, using pure C make that should work also just as it does on any platform. It should work on windows so.
**Marc Alff [MySQL]** 18:14 You know.
**Doug Barker** 18:15 We could provide instructions for, for if somebody didn't want to use Vc package if they're using Vc. Package, then I think they they just use the port file that Tom maintains. But if they're not using Vc package they could just install the dependencies with native C make with that Pr. That we just looked at.
**Marc Alff [MySQL]** 18:35 Yeah, it's it's very likely that we need to to clean up installation instruction, to be sure that it's aligned with the recent code that we have.
so that people know what to do when we are trying the 1st time.
Raphael, out of curiosity, which platform are you using.
**Rafael Roquetto** 18:57 So you mean for development or.
**Marc Alff [MySQL]** 19:01 Yes.
**Rafael Roquetto** 19:02 I, I run? Arch Linux. Yeah.
**Marc Alff [MySQL]** 19:04 Okay, so you won't see this. All this thing with Vc package and whatnot. So.
**Rafael Roquetto** 19:10 Okay.
**Marc Alff [MySQL]** 19:10 Yeah.
**Rafael Roquetto** 19:11 For Lena.
**Marc Alff [MySQL]** 19:12 But but likewise, if you see something strange like when trying to install and and build open telemetry and things like that, just let us know.
because we, we are so used to do it after a while that we when I 1st started to actually build roofing, it was very complicated. So I know that it it can be challenging at times.
A lot of cleanup has been on since. But now that we know the process, we.
We tend to forget also what the learning curve is. So if you have some some comments on on the learning curve that would be good feedback as well.
**Rafael Roquetto** 19:49 Absolutely. Yeah, yeah, hopefully. it's not gonna be too much. I'll tell you.
**Marc Alff [MySQL]** 19:56 Okay, thanks.
Okay. So this one, basically looks good to me, looks good to, and just need to have confirmation for for the windows part.
which means the previous one.
So this this one has no windows. Dependencies in court.
**Doug Barker** 20:24 Correct.
**Marc Alff [MySQL]** 20:27 So I will watch that after after the meeting.
So the next is everything related to file configuration. I see that Lalitz just approved the 1st thing on the trace model.
and as just a question, I will address that but otherwise. So this thing is good to go then, and so I will merge that this one.
Okay? So I'm basically waiting because this is a a major project. I'm waiting to have overall maintainers to look at that as well, so that it just did.
I don't know if you had comments, I will. I will double check.
So yeah, so we will have the trace and the samplers that go goes with it. Would you have some time to take a look at the log and matrix model? It's It's the next thing in line for for that.
**Doug Barker** 21:36 Yep.
**Marc Alff [MySQL]** 21:37 Okay for metric. I just noticed that there are a couple of things which are with some minor comments, like a Fix me where something is supposed to be an enum, but it's it's just told as a string attribute. So I know that for metric I would have to do some minor changes. I will do that.
But for logs everything which is there should be okay, as is, I'm not aware of any remaining items.
something.
And then so it's only for them. But expect more. Pr's to come, because there are other parts as well.
I'm I'm creating the Prs in the in a logical order, so that it's easy to easier to understand the whole thing.
**Doug Barker** 22:25 Yeah, so, face.
**Marc Alff [MySQL]** 22:31 So this one is the pair that you are just splitting. So I'm assuming that once the previous one are merged, the size of that should decrease.
**Doug Barker** 22:42 Yeah, I'm probably not gonna maintain this anymore. But I'll leave the branch. I may. I may close this Pr, but I'm I am gonna pick out like, I probably have 5 or 6 more Prs to post. I didn't wanna overload the the channel.
**Marc Alff [MySQL]** 22:55 Sure one cook between those 2. Do you suspect any merge issues, or do you have any preference in which order they should be merged.
**Doug Barker** 23:15 Let's go ahead and merge. The 3rd party install 1st since that one, and then there will be like one a 1 line kind of like, I'll resolve it.
**Marc Alff [MySQL]** 23:25 Okay, sounds good.
This one.
So it's still draft small one.
I think this was to test in test to see. I change.
So not sure we need to do anything with it. It's better to wait from for Tom to see if he still thinks we need it or not. My understanding is that that was just.
We test Pr to to try cin and expose a failure, but I don't know if we should merge that or not. Well.
we we can wait on him.
and I'm thinking on exporter tests. So yes, thanks for the review.
I saw that you had a couple of comments which have been resolved, I think.
Oh!
Can you confirm, if the if the last comment is resolved as well by one.
**Doug Barker** 24:28 Yeah, I'll I'll mark that I approve. So that one is resolved. Yeah.
**Marc Alff [MySQL]** 24:32 Okay, okay, good.
Okay. So I guess you should be good to go as well.
okay.
wow.
I'll take a look, and and most likely we'll merge that also.
So this one is starting to get old and still waiting on.
Yeah, some conflicts resolution.
I guess we can wait a bit more because I don't want to get into merging that without knowing exactly the the code change itself because it's it could be risky hoping that this power will be looked at at some point so this is late with a test framework. I'm guessing he has had no time to look at it so it should be still in the same state. But we need to keep that way around.
It doesn't change, and the last one is the overall Pr for the file configuration.
so that one actually, I should market as do not merge, because it's merged by parts. So okay, so I guess this is it for peers?
Anything I forgot. There, piano wise.
What you want to discuss.
**Doug Barker** 27:26 I don't think so.
**Marc Alff [MySQL]** 27:27 Okay.
Oh, I forgot to mention something. So for all the configuration work, actually, the configuration report was released.
Version one. Now it's well, it's a release candidate, but it's it's getting there.
So it's It's on the path to be stable with a version one I created a an issue for the next release. Of open telemetry.
If somehow you you are aware, or you depend on an issue, but absolutely needs to be fixed.
just feel free to add a comment there.
If there are issues that need to be part of a tree so that we can make sure it is reviewed on time, and we can, we can include it in the reason.
**Doug Barker** 28:27 Do you ever.
**Marc Alff [MySQL]** 28:28 Out of Jersey.
**Doug Barker** 28:29 Mark.
**Marc Alff [MySQL]** 28:30 Early July, but I don't know when exactly.
**Doug Barker** 28:33 Okay.
**Marc Alff [MySQL]** 28:35 It was. I mean, it's indicative at best, because it depends on on different reviews.
Out of curiosity. Do you use open time between production? Yet.
**Doug Barker** 28:48 I did in my in my last role. So I've been working on a project for for robotics. But we had like in the last role. We had over a hundred robots using open telemetry in the field.
**Marc Alff [MySQL]** 28:58 Okay, I'm asking, because sometime people depend on the Netflix. So they they contribute the bug fix, and then they wait and want to have that bug fix as part of our lease so that we can, they can actually use it in their own project.
So if, should that be the case make sure to to list the bug you need in that in comments, so that we know we Wizburg is as more priority.
So this thing, someone has a link issue, I think, you spotted the the problem with that which is to use the Metrics Exporter Library, and the confusion comes from this thing so historically the Otlp Jarpc. Exporter Library.
It was implemented with with traces only.
so it was named Jpc. Exporter period, even though it only contained the trace signal.
and then, when metrics and logs were implemented later, the Library for Jpc. Exporter metrics and Grpc. Exporter logs was created.
but the name for Jpc. Exporter was not changed to to trace exporter.
So I guess this is why the confusion comes from, because that guy he wants to use the job. PC. Exporter, and he's probably be assuming that this contains everything, including metrics which it doesn't. This is only for tracing.
So I'm assuming this is the root cause of that link issue.
And so, yeah, this is what you indicated. And I guess we can wait on on his feedback to see if that resolved the problem or not.
**Doug Barker** 31:04 Yeah. And to be fair, they're not well documented. So I added, that table that actually shows all the targets on the install markdown file, but it doesn't give an explanation for what each one has. So we're hoping that the names are descriptive enough.
**Marc Alff [MySQL]** 31:19 Yeah. But in some, in some cases it can be confusing.
So this one. So it's related to the way we populate string attributes inside the photograph messages which owent looked at.
But I think there is more to it also that Guy wants to have some debug log all over the place to detect if something is valid, valid name or not.
Not quite sure whether we should do that. Because, oh.
I mean, it would be basically printing envelope file every every message sent which. So we can produce a lot of logs.
If we do that, maybe we can have a blog in a in a debug severity, or something like that.
But I can see the point. He has, like most likely, some one name somewhere contained a bad character.
but we don't know which one. So there is one event somewhere which is causing some problem room on the.
on the sending or receiving side, and it's not easy to trace what part of the code and what is instrumented that produce that but name.
So not not sure what to do with it. So I don't like so much the fact that we have logging statement all over the place in the code to discuss. I guess.
So. This is related. This is the someone wants to send bytes and binary to a log record.
which is quite strange, because then you have to to know what to do with it on very silly side.
and I don't get sure even if this is supported on the protocol level. I mean, once you put the open telemetry collector or backend that tries to display those logs. I'm not quite sure what the expected behavior is there.
because we're the back end will see a binary content. And then what I mean.
You probably need to make an assumption on what it is to manipulate it, or to make any any aquarium. So it's it feels strange to me.
but I'm assuming that this will be resolved by the discussion between edit and went on, what is the specs, allowing exactly.
and whether we support binary there.
because all those things, all those things are related, and this one not so much familiar with zoom for me to use exporter. But basically, when we have a metric which is reported there is a timestamp in the measurement that says when it was collected.
And this guy wants to not use the timestamp of when it was collected, but use a different timestamp, most likely, because he has a measurement coming from somewhere else.
So we need to check if this, if 1st of all, the specs, allows that.
or if the spec says that we we should set the time stamp away when they are recorded.
And then, if if the spec goes that, then we probably need to change the way.
the instrumentation, the measurement works.
And this is it for new new issues I've I'm I haven't checked. If we have all the issues which have been changed looks like no offering any other things you want to to talk about.
still observing, to get a feel from what open telemetry is, and and how friendly we are. During during the team meeting.
**Rafael Roquetto** 36:14 Yeah, yeah, yeah, for sure. Yeah. Yeah. So I started like, I had no idea about open telemetry until I joined Grafana a year ago us, and and then I've been working.
you know, with the Grafana Bela, and and afterwards, now it's open telemetry. Bpf. Instrumentation. The project is called now.
I think it. It's 1 thing working from the inside of the project and the other thing as an user. So I was, I've been planning to and start toying. And with, you know, the C plus plus stuff, and actually trying to build something that uses it first.st So I can better understand the Api, and you know how to mute it, and every you know how to use it. And maybe then I can.
Yeah, contribute if there is anything to to contribute.
so yeah, and also to, you know, remain in touch with C, plus plus. Because.
yeah, I've been doing a lot of C and go but I quite like I quite like working with C, plus. Plus. That's what I but I did most of my career. So it's it's nice to have a an anchor there in.
and the project still action. So yeah. But for now I still I still feel I don't have a lot to say, you know, like a lot that that's for sure. I'd love to pitch up.
Yeah.
**Marc Alff [MySQL]** 37:36 So the open telemetry in general is doing a lot of things. So 1st of all, there are, there are different type of instrumentation being trace metrics and logs so trace, I think, is the most interesting and easy to learn.
because it's you can. You can only see a lot of interesting good things with traces, and if you have a back end like with Jaeger, or something like that, you can also see your traces in the application.
So this is this is really nice.
Matrix has a learning curve of its own, because there is plenty of things with aggregation and different type of instruments and a lot of complexity there which is very specific to metrics. And the way it is reported.
So it's a it's a beast by itself and the aggregation. There.
We've the way instruments are named, the way you can put a view on top of something else to derive a different metric. I mean a lot of lot of things that can happen there.
And logs, I guess, is the most straightforward.
Oh, I did so.
So it's it's easy to to understand, and you can quickly instrument an application to raise a couple of things. But then you don't have a lot of it's it's only a log, so you you don't have a lot of things to to look at.
**Rafael Roquetto** 39:02 And on top of and on top of that. Then for each type of data.
**Marc Alff [MySQL]** 39:08 Then you have plenty of choices where the data can can go and how to export it.
whether you want to dump that to a file, or give that to the primitives tool to to show a metric directly, or give that to an utility exporter which can use different protocols on the wire to send it out, and it quickly adds up, because then you hear so many you are like, Okay, Zip, keen and formatives and Otlp and Http and Grpc and file and output stream exporter and and a lot of things that all which are all different ways to export the data.
So what I've done in the past is just to for for traces where I add my own application to instruments. So add some some data that can be generated.
and I've had my application. That degenerate trace traces fed up to a year ago to Jaeger to observe the data in Jaeger. And then it's really when once you get to that point, you can actually see the data which is that comes from your instrumentation. So it's when everything starts to to add up.
**Rafael Roquetto** 40:26 Right? Yes. So there are so many things to digest that.
Yeah, I have to. That's why I'm just here observing and and see what's going on with the project.
I do intend to start working like in a toy project.
That. It's just a small Ebpf tracer. But the user space I want to do in C, plus plus usually a lot of these tools are, you know, isn't go. So that's when I want to.
Bring in the open telemetry, Cpp, and and learn how to use it, and like getting the my hands dirty, and see how.
Just so I'll let you know, if I run into any issues when it comes to building dependencies, that's gonna be the 1st thing I'm gonna stumble upon and and familiarize myself with the Api, and how it's being used. Yeah.
**Marc Alff [MySQL]** 41:17 Yes. Okay.
**Doug Barker** 41:23 Raphael, maybe a good place to start. There is a docker file for the Dev container, so you can either use it in the Dev container. If you don't use Vs code, you can just use that docker file as a good reference for how to install the dependencies, and the dependency install gets cleaned up. Once Mark merges that that cmake pr, we just looked at.
**Rafael Roquetto** 41:42 Okay, okay, all right. And that help. That's helpful.
**Marc Alff [MySQL]** 41:55 Okay, I don't have any any other topic So unless you want to discuss something specific then we can close the call then and.
**Rafael Roquetto** 42:09 One quick one very quick question, which c plus plus version is are you using? Is it 20.
**Marc Alff [MySQL]** 42:18 So the minimum requirement used to be c plus plus 11. And now it's c plus plus 14 but you can use 1417, 20, and most likely 23, I guess.
we. We have Cis for all the different different compilers. Where is that?
**Rafael Roquetto** 42:42 Cool.
**Marc Alff [MySQL]** 42:43 You see, ci, for all different things, we try to make sure that the code is running free for all of them.
and so it tends to be sometime. It's annoying, because then you you write some code it works, and then you forget that. Oh.
this c plus plus construct I'm using is only in C plus plus 17 and not 14. So I have to use something else. So that that happened sometime when we when we write code, but otherwise once when something pass ci. It should be good to go in any c plus plus version.
**Rafael Roquetto** 43:16 Okay. Okay. So for instance, if I wanted to use, I don't know just making this up standard span wouldn't be able to, because it needs to be backwards compatible with C, plus plus 14. For instance.
**Marc Alff [MySQL]** 43:29 Yeah. But in that case we have. So we have things that we call no Std, which are replacement for Std span.
It's okay.
typically inside the code, we would use no Std something. If if it's not available on every platform and in the in the public Api. We try to avoid those if we can.
Otherwise we would take a no Std. Something as opposed to a CD. Span. For example.
**Rafael Roquetto** 44:01 Okay, well, makes sense understood.
Yeah, that's all. All the questions I had so far.
**Marc Alff [MySQL]** 44:09 Okay.
**Rafael Roquetto** 44:10 Thank you.
**Marc Alff [MySQL]** 44:17 Alright. Well, thanks everyone. And yeah, Rafael, I don't know if I don't know if you know. But the the team meetings are alternating between Mondays and and Wednesdays every other week.
Silver.
Yeah, the calendar is there, anyway?
**Rafael Roquetto** 44:38 Right. Yeah, I'll probably be away next week. Then, because it on the first, st it's kind of day and getting a long weekend, but then I'll see you in 2 weeks.
**Marc Alff [MySQL]** 44:49 Okay. Sounds good.
Well, thanks. Everyone. Thanks for joining.
Have a good week.
**Doug Barker** 44:58 Good sense.
**Rafael Roquetto** 44:58 You.
**Doug Barker** 44:59 Thanks to you.
**Rafael Roquetto** 45:00 Bye.
