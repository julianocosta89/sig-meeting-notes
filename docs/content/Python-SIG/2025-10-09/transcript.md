SIG: Python SIG
Date: 2025-10-09
Duration: 40 minutes
Zoom Recording URL: https://zoom.us/rec/share/ZnPm_uCOiQJENaGrFNtcPdHBRvnDn16x_PNMhzCmmVwxY5kU473R8yrCSAyMHShA.iroZIDzT0wPHUaVX
============================================================

## Zoom Recording Transcript

**Riccardo Magliocchetti** 02:23 Hello?
**Nagkumar Arkalgud (Microsoft)** 02:28 Good morning, Ricardo.
**Aaron Abbott** 03:07 Hey everyone, how's it going?
**Dylan Russell** 03:12 Hello.
**Aaron Abbott** 03:22 Yeah, if people could add… Add yourselves to the attendees and any topics you have.
**Riccardo Magliocchetti** 04:28 Okay, so I think we can start. So welcome, everyone, to this week's Python SegWIC call.
And, as I was said, the fumes, Agor, please add yourself to the notes, and if you have any less than a minute topic, also feel free to add them.
Let me share… On the chat, the notes… Document?
Okay.
So, first topic is from me.
And a quick one, just a quick update on the log stabilization, the very slow log stabilization process we have in place.
And just a quick update, like, this week, like, we merged the free PRs, switching from event API to the log API in a few instrumentation.
And while reviewing this, I just did, like.
a quick search on GitHub on the OpenLelementary repo.
And found that we're using some SDK classes that we are going to remove, that we want to remove in their test.
But… They test against, like, an old OpenTelemetry version? Like, the… I think 1.20-something.
And so… Yeah, I think, like, I think they're one of our biggest users of this stuff.
And so… Yep.
Like, probably we can try to merge it, or maybe, like, we'll get in touch with them.
And… Yeah, if you have any opinion?
Or maybe we shouldn't care, I don't know.
**lechen** 06:37 Can you open up the PR?
Right.
So the other instrumentation besides OpenAI have made this change already, or… Or no.
**Riccardo Magliocchetti** 07:03 No, no, this is, like, another topic, like, the… the OpenAIA, the other instrumentation, just switched from the event API to using, like.
The log API directly, yeah.
**lechen** 07:17 Okay, nice, nice.
**Riccardo Magliocchetti** 07:19 This is, like, on top of that, I think this is the next PR we want to merge.
**lechen** 07:25 Yep.
**Aaron Abbott** 07:33 Yeah, has anybody been in touch with OpenTelemetry folks about this?
**lechen** 07:43 I've tried the, don't really respond. Is there still, like, a Gen AI… Work stream that's going on, or is that, like… Not going on anymore.
I haven't been…
**Aaron Abbott** 07:57 Still happening.
**lechen** 07:59 still happening?
**Aaron Abbott** 08:01 Yep, the… it was moved, like, maybe, like, 6 months ago to Tuesdays.
What time is it? I think it's Tuesdays at noon? Or sorry, Tuesdays at 11 Eastern.
**lechen** 08:15 Right.
**Aaron Abbott** 08:16 But yeah, we haven't really seen TraceLoop there, to be honest.
**Sergey Sergeev** 08:21 Yep.
So, Nier is on a vacation right now, so it's hard to get him.
**lechen** 08:28 Okay, cool.
I see.
**Aaron Abbott** 08:34 Yeah, I…
**lechen** 08:35 donate.
**Aaron Abbott** 08:36 Sorry, go ahead, ladies.
**lechen** 08:37 Excellent.
**Aaron Abbott** 08:38 I was just gonna say, can we open, like, an issue in their repo and just let them know what we're doing, maybe?
I'm guessing… Yeah, that would be decent.
Sorry. I'm sorry, I was gonna say, I'm guessing they're using the events because… That was the convention that we had.
And, and when they were kind of, participating a lot.
We had the separate events breach part in the message.
**lechen** 09:10 Yeah, I think… I think opening up an issue in… At least would… serve as a good due diligence. If not, we can try to attend the GenISA, but if TraceLoop is not showing up, then it's like… Opening up an issue would be the only direct way to get their attention.
**Sergey Sergeev** 09:31 Yeah, I don't want to open a big can of worms, but, probably we should implement the logs, the proper approach in Utogen AI.
And just, switch.
Just to propose a swoop to use that Retail Gen AI.
in their instrument fermentation.
Aaron, does it make sense?
**Aaron Abbott** 09:59 I mean, is it ready? Like, would it solve the… Immediate problem, kind of for this next release.
**Sergey Sergeev** 10:06 Next release, yeah.
Yo, let's… No, we don't have it merged, but we probably should merge, right?
**Aaron Abbott** 10:19 Yeah, I mean, there is, does… I mean, we could give it a shot, I don't know, Sergey, have you contributed in OpenLeetry? Do you have, like, a…
**Sergey Sergeev** 10:31 Nope. No.
**Aaron Abbott** 10:35 I don't know, Sergey, what do you think about, opening an issue over there, with kind of the context here that Ricardo shared about The breaking changes that we're making.
And, maybe pitching the… The util thing for them.
**Sergey Sergeev** 10:51 Yeah, I would love to trade, at least.
maybe… Yeah, I think if we are changing it to the proper way, and if We do it in Utilogen AI, so we have better chances just to… to do it once in VTO GenAI, and then to switch Open the A.
To using it.
**Aaron Abbott** 11:26 But it's a bunch of their instrumentations, right? It's not just OpenAI, is that right, Ricardo?
**Riccardo Magliocchetti** 11:33 Like, I think every… like, the issue with VPR Is that, when you… when you want to compare the, like, the exporter logs in test.
At the moment, you have to go through log data.
And log data is the class we are going to remove.
And so, like… I think that the code will still run. Maybe, like, we can just take a look at the… Advertest, so maybe it's…
**Aaron Abbott** 12:14 Okay, I mean, if it's just the tests, I'm definitely a bit less concerned.
**lechen** 12:23 Instead of, like, maybe we can find places in which they're using it, but, like.
Wouldn't just creating an issue just be a catch-all, not even just a courtesy thing, but it's also, like, they can…
**Riccardo Magliocchetti** 12:36 Evaluate whether or not it will break them or not.
Okay, so, like, share the… Like, link, like, our issue.
And see, this is our plan, okay.
**lechen** 12:55 Yeah.
**Dylan Russell** 13:00 Yeah, it looks like they're using events everywhere, too.
Which…
**lechen** 13:06 Right.
**Dylan Russell** 13:08 Yeah, we should probably point out we also eventually want to, like, remove those.
I was gonna ask if we wanted to put the deprecation warning.
submit that PR for events.
But… Yeah, maybe not, because they're using it everywhere, but… Yeah, I guess that's another thing to ask.
**lechen** 13:41 Yeah, I don't, yeah, I think we should come from the point of view of, like.
This is what we're doing.
Here's a heads up.
Or, like, if you ever upgraded in the latest.
Not sure if we should, kind of… ask them for permission whether it's okay or not. Unless if that's not what you're talking about, Dylan.
**Dylan Russell** 14:05 No, that makes sense, yeah. That's a better way to do it.
**lechen** 14:13 Yeah, and whether we kind of onboard them onto using utils or not, can be separate from that, I think. I think the workstream to stabilize logs is… Like, we don't want to be blocked on… We don't want to be blocked on that.
**Sergey Sergeev** 14:30 Yeah, maybe we should offer an easier way for them to solve this problem by using UTL. If it doesn't let it solve easier, then it invalidates the whole idea of UTIO.
I think we should do it, but it's not… Yeah, boy care, for sure.
**lechen** 14:52 Yeah, and it could be, like, that they take a dependency on it, but I think we have to, inform them, and they should recognize and also evaluate the scope of how much this would break them first, and then come back to us and be like, hey, like.
do you have any solutions for us? Maybe, you know, and then maybe we could close that, so…
**Sergey Sergeev** 15:12 Yeah, makes sense.
**Riccardo Magliocchetti** 15:22 Okay, thank you.
And by the way, like, probably, like, if you know any other users of… the event API… Let me select… A good moment to… Yeah. To share, so just add to the… to the notes.
So we are aware of… of… Places where we can break things.
**lechen** 15:49 So, just for context, is this the first Big breakage? Or has there already been precedence?
In past releases.
**Riccardo Magliocchetti** 16:02 No, I think this will be the first breakage.
**lechen** 16:06 Okay.
So, I think we'll have to be careful with the messaging.
And the… I guess… informing users.
But it's okay, it's like, we gotta pull the Band-Aid off eventually, so…
**Dylan Russell** 16:31 Right. So, for events, there's… The PR that just adds the deprecation warning.
Which we wanted to do before we actually, like, removed it.
And…
**lechen** 16:43 Yep.
**Dylan Russell** 16:44 I think pretty soon we'll have, like, all the event stuff removed from Contrib.
So I think we could merge that PR, just adding, like, the deprecation warning, once that… once that's all sorted out.
**lechen** 17:06 Yeah, I think that makes sense.
I haven't taken a closely looked at Hector's PR, but it's simply removing log data, correct?
**Hector Hernandez** 17:20 Yeah, there's two of them, but, No, this is… yeah, I have way more changes. Started as that, but I think I might in, like, the read, write, credible, log records, readable only, that kind of stuff as well.
**lechen** 17:38 - is that from, like, Lyudmilla's suggestions, or… Sorry, I haven't been involved in this for a while.
**Hector Hernandez** 17:44 No, we discussed this in a SEC meeting, like, a few weeks ago.
**lechen** 17:50 Got it, got it.
And remind me again, is log data part of our public API?
Like… People take dependencies on it, or… What is the blast radius of this?
**Hector Hernandez** 18:06 I think this is affecting, instrumentations, only in theory. I'm not sure, to be honest.
**lechen** 18:14 Right.
**Riccardo Magliocchetti** 18:18 Well, changes here are only in the SDK.
**lechen** 18:23 Yeah.
**Riccardo Magliocchetti** 18:24 And… yeah, usually, like, it's in test, because, again, like, log data is the stuff you get when you read the…
**lechen** 18:33 Right.
**Riccardo Magliocchetti** 18:35 Like, maybe we can have an example.
**lechen** 18:40 Like, you create these when you're just evaluating whether or not the collected record matches what you expect, right?
**Riccardo Magliocchetti** 18:49 Yeah.
**lechen** 18:51 Right, so, like, in a way, it's like…
**Riccardo Magliocchetti** 18:54 Nope.
**lechen** 18:54 In terms of actual functionality, Theoretically, people shouldn't be using this.
Like, it's not document or public API, I guess.
**Riccardo Magliocchetti** 19:05 Yeah, but, like, usually people, like, asserting stuff.
We want to get the log record and need to go through log data, but it's… What the, yeah, makes sense. Yeah.
**lechen** 19:20 Yeah, and then, because… It is… it is common, I can see people doing that, because, like, you have to… To inspect, like, the underlying data, you have to access log data?
But it's… it's not as dangerous as, like.
You know, like, removing log record, or, like, span, or something like that.
But yeah, I do agree that, we… upon this release, we'll probably get some complaints, but I think we can kind of rest easy knowing that, like, functionality shouldn't break, theoretically.
Yeah, but I guess we'll just, have some more reviewers for this PR, and try to get this out.
**Riccardo Magliocchetti** 20:12 Yep.
**lechen** 20:17 And, once we… Once we merge it, we can then bring up the… I'm creating an issue and open that elementary to, to warn them.
**Riccardo Magliocchetti** 20:37 Yeah, makes sense.
Okay, thank you.
So, I think we can move on to the next topic.
**Nagkumar Arkalgud (Microsoft)** 21:03 Hey, bro.
I'm not Kumar from Microsoft.
So, this is the second part.
of… The PRs that we came up with last week.
One of the feedback items was that the PR's too big, it does everything at once, let's break it up into bare bones, add functionality slowly so it's easier to review.
So we got the bare bones merged in, and this is the second one which adds the traces and spans. This still doesn't do input or output messages. I'm having a separate PR for that, just to keep things easy and simple to review.
So once… Like, would really appreciate people taking a look at this.
I have some very basic samples, examples listed.
Which you can run and have a Notel collector running to see how the traces look like.
So… So far, we've… we've been capturing everything that has been listed, or, like.
Everything that is mandatory and a few of the optional ones.
I would love some feedback on this, so…
**lechen** 22:20 Hey, yeah, Nakmar, thanks a lot for splitting up into smaller PRs. It's, like, way easier to… to review this. I left some comments already, but overall looks pretty good. I just need to go over the actual attributes and, like, verify them.
I think the only outstanding comment or question I have, and I don't know whether it's right or not, but it's regarding the, the pattern for creating a server span on trace start.
Just for context for everyone who hasn't taken a look at this yet, I believe For OpenAI agents, when a trace is started, a… a overarching parent span is created so that all, like.
Proceeding tool calls and agent operations fall under this, like, kind of parent Yeah, you can see here, Natkumar outlined it pretty well.
This is similar to the pattern that we have for other… even, like, HTTP instrumentations and everything, it's just that we don't have this specifically… spec'd out, which is fine. Does anybody have any experience regarding this in the context of Gen AI libraries?
**Aaron Abbott** 23:41 This is for Asian communication?
**lechen** 23:45 Sorry, can you say that again, Aaron?
**Aaron Abbott** 23:46 Yeah, what does the overall span represent? Is it agent invocation?
**Nagkumar Arkalgud (Microsoft)** 23:54 Yes, it is on the TraceStart agent, when an agent is involved, yes.
**Aaron Abbott** 23:59 Okay. I mean, I just shared in chat, but I think we do have a convention for that.
**lechen** 24:09 Is there not a separate stand that's created, Nakumar, for invocation of… Agent?
Or is that actually called on TraceStart? I'm not too familiar with the inner workings of OpenAI agents.
**Nagkumar Arkalgud (Microsoft)** 24:24 So, it's called Invoke Agent, followed by the name of the agent. That's going to be the client's plan.
But for an overarching workflow, in case there are, like, multiple agents involved, dope.
That would probably add, like, an… a parent for all of the agents involved? Like, all of the agents, invoke agents.
will have a common parent, so that… that was the idea. Invoke Agent is already implemented, so we already have Invoke Agent, which puts in the LLM span, LLM tool call spans, and all those after that.
**lechen** 25:03 Corporate.
**Nagkumar Arkalgud (Microsoft)** 25:04 But in case of multi-agents, I can spin up, write a few more samples, and, you know, showcasing things like handing off between multiple agents, and how do we, you know, group all those spams.
From two different agents, or more than two agents under one umbrella.
**Aaron Abbott** 25:27 Okay, I can take a look. I… I… I'm not sure if we have something like this in conventions. I mean, some people propose things like workflow and stuff like that, but, to me, I guess I'm kind of confused how the entry point is not, like, a single agent. Like, do you make a request to invoke multiple agents, or is there not a root agent?
**Nagkumar Arkalgud (Microsoft)** 25:50 So let's say there is one agent which invokes other agents, but it does it so in a hand-off-like pattern, wherein the control never goes back to the first agent which is involved.
So, it's gonna be, like, Agent 1 calls Agent 2 and 3, but never goes back to Agent 1 to close the loop. Like, Agent 3 would be the last message.
**Aaron Abbott** 26:15 Gotcha.
Yeah, I think we have something similar in, like, Google ADK instrumentation, but… that doesn't live in Contrib, the actual framework is, like, natively instrumented. So I think it surrounds things with, like, this invocation span.
And then there's the invoke agent underneath. It also has this concept of handoff.
**Nagkumar Arkalgud (Microsoft)** 26:36 Where they get…
**Aaron Abbott** 26:37 The spins get kind of flattened out, but, I would recommend… I mean, I can take a look, or send you a screenshot of what what the traces look like from ADK, but, do you already join the LMSIG on Tuesdays?
**Nagkumar Arkalgud (Microsoft)** 26:53 I do not. I can join on Tuesday, but I have taken a look at ADK, and it's pretty similar to what ADK does.
But, I mean, I'm not 100% sure that it's, like, the exact same thing.
**Aaron Abbott** 27:09 Okay. Yeah.
**Sergey Sergeev** 27:11 Now it's, basically as a workflow, as a top, Top, top type, being discussed, I think we really need to figure out what will be that connecting attribute if it's not trace ID.
Which, which is currently the only thing which propagates, cross our PCs.
So we will need, to figure out what will be that connecting attribute for that, Multi-agent, distributed workflow.
And, make sure that it also propagates across RPC.
I think it's quite… Embiq.
**Aaron Abbott** 27:54 You can…
**lechen** 27:55 Is this currently being talked about, Sergey, or is this, like, we want to drive this conversation?
**Sergey Sergeev** 28:01 Yeah, we definitely want to derive this conversation by the group, especially if they have use case.
**lechen** 28:11 Makes sense.
I think just to move this forward, like, that's the only kind of outstanding part of the PR, Nakamar, that, like, I'm not super… Sure. If we want to just move things along, like, feel free to… Omit that part, or, like, add a to-do, until we, kind of.
Get consensus, in the community regarding what we want to do for the root span.
**Nagkumar Arkalgud (Microsoft)** 28:40 Sounds good. I will, make that add a to-do and replace that, and follow up with a separate PR for it.
**lechen** 28:49 Awesome, thanks.
**Aaron Abbott** 28:52 Yep, that sounds good to me. I definitely recommend joining the SEG. I'm digging up the information, but it's, Tuesdays… Tuesdays at, 12 Eastern.
I'll add a link to the notes doc, though, but we usually discuss both, like, instrumentation PRs and the semantic conventions, so… seems like a good topic.
**Nagkumar Arkalgud (Microsoft)** 29:15 Awesome.
**lechen** 29:16 interruption.
Yeah.
**Aaron Abbott** 29:22 Really?
**Nagkumar Arkalgud (Microsoft)** 29:23 Cool. The next one's another PR for me. It's to update the line chain tracers, to follow the latest ones. Pretty similar to what we have, there is a a 3.9 gate, which is… bugging me, but I'll get through that. There is, like, general feedback on what we have to do, or, like… Any other changes, because it's just doing the same.
Same stuff that we have, like… How to be updating it to the latest spec?
Getting more data for, line chain stuff.
Line chain, line graph.
All of those packages.
**Sergey Sergeev** 30:06 Yeah, I can start a thread… a thread in, Hotel Gen AI Instrumentation's work channel, I think I added you over there, yesterday. But, Redima from, Splunk team.
She… she… she's starting to work on migrating that link chain to using Utilogen AI.
Maybe you can meet and brainstorm.
if… It makes sense, to do at this.
stage, because it should only have OM and vacation, which is, in… We do with NA over in there.
**Nagkumar Arkalgud (Microsoft)** 30:52 Awesome. Sounds good. Yeah, feel free to tag person on my PI.
So we can brainstorm together.
**Riccardo Magliocchetti** 31:11 Okay, thank you.
Yeah, last topic is from Kif.
**Keith Decker** 31:26 Yeah, just a reminder for… reviews on this. I know you just started looking at that again, Aaron. You left a comment. I got that fixed. Wow.
All the other topics were up here, so if you want to just take a look at that one other comment, and then I think the last test is just failing on that flaky thing which you're tracking somewhere else, so…
**Aaron Abbott** 31:46 Okay, yeah, I'm taking another look as well, had kind of, like, a… General question around the, like, context manager behavior.
I don't know if you want to spend a couple minutes chatting now, but I'm also… I have some, like, Pending review, comments to submit, someone can.
**Keith Decker** 32:06 Oh, okay.
**Aaron Abbott** 32:07 I apologize for the delay, I know it's been open for a really long time.
But yeah, so basically, I guess my question was, if you can go to the files changed, Ricardo.
If you just search for, like, the context miniature decorator, I think it'll come up.
Yeah.
A little bit below this.
Yeah, right here.
So, this context manager, it's kind of, similar to the usepan.
context manager we already have, which I'm… I'll put in a link as I comment on this, but the, like, exception behavior is slightly different, if I understand right.
So we're kind of, like, rewrapping the exception See you later We're kind of rewrapping the exception, and the behavior might be kind of different, but also it's just… a little bit… duplicating it. I know that we have kind of extra hooks Here, but, Yeah, have you had a look at the YouSpend decorator?
**Keith Decker** 33:24 Not off the top of my head, I'll have to go look at that.
So you want it to operate more like the usepan, versus…
**Aaron Abbott** 33:34 Yeah, or just if there's a way to reuse it.
**Keith Decker** 33:37 Okay.
**Aaron Abbott** 33:38 So yeah, because basically it already catches exceptions and spins.
But it doesn't have, you know, kind of, like, general hooks for the lifecycle, so you'd have to… Probably wrap it anyway.
But I see that, like, start LLM, fill LLM, stop LLM also have the context attached and detach, so you could probably refactor that part into just using that decorator.
But yeah, that's pretty much it, and then there was, like, a lot of, star star keyword args, any… arguments, that was my other kind of question.
If… so, like, right there on 170.
and the constructor to the telemetry handler thing, I was wondering if we could… just, pin down the arguments. Was there any specific reason to do this instead?
**Keith Decker** 34:29 I think that started with… When we were having metrics and, Logging.
and the tracer being handed into it, and then as we downsized this, it all just kind of fell out, so I guess for this PR, we can button this down to just being…
**Aaron Abbott** 34:48 Pop being the few things it needed.
Okay, cool. I will drop those comments, otherwise… Yeah, thank you.
**Keith Decker** 34:56 Okay, I will get back to you ASAP on those.
**Aaron Abbott** 34:59 Okay, cool.
**Riccardo Magliocchetti** 35:13 Okay… This was the last topic for today.
Any… Last minute topic, or comment, or something you want to discuss?
Okay, so thank you, everyone.
And… See you next time.
Bye. Thank you.
**Aaron Abbott** 35:43 Thank you, everyone.
