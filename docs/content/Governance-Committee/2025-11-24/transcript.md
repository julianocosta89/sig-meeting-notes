SIG: GC Project Management (EU)
Date: 2025-11-24
Duration: 38 minutes
Zoom Recording URL: https://zoom.us/rec/share/oMN_Ti7Th5d2W7bv5JbvNDJqwEEK0ziK1kEGf5r9-9E4qfMuVaUZ_bCQljeXoSL2.UvrXZKBYvEJrrxzi
============================================================

## Zoom Recording Transcript

**Pablo Baeyens** 01:55 Good morning!
**Juraci Paixão Kröhling** 01:56 Hello, Pablo, how are you doing, man?
**Pablo Baeyens** 02:00 Doing fine. What about you?
**Juraci Paixão Kröhling** 02:04 Can't complain.
It's been a while since we last talked.
**Pablo Baeyens** 02:09 Yeah, yeah, I… I had… some stuff to do on Monday mornings, but, should be able to join.
control work.
Do you know if… Severin is joining?
**Juraci Paixão Kröhling** 02:30 I don't know, I think I saw him this morning elsewhere, let me see…
I don't know.
Yeah, I think we can get started.
**Pablo Baeyens** 02:54 Okay.
If you give me a minute, I can share my screen.
**Juraci Paixão Kröhling** 03:08 Okay.
**Pablo Baeyens** 03:36 Yay.
There's quite a few of them.
**Juraci Paixão Kröhling** 03:45 Whoa.
Yeah, but very granular. Those are SPAC issues, but those are SIG-specific, right? So those are…
Like, all of the Prometheus ones.
**Pablo Baeyens** 04:00 we can…
**Juraci Paixão Kröhling** 04:03 Let's see…
**Pablo Baeyens** 04:04 Hmm… Seek issue…
Do we need a triage label, or will that… oh, yeah, CD issue will be enough to remove them from there.
**Juraci Paixão Kröhling** 04:21 Cool.
**Pablo Baeyens** 04:22 Okay, so… Now, if we refresh…
Okay, well… Okay, no worries.
**Juraci Paixão Kröhling** 04:36 Cool.
**Pablo Baeyens** 04:38 Right, so let's start with… Jeez…
Okay, why is this…
I think we can.
Probably closes, like… the idea…
**Juraci Paixão Kröhling** 05:21 Focus.
Yeah, I, can I look at the latest? I think that…
Yeah, can you scroll down a little bit? Let me see what it says there? Oh, two weeks ago, okay. Yeah, I think we can close it, yep.
**Pablo Baeyens** 05:58 It's a very old one.
Which… The only update is… is…
**Juraci Paixão Kröhling** 06:33 This is also…
**Pablo Baeyens** 06:36 pretty old, I need…
any update, any real update recently. Like, the update here is that it was removed from the…
CENCOM project. So…
**Juraci Paixão Kröhling** 06:47 I think it needs to be retriaged, yeah.
We want to feed back, yeah. Yeah.
Yeah.
**Pablo Baeyens** 06:58 Okay.
Oh… Okay, this one is also old.
**Juraci Paixão Kröhling** 07:06 This might be…
So this is OpenP, right? This is related to Open. Yeah, sounds like SIG issue.
Mmm…
Kind of. I mean, it does affect the individual SDKs, like, every single SDK would have to implement that.
**Pablo Baeyens** 07:31 Sure, you can make the same argument about the Prometheus ones, right? Right, well, that's true.
Export here.
I would say SIG issue is the right.
**Juraci Paixão Kröhling** 07:40 Yep.
**Pablo Baeyens** 07:41 Please.
**Juraci Paixão Kröhling** 07:42 Yep.
**Pablo Baeyens** 07:44 Yay.
Great.
So…
How's this?
**Juraci Paixão Kröhling** 08:27 I don't.
Yeah.
I don't know what this is about.
New attribute value types.
limits.
**Pablo Baeyens** 08:37 I think the value types are the complex types, the ones that we announce on the blog post.
So… Things like nested mobs.
**Juraci Paixão Kröhling** 08:47 I see, okay. And the issue is… yeah, okay. And the issue is about adding support to the… to the individual SDKs, or what is that?
Go prototype.
**Pablo Baeyens** 09:01 Yeah, like, making it stable is the… the issue is making it stable.
So… I am assuming the part of the spec that handles this is not…
**Juraci Paixão Kröhling** 09:14 statement yet. Okay, so this… so there's no triaging necessary then, because it is already a change that was approved?
**Pablo Baeyens** 09:25 Right, so…
**Juraci Paixão Kröhling** 09:26 It's only tracking…
**Pablo Baeyens** 09:30 accepted… ready with sponsor, I guess?
**Juraci Paixão Kröhling** 09:35 Yeah.
Yeah.
**Pablo Baeyens** 09:40 Okay.
Okay, is there anything about, like… Orr.
administrative issues or something?
**Juraci Paixão Kröhling** 09:58 Infra. I think there is something like INFRA?
**Pablo Baeyens** 10:02 I'm not on the community URIFO, so it's not here.
**Juraci Paixão Kröhling** 10:05 Oh.
**Pablo Baeyens** 10:07 Yeah.
**Juraci Paixão Kröhling** 10:07 Yeah.
Which is no spec, so this is definitely not spank, but I…
**Pablo Baeyens** 10:17 I think we can accept this, like, it seems… reasonable enough to me.
It's deprecated, we use C-Spell elsewhere.
It's already… there's prior history on other repos, so I would… Except, dude.
**Juraci Paixão Kröhling** 10:39 Ready.
**Pablo Baeyens** 10:42 Stop.
Missing… State events to drive alerted.
You know.
I'm just going to print this part on.
I…
**Juraci Paixão Kröhling** 11:36 I don't think it's in scope for the project, but .
**Pablo Baeyens** 11:41 Like, if anything, it would be in scope for, like, Some sort of semantic conventions.
**Juraci Paixão Kröhling** 11:45 Yeah.
But I… Yeah.
That's true. It is… It does mention a new feud at their log record level.
So that's not an attribute. Or, or… oh!
It is, so, would enable the log record of UID SIM code to be deprecated, just like… okay, yeah.
**Severin Neumann** 12:13 Hey, sorry for being late.
**Juraci Paixão Kröhling** 12:15 No, that's fine.
I don't know. I… my initial feeling is, let's just say no to this one. We have so many other things in mind.
But, but I guess it belongs to the C inbox.
**Pablo Baeyens** 12:36 I wouldn't even put it on TC inbox, like, if…
If we don't want to reject it, I would put it on, like, community feedback, like, wait it to see if anybody else is…
**Juraci Paixão Kröhling** 12:48 Yeah.
**Pablo Baeyens** 12:49 on, I mean.
I think it's not a priority right now, but I, like, I think it doesn't hurt to have it open.
**Juraci Paixão Kröhling** 12:59 That's true.
**Pablo Baeyens** 12:59 But actively working on it.
**Juraci Paixão Kröhling** 13:02 Yes, that's true.
Yeah.
**Pablo Baeyens** 13:06 Or, community feedback.
**Severin Neumann** 13:35 I remembered that one.
But… Also remember, like, that It was mentioned a few times in some conf conversations, but…
**Pablo Baeyens** 13:48 This was opened last week, so.
**Severin Neumann** 13:50 No, no, no, but the whole discussion around types, on… spends.
It came up a few times before as well.
I think that's also what he's referring to, that Josh…
Raised it at a few occasions.
But yeah, I think it's another one that's just, like.
Needs a little bit more community feedback.
So yeah, I think that's how I would triage it for now.
**Pablo Baeyens** 14:28 Okay, yeah, I mean… It hasn't been outright rejected by others.
**Severin Neumann** 14:32 Yeah, exactly. No, no, and seeing that, like, a few people interacted with it, I think it's not like…
horrible, so to speak, so yeah, no, I think we can keep it away.
Introduce lock time fill.
Isn't that a duplicate of the other one that we just looked at 2 minutes ago?
**Pablo Baeyens** 14:53 This is spun type.
**Severin Neumann** 14:54 No, no, no, the other one, like…
**Pablo Baeyens** 14:57 Oh, the… Dude.
**Juraci Paixão Kröhling** 15:00 SimConf, yeah.
**Severin Neumann** 15:01 It had, like, a lock type as well, right? It had, like, no, event kind.
**Pablo Baeyens** 15:07 Right.
**Severin Neumann** 15:08 Alternatively, we call it type.
**Pablo Baeyens** 15:30 I think we should wait until…
There's a reply to this question.
**Severin Neumann** 15:39 That comes…
**Pablo Baeyens** 15:42 Don't know if there is a way to represent that.
**Juraci Paixão Kröhling** 15:49 that we are waging? Needs info? No.
Deciding needs info.
**Pablo Baeyens** 16:07 The siding needs info, I don't think it's… oh, yeah, okay, yeah, so… That's it.
Sorry, I wasn't seeing that.
This is the one we got ready.
**Severin Neumann** 16:36 Why would… Okay…
**Pablo Baeyens** 16:47 Yay.
So, I think… My understanding of this is that the protocol supports
colon, or, like, anything UTF8, but when you… Create, instrument, It has some extra validation.
It does not allow,
Colons. So it's… it's an issue about that, about discussing…
I think this is reasonably Prometheus.
allows it.
Huh.
I would put… community feedback.
**Severin Neumann** 17:38 Can we probably, like, put it in the Prometheus working group?
I mean…
**Pablo Baeyens** 17:44 But it's not Prometheus. We can ping the Prometheus working group, but I don't think it's a SIG issue from the Prometheus working group.
**Severin Neumann** 17:50 Yeah, okay, it's a more generic issue to say, like, hey, in general, why are we not allowing those? Is there a wrong reason for that? And if not, then just let's…
Let's stop doing that, so yeah.
**Pablo Baeyens** 18:05 Okay, so… No.
I mean, this group is not really…
The best we have, I guess.
So… Community Feedback… on… This is the last one.
I… Would be tempted to reject this.
**Severin Neumann** 19:53 It's a little bit hard to read because of how he did his, comments.
**Pablo Baeyens** 20:01 I mean, too.
The first part is this.
**Severin Neumann** 20:11 And he has an issue with the local, right?
**Pablo Baeyens** 20:15 Yes.
Yeah, with this local.
**Severin Neumann** 20:34 And what's the problem with that? I'm not exactly sure if I understand it.
when I read, that gives me the impression that it's intentional, given
remote external servers, however, when I read…
I'm not sure if I understand that.
**Pablo Baeyens** 21:01 Yeah, and I'm rereading it, I'm not sure I understand it either.
We can ask for…
an example… Oof.
**Severin Neumann** 21:20 What's that spend resign?
**Pablo Baeyens** 21:41 An example of the situation that.
**Severin Neumann** 21:42 Okay, I… okay, it means in the sense of, like, a producer could…
So, so clients, client server always means, like.
There is something going over the network to make it very simple.
But producer diverting as it is also means, like, hey, I schedule something, but it stays within the same process, right?
I think that's…
**Pablo Baeyens** 22:12 Right, so, like,
the local here is inconsistent with the within an application here, or confusing with that? Is that bad?
**Severin Neumann** 22:21 Yeah, I think that the big question is, like, imagine you have, like, a scheduling system.
Like, like a cron job, or whatever, or, like, a local video… Encoding or whatever.
And a producer dispatches that, not, like, on a separate service.
But on a separate thread, for example,
then this would be local, right? And then the question is, like, is this a producer span or an internal span?
But the question is, like, do those…
types always have to… S-band kinds always have to be… entirely non-overlapping, like…
Or to make it short from a triage perspective, I think it's a valid question.
**Juraci Paixão Kröhling** 23:26 Yeah, I guess there might be an ambiguity there on local remote as well. Yeah, I think the only thing I would do…
**Severin Neumann** 23:32 for him is, like, I will reformat that issue, because, like, it's really hard to read.
and just do that with, like.
**Pablo Baeyens** 23:41 Oh, if you're gonna do it, I'll let you.
I think, like, just a quote block here.
**Severin Neumann** 23:47 Yeah, exactly, that's what I'm… what I'm just doing, just adding that to…
And maybe write a comment and say, like, hey, don't use code blocks for… .
**Juraci Paixão Kröhling** 24:02 quotes.
**Pablo Baeyens** 24:02 Looks for quotes.
**Juraci Paixão Kröhling** 24:04 I think… but I think I, I, I understand the… the… the confusion there.
And one example that is very common in Go is… you… People use, like, worker queues.
I mean, even Java, like, so, in Threadpool, or worker queues in general, like, work groups.
They send it to a queue somewhere, and that's picked up by a worker. And is that, like, internal, or is it produced certain consumer?
I would argue it's producer-consumer.
Even though it is local.
Alright, so I guess this is… and it… what it means is, the internal…
Defoe would be, like, the internal spend kind.
would not…
Perhaps we need a better wording there, or perhaps we need more examples on what is a producer, what is a consumer, and what is internal.
**Pablo Baeyens** 25:08 Yep, yeah, okay, I think I… I think I understood it now.
I'm not sure what to put for it.
triogen?
**Juraci Paixão Kröhling** 25:21 I think it is…
I mean, I guess if we are all in agreement.
if it is clear to us, if it is, like, obvious to us what it is, so what is a producer and consumer for that kind of situation, then I think it's only a matter of changing the website to clarify those cases. But if we think that there's any contention there.
then we should definitely have a discussion at the… like, the TC would have to clarify that.
**Pablo Baeyens** 25:55 I… so I don't think any of us…
Correct me if I'm wrong, but any of us, like, wrote this or participated in the discussion that led to writing this, so maybe it's good if we have somebody that
Mike.
wrote this.
Take a look.
**Juraci Paixão Kröhling** 26:12 Yep.
**Pablo Baeyens** 26:13 Or, yeah, like, more… perspectives in general, because, yeah, like…
**Juraci Paixão Kröhling** 26:18 fuel it.
So, sorry, go ahead.
Yeah, I was gonna say that this feels somewhat trivial to me,
I would perhaps open the GitHub issue, like, against the OpenTrumpet.io, like, changing the documentation, and they're asking the GC to review, like, is this really…
**Pablo Baeyens** 26:41 This text is on this repository, on the spec repository.
**Juraci Paixão Kröhling** 26:46 Oh, is it? Okay. Oh, yeah, that's true. Yeah, yeah, yeah, yeah.
Right, so, yeah,
Yeah, then I would open a PR against this repository.
**Pablo Baeyens** 27:01 So, is it…
**Juraci Paixão Kröhling** 27:01 ask ATC to review it. Because I think it is… I think it is to review, I think it is non-contentious.
**Pablo Baeyens** 27:09 So then, I'm gonna put Breddy.
**Juraci Paixão Kröhling** 27:12 Yeah, I think so.
And then perhaps leave a comment down there that, you know, we… the three of us, we believe that,
Producer-consumer can indeed be used in local.
Processes on a producer-consumer pattern, like leopard use, and
A clarification might be necessary to this bank.
Just on that specific part.
But there's no contention about that.
**Pablo Baeyens** 27:54 Does this sound reasonable as a summary of what you said, or do you want…
**Juraci Paixão Kröhling** 27:59 Yeah, I think I would just add that there is a consensus among the three of us that producer-consumer is possible in internal
On… on… within a single process, such as in… In worker queues.
Worker cube patterns.
**Pablo Baeyens** 28:32 Still like that?
**Juraci Paixão Kröhling** 28:32 Exactly. Yep, exactly.
**Pablo Baeyens** 28:37 Right.
I think that's all of it.
Let me… oh.
Me opened it.
Filter… Yep.
See?
I don't know if we want to look at the… Community… Repo…
Actually… Guess I'll use the time to ask you about…
Should I go ahead and do this? Do we want to…
wait, it seemed pretty clear last week that there was consensus on the GC, and I haven't heard any…
Opposition from the community.
**Severin Neumann** 29:29 No, I think… I think we agreed just to do that. I think the only thing we need to do is that someone
puts it in, right? So, the one thing is the GitHub announcement, and I think the other one is the…
Canceling of all the meetings.
**Pablo Baeyens** 29:47 Okay, I don't have permissions for the announcement. I don't know if that can be scheduled.
**Severin Neumann** 29:53 Let me check. I have never done one before, but I can…
**Pablo Baeyens** 29:58 Yeah, you should have permissions, yeah.
Announcements, moderation…
**Severin Neumann** 30:12 I have no idea where you do this.
Settings, announcements, okay, I don't know, maybe it's just blind.
Not seeing… oh, yeah, I have it. Okay, cool.
I can set an expir… ex…
Puration date, but not schedule it.
**Pablo Baeyens** 30:53 Okay.
I could schedule a reminder on Slack, for people to do it, I…
Guess somebody will be around?
**Severin Neumann** 31:07 No, I think we should do it a week before, something like that, or maybe even two weeks before, to say, like, hey…
I think just putting it out on December 22nd is a little bit…
**Pablo Baeyens** 31:19 Okay, yeah, sure.
**Severin Neumann** 31:20 Oh, no.
**Pablo Baeyens** 31:21 something like… December 8th, or December 15th?
**Severin Neumann** 31:27 Maybe 15th, maybe a week is enough. I think 2 is too much, right? Then people get confused, and they're like, oh, they're on a… like, like, people don't read it, and then suspect, like, we're on a break already, or something like that, so… I think a week before is fine.
**Pablo Baeyens** 31:42 Okay, so I'm going to just schedule a message on the…
I guess GCTC tunnels, since the admins are from both.
**Severin Neumann** 31:51 Yeah.
**Pablo Baeyens** 31:52 2… to schedule the reminder. And I can do the… the cancelling of the meetings now.
Cool.
I don't know if we… like…
Label areas.
This is… area… For your infra…
I'll spend some time on the… improving the area labels, because, like, I don't know, the feedback ones, for example, I don't…
Know that we have a good label?
On things like biz, or…
Dez, or… even mine.
I also don't know what area I would put them as.
Does that sound reasonable?
**Severin Neumann** 33:35 Yep.
**Juraci Paixão Kröhling** 33:37 Yep.
**Pablo Baeyens** 33:43 Okay.
then I think we're done.
**Severin Neumann** 33:45 Awesome, thank you very much.
**Pablo Baeyens** 33:49 Yep.
**Juraci Paixão Kröhling** 33:49 Nice.
**Severin Neumann** 33:50 Talk to you latest on Wednesday.
See you in one seat. Yep.
**Juraci Paixão Kröhling** 33:54 Like…
