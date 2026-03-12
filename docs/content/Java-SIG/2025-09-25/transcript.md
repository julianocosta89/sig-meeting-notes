SIG: Java SIG
Date: 2025-09-25
Duration: 58 minutes
Zoom Recording URL: https://zoom.us/rec/share/9dxtg7dsQwCSZfT8Rw_q9Lkygtm1sljKjj6WB4KX5FhJ5vXs0GSZZD0A350YYx8S.9Re1gFHfUK2rQndu
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 01:20 Hey, early birds.
**John Watson** 01:28 On Time Birds, I think I call us.
**GZ Gregor Zeitlinger** 01:36 Huh.
**Trask Stalnaker** 01:38 Indeed, indeed.
**Jason Plumb** 02:10 Trask, I still haven't looked at the extended attributes.
PRs yet.
I said I would last week.
**Trask Stalnaker** 02:17 That's right. And here we are. Alright.
And around we go.
I thought we could start… the meeting chatting a little about… about issue triage in general. I noticed, Jay and Sylvain have been, Doing some great work, like, putting some effort in there, and just wanted to see what, We can do to support that work, or continue that work, or broaden that work.
Definitely an area that we have… neglected the backlog of, I think… We have been pretty good at Triaging new stuff that comes in.
But there is quite a backlog of both PRs and issues.
So, I don't know, Jay… Sorry to put you on the spot, but any, what… how… what has been your… I think, I've seen you going through some old issues, and Sylvain going through some old PRs.
Both super useful.
But what if you're… Thoughts, Ben?
**Jay DeLuca** 03:52 I'm glad you brought this up. I actually had some thoughts, and I was… that I wanted to talk to you and Lori specifically about, because I think that there's… there's a lot of… or not a lot, but there's definitely a category of issue or PR where there's some ambiguity around,
**Jason Plumb** 04:09 Just, like, some decision being made.
**Jay DeLuca** 04:11 around them, and I don't know if it would make sense to… to tag them in some way, or… or research them. One thing that I was thinking was.
like, I'd be happy to create, like, a thread a week or something in our, like, back channel, and kind of tag people there, if it would make more sense to have discussions there, or, you know, if we want to keep everything in GitHub, we can do it there too, but… Yeah, I think Sylvain also brought up the idea, or the topic of some additional automation. I think… There was some… something that said something somewhere around… like, if a new feature request issue was open for more than a year without any movement or something, we might, you know, close that as well. Because there's certainly a lot of those, of, like, the contribution welcome.
But, you know, if somebody's gonna actually pick it up is… who can say?
So yeah, I don't know if it would make sense for us to do, like, a weekly… triage set… triage session or something. I'm certainly trying to… Figure things out as much of my own, instead of berating you guys with all the context, but… Yeah, those are my thoughts anyway.
**GZ Gregor Zeitlinger** 05:27 I think we had, had a session going a year ago, or was it even more trash?
We've tried…
**Trask Stalnaker** 05:37 Yeah, we've gone through fluctuations over the years of, like, we'll get some energy and start tackling the backlog, for a little while, and… It's great, makes some progress.
But then, yeah.
So anyway, I felt like this was maybe a new wave, like, capitalize on this new wave of, energy to get, another, Effort going.
**Jay DeLuca** 06:08 Yeah, I've been… at least the past couple days, this week, I've been trying to spend a little time each morning, But yeah, there's just some things that I don't have the context for, at least yet, so…
**GZ Gregor Zeitlinger** 06:21 So, I like the idea of, Starting a thread in our, Channel, if there's something that, might be interesting, and then, then we can start a discussion. I think we didn't try that last time, but, We were more cleaning… having the meeting to clean up things instead of going deep into discussions.
**Trask Stalnaker** 06:53 Yeah, it would also be, I mean, Jay, feel free to, like, if you… Pull out, you know, 3 or 4… issues that, and throw them on the weekly SIG agenda.
is… I think it's a great use of our time here.
Duh.
**Jay DeLuca** 07:17 Cool.
**Trask Stalnaker** 07:17 chopped through.
**Jay DeLuca** 07:19 Yeah, I think that's a great idea.
**Trask Stalnaker** 07:22 I think where we struggle here is… If I just come in randomly and start to do it in the meeting, we struggle, but, like, if you… Kind of… I can… queue us up with some good discussion topics that would… Be awesome.
**Jay DeLuca** 07:46 Yeah, definitely.
**Lauri Tulmin** 07:47 I think a lot of those issues are… Some sort of feature requests.
Obviously, some of those features are such that we probably have, like, no intention to ever implement them.
For those, I think, the best course would be to tag them with something, I don't know what was it that, got auto-closed after a year?
**Trask Stalnaker** 08:16 Yeah, I like that, for… Yeah, cause, I mean, you're right, there's a lot of things that… You know, we would accept a contribution for, but nobody's, like, proactively Gonna implement it.
And so…
**Lauri Tulmin** 08:34 And for others, like, if you want to help out, then, well, just implement the stuff that is being requested, or help the user debug the issue.
**Trask Stalnaker** 08:47 So, Jay, maybe, that, automation, I think Lori and I would both support an automation… For issues that are… Enhancement and contribution welcome that doesn't have any activity on it in the last year.
Auto-closing all of those.
**Jay DeLuca** 09:14 Yeah, I can do that.
**Trask Stalnaker** 09:15 With, you know, a nice message that's like…
**Jay DeLuca** 09:17 Yeah, of course. Yeah. If somebody wants to do this…
**Trask Stalnaker** 09:21 Yeah.
**Jay DeLuca** 09:24 Yeah, there's uncle.
**Jason Plumb** 09:25 I think there's another class of issue that I keep seeing, which is people that come in, and they have a, like, they're trying to do something, and they have a genuinely good question, and it ends up being, like, kind of complicated.
like, the answer, or what they're doing, like, maybe they're not clear, or we're… we have gone back and forth a little bit, and then it stalls out, and I'll… like, a lot of them, too, is even just someone asking a question, and it hasn't been answered.
I think there are fewer and fewer of those these days, but, like.
they'll ask a question, then I need to come back to it, so… sorry, I'm getting a phone call.
**Jay DeLuca** 09:59 Yeah, I think I saw one of those similar ones even this morning, where I think… I forget which one it was, but the end of the discussion with Lori basically pointing out, like, what could potentially be done about it, but mentioning that it was, like, probably more work than is worth.
And at those, like, I don't know if I should say.
like, author feedback required for something like that? Because, you know, it's more maybe on us to decide if we want to actually do it, but yeah, I think some of them are, like, rabbit holes, for sure.
**Jason Plumb** 10:31 And there's, like, some archaeology on some of these, too, like, they'll ask a question, but it's, like, 2 years old, and I'm like, I'm pretty sure that that was implemented, or I'm pretty sure we fixed that or changed that, and sometimes it's just a matter of, like, asking again, like, hey, it's been… 18 months, 24 months, is this still a problem for you? And a lot of times, the people have just gone off to do other things, and it's actually not…
**Lauri Tulmin** 10:52 important to them. I'll ask whether this is still a problem, and tag it with, I need author's feedback.
**Jason Plumb** 10:59 I mean, that is a good… it is a good strategy for helping reduce these, like, it really does work.
**Trask Stalnaker** 11:04 Yeah, and it gives people a way to basically, like, opt out of, like, oh, like, I don't really care, I'm just not gonna do anything, and then it gets auto-closed.
Yep. Because they do get pinged on it.
**Jason Plumb** 11:19 But if they do still care after two years, they can chime in and be like, oh yeah, I hate this, I'm dealing with it every day still, and I wish you guys would fix it. Like, you know.
**Trask Stalnaker** 11:28 And we see both. I've seen both of those when I… done that before. Yeah.
But yeah, that's a really good, yeah, good point, Laurie. That was one of my major strategies in the prior waves of… Bringing the backlog down.
**GZ Gregor Zeitlinger** 11:54 So, overall.
Would it really make a difference if we close all issues after a year, regardless of, the labels?
I mean, we are not missing pucks for a year, and if we do, then it's probably not An important one.
**Jason Plumb** 12:13 Well, I don't know, the Groovy one was definitely open for more than a year.
**Jay DeLuca** 12:18 But no activity on it.
**Jason Plumb** 12:20 I mean, it's true, yeah.
Yeah, a year of no activity, it is interesting.
**Trask Stalnaker** 12:41 Yeah, like, here was an example where we, Kind of tagged it. They came back.
Probably we could add… That also, like, if it needs… re… if we've tagged it needs repro for some period of time, probably doesn't even need to be a year.
Cause it's kinda like… Author feedback, Needs author feedback.
**Jason Plumb** 13:19 It's kind of a subset of that, really.
**Jay DeLuca** 13:22 Yeah, I'd be tempted to throw the needs author feedback right on this one.
**Trask Stalnaker** 13:27 Having that.
**GZ Gregor Zeitlinger** 13:28 It would be, beneficial if it has an earlier deadline, like 2 weeks, because then there's a higher chance that the, a thing can actually be reproduced. After a year, you usually have no… Idea how to do that.
**Jason Plumb** 13:48 I mean, 2 weeks, though, Europeans are just coming back from their 3-week vacation, they, like, you know, forgot what they were writing about… Too bad, then they just have to reopen it. I mean, there's probably some middle ground there.
**Trask Stalnaker** 14:09 Yeah, that… that would be one… Kind of on my wish list, when we auto-close something, would be, to… Tell them that they can do, like, slash reopen.
To reopen it, because they actually don't have permission to reopen it, the author.
So all they can do is comment on the, like, if… it's something about, like, if… I don't know if… automation closes it, if that's the same, but I know, like, if a Somebody with right permission… well, it should be the same.
Closes it.
The author doesn't actually have the reopen button.
**Jason Plumb** 14:58 I did not know that.
**Lauri Tulmin** 15:04 Yeah, I think I also have replied to a bunch of those issues that feel free to reopen and close it.
**Trask Stalnaker** 15:12 Yeah.
**Jason Plumb** 15:13 It never feels good, though.
But… Yeah.
**Trask Stalnaker** 15:20 On a single case, Like, it's tough, but, like… For the broader health, Yeah.
It's a good thing.
And makes people… like, I think when people see… less issues. They have a little bit more confidence that if they are putting in an issue, and putting in the time, and responding to questions, and providing repros, that… They will get… better support.
**Jason Plumb** 15:56 Yep.
**Jay DeLuca** 16:01 Cool, so just taking some notes. So, I'll look into some automation to auto-close issues for after one year for the new feature request type tags.
I'll add one to auto-close if… A needs repro, tag is on there, maybe for, like, give them 1 or 2 months?
And then, do we want to also include… auto-closing PRs, if they're a certain age.
Regardless of tags.
**Trask Stalnaker** 16:38 What's your thought, Lori, on PRs?
**Lauri Tulmin** 16:47 I think we've probably gotten close to him.
**Trask Stalnaker** 16:54 So, yeah, maybe, PR with no activity… Or… 3 months.
**Lauri Tulmin** 17:05 I guess, like…
**Jason Plumb** 17:07 crap.
**Lauri Tulmin** 17:08 actually that many PRs, like, if we'd, like, manually go through them once and close most of them, then we'd be all set for… For an extended period of time.
**Trask Stalnaker** 17:21 The thing I like about Doing it via a bot.
Is the user… like, it feels a little less personal to the users.
Than having an individual person say, hey, we looked at your PR, and we don't want it. It's just like, hey, nothing personal, this is… Just a bot policy.
Yeah, I would say something, just no… no activity.
You know, this one has been open for a long time, but there's activity.
If there's no activity on it for… I don't know, throw a number out, and we can debate the number on the PR.
**Jay DeLuca** 18:10 Sounds good.
**GZ Gregor Zeitlinger** 18:13 CollectorContrip has this, I'm just checking, I think it's 2 weeks, but I have to double check, and they have had this for a long time.
**Trask Stalnaker** 18:28 I'd vote for a little longer, but… We can…
**GZ Gregor Zeitlinger** 18:32 Yeah, 14 days, I just found it.
**Lauri Tulmin** 18:38 But anyway, again, it would be more productive, generally, if somebody had the time to work on those PRs.
And help the auteur of the PR to… Get it successfully merged.
**Trask Stalnaker** 18:55 Are there certain… yeah, I mean, so that's a good… Question, are there some of these that we are… interested in… Enough to sort of… Push to revive them… Oh, the other thought for Jay, for the automation is, maybe not just auto-closing right away, but putting… marking them stale first.
**Jay DeLuca** 19:29 Yeah.
**Trask Stalnaker** 19:30 Just to give users, sort of, that heads-up that, hey, this is coming, and that might trigger some reinterest from Some of them to try to get it.
**Lauri Tulmin** 19:43 I guess one option would be to add this, needs water feedback label.
**Jay DeLuca** 19:51 Oh, automate the addition of that label.
**Lauri Tulmin** 19:54 Something like that.
**Jay DeLuca** 19:56 Which would then automatically close the rest, or close them after.
**Lauri Tulmin** 20:00 Yeah, I hope so. I hope that it closes.
**Jay DeLuca** 20:04 We can find out how to fix it if not.
**Trask Stalnaker** 20:06 Yeah.
I think it does. I do think there's a little bit of a diff… Needs author feedback.
Sounds like we're asking a question…
**Lauri Tulmin** 20:22 Well, then you probably would need to add some sort of comment, like, hey, are you still planning to work on this? And then add a need sort of feedback label.
**Trask Stalnaker** 20:31 Yeah, yeah, instead of stale, so do… it's basically a stale bot.
But use the needs author feedback instead of stale.
I like that.
Cool. Alright, some good, good ideas.
Let us… move on. We've got, some… topics, So, I just wanted to throw these, I ended up going down some rabbit holes over the last week, kind of around the unsafe usage in the core repo.
Specifically… this, spurred on by this.
issue.
And… so… it does… the good news is that the core repo seems fine, like, there is not gonna break. There are, as Jack says, there are fallbacks in place.
And, I was able to get all the tests running, passing with, this JVM option. Thanks, Jonathan.
That was some hackery, because some of our tests Only dependencies don't support it yet, so, like, the… workflow, builds, Armyia and Protobuff locally, patches them, and uses those snapshot versions when running the tests.
**John Watson** 22:25 Yeah, that gives me the heebie-jeebies, by the way.
**Trask Stalnaker** 22:29 That's fine, you don't have to merge this, I mean, you… you… at least it's separate?
It's a separate workflow, right? So it shouldn't affect anything else.
**John Watson** 22:45 So we're not, we're not shipping patched versions with this?
**Trask Stalnaker** 22:49 Oh, God, no.
**John Watson** 22:50 Okay, okay, I feel better about it.
**Trask Stalnaker** 22:53 What I…
**John Watson** 22:53 I look through this, and I'm like, what's going on here? Are we patching our Marriott dynamically as a part of our build process, and then shipping that? I'm like, yikes!
**Trask Stalnaker** 23:03 Yeah, no, these are test-only dependencies.
**John Watson** 23:07 Okay.
**Trask Stalnaker** 23:07 Which is also why, like, because if we had to patch real dependencies, then that… then that would not show that our SDK was…
**John Watson** 23:21 safe. Do we know… do we know if Armaria has work in progress to get The dependency broken?
It's so…
**Trask Stalnaker** 23:33 No, I looked… I did not…
**John Watson** 23:37 None.
I know… I know Anarag has… Honorag has a lot of, close connections with the Armaria team. I wonder if we can get him to nudge them to…
**Trask Stalnaker** 23:51 Yeah.
**John Watson** 23:52 Sort of.
**Trask Stalnaker** 23:53 I can open an issue over there, for sure, to get that ball rolling.
At least.
**John Watson** 24:03 Because it feels like that's… that's, like, the better long-term solution, right? It's like, just let's get the dependencies that we need here.
**Trask Stalnaker** 24:09 Sorted. Yeah, yeah.
**John Watson** 24:14 Cool, awesome.
That's right. Our Mary, we just use as, like, our server for backend, for some testing, right?
**Trask Stalnaker** 24:24 Yeah.
**John Watson** 24:25 Alright, I was trying to remember. I didn't even remember why we had that in our project at all in the first place, but yeah. Protobuff is a bigger deal, though, right? Or is that only still used for testing?
It's only used for testing, which is fantastic.
**Trask Stalnaker** 24:37 But they do have an issue up… upstream.
**John Watson** 24:42 Yeah, I think I saw it.
**Trask Stalnaker** 24:44 Yeah, I think Jack linked to it.
**John Watson** 24:47 Yep.
**Trask Stalnaker** 24:51 Here, yeah.
Cool.
**John Watson** 24:57 run into this… so, you know, we publish protograph bindings in that… Whatever the OpenTelemetry, Java.
Proto repo, I think is what it's called? ProtoJava? ProtoJava. Do we have an issue in here for the same thing? Because obviously that's going to be… Ended up being a problem, right?
**Trask Stalnaker** 25:20 Yeah, we don't, but…
**John Watson** 25:25 Also true, also fair, also fair.
**Trask Stalnaker** 25:29 So, I don't… Somebody's gonna…
**John Watson** 25:30 Yeah, yeah.
**Trask Stalnaker** 25:32 Yeah, yeah.
But we can just point them upstream, and I think it will… Get taken care of.
**John Watson** 25:38 resolve itself eventually, yeah. Fair enough. Okay, cool.
**Trask Stalnaker** 25:47 Let's see… So… Oh yeah, so one of the things that was interesting in that issue… The unsafe issue is that people think that we're gonna break.
in Java 26, because the JVM logs this warning.
Even though we catch the exception and we do the fallback.
But the JVM still logs the warning, and Lori, when he did implemented the, the string encoding using unsafe.
added a, JVM version, a Java version check.
to not… use unsafe on, I think, Java 23 and later, when that, Warnings started getting logged, which was clever, and so… I was originally planning To just do the same thing here?
Or I guess 22 plus? I forget.
But then, given that the benchmarks for this other safe implementation of, JC Tools.
At least in our usage.
The benchmarks seem fine, and so, seems worth just simplifying And using that.
only. We could go back. My initial… if you look at my initial commit, before, always use SafeQ.
Did the fallback… Yeah.
Kept the fallback to the unsafe version.
But then, given the benchmarks, thought it might be worth just simplifying.
**John Watson** 27:50 Do you have any feeling why those benchmarks are so… excuse me, so noisy, especially on the… Zero delay… zero delay?
Hardware? Hardware issues, or… Like, the plus 26% seems bad.
But you said you saw a lot of… it was… very noisy.
**Trask Stalnaker** 28:12 Well, actually, plus 26 is good, because it's operations per second. Oh, well, the minus… minus 8…
**John Watson** 28:19 Whatever. Right, right.
**Trask Stalnaker** 28:21 Yeah, yeah.
**John Watson** 28:22 It was quite noisy, though, right?
**Trask Stalnaker** 28:25 Yeah, in both directions, I've seen… I've seen it, yeah.
**John Watson** 28:29 Is this running on your laptop?
**Trask Stalnaker** 28:32 No, this is, so this is another, Add option to run benchmarks on PRs.
So, all of these are from… the Oracle benchmark. It's a bare metal, box in Oracle Cloud that we have access to in OpenTelemetry for running benchmarks.
So this… I basically cherry-picked this.
Pr into all my other PRs to be able to run them.
But it… runs the benchmark on the PR, and then it checks out main, and runs the benchmark on main, and then attaches those results, to the run.
**John Watson** 29:28 Well, that's interesting, it's running on bare metal, it's… I'm surprised it's so noisy.
**Jason Plumb** 29:37 That doesn't, preclude you from having noisy neighbors on the same physical host.
**John Watson** 29:42 Well, well…
**Trask Stalnaker** 29:44 I think it is a bare metal.
**John Watson** 29:45 It's not bare metal anymore. It's a virtual… that's virtual metal, if there's other… other things on your same host.
**Jason Plumb** 29:53 There's certainly other processes running.
**John Watson** 29:56 Sure… but ones that are gonna have that much CPU impact? Like, that seems surprising to me.
**Jason Plumb** 30:05 Yeah.
**Trask Stalnaker** 30:10 I mean, I can try running them on my… Laptop.
It… doesn't… I've spent so much time in my life trying to, make noisy, microbenchmarks.
Not noisy, but I kind of just… as long as I see a good amount of fluctuation one way or another, I mean, like, sometimes the JIT decides to optimize a different path.
I don't know, there's some… I've kind of given up on that dream.
But I can definitely run it locally and, see if I get fluctuations.
**John Watson** 30:57 I'm not… I'm not opposed to this, I'm just… I was just… some commentary, I'm just kind of a little bit surprised that there's that much variance from run to run.
**Trask Stalnaker** 31:06 Yeah, it is interesting.
**John Watson** 31:07 But there isn't on the ones with delay, like, those ones are super.
**Trask Stalnaker** 31:10 Yeah.
Yeah, yeah.
This is worth… Taxing it a lot more.
I guess.
Let's see… My goal was just to kind of give an overview here and answer any questions that folks have.
**John Watson** 31:34 I swear that one, so… Oh yeah, but the Android had comments on it.
**Trask Stalnaker** 31:39 Yeah, because this, the reason why I'm kind of… I brought this up in connection to the unsafe stuff is just that as… were making change… I know that part of this was around dealing with our access of unsafe And so, wanted to make sure that my changes to use, like, a different JC Tools implementation.
Really my concern was around the JC tools, because Previously, it would fall back to Array Blocking Queue.
But now I'm not falling back, I'm just only using the safe version of the JC Tools.
Q.
And so… I want to know that that is Android.
compliant, the JC Tools… Implementation is Android compliant.
And we…
**Jason Plumb** 32:41 That's.
**Trask Stalnaker** 32:41 it just… Yeah.
**Jason Plumb** 32:45 Go ahead.
**Trask Stalnaker** 32:45 Yeah, we used to just include… all… JC Tools from Animal Sniffer.
Which made me nervous, because I'm like, okay, but wait, now I am using JC Tools for Android.
But then, I tried to remove this, and… It's still passed.
So, I don't know, Jason, if the… Easiest, like, is there a way on… Basically, this PR is the one I'm worried about.
Can we test, verify on Android?
**John Watson** 33:33 I mean, it's gonna vary by Android version, though, also, right? Which is the… what makes Animal Smither useful.
Because depending on what version of Android, you have different support for different Various things.
What's the oldest version OTel Android supports, Jason?
**Jason Plumb** 33:52 Why would you ask me that? I think it's API 21, I think is what we say.
**Trask Stalnaker** 33:58 I thought we bumped it to 25. Let's see.
We're documented.
**Jason Plumb** 34:04 Yeah.
**Trask Stalnaker** 34:13 Split the difference.
**John Watson** 34:16 The average of your opinions.
Hey, they say if you, ask enough people a question.
**Jason Plumb** 34:27 And I think that's based entirely on the minimum version… that AGP supports, I think?
**Trask Stalnaker** 34:34 Yeah.
**Jason Plumb** 34:36 Oh yeah, okay.
**John Watson** 34:41 So as long as we can verify that it works on 23 plus… 23, then we're okay.
But I think, Jason, your question was good… a good one on the other PR. I was like, can… is there a way we can just verify that Animal Sniffer is even running?
Like, you could add to that PR something that we know violates And verify that it fails.
**Trask Stalnaker** 35:10 Yeah.
**John Watson** 35:10 a handy test, although I don't even know what validate… what fails validation these days in Android.
**Jason Plumb** 35:17 Yeah.
**John Watson** 35:24 I've been out of that world for… A while now.
**Trask Stalnaker** 35:34 Okay, so on this one…
**John Watson** 35:40 It may be that the de-sugaring has gotten good enough on, even on 23, that these things aren't even problems anymore.
And that the animal sniffer library has already accounted for all that. So it may be that… that may be a valid result, that we don't have to worry about it anymore, but it would be nice if we could find something that does violate and verify that we actually do fail.
**Jason Plumb** 36:04 Agreed.
It's a good idea.
**John Watson** 36:09 Write a failing test.
Then fix it.
**Trask Stalnaker** 36:21 Okay.
**John Watson** 36:23 Cool.
**Trask Stalnaker** 36:25 We've got game plans.
This is, we talked about last week, as promised, here are… Benchmarks, and my, Creative attempts at something eventual.
Eventual… eventually visible, and how horrible those benchmarks are.
So…
**John Watson** 37:01 I'm… I'm still confused about what these… what the meaning… So I look through the benchmarking code, and I'm still confused about what we're actually measuring here.
Because we're not, as far as I can tell, actually measuring the eventuality. We're just measuring throughput under different circumstances.
**Trask Stalnaker** 37:21 Right.
**John Watson** 37:22 Right.
**Trask Stalnaker** 37:24 So, the eventuality is, if you look, like, it's… This is… the idea of this one is, okay, let's use a non-volatile counter, and every thousand gets, we will, Update it to the volatile. We'll do a volatile read.
**John Watson** 37:48 It'd be interesting, though, to know… under load… I guess it's never going to be a realistic situation, though.
Wait.
**Trask Stalnaker** 38:04 It's just every thousand GET, every thousand…
**John Watson** 38:06 reads. But it may be that the cash value is already, like, is already fine. Like, it may… synchronized, right? Like, you may be doing… you may be doing work here for no reason if it's already been synchronized across threads.
Right.
**Trask Stalnaker** 38:20 We can't count on that.
**John Watson** 38:22 I know, that's why I'm like, it'd be really good if we could figure out a way to actually measure how eventual we're talking about without any of this volatile stuff.
But… I don't think there's any real way to do that.
Not enabled.
**Trask Stalnaker** 38:39 Yeah.
**John Watson** 38:43 Any way that you would do it would probably force the synchronization and make it a… make it a non-valid test anyway.
**Trask Stalnaker** 38:54 So as far as what it's measuring, it is measuring… 100… how long does it take to make 100… reads of that state, that Boolean state.
And I… Designed it this way very specifically to… This is where… Non-volatile access shines.
In a tight loop, because the JIT can just say, okay, I'm gonna read the state once.
And use that value for this whole loop.
Whereas, if it's non-volatile or anything else, it's gonna have to actually make those memory… accesses.
And so we can see… I mean, it's kind of not even fair, like, what, it takes 1.2 nanoseconds?
To, makes me question that it's even… it's probably just optimizing away that loop entirely.
the volatile axis I mean, 74 nanoseconds for 100 volatile reads?
That's… not bad.
To Jack Shirazi's… point last week.
Anybody…
**Jason Plumb** 40:25 For whom that's gonna make a difference.
**Trask Stalnaker** 40:29 isn't using op… Hopefully isn't using OpenTelemetry.
**Jason Plumb** 40:34 Or Java?
**Trask Stalnaker** 40:36 Or any kind of logging library, because as we saw, like, Log4J2 does similar, has a volatile read on… is debug enabled.
**John Watson** 40:50 Yeah, I mean, if you have real-time requirements, you're probably doing something wrong if you're using OpenTelemetry in Java.
**Trask Stalnaker** 41:01 So… so I went ahead and spent, the PR to… Make that one-line change.
Based on the spec, and based on the benchmarks.
I think Jack has other thoughts… So, I'm going to probably ask him to block… I think he needs to block the spec PR.
If he has reservations, Because I… I think if the spec PR goes through, that we should… follow suit. I think it would be… I'd be hard-pressed to justify why we aren't Following spec.
**Jack Shirazi** 41:54 Even that 74 nanoseconds sounds high.
I remember, peter Laurie on the… Chronicle guys doing tests on shared memory, and it was 20 nanoseconds for… Different threads to access the same variable, so…
**Trask Stalnaker** 42:13 This is doing 100 reads.
**Jack Shirazi** 42:15 Yeah, but… Is it… that's per… is that per 100, or that's per read?
**Trask Stalnaker** 42:20 Per 100.
**Jack Shirazi** 42:21 Oh, okay.
**John Watson** 42:25 So only 7 nanoseconds per single read.
**Trask Stalnaker** 42:28 0.7 nanoseconds.
**John Watson** 42:31 Oh, right, 0.7 nanoseconds.
**Trask Stalnaker** 42:34 Now, obviously, if it's just a, as Jack Shirazi says, like, if you're doing a real test of one that's not cached, and you have to, like, go and get it, read it from them, you know, it's probably gonna be slower than that.
But… if I… when I'm measuring a single Yeah, there's probably better ways to measure this. I struggled. The main… the way that I was able to see a difference between non-volatile and Volatile, was to do it in that tight loop, because that's where the non-volatile basically kills it.
**John Watson** 43:13 But again, as you say, it may just be being optimized away.
**Trask Stalnaker** 43:19 Yeah.
Which, non-volatile, it can do, but that might not be realistic if it's buried in, you know, some… enough code paths that the JIT can't… Inline everything and optimize it away.
**Jason Plumb** 43:38 I'm confused by this spec issue on this thing, like, what… this is around declarative config?
**Trask Stalnaker** 43:46 No, I think it's.
**John Watson** 43:47 Around dynamic config, not declarative config.
**Jason Plumb** 43:49 Oh, dynamic config.
**John Watson** 43:52 If you're using an op-amp or something.
**Jason Plumb** 43:55 Trade.
**Trask Stalnaker** 43:58 and logger… the SDK, there's an experiment… it's still experimental in the spec, the enable… logger config enabled.
**Jason Plumb** 44:07 Oh, that's what this is about.
**John Watson** 44:10 Yeah, you want to, like, turn on… turn on logging, turn off logging.
**Jason Plumb** 44:13 Okay.
Okay.
**John Watson** 44:14 You know, running system.
**Jason Plumb** 44:15 And that change needs to be eventually seen by the people that care about it. The places calling is enabled. Yeah, okay.
**John Watson** 44:24 Yeah. That makes more sense.
I think if someone is logging enough that that 7.7 nanoseconds read is going to impact them, they need to, think… rethink their life choices about how they're using logging.
**Jason Plumb** 44:40 It wasn't clear for me, like, reading the descriptions and these spec issues, like, where it was coming from, or, like, what the target use case was.
**Trask Stalnaker** 44:50 It's because, you… the Android meeting conflicts with the spec meeting.
**Jason Plumb** 44:55 I know, it doesn't stop.
**Trask Stalnaker** 44:56 a good context.
But that's why we have these meetings.
Proliferate the, context.
**Jason Plumb** 45:08 Yep.
**Trask Stalnaker** 45:11 Let's skip over the remaining ones of mine. We've got more topics.
Patrick.
**patrickpok** 45:21 Yes, hello, mine is a short one, so… finally able to complete it. Many thanks to Laurie for… because this is my first PR, and I really needed help, so thanks to him. So I was just wondering what is the next step? Like, is it pos… like, what is the process? Actually, I'm just curious to learn.
So what is the process? Is it going to be merged, or what should I do?
**Trask Stalnaker** 45:46 Yeah.
**Lauri Tulmin** 45:47 do anything. You should just wait.
**patrickpok** 45:49 Okay, that's something I can do, I'm good at that.
**Trask Stalnaker** 45:54 So, Lori added it to the next release already.
So, and he's approved it.
So, pretty much, I will take a brief Look at it, and… I probably will just click the merge button.
**patrickpok** 46:11 Okay.
**Trask Stalnaker** 46:12 That'll be it.
**patrickpok** 46:13 I think that's a good plan. And just for me, for, like, for the… what is the release cadence? Like, I tried to look in the documentation. Is it, like, once per month, or, like, when is this, like, 2.21 going to be live?
**Trask Stalnaker** 46:29 Yeah, so we do have it here, release cadence. I'll drop it in the, Doc.
**patrickpok** 46:37 Okay, then let me read it.
**Trask Stalnaker** 46:40 Yeah, and it's super clear.
Wednesday after the second Monday of the month.
**patrickpok** 46:48 Okay.
Understood, understood.
**Trask Stalnaker** 46:54 It's designed this way as the, to follow the… core Java repo, so we release on a Friday from the core repo, and then we release the next week from the instrumentation release.
**patrickpok** 47:09 Understood. Thank you so much.
No more questions on my side. Everything is there, thank you.
**Trask Stalnaker** 47:18 Great.
Gregor.
**GZ Gregor Zeitlinger** 47:27 Yeah, this is about, Lyci, since we have started, to, roll out the same Lyci check everywhere.
I thought we should discuss what we do about upgrading Litgy, which is currently blocked, because an upgrade of Lyci actually activates anchor checking, which did not work before.
And activating doesn't work because, GitHub anchors do not work, and this is what this issue is about. I have already spent roughly a day trying to fix this, but this is a little bit more complicated, so we have to decide if we are just sticking with the current version, or we are just, Deactivating anchor checking.
at least this is the choices that I can see.
**Lauri Tulmin** 48:21 If the anchor checking… Doesn't work, as you said.
Then, we don't lose anything by deactivating it, do we?
**Trask Stalnaker** 48:32 It works for non-github.com.
If that makes sense.
**GZ Gregor Zeitlinger** 48:40 This is how it is. Okay, I mixed that up, okay.
**Trask Stalnaker** 48:42 Yeah.
So, we are getting benefit of its checking anchors on ex… other sites.
So my preference is to just stay with the current version, since it's giving us something.
And… Trust that some… hope that somebody… is going to fix this in Lychee at some point.
And maybe it'll be S.
**GZ Gregor Zeitlinger** 49:14 So we're not… We're not nervous about having something that we cannot upgrade, that might have some security problem.
**Trask Stalnaker** 49:24 Not yet. I think I've noticed… you know what I've noticed is, Renovate… Will tell us if something hasn't Had an update in a year, it starts flagging things.
Anyway… At some point, yes, Gregor. Definitely.
**GZ Gregor Zeitlinger** 49:48 I'm not sure at what point… Not to worry about now.
**Lauri Tulmin** 49:53 Would it make sense to run, like, G twice, like, once for GitHub, and once for everything else, or something like that?
**GZ Gregor Zeitlinger** 50:04 Using different versions? Yes. What's the idea?
**Lauri Tulmin** 50:08 No, like, for everything else, you could use the anchor check, and for GitHub, you could just skip the anchor check, as it doesn't work anyway.
**Trask Stalnaker** 50:18 So, two different… essentially two different TOML files, Gregor.
**GZ Gregor Zeitlinger** 50:26 Yeah, or a parameter, yeah. I think that's an idea, yeah?
I like that.
**Trask Stalnaker** 50:32 shock.
**GZ Gregor Zeitlinger** 50:34 I'll see if I can get that going.
**Trask Stalnaker** 50:40 Cool.
Alright, let's move on, Serbi.
**Surbhi Agarwal** 50:49 Hello?
Oh, So my question was regarding whether adding events like such to HTTP spans, is it acceptable? So, while there are metric signals that agents can send to the backend for gathering metrics.
There are separate use cases, like, the backend would want to gather the timestamps and roll up their own metrics in the way they want it to, right? And they probably want to show per request DNS duration, TLS duration, TCP duration, which the metric signals won't allow, right? Because it's not exactly correlated to per request.
So, I… this was, like, firstly specific to the OKHTTP library, which is there in the Java instrumentation repo.
So, if we can add events like such, it can… it doesn't have to be by default. There could be a flag if the customer is interested in enabling this, or the particular agent.
is interested in enabling this, they can enable it, so their backend can understand this, can gather this timing and develop the metrics in the way they want it to.
**Trask Stalnaker** 52:13 Does anybody remember offhand what, instrumentation, we already have some, like, DNS…
**Lauri Tulmin** 52:23 I think it's native.
**Trask Stalnaker** 52:24 telemetry.
**Surbhi Agarwal** 52:27 I saw…
**Lauri Tulmin** 52:29 Or reactor writing, or something like that.
**Surbhi Agarwal** 52:31 I saw for .NET, there was…
**Trask Stalnaker** 52:38 Okay. So these here, for Netty, connection telemetry and SSL telemetry.
**Lauri Tulmin** 52:48 But I believe those crate spans.
**Trask Stalnaker** 52:54 Okay.
**Lauri Tulmin** 52:56 I think it might be, like, because, the way the latest band is created, it, the actual HTTP span might be created after the… DNS and Handshake are already done, and the connection is established.
**Trask Stalnaker** 53:21 So, yeah, so, couple thoughts, Serbi, I think, yes, this is definitely something that, makes sense. The… You.
I would look at what we're doing for Netty already, but also, I would… look… well, for one thing, span event, we're… is… we're moving away from to just events.
So we'll want to do events… Potentially… And also, it would be good to make a proposal in the semantic convention repo, even if it's just opening an issue and sort of making a proposal of what semantic conventions would look like.
For these events?
So that… when you… send a PR, To the instrumentation repo, you can kind of cite that, and potentially people in semantic conventions can chime in. We can… you know, it doesn't need to be… it's not going to be stable, it's just, as you say, it's just going to be an opt-in Configuration parameter initially anyways, but we want to have that connection with semantic conventions.
**Surbhi Agarwal** 54:47 Hmm.
That makes sense, yeah.
So, the events would be an attribute in the span, right? Or separate events are we talking about?
**Trask Stalnaker** 54:59 We're talking about separate… we're talking about log-based events.
**Surbhi Agarwal** 55:04 Okay.
**Trask Stalnaker** 55:04 so, span events is, Going… away, more or less, or we're moving to log-based events in across OpenTelemetry.
So if you look at semantic conventions.
**Jason Plumb** 55:32 There's no timeline that's been established yet for that, is there?
**Trask Stalnaker** 55:37 No.
**Jason Plumb** 55:37 Okay.
**Surbhi Agarwal** 55:41 And this would be related to the span in certain way.
Like, if it is, okay, event-related to this one.
**Jason Plumb** 55:50 It gets spanned context on the event.
**Surbhi Agarwal** 55:52 Okay.
**Trask Stalnaker** 55:55 Yeah, it's sort of like a child of the span, you can think of it that way.
**Surbhi Agarwal** 56:00 Okay.
Yeah, I will create a proposal in the semantic convention repo as well, and in the Java instrumentation repo as well, referring that, and yeah, let's see, we'll take the discussion forward.
**Trask Stalnaker** 56:28 Yeah.
Cool. Thanks.
**Surbhi Agarwal** 56:34 Thank you.
**Trask Stalnaker** 56:35 we're at our time box, but let's just quickly… Profiling signal…
**Jonathan Halliday (IBM)** 56:47 Yeah, that's just a little bit of background and some potential use cases.
At some point, we're gonna have to decide.
Which of those use cases we want to add support to for the… whether it's going in Conchib, or whether it's going in the SDK, and exactly what features we're going to have, and what the API for them is going to be, and things like that.
So, yeah, if there's one of these meetings in the next two or three weeks where there's a lighter agenda, I'll stick something in there to discuss those ideas.
**Trask Stalnaker** 57:20 Yeah, let's just put it on, so we can all… Put that on our reading.
List for this week, and plan on having a… chat about it. Oops, not that.
Next week.
And Gregor, I think you had the last… Topic quickly…
**Jason Plumb** 57:55 Quick 3 minutes, declarative config, go.
**Trask Stalnaker** 57:59 No, no, no, no, no, okay, we're good, we're good. All right.
**GZ Gregor Zeitlinger** 58:05 This was just in the hope that if we had had time left.
**Trask Stalnaker** 58:09 Yes.
**GZ Gregor Zeitlinger** 58:10 So, all good. Don't, don't panic.
**Trask Stalnaker** 58:16 Okay, thanks all.
**GZ Gregor Zeitlinger** 58:19 See you!
**Jay DeLuca** 58:19 Y'all later.
**Robert Niedziela** 58:20 Video, mine.
**Surbhi Agarwal** 58:22 Thank you, bye-bye.
