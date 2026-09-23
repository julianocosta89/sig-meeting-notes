SIG: .NET SDK SIG
Date: 2026-09-22
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Martin Costello (Raintank, Inc. – Grafana Labs)** 01:02 Hi.
**Navya Sharma (HealthStream)** 01:06 Hello.
Just while nobody's here, Martin, is it okay to come into this meeting to discuss one particular PR?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 01:30 Yeah, that's absolutely fine. That's kind of what this meeting's for.
**Navya Sharma (HealthStream)** 01:34 Yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 01:35 to talk about stuff.
Hi, Raj.
**Navya Sharma (HealthStream)** 01:40 Hello?
**Rajkumar Rangaraj** 01:44 Weird.
I'm gonna share my desktop, I think.
Before that, like, do we have any agenda, like, Martin, or… Navya, like, Navya seems to be a new one who's joining the… is this the first time you're joining our SIG?
**Navya Sharma (HealthStream)** 03:21 Yes. Yes, it is, hi.
**Rajkumar Rangaraj** 03:24 Yeah, do you want to give an intro about yourself, and welcome to our SIG as well.
**Navya Sharma (HealthStream)** 03:29 Oh yeah, thank you, thank you so much. New to… well, I'm not new anymore, I've been contributing… well, I've only contributed two PRs, but I'm here to talk about the Metrics SDK PR. I am a software engineer at HealthStream, currently in San Diego, California.
**Rajkumar Rangaraj** 03:49 Okay, cool.
**Navya Sharma (HealthStream)** 03:50 Yeah.
**Rajkumar Rangaraj** 03:52 We will get that covered when we are, checking the… Fear.
Martin, you have anything? I know there… I recall, like, two releases happened.
Yes, ma'am.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 04:10 Nothing in particular, so there was the 19 release I did on Friday, and then the very last PR I had as part of the release process was to update a Grafana distro, which found a buck.
**Rajkumar Rangaraj** 04:23 Okay.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 04:24 So, the change… To do with the regular expressions?
To try and avoid, backtracking.
Our test cases didn't throw enough data at it to find that there's an internal limit on how much non-backtracking the regex engine will allow, and it calls an exception.
So, had to partially revert that change.
So that was what, Monday's release was for, but because… the bug was in the SDK package.
Paid to do a new version of all the packages that depended on it as well.
And it was also.
**Rajkumar Rangaraj** 05:05 Perfect.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 05:05 Meeting zero code.
**Rajkumar Rangaraj** 05:07 Okay, what is… what should be our plan regarding keeping the 19? Do you want to unlist, or just leave both of them there?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 05:17 We could unlist it.
**Rajkumar Rangaraj** 05:21 If it is going to throw in all the cases, like, even if they onboard and they…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 05:26 It's not all cases, because…
**Rajkumar Rangaraj** 05:28 Okay.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 05:29 Like, I updated all of my personal apps, and it was fine, but if you configure enough trace sources, the regular expression that gets constructed gets long enough that it hits the limit.
**Rajkumar Rangaraj** 05:43 Okay, then I think then we are good, actually. I don't think we need to do anything.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 05:48 And on that as well, I pinged Dan Roth.
on the APNET Core team that we'd done the release, and they've updated the thing that they needed to update for the blocking Blazor issue.
**Rajkumar Rangaraj** 06:00 Yeah, I got an update as well from Daryl. He confirmed that it's working as expected.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 06:06 Okay, cool.
**Rajkumar Rangaraj** 06:09 So, I think, there's no other topic apart from the PRs. We can jump into this. I've been slow in getting into the PRs, like, last few weeks have been… I've been heads down on the different project now, so… That's why I couldn't do it, like, I'll try my best to cover the PRs now. So, Martin, I need your help, like, what we did last time, prioritize which one needs to be taken, like, the order in which it needs to be reviewed, that would help me,
**Martin Costello (Raintank, Inc. – Grafana Labs)** 06:43 So, this one.
I think… Anything that's marked review… so anything that's approved that hasn't been merged.
**Rajkumar Rangaraj** 06:52 Okay.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 06:53 So, I'd like one other person to look at it.
And otherwise, the only important PR was the bug fix that I opened on Saturday that Piotr approved yesterday. So I think, just maybe oldest first?
Because I think there's a few that have been knocking around for a few months, including, obvious.
**Rajkumar Rangaraj** 07:16 Okay, I'll try and finish off all these PRs by Friday. I don't think we plan to do any other release now, so I think I'll try to go in the order, like, the oldest first, and any things, as you said, the order, to go over it.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 07:34 So, in terms of… sorry, in terms of releases, what I was thinking is, if we wait until RC2 ships… Because there's a change for ASPNET Core, I want to test some changes in Contrip width. And then, when that's shipped, we do a new stable release without merging the .NET 11 PR, Of whatever we accumulate over the next month.
And then, once that's released, then we do an RC with the .NET 11 change, because then that gives us a couple of weeks to bake before November.
**Rajkumar Rangaraj** 08:10 Yeah, that makes sense. Yeah, that's just… that time is slightly crucial, because… We take the RC version of the .NET as well in the repo.
Yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 08:22 Yeah, that's why I was thinking we did, like, a 120 first.
**Rajkumar Rangaraj** 08:27 Yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 08:27 with the 10 SDK, and then if everything looks okay, then we merge with the 11RC2 SDK, and then we just sit on RC until November.
**Rajkumar Rangaraj** 08:39 Yep, that makes sense.
So, I've been pinged by Steve to take a look at one of his self-diagnostics PR. I'm just going to prioritize that as well.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 08:53 Oh, yes, that's… I… that's my fault. I should have used the label on other people's PRs, not just my own.
**Rajkumar Rangaraj** 09:01 Yeah, so this one, I will take a look at it. I like the idea, initial idea, of looking at by just glancing through it, but I'll take an in-depth look before commenting on that.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 09:16 Yep, sure. Yeah, I think I said to SIG… to Steve that you'd said the SIG Two or three weeks ago, that you were, like, halfway through it.
**Rajkumar Rangaraj** 09:24 Yeah.
So, at least I recall I've been on this PR, like, I started the review at least 3-4 times, and never got a time to complete it.
So, I've been, like, sidetracked so many times when… this PR is slightly big also, I believe.
That made me sidetrack many times. I'll find some dedicated time to sit on it, because it's… there is a… the reason why I need to sit on that is there is a principle we followed when doing the self-diagnostics.
We… it's based on the memory map, right? So, we don't want to restart the app or do any impact, so I want to see all those principles are still intact with this coming… with these changes of using the iLogger part.
Cool, I think, Navya asked some question about the PR, so probably, we can… Discuss about that.
**Navya Sharma (HealthStream)** 10:26 Yeah, so, I was trying to discuss about Metrics SDK, which is 7557.
And there's a couple questions I had before I went on implementing them.
Maybe you want to pull that up? Or should I pull that up?
**Rajkumar Rangaraj** 10:49 No, I'll pull it out. No, Josh.
**Navya Sharma (HealthStream)** 10:58 Okay, so, the first one was about a change in the public API.
Or… well, I guess a decision could be made on how we want to do that.
But right now, there's a getHistogramSum.
which is a shipped public API.
Which… Is non-nullable.
it's… which is not great for this PR, because we're now allowing… Negatives, for aggregation types, so… Let's say someone… says, oh, I want to use up-down counters with histograms, which means now that the sum can be negative. In which case, the sum, according to the spec, is supposed to be not recorded.
So I suggested that we should use another API endpoint called tryGetHistogramSum, which, basically, if… that histogram sum is negative, we would just send out null, and it won't be recorded.
Is that… Okay.
**Rajkumar Rangaraj** 12:20 So, I don't have a more context, I haven't reviewed this one to…
**Navya Sharma (HealthStream)** 12:24 Yeah.
**Rajkumar Rangaraj** 12:24 But I understand. Martin, do you… did you catch up on, you have reviewed it.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 12:31 So, this one, I reviewed it… To a certain extent.
when it was first opened, and then CJO had a load of comments on it, so I sort of deferred to CJO, but CJO hasn't come back to it.
**Navya Sharma (HealthStream)** 12:45 Yeah, yeah.
**Rajkumar Rangaraj** 12:48 I can do something. I can reach out to SIGO to take a re-look at it to answer some of this here. SIGO is one of the metric experts who wrote, the… most of the things also here, or, like, reviewed most of this.
So, we will pull him into it to check if he feels or what is needed. I… whatever the issue you explained, I also remember running into that, like, in an updo encounter, it's going negative and all that.
In the… in one of the scenarios. So, looks like, the PR may be doing the right thing, but let me check with Sijo on, what, what his thoughts are on.
**Navya Sharma (HealthStream)** 13:37 Yeah, that's completely fine. Maybe it's, I think I should just wait, then, on his review.
**Rajkumar Rangaraj** 13:44 I'll reach him out today. I crossed Joe in office today. While walking back after this meeting, I'll just give him an… ask him to take a look.
**Navya Sharma (HealthStream)** 13:52 Thank you so much.
Most of my questions are already on, like, this top comment, so he should…
**Rajkumar Rangaraj** 14:05 Nope.
**Navya Sharma (HealthStream)** 14:06 Be able to take a look at that.
**Rajkumar Rangaraj** 14:08 In case Resido is busy, this week, I'm planning to cover up all the PR, so I'll take a look at it, or even other maintenance also can look into it.
**Navya Sharma (HealthStream)** 14:19 Got a kiss.
**Rajkumar Rangaraj** 14:20 It'd be okay.
**Navya Sharma (HealthStream)** 14:21 I'll try and join next week as well, so that we can maybe discuss it on call instead of on Commons.
**Rajkumar Rangaraj** 14:29 Sure, definitely.
Yeah, but we will, only if we review, we will, no, like,
**Navya Sharma (HealthStream)** 14:40 Yep, good.
**Rajkumar Rangaraj** 14:41 What's your proposal and everything, yeah.
**Navya Sharma (HealthStream)** 14:43 Yeah.
**Rajkumar Rangaraj** 14:45 Yeah. Thanks, Navya. Yep.
Martin, back to you, like, is there anything, not very active in the contrary by as well? So, I think,
**Martin Costello (Raintank, Inc. – Grafana Labs)** 14:59 So I think the… there's two that are quite old.
that would be… I'll put labels on them in a minute, is, does the… There's the Elasticsearch one.
Yeah. Because I think that was discussed when I couldn't make it the other week. It's like, I don't think anything particularly Elasticsearch-esque is happening in that PR, it's just updating the semantic conventions.
But if no one wants to review it, then we should consider just completely deprecating the component, because it's… the PR's been open for 3 months now, so if no one's ever going to look at PRs for the Elasticsearch component.
Then it doesn't make any sense to invest any effort in it whatsoever, and we should just deprecate it.
**Rajkumar Rangaraj** 15:45 I also strongly believe, I also brought this topic earlier also, Martin, like, a lot of the component in this one does not have a component owners. So, probably, like, we… I bought a topic, I don't know whether you were there in that meeting, Alan was there.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 16:01 I wasn't there that week. I watched the recording.
**Rajkumar Rangaraj** 16:04 Yeah, so probably we should come up with a process to… we cannot just immediately go and duplicate as a maintainer, like, we should…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 16:12 Because I did… I did… I did try and… gently persuade.
Well, I put a comment on an issue about deprecating it. It said something like.
**Rajkumar Rangaraj** 16:24 No games.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 16:25 Two months now, maybe we should deprecate it, because no one's reviewing anything, thinking that maybe the code owner would maybe see that and have an opinion, but they didn't.
So, we've already suggested it over a month ago that we deprecate it, and no one said anything. And usually what happens is the second you try and delete it, then they go, oh, no, no, I do care about it. But, it's been 3 months.
**Rajkumar Rangaraj** 16:49 Okay, so this is what I recommend in that case, Martin. In case if you have bandwidth, if you think through the process, how we can start the deprecation process of the component, and we write up somewhere as a process in this contribo, it would be helpful for us.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 17:09 Okay have a think about that, because, yeah, it's like, I didn't think it was a particularly controversial PR.
**Rajkumar Rangaraj** 17:18 He…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 17:18 We'd need the code owner specifically to look at, and it's been, like, open for 3 months.
**Rajkumar Rangaraj** 17:24 Yeah, they should not… there should not be a blame saying, we have tried this in the past, and a lot of complaints has come up. We abruptly went and trying to protect the component off.
So, like, at that point itself, they asked us to devise a process, and that never got materialized. I think now it's the time, I think.
I think, like, someone comes and adds a beta, for example, Service Fabric one as well, right? Someone came, forced us to add a beta version as well. They did not take effort to move it further at all. So, it's just the initial code that's sitting in there. So, these are the examples where we need to notify, and if there is no progress, we are going to remove those codes.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 18:08 I've assigned the issue to myself, but it looks like the issue to deprecate the Elasticsearch repo was first created a year ago.
**Rajkumar Rangaraj** 18:17 Yeah.
Well, that… then in that case, we should… probably we should do that.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 18:23 activism.
**Rajkumar Rangaraj** 18:23 For a year, we should start the deprecation on that.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 18:25 Because we only.
**Rajkumar Rangaraj** 18:26 but good again.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 18:26 Piotta opened it a year ago, and then two weeks went by, and the code owner said, oh, it'd be really breaking to not support this anymore. And then nothing… and then nothing happened since they're not reviewing PRs either.
**Rajkumar Rangaraj** 18:43 Then we should deprecate it, Martin. I think it's there for a year. Makes no sense to wait on that specific component, but for the remaining components, we can devise the process and leave it.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 18:54 Yeah, because I think it was… oh, I've forgotten what it was now. We had an exporter, and it had loads of security issues in it, and we reached… and Piotr… tried to reach out to the company that the person who wrote it worked for, and they didn't work there anymore, and they contacted the security Email address for them, and they basically said they didn't care, so we just immediately delisted it.
I can't remember what it was for, but it was an exporter.
But yeah, we, yeah, I agree, we should have a documented process.
**Rajkumar Rangaraj** 19:32 Yep.
I think that's all for today. I don't think we have anything else to discuss.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 19:43 Oh, the, sorry, the other one I mentioned that's waiting for some reviews is the number 4986?
It's… it's in the bottom section.
It says waiting on authors, but, Steve had some feedback, but I've replied to him Matt's approved it, but Matt's approvals don't currently count for Merge, so… It'd be good to get someone else to look at that.
**Rajkumar Rangaraj** 20:17 Yeah, I don't think… don't wait for me, Martin, on that.
Like, Matt's… that PR, which I created. Let's wait for one more day to see if Alan takes a look at it, then merge it, and then we will provide him the permissions needed.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 20:36 Okay, that's fine. Yeah, it's just, yeah, because it's just, as it stands, I still can't merge this one.
Even though two different people have looked at it.
**Rajkumar Rangaraj** 20:44 And also, there is another conversation came up, that, like, also, pre-order brought that, topic, getting Steve also to an approver, so you just check with him, if he's interested in, if, if yes, we can even think about, adding him also as an approver.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 21:07 Yeah, yeah, that'd be good, because, yeah, we're, Lots of people are always busy at the moment.
**Rajkumar Rangaraj** 21:14 Yeah.
So, to be honest, like, at some point in time, I was thinking about, I should step down as a maintainer from all the three .NET repos.
I'm not doing the things that are described in the maintainer process. So, let me… I need… that's a discussion I need to have, because right now.
me removing myself will create an issue there, so I just need to see how… what needs to be done. I just need to take a consult from Traska as well on that.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 21:48 You've been fully sucked into the Rust ecosystem now, have you?
**Rajkumar Rangaraj** 21:52 Yeah, I just want to move from the maintainer to approver, if possible, because I'm just driving this SIG and all, but if you ask me, if I go back and check it on my… reflect myself, I may not be doing the things that is completely needed for the maintenance.
So, planning to step back from the maintainer and then be as an approver, but thinking about that, but I haven't decided yet on that part.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 22:19 Okay, well, I'd support you continuing, Ryan.
**Rajkumar Rangaraj** 22:23 Yeah.
Yeah, let's see, like, how it goes. Hopefully, no, I'm not going to change anything abruptly now, but we slowly… even if I need to do, I will have a slowly ramped-down path created, not leaving abrupt.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 22:40 Sure. Yeah, I just say, you shouldn't feel guilty.
**Rajkumar Rangaraj** 22:43 Sure, yeah, thanks for that.
Yeah, I think we have pretty much everything covered.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 22:56 Yeah, I think, yeah, I think we're good for today.
**Rajkumar Rangaraj** 22:59 Okay, cool then. Catch you up next week. See you. Bye.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 23:02 See, Rush, bye.
