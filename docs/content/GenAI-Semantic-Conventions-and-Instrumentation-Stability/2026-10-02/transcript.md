SIG: GenAI Semantic Conventions and Instrumentation Stability
Date: 2026-10-02
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Wolfgang Therrien** 02:15 Hello.
**Liudmila Molkova** 02:17 Hey, how's everybody doing?
**Wolfgang Therrien** 02:20 Doing okay, doing okay.
**Liudmila Molkova** 02:26 Awesome.
Let's get to the stabilization.
**Wolfgang Therrien** 02:35 Thanks, Ludmila, for taking a look at that 447 PR the other day.
The I appreciate it.
The agent, agent interaction stuff.
**Liudmila Molkova** 02:48 Oh, okay. Are you interested in it?
**Wolfgang Therrien** 02:52 Yeah, I was, I was, looking, looking to review that, but I was unexpectedly away last week.
**Liudmila Molkova** 02:58 I'm.
**Wolfgang Therrien** 02:59 some of this week, so I appreciate you moving it forward. So, I'm gonna see what you had to say and re-review it, because I see that there was a lot of updates there, too. So, hopefully that one can move along.
**Liudmila Molkova** 03:12 Yeah, I'm, like… I'm a little bit blind there, so, like, if you think… if you have experience with it, and you think that I'm wrong, I would be excited to hear.
Okay…
**Wolfgang Therrien** 03:29 I feel like I'm still leveling up in a few areas here, so.
**Liudmila Molkova** 03:33 Yeah, right? Yeah. We don't know everything about GenAI.
**Wolfgang Therrien** 03:37 Not yet, not yet. Hopefully, hopefully by November, right?
**Liudmila Molkova** 03:40 Right, by November we'll know everything.
**Trask Stalnaker (Microsoft Corporation)** 03:43 For sure.
**Wolfgang Therrien** 03:45 And after that, certainly no new information will need to be generated.
**Liudmila Molkova** 03:49 No.
From Danny, I will take over.
Okay, so… from the last time… I think we were going to do a couple of things, First, I don't know, but I believe there is no changes in the PR reviews.
I would like to go through them, but also we wanted to chat about the agent versus workflow.
If we are ready.
But maybe let's go through the board and see… oh, sorry, through the… this dock and see if anything has changed.
Is this how you intended for it to work, Trask? Or, like… Okay.
**Trask Stalnaker (Microsoft Corporation)** 04:48 I didn't have a super strong intention. I was trying to kind of add statuses to things wherein there was… anything to report.
**Liudmila Molkova** 05:06 Okay.
**Trask Stalnaker (Microsoft Corporation)** 05:07 So, I know that, like, Wolfgang hasn't probably had a chance to update on the… I think, what were you… You are looking at the agent identity hierarchy stuff.
**Wolfgang Therrien** 05:25 Yeah, I started digging into that. It looks like a bunch of stuff is merged and in. I think 91 still needs a PR, and I was trying to understand sort of what the open questions were there. And the two that came to mind that we can maybe talk about is like what the mechanism is for carrying agent name.
to child spans, but I think at this point, it's, context attributes is what we want folks to be reaching for, and not something like baggage.
Okay.
**Trask Stalnaker (Microsoft Corporation)** 05:56 Definitely not baggage.
Contacts attributes would be great if we have context attributes, but I think we, had discussed previously that we would be okay with it being also sort of an ad hoc contract within the Python GenAI repo.
**Wolfgang Therrien** 06:19 Okay, so maybe the recommendation is that if use… Context attributes, if it's available, but otherwise, You know, homegrown is fine if you don't have that.
**Liudmila Molkova** 06:33 I think, like, what we talked about, that we want a special case two, for now, attributes, and we don't want to grow this list, at least uncontrollably. And that's the conversation ID and the agent name.
And we would, at least we already merged the conversation ID, and we didn't say… Oh, we did? Yeah.
Sorry if I… if it was unexpected.
**Trask Stalnaker (Microsoft Corporation)** 07:00 No, no, no.
So that we are propagating that.
the… down.
**Liudmila Molkova** 07:07 Yeah, we didn't say that we are propagating it down. I think we're saying if available and we'll leave the propagation mechanism.
**Trask Stalnaker (Microsoft Corporation)** 07:15 Okay.
**Liudmila Molkova** 07:16 unspecified… Here.
**Wolfgang Therrien** 07:20 Okay, so it's, so that is, what we want to do similarly for agent name is to say that it is.
You know, conditionally required if available, but not necessarily specify the mechanism.
**Liudmila Molkova** 07:36 Recommended, or conditional, or required, or… Oh, we see something!
Or maybe… oh, we just edited, that's an existing note. There is an issue, and even a PR… Yes, this France. We created a tracking issue to document this couple of attributes, and maybe this could be a good place where we say.
A little bit about, Mechanism.
**Wolfgang Therrien** 08:17 Oh, okay, alright.
Is this…
**Liudmila Molkova** 08:22 I'll link.
**Wolfgang Therrien** 08:23 Yeah, okay, I'll link that to this issue. Yeah, because there was a couple of comments that Mike had made earlier, but the universe has certainly shifted since, I think, May, so I'm just trying to… reconcile.
Sort of what was what was mentioned there.
Okay, cool.
**Trask Stalnaker (Microsoft Corporation)** 08:55 and.
**Liudmila Molkova** 08:56 Okay.
**Trask Stalnaker (Microsoft Corporation)** 08:59 We need, we need one more, approval still, or review and approval for the naming the… Inference, operation, basically the operation span type split out.
And metric split.
That's blocking, Further progress in that area.
**Liudmila Molkova** 09:27 Yeah.
So, maybe we should talk about this. Aaron… Aaron is not here today. Okay. Aaron raised a concern, a mild concern.
Because of the discussion we had about inference separation and whether inference is the right name.
And I've been thinking about it.
There is an issue I think Felix created.
And.
this print.
At.
And the concern, if I understand it, that this is not the real insurance.
And maybe this is the real inference, but.
Who even knows what the real inference is?
So I've been thinking about it and trying to come up with some other name.
I think chat is the… not the good name. It's not a generic name, it's a legacy and provider-specific thing. And I've been trying to come up, okay, if we can find a name that's reasonably good, then I think we could consider a rename.
But a couple of things I came up with that are reasonably good have exactly the same set of problems.
Umm.
The generation maybe is interesting, but still, it's… Like, is it one generation?
Sounds like one, but there could be multiple under, and my point is that The model APIs pretend it's an inference, even though they run complex Agentic workflow. They pretend it's an inference.
So… I… I think we are in the same position with pretty much any distributed application. For HTTP, we have nested HTTP calls. They are two different places.
And I don't think we should rename inference.
**Neil Yashinsky** 11:56 Yeah.
**Liudmila Molkova** 11:56 We can…
**Neil Yashinsky** 11:58 Oh, sorry, Ludmila, I was gonna say, I agree broadly with everything you said, and I feel like until we have something better.
you know, to finalize on, to just move from one thing that's not perfect to something else that's not perfect is not enough of an improvement, I guess, to justify, you know, doing something.
So, and I think you're… It seems like, in some ways, the vendors, if you will, are still trying to figure this out themselves.
There's a lot of flux or whatnot in the… in how… how it's being called, and so… Yeah, I don't have… I don't have anything better. Oh, please, Emil, bail me out.
**Emil F** 12:38 No, I'm kind of strongly agreeing. I think that the knowledge of what is the real inference is immaterial in this case.
Like, if further down the line, people really want to disambiguate between the inference that is being presented as an inference and the inference that, you know, people in the know that inference, we can… it can be amended. But I think for the time being, inference is good enough.
**Wolfgang Therrien** 13:06 And just so that I'm understanding, the issue or the concern is that it's not technically, it's not technically correct, because the inference could actually be happening, you know, further down. But even though colloquially, we all just… it's sort of bucketed as inference.
But we don't have a name that's necessarily better, just different.
**Liudmila Molkova** 13:29 Yeah, so like what we call inference, client inference is this friend.
**Wolfgang Therrien** 13:32 So.
**Liudmila Molkova** 13:33 And there are multiple… Underlying conference calls, server toll calls, guardrails, content filters, authentication, and all this other crap that's going on behind the scenes.
**Wolfgang Therrien** 13:46 Yep.
Yeah, I don't think we should name it to something different unless it is solving a, like, a problem with representation, or that the new thing is clearly I'm… More, a clearer better name.
And it doesn't sound like that's the case.
**Neil Yashinsky** 14:08 I wonder, is there, is there such a thing as like, Like, how a convention is, if you will, too early to be properly defined, but… to have a sort of, like, a definition of sorts, or requirements, I guess, defined for what, once we have it, it would do.
Because I, you know, I'm looking at the name, and it's like, it is somewhat clear That… that they should be separate?
And I hate to be like pedantic or whatever, but I feel like in some ways maybe if we defined like the primary objective of the identification, at least we kind of settle on what's important.
As a means of, like, furthering discussion, even though it can't be decided now, but, like, you know, the solution of the future will have this flavor, or whatever, will be able to provide this benefit.
Does that make sense?
**Trask Stalnaker (Microsoft Corporation)** 15:07 I mean…
**Liudmila Molkova** 15:07 Tracking.
**Trask Stalnaker (Microsoft Corporation)** 15:08 Issue that we come back to later.
**Neil Yashinsky** 15:12 Yeah, more or less.
With maybe, like, some notes on, like, what We're missing at the moment that we can't… the reason we can't settle this is, you know.
At the moment, there's a lot of ambiguity across vendors, there's… and we haven't found the right I guess, convention, if you will, to… to… consense around? Is that a… is that a verb? Can we consense, or build consensus around? And so in the… when we… when we develop that consensus, it should do, you know, X and Y. Thus.
Enabling, you know, this insight or this analysis.
**Liudmila Molkova** 15:48 And… Maybe what we miss is a notion of real inference and what it is.
And.
I can document this.
And the issue, here… But all we need is a way to distinguish the perceived, the client-side inference from whatever real one is that's done by the model process itself, essentially, right? Only the model knows that it does the inference.
We can always have some distinguishing factors.
I'm.
It can be spankind, it can be something else, a different name for the real inference.
But… I, I think what I want to avoid is us keeping this in limbo.
Yeah. And we would make a call, and I don't think we will change it after. It's not worth it, like, the bike shedding on the… and changing the names without any reasonable semantics.
**Neil Yashinsky** 16:51 Yeah. Well, I guess in that context, then, it doesn't seem like… It's not a bad choice, what's proposed.
As a kind of… I'm not trying to, you know, criticize the PR or the, you know, the requirements or whatever, I just… just trying to reflect what I… what seems like the… Fluid nature of the data, the underlying data and the structures that we're trying to, if you will, govern.
I'm not trying to cause complications.
**Liudmila Molkova** 17:24 Thank.
**Trask Stalnaker (Microsoft Corporation)** 17:24 And as the space You know, matures, there may… New names may mature, new terminology may… happen. There may be… a consensus at other, you know, I'm thinking of, like, the… the A… the, AAIF, the, the Linux Foundation Agentic AI, they're, you know, working on terminology and, taxonomies and things. So someday we may have, you know, something that we can lean on. And, you know, that would be a good justification for making changes. Right.
the future.
Certainly we can always add an attribute to these inference spans if we find that, you know, this distinction is important and somebody wants to capture the difference.
I would say for now, just a PR where we state that inference spans may either be this outer inference, like the call, or it might be an inner actual inference.
Oh, it's probably already… clear, given that it's mapped, I think, generally to the OpenAI the, the normal… chat response…
**Liudmila Molkova** 19:01 It doesn't… it's not hurt… doesn't hurt to clarify.
That it does not imply a single inference.
On the model side, and retries and, like, internal details of the server, we don't know.
**Trask Stalnaker (Microsoft Corporation)** 19:19 Yeah, yeah, I agree, because normally, I mean.
It's inference to the client. You get back the number of tokens you used.
That's… that's inference from a client's perspective.
It's just a more advanced inference.
**Liudmila Molkova** 19:38 Yeah.
Maybe we should also talk about this a little bit. I'm going to postpone Agent versus workflow, because Surya wanted to prepare something and they don't see him.
But one of the problems this.
This issue raises is token usage and the nesting of the token usage.
That… If we report it here, and report it here.
Then somebody who naively sums up token usage across different spans would double counter.
Triple count, or whatever.
I'm.
I think this is the variation of another problem we need to solve, and… Number 19.
And this is the problem for the agents.
Where there is a proposal to use a different attribute name on the agents.
And I wish, like, Felix also commented here, and I wish Felix or Alex were here to talk about it.
But.
Umm.
Like.
It's just kicking the problem up the… the stack.
Right? You, like, it's just, we can never guarantee that summing up tokens across different spans is meaningful.
You always need to filter the specific span or metric.
**Neil Yashinsky** 21:21 I'm not sure I… fully follow, Neil, so forgive me if I'm… if I'm missing something here, but it seems like by having a named, aggregate that you… Yep.
Specify the right place to do it. And that is clearer than… than nothing.
And so, you know, it's a… it's a direction of how it should be done.
Which I think is better than… people… You know, figuring out how to do it on their own without, you know, in a vacuum.
And I think that the… I guess the… what is it called? The total, in particular, I think is the most important to have a spot for, since that will be reliably important to track across.
**Liudmila Molkova** 22:14 The trick is that you never, like, the instrumentation, the stateless one doesn't know what.
If you represent a total.
You only know that either… You got this from, let's say, a server. If you run the client agent or inference client call.
And you got them reported.
Or you know that, okay, you're an agent workflow, something higher level, and you collected it from the underlying calls.
R.
But even with just the inference.
As we just discussed, you don't know how many inferences are under you. With agents, you don't know how many agents are under you or above you.
**Wolfgang Therrien** 23:03 Right.
**Neil Yashinsky** 23:06 That's… that'll always be true, and I feel like, excuse me, the presence of a namespace, I guess, for lack of a better term.
is… Concrete step.
That will allow… a distinct use for a distinct purpose, and that's why I think there's value, but it's not, you know, this is a hill, it's not really important, it's just, like, that's my perspective, so… Yeah, take it, you know, 2 bucks with that, we'll get you… actually, 4 bucks, I guess, he says, we'll get you coffee, so, you know, take it for what you will.
**Trask Stalnaker (Microsoft Corporation)** 23:43 For agents, differentiating agents, tokens on agents and tokens on inference.
I mean, the aggregate… namespace… I think fits… Better on… or could fit on agents.
I don't know how it would solve the… Inference… the nested inference problem, though…
**Liudmila Molkova** 24:13 I'm saying that people who… Once, like, the reason behind the change.
Is that… It somehow prevent.
A a naive mistake.
When you write the query, like, some tokens… Across all spends, right?
I guess the argument for a separation is that people would write it on the inference and would not write this query on.
Agents.
For aggregated.
It also creates problems for the client agents. What do you report? Is it aggregated?
It is not.
**Trask Stalnaker (Microsoft Corporation)** 24:56 Oh, do you get back tokens on client agent?
**Liudmila Molkova** 25:02 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 25:04 Yeah.
Yeah, I mean, it… it… Really feels like it's, like, if you want to sum them up.
you sort of… half to sum up essentially leaf… nodes of your span tree, I guess.
**Liudmila Molkova** 25:27 You sum up by.
Well, I don't think you should sum up spans to find token usage. You should use metrics.
But if you do!
You should filter to specific spend types, maybe to client spends.
At least.
**Trask Stalnaker (Microsoft Corporation)** 25:47 That still wouldn't… you'd still get duplicate on that inference.
Case, so…
**Liudmila Molkova** 25:55 Oh, and also by the service name.
Regardless.
**Trask Stalnaker (Microsoft Corporation)** 25:59 Okay.
Yes.
This makes sense to me.
**Neil Yashinsky** 26:08 I see what you're saying, Lubiela, so essentially, like, the reason that is bad is because you're kind of encouraging a practice that should really be done a separate way.
And by creating this space, you kind of encourage, I don't want to say bad behavior, but, like, not optimal behavior, is that my understanding?
**Liudmila Molkova** 26:28 Yeah, it's just we cannot guarantee anything. Like, we cannot guarantee that some of the usages across spans is meaningful, regardless of how many namespaces we create.
**Neil Yashinsky** 26:40 And so it's not really clarity, it's just… Up.
Different type of ambiguity, maybe?
Versus the clarity of just using the metric.
**Liudmila Molkova** 26:54 so, for attributes, the… I think there is some merit to having just one set of attributes.
Right? We already have, like, 25 different user attributes.
If we invent a whole new set for aggregate once.
And it would… would that solve the problem?
**Neil Yashinsky** 27:19 Right, and when there are reasonable alternatives that are as good or better, I guess maybe I didn't make that clear from your perspective, that there's a better approach to this overall.
With metrics, and so any kind of attribute creation to support this here will still always fail to be as good as the alternative.
And, and it doesn't increase clarity or Well, clarity, I guess.
And so it… so…
**Trask Stalnaker (Microsoft Corporation)** 27:48 For me, if… if aggregate namespace actually worked.
then I would… I… I… I'm kind of interested in it, because it is a foot gun. It's something that a lot of people have reported.
The problem that I… as I see it, is that the aggregate namespace doesn't solve the problem… like, solves the problem, like, maybe 70 or 80% of the problem.
But you still have, client, invoke agent client spans?
What are you gonna put on… are you gonna put aggregate?
Tokens on that, or… Raw or non-aggregate tokens on that.
**Neil Yashinsky** 28:41 And so you're saying the lack of… overall consistency is… makes it less than ideal, if I'm hearing right.
**Trask Stalnaker (Microsoft Corporation)** 28:49 doesn't.
**Neil Yashinsky** 28:50 nice.
**Trask Stalnaker (Microsoft Corporation)** 28:50 Maybe it doesn't solve the problem.
**Neil Yashinsky** 28:52 I.
**Trask Stalnaker (Microsoft Corporation)** 28:53 Like, if it… if it was a clear… like, if it solved the problem.
And we could just give that guidance to people.
Then, you know, I was kind of leaning towards the aggregate attribute initially, just because of the number of people who seemed to run into this problem.
**Neil Yashinsky** 29:13 Yeah, same.
**Trask Stalnaker (Microsoft Corporation)** 29:14 But… That we're just gonna be setting them up for thinking they've solved the problem, but they're still gonna get duplicates.
Because we don't have a solution for… Nested… invoke agent client spans, and we don't have a solution to this newer, more rare problem, for sure, the nested inference.
Client spans.
**Neil Yashinsky** 29:42 And so, because we can't cover… Server and client holistically across that whole 100%, then you're like, maybe it's just better not to do it.
Yeah. If I'm understanding. Yeah. Well, Emil, I think, has his hand up. Well, I know he has his hand up, sorry.
**Emil F** 29:56 Yeah, thank you. I'm kind of part of the school of summing up things. I think that it would work if… only the spans that are actually incurring that cost are reporting this attribute, right? So if you say only the leaf spans that are doing the actual inference and counting that you're billed for, if only they give you that cost, then something is great.
But I suspect that this might not always work. Maybe those bands are not part of the tree in this In the particular configuration, or they're not visible, and are somehow reporting the metrics to the higher level span.
Umm.
Maybe this can be instead solved with, with an attribute, like, just a Boolean flag.
That says whether the tokens that the Spanish reporting are coming directly out of it.
Or if they are… Coming from children.
Then your algorithm can become, you know, you walk to the leaves of the tree that you have.
And some kind of the, the last… Value from those leaves, either… An actual true cost that came out of the span.
Or something that was, reported, that was aggregated into a higher level span.
Does this make sense?
**Trask Stalnaker (Microsoft Corporation)** 31:21 Yeah, what I don't know is how does, like, invoke agent client span Know whether the remote side is going to be emitting.
inference spans… With the raw costs.
So how does it know it's a leaf?
**Emil F** 31:41 It only needs to know if the cost is coming from itself.
Or, I guess, if it is passing on the cost for somebody else.
**Trask Stalnaker (Microsoft Corporation)** 31:52 Oh, I see what you're saying.
**Liudmila Molkova** 31:56 I mean, we could probably f… Find the ground. Well, we are out of time, like, just let's just finish if people are comfortable.
We could probably report The usage not aggregated on the… all the client spends.
Doesn't show the nested and double counting.
But… Presume… yes, as you said, Trask, it would solve the problem in 80% of the case. Most naive queries will be fine.
**Trask Stalnaker (Microsoft Corporation)** 32:40 The other, Like, I can't… It's… I'm surprised… I guess I'm surprised how many people have run into the problem.
And so I, Because we have the same problem, right, with all spans and, like, duration.
Right, duration of spans… like, you can't add up duration of spans over nested spans, it's… it's meaningless.
And… So.
I don't know if there's… we just… we need to make a… we need to camp… put a campaign effort together to, like, an education campaign for Invoke that… to think of… Tokens as similar things that you can't… Sum up over nesting.
I don't know, I'm trying to…
**Wolfgang Therrien** 33:38 I think that's hard, because tokens have a cost, and people want to be able to say, how much is this thing? Like, how much am I spending here? Which it feels… I think to most people, intrinsically different than just how long something took.
**Trask Stalnaker (Microsoft Corporation)** 33:54 Well, that's to Emil. I think that gets at Emil's point of, like, that reminds me of profiling, where you do have that CPU cost, and you have, like, self-CPU, and then you have the sum of the CPU under you.
**Wolfgang Therrien** 34:08 Yeah.
**Neil Yashinsky** 34:16 Yeah, maybe the profiling is a good model for this, because, you know, token's an interesting one, because it's a little bit of a, you know, a cost, but it's also analogous to other things besides that. It's a… I don't want to say it's kind of loaded, I guess, or whatever? Like, the values are somewhat loaded, and… Not… uniformly used, as best I can tell.
So it's… Everyone agrees it's important, but we don't agree on what it should be used for or why. I mean, over… over…
**Trask Stalnaker (Microsoft Corporation)** 34:47 If we did do that, right, like, so what, the proposal would be… Only inference spans would… Record it as, like, self.
versus aggregate.
**Emil F** 35:01 But we're talking that inference can be like a proxy actually to an actual inference, right?
Yeah, so that's…
**Trask Stalnaker (Microsoft Corporation)** 35:09 That's, that's, that's problem number two. So.
**Neil Yashinsky** 35:12 Before you…
**Trask Stalnaker (Microsoft Corporation)** 35:12 The problem number two, let… problem number one, or… is the general proposal that we would Always do aggregate tokens on agent calls and self-tokens on inference calls.
**Emil F** 35:29 Is it actually, like, the graph that Ludmil is building here in the document?
When you do… So, when you do the inference with the LLM, right, it generates some output in the form of tokens, right? And that's the moment of billing. You've got this input tokens, and you've got this amount of output tokens.
There is nothing nested.
Or there shouldn't be nothing nested in the actual… Real call that is, that is doing the cost.
Which means that we sh… It should be possible to just sum up.
The cost of those leaves?
They're not going to have any children.
The real cost drivers.
**Liudmila Molkova** 36:20 Well, they can have.
Children, it's just not GenAI children, and it's very expensive to… Write the query.
Like this.
**Emil F** 36:31 What kind of children could they have?
Like, in your example here, the usage pieces.
That's where.
**Liudmila Molkova** 36:38 call.
**Emil F** 36:39 Most is coming out of it.
**Liudmila Molkova** 36:40 HTTP spans they would have, and you never know how many layers under you need to look, so you would need to query… you would need to get all the spans.
**Emil F** 36:53 But… The HTTP would be a sibling. It wouldn't be part of the inference, so it wouldn't be a child of the inference.
**Liudmila Molkova** 37:01 If it is a client inference, then there is a transport span under.
Which is HTTP, GRPC, whatever.
I think the only place where you know it's a real inference is inside the model, or inside the process that communicates to the model directly.
So whenever you host a model, this is where the price should come from. I'm really surprised we're in 2026, and still the providers don't report proper, like, costs metric for the models themselves. This is why we are talking about it.
**Emil F** 37:37 Okay, I see what you mean. Yeah, you're right. If it's on the client side, then it will have children.
**Liudmila Molkova** 37:43 And more importantly, you don't know if you, if it's the client inference.
There are turtles all the way down.
**Emil F** 37:52 Right, okay.
**Liudmila Molkova** 37:56 Okay, we are out of time. I'm thinking what could be a good, next steps. One good step could be I can try to draft a PR that, or if anybody else wants to, to, like, introduce aggregate usage, and we can just look at it and see… If we like it, I think this is the critical part, what we do for this sprint.
The other approach is that we need to, as Sister Ask mentioned, educate and document, maybe clarify more.
that, you cannot query by this attribute alone, you need to limit the specific span and service.
**Wolfgang Therrien** 38:37 Yeah.
**Neil Yashinsky** 38:39 Makes sense to me.
**Wolfgang Therrien** 38:43 So it sounds like there's maybe, like, eventually a blog post or some other sort of, like, durable, easy-to-consume education bit, and then maybe a prototype?
Draft PR.
**Trask Stalnaker (Microsoft Corporation)** 38:55 I mean, given how, And, like, most people want to sum up tokens over a trace.
I would suggest even a, like, in the spec itself, like, a section there that's… You know, a permanent… Documentation of that, that hopefully, over time, all the agents will…
**Wolfgang Therrien** 39:20 internalize.
**Trask Stalnaker (Microsoft Corporation)** 39:21 Yeah, exactly.
**Wolfgang Therrien** 39:25 Yeah.
**Neil Yashinsky** 39:31 you Okay, well, good conversation, I gotta run. Thanks, Lubila and Trask and everyone else for your contributions. It's always a pleasure. Have a great weekend.
**Liudmila Molkova** 39:40 if.
**Trask Stalnaker (Microsoft Corporation)** 39:41 Thank you all.
**Liudmila Molkova** 39:41 Thank you. Bye.
**Trask Stalnaker (Microsoft Corporation)** 39:43 I…
**Liudmila Molkova** 39:44 Bye.
**Emil F** 39:44 Bye-bye.
