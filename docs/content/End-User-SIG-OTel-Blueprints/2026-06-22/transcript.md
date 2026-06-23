SIG: End-User SIG: OTel Blueprints
Date: 2026-06-22
Duration: 59 minutes
============================================================

## Zoom Recording Transcript

**Dan Gomez Blanco** 01:03 Hello, hello.
**Alexandre Ferreira** 01:05 Hello there, Don. How's it going, man?
Can you hear me good?
**Dan Gomez Blanco** 01:09 Yep, can we hear you fine?
**Alexandre Ferreira** 01:11 Alright.
**Dan Gomez Blanco** 01:12 You feeling okay?
**Alexandre Ferreira** 01:14 Much better. I got influenza.
And, developed a pneumonia as well, so… I was feeling wracked.
I went to the hospital thinking that they were going to give me some drugs or something, and they said, we're going to have to admit you into ICU. I said, what the fuck?
So I stayed in the hospital for, like, 5 days.
And I came back yesterday. But for protocol, I'm still using the face mask because I have a baby.
So, even though, like, the exam returned negative yesterday, I still have to use this.
But yeah, things are much better now.
before that, I was, like, traveling for my company and all that, so I do apologize the late response for reviewing the PR.
But since I was in the hospital, I took the time to, like, review everything and change some stuff.
**lciukaj@splunk.com** 02:17 Perfect.
**Dan Gomez Blanco** 02:18 I don't tell. I think so.
**lciukaj@splunk.com** 02:19 Thanks. Thanks for your update, and no worries about the delay.
We don't have any deadlines here, so we just want to have everything under control and move forward step by step. So thanks for providing that update and new PR, new commit, I will review it. I'm in the… actually doing it right now, so please expect some update by the end of business day.
**Alexandre Ferreira** 02:42 Alright.
**Dan Gomez Blanco** 02:44 Good stuff.
**Alexandre Ferreira** 02:45 Hence.
**Dan Gomez Blanco** 02:46 Okay, let me just create the… Oh yeah, it's already there.
Thank you for the attendees.
**lciukaj@splunk.com** 02:58 Yeah, I updated our notes and added one topic that I would like to discuss today, about the triage process.
Hi, Alolita.
**Alolita Sharma** 03:12 Hey, Lucas, how are you? Good morning.
**Dan Gomez Blanco** 03:14 Whoa.
**Alolita Sharma** 03:15 Hi, Dan.
**Dan Gomez Blanco** 03:21 Let's just wait, well, just one minute, I just wanted to put something in the agenda to discuss.
**lciukaj@splunk.com** 03:29 Sure.
Where are you guys based in? So, Dan, you are in Scotland or Ireland?
**Dan Gomez Blanco** 03:41 Scotland.
**lciukaj@splunk.com** 03:41 Okay. New analyolica?
**Alolita Sharma** 03:43 I'm in California.
**lciukaj@splunk.com** 03:46 And Alexandra, how about you?
**Alexandre Ferreira** 03:48 Man, Brazil. So, actually, Brazil's going to play against Kotlin on Wednesday, I think, right? So…
**Dan Gomez Blanco** 03:53 Yeah, right, that is right.
**Alolita Sharma** 03:55 Yes.
**Dan Gomez Blanco** 03:57 Everyone here is, like, we might need to stay up late, you know.
**Alolita Sharma** 04:01 Yes, exactly.
**Dan Gomez Blanco** 04:03 Not… I mean, not that we have, like, a lot of hope of Scotland playing against Brazil.
**Alexandre Ferreira** 04:10 But I don't have much hopes for Brazil soon as well, like, we are… Like… It's not a good team, but… alright, I guess that's what we have now.
**Alolita Sharma** 04:22 Yeah, it goes through phases, right? So…
**lciukaj@splunk.com** 04:26 I'm a big soccer fan, or European football fan. I'm originally from Poland, so I'm happy that, you know, the World Cup is now in North America, so, you know.
**Alolita Sharma** 04:36 Yes, yes, totally.
**lciukaj@splunk.com** 04:37 It's very convenient for me to watch the games, you know, when I talk to my parents, my dad, my brother-in-law, they are, like, complaining, oh, it's the middle of the night, I don't know the game, so I'm in a good position this time.
**Alolita Sharma** 04:50 So, totally worth it. And also, I mean, you know, as Lucas, you have seen, there are a lot of people who play soccer here, so it's not…
**lciukaj@splunk.com** 04:59 Yes.
**Alolita Sharma** 05:00 Exactly.
Soccer is a great game.
**lciukaj@splunk.com** 05:05 I've heard from folks come forward that after the World Cup, most likely there will be this, you know, big wave of interest and, you know, even more, like, activities and events and everything around.
**Alolita Sharma** 05:15 Oh, yeah, yeah, absolutely. It's… it's quite popular.
**lciukaj@splunk.com** 05:20 Thank you.
**Dan Gomez Blanco** 05:22 Yeah.
**Alolita Sharma** 05:23 All the kids play it, so… Therefore.
**Dan Gomez Blanco** 05:30 Should we, should we start discussing those things?
**lciukaj@splunk.com** 05:35 Yep, that's…
**Dan Gomez Blanco** 05:37 Let's go for it. Yeah, Lucas, if you wanna…
**lciukaj@splunk.com** 05:43 Yeah, I can kick off with the… with the triage process, so let me open the… comment that I… or the issue that I opened, in, I believe that was the community, or end user, I don't know.
**Dan Gomez Blanco** 05:57 I just… I put it in the notes, I was just…
**lciukaj@splunk.com** 06:00 You put it in an awesome.
Yeah, there is something that I would like to discuss, because I think we don't have a good trash process yet. Of course, we are still in the early stages of the Blueprint Initiative, I would say, but we have more and more proposals, more and more interest, so I think we should start discussing the That the proper triage process for, for blueprints?
I have some idea, how it could look.
But I would like to get some feedback from the team. What do you think about this? Okay, let me share my screen very quickly, because I don't remember it from the top of my head. It was, like, 2 weeks ago.
And… Oh my gosh, I won't be able to share, I need to leave, because I have an update of my system, but…
**Dan Gomez Blanco** 06:50 That's okay, I think we can… we can…
**lciukaj@splunk.com** 06:52 Can you share that, Dan, or I can read through it, if possible.
**Dan Gomez Blanco** 06:56 Yeah, I think we can all… I mean, this is in the notes, so we can.
**lciukaj@splunk.com** 06:59 Yeah, yeah, so everyone can look it. But my idea about it is that there's, like, 9 stages that I managed to identify. So, first one is about the blueprint proposal created, that someone is opening the GitHub issue. Then there is the Blueprint team.
That is reviewing it, and providing the initial feedback.
And then, also, we need to have outers identified, so quite often, the person that will be submitting the GitHub issue will be the outer, but it's not the case. Everyone can submit the GitHub issue, and maybe someone else can pick it up from there and be an outer. And also, we can… we may have 2 or 3 outers, right? A couple of outers for the blueprint. So then, there's the important stage. Okay, there is actually 10. I see that I made a mistake with the numbering. So there is the stage four, which is, like, approved for outoring, right? So where the blueprint team approves that we have outdoors, we have the… the proposal is okay, the topic is needed, we can continue working on that. So, only after this, the person or the team that will be working on the Blueprint can start actually putting the content together. I mean, everyone is… we are okay if someone can start earlier, but in order to move forward, they need to have this approval from the Blueprint team. So then the Blueprint team needs to obviously review a couple of things, like, as I said, like, whether the idea is good, whether we have outdoors identified, if there is a time commitment as well from outdoors, if they can, let's say, finish that by some, let's say, foreseeable future, not like having this open for two years, then the team or the person that will be the lead of that blueprint We'll submit the PR, so then we have the PR submitted, and then the Blueprint team is again reviewing that PR, and tagging relevant 6, right? This is important. So, so, so, so, so by tagging 6, we are asking other, 6 members to review it and get the approval for the next steps. So once we have the SEC approved from all of the groups that are tagged, and again, that is more like a blueprint team responsibility.
I mean, the outer can also suggest, okay, I believe this is, let's say, the platform, or this is a… Kubernetes, or this is a collector, so it would be good that collector Sikh can review it. So, suggestion from the outer is okay, but it's more about the Blueprint team that is reviewing it, and tagging the appropriate SICKs here for the content approval, right? And then, when we have all of the approvals from… from SIX, And we, the Blueprint team, provides the final approval.
And then there is a docs team involved to actually review it, make sure that the structure and the wording, the bullets and everything, and the format is okay, so then we are ready for publishing. So it's, like, at 10 stages. I'm not sure if that is correct. It's, like, my idea, maybe I'm overcomplicating that. What are your thoughts about this? Is it, like, too complicated for this?
Simple blueprints, or we are good.
**Dan Gomez Blanco** 10:18 I think it's good. I think what I would do is, a couple of questions that I've got, basically. One is, like… I think it would be good to separate what is the issued triaging process, or the initial… triaging from the, you know, after the blueprint is… let's say the drafting and the PR open into the website.
So on the triage side, it'd be good to identify, you know, what labels we want to use, because that's normally, like, gonna be on the… we're gonna have a blueprints approvers team that can apply these labels to…
**lciukaj@splunk.com** 10:54 the issue.
**Dan Gomez Blanco** 10:54 use on the second user repo.
And you know, basically we can sort of, like, map That, workflow to this.
And then, another thing, another comment I've got is that I think it would be better if… this… the Blueprint's approvers have an initial review, rather than… and directly to the SIG.
Because they're already, you know, segs are already stretched, in a way, so, like, the more that we can…
**Alolita Sharma** 11:23 Yeah, I agreed.
**Dan Gomez Blanco** 11:24 Make it easier.
**Alolita Sharma** 11:24 for them.
**Dan Gomez Blanco** 11:25 review.
**lciukaj@splunk.com** 11:26 Yep, yep, yep. I agree with you, like, we need to be aware as well, right, that the Blueprint team, if that makes sense or not, and maybe drive the conversation to provide more clarification, and then tag the Sikh only for the final review, like, not, like, asking them for basic stuff, right? Yeah, I agree with you. So that's important here.
**Alolita Sharma** 11:45 Yeah, I think, just to add to what Dan was saying, because I would… I would separate the triage process, because that's something that definitely is on us, right? Like, and, as folks are submitting proposals, again, reviewing and, you know, kind of accepting that the review That we are reviewing it, and then… you know, then assigning, asking questions, and assigning, getting one person assigned, as you said, like an author, or an owner, if you will, because there could be multiple authors, but there could be one owner in terms of taking the process forward, like a steward.
**lciukaj@splunk.com** 12:30 Receipt.
**Alolita Sharma** 12:31 Yeah, yeah, exactly, exactly. So, but I would separate out the triage process from the publishing process, because the review and publishing, as you guys, you know, rightly pointed out, is… is a lot more detailed than… and the review process and the publishing process could be, you know, that, hey, we do most of the legwork with the… as part of the SIG, with the, you know, proposal owners, and then… once it's ready for review for, you know, other SIGs, then we ask the other SIGs to get involved.
Because to Dan's point, again, most of the SIGs are quite maxed out, so the more we can do, you know, on our end, we already have a template, right? So… That could be, again, automatically used, you know, and people do use it, right, for submissions. But, the other question I have is exceptions, right? So, what happens if somebody, you know, made a proposal, and then… Started working on it, and then dropped out, right? Because that can happen, due to many reasons, you know, books, take off, and… So, then there is, say, no activity for a month, right? Or no activity or progress by the authors for a… for a month, or maybe more, what… what is the process then, right? Because, say it was in single owner.
and not multiple owners, then how do we get that over the… or is it something that's abandoned, right, for… For the SIG, because you can easily have that situation where people are, you know, people contribute, and then… Get busy with some things.
**Dan Gomez Blanco** 14:24 Yeah, I think that we should have something in place that says, well, you know, people should be able to, like, pick up where someone left, right?
**Alolita Sharma** 14:32 Yeah.
**Dan Gomez Blanco** 14:33 Have you shared any progress so far, for example, that would be…
**Alolita Sharma** 14:36 Yeah, and the other thing is that having clear, AI, guidelines… I know, Dan, we discussed this, which, where I really like the idea of having, the word limit of, you know, 2,000 words or 2,400 words, and kind of keeping it, focused in that way.
**Dan Gomez Blanco** 14:55 I would think that, yeah, it was… I think I didn't create the issue for this, but I wanted to create an issue for that, like.
**Alolita Sharma** 15:01 Yeah.
**Dan Gomez Blanco** 15:02 You know, as in… guidelines.
**Alolita Sharma** 15:05 Yes. Like… Yes.
**Dan Gomez Blanco** 15:06 Because we have the template, and the template does contain… some guidelines there, but, maybe some general, like, maybe some general guidelines. Well, actually, that's a question, like, do we want to have the guidelines in the template itself? Which, at the moment, they do… make… I mean, we do have some guidelines in the template as comments.
Or we want to have a separate document. It's just basically, like, more… Perhaps.
**Alolita Sharma** 15:31 I mean, maybe having more detail on a markdown page, and then just having the link in the template may be useful, but folks acknowledging that they've read, you know, the.
**Dan Gomez Blanco** 15:44 Yeah, so if you go… let me see if I can… I can link it, but.
**lciukaj@splunk.com** 15:48 That's a good point, Alolita. I would like it, like, with the opening the GitHub issue.
**Alolita Sharma** 15:52 Yeah.
**lciukaj@splunk.com** 15:52 Checkbox, okay, I read the guideline of blueprints, and I'm aware of everything.
**Alolita Sharma** 15:57 Yeah, because, I mean, if you look at some of the… folks, like, even contributing in different hotel things, especially the GenAI one, you will see there are a lot of AI responses coming in. Oh, yeah, I want to…
**Dan Gomez Blanco** 16:14 I wanted to talk about one of those things, but yeah, so I think… let's… let me share my screen, because I think if we… This is… this is actually a good point. If you open this, and you just read this, you will not see any of the guidance, because this is just an example, right?
**Alolita Sharma** 16:28 Right, right.
**Dan Gomez Blanco** 16:29 However, if you go to the actual quote, there's a bunch of stuff here in Commons that I added.
**lciukaj@splunk.com** 16:36 Which is…
**Dan Gomez Blanco** 16:36 I guess… you know, That is, like… some guidelines here. It should be structured in a way that conveys the journey, but it does talk about the guidelines, so I think they may be a bit hidden at the moment.
So, maybe it's better to, like, Take these comments somewhere else.
And put them in a more visible place.
**Alolita Sharma** 16:57 Yeah, and also force people to kind of sign off on it, that they've read it, because otherwise, you know, I mean, this will continue to happen, right? Everybody's using some tool or the other.
Yeah, exactly.
**Dan Gomez Blanco** 17:10 Exactly. Actually, my intention of these comments, and this is why I kept it here, was that… you could… give this to a, you know, give this to an agent, to an LLM, to… to actually… Use the comments to say, well, this is how you should write it, but maybe it's better to keep it in a separate document.
**Alexandre Ferreira** 17:31 So… I would add that this… the way that this is written on… with the comments.
Have helped the agent a lot to get to write, everything, like, within the framework of the guidelines. So, like, we have this template, but at some point, you mentioned that, hey, this template is actually based on a author that, like, mentioned… I forgot the name of the guy, but, the Good Strategy, Best Strategy thing, right? Yeah. So… Perhaps you could… Live… leave this as a success, but also, like, take… The rationale behind… Why the template has the format that it is, and mention it either somewhere else or, like, within the same heading of the page, right?
**Dan Gomez Blanco** 18:26 I mean, when we open an issue, this is an interesting one, so when we open an issue.
In the issue template.
It does mention the Blueprint template here, right?
However… Yeah, we don't really… I guess we don't really… I mean, when we create an issue, you haven't really started writing the template yet.
So, what was your opinion, that we should probably have something here saying, like, oh, I've read the template?
**Alolita Sharma** 19:09 Yeah.
**Dan Gomez Blanco** 19:10 Yeah.
Okay.
**Alolita Sharma** 19:14 Like, before, exactly, Dan, because if, somebody's bringing up the template, you know, they should definitely… Kind of click a checkbox somewhere.
**Dan Gomez Blanco** 19:27 Yeah, so maybe something like, I write the template, and… the comments or something like that, because I think… I do think the comments will make it easier to…
**Alolita Sharma** 19:34 Yeah, yeah.
**Dan Gomez Blanco** 19:36 It's just one document to pass to your…
**Alolita Sharma** 19:38 Yeah.
**Dan Gomez Blanco** 19:39 To your agent, if you want to start somewhere, right?
Okay, so I'll… I've taken action on that.
**lciukaj@splunk.com** 19:49 And something that I just realized is that we have actually two different repos, right? Because the proposals are being, I mean, GitHub issues are opened in end user.
**Dan Gomez Blanco** 19:58 Sick? Yeah.
**lciukaj@splunk.com** 19:59 But the PR is opened in Opentelemetry.io.
**Dan Gomez Blanco** 20:03 Yep.
**lciukaj@splunk.com** 20:03 So, we have two different repos, and already in OpenTelemetry.io, there are some labels. I can see that there are some labels for existing blueprints, like missing docs approval, missing SICK approval.
**Dan Gomez Blanco** 20:16 triage process of the docs website in general.
**lciukaj@splunk.com** 20:20 So the question is now, like, do we want to have a separate process for… on OpenTele for Docs on Blueprint, or…
**Alolita Sharma** 20:30 Actually, Dan, good question, Lucas, because, before a… is there such a thing as a proposal being accepted first?
In your thinking?
**Dan Gomez Blanco** 20:42 I think this is what I was saying, like, to separate both things, the triage process, from the PR submission, because in the… the docs write and already have a process, right?
**Alolita Sharma** 20:53 Yes, exactly.
**lciukaj@splunk.com** 20:54 And it's the same, right? Whether it's the blog post or blueprint, it's exactly the same process.
**Dan Gomez Blanco** 20:59 And if we have a team, basically, as co-owners of that… of the Blueprints section.
then we can integrate with that docs process, right? So, like… It will require the approval from… from… from us, basically. It would just basically… already, like, assigned the PR to…
**lciukaj@splunk.com** 21:19 I think we shouldn't, like, reinvent the wheel here, like, more focus on the first part of the process, like, review the proposal, make sure that the topic is good, we have outdoors, we have the time commitment, everything. We give them, or the outer, the green light to open the PR, and then we continue with the regular docs trash process.
**Alolita Sharma** 21:38 Yeah, yeah, maybe that's a good step, because, the question here is that, you know, do the docs… does the docs team expect us to kind of you know, work with the author through that process, or do they take over at some point? What, you know, how does that handoff occur? Because my concern here is that, you know, if we can kind of help the authors as much as possible to be, you know, say, ready for publication before they file the PR and the docs.
a repo, then it's much easier for the docs team to, you know, run through it, say, hey, you know, the end user seg has already approved it, and then, Then they can just do an edit review rather than accuracy of content review, right?
**Dan Gomez Blanco** 22:37 Yeah. So I think in the process, before the PR is open, after the PR is open, that's a different one, but before.
maybe, I think, you know, we had spoken about this as, like, starting the blueprint as a… and I think, you know, you did it, Lucas, and Alex as well, and myself, start the Blueprint as a Google Doc, right? Which is easier to, like.
Maybe iterating faster without… without opening the PR, and then… When that's gone through an initial review.
then you can open the PR to the website, and then get the… and get the other approvals from, like, the SIG, the, you know, the specific SIGs that we want to do, the docs for copyedit, and all that, but maybe you can keep the process a bit lighter when you start in a Google Doc, right? Maybe we could document that.
As part of the process.
**lciukaj@splunk.com** 23:29 I agree, yeah, I think that makes sense to not only, like, rely on the, let's say, a couple of sentences of what is the idea, but for us, for the Blueprint team, to actually look into some draft, right, of the Blueprint before opening PR.
So then, if we say… if we see it's okay, we give a green light for opening a PR in Doc's team, right?
**Dan Gomez Blanco** 23:52 And then we can document that with labels and the issue, right? As in, like, you know, the issue… as is the same way that's done with the spec, for example. Where, like, there are issues in the spec that have been in, for good reasons, community feedback for… For a long time. Alolita knows this well.
Yes. Sometimes, sometimes for too long. Right, exactly. But, you know, there are good reasons for it, like, you know, maybe there's better, you know, there's more discussion needed about the, you know, what needs to be covered in a blueprint, and there's still, you know…
**Alolita Sharma** 24:22 I mean, given, Dan, given that these blueprints are, you know, reasonably concise, right? So, maybe we can recommend a time… a timed process that is… because… check… think about it this way, right? If we are talking about, some… specific configuration blueprints or specific, you know, GenAI, you know, conventions being used for instrumentation or auto-instrumentation. The implementation is changing constantly, so… or evolving, I should say, so… You know, what is not… say somebody publishes this, 6 months later, it might be out of date.
And…
**Dan Gomez Blanco** 25:12 That's a good… that's a good question, actually, but I think some of these will be… it'll be part of discussing them here as well, right? That is, like, I wanted to discuss the one for a couple of proposals.
**Alolita Sharma** 25:23 Yeah.
**Dan Gomez Blanco** 25:24 One is related to MCP, for example. I'm like, well, you know, we haven't even, like, you know, there's a project for NCP at the moment. Whatever we write now will probably change in a few months, because…
**Alolita Sharma** 25:36 Exactly.
**Dan Gomez Blanco** 25:36 You know, so I don't think it makes sense to write a blueprint at the moment for MCP. Like, I think it's better to wait. Yeah, so I think that's… That's a good point.
**Alolita Sharma** 25:45 But, I mean, if we time box it, right? Like, if we say that, it's 4 pages, you know, which is 20, 2,000 words, 2,400 words, Then, it's done within a month, maybe that's a good cadence, because then we have at least a couple published, you know.
**Dan Gomez Blanco** 26:09 And I think it's good to… it's good to give that both ways, right? The indication of time as well, time box it.
For, like, there may be end users that are coming and, like.
**Alolita Sharma** 26:19 Yeah, exactly.
**Dan Gomez Blanco** 26:20 Contributing for the first time, and they might get a little bit frustrated that A blueprint might need more time to… to be reviewed, right?
**Alolita Sharma** 26:30 Yes.
**Dan Gomez Blanco** 26:31 I don't know, you're trying to get, like… You don't… you might be touching multiple areas, and you want to get a bit more of a cross-functional review, so it's okay if it takes a little bit longer.
But maybe, yeah, I think to your point, I think that's a good idea, to time box it.
M.
**Alolita Sharma** 26:48 At least for some things, right? Because again, it's a good practice, and let's keep it not too long of a blueprint so that folks can, you know, again, add versions to it later if they need to.
**Dan Gomez Blanco** 27:03 Yeah, yeah, definitely.
**Alolita Sharma** 27:04 Because at least then there's an, there's a sense of, you know, folks also being able to present, their… Because in the, in the tab, right, in the end-user discussions, as folks have submitted reference architectures, what we have been doing is encouraging them to, You know, submit more, and then… fundamentally, you know, maybe thinking even about having an Lightning Talks kind of a session at KubeCon, where folks who have published their, you know, blueprints, actually can, present on what, you know, kind of the core areas were. We had… remember, Dan, we did that for CERN, in the, Amsterdam KubeCon, and it was actually quite, quite cool to hear them, you know, as to what some of their assumptions were, and what were they actually, proposing, so… I do.
**Dan Gomez Blanco** 28:05 Speak to the… about this, actually, to the rest of, of the, of an end user, say.
**Alolita Sharma** 28:11 I think…
**Dan Gomez Blanco** 28:12 If we have, because it's related to blueprints, but also, like, I think for reference implementations.
sense that when people write them, then they go to one of the old OpenTelemetry live sessions, right? Oh, tell me, and then, you know, it's just like a live… yeah, as you said, you know, lightning talk with some.
**Alolita Sharma** 28:29 Oh, yeah, yeah, that's a great idea. I like having even podcasts or, you know, short, videos, which… which would tell me is a great idea. That's fantastic.
**Dan Gomez Blanco** 28:40 Awesome. Sorry, I'm conscious of the time, do you get… you got some feedback there, Luca, on… on some of the… The thing's too, so, like… Change or modifying that triage.
**lciukaj@splunk.com** 28:52 Yes.
Yeah, yeah, yeah, I'll be working on that, and I will update the GitHub issue with what we just discussed, that we have two separate GitHub repos.
So we will be, like, focusing on the first part only.
And, yeah, like, I will simplify that, so, so, so I know what I should update in the GitHub issue, so I will.
**Dan Gomez Blanco** 29:16 And then what I'll do is I'll take an action to, add a checkbox to the issue templates, say, like, you know, you write the template.
**lciukaj@splunk.com** 29:23 Thank you.
**Dan Gomez Blanco** 29:24 It wasn't.
**lciukaj@splunk.com** 29:26 Closing this topic, so do you think, like, do we need some additional labels in End UserSeq for blueprints?
**Dan Gomez Blanco** 29:34 We should… what we should have is, If you can create a PR.
you know, with… there is an architecture subsection in the second user report, right? Maybe, like, if you document it there in a small document, then we can create the labels afterwards. Say, like, this is the… this is the process, and then we'll create the labels It takes no.
**lciukaj@splunk.com** 29:57 Yeah, it should be something simple, like, I don't know, blueprint under review, or then approval for just 2 or 3 of them, like, end user seek, and then we move to the OpenTelemetry and the IO to Docs. Okay, yeah.
**Dan Gomez Blanco** 30:12 If you want some inspiration, I can link you to the triage.
Document to the process in the spec.
**lciukaj@splunk.com** 30:19 Okay, yep, please do so. I can take a look. Awesome. Okay, I think we're gonna close this topic and move to the next one.
**Dan Gomez Blanco** 30:27 Alex.
Actually, you had your hand raised.
Because you've got a yellow background, I…
**Alexandre Ferreira** 30:33 Mr.
**Alolita Sharma** 30:33 I know, we missed it.
**Alexandre Ferreira** 30:35 I just thought that, like, I had to, like, lower the contrast on my background or something, but, the reason I had my hand raised is that perhaps what we were discussing on the, like, overall blueprint template and guidelines.
kind of ties with some of my comments within the Kubernetes, blueprint. So, I'll share my screen real quick to… to… Nope.
I have, like, the overall comments about the review that I made, but before that, So, this is taking consideration, like, the template, but also the framework that's mentioned within the .MD commons, right? So, like, you have the guidelines. I mean, you have the challenges, and then when you're implementing a guideline, you have to tell which challenges it addresses, right?
Which is okay, but then, as I was, like, doing this, and, like, actually me and Claude, right? So, I use AI to generate some of this.
we have some, like, references, like, okay, you have to use the presets from the help track, right? And here's how to enable them.
But… Consider that every single snippet of configuration could work today, but tomorrow, something of this may change, right?
So, ideally, I don't want to tie the… maintenance of the blueprint to any specific configurations, right? So, like, my thinking is that I'll probably just remove every single snippet of configuration here, and just point to the documentation set. This will make the guideline overall, like, more concise, right? Because this is a bit long because of the snippets.
And… to my point that I had my hand raised, perhaps we should Mentioned this in the overall, like, guidelines or template, that, hey.
The blueprint is a guideline to how navigate… Throughout the challenges that you have.
But refrain from actually putting configuration in here, because you run the risk of this being dead on arrival, right? Like, what if this changes, for example? Like, the ceiling agent or the CNR or something? So this is my first comment. I would like to get your feeling if… This makes sense.
like, suggested alerts and all that. I'll just scrape all of this and say, hey.
If you're here, like, if you're trying to implement, like, the Kubernetes presets.
just go to documentation and see how to do it yourself, right? So, like, does this make sense for you?
**Dan Gomez Blanco** 33:33 I think that makes… I think to me, and I think that's the pattern I've been trying… I was trying to follow in mine… in my blueprint, at least, is that… I see Blueprints as, like, a very useful collection of links to other places. And there is one thing that the website documentation does, which is it validates every link.
So if for some reason that component or that, you know, that document that you're linking to were to disappear, then the… documentation would fail. The NEPR then after would fail the checks. So there's… so that's why I think blueprints having links rather than snippets makes more sense.
And then, you know… the maintenance of that, unless it's, like, something that is… I don't know.
Mmm… I'm not entirely sure when I would add a snippet. Maybe a snippet that is… not… doesn't need to be maintained, that… but I don't know, I just… I can't really think of it right now. I'm not saying no to snippets completely, maybe if it makes sense, but, like, yeah, to your point, I think for collector config, for example, that could change, and then it depends on the version of the collector they're using, and not, like…
**Alolita Sharma** 34:47 Yes, absolutely.
Yeah. Oh, my God.
**lciukaj@splunk.com** 34:50 We had the same discussion, I believe, last time when Kyle joined from Splunk. He wanted more, like, detailed configuration details, etc. So, yeah, there is… my view on that is the same, like… Blueprint, yeah, we can give a little bit of the config details, or something that we are sure that is general, and it's not gonna change, something that is useful. The rest, as Dan mentioned, we can put the links, references, and the reader can take it from there. So that's my understanding of Blueprint and how we should continue.
**Dan Gomez Blanco** 35:27 There is one thing, though, which is, I think we are… it's very early days, but we should probably… I don't know.
See how… when we finish this.
first round of blueprint, see how it evolves, is the… in the Ecosystem Explorer.
Now, for… I'm not sure if it's for the collector, it's definitely for declarative config for Java.
you can basically do, like, a checkbox exercise of, like, I want this and that and that, and it specs out some configuration. Right.
Which is really cool, right?
But again, you know, that's maintained by the Ecosystem Explorer, and it would be like, if you could link to something like that from a blueprint, that would be awesome, right? Which is like, okay, you know, go here, mark this, that, and that, and then it generates some config, yeah, but I don't think it should live in the document itself.
**lciukaj@splunk.com** 36:18 Beautiful.
**Alexandre Ferreira** 36:18 What's the, what's the name of that again? Resource Explorer?
**Dan Gomez Blanco** 36:22 the Ecosystem Explorer.
**Alolita Sharma** 36:25 Yeah, it's… I think it's part of the docs, or accessible from the docs, right?
**Dan Gomez Blanco** 36:29 Yeah… what is it? Mmm… Actually.
I'm struggling to find it.
If I go to ecosystem, I can't see it, so…
**Alolita Sharma** 36:42 I think that's what it used to be called, maybe the name has changed.
**Dan Gomez Blanco** 36:44 The registry, it used… yeah, but.
**Alolita Sharma** 36:47 Yeah, it was a registry area.
Let me look also.
**Dan Gomez Blanco** 36:52 Explorer is explorer.opentelemetry.io.
**Alolita Sharma** 36:55 Okay, okay, cool.
**Dan Gomez Blanco** 36:59 And then if you go to the Java agent, there's a config builder.
I'm not sure if it is for the collector as well, but… Collector Explorer is unavailable, so I guess, you know, it will… It will be there at some point.
**Alexandre Ferreira** 37:15 I'll just add this for my reference loading.
**Dan Gomez Blanco** 37:17 I haven't seen that, that's really cool.
**Alolita Sharma** 37:18 Yeah, it is. Cool.
**Alexandre Ferreira** 37:21 Yeah… It is really, really neat.
**Alolita Sharma** 37:23 Awesome.
**Alexandre Ferreira** 37:24 Oh, nice.
Alright, so…
**lciukaj@splunk.com** 37:27 As AI is getting more advanced, I think we'll see more and more.
**Alolita Sharma** 37:32 the same models! Nice.
**lciukaj@splunk.com** 37:34 interactive documentation and generating some stuff, some con… I mean, why not? Why not?
**Alolita Sharma** 37:41 It's becoming easier, right? So it's definitely a.
**Alexandre Ferreira** 37:43 Good thing.
**lciukaj@splunk.com** 37:45 It's fun, it's.
**Alexandre Ferreira** 37:45 Right.
**lciukaj@splunk.com** 37:46 plus something we had internally here at Cisco at Splunk, like, like some… you know, the presentation about how we can leverage AI for building the demos and customized stuff, right? I believe every vendor is doing that right now, right?
**Alolita Sharma** 38:00 Oh, yeah, yeah, it's, it's, again.
**lciukaj@splunk.com** 38:02 But then we started discussing.
**Alolita Sharma** 38:03 Yeah, yes, yo.
**lciukaj@splunk.com** 38:04 for the future, like, that maybe in a few years, there will be, you know, on each vendor website, there will be, you know, just a couple of checkboxes, and customer can provide the use cases, and then there will be, like, you know, the demo generated in Fly, with some, you know, AI-generated voice, or something like that. So then, what's the future of pre-sales engineering then, right?
**Alolita Sharma** 38:24 That's really good. There you go. Very happy people.
**lciukaj@splunk.com** 38:27 I think it's part of this blueprint stuff, and all of this, you know, the documentation and guidelines, and so I think that there is this, like, transitioning and changing very dynamically, so we.
**Alolita Sharma** 38:38 I think, I think, you know, one of the things which I think, Lucas, to your point, is that the idea of a playground, which has always been very useful and, you know, very, very valuable, will, will become very dynamic, which is very cool, because the playground then can be used for, you know, hey, I have this blueprint, you know, this is my configuration, you know, build it out.
It kind of…
**Alexandre Ferreira** 39:04 Yank.
**Alolita Sharma** 39:05 And that makes it really very useful.
**Alexandre Ferreira** 39:09 I'm too convinced.
**Alolita Sharma** 39:10 Get out what works and doesn't.
**Dan Gomez Blanco** 39:12 C-coo-coop.
**Alexandre Ferreira** 39:13 But this reminds me of, like, the Atelbin, you know, if you have seen this, but, like, this is amazing. And I would expect that the next step on, like, all of this is… whenever, like, I'm trying to generate configs from LLMs, sometimes they hallucinate it out, right? Like, they take a configuration that doesn't work anymore. It'll be sort of, like.
adding a pipeline to the agent where it could validate the config that's generating, right? So, like, the LLM generates this config and tries to run it, and if it runs, okay, that's a valid configuration, right? Like, so I would expect that This would be the next step into all of this.
**Alolita Sharma** 39:55 I have a… I have a question here, or a point I wanted to bring up. So there is a standardization effort that's happening on the format between you know, agent-to-agent communication, and why I'm bringing that up is somewhat related, because there's an evolution of a kind of a knowledge format, right? And you've seen that, you know, OKF got released from Google. And the question I have here is that, could we actually envision a bit more, you know, kind of to be forward-thinking, where our formats or templates that are currently, you know, we are leveraging for blueprints becomes more aligned with, you know, some amount of these formats, because then, you know, fast forward 6 months from now, if we have agent and agentic interface, then that could be just consumed, and the blueprint could be consumed along with the configuration, and just, you know, the result could be generated, right, by an agent. So…
**Dan Gomez Blanco** 41:07 Yeah, absolutely. I think already, like, you know, I've seen… well, I was… hooking that up to the MCP server, I mean, it's already been automatically done with the Cabat AI stuff on the website, so you.
**Alolita Sharma** 41:19 Yeah.
**Dan Gomez Blanco** 41:19 As long as the blueprint is already… Published, you know.
However, yeah, to your point, I think I can see that.
Maybe that's something to discuss next time. A bit more structured.
**Alolita Sharma** 41:32 Yeah.
**Dan Gomez Blanco** 41:33 And I think, you know, almost like building a… a set of, you know, scales as well, for, like, you see these common challenges, and there'll be common patterns, design patterns that you… Yes. …that you want to apply, yeah.
**Alolita Sharma** 41:46 Because some amount of it, and again, you know, could be done through skills, right? Like, some of the triage or review, you know, some amount of it, and it's a nice thing to be able to kind of add in, in a limited, you know, way initially, but as Bhavar… templatization assumptions are right, then we can clearly, you know, kind of use that framework as we go forward.
**Dan Gomez Blanco** 42:17 Conscious of time, do we want to go through… I'm not sure if we're going to have time to go through the blueprint to discuss it, and Alex, but…
**Alexandre Ferreira** 42:25 No, I don't discuss all of this, we can do this async. The other comment that I would like to make here is that, like, we chose some components to add here as examples, like, KEDA, And, like, other stuff.
but… once we come, like, to this, and I think Lucas made a comment that made me, me, reflect a little bit on this. So I… if we… Select every single, like.
it doesn't matter how many components we put here, like CADA or, like, ingress controller and all that, like, it could be that someone is using NGINX or Trapic, but, like, someone could be using anything else, so, perhaps I'll just mention some of those tools in the guidelines, so people can be aware that, like, each Kubernetes platform will have its own specific services for its work, but on the guideline… on the guidelines itself, I'll just mention something like, hey, you have to map the services that are imported into your cluster and figure it out yourself, right? Like, if there is NGINX, go search for this.
And this will make the, the blueprint on itself be even more concise, right? So, like.
those are, this is what I'm thinking on working as well, and that's why I put this comment right here.
and yeah, there's our…
**Dan Gomez Blanco** 43:58 So what you're saying is, like, instead of, like, each of the components, what you can say is, well, you know, these will expose Prometheus metrics, because it's Kubernetes, like, you know, Prometheus is, like.
lingua franca, let's say. So then what you're doing is, like, you're explaining how to enable a Prometheus receiver for these, and blah blah blah, right?
**Alexandre Ferreira** 44:22 Yes, yes. So, and… After that, I would say that the Blueprint would be ready for, like, another set of reviews, and then perhaps publishing this.
And I… I hear the… on… we were discussing earlier that, hey, we want to, discuss this in the doc first before opening the PR, but since We've been, like, reviewing most of this on the PR, Perhaps we can continue, this way for this blueprint, and then the next ones, we go first to the doc, and then…
**Dan Gomez Blanco** 45:00 Actually, I'd like to see your… I'd like to get your opinion on, because I've never really… I mean, one thing, you can open a draft PR, which is what you've done, and it's completely, you know, a valid approach, and the other approach is… the… you know, Google Doc, separately. However, like… there are… Very, very niche cases, right, where companies are not allowed to work with Google.
Tulin, but there are.
**Alexandre Ferreira** 45:26 To work with.
**Dan Gomez Blanco** 45:27 GitHub, right? Very, very niche, but, like, I don't know, maybe there is an element of, like, maybe you just… we open a draft PR. So what I… I would like to hear after this, your… your feedback on, like, you know, the… opening a draft PR rather than a Google Doc.
If that makes sense. Alright.
**Alexandre Ferreira** 45:49 I'll do that.
Yeah, I think that's me for today.
**Alolita Sharma** 45:53 I think, though, Dan, that… Maybe the initial work can be done with a Google Doc, and then, you know, the final PR is done as a PR, obviously.
**Dan Gomez Blanco** 46:05 Yeah, so that's what we originally, you know, proposed. I think, and then that's… that's how Lucas and myself have done it in the… I know that Alex, you created that originally that way, but, you know, again, you know, it doesn't really… make a massive difference. It's more like, you know, that the PR will be slower for people to, like, I don't know, maybe a bit more difficult to add comments fast and edits fast, right?
**lciukaj@splunk.com** 46:30 And also, the comments in PR stays there, right? You have the entire history, like what you have in the Google Docs.
**Alolita Sharma** 46:36 Exactly.
**lciukaj@splunk.com** 46:37 transitioning that to the GitHub, so… Yeah, I think that, yeah, Google Docs is good, but having it as a… but again, like, coming back to the trash process, like, we don't want to have PR opened until we have, like, a.
**Alolita Sharma** 46:51 Yes.
**lciukaj@splunk.com** 46:52 By the blueprint piece.
**Dan Gomez Blanco** 46:53 You know, there's… there's… yeah, I guess the aim is to… reduce… The noise in… for other people, right?
So that'll make sense.
Cool. Awesome. Right, just a quick update on the PR that's in progress, the other one, the… the one for managed platforms.
Got a respo- got a review from, well, from Jurassi and… and CJO, got a review from, from Jacob as well, from the perspective of the operator.
**Alolita Sharma** 47:29 Cool.
**Dan Gomez Blanco** 47:30 I've been trying to ping the collector folks, I pinged, like, Pablo, and Braden, and other folks, and I think Braden was, like.
Having a look at it, but, like… people not seem to have much bandwidth. So, yeah, just basically trying to be patient here, and get a review from the collector folks. I did ping the config.
SIG as well, the declarative Config, just because I mentioned it. I got from… I spoke to Jack, to Jack Berg, and JAG has basically said that there's not a lot of things there in terms of the collaborative config. I was like, well, so he doesn't seem to think that there's, like, much value in him approving or not approving.
So, I guess, you know, if we get the collector folks approving the operator as well.
I think we should be okay, with this… with this one?
Let me know if you think otherwise, but yeah.
And then, any other comments, still welcome, but yeah, I think that's… Pretty much ready for copy edit, apart from the comments from the… wherever the collector folks… One to us?
**lciukaj@splunk.com** 48:40 Do you know if… now, Tiffany, she updated us that she won't be able to focus a lot on the blueprints. Do you know if we have, like, any other main contact from Doc's team that would be working with us for Blueprints?
**Dan Gomez Blanco** 48:53 Yeah, so I spoke to… I spoke to Tiffany, and she gave me… yeah, she, she said that I originally thought Patrice would be in that, but I think Patrice is also, not, like, coming in and out, but there is, like, other folks in…
**lciukaj@splunk.com** 49:07 Okay.
**Dan Gomez Blanco** 49:07 And either Fabrizio or other folks that might be able to…
**lciukaj@splunk.com** 49:11 It would be good to have, like, you know, the go-to person for blueprints that we could ping and always, like, you know, get some quick support if needed.
**Dan Gomez Blanco** 49:19 I think that was the… I mean, that was why Tiffany originally joined the project. Yeah, I think she still wants to be involved, but, like, she doesn't really have the bandwidth at the moment. But, but yeah, let's see how it evolves for these ones, and…
**Alolita Sharma** 49:34 Maybe… maybe, Dan, we can also do some campaigning for some more folks to join in, so that… on the docs team, so that they can… they can also learn and help.
**Dan Gomez Blanco** 49:45 I'll chat with him, too.
**Alolita Sharma** 49:47 Yeah, it's a good opportunity, right? So, I think…
**Dan Gomez Blanco** 49:50 Yeah, I know that, yeah, I checked with them, see if, they want to… to get involved.
Yeah, and that basically is… that's pretty much it. There's one thing… one thought I was thinking of, Again, that blueprint, the one that is up for review, I think it's borderline… long, and.
**Alolita Sharma** 50:11 Yes.
**Dan Gomez Blanco** 50:13 I think what I would like to do is, like, publish it as it is.
But then perhaps remove parts in the future and put it into a separate one, as in, like… I think it's fine as it is, but I wouldn't mind, for example, taking the sampling part of it.
And then create a blueprint for sampling.
And then take that out of fear, and maybe evolve a little bit more in something, right?
**Alolita Sharma** 50:35 Yeah, that's a very good idea, actually, Dan. And also, any other section you think can be standalone? Maybe we can move some of that detail into appendices, so that then what happens is we could take, you know, those appendices and make them blueprints of their own.
**Dan Gomez Blanco** 50:55 That's… That's a good point, yeah. I think… I'm not sure… there is… There are two aspects of it, the… self-observability that I think CJ was saying, like… and I think I had a discussion with Cijo on this, CJ was like, oh, I should be in here, maybe it should be elsewhere, and I know that now that I'm seeing the… the blueprint from, you know, from Alex, and I think Lucas as well, mentioned that self-observability of SDKs and collector, maybe that could also be… a different one, so I basically… I… taking it out now, basically, will… Will mean that we… we end up with… another set of reviews, and I think, you know, I'm happy to do it, but, like.
I don't know if it's easier to… no, not easier, but better to publish this first.
And then split that into, as we're seeing patterns of marriage, split that into… into other… into our separate blueprints.
But, like… I'll open up for…
**Alolita Sharma** 51:57 I think… I think, going forward then, it'll self-adjust, because if we put in a word limit, you know, obviously that'll help. But, for this one, definitely, I think your idea of splitting it out, you know, or maybe even moving some sections which are very detailed into appendices may be… a good way… make it easier to read, right? Because if it's too long, then people don't read enough… all the detail.
**Dan Gomez Blanco** 52:25 That's a fair comment.
Mmm…
**Alolita Sharma** 52:29 I mean, should we try? Do you want to… Go at it one pass and see if that can be even doable.
**Dan Gomez Blanco** 52:38 Mmm…
**Alolita Sharma** 52:39 Or should we just leave it as is?
**Dan Gomez Blanco** 52:42 I could do it, I could have a… have a pass at it. I think there are definitely some… Yeah.
Let me have a go at it, and see if I could… Put it into appendices.
Okay, I'm just… sorry, I'm just looking through the… Through the template, through the… Blueprint at the moment.
Okay, yeah, I'll have a look at it.
Now, the one… I know that we've got 5 minutes, but there's one thing that I wanted to discuss, and let me share my screen.
So I think it'll be easier to explain.
This proposal.
I'm not gonna go through it, and I found it actually quite difficult to read, so…
**Alolita Sharma** 53:38 I can go through it, Dan, because given I'm working in this space, I can definitely go through the proposal, but…
**Dan Gomez Blanco** 53:47 Okay, so I think, you know, one thing that is clearly, like, AI generated, and I'm okay, I mean.
**Alolita Sharma** 53:51 Yes.
**Dan Gomez Blanco** 53:52 Yeah, as long as people are… But it seems like… what I can get here is that… there was a response here to an account that doesn't exist, right? Or, like…
**Alolita Sharma** 54:04 Yes. Yeah.
**Dan Gomez Blanco** 54:05 and there's, like, I don't know, there's just certain things where, like, they seem.
**Alolita Sharma** 54:09 Should we, should we reject it until, some human shows up?
**Dan Gomez Blanco** 54:15 Yeah, and then even this was also released when it says generated. So I'm… I think I'm… what I'm proposing is rejecting it. Of the… from the premise that is, and, you know, I'll let you go through the… through the comments, but it's, like, it's trying to confuse two things. One is, like, basically doing… proposing some new soundconf, which is not what Blueprint is.
And the other one, even, like, getting into the scope of, like.
NCP, or, like, on, like, backends, almost, already?
**Alolita Sharma** 54:46 Yeah, yeah.
**Dan Gomez Blanco** 54:47 Which is basically why I said here is, like, you know, And… Yeah, I think… I would propose to reject it unless they come back.
I don't know, this week, and they… they… Reshape what they… what they wanted to… Talk about, but if no one responds here, that doesn't… Sound like a human. Yeah, I don't think this is insane.
**Alolita Sharma** 55:14 No, no, but you can see this. This is the same thing that is happening in the GenAI 7Con repo. So if you… this is an example for… if you click on that link, Dan, the 3816, so you'll see that it's the same generator, if you scroll down.
You know, this, this guy.
**Dan Gomez Blanco** 55:34 Alright, yeah, yeah.
**Alolita Sharma** 55:35 So they are, you know, actually… and if you read these, these are all generated. They don't actually necessarily, and there are, like, hundreds of them. Literally every issue, they are going and posting, as this, you know, this ID.
**Dan Gomez Blanco** 55:57 Yeah, yeah.
So, yeah, so I think I will… I mean, this person did not, like… Raising.
**Alolita Sharma** 56:03 Same, same person, the receipt, the ID is the same.
**Dan Gomez Blanco** 56:08 Yep, yep, that one in particular, yeah.
**Alolita Sharma** 56:10 Yeah.
**Dan Gomez Blanco** 56:11 So… Yeah, basically, I'll give it… Another couple days, just in case, like, someone else that commented here.
I see you're commenting from two accounts, Lucas.
**lciukaj@splunk.com** 56:25 This thing can happen?
**Alolita Sharma** 56:26 No, it doesn't.
**lciukaj@splunk.com** 56:28 Huh?
**Dan Gomez Blanco** 56:28 Yeah, cause I…
**lciukaj@splunk.com** 56:30 Oh yeah, it is, sorry.
**Alolita Sharma** 56:31 Oh, your history's getting split out, Lucas, come on.
**lciukaj@splunk.com** 56:34 No, I have, like, I recently started, you know, I created my private GitHub repo and doing some other stuff there, where I'm using my private PC, my private, you know, tools, you know.
**Alolita Sharma** 56:46 Chevy.
**lciukaj@splunk.com** 56:47 Bunny, so I think I'm… I…
**Dan Gomez Blanco** 56:50 So this one is the one that… this one is the one that you're a member of the OTEC.
**lciukaj@splunk.com** 56:53 Exactly, that's my corporate and open telemetry one. That one is private one. I mean…
**Dan Gomez Blanco** 57:00 Alright.
**lciukaj@splunk.com** 57:01 be any problem, but no.
**Alolita Sharma** 57:03 I don't think it matters. You can just link the two together.
**lciukaj@splunk.com** 57:07 Yeah, I decided to split that, that, that work at some point.
Quick question here, coming back to the triage ones, do we need to get some insights from the docs team, what they expect from us as part of, let's say, the pre-validation and the first stage validation? Or not really?
**Dan Gomez Blanco** 57:28 Don't… I don't think we do. I think it's, you know, basically… because it's part of the blueprint.
It'd be good to let them know, I guess, if we have someone from the docs team.
join, but I think… Blueprints triage.
**lciukaj@splunk.com** 57:43 Yeah.
**Dan Gomez Blanco** 57:43 It happens elsewhere, it doesn't happen in the docs website. I think it's fine if we come up with our own.
With our own process, and then we just shared it with them, right? And say, hey, you know, we're thinking of doing this.
Okay.
**lciukaj@splunk.com** 57:57 That's good. So I will update the GitHub issue, with…
**Dan Gomez Blanco** 58:02 Something that would be interesting is, like, they… they probably have it documented somewhere, I don't have a link here.
look at their triage process in terms of, like, the PR.
you know.
Maybe that's something that we want to link to.
As well. So if you're writing down a triage process, and say, okay, this is how you're, like… when you get here, this is ready for… wherever, PR, and then there will be a… and then maybe we want to link that to the… to the docs process, right?
And then there will be a process that kicks off when you open up PR.
In the… in the website, which is blah blah blah blah blah.
**lciukaj@splunk.com** 58:38 Okay.
Sounds good.
**Dan Gomez Blanco** 58:41 And I think they should… we should be fine with that. That requires… that will require the docs approval, and that will require the SIG approval, and by SIG, we mean… Our sake, right, the end user's sake approval, so…
**lciukaj@splunk.com** 58:53 Hmm, yep.
**Dan Gomez Blanco** 58:54 That's the way that the docs PRs work.
And I don't think… and then we discussed this with Tiffany, that for now, we don't need a sponsor, as in, like, when you have a… when you write a blog post, for example, you need a sponsor.
But for blueprints, because we have the… the approvers, and the Blueprints Approvers team, which we will have, that should be enough for the… for the website.
**lciukaj@splunk.com** 59:21 Sounds good.
Not yet.
**Dan Gomez Blanco** 59:24 Good stuff.
Cool. Okay.
**Alolita Sharma** 59:26 Very cool.
Dan, next time onward, should we, keep, like, 5 minutes to review all the incoming proposals, if any?
**Dan Gomez Blanco** 59:39 Yeah, we should, we should, dedicate some time at the start.
To review that.
**Alolita Sharma** 59:44 Yeah, maybe we can just timebox, like, 10 minutes or 5 minutes, whatever, makes sense.
Alrighty, coolness. Thank you. Thank you, everyone. Take care. Bye.
