SIG: LLM Semantic Convention WG
Date: 2026-07-07
Duration: 40 minutes
============================================================

## Zoom Recording Transcript

**Tom Yu (Alibaba)** 01:58 But.
Yep.
Aurora.
**Liudmila Molkova** 13:21 Hello! Hi, everyone!
**Steve Rao** 13:24 Hello, Rumiro.
**Liudmila Molkova** 13:28 I'm glad you're here.
Among at least 3.
But… Sorry, I'm like, Get started… Okay.
Oh, you have a bunch of topics. Wonderful.
**Steve Rao** 14:17 Yes.
**Liudmila Molkova** 14:25 Cool. Should we talk about Finnish reasons?
**Tom Yu (Alibaba)** 14:32 Okay. I, I am the… One who proposed these topics.
Yes, and I think you.
Maybe you have already read this.
PRs.
Right?
**Liudmila Molkova** 14:50 I've… yeah.
**Tom Yu (Alibaba)** 14:52 Yeah, and the first two PRs are about… clarification, I think. There is… Nothing new proposed.
But, because I am… I'm not the one who writes the instrumentation. I am the consumer, so I will be quite confused if The finished reasons are double recorded in both output messages and a dedicated Finnish reasons field.
So… So I think we should make the you know.
Finnish reasons feel authoritative or we just remove it.
That can… yeah.
**Liudmila Molkova** 15:47 Demetri.
**Tom Yu (Alibaba)** 15:48 I reduced that.
**Liudmila Molkova** 15:49 The redundancy rate.
**Tom Yu (Alibaba)** 15:51 Yes.
**Liudmila Molkova** 15:52 Mmhm Yeah, this makes sense. I probably… I will need to pull up some history, because there might be some reasons why it is this way.
But yeah, I, I think it's a good idea to clean it up.
**Tom Yu (Alibaba)** 16:10 Yes, and yeah, and current proposal is is to make it authoritative and remove the redundant.
things in the output message. And another PR is about the system instructions.
It's, yes, you can see you do not need to change.
the document that the document is in the same page, but a different tab.
Hmm.
**Liudmila Molkova** 16:44 Okay.
**Tom Yu (Alibaba)** 16:45 Okay.
Yep. -H I think most… more than, error on APIs.
have already separate system instructions from user Prompt.
Yeah, it…
**Liudmila Molkova** 17:08 It's more like they provide both.
**Tom Yu (Alibaba)** 17:13 Yeah, and I think the recommended way is to use a dedicated field, and that makes user cannot override the system prompt, and the system won't forget system prompt.
**Liudmila Molkova** 17:29 Yet, it was a user.
I can write a code that will set system instructions, the specific field.
And I would add a message, input message, with system role.
And that's how things are different. Everything was input message. Everything that went into provider API as input message.
is in input messages. The specific explicit field for system instructions goes to system instructions.
We cannot merge them because these messages can appear anywhere in the chat history.
It can be the last message, the first message, and our goal.
For observability is to capture what happened, not what recommended way is right.
**Tom Yu (Alibaba)** 18:15 Yes, but That's… quite, I think… oh, so… so why there is, separate system instruction, because some APIs just provide a separate field to yeah.
To write, write, write it here, right? Yeah.
Yep.
And… Okay, but… But I think, that… Maybe there is another point here.
the system instructions The structure is… different from the one in the messages. It doesn't have rope part.
I just record parts.
**Liudmila Molkova** 19:06 This is…
**Tom Yu (Alibaba)** 19:07 So…
**Liudmila Molkova** 19:07 where there is this special field.
**Tom Yu (Alibaba)** 19:12 Yes, but…
**Liudmila Molkova** 19:13 It doesn't cover.
**Tom Yu (Alibaba)** 19:14 the, the, the, the scripts.
the scenarios.py, those scripts aren't right. Their structure is not right.
I think you can…
**Liudmila Molkova** 19:37 We we have the alternative source of information for this one. We have adjacent schema.
And see what's in there.
So, okay, there is a generic part, the text part.
So it's… it's a… a list of… Parts. Let's take a look at the Python models for this.
Sorry.
So it's a union of text part and generic part, and the text part…
**Tom Yu (Alibaba)** 20:16 This one is correct, but the scenario.py is not correct.
They are not, right.
**Liudmila Molkova** 20:23 Oh, that's good.
**Tom Yu (Alibaba)** 20:24 If you read the… pull request, and the difference is quite clear.
And…
**Liudmila Molkova** 20:32 Yeah, I think what your pull request proposes is to merge input messages with system role and system instructions. And this is.
**Tom Yu (Alibaba)** 20:42 There are two things, yes. And actually, I found the problem in the structure, in the JSON structure.
Yeah, you see, the difference is quite clear, and the…
**Liudmila Molkova** 21:01 So wait, so this one, here. So if it depends on what's in the example.
And.
So there is a dedicated field systems to okay.
**Tom Yu (Alibaba)** 21:34 If you scroll down and see the scenario.py, these PYs, And.
They they don't generate correct.
system instruction…
**Liudmila Molkova** 21:49 I assume that that's that's fine.
**Tom Yu (Alibaba)** 21:51 Okay.
**Liudmila Molkova** 21:52 fix it. But I I'm not sure like what is if if there is something else in this PR.
**Tom Yu (Alibaba)** 22:01 Yes, there is something else. It proposed that we should extract system prompts from the input, but as you stated that The system prompt can appear anywhere, so we can't do this, right?
So I think we maybe we should. Hmm.
Simply separate these things and make this PR only fix the.
structure problem.
**Liudmila Molkova** 22:34 Awesome, that's great.
Okay.
**Tom Yu (Alibaba)** 22:40 Okay.
And that's all for the first two PRs.
And,
**Liudmila Molkova** 22:49 Nice. Thank you.
**Tom Yu (Alibaba)** 22:50 Yes.
Yeah, let's talk about… the… message delta attributes.
Hmm, okay.
Yes.
And Actually, we are implement some message recorded for… AI coding agents, and these agents using hooks to make their prompts observable.
Hmm.
However, This hooks only.
provides.
What… what is… what's new message?
And they don't provide the whole context.
So, what we record is… Current… new input message. So that's what I called message delta here.
And… I think, this is… You know, Not only way, not only.
Where it can be useful, because… Hmm. Agent.
Authors can use this field to Emit spans, and maybe it… Does only need to record.
the new message.
Because recording the whole context can be very… can be… have a very high cost, right?
And if the… If the agent runs for a very long time, the The about 90% context is redundant, right? That's…
**Liudmila Molkova** 24:45 Mmh.
**Tom Yu (Alibaba)** 24:47 That's why we have a quite high cash… Cash rate, right?
So… So, this… PR, in this PR, the messages data is proposed to just to record the new message in the in the step, not the whole context.
And I think that's, if… If we can, have the conversation ID recorded correctly and know about the whole context, we can compress the whole… Yeah.
trajectory.
Much smaller.
**Liudmila Molkova** 25:42 Yeah, so I think the way this friend is defined and used is that you put all information you have.
So, for example, in open AI responses. Api, you can keep the the state on the Model side.
**Tom Yu (Alibaba)** 26:02 To the world.
**Liudmila Molkova** 26:03 You can.
**Tom Yu (Alibaba)** 26:03 That's.
**Liudmila Molkova** 26:04 And you can just provide the new messages.
And, we still populate GenAI input messages, because those are the messages that were provided.
at the time. Right? We we don't know what happened before. If anything has happened before on the instrumentation side. So when you the the only thing you know is just the the new stuff.
Then this message is still this. This attribute is still used currently.
They can clarify it better. The I get, I totally get the concern with redundancy. It's just, it's very hard to know what delta is. How, how do you know?
Practical in the instrumentation.
Assuming.
**Tom Yu (Alibaba)** 26:55 Do you have.
**Liudmila Molkova** 26:55 You have the full history.
**Tom Yu (Alibaba)** 26:57 And.
Yeah, if I am not there… Agent author. It is quite difficult because I have to keep the context, or at least the harsh of context. And in my context.
Object, right? And when the model responded, I have to append the output to the… harsh at the the harsh Let me state it that way. We can have, quite light-weighted, light-weighted the way to record the context to compare them. For example, we can yeah.
record each messages, Hashi.
And… On the next round, we can append the newly You know, respond, you respond harsh.
To the first hash, like, just like, like how blockchain did, right?
Yes.
And… if the… Yes, and if them.
Hunch matches what?
what the whole context, oh.
if this hash matches the whole new input message except the last one.
And this means the context haven't been changed. And we can just record the last one in the message data.
And… And in this way, we can… Reduce.
reduce a lot of what we need to record. And if I am the Agent also.
I can control the… I can… I'm the one who compiled the… Prompt. So, I can just use this message data to record what the new input is.
So I… I think… the call, the semantic convention isn't Mmm.
Bonded to the… instrumentation.
Implementation.
So…
**Liudmila Molkova** 29:42 So what you're saying that you.
**Tom Yu (Alibaba)** 29:43 I'll wait.
**Liudmila Molkova** 29:44 You're you're agent.
Then you can, even if you're writing the generic instrumentation, you can have some algorithm that, I don't even know what… okay, so you would… Take the list of all messages you've got.
you would compute a hash of it. Then you need to compute hash of the Per previous combinations.
Not sure what would you match against, or if you're… So let's.
**Tom Yu (Alibaba)** 30:20 Yeah, I think we have message one, respond one, and message two. Okay.
And Messenger 1 can have a Hashi, and… And the message… Respond one can have a Hashi.
we take the first hashi, and I made a mistake. Yes, the 1st the 1st message can can calculate a Hashi, and the Hashi plus the second, the first messages respond can create a Hashi.
Right.
And this is the… previous context, and.
**Liudmila Molkova** 31:03 So, okay.
**Tom Yu (Alibaba)** 31:04 Okay.
**Liudmila Molkova** 31:04 Can can you give me a sec? Let me see if I'm on on catching up with you. So let's break it down in a couple of different scenarios. The 1st one is inference instrumentation.
and then engine instrumentation.
So, the inference instrumentation, I have a request, I'm patching, patching operation.
I see, 3 messages, in the input messages that I'm about to send to a model.
So, I don't know which one of them is Delta?
Right?
So maybe this, maybe all 3.
Right? Maybe, maybe there is, Well, maybe somebody added 2.
Well, you don't know because there could be a bug or maybe it's intentional.
So you don't know which one of them is Delta, you kind of have to assume.
Or maybe you would maintain a hash for each message.
As you're saying.
And then you would maintain, you would need to hash, let's say, this message and look up if you've seen this message before and maybe hope that it belonged to the same conversation. But if you've seen this before, you get back to the previous message. And then finally, you would need to compute a hash of Like, total thing.
And then make sure it's the same one.
Right. Because just to understand that only Suri was in the delta. I'm not saying it's not doable, it's just compute intensive and it could be an opt in feature and inference instrumentation, but it's it's very compute intensive.
**Tom Yu (Alibaba)** 32:51 Yeah, because my network makes me quite difficult to… Edit this document now, and…
**Liudmila Molkova** 33:03 Oh, sorry.
**Tom Yu (Alibaba)** 33:03 I think this is not, This is not the algorithm. Actually.
Used, right? And, but at least one thing I I think.
That that could be stand there is that.
the… Agent author.
can use this… Field to record only the new messages.
Just like… Cloud Code hooks, or Codex hooks do.
They do only emit New message in this round, not… the whole context.
**Liudmila Molkova** 33:50 Yeah, so then it becomes the only place where it can be reliably populated without sufficient overhead.
is manual instrumentation.
And, like, when you say agent instrumentation, there is automatic agent instrumentation.
right? It has the same problem of as inference. It's just hard to Figure out what delta is.
**Tom Yu (Alibaba)** 34:18 Yes, the agent can be quite difficult. Agent instrument can be quite difficult, because sessions can be parallel. It at least have to maintain these dates for our session. First, all the sessions, and the second, each session have the previous message Hashi.
Yes, and I think that's enough. Just think about how blockchain do. You only need to know the last hashi, so they know everything hasn't been changed, right?
So they don't have to record all the messages hashes. Only one hash is enough.
**Liudmila Molkova** 35:07 I understand the goal. I I'm questioning how we can get there.
And if you want to… say that inference instrumentations or auto-instrumentations for inference libraries or Agentic frameworks like LangChain would calculate it. You could suggest an algorithm. You don't have to. You can say this. They can provide this as an opt in feature and leave it up to instrumentation to decide how.
And then where it lands naturally is manual instrumentation, right?
You're saying that it's not the auto instrumentation for something like Blankchain that would do it for you, but if you, write your code yourself, then you can, Popular Delta.
on manually created… Spans.
Unfortunately, this, the idea of manual, conventions for manual instrumentations, it's.
It's just nobody would follow them like you're like.
You're better off just doing your own thing.
**Tom Yu (Alibaba)** 36:29 Mmhm.
Maybe, yes.
But the goal of the semantic convention isn't It is to unify them right. However, unfortunately.
**Liudmila Molkova** 36:44 The goal is not to unify everything, the goal is to… Have instrumentations produce consistent telemetry.
And, manual instrumentations or.
Prone to all sorts of issues.
I'm not opposing this attribute. I'm opposing the idea that we target manual instrumentation as the goal.
If we do this, we will never agree, because there are… millions of people who implement things and they have different needs. And if we talk about like libraries, like link chain, there is plenty of them, but still.
They're very similar.
**Tom Yu (Alibaba)** 37:29 Yeah.
I agree with that. But you know, current Trace.
is… Too big for… Long conversations. Too many.
**Liudmila Molkova** 37:45 Absolutely. So if you want to introduce an attribute, the way I see it, it works is that you would suggest.
You don't need to actually suggest an algorithm in the semantic conventions, you can propose it in the PR title, but it can be anything, it doesn't matter, as long as this algorithm is Consistent within one instrumentation. That's fine, right?
And then we would say that this delta attribute is opt-in.
And instrumentations may support it.
Right.
And then it also becomes available for manual instrumentations.
**Tom Yu (Alibaba)** 38:34 Mmhm.
**Liudmila Molkova** 38:40 Cool, let me take some notes, Cool. Sorry we didn't get to Hu Sheng's topic, and I didn't have a chance to look. Wow, that looks amazing.
**Steve Rao** 39:29 Yes?
This is not an issue, just a block.
Pushing a blog, and you want to, post on the hotel official website in the future. So he want you and other maintainers have him to review the blog. If you and others have any question, you can leave the comments.
Yeah, in this Google Doc documentation.
**Liudmila Molkova** 40:03 Awesome.
Yeah, thanks. I think he pinged us to review, and I didn't yet, but I'll take a look today. Thank you.
**Steve Rao** 40:13 Okay, thank you.
**Liudmila Molkova** 40:14 Okay, thank you for coming. It was great to meet you, Tom.
**Steve Rao** 40:18 Thank you. Oh, yeah.
**Tom Yu (Alibaba)** 40:20 Nice to meet you too.
**Liudmila Molkova** 40:22 Okay.
Thanks. Okay, see you next time.
**Steve Rao** 40:26 See you next time.
**Tom Yu (Alibaba)** 40:26 See you.
