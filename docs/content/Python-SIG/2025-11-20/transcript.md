SIG: Python SIG
Date: 2025-11-20
Duration: 19 minutes
Zoom Recording URL: https://zoom.us/rec/share/8KlqWyfHpY3S4Skx3uSzdGDvg5VnsfAK5M32Wy83h93-K2_rGvdUhFD_YZrnxjtB.e83Rt0sOFVZkvjeH
============================================================

## Zoom Recording Transcript

**Riccardo Magliocchetti** 00:23 Hello, everyone.
**Keith Decker** 00:26 Morning, afternoon, evening, wherever you are.
**Hector Hernandez** 00:30 Hello.
**Riccardo Magliocchetti** 01:32 So, welcome, everyone, to this week's part of sync call. We're waiting a few more minutes for more people to join.
In the meantime, please add yourself as an attendee to the sign notes. I'll share the link in the chat.
And if you have any topic you want to discuss, please also add them to the notes. Thank you.
**Aaron Abbott** 02:23 Hey everyone, sorry I'm late.
**lechen** 02:26 Hello.
**Riccardo Magliocchetti** 02:45 Okay, we have 10 people.
I think we can start. Welcome again to this week's Weekly Code.
Please add yourself as an attendee, and if you have any topic you want to discuss, feel free to add them to that.
signals.
First topic is from me, some updates on the log stabilization process. We merged, Ecto… another actor of PR.
This week.
Yeah, thanks, Ector. This one was the one renaming from… Classic from log to log record, but we are still keeping the old names around, just with deprecation note.
Yeah, so after imaging this, I took a look of users we have around.
We have some entries in the OpenTrial documentation.
And I… I think Emilio, already proposed to implement them, like, to fix RAM?
And we have some interest in Contrib, but there is already an open PR from ACTOR.
But… Still… requires some fixes, because we need to handle both, versions, because some, like, mostly the GenAI implementation are… are testing against, like, a baseline API version, and also on the latest.
And so the oldest one, of course, does now have the… current classes.
**Hector Hernandez** 04:38 Is this something that we want to include next release as well? I totally forgot about this one, to be honest.
But, I can make the changes if we want to include this, next release.
**Riccardo Magliocchetti** 04:52 Yes, please?
**Hector Hernandez** 04:54 Okay.
**Riccardo Magliocchetti** 04:55 Like, like, because at the moment, I think some stuff… Like, we get, like, just a ton of, deprecated warnings in the test, but, like… I think it would be nice, like, to… like, if SundaysTream user needs an example, at least we can point them to our… instrumentation, I guess.
**Hector Hernandez** 05:24 What about the release plan? I'm asking, I don't want to be the guy who broke everything before the holidays, so do you guys have some plan for release?
**Riccardo Magliocchetti** 05:37 Like, my plan was to To cut release after we merged, your PR And I think we have other stuff in the tracking issues, but I don't think we are urgent as these ones.
And so, I think the earlier the better.
Like, hopefully the warning… And just was, like, helpful?
Yep.
Cool. Like, we added that to the change, look, we have some… Like, I hope we can handle that.
Like, I'll be around until, Christmas, so until end of December, so hopefully, like, we have time to fix that, any issue, yeah.
**Hector Hernandez** 06:29 Sounds good. Thank you.
**Riccardo Magliocchetti** 06:40 Okay, so… Yeah, like, I also, like, this morning, pinged a couple of people, I pinged Alex from Logfire.
Because I like… I think we need to do some changes in their stuff.
I haven't heard back from him, but, like, we'll see.
And also filed an issue on open telemetry.
Just, like, pointing out that it would be nice if we moved to a meeting, Lorec, like, on your, Like, if you found a decent enough open telemetry.
SDK, if I can just, like, emit log records instead of events, so we can merge, like, we have, Dylan PRs from many months ago.
But we'll add some deprecation notice, Over event classes.
Also there, I haven't got, feedback?
Oh, no. Okay, cool. We're working on a fix, nice.
yep.
Yeah, we already did go through October 7thrit.
And so… Any comments?
**Aaron Abbott** 08:17 No, thanks for working on this, Ricardo.
Yeah.
**Riccardo Magliocchetti** 08:24 Okay, cool.
Thank you. And… okay, next topic.
is also from me, just a quick one. Like, some days ago, I opened up PR, from being able to, override the default, processors we have for, logs and traces when using out-instrumentation.
Yeah, like, from people maintaining Vistra may be interesting for them, so… If you have time, please take a look. Like, you have no hurry in getting this in. I also left some comments.
One is about, like, some typing.
And the other one is, Like, if you have any opinion, if… Maybe you have use cases.
For, like, where, one processor, Maybe enough.
Or maybe you want a specific processor for every export you have in the pipeline?
So, yeah, if time are interested, please take a look.
**Aaron Abbott** 09:41 I think I missed some of the context here, but is this for…
**Riccardo Magliocchetti** 09:44 Auto instrumentation?
Yeah, this is, like, in the configure code.
Where, at the moment, we are coding, the batch spam process, and I don't have my Marx code.
The waffle locks.
They'll… Yeah, batch log record processor.
And, like.
I think in my distro, I would prefer to have our own processor, so… in case I need to implement something.
I can do that there, and… Like, I currently use the current, SDK configuration machinery.
**Aaron Abbott** 10:29 Isn't there an entry point for the processor?
Where is it?
**Riccardo Magliocchetti** 10:33 we have entry points for, processors, yeah, but… like… I think we have VAMF.
for, loading them, but I'm not sure if you have one for, like, deciding which one to use.
**Aaron Abbott** 10:56 Okay.
**Riccardo Magliocchetti** 10:57 So, yeah, but good point. I should probably take a look at that. Thank you.
**Aaron Abbott** 11:04 Yeah.
The other thing I was just gonna point out was, I wish I had time, but the YAML config stuff… I feel like it would make… a lot of this much easier. I mean, it wouldn't help with the distro use case, but, It would be… Nice to put effort there.
**Riccardo Magliocchetti** 11:28 Yeah.
like, I guess, with the YAML configuration, like, we need to take… Another, like… Probably will need to rewrite our configuration story, because… Like, it's probably very different.
**Aaron Abbott** 11:45 Yep.
Nope.
**Riccardo Magliocchetti** 12:01 Okay, in the meantime, I'm adding notes. Keith?
Your topping is next.
**Keith Decker** 12:09 Hey, so, thanks for the reviews this week on the additional attributes for SimConf, so, or for… inference calls. This one is for adding metrics to LM invocations for… for Gen AIA, so I just need some more reviews on it. I already got one from Noodmilla, looking for… More eyes on it.
I just updated to main and fixed some latent issues, so should be ready to go.
**Aaron Abbott** 12:42 Yeah.
I would, I would offer, but I honestly don't know if I'll get a chance to review it before somebody else.
But yeah, like, Lyudmilla.
Her approval should be good here. It probably just needs, like, a… Probably not a big deal if she approved it. Just take a quick look for Python, readability kind of thing.
**Keith Decker** 13:10 Sounds good.
**Aaron Abbott** 13:12 Okay, yeah, sorry for the delays here.
**Keith Decker** 13:18 Yeah, appreciate your time.
**Riccardo Magliocchetti** 13:31 Okay, thanks, Keith, for the PR. Any other comment?
Or… Any other topic?
By the way, speaking of reviewer, I think, we are, like, making… Ludimila as an approver for both repos.
Because I think she lost them… the green tick after some, I guess, admin configuration?
Yes. So, yeah.
**Liudmila Molkova** 14:09 Thank you. Appreciate your trust.
**Aaron Abbott** 14:13 Thank you.
**Riccardo Magliocchetti** 14:14 your head.
Okay.
So… Yeah.
Looks like this has been, Quick one.
Thank you, everyone.
Yep, have a nice day.
**Hector Hernandez** 14:48 Thank you.
**Aaron Abbott** 14:49 Yep, thanks everyone later.
**Keith Decker** 14:52 Bye.
**Liudmila Molkova** 14:53 Thank you.
