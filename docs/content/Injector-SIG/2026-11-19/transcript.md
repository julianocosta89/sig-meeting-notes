SIG: Injector SIG
Date: 2026-11-19
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Diego Hurtado (Dash0)** 00:33 There you are.
**Michele Mancioppi (Dash0 Inc.)** 00:36 Here I am.
**Diego Hurtado (Dash0)** 00:40 Hey, Chief, I didn't know the, the Bunchik bag behind me, bothered you, I mean,
**Michele Mancioppi (Dash0 Inc.)** 00:45 Oh, I just, I need an example of something vexing, so…
**Diego Hurtado (Dash0)** 00:49 Yeah, because, It's, the… Yeah, it's pretty heavy and pretty installed there, I don't think I can move it anywhere, you know?
So… yeah, I think I'm… I'll just… I'll just be vexing.
**Bastian Krol (Dash0 Inc.)** 01:15 Hello.
**Diego Hurtado (Dash0)** 01:16 Hey, Bastian.
**Bastian Krol (Dash0 Inc.)** 01:18 Digo Michele.
**Michele Mancioppi (Dash0 Inc.)** 01:20 Hi,
**Bastian Krol (Dash0 Inc.)** 01:21 Alright, honey.
This is a Des Zero meeting, what's going on?
**Michele Mancioppi (Dash0 Inc.)** 01:27 Antoine is, is busy, adulting somewhere else.
I don't know where Jack is… Or where Nikola is?
**Bastian Krol (Dash0 Inc.)** 01:37 Nikola, I think, said he cannot make it… Yeah, he said yesterday, and it's, like, an off-site and can't make it.
**Michele Mancioppi (Dash0 Inc.)** 01:47 True. So we can probably keep it, and if Nico is on an off-site, so is, so is Jack, so we can keep it very.
**Bastian Krol (Dash0 Inc.)** 01:53 Probably. Although I have a question for Jack about his spec PR, but that can also wait.
Yes.
**Michele Mancioppi (Dash0 Inc.)** 02:02 So, let's look at the open issues, if there's something new, exciting.
**Bastian Krol (Dash0 Inc.)** 02:10 I started with this.
you ask. What?
**Michele Mancioppi (Dash0 Inc.)** 02:15 This is not new, but very exciting.
**Bastian Krol (Dash0 Inc.)** 02:17 It's exciting, yeah, I think… I think there's, CloudFaults on some good ways. So we… what we will do, probably, is to… to check the… what the executable exports, and that is probably good enough to detect whether it's actually Node.js, or Deno, or something else, so… This has all become much easier if someone else does the hard syncing.
**Michele Mancioppi (Dash0 Inc.)** 02:48 This one I made…
**Bastian Krol (Dash0 Inc.)** 02:54 But…
**Michele Mancioppi (Dash0 Inc.)** 02:55 So this one, I actually was testing the injector in one of my infiniteKind clusters.
And, I had a problem with, Mounting the configurations of the injector over a config map.
Because siblings were not followed.
Because at some point, we made a change to avoid, checking, directories.
Then we say it has to be a real file.
And a SIM link is not a real file, and then.
**Bastian Krol (Dash0 Inc.)** 03:27 Hmm.
**Michele Mancioppi (Dash0 Inc.)** 03:29 But this might need revisiting.
**Bastian Krol (Dash0 Inc.)** 03:31 No. Is there any reason why we restricted it to real files? Probably on accident, or…
**Michele Mancioppi (Dash0 Inc.)** 03:38 It was an overcorrection. We,
**Bastian Krol (Dash0 Inc.)** 03:40 Yeah.
**Michele Mancioppi (Dash0 Inc.)** 03:41 We went with, oh, real files are the real deal, and I did not think of Sunix.
**Bastian Krol (Dash0 Inc.)** 03:47 I didn't even… don't even remember that we… Made the change. Yep.
**Michele Mancioppi (Dash0 Inc.)** 03:54 So that one, I will unleash Claude on it.
**Bastian Krol (Dash0 Inc.)** 03:57 Nope.
**Michele Mancioppi (Dash0 Inc.)** 03:59 This has… This actually is not a fix in, This doesn't need a fix in the injector, right? It's only packaging.
**Bastian Krol (Dash0 Inc.)** 04:12 Probably, so… What, what did they do? Just… because I'm curious, it's now registered CJS? Just the file ending changed?
**Michele Mancioppi (Dash0 Inc.)** 04:27 I proceed to this.
And, I opened IPR for backwards compatibility, which… As zero people looked at.
Okay, that's neat.
Bloop.
So…
**Bastian Krol (Dash0 Inc.)** 05:02 But, I mean… Even without that fix, in packaging, you know which version you package, and you know which path, so that's easy to solve there, right?
**Michele Mancioppi (Dash0 Inc.)** 05:12 Aging is already solved.
**Bastian Krol (Dash0 Inc.)** 05:14 Got it.
**Michele Mancioppi (Dash0 Inc.)** 05:15 It's fixed.
Now the question is, do we need to fix anything inside the injector codebase?
**Bastian Krol (Dash0 Inc.)** 05:24 wouldn't think, so we don't handle concrete past the user anymore as…
**Michele Mancioppi (Dash0 Inc.)** 05:31 Yeah, right?
**Bastian Krol (Dash0 Inc.)** 05:31 Just as I remember, it's… the default is the empty string, and you need to set it to some actual string.
To enable injection for a specific runtime, so it should all be in packaging.
That's just from my memory. That's… It's probably all tests. I would guess at the unit tests inside ZIG, but I might be wrong, but since it appears so often.
And it's not at the top of the file?
**Michele Mancioppi (Dash0 Inc.)** 06:01 Configuration MD… So it's, we should update to the latest one.
**Bastian Krol (Dash0 Inc.)** 06:07 Yeah, probably the docs, that could be a thing.
**Michele Mancioppi (Dash0 Inc.)** 06:11 Yeah, let's, comment on the issue of that.
No, the fix came in with 082.
It's been an earlier PR.
this.
Yes.
Okay. Basti, do you want to take this one?
Kriti, please.
**Bastian Krol (Dash0 Inc.)** 08:23 Well, I decided to…
**Michele Mancioppi (Dash0 Inc.)** 08:35 This one, I, it's like 2 weeks that I tried to go to VHP SIG, and then my calendar lies to me, because they moved it at 8.30 in the morning.
So today, I was like, today's the day I go there, and then I logged in, and there is nobody.
**Bastian Krol (Dash0 Inc.)** 08:51 Okay.
**Michele Mancioppi (Dash0 Inc.)** 08:55 Yes.
Meet jacob, lost in the fog.
And now that Terra has been acquired by Kribo, maybe he has more time?
That's it, right? Do we actually, in this one, do we actually need to do something about it?
**Bastian Krol (Dash0 Inc.)** 09:35 I have zero recollection of what this was about. It's from May.
**Michele Mancioppi (Dash0 Inc.)** 09:41 Lana?
**Bastian Krol (Dash0 Inc.)** 09:43 I don't know.
**Michele Mancioppi (Dash0 Inc.)** 09:44 The CAIC configure being deployed by OPAMP to override the current values.
Pasting case when YAML has performance implications, we call the comp.
Supported graphic config file type.
Solution, social insurance…
**Bastian Krol (Dash0 Inc.)** 09:58 We discussed that before in… which… which number is it?
Let me search the again now.
Yeah, we discussed it in May. I'm clear if the person posting the issue wants to configure the injector via declarative config, don't support that, or just have the injector forward a declarative config.
**Michele Mancioppi (Dash0 Inc.)** 10:22 I mean, that already exists, you can just put what Jack says, right?
**Bastian Krol (Dash0 Inc.)** 10:26 Yeah, and I think that is probably the outcome of our discussion, so that question from Jack, and then he never… so the original author never got back to us?
So maybe we just… Close it if… if he doesn't care.
Get back to us.
Yep. Excellent.
**Michele Mancioppi (Dash0 Inc.)** 11:04 This is another banger.
**Bastian Krol (Dash0 Inc.)** 11:06 Yeah.
Whatever.
What is this giant comment, officer? It's your giant comment.
I think this can just sit in the issue list for a few more months, and… Is there anything in the pull requests that we should take a look before we take a look at very old issues?
our drafts, and that I think I commented on… on… no, that's new, right?
**Michele Mancioppi (Dash0 Inc.)** 11:56 That's new?
**Bastian Krol (Dash0 Inc.)** 11:57 That's new, I didn't look yet.
There's probably the follow-up change from… from the…
**Michele Mancioppi (Dash0 Inc.)** 12:03 Yeah, actually…
**Bastian Krol (Dash0 Inc.)** 12:04 generation stuff.
**Michele Mancioppi (Dash0 Inc.)** 12:05 I reviewed it today, and We don't like it very much, but this section looks misplaced to me. And actually, I would die on the hill of requiring that in Markdown documentation, we write one full sentence per line so that kit actually works.
**Bastian Krol (Dash0 Inc.)** 12:25 Yes, that's very, very much, to my liking. I do that also because otherwise this look shit.
I would actually go so far and say one sentence per line and 120 characters max, but that's just… Met off taste.
**Michele Mancioppi (Dash0 Inc.)** 12:45 Defy, pros… Logic.
If I press rules… Notation.
**Bastian Krol (Dash0 Inc.)** 13:07 I mean, that's easy to just reflow existing doc sets.
**Michele Mancioppi (Dash0 Inc.)** 13:13 Yes.
**Bastian Krol (Dash0 Inc.)** 13:14 Can be automated very nicely.
**Michele Mancioppi (Dash0 Inc.)** 13:17 1… 4… Santos.
Combined, and I vote for the foot.
Do you want to make the honors?
Or should I? Because I love to open these things.
**Bastian Krol (Dash0 Inc.)** 13:40 No, it's fine, Obmet.
**Michele Mancioppi (Dash0 Inc.)** 13:42 I will… I will open it, and then you, you, you voted.
**Bastian Krol (Dash0 Inc.)** 13:46 I, I, I reviewed and, and directly… implemented.
**Michele Mancioppi (Dash0 Inc.)** 13:51 Excellent.
**Bastian Krol (Dash0 Inc.)** 13:52 Any further discussion?
**Michele Mancioppi (Dash0 Inc.)** 13:54 Because it's obviously correct.
**Bastian Krol (Dash0 Inc.)** 13:56 Yes.
**Michele Mancioppi (Dash0 Inc.)** 13:59 There is no need of discussion since it is obviously patently correct.
This one is waiting on, I now remember his Jack.
James.
**Bastian Krol (Dash0 Inc.)** 14:13 Yeah, that's the same guy that we just had, and I even pinged him, like, one week back or so. I think we should just do it on our own, without waiting.
**Michele Mancioppi (Dash0 Inc.)** 14:24 I think we could open the data source here.
**Bastian Krol (Dash0 Inc.)** 14:30 Because right now, it's broken. There's already a 17.1 release, and what I did previously with the script also did not work, because that failed at the CLA check.
And so we never recognized that there was a music release.
**Michele Mancioppi (Dash0 Inc.)** 14:51 Then we just maybe opened the PR to… to renovate for SIG.
**Bastian Krol (Dash0 Inc.)** 14:59 Yup.
Hallelujah.
**Michele Mancioppi (Dash0 Inc.)** 15:03 I'll take that.
Good.
District enclosed, right?
**Bastian Krol (Dash0 Inc.)** 15:24 Yes, this is… garbage.
**Michele Mancioppi (Dash0 Inc.)** 15:29 And, this one, we miss Antoine to make fun of.
**Bastian Krol (Dash0 Inc.)** 15:34 That.
Next time.
**Michele Mancioppi (Dash0 Inc.)** 15:36 Next time, yes. He's avoiding me because I asked him about external kicks.
Oh, I never noticed that also PPC.
Oh, that's even funnier.
What is AIX?
**Bastian Krol (Dash0 Inc.)** 15:50 Good point.
**Michele Mancioppi (Dash0 Inc.)** 15:53 What about AIX?
All right.
**Bastian Krol (Dash0 Inc.)** 15:58 Good. I think that's probably… Good enough for today.
**Michele Mancioppi (Dash0 Inc.)** 16:05 other… each other a few minutes to open PRs and merge them right away.
**Bastian Krol (Dash0 Inc.)** 16:09 Right.
**Michele Mancioppi (Dash0 Inc.)** 16:12 Bye, folks.
**Bastian Krol (Dash0 Inc.)** 16:13 Bye-bye!
**Diego Hurtado (Dash0)** 16:14 Hey, Michele, Michele, can you stay for a second, please?
**Michele Mancioppi (Dash0 Inc.)** 16:17 Yes.
If it is, if it is, not Injector business, then, we don't talk here.
**Diego Hurtado (Dash0)** 16:27 I mean, it's packaging business, so it's kind of related.
**Michele Mancioppi (Dash0 Inc.)** 16:30 Oh.
Yeah, let's, let's not do it in the wrong… in the wrong SIG. How do you…
**Diego Hurtado (Dash0)** 16:37 Alright.
See you in Huddle?
