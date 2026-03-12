SIG: Kubernetes Operator SIG
Date: 2025-06-19
Duration: 8 minutes
Zoom Recording URL: https://zoom.us/rec/share/EpforpMfnqrbcHT0Nba1oyjsuBXZHRIrppNehinuSefoWjJ41IaRFQwAvpl1way4.6_-KnmtacbA9QYFk
============================================================

## Zoom Recording Transcript

**ploffay** 01:42 Happy lyde.
**Mikołaj Świątek** 01:51 Hello! Can you hear me?
**ploffay** 01:53 Yes, yes, I can hear you.
**Mikołaj Świątek** 01:54 You.
**ploffay** 01:56 Can you hear me?
**Mikołaj Świątek** 01:58 Give me a second.
Yes, of course.
How about now?
**ploffay** 02:06 I can hear you.
**Mikołaj Świątek** 02:07 Yeah, I can hear you now as well. Alright! Cool.
**ploffay** 02:09 Okay. Awesome.
**Mikołaj Świątek** 02:11 Everyone to wait like maybe 2 more minutes. I don't know if anyone else is gonna enjoying today.
**ploffay** 02:21 Yeah, I think lot of people are on public holiday today.
**Mikołaj Świątek** 02:29 Yeah, am, too, you know.
**ploffay** 02:32 Or Indos.
**Mikołaj Świątek** 02:34 Yeah, I've had. I don't mind showing up for this meeting sometimes sometimes, and when when I like.
I'd like, I don't know. This is a good mission to make, but sometimes sometimes on like my off days, I I kind of sit down and and write some code, or do some stuff for like an hour or something, and I just find it relaxing as opposed to, nor on during normal work hours where everything's caught up in in like plans and milestones, and 50 different things, and people asking me stuff on slack, and so on.
**ploffay** 03:11 It's definitely much quiet and like.
you don't have to reply, and you have to be present. You can just do the work that you you want to do right.
**Mikołaj Świątek** 03:26 Yeah, sometimes it's nice to have a quiet day, although I don't think I don't think anyone else is gonna arrive now. So I think I know. If you if you just wanna leave all the stuff that's in the that's in the document for next time. That's also okay with me. I don't know if it's like worthwhile to talk about it if you want to, because it's like a bunch of just a bunch of issues linked you can have a look at them offline. There's 1 particular one where we have a bug.
and I just want, but it's like a bug that we've had from the very beginning. I think so. It's almost like a feature at this point.
Oh, and it's about like the priority of environment variables in for instrumentation where and and the issue it had. The issue has a discussed at Sig label.
it's basically the fact that the the priority is wrong for for the instrumentation, because we have, like 2 levels of environment variables, right in instrumentation, we have the global one for the instrumentation object. And then we have the per language, one.
The priority should, and the priority should be something like highest priority are the language spec ones, then the global instrumentation ones, and then, whatever the instrumentation just sets by default, right? And it's the other way around, like the the instrumentation defaults are, have higher priority than the than the global variables.
which I think is an obvious bug. But it's also like, I said, a bug that's been there for a long time.
So.
**ploffay** 05:34 So you say, the the global one should have the highest priority.
**Mikołaj Świątek** 05:37 No, no, I think the global one should have higher priority than the defaults, because right now, if you try to set something in there that's set by default. Then the default wins, which is not correct.
**ploffay** 05:50 And set by default.
How is the default set.
**Mikołaj Świątek** 05:54 I mean, the defaults are just things like auto, something something exporter, right or or or the protocol like whatever all the resource, attributes all, we set a bunch of environment, variable variables by default.
**ploffay** 06:10 For when we inject instrumentation and.
**Mikołaj Świątek** 06:14 But if the user sets them their own, then we then we let them right.
**ploffay** 06:20 Here, something else is happening.
**Mikołaj Świątek** 06:22 I'm not sure if this is like I I don't think this is behavior that anyone anywhere actually relies on. I think it's more more likely that barely anyone ever does this, which is why we haven't known all this time.
**ploffay** 06:37 Yeah, probably.
**Mikołaj Świątek** 06:39 Yeah, but but, like I I don't know like the the issue is here. If the only thing I'm looking for is just like, you know, thumbs up on. Let's fix it.
maybe maybe. And maybe, like, you know, point out in the change lock what's what's supposed to happen.
**ploffay** 07:03 Yeah, I think that should be fixed.
**Mikołaj Świątek** 07:08 Yeah. And I, I, personally don't have don't really have anything else the other things that are in under discuss at Sig can just stay there. None of them are really very urgent. I don't think they're like proposals about what we should be doing in the long term.
So if we don't have anything else, then we can just you know.
**ploffay** 07:41 Yeah, you can wrap up and get some time back at least.
**Mikołaj Świątek** 07:44 Very cool.
Thanks. Have a have a nice have a nice rest of your day.
**ploffay** 07:50 Yeah, thank you. You, too. Enjoy your day off. You shouldn't be working.
**Mikołaj Świątek** 07:55 Okay.
See? You.
**ploffay** 07:57 Alright! See you bye.
