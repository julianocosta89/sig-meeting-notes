SIG: GenAI Semantic Conventions and Instrumentation Stability
Date: 2026-10-09
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Max Ind (Google LLC)** 00:43 Hello, sorry, I was deafened.
**Trask Stalnaker (Microsoft Corporation)** 00:46 Hey, Max. Hey, Surya.
**Surya Teja** 00:48 Hey, hi Trask. Hi Max, how are you?
**Max Ind (Google LLC)** 00:51 Hey, hey, I'm good. How are you?
**Surya Teja** 00:54 I'm doing great. Thanks for asking. Trask, how are you doing?
**Trask Stalnaker (Microsoft Corporation)** 00:59 Good, good.
Max, we had a good discussion… on Wednesday about your PR.
I think we kinda… understood other people besides just Ludmilla and yourself now understand it.
I don't remember if there was… I don't know if you got any feedback, from Ludmilla on that.
**Max Ind (Google LLC)** 01:55 Yeah, I got a lot of comments and I think Yeah, the… at least the semantics seem to be clearer now, and… Now moved on to naming, just kind of, I saw the Ludmilla has done, I think Ludmilla has done some research on naming, comparing different frameworks and what they… Call a turn, and I saw that, like, there's some ambiguities, because some… Hmm.
Some frameworks call the… loop between the… Like an Agentic loop using tools and inference to to drive the Agentic. Some frameworks call that a turn.
But actually… Everywhere I've seen frameworks.
Call this a term, they also refer… to conversation terms as terms as well. So, maybe, like, a disambiguation there could be handle conversation term for the operation name.
But again, but yeah, but I'm… Still in the process of, yeah, of, like, the research.
For the naming, and the… Like, scouting out what could be the… Yeah, what could be the name?
**Trask Stalnaker (Microsoft Corporation)** 03:22 And sort of my… my takeaway or understanding is that it would… It.
is just… An operation name that I can be.
Specific to a framework, like, whatever the framework calls it is fine to use that, like.
I'm not sure if we need… a semantic… definition… of… turn… Like, we already have… we have the hierarchy, the span hierarchy. They're all… I think we're thinking that all of those will be… this invoke agent, or whatever we call the FOO, whatever we call the span type.
And it covers… Invoke agent… Invoke workflow… This handle turn thing, and whatever frameworks want to call This, they can use that terminology.
But structurally, that doesn't really change anything structurally.
Or… And this is where I'm not quite sure, is whether it changes anything semantically, even.
Like, what would we do… what would a consumer do with that information that it's a turn versus a workflow versus an agent invocation?
Are we just, sort of, exposing that as, sort of.
a framework-specific thing that they can then rely on, that Google ADK emits this thing called a turn, but some other framework might emit something else.
But overall, we're not… necessarily trying to unify that. I'm not… that's where I'm not quite sure.
**Max Ind (Google LLC)** 05:18 Yeah, yeah, I.
We may not want to unify that, but, like, one… idea why unification might be… Good is because, If we don't semantically define when to emit this.
GenAI Invocations Fund.
then I… we may… it might just be unclear when to emit it, and it may lead to, you know, people not knowing whether, like, you know, so, for example.
in ADK, there was kind of, like, an idea to drive the agent loop through a workflow, and that was an implementation detail, or for example.
Agent as tool, that's also, that's driven for a runner, so, you know, should an instrumentation emit this.
Invocation span in these cases.
And I would say that this would lead to a lot of noise if frameworks were to emit.
You know, each kind of layer of orchestration.
If, like, each layer of orchestration Just internal to the framework, emitted the… Invocation span.
So… the… like, just defining Just kind of semantics for the invoke agent operation name, invoke workflow operation name. And then this, like, third thing, which is kind of just, like, framework-defined control flow.
It's the most difficult part, but I'm, you know, I hope to… Get some, you know, some unification so that, you know, the Yeah, so that it's like clear when this span should be emitted in the first place, yeah.
**Trask Stalnaker (Microsoft Corporation)** 07:10 Cool, okay, that makes sense to me. So, you are trying to kind of layer a semantic meaning for those three things.
Nice, yeah, yeah, that will be… That would be very nice.
Alright, let's see, Aaron, art.
**Aaron Abbott (Google LLC)** 07:38 Yeah, so the issue is linked here, but this is to fix the issue where the parts right now just collapse to any.
I also put a before and after in the PR, which might be in the description, which might be helpful, but… Yeah, the gist of it is… This makes it so that the fallback isn't a specific subtype. Where the key is always generic, so that the type isn't just a string, and you actually have, like, a… Disjoint union of different part types.
So Lumil left a comment, which was kind of against this, but I… I replied to her, She's not here, so I guess this is just a call for review, unless anybody had thoughts on this right now.
**Trask Stalnaker (Microsoft Corporation)** 08:52 Cool, anybody on the call understand parts enough to… Discuss this.
**Aaron Abbott (Google LLC)** 09:01 I mean, I could explain it a little more if people are interested, but…
**Trask Stalnaker (Microsoft Corporation)** 09:07 I would love, like, a 3-minute Primer on, like, what the… Yeah, on the problem.
**Aaron Abbott (Google LLC)** 09:17 Yeah, so definitely. In… Actually, if you go to the files… And if you go… Yeah, so some of these… I added these YAML files, which are kind of, like, golden test cases.
And what they do is they capture, like.
A payload for the input messages, output messages, whatever, and then it shows, it generates the errors or lack of errors that you would get.
So if you look at, for example, I think it's… System… which one is it?
Unknown part type, input messages unknown part type.
Yep.
And if you expand the whole file.
So, this change to the schema makes it so that this document gets flagged as invalid.
Whereas before, That wasn't… The case, there's a bunch of them in here, the other one is like If you had…
**Trask Stalnaker (Microsoft Corporation)** 10:25 And that's because, search results is not one of our defined types.
**Aaron Abbott (Google LLC)** 10:32 Exactly, yep.
**Neil Yashinsky** 10:35 Great question, Trask, thank you. That's exactly what I was wondering. Well, I was gonna ask it half as smart, but yeah, thank you.
**Aaron Abbott (Google LLC)** 10:41 Yeah.
And there was one where, if you scroll down a little bit.
**Neil Yashinsky** 10:45 Can you say a little bit more, maybe, Aaron, about, like, how that works, and, like, where the… so the type, maybe… you said, or Trash said was not defined, or was defined, that was the validation, and maybe, like, where that is defined? Where it would check to see if that is or is not defined?
Thanks, Zach.
**Aaron Abbott (Google LLC)** 11:03 Well, yeah, I mean, it's all in the… Actually, Trask, maybe I can share?
**Trask Stalnaker (Microsoft Corporation)** 11:08 Yeah, that would be awesome.
**Aaron Abbott (Google LLC)** 11:10 Okay, sorry.
**Neil Yashinsky** 11:11 Hopefully that's not a dumb question.
That was like kind of underlying. Yeah, yeah, okay, okay.
**Aaron Abbott (Google LLC)** 11:17 Okay. So… This… This is what we have right now. We just let anybody put… you all can see my screen, right?
**Trask Stalnaker (Microsoft Corporation)** 11:28 Yeah.
**Aaron Abbott (Google LLC)** 11:29 Okay. Right now, we just let anybody put anything.
In… in the parts, so… The goal was to allow people to extend stuff, so for example, like, if an API adds a new thing that's not in the Semantic Conventions, they can still put it in the JSON schema, and it will pass.
And that's totally fine, the goal is fine, but the implementation was such that if this was.
type text, and then you put stuff that wasn't supposed to be text, which is defined in the Semantic Conventions, it would allow that, right?
**Neil Yashinsky** 12:00 Right.
**Aaron Abbott (Google LLC)** 12:01 Yeah, so the change here is… To basically add more structure, so that type generic, with generic type lets you put whatever stuff that you want without interfering with the other ones, if that makes sense.
**Neil Yashinsky** 12:15 Definitely.
**Aaron Abbott (Google LLC)** 12:15 Does that answer your question?
**Neil Yashinsky** 12:17 A billion percent, yeah, no, I appreciate that very much, and I think that makes your, you know, really clear how much better it is to do it this way.
**Aaron Abbott (Google LLC)** 12:28 Okay, cool.
**Trask Stalnaker (Microsoft Corporation)** 12:29 John Murcott, So, generic type is freeform, it can be anything.
**Aaron Abbott (Google LLC)** 12:33 Yes, yeah.
It's like the follow-through or the escape hatch.
**Neil Yashinsky** 12:39 Oh, and maybe what's defined out of the box? Are there things that are defined? Is that search one that you showed, that format, or is there anything else?
**Aaron Abbott (Google LLC)** 12:46 Yeah, I mean, that doesn't change in this PR. So I actually added, if you look at the stack, there's a bunch of valid documents here which were added. Some of them are invalid. So you can look at these and see what was allowed before and after.
**Neil Yashinsky** 12:59 Hey, yeah.
I would like not questioning, I just like thought that was a useful part of illustration, the use case. Yeah, yeah, thanks.
**Aaron Abbott (Google LLC)** 13:05 Yeah, yeah, no problem. So basically, we have, like.
tool calls, I can actually just show you the schema.
helpful.
So it's defined… it's defined in this Pydantic thing, which I think is a little bit easier to read than a JSON schema document, but there's basically… Yeah, there's basically… Somewhere down here.
Oops, sorry.
Yeah, these… these are the defined ones.
**Neil Yashinsky** 13:53 Hmm.
**Aaron Abbott (Google LLC)** 13:55 Yeah, so most providers support… yeah, most of these are supported by at least one provider. Or, sorry, at least two providers.
**Neil Yashinsky** 14:06 That's super helpful. Thank you so much.
**Aaron Abbott (Google LLC)** 14:08 Yes.
Cool, any questions, or… that's pretty much all I had.
**Trask Stalnaker (Microsoft Corporation)** 14:19 Yeah, that helped me. Thank you.
**Aaron Abbott (Google LLC)** 14:22 Okay.
Josh, do you want to share again, or do you want me to go back to the doc?
**Trask Stalnaker (Microsoft Corporation)** 14:28 If you're… if you're up for it.
**Aaron Abbott (Google LLC)** 14:31 Sure.
I mean, I think that was all the agenda today, unless… We could go through, these kind of updates.
people on.
**Trask Stalnaker (Microsoft Corporation)** 14:43 Yeah, anybody have any updates they want to share, or anything they want to call attention to?
**Aaron Abbott (Google LLC)** 14:57 Nope.
I don't know if we discussed this one last time, but the, the token usage histogram. Pr.
I think we probably did discuss this one last time, right?
**Trask Stalnaker (Microsoft Corporation)** 15:18 Can you open it?
**Aaron Abbott (Google LLC)** 15:20 Yeah.
**Neil Yashinsky** 15:21 I recall it being our favorite, but I could be wrong.
**Trask Stalnaker (Microsoft Corporation)** 15:27 There's a few.
**Aaron Abbott (Google LLC)** 15:31 This one, sorry, the field operations.
I approved this one, like, right before the call. I think this is fine.
**Trask Stalnaker (Microsoft Corporation)** 15:42 Okay, and this was the one we left… Ludmilla left a comment to align it. Did that happen already?
**Aaron Abbott (Google LLC)** 15:52 I think so, she approved it… Let's see when she approved… Four days ago, so maybe…
**Trask Stalnaker (Microsoft Corporation)** 15:58 Okay, yeah, yeah, looks like… They did… okay.
**Aaron Abbott (Google LLC)** 16:04 Yep.
**Trask Stalnaker (Microsoft Corporation)** 16:05 Cool, that is 536.
**Aaron Abbott (Google LLC)** 16:09 Yeah, I'll put it in the notes too.
**Trask Stalnaker (Microsoft Corporation)** 16:14 Yeah, I can… Look at that and merge it.
**Aaron Abbott (Google LLC)** 16:21 Cool.
**Trask Stalnaker (Microsoft Corporation)** 16:23 Let's see, it should be on our… oh, look at that, it is on… it's the one PR waiting on maintainers on the PR dashboard.
Love when that works.
Alright, I'm just gonna hit merge on that.
**Aaron Abbott (Google LLC)** 16:43 Cool.
Yeah, anybody, if you want to share updates, otherwise, I guess… And call it there.
**Neil Yashinsky** 17:04 May… maybe just… Oh, sorry! Go ahead, Trask, what you can say.
**Trask Stalnaker (Microsoft Corporation)** 17:09 I was gonna suggest pulling up the.
PR dashboard and looking at… I was just looking at the PRs that have one approval.
So, the one…
**Neil Yashinsky** 17:21 gonna.
**Trask Stalnaker (Microsoft Corporation)** 17:22 on reviewers.
That have one approval already.
Those are probably good ones for us to target.
**Aaron Abbott (Google LLC)** 17:32 Yeah.
A couple MCP ones.
Are any of these, jumping out to you, Trask? Like, the ones that are in scope for the stabilization?
**Trask Stalnaker (Microsoft Corporation)** 17:51 So I was gonna look at ones with the third column that have a green checkmark.
Yeah.
Yeah.
This one.
**Aaron Abbott (Google LLC)** 18:01 soon.
**Trask Stalnaker (Microsoft Corporation)** 18:06 Clarify this.
**Aaron Abbott (Google LLC)** 18:07 one, maybe.
**Trask Stalnaker (Microsoft Corporation)** 18:08 Usage totals, yeah, can we look at that?
**Aaron Abbott (Google LLC)** 18:12 Yep.
Yeah, I think… Maybe I'll see if Pranav can take another pass, because he's implementing this in JS right now.
But yeah.
**Trask Stalnaker (Microsoft Corporation)** 18:41 Okay, yeah, I will look at this one. Also, this is… Yeah, I had missed that. That's a good one.
**Aaron Abbott (Google LLC)** 18:53 I'll paste the notes, too.
**Neil Yashinsky** 18:58 Where was the, where was the view you show of the three columns, a moment ago? With the… that show that we had.
**Trask Stalnaker (Microsoft Corporation)** 19:06 Yeah, if you go to the issues, there's a pinned issue at the top of the issues list called Pull Request Dashboard.
**Aaron Abbott (Google LLC)** 19:23 Yeah, I also put in the notes.
**Neil Yashinsky** 19:33 Perfect. Thank you so much.
**Trask Stalnaker (Microsoft Corporation)** 19:35 Yeah.
**Aaron Abbott (Google LLC)** 19:37 Yes.
**Neil Yashinsky** 19:38 A dumb question, or if you will, is this view… Oh, okay, I see it, I see it. Okay, thank you.
That is the Stabilization Wave 1 for people keeping score at home in the Semantic Conventions Working Group document. Is that right?
What we're showing is just a different, like, you have to scroll all the way down.
**Trask Stalnaker (Microsoft Corporation)** 20:00 Oh, no.
**Neil Yashinsky** 20:02 Have you?
**Trask Stalnaker (Microsoft Corporation)** 20:04 This, this is an issue… this is, like, a tracking issue that's automatically updated. We have some automation that keeps it updated, and it's sort of like a view… overall view of the repo… all pull requests in the repo.
**Neil Yashinsky** 20:19 Oh.
**Trask Stalnaker (Microsoft Corporation)** 20:20 Sort of.
**Neil Yashinsky** 20:20 Not hot.
**Trask Stalnaker (Microsoft Corporation)** 20:22 Yeah, it's not limited. We don't have a label. We could add a label for the Stability Wave 1 if we wanted to and expose it here, actually.
**Neil Yashinsky** 20:33 I see.
That's what I conflated. I thought it was specific, but it's not, but it's just… it's just… or I thought it was correlated, but it's just conflated.
So that'd be the.
**Trask Stalnaker (Microsoft Corporation)** 20:43 Yeah. Yeah.
**Neil Yashinsky** 20:45 I correlated what was… or I causality what was correlated. Okay, thank you, sorry. But this is still a great, view, I think. Either way.
**Trask Stalnaker (Microsoft Corporation)** 20:53 Let's see, we've got Dylan's yeah, yeah, yeah. I was just pulling that up too.
**Dylan Russell** 21:00 Yeah, that's…
**Aaron Abbott (Google LLC)** 21:00 Still in the GPS.
**Dylan Russell** 21:01 Pretty… pretty simple. It's just switching this event to be recommended.
And that way we can… Use, like, the generic config to… There's, like, existing… logging… like, disablement.
To, like…
**Trask Stalnaker (Microsoft Corporation)** 21:23 Get rid of it.
Yeah, so what's the severity level?
Today, for it.
**Dylan Russell** 21:32 We just changed it to debug.
**Trask Stalnaker (Microsoft Corporation)** 21:36 Perfect. Okay.
Let me see where that is. Debug. Yeah.
All right.
I'm gonna approve that.
And merge it.
**Aaron Abbott (Google LLC)** 21:56 Do that.
**Dylan Russell** 21:58 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 22:08 Next one, is… One of Aaron's…
**Aaron Abbott (Google LLC)** 22:15 Yeah, these… these are the ones that I… these were in the,
**Trask Stalnaker (Microsoft Corporation)** 22:18 These are the stacked plans.
**Dylan Russell** 22:19 through them.
**Aaron Abbott (Google LLC)** 22:21 Yeah, this just shows, these are just like some test files that I added for.
For basically the parts that you can see, the thing that I showed before, it's just the infrastructure for it.
**Trask Stalnaker (Microsoft Corporation)** 22:33 Okay, so this first one doesn't… change anything…
**Aaron Abbott (Google LLC)** 22:39 You know, these are… Yeah, these two are both editorial, I guess you'd say.
**Dylan Russell** 22:45 you.
**Trask Stalnaker (Microsoft Corporation)** 22:46 Nice, okay. Yeah.
**Aaron Abbott (Google LLC)** 22:49 They're just adding some tests.
**Trask Stalnaker (Microsoft Corporation)** 22:50 So, the second one… Okay, cool. I can.
Sam Miller, gloss over those two, after this call, and add a second approval, and merge those.
**Neil Yashinsky** 23:09 I was just gonna… yeah, I can do the same.
**Trask Stalnaker (Microsoft Corporation)** 23:11 Oh.
**Neil Yashinsky** 23:12 Yeah, yeah. You're some admin, or, like, you don't want to have all the commits in your name, Preston, I'll do it right now.
**Trask Stalnaker (Microsoft Corporation)** 23:18 No, no, go for it.
**Neil Yashinsky** 23:20 I'd be happy to. Yeah, would love. That's 5… the whole stack. Aaron, 583 through 586, is that right?
**Aaron Abbott (Google LLC)** 23:27 Well, the top one is the real change, this one.
**Neil Yashinsky** 23:31 Okay, I didn't know if they would all need a review, approver, or just the 583 is the last one.
**Aaron Abbott (Google LLC)** 23:38 Yeah, I mean, please take a look at 5A… so they're out of order, sorry. Yeah.
**Trask Stalnaker (Microsoft Corporation)** 23:42 Stacks, you gotta read these stacks from the bottom up.
**Neil Yashinsky** 23:47 Right, okay, so here, 83686 and 84, all together.
**Aaron Abbott (Google LLC)** 23:53 Yep.
**Trask Stalnaker (Microsoft Corporation)** 23:54 Yeah, but the 8.3 and 8.6, the first two, are, not spec changes.
They're just adding test cases.
**Aaron Abbott (Google LLC)** 24:05 Let's do something like this.
**Trask Stalnaker (Microsoft Corporation)** 24:07 So those are… those are uncontroversial, so if you look at those and approve them, if they look good, then I can merge those.
pretty freely. The last one is the one where I think Ludmilla had left some comments, and we have zero approvals on, so that one… yeah, if you look at it and have thoughts, that would be great to post on there, but that's not one that I will… Be able to merge today.
**Neil Yashinsky** 24:36 Yeah, no, just figured out, like, wherever I can help most.
Happy to help. Yeah, I'll do it.
**Trask Stalnaker (Microsoft Corporation)** 24:43 Thanks.
**Neil Yashinsky** 24:44 Of course, happy to help.
**Aaron Abbott (Google LLC)** 24:46 Cool.
I think that was all the ones from this list we already talked about. Sorry. I think that was all the ones with any approvals that were waiting on maintainers or sorry, waiting on reviewers.
I guess some of these… let's see… This… yeah, some of these are really out of date. Let's see if there's anything up to date, but just…
**Trask Stalnaker (Microsoft Corporation)** 25:09 Yeah.
**Aaron Abbott (Google LLC)** 25:12 This one I think I blocked because it's kind of overlapping with the one I had. It's basically the thing that Lydmilla suggested, so no need to take a look at that one right now.
Yeah, there's this one.
which me and Ludmilla both approved.
Yeah, this was a really small change. I don't know if… I think the open stuff.
Was pretty nitpicky, yeah.
So, feel free to review this one, too.
And… Yeah, I think, I think that's pretty much it, right?
**Trask Stalnaker (Microsoft Corporation)** 25:56 Yeah, what is that? Climate is a logical operation.
There's… How does it say I commented on it?
**Aaron Abbott (Google LLC)** 26:12 Did you?
No.
But you did.
**Trask Stalnaker (Microsoft Corporation)** 26:16 Oh, okay, we were discussing this.
Oh, yes, yes, I remember this one. Yes, okay.
Okay, yeah, let's let that one sit a little bit, or maybe we can get Felix's… input, still.
**Aaron Abbott (Google LLC)** 26:32 Yep.
**Dylan Russell** 26:34 One question on the generic part thing, now that I'm thinking about it.
**Aaron Abbott (Google LLC)** 26:39 Yeah.
**Dylan Russell** 26:39 Should we… is there some way to validate that the… Values are any values.
in the Json schema.
Cause… I think, ultimately, these things all become attributes, and attributes have to be, like, in any value, which is, like… You know, in spool… whatever list.
**Neil Yashinsky** 27:04 ones.
**Dylan Russell** 27:04 Dict.
**Aaron Abbott (Google LLC)** 27:06 You mean, like, serializable?
**Dylan Russell** 27:08 Yeah.
**Aaron Abbott (Google LLC)** 27:09 Oops, sorry.
**Neil Yashinsky** 27:10 Oh, no, I apologize for interrupting. I was just gonna say, do you mind asking your question from the very beginning? Or restating your question?
**Dylan Russell** 27:17 Yeah.
Can we make sure the JSON schema, the types that we have, the part types, are… All… Like, types that we can…
**Neil Yashinsky** 27:31 Fine.
**Dylan Russell** 27:35 turn into, like, an any-value type, because they just go on to attributes, which has to be, like, an OTEL any-value thing.
**Aaron Abbott (Google LLC)** 27:45 I mean, I think…
**Trask Stalnaker (Microsoft Corporation)** 27:46 wouldn't… What's an example of something that couldn't be…
**Dylan Russell** 27:52 Serialized changes.
**Trask Stalnaker (Microsoft Corporation)** 27:53 value.
**Dylan Russell** 27:55 Well, we were letting like a, I think we had things defined as type any.
Which is, like, what is that? What is an any type?
**Trask Stalnaker (Microsoft Corporation)** 28:06 In Semantic Conventions? Like, in OpenTelemetry?
**Dylan Russell** 28:13 Like…
**Trask Stalnaker (Microsoft Corporation)** 28:13 and… Like, at the OTLP layer, any?
value, any value.
**Aaron Abbott (Google LLC)** 28:26 So this is like the JSON spec, I think.
**Dylan Russell** 28:29 Okay.
**Aaron Abbott (Google LLC)** 28:29 Any valid JSON would technically be valid.
Any value, because it's…
**Dylan Russell** 28:33 Okay.
**Aaron Abbott (Google LLC)** 28:34 It's bool. I think we have the null. We have a spec for null for any value now. I think it's just an empty.
with none of the, one offset, and then number string array object. There's no, like, date Or anything like that. Okay. Yeah.
**Trask Stalnaker (Microsoft Corporation)** 28:54 I'm looking for, back here… Thank you.
This might be what you're looking for…
**Dylan Russell** 29:12 Having arbitrated… well, that… Basically, I just want to make sure that whenever we define a part.
We, like, define the types… Like, it's very easy to, like, write code that will… Like… turn into that OTLP any value type.
**Aaron Abbott (Google LLC)** 29:40 Yeah.
**Neil Yashinsky** 29:41 Hail open.
**Trask Stalnaker (Microsoft Corporation)** 29:46 I don't know what the Python API looks like for that. I know in the… I think in the… Java… We have, like, kind of some convenience methods for taking arbitrary… maps and lists of maps. We don't… do we do from JSON? I don't know, but, like, and converting them to… any value.
So it may… may need, like, a common… Convenience, utility.
**Dylan Russell** 30:20 Yeah.
Yeah, Ludmilla has been writing something for, like, tool arguments and results.
**Aaron Abbott (Google LLC)** 30:27 Because…
**Dylan Russell** 30:29 That could just be any arbitrary, like, Python object.
So we're sort of figuring out how to deal with those things.
I.
**Aaron Abbott (Google LLC)** 30:43 I guess it wouldn't be part of the JSON schema though, right? Like it would be.
more part of the text of the Semantic Conventions explaining, like… like, for example, we had this bug in Python where somebody reported any value with a self-referential object having a recursion error.
But, like, generally, it would be kind of useful to have a spec on how to handle self-referential objects being serialized to any value.
Or, like, date types, I guess, but… Yeah.
Does that make sense, Dylan? I guess I'm saying it seems like more generic any values problem than the… GenAI problem.
**Trask Stalnaker (Microsoft Corporation)** 31:29 Yeah, GenAI is sort of the first… Big user of any value.
So it becomes our problem.
**Dylan Russell** 31:41 Yeah.
Yeah, I think it's probably more just a thing to look at when you're reviewing, like, semantic conventions. It's like… Whatever the proposal is, we have to convert To this value, at the end of the day.
So, like… Yeah.
**Trask Stalnaker (Microsoft Corporation)** 32:04 If it's JSON, like, for response objects, I'm assuming they're already in JSON structure?
Or are they Python objects that we're converting to… Any value?
**Dylan Russell** 32:18 Some of them are JSON, some of them are Python objects.
**Trask Stalnaker (Microsoft Corporation)** 32:21 Okay, because JSON to any value should be straightforward.
**Dylan Russell** 32:28 Yes.
**Trask Stalnaker (Microsoft Corporation)** 32:31 Python objects… Yeah, then it's like, well, what are properties there? What do we serialize? Yeah, there's open questions.
**Dylan Russell** 32:41 Yeah.
Yeah, what I said on that is… Yeah, I mean, one… never mind. I don't know if we wanted to get into that, but there is an open PR in the GenAI repo to… Figure out the best way to do this serialization, if people are interested.
**Aaron Abbott (Google LLC)** 33:04 You might just drop in the PR in the notes, and we can take a look.
**Dylan Russell** 33:07 Sure, yeah.
**Trask Stalnaker (Microsoft Corporation)** 33:13 And I think for date… dates format, I think we have something in the general SEMCOM repo.
About how dates are supposed to be… Formatted…
**Dylan Russell** 33:33 That would be good, because this PR is… Doing something with dates, in particular.
**Trask Stalnaker (Microsoft Corporation)** 33:40 Yeah, I mean, if it's… again, if it's, JSON.
to any value.
I would assume you would just use… I mean, JSON doesn't have dates, so you would just… it would just be mapping whether it exposes them as strings or as… numeric values. We would just… Pull that in directly.
**Aaron Abbott (Google LLC)** 34:03 Yeah, but it's basically… String… string numeric value.
**Trask Stalnaker (Microsoft Corporation)** 34:08 Yes, yes. No, not that. I mean, I guess, yeah, if that's what it is in the JSON data, that's what we would capture.
**Aaron Abbott (Google LLC)** 34:17 I mean, that's like how OTLP does the Unix timestamps because they're in JSON, 'cause they're 64 bits, so they won't fit in JSON, yeah.
**Trask Stalnaker (Microsoft Corporation)** 34:31 But yeah, if it's a Python date object that you're serializing, then we have to make a decision there.
**Dylan Russell** 34:38 Yeah, I think she used, like.iso format.
**Aaron Abbott (Google LLC)** 34:43 Makes sense, yeah.
**Trask Stalnaker (Microsoft Corporation)** 34:46 Yeah, I think that's that 8601 is… think what we… But check this MCOM repo. I feel like this has come up before.
**Aaron Abbott (Google LLC)** 34:58 Yeah.
**Dylan Russell** 35:00 Alright, that's a good idea.
**Aaron Abbott (Google LLC)** 35:06 Okay.
Cool.
**Trask Stalnaker (Microsoft Corporation)** 35:08 I think it's date to string because we didn't have this. I think it predated any value.
**Aaron Abbott (Google LLC)** 35:14 Hmm.
**Trask Stalnaker (Microsoft Corporation)** 35:16 Or I guess we had to decide numeric or yeah, it is any value essentially.
Awesome, thanks for driving the second half there, Aaron.
**Aaron Abbott (Google LLC)** 35:30 Oh, yeah. No problem. No one's working on it.
**Neil Yashinsky** 35:32 work.
Thanks, everyone.
Appreciate the leadership.
**Dylan Russell** 35:36 Yes.
**Max Ind (Google LLC)** 35:37 Thanks.
