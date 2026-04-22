SIG: Android SIG
Date: 2026-04-21
Duration: 22 minutes
============================================================

## Zoom Recording Transcript

**Cesar Munoz** 03:33 Hello!
Good morning.
**Jason Plumb** 03:37 Good morning, Cesar.
How are you?
**Cesar Munoz** 03:45 So far, so Hey, Jamie.
**Jamie Lynch** 03:48 Hold on.
**Jason Plumb** 03:59 Let's give it one more minute.
**Hanson** 04:09 Hello…
**Jason Plumb** 04:13 Yeah, Cesar, I got back, last Friday, so I'm still playing catch-up, as you might guess.
**Cesar Munoz** 04:22 Got it.
**Jason Plumb** 04:29 Where's my keyboard?
Alright, that's probably enough time to wait for people. Let's go ahead and get started.
If you have anything, or you think of anything as we're talking, feel free to add it. The agenda's pretty light, so we've got room for other discussions as we want.
First item is Cesar.
Talking about the stabilization effort.
Not this one, this one.
**Cesar Munoz** 05:06 Yes.
Right, so this was the, this is currently the last Item on the milestone for the next release.
The, other ones… Including one requirement to go ahead with this PR.
are already done.
So… I mean, so far as Katala, I think it's got enough approvals.
And it's got the, requirements set up. The reason I haven't merged it is because you had some concerns, Jason, and… It's about.
**Jason Plumb** 05:48 I know, and then I just appeared, I'm sorry.
Yeah.
**Cesar Munoz** 05:51 Yeah, yeah, it's a pretty big change, so that's why I didn't want to just merge it.
You know, willy-nilly.
So… But I think the concerns that you had Especially regarding with session stuff, are already addressed, so…
**Jason Plumb** 06:09 Yeah, because of this one, right? Like, and this is based on former SIG discussions that we had around that being okay, right? If we're stabilizing… if we're looking to stabilize the instrumentation API, and that new API does use or leverage the session, then the session needs to be stable, which is what this one did.
And I think we're okay to move forward on this, you know?
**Cesar Munoz** 06:35 Sounds good.
**Jason Plumb** 06:36 Yeah, I think… yeah, I think you have the approvals, and we've talked about it enough that I think… I think it's okay. I mean, I think it's a path forward. Yeah.
**Cesar Munoz** 06:46 Got it. Okay, so I'll go ahead and merge it.
**Jason Plumb** 06:51 Yeah, there hasn't been any other changes recently other than just rebasing or whatever, yeah.
I think that's fine.
**Cesar Munoz** 07:00 Awesome.
**Jason Plumb** 07:02 And then we could do a release, I think. There's nothing else in this milestone, as you mentioned, so…
**Cesar Munoz** 07:10 I created another PR, which was related to… It's something I mentioned last week's meeting.
which I'm really concerned about how long we… You know, provide this crash reporter with essentially the wrong name at this point.
Because to me, this is… This is probably the most… Popular or most used instrumentation, probably.
Alongside HTTP.
So, it seems like we at least… You know, settle on a name that doesn't seem like causes any concerns.
So, I wanted to… update the code as… you know, I think the sooner the better.
**Jason Plumb** 08:02 App.crash is what we're working toward, and what do we have today?
Device.crash.
Which, yeah, this is even more accurate, right? It's more specific. Your whole… your whole device is not crashing in this queue.
**Cesar Munoz** 08:15 Our device is not gonna crash, yeah.
**Jason Plumb** 08:17 Yeah.
**Cesar Munoz** 08:18 Now, Hanson, I don't know if you've seen… The messages… Icend, but it's… the… like, your PR in semantic conventions is almost ready to go, it's just that it's got some CI failures, so it's probably why.
**Hanson** 08:34 Yeah, schema check added another thing where it doesn't work well with… it requires Docker, so I'm trying to… I'm trying to generate that. I'm running all the makes. I had to fix it last time.
And now that there's another one, I either have to fix it, or find the specific thing that, like, skips schema check and see if there's any other things that it tried to run.
**Jason Plumb** 08:58 To this thing? Is this what we're talking about?
**Hanson** 09:00 Yeah. Schema check doesn't run, locally, it's not, it's not a Docker broadband failure, but… so, no, I should say, the dead, the, the dead YAML check doesn't run locally. there's a, there's a, there's a, there's an error.
And make all fails, because schema check fails, and schema check is failing because of, again, the pod man versus, thingamajig detection, so I'm gonna try to figure out locally to see how I can generate, one of the markdown files that doesn't have, the generated app.event. So, Yeah, been trying to do it this morning. I didn't check last… I assumed that I should have checked, I assumed it went in, but It didn't, because.
**Cesar Munoz** 09:50 I mean, this project has changed so much, semantic conventions, CI and stuff, and… You know, yeah.
Yeah.
**Hanson** 09:59 It worked last… it worked last… I mean, I can generate… like, I had to fix, a bunch of stuff to just generate, the… the YAML and the specific markdowns is, like, a new one that came up, so I'm gonna try to… I'm gonna spend today and try to figure that out. It's… Yeah, if you could somehow run… I need to generate that specific, markdown, from the YAML, and I've tried running… Anyway, I'll fix this. I'm gonna submit another check upstream to fix the, the pod man versus, Docker thing. Docker. Got it. But yeah.
**Cesar Munoz** 10:41 Got it, thank you.
**Jason Plumb** 10:41 Hanson, if it helps, if you're… if that's really a pain, you and I are in the same time zone, I might be able to make a PR into your branch.
If, like, if I can run the tools just fine, then I can maybe find it in PR under your branch, if that's helpful.
**Hanson** 10:55 That would be extremely helpful, if you could just pull my branch down, generate, a thing, and then contribute to it.
**Jason Plumb** 11:03 Yeah, let me… let me try that. I have to do it probably at 9.30, but I'll see what I can do.
**Hanson** 11:11 I'm gonna spend the time trying to fix it locally, and if I can, that'd be really fantastic, because…
**Jason Plumb** 11:16 Just… just keep me posted.
**Hanson** 11:17 Yeah. Am I the only person that uses a setup locally that doesn't have Docker, or has Podman set up in such a way… ugh.
**Jason Plumb** 11:27 You are, yeah, sorry, I hate to break it to you.
**Cesar Munoz** 11:30 I haven't used Podman.
Yet.
**Hanson** 11:33 The…
**Jason Plumb** 11:35 I run Podman on my personal stuff.
**Hanson** 11:38 Like, there is support for Podman, it's just not… not everybody… supports.
**Jason Plumb** 11:44 Yeah.
**Hanson** 11:44 Yeah. CI doesn't need it. That's the thing.
And I suck at… I absolutely suck at all this config stuff.
Oh, yeah.
**Cesar Munoz** 11:57 And it keeps changing, so… Anyway… It ran fine!
**Hanson** 12:01 I did it last month. This schema check thing is new.
**Jason Plumb** 12:05 So, I wonder…
**Cesar Munoz** 12:06 just to mention, I mean, the McCration renaming, it… It's a nice-to-have for this release, but it's not a must, I guess, because I don't want to rush. I mean, it's probably better to wait for the semantic conventions PR to get merged before merging this.
Yeah, I agree.
**Jason Plumb** 12:24 I agree.
**Cesar Munoz** 12:25 It will be nice, but if it's not, I guess it's fine to skip this release.
**Hanson** 12:31 Yeah, sorry.
**Jason Plumb** 12:33 Yeah, because this is a breaking change, right? Anybody who has stories. Yeah, any, any.
**Cesar Munoz** 12:38 Yeah.
**Jason Plumb** 12:39 Using this crash event or looking for crash events is gonna break when this happens, so… I think it makes sense to have it in semantic conventions first, yeah.
**Hanson** 12:48 Well, folks need to change their dashboards to basically take both anyway, because it's gonna be a long tail of device.crash coming in, so…
**Cesar Munoz** 13:00 Yeah.
**Hanson** 13:01 Nothing's clean with mobile.
**Jason Plumb** 13:04 Alright, so, I mean, we're talking about the release, yeah, we're at 2 months now, we should have released last month, and we didn't, for all the reasons. So I think we should prioritize getting it out this week, and it sounds like we're close. It sounds like this'll go in, we've already stabilized session. We're not stabilizing the instrumentation API in this release.
We're making these changes, but we're not yet marking it stable, is that correct?
**Cesar Munoz** 13:30 been so long. I think, no, I don't remember adding.
**Jason Plumb** 13:34 I think, I think Noah as well.
**Cesar Munoz** 13:36 Dough, yeah, yeah, I know.
**Jason Plumb** 13:37 Okay.
I don't see the properties file.
Okay, that… and I'm fine with that, we can work toward that next re… next month, right?
**Cesar Munoz** 13:47 Yep.
**Jason Plumb** 13:48 Okay.
**Cesar Munoz** 13:50 Yeah, we can release… make it stable.
Later, but I do believe we should merge that VR before the next release.
**Jason Plumb** 14:00 I agree, yeah, yeah.
We have to, it's part of the milestone.
**Cesar Munoz** 14:06 Got it, so… I'll do it later.
I'm gonna be off… essentially for the rest of the week, so I won't be able to help with the release, but…
**Jason Plumb** 14:21 Okay, I will… I will take care of it today. Yeah.
**Cesar Munoz** 14:26 Thank you.
**Jason Plumb** 14:27 Unless, yeah, the only thing I can think of is if anything else pops up around this, but I think it's… I think it's in pretty good shape, and then the other one around the semantic invention, I think, is in good shape. So, not this one, but this one, yeah.
**Cesar Munoz** 14:41 Cool.
**Jason Plumb** 14:42 Okay, I think there's forward progress then, and we'll get it out this week.
Okay, David, dropped something onto this. I think this is an… I think this is a long-standing PR, or no? Let's see… Yeah, a little, little old now. Okay.
Would you like to talk more about this one?
**DavidGrath** 15:09 Okay, can I hear you?
**Jason Plumb** 15:12 Yeah, it's pretty… pretty quiet.
**DavidGrath** 15:16 I'll try and project my voice a bit. That helps. And also, this is a con… okay. So this is a continuation of the… Issue 1576, was it? That somebody was asking for additional gesture supports, things like scroll and zoom.
bootstrap as well, so I said that I would That's off by walking on the hook.
And then we'll see where it goes from there. So, first of all, creating my own instrumentation, but then Thompson reviewed it.
**Jason Plumb** 15:56 I think you've… I think we've lost you, or you broke up quite a bit. It was… it was pretty hard to follow, but yeah, this is new instrumentation. There was some enhancements, I think, that were being made.
**DavidGrath** 16:05 We're just this.
And instead, just add an extra duty to the sheets, so in the kids don't…
**Jason Plumb** 16:16 I'm having a really hard time hearing you, sorry.
**DavidGrath** 16:21 Creating a new experience.
**Jason Plumb** 16:29 I don't think that we're able to hear you, David, yeah, sorry. So, I appreciate you pointing this back out, back… pointing this, pointing to this, and bringing this topic back up again, because I think it has gone a little bit, stale, but I'm not sure why James Thompson is jumping in on this PR. He mostly works on the SEMCOMF, so I'm guessing he's just… picking on SEMCOMF stuff, so… I mean, yes, let's give some approver review… eyes on this.
So that it's not just a semantic convention review.
And we'll go from there.
So thanks for the nudge. Yeah, it's been a little… it's been a little slow in the last couple of weeks, so I'm sorry it hasn't been, hopefully, as quick as it should have been. We'll give it some attention.
Okay.
What else?
**Cesar Munoz** 17:41 I just remember… I think there was a PR… somebody created around, TLS certificates.
I'm not sure if we want to include that.
**Jason Plumb** 17:59 I'm hesitant to add anything else to the milestone, but if this is low-hanging fruit, and it has been approved.
Alright, this was a little bit contentious, I wish… But…
**Cesar Munoz** 18:10 It is, yeah.
**Jason Plumb** 18:11 Yeah, I wish Manuel was here, because I think he felt the strongest about it.
Right, and the point of this one being, this is for client certs, right? So you can put a client cert… into your app.
Then the exporter will use that. The server side can then verify the client cert, to which the response is, well, it's not secure, because it's on your app, and anybody can just pull that client cert, and then forge data from any other app or any other system. And it's a valid point, but it's, like, another… it's another hurdle, it's another step of, like.
At least having some expectation of… authenticity, from the sender side. So, I… yeah.
I didn't… I don't think I saw this comment. What is this about, Jamie?
Sorry.
It's unplugged, yeah, it's unpl.
**Jamie Lynch** 19:06 Yeah, fingers.
**Jason Plumb** 19:06 Okay.
**Jamie Lynch** 19:07 Yeah, it's not… it's just kind of, like, a style thing, really, rather than anything fundamentally against that.
**Jason Plumb** 19:16 Cool, and this is instrument… This is Agent?
Where… where is that code?
**Cesar Munoz** 19:25 Is that the DSL?
Yeah, from the.
**Jason Plumb** 19:27 Yeah, oh, but it's incubating, so we could… Yeah, we could still change this to an interface, and it wouldn't be breaking in the future. Okay, so… Let's get… yeah, there's… there hasn't been any comments on this for quite some time.
And without Manuel here to defend himself, I think we should merge it.
**Cesar Munoz** 19:47 From my side, this is something I've never used as an Android developer, usually… the idea… Behind doing these kinds of stuff is that you might expose a security risk.
Because you're… Packaging your key, your certificate with your app, which can be easily unpackaged, but… I mean, yeah, I don't know. Probably, as you say, definitely if somebody created a PR, it's because it's useful.
For some use cases, so… Yeah.
**Jason Plumb** 20:24 I think they responded to it too, right? So, like, yeah, they know about the problems with embedding secrets.
it's not just a static key, it's mutual TLS, you know. There's some sort of, like, OS-level key store where they can put it, which makes it harder to get to, I guess?
So, you know, I think this is a very valid response. It sounds like they know what they're doing. So, I mean, this seems like a good change to me.
Alright, I'm gonna merge it.
Going one.
**Cesar Munoz** 20:57 Let's go.
**Jason Plumb** 20:57 Yeah, okay.
Alright, that'll be in the release, that's good. This is gonna be a big release after 2 months, oh my gosh.
Is there anything else in here that we also want to cram into this chunky release?
**Hanson** 21:13 Seems like you're putting your thumb on the scale of not cramming anything in, so…
**Jason Plumb** 21:17 I know, I know.
Okay… There was… oh yeah, there was… every time we do a release, there's, like, one little bit of automation that doesn't fill in a version correctly, so maybe, cross your fingers, maybe this time it will work.
**Cesar Munoz** 21:48 Yeah, I think you fixed it the last time.
**Jason Plumb** 21:50 I think I've fixed it, like, 3 times, so…
**Hanson** 21:54 Or maybe this time, some branch protection stuff can stop you from releasing.
**Jason Plumb** 21:58 Oh my gosh.
Okay, well, I don't think we have to draw this out anymore, if we're all content with this. Cesar, one of you back? You're back next week?
**Cesar Munoz** 22:13 Yeah, on Tuesday.
**Jason Plumb** 22:15 Okay.
Sounds good.
**Cesar Munoz** 22:20 So, see you in the next… in the next meeting.
**Jason Plumb** 22:23 Alright.
Take care.
**Cesar Munoz** 22:25 Thank you. Hey.
