SIG: OpenTelemetry C/C++ SIG
Date: 2025-07-14
Duration: 33 minutes
Zoom Recording URL: https://zoom.us/rec/share/1G7JJiv8JmT4wxdAbInoLRfnvdR8QDWZLgLXGJD6-5kaTGzoeTV146tii58eQSVh.9jEEFjL0LtN06e1d
============================================================

## Zoom Recording Transcript

**Doug Barker** 00:50 Hey! Pranav! Hey! Raphael!
**Rafael Roquetto** 00:53 Hey? How's it going.
**Pranav Sharma** 00:55 Hey! Doug, hey!
**Doug Barker** 00:58 Pretty good, pretty good.
**Marc Alff [MySQL]** 01:06 Hi! Everyone.
**Pranav Sharma** 01:09 Hello!
**Doug Barker** 01:10 Hey, Mark.
**Marc Alff [MySQL]** 01:45 So welcome, everyone. Do you see my screen.
**Rafael Roquetto** 01:50 Yes.
**Pranav Sharma** 01:51 Yes.
**Marc Alff [MySQL]** 01:51 Okay, good.
So I do get a point of Ira file.
Sorry I missed the last meeting. I couldn't make it
not sure if Tom and Larry can make it. But do you have any special things to discuss today?
**Rafael Roquetto** 02:27 Not me. I'm just watching as usual.
**Marc Alff [MySQL]** 02:30 Okay.
**Doug Barker** 02:31 Yeah, I don't have anything special.
**Pranav Sharma** 02:33 Yeah.
**Marc Alff [MySQL]** 02:40 So I don't know if you noticed. But there's a new release for open telemetry c plus plus
much was done last week. So it's res 1, 22,
and it actually contains a lot of changes in a lot of cleanup inti and France
include what you use and a lot of cleanup in cmake as well from from Duke.
So thanks all for the all, the work.
one, any topic at all to discuss? Or shall we go to the typical issues and Npr's.
**Pranav Sharma** 03:47 We can go to the issues.
**Doug Barker** 03:49 Yep.
**Marc Alff [MySQL]** 03:49 Okay.
Okay. Well, it is. It has been very quiet, which is,
well, somewhat of a good sign. I don't know if it's because it's the summer of.
or because everything is fine.
There is a new Pr for moment
about the data race using the fed sanitizer.
I did not have time to look at it in details, but
coming from a rent, I'm assuming it's valid.
and so we most likely have a race condition somewhere
somewhat related to that. I also noticed that we have
some unit tests failing once in a while with something which is
it's a failure that does not happen all the time. It looks like it's also due to risk condition.
So I'm wondering if the 2 are are related or not because we have. We have one unit test in particular, which is failing once in a while.
causing Ci to break.
And apart from that, we don't have.
So yeah, there is the thanks, Luke, for that. Very
we. We should upgrade dependencies in general to keep up to date. So yes, we have to do something with
with at least
One thing I've seen that in in C make you have made some different lists for cmake with a different configuration.
I'm wondering if we should have a configuration, for, like all the latest dependencies compatible with C, plus plus 14, and all the latest dependencies compatible with C, plus plus 17, for example, things like that.
Oh, no, no need to decide now, but something to consider. Maybe.
**Doug Barker** 05:57 Yeah, that's an interesting approach. That might be a better approach. Because I think right now, I just kind of put minimum version, which is somewhat of a guess on my part, and then
the stable version, which doesn't really have a media, then those are like 2, 1 to 2 year old dependencies, and then latest, which is the
the latest versions available.
**Marc Alff [MySQL]** 06:18 But definitely open to other approaches.
because if if someone is constrained by say, we have to use C plus plus 17,
most likely they will want to know what are the latest version that that can use
for that level of C plus plus. So if we have that list already, it will be.
1st of all, it would be much better for us to test it up front, so that we have no surprises.
and it will also serve as documentation for people to know what is the latest we can get
with a given version.
**Doug Barker** 06:56 Okay, yeah, I like the idea. I'll I'll have to mean a login issue just to track the idea. And then we can follow up.
**Marc Alff [MySQL]** 07:02 Yeah, we're some.
Thanks sounds good.
So yeah, in any way, we in any case, we need to do something about it. There is no question.
Apart from that, we have some things like
complaining that we. So in this.
for every exporter that we have, the spec defines some environment variables that may optionally be implemented.
And this is typically a report that says that, hey, the spec has some environment viable. But we don't. We don't support them.
So those are things that we can improve.
So it's a it's a valid defect.
There are a lot of things in the specs which are
maybe forgotten, maybe optional and and not covered yet.
I think at some point we need to take a look at, respect and identify
all the discrepancies to make a list of everything which is missing.
And so this is one of those it's a
it's. It's simple to do, but it's it's correct that it's something we don't. We don't report yet.
**Doug Barker** 08:25 One thing Mark, and I don't know if we need to go deep into it. But one thing like in that example there, that issue they gave the default values
right now, even with the declarative configuration, I think we have different defined defaults in different places, so that might be something to consider is like, do we want to
have a single place where we define the defaults for things like
export intervals or timeouts? So on.
**Marc Alff [MySQL]** 08:51 Good. Yeah. Good question, because,
well, the the problem is that we have different ways to provide configuration to start with. So there is the
the historical way to which is to provide environment variables, and those come with their own default.
And then on top of that, there is the the config dot file that comes with
a yaml document that define also presumably the same defaults for the same things.
but this is defined in a different place in the spec and also in the code. This is also defined in a different place.
So yeah, the question is, then is, should we
at least try to use the same constants so that we make sure that we don't have.
Oh, different behavior with environment variables and and the yellow config. Yeah, it's a it's a good question.
Hi, son.
from what I've seen so far, the the spec for the Yaml configuration file is very close, and it's identical
all the defaults we have for all the environment variables.
But this is because it's it's brand new
in the long term. If the spec changes, there is indeed the risk that the 2 can diverge.
So yeah, so this has been very quiet on issues.
any issue that I've missed, that you want to to discuss.
If not, then we can. We can go to a pull request
so pr wise
We still have the the same old ones.
This is my the Pr. I'm using for for testing overall, for configuration
for the the Ml. Config. But this this is not the this one is just for testing only
the review is to be done by parts by parts. And
again, Doug, thanks a lot for all your reviews. I know it's quite a lot of good to look at, and you have been diving into that
very efficiently. I might say.
**Doug Barker** 11:47 So.
**Marc Alff [MySQL]** 11:48 Here's the next part with it which is getting closer and closer.
For people you don't know. The
the Yaml config project is to say, instead of writing code in an application to say what the configuration is for open telemetry.
The point is to declare that in a yaml file what can be changed?
whenever people want to change it. And the most important point being that you don't have to write code again and compile your application again to change the config file.
And so with all the code that we have today.
all the parser code has been reviewed and is capable of producing
in memory representation of what the configuration looks like.
The next step, which is that that 1st pr there is to make sure that from that configuration memory, we can. We start to instantiate objects in the in the SDK itself to build exporters, build
SDK parts to do all things together. So it's it's coming.
yeah. I don't know who is talking, but I we cannot hear you.
One half was was that you.
**Pranav Sharma** 13:21 So I know
**Marc Alff [MySQL]** 13:24 Okay.
I I thought, I sorry. I thought I understood. I I heard some some background question. But maybe not.
Okay. So in in any case, the the review for that is progressing. This is the next part, and there are a couple of parts to to follow up with that.
But it's it's a lot of code. And again, thanks, Luke for the review, and it's it's making good progress.
**Doug Barker** 13:52 No worries.
**Marc Alff [MySQL]** 13:53 Damn
There are also some so I need to take a look at this. I have not looked at it yet, but I see you have more changes to see make
there is curl, glib, and then there is polar beef and jpc, so I'd like to review this with this week.
Hmm.
**Doug Barker** 14:16 Sounds good. Yeah, this grpc, one's not ready yet, because there's some failing. Ci. So once I figure figure that out this week, I'll market as ready for review. But
once these 2 Prs are in, then all the dependencies will be using the the modern fetch. Content. With the exception of Zlib, I think that one's a little bit too complicated just by the nature of Zlib.
**Marc Alff [MySQL]** 14:38 Okay.
**Doug Barker** 14:38 User.
**Marc Alff [MySQL]** 14:43 Sounds good. So yeah, I will. I will try to take a look at this this week.
and I'm sure so owent is also very knowledgeable in C making general, and he makes good comments, so I'm sure he will take a look at as well.
there is also some flight sanitizer warnings. I don't know if any of you got a chance to look at it.
I've seen the Pr. For it, but I don't quite understand it, especially.
What I don't get is that this code was added.
but only if a threat sanitizer is not used.
which means this is production code.
So I don't quite understand the fix. I would expect the opposite
like. If French sanitizer is confused, add some code for thread sanitizer, but not put it in production. So it's
I may need some details on from. I went on, that to understand exactly
why it is done this way.
So yeah, if you if you had some
sometimes look at that also, please comment.
Those 2 Prs are a bit special, so I don't know if you're aware of it. But
there is an initiative to try AI in open telemetry in general.
where copilot was enabled in some repositories.
I think it was done in the Rest Repository, where Lalit Lalit is also a maintainer there.
and it was also done in semantic conventions, and it was also recently enabled, in in open to Ms. 3 Cpp.
So to say the least, there have been some some confusion about it. So it's being being sorted out.
Oh, it looks like from from the latest conversation with
the Gc. Committee. It sounds like using autopilot is actually
approved so that we can do it.
There's only one concern which is to see
all this works with the Easyca check to make sure that the the Pr.
I mean, when when someone writes a Pr, there is an easy check to make sure that the the
the contribution can be accepted, and we need to see how this is enforced in case of
good pilot, because it's compiler is a different user compared to the
the user who actually drive the Pr, so some some details to be clarified.
So this is.
This is being sorted out right now.
I've seen also another thing from our end.
I didn't have time to comment yet, but this is a lot of so the point there is
someone complained that if you have a broken utf 8 string that this they set for like a span
it goes all the way through the open telemetry c plus plus library all the way, and at the end, when it's time to agree. Send a message with portable birth rejects it.
So
the problem is that it's extremely hard to debug to find to find out where, in the application that string is coming from, if it is not correctly formed.
So my understanding is that we went. I did some good to actually verify that.
One thing, though, is to decide what is the best place to to put that code in.
From from what I understood is, he actually added that to the Otlp exporter itself
if I can find it, or maybe not.
he added that to her. Okay, so something to consider.
there are many aspects of this one is. It's a debugging. It's it's basically a debugging tool to find.
if an application instrumentation is providing call strings or not.
So there is the concern of overhead import in in production. And the cost of that
if we add it to a to the code like this.
so to to investigate. But it's a it's nice that we have.
which we are more developer, friendly, and provide also some tools, not only to to debug open Mstpp, but also to debug the instrumentation from the application. In case people do
things we're trying quite.
And this is old. Otherwise,
do you want to discuss an Api in in in detail
anything I might have missed.
I don't.
**Tom Tan** 20:55 Hi! Mark! Hi! Everyone!
**Marc Alff [MySQL]** 21:13 Is lalit. Next to you.
**Tom Tan** 21:17 I think he he's in some some other meeting. Yeah.
**Marc Alff [MySQL]** 21:20 Okay.
okay, so
just just to summarize. Well, we have a lot of different peers on a lot of things. But overall, the
the reviews are making good progress with changes from oent, and so on.
So
if you have some time, please please take a look at record reviews to make them moving and we also try to make you look at, to take a look at the C make changes.
Oh, Doug, I had a question for you.
**Doug Barker** 22:07 Yep.
**Marc Alff [MySQL]** 22:09 You remember for that, for, include what you use.
you upgraded Ci to use the most recent version.
So that fixed 1st of all a couple of crashes that we had, but also it raised much more warnings.
because include what you use in a recent version is
more proficient at detecting things which is expected.
I was wondering if we could do the same for seeing tidy, and especially
the latest pr that you have sent for selling Teddy.
They fixed a lot of things. But the warning count did not decrease that much. So typically like you fix maybe 2020 warnings
as detected. I'm assuming by a recent version of Yangthadi, but the warning count only decreased by one or 2.
So, if I understand correctly, my fear is that Silenti, as in Ci is old and doesn't see everything.
Is that your impression also? Or.
**Doug Barker** 23:20 Yeah, that that's my theory. I'm using the def container and Vs code with the client d extension in it. Every time I open up a
file. It will show me the the warnings live. So it runs it in in a different way, but it is running the very latest clang
version, so I can take a look and see what it would take to upgrade.
**Marc Alff [MySQL]** 23:42 Okay.
**Doug Barker** 23:43 Rci to the latest cling tidy, and and maybe that will close the gap.
**Marc Alff [MySQL]** 23:48 Yeah, because well, not only that will close the gap, but also
if in Ci we have better, better reports for sanity that will also prevent new errors to come in.
because today we do cleanup. But there is nothing that can prevent
that could to introduce the same errors. It fell invisible to send Id, at least in recent versions.
**Doug Barker** 24:17 Yeah, it. It's a good point. I'll I'll log an issue for that as well. After the meeting.
**Marc Alff [MySQL]** 24:21 Okay. Yeah. Thanks.
**Doug Barker** 24:23 Yep.
**Marc Alff [MySQL]** 24:27 One thing I forgot. Also, there have been some some administrative changes.
Let's see, it was approved already.
Okay.
oh, thanks, David, okay, so just so, you know, in the past.
so typically maintainers in all the different repositories have maintainer privileges on every repo
in the past. We have asked to have Admin privileges on the open, M. 3 Cpp and Cpp control.
so that we could change the the settings ourselves.
That was to have some better freedom in case of failures in Github and things like that, to to trying to recover from the from something broken
but now there is also a new open telemetry admin repo, which is,
actually, it's a private report. So I'm not trying it. But basically, this is
a repository that contains all the settings for every repo in open elementary.
So because of that, everything will be managed centrally from open to admin.
and as a result, we also, we are now
we no longer have admin privileges. We are back to maintainers.
And as a result, this, there is one file like this that was created in opentelemetry Cpp, and the same one in opentelemetry Cpp contribute.
which are removed.
So some some admin cleanup which is going on just to to get the privileges right, and to to
one place where privileges are maintained and all the settings are maintained.
I was about to ask for for a review of that Pr, but it has been already done. So
nothing to nothing to worry about.
yeah. I prepared a couple of notes. But we've discussed that already. So nothing new from my side.
Raphael, do you have any question or topics.
**Rafael Roquetto** 27:28 No, not yet. I'm still not yet. I'm working on a personal project that is, it's a Vpf
tracer for Http
requests only so similar. What we're doing at Grafana. But it uses a different kind of Bpf programs. So just experimenting with that. And the very next step is, I'm gonna start looking the user space in C, plus plus, I'm gonna start hooking up the
the Hotel C and C, plus plus
SDK, and then hopefully, then I'll have something constructive to say.
**Marc Alff [MySQL]** 28:07 Okay. Thanks.
**Rafael Roquetto** 28:08 No worries.
**Marc Alff [MySQL]** 28:11 And out of curiosity, are you?
Which version of open imagery are you using with that.
**Rafael Roquetto** 28:20 I haven't picked one yet. So any recommendations.
**Marc Alff [MySQL]** 28:26 Well, by principle, I would say the least. One.
**Rafael Roquetto** 28:29 The latest. Yeah.
So probably that's what I'm gonna go for.
**Marc Alff [MySQL]** 28:34 Okay.
Speaking of latest version of this release
contains some so there was were some code that were some error files that were deprecated a very long time ago
which have been finally removed ready to edify for 70 conventions.
So let's see.
we should have raised, not.
we should have reasonables on that.
Yeah, yeah. So
2, 12, 5 have changed. So if you have some variable code using 70 conventions, you need to adjust for that.
So just a reminder. If people encounter that
just some notice I will be away in August, so I don't know.
Based on attendance.
I I don't know who will be available who will not be for team meetings. But if
typically I tend to drive a meeting, but if I'm not there. Someone else should should step in
to drive a meeting. Otherwise. We can also just cancel it.
depending on the tenants.
and without any other topic in general to discuss.
**Pranav Sharma** 31:01 Not from my side.
**Doug Barker** 31:04 Nothing here.
**Marc Alff [MySQL]** 31:06 Okay, well, that was a short meeting then.
Oh, thanks everyone for all your work. And all the issues, Pr's reviews and so on.
And let's continue to to make progress here. So
thanks a lot, everyone, and see you next week. Then.
**Rafael Roquetto** 31:29 They can't see it.
**Pranav Sharma** 31:31 Cheers.
**Tom Tan** 31:32 Thank you.
**Pranav Sharma** 31:33 Everyone see you.
**Marc Alff [MySQL]** 31:35 Bye. Goodbye.
