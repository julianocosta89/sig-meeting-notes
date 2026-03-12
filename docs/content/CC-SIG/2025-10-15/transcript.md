SIG: C/C++ SIG
Date: 2025-10-15
Duration: 15 minutes
============================================================

## Zoom Recording Transcript

**Nikhil Bhatia** 00:21 Hey, hi, Mark.
**Pranav Sharma** 00:43 Hey, guys.
**Nikhil Bhatia** 00:45 Hi, Brono.
**Pranav Sharma** 00:46 Hello?
**malff** 01:23 Hi, everyone.
**Pranav Sharma** 01:26 Mark.
**Nikhil Bhatia** 01:27 Hi, Mark.
**malff** 01:59 I didn't have a lot of time to prepare the meeting, so I don't have anything special. Do you have any things you would like to discuss?
**Nikhil Bhatia** 02:08 Yeah, Mark, I wanted to ask one thing, In my, I have raised a PR on metrics, which will do re-aggregation when some spatial dimensions are dropped. So, There is only one concern with it that, before… this, it was using, like, one for loop, but now, after my changes, I have… I have done, three for loops are there. So, If there is any idea for any workaround where we can decrease the number of for groups, then it would be great, actually.
**malff** 02:50 Oh, okay. The best person for… for all the aggregation code, I think, is Lalit. So… If he can, he will take a look at it, but I can also look at it and see what I can find.
Yeah, yeah, much.
Okay.
Do you know in which file are those for loops?
**Nikhil Bhatia** 03:22 Yeah, they are in, they are in asyncmetric storage.h.
Yeah, in the, this one. This is one extra one.
So, if we have any way to reduce that…
**malff** 03:49 Okay, yeah, I'll take a look.
Out of curiosity, which platform do you use when, working locally?
**Nikhil Bhatia** 04:17 You're asking me, Mark?
**malff** 04:20 Yes, well, both of you, but yes, yeah.
**Nikhil Bhatia** 04:22 Yeah, I use VS Code, Mark.
**malff** 04:26 Okay.
**Nikhil Bhatia** 04:27 Nope.
**malff** 04:27 And, Bonav, what do you… what do you use?
**Pranav Sharma** 04:30 I, I typically use C-Lion.
**malff** 04:34 Okay.
**Pranav Sharma** 04:35 You're talking about the IDEs, right?
**malff** 04:38 Well, the compiler, the operating system, just to have an idea of,
**Pranav Sharma** 04:44 I see that.
**malff** 04:45 Yeah, I think.
**Pranav Sharma** 04:46 I think the compiler, by default, come with, Is it… is it GCC? I think it's… No, I think it's Clang. I don't remember. Whatever comes default in CLion.
**malff** 05:00 Okay, I see.
**Nikhil Bhatia** 05:02 And, my operating system, I use, macOS and Clang.
A compiler.
**malff** 05:09 Okay.
I'm asking because we still have a lot of issues on Windows because of a very special way we build the Windows DLL.
**Pranav Sharma** 05:30 Oh, no.
**malff** 05:31 Looking if someone is familiar with this area.
**Pranav Sharma** 05:35 No, actually, I haven't done C++ development ever on Windows. It's mostly either Linux or macOS. Those are the two… computers I use, yeah.
**malff** 05:45 Okay.
**Nikhil Bhatia** 05:47 Actually, I have a secondary Windows laptop, but I never use it, actually. I don't use it a lot.
**malff** 06:00 Okay, so… Thanks for the details, that was just a side curiosity question.
Because we… we still keep, things like that. I mean, the… There are many related issues which are all related to symbols missing in one DLL.
**Pranav Sharma** 06:35 Interesting. I thought, doesn't Thomas, Thomas use this Windows? I thought…
**malff** 06:43 Tom does, yes, I think.
**Pranav Sharma** 06:46 Hmm.
**malff** 06:53 Okay, Looking at this list, so this is the current list of things which are more or less easy to start with.
Have you take a look at that, and do, Do you want me to add more tasks in that, just to have more choice or more ideas, if there are things you are interested in, in general, or…
**Pranav Sharma** 07:22 I mean, if you… if there are certain issues on the… off the top of your head which you think are easy for first-time contributors, then sure, go ahead.
You could find them.
Yeah. I'm sorry, I haven't been able to contribute much more frequently. I was actually, time off. I had time off for the past month or so, so… Yeah.
I'll ramp back up, so…
**malff** 07:48 Well, it's, It's not an obligation, but if you are contributing, you might as well contribute on an area which interests you.
So, which is why I'm asking, in which… which area, do you… Do you prefer to look at?
**Pranav Sharma** 08:05 Right, so, because you're asking, there might be, some work coming my way which would involve around resource detection.
on Google Cloud and C++. There might be some work there, but I think that's more like a contrip thing, right? That's more in the CPP contrip thing. Are there resource detectors in C++ right now?
**malff** 08:26 There are some in the SDK, but there are, I don't think there is anything in Contriba.
**Pranav Sharma** 08:34 Okay, where would you typically, add vendor-specific, resource detectors? Like.
**malff** 08:44 So, if it's just OS-specific, we can always have, some code for that to investigate, it's not an issue. When it's more, like, vendor-specific, like Azure.
**Pranav Sharma** 08:56 Or another cloud.
**malff** 08:58 This typically should go in Contrib.
**Pranav Sharma** 09:01 Okay, okay.
Good to know.
**Nikhil Bhatia** 09:04 Actually, Pranav, I was working on resource detectors, but, yeah, I stopped around, operating system resso- resource detectors because The list is very long, and Yeah, I'm thinking to do, but… I'm finding a way around, so…
**Pranav Sharma** 09:23 I see. Yeah, that's good to know, but I was asking more around, like, vendor-specific resource detectors, like GCP or AWS, or something like that.
**Nikhil Bhatia** 09:34 So, actually, in that original issue, Lalit said that all the vendor-specific, resource detectors would go in the contrib report.
**Pranav Sharma** 09:42 Okay, yeah, that's good.
**malff** 09:47 Assuming we have a clean interface so that there can be a moduling contributor.
Since this has never been done before, we may have… we may have some surprises there.
**Pranav Sharma** 09:58 Right.
Right?
Yep.
So, yeah, just to… a heads up, like, this work might be coming my way in the coming month or so, so… Okay. Maybe that's an area.
I think, I was working on this API support for logger-enabled.
One as well. Like, I think I was working on it. I had to kind of stop it midway, but maybe I'll just pick that back up.
**malff** 10:31 Okay.
None.
Also, I'm working on many different things at the same time, so I don't have too much time.
Sometime I have, sometimes I don't, to look at things.
**Pranav Sharma** 10:51 Yeah, totally understandable.
**malff** 11:11 Okay, I haven't looked at the… all the different dependencies. I know that Spec made a release recently.
But since we… we don't have a strict, good dependency on specs, so we are not so much affected. We just need to… to make sure that, yeah.
Last month.
We need to make sure that we… we keep up with the spec.
Different story. And for the rest of it, I have not seen any recent changes, so I think we are… Fairly up to date.
Yeah.
Although this is getting old, so, it's probably be… probably it would be… release again soon.
We have some… still some work to do on configuration to go GA. We still have some very minor things to do, but it's, He's ticking, It's taking shape. There is a second release candidate that just was published, we need to align to that. We got some minor changes.
And Portov usually is very quiet. We did upgrade recently.
Ou vous… I'm not sure if we use 1.8 already, or if we still are on 1.7. I don't remember.
Need to check that.
And Weaver, this is the thing that goes with semantic convention, it's, It's very stable as well.
I think… I think we should be up to date with that.
Okay, I was hoping to discuss some issues and PRs with Tom for Windows.
And we've dug for the configuration thing, but since they're not here today, I think we can… Skip that and discuss that next week, if it's okay with you.
**Pranav Sharma** 13:29 That sounds good to me.
**malff** 13:33 Okay.
any… Any other topic, then, you would like to discuss?
Because I don't… I've not prepared anything, so I don't have a long list, as usual, for today.
**Pranav Sharma** 13:50 Nothing, nothing from my side, currently.
**malff** 13:53 Okay.
Just a reminder, this Google document, it's, you should be able to write to it, so if you want to discuss something, feel free to add any notes, so that we can prepare for the next meeting as well.
If you have a question or want to Yeah, to discuss a specific thing. Feel free to add to the agenda.
And speaking of which, Okay.
Yeah, so it works, you can… You can actually edit the document.
Okay, if there is nothing else, we can make it a short meeting then, because I have other things scheduled for this evening as well.
Thanks, everyone, for… yeah, thanks everyone for joining.
Come on.
**Nikhil Bhatia** 15:21 Thanks, Mark. Thanks, Bran.
**Pranav Sharma** 15:23 Yep.
**malff** 15:24 Bye now. Bye-bye.
**Nikhil Bhatia** 15:25 Bye.
