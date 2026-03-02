SIG: Sampling SIG
Date: 2025-10-23
Duration: 40 minutes
============================================================

## Zoom Recording Transcript

**Joshua MacDonald** 05:28 Hello? Good morning.
I see some familiar faces and a couple of new people here in our sampling SIG.
Hello to the familiar faces.
And, here we are, the meeting has started. I will share the usual meeting notes, and I will invite our two new guests to say hello while I do.
**Mahad Janjua** 05:57 Hello.
**Dhanya R Mathews** 05:59 Hello, I am Dania, I am from IBM Research Labs.
Good to be part of this meeting.
**Joshua MacDonald** 06:06 Great. Thank you for joining us.
Well, we meet every other week, and, sometimes there's very little to talk about. Sometimes there's an exciting topic or two.
Can you still hear me?
**Kent Quirk (he/him)** 06:21 Yes.
**Peter Findeisen** 06:21 Yes.
**Joshua MacDonald** 06:22 Yes, good. Okay, my ears are doing something. At the moment, I don't have an agenda. I do, would like to congratulate us, for publishing a blog post,
In the last two weeks.
And, oh, good, someone's making an agenda.
**Dhanya R Mathews** 06:43 Sorry, I've just added an agenda, so… and an item to the agenda. So, I'd like to get your feedback on one of those PRs that we have raised. So, whenever it's my turn, please let me know. I shall discuss the issue.
**Joshua MacDonald** 06:58 Sure, I, I,
I was just, saying we posted a blog post, I'm hoping that that is, well received. I haven't heard much about it, and there's not, been any follow-on discussion in the hotel spec SIGs, yet.
I filed issues with Go and Rust to push them using my prototypes, and that's what I have on that.
given that we've published that post, I think one of the topics I would put on the agenda, maybe, is to ask around for thoughts on priorities and next steps, if there are any, what people want to see happen, if they want to see something happen. But I'll put that in the end and let you think about it. I'm going to now open the first link here.
See what we're looking at.
Yeah.
**Dhanya R Mathews** 07:53 Mmm.
**Joshua MacDonald** 07:54 I've seen this one before.
Oh, yes, and I even put some comment on it. So I hope I was polite. Let me see what I wrote. I do remember this.
**Dhanya R Mathews** 08:07 Yeah, so I'll give a slight bit of context into this.
So, whenever an application service is deployed in production, there is a specific usage semantics associated with it, meaning there are multiple use cases.
Which is associated with this particular application service. And whenever… what we have observed with the current tail sampling processor is that even though it's capable of grouping spans by trace, it lacks an awareness of, you know, specific use case or the functionality context that each of the trace represents.
So whenever we are sampling the traces, using the tail sampling processor and the configuration options or the policies that are available, we see that some of those infrequently used use cases are missed.
So, basically, what this leads to is,
that the sampling… sample dataset may not accurately reflect the real, true distribution of application usage, or the real application usage. So what we suggest here is.
An enhancement to the sampling policies of the tail sampling processor, which actually guarantees that at least one of the trays belonging to each use case in a given sampling interval is sampled.
So this is a change that we are suggesting. So, we have done some local testing of it, and we have seen that this adds value in terms of, you know, the information retained in the sample traces. It represents a real usage more compared to a random sampling or
you know, some of those, when we are using multiple policies. That's what we see.
**Joshua MacDonald** 09:40 Right. I do remember now reviewing this, and, thank you for joining us to talk about it.
to bring the, I guess, the rest of the group up to speed here,
stratified sampling is certainly something we talk about quite a bit. Peter would be… Peter has spoken about this a lot, and I think it's one of the driving motivations for him.
In the sampling project as well. I,
Some of my feedback was to talk about this
I mean, the sort of low-level details of what you did, just… the blog post that we put out recently has sort of, like, prescribing a new way of dealing with this ash salt concept. So instead of having salt, we have consistent hemp sampling now, and that's a step forward, but I don't think it really changes what you're doing.
And I'd be glad to help you. As I mentioned, there's a support package that just does the logic for you.
However, I think you've come to a group that will… would be glad to talk about this with you, and we… but we have also spoken about the tail sampling processor here at length.
And trying to be a little bit careful in my words, we have decided it's a little bit of a,
Difficult to manage difficult to maintain.
codebase.
**Dhanya R Mathews** 11:06 I'm trying to suggest that it is…
**Joshua MacDonald** 11:09 Difficult for us to see a nice path forward with it that
brings what I think we all want to it, and I think there's lots of competing interests in it, and it's a bit of a…
A mess at this point.
So there has been some discussion about whether it can be upgraded, how it would be upgraded, whether there's political and engineering will to do so. There's also been a, like, every time this comes up, there's a question of, like, could we start over?
Should we start over? And…
Well, I… I'd like to hear if anyone else have anything to say on this topic. I mean.
at some level, when I read this PR, I also… while I love talking about certified sampling, and I think we should, whether the codebase can handle it or whether we start over.
what I saw here was a slight difference, and I…
I wanted to call it out. I think stratified
gets close to the behavior, but I also… what I… what I read from the code was you want to get at least one of any… of every category, which is…
Slightly different, I guess, in my way of thinking.
**Kent Quirk (he/him)** 12:24 So, so yeah, one of the things… questions I have for you on this, Josh, is, you're… you're asking to try to use…
the sample… The, the…
package sampling, but that's… the whole point of that is based on, kind of, trace ID and not additional information, whereas here, we're looking to establish some categories
And we want to make sure that at least one of every category is there, and that's where we're applying a hash to the category, not to the trace ID, right? Am I correct in that?
In other words, we want to say, for example, we would like to make sure that we have at least one instance of every path that hits our, you know, URL. And so…
in that sense, the trace ID-based stuff that we've already established as a standard doesn't actually have any impact on that at all. The thing we're… the categories we're trying to establish are completely independent of that, so a hash-based approach actually does make sense, right?
**Dhanya R Mathews** 13:39 Yes, that's what we're trying to build in here. So the trace ID-based categorization helps us to identify the spans belonging to a trace, and once you have the spans, you can establish those paths using the relationships in those spans.
**Kent Quirk (he/him)** 13:57 This is actually part of the reason
speaking about, this is very similar to what Honeycomb uses with our, dynamic sampling. You establish a key
Which essentially uniquely identifies the categories of your trace, some subset of fields, and those keys are then hashed, and we make sure that at least one instance of every hash comes out of our samplers.
And it was the original trying to put that into the tailbase sampler in
collector had made me go, oh my god, this stuff is a mess, and we should think about rewriting it. You know, so… so that's part of, you know, part of the conflict here is it… I still sort of feel like…
The more we put into the existing system, the harder it's going to be to get out from under it, and that these things don't compose very well.
**Joshua MacDonald** 14:54 I see what you mean.
About using the path or some sort of string-based identifiers, and that's… I think the word stratified is meaning, or has applicability in that context, too. Yes.
So that… the word is not wrong, it's just that there was a focus mainly on getting one per category that I saw.
And then I think that the hash seed stuff might still be a distraction for us. When I see a hash seed, usually it's a way to work around consistent sampling not being present. You're saying you can sample this again and again with different hash seeds, but if you use the same hash seeds, then things go badly.
We should be able to avoid the hash seed, I think, either way.
and I'm not aware of anyone really using a…
like a multi-stage tail sampler, so that would be… if there were a multi-stage tail sampler, you would perhaps want to use different hash seeds or something like that. That's the existing… there are existing collector processors that make use of such… such mechanisms.
Yeah, so I think, well, I do understand, then, the goal.
I…
I think we should be practical and say, like, I think there is an opinion, it's roughly held in this group that is to say that
I want certain things from this code, and it's really hard to get to where I want. I'm referring to getting,
consistent sampling probabilities out of the sampling logic.
**Kent Quirk (he/him)** 16:36 That's the problem with this.
**Joshua MacDonald** 16:38 That's the hard part, and we've looked at the changes that would be needed, and, you know, the structure of the code, there's several problems. It's not just that you would have to take this decision type, which is a Boolean right now, and turn it into a threshold.
It's that there's also this logic which is really difficult to understand about dropping versus the prioritization. There's, like, a no-decision mechanism, like a sampler can say, I don't care.
And then there's a prioritization where you say, I'm gonna take my drop rules first, and then I'm gonna take my normal rules, and then I'm gonna take my don't sample rules, and I'm gonna assemble them in priority order.
and get to the decision. It makes it hard to reason about the code. Very hard.
There's also some feature flags that are just tying it up, and the point is that there doesn't seem to be a lot of energy
Behind it, other than occasionally someone comes in and says, there's one more thing I want it to do, which, again, I'm being practical, I could accept this PR, but I don't have great hopes for this codebase in general.
I hope that's fair.
Yeah, thanks so.
**Dhanya R Mathews** 17:49 the comments, so in case if, like, we'd like to contribute, so if you are planning to kind of refactor the code bees or something, so…
we can still, refactor the code that we have, the PR that we have raised, and then contribute to the code base.
**Joshua MacDonald** 18:05 Yeah, I just… I'm trying to say that to be helpful, I don't want to say, this code sucks, I'm not going to accept anything, because I'm not actually the… I mean, I am becoming an owner, or I am an owner, but I don't want to block it, so I would say.
I am ready to accept, you know, I'll review it again if you'd like. I think the hash seed stuff could come out, and I think…
My point about package sampling is also sort of…
irrelevant. If, if we're not, you know, we're not doing the grand change that Kent and I have kind of hinted at to get probabilities out.
then using package sampling is not going to help you either.
So…
But I'm also, like, I'm seeing this… that… I think the hash salt stuff worries me, I'd like to see it.
move out somehow, but, I can take a look at this PR,
Again, if you'd like, and I promise to be helpful. I just can't promise that this code will ever be what this group wants it to be.
**Dhanya R Mathews** 19:09 That'll be great, thank you. So, we will also see the consistent hashing that's… that you recommended. We have gone through it, so we'll try to modify the code based on that.
**Joshua MacDonald** 19:20 Yeah, I would love… I would love, I think briefly, it might help now to explain, roughly speaking, I've spent
multiple effort sessions digging into this code, trying it, trying to figure out if it could be… well, how to get where I want it to be, for example. And,
So… I… I think,
I… I'm not sure what I was gonna say. I think, that…
there will be a way to get what you want here in, and I will… I will agree to go look at it and make more helpful remarks, more helpful suggestions. We can try and get this merged. The… the thing that I…
My dream for this code, let me just try and share it, the vision is, this is a reservoir sampler, it has a fixed amount of memory. It does not run out of memory. It adjusts its sampling thresholds before it does.
It has intervals of time that it samples independently.
And the intervals of time are somehow related to that decision window. So you will wait for 10 seconds, and then you will do some decision making.
there's a fixed amount of space available for each window, and if more traces arrive during that window, I'm going to adjust my threshold.
In the correct way, so that each interval independently keeps a reservoir sample.
I want to make sure we don't run out of space.
I also want to make sure we're counting correctly. So… so that's…
one sort of leg of the platform. All the decisions should be threshold-based, and that means that if we're going to say a sampling decision, it will be 100%, it'll be 50%, it'll be some threshold value within the range of 56 bits. That's the intended
Acceptance threshold.
Every decision policy in this codebase will then have to participate, and most of them are straightforward. We know how to AND, and we know how to OR with these thresholds. We know how to make a probabilistic decision with the thresholds.
all the other behaviors are sort of assemblies of those core… those… those core features. So then,
Then the goal would be that all of the sampling policies Participate in a threshold-based decision.
And…
they adjust for lock of space by thresholding as well, so that it acts like a reservoir sampler.
Those are two huge changes, and I could see doing it incrementally, I really could, but it's… but the duration and the number of changes, it would be terrible. So, I can see it, but it's, like, just barely.
It's tough. It's tough to see.
And… and for me, the thing about priorities and the precedence of drop versus don't sample and do sample, that makes it just really hard to reason about. I would try and get rid of that first.
So that's… that's just sort of the feeling I have.
That's, mixed news for me to deliver.
So, that said, I will be glad to try and help you with your PR.
**Dhanya R Mathews** 22:45 Oh, thank you.
**Joshua MacDonald** 22:46 Because there's nothing…
like, get… if we accept what we have and where it is today, this is a nice step forward. It's just that I want to go all the way back to the beginning and take different steps.
**Kent Quirk (he/him)** 22:58 Yeah. The biggest issue here is going to be that this will further complicate the problem of being able to pass through the threshold and aggregate it, because a sampler like this needs to decorate each individual sampled trace with a different threshold.
And so that's… that just adds complexity to this problem.
**Dhanya R Mathews** 23:23 It's not…
**Joshua MacDonald** 23:24 It's solvable, right?
**Kent Quirk (he/him)** 23:25 It just… it adds up an additional layer to the thing you're trying to refactor.
**Joshua MacDonald** 23:31 Yeah.
Agree.
I will also add that I did… I came into this topic not just from my sampling interest, which has been a long… around for a while, I also was working in the collector
And I… some of the guys here have heard this already, but I'll say it again so that we can widen the circle. I was working in the collector, and one of the big, I guess, missing features in the collector is a sort of apparatus for
limiting, whether it's memory limiting or rate limiting. And I picked up some sort of, like, loose ends and started working on the problem space, and did a bunch of research on how
sort of proxy-like forwarders do this type of thing. So, rate limiting or memory limiting in a pipeline, essentially. I found Envoy was a pretty strong example. Users who operate Envoy know how to configure its rate limits and so on.
And… and then I found myself wanting to compare and contrast the configuration model and rate-limiting setup model for, say, Envoy versus the collector with configuration for rate… for rate-limiting
Traces, and once you get to the sampling, the tail sampling problem.
what you… what you see here is all of this work is trying to rate limit to lower the cost of traces while still preserving the few things you want. So then, going back to the rate-limiting question in Envoy as my research project here, like, I wanted to see, like, how are people configuring resource limits in a way that are stratified similar to what you're
you're doing, but in a more kind of explicit configuration sense. Like, I want to give this tenant more traces, I want to give that tenant less traces, and that somehow enters into tail sampling configuration as well. And we do see a composite sampler rule in this code.
And you could imagine trying to compose it with your stratified sampler in this code, and then the composite's gonna say, well, I'm in my high priority tenant, I'm going to that sampler configuration, or I'm in my low priority tenant, I'm going to this sampler configuration.
That's another dimension along which this code is
not quite as sophisticated as the, I guess the state of the art for other types of servers in its category.
So, being able to configure
rule sets for sampling that are, that have key and value, like distinctions, predicates that direct you to one configuration or another. That's probably what users are gonna ask for next, if they don't have it yet.
It's not clear that people are using the composite sampler configuration of this code, and…
the point is, some people like it, it's working. We'll get… we can do what you're doing, but I think,
probably it will never do the thing that Kent imagines, or that I imagine, which is that after we sample these traces, we have thresholds on them that tell us, this trace happened about 100,000 times, this trace happened about 10 times, this trace happened about 10 million times, or whatever. Those are the types of things that we want to be able to accurately estimate.
I hope I haven't shredded this too much. The concept is good. I love the idea of one per category. That's always been a hit for me with sampling.
**Dhanya R Mathews** 26:53 Oh, Joshua, I've taken all your comments, we'll work towards… I'll try to modify this code to use consistent hashing, then we'll seek your opinions on the revised code.
**Joshua MacDonald** 27:05 Great. I'd be glad to help. I'm on Slack, and this is a topic that does interest me, so I appreciate your patience with the feedback.
**Dhanya R Mathews** 27:14 Thank you.
**Joshua MacDonald** 27:15 Alright, when we've done that one, and I will commit to time on that later, in the coming weeks.
Okay, this is gonna be an interesting one. This is even better. Where are we? We're back in the specification now.
And I suppose the Mahad, this is your topic.
**Mahad Janjua** 27:33 Yep.
Hi.
**Joshua MacDonald** 27:35 I'd love to hear you describe it.
**Mahad Janjua** 27:38 Yeah, so, I'm working at AWS right now, and we have our AWS version of the OTEL instrumentation, for which we use this always record sampler, and essentially this is just a way which
I… from what I've seen, to access the record version of the sampling flag. I don't think that there's any way, to do that built into or available to users of OTEL right now.
And this is just the first step to allow people to basically process all spans, in a consistent way, vended by OTEL directly. We already have the code in 4 languages, and maybe more that we support.
So, it's very simple. The point of the code just being.
Now that we have a sampling decision made by some delegate sampler, let's wrap any drop decisions with record and drop.
Just to…
have every single span, at least recorded, so that we don't… we can process all of them. And that's sort of just the very basic idea.
Yeah.
**Joshua MacDonald** 28:47 Remind me, is record and drop not real yet? That's, like, something you've made up.
**Mahad Janjua** 28:54 It might be… drop-in record or something like that, but it's, it's definitely…
**Joshua MacDonald** 28:58 Okay, I know there's a… I thought there was a record only, or drop, or record, or sample and record. This is a good question.
I recall there being.
**Peter Findeisen** 29:07 I believe… I believe the intention is to use record only, it's just a different name.
**Joshua MacDonald** 29:13 I… okay, okay.
**Mahad Janjua** 29:14 Oh, yeah.
**Joshua MacDonald** 29:15 only.
**Mahad Janjua** 29:16 Yeah, good. That's what I meant. Yeah, sorry.
**Joshua MacDonald** 29:18 I see, I see, I see. Good. So, then the feature request is,
To create a sampler that
As a delegate, and just replaces drop with record only, or what… record and drop.
**Mahad Janjua** 29:35 Yeah, exactly.
**Joshua MacDonald** 29:42 I'm… that sounds very reasonable.
And you're saying that you're using this to generate, I would guess, metrics from spans?
**Mahad Janjua** 29:52 Exactly, yeah. It's pretty…
**Joshua MacDonald** 29:54 liquid is.
**Mahad Janjua** 29:55 all of our instrumentations. We basically wrap every sampling decision with this sampler.
**Joshua MacDonald** 30:05 Good, and that's, I take it that's because you like your span instrumentation and you want metrics.
**Mahad Janjua** 30:12 Yeah, exactly.
**Joshua MacDonald** 30:14 Okay. Well, it seems like a fairly, this is an issue, right? So, this seems like a…
Pretty easy one, to be honest. I'm not sure what people are gonna say. Let's see what…
And I will be at the next SIG meeting if you want me to be here. We can talk about this together, let's see.
This, to me, is a pretty reasonable request, and it's very small, so I would… I would support it, probably. I can't think of any reason not to at the moment.
If I may bring up a…
**Kent Quirk (he/him)** 30:52 Can I ask for a piece of clarification here?
**Joshua MacDonald** 30:54 Please.
**Kent Quirk (he/him)** 30:55 When it's… who's doing the dropping?
You know, like, there's… the recording is happening, but where… at what point does something say, okay, this was… now it's all… now we're actually done, and now we can actually drop this?
**Mahad Janjua** 31:14 I don't think I have an answer for that right now.
I…
**Joshua MacDonald** 31:19 was that the sampler that does this decorating will return the record-only decision, and then when it
gets to processing, it will see
It will somehow decide whether the thing was sampled. Well, the flag will say whether it was sampled or not, and then it will drop things from export.
Before they…
**Kent Quirk (he/him)** 31:42 So, in other words, the application… the sampler that's marking this for the tracer is marking at record and drop, but it's the exporter at the application level. It's not like we're expecting the collector downstream to drop it.
It's still being dropped before it leaves the application, but within the application, it's retained.
**Joshua MacDonald** 32:07 I wanted to bring… this is… there's a history of issues connected here, and I wanted to bring up some of them.
Oh, look, I'm assigned it. So…
and I think this may not even be the only one of these issues. Span stats, processor… anyway,
And this is 2 years old, at least, at this point, so keep in mind it's hard to read these things. And there's…
But this is one of the issues connected to, I would say.
you know, we were… I just, at the top of the meeting here, said we published our milestones blog post, we've done quite a bit on threshold and randomness and stuff, and basic
specs. If you ask me what's left, what's next in OpenTelemetry sampling, I mean, there's a lot of things, but this one here comes up again and again, that there's no way for an SDK to say, you know what, I know what I'm doing. I want to record all these spans, and I actually want to export them, even though these traces are not sampled.
Because I know what I'm doing, and I know that I can record those spans, write them to a stream of pipeline, and then at the end of the pipeline, I can do the same thing. I can calculate those metrics.
So that having a span that was untraced is actually pretty useful, and it does the same type of…
I mean, there's an efficiency argument for, like, not sending all those spans and doing the metrics in the SDK, but there's also a complexity argument for just recording the spans and having the metrics computed downstream, even when you're not part of a trace.
So that's why this issue has been discussed.
I know that there's another issue lurking with the same topic somewhere, because I've seen this come up in multiple repositories. I just want to export spans, they're not traced.
So I feel like that's one of the big things that we lack.
And, your issue hints at.
Have you given any thought in this same setting to whether…
I mean, here, anybody, open question, would you like to see spans?
that are…
being exported for reasons, even though they're not traced. I have a bunch of reasons, but I'm asking you guys.
**Kent Quirk (he/him)** 34:17 I'm pretty sure the use case you just described is actually relatively common.
**Joshua MacDonald** 34:24 For me, the one that we know about is, like, I'm an ingress node, I'm receiving data from an upstream, and I'm sending it to a downstream, and
My…
And we want to drive network metrics, and I'm the one person who knows my peers. I know my upstream peer, and I know my downstream peer.
I want to have,
a complete network, like, information be recorded by that node, and my spans actually have the perfect information. If I record 100% of spans.
with the network peer attributes on them, then I can go derive metrics with all the peers, and I can do a, you know, like a dependency graph of network metrics.
But it requires being able to store spans that weren't traced, and OTEL gives us no way to store spans that weren't traced.
I think we could solve it. I mean, I think we could specify it. In the first version of OTEL's protocol, there was no span flags in the span data.
That gave it… that made it really hard to say this span was not sampled.
But we did add that field years ago, and now there's a span fa- trace flags
Field in the span, which means that
We can see that the span was not sampled.
And that means I should be able to send it to a collection pipeline. These spans weren't sampled, but they have useful histogram information, they have useful network attributes, etc.
Or you're computing an SLO. Those are all things I've seen people do with spans that were not traced.
But there's no hotel spec.
**Mahad Janjua** 36:02 Is there, sort of a gap between the proposal that I linked and what you're describing? It seems like
to me.
**Joshua MacDonald** 36:12 They're… they're connected, they're not… they're not really… they don't have to be dependent on each other.
Be accepting your change without any more conversation, actually.
**Mahad Janjua** 36:20 Right.
**Joshua MacDonald** 36:21 I just wanted you to be aware of the larger issue that keeps coming up.
**Mahad Janjua** 36:26 Of course. Yeah, that makes a lot of sense, thank you.
what we get from this proposal to taking action, right? I'm not familiar with the process, so…
**Joshua MacDonald** 36:37 Yeah, yeah, you've actually done great. I see that you filed an issue, you made a draft PR…
This… is…
it's really nice to see a very small change. I think this is a perfect pitch for the spec SIG, because you want all the maintainers to look at this. I'm obviously enthusiastic about it, but the maintainers are the ones that are going to see, like.
what, from their perspective, might be… might… might go wrong. I feel like, let's see, what's… the first question someone's gonna have is what Kent already asked me. Who does the dropping, and how does the exporter know that it's supposed to do the dropping? We might want to add a sentence or two here saying, this processor… this sampler will…
How does the processor know to drop it before the exporter gets it? That's really the question.
**Mahad Janjua** 37:26 Okay, let me note that down for later.
**Joshua MacDonald** 37:30 Yeah, maybe look into your implementations and see how they do it, like, because…
**Peter Findeisen** 37:36 So, it looks like span exporters will simply drop those spans which do not have record and sample.
**Joshua MacDonald** 37:48 Does… does the exporter see those spans with… Without recording sound?
**Peter Findeisen** 37:53 Yes, they will… I think they will reach the exporter, because the exporter is really a processor, so it is…
registered as a processor. It does exporting, but it has processor interface.
So it will see all spans that haven't been dropped.
But it will export on the…
that are recorded as samples. I believe this is how it… I… it's been some time since I looked at it, but this is how I remember things.
**Joshua MacDonald** 38:28 That sounds right, and I can believe it. So I would just go verify that, in your understanding, the SDK exporter already drops spans of this nature. We just don't have a sampler that can decorate this way.
**Mahad Janjua** 38:41 Yeah.
**Joshua MacDonald** 38:42 So, it's a pretty easy change, I would say.
**Mahad Janjua** 38:44 Yeah, so the recommendation at this point is to, you know, get the answers to those questions and go attend the SPECSIG.
**Joshua MacDonald** 38:53 Yeah, well, okay, I can offer to present this for you if you'd like. If you don't feel comfortable at the Spec SIG, it's pretty easy, and I would be glad to sponsor it. Just, you know, I could spend 2 minutes explaining it and ask for feedback. If you show up, I imagine it will get a little more attention, maybe. It's nice to see people show up and talk about their own work. Either or.
**Mahad Janjua** 39:13 Yeah, I can probably handle it myself, but, you know, if you show up to support…
**Joshua MacDonald** 39:20 So, what I recommend is, if you put it on the agenda.
which is in the notes, for the weekly meeting, and don't feel like showing up. Just say, sampling topic, please review. I'll be in the meeting, and I'll pick it up, and I'll know that I can talk about sampling topics in that meeting.
**Mahad Janjua** 39:37 Great, that would be…
**Joshua MacDonald** 39:38 Glad to help.
**Mahad Janjua** 39:39 Thank you. Yeah.
I appreciate all the…
**Joshua MacDonald** 39:43 You came here to talk about it, so yeah, I'd be glad to. If you put it in the spec notes, I'll take it from there and get, help.
**Mahad Janjua** 39:49 Yeah, I'll definitely be putting it in the notes, and be attending the meeting as well, just to, of course, know where it goes, if… yeah, and hopefully I'll contribute to the talking a bit about it. Thank you.
**Joshua MacDonald** 40:01 Appreciate that.
Cool. Well, we're back in the notes.
Josh will help, we can do this.
We can… Josh will help review… this PR.
And then I'll add here, Josh… We'll support InspectSec.
I'm glad to do all these things, everybody.
I think we've reached the end of a meeting.
Donya, I will be glad on Slack to discuss this more, if you'd like, and everybody else, thank you for being here. I guess I'll see you in a couple weeks.
**Dhanya R Mathews** 40:42 Thank you.
**Joshua MacDonald** 40:43 Cheers.
**Peter Findeisen** 40:43 Thank you.
Like…
