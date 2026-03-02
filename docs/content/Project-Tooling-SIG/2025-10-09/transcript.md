SIG: Project Tooling SIG
Date: 2025-10-09
Duration: 24 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 00:47 Hey there!
**jea** 00:48 Ebb.
How's it going?
**Trask Stalnaker** 00:53 Pretty good. How about you?
**jea** 00:57 Good. Just, a lot of meetings today, there's, like, big… this is my,
This is when the operator SIG falls. We do every… we do bi-weekly for that, and so, I have those two meetings, and I have, like, a bunch of other meetings. So, it's my meeting-heavy day.
But… Yeah, not much, going on,
I feel like I've just been… I've also been doing these, like, instrument… these injector SIG meetings.
It's been a whole other day.
**Trask Stalnaker** 01:27 Oh, yeah Yeah, yeah.
**jea** 01:29 button.
And that's, yeah, a lot of… a lot of things.
**Trask Stalnaker** 01:39 Yeah, I wonder if we should go to every other week here.
**jea** 01:44 I think we should. It feels like we were, you know, we don't have, like, a ton of stuff. It feels like, you know, a lot of the stuff that we needed to do is now in place, which is great.
Do we have anything actually, like, outstanding right now?
**Trask Stalnaker** 01:57 So it depends on our… definition of scope.
**jea** 02:07 Well, maybe we'll put more, clearly. Is there anything that you need assistance with right now?
**Trask Stalnaker** 02:14 No, there's nothing, like, there's nothing really… I think ongoing right now.
had put this on the agenda, I've been hesitant to merge all of these things, because I don't have a great sense of…
I don't have a lot of trust in our,
Tests for, essentially, this is the…
I guess the only thing we have, really, in fraud is…
I guess we have the stack overflow. This is… Python, though? Yeah, that's Python.
**jea** 02:58 That also feels like… I think that, like, is broken right now.
**Trask Stalnaker** 03:04 Great.
**jea** 03:06 Oh yeah, that hasn't been working since June.
**Trask Stalnaker** 03:12 Okay.
Do we… Should it be working. Go to the…
**jea** 03:19 I don't think so, that's a good question.
We can ask in the…
**Trask Stalnaker** 03:23 Slack, generally, yeah.
**jea** 03:26 Austin's out, though.
**Trask Stalnaker** 03:31 the last…
Bye.
Just pausing it… June, I see, and if we can use it after Friday, think about…
It's just repeating now.
Yeah, I'll ask.
**jea** 04:04 Hmm.
**Trask Stalnaker** 04:44 Okay… That was a good topic.
So, I just realized, so this is… okay, I was thinking this was… these updates I am not afraid of, because, auto isn't in production anyways.
**jea** 05:25 Yeah, and I thought we also got rid of… which repo did we get rid of?
**Trask Stalnaker** 05:32 We got rid of the Stack Over… there was a separate repo for Stack Overflow.
**jea** 05:37 I thought there was one more. I thought there was also…
**Trask Stalnaker** 05:40 There's the changelog.
But that is a separate repo.
**jea** 06:09 I thought you got rid of a different one. Maybe I'm misremembering, but…
I think Austin posted about it.
Oh, no, no, you got rid of the project infrared team. That's right.
**Trask Stalnaker** 06:21 Oh…
Yeah, but not really. That was an old project infra team. We still have the… the real…
for a team. Yeah.
It should be what we're using in…
**jea** 06:36 Yeah.
**Trask Stalnaker** 06:36 year, yeah.
**jea** 06:37 Oh, it's the first time I've seen this code owner's file as valid. I feel like there's always a problem with these.
**Trask Stalnaker** 06:43 That's because the collector uses a… intentionally has invalid… Code owners…
**jea** 06:53 Cool.
**Trask Stalnaker** 06:57 Do you know what this is?
**jea** 06:59 I think this is something that, like, Adrian had set up?
**Trask Stalnaker** 07:02 It looks like, yeah…
**jea** 07:04 Yeah.
**Trask Stalnaker** 07:05 Well, maybe this is what they're using… For the…
**jea** 07:10 Maybe what they…
**Trask Stalnaker** 07:11 I… C…
**jea** 07:13 Yeah, on, like, the hosted runner or something.
**Trask Stalnaker** 07:19 Okay.
But if I merge stuff, that's not going to break, because they have to actually… it's not, like, auto-deployed there.
Alright, I'm just gonna merge everything that passes the build then.
That was my worry, the reason I was holding off. I… actually, it was the changelog. I thought this was… I think I got this confused with the changelog, which I am kind of afraid to merge things.
Well, not only are they all red.
What are your thoughts on auto-merging?
Version updates.
**jea** 08:25 Oh, it's funny that you ask that, because I've actually gotten a ton of, like… most of the PRs that I've been having to review recently are just Dependabot, or Renovate, or whatever.
**Trask Stalnaker** 08:34 There's so damn many of them.
**jea** 08:36 It's so weird, because it feels like things have been really quiet in the hotel realm for me recently.
like…
A lot of the… I think we're in kind of… it feels like a lot of people are in very, like, deeper research mode.
and, like, stability mode that I haven't had much of an opportunity to get anything else, you know?
**Trask Stalnaker** 09:01 Yeah, the, I mean, the… the Semconv and Java… Instrumentation, repo are always… Chugging.
Always too much.
**jea** 09:18 But I haven't really had much else happening.
**Trask Stalnaker** 09:47 Oh, what's this?
Here, if you… Can look at this guy.
**jea** 10:15 Which one?
Just put it in, the…
**Trask Stalnaker** 10:20 Doc, it's, minimum token permissions.
Oh.
**jea** 10:39 Is there a reason to separate out the permissions for read and write on… the Slack Clean Cache.
**Trask Stalnaker** 10:49 Let's see…
**jea** 10:53 Because there's, like, a permissions… there's a write permission…
In the cleanup, but the whole thing only has read contents?
**Trask Stalnaker** 11:02 Oh, so this is… This overrides this.
This is the route, and so it's not really the, OSSF scorecard,
likes us to add this at the root, even when we have them defined in all of the jobs already. Yeah. They say because if you add another job, you might forget to add explicit permissions.
**jea** 11:33 I see.
**Trask Stalnaker** 11:33 So, it's just to keep the OSSF scorecard happy.
**jea** 11:38 Where can I look at our scorecard? I haven't looked at that in a while. I forget the site. Scorecard.dev, that's it.
**Trask Stalnaker** 11:46 Yeah, but we've got… we've got lean… we've got a dashboard over in the SIG security repo here.
That has them all.
**jea** 11:54 -Oh.
**Trask Stalnaker** 11:59 I'll drop the link.
**jea** 12:00 Is there, like, a, I thought that there was a, like, a site where it showed you, like, the detail view.
**Trask Stalnaker** 12:06 Yeah, if you click on one of these, It'll take you.
**jea** 12:10 That's it, that's it, yeah.
Team Security, open.
Yep.
Approved.
**Trask Stalnaker** 12:42 Whoa…
**jea** 12:43 I forget if I already asked you. Are you gonna be at, KubeCon Atlanta?
**Trask Stalnaker** 12:47 Yeah…
**jea** 12:49 Nice.
Where are you staying? Have you gone to hotels already?
**Trask Stalnaker** 12:55 Yes, it… Don't… remember where to go.
**jea** 13:01 my, partner's also coming, she got a ticket, like, she's getting her company to pay for it, and, because I'm at… in my, you know.
solo founder phase. I'm like, she's the one who's paying for the hotel, and I'm just crashing with her, and so I'm trying to find out where the right place to stay is.
**Trask Stalnaker** 13:23 Give me a minute, and I will.
Tell you where I am…
**jea** 13:43 Oh, I thought there was, like, a way to view… Like, the whole,
An entire org's things, but maybe not.
**Trask Stalnaker** 14:00 put it in chat, it's the Westin…
**jea** 14:03 The Westin, okay.
The Westin Peachtree Plaza, okay.
Thank you.
Signed releases… how hard is it to add in signed releases?
Oh, also, it looks like we don't have… I'm looking at the operators, and it looks like we don't have branch protection on? That can't be right.
**Trask Stalnaker** 14:39 It's wrong about, it can't read the branch protection rules.
**jea** 14:43 Oh.
**Trask Stalnaker** 14:44 doesn't have permission, it's annoying. I've been…
I think once we move to rule sets, it can read them.
**jea** 14:53 Oh, okay.
But yeah, signed releases, how hard is that to do?
**Trask Stalnaker** 15:01 I did it for Java, posting the…
Basically, I think just post… let me see, make sure that it… is checked for Java… Sec… security…
**jea** 15:26 Is there, like, a GitHub action for it?
**Trask Stalnaker** 15:31 No… Although, I would hope that you can do… okay, so…
Yeah, so I posted the… basically the, you know, the MD5 hashes.
To the release artifacts.
So…
**jea** 15:56 Do that manually, though?
**Trask Stalnaker** 15:58 I have it in the automation… in our release automation.
So it publishes this…
**jea** 16:06 yeah.
**Trask Stalnaker** 16:07 here.
**jea** 16:08 Can you send me that?
**Trask Stalnaker** 16:11 Yeah.
**jea** 16:13 You're just doing, like, an MD5 of the, like, release, and that's it?
**Trask Stalnaker** 16:18 Yes, of the artifact that we attach. Now, do you even attach an artifact to your…
**jea** 16:23 We do, I'll show you.
If you go…
**Trask Stalnaker** 16:29 Here, let me just…
**jea** 16:30 To hear?
**Trask Stalnaker** 16:31 R is… B…
Looks like Gradle was already generating it for us, and we just had to copy it over.
artifacts.
**jea** 16:58 Oh, yeah, that's nice.
I wonder if ours just does that. Let me check.
**Trask Stalnaker** 17:04 The other, option, I would hope that
I mean, I think the better way…
Going forward, really, is the GitHub attestations.
Have you seen that?
**jea** 17:20 I don't think so.
**Trask Stalnaker** 17:27 So… Yeah, I mean, this is what I would really…
I would probably do instead, even if it's not
Let's see, I think somebody has a…
**jea** 17:44 Do I need to have an S-bomb for this, though?
**Trask Stalnaker** 17:47 No, I don't think so.
Testation… Yeah…
**jea** 17:59 So, in the workflow that builds the container image, I have the following permissions…
After the step where the image has been built, add the following step.
And then what do you do for the digest? If your workflow uses Docker put, then you can use the digest output. Oh, okay, cool. This actually is pretty simple, I think.
And this will give me the signing?
**Trask Stalnaker** 18:30 I don't know… I mean, it addresses the same use case. I don't know if it'll check the OSSF scorecard, understands it.
But it is the same use case, and it's better integrated into GitHub, so that you can actually… Verify…
**jea** 18:53 Is there an issue for all of these already?
**Trask Stalnaker** 18:56 I dropped a link in chat for this issue, which is about attestations.
**jea** 19:02 Cool.
I will link to that, then.
So… I changed the permissions…
In the workflow that builds the container image you would like to attest, add the following permissions.
Okay, we have, like, a bunch of fucking things that… sorry, we have a bunch of things that,
The build, fortunately.
This may be a little annoying.
**Trask Stalnaker** 19:58 So the other stuff… so we've got all kinds of other random things on our…
Discussion list, but let's save these for next week, when…
**jea** 20:10 Yeah.
**Trask Stalnaker** 20:11 Hopefully Austin is here.
We can talk about…
scope of what we want to do in this group, and potentially moving to… let me put that on the agenda…
Oops, I put that in the wrong place.
Alright.
**jea** 21:03 Cool.
**Trask Stalnaker** 21:05 Good seeing you, as always.
**jea** 21:08 Yeah, you too. Thanks for all the stuff, and yeah, if you need any more reviews, just, ping me on Slack. Always happy to. Jared…
**Trask Stalnaker** 21:17 Sorry.
**jea** 21:18 Whatever.
**Trask Stalnaker** 21:20 done.
**jea** 21:21 Sometimes it's happened.
**Trask Stalnaker** 21:23 Why am I…
**jea** 21:26 That's okay, don't worry about it.
**Trask Stalnaker** 21:29 No, it's horrible.
**jea** 21:31 That's really funny, I changed that already.
**Trask Stalnaker** 21:33 Thank you.
**jea** 21:35 It's okay, you're actually not the first person to even do that this week.
So it's… it's okay. That's so funny, why is J… why is Jared the one that people go for?
**Trask Stalnaker** 21:46 Oh, I don't know, what… What's your last name? Oh, Aronoff, maybe.
What, your last name.
**jea** 21:52 Oh, like, Jared off, and yeah, yeah, you see the jar?
**Trask Stalnaker** 21:55 Or…
**jea** 21:55 Yeah.
**Trask Stalnaker** 21:56 your… is that your GitHub handle? Jarenoff?
**jea** 21:59 Brilliant, yeah.
**Trask Stalnaker** 22:01 Okay. Probably… probably that's the…
**jea** 22:05 That makes a little…
**Trask Stalnaker** 22:05 Switch in my brain.
**jea** 22:07 Yeah.
**Trask Stalnaker** 22:07 Don't worry about it, misfired.
**jea** 22:11 We're all, we're all heads on Zoom, you know, it's, what's it called?
**Trask Stalnaker** 22:16 Oops.
Yeah, well, I do, I mean, every, every time at KubeCon, I'll always wish that the people's GitHub handles was, like, front and center on the badge.
**jea** 22:31 Yeah, that's great.
**Trask Stalnaker** 22:32 I know, like, a lot of people only buy their GitHub handles.
**jea** 22:37 Dude, maybe I'll bring my own little, like, pin or something that is my GitHub handle.
**Trask Stalnaker** 22:44 And also, we need the little say, like, whatever your icon is, that would be perfect, because yeah, like, I do recognize…
icons…
**jea** 22:54 Yeah.
**Trask Stalnaker** 22:56 Even people who have, the random, generic icons.
like, I know which… I know who they are, like, I know this is Lori.
In, you know, the Java repo.
certain ones, I know, like, whereas…
Good… I know James is, yeah, this is James in SEMCON.
**jea** 23:24 That's funny.
When you have the, when people just have the default icons, though.
**Trask Stalnaker** 23:31 But the default icon, they give you one of these random bit… bit things?
Which is nice, because at least there's some…
**jea** 23:44 Yeah.
**Trask Stalnaker** 23:45 Some differentiation.
**jea** 23:49 Maybe I'll try to make my own pin. I don't know how to do that.
But I feel like I could learn.
I have a friend that makes them, so I'm gonna ask him how to do it.
**Trask Stalnaker** 24:02 Nice.
**jea** 24:04 Well, thanks so much. Have a good day. I'll see you later. Same.
**Trask Stalnaker** 24:08 Bye.
