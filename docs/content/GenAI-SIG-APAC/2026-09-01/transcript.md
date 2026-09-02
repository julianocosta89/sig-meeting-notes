SIG: GenAI SIG (APAC)
Date: 2026-09-01
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Victor Lu** 00:39 Oh, Nida?
**Nida Hasan (Salesforce)** 00:43 Hey, Victor.
**Victor Lu** 00:45 My first time in this meeting. Is this, there is another meeting at 12, which is… I mean, it looks like the same thing?
**Nida Hasan (Salesforce)** 00:53 Yeah, they have slightly different agendas. The second meeting is a little bit more thorough. You know, we go over PRs and stuff.
**Victor Lu** 01:09 So…
**Nida Hasan (Salesforce)** 01:09 I'm not…
**Victor Lu** 01:10 Sure.
So, the reason here is, I'm a journalist, I'm involved in a community that's called COSI, proposing, AI, Agentic AI, telemetry, just a lot of details. Actually, Trask is here.
So he'll, he'll know.
**Nida Hasan (Salesforce)** 01:30 Yeah. Sorry, kind of new, too.
**Victor Lu** 01:33 Okay.
**Nida Hasan (Salesforce)** 01:34 It's my third one here.
**Victor Lu** 01:37 Yeah.
**Nida Hasan (Salesforce)** 01:37 You wish.
**Victor Lu** 01:38 Okay, yeah, I Trask, just following up on the, Okay, let's say more people are joining.
Last… actually, last week, the week before last, on the… I brought up the Gen… the co-size proposal to add, AI security matrix, and… and I was… I couldn't join this meeting, or the 12 o'clock meeting, but I was told that, there is a different proposal, and, need, to, I guess, discuss here. That's why I'm here.
**Liudmila Molkova** 02:18 Oh, hello.
**Trask Stalnaker (Microsoft Corporation)** 02:21 Hey, Liudmila.
**Liudmila Molkova** 02:24 I accidentally joined the old meeting.
And… the… the single bod still survived. It's still there.
**Trask Stalnaker (Microsoft Corporation)** 02:39 So, Victor, I'm not sure, not totally clear. What I remember from last week, Was it last week?
Yeah.
Was that, we… asked. We said that we really need, you and Arthur or somebody present who can, Talk about it.
**Victor Lu** 03:15 Yeah, so Arthur… I actually told Arthur about the 12 o'clock meeting, so maybe he will join that one. I just find this meeting, and so… That's how I joined. I share the link again, and yeah, definitely, if there's time, I definitely can talk about what it's about, and I just want to learn anything that's already been proposed here.
**Trask Stalnaker (Microsoft Corporation)** 03:37 Cool. I would suggest the, 12 o'clock Eastern Call, just because there's a lot more people on that, as far as getting a broader, audience of people who may be Thinking about that, but, definitely, if we've got time in this meeting, we can… Spent some time.
Let's see… Go ahead and… Add yourself… And… Yeah, so I guess, yeah, floor is open for topics for… This meeting.
I'm guessing, Ludmila, you add a… you pushed these down as a… to… Because you wanted to talk about them in the… 9 o'clock.
**Liudmila Molkova** 04:53 I want to talk about them at 9 o'clock, but if we don't have, other topics for this meeting, I would love to pre… Have a pre-chat with you about the stability.
**Trask Stalnaker (Microsoft Corporation)** 05:06 Cool.
**Victor Lu** 05:07 Actually, I just find I may not… at least myself may not be able to make it to the 12 o'clock meeting, so if I… Just briefly talk about it.
The cosi thing, that'll be good.
**Liudmila Molkova** 05:20 Yeah, sounds great.
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 05:23 Yes, I'm also interested in that.
**Trask Stalnaker (Microsoft Corporation)** 05:28 Cool. So why don't we start with that, Victor?
**Victor Lu** 05:32 Yeah, so, a long story, there's, proposal in the community called COSI, Coalition for Secure AI, to, add matrix. At first, the proposal is to add, OpenTelemetry matrix.
Then it was determined that, OCSF has the, at least, current solution already in place for security.
Comprehensive security solution.
So, there's a proposal, if you see the link I have, added.
Which is a combination of both. The idea is to leverage what is being already in place for OCSF, and then see what is appropriate to be added to, to OpenTelemetry.
So it is a very comprehensive framework, I would say, already in place. And for OCSF, there's already collaboration between OCSF and COSI in implementing what is being described in that document.
So, so this is actually a draft. You can see it's draft 0.3, it's not formal, final, draft. The idea… to propose here is make, hotel community to be aware of this, and see whether, yeah, how to add the appropriate, metrics to OTEL as well, and what makes sense for hotel, what makes sense for OCSF. It is, when it comes to, also, how to say, the COSI community, in a way, actually, it just… people just want a solution, right? So whether it's OTEL, OCSF, that's secondary. Yeah, the main thing is definitely a security matrix is needed. That's why that proposal has been created.
That's… so that's a…
**Liudmila Molkova** 07:25 shouldn't…
**Victor Lu** 07:27 Yeah, go ahead.
**Liudmila Molkova** 07:29 you mentioned security metrics, I'm curious about this, but can… can you guide me, sir? I… I think I… I… I'm not sure what this… the… user experience. So, like, can you… Draw a broad picture of, like, how what would users do, what they would get, what is the OCSF vision on this, and Quasai?
**Victor Lu** 07:56 Yeah, so… so, just to give you an example, I find this article, this is actually totally unrelated, so don't use it to be… it's not related to OCSF at all, but this is one example of, the article's name is called Semantic Aware RSIN for Security Logs.
And this is something OCSF community is already doing, based on the current OCSF data.
And so, for example, one of the companies is generating… like, they're a big company, so they're doing a lot of hosting, so they are processing 1 petabyte a day of data, so it's impossible for a human or any regular program to parse it and identify information.
So in order to do that, definitely they're using AI. And then… but how to use AI? So you need an opera ontology. So that's, at this point, OCSF is using, MITRE Defense as an opera ontology, which in turn used the top level ontology called basic formal ontology.
So all this make it possible for, different… so once it's become a, universally, got adopted, I guess, in the OCS community, then it's possible for different sources to basically talk about the same symptom and problem in the same way, and that's why it's important to have a standard. So did that answer the question?
**Liudmila Molkova** 09:17 So, like, application or some system emits whatever arbitrary logs?
And the idea is to parse these logs and produce structured semantical signals that are useful for security.
It's just…
**Victor Lu** 09:32 Yeah, this is actually good for everything, but in this case, particularly cases about security. It's, for example, you see a pattern in the, like, a Cisco router.
you see a pattern from a web, and then… but how do you correlate them, right? So, the… for humans to process… even just hard-coding the logic is impossible.
So you have to, like, understand what is… what you're trying to look for, and then AI will automatically process a petabyte of data per day to identify any problems.
**Liudmila Molkova** 10:08 Sure.
**Trask Stalnaker (Microsoft Corporation)** 10:08 What's the connection to, Gen… Generative AI semantic conventions.
**Victor Lu** 10:19 This is… actually, that's a good question. The… the proposal is to add AI security matrix, so it doesn't have to be… actually, the original…
**Trask Stalnaker (Microsoft Corporation)** 10:31 Is it AI, like, security… is it security of AI systems, or using AI to parse security logs for general systems?
**Victor Lu** 10:42 It's actually both.
When it comes to which group, OpenTelemetry group, is appropriate for this, I would think it actually should be a security group, specifically.
Because OCSF already have established huge, framework for security. The AI security stuff, especially Agent AI security stuff that COSI proposed is just an addition to the existing OCSF framework.
Whereas in OTEL, I don't believe there's any framework at all at this point.
So it'll be from scratch.
So, yeah, so the question about whether this is the right meeting, I mean, the co-size one is an addition, specifically for Agentic AI, so it definitely is, relevant to this working group, but this goes beyond just Agent Kai, it's a security overall.
**Trask Stalnaker (Microsoft Corporation)** 11:34 So there's defi- I mean, the… This group could be the right group, I mean, because there is certainly renewed interest in security for, AI systems.
What I don't… knows whether, you know, if it's layered on, like… I think some of the proposals in this group have been more specific to security of AI systems and things that you would want to track out of that. Not… not necessarily tackling… The general security domain?
Which is where, I mean, I actually love that… We're working with the OCSF, and I would love to see, like, this triangle, kind of.
**Victor Lu** 12:28 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 12:29 Somehow.
**Victor Lu** 12:30 As a matter of fact, those two cannot be separated.
I'll give you an example. Generous… so, so let's say you have a, software, a PyTorch, compiled program, got jailbreaked, and… I don't… not jailbreaked in PyTorch, but, like, the model got jailbreaked, and… started to behave strangely, and you identify, okay, there's some problem with the actual PyTorch, the Python program that was generated, there's some data problem generated.
So, the… the actual… the PyTorch stuff, which is software, is actually a software-level, security issue.
And then the way the attacker actually got into that ecosystem is totally irrelevant to AI at all. So… just talking about security, AI security alone is, it's impossible. If you look at the MITRE defense, framework, the ontology, let me get that. So, so, the foundation, is, is, let me find that. So, the, yeah, so, so, so, in other words, if you just talk about AI security alone.
You will not be able to secure anything.
**Trask Stalnaker (Microsoft Corporation)** 13:57 So, I mean, it sounds like there's… Collaboration already happening… between OCSF and COSI, I mean, are… are you all able to put together some kind of proposal? Something… some kind of proposal for how… the… how this can… how open telemetry… Community can work.
together, like, how we can integrate that into OpenTelemetry more?
**Victor Lu** 14:31 The… the… the draft is… is the proposal.
**Trask Stalnaker (Microsoft Corporation)** 14:35 Oh, okay.
Thank you.
**Liudmila Molkova** 14:39 Yeah, it took me a bit to find it.
So, there were some attempts to introduce this… some similar attributes.
And I might have blocked because it was… so terribly, I generated, and not clear.
but it… it's a good context.
No.
**Victor Lu** 15:05 draft, so definitely I just needed to speed up, for sure.
**Trask Stalnaker (Microsoft Corporation)** 15:26 Cool, is there… I mean, so this is huge.
Is there a way that, you could… presented to the OpenTelemetry community in more bite-sized chunks that, like.
overview… I don't know, some way to construct it in a way that we can engage the community, because I worry if we just point the community at this document.
People are, you know, not.
**Victor Lu** 16:02 Yeah.
Yeah, so what to do with?
**Trask Stalnaker (Microsoft Corporation)** 16:05 I bet.
**Victor Lu** 16:06 the author, who works for Meta, he is interested, he will most likely be the presenter.
I'm not sure he's gonna join today or not.
Yeah, so, regardless, I'm gonna communicate with him so he can, do what you're asking for about this. In the meantime, definitely, you know, anyone interested in, you know, detailed work, collaboration between COSI and, and OCSF, even OCSF, welcome to join those meetings, as well to, discuss over there.
**Trask Stalnaker (Microsoft Corporation)** 16:36 Which OCSF meetings are these taking place in?
**Victor Lu** 16:42 Right now, it is the… the AI one, which is the most active one, is the… together with the networking meeting. I tried to sell you there, Trask, I think, I believe. The networking meeting is where the… this collaboration happens most at this point. Other than that, COSI's own meeting, for, So that's OCSF meeting, OCSF network meeting. Then for… from COSI side, there are multiple meetings, related to this, especially the… there's a Thursday, telemetry meeting that focused on this.
**Trask Stalnaker (Microsoft Corporation)** 17:27 Cool! Yeah, that'll be great to, see Arthur and kind of see how it presented.
to the community.
Yeah, I'm glad that, that's great that you all are working with the OCSF And COSI folks.
**Victor Lu** 17:48 Yeah, thank you. Yeah, that is all from me. Any questions?
Comments.
**Liudmila Molkova** 17:59 Thank you.
**Victor Lu** 18:01 Yeah, I'm on CNCF Slack, so ping me if you, want to follow up, anyone.
**Trask Stalnaker (Microsoft Corporation)** 18:09 Thanks.
Alright, Ludmila.
What would you like to chat about?
**Liudmila Molkova** 18:19 Yeah, I… let's first fill in the cloud stuff to the later call, because it's… just announcement. I found out that, there are… bunch of open telemetry semantic conventions there. Well, somebody pointed me out to this.
**Trask Stalnaker (Microsoft Corporation)** 18:40 Nice.
**Liudmila Molkova** 18:43 Maybe we can, be in Trask… we had a chat about stability and related, but, we thought that… well, it's applicable to GenAI, and it's been a long desire to stabilize some parts of it, at least.
And I think, what I see, it hurts a lot, because we don't have stability.
And I'm thinking about the scope first.
Like, I feel very confident in the inference that we can stabilize it with some refactoring.
Especially assuming that we can have V2 at some point, like, in, in… Months, or a year, or something like this.
I'm… Subjectively, like, 80% confident that we can stabilize Agentic frameworks, at least some Big parts of them.
And I think I wouldn't go any further. I am not ready to think about harnesses, life, like, I don't know about guardrails, maybe security folks, would really want to push for them, and it's important.
But it's also additive, so, like, we can probably remove them.
And I've prepared the… well, yeah, I prepared the project board. I was… and categorized what we have.
It's a little bit, overwhelming, because there is still quite a lot of to-dos, like 31, and I'm pretty sure there… there is… more that AIM used.
I… like, there are 79 things in possibility, this is crazy, and I'm pretty sure there is something there that would make it into a to-do.
But I kind of want to get a sense of how do we approach it?
And we started talking that this… These meetings were mostly focused on features, and, like, new things, the discussions for the tourney topics, or calls for reviews.
Would we be able to find time in this meeting to drive stabilization, or how would we prioritize That asks, like, the refactoring and cleanup needed for stabilization versus the post-stability topics.
Wanted to get… people's thoughts.
**Trask Stalnaker (Microsoft Corporation)** 21:33 I… I love it, I think we should do it. I think what, I feel like work.
I would… maybe propose… separate, Meetings… half-hour meetings, a couple times a week.
to drive, the stability topics specifically.
Kind of thinking what worked.
Well, I felt like for some of the… At least the early phases of the HTTP and database stability.
Where, you know, there's just kind of a lot to chat about, and it helps to have those discussions in real time, and then throw the PRs together.
I would definitely… Yeah, I would definitely make… Time.
**Liudmila Molkova** 22:43 Yeah, I would also make time for it. I think that the question, who else would make time for it, and then we can think about the time.
Because if it's just the US people, it's kind of unfortunate, but then it's easy. If it's Europe or Asia people, then it's hard.
It's better.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 23:06 Yeah, yeah, Ludmila, yeah, yeah, I have a question. Yeah, when we, migrate from a semantic convention to, current, repository.
GenAI cement convention. We don't release animation. Yeah, this is, related to the release.
Do we want to, stabilize something, and then we release, our GenAI version?
This is related or not.
**Liudmila Molkova** 23:41 I think it is related.
I would love to release before, but I think we still have a lot of refactorings going on.
And if we release, we will need to do backward compatibility with them.
And we can… if we finish refactoring some of the major ones.
I would love to, I don't know, release a development version, the first one.
And then at the rate was, like, minor details. So, like, we go the… the… progression to RC with a few releases, at least.
Well, with at least two releases.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 24:23 Okay.
**Liudmila Molkova** 24:25 You, like, Steve, I'm curious, would you… What is the reason behind your question? Do… do you miss the release?
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 24:35 Yeah, because, in semantic convention repository, there is a cadence.
Of, release, new version.
And, bata, for example, we will, support some, GenAI instrumentation in our, Commercial ver- commercial, instrumentation.
So, It's a long time, I don't see the release version, so, yeah, I'm curious about this point.
**Liudmila Molkova** 25:26 I feel like us not releasing is an answer to people… Treat released version as stable regardless.
**Trask Stalnaker (Microsoft Corporation)** 25:39 Yeah.
**Liudmila Molkova** 25:40 You're losing dozens.
**Trask Stalnaker (Microsoft Corporation)** 25:42 My worry is churn at this point. So many people… We have a surprising number of external people adopting GenAI semantic conventions, which is amazing.
But we also… we have this conformance goal, and almost, like… I worry about the conformance testing, like, showing, like.
what are people… what are people targeting over there? Like, is this this constant churn that's gonna, like, turn people off?
So… I almost prefer not to, like, to leave people stuck on the… the last version that was released out of the old repo, until we're ready to, you know, put out, like, an RC or something more… That we're recommending people to bump to.
**Liudmila Molkova** 26:43 So RC is the first released version from this repo.
Good motivation to actually do this.
**Trask Stalnaker (Microsoft Corporation)** 26:53 Yeah, we also have KubeCon, we also have KubeCon coming.
So…
**Liudmila Molkova** 26:59 Okay, well… I mean, can we pull it off by KubeCon?
Well, if we finish the major refactorings, I feel like we could if we deliberately spent time on them.
And… for the instrumentations, we would pick a few. Like, if we limit to inference, then it's trivial, right? There are a few.
If we limit to inference and agents, we will need to pick a few frameworks, and then… Also, I would love to be able to release RC for instrumentations as well, if it's a, like.
A reasonable set.
**Trask Stalnaker (Microsoft Corporation)** 27:45 I mean, what do you think of if we… How much do we narrow our scope by just doing inference, or… a wave… for Phase 1.
**Liudmila Molkova** 28:02 let's say we release inference. I think we can… we can pull it off relatively easy. Well, I might be totally wrong, but let's see if we've done it. And then… the Agentic stuff will come out in the same RC inference version at development.
it might be okay, we can do the trick of the, like, the two schemas, right? I don't think it will help much.
How much?
**Trask Stalnaker (Microsoft Corporation)** 28:32 External, like, with the cloud, like, the Cloud stuff that you saw… other things that you've seen. Do you have a sense of how much of that is… just pure inference SEMCON versus… Do… are the… is there much that's… Implementing the agent stuff at this point.
**Liudmila Molkova** 28:57 Quite a lot. I think Agentic stuff is… there are a lot of native instrumentations and conformance repo that are for Agentic stuff.
**Trask Stalnaker (Microsoft Corporation)** 29:05 Okay. Okay, then yeah, we should… I would say let's do them both.
**Liudmila Molkova** 29:13 Cool. But then, if we are very strict on scope.
we can try to pull something off by KubeCon, but I'm… I'm a little bit pessimistic. It's… Very short timeline.
**Trask Stalnaker (Microsoft Corporation)** 29:26 Yeah, yeah, yeah.
As far as scheduling, Yeah, let's see in the, The general meeting, but we basically… we need… we need at least one more person, because we need two approvals.
on stuff, hopefully, maybe at least Aaron and then we can… Put together some meeting times.
**Liudmila Molkova** 29:53 Awesome, cool, yeah, thanks a lot. Let's continue on the next call, and thank you everybody for joining.
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 30:03 Bye-bye.
