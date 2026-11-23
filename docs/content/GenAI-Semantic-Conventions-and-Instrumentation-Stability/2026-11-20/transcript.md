SIG: GenAI Semantic Conventions and Instrumentation Stability
Date: 2026-11-20
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker (Microsoft Corporation)** 02:48 Hey folks, we'll give a… Couple minutes for… hopefully some more folks to show up on this Friday afternoon.
**Liudmila Molkova** 04:34 Hi, folks.
**Trask Stalnaker (Microsoft Corporation)** 04:38 Hey, hey!
**Liudmila Molkova** 04:40 I am sorry I'm late.
**Trask Stalnaker (Microsoft Corporation)** 04:44 No worries, looks like you are someplace.
**Liudmila Molkova** 04:50 office, very… Rare occasion.
**Trask Stalnaker (Microsoft Corporation)** 04:54 Seattle?
**Liudmila Molkova** 04:56 Kirkland.
**Trask Stalnaker (Microsoft Corporation)** 04:59 Cool.
**Liudmila Molkova** 05:02 2 miles to Microsoft Canvas. Well, maybe 5.
A.
**Trask Stalnaker (Microsoft Corporation)** 05:12 I can share.
**Liudmila Molkova** 05:14 Yeah, thank you.
**Trask Stalnaker (Microsoft Corporation)** 06:05 Okay, so I know we have a couple of topics, let's see, release… Operation… Name… Operation Naming.
Anything… Else that we should discuss?
Got a few PRs… For the stabilization wave that need another review.
**Liudmila Molkova** 07:06 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 07:07 I think this is related to that…
**Liudmila Molkova** 07:10 Great.
**Trask Stalnaker (Microsoft Corporation)** 07:11 Question…
**Liudmila Molkova** 07:22 Dylan, would you mind reviewing a couple of Trask PRs?
**Dylan Russell** 07:26 Yeah, I can do that.
**Liudmila Molkova** 07:28 Thank you.
**Trask Stalnaker (Microsoft Corporation)** 07:28 doesn't help.
**Liudmila Molkova** 07:30 No, why?
Your peers.
Yeah. Oh, no, it doesn't help, no.
I need that echo.
**Trask Stalnaker (Microsoft Corporation)** 07:39 I need to, I will, ask I'll get, okay.
Let's see, approve… how do I do has an approval?
Reviews… they… Approved. Okay.
Yes.
**Liudmila Molkova** 08:13 pending query.
**Trask Stalnaker (Microsoft Corporation)** 08:15 Yes.
**Liudmila Molkova** 08:18 But you're also very welcome to review Trask peers, everybody else's.
**Dylan Russell** 08:28 Good.
**Liudmila Molkova** 08:29 Thank you.
**Trask Stalnaker (Microsoft Corporation)** 09:00 Okay, this one I need to mark.
Next there, 8, Okay, and then, let's see, waiting on author… Okay… Finish reason… Okay, I think this one… Probably I just left… Okay, so I will approve that as soon as… Erin has a chance to review… Okay, this one, yes, is good to go, and this one is pretty much good to go. Okay. Okay, so I think we're doing… Well there, so let's… Do you want to talk about, anything you want to talk about the release, Ludmila?
**Liudmila Molkova** 10:39 No, I can probably cut it today. Any objections?
Okay.
So, let's… let's make it happen.
**Trask Stalnaker (Microsoft Corporation)** 10:48 Alright.
Okay, so let's talk about Operation Name.
Let's pull up… Oh, what's the issue number? Do you remember it by heart?
**Liudmila Molkova** 11:09 Okay, this one I cannot remember. Music.
249.
**Trask Stalnaker (Microsoft Corporation)** 11:21 Thank you.
Alright.
So… Yes, so what, I… So I saw… yes, so I saw the… is the question… Basically, do we… PIN, operation name, or do we leave that as flex… more flexible, the way we did for… Invocation invoke here.
Or is it specific? I didn't quite follow the relationship to the dot versus sort of the… interactions.create versus create underscore interaction.
**Liudmila Molkova** 12:23 Yeah, so, the current scheme uses underscore in this form.
But if we look into native instrumentations.
or, the issue Dylan… Dylan… maybe not Dylan, but somebody created about Google GenAI, interactions.create. It kind of matches the… the programmatic way APIs are called, right?
And there is a pattern outside a photo.
It seems so, to name operations with this style.
And… It's a matter of style. Either works for me, but I would imagine that more and more native instrumentations or something outside a photo ecosystem would not follow the patterns we have and give this style of the naming.
And there is a… comment was collapsed, the one above… yeah, here, sorry, one above. So if you look for native things here, for example, on tropic native Instrumentation.
Calls them, anthropic.shut message create, because… this… this matches their REST API, which is create… message create.
So, from the broader to the… From the object to the action.
**Trask Stalnaker (Microsoft Corporation)** 14:06 So, these, though, I mean, wouldn't we prefer… I don't know, would we prefer these to just be chat and embeddings and, like, not… like, I'm wondering if the reason they put these, like, namespaced them was thinking that they needed to namespace them for, Uniqueness to them, like, since it's their own names.
**Liudmila Molkova** 14:33 Potentially, but, like, you see the pattern, so, like, I think maybe it was a stupid idea to merge together there.
non-native and native Instrumentation with anthropic message create, then Haystack Native uses the same pattern.
I…
**Trask Stalnaker (Microsoft Corporation)** 14:52 I see Agent wrong.
**Liudmila Molkova** 14:57 And then, And, like, yeah, imagine we want to introduce step. Would it be step underscore agent, or agent underscore step, or agent dot step?
So the pattern was…
**Trask Stalnaker (Microsoft Corporation)** 15:15 Or just step.
**Liudmila Molkova** 15:17 just step, yeah.
**Trask Stalnaker (Microsoft Corporation)** 15:19 Because it's already scoped… well, I don't know, a little confusing, because we… we reused the operation name… attribute.
in different… span types.
So it's sort of scoped… To span type, but also sort of not.
**Liudmila Molkova** 15:42 Christmas.
**Trask Stalnaker (Microsoft Corporation)** 15:43 Sort of a global list.
**Liudmila Molkova** 15:45 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 15:47 Well, it's… that's because it's an enum, right? Is it an enum today?
**Liudmila Molkova** 15:53 It is an enum, yes.
And we… we could say it's a string, if we had span type actually usable, right? But I think we need to stick with the enum and somewhat reasonable guidance until span type is… Widely used and stable.
**Trask Stalnaker (Microsoft Corporation)** 16:14 Right.
But looking forward to that…
**Liudmila Molkova** 16:24 Looking forward, I think we would just say it's a string? Put whatever you want.
Like, language agnostic, at least, within your ecosystem.
**Trask Stalnaker (Microsoft Corporation)** 16:36 Right. Yeah, we almost don't… care that much.
Except maybe in… Cases where we're… Aggregating multiple operations into a single span type.
**Liudmila Molkova** 17:01 Yeah… But, like, if… if in your world you prefer… prefer… I don't know, replaced to absurd.
then… You are free to call it… Just be language agnostic.
**Trask Stalnaker (Microsoft Corporation)** 17:18 That's true, yeah, because, like, I've seen database, like.
I think, like, it being select, but we don't… I don't think we actually say anything about it.
Should be select, it's just whatever the verb.
But… The database ins… database uses.
**Liudmila Molkova** 17:41 Yeah.
So, I'm… I… I don't have a preference. I… See how keeping an operation names is good, because so many things is built on top of them.
Alrighty.
**Trask Stalnaker (Microsoft Corporation)** 17:59 Yeah, it's very nice for the span name.
**Liudmila Molkova** 18:03 Yeah.
And, what should we do about interactions.create? Because, like, I think it makes sense.
And I would approve it, unless we… Wanted to coerce it into something common.
**Trask Stalnaker (Microsoft Corporation)** 18:32 I see. So, I mean, do we… I'm trying to think… in… Like, database semantic conventions, we don't… Say… we don't… name them. We're, but I guess we could.
We kind of just leave it up to the instrumentations to use the term, but I guess in that case, it's a little more… there's… it tends to be more clear, because it's part of the syntax, typically.
Although, maybe not, like, for example, like, Mongo, I think… What we ended up doing for some of the non-SQL databases.
is just using, like, the API, the… yeah, the Java API name, which is sort of, like, what this is doing.
**Liudmila Molkova** 19:27 Yeah, and I think it mostly follows the API name, because, like, if the reference documentation is create interaction.
I'm curious, Dylan, what you think, like, how does interactions of crate look for you? Because I think you've done a lot of instrumentation around…
**Dylan Russell** 19:47 Yeah.
It… it's exactly what you call… Like, when you talk to the API.
**Liudmila Molkova** 19:58 the Python API.
**Dylan Russell** 19:59 Yeah.
Yeah, I… yeah, is it also the underlying API? That's a good, good question.
**Liudmila Molkova** 20:17 the internal API is paused.
**Dylan Russell** 20:20 Okay, it's just, like, there's, like, an interactions resource, right? And you…
**Liudmila Molkova** 20:25 Alright.
**Dylan Russell** 20:31 Yeah.
That is a little funky.
Makes me think maybe it should just be interactions.
**Liudmila Molkova** 20:47 Oh, but then you can do more things than create those interaction, right?
It cannot be just the resource name. You can cancel, get, delete.
**Dylan Russell** 21:00 Right.
Is this operation name is for a particular span, like an inference span?
**Liudmila Molkova** 21:11 Oh, this is even more interesting, because this operation is the same for Invoke Agent and Invoke Model, because both exist behind this API.
**Dylan Russell** 21:22 Yes, that is true.
**Liudmila Molkova** 21:25 And then we would… So, is it a good idea to even use this name? Because for Invoke Agent, we probably want Invoke Agent, at least for the time being.
**Dylan Russell** 21:41 for… do we… I don't know what we do for the agent name, for the span name for agents.
Do we have this… oh, this operation, I'm sorry, this is an attribute.
Or is.
**Liudmila Molkova** 21:54 Yeah, this is both, so you can put it in the spend name, And standard as an attribute.
**Dylan Russell** 22:02 Okay.
**Liudmila Molkova** 22:05 And this API, this PR, what it does, it says, invoke agent for agent, keep this, but do interactions that create for inference.
**Dylan Russell** 22:17 Right.
Yeah.
Mmm…
**Liudmila Molkova** 22:25 Gosh, this is… more difficult than I thought.
Alright.
**Dylan Russell** 22:38 Yeah, how do we define, like, operation name?
We'll have to… Yeah, I think I have to look at this one… For a little bit, to… Come up with an opinion, maybe.
**Trask Stalnaker (Microsoft Corporation)** 22:58 Yeah, I think the discussion helped me, to understand, sort of, where you're coming from, so I think that'll help me. I can go back and look at… These now with that.
perspective.
**Liudmila Molkova** 23:14 Yeah, okay.
So, let's sleep on that. Cool.
**Trask Stalnaker (Microsoft Corporation)** 23:20 Yeah.
Alright, anything else we should chat about?
**Liudmila Molkova** 23:39 Rather than anybody.
**Trask Stalnaker (Microsoft Corporation)** 23:40 Wants to chat about.
**Liudmila Molkova** 23:42 Let me add an item. I created… I've been reviewing PRs, and I created a bunch of issues. Some of them are about the ports.
And I think we need Aaron for this.
that I like to talk about the Finnish reasons.
It's 7, 9… 729.
**Trask Stalnaker (Microsoft Corporation)** 24:12 Instead of…
**Liudmila Molkova** 24:19 So, what do we do today? We have GenAI response finish reasons on Agent.
And we define it as… The… Essentially, the last model response.
That resulted in agent replying to user. The finished reason of this.
It breaks in a few cases.
For example, if, I don't know, Agent is asking you for an action.
asking humans for an action. We reasonably don't have a right way to document it, or if an agent run out of the… there is a tool called limit, for example, or iterations, or steps, whatever.
And most… essentially, it seems the response finish reasons don't fit Nicely into the Agent world.
And… I was thinking, what is the… other attribute we can use, or if we need to do something about Finnish resins.
And it's some sort of a status. Like, we don't have the domain-specific status code for GenAI, right?
The Finnish reason is some version of it, but not… not quite.
The exception, in error type is another one.
But, like, again, things like cancellations and benign errors, there is no way to capture them. There are not errors.
So, I'm thinking we have an attribute generic response status, which is… more broad.
The trick today… It's used by the fetch response.
And it represents the… the generation status, not the upper… not the operation. So I'm fetching something.
And there was a Finnish reason there.
Or maybe it's still in progress?
and I'm returning, okay, it's in progress, or I'm returning, okay, it reached the maximum length, right? But it's not my status. If I was canceled.
I should not put it there, because it's mine, not the… not the definition of the thing.
And I think it's not great.
So… what I was thinking about.
Leaving the fetch response aside for a sec.
We should probably use the… some version of response status and make it About this operation, or maybe the operation status.
And this would represent the… what happened to an agent run.
It can also represent what happened to any other operation, GenAI operation.
I don't want to limit it to agents, because… Huh.
I don't know.
It's too narrow.
**Trask Stalnaker (Microsoft Corporation)** 27:45 So, response… status… I'm trying to think of the… I feel like there's kind of… There's client requests that make requests and get responses, and it's sort of, like, response status.
Although… We do, I think in databases, some kind of generalize that response status, or RPC, to also include, sort of, things that didn't necessarily come back over the wire.
And then we have things like… invoke agent… server or internal… Which… I don't know, do we model… do we have other request response attributes on those?
**Liudmila Molkova** 28:38 on agents.
**Trask Stalnaker (Microsoft Corporation)** 28:40 Yeah.
a non-client.
**Liudmila Molkova** 28:43 Let's see… I have the motto.
**Trask Stalnaker (Microsoft Corporation)** 28:50 Oh, like, request model?
**Liudmila Molkova** 28:51 to me.
**Trask Stalnaker (Microsoft Corporation)** 28:52 We do request… is it request model?
**Liudmila Molkova** 28:54 It is the request model, yeah.
**Trask Stalnaker (Microsoft Corporation)** 29:05 I mean, it makes sense, from It's… you're requesting it of that.
Even local agent.
**Liudmila Molkova** 29:19 Yeah, we have a bunch of other requests, choice count, we probably… Wow.
it's a good idea to clean some of them up using the conformance. If nobody populates it.
Then maybe we should drop it on spans, for sure.
It's in the… Edge and Spence.
Should clean this up, right?
**Trask Stalnaker (Microsoft Corporation)** 29:52 Oh, here we go.
**Liudmila Molkova** 29:54 Invoke Agent internal span.
**Trask Stalnaker (Microsoft Corporation)** 30:03 West… okay, so we have some…
**Liudmila Molkova** 30:18 I'm thinking…
**Trask Stalnaker (Microsoft Corporation)** 30:20 Are these, typical… are these borrowed from inference, and sort of then, like, defaults for an agent for its inference calls?
**Liudmila Molkova** 30:31 Yeah, and some SDKs allow to configure them. Maybe most of them we should drop, and just let the individual SDKs, if they define conventions, to reference them.
Because it's kind of confusing here.
**Trask Stalnaker (Microsoft Corporation)** 30:58 Okay, and this is the one response, so we've got various requests, and just this one response.
soonish reason…
**Liudmila Molkova** 31:07 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 31:11 Okay, but yeah, not… not… this is from inference.
Okay, so you're saying, sort of, what's your current… I think… do you have a current thought or proposal?
Or leaning.
**Liudmila Molkova** 31:41 I would prefer something like operation status.
Because I think this response on the agent It implies the in-process… oh, sorry, the… Not implies, but hints at the remote stairs.
And I think… for the current usages of response status on the fetch response, I'd rather replace it with finished reason.
on… At the same time, the fetch responds.
Who would have some additional place, like operation status, to record that the operation was canceled.
So I would deprecate the response status.
And repurposes into operation status.
**Trask Stalnaker (Microsoft Corporation)** 32:41 Okay, let's, I'll look at… I'll think about this.
try to get up to speed for the next… for Monday. We can chat more.
What else do we want to… We want to be ready for… we want to discuss… Already lost the… oh yes, this one.
I do.
Ready?
Oh, I put it… I see, I put it in the wrong… Order it is.
I don't know why that amused me so much.
Okay. Anything else that, you want us to, think about before Monday, to discuss on Monday, from your issues?
Oh, can't hear you.
**Liudmila Molkova** 34:08 Sorry, there are a few issues around the ports.
they are… I want to discuss them with Aaron. I'll ping him, make sure… He takes a look before we talk about them.
**Trask Stalnaker (Microsoft Corporation)** 34:24 You said around reports?
**Liudmila Molkova** 34:27 Around parts.
**Trask Stalnaker (Microsoft Corporation)** 34:28 It's… okay.
**Liudmila Molkova** 34:30 So we… and messages. So, example, make her all optional on GenAI messages.
**Trask Stalnaker (Microsoft Corporation)** 34:40 Cool, if you could drop a… list here of… things that you'd like to discuss, I will try to, Get up to speed on them.
Before Monday's discussion.
**Liudmila Molkova** 34:56 Awesome, thanks. Then I'll go work on the release, and maybe clean up some docs, but anyway.
Whoa.
**Trask Stalnaker (Microsoft Corporation)** 35:05 All right.
**Liudmila Molkova** 35:05 each other on Monday.
**Trask Stalnaker (Microsoft Corporation)** 35:06 If you have a chance, I left you a Slack message about a conformance PR that I'd like to merge, if you have a chance to look at.
**Liudmila Molkova** 35:15 Oh, awesome, I'll take a look now.
**Trask Stalnaker (Microsoft Corporation)** 35:18 Alright.
**Dylan Russell** 35:18 Good. Yeah. Perfect.
**Liudmila Molkova** 35:20 Have a good weekend, everybody. Thank you.
**Dylan Russell** 35:22 Yes.
**Trask Stalnaker (Microsoft Corporation)** 35:22 by…
