SIG: .NET Auto-Instr SIG
Date: 2026-01-21
Duration: 29 minutes
============================================================

## Zoom Recording Transcript

**Mateusz Łach** 01:15 Hello.
**efshaikh** 01:21 A… To see you again.
**Alexey Pukhov** 01:25 Alright, long time now seeing.
**efshaikh** 01:58 Matthews, is it possible for me to download the end-to-end test binary's artifacts?
Because I'm seeing that the test is failing because the continuous profiling is not enabled on .NET, at least on the end-to-end test machinery on GitHub.
**Mateusz Łach** 02:21 Yeah, I think so. Let's… let's discuss it on.
**efshaikh** 02:24 Because, yeah, no.
**Mateusz Łach** 02:25 Nope.
**Zach Montoya** 03:35 Hey, everyone.
**Yevhenii Solomchenko** 03:40 Okay?
**Mateusz Łach** 03:42 Hello?
**Alexey Pukhov** 03:43 Bye.
**Zach Montoya** 03:54 Couple minutes passed, so… Suppose we can get started.
Does anybody else want to drive?
**Mateusz Łach** 04:06 I can… I can drive, give me a second.
**Zach Montoya** 04:08 Okay. Thank you.
**Mateusz Łach** 04:21 Okay.
Yeah, so… I'm not sure if Pilgris is going to join today, he has some… Other… other stuff to take care of, so that's… as you said, it's… 5… Past 6, so I think we can start. So… Let's start with the PRs. So PR released, release the new versions of the packages, of the core packages in the SDK and CodeTrip repositories, and updated, basically created a PR with updates, on… In, .eng instrumentation Repository as well, so if you could take take a look, that'd be very helpful. I think, aww.
The idea was to, to release, later this week, the new version of Auto Instrumentation, if Sieg is okay with… okay with that, I'm not sure if this was discussed last week.
Aw.
But… Yeah, so… So that's the first one, then we have, Then we have draft, so, if any, anything you'd like to discuss at this, At this time, or… Igor just wrote a…
**Yevhenii Solomchenko** 05:55 Comment for that?
For not implementing… That in the file base.
**Mateusz Łach** 06:04 Okay.
**Igor Kiselev** 06:14 It really feels for me that it's more a property of how our .NET agent distributed, because it would be… it should be true always when we distribute it as a zipper hype, and it should be always false for distributing it as a NuGet.
In most cases, when it is distributed as a NuGet package, because in first case, we resolve complete dependence ourselves. In second case, we… NuGet already have Done, calculate the resolution.
If we would go with Alexia's approach for conflict solution in .NET, it would be even more critical, because, system diagnostic, diagnostic source most probably would be loaded before, our assembly, as our assembly depends on it, so… I don't think it would work. At the same time, I understand that Having it as just an environment variable may be ugly, so maybe it would be better to invest in inventing some mechanics to auto-detect default value.
and still have an environment variable or config-based approach. I don't know yet how to implement that config-based approach, only as a fallback solution if customer would like to override what we default detected for them. And by the way, it already works that way, because that property detected from our CMD, SSH, file the… There is a true file, so it already feels most… mostly as internal, unless the customer, need to configure, because he don't want to use our startup script.
**Mateusz Łach** 08:09 Okay, any, like, comments to what Igor said, or…
**Zach Montoya** 08:22 I guess, what's the… The next step on this… are you still iterating on the draft, or do you require input to proceed?
**Yevhenii Solomchenko** 08:34 I would keep it in the draft for… a few days.
Discussion, music, or maybe?
**Zach Montoya** 08:43 Okay.
**Mateusz Łach** 08:44 Okay.
Okay, then do we have GitHub attestations for this artifact, so I… it seems like Rasmus already… Had the chance to look into this one.
Is this something that may be well discussed?
On a previous meeting?
**Zach Montoya** 09:15 No, we didn't discuss this. This is the first time seeing something like this, but I can take a look at the related pull request to get an understanding.
**Mateusz Łach** 09:24 Okay.
That'd be helpful, thank you. Yeah, it seems like this is following the steps from the other repositories, right? SDK and Contrip.
**Zach Montoya** 09:34 Yeah, it looks like it, so… I don't know.
Oh, I'm sorry. Raja, I don't know if you, had looked at the related pull requests, but if not, I can just look into the linked ones to get a better understanding. I'm sure it's fine, but if there's any issues, of course I'll… comment on.
**Mateusz Łach** 09:52 Okay.
Okay, so moving on, we have semantic con… update, semantic conventions, so this is for MongoDB bytecode instrumentation, right? So, again, it seems like you've already had a chance to review it.
**Yevhenii Solomchenko** 10:10 Nuh- For licensing code, it's already good.
Manage.
**Mateusz Łach** 10:14 Okay, and what about the comment? This is something that should be implemented before merging?
**Yevhenii Solomchenko** 10:19 She already refactor that. It's about 1V… Goodbye.
**Mateusz Łach** 10:24 Okay, oh, okay, I see, sorry, I missed that. So it's already, like… okay, yeah, so, yeah, so we'll try to… Try to schedule some time to review it, and it seems like it's ready to be reviewed, and Oh.
Yeah, obviously we merged.
Then we have, the PR from Alexier.
So this is in draft for now. Alexi, anything you'd like to discuss at this time?
**Alexey Pukhov** 11:02 Well, yeah, it's kind of a draft, but if you can start looking at this, I would really appreciate any early feedback, because the change is big.
Okay. But the profiler-based solution is there. I'm just fighting a little bit with the build infrastructure. There is still a… because it's a learning curve for me.
I have a problem with understanding the dependencies, like, the idea behind what should be included and what should not be included in the tracer home output.
So this is kind of a last thing for the profiler… last big thing for the profiler-based solution to make it complete.
But the solution itself is there, so if you have any, feedback, I would really appreciate that. The next step for me for this will be, to extend the solution for the… non-profile… non-native profiler deployment when you just use startup hook, because that will require a special a special thought. I mean, we don't have native profiler, we don't have, native redirection, so we have to fix… to do something else there.
But yeah, if a community have time, please take a look.
And for, for convenience, I posted a commit that shows the essence of the profiler… of the native profiler-based solution. It's in the description.
Because the change is because of the renaming and the removal of the additional dependencies projects. But if you just want to understand the essence of the idea, it's… you can just look at the first commit. It's… if you scroll a little up.
It's under the word section.
Or you just go to the first commit, really.
**Mateusz Łach** 13:06 Okay, but it is under the what section? Okay.
**Alexey Pukhov** 13:08 Yeah, it's the word section, native profiler-based deployment, and then there is a link to this commit.
**Mateusz Łach** 13:17 Okay.
**Alexey Pukhov** 13:20 It's essentially the first cook.
**Mateusz Łach** 13:26 Yeah, okay, so if, so basically this is in draft, but ready for, early feedback, so if, If anyone have, has, has a chance to…
**Alexey Pukhov** 13:38 to review it and provide some feedback, that'd be… If you have time, yeah.
**Mateusz Łach** 13:41 useful, right?
**Alexey Pukhov** 13:43 If you… yeah, absolutely, like, something to test, because every change that I'm doing, I'm testing locally with the… with my test application, but I mean, any, really, feedback.
would be appreciated. Like, things that I should look at, things that I should test eventually at the end.
Anything.
**Mateusz Łach** 14:11 Okay, thank you, Alexi.
**Alexey Pukhov** 14:13 Sure, thank you.
**Mateusz Łach** 14:16 Okay, then we have… There's one for producing symbols… Seems like, again, Rasmus was… Started looking into that.
Fortunately, Martin is… Not here today.
Okay… Yeah.
**Zach Montoya** 15:19 Yeah, those look like some pretty big changes in terms of size, I think, right?
**Mateusz Łach** 15:24 Yeah, that's true.
**Zach Montoya** 15:25 Where else must, suggestion?
Is it a good one that maybe we can just, separate them out?
**Mateusz Łach** 15:39 Yeah, I agree.
Not sure if, zach, Do you want to, like, add a comment here, or should I add it… Yeah, yeah, okay.
Thank you.
Yeah, and then in a similar vein, there is another… Another one from Martin, so… Okay, so it seems like Aftika is, already helping here…
**efshaikh** 16:33 Yeah, I did provide my comments. The stack thing may not be compatible, or it is not compatible with current linkage.
**Mateusz Łach** 16:45 Okay… So, FDCar, any… and I think you, You think should be added here, so… Oh.
**efshaikh** 17:20 No, as of now, with the current linkage, it is not possible to have that save stack. It is ineffective, basically.
**Mateusz Łach** 17:27 Okay.
**efshaikh** 17:30 So where is this requirement coming from? Is that a compliance thing?
**Mateusz Łach** 17:34 I don't think this is, like… Huh.
I think it's probably something that I assume Martin noticed.
**efshaikh** 17:45 Okay, because… Messing with linkage would be non-trivial. Making it dynamic opens its own problems, as Igor would testify.
**Mateusz Łach** 17:56 Yeah.
**efshaikh** 17:58 If it is not a hard requirement, let's not create that. Let's not open that can of worms.
**Mateusz Łach** 18:06 Yeah.
**Chris Ventura** 18:11 I think… worth commenting about that on the PR, just so that we can remember it.
**efshaikh** 18:19 I will… I will do that, certainly.
**Mateusz Łach** 18:23 Okay, but it seems like you added your comment, FD car, so… Oh… So, in your opinion, what would be, like, the… what would be, like, the final shape of this PR?
**efshaikh** 18:40 So, we will have to, if we insist on having that, then we will have to change the linkage to dynamic, and then have.
**Mateusz Łach** 18:47 Yeah, that's true.
**efshaikh** 18:47 step.
**Mateusz Łach** 18:48 Yeah, but as you said, this is, like, non-trivial change, so what would be, like, if we don't want to change the linking, so what would be the contribution from this PR?
**efshaikh** 18:58 It would probably add some comments, annotate that area, the make files, saying that we did attempt to introduce this flag, but currently it is incompatible with the existing linkages.
So that'll be with Trey last it was investigated on.
**Mateusz Łach** 19:16 Yeah, so it seems like there is still some work to be done in this PR, right?
I mean, to be.
**efshaikh** 19:21 Yeah, I suggested… Yep.
that they leave comment on that, so I will follow up on that, and I will post a comment.
So that… It can be closed.
**Mateusz Łach** 19:34 Okay.
Okay, thank you.
**efshaikh** 19:38 Yeah, no problem.
**Mateusz Łach** 19:40 Oh… And we have a draft PR from Igor. Igor, anything you'd like to discuss?
**Igor Kiselev** 19:48 Oh…
**Mateusz Łach** 19:48 Related to this one.
**Igor Kiselev** 19:51 So, I still have not enough time to continue to work on it. Zpr currently in a stage that Everything mostly implemented, except of, of some unit tests.
So, some unit tests, and so it's ready for early review.
At the same time, there is no hurry to do it right now.
**Mateusz Łach** 20:17 Okay.
**Igor Kiselev** 20:24 It really address mostly edge cases, so… It's not very critical.
**Mateusz Łach** 20:32 Okay, then we have some documentation, PR, which is… it seems to be already approved.
Right, so… Yeah, okay, so this is… this was waiting for the releases that happened today, so… Yeah, I think this should be… Good to merge.
I'll follow up with Pietro.
On this one. And then we have, two additional drafts.
First one is… Okay, so Teswanis… Blocked.
Why some open issue.
And this one… Okay… So… This will stay in draft for now, I think, as well.
So that's all for the… PRs… What about… So, what about the issues?
Which have no milestone.
So, this one is about, semantic conventions update, so we have PR for this one already, so… -Oh.
Is this something that we want to target for the release that we plan later this week, or… I think it seems like, can you say that this is, almost… Almost ready, right?
**Yevhenii Solomchenko** 22:30 Yeah, it's almost ready.
**Mateusz Łach** 22:33 So it looks like it's waiting for the… For the additional reviews, so, yeah.
Are you fine with setting the milestone for the… to the, like, next release?
For this one, it seems like it's… It's mostly about updating to semantic conventions, so… And the PR is, like, ready.
Okay.
Set it to next release, then we have some… something to… In… Approved test coverage… Okay, so it seems like nothing new, right? So it's like.
**Yevhenii Solomchenko** 23:29 It's also new, but also old stuff.
Could be, be next.
One of her time.
Megan.
**Mateusz Łach** 23:36 Okay, maybe the next, or the next release, like, 1.15.
**Yevhenii Solomchenko** 23:42 Maybe…
**Mateusz Łach** 23:42 Cool.
**Yevhenii Solomchenko** 23:43 I'm not sure about timing or that.
**Mateusz Łach** 23:46 Okay, I'll set to UV next.
In that case, then we have variable… environment variable conflict, but this is something that you really investigated, it seems like… Okay, there was no update last week, so… Seems this belongs in another repository, right?
**Yevhenii Solomchenko** 24:07 Yes.
**Mateusz Łach** 24:10 Okay, so there, like, there is no activity here, should I… Market stay, or, like… Closed it already.
Okay, fiat market stayed last week, so…
**Chris Ventura** 24:27 Yeah, let's just close it.
**Mateusz Łach** 24:29 Yeah.
Db common bytecode instrumentation, this one is new.
**Zach Montoya** 25:03 Did this get reopen? Oh, it's quite old.
**Chris Ventura** 25:05 No, it's an old ticket that we've been considering, but there was a… Question regarding it, because there's a desire to attempt to do it again.
**Zach Montoya** 25:18 Oh, okay, I see.
I see. Okay.
Yeah, I mean, I'm sure we can add some logic, like, if we hit multiple… multiple spans, or multiple instrumentations run of, like, checking what the existing span is, just so we don't… Like, we might hit multiple instrumentations, but only… Generate, one, like, activity.
Heh, yeah.
Would need to… need some experimentation.
Probably easier to use with SQL Client.
**Mateusz Łach** 26:08 Okay, so I think… so Piotr's ask was to, to add 115 target to it, I think this is something that he'll probably… I'll start looking into, you know, Next few weeks, so… Yeah. Are you okay with adding the 115 milestone to this one?
**Zach Montoya** 26:31 Yeah, sounds good to me.
**Mateusz Łach** 26:32 Okay.
Yeah, so these are all… That were missing, milestone, I… Don't think we have any discussions.
So… There is nothing that has milestone, but is not assigned to the project.
Okay, this one.
So… Yeah.
Let me assign it to the board.
And… Then we have a project board review.
Anything that… That needs to be updated here.
Yeah, so…
**Zach Montoya** 27:32 You can just move the semantic convention one to in progress. Maybe you need a refresh, but… It's probably the only change we need to make to this.
**Mateusz Łach** 27:40 Yeah, I will… I will also take a look, because the flaky test is assigned to this milestone, so I'll take a look there. And, yeah, so for the release, I… As I said, I, I think Pyot was, is working towards that, and the plan was to… to release later this week, if this is, like, fine with the 6, so probably, like, tomorrow or Friday.
**Zach Montoya** 28:12 Sure, I'm… yeah, I'm not aware of any blockers or… Anything else we're waiting on?
**Mateusz Łach** 28:18 Okay.
So it's… I think this is all from our standard agenda, so anything else we'd like to discuss?
Okay, so in that case, thank you all for attending, and see you next week.
**Zach Montoya** 28:45 Alright, thank you.
**Alexey Pukhov** 28:47 Thank you. Bye.
**Yevhenii Solomchenko** 28:48 Ryan?
