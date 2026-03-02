SIG: Kubernetes Operator SIG
Date: 2025-10-09
Duration: 32 minutes
Zoom Recording URL: https://zoom.us/rec/share/7qrGHHvJFNE3LuZ1fyFBBW_xKCfPSUVdjpUdsx2zxTyo4nMJuuZeNrRZqWOA1-ox.knwesufcDhkyq21d
============================================================

## Zoom Recording Transcript

**yurioliveirasa** 00:16 Hello?
Hello, T-Mobile.
are doing…
**Timo Johner** 00:32 Ayy.
Good, how are you?
Boom. Can you hear me?
**yurioliveirasa** 00:42 No.
**Timo Johner** 00:43 Okay… Oh, that's weird.
One second…
Doing those out?
No?
**yurioliveirasa** 01:12 Test, task, test, task, can you hear me?
**Timo Johner** 01:14 I can hear you, can you hear me?
**yurioliveirasa** 01:18 Now I can hear you back.
**Timo Johner** 01:20 Okay.
That's weird. No, I'm not sure if it was me or you. Probably it was me.
**yurioliveirasa** 01:26 Yeah, I don't know. Hi, Jenny.
**Timo Johner** 01:28 Doesn't matter. I'm good, how are you?
**yurioliveirasa** 01:31 Yeah, I'm doing great. Yeah, nice to meet you.
Hey, David.
**Timo Johner** 01:37 Okay, first time attending.
**yurioliveirasa** 01:41 Yeah, you're very welcome.
**jea** 01:44 Hello both. Please add yourself to the agenda if you got anything. I'll just copy the link in the chat here, in case you need it.
**yurioliveirasa** 01:57 Nope.
New apartment, Jacob.
**jea** 02:10 It's here, nice, I have a lovely tree right outside my window, so…
**yurioliveirasa** 02:17 Oh, but you…
**jea** 02:18 I was removed.
**yurioliveirasa** 02:19 Yeah, that's good. Yeah, that's good. Yeah, finally got settled, right?
**jea** 02:26 Yeah, finally. How did yours go?
**yurioliveirasa** 02:29 Oh yeah, same for me. Yeah, yeah, I'm settled, yeah, everything is done, yeah, but, yeah, those moves, and in my case, yeah, actually a country movement, it was, yeah, pretty, pretty stressful, but now it's.
**jea** 02:43 Yeah.
Yeah, but now… it's over.
**yurioliveirasa** 02:47 Yeah. Get back to the contributions.
**jea** 02:51 Not what I'm saying, not what I'm saying.
Well, let's see what we got here.
Okay, whoop.
**Timo Johner** 03:08 That was me, sorry.
**jea** 03:19 Let's see…
**yurioliveirasa** 03:35 Good morning.
**David Ashpole (dashpole)** 03:39 Sorry about that.
**yurioliveirasa** 03:42 Not a problem.
**jea** 03:45 No worries.
Yeah, so David, do you want to kick us off? I think we're gonna have pretty light attendance today, like, Mikolai's out, I think a bunch of other folks are in, like, longer meetings, like the Red Hat folks, I think, are all in, like, meetings.
Right now.
**David Ashpole (dashpole)** 04:00 Cool. I just wanted to…
Stop by, say hi. I was recently added to the TC.
So, and one of the things,
one of the SIGs I'm gonna be connecting with is the operator SIG, so… yeah, thank you.
**yurioliveirasa** 04:15 Yep.
**David Ashpole (dashpole)** 04:16 And if you need anything from the TC, or…
I'm not sure how involved I'll be yet, but I'll try and come occasionally, at least.
Try and keep tabs on what's going on. But, yeah, just stopping by to say hi, and
You guys do great work, so keep it up.
**yurioliveirasa** 04:32 Yeah, take it, David.
You're on mute. You're on mute, Jacob.
**jea** 04:40 Does that mean that you're…
taking over for Jirassi, or maybe I'm…
**David Ashpole (dashpole)** 04:46 I think it was… I think it… yeah, he's… so GC is still gonna connect with you primarily about, like.
I don't actually know, as well, the dividing lines anymore, but if you have things that are spec-related.
that you have questions about, then, like, I'm your escalation point there. And I will try and be
involved at least a little bit, so that I know, like.
what you're doing. I think the GC is probably gonna keep tabs more on, like.
how is contributions going? Is the SIG healthy? And I don't care at all about that, so…
**jea** 05:22 It doesn't matter. Well, that sounds great, so, thank you. I think…
**David Ashpole (dashpole)** 05:28 taking over from Tigrin, is the.
**jea** 05:30 Oh, Tegan, he's been too busy for a long time.
**David Ashpole (dashpole)** 05:34 So, yeah.
**jea** 05:35 It's good to have some more hands in.
I think the only thing that is of mild interest to you, potentially, that's, like, semi-spec related, would be the work that I'm doing with, Antoine over in the injector SIG.
That's, like, a long project. There's quite a horizon there, so don't… like, there's not, like, a rush on it. The biggest pain point that I think we've had in the past year or two.
Is around, like, the semantic convention versioning changes between languages.
So the ways that, like, Java and .NET decided to do, major version changes and not really have, like, backwards compatibility options has made our life…
more difficult in that regard. And so…
there's also sort of this, like, simultaneous story. If Mikolai were here, he has a lot of thoughts on this, so I'll maybe let him say more of them. The gist of it, though, is that
And this is where it connects to the, injector SIG, is that we want to have better, like, cross-SIG standards for, testing and, like,
versioning, essentially, such that, we don't… right now, we maintain all of these images on behalf of these SIGs, so that when there is a breaking change, it's, like, weirdly on us, and we have to go to them, and it's kind of this odd, this odd relationship.
**David Ashpole (dashpole)** 07:05 Is this for auto instrumentation agents?
**jea** 07:09 Yeah, and so I think, better coordination with them would be… would be really great.
**David Ashpole (dashpole)** 07:15 Okay.
**jea** 07:16 But that's, like, a… there's a much larger story there. Again, Mikolai would be, like, the point person for that. He's definitely the most, passionate and aware of those problems. Not that I'm not, but, like, he has…
more… he's looked into this a lot more than I have, for sure. I think more than any of us have. Tell me if I'm wrong, but…
Yeah, I think that that's a more,
That's probably the only thing that comes to mind, as far as, like, larger spec level things.
**David Ashpole (dashpole)** 07:50 Okay.
Do you think… do you think you guys are the right owners for the, like, agent image builds?
**jea** 07:59 In terms of, like, the auto instrumentation stuff?
Yeah, like, I'm surprised that it fell to you guys, but…
**David Ashpole (dashpole)** 08:06 I guess the language sigs maybe themselves aren't as interested in doing container builds.
**jea** 08:12 Yeah, I think that that's kind of how it began, and so we need to have
a better relationship with the language people in… in regards to that. And that's sort of what, like, Nikolai's goal with it is, is to get more, alignment and, like, ownership from them, so that we don't… we're not as, like.
On the hook for things that happen, like, way downstream from them.
When it is, like, their changes, yeah.
**David Ashpole (dashpole)** 08:43 I will stay.
I will pay attention. How about that?
**jea** 08:46 Cool. I don't know, Pavel, is there anything… Pavel, Yuri, is there anything that, either of you can think of from the past year of,
things that David should be aware of?
**PL Pavol Loffay** 09:02 No, I have one ticket opened with the… on the community repo.
I'll share a link here.
It's… it was about adding, like, enabling Gemini code review.
I'm not sure if that one…
has any updates. I know that… Curiosity opened, CNCF ticket.
**David Ashpole (dashpole)** 09:30 That's probably more in the GC category.
But it's very interesting.
**jea** 09:39 And, Pavel, I just posted that on our check-in thing with, Drossi as well, so…
I didn't realize that was still open.
**yurioliveirasa** 09:49 And I can check with him, by the way.
**jea** 09:54 Message him on Slack, say, hey, Pablo, we've been waiting.
Yeah, no, that'd be good to have. I've been wanting to try that out. I also saw that, like, Graphite just released one. We tried using Dosu for, like, a minute, and I don't know if you've used that, David, but that was kind of a…
a non-starter. We did it in the Helm SIG, and it was, like…
really bad, false positive rate.
So Tyler just turned it off, because it wasn't great.
Yuri, is there anything on your list of stuff past year that you wanna…
**yurioliveirasa** 10:36 No, you're… actually, you raised a very good topic, because I remember we've been talking about, for example, the Java, and also the… the Node.js, stuff, and…
**jea** 10:48 I think it's .NET.
**yurioliveirasa** 10:50 No, the Node.js as well.
**jea** 10:51 I was in late?
**yurioliveirasa** 10:52 Yeah, as far as I remember, yeah, it was the .NET and Node.js as well.
**jea** 11:00 Oh, okay.
Well, yeah, I think… and David, if there's anything else that pops up, I'll let you know.
**yurioliveirasa** 11:12 Yeah, for sure, yeah, yeah.
**David Ashpole (dashpole)** 11:15 Cool.
**jea** 11:19 Cool. Well, moving on then,
Timo, do you want to share what you got?
**Timo Johner** 11:29 Yeah. So…
Please forgive me, because I think that has been discussed before, on the 28th of August, and it's about, basically, the idea… like, what we have, we are running OpenTelemetry mostly for logs, and we want to…
Like, we want to use it also for audit logs, and for that, we need, like…
additional access to the host PID, which is currently not possible, and I think
the last time, so on August 28th.
My colleague was here, and he discussed it, and I think the idea was to have a sidecar, injection, instead of having it directly in the operator.
The adaption of the CRD. So I'm basically picking up the issue here.
Trying to get some… get some love for the issue, because we're, like… the injection, the sidecar injection would not…
solve our issue, as far as I… Can think about it.
And I… yeah, I'm basically stuck there, because I… I'm not sure how to pick it up from here, because it would be cool to have.
**jea** 12:48 I'm chasing.
**Timo Johner** 12:48 in, but I also see that it might, like, raise, security concerns.
**jea** 12:55 Yeah, security concerns is something that might be,
concerned about… did the sidecar not work at all?
**Timo Johner** 13:05 I think it's not sol… like, maybe you can tell me what exactly would the sidecar solve there. I mean, it would gain access to, to the host PID, but then you have to…
Would the sidecut then… Like, yeah, what would it, what would it solve there, actually?
**jea** 13:25 Yeah, so what I think was proposed here, I don't know if I was at… oh, no, I was at this meeting, I might have…
dipped out before this.
**yurioliveirasa** 13:33 It goes on the 4280, right?
**Timo Johner** 13:35 Yeah, exactly.
**jea** 13:37 Yeah.
I think… What the recommendation here is, is if you were to have a pod with the correct
security and host PID settings…
Already, if you did a sidecar on it.
I think… do we copy those over?
I don't think so.
Let me, let me,
I haven't looked into this, so I'm kind of just going off what we have in the notes here.
**yurioliveirasa** 14:12 I'm not sure if it's access audit demo.
Straight cross.
**jea** 14:18 Yeah, I think my concern would be the security, like, the added, security stuff.
It's definitely my fear with it.
**Timo Johner** 14:34 Is there, like… because it's sometimes hard to, like, follow a discussion, even though it's on Zoom, and…
**jea** 14:43 Yeah.
**Timo Johner** 14:43 Does it make sense if you, like, you're…
Because, like, from the meeting notes, I tried to understand what you proposed, but I'm not sure
How to actually… how it would actually solve our problem, so it would help if you, like, under the thread, under the issue.
You can… yeah.
maybe… Outline a little bit more what you…
What'd you mean by that? If possible.
**jea** 15:14 Yeah, I… I don't have, like, a ton of free cycles currently.
**Timo Johner** 15:19 Yeah, true, yeah.
**jea** 15:22 I can look into this a little bit, today. I'm sure that there's, like, other vendors that have also run into this problem before. Like, I'm looking at one, like, from Elastic right here.
Hmm, can you…
**Timo Johner** 15:36 naked, maybe?
**jea** 15:38 Yeah, I'll put it in the, SIG notes, so it's at least… Present.
**Timo Johner** 15:46 Cool.
Because I know there's also, like, a SIC going on about audit stuff, like, audit log stuff, but I'm not sure how active they are, and didn't participate in any meetings from them so far.
**jea** 16:02 No, I haven't heard anything about that. Okay, okay.
But there, you know, there's so many SIGs, so…
**Timo Johner** 16:09 Yeah.
**jea** 16:10 Yeah, it's hard to know it all.
**Timo Johner** 16:13 Sure.
**jea** 16:15 Let me check… What the gold is here.
Yeah, like, the worry about, host PID is…
Well, I thought we embedded, like, security context. Maybe we don't, but,
Oh, no, we do.
Hold on.
And we have pod security context. Isn't this a security context field?
**yurioliveirasa** 16:48 I believe so.
**Timo Johner** 16:49 Yeah.
**jea** 16:53 One.
Give me… yeah, I'm just looking at… give me, like, 1 minute to…
Any of these things.
**yurioliveirasa** 17:16 And security context is there.
**jea** 17:27 No, it's not there, let's see…
**yurioliveirasa** 17:40 Yeah, but for, yeah, security context, but for,
For sidecars, works a little bit different, you know?
**jea** 17:51 Yeah, you might be able to use the…
So we do embed just the base security context in there, and one of the options in that is the privileged
flag, the, like, privileged Boolean, and I think that is actually what you want to be doing.
So, the description of privilege… I'll put it in here.
**Timo Johner** 18:19 Hmm.
**yurioliveirasa** 18:21 But do you run, in OpenShift or something?
**Timo Johner** 18:26 Nope. No.
**yurioliveirasa** 18:27 No? Oh, okay.
**jea** 18:34 So, I think privileged… Is… it's running it, like, the equivalent to the root on the host.
And so I think that you should have access to the host itself, because it's technically running as, like, a root user.
So you might… you should have… I think that might work. Again, I'm like…
**Timo Johner** 18:57 Yeah.
**jea** 18:57 Solely documentation here.
**Timo Johner** 18:59 Yeah, yeah, yeah.
**jea** 19:00 But… Hosted versus…
**Timo Johner** 19:15 And then basically running the collector in privilege mode.
**jea** 19:19 Yeah. Could be a deer.
**Timo Johner** 19:21 I see… We tried a bit.
I thought we tried that as well, but I can… I can see… I can'.
**jea** 19:33 Yeah, this is definitely not my…
like, kube security stuff and this type of stuff is usually… is, like, not my area of…
Expertise in here.
**Timo Johner** 19:43 Nope.
**jea** 19:44 But… I think it's worth giving… giving it a try.
Trying to find anything that, like, talks about this, but it's kind of… pretty niche.
**Timo Johner** 19:59 Unfortunately.
**jea** 19:59 remote.
**Timo Johner** 20:01 Yeah, I think that's… that was our problem as well, that it's hard to find the solution, actually.
**jea** 20:08 Yeah.
**Timo Johner** 20:12 And I, like, I totally can understand that it might be too much of a security issue, but…
Then, in the end, if we
audit logs, it makes sense to have host PID as well.
**jea** 20:23 Yeah, for sure. I think the…
like, the reason we added security context is because that, that was, like, the Kubernetes recommendation.
So that you could, like, define privileges and prevent that type of, like, escalation.
But let me check.
Lone.
**yurioliveirasa** 21:00 Yeah, I have to check, but in the security context, probably you can, set some OS capabilities,
I don't know… I remember something like that, huh.
**jea** 21:17 Yeah… And what is this on? The pod? Yeah…
**yurioliveirasa** 21:24 Yeah, yeah.
**jea** 21:29 Yeah, I mean, it's kind of.
**yurioliveirasa** 21:30 host PAT, right? Yeah.
**jea** 21:34 Yeah, I'll have to… maybe to summarize, I have to think about whether or not this is something that we want.
I would be a little bit worried about, escalation, in it.
I don't know, Pavel, you've been doing more security stuff as of late, with, like, FIPS compliance, right?
Are you aware of any of this, like, host PID stuff?
**PL Pavol Loffay** 21:58 That's not really related. Yeah, I'm not a great security expert on Kubernetes, yeah.
**jea** 22:05 Yeah, more saying in that you've been doing more security stuff than I've been doing in the past year.
**PL Pavol Loffay** 22:11 Yeah, I looked at FIPS and the network policies recently, but this is, yeah, something.
**jea** 22:16 Totally different. Yeah.
**yurioliveirasa** 22:22 Pressure is secure all the time.
**PL Pavol Loffay** 22:26 Is the question whether we should allow it by default, or have it behind the feature gate?
**Timo Johner** 22:34 Doesn't… like, no, no. That would be too simple. I actually, like, we came to basically an end where we're not sure how to solve it.
So… that's why we thought, Enhance the operator, or…
find somebody who knows more than we know. And I think the second is also very likely, so that's why I came to this group.
that somebody can solve it, or help us solve it. I don't… I don't want you to solve it, but, I don't know, point us to… to someone else.
Would help, you know.
**jea** 23:07 Yeah, I don't wanna… you know, what I want to avoid is, like, putting you through the wringer of just asking, like, a bunch of sigs and then, like, going around in circles.
**Timo Johner** 23:16 Mmm.
**jea** 23:17 David, great question for you.
there is a security SIG, right?
I don't know what their, like.
familiarity is in the Kubernetes space.
Do you think it'd be… is there, like, a cube…
SIG that we could, like, reach out to about this?
And get…
**David Ashpole (dashpole)** 23:38 Kubernetes take.
**jea** 23:40 Yeah.
**David Ashpole (dashpole)** 23:40 Kubernetes stick, or…
**jea** 23:42 Yeah, like, is there a Kubernetes SIG that is, like, Kubernetes, you know.
Pod security or something, like, something hyper-specific.
**David Ashpole (dashpole)** 23:50 I mean, there is the… Let me figure out what it's actually called.
I mean, some of this is gonna be under Signode, because Signode, like.
Has driven some of the features around, like, container privileges, especially if they require,
changes to the container runtime interface, but usually it's, like…
And then there's the security, I think it's… Is it SIG Security?
Then there's SIG Security, which has mostly been behind, like, everything to do with RBAC, and… yeah.
**Timo Johner** 24:32 Hmm.
**David Ashpole (dashpole)** 24:35 Things like that there. Let's see… Who's working on this today?
**jea** 24:47 Yeah, I'm sorry, I wish I had a better… a more immediate answer for you.
**David Ashpole (dashpole)** 24:50 I think the OTEL security SIG mostly just does audits.
**jea** 24:57 Yeah.
**David Ashpole (dashpole)** 24:57 and maybe handles escalations. I don't think they're subject matter experts in
Container privileges or anything like that?
**Timo Johner** 25:04 But then they should run into a similar problem, like, if you…
If you talk about audit, auditing and audit logs, especially, it should matter to them.
**David Ashpole (dashpole)** 25:16 More like auditing more in, like, pay a consulting firm to look at the operator.
**Timo Johner** 25:23 Alright.
**David Ashpole (dashpole)** 25:23 All the things that are wrong with it, not like…
**Timo Johner** 25:26 Okay, okay, that's another subject then, yeah, true.
Okay.
Yeah. I don't want, like, I don't want to, to, take the whole time.
**PL Pavol Loffay** 25:40 Do you have, like.
**jea** 25:41 Because you're the last on the list, so…
**Timo Johner** 25:43 Okay. Alright.
**David Ashpole (dashpole)** 25:45 Is the question what Linux capabilities are required to be able to access the host PID?
Is that essentially what we're trying to figure out?
**jea** 25:55 I think more, is it, is there a way in existing Kubernetes to allow
Getting audit logs without having the… Post fit set to true.
Because in a lot of the recommendations for… as you're linked here, it's like, a lot of the recommendations for.
**David Ashpole (dashpole)** 26:16 Kubernetes and audit logs that are written, like, on the… Control plane.
VM, right?
These aren't, like.
**jea** 26:29 Yeah, I assume that these are, like, the audit logs. Well, I think these are probably node audit logs, not just the control plane ones.
correct me if I'm wrong on that.
**Timo Johner** 26:38 Yeah, I mean, for us, it would be both, yeah.
**jea** 26:41 Yeah.
**PL Pavol Loffay** 26:44 So, setting the hospital is one solution, but we're trying to figure out if there is a way to do it without it.
**Timo Johner** 26:50 Yes.
**jea** 26:51 Yeah, or, like, if there's a way to do it with the security context or pod security context, because we already support that, and I think that that is the more recommended form for doing this stuff.
Because you can also write policy around that.
As well. I mean, not that you couldn't with HostPid, but I think that it's, like.
They're trying to stand… my understanding is that they're trying to standardize on security contexts.
**PL Pavol Loffay** 27:17 I can ask around here,
There is a team that maintains the…
block collector for OpenShift, they might know.
**jea** 27:26 That'd be great.
**Timo Johner** 27:35 Perfect. And yeah, if you… yeah.
If you have somebody just,
Drop it under the issue, that will help.
Thanks. Much appreciated.
**jea** 27:50 Yeah, no problem. Sorry we couldn't get you a more immediate answer on it.
I think that's all we have for today. Anyone else have anything to bring up for the group?
**PL Pavol Loffay** 28:16 I have one question for Timo. So do you want to use the… Oh, the receiver?
**Timo Johner** 28:24 Probably, yes.
The RD receiver…
**PL Pavol Loffay** 28:34 Or, like, what would help, maybe, if you can share… like a CR with the… collector builds.
on the issue. If you kind of want to use some custom… component that is contribute.
So if you can, like, maybe provide, like, a reproducer or something like that, that would help.
**Timo Johner** 29:01 Yep.
That's… I can do that, yeah, no problem.
**PL Pavol Loffay** 29:08 So maybe it, you know, prints the logs with the debug exporter.
**Timo Johner** 29:16 Yep. Okay.
**yurioliveirasa** 29:27 Pavel, I don't know if you saw the chat, but, Jessie just checked, and C at CFG didn't act, the ticket, okay?
I don't know if you, Dave, can help somehow.
**David Ashpole (dashpole)** 29:42 Probably not. That's more our GC.
**yurioliveirasa** 29:46 Okay.
Got it.
Okay, guys.
Do you have any questions?
Any topics? No?
**jea** 30:01 In call, good. Thank you all very much. David, congratulations on the TC.
**yurioliveirasa** 30:08 You know.
**David Ashpole (dashpole)** 30:08 Excellent.
**yurioliveirasa** 30:09 Congrats for that, yeah. See you next time.
**Timo Johner** 30:12 Thank you, bye-bye.
**PL Pavol Loffay** 30:13 Goodbye.
