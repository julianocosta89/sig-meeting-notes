SIG: GenAI SIG
Date: 2026-10-20
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Surya Teja 00:01:07 Hey, hi folks.
Trask Stalnaker (Microsoft Corporation) 00:01:11 A…
Josh Bonczkowski 00:01:14 Blue.
Trask Stalnaker (Microsoft Corporation) 00:02:06 Please go ahead and add any topic.
To the agenda.
Alright. Let's get started.
Let's start with, Manish. Are you… yes, hey!
Mohnish Srivats Ramesh 00:03:39 Hey, Rosque. Thank you so much.
It's been quite some time since I came here. I think… what I've added and what TN from AWS has added is kind of similar, so… can I… can I share my screen for a moment?
Trask Stalnaker (Microsoft Corporation) 00:03:55 Absolutely.
Mohnish Srivats Ramesh 00:03:58 Thank you.
Alright.
Yeah, I think, so… I just resolved all the merge conflicts, it's on the evaluator Provenance, and this is in the dashboard, it's waiting on reviewers, but before… asking a few questions about the review process. I created a document for myself about what each field, how we have narrowed it down. There are four fields, like.
the ID, type, version, and setID. So, the first two fields are being emitted by either Azure AI or DeepVL, or DSPA, one of those, and version and setID, the reference set ID is something I was not able to emit it, so I kind of went through, some of the the rules, like the skill.md, the reference instructions, and it said if… if it is not… if you're not able to instrument it, don't propose a convention and open an issue and bring it to the GenAI SIG. So, do you recommend dropping these two fields? But we absolutely think that version and setID is very relevant to this provenance, but we are only able to instrument these two fields, so do you have any suggestions so that I could rework on this, or do you think the state of the PR right now is okay.
Trask Stalnaker (Microsoft Corporation) 00:05:31 I'm… Could you explain how, like, so you… it's not instrumentable in… Open source libraries, but you have a use case for it.
Yourself?
Mohnish Srivats Ramesh 00:05:44 Yeah, yeah, absolutely. So… Just… just a very quick view of what the PR is doing.
for the evaluations, we are writing the provenance, like, which means where is the evaluation coming from? Is it a rule-based deterministic evaluator, or… LLM SHH or a hybrid evaluator. We are just tracking the provenance, which means if that evaluator would have an ID, or a type, and what version of that it would be, and… What… what is the… the ground truth reference that is being used?
For the evaluations, there are these three libraries, Azure AI, Deep Event, and DSPY.
Yeah, I was not able to instrument, version, and reference it in any of these open source libraries.
So, but… In some of the work that we did with some clients in regulated industries previously, we had the need to Include the version and the reference ID.
So… I was thinking that I could just keep these two in this PR, and then open a new issue for these two.
Because these two are very similar to Providence, maybe… Capture it up, record it as a capture gap, and then… Because I was not able to automatically instrument in any of the open source libraries.
So if you have any suggestions, that would be awesome.
Trask Stalnaker (Microsoft Corporation) 00:07:19 Ankit, go ahead.
Ankit Singhal 00:07:22 Hey, hi. So, I know for… I can speak for usual evaluation, so the evaluator ID also had the version of the evaluator, so that's why we didn't have a dedicated field, evaluator.version.
But I could see that going either way, where you want to have, like, evaluator as well.
constant thing that you evaluate, and that you can have multiple versions as you improve it. So, I think both makes sense to me. But I think for Azure evaluation, why… evaluator.version does not exist, because evaluator ID already had the… Kind of version.
Mohnish Srivats Ramesh 00:07:58 Oh yeah, I totally understand. Yeah, I totally understand.
Yeah, I think, that's a… That's a fair point to bring up. Then, in that case, let me see… since we are able to track the version ID itself, I would reconsider the version field in this PR.
And… yeah, I was not able to instrument reference at ID in any of these cases, so… maybe I could open a new issue, for the… for the reference set, so that we have an idea how we are tracking the The reference set for the evaluations that we are doing.
Trask Stalnaker (Microsoft Corporation) 00:08:45 Neil, go ahead.
Neil Yashinsky 00:08:46 Thanks, Trask. I hope I'm pronouncing this right. Is it, Mohnish or Mohnish?
Mohnish Srivats Ramesh 00:08:51 Yeah, it's Mohnish, yeah.
Neil Yashinsky 00:08:52 Thanks, hi. I don't know if we've chatted before, I was just gonna say, if you wanna Slack me, I may have an opportunity to, I guess, instrument, this field, or, you know, one or four of them, or, you know, even… what's the word I'm looking for? Project them onto how I use this in a project. If you want to Slack with me offline, maybe we can find, see if I might be able to… help you, flesh this out, or whatever, put a little close on your straw person, or whatever my mixing my metaphors is, in order to, help you… Illustrate how you think this data could or should look.
If you'd like.
Mohnish Srivats Ramesh 00:09:34 Yeah, absolutely. Yeah, absolutely. So, I'll share all the relevant information, like the PR link, the documentation of what we are trying to achieve, like, the description of the fields. I can absolutely slack you. Thank you so much.
Neil Yashinsky 00:09:46 Sure, sure thing, happy to help.
Mohnish Srivats Ramesh 00:09:48 Yeah, yeah, and I think that was the only thing that I wanted to discuss, and… Yeah, thanks, Trask.
Trask Stalnaker (Microsoft Corporation) 00:09:56 I have a question, Ankit, about the version encoded in the ID. So, Mohnish, when I first saw your list there, the dot version, The… there's, you know, a lot of precedent in semantic conventions for having a, a version… having a dot version on something.
So I could see that, but I am curious to understand, Ankit, you were saying that can also be encoded in the ID, and… is that… What are, sort of.
Ankit Singhal 00:10:35 Oh, yeah, I was just mentioning, like, why, like, Mohnish was not able to find that field in Azure Avaluation. I think the only reason was, like, how the versioning of assets, in a way, like, here evaluated, where if you have to identify a specific evaluator, you have to give, like, the absolute evaluator relevance slash version slash, like, or something of the sort. But, that's not, not meaning that it has to be done that way, but it's just that, like, that was the reason. But, I think it makes sense to do it either way.
I think.
Trask Stalnaker (Microsoft Corporation) 00:11:09 If you had it, if we had a separate .version attribute would you… Do you think the Azure AI Evaluator would split those?
Or that's just kind of the way that the ID works in the Azure AI Evaluator.
Ankit Singhal 00:11:30 Like, for emitting, yeah, for emitting the evaluation design, like, the telemetry, I mean, it can be done. Not an issue at all. Just like, when you have to evaluate and get that actual evaluator, like, what service does is basically If you don't provide the version, it gets you the latest one.
So… Would that be beneficial?
Trask Stalnaker (Microsoft Corporation) 00:11:52 Is it beneficial to be able to track them separately.
I'm just thinking of being able to… see, You know, an evaluator changes over time, but have that.
Ankit Singhal 00:12:05 Yeah, definitely, definitely it would be. And right now, the Azure A evaluation does that as a part of the evaluate by IT, but I could see it being a separate field as well. Yeah, not a possibility, definitely.
Oh my god.
Trask Stalnaker (Microsoft Corporation) 00:12:25 But Mohnish, it's always a good option to, as you suggested.
Splitting things out, so that we can, you know, land the less controversial or the simpler things that, And, Them.
Working through the version and the other attribute.
Mohnish Srivats Ramesh 00:12:49 Yeah, sure.
Yeah, sure. Thank you so much.
Trask Stalnaker (Microsoft Corporation) 00:12:58 Cool, moving on, we've got… Haoting,
Haotian Hu (AWS) 00:13:08 Hey, everyone.
Oh, so… Hey, it's my first time here, yeah, thanks everyone, giving me the chance. So, basically, we are proposing to add some, new convention fields, especially to support needs. Like, we have some customers, they run their evaluation outside of AWS, and they want to export their evaluation result to AWS.
But due to we don't have, like, a standard convention on this result, so when we interpret these results, like, hallucination, like a serious good, a wise good. We have some kind of… our UI experience is not so great, so we are proposing to add, additional, GenAI semantic emission fields to help, customer get, like, a unified experience.
We… so today, we're already adopting, Hotel convention as much as possible. We like to keep that way, going forward, too.
owned.
But, some… there's some gaps, definitely. So we… So we're starting, four fields sync, which is the minimum one to… for our customer experience.
So we want to get, get some, feedback, see if, communities, a DRN.
Yeah, so basically, like, the first Y is the score direction.
Which is to solve the problem, some customers have evaluation score, like, 01, 0.1. We don't know if, maximum is good or minimum is good. And, the evaluation level.
Which is, used to… because in AWS, we… when we help customers evaluate a target, the target can be either a section, which is, like, a conversation information.
Or a trace, which is, like, a single term, like, input… user input and aging output. And all spam, which can be, like, some tool usage.
This, we have three levels here, which is, we internally are using.
With, when customer exports those ZVA results, you want to have, have the ability to.
like, mark the ZVA results based on which level, so our UI can show them, correctly. The third one is the score, the writing scale.
Which internally, we have some, like, better operating for rating scale, similar attribute. Basically, we are differentiating, evaluators to see, okay, this evaluator results are numerical or categorical.
Today, we have, like, two types of the evaluator.
On the written scale.
And the last one is, evaluation tech, which, which I'm also seeking if OTEL already have some sort of, tech support.
It doesn't need to be, like, the evaluation type, but I think it can be, like, any type, which is, maybe it can be… if I can find something broader, that's also work here, yeah.
Yeah, so that's, for, fields. Generally, we want to get some feedback.
And also, before we, because we don't want to block by this, internally, we are trying to see, using something like, AWS namespace, like AWS. evaluation.score direction, so we want the customer to use that first as a temporary thing, before OTEL has, clearly, Commission on it. Once OTEL has it, we will first, we will support the hotel front as priority for back to our AWS naming space.
Yeah, so that's the approach we're probably gonna take.
Trask Stalnaker (Microsoft Corporation) 00:17:16 Yeah, definitely that's a good, Good.
Approach for, being able to move forward, but yes, appreciate you bringing Be bringing it here also, so that eventually we can all align.
A quick question, about this, the direction, and I don't remember if we already Defining the, in score, what's better or worse.
And wondering if we could, instead of having this, just say that, define what the direction is, and if it's not that direction, then you should just flip The score… flip your score around when reporting it.
Neil Yashinsky 00:18:15 Yeah, I was thinking something along the same lines, based on the nature of the… like, the time series database sounds like, like, this can be, what's the word I'm looking for? Inferred, I guess? Rather than… Is that what you're saying, Trask? Like, basically, compared to the measurement before or after, that you should be able to… Evaluate the metric, and then… Determine the direction?
From looking at the data? I mean, I really like the… the… what you have here, I think it's… I actually, I didn't see it before, I'll admit, this, actually, I could probably use something a little bit like this. And so, yeah, I think it… I like the value that you have to pose here, but Trask, I don't know, I don't wanna… I'm not trying to put words in your mouth, but maybe synthesize your thoughts as, like.
score direction is, superfluous given the metrics come with the time series database needed to always evaluate this at comparison time, I guess? Is that what you're saying?
Trask Stalnaker (Microsoft Corporation) 00:19:18 So, I think this is a little different. I think what you're thinking of is basically, like, the tangent. Like, is… are things getting better over time, or worse over time?
Where I… this is… meaning, like.
like, is score zero, ask score was 0, and score 1. Is 0 better than 1, or is…
Neil Yashinsky 00:19:39 Oh my gosh.
Trask Stalnaker (Microsoft Corporation) 00:19:40 One better than zero.
Neil Yashinsky 00:19:41 I miss… I see now, maximize, minimize, my mistake, okay, thank you.
Liudmila Molkova 00:19:46 I think, like, when we… And there's discussions around the square.
Or you kind of give up on trying to normalize it, because a lot of the times, these are the… either the… let's say, ML metrics that are very well known somewhere and defined, and the direction is defined, but we are trying to record them in different places. Oh, and the same attribute, let's say.
Or they are not numerical at all.
And it is more like a category, or is this content harmful?
Right? You cannot really put a score around it, and we needed to find something that works among the zoo of ovulators, and I imagine it's still a zoo, and even the similar ones that measure the content harmfulness do not agree on the scale.
So, I think, at least in the current world, it kinda… impossible to normalize, but it's been a while since I looked into evaluations.
Haotian Hu (AWS) 00:20:56 That's exactly the problem I'm facing. Our customer, especially even today, in AWS, they can define their customer evaluator with their own definition.
But Samsung can still get evaluated animation from APIs internally, but if support from third parties, we had no idea of that.
So, we really, really like to see either evaluation results carry this, or evaluator definition, we have some convention on this. So, when we try to normalize internally, we can know how to normalize it.
Liudmila Molkova 00:21:35 I want to call out the pro- oh, go ahead.
Trask Stalnaker (Microsoft Corporation) 00:21:36 Please, go ahead.
Liudmila Molkova 00:21:38 I want to call out the problem we have for regulators, that they are mostly not open-source libraries, but vendor-driven.
And we have a very, unreliable way to support them in semantic conventions. We don't have a good Visibility into internal, sorry, what's needed, where, and how to instrument them.
Josh Bonczkowski 00:22:07 Very true, and I'll speak up for, like, from New Relic, we have been building evaluations internally, emitting events, like, different events, but customer, you know, our own events, that actually have basically the same format to them. So, like, it lines up very well, just different names of things. So I'm glad that, you know, Ocean, you guys are bringing this up for OTEL, because it would be a nice thing to kind of normalize on our internal representation.
Trask Stalnaker (Microsoft Corporation) 00:22:39 And, I mean, we do… I think, we've kind of scoped our current semantic conventions definitions and decisions around open source libraries, because that's the, like, easiest for us.
And most concrete.
But certainly, I would assume in the long run, like, we… there's some… Categorization of things that… That's not going to work for… And that's kind of where we're building this coalition of people here, representing, various vendors to.
I feel like there should be some… Way for us to, lean into that and be like, okay, we've got, you know, these Well-defined use cases from multiple, people. We just don't have open source representation for them, and that would still allow us to move forwards with things.
Haotian Hu (AWS) 00:23:57 Yeah, so it looks like we had technology the same problem.
as next step, do we want… I mean, I can propose some… Cr… PRs, or…
Liudmila Molkova 00:24:11 Bing…
Haotian Hu (AWS) 00:24:12 The problem…
Liudmila Molkova 00:24:12 It would be. Yeah, the…
Haotian Hu (AWS) 00:24:14 Bye.
Liudmila Molkova 00:24:15 We've seen it, as Mohnish if he's still here.
that, the… evaluation PRs tend to get stuck, because The people who are approvers Either don't have interest in evaluation or expertise, and… We can work around this, but… in order to approve this, I would need somebody who, like, has some skin in the game, who works in evaluations, who reads evaluation results, who builds dashboards and evaluations to support it. Like, Josh, you mentioned, you do this in New Relic.
And even if you don't have approver powers, or many sh… can you folks work together? And, like, your consensus would be a signal that we should, approve and merge it. And without, like, your consensus and you working together, I have no idea whether it's a good addition or not.
Josh Bonczkowski 00:25:21 Yep, totally understand, and I've actually already sent this link back to our lead engineer on this area, so I'm starting that conversation when he's back in the office tomorrow, to get him to come review what has been put in here.
Liudmila Molkova 00:25:35 Awesome.
Trask Stalnaker (Microsoft Corporation) 00:25:38 And I would suggest, Like, the score, these two kind of, feel like a good first, step.
It certainly makes… made sense to me, your explanations of these, and it feels like is our… we already have score.
Right? So, the fact that That is… So ambiguous without these two things.
Ankit Singhal 00:26:08 What's a good day.
Trask Stalnaker (Microsoft Corporation) 00:26:09 Feels like a case that could be made.
Easier than… than… and then, you know, tackling these other two things separate.
Ankit Singhal 00:26:18 Okay.
Yeah, so… I'll also send this PR across, within our group. I think we have a team who works on evaluation pretty closely, and I work with them as well, so I'll do that. I think for, the third point, scores, rating scale, I think there was already an open issue regarding it when the first graduation result PR went in.
So I think it'll be good to just pick it up. I don't know if it's in the old group, or it's there in the new request. If not, I can… I'll definitely pull it up instead.
Trask Stalnaker (Microsoft Corporation) 00:26:53 Might be this one that's linked here. Score range.
Ankit Singhal 00:27:01 Yeah, yeah, exactly, yes.
Trask Stalnaker (Microsoft Corporation) 00:27:03 Okay.
Yeah, yeah, thanks.
Ankit Singhal 00:27:05 at Ramesh when the initial PR went in, so…
Trask Stalnaker (Microsoft Corporation) 00:27:11 Alright.
Sounds like we've got a good… Passed.
Plan there.
Yes. Next topic I threw on with Nikhil.
Wanted to draw people's attention to it, just going through the review process, myself, but, I think generally makes sense to me.
And…
Liudmila Molkova 00:27:48 Oh, Trask, you had an open comment. Maybe we can talk about this a little bit.
Trask Stalnaker (Microsoft Corporation) 00:27:53 Yeah, yeah, I saw your reply, and it makes sense to me. I was wondering if that was, sort of, there were future… Ambitions there for the attribute.
Liudmila Molkova 00:28:08 Yeah.
Trask Stalnaker (Microsoft Corporation) 00:28:14 Yeah, so that… that makes sense. I'm… I'm good with that.
Liudmila Molkova 00:28:19 Okay, sounds good, thank you.
Trask Stalnaker (Microsoft Corporation) 00:28:25 So this is, about… agent, agent-to-agent handoffs, via tools. So it's a tool span refinement to track, what agent is being, Hand it off to, and also… Whether that handoff is… Basically, synchronous or asynchronous, on, if it's… Delegation, getting a return back from it, or… Delegation, and that agent is then responsible for handling the… Responding back to the user, or origin, or the web book.
Etc.
For as large as it is, it's actually fairly… simple, straightforward, after lots of, discussions. Thank you, Nikhil, I feel like it.
Came in to a good place, and… So anyway, yes, please look at it.
Comment on this.
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:29:48 That helped.
Trask Stalnaker (Microsoft Corporation) 00:29:51 Nikhil, anything you wanted to say about it?
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:29:56 Tammy?
Neil Yashinsky 00:29:58 I think just barely, there's some muffled noise, Nikhil if you're trying to talk, or maybe background noise.
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:30:04 Hey, can you hear me now?
Neil Yashinsky 00:30:05 Yeah, there we go, yes.
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:30:06 Awesome. Yeah, I was just adding, yeah, thank you for all the reviews, yeah, definitely it has been, scoped to… It's helped to scope it down to a tool so that we can get this PRN, definitely helps.
Trask Stalnaker (Microsoft Corporation) 00:30:27 Surya?
Surya Teja 00:30:30 Yeah, just a quick question. There is an effort to merge both agent and workflow spans. From my nieve understanding, this PR is not going to clash with that.
PR, but, Is my assumption right?
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:30:50 Yes, so this only adds… A refinement on the execute tool span, so it adds two attributes, to record the, agent Or the destination, where the handoff is happening, or the transfer is happening to.
Surya Teja 00:31:12 Okay, okay, okay, thanks, thanks a lot.
Trask Stalnaker (Microsoft Corporation) 00:31:22 Alright.
Moving on, Ankit.
Ankit Singhal 00:31:29 Oh, hi, thank you. So, first of all, thanks, Lumina, for the reviews.
And, I would just, I guess all of them. I made sure of that yesterday night before the meeting, so, please help, review the PR. Liman, I think I did, reply to the comment that you had from last, week.
So, about the child span part, so please, take a look and… WN… If… there are no major concerns, I would definitely like to move into getting this merged.
Liudmila Molkova 00:32:09 Yeah, I'm mostly curious what you've done with the two call parts. Do they show up now?
Ankit Singhal 00:32:15 I'm sorry.
Liudmila Molkova 00:32:17 The, the two call parts.
So, like, in case of… Gemini, the… we report one span for the full tool loop.
And whether, you found a good spot for the total parts.
Ankit Singhal 00:32:32 Yeah, for the generation, I think for… I think it was Gemini Live 3 per month, if I remember correctly. So, I think tool call part and the response part being part of the generation, like we do for, like.
the text space info site. I think that made the most sense to me, because The other, part, as you mentioned, was about, like.
Where that tool execution happens, and whether that can show up as a child is also, not heavily reliable, right? So… For those reasons, I wanted to put that as part of them, basically.
Liudmila Molkova 00:33:10 Okay, cool. Yeah, makes sense.
Thank you.
Ankit Singhal 00:33:14 Bingo.
Yeah, and I think apart from that, I didn't see any major, comments. I think I addressed most of them, and if there are any… comments, or feedback that feels like needs to be a discussion, I'm happy to do that. But so far, to me, at least, I looked at all the comments last night, and… This was a major last one, and… Did that unbox.
But yeah, thank you so much for the support and the feedback.
Alan as well, you know, Alan hasn't seen him on the call, but yeah, thanks so much.
Liudmila Molkova 00:33:57 Yeah, thank you. Oh, would… anybody else, like, let's say, it looks good, I have proof. We need a second approver. Do we have other people who are interested in the topic?
Okay.
Trask Stalnaker (Microsoft Corporation) 00:34:09 I don't…
Ankit Singhal 00:34:11 Oh, yeah. I couldn't deliver.
Trask Stalnaker (Microsoft Corporation) 00:34:12 you.
Ankit Singhal 00:34:13 That's true.
Trask Stalnaker (Microsoft Corporation) 00:34:13 Just from a general… semantic GenAI perspective, I don't have any specific voice, Interest or knowledge.
Dylan Russell 00:34:28 I did add one comment this morning that we might discuss.
Which is that these… like, at least the Gemini Live uses, like, WebSockets.
And I guess with WebSockets, there's, like, one HTTP request at the start.
Which can have, like, the trace parent header.
And then afterward, everything is through, like, a raw TCP socket, and there's no headers, like, allowed.
So, the question is, should we… Like, add some guidance to add… a… Add the trace parent header to that initial GET request.
Like, could that be interesting for… instrumentations to do.
Aaron Abbott (Google LLC) 00:35:24 Is it kind of implicit already? Like, do we need to say anything?
Dylan Russell 00:35:31 Yeah, maybe not.
Ankit Singhal 00:35:34 I think that was my first reaction as well. I don't know if he explicitly calls out any other places or not, but yeah, I think, good point, as you mentioned, there's a transfer over from HTTP, and… That's the other side, so… But yeah, I agree.
History.
Liudmila Molkova 00:35:52 It wouldn't help anyway, because the session and individual Operations within session are orthogonal to each other.
Dylan Russell 00:36:05 all the operations are kind of, like, stand on their own. Is that what you mean?
Liudmila Molkova 00:36:10 I mean, like… the session can last for, I don't know, 10 minutes, and there's back and forth, and there are multiple individual Generations or turns within.
And… we don't even… Suggest a record session span.
Right. Because it's so long, and… Some were orthogonal.
So… it's… even if we… even if it's a HTTP request, and even if it's propagated, like, the correlation between client and server for individual like, I said this, and then model did that. It would need much more. It would need the protocol between, like, for an individual WebSocket message to support context propagation.
Dylan Russell 00:37:03 Right.
But I still think it could be useful for, like, the initial request to get traced, and to see, like.
What was done on the client side that led to that first request?
And then… Like, the server has the same trace ID and does some stuff.
Liudmila Molkova 00:37:22 If it's HTTP, it would be traced if HTTP instrumentation is enabled.
Dylan Russell 00:37:29 I think for… yeah, for WebSockets, we might not have, like, any instrumentation.
But… Yeah.
Aaron Abbott (Google LLC) 00:37:40 I was gonna say, it might be good to have this as, like, a non-normative thing in the reference scenario, if that's possible. I don't know, like Dylan mentioned, the WebSockets doesn't have… like, the WebSockets library does its own thing, so it doesn't reuse the HTTP instrumentations we have, at least for Python, but… It would be interesting to see, like, if it becomes, for example, the… Parent spend of the real-time stuff underneath it.
I don't know if that would be possible to do in the reference Ankit.
Liudmila Molkova 00:38:13 It's a separate layer. How is it related?
Like, in inference, we don't talk about, okay, propagate context.
Wh-white, why here we would…
Trask Stalnaker (Microsoft Corporation) 00:38:29 We're generally… model… the, the GenAI at the logical layer.
So this is… I think that's… This is starting to get into that physical layer of… How to propagate context.
Aaron Abbott (Google LLC) 00:38:51 I just remember we were talking about how the spans would have no parent, and it would be hard to read. Like, I agree with you, but it might… and definitely not a normative thing, I was just kind of curious if it would be useful to see for reviewers.
Trask Stalnaker (Microsoft Corporation) 00:39:06 Which spans the server spans?
Or the…
Dylan Russell 00:39:11 I think it means the client spans.
Aaron Abbott (Google LLC) 00:39:13 Yeah, and like the… I think we have events in here as well, right?
Dylan Russell 00:39:21 Like, we say the spans and the events have no parent somewhere in this PR, I think.
Liudmila Molkova 00:39:27 Oh, this was Shadrimu.
Aaron Abbott (Google LLC) 00:39:30 Yeah.
Ankit Singhal 00:39:32 -Oh.
Dylan Russell 00:39:35 Is that true? I might have made that up.
Ankit Singhal 00:39:41 I can… I can score the, like, PR to see.
anything that I had to say. It's yes, but I would love a little more that it's not the intention.
Aaron Abbott (Google LLC) 00:39:53 Okay.
Cool, and maybe…
Trask Stalnaker (Microsoft Corporation) 00:39:55 That wouldn't need… that wouldn't need… Propagation, if we're just talking about the client.
Sidespans and events.
Dylan Russell 00:40:13 Sorry, I didn't follow that.
Trask Stalnaker (Microsoft Corporation) 00:40:16 I was trying to understand what, You… how it relates to Trace parent propagation, if we're just talking about client-side spans and events.
those… I don't think would… you could… We can model those.
And we should model those, because those are logical.
Client spans and events.
But I… I don't think we need trace prob… like, I don't think you need the trace parent to propagate to the server and back, necessarily, to be able to link those… events, or spans, nested events, to the original span.
Dylan Russell 00:41:08 I think that makes sense.
Yeah.
Trask Stalnaker (Microsoft Corporation) 00:41:15 Streaming is fun.
Ankit Singhal 00:41:17 Observability.
Trask Stalnaker (Microsoft Corporation) 00:41:18 We've had so many discussions in RPC land.
Ankit Singhal 00:41:24 Swimming is fun, but not for others.
Neil Yashinsky 00:41:29 Their fur girl is real.
Ankit Singhal 00:41:36 Cool, thank you. I'll discover the PR just to see if there's anywhere that, there cannot be any… parents can contextual besides, so… propagation, or it just talks about that it cannot be done, so… I'll definitely remove that. That's not the intention, and… Yeah, thanks again for the use for the…
Trask Stalnaker (Microsoft Corporation) 00:42:04 Cool.
Let's go to, the next topic, which is Neil.
Neil Yashinsky 00:42:11 Hey Trask, thanks. So, I may have mentioned this a time or two in the past, and just a little bit of an update, and it's, for me, trying to wrap my head around all the… rich, context and details of the, you know, the AI semantic conventions, I've often struggled to… be able to hold, like, all the abstract concepts together in my head at one time, and make decisions, and so, some of the work that I've been doing has lent itself very readily to… using these conventions and testing them out in the real world and seeing how they perform, and so I just wanted to… I think it may be helpful and useful for others as well, so I've just been trying to, you know, in a open source sense, share my work. I'm happy to talk a little bit more About, how this works?
But basically, there's a benchmark that I'm working on. It tests, You know, ability of 31 models to generate an application.
And, that one in particular has been really helpful in… testing across multiple, you know, OpenAI, multiple vendors, OpenAI, Anthropic, and Google in particular, have, like, native instrumentations.
But I haven't been able to test everything in there, and specifically, like, the next one, what I call reference instantiation 2, is for a Gemma, a Kaggle competition, I hope I'm pronouncing that right, Kaggle competition, and this one gave me a chance to exercise, some of the ADK stuff.
Really well. And so, Yeah, I don't… I mean, I'm happy to get into as much detail, Trask as the group wants or not. I've been trying to put together enough stuff that it will be, you know, for folks who want to keep score at home, they'll be able to see, like, more readily Links from here to, like, what the tests say, and, you know, how… how… the, you know, developers or whatnot who have these PRs may or may not want to… you know, change their implementation, how the, obviously the, you know, you kind folks, you know, may be able to see some things that was harder to, if you will, grok or, you know, understand all the pieces of, without abstract.
examples to work from. So I'll come back with a few more details later. The last one is, is a newer one.
Shout out to Totoro or whatever, the Nekobasu, I hope I'm pronouncing that right, any, any people of, you know, Japanese, speak Japanese natively, let me know. But, that one in particular is, like, good for testing agent-to-agent handoffs.
And so I've had a chance to exercise that one a little bit internally.
And, you know, obviously I want to be mindful. These are obviously not specifically hotel projects, but they, I do believe, have a lot of value. That's why I've used them both to educate me on how they work, but also maybe inform even a few of the design choices around the conventions.
And so, yeah, thanks for the time for sharing that. Like I said, any more details, anybody wants, information, I am preparing to stand up a little portal for people who want more information. I'm happy to invite everybody here. And that will have, like I said, the more detailed information about I mean, it's there in, without links, right? But you could see the… all the issue numbers that are tested out, and informed, and hopefully, it is… Oh, I guess I already said it, but informative and helps the committee understand how this will behave, you know, in a real-world scenario across multiple vendors.
Thanks.
Trask Stalnaker (Microsoft Corporation) 00:46:17 What I think would be, help interesting for this group would be to, share traces.
from…
Neil Yashinsky 00:46:28 Yeah.
Trask Stalnaker (Microsoft Corporation) 00:46:29 Jeez.
Neil Yashinsky 00:46:29 I can do that, absolutely.
Trask Stalnaker (Microsoft Corporation) 00:46:30 Huh.
Yeah, in some kind of form where, you know, we can see, you know, having real, live traces from systems is… Very interesting.
And, yeah.
Neil Yashinsky 00:46:45 Yeah, great. And, one last one that I'll just mention, I think I may have mentioned this, it was 390 that we were just talking about, which is a little, side project for NetBSD, and it's a voice pilot.
For, like, you know, people who use screen readers or, you know, whatnot. And so, that might also be a handy way for, I forgot who was working on 390, if they wanted a little bit of… what's the word I'm looking for? Basically, an illustrated trace, I think, Trask, how you described it, or, you know, what you described, you know, as a means of informing that. I'd be happy to produce that for that as well. Thanks, Trask. Bye, everyone.
Trask Stalnaker (Microsoft Corporation) 00:47:29 Cool, thank you.
Let's move on to, Nikhil.
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:47:38 Hey, folks. So, so, in Microsoft, most of the agents run as, like, agent services, so… using, using S, using the client SDKs to represent the agent.
might not… Give us, like.
Or, let me say this. There might be, like, additional attributes that, you know, like, we capture or need or use on the… On the agent server that might not be represented in a… in, like, an agent running on a client, right?
So, I just want to understand, like, if we want to model those attributes in, in OTEL, so… what would be, like, best practices or evidence that, you know, would be needed to support that?
Or do we have a guide, maybe?
Trask Stalnaker (Microsoft Corporation) 00:48:41 Might be interesting to start, Erin, with sort of, the work that you did around the hosted agents, the, the… Agent Entity.
And sort of how that's… I hate… My understanding is that was sort of your attempt at solving this problem, or what… a piece. I mean, it has more, also, because entity attributes end up on all the… all the things, which is a great, also.
byproduct there.
Aaron Abbott (Google LLC) 00:49:23 Yeah.
No, I agree. We don't… we don't have a server span for Invoke Agent today, right?
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:49:31 Correct.
Trask Stalnaker (Microsoft Corporation) 00:49:31 Right.
Aaron Abbott (Google LLC) 00:49:32 Okay.
Yeah, I… So I think the agent entity is helpful for the attributes, but maybe, like, having the spin still useful, and I also know that, Liudmila, you have, like, a PR for, Adding the agent ID, Or, sorry, adding the main agent ID on, Invoke Agent, right?
Liudmila Molkova 00:50:02 Yeah, but I guess we… last time we tried, we got stuck around the question.
the invoke agent be the server, or there is a protocol level span.
that… Would be the server.
Or, there is now A2A span that would be the server.
Oh, no, not yet, but it's about to be merged.
And we kind of need to figure out how to… Approach it.
And… It… on one side, it makes sense to say, okay, this represents, like.
let's say I'm the… some… some form of the Agent platform.
And I only want to expose to users.
a certain amount of information. I don't want to expose the details about HTTP, or gRPC, or it doesn't matter.
Or A2A, or whatever, bespoke protocol.
I only want to say, okay, this represents the incoming point into my application.
And… On the other side, it also makes sense to say, okay, Please track your… Protocol separately, and then call it an internal.
The first approach seems more, like, pragmatic to me, that you could Say it's a server, and hide all the transport level details from your external users.
Aaron Abbott (Google LLC) 00:51:53 Yeah, and also, like, the conversation we've been having in other weeks about the, the turn.
Neil Yashinsky 00:52:01 Yeah.
Aaron Abbott (Google LLC) 00:52:03 Yeah, like that… we're talking about, like, the top-level entry point into the agent, and that seems like the best candidate for Invoke Agent.
Server. Service pin.
Liudmila Molkova 00:52:16 Whatever that span we end up with could have a server flavor.
Don Branson (International Business Machines Corporation) 00:52:22 So is this, like, a gateway where you might do cost control and things like load shedding for low priority items?
Just wondering about the use cases. Something I've looked at lately.
Liudmila Molkova 00:52:39 Understanding that the use case is You are hosting agents.
And you want to tell… like, you want to collect information about them yourself, Or… You manage them for somebody else, and you want to give them the telemetry about their Legends your host for them.
Don Branson (International Business Machines Corporation) 00:53:00 Okay, so it's like you've got a certain amount of metadata, you don't want too much internal details, but you want to be able to Yeah, collect appropriate metrics and kind of have a data warehouse that's provided as specific Groups, individuals.
Neil Yashinsky 00:53:19 I feel like this should be informed by, like, how… the SaaS model works, because I feel like there's two equally valid views of this. You know, there's the, if you will, the agent's perspective, or the server's perspective, and the agent's perspective. And so, in… Nikhil, correct me if I'm wrong, but in your instance, like.
The agent is… Oh, maybe I should ask. Is there a one-to-one relationship between service and agent, or does one service spawn multiple agents?
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:53:58 Yeah, so we have many instances in Microsoft where… Can you hear me?
Neil Yashinsky 00:54:03 Yeah, yeah, sorry.
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:54:04 Yeah, so we have many… Applications in Microsoft, where… so… one example is, like, Copilot Studio, where we have… there's a central service, for which, you know, which receives all the requests, right? And that, is tenant, it's… it's multi-tenanted, so they will… so… and… So they receive all the requests, and then there is n number of agents that they… that it services.
So, we run into that situation where, yes, so at that point, it is a hosted Agent, and then… we need, or… it… So the execution of it is technically not… invoke agent internal at the point, from how I'm seeing it.
Neil Yashinsky 00:54:58 Yeah.
Because I feel like that's… it's a… it's almost like a matter of perspective, in that, like, if you have… you know, the agent that was spa… Or I guess I should say the… Multi-tenant master service that is, spotting agents.
is essentially a quasi-parent-child relationship, as I understand it, and they'll have their own views, so the child doesn't know about the parent, per se, knows it was called by them, but the parent obviously knows about the child, and so… The parent will… you know, you'll rely on the parent to provide full transparency to the turns, the handoffs, all that good stuff, and the child will have the… consumer's view, I guess, of that. And I don't know if that answers your question, or if that… but that's how I was thinking about this across, like, how we… how to… how to model both, sometimes, validly, because they require, I guess, like, a perspective.
On if you are the agent that got a handoff.
Or if you are the agent that's, like, the result of the handoff, you know, which side, I guess, of the handoff, you know, the… Originator, or the… what's the opposite of virginator? Someone help me out, bail me out. The recipient, I guess? Does that make sense? Anybody lining up what I'm trying to articulate about how this relates back to… The workflow and the churns and all that good stuff.
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:56:33 So… It's also that, like, the agent service, as you said, knows about all the agents that that is tied to it, essentially. So, it can also be its own process, right? So, you get a request, it's a multi-tenant, so the server figure out, okay.
Spawns a process to, execute that.
Request for a specific agent.
Aaron Abbott (Google LLC) 00:57:04 I…
Neil Yashinsky 00:57:05 So it's its own pair? Oh, sorry, go ahead, Aaron.
Aaron Abbott (Google LLC) 00:57:08 No, I was just gonna say, like, can we kind of just work with the hotel model and ignore the tenancy? Like, I know we were talking last week about how to do this, and we do have this, like, multiple resource in an SDK proposal, which I think is even implemented in Java now. Like, if we… if we assume that we can use the entity.
For, like, a multi-tenant, single process.
Is there, like, still a sticking point with just, the kind of straw man that Liudmila mentioned about having Allow… allow server type for one of those bands, for the topmost one.
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:57:48 So it's a proposal that I'm saying?
We will figure out what is the topmost span, and then we can mark that as a… have a server version of that span.
Aaron Abbott (Google LLC) 00:58:04 What, I mean…
Liudmila Molkova 00:58:07 We need to figure out… like, how we would define the server span, the key part should be that it should be the local route. It cannot… we cannot have multiple nested server spans.
And the definition of the service band would be that you report it if you do not report Protocol level spends.
Which kind of makes sense, because as the service, you decide if you want to emit.
Top-level, let's say, protocol spends.
Trask Stalnaker (Microsoft Corporation) 00:58:38 Even then, I feel like we could… you could choose to emit both. Like, we have ACTP server span and RPC server span.
Which… can be… nested.
Why… why not?
HTTP span and GenAI Invoke Agent Server Span.
Nested under that.
Liudmila Molkova 00:59:05 And… the… you can decide to suppress, and then you lose all the Agent stuff. You would only keep HTTP.
So maybe the A2APR195, it's pretty close, where actually it has all the approvals.
It suggests a different thing, how to it has a refinement of A2E HTTP. It's an HTTP span with extra A2E attributes.
We can entertain this idea, so that if you suppress instead of suppression, you can enrich. I feel like for the hosted agent providers, it's not helpful, like, they wouldn't suppress. They would choose one or another.
Trask Stalnaker (Microsoft Corporation) 00:59:55 And probably choose the invoke agent server span.
Liudmila Molkova 00:59:59 Yeah, otherwise they wouldn't be here.
Trask Stalnaker (Microsoft Corporation) 01:00:02 Yeah.
Cool, we hit time, but, Nikhil, it sounds like there's… I mean, there's… growing… an acceptance or understanding of the server invoke agent server span. Maybe fleshing out, like, what… what it would look like, maybe a more… a concrete proposal that we could look at next.
Nikhil Chitlur Navakiran (Microsoft Corporation) 01:00:27 Sounds good, yeah.
Thanks, folks.
Liudmila Molkova 01:00:32 Thank you.
Aaron Abbott (Google LLC) 01:00:33 Y'all later.
Trask Stalnaker (Microsoft Corporation) 01:00:34 I…
Neil Yashinsky 01:00:35 Thanks, Dr. Fearless Leaders.
