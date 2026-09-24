SIG: OpenTelemetry .Net Auto Instrumentation SIG
Date: 2026-09-23
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Piotr Kiełkowicz (Splunk Inc.)** 04:51 Hi, guys.
**eftiquar** 04:54 Hello.
**Piotr Kiełkowicz (Splunk Inc.)** 04:58 Can you guys, drive meeting today?
**Zachary Montoya** 05:03 Yeah, let me… Let me get that set up. I can drive.
**Piotr Kiełkowicz (Splunk Inc.)** 05:08 Thank you.
**Zachary Montoya** 05:09 Let's see… Alright, so you should be seeing my screen.
Did, did I miss anything from last week? I was, busy and couldn't make it.
**Piotr Kiełkowicz (Splunk Inc.)** 05:50 Not from last week, but on Monday we have released… or Tuesday?
Tuesday, probably. I freeze the auto Instrumentation.
Mainly to handle, Security issue in hosts.
research detector and the Nuggets case scenario.
**Zachary Montoya** 06:10 Gotcha.
**Piotr Kiełkowicz (Splunk Inc.)** 06:11 Starts, starts failing.
But also, there were also a lot of other improvements, yeah. SDK country pants on our side, so… Finally, end users can use it.
**Zachary Montoya** 06:24 Great.
Alright, let's go through the PRs. Okay, so we have a bunch of renovate PRs we need to go through.
It looks like the most recent one… Was the runtime async?
I still plan to review this.
But, are there any blockers on this one at the moment?
**Piotr Kiełkowicz (Splunk Inc.)** 06:47 For runtime, I think the native sync would be better to merge first, because the… Files overlaps, and it is… it is… to be honest, it is easier to adjust this one instead of the… the runtime sync.
**Zachary Montoya** 07:05 I'm sorry, I'm not sure I understand.
**Piotr Kiełkowicz (Splunk Inc.)** 07:07 So, I would like to merge first the native code PR updates from the Datadoc, the.
**Zachary Montoya** 07:14 This one.
**Piotr Kiełkowicz (Splunk Inc.)** 07:15 Excellent.
**Zachary Montoya** 07:16 Okay.
**Piotr Kiełkowicz (Splunk Inc.)** 07:17 And it is purely on you, to be honest.
**Zachary Montoya** 07:19 Yep.
Yeah, I can, I can look into this, this week.
**Piotr Kiełkowicz (Splunk Inc.)** 07:26 And when this is done, we can merge this one, and also the one related to the OpP.
Scenario for the disabling and… enabling and disabling, profiling dynamically.
**Zachary Montoya** 07:44 Gotcha, is that one… what's that one called?
Oh, here we go, make native contest profile.
**Piotr Kiełkowicz (Splunk Inc.)** 07:53 Yes.
**Zachary Montoya** 07:54 Okay. Okay, yeah, I will make sure to get to this. I should have time today to start reviewing this.
Okay, cool. And then, you know, these two… This one already has reviews.
Okay, so cool. Besides those three, it looks like we have one Kafka tracing one.
I think this one should be reviewable at this point, because I believe the… Hispanic conventions about data, right?
**Piotr Kiełkowicz (Splunk Inc.)** 08:27 Yes, but we have agreed that we do not want to switch it.
Purely to 144, but we need this environmental variable to utilize old versus new.
Our semantic conventions recommend?
So, Daniel's stuff should be enabled when this is set to messaging or messaging duplication.
**Zachary Montoya** 08:53 Gotcha, okay.
So then that means that this PR would also need support to parse… This environment variable and this particular values.
**Piotr Kiełkowicz (Splunk Inc.)** 09:06 Yes, exactly.
**Zachary Montoya** 09:07 Okay.
Sounds good.
Yeah, it makes sense to me.
**Piotr Kiełkowicz (Splunk Inc.)** 09:13 In country repository, there is kind of similar… Infrastructure stuff, so it can be easily copied.
**Zachary Montoya** 09:20 Oh, okay.
Okay, great.
Okay, so besides the PRs we just mentioned… Yeah, upstream.
RabbitMQ… Okay… IBM, okay.
Is there anything that you guys wanted to discuss in particular? Any other PRs?
**Piotr Kiełkowicz (Splunk Inc.)** 09:49 Alexey, are you ready with this?
on… Strange… new way to…
**Alexey Pukhov** 09:57 Legit-level reflections.
**Piotr Kiełkowicz (Splunk Inc.)** 09:59 Yeah.
**Alexey Pukhov** 10:00 Well, I did address the comments, raised by Igor and eftikar, so just waiting for the second review.
The tests are passing.
**Piotr Kiełkowicz (Splunk Inc.)** 10:12 Right.
**Alexey Pukhov** 10:12 Well, I mean, the change is definitely working, just need to make sure it's a good one.
**Zachary Montoya** 10:21 Which, I'm sorry, which PR is this?
**Alexey Pukhov** 10:23 I think it's in the draft, and it should be called… Hmm… How do they call it?
It's something related to unsafe, access, or…
**Piotr Kiełkowicz (Splunk Inc.)** 10:37 Heard from the bottom.
**Alexey Pukhov** 10:38 type native redirection. Yeah, it…
**Zachary Montoya** 10:40 Pardon?
**Alexey Pukhov** 10:41 It's 493… 4931. Oh, fantastic. It's third from the bottom, yeah.
**Zachary Montoya** 10:46 Oh, I see.
Okay.
**Piotr Kiełkowicz (Splunk Inc.)** 10:52 And I think we need to merge it before .NET 11 also.
**Alexey Pukhov** 11:00 Yes. Yep.
**Zachary Montoya** 11:04 Okay. When does Starlight 11 go out? Is that… mid-November? Should be November.
Alright, that's good to know.
Should we give it a milestone in that case? Did we just release 1.17?
**Piotr Kiełkowicz (Splunk Inc.)** 11:22 Yes, I'll… I'll recluse it. One, the… yeah, we have the milestone.NET 11 release tracking.
**Zachary Montoya** 11:29 Oh, perfect, okay.
Yeah, it's at that.
Okay.
And then let's also add the runtime async. We could put that same milestone as well.
Okay.
Alright,
**Alexey Pukhov** 11:48 also from my side, I'll be wor- I'll soon start working on the second… part related to .NET 11, which is bringing back additional dependencies for startup hook-only solution.
We will also have to do this before .NET 11. I mean, actually… I mean, we can? I mean, it would be nice to have it before .NET 11. Let me frame it this way.
**Zachary Montoya** 12:17 Okay. Yeah, I mean, that makes sense, and we can track it for .NET 11, And then, you know… If it's still just a nice-to-have, then… You know, it doesn't… it's okay if we miss the mark, but we can certainly track it to include in our .NET 11 release.
**Alexey Pukhov** 12:33 Sure.
**Zachary Montoya** 12:36 I suppose this would also go… I imagine, Piotr, that this would be something that we just merge… At the time of .NET 11 release.
**Piotr Kiełkowicz (Splunk Inc.)** 12:48 Yes, it is kind of… I'm trying to revise it monthly, when the new pre-release or RC occurs, last time everything was working fine.
on RC1.
**Zachary Montoya** 13:03 Okay.
Got it. So this is, mostly, builds, changes?
**Piotr Kiełkowicz (Splunk Inc.)** 13:14 To be honest, it's everything. Wheels changes, output changes.
kind of small adjustments to do not load CR profile error.net 8, and… 8 and 9… Yeah, a lot of stuff.
**Zachary Montoya** 13:35 Gotcha. Okay.
Alright, well, we have.
**Piotr Kiełkowicz (Splunk Inc.)** 13:38 Comments from the… comments from the beginning are kind of pretty well named, but… Later, it's kind of a mess, and I decided to try to clean it up.
**Zachary Montoya** 13:50 Yeah, I apologize.
**Piotr Kiełkowicz (Splunk Inc.)** 13:51 Closer to .NET 11.
**Zachary Montoya** 13:53 Yeah, I have plenty of PRs like that. They start off with the best organization, and then become more messy.
**Piotr Kiełkowicz (Splunk Inc.)** 13:59 Yeah, to be honest, issue-based, kind of, it's this next layer of mess, so…
**Zachary Montoya** 14:05 Yeah.
Okay.
Alright, so now we have a couple of PRs with the milestone, so that'll be helpful.
Anything else you guys wanted to discuss in terms of open PRs or drafts?
Alright,
**Piotr Kiełkowicz (Splunk Inc.)** 14:24 IBM is still waiting for some review, I'm not sure if it is on you or someone else, I do not remember the PRS.
**Zachary Montoya** 14:36 Okay, yeah, Okay, so this is the messaging API?
I could… I don't… probably don't have time this week to look at this, but I could see, I think we have some sort of IBM stuff in the Datadog one, so maybe I can review this next week.
**Piotr Kiełkowicz (Splunk Inc.)** 15:04 For sure, it is fully AI-generated, and I'm not sure if the… Contributor, and has a big knowledge about the code he created.
**eftiquar** 15:14 So, Piotr, I'll also take a look at this one. I think it may skip my attention.
I'll take a look.
**Piotr Kiełkowicz (Splunk Inc.)** 15:20 Right.
Great.
**Zachary Montoya** 15:28 Alright.
Alright, if there's nothing else on the PRs, we can move on to the issues.
This one… So, adding in some opt-in… semantic conventions…
**Piotr Kiełkowicz (Splunk Inc.)** 15:45 I think in the PR, we have… I've commented, based on the last SIG decision, that we will not accept this until semantic conventions accept This kind of, attributes.
**Zachary Montoya** 16:03 Perfect, okay. Yeah, makes sense.
Is there, like, a better holding pattern we should do for this, so we don't… Oh, so is it this only when the semantic conventions are added?
**Piotr Kiełkowicz (Splunk Inc.)** 16:19 I think we can close this PR fully, but… Or wait one more week, and if there will be no response from the contributor, then close it.
**Zachary Montoya** 16:40 Okay.
Alright, so that was the RabbitMQ spanning Conventions, runtime async, yep.
And then this, SIG fall looks like.
**Alexey Pukhov** 17:01 Yeah, that I haven't yet looked at, that's on me.
**Zachary Montoya** 17:07 Is there already a… Okay, there… it looks like there could be a reproduce… okay, cool.
So the provider reproduction, it seems. Okay.
So she'll be able to review that.
Okay, let us know if you find anything, or if, Or, if next week, someone else should take a look.
**Alexey Pukhov** 17:30 Sure, yeah, I'll try to see if I'll get some time this week to look at this.
**Zachary Montoya** 17:39 Alright, I think that's it for the… the issues.
No discussions… oh, this one was the one… I think we need to update this milestone here.
Alright, let's go just update that.
Oh.
Sorry about that, folks.
Okay… I'll do a fun rename of this again. Okay, all good.
So we got .NET 11 support in progress, a couple different PRs, the Kafka span attributes, This one… Sorry, I thought we… What's the status on some?
Sorry, just wondering if this is something we're still in progress.
So this Kafka one… So is this still waiting on a stable release?
**Piotr Kiełkowicz (Splunk Inc.)** 19:24 I think this one is blocked by the… Kafka semantic conventions update.
**Zachary Montoya** 19:35 Okay.
Sorry, I'm just, confused about the order of the… or the pronunciation chain of this one.
So we have Caucus Vanity Conventions on 4-4.
**Piotr Kiełkowicz (Splunk Inc.)** 19:49 So, we… this new Kafka tag is available in the latest Kafka semantic conventions.
So we cannot add to the east… add to the… all semantic conventions.
But… if he would like to implement this, he needs to finish this PR first, and then add the new… attribute on top of the semantic conventions arrive only when the environmental variable switches away.
**Zachary Montoya** 20:24 Okay, so if I go back, so this one is 1.5… or 4… And this one adds, in particular, messaging Kafka Cluster ID.
**Piotr Kiełkowicz (Splunk Inc.)** 20:38 And it is not part of this, because first he needs to update semantic conventions, and then he can add the new attributes.
Technically, it can be merged into one PR, but… This one is big enough to review it.
**Zachary Montoya** 20:52 Okay. So is it safe to say that… We should… this should be done first, and then the previous one should be done second.
**Piotr Kiełkowicz (Splunk Inc.)** 21:03 Exactly.
**Zachary Montoya** 21:03 Okay.
Alright.
Let's it, let's… Cool. Sorry, I just thought of the… Yeah. A lot of semantic conventions going on. Okay, and then IBM MQ is in progress.
Okay.
Committed, we have some… thing about the ASP.NET Core hosting startup assemblies… I don't really remember much about that one.
And then I'll just.
**Piotr Kiełkowicz (Splunk Inc.)** 22:09 I do not think it is high priority right now.
Igor?
**Igor Kiselev** 22:19 Yeah, it's still nice to take a look, it's ready, but no priority for it. It can be done in years from now, also, without any problems.
**Zachary Montoya** 22:32 Okay. I'll leave it there for now.
Anything else? I just moved the .NET 11 runtime async method support into in progress.
I guess this is technically the same thing.
Invalid IL.
Is this a startup isolation hook? Is this… Similar to the… NET 11 stuff that, Alexey, you're working on, or is this a different thing?
**Alexey Pukhov** 23:08 This is a, this is a different issue, so… I think this… Well, I mean, it's kind of related to assembly resolution conflict, assembly conflict resolution. It's just the customer reported some issue, with their application that looks like our assembly conflict resolution on the startup hook is breaking their Application in a very specific way.
so, the additional dependencies fixed, thing that I'm bringing back will help, will definitely help them.
So I'm actually planning to reply to this ticket at some point, saying that, okay, we are working on a… on bringing back additional dependencies that should fix your problems, but probably for that particular customer, I can also suggest just to not do the assembly redirection and just fix them. Use any workaround to align your Assemblies with whatever we need.
that could be also a fix for them. But maybe for them, they don't even need any assembly redirection, because it looks like they just Don't really need any assembly.
Conflicts to be resolved.
But I still have to look at the ticket to reproduce it, probably, and just… Give them a better reply.
**Zachary Montoya** 24:36 Okay.
So yeah, I mean, we have a… we have a couple items over here. I'll just leave them as… as backlog. We'll focus on… these .NET 11 ones and these couple of instrumentations.
**Igor Kiselev** 24:50 Are we… are we moving to committed everything that .NET 11, related, or not? Because if they are moving everything that .NET11 related to committed already, is that issue? And, unsafe accessor type, bypass native, and next one should, be moved to committed?
Because it's all… it… all three of them will be… we need to resolve before we claim .NET 11 support, so… And he's already… and then he already started working on them.
**Zachary Montoya** 25:25 Yeah, that makes sense.
Alright, so that'll live here for now, and then we can see if we need to split this up.
I spelled out the work.
Alright… I think that's good updates on the project board.
Not sure if there's anything else, you guys wanted to go over.
Let's close that down… Okay.
So that's our regular agenda. Any other topics, questions, concerns?
Alrighty, cool. Well, thanks everyone for your time.
See you next week.
**Piotr Kiełkowicz (Splunk Inc.)** 26:38 Thank you.
