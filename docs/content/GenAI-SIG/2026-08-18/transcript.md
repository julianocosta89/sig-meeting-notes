SIG: GenAI SIG
Date: 2026-08-18
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Surya Teja 00:03:54 Hey, good morning, folks.
I hope you're having a good day.
Aaron Abbott (Google LLC) 00:04:31 Everyone, how's it going?
Felix Becker 00:04:35 Good, how are you?
Aaron Abbott (Google LLC) 00:04:38 Yeah, pretty good.
Give it a couple more minutes. I don't think Lynn Mill is going to join today, but… Yeah, can wait.
Wait until, like, 3 or 4 after.
Felix Becker 00:04:55 Also, sorry, I'm new here, I'm Felix, I work at Anthropic, so everyone has met me.
Nice to meet you all.
Aaron Abbott (Google LLC) 00:05:05 Cool. Nice to meet you, Felix. Yeah, I see a couple new people. If anybody else wants to say hi, feel free to… Come on.
Nida (Salesforce) 00:05:18 Hi, I'm Nida, I'm an architect at Salesforce, this is the AI innovation org, and I just wanted to plug in here.
And see what the group is up to, where the semantic conventions are heading, especially in the agent and multi-step work.
And hopefully I can contribute back.
Aaron Abbott (Google LLC) 00:05:43 Cool. Nice to meet you.
Yeah, so folks haven't seen, the agenda, I can drop a link here.
But yeah, please add your names, and if you want to add any topics, feel free to, just throw something in the agenda.
Alright, I guess I'll share, I don't think Lamil's gonna join.
Cool. So I think some of these items were probably from this morning's meeting at 7.30, but Unless, Hushing, are you around? Huxing, Steve, Jeremy?
Trask Stalnaker (Microsoft Corporation) 00:06:28 No, those first two were from this morning, but I did… So that I would raise them here.
Hu Xing, did… posted in the Slack, also.
He was just curious if there were… was interest in… This… Instrumentation for the deep-sea harness.
And then more generally, was kind of curious if there was interest in A special interest group specifically for observability for coding agents, Codex… Claude.
I know that… that Copilot already ha… has, emits… Or can we met OpenTelemetry?
So, anyway,
Aaron Abbott (Google LLC) 00:07:33 Yeah.
I mean, it sounds… it sounds pretty cool. I wonder, was… was it more focused on, like, instrumentations, or on… Different conventions for coding agents, in particular.
Trask Stalnaker (Microsoft Corporation) 00:07:47 Probably… Both…
Aaron Abbott (Google LLC) 00:07:53 Yep.
Yeah, I guess the only other thing I would say here is it's written in… TypeScript? It seems like maybe we would want… a new repo, because I don't think it's probably monkey patching based, it's probably just, like, a plugin, but I guess we could check with JS as well, if we did want to have this in OTEL.
Okay, and then what about this one, Trask from Steve?
Trask Stalnaker (Microsoft Corporation) 00:08:25 Yeah, he was asking about, adding a span for skills.
And I was curious if anyone here knew, had background on… I was kind of surprised we don't have a span for skills already.
And was wondering if that's… was because maybe, They're already often captured via tool spans, I don't know, I was looking for… looking for help here.
Aaron Abbott (Google LLC) 00:09:04 Yeah.
This one's been open for a while, right?
I believe.
Trask Stalnaker (Microsoft Corporation) 00:09:10 Yeah.
Aaron Abbott (Google LLC) 00:09:10 She has, yeah.
I wasn't super sure, like, what the time of this… of invoke skill meant. Like, I think in some cases, the skill might be stored in, like, a registry or something like that, if it's not locally, but… I… I don't know, like, if this… This didn't make a lot of sense to me, because it seemed like usually skills just get put into the context for the agent, and there's not, like, a… concrete invocation, but, if anybody has another opinion, I mean… Oh yeah, there's tons of discussion here, so maybe I should just catch up before I say too much.
Felix Becker 00:09:55 Yeah, that's my initial reaction, too.
Aaron Abbott (Google LLC) 00:09:57 Okay, cool.
So yeah, if anybody has thoughts, you know, we can discuss it now a bit, or if you want to take a look, I think there's… Yeah, this issue comment.
Yeah, just from Steve. So it sounds like people are interested, so please take a look at the issue.
Trask Stalnaker (Microsoft Corporation) 00:10:20 So just so I can understand, Aaron and Felix, what you were saying, that, the skill invocation isn't necessarily something we capture, or it isn't necessarily something that happens, it's just additional context that gets put in, and then the LLM makes tool calls based on that.
Felix Becker 00:10:46 Yes and no, like, there's… there's part of the skill description that contains instructions of, like, when to, load the rest of the skill. That always gets loaded into context, and then the if that condition is triggered, and the agent decides it wants to, like, load the remainder of the skill, it'll load, like, read the rest of the skill into context, too. And then from then on out.
it could be, like, various different things that it does, right? Because the skill is really just instructions, and it could say.
I don't know, call this API endpoint, or call these other tools, or it could bundle a binary that gets called, or a Python script inside of the skill, but it's like… It's hard to, It's hard to, like, say what the, like, standard, rigid, you know, behavior will be that you could model as an operation here.
Trask Stalnaker (Microsoft Corporation) 00:11:47 Cool, thanks, that helps a lot. I'll reply to Steve. I told him I would… Provide him the feedback from this meeting.
Aaron Abbott (Google LLC) 00:11:58 I wonder if they have something in the deep-sea harness instrumentation for this, because… It seems like one where we would want, I guess it's possible that some coding agents out there do treat this differently.
But yeah, I agree with what you, like, said, that's what I mean.
Felix Becker 00:12:14 Maybe an operation could be, like, load skill, but, Even then, like, the loading itself usually wouldn't be, like, an expensive operation. It's more like the next inference request that then contains more context.
Be maybe a little more expensive, or take some time.
Aaron Abbott (Google LLC) 00:12:42 Okay, cool. Any other thoughts on this one?
Alright, Jeremy, are you around, or…
Jeremy Eder (Red Hat LLC) 00:12:56 I'm here. Hello, folks.
Aaron Abbott (Google LLC) 00:12:58 Great.
Jeremy Eder (Red Hat LLC) 00:12:59 Yeah.
Aaron Abbott (Google LLC) 00:12:59 Do you want to talk about these?
Jeremy Eder (Red Hat LLC) 00:13:02 I… I… yeah, it's, so the… I… I joined it maybe in the end of June.
Looking at… Cost overall, cost per turn, and budgeting?
To kind of do, yeah, all kinds of instrumentation and control for the users.
some dude from Disney, who I don't see on the call here, has sent a PR for it, and I wanted to call attention to specifically 443, which closes 287.
Which, 287 was my E0 at the time, so… I don't know if anything is holding these up, or whether they're just looking for review, but these are going to be very important for us to pull the next level of fidelity out of traces that we already received.
Aaron Abbott (Google LLC) 00:13:51 Yeah, I think…
Jeremy Eder (Red Hat LLC) 00:13:52 So it's kind of just a call to… yeah, sorry.
Aaron Abbott (Google LLC) 00:13:54 No, no, I was gonna say, yeah, it looks like there's maybe some discussion here. I know we've been chatting about this a lot, but mostly in the context of, like, token attribution, and then one of the things we kept discussing was Whether we should focus on recording the like, token counts and calculating the cost on the back end versus trying to stamp the cost in the client side, and then I know thentic folks are pretty interested in this, and there was, Yeah, Alex has commented here, but there's a Pydantic library that has, like, current costs for… LLMs, but… Yeah, I don't know, was there any discussion on this PR about that? I assume it's stamping the cost directly.
Wolfgang Therrien 00:14:39 Yeah, we're at Honeycomb, we're using, the, a similar approach where we're stamping the cost, derived from token usage at ingest, and so it's, it's really interesting. We're really interested in getting this, getting this through, as well here. I haven't had a chance to catch up on the… the rest of the… the comments here, but, If you ever following along, and we're really supportive of this one as well.
But it seems like there's still some open, questions about, sort of, like, the namespacing issue.
Like, where it should live under the namespace.
But yeah, I can… I can follow up and, and, and add some more… add some more comments in there as well.
Aaron Abbott (Google LLC) 00:15:31 Awesome, it looks like there's a good review. Oh, sorry, go ahead.
Felix Becker 00:15:34 Yeah, I have a question on this. I don't know how this is usually done in OpenTelemetry for monetary values, but I see it's a double here in the PR. Is it… More, like, common to use doubles for monetary amounts, or, like, minor units and integers?
Trask Stalnaker (Microsoft Corporation) 00:15:58 I don't think we have anywhere… In semantic conventions, that is capturing cost At this point, so I don't think we've ever thought about it.
Felix Becker 00:16:14 Okay, yeah, I know in the Anthropic APO, we decided for minor units, there's a bit of a wrinkle that sometimes I think we can build partial minor units, too, so… It gets a little tricky sometimes, but I'm wondering if, If this should… Be an integer instead of a double in minor units.
Aaron Abbott (Google LLC) 00:16:41 Did you say binary units, Felix?
Felix Becker 00:16:43 No minor units, so, like, cents for dollars.
Aaron Abbott (Google LLC) 00:16:46 Gotcha, yeah.
Wolfgang Therrien 00:16:49 Is there any inspiration to be had from the open cost project, which is, like, another CNCF, I'm not quite sure how they represent cost, but that's, like, costing for, infrastructure.
Felix Becker 00:17:11 Good question, I'm not familiar with it.
Trask Stalnaker (Microsoft Corporation) 00:17:16 I just…
Wolfgang Therrien 00:17:17 remembered that it's a thing, and I'm not, I'm not super familiar with it either, but if they have a, a preferred format that also makes sense for this. It might be useful to align there, unless there's a good reason not to.
Felix Becker 00:17:34 Yeah.
I guess it would be interesting to hear from, platforms, anyone that ingests these attributes or plans to ingest them, if having them in doubles would cause any, like, potential issues with summing them up and, like.
you know, bad calculations.
Aaron Abbott (Google LLC) 00:17:58 Yeah, I would just say, I don't know if this was proposing just span attributes, or if this was proposing metrics, but… like, Prometheus represents everything as a double.
So it… it kind of… we try to, like, index a little bit on the open source use case there, and I think most OTEL native, like, you know, span, log backends, they can round-trip all the stuff that OTEL supports, but… At least for Prometheus, if it ends up in metrics, it would be converted to double eventually.
Trask Stalnaker (Microsoft Corporation) 00:18:27 Yeah, that's a good, Reference, like, possible prior art was the tracking, duration.
Has seconds versus… Milliseconds or nanoseconds, which is… Standard semantic conventions to track durations as seconds.
It would be great if somebody, could open a… I would suggest open an issue in the general semantic convention repo.
Feels like that would be something nice to get, sort of general consensus across semantic conventions.
Ankit Singhal 00:19:21 Another aspect of the currency?
Depending upon… Where you're looking at some… Like, dollar response versus yen.
Felix Becker 00:19:38 Sorry, can you repeat that?
Ankit Singhal 00:19:40 So, the currency, like, okay, in the US, yeah, you're gonna talk about dollars, in Europe, you're gonna probably talk about pounds, right?
And… in… say, China, you'll talk about yen, or that's the currency you would want the cost to be shown in.
It's more like a normalization, or, you know, Yeah, 18, and I forgot what that's called.
Felix Becker 00:20:10 So you're arguing for, having a major unit.
Ankit Singhal 00:20:16 Oh, not exactly, but I think this aspect goes in parallel with that, right?
All right.
Calculate, but then showing the value in dollars versus pounds, depending upon Like, where the user is, right?
Trask Stalnaker (Microsoft Corporation) 00:20:37 Does the PR today say anything about currency…
Wolfgang Therrien 00:20:44 Yeah.
The… the proposal, has a required field that stamps the currency that the cost was reported in. And so, you know, at least at the time of… well, at the time of recording, it was, you know, this many dollars, or this many yen, or this many, euros.
Which I think should be enough for a client to do a conversion if they needed to convert it to another amount.
Do you… are we seeing that there, like, that… we need additional data recorded on the span?
In order to service the use case.
Or do we feel like currency… the recorded… Currency unit is… is sufficient.
Ankit Singhal 00:21:50 To be honest, I don't have an answer yet, but I'm just thinking about, like, the conversion from one currency to the other fluctuates and changes from time to time, right?
currency reporter, like, today might, like, say, $10 reported today might not actually be, say, 8 pounds, tomorrow, right? Yeah. So, I think there's a conversion rate that might come into picture there.
Worst case. I don't think I have a solution to it, but I'm just thinking out loud here.
Aaron Abbott (Google LLC) 00:22:20 Yeah, no, that's helpful, and I think the localization is probably non-trivial as well.
So I guess the user would have to configure the currency, or we could… Try to figure out where they are based on locale or something like that, but it seems like a big can of worms.
I think… Yeah, go ahead.
Felix Becker 00:22:40 The other thing I want to ask about the… where are these attributes supposed to go? Like, what operation are they intended to be attached to?
And the reason I'm asking is that, is that billing is usually an asynchronous process for all the, like, major providers, so… the, like, actual cost. Like, we know the token usage after every inference request, but you don't actually know the real cost that was incurred for those tokens until, like, after the request has already finished.
And so, if this was supposed to, like, go straight onto the, like, chat spam, you don't actually have that information yet. What you could maybe do is, like, estimate it just based on list prices, but, you know, there's, like, many different things that go into cost calculations.
Aaron Abbott (Google LLC) 00:23:38 Yeah, I think… I think there's a lot of providers who are already doing this, and I think part of it is, like, a feature, like, because the asynchronous, at least we hear this, you know, from Google customers, the asynchronous billing is It's difficult to, like, understand what's happening in more real time, so… I don't know if it's… intentional, but it looks like, it's for inference, embeddings, agent, and workflow spans without per-type duplication, so… Yeah, there's a currency code attribute.
Not sure what this source is, and… There's a metric for operation cost.
Wolfgang Therrien 00:24:16 Yeah, I think so.
Felix Becker 00:24:17 Actually, histogram metric is interesting, because that could be reported, asynchronously.
I'm not sure, like, how we would… Report, like, true cost for each… For each inference span, unless… We're like… Delay it super low, but it would be very, like, challenging to implement, like, delaying the inference span until you have that attribute.
or… Maybe the spec would need to say, like, it's okay for this to just be, like, estimated cost, but,
Wolfgang Therrien 00:24:57 I think that's the intent behind the source attribute, so if there is… if a provider can, sort of.
Felix Becker 00:25:05 Hmm.
Wolfgang Therrien 00:25:06 give that information back, sort of real time. That's, I think, what the source equals provider means.
pricing table… I don't quite appreciate the difference between pricing table and estimate. I think pricing table is maybe the customer has established their own pricing table and is self-reporting their cost, because maybe they have negotiated terms, and then Estimate is, I believe, something that is, using sort of an aggregated or open-source, like, third-party MSRP-type, pricing… pricing table.
And so, maybe that… Maybe that means a little bit more… more clarity.
Felix Becker 00:25:45 Yeah, I think the enum could be a little clearer here, because also, if I'm the provider, and I'm giving you an estimate, do I use provider, or do I use estimate?
But I also wonder if maybe… like, the attributes should be separate, like, maybe there should be a usage.estimatedCost and a usage.
Cost.
or it seems like it would maybe be a bit more complicated to… Sum up the costs, and without, like, mixing… accidentally mixing, like, real costs and estimated cost together.
Wolfgang Therrien 00:26:23 Yeah.
I wonder… If there's also maybe a separate telemetry shape, if it's not realistic for providers to give you actual costs, sort of real time, there… could be instrumentation that emits something else that is linked to that span that has done the work, that says this was the actual cost for this span. It could be an event that gets emitted that's, like, cost calculated or something.
That, I think, is less… Clear and less ideal, but that… is a way… that the information could be housed, but that's… that's probably… that is well outside the scope of this conversation, I think.
Felix Becker 00:27:08 Yeah.
I think, generally, it's something that I've run to many times that's a little unfortunate that, like, you cannot… like, you have to… in OpTelemptory, you have to spend a span in its completion, like, you can only send it once it's completely full and has all the attributes attached to it.
You cannot add attributes later, or you cannot send attributes before the span is completed.
So… This feels like more of a shortcoming that's maybe not specific to this.
PR, but… Definitely something that, kind of shows up here.
Jeremy Eder (Red Hat LLC) 00:27:49 Yes, I have a use case, where it's not for billing.
But it is for, like, routing, cost-based routing, or even value-based routing. So someone mentioned, like, when we negotiate deals with different providers.
This is essentially us trying to do dynamic cost arbitrage across providers, where they are the same, essentially, for us, in terms of capabilities. So that's what I would use it for. I don't necessarily need to the sense accurate, that can be an offline reconciliation, like someone just mentioned.
But having it in real time is made… is meant to program a routing tier.
For our users.
Felix Becker 00:28:26 And you would use OpenTelemetry to… to do that routing?
Jeremy Eder (Red Hat LLC) 00:28:31 No, we have… no, there's backend solutions for… It, but the… the cost flowing through the entire System are meant to output a routing rule set.
That we put into our router for it.
And then users hit this routing, you know, just an OpenAI-compatible endpoint, and they get what they get.
Based on the business policies that are Yeah, this is.
Felix Becker 00:28:57 Oh, you just want to emit these attributes from your router that already does, like, kind of pricing table, like, cost calculation.
Jeremy Eder (Red Hat LLC) 00:29:06 We already have costs on the side, for those… so that's a… that's the equivalent of the… I guess it was a pricing table or something in there.
We thought about making those more and more dynamic over time, but it's essentially real-time Dynamic.
Cost-based routing across many providers.
We use MLflow on the backend, if that matters at all, and so my current setup is just annotating those afterwards, and I can kind of reconcile, sort of, the similar approach here, so it's not a complete gap for us, but I'm working to make sure this works across solutions.
Felix Becker 00:29:41 Got it.
Ankit Singhal 00:29:42 No, I think I like that approach where we're not putting this in the inference path, and would rather, like, stamp this on the spans in the Like, after they are emitted, but in the processing stage.
Jeremy Eder (Red Hat LLC) 00:30:05 Okay, there's an argument, for that as well, I understand.
One question, excuse me here, but… The completion of a span may introduce latency to the request, but what the concern was in doing it in real… in, like, inline.
Ankit Singhal 00:30:24 Yeah, yeah, definitely.
And then, I think, if you have to, like, get the billing information, which is not, like, a static data from somewhere, I think that would also lead onto the latency. Yes, I mean, some of them could be mitigated, but then still, it's gonna be in that hot path.
Both entrance to nature.
Aaron Abbott (Google LLC) 00:30:49 Yeah, I mean, I think in most cases, like, at least what I've seen with is you include the library with the costs.
in your process, so it's probably just doing some really basic math. I don't think it would lead to a lot of latency, but I see what you're saying. If you wanted to have, like, a more robust pipeline, it doesn't depend on whatever's, like, linked into the process, so…
Jeremy Eder (Red Hat LLC) 00:31:17 Okay. I don't know if it would help with, like, benchmark both ways.
But, I can get away with the annotation afterwards, it will just add a little bit of dependency on an external solution for our end.
Aaron Abbott (Google LLC) 00:31:30 Yeah, I mean, it's not… yeah, I was gonna recommend, you know, everybody's interested, please take a look at this PR offline, and if we have, like, questions about the scope or the use cases, maybe we can clarify that a little bit. I think everybody has maybe different Different use cases in mind, but, yeah, we should record them maybe in the issue or something like that, so…
Trask Stalnaker (Microsoft Corporation) 00:31:53 And Jeremy, if the concern is adding latency to the application, I mean, you can delay sending the span. You can capture the end duration when it ended.
And then, you know, push that off to some… Background job that then… Gets whatever you need.
finishes up the data on that span and sends it, you know, as long as it's not excessive and that it's going to cause delays to people seeing their spans ending But you can retro… you can retroactively set the end time on it.
Jeremy Eder (Red Hat LLC) 00:32:37 Got it.
Thanks for that, Trav.
Aaron Abbott (Google LLC) 00:32:44 Any other thoughts on this one? I think there was also this PR.
which is slightly different, but this was… yeah, Jeremy, did you.
Jeremy Eder (Red Hat LLC) 00:32:54 I flagged as related… I flagged as related because this is kind of the intended goal here, is to make agents more efficient by forcing them into these budget buckets.
And… well, at least seeing how it goes. And so I saw someone with a very similar idea. My guess is these folks at Disney are trying to do the same thing we're doing here.
Should probably reach out to this guy.
Aaron Abbott (Google LLC) 00:33:17 Yeah.
Okay, cool.
Unless anybody has any other thoughts, I think we should probably move on.
I guess I can go through this one. So, Ludmol is not here, at least Python GenAI. I think I was planning to do that.
I could do it probably tomorrow, should be pretty routine. I don't think we've got a lot of stuff, but if anybody has, anything in particular, you know, please reach out in Slack or whatever, and we can make sure some PRs get in, but… Yep, and then the other thing was releasing the deprecated old libraries from the contrib repo.
I think that will just… We will have to go and do that manually. We've already updated all the READMEs.
To add deprecation notices, and… Yeah, should be routine.
So I think… I think this is pretty much all on me.
Okay, cool. Habiba, are you around? You want to talk about the guardrail PR?
Habiba Mohamed 00:34:23 Yep, I'm here. Can you all hear me?
Yeah, okay. So yeah, I'm just bringing 427 back up. There's, since we last talked, I did the refactor to remove security versus generic namespacing.
The point you brought up last time, Trask, about the generic framework instrumentation, whether you can, like, infer if a guardrail is security, related.
So I took that away, so then the top-level namespacing is just GenAI.Guardrail, for the base tier frameworks.
Let's see, what other major changes? I think that's pretty much it, and then I did do a review. I don't know, Erin, if you had a chance to do a pass-through at all the fields, and I think they're all the minimal, like, set of fields that we do need, And then… let's see, I removed the span hierarchy language, and I think that's about… that's… that's the main one. And then for today, I wanted to kind of discuss there was, one thing that came up in the last PR, which was closed out, carrying over from Nakumar's PR, but, verdict type versus action type. There was a question of whether they mean the same thing, if anyone has any feedback, they can add to the PR, but I think they're both orthogonal, given that, like, a verdict would be the guardrails judgment, and then an action, is what the caller essentially enforced, so I think we do need verdict type and action type, for both.
But yeah, I think that's about it. I think it's coming along pretty well. There was one… part where, what was it? I think Lyudmila had put up a point about doing some, some research. I did some system-evaluated research. I'm not sure if we should add any of those to the docs, or, like, where… I'm guessing under docs, GenAI would be a good place to place it under, but there was one sort of asking, evaluating which systems, Or, the list of systems that were evaluated that share properties that map to the attributes. So I can add that there.
And then there was one… was it… I don't know if Surya's on the call, but he… you brought up a point about someone had brought up a need for an AI threat detection span.
I think we should… we could maybe follow up with that, honestly, but I think the guardrail base tier should stay separately for now, and then we can kind of follow up with a… with a GenAI threat detection, spin, given that I want to kind of look into, like, how auto… how well we can kind of auto-instrument that. And then a lot of the detection engines, they emit… I'm not sure if they really… emit spans, and how that would work, so…
Surya Teja 00:37:19 Yeah, yeah, that makes sense, Habiba. I'm fine with it, yeah.
Habiba Mohamed 00:37:24 Sounds good, okay. So I'll just ask for another round of reviews, Erin. I don't know if there… there haven't really been any major changes, and then, the… the comments from the previous PR were all… well, they were closed, but I addressed the… the… the changes here.
Aaron Abbott (Google LLC) 00:37:41 Yeah.
No, it looks good. I did take a quick look, and I passed it on to the Model Armor team again. I'd like them to, you know, even if it's just rubber stamp again, just take another look.
Yeah, maybe we could look at these scenarios a little bit, because I think that was one of the interesting points, but yeah, I already looked at these.
data JSON files here, this looks pretty good, so… Yeah, you wanna go ahead, Felix?
Felix Becker 00:38:09 Yeah, I just wanted to… sorry, I didn't read the PR in depth, I just kind of skipped it, but just wanted to ask a general question, like, what… what… how do we define, like, what a guardrail is? Like, the purpose of when these, attributes should be used, and which providers, would this be implemented today? Like, is… Is any sort of safeguard, a guardrail, or, is it, like, a specific… API concept of a guardrail that only exists in certain providers.
Habiba Mohamed 00:38:42 No, I think it's just a generic sort of guardrail, because there's gonna be policy guardrails, right, security guardrails. Initially, this PR was introduced for generative, like, securing generative AI, and so how would you, for example, emit spans for XPIA, like prompt injection, or any of the top 10 sort of OWASP, LLM, vulnerabilities, and then also security events. But then it was a little bit more generalized for just guardrails in general, so any sort of… yeah, any… any guardrails, I guess, you would place within the system, and I… we did utilize OpenAI's, I think that was the main example, was the sort of OpenAI, library, so…
Felix Becker 00:39:28 Okay.
So is OpenAI the only provider that provides this right now?
Habiba Mohamed 00:39:33 There's a few examples, let's see… hold on, let me pull it up.
Felix Becker 00:39:41 Like, basically what…
Habiba Mohamed 00:39:42 Yeah, there, yeah.
Felix Becker 00:39:43 in my head is, like, do we already have this Anthropic as a, like, thing that we would annotate this with?
Or is this maybe for a future thing that we don't have yet? In which case, I would wonder, like, would it, would it, you know, is it general enough to apply to those two?
Habiba Mohamed 00:40:02 Yeah, so what we have right now is OpenAI Guardrails, Nemo, there's the AWS Bedrock Guardrails, and there's the Azure AI Safety Content, and then, the first PR that we ended up closing, this… some of the spans were pulled into, the model armor.
SDK as well, so…
Felix Becker 00:40:24 Okay, I might just have to read up more on those.
Habiba Mohamed 00:40:26 I'm up.
Felix Becker 00:40:26 Play out with those features.
Habiba Mohamed 00:40:29 Sounds good.
I'm not sure who was next. Is this Surya?
Aaron Abbott (Google LLC) 00:40:34 I think… I think Surya, but Surya, were you gonna… were you gonna reply to that same thread there?
Surya Teja 00:40:38 No, no, no, I had a doubt, actually. However, when I was discussing this with Naq Kumar, I asked him in doubt whether… Cloud agents.
There are a few security hooks that run before, any command is run, whether.
Habiba Mohamed 00:40:54 those.
Surya Teja 00:40:55 come into this, span or not, and he said that, yeah, they are going to get covered under this span, because those are security checks that any agent framework or something runs. So, my question is, as, if I'm understanding it right, Anthropics tool hooks, or those come under this span, right? Or are we going to have different spans for that?
Habiba Mohamed 00:41:23 I think I would have to review that initially, if you discussed that with Nakumar, but maybe… yeah, I'll follow up with that, Surya.
Surya Teja 00:41:30 Yeah, sure, I can write up something and ping you on the Slack if you're in Slack.
Habiba Mohamed 00:41:35 I am.
Surya Teja 00:41:36 Yeah, cool, let me repeat.
Felix Becker 00:41:37 we added a feature in the Anthropic API for users to, like, specify their own safeguards that run on their prompt and tool results, would that be considered a guardrail?
Habiba Mohamed 00:41:51 Yes, yep, it would be.
Aaron Abbott (Google LLC) 00:41:57 Yeah, I was gonna… Felix, I think that's a good point. I was gonna raise that this was… kind of initially more targeted at, like, cloud providers, where there's a policy which is kind of externally defined, so it is kind of API-focused right now.
I don't know if it would work for something like what Surya just said about if you set up, like, a plugin in Cloud or whatever, if you… it seems more like if you had something in the inference layer, which is kind of part of the proxy, and something the agent doesn't opt in or out to. I know, like, at least for Gemini, we also have some built-in, like, safety thresholds for various things, but we don't… I don't think we consider that part of… model armor, because it's just inference spans. Like, it's just an option on the inference spend when you call the Gemini API. So, like, this is more kind of, like, externally managed, I think, kind of focused on APIs, but I mean, keep me honest, Habiba.
Habiba Mohamed 00:42:51 No, it is focused on APIs and sort of whatever guardrail outcomes, right, the results, and then also security events, so that if there is anything, essentially, if there was anything… if there were any violations of guardrails, what… capturing the result of that as well. So…
Aaron Abbott (Google LLC) 00:43:14 Yeah, and I just…
Surya Teja 00:43:16 So, Gordon.
Aaron Abbott (Google LLC) 00:43:18 Yeah, one more piece of context I was gonna say for model armor, these spans, we don't follow this exactly, but we were… you know, inspired by this when we were adding instrumentation to Model Armor, but the instrumentation is something that's part of, like, the Google Cloud platform, so the spans come out of Model Armor, you don't do the instrumentation itself, it's just kind of part of the service.
Surya Teja 00:43:45 Yeah, I'm just going to repeat what I understood, Aaron. Just correct… feel free to correct me. So, OpenAI Agent's Framework has guardrails, which are going to run before a tool is being run or anything to have some safeguard. And similarly, I guess cloud agents also have some folks Those will not be covered under this guardrails ban, if I understand correctly.
Habiba Mohamed 00:44:10 That's correct, yeah.
Aaron Abbott (Google LLC) 00:44:12 Well, Habiba, the example here, one of them was OpenAI too, right?
Habiba Mohamed 00:44:15 Yeah, I'll review the point you mentioned, Surya about hooks, but I don't believe so.
Felix Becker 00:44:24 Why would they not be covered?
Habiba Mohamed 00:44:29 Oh, on why they would not be covered?
Felix Becker 00:44:31 Yeah.
Habiba Mohamed 00:44:34 That's a good point. So I guess my… my point is that the… the vulnerabilities that this was, like, mapped to was the OWAPs… OWASP top 10, and so for hooks, were you saying that it's more of, like.
To hope to essentially, like, load, like, metadata, like, in regards to a tool call, or is it something that would be happening exactly at one time?
for, like, an action. So…
Felix Becker 00:45:00 It happens at runtime, but the hooks are very generic, so I guess you can implement a guardrail in a hook.
And then the question would be, you know, would… if you do that, would you report Guardrail spans from that hook.
Habiba Mohamed 00:45:20 I can give that a review to kind of see exactly.
We'll follow up. I'll follow up next week on that.
Aaron Abbott (Google LLC) 00:45:35 Okay, cool.
Yeah, and also, if you take a look at the PR, please also look at the reference scenario. I think So there is OpenAI guardrails, and I think it might just help to… help everybody get on the same page, so… I can drop… A link in here too, but… Anything else on this one?
Habiba Mohamed 00:45:56 Nope, I think that's it.
Aaron Abbott (Google LLC) 00:45:59 Okay, cool. Ankit, do you wanna… Talk about real time.
Ankit Singhal 00:46:06 Yeah, so, I think the major update is, based on, like, the feedback and some discussions last week, about the open questions, whether you want to model The long-running WebSocket connection, and I think we discussed that it would be more events limited, so I made that change. The other one is about the, span. I named it as Generate Live Content for now, but I'm open to suggestions on the name of the operations for, real-time.
model content generation. So, And then the other one was about the span for the user input, and if the provider has enough VAD events to figure out when the user activity started and when it ended. And it could be optional and, based on the provider.
So, I think I made these 3 major changes, and then there are certain related to the, like, the attributes needed for audio tokens. So, these three major changes in the PR, as per the discussion last week. So, would appreciate if I can get some reviews, and feedback on the PR.
While doing this, like, one, question that came up was.
How do we link the events to the trace?
So, I think I wanted to see if we had any suggestions around those.
Aaron Abbott (Google LLC) 00:47:41 I don't know if I have a lot of context here, to be honest, but one thing I was thinking was… since I think both of these use WebSockets, there should be some kind of parent HTTP span for the WebSocket, handshake.
I think that was one of the things we were saying we should check, is, like, if we look at some of the Python instrumentation that exists today.
For, like, HTTPX, or… Whichever… whichever thing that these client libraries are using under the hood.
It might be good to see if there's a parent spend that would just naturally be there to model this on.
But I haven't really dug into that deeply, it's just kind of my first impression.
Ankit Singhal 00:48:21 AC? Okay.
I don't, like, I was looking at the session ID, that's available for GPT real-time, but for GenAI, it was not so clear whether it's available. Like, you can pass in when you're doing, like, this WebSocket connection.connect, but it was not… At least from the documentation and from the source code, it felt like it might not always be available.
However, for open… OpenAI real-time, it's… it's there, it's generated by the service. So, I don't know if it's a difference between the developer API versus the Vortex, right? And we have seen some differences, so… Yeah.
So I just also wanted to see if there was a suggestion if… it's okay to generate a session ID if it does not exist, or, like, a conversation ID if it does not exist.
Aaron Abbott (Google LLC) 00:49:15 I think Lyudmila would probably have some thoughts on that. I… yeah.
Ankit Singhal 00:49:22 that's.
Trask Stalnaker (Microsoft Corporation) 00:49:23 I feel like we've said no to, before, to generating Kind of a fake one.
Cause that would be more about, like.
modeled in OpenTelemetry as a span… I mean, there's… there's other ways… As far as linking your events to the trace, I mean, whatever…
Ankit Singhal 00:49:47 Yeah.
Trask Stalnaker (Microsoft Corporation) 00:49:48 Yeah, whatever the outer… span is?
Right, that should get linked, that should be the parent for the events. I mean, it's… events have a trace ID and span ID.
Ankit Singhal 00:50:04 Yep.
Agree. But I think in this case, like, since we don't have a span for the WebSocket connection, right?
Like, this… If I'm not wrong, there's no span when those events would be immediately.
Trask Stalnaker (Microsoft Corporation) 00:50:22 Is there a span for the agent above that WebSocket?
Connection?
Ankit Singhal 00:50:31 So this is for the, just the real-time model inference, so… It could be or could not be, possibly.
For example…
Felix Becker 00:50:41 Doesn't this proposal define a new span, generate live content? I was just reading through it.
Ankit Singhal 00:50:47 Yes, yes, it does. It does. But this is after, like, the WebSocket session connection is set up, right?
Felix Becker 00:50:56 Okay, but that's the same for, like, you know, chat spans too, right? Like, there's an HTTP span that just, like, represents the… the HTTP request, and then there's a child span of, like, when inference actually happens, and, like, that's the…
Ankit Singhal 00:51:12 Yeah.
Yeah, I think, yeah, we did discuss there were, like, some… like, high-level differences on those, where in case of, like, the X-based LNMs, like the… there is a distinction between the request and the response, right? And you make a connection over, like, HTTP or… However, in case of real-time, it's like you create some… you create a long… a long-lived WebSocket connection, even, so… and you start streaming over that connection, right? And then influence can happen.
Trask Stalnaker (Microsoft Corporation) 00:51:50 point Felix is making is that inference spans, client spans.
also may or may not have an outer, like, span, like, if they're inside of an HTTP request service.
then they have an outer span, and they're linked up that way. If they don't.
they just don't have a span, and they're all, you know, independent, and you don't get correlation, which sucks, but that's why, you know, like, then you go back and you're like, oh, I don't have any correlation, so I create a span around them, even if you have to do that manually.
Ankit Singhal 00:52:32 Oh, so you're saying we would, like, if there is no outer span to link the session events to, we would create some span, and we don't know what that span is.
Trask Stalnaker (Microsoft Corporation) 00:52:41 We wouldn't. No.
Ankit Singhal 00:52:43 I see.
Trask Stalnaker (Microsoft Corporation) 00:52:44 But the user… I mean, it's… Right, in a lot of scenarios, there is an outer span. In most… hopefully in most scenarios, there is an outer span already.
Felix Becker 00:52:58 And then the most… the more important attribute is actually GenAI.conversation.id, right? Because…
Ankit Singhal 00:53:04 Yeah, yeah, yes.
Felix Becker 00:53:06 the HTTP… the WebSocket may drop as a reconnect, like.
Ankit Singhal 00:53:10 Yeah, yeah, yeah, yeah, exactly. But I think what I found was, like, in OpenAI, OpenAI real-time model, there is a conversation ID I can put in there which can correlate, but in case of Gemini Live, it's not always present, depending upon… I think there are two flavors. One is the developer API, the other one is Vertex API, so… And there's no, like, conversation ID, per se, that's exposed in Gemini.
But there is an optional session ID.
And in LLM cases, we have used in the past, where if, providers, they manage the conversation as a part of the session, you could use that.
So, I think that's why I was kind of… Asking, if there is no session ID provided by the provider, can we… create, like, a fake one, but I think what Trask is referring to Sweet.
Probably don't want to do that.
So, just looking for alternatives then.
Hey, Aaron, please go ahead.
Aaron Abbott (Google LLC) 00:54:12 Yeah. I mean, I think I kind of agree with Trask, maybe it can just be out of scope, where we can let it be… whatever the behavior of the system is, and we can figure out if there's an issue, and especially if we're writing instrumentation, add something special. We need to, but…
Ankit Singhal 00:54:29 Got it.
Trask Stalnaker (Microsoft Corporation) 00:54:30 And if you… if you want, like, you could have an opt-in span for the WebSocket, the duration of that WebSocket, kind of modeled after the gRPC, long span there.
But as we discussed, I think, last week with Lynn Milo, that we're not quite sure that that's the best modeling, a great modeling on the gRPC side anyways.
Ankit Singhal 00:55:00 Yeah, exactly, I think that's why I didn't put that in this PR at least, because there were… Kind of consensus on, like, having a span which leaves, like, an hour or more, might not be a feasible one.
Trask Stalnaker (Microsoft Corporation) 00:55:14 Yeah, I would just… I like Aaron's proposal, just leave it out of scope for now.
Ankit Singhal 00:55:21 I see, okay, then I can document that for, for probably, Gemini.
We can… if you want to… capture them, it needs some sort of span around them, or… Optionally, we cannot capture, or we do not capture the events for this session.
Trask Stalnaker (Microsoft Corporation) 00:55:45 I mean, we capture the events, and they're in the context of whatever the outer span is.
Ankit Singhal 00:55:53 If it exists, yeah.
Aaron Abbott (Google LLC) 00:55:55 Yeah, and one more small suggestion is you can… it's fine to parent events on, like, a closed spin, or a finished spin, I think, so if… even if the outer span doesn't… doesn't need to live the entire time that the WebSocket is open and all the conversation is happening, they can still cascade underneath the handshake if that's something that works well when we test it out.
Cool. Ankit did… I also saw that there was a couple docs you shared here, Should we, like…
Ankit Singhal 00:56:32 So yeah, it's the same. I think we've been discussing on those talks, right? So, I think…
Aaron Abbott (Google LLC) 00:56:36 Okay. Is this one ready for review, then? Would you, like, should people take a look at this PR and leave comments there, or look at the docs first?
Ankit Singhal 00:56:42 Yes, please. I think, Docs has, like, a high-level idea on, like, how we got to that PR, so, that'll be helpful just to get the context, and then PR has, like, somewhat more, like, details.
About the span, the attributes on it, things like that, yeah.
Aaron Abbott (Google LLC) 00:56:59 Okay.
Cool, awesome. We've got 2 more, and I think we have, like, 6 minutes, so, try to go through both quickly.
Mohnish and Marisa, you run?
Marisa Boston 00:57:12 We are, and just really quickly, Erin, I'm pretty sure that we are close to pushing this PR. We have one out, like, outlying comment, and we just wanted to get finalization on that. I think we can get it in the next 6 minutes, and then I think this PR can go in, so let's see if we can do that. Manish, go ahead.
Mohnish 00:57:30 Yeah, so we had a little bit of questions on the auto-instrumentation guidelines, so Trask, he shared a skills.md file on capturing the right data.
So we got some comments from Leot Mila on, how do we get those things, but, so talking about the fields in the first place, even before talking about the reference scenarios.
Most of the fields that we proposed. So, the fields were related to the provenance of evaluators, and there are 3 libraries which has evaluation module, which is, Deep Eval, DSPY, and Azure AI Evaluation.
And none of them are auto-emitting those fields, such as ID for an evaluator, or the version, or the reference at ID. So we are constructing it manually with some of the existing fields, like adding the model name to the version, so we are just constructing it.
And we are not sure if that is the right way to do it, according to the guidelines of the OpenTelemetry instrumentation, because some of the fields that we constructed were, from the suggestion that we got from Lyudmila, that this ID could be constructed this way, and… And then we got some contracting comments on, why is it being constructed if we can track it individually. So, that is where the confusion lies, if someone can help that.
Aaron Abbott (Google LLC) 00:58:54 Is there a specific, like, comment or somewhere in this thread that I can… that we can point to?
Mohnish 00:58:58 Yeah, if you could go a little up, yeah.
Not… oh, no, no, no, not that. Could you please scroll down a little bit?
Aaron Abbott (Google LLC) 00:59:07 Yeah, yeah, I can also search.
Mohnish 00:59:09 search for the ID, Yeah, so that was the comment, yeah. The field… No, it was not this one,
Aaron Abbott (Google LLC) 00:59:28 Would you like to share, Moish, by the way?
Mohnish 00:59:30 That works better.
Aaron Abbott (Google LLC) 00:59:31 Yep.
Mohnish 00:59:32 Just give me one second…
Marisa Boston 00:59:39 So the main thing about the comment is that, like, we can create an ID field, and the way that we're creating the ID field right now is from information that's already being emitted, but that's just because of the way that, you know, it's a new… we're putting together a new PR, and we're hoping that eventually these IDs will be unique beyond the information that is currently emitted, just because of what is there. So I think, like.
I would argue that the ID, a unique identifier, would still be useful, even if right now it is being filled by information that is, already coming through from these… from these only 3 libraries that are doing it. I was just talking to the people at Langchain, they would definitely be using this if they said… if it came through.
And they would be interested in it. So, I think that's just where we're… going back and forth, and I think if we can just resolve it and say an ID is still useful, even if right now it's only being populated by information that is already collected in other fields, but long-term, it is meant to be its own unique identifier.
Mohnish 01:00:42 Yeah, so one of the suggestions that Louvid Mila gave was… so, this was a table for these three libraries that I mentioned, and these are the fields that we proposed. So, one of the suggestions that we got was, like, we can construct an ID with the name, and concussenating it with the evaluation model.
So most of them are not native, and we are going to construct it either through the existing fields, or leave that has a capture gap, which we could not do that.
So, that is where, we sort of get a confusion on, should we, construct this, or should we just leave? So, one of the, The comment that I got was, if something that is generic instrumentation, is it a property or a dataset that it derives? So, if someone can give me a suggestion on should we construct it or leave it as a gap, that would make this very clear.
Ankit Singhal 01:01:42 Hey Marcin, just one quick question, like, what's the motivation to capture the evaluator… this is the evaluator idea, right?
Mohnish 01:01:50 Yeah, it's not just the ID, it's the provinces. So, if there are multiple evaluations that are happening at from the library or any other custom library. We are not sure which evaluator is doing what. So, the type, the ID, the version, and what scope it's capturing, that is our proposal overall.
Trask Stalnaker (Microsoft Corporation) 01:02:20 So, I don't think we're, marisa, sorry, I don't think we're going to get resolution on this without Ludmila.
I would just… Make sure to, you know, is this clearly… have you replied in the PR?
With this info already.
Mohnish 01:02:44 Not for the latest comments, because we wanted to come to this meet so that we get clarity on should we… if that is not being natively emitted by the library, should we leave it as a capture gap, or figure out some way to achieve auto-instrumentation? That was… that was the question overall.
Trask Stalnaker (Microsoft Corporation) 01:03:03 Why don't you ask it on the… just ask the same… that same question on the PR, in case Lyudmila has a chance to get to it async. Sure. Otherwise, I'm sure she'll… I imagine she'll be here next week.
Mohnish 01:03:17 Yeah, for sure. Maybe after this call, I'll add a comment there. Thank you, Trask. Yeah.
Marisa Boston 01:03:22 Then, as long as that gets resolved, then that will be the last remaining comment, and we can push this through.
Trask Stalnaker (Microsoft Corporation) 01:03:30 I can't guarantee that.
Mohnish 01:03:37 Yeah, I think, other than that, the fields were agreed on, it's more… the comments were more on the auto-instrumentation, the reference scenarios, and there were almost no comments on, the fields itself, so… I think that might be the route.
Trask Stalnaker (Microsoft Corporation) 01:03:51 That's… Okay. Yeah, sorry, I haven't been following, but yeah, Lynn Millik, could give a better answer to that question.
Mohnish 01:04:00 Sure. Thank you so much.
Aaron Abbott (Google LLC) 01:04:03 Alright, folks, we're at time. Good discussion, and good to see new people. See y'all next week.
Trask Stalnaker (Microsoft Corporation) 01:04:10 by 8…
Nida (Salesforce) 01:04:13 Thanks, guys.
