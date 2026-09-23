SIG: Arrow SIG
Date: 2026-09-22
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Albert Lockett** 01:41 Hi, everyone.
**Drew Relmas** 01:46 Hello.
**Pierre Mariani** 01:49 Hello.
**Joshua MacDonald (Microsoft)** 01:51 Whoa.
Okay, hey everybody, I'm gonna share my screen.
Yeah, so I know Laurent's not going to be here today, but we have a good number already, so… That's cool, I tried to… Organize the issues a bit before the meeting today.
Go ahead and write your names while we do, and we'll start looking through some issues. Here we go.
I moved the Phase 3 issue to the pinned list up above.
I asked if we might see, CJO or, Lala in this meeting, but I don't think we will. CJ's gonna try and make it to next Thursday.
I don't… Some of these have been updated recently.
**Drew Relmas** 03:12 So, this one is actually me, I reactivated it. I… Riley had asked me to think about the stability level thing, especially as we have, you know, additional components coming in, such as the scraper and the database receivers, and we're just growing a lot, so… I actually reopened this. I think we had briefly, at some point, talked about stability levels. There was a PR opened by an external contributor that I think was abandoned. I don't think it's been touched in about a month.
But I'd love to see it be part of the component inventory that David's been working on. So, David might not be here, so we might… go past it, but I was hoping that we… can do this.
**Joshua MacDonald (Microsoft)** 04:02 Cool. Do you know which, we'll request you were referring.
**Drew Relmas** 04:06 I'll… I'll find it and paste it in my thing on this issue, don't worry about it.
**Joshua MacDonald (Microsoft)** 04:13 Alright.
Let's see, and then… One that we filed this week, from Ben.
I think he's here with us, but this was one that we also found a pending fix for, so I believe there are two draft PRs associated with this right here.
**Drew Relmas** 04:34 Yeah, I don't think we have Ben, but this, Uros?
I think they're from Databricks, if I'm interpreting the username properly.
And they were collaborating on what the best, solution for this would be, so… Looks like they're… Going back and forth, Ben approved this one.
**Joshua MacDonald (Microsoft)** 04:58 Got it.
Very good. Still draft. I haven't taken a look at this yet.
I did see two on the same topic.
So this one's… the other.
And I have more work to do.
So, please look at this, all of us.
Okay, so that was the, needs discussion. We aren't done, but let's see. I asked Laurent right before the meeting if he cared to see any of these… not be unstaled. He's, I think, getting to an airport right now, so, I'm gonna propose that we… Unstale his issues. Albert, two of these are yours.
I think down maybe at the bottom here.
Why can't I see that? Great, there you go. Ugh.
Can I unstale all of these, Albert? That includes these two down at the bottom.
**Albert Lockett** 06:06 Yes.
**Joshua MacDonald (Microsoft)** 06:07 Coalescing of set and transform attributes.
**Albert Lockett** 06:12 Yep.
**Joshua MacDonald (Microsoft)** 06:14 Cool.
And… I realized last week that, we skipped looking at the new list, the new issues list, and some of them have already been accepted by triagers. I thought we should add this to our, weekly, like, template. We don't always have to do it, but these are… At least the last, week worth we should look at, probably about 2 weeks. And that would have covered the one we missed last time, which, you know, includes the Windows event receiver. So if we start going through this list, we're going to cover all the ones that… most… at least most of the ones that I highlighted earlier.
So with that, I think we should take it away. Drew, would you like to speak to this?
Or…
**Drew Relmas** 07:03 Yes, I was hoping Jitunder would, be here. I guess, Pragna, you're here?
Maybe you can represent this in some way?
**Pragnamohapatra** 07:16 So I… I don't have the entire context, let me try to reach out to Jiten, if you could join, so that we can come back to this one.
**Drew Relmas** 07:23 Okay.
But in general, Josh, I know we've talked about it just the barest bit. There's… this is, you know, an Hotel Arrow version of… there's a Go Collector.
receiver component, for collecting Windows events.
So, Jitinder, I guess, made this super long… issue about.
**Joshua MacDonald (Microsoft)** 07:47 I'm moving for a living.
**Drew Relmas** 07:48 I'm gonna go…
**Joshua MacDonald (Microsoft)** 07:48 collector component.
**Drew Relmas** 07:50 And… Andres, I know, I see you joined as well, like, I know you had done a little bit of research on what this could look like, so maybe you can connect with Jitinder offline and chat about it a little bit more. I think a lot… similar to all of our other pull-based receivers, like, the hardest thing here is…
**Joshua MacDonald (Microsoft)** 08:10 Mmm.
**Drew Relmas** 08:11 You know, the faculty working in a distributed core, context, so it's another… Another one of the same problem.
**Joshua MacDonald (Microsoft)** 08:21 Right, so, I take it that they're… like the ETW receiver, there may be, per-core, Q, I'm assuming?
**Andres Borja** 08:34 Yeah, so I've been exploring this one. It's not exactly the same solution, because this is more, like, to run as an agent. The one I'm not thinking is to… more to run as a… As a gateway collector.
But the problem is about keeping state in some way. So we need to keep, in this case, we need to keep the state of the… bookmarks.
And those should be… You know, I… independent on the thread, basically. So… So, maybe it's an opportunity to think on this, somehow centralized storage. I don't know how genetic it can be, but it needs to be… it needs something where it can store something independent on the thread, basically.
**Joshua MacDonald (Microsoft)** 09:30 Got it.
So that sounds, similar to, an issue that I know Where is it?
I was just looking at it this week, on the topic of Prometheus… oh, I want an issue. There is one that, between Lockett and LaRon, we have something filed about it.
Let's see if we can find it.
This, let's see… there was… Oh, I need Lowatt to find it for me, but we have an issue filed, like you said, Andres, about the fact that when we have state being checkpointed, each thread will have its own copy of these, set of tasks that it's working on and need to maintain that checkpoint. I was also going to see if Tino is here. We have an open PR that's sort of on the same topic.
Somewhere here.
which is introducing that checkpoint logic here, and I haven't read it yet. So, actually, it'd be good to have, somebody, maybe Ben, maybe Jiten or Pragna, to take a look at this PR as well.
They have, of course, as we see covered up by my screen. So yeah, we have one approval so far, very good. If anyone wants to… if there are changes requested, that might keep other reviewers from taking a look at it, so, it'll be good for, Tina to follow up there. But now we're a little bit off.
Of the list.
So… so do you think we need any decisions made about the Windows event receiver?
**Drew Relmas** 11:19 I…
**Joshua MacDonald (Microsoft)** 11:20 log receiver.
**Drew Relmas** 11:22 With Jiten not here, I'm not sure we can…
**Joshua MacDonald (Microsoft)** 11:27 Got it.
**Pragnamohapatra** 11:28 He's on the way, so he will be joining us shortly. We can continue the analysis, while he's happening.
**Joshua MacDonald (Microsoft)** 11:34 Here we were. Went all the way back. Okay. I did look up the, Go collector's version of this, So, at least I'll put a link for the next person, to see, and we can come back to this. Let's see.
So, again, it's all very red, I don't like seeing it. Let's move back. So, Drew, do you want to talk about 4098?
**Drew Relmas** 11:59 Oh, yeah, this is a… pretty open and shut one, honestly. I should mark it as, Story short, we had a, internal use case pop up for us about, octet-counted TCP framing for syslog, so this is something… you're shaking your head, Josh.
**Joshua MacDonald (Microsoft)** 12:23 Yeah, what… okay, what?
**Drew Relmas** 12:25 Like, okay, like, okay.
So, essentially, you can specify the length of your syslog message.
ahead of time, and that's your delimiter instead of new lines. So, the receiver today only supports new line delimited, but this adds a framing. The collector contributes this log, has a similar option to enable it. So, I'm working with Ukarsh on that, he's already done one round of review. I'll mark the issue as accepted.
If you're speaking, Josh, you are muted.
**Joshua MacDonald (Microsoft)** 13:24 Oh, good. Hi.
So Lockett updated this one, it, has not, it's… it was stale. The same here, we discussed this last time, I think we need Lowatt for these.
And then… I don't think.
**Drew Relmas** 13:40 Do you get?
**Joshua MacDonald (Microsoft)** 13:41 This one last week.
**Drew Relmas** 13:43 Yeah.
So, this was something that I found as a result of… moving the OTLP exporter to the new shared metric sets that track exporter.attempted.
And basically, gRPC can have a partial success that gives you a little info about how many, or how, like.
How many, peter… What am I trying to say? I'm failing to find the verb.
But it's related to an issue we've found before of, like, how should we track partial Success.
And for right now, the README actually says that it follows… that it's treated as an export failure, but that's not actually correct. It treats it as an ACK.
**Joshua MacDonald (Microsoft)** 14:38 Yeah.
Does anybody want to talk about partial success? I know that that one is a long topic in hotel.
I knew it wasn't implemented.
**Drew Relmas** 14:54 It's not like a burning fire, it was just a discrepancy I noticed, so I made an issue for it.
**Joshua MacDonald (Microsoft)** 15:01 I suspect there's an open issue somewhere from long ago, unless it got stale closed.
**Drew Relmas** 15:06 It might be down at the bottom, linked.
Okay.
progressive plan to improve, I think it's in there.
**Joshua MacDonald (Microsoft)** 15:16 Yeah, got it.
**Drew Relmas** 15:19 Or it's just related.
**Joshua MacDonald (Microsoft)** 15:21 Or there could be even more. Anyway, I accept.
So, let's see…
**Drew Relmas** 15:28 I see we do have Jiten, too, if we want to go back, but…
**Joshua MacDonald (Microsoft)** 15:32 Okay, let's move in that order.
Jitinder, I see…
**Jiten** 15:37 Yay!
**Joshua MacDonald (Microsoft)** 15:37 Let's talk about Windows Event Log Receiver.
**Jiten** 15:42 Okay, sorry, I'm driving right now. I may not be able to present and walk you through the Windows Event receiver. I mean, we can punt this. This is not kind of urgent right now, because they're pushing this forward, but I'm okay to take this sometime next week. It's perfectly alright with me, so…
**Joshua MacDonald (Microsoft)** 16:01 Great. I don't think we're worried about this. Nobody's gonna turn us away or turn this away. I think we can accept the idea, but if we want to have discussion, we, you know, we can reserve it for next week as well.
**Jiten** 16:13 Yeah, yeah, I wanted to have first, like, let's people take a look at it, you know, walk it through, and have at least the, you know, the common understanding, and then we can have the discussion on this. It'll be great. I just want to keep it, open for summertime, so that's something that's all up to me.
**Joshua MacDonald (Microsoft)** 16:29 It will be good to have a sort of strong comparison with the ETW receiver. I know that that component had a really nice diagram when we started that helped explain the relationship between threads and queues and CPUs, at least, so that would be a good one to dig into a little bit more.
**Jiten** 16:49 Okay, sure, cool, thank you.
**Joshua MacDonald (Microsoft)** 16:54 All right. And then I felt like I was going to, come up with a list of recently accepted issues. If you just look at the open issues.
Sorry, wrong window.
You get to here, and then, I wanted to make sure that we had a chance to check in with… any of these ones on the bottom, especially. I know that… a very exciting one here. I'm not sure, Erin, if you've spoken about your work on WebAssembly receivers. It's very exciting. Would you like to?
**Aaron Marten** 17:34 Sure, this is a pretty long issue, so I don't know that we want to go through it in great detail, but I can at least go over the, kind of, the high-level outline.
So the… this was an attempt to capture and define how we want to approach the ability to provide a receiver plugin, as a binary plugin via WASM. There's a top-level issue that this is a child of, specifically about, WASM overall and binary plugins overall, but this issue is specifically about receivers.
So, Yeah, there's a number of different categories of WASM-based receivers. It turns out that receivers are actually, can be quite different if you look at, for example, the existing receivers that are in, the GoCollector, and then, like, the GoCollectors contrib… Repo, and they take a number of different shapes.
So for example, you know, you could have ones that are just basically, HTTP receivers. You could have ones that are, you know, socket receivers, you could have ones that are, like Prometheus, that are… that actually go out and scrape data from somewhere else. They don't just sit there and, like, passively receive it.
And then finally, there's another category, which is, You know, you may, not really be receiving data on a network socket or going on reaching it, but you want to provide some kind of drop-in logic to be able to parse a custom file format. And so that's another category. I think something that's open to discussion, on… on that last topic on file receivers, is… you know, exactly how we would want to implement this. Like, is it that the WASM host, which is, you know, that's native and that's in Rust, does that thing… is that thing the file receiver, and then just, like, it knows… it is, like, the native file receiver, and it knows how to call in a WASM, or is there a separate, like, special, you know, built-in first-class file receiver that's completely separate and, you know, not related to this path at all, or… Or some kind of mix of the two, so we can… we can talk about that, whoever's gonna be, you know, involved in, Looking on file receivers, but… But yeah, so those are the four, kind of, main… main categories.
And then, kind of, the rest of this is all… all details that I don't know we want to dive into here. It's probably better for Rotland comments.
**Joshua MacDonald (Microsoft)** 20:18 Yeah.
Thank you, Erin. I did read this, last week, and it looks great. I'm really happy to see it.
So, everyone take a look.
Alright.
On the agenda was nothing else except I had gone through some of our open, issues that are a little bit older. I wanted to check in with people about… A few that are open.
I see we still have Albert.
Allow it, unfortunately, we don't. These may not… This… this was one that we covered earlier. We shouldn't look at it again, sorry.
I wanted to see if anyone knows why the performance tests are broken. That would be nice to know. We don't have to do that here.
**Jake Dern** 21:15 Hey, sorry.
Real quick on that last one, the centralized transport optimized ID Guard, I missed the first couple minutes of the meeting. Was there, like, a conclusion on this one?
**Joshua MacDonald (Microsoft)** 21:24 Awesome.
**Jake Dern** 21:24 trusted in it.
**Joshua MacDonald (Microsoft)** 21:26 Mainly, I wish that I could get a time where Lalit would be here. I think the afternoon is hard for him, so, we might not get this today.
**Jake Dern** 21:34 Sure, no problem.
**Joshua MacDonald (Microsoft)** 21:36 And I haven't looked through it.
So, some sort of guard for the transport encoding, that makes a little bit of sense to me. I haven't looked at the details.
**Jake Dern** 21:51 Yeah, I think there's just been, like, two, well, there's been at least two attempts at it. I think one by a, like, first-time contributor, maybe, and then Ben's recent one. I kind of left a little, like, comment at the bottom.
Just talking about, like, how we want to deal with this case, since there's not really an obvious, I guess, like, failing to decode transport optimized IDs before creating the view, in most cases is kind of a programming error, rather than something we need to handle dynamically.
So that, that was something that I wanted to, to discuss if possible, but, yeah, while it's not here, we can…
**Joshua MacDonald (Microsoft)** 22:26 Got it.
**Jake Dern** 22:26 We could definitely follow up later.
**Joshua MacDonald (Microsoft)** 22:28 Alright, we will leave that open with needs discussion.
Oh, hey, I see a new face.
Everybody, let's say hi to Noah.
Yeah, maybe new to a few of us, but I think a bunch of Microsoft people know Noah, so welcome here. Thank you.
I saw that, you had a pull request open.
you know… As far as, Albert's waving, nice to meet you. So, Noah's gonna join our team, and so, a new face, but also a new contributor, I think, coming soon.
Hopefully, it's great.
So we've actually gone through basically all of this stuff, I don't know if we really need to do this other one without Lalit, and I was gonna say, since there's, still at least half an hour here, and I see the attendees list, we might want to take a look at the open pull requests, which would also cover, NOAA's open PR, but I also see Pierre here, has a couple, and I'd like to get a chance to speak to people about their open PRs.
So, I never know which order to go in.
I think, since I see Pierre here, and there was some enticing PR, title here about an allocation-free single pass, those are all good words for me.
Would you like to speak about it?
**Pierre Mariani** 24:03 Yeah, sure, hey, hey everybody. So, Josh, this is actually, from a issue that you opened some while back. It's the… 2883 here, it's literally the… The words are the title of the issue.
I'm a… yeah, for everybody's context, I'm a very, very new contributor, so I was looking for something open that would also let me, I learned some of the fundamental data structures.
So I found that. So… Yeah, so the issue is about, improving the performance of the num items, for the, Hotel, bytes.
The first PR I opened is just enabling some extra tests that I felt I needed to create to understand what was going on and test the three types of messages and signals that we're sending.
And then the second issue is the actual implementation.
there was a, interesting and challenging, co-pilot comment on the implementation PR, and it worries me a little bit. I'd love for, you know, experienced people to look at it. Yeah, if you can, exactly.
I'll probably let you read it. It's as quick as me saying it.
**Joshua MacDonald (Microsoft)** 25:41 That's done.
Got it.
So you're talking about this comment here.
**Pierre Mariani** 25:56 That's right.
**Joshua MacDonald (Microsoft)** 25:58 I think I would agree, without spending any more time on it, that the meaning of a one-off is you will not see more than one value, and the gRPC protobuf library kind of prevents you from doing that. So, in a traditional protobuf environment, you would never see that, and I'm okay with it. Did you get my…
**Pierre Mariani** 26:18 Awesome.
Awesome. Yeah, so that was really the, you know, the most, risky part of the review here. I've also run the… benches performance, I'm, you know… I mean, I clearly saw that.
the resource would move all over the place, you know, as many times I would run it, so I don't know, you know, I've done my best in, isolating my environment and keeping my books pretty quiet, while this was going, but, you know, let me know if I can do more, in, In validating the change set.
**Joshua MacDonald (Microsoft)** 26:58 Great. I will take a look. This looks really good. Since I'm the one who filed the issue, I now recall it very well.
Yeah, I would say, this is a worthwhile special case. I haven't looked at how much code it takes yet, but this is basically the idea that if you're gonna count OTLP points, you can, skip the heavier weight view abstraction, which we use.
In the, in the common case, we'll say.
**Pierre Mariani** 27:31 Yeah, yeah, that's… that's what's happening.
Awesome, well, thank you so much for taking a look.
**Joshua MacDonald (Microsoft)** 27:37 Yeah, I'm gonna catch up with code reviews for sure by the end of the week, but I will take a look at this one tomorrow, I think.
**Pierre Mariani** 27:44 Thank you.
**Joshua MacDonald (Microsoft)** 27:46 Cool, so let's see, Noah, did your change merge? Let's check the… check in on…
**Noah Falk (Microsoft Corporation)** 27:50 biz?
**Joshua MacDonald (Microsoft)** 27:51 Very good.
Yeah, so I should take away the draft. Sorry, I should have done this first.
And anyone else here want to talk about a PR they have open?
Lots of code reviews to do, folks, here.
I have this feeling that not everyone likes the Friday… the 4 o'clock time slot, so we might want to talk about whether that's still working for people.
Since there's a number of people that I wish I could see sometimes in these meetings, and they… I think are having trouble with the slot, so… It is something we could discuss.
Anybody who wants to review? CJ did that one. Let's see… as you see, I'm running out of topics here. Would anyone like to propose anything else for the agenda?
**Drew Relmas** 28:59 We do have some of the extension work being done by Blangee, but I also think he's not, here today. Aaron, you have your hand up.
**Aaron Marten** 29:10 Since we have time, one, like, kind of… pet thing that I like to go back to is, if you go to issues, look at the flaky test tracker at the top. I made some revisions a few weeks ago, to kind of repair it, because it fell into a broken state. Oh, great! It's performing clean right now!
That's great. If you look at some of the recent edits that have been made by the action that runs the report, you'll see that there probably are some flaky tests that just haven't gotten caught recently, and so therefore, because it's only looking back at 50 runs.
Okay, so… So just… I would just remind everybody to please keep an eye on this issue and take a look at it from time to time to see if there's, you know, tests that are in areas you typically work on that may be in need of repair.
**Joshua MacDonald (Microsoft)** 29:59 And you say to look at the edits,
**Aaron Marten** 30:02 Yeah, if you go to the top of the issue, there's a little drop-down menu. See it says Last Edited by GitHub Actions in the upper right.
**Joshua MacDonald (Microsoft)** 30:10 I see.
**Aaron Marten** 30:11 So it does run every night and tries to analyze it, so you'll see if, you know, there have been… yeah, there have been tests in there, and I'm sure those are the, you know, there's… it's usually timing issues, right? The tests are not as deterministic as they could be, and so they fail.
**Albert Lockett** 30:29 I think, that would fix that Catholon.
**Joshua MacDonald (Microsoft)** 30:35 Thank you, Aaron. I did look at this earlier today, and, at least knew it was going to be clear.
Very good.
So, Drew mentioned, Blanche's… Well, it's on the second page, which makes it hard to see, of course.
**Drew Relmas** 30:52 There's this one, and then 4077 right there.
**Joshua MacDonald (Microsoft)** 30:56 This one, I'm looking at 477.
**Drew Relmas** 30:59 Yeah.
**Joshua MacDonald (Microsoft)** 31:00 I don't know which one this one was.
**Drew Relmas** 31:03 Yeah, this is correct. I think this is, the one. So, if you open up the files changed, I guess we can just briefly talk about it. I have taken… A small look, but this, Essentially, there is a lot of baked-in code in a few of the exporters that were using, some of these capabilities, and he's trying to extract it all out. I'm afraid that I'm not the best one to talk about what's actually happening. I guess Ukarsh has been working on it a lot. Camila, is there anything you'd like to say, or you're just waiting for the review cycle to kind of continue on this?
**Camila Valdebenito** 31:46 Yeah, unfortunately, I… this is, like, on my to-do list to review this one. I just reviewed the previous one, but I agree that it'd be really nice to have… Maybe Josh take a look, when you have time, as this could be, used, or… as Utkarsh mentioned, like, this might be something that F5 might be interested in.
But I should be taking a look today.
**Utkarsh** 32:22 Yeah, so I was, since it's touching OTLP exporter, like.
I can review it, I think, Flanche has been addressing the PR comments. I haven't checked the latest state of the PR, but yeah, since it's touching OTLP Exporter, like, I'm not sure if Laurent wants to take a look before, We decide to merge.
Whenever that… that's ready.
**Joshua MacDonald (Microsoft)** 32:48 We need some more, approvers first. I will take a look at this tomorrow.
I have seen it.
I would appreciate having more reviewers, just across the board, but we'll get this one in as well.
**Utkarsh** 33:02 No.
Yeah, and I think the major reason for changes in a lot of exporters is because a new method is being added to a trade.
So… Yeah, every, exporter or, like, node which was implementing that rate for the Extension capability has to now include that, so there's a lot of… Not if code added because of that.
**Joshua MacDonald (Microsoft)** 33:28 Right.
Okay, well, I think we shouldn't review it here and now.
Very good. Let's see… I think we've reached the end.
Lots of work to do, but I don't know that there's anything more to discuss about the open PRs.
I see one thumbs up. As you all know, I like it when a meeting ends early.
This might be our chance.
**Drew Relmas** 34:04 Sounds good.
**Joshua MacDonald (Microsoft)** 34:05 Okay, go do some code reviews, everybody, instead. You have 25 minutes.
Here, cheers.
**Noah Falk (Microsoft Corporation)** 34:13 Hey, well…
**Albert Lockett** 34:13 Right.
**Pierre Mariani** 34:14 Thank you.
