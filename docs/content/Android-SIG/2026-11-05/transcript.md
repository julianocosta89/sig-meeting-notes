SIG: Android SIG
Date: 2026-11-05
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Jason Plumb (Splunk Inc.)** 01:39 Hello, everyone.
**Jason Morris** 01:49 Hello.
**Jason Plumb (Splunk Inc.)** 02:04 Give it another minute or two.
Please feel free to add anything to the agenda that you'd like to talk about, because it's wide open right now.
Hey, hey!
We have a completely open agenda, so if anybody has any pet topics they would like to… Bring up.
Discuss?
We're here for it.
Alright, I have work to do over here, because I need some ContribFest from Android as well.
And I hadn't checked until just now.
I guess the only thing to say about that is if you see an issue that's marked ContribFest and you're on this call, please don't pick it up.
Seems obvious, but I'm gonna say it out loud anyway.
**Ben Joseph** 03:58 What is the idea behind it? Like… Who's it meant to… meant for?
**Jason Plumb (Splunk Inc.)** 04:05 Yeah, so it's a thing that we've done a number of times at KubeCon.
And it's an hour-long session where people who have not… contributed to OpenTelemetry at all, ever, can come in and learn how to be a first-time contributor. So within an hour, they leave with a contribution under their belt.
And so we're there to sort of help them, and so we front-load some work of, like, deciding what issues might be a good first issue to work on, and we label them.
So they can find them easily. And… I think it was last year in the US one. We haven't done it every KubeCon, but we've done a bunch of them, and Yeah, I think one time we had, like, 30… 30 commits within one hour. It's like… Pretty good for people that haven't ever contributed to open source before, yeah.
I mean, David, to answer your question, some people have never contributed to any open source, it's their first time.
And they just happen to be at KubeCon, there happens to be at ContribFest.
A lot of times these people are users of these tools, but they've never… either been allowed through their employer, or they haven't given an opportunity, or they're just kind of new to it, and so it's both. Definitely people that are new to OTEL, but certainly some people are new to open source.
Okay.
Well… Does anybody have anything else they would like to talk about? And if not… we can… I can just go through and do a little looking at issues, because I'm behind, and you can hang out with me, or we can just call it.
**Jamie Lynch (Palo Alto Networks)** 05:47 I just added one item onto the agenda, it's basically just to look at the top two issues, so… Awesome.
Yeah, I think… I guess we should figure out whether it's worth shipping a fix.
Shipping and release, but… ship's face fixes, basically. Like, there's two issues that came in.
**Jason Plumb (Splunk Inc.)** 06:08 Cool, yeah, let me add one more. I just thought of one more thing.
Okay Oh, so this is, like, new behavior?
And we've patched it.
**Jamie Lynch (Palo Alto Networks)** 06:28 Yeah, so there's a PR for this, which is linked to the issue, and I think it got merged down today, but yeah, it's basically a desuggering bug.
Where we're using code, but when… If you're not de-sugaring it.
**Jason Plumb (Splunk Inc.)** 06:44 Damn.
**Jamie Lynch (Palo Alto Networks)** 06:45 Yeah, crashes.
**Jason Plumb (Splunk Inc.)** 06:48 Okay, that seems bad, and then… this one's also related, or unrelated? I mean, it's related to the release, maybe, but…
**Jamie Lynch (Palo Alto Networks)** 06:57 Unrelated, but it could potentially leak large objects.
**Jason Plumb (Splunk Inc.)** 07:04 Yeah, let's do a patch release for this, because we just released, right?
I think it's worth doing, these seem bad.
What do y'all think? I don't mind doing it.
**Hanson Ho** 07:17 I should do it.
The duration thing's weird, shouldn't that get flagged by the ID saying, API compat?
I wonder how it passed… everything.
**Jason Plumb (Splunk Inc.)** 07:37 It's a good question.
**Hanson Ho** 07:46 Like, I would recommend blacklist, or, deny listing it, but I thought we have linting to configure that, given our min API.
**Jason Plumb (Splunk Inc.)** 08:00 So the problem… yeah, so the problem was that calling 2 seconds on a duration on lower levels was crashing apps.
**Hanson Ho** 08:12 Yeah, this doesn't exist in older API versions. You have to… the sugar, so…
**Jason Plumb (Splunk Inc.)** 08:19 Which we still have that requirement, right? But we… it's on… it's not on… it's not on 30. It's on stuff, like, below…
**Hanson Ho** 08:26 Yeah.
**Jason Plumb (Splunk Inc.)** 08:27 Okay.
**Hanson Ho** 08:28 But, but regardless, our, the, the agent itself doesn't… we're not… our API checks isn't… This should not have passed our API checks. This should have been flagged. I don't know why this wasn't flagged.
**Jason Plumb (Splunk Inc.)** 08:45 Oh, good, yeah, good, good point.
Do we… Do we know if that runs as part of the… PR?
You know what?
**Cesar Munoz** 08:57 It's true, yeah.
**Jason Plumb (Splunk Inc.)** 08:59 Is it part of PR Check?
**Hanson Ho** 09:04 It… it certainly highlights it for, in the IDE, and I think… I don't know which linting, you know, does it, but something tells me when I screw up and use, like, you know.
concurrent APIs that I can, or whatever it is.
**Jamie Lynch (Palo Alto Networks)** 09:24 Well, good.
I tried pasting it into my IDE, and it didn't show up with a Like, Lynch or IntelliJ warning.
I know that we've got an animal sniffer plugin in this project, which is meant to detect things like that.
**Jason Plumb (Splunk Inc.)** 09:42 Okay.
**Jamie Lynch (Palo Alto Networks)** 09:43 O… Yeah, I'm not sure about that.
Wouldn't get picked up, Paul.
**Jason Plumb (Splunk Inc.)** 09:48 It's… it's a good question. Why… Do we know where it runs?
**Hanson Ho** 09:57 Oh, is it… oh, maybe it's not run on that specific project?
**Jason Plumb (Splunk Inc.)** 10:03 So, yeah, here's our, here's our custom thing for it.
And… but the question is, when is it wired up to builds, right?
So we have a cool definition for it.
Rebuild it.
**Cesar Munoz** 10:17 Hmm… Yeah, Nemo's never plugin should run.
She's part of the… she ran as part of the checks.
Raddle checks, so the plugin itself attaches it to it.
**Jason Plumb (Splunk Inc.)** 10:31 Okay. Yeah, so, I mean, we have it wired up as a plugin for our library conventions, which is, like, everything, so why didn't this get caught?
Can we check the… let's check the build log thing. The… You think it's PR checks is what you were saying, Cesar?
**Cesar Munoz** 10:49 She'll be there, I guess, yeah.
Maybe it's part of the…
**Ben Joseph** 10:58 Should we be checking on this PR, or the change that added it?
**Jason Plumb (Splunk Inc.)** 11:03 I mean, it should run always, right?
**Ben Joseph** 11:04 But, yeah.
**Cesar Munoz** 11:05 Yeah.
**Jason Plumb (Splunk Inc.)** 11:07 So, if this one broke it, I would… I mean, if this one didn't break it, we should see it passing, but…
**Cesar Munoz** 11:17 Yeah, it's very strange.
**Jason Plumb (Splunk Inc.)** 11:20 So, in this one… What is this signature one? I don't know what that is.
**Cesar Munoz** 11:31 That generates the, the, the, like, the set of… I guess, methods that are available, so that Animals and Infer compares that to the codebase.
**Jason Plumb (Splunk Inc.)** 11:45 Okay.
**Cesar Munoz** 11:53 You know, if we have… Define the… our minimum… SDK version, because I think, ideally, there should be two… Like, two layers.
to check this. One is animal sniffer, just to make sure that Stuff that it's… added… after API 23, up until API 26 is covered by Animal Sniffer, but then everything that's added after API 26 should be covered by the native Android Linter or something.
Which I think kicks in when you add the minimum Version.
Minimal SDK version.
**Hanson Ho** 12:38 Yeah, that's the weird part. It's like, there's two things that should have caught this.
That's just fun.
**Jason Plumb (Splunk Inc.)** 12:44 So, but this is a… oh.
Sorry, what… So, this is a 30 API level 31. If you were compiling your app with API level 30, That should be fine.
that wouldn't pass the min SDK, like, that wouldn't… break them in SDK check, would it?
I don't see how the Mint SDK check is relevant there.
**Hanson Ho** 13:10 the min SDK check is defined for the project, so it's saying it should for this SDK. So, when it compiles, it should be like, hey.
I mean, it wouldn't fail the compilation, but it'll… It'd be a violation to say, hey, this compiled binary is not gonna work with, like, 29.
And that should get flagged. It wouldn't be a build error, it'd be… that's why we need the linting. If it's a build error, then we wouldn't have to worry about it, but that's why one of the linters, an animal sniffer, should have caught it.
**Jason Plumb (Splunk Inc.)** 13:43 Yeah, that's super weird that it didn't. I mean, do we have to… I mean, just having the plugin here, do we have to somehow, like.
Depend on or configure the tasks?
**Cesar Munoz** 14:00 No, I mean, there's an Animal Sniffer plugin that should, like, install itself into the… Checks.
Gradle task.
We need to definitely take a look at why this happened.
**Jason Plumb (Splunk Inc.)** 14:14 Yeah…
**Cesar Munoz** 14:17 Really an issue for it.
**Jason Plumb (Splunk Inc.)** 14:24 Yeah, I can do that if you want me to.
**Cesar Munoz** 14:29 Yeah, thank you.
**Jason Plumb (Splunk Inc.)** 14:40 Okay, and what's the, what's the story on this one?
Oh, leaked objects, okay, so this is the same situation.
**Jamie Lynch (Palo Alto Networks)** 14:52 We'd basically be leaking activity, which, could be a… Heavy Lodge Object.
**Jason Plumb (Splunk Inc.)** 14:59 Yeah.
**Hanson Ho** 15:00 Yeah, this one probably is worth… A patch.
To be honest.
**Jason Plumb (Splunk Inc.)** 15:07 Yeah, let's do it. I think I will just say, yeah, we want a patch, Is it 8.1? Will that be our patch number?
Yeah. Okay. And it'll just have those two cherry-picked into it.
If that makes sense, if that's cool.
**Cesar Munoz** 15:32 Sounds good.
**Jason Plumb (Splunk Inc.)** 15:34 Okay, I will… I will do that sometime this morning.
**Cesar Munoz** 15:40 Thank you, here.
**Jason Plumb (Splunk Inc.)** 15:42 Thank you all for… thank you all for being on top of these, I appreciate that.
**Hanson Ho** 15:45 Might be worthwhile to do a search for, the use of duration, or any of the new duration APIs in the rest of the codebase to see if This got just snuck in anywhere else.
**Jason Plumb (Splunk Inc.)** 16:00 I can do that before I do the patch, that makes sense.
Although, if I can figure out the animal sniffer thing, I can just run that and let that probably tell me, right? But…
**Hanson Ho** 16:17 Shit, that's a bit.
**Jason Plumb (Splunk Inc.)** 16:18 They're obvious, yeah.
**Cesar Munoz** 16:24 I see that Ben mentioned that we disabled the… Android check.
So maybe we're only relying on Animals need for… But I don't remember why.
**Jason Plumb (Splunk Inc.)** 16:38 So in the library conventions,
**Ben Joseph** 16:41 It's a PR from Serbi while adding some desug… Removing call library de-sugaring.
**Jamie Lynch (Palo Alto Networks)** 16:51 Yeah, that seems plausible.
**Cesar Munoz** 16:56 I don't remember there was an issue with it, probably compatibility or something with a small sniffer, but I don't know.
Have the details right now.
**Jason Plumb (Splunk Inc.)** 17:11 Saying it was one of these.
**Ben Joseph** 17:13 Pan 01.
PR number.
**Jason Plumb (Splunk Inc.)** 17:19 What's the number?
**Ben Joseph** 17:21 701.
**Jason Plumb (Splunk Inc.)** 17:23 This woman.
**Cesar Munoz** 17:23 Good up, yeah.
**Jason Plumb (Splunk Inc.)** 17:24 Yeah, sorry.
That was a while ago.
**Hanson Ho** 17:30 Whaaat?
Wait, what?
**Jason Plumb (Splunk Inc.)** 18:03 Well, I think I need more coffee to fully understand what this is about, but this has been here for a while. We've certainly had this for a few releases.
Like… A lot of them.
**Hanson Ho** 18:15 2 years.
**Jason Plumb (Splunk Inc.)** 18:16 Yeah.
So maybe that's not as relevant, but if it was… I mean, this is the… Yeah, so I think this was, de-sugaring our own libraries, is that what this was? And then she removed that.
**Cesar Munoz** 18:39 I don't remember the details.
That's too long.
**Jason Plumb (Splunk Inc.)** 18:42 go.
**Cesar Munoz** 18:43 Yeah, I think it was something about… this ANDRI mechanism complaining that we were using newer APIs.
But we could, it's just that those… wouldn't work.
on older versions.
But if I remember that it was about, an instrumentation.
That was only meant to be installed on newer versions.
So… I think it's the HTTP rail connection one.
Which… Which has… No, sorry. I think it was… okay, now I'm starting to remember. I think it was… that she was instrumenting some methods from… from HTTP area connection.
that were only available after some… some API.
So API 24, for example.
**Jason Plumb (Splunk Inc.)** 19:37 Okay.
**Cesar Munoz** 19:38 So, in theory, it's fine to ignore Android's Linton… linter there.
Because that APA… that method won't get instrumented if the method is not there. So it's essentially… it was kind of not safe because of that, so the instrumentation just wouldn't touch it.
But then Android… I think the Android linter was too strict.
And I think we were just relying on animal sniffer because of that.
**Jason Plumb (Splunk Inc.)** 20:12 Okay.
**Cesar Munoz** 20:13 Yeah, yeah.
**Jason Plumb (Splunk Inc.)** 20:14 That makes sense, I kind of remember this.
It would make sense that there are some methods on… HTTP URL connection that are newer, or… No, like, newer and ignore it if you're running on a… API that doesn't have those yet.
**Cesar Munoz** 20:32 Yeah, I need to check.
I mean, at the end of the day, we can probably just revert the, Gradle ignore Lynch API and just add it case by case.
Whatever needed, like, with an annotation or something.
**Hanson Ho** 20:49 Yeah, this is too harsh.
Or too… broad.
**Jason Plumb (Splunk Inc.)** 20:56 But this doesn't explain the animal sniffer problem, right? We expect animal sniffer to be running On every PR.
**Cesar Munoz** 21:05 Yeah.
**Jason Plumb (Splunk Inc.)** 21:06 Okay.
Okay, well, I will look at that. I will try and do a deeper dig. If anybody beats me to it, just hit me on… hit me on Slack.
Cool.
I had one other thought. So I've been… I've been looking at some of these old, stale PRs.
And if you scroll down here, there's a bunch, right? Like, we… this… this is, like, the oldest stuff here. Some of it going back to February.
And this is draft, so, like, maybe it's a special case, but my thought process was, why are these old, stale ones not… getting closed automatically. I thought we had… some automation around that, right? Like, the workflow is supposed to go, needs author feedback.
As soon as we label it, there's a certain window of time, and it's, like, 2 weeks or something. And if the author doesn't respond within 2 weeks or a month or whatever it is.
Then we put the stale label on, and then there should be another timer that starts, and after a certain other number of times, like another two weeks, we should just close it. Like, there's automation that should automatically close these things.
And I think that that's not working correctly.
And I'm not sure why.
I'm gonna ignore this one because it doesn't have both. The workflow… I think the workflow might require both, is the problem, and I'm curious what people think about this.
I kind of want… to fix this, because I think… having to do this by hand is a little bit tedious. Like, there's just plenty of stuff that people have a good idea, and they come and they submit a PR. We chat about it a little, and then it goes dormant. And then there's, like, the build's broken, or Copilot has some review changes, or we have some questions.
And if it just goes quiet, I mean, we can manually close it, but it's nice for us not to have to do that, if we can do it with automation. And so, that's the way the process was supposed to work, but I think it's broken.
**Cesar Munoz** 23:15 And David, yeah, no problem with that system.
**Jason Plumb (Splunk Inc.)** 23:18 You would like it, yeah?
**Cesar Munoz** 23:19 Yeah.
**Jason Plumb (Splunk Inc.)** 23:20 Okay.
**Jamie Lynch (Palo Alto Networks)** 23:21 Dude.
added a link to the doc. I think this came up on OpenTelemetry Kotlin, and… I think I fixed it?
I don't think it's actually run on a PR… But I remember… I've definitely seen the stale label come up on PRs, but…
**Jason Plumb (Splunk Inc.)** 23:42 And what was the fix for this?
**Jamie Lynch (Palo Alto Networks)** 23:44 So it was a permissions… Issue, like, it didn't have permission to write for label.
**Jason Plumb (Splunk Inc.)** 23:51 Oh, interesting, okay.
Were you seeing that error in the automation? Like, in the…
**Jamie Lynch (Palo Alto Networks)** 23:58 I just thought that nothing was, like, happening with old PRs which should have been flagged by it.
**Jason Plumb (Splunk Inc.)** 24:09 So it's called issue management, but I think it applies to everything. Like, PRs are considered issues, I think.
When it comes to GitHub, so I think it… I think it is supposed to apply to both.
So the stale action… We think there might be errors in here.
But maybe it's not looking at PRs.
Are any of these actually PRs?
Is there a way to tell?
Short of clicking them. So, $7.92.
I can't even remember what I just said. 792.
Okay, that's an issue.
3, 4, and 5. 3.
Gotta be a better way of doing this, right?
4?
Yeah, okay, so I don't know how to… I mean, in your experience, Jamie, was this ignoring PRs?
**Jamie Lynch (Palo Alto Networks)** 25:42 Yes.
**Jason Plumb (Splunk Inc.)** 25:44 Okay. But it has some… okay, this is how you tell, because they're called out as PRs.
So we should be able to look at, like, one of these ones that we said was stale.
Like, just… I'll pick one.
I'm in the wrong project now.
like… I don't know, let's look at David's. 1841.
No, why would it be in here?
There it is, okay.
So now this is getting exciting. Okay, it was last updated here, so it's still current, right? That's not stale if it was last updated.
Let's look at a different one.
Wrong project.
Let's look at… this one. So, 2011. I'm gonna just do this manually and see when I think it was last updated.
So, big PR, August 25th.
Some discussion, some discussion… Needs author feedback. Stale on the 17th. I asked on the 22nd.
more, more, more, and then I think there's… Okay, so there has been some activity… Within 3 weeks. But it still has the stale?
I'm confused.
When was the last commit? The last commit was… Here.
I can't… can I see what date?
Be too easy. September 23rd. Okay, so… That's when the last commit was.
Do we know if the stale gets removed on any PR activity, or is it based on commits? I don't remember.
**Jamie Lynch (Palo Alto Networks)** 28:02 I think it was just… Any activity, but, like… I'm not 100% sure on that.
**Jason Plumb (Splunk Inc.)** 28:11 Okay. Well… It sounds like I certainly don't know how it's currently working. I know how I want it to work, I think it's not currently working, and it sounds like nobody else has exactly a better understanding of it right now, so I'm gonna open a tracking issue and try and fix this, because I agree with Cesar, it's… I want this to be working.
**Jamie Lynch (Palo Alto Networks)** 28:31 Hmm.
**Jason Plumb (Splunk Inc.)** 28:32 Just because of the… like, just the maintenance burden is a little bit much when the PRs are growing indefinitely, so… Okay. I'm gonna continue giving myself action items.
Not sure if we have docs on this already. Does anyone know?
**Cesar Munoz** 29:05 No, the CI stuff that we have here, I… I have been up to date.
**Jason Plumb (Splunk Inc.)** 29:13 Okay. So, I mean, as I do this effort, I will also try and capture it in some sort of markdown, so that we can answer this question more easily in the future, and not have to be like.
How is it working again?
Alright, but the goal, I'm just gonna write this down while I'm thinking about it, the goal is to have… both issues and PRs, that are flagged to get stale after… I don't know.
Y time. Okay.
Okay, anything else exciting? Wrong project, Jason.
**Ben Joseph** 30:01 And any stale marking goes away on any activity?
**Jason Plumb (Splunk Inc.)** 30:06 Yeah, yeah, and needs author feedback, so… I guess the question is, yeah, what kind of activity? Like, if there's still comments, I think we should leave it open. Like, if people are still actively commenting on it, then I think we don't close it, so…
**Hanson Ho** 30:22 Many human activity, even if it's, like, bump.
**Jason Plumb (Splunk Inc.)** 30:26 Totally.
And we should also remove the stale in this case, right?
Like, if someone comments on a stale… PR or issue, we can remove it, right?
We can remove the stale label, and then… Two weeks later, it will automatically get added, or whatever the time is.
**Ben Joseph** 31:12 Do we have to apply the same rules, to issues and PRs? The concern here is that, like, issues might be worth keeping alive for longer. PRs, if somebody… the order is not responding, then we cannot take it forward, and we have to close and open new, maybe?
So maybe, maybe we should have different rules.
**Jason Plumb (Splunk Inc.)** 31:35 I agree. Yeah. I think issues… Should be able to stay open for, like, a year or something.
Hopefully you don't have to treat them the same. My intention is to not treat them the same.
**Ben Joseph** 31:47 Okay.
**Hanson Ho** 31:50 an issue is not ongoing work, an issue is, hey, this is a problem, versus, like, a PR, at least a not-draft PR is… should ought to be ongoing work. If it's not ongoing, it's literally stale, so…
**Jason Plumb (Splunk Inc.)** 32:01 Yeah, and, like, so issues that are… I think issues that are 3 years old are fine. I think they can stay out there. If they have the needs author feedback, like, if someone opened it 3 years ago, and we're like, oh, hey, is this still a problem for you, and they don't respond, I think that's fine to go through the workflow.
If one of us manually labels it stale, because we think it's stale or not relevant, then that can go through the workflow.
But if it's just a regular old issue, I'm fine with it staying open indefinitely.
What do y'all think about that?
Should there be some maximum age? I think… Java and instrumentation both have a maximum age on everything now.
Just cause it's insane.
But I think ours is manageable still.
**Hanson Ho** 32:51 Yeah, if it gets insane, we can put a maximum age, but…
**Jason Plumb (Splunk Inc.)** 32:57 Okay.
Cool.
**Ben Joseph** 32:59 I don't think we deal with that volume of issues, too.
**Jason Plumb (Splunk Inc.)** 33:03 Yeah.
**Ben Joseph** 33:04 Yeah, so it should be a.
**Jason Plumb (Splunk Inc.)** 33:06 Cool. Yeah, I agree.
Okay, well, I'm gonna, I'm gonna prioritize the patch, and I'll do that first, and then I will revisit these other… Action items today.
Alright, I have 28 minutes until the Java SIG meeting, I'm gonna try and do a cherry pick and changelog PR.
Sound good?
Alright, everyone.
**Cesar Munoz** 33:33 Yep.
Thank you.
**Ben Joseph** 33:35 Bye.
**Hanson Ho** 33:36 And I…
**Jason Plumb (Splunk Inc.)** 33:36 Take care.
**Cesar Munoz** 33:37 8.
