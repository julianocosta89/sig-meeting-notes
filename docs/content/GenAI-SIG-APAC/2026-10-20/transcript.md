SIG: GenAI SIG (APAC)
Date: 2026-10-20
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 02:33 Hello!
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 02:39 No.
**Trask Stalnaker (Microsoft Corporation)** 02:42 Good morning, good evening.
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 02:44 Good, good evening.
**Liudmila Molkova** 02:48 Are you there very early or very late?
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 02:51 Actually, we're very late, it's… it's 10… it's 10.30 in the PM.
You know…
**Trask Stalnaker (Microsoft Corporation)** 03:02 Yeah, I understand.
**Liudmila Molkova** 03:03 How are you?
**Trask Stalnaker (Microsoft Corporation)** 03:04 And it's gonna be… we'll have to figure out what to do… When, daylight savings changes.
In a couple of weeks.
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 03:16 Oh, Steve, told me that, about the time change, so… I would say, if we have one hour later for us, that will be too late for us. Maybe we should change another time, maybe… Switch to the… the morning in China and the afternoon in the United States.
Is that… does that, look good to you, or you have any better suggestions?
**Trask Stalnaker (Microsoft Corporation)** 03:53 Yeah, what, what time would… That be… Let's see… Huxing Zhang (Alibaba Cloud (Singapore) Private LTD) 04:06 Yeah, we… usually we do, like… Maybe 9 AM in China time will be usually good for us, any working day.
Because it's, like, half… Half an hour or so.
That would be… Should work for us, and generally work for us.
**Trask Stalnaker (Microsoft Corporation)** 04:32 Okay, so that would be… Right now, that's 6PM for us, with daylight… after daylight savings changes, that would be 5PM.
For us…
**Liudmila Molkova** 04:51 Yeah, 9am for you folks, 5pm for us.
I can do it most of the days, and then I'll Trask How do you feel about it?
**Trask Stalnaker (Microsoft Corporation)** 05:05 I think I could do it on Mondays… Probably… Work… Tuesdays and Wednesdays.
That's a little harder for me.
**Liudmila Molkova** 05:21 Okay.
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 05:21 Excellent.
**Liudmila Molkova** 05:24 Yeah, Hoshin?
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 05:26 So, Monday, U.S. time, so it's the Tuesday morning, China time, right?
**Trask Stalnaker (Microsoft Corporation)** 05:32 Right.
**Liudmila Molkova** 05:33 Yeah.
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 05:35 I think that will be good.
Of course, yeah, I think I can do it.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 05:43 Yeah, me too.
**Liudmila Molkova** 05:47 Okay, how should I.
**Trask Stalnaker (Microsoft Corporation)** 05:48 Cool. Let's give it a shot then, starting, what, in… Two weeks, probably? When is the daylight savings change today?
I mean, this year.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 06:03 November 1st?
**Trask Stalnaker (Microsoft Corporation)** 06:06 Okay, alright, so 2 weeks from today, we will… Or… Two weeks.
Minus a day.
I guess it's your… still your Tuesday there.
Yes, that would be our… Monday.
**Liudmila Molkova** 06:31 It'll still be 9 a.m, yeah.
**Trask Stalnaker (Microsoft Corporation)** 06:36 I can fix…
**Liudmila Molkova** 06:41 We're going to update calendar?
**Trask Stalnaker (Microsoft Corporation)** 06:42 Yeah…
**Liudmila Molkova** 06:44 Awesome, thank you.
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 06:46 Yeah, can you share your, link to that website you just shown to us? I think that's a pretty good website. I want to know from.
**Liudmila Molkova** 06:56 I just Google, time zone converter, and I pick one of them, there are a few, but yeah, it's very useful.
Okay, so let's see… The blog post.
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 07:29 Yeah.
**Liudmila Molkova** 07:32 Okay, I reviewed, and I think you addressed the changes, and I didn't come back to you, I'm sorry.
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 07:38 Yeah, I'm sorry I have a late response, because, yes, that's too much of my work due to my bandwidth, so I replied in late, so I already addressed your comments, and, maybe… you can take a look and check if they say… and I removed most of the… like, AI styles, that looks more human-readable, I think.
**Liudmila Molkova** 08:08 Yeah, thank you, I appreciate it. Yeah, I'll take a look, I'll try today.
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 08:13 Okay, psycho, appreciate it.
**Liudmila Molkova** 08:15 Yeah, thank you.
Okay, then let's talk about the user ID.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 08:29 Yeah.
I reply to your question.
**Liudmila Molkova** 08:34 Okay, so sorry.
Yeah, that's a good question. What should we… what should we call that user?
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 08:57 Mmm…
**Liudmila Molkova** 08:58 Yeah.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 08:59 Yeah, from my perspective, we have some, scenarios we want to record the user identify if, the user application passed the, parameter, like this.
yeah, firstly, yeah, we come up with, the fields called, GenI UserID.
And, I also, yes, there's the discussion in the repository before, and, I, I, I found some people, they suggest to use the, use ID without the GenI. This is, failed in, hotel semantic convention, but, you, you, you think, the use ID is too general, and, there are too many millions, on these, fields.
So maybe we can narrow the, Meetings to the GenAI user ID.
or something like this, I think we can discard the… The naming of these, fields.
**Liudmila Molkova** 10:23 Yeah.
I'm… I'm thinking how many users could there be?
**And is it the… ID. So what, what I see from your clients, all of them are the users associated with session, Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 10:45 Hmm.
**Liudmila Molkova** 10:46 And… This is the… Is it, What are the properties? So there are the other prop… is it… I'm kind of curious how the API looks like.
For… that allows to set it. Is it one property?
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 11:10 Hmm… Yeah, you can go back to the PR, and if I remember right, I… You also… Oh, there's a… API, yeah, from other…
**Liudmila Molkova** 11:34 Okay.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 11:54 And, I also… Found in some, GenI framework, something like long chain. It provides, annotation.
like a memory ID.
2… Pass this, User identify.
launch.
memory ID.
**Liudmila Molkova** 12:23 And I see them using user.
Yeah.
It sounds like from this one.
And… Give me a sec.
Not in this one.
We're seeing Agna and Agent Scope.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 13:11 In a long… long-chain, long-chain 4J in Java version, so it's a… annotation called the memory ID.
**Liudmila Molkova** 13:20 Can you share a link?
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 13:26 Wait for a moment, let me search.
**Liudmila Molkova** 13:44 Yeah, this is what makes me scared.
User session or resource success policy.
I think these are two different beasts.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 13:55 I… I… I… I sent a link.
**Liudmila Molkova** 13:59 Yeah, thanks.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 14:00 In chat.
Yeah, it's a memory ID.
**Liudmila Molkova** 14:21 Separate chat memory per user, I see, some form of partitioning.
So… Seems, everybody… Almost consistently.
calls the user is, user… Is this?
And… There is also user… Identity for all.
And these are two different… Thanks.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 15:17 Hmm.
**Liudmila Molkova** 15:18 And… There is urgent identity on behalf.
User and… There is user ID from UX perspective.
the… the… the… this two of friends… Are probably the same, but wait… oh, sorry.
These two friends are probably the same, but we don't really know.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 16:03 Yeah, I guess, mostly, usually, it's represent the first one, user.
Interacting with the session.
**Liudmila Molkova** 16:18 Yeah, I'm just trying to list different users.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 16:21 Hmm.
**Liudmila Molkova** 16:46 So, I… I think the… the concern… I'm just trying to understand my own concern about it.
Hmm. It still feels like it's so… Broad, and Definition we would put is something that Whatever the… Library or harness calls the user.
So a more specific one might look like GenAI, since it's the user associated with the session and the call session conversation.
But it's… It's very specific.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 17:44 Hmm.
**Liudmila Molkova** 17:45 It's very long.
And it's kind of weird that the user is a property of conversation.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 18:07 Yeah, but, this field, it's, it's important for some observability, plan for some, in some scenarios, the plan 4 wants to calculate the user's, token, yeah, consumption.
Something like that.
Yeah.
**Liudmila Molkova** 18:36 I'm just checking if, there is… user… I think I remember… user… Property in… Model responses.
Anyway, I'm thinking, like, I'd like to understand how else user… something like user is used in other places, like REST APIs for models. I think I saw something for OpenAI, maybe in the All ChatCompletions API.
I'm like, is it used… I think it was used… As some marker that you… I don't remember.
But, like, what… how many things would represent?
And… If we understand All the use cases, then… We could understand if we need the broad one, like this, or something more specific.
Yeah.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 20:10 Okay, okay, I, I can… Do some research, and provide more, Supportive case.
on my… PR?
**Liudmila Molkova** 20:28 Yeah, like, where else it's used, not just the Agentic, things.
But, I mean, you already have frameworks. I'm a bit curious to know what entropic reports for Claude, or, like, the… what harnesses report, and… If it's used in the… REST APIs for model providers.
And I, I… I understand the need, and I agree we need to decide what would happen, it's just a matter of which name we should use.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 21:10 Okay.
**Liudmila Molkova** 21:18 Damn.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 21:19 Thank you.
**Liudmila Molkova** 21:20 Thanks.
And the other one is also from USD for what chunk means in time.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 21:29 Hmm.
Yeah, I like my… Commas? Yeah, you can score… score top.
**Liudmila Molkova** 21:47 That's a good question.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 21:50 Yeah, we, come across this problem, today from our users.
Whether we should, include, retries.
to crowd in, F, if, TTF.
C.
**Liudmila Molkova** 22:17 I think we should, right? The… the operation, the inference span starts.
When the first try starts, And… for as long as it takes to get the first chunk, it's like the… it measures the user experience, right? How long as a user I wait for the first chunk, like, for… to start seeing the reply?
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 22:46 Okay.
Yeah, if, yeah, we can reach the… common, definition, yeah, maybe I can, send a PR to…
**Liudmila Molkova** 23:01 Nice.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 23:02 To explain this point, to clarify.
**Liudmila Molkova** 23:06 Yeah.
Thanks.
**Trask Stalnaker (Microsoft Corporation)** 23:10 Would we possibly… would we potentially have on Sunday a retry count on that, similar to the HTTP… like, I'm trying to think, what's the equivalent on the HTTP span?
I guess we don't have a…
