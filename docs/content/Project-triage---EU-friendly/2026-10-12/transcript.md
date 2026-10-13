SIG: Project triage - EU-friendly
Date: 2026-10-12
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Severin Neumann (Bronto) 00:01:48 Hey, Robert, good morning.
Robert Pająk (Splunk Inc.) 00:01:55 Good morning, how are you?
Severin Neumann (Bronto) 00:01:56 I'm fine, how are you today?
Robert Pająk (Splunk Inc.) 00:01:59 Good as well.
Severin Neumann (Bronto) 00:02:02 So, let's see, I don't know if anybody else joins, but, I mean, we can just… do a little bit of triage, right? And then…
Robert Pająk (Splunk Inc.) 00:02:09 Sure, let's go for it.
Severin Neumann (Bronto) 00:02:11 See how it goes. There's not a lot, I guess. Let's see, I can share my screen with you… saying to find the right window. Can you see that?
Robert Pająk (Splunk Inc.) 00:02:23 Yes.
Severin Neumann (Bronto) 00:02:27 Okay.
Excuse me a second.
Okay… Cool. Let's go… top to bottom, but I don't think it really matters.
Let's just open all of them real quick.
Nice.
Okay, clarify what to do with not a number, inf plus, inf minus for explicit histograms.
Robert Pająk (Splunk Inc.) 00:03:07 You can accept it.
Severin Neumann (Bronto) 00:03:08 Yeah.
Robert Pająk (Splunk Inc.) 00:03:09 Yep.
Severin Neumann (Bronto) 00:03:10 Does it need a sponsor, and are you the sponsor, or is it…
Robert Pająk (Splunk Inc.) 00:03:15 It doesn't need a sponsor, it's like clarification or, you know, I don't remember what was the process.
It's a bug in the spec, I will say.
Severin Neumann (Bronto) 00:03:26 Okay.
And should I write a comment on that or just like, yeah, this makes sense.
Robert Pająk (Splunk Inc.) 00:03:32 I don't think it's needed.
Severin Neumann (Bronto) 00:03:34 Yeah, okay.
Robert Pająk (Splunk Inc.) 00:03:35 You can ask… The only… I'm… The only thing that which maybe we can do is to ask, Tyler, so Mr. Alias, if he wants to own it.
Severin Neumann (Bronto) 00:03:50 Yeah.
Let me reconquest your handle.
Robert, what was your handle?
Robert Pająk (Splunk Inc.) 00:04:05 All right, P-A-P-E.
EE, not AE.
Oh, wow.
Severin Neumann (Bronto) 00:04:12 Yeah.
Robert Pająk (Splunk Inc.) 00:04:24 Or, wait, jack was also writing some here.
But I think it was Tyler who was prop… yeah.
I think Tyler was the main, the main proposal.
Are you here or have I lost you?
Severin Neumann (Bronto) 00:04:47 No, no, I'm just…
Robert Pająk (Splunk Inc.) 00:04:49 Your eyeballs are moving.
Severin Neumann (Bronto) 00:04:51 Yeah, what are we writing down? Like, what's our comment below it?
Robert Pająk (Splunk Inc.) 00:04:59 Yeah, I think it's accepted. The question is that, do we want to ask, you know, someone who assigned himself to work on it, so it doesn't get stale, and, you know, because I think there's already, you know.
If you want, I can write it and I can ask Tyler if he wants to own it.
Severin Neumann (Bronto) 00:05:23 Okay.
Robert Pająk (Splunk Inc.) 00:05:25 common.
Severin Neumann (Bronto) 00:05:25 on it.
Robert Pająk (Splunk Inc.) 00:05:26 Yeah, I just need to find you. Can you write me on Slack?
Severin Neumann (Bronto) 00:05:30 5, 3, 4, 6. Let me.
Robert Pająk (Splunk Inc.) 00:05:33 is.
Severin Neumann (Bronto) 00:05:34 Profit to you… Just give me a sec.
Robert Pająk (Splunk Inc.) 00:06:09 Okay, I'm writing.
Severin Neumann (Bronto) 00:06:10 Okay.
Are you done?
Robert Pająk (Splunk Inc.) 00:07:15 Okay, yes, you can double check.
Severin Neumann (Bronto) 00:07:18 Oh, yeah.
Okay, perfect.
And we can go on to the next one.
Support generic default off event opt in via logger enabled and logger config. Commented on that already.
Is this still an ongoing discussion, or…
Robert Pająk (Splunk Inc.) 00:07:43 Yeah.
Severin Neumann (Bronto) 00:07:45 So I call it community feedback.
Robert Pająk (Splunk Inc.) 00:07:48 And so far, I'm against his proposal.
Severin Neumann (Bronto) 00:07:51 Yeah, but it looks like…
Robert Pająk (Splunk Inc.) 00:07:53 Yeah.
Severin Neumann (Bronto) 00:07:55 Submitting it is still… Oh, damn it.
Define behavior. Okay, that's yours.
Robert Pająk (Splunk Inc.) 00:08:12 It can be community feedback.
Severin Neumann (Bronto) 00:08:13 Yeah. Same.
Okay, define idle behavior. Also yours. Nobody so far has really commented on it.
Robert Pająk (Splunk Inc.) 00:08:25 Is it not the same?
I'm right now puzzled.
Severin Neumann (Bronto) 00:08:30 Define behavior for serial.
Robert Pająk (Splunk Inc.) 00:08:31 Oh…
Severin Neumann (Bronto) 00:08:33 My idle behavior.
Robert Pająk (Splunk Inc.) 00:08:36 What was the… was there any response here?
Nope. I think he's… I think you think the same.
I can always work on my own, at least it won't be, you know.
Try Azure back and forth.
Severin Neumann (Bronto) 00:08:58 Yeah.
Robert Pająk (Splunk Inc.) 00:08:58 These are edge cases.
The thing is that because of these edge cases, the… Most of the SDKs have very strange logic.
Severin Neumann (Bronto) 00:09:09 Rick's just give me a sec.
Okay. Span attributes have no duration time. Can't compare Tmax.
Always.
Robert Pająk (Splunk Inc.) 00:09:20 Yeah, they don't.
Severin Neumann (Bronto) 00:09:48 Didn't we have an issue for that in the past? I'm just…
Robert Pająk (Splunk Inc.) 00:09:52 You mean that they have… it's very probable that it was something like that in the past. Like, usually, if I remember correctly, we just… Use nanoseconds as a unit.
Like, you know, the Unix timestamp usually is nanoseconds.
Severin Neumann (Bronto) 00:10:10 Yeah, yeah, exactly. I think we standardized that at some point. I think there was something around it. I remember it has been a few years ago.
Where, like, different attributes said, like, oh, this is given, and this and that.
in dissident, whatever, in somewhere milliseconds and nanoseconds and whatever.
camera.
Robert Pająk (Splunk Inc.) 00:10:47 That's… It's like… I'm not sure should not be moving semantic conventions. I don't know if there are any, if there is any semantic conventions for OpenRTB.
It's just, you know… It depends on their semantic conventions, what they… what the units should be. Like, the semantic conventions, if I remember correctly, define the units, right?
Severin Neumann (Bronto) 00:11:09 So I should move it to Semconf?
Robert Pająk (Splunk Inc.) 00:11:14 Not sure at this point of time. Open arts kind of.
Severin Neumann (Bronto) 00:11:18 Or what I very often do is that I do something like I add it as community feedback.
And then I sound like.
Hey, can you… And one of the basic things.
Robert Pająk (Splunk Inc.) 00:11:32 I think I can also, when it was two weeks ago.
I could also respond here that, you know, this schema, the semantic conversion schema, also you can define units there, if I remember correctly.
And… Yeah, I can. I can. I can. I can try responding here.
Severin Neumann (Bronto) 00:11:51 Okay.
Robert Pająk (Splunk Inc.) 00:11:52 Yeah.
Severin Neumann (Bronto) 00:11:53 But I keep it as community feedback and I just draw.
Robert Pająk (Splunk Inc.) 00:11:57 Yep.
Severin Neumann (Bronto) 00:11:57 The link in the channel, so you can…
Robert Pająk (Splunk Inc.) 00:12:00 Thanks.
Severin Neumann (Bronto) 00:12:00 You can take a look.
Robert Pająk (Splunk Inc.) 00:12:02 Yeah, I think you… give me a few minutes, just… Obviously, question, is there or could be there a mark and attribute as a duration?
So the so it's about just answering the question.
Okay, I will, I will…
Severin Neumann (Bronto) 00:12:19 Okay, thank you.
Okay, I think… did all of those, and then we need label triage follow-up. There could be a bunch of them, yeah, because we failed to follow up with them for a while.
So there's…
Robert Pająk (Splunk Inc.) 00:12:38 It's in your other screen, right?
Severin Neumann (Bronto) 00:12:40 Sorry?
Robert Pająk (Splunk Inc.) 00:12:41 It's on your other screen.
Severin Neumann (Bronto) 00:12:43 What am I sharing?
Robert Pająk (Splunk Inc.) 00:12:45 You're still showing Opera RTB, maybe you click the pause.
Severin Neumann (Bronto) 00:12:49 I clicked the pause, yeah.
Robert Pająk (Splunk Inc.) 00:12:51 Yeah, custom as well.
Severin Neumann (Bronto) 00:12:53 Okay, there's, like, now… 80…
Robert Pająk (Splunk Inc.) 00:12:55 you.
Severin Neumann (Bronto) 00:12:56 Almost 80 of those, so we can see that we can get through a few of them.
Open to my GitHub refined.
Okay, Iris.
Let me just open at first.
5… Clarify exemplar sampling for cardinality measurements.
Good question.
So, so, so what's, what's our… triage on that? Should we just keep it as community feedback, or…
Robert Pająk (Splunk Inc.) 00:13:30 Yep.
Severin Neumann (Bronto) 00:13:31 Any, any, anything to bump it up?
I mean, I kind of asked CJ if he had a chance to circulate that with the… The larger team.
Robert Pająk (Splunk Inc.) 00:13:47 I don't think he'll have time right now, given his training, his job.
Severin Neumann (Bronto) 00:13:50 Yeah, yeah, I know.
I mean, I can also just leave it like that, and it will come back in two weeks from now, so… Yeah, okay.
Robert Pająk (Splunk Inc.) 00:14:00 We can, I know what we can do. Could you bring it back?
Severin Neumann (Bronto) 00:14:04 Yeah.
Robert Pająk (Splunk Inc.) 00:14:04 We could, we could ping the metrics maintainers or something like that. I think there's a.
Spec metrics approvers, yeah.
Severin Neumann (Bronto) 00:14:15 Magda?
Robert Pająk (Splunk Inc.) 00:14:16 Yep.
Severin Neumann (Bronto) 00:14:21 Consider classifying context scope attributes so providers can filter them.
Yeah, I asked them a bunch of questions, and they never came back.
So maybe I just close it and said, like, hey, stalled.
Robert Pająk (Splunk Inc.) 00:14:47 Yep.
Works for me.
Severin Neumann (Bronto) 00:15:02 We have a stale.
Robert Pająk (Splunk Inc.) 00:15:03 Yes.
Severin Neumann (Bronto) 00:15:38 Yeah, the skill. Yeah, that's yours.
Robert Pająk (Splunk Inc.) 00:15:41 Mine? Give me a sec.
Severin Neumann (Bronto) 00:15:43 Yeah, that's the skill for reviewing spec compliance.
Robert Pająk (Splunk Inc.) 00:15:47 Let's close it. I don't think… I don't think it's worth working on it.
Severin Neumann (Bronto) 00:15:53 I.
Robert Pająk (Splunk Inc.) 00:15:53 Started doing like, yeah.
If you want, I can, I can close myself.
Severin Neumann (Bronto) 00:15:59 Okay, yeah. Should I send you the link again, or…
Robert Pająk (Splunk Inc.) 00:16:03 5226… 5… 2, 2, 6… I have problems with my English. There are many factors that Okay, close.
Severin Neumann (Bronto) 00:17:19 Past?
Cool.
Bats, band processor, benchmark processor, add or opt-in blocking mode when queue is full.
That has a long, long, long, long, long discussion.
Just remove the label.
Robert Pająk (Splunk Inc.) 00:17:42 Yes.
Alexa?
Severin Neumann (Bronto) 00:17:49 API, okay, this is closed, this is really good.
I think we should just remove the triage labels then.
Oh, this is actually something we should do.
Robert Pająk (Splunk Inc.) 00:18:02 That's it.
It was closed. Can you bring it back? I think there was a comment after it was closed.
Severin Neumann (Bronto) 00:18:09 I closed it out.
Right.
Robert Pająk (Splunk Inc.) 00:18:16 I, I…
Severin Neumann (Bronto) 00:18:17 So should we reopen it?
Robert Pająk (Splunk Inc.) 00:18:20 Yes.
Severin Neumann (Bronto) 00:18:21 So he said, like, I have no issue with not documenting it as an API, but Then I reopen it.
Robert Pająk (Splunk Inc.) 00:18:28 Yep.
Severin Neumann (Bronto) 00:18:29 Okay.
Robert Pająk (Splunk Inc.) 00:18:33 Okay.
Severin Neumann (Bronto) 00:18:34 Then we need to relabel it.
Robert Pająk (Splunk Inc.) 00:18:37 Unacceptable.
Can you fix that one?
Okay.
Severin Neumann (Bronto) 00:19:09 Bunch of those that are closed, technically.
Maybe we just need to remove the label.
Yeah, we need to remove the label, otherwise, Dave, because I did not…
Robert Pająk (Splunk Inc.) 00:19:21 I know.
Severin Neumann (Bronto) 00:19:22 specify that I… Okay, okay, that's something we should be doing.
Otherwise, stay… I'll put Dan… I'm just checking if anybody answered after my… Thing.
So…
Robert Pająk (Splunk Inc.) 00:19:56 What was the response on the unit, et cetera? Maybe we can refer to.
Severin Neumann (Bronto) 00:20:00 Sorry?
Robert Pająk (Splunk Inc.) 00:20:01 Could you re- reopen the closed tabs? I think one may help me regarding this, timestamps. No, no, no, this one, previous one.
Yeah, this one may help me. Can you send it to me?
Severin Neumann (Bronto) 00:20:14 Oh, it's very similar to the other one, right?
Robert Pająk (Splunk Inc.) 00:20:16 Yeah, exactly.
Maybe I could refer to this one. Oh, okay. Later. Maybe I'll check later.
Severin Neumann (Bronto) 00:20:22 Okay, yeah, they're linked already. : I think they mentioned.
Robert Pająk (Splunk Inc.) 00:20:27 Okay. Okay, so dimensions then doesn't matter.
Severin Neumann (Bronto) 00:20:30 Yeah.
Robert Pająk (Splunk Inc.) 00:20:40 Okay.
Severin Neumann (Bronto) 00:20:53 Okay, you know what I just do for now is open.
Which is still…
Robert Pająk (Splunk Inc.) 00:20:59 I thought you want to first see the clothes.
Severin Neumann (Bronto) 00:21:03 I can also… Look at the closed ones.
Robert Pająk (Splunk Inc.) 00:21:09 And we can just quickly double check them.
It's a group, it's a group.
Severin Neumann (Bronto) 00:21:18 Yeah, nothing happened, so I can… to triage Nothing happened. Okay, I would say that's probably… to be expected… Just.
Robert Pająk (Splunk Inc.) 00:21:35 Bye.
Severin Neumann (Bronto) 00:22:25 Just remove them.
Strange.
There we go.
But there's another… 50 something.
Let's see, let's just do 1, 2, 3, a few of them.
Spam flag.
to indicate metric exemplar reference.
Thoughts on that one?
Just dropping the follow-up, or…
Robert Pająk (Splunk Inc.) 00:23:29 I'm not sure how to handle things nicely. I will just personally write to Josh.
Oh.
Severin Neumann (Bronto) 00:23:35 Okay.
So I just drop the label.
Robert Pająk (Splunk Inc.) 00:23:40 Like, 3 weeks, You know, there are three weeks, and I think that Josh could just look at it.
Severin Neumann (Bronto) 00:23:50 I can also tag him again and say, like.
Robert Pająk (Splunk Inc.) 00:23:52 Yep.
It's sweet.
Okay, let's go further.
Severin Neumann (Bronto) 00:24:13 Find resource detector API.
internet… Same thing here, right? I mean, it's just…
Robert Pająk (Splunk Inc.) 00:24:22 Could you go to the first one? I need you.
I'm not sure if we even need an Api for this one.
This has come over.
I think the TC should decide if it's even needed.
It's like, you know, do we need a new API or… All things like that.
Give it to this inbox.
Maybe we should just close this one.
Hello.
Severin Neumann (Bronto) 00:25:05 Yeah, done.
Next one.
Robert Pająk (Splunk Inc.) 00:25:10 Yep.
Severin Neumann (Bronto) 00:25:15 It's yours again.
Robert Pająk (Splunk Inc.) 00:25:16 So.
Severin Neumann (Bronto) 00:25:17 cell block?
Robert Pająk (Splunk Inc.) 00:25:18 Yeah, it is, indeed.
Severin Neumann (Bronto) 00:25:24 Stabilize scope configuration.
Robert Pająk (Splunk Inc.) 00:25:28 Yeah, it's still ongoing.
Severin Neumann (Bronto) 00:25:31 Ongoing, okay.
Robert Pająk (Splunk Inc.) 00:25:32 Like, it doesn't need this one. I'm not sure if we need… This one could be accepted, because, you know, these are just parts of the spec that we want to stabilize. It's just, it's blocked before, you know, we have all of the things, all the languages following this. I'm not sure we need deciding community feedback and, you know, discuss it during triage. It's just, you know…
Severin Neumann (Bronto) 00:25:56 I can accept it.
Robert Pająk (Splunk Inc.) 00:25:58 Yep, just accept it.
And when the time comes, you know.
Severin Neumann (Bronto) 00:26:04 just.
Robert Pająk (Splunk Inc.) 00:26:05 Yeah.
Severin Neumann (Bronto) 00:26:05 Ready? Okay. Yeah.
Cool.
Add span context assembled to SPAC.
Yeah, I think it's stalled out. No.
I still like to keep this open. The inconsistency of my Yeah, let's… let's give them some more time. I mean, it's… Just, like… Let me… Just remove the follow-up.
Robert Pająk (Splunk Inc.) 00:27:04 We don't…
Severin Neumann (Bronto) 00:27:06 end.
Robert Pająk (Splunk Inc.) 00:27:08 The easiest way, if these people worry, you know, care, they probably should join the SPEC meeting. Otherwise, nothing will happen.
Severin Neumann (Bronto) 00:27:17 Yeah, I mean, at the end, what they also could do is, like, go to the specific languages and say, like, hey, those languages have it already.
Yes. Would you mind adding it as well, right? I mean, it's like, enforcing it via the spec feels a little bit…
Robert Pająk (Splunk Inc.) 00:27:37 Do you want to write it down?
Severin Neumann (Bronto) 00:27:39 That's also something, as… An additional feedback.
Please consider to into language, safe meetings, and suggest That.
Convenience, or this?
Yeah. This functionality has… It's been available.
Something like that. And then in two weeks from now, whatever, we can still close it.
Robert Pająk (Splunk Inc.) 00:28:16 Yes, makes sense. Thanks.
Severin Neumann (Bronto) 00:28:20 Metric aggregation and variables are only for OTLP exporter.
Oh, boom.
Nothing happening on that for, like, a really long time.
Robert Pająk (Splunk Inc.) 00:28:33 What's, what's the issue about, like, is it in some bug?
Try to ignore the temporary question.
Since you will be the one who will know how to handle it.
Severin Neumann (Bronto) 00:28:56 What? Huh?
Robert Pająk (Splunk Inc.) 00:28:58 I mean, this is… I think… I think the design of the metrics configuration is bad. I think it should be on, not on the exporter level, but as suggested.
Yeah, non-OTOP exporting, exactly.
Could you scroll down?
Severin Neumann (Bronto) 00:29:26 Sorry?
Robert Pająk (Splunk Inc.) 00:29:27 Could you scroll down? I just want to…
Severin Neumann (Bronto) 00:29:28 Yeah, just give me a second. I'm saying, ring my bell.
Understand.
Just give me a second.
Robert Pająk (Splunk Inc.) 00:29:44 Sure.
Severin Neumann (Bronto) 00:29:58 Okay, I'll go.
Where was I? Okay, you said scroll down.
Robert Pająk (Splunk Inc.) 00:30:05 Yeah, you can scroll further.
Severin Neumann (Bronto) 00:30:07 Yeah.
Robert Pająk (Splunk Inc.) 00:30:08 I think it got stale, yeah.
for me to use. Okay, CJ mentioned it even. He created some new issue.
Yeah, we can just remove the follow-up and see how it goes.
Severin Neumann (Bronto) 00:30:24 Yeah, it will, it will show up every, every two weeks now.
And the problem is, I think our our stale and our follow-up process.
Robert Pająk (Splunk Inc.) 00:30:38 We'll sleep with each other.
Severin Neumann (Bronto) 00:30:40 Yeah, yeah, yeah, yeah.
But because GitHub action or like the stale bot says like, oh, someone added like this label every two weeks. Let me.
Robert Pająk (Splunk Inc.) 00:30:52 know.
Severin Neumann (Bronto) 00:30:53 Let me actually report that.
Let me create a new issue… Blank issue. Stale bar and… To be able to follow up.
You see.
I think we closed him after a year.
Robert Pająk (Splunk Inc.) 00:32:26 Okay.
This one, which we have opened, like, a minute ago, probably was two years old.
Severin Neumann (Bronto) 00:32:35 Sorry?
Robert Pająk (Splunk Inc.) 00:32:36 I mean the one which you opened just a second ago. I think it was even two years old or something like that.
the CJOS issue.
Severin Neumann (Bronto) 00:32:47 Yeah, let me suggestion, as… Okay, we should… See if we can configure stale… See? 2 more.
the follow.
Landlord.
triage enables one.
So, I just… Create this issue… Then let me put it also, at least in EU or no, let me put it in GCTC channel.
Robert Pająk (Splunk Inc.) 00:33:26 Hmm.
Severin Neumann (Bronto) 00:33:35 So, okay.
I… This was the one we actually looked into, right?
Yeah, this was…
Robert Pająk (Splunk Inc.) 00:33:49 And you see 2024. That's what I told you. It's two years old.
Severin Neumann (Bronto) 00:33:53 Okay.
Robert Pająk (Splunk Inc.) 00:33:54 not.
Severin Neumann (Bronto) 00:33:54 Closing this, Estee, a little.
Robert Pająk (Splunk Inc.) 00:33:57 Yeah, I think we can.
Seizures was the only one.
Who notices the problem? We didn't discuss it. Yeah.
Maybe it's not planned.
You're not using this, right?
I use it a lot.
Severin Neumann (Bronto) 00:34:15 Yeah, no worries.
I often forget that it's here. TLS certificate reloading in SDK.
I mean, very similar situation and Pablo opened this in 2024.
And then nobody cared.
Robert Pająk (Splunk Inc.) 00:34:33 Yes, I would close it, personally.
It's too hard.
Severin Neumann (Bronto) 00:34:50 Resource remove an attribute.
Doing the thing, just I'm gonna…
Robert Pająk (Splunk Inc.) 00:35:00 Resources are immutable. You cannot remove an attribute.
You cannot do it by design.
Severin Neumann (Bronto) 00:35:08 any.
Robert Pająk (Splunk Inc.) 00:35:09 common.
Severin Neumann (Bronto) 00:35:09 on that.
And just…
Robert Pająk (Splunk Inc.) 00:35:12 You can close it as stale, right? Anyway.
Severin Neumann (Bronto) 00:35:15 Yeah. I can close it as still as well.
Robert Pająk (Splunk Inc.) 00:35:17 Like, what what Daniel written has written is correct. Entities are a replacement or are going to solve the issue.
Severin Neumann (Bronto) 00:35:25 Yeah.
I just close it, Estelle.
Robert Pająk (Splunk Inc.) 00:35:29 Yes.
Severin Neumann (Bronto) 00:35:31 A specification for managing sessions. Oh, wow, that's browser sick.
I think I tagged them here.
Browser… approvers…
Robert Pająk (Splunk Inc.) 00:35:43 I think you, you again paused the sharing. That's my guess.
Severin Neumann (Bronto) 00:35:46 Sorry?
Robert Pająk (Splunk Inc.) 00:35:47 I think you paused, screen sharing because I still see.
Severin Neumann (Bronto) 00:35:50 Oh, yeah, yeah, yeah. I often do this when I copy a new… so…
Robert Pająk (Splunk Inc.) 00:35:53 I know, I have the same problem.
Severin Neumann (Bronto) 00:35:55 browser… Please, hey?
I'll look into this issue.
Actually.
Oh, no.
So it's like.
Moment.
info… Right?
Robert Pająk (Splunk Inc.) 00:36:19 Is there already someone working on it?
Severin Neumann (Bronto) 00:36:21 Yeah, yeah, I think so. There's some bunch of stuff going on, but then maybe they should say, like, oh.
this is happening already, or whatever, or we wait for the… still waiting for the prototype, or whatever, but just, like, they should give some feedback on it.
Cool.
Okay, I closed that one. Oh, I forgot to remove…
Robert Pająk (Splunk Inc.) 00:36:43 Remove labels.
Severin Neumann (Bronto) 00:36:45 labels… Okay.
Wow.
takes Github a little bit.
1, 2, 3.
1, 2, 3… Okay, whatever.
Support besides sampling and all span life cycle.
Robert Pająk (Splunk Inc.) 00:37:16 Oh.
Severin Neumann (Bronto) 00:37:17 Looks very… Dale.
Robert Pająk (Splunk Inc.) 00:37:21 Yeah, and… Extremely hot as well.
Severin Neumann (Bronto) 00:37:26 Yeah.
Hmm.
Robert Pająk (Splunk Inc.) 00:37:35 Oh, yes, and the response, which was the response, the latest response?
It looks valid. Yeah, this one, Daniel.
Severin Neumann (Bronto) 00:37:43 the.
Robert Pająk (Splunk Inc.) 00:37:44 Totally agree with his answer.
Severin Neumann (Bronto) 00:37:46 Okay.
Yeah, I just… I mean, if people come back, we can say, like, hey, there was this answer, this looks good, whatever.
But then I don't make myself like the person that needs to have this conversation, right?
Robert Pająk (Splunk Inc.) 00:37:58 clearly.
Oh, who's there?
Severin Neumann (Bronto) 00:38:00 Brad, open clarify how export retry should be implemented.
Robert Pająk (Splunk Inc.) 00:38:11 Okay, so…
Severin Neumann (Bronto) 00:38:24 And then here, Brad also linked to it, like, two weeks ago, so I would like to really tag him and say, like, hey, is this relevant?
Robert Pająk (Splunk Inc.) 00:38:32 To be honest, could you show the spec PRs? I think Tyler's spec PR It's… kind of… addressing it.
Severin Neumann (Bronto) 00:38:44 Do you know how Flag.
Robert Pająk (Splunk Inc.) 00:38:48 Give me… Can you just open a new tab with spec PRs?
OpenSpec PR.
Severin Neumann (Bronto) 00:38:53 Yeah, just give me a second.
Robert Pająk (Splunk Inc.) 00:38:54 think.
Severin Neumann (Bronto) 00:38:58 Oh, you mean there's, like, a… happened.
Did I open? No.
I opened it in another window.
But now it's… Here you go.
Can you say something?
Robert Pająk (Splunk Inc.) 00:39:20 Yes.
Yes, that's the one.
Time out once it hurt.
This is related.
Very much.
Severin Neumann (Bronto) 00:39:30 Yeah, let me…
Robert Pająk (Splunk Inc.) 00:39:43 Yeah, that makes sense as well.
Severin Neumann (Bronto) 00:39:48 Then I turn it into needs info.
And here we go.
Cool.
We can't accurately… Calculate a critical blocking path for async services. Should we add previous sibling span ID as an optional span attribute?
That's like.
stalled, right?
Robert Pająk (Splunk Inc.) 00:40:19 Yes.
Severin Neumann (Bronto) 00:40:35 "Adding a means to deny preference for linguae span in given context.
Robert Pająk (Splunk Inc.) 00:40:42 It's a preference.
Okay.
Severin Neumann (Bronto) 00:40:48 I mean, yeah, there's also stale arches.
Robert Pająk (Splunk Inc.) 00:40:52 Yeah.
Severin Neumann (Bronto) 00:40:54 I mean, people still kind of like it. It's not a credit.
Should tracers, loggers, meters be enabled by default?
Stale?
Robert Pająk (Splunk Inc.) 00:41:13 Yeah.
I think the spec is anyway.
Severin Neumann (Bronto) 00:41:20 Evolved from that, right? So…
Robert Pająk (Splunk Inc.) 00:41:21 I think it's already stable, I don't think… It will help anyway.
Severin Neumann (Bronto) 00:41:26 Instagram exemplar reservoir and performance impact, and then it's like nothing happened also for almost over two years now.
Robert Pająk (Splunk Inc.) 00:41:36 Yeah.
Closing this thing.
Severin Neumann (Bronto) 00:41:44 Clarify the valid content and primitive type.
train… And then there was an OTAP.
That was closed.
Stale?
Robert Pająk (Splunk Inc.) 00:42:00 Yeah.
I know Josh Surat recently picks It's OTLP.
But it's very English speaking, and probably it speaks with AI.
Severin Neumann (Bronto) 00:42:13 Okay… Did I forget?
Robert Pająk (Splunk Inc.) 00:42:17 See you when I'm done.
Severin Neumann (Bronto) 00:42:18 To remove some… Tax again… Question, accent, plar, symbol of accent.
Let's see again, like that's again one that has not been addressed over two years.
I suspect that a lot of them are now like that, that there's, like, probably all… 50 something.
Robert Pająk (Splunk Inc.) 00:43:03 Like, the problem with this previous one, It looks like it's… Likes clarification in the Matrix SDK.
But yeah, the problem is that nobody's pursuing these issues.
Severin Neumann (Bronto) 00:43:15 Yeah.
Robert Pająk (Splunk Inc.) 00:43:19 collection.
Severin Neumann (Bronto) 00:43:24 Okay, how should we continue? Like, should we do some more?
Robert Pająk (Splunk Inc.) 00:43:30 What's the time?
30, maybe, maybe just two more.
Or 3 more.
There are…
Severin Neumann (Bronto) 00:43:42 Yeah, there's again, like, no movement for, like, ever.
Robert Pająk (Splunk Inc.) 00:43:45 Yeah.
And I also think it's, I kind of, if I remember correctly, these issues were created before Metrics SDK got stable.
Group consensus studies, yeah.
This is even deprecated totally, because right now we have development and stable and alpha, beta.
Yeah.
Severin Neumann (Bronto) 00:44:12 Oh, I forgot the too late.
Robert Pająk (Splunk Inc.) 00:44:14 Yeah.
Severin Neumann (Bronto) 00:44:14 And…
Robert Pająk (Splunk Inc.) 00:44:19 I think we can go through all of them like that.
Severin Neumann (Bronto) 00:44:22 Yeah, so if you like, I mean, I… if you… I mean, I can… if you like, I can still go on.
And do a few more, and just everything that's, like, 2 years.
Robert Pająk (Splunk Inc.) 00:44:33 I can be… I can be here with you, so I can double check if there's really nothing that is, you know, very important, old.
Severin Neumann (Bronto) 00:44:41 Okay.
Robert Pająk (Splunk Inc.) 00:44:42 applicable.
Severin Neumann (Bronto) 00:44:43 Okay, then let me…
Robert Pająk (Splunk Inc.) 00:44:45 And you can just, you know, mechanically click. I react if something catches my eye.
Severin Neumann (Bronto) 00:44:50 Okay, and then if something catches your eyes, you just say, like, okay, let's take it away.
Robert Pająk (Splunk Inc.) 00:44:55 So sorry.
Don't touch the keyboard.
Severin Neumann (Bronto) 00:44:59 I'm your agent now. I'm clear.
Robert Pająk (Splunk Inc.) 00:45:01 Yes.
Severin Neumann (Bronto) 00:45:01 you.
Let me just open 25 of them and then like.
To them, like, in a… Rick.
Robert Pająk (Splunk Inc.) 00:45:15 Or, for instance, yeah, this one can be…
Severin Neumann (Bronto) 00:45:20 Close.
Robert Pająk (Splunk Inc.) 00:45:21 Yep. Yeah.
both.
Severin Neumann (Bronto) 00:45:27 You know what? I spare myself from the labeling, and I do that in batch at the end. Right? I just close all of them, and then later I take the ones that are still labeled and just do them in a batch.
attendant.
Robert Pająk (Splunk Inc.) 00:45:38 Okay.
Severin Neumann (Bronto) 00:45:39 So we'll just go through them.
Robert Pająk (Splunk Inc.) 00:45:41 We can just go through the tabs. Schema transformations should be able to convert metrics.
Yeah, further.
Severin Neumann (Bronto) 00:45:53 Hmm.
Robert Pająk (Splunk Inc.) 00:46:00 Huh? That one is interesting. I will keep it.
Severin Neumann (Bronto) 00:46:04 Yeah, and what should I do?
Robert Pająk (Splunk Inc.) 00:46:07 Yes.
Okay. Do you remember one of the recent CJSPR, when he tried to add… I'm not sure what's the status of it, when he wanted to add, like.
Guidance for instrumentation authors.
Do you remember what's the state of this pier? I remember that.
Severin Neumann (Bronto) 00:46:29 Yeah, I remember this, the supplementary guidelines, supplementary… 5191, could this be the case?
Robert Pająk (Splunk Inc.) 00:46:40 It's very new one, so yeah. I… because I think you can know how to handle it.
Yeah, and there was also one in OpenTelemetry.io. Yeah.
Is this profitability?
So.
The question is if it's related to this one, if it's not including already language.
Severin Neumann (Bronto) 00:47:03 Should I check, like, Is this address.
Robert Pająk (Splunk Inc.) 00:47:09 all…
Severin Neumann (Bronto) 00:47:11 This be addressed… My, and then I tagged…
Robert Pająk (Splunk Inc.) 00:47:16 Exactly.
Severin Neumann (Bronto) 00:47:17 CC and CJoy or?
Robert Pająk (Splunk Inc.) 00:47:19 See you, Joe.
Procedure he yeah.
He's still working on this one, because he even asked me, like, last week, if I can take a look at this PR.
Severin Neumann (Bronto) 00:47:30 Yeah. So then I turn this into needs info.
And we're good, and we can do the next one.
Recording externally sample metrics without resampling has not been looked into for three years.
Robert Pająk (Splunk Inc.) 00:47:46 never… Yeah, nobody cares.
Severin Neumann (Bronto) 00:47:58 The expo histogram zero threshold configuration.
Still, for like 3 years. Huh?
Robert Pająk (Splunk Inc.) 00:48:08 Yes, yeah, close.
Severin Neumann (Bronto) 00:48:11 Okay, I close until you say otherwise.
Robert Pająk (Splunk Inc.) 00:48:13 Yes.
Severin Neumann (Bronto) 00:48:14 Okay.
Do we need a spec for console output format?
Robert Pająk (Splunk Inc.) 00:48:21 Outdated. We already specified that we do not want it.
Severin Neumann (Bronto) 00:48:25 So we already… Decided that we do not want to do this, right?
Robert Pająk (Splunk Inc.) 00:48:34 Yes.
We have a spec. The spec says that it's.
It's not standardized.
Severin Neumann (Bronto) 00:48:42 Yeah, advice HIN API should be applied to all signals when applicable.
3 years old.
Robert Pająk (Splunk Inc.) 00:48:50 This can be kept.
Severin Neumann (Bronto) 00:48:52 Yep.
Robert Pająk (Splunk Inc.) 00:48:53 Yeah.
There have been recent discussions, Ethan, regarding this.
Severin Neumann (Bronto) 00:48:57 Whom should I attack?
Or just…
Robert Pająk (Splunk Inc.) 00:49:01 Ludum Yua. Ludum Yua, maybe. Sorry? Ludum Yua.
Ludum, you are muted.
Oh, yeah, this car.
She can decide if we want to keep it or not.
Severin Neumann (Bronto) 00:49:20 And, add metric advice to capture only a specific set of values for a given attribute and normalize the rest of a value which restricts them.
Robert Pająk (Splunk Inc.) 00:49:27 is.
Severin Neumann (Bronto) 00:49:29 other There has not been any movement since 3 years. Again, this is irrelevant.
So I close it.
Robert Pająk (Splunk Inc.) 00:49:37 Yes, close.
Severin Neumann (Bronto) 00:49:38 That's not planned… Schema transformation process should be able to preserve original attributes.
Has also not… for, like.
Over 2 years, so I close it.
It's not planned.
Converting values that cause conflicts has a lot of discussion, but also not moved forward.
or ever Metric exporter specifies support batching per data point on top of per metric.
That has not moved for, like… ever… Loves.
Add account argument to histogram record API.
Also not really doing any movements here.
Research merge error for different versions. Oh, there was some progress in August.
Robert Pająk (Splunk Inc.) 00:50:47 Yeah.
Severin Neumann (Bronto) 00:50:48 Oh, and there's Mike.
Daniel, you commented on it. So I just removed the follow-up label, right? So…
Robert Pająk (Splunk Inc.) 00:50:58 Yeah.
Severin Neumann (Bronto) 00:50:59 It seems to make some progress.
I don't know.
Exporter OTEM should be retriable or not.
That's stalled as well.
How's this look?
Ignore transactions and consistent probability.
Ability sampling… Stone… Claws and stuff.
Equivalent of log level for spans, yeah, that's…
Robert Pająk (Splunk Inc.) 00:51:30 It's yours.
Severin Neumann (Bronto) 00:51:31 Yeah, yeah, but it's…
Robert Pająk (Splunk Inc.) 00:51:33 Alright.
Severin Neumann (Bronto) 00:51:35 There's, like… I just…
Robert Pająk (Splunk Inc.) 00:51:38 Okay.
Severin Neumann (Bronto) 00:51:39 I mean, we made some things in that, but not really. So support explicitly removing attributes from instrument API. Let's even, oh, there's some progress. I think this should remain open. The semantic key missing.
Robert Pająk (Splunk Inc.) 00:51:54 Yeah, this one.
This one is actually in progress.
Severin Neumann (Bronto) 00:52:01 Okay, cool. So I keep it. Is it ready already? Like, is something happening here or is it just still needing community feedback?
Robert Pająk (Splunk Inc.) 00:52:09 I'm just checking… I know there's been some prototypes. I know Tyler created a prototype for AutoGo, which is experimental. I'm not sure, and I think it's exactly about this one.
Okay. I'm not sure about, I'm not sure about other, and if there's anyone who is leading this effort.
Who has created this issue?
It will be good if someone is assigned to it.
Severin Neumann (Bronto) 00:52:38 A soften.
has created it in 2022.
Robert Pająk (Splunk Inc.) 00:52:47 You can write it to me, I'll double check if.
Severin Neumann (Bronto) 00:52:51 Should I assign it to you, or should I tag you?
Robert Pająk (Splunk Inc.) 00:52:56 Just tag me.
Or even write me on Slack.
I will double check if it's actually something which I think it's related to, because I'm not 100% sure.
Severin Neumann (Bronto) 00:53:06 And drop it into your… Here we go.
Again, and then we resume… Blah blah blah blah. Okay.
Define low, high cardinality…
Robert Pająk (Splunk Inc.) 00:53:31 Oh!
Is it not some cons?
Severin Neumann (Bronto) 00:53:35 Huh?
Robert Pająk (Splunk Inc.) 00:53:36 I think it's Sam Khan's.
Severin Neumann (Bronto) 00:53:37 Okay, I can move it over.
Transfer issue… Okay. Add force flush to tracer provider trace API.
Robert Pająk (Splunk Inc.) 00:54:03 the.
Severin Neumann (Bronto) 00:54:03 Classification…
Robert Pająk (Splunk Inc.) 00:54:05 What's the brand?
Severin Neumann (Bronto) 00:54:06 prompted…
Robert Pająk (Splunk Inc.) 00:54:07 No.
Severin Neumann (Bronto) 00:54:08 Huh?
Robert Pająk (Splunk Inc.) 00:54:10 That's all.
Severin Neumann (Bronto) 00:54:18 I mean, this seems to be the original author.
No, it's not.
I'm gonna open it. Then at some point, it got assigned.
Josh… Why did it get assigned to Josh at some point?
Robert Pająk (Splunk Inc.) 00:54:41 Automatic assignment, I wasn't sure.
Severin Neumann (Bronto) 00:54:45 Oh, you mean that this was happening at a time where we auto assigned stuff?
Robert Pająk (Splunk Inc.) 00:54:50 Yeah, yes, in 2022.
I would still close it. I… Yep.
Severin Neumann (Bronto) 00:54:58 So I removed the assignment.
Robert Pająk (Splunk Inc.) 00:55:00 Yeah, I'm closer still.
Severin Neumann (Bronto) 00:55:02 Oh?
I mean, someone bumped it in August.
So what I can do, I can tag them and say, like, hey, if this is still relevant for you, please… Make your case at the… Spec Meetings, something like that.
Define distribution.
Boy.
I will…
Robert Pająk (Splunk Inc.) 00:55:53 It was solved in the OpenSegment.io.
Severin Neumann (Bronto) 00:55:56 Yeah, yeah, yeah. I just, this is the smallest one, docs.
Let's just comment.
Structured stack trace and span attribute logs.
Oh.
Robert Pająk (Splunk Inc.) 00:56:12 Monthly conventions.
Severin Neumann (Bronto) 00:56:14 Yeah.
Robert Pająk (Splunk Inc.) 00:56:16 Or… are we sh… yeah… Yeah, let's move it there.
Severin Neumann (Bronto) 00:56:23 Move it.
Robert Pająk (Splunk Inc.) 00:56:24 Yes, let's move to semantic conventions.
At least it will be cleaner here.
Severin Neumann (Bronto) 00:56:45 Okay, propose a clarify behavior when retrieving non-existent, currently active span.
It's stalled, right? But I'm not sure if it's still relevant.
Robert Pająk (Splunk Inc.) 00:57:04 No, I don't think so. I think it can… Okay, yes, still.
Severin Neumann (Bronto) 00:57:18 Support for asynchronous histogram instrument.
That's also staled.
Remove spec for in-memory export first.
Robert Pająk (Splunk Inc.) 00:57:39 Could you bring up the previous one? I'm not sure it should be closed, or maybe it's… This, I think… histogram.
Is it not already implemented?
Severin Neumann (Bronto) 00:57:51 Which one? The other one I just closed.
Robert Pająk (Splunk Inc.) 00:57:54 Yes, this one. The thing is that I think something like that exists in Prometheus.
Yeah.
Severin Neumann (Bronto) 00:58:03 Should I reopen it, or should I…
Robert Pająk (Splunk Inc.) 00:58:05 Give me a second, to… I know…
Severin Neumann (Bronto) 00:58:10 I can also link copy to you and you can take another look.
Robert Pająk (Splunk Inc.) 00:58:13 Yes, let's do it.
And I will take a look just after the meeting.
I think it may be already solved.
Severin Neumann (Bronto) 00:58:21 Okay.
Cool.
Should we stop now? It's like two minutes left.
Robert Pająk (Splunk Inc.) 00:58:27 How many… how many… how many are left?
Severin Neumann (Bronto) 00:58:30 Those 3, and then another 25, or something like that?
Robert Pająk (Splunk Inc.) 00:58:34 Also, next time.
Severin Neumann (Bronto) 00:58:36 Oh.
Robert Pająk (Splunk Inc.) 00:58:38 We can, we can move, you, we can finish with those three, which are open. Okay.
And then…
Severin Neumann (Bronto) 00:58:45 Removes back for in-memory exporters.
Robert Pająk (Splunk Inc.) 00:58:48 Your post again.
Severin Neumann (Bronto) 00:58:50 Huh?
Robert Pająk (Splunk Inc.) 00:58:51 You have… you're sharing his post.
Severin Neumann (Bronto) 00:58:53 Sorry.
See it now? Removes pack for in-memory exporters.
Robert Pająk (Splunk Inc.) 00:59:01 Why would we remove this pack? I do not understand.
Stale. Remove.
Severin Neumann (Bronto) 00:59:06 Bill.
Robert Pająk (Splunk Inc.) 00:59:07 Keeping this open.
Severin Neumann (Bronto) 00:59:12 Removes… Oh, no, okay, sorry.
Robert Pająk (Splunk Inc.) 00:59:16 Yes.
Severin Neumann (Bronto) 00:59:18 Specify how OpenTelemetry will deal with idle metrics no longer being reported.
I don't know, stale, right?
And by then, I think we are in a really good shape.
Yeah, there's another… I can, those… I, I, I delabel all of them, and then there's, like, it's open… So there's 15 left.
So we can, I mean, there will be another bunch next week because a lot of the ones we, we, we delabeled will, will come back at some point. But yeah, I think we, we make some progress here.
Robert Pająk (Splunk Inc.) 01:00:12 The first one, you should go.
I think you have not clicked the button.
Severin Neumann (Bronto) 01:00:17 This one? Add force plus…
Robert Pająk (Splunk Inc.) 01:00:20 Yeah, yeah.
Severin Neumann (Bronto) 01:00:21 No, no, I asked that guy.
Robert Pająk (Splunk Inc.) 01:00:23 Okay, yes.
Severin Neumann (Bronto) 01:00:25 But I should remove the follow up and add a needs info.
That's a good point.
And then now for the is closed.
I can… Take donuts.
Robert Pająk (Splunk Inc.) 01:00:40 Legos.
Severin Neumann (Bronto) 01:00:41 And drop any triage labels.
No.
Robert Pająk (Splunk Inc.) 01:00:49 I think that's good.
Severin Neumann (Bronto) 01:00:50 That's good. I think that's enough, right? I mean, I can…
Robert Pająk (Splunk Inc.) 01:00:52 Yeah.
Severin Neumann (Bronto) 01:00:56 Okay. Talk to you maybe next week? No, I think we talk on Wednesday at the shared whatever GCTC meeting.
Robert Pająk (Splunk Inc.) 01:01:03 Yes, indeed.
Severin Neumann (Bronto) 01:01:05 theater.
Robert Pająk (Splunk Inc.) 01:01:05 See you. Bye-bye. Thanks.
