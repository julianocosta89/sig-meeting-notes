SIG: GC Project Management (EU)
Date: 2026-01-12
Duration: 36 minutes
Zoom Recording URL: https://zoom.us/rec/share/fc6MDXb1YfF9YMCOI7Ms-Cz6ZRVRZEyyX2PbXqdReNDrKc34WYkOOJlUH7wvVsfg.8D2FOZkeZicLodno
============================================================

## Zoom Recording Transcript

**Juraci Paixão Kröhling** 03:58 Hello, hello, hey, Pablo.
**Pablo Baeyens** 04:01 Hey, good morning.
**Juraci Paixão Kröhling** 04:03 Morning, Happy New Year, man.
**Pablo Baeyens** 04:05 Yep, happy new year.
How is it going?
How was it while I was out?
I mean, well, two of those weeks were a quiet period, but I was out also, like.
December 17th, or so.
**Juraci Paixão Kröhling** 04:21 Yeah, I mean, I don't know what is a quiet period, but yeah, no, it was fine.
**Pablo Baeyens** 04:28 meetings.
**Juraci Paixão Kröhling** 04:29 At least no open telemetry meetings, yes, that's true.
No, that's fine.
I did. Well, I did take two weeks off, but it's not really… So I spent doing other things, like finishing the book that I was writing to my fair… to my… to my dad, And then I started drafting a book about OpenTelemptu Collector.
**Pablo Baeyens** 04:57 Huh, cool.
**Juraci Paixão Kröhling** 04:59 Based on the cookbook that, that, the repository… so I have a repository called Hotel Collector Cookbook.
And for some time, I was thinking about writing something about it, like, converting that into a proper book.
So I kickstarted, sent to a few publishers, and let's see. Let's see if anybody is interested in… In making, like… Publishing the book, so… So this is the repository that I've spoken about.
It's here in the meeting chat.
Yep.
And I created a lot of content, so I prepared… A lot of content to be published this year.
I think the first one you might have seen.
**Pablo Baeyens** 05:51 Right, it's the one we talked about the.
**Juraci Paixão Kröhling** 05:54 Exactly.
**Pablo Baeyens** 05:55 messages analysis, yeah.
**Juraci Paixão Kröhling** 05:56 Yep, yep, yep, yep.
Yeah, that's one of them.
**Pablo Baeyens** 06:03 I don't know if anybody else is joining… Acknowledge… I can… Share my screen.
Yay, still… Ayy.
I think we can… I mean, there's active discussion on this.
We can Probably just say… Community feedback… Do you agree? Sorry, I'm not sure if you were saying something, you're muted.
**Juraci Paixão Kröhling** 07:47 Sorry, no, I was not saying… I was reading the message here. I, I, It's true, but it doesn't imply that it's sufficiently unique to identify the resource, and consequently, if… It doesn't imply that all resources are required to… I mean, this is part of… Is that there's a counter, for example.
Maybe it's instant, but also database name as resource entry, which just means two different sets of resources can show the same source.
I… So… has, hold on a second, the kid's call is calling. Just one second.
**Pablo Baeyens** 08:34 Okay.
Hey, Sabrin.
**Severin Neumann** 08:49 Hello, hello.
Jess, give me a second as well.
**Pablo Baeyens** 08:54 Sure.
**Severin Neumann** 09:23 Oh… Okay… What have you been talking about?
**Pablo Baeyens** 09:35 No, not much, we were both reading the… Yeah. I was saying… There's active discussion on this from one hour ago.
**Severin Neumann** 09:43 Yeah.
**Pablo Baeyens** 09:43 I'm tempted to just say community feedback and…
**Juraci Paixão Kröhling** 09:46 So, I… I need to pick up my kid at kindergarten, and I'm vexing.
**Severin Neumann** 09:53 Ours.
**Juraci Paixão Kröhling** 09:54 Alright, see your folks.
**Severin Neumann** 10:00 Okay, sorry.
**Pablo Baeyens** 10:03 Right, yeah, I was saying, since there's active discussion on… I mean, it's… It's a question that may or may not lead to a clarification on the spec. I would say community feedback is the right Classification.
**Severin Neumann** 10:17 Yeah, yeah.
Yeah.
**Pablo Baeyens** 10:22 I'll keep it open, because I think… Jersey was saying something. I don't think this is a SIG issue.
Into Forest, it's like… Across several things, Prometheus, on semantic mentions, and…
**Severin Neumann** 10:41 Mmm.
**Pablo Baeyens** 10:45 So, yeah, I mean, let's keep it open, and if Jurassi says something… Weekend… Revisited.
**Severin Neumann** 10:59 Your best metrics level function.
Sana.
Is there any ongoing discussion or any comments already?
**Pablo Baeyens** 11:36 Nope.
**Severin Neumann** 11:45 Yeah, because I think, I mean, it begins with, like, a community discussion, right? I mean.
**Pablo Baeyens** 11:57 Yeah, and this is still under active discussion.
**Severin Neumann** 12:01 Run.
**Pablo Baeyens** 12:29 Okay, so, I don't think this is accepted or rejected.
**Severin Neumann** 12:41 No, no, it's definitely… Deciding, and then something like, needs feedback, or community just… it's just net new, right? I mean, if you come back to it, like, when it's back into follow-up, then we can look at it differently, but yeah, just give it community feedback.
**Pablo Baeyens** 13:01 Okay.
**Severin Neumann** 13:16 Span link directive. Make span link direct.
Spaneling, directive, and context propagation header.
**Pablo Baeyens** 13:27 That's suspense.
**Severin Neumann** 13:30 It's my expelling.
Oh… do you have a… okay, at the end, it's about triage, right? I mean, there's not yet a lot of… This is net new, right?
Yeah, so I think it's, again, like a community feedback thing. It just requires a lot of feedback, right? It's more like…
**Pablo Baeyens** 14:28 Yeah, I don't have an answer for them, but I'm going to guess this can be solved in a different way than what they are proposing that is already supported.
Without having bread.
every single thing.
**Severin Neumann** 14:42 I mean, if you think, like, you can answer to it and, like.
drive the discussion, then yeah, then maybe give Dan a try.
Yeah.
**Pablo Baeyens** 14:52 No, I… let's put community feedback, because I don't… I haven't read the whole thing, it's just a gut feeling, and I don't want… Yeah.
Food something… That is not accurate.
Okay, I mean, this is accepted.
**Severin Neumann** 15:28 Yeah, this is an editorial thing.
And can you add an editorial label as well?
Just editorials, or something like that, yeah.
I think the last one we just put into… Tease, or is it just accepted?
I mean…
**Pablo Baeyens** 16:10 The last one, I put it on.
**Severin Neumann** 16:11 No, no, no, no, no, this one, the, the, the OT.
**Pablo Baeyens** 16:14 Oh, the… This one, you mean.
**Severin Neumann** 16:17 Yeah, this was the Jager one, right? And that was more like… Triage deciding, TC inbox.
Yeah, I think we should do the same thing and say, like, hey, TC…
**Pablo Baeyens** 16:32 Okay.
So…
**Severin Neumann** 16:36 They will talk about this anyway, so I assume, so… .
**Pablo Baeyens** 16:43 Well, yeah, but it's good to follow process.
**Severin Neumann** 16:47 Similar to whatever… Yeah.
Something like that.
Or please take a look, huh?
But I think that's…
**Pablo Baeyens** 16:56 Yeah, we're gonna say similar to,
**Severin Neumann** 16:58 Yeah, exactly similar, 24786.
Yeah.
But, but I think they, they… Yeah, it's obvious. I mean, it's from Carlos, I think I saw that Jack already is something.
**Pablo Baeyens** 17:08 Yeah, Jack has not voted.
**Severin Neumann** 17:11 Yeah, so there's already, like, a certain consensus, and I think deprecation should go through the TC inbox, so, yeah. No, I think we're fine.
**Pablo Baeyens** 17:23 Fair.
**Severin Neumann** 17:30 And entries for complex attributes.
**Pablo Baeyens** 17:35 this Sims editorial.
**Severin Neumann** 17:39 Yeah. Yeah.
**Pablo Baeyens** 17:42 Or… I mean, I don't…
**Severin Neumann** 17:45 Yeah, I think, I mean, there is maybe some debate open, like, about the how and what and why, but I think at the end, it's, like, not something that requires… a lot of… Fair enough.
**Pablo Baeyens** 17:59 let's say accepted already, and yeah, maybe editorial, I don't know.
**Severin Neumann** 18:04 Yeah, but I don't think there's any… Because it's more cosmetic than any, like, real… Real change, right?
**Pablo Baeyens** 18:14 Right, yep. Yeah, that was my… that was my point, but, yeah, maybe… There is some debate, exactly, on.
**Severin Neumann** 18:22 Yeah.
**Pablo Baeyens** 18:23 What does it mean, soap?
To support it. So let's just put accepted, ready.
**Severin Neumann** 18:41 Stabilize Prometheus.
Is this, I mean, this enteropis is a sick issue?
**Pablo Baeyens** 18:52 Yeah, on this one, it also seems like it's the issue, so let's… let's the issue… Huh, no, no.
Issued.
**Severin Neumann** 19:43 4873… It's probably a 773, but yeah.
**Pablo Baeyens** 19:53 Yeah, the…
**Severin Neumann** 19:54 But just comment on it, I think it's like…
**Pablo Baeyens** 19:59 We can let him correct it.
**Severin Neumann** 20:04 Maybe? I don't know. Just let him know that it's this wrong number, and he can… Typically… this looks like a… Is this an in-sync issue for declarative configuration, or is it… .
**Pablo Baeyens** 20:25 I think it's a sick issue. It's…
**Severin Neumann** 20:28 Yeah.
Yeah.
Didn't take it like that, so…
**Pablo Baeyens** 20:47 On… this is the last one.
This is… Also a big issue?
from the sampling sig…
**Severin Neumann** 21:15 Preston and learn, I'll take care.
Yeah, it's, sampling, sick sampling thing, yeah.
**Pablo Baeyens** 21:31 Say you seekish as well, 10.
Okay, I think that is everything on this Back, repo… Right… And we have… This one, in case Jersey comes back.
We can take a look at the community.
across, well…
**Severin Neumann** 22:15 Okay, so…
**Pablo Baeyens** 22:19 Dis… 2… I think our repo maintenance?
**Severin Neumann** 22:29 Yeah.
**Pablo Baeyens** 22:49 Look at these two that are more recent.
**Severin Neumann** 22:51 Yeah, this one was opened on the OTLIO repo, and I moved it to Community. It's… it might belong into Collector or any other repository, because someone is like, hey, we rent some… Security checks, and… no.
Whatever.
**Pablo Baeyens** 23:09 Yep.
**Severin Neumann** 23:10 Yeah, especially now I see receivers and exporters, host metrics, locks and trace.
Oh yeah, no, I see it. I singed it.
**Pablo Baeyens** 23:19 Yeah, we need more information from.
**Severin Neumann** 23:21 Yeah, exactly, so not sure if there's a needs info label or something like that, so…
**Pablo Baeyens** 23:26 I'm guessing I can remove it from the sitcoms project?
**Severin Neumann** 23:30 Oh yeah, absolutely, yeah, yeah.
**Pablo Baeyens** 23:33 Okay.
**Severin Neumann** 23:35 Do we have a needs info or something like… yeah, needs author feedback. Put it like that, yeah.
**Pablo Baeyens** 23:43 Okay… And then… This one…
**Severin Neumann** 23:55 Yeah, so they want to use, play SDK console or whatever, I just ask a bunch of questions, but I'm actually not. So with those kind… if you scroll down, I think there's a little bit… what was the last status?
Yeah, I think… I don't know exactly, like, how this works these days with Sig Infra.
If anybody is actively looking in those… to those things, or… Yeah, I mean, technically, you or I or whatever could handle that, but yeah, anyways.
**Pablo Baeyens** 24:42 Yeah, I guess it's… Sig infra… Should morally do it, even if we can't.
Yeah.
Okay.
**Severin Neumann** 24:58 I don't know if there's an infra label or something like that, so… Project in front, yeah.
**Pablo Baeyens** 25:07 Cool.
I think this one… And probably be closed, since it's been a while since this was released.
But… I don't want to close it myself. If you think it makes sense, I'll pay include Lyudmila.
**Severin Neumann** 25:47 Yeah, I don't know, for those feedback issues, I… I don't know.
If there's any idea how long… how long they should stated way, Ryan.
**Pablo Baeyens** 26:01 I don't think there is, so…
**Severin Neumann** 26:03 Yeah.
**Pablo Baeyens** 26:38 Okay, I'm in.
we can…
**Severin Neumann** 26:48 Awesome.
**Pablo Baeyens** 26:49 That's funny.
I think that's, far ago, but, like, it's… Enough time ago, October 23rd, so… Okay, anything else that we should check?
**Severin Neumann** 27:13 There's always something to check on, but I'm also not sad if we… We'll keep it short today.
Yeah, yeah.
**Pablo Baeyens** 27:22 like, if you think there's maybe something on GC work to check, but…
**Severin Neumann** 27:29 There's always something to check, a document again.
Can you click quickly into the Dart SDK and API for OpenTelemetry? I mean, it's unassigned, right?
**Pablo Baeyens** 27:48 Yes, it's unassigned, and it's marked as waiting on orders.
**Severin Neumann** 27:58 Oh, he has updated something last month.
That's new. I missed it, totally, I must admit.
Can you hover over the last months when this was? Like, when did he raise that?
**Pablo Baeyens** 28:12 December 17th.
**Severin Neumann** 28:14 Come on.
The arcade that got lost in… Everybody being off. I'm just basically back, right? I was on a company offset last week, so…
**Pablo Baeyens** 28:29 Okay, should we discuss this on the GC meeting?
I hope this.
**Severin Neumann** 28:44 Once I stock, I'd be on an island.
Yeah, maybe we should talk about this once again on… On Wednesday, maybe let's put it on the agenda.
Let's put it back.
**Pablo Baeyens** 29:08 Okay, I'll do that, once I've stopped sharing my screen.
Okay, I'm gonna see if I can do the tree edging for… The community ripple.
And, Yep, I think that we can call it a day.
**Severin Neumann** 29:37 Awesome.
And talk to you on Wednesday, right?
**Pablo Baeyens** 29:41 Yep, see you on Wednesday.
**Severin Neumann** 29:44 Bye-bye.
**Pablo Baeyens** 29:44 Bye.
