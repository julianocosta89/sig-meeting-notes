SIG: GenAI SIG
Date: 2026-10-27
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:04:45 Oh, hi everyone.
Pam Dixon 00:04:50 Hello!
Liudmila Molkova 00:04:57 Okay, if you have anything to discuss, please add it to the agenda.
And while we are wait for people to join… Let's see what we have… So I think this one, we're ready.
Discussed, and… Maybe even… merged?
Not, not merged yet.
But I think there's nothing to discuss.
Okay, we already have this one on the agenda.
And the evaluation result, I think we talked about it last time.
There are some PRs.
If… If you folks want to talk about this, please set it to the agenda.
I am… Keeping it… Here, in case anybody wants to drive this discussion.
And… Sorry, I missed the morning call. Trask, did anything interesting happen there? I think you've discussed this, France, right?
Trask Stalnaker (Microsoft Corporation) 00:06:26 Yeah, Steve was just asking for reviews on them.
Nothing in particular.
Liudmila Molkova 00:06:33 Okay.
Yeah, I, I took a look, at this one, didn't at this yet.
So, we are here, right?
Okay, so, I think, Danielle, you're the first… is it Daniel?
Was this topic?
Daniel Rolles 00:06:55 Yeah, hi?
Liudmila Molkova 00:06:57 Hi!
Daniel Rolles 00:06:58 How are you?
Liudmila Molkova 00:06:59 Good hurry up.
Daniel Rolles 00:07:01 Hanging in there. Hanging in there.
Liudmila Molkova 00:07:04 Awesome.
They want to present? They want to talk?
Daniel Rolles 00:07:07 Yeah, I'm happy to go. I was expecting to wait, but if we've already discussed those, I was, I put my name on the list, but so we've already done those other ones, have we?
Liudmila Molkova 00:07:17 Yeah, we have the… the other meeting before this one, like, hour and a half before. We are going, by the way, to reschedule this early meeting to some other time.
In the US evening, and China morning.
For the next 6 months, I guess.
Until the time zones switch back.
But yeah, we discussed it there, and you're the first on the agenda.
Daniel Rolles 00:07:45 Fantastic.
Liudmila Molkova 00:07:47 I'm going to stop sharing. Go ahead.
Daniel Rolles 00:07:49 Yeah, thank you. I'll share in a second when I jump into the call chain, but, let me… let me introduce myself and, And give a little bit of a background first, and then I can jump into the call chain artifact from the lab. So, first of all, hi everyone, Dan Rolles, founder and CEO of Bering Node. We are a data analytics and AI consulting firm, about 2 years old.
I'm not 2 years old. As you can see, I have, some grey hair and grey beard, like some others on this call.
So I've been at this a long time, and I've spent about the last 20 years of my career working in London, working with, chief data and analytics officers, risk teams inside, predominantly financial services firms.
Over on this topic, we have spent about the last 12, 24 months, working with the Open Standards Committees, the technical, steering committee over at, Open Lineage.
It's particularly focused on data and information, observability. And one of the topics that's kept coming up over in that community is, agents, whether it be on behalf of or autonomously, reaching to govern data sets.
And how do we manage those, sorry, how do we gain observability onto those events?
So, we've been doing some research over the last little while, and looking at MCP, looking at OpenTelemetry, and looking at the open lineage standards, and working out where those gaps are or are not, and where the correlations need to happen, and where they don't need to happen.
In, about 2 months ago, 3 months ago?
What we did was… I'm just gonna share my screen.
What we did was launch, the, Bering Node Lab.
So, we launched into… launched up on GitHub, the Baron Knight Lab, and the first piece of workstream that we've… we're launching into that lab is the… what we're calling the MCP lineage work.
So, lab's up there, it's all source available, for anybody to, to look at. But… the MCP lineage work was focused specifically on when agents whether on behalf of or, or autonomously are calling governed datasets, and the particular example we picked was a SQL backend Postgres instance. When that call is happening, what should that call chain look like?
And we've done some analysis in building a reference implementation, so we talk an MCP off the shelf, so one of the widely used MCPs. We fired a set of events, through that MCP, into a Postgres instance, and, we used an OpenTelemetry collector.
In, Jager, and used, one of the standard open lineage Implementations to collect those events.
And we pushed up a set of synthetic data sets, so we imagined that was a… insurance company, called Opsinsure, Observability Insurance, to, to push those events through, to try and make it as realistic as possible.
So, in… in that lab, all that work is… is up there and source available.
But more particularly, the key ask and the key agreement we're here today with is, to flag the issue we've raised.
and at least two of the key principles in there, but certainly open it up to this community to, to make sure that, we've consulted with you guys, as I don't think there's a particular ask yet, only at the principal level, but that's exactly why we're coming to you guys and having you guys challenge it and question it.
But here is the specific issue we've raised in the OpenTelemetry repo, and it focuses in on the call chain, which I'll come to in a second, focuses in on when that SQL call happens, how do those events get logged in, how do we get correlation between the open telemetry event and the open lineage event.
over into that call chain, so what we've built, there's an… again, in the artifacts directory of the lab, there's a HTML and PNG of this, but it walks through the call chain, if I can just spend a minute walking through.
So, that agent calls out through, through the MCP. That MCP gets passed through, via underscore Meta, which is part of the MCP standard, which we've also raised an issue in their repo.
And it calls the ExecuteSQL, tool within, within that MCP.
we swapped out the factory to make sure it was open lineage compliant. It wasn't, in the standard MCP that we pulled down. And then the call chain that… that happens in the lineage gets captured, via, via the OpenLineage, collector.
Liudmila Molkova 00:13:39 Can you indicate us a little bit? So, what you're describing is what we just call correlation in open telemetry, and you would see, like, the waterfall of spans that are correlated to each other.
What is…
Daniel Rolles 00:13:54 You… oh, sorry, you got…
Liudmila Molkova 00:13:56 What is, missing from the OpenTelemetry side that we can try to address?
Daniel Rolles 00:14:04 We… we don't think there is, so in our issue, yeah, that's what… part of what we're looking to confirm, Limil.
We… we don't think there is anything missing… missing. What we've managed to do in our reference implementation is we have got correlation.
Right? So we've actually been able to insert, a run ID.
So it gets correlated correctly. We have also had to adjust our sampling policy, which we've talked about over in this artifact, where we've… we… if you apply sampling, you do lose what are audible events.
Right? For a regulated industry like financial services, those lineage events are auditable, right? As in, a decision touched a… sorry, governed data set was used in a decision. So, we think in the implementation, and that's part of the reason why we're opening up the community, we think we can achieve we can achieve correlation and auditability with it as it stands, we think. What we're doing is we're going to the MCP team, we've already spoken to the financial services special interest group there.
They've supported us raising an issue in their repo. We've raised it in your repo to make sure that, our understanding is correct, and, we've raised it in… and already discussed it in the Technical Steering Committee of the Open Lineage.
So we think we've done the rounds, but that's part of the reason why we're coming here, to make sure we have done the rounds, and make sure that we have got it correct.
Does that make sense?
Liudmila Molkova 00:15:47 Yeah, thank…
Trask Stalnaker (Microsoft Corporation) 00:15:48 Yeah, yeah, thanks for the RUB. I'm just trying to also kind of get, over… understanding here. On that… that left side, you're, like, the run event, the open lineage, You're capturing events.
already about, and, are you wanting those to go… to be, like, open telemetry events, or that's a whole different… that's an orthogonal, like, collection of…
Daniel Rolles 00:16:17 Excellent. So let me jump back to the specific asks, and we've updated it. We would… we tried to come to you guys on the 13th, I think, of this month, and we've updated it, since to focus purely on these two asks.
Right? So there's one ask, which is exactly the opposite of what you just said, right? So the key principle is, these are different standards capturing different things, right? One is software and infrastructure observability, which is what OpenTelemetry is.
And the other one is data observability, which is open lineage, right? So that first principle we're asking everybody to agree is these are different capabilities of observability, and we should treat them differently.
Right? So, in lineage events, we need a very particular set of things around the dataset it got, the one it brought back.
the, you know, we parse the SQL, et cetera, et cetera. We do a bunch of stuff that presumably the OpenTelemetry standard is not interested in, right? And scoping it out… taking it out of scope of that standard is probably important. And hence, right there, the first principle is That we need to agree that these are separate capabilities, you know?
And then the second one is, when they reach, reach to, which is Lemur's question, when it reaches, that's an auditable event, and we need to make sure that we're sampling that.
Now, OpenTelemetry already has, on that second point, OpenTelemetry already has policy adjustments, through the YAML files, and we can make sure that we can capture those And don't… don't drop them, even when we're sampling. So they… they… the policy adjustment is necessary, but the standard already allows for it.
Liudmila Molkova 00:18:04 Yeah, thanks. I have some thoughts on this, I'm curious what Pam thinks.
Daniel Rolles 00:18:09 Sure. I'm conscious Pam's got a hand up. Do you want Pam to go first?
Pam Dixon 00:18:13 Oh, hi folks.
Just a super quick question. I'm trying to work out the architecture in my mind here, and I'm looking at the, ID and how you're working with it, so if this is auditable.
Is this an ephemeral ID, and it disappears? How are you working that, and what standard are you passing it to? Is it part of the payments architecture, or which lineage are you going to? Thank you, that was it.
Daniel Rolles 00:18:41 Yeah, so let me try and… you've asked a couple in there, so let me try and capture them in… in turn. So, the whole point is exactly the opposite of ephemeral.
That was the point where we touched on sampling just now, so… It's absolutely critical in regulated industries, when you're touching governed data sets, that those events are auditable.
and especially as we move to more Agentic commerce, Agentic payments, etc, those calls get captured and audited and not sampled, Pam, to your question, right? So what we've actually done in the lab And I was quickly trying to flick through to the README where, where the architecture is. We've stood up a, Jaeger, OpenTelemetry collector, and we've adjusted the policy, so even when it's sampling, it still collects anything with a lineage event in it.
Gets collected as well, so you can actually do the correlation.
So, exactly the opposite.
You asked it… the other question was around payments infrastructure. It shouldn't matter whether it's payments. Anywhere where it touches a governed data set.
The use case is predominantly focused around reporting, and particularly in banks and insurers, etc, when you're reporting up to the board, and up to risk committees and governance committees.
Right? That… that injection of context, i.e. an agent reached out to a governed dataset and brought it back.
into a decision, or into a board report, or into a, a, necessary management decision where we're taking risk, risk decisions, that that, that gets captured.
Yeah, so not necessarily payments, and I think one of the topics we'll be talking about tomorrow that one of the guys from the TSC brought up, is streaming events, where we have a number of payments happening. So that's one of the things that this implementation is still an open question on.
hopefully I answered… you asked two key questions, Pam. Hopefully I answered both of those.
Pam Dixon 00:20:47 Y-you did, thank you.
Liudmila Molkova 00:20:50 Yeah, thanks. Getting back to the principles you outlined.
I think we cannot draw the line between the audit.
If that's what OpenLineage is after, and telemetry.
So there are asks to… say, to mark… to record events about data being written and what's being written, and we do this in GenAI conventions, and I don't think it will… Stop.
So I… I think we… we cannot draw the line, and if there are two ways to report events.
there will be two ways to report events. We can try to figure out how to make them work better together, how we can share the same schema, or how we can share the same instrumentation, how we can, work with delivery guarantees. There is, And… endless, proposal to start audit logs, SIG in OpenTelemetry.
So I… I think we cannot draw the line, but I would love to figure out how we can work together with OpenLineage. To be fair, I don't think this is GenAI concern at all. It's more, like, of the whole open telemetry and semantic convention story than this group.
Daniel Rolles 00:22:07 Yes. I think what's happened is the way agents operate and can operate through MCP, unfortunately, has just highlighted the issue and is highlighting it very quickly.
Right? So, hence… hence, we didn't know where to bring it, so we brought it here. We didn't know whether that was the right home, but we raised it, we just wanted to make you guys aware and start the conversation, right? And initially, with our analysis, we thought we were going to ask for a spec change, but actually, through our work, and again.
all the decisioning. What we've tried to do different with the lab is we've shared the complete RAID. So the risk issues, decisions, and assumptions we've taken are all completely there… are all completely open and there in the lab. So we're not arriving here with a completed decision that's not clear how we got there.
That's all available in the lab, so it all can be looked at and inquired and queried.
Yeah.
I just got a little bit confused, sorry.
Around your point about audit? Can you… sorry, can you just make that again?
Liudmila Molkova 00:23:10 Yeah, Trask posted a link in the chat, and there is a proposal to start audit logging, SIG and OpenTelemetry.
And I think commenting on this issue and say in the Open Lineage is also interested in this, and there is… if there is any, like, workforce that is interested to driving it forward.
Then… Working together with other organizations would be the way to, make any changes, or, like, try to draw the line, or, establish, like, how we can cooperate from different angles.
Daniel Rolles 00:23:46 Hmm. I think one of the things that… The lab proves.
We think, and this is… Again, it's a community challenge.
is… With the sampling policy and with the implementation we've done.
you can actually capture, to Pam's question, you can actually ensure that you capture. Now, with the retention questions on your OpenTelemetry stores.
So the, the spans and traces stores. That's, of course, an implementation and a data retention policy question for the implementing organization, the using organization.
Trask Stalnaker (Microsoft Corporation) 00:24:26 Part of the problem, though, with the… is that there is not a delivery guarantee for telemetry.
So even though, you know, you can ensure that it's sampled in, there's a lot of, places in the pipeline where things are intentionally lossy to avoid running out of memory, other factors, and that's one of the key pieces of the audit logging SIG proposal, and one of the complexities to launching that is that it would need to Provide that kind of a delivery guarantee as the first step there.
Daniel Rolles 00:25:07 We have put some redundancy in there, so in the design, we have put some redundancy in there, but have we put enough? Again, I think it's an open question. But we have… we have tried to second guess that that may happen, so there is redundancy between the two.
Liudmila Molkova 00:25:24 Awesome, so I think the next step would be to, rather bring it in the pull request Trask shared that you're interested in working on this. I don't think this SIG has, the scope.
To address the open lineage, collaboration.
Daniel Rolles 00:25:45 Yo.
Understood, and again, I think you're absolutely right, Liila. The, unfortunately, agents have made this acute.
Right? And MCP has made this acute. I don't think this is the first time… last… first or last time we'll deal with this one.
Trask Stalnaker (Microsoft Corporation) 00:26:02 Yeah, we find a lot of people end up in coming to this SIG because, the, AI is exposing things in the kind of core semantic conventions, but we do…
Daniel Rolles 00:26:17 We've been talking about consumption events now for about… going on about 24 months on the… on the TSC at OpenLineage, right? So, OpenLineage is primarily designed around static jobs, as in data pipelines.
What it's not… what we're trying to now get our head around is what… what happens when you've got a framework data pipelines? Because you've got agents calling out to govern data sets, creating data pipelines ad hoc.
Right, so that's the… that's why it's become acute, and that's why MCP is such a beautiful example of the challenge.
Trask Stalnaker (Microsoft Corporation) 00:26:50 Yeah, so I think what the ask for you would be to, sort of inside of OpenTelemetry, we would want that to be generalized, like, I mean, have a… Outside of… the GenAI, and then we can apply it in this SIG.
So that would be either the general semantic convention meeting SIG, where, you know, we can discuss, you know, new semantic conventions, we can explain, sort of, federated semantic conventions that you can own.
As well as… potentially, you know, the overlap or, you know, drawing the line with the audit logging SIG, My concern there is that that has been open for 2 years, and there's definitely been Lot of interest in it, but it hasn't… Nothing has… really happened concretely.
Daniel Rolles 00:27:53 Sorry, sorry, are you sending me to a SIG that is dead?
Liudmila Molkova 00:27:59 It is the proposal to start a SIG, and this is the place where people who are interested find each other, and we need some people with energy and desire to drive it, from a diverse set of organizations, at least two or three, to actually move it forward.
And, like, unless we have this group of people, I don't know how we can make progress.
Trask Stalnaker (Microsoft Corporation) 00:28:24 But what you can do on your own with OpenLineage is look at the federated semantic conventions, that there's tooling and prior art now. It's just… it's fairly recent in the last, you know, 6 plus months that this has been a reality for OpenTelemetry, but that allows… you to potentially, you know, you want some attributes, some additional semantic convention layer on top of the general semantic conventions, or on top of even GenAI, you can build, and you can own that within OpenLineage Foundation yourself.
Daniel Rolles 00:29:04 Yeah, yeah, so that's… sorry, so on the… I should have been clear. On the open lineage side, we're… we're driving that. That's fine. We've got a working group, I presented there. I've presented there over the last couple of months as we've progressed there. We're setting up, some of the vendors, like the guys from IBM, engaging with us on that, and working through. And especially, we've also, in your group, in the same vein, we've talked to the… end-user SIG, so I hope I've called that the right thing. So we presented there with Daniel, who's running that, who's based here, in the UK. So we've presented at the end user group. So we're trying to do the same thing with a special interest group.
in the open lineage community, right? Drive this out and work out how we engage it, because there's a problem that everybody's starting to deal with, especially across regulated industries.
Liudmila Molkova 00:29:55 Awesome, thank you for coming, thanks for bringing it up.
Daniel Rolles 00:29:58 No, you're welcome.
Liudmila Molkova 00:30:00 Yeah.
Okay, moving on to the next topic. Ankit, are you here?
I think you're here.
By the way, if you're talking, we cannot hear you, or see you.
Okay, So, we have a PR from Ankit.
I left another round of reviews yesterday, I'm not sure, it seems… Oh, Ankit might have addressed some of it I didn't have a chance to check.
So, I think I'm… My proposal was that We take the controversial part of this PR away.
So the controversial part is that sometimes we capture the real-time inference for Generation that calls with a tool call.
And sometimes we cannot… we don't have this information, and we capture it for the overall Operation with all the tool calls.
And… Somewhat mimics the… The inference problem that we have, that it can be one request, or it can be include tool execution.
So, what's unclear is how to record local parts. Where would we put this information?
And my proposal is to maybe, since we… Don't… Have a span that… can cover them reasonably well. We would eventually need to report them with maybe events, saying, okay, there was this long operation, and we know when the two call started and toll call ended.
And what was the information, like arguments and results?
And that the parts… Would be available on this event.
And I'm not suggesting to define them now, I'm suggesting to… Just leave it as TBD for the futurist.
And I've… it would be… awesome to follow up, but I think there is a merit to this PR without it.
I kind of feel that we probably come back to redefining, some of those things, but it's just I don't see, unless we… We have more examples of… Live API, that's what you… like, redesign it. At least, I don't feel we know enough yet to… do more than this PR does. So, like, if… Ankit, if you took it away, then I think it just has some cosmetic changes that, if you address a… if you are dressed, I would be happy to approve.
Ankit 00:33:23 Yeah, thanks, Liuda. Yeah, so I'm working on these, comments.
Yesterday I was not able to, get to them, but I'm working on this morning, so hopefully I'll get them done in a couple of hours, next couple of hours.
And I can, Of course. And, I think one thing you mentioned, yeah, I think that part, yeah, definitely I'll, I think, link the new issue for that, the one that you mentioned just now.
About the tools, right?
So, that's good. Definitely, I will do a follow-up on that.
And, the other part that you mentioned about, like, revisiting this, is it more about, like, getting to understand more on the real-time inference as it becomes… More and more popular and mature, or…
Liudmila Molkova 00:34:13 Yeah, I kinda think that this… the… The fact that we… Have real-time inference.
Definition, essentially, tied to whatever we get from the provider.
we might…
Ankit 00:34:28 Edge.
Liudmila Molkova 00:34:29 Want to design it in some other way, or maybe we would… decide to put… I don't know, like, for example, we would not collect audio as a buffered part, we would also collect it as a set of chunks.
events, because it's just impossible to buffer that much audio and put it on telemetry. Or there could be other things that we will discover as it gets more adoption.
But I don't think it's blocking, it's just the nature of defining semantic conventions and see how it plays out in real life.
Ankit 00:35:09 Okay, no, that sounds good. I think, sounds like, A journey he will have to go through as he learns along.
So, that's good.
Liudmila Molkova 00:35:18 Yeah, I'm not… I don't think we, like, we need to break anything anytime soon, unless our round of renames will… Touch it.
Ankit 00:35:30 Becca.
That sounds good. Yeah, I'll address the comments that are open, and I'll post back ones that are addressed.
And what kind of.
Liudmila Molkova 00:35:39 Yeah, thanks.
Ankit 00:35:41 Thanks, Linda, appreciate it.
And I know, thanks, Dylan, as well. I think Dylan has, given the approval, so that's good. Thank you so much, and I think I will probably need two green ticks.
So, if someone else can, as well, like, Trask Aaron if you could help take a look at the beer, I would appreciate that.
Trask Stalnaker (Microsoft Corporation) 00:36:04 Yeah, I will look at it, definitely will need to, it will have to be somebody non-Google after Ludmila.
Ankit 00:36:17 Oh yeah, that's right.
Liudmila Molkova 00:36:18 And Ellen.
Cool, awesome.
Ankit 00:36:23 Thank you, appreciate it.
Liudmila Molkova 00:36:25 Thank you.
Cool, moving on. Max and Michael are absent, so I think it's a call for review.
And for the broader group, we've been discussing it in the stabilization calls, where… There is a problem we have today that what we call a workflow is just an implementation detail.
And it can be called graph, it can be called workflow, it can be a set of arbitrary code that runs together, but it's usually represented as an agent. Like, when you work with a harness, then you don't care what API, the hardness uses underneath, you consider hardness an agent?
And it creates some problems that today we have workflow and Agent together, and they represent the same thing.
So what we've been discussing is that, we would like to merge them into a single span type and metric name.
And, have, additional flag to say what was the outermost. Today, we kind of assume that the workflow is outermost, but it's arbitrary. It doesn't have to be. Workflows can be nested under each other, under agents.
So… Also, in many cases, what is the top-level thing is something like runner run, and it receives some configuration that says how to run it, and essentially this thing, new thing becomes the… span and metric that is emitted for this, and clear things. And the operation name.
Would be specific to the framework.
So the workflow name, is now… becomes agent name, if known.
And… through the operation name, you can… you will still be able to see what flavor of the API, or what Type of the Agentic flow was used.
And… Oh, also the… Call… number of inference calls and number of toll calls is moved under this, oh, we, we have it. They, they are preserved.
So this is the scope we've been discussing. Maybe it's a little bit bigger than what I was thinking about, but it makes sense, and maybe we'll Need to split it, but it looks… The intent looks… Aligned to what we discussed.
Okay.
Let's move on to the next topic.
Dylan, a plot hook.
Dylan Russell 00:39:51 Yes.
So… we currently have this upload hook mechanism.
And it only… applies to the… Input and output messages… On the inference span and event.
And the input and output messages is like a repeated array of content parts.
So, the question is, should we… Potentially apply this upload hook mechanism.
To individual content parts.
Within input and output messages.
And the idea is you would upload just the individual parts to… This… External storage, and you would replace it with… like a URI part.
And the URI part would point to… The place where you uploaded it.
And… We could potentially extend it to, like, Any attribute that exceeds some size limit.
Like, on any span.
Bud.
maybe that's, like, a follow-on. Maybe initially we just say, just for, like, individual content parts.
Within input and output messages.
Yeah, and we can, like, dedupe by hashing… And… there's some other… Yeah, there's even more stuff to consider around, like, normalizing… like, formats?
Cause you can have, like… an audio… Blob in, like, a bunch of different formats.
And maybe the telemetry should, like, standardize, or allow the user to say, like, convert to, like, a particular format.
Anyway, so it's a lot of stuff, but yeah, I just wanted to get feedback on this idea.
Liudmila Molkova 00:42:18 Yeah, Aaron.
Aaron Abbott (Google LLC) 00:42:20 Yeah, no, thanks for starting this one. I've been interested in this, too.
I… I wanna say we discussed this a lot in the past, And we can talk about, like, the context, but… Just one question is, do we need any change to the semantic conventions to do this right now?
Dylan Russell 00:42:44 I think so, because I think we just say… the upload… upload hook… Is applied to the full input and output message array.
But, anybody?
Liudmila Molkova 00:43:01 do they… The implementation details are left out, right? So somebody could implement it this way, if they wanted to.
Dylan Russell 00:43:10 Oh, okay.
Aaron Abbott (Google LLC) 00:43:13 Yeah, that's… that's what I was thinking, too, is… because we pass… We pass everything, it's all mutable, and we pass the span and log.
my nose… Yeah, yeah. I know Ludmila's working on the ref thing, I don't know if that was already merged in the main semantic dimensions.
Liudmila Molkova 00:43:33 I did, yeah.
Aaron Abbott (Google LLC) 00:43:34 Yeah.
But I don't know if that… like, I think they can both be options, it's kind of… like you said, Dylan, maybe we can play around with heuristics and figure out what works well, but it seems like we could do… Either or, some combination, without changing anything right now.
Liudmila Molkova 00:43:54 Speaking of refs, this is the PR that adopts Semantic Convention Guidance on Unbounded attributes.
So, any attribute that we expect to have arbitrary values, arbitrary large values.
Or somewhere should be marked with this annotation.
And there are some checks that kind of ensure they are obtained, and so on.
And we get a combination of attributes now.
So this PR also defined some reference attributes.
So, where is the registry?
So we get, both… oh my gosh.
Yeah, so we get input messages, and input messages ref, which is a URL to somewhere else where this Thing is stored.
I am… it seems everything on this PR is resolved, and it… it gets to… it got two approvals from… Different companies, also from Pydantic, who were initially pushing for the parts, I think. Aaron Dylan, do you remember?
Dylan Russell 00:45:20 Not sure.
Liudmila Molkova 00:45:22 There was a discussion with Alex at some point that, they actually wanted ports.
And we had the full thing, and this is why we didn't add ref attributes, or there was discussion that we don't know how to approach it.
But it seems, at least from Alex's side, He supports this.
And everything was addressed.
I believe.
Okay, this, this is addressed.
And… conflicts are resolved, so I'm just going to merge it.
Sorry for the… Detour, but I think it's related.
Aaron Abbott (Google LLC) 00:46:06 Yeah, I think I kind of remember some of the context with Pydentic, and we had… we were discussing, like.
Oh, is it better to have more small parts? We were mostly discussing it from the perspective of the person consuming the telemetry.
And… it was… it was all kind of hypothetical, to be honest, so I think… like I said before, I think maybe testing out some heuristics and seeing what works well would be a good way forward, since we kind of… I think we support both, I don't think we need to make any change.
And yeah, I think… From the instrumentation perspective, like, the network… Impact if we do the, the, the content.
Like, the content addressed hashing.
I think that could be a big improvement, but obviously then we have to hash everything, which is the sort of the flip side. But I think it would be super cool to see if you have, like, a prototype of doing this.
How it works.
Dylan Russell 00:47:05 Okay.
Yeah, I had the same thought of, like, deduplication.
Because if you do it at the part level, you're gonna get a lot more, like, deduplication, probably.
Because you get people sending, like, the same… Same stuff again and again, so… Yeah.
But… Alright, I will prototype something and come back to that.
Aaron Abbott (Google LLC) 00:47:32 Cool. And maybe… I was gonna ask one other question, but you wanna go ahead, Limila?
Liudmila Molkova 00:47:37 No, no, no, go ahead.
Aaron Abbott (Google LLC) 00:47:39 Yeah, we also had a PR… I think we merged it, and it was for, Conversation ID.
based, like, uploading, or maybe not necessarily uploading, but doing the inference with previous conversations referenced, because, some of the APIs, like, interactions work like this one.
Liudmila Molkova 00:47:59 Of the previous request AD or something?
Aaron Abbott (Google LLC) 00:48:02 Yeah, yeah, exactly.
Liudmila Molkova 00:48:02 Yeah, we should have it.
Aaron Abbott (Google LLC) 00:48:04 Yeah. How does that work with this one, Dylan, do you think… It's kind of… Orthogonal.
Dylan Russell 00:48:11 Yeah, I think it's a… different… Ding.
Yeah, I know some APIs let you, like, continue the conversation through, like, some ID. Is that what you're talking about?
Aaron Abbott (Google LLC) 00:48:28 Yeah, because it kind of does a similar thing, except you make, like, a linked list of parts, as opposed to having all of the content chunks stored in each prompt.
But it's kind of the best we can do based on the calling convention of the thing we're instrumenting.
Dylan Russell 00:48:46 Yeah.
Bless.
Liudmila Molkova 00:48:48 The impact it would have, that if it becomes prominent to… And it seems it's becoming more popular to continue the conversation with the state maintained by the model provider.
that this optimization would not be necessary. There will be… One, two parts, anyway.
Aaron Abbott (Google LLC) 00:49:09 Yep.
Liudmila Molkova 00:49:17 Cool, so it sounds like this is the implementation thing, and both implementations could be done, and we are still, like, we don't have a specific favorite, and… we don't… At least for my site, I don't see the need to describe the uploading mechanism in semantic conventions.
Dylan Russell 00:49:49 Yeah, that's a good question.
Whether that should be prescribed or not.
Because, I mean, yeah, I don't know, it's nice if everyone does it the same way.
Right.
But, yeah, maybe it's better to start with… Us implementing it, and see what people… I don't know, build the feature, see if people like it, and then maybe come back to the semantic convention.
Yeah.
Liudmila Molkova 00:50:34 Dawn?
Don Branson (International Business Machines Corporation) 00:50:39 So, interesting, sort of thoughts. One of the things I'm wondering about is key use cases. Would this be for, like.
Agent workspaces, where it generates, sort of.
incremental or iterative deliverables that it uses to make decisions on? Is this… Like, is that kind of roughly where you see this being most valuable?
Dylan Russell 00:51:07 I think it's… It's for when, like, a large part is being passed to the model.
Don Branson (International Business Machines Corporation) 00:51:13 Yeah.
Okay.
And sometimes, like, I'm thinking about things like deep agents, or… I have sort of an implementation where I create a graph that is, on the fly that's used to make downstream decisions. It's… It's larger, but it is related to, sort of, work that an agent does. And so, in terms of traceability.
You want to be able to, Sort of relate to it, but you don't want it part of the… Like, you know, OpenTelemetry just isn't meant to store Like, large objects like this, so it's on the side.
Liudmila Molkova 00:51:54 Yeah, exactly. So this is for when we record either agent input-outputs, or the intermediary inference calls their inputs-outputs, whether to record the whole input-output as one blob, or Multiple blobs in external storage.
I'm… I'm… I'm thinking it would become… semantic conventions, an interesting concern. So today, the implementation is the spec. We have one implementation of completion hook in Python.
And it works a certain way, but let's say Entropic, with their native instrumentation, would decide to support completion hooks, and they don't want to take dependency on Teal GenAI, and they will provide their own completion hook.
Then we might need to agree better on the interface and, some details of the behavior.
And then it would become something we probably need to spec out somewhere.
Dylan Russell 00:53:08 Yeah.
Liudmila Molkova 00:53:12 Yeah, thank you for bringing it up.
We have one more… Item on the agenda… Okay, Sounds like it's easy to address.
We have 10 minutes. Any last-minute topics?
Have never happened on this call that we ended early.
I don't want to let you go. I want to do some discipline thing.
And look at the… PR dashboard and see what we can… Make progress on.
Yeah, I can't. So this one…
Aaron Abbott (Google LLC) 00:54:02 I could rep number 608, I think, Trask, just since you… I could ping you if you prefer, but it's almost identical to the one you already approved.
Trask Stalnaker (Microsoft Corporation) 00:54:11 Yeah, 608, I'll pull that up.
Aaron Abbott (Google LLC) 00:54:14 Yeah.
Liudmila Molkova 00:54:18 Oh, Habiba, go ahead.
Habiba Mohamed 00:54:20 Hi, y'all. Hey, it's been a while, like, a couple months, but, I wanted to bring 427 back up, Liudmila. I addressed most of the comments, I think I need to rebase, but, I think it was already approved by, one of the folks, Aaron, from the, Model Armor team, so… If you could take a look at that when you get a chance.
Liudmila Molkova 00:54:41 Yeah, thanks.
I… I wanted to ask you, so, if I remember correctly, we… we kind of got stuck with the scenarios, and that was the reference scenarios that we have. We are limited to some, Client libraries for… for guardrails, and there aren't many.
Exactly.
Habiba Mohamed 00:55:05 Yeah.
Liudmila Molkova 00:55:05 Yeah, and it's… it sounds like you addressed this, but I was curious, from your side, is it what you're interested in? Maybe… because if you're interested on the, like, more, like, reporting it from the server side.
Where you control instrumentation fully, and you have way more information.
And Model Armor in the same story, and maybe some other providers.
How can we… Come up with a good way to add this information that only provider can add, and we don't have reference scenarios and cannot add them here.
Habiba Mohamed 00:55:46 Yeah, that's… I think that's sort of the chicken and the egg situation we're in, where we want to be able to expand it, but then it's not, like.
like, publicly documented, right? So, I don't know if… so what I did was I removed, any portions that aren't supported right now, and so I don't know if we should maybe iterate and merge this in, and then see if then we do get additional… Like, I, like, I don't think there's any other, other than, like, model armor that we have available, so…
Liudmila Molkova 00:56:15 Yeah, and would you be interested in coming back once there's anything public out there?
And, like, using the actual implementation that you have is maybe more things that are in this PR.
To… Add these extra things.
Habiba Mohamed 00:56:35 oh, like, kind of closing on this, and then coming back when there is available? You're saying that it might not be… Is that what you're saying, or are you saying let's merge it, and then we sort of follow up?
Liudmila Molkova 00:56:45 I mean, if it… covers the client libraries. I might have some cosmetic concerns, but let's merge it, regardless. But then, it sounds like It does not… address the need that you have, and also the people from Model Armor and Google have.
And it does not address the need of all the other providers that do guardrails on the server side.
And I'm thinking, like, we should probably address the gap, but for this, we would need to have something, like, public that you would probably implement for yourself.
And, we would be able to look at it and use the documentation or the actual information reported by the provider as the sign that, okay, this is needed, and what is the common things between different providers?
Where maybe people on the call have other thoughts on how, like, we can, in the future, and for this, address the, okay, this is not in the client library scenario.
Habiba Mohamed 00:58:01 So I'm definitely open to following up. It would be useful for us internally. It's not public… like, it's not available publicly. We would be able to utilize this, server side and some of the things that we do. And then some interesting follow-up or work that's kind of come out of this. I don't know if it was… someone else had sort of tagged, the need for detections, sort of, like, spans for, like, AI-based threat detection as well, which sort of would… would essentially take, like, be a follow-up, right, of, like, any sort of spans that were emitted for, like, outputs for classifiers, security events.
I'm not sure if there are any sort of public-facing… I don't think so. I think a lot of them are more facing… more, like, SOC-related, and not so much, like, AI threat detection.
But that's a good point. I don't know if anyone else in the… And the team has any thoughts, But we can… we can continue offline, yeah.
Liudmila Molkova 00:59:07 Yeah.
Cool. I'll… I'll take a look, thanks. And I'm moving and checking if it shows up on our dashboard properly.
Okay, so if, it's probably, well, like, caused by some of the changes, when you have a moment.
please resolve the conflict, but I'll put a mental note to take a look. It's just when… when there are quite a few PRs here.
And I think where we're trying to focus is, like, going from top to bottom, and if it doesn't show up in maintainers or reviewers.
Then it's just… nobody would… would notice it.
And, there is the command if you see, like, if you're… There is this comment here.
The status of the dashboard.
And if it's not waiting for reviewers, but you believe it should be, then… there… there will be a command here, in this, collapsible box. And it's not for… for you, Habiba, it's just for everybody to explain the review process and how to, bring more attention to the PR, sorry.
cool.
Okay.
There is this one, since we're here.
And I think it lo- it's a… It's a reveal one, and it has a couple of approvals, but it's from me and Aaron, and if anybody, not Google.
would be interested to take a look. Please go ahead.
Trask Stalnaker (Microsoft Corporation) 01:01:09 I didn't approve that one.
Liudmila Molkova 01:01:11 No…
Trask Stalnaker (Microsoft Corporation) 01:01:13 Which…
Liudmila Molkova 01:01:14 5, 2, 4.
Okay, and I'm just going from top to bottom, and sorting by the things that already have an approval.
There is a few more trivial things.
That, I think, are… Almost ready.
So this 458 fluid dulsel… Be nice to have.
There are also a few, like, trivial ones that we didn't pay attention to in a while.
Or maybe it got merged, so this one… Since… Alright… Okay, I'll take a look at this one, but it looks good.
Oh, interesting, this… This is another classic failure mode that we have, that, we created The reference tests allow you to write anything, so it doesn't use any library, it just puts the… Provider here.
Anyway, I'll comment on this one. We are at time. Thank you all.
See you.
Trask Stalnaker (Microsoft Corporation) 01:03:36 Bye.
Pam Dixon 01:03:38 Thank you!
