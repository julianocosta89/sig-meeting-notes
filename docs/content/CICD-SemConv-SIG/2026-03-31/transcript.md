SIG: CI/CD SemConv SIG
Date: 2026-03-31
Duration: 53 minutes
Zoom Recording URL: https://zoom.us/rec/share/K0AqTmo8RgedlauqIUt2pFzWjyG6SAd0wfHiL4gv5ApMhsgk5-xTHSmonAzmxYKn.Fr23cGKRsHPhExuI
============================================================

## Zoom Recording Transcript

**Adriel Perkins** 01:25 Good day.
**Victor Lu** 01:27 J.
I'm a visitor here, so I'm not sure you have a regular meeting on that. Are you part of a regular team here?
**Adriel Perkins** 01:36 To me, problem.
**Victor Lu** 01:39 Pardon?
Hello.
**Christophe Kamphaus** 01:42 Boom.
**Adriel Perkins** 01:44 Okay, now I should be able to hear things. Testing 1, 2.
**Christophe Kamphaus** 01:49 We can hear you.
**Adriel Perkins** 01:50 Sweet, I can hear you too. Alright, awesome.
Audio problems, always.
**Victor Lu** 02:12 So, the reason I'm visiting this, meeting here is there is a Senkov CV event.
which is part of Linux Foundation, but it's in the CD Foundation.
I just wanna see, is there, anything that's… Kind of related for this, telemetry, meeting.
**Christophe Kamphaus** 02:36 Yes.
When we defined the CICD SAMconf, we base ourselves regarding names a lot on the CD events spec.
**Victor Lu** 02:47 Good to know.
**Christophe Kamphaus** 02:48 They also know that the maintainers behind CD events are aware about the OpenTelemetry CICD MCONF, But we don't have a direct exchange between each other.
**Victor Lu** 03:00 Okay, cool.
That's great. I'm gonna listen and learn then. The reason…
**Christophe Kamphaus** 03:06 And…
**Victor Lu** 03:06 We're doing that is we're actually, creating another extension of CD events, for data ops events. So, that's why I'm, going to those places and learn what's going on. This is the other one that's, creating a… DataOps event. It is basically a state event, but it's more data-related.
So, is that… is that also… should be part of this, meeting?
**Christophe Kamphaus** 03:35 You're welcome to, stay here in the meeting.
One thing I know is that, OpenTelemetry SamConf, does support CD events.
If I remember right.
It's just… It's basically a wrapper around the CD events.
And we don't map it to the more specific sumconf.
So we don't have to support.
**Adriel Perkins** 04:00 That'd be decent.
**Christophe Kamphaus** 04:01 between CICD, SamConf, and CD events.
**Adriel Perkins** 04:05 It supports cloud events, and cloud events support CD events.
If I recall correctly, I just sent the link there. But we, we, you know, just to elaborate there, like, we originally wanted to just use CD events.
But, like, the feedback from the community that we got was basically, like, no, like, let's make something very industry, like, in-tool agnostic, because CD events kind of came from… it's got a lot of the same nomenclature that you'll see in TechThunt pipelines, because that's partly where it was, like, what do you call it?
Not inferred from, but, like, inspired by?
And so, the industry, like, there's a long PR, we can absolutely send it to you, where there's a lot of back and forth around, like, how we should handle this, but the approach that we took for OpenTelemetry and basically telemetry as a whole, was to go with this, non-vendor-specific or inspired, kind of semantic set of conventions there. But you can certainly embed data ops events or cloud, or CD events, you know, into cloud events, because cloud events is supported experimentally as, in the semantic conventions.
It's just not going to be the same kind of, like, first-party support, I don't think, from the, like, registry of nomenclature for all the different, attributes that should be on telemetry, so it's a little bit of a difference there.
**Victor Lu** 05:37 Awesome. Would it be possible for you to paste the long discussion you mentioned? That really helps us, the DataOps event, to learn the history and how to do the, extension to DataOps event, CV events properly.
**Adriel Perkins** 05:49 Sure.
**Christophe Kamphaus** 05:53 We are thinking about the initial PR where we defined CICD SAMconf.
**Adriel Perkins** 05:58 Yup.
**Christophe Kamphaus** 05:59 Yeah, I remember there were a lot of discussions on it. It took a long time.
**Adriel Perkins** 06:04 Yup.
**Christophe Kamphaus** 06:06 And maybe to give some background, comparing the open telemetry SAMconf, or CICD, versus CD events, The CD events are good if you have long-running traces, So, long-running bill drops.
Because it's asynchronous, and in OpenTelemity traces, we have an open issue.
Or long-running traces.
Where we are… Thinking about moving to an events-based model, basically.
While the OpenTelemetry traces model is very good when it comes to Displaying drops, because we can have nested spans inside the trace, where the trace represents It's a bill drop.
Yeah, that's… that's basically it if you compare both.
**Adriel Perkins** 07:18 Pasted some of those links in the chat, by the way.
We'd love to, yeah, definitely stay here, for sure, and we'd love to, like, collaborate if you have anything that you feel should be collaborated on.
Well, we'd still love to, I think, collaborate with the CD Events folks more, too. I know, like.
Oh, I'm forgetting names. Antoine I'm just gonna go pull up the Slack, because I bet you it's in there.
**Victor Lu** 08:09 Yeah, actually, we, we work very closely with the CD event folks.
**Adriel Perkins** 08:16 Cool. Yeah. Yeah, we love to collaborate more, for sure. Right now, you know, again, like, I think CD events is just supported under Cloud Events, because it's one of those things that's supported within there, and then Cloud Events is… supported as experimental, but I'm not sure how much, like, movement Cloud Events has gotten over the period of time, because, Cloud Events has been… there in the semantic conventions for way longer than CICD has been.
But the primary, like, working group for CI-CD has been this one, which is, like, you know, again, lives outside of the cloud events semantics, so…
**Christophe Kamphaus** 08:54 straight.
But we don't have events under Cloud Events, it's just the span mentions.
**Adriel Perkins** 09:02 Yeah, yeah.
I don't know how… I don't even remember… Seeing cloud event spans come into play.
I don't know when that was added, that might predate this, but I'm not… I'm not sure.
It's, Great conversations to… to have. And then there's also that whole, like, oh, that one PR that's, like, unify workflows.
Do you know which one I'm talking about, Kristoff?
**Christophe Kamphaus** 09:35 Yes, I think we have it on the board, so if you share the screen… support.
We can take a look.
**Adriel Perkins** 09:44 Okay.
Okay, huh?
**Christophe Kamphaus** 10:00 It's in the leftmost column, Unified Semantic Conventions for Task Workflows, pipelines, and Drops.
**Adriel Perkins** 10:22 I'm sorry, I had a phone call for a second. Or my wife was calling me for nonstairs, but which one did you say, I'm sorry?
**Christophe Kamphaus** 10:31 The Unified Semantic Convention, yeah, that one.
**Adriel Perkins** 10:34 There we go.
Yeah, this is also one that you might want to take a look at, just, like, for… context. It's a… it's an interesting one. Because, like, right now we have… you know, cicd.pipelines, but there's conversation around, like, unifying the pipelines, concept into just, like, either, like, workflows or whatever it may be. We have…
**Christophe Kamphaus** 11:01 Because you don't know if you have a machine learning job. Is that now a CICD pipeline run?
Or would it be a workflow?
Same if you have batch shops.
Any kind of, drop, engine.
Yeah, so that's why we are thinking about unifying it.
And the reason why we haven't moved forward with it is we basically need more prototypes, so not just CICD systems implementing it.
But, whatsoever's, like an, processing engine.
a batch engine.
That would emit this, subconfine epoch.
**Adriel Perkins** 11:47 Yeah, I would love to see, too, like… like, I know when we started CICD semantic conventions, I know someone from Apple came here, and… because they had implemented OTEL in their custom build of Tekton.
And I would love to see, like, what they chose, too, like… because, I mean, that's technically an implementation, right, that already exists and predates this.
**Victor Lu** 12:11 What… was that the DC?
From Amazon.
**Adriel Perkins** 12:16 First, say that again?
**Victor Lu** 12:18 Did he see me, he's from Apple, is that him?
**Adriel Perkins** 12:21 I think so, I think so, yup.
It would have been on the original… I cannot type this morning.
**Dotan Horovits** 12:42 Wasn't it already on the EOTIP?
**Adriel Perkins** 12:46 I don't know, I don't know that it was on the OTAP, but it was definitely in the project, like, the original project. Yeah, that's for sure.
**Dotan Horovits** 12:51 Sure, I'm just thinking, because I do remember, even on the OTEP, original OTEP, this discussion started coming up, and the CD events, and all of that, so I'm wondering…
**Adriel Perkins** 13:04 Yeah, the, This is the original community proposal that was, yeah, from… from one of the OTEPs. I think it was the OTEP that you opened, DOTAN, the original one.
But it would have been… yeah.
XIBZ.
**Dotan Horovits** 13:23 Yeah, exactly.
**Adriel Perkins** 13:24 he was telling us early on about some of the stuff that they had done, for Tekton internally. Like, I'd love to know what conventions they chose there.
**Dotan Horovits** 13:35 Yeah, they gave good input back then, I remember that, Made it seem more feasible at the time, but… It didn't come from any other direction, so… interesting how it ended up with that.
**Adriel Perkins** 13:49 Could probably reach out to if there's, if it makes sense.
Alright, where'd we go? There we go.
Cool. Anything else there?
**Christophe Kamphaus** 14:05 Yeah, I found a few issues in the, semantic convention issues.
And added some to the board, because I noticed We only get new issues on our board if we add some more stuff.
**Adriel Perkins** 14:20 Mmm.
Okay.
Thank you for doing that.
There it is.
**Christophe Kamphaus** 14:30 So what's the one about artifact build pipeline URL full?
I added that one on the leftmost column.
**Adriel Perkins** 14:41 Okay.
**Christophe Kamphaus** 14:42 missing.
**Adriel Perkins** 14:43 From our board.
**Christophe Kamphaus** 14:43 one… Oh no, I think it was Pipeline Run Active 2.
A pipeline run status.
**Adriel Perkins** 14:52 Okay.
**Christophe Kamphaus** 14:54 And I created the one below.
when I was implementing the SAMconf in Jenkins pipe… in the Jenkins plugin.
There was one thing that wasn't quite clear to me. I asked that as a question.
And I would create a PR to clarify it, maybe.
**Adriel Perkins** 15:16 Okay.
Do you want to review that here, or…
**Christophe Kamphaus** 15:21 Yeah, we can, pull it up, see, pipeline task run ID.
So, one below, yeah.
Basically, I was not sure.
whether tasks CID should remain stable inside a pipeline run, Or… Or should it be just within a single run, or within the pipeline? So if you rerun the… Pipeline multiple times.
It's meant to be the same ID, if it's the same task.
**Adriel Perkins** 16:05 I think any… any .run.id is unique to the run, yeah?
**Christophe Kamphaus** 16:12 So, if y'all… For multiple runs of the same pop-up.
pipeline, it would be different IDs.
**Adriel Perkins** 16:23 I think that was the original thinking, at least that was the original thinking I had. I don't know what the original thinking everyone had.
But the… I know for… Hub's perspective, like, that's not the case, because they just say, run attempt, right?
And they give you a number for the run attempt, and then that's how we create, like, the deterministic span IDs for that.
But I'm just thinking, from the run perspective, I don't know if we have the language there. Maybe that's something we should… That is something we should ex… it's not a maybe, it is something we should discuss, but, Let's see… Yeah, the way a run ID is expressed here is it's the unique identifier of a pipeline run.
And a unique identifier of a task run.
So, yeah, I…
**Christophe Kamphaus** 17:21 Yeah, and here for the task run ID, it's not clear whether it should be unique within the pipeline, meaning If we have multiple runs, The task ID stays the same.
Over so it's globally unique.
**Adriel Perkins** 17:37 Yeah.
We should definitely… clarify that.
I would think of it… So I guess if you… if you correlate it with, like, the result, right?
You'd have to have some way to differentiate that this, like, this first run was not successful, and this second run was successful.
Yeah.
**Christophe Kamphaus** 18:02 I guess you could take the task name.
But you might have multiple tasks that have the same name.
**Dotan Horovits** 18:22 Is there another, like, an ID entity on the pipeline, on task level that you can qualify by… with that? So, the combination of which will get a global unique, or.
**Christophe Kamphaus** 18:33 the run URL full.
I think would be globally unique.
**Adriel Perkins** 19:04 So I guess what… what do we want to put here?
Cause I know that, like, It's not… it's probably not unique in the context of implementations that exist.
like, I think this… and I think it part… in part, depends on the CI-CD vendor.
But, the… I guess the question is whether or not it should be globally unique.
**Dotan Horovits** 19:31 I guess it's also the question, on one hand, we try to decouple from the vendor implementations. On the other hand.
if we get too far away, it means that you need sort of an ETL just to convert, you know, convert their ID to another set of IDs that you manage separately, that you ensure the global uniqueness, and then something like that, so… And then it obviously creates an additional overhead, so… I guess finding the sweet spot that's still… Aligns with the industry's best practices, if we can figure out what those, are.
**Christophe Kamphaus** 20:14 Well, I think we should… Maybe think more what are the use cases we want to cover with this attribute.
We could use the tool.
Identify?
Tasks.
And we can use it to correlate tasks within the pipeline.
And those might not be the same use case.
Because for one, the correlation, it would be better to have an attribute that stays the same.
Or one task.
Inside a pipeline.
When you execute it multiple times.
And when… Identifying a task run?
It's better for it to be globally unique.
Or at least unique within.
Multiple runs in a pipeline.
And thinking about it, if we associate our CICD pipeline and CICD pipeline run entities to the span.
As I said, it doesn't need to be globally unique.
**Adriel Perkins** 22:19 Say that again? I didn't mention…
**Christophe Kamphaus** 22:21 We…
**Adriel Perkins** 22:21 Grok that one.
**Christophe Kamphaus** 22:22 You see resource entities, the CICD pipeline and CICD pipeline run.
We said we can scope we can already identify the pipeline, we can identify the pipeline run.
And then inside of that set.
We could have unique IDs for the task run.
Even if CIT would be the same.
Across multiple pipeline runs.
**Dotan Horovits** 22:56 And I agree, that's more like what I said before about qualifying, sort of, the… that ID with that ID, and then you get, sort of, the uniqueness, so… That could be a good, I guess, middle ground for that.
**Adriel Perkins** 23:25 So, are we thinking, then, that, like, IDs should be unique globally?
**Dotan Horovits** 23:31 So if you qualify, you don't need it to be… like, the combination will be unique globally, so you don't need to enforce the globally unique just for the… for the run ID.
**Christophe Kamphaus** 23:47 Yeah, and then we could use it for correlating The same task inside of a pipeline.
see if… one task, Starts becoming flaky.
**Adriel Perkins** 24:31 So, basically, did I articulate that correctly in this sentence?
**Christophe Kamphaus** 24:38 Yeah, so, all the task run IDs inside of a pipeline run.
Are unique, so you don't have the same Task run inside of one pipeline run.
with the same ID, too.
Yeah.
Makes sense.
And then you… between multiple pipeline run IDs, you could have the same task run ID.
**Adriel Perkins** 25:41 Okay, anything else to add there?
**Christophe Kamphaus** 25:44 Sounds good.
**Dotan Horovits** 25:45 I'm just wondering, before you finish the comment, if… because I really like the way that, Christoph sort of articulated the two different use cases, which sort of drive the need. One of them you actually listed as the IE there, when correlating.
So I guess this… maybe if we can just say that, like, we identify two main use cases. One is the correlation, and just… I like the fact that… the way that Christophe presented it is… two main use cases, maybe… there are more use cases, I don't know, but these are definitely, Should be top of mind when considering the design.
Christopher, you want to say what you… you said it best, so if you want to.
**Christophe Kamphaus** 26:24 Yeah, so one is the identifying ID.
Where you want to be able to address one task run, And… I think one good way is when you will link to it.
So I think… we already have CRL… For a task run.
So I think that one could be covered by that. And we now discuss it, and we have by saying, Is that a… by applying run ID, in combination with a task run ID, must be unique, globally.
We also have this identifying case covered.
**Adriel Perkins** 27:15 Right.
**Christophe Kamphaus** 27:15 And the second one was that you want to be able to Track one task between multiple runs.
To be able to detect when has it become failing, or is it now flaky?
And I know, for that one.
to have stable IDs across multiple pipeline runs is not a trivial task.
Because your definition of the pipeline might have changed.
So, do you know… use the same IDs, or is it a new ID?
I think there are the different systems use heuristics to… Assign CITs.
**Adriel Perkins** 28:30 Yeah, that would be… if we had, like, tasks… task IDs… That… I just feel like, yeah, that would be really hard on the CIC CD system itself, to be able to say, like, hey, every time… like, this task itself has been given a globally unique ID.
That is… Stable across all different types of runs of that task.
Because it would relate directly to the pipeline that's calling it, right?
**Christophe Kamphaus** 29:16 Yeah, and you might change the order of tasks in your pipeline. You might change how they are called.
So, it's really not trivial.
**Adriel Perkins** 29:27 Yeah, so my guess is we shouldn't do that?
**Christophe Kamphaus** 29:33 I would say Bastafold.
Okay, I'm just thinking about how would we bring this over in the PR, if we update the description now.
So we caught, say it needs, I would maybe put a note there.
So that we can, have a longer explanation.
And then also say, that… The combination of pipeline run ID and task run ID must be unique.
and set the ID, might be reused.
Between pipeline runs.
And maybe I would also put some things there.
It may be used to, help correlate The same task between runs.
But here, it's really just May, and then it's up to the… CICD systems, whether they want to do that.
**Adriel Perkins** 31:15 Great, does that capture what we're thinking?
**Christophe Kamphaus** 31:17 Yup.
Sounds good.
**Adriel Perkins** 31:26 Okay.
Cool.
Alright, we'll go back to the dock.
Alright, you wanna.
**Christophe Kamphaus** 31:45 Yeah, so… I talked with the maintainers of OpenTelemetry, and also Lutmiller.
whether we can move towards release candidate for CICD conventions.
They, checked our histories that we had, and they saw, within the last almost a year. We didn't have any… big changes. So, as they said, definitely move towards release candidate now.
**Dotan Horovits** 32:13 Mmm.
**Christophe Kamphaus** 32:14 And, yeah, they also said we have implementations in the collector, so… As a requirement to have an, a poker, implementation is given.
So, there's no… So you didn't see any, stoppers.
So it's up to us, do we not want to move forward?
Or do you see anything that would block us at the moment?
**Adriel Perkins** 32:47 I think the only thing that might block us is… the unified, Conversation.
Like, if we move to stabilization, and we say later on that we want to… we don't want to differentiate between Pipeline types at a namespacing level of attributes.
then that would be a breaking change, and saying, like, you need to… you… like, you're… in this example, if I'm just reading off of here, right, like, CICD pipeline name should now just become workflow name. Like, if we stabilize CICD pipeline name, but then we say, like, we're unifying this, then that becomes a breaking change.
From a stability standpoint.
Not saying that it can't happen, But the… I think this is the only thing that, like, really makes me hesitant to… I know we're, like, not making progress on this, but it makes me hesitant to say, like, yeah, let's stabilize CI-CD pipeline name.
As an example.
**Christophe Kamphaus** 33:53 Yeah, makes sense.
**Dotan Horovits** 33:55 I agree with you. On the other hand, just to, present, I guess, the other side of the equation. This is a big thing. Like, we started off this working group with, and the SIG with the CICD in mind, and this broadens the scope significantly.
Which will, you know, if we do, you know, formalize this extended scope.
It will take a significant amount of time to, now stabilize.
So the question is if we want to, and we can reflect that, by the way, to the SEMCON, saying, hey, within the scope of the CICD, we're stable enough and mature enough to go ahead. There is this discussion that is beyond the original scope.
And A and B, there is no significant drive now behind it. We don't see, like, a significant driving force, pushing it.
then we suggest advancing, and we can let them know that if this becomes the expanded scope, this will obviously necessitate a breaking change. But I think these are the classic situations where breaking change is mandated, like…
**Christophe Kamphaus** 35:11 And it was also at the start, when we started defining CICD, the message was, let's rather start inside the CICD scope.
Because there we can make progress faster than… If we want to define a universal Solution for workflows.
**Dotan Horovits** 35:31 Exactly, exactly. Grabbing too much, more than we can bite, more than we can chew, you know, is something that we identified really early on, and also based on other SIGS experiences that… but even all the… if you look at hotel in general, one of the reasons that we found it so difficult and still to get hotel past the, the GA mark is because the scope keeps on broadening so much, and no one said, but, okay, you broaden the scope, but this essential scope is the one based on which will… will GA, it will stabilize. So, even the collector is still not stable, so I think… This is the… The pattern we want to, Be careful of, because there's so many use cases out there that if you try to cater for all, you find yourself, experimental forever.
**Christophe Kamphaus** 36:22 Yeah, I think that's why they are now, this year, focusing on, Becoming stable.
**Dotan Horovits** 36:28 And on the…
**Christophe Kamphaus** 36:30 Using a defined scope for that.
**Dotan Horovits** 36:32 Yeah, exactly.
So it's fine that, I don't know, the, I don't know, Profiles is only now getting into alpha.
Because you say the scope is without the signal, and the signal will be added later, or, like, you start carving out exactly the scope. So we can also say the scope that we take for stability is the CICD scope. There is a broadened broader scope that is in discussion, it won't be part of the stabilization. Like, that's, I think, the… if I look also on the broader hotel.
This is sort of the… The learning path that we've all gone through.
**Christophe Kamphaus** 37:07 Yeah, and actually, there were some discussions I had with the maintainers of OpenTelemetry, That we should have.
unconscious moving forward of all semantic conventions, that we shouldn't just stay in development or in alpha. We should consciously move towards release.
Towards stability.
**Dotan Horovits** 37:31 Yep.
So again, we can take it to a broader vote, but I think here sounds like, And given the fact, again, that it's been there since late 2024, but there was no driving force to push it forward, and the efforts that have been made were around the CICD scope, the original scope, so… I think it's also aligned. If we had seen, like, now, you know, 3 maintainers jumping in, full steam to push, this, it would have maybe shifted the decision, but seeing that it's… the proposal is there since December, 2024.
I think also speaks for the sense of urgency, or lack thereof, maybe.
**Christophe Kamphaus** 38:14 Yeah.
**Dotan Horovits** 38:21 Adria, what's your, what's your take on it?
**Adriel Perkins** 38:25 Yeah, I think, I think bringing it to the largest Semantic Convention group next Monday.
The general meeting?
Would be… would be good to have the conversation there.
I still hesitate a little bit.
But, I think bringing it up to the… to the larger group and just, like, making that hesitation very clear before we move to stabilization and getting the larger feedback would be… would be the right approach.
**Dotan Horovits** 38:56 Okay. I just do want, Let's… I don't do… again, from my experience, just putting question, I think, is usually a bit more tricky. I think we do… should come as the ones that deal with that day in and day out, with some sort of I don't know, our own, you know, best practice or fields. Of course, it's not a finalized decision, we'll bring it to the forum, but let's bring it with our, I guess, our read of the situation and the feasibility and so on. So, not just as an open-ended question. Christoph, will you be able to be there? I think, since you were taking the discussion in person and in the.
**Christophe Kamphaus** 39:40 Yes, I would be… Or will be at the next, some calls sick meeting.
**Dotan Horovits** 39:47 Great. And Adriel, of course, if you're able to join and express your, your concerns as well, then I will… Get all the… all the views, and I'll try and join as well, but I think… I think pretty much we've summarized what's the take, the pros and the cons, and then we can ask for more feedback.
**Adriel Perkins** 40:10 Yeah. Okay. Sounds good. So that's when Monday… Monday, April… April 6th?
at 11 ET.
**Dotan Horovits** 40:22 Second, just go back Monday, April… It's Monday. Yeah, coming Monday. Yeah. Next.
Okay.
**Christophe Kamphaus** 40:32 Oh, is that Easter Monday?
**Dotan Horovits** 40:34 Yeah, so it's Easter Monday, that's why I'm wondering if it's problematic, or if they're keeping it in Easter Monday, I don't know what's the customer…
**Christophe Kamphaus** 40:42 We already had two council sick meetings this week and last week, so… I don't know if we will have it next week.
Okay. Anyway, I will bring it up in the next one.
**Adriel Perkins** 40:54 Yeah, I'm already…
**Dotan Horovits** 40:55 Oh, sorry. Go ahead, Adriel.
**Adriel Perkins** 40:58 I'm already adding to the dock, for this. It does look like they have…
**Dotan Horovits** 41:03 They…
**Adriel Perkins** 41:04 the date…
**Dotan Horovits** 41:04 Yeah, pleasure.
**Adriel Perkins** 41:04 Are you there?
**Christophe Kamphaus** 41:05 I didn't think that it's Eastern.
**Dotan Horovits** 41:07 Yeah, sometimes they put, and then someone flags, hey, you know, this date is…
**Adriel Perkins** 41:14 So, I'm just gonna write the description here, and like, you know, if they punt it.
blindness there, we can copy it forward to the next one. If they don't punt it, though, we could talk about it. I mean, I have no problems going on Monday the 6th.
Well, Christoph, do you have any issues showing.
**Christophe Kamphaus** 41:30 No, it should be fine for me.
**Adriel Perkins** 41:32 Okay, so, discuss, stabilization.
of CICD, let's see, discuss moving… board with stabilization of CIC semantic convention.
**Dotan Horovits** 41:46 5PM, right, Christoph? Your time.
**Christophe Kamphaus** 41:49 Yes.
**Adriel Perkins** 41:50 can, like.
**Christophe Kamphaus** 41:50 It's 5pm.
**Adriel Perkins** 41:51 Yeah. Breaking changes if we move forward now.
That sound reasonable? Anything we want to add here, to this description?
For any, like, data points? I would…
**Dotan Horovits** 42:08 Maybe I would just mention a follow-up to, yeah, as a sub-bullet, follow-up to the in-person discussion at KubeCon.
I don't know if you want to name, like, Ludmila and Christoph as, like, the anchors for people to, connect, or something like that, yeah.
Christoph, you were there, so if there's anyone else you want to name, just to give the scope…
**Christophe Kamphaus** 42:31 It was us two was there, and we discussed it.
**Dotan Horovits** 42:33 Okay.
**Adriel Perkins** 42:35 I gotta make sure I spell names correctly.
**Christophe Kamphaus** 42:39 You can also paste the link to the unified semantic, for workflows, sir.
No, that's a project port link.
**Dotan Horovits** 43:06 And Christoph, thanks so much for, for taking that in person. Like, I… I unfortunately had to cancel last minute, my trip to, that was one of my, wish lists, on my wish list to, to get this discussion going, in person with the folks. I did, like, a preliminary discussion with them at, the Hotel Unplugged, so, you know, it was favorable vibes that I hope were conducive to the situation, but definitely Cuba.
**Christophe Kamphaus** 43:34 That's the same Michael time.
**Dotan Horovits** 43:35 Yeah, yeah, very good. I'm glad that.
**Christophe Kamphaus** 43:39 And also, feedback I got was, yeah, we don't want to leave it too long in development, because people are starting to implement it, and then it becomes stable by default.
**Dotan Horovits** 43:51 Exactly. And then again, this is the learning across the board, like, this is why I'm saying that I think it's not just because they're in favor specifically of CICD, it's because they realize that in many cases in the past.
People trying to bring it to perfection, and to, all-encompassing.
And the result being that it stayed in development for way too long, and the fact being that, you know, vendors and the companies are already starting de facto to put it in practice. So, this is the learning across OTEL, I guess, that we need to be less of engineers trying to bring it to perfection, and less, Go the pragmatic path of, let's roll out something that is, has solid value on its own, that can move forward with.
Yeah. That's the message that I got from all these discussions that I attended, at least.
**Adriel Perkins** 44:40 Yeah, no, it makes sense, right? Like, because when we broke… when we moved deployment.environment to deployment.environment name, because deployment environment had been in development for so long, it was fine for us to move it, but people had already implemented, and it was a breaking change, and people got a little bit, up in arms about that… that change, right? Because it was… it was really a breaking change, but it was experimental, and so… Like, it makes sense, like, I…
**Christophe Kamphaus** 45:05 I also hear it… I also hear it was a discussion in some config.
So, as they are changing something.
It's still in development, but people have started implementing it, and maybe they changed it once already, so there, people have really start getting a bit frustrated.
**Adriel Perkins** 45:24 Yeah.
**Dotan Horovits** 45:24 And you can only draw a pool so much that, okay, but you know, we didn't declare it stable, because, okay, but it's been like that for ages, so… I see that by the way also with the Gen AI SIG as well. Again, people move very fast with implementing the AI observability workflows, and… they count on that, although it's not yet fully, like, stable, and it moves very, very fast, and that's why you start getting, like, patterns like the one that I shared a while back with trying to unify what they do in Traceloop, and what they do with this, and all that, and try to do a collector processor, or something like that that will merge these, and then you get all these patterns that are ultimately patches because you don't have the standard. So, I think… Yeah, we see it across the board.
**Christophe Kamphaus** 46:11 Yep.
**Adriel Perkins** 46:11 I wonder if, like, from that breaking change perspective.
Because, like, there was a talk, I don't know if it was last year, or if it was, like, more recently than that, but it was, like, how to… it was from the Weaver Project, if I recall correctly, and it's how to migrate people's semantics without breaking them.
using, like, Weaver and using, I think, processors. I wonder if, like, in the event that we do break things, or if we keep it in the back of our mind, we could provide some type of guidance for migration, using that kind of approach, right? Like, maybe it's… maybe it's as simple as an OTEL collector OTTL statement for migration, or maybe it's… more of the Weaver approach. I don't remember exactly how the Weaver approach worked, on that side of the house, so, like, I'd have to validate on how, like, the implementation details of that, but maybe that's something we could keep in mind with regards to, like, breaking changes and migrating people later in the future to make it easier and, like.
Just to make them feel less pain.
So, maybe, maybe we could think about that, too.
**Dotan Horovits** 47:14 Yeah, although I think this would be probably a systemic question to ask across the SIG, so I think this is a discussion that we shouldn't be trying to solve specifically for CICD, SEMconv breaking changes, but rather across the board, what would be the best practice for SEMCONV in general, if.
**Christophe Kamphaus** 47:32 If I remember right, the collector has a transformer.
When you get to the schema.
I don't think it's the OTTL, but you give it a schema.
**Adriel Perkins** 47:44 Oh, the schema process?
**Christophe Kamphaus** 47:45 Yeah, I think so.
**Dotan Horovits** 47:47 Oh, yeah, yeah.
**Christophe Kamphaus** 47:48 I'm not sure if it works, I haven't tried it.
**Dotan Horovits** 47:54 It's a processor, yeah, I think I saw the processor, I don't know the stability of this one, but yeah, I remember the translator, but I actually never understood why… when would you rather go with OTTL rather than this? And I don't know. I always find it confusing, but I've never gone around to digging into that further, but either this or that probably will be… So, along the best practices that, semConfig would probably, recommend.
**Christophe Kamphaus** 48:21 Yep.
**Adriel Perkins** 48:22 I'm gonna just pop that as a sub-bullet in here, too.
**Dotan Horovits** 48:27 Again, maybe not even a sub-bullet. Maybe you can bring it to this whole topic, because I think the value of this discussion is… goes beyond the SIG… the CICD SIG. I think it's, like.
a good discussion to have across the board, and actually, it would be good that not each sub-sig will have its own solution, but rather something… because if you have several… if you've already adapted as an end user, if you've already adopted a mechanism, let's say Weaver.
to move, breaking versions, like major releases of, of, SEMCOMs in one, in one side of Autel, you wouldn't like to use another mechan… you wouldn't expect to use another mechanism in just another subset of the OTEL SEMCOM, right? Intuitively.
**Christophe Kamphaus** 49:20 Yeah, probably Josh and Lutmila are the best people to ask there.
**Dotan Horovits** 49:24 By the way, you can put, if you already have it open, Adriel, you can put these as, like, sub-bullets as links on this, issue, adding both the, schema processor and OTTL as, like, potential, mechanisms or something.
**Adriel Perkins** 49:43 Which issue do you think that should go on?
**Dotan Horovits** 49:45 No, I'm saying the issue is good, I'm just saying if you want to add as a sub-bullet the links to the schema processor and to OTTL as… links for, I guess, potential mechanisms to address For the, how to migrate.
**Adriel Perkins** 50:02 Do you mean, like, the GitHub issue?
**Dotan Horovits** 50:04 Yeah, yeah, Gator Beaches, sorry, what did I say?
**Adriel Perkins** 50:07 Well, I'm just clarifying, because I don't know which.
**Dotan Horovits** 50:10 Yeah, yeah.
**Adriel Perkins** 50:10 GitHub issue that we…
**Dotan Horovits** 50:11 Yeah, you're… the one that… No, no, the one that you… not the… the… the… hotel collector processor that does this schema conversion. You had it open a second ago in one of the tabs, saying if you already have it open, just… Copy, paste the link.
And you can put it on the agenda item as a sub-uller there.
**Adriel Perkins** 50:30 Okay, the agenda, yes. Yeah, I did.
**Dotan Horovits** 50:32 Yeah, that's what I… okay, sorry.
**Adriel Perkins** 50:34 August.
**Dotan Horovits** 50:35 Oh, it's not hypertext, that's what I didn't see, okay, sorry.
**Adriel Perkins** 50:37 Oh, let me…
**Dotan Horovits** 50:38 Yeah, if you're spaced… There we go. Yeah, exactly, okay, okay.
No, it's it.
**Adriel Perkins** 50:42 Alright, so two items, then, for Monday's semantic convention.
**Dotan Horovits** 50:47 Taking over SEMCOM's, thing called.
**Adriel Perkins** 50:51 I put 10 in 15 minutes, you know that those are gonna go way longer than that.
**Christophe Kamphaus** 50:55 I remember. But we'll play, we'll play.
**Dotan Horovits** 50:57 You looked Mila and Josh. Yeah, yeah, yeah.
**Christophe Kamphaus** 51:00 with one small point where I thought it's a discussion of maybe a few minutes, and it became a 15-30 minute discussion.
**Adriel Perkins** 51:09 Yeah, yeah. Like, I wanted to start at just saying, like, 30 minutes, but, we'll try to keep…
**Christophe Kamphaus** 51:14 There will be other stuff.
**Dotan Horovits** 51:16 Fair enough.
**Christophe Kamphaus** 51:18 Hi, and one last thing that they gave us as feedback at KubeCon.
when we create the PR, To move towards release candidate stability.
We should also, create a blog post to advertise it, so… Vendors know to take a look, and we should define And, That line, when we want to go towards release.
Jose knows that by then, They should definitely give us feedback.
Whether we keep the deadline depends on if there's any blockers or breaking changes coming up, I think.
**Dotan Horovits** 51:57 Yeah. Adriel, we can piggyback on the one that we anyway were planning on doing, and by the way, sorry for not, having, like, we need to get it back on track, but actually it could serve this purpose, even more.
Importantly, maybe, than what we had before. So, maybe all things work for the better.
**Adriel Perkins** 52:16 Okay, awesome.
**Christophe Kamphaus** 52:17 Yeah, that's it for my site.
**Adriel Perkins** 52:20 Cool.
I know that, The other item on here was a 3-minute item for… from Carlos, but he is having internet problems, so he dropped. I don't know if he's coming back, but…
**Christophe Kamphaus** 52:34 I'm in and back out several times.
**Adriel Perkins** 52:37 Okay.
**Dotan Horovits** 52:38 I need to drop because I have a meeting in a few minutes, I need to have a bio break in between, so sorry for dropping off on the last item, but I'll catch up offline. Thanks a lot, guys. Good to speak with you.
**Christophe Kamphaus** 52:49 of all.
**Dotan Horovits** 52:50 Yay!
**Christophe Kamphaus** 52:50 So you're.
**Dotan Horovits** 52:52 Bye-bye.
**Adriel Perkins** 52:52 Agreed. Bye.
**Christophe Kamphaus** 52:54 But…
**Adriel Perkins** 52:59 I guess we'll just take a… yep, okay.
