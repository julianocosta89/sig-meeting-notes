SIG: .NET SDK SIG
Date: 2026-09-08
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Matthew Hensley** 00:29 Hello.
**Rajkumar Rangaraj** 00:32 Imagine.
**Matthew Hensley** 00:36 The… Martin is not gonna be joining today, he's not feeling well.
**Rajkumar Rangaraj** 00:40 Yeah, he just dropped a note saying that he is sick. I hope he recovers soon.
Let's wait for one or two minutes to see, if anyone joins. We will try.
Efficient.
I think it's going to be a short one, we don't have any agenda.
Been added in there.
**Matthew Hensley** 01:07 Sounds good.
**Rajkumar Rangaraj** 02:27 We will get it started.
So, there are no… do you have any topics, I think I see Alan also has joined. Yeah, but do you have any topic?
**Alan** 02:55 Hey, friends.
**Rajkumar Rangaraj** 02:58 Helena.
**Alan** 02:59 None for me.
**Rajkumar Rangaraj** 03:01 Okay.
So, let me get started. I don't think there's anything in the agenda. As I said, Alan, I was telling Matthew as well, like, it's going to be a short meeting, we don't have any topic or anything. Yeah, and also, we did that, after 1.18 release, we did not do any major merger or anything at this point.
The only change that has happened, if we need to call out, there is some bug we fixed related to that, Blazor single thread, based on the .NET ask. Martin itself did that PR.
The .NET team has followed up with me, asking when is the release. I said, nothing planned in, like, a couple of weeks, so they are fine to wait, on it. I said if needed, we can do release a patch.
But they are fine waiting for it. That's the one… Update from my side on that part.
Apart from that, if we look at it, there are a lot of, And let me go to the, PRs. There are a lot of PRs, new PRs that got created in the past week. I did not get a chance last week to take a look into it.
So I'll spend some time this week to go over the PR and unblock things over here.
So, there's nothing much… Apart from it, the… I think the, contrab is well under control, it's very actively being… like, both Pyotr and Martin keeps it up to date, and I think these things have some questions that has been left, that's why it's been waiting. Apart from that.
Don't think… There's anything that is… Very important that's waiting over here. I did glance on this one as well, so nothing major.
On… on this one.
Let's go back to the issues and see… Well, no new issues as well.
So here also the… it's all the recent, PRs, That needs any… Study, considering it's a, like, a… U.S. holiday, I think it's slightly pinning here. If not, I think it should also come down.
So, as I called out, there is nothing that needs to stand out apart from the PR reviews that need to happen in the repo, so I'm planning to help out there this week.
Hmm.
I think that's all I have, nothing much. Like, any of you want to share anything, yeah?
**Matthew Hensley** 05:54 I have 2 items, I can put it in the dock, or one here.
So, well… Sorry about that. Looks like it… Picked up some weird formatting things there.
Let's hit that.
**Rajkumar Rangaraj** 06:10 Okay, here, placing it here, okay.
**Matthew Hensley** 06:13 Yeah, it's going to… I'll just put it here in the chat, and I'll fix the formatting after the fact. Sure. It's picked up the thing. There's this elastic… SDK stuff, that it's like, there's been a… maybe we should deprecate it for… almost a year now, but there's been some PRs open for a while, can see it was… A few weeks ago, that it was even… noted that it had been almost 2 months, so we're over 2 months now without any feedback, and… Feels like some of the other things in Contrib are heading this way.
Where there's code owners assigned, but we're not seeing much traction on, like, reviews or anything.
This one in particular was just because it had already been flagged last year.
So, something to consider how we want to handle that policy, because I know we've had to do that with AWS before.
**Rajkumar Rangaraj** 07:08 Yeah, I think it's, every time and now this conversation comes up. And then, do you remember, like, earlier, did we devise any… Plan, because we just don't want to… I still recall if some component does not have an owners, apart from the repo maintainers. We had a plan to do a notice, and then go ahead and do the… follow the deprecation plan.
I remember, I don't know whether we followed any of the steps in that.
**Alan** 07:45 Yeah, up to this point, I don't think that we've ever… I mean, I can't recall what we actually wrote down in our… guidelines.
But I… I do know that I don't think we've ever gone through The actual process of… of deprecating.
anything. So, if we were to do that, it would be the first time.
**Rajkumar Rangaraj** 08:11 Maybe we will summon all the maintainers next week to join, if possible, and we can come up with a process. Earlier, I think this process was discussed. I was a maintainer at that point in time.
So we could follow something that, instead of giving an immediate shock, saying that, hey, I'm going to deprecate tomorrow.
at least some time for the, create an issue and leave it in the repo and then follow the process for the components. Maybe we should not do it for… only for the elastic fretch. I would say for whichever the component that does not have an owner, we will create the issue.
For all of them, and start the process of deprecating. So it reduces the maintenance overhead, because here, Martin is the one who is driving the maintenance overhead for these components.
**Alan** 09:02 Yeah, we should probably talk about it. I mean, yeah, your ideas of, like, adding an issue and all that, a notice is good. If there's anything we could actually do in the distribution… The binary itself would be cool, like, if… We were to somehow make it… like, if we were to release a new version, and, like, everything was obsolete, you know, making it in people's face that this thing is going away.
Might be another idea that might be useful.
**Rajkumar Rangaraj** 09:31 Yeah, probably we should brainstorm in the next week with all the maintenance, and come with an agreeable plan, and… take it forward. That's much needed at this point, I believe.
With the noise it's getting… it's creating in that space.
**Alan** 09:48 Yeah.
And then, you know, I don't know. It'll probably also be… we'd probably also want to, like, consider kind of case-by-case type of things. Like, maybe there's some instrumentation that's really important, even though we don't currently have an owner.
maybe we should try to find one, or something, like, I don't know. If you go back to the issue.
with respect to this one, I actually think I saw the original conoder If you scroll down just a little bit, how long ago was it?
EJ Smith, I think, is marked as the code owner of this instrumentation.
So he was active as of October last year, so it's been… Almost a year.
And… if I'm understanding him right, he's basically saying, like, this new version… what's he referring to? This new version of, what, Elastic Client?
was massive and breaking, so… Yeah. Is he making the claim that, like, this instrumentation is still relevant?
**Rajkumar Rangaraj** 10:58 Yeah.
**Alan** 11:00 Yeah.
**Rajkumar Rangaraj** 11:01 So, unless, like, we know from some customer or from the owner itself, we don't know the usage or how it's being utilized in here.
B-U- And you or Matthew, you… have you ever seen this being used by the customers, and
**Matthew Hensley** 11:21 Yeah, I have. It's not super common, and I only brought this up as a really easy example. It's like not to call out the code owners here, just more… It's a… Relevant and timely one of how do we want to handle these situations in general.
Because, obviously, our AI tooling is meaning that we're getting lots of PRs against Components that are not necessarily being actively maintained.
And how do we want to handle that?
**Rajkumar Rangaraj** 11:58 Well, I'll bring this up in the next video, and thanks for bringing it… Yeah, you said two things. One is this one, and is there any other thing, or…
**Matthew Hensley** 12:07 Yeah, it's more a governance thing. I was just curious. I've been doing this for a while.
Hmm… Wondered what… Kind of standards we have for getting to, like, approver status.
I've been opening up lots of PRs, especially recently… Oh, yeah, yeah.
**Rajkumar Rangaraj** 12:27 Thanks for asking. Today, even before you're speaking, I thought I'll go to the maintenance and speak about that, your approval status. I think you have reached the consensus, so I am supportive. Alan, Matthew, I've been contributing a lot to both the repos.
both the contrary band, the SDK reports, and I feel like the time to promote them as an approver, now, If we want, we can take an offline conversation and check with all other maintenance and.
**Alan** 13:03 Sure, yeah, no, I'm… I'm 100% supportive, too. Yeah, Matthew, sorry, you know me, like, I haven't… I haven't been as active, like, paying attention to… kind of like the movement of these… of these projects, so forgive me, I guess, for… for not being on top of that type of thing, but Absolutely. Supportive. So… I think we should just make it happen.
**Rajkumar Rangaraj** 13:29 Sure, cool. I think I'll get that rolling.
And you called it out at the right time, when you were brought up about this topic. In the back of my mind, I was thinking that you should be with the kind of The question you bring it up, that itself shows the kind of commitment you have towards this repo.
**Matthew Hensley** 13:52 Yeah, I've been trying to spend a lot more time here. I've, Now that Martin and myself had dealt with all the things we needed to internally, I've been able to spend a lot more time upstream.
than I have in a bit, so…
**Rajkumar Rangaraj** 14:05 Cool.
**Matthew Hensley** 14:05 That's gonna continue, so…
**Rajkumar Rangaraj** 14:07 Yeah, thank you.
**Alan** 14:09 Great.
**Rajkumar Rangaraj** 14:12 So, I think that's all we have for… Today, I think we could end now.
**Alan** 14:21 Okay, thanks, y'all.
**Rajkumar Rangaraj** 14:23 Thank you.
**Alan** 14:24 Yeah, next week?
