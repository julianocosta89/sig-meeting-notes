SIG: LLM Semantic Convention WG
Date: 2025-11-11
Duration: 23 minutes
============================================================

## Zoom Recording Transcript

**Aaron Abbott** 07:31 Everyone, they going?
So I think it's KubeCon week, it looks like we don't have an agenda. Could wait a couple minutes, but if… I'll put together, like, the,
Agenda boilerplate, and maybe if there's no items, we can call it a little early.
Alright, if nobody has anything, I guess… Probably just, stop there.
**Steve Liu** 08:36 Sorry, hey, Aaron. I actually have a PR for adding new, GenAI attributes, like, info attributes that I was wondering if I can get maintained to look at.
**Aaron Abbott** 08:47 Sure, do you mind adding it?
To the agenda here, just so we can find it.
**Steve Liu** 08:53 Sure,
Just, like, down… okay, I see, I see.
**Aaron Abbott** 09:01 Yeah, it's just the Google Doc,
Did you… did you want to talk about it at all, or you just kind of need a review?
**Steve Liu** 09:22 Yeah, I guess I can give a…
Like, brief summary of, like, these attributes.
**Aaron Abbott** 09:30 Okay, do you want to share your screen?
**Steve Liu** 09:34 Yeah, sure.
**Aaron Abbott** 09:35 Okay.
**Steve Liu** 09:36 Oh, I think, oh, okay.
Can you see this?
**Aaron Abbott** 09:46 Yep, I can see it.
**Steve Liu** 09:48 Okay, cool, thank you. Yeah, so basically,
just a… I guess, sort of a context,
So AWS released, this service called Agent Core, Bedrock Agent Core, which lets you build your own, like.
agents on… hosted on, like, AWS platforms.
And,
I was thinking we should expand some of the genera attributes to encompass, like, some of the infrastructure that you can…
Add to these, survey agents?
Pretty much it. But also, I also wanted to add, like, some additional, like, AWS attributes for each of these AgentPore services, and…
Yeah, mostly I kind of just want to take a look at these Gen AI, these new Gen AI attributes,
The AWS ones are a little bit less priority.
**Aaron Abbott** 10:35 Okay, yeah, we can… we can take a look. I'd probably recommend splitting… splitting it into a separate PR for the non-AWS ones versus the AWS ones.
But yeah, we could, we could go over it.
**Steve Liu** 10:49 Sure, yes, I think I got an initial review from…
I'm not sure if he's a maintainer or not from this person.
And…
So apparently, I'm not entirely new to… I'm not entirely, like, too familiar with some of these concepts, but…
This, code interpreter, browser, memory, runtime, gateway, they're all, I guess, general Gen AI concepts.
And…
So basically, just what each of these represent is that, when an agent, like, invokes any of these,
Let's see…
Yeah, when an agent invokes any of these.
I guess, infra to help it…
execute, like, a prompt. The basic idea is we can capture, like, some sort of identification for that request from the agent.
And just, log in to the spans.
I think it was the general idea.
**Aaron Abbott** 11:54 Okay. Have you seen…
So there's two things that we've been talking about a couple weeks, but there's a session as part of, like, the real user monitoring SIG,
In OTEL already, which is… which would be, like, the browser session, as far as I understand.
And then we also have, like, a conversation ID.
Which is GenAI-specific. Have you seen either of those ones already?
**Steve Liu** 12:16 I'm aware of the conversation ID, I'm not aware of the, the session one, I guess.
**Aaron Abbott** 12:21 Okay.
Yeah, maybe I can… I can leave a review on here and add a link to it.
But yeah, I think when we… we've talked about this a couple times,
In the… in the context of, like.
if those are… if the… those two that I mentioned were the same or not.
But yeah, I would probably…
It sounds like that's pretty much the same as the browser ID you have here, right?
**Steve Liu** 12:46 I see.
**Aaron Abbott** 12:47 So, these can all be lumped in, I guess, the…
**Steve Liu** 12:52 Or, sorry, the session attribute, essentially.
**Aaron Abbott** 12:55 Well, I mean, some of them, right? But I'm curious about, like, a code interpreter ID, which… what is that supposed to be?
**Steve Liu** 13:06 Yeah, I guess the same thing as browser, it's sort of, kind of, like, browser, I think, is… just allows the agent to use the internet, or use some sort of, like, web browser to
These searches, and information.
For Code Interpreter, it… I think the agent can execute… actually write and execute code to…
Also help with a task?
I'm just thinking that they probably fall in the same category.
**Aaron Abbott** 13:34 Is… is the code interpreter…
part of Agent Core, or is it just, like, part of, part of Bedrock, more generally, like a server-side tool kind of thing?
**Steve Liu** 13:46 I think as far as I was aware, like, initially, I thought it was an agent core concept, but…
Apparently, this code interpreter thing is a just general, like, Gen AI…
**Aaron Abbott** 13:55 Yep.
**Steve Liu** 13:56 Yeah.
**Aaron Abbott** 13:56 Yeah, so there's an issue somewhere for server-side tools,
this, at least I can speak for Gemini, which I'm familiar with, it does not have browser right now as a server-side tool, but there is
code interpreters, so you can ask it, you know, to run arbitrary Python code. But… But the…
There… I don't know if there was a proposal for that one, but I will link you…
I'll link you the issue, at least.
**Steve Liu** 14:28 Okay, sure, thank you.
**Aaron Abbott** 14:29 Yeah, in any event, like, Was this supposed to be… I can review the PR.
I'm a little confused how…
Like, were these just attached to the agent spans? Like, what do you do with these attributes in this PR?
**Steve Liu** 14:43 Yeah, essentially, like, if an agent, internally, like, invokes one of these, like, tools, my idea was it would emit a client span.
Represents the outgoing call.
**Aaron Abbott** 14:57 Right, yeah.
Yeah, so in the context of, like, the server-side spins, sorry, the server-side tools, it's all done usually as part of a single LLM call.
At least, at least for Gemini, so somebody else, please keep me honest. But, so it would be very difficult to, to do a span for that. I'm not sure about, for Agent Core. So, I was wondering, do you have, like, a prototype of instrumentation for these attributes at all?
**Steve Liu** 15:25 Yes,
So, in AWS, what we were doing is, when there's an outgoing, like, client call to any of the Agent Core services, using the AWS SDK.
The idea is, like, we were instrument, like,
Like, if it was to call the browser tool, like, using database SDK, then we just capture the ID for that outgoing, like, call, essentially.
**Aaron Abbott** 15:54 Okay, okay, I see. Yeah, if you could add, like, some… some of that context to the…
To the PR description.
And maybe, like, a link to the instrumentation prototypes,
Or, like, if you have it committed in some AWS repo or something like that, that would be,
Super helpful, and maybe even, like, a screenshot or something of,
How this looks, if you're able to.
Yeah.
But yeah, I kind of see what you're saying now, that it's more… more like these are specific,
services as part of Agent Core, so we're proposing, kind of, new top-level spins for those.
**Steve Liu** 16:34 Right, right. Yeah, yeah, I guess I'm not sure how other services would, like…
utilize, these attributes of sensor. Like, I'm unfamiliar with how Agent Core would work, but yeah, again, like.
Not until it's, how the other, like, services, or, like, how other,
PS Services would use these attributes.
**Aaron Abbott** 16:55 Okay.
Yeah. Yeah, so I think,
I'll take a look, but if you could please… maybe let's split the AWS one separate from the generic ones, and
If you could link to some of the instrumentation.
That'd be super helpful.
**Steve Liu** 17:11 Yep, that works. Thank you.
**Aaron Abbott** 17:13 Okay.
Cool, that's all we had, so…
Oh, instrumentation around Claude, agent SDK. Yeah.
**Surya Teja** 17:24 Hi, I was actually looking at the Python contributions, and I saw that you have an SDK for OpenAI and Google and Bedrock, but I was curious to see if there is an appetite
for adding instrumentation for Clots Agent SDK, because they released a new SDK, and I'm not sure if…
They have spans or anything around it in our Python contribution repository.
if there is an appetite, I can open a draft PR and get some…
Co-prototype ready, so that you guys can take a look and.
**Aaron Abbott** 18:02 I think, I think there's one for Cohere already, or at least there was an issue, at least, for it. There might have been a boilerplate.
Was that you?
**Surya Teja** 18:11 That… oh, that wasn't me. I don't know who opened it up, but I was not sure if there was something for Cohere, but yeah.
**Aaron Abbott** 18:19 Yes, I think.
So there's… I'll put it in the doc here, but there is,
an issue here, I think Leighton added some boilerplate for it… already?
So I think that one's pretty much open.
Oh, interesting.
Yeah, I don't know what the state of that is, actually. Maybe just, reply on that issue and see if,
see if Leighton, who filed it, will get back to you, but… Yeah. I don't think we have anything for Claude Agent SDK, either.
Could you Maybe file an issue.
**Surya Teja** 19:03 Yeah, sure.
**Aaron Abbott** 19:04 Yeah. Sure.
**Surya Teja** 19:05 Yeah, I'm not from Anthropic, but I was… I use a lot of Cloud SDK for our internal apps and agents, so I was just seeing if there is an appetite or not, so I'm concluding that there is appetite, and I'll open an issue, and… should I link a prototype, or is that not needed?
**Aaron Abbott** 19:23 If it's something small, but I wouldn't spend too much time or polish at this point.
Yeah.
**Surya Teja** 19:31 Cool. Thanks.
**Aaron Abbott** 19:32 Yep, no worries. One other question, is this…
You said agent SDK, is this for calling… is this for calling LLMs, or just for some kind of offering they have where you can build or run agents?
**Surya Teja** 19:45 It's for calling LLMs, I guess, but I need to dig more into it.
**Aaron Abbott** 19:52 Okay. Are you familiar with the kind of conventions we have?
**Surya Teja** 20:00 No, I'm not familiar with the conventions.
**Aaron Abbott** 20:02 Okay.
Yeah, I would… I would definitely start there, too, and make sure that
But we generally try to… do instrumentations.
Where we already have some conventions, so, please take a look, and…
If you think that that stuff is covered by,
Sorry, that's not the right link.
If you think the,
Instrumentation you want to add is covered by these conventions, then that's… that would be pretty, uncontroversial to add.
Sorry, there's a link.
**Surya Teja** 20:36 Cool.
**Aaron Abbott** 20:37 Okay, great.
**Surya Teja** 20:41 Thank you.
**Aaron Abbott** 20:43 Yep.
Alright.
Thank y'all.
See you later.
