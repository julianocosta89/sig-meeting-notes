SIG: C/C++ SIG
Date: 2026-06-10
Duration: 29 minutes
============================================================

## Zoom Recording Transcript

**malff** 03:50 Hi, Doug.
**Doug Barker** 03:51 Hey, Mark, how's it going?
**malff** 03:53 Not too bad.
I'm struggling against zoom. Somehow, it took the focus of my mouse, and I cannot click anywhere else, and not move anywhere.
And of course, this is recorded, so I would be famous for that.
So, how have you been?
**Doug Barker** 04:18 Oh, not too bad. It's starting to get warmer here in Massachusetts. The weather's nice.
How about yourself?
**malff** 04:27 Very, very busy with many different things at once.
**Doug Barker** 04:31 Yeah.
**malff** 04:35 So, I can't go over the notes, but, which I've not prepared anyway, but one thing I would like to discuss in general is, have you seen the number of PRs that we have?
**Doug Barker** 04:44 Yes.
**malff** 04:45 And not only we have a lot, but there is a constant flow of fixes coming in.
So it's, It's a good thing, a good sign, good thing, but also, I've started to notice that sometimes it causes conflicts, because two different persons are fixing the same thing, exactly.
So we have, sometimes two PRs for the same issue, and people don't even… are not even aware of that.
**Doug Barker** 05:16 Yeah, I was looking briefly at the, the composable sampler, probability sampler, and I think there's a conflict there as well, and you marked one as duplicate.
**malff** 05:26 Yep.
Well, on this one, so I've… I have not approved it and merged it yet, but I think I will take the composable sampler, because it's the most, complete.
And so, the samplers which are implemented, they are not used yet, but at least they are implemented and they are tested with unit tests.
And if we take that, I guess the next step is to hook them up in the SDK builder when we parse YAML.
And that should be easy to do then.
Yeah.
**Doug Barker** 06:06 That makes sense.
**malff** 06:07 Yeah, and once we have that, I think we can take a look at the probability sampler again and see if it fits.
Or not.
**Doug Barker** 06:16 Yeah, I'll make a comment on the composable sampler PR. I think the only thing I noticed was the, they implemented… it looks like they implemented the probability sampler, but called it the trace ID ratio sampler.
**malff** 06:29 Yeah, well, the…
**Doug Barker** 06:31 So I think it's just a naming issue, but I think there's… the spec calls out.
**malff** 06:35 composed before.
**Doug Barker** 06:36 probability sampler, and I think that's what we probably just need to rehab.
**malff** 06:39 Yeah, there is… there is some history in the spec itself, because it has both samplers and Composable samplers, and those are different.
So, I would not be surprised if we have both in the spec, but just to… we need to double-check, but… there is a bit of history there. For example, the always-on, always off.
There are two in the spec, one for sampler, one for composable sampler.
It's kind of strange, because there is a… I think it's meant to have a migration path, but from one to the other, but… Oh.
to investigate.
**Doug Barker** 07:17 Yeah, and I logged that issue to create the probability sampler. I didn't realize at the time that it was, like, somehow implied or included in the composable sampler.
**malff** 07:27 No.
**Doug Barker** 07:27 But I think, and you may know, I think I looked into the configuration, schema, and it doesn't have a standalone probability sampler, is that right?
**malff** 07:37 Not yet.
**Doug Barker** 07:42 Yeah, so that might be the confusion. It's like, do we just deprecate all the other samplers and just use composable samplers, or how's it supposed to work?
**malff** 07:51 Don't know yet. But the good thing is, it's nice to see some people actually contributing some parts. So… There are a couple of people doing a cleanup, Incident ID, which is nice. I also saw that you reviewed the PR, making some cleanup on include what you use, especially the discrepancy between CI and the dev container.
And that was… that was a bit weird, but it's, oh.
It's actually much better now that we have the same results in the dev container and NECI, because then people can… Sort things themselves, as opposed to… Push and wait for, GitHub to do the build and finally pick up on that, so… So yeah, so we have that. We have some small fixes in ceiling tidy and things like that.
And at the same time, some fixes in the… in the YAML config file, some fixes in samplers, I mean, different, different places, so… It's, good news.
Hi, Tom.
**Tom Tan** 09:05 Hi, Mark and the dog.
**Doug Barker** 09:07 Hey, Joe.
**malff** 09:10 I'm sorry, somehow my mouse is stuck. Zoom can… don't want to… to give it back to me, so I cannot, Scroll on… scroll on issues and on the agenda, also.
We just have to… I just have to talk for Nemo, Eva.
Tom, so, as you may have noticed, we have quite a few PRs, and some of them also, which is unusual, are touching ETW.
I think two different persons there are making changes to that to, to fix.
a couple of things. Do… Do you have some time to take a look at it, maybe?
**Tom Tan** 09:56 Yeah, I will take a look at the E2W exporter related changes.
**malff** 10:01 Okay. I saw that Lalit started to comment on that already, but I think there are 3 different PRs, so not sure if you've seen all of them.
**Tom Tan** 10:10 Yeah, I also saw that, yeah, just need some more time to review it.
**malff** 10:14 Okay.
**Tom Tan** 10:16 Thanks.
**malff** 10:23 And, one thing which is going on right now, so… what was it? Oh, yes, for the environment variable, propagation.
So, it's basically propagation where instead of writing to HTTP headers or whatnot, when a process forks and over, it can pass the trace context in an environment variable, so we have code for that, and some Some way to support propagation for that.
Perride from the spec just noticed that we have some spec discrepancy, which are being addressed, and on top of that, I also filed an issue in the spec itself.
Because there are some things that I think can be simplified in the spec, so that we avoid having to look at every environment variable that exists.
To, to implement that.
So, just don't be surprised, this thing is moving in… at many different levels. It's moving in the code, which… because we just have a… had a fix that was merged, and it's also moving at the spec level with a… A follow-up discussion on that.
So… Hopefully that should be settled, soon, I guess.
And apart from that, I don't have anything special.
just noticing that we have a lot of… a lot of PRs, which is good.
**Doug Barker** 12:02 Mark, can we go over a few of the, items that we have tagged with Discuss?
**malff** 12:07 Sure, but if you have a screen in front of you, you need to… To call them out, because, like, my screen is frozen now.
Okay. I think, from memory, I think one was in the YAML config file. Yes. I think you proposed to split the meaning of with configuration, so that we can have all the configuration files themselves for the programmatic configuration, which are always available, and have the flag only for the YAML part. Is that correct?
**Doug Barker** 12:40 Yes.
**malff** 12:40 Yes, yeah, that sounds, that sounds good to me.
And on top of that, someone already made a PR for that.
And so the… I think we can merge that. The only… Only possible concern I have is that The library name is changed in the current PR.
Because we had, OpenTelemetry configuration, and now we have OpenTelemetry configuration, and a new library, which is… OpenTelemetry Configuration YAML.
So, this may break, existing make files if someone is using that today, but this can be adjusted, or… Or at least we can document that in the changelog, so that it's, hmm.
So that we define what to do instead of having people being broken.
But yes, I think it's a very good idea, and we should do that.
**Doug Barker** 13:42 I'll review that PR then.
**malff** 13:44 Okay.
Do you recall if we had anything else to discuss? I don't remember.
**Doug Barker** 13:56 We had several ones. I had flagged the, log record limits I think there's probably some… I know that there's a PR open for that, so I think probably a lot of the discussion can take place there.
One thing I wanted to discuss was on the recent merge of the emit log rate groups and the log record group filtering.
**malff** 14:16 Yes.
**Doug Barker** 14:16 I had some… some discussion with… with Olad, so I think what… Was merged is to disable the log record filtering based on severity.
in ABI V1, but then enable it in ABI V2.
wanting to discuss with you guys is, should there be a preview flag for that?
Since it's not necessarily a, ABI breaking change.
**malff** 14:41 Okay.
Yeah, I've seen that discussion, but I thought it was resolved, which is why I merged the PR itself.
Maybe I missed it, I'm not aware of anything else that needs to be… to be addressed for that.
I can… I can take another look.
I think Ladit has had some concern that, whatever we do, we should not have more overhead for ABI V1, I think.
That was the main line, as I understood it.
Okay, if… If there is something else that is missing that needs to be done, could you file a different issue for that so that we can follow up?
Oh.
Because the PR itself, is already merged, and it was… to me, when I merged that, it was already resolved, so if something was missed, we need to do that in a follow-up PR event.
**Doug Barker** 15:44 Okay, yeah, I think the only question remaining is, should we have a preview flag that allows, those using ABFV1 to turn that Severity-based log filtering on.
**malff** 15:57 Okay, yeah.
**Doug Barker** 16:04 A logger and a sheet.
**malff** 16:06 Okay, thanks.
There is also a big PR about, having a custom HTTP client?
not necessarily curl.
So VPR is getting big, because a lot of things had to be changed to basically And our trace metrics and log to use any clients, and a generic clients, not necessarily the current client.
So, a lot of helper classes that change as well.
As far as I understand, VPR… is, is ready to go. I don't see any open discussion remaining.
Could you… Could you take a look and confirm that?
If you… if you can.
And I don't remember if you looked at it, or if Lalit looked at it, or both, but the… basically, my understanding for this PR is that it's, for me, it's ready to go. I think I approved it already.
And, if you, if you see some remaining issues, just, Please comment so that otherwise, we'll merge the two, I guess.
And if you're talking, you might… you are muted, so…
**Doug Barker** 17:47 Yeah, I'll take a look.
**malff** 17:49 Okay, thanks.
Okay, I don't have anything else. Tom, do you have any… anything to discuss?
Odu.
**Tom Tan** 18:08 No from my side.
**malff** 18:12 Okay.
**Doug Barker** 18:12 True.
**malff** 18:13 Huh?
some, on the different things that happened recently as well, You remember that there is this workflow which looked at, everyone which is flagged as maintainer, or… approver who has not been active for a while, and this automation just throws PRs against all the different repos to say, hey.
This, this approval has not been, active for a long time. There is an OPR to To consider to… Remove the maintainer from the… or the approver from the lease, and so forth.
And we had one, in the Contribu repository.
And… it was not merged because Lalit mentioned that before doing so, we also needed to change the code on our file.
Otherwise, we… the quote on the file mentioned people who are no longer approving.
So, last week, I did that cleanup, this cleanup on the coroner, which Tom approved, and then I also went and merged the PR to do the cleanup on approvals. So, this thing is now done in CPP control, but just so you know.
**Tom Tan** 19:28 Do the PR can be marched, right? To remove, like… The inactive tenors there.
I saw the PR, the owner was paying rent on that PR.
**malff** 19:41 Yeah, so the code on a file is cleaned up, so it no longer mentions people by name who are no longer here, and the CPP contribute approvers have been cleaned up as well.
**Tom Tan** 19:54 Okay.
Yep, sounds good.
**malff** 19:58 In the long term, we still need to decide what to do with CPP Country, because it's, it's really taking dust there, it's not even building properly, and a lot of things Our story degrading.
But at least, what we have documented as who is in sync with the current state.
**Tom Tan** 20:21 I think we don't have a deprecation process for contributory modules, right?
**malff** 20:27 No, we… well, what we should have is a clear status of each country, but… Whether it is maintained or not, and we don't say anything, so at least we should We should at least mention which one are supported, which one are not, because I think that Geneva and things like that are supported by Ladit and yourself.
Yeah. But other things, at least we should clearly mention that they are not… no longer maintained, so that people don't have surprises, and then maybe someone will volunteer to maintain it then, or at least say, hey, I depend on that, can we please keep it?
Because it's… it's even unknown if… which contribute is actually used or not. It's.
**Tom Tan** 21:13 I think maybe when we could bring up a deprecation process, like, for an unmaintained component, we… we duplicate it after sometime, like, 6 months of no owner, and then we archive it. If someone wants it, they need to, like, stand up as owner for that.
**malff** 21:34 Okay. Yeah, we can… we can look into it.
**Tom Tan** 21:38 Yeah, because I think for us, we were trying to maintain, like, every, component in there.
**malff** 21:46 Oh, and especially some components have dependencies on third parties, like the web server and whatnot, and NGINX, so it's, It's another world, so we cannot just maintain everything.
**Tom Tan** 21:57 Yeah, that's… that's true.
Okay.
**malff** 22:03 Okay, I don't have anything else myself, So we had, recently, we had a lot of changes for cleanup in Scaling Tidy, and I'm hoping that this will continue.
ceiling… so yeah, it's feeling tidy. Include what you use, it's still clean, so it's, this is a good thing.
Also, we are in June now, so I don't know… Well, people tend to take vacation during the summer, so I don't know what will be the next release and when it will be.
Oh.
I think we can…
**Tom Tan** 23:00 Summertime, we should do a release, so this, this month.
**malff** 23:04 Yeah, I think we should probably release something in June.
And then, in the summertime, most likely it will be quiet. I'm hoping it will be quiet.
And… So, but at least do a release in June, otherwise, if the next release is in September, that will be too far away.
**Tom Tan** 23:24 I think I may have some fixes for… no, not for Geneva, so… Yeah, we'll see. Yeah, maybe not affecting the Qualcomm core SDK.
**malff** 23:35 Okay.
Well, as usual, I will prepare an issue for that, and we can list all the issues or PRs which are important that needs to be part of our… Oh, yeah, sure, yeah.
**Tom Tan** 23:46 Okay, sounds good.
**malff** 23:48 Okay.
Just so you know, in general, I'm… I'm more busy than before, so I'm trying to make it to every team meeting, but sometimes I cannot, because I have some Sometimes conflicts, but One thing I wanted to check with you also… so, we have also Slack, but we typically do not use it very much.
Oh… So, do you think we can have some, discussion, say, about this, I mean, this area, or… or CI, the state of CI, or whatever, in stock sometimes.
Or should we just always discuss things in the team meeting itself?
**Tom Tan** 24:45 I think Slack is fine, it'd be more convenient than… And, meeting here, yeah.
**malff** 24:51 Okay.
**Doug Barker** 24:53 Yeah, Slack is fine.
Should we, consider reducing the number of meetings, or… because I have the last, three, I think we had limited attendance.
**malff** 25:03 Yes. I'm not sure, but I… One thing I've seen with the meeting is that, Typically, we don't prepare an agenda ahead of time, so, When people are present, we can discuss things, but otherwise… It's, It's hard to have an in-depth discussion on a specific topic, because people need to be prepared and do some research before that.
So at least we can… I think we can keep the meeting just to coordinate things, but for… for deep discussion about something, we can… we can maybe use that more.
I mean, whatever works, I'm okay.
profiling.
**Tom Tan** 25:52 Yeah, Slack works, yeah, works for me.
And that's what I think, yeah.
Slacks also, I think, hosts many other, other, I think, OpenTelemetry channels there, so…
**malff** 26:02 Well, there are plenty of channels, but at least there is a channel for maintainers.
**Tom Tan** 26:07 Yeah, okay, I see, yeah.
That's true.
**malff** 26:20 Okay, well, I don't have anything else, so, nope.
And this was a… get some… another topic to discuss, I think we can close the call.
I'll try to make it, for the next meeting, Monday, so it's Monday evening for me.
Okay. Usually Mondays are better, but, for Wednesdays, It's, I have a lot of… possibly a lot of conflicts, so it's harder for me to attend, Wednesdays.
**Tom Tan** 26:54 Okay, no problem.
I think, as Nalid mentioned, Nalid, I think, is also, you know, different time zone, maybe for a few weeks, for now.
**malff** 27:04 Okay, good to know, yeah.
**Tom Tan** 27:10 Okay, that's all from my side.
**malff** 27:12 Okay.
Well, thanks everyone for joining, Ben.
I know.
I'm… overall, just looking at all the PRs that we have, I think we have a good momentum, so I think it's, OpenTelemetry CPP… well, OpenTelemetry is great, but CPP itself is picking up. Oh, one last thing, and I forgot, I don't know if you saw the discussion on Python?
And the way that, the SDK in Python is reusing the C++ SDK underneath.
And, in particular, he's using, the YAML config file there.
So, that was… That was unexpected, but it's, the interesting part is that all the parts are reusing the C++ SDK, and OpenTeametry CPP in new ways.
**Tom Tan** 28:10 I'm not aware of that. Is that a new, or change?
**malff** 28:13 So, I pinged you on that. I think it's in the community repository.
while discussing a donation from ONECOM for Python.
**Tom Tan** 28:29 Okay.
Okay, interesting learning.
**malff** 28:40 So, that was a… A big, a big surprise for me, but a nice one.
**Doug Barker** 28:46 Yeah, it's really neat.
**malff** 28:51 Okay, that's it from Event.
Thanks, everyone, for joining, and see you soon.
**Tom Tan** 29:00 Thank you, thank you, Mark and the dog.
**malff** 29:03 By now.
**Tom Tan** 29:04 Talk to you later. Bye.
**malff** 29:06 Later.
