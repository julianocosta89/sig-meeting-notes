SIG: GenAI SIG
Date: 2026-11-03
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Surya Teja 00:01:36 Hey, hi folks.
Tammy Baylis 00:01:43 Hey, Surya. Hey, everyone.
Trask Stalnaker (Microsoft Corporation) 00:01:49 I…
Liudmila Molkova 00:01:51 Hello! Hi, everyone.
Sick.
I'll Trask you're going to present, I appreciate it.
Trask Stalnaker (Microsoft Corporation) 00:02:03 Yeah… You shouldn't have to present in back-to-back meetings.
Let's see, we do have slight… Change to our schedule now. Did I call this Monday or Tuesday?
I'm gonna call it Monday,
Liudmila Molkova 00:02:29 It was both Monday and Tuesday.
Trask Stalnaker (Microsoft Corporation) 00:02:32 Yeah… Alright, please add your topic.
to Tuesday, this is Monday the 2nd.
I'll kick it off with, Steve from Alibaba had asked us to advertise these two PRs, hoping to Find other folks who are interested.
In these topics to review.
So if you have a… Use case or interest in this, please… Have a look, leave a comment.
Approval, anything.
Liudmila Molkova 00:04:01 And our topics today.
Trask Stalnaker (Microsoft Corporation) 00:04:04 Yeah, we can, look at… PRs. We've got a bunch of PRs that could use… Reviews… Let's… what would help us the most, is right now, especially for… Is getting a second green checkmark on places that have one green checkmark already.
The one problem we have is currently we don't… Allow both to be from the same company.
So… What do we have here?
I can… so I can call people out who we need, help from… Let's see, so, like, anywhere where Ludmila has a checkmark, if it's my PR, I can't approve it, and so… We need, alec… Ankit… oh, I can… Bug Ankit, yes.
Ankit Singhal 00:05:23 Josh.
Trask Stalnaker (Microsoft Corporation) 00:05:26 Mike Ming Li.
Liudmila Molkova 00:05:33 Oh, we… we didn't update this list. I think, Mike is not an approver.
And Dylan is… oh, Dylan is here. Nice.
Trask Stalnaker (Microsoft Corporation) 00:05:45 Yeah. Oh, did we not… oh, Okay, oops. We moved him to emeritus, but didn't remove him here.
I will fix that.
Liudmila Molkova 00:05:58 But Mike, we would love to have you back, if you… if you hear this.
Trask Stalnaker (Microsoft Corporation) 00:06:04 Yeah, there's automation, org-wide automation that automatically sends PRs to remove people who have been inactive for 3 months, I think.
Cool. Hey, Matt, welcome!
Yeah, let's hear what has been going on over in the AAIF.
Matt Lee (Datadog, Inc) 00:06:29 Sounds good. So, after a couple of months of just working through, the way for us to best contribute to the GenAI SIG in OTEL here, we've come up with a couple of proposals that we'd want to talk through about things that could potentially use, clarification in the semantic invention. The first of which that we wanted to talk about was this idea of a sort of turn semantic. Ludmila, I know you had a previous PR that was exploring that idea of, like, how can we have something that constitutes some input into an agent, leads to n units of work together that constitute a larger entity to sort of conceptualize. And there were some discussions about, should this be its own separate, semantic entity? Should it be attached to the sort of top level, so to speak, that, captures this, and what the best way to approach this is.
we in the AAF have sort of come up with a potential proposal for what this might look like, as well as sort of a survey of conformance across the n different SDKs, coding agents, even some gateways that might model this, and we're just wanting to discuss with you all here about what the best way is to, sort of, move forward with this discussion, talk you through, like, what we were thinking about, what we are thinking makes sense given the current state of the industry, and, sort of be able to make sure that our proposal isn't just a large amount of information, but something that's actually clear and actionable for us to help things move forward. So, just opening the topic there and sort of seeing where we go.
Liudmila Molkova 00:08:04 Nice! Do you have any write-up, or do you want to come and present other time, or are you ready to present? Let's talk!
Matt Lee (Datadog, Inc) 00:08:11 I can present now, but another thing I'd like to do is actually make sure that, I pull in other folks from the WAF along with you. I just wanted to sort of raise the topic here, so that we can then come prepared with a couple folks who can talk you through the various things that we've thought about, about what makes sense or not in terms of what we're proposing, as well as sort of a sequence of, here's how we're thinking of PRing this incrementally, so it's not just a deluge of, here's an entire model, but, like, here are incremental things that we can use to move the semantic invention forward.
Liudmila Molkova 00:08:39 Yeah, I… we kind of have the PR4 that defines this without the using term terminology. Yeah. Let me see if I can find it.
But…
Matt Lee (Datadog, Inc) 00:08:52 There were a few discussions that I saw related to that, but they didn't exactly explicitly call it this semantic.
Liudmila Molkova 00:09:00 Yeah, so I'm pasting link in the chat.
So, what we are essentially saying that we are calling… a turn… In turn, an invoke agent are the same.
In our… in this proposal.
And it can be not just the agent, it can be a workflow, it can be whatever piece of code that looks Agentic.
Matt Lee (Datadog, Inc) 00:09:31 And this is essentially then a metadata element associated with this invoke agent that is denoting this is the unit of work, rather than an entirely new entity.
Liudmila Molkova 00:09:44 So this pen represents the… the turn. It's… it's just it can be nested, right? There could be multiple turns within one turn, and by… Looking at the hierarchy, you kinda know the boundaries.
of this.
Nothing saves, it's a turn.
But there are input and output messages that imply there was user input, and… it ended with some output, and there's a finish reason, or some status that says, okay, this is… I'm done.
Or if it ends with the ask for a human, then it would show up there.
Matt Lee (Datadog, Inc) 00:10:32 Makes sense. One of the, sort of.
things that we ran into when we were doing this sort of initial survey is the idea of, sort of delegation to sub-agents or other agents, and how these sort of interoperate.
I think the current model, if I'm not mistaken, was thinking about this being something sort of akin to a span link type of interaction, where if there is sort of that sort of delegation-style interaction.
Yeah, the transfer.
I don't know if this was, closed, or if this is worth thinking about or conceptualizing as part of when a unit of work leads to other agents interacting, if there's something that you'd sort of conceptualize of, this is how this should be defined, or if this is still something you'd want to sort of postpone to a, after the semantic has been created.
Liudmila Molkova 00:11:26 Yeah, so, What this one, did is, when you call a sub-agent as a tool, and there is some form of a handoff, it would be recorded.
There are other means of transfer, like when trace context is not propagated, at least yet, and we didn't tackle it yet. But, like, yeah, so if I'm handling some work to another agent, I ideally should make the trace context I worked in as a part of the handoff, and then pass.
Matt Lee (Datadog, Inc) 00:12:00 Acid.
Liudmila Molkova 00:12:01 along, and then the next one can link it. It's just we didn't try to solve the problem of this propagation yet, because we would need to change How agents, do their handoffs.
Matt Lee (Datadog, Inc) 00:12:15 I see, I see.
One of the sort of ideas that we had been thinking about is this notion of a trigger or some sort of an identifier that sort of isn't a span link per se, but is denoting this is the origin, so to speak, of what invoked this agent.
I know that this isn't yet a formal concept, but is this something you've explored, or, has this sort of been… either propose or anywhere in the current slate of ideas that have been brought to you. I couldn't find any in my, sort of, cursory survey, I just wanted to see if this has been something that's been discussed.
Liudmila Molkova 00:12:53 There was a… there are people from COSI, who presented the concept of GenAI trigger… Yesterday. Oh.
And they are interested in this from security perspective, but you're right, it can… it's just also very useful for general observability.
Matt Lee (Datadog, Inc) 00:13:16 Got it. Let me see if I can find that one, then. I wasn't aware that there was a group working on this one as well, because I think a lot of the discussions in the observability tracing, or traceability group have been not just around pure observability, but also this sort of idea of attestation. I don't know how much this has come up in the discussions in the GenAI SIG, but one of the important things that, comes along with observability is the idea to say, can I verify from where this originated, and or who actually generated this, either trace or sequence of events? And having the ability to always, in some way, sign it, if you will, has been useful or in… interesting thing that a lot of industries are looking into for, can I not just see or observe that this sequence of events happened, but also be able to verify that this happened?
Liudmila Molkova 00:14:12 Yeah, we are kind of trying to be grounded by the… what exists in the libraries, right? Because our kind of first goal is to take what libraries have and try to find semantics to ex… express this.
And since none of them have this information, we kind of didn't look into this problem. But, like, yeah, harnesses and other, like, vendor-specific environments have more freedom, have the information, and… I think this, like, the AI security in general is super interesting and useful, so we would love to work with you, especially if you already explored it and you have, like, the… You know the use cases.
Matt Lee (Datadog, Inc) 00:14:59 Yeah. So, what we were thinking is, sort of… The best way to approach this, given that grounding the libraries ultimately is the sort of baseline, is to start with, making the proposals or pushing some of those existent, ideas around, turns, etc, and otherwise, as the sort of foundation for, can we have this be a consistent how do I say this?
a consistent terminology for this unit of work, because another thing that we had noticed is that term is in some ways overloaded. You've probably seen it used to refer to not just a body of work led to by one input, but also the individual actions themselves that are taken. And having that sort of clarification, I think, is going to help Make it more clear what this semantic refers to.
Liudmila Molkova 00:15:49 I've been thinking, I tried to, summarize the glossary and, like, the terminology we use.
I'm pasting the issue, it's my… obviously, I assisted attempt to make sense of AIF taxonomy and all the different ways people call things.
It's… Probably, like, there are multiple ways, multiple terms for everything.
Maybe if we establish some… maybe even non-normative, glossary, and release synonyms. Then we can say, okay, this operation and semantic conventions country, like, is very well aligned with this term, or represents this thing.
Yeah.
Matt Lee (Datadog, Inc) 00:16:41 One of my thought processes here is, as part of the work that we're doing with that sort of taxonomy group, is to try and build out that sort of, synonymous, or that map of synonyms of terms that are used to refer to the same concept, to at least, even if we don't, say, agree on one term, to be able to know roughly what the concept is that we're describing.
My thought process around this is, for some of those that are currently in flight, I'll try to flag this in either the Slack channel or otherwise about these are the things that are in flight that are going to largely be associated with these, potentially overloaded terms, so that you have a reference to what those are. Another thing is.
for the ones that, at least in the industry, have… how do I say it? A larger, critical mass behind one definition or another, I'd also like to make a few PRs to propose Both to the terminology group, and potentially here as well, that we default or try to push folks to adopting that terminology rather than further fragmenting the names of things that are the same concept, but not referred to that way.
It's challenging, as you mentioned. Like, normative is going to be difficult.
Go ahead.
Liudmila Molkova 00:18:10 Assuming you publish terminology somewhere in AEIF, I would love to just link to it. I don't think we need to redefine, because they will, like, drift apart if we do this. Exactly.
Matt Lee (Datadog, Inc) 00:18:25 Yeah, that's also my worry. So, what I'm thinking is that if we can have that notion of synonymous concepts and be able to link, then we don't need to push definitions everywhere, because that inevitably is going to be difficult to scale. There is a repository for this, I'll send it… just a moment.
For the taxonomy Working Group in particular that is working on this.
So it's, this one right here.
You'll see that, there are… pull requests for the definition of these terms that are slowly building up the sort of taxonomy for the way the AAF is thinking about these.
Liudmila Molkova 00:19:09 Oh my gosh, thank you for doing this.
Matt Lee (Datadog, Inc) 00:19:13 It's… it was exactly this problem where we had many terms referring to the same logical concepts that were difficult to rectify, and one of the things we were hoping to try and contribute back here is at least we have a common language or a mapping to name these consistently, so that it isn't confusing about what we're referring to when we're saying specific concepts. But, definitely do… if there are certain terms that are, you do feel strongly about, do comment or, even propose these, and we can discuss those with the broader AAF taxonomy group.
Liudmila Molkova 00:19:50 You know, slop.
Matt Lee (Datadog, Inc) 00:19:52 Yes, there are some of those definitions, I suppose.
Trask Stalnaker (Microsoft Corporation) 00:19:55 Scientific.
Matt Lee (Datadog, Inc) 00:19:56 Very scientific.
The discussions there are quite lively, just because there are… the number of concepts in this domain are quite large.
Also some of them are relatively fun, like Slop. I don't know if there's a bunch of hands, I think Victor…
Trask Stalnaker (Microsoft Corporation) 00:20:16 Yeah, Victor.
Victor  Lu 00:20:18 This is actually a topic I was just discussing in multiple communities. I'm a journalist, so I'm in a lot of communities, including standard organizations, so I… one thing, in last week's, OpenID Foundation, you know, the… one working group on, it's called AIAM Community. These three terms.
Has been identified as a top, most important to make sure everybody agree on what it is. So, after that, I already, yeah, I definitely, I'm not sure, Matt, which… so you mostly work on the AIF as well, on that site?
Matt Lee (Datadog, Inc) 00:20:58 Yeah, that's right. Primarily AAF and the observability within that particular.
Victor  Lu 00:21:03 Yeah, I was in the taxonomy and AIF yesterday as well. So, AIF, there's going to be updated definition for agent identity.
And then aging skill. At this point, credential is not considered a concept that needs to be defined, so that's… that's what's in AIF.
In, in DIT Foundation, Central Identity Foundation, all three, identified, I mean, actually, they're pretty flexible, I guess, that's what, what I've heard. And then, in COSI, I think the three, there's actually quite strong.
I guess, opinion about all three include especially agent credential.
So, yeah, I think… definitely, I think what you do is very interestingly important. For me, I'm just going to focus on three at this point, and make sure that it's across the ecosystem, across those standard organizations, to try to get, you know, what people are thinking should be the definition for these three.
Matt Lee (Datadog, Inc) 00:22:03 Makes sense. So…
Trask Stalnaker (Microsoft Corporation) 00:22:05 Victor, send… send people to the AIAF for the taxonomy, you know, to define there, because that… Feels like the logical place that we would… reference out to.
Matt Lee (Datadog, Inc) 00:22:20 Just to be clear here.
Victor  Lu 00:22:21 I'm asking to redefine her.
Matt Lee (Datadog, Inc) 00:22:22 but to have.
Victor  Lu 00:22:23 They're…
Matt Lee (Datadog, Inc) 00:22:24 to map.
2.
Victor  Lu 00:22:25 Yeah.
Matt Lee (Datadog, Inc) 00:22:25 concepts in similar spaces, so that we're not asking everyone to rewrite their definitions, but to essentially give equivalence classes to, here are the concepts we're talking about, so that we're speaking the same language.
Victor  Lu 00:22:37 I'm talking about beyond that, and it would be ISO, W3C, NIST.
Matt Lee (Datadog, Inc) 00:22:43 Oh, he's just…
Victor  Lu 00:22:44 Stalisations, yeah.
Matt Lee (Datadog, Inc) 00:22:45 Oh, absolutely. One of the things that I think is the goal of that taxonomy workstream is for us to not just define it once, but also to call out to various other standards bodies that may have similar concepts, to map them together instead of it being An exercise that each person would have to go through.
Trask Stalnaker (Microsoft Corporation) 00:23:06 Aaron?
Aaron Abbott (Google LLC) 00:23:10 Yeah, super cool. I'm looking forward to reading through that glossary, and Yeah, figuring out all that stuff is, really helpful. I was gonna ask about the signing thing that you mentioned, like, both from the hotel side and AIAF. I feel like this has come up A number of times, it, like, in the context of attestation, and I was wondering, like, do we have a good concept of what we would even sign with? Is there, like, a good standard across different runtimes and stuff like that?
And then I think, from the hotel perspective, it would be nice to have, like, a place to put the signature that's not just an attribute or something, because you would corrupt the signature by doing that, unless we had some complicated convention, so… Yeah, I'm just curious about that one.
Matt Lee (Datadog, Inc) 00:23:55 Yeah, it's a good question. I don't think there is a standard today for how you would sign such a payload, which is one of the challenges, actually, of it being not standardized. There have been n different proposals that we've seen in the, AAF about ways that this could be done, but to your point, though, it's not just how to sign, but how to carry that signature through in a way that won't Change the payload itself.
And I think that one of the things that we were considering upstreaming or proposing to the hotel is what that would look like. Not the nature of how to sign, per se, but how to carry that information through. And I think to that respect, the challenge here is more that most of the libraries today, because there isn't a standard, don't have a way to do that signing. So it's almost like a chicken and egg problem that we're running into. We know that this is necessary, but there isn't yet an involved or proposed standard for something around this. One of the things we're considering doing as the observability Working Group, was to put forth a, here is a way that this signature can be done, and what we're looking for is a way to carry this information through, so that hopefully that will lead to us developing a standard around this.
Aaron Abbott (Google LLC) 00:25:11 Okay, yeah.
Yeah, I know there's, like, Spiffy and stuff like that, there's a lot of standards, maybe some of them would work, but… Yeah, I was just gonna ask, like, Trask and Ludmila, has this one come up as a general thing in a hotel? I feel like maybe for audit logging we discussed it, but… Just signing of telemetry at the source in general.
Trask Stalnaker (Microsoft Corporation) 00:25:34 Not so much signing the telemetry, certainly there's, sort of… provenance of, like, proving where the, I guess.
A little bit more broadly, Keeps coming up from time to time, which maybe is… maybe it's the same thing, maybe it's very related, yeah.
Aaron Abbott (Google LLC) 00:25:59 Oh, cool.
Trask Stalnaker (Microsoft Corporation) 00:26:01 If there's any… there's been anything concrete, you could, search the community repo. there have been a couple of proposals.
Or people interested.
Liudmila Molkova 00:26:17 But I'm curious if you… oh, go ahead.
Matt Lee (Datadog, Inc) 00:26:20 No, no, no, please, not Gene.
Liudmila Molkova 00:26:22 I'm curious if you've been working on anything related to trajectories?
I guess the concept comes up every once in a while in this call, less… less frequently lately, but it seems it's another way to provide observability into agents.
And we probably, at some point, need to build some bridges. I think Etsy is one of the popular formats. Have anything else came up in your world?
Matt Lee (Datadog, Inc) 00:26:52 Oh yeah, that's definitely been mentioned. Part of the reason why we're thinking about this is, like.
in a… Indirectly, that notion of an observability format is also a way to have that full provenance of here's what the agent actually did over time. And one of the sort of reasons why we're thinking about that turn concept is if we can formalize these are the units of work that make sense, then a mapping between these can be much more easily facilitated. One of the things that we were thinking of contributing to the broader community It's not just, here are the… consistent concepts across all of these various representations, but also here is a way to have a lossless transformation between them in as much of a way that lossless can be achieved, so that if there is a need to sort of move between these, either from Consuming via observability, translating into this format, then this is something that we could offer.
Almost like a… Go ahead, please.
Liudmila Molkova 00:27:50 So this step is also on your radar.
After a turn.
Matt Lee (Datadog, Inc) 00:27:55 That's correct. Step and turn are the two main concepts that we're trying to push into the AAF taxonomy, and when we come back next week, we'll have a very cogent proposal around, here's what these look like and why we think that these make sense.
Liudmila Molkova 00:28:12 Yeah.
Matt Lee (Datadog, Inc) 00:28:13 Oh yeah, very, very much so. I think that this is, Increasingly becoming apparent that this is something that needs A… if not a convergence, at least a understanding of what are synonymous concepts across these various different ways of representing the same type of fundamental idea of agents doing things.
So, that's it for me.
Go ahead, please.
Liudmila Molkova 00:28:41 You mentioned next week. Next week, me and Trask will be out at KubeCon.
Like, you're not coming.
Matt Lee (Datadog, Inc) 00:28:49 Unfortunately not. In that case, then I will… talk to my co-contributors, and likely we can… the next… Oh, I did not realize that. That's a good point. It is KubeCon.
It'll probably be then on the 17th, then we can bring that proposal.
If that's too late, we can also do an async, and then say, here's what we're thinking, and then we can talk about that during the… Meeting itself on the 17th.
Trask Stalnaker (Microsoft Corporation) 00:29:18 Definitely open to an issue would be great to kind of, you know, outline, your proposal, but then, yeah, I think both.
It's…
Matt Lee (Datadog, Inc) 00:29:32 Definitely. So… And along parallel with all of these, we'll be opening issues and sort of trying to articulate, here are the things we're seeing and what we're trying to do. But I was hoping as well to just make sure that we're able to talk through this for… here's the conceptual idea of why this is important, rather than just deluge you with a bunch of text. So, try to… Struck a good balance of, like, this is, a good format to consume, and not just a, here's a bunch of AI slump.
Liudmila Molkova 00:30:04 Other than…
Victor  Lu 00:30:04 I mean… Other than taxonomy, at least on the security side, COSI is developing not only a taxonomy, but an ontology.
Which is much more, not only to find the term, but also the relationship to the term. So make sure in the terms there's no ambiguity, and relationship is clear. So I'm not sure, yeah, that's just… it only started, like, 2-3 weeks ago, so, guess that should be some communication there later on.
Trask Stalnaker (Microsoft Corporation) 00:30:36 Alright.
Thank you. Thanks for coming here, Matt, and look forward to… Seeing and hearing more.
I'm good.
Ankit Singhal 00:30:49 Thanks, ask. Well, first of all, thank you. I think I've got 3 clean text on the PR, so that looks amazing.
And there are a few PR gates that are peeling, and then a few comments that were widely addressed this morning, and I'm just working on fixing the PR gates failure, and once I have that, I'll… Probably request, review, and if there are any open items, I'll address them. And otherwise, if it looks good, would like to get explored.
And I would like to get this much before next week, because I know a lot of folks will be at KubeCon.
So…
Trask Stalnaker (Microsoft Corporation) 00:31:28 Yeah, I think we can merge it.
Just as soon as,
Ankit Singhal 00:31:32 That's good.
Trask Stalnaker (Microsoft Corporation) 00:31:33 Yeah, everything is cleared up, we have the approvals, and as long as there's no outstanding Comments.
Shit.
Ankit Singhal 00:31:43 Yeah, I made sure there are no outstanding comments. I'm just looking at fixing the PL gets, and I'm hoping I can get it done before the meeting ends.
Awesome. Thank you. Great. Appreciate it.
Trask Stalnaker (Microsoft Corporation) 00:32:02 Ludmila, on to you.
Liudmila Molkova 00:32:05 Yeah, I wanted to check if anybody besides me and you, Trask are coming to KubeCon, and if we can do something, office hours or anything there?
I… now there are some people who… From Google's side, who are not on this call, who would like to, maybe come and present about something there, so I guess I'll coordinate office hours somewhere in the hotel Slack channels.
Yes, Surya?
Trask Stalnaker (Microsoft Corporation) 00:32:39 Yeah.
Surya Teja 00:32:42 I have a real stupid question. Where is KubeCon happening? Is it in New York, or is it happening somewhere outside states?
Trask Stalnaker (Microsoft Corporation) 00:32:49 Salt Lake City, Utah.
Liudmila Molkova 00:32:52 This time.
Surya Teja 00:32:55 Oh.
Oh, cool. The… I'll try… I'll see if I can come, but I'll try to meet you guys if I can come to come over there. Thanks, guys.
Liudmila Molkova 00:33:04 Oh, please, please do, yeah.
Trask Stalnaker (Microsoft Corporation) 00:33:09 So, usually for the office… usually somebody organizes office hours, across SIGs. I haven't seen that go out. I'll check with.
Liudmila Molkova 00:33:19 Yeah.
Trask Stalnaker (Microsoft Corporation) 00:33:20 community managers, I'll ping them and see if they're gonna do that this, this time.
Because that's usually the easiest, because then would they post a schedule for all the SIGs who Want to have office hours, so that would be perfect.
Liudmila Molkova 00:33:38 Right.
Thank you.
Okay, no other topics?
Should we, I don't know, talk about stability efforts then? Because we have some follow-ups from yesterday.
Trask Stalnaker (Microsoft Corporation) 00:34:01 Yeah… Do you have something specific we should jump to, or just go into the… continue down the list here?
Liudmila Molkova 00:34:19 Yeah, we didn't merge anything, Oh, there was one thing I wanted to bring up. So, we talked about the renaming operations to nouns, like… agent invocation, invoke Agent to Agent invocation.
I have a couple of PRs for, tool execution and something else. I… Decided not to do this redeem yet.
Because, we would need to rename the operation names accordingly, I would imagine.
So, like, when we… the operation name is now invoke Agent, and it would become Agent invocation.
And, first, I wanted us to agree on this, and second, it will be… a big change, we probably… It's just very noisy.
So, I… I'm no longer pursuing this rename right now.
Trask Stalnaker (Microsoft Corporation) 00:35:32 Yeah, I agree with doing it, as a separate layer after?
And that will give us a chance to also Decide, like, once we see the… the… Impact there, and kind of evaluate it on its own merits.
Liudmila Molkova 00:35:53 Okay.
And then maybe an ask to Ankit and Aaron, since you folks are approvers.
There are a bunch of this renamed PRs, which are relatively trivial.
And it's… just a matter of maybe feeding them to your EI and asking if there is anything you wouldn't expect there, or maybe reviewing once thoroughly, and then just looking at the Others, briefly.
But maybe we can expedite this, and it will unblock a lot of… Other small things from… to happen.
Aaron Abbott (Google LLC) 00:36:35 Sure, I think… so these, these aren't the metric renames, right? These are, spin… Name renames?
Liudmila Molkova 00:36:44 they are everything. So the metric renames, So maybe, Trask, can we start with one of yours for exceptions? And we'll walk Ankit and iron through, and then we can switch to one of mine for metrics.
Trask Stalnaker (Microsoft Corporation) 00:37:01 Yeah.
Let's take this one… So… What we are, So, we used to have a single client operation exception, and a single client operation duration metric.
And so, we are splitting those out. So this is part of this 249 issue.
The duration metric was the same for all these span types.
And what we are doing is, Now, each one has its own metric.
And also has its own exception.
And so… My stack of PRs here is doing that for exceptions.
So it's… pretty… these ones are pretty mechanical. Well, all of these are just… so it's sitting, it's, in… And Ludmila has also been… Extracting out into a new page, in places, but… so it's basically changing this generic exception to specifics.
And if we look at… Ludmila's…
Liudmila Molkova 00:38:37 That's maybe due to the… the, yeah, the tool execution.
Trask Stalnaker (Microsoft Corporation) 00:38:41 Cool.
It's doing the same over here, where… It used to be… So… We now have… it used to be part of the GenAI client operation duration metric.
And now it has its own execute tool metric.
And there's some naming, patterns involved here, where… If it's client or server, we do GenAI.client or GenAI.server.
inference.duration.
But for internal spans, we are not adding the dot internal, so the lack of that means, internal, so it's just GenAI execute tool duration.
Liudmila Molkova 00:39:54 the minimally sufficient review is, Aaron, you review all of mine, because Trask already reviewed, and we need somebody from another company.
Trask Stalnaker (Microsoft Corporation) 00:40:03 Yes.
Liudmila Molkova 00:40:03 And Ankit reviews every Trask PR, but you can also review. Yes.
Aaron Abbott (Google LLC) 00:40:10 Yeah, yeah, sounds good.
Ankit Singhal 00:40:16 Thank you. Yeah, I'll transfer later to the offline as well. I just want to make sure I'm looking at the right PRs, I'm missing any.
Trask Stalnaker (Microsoft Corporation) 00:40:24 Yep, yep.
Awesome.
Liudmila Molkova 00:40:33 One more thing, maybe, to Aaron.
There's this PR from… About making blob… Part content optional.
Aaron Abbott (Google LLC) 00:40:50 Yeah.
Liudmila Molkova 00:40:50 find it.
And I think it's… it's almost good, give me a sec.
I think we had a discussion with you at some point about saying that In the model, yeah, this one.
In the model, you can make content Sorry, you can make a field Optional.
And provide a default.
And then it would be the in JSON schema, it would have no… like, it would be any of the type versus no.
And we kind of discussed that maybe we should just make it not required. It's not optional, and it has default none, right?
Aaron Abbott (Google LLC) 00:41:55 Yeah, I have a separate issue for that one. I was actually talking with, agent… trying to remember their GitHub name, agent…
Trask Stalnaker (Microsoft Corporation) 00:42:05 Oh, gym leader?
Aaron Abbott (Google LLC) 00:42:08 Yeah, yeah, yeah, that one, yeah. Agent Gym Leader.
And I can try to find out.
I think one thing we discussed was how to, like, usefully validate in Weaver if we do that approach.
And, like, one thing we were talking about was adding some additional hints for Weaver, which are not part of, like, the JSON schema standard, which is easy enough to do.
So you could have, This one in particular, with the making the blob part content optional, maybe we wouldn't do that, but for fields that we do expect, we could still… have an annotation for Weaver, and try to find that one really fast.
Liudmila Molkova 00:42:50 I think for this one, like.
For just not making something required.
Aaron Abbott (Google LLC) 00:42:56 Hmm.
Liudmila Molkova 00:42:57 it's actually the clarification, I don't think we need to do this, implement this in this PR, because it's the widespread issue, we will fix it in one go, everywhere. So, it's just that, I think it's a good starter for this.
And… For this, the JSON schema should be enough, right? If it's not required, and it does not show up, then good. If it's required and does not show up, it's a violation.
I also talked about, like, not… trying not to distinguish absence from… None.
Right, so absence means none.
and… the… I'm think… do we need anything, any extra?
Things? Any other hints that are not in Jason's schema, then?
Aaron Abbott (Google LLC) 00:43:55 I don't think for that, I think we would just need to update to, make it more permissive, and then I guess we could say something somewhere in the wording.
Honestly, I… do we have, like, an agreement on this 619?
I see you mentioned, like, mentioned it in something at the bottom there, Trask, but, like, is this… does the… what Liudmila mentioned sound good to you also?
Trask Stalnaker (Microsoft Corporation) 00:44:33 Sorry, I got a little lost.
Aaron Abbott (Google LLC) 00:44:39 That's right.
The idea is… I guess there's a couple… there's a couple things. The first one is… For fields like the blob content, we would make them optional.
And the same goes for, like, text strings and stuff like that, so for, text parts, we would make the string content optional.
And the reason is it makes it a lot easier to evolve the schema.
But also, it seems like there's cases where we just have, like, an empty string, and so people are forced to put these dummies, like, empty quote and stuff like that.
Then the other one… the other reason was… Right now, we have… kind of complicated rules, I think, in the schemas. I can't remember exactly what it was, but we differentiate between, like, null, not present, and it just introduces, like, extra complication that we don't really care about.
Trask Stalnaker (Microsoft Corporation) 00:45:36 Yeah, I'm a big fan of not, null and not present being the same thing, because otherwise it… is… I mean, everywhere, throughout programming land.
That's forever my opinion.
Aaron Abbott (Google LLC) 00:45:50 Not a JavaScript fan, I see.
Trask Stalnaker (Microsoft Corporation) 00:45:55 I mean, I understand languages… lots of languages different… have differentiation, like, I mean, in Java, like, empty string and null, but they… you should… they should semantically be the same.
Aaron Abbott (Google LLC) 00:46:09 Yep.
Cool, so if you scroll down a bit, you can see Agent Jim Leader's comment. We were just chatting about some… I don't know if there were specific cases that they were worried about for, like, URI part.uri, textpart.content, it was like… do we care about differentiating those in the Weaver conformance test or not?
Liudmila Molkova 00:46:34 This thing in waiver conformance.
Tests… Or you're saying that, okay, in normal cases, this should be expected, like, URIPART.URI.
But from the schema perspective, there could be edge cases or future compatibility where we don't want it required, and then we kind of have two different schemas for the happy case and for the future case.
Aaron Abbott (Google LLC) 00:47:03 it.
Liudmila Molkova 00:47:04 and… I… Thing queer.
These schemas are intended for the comp… For the external thing, for compatibility, what we tell consumers to expect?
And Weaver, we can solve in multiple ways. We can have better, like, additional policies that check for presence, we can make it part of validation.
It's for us, and it's less important this way.
Aaron Abbott (Google LLC) 00:47:41 Yeah.
And I think that's… that's kind of what I was suggesting here, so rather than making a separate schema, we can just add some hints for… I think this is what they did here, XOTEL producer required as a hint.
In the JSON schema, which is only intended for the Weaver Conformance tests.
Liudmila Molkova 00:48:00 Let's not do this. I mean, then… I think for the producers, Jason's schema is not the right.
For a matinee, right?
I think we've already had this discussion on… one of the PRs.
Where… For the… Complex values, right?
Aaron Abbott (Google LLC) 00:48:27 Yep.
Liudmila Molkova 00:48:30 that… from the API perspective, we want, let's say, binary payload to be bytes or byte array.
And from the schema perspective, you cannot express it in JSON schema at all.
Aaron Abbott (Google LLC) 00:48:48 So, I think the request is more practical. It's like, I know we can put it in Rego and do all that stuff, but it just becomes kind of sprawling.
Liudmila Molkova 00:49:01 I mean, let's start with just cleaning up the schema, let's not overthink it. We can add the hints if we need them at any point later.
Aaron Abbott (Google LLC) 00:49:10 Yep.
Okay, so it sounds like at least folks here agree I can send a PR for 619.
Liudmila Molkova 00:49:29 At 619, it's… The one that makes everything but type.
Not required, right?
Aaron Abbott (Google LLC) 00:49:38 Yep.
Liudmila Molkova 00:49:45 Yeah, I'm… And this is for the evolution, so I just briefly check in what we have required.
And it has things like modality, Mimes… And all the content. So, all the content properties.
Seems like an obvious thing to not make required.
for the… Three little things.
We are making them not required.
Because this is the way for us to evolve the schema, right?
And also, since we're parsing what provider gave, they could, in theory, give invalid.
Thing with that property, and we will have no means to populate it.
Aaron Abbott (Google LLC) 00:50:49 Yeah.
I mean, ultimately, it's like a validation, so I think if the producer does something wrong, then the consumer is, like, welcome. They can still parse it and allow the validation to fail and do something different, but… like… From the perspective of, So say we add a new field in the future to one of the existing parts, so say, like.
for you or I, we add, like.
I don't know, storage system or something like that, which would be the… you know, OpenAI files, or Gemini files, or whatever.
Like, if we add it in the future, it has to be not required anyway, because old producers aren't going to be sending it.
So, it seems like we're gonna end up in that situation regardless, and it shouldn't cause a validation error.
So, that's kind of where I'm coming from.
Liudmila Molkova 00:51:49 Yeah.
Well, I'm fine with it. I think I… feel, I wish I was… we provided more… The schema was more strict, but… It would hurt us in the long run, because we just don't know what we're doing yet.
Trask Stalnaker (Microsoft Corporation) 00:52:39 Yeah, send… send the PR, I find it for… it's easier to, once I see it in the PR form, to understand the trade-offs.
Aaron Abbott (Google LLC) 00:52:52 Yep.
Cool. Ludmila, I think you mentioned… the, this one seems… 540 seems kind of relevant, also, and I see you put up, like, a block on it.
And it's kind of related to one of Trask VR, so should we discuss this one real fast?
Liudmila Molkova 00:53:12 Wordy?
Yeah… So none of this… Seems to be… Related to the producers.
And if we do any value end-to-end.
Then, it's the exporter who serializes.
Aaron Abbott (Google LLC) 00:53:43 Yep.
So one… one concern I had was, as far as I can tell, this format binary thing, That we currently have.
is just a Bydantic hint. It's not, like, part of the JSON schema standard.
maybe it's widely used, and I can dig into that a little more, but from the perspective of, like, a consumer.
of the data, I think they would just assume it's a string right now with what we have, unless this format binary is widely recognized outside ofantic.
Liudmila Molkova 00:54:27 This is our Jason Spiemer. Yeah, go ahead, Trask.
Trask Stalnaker (Microsoft Corporation) 00:54:30 Yeah, I mean, it… What?
I think what we're trying to do here is related to, yeah, related to this PR… Where, I actually tried to strike anything about JSON serialization.
From the semantic conventions.
And say that the JSON schemas describe the structure of the attributes. It's not a export format or encoding I know it's… it's confusing because we're using JSON schemas. We're basically… we're basically just using it as a… Some kind of random schema.
To describe our complex data structures, our any values.
And maybe that… and maybe in the long run, that will do more harm than good, and maybe there's some other… Format we could use.
But ideally, it shouldn't matter.
Yeah, alright, I… I mean, yeah, basically anything that doesn't then cause that confusion, that people think that it is a JSON schema.
Aaron Abbott (Google LLC) 00:55:56 Yeah.
Yeah, I think that's exactly the friction. It's like, JSON schema is inherently tied to JSON, and JSON can't represent everything in any value.
Liudmila Molkova 00:56:08 Would that be any better if we really changed it to Prado?
Trask Stalnaker (Microsoft Corporation) 00:56:17 I mean, it'll be worse in a lot of ways. The only thing that it improves is the confusion, which… I mean, is…
Liudmila Molkova 00:56:29 Well…
Trask Stalnaker (Microsoft Corporation) 00:56:30 Something.
Liudmila Molkova 00:56:31 it… It allows us to… Well, the OTLP is in Prada, right?
And at least on this level, it maps.
Aaron Abbott (Google LLC) 00:56:47 Except it gets encoded as any value.
In the… in the proto, right?
Liudmila Molkova 00:56:53 And we would expand what that… this specific any value means.
Aaron Abbott (Google LLC) 00:57:00 Hmm.
Liudmila Molkova 00:57:02 But, I don't want to create a lot of work for no good reason. It would be, like.
Trask Stalnaker (Microsoft Corporation) 00:57:11 I feel like that's something we can, in 3 months, if we've got some time and interest, we could convert our entire schema to something else.
Aaron Abbott (Google LLC) 00:57:20 Agreed.
Agreed.
Yeah, so…
Liudmila Molkova 00:57:23 And now we are documenting it away. We're saying JSON schema is there for demonstration purposes.
Aaron Abbott (Google LLC) 00:57:31 Yeah, and I think from the… from the perspective of, this is… this isn't information for the consumer, we should just have some… as far as I can tell, this content, I think it was called Content Encoding, is the… Best way to indicate that it's… Binary to a consumer.
Dylan Russell 00:57:49 But we're saying there that we want it to be Base64?
like… I don't think that's true, right? Because it can be any binary encoding.
Aaron Abbott (Google LLC) 00:58:05 Like, the consumer sees… the consumer sees, like, structured any value from… from the protobuf, right?
Trask Stalnaker (Microsoft Corporation) 00:58:18 And it would be binary in the prototypuff.
Dylan Russell 00:58:24 Right.
Trask Stalnaker (Microsoft Corporation) 00:58:26 But I didn't follow… Aaron, are you saying that we should still do this?
Aaron Abbott (Google LLC) 00:58:34 I'm… I'm kind of… leaning that way, just because this is part of the JSON schema, which is a hint to consumers that this thing should be binary, but I'm also okay to put it… to just leave it in the description or remove the information about the encoding. You could just say, like.
this field… Will be bytes value in any, any value.bytes value, or whatever, and should be interpreted as bytes, or something like that.
Trask Stalnaker (Microsoft Corporation) 00:59:02 My only worry about doing this is that then people will stick Base64 into strings, into the any value.
Aaron Abbott (Google LLC) 00:59:14 Yep.
Yeah, I'm mostly concerned about that.
Unfortunately, it's always going to say type string here, because there's no other option.
Liudmila Molkova 00:59:31 I mean, it just means we need to eventually invest in the proper schema that's for semantic conventions.
We cannot rely on the external thing to represent what we want.
Aaron Abbott (Google LLC) 00:59:45 Yeah.
Trask Stalnaker (Microsoft Corporation) 00:59:47 I mean, I find if, like, you know, we could add comments… trailing comments.
here, and here, and everywhere, like, to… I don't know. Yeah.
Alright, we have hit our time.
Liudmila Molkova 01:00:08 Yeah, thank you.
Trask Stalnaker (Microsoft Corporation) 01:00:10 Yeah.
Aaron Abbott (Google LLC) 01:00:10 Thank you, Lauren.
Dylan Russell 01:00:12 Thanks.
Aaron Abbott (Google LLC) 01:00:14 Thank you.
Liudmila Molkova 01:00:15 Jim, see you around.
