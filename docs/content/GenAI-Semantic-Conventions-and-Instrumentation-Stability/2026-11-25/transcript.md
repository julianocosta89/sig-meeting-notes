SIG: GenAI Semantic Conventions and Instrumentation Stability
Date: 2026-11-25
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 00:31 Hello.
**Trask Stalnaker (Microsoft Corporation)** 00:35 Hmm…
**Matt Spiekerman (New Relic, Inc.)** 00:37 Hello.
**Liudmila Molkova** 00:40 Zoom is working.
It didn't work in the morning.
**Trask Stalnaker (Microsoft Corporation)** 00:45 Oh, I heard the Weaver… for the Weaver call.
**Liudmila Molkova** 00:48 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 00:51 Somebody else in the CNCF maintainer circle channel had reported problems.
So, I don't know, seemed like some… maybe it was glitching.
the… the LFX… Stuff, probably.
**Liudmila Molkova** 01:11 Yeah.
Okay, so welcome to the call!
I've collected some… things that… We should… review?
If anybody wants to bring something, like a discussion up that's not one of those, go ahead.
Mikola, I think I added some of your… your PR here.
**Mikolaj Knap (Google LLC)** 01:48 Yeah, I think I see it. Thank you.
**Liudmila Molkova** 01:51 Yeah. But if you want to talk about, like, the… the roll-ups.
**Mikolaj Knap (Google LLC)** 01:57 I think… I think the roll-ups… I'll mention it during the PR, but probably not for today.
**Liudmila Molkova** 02:04 Okay, sounds great.
Cool.
So let's go through some of the trivial things.
The tr- oh, no, it's not in.
The Copilot doesn't have… Needs an approval!
How come?
You're told…
**Trask Stalnaker (Microsoft Corporation)** 02:27 Yeah.
**Liudmila Molkova** 02:29 You told it to resolve conflicts.
And turns out it needs the approval for workflows to run.
**Trask Stalnaker (Microsoft Corporation)** 02:37 Oh, did I not fix that here?
Yeah, I will… that's the default setting, which… is… feels dumb, but I guess it's for, like, security. But since we don't review those, before clicking the button anyways… And, I mean, all of the secrets are protected anyway, none of the secrets are available for PR runs. I don't understand, really, why that's… the default, but I will fix that.
**Liudmila Molkova** 03:12 Yeah Okay, so then there are a few that needs a non-Googler to approve, and Trask, I think you could take a look at this one, the invocation.
**Trask Stalnaker (Microsoft Corporation)** 03:24 Yes. Yes.
**Liudmila Molkova** 03:28 R… For this one… Dylan here, I'll ping Dylan to take a look at this one.
This is…
**Trask Stalnaker (Microsoft Corporation)** 03:42 Oh, I… no, this one… oh yeah, this one, I asked, Ankit just now to review it.
**Liudmila Molkova** 03:48 Oh, because, yeah, you need the non-Googler. Okay.
Confusing.
Okay.
**Trask Stalnaker (Microsoft Corporation)** 03:54 Yeah, one thought I had… Is that we could change our policy if we wanted to say that If the PR author is an approver, That… that counts for… odd.
company diversity.
**Liudmila Molkova** 04:17 Yeah, I think it did make sense.
**Trask Stalnaker (Microsoft Corporation)** 04:21 Yeah. I'll send a PR.
**Liudmila Molkova** 04:27 Okay, so this is Thoravio, right?
Nothing super interesting.
**Trask Stalnaker (Microsoft Corporation)** 04:36 We'll see.
Yeah, I mean, so the only… if you go to the PR description, the al… the alternative there Is… worth at least… Considering briefly.
So, if the tier comes back in a later chunk.
This is saying don't capture it.
So that we have consistency there.
But it also means we lose that.
**Liudmila Molkova** 05:18 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 05:19 I don't really have strong feelings either way, I just, some, you know, something flagged this as a question, I think, on a prior PR, and I didn't want to hold up that PR, so I sent it as a follow-up.
**Liudmila Molkova** 05:34 I left a related comment on your other PR.
I think… this one.
I had, like, 10 minutes when I… before the meeting, when I started reviewing it, so I didn't have a chance to think through, but… What we're doing here, we are saying to hold Oh, the usage.
Until the operation ends.
Right.
And there is a trade-off.
So we either populate… like, Aerotype is the most interesting one, right? So the tires usually could be available, right, with the start, but Aerotype never is.
**Trask Stalnaker (Microsoft Corporation)** 06:23 Right.
**Liudmila Molkova** 06:26 Yeah, and either we say, okay, for abandoned streams, the midstream crashes, we return, we don't report anything.
or we report… Counters without error type, at least.
**Trask Stalnaker (Microsoft Corporation)** 06:45 Yeah, there's the other question of, I think there was another question of duplication.
Possibly… Though I think we would say on the… dreaming… like, how do you… how do you sum them up? Like, the… the convenient thing about only stamping on the last one is that You know that's what it is, whereas… if you're getting them iteratively. I think in some cases, you get the total, not the diff each time, so…
**Liudmila Molkova** 07:25 You calculate the delta.
**Trask Stalnaker (Microsoft Corporation)** 07:28 in the Instrumentation.
**Liudmila Molkova** 07:30 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 07:31 Yeah.
That would be fine.
**Liudmila Molkova** 07:35 But, I mean, like… We could make it work.
Except the attributes that are not available.
**Trask Stalnaker (Microsoft Corporation)** 07:48 The error types, the things that are on the… yeah.
**Liudmila Molkova** 07:53 Yeah.
And I think we need to make a call.
So for abandoned streams, I think, like.
The fact that we would record something for abandoned stream is nice, but… It… it's a broken experience for abundant streams regardless.
So, I'm thinking… We should have some… Probably up-down counter for number of active streams as an indication for users, or, like, we could provide the observability necessary to see if you abandon streams.
And then… Effectively… I… I don't want to optimize for them.
**Trask Stalnaker (Microsoft Corporation)** 08:43 Well, I mean, you're still getting the… But… chunk… Operations.
We're still recording… I forget, we're recording an event? No.
**Liudmila Molkova** 08:58 Wait, wait, don't trickle.
**Trask Stalnaker (Microsoft Corporation)** 08:59 Oh, it's a metric, I see. Right, right, right, right. It's only the metric, okay.
**Liudmila Molkova** 09:06 Yeah.
The midstream crashes are also, like, not something… We can optimize for.
**Trask Stalnaker (Microsoft Corporation)** 09:17 I remember one other argument for this PR… is that… The… The count… Then matches your operation count.
Instead of, like…
**Liudmila Molkova** 09:41 For… for the histograms.
**Trask Stalnaker (Microsoft Corporation)** 09:43 If you… yeah.
**Liudmila Molkova** 09:45 But histograms are, for sure, You cannot report it when chunks arrive anyway.
**Trask Stalnaker (Microsoft Corporation)** 10:00 So currently, sorry, I think I got lost. The chunks, we record, Our option is to record them as they come in.
in the hidden… Oh, in the histogram. For that, we want… what is this metric? Sorry, I think I'm lost. Can you expand above?
**Liudmila Molkova** 10:22 Yeah, these are old, token usage metrics with this note.
**Trask Stalnaker (Microsoft Corporation)** 10:30 Oh, okay, this is the counter, yeah. Yeah.
So, I guess the… Question is, I mean, if you used a different aggregator, for the counter… And you cared about it being… Matching the operations.
**Liudmila Molkova** 10:52 Mmm.
**Trask Stalnaker (Microsoft Corporation)** 10:53 The number of times you record would be the number of operations if you record it once at the end.
**Liudmila Molkova** 11:00 Okay, so then if we wanted in the future to report something Inside the stream, as it goes, we would have something like the chunk usage, or some other metric that would have this information. I don't know how useful would it be, but that would be…
**Trask Stalnaker (Microsoft Corporation)** 11:21 Yeah.
Don't meet.
I think that makes sense.
And then, does the same thing apply to the tiers thing? I forget, so if you… If we reported… Oh, no, that one, it is per chunk. We're already recording per chunk there.
On the service tier question.
**Liudmila Molkova** 11:55 To your… Time…
**Trask Stalnaker (Microsoft Corporation)** 11:56 Per… time per output chunk.
**Liudmila Molkova** 12:02 And that's the buyer… And here we are saying to… keep the attributes consistent for the whole stream, right? So if you resist something later, You would not… Saturday at all.
**Trask Stalnaker (Microsoft Corporation)** 12:25 Yeah…
**Liudmila Molkova** 12:27 And this is…
**Trask Stalnaker (Microsoft Corporation)** 12:27 I see.
You would lose that.
More granular data.
**Liudmila Molkova** 12:35 Because for Google GenAI, do we report the service tire comes back early in the stream, when it starts, or later?
**Mikolaj Knap (Google LLC)** 12:46 Great question. I would say probably early in the stream, but I honestly don't remember.
I know we can report the tokens at every point.
**Liudmila Molkova** 12:57 Yeah, I think for OpenAI reports it in every chunk. I will check with Google GenAI, but essentially, if it's just one outlier that reports it later, then… Shelby.
**Trask Stalnaker (Microsoft Corporation)** 13:09 Maybe they should fix it.
**Liudmila Molkova** 13:11 Yeah, agree.
Okay, I'm glad we talked through it. I think we have a pass forever with the chunk metric, so I'll… I'll put a comment later here, I left a comment to discuss.
**Trask Stalnaker (Microsoft Corporation)** 13:26 Cool.
**Liudmila Molkova** 13:29 Wonderful.
There is a… okay, so we talked about this one, talked about this one… This is a trivial one.
It's a nice cleanup, turns out we have two co-response for… client-side tools for server-side tools, but the description is inaccurate, and based on the history, it's like, it was just an oversight. It's not intentional at all.
So this is a nice clean-up trivial… oh, you already…
**Trask Stalnaker (Microsoft Corporation)** 14:03 I approved it just before the call, also.
**Liudmila Molkova** 14:07 Okay.
Okay, so then there are… A couple of things that need approval from… Not from Trask.
So, I'll ping Dio and Aaron to take a look.
But this removes the OpenAI refinement for the old metric.
the other one is more interesting.
Oh, Trask! This is the new experimental bot, right?
**Trask Stalnaker (Microsoft Corporation)** 14:46 Yes, so I actually took this, because I didn't love the comment they gave you here, and so I, I… Updated the prompt so it will give a little better formatted comment.
And less, like, noise.
**Liudmila Molkova** 15:03 Is it, like, the Autelbot on behalf of Trask, or is it just the automation?
**Trask Stalnaker (Microsoft Corporation)** 15:09 So I have a PR up in the shared workflows.
to, but I've been running it… I've been dispatching the workflow, like, manually through that repo for testing it.
And basically, it's pretty straightforward. It just does a review using, GPT Soul, on Macs, and then does a Koala, because the GPT model is cheap for Microsoft, at least.
The… then there's, double-checks that using Opus, 5.5.
On high, and then it, it does one other thing, the… the… it looks for simplifications.
Which is something… not that useful in this repo, but in the Java Instrumentation repo, I've noticed Copilot, like, normal reviews, like, doesn't really look very hard at all for things that could be simplified, and so we usually end up human-flagging those So it's been… had some good results there.
**Liudmila Molkova** 16:29 Nice, okay.
Cool, I'll take a look at the comments, but yeah, let's just collects the… Other ways to capture errors inside the result.
And size to satire type accordingly.
**Trask Stalnaker (Microsoft Corporation)** 16:49 One of my goals is, I was noticing, in the conformance repo, like, Kristoff?
Claude reviewer seems to find a lot more things than the Copilot review, so I'm still trying to understand, like, yeah, how we can do better.
**Liudmila Molkova** 17:12 I love asking, the harness, like, why Copilot didn't notice it when I reviewed PRs.
And it usually has an explanation, they have no idea how well the explanation is.
**Trask Stalnaker (Microsoft Corporation)** 17:25 So, the… the other thing, kind of bigger picture I'm working on is, so I have also a PR in the shared workflows that will, generate… We'll, generate a co-pilot Instructions.
For a repo, but it's also tied to… so I… I'm… going to start tracking, all the human and bot, review comments, and whether they were addressed or not in the PR as sort of, like.
A, how many… I want to bring down the number of human comments, that we have to make, and B, like, what's the effectiveness? I'm assuming if it was addressed, it was accepted.
And, then using that same data, then those review comments to then funnel into the co-pilot review instructions, and then have something that can keep that up-to-date over time. I have a… if you look in the conformance repo, I have a draft PR up.
That is the result of that automation.
**Liudmila Molkova** 18:47 Hmm.
**Trask Stalnaker (Microsoft Corporation)** 18:48 So this is the first repo. And I've kind of, in the Java Instrumentation repo.
I've established… if you look, there's one called… file called Instruction Authoring.
There all have the word instruction in it. Authoring.
Dash authoring.
Yeah.
**Liudmila Molkova** 19:14 Okay.
**Trask Stalnaker (Microsoft Corporation)** 19:17 Oh, wow, this is interesting. I don't know why it embedded the Apache license there, I'll have to look at that. That's great.
But anyway, a specific way to, have these where there's kind of one rule per bullet, and I have been running an experiment in the Java Instrumentation repo where I have an audit running, where it'll go, bullet by bullet, and for each bullet, it will look for Conformance against the whole repo for that individual bullet.
And it'll send a PR if there's any violations of that rule.
And it's good for both getting your repo consistent, as well as pointing out problems in the instruction files, because when you go and review the PR, and you're like, wait, that's not what I meant at all, and then you… close the PR and fix the instructions.
So yeah, so I'm working on a bunch of things kind of around in that area, so yeah, I'm using the Java Instrumentation repo, but also the GenAI SemConv rep repo as… and now Conformance repo as my testing grounds.
Nice. So bear, bear with me.
**Liudmila Molkova** 20:37 Oh, that's awesome! I love the skill to write skills.
Yeah.
Okay, what else do we have interesting to talk about? Yeah, we should talk about… Mikola is pure, so I think we are down to this one.
I didn't have a chance to review yet.
**Mikolaj Knap (Google LLC)** 20:59 I don't think it's anything too controversial. I think we discussed it previously. I think it's just adding agent name to all the inference metrics.
I think the main use case for this is just token attribution, and then being able to… have, like, inference attribution as well, per agent, so… Yeah.
**Trask Stalnaker (Microsoft Corporation)** 21:24 And so, is this, like, generic… are you proposing generically, kind of, that idea of… Propagating agent name down the hierarchy and stamping it automatically.
Or is this sort of… Constrained to agent harnesses, which also do the inference calls and track… capture those inference calls, so they… they can do all of it together.
**Mikolaj Knap (Google LLC)** 21:52 I think it's probably getting it down the hierarchy, so…
**Trask Stalnaker (Microsoft Corporation)** 21:56 In, like, a generic way.
**Mikolaj Knap (Google LLC)** 21:57 Oh, no, no, no, no, sorry, sorry, sorry. And I don't mean… I misunderstood you. I meant that there would be attributed to the agent that's directly calling the inference, so it wouldn't be some higher order agent.
That wouldn't be the agent name you're attributing it to. You would be attributing it to only the… basically the agent that's actually making the inference call.
**Trask Stalnaker (Microsoft Corporation)** 22:20 So, a lot of times, I mean, the inference… Calls are captured by a different library.
How does… how would the agent… How would that library know what the agent name was to stamp that onto the… Spam.
**Mikolaj Knap (Google LLC)** 22:41 metric, the span.
I think… I think then you could do context propagation on through, and that would be good enough, because that's…
**Trask Stalnaker (Microsoft Corporation)** 22:53 Yeah, Led Miller, you had pulled up that one page already that… yeah… Weird.
Essentially said that this was allowed.
what is… Mikolajay, what is your PR, sort of, Proposing above this.
**Mikolaj Knap (Google LLC)** 23:18 bored.
We should… Water operations…
**Liudmila Molkova** 23:24 Just referencing the attribute that was not referenced before.
**Mikolaj Knap (Google LLC)** 23:30 on what?
Sorry, so what is the question again?
**Trask Stalnaker (Microsoft Corporation)** 23:34 I'm… Liila, can you show the other… your other tab?
the existing… in case, Mikola, in case you hadn't seen this already.
**Mikolaj Knap (Google LLC)** 23:46 On operations where agent name identifies Instrumentation was non-populated from the other context.
Okay, I see, so there's specific instructions to not pass it through the context.
**Liudmila Molkova** 23:59 No, no, no, no, no. Sorry, I… it's probably misleading, we should rewrite it. So… This may be the first.
**Trask Stalnaker (Microsoft Corporation)** 24:07 First sentence, yeah.
**Liudmila Molkova** 24:08 Right.
Listed below, maybe we should list them here, but this is explicitly the two attributes that we want instrumentations to propagate across each other.
**Mikolaj Knap (Google LLC)** 24:21 Okay.
**Liudmila Molkova** 24:22 And there's a lot of language saying here that you should not propagate others, and also you should only stamp them if they are defined on the corresponding metric.
**Mikolaj Knap (Google LLC)** 24:34 Okay, I see. I think, agent.name is listed here, right? So it should be… Yeah. Yeah.
Should be good.
I think that's exchanged in the PR, but yeah.
**Trask Stalnaker (Microsoft Corporation)** 24:48 So what I was… kind of the question I was trying to ask, sorry, was… What, beyond that.
current, allowance for instrumentations already to do that. What is your PR… proposing.
**Mikolaj Knap (Google LLC)** 25:07 between that allowance, I think… besides allowing that, it's just adding it to the… to the reference group for the inference metrics. I don't think there's… and then I think there's, like, a scenario for it.
I think adding it for the spans… is covered in a separate PR that is currently in draft.
**Liudmila Molkova** 25:30 Seems it was already there, though.
So I can, in YAML, It just shows the note was added.
But it was already there.
**Mikolaj Knap (Google LLC)** 25:44 That agent name was already in the reference group for this?
**Liudmila Molkova** 25:49 Sir or something, yeah.
**Trask Stalnaker (Microsoft Corporation)** 25:50 Might have been… yeah, that it's impossible to understand the inheritance of the, YAML… YAML inheritances.
**Mikolaj Knap (Google LLC)** 25:59 So this was pointless, so overwhelmed by misunderstanding.
**Trask Stalnaker (Microsoft Corporation)** 26:05 Well, there may still be a point, but yeah, yeah, check, check that out, the existing… Allowance, and then… Whether it's added to the places that you want it already.
**Mikolaj Knap (Google LLC)** 26:21 Okay.
**Liudmila Molkova** 26:26 Probably in the metrics GenAI, metric attributes GenAI.
Probably somewhere in the GenAI Common!
**Trask Stalnaker (Microsoft Corporation)** 26:43 Yeah, the trick, Mikolaj, as Ludmila was showing, is just… or, I don't know, the only thing I can do is look at the markdown.
To see, like, what all the things aggregated together.
**Liudmila Molkova** 26:56 You know, in the old days, when we used VS Code, I had… I built a plugin to actually navigate as a code, so you can go to definition…
**Trask Stalnaker (Microsoft Corporation)** 27:04 and whatnot. Like, click.
**Liudmila Molkova** 27:06 Like, CLIC, yeah! It's in the VS Code extensions, but who uses VS Code these days?
**Mikolaj Knap (Google LLC)** 27:12 Shm.
**Liudmila Molkova** 27:13 Where is it?
Okay, so then, essentially, here.
Looking at the markdown, nothing changed.
Oh, it changed something, somewhere.
In some refinements.
**Mikolaj Knap (Google LLC)** 27:35 Yes. But…
**Liudmila Molkova** 27:35 for the token metrics, it seems it was already there, because there is no… Oh! Okay, so it added something here. Okay, so take my words back. It wasn't there.
**Mikolaj Knap (Google LLC)** 27:48 Okay, so it wasn't inherited.
**Liudmila Molkova** 27:51 No, it wasn't inherited everywhere, probably it was inherited somewhere.
But, like, is this… Is this just a markdown without… that's not auto-generated?
**Mikolaj Knap (Google LLC)** 28:08 Cool.
**Liudmila Molkova** 28:11 Probably should drop everything that's not auto-generated from these files, because… We already have it.
**Mikolaj Knap (Google LLC)** 28:21 Yes, I think that could have been an issue. That could have been a mistake.
But… Yeah.
**Trask Stalnaker (Microsoft Corporation)** 28:42 Yeah, if only, gitHub would… Could hide, or things that were auto-generated in these files, so we could… Only see the things that were… Manual.
I very often ask my, agent to mark all the files as viewed, which are only auto-generation.
that only have changes which were auto-generated. Now, whether it does that correctly is maybe, but probably gets it right.
**Mikolaj Knap (Google LLC)** 29:22 Yeah. I wonder.
**Trask Stalnaker (Microsoft Corporation)** 29:22 I should try that on this one, see if it leaves this one unviewed.
**Liudmila Molkova** 29:28 Up… have we… I keep thinking about how to organize it better, and we, by the way, need to clean the sub, not in the SPR, but, like, in general, but… if… we view it in GitHub, the best view, if we have, let's say, one metric per file.
And then the folder is all the metrics and spans applicable to the separation, for example.
And then the… whatever prose we write that's, like, handwritten just links to this.
It's…
**Trask Stalnaker (Microsoft Corporation)** 30:07 I like that idea, though, like, from… Treating the website as the end, like, the user view… Because we're kind of mixing two things here in the Semantic Conventions repos of trying to make it user-viewable, as well as… Us.
Editing it.
**Liudmila Molkova** 30:31 Yeah, and also I kind of want to tell the whole story, but the whole story is too big now.
Okay.
We'll experiment with it, sorry for the…
**Mikolaj Knap (Google LLC)** 30:46 I will maybe schedule the park, but… Yeah, how? Maybe.
Separate the model from the markdowns, but you just have, like, generated and then auto-generated, clearly.
**Liudmila Molkova** 31:00 So, like, the generated are in the different files, and…
**Mikolaj Knap (Google LLC)** 31:05 No.
**Liudmila Molkova** 31:06 Text, like, the handwritten stuff just links to it.
**Mikolaj Knap (Google LLC)** 31:10 Yep.
But, it just depends.
**Liudmila Molkova** 31:16 Yeah.
I'll see. I'll see, we'll need to figure it out.
**Mikolaj Knap (Google LLC)** 31:25 Anyway… So, is it… so, okay, so, Was I missing something? Was it inherited, actually? Or…
**Liudmila Molkova** 31:33 No, it wasn't, you're right. So it seems it was, it was already there, for example, here, for the two calls.
**Mikolaj Knap (Google LLC)** 31:41 What do you call the bus.
**Liudmila Molkova** 31:42 Yeah, so, like, for the two calls, it just updates the note.
But it was not… it was inherited for the metrics.
It was not inherited. There is this… this is a new record, it wasn't here before.
**Mikolaj Knap (Google LLC)** 31:59 Okay, cool. I will clean up the AI slop, then, from the… I'm decent.
**Liudmila Molkova** 32:04 Do we need to note, Name of the agent.
performs that operation.
**Mikolaj Knap (Google LLC)** 32:31 Joe.
**Liudmila Molkova** 32:32 I would… like… It's a little bit nitpicky.
We can't… I feel like this… this node, we don't need it.
On the definition itself.
But when we reference For example, here, we say that for the inference, it's the human-readable name of the agent that makes the inference call, right?
I can also update the brief for the agent name.
For the invoke agent, and say… Oh, wait, for the invoke agent, it's already… it should already be accurate.
Right.
**Mikolaj Knap (Google LLC)** 33:29 Yeah, so just update the brief for the… Agent name and, inference level.
**Liudmila Molkova** 33:35 Yeah, so, like, if you drop this chain… if you drop this part, would… Anything look wrong.
Without this note.
**Mikolaj Knap (Google LLC)** 33:51 No, I don't think… I don't think it actually adds any clarity, that's a good point.
**Liudmila Molkova** 33:59 Yeah, so maybe…
**Mikolaj Knap (Google LLC)** 34:01 My Victor doesn't need to exist.
**Liudmila Molkova** 34:24 Cool.
**Mikolaj Knap (Google LLC)** 34:26 Okay, cool.
**Liudmila Molkova** 34:29 Done.
Looks good.
**Mikolaj Knap (Google LLC)** 34:33 Alright, sounds good. I will change it, and then probably next time we could come next week after Thanksgiving, we could come and discuss roll-up.
for this.
**Liudmila Molkova** 34:43 Yeah, I mean, it seems if, unless there is something new that you'll find.
It seems true, though. If you have…
**Trask Stalnaker (Microsoft Corporation)** 34:51 Mikolaj said, did you say roll up?
**Mikolaj Knap (Google LLC)** 34:54 Roll up, yes. Yeah.
**Liudmila Molkova** 34:56 Yeah, yeah.
**Mikolaj Knap (Google LLC)** 34:56 Oh, no, not this, though, yeah, yeah. Like, this is part of the same idea of attributing token spend, but just this, since, yeah, I'll fix it for later tomorrow.
**Liudmila Molkova** 35:07 Okay, cool. Yeah, I'm…
**Trask Stalnaker (Microsoft Corporation)** 35:10 forward to discussing Rollup.
That sounds tricky.
**Mikolaj Knap (Google LLC)** 35:14 Yeah.
Bye.
**Liudmila Molkova** 35:17 Cool, so then… Thank you. I think that's it, and we are canceling on Friday.
I want to hear.
**Trask Stalnaker (Microsoft Corporation)** 35:25 I canceled it.
**Mikolaj Knap (Google LLC)** 35:27 Alright, happy Thanksgiving.
**Trask Stalnaker (Microsoft Corporation)** 35:28 Post in the Slack, I didn't do that. Yeah, enjoy the, long weekend.
**Liudmila Molkova** 35:33 Yeah, have a… enjoy the quiet time, Mikolaj, and lack of the US people in your life.
**Mikolaj Knap (Google LLC)** 35:40 Thanks.
**Trask Stalnaker (Microsoft Corporation)** 35:40 Bye.
**Liudmila Molkova** 35:41 Thank you, bye.
