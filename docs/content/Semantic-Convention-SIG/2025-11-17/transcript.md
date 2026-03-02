SIG: Semantic Convention SIG
Date: 2025-11-17
Duration: 35 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 03:21 Hi, everyone!
**Christophe Kamphaus** 03:27 Hello?
**Trask Stalnaker** 03:28 Hey, wow, that's quite a view. Where is my camera?
**Liudmila Molkova** 03:34 Nice cup.
**Trask Stalnaker** 03:58 Believe it's… My turn to drive.
**Liudmila Molkova** 04:04 Oh, thank you.
**Trask Stalnaker** 04:40 This document is getting… Slow…
There, it's loaded. I learned a trick from, pablo, that if you move…
You can archive, into a separate tab, and that will speed it up.
You don't have to archive it to a whole separate dock.
**Liudmila Molkova** 05:08 Cool, I… I can do this in the background.
**Trask Stalnaker** 05:16 Cool.
**Armin (Dynatrace)** 05:17 419 pages, really.
**Trask Stalnaker** 05:30 Alright, let's go to the triage board.
start with, these mostly look the same. Now, the… Details… I think I had…
Invited the browser full.
I think I added it to their…
13… 12… So…
I added it, but, I didn't attend the meeting and don't know what the outcome was there, so I will ping them again.
This was the one, right? Let's see…
Oh, no, no, this was a different topic. Entirely.
**Liudmila Molkova** 06:58 I think we're res… Doved it.
**Trask Stalnaker** 07:02 Oh, did we? This one?
**Liudmila Molkova** 07:04 Oh, the app, no, no, no, no, this one, no, yeah.
**Trask Stalnaker** 07:07 This one. Okay.
Yes, yes. I'm pretty sure this one… was… Is rejected by the… Client. SIG.
Will it… Oh, well, it won't time out, it won't auto-close if… It continues to be active.
Locked.
prettier…
**Liudmila Molkova** 08:41 I would like… we probably, can have a discussion here, but I…
I think it's useful to enforce a certain label, a certain list.
symbol, or a certain italic symbol, and I don't think it's useful to enforce it.
I have never heard of any problems that… and Patrese confirmed they don't have any problems on up until Emmetry.io, because we don't follow certain…
syntaxes, and I think that enforcing it would bring more harm than good.
**Trask Stalnaker** 09:24 So, the only one that I have a preference for is the list items, is the dashes, but the…
The italics, the underscores, at least…
Yeah, I don't think we should enforce the italics, because in… I generally prefer underscores, but in some cases, we use underscores, and then it ends up looking really
Weird, confusing.
And… What is… Part of this, also, there was another PR that would…
Why is it this is only two changes?
This would also rap… word wrap, right?
I thought there was another PR that had a lot of… Wrapping…
Oh, was it really only these two things?
**Liudmila Molkova** 10:36 Bye.
think so? I'm not sure. Maybe there is something new. There was some… PR, da-da-da-da-lint as well.
But I don't remember the number.
**Trask Stalnaker** 11:56 Alright, switching Iskorless to…
So, as I said, this is actually a… I support this preference, but… It's also not important.
**Liudmila Molkova** 12:20 I'm curious why.
How is it helpful?
**Trask Stalnaker** 12:24 I'm used to it. I think probably from the, I, I don't…
I'm not sure I would enforce it, but I don't… yeah, I don't know, it's weird.
Like, I can… Definitely not gonna fight for it.
**Liudmila Molkova** 12:47 Me neither, so I want… what I'm fighting against is a flood.
**Trask Stalnaker** 12:52 Lots of PRs.
**Liudmila Molkova** 12:54 Not of useful… super useful peers.
Thank you.
**Trask Stalnaker** 14:11 Browser resource timing event…
So this does not look locked, so…
I'm gonna move it to… awaiting code owner approvals.
By the way, we… Pretty light agenda, so let's spend a little bit more… time triaging…
Check collision for metric names.
**Liudmila Molkova** 15:03 Oh, I think we talked about it last time. Isn't Alexandra here?
Oh, maybe it's ready to be merged, or ready for another round of review. Let's see.
**Trask Stalnaker** 15:52 Sign areas with code owners… oh yes, I left a comment. Okay, so…
**Liudmila Molkova** 15:58 Just…
**Trask Stalnaker** 15:59 Neat.
Let's follow up there… This is an easy one…
What did we do?
Okay, I can… I think I can fix this…
V1…
**Liudmila Molkova** 18:03 Oh, you're actually reviewing it, wow.
**Trask Stalnaker** 18:08 Wow.
Figure and call that review, but yes, I did scroll through it.
Alright…
And we've got, yes, our never-ending list of untriaged. Okay.
**Liudmila Molkova** 18:34 Did they just close the rate, PR? That one is blocked, 2294?
**Trask Stalnaker** 18:42 Right. Oh, yes, we… yeah, that's a good idea.
What is our normal… Response there for… There's not an active SIG…
**Liudmila Molkova** 19:13 I can leave a comment, I can copy it over from any of the PRs that were closed.
**Trask Stalnaker** 19:19 Cool, thanks.
Cool. Well, let's, go to… Christoph.
Unified Workflow Conventions.
**Christophe Kamphaus** 19:53 Yes.
We discussed it in the last CICDSIC.
And we wanted to come back to the general SUMCONF with a few questions.
initially in SICK1, in the Phase 1 of the CIDC, when we came up with the initial attributes.
We thought about unifying the workflows, pipelines, and so on, but at the time, It was sought.
Maybe it's better if we start out with CICD and generalize later.
And we are now at that point. So, the question is, what would be the best way to proceed?
**Liudmila Molkova** 20:37 Why do you want to do this?
**Trask Stalnaker** 20:42 Do you want to generalize? Yeah.
**Christophe Kamphaus** 20:44 Yeah, because we sought, the concept of a workflow
is similar for CICD pipelines, as well as other task engines.
So it might make sense to generalize some.
**Trask Stalnaker** 21:02 The problem is that for us to generalize, we need, like, oh, we need a new…
We need a working group, a SIG, we need, multiple… implementations.
just to CICD.
So, I would say, if you want to pursue this, you would need to make a community proposal for a new SIG, and kind of scope that out, and…
Find people and implementation areas that are not CICD.
**Christophe Kamphaus** 21:45 Okay, yep.
**Liudmila Molkova** 21:48 If, if you'd like… oh, go ahead, sorry.
**Christophe Kamphaus** 21:50 And if we invite those people from the other areas to CICD, and we Take it.
Under our area.
Would that work as well?
**Trask Stalnaker** 22:05 I think I would ask, then, that you change the CICD SIG to be the workflow SIG, because…
I mean… Workflow is a… bigger…
area, right? I don't want to just lump it under CICD, SIG, like, because I feel like
It will get… Too much of a, bias.
towards CICD workflows.
Opposed to solving the general workflow.
problem.
**Christophe Kamphaus** 22:38 Makes sense. In the current proposal, it's heavily based on the CICD,
some conversations. Yeah, we would need to have more input.
**Trask Stalnaker** 22:49 Yeah, and given, I mean, I would… I would
My personal suggestion would be to go ahead and stabilize CICD workflows.
as your V1, because with the new, sort of, focus within OpenTelemetry of stabilizing what we have already.
There's going to be more scrutiny and pushback on spinning up new things.
**Christophe Kamphaus** 23:21 Like, a workflow, a semconfig?
**Trask Stalnaker** 23:26 And then, you know, there can always be V2 two years from now that generalizes things if that
evolves naturally.
**Christophe Kamphaus** 23:38 Yeah, that was also a thought we had.
If we now started working on workflow semantic conventions.
which that prevent us from stabilizing our current SAMconf in CICD.
**Liudmila Molkova** 23:54 I don't think we should be blocking on this. I also don't think that there is a lot of intersection between AI agent workflow and CI-CD pipeline, to be fair. So, even if there is some small intersection, it might be too, like, a few attributes.
**Christophe Kamphaus** 24:12 Okay.
**Liudmila Molkova** 24:13 I… I would…
I would not consider this unification to be blocking, but maybe some… the future of some conf, this major version bump would unify the…
And by the future, I mean, like, distant future. I don't think, like, we would be… we would… like, the benefit of unifying would be big enough to justify just this to be the reason for the breaking change.
**Trask Stalnaker** 24:47 So, in the… yeah, that's a good… Question…
Since that was one of the motivating… motivations here.
It sounds like from the… the… Gen AI… SIG that…
I mean, yeah, we would want…
That… those folks to be on board with that, and that…
So if people are… I don't think there's that… I mean, as far as benefit to… I mean, I think CICD is such a big area, and Gen AI is such a big area.
But I don't think there's… Much harm in having those workflows.
Separate and targeted to those areas.
where I could see a workflow.
A general workflow thing would be more like a business process workflow engine…
These kinds of very generalized tools that are for any kinds of workflows, and that…
You're kind of have to… There could be some benefit there.
I'm trying to think from a dashboarding and alerting perspective, like, would you really…
treat your AI agents and your CI-CD workflow the same.
Because that's kind of the… the… would be one of the arguments for… unifying those.
**Christophe Kamphaus** 26:21 Yeah, we had Komunda BPM, also as an example for workflows.
**Liudmila Molkova** 26:32 I quit sitting.
**Christophe Kamphaus** 26:33 Cases where one would, call into one of the other types of, systems.
If you wanted to then have it unified, Might make sense.
**Liudmila Molkova** 26:48 It might. There are also something I learned… I've heard of, but I need to learn more, that Cloudflare, they instrumented their runtime, and their workers and jobs produce something today.
It would be interesting to take a look, it's just a general… job processing.
thing, and definitely there is some merit to defining conventions for it. This discussion reminds me of the operation name thing we have everywhere.
our operation name and database, in Gen AI, in messaging, and we tried hard to…
Find good reasons to unify those.
And this unification turned out to be… well, it raised more questions than answers.
We stabilize database without it, and we would stabilize…
probably other conventions without this unification, but we… I don't feel like we're completely closing the door for it in the future.
**Christophe Kamphaus** 27:53 Okay.
Yeah, makes sense.
Yeah, I guess I can, take that.
Back to CICD.
**Liudmila Molkova** 28:09 But if you would like to pursue it, it would be wonderful if you
like, take the… if you want to investigate what Cloudflare did, it would be interesting, or if there are people who are investigating things for GenAI agent workflow.
We don't have any consensus there yet. So if you want to, learn more, there are…
There are people to talk to.
**Christophe Kamphaus** 28:40 That's good to know.
**Liudmila Molkova** 28:43 I'll bring it up in the Gen AI call tomorrow, and we'll just… just check if people have any appetite for it.
**Christophe Kamphaus** 28:50 Yeah, that would be great.
**Liudmila Molkova** 28:53 Thank you.
**Christophe Kamphaus** 28:56 Thank you as well.
**Trask Stalnaker** 29:00 Cool, anything anyone else wants to… Raise today.
We have hit the end of our agenda.
**Michele Mancioppi** 29:13 Having a hard time representing in the…
Semantic conventions, the service.peer.name and namespace.
Specifically, I cannot figure out from the… documentation.
How to generate these snippets.
**Liudmila Molkova** 29:41 So, you… do we have service.peer? Is this… would be a new group?
**Michele Mancioppi** 29:48 Yeah, I have it in the registry YAML as a how-to-it group.
I added, in the common YAML, this thing?
I do not understand how the common YAML and registry YAML fit together.
I cannot figure it out.
And I don't know how to reference this from here.
**Liudmila Molkova** 30:14 So this is generated if you do… Make table generation.
**Michele Mancioppi** 30:24 Alright, that's fine.
Oh, wow. I think it took back, it works.
Fantastic.
**Liudmila Molkova** 30:32 Yeah, and there is another one, so normally you would run table generation and…
space register generation to two targets at once, so that it's
Oh, sorry, table… space, I meant the space.
**Trask Stalnaker** 30:47 bar.
**Liudmila Molkova** 30:49 registry.
It would also generate the new… Attributes… yeah, the service.md.
It's just the registry that attributes documentation.
**Michele Mancioppi** 31:13 And, is there a way that…
Hey, if I recall correct from Josh.
He said there is no way to say an attribute group, to which signals
It, it applies, right?
**Liudmila Molkova** 31:28 No, we… today we just documented and marked down, so you can, have something just in a pure text saying what… what you want, and hopefully, eventually, we…
**Michele Mancioppi** 31:38 We will be able to…
**Liudmila Molkova** 31:40 Document.
The public groups formally.
**Michele Mancioppi** 31:42 We could do this, for example, in this document, right?
Like, here.
**Liudmila Molkova** 31:48 Yeah, you cannot change the one that's in the registry, but here you could write Anything you want.
**Michele Mancioppi** 32:11 All right, then, expect APR very soon. Thank you.
**Liudmila Molkova** 32:16 Thanks.
By the way, I don't think you should limit the signals. Like, why wouldn't somebody use these attributes on events, if it makes sense for them?
**Michele Mancioppi** 32:27 I cannot figure out a use case why anybody would use this in profiles and logs.
Metrics makes perfect sense for connection metrics.
Spans, sure, naturally.
Yeah, okay.
And it's, it's… it's…
**Liudmila Molkova** 32:47 I think the principle, is it harmful?
If it's harmful, then you shouldn't. If it's not harmful, then…
**Michele Mancioppi** 32:53 Define heartfelt.
**Liudmila Molkova** 32:56 Hi, Crystonelli.
**Michele Mancioppi** 32:57 confusion, like… Okay, but for example, like, in a profile, when you go inside service.
What would that mean?
**Liudmila Molkova** 33:07 It depends on the semantic of the event, right?
**Michele Mancioppi** 33:12 Okay, well, I will just not add it.
the, so we end up with those.
As a proposal to replace the peer.service.
Doesn't mean we mark period the surface as deprecated.
**Liudmila Molkova** 33:32 I don't see a big reason not to. We had a discussion in the past that it might melt the world, but since it's up in nature.
I think it's… it wouldn't do much harm, actually.
**Michele Mancioppi** 33:49 To deprecated, you mean?
**Liudmila Molkova** 33:50 Yeah.
**Michele Mancioppi** 33:52 Okay, I'll make that in the PR as well.
Cool.
**Liudmila Molkova** 33:56 Thank you.
Nice, so when you do this, you can list the deprecation
A reason renamed, and you mentioned the new attribute name.
It's just the tool length.
**Michele Mancioppi** 34:08 Technically, it's under the name. It's under a name, technically.
I mean, it could… well, peer.service yesterday would be service.peer.name.
Yeah, okay.
Okay.
Alert.
**Liudmila Molkova** 34:25 Cool, thank you.
**Trask Stalnaker** 34:35 Alright.
Last call for topics.
Then, see you all next week!
**Liudmila Molkova** 34:51 Thank you.
**Christophe Kamphaus** 34:51 Leo.
**Armin (Dynatrace)** 34:52 Oops, bye.
