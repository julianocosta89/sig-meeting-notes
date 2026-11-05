SIG: GenAI Semantic Conventions and Instrumentation Stability
Date: 2026-11-04
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 00:38 a…
**Trask Stalnaker (Microsoft Corporation)** 00:50 Alright, I'm actually here now.
**Liudmila Molkova** 00:53 Awesome.
Did you check about the KubeCon, the office hours?
**Trask Stalnaker (Microsoft Corporation)** 01:02 It had, yeah, in the maintainer chat, And I missed it, and probably a lot of people missed it, but in hotel maintainers, there was a call out from Reese?
On Monday.
So, we just need to pick a time slot here. I'll give you the… SIG Meeting Schedule, I will share.
Let's see…
**Liudmila Molkova** 01:49 You can't imagine what an ordeal it is to open the Slack.
That's crazy.
For in-browser, a link.
**Trask Stalnaker (Microsoft Corporation)** 02:01 Oh, okay, yes, yes.
**Liudmila Molkova** 02:03 Sorry.
**Trask Stalnaker (Microsoft Corporation)** 02:03 It's in the hotel maintainers channel from.
**Liudmila Molkova** 02:06 Yeah. Yeah.
Cool, do you have a preference on time?
**Trask Stalnaker (Microsoft Corporation)** 02:15 Don't. Let's see what we… All slots in yellow are available, just type in your signa.
**Liudmila Molkova** 02:30 We have, our talk is actually on… Thursday. Thursday.
**Trask Stalnaker (Microsoft Corporation)** 02:36 J.
**Liudmila Molkova** 02:37 Well, and everybody will be gone.
**Trask Stalnaker (Microsoft Corporation)** 02:38 Gone. Yeah, yeah, Thursday, yeah.
**Liudmila Molkova** 02:43 But… I'm mostly in.
**Trask Stalnaker (Microsoft Corporation)** 02:46 Yeah, especially when starting on Sunday.
Like, I'll… I left on Wednesday, the last time I started on… Sunday, just because it's so long.
**Liudmila Molkova** 03:02 It is, yeah.
then maybe, I think I have something on Monday.
But I don't remember… Wow. That sucks.
**Trask Stalnaker (Microsoft Corporation)** 03:15 Yeah, time slots are only Tuesday, Wednesday, Thursday.
**Liudmila Molkova** 03:19 Oh, okay.
Oh, I have something on Tuesdays, but maybe… We do either Tuesday afternoon, or Wednesday?
**Trask Stalnaker (Microsoft Corporation)** 03:39 Tuesday is, oh, no, Observability Day is Monday, so Tuesday's conference.
**Liudmila Molkova** 03:46 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 03:48 So, yeah, whatever you prefer, Tuesday at 2 p.m, or Wednesday, we could do morning.
Or after 11 or 1.
**Liudmila Molkova** 04:05 Actually… Tuesday is all free for me. Maybe we do Tuesday while people are still fresh, like, 2PM?
Why not?
How doin'?
**Dylan Russell** 04:23 Yay.
**Trask Stalnaker (Microsoft Corporation)** 04:23 lined up.
**Liudmila Molkova** 04:27 Cool.
Do you want to present the notes, or I can present?
**Trask Stalnaker (Microsoft Corporation)** 04:35 Yeah, I can… present…
**Liudmila Molkova** 04:46 Do we have… a few trivial PRs.
I added.
So this… we need to unkip, probably, your…
**Trask Stalnaker (Microsoft Corporation)** 04:57 Yes, I'm pinging him right now.
**Liudmila Molkova** 05:01 Yeah, and the first two, we need approval from Dylan or Aaron.
Or both.
And these are the… three of you already agreed, or just moving things around.
**Trask Stalnaker (Microsoft Corporation)** 05:18 Yep.
And… I haven't thought more about the… the… the noun versus verb thing, the original, like, I actually like the operation name as, like, or at least the verb is how we have seen Like, database is, like, it's the verb, it's select, update.
Or I guess I could… anyway, I don't know. I haven't thought about it.
**Liudmila Molkova** 05:55 I'm in the HTTP post, the, messaging, send… So… and we… I think we have some guidance that the span name Should be, like, something like a verb.
Action and target, or something?
It's not… protection.
**Trask Stalnaker (Microsoft Corporation)** 06:18 Yeah, so, but you're thinking that we should… align the… Operation name with the metric name.
**Liudmila Molkova** 06:30 Good question. So, I was thinking about it, just because they are somewhat aligned.
But, given that we want, eventually, operation names to be freeform, like idiomatic to a certain, like, producer.
library, and it probably doesn't matter, they won't be aligned anyway. Like, can chat or… Text completion, or… Unrelated to inference.
**Trask Stalnaker (Microsoft Corporation)** 07:02 Okay.
That was… because I think my initial leaning… is… I liked the… noun names for the metrics, because they aligned with, like, operation duration, but I liked the verb operation names seem to align better with Semconv.
**Liudmila Molkova** 07:23 Okay.
**Trask Stalnaker (Microsoft Corporation)** 07:24 In my barely… Thinking about this.
**Liudmila Molkova** 07:30 Okay, I would imagine we keep… What do we keep?
I think embeddings is the one, so should we… Change it to embed and retrieve.
**Trask Stalnaker (Microsoft Corporation)** 07:45 O for the operation name.
Yeah, I hadn't thought about that a lot, that, yeah.
**Liudmila Molkova** 07:56 Or maybe we don't care that much.
Okay.
Let's… let's get to it once we do this round, and yeah.
**Trask Stalnaker (Microsoft Corporation)** 08:14 Okay.
**Liudmila Molkova** 08:14 Yay!
**Trask Stalnaker (Microsoft Corporation)** 08:15 Yeah, art schemas.
Who wants to drive the discussion?
**Liudmila Molkova** 08:27 I, I can, I try to make way, maybe we will start with the Or this one.
I think we agreed on this, this is non-controversial.
And we wanted to…
**Trask Stalnaker (Microsoft Corporation)** 08:55 2… Okay.
I can look at that…
**Aaron Abbott (Google LLC)** 09:01 Yeah.
I mean, seems good to me, I can approve it as well.
**Trask Stalnaker (Microsoft Corporation)** 09:11 Okay.
But this was pre… what I was trying to just get was… is… The concern… was your concern here pre-existing?
Is it… Related to what we were doing here with the… Or is it something easy for me to just change in this PR?
**Aaron Abbott (Google LLC)** 09:34 Yeah, I think it… I think it was the same thing. I think it was… the assumption was that these would be just, like, JSON strings.
I think that's why it says they should deserialize to an object. But in the case we're storing structured stuff instead, I don't think we need that anymore.
**Liudmila Molkova** 09:51 Oh, we still need it, because we need to tell that Because string is a valid any value, right?
We need to tell what to do if you think it's JSON but serialized.
But it's probably our token up to this pure.
**Trask Stalnaker (Microsoft Corporation)** 10:08 Sorry, can you help me find the, what you're sugi- what you're talking about, Aaron?
**Aaron Abbott (Google LLC)** 10:16 Yeah, I mean, so it should be for the audience.
It might be in the, Rendered Markdown.
**Trask Stalnaker (Microsoft Corporation)** 10:33 for… GenAI spans…
**Aaron Abbott (Google LLC)** 10:38 I guess it would be an Asian spin.
Hopefully this isn't a complete hallucination, but I… It's, it was definitely originally an AI comment, but I thought the goal was, yeah.
**Trask Stalnaker (Microsoft Corporation)** 10:58 Help me.
**Aaron Abbott (Google LLC)** 11:00 It might… it might be in the diff, like, it might be hidden in the diff.
Like, maybe just open the file separately. I can… Oh.
**Liudmila Molkova** 11:11 This should be for the two… call… arguments.
**Trask Stalnaker (Microsoft Corporation)** 11:18 Oh, is this… okay, here it is. The instrumentation should do the best effort to deserialize it to an object.
**Aaron Abbott (Google LLC)** 11:27 Yeah, so I, I can, I can poke through the history, but…
**Trask Stalnaker (Microsoft Corporation)** 11:31 Isn't this still accurate, though?
That's what I thought.
Because the argument… I mean, you still need to deserate, like, if they give you back a string.
**Aaron Abbott (Google LLC)** 11:44 Oh, okay, sorry, I was… maybe I was reading this as a note for the consumer, not for the instrumentation.
**Trask Stalnaker (Microsoft Corporation)** 11:51 Oh, okay.
**Aaron Abbott (Google LLC)** 11:53 Does anybody remember why it's added?
Yeah, does anybody remember? This is saying that the tool call arguments from the agent might be a string, and they should be deserialized?
**Liudmila Molkova** 12:06 So what… Interesting.
Yeah.
**Trask Stalnaker (Microsoft Corporation)** 12:09 Serialized into an any value.
**Liudmila Molkova** 12:12 Yes.
So when the two… when the model returns with two call arguments, It usually frequently returns a string.
And… At least, instrumentation sees it as a string.
And then the instrumentation should do its best effort to desperalyze it, because chances are it's an object.
**Trask Stalnaker (Microsoft Corporation)** 12:39 Preserialized is probably confusing the word that's confusing here.
**Aaron Abbott (Google LLC)** 12:44 Yeah.
Okay, yep, maybe it's orthogonal, we can just resolve it then.
**Trask Stalnaker (Microsoft Corporation)** 12:51 But yeah, it means deserialize into… a structured Object.
In this case, and any value.
**Aaron Abbott (Google LLC)** 13:01 Yep, got it.
I'll resolve it right now.
**Trask Stalnaker (Microsoft Corporation)** 13:06 Okay, cool.
Alright, next… Base64 for blob part…
**Liudmila Molkova** 13:37 I think we… I put it here because I think last time we talked about something, and maybe, Aaron, you wanted to check if… What's the… the better way to do it than JSON schema, or maybe we decided to just document it out, around… Oh, yeah, I think we talked about just not solving this, and just say that JSON schema is there for, I don't know, validation reasons for… And to brief, like, Outline the type we want to provide, not for actual serialization or deserialization.
**Aaron Abbott (Google LLC)** 14:17 Yeah, yeah, exactly. I think we can solve it later and just add some, some wording in the meantime that makes it clear, and then Yeah, I think… I think part of this, or, like, the way this came up was originally this sentence here, I think, was added for the remote upload thing, the object storage upload.
where we do serialize to JSON, but it's not necessarily… it could be Parquet or whatever, so… I see the argument for removing it, but… maybe we should write the encoding as an OTLP any value.
and say this should be expected to be bytes value in OTLP, if that makes sense.
**Liudmila Molkova** 14:57 Like, in the description.
**Aaron Abbott (Google LLC)** 14:59 Again, exactly.
**Liudmila Molkova** 15:01 Yeah.
I can create an issue for this and maybe send a PR.
**Aaron Abbott (Google LLC)** 15:08 For which part? For just the wording?
**Liudmila Molkova** 15:11 For the wording, and any other places where we need to document it more clearly that this applies to.
I don't even know how we describe…
**Trask Stalnaker (Microsoft Corporation)** 15:22 But it's not just what it regulates.
**Liudmila Molkova** 15:23 Yeah.
**Aaron Abbott (Google LLC)** 15:25 Yeah, we need OTLP schema. OTLP any schema.
Cool.
**Trask Stalnaker (Microsoft Corporation)** 15:37 Alright, disallow null.
**Aaron Abbott (Google LLC)** 15:45 A nice way to PR.
**Liudmila Molkova** 15:50 Did you send a pair, Ernie?
**Aaron Abbott (Google LLC)** 15:52 No, no, no, this one's been here since August, I guess, so…
**Liudmila Molkova** 15:57 Yeah, does it do what we wanted?
And if it does, maybe we should just approve it and load it in.
That's a lot of dogs.
**Aaron Abbott (Google LLC)** 16:10 Can you go to the models PY over Ship Trask?
**Trask Stalnaker (Microsoft Corporation)** 16:13 Yeah.
**Aaron Abbott (Google LLC)** 16:14 Yeah.
**Liudmila Molkova** 16:20 Oh, I think we went on the detour of exploring pedantic missing.
And since then, we… I think Paul agreed that We don't want to differentiate missing and null.
And maybe you would tell the PR order to just… do the… It would be, let's say my intent would be just string.
With a default none.
Would it be the way to make it not required in this schema?
**Aaron Abbott (Google LLC)** 16:58 I'm honestly not sure for Pydantic, but you're saying that we would allow… we would allow it to not be there, allow it to be null, and they would have the same semantics?
**Liudmila Molkova** 17:08 Right, I think this is where what we've been discussing so far.
**Aaron Abbott (Google LLC)** 17:12 Yeah.
**Liudmila Molkova** 17:13 Yeah.
**Aaron Abbott (Google LLC)** 17:13 That sounds good to me, and I have no idea how to do it correctly in Pydantic.
**Liudmila Molkova** 17:18 I will leave a comment, then, on the schema file, asking Author to achieve this outcome, and how it's probably… Less important. In model pi, it's not normative regardless.
**Aaron Abbott (Google LLC)** 17:34 Yep.
**Liudmila Molkova** 17:39 Okay.
**Aaron Abbott (Google LLC)** 17:45 So I guess the last thing there would be… I'll send a PR, I can do it today for… making some of the other fields… well, maybe I should wait for this one, but making some of the other fields Optional slash nullable.
The ones we discussed, like content, text, etc.
**Liudmila Molkova** 18:03 Maybe you just send the PR, because then we will… stamp it, and, like, I don't know if the order of this one will come back soon, or how long it would take us to, like, get to the… yeah.
**Aaron Abbott (Google LLC)** 18:19 Cool. I will… I will do that today.
**Trask Stalnaker (Microsoft Corporation)** 18:28 Alright, this is the… yes, we were discussing this last Friday.
With Felix.
Let's see, there were 3 PRs… So, one is splitting it.
**Liudmila Molkova** 18:53 I tried to make sense out of them in the table, in the notes.
**Trask Stalnaker (Microsoft Corporation)** 18:58 Oh, thank you.
**Liudmila Molkova** 19:02 So this giant… thing.
So… The absolutely minimal sufficient proposal is the 654.
it just allows anything. So, currently, we are only allowing object.
And it allows… Right.
Anything.
And this is, like… Maybe… It is what we will do, it's one of the viable options, I think.
I think the… yeah, this one… It is… not clear.
Because it only… Shows the… the object part, it doesn't show what to do with arrays.
I imagine this is the… Would be, with different type, type array, and then there is an array.
And then there is a list of them.
But it's like a union of… Discriminated.
values.
And if you compare, maybe useful to look in the value example JSON plus image.
and compare… Things.
Fair.
So… Yeah, there is the discriminator.
Value parts, or whatever.
And it's an array of the subjects.
Those different discriminators.
**Trask Stalnaker (Microsoft Corporation)** 20:55 Okay, and the minimal one is the tool result already in array?
Or no, this… it's anything, including an array.
That's a proposal.
**Liudmila Molkova** 21:08 Yeah, so whatever we have got from the tool, we just put into any value, to the best of our ability.
And with all the other three.
I think… We try to… we use the convention for this library on what this tool can return. Sometimes it returns type things that we can explore.
So, if we expect it to return a list of ports, Then we can… Do something about it, and… put them accordingly. So the first one does not look into the result at all, the other three… Try to parse it to their best ability, and it's just the difference is what they do with the things they recognize.
**Aaron Abbott (Google LLC)** 22:05 So I think…
**Liudmila Molkova** 22:06 Yeah.
**Aaron Abbott (Google LLC)** 22:06 Sorry, I was gonna say, I think for, like, Langchain and ADK, depending how we patch it, I don't think you have to parse, because they have, like, a specific convention for it.
So, so the, the Asian framework should… You know, assuming you patched it in the right place should differentiate them, like, natively, if that makes sense.
Gonna try to send this animal.
**Liudmila Molkova** 22:32 Yeah.
It will normalize them in some way.
**Aaron Abbott (Google LLC)** 22:41 Yep.
**Liudmila Molkova** 22:45 And… than 4… This first 654, it will be… Normalized for Langchain, but it will be different for OpenAI.
We're entropic, because we would not attempt to normalize anything.
**Trask Stalnaker (Microsoft Corporation)** 23:09 And can you draw the connection for me to the MCP… Tool cause that… I think my understanding was those always… the part of the spec, as Felix was showing this.
Includes both of these things. And… If that's… via, like, LinkedIn… Anthropic, whatever those APIs are, is that… Do they all expose What I'm trying to understand is how common is that format? Like, are most tool calls being done over MCP? In which case, you know, it might make sense to lean into that format and, you know, then something like this is kind of attractive to me.
Or, if it's not, then it's not as important.
**Liudmila Molkova** 24:12 Can you… there is a tab in the doc?
And there is a… Two colors out there.
And there is another sorry giant table with different scenarios.
So, to summarize, to answer your question, there are a couple of two or three cases, if, I remember correctly, where We… we have, like, both the… some JSON object, and some… List of parts.
And for example, Google ADK generate content.
You can see there is this temperature of 57.
And then there are typed parts, but this is a legacy API, it's not… it's not in the new version, Google Interaction, so… but Bedrock also has it.
So, can you see Jason temperature, and then image.
But they have the special JSON block, that nobody else has.
So, there is MCP, and there is Legacy Google API, and there is the Bedrock.
These are the examples where we can have either whatever object, or parts.
Or altogether.
**Trask Stalnaker (Microsoft Corporation)** 25:42 Okay, but with, like, OpenAI and Anthropic, if they're calling It's… non… If they're calling MCP Tools, do they get that?
Or…
**Liudmila Molkova** 26:02 If they're…
**Trask Stalnaker (Microsoft Corporation)** 26:03 Right.
**Liudmila Molkova** 26:04 if… It's even… more complicated. Let me think. So, let's say I'm calling MCP tool, then MCP Instrumentation needs to represent To call results somehow.
And there is some logic in, let's say, OpenAI that transforms this thing into OpenAI parts that are sent to the model.
And it's related, but somewhat separate. I think it's useful to record what your tool actually returned.
And we will also record what model received out of it.
And then you can compare and see maybe you had a bug, or you put things in the wrong place.
So… Interesting. Yeah.
**Aaron Abbott (Google LLC)** 26:57 I mean, Ludmila, that kind of sounds like the simplest option from the table.
Just record whatever came out of the… Tool function.
**Liudmila Molkova** 27:10 Yes.
Probably.
Aye.
I… I think it's… like… Duh… So what you're saying, if we tried to normalize, we would lose something that tool returned.
**Aaron Abbott (Google LLC)** 27:37 Maybe. I mean, I feel like, in a lot of cases, it's returning, like, a class.
Or something like that, so it's already… we have to lose information. It's not… It's not, like, just structured data. It's already gonna be abbreviated in some way.
**Liudmila Molkova** 27:55 And then, if we see, like, that… Let's say the tool result is a list of parts, and these parts are already provider.
Specific.
Things that we recognize for input and output messages.
it makes some sense to leverage them, and to have the same format. So if we… if we lose information in one place, we would lose it in the same way in another place.
But if we don't recognize it.
Then, we would record it as is, like, to the best durability.
**Aaron Abbott (Google LLC)** 28:33 Yeah.
**Liudmila Molkova** 28:35 I'm… I'm thinking we, like, even regardless of this, we kind of have to… Explore this object that we get from the tool, because apparently there is this convention which is error.
That you can… And in many libraries, you can Add specific properties to the result to indicate an error.
Or some other things. To call result, apparently, you can just put in the… Sorry, the call ID.
Or a function name you can put into the… output.
Do we keep it there, maybe? But we probably should also use it for… Other things that we have, like the span status.
Sorry, I'm making it more complicated.
**Aaron Abbott (Google LLC)** 29:39 Yeah, I wish Felix was here, because I… I kind of see the argument for not parsing anything, and then I see the argument for trying to parse it and normalize it.
It sort of depends, I guess, where you instrument.
Or, like, what layer the instrumentation is patching at, if it's within the framework, or if it's, like.
Lowered before it gets parsed by the framework.
**Liudmila Molkova** 30:04 I would actually… yeah, go ahead.
**Trask Stalnaker (Microsoft Corporation)** 30:07 I was gonna ask, what's consistent with, sort of, is… can we draw any parallel to input-output messages?
In terms of… don't… Wholesale, dump those in, or we inspect them, or… I don't know.
**Liudmila Molkova** 30:26 Did this… this… Parts part, if it's there.
becomes… It is appended to output messages.
By the framework.
Sorry, appended two input messages after the two call and sent to the model.
And they are in a rake.
But they are guaranteed to be an array.
And this object, I think the… it's very not ergonomic to have something that sometimes is an array and sometimes is an object. So I would actually prefer, like, the… the design, Aaron, you had, that we at least specified this.
And have the rubber.
That it's always an object, but then you can explore this object to see if it's an array.
Or… A single value, or both? Like, because why wouldn't it be possible?
**Aaron Abbott (Google LLC)** 31:35 So, kind of like 676.
**Liudmila Molkova** 31:38 Kinda. But then there is a question of, do we actually… parse the parts and try to normalize them. I think 676 attempts to do this.
**Aaron Abbott (Google LLC)** 31:52 Yeah.
So, spoiler, I approve 676.
**Liudmila Molkova** 31:59 Before…
**Aaron Abbott (Google LLC)** 32:00 before this discussion, but I kinda, I kinda like it, like, Because I think if it fails to parse, you would see whatever you expected to be in parts in value. So it seems like that use case is still there. And then when you looked at the, input messages from the next LLM call, you would see that it's not… not encoded how you expect, maybe it gets converted to JSON string or something.
**Liudmila Molkova** 32:30 I am… slightly worried about our ability to parse and normalize, because it's just so hard, based on what… every SDK does something internally very funky. Maybe what I can do, I can use some tokens to just prototype it in Python.
And see what… how bad it would be, and if it's visible, if it produces something meaningful and educates us.
**Aaron Abbott (Google LLC)** 32:59 Yep.
So, I mean, for… I just shared two links in the chat a little bit ago. I can tell for Langchain, it's pretty straightforward, and then for MCP, it's obviously pre-parsed.
It's pretty straightforward.
the LinkedIn org. Do you see where it says return multimodal content in the bookmarks on the right?
**Liudmila Molkova** 33:21 Yeah.
So, like… For each framework, we need to know what's expected there, what convention is there.
We need to check the type of what's returned.
If it's, least… We explore each element, if it's a list of parts we recognize.
We put that in parts.
What if there is one… Part that we don't recognize the type of.
What, what do we do with it? We drop it?
Do we put it in the value? Then… or if we put everything… if we… if we don't recognize at least something, we put it Everything in the value.
So you see what I mean?
**Aaron Abbott (Google LLC)** 34:27 Yep.
Maybe I could put… Dylan, I could ask you if you know the answer to this, put you on the spot. Do you know if the instrumentations in Python GenAI, do they see… Kind of before or after the tool call, like, is parsed by the framework.
Does that make… does that question make sense?
**Dylan Russell** 34:56 Yeah, I think mostly after.
**Liudmila Molkova** 34:59 Ghost!
Both. Because… because you see the after inside the next inference call.
**Dylan Russell** 35:09 Right.
And then…
**Liudmila Molkova** 35:14 Pretty decent.
**Dylan Russell** 35:15 That's cool.
**Liudmila Molkova** 35:18 Oh, so, like, you're saying that if the audit tool calling is there, then maybe it's already parsed.
**Aaron Abbott (Google LLC)** 35:26 Exactly, yeah.
So, like, in Langchain, I think we have callbacks, and I think they're already parsed. Like, we implement callbacks, and I think It's already parsed by the time it runs our callback.
That would be my assumption, but we can check.
**Liudmila Molkova** 35:46 It's… in normal case, it's a user application that's… poses… wait.
Auditor calling, yeah.
Okay.
I mean, maybe… Even, like, even if it… if it happens before the framework parses it.
we could say that in most cases, most interesting ones, for OpenAI Phantropic.
It's either everything are parts, or Nothing.
And… In most cases, we would be right with pudding.
The parts, or a value.
But if we don't recognize something in parts.
We could put the whole thing into value.
**Trask Stalnaker (Microsoft Corporation)** 36:58 What is, Evolutionarily, like, is there… Some… what would be the minimum we could do now that would allow us to evolve?
Trying to decide, like, if we can't… make this decision.
**Liudmila Molkova** 37:25 Then it's either that we allow anything at all, Or that we… Separated by… We have a wrapper object that says, okay, this is the everything.
were… This is the object part of it, this is an array part of it.
**Aaron Abbott (Google LLC)** 37:56 Yep.
**Trask Stalnaker (Microsoft Corporation)** 37:57 The… I'm worried about the… the anything case.
Like, how is… That… how do we evolve that if there's, like, how do you… No, then, say, we do add structure later.
I guess… Then it's a little bit more… You add a discriminator later, and you say the presence of that.
**Liudmila Molkova** 38:27 Yeah, but then we cannot discriminate her now and say, okay, this is everything.
**Trask Stalnaker (Microsoft Corporation)** 38:33 Sort of, where… I was wondering if that made sense.
**Aaron Abbott (Google LLC)** 38:40 I mean, for 676, we could just add new… Object keys, right?
Sh- it would be the same.
**Trask Stalnaker (Microsoft Corporation)** 38:47 Yeah, I mean, this one feels, of, like, evolvable… Because it's at least… Split into these… Two parts, and we can add more… Attributes to that object later.
**Liudmila Molkova** 39:06 than the value.
It's the same problem as with attribute. We need to… Specify that the value is everything or not everything.
Because here, the N676, the value is everything that are… is not parts.
And if we have… Alternative representation for… The whole object, then it would be… Well, I guess you can put it in the value, and the lack of parts means it's everything.
**Aaron Abbott (Google LLC)** 39:56 Yep, or we could add a new key if… The conception of tool calls changes completely in a year.
**Liudmila Molkova** 40:04 Yeah.
Okay.
Okay, so it sounds like 676… can be it? It's just I… I didn't review it before, because I… I think we need a better naming for this.
Properties and better descriptions.
But other than that, structurally, it seems… Evolvable, and it's… The 604 is not different from it, it's just that… Different representation of the same story.
**Aaron Abbott (Google LLC)** 40:42 Yep.
**Dylan Russell** 40:46 So, 676 is… Parts describes the schema of value.
No. Oh. No.
**Aaron Abbott (Google LLC)** 40:56 Perfect.
Parts… parts would be, like, if the tool decides to return, Like, content parts, which some agent frameworks support, and then value would be, like, a raw, structured data.
**Dylan Russell** 41:16 Value would be raw structured data. What is raw structured data?
**Aaron Abbott (Google LLC)** 41:20 Yes, maybe as an example, like, You can have a tool which returns, like, an image part.
**Dylan Russell** 41:27 Right.
**Aaron Abbott (Google LLC)** 41:29 Or you can have a tool which returns, like, the result of calling some API.
**Dylan Russell** 41:35 And we don't know what the part is.
**Liudmila Molkova** 41:38 We, we, we know, we could know, because the part is the… the object, That we know the type of.
And so the Google GenAI defines the type.
For this part. And we can check if it's the instance of this type.
**Aaron Abbott (Google LLC)** 41:58 Yep.
**Dylan Russell** 42:04 Okay. I don't… I don't get it, but that's okay.
**Trask Stalnaker (Microsoft Corporation)** 42:09 So what's the… I mean, what's the story here as far as why is it useful to extract the parts out of the response?
Is it because those are the same things that then get fed in as input messages? So it's sort of almost like a correlation thing?
**Aaron Abbott (Google LLC)** 42:29 Yep.
**Liudmila Molkova** 42:30 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 42:36 Sounds compelling to me.
**Liudmila Molkova** 42:38 Yeah, it sounds compelling. I don't know if it's… like… Absolutely essential.
But, yeah.
**Aaron Abbott (Google LLC)** 42:49 Yeah, I mean, at least for MCP, it's really straightforward, because it matches the data model.
And we've… we've said that MCP is, like, the, execute, execute tool spin, so…
**Liudmila Molkova** 43:09 Cool, so then, I'll make a pass on 676, maybe leave some comments, suggestions on the naming, and narrowing down the descriptions for things.
But… it seems we're trying, like, this is our favorite.
Approach, based on this discussion so far.
**Aaron Abbott (Google LLC)** 43:33 Yep.
**Liudmila Molkova** 43:38 Yeah, and I think Felix's, at least when we initially discussed it on Friday, Felix's favorite was the last one, 653, which is the same, but separates into two different attributes.
And I don't have very strong reasons, but I don't… I don't like it.
**Trask Stalnaker (Microsoft Corporation)** 44:04 Yeah, we have enough big objects, one… one less is… and we're talking about alternative mechanisms for storing it because of privacy and… and size, and so having one less of them seems… worth it.
And that's… All one concept, anyways.
And we've very much leaned into complex data structures already.
So we're not.
Paying that price.
**Dylan Russell** 44:37 Yeah.
**Liudmila Molkova** 44:39 Cool, so then we have next steps.
**Trask Stalnaker (Microsoft Corporation)** 44:43 Alright.
**Aaron Abbott (Google LLC)** 44:48 Cool.
Del Friday, I guess.
**Liudmila Molkova** 44:52 Till Friday, please review the PRs.
**Trask Stalnaker (Microsoft Corporation)** 44:54 Yep, I will, I will.
Check in… keep checking in with Ankat.
**Dylan Russell** 45:01 Alright.
**Liudmila Molkova** 45:02 Thank you.
**Trask Stalnaker (Microsoft Corporation)** 45:02 Thea?
**Liudmila Molkova** 45:03 Dear.
