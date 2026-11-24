SIG: GenAI Semantic Conventions and Instrumentation Stability
Date: 2026-11-23
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 02:08 Hello. Hi, Trask.
**Trask Stalnaker (Microsoft Corporation)** 02:10 Ayy.
**Liudmila Molkova** 02:12 I met.
**Matt Spiekerman** 02:15 Huh.
**Trask Stalnaker (Microsoft Corporation)** 02:18 I didn't do my homework.
**Liudmila Molkova** 02:20 Great.
Weekend is not a great time to do homework.
Well, they expected it from us at school, right?
**Trask Stalnaker (Microsoft Corporation)** 02:36 What's that?
**Liudmila Molkova** 02:38 At school, they expected us to do homework on weekends.
Bye.
So, I think… Oh, Erin, you're here.
**Aaron Abbott (Google LLC)** 02:59 Yep.
**Liudmila Molkova** 03:02 I was looking into what we have left.
From the stabilization perspective.
And yes, there are quite a few things.
But… If we look… Thanks, Trask, for this.
**Trask Stalnaker (Microsoft Corporation)** 03:25 That's a cool one.
**Liudmila Molkova** 03:29 Yeah, so we have a few things that are not parts, but a lot of them are around parts.
I think we need to make a push to fix the parts things.
Because if we want to do RC by the end of the year, it's probably the biggest… area that we… Didn't clean up yet, and the rest is… Seems to be less important.
Or not that less important, but we can make progress in parallel.
So…
**Trask Stalnaker (Microsoft Corporation)** 04:03 And I… I over… possibly over-labeled things. I tried to be more, So some of the things may not… That are labeled with stabilization wave, we may decide aren't part of the stabilization requirement.
**Liudmila Molkova** 04:21 Can we then unlabel this one? The declarative context?
**Trask Stalnaker (Microsoft Corporation)** 04:25 Yeah.
Are you on an iPad? The form factor.
**Liudmila Molkova** 05:00 No, it's just, I am on a small screen, and I'm trying to show both the GitHub and,
**Trask Stalnaker (Microsoft Corporation)** 05:06 Oh, the notes, yeah.
**Liudmila Molkova** 05:09 Yeah, well, you've…
**Trask Stalnaker (Microsoft Corporation)** 05:10 Oh, the… yes, yes, I understand.
**Liudmila Molkova** 05:16 Yeah.
Okay, thank you, Mr. Speaker.
Okay, so then… A lot of the things here are related to parts… or maybe we should also remove this one from the stabilization effort, because we… the suppression is implementation detail, and we do this in Python and JS.
**Trask Stalnaker (Microsoft Corporation)** 05:44 I'm good with that.
**Aaron Abbott (Google LLC)** 05:50 I think on this one, we had, triaged which ones were stability blockers, and there was… 1, 2… one… only two left, I think? But maybe…
**Liudmila Molkova** 06:03 Which one?
**Aaron Abbott (Google LLC)** 06:05 I sent it in chat, it's issue… if you open Issue 527.
**Trask Stalnaker (Microsoft Corporation)** 06:13 Oh, for the part, specifically.
**Liudmila Molkova** 06:19 Yeah, I added a couple today.
To this list.
**Aaron Abbott (Google LLC)** 06:24 Oh, okay.
**Liudmila Molkova** 06:30 Yeah, this one.
So, maybe we can chat about the one, the PR, that you have, Farron, the 688, I think?
**Aaron Abbott (Google LLC)** 06:44 Sure.
I'm, I saw Trasky love some comments, and I'm… updating right now, I think they're pretty… Minor, though, right?
**Trask Stalnaker (Microsoft Corporation)** 06:54 Yeah, I don't remember leaving anything important.
**Liudmila Molkova** 07:15 Yeah, the… the only big discussion I think, Aaron, me, and you had on this is the optional versus,
**Aaron Abbott (Google LLC)** 07:24 No, yeah.
**Liudmila Molkova** 07:25 Now, and it can be a separate discussion, it should be a separate one.
**Aaron Abbott (Google LLC)** 07:31 Okay, sounds good to me.
Just in terms of… I think all these comments, pretty much, are… Because it's kind of vague where the, like, description moved.
So, what I'm planning to do is, the documents in the JSON schema, like, next to the field, so… For example, You know, like, if, for example, text should be there on a text content, or a text part, it would say this should be populated inline instead of, I think it's kind of in the YAML right now, which is a bit confusing.
**Liudmila Molkova** 08:11 Yeah, sounds good to me.
**Trask Stalnaker (Microsoft Corporation)** 08:13 Yeah, I'm fine with however you want to… I mean, I'll approve it.
**Aaron Abbott (Google LLC)** 08:18 Okay.
**Liudmila Molkova** 08:22 Cool.
Okay, so Dan, What else do we have mentioned here?
And maybe we'll tackle this some other time.
Decided now.
I… I think we need to… Finish the two-call response.
And I've been pinging Felix, Felix, if he would return back to it, and he's not replying.
So, I'm thinking maybe either… just go and create a new PR based on this one, with his commits, and then do things on top of it.
So we can review it, and yeah, go ahead.
**Trask Stalnaker (Microsoft Corporation)** 09:13 Makes sense.
**Aaron Abbott (Google LLC)** 09:15 Do we… You have a good… like, are we all decided on this one versus… I don't remember the exact number, but the other one, which had two attributes on the span, instead of having one attribute with two, keys in the payload?
**Liudmila Molkova** 09:33 I think… yeah, go ahead.
**Trask Stalnaker (Microsoft Corporation)** 09:35 I think we all seem to, at least initially, prefer the single attribute.
For me, it was sort of about… That's, Having one thing to route, like, because it's a content, it's a big content thing, one thing to… Route, report, hook… the hook stuff, the references stuff, the… Collector routing stuff.
Seemed to make sense to keep that all together.
**Aaron Abbott (Google LLC)** 10:23 Yeah, I think that was kind of my… I couldn't… I was having a hard time, like, coming up with answers to Felix's specific concerns on 676.
like, I was thinking about… How, for input and output, we make separate attributes, and it feels a little arbitrary, but… I agree with you, like, my intuition was to keep them together, because it feels like it's logically the same thing to me, and it's just kind of… Two… two variants.
**Liudmila Molkova** 10:51 I don't even think it's comparable. Input and output are different objects.
They are available at different times. We could, in theory, even send them to different events, or one could be present, another not.
**Aaron Abbott (Google LLC)** 11:08 Yeah, that's true.
**Liudmila Molkova** 11:12 Or, like, decision models would have inputs as normal, but output something special.
**Aaron Abbott (Google LLC)** 11:20 Okay.
**Liudmila Molkova** 11:26 Okay, so I'll take connection item to… Take this one and polish it.
And what else did I want to bring up?
So let's take a look at here, Sharon, actually, the tracking one.
So, the 6 size8 would resolve this, right?
**Aaron Abbott (Google LLC)** 11:56 Yep.
**Liudmila Molkova** 11:58 And then… the… Felix's PR would resolve this one.
So we are still having… oh, this, this is tracking the null versus…
**Aaron Abbott (Google LLC)** 12:12 Yeah, that's the null one.
**Liudmila Molkova** 12:13 Yeah.
Okay, so then… I… created, this front, and it… it is almost solved by 6X… 6… 8, 8… But I have a PR… That is in draft, because I want to build on 688.
to… Populate the role as it was provided by the provider.
Because we currently… it's required, and we fake it.
And we'll also try to normalize.
And we can kind of debate whether we should normalize or not, but then we kind of lose what… what was there in the… What provider gave us.
And it doesn't seem like It's super critical to know what the role was.
You have input messages, you have the… Parts that describe things.
So… I don't know if I need to normalize rows at all.
**Aaron Abbott (Google LLC)** 13:24 What did you mean it's not important? You meant for normalizing it?
**Liudmila Molkova** 13:29 Yeah.
Like, the only place where normalization is helpful is, like, the chat view, and you see, like, user assistant.
user tool… assistant, right? Something like this.
And… It's… essentially arbitrary.
What are the strengths? Who talks to whom?
So, we can… let the 688 merge, and then maybe we can discuss more on Wednesday, and it would also be good if you folks think About the normalization for roles.
Yeah, the one thing I want is to not… to ask Instrumentation is not to fake it.
**Aaron Abbott (Google LLC)** 14:32 Do you… can you remind me when… who doesn't set role at all? Is it, like, default to user for certain APIs?
**Liudmila Molkova** 14:41 Yeah, so… OpenAI, that, chat completions.
sets them. There are a bunch of things that are… not even messages, and this is the other thing I want to discuss later, like.
Approval request or something.
Alright.
And… OpenAI on Messages has the role, but not all the… Items we put on messages are… have roles.
Oh, no two calls per function call.
And there is function call output, but also no role.
Then the real time the same. Then Tropic never has a tool role.
It has special block for tools, and we represent them with tool parts, and from tool parts, you can figure out that they are More tools, same bedrock.
same Gemini… Same Gemini Life!
But OpenAI compatible ones and inspired by them have to grow.
**Aaron Abbott (Google LLC)** 16:02 Yeah, I guess the only value in normalizing them is, like you said, if you're trying to display a UI, it's really helpful, but I guess it's not really the instrumentation's concern, like, your UI can figure it out based on The data it supports.
**Liudmila Molkova** 16:18 And we can probably normalize, like, model to assistant between these two, I don't know.
**Aaron Abbott (Google LLC)** 16:27 Yeah.
Okay, I'll take a look. I seem to remember that some of them also had, like, default behavior if either it was Empty on, like, a text part, or if, You used a string that wasn't user, maybe it would always treat it as model, so I can… Trying to dig that up, but… Sounds good to me.
**Liudmila Molkova** 16:52 Great.
Take a look. And then, on the related nod, So… the… Maybe we're just looking here.
So let's say we have a model… Open-hair responses.
They have, for example, input.
And it can be a bunch of different things.
And among this input item lists.
There are messages.
That contains raw different sorts of messages.
But there are also the two coals.
Here.
And a lot of other things.
For example… Our configuration update is somewhat representable.
Let's see what we have here.
The approval request ID, yeah, that's the one.
Or item reference.
So, these things are not representable with our chat message. So the tool calls R, because they are parts.
But… The… something like approval request ID is not.
Let's see if we can find it there, SMCP approval request.
So, it has some structure.
which does not… Which is not a part of any sorts.
And we can, try to represent it.
As such… Your metric.
It's so complicated, actually, our schema is difficult.
This is our… Chat message… Okay.
So, the chat message.
It is a list of parts.
And that's the problem name. Both… all 3 are going to be optional, right? From your PR688, right?
So, like, if we try to model this, we have two options.
We can model it as a part, horror.
We can model it as, Some other thing that does not contain parts.
So what I'm proposing is that the… Chat message stays as it is, it's the message.
But we make another higher level container for it to its discriminator, and we would say, okay, this is a chat message, or this is a message.
And we would have a generic item, similar to the generic part, that would represent something else that does not have parts.
And that's the proposal.
**Aaron Abbott (Google LLC)** 21:01 Interesting. I'm trying to… I feel like we… we did kind of discuss this when we were doing this at first. I guess the OpenAI schema is a bit flatter, right? Like, the… MCP approval, for example, just goes at the top instead of in part, and I… I guess the approach we've been taking is to just jam it into the parts.
Is there… is there a reason that one… that doesn't work if we do that?
**Liudmila Molkova** 21:34 Let's see.
Get back here… So… there is… Hmm, message.
And there's a typed message.
So we model this.
And there is… Let's say File Search, and it has this type.
So we, at some point, decided that the tool calls… Go into parts.
Right.
Okay, so this is the message.
You're saying that we can find means for it to go into parts.
**Aaron Abbott (Google LLC)** 22:42 Yeah, especially if we don't require, roll.
Because if I understand right, you're also kind of suggesting to add… Add, like, nesting layer above it, or just add type to it as it is, and then keep the nesting structure, like.
We still have list of content, and then content.
We'll just have type.
**Liudmila Molkova** 23:06 Yeah, so I think we need a discriminator.
So… Completely lost now. If we look into our current model.
**Aaron Abbott (Google LLC)** 23:22 Hmm.
**Liudmila Molkova** 23:24 It does not have a discriminator at all.
It does, it won't have anything required, so it would be like a generic part that everything fits it.
And without discriminator, we just cannot use it, so parts… we would need to make parts required, or add a discriminator.
**Aaron Abbott (Google LLC)** 23:49 Parts has, right?
**Liudmila Molkova** 23:52 Part has one individual part, but the message does not.
So I think it should have a discriminator.
And if we had a generic part.
At least we'll have the means to represent something else.
Sorry, not generic part, generic message, generic item.
**Aaron Abbott (Google LLC)** 24:35 Yeah.
I think maybe I'll, I'll poke around. I think we did discuss this when we were doing the original structure, and we were… because we were looking mostly at, like, Anthropic, maybe Cohere, Gemini, and OpenAI, and then I think what we… we chose what we had.
knowing kind of the caveat that we were putting parts, OpenAI stuff, into parts that was actually at the topple, so… Just so I can, track down the decision, maybe I'll have a look through the history.
**Liudmila Molkova** 25:07 I mean, imagine… even if we decide to put all of those things in parts, which is fine, which probably is at least consistent with what we do for tools reasoning and so on.
Right. We… if we have a pop… if we have a… Type that doesn't have any required properties.
We are not describing any schema.
Toe?
**Aaron Abbott (Google LLC)** 25:33 Yeah, that's fair.
**Liudmila Molkova** 25:35 And, like, it's not extensible.
**Aaron Abbott (Google LLC)** 25:38 Yeah.
**Liudmila Molkova** 25:39 Like, de facto, you would use parts as a discriminator for… For, for… this type. We can work around this, but then… Yeah, and just from the long-term evolution perspective, if we do the generic part, we should also have the generic message or generic item.
**Aaron Abbott (Google LLC)** 26:02 Okay. Yeah, I see what you're saying.
Cool.
**Liudmila Molkova** 26:15 Yeah.
I don't want a giant… Conflict. But then, can we solve 6x6688 without this?
Well, we can name them all optional, and then introduce the required property later.
Yeah, so then let's focus on 6Actade for now.
Then we'll try to figure out the raw thing, and this can come in parallel, and the tool call responses… Sorry, tool call result is independent.
**Aaron Abbott (Google LLC)** 26:48 Yep.
That makes sense to me.
**Liudmila Molkova** 26:57 Cool.
Okay.
**Trask Stalnaker (Microsoft Corporation)** 27:02 Aaron, just ping me after you, reply, or resolve, or whatever you choose to do with my AI feedback, and I will… Look once more and approve.
**Aaron Abbott (Google LLC)** 27:17 Okay, sounds good.
**Liudmila Molkova** 27:21 We have a couple more minutes, so this is what we have left from the previous one.
Trask, you mentioned you didn't have a chance… Do you want more time to think about this?
Right.
**Trask Stalnaker (Microsoft Corporation)** 27:35 Yeah.
**Liudmila Molkova** 27:37 Yeah.
Quay.
And then… So, we talked about this last time. Probably need more time to digest.
**Aaron Abbott (Google LLC)** 28:06 Is this… sorry, I haven't seen that one yet. Is this one for stability, or…
**Liudmila Molkova** 28:12 For Stability, yeah, because we… We have the finished reason, finish reasons on Agent Span as an indication of, How it ended, but it's… It doesn't fit nicely, and, like… It's one of the consistent fightings across all the instrumentations that they don't populate it.
Open telemetry or external ones.
**Aaron Abbott (Google LLC)** 28:38 Okay.
Do we consider doing, like, a separate GenAI.agent.
Response.finish reasons kind of thing.
**Liudmila Molkova** 28:48 So I'm… Tentatively proposing the operation, that status.
I guess it would represent something, like, in progress as well.
Where, I don't know, budgets exceeded, or something like this.
that Finnish reasons does not necessarily represent well, or require section in, like, in human-developed things.
Yeah, I don't know about the agent specifically, because Just feels like… in A2A… well, A2As also… but, like, in case of inference.
when inference is still in progress, you still need some status to capture that it is in progress. We currently have response status for this.
And we can reuse it.
But then, like, there are other questions, so I'm thinking either reusing this or adding a new one instead of the response.
**Aaron Abbott (Google LLC)** 29:54 Okay.
Yeah, that makes sense.
**Liudmila Molkova** 30:03 So then we are kind.
See y'all tomorrow, maybe even today, we have a call with a pack, folks later.
**Trask Stalnaker (Microsoft Corporation)** 30:14 Is that… did we do that every week, or every other week?
**Liudmila Molkova** 30:17 Every week.
**Trask Stalnaker (Microsoft Corporation)** 30:19 Every week, okay.
**Liudmila Molkova** 30:22 5 GenA calls a week.
**Trask Stalnaker (Microsoft Corporation)** 30:25 Oof.
**Liudmila Molkova** 30:28 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 30:29 Alright.
**Liudmila Molkova** 30:30 Have a good day. Bye.
**Aaron Abbott (Google LLC)** 30:32 Yo.
