SIG: LLM Semantic Convention WG
Date: 2025-11-25
Duration: 29 minutes
Zoom Recording URL: https://zoom.us/rec/share/ycsFGTotdreth2HBDwaBo2fbq6QUks8kpnL41I5onTRSkfXjBqvfn8gNMVuRfF5z.ih9E9DRNZ3Ht2tnm
============================================================

## Zoom Recording Transcript

**Aaron Abbott** 02:20 Hello everyone, how's it going?
**Bruno** 02:24 Hello?
**Aaron Abbott** 03:57 I don't know if, Lynn Mill's gonna join.
sheep.
Put her name in the agenda, but, We could probably just get started.
**Alex Hall** 04:07 She posted in Slack that she's… that she won't.
**Aaron Abbott** 04:11 Oh, okay, cool.
Let me share my screen then, give me a sec.
Okay, you know, let's start with the triage.
Okay, got a couple new… Shoes.
Keith, do you wanna say anything about this?
Briefly, or do you want to chat more about it later on?
**Keith Decker** 04:50 I think this one, we were waiting on the workflow and task group that Luke Miller wanted to set up.
And then we're also going to… Investigate other frameworks and make sure that this isn't too lane graph specific.
Okay. It's just kind of pending some of those.
**Aaron Abbott** 05:12 Okay.
I'm inclined to mark it accepted then.
**Keith Decker** 05:19 Okay.
**Aaron Abbott** 05:20 Sounds like we have… We do this… Okay, I think that will move it automatically.
Somebody let me know if that's not right.
Okay, this one's from Ludmilla… This one didn't move, so I guess it doesn't move automatically.
Tools should arguments be a template.
Okay.
I'm gonna move this to… To do?
Probably do the same with this one.
Okay, yeah, I solved this one.
Not sure if you're… if Brian's here? I don't think so.
Yeah, I think this is basically proposing a couple of new metrics.
Which would be, like, we already have a server time to first token.
But this is proposing adding a client histogram for… Time to first token, as seen from the client.
How many tokens per second were generated during generation?
Yeah, and they seem to all be kind of based around the idea that the streaming is… Not buffering, and it's giving you stuff immediately.
So I, I know… I don't have anything against these, so I'm inclined to mark it accepted, but yeah.
Okay, 20 hours ago with Milla. How to read params end result.
Yeah, I think we chatted about this a bit last week. This is just creating an issue for it.
Yeah, I'll mark this one accepted.
Okay, cool. That's it for the triage.
So Lamila added a couple… Of agenda items, but otherwise, there's not much.
Add an agent called the Calendar Community Repo.
I think this is just updating the docs.
Okay, that's great.
And then the other one was… the MCPPR… Yeah, so I think… I think Linvilla addressed a lot of comments here.
I'm gonna take another look and hopefully approve this. I feel like… there's been a ton of feedback, and we have pretty good agreement from, like, MCP maintainers and such.
There was… there was, like, one comment down here about, what to do.
I think that this tool comment is, we kind of don't usually, like, give a recommendation on instrumenting one or the other, but I would say just instrument both, like… the MCP client is probably… Gonna be underneath the tool, but the orchestration framework would be, like, the thing emitting this invoke tool in the first place.
And there's another question about, like.
when you use the HTTP transport.
But we also include the trace parent and the meta within the JSON RPC.
you could end up potentially with different, like, conflicting values for TraceParent.
I think it's a good point, but… Probably not super unique to Gen AI, like, I think… You could have this situation for other things, like we have, Messaging semantic conventions for something like, Kafka or whatever, they could have this problem.
Or generally for any, like, embedded protocols, I think.
Loon mentioned it could… A bunch of them, somewhere.
**Alex Hall** 10:04 I don't really understand how you would end up with conflicting values.
**Aaron Abbott** 10:09 Yeah, I think the idea is, like, if you generate the MCP.
**Alex Hall** 10:14 Meta?
**Aaron Abbott** 10:15 before you initiate an HTTP post, for example.
Then the meta would be whatever the parent span was when you generated it.
But then, once the HTTP session is initiated, if you have HTTPX instrumentation, for example, you would get a new parent span.
Which would then put… that… that span into the trace parent for the actual HTTP header.
**Alex Hall** 10:50 But if you… So you're saying, like, that the order of… the nesting spans could be on the outermost level, you have, like, the MCP span with one transparent, and then you have the HTTP Client span.
And then maybe the HTTP service ban and the MCP service ban.
**Aaron Abbott** 11:12 True.
**Alex Hall** 11:14 time you get to the MCP service band, it tries to extract one trace parent from the MCP Meta.
But there's already an active span That was extracted from… or that came from the HTTP server span. Surely you just ignore the trace parent when there's already an active span?
**Aaron Abbott** 11:35 Oh, interesting.
Yeah, I don't know, I mean, I feel like in the case of MCP, it would probably make sense to override it.
With the one from Meta, right?
I don't know, I mean, do you think this is worth, like, specifying? I feel like it's kind of… Maybe an implementation detail?
**Alex Hall** 12:28 I mean, the other thing is just the HTTPX… Something about HTTPX, just the HTTP stuff.
It is a myths.
Well, maybe it differs in other languages.
Like, the way that the spans happen with the streaming, or events, or whatever it is.
**Aaron Abbott** 12:48 Yeah.
**Alex Hall** 12:49 needs to.
Normal context propagation not even working.
I'm just looking at what happens when it extracts context. It doesn't look like it actually pays any attention to existing context.
**Aaron Abbott** 13:06 Yeah, I think we generally just overwrite it, I mean, Alex, I think you've… you're probably one of the people who's actually implemented an instrumentation for MCP.
So you probably have a lot of context here, Like, is it possible that the… the MCP… level, like, JSON RBC level… Trace parent would be… More specific, like, if you're reusing, a single request with SSE. It seems like you're even allowed to have, messages from different sessions returned on like, an SSC stream from a different one, if I'm reading the MCP spec correctly.
**Alex Hall** 14:10 I… I can check what hap- And what I worry about is that whatever happens in Python is not necessarily a good representation of what happens in other languages.
It is harder for me to check.
Well, I don't know how to check what happens in other languages.
**Aaron Abbott** 14:25 Okay.
I remember there were a lot of issues with context that you had, but were those… were those more around, like, the async paradigm used in the MCP client library, or around, like, the actual protocol?
**Alex Hall** 14:41 I think they were more about the former, the async.
**Aaron Abbott** 14:45 When it does things.
Okay, I mean, in my opinion, I don't think it should block this PR, necessarily.
Like, we should do some prototypes, and I think we have a couple, there's, like, from Open Inference, I think there's one, there's probably OpenAllimetry, etc.
But yeah, they're all Python, most likely.
Oh, yeah.
Well, that's all I had on this one. I think it's mostly just a call for reviews, so please take a look.
If you have any thoughts on this comment specifically, yeah, please add… add to review. But, Yep, that's all I had here, Anyone… anyone else have any thoughts on MCP, or should we go on?
Okay.
Alright, I think this is… oh, we got more coming in, but Keith, do you want to, talk about this? Oh, yeah, yeah, yeah, you've mentioned this a couple times.
**Keith Decker** 16:05 Yep, just, just our weekly reminder for a review.
It's a pretty small one. Most of the line changes are in test files, and it's just adding some metrics.
Token and duration.
**Aaron Abbott** 16:19 And these are the SEMCOMF metrics, right?
**Keith Decker** 16:22 Yes.
**Aaron Abbott** 16:23 Okay.
Cool. I'm inclined to just merge it since Ludmill reviewed, but, I'll try to take a look.
as well.
**Keith Decker** 16:32 Sounds good.
**Aaron Abbott** 16:33 Appreciate it. Sorry for the delays there.
Okay, josh, I see you adding this… item, do you wanna…
**Josh Winerman** 16:49 Yeah, so, well, I… let's see, it went a few weeks where I sort of avoided it, but Liud Mila and I had had a few conversations about, and I think you… you might be a little looped in, Aaron, about, retrievals as a type in Gen AI, as a span type in Gen AI, and it seems like Leo Mila and, the Cisco group sort of made an agreement that it's okay to put the type in the DB space, so now I'm semi-wondering, do I have to… is there another group in DB that I should be bringing this to as well for SimCon? Or.
**Aaron Abbott** 17:26 I think.
I think the automation here will, like, assign the correct owners.
I… I'm trying to remember if there is a DB… Working groups still going on.
Lumila's definitely involved with that, so I think she would be a good contact, but… Yeah, I don't see… Does anybody know if we're still having DB SimConv, like, working group meetings?
Yeah, I don't see it on the calendar, Actually, this… the earlier topic with updating the community repo, you can check there if there's a call, but generally, I think the automation will assign the right people to review this with, like, the code owners and such.
So yeah, this is probably still mostly the right audience.
**Josh Winerman** 18:23 Okay, yeah, so, otherwise I'm just looking for review. It's a lot of what Liamla and the… I and the group had talked about or agreed upon before, so not too many changes.
**Aaron Abbott** 18:38 Okay.
Cool, yep, I will… I don't honestly have a ton of context on retrieval. I'm wondering if anybody from Cisco would want to take a look at this.
Especially since you were going back and forth, but… Yeah, makes sense. Please take a look.
**Josh Winerman** 19:01 Thanks, Aaron.
**Aaron Abbott** 19:02 Yep.
**Surya Teja** 19:07 Hey, Adam, I have a small doubt.
**Aaron Abbott** 19:10 Yep.
**Surya Teja** 19:12 my, anthropic, issue that I raised, it was mentioned that let's immediately type in. I'm not sure what immediately type in means in this context, so can you please elaborate more on that?
**Aaron Abbott** 19:26 Say it one more time, immediately what?
**Surya Teja** 19:28 Immediately type in.
on the issue that I raised for adding the library.
**Aaron Abbott** 19:34 Related to Claude.
Do you have the issue number? Can you stick it in the.
**Surya Teja** 19:40 Yeah.
What up? Sure, sure, sure.
**Aaron Abbott** 20:31 Is it this one?
**Surya Teja** 20:34 Yeah, I… sorry, I just pasted it at the wrong one.
But it… it's the one ending with.
**Aaron Abbott** 20:43 This one?
Oh, am I sharing?
**Surya Teja** 20:46 2949.
**Aaron Abbott** 20:48 Yeah.
**Surya Teja** 20:49 Yeah, yeah, yeah, Thune and Fundham, yeah.
**Aaron Abbott** 20:51 Okay, and your question was about this typing?
**Surya Teja** 20:53 Yeah, yeah, let's…
**Aaron Abbott** 20:55 Yeah, here I can… sorry about that. We really need to update the docs, and I would like to make this, like, opt-out for any new packages, but I'm not sure. So basically, there's just, like, a pyrite config here.
I don't know if you're familiar with it, but it basically entails just adding your package to this include.
When you add, like, the boilerplate or whatever, so that…
**Surya Teja** 21:18 Yeah.
**Aaron Abbott** 21:19 It'll run.
**Surya Teja** 21:20 I… I was creating the boilerplate, based on your, pull request you made for Vertex AI, so I was including that, but I just want to ensure that what type in means, so…
**Aaron Abbott** 21:34 Yeah, we… we use…
**Surya Teja** 21:38 pyrite in CI, so it's mostly just opting into this, yeah.
**Aaron Abbott** 21:43 And there's a docs target you can run locally, I think it's docs-eat. Yeah. Yeah.
**Surya Teja** 21:49 Yeah, makes sense. So, another note, since we're on the context, I saw one of your PRs that you made for, the Vertex AI, and I was closely following that for setting up the boilerplate. Okay. Because the comment over there says that this can be used as a template for building the base. Is that still the norm, or is there any other thing that was introduced?
**Aaron Abbott** 22:16 No. I think that should be… A good example, still.
**Surya Teja** 22:20 Yeah, cool. Thanks, Aaron.
**Aaron Abbott** 22:23 Okay, cool, I just dropped a comment on here also, so… Alright.
That's the end of the agenda. Anybody else have any comments? Topics?
**Alex Hall** 22:40 I'll just say, I took a look now, if I have… both HTTPX and… more HTTP and MCP hotel propagation.
Well, whatever I do, If there's HTTP propagation, the trace just looks like a mess, it doesn't work properly.
But it's definitely better with the MCP propagation on hand, as far as I can tell, overriding.
you want.
**Aaron Abbott** 23:10 Okay, I see.
And is that related to, like, the, the transport, or the… the code.
**Alex Hall** 23:19 It's hard to say.
**Aaron Abbott** 23:21 Okay.
Yeah, I found the MCP… I know they just, like, there's a new… I think they call it Streammable HTTP.
Transport? Is that this one, or, like, the old SSC one?
**Alex Hall** 23:37 That's what it was in this case.
**Aaron Abbott** 23:39 Okay.
Yeah, so I think… Like, we have lots of, prototypes out in the wild.
You know, usually we want a prototype of semantic conventions, like this MCPPR, it would be great to have, like, a prototype of it, so… I think at one point, somebody… Somebody raised an issue for contributing an MCP instrumentation into, like, OTELPython Contrib.
Don't think it really moved forward, though, but… Yeah, I think… Maybe just for the specific comment, like, yeah, it seems like we have to override HTTP, it's just gonna be a mess otherwise.
But yeah.
Thanks for checking.
Okay.
Okay, great, I think that's it for today.
Thank y'all for joining.
**Alex Hall** 24:45 Alright, cheers.
**Keith Decker** 24:46 Thanks, buddy.
**Aaron Abbott** 24:47 Little.
**Bruno** 24:48 Yes.
