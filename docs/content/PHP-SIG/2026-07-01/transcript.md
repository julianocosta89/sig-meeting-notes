SIG: PHP SIG
Date: 2026-07-01
Duration: 17 minutes
============================================================

## Zoom Recording Transcript

**Pawel Filipczak** 00:14 Okay.
**Chris Lightfoot-Wild** 00:17 How you doing?
**Pawel Filipczak** 00:19 And… Notes.
**Chris Lightfoot-Wild** 00:22 Excellent. Is, Sergey joining us today, do you know?
**Pawel Filipczak** 00:25 I don't know, I know.
**Chris Lightfoot-Wild** 00:27 Food.
Nice.
No, I think Bob said he was at a wedding this week, didn't he?
From, memory.
**Pawel Filipczak** 00:36 I will ask him, I mean, Sergei.
**Chris Lightfoot-Wild** 00:42 Just give them a minute to work up.
Right, so if Bob's not here, I can, share the screen.
I'll just get that set up just in case.
Just give him another minute, just in case he responds. He hasn't seen your message yet.
**Pawel Filipczak** 01:56 I'm just waiting, so… Interesting. I asked him, that's face.
But I guess we can start.
**Chris Lightfoot-Wild** 02:05 Yeah, sure.
See, I've already added some… oh, no, I'm showing the screen, sorry.
**Pawel Filipczak** 02:19 We're gonna join.
**Chris Lightfoot-Wild** 02:22 I was that, sorry, you can't join today.
**Pawel Filipczak** 02:24 Yeah, yeah, he has some other appointment, so…
**Chris Lightfoot-Wild** 02:28 Anyways… Can you see this? Okay.
**Pawel Filipczak** 02:33 So, from my side, I was working on these construct metrics, you saw, probably.
And, so, it's a first metric package in the country repository, so my question is just about the… the… the folder structure, so it's… I created a new one, so it's, This is the first package, so… If you have any, you know.
quotes about that, or if it fits or not, please let some comments on the pull request. I'll already get some feedback from Nibai, so he reviewed and gave me some clues about… about how to protect Run the batch metrics.
So, get the metrics from the one function run, and then just put it into different dimensions.
But, yeah, it works, so I tested it.
And that's it, so if it's… If it's okay, then we can… we can… we can merge it, or… Improve, whatever we think.
Yeah.
**Chris Lightfoot-Wild** 03:45 Yeah, awesome, I'll take a look. It looks like, obviously, Neve's already done quite a lot, so.
**Pawel Filipczak** 03:49 Yeah, yeah.
**Chris Lightfoot-Wild** 03:50 That's that review, I'm sure I can't pick any thought on it, but I'll, yeah, I'll take a look.
**Pawel Filipczak** 03:56 So my biggest concern is about for the structure and naming of the packages, package on the packages, so that's what I would suggest, you know… I don't know if it's okay for all of us or not, so… So for the auto instrumentations, we had the open telemetry, dash auto, dash the technology instrumented, but now it's… it's… it's a bit different here, so it's… you can take a look into Composer.
And the package time is Opraimetry metrics runtime, so… I guess it's… it should be okay, but yeah, if you have any thoughts, please let me know.
**Chris Lightfoot-Wild** 04:35 Yeah, I guess then the purpose of that, it's just, like, the… Like, sort of internal runtime metrics, not anything user-facing, is it?
**Pawel Filipczak** 04:44 Amen?
**Chris Lightfoot-Wild** 04:45 Yeah.
**Pawel Filipczak** 04:47 Is there a song for me.
**Chris Lightfoot-Wild** 04:50 Cool. Is there any, other SIG that's got similar, in a different language, do you know, at all, or…
**Pawel Filipczak** 04:56 I wasn't checking that. I might… probably I should take a look into the Java or Go. Okay, I will take a look, maybe I will find something.
**Chris Lightfoot-Wild** 05:04 I'll have a look as well, just to check around to see. It's not always obvious, is it, what other SIGs are doing? Well, at least I don't think so.
Maybe I'm not on top of it like what Bob is, going to the maintainer's meetings and whatnot, but… Cool, cool. Yeah, I'll take a look at that.
**Pawel Filipczak** 05:20 Thank you.
**Chris Lightfoot-Wild** 05:24 Okay, well, it's just that one agenda item, so I guess we could go through the board if, else to add to that.
I think… the… did Bob manage to tag the SDK that you'd, added the metric?
**Pawel Filipczak** 05:37 Yes, yes, yes. He asked about merging and releasing, so I didn't get notification, so I let him know today.
**Chris Lightfoot-Wild** 05:47 Okay.
**Pawel Filipczak** 05:48 So both the micro requests should be merged. I mean, the semantic conventions version bump.
And the… the fix for the… for the metrics then… We can make a release.
**Chris Lightfoot-Wild** 06:02 Okay, brilliant.
Excuse me. So, looking at the PRs, a lot of, Renovate stuff near the bottom, but then you've got yourself, a couple there.
Is this one… Oh, yeah, I've looked at it already, Yeah, sorry, I think I added, PHP maintenance so Bob would get notified, so I'm sure.
Nivea and myself have looked at that. Bob can, pick that up when he's back.
Oops, sorry.
A bit keen on the clicking there.
**Pawel Filipczak** 06:48 Hmm.
**Chris Lightfoot-Wild** 06:58 I took a look at this one as well, it looks like an interesting… unfortunate error that I see quite a lot of times, though, in PHP, with the sort of, emptiness check, on this. So… Yeah, I think maybe just tag the… it's a good find, but I'll tag the author and see if, to look at… Fixing the desktop.
I think it was just… A test that was covering the old behaviour, perhaps… Unexpectedly, I suppose.
Mmm… Yep.
I guess it was, called the wrong thing before.
Excellent.
I don't know about this one, so I'll just open a new tab and have a look later. And then, this one you say you've already looked at?
So you've lost…
**Pawel Filipczak** 08:18 Is PR about unsanitized fields. Can you run the… Allow to run them.
Workflows on, on that, PR?
on this avoider, you have in the second tab, avoid collecting unsanitizer. It's waiting for the workflows to run, so…
**Chris Lightfoot-Wild** 08:41 Oh, yeah, yeah, sure, yeah, I think.
**Pawel Filipczak** 08:43 Yep, let's see what… how we'd end up.
**Chris Lightfoot-Wild** 08:46 Yeah, isn't cute.
It's got the CLA as well to sign, but I guess we can see the workflow run fast, and… If it's looking good, ping them.
Awesome.
I'll just go through the country board, and then we can just look at the issues, I guess.
as well.
So yeah, that's that one. I'll take a look at that separately, I'll just open a tab so I don't forget, sorry.
**Pawel Filipczak** 09:20 Hmm?
**Chris Lightfoot-Wild** 09:21 What's that?
Lots of renovate sperm.
Marvel one to take a look at… Yeah, I only… I guess that's partially the problem with some of these things. I just tagged someone else, not knowing if this looked like… You know, it would be an issue or not, so the original author, Hopefully, we'll come back and have a look at that.
I guess it was similar to if, some curl instrumentation issue had arisen.
**Pawel Filipczak** 10:07 And…
**Chris Lightfoot-Wild** 10:07 hopefully tug yourself and, you know… hear back. I think that's what I was trying to… I've not got around to it yet, but the component owners think… To try and have, like, an automated way of, sort of, notifying people when… Things they might be interested in, or have, like, a, you know, ownership toward, is proposed to be changed.
**Pawel Filipczak** 10:31 Sorry, I have to open the door, okay, once again.
**Chris Lightfoot-Wild** 10:33 Yeah, sure.
**Pawel Filipczak** 10:37 She called.
I'm Becca.
**Chris Lightfoot-Wild** 10:53 Oops.
Cool, so PIs, I'll look at some of those a bit later on.
Any new issues? Let's see what we've got.
Sick, sick.
I mean, this is probably a bit outside my wheelhouse, if it's, instrumentation, sorry, the extension.
**Pawel Filipczak** 11:23 I'm the girl.
**Chris Lightfoot-Wild** 11:25 Thank you very much. There was a… additionally, I'd seen, someone was saying they were fixing a build pipeline for 8.6. Is that something you wouldn't mind having a look at as well, with your, You know, expertise.
**Pawel Filipczak** 11:38 Okay, I'll take a look, take a look too,
**Chris Lightfoot-Wild** 11:41 some, you know, write-up about the seaside of things, but I wasn't, I'm not versed in that, so thank you very much.
**Pawel Filipczak** 11:48 review the changes in the, in the Xanthin drain for the 6th, and then I will compare what… what have to be updated here.
**Chris Lightfoot-Wild** 11:56 Amazing, thank you. Are you already, are you in the group for, instrumentation? Like, the…
**Pawel Filipczak** 12:02 I'm not.
**Chris Lightfoot-Wild** 12:05 Okay, no, I just wondered if that was something you'd be interested in, maybe in the future? Not to put anything on here, but…
**Pawel Filipczak** 12:10 Surely not.
**Chris Lightfoot-Wild** 12:11 As our… our local expert.
Yeah, that'd be awesome, thank you. Maybe we should put that in the… I'll just write a message in the PHP admin thing, so when Bob's back, he can…
**Pawel Filipczak** 12:22 Hmm.
**Chris Lightfoot-Wild** 12:23 I guess if he has to propose that or something.
**Pawel Filipczak** 12:26 Yeah, I will ask him on the group.
**Chris Lightfoot-Wild** 12:28 Thank you.
Autogazol, post-tog signature… I feel like this has already been linked to a PR.
Oh yeah, there's ODPR in the country for that, so I'll follow up on that.
And some older stuff that… Doesn't look particularly… Press them, suppose.
Yeah, I've seen about that. Do you know anything about the OTLP profile at all, or…
**Pawel Filipczak** 13:04 Yeah, I was… I was looking into that many, many months ago, how to integrate it, so it requires changing the extension.
And then, just… it's just about passing the context.
So, it's possible to do that, yeah, but… I can try to… to find… get some, you know, summary, and maybe create some plan how to do that.
Yeah.
**Chris Lightfoot-Wild** 13:32 Yeah, I mean, we could potentially put the help required lib on it, just in case anyone comes along and, decides.
They're interested.
But, I guess you've already got, you know, a bunch of other priorities and things first as well, so…
**Pawel Filipczak** 13:46 Yeah.
I designed that for the, for the eBPF profiler integration when it was elastic only, but now it's, it's, it's upstream, so it's in hotel.
So I guess not much changed, but I have to update my knowledge. If it changed or not, I mean the… The symbols in the native code, and then maybe we can integrate it, yeah.
**Chris Lightfoot-Wild** 14:14 Presumably, I guess, there's also someone at Elastic that's a maintainer of that, so that… you've probably got a pretty good chance of getting a…
**Pawel Filipczak** 14:22 No.
**Chris Lightfoot-Wild** 14:23 If needed. More so, myself, anyway.
Cool.
And then this Margo one. I don't think anything's happening on that. I think there was a comment Ugh.
Boom.
Yeah, I'll respond to that.
I had briefly looked at Margo as well. It looks like, from this summary, where they were suggesting that the tooling highlights all the, the differences. It looks like they've got a similar concept to, like, PHP stand and, whatnot, where you can provide a baseline as well.
So we could potentially have something like that in a pipeline, where… You know, we set a baseline for the old stuff to fix later, and make sure that new stuff doesn't… Complete the brick.
But, maybe we can leave that one a little longer, because I'm not sure I've got the capacity either to look at that this second, but.
**Pawel Filipczak** 15:24 Damn.
**Chris Lightfoot-Wild** 15:24 Yeah, I'd be interested to see where it goes with Margot, because… Our… at work, the build pipelines are very slow, so…
**Pawel Filipczak** 15:32 No.
**Chris Lightfoot-Wild** 15:33 That would help.
Cool. Was there anything else there, or do you think we should wrap on that?
**Pawel Filipczak** 15:39 No, not really.
We don't have to look into stats.
**Chris Lightfoot-Wild** 15:45 Oh, I didn't look at the stats, sorry, yes.
**Pawel Filipczak** 15:46 You can, if you want.
**Chris Lightfoot-Wild** 15:48 That little endorphin, yeah, you know, this does.
API is up almost 3 million in a month is pretty good.
**Pawel Filipczak** 16:06 Man, nice globe. Wow.
**Chris Lightfoot-Wild** 16:08 Yeah, definitely. Well, that did remind me, actually, there was, I think… there was a Magento 2 package that got merged in Contrib.
I'll probably have to… I'll probably have to ask Bob about… So I created the repo because the Git split pipeline failed, because that repo didn't exist.
But I'm not… I'm not any kind of, like, maintainer or owner or whatever the terminology is on Packagist, so I can't actually set up the webhooks to sort of align all that, so… I guess I put an action on myself to just check what the flow is supposed to be. Like, I wasn't sure if I was even supposed to create the repository manually, there might have been some other way, so I'll, I'll add that as an action, and then… Ocean.
Call it a… a computer.
Well, alright, that's great. Thanks for your time, and I guess we'll see you next week.
**Pawel Filipczak** 17:28 See ya? Thank you.
**Chris Lightfoot-Wild** 17:29 You too, thank you. Bye-bye.
