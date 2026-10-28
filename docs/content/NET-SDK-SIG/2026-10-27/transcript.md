SIG: .NET SDK SIG
Date: 2026-10-27
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Martin Costello (Raintank, Inc. – Grafana Labs)** 03:54 8.
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 03:56 Hello!
Sorry to be a little late, having trouble with the LFX sign-in.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 04:03 No worries. I was wondering if maybe… Either everyone else or me was having time zone issues.
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 04:14 Yeah, that's… Not sure what was going on there, I had to log in, like, 3 or 4 times before I'd actually do it, so… anyway.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 04:23 Weird.
Yeah, because, our clocks changed this weekend. So, it's the one week of the year where the meeting is, like, at 6pm for me.
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 04:34 Yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 04:36 Hey, Raj.
**Rajkumar Rangaraj** 04:39 Hey, madame. Hello, Matthew.
Sorry, I had a challenge studying the Zoom and joining itself.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 04:52 I think Matt had the same problem.
You know, the practice.
Women?
I just put a few… a couple of things on the agenda. Is there anything anyone else wanted to add?
**Rajkumar Rangaraj** 05:40 I think it's good to start with.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 05:43 Okay, cool. I can't remember what first item, I can't remember what I was doing, but I was doing something last week.
And then I realized there was an issue I'd opened a while ago about putting something in about the support statement.
So, I've opened a PR, and it's just a copy… I remember now. I was reading something in the Security SIG, and there was a support statement in it that said, we only support the latest miner.
So I've copy-pasted it, and then linked to it.
in our README, so I know Matt's already looked at this, but if there's an agreement that this is fine, then we can just merge this, and it will hopefully contribute to closing off the issue, which was people asking for us to support multiple minor versions for patches.
**Rajkumar Rangaraj** 06:34 Yeah, that looks good to me. I just went ahead and uploaded.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 06:39 Okay, cool. I'll match that in a bit.
I've moved the .NET 11 PR in the main repo It's ready for renew… excuse me, ready for review now.
It's quite dark.
**Rajkumar Rangaraj** 06:55 So, old beer, if I understand correctly, right? Like, the very old one is… That sits at the end of the PR list, is that the one?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 07:05 Yep, it's that one. Yep, that one's now…
**Rajkumar Rangaraj** 07:07 Yeah, okay.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 07:09 up for review. It's quite big, but… The majority of it.
is either C-sharp 15-only features, or it's mechanical changing numbers and updating hash defines.
And things like that. The only new feature that's in there is… it's in the list… let me… let me open the PR, that'll probably help.
The only new feature is… The support for this new interface.
Which lets you configure, activity sources from config.
But otherwise, it's all just version number changes, pretty much.
There's quite a few files changed, but… Should be relatively light in terms of actual content.
**Rajkumar Rangaraj** 08:06 I think this is a reasonable stuff with… I mean, I've seen, historically the… adding the support for a .NET level, it's always, like, touch as many files. So this is fine, we can take a look at it, and it has been tested thoroughly by version by version, so I don't think we should be worried too much. We can take a look at it.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 08:25 Yep, sure. Yeah, my plan is, once it's got enough approvals, to do… to merge it and then do a 1-21 release, RC1, And then we can have that released for a couple of weeks. I'll check it in some of my own applications.
And then, if everything's good, it should just be a minor PR next month to bump it to RTM.
**Rajkumar Rangaraj** 08:53 So, for the time being, right, if any other security issues comes, right, so how do you plan to tackle that?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 09:02 We'll have to go with the branch, because there's already changes merged that are a minor patch bump, a minor bump anyway.
So, if we were to get anything important enough to do a security release, I think even without merging this, we're already at the point where we'd have to revert a load of stuff, or we'd need to branch.
**Rajkumar Rangaraj** 09:27 Yeah, maybe if we are ready earlier, we were using… I don't think we still follow that. We had earlier two branches, and we used to do that. And I think it's… we can do it the other way. This time, if something comes up from the last tag release, we can take and apply the patch and release it if need be. That's what I'm thinking, instead of touching any main branch on it.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 09:46 Hmm, yeah. Yeah, I think, all of the… Anthropic scan results now have either got a PR open or they're already merged.
And all of the ones that were security relevant, even if we didn't want to do, like, a full CVE for them, they all got shipped in the 121 patch release already.
So yeah, so then, update on the Anthropics kind of stuff. So, they launched the ability in the last day or so, to report the issues as GitHub security advisories.
So, I've got a PR open to switch over for that.
Primarily just because it gives us individual issues to track.
Rather than just an email with a bunch of text in it.
If it doesn't work a lot of time, we can always switch back to email.
But even if they're not security-related, we can just close them and copy them into a normal issue to work on.
It just makes it easier to track things.
**Rajkumar Rangaraj** 11:02 Yeah, that makes sense.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 11:04 And I've… asked in the community repo to get a email alias set up. Trask has done that.
And he said he's made me a manager so I can add everyone else, but I don't know where to go to do that yet, so I've asked him in the comment, and once he replies, I'll, get that set up, and then do the PR to update it.
In the scanner. Fake.
everything that it found is either merged or there's a PR open. I think there's one left for me, which you already had a review comment on, Raj.
That I've responded to. And then there's another one open from Piotta.
And once all of the final PRs emerge, and I've got the email list set up, I'll onboard Contrib.
And see what it finds there.
power to the PR dashboard… Steve DM'd me the other day, said he's at a conference this week, so… we're not going to hear back from him on that one.
Yes, to fix the managed conflicts.
That's the one we just talked about, I'll merge that in a minute.
This is the one that's, like, it's the third attempt to fix the same problem.
I think we talked about it a couple of times. We'll just try to fix it again using a app context switch, so people can opt out of the behaviour change if they need to.
I think that's the most important in quotes, of the ones that the Anthropic scan found.
There's Navia's PR, which we're still waiting on CJ to look at.
This is the one that you had a comment on, Raj.
Similarly, with that one, I've put in an app context switch.
Not an app context switch, an environment variable that people can use to opt out of that if they want to.
**Rajkumar Rangaraj** 13:12 Yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 13:13 That one, I need to re-reviewed that one.
the .NET level we already talked about, and then there's two PRs that are performance tweaks.
No, sorry, that's not right. That one's a performance tweak from a scan I did the weekend, and that's, one of the other anthropic things that Piotr's already looked at.
Let's main repo… contribute… That's waiting for your pre-order to re-review.
I know you're looking at that one, Matt.
And then there's 2 PRs that are… Me doing performance investigation stuff again.
And then someone opened an issue to EdsonShoosh.net, however you want to pronounce that instrumentation, but Piotto replied to that and asked, have you tried asking upstream if they'll just build Instrumentation in first.
So, we're still waiting to hear on that one.
**Rajkumar Rangaraj** 14:27 Yeah, I think we should try and push that. I've seen in the recent times, whichever the instrumentation that got added here, right.
None of them come back and did the maintenance on that part as well. For example, there is a service fabric package. We tried pushing back, and they came very strong, said that we need to add it here, and they added… got a beta package, and then don't see any contributions on that at all.
So…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 14:52 They appear rarely. I think Sebastian is the main maintainer for it. He has popped up occasionally to do PRs for new versions of Service Fabric.
But otherwise, they… it doesn't seem to respond to feedback to just general PRs.
**Rajkumar Rangaraj** 15:09 Yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 15:11 what I was thinking we could maybe do, I've got, like, a to-do item is… that I've made myself, is every time this comes up, I think, oh, do we have some documentation somewhere that basically does this whole, go off and… try and add it somewhere else first, but I don't think we do, so I think maybe we should write a guide that we can point people to, going in the contribution guide, that says, if you want to add new instrumentation first, try and do these things.
Because I think we get a lot of people who just sort of… they do it as a drive-by out of nowhere with no notice.
And it feels a bit mean.
for them to put the effort in, and open a PR, and then us go, no, we don't want it.
And then… I already opened the main repo issues in the last week, there was nothing… And then there's two related issues in Contrib.
someone opened an issue, which I don't think is an issue, it's just… really, it's a feature, that they can't pass iConfig into the host resource protector.
And then that spun off into a conversation about supporting that in all of the resource detectors, so I've left a comment on that.
for Steve, because I think this is probably something we can deal with.
Via all the declarative config work.
Because the resource detectors need to play the deverted comfy anyway.
So, probably.
Get resolved somehow that way.
Otherwise, that was… everything that I put on the agenda was on the, the PR dashboards.
Is there anything else anyone wants to chat?
**Rajkumar Rangaraj** 17:20 Okay, that's all. I believe, I think, the biggest, like.
Thing is the .NET 11, and then… Like, ruining that… Pending year, so that you get unblocked for the next major release, sorry, the next final release as well.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 17:41 Yeah, nearer the time, I can always do a point and create a PR in draft that's got all the 11.0.0 version numbers on it, and it just won't build until it gets released, and we can have it ready. Yeah.
**Rajkumar Rangaraj** 17:58 It's November 11, right? Or 13, I don't recall when it's 13.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 18:04 I think 12 through 13th, I think.
Oh, no, 10th. 10th. 10th.
**Rajkumar Rangaraj** 18:12 Then, oh, it's slightly earlier, okay.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 18:16 Yeah, about 2 weeks.
Cool, unless you've got anything, Matt?
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 18:28 Not today.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 18:30 Cool. Alright. Quick, quick meeting then today. See you next time.
**Rajkumar Rangaraj** 18:38 Thank you. Bye.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 18:40 Bye.
