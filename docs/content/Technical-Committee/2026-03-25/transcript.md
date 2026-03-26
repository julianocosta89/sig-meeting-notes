SIG: Technical Committee
Date: 2026-03-25
Duration: 13 minutes
============================================================

## Zoom Recording Transcript

**Reiley** 00:45 Hey, Tiger. Morning.
**Tigran Najaryan** 00:48 I don't Good morning, how are you?
**Reiley** 00:51 Yeah, good, good. How are you?
**Tigran Najaryan** 00:54 Cuth.
**Reiley** 00:56 I wonder how many folks we'll see today.
**Tigran Najaryan** 01:02 But you mean due to KubeCon, they may not be able to join?
**Reiley** 01:06 Yeah.
**Tigran Najaryan** 01:08 No. Okay, let's wait, let's B.
If it's just you and me, we probably should cancel.
**Reiley** 01:15 Right.
I canceled a SPAC meeting yesterday, but for this one, I… Like, I'm curious, like, how many folks will join.
**Tigran Najaryan** 01:24 Yeah.
**Reiley** 01:29 It's 11 a.m. on your side, right?
**Tigran Najaryan** 01:33 Yes.
**Reiley** 01:38 Okay, I'll mute myself and check some email while waiting for people.
And…
**Tigran Najaryan** 01:45 Sounds good.
**Reiley** 01:46 We do have the spike, issue triage, I clicked the link, I don't see anything there, so… both the community and the SPAC.
Inbox are empty.
there are a lot of PRs on the spec repo that we need to assign owners, so if you can take a look, of the… the PRs, there, there may be, like, one or two simple things, just bump some version from dependent bot, like, already approved and set auto-merge, so we just need another approval.
**Tigran Najaryan** 02:22 Okay, I'll take a look.
**Reiley** 02:25 Thank you.
Hey, Army.
Hey.
So, we're… we're trying to see if we can get the quorum today, or we need to move to next week, but meanwhile, Tiger and I already look at the… the community and the TCA inbox and the spec repo. Both are empty, and there are a lot of PRs on the spec repo, that… we haven't put the assignee there, so if you could help, like, there are a couple small PRs that are just, like, security update, like, version bunk or something.
Then… there's a bunch of configuration change and premises-related PRs.
**Tigran Najaryan** 03:21 Yeah, I'm just doing a pass myself, I will self-assign a few.
**Reiley** 03:25 Yeah.
**Tigran Najaryan** 03:26 Maybe you guys can do the same, and if people join, we can do a proper session with assignment. If not, then maybe next time we'll do that. Right. Go over the list properly.
**Reiley** 03:37 Right.
**Armin (Dynatrace)** 03:39 Why are we not reaching quorum today? I think attendance of the TC at this week's KubeCon is not… that…
**Reiley** 03:48 Alright, so, yes.
**Armin (Dynatrace)** 03:49 Wrong, right?
**Reiley** 03:50 Yeah, if we have the quorum, like, let's maybe give another 2 minutes. If we have the quorum, we'll continue the topic discussion. If we don't have the quorum, I think at least we'll do the… the issue, triage, like the TC inbox, and assign the right owner so we can follow up offline instead of waiting for another week.
**Armin (Dynatrace)** 04:08 Okay.
**Tigran Najaryan** 04:09 Okay, sounds good, yeah.
**Armin (Dynatrace)** 04:14 For the Promifos paios, do you think that, David will… Would like to be assigned to them, since he's driving them nonetheless anyway.
**Reiley** 04:23 Right, so for config, like, by default, all of them go to JAG, for premises, all of them go to Divot, and I can also help if it's related.
**Tigran Najaryan** 04:32 Prometheus, the problem is he is the author of the PRs, I think all of them, or most of them. We need someone else, I guess, in that case.
**Reiley** 04:40 The laws are not…
**Tigran Najaryan** 04:42 If there is an assignee, I think we said we're not doing assignees if the author is a TC member, right? So those we should skip, if that's the case.
**Reiley** 04:51 I've been taking care of the metrics related to PR, if that's from Vivid, so don't worry about that.
And he knows he'll always find me, so we're not blogged.
**Armin (Dynatrace)** 05:03 Do we do S&E's full tips?
**Tigran Najaryan** 05:09 And I think that we also said we are not doing, right?
Yeah, yeah.
**Reiley** 05:17 Okay.
**Tigran Najaryan** 05:17 So there isn't much remaining, actually, yeah, if you look at that.
**Reiley** 05:21 Yeah, it's 5 minutes past. I guess we don't have the quorum, so I'll update the meeting notes.
Let people know that we'll… and move the topics to next week.
Okay, thank you both.
Have a good one. Bye.
**Armin (Dynatrace)** 05:37 All right then. Thank you. Bye-bye.
**David Ashpole (dashpole)** 08:18 Hey, Josh.
I'm not sure if anyone else is coming.
**jmacdonald** 08:28 Yes, I think it's KubeCon, and I don't know if we're having a meeting, actually.
I know it's KubeCon.
**David Ashpole (dashpole)** 08:37 I think if we wanted to meet with just 3 or 4 of us.
It'll… it would probably happen, but… I think anything that needs the full group should probably just wait till next time.
**jmacdonald** 08:46 Oh, there goes Riley. I think we're done.
**David Ashpole (dashpole)** 08:48 Okay, okay. Well then, it's good to see you.
**jmacdonald** 08:51 David, David, Simon.
