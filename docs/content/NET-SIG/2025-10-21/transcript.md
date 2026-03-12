SIG: .NET SIG
Date: 2025-10-21
Duration: 15 minutes
Zoom Recording URL: https://zoom.us/rec/share/ha2YFGghEzH_wol7i4LxhsPDWutujLDYdU6MzGJIEMy0oxf1GdTKfmUIcp5mihax.Bkzv2cWt_TdYQCUG
============================================================

## Zoom Recording Transcript

**Rajkumar Rangaraj** 02:22 Hello, everyone.
**Martin Costello** 02:25 Oh, rush.
**Matthew Hensley** 02:28 Hello.
**Alan West** 03:10 There you go.
**Martin Costello** 03:12 And…
**Rajkumar Rangaraj** 03:35 There are no topics for discussion. I see the agenda, there are… no one has in the agenda. Just want to check if we have any before I start, is there any topics for discussion?
**Alan West** 03:50 Nothing for me.
**Rajkumar Rangaraj** 03:52 Okay.
**Martin Costello** 03:55 No, nothing for me either.
**Rajkumar Rangaraj** 03:57 Okay. In that case, I just want to give a small update. I think everyone might have observed that. We did a, like, a better release of OpenTelemetry with .NET 10RC updates. The plan is to take that to the config repo and release the instrumentation libraries RC version from that. I think I called it out as an beta version, it's not a beta version. We released an RC version of 1.14.
So, that's the update, and Piotr is driving the release for that. So… We might… tomorrow, we might see an update in that area, you know.
**Martin Costello** 04:50 I think he left one small question somewhere on that. Like, the release process says that Something about how… Libraries that haven't yet been stable must always depend on stable ones, so I feel that it's… the doc needs tweaking to say… unless you're trying to do a pre-release.
**Rajkumar Rangaraj** 05:12 Yeah, that is exactly right, and yesterday I told him, don't do the core unstable release. The confusion is a part of the issue I created. I should have not added the core unstable in my issue, so I clarified that with Pyotr. So whatever the releases from the OpenTelemetry SDK part, we are done at this point. So, only the release pending is only in the, the contrib area. The core unstable is not something that we will release. We have to wait for the stable version of release to release, to make a core unstable, packages available.
**Martin Costello** 05:51 Right, okay.
**Rajkumar Rangaraj** 05:58 That's all I have it, and I looked at the PR or issue also. There is nothing that is… That stands up or needs a… discussion here, unless… and I know Martin has created, like, he created some PRs. I'll… I took a… I started taking a look at one of them and merged it. Remaining, I'll, go ahead and continue reviewing that.
further. We have a very strict rules on this repo, saying that, we merge a PR, and we need to go and update a branch, wait for all the build to complete, and then go review, approve, and merge it. So that's why it causes the delay.
Pyotr also speak about enabling the merge queues for our repo. Probably, we might need to consider that in order to…
**Martin Costello** 06:48 Yeah. Yeah, that would be really good, and or auto-merge, because when Renovate runs, it's a lot of time just waiting for the CI to finish, just so you can press the green button.
**Rajkumar Rangaraj** 07:02 Yeah, we need to go ahead and improve those qualities. That will… at least reduce the maintenance, or… because I get sidetracked when I review and all of this update branch happens, then I move away to some other task, and I miss out on the reviews of the remaining things. It keeps happening, so if we have something like this set up, we can go ahead and continue reviewing, And, like, concentrate on one item, like the reviewing part at a given point.
So, I don't have any other issues or anything that stands out that needs to be, like, reviewed for today.
like… If there is nothing else, that's all we have it, I think, for today.
**Alan West** 07:57 Cool, sounds good. Just one comment from my end, I… It's taken me a while to get to it, but I just opened up Steve's PR with the database summary.
stuff, so I'm gonna take a look at that, one final pass at that, and hopefully we can get that merged today.
move forward. There was some discussion last meeting about, you know, hey, when do we think we're gonna have database instrumentation?
I haven't taken kind of, like, another pass just to kind of see where we're at, but I feel like we're as… Closer than ever now.
Do you have any thoughts, Martin? Because I know that you did some stuff just to kind of, like, clean up some of the… And then Steve did some stuff, and I think we've got, like, basically documentation and maybe one other thing left?
**Martin Costello** 08:49 So, off the top of my head, the only two things I can think of is taking out the opt-out, opt-in stuff.
flags, once it's, like, got to the point of, like, right, now it's… even if it isn't the stable version, like, the code is at the point to be stable. Like, the opt-in stuff? I'm not sure exactly on that. And there's an issue assigned to me that I haven't done yet to look at what's needed to make the EF core package stable.
Because that's got a whole separate bunch of bits and pieces to check for stability on that versus SQL client.
**Alan West** 09:27 Sure, yeah.
Yeah, I think, I think we can kind of… We can think of those… the path to stability is somewhat separate to those two things.
Wow.
Still, there's a lot of overlap, for sure.
**Martin Costello** 09:46 Yeah, I think it's… it's tough.
it would be fine if SQL Client shipped stable, but EF Core didn't yet.
even though they should be… they should be on par for what they do that's the same. But yeah, there's all the extra database providers that I need to dig through the semantic conventions and check that it's doing the right thing for each of those individually.
**Alan West** 10:09 Yeah.
That's right. Oh, and… Yeah, it looks like the one last thing that I see… I'm now looking at the milestone… is the DB operation batch size attribute. I think we just need to… have an answer for whether that's something we can do anything about, or if we can't. And if we can't, then cool, I think we're pretty much good.
If we can, then it's a matter of seeing if somebody has some bandwidth to.
**Martin Costello** 10:42 Was that… is that one of the ones that's, like, optional?
**Alan West** 10:46 I… let's look at it together here, I'll just share my screen really fast.
DB operation batch size. I think I created it because it wasn't necessarily… Optional, but let's refresh our memories.
**Martin Costello** 11:05 recommended.
**Alan West** 11:07 It's recommended, yeah. So, in that case, like.
If… if it's something we can support, then we really should.
Yeah.
it's kind of a funky one, because I don't really think that, like, I don't know, maybe EFCore has other things, but, like, the SQL client thing, like, short of basically parsing the thing and, like, finding semicolons or, like, whatever… Which I don't think we want to do. Short of doing something like that, like, the, Driver itself doesn't have, like, a property of, like, you know… Here's what was… Here's the number of queries that was included in the batch.
**Martin Costello** 11:52 And just looking at the… just looking at the footnote, and it says…
**Alan West** 11:57 Operations are only considered batches when they contain two or more operations.
**Martin Costello** 12:01 So yeah, so you'd have to parse the query to know That there's more than one.
**Alan West** 12:08 Yeah, I think, I think, I think this came from, like.
the assumption, so… I want to say, in talking about this with Trask a long time ago, like, there's the Java some Java library out there.
actually had some property where you could just say, like, oh yeah, this is the size of the batch. And it was simply, like, looking at an integer versus, like, parsing the query, but I think in our case, it's like… You'd have to parse the query.
**Martin Costello** 12:42 Maybe if it's recommended, it's something that we could get away with Leaving in the backlog if it needs that much work to actually compute.
And just wait for someone to come along and go, oh, actually, I really need this.
**Alan West** 12:57 That's how I feel. Also, it's only a property on spans, So, adding attributes to spans… I'm actually making sure that my assertion is correct. Yeah, it's not a property in metrics. Adding attributes to spans is not a breaking change.
Adding attributes to a metric is a breaking change.
Since it's not on the metric.
I feel pretty okay.
With… Yeah, saying we don't support it because it would require, like, you know, parsing the thing and blah blah blah.
**Martin Costello** 13:33 Yeah, looking at the issue again, Steve said… asked me to assign it to him, so I guess if he's interested in tackling that, it could be added later.
**Alan West** 13:45 Yeah.
And I can… I'll Slack him just to see if he had any interest or bandwidth to look at it sooner than later, and if he doesn't, I'll just suggest to him that, basically what we just talked about now.
That we can do it later.
So then, with that in… with all of that in mind, merging Steve's PR, So this is your point, for, again, just talking about the SQL client instrumentation.
I think the next step would then be to… Create a release candidate.
release of it, where we remove the opt-in. That's how we handled the HTTP instrumentation back in the day. Basically, we, you know, we've been pushing out, like, beta releases.
And then we'll do the release candidate, where we remove this.
And then we'll do, like, a final release, after… afterwards.
**Martin Costello** 14:42 Right, okay.
**Alan West** 14:44 I will… Look at Steve's PR, get that merged.
I'll probably also take a pass, at the documentation, I think it's somewhat not in line with what the instrumentation now does, so…
**Martin Costello** 15:03 maybe I'll take a stab at the… at the documentation for this, kind of get that squared away, and then maybe…
**Alan West** 15:09 come… a week from now, we can… we can talk about doing that RC move.
**Martin Costello** 15:18 Okay, cool. Yeah, I am… I'm on, holiday next week, so I won't be at next week's Sydney.
**Alan West** 15:25 Okay. No worries.
Sounds like a plan.
That's all I have.
**Rajkumar Rangaraj** 15:40 I think then we will end now.
Thanks, everyone. Bye.
**Alan West** 15:44 Talk to y'all later.
**Martin Costello** 15:46 Bye.
