SIG: CI/CD SemConv SIG
Date: 2026-04-07
Duration: 49 minutes
============================================================

## Zoom Recording Transcript

**Adriel Perkins** 02:28 Good day.
**Christophe** 02:31 Hello?
Can you hear me?
**Adriel Perkins** 02:34 Yes.
Sure can.
**Christophe** 02:39 Alright.
**Adriel Perkins** 02:41 I'm gonna be on mobile, for a bit, so if you would be willing to drive the meeting, I'd appreciate that.
I'm sorry I didn't show up yesterday. I completely forgot about it, and it wasn't on my work calendar.
I work out.
**Christophe** 02:54 Problem.
**Adriel Perkins** 02:55 A little bit overloaded.
**Christophe** 02:58 We discussed everything, and… The good news is, we can go ahead and… Move towards release candidate.
**Adriel Perkins** 03:07 Awesome. What did they say about the, standardization concern for, common, a unified workflow semantics?
**Christophe** 03:18 Yeah, is that… They don't think it's worth it to wait for it. We should go ahead right now with what we have.
**Adriel Perkins** 03:28 Okay.
So, just, like, if that ever happens in the future, we'll just do a breaking change and communicate that, and say, like, hey, you know, these have been the conventions, now adopt these.
Is that the intent?
**Christophe** 03:39 Okay. So we would have a version 2 of the CICD conventions.
And actually, that's one point that they are working on.
At the moment.
How can individual SIGs or conventions have breaking changes in the future?
And, Sarah's work with Reaver is, what they are working on.
**Adriel Perkins** 04:03 Okay. Yeah, we're just becoming a really awesome technology, so it's good to hear.
**Christophe** 04:08 Yep.
And actually, the schema processor that you Noted down the link.
**Adriel Perkins** 04:15 Yeah.
**Christophe** 04:16 It works, but only for renames.
Not all the time for all changes.
**Adriel Perkins** 04:22 Okay.
**Christophe** 04:23 And for that, people are using OTTL at the moment.
If they want to perform, Migrations between schemas.
But it's not… it's a manual process.
**Adriel Perkins** 04:39 Done.
**Christophe** 04:40 So they hope that with Weaver.
They might have a better solution in the future.
Potentially also something that they could… Compile into native code to have better performance.
**Adriel Perkins** 04:55 Yeah, okay.
**Christophe** 04:56 But yeah, that's a solution that's, That would be solved in SamConf or in Weaver.
We don't need to care for… about it at the moment.
**Adriel Perkins** 05:08 Okay.
**Christophe** 05:20 So yeah, I think we can go ahead and open a PR.
mark the CICD conventions as release candidate.
**Adriel Perkins** 05:29 Okay.
**Christophe** 05:32 There is one open PR at the moment, where It was for the issue I highlighted for clarification.
Yeah, I don't have, I'm not at my laptop, so I cannot share my screen.
**Adriel Perkins** 05:54 Okay, no worries.
Is that a pull request that needs to get merged first?
**Christophe** 06:01 It's just a description update, so… Probably it would be fine to still update it after we mark it as release candidate, but maybe… Let's merge that one first.
**Adriel Perkins** 06:13 Oh, God.
For stabilization, do they want stabilization of the attributes on the registry as well, or just the conventions around spans and events that are inside of CICD? Does that make sense?
Because, like, we have, so as an example, like, we've got, like, there's VCS attributes, and I think they have their own stabilization that are separate from, like, the… Information around the… Event type, or the signal type, rather.
So I assume that when we stabilize our release candidate, we'll say, like, alright, we're stand… we're… we're doing the VCS attributes and the VCS metric convention as an example, and that would be one stabilization, then another one would be stabilizing CICD, Attributes and CICD span conventions.
**Christophe** 07:20 I'm not sure I got it. You mean that our SIC is taking care also of the VCS conventions?
So we would auto-stabilize those.
**Adriel Perkins** 07:33 Yeah, I mean, we wrote them.
And they are part of the CICD semantic conventions.
**Christophe** 07:42 No, sweetie.
**Adriel Perkins** 07:42 But, like, we've also got… If…
**Christophe** 07:44 We stabilize any metrics or spans that… use them to also stabilize attributes for VCS.
**Adriel Perkins** 07:56 Yeah, we do have that in that page, the metrics.
I'm just thinking, like, too, in addition, like, we've got ones that are in the attribute registry that have had a long life that, like, we haven't, like, clearly… Written any type of event for, as an example?
So the example I'm thinking about is the artifact one.
and tests, right? Like, those are… have been part of the CICD semantic convention working group, so to speak, because we put them in there. They were part of the initial thing, and they've… We've not, like, done, like, this is what a test event looks like, or this is what an artifact event looks like, but we have had the attributes in the registry for a long time. So, are we ignoring those?
**Christophe** 08:46 Okay, I think I get what you, what you're getting on. So, you say we have these attributes in the registry for which we don't have any signals defined. So, no spins, no events, no metrics.
Yes. Yeah.
Yeah, I think the idea in some conf is that the registry You shouldn't directly go to the registry.
It should be used in some higher level signal definition.
**Adriel Perkins** 09:18 Hmm, interesting.
**Christophe** 09:20 So yeah, I think it's better if we stabilize only those attributes and signals.
Where we actually defined a convention, like spans or metric.
**Adriel Perkins** 09:32 So then we probably need to start working on some of those other conventions then, too.
Since they've kind of been held off for a while.
**Christophe** 09:40 Yeah, I think it makes sense to, to do that.
**Adriel Perkins** 09:43 Yeah. Okay.
That was helpful. So, at least the VCS, conventions, like the registry attributes, and then the conventions for the metrics, and then the spans are gonna be stabilized for CICD.
And those attributes. Cool.
Cool, cool, cool, cool Do we need to open up new issues on the board to track that and link back to?
**Christophe** 10:07 I think we have some on the board to work on the… on some of them?
Oh no, it's add incident attributes… Oh, yeah, I think I… Yeah, we should add issues to… write conventions using the tests and deployment attributes.
**Adriel Perkins** 10:32 Okay. And then tasks for the… we were gonna move the stabilization… to release candidate.
**Christophe** 10:41 Yeah, a task to, okay. To go to release candidates.
**Adriel Perkins** 10:47 Okay.
Okie dokie.
That sounds good.
**Christophe** 10:55 And once we… Do merge the PR for release candidate.
I think Hugh and Totan are working on a blog post.
**Adriel Perkins** 11:05 Yeah, yeah, yeah.
**Christophe** 11:07 Yeah, to water.
**Adriel Perkins** 11:08 Change how we're working on it, but yeah.
We'll, probably include you on it, too.
I think we should.
Yeah, I gotta find the dock, I don't know, I reviewed it and commented on it a long time ago, but it's gonna have to change with this release, so…
**Christophe** 11:32 Cool.
Yeah, I don't have any other topic from my side.
**Adriel Perkins** 11:42 Okay.
Cool.
Cool, cool, cool. Alright, I don't think I have, anything, either. I've just been… Trying to get caught up.
It's been a little bit hard, too, as of late, so… Try to get back into the swing of things, and… Get… get more active.
Than just the meetings.
**Christophe** 12:14 I know how it is.
**Adriel Perkins** 12:18 Man.
Happens sometimes. Still got some collector work to do. But, oh, I guess we will probably need an issue then, too, for… Adopting the stable conventions and the collector once they're there.
**Christophe** 12:36 So, what would need to be done?
Because the actual conventions don't change, it's just changing the package import and the documentation around it?
**Adriel Perkins** 12:50 Yeah, I think, so there is a, inside… because I guess… So when you stabilize, you'll release a new version, and as that new version comes out, that's the version that will have these stable conventions.
So we'll have to update the package for which we pull conventions from to make sure that it's up-to-date with the stable.
And then, we'll probably want to mark the… Collector component itself.
as… stable.
Which… Probably.
That one will be interesting. I'm gonna have to do a little bit of work before I market a stable, I think, because there's a… Couple issues that I think still exist.
And they are… oh.
In our semantic conventions for CICD spans, do we talk about Q spans?
**Christophe** 13:47 I think we have it as part of, the face.
If I remember right.
**Adriel Perkins** 13:54 Okay, did we update that based off of the latest learnings for the GitHub receiver?
Maybe.
**Christophe** 14:03 There haven't been any changes in a long time, so… Probably not.
**Adriel Perkins** 14:08 Okay.
We'll need to review that. It actually might be that a GitHub receiver implementation was incorrect.
And didn't match the spec.
I gotta go back and look and remember.
But the Q-SPAN behavior was not what, Was not aligned with general tracing behavior and what it should have been.
And I… I fixed it. Well, somebody else published it, and I nerged it.
But I don't know if… It matches our CIC spec.
So that's what we'll have to check.
**Christophe** 14:57 Yeah, and when you move the collector to stabilize it.
Would you go in, one step directly to stable, or are there intermediate?
Stability levels, like, release candidates there as well.
**Adriel Perkins** 15:15 Yeah, there's a… there's a, like, alpha-beta stable.
And I think we're in… Beta right now?
I think we're in beta right now, but I'll check. We're either in alpha or beta, In fact, I just got back to my computer, so let me just check while I'm here.
**Christophe** 15:39 Yeah, I'm thinking we shouldn't directly go to stable until… the CICD conventions are actually stable, so… Maybe move up one level, now that we are a release candidate, but not yet stable.
**Adriel Perkins** 15:54 Got it, yeah, so metrics is alpha, Traces are beta, so what I will… or our development, rather. So, what I'll do is I'll make a PR to move traces to alpha and metrics to beta.
**Christophe** 16:12 Sounds good.
**Adriel Perkins** 16:15 Alright, so let me just… I don't know, put a note somewhere, let me go pull up the doc.
Oh, goodness.
All you have to do is go to the link to get it. You just hit start, or if you want the code. It's playing?
Functionalities within this.
Alright, there we go. Sounds like a video playing in the background.
Okay, where would I?
So I'll just update these.
We're gonna separate… We're gonna separate CI-CD from VCS metrics, right? We're gonna separate the, basically, the span stabilization and the metric stabilization.
**Christophe** 18:01 Between, CICD and VCS.
**Adriel Perkins** 18:04 Yeah.
**Christophe** 18:05 You know.
Do you also mean to separate Spanner metrics, conventions.
Stabilization for… inside CICD itself.
**Adriel Perkins** 18:25 Let's see, let me pull up the, If we go to CICD, we've got span… oh, we've got logs, too, actually.
**Christophe** 18:45 Not really, there's not much on the locks.
It just says, to use.
the NTTs.
**Adriel Perkins** 18:54 Okay.
**Christophe** 18:56 But I guess we can also mark that as release candidate.
**Adriel Perkins** 18:59 Okay.
So, probably the way I would group it is… one release candidate for spans, for CICD spans, which includes.
**Christophe** 19:19 like…
**Adriel Perkins** 19:21 Basically, the majority of these… CICD registry. I don't know if it includes all, but it includes most.
And so, on that line, whatever's in the registry that it includes, I would probably say, like, include that as stabilization, too.
I was like, if we go to CICD… Yeah. And then… Or… metrics.
I do one for metrics, which also includes CICD, but it also includes VCS metrics, so I'd probably… I don't know. In the effort of making pull requests small, I would probably do one for CICD metrics, and then one for VCS metrics.
**Christophe** 20:09 Okay, so one CICD span, one CICD metric, and one PCS metric.
Yep, makes sense.
**Adriel Perkins** 20:22 One item for CSCE metric plus attributes.
One item for CS… Vcs metric plus… Sugars.
And then we just have to validate that all… attributes are, from… registry and CIC and BCS are covered.
by the respective signal. And then I guess you said one for… one item for logs, too?
**Christophe** 20:56 Yes, it's just marking the document itself as release candidate, but there's no conventions on it.
**Adriel Perkins** 21:03 Got it, okay.
Okay.
Alright, got that noted down.
Perfect.
Cool, cool, cool.
And then I'll check the… Let's see… oops.
Oops.
Oh, so there is no queue.
On the side of the CICD Spring Convention.
**Christophe** 22:00 We have the pipeline run state.
So, pending, if it's in pending, that's basically, it's being… it's still in the queue.
**Adriel Perkins** 22:35 So… I don't see that on the semantic conventions, though.
**Christophe** 22:44 If you go to the metric, run duration, You have the attribute, CICD pipeline runs state.
**Adriel Perkins** 22:55 Oh, it's on the metric, not the span?
**Christophe** 23:02 Let me take a look at the span… Yeah, I don't think we have… Any span convention defined for the queue.
**Adriel Perkins** 23:22 So, that might be something we want to evaluate before we move forward, actually.
Because in the GitHub receiver, what we ended up doing… Whoa.
Oh, no.
Okay, Google's… GitHub's just having issues, again.
**Christophe** 23:44 Oh, you have the unicorn.
**Adriel Perkins** 23:46 Yeah, really.
True.
So we have a dedicated… inside of GitHub Receiver, we spawn a dedicated Q-SPAN.
So where you have your, like, general pipeline, and then you have, like, a queue time that you… which is, and then it's got a bunch of sibling spans. And so that way you can understand the distribution of that. That was heavily requested by the community for that. And then if we do, label… Let me just close that. Label. Receiver, GitHub.
Oh, man, we have a lot of issues open.
**Christophe** 24:33 Are you sharing your screen?
**Adriel Perkins** 24:35 Oh, no, I'm sorry, I'm not even on the Zoom call, and… Let me swap devices one moment.
**Adriel Perkins** 25:02 Okay, can you hear me?
**Christophe** 25:06 Yes, I can.
**Adriel Perkins** 25:08 Alright, cool.
Hmm.
So… Yeah.
So, we originally had… It's easy, sir.
Yeah, so this was, heavily requested, but we have, like, this is your… Main pipeline run.
And then you have a Q span, and then the Q span has a bunch of siblings. This is… improperly… Those should have been…
**Christophe** 26:24 sibling spends.
**Adriel Perkins** 26:26 Yeah.
Yeah. So, we originally had it like this, But then the… Nope, not it. Hold on.
Where is that one comment? There was a really good comment. This is not the only… oh, yeah, okay, this is it. So, someone from Moneycomb mentioned.
that, our spans were children of Q, but they should have been siblings of Q, and so that aligns more with the Span conventions.
So we did fix that.
And so now it's like, instead of… yeah, it actually looks like this, right?
Like, the queue, and then set up, set up, set up. But then they're also requesting execs fans.
To where you have a Q span, and then an exec span, and this exec span is a… does have the spans of children, and that way you can clearly calculate the execs, like, how long it was in job queue, and how long it was in exec queue, and derive them from the traces.
So, I don't know if… I feel like we should make sure that, like, our CIC before we stabilize them, because otherwise the GitHub receiver is just gonna continue to drift between the two.
And people are gonna say, well, like, I wanna see my spans like this, or this matches, like, the conventions better.
And then we're just gonna kind of miss out.
We also have a little bit more… I mean, we do have some more attributes, like the GitHub-specific ones, which is fine, but… That doesn't really affect stabilization, but I do think we should probably make sure that this is captured.
And whether or not we want execJob to be something that's captured in the semantic conventions.
**Christophe** 28:22 Yeah, basically, we don't have a convention for Q or exec.
**Adriel Perkins** 28:29 Yep.
**Christophe** 28:30 on those funds.
And that would be something matching the… Duration metrics, the different phases.
Pending and executing.
**Adriel Perkins** 28:47 Right. But without, like, without having clearly defined spans or attributes, it makes those metrics a lot harder to derive and, Calculate.
**Christophe** 29:04 Yeah, so… Ideally, we should be able to have a spam processor to derive The metrics from it.
**Adriel Perkins** 29:19 Right, but we wouldn't be able to… So, in queue, we would not be able to write a span processor that was able to detect that based off of the attributes that are in the span set today.
**Christophe** 29:33 Yeah.
**Adriel Perkins** 29:39 We would only be able to… into a guitar.
**Christophe** 29:42 Collector, how it is currently.
You would, you could only distinguish the different types.
Based on the spam name? Or do you also have attributes.
**Adriel Perkins** 30:08 I mean, we have a ton of attributes, but we figure out which one's the one that we want to look at.
**Christophe** 30:20 The spend for the queue.
**Adriel Perkins** 30:31 It's gonna be in the advent handler.
So I've got handle workflow run.
Which we'll look at that in a minute.
The handle workflow job.
And then in Workflow Job, we… Job queue span.
Oh, I jumped to definition in Google.
Which… does have the span name of Q-jobname.
And yeah, so it gets set as a spam name. It's internal.
The parent span is the main parent, and so it is a sibling now.
And then the…
**Christophe** 31:23 I see you have C. pipeline run queue duration as an attribute.
It's the attributes put double.
That's the very end.
**Adriel Perkins** 31:39 Oh, yeah, I read that far ahead. Yes. So we do add that CICD pipeline run cue duration as a double.
**Christophe** 31:51 Does that make sense? Because… Wouldn't it already be?
Part of the spend duration.
**Adriel Perkins** 32:12 I don't know.
Do we have anything in here for that?
Or was that… I might have made that up.
I don't think we ever…
**Christophe** 32:25 attribute for it.
**Adriel Perkins** 32:27 You're right.
**Christophe** 32:29 It's more… it basically duplicates the spend duration as an attribute.
**Adriel Perkins** 32:35 Yeah, okay, yep, agreed. This should probably be span duration, and… but there should be a secondary attribute that says this is of type Q, right?
**Christophe** 32:47 Yeah. We are getting here to… It's a problem of… How do you identify the type of a spam?
And it's a recurring issue in some conf.
**Adriel Perkins** 33:05 fair.
**Christophe** 33:11 It's… it's not documented anywhere.
Right. It's just, currently… Spans don't really have a… Type.
It's implicit by the name of the span and the attributes that are set on it.
**Adriel Perkins** 33:33 Right. So, I mean, I… so, I guess for… for the implicit portion of this, the way you would determine if it's a Q span would be, one, the name has Q prepended to it.
So that's obvious. And the GitHub receiver. The duration should be not queue duration, but span duration. And then there should be an attribute that says CICD pipeline.
Running state or something, or maybe it's just the state one that says queued.
Right? And then you can… between those three things, you can tell, okay, this span was a Q span, and if I want to calculate the exact time out of my parent span, I could say total time minus queue time.
Right? Total span duration minus, Q span duration, which would give me the whole span duration.
**Christophe** 34:26 Yeah.
**Adriel Perkins** 34:27 Although, they still want the exact span, but, That would be a way to calculate it.
So I guess what we… I guess the thinking that I'm having is that we need to add some of these attributes and take a look and… Update some of these things, yeah?
both on the GitHub side and also on the… SimCom said.
**Christophe** 34:53 So basically, you want to… Create an additional span for queues.
Here on this page.
**Adriel Perkins** 35:05 That's what I'm thinking.
Should we also have one for exec? Because that's… A conversation that has come up, and a feature request that's been asked for?
**Christophe** 35:34 I'm not sure.
We had the discussion initially, With something very similar.
There, I propose the stage.
So, a way to group task expense.
**Adriel Perkins** 36:07 Okay, would stage be… would one of the stages be queued, and one of the stages be exact?
Is that what you mean by stage?
**Christophe** 36:21 It's basically a way to group A few task executions.
**Adriel Perkins** 36:30 Is that, issue open anywhere?
**Christophe** 36:34 It was a discussion in the initial PR.
**Adriel Perkins** 36:40 Gotcha, okay. Like, the initial CICD.
**Christophe** 36:43 Yeah, for the initial attributes.
**Adriel Perkins** 36:46 Got it.
Oh, okay, wait, I'm trying to think. I think I know, let's see.
Let me search shit this way.
What's your GitHub handle?
**Christophe** 37:03 COMPOSE, K-A-M-P-H-A-U-S.
No, you created that initial PR.
**Adriel Perkins** 37:15 Boom.
This one?
**Christophe** 37:21 Yup, it was that one.
**Adriel Perkins** 37:24 The OG, OG ones, oh no.
This was a heck of a… issue. Report requests, Oh, man, I don't even know where to begin looking for this discussion on.
**Christophe** 37:40 Yeah, there were too many discussions on it.
**Adriel Perkins** 37:43 Yeah, like, 700 and something, I think? Or, yeah, 236.
Wait, did they change the way… wait, hold on.
**Christophe** 37:56 Yeah, as there have been changes since the UI.
**Adriel Perkins** 38:00 Yeah.
You know, I'm, like, struggling to find… All the… where the comments are.
**Christophe** 38:16 Yeah, I don't think you can easily find anything here.
**Adriel Perkins** 38:20 Great.
Trying that… nope.
There used to be, like, a little select down up here, or, like, right here.
That would show you… show you all the different comments that existed. Oh, here, maybe, maybe a good conversation.
Alright, here we go. This, this'll work.
I think.
You're, let's see… Yeah.
**Christophe** 38:55 net worth? Yep.
**Adriel Perkins** 38:56 Nope.
Felter… Well, that's silly.
It doesn't show the… conversation.
Do you want to see the stage?
Oh, this is so lame.
It shows barely any.
**Christophe** 39:48 You know, it's… you know, I don't… I don't find it easel now.
**Adriel Perkins** 40:04 It's a bummer. Yeah.
**Christophe** 40:08 But yeah, coming back to the discussion… Should we have… Stage spans, exec spans, queue spans.
what use case do we want to solve? We want to… Be able to group the… We want to… takes the pipeline run, Span, and be able to subdivide it.
To better know which part was queuing, Which part was execution?
And I guess then it would also make sense to have a finalized span.
**Adriel Perkins** 40:49 Yeah.
**Christophe** 40:50 we might also want to be able to group C.
Task executions?
**Adriel Perkins** 41:14 A desert stage… Q, exec… And finalize.
**Christophe** 41:30 Yes.
And I guess stage and exec could be similar if we say we could have multiple.
Such spans, one after the other, or even concurrently.
But then, what's the difference between a workflow and a task?
No, I mean between the workflow under stage.
Or workflow and exec.
Because we can already have nested Pipelines.
**Adriel Perkins** 42:13 Right, right, right, right.
Yeah, I think the pipeline has been, like, you've got, like, the workflow run is a pipeline, the job run is a pipeline, but then the little tiny things that you do within that have been the tasks.
**Christophe** 42:37 Yep.
**Adriel Perkins** 42:42 And I guess, theoretically, like, you know, if you have another… most of the tools have, like, only those two layers, or three layers.
**Christophe** 42:53 And nothing prevents you from nesting tasks.
That's what…
**Adriel Perkins** 42:57 Right.
**Christophe** 42:58 want to do.
**Adriel Perkins** 43:00 Yeah, exactly, right? Like, when… if you use, like, something that… that spans from within the task, that can be, you know.
A task, a subtask.
**Christophe** 43:12 Yeah.
So it's more really wanting to be able to distinguish queuing and finalization.
**Adriel Perkins** 43:22 Yeah.
And… Execution.
**Christophe** 43:29 No.
So basically, So, different run states.
That we have in CICD pipeline 1 duration.
**Adriel Perkins** 43:56 So, probably the easiest ones to get going would probably be, like, the VCS ones first.
And the CICD metrics, and then I think this one might have to… just… iterate on a little bit beforehand.
I'll take a look, like, a drill action item.
I'll compile an issue for this.
And reference some of the things.
Anything else on the subject?
**Christophe** 44:47 No, I think that's it.
**Adriel Perkins** 44:52 Hey, Carla.
**Christophe** 44:53 Awesome.
**Carlos Alberto Cortez** 44:54 Hey, hey!
**Christophe** 44:56 Hey.
**Adriel Perkins** 44:57 How's it going?
**Carlos Alberto Cortez** 44:58 Yeah, great. I think Amy have joined the, specification call instead by mistake.
**Adriel Perkins** 45:04 Yeah. Oh, got it.
**Carlos Alberto Cortez** 45:10 But on that point, I don't know if you saw that, and actually we can talk briefly about that, but there's a PR… The specification in the call.
It's 781… no, sorry, 5003, about removing, in the specification, the mention of the custom text propagator for AMP propagation.
So basically now, the specification would only mention, like, a custom carrier.
Right, that one.
So, Robert, who is the author of this PR, he will be talking about that in today's call. I don't know if you have any opinion?
Even though it was not normative language that you use, Adriel, when you created this PR, he still seems to think that This is, misleading, and we should mention to, you know.
seek authors that they go for together route instead only.
**Adriel Perkins** 46:20 Yeah, I mean, I don't feel like it's misleading or buggy, but if… if implementers of these SDKs and languages.
want to focus on EMD failures instead? Like, that's fine.
**Carlos Alberto Cortez** 46:37 Yeah, on the right side, I think that most of the actual SIGs, sorry, most of the actual implementation in different SIGs are using carriers instead.
So, at least that's a well-accepted thing.
**Adriel Perkins** 47:07 Sorry, I had some background noise. Yeah, I mean, I'm… It's totally fine. Like, if that's… if that's just the implementation detail that people need, like, because at the… at the end of the day, like.
there were… there was only the propagator originally, right? Like, Python had a propagator that was dedicated, Swift had one that was dedicated. The only original implementations were propagators.
And that's what started this whole conversation, and that's why it ended up in non-normative, because of the prior art. But if people want to, you know, say, well, like, look, the… we've looked at the implementation details, and the ENV carrier is just a better solution.
For this, and so that's actually what we want to recommend, and, like, totally fine.
**Carlos Alberto Cortez** 47:50 I will mention this part about the prior art, I have forgotten about that one, so it's a good one, just to mention.
**Adriel Perkins** 47:55 Yeah, like, you know, 3 years ago, when… actually, maybe longer than that, when the original request for it was made.
Python implementation was ENV propagator. Swift, they never merged that one. Swift did merge theirs.
And then years later, we finally were able to move this, like, the request for this thing forward. So, like, you know, there was a lot of feedback. None of the ENV carrier slash propagator came up in the original feedback for the spec request.
And so, like, we just, like, for prior art, it was like, it was there, you know.
We don't want to be prescriptive of this guidance, but, you know, we want to make sure that it's… compatible without having to impact the community at large. But if, like, we're already fixing it.
you know, Python, since it was never merged, I just merged in the NVIDIA carrier solution.
And then, he's already made a PR to SwiftCore, like, if they're good with it, then… ship it. We can be consistent about it, I have no problem being consistent about it.
**Carlos Alberto Cortez** 49:03 Okay, perfect.
**Adriel Perkins** 49:06 Is that call after this call?
**Carlos Alberto Cortez** 49:08 Yes, in turn.
**Adriel Perkins** 49:09 Okay.
I'll try to… I'll try to jump on.
**Carlos Alberto Cortez** 49:12 Nice.
**Adriel Perkins** 49:21 Cool. Anything else?
**Christophe** 49:26 Not from my side.
**Carlos Alberto Cortez** 49:30 Likewise, low progress, but making progress. Otherwise, all cool.
**Adriel Perkins** 49:36 Alright.
Cool deal. Well, hey, it was good talking to y'all today, and looking forward to stabilizing and all the fun things to come. Y'all have a good rest of your week.
**Christophe** 49:45 You too. See you.
**Carlos Alberto Cortez** 49:47 Chop.
