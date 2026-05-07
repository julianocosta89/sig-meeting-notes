SIG: .NET SIG
Date: 2026-05-05
Duration: 34 minutes
Zoom Recording URL: https://zoom.us/rec/share/URj01i2Gdtv6Q3eIIxF3TUZcnV6Yt0BWWkVzAWygArtm5GhZxy5JReTy3j4j0b74.sXJW2INY_VBnwcij
============================================================

## Zoom Recording Transcript

**Martin Costello** 04:38 8.
**Matthew Hensley / Grafana Labs** 04:41 - Messaging the, random note-taker, Nort link. You can use, like, SMS-style things to get them to go.
**Martin Costello** 05:10 Yeah, I don't… I don't know if Raj or Alan have come in. I haven't heard anything from them today.
**Matthew Hensley / Grafana Labs** 05:23 No problem.
**Martin Costello** 06:10 Hey, Raj.
**Rajkumar Rangaraj** 07:23 Hello, everyone.
**Martin Costello** 07:25 Fair enough.
**Matthew Hensley / Grafana Labs** 07:28 Hello.
**Rajkumar Rangaraj** 07:33 Let me see if I can today share and drag things out.
Is everyone able to see my desktop?
**Martin Costello** 07:47 Yep.
**Rajkumar Rangaraj** 07:54 Martin, you have some topics, like, is it really a PR, you want to someone to take a look at the PRs, or…
**Martin Costello** 08:06 So… The first one is a fix that Piotta DM'd Yumi and Alan about, and also it's touching an area that people have tried to fix in the past, and then the fixes have been reverted, because they've issued… caused issues. So… That needs looking at.
And then… That bug, plus another one I fixed on Friday.
could do with being released sooner rather than later, but there's already changes in main, quite a lot of changes in main now, including ones that add new APIs. So, to release those, we'd need to do a 1.16, And Piotta suggested to me when I was chatting to him on Slack earlier, that if we're going to do a 116, ideally it would also include, though, Julius's log bridge-related PRs.
Even if we… if they're just included in an RC, and we do an RC on the same day, so there's an RC with the experimental stuff.
And then full release.
**Rajkumar Rangaraj** 09:16 I'm slightly worried about the logs PR, because the scope of the logs bridge, the discussion, what we had, and the way where we are heading is in the, is not in the right direction.
So, if you look at it, like, when we agreed upon on the logs bridge, whatever we have it in the experimental, we will switch that and build at a later point if anything is needed, or we need to fix, and then incrementally on top of that.
But, seems like, like.
we need to go out and fix so many things. We know the current logging, does… does not follow the log specification, because the .NET went… .NET did a stable… the OpenTelemetry.net did a stable release of logs even before the, I think, OpenTelemetry log specification has evolved. That's why we see a gap in… in that.
So…
**Martin Costello** 10:15 On this, I'm just passing along what Piotr said to me, which was, ideally.
**Rajkumar Rangaraj** 10:21 Yeah, I hear, I know that, like, we all.
**Martin Costello** 10:24 I'm not pushing that they have to go in.
**Rajkumar Rangaraj** 10:27 Yeah. As soon as possible. So, I would say that we have to hold on on this one, like, if we want to bring further changes, I don't think the experimental APIs are tested with the new specification, with all these things.
If this has to be done, I would say we should also part this under the experimental flag, release a beta version.
get the feedback from the user, and then switch it, because this is a change which is happening on the… something. We have kept it under the experimental, and we feel this is going to help and everything.
So, that's how this has to be driven. I know Logs Bridge is one of the biggest gaps. For example, it's a biggest gap even for the Microsoft also.
So we have the customers who are using the classic analog adapters for application insights and all. So we pretty much moved all our customers saying that, like, OpenTelemetry is the, SDKs to use and everything. So, but still, those kind of customers who had the adapters which had been written, or kind of stuck. They didn't have a solution, but that also should not mean, that it should come at the cost without reconsidering things in here in a proper way. So, that's why I just want to leave a comment, even if it gets recorded, even Piotr can also Go ahead and take a look.
I think Alan was, like, supportive with a few APIs. I think I'm… I should be fine with this, but if there is no specific change, big change, we should be good enough. Probably I'll also have a… if possible, I'll catch up Pietro, tomorrow, to see, Decide upon it, and we can… Work on the release.
**Martin Costello** 12:20 Okay.
**Rajkumar Rangaraj** 12:21 Yeah, do you know what demands a minor version bump here, on this?
**Martin Costello** 12:30 It's… the minor version isn't to do with any of the PRs that are in the document, it's stuff that's already been merged.
**Rajkumar Rangaraj** 12:41 Does it change? No, like, should it be a… like, I just want to check, like, what's your take about… should it be a patched version, or should it be a, A minor version, but that's my question, like.
**Martin Costello** 12:57 Well, there's new public APIs in Maine.
**Rajkumar Rangaraj** 13:01 Okay, makes sense. That answers it.
I think… I don't think there is an issue, us, with releasing 116, like, I think we should be good. When did we release the other one? Because people might be very frequently taking the updates.
**Martin Costello** 13:19 I can't remember when 15 was. I think it was maybe January, but we've had a patch in the last 2 weeks.
**Rajkumar Rangaraj** 13:26 Yeah.
So, that patch… Forced everyone to take an update, because we marked the packages as vulnerable, so everyone had to go through the, update. But, if, if you, if there is a customer waiting for it, and if we have to do a, like, minor version release, like, in… within a week or two, I think I'm fine about it. If no customers are waiting… Yep.
**Martin Costello** 13:59 The ti… the timeline, really, It's a mix of two things. The first is… 7191.
Because 71 might… 7191 might need us to do a release.
Because that's the thread Piotr has in Slack.
Because there's a possible security implication of this fix.
**Rajkumar Rangaraj** 14:22 Okay.
**Martin Costello** 14:24 But other changes have gone in in the last two weeks.
Which means that unless we go through all the hoops to do a patch from a branch just to cherry-pick.
Two… two changes.
Then it will be 1.16 anyway.
**Rajkumar Rangaraj** 14:41 Okay.
I'll take a look at these things.
**Martin Costello** 14:49 Yeah, so I think for this PR, the main concern is Context being leaked between threads.
And the fix seems okay to me, but Pyoto said to me that, like, there's a comment on the PR, there's history of changing this area, so we don't want to fix one problem and cause 10 others.
**Rajkumar Rangaraj** 15:12 Yep.
**Martin Costello** 15:15 So that's the… that's the only reason this one's hanging around, and also, if we… if we do take the change, why we should do the release sooner rather than later.
**Rajkumar Rangaraj** 15:24 Yep.
**Alan West** 15:25 It'd probably be worth looking. There was an old PR, that Cote Blanche, opened.
Due to an issue with baggage.
Sounds like it might be similar to this, but honestly, it's been a while, so I'd have to… I'd have to refresh my memory, but… One of the things, whatever it was that he was doing a couple of years back was essentially changing the behavior of baggage.current. It was essentially a braking change.
There were arguments made that it was a bug, But there were also arguments made by users saying, no, we actually rely on the current behavior.
So… it might be worth digging up that PR. I can maybe try to find it. To see…
**Martin Costello** 16:20 I think it might be the one that's linked there.
**Alan West** 16:23 Okay, okay, so it's already been found. So yeah, I guess, I guess I've not looked at, your recent PR.
But that'd probably be one of the lenses that I'd look at this through, was to be… is it essentially doing the same thing? Is it changing that behavior in the way that people were…
**Martin Costello** 16:42 Yeah, I think it is effectively doing the same thing, because Blanche's PR description says, remove the wrapper object to prevent context leaks.
But the issue was surfaced in the context of a codec scan that Pyota did that said that context leaks are a problem.
So they… and they shouldn't happen. So… If it's a valid security issue.
We should have to fix it regardless of the impact to the behaviour.
Or at least provide an escape hatch.
Somewhere.
Because I think that's the crux of the issue, because if it's… if it's a security problem, we might have to fix it anyway.
If it isn't, and the fix is basically the same as the one that's already been reverted, then we should just abandon it.
**Alan West** 17:39 All sounds reasonable.
Yeah, and my memory about the, you know, our baggage API is just really bunky. There's, like, another aspect of this, right, that… in an ideal world, we wouldn't really own the baggage API, right? Like, it would be something that .NET would own, much in the same way as it owns activity and so on.
And so that's something that I'd look to as well, like, I don't know if there's… active plans for the .NET team to take this on, but… Ideally, we would just get rid of this API, right? Like, or just, like, basically obsolete it, at the very minimum.
And…
**Rajkumar Rangaraj** 18:24 There was a conversation about it, and I recall Lodmilla and Sam Spencer was earlier driving in the .NET.
**Alan West** 18:33 Yeah, dude.
**Rajkumar Rangaraj** 18:34 I don't know where there was an issue created, and they both were driving very aggressively, so I don't know where it stands now.
Maybe we need to take a look at that, too.
**Alan West** 18:49 Yeah, that… that's always been, you know, the thing that I've felt would be ideal, is that… you know, the diagnostic source is basically our API, but, like, there's a couple things like this, like baggage, that are these kind of weird appendages that we… we have We have in the hotel, you know.net, API.
Anyways, that'd be something… that'd be something to maybe kind of dust off as well.
**Rajkumar Rangaraj** 19:29 Well, I think we need to do an offline review on this and figure out, is it, like, reasonable to leave, or we need to have it fixed?
As per the findings, security findings.
Let me see if there are any other topics.
There are no other topics, let's move on to the… pull request Martin, I know here there are a lot of pull requests, most of them are from you, and you're handling also, the lot of requests from the, the other contributors, too.
So when I just come here, right, like, my bandwidth is currently limited for… it's going to be the same way for next few months, and we know about Alan's bandwidth also. This is also limited. So if we need to come to this repo, and we need to understand if there are 20 PRs.
From you, like, which is the highest priority you wanted us to take a look and merge it?
So, if we have some labels to figure that out, it would be easier for me instead of randomly jumping on a few of the PR and giving approval on that. For example, if I come here, I'll immediately… whatever is on the top, I'm just gonna pick that and take a look at it.
So, if we have some strategy to help us out, the maintenance, it would be… and the uplures, it would be slightly easier to manage this phase.
**Martin Costello** 21:05 Yeah, I'm happy to label stuff if we come up with a way to do that, because Piotr already said yesterday he was going to be away from Friday.
For a week and a bit. So I DM'd him a list where I'd gone. These are blocking work, these are small, these are bug fixes, and he went through some of those for me today.
**Rajkumar Rangaraj** 21:26 Sure, and you are doing an excellent work. It's a, like, the issue is on our side, but we are giving you more work. Even if you don't want to formalize here and randomly ping us on a Slack, that's also fine with us.
**Martin Costello** 21:40 Okay, yeah, I'm just very… I'm very aware I don't want to be the person who keeps poking people asking for reviews.
But ideally, they happen naturally, rather than you having to chase.
**Rajkumar Rangaraj** 21:53 Yep.
Just for the prioritization because of the bandwidth challenge. If not, everything should be okay, like, fine, yeah.
**Martin Costello** 22:02 Yeah, I think the main issue I'm having is trying to do the Prometheus stabilization is… I'm trying… I'm… trying… I'm touching the same area of code and creating merge conflicts with myself, because everything's split into multiple parts, so… That's creating some complexity, but… Most of the PRs that open at the moment, they're just old, rather than important.
**Rajkumar Rangaraj** 22:31 Got it.
Is it… is there anything that needs an immediate attention apart from the one in the list? Like…
**Martin Costello** 22:42 let me… there's one in Contra, let me find it. There was a PR that got merged last week, and then after it got merged, there was a co-pilot review that found a bug, which I fixed, but It's number 4337 in Contrip.
It doesn't have to be reviewed right this second, but, that fixes a bug that's in main, in Contra at the moment.
He just checked the list I sent to Pyoto, but I think that was the only one that's not been dealt with today.
**Rajkumar Rangaraj** 23:21 What am I doing?
**Martin Costello** 23:28 And that's the annual, that's the annual.
You've got raw.
**Alan West** 23:34 And the… The URL is just wrong.
**Rajkumar Rangaraj** 23:37 Boom.
**Alan West** 23:37 github.com slash raw.
**Rajkumar Rangaraj** 23:39 I did not notice that.
Which one is that?
**Martin Costello** 23:50 The second one down.
**Rajkumar Rangaraj** 23:52 Okay.
**Martin Costello** 23:54 And the third one would be useful as well, I just noticed.
**Rajkumar Rangaraj** 23:58 Okay, I also, like, reached out the ASPNet core, like, we… I remember, like, we had a discussion in private to get the ASPNet, team to take a look at. Did he take a look at it? I did remind him the second time he.
**Martin Costello** 24:12 Same good.
**Rajkumar Rangaraj** 24:13 If not, I'm just going to engage Daniel to get someone else to look at it.
**Martin Costello** 24:18 No. Yeah, I think… if I remember correctly, it's like, one or two of them are PRs that just need reviewing. One of them's been reviewed, it just hasn't been merged. And then I think the others is me asking for… Quick initial feedback before doing a pull request to do something.
**Rajkumar Rangaraj** 24:39 Got it.
the idea was to have the… someone from the ASPNet Core team also as a learner to that ASPNet Core instrumentation. That's what something we need to do for them to have the ownership in this area.
**Martin Costello** 25:03 Yeah, because I think one of the… one of the PRs… James Newton King has approved it, but I think because he's now working on Aspire, he hasn't merged it, because it's not his anymore.
But it's just sat there waiting for someone to press the big green button.
CR.
**Alan West** 25:27 Like, one of these… one of these cases where… The work we're doing on this instrumentation The behavior may be different between traces and metrics, which is done natively library.
**Martin Costello** 25:40 So, say, sort of. What I'm trying… so… They're trying to make it in 11 that it implements the full HTTP semantic conventions, but there's a few bits missing, or that don't match our current behaviour.
And I've got pull requests or issues open to… Get that so it actually definitely does, so we can drop as much code as possible from our side.
It's just getting people to actually review and merge, or give feedback on those things.
**Alan West** 26:18 Gotcha, okay, so these are changes that are… being made, also coming up in .NET 11.
**Martin Costello** 26:27 Yeah, yeah, because then it's… I think… James Newton King opened an issue saying, hey.NET 11 implements all this stuff so you can remove things from telemetry.
it's in Preview 3. Then when Preview 3 landed, I went through it all and ripped… not ripped out, made some of our code conditional on, if it's .NET 11, don't bother, because it will be there anyway.
And then there was a couple of bits left over from the spec.
That they hadn't done. So it's just trying to get those bits in, so ASP.NET Core itself can go, we are compliant with the semantic conventions.
Because, at the moment, there's, like, one or two bits left over that mean you would still need the instrumentation library.
**Alan West** 27:14 Okay, and the idea is that the .NET team, by the time of .NET 11's release, is that they would… They would fill those gaps as well.
Or we would continue to.
**Martin Costello** 27:27 Yeah, because one of the issues is… there was an issue created in the .NET 10 timeframe, which was, like, had the schema URLs.
And then it didn't make 10, got bumped to 11, and no one's picked it up. And I've gone, I'm happy to do it, but how do you want me to do it? And I've got no feedback on that yet.
**Alan West** 27:45 I say, I say.
**Martin Costello** 27:48 But yeah, I think the ideal end state is that when Eleven ships, you wouldn't need the Enrich library for ASPNetCore, unless… sorry, you wouldn't need the instrumentation library unless you wanted to use the enrich hooks.
And you'd get all the, the attributes built in.
**Alan West** 28:11 Cool. That sounds awesome.
**Rajkumar Rangaraj** 28:21 Cool, I think the other thing is all the… mostly the issues opened by you.
I'm not in here, like… And then I see one circular dependency issue.
**Martin Costello** 28:34 Yeah, so that one, the fix has been merged.
**Rajkumar Rangaraj** 28:38 Okay.
**Martin Costello** 28:39 But I've left it open because the test coverage didn't find it.
**Rajkumar Rangaraj** 28:43 Okay.
**Martin Costello** 28:44 So when I get time, I'm gonna write a test that finds the bug.
And then I'll try and revert the fix. Sorry, not the revert the fix… revert the undo, which was the fix, so that the functionality comes back again.
**Rajkumar Rangaraj** 28:58 Got it.
I think pretty much we are done covering all the items. Is there anything else that anyone wants to bring in?
I think if there is nothing else, we could call it out. Thanks, everyone.
**Martin Costello** 29:19 Bye.
