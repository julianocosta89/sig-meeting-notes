SIG: GenAI SIG
Date: 2026-08-25
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

AWAB Melayem 00:00:20 No faults.
Siri Varma Vegiraju 00:01:13 This is Siri.
I'm not able to hear you. I think you're on mute.
Nope, not able to hear you.
So she chose mute.
Nope, not able to hear you.
Liudmila Molkova 00:07:50 Hello, hi everybody.
Siri Varma Vegiraju 00:07:55 Hello.
Alexander Akhmetov (Grafana Labs) 00:07:58 Inc.
Iwa Wong 00:07:59 Hello.
Surya Teja 00:08:01 Hey, good morning, folks.
Trask Stalnaker (Microsoft Corporation) 00:08:03 Hey, y'all.
Liudmila Molkova 00:08:09 Okay, so… let's get… Dark it?
Please add your name to the agenda, please add your topics if you have any.
We had some discussions… And, Morning… early morning call for… for… for me.
Hopefully it's not that early for you.
One thing to review from it, there is a blog post from Hushing around the conformance repo. If you're interested in how conformance Repo works, and what you can get from it, this is a good source of information, and also if you, you can Maybe find some issues, and it would be also useful. If you take a look… Moving on to the topics for this week. Do we have Victor or Arthur?
It seems not yet, so let's… Put it… Let's see if it comes up later… And… Yan, do you want to talk about the LMD?
Yuan Gao 00:09:41 Yeah, sure. So, yeah, this is just to initialize a proposal.
To drive the… standard, influence telemetry. I'm Yuan from Google Kubernetes, and I'm working on RMD open source community as well. So, the feature gap here is that Currently, we have very limited coverage of influence, telemetry, mainly, traits and metrics.
So, and, RMD is, like, influence engine orchestration layer, and what AMD does is to extract the different signals metrics from different heterogeneous RM backend engine, like VRM and SGLAM.
to, like, unify the different metrics or traces from different, RM engines, and expose them to the, to the customer.
So… What we plan to do is to propose a bunch of new GenAI thematic, GenAI thematic conventions for inference to standardize, standardize these, these telemetries.
So, I start, SIG, and I want to bring this up here to see if there's anyone else, is interested in this, or would… Like, to support this proposal.
Liudmila Molkova 00:11:17 Yeah, welcome in. Do you have any links to share? Is there anything public?
Yuan Gao 00:11:22 Not really. I have a draft proposal. The audience are mainly for MD, but I think it might be helpful to share here as well. Give me one second.
Sorry, I'll do it later, because there are some permission issues.
I'll create a public doc, and Linked here in the, in the, in the meeting notes.
So, I… Wonder if SIG… I barely remember, like, someone from other groups also interested in the, influenced elementary.
Liudmila Molkova 00:12:04 Yeah, we had Steve in the earlier call.
Yuan Gao 00:12:08 Okay…
Liudmila Molkova 00:12:09 not… not… I don't think he's here. Now, it… There is some existing discussions in the semantic conventions GenAI repo on this.
And maybe a good idea would be to comment there, and I think maybe Steve or somebody from Alibaba created, Let's see… Okay, maybe, I'll find it later, or I'll send you links later, but, there… there were proposals from Alibaba, and, it may be easier for people to find if you either comment or post a new issue. Oh, here we go.
Okay, I'll, I'll… Add them to the waist.
Yuan Gao 00:13:11 Great. Yeah, so… yeah, I can follow up with them offline, and we can see if we… if once we have some, supporters, I can drive the SIG.
Liudmila Molkova 00:13:26 Wonderful. I'm curious… well, we talked about it in person, but I'm curious, what would be the reasons to have the OpenTelemetry as authority, rather than having LLMD be its own authority to define semantic conventions for LLMD?
Yuan Gao 00:13:47 I think it's more like, RMD is the oxygen layer. It extracts signals from heterogeneous background systems via M, SGLAM. So, we could, and we are currently working on doing this in RMD. Like, we can define, like.
Let's say, okay, cash hit rate.
And this, this is, unified signals from different backend engines. It might call, like, K slash K… K-value caching VRM, it might call, KV cache in media. So.
What we cannot do is that we cannot maintain the standard of PRP seminar convention in all the, I would say, upstream engines.
So, that would be very hard for us to maintain this standard. Instead, I would like to… proposed the standard GenAI semantic connection here in OTRP, so that might be helpful for our upstream engines to adopt the standard… to adopt the standards if they would like.
And also, I would say, these, inference time entries are… are supposed to be commonly used. They should not be, like, AMD-specific signals. It should be common enough for most of inference engines or inference obstetrators to adopt and to use.
Liudmila Molkova 00:15:21 Thank you.
Okay, anyone wants to chime in on this?
Okay, then. Thank you, Yan.
Yuan Gao 00:15:45 Thank you.
Liudmila Molkova 00:15:46 Looking forward to the comments on the issues, or new issue.
Cool, do we… have Victor order?
Iwa Wong 00:15:59 No, I think, Victor asked me to be here, to… probably, Yuan and Victor, an author, probably should, partner, on this, I think it's another proposal where they're trying to figure out, whether there is a standard upstream, for motel, as well, on, GenAI-related.
things, and, right now, what is the semantics around it? How do we, understand, not just from, closed source model, let's say, for example, and Tropic OpenAI, but also, or Meta.
But also, like, open source models. I think there needs to be a standard, and I agree with the team here. There needs to be a standard, on… How to observe, the agent's intent, the exact two calls that is resulting from this, whether there is, approval, policies, where those approval policies reject or accept, And resulting in a tool call. All those need a standard way.
An industry-centered way of, like, observing, what is going on.
So I think those two… proposal, so from Yuan and Victor probably needs to… Needs to sync.
Liudmila Molkova 00:17:34 Okay.
Trask Stalnaker (Microsoft Corporation) 00:17:34 Yeah, I think that we could, it would be great if they can join next week, it's fine to, push that discussion. I do think it's a good discussion and would be great to have, them. I assume, we know Victor… I assume Arthur's from the COSI, group?
It would be great to kind of get an overview of what they're doing and how they see that, you know, we can work together.
Iwa Wong 00:18:06 Yeah, sounds good, and thank you for, Let me talk as well, like, I… I have previously, contributed to the Codex repository as well, I have understood enough, about how the agent looped on the codec side works as well, and, like, understood, some of the… challenges of observing what is really going on. The… the chain of thoughts is all encrypted, and there isn't really a good way to, visit… I mean, check, whether the auto-real site, actually resulted in escalation onto.
The sandboxing style of things as well, and, like, how do we even correlate like, say, for example, if you put an agent, like, for example, Codex Cloud, or any, agents, onto the cloud, how do you even, correlate between the infrastructure And identify there is an agent, there, Like, all that correlation needs to be standardized, just so that we can actually have visibility onto what's going on. So, looking forward to…
Liudmila Molkova 00:19:22 I think there is a lot of things in OpenTelemetry that provide the correlation. I would encourage you to maybe try it out and see what you can get, and then come back with some gaps. And there are a lot of issues in the repo that talks about security, sandboxing.
different aspects of it.
it's a little bit too AI-generated in the repo, so it might be hard to understand what these issues are about, so if you would like to, like, maybe do a revision on what we have in the repo, and what there is in existing semantic conventions, and what's missing, that would be wonderful.
Iwa Wong 00:20:04 Yeah, sounds good.
Liudmila Molkova 00:20:09 Awesome. Thanks. So then, looking forward to Victor or somebody from COSI coming and presenting, more on this, and… Moving on to the next topic, the… Opentelemetry JavaScript.
Pranav.
Do you want to talk about this?
Pranav Sharma (Google LLC) 00:20:31 Yeah, like, in the last meeting, like, we discussed about this utils package, so just wanted to, like, bring this to the attention of the sick people that, like, I have a PR ready, and I also, just as a experiment, like, tried to, like, add a refactor to the, one of the instrumentations, to use this GenAI util library, and I'm just basically looking for feedback or any concerns that folks might have about this.
So… Yeah.
The PR has gotten quite big, so if folks want me to split it up, I'd be… Happy to do that, but, yeah. I mostly modeled this after the GenAIutil Python.
And which is why it got so big, because I just added all of the features at once.
So…
Liudmila Molkova 00:21:24 Yeah, I'm… I think we don't have anybody from JavaScript SIG here, or somebody who contributed… Do we know who contributed the link chain instrumentation to JavaScript?
Ridhima, was it.
Ridhima Satam 00:21:42 No, no, that's just the Python one I did.
Liudmila Molkova 00:21:47 Okay.
So, probably need attention from some of the JavaScript people, and I think Jamie and Volvgang were, too, who… We're proposing some of the features like this.
Maybe this issue.
Probably can't ping them on Slack.
So, Pranav, if you… if you want, you can ping them, or if you want to just post in the hotels GenAI, I'm happy to ping them and ask for reviews.
Surya Teja 00:22:19 Okay.
Jack from Microsoft can be helpful on this one, because he has… he's a SIG guy for JavaScript, and he contributed to our… to our Python-pack instrumentation.
Pranav Sharma (Google LLC) 00:22:35 Jackson Weber?
Surya Teja 00:22:36 Yeah, Jacksonville, yeah.
Pranav Sharma (Google LLC) 00:22:37 Yeah, I'll reach out to him, yeah.
Surya Teja 00:22:39 Yeah.
Liudmila Molkova 00:22:40 already here.
Pranav Sharma (Google LLC) 00:22:43 Yeah, I think he did leave a couple of comments. I'm anyways going to present this tomorrow in the JS SIG as well. Just wanted to see if anybody here would like to take a look.
Liudmila Molkova 00:22:56 I have… I have a question… oh, sorry, Arianne, go ahead.
Aaron Abbott (Google LLC) 00:23:02 I was gonna ask… excuse me, if you go back to the conversation, there was, like, a follow-up PR that shows how it's used. I was just gonna ask, Pranav if you… Like, does this PR, the follow-up draft one, is it making Langchain use this, or, like, do we have any good way to test that this API works?
Pranav Sharma (Google LLC) 00:23:21 This was, mostly about, I think, the anthropic instrumentation, But we don't have the conformance tests yet in the JS, so yeah, you're right, we don't know, if… We don't know if that, if the resulting instrumentation is, SEMCON compliant.
Yeah, I was just thinking how, like, should we add conformance first, before merging everything, or can we do it, like, in stages? Like, we merge this.
then we add instrumentation, we add conformance, and then retroactively fix it. Everything in this PR is right now marked as experimental, and none of the API is being exposed publicly. None of the functions are being exported publicly.
As of right now.
In the index.ts, yeah.
Aaron Abbott (Google LLC) 00:24:15 Cool, yeah, the anthropic thing sounds interesting, and I think… it's… I guess it's a question for JS maintainers, but I hope we can just go with, kind of piecemeal approach and start with something like this. Surya, go ahead.
Surya Teja 00:24:28 Yeah, I wrote the JavaScript instrumentation. The intention of that is to start small and then add confirmants and everything once everything is in place. I had a brief discussion with JavaScript folks and explained to them that this is the first bit of, what we are… what is going to come for Anthropic, and then next few more things are going to follow. So, conformance will be added in subsequent years, once the Pr that is open is merged.
Adam.
Pranav Sharma (Google LLC) 00:25:01 Right.
Liudmila Molkova 00:25:03 I think for the first time when conformance tests are added, it makes sense to do this later.
But as a follow-up, but for… After the conformance patterns are established in the repo.
It is in Python a requirement to the confirmance test.
So that it's the only reasonable way to test that instrumentation actually is producing compliance and conf.
Pranav Sharma (Google LLC) 00:25:31 So, just to be clear, Ludmila, you're suggesting that we should hold off on merging these PRs and the instrumentation PRs until conformance is done?
Liudmila Molkova 00:25:42 Oh, no, no, I'm saying that when we're establishing the pattern of doing conformance tests, it's… I think it's fine to follow up, but moving on, this is the gate for the reviewers, and I think it should come Along with the first instrumentation. It's essentially part of the testing.
Pranav Sharma (Google LLC) 00:26:05 I think we can take Surya's anthropic instrumentation as, like, a test, and we can make sure that the conformance works on that instrumentation before adding further instrumentations.
Liudmila Molkova 00:26:21 Yeah, and it should be trivial, like, you can now use the common runner. Within Python, we still use the Python-specific runner, and we can actually get rid of it, but it should be possible to just use the common runner from conformance repo.
And, and, like, we'll… well, we'll talk about this. It's not an immediate need. Let's get the OTOs and Anthropic figured out first.
Pranav Sharma (Google LLC) 00:26:49 Okay, thank you.
Liudmila Molkova 00:26:53 Thank you!
Okay, anything else before we move on to the token usage?
Okay, so then moving on. I'm trying to eat the talking usage elephant piece by piece.
And this is the… another small piece, that… We can do… so, we have the problem of… Having agents, span Having usage attributes on agent spans, and also on the inference pants.
And, well, I believe there is some, there are some discussions about the input and output tokens.
On the Agent Span, We somehow added this to friends.
on… Them two?
And I like to remove them, because, like, cash is… inference… Feature, not an agent feature, and it doesn't make much sense to drill down into Cash metrics at the agent level.
Until at least we figure out some better way to do this, which could be that we just stamp Agent Name on the inference metrics.
So this is a small PR that, removes this to… Friends from Engine Spence.
Just looking for the reviews, And the other one is more complicated.
This is the… The elephant itself?
And I removed some of the pieces of elephant. For example, there used to be total tokens as a sum. We can add it later.
Just to, keep the amount of changes sane.
As we've talked about this in the past, and the problem we have today was our usage metrics.
this friend.
is that… It has input and output as two different dimensions.
And when people write a typical query.
They might think that they have a total tokens, but what they have is… It's a meaningless number.
And in order to solve it, we kinda have to define Usage metrics, differently.
So I still don't love the naming, and we probably will backpike shed on this, but… there are… Currently, in this proposal, two groups of usage metrics. The first one is This French?
They are counters.
And we'll talk about why in a second, but they are broken down by bundality.
So you can filter by only text, or only image, and you can sum them up, and those things will work.
The… in theory, we could have… Like, caching and reasoning as a sub.
Dimensions too, but it comes with its own set of problems, and it becomes harder to use, so the strands are separate.
If we had tool usage, it would probably be yet another metric, because it needs to be broken down by modality, potentially. But, the two usages.
supported by one provider, and we probably can postpone, adding this. But anyway, so these friends are counters, you can sum them up, you can calculate rate, you can calculate the ratio between, like, an average between different modalities.
These friends are… the histograms, and they are just for input tokens and output tokens. There is no dimension that talks about modality, cache, or anything like this.
And the motivation for this, I've tried to describe in the design, a small design dog here.
It's the, essentially, FAQ Trask from your PR.
Slightly adapt… adjusted. But this is the… the demonstration of the problem.
So if we… and histograms.
With modality in them.
what… They would mean, like, what this query would return.
it's something… irrelevant. It's not the input tokens, it's not the percentile from per modality, it's just some random number that has nothing to do with anything. And this metric would measure the tokens in the parts, like image part, or Audio part, rather than the… Input tokens or anything.
We could introduce Histograms per modality?
And there is, like, more… Consideration samples, they would look like this.
And this would be… That would provide the distribution.
And the point I'm making here is that the advanced case, and it's costly, so if you want to introduce them, they would probably be opt-in.
And we can do this later.
It's kind of hard to digest this within the meeting.
And it's some burning need that we have in the GenAI SIG, because we don't have proper usage metrics.
I would like to maybe… for people to spend some time reviewing it, and I'm pretty sure the explanation here is not sufficient, and there could be a better example, so if you share with me your confusion around this, I would really appreciate it, and I will try to address it.
Yeah, Ankit?
Ankit Singhal 00:33:41 One quick question, a little orthogonal to this, so… I know, like, one other thing that I've seen come a lot is, can I have token counts, and then probably, and then cost for an agent, right? Is that something that's possible with this refactoring?
Vega.
Making these metrics more, like, modality-driven right now, so that we can kind of count them separately, as you mentioned.
Accurately.
Liudmila Molkova 00:34:08 Yeah, we can use these metrics to estimate costs.
I've tried to write queries, parameters, PromQL queries, to estimate cost based on these metrics. They become very complicated very soon. I can add them if you think it would be useful, but it's a lot of PromQL.
to read.
Ankit Singhal 00:34:30 I see. And, would that require, like, adding new dimensions, or is there a difference? Because I know, like.
Yeah, like, for example, like, agent ID or something, kind of… Tell them, okay, this is… or, like, be able to filter them by.
Certain agent.
Liudmila Molkova 00:34:49 So my current goal… oh, you're asking the costs per… per agent, grouped by agent.
Ankit Singhal 00:34:55 Yeah, yeah.
Liudmila Molkova 00:34:57 So, not yet. I think my first goal is to, like, figure it out for inference.
And as the next steps, I'm thinking we should Figure out how to stamp Agent Name on the nested spans and metrics.
through context scoped attributes or something like this, and then we will figure out how to do this for agents, but before we get there, I think we need to figure out the inference alone.
Ankit Singhal 00:35:25 Got it, got it. Yeah, no, definitely. Like, I think because I just want to make sure, like, we keep that in mind as well when we are designing this, so that it's, it will be… Hoping, like, just an additional delta for Agent.
Trask Stalnaker (Microsoft Corporation) 00:35:40 And that's addressing… that's, like, calculating cost on the back end from this data, but there's also been discussions and proposals here about calculating cost, In the instrumentation, or applying stuff there, and having… Actual cost metrics emitted.
Ankit Singhal 00:36:03 Oh, yeah, yeah. Actually, I was referring to more about, like, if you can know the tokens or, like, inference which are caused by a certain agent, right? Which can attribute… can be attributed to a certain agent, then I think, yeah, cost calculation, whether we do it behind the scenes versus instrumentation, I think that can still be probably, I guess, a separate thing to solve.
But at the same time, like, how do I add the dimensions of, okay, agent in here is something that was… Looking to shine to it.
Liudmila Molkova 00:36:30 Oh, I… I see. Yeah, so for this metrics, we sh… it should be, at my level, current level of understanding, and histograms turns out to be very complicated. We should be able to add agent as a dimension here, because one inference call contrib… like, it's one measurement per… Agent. We are not breaking down a single measurement by… Multiple agents, and this was the problem with the input-output tokens, or with modality, that we would report multiple measurements for one operation.
Oh, I see. Oh, so right.
Ankit Singhal 00:37:10 And then you have to have something to break it down. Okay, so here it should be possible just to add another dimension. Like, but I know there should not be a dimension Okay.
Sounds good.
Liudmila Molkova 00:37:29 Okay, so then I'll… I'll give you some time to digest, but I would really appreciate the reviews. It's been a long, lingering issue in some content, like, there is no solution today. Let's… let's try to figure it out.
Yeah, Erin?
Aaron Abbott (Google LLC) 00:37:46 Yeah, so I… we talked a lot about cost last week, in terms of, like, you know, stamping a monetary value in the instrumentation or in the telemetry.
I just wonder if you could talk a little bit about the intersection of this with the cost calculations, or what our plan is, or if we have a plan for SEMCOMF.
Liudmila Molkova 00:38:10 Yeah, I… Well… two things. The first one is, The calculation of the cost from usage probably is not the instrumentation concern in its own, because instrumentation doesn't know anything about costs. Well, unless it does, unless somebody reports costs.
But it can't totally be done in, let's say, some processing layer, where you have… the information about costs. So, I think there are two ways to approach the cost. The first is estimate based on the public prices, and the second one is Nobody actually… well, maybe somebody gets actual pricing, but the public won't, but it's negotiable, and every customer has their own rates.
And only them can provide this information.
So, I would imagine some processor collect… sorry, collector-processor that would augment these metrics, or transform this metrics and create new metrics using the customer-specific information.
Along with… this data.
would… be viable. More viable than every instrumentation getting it. Or some form of a plugin with config that we can… that customers can plug into their SDKs.
Aaron Abbott (Google LLC) 00:39:48 Yeah, I think we kind of arrived at a similar thing yesterday, or at least doing it asynchronously.
But we were also talking mostly in the context of spins, I think, so… Or spend attributes, I should say, so… Yeah, I guess we should just take it into consideration when thinking about this, making sure that the… The cost requirements are… derivable, I guess, from these metrics.
Liudmila Molkova 00:40:16 Yeah.
Okay.
So, done.
Let's move on… To… the next topic?
Surya?
Can you…
Surya Teja 00:40:48 Yeah.
Liudmila Molkova 00:40:49 this, can you elaborate?
Surya Teja 00:40:50 Yeah, sure, someone from… someone mentioned that, Anthropic was trying to add, GenAI instrumentation to both Cloud Agent SDK and Python and TypeScript, so I don't remember the name of the person, but I just wanted to see if they're in the call, and if they know something about this, because they mentioned that it's going to come in August.
And I was waiting to see if… It's already in progress or something.
Chris, Chris, yeah. The name of the person is Chris, yeah.
Liudmila Molkova 00:41:27 I don't think Chris is here.
I had a vague memory of September.
Surya Teja 00:41:37 Okay.
Yeah, if that is the case, fine then. But if we know some date or anything, we can close the issue on that one, saying that it's going to be native instrumented.
Liudmila Molkova 00:41:53 Yeah.
Okay, does anybody know anything?
Trask Stalnaker (Microsoft Corporation) 00:42:01 Felix, do you know anything?
Or, can you share anything?
Felix Becker 00:42:08 Sorry, can you restate the question?
Surya Teja 00:42:12 Yeah, so Claude, the question is, Claude, Agent SDK, both in TypeScript and Python. They… we were told that we are going to get GenAI instrumentation, for those, packages in August.
or September, I might not be sure about that.
They already have native instrumentation, there is, an ability to hook OpenTelemetry exporters at Export Telemetry, so the question is, any idea on when we are going to get GenAI spans and anything in cloud SDK instrumentation.
Felix Becker 00:42:53 I didn't know, but I can follow up with the team that owns the SEK. Do you have a name who told you the August-September timeline?
Surya Teja 00:43:02 Yeah, sure, I can, I can post the GitHub issue in the… in this chat, or either I can ping you directly on the CNC of Slack.
Goodness.
Liudmila Molkova 00:43:17 Can you post the issue in the chat, and I'll just put it here, so it's somewhere? Yeah.
Surya Teja 00:43:21 Yeah, sure.
Liudmila Molkova 00:43:23 Thank you.
And I think what we heard is a rumor from somebody from Netflix that Anthropic is considering Following semantic conventions, and we don't know… Where this information is coming from inside Anthropic.
Felix Becker 00:43:46 I can follow up with the, like, Claude H and SCK team of… Yeah, it would be helpful who you were talking to.
I'm not on the team that owns the Cloud Agent SDK, so… I don't know, up there.
Liudmila Molkova 00:44:07 Cool, thank you. Then let's follow up on this.
Moving on to the next topic, the real-time Ankit.
Ankit Singhal 00:44:17 Yeah, I think it's a PR that we discussed. I've updated the PR as per the discussion and some of the decisions that we made.
So, I think there were a lot of conflicts, so I'm still working on resolving them, all of them. I saw that, like, some of the mocks were moved to a different report, so, kind of, it's taking a little bit more time than I anticipated. Yeah, please do review and give your feedback. I'd like to… Get this moving along.
And hopefully get this much soon.
Liudmila Molkova 00:44:50 Awesome, yeah, sorry about, disrupting the… this was the new.
Ankit Singhal 00:44:55 Fair enough, that's it.
Yeah, that's like, I'm still working on it. All of them are not done, so once I have them, probably in another couple of hours, so… Get this sorted out. The conflicts.
Liudmila Molkova 00:45:06 Cool, and, like, it's… it's now in the confirmments repo, feel free to send a PR there, I would be happy to approve, it should be trivial.
Ankit Singhal 00:45:14 Okay, yeah, definitely, yeah, working on that.
Liudmila Molkova 00:45:16 Yeah.
Ankit Singhal 00:45:18 And then, I think I did see some feedback from Dylan, so that's good. And some of the attributes that we're adding for the tokens are already covered in one of your PRs, Liu, so I think that'll reduce the surface area to some extent.
Liudmila Molkova 00:45:33 Awesome, thanks. Anything we need to discuss, or all… all good?
Ankit Singhal 00:45:38 Yeah, I think, in the… in this PR, I'm not going… I've not added the turn detection part, right? So for that, I'm gonna probably have another PR where I can have, like, provide a specific information on.
What's the best way to predict, and then we can discuss more on that part.
So, I'm just going with the users, And then the Generate Live Content. Yeah, and the naming, I'm not so great at naming things, so, open to suggestions on what the name of the span should be.
Liudmila Molkova 00:46:12 Yeah, I added this because it mentioned because the Gemini uses Generate Content, and this was live, so I called it Generate Live Content. We probably should be, I don't know. More… like, I think that the spend type should be not tied to a specific provider. The operation name could be, but spend type should be more general, like we have for inference or embeddings.
So this one… Yeah, I don't have immediate suggestions, but maybe.
I'll have some.
Ankit Singhal 00:46:53 Yeah. Sounds good.
Cool. Thank you so much here, I think, majorly, that's from my side.
Liudmila Molkova 00:47:04 Thank you.
Oh, okay, so, so you, you linked this, this one.
Oh, this is the person from Netflix, right, who told us this.
Surya Teja 00:47:32 Yeah, yeah, I linked out the comment.
Liudmila Molkova 00:47:36 Okay, August.
Surya Teja 00:47:38 Yeah.
Liudmila Molkova 00:47:42 So, Felix, it doesn't seem like there's any pointers.
Felix Becker 00:47:45 Who is the source here from inside Anthropic?
Liudmila Molkova 00:47:49 No, he's from Netflix.
Felix Becker 00:47:52 Oh, okay.
Liudmila Molkova 00:47:54 It's remarkable.
Trask Stalnaker (Microsoft Corporation) 00:47:54 Rumors only, rumors only.
Felix Becker 00:47:56 Just check in with the client agency. Sorry, I don't have anything to share right now.
Liudmila Molkova 00:48:01 No worries. Thank you.
Okay, So then, the final topic on the agenda is inference bands, the duplication. Dylan, do you want to guide us?
Dylan Russell 00:48:18 Sure.
Yeah, so we had this problem where… Multiple libraries.
Along the call stack. Might be instrumented to write these, like, inference bands.
And so, to solve that problem, I'm proposing we put the span onto the context.
And if you're a library and you're not sure If you're… Like, at the top of the call stack.
Check the context to see if… The span is on it.
And if it is, Then you can either, like, suppress your instrumentation, or… Get the span and, like, make modifications to it.
But yeah, that's pretty much the idea.
Trask Stalnaker (Microsoft Corporation) 00:49:12 In Python, are you able to tell… are you able to read anything about the span that's on the context, like checking the type to know that it's an inference span?
Dylan Russell 00:49:25 Yes, you can… you can, like, take the span off and, like, modify it, and… I'm only proposing we do this for inference spans, at least for now.
Trask Stalnaker (Microsoft Corporation) 00:49:37 Sorry, the reason I ask is, at least according to the spec, you can update the spans, but you can't actually read any data without casting… without going through the SDK.
But Python may be different, for language-specific reasons.
So, like, in… in Java, the way we have to solve this, we can't look at the span and decide, so we have to put some… another marker in the context that we can read.
To know if it's nested.
Dylan Russell 00:50:17 I see, I think.
this… At least here, the context, like, a dictionary, and there's, like, a key you can… It's like a special key you can look at. It's just like a key-value pair, and you can say, like, the key will be, like, inference span… And so you can use.
Trask Stalnaker (Microsoft Corporation) 00:50:40 Oh, so not… oh, so not putting it in the context as the current span, but putting it under your own key.
Dylan Russell 00:50:47 Exactly.
Trask Stalnaker (Microsoft Corporation) 00:50:48 Okay, I gotcha.
Liudmila Molkova 00:50:53 Yeah, I think that that interesting part here, and maybe that's relevant, so… I think in Java, the suppression Just backs off, right?
It does not create a new span.
But here… I think what Dylan is proposing is more interesting, that we actually enrich the outer span with the new information we have.
there is a… like, we can enrich, the problem is that we… on the spec level, we don't… we cannot read from the span, we… we cannot get attributes from the span. It's possible in Python, not possible in many other languages.
But… I think we need to… we had this problem in MCP, and we kind of decided to enrich.
And we never put any code behind it.
We never put the proper guidance. For example.
Do both layers report metrics? No, just one layer reports metrics.
And then the… Can we enrich metrics? No, we cannot enrich metrics.
We can only enrich spans, not even events.
Are we happy with this?
Probably it's better than… Not enriching anything.
Trask Stalnaker (Microsoft Corporation) 00:52:27 What kind of… what kind of information would you enrich that you only have access to in the lower level?
Liudmila Molkova 00:52:37 That's the tricky part. The first one is… The immediate thing that we usually never populate an outer layer is the server address, server port, because something like Langchain doesn't know.
But there is more. So, the… thing I'm mostly worried about with this is… Let's take OpenAI. There will be OpenAI instrumentation in OpenAI.
BankChain, Agno, and 5 other libraries. They would quickly become they would drift from each other. Drift is a AI word. Anyway, so they would drift from each other, we will have multiple implementations. Could we maybe say that the outer layers Don't populate everything, but then inner layers provide some optional tiny, gritty details, I don't know.
But the server address, server port is the first thing that comes to mind right now.
Aaron Abbott (Google LLC) 00:53:54 Yeah, plus one on those, and I think plus one to the general idea, it seems super useful.
One thing I wanted to call out was, like, we're… in GenAI Utils, we have these kind of wrapper classes around the span, which I think we're already using to read data out of them to get around the thing that Trask mentioned, where You can't… Look at what's already being set.
And the thing that we store in context can be one of those objects, too. It doesn't have to be a spin, necessarily, it's just another idea.
But yeah, I kind of like the general approach of having… I'd love to hear more about what Java does, because I think there's a somewhat general solution.
But, like, having something general, like, for every spin type defined in SEMconf, we have a well-known context key that, instrumentations can access.
Seems… seems kind of interesting, because this applies to… I think we've seen this in URL… URLib3, which is used under the hood in requests. We've seen it for some ORM instrumentations.
Yeah, and one… one other thought, just looking at the the SEMCOM PR a little closer. The keys are kind of specified as strings, but I think… I think this is in the OTEL spec, but we also implement it… implement it in Python, where We create, like, an opaque identifier for context keys.
And you have to use the opaque identifier, and you can't just use the string. So I think it kind of implies that we have to expose some kind of API for the context keys, besides just the string names, which are defined in semconf.
Trask Stalnaker (Microsoft Corporation) 00:55:32 Yeah, so what we do in Java is we have a, A key that is essentially the span type.
that new proposal, which, yeah, generally we, and we provide two options in Java, or I guess three options. One is never suppress One is suppress at The client span level and the server span level, so meaning clients never nest and servers never nest.
Those are the kind of outliers, and the one in the middle, which is the default, is just that the, spans of the same type never, nest.
And yeah, we do have to… we do have an API, we have to expose the API for that, since, you can't just use the strings, so the context keys are opaque.
Did you have another question about…
Aaron Abbott (Google LLC) 00:56:40 No, no, no.
I think… I think that makes sense,
Trask Stalnaker (Microsoft Corporation) 00:56:45 Oh, yeah, we don't… as Liudmila, alluded to earlier, we don't do any, enhancing of the parent span at this point, but, that was, like, an early Thought that that would be cool, we just never did it.
Aaron Abbott (Google LLC) 00:57:07 Yeah.
Trask Stalnaker (Microsoft Corporation) 00:57:08 For… specifically in our case, we were thinking for, like, some protocol layer Details.
That, yeah, you may not have access to. I think this case is a great example of the server address.
Aaron Abbott (Google LLC) 00:57:27 Yep.
Yeah, I think… I'm a little… the enriching thing seems really cool, but I think, Ludmila, you called out the MCP example, where it would enrich the tool, execute tool spend.
it feels like we would have to… because the MCP Python SDK is where the instrumentation lives right now, like, it's natively instrumented.
then we'd have to, you know, ideally expose some kind of stable API if we wanted the enrichment to work across native instrumentations, and I don't know if we're ready for that yet.
Liudmila Molkova 00:58:03 I mean… It's… it's doable, especially in Python, where you can Easily check if there is a, you don't need to take a hard dependency, but if you check that try importing the GenAIOTL.
and, check if the… get the context key through, like, the… the Python, whatever.
It's kind of easy to add this layer to native instrumentation. It's a little bit unstable, and… It would be the story with any native instrumentation that they would need to adapt for our changes, because we are still actively changing things. We've done the suppression in Java in native instrumentations in Azure, and it's been much more complicated because of reflection, but it's still doable. Like, you don't need to take a direct dependency to, like, use the context keys, it's just difficult.
Aaron Abbott (Google LLC) 00:59:11 Yeah, I think you can technically just use strings in Python also, because we added the opaque key thing afterward, so… probably a couple options, but… sorry. I think exposing just the context key seems pretty manageable. It's like, you know, single constant defined somewhere in semconv, and Everything is completely decoupled.
Liudmila Molkova 00:59:35 I feel we need to do the language agnostic way here. Well, we can… actually, wait, wait, we… We can start with the Python implementation, and we can put things in semantic conventions after. The one thing I think we should put is this enrichment, that this is a legal option.
And maybe outline Some rules around that.
No metrics, no events, just spans, and you don't try to read the span.
Yuan Liu?
Add things, and they might overwrite existing attributes, but… shall be eat.
and… the context keys, maybe… I don't know, do we need to put them in the semantic conventions? It seems something language-specific, no?
So I'd rather have a pack once.
Dylan Russell 01:00:35 Rather have a what, sorry.
Liudmila Molkova 01:00:37 That, that pack key, like, the… you cannot use the string representation, you need to access to API to get it.
I personally hate Apacies, they gave me a lot of pain in the past, but this is the language-safe option.
Trask Stalnaker (Microsoft Corporation) 01:00:56 we have.
Dylan Russell 01:00:57 Yeah.
Liudmila Molkova 01:00:58 And we can relax it later, and I think this is somewhat a requirement of the spec, that, at least for the current span.
Aaron Abbott (Google LLC) 01:01:08 Yeah.
Trask Stalnaker (Microsoft Corporation) 01:01:09 All context keys in the spec are supposed to be opaque.
Aaron Abbott (Google LLC) 01:01:15 I think… I think the idea was specifically to outlaw this, right? Like, they want to make sure that you use some API, some public API, to make sure that context sharing is explicit.
Liudmila Molkova 01:01:28 And I hate it, but… Have to live with it now.
Aaron Abbott (Google LLC) 01:01:32 Yeah, that's fair.
But yeah, option one sounds good to me. I agree with everything you said, like, just let lower layers overwrite, and if they mess something up, it's… Kind of on them.
Dylan Russell 01:01:49 Cool. Okay.
Yeah, I'll update the PR with what we discussed, or I'll try to.
And…
Aaron Abbott (Google LLC) 01:01:58 One… you know, one other thought, I just wanted to ask about context-scoped attributes.
this is… this is kind of the opposite, right? It's like, instead of pushing down attributes to be stamped below, you're setting attributes lower down in the call stack.
I don't know, maybe… maybe we can share the feedback on the context scope attributes if… if that's still in progress or something, but they seem like different use cases, I guess, but kind of related.
Liudmila Molkova 01:02:28 What feedback would you share?
Trask Stalnaker (Microsoft Corporation) 01:02:32 I agree that they're… they're, like, complete opposites. One, the context scoped attributes is for enhancing your child spans.
And this is for enhancing your parents' bands.
I don't think… I think both use cases are very valid in certain… in different ways.
I'm not sure I… See an overlap, other than that… They are opposites, and it's a nice way to think of it.
Dylan Russell 01:03:12 So, context scoped Attributes is just, like.
A specific attribute you, like, put in the context, and then… like… Child spins, pick them up.
Trask Stalnaker (Microsoft Corporation) 01:03:26 Yeah.
So, for example, that could be really handy for this group here, for putting the agent name into a context-scoped attribute, because lots of people want to be able to split their… Inference metrics and other things that happen within an agent by the agent name.
Dylan Russell 01:03:54 That makes a lot of sense.
Liudmila Molkova 01:03:57 By the way, we have 2 minutes, but I'm thinking, for the context sculpt attributes, for something like Agent Name or conversation ID, I… For specific attributes.
we… as long as it's not exposed to end users, I think it's okay to implement this propagation in instrumentations.
Because this is… this will be scoped and hidden within the GenAILTL, in Python or whatever language, let's say.
And then the inner layer, it knows which attribute it wants to set. There is a set of very well-known attributes that do this. And we will have to, I think, keep it with the one… even one context call attribute come, because we will need it for metrics.
by default.
And I think context sculpt attributes don't… Need user agreement to put a ton metrics by default.
Trask Stalnaker (Microsoft Corporation) 01:05:02 So you're proposing to, we could implement it the propagation without the SDK supporting context-scoped attributes, we could just do it kind of under the covers as an instrumentation contract.
Liudmila Molkova 01:05:17 Right, and only for the well-known set of attributes, and without exposing any public API to the end users.
Trask Stalnaker (Microsoft Corporation) 01:05:26 Yeah, makes sense to me.
Liudmila Molkova 01:05:32 Okay, cool, then we are at time.
Appreciate everybody coming, keep good stuff coming in, and see you next time.
Aaron Abbott (Google LLC) 01:05:42 So…
Trask Stalnaker (Microsoft Corporation) 01:05:43 Thanks. Bye.
