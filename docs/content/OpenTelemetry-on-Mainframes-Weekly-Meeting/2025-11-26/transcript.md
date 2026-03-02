SIG: OpenTelemetry on Mainframes Weekly Meeting
Date: 2025-11-26
Duration: 17 minutes
Zoom Recording URL: https://zoom.us/rec/share/yNWgdAI8-UjxKN0w1qSDo6aSnvLFsa_6_62-SnSrTOcwcTecZjb_6EaAvyRHwitD.cDMRyT-44WEgmzTQ
============================================================

## Zoom Recording Transcript

**Greg Shriver** 00:26 Hey, Morgan.
**Morgan McLean** 00:33 Oh, my mic was off. How you doing?
**Greg Shriver** 00:36 I'm well, how are you?
**Morgan McLean** 00:37 I'm doing alright.
I assume it's a short week for you?
**Greg Shriver** 00:41 It is. In fact, as soon as we hang up, I'm probably leaving.
**Morgan McLean** 00:46 Very nice! I've got a couple more meetings, but, but, yeah, should be, should be good.
**Greg Shriver** 00:51 Nice.
Nice. I…
**Richard Nikula** 00:55 The hardcore people are here, I see.
**Greg Shriver** 00:58 There you go. Hey, Richard.
**Richard Nikula** 00:59 Nope.
**Morgan McLean** 01:00 I would… my only issue with that is I think Rudiger is the most hardcore of all of us, and he's not here yet.
**Greg Shriver** 01:06 Yeah, yeah.
Yeah, I don't know if he's planning on… I didn't see anything in the chat that said that he would not be here.
**Morgan McLean** 01:16 No, I saw that Jim is out…
**Greg Shriver** 01:19 Jim's out.
**Morgan McLean** 01:20 Yeah.
**Greg Shriver** 01:26 Yeah.
So, I have… I guess an update, let's see…
Where'd I leave my stuff here?
So, I think last meeting, and the meeting before that, we had talked about, I have an action item to trying to get together, some… some documentation. So I guess some overview documentation for…
mainframe. And, I started working on that. I am not in… I'm not really in a place to… to be ready to share it quite yet. So I have something, and I can…
Show…
**Morgan McLean** 02:33 Yeah, sure.
**Greg Shriver** 02:34 Actually, why don't I just share real quick?
So, here's kind of where I started.
First of all, can you all see… Yes. …my VS Code? Okay.
So, I don't know anything about Yugo, right?
But I looked at some of the other stuff that was in here, some of the other, like, under platforms, so it looked like…
It looks like the best place to start, like, with a really high level, hey, here's a mainframe.
is kind of under this, content, en, docs platforms, and then we've got client apps, function as a service, and Kubernetes. And I kind of modeled, I was looking at what they do with the index.underscore index.md.
And I'm thinking that, you know, maybe that, you know, following that sort of,
Following that sort of convention makes some sense.
And so, I… copied… I created a branch called Add Mainframe Overview.
And I added this mainframe folder under Platforms, and I took a stab at creating the… at least the index, right?
some of this, I don't… I'm not really… I'm less familiar with… well, I'm not familiar at all with Yugo, but, I'm not horribly familiar with, like, all of the mechanics of… of, providing, you know, I guess, open telemetry contributions.
I'm assuming here that if I can, you know, take this and… Committed to my local branch.
And at that point, do I… would I then push it up and then have us review it on a SIG… a future SIG call, or how would that kind of work?
**Morgan McLean** 04:41 Yeah, so… I think…
So, what I would typically do is then put in the PR… this is in the mainframe SIG itself, right?
**Greg Shriver** 04:53 Damn.
**Morgan McLean** 04:53 docs.
**Greg Shriver** 04:54 No, this is in Docs.
**Morgan McLean** 04:55 Yeah, yeah, so what I would do is open the PR, solicit some reviews there, and then if needed, there's a weekly docs call.
**Greg Shriver** 05:06 And I would join that.
Oh, I see. Okay.
**Morgan McLean** 05:10 Yeah, but typically for docs, in my experience, you don't always need to join the call. Typically, you can just open a PR and then ask for review.
**Greg Shriver** 05:17 Okay, and do you think it would be appropriate… so, first of all, are the mechanics, the Git mechanics, the local branch? I'm thinking that the… having a descriptive branch and a branch name makes sense to facilitate the PR, right?
**Morgan McLean** 05:35 Correct. It doesn't typically… it's funny, it's actually kind of funny you ask this, because I ran into this a couple weeks ago. For most repos, you do not need to have a different branch, right? As long as you have your own sort of fork of the repo, and you're in main.
And then the source one is in main, it's fine, the, the, doesn't really matter. For docs, they specifically require you to have a branch that has a different name than their main branch.
I don't know why, it's some weird technical thing, it's not a process, it's not like a human process thing, it's some technical thing.
**Greg Shriver** 06:08 Okay. But I actually had to, like, resubmit a Docs PR recently. Like, I actually had to close it out and submit a new one, because I had to change the branch.
**Morgan McLean** 06:15 to one that didn't conflict. So, you ask, I think, because of human processes, and that actually isn't the reason why, but in docs, you do need to do it.
**Greg Shriver** 06:23 Right.
Okay.
Alright, well then, so I assume that, provided I'm in EZCLA and all that stuff, I shouldn't have a problem then.
**Morgan McLean** 06:33 You should have no trouble.
**Greg Shriver** 06:34 Pushing this branch up to… the actual repo, right? Yeah. And then opening a PR.
**Morgan McLean** 06:43 So typically you would open a PR from a fork of the repo that you have under your own name, or in some other organization that isn't OTEL.
**Greg Shriver** 06:54 Okay, that's helpful to know. I did not fork it, all I did was clone it.
And now we're pushing up against the edge of my GitKnowledge. Don't do that. Okay.
**Morgan McLean** 07:05 I think that's okay…
Basically, what you won't… typically what you… what you will not do is, like, contribute your fork, and then do a PR against that. You would usually do a PR from another repo that's typically a fork.
Right, so, like, like, you would not contribute your branch.
to the upstream repo, and then do a PR from their main branch against your branch, all within that repo. Typically, it's from…
A repo in your own organization.
**Greg Shriver** 07:39 I think that's correct.
**Morgan McLean** 07:40 Yes.
I'm pretty sure what I said is right. Yes.
**Greg Shriver** 07:43 Okay.
**Morgan McLean** 07:44 Yeah, because, like, it turns out you and I, for that matter, don't have the ability to go create a branch in the OpenTelemetry organization repo.
**Greg Shriver** 07:57 Okay, so… okay, so that makes more sense then. Okay.
Because, so, when I… if I tried to push this branch directly up to the main repo, I'm probably gonna get failed. It won't accept it.
**Morgan McLean** 08:09 Yep.
**Greg Shriver** 08:10 Alright, well, then…
**Morgan McLean** 08:13 That's how I've always done it, and that's my understanding, right? Like, the PR, like, it… or it would require a PR to even contribute it, but now you'd be doing a PR just to put it in a separate branch, anyways.
**Greg Shriver** 08:25 Yeah. Which is, like…
**Morgan McLean** 08:27 You want to contribute it up to the main one.
**Greg Shriver** 08:29 Got it. Okay, so these are the details that I'm just unfamiliar with. All good.
**Morgan McLean** 08:34 Yeah.
**Greg Shriver** 08:34 Okay, cool. Well, thank you, that's helpful.
like I said, I don't have it… I mean, I could share the file that I intend to put up through this thing, but…
**Morgan McLean** 08:44 That's fine.
**Greg Shriver** 08:45 But… but I don't… it's probably premature to do that at this point, and I'll… I'll… I'll,
I'll do the other thing. I've never forked before, so I'll… I'll fork it and see, and maybe I'll come back, you know…
**Morgan McLean** 09:02 If you want to be lazy, you could just do it all in the GitHub UI. That's… for docs, I usually just do it in the UI, where just, like, go to… and I might be using the wrong words, let me just pull up GitHub on my own.
For docks, what I usually do… Pulling it up…
Yeah, what I usually do is fork it into my own, you know, GitHub org that belongs to my account.
go into a different branch, and then if you're just adding a file, you could literally just go in the GitHub UI in that branch, and add a file. Like, just copy-paste whatever you have, just blindly into a new file, give the file a name, and then GitHub will prompt you to be like, oh, do you want to open a PR against the original repo with this fork?
**Greg Shriver** 09:54 Okay.
**Morgan McLean** 09:55 Makes sense. Yeah, super easy. But that's nice for a PM like me who struggles with Git commands.
Cloud repos, I usually, well, always, just actually use Git properly, but Docs has that weird branch requirement that's specific to Docs. Sure. And also, Docs, I mean, it's just Markdown.
**Greg Shriver** 10:14 Okay.
**Morgan McLean** 10:15 Usually, I just do it within github.com.
Cool. So that might be the easiest way to do it, especially if you're just adding, editing a few files.
**Greg Shriver** 10:23 Okay.
**Morgan McLean** 10:24 Cool. And there's a nice markdown preview editor on GitHub.
**Greg Shriver** 10:28 Yeah, okay, yeah, that, that would be helpful for…
**Morgan McLean** 10:31 Yeah, so that's probably the easiest path.
**Greg Shriver** 10:34 Yeah. Okay.
Thank you.
**Morgan McLean** 10:36 Yeah, of course.
**Greg Shriver** 10:38 And unfortunately, that's the only update that I have for today, so…
**Morgan McLean** 10:41 Okay. We've got more people now.
**Ruediger Schulze (IBM)** 10:44 Thanks, Greg. I think this is good. Just FYI, if you have the PR, there are also a couple of tasks running, so Lint and a few other checks.
Maybe you've seen it already, so you, you need to, you know.
be… be… yeah, just look at this. It's often just a space, or a new line, or something that, you know, these tasks are complaining about when they fail.
Sometimes it's also words that they don't know. There's a couple of rules of how to add them then. I guess, you know, as you go through this, you will see this and figure it out. This is the things that I came across
Writing the blog, so it, you know, it's something to learn as you go.
**Greg Shriver** 11:33 Yeah, yeah, well, I appreciate that. I saw some of that stuff in the contributing documentation, and ways to get around it, like, they have, you know, like, they have, like, fixers. I don't know what you call them, but, like, NPM fix, you know, if you want to just…
fix spelling errors that get caught by C-Spell and things like that. So, that… yeah, and that's helpful to know, thank you.
**Ruediger Schulze (IBM)** 11:57 Yeah, right.
Maybe one update for me, so we have this discussion around the GitHub Action Runner, and obviously we, you know, why we have been able to install the app, the GitHub Action Runner for the Linux S390.
platform. We had… we seem to still have issues with, properly authorizing this, and this might be related to
requiring admin rights on the repo itself. Now, we didn't investigate this further, but our open source office actually informed me that the CNCF is now looking at also having their own GitHub Action Runner for
Linux on C, or the Linux on S390 platform.
**Morgan McLean** 12:45 Nice.
**Ruediger Schulze (IBM)** 12:45 Which… which is maybe…
the better way, then. It's still, you know, work that the CNCF team obviously needs to move forward with, or the organization, but they got the…
the patch, which I think refers to the JITAB Action Router app that we be using, and I think this has been shared with the CNCF org.
And, obviously, our contact or our, you know, open source office is hopeful that, CNCF will make progress there. Just FYI, this is obviously going with… together with the Marist, college, so the…
That's an… that's an organization, I think it's close to Poughkeepsie. Poughkeepsie is an IBM location where, you know, lots of mainframe development has been done in the past and still is occurring.
But that would be then a more, community-driven approach.
And maybe, and this is the question that I can't answer, but maybe it will simplify the way of how then these…
administrative tasks around installing, you know, GitHub Action… self-hosted GitHub Action Runner apps would be maybe simplified, and maybe then more from an OpenTelemetry project perspective, maybe this becomes easier than, you know, what we discussed around
the… having a, you know, somebody with an IBM ID doing this, having, you know, a respective email associated with this ID, and then obviously also running into these challenges with the…
With the authorization, as we understood the problem right now. So,
So maybe it's reasonable, and I don't know, I can ask who the contact from a CNCF side is, but maybe it would be of interest if CNCF and OpenTelemetry project
Have a… have an exchange on that, and maybe then we can also understand the timeline, and maybe this is the better way to move forward in this…
**Morgan McLean** 14:50 That would be excellent, like, I know Antoine's not here today, but this is actually something he and I were discussing, which was, like, how do we improve automated testing for any of the mainframe components?
**Ruediger Schulze (IBM)** 15:01 Yeah.
**Morgan McLean** 15:01 So, this would be excellent.
**Ruediger Schulze (IBM)** 15:04 Yeah, let me ask who our team is talking to on the CNCF side, and let me share this, and then maybe, you know, Antoine or, you know, whoever from the project side, open telemetry project side.
Maybe could… could have a discussion with CNCF team.
**Morgan McLean** 15:23 Yeah, yeah, we'd be… like, once you know who to talk to, I'd be happy to.
**Ruediger Schulze (IBM)** 15:26 Yeah.
**Morgan McLean** 15:26 involved in that.
**Ruediger Schulze (IBM)** 15:27 Right. Yeah. Okay.
**Morgan McLean** 15:29 That was a challenge, like, even for our own stuff inside of Splunk, like, apparently Cisco has a mainframe somewhere, but we've asked around a bunch and we still can't get details on it.
And then we were chatting to some people at IBM who offered to give us time on one, but it was for, like, 6 months or something, right? Like, we need perpetual testing, the ability to test things perpetually. So if the CNCF has GitHub Actions, like, access to GitHub Actions that can run on a mainframe, that would be amazing.
**Ruediger Schulze (IBM)** 15:57 Right. Yeah, so I get back to you on that one, or to… Awesome. …the group here.
Okay, good.
I also don't have any other updates, but I think, I think this was,
One of the points to share today.
**Morgan McLean** 16:17 Okay, well, this is all great.
Alright. I don't have anything else from my end. But yeah, Greg, send a message on Slack once you get the PR submitted to Docs. I can take a look as well.
**Greg Shriver** 16:31 Sure.
**Morgan McLean** 16:32 I don't… I've submitted a whole bunch of stuff to docs over the last year. I very rarely attend their weekly calls, and so they're very good about approving stuff and reviewing it just asynchronously on GitHub. If, for some reason, we're not getting traction, that's when you or someone else can join their weekly call and poke them on it.
**Ruediger Schulze (IBM)** 16:47 But I can just confirm what Morong said, Craig. It's actually… they're very responsive, just submit the PR. Yeah. I also had been chatting with a few of them, so if there's any questions, we can also just do this via Slack.
But, usually this really runs very smoothly once you submit the PR.
**Morgan McLean** 17:08 Yeah.
**Greg Shriver** 17:10 Cool. Appreciate it. Thanks, guys.
**Morgan McLean** 17:12 Cool. Alright. I think we can have it early.
**Ruediger Schulze (IBM)** 17:15 Yeah, have a nice Thanksgiving, with friends and family.
**Morgan McLean** 17:21 Yeah.
**Greg Shriver** 17:21 Thank you.
**Morgan McLean** 17:23 Alright.
**Ruediger Schulze (IBM)** 17:23 Okay.
**Richard Nikula** 17:24 Are you all late?
**Ruediger Schulze (IBM)** 17:25 And you have one as well, right? Okay, thanks.
**Richard Nikula** 17:30 You don't get it, but that's life.
**Ruediger Schulze (IBM)** 17:32 I didn't have.
**Richard Nikula** 17:34 anything to do with that decision, you, you could have…
**Morgan McLean** 17:38 Alrighty, catch y'all later.
**Ruediger Schulze (IBM)** 17:41 Yeah, but…
**Greg Shriver** 17:42 Thanks, everybody.
