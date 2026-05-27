SIG: Android SIG
Date: 2026-05-26
Duration: 23 minutes
============================================================

## Zoom Recording Transcript

**Jason Plumb** 02:16 Good morning.
Hey.
And I just got set up here.
Yeah, 8 AM, first thing after a 3-day weekend. Definitely not the highest point of my week.
Probably the least coherent.
And… alert, attentive, aware, meaningful part of my day, right now.
Well, let's do it!
I'm gonna, I'm gonna try my best.
**Cesar Munoz** 02:50 Yeah, it's fine. Broadly, there's not much.
Let's see. To discuss.
**Jason Plumb** 02:58 Oh yeah, we don't even have the new date set up yet here.
Yeah, so we did the release last week, right?
**Cesar Munoz** 03:27 Yeah.
And your fix for the, versions Seem… seem to work.
**Jason Plumb** 03:37 Yeah, this part, right? Yeah, this…
**Cesar Munoz** 03:39 Yeah.
**Jason Plumb** 03:39 And, like, it's failed the last 4 times.
So it finally got it shaped up.
Oh, man.
**Cesar Munoz** 03:46 Fifth time, the charm is the charm.
**Jason Plumb** 03:50 Yeah.
**Cesar Munoz** 03:50 Yeah, and it's very useful, to be honest.
**Jason Plumb** 03:53 So, I think that there was something in… I think they're gonna patch upstream. Have they done that yet?
Yeah.
But I don't think that we need to patch. I think it's very specific.
Java agent startup failures, declarative config, so that doesn't affect us.
Right, we only really use the instrumentation stuff. Like the… The OKHTTP and the instrumentation APIs.
So…
**Cesar Munoz** 04:18 Yeah.
**Jason Plumb** 04:19 I think we're okay without that.
Cool, yeah, thanks for… thanks for running that, it's awesome.
**Cesar Munoz** 04:26 No, it is fine, it's… There, there, there are a couple of, steps.
that… They seem a bit redundant, or a bit… Strange.
to, you know, in terms of the order that you have to execute them. So, for example…
**Jason Plumb** 04:48 Yeah, let's talk it out.
**Cesar Munoz** 04:50 The, when you're preparing the release.
I think there's an action that creates two PRs, one that goes to the new release branch, and then the other one goes to main.
**Jason Plumb** 05:01 Yep.
**Cesar Munoz** 05:02 the instructions, I think they read something along the lines of that you can merge them both before the release.
And it's a bit weird, because…
**Jason Plumb** 05:12 You have to merge them before the release, or it will fail.
**Cesar Munoz** 05:17 Got it, but, like…
**Jason Plumb** 05:18 Yeah.
**Cesar Munoz** 05:19 at least the one that gets merged into main, I think it's weird.
Because if you're feeling it… I felt like I was merging it.
Before that, it's live.
**Jason Plumb** 05:29 Yeah, yeah.
**Cesar Munoz** 05:30 It's like, what if it fails, you know? And now we have all the new stuff and docs and stuff in the main branch.
**Jason Plumb** 05:38 I know.
**Cesar Munoz** 05:39 Things like that, they're very small.
**Jason Plumb** 05:43 Yeah, I think… I think there's a… I think there's a step in here that tries to verify… let's… let's just walk it through, since we have a light agenda. Karthik, I don't know if you've joined us before, if you… if you have or haven't, but welcome anyway. I'll put a link to our document that we're working from, and it's very light today, so if you have anything that you would like to chat about.
Please feel free to add it to the agenda, and we'll come back in, like, a second, but thanks for joining.
This workflow here… let's see… Not the patch release. It might be in one of the scripts or something.
**Cesar Munoz** 06:25 I think it's in the, it's in the pre… pre-release, prepare-release? I don't know what's the name of the…
**Jason Plumb** 06:31 That's the one that creates them, right?
**Cesar Munoz** 06:35 Yeah.
**Jason Plumb** 06:36 Yeah, this is the one that creates it, but I thought during the release there was a step that checked it.
**Cesar Munoz** 06:41 Oh, I'm not sure.
Because during the release, you only need the… the release branch.
**Jason Plumb** 06:51 Yeah, I thought it did a verification somewhere.
Here, yeah, yeah, this.
I think it's this. So check that the changelog update was merged to main.
So if you don't merge that one domain before you run the release, it'll say, nope.
And it'll exit. It'll just break the build. So we could consider, like, removing this, I suppose, but it's just another safety check to sort of make sure that it was followed. I think… so I think this… a lot of this is borrowed from other projects, but I think the idea is probably that… What was intended… Is that the changelog in main already reflects the release that is being built, even though it hasn't been built yet.
And that does seem a little bit out of order, to your point.
So we could.
**Cesar Munoz** 07:39 Yeah, I mean, it's not… like, we can improve it. I'm not saying… it's not a… It's not a deal-breaker or, you know, anything too bad.
**Jason Plumb** 07:47 Yeah.
**Cesar Munoz** 07:48 I'm just really not… just nitpicking here.
**Jason Plumb** 07:51 Yeah, no, it's fair.
**Cesar Munoz** 07:52 Process already works, so…
**Jason Plumb** 07:57 Yep.
And also, just troubleshooting the release process is kind of… Time-consuming, and it's… it's a little bit tedious to make… to make changes, you know?
**Cesar Munoz** 08:11 Yeah, or to make them work, actually, at the first…
**Jason Plumb** 08:14 Yeah.
**Cesar Munoz** 08:14 restoration, yeah.
**Jason Plumb** 08:15 And no.
**Cesar Munoz** 08:17 So, I think it's fine, for now, Aziz.
If there's nothing, else to discuss… I just wanted to take a look at, some PRs that… that Jamie created before.
Going on leave.
**Jason Plumb** 08:46 Yeah.
Let's do it.
Fractal Wrench.
What's the only one that's open?
**Cesar Munoz** 09:11 Oh, the… no, the… oh.
I think you'll have to remove the issue filter.
**Jason Plumb** 09:16 Oh, issue, yeah, sorry. PR.
Like I said, 8 o'clock in the morning after a 3-day weekend, not my finest time.
**Cesar Munoz** 09:25 That's fine.
**Jason Plumb** 09:28 What do you want to start with?
**Cesar Munoz** 09:30 Well, the first one… well, yeah, from bottom to top. Yeah. The ROM constants one, I think it's pretty straightforward.
**Jason Plumb** 09:37 We talked about this last week, yeah.
**Cesar Munoz** 09:40 Yeah, it's just that it's… I mean… the three PRs, I think, I think, are fine to get merged, it's just that they touch on a lot of files.
So I just wanted to make sure… you know, I'm not the only one looking at those, but essentially, they're just moving you know, things, it's not, like, breaking changes or anything.
**Jason Plumb** 10:04 Okay.
Definitely agree that anything that has, like, a large footprint needs extra eyes.
Yeah, I'll take a look at this today.
I'll try and take a look at all three of these today.
**Cesar Munoz** 10:19 Thank you.
**Jason Plumb** 10:21 Yeah, I mean, this is… this is great. Like, I… I mean, this is awesome.
So there's one thing…
**Cesar Munoz** 10:28 It removes a lot of…
**Jason Plumb** 10:29 Yeah, or a few things are left, but it's, like, much better.
Yeah.
**Cesar Munoz** 10:33 Yeah.
**Jason Plumb** 10:35 Okay, what was the other two? It's.
**Cesar Munoz** 10:40 More of the same.
**Jason Plumb** 10:41 Yeah.
**Cesar Munoz** 10:42 I mean, the same kind of work, it's just… Reorganizing stuff.
**Jason Plumb** 10:56 Okay.
Cool, so we don't necessarily have one consolidated place for every… kind of services thing now, some of them have moved around closer to where they're used.
Seems fine.
**Cesar Munoz** 11:13 Yeah, there are still a couple of things missing, which I think he addressed in the last VR.
But there are still… I think we still have… to, even after this… after merging these 3PRs, we still have to figure out What to do about some remaining bits in common, and surfaces.
But it's a huge… step forward, I think.
**Jason Plumb** 11:40 Cool, that's great.
You reminded me… Because my brain is not alive yet. Was there anything that stabilized this time?
I think we didn't.
**Cesar Munoz** 11:55 wah… I think… no, I think we… I think we did.
**Jason Plumb** 12:00 Which module?
**Cesar Munoz** 12:02 Was it?
Well, I have mixed… a mix of, conversations in my mind right now, but I think I remember we were talking about stabilizing the instrumentation API, didn't it? Or maybe that was for the previous release, I…
**Jason Plumb** 12:20 I think that was the previous release.
**Cesar Munoz** 12:22 Okay, got it.
**Jason Plumb** 12:24 So, we got session stabilized, and then I think it was the last release that had the instrumentation API, but let's double check.
**Cesar Munoz** 12:41 Yep.
There it is.
**Jason Plumb** 12:44 session… I don't see the instrumentation API, am I missing it?
**Cesar Munoz** 12:54 Oh, it's Agent API, okay.
**Jason Plumb** 12:57 Right. So, instrumentation API… I'm just gonna keep opening tabs, apparently.
I thought we did stabilize that one.
Is it this module?
**Cesar Munoz** 13:10 its room.
**Jason Plumb** 13:12 No, he did not.
So, that should be next on our list. What was preventing us from doing that? Did we just let it slip?
**Cesar Munoz** 13:23 Probably, to be honest, I don't remember.
**Jason Plumb** 13:25 Yeah.
Well, we can pick that up the next time, but is there a milestone for it?
This one.
I'm sorry I pulled you off of those PRs, but, like, the three that we were talking about.
**Cesar Munoz** 13:42 I mean, there was nothing else to these cars.
**Jason Plumb** 13:44 Yeah.
**Cesar Munoz** 13:45 My side.
**Jason Plumb** 13:46 Oops.
**Cesar Munoz** 13:52 Oh, this was the, oh, I created a PR for this, actually.
**Jason Plumb** 13:57 You did.
**Cesar Munoz** 13:59 Not sure if I merged it. I mean… It's probably the same for you, but currently taking care of a lot of projects.
**Jason Plumb** 14:07 Oh yeah, man.
**Cesar Munoz** 14:08 Sometimes you just mix stuff up.
**Jason Plumb** 14:09 I know. It's a lot of balls in the air at once.
**Cesar Munoz** 14:13 I did create a PR, which… It's approved… I don't know why I haven't… I haven't merged it.
But yeah, once that's merged… It's, It's the fourth one on that list.
**Jason Plumb** 14:30 This… no. 1, 2, 3, this one.
**Cesar Munoz** 14:33 Yeah.
**Jason Plumb** 14:39 Cool, okay.
Awesome.
**Cesar Munoz** 14:46 I can just take a look at stabilizing the instrumentation API.
Right away, I think there's something left.
**Jason Plumb** 14:54 Cool. Looks like it's got some review already, that's great. Okay, so I'm… I'm trusting, and I want that to be merged.
And if there's mistakes, we can fix them, but we got two approvals, that's great. I love it. And so that does close that one, which I think then closes the milestone.
And I don't know how to get back in there.
Once we do this one.
So this is now closed, right?
Mmm… what am I missing?
Aside from my brain.
**Cesar Munoz** 15:42 Not, too familiar with GitHub.
**Jason Plumb** 15:46 Closes 1738. Oh, so that's separate… that's a separate issue.
Then 7… then 532.
But we can close this one.
Is this… this is the same… I mean, yeah, so… I was commenting here… this is the only thing that's left in the milestone. I was commenting in this comment that I liked your docs that you added.
Man, where is… GitHub is being very slow this morning.
**Cesar Munoz** 16:17 A couple of hours ago, GitHub was… was down.
**Jason Plumb** 16:21 Like, look, like.
**Cesar Munoz** 16:22 So, it's probably…
**Jason Plumb** 16:23 I think this comment… so if you look at the URL when I'm hovering, it shows that it's linking to a comment, but I click on this and it no longer… goes to the comment, it just goes to the PR, and so did it auto-close the comment?
Yes. No.
**Cesar Munoz** 16:42 weird.
**Jason Plumb** 16:42 Yeah, it's… that is bizarre.
Anyway, it was this comment, and I was just saying that I liked these… I liked these docs, And… how do we document it more broadly? I'm not… I didn't read it. Did… does this cover that? Does it tell people that, like, when you're configuring stuff?
You probably.
**Cesar Munoz** 17:03 Big.
**Jason Plumb** 17:04 Do it before you install it?
**Cesar Munoz** 17:05 The guide touches on it, or on how to use it, but it's more focused on how to create an instrumentation.
**Jason Plumb** 17:13 Okay.
Which is great, but I think it's a separate issue, and… The broader guidance of, like, if you're writing your own instrumentation, or if you're… if you're stitching in your own instrumentation, ensuring that you do any configuration prior to install.
**Cesar Munoz** 17:28 It's mentioned there in the guide, as far as I remember.
**Jason Plumb** 17:31 Do you want to close that issue? Should we close that thing, then? Should we close…
**Cesar Munoz** 17:35 I think the money's gonna be getting closer.
**Jason Plumb** 17:37 room.
So then, okay, did it really… it automatically closed? Or did you close it?
**Cesar Munoz** 17:49 Yeah, it's mentioned there.
I did include it, Sid.
**Jason Plumb** 17:53 Maybe…
**Cesar Munoz** 17:53 I was automatically closed.
**Jason Plumb** 17:55 Okay, okay, well maybe I was just ahead of GitHub.
That's real weird.
I haven't seen that happen before, but okay, our… great. Everything's going…
**Cesar Munoz** 18:05 Eva has had a rough day today.
**Jason Plumb** 18:08 Okay, okay.
**Cesar Munoz** 18:09 So… And a rough couple of weeks, to be honest.
**Jason Plumb** 18:15 Months, yes.
**Cesar Munoz** 18:17 Yeah.
**Jason Plumb** 18:19 Okay, that's… that's awesome. So what's this one? Let's see… Yes.
David, thank you for submitting this. We should probably get back to it. It's more of the click work, yeah, the long press. Did I review this? I thought I looked at this.
But I didn't leave a review. Jamie likes it. I did look at it.
And I had very important feedback here, Jesus.
Okay, cool, yeah, we should circle back on this. I will also try and give that a look today.
Have you seen this one, Cesar?
**Cesar Munoz** 19:00 No, not in detail. I saw… Manuel's comment.
But, yeah, not much.
**Jason Plumb** 19:11 Yeah, this is frightening, but we can address it if that happens.
**Cesar Munoz** 19:17 I mean, that it could be added later?
**Jason Plumb** 19:22 Yeah.
**DavidGrath** 19:26 Okay, so I want to confirm, so it's non-blocking then?
**Jason Plumb** 19:31 I mean, it's… I think it's up to you. I… I don't… I mean, this is anecdotal, I don't know that it's that important, but what do you guys think?
**DavidGrath** 19:43 I mean… I guess I could add it, just I don't know how involved it would be, that's my concern.
**Jason Plumb** 19:52 Yeah.
I haven't… I'll… yeah, I will re-read this. I don't want to do it on the call, but I will re-read this and leave some feedback.
**Cesar Munoz** 20:02 Also, have a look after the call.
**DavidGrath** 20:09 Alright, it's…
**Jason Plumb** 20:10 Cool, appreciate those contributions, David, those are awesome.
**DavidGrath** 20:17 Thank you.
**Jason Plumb** 20:31 Let's just, for the… for the record, let's link to these, three PRs that we had talked about. I no longer can keep track of them.
Author… I think the challenge now is that he's on… he's on leave for a while, so if we do have feedback on these, it's gonna be hard to address them. Somebody else will probably have to… to pick them up.
**Jason Morris** 21:15 to do that.
**Jason Plumb** 21:17 I think it's… it's fine. Who… who was speaking? Was that Jason?
**Jason Morris** 21:19 First and others.
**Jason Plumb** 21:20 Yeah, okay.
**Jason Morris** 21:21 But… Okay.
**Jason Plumb** 21:22 Alright.
**Cesar Munoz** 21:23 Thank you.
**Jason Plumb** 21:23 Yeah.
So, Karthik, I think it's your first time joining us, so I just wanted to give you a chance to say hi, or provide feedback about the project, or what your interest is, or who you're with, or any input to this team would be… would be great.
**Karthik Rajan M R** 21:41 Yeah, hi sir, I just now started my journey in OpenTelemetry.
on the… I have applied for the NFX mentorship in Go language.
**Jason Plumb** 21:53 Okay.
Cool.
**Karthik Rajan M R** 21:56 Yeah.
And I'm currently learning about what OpenTelemetry and how it works.
That's what my current journey is.
**Jason Plumb** 22:06 Cool. Well, welcome. Have you had a chance to look at Android at all?
**Karthik Rajan M R** 22:12 As of now, I didn't.
I moved both time.
**Jason Plumb** 22:18 Well, awesome. We certainly can use contributors and people looking at PRs and providing feedback, especially those who have some Android experience, so that's great.
Okay, cool. Well, pretty light agenda today. We can wrap early, unless anybody has anything else they'd like to bring up. Jason, you got anything for us?
**Jason Morris** 22:42 Hello?
Also, 3-day weekend, etc.
**Jason Plumb** 22:48 Yeah, I know.
Were there any exciting new issues or anything that were raised? I didn't… and, like, I'm just literally just logged on, so… Nothing… nothing too pressing and new. This is pretty exciting. Cool. Alright.
Well, I think that's a wrap.
Appreciate it, thank you.
We'll see you soon.
**Jason Morris** 23:13 Thanks, Carol. Thanks.
**Jason Plumb** 23:14 Right.
