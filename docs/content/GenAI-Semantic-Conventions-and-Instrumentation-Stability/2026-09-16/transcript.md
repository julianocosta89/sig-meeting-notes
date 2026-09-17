SIG: GenAI Semantic Conventions and Instrumentation Stability
Date: 2026-09-16
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 01:31 Hi, Siri, how are you?
**Siri Varma** 01:33 Doing good. You?
**Liudmila Molkova** 01:35 I am doing fine, thank you.
**Siri Varma** 01:39 I had a quick question. I was looking at the board, And, the stabilization board.
And then, or Trask is also here. So, one question I had was, there was status post-stabilization, and there are to-do. Are the to-do ones that we should start picking up, and post-stabilization, we leave them, or no?
Second.
**Liudmila Molkova** 02:03 Yeah, in general, yes, that's the case. I… the things in to-do might be in the state that is… like, hard to work on yet. So, if you're interested in something.
Maybe we can discuss what's, like, actionable, what's ready to go, because some of these items are very complex, and some of them are actually ready to go.
**Siri Varma** 02:31 I see, so… Okay, makes sense.
**Liudmila Molkova** 02:35 Sorry, I… I might need to jump on a call, I need to take a phone call, so Trask, if you can present, I will be out for maybe 5 to 10 minutes, sorry about this.
**Trask Stalnaker (Microsoft Corporation)** 02:45 No problem. Hi, bye.
**Liudmila Molkova** 02:47 No, no, no, I'm here. I will need to take it at some point.
**Trask Stalnaker (Microsoft Corporation)** 02:50 Oh, gotcha, okay. I'd seen your message earlier that you were always surprised to even see you here, but got it, Emil.
**Liudmila Molkova** 02:58 Oh, the message was for the Tuesday call, I think.
**Trask Stalnaker (Microsoft Corporation)** 03:01 Oh. Yeah.
Yes, I will share.
Let's see, so this is what we discussed on Monday, and… Cool. I don't think we necessarily need to discuss Here, just, yeah.
Have people look at it, but, I think it's a good… compromise.
Yeah, I think it would be good. I think that's a good question about the, the project board.
To… maybe we can spend some time looking at that.
As this would… these would be good things that people can start, kind of, picking up.
Voting procedures… Prs.
And approvals on PRs, and merged PRs.
**Neil Yashinsky** 04:42 Yeah, it works for me. I was just curious if there's, you know, a process. Obviously, there's probably been ways that have been… you know, this type of thing has been decided before, just before I've been involved.
**Trask Stalnaker (Microsoft Corporation)** 04:53 Yeah, I don't think we've ever, in the stabilization efforts, ever like… voted… On anything other than via our green checkmarks.
**Neil Yashinsky** 05:07 be safe tonight.
**Trask Stalnaker (Microsoft Corporation)** 05:07 I did really great.
**Neil Yashinsky** 05:08 anyway, so… Oh, sorry, go ahead.
**Trask Stalnaker (Microsoft Corporation)** 05:10 And really very, consensus-building oriented.
Cool, let's see, I don't know, Liudmila, you… do you have any tips for… how to… what to do.
with the board.
**Liudmila Molkova** 05:36 I'm thinking…
**Trask Stalnaker (Microsoft Corporation)** 05:36 It's like…
**Liudmila Molkova** 05:38 Yeah, maybe, like, in the items, In to-do.
We can… Try to look at a few of them.
If we have time, or maybe we reserve, like, 5 minutes.
And try to find the next, like, thing that is actionable.
like, the issue number 11 is not actionable. Maybe we just, I don't know, close it.
**Trask Stalnaker (Microsoft Corporation)** 06:11 Okay, so we can drag it to the bottom.
**Liudmila Molkova** 06:13 Right.
Yeah, so… The 51 is a little bit more actionable.
And I think… This is essentially… the conversation ID, is the session ID?
And… From what's been here.
we still, like, in this issue and related, we still don't know anything different about session ID.
So I… my intention was to close this issue at some point.
It's just there is a lot of context and a lot of spike shading on the terminology.
**Trask Stalnaker (Microsoft Corporation)** 07:07 Yeah, For… okay if I just move it to post-ability, at least, for now.
**Liudmila Molkova** 07:16 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 07:23 This one… Oh, okay, so some of the… to-dos are in PR. Should those automatically go to in progress?
**Liudmila Molkova** 07:38 So there are in-progress PRs that I deliberately didn't triage because I don't want to put them in any category.
**Trask Stalnaker (Microsoft Corporation)** 07:47 Oh, I see, there may not be, for stabilization.
**Liudmila Molkova** 07:52 Right, yes, I… yeah.
So the, the, yeah, 4.59 is a PR.
But it's also an issue that probably we shouldn't… we should have created.
And, the, the Dazzella with this one as well.
Oh, this one we should probably move in progress, right?
**Trask Stalnaker (Microsoft Corporation)** 08:23 Yeah, yeah. Yeah.
Yes, that is that one, yes.
This one… Probably just close now, right? Because… of… We have a comment here.
**Liudmila Molkova** 08:51 Yeah, and I've opened the PR, the draft PR that would start Fictionary.
**Trask Stalnaker (Microsoft Corporation)** 08:57 Nice, nice. Okay, yeah, so that is closed now.
**Liudmila Molkova** 09:05 It's in progress…
**Trask Stalnaker (Microsoft Corporation)** 09:07 This one…
**Liudmila Molkova** 09:12 Oh, this is yours, too.
**Trask Stalnaker (Microsoft Corporation)** 09:17 Okay, and so this is… yes, this is to be closed as well. It's the… Metrics.
Aggregated token usage… Is this resolved by your PR?
**Liudmila Molkova** 09:45 I don't think so. I think Alex is asking for… A different attribute on agents?
**Trask Stalnaker (Microsoft Corporation)** 09:53 Right.
**Liudmila Molkova** 09:54 And… For the reasons… That's summing up things… Summing up usage attributes across all spans.
Otherwise produces wrong results.
I… I still have… Mixed feelings about this. I don't think you can… we can build the promise that summing up usage attributes across all spans What is… is meaningful?
But we need to, like, it's to do, we need to resolve it. Yeah.
**Trask Stalnaker (Microsoft Corporation)** 10:43 Yeah.
Define a more structured alternative to operation name.
**Liudmila Molkova** 10:51 Oh, it should be, looked at together with this issue number 21.
Next to it, because this… this one is asking for more structured And 21 is asking for… less structured.
But I'm sorry, now I need to drop for…
**Trask Stalnaker (Microsoft Corporation)** 11:09 Oh, yeah.
**Liudmila Molkova** 11:10 Nicole, I'll be back soon.
**Trask Stalnaker (Microsoft Corporation)** 11:11 Okay.
So… more structured alternative… But also… okay.
That sounds.
**Neil Yashinsky** 11:33 Sounds like a level of verbosity, I guess, yeah, in some ways?
**Trask Stalnaker (Microsoft Corporation)** 11:40 Structure Alternative…
**Aaron Abbott (Google LLC)** 11:54 Is the goal to have it normalized across providers?
So, like, right now, for inference, we do generate content, or we do, completions, or whichever version of OpenAI we're on.
I think we record different strings for each one. Is the goal just to have a better normalization?
**Trask Stalnaker (Microsoft Corporation)** 12:19 That could come from… yeah, I was trying to… Figure out if the span type Overlaps with this.
Because that would probably… if span type would be the structured, like, thing, and then operation name…
**Aaron Abbott (Google LLC)** 12:42 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 12:43 could be…
**Aaron Abbott (Google LLC)** 12:47 Yeah, I think I agree with that.
**Trask Stalnaker (Microsoft Corporation)** 12:58 more… schema… Fields… Oh yeah, let's drag these two together so they're next to each other.
Semantic oh, and this is for generative AI systems.
Okay, this is… I'm just gonna drag this to the bottom for… No… It's kind of one of these big… Things that probably… Is not in scope.
parts. Okay, I saw, is this related to the topic?
Today, I saw there was a topic where… Yeah.
**Aaron Abbott (Google LLC)** 13:52 Nice. And it's… it's just the schema stuff, if you want to put it next to those ones.
**Trask Stalnaker (Microsoft Corporation)** 14:06 There's so many.
schema.
Yeah.
Yeah, we might… Be useful to group these.
Some point. Somehow.
Genai, okay, parts… metrics for detailed token usage. I think this one… at least cash… yeah, and reason, I think this is… Probably resolved by… We have a PR here.
But then, isn't this… what Ludmila's… this PR.
Agent name… on child… okay, so this is what we discussed, yesterday in the SIG meeting.
More stuff about the parts. Okay, so lots of… yeah, that would probably be a good grouping.
Multiple agents on the same telemetry.
So… kind of… I'm curious if this is… Partly or fully addressed by the… the handoff.
PR that we discussed yesterday also.
**Aaron Abbott (Google LLC)** 17:02 Yeah, I also… Sorry.
**Neil Yashinsky** 17:06 No, go ahead, Aaron.
**Aaron Abbott (Google LLC)** 17:08 I was just gonna say, I also have that PR for including, like, the agent URN and the resource, so I think… The part of that… the question of that one is if you have a trace with many concurrent agents running at once.
**Neil Yashinsky** 17:24 Yeah, exactly, and I thought, like, the context… Used for experiments and stuff was a sub… sub… part of that discussion? Which I… which, to me and Trask, I think they have slightly… Different concerns, although overlapping, but also separate.
**Trask Stalnaker (Microsoft Corporation)** 17:46 So this is the one, Erin, that you were talking about.
**Aaron Abbott (Google LLC)** 17:51 Yep.
**Trask Stalnaker (Microsoft Corporation)** 17:58 And… sorry, Neil, can you… Repeat what you were saying.
**Neil Yashinsky** 18:03 Sure, sure. I think you're just asking if the two PRs were, you know, the same or related, if I recall your question, and I said, they're both, I guess, or they're not both, they're related, but there's a little bit of… not over, or separate concerns, not overlap? What's the word I'm looking for? Granularity? Aaron, do you agree? I think that's what Aaron was saying as well. I don't want to mischaracterize what he said.
**Aaron Abbott (Google LLC)** 18:29 I… I think so. Maybe… I mean, Limila's back, too.
I don't feel stupid.
**Liudmila Molkova** 18:37 I missed…
**Trask Stalnaker (Microsoft Corporation)** 18:40 Do you remember if this issue, or just dragging issues, do you remember if this… is… Is it… will it be resolved by the handoff?
PR from Nikhil and or Aaron's, main agent…
**Liudmila Molkova** 19:05 Yeah, I think be resolved by… both of them, and I think… Niko Spjor… It explains why this is the wrong issue to solve, because… I assume that handoff is only between agents.
It's not the case. You can hand off to an arbitrary nod in a graph, which could be, I don't know, anything.
So it's not even the agent namespace we should be… Recording these things in.
**Trask Stalnaker (Microsoft Corporation)** 19:46 Did we… where are we recording?
Oh, under, like, a tran… Oh, under something completely under the handoff?
**Liudmila Molkova** 19:56 I think the description is out of date. Oh, and this is not the Nikios ER, it's some previous version of it that we unfortunately abandoned.
**Trask Stalnaker (Microsoft Corporation)** 20:07 Oh, okay.
**Liudmila Molkova** 20:08 As a review versus the… For contributors, still.
Doesn't know, maybe.
**Trask Stalnaker (Microsoft Corporation)** 20:18 That's hot there.
Okay.
Yes, yes, yes, okay.
Let me fix my accounting… Alright, alright, Okay… Alright, that was a… let's, pause there. So one, we did find those… definitely would be a good kind of grouping, maybe Uber issue, if someone wants to create around parts.
Like, all the different, related pieces, just to tie those together.
And on that topic, let's… This… you said, Aaron, this was you?
**Aaron Abbott (Google LLC)** 21:36 Yeah, yeah, I added that one.
**Trask Stalnaker (Microsoft Corporation)** 21:38 Cool.
**Aaron Abbott (Google LLC)** 21:41 Do you mind… oh, yeah.
**Trask Stalnaker (Microsoft Corporation)** 21:45 Yeah.
**Aaron Abbott (Google LLC)** 21:46 So, if you… I think it's pretty… this is a little more obvious if you paste it in… if you, like, create a… document like VS Code that has JSON schema validation and autocompletion, but… Essentially what we have is, like, a union, which is the NEof.
Each of the part types, and generic allows arbitrary strings for type.
And what that… what that means, though, is that even if you have a type like tool call, or… text.
If it doesn't meet the criteria for text part or for tool call part, it will just fall back to the generic part and pass the validation.
So, like, the goal… I don't think the goal was ever validation necessarily, but it does feel maybe a little bit too… Open.
And… Yeah, there's probably a couple ways we could fix it, but that's kind of the crux of the issue.
**Liudmila Molkova** 22:44 I've already seen it in the Python GenAI repo, we did something wrong, and it passed validation because of this problem.
**Aaron Abbott (Google LLC)** 22:56 Yeah.
**Liudmila Molkova** 22:57 What would be the right way to solve it? Like, how… I think Dylan had some comments on… Should we even record generic parts?
Or it's something… Like, one choice we can have is that generic part is not to be recorded in telemetry, it's the extensibility mechanism When somebody wants to define a custom part that's specific to a certain provider, or, when It's just the future-proofness that consumers should expect parts that they… we don't declare yet.
And then we never create generic parts, intentionally. Somebody creates… it's like an abstract class.
**Aaron Abbott (Google LLC)** 23:47 I'm not sure I totally got that.
like, You're basically saying the schema wouldn't have it, and then people would just do it anyway? Is that right?
**Liudmila Molkova** 23:57 Now, the schema would have it.
**Aaron Abbott (Google LLC)** 23:59 Okay.
**Liudmila Molkova** 24:00 But… It's not something… it would have a type… I think it should have a type, right? That's the thing we demand. Like, from the code perspective, let's forget about schema for a sec. Let's say generic type, generic part is an abstract base class. Yes. It has one property type. You cannot instantiate it, you cannot serialize it, but you can subclass it.
I don't know how to express it in the schema, so, like, you never populate that, but you populate Something that's derived from that.
**Aaron Abbott (Google LLC)** 24:36 Yeah.
I think… I think this is kind of the same thing, but what I was thinking was you can… we can have generic as… a literal, like, type, so somebody can put generic, or it could be… it's essentially like an escape hatch. And then it has, like, an unstructured Or an unchematized any within it.
So that people can throw whatever they want in there, and it's explicitly in that… that separate type, and then as things get added to the schema, They would be part of this tied union, but not… you would move them out of the generic part eventually. Is that kind of what you were saying, too?
**Liudmila Molkova** 25:14 No, I'm… I was thinking, if you don't Have a part to report your stuff in.
You either don't report it at all.
Where you define your own part type.
That's, let's say, specific to OpenAI, or Entropic, or Google GenAI, or whatever.
And then you populate this type.
it has some literal that's specific to you, I don't know, OpenAI FU.
And then… You don't break it, you don't change it over time. Well, if it's stable.
**Aaron Abbott (Google LLC)** 25:55 Okay.
Yeah, I see what you're saying. I have no… clue if JSON schema… makes it easy, but I think we could… I get what you're saying, though, yeah.
**Trask Stalnaker (Microsoft Corporation)** 26:11 So, essentially, just removing the fallback.
**Liudmila Molkova** 26:15 The fallback exists for consumers to expect stuff they don't know about. It does not exist for producers, you never write stuff you don't… you don't… Have a schema for.
**Trask Stalnaker (Microsoft Corporation)** 26:39 So does that require two different schemas?
Like, how… how do you… how do you relax it for consumers, but keep it… restricted for… Producers.
**Liudmila Molkova** 26:59 Let me research… I… there is either a mechanism in JSON schema, Or… We need to be creative.
**Aaron Abbott (Google LLC)** 27:10 Yeah, I thought what you were saying.
what I understood was, we would let people effectively, like, subclass the schema or specialize this schema if they needed to, and then producers… sorry, consumers wouldn't use that. They would use this schema, but the two would be compatible because it would have the… the kind of fallback case.
Which makes them compatible, is that right?
**Liudmila Molkova** 27:40 Sorry, I didn't get that, but I'm thinking that two different schemas might be… At one… at some… one side over engineering, at the other side very useful, because, for example, we have everywhere allow additional properties.
It's for consumers to expect them, but not for producers to produce them.
Can we, like, if we… We kind of need to investigate it, but it's… if it's a viable approach, if it's not too much over-engineering, we would stabilize the producer schema.
And we would not… Stabilize the consumer.
Or the opposite.
**Trask Stalnaker (Microsoft Corporation)** 28:34 What do consumers do with the schema?
**Liudmila Molkova** 28:41 Imagine they queried… They say, okay, find me all the assistant messages, right, let me run evaluations based on them, on the input and output.
**Trask Stalnaker (Microsoft Corporation)** 28:51 To understand the… content.
**Liudmila Molkova** 28:55 Yes.
**Trask Stalnaker (Microsoft Corporation)** 28:56 Not to do validation.
**Liudmila Molkova** 28:59 Yes, not to do a validation, yeah.
**Aaron Abbott (Google LLC)** 29:07 I… I think… I just want to call out, I think… The reason we had this generic thing in the first place was… because, well, obviously we didn't have all the part types represented, and I think it was maybe Alex or somebody from Pydantic said they don't want to drop the data on the floor.
So their kind of explicit goal was for the producer to add generic or extra stuff that's not in the schema.
**Liudmila Molkova** 29:35 But that's okay, it's… it's not that… You should not see the… Part was typed generic.
Y-you, you, you were… Expected to… you should expect to get types that you don't know about.
**Aaron Abbott (Google LLC)** 29:57 Yep, no, that makes sense.
**Liudmila Molkova** 30:03 But in our instrumentations, We… Don't know what to do with types we don't support today, and would rob them, I think.
**Aaron Abbott (Google LLC)** 30:20 We should… we should check on that. I thought… kind of thought we included them, but we should double check.
**Liudmila Molkova** 30:27 I think it's maybe a little bit of a Wild West, but yeah.
**Aaron Abbott (Google LLC)** 30:31 Bill.
So maybe, Ludmila, if you're up for it, could you leave a comment on here with… with what you were thinking, and then I'm happy to work on this one.
But yeah, sounds like we're not… Completely on the same page yet.
**Liudmila Molkova** 30:49 Yeah, and I mean, whatever allows us to college table, I will be supportive of, but, like, that… Would not… would be… Open enough to… For us to add more things, right?
**Aaron Abbott (Google LLC)** 31:06 Yeah, yep.
**Liudmila Molkova** 31:08 Okay, I'll leave a comment.
**Trask Stalnaker (Microsoft Corporation)** 31:13 Cool, we're at time, but, if we'll have a minute or two, we could discuss what we want to try to do for Friday.
Or we could follow up async.
There aren't…
**Liudmila Molkova** 31:38 I will be out.
For the next… Essentially, in terms of this Meetings for the next two weeks.
I'll be back on Tuesday, the 29th.
I… I'll check Slack, I can approve something if it… if it needs to happen, but mostly I will be out-out.
**Trask Stalnaker (Microsoft Corporation)** 32:01 Okay.
So, yeah, so… let's… try to… let's focus on issue triage, or the board triage, for Friday.
If folks have a chance to, you know, go through and, like, as I kind of… you saw me, like, trying to just tie in related things, even if you don't say, like, this or that, like, yes or no on them, just trying to connect them together.
If somebody who… I don't understand the parts stuff well, if somebody who understands that wants to, I… create an Uber issue or something for all of those.
That would probably be helpful.
And, yeah, I'll try to… go through.
also, before Friday, and then, if we can leave just some little notes on issues, then we can, Tried to make some decisions on, you know, actually working, Spitting some of them out, and people picking them up.
**Liudmila Molkova** 33:18 Yeah, there is a big piece that is kind of easy to do, and it seems we have consensus on, is the metric renames.
And the draft PR I have, it kind of shows how to do things, given I will be out, I want.
work on this, in the next couple of weeks, and if somebody wants to pick it up and, like, close this one and go… work on it. There are multiple pieces, like, we… this is just for the inference renames.
And we do… we have, like, 10 other operations. So, once we establish the pattern, it's kind of up for grabs to do the rest.
And I think the only, interesting question there is about exceptions.
Do we have exception per operation, or do we have one exception event?
We can't decouple this problem and solve it later.
**Trask Stalnaker (Microsoft Corporation)** 34:20 Cool.
**Aaron Abbott (Google LLC)** 34:21 Cool.
**Trask Stalnaker (Microsoft Corporation)** 34:22 Awesome.
Welp.
Stay in touch on Slack, and see you all on Friday. Except for you, Lyudmila.
**Liudmila Molkova** 34:30 Yeah, have fun here.
**Trask Stalnaker (Microsoft Corporation)** 34:31 when you're back. We are.
**Neil Yashinsky** 34:34 That's right. Always. Thank you.
**Trask Stalnaker (Microsoft Corporation)** 34:36 Bye.
