SIG: .NET SDK SIG
Date: 2026-11-17
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:00:39 Hello!
Martin Costello (Raintank, Inc. – Grafana Labs) 00:01:13 You hear me now?
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:01:15 Yes, I can.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:01:17 When I joined the call, it said the mic was fine, and then it randomly just decided it to tell me it wasn't.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:01:24 Wow.
Seems about pace for computers.
Last week.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:01:32 Might just be me and you, as… I think this is the week where Raj doesn't come, and Alan said he couldn't make it.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:01:43 Okay.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:01:45 I was KubeCon?
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:01:47 It was pretty good.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:01:52 Other than, you know, there being no planes.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:01:55 Yeah, well, I mean, there were plenty of planes. It's just, they weren't going places.
So, I only got home 24 hours later than expected.
So, not too bad.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:02:16 Guess it's just gonna be me and you. So… The only stuff… the only thing I've put on the agenda is this issue that Andrew Locke opened earlier.
Which… So, putting it on the agenda, there's been some comments on the upstream issue. There's one I haven't even read, because they're talking on it now. But it basically seems like Net Standard 2 is all well and good, but if you're using a few… continue to try and use .NET 9, even though it's unsupported. It won't work anyway.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:02:55 I… Well…
Martin Costello (Raintank, Inc. – Grafana Labs) 00:03:01 Seems to be to do with… is… something to do with his external init. Let me open the… And then there's a… there's a debate.
Happening about it.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:03:35 I… I can understand… the point here about, if you say you support Net Standard, Can you support it?
Martin Costello (Raintank, Inc. – Grafana Labs) 00:03:49 Yeah, it's sort of like, I get both sides of the argument. It's like, yeah, well.
Net standard is there.
regardless of support, I mean, it should work.
But it doesn't.
But also, now, because it's unsupported, they're like, well, we're not gonna fix it.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:04:10 Well, that's… that's the thing. It's… net standard is separate from runtime version, so… Net standard 2.0 libraries are… don't have this problem on supported runtimes, do they?
Martin Costello (Raintank, Inc. – Grafana Labs) 00:04:25 No. But also, I think the thing that's… a frustrating Andrew Locke is because A works.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:04:33 Nope.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:04:34 8 works, 9 doesn't.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:04:36 Well, neither one of those is supported.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:04:39 Yeah, so they both went out of support, but the newer one doesn't work at all with 11.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:04:46 I'm trying to look and see if there is… an easy fix?
If this is… Yeah…
Martin Costello (Raintank, Inc. – Grafana Labs) 00:05:05 Because then, we're stuck on 11, because… Even if we wanted to go back, there's stuff in 11 we need.
So, even if we wanted to diverge on versions.
It would break stuff we've already shipped.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:05:22 Is there no way to… do a… net 9… Pragma, and a patch release, and just tack around this, so at least it doesn't blow up.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:05:37 I mean, we could, but you could just argue Because a fixed forward to make 9 work would be… Oh, but it's the new one, but it's not really, it's still 10.
So, you might as well just say, well, don't upgrade.
If you're on an unsupported runtime and it doesn't work, don't upgrade.
Because you can't… we can't give you the new features.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:06:02 Yeah.
Okay, so… Sorry, go ahead.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:06:06 No, I was just gonna say, like, we can't give you the new features, so you're getting a new version that actually doesn't give you any benefit, it just unbreaks you, but you could unbreak yourself by not taking the upgrade.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:06:16 Yeah.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:06:19 I guess.
For Datadog, it's… they want to support 9 anyway, regardless of Microsoft's and our stance.
And they find that they can't.
Because they're blocked. Because it breaks.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:06:40 Yeah… I don't… Whoa.
My two cents on this one would be… Let's see how the runtime issue shakes out. Looks like there's already people replying to it, and… Discussing it with them from the runtime team, so…
Martin Costello (Raintank, Inc. – Grafana Labs) 00:06:57 Because I think if… If they change something, say, for, like, 11.02, to… Fix whatever thing in the build system and the shims for his external init that makes it stop working.
Then we could, for net standard, increase the baseline to, like, 11.02.
Which would block it. Although, you could patch that yourself in your own app, and we wouldn't have to do that if you wanted to run it online.
But it… then it does raise… but if they don't fix it, or even if they do, it does raise the question about, well, if… diagnostic source just doesn't work in that standard anymore.
Should… what do… what's the point of us having that standard if the thing we depend on doesn't work with it?
Because also, separate to this issue, it's like, we don't actually test the net standard build.
Because every framework we test for, doesn't use that TFM.
And to test the net standard build worked, we would have to actively test against unsupported runtimes.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:08:11 Yeah, and I don't…
Martin Costello (Raintank, Inc. – Grafana Labs) 00:08:13 Munch about with stuff. No, neither do I. Or we'd have to munch about with stuff, because when I was getting Claude to work on something the other day, it was like, oh, yeah, Copilot says that we're not actually checking the net standard build.
And to validate and get coverage for that.
I'm just gonna mess around with the Blazor app, and force it to do so. And it just created loads of hacks. And I looked at what it was doing, and I was just like, okay, continue with what you're doing, and validate it does actually work.
And then delete all of this test code, because we're not going to keep it.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:08:51 Yeah.
I… I am both sensitive to their… Concerns here, and the pain it causes?
I 100% get it.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:09:08 Hmm, yeah, it, it, yeah, I think… My initial read on it, which I put in a comment on it, was basically, yeah, this sucks, it doesn't work, but also it's not our fault.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:09:22 Yeah. So, I mean, in that case, what I would consider doing… is… Letting the runtime team figure out how they want to respond.
And… Maybe they'll come up with a… Nice solution. I mean, they're the.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:09:39 experts.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:09:39 in it?
And… Microsoft is, of course, very dedicated to backwards compatibility, so… If someone can make a good argument, I'm sure they'll be happy.
To do something.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:09:54 Hmm, because Andrew suggested we, like, put in a build target to do a warning about the fact that it doesn't actually work, but I don't really see the point in doing that, considering that the SDK already tells you it's not supported.
Like, you'd have to ignore one warning.
And then get another one.
And it's like, if you're already ignoring one warning, you'll ignore the extra warning, and then it still won't work, so…
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:10:21 Yeah.
I, without being unfriendly, the commoner.
To say, that's a contributions welcome.
Scenario.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:10:35 Hmm.
But yeah, I don't… I don't… I don't… think there's realistically anything I… we could do to fix it, because the bug is in… diagnostic source. I did… I did put some… I didn't want to point it out too strongly, but I put something in my comment that was basically like, oh, if only you tried this out earlier.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:10:59 Maybe…
Martin Costello (Raintank, Inc. – Grafana Labs) 00:10:59 Wouldn't have shipped.
Because we had… we did do a pre-release.
without 8 or 9 TFMs in it. If it had been tested earlier, you would have found this earlier, and it probably still would have been too late for RTM.
But they might have gotten, oh, yeah, we didn't mean to break that.
Fix it in the first patch.
Although, it maybe… would have maybe been an interesting… A theoretical debate to have, which is, like, the version you're about to release for a runtime that is in support now, but won't be when it ships, doesn't work.
Do you fix it because I'm telling you about it now when it is in support, or do you not fix it because it won't be in support?
when it ships.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:11:54 I suspect we're gonna have some more of these pop up, because… The people that are in these situations like this?
Are obviously not going to be checking these beta releases… Unless they are one of the more advanced teams?
Who is begrudgingly supporting one of these, and knows they have to drag it along.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:12:20 Hmm.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:12:22 But if they're actively developing on these products and don't have a migration plan, This just gonna keep happening.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:12:30 Hmm.
I would take… I already did. I was gonna say, take the triage label off, that's already done. So yeah, I think for this one.
I think the ball is in Microsoft's court, unless… Unless it can be proved otherwise, but then if they don't patch it, there's not really much we can do.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:12:57 Yeah, I mean, there's always gross hacks, but… I think we should try to avoid those.
As we can going forward, and encourage people to upgrade.
But I'm… That's why I'm always just like, yeah, they're not gonna check out that beta. I mean, it's just… A lot of the people just can't.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:13:20 Yeah, I was thinking more for, like, vendors, you'd hope they'd be a bit more… Ahead of the curve with it.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:13:28 Hmm.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:13:29 Than, you know, just random… Joe Bloggs and his, to-do app.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:13:35 That is… that's a good point.
Yeah, I don't… Wow.
Say we can just leave this till next week.
If enough people Run into serious problems.
And raise the alarm, we can get more involved, but it looks like the runtime team's messing with it already and aware, so… Might as well let them… make a call.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:14:06 Yep.
Yeah, because I think if they do fix something in an 11.0 point something release, we can always increase the minimum version, even if it's just for the net standard build.
But that one, because I think we already… But .NET 8, we already shipped, like, 802, because There was an AOT bug.
Or something like that.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:14:37 Yeah.
Nope.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:14:47 Yes, put that one pending, see what happens in the runtime, and then, see what we do after we get an answer, because I guess the easiest thing is they patch something, then we just update it, and then it's fixed.
And then we can kick the can down the road of… Do we care about a net standard or not?
I think we should probably should keep it, because it's… it's, like, sort of the get-out-of-jail-free… TFM.
Where, if you really, really want to try and still use OTEL, and you're using some weird, wacky Combination of things, you still can.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:15:27 Yeah. No, that's… I mean… I think that's why we elected to go Keep publishing that?
Just because it has benefits, despite the fact it has these.
issues. I mean, it gets a little nuanced, and… It can be handy, even though it can… cause problems.
I mean, between all the net standard stuff, and then, Oh, the different NuGet versions, it's… Kinda like roll the dice when you start getting off the happy path.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:16:06 Hmm.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:16:06 All kinds of strange compatibility interactions.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:16:15 Yeah, so that was the only thing I put on the agenda, other than the usual issue and PR review. Was there anything either you or… Hi, Sean, you wanted to talk about?
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:16:30 Not really, just… I have plenty of time if there's any of these we want to look at and discuss.
I tried to keep up last week.
But once more was gone again, so… Don't know if there's anything that… You're needing… More eyes on, or anything? Go ahead and knock them out if there's something that you've seen.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:16:54 Just have a quick look through the list. I believe Steve's on vacation this week.
So, his stuff would just be waiting till he gets back.
I think this… this one's ready for merge, but I've been letting Piotta decide what to do on that one, because it's a… it's like a breaking change for minor, and I asked that we leave it out for a couple of days in case there was… Some issues with the 121 release.
But some of the, anthropics and stuff's already gone in.
So, that's kind of free to go in now, but I've been leaving it for… Pure to press the button on that.
this one… that one's been reviewed, but it's related to an ask Steve had.
So, I'm gonna leave that unmerged until he's got a chance to look at it.
You've already looked at that one. This, this one is for an anthropic scan result, I won't click through to it.
But it ended up… being larger than I would have expected it to be.
in… I think it's over a thousand lines, the diff.
this one.
Because it was one of those changes where every time the agent finishes a turn, the other agent finds problems.
And you just keep eating, and it snowballs from there, so… That one's… Could do with, like, an extra eye on it, in case there's any issues with it.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:18:29 Yeah, I started looking at it, Yesterday, and have not reviewed, because it… some of the… what was it? Let me pull it up real quick so I can see what was causing me.
concern. Yeah, this new, like, stateful tracking that happens in it to split it into batches.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:18:52 Hmm.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:18:53 It's… like, it's not… Especially… difficult.
But there's just a lot here, and trying to read through it, and…
Martin Costello (Raintank, Inc. – Grafana Labs) 00:19:05 Good news.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:19:05 And the execution flow was… more than I could, track.
anymore. It's like, in isolation, all the methods look reasonable, from what I can understand, but I couldn't figure out if The totality of it.
was okay.
It's like, alright.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:19:24 Oh my goodness.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:19:24 So it's… I don't know if there's a way… Yeah, it's just, it's very… It's a very different way of, Doing what's here, so it's, like, completely reworking how this… behaves. And actually, I need to see… I have a note somewhere here that I took.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:19:48 Yeah, I remember when I set Claude on this, it started relatively simple, and then It… the reviews kept finding more edge cases.
And then it was like… and then I benchmarked it, and it made it, like, twice as slow.
So they were like, go think about it again, and then they did a different approach.
Is that this… this is one of the… The batch we got on Friday morning.
Europe time, which was, like, 22 findings, and I think it was, like, 5 or 6 of them were medium, and this is one… basically, I'm going through the most to least severity, and all the ones that are left now are low, and this was one of the medium ones.
But… but none of them I would consider to be actual security issues.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:20:43 Okay, so I found my note that I wrote last night, because this adds, like, mid-export, bump it to the next batch, right? That's…
Martin Costello (Raintank, Inc. – Grafana Labs) 00:20:50 Yet.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:20:51 Trying to keep track, looking at what the… these bullet points of changes we're trying to do.
I will… Was struggling to track the estate.
stuff, whatever. I didn't know if it might be… more straightforward to… Estimate.
Ahead of time.
Since we're now including things like, what is it?
The schema version, semantic convention version, and things like that, that are starting to blow up these a little bit, and… Didn't know if it might be… simpler to… Estimate batch sizes in… Handle it that way.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:21:37 No.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:21:37 and B.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:21:38 If I remember correctly, this and some other PRs.
They're all based around the, like, the scenario where you're logging an attribute, And… It's crazy long.
And that's what messes it up.
Because, like, some of them that are in the Prometheus, quite low, is it's like, yeah, if you log a user agent string that's 8 kilobytes long, and you make it an attribute on your metrics, which will just shaft your cardinality.
and you accept such big values, and then they're in metrics, then yeah, your batches will get too big.
But… Maybe I'll look at this again. I'll re-review it tomorrow.
And see if there's a different way it can do it.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:22:36 I'll, I'll take my notes and just yell at the computer, since I'm sure I'm not describing myself great here, since…
Martin Costello (Raintank, Inc. – Grafana Labs) 00:22:45 I think the main thing that I wasn't a big fan of it when I opened was… Every time you, like, write a bit of data in the serializer now, you need to remember to, like, do the bookkeeping.
in it, which… Has… has a bit of a… Oh, we add support for a new field in the future and forget to do it, and then we've got the same problem again.
to it. But, well, that's…
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:23:14 That's why I was suggest… wondering if we could, not… track the specific links that were happening here, because as it writes, it's having to do that. It's like… All the writing methods here keep track of the position, and it knows the buffer size, and… I just… I want to look and see if we could estimate Reasonably well how much we're about to write without having to actually go through it and do it.
Because that's… I think that's where the, the state management gets weird, and having to bump it to the next batch.
It's like, if we could… Guess ahead of time?
And I think part of it is that it's the first item of a batch, if I recall.
That it's the only one that actually gets fully measured.
Because that's the one that has to fit. I don't know, it's just… We're trying to handle edge cases, strangely, I wonder if we could just estimate our way out of some complexity, and maybe end up with more batches, or slightly mis-sized ones?
I just…
Martin Costello (Raintank, Inc. – Grafana Labs) 00:24:22 Hmm.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:24:23 Yeah, it's…
Martin Costello (Raintank, Inc. – Grafana Labs) 00:24:27 Take a look.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:24:28 Yeah. Yell at the computer.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:24:29 Yeah, because, yeah, this is the one I'm the least sure on, because it ended up so big.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:24:35 Yeah.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:24:39 Yes.
Conflict bluzer, there's some others that are open from stuff I've been doing today that shouldn't be too… controversial There will merge conflicts.
I don't… I need to fix that, apparently.
There's… they're all draft things. Spec stuff… actually, yeah, there'd be one, if you haven't already seen… who's it called? This, this one, the Kafka one.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:25:17 Yeah, I know this, this person… Some more time.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:25:23 Yeah, because there was the latest push, and it did a novel thing to this project, at least.
Is it added a third-party notices license file.
Because the contributor went into Aspire and pulled some code out of Aspire and brought it over here.
We traces two points. One, I don't know what we should be doing in hotels slash… LFX slash CNCF.
About attributions for copied code.
Because it hasn't come up before.
For me, at least. But also, Aspire vendors this instrumentation because it's not stable.
So…
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:26:08 Oh, and Nougat shenanigans.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:26:10 it's gonna create some sort of weird circular dependency, because if they pull bits out of Aspire and a spy don't know about it.
And they go into here, and then Aspire pull in Vendor Inc. immediately they have to manually put it in and test it, but then you've, like, got double the code.
Because… I think this code is copied out of their stable extra package.
I believe. So, basically, I pushed back on them, and I said, you should go speak to these buyer people, because ideally.
All of the extras they've added will just get backported here.
And then they… then we can ship the NuGet package, and then they can update their vending, and just do whatever shenanigans they have to make it stable.
And their code just gets thinner and thinner and thinner.
Rather than getting into some sort of weird… Attribution, rendering, infinite loop.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:27:16 Well, this specific third-party notices thing… It's actually a fun cane of worms we've avoided. If you… peek around the SDK and contribib, there is some copy-paste from other places.
With inline attribution.
Like, even between contribib and the SDK, there's manually synced files here and there. Far fewer than there used to be, but there's…
Martin Costello (Raintank, Inc. – Grafana Labs) 00:27:44 Oh yeah, I know we've got the, like, the… the OTLP retry stuff.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:27:49 Yeah, there's that one, or, like, in the test code, the, environment variable scope.
stuff.
So, I mean, so far, it's been pretty straightforward, right? Like, just… Leave a comment, but…
Martin Costello (Raintank, Inc. – Grafana Labs) 00:28:04 Yeah, I never really think of that one as license.
Problematic, because it's two things in the same org.
under the same license, rather… because the Aspire stuff's MIT, not Apache.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:28:20 Well, there's some, there's some code copied directly out of the runtime, too. Like, some of… or the BCL.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:28:27 Oh, I know the ones you mean, yeah.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:28:29 Yeah, there… just in general, there's code that is permissively licensed, it is attributed in those files, but there… I don't think there has been this third-party one, We probably need to check.
Since this has now come up… What, the other hotel projects?
are doing to handle it, because I know, like, Obi… Has tons of things that they pull in.
Because they vendor, like, half of the planet, just like, the collector ends up doing.
We might need to go through and… Make sure to collect all those to be compliant. That might be a question for CNCF Legal.
I'm sure they're tired of hearing from us.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:29:21 But yeah, code-wise, this one I haven't looked at at all, until I saw those things, and then I was like, we need to think about this.
This is…
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:29:30 The second attempt, this is a subset of it. The first one was supposed to be this much, and they… Implemented everything, and it had gotten out of… The implementation looked okay, but it was really hard to review, and if you wanted to make any changes, it would involve lots of churn, so I asked them to pare it down and Even the Paradowden one is… a lot to consider, especially because you have to look up Kafka semantics to make sure it all looks okay.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:30:03 Yeah, but, yeah, it's been… how long? It's been… it's been a natural day? Yeah, it's been over a day since I made this comment, and they haven't come back yet.
It just feels… it feels a bit like one of those, oh, but we need it now, sort of things. It's like, yeah, but if you really need it now, you could just build it yourself.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:30:22 Yes.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:30:23 And put whatever you want in it.
We're not gonna rush just because you're in a rush.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:30:30 No, yeah, the volume of code that's, coming with these, like, it… the contribution's appreciated, it's just hard to…
Martin Costello (Raintank, Inc. – Grafana Labs) 00:30:39 Hmm.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:30:40 You know, the more that's there, it can be difficult to, review.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:30:45 Yeah, this one's, like, 2009. But yeah, there's just some, like, novel, not-talking-about-the-code things in it that I think we need to sort out.
At least in the shape it's in at the moment.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:31:00 Before we continue, I just want to say, Sean, you joined us, did you have anything you wanted to bring up, versus us just Talking about random PRs.
Sean Li 00:31:11 I don't have any specific topic, just want to, see what's happening.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:31:20 Okay, cool. Just wanna make sure, in case there is something that you really want to talk about.
Sean Li 00:31:27 Well, thanks for asking.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:31:30 Yeah, no problem.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:31:38 There's… Yeah, I know that we're going to have some PRs to do with the RPC SunConv. There was that conversation we had in Slack.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:31:48 Yeah, and I saw that, I started to look through the feedback, there's… Looks like there's gonna be some churn on this one, too.
Yeah.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:32:03 Yeah, I didn't read the feedback, I just saw that there was some… Peter said he was gonna do.
some more… Work on other bits and pieces, as well as applying to that.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:32:23 Yeah, it seemed like there was, there's gonna be a Bonsai comments added.
to this shortly, if I understood the Slack message correctly, that basically A codex review turned up a bunch of things that seemed relevant, so…
Martin Costello (Raintank, Inc. – Grafana Labs) 00:32:40 Hmm.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:32:42 I'm not surprised, I think there's… what I'm finding on some of these instrumentations, that the semantic conventions have been lagging.
They haven't had much active maintenance.
And… especially now that we have our new fancy tools, there's lots of correctness problems in these. I mean… You've been opening up one PR after the other that's… there's small tweaks, right? Like, they're not catastrophically broken, but they're clearly not right. I know all the HTTP.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:33:15 Hmm.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:33:15 Timing stuff that's been fixed over the last few months.
That has increased the accuracy, but it wasn't off enough to actually Be noticeable, you know, when it's, like, less than 5% deviation.
Is what's happening, but I think that's… it's more of that here. The WCF stuff, I've barely been able to work on semantic conventions.
As I try to fix obvious correctness problems that just, like.
Leaving activities unstopped. In all kinds of scenarios.
Like, frankly, the WCF instrumentation was completely broken.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:33:52 Yeah, I've got a to-do item that I probably won't get to for a couple of weeks, is… I'm gonna try and… write a skill in terms of just hints. Oh, you want to implement a semantic convention version upgrade, do you? Or a new feature? Here's all the things you have to think about and need to go away and check actually works.
A bit like the, the one I did the other week, just for the simple version bumps.
Cause, yeah, it's… I think… There's definitely a hole somewhere, because… I find it a bit frustrating that you'll try as hard… I'll try as hard as I can locally with an agent to do a PR right.
And then as soon as Copilot looks at it and goes, here's a bunch of problems.
And then I'll fix them all, and then I'll find more, and then I'll fix them. And then Codex had come along and find some completely different problems, and it's like.
Why can't it just keep going locally and find all the same people?
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:34:58 That is one that has very much been bugging me, the fact that Copilot on GitHub, even at what they… they introduce, like, effort levels.
however many weeks ago, even at the lower effort, it still finds things that, like, Copilot and Visual Studio does not.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:35:21 And so, how do you…
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:35:23 Deal with that.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:35:25 It was, it was like the… two weeks ago, like, the last round of Anthropic. Every… every… I got Claude to do the fixes, I then got Claude to review itself, I then got Copilot to review what it had done, and then I got Codex to do… review what it had been done, and then there would still be stuff when it co-pilot reviewed in GitHub.
It's like… Yes, so the age of deterministic tools, at least you get the same answer.
Every time, you can keep going until it shuts up.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:36:00 Yeah, I don't… I would love if we could find a solution to that.
Because… I don't know about you, but I feel very stupid when I have put a bunch of time into one, and then Copilot nerd snipes me with something that's like, oh, I can see that.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:36:17 Yeah.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:36:18 It's like… and it wasn't for… it isn't like you just, you know… cranked out a PR and just hoped for the best. It was actually had effort put into it, so… I just… I wish we knew what the difference was, or if there was some way to run it locally, and make reviews not messy.
So, in most cases, that's why you'll see my PRs sit in draft.
For a day or two.
To give a chance for all the tools to come by and tell me how wrong it is.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:36:46 I've been doing the same. It's, like, the latest anthropic batch.
So I'll open a draft, and then I'll immediately tell Copilot to look at it.
And then there'll be a cycle until… Locally, it's fine.
And Copilot gives it a green tick, and then I'll move it out of review. And then I'm sure… and then usually, be able to find something new with Codex.
And then there's more feedback.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:37:15 Along those lines, actually, something that… has been bugging me around the correctness issues, is that I can have whatever agent go through and find missing test coverage.
Not stuff like the code coverage bot.
Flags, but just functionality and… the actual call chains, that just depends on, like, what parameters you pass. Is this actually covered? And all these correctness issues, like the WCF problems I'm finding… Where activities are just left running.
It's not anything to do with code coverage, just, like, incorrect conditionals in all kinds of places.
And I want to improve the test coverage, but then they'll be failing.
I've been considering seeing if we could have, like, Advisory test?
Tested just warn that, like, we expect to fail until someone fixes them, to start giving us a backlog of things to hack on, because it's…
Martin Costello (Raintank, Inc. – Grafana Labs) 00:38:18 Look, we have had… tests in the past… there's less of them now, but we have had tests in the past that have been skipped with just a URL to a GitHub issue. And I know that .NET teams, they've got some X-unit infrastructure.
what they call them? Quarantine tests, they call them, whereas, like, they're tests that if you run them, they will fail.
But they, like, they get hidden from the test reports, so it still goes green.
Maybe that… maybe there's, like, a category or something we can add, and then a bespoke job.
That surfaces all that, but doesn't fail the build.
And then that can be a bunch of issues.
That people can… we can slap Help Wanted on.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:39:06 I… I like that idea, because… My thought being, I'd rather get them merged, and have them be there, and have, you know, they're not blocking.
And more informational things, because if you open up an issue and put, like, reproduction case in it, it's kind of hard to work against for a lot of people.
And if it was there, already, I feel like they could, The issue, and then the link to the reproduction case already being in the codebase would be… Much more likely to get fixed in a reasonable manner versus someone having to… Figure out how to get it working, and all that.
I know it's kind of like a… it's definitely a weird one, just… there's so many of them, and I… have been getting nervous and having to, like, break PRs into lots of pieces.
And it slows things down to figure out how to un… you know, rip it apart into stacks of them, versus…
Martin Costello (Raintank, Inc. – Grafana Labs) 00:40:11 I think this one here, I think, precedent for you, is, like, there's a… there's a test here every… In, like, every theory case is skipped.
And then it just points to this issue.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:40:24 Okay.
That is… 56.77.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:40:30 I don't remember why it stood open and why I haven't put Help Wanted on it, but… There's an example of a test that's in the codebase that's skipped.
And, yeah, if it was last week.
it was annoying me that every now and again I'd open a test file. An X unit would go, hey, why don't you fix this? Why don't you fix that?
So I've had… Lord, fix most of them and raise all the severities to warning, but I intentionally left the warning about having skipped tests out.
Because we've got a bunch of them that we can't fix.
At the moment. We're sorry, no.
Can't enable at the moment. Not that we can't fix them.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:41:20 Okay, cool, I… I want to think about this for a little bit, because we always ask people for reproduction cases.
And we find all kinds of random issues, and I'm sure you have just a document that's Pages long of things to check out that you just happen to notice while doing something else.
Maybe we should, get some skip tests merged.
For anyone that wants to come by and pick it up, but also it serves as good… Documentation that we know those exist?
And we can turn them into issues, so I wonder… there's probably something fun we could do with, Just like their PR dashboard here. It's like, hey, we found a skipped test with a GitHub issue thing, or whatever, or lack of one.
I'd like to be able to mark them in such a way where we don't have to write up an issue right away.
And we can… No different than, like, maybe we should have a list of to-dos called out in that dashboard.
I like… Comments that are to-dos.
Or someone felt the need to mention it for the future.
And we can start chipping away at those, or anyone can. Makes it a lot easier.
Someone wants to… contribute, I feel like.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:42:36 I'm just trying to think… find the thing I'm thinking of, Because I've seen it, the runtime repo.
It might be.
Yeah, it's… .NET Runtime has this thing where, like, when there's tests that randomly flake.
They have an issue to track it, and then it links… it automatically, like, updates this table of, like, where it's hap… what runs it's happening in, and how often it happens.
And stuff like that.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:43:13 I guess, and of course, I guess the infrastructure that powers this, we can see, like, it's a job that we can… Pluck some things from, if we're curious.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:43:23 I'm sure all the bits to pick it apart and reverse engineer it are there, but I think it actively runs inside Azure DevOps, but I'm sure all the bits that make it do.
Are there to be hooked up.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:43:39 It's the flaky test situation.
drives me crazy, because I can never figure out, is it… just stupid things like SNAT exhaustion? Is it a flaky test because there's an actual race condition that gets triggered?
Martin Costello (Raintank, Inc. – Grafana Labs) 00:43:55 Hmm…
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:43:56 It's like, it takes so much time and effort to, dig those out.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:44:01 I did get through a whole bunch of them.
Earlier this year, and… If this loaded, it should show… it should show you if there's any tests that, CodeCov thinks are flaky.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:44:21 I will be right back. There is someone at my door.
So, KP end up dropping, but I should be just a moment.
Alrighty, I'm back. Sorry about that.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:46:01 Right?
While you were going. I just put a comment on that Ed Standard 2 issue that was basically… we're waiting to see what the runtime team deem it say.
What were you saying before you had to go to the door?
It's about the trache tests.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:46:25 Oh, just being able to pick out that… Report stuff where it can flag them.
Just because it's very difficult to figure out if, Are they actually flaky? Like, or is there a race condition? Because we've seen both.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:46:41 I think what I've been trying to do is, when they happen in my own PRs, so once I've got the PR green.
Especially if it's something, you know, I'm doing a change in gRPC and WCF fails.
That's not what I was touching. Then I just tell Claude to go and look at it.
No, maybe 50% of the time, it just changes the timeout.
But, after the XUnit V3 upgrade, lots of tests suddenly became flaky, and it was because And… They'd never really been designed to work in parallel with each other properly.
And the XUnia V3 refactoring just made that really obvious.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:47:24 Yeah, so I think being able to flag those and open issues with Some way of… Calling that out.
Could really help as far as, like, help wanted.
First-time issues, because you don't necessarily have to understand a bunch if you have a reproduction case.
Especially for something like that, that's not behavioral.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:47:49 Not to go down the whole, I've got a hammer so everything's a nail.
route. Maybe this… if we created, like, put a skin in the repo, where you could just put… say to an agent, hey, here's a link to a GitHub Actions run, it just failed.
Open a new issue with this template with the details, because the problem with just quickly opening an issue and going, this test failed link to workflow is in 30 days it'll be deleted.
So you have to go and copy out all the relevant context.
See if we can get our agent friends to do that for us.
Well, I think,
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:48:29 Actually, that's, having a skill for that would be great, but not just open the… Issue and pull the details, but… Have it tried to probe and figure out.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:48:42 Hmm.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:48:43 Of reproduction, and not open an issue, like…
Martin Costello (Raintank, Inc. – Grafana Labs) 00:48:48 Oh, sure, yeah, yeah. I was just thinking for the case where I'm busy, I don't have the time to go off on that.
bug hunt.
You could just.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:48:59 Hmm.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:48:59 Put all the context into an issue, so it doesn't get lost, and then someone else, or you can come back to it, you know, 31 days later, once the logs have been deleted, and not lose the context.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:49:12 No, definitely. I think that might be better for something like the PR dashboard.
Where there can just be a general, like, here's a list of candidates.
That have not been vetted, and… You know, like, here's all the flaky test runs, and… they may or may not be, like, spurious reports. It could totally have just been a GitHub Action problem that day.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:49:37 Hmm.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:49:37 Because that's our problem here. It's like, we don't know if there are actually problems with test concurrency.
It's a problem with GitHub Actions… The number of times a test fails because Docker can't allocate a port is… Hilarious.
Just, it's constant.
But having a nice, list of candidates.
Could be interesting, especially as people are looking for something to do. And you don't necessarily have to be an expert in the behavior of hotel.
to diagnose… A concurrency issue in a test.
Anyway, just spitballing ideas, it's just… because they happen constantly, and… we all… Tend to ignore them until we get some free time, because they're just a pain to investigate, so… Figuring out a way to… call them out, like that, we have the PR dashboard, something like that, like, all the test runs that have failed, and being able to turn them into issues or not. But having a skill… With, kind of, the steps that you want to take to figure out if it's a silly test failure.
Or if it's… some systemic issue, like the X-unit upgrade. I think that would be valuable and would… help people out, or just help us out when we go to do it. I mean, I know I always have to… Think through what it could be, so… Sometimes the skills just serve as documentation.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:51:05 Yeah, because that's why I did the security one yesterday.
Because it's like, oh, yet another bunch of Anthropic things to go through. And I had, like, a notepad file open on my desktop with, like, 3 prompts written in it.
I've died… came up with about 2 weeks ago, where I'd, sort of, every… every new issue to look at, I'd added… added, like, another sentence of, like, don't do this, or make sure you do that.
So that's why I turned it into a skill, because now I can just say triage number.
And it just goes off and does it, and knows that it shouldn't push anything unless I tell it to, in case it is a security issue, or… or whatever.
Rather than having to email myself prompts.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:51:56 One of the things I was… Wondering about with all this, since we are just talking about random things, is how we could use discussions better?
And these repos, because they're not used at all, hardly.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:52:12 No, I find that often with many repos, to be honest. They just seem to be, like, a… I know this isn't an actual issue, so… because it's a question, so I'll open a discussion, and then they just sit there.
Or they'll get one reply and then be left open forever.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:52:34 Well, I was thinking as part of the, Noticing we're getting some more people opening issues, which is awesome. Some new names, and even some repeats now.
And also have some folks opening PRs that… are pretty good, they're not just… You know, agent drive-bys.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:52:53 Hmm.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:52:54 But, didn't know if… there might be something to make a better curated list of issues, and PRs, if we could.
shuffle some of this stuff into discussions. I know I've seen some other projects do that, where, like, the issues is a very official list. Like, you can't just open one.
Until you've talked to someone.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:53:18 open.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:53:19 and…
Martin Costello (Raintank, Inc. – Grafana Labs) 00:53:20 Personally, I wouldn't like to add the gatekeepy aspect.
But I get what you mean, this all said, there's spitballing, and then there's… here's a definitive piece of work that needs to be done.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:53:34 Yeah, I think about it more not like, how dare someone open an issue that's not fully baked, but trying to lower… The effort for people to join in?
Martin Costello (Raintank, Inc. – Grafana Labs) 00:53:45 Hmm.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:53:47 Yeah, I feel more comfortable.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:53:50 I guess what I'm thinking is, what I wouldn't want to do is what Renovate does.
Which is, like, you cannot open an issue. You have to open a discussion, and I find it very annoying when you find a genuine bug, that I have to open a discussion, fill it in like a bug report, wait for them to look at it, and then just go, oh yeah, it is an issue, and then click a button and it moves.
I was like, yeah, that was… admin annoyance.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:54:19 I think an easy example is the gRPC SimCom issue that opened and had to be rewrote.
Not for bad reasons, someone's like, hey, I'm gonna do a thing.
And I got tagged.
asking, Matt, are you gonna implement these or not? It's like, oh, you're welcome to. Also, are you gonna do metrics?
And then, like… Okay, I'm gonna rewrite the issue to beat… match this discussion.
Like…
Martin Costello (Raintank, Inc. – Grafana Labs) 00:54:45 Hmm.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:54:46 I would like for people to feel comfortable asking for futures.
But when we make issues out of those future requests, and we have to have a big discussion, I know it's, I mean, like, look at some of the discussions on the runtime repo, and… Issues, like, it's, you know… You have hundreds of comments because people like or dislike what's going on, and trying to reconstruct the state of the conversation to actually work on it is… Painful. Anyway, just random thoughts, I was… that… it was a great thing where someone's like, hey, I want to do this, do you mind? It's like, you are more than welcome to. Yes, please.
do that. Also, do you want to do some more work? And… You know, if someone comes along later, some of that back and forth makes it hard to figure out what the decision was, or any of it, and… I think we'd like more people to… Talk to us and ask for things, or offer to help.
And… Think about lowering the, the expense.
on asking.
It's like… I'd rather people feel comfortable asking that stuff, because clearly there's not many messages in the Slack channel in the CNCF.
community, so…
Martin Costello (Raintank, Inc. – Grafana Labs) 00:56:01 Yep.
Yeah, I think that makes sense. Yeah, I just think… I just wouldn't want us to go down the… Only project members can create issues. Root.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:56:12 Oh, no, no, I want to make it as easy as possible for more people to join in, I think that… We're looking at needing some more folks.
and… There's obviously some people interested, so… I like to be friendly and make sure they feel comfortable, and… This makes me wonder how many people are looking at the repo and wondering if they should open up that issue, because it's not fully baked. Like, they don't know the question to ask, they just know they've encountered a problem.
So, I don't know.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:56:46 Yeah, maybe that we could do a, Review the, like, the issue template.
And see if, like, it could be improved or something like that.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:56:59 That's actually where I was thinking about putting anything, just like we added the AI disclosure stuff that is not unfriendly.
I feel like.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:57:08 Hmm.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:57:08 You know, if you check that I can't explain this, and I think we all checked that, where it was just an auto-generated Couple of line fix.
That we skimmed, and it's like, oh yeah, that's right. It's like… I think, I think that's fine, as long as, you know, people are upfront about it, and if we wanted to put in the issue template, like, you're not sure, like, come ask, like, we can talk about this. You're… More than welcome. There's no harm in bringing it up, and… I know it's scary to open issues against repose.
But we clearly have some more people looking, and just like to encourage them to continue to participate.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:57:49 Yeah, that makes sense to me.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:57:53 Alright, that's all the random things I have.
Today, if anything else comes up that needs attention, please ping me, and I will prioritize that.
Forever catching up, it feels like.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:58:07 And I don't think there's anything important currently open. It's… there's… it's just the pile of, because I've… I've got another… And, anthropic findings to point Claude Code up.
But, they're all lows, and some of… some… hasn't happened yet, but some of them might even be… no one cares, and I'll just close it.
And I'll not even do the fix. Or the fix is far too complicated for a load, so it's not worth the hassle.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:58:44 Yeah, I think we've already seen some of them that are… They've been fixed just because… It's…
Martin Costello (Raintank, Inc. – Grafana Labs) 00:58:50 Hmm.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:58:50 You know, it's… some of those have been pretty… like, how you ever exercise it?
But… still worth covering.
Martin Costello (Raintank, Inc. – Grafana Labs) 00:58:59 Yeah, actually, there was one I didn't fix today, because I thought it was ridiculous. But I did do a PR to update the comments, so hopefully the scanner will see the comment and not open it again. It was… So there's something silly, like, if you do a HTTP connect.
to a URL that you can't actually connect to, but the URL had the username and password in it, then an exception will be thrown that we'll then put in the event log that contains the username and the password.
And it's like, yeah, that would happen, but we don't guarantee that we're never going to log anything sensitive, especially if the runtime Was who gave us that.
URL with the sensitive information in it, because the Claude suggestion to fix it was basically, like, let's parse the string and look for a URL, and then see if it's got a credentials in it, and then take them out, and I was just like, that's just ridiculous.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 00:59:57 Yeah, man, that's… That's one of those tough ones where… Totally valid, right? Like… Logging raw URLs can be problematic.
But how… like, what do you do when someone typos and is an invalid URL? You just redact everything?
Or redact.
Martin Costello (Raintank, Inc. – Grafana Labs) 01:00:18 Hmm.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 01:00:18 the things that look like HTTP basic auth.
But… it's very easy to be broken.
In that case.
Like, the safest answer is to… Put nothing in the log, or just a placeholder, saying you couldn't.
parse it. Like, that's the only actual answer.
Martin Costello (Raintank, Inc. – Grafana Labs) 01:00:39 Yeah, because it was coming from, like, looping runtime, I was just like, if it's anyone's issue, it's the runtime's issue, we can't redact everything, so I just put a comment at the top to that effect, and that was the end of the issue.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 01:00:54 Yeah.
Martin Costello (Raintank, Inc. – Grafana Labs) 01:00:57 Cool, right, I'm gonna head off now.
Extra long meeting today. Let's speak to you tomorrow.
Matthew Hensley (Raintank, Inc. – Grafana Labs) 01:01:04 Yeah, see?
Martin Costello (Raintank, Inc. – Grafana Labs) 01:01:05 But…
