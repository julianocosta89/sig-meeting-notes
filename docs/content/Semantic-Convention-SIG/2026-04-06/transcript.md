SIG: Semantic Convention SIG
Date: 2026-04-06
Duration: 60 minutes
Zoom Recording URL: https://zoom.us/rec/share/q2JskWLUFk1Wz5dabsLT5z4Jl984IWC3BaFINTY8NbgNP8vmNbeEbsRpkHZ7maiU.vQk80ibIW5Fax2KY
============================================================

## Zoom Recording Transcript

Victor Lu 00:01:18 Hey, good morning.
Question?
Christophe Kamphaus 00:01:23 Good morning.
Victor Lu 00:01:24 Yeah, so, I've been attending a different meeting, but this is actually just a general question. There's, some interest in extending OpenTelemetry.
to cover AI security. However, there's some discussion about Where… whether that… those kind of matrix… belong completely as part of OpenTelemetry versus another spec called OCSF for analytic purpose.
for example, time series, etc. Which open television meeting is right for that discussion?
Josh Suereth 00:02:05 I think… so, one of two meetings?
This meeting, when Lun Milla gets here, I think she can help talk about that. Or, we have specifically a generative AI meeting, but this is the OpenTelemetry Semantic Convention meeting, where we talk about, like, OpenTelemetry Semantic Conventions, what they are, what we do, how we try to promote them, etc.
Victor Lu 00:02:26 Cool, so this is the right meeting.
Josh Suereth 00:02:28 Yes, yes.
Victor Lu 00:02:29 Cool, thank you.
Josh Suereth 00:02:30 Yeah, we're, we're a bit, I think, Maybe everyone's a little bit slower today, but, yeah, we… Anyway, we're starting to show up.
Here's Labila, by the way.
Liudmila Molkova 00:02:41 below.
Josh Suereth 00:02:43 Do you want to restate your question for Ludmel?
Victor Lu 00:02:46 Yeah, I, participate in a community called COSI, Coalition for Secure AI, where it's been discussed to extend OpenTelemetry to cover AI security, and then there's discussion, almost a debate, on whether it can be all… be added as part of OpenTelemetry.
Versus another spec called OCSF for, analytical, purpose, because that is, I would say, much more… my understanding, much more data-intensive. It's also, you know, kind of mostly using columnar for analysis and, time series, so… so different kind of use case. So, yeah, so I… that's why I, come to ask, is this the right place to… discuss what type of matrix is a fit for OpenTelemetry versus, like, OCSF.
Josh Suereth 00:03:39 So.
Liudmila Molkova 00:03:40 Yeah, trust.
Josh Suereth 00:03:41 Go ahead. Sorry.
Trask 00:03:43 Yeah, thanks, just wanted to jump in, because I have a little bit of, background knowledge here, Nagkumar from Foundry has reached out to, he has submitted the… guardrails, I think the, PR in… some conv.
And has been looking at security, AI security, semantic conventions, and I had suggested to him to reach out to the OCSF community, to discuss with them I don't think much has happened there, but I know in the past, we have reached out to OCSF, because That's been an area… security has been an area that we've struggled to get off the ground in OpenTelemetry.
And so potentially there is good collaboration to be had there.
Victor Lu 00:04:47 Yeah, actually, Nag… I talked to Nag, and he actually invited him to join the co-sign meeting. He didn't… he passed… he joined, I think, twice, didn't join last week.
But, yeah, so, the… if there is interest in collaboration between this community and the OCSFs, I can because I also participate in the OCSF side as well, as a generalist. So, so I guess the… sounds like at least there's… this is not clear, right? So, whether it should be, What type of matrix should be in OpenTime versus OCSF?
Christophe Kamphaus 00:05:32 Yeah, exactly.
Trask 00:05:32 Certainly.
Christophe Kamphaus 00:05:33 It also doesn't have to be either or. It could be that we have a mapping between both.
Josh Suereth 00:05:39 I think… I think I want to call out, we need to aim for compatibility, and we've known this with OCSF for a while. I think the writings on the wall that observability and, security observability, or, like, the signals that you use for… like, if you think of security as both signals and policy together.
Observability is the signal part, and we're seeing a convergence where people are starting to want the same thing that extracts the signals to work for both cases, because instrumentation is hard and expensive.
And so semantic conventions are a way for us to kind of share instrumentation between different places, and there's a convergence that's occurring between observability and security, and agents are driving it real hard.
Because, That's just, you know, if you want to see what an agent's doing, the security aspect's really important. So, I… I… I just want to call out, like, you're saying, hey, I don't think this fits here, I don't think this is the right kind of data. I would challenge that highly. I think we need to get these two communities to align and work together well, and I think what I'd like… what I think is success for us is if we get a set of instrumentation that gets the signals out.
in a way that everyone can consume it. That's the goal of this group.
Right? And we don't care, necessarily, exactly, like, the, I mean, this group does care a lot about the shape of signals, but from my perspective, our overall objective is we want people to share that instrumentation and be able to reuse it across a lot of components, because the instrumentation is expensive, and we want a community within the Linux Foundation and CNCF to own it, right?
So that we can all share it. That's the key.
That's what we're going after, and I don't think, honestly, everything in OCSF could be here. A lot of things that are here could be in OCSF. We need to bridge the gap.
Right? And I think we need to start having those hard discussions, because it's coming. And we see this almost every day, of various security things and observability kind of clashing.
Victor Lu 00:07:36 Yeah, I'd love to… if there's any documented, what you're saying, I mean, I definitely agree, it's, it's not just either or, it can be both, doing the similar. The main question is, for example, the person, OCSF person I talked to, his, com… he's… just his job is processing, I think, like, one petabyte a day. Is that what OpenTelemetry is built for, to process amount of data per day?
Liudmila Molkova 00:08:06 OpenTelemetry is not for processing the data, it's for generating the data, but the backends who process the data from OpenTelemetry can do much more. I think Joshua Trask can speak on the Google or Microsoft load that, yeah.
Josh Suereth 00:08:21 Yeah, that's not an unheard of load for us.
Victor Lu 00:08:26 Okay, good, good to know, yeah.
Yeah, again, this is from a kind of a third party. COSI is not either CSF or OpenTelemetry. They're trying to understand how to, you know, best use this thing, and Yeah. So, if there's any, I think until there's a kind of formal dialogue, I can, you know, just take the information and put back and forth, and let the community kind of start talking.
Liudmila Molkova 00:08:53 We didn't have a good story of, like, writing down the strategy of how to work with OCSF, and we… we didn't develop a plan, but… We can, but also, if… If it comes to AI security, maybe this is the good first place for us to start collaborating. I think the worst outcome is that we have two separate specs that don't.
talk to each other, or we never talk to each other. I think we should try to build something in common, and the AI is so hot that we have a lot of resources. I don't think we can come up with, like, okay, this is the final strategy between OTEL and OCSF.
Without doing some pilot projects.
Victor Lu 00:09:38 So who should I follow up with about the possible dialogue with OCSF?
Liudmila Molkova 00:09:47 I think we have a Slack chat for the security, semantic convention security, but it went quiet. I think people you see here, semantic convention maintainers, are the best people, too.
To have dialogue with.
Josh Suereth 00:10:01 Yeah, there's a CNCF Slack channel in Semantic Conventions, and then we were all invited to join the OCSF Slack, which I am on, but I'll be honest, like.
work makes Slack hard to use, so it's hard for me to be on, like, a separate Slack workspace and have all of them open. So, I haven't paid attention to that, but there is a channel in OCSF's Slack for open telemetry and semantic conventions and OCSF to chat.
I'll see if I should find that link.
Victor Lu 00:10:31 So you're already on there. Let me see whether, either, yeah.
Josh Suereth 00:10:35 Riley Yang is the one who kind of organized all this initially, if I remember right. Like, he was doing some work, but I don't know what… it kind of just dropped, basically, the discussions between OCSF and Optel.
Victor Lu 00:10:47 Yeah.
Josh Suereth 00:10:47 Personal.
Victor Lu 00:10:48 So there's actually a meeting called Mapping. Have you ever attended that meeting?
Liudmila Molkova 00:10:54 Mapping?
Victor Lu 00:10:55 Mapping meeting, yeah, OCSF mapping.
Yeah, so that's where it's been discussed. So what's happening is they are actually creating a new AI mapping, so I think it's probably the right time, yeah, as I said, it's the right time to discuss, how do the two fit, and, So, yeah, George, I try to find you on… OCSF, you're not active there.
So, yeah, it'd be great, yeah, if you're already on there, it's much easier, because they, they, they, I'm not sure what's their policy for… because I'm also a kind of guest on there. so, yeah, the mapping meeting on Thursday at 2 p.m.
is where it's been discussed, and they're really interested in the dialogue and see… because what's happening is, a lot of people…
Josh Suereth 00:11:46 By the way, for everyone here.
Victor Lu 00:11:48 Oh, yeah, yeah, sorry, yeah, I remember, it's global. 2 p.m. New York time.
Thursday. So if you go to the general meeting, on the general meeting, there are several, pinned meeting information. Yes, if you go to General, let me see, general, and then pinned, then, you'll see there are several meetings listed.
And, and then the one for, mapping meeting is the first one, actually. I'm sorry, no, it's not. But yeah, No, that's mapping language. The mapping meeting is not that one. Finding and mappings, which are the bottom. Thursday, 11 a.m. PST. Let me go ahead and create, and hopefully this is, not, yeah, there don't seem to be as kind of an open community as, you know, CNCF, that's why I'm kind of hesitate to, But let me share it here. Yeah, I'll share it.
Josh Suereth 00:12:48 you're not aware of, there's, there's actually a group in CNCF that met with us, recently as well, that is working on agent observability, like, and security. Like, there's… I… I just want to caution that I think there are many attempts to deal with agents from all different aspects, so I just want to make sure, if OCF… if OCSF is somewhat closed, that has me a little bit concerned, just because of how fast the space is moving and how much people are experimenting.
Are, like, is OCFF grabbing those folks into those conversations? Like, the new, the, the whole agentic, like, tag? Not tag, what are they called?
What's the CNCF call their new working groups? Are they still working groups?
Liudmila Molkova 00:13:34 They are a new foundation.
Dotan Horovits 00:13:36 There's the initiatives under, which is, like, the targeted, short-term, well-scoped, under the tag. That's what you mean?
Josh Suereth 00:13:46 I think Lyudmila knows what I'm talking about. So you said it's a new foundation, Lyudmila?
Liudmila Molkova 00:13:50 It's a new foundation, it's under Linux Foundation, it's a JNJKI foundation.
Dotan Horovits 00:13:54 Oh, the AAIS, you mean? AAIS?
Liudmila Molkova 00:13:57 Yeah, don't…
Dotan Horovits 00:13:58 it's a separate sub-foundation on the DLF.
Josh Suereth 00:14:01 Right, right.
Liudmila Molkova 00:14:02 We… me and Trask started… have started to joining their calls, and they're also closed.
So they only accept people from certain companies, and I could get there only using my hotel status. It was hard.
But Microsoft is there, Google is there.
Victor Lu 00:14:21 Yeah, but for me, I definitely love the open, collaborations, and, and, so… but I think to… the problem for, having a new spec is, at least from a… because I participate in a community called SPDX, Supply Chain Security.
And we worked very closely with MITRE on, a lot of things, ontology. So what OCSF, I think, has been doing right, the other, spec has not done so far, is to, build a, kind of mapping to the MITRE defend ontology that makes real a lot of, automated LRM, kind of, automation possible.
Then, so, I mean, that, that's, so I, I… to be able to do AI, the two… AI security and regular security cannot really be separated, because if you look at the AI use cases, they all start from someone doing traditional, classic security attack, rather than just AI, pure AI.
That's why, if anyone say, I'm gonna do AI only, that just doesn't work. That's the problem. That's why I feel, even if OpenTelemetry decided to, you know.
kind of do everything. It's still good to have a dialogue, and at least a lesson learned on, you know, everything.
Josh Suereth 00:15:35 I agree we need to have a dialogue, I just want my… My overall concern, and by the way, I need to call time on this so that we can get through the rest of our agenda, My overall concern is just that we're having the discussion in a place where the right people are in the room, and that that discussion is going between different communities. Like, again, my point was, these things are moving so fast, and there's so many people trying to get a piece of the pie.
Like, we want to make sure that if we put an effort together, it's set up for success because it has the right people in the room, or because it has the right set of companies behind it, or, like, the standard is in the right place to address the right problem.
So, that's kind of what I'm asking, is basically when it comes to OpenTelemetry and OCSF, and like, who owns what, part of it is really going to be who's positioned in the right spot with the right set of data that will be able to drive that standard.
And they're kind of gonna own kind of, like, the weight of the standard, if you will. We should make sure we're compatible with each other, no matter what, because both standards are going to be used. But that's kind of my main concern of where should the discussion be happening, is what I'm trying to understand. And, like, does OpenTelemetry need to facilitate that?
As a thing that we do. That's overall what I'm asking. I'm not asking, like, hey, is this a good idea? Does this have to be comprehensive? Already sold on that, right? It's just, I'm more thinking about the health of the community and the ecosystem, and the success of that sub-project. Where does it need to belong? Who needs to be in the room? Those are the questions I'm asking now.
Victor Lu 00:17:09 Got it, got it, yeah, okay. I'll follow up with you, since you already have a Slack on the OCSF, I'll follow up with you on that Slack.
Josh Suereth 00:17:16 Okay, I'll have to make sure I'm logged in, so, I don't think I've logged in in quite a while, my bad. Cool.
Trask 00:17:23 I can join on the Thursday Findings and mappings meeting. I'm interested in trying to… I had chatted with them previously, with Riley, And I'm interested in this topic.
Victor Lu 00:17:40 I think that'd be… that'd be great.
Josh Suereth 00:17:46 Cool. Let's… let's get into the agenda. I'm gonna skip triage for now.
Apologies. I'm also coming off a one-week vacation, so I'm a bit rusty here. We'll come back to triage if we have time. Hedril and Christoph, do you want to talk about stabilization?
Christophe Kamphaus 00:18:02 Yes.
Josh Suereth 00:18:02 TV.
Christophe Kamphaus 00:18:03 So, we discussed the, moving the CICD conventions to release candidate status.
And we are all for it in the SIG.
There's just one open issue we thought might be a blocker, or where we might have breaking changes later. That's the one that we put there in the link.
And we wanted to know your opinion.
Can we move forward with CICD, to release candidate status despite this being open?
Or how would we handle a breaking change later?
Liudmila Molkova 00:18:47 To the open issues around workflows.
Christophe Kamphaus 00:18:50 Yes.
Liudmila Molkova 00:18:51 It's unified.
Christophe Kamphaus 00:18:53 Conventions for workflows.
It's been open for a long time without any activity.
So, our thought here is that probably It's not worth it waiting for this.
Josh Suereth 00:19:12 Yeah, I would agree with that.
Message.
Dotan Horovits 00:19:16 I would also say it's, calling it an issue is, makes it an understatement. It's a significant expansion of the, original scope of the, CICD SEM conference.
Christophe Kamphaus 00:19:26 Indeed.
Dotan Horovits 00:19:27 to treat it as such, and by the way, I put a note, a comment on that, actually, recently, I think last week. And I think it falls on something that Lyudmila also said in the past, about making sure that we have well-scoped things, we have, Vast experience in open telemetry, taking too wide a scope, and then getting stuck in development or experimentation or whatnot, so, Concerned about, trying to tackle that will, make sure… delay significantly our ability to, to mature this.
Liudmila Molkova 00:20:01 Yeah, so to provide additional context, in GenAI, we created a GenAI workflow, because it has attributes specific to GenAI.
and some other characteristics specific to GenA and CICD, I would imagine you also have a lot of things that are specific to CICD, and it would be extremely hard to… Explain what this metric means.
if it can be CICD or… or any other workflow, like, I don't know, business process approval.
Josh Suereth 00:20:35 I'm still waiting for a use case where… Having these be abstract makes sense.
that we can demonstrate easily. Like, there's the conceptual, oh yeah, they're both workflows, cool, but give me actually, like, how I'm gonna use that. Like, what UI would I have?
that is workflow-based, that doesn't need to kind of know it's CICD to do a good job. What alerts do I have that are workflow-based? You know what I mean? Like, I do… I… This is one that I remember we talked about… there was a proposal, I don't know if you remember this, Kristoff, like, 3 years ago, to abstract everything to be workflow-based.
Christophe Kamphaus 00:21:16 Yes.
Josh Suereth 00:21:17 And that got shut down already, right?
As being too generic.
I think this is…
Liudmila Molkova 00:21:23 The same proposal.
Josh Suereth 00:21:26 I think it'.
Christophe Kamphaus 00:21:26 this one.
Josh Suereth 00:21:27 That was this one? I thought there was a different one, like, a year before this. No? I guess that is 2 years ago.
Okay.
Christophe Kamphaus 00:21:36 I think when we first defined the CICD conventions, we thought about it.
Dotan Horovits 00:21:45 It definitely… it definitely came up in the… even the original OTEP.
And so… In one shape or form, this discussion already took place, and the phase one already, scoping of Phase 1 was very deliberate in making sure that you have well-defined scoping, and it wasn't specifically the discussion about AI flows, of course, but I'm saying, a flow is a flow, a workflow is a workflow, and we see them in so many places. Business workflows, AI, That shocks. As engineers, we always try to abstract and to generalize.
But, this is something that we've… so this was the discussion back in the original OTEP, and then the, the proposal of the SIG, the original SIG, and, every time we came to the conclusion that, overgeneralizing will, will set us back, from… from actually making progress and being effective in the, SEMCON.
Liudmila Molkova 00:22:45 I think there are a couple of examples when knowing this is, let's call it workflow, that operation as a workflow helps. So, for example, you would visualize it not as a tree, not as a Gantt chart, let's say a trace, but as a graph, and you would show each workflow node as the node, rather than, When you visualize service map, you visualize services.
And I think people are experimenting with it for agents.
Does it need everything to have the workflow.prefix in front of it? Probably not. Probably there are other means. The other case is long spans and tail-based sampling. These things are long, but again, this is probably not… Not generic to workflows.
Yeah, but also…
Christophe Kamphaus 00:23:35 We are already looking into that.
Liudmila Molkova 00:23:37 Yeah, I'd also, like, as you mentioned.
building something generic enough, we would need a couple of different, maybe two, three different similar things that were, unifying before we do this, and if it ever happens, it's probably years ahead.
So I think it's pretty safe for you folks to, go stable as soon as possible. And if ever generic workflow comes, we will issue a new major version for CICD semantic conventions. We can federate them at that time, and we have pass-forward anyway.
Josh Suereth 00:24:13 Yeah, I don't think… I don't know if you've looked at all this, Kristoff, but the, the goals of Federated SEMCOMF, we should make sure that we're all on board with that, but we want to make it so that if CICD needs a major version bump.
we don't have to major version bump everything. That's one of the things we're trying to figure out. So it should be less of a scary change going forward.
Christophe Kamphaus 00:24:35 Yeah, sounds good.
Dotan Horovits 00:24:40 Which was also a good segue to the other item that you want to discuss, Christoph.
Christophe Kamphaus 00:24:45 Exactly, that was the follow-up. How would we deal with breaking changes?
And what have you… What will you put in place there? We see… with Weaver or the collector, we noticed the schema processor would be something like that?
For helping with migrating one version to another.
Josh Suereth 00:25:10 Yeah, so the schema processor never actually dealt with breaking changes. It was to make more changes non-breaking.
And so there's a set of changes that it, like, couldn't handle. So in practice, people just made giant OTTL expressions anyway.
For doing, like, A to B changes. They, like, they weren't necessarily using the schema processor. But, that doesn't answer your question. That's just, like, explaining, like.
The state of the world.
So, Weaver does have a diff cap capability, and inside of Weaver, there is a deprecation capability, where we can handle simple renames.
the theory here is that once the schema V2 is out and stabilized and everyone depends on it, those simple renames will be handled via that.
However, that's the same as schema URL today, where it kind of only handles non-breaking changes?
we haven't had a chance to do a lot of exploration with the breaking change diff, but we think that's actually where the value would be with the diff cap capability, right? Look at schema A versus schema B, come up with a set of transformations that go from A to B. From my own experimentation.
And this doesn't work for anyone who doesn't have access to AI tokens, but… I've had lots of success having AI make a static set of rules to do that transformation.
And give me, like, a translation layer.
Right? We actually, when we moved Weaver to its V2 YAML syntax.
I was able to take all the SEMCOM rego policies and translate them into V2 syntax, with an agent, with a good set of descriptions for the two schemas. So, that would be my current recommendation for something to try, since people are already using OTTL expressions.
Basically, take your… take whatever was your previous stable, take your new thing with breaking changes, and… and, like, give them a set of transformations that you can then validate.
If we can turn this into a repeatable, more strict, kind of, doesn't require token usage ever, that would be cool. If it has a little bit of token usage, but everybody gets some sort of stable, like, diff capability later, I think that's our goal, right? Of give people that translation. So that'd be the thing I'd recommend trying. Go ahead, Milla.
Liudmila Molkova 00:27:32 And there is an effort that's slightly unrelated, but also very related. Maybe, Dutton, you know about that the OpenSearch folks are proposing normalizing different Gen AI, into OpenTelemetry, shape.
And I think, Braden, one of the people working on the collector, have some interest, at least thinking about supporting, this component, and what he was… we talked to him at KubeCon, and he mentioned that he is interested in building something a little bit more generic.
Let's say you have schema 1 and Schema 2, and we have a language that maps from schema 1 to schema 2. It can be ODTL, it can be something else, but then you can, I don't know, compile it at start time, or run time, better start time, and into Go, so it's super efficient, and even if, like.
even if OTTL is too long and too hard for a certain case, then it can be short. But, it may be interesting to follow up with Braden Do you folks know Braden? Christoph Dutton?
Christophe Kamphaus 00:28:42 Yeah, I talked with him at Kuukun.
Liudmila Molkova 00:28:44 Oh, nice, right! You did. So, like, if… it would be interesting to find out where the things are.
And if he's actively looking into this, Something-to-something transformation that would be helpful here, too.
Christophe Kamphaus 00:28:59 Yeah, definitely. But I think for a CICD, that would come Whenever we would have such a breaking change.
Liudmila Molkova 00:29:08 Yeah.
Dotan Horovits 00:29:09 I think that, maybe two words about it. Just, the origin of this query came from the CICD discussion when we started talking about stabilization. We realized that, obviously, we'll need to cut at some point, to stabilize, and what will happen day after.
And we started discussing different paths, Weaver or not, and then we said, but hey, CACD is just one of the SEMCONs, the answer, or the method to approach this should be systematic across SEMCON, so this is why we wanted to bring it to the discussion here.
And it's obviously very legit that it's new to all of us, and we need to figure it out together, but just saying this is the question that shouldn't be addressed in the specific SEMCON SABSIG, but rather the, across the board. And the word about the initiative that started at OpenSearch Project around that. So, just to clarify that at least the original scope is… is slightly different. So, the original scope was because of the lack of, standardization in AI, and you have, like, the OpenLLmmetry, and this and that, and sort of, what's the way to converge that until we have everyone speaking the same language, and it started from a processor, and then rerouted to OTTL path.
But it's slightly different than addressing what you said with a much, much broader, like, schema A to schema B conversion. So, we need to verify, and if you talk to Brady, you should have the latest on that, but at least the original scope wasn't that all-inclusive, but much more limited to addressing the specific current state of affairs in the Gen AI space.
Liudmila Molkova 00:30:50 Yeah, I understand. So, it sounds like you are not blocked on this anyway right now, because you're… if you have any breaking changes, they would come… Hopefully in years.
Yeah.
Christophe Kamphaus 00:31:03 Hopefully.
Dotan Horovits 00:31:04 Yeah, I wouldn't be so optimistic, but, yeah. In the rated, things move forward.
Liudmila Molkova 00:31:11 So what is your horizon? When will be the next breaking change? Let's bet on it.
Dotan Horovits 00:31:16 I would say probably a year, but again, it's just because we see so much disruption with AI putting in new needs that the time factors are changing on what you're used to, but my guess is as good as yours, I'm not, aiming to save… hopefully to have something stable for a couple of years, I think this is the definitely… what I would say… Until a year ago, let's say? Now I'm starting to be even more cautious about that.
Liudmila Molkova 00:31:46 Yeah, just to clarify, you're cautious because of CICD, that EI will.
Dotan Horovits 00:31:50 No, no.
Liudmila Molkova 00:31:50 So, ACD enough?
Dotan Horovits 00:31:52 No, no, no, I think that just because seeing that, there's, so… the domain is… is moving so fast, around us that it's not specifically for CICD, I think the disruption. We just had in the first topic of today's agenda with, with security and, and what, agenda can mean.
wherever you put your finger on, I think you'll see that things are… so as much as we try as engineers to try and define the scope and see forward as much as we can extrapolate and things like that, I feel more humble these days in trying to extrapolate. But that's just me being… trying to be more cautious, but… Nope.
Liudmila Molkova 00:32:31 Yeah, makes sense.
Josh Suereth 00:32:34 One thing I will say for folks, like.
I do think this is an open telemetry culture thing I want to get past, but when you give yourself a requirement of remaining stable, you can make changes and adapt rapidly.
you just get more clever. And it actually is rewarding when you figure out how to add a whole bunch of crazy stuff to handle AI without breaking the whole ecosystem.
And we really, really need that creativity in our world, like, so much in OpenTelemetry. It's fine to have things be clean and pristine, but yeah, I just want to call out, I feel you, Doughton, like, I think the world is changing so quickly that it's going to be hard to adapt.
But I hope that we can rise with creativity, or assisted creativity, if you will, on how to keep the things that we had working stable and expand to adapt to new things.
At the same time. Because otherwise, you know, it's a stack of cards, right? Hopefully it doesn't all come crashing down because we changed one thing.
Dotan Horovits 00:33:38 Thumbs up on that, and that's the rule of thumb for semantic conventions in general, and specification, so, no argument, definitely.
Josh Suereth 00:33:52 Cool, so, did that answer your questions, then, for what to do here? I think these are good… good discussions, and I'm glad we're starting to come up with some… some answers for these, because this has plagued us for a while, so… cool.
Christophe Kamphaus 00:34:08 Yeah, it answers our questions. Thank you very much.
Josh Suereth 00:34:11 Alright, Ludmila, AI Usage Disclosure.
Liudmila Molkova 00:34:15 Yeah, I would like us to, update our… PR template. It's a little bit… a lot of information I'm asking for. I would like to understand the level. And the context is that I… spent some time, reviewing PR that was essentially driven Well, my estimators… 80% to 99% by AI.
And, I had my suspicions, but if I knew, it's completely… AI, I would not… Spend that much effort on it.
Honestly, and… I would love to know that people use AI, it's a good aligns with our policy, and I would love to have a sense of how much of the AI they're using. The last point… Is the consent that people should be… ready to talk about their change without AI, and this is, I copied from, Autel.io. They use this.
remark. Not sure if it will be efficient, but at least this will be… this will communicate that we expect people to know their stuff.
Whether they use AI or not.
Josh Suereth 00:35:44 So, here's a question. I mean, I think it's fine to say there's no AI, AI-assisted and bulk AI-generated, but my opinion is, it shouldn't matter how much the AI wrote, you're still responsible the same amount for the code, no matter who wrote it.
Like, I agree with the principle. I think this is a decent sign. I just… I'd be disturbed if you know how much bulk AI-generated things I have now. It's just, I… I personally feel responsible for the code, you know what I mean? Like, if that code doesn't look like I had written it, then I shouldn't send it.
Liudmila Molkova 00:36:17 Okay, so yeah, I'm kind of thinking that for the… so my, my problem is more was… AI replying to my comments, review comments than with the content of the PR.
And, this probably wouldn't help with it, so maybe… I can remove this classification and just… add a link to the Intelligent AI policy. Like, I'll reduce it, yeah.
Josh Suereth 00:36:47 Well, yeah, I guess… I just want to make sure we're answering the problem you have. Like, I agree with this is needed. I don't think people are taking this seriously and aren't owning the result of the PR, but I would… like, we should focus that. Like, this line here.
Does seem like… the most important bit. Like, if you don't have the knowledge to review what the AI generated.
and you send the PR, That's… we can prompt an AI to do the thing you were doing.
You know what I mean? You're not actually helping the project by… I guess you're spending tokens on our behalf, but still.
Yeah.
Liudmila Molkova 00:37:24 Yeah, so we can keep the last line.
And maybe I…
Josh Suereth 00:37:28 This line too, actually. Like, I think disclose that you used AI. I think, I think that, you know.
AI was used in the making of this PR. I think that's fine as well.
Because then we can basically, it gives us a signal that we need to validate the person can prompt their AI and evaluate its output.
Right.
Liudmila Molkova 00:37:52 Yeah.
Josh Suereth 00:37:53 Okay.
I was just thinking, like, these levels. I'm not sure what I would do with these levels when I reviewed them.
Liudmila Molkova 00:37:59 Well, let's remove them. Okay. It's not important.
Josh Suereth 00:38:02 Cool.
Trask 00:38:03 put in… I put in the, meeting note doc a link to our attempt in Java instrumentation, which I haven't merged, because this is a tricky area, I don't know what to do with, still.
But the… I extracted out the piece that I thought was most important to me was, have you thoroughly reviewed and understood all of the code written by AI?
Which kind of gets to Josh's… play.
Liudmila Molkova 00:38:35 Oh, yeah, we can update the contributing MD with this.
Trask 00:38:39 a… most of my PRs are AI-generated at this point, but I do… thoroughly review and understand all of the code before I… Send it.
This is the key part for me.
Josh Suereth 00:39:00 Go ahead, Doug.
Dotan Horovits 00:39:03 I'm wondering, is that phrasing that, is used currently? I have experience and knowledge necessary, is that what you, Ludmila, what you said, that is taken from, from the main OpenTelemetry I.O, or.
Liudmila Molkova 00:39:16 yeah, this is part of their PR template.
Dotan Horovits 00:39:21 Okay.
No, it makes sense to, use a consistent, phrasing. I just wonder if we want… but if it's… it appears that maybe it's less relevant, my comment, but, like, also the notion of the ownership, like, we ask the experience, the knowledge necessary to understand, review, and validate.
I think what we said here, verbally.
But it's not put in writing, it's the ownership, so it's okay if you use the AI to generate, whether to a larger extent, a lower extent. Ultimately, you're the owner. You… which… then means that you need to be, obviously, be able to comment on that, you reviewed it thoroughly, you can answer questions about it, but… so all of that comes… boils down to your… you are… when you do that, you understand that you are the owner, not the AI. Whichever way you used it is… is a tool, just like any other tool, but we wouldn't have asked that of other tools, like, did you use an IDE, or just you do it in, I don't know, VIM?
But here, where things might blur, I just spell out the ownership. I'm just raising a thought here.
Josh Suereth 00:40:28 I… I like that. That's… that's what I was trying to go after. I also really like how you phrased this here, Trask. Maybe if we do both of those changes, that would be… good, like… basically, did you use AI as part of the pull request? If yes, have you thoroughly reviewed and understand the code? And then maybe a thing that says.
I agree that I own the quality of this code.
You know, that AI generated, something like that.
Could go a long way.
Trask 00:40:59 One other topic piece of that, Leno, that I think you called out in, Chat was the… Using AI to reply to comments.
And I have… I've seen that both from people who don't know don't have the knowledge and context, and I've also seen it from people who do have the knowledge and context.
And… Honestly, I'm not a super fan of it in either case, like, it's… But, I don't know what… I don't know what I… I haven't developed a stronger feeling about that yet.
Josh Suereth 00:41:42 Oh, I, I had to… turn, like, my AI tried so hard to respond to comments when I ask it to help me, like, I just say, hey, tell me what PR comments I need to address, and it tries to actually fix them and respond to you without me actually interfering.
Just by default. So, one thing I'll say is there's also accidental AI comment addressing. That's fine.
Trask 00:42:06 Yeah, yeah.
Josh Suereth 00:42:07 Boxed it? Yeah. Anyway, go ahead, Bloodmelon, sorry.
Liudmila Molkova 00:42:09 We're not going to…
Trask 00:42:11 to ban people for this.
Liudmila Molkova 00:42:14 Right, it's just a pattern that if you're consistently using AI… I don't know how to codify or enforce it, but you can tell if response is generated by AI, usually.
At least we can explain that we don't… Encourage it, So, you.
Trask 00:42:37 I prefer that.
Liudmila Molkova 00:42:38 You wouldn't prefer AI automatically addressing review comments and replying to them.
And again, AI usage, I would encourage people to use AI. I use AI to fix my broken English, but, like, use your judgment, human judgment. If you don't have human judgment, don't send PRs.
Josh Suereth 00:43:04 The caveat is when you use GitHub Copilot.
Like, we have had some… in Weaver, we've had some successful usage where… but you know you're talking to the AI.
It's explicitly AI, it's a shared AI that we all can see what it's doing.
And understand its instructions. And one of us owns the GitHub Copilot output, generally.
Liudmila Molkova 00:43:30 Exactly, so that was my second part of the proposal. If people want to fully automate something with AI, just use the AI bot.
Josh Suereth 00:43:40 Yeah. Yeah, I agree with that. We… I think our… how do you feel about our experiments in Weaver with that so far? Like, do you think it's at the point where we could… tell people, if you want to use AI in this project, to start creating shared agent MDs, and, try to… push on using, like, a GitHub thing. I feel like that's too limiting, because it's, like, one… one company, basically.
Liudmila Molkova 00:44:06 I don't mind people using anything. Like, whatever you use, use it. If you have license, if we… if it's okay with CNCF, but it's probably… I have no idea what it takes for someone to use Claude. I would use Cloud. I would try.
Josh Suereth 00:44:21 Yes.
Dotan Horovits 00:44:22 Is there a guidance from the CNCF that we can lean into, or… I know that the discussion has been taking place on the, you know, Chris Anachak and the team, but I'm wondering if anything productive came out of that that we can, Use.
Josh Suereth 00:44:38 I don't know, Trask, do you have any updates on that?
Trask 00:44:41 So the GitHub coding agent, that's only gonna work for people with write permission to the repo?
So that's kind of limited.
As far as AI, general AI guidance from the CNCF, I haven't seen anything since a while back where it was basically fine.
But I could see, maybe, Doughton, if you know of more recent developments, it's certainly, as you said earlier, it's certainly a fast-moving area.
Josh Suereth 00:45:14 I'm pretty sure we're allowed to use it last time I checked the policy. What I meant was trying to proactively, as a project, start to share AI features, like Agent.md, Claude.md, workflows, tasks, skills, that kind of stuff.
we've started, like, with Weaver, we've started actually trying to get those markdown files in a shared spot.
So that, like, if Lyudmila's using Claude, and I'm using, you know, Gemini anti-gravity or whatever.
we can actually start trying to share some of these tasks and skills. The problem I have with, right now, sharing stuff is I think people have very highly tuned to their work environment.
AgentMD files.
And I… I use Claude, personally.
And I use anti-gravity at work.
And I've found that the same H&M NT file can work really well on one and horrible on the other.
Right?
Because of how it decides to use tokens and things. So, I don't know, like, I would love if… to Lyudmila's point, I don't want to talk to someone's AI, I would rather… or talk to someone who talks to their AI. I would rather talk directly to the AI sometimes, if I can, like, update your prompts and your instructions as a maintainer. So if you're, like, sending some submissions and doing some AI-related stuff, if you give me that workflow.
as a contribution to the project, and we can work on it together. I like this as an open exchange of ecosystems and ideas and things we're doing. And we're starting to experiment with Weaver with that.
I think we did, Weaver packages, I don't remember how much I submitted for Agent.md, but I know the README is tuned for agents to be able to, like, do validation and stuff.
I'm still wondering, like, when do we start thinking about that as, like, a meta-level contribution, right? I'm gonna contribute AI augmentation for this project that we can share and evaluate together.
Liudmila Molkova 00:47:30 I would love us to do that.
Dotan Horovits 00:47:31 Where.
Liudmila Molkova 00:47:32 Yeah, sorry, go ahead.
Dotan Horovits 00:47:34 I'm just saying that we're broadening the… I think your original question was, now we take it to the meta-level of that, so I'm just wondering if we want to separate the two questions.
Josh Suereth 00:47:45 That's fair.
I… yeah, I guess… I don't want to let perfect be the enemy of good. Ludmela, we should… I think we… you have, some good feedback on here, and I think we have some changes, minor changes that I think, but let's… let's get a PR through quickly. I… I do… would… I would love to encourage people, though, to, like.
Contribute agentic flows for everyone to share over time, so that we can collectively get better.
With these things, you know?
Trask 00:48:15 Sorry, I'm on my phone, so… and on my computer, but I dialed in on my phone, so I can't type in chat, so I'm just putting random stuff into the dock.
Liudmila Molkova 00:48:27 Trask, is it you, or is it the AI talking?
Trask 00:48:30 I wish, my voice is not, my voice is not very good today.
Josh Suereth 00:48:38 You should… you should get a fake AI camera to talk whenever you talk. I think that would be just priceless.
Trask 00:48:48 I've been dictating to AI a lot lately. I enjoy that, except for… I've been sick for a few days, and so I've actually had to go back to typing.
Josh Suereth 00:49:00 Oh, everyone I know who does that does love it. I still haven't pulled the trigger. This is… this is great. So here's some example. You have the code review agent, draft release, code review and fix, knowledge. Yeah, for context, in Weaver, I can show this quick. We… we just added…
Trask 00:49:15 from a structure perspective here, kind of the approach that I found works well is putting most of the stuff under, like, these individual knowledge articles, and then linking to those from, like, the agent's MD file, so that the agent's MD file is light, and just knows to pull in Additional context, how to pull in additional context when needed.
Yeah.
Josh Suereth 00:49:41 To help with the clod.
Trask 00:49:43 That can help with the Claude situation also, because you could just have a separate Clod ND that's just a copy-paste, more or less.
Liudmila Molkova 00:49:52 Same link, I learned.
Josh Suereth 00:49:55 That is what I've been doing with Cloud as well. You put the, what, the at symbol in Cloud.md to the other one, and yeah, it works well.
I really like this. For context, what we're trying with Weaver, we have a… our release automation is not as nice as Java's, because we can't fully automate it.
So, what we added, and I think it's still under GitHub.
We have a release agent.
That actually, goes through and manually does the process of making, making a PR with the change.
I think this also does a check… for those of you who use the, like, GitHub changelog thing that actually automatically makes a changelog.
I just… I didn't feel like wiring that in, so I just threw it in the agent script as a one-liner, and it works, so I'm pretty happy with that.
Sure, it's probably 3 times as expensive, but, you know, it was one line of markdown. Anyway, these are things that I think, you know, folks, please… If you have something like this that you use, submit, interesting.
I think we should try that knowledge thing, though, too. I really like that.
Because I think this is also useful for humans.
You're basically documenting, like, how to use your… how to use Java, OpenTelemetry Java, right?
Trask 00:51:27 All of our myriad of conventions in our repo.
Liudmila Molkova 00:51:32 How to write conventions is a perfect example. We should target agents with it, not humans anymore.
Josh Suereth 00:51:41 I feel like, you know, doing one does both, but yeah.
Liudmila Molkova 00:51:45 Yeah, yeah.
Josh Suereth 00:51:47 Cool. So, we should move on. We only have 8 minutes left for the last topic, but okay.
That all makes sense. Cool. Anything else people want to say to wrap up that one?
Okay.
Let's move on to GraphQL.
Liudmila Molkova 00:52:05 Yeah, I don't have any technical question. I'm thinking how to, and if to review this pure. I think Trasky worked with the GraphQL folks at some point.
And we do have GraphQL conventions in this repo, but they are adding some more, and I'm thinking, like.
We can let GraphQL conventions, be here.
But we also should probably have a discussion if the group is interested in hosting them.
Themselves?
Trask 00:52:44 I think they would be… I had just hesitated on pulling the trigger because I wasn't sure if, I didn't want to put them through pain if it… if we weren't quite ready.
But I haven't been following the Federation work closely, so…
Liudmila Molkova 00:53:03 So how would you feel… do they have their own repo, where they would host it?
Trask 00:53:10 I think so.
Liudmila Molkova 00:53:13 like, how would you feel if I, sent a draft PR to that repo? With demonstration?
Or to my fork, so it does not create some… Unnecessary publicity before it's needed.
And then we would, me and you, we would look at it.
And this would be a good prototype for you to approve, though, I'd have.
Trask 00:53:36 Yeah, yeah, let's do it.
Liudmila Molkova 00:53:38 Awesome.
So I'll work on the… I'll work on this this week, maybe Friday.
Josh Suereth 00:53:46 Oop, I look.
Christophe Kamphaus 00:53:47 Question here.
Josh Suereth 00:53:48 Oh, it's a beaver.
Christophe Kamphaus 00:53:49 Is there a minimum size when we should move something to federated? Because here, GraphQL I would think that's a bit like HTTP, a bit like database, It's, very… Self-contained, and Would it make sense to have a federated SAMConf when it's just 2-3 pages?
Liudmila Molkova 00:54:15 I think it's less a matter of the size, but more a matter of who should own it. There is a GraphQL group that owns GraphQL, and it's natural for them to own GraphQL semantic conventions. In the same way, like, for a .NET runtime, it makes sense for them to own their semantic conventions.
And they should be built on top of OpenTelemetry most of the time, right? There are attributes or some, I don't know, some notions that they should leverage. The naming policies, we hope they will. But they… like, it's the matter of ownership and an existing group that would be the best candidate to own it.
But also, I don't think we have a strategy to move everything out.
yet. It's more like, if something new comes in.
The first, idea would be that it probably should be outside, if it's specific to some technology.
If there is… several things in OpenTelemetry that would depend on these conventions.
it would make sense to host them somewhere in OpenTelemetry.
Josh Suereth 00:55:34 I'll also throw out that if we had had federation as a capability when HTTP was stabilized, I think it would have made sense for us to have that as a separate federated thing, to build it there, stabilize it there, and then bring it in the core. Like, if this federation thing is gonna be successful.
It should have been something we could have done with HTTP in the past.
That is… sorry for non-native English speakers, I just used a lot of weird… Grammar, but anyway. But you get what I'm saying, like, if this is gonna work.
and it wouldn't have worked for HTTP. It means that the plan is bad. But I think it could have, and I think that's what we're trying to build. So, like, a new thing like HTTP comes in, we actually want to give it an incubating area where it can rapidly grow.
Where it can go through a breaking change if it needs, without impacting all of CEMCOV.
And then, once that thing is considered stable, we can bring it into core, and that's where it hits the, you know, this, this does not change.
level.
Christophe Kamphaus 00:56:41 Yeah, to make this distinction a bit clearer.
Josh Suereth 00:56:44 Yeah, yeah, yeah.
Christophe Kamphaus 00:56:47 Yeah, that's a great vision.
Liudmila Molkova 00:56:55 Awesome.
Josh Suereth 00:56:57 I think that's it. Great discussion, everybody.
Anything else before we call it?
Didn't it?
Liudmila Molkova 00:57:09 Didn't do any trash.
Josh Suereth 00:57:11 I know. Should I do with you?
Liudmila Molkova 00:57:13 Let's try.
Josh Suereth 00:57:15 Okay.
Give me a sec to get… oh, man.
Come on, length.
I need to close a few Chrome tabs quick, so that I have RAM again. Okay, we're good.
Do we… do we, go through blocked quick?
I'm gonna stay here. Add CPU metrics for Kate's pods, and containers. Do we know why this one's blocked?
Liudmila Molkova 00:58:05 Oh, I moved it to blocked, but I… I have no memories of why. It probably was not a good idea.
Or maybe I made a mistake.
Josh Suereth 00:58:19 Can we split this into smaller standalone PRs? And then, it looks like it was split, but kept for a few?
I don't know, you took some action here… Three weeks ago.
Liudmila Molkova 00:58:35 It might have been… Cat on my keyboard.
Because I have no memory of doing it.
Let me… OPR on hold, so the first topmost thing, that's why.
We are on top.
Josh Suereth 00:58:51 We're blocked on this, okay.
DJab, yeah.
Trask 00:58:55 I like the idea that cat walked on my keyboard as the new, my dog ate my homework.
Josh Suereth 00:59:06 I don't know if you can see, but my cat is, like, sitting on my hand while I type. It's really frustrating.
Anyway… Okay.
So, next is process executable to its own entity.
This one… Got blocked by Braden, right.
Her name and path being separate things.
It's intended to block merging.
Path is identifying… I'm processing.
Make the EFTL match.
Okay, this is about the… the path of the executable doesn't necessarily identify the process.
That's a fun one.
I think this is still blocked.
Looks like it's not resolved. Okay, cool.
So nothing to do there.
And then we'll check the last one. Invoke agent server span. Is this one still blocked?
Liudmila Molkova 01:00:21 Yeah, this one is blocked. We want the PR router and Kip to do a little bit of research.
Got it.
just not clear if we need a service pen. This is in the GenAI discussions.
Josh Suereth 01:00:38 Okay.
Cool.
Alright. Well, we can't make progress on blocked PRs, and I think we're out of time. So, thanks everybody. We'll see you all next week.
Christophe Kamphaus 01:00:50 See you.
Liudmila Molkova 01:00:50 Thank you.
Trask 01:00:51 baby.
