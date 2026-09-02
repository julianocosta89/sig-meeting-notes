SIG: GenAI SIG
Date: 2026-09-01
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker (Microsoft Corporation)** 01:50 Hey, everyone!
**Neil Yashinsky** 01:54 Hello, Trask, how's it going?
**Trask Stalnaker (Microsoft Corporation)** 01:58 Good, thank you.
**Neil Yashinsky** 02:00 I'm glad to hear it.
**Trask Stalnaker (Microsoft Corporation)** 02:45 Alright, Neil, go ahead and drop your, popic down here…
**Neil Yashinsky** 02:52 Oh, yeah, thanks, sorry.
**Trask Stalnaker (Microsoft Corporation)** 02:53 Yeah.
**Neil Yashinsky** 02:55 Certainly.
**Trask Stalnaker (Microsoft Corporation)** 03:18 Alright, let's… Get going.
This was a discussion we had this morning.
And… The earlier meeting, I'm not sure if Arthur… hopefully someone from COSI will present to us here in this meeting. We request to ask for that, Some interesting work going on around, security and AI at the cross-sections, and work happening in OCSF and COSI.
And, Very interested to learn more about how we can… Benefit from that, or be involved in that.
Let's see, Ludmila, we discussed this a bit this morning.
Do you want to… Share here…
**Liudmila Molkova** 04:30 Yes.
**Trask Stalnaker (Microsoft Corporation)** 04:31 Summarize…
**Liudmila Molkova** 04:33 Yeah, so… for everybody who hasn't been here in the previous call, we've been chatting about stabilization, and it's been a long-term, like, goal for the SIG to also produce a set of stable conventions and some of the instrumentations.
And I think we are close to the point where we can do this. We still have a bunch of refactorings going on.
But I think we… if we have energy in the group.
And by energy, I mean people, specific people who are ready to commit to this work, probably at the cost of the future work.
And I… I am committed. I think, Trask, you mentioned you're committed, but we are looking for a few other folks who want to participate in the stabilization effort.
and what Trask proposed, and I really like that we could have maybe a separate call, or a couple of short calls a week, which are more like, okay, let's go through the project dashboard, let's speak issues that we work on, let's prepare the PR and, like, review this next time.
And this will be a very focused effort. Will probably be, very, scoped-down, approach. Like, find the minimum viable, thing we can stabilize, and postpone, like, complicated features that can be added later.
To the later point. I think the most important thing besides the energy is the scope.
And I think there are a couple of possibilities. I think the inference is kind of easy, but it might be, too narrow.
And… One thing we've been worried about is that if we call inference stable, people will not look into the details, and would assume that the agents are also stable.
And we will be back to this vicious cycle of breaking changes and breaking people's trust.
So… I would like to try to find the scope within Agentic frameworks that we can stabilize.
It might be, like, just a couple of spans and their corresponding metrics, and, like, the core parts of how we capture the agent information.
And if later we need to add some more details, we can do this.
The hope that, let's say, if we… I'm being optimistic, but if we call a subset of things stable by the end of 2026, In 2027, we can… have a new major version, which was some… not significant, probably, hopefully, but breaking changes. It's like, we reserved the room to make breaking changes, and we… we should target to have V2U sometime 2027, 2028. If not perfect, but yeah.
I would like to keep a lot of, other features out of scope. No harnesses, no live real time and the initial stability, like, if it's not the core part of Agentic framework, it's out. It doesn't mean that people cannot keep working on this, it means that the stability group will not focus on them.
And… I have some ideas about what we, like, big, big rocks we need to resolve before we can, call stability. We can talk about them, but first I just wanted to hear what you folks think, and if we have people who want to… Work on destabilization.
**Trask Stalnaker (Microsoft Corporation)** 08:51 Yeah, and probably what we would ask for once, once we gather, you know, group of folks is… Like Liudmila mentioned, we have had… we've gone through this stabilization process in the past with HTTP and database, and what worked well in the early stages of that was… two or three half-hour meetings a week as sort of these checkpoints. There's kind of a lot of churn and little discussion topics, and just to check in that we're, you know, making progress.
For, you know, probably, like, a two-month Period, until things sort of… calm down, hopefully, and we're, you know, more kind of ironing out the last things and looking at RC and whatnot.
And yeah, it's one of the… One of my worries of not Stabilizing as we've been, building out the conformance repo.
Has been, we have a lot of external people using GenAI… the GenAI semantic conventions, and with the conformance repo, we're saying, hey, we really want people to support GenAI semantic conventions, and we really want there to be an industry alignment. But if we just keep churning out more versions, of, breaking changes, over versions, then, you know, like, what are we asking the industry to conform to.
And so the, topic… one… one reason we've been really hesitant, I think, to make a release out of the new repo.
has been… To not put out yet another GenAI target version that people, some people will align to, and some people won't, and, like, which one are we asking, you know, people to conform to, etc.
And so, yeah, the… I think… Stability would be really amazing for the conformance project.
Surya?
**Surya Teja** 11:32 I was lost in my windows. So, a question, I was late to the meeting, This might be a stupid one, but what do you mean by standardizing the conventions? Like, how is this going to help, and… What is going to happen after we standardize the conventions?
**Trask Stalnaker (Microsoft Corporation)** 11:53 stabilize…
**Surya Teja** 11:55 Yeah, stabilis, yeah, sorry.
**Liudmila Molkova** 12:00 Well, the… the status, right? So today, we have maybe 10 different versions of cementiage and AI semantic conventions, and people randomly follow them. They are all in development. We reserve a chance to make breaking changes, from what I see, at least, in the… bigger and small corporations, companies working on observability, it hurts a lot, because they… they build the UI, and it becomes irrelevant months later, and they need to support multiple versions at the same time, and they cannot We cannot provide any guarantees, and it essentially hurts the reputation Our reputation, because people at some point learned that this all was not guaranteed, and they built so much on top of this.
**Surya Teja** 12:51 That answers my first question. I have another question. Ludmila, this is for you.
In order to help.
You said community participation, what… kind of things you need. You might have mentioned it, but if you can elaborate what… how we can help, that also will be helpful. And this answer… this is my last question.
**Liudmila Molkova** 13:11 Yeah, so during the working group, like, that, branch of the working group, we would go through… there is, the example of the project board, which essentially divides things into entreeaged, target for stability, and, post-stability.
And it's just initial, bucketing.
might be a little bit imprecise, but we'll work through it. So we will first start by, triaging and, Picking the things that we… Can start working on.
the things in semantic conventions that we would work on is something that's essential for these two layers, or whatever the scope we identify. Like, without them, observability doesn't make much sense. It's not a good experience, not even the average one.
And then, we would see what's… what are the open issues around this. So, for example, for inference, we would find that the metric names are wrong.
We don't have a good separation between the spans and the, like, we report everything on their operation duration, and it falls into inference Agentic and everything. We will go work on PRs that refactor the parts and separate, let's say, inference metrics from Agentic metrics.
We're about… dive more into the instrumentations, and, like, with the conformance, it's kind of easy. We can see that, for example, response ID is reported by maybe a half of instrumentations. Maybe we should change the requirement level for it, and so there are, like, big rocks, the things we need to change in semantic conventions.
That would be breaking otherwise.
And that we want to stabilize, and there are changes in instrumentations that would also drive some, maybe, minor stuff in semantic conventions.
The help that's needed is, to actually go and do stuff in semantic conventions and drive PRs through, like, the round of reviews. We will actively review PRs and talk through, like, points during the calls.
And we will try to untangle complex discussions and just work on the things that are important for stability.
we will need to update instrumentations accordingly. We'll need to make sure the Python GenAI repo is in sync. It's out of sync, even currently with the semantic conventions that we have.
And there are some ways we can make it easier, but we need to take care of it.
And JavaScript instrumentations also would be awesome. So having instrumentations in more than one language would definitely help.
And if we declare stability for, let's say, this, the semantic conventions, we'd probably Near the same time declare stability for, some of the instrumentation libraries.
**Surya Teja** 16:25 Yeah.
**Liudmila Molkova** 16:26 Trask, yeah.
**Surya Teja** 16:27 Yeah, well, so what I understand is you need a triage who can help drive the PRs and, Prioritize or organize them?
for SIG to… spend time around it. Is this understanding right?
**Liudmila Molkova** 16:45 Well, if you want to do it a triage job, it's… it's good. I think we need people who would also do the changes in semantic conventions, and… instrumentation library. So we will identify some specific issues, and I'll be trying to assign an owner to an issue, and we would want the owner to come back within the same week or the next week with some, maybe, proposal. So it's like.
a short… a short-term project. So we… if we were absolutely aggressive, we would be… we would try to stabilize it by KubeCon, like, in two months. It's a very short timeline, but, like, double it, and by the end of the year, I think it becomes more feasible. But it's a short effort, it's not something you take and you work in, like, two months once you have time.
**Surya Teja** 17:38 Yeah, got it.
Thanks, Luke.
**Liudmila Molkova** 17:45 Thank you.
**Trask Stalnaker (Microsoft Corporation)** 17:49 Yeah, Aaron.
**Aaron Abbott (Google LLC)** 17:51 I'll just say, plus one, I think this is a great idea, and I feel like we already, like, I guess this is what you were saying, Trask, but I feel like we have some de facto stable stuff, especially with the conformance repo set up, and Yeah, I guess it'd be helpful to know what the downsides are, or, like, what's the risk here if we stabilize stuff before we're ready?
**Liudmila Molkova** 18:20 Future breaking changes.
**Trask Stalnaker (Microsoft Corporation)** 18:21 Yeah.
You know, we do… we do like to put, a good amount of thought into, you know, as we stabilize things, so that… to make sure that at least we have a consistent story across semantic conventions, different domains, naming structures.
A lot of different factors, But we had already kind of… decided in this… in the generative AI space that we… there was… We weren't… in other domains, we were kind of unsure of what future major version bumps looked like. And there are such stable domains that we felt like we could probably, do pretty good on V1. For example, HTTP V1 has been out for a few years now, and, you know, we haven't had any, need to do a V2.
That will probably… hopefully continue. The GenAI space, we acknowledge up front that That's not gonna be the case, and so, you know.
We don't want to let perfect be, you know, the enemy of getting something… getting all the benefits that we will get out of having a stable release.
**Aaron Abbott (Google LLC)** 19:55 Yup.
I totally agreed, and I'm thinking back to when we federated the semantic conventions for GenAI, and I think, That was also in a step that, if things do change, like you said, the industry's moving quick, we can… make more releases as we need, so I… I don't know if we know how long we would want to keep this stable for. We have, like, we're gonna work on some stability guidelines specifically for GenAI, besides the general hotel ones, but… Yeah, any thoughts?
**Trask Stalnaker (Microsoft Corporation)** 20:30 Not… I mean, I think it's… fee as we go, like, obviously, we don't want to, I think, I… I think once we do a stable release, often there's just an amount of time that it takes for, you know, instrumentations and people and everything to catch up.
And so there's kind of a natural time there where we can introduce breaking changes still, under the development status.
Right, so it doesn't stop us from adding new features or, you know, even conflict… making changes. It's just that those would be under development status for some period of time.
And again, like, we want to give… like, I think the conformance testing is a really good thing to think about through, because the same motivation there of getting the industry to align on something.
Right? It doesn't help us… If we get the industry to align on 10 different versions of OpenTelemetry's GenAI semantic conventions.
That's just… Almost as bad as, you know, having multiple completely different semantic conventions out there. So we do want to, you know, give people a chance to target a version and not feel like, you know, it's just Yeah, a chance to… Get most people emitting a particular version before, you know, we then go and bump To another.
And yeah, hopefully we can continue, you know, most of this stuff will be additive and not, you know, breaking there. Definitely it's not our intent to, you know.
continue breaking these core things as to put them in, you know, a decent state that, okay, now we can start working on all the other… focusing on all the other GenAI stuff, and that's all gonna take time.
And it's gonna take time for the industry to converge and whatnot, so… I mean, honestly, I would be surprised if we… feel like we're in a position to have a V2 you know, anytime soon.
**Aaron Abbott (Google LLC)** 23:15 Yep, no, I… I think I… That all sounds great, we don't… need to target, V2, I guess.
Yeah, I feel pretty good about the stuff that's in the scope here at Inference, and Token counts and whatnot, so…
**Trask Stalnaker (Microsoft Corporation)** 23:34 Cool, so… Yeah. Go ahead.
People who are interested, you know, ping Ludmila and myself on Slack.
And we'll then, once, you know, maybe… Tomorrow, we will… try to… try to let us know soon, because we'd like to get these meetings going, and so, tomorrow we'll send out a meeting poll to try to find times.
**Liudmila Molkova** 24:09 Sounds great. I'll post in the GenAI instrumentation Slack channel.
Yeah.
**Dylan Russell** 24:16 I have a question about the… Instrumentations.
Do we… Just say the instrumentations are stable right now.
Or do we say, like… The part of the instrumentations that are setting, like, the stable semantic conventions.
Like, those parts are stable.
like…
**Liudmila Molkova** 24:40 Now nothing is stable, right?
**Dylan Russell** 24:42 Okay.
**Liudmila Molkova** 24:44 They even have the beta, prefix, whatever, the beta annotation in the version.
But I would like us to stabilize instrumentations around the time.
the semantic conventions are stable, where if, like, I think in Python there are problems, because we would need to depend on a development version of OpenTelemetry instrumentation, the core package.
Maybe we can declare them RC, at least?
And work on the up and telemetry instrumentation stabilization within the Python SIG then.
**Dylan Russell** 25:24 Okay.
And the idea is to stabilize the whole instrumentation. Just, like, mark the whole thing as stable.
**Liudmila Molkova** 25:35 Yeah?
I mean, we can talk more about this, but yeah.
**Dylan Russell** 25:39 Due.
Okay, yeah, that sounds good. It seems like we would want maybe some way of saying, like, these… this part of the instrumentation is stable, or like… Yeah.
**Liudmila Molkova** 25:51 We would probably have, like, some experimental feature opt-in.
And it can be global, it can be, more granular, we'll decide. And we can, in theory, keep something like instrumentation, the completion hook, as experimental for the time being, or other parts. So, like, instrumentation will not expose behaviors that we don't consider stable.
But the API shape.
We would need to stabilize it.
**Dylan Russell** 26:23 Right.
Okay.
**Trask Stalnaker (Microsoft Corporation)** 26:26 Yeah, that's what we've done in Java, is we've stabilized instrumentations, is anything that's not stable, we hide behind a feature flag.
And for API shape, we have, like, a non-public experimental, very clearly labeled experimental.
way to enable those experimental flags so that that's not part of the public stable API.
**Dylan Russell** 26:57 Great.
Okay.
Makes sense.
**Trask Stalnaker (Microsoft Corporation)** 27:06 Alright, let's move on. We've got, several topics… Vanilla…
**Liudmila Molkova** 27:14 It's just a short announcement. I learned about this today. Somebody pointed out to me that, the, Claude caught… now it meets some of the hotel semantic conventions, on OTLP. It's like they, it meets some of the attributes. I think if you scroll down, you'll see some of them. By the way, they report spend type attribute.
It's the, like, you see the previous version, the 136 whatever, GenAI.system.
And there are some sprinkles, it seems that they just added a few attributes.
Aww.
that are in conventions in addition to what they had. So, To remain stable and not break their users.
It's kind of cool. Unfortunately, we have this versioning problem with old version that they follow, but I think it's awesome, and I'll try to play more with it and see.
And maybe, Surya, it's related to the discussion we had, that, the… maybe it's part of the Cloud Agent SDK that you wanted to instrument.
**Surya Teja** 28:27 Yeah.
Yeah, this is actually a great step forward, because, We are in a limbo because Cloud code is not accessible to outside, and we don't know how we can instrument clot agent SDK. We can do it, but I don't know, since we prefer native instrumentation.
**Liudmila Molkova** 28:48 Yeah, and it's probably a good thing to try it out. I'll probably try with Cloud Cod, the binary, and yeah, if you want to try with the SDK, it would be cool.
**Trask Stalnaker (Microsoft Corporation)** 29:05 Alright, Marisa?
**Marisa Boston (Reins AI LLC)** 29:08 Hello, everyone. I think that this is just really simple. Ludmila, I saw that you were on the branch for this one. Just want to make sure that you guys aren't waiting on us for anything. I think it looks… like, things are okay. I just, saw that the branch was out of date, so I updated it, but, just wanted to see next steps, because we haven't gone through this process before, so I just don't want… I just want to make sure we're not missing anything or causing you guys extra work.
**Liudmila Molkova** 29:41 No, I didn't have a chance to re-review, sorry about.
**Marisa Boston (Reins AI LLC)** 29:45 Oh, okay.
**Liudmila Molkova** 29:45 I'll take another look. For some reason, it doesn't appear on our project dashboard. Where does it, what's the status?
**Trask Stalnaker (Microsoft Corporation)** 29:53 Let's see… Oh, okay. So it wants merged?
Says there's two threads… Unresolved, let's see.
**Marisa Boston (Reins AI LLC)** 30:10 I think we fixed those, but…
**Trask Stalnaker (Microsoft Corporation)** 30:16 Yeah, let me see why, but, like, in any case, if that happens, just as the author.
So Manish, or one of us, dashboard, route, reviewers… It shows in this, comment here, if the status doesn't look right, gives you this.
command.
**Marisa Boston (Reins AI LLC)** 30:44 Okay, got it. And so now it's there, and nothing else from our side?
**Trask Stalnaker (Microsoft Corporation)** 30:51 Yeah, and that dashboard, for everybody, if you haven't seen, is over here, and this.
**Marisa Boston (Reins AI LLC)** 30:58 Okay.
**Trask Stalnaker (Microsoft Corporation)** 30:58 just helps us, to know what's waiting on reviewers, since most of us are in GitHub notification bankruptcy.
**Marisa Boston (Reins AI LLC)** 31:08 I bet. Yeah, that's why I wanted to check. I wasn't sure, and we… I… we're still trying to figure out a lot of this stuff, so thank you guys so much, by the way, for all of this. So, it's in reviewer. Liudmila, if you have any questions, we're available, like, on Slack or wherever.
**Liudmila Molkova** 31:25 Yeah, thank you.
**Trask Stalnaker (Microsoft Corporation)** 31:29 Cool. Alright, Ankit.
**Ankit Singhal** 31:33 Hi, so I have, so, first of all, thanks, Liila and Dylan, for the review comments, so… I went through them, I think I had another set of conflicts that came up. I've resolved them, along with the comment reviews. I know, it's gonna happen, but it's easier now with Copilot to resolve those things. I don't have to go do them.
That's good. So, I have resolved most of the comments. Please do review, and if there are any more feedback, would be happy to cover them as well.
Most data from my side, otherwise… I feel like, yeah, ZRA is moving along, so that's good.
**Liudmila Molkova** 32:14 Yeah, thanks for putting it together. Yeah, how do you feel about the speech versus other modalities in life?
**Ankit Singhal** 32:23 Yeah, so I think I did some digging last night, so, I feel like for the speech that user spam makes sense, like user input spam. I know the name might be slightly different, as per the feedback, but I feel like for the other modalities, it just didn't really… At least my opinion was maybe that could be separate, which that could be directly on the… span for the actual generation from the model, because we don't really wait for that to finish. Customer just adds, like, text as we do for the models, right? The text models, or images.
But yeah, I think I put my finding in the comment as well, so if you'd like, I can share with you.
**Liudmila Molkova** 33:09 No, thanks, I'll take another look, appreciate it.
**Dylan Russell** 33:15 Did you decide… How to… If you want to capture, like, actual audio and video.
Or what to do about that, because you can, like, have, like, actual, like, audio files and, like, video files attached to the request.
Which seems like it's probably, like, too much to put in the actual instrumentation, but…
**Ankit Singhal** 33:38 I was hoping, like, and this is for the generation, right? Or even for the encodeon?
**Dylan Russell** 33:48 Yeah, I think both input and output can be audio and video.
**Ankit Singhal** 33:53 Yeah.
So, I was hoping, like, we can probably use as much as we can from the, text model, because I think there also you can do input for inference paths, and… Having… If you can reuse as much as… And if we still see any gaps, I'm happy to… Happy to discuss more on this.
There are, I think, messages… I forgot that.
Yeah, on the text model as well, like, you can have messages which can have, like, other modalities other than text, so…
**Dylan Russell** 34:44 Okay Yeah, I feel like… I don't know what the size limits are, but I suspect it might be, like, too big to put onto the… Span, or the event.
**Ankit Singhal** 34:59 I think there are file parts as well.
Which can lead to, like, files which aren't, like, are, like.
Right. Sweets are stored somewhere else, right?
**Dylan Russell** 35:11 Yeah, yeah.
**Ankit Singhal** 35:12 So, we can definitely go that route as well.
alerted.
arguments.
**Liudmila Molkova** 35:20 I was thinking that maybe buffering the whole audio is… Opt-in.
of behavior, opt-in on top of opt-in, so we can have the content capturing mode for live sessions to have a variation where the content goes onto per-chunk events. We didn't define per-chunk events for, like, text.
Because, it's too overwhelming, but for the… Chunks that are… Audio samples.
Might make more sense, and the content would go there, so we don't at least buffer in memory.
And we don't stamp it as a whole on the final span. But I feel like we can probably think about it as the evolution of the opt-in behavior.
But in some cases, buffering might be okay.
**Ankit Singhal** 36:19 For the cases where buffering might not be okay, we are suggesting have those chunks carry the actual content as well.
The chunkier ones?
**Liudmila Molkova** 36:31 to introduce Chunk Events.
**Ankit Singhal** 36:34 Sorry, could you repeat that?
**Liudmila Molkova** 36:35 to introduce chunk events. We don't… we don't have chunk events yet.
**Ankit Singhal** 36:39 Hi, I see.
Okay, so for, if I understand it, default behavior would still be that we can buffer and… Put that on the spot.
**Liudmila Molkova** 36:52 So the default behavior, we don't capture content, right? Because the content is opt-in.
**Ankit Singhal** 36:58 Yeah, great.
**Liudmila Molkova** 36:59 We have today opt-in flag to capture buffered content.
So maybe we should evolve this flag to introduce more of options.
And… Okay.
Yeah, part of the stabilization work would be to give this, either the legit stable version of the opt-in flag and config probably configuration, but, like, for now, we can treat it as… In theory, we can break it or introduce a new one.
**Ankit Singhal** 37:30 Okay, and by default, for the opt-in one, if I say I want to opt-in, we would buffer the content and put that on the span at the end.
Something else.
**Liudmila Molkova** 37:40 This is the existing behavior, I think, what Dylan is asking, if it's a good idea.
**Ankit Singhal** 37:45 Yeah, yeah, no, understandable, yes, good, yeah, okay.
Okay, no, that makes sense.
**Trask Stalnaker (Microsoft Corporation)** 37:55 Surya.
**Surya Teja** 38:02 Yeah, Google recently released a model for transcription or something. Are we targeting that in… over here?
**Ankit Singhal** 38:12 It's not in the plans right now, but if it's very similar, we can look into it.
But if it's very difficult, maybe… would prefer a different, PR for that.
**Surya Teja** 38:24 Yeah.
**Ankit Singhal** 38:24 But yeah, happy to discuss. Cool, exactly.
**Liudmila Molkova** 38:27 I think the transcription is kind of special. It uses the same API and everything, but when you use the transcription model, you don't get, like, back and forth.
it doesn't try to interpret the pauses in your speech, it's just that the bidirectional stream with no synchronization. As I talk, it transcribes, and, like, it's… There is not, there are no spans at all. There are only chunk events.
And it can last 4 hours. Okay.
**Surya Teja** 38:59 Okay, yeah, makes sense. It's not aware of it, actually. Thanks.
**Liudmila Molkova** 39:05 Thank you.
**Trask Stalnaker (Microsoft Corporation)** 39:12 Alright, anything else you wanted to… bring up or call out about that PRO Ankit?
**Ankit Singhal** 39:20 So, yeah, I think one thing that came up, probably last week or a week before that was… About the session events, and where to put them.
I think, yeah, that's, I think, is still an open question that I don't know about.
**Liudmila Molkova** 39:39 You have a proposal for session events, and it looks okay? Like.
**Ankit Singhal** 39:44 Okay, that looks okay. Okay, then, yeah, I think, probably, Aaron had some… Feedback as well, Aaron, if you would, Would appreciate if you can take a look at this proposal and see if the session even says model in that proposal next year.
**Liudmila Molkova** 40:05 Yeah, thanks.
**Ankit Singhal** 40:11 Alright, thank you.
**Trask Stalnaker (Microsoft Corporation)** 40:12 Thanks, Ankit. Neil?
Benchmark and Tournament.
**Neil Yashinsky** 40:19 Yes, thanks, everyone. Let me just throw one last link in here. No, actually, I'll do it afterwards, if people are interested. Just focus on the attention and the time I have. I have a few slides, I feel like, just to… to make it more clear, but I'll try to go kind of the 2-minute version, and if people want more details, we can… we can dig in for there, because I certainly respect everybody's time.
And, I, me and the folks at Context Core, I definitely, way more than just me, let me make sure I can share a screen here, have, been thinking about, like, what is the best way to.
Evaluate the capabilities of… what I like to call LLM, like, code generation, and whether or not it qualifies as building software.
And so, a lot of great work out there. The best one on this topic, I think, in my personal opinion, is, I don't know how it's pronounced, the SWE benchmark or whatnot. And, it's focused… on, you know, lots of issues that are already existing, and it has a really great, broad view of things. But in some ways, like, it left a lot of questions for us. And specifically, like, yes, it can create a fix, if you will, but how good is it at Actually building something that is stood up and run.
And so… What we did is we took the Google Microservices boutique, among other things, but that's kind of the focus, because it's a pretty robust and well-established Application, and we start by… Asking all of our models to build services in isolation?
And then we go forward, to asking it to build all of the application together.
And then stand up and run.
And so that's kind of the depth that we want to go in. And so we do it across the five languages that are represented there, and we, like I said, it's it kind of brought us to one last question, which was, like, okay, this is a really good measurement.
But, but we, you know, I, you know, in part, drove this, like, how much… is enough enrichment in the prompt in order to get the best results for your money? In other words, if we took a look at the three levels of task prompt instructions or whatever.
You could be very terse and say, like, this is the service, you know, implement it. You could provide a little bit more structural guidance around On how that could work, or you could do very specific instructions, what we call binding and advisory.
And… you know, what we've found is it varies, and some application… or some models, I should say, do really, really well.
with… with some, and others, you know, the more… seems like, generally speaking, like, the more capable models do better with raw instructions. But, you know, we're not… we're not deciding that. Obviously, the whole purpose is basically across those dimensions.
How well do the models score, given these three stages, if you will, or levels of prompt enrichment or prompt depth. And so, we are doing… I think there's 33 models that are included in the benchmark for this time around, and so… you know, this is how the measurement in terms of scoring works, and, you know, you talked about the quality, but also, like, the cost is a part of this benchmark as well, and the speed and the token usage is, you know, interesting, but I'd say, you know, kind of the real focus Is… is largely around quality and cost, and speed.
And then, because enterprises are being asked oftentimes to adopt not, like, you know, A model, or A models are asking to usually sign up for a vendor, you know, it became… clear that it would be useful to show these both in an individual level, as well as kind of as a squad, if you will. Because… You know, in our research, we found that, like, a good variety of, you know, high-performance and low-performance models may offer the best cost-effective solution… cost-effective solution, pardon me, at using this approach, and so this is essentially… or this is the, the, the structure, of the entrance, and so across the, like I said, it's 33 at the moment. There may be a little bit of changes as the week we're finalizing, but it works across these teams, and so we're providing what we thought was a pretty broad view across the… more mature, more robust, offerings, as, vendor teams. And so… Yeah, that's, I think, that's, I think, pretty much it. And then, just one last thing is, like, structurally, we're doing, also what we call the Pro-Am division, and so to start all this, we're running local models that we host, and… and evaluate, and it's not officially as part of the benchmark, but it's really useful for means of Validating, the harness, etc.
So, yeah. Thank you so much for your time. Oh, one last thing, yeah, this is a… we built this heavily on both OTEL standards, as well as, you know, the, the, semantic conventions, and, you know, the GenAI, A2A, as much as we could, really, to avoid, you know.
recreating something that was already there, and also, you know, kind of modeling and adopting as much as possible in terms of, you know, the richness hotel provides for tooling.
**Trask Stalnaker (Microsoft Corporation)** 46:33 Cool, so you are, these are all the metrics you're getting out of, from, I guess, token usage, cost, that kind of thing are… Open telemetry metrics?
**Neil Yashinsky** 46:50 So…
**Trask Stalnaker (Microsoft Corporation)** 46:51 what exactly are you leveraging? I mean, you're emitting open telemetry But what are you doing with that data, if anything, here?
**Neil Yashinsky** 47:03 So, we use OpenTelemetry data for, basically, a few parts. So, so, you know, one is it's… heavily involved in the quality, assurance. You know, we've already ran these, so we know what they are supposed to do, leveraging, like, all hotel offers, and The tooling that we run is all built on, you know, these standards, and so it's a good example of how they work, and then I think one other part of the questions was, like, what's available from the hotel? Is that what your other part of your question was, Trask? I want to make sure I answered it fully.
**Trask Stalnaker (Microsoft Corporation)** 47:41 No, more like, what are you… so you've integrated OpenTelemetry in here, you're emitting telemetry.
**Neil Yashinsky** 47:50 Huh.
**Trask Stalnaker (Microsoft Corporation)** 47:50 following OpenTelemetry. My question is, what are you doing with that telemetry, if anything?
**Neil Yashinsky** 47:58 Oh, yeah. So, actually, all of the evaluation, scoring mechanisms, etc, is built using and reporting OpenTelemetry, and so it's all first cataloged in a time series database, you know, OpenTelemetry backend, and, in addition to that, we have… Basically, context scores raison d'etre is, like.
Opentelemetry is a great way to… encode not just application data, but business data. And so, if you think about a lot of the output from this is, like, hey, this model built this, you know, this capability, this service, or whatever.
And it costs this much. And so, we package that as a trace, as an OTEL trace. I mean, there's another mechanism, too, if you don't want to use that, so you're not forced to, but hotel's a great, what we like to call a narrow waist.
And so everything has, you know, an expression as OTEL, and so that serves as a really useful model for us to encode, the, you know, all of the information about this, and so we use, you know, dashboards are querying that and showing all the scoring, etc.
**Trask Stalnaker (Microsoft Corporation)** 49:15 I see, so it's, it's, the standard GenAI telemetry plus you're layering in, sort of, specific attributes and spans and things that you need into that… those traces. Nice! Yeah. Nice.
**Neil Yashinsky** 49:29 As well as, like, the agent's work itself is a trace. You could go and follow that as an OpenTelemetry trace, like the client-side execution.
And so, you know, sessions are related. Issues in, like, that you committed to the repository represented as traces as well, so you have a kind of a running track of what your agents are working on as well.
All hotel-based.
**Trask Stalnaker (Microsoft Corporation)** 49:58 Cool, definitely throw some links in the, meeting notes.
**Neil Yashinsky** 50:02 Will do, thanks. Appreciate everybody's time.
**Liudmila Molkova** 50:05 Thank you.
**Neil Yashinsky** 50:08 Stop sharing.
**Trask Stalnaker (Microsoft Corporation)** 50:12 Alright, Lyd Miller, you have the last topic.
**Liudmila Molkova** 50:16 Yeah, so… I have… we… I've tried to solve this problem for a long time, and this is the token usage. We had some, discussion with Alex in the comments, and he proposed a naming option that I kind of really like.
So, if you scroll, I think it's in the PR description.
So… the… The histograms, this is the naming pattern for histograms.
And below… There is the breakdown for tokens, for… sorry, for counters, and it's the same, but with detailed part.
There are, like, 3 other options below.
And they all are a bit awkward, so the challenge here is to separate like… Histograms from counters.
And option 1 was here before.
Yeah, this one.
And it's absolutely unclear from the naming, what does it mean? Like, and what's the difference?
I think Alex's proposal solves it better. I have, like, a couple of other options listed below, but… formally… like, I have approvals, I wanted to settle around on the naming, so I would appreciate people Thinking about it, and if you have immediate Knee-jerk reaction about this one, let me know.
**Aaron Abbott (Google LLC)** 52:06 Which… which one was Alex's proposal?
**Liudmila Molkova** 52:08 This one. It's implemented now.
**Aaron Abbott (Google LLC)** 52:12 The detailed one.
So, detailed means, Herb.
**Liudmila Molkova** 52:18 It means it has modality as a dimension.
**Aaron Abbott (Google LLC)** 52:21 Okay.
**Liudmila Molkova** 52:22 And it's, like, the… If we have more, like, two Leos, we would also put it here.
So it's like, it's the breakdown.
**Trask Stalnaker (Microsoft Corporation)** 52:34 But more importantly, It's the counter.
Versus the histogram.
**Liudmila Molkova** 52:42 Right.
So I had a proposal with, like, using .count.
And I think it's option 2 or option 3.
And it… Looks awkward.
Not because of the dot count, but because of other reasons.
**Trask Stalnaker (Microsoft Corporation)** 53:13 Cool. I will definitely take another… pass over…
**Liudmila Molkova** 53:21 Okay.
Maybe we can combine them, and we can have detailed input token.count, and it would be… Obvious.
**Trask Stalnaker (Microsoft Corporation)** 53:33 That's so long. Yes.
**Liudmila Molkova** 53:37 I'm glad they increased the metric length to 55, because I think the longest one here is 63 or something already.
**Trask Stalnaker (Microsoft Corporation)** 53:47 Yeah, Ankit.
**Ankit Singhal** 53:50 There's something recently came up about short tokens and long tokens.
Have you considered that as well here.
**Liudmila Molkova** 54:00 Can you point to some sort.
**Ankit Singhal** 54:02 I appreciate it.
**Liudmila Molkova** 54:03 I have no idea about short and long talkings.
**Ankit Singhal** 54:06 Yeah, let me share a link to that in the chat, yes. It's something new that came up recently in OpenAI. Somebody pointed out to me internally, so… Beautiful.
**Liudmila Molkova** 54:19 See, we need to stabilize before new stuff comes up.
**Ankit Singhal** 54:27 Yeah, I feel like, I think, that short and long program might be very relevant to this PRFS as well.
**Liudmila Molkova** 54:35 Awesome.
I'll leave a comment to investigate.
**Trask Stalnaker (Microsoft Corporation)** 54:44 All right, any last things anyone wants to chat about?
Otherwise, we are almost exactly at our 5-minute… well, I try to… In other meetings, I tried to have a 5-minute cutoff.
Target 5 minutes before the hour.
**Neil Yashinsky** 55:05 Nope.
**Trask Stalnaker (Microsoft Corporation)** 55:06 So we are right on time.
**Neil Yashinsky** 55:09 Very human thing of you to do, Trask. Excuse me. I get all choked up.
**Trask Stalnaker (Microsoft Corporation)** 55:17 Alright then.
Thanks, everyone.
**Neil Yashinsky** 55:21 Thank you.
**Liudmila Molkova** 55:22 Thank you.
**Neil Yashinsky** 55:22 Have a good day.
