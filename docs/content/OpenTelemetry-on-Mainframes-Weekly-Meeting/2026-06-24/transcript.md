SIG: OpenTelemetry on Mainframes Weekly Meeting
Date: 2026-06-24
Duration: 11 minutes
============================================================

## Zoom Recording Transcript

**Robert Pająk (Pellared)** 00:21 Hello, Greg.
**Greg Shriver** 00:38 I'm sorry.
**Robert Pająk (Pellared)** 00:40 And he says, hello.
**Greg Shriver** 00:41 Yeah.
Hey, how are you?
**Robert Pająk (Pellared)** 00:45 Dude, how about you?
**Greg Shriver** 00:47 I can hear you, can you hear me?
**Robert Pająk (Pellared)** 00:49 Yes, I can.
**Greg Shriver** 00:51 Alright, and you're Robert, right?
**Robert Pająk (Pellared)** 00:53 Exactly.
**Greg Shriver** 00:54 Yeah.
lost hope, yeah.
You, you still show up as, yeah.
**Robert Pająk (Pellared)** 01:01 I have no idea why he doesn't remember my trainer.
I'll probably look at it later, also, check.
if I have the same on other cities.
Yeah, I saw that Rodriguez has written that he's out.
**Greg Shriver** 01:18 Yeah.
**Robert Pająk (Pellared)** 01:18 He's still not here for… for this week. He'll be awesome.
**Greg Shriver** 01:21 Right.
**Robert Pająk (Pellared)** 01:23 Is there anything that you want to discuss?
**Greg Shriver** 01:25 I don't have anything for today. I mean, the only thing, I saw some, some notes come across, with the repo, so the repo, I think, is ready to roll.
And I think, I think Rudiga had accepted… A couple of the, modifications, and… But I don't… I… I know… I don't know if he's 100% complete or not, but, I mean, the repo looks like it's ready… looks like it's ready to go.
I haven't had a chance to do anything with it, But, but at least, at least that's progress… at least… at least we're, you know, moving forward, at least with that.
**Robert Pająk (Pellared)** 02:13 I just tried to look at the repo. I think only one PI was merged, which was from Renovate.
Yeah, this is true. They're only renovated pumps, but none of the issues that were created, were actually solved, and I think, yeah, I think…
**Greg Shriver** 02:29 the issues, yeah.
**Robert Pająk (Pellared)** 02:31 Yeah, we have just the issues, and yeah, there has been no progress so far.
Related to that, there have been, conversations in this… in the OpenTLMD specifications meeting regarding the split of the semantic conventions, because the Gen AI were the first.
And there were some concerns raised for the tooling, because previously everything was, you know, as one big, you know, repository, and one tool link, etc.
So, for instance, in OpenThereMat2Go, we are generating the code for semantic conventions, and right now we are missing the, like, the new semantic convention for GenAI.
And there have been some problems, you know, regarding the releases, synchronizing, what if, for instance, you would like to reuse some semantic conventions from upstream?
how it will work, can it be our sync, you know, mixing attributes. For instance, if you would like to use some attributes in your spend, etc, from upstream, and yeah, this question has been raised, and thanks… because Jennai was first.
at least we are not the ones that we will be dealing with, but I think it's worth calling out that there have been since some problems coming with the split.
**Greg Shriver** 03:57 For sure. Yeah, and I wasn't aware of that, so yeah, thank you for… For… for reporting that.
I mean, are…
**Robert Pająk (Pellared)** 04:08 I can put maybe… I will try to find… Maybe I will find something in the submitting notes.
And put it, here.
Yeah, that'd be great.
**Greg Shriver** 04:21 Oh.
**Robert Pająk (Pellared)** 04:24 Let's see recommendations, Altab. So I can just share my screen.
**Greg Shriver** 04:29 Sure.
**Robert Pająk (Pellared)** 04:35 So, this was the agenda topic.
And this is, like, one of the kind of issues that we see, you know, mixing somatic conventions on a signal-signal item, meaning, you know, the fact that You want to have, you know, you have planned semantic conventions for, you know, mainframe, and how we'll use the upstream semantic conventions, how we generate code for this kind of stuff, etc.
Also, the releasing cadence.
as their separate repos, then do you want to have, you know, releases separately? Probably yes, and how it works if it will not conflict? Schema URL, will have different schema URLs? Usually, it was one version, so everything was under one umbrella.
And there is this one, OTAP.
which is kind of related to these issues, and I think they were asked to put more, more, like, potential problems regarding, you know, kind of this, regarding this split here, and there are a lot of open, you know, open comments here.
So maybe I'll just put this.
**Greg Shriver** 05:50 Yeah, 4906, yeah.
**Robert Pająk (Pellared)** 05:52 It just stop.
**Greg Shriver** 05:53 I thought we had that in here, but I guess… I don't see it now, so yeah, if you could add it, that'd be great.
**Robert Pająk (Pellared)** 05:59 Or should I edit any recommendations, and show how you're running this, this doc.
open PRs, or I don't know.
**Greg Shriver** 06:12 You could put it there. It's probably easier to track it there. Usually, if it's something like that, I usually put it in both… in both sections, you know, in, like, the open PRs, or under, you know, meeting minutes for 24th.
I'll add that.
Oops.
**Robert Pająk (Pellared)** 06:38 That's the one child?
Indeed.
Let's go by yourself.
Thanks.
Okay, I'll… And maybe I can also reference This, one issue, which is kind of related.
Oh, yeah.
**Greg Shriver** 07:41 Oh.
**Robert Pająk (Pellared)** 07:43 Yeah, go on, you can continue.
**Greg Shriver** 07:45 Oh, okay.
**Robert Pająk (Pellared)** 08:12 No?
I got you enough?
Bye.
**Greg Shriver** 08:32 Summarized that well.
**Robert Pająk (Pellared)** 08:36 Let's play with that Also, and there's a second one.
**Greg Shriver** 08:41 Okay.
**Robert Pająk (Pellared)** 08:43 Let's go right down.
Yeah, so I think that now we can have this meeting shorter.
And you can take time also to quickly look at this PR and issues. The more feedback, especially in the LTAP, will get, because the LTAP is concentrated on the whole tooling of SAMConf.
Which Josh Surath is working on, so any feedback we put there, you know, as people are actually using it, will be beneficial for them.
**Greg Shriver** 09:22 True, true. Well, to be fair, I don't know that we've used it yet. I mean, we're… But yeah, no, I agree with you. I mean, it makes sense that… and it would probably be helpful for them to know that there are other people that are… willing to be guinea pigs for the federated semantic connections. Are there any other groups besides GenAI and Mainframe that you know of that are…
**Robert Pająk (Pellared)** 09:45 Nope.
No.
**Greg Shriver** 09:48 Okay.
Yeah.
Very cool. Well, thank you for that update. I was unaware of it.
**Robert Pająk (Pellared)** 10:02 No problem.
**Greg Shriver** 10:07 Come on.
**Robert Pająk (Pellared)** 10:19 Sir?
**Greg Shriver** 10:51 Okay.
Alright.
So… Yeah, I don't have anything else for today.
**Robert Pająk (Pellared)** 11:06 Yeah, just nice to see you.
**Greg Shriver** 11:08 Yeah, good to see you, and thank you.
**Robert Pająk (Pellared)** 11:11 Thank you, have a nice day.
**Greg Shriver** 11:12 Yeah, you too. Alrighty.
Bye-bye.
