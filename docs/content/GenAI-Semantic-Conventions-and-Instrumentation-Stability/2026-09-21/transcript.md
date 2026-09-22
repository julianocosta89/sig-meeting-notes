SIG: GenAI Semantic Conventions and Instrumentation Stability
Date: 2026-09-21
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker (Microsoft Corporation)** 01:33 Hey folks, we'll get started in a minute.
**Aaron Abbott (Google LLC)** 02:13 Everyone?
**Trask Stalnaker (Microsoft Corporation)** 02:39 Ha, okay.
I added you up here.
**Aaron Abbott (Google LLC)** 02:45 this.
**Trask Stalnaker (Microsoft Corporation)** 02:52 Cool. Well, let's… get started, what I was thinking to do, and I kinda, Started with mine here is sort of putting a status.
And we can just kind of have a rolling status, if there is anything. It doesn't have to be a status every time, but… So, for the naming, category of things.
Which is… The big one is… This whole, kind of, proposed restructuring of the namings, instead of just having the one operation Span, splitting those out.
And the metrics.
And, so this was, Limil had sent as a first, Doing the first one.
And so what I will… I'll have for the next meeting, I'll get this into… ready to review.
And then… We can… review, or people can review asynchronously at that point. And then, once we get the first one, basically once we agree and maybe merge the first one, then I'll probably just send a mass number of PRs for all the others, because they should be all essentially identical.
I think there's some… there's a… bit more to this first one. I think there's a little bit more reorganization, Yeah.
The… For the token usage, So, this is also Ludmila's PR, that… I think, you know, there was kind of the, I don't know, last kind of question from you, Aaron, about sort of the naming.
And it sounds like, Ludmila has a preference for this, and I don't have a strong… Preference not to do it.
**Aaron Abbott (Google LLC)** 05:30 Same, I feel like we're at the… Bikeshed level, where we can… Just kind of go with one approach, especially if someone has a stronger feeling.
**Trask Stalnaker (Microsoft Corporation)** 05:41 Cool. So I know Lamila had, wanted to merge this end of date today.
So I will go ahead and… do that.
Merge. Yes, no.
Cool. And then for, this one… I will… for the next meeting, I'll… basically have a proposal of whether… I… I'm pretty sure I will… that we should split this into… Per… Like, the inference exception… Retrieval exception, all of the… basically, the same way that we're splitting up the metrics.
But I haven't thought… About it, other than very superficially.
So I will… Have a proposal for that for the next meeting.
And with that, I… Can pass to anybody else who has any, Anything you want to update, either, things that Are… have been done, or that kind of what you want to target for next meeting?
**Aaron Abbott (Google LLC)** 07:15 I can give a quick update on the… Please.
**Neil Yashinsky** 07:20 Yeah, please go ahead, Aaron.
**Aaron Abbott (Google LLC)** 07:22 Yeah, yeah, on this parts JSON schema one, I'm planning to, Tackle these… the kind of structural issues first, which were, like.
whether or not we should allow extra values inside of each of the messages, whether things should be optional versus allow null, kind of silly stuff like that. And then the other one was what we talked with Felix, I think, last week, on Friday about, which was, Basically, making the types so that they're less permissive, because right now they're just way too permissive.
And, yeah, that was probably just the first step, which would probably have some breaking changes.
**Neil Yashinsky** 08:09 Especially if we do it right.
Yeah. By intention, I feel like, because that's the point of, like, failing loud and making sure that for people who want to fail loud, it does.
**Trask Stalnaker (Microsoft Corporation)** 08:24 Yeah, and breaking changes are… are fine. I wouldn't… Try to avoid them.
**Neil Yashinsky** 08:32 It's a little bit of the point to, like, do them now, right? Before later?
Yeah.
**Trask Stalnaker (Microsoft Corporation)** 08:40 It will be the least of our… one of the lesser of our… Any breaking changes, so… Cool.
Anything else you want to call out or discuss about that one?
**Aaron Abbott (Google LLC)** 08:57 No, I think, we could just come with, like, a proposal.
Discuss Wednesday, maybe.
**Trask Stalnaker (Microsoft Corporation)** 09:04 Nice.
Anything you want to call out on the inference?
**Neil Yashinsky** 09:16 We didn't discuss this formally, but, like, informally, I think it makes the most sense to, like, we'll do schema, right? Make sure we have the schema, I think, tightened up, for lack of a better word, and then inference and tooling will kind of naturally flow out of the decisions that are made there. Aaron, feel free to disagree.
Yeah, okay.
**Trask Stalnaker (Microsoft Corporation)** 09:47 Cool.
Thank y'all.
**Neil Yashinsky** 09:53 Yeah, and I would say just one last thing.
**Trask Stalnaker (Microsoft Corporation)** 09:55 with tools.
**Neil Yashinsky** 09:56 Yeah, I would, you know, again, you know, I think inference comes before tools. There's a, you know, fair argument to be the otherwise, but it seems like we do inference first, and then it's like measuring is the better way to do once we have inference down.
That's my natural instinct.
**Trask Stalnaker (Microsoft Corporation)** 10:24 Cool. Any… Dylan, you got, volunteered for content capture. Thank you.
**Dylan Russell** 10:36 Sounds good.
Yeah, I'll read through these.
I think… Yeah, I'm also working on porting over some of the instrumentations from Open Inference.
I… will look at this, I guess, secondarily. I'm hoping I can wrap that up, like, this week, but… Yeah.
**Trask Stalnaker (Microsoft Corporation)** 11:05 Cool.
That's fine. Do you have… Yeah, do you have any sense on how much… Work… The… this is the, like, is this a… like, some of these are kind of bigger.
This one seemed… Content capture…
**Dylan Russell** 11:35 I know there's one… One issue we can't resolve until there's, like, a release of the OTELPython.
Because we… Yeah, to get this message content that NVAR is, like, tied up in whether we should omit the event, and we want to wait for that.
the hotel Python library to be released, so we can… Yeah.
**Trask Stalnaker (Microsoft Corporation)** 12:09 Yeah, Aaron, go ahead, we've got some hands.
**Aaron Abbott (Google LLC)** 12:12 Yeah, no, I was gonna say, like, I guess we should… Scope this a little bit.
And I think it's kind of independent of the implementation. We kind of just want to… Think about how we would implement it, I suppose, and… The biggest thing that comes to mind for me is right now, we've pushed everything down into the instrumentation, so… You have to make a decision whether or not you're gonna record stuff, you have to make a decision whether or not you're gonna upload it somewhere with these hooks.
Like, none of it can be deferred to a collector right now, unless you turn it all on at the bottom, so… Ludmila has, like, a draft PR, I don't know if she's widely shared it for representing Like, the blog references as well, which is kind of tied up in this, so… I guess my question is, should we just keep it scoped that way, where the instrumentation Controls all the, like, all the content capture happens at the bottom.
Go ahead, Trask, sorry.
**Trask Stalnaker (Microsoft Corporation)** 13:09 No, no, no, no, no.
Continue, I was just making connections in my head up to the reference stuff.
Yeah.
**Aaron Abbott (Google LLC)** 13:19 Yeah, well, I mean, that was most of my piece, I guess, was just whether… Like, whether we want to scope this to work with the collector, for example.
**Dylan Russell** 13:33 You kinda lost me there. What do you mean, scope what, to work with the collector?
**Aaron Abbott (Google LLC)** 13:39 So the thing we have in the spec right now is something about hooks?
Yep.
it seems, like, somewhat related to this, and that was a way to, in my opinion, just kick the can, I guess.
And whether or not we solve it for this first milestone.
Should decide if that's in scope or not for this first Stability milestone.
**Dylan Russell** 14:09 Okay.
**Aaron Abbott (Google LLC)** 14:12 Ankit, do you want to jump in?
**Ankit Singhal** 14:16 If you have the Python Instrumentation, I did see there was an option to say if I want to capture the, like, input-output messages for the tool call and its results on events.
Or attributes, or both?
And I think there was some configuration which had, like.
I don't know, events, or, like, I don't remember the name of those values exactly. Could that also be… Captured here.
**Dylan Russell** 14:50 Are you talking about the environment variable that controls whether an event is generated?
**Ankit Singhal** 14:55 Yeah.
**Dylan Russell** 14:57 Yes, yeah, I think it makes sense to, like, Resolve that issue.
**Trask Stalnaker (Microsoft Corporation)** 15:14 I don't remember… If Red Miller… Wanted to try to target… Look for LARD, the refs work.
Hook.
Is this as tied to refs, or is that more general than just refs?
**Aaron Abbott (Google LLC)** 15:57 It's a bit more general, Like, the up… the upload hook… upload is an implementation of the hook, but it doesn't have…
**Trask Stalnaker (Microsoft Corporation)** 16:10 I see, but that's the primary reason why we've added it.
Okay.
And then the… should it work with the collector?
That means… The refs?
Where the collector could extract them as refs, and how to do the upload.
**Aaron Abbott (Google LLC)** 16:44 Yeah.
Yeah.
I mean, I was kind of wondering about that, like, I think… We also discussed at one point.
Like, the idea that a collector would, act as an upload target.
For uploading the refs, too, so… I guess that would… Oh, it could be in context.
**Trask Stalnaker (Microsoft Corporation)** 17:08 Oh, okay.
**Aaron Abbott (Google LLC)** 17:10 Yeah, I mean, I think it's fine if we don't… Try to boil the ocean for this first go.
**Trask Stalnaker (Microsoft Corporation)** 17:25 Cool. Yeah, even just, kind of, scoping out, yeah, what these areas mean is helpful.
Let's see, what other areas do we have?
Agent Workflow Model… Any thoughts or anything you want to…
**Surya Teja** 17:54 Yeah, yeah, Trask. This is a dense, recommendation from Ludmila. There are a few moving parts, and I'm trying to whittle down to a few things that we can do before November, and I'm waiting to consult with her before I move ahead on that.
Once we have a few things outlined, I'm going to raise a PR for get them moving.
There are other asks, like… merging both workflow and, invoke agent spans.
An archaic crest, or someone who is… a person suggested using turns. I'm kind of trying to see how that gels well with, The existing thing, but… He suggested few… Renaming around few conventions, that sounds pretty easy and low-lift.
I'm just taking a look at that, and once, I have a… clear understanding. I can write down the timeline and how we can attack this. But in this present shape and form, if we try to attack it, it's going to be quite ambitious.
In my opinion, and it might not be ready for our November timeline.
**Trask Stalnaker (Microsoft Corporation)** 19:14 So, what… yeah, maybe, could you… Kind of give us a high level of the different pieces, because I was, the only part that I'm kind of familiar with is the discussion around whether the agent… invoke agent and invoke Workflow should be merged, or whether invoke Workflow should be merged into Invoke Agent.
**Surya Teja** 19:44 Yeah, yeah, so different pieces, let me just… let me see what my notes is.
Yeah.
So… The other thing is, First is merging invoking… invoke agent and invoke workflow, and the metric definitions that are associated with both these spans.
And the other thing is… have to, model it, what operation name we need, whether it's InVork Agent or Invork Workflow, and have to… Represent one.
And the third one is to have some span hierarchy around, there are nested agents and stuff, how to represent if there are… if there is an agent calling a sub-agent, and how the span hierarchy should be. And there is a… pull request for that. So those three are the proposals.
And, Based on that, we also have a few ideas from the commenter ask, adding, both Invork agent and invoke workflow metrics into one.
And Renaming them.
and also, using turns.
For, understanding how each… interaction can be modeled. So those are the high-level points around how to model this.
**Trask Stalnaker (Microsoft Corporation)** 21:56 Can you explain the, the nested, hierarchy? What are… what is the kind of open question there? Open questions?
**Surya Teja** 22:11 So… It's not an open question, actually. She, Lydmila already has a PR.
for, adding an attribute for a nested agent and workflow invocations.
So, it's not an open question, actually.
It's a proposal.
**Trask Stalnaker (Microsoft Corporation)** 22:40 Let me… okay, let me find that.
**Surya Teja** 22:43 It's 385, it's in draft status.
**Trask Stalnaker (Microsoft Corporation)** 22:52 Oh, the main ancient name.
**Surya Teja** 22:54 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 23:01 So, I think that is also tied into this agent identity and hierarchy question.
**Surya Teja** 23:12 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 23:13 categorized it there a little bit more than nested. So, this is as an attribute for that I… Okay.
Any… any challenges on the structure, the… Nesting structure here.
**Surya Teja** 23:37 I don't have a good answer for you right now.
I need to dig a little bit and give you a good answer with some examples to clarify that. And sorry, I couldn't go that deep on that.
**Trask Stalnaker (Microsoft Corporation)** 23:52 Oh, no worries. No, no worries. Yeah, that would be, yeah, super helpful, Amy, you know, in a future meeting, to kind of… Dive into this… Start, like you said, start kind of picking apart, you know, what are the different pieces there that we can extract and make progress on individually.
**Surya Teja** 24:16 Yeah, I mean, I have some notes that I want to present in either Wednesday's or Friday's meeting, showing what I have.
plan, and from there, once Lydmula is back, she is the one who created this, and she has some good notes around it, as well as PRs around it.
Based on that, I'll discuss with her and focus on what's achievable within the timeline, and just work on that rather than… Give you an ambitious plan without discussing with our own.
**Trask Stalnaker (Microsoft Corporation)** 24:51 Sure, so Lamila's out for another week and a half, still, so, I would suggest that, you know, we can… we can discuss in this meeting.
And tried to make, you know, we'll try to make progress, optimistically without her, and then, for sure, when she's back, get her thoughts and, any… she's got, veto power on, on everything there.
**Surya Teja** 25:22 Yeah, sure, Trask. Thank you.
**Siri Varma Vegiraju** 25:31 Yeah, I…
**Trask Stalnaker (Microsoft Corporation)** 25:31 Yeah.
**Siri Varma Vegiraju** 25:32 So, I did look into both those PRs and issues. It is mostly about clarification of the internal versus What happens when the… agent hosted on a service is being called. And… the PRs that are there address those Trask. So, I did look at them, and they look good. So, should I just tag you, or…
**Trask Stalnaker (Microsoft Corporation)** 25:58 You should approve the PR.
**Siri Varma Vegiraju** 26:00 Okay, I see.
**Trask Stalnaker (Microsoft Corporation)** 26:02 Yeah.
**Siri Varma Vegiraju** 26:03 I don't think I have permissions for review, it's,
**Trask Stalnaker (Microsoft Corporation)** 26:07 So your, your… you can approve it. Okay, yes. You'll… it just… you won't have a green checkmark, you'll have a gray checkmark.
**Siri Varma Vegiraju** 26:17 Yep.
**Trask Stalnaker (Microsoft Corporation)** 26:17 But that's fantastic, still.
**Siri Varma Vegiraju** 26:20 Sounds good. I will do that. And once I do that, should I just tag you and Ludmila, or is it just…
**Trask Stalnaker (Microsoft Corporation)** 26:28 So it will, It will go into… it should hopefully then end up in… We will see it naturally in the dashboard.
**Siri Varma Vegiraju** 26:43 Okay.
**Trask Stalnaker (Microsoft Corporation)** 26:43 But, that's part of what these kind of status meetings are for, is to, keep those things bubbled up to the top when they need attention.
**Siri Varma Vegiraju** 26:55 Okay, okay. Yeah, sounds good.
**Trask Stalnaker (Microsoft Corporation)** 26:58 So, I'll, let's see, so…
**Ankit Singhal** 27:01 If any help is needed on this, I can help take a look at this as well. Sorry, I was not available for the last meeting, so I'm missing some context, but I'll be happy to help.
**Trask Stalnaker (Microsoft Corporation)** 27:10 Oh, hey, okay.
**Ankit Singhal** 27:11 Yeah, I feel like there was something done to kind of, assign, work across people, so sorry about that.
**Trask Stalnaker (Microsoft Corporation)** 27:20 Yeah, yeah.
No worries, we are just trying to organize, all the work and make sort of parallel effort.
progress.
So, yeah, I mean, definitely all the PRs, you know, we will need reviews.
But certainly, any… if you have any… interest in specific areas, feel free to reach out to folks. It's fine to have multiple people, just kind of, if you have a little Slack, DM.
To coordinate.
**Ankit Singhal** 27:56 Sounds good. Okay.
forgive them.
**Trask Stalnaker (Microsoft Corporation)** 28:11 Alright, I think our last… When… Wolfgang, any… anything that you want to call out?
**Wolfgang Therrien** 28:21 I'm still trying to get my head around, you know, what's going on in these, six, five or six PRs, and I think a lot of it was already touched upon. I was, like, reading through them, and I was like, this seems related to some of the other, areas, so I hopefully will have a better sense of what can be teased apart, and what is, you know, what is small.
Versus, versus a little bit more bundled together.
**Trask Stalnaker (Microsoft Corporation)** 28:47 Sounds good.
And with that, we have a minute left.
Cool. Thank you all.
Thank you, Trask. See you on Wednesday.
**Neil Yashinsky** 29:03 Sounds great. Thanks, everyone. Bye.
**Aaron Abbott (Google LLC)** 29:04 Teladuke.
