SIG: Zig SIG
Date: 2026-10-21
Duration: 45 minutes
============================================================

## Zoom Recording Transcript

**Francesco Gualazzi (OpenTelemetry)** 01:27 Hi there.
Johnny, can you hear me?
Wait a sec.
Now, can you hear me?
Meeting now?
I can eat a no, okay?
**Giovanni Panice** 01:50 Okay, okay, okay, cool.
**Francesco Gualazzi (OpenTelemetry)** 01:52 My Zoom misbehaving.
How you doing?
**Giovanni Panice** 01:58 Well, fine, fine. You? Yeah.
**Francesco Gualazzi (OpenTelemetry)** 02:02 I'm good, I'm good.
**Giovanni Panice** 02:03 Buh.
Yo… You notice from my voice… Yes.
Okay. I understand.
**Francesco Gualazzi (OpenTelemetry)** 02:10 I understand.
Quiet, don't worry.
**Giovanni Panice** 02:23 Got it.
So, do you think that,
**Francesco Gualazzi (OpenTelemetry)** 02:28 Probably Antoine is not gonna join, but I… am I mistaken, or… The previous meeting was on October 14th, not this… not the 7th.
We had a meeting last week, no?
**Giovanni Panice** 02:41 Yes, yes, yes.
**Francesco Gualazzi (OpenTelemetry)** 02:42 So this…
**Giovanni Panice** 02:43 Maybe we didn't, we didn't, Bright 10, if you could probably talk to them.
**Francesco Gualazzi (OpenTelemetry)** 02:53 Okay.
Okay, maybe I messed it up.
But whatever.
So Yeah, the status of 0-17 upgrade.
I have reviewed and left a couple.
**Giovanni Panice** 03:09 Of course.
**Francesco Gualazzi (OpenTelemetry)** 03:09 for Antoine. Have you tried out the PR?
**Giovanni Panice** 03:13 No. No?
**Francesco Gualazzi (OpenTelemetry)** 03:16 Oh, okay, okay, okay.
Okay, okay, so, okay, Antoine replied. Very good.
Okay, run benchmarks, well done at 1, 6 hours ago. Okay, I'm gonna merge, I'm gonna prove and merge.
That's beautiful.
Antoine, great job, if you listen to this.
**Giovanni Panice** 03:40 Nice. Anyway, I… I can, I mean, I'll feel the vibes.
**Francesco Gualazzi (OpenTelemetry)** 03:49 Yes.
Okay, let me just, Okay, let me just do quickly an approve and merge. This is, this is incredible.
The update to… to… 017 is… is… Awesome.
Okay.
**Giovanni Panice** 04:11 Yeah.
**Francesco Gualazzi (OpenTelemetry)** 04:12 Because, again, Zig is still not yet 1.0.
I guess it will not be for a long time, because there are still so many things To be improved, not in the language, but in the ecosystem, right?
So… yeah.
And when it's gonna be 1.0, I guess by then, a lot of people will have seen the value that it brings on the table.
Okay.
Actually, let me write in Slack.
That we have, merge the 017 upgrade, which is good.
And then, I don't know if you have any other topics, Giovanni, for me?
**Giovanni Panice** 05:08 No, from my side, nothing.
**Francesco Gualazzi (OpenTelemetry)** 05:11 Okay.
Looks good. So… I don't have anything.
**Giovanni Panice** 05:19 Okay.
We can close here.
It's not an issue.
**Francesco Gualazzi (OpenTelemetry)** 05:25 There has been a couple of new bugs, but nothing that we cannot handle. One for Windows, oh yeah, Windows support, that's… that's what huh?
**Giovanni Panice** 05:35 Oh.
**Francesco Gualazzi (OpenTelemetry)** 05:36 Apparently, none of us have ever.
**Giovanni Panice** 05:40 Yeah.
**Francesco Gualazzi (OpenTelemetry)** 05:40 filing for Windows. I mean, Hendrik, yourself, we'll run Linux, right, or Mac.
**Giovanni Panice** 05:47 Right?
**Francesco Gualazzi (OpenTelemetry)** 05:49 So, Windows support, how to progress, I myself want to… add a CI runner based on Win? I don't even know if it's possible in GitHub, but I guess so, because they… I mean, GitHub is part of Microsoft, so… Aren't they gonna offer Windows-based VM for their actions? I think so.
**Giovanni Panice** 06:11 I think, yes, because they offer for Apple, so I think they offer also for Windows and so on.
**Francesco Gualazzi (OpenTelemetry)** 06:16 Okay, so what I will do, and let that assign to me, Is it?
Doesn't work like this.
Assigned to… That's cool So I will… I will take care of that, because the bug is legit, so… we… we call a POSIX API that doesn't exist on Windows in Clock.
And, I mean, it even slipped… it even slipped my review when we added the clock stuff, which, by the way, I would reconsider having at all. The entire clock namespace that we have, I think it's… Just bloat.
Maybe we can get rid of it, Let's write it down as an opportunity. So, as I…
**Giovanni Panice** 07:06 No.
**Francesco Gualazzi (OpenTelemetry)** 07:06 Right? So, add the CI runner based on Windows, I will do that, it's super easy.
**Giovanni Panice** 07:11 I think that we will have other stuff at Windows, so it's important to have a CI that's built for Windows.
**Francesco Gualazzi (OpenTelemetry)** 07:20 Exactly. So, Clock.zig, I made a recent change in Clock.zig, adding a… timed function call to allow… to fix a bug in the OTLP exporter, but… again, we don't have to have it together with, you know, getting the timestamp and all of that. I think we can get away with something from the standard library, and should be, by nature, portable across all environments. But, yeah.
Let me, let me figure that out. Actually, I will create the issues for that.
**Giovanni Panice** 07:54 Okay.
**Francesco Gualazzi (OpenTelemetry)** 07:56 Or we can switch to… the Lib… usage.
What's there.
So the helpers define it there.
All right, what else? Let me open the issues real quick. Okay, update for Zig is done, so I will write in Snapchat was 017.
Thanks, Juan.
Or the big effort.
In making it happen.
Please update your, forcs.
Of course, and Z gap, 0170… When?
Bing.
October.
Nice Beautiful. What else? Let me quickly go through the issues… Windows support… Yeah, the other one about OTLP is dependent on Jacob's PR.
We still have it there.
Oh, this one by Bach. There are two from Bach on the.
**Giovanni Panice** 09:23 Can you share the screen? Can you share the screen?
**Francesco Gualazzi (OpenTelemetry)** 09:25 Apologies.
**Giovanni Panice** 09:26 Oh, don't worry.
**Francesco Gualazzi (OpenTelemetry)** 09:32 Is it?
Is it too big? Is it too small? I can zoom.
**Giovanni Panice** 09:41 It's a bit small, if you can zoom.
**Francesco Gualazzi (OpenTelemetry)** 09:44 So… Yeah.
Windows support, I will work on it.
Actually, let me assign this to myself.
And now we'll create the necessary sub-issues.
This one is on hold, because, again, we need to wait for… Zig protobuf compared to changes in Agust PR.
Shut down, skips final collect. This is a bug reported by Buck. I… we should find someone to work on it, although for the metrics, I should be probably the one working on it, because I know the metrics inside out, because it's the first one that I wrote.
Shut down… yeah, this one needs to be fixed. There's an actual theme about better synchronization across exporters and readers.
in the whole SDK, maybe we can come up with a… Standalone component that does that, and, you know, and dispatches to the values signals? I don't know, but I will… I will have to figure out what this is.
This is… this is not… Yeah, I replied already to back, yes, okay. We send the PR, right? Because this is a pure… It's a small task, we just need to fill in the stress state field in the spot.
This one…
**Giovanni Panice** 11:11 The, you can do.
**Francesco Gualazzi (OpenTelemetry)** 11:13 Yeah. No, but also, Bacco is also… has been working on the trace propagation, so he knows that part very well.
This one was raised by Antoine, we discussed it together, that, we need to change the SEMCOM generator.
But it's not… it's not a priority right now, because… We don't really need strictly typed enums.
for the CENCOM staff. And that one, Daisuke.
wanted to work on it, and I don't know if it's still… Going to… Okay, this one should be… okay, I will merge this one next, so you can work on that.
And that's… that's basically it, because this… Oh! Oh, I completely missed this one.
Ouch.
Alright.
So this is from the guy that is trying to add the OpenTelemetry into the Vercel RMS coding agent, right?
-Oh.
I guess… I guess I will have to reproduce, see if it's with the recent changes that we did to the exporter.
is still valid? Yeah.
I don't know if I can work on it, honestly.
That's basically it, because the others are already known stuff, but yeah, good stuff, good progress.
I guess what this is about.
I guess. So if we really want to give a timeline for the beta, sorry, for the alpha.
**Giovanni Panice** 12:54 Yes.
**Francesco Gualazzi (OpenTelemetry)** 12:55 Can we create a milestone?
**Giovanni Panice** 12:57 Yeah.
**Francesco Gualazzi (OpenTelemetry)** 12:58 Can we create a milestone? Where is that called?
**Giovanni Panice** 13:02 In project, you should do it, if I remember correctly.
**Francesco Gualazzi (OpenTelemetry)** 13:05 No, no, it should be around here.
Project?
**Giovanni Panice** 13:14 Yeah, I mean, if I recall correctly, the, Our liaison created the project, no, and there we can create the milestone.
**Francesco Gualazzi (OpenTelemetry)** 13:31 Why are you… okay, so how do we do that? Let me see.
**Giovanni Panice** 13:35 Check the issue, and maybe you Find the project, yeah. Goldway…
**Francesco Gualazzi (OpenTelemetry)** 13:40 Yeah.
**Giovanni Panice** 13:42 1 issue… Okay. Okay.
**Francesco Gualazzi (OpenTelemetry)** 13:45 Zig Singer? Yeah.
**Giovanni Panice** 13:47 Okay, so, yes, exactly.
**Francesco Gualazzi (OpenTelemetry)** 13:48 No, my… I don't know my instrument, look, look.
Okay, if you don'.
**Giovanni Panice** 13:51 No, you have… yeah, you… in the project? Yeah, here, you should, find something… I don't think we…
**Francesco Gualazzi (OpenTelemetry)** 14:01 create the milestones from here, right? Do we?
**Giovanni Panice** 14:10 Go to Roadmap?
Tap roadmap, yeah.
**Francesco Gualazzi (OpenTelemetry)** 14:17 He's the fourth…
**Giovanni Panice** 14:19 Fourtha, 4th, 4th.
**Francesco Gualazzi (OpenTelemetry)** 14:20 Okay.
**Giovanni Panice** 14:22 Okay, welcome to Roadmap, If you click on the plus, what is… what happened? Create the date or iteration of it to specify dates.
**Francesco Gualazzi (OpenTelemetry)** 14:38 This one iteration. What I wanted to do is a milestone.
**Giovanni Panice** 14:42 Yeah. That's okay.
**Francesco Gualazzi (OpenTelemetry)** 14:43 I can figure it out later. So what I will do is I will create a milestone.
That is the alpha release.
And I will add all the bugs that we need to fix before we can call it the alpha.
**Giovanni Panice** 14:58 -
**Francesco Gualazzi (OpenTelemetry)** 14:59 For example, this needs to be done.
**Giovanni Panice** 15:02 Yeah, yeah, yeah, yeah.
**Francesco Gualazzi (OpenTelemetry)** 15:04 Probably this.
Of course there is.
**Giovanni Panice** 15:11 It's very simple. Open an initial, open initial.
**Francesco Gualazzi (OpenTelemetry)** 15:15 Yep.
Good to you.
**Giovanni Panice** 15:16 No, no, no, no, sorry, name.
**Francesco Gualazzi (OpenTelemetry)** 15:18 No, anywhere, anyway.
**Giovanni Panice** 15:19 You ever, yeah, any issue, yes, yeah?
**Francesco Gualazzi (OpenTelemetry)** 15:23 Happening.
**Giovanni Panice** 15:24 Okay, then, this one?
Yeah?
So, for example, you want to add it in the milestone, write the name of the milestone that you want to create, for example, the…
**Francesco Gualazzi (OpenTelemetry)** 15:36 Exactly. There you go. Exactly.
**Giovanni Panice** 15:37 Yeah, yeah, yeah.
**Francesco Gualazzi (OpenTelemetry)** 15:41 Alpharis.
Alright.
**Giovanni Panice** 15:43 Thanks, Seth.
**Francesco Gualazzi (OpenTelemetry)** 15:44 Beautiful. Do we want to set a due date for this?
**Giovanni Panice** 15:48 I'll say no. I mean, from my side.
**Francesco Gualazzi (OpenTelemetry)** 15:52 I don't need more than that.
**Giovanni Panice** 15:54 Exactly.
**Francesco Gualazzi (OpenTelemetry)** 15:56 I want more deadlines.
**Giovanni Panice** 15:58 Otherwise, my dead.
**Francesco Gualazzi (OpenTelemetry)** 16:00 But that's good. No, that's all. This is a bug, so I can do alpha list. Okay, so I will do that, right? Okay, let me actually write this down, so… defining the milestone… Or the first Alpha Aries.
Auto… SamCom… SDK.
Right?
Oops.
Okay, so… Okay, let's do that. We don't need… for example, we don't need that.
We don't need this, although Daisuke will work on it.
We definitely need this.
This looks like a bug.
betting test from the logs? No, I think it's on the trace.
Yeah, export spans, yes, yes, yes.
Milestone alpha.
Okay.
Okay.
this… I mean, this is… this should be in, because it's a supported feature, but maybe not.
The files we don't need, exemplars we have to, yes.
**Giovanni Panice** 17:22 Yeah.
**Francesco Gualazzi (OpenTelemetry)** 17:27 This is featured.
Do we have a feature?
**Giovanni Panice** 17:32 An incident.
We are in.
**Francesco Gualazzi (OpenTelemetry)** 17:34 Announcement?
**Giovanni Panice** 17:37 If you want to…
**Francesco Gualazzi (OpenTelemetry)** 17:38 then… oh!
Oh!
Oh, I completely missed this.
**Giovanni Panice** 17:47 Don't worry, you can answer the error, it's normal for…
**Francesco Gualazzi (OpenTelemetry)** 17:51 But it's been months, so…
**Giovanni Panice** 17:53 It's not a problem, it's not, it's not a problem, no. I'm answering, like, I answer people, like, ages, don't worry.
**Francesco Gualazzi (OpenTelemetry)** 18:03 I completely missed this, I don't know why.
**Giovanni Panice** 18:07 Well, I know why. Too many things to do.
**Francesco Gualazzi (OpenTelemetry)** 18:15 Yes.
Okay, very nice.
GRPC, of course.
But GRPC is almost done.
**Giovanni Panice** 19:01 Yep.
**Francesco Gualazzi (OpenTelemetry)** 19:02 Because now that we have 017, I guess the proto is updated, and
**Giovanni Panice** 19:08 can move from draft to…
**Francesco Gualazzi (OpenTelemetry)** 19:11 Exactly. Now, now it should be easier for Antoine to… to do that.
I mean, this… this… rude, but maybe not. I mean, we don't… Yeah, yeah, I had to lose this one, I remember.
Yeah, yeah, yeah, yeah, yeah.
Oof.
Too bad.
Maybe I can resume this.
But let me see… Well, I will fix… I will check this later.
But it's not, again, it's not, it's not something that we have to do right now.
It's just an idea.
Block 3 we don't need, this we don't need… this we don't… okay, so the milestone basically… okay, let me see how… how far are we?
Not too bad. So this one… Yeah, Windows support… yeah, Windows support needs to go.
What?
Okay, I missed that.
That's it. I guess, yeah, I guess that's it. We can… Build… Marvel's build… How is it on your side, the weather? Is it raining like here, or is it easy?
**Giovanni Panice** 20:35 Raining, sorry, raining, you said, raining, yes.
Yeah.
**Francesco Gualazzi (OpenTelemetry)** 20:42 Okay, so… Realistically, I don't want to put to that line, but realistically, I think…
**Giovanni Panice** 20:49 For the end of…
**Francesco Gualazzi (OpenTelemetry)** 20:50 End of year, we are going to go.
Which is not bad.
To think that I started writing the unofficial one March, April 2025.
bad.
**Giovanni Panice** 21:06 Yeah.
**Francesco Gualazzi (OpenTelemetry)** 21:07 Thanks.
I guess that is, that is all.
**Giovanni Panice** 21:13 Yeah.
You can write that we have defined it in milestone.
**Francesco Gualazzi (OpenTelemetry)** 21:25 Okay, good, thanks, yes.
you know, I don't understand why the name of the… there's lags for emojis is different between Google, and Google picks their own, I don't know.
Okay, yes, defined as… Alpha, there it is.
And I can actually link to that, right?
Yes, this one.
Yeah.
Oops.
Like this.
It's happening.
It's time for a new computer, huh?
Okay.
Beautiful.
See you next week, huh?
**Giovanni Panice** 22:35 Okay, yes, Francesco.
**Francesco Gualazzi (OpenTelemetry)** 22:37 Get some sleep?
I'm sorry.
**Giovanni Panice** 22:42 Bye.
**Francesco Gualazzi (OpenTelemetry)** 22:43 Enjoy.
**Giovanni Panice** 22:44 And…
