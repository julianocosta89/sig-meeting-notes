SIG: GenAI Semantic Conventions and Instrumentation Stability
Date: 2026-10-30
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:01:01 Hello.
Dylan Russell 00:01:05 Boom.
Trask Stalnaker (Microsoft Corporation) 00:01:06 Happy Friday!
Liudmila Molkova 00:01:09 Happy Friday!
Trask Stalnaker (Microsoft Corporation) 00:01:23 I can drive the boat today.
Liudmila Molkova 00:01:26 Thank you.
Congrats on the election!
Trask Stalnaker (Microsoft Corporation) 00:01:31 Thank you.
Liudmila Molkova 00:01:33 Trask is.
Forever a GC member.
I wish all the elections in our life were between awesome people.
Trask Stalnaker (Microsoft Corporation) 00:02:11 All right, so… We don't have specific topics.
But… I think Probably be worth going… through… I wonder… I could probably go through… it might be better just to go through… Separately acing, offline to kind of re-sync on what's… where we're at with the whole, Stability… Effort.
Liudmila Molkova 00:02:52 Sounds great.
Trask Stalnaker (Microsoft Corporation) 00:03:01 I did, This morning, Postpone, officially gave up on getting the, Java release out.
-Oh.
Liudmila Molkova 00:03:15 Whoa.
Trask Stalnaker (Microsoft Corporation) 00:03:15 So I… So, that's gonna happen in December, because, we're… I need to… help out here more, and also we have KubeCon.
Liudmila Molkova 00:03:29 Oh, I'm sorry, what blocked it, if it's not a secret?
Trask Stalnaker (Microsoft Corporation) 00:03:34 Oh, no, no, just too much, too many things, too much things trying to get into there, and too many, finding too many corner cases in semantic conventions and database, we're stabilizing database semantic conventions and RPC semantic conventions.
Liudmila Molkova 00:03:56 I see.
Trask Stalnaker (Microsoft Corporation) 00:03:58 It's fine. There's no… I was trying to get it out, but there was no, like, external pressure, and we have the 2X maintenance branches going now, so we can continue making Standard monthly.
version bumps.
Yeah, so this… So, let's say, Yeah, I can do that offline.
Yeah, let's look. I think the best use of this time has been… Kind of looking at… PRs… Do we have, I forget our cast.
name.
Liudmila Molkova 00:05:14 Max.
Trask Stalnaker (Microsoft Corporation) 00:05:15 Max, thank you.
Liudmila Molkova 00:05:19 Doesn't seem to hear.
Trask Stalnaker (Microsoft Corporation) 00:05:22 Some follow-up. Okay.
Liudmila Molkova 00:05:25 I've got through it, and… I left mostly cosmetic stuff, no… big concerns, Maybe we need some more clarifications and less text.
But overall, it looks good.
No structural changes that they would propose.
Trask Stalnaker (Microsoft Corporation) 00:05:53 Cool.
Yeah, this would be really… yeah, I'm trying to think what… if we think we can… I know we're not going to RC it, but it would be nice to get a release.
Do we want… Do we want to release before RC?
Or do we want to just… I'm a little nervous about people adopting interim changes, but I think people are doing that anyways.
Liudmila Molkova 00:06:31 I'm thinking, we… And now… Let's… let's imagine we've done… we've done all the major changes.
That we planned, and we're almost there. Except that there's a big invoke agent in Workflow.
And summary names that they're in flight.
Imagine we've done this, and it's in your issue 511.
So I'm looking into this.
So, like, this is very uncontroversial.
This list of spans and metrics.
if we're… finalized this.
This would be… Safe to call RC.
Before that… If I release before… I would prefer not to.
Given how close we are.
Trask Stalnaker (Microsoft Corporation) 00:07:45 Yeah, so maybe that is, yeah, I think that makes sense. And then the… I guess the follow-up question is, what's… Yeah, how close are we to RC? And that was the homework I… had meant to do here.
Liudmila Molkova 00:08:04 I did look at.
Trask Stalnaker (Microsoft Corporation) 00:08:08 I did look at… yeah, 249 is looking really close. That was a big one. I was looking through your PRs.
Liudmila Molkova 00:08:21 Yeah, 2.49 for the scope, I'm pretty sure we can push it through… Soon. The Invoke Agent Invoke workflow, I hope we just had the cosmetic stage now. I'll ping Max and see, like, how far… how fast he can make progress, and if he needs any help.
I am pretty much… Sure, that he wants to also add the ease nested.
And without it, This one be super helpful.
Like, all the dashboards have no idea, unless you know the agent name that you want… is the top one.
They wouldn't have a good breakdown.
Trask Stalnaker (Microsoft Corporation) 00:09:08 for metrics.
Liudmila Molkova 00:09:10 Yeah, Pharmatrix, yeah.
And… Other than that, we have exception events, but I imagine we can keep them in… We don't have to stabilize them, or we can rename them.
Trask Stalnaker (Microsoft Corporation) 00:10:23 Oh yeah, you were saying exceptions.
What about main agent?
Liudmila Molkova 00:10:37 The entity? Or the… Stamping it.
The attribute.
Both.
Stamping, we can add. Entity… We do use it internally, well, and externally.
It's effectively one implementation.
do… we have anybody else who… used it.
And it worked for them.
Trask Stalnaker (Microsoft Corporation) 00:11:21 Not as entities, although I think it's… I know we've used… The main agent concept stamping.
On spans.
Liudmila Molkova 00:11:41 Yeah, well… Could we… I feel confident about stamping, even though we don't have it implemented.
I'm not… I'm less confident about NTT, but just because there is just effectively one user that I'm aware of.
But if there is appetite to stabilize NTC, We probably can.
Trask Stalnaker (Microsoft Corporation) 00:12:14 It makes sense to me from a hosted perspective. I… I can… Check with, internal… Folks.
I know there were… A little confused about it.
Felix, the reason you, you have hosted agents, but you would… Do you have interest in main agent either as an entity or span attributes?
Felix Becker (Anthropic) 00:12:53 Yes, I think so.
Sorry, I haven't looked into this proposal, deeply, but, generally, currently, it's… it's a little messy, because we have the GenAI conversation ID, And we put it… we make it like the… the thread ID, so that different sub-agents are not, like, mixed with each other, but then there's no standard attribute for, like, well, what is just the session ID that it, like, encompasses everything?
And so some more… First-class concept or attributes for, like.
What here is the main agent? What is, like, the overall, kind of, session identifier that encompasses it all, and which are, like, the… Sub-agent ideas would, would be helpful.
We've had a few customers that were, like, confused by this.
Trask Stalnaker (Microsoft Corporation) 00:14:01 So I guess the other… like, I feel like it's a really important concept, but… I guess the… maybe the more… more… or another irrelevant question is, can we add it later? Is there any… Problem with that, layering it on top of… Adding it later, basically.
Liudmila Molkova 00:14:23 I don't think so.
Same as entity, right?
Trask Stalnaker (Microsoft Corporation) 00:14:27 Yeah, I think so. So… Yeah, cause… Probably… Especially if we're thinking of… Doing the RC… very soon.
I think there's probably a little too much… Thinking and discussion and… Prototyping to… Iron that out.
Liudmila Molkova 00:15:01 Yeah.
And maybe we should get better at… Stabilizing smaller features.
Felix Becker (Anthropic) 00:15:21 Yeah, I mean, from my perspective, that's fine. Our solution currently works. I don't know if it's, like, a Like I said, I haven't looked at this too deeply, I don't know if it's, like, a breaking change afterwards.
I could just… additive.
Liudmila Molkova 00:15:46 It should be additive, because it's the… the new attribute, or… New entity that's being added.
Unless you already have some notion to say, okay, this… Sub-agent execution happened in scope of this outer agent, however it's… propagated.
And done.
Do you do this? Do you capture, like, the top-level thing, or it's just assumed to be harnessed all the time?
Felix Becker (Anthropic) 00:16:22 Sorry, what do you mean, what capture the top-level thing?
Liudmila Molkova 00:16:29 So, like, the main agenda that's important when you have Some agent as entry point, like the main agent that is hosted And it has a name.
And then, there are sub-agents.
And then, let's say you have invoke Edge and Spence, and then you query the spanse, but you need to… No.
At query time, who is the top-level agent for this nested.
Felix Becker (Anthropic) 00:17:02 Yup.
Yeah, we, I don't think we really put in… Like, have any attribute that tells you that right now?
Which is a bit of a gap. I think it's… it's only, like… when you… When the client invokes the agent, right, like, the main agent is always the coordinator that's gonna, like, handle the… The request directly, and so you kind of see it in the span hierarchy.
Because the coordinator will then talk to other agents, then kick off, invoke agent spends there, but there's no, like.
specific attribute that tells you, like… so if you were just gonna write a query, you wouldn't really have a good way to do that.
Liudmila Molkova 00:17:54 So then it's good news, because it's got for everybody, and if we add the main agent, it would fill the gap, and it wouldn't break anything that you have.
Felix Becker (Anthropic) 00:18:04 Yeah, I assume so. I can take a look at this PRA sync.
Liudmila Molkova 00:18:09 Let me find it.
Felix Becker (Anthropic) 00:18:13 Is it not the one that's on the screen?
Trask Stalnaker (Microsoft Corporation) 00:18:16 No…
Liudmila Molkova 00:18:24 It's actually in draft, and it's a very old one.
Trask Stalnaker (Microsoft Corporation) 00:18:29 I got it.
Liudmila Molkova 00:18:30 Oh, thanks.
Felix Becker (Anthropic) 00:18:40 I'll take a look at that.
Trask Stalnaker (Microsoft Corporation) 00:18:49 For Marine's… let's see… Remote.
Liudmila Molkova 00:19:00 Oh, so client agent… oh, it's… it's in the… the issue that you have, 511.
So, it is the braking change.
Felix Becker (Anthropic) 00:19:17 Are we also adding mainagent.id? Because we don't always have a name.
We touched on that in a previous.
Trask Stalnaker (Microsoft Corporation) 00:19:29 I was… I was in favor of.
both ID and name.
Liudmila Molkova 00:19:33 Yeah.
Trask Stalnaker (Microsoft Corporation) 00:19:33 attributes.
Felix Becker (Anthropic) 00:19:39 Otherwise, I… I mean, we can put the ID into the name, but… Might be nice, separate.
Liudmila Molkova 00:19:48 We can't… we can decide, yeah.
This PR, it has some extra stuff that also intends to use this is not… Anyway, so there are parts of this PR that are probably irrelevant, and we'll take them away, but, It's… It's a… it's a predative. If you mind dropping a comment, that ID would also be useful. I'll figure out how to… Make it nice.
Felix Becker (Anthropic) 00:20:26 I would love if we have some time to talk But the PR side linked in the agenda.
They're my first PRs.
Trask Stalnaker (Microsoft Corporation) 00:20:34 Yeah.
Liudmila Molkova 00:20:35 Peace.
Trask Stalnaker (Microsoft Corporation) 00:20:37 Let's do it.
Felix Becker (Anthropic) 00:20:40 And so I brought this up at a previous call before, but, currently the tool results… specification… has kind of two issues. One is it contradicts itself in two places. In one place, it says any object is allowed, or, like, any JSON value, and then in another place it says only objects.
And the other problem is that It's not really specified, like, how we… Should handle providers that have, like, a… multimodal message part array, and not just, like, structured JSON content as tool result.
and several… vendors to, half that shape, so I think… OpenAI has it, Anthropic has it.
And in Gemini, I looked into it. In the Interactions API, it's also, like, a kind of message part array, and then in the… the, like, a Generate Text API. It's actually, like, a very interesting case where it's, like, both JSON content, but then there's also a parts array, and then the JSON content can, like, reference items from the parts array.
So I have two PRs here to… resolve this, that are, like, kind of alternatives of each other. One is… Simply just relaxing the, the any requ… the, like, contradictions to not say it's only objects, like, it can be any value.
And then… you know, if you have a content part, the instrumentation should use, like, the message part JSON schema to put it in there as an array.
Because I looked at the… Some existing instrumentations that basically just put, like, the vendor-specific, message part equivalent array in there, and so just having, like, an extra sentence in there that says, like, hey, if there is a… content part-like.
structure, it should reuse our, like, GenAI message part, and not, like, the vendor-specific one.
So that's kind of the kind of simple, quick fix, I would say, but it does leave… the type's a bit more ambiguous, like, if I'm a… Platform or a user who wants to, like, query this data, it's not clear, like, is a JSON structure inside of it? Is that, like, the message part array, or is that just, like, an array that a tool returned as structured output, right? Because we're, like, overloading the same attribute.
And then the other PR here is an alternative to this, of, like, actually adding an additional An additional attribute, so we would have, like, dot result and .resultParts.
And parts holds.
the array struct, the message parts, array, and result holds, like, structured JSON content.
And I guess the interesting thing about this is that it would also handle that, like, Gemini-generated text case, where, like, you actually have both, and, like, one can kind of reference the other.
Whereas the… the other solution… doesn't, really.
And the one thing I noted here was that I think it would be good, basically, to have Some sentence in here that says… Ideally, like, one or the other is preferred, like, we try to avoid putting both on the span, because that bloats the span size, and some platforms have, like, limits on how much content they accept, so we shouldn't just, like… redundantly send the same content in two different representations, but if there is structured content, use that attribute.
If it's a content array, you see other attribute.
And if it's, like, the Gemini GenerateText case, where it's kind of both, then I guess use both.
But yeah, I'm curious for feedback of, like, which… which of these solutions feel better.
Liudmila Molkova 00:25:03 One thing before… there is a PR for this from somebody else, an old one.
604, I added it to the notes, but what it starts doing, it's… Suggests an approach where it's one attribute.
And it's a thing with discriminator, it's a union of, yeah, this friend. So, it says type value, but maybe we can have type any, and then, We could have type.
Array for the generic array.
And we can have type.
Whatever, provider parts, entropic parts.
For the entropic structured parts, and this way it could stay Union, but one attribute.
I… I don't know what's a better idea, it's just that having multiple attributes and saying, okay, populate this, only one of this, and then at query time, it becomes difficult.
And it's structured anyway, with arbitrary structure anyway.
So maybe we can solve it with union instead of some form.
But yeah, or maybe we should… like, we definitely need to relax, that's the bare minimum, but we can be as specific as we need to.
Felix Becker (Anthropic) 00:26:32 Yeah.
That's interesting. I guess the, the, The one property of the, like, allowing any, and the… just having, like, the… the tool result as a top-level thing in the attribute was that there was already a pre-existing spec sentence that said, like.
if, if the tool result is, like, a serialized JSON string in some form, it should do every effort to, like, deserialize it so that, you know, I don't know, if you're in Datadog or something, you look at it, you don't see, like, a double encoded JSON string, you just see, like.
extracted, JSON object.
And so, I guess the… like… Adding, like, the tide value Then you're kind of packaging it more together.
Although I guess the content here is still an object, so it can still do that.
But it's maybe, like, a larger design decision here of, like.
do we and GenAI attributes, Kind of want to move more things into the attribute value with, like, discriminators.
Or keep things more, like… The top level, attribute level.
Because if you imagine, like, I don't know, writing a filter on top of… These things… you might have… like, many platforms probably have very easy filters on, like, the presence of an attribute, or, like, addressing those attributes directly. If you package more things in, like, nested values into the JSON, now you need to do, like, a query on the value, and… the platforms need to be able to parse the JSON in the value to then be able to, To handle, like, express any sort of query on it.
Liudmila Molkova 00:28:36 Yeah, I agree, and we've talked about, okay, this thing is always a primitive.
then we even have a recommendation that the primitives should go to the top-level attributes whenever possible. But here, it's like, okay, you have multiple different… Types, and… They could be… Even if they are different attributes, they are still complex types.
And it's still the story for input messages and output messages, because there is no way around it, right?
So your query capabilities to understand those would need to be advanced already for, like, way more common cases than, I think, parsing tool results.
Felix Becker (Anthropic) 00:29:27 Yeah.
The other thing I was thinking about here is that it appears just like, in some cases, that these are not actually mutually exclusive. Like, MCP allows you to, like, return both structured content and you know, like, message part-rich content, and then the Gemini-generated text also allows you to give you, like, both Both structured content and then also separate parts.
Whereas, like, having a discriminator implies that… the two cases are mutually exclusive, right? Whereas two attributes, it's more like, yes, you can provide both, or you can provide one of them.
Based on what is actually available.
Liudmila Molkova 00:30:10 Oh, the part about the referencing things around, that's… I… I need to learn more about.
You mentioned before that one… one thing can reference something from another part.
Can you… show some example of it, some link that I can just read offline.
Felix Becker (Anthropic) 00:30:32 Yeah, I saw that in the Gemini docs.
I can send that to you, and put it in the PR description, too.
Liudmila Molkova 00:30:40 Thank you.
Felix Becker (Anthropic) 00:30:43 I'm actually not, like, the, you know, the expert on the Gemini API either. I was just, like, having Claude dig through the documentation. And I don't know how common that is, or, like, if we need to support it or not.
Liudmila Molkova 00:30:56 Yeah, we thought you caught it, Claude, with anti-gravity, absolutely. Like, why would you do this with Claude? Never.
Felix Becker (Anthropic) 00:31:10 Cool. Well, thanks for, entertaining my two PRs here. This is probably… we've heard from a lot of customers, they're like, oh, can you start sending the tool results and, like, the standard attribute? And I've had to reply, well, I don't really know what the… Standard way is for us to, like, add the tool results, so this would be great to resolve soon.
Liudmila Molkova 00:31:34 Do you have a strong preference, with regard to one attribute or two attributes, and why?
If… if so.
Felix Becker (Anthropic) 00:31:46 I don't think I have a strong preference.
Yeah, I don't know. I was really hoping to, you know, get some takes, especially from the Google side, since it seems like that's where this is more common.
Trask Stalnaker (Microsoft Corporation) 00:32:09 Ludmila, maybe you can, speak a little bit about the advantage to having it, like, be able… being able to union them, versus just, you know, I mean, making it an any… isn't any type, but, I mean, making it true any, and being able to store, like, a string directly, or anything directly in Here… Versus having, like, some minimal common Object structure, so you can union them.
Liudmila Molkova 00:32:42 Oh, like, we can union different things, or we can have a big top-level object with multiple properties. Is this the question, or…
Trask Stalnaker (Microsoft Corporation) 00:32:54 Maybe I didn't follow, for… If we're talking about Say we're talking about this option, as opposed to… Result parts.
It sounded like there were two options. One, this PR, which basically just says it's anything.
Slam whatever in there.
Versus this one, which… tries to… Still keep it an object, or make it an object, but provide some kind of discriminator information there.
Liudmila Molkova 00:33:35 Yeah.
Trask Stalnaker (Microsoft Corporation) 00:33:36 What do you see as the pros, cons of those two?
Liudmila Molkova 00:33:41 So… Staying it's just any.
is… primitive object array, I think it's the bare minimum, it's just because that the function can't return anything. What we have today is a bug.
Trask Stalnaker (Microsoft Corporation) 00:34:03 Yeah, I ran into that in the, in the reference scenarios. Copilot was yelling at me that it didn't conform to something, and I'm like,
Liudmila Molkova 00:34:14 Right.
Trask Stalnaker (Microsoft Corporation) 00:34:14 That's not my pra- that's not my current problem.
Liudmila Molkova 00:34:20 Yeah, so… What is the added value of describing any better?
is that, okay, imagine I'm de-sterilizing it.
If I don't know what it is.
I would need to always write, let's say, two branches. That is… This serialized to an object.
Then they check the type of the object, and, or deserialize to array.
Because just from the JSON Decentralization perspective, These are… In strongly typed languages to different… Types you get back, right?
It's just very not ergonomic to have something like this. Than… it seems what Felix wants is a little bit… more than just any. So, like, there are special… ways to return result that's already wrapped? Like, if you already wrap it to the, let's say, Entropic-specific result part, to a co-response part, right?
It's like the function can do this wrapping.
And then… There is some… something extra that, Felix, you would like to do around these types, is that right?
Felix Becker (Anthropic) 00:35:55 I'm not sure I follow what you mean with… Wrapping.
Liudmila Molkova 00:36:01 So, like, imagine my function can return an array of objects, or array of strings, for example.
And… There is a special meaning.
For my function returning The two corresponds parts directly.
That, later on, are not converted into input messages, but are taken as is.
Felix Becker (Anthropic) 00:36:30 Yes, correct. Like, in Anthropic, a tool always returns.
like, a parts array. It's actually the other way around. Like, if you want to return just JSON, you need to serialize that JSON and put it in a text block.
Liudmila Molkova 00:36:48 Oh…
Felix Becker (Anthropic) 00:36:49 And I think the same is true for, like, the Gemini Interactions API and the OpenAI tool results.
and then only the Gemini generates… Text one is a little… Different, where, like.
the default path is, like, just the JSON structure, but you can return, like, extra multimodal parts, and then your JSON can, like, do a dollar ref reference into that, so the parts can contain an image, and then your structured JSON can say, like.
I want this image, like, to reference it in this… this section.
But that seems, like, more like the exception of all the providers.
Liudmila Molkova 00:37:37 Yeah, I'll investigate it more, but my thinking was that if we, if SDK has any special treatment for… the… To call result.
And it's especially for the expect certain structure sometimes.
from it. And maybe it would be useful to have a deterministic way to capture this.
Felix Becker (Anthropic) 00:38:08 Yeah.
Liudmila Molkova 00:38:10 Yeah, but I'm, I'm thinking, like, what… about Trask's question, and I think it boils down, do we… how much… Where we can go with it at the moment.
And if I say it's just any today, it's backwards compatible, and how precise we want to be.
In the future.
Felix Becker (Anthropic) 00:38:37 Yeah.
I think I have a slight preference for a new attribute, because… It feels cleaner, and it supports the cases of where there can be multiple, like… Mcp specifically.
started out with just the shape of, like, content blocks, so it also, if you want to return JSON, you have to serialize it and put it in a text block.
But then when MCP added output schemas for tools to the specs, so that the model could, like, know in advance, kind of, what schema to expect, which helps with, like, programmatic tool calling.
They also added, like, structured outputs as, like, a property, and so on.
Now, tools can return basically both a structured representation And… the message parts array, and what some tools then do is, like, they put the structured content into JSON, and then in the parts array, they put, for example, a markdown version of that result.
for the model to read. But there's also other tools that maybe, like.
make it complementary. So, like, you can put structured content in the structured content, and then the parts area, you know, contains an image that's binary. And so, it's like… Kind of hard to… and force, or like, say, like, oh, we don't need both, right? Like, I feel like there needs to be a little bit of flexibility for an instrumentation to just provide both in some cases, or prefer one or the other.
Liudmila Molkova 00:40:20 I, like, I think I still don't understand something fundamental about it. So, let's say I have a function.
Python, JavaScript, whatever.
For the toe call. It can return an object. I would imagine it's SDK business to serialize it to JSON to put into a part.
It doesn't have to return a string.
It can return anything.
Felix Becker (Anthropic) 00:40:51 I mean, so, not every SDK even has abstractions for, like, tool calling, right? And, like, you can use the messages API and kind of just listen to tool use and tool results.
Like, and provide… provide back tool result blocks. But in the Anthropic tool runner, for example, you… you must return… like, the tool interface is typed as you always must return an array of message blocks. Like, your function cannot return anything else.
Liudmila Molkova 00:41:20 I see. Okay, so then, I'm here, I'm specifically talking about the tool called span, because this is where it appears.
the…
Felix Becker (Anthropic) 00:41:31 Correct.
Liudmila Molkova 00:41:32 The parts already appear on input-output messages in their form.
But here, it's, what a 2 call actually returned, and… for… Anthropic, we would capture the toll runner, we would capture the… This array of parts.
Felix Becker (Anthropic) 00:42:02 Yeah, exactly. Which is the return value of the tool function. Right. I think this is also why this maybe hasn't, like, popped up as a problem as much before, because I've checked the, like.
Instrumentations in the repo, and… a lot of them don't even produce the tool execute span. They just say, well, that's for the application to… to emit, right? And so it's not something that has actually been emitted in the instrumentations in this repo.
Liudmila Molkova 00:42:29 should be. OpenAI definitely has auto-tool calling, and we have… Quite a few scenarios for auto-tool calling.
Felix Becker (Anthropic) 00:42:38 But I think the… okay, at least the Anthropic one, I think, didn't emit it for the 12Runner, but our first-party one.
Liudmila Molkova 00:42:45 Yeah, probably.
Felix Becker (Anthropic) 00:42:47 And I saw, I think, in… I saw some instrumentation, maybe it was the OpenAI one, that then just, like, used the vendor-specific array and just put it in the… into the, like, tool result attribute, and then it was another, I think, that, like, nested it under, like, a content attribute, just so that it, like, complies with the, it must be an object, and it can't be an error.
Liudmila Molkova 00:43:13 We've done some cleanup there recently, but I think for… Dylan, correct me if I'm wrong about Gemini, but I think for Gemini and OpenAI, it is whatever object.
It can be anything. It's, like, whatever language… whatever tool decided to return.
And then the SDK, serializes it in some shape to pass to the model.
Felix Becker (Anthropic) 00:43:38 If you reload the page, or I could also try to screen share, there are… Oh, I cannot. Well, because you're a.
Trask Stalnaker (Microsoft Corporation) 00:43:47 Oh, yeah, I can stop.
Felix Becker (Anthropic) 00:43:55 So… I'm just trying to find the right tab. I just added the examples here. Can you see this?
Trask Stalnaker (Microsoft Corporation) 00:44:12 Yeah.
Felix Becker (Anthropic) 00:44:12 Okay.
I just added the examples here.
And so this is the Gemini API.
In interactions, you also return this result error, and it's, like, type text… And then type image can be, like, a multimodal response.
And… For… the… for this other API.
You could provide… the parts array.
Separately, and then, oh, I thought I had links to the docs.
Liudmila Molkova 00:45:03 Oh, okay, so then…
Felix Becker (Anthropic) 00:45:05 port.
Liudmila Molkova 00:45:05 The question is that Like, if we have… if we… Put an analogy with input messages.
We could have said, okay, whatever the provider schema for input messages is, just dump it into this any.
And sent to the backend. But we're not saying this, we're saying normalize it.
And here, for the two core result, I was under assumption they are just whatever application returns, and absolutely anything.
But what you're saying, that providers have more structure to them.
And that we could probably do some structuring similar to input messages to unify them a little bit.
Felix Becker (Anthropic) 00:45:54 Yeah, so it seems most providers actually follow a similar thing as message parts, or even reuse, like, their equivalent of message part array.
And some providers have… separately, the concept of returning structured data. So this is an MCP, for example. There's, like, structured or unstructured content, and unstructured content also is, like, you know, type text, type image, type audio.
Versus then you can provide structured as a separate property.
When you have, like, output schema, and then… The result has both content, but typed text.
And structured content, which is just, like, the JSON object directly.
But this is relatively new, like, this was the original shape.
And an MCP server doesn't have to, like, this one here actually, like, puts this in here as, like, backwards compatibility, basically, which I think is a recommendation in the spec.
But… an MCP server could also put, like, markdown content here, and then JSON version of it here.
Or they could put, like, an image attachment here that is, like, complementary to the structured content.
Liudmila Molkova 00:47:12 Okay.
So then probably the… the next step would be to… Try to… Suggest a structure.
Right, either a separate set of attributes, or one attribute, but, like, what would be the… The common denominator that we want.
In the, like, provider agnostic.
Felix Becker (Anthropic) 00:47:38 Yeah, so my suggestion here was that we just… Like, say, we should use the… like, message part array. When the provider uses some message part-like structure, it should use the message part array.
And the… basically, the design decision we have to make is, like, do we just overload that same attribute and say, like, sometimes it's just, like, the structure JSON object, and sometimes it is… an area of message part, and the client just kind of needs to, I don't know, detect that. Or do we say it should be separate attributes?
Where one is always that array, one is always… structured content JSON object, depending on which ones were provided or supported by the provider, and one or the other or both can be set.
Liudmila Molkova 00:48:32 But from what you've shown for the MCP, it's not a part of any sorts, right?
Felix Becker (Anthropic) 00:48:39 It is, for… Here, this is basically a message part, right?
Liudmila Molkova 00:48:47 it… It is, but, like, the structured thing.
Felix Becker (Anthropic) 00:48:51 The structured thing is not.
Liudmila Molkova 00:48:54 Yeah, so, like, this is not the… the message part.
Felix Becker (Anthropic) 00:49:00 Yeah, so that's what I'm saying, is like, you might set, like, this could be one attribute, like, result or result.structured, or result.parts, and this could be the separate attribute, like, result or result.structured, and both could be set.
And this is always, like, the content message part array, and this is always, like, the kind of raw JSON structured object.
But an MCP server could only return maybe this, right? Like, this is a more recent feature.
And the question is, do we… Do we use the same… GenAI OpenTelemetry attribute for both of these, and sometimes it holds this, and sometimes it holds that? Or do we use two separate attributes, and they can be both provided? Sometimes maybe only one of them is provided?
Depending on what fits.
Liudmila Molkova 00:50:07 Ugh.
I don't know yet, but I'm curious.
what… How much the parts cover, and is it just the same as message parts?
For the providers, and what it doesn't cover.
And I think for OpenAI, there is this whatever, anything you can put in the result.
I don't know if they support parts now as well.
And for Gemini, there… it seems there are… To different objects on the result, which is parts and not parts.
And then, like… What things don't fit into the just parts model?
Looking into the… the… MCP response. It's still result?
And then there is a structure, and I think it's, it's one thing. It's whatever we call result.
So it's like, it's a custom schema, is it?
Felix Becker (Anthropic) 00:51:15 What is a custom schema?
Liudmila Molkova 00:51:17 In MCP, like… Like, this, this result, the contents of the result is content, is… and structured content are… Documented somewhere, or it's just the… the conventional.
Felix Becker (Anthropic) 00:51:33 This one here is a static type that's defined by the MCP spec.
Whereas this one here matches the schema that the MCP server provided. So this, from a… MCP spec perspective, or from a GenAI perspective, is any.
Because it matches this here.
Liudmila Molkova 00:51:53 Yeah.
Felix Becker (Anthropic) 00:51:54 But this one here is always the same shape. It has, like, type, text, type, image, type… Audio.
Liudmila Molkova 00:52:03 Oh, and this is already essentially formatted, like, like, parts.
Felix Becker (Anthropic) 00:52:08 Zach's video.
Liudmila Molkova 00:52:08 Consider that.
Felix Becker (Anthropic) 00:52:09 If you want to put JSON in here, you have to make it a text block that has serialized JSON inside of it. Right. Because at the end of the day, right, these are LLMs, and they only take text in, right? So, like, this is how the LLM sees it, right? It gets a text block with that JSON inside.
Liudmila Molkova 00:52:29 Right. Using the same approach, the structured content can also be a part, it's just we would… For reciting to be in a part.
Yeah. With subtype.
That was a property that would be any… Yeah.
Felix Becker (Anthropic) 00:52:46 Oh, you mean, like, a type structured?
Thing.
Liudmila Molkova 00:52:50 Yeah, JSON part, shape, or a structured part.
Felix Becker (Anthropic) 00:52:56 Yeah, I think that is an interesting… thoughts, from serving, like, the implementations that exist, it seems usually they're, like, kind of… They're separated.
Liudmila Molkova 00:53:15 Yeah.
Felix Becker (Anthropic) 00:53:15 Corporate content is not a part of this, like, list.
Liudmila Molkova 00:53:18 I agree.
Felix Becker (Anthropic) 00:53:19 that has, like, an ordered position inside of it. It's, like, like, separate. It's more like an alternative representation, or in the case of Gemini, it's, like, this interesting thing where it can reference it, almost like… almost like an email with attachments, you know?
Or, like, this is the email, and these… this is the email, and these can be the attachments.
Liudmila Molkova 00:53:39 Yeah, yeah, like, you don't know where to put this part in the content, it would be imprecise to either put it to be the first, or the last, or whatever.
Yeah.
Trask Stalnaker (Microsoft Corporation) 00:53:58 How, If we just said result is any, And… Everybody, you know, it's a free-for-all.
I'm trying to understand, is this something that we feel we need to understand, before… RC before stabilizing, like, whether we want to do something Whether we want to provide more structure there.
Versus it being any, and possibly evolving in the future.
Because I assume with… with it any, Felix, like… You just slam whatever you want, you slam the whole… the whole thing, including the parts and everything, into that result.
Felix Becker (Anthropic) 00:54:52 Yeah.
Trask Stalnaker (Microsoft Corporation) 00:54:52 result field.
Felix Becker (Anthropic) 00:54:54 By the way, I've found the Gemini example here with, generate text, where…
Dylan Russell 00:55:00 Right.
Felix Becker (Anthropic) 00:55:01 inline data, MIME type… And then… the… function returns both responds, which is, like, basically the structure JSON, and then Parts, which is the multimodal data.
And then the response has, like, a dollar ref that points to something in parts. So here's a case where, like, you need to support both.
Trask Stalnaker (Microsoft Corporation) 00:55:27 The parts within parts.
Felix Becker (Anthropic) 00:55:30 Yeah.
Dylan Russell 00:55:31 This API they're calling, like, Legacy now.
Felix Becker (Anthropic) 00:55:37 In some places, it's called Legacy, yeah, I noticed it's not called Legacy everywhere.
Dylan Russell 00:55:43 Yeah.
Felix Becker (Anthropic) 00:55:45 But to answer your question, Trav, I… I think, it would be good for, at least for me, to know what to do, because whatever we start emitting, like, we'll probably have, like, platforms move to, like, change the UIs to read that.
And it might also be, you know, harder to, like, once Instrumentation, start putting it in that one… like, if we were to decide, like, oh, we just make it any, and then all the content areas just go into that one overloaded attribute.
You kind of lock in that… decision that now you can't distinguish anymore, like, what… what it actually is. Like, is it a structured content that just the tool returned, or is it, like, the… the part schema.
Liudmila Molkova 00:56:43 I think two things… what's important is we decide we have another attribute or not.
And I think another attribute does not make sense, because… you, an anthropic side, you would always submit the parts attribute. It doesn't even matter.
For you, that the other one exists.
Felix Becker (Anthropic) 00:57:05 Yeah, for Anthropic, that is true. I think for MCP, that would not be true, though. Like, we do need to emit both.
Sometimes.
Liudmila Molkova 00:57:17 For MCP, as you've shown… There is two things, and sometimes you need to repeat… either report both of them, like the structured.
And the parts… And, then the user will be in the question, which one to read and when.
But… I think it was COVID.
Down… sometimes it's anything, and sometimes it's… Something.
And… if we at least… Could have means to say, Okay.
This guy represents… an arbitrary value, we don't know what it is. It's truly any.
And this guy is structured.
With some non-structure. It's like this proposal, but with unions.
So, for… From the evolution perspective.
We would start, let's say, with, okay, everything is unstructured, that's what we have today, but it will be under a specific discriminator.
Sorry, not unstructured, but unknown structure.
Type, type any.
And then there is an object that can be anything.
And then… Where… Could use the same approach with As with, parts, we can say, okay, there are, like.
There could be an object that is an array of parts.
It's another discriminator.
Oh, Trask has something.
Trask Stalnaker (Microsoft Corporation) 00:59:03 I'll… just so I make sure I'm following what you're saying.
Liudmila Molkova 00:59:10 Yes, start with it, but probably, like, better discriminator value.
and then we can evolve it to… have type and tropic parts. For example, if we need to, we're just type parts.
Felix Becker (Anthropic) 00:59:31 But doesn't a discriminator inherently say, like, that the values are, like, mutually exclusive?
Which are not in the case of MCP.
Like, you have both. You need to be able to provide both.
Trask Stalnaker (Microsoft Corporation) 00:59:47 It could be MCP parts.
I mean, the content could be both of them together.
Liudmila Molkova 00:59:54 Oh, it can be an array of these things.
Felix Becker (Anthropic) 00:59:59 Right, but, like, I think in this context, you don't want the type to be, like, coupled to MCP, right? You want to have a standard way to represent tool results.
Trask Stalnaker (Microsoft Corporation) 01:00:14 Which we…
Felix Becker (Anthropic) 01:00:15 through MCP or not.
Trask Stalnaker (Microsoft Corporation) 01:00:17 I think the thought is that could evolve, and we could have a type part in the future where content was then an array of those parts.
Felix Becker (Anthropic) 01:00:29 And then also, like, a… type… parts and structure? Like, how do you handle the case of both?
Trask Stalnaker (Microsoft Corporation) 01:00:37 No, sorry.
Liudmila Molkova 01:00:42 de… I think what Trask is saying, that the type… Yes. Parts and structured.
could be the case. Whether it's a good idea or not, that's… that's a separate question.
Trask Stalnaker (Microsoft Corporation) 01:00:58 But the idea was…
Felix Becker (Anthropic) 01:00:59 From a, like, a… from a perspective of, like, you know, writing conformance tests.
It's easier to have a separate attribute that is only specified as… You know, being the parts array schema, because then you can validate that attribute against the parts array schema.
Versus if you start with an attribute.
that says anything is allowed, and then you have spec sentences that say, well, in these cases, it should actually be an area of this other type. From a JSON schema perspective, it's still any, right? Like, anything would validate, anything would pass. You can't really write, like, a programmatic test that makes sure your instrumentation put the right Content in this attribute.
Liudmila Molkova 01:01:44 Yeah.
Okay, another way to phrase it, if we decided to go with different attributes.
Should this one be renamed? Because then, currently, it represents everything that function returned.
And if we want it to represent something smaller, then we should rename it.
Felix Becker (Anthropic) 01:02:06 Yeah, one thing I was considering here is, like, should… result parts just be an extra attribute, and we keep the current one, or should we actually, like.
Remove the current one, and, like, basically split it into two, one being, like, dot result.structured, and one being one .result.parts.
And just, like, make it very… Clear that these are the new two attributes, and kind of the old one is deprecated.
One thing that's a little weird is, like, I originally thought that you could just add dot result.parts, but there's actually, like, a check in the repo that's, like, an attribute cannot be both a namespace and an attribute at the same time, so that's why it's, like, result underscore parts.
Liudmila Molkova 01:02:55 Yeah.
Felix Becker (Anthropic) 01:02:56 But if we were to remove the old one, we could make it .result.
structure.result.parts.
Liudmila Molkova 01:03:09 Yeah. So, we…
Dylan Russell 01:03:11 structure, sorry. Is structure exactly what the… Structure of result is in this instance, or the possibilities of, like, what it could be?
That question makes sense.
Felix Becker (Anthropic) 01:03:27 You were afraid that?
Dylan Russell 01:03:29 So, like… Is it the exact, like, type of what result is?
Like, if result is, like, a list of strings, it'll be, like, List of strings.
Felix Becker (Anthropic) 01:03:44 Structured would be the structured value, it wouldn't be, like, the type.
Dylan Russell 01:03:50 Structured value.
Liudmila Molkova 01:03:52 It would be the… the… the thing that you don't know, the type of. It's… it's…
Felix Becker (Anthropic) 01:03:57 Yeah.
Liudmila Molkova 01:03:58 Structured with a known structure. The parts of structure was almost known structure.
Felix Becker (Anthropic) 01:04:03 Yeah, well, like, in the MCP case, the MCP server does actually give you, like, a schema for it.
But we… that could be a separate conversation if that should be, like, exposed on an attribute.
Liudmila Molkova 01:04:15 Unknown structure at the Instrumentation time.
Felix Becker (Anthropic) 01:04:19 Yeah, exactly.
It's like…
Dylan Russell 01:04:23 Hmm.
Felix Becker (Anthropic) 01:04:24 basically chosen by the… the tool of it, like, the implementation, right? It's not… Not statically chosen by our spec.
Dylan Russell 01:04:35 I see.
Liudmila Molkova 01:04:37 So I think we have two options on the plate, and we need to, I think, to make a decision before we, go or see, that either we dump it all in one .result attribute.
In some way.
Or we have two attributes, neither of them is .result, because it changes the meaning and whatever that we put in it.
We maybe need to document these two different options and, like, have some prototype for… for them. Prototypes.
I don't know if I have time to work on it by Monday.
But I'll try to at least think about it.
Felix Becker (Anthropic) 01:05:19 What do you mean with prototypes? Like, just implementing both Suggestions in the different instrumentations.
Liudmila Molkova 01:05:27 In Semantic Conventions. No, not in Instrumentation. I'm pretty sure in Instrumentations we can do either or, but, like, how does it look like in semantic conventions, both of those approaches?
Like, fleshed out…
Felix Becker (Anthropic) 01:05:43 Is that not the two PRs? So what's missing from the two PRs?
Liudmila Molkova 01:05:47 the union for the Dutch result.
Felix Becker (Anthropic) 01:05:51 Oh, okay.
So that's the other PR you linked.
Liudmila Molkova 01:05:57 Yeah.
Felix Becker (Anthropic) 01:05:58 But it's, like, not really considering… Honestly, I'm still not clear, like, how a union would fundamentally work for, like… like, it seems like the… a union is for when you have one or the other, right? But, like, fundamentally structured and,
Liudmila Molkova 01:06:18 Oh, incredibly bold.
Felix Becker (Anthropic) 01:06:20 The project can both be provided, so…
Liudmila Molkova 01:06:22 So then it's an object with two properties. Like, we either flatten them down into… two attributes where we'd put them both into a complex object in that result.
Felix Becker (Anthropic) 01:06:34 Which is where, I don't know, I feel like my… inclination would be that, in that case, then it should just be separate attributes, because you could make that design for anything, right? Like, you could… any attribute we have in GenAI, you could just pack into one single attribute that is a JSON object of many properties.
Trask Stalnaker (Microsoft Corporation) 01:06:57 Isn't that what we do for, like, input messages, output messages already?
Felix Becker (Anthropic) 01:07:02 Well, that's an array, right? So, like, you… you actually cannot… But, I mean, I guess you could do an address, like.0.1.2, but, like, you know, that would be… nobody's… Proposing that.
Liudmila Molkova 01:07:17 I think we do split them out when we can.
Like, because this is what… And the model returns were accepts.
And, like, we couldn't put input and output messages into one attribute, because then… They are populated at different types, they can be part of different spans, if it's, like, a synchronous execution and whatnot, and so on.
And I think we… we… Do break them up.
When we can.
Here, I'm still thinking, like, If it's one thing that the tool returns.
What?
Should we split it? It's one thing that two returned.
But I…
Trask Stalnaker (Microsoft Corporation) 01:08:13 That was sort of my… my initial, also, thinking of, for people… who are… I mean, these are, like, opt-in, right, because they're… Large and sensitive, and so people sending that data off somewhere.
There is some advantage to it being one single attribute that you pipe out somewhere that you can reference back to Not… but not that it has to be, though.
But yeah, let's, that's your point.
Let's… I'll try to think on… I'll try to do some reading and catch up to y'all on, how those are used there, and… Yeah, but maybe that… I think that's a good… thought for Felix, if you can… it sounds like the two options we're gravitating to are, one is splitting them, like you've essentially done in one of your PRs.
And the other being the other PR Liudmila link to, which has the… has the single attribute, but with a discriminator type.
And then kind of coalescing, you know, everything into content under… under that one attribute.
Felix Becker (Anthropic) 01:09:45 Yeah, sorry, is this an action item for me?
Trask Stalnaker (Microsoft Corporation) 01:09:49 If you… if you have time by Monday, otherwise, you know, we'll just…
Felix Becker (Anthropic) 01:09:55 I could make a third PR that's basically, like, what a… like, attribute with one object, but two properties.
Is that basically what we're, you know, what we want to consider, too?
Trask Stalnaker (Microsoft Corporation) 01:10:10 Yeah, the discriminator, like, a type…
Felix Becker (Anthropic) 01:10:14 Oh, it's not… it's not mutually exclusive, right? So that wouldn't be a discriminator.
Liudmila Molkova 01:10:20 So, like, the one attribute was complex object having two top-level properties.
Maybe more. Versus two different attributes, which we already have here for.
Trask Stalnaker (Microsoft Corporation) 01:10:35 Oh, I see, so not, so… I thought you meant these would be the two top-level attributes, but you're saying the two top-level attributes would be the… The structured and unstructured.
Liudmila Molkova 01:10:52 parts and…
Trask Stalnaker (Microsoft Corporation) 01:10:54 Value… value.
Liudmila Molkova 01:10:55 raw, raw or something, or value, yeah. Okay.
Trask Stalnaker (Microsoft Corporation) 01:10:58 Okay.
Makes sense.
Felix Becker (Anthropic) 01:11:00 Yeah.
I mean, also, if we're… if we're talking about, like.
should this contain the whole… like, should there be one attribute that contains the whole tool result? Like, isEra is another flag that's returned by the tool.
That… I don't think is currently… Exposed in, like, an attribute?
I think we mapped that, or at least instrumentations. In our case, I think we mapped it to the span status, so we just, like.
Make the spend status error.
But I think that's maybe then another point for, like.
the entirety of the tool result is already not, like, just contained within a single object. It is… Map to different attributes of the span.
Liudmila Molkova 01:11:52 Yeah… Yeah, we should map it to archetype, it's just we don't have anything in the semantic conventions that says to attempt to.
Because for… so far, we've been treating whatever to return as a… as any.
We have no visibility into.
Trask Stalnaker (Microsoft Corporation) 01:12:15 Oh, so we don't, I see, it's not… and the tool result could be error, an error encoded inside of the value.
Felix Becker (Anthropic) 01:12:25 Yeah, so here, this is the example of… an MCP.
there's always is error true or false? I see. And otherwise, you still provide the exact same content area. You can even… the error can still be JSON, right? Like, you can have error… is error true, and it's still, like, the same con… it's kind of like HTP, where the status code is, like.
you can have an HCP400 and so would it turn JSON, right?
and this one, currently, basically, all we're recording as an attribute is this here inside, like, what is actually in the text, which is usually, like, a JSON, right? But this, what, like, which is part more of the envelope of the result.
We don't record at all.
Or, in the case of Anthropic, I just, like, I set the span status to error, so that it, like, shows up as red in the platforms, which I thought, you know, was nice.
Liudmila Molkova 01:13:20 Yeah. I love this new era… okay, go ahead, sorry.
Felix Becker (Anthropic) 01:13:23 Oh, yeah, so, but, like, saying, you know, this is already self-contained of, like, the entire result is, you know, not fully… Correct even today.
Liudmila Molkova 01:13:33 Yeah, that's right. I love this new era where we… the API design is targeted to LLMs, so that it's… like, we have this constant problem in open telemetry that we don't know how to classify 404, because sometimes it's an error, sometimes it's not. But at least we know what to look for, and it always have the same meaning.
Yeah. And for LLMs, it doesn't really matter where you put his error.
Felix Becker (Anthropic) 01:14:01 Yeah.
Liudmila Molkova 01:14:01 the total result.
Felix Becker (Anthropic) 01:14:03 Yeah.
I have to hop, but, okay, I'll open that other PR, give it a thought, like, you know.
if you have a stronger opinion next week, on which one to do, I'm happy to kind of lay the options out.
I think my inclination is a separate attribute, but I'll also think about it more.
Liudmila Molkova 01:14:30 Yeah, thanks a lot for bringing it up.
Trask Stalnaker (Microsoft Corporation) 01:14:32 Yep.
Sounds good.
Liudmila Molkova 01:14:36 Thank you.
Trask Stalnaker (Microsoft Corporation) 01:14:37 yet?
