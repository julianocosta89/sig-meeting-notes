SIG: GenAI Semantic Conventions and Instrumentation Stability
Date: 2026-11-06
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 00:26 Hi, everyone!
**Max Ind (Google LLC)** 00:28 Hello.
**Trask Stalnaker (Microsoft Corporation)** 00:31 Hey!
**Liudmila Molkova** 00:38 You can share.
Oh, this is… Not Wednesday. Happy Friday!
**Max Ind (Google LLC)** 00:48 You frame me.
**Liudmila Molkova** 01:06 I think, Max, we have your PR…
**Max Ind (Google LLC)** 01:13 That's… fix the 89, I think.
**Liudmila Molkova** 01:32 this friend… Just looking… What we need to talk about today.
Nothing waiting for maintainers… Geometrics is not stabilization.
This seems like something related to stabilized stuff, this is on the agenda.
Not stabilization… Should be on the agenda already.
Not stabilization… No.
Put on the agenda… This is probably something related to stabilization… Features… Okay, seems to have… Everything.
Not sure if we… We'll have time or chance to talk about this.
by 40… Somewhere here… This is a new one.
Anyway… Okay… Cool. So then… Let's get started! If you want to discuss something that's not here, slash add.
And since we have Max here… Let's talk about this friend. I think I almost approved with some… Oh, the naming.
Sorry, I didn't have a chance to read.
**Max Ind (Google LLC)** 04:29 No, no worries, I kinda procrastinate at it.
Till, like, 15 minutes ago.
**Trask Stalnaker (Microsoft Corporation)** 04:36 So… How, what's the plan for… Knowing if it's nested or not.
**Max Ind (Google LLC)** 04:46 And… a context key, I think, shared in, like, a… And they… Library that each, instrumentation Can depend on.
**Trask Stalnaker (Microsoft Corporation)** 05:07 Do we have any… Examples of this, before, where… Because the OpenTelemetry context key is opaque.
And can't really be shared.
Like, by name across… Libraries… Like, that would force… Native instrumentations to depend on our… library… Or is Python different? Ludmila, is it not opaque? Is our context keys readable in… by name in Python.
**Liudmila Molkova** 05:52 Erin and Dylan would know better. I think they are, right?
**Aaron Abbott (Google LLC)** 05:55 They're… they're opaque.
**Liudmila Molkova** 05:57 Oh, they're a pack?
**Aaron Abbott (Google LLC)** 05:59 Yeah.
**Liudmila Molkova** 06:00 even if they are, like, it's… it's an optional dependency, right? So, in Java Trask, you know, we've done hacks and Azure SDKs with reflection.
And it's… Doable, but it's also doable with optional dependency, depending on the language or reflection.
**Trask Stalnaker (Microsoft Corporation)** 06:21 Right, but it would require native instrumentations to depend on Our… some other… some shared package that we have.
**Liudmila Molkova** 06:34 Optionally.
Or visual reflection?
See you.
**Trask Stalnaker (Microsoft Corporation)** 06:39 Alright.
**Liudmila Molkova** 06:39 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 06:41 But there… oh, go ahead.
**Aaron Abbott (Google LLC)** 06:43 Sorry, I was gonna say, we do have this for, like, the HTTP suppression, but, yeah, we could expose it At a well-known place, and then you can just do, like, a try-catch import.
Python.
**Liudmila Molkova** 06:57 Yeah, so, like, essentially, in Python, all the libraries depend on OpenTelemetry instruments, Instrumentation package, which has the… Like, think about it as Instrumentation API, but without steroids.
**Trask Stalnaker (Microsoft Corporation)** 07:17 So this is, in the Python contrib repo, or the GenAI utils shared?
**Liudmila Molkova** 07:26 That one is in Python Contrib.
**Trask Stalnaker (Microsoft Corporation)** 07:28 Okay, but this one would be in the GenAI… Shared utils.
**Liudmila Molkova** 07:36 Yeah…
**Dylan Russell** 07:39 For what? Just the context key?
**Trask Stalnaker (Microsoft Corporation)** 07:45 Yeah, because you can't look up context keys by a string.
**Max Ind (Google LLC)** 07:52 Yep. Why is that? Because in Python, I thought that it's like a design… That it's, like, opaque by design.
**Trask Stalnaker (Microsoft Corporation)** 08:02 There's specification language.
**Max Ind (Google LLC)** 08:04 Okay, okay.
**Trask Stalnaker (Microsoft Corporation)** 08:05 about that.
I forget the reasoning.
**Aaron Abbott (Google LLC)** 08:11 I think it's intended to prevent collisions.
**Liudmila Molkova** 08:17 It's intended to make life miserable, but okay.
**Aaron Abbott (Google LLC)** 08:22 Yeah, so this is what we expose for, setting this context key for suppressing HTTP Instrumentation, which we do for, like, exporters and such.
So we could throw it in here, and then people don't need a hard dependency necessarily, they can do, like, a Like, a try import, and… Just fall back if it doesn't work.
**Trask Stalnaker (Microsoft Corporation)** 08:47 Okay, and so other languages would have to do the same thing, essentially.
in order to support is nested.
**Liudmila Molkova** 08:59 To support is nested main agent propagation conversation ID propagation. We have the whole story for this.
**Trask Stalnaker (Microsoft Corporation)** 09:09 So, will that… will this… because I was assuming the main agent, those other propagation things would be solved eventually by, context-scoped keys?
**Liudmila Molkova** 09:22 The outer instrumentation would… Put the context Sculpt attribute.
on the… When, when it's starting.
The isNested could also be that you put the isNested on the context scoped key attribute.
**Trask Stalnaker (Microsoft Corporation)** 09:44 Yeah, and then you just don't stamp it.
If it's false…
**Liudmila Molkova** 09:49 You don't stamp it if it's false, yeah. Or you can stamp it if it's false. It's actually… I don't know if, Max, you want to have a discussion about this. I would prefer not to stamp it, but it doesn't matter.
**Max Ind (Google LLC)** 10:01 Yeah, I think I… I don't have a horse in the race, I think it mostly is, like, the people who have to query the… The metrics… that I think that, like, if… Some query language, like, languages, like, they make it difficult to… see if, like, an attribute is missing? I'm not… fully sure.
**Liudmila Molkova** 10:28 Hmm.
Yeah, maybe let's talk about this, but I think Trask how… Do you want to move on? Are you ready? Do you think we should talk more about the context part?
**Trask Stalnaker (Microsoft Corporation)** 10:49 Yeah, let's move on. Yeah.
I think, I mean, there's… there's a couple options. We don't have to… prescribe. I was just… Trying to think if there was… if we had done anything… if this was sort of the first case of this that we've had in semantic conventions.
And… I mean, the main agent stuff.
I feel is a little different, because it's, like, it's this idea of just denormalizing, stamping the same attribute On down the chain.
And so this is… Slightly different.
**Liudmila Molkova** 11:33 Right, because you don't want to stamp it on everything just on the spans of the same type.
Like, we wouldn't want to stamp it on.
**Trask Stalnaker (Microsoft Corporation)** 11:44 Right.
Right, like, yeah, it's a little bit of a different purpose than the others, which is… Just to save joining… So the next thing maybe we can… Discuss is how, Because there was some thought that maybe main agent… Would be the indicator that it was… not nested.
**Liudmila Molkova** 12:19 The lack of main agent would be the indication it's not nested.
The lack of this pen.
Or a metric attribute, precisely.
And it can be… it's just… it feels very subtle.
**Trask Stalnaker (Microsoft Corporation)** 12:38 Yeah.
**Liudmila Molkova** 12:38 Very nice.
**Trask Stalnaker (Microsoft Corporation)** 12:39 We want to stamp… well, and we want to stamp main agent down the chain. It does apply.
It just… you would have to see if it's not equal. Equal to the agent name is equal to main agent name, or something.
**Liudmila Molkova** 12:52 Right, or we require not to stamp it on the main agent.
Lear.
**Trask Stalnaker (Microsoft Corporation)** 12:58 Oh, right, right, right.
**Liudmila Molkova** 12:59 That's… I don't know if I can guarantee, like, it will be very difficult to achieve.
**Trask Stalnaker (Microsoft Corporation)** 13:07 Yeah, and so this is yet another example. The pure motivation here, Max, is just to make query time easier.
**Max Ind (Google LLC)** 13:16 Yeah, it's to make it possible to know the end-to-end duration of an Agentic system.
**Trask Stalnaker (Microsoft Corporation)** 13:24 Without having to do joints.
**Liudmila Molkova** 13:28 on metrics.
**Max Ind (Google LLC)** 13:29 Oh.
**Trask Stalnaker (Microsoft Corporation)** 13:30 Oh, on metrics.
**Aaron Abbott (Google LLC)** 13:35 How could you solve it with the metric join?
**Liudmila Molkova** 13:40 you would need to know the agent name. So, like, imagine we… we make a dashboard for arbitrary Agentic system. We need to know who is the outermost, somehow.
**Aaron Abbott (Google LLC)** 13:52 I… okay, I gotcha, yeah.
**Trask Stalnaker (Microsoft Corporation)** 13:57 I see, so metric… for metrics, so targeted more at metrics, hand… for… invoke… Agent, operation, duration, Since… There's gonna be a breakout of different… agents and nested agents in there. We're gonna have that overlap stuff.
And we don't want to suppress The way that we kind of do in other semantic conventions.
Okay.
Makes sense to me. Thank you.
**Liudmila Molkova** 14:35 Yeah, this is why it's important for stabilization, because it's a metric attribute, the most important part of it.
**Trask Stalnaker (Microsoft Corporation)** 14:42 Right.
Yeah, is that sort of… is that case already made? Should we make it in… like, the non-normative doc. I feel like we added something for the… stamping conversation ID down.
like, that… There's… just because it's a little, like, where I… we're building in… Well, I guess maybe not. For the metrics, it's not redundant.
Yeah, is what you're saying, and that makes sense to me.
Okay, I'm all caught up. Thank you.
**Liudmila Molkova** 15:24 Yeah, thanks.
So the naming, the hardest problem of the humanity.
I think it's not a request, right? It's… it's not… there is no request in the Agentic… In vocation.
**Max Ind (Google LLC)** 15:41 True. That's true. I have seen other… Attributes named similarly.
Indeed… internal agent.
I hope it's in the internal agent. I hope I haven't… My mistake.
**Liudmila Molkova** 15:54 Yeah.
**Max Ind (Google LLC)** 15:55 Looked at the client.
**Liudmila Molkova** 15:58 Oh, you're opening a can of worms. Should we rename the GenAI.request friends?
To be precise, or… to be broader than just the inference.
I'm actually thinking… Maybe I'll create an issue.
But the internal invoke agent has a bunch of attributes that it might not need to have.
it… they don't work well. The response finish reasons is one.
Half of the instrumentation is not populated.
We probably need to do something about the… Mmm… talking counts.
Maybe we keep some of them.
But I, I think the request is… Zip is… for… specifically for this attribute is wrong.
**Max Ind (Google LLC)** 16:59 That makes sense.
Yeah, I was wondering, yeah, there are request attributes on the internal agent span.
But I… it felt, as if it's, like, some… Yeah, something that hasn't landed there recently, or, like, landed by mistake, or… Or… whatever else.
Yeah, the alternative is the… is the agent.internal.
That is nested.
**Liudmila Molkova** 17:45 Oh, sorry.
So this is… this would be your preference.
**Max Ind (Google LLC)** 17:50 Yeah, I think, I think if… Yeah, basically… Yeah, this seems like a fair, you know.
I like a fine name, because it, like, matches the span type.
**Trask Stalnaker (Microsoft Corporation)** 18:10 Matches the span type.
Oh, the namespace?
**Max Ind (Google LLC)** 18:22 The namespace of the metric as, as well, yes.
So the metric is search GenAI invoke agent, and this is… the attribute is agent.invocation.
**Liudmila Molkova** 18:38 this would be the spent type of plant, right?
This is the one that… We are entertaining, and the current one is GenieI DOT in Europe.
mentioned.
so if we want to match this… Where… Would put underscore here.
And we put that everywhere.
**Max Ind (Google LLC)** 19:29 The… the underscore versus that is… It's like a… it's, like, easy to shoot yourself in the foot, because it's, like.
Sometimes you put a dot, sometimes you put an underscore. And, like, agent.invocation… There, at least is currently an agent.name attribute.
Yeah.
**Liudmila Molkova** 20:18 That's why I was proposing this.
To avoid this conversation.
**Max Ind (Google LLC)** 20:28 Yeah, I went with the dot invocation because I think the… there's kind of, like, a WR file distinction that, like.
the… GenAI.agent.
no invocation, it's kind of like a parameter of an agent that's just, like, static. So, like, a name doesn't have anything to do with a given invocation.
It has to do with the agent.
**Liudmila Molkova** 20:54 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 20:57 If we want to… if we want to switch gears and argue about other naming Things, I have two other… Aspects of this name to bring up.
**Liudmila Molkova** 21:09 Okay, break down, break it down.
**Trask Stalnaker (Microsoft Corporation)** 21:11 The easy one is probably, is. I don't think we typically prefix with is.
**Liudmila Molkova** 21:17 Oh, right.
**Trask Stalnaker (Microsoft Corporation)** 21:19 The harder one is, Whether it should be flipped, and it should be… top level, like… Instead of… for the true value, meaning if we don't report… if we want false to be the same as not reporting it.
it feels… Well, I don't know. I'm trying to decide whether, like… because if there's nothing there.
Then, you don't know if the instrumentation is capturing it, or not.
Which is possibly an argument for capturing false even when it's… Instead of leaving it.
The other is, like.
if we don't do that, then I figure the one you'd see we care about mostly are the top-level ones, right? And so what's your query going to be?
Your query's gonna be where… Is nested flag is not present.
Like, it's a little… feels like a little… feels easier to query where, you know, Top level equal true.
**Max Ind (Google LLC)** 22:40 Yeah, and then it seems kind of also easier to… I think implement, because the… You have to… you only… although I'm not sure, because, like, right now.
My worry is that, like, you have… One part of the framework that is… Setting this nested.
and then another part is not setting it, and now you can differentiate which one is actually the root. Whereas if it's the… you mark the root just once, then you can have, like, one framework that is Pretty confident, maybe?
And then it just sets it, and then another framework which is not confident that it can set it.
Reliably doesn't set it, and it doesn't mess anything else up.
Yeah, but I haven't thought about it.
Too long, so…
**Liudmila Molkova** 23:41 I think, my motivation for the Nested was that You never reliably know that you are root, because we are relying on the context propagation, and it's in process.
And it's between the native instrumentations and non-native Instrumentations, it's a little bit difficult, but… We can only know that when something is nested.
But I can see the argument where we say, okay, if you… Participate in this.
Nesting logic, in Instrumentation supports it.
You can set yourself as a root whenever you don't detect.
You are.
**Trask Stalnaker (Microsoft Corporation)** 24:37 Yeah, I think you're gonna end up in the same place, same problem, either way, where users are gonna have to write… or, I mean.
If it isNested, they would end up writing queries for… is nested… Being false, or not present, or whatever, which could be… incorrect.
**Liudmila Molkova** 25:01 Alright.
**Trask Stalnaker (Microsoft Corporation)** 25:01 Also, if other things don't participate, I do agree that the… Isnested true is more honest.
More… probably more accurate, the way that you're… describing it.
Bye.
don't… so I think it's kind of a… but I think the usability is maybe easier with the other.
**Liudmila Molkova** 25:30 Yeah, it's much easier.
Max, how you feel about switching to root or some other…
**Max Ind (Google LLC)** 25:38 I'm gonna sleep on it, because I wanna actually draw, like, a… Like, a table with, like, possible, you know, failure cases and what is, like, which one is better?
**Liudmila Molkova** 25:55 Okay, awesome.
And then… We can… think about this. I think… Neither one can work.
Okay, so we… We have the next steps here.
Let's move on to the next topics. I think Erin has to drop, and it's unfortunate.
I wanted to chat about, JSON fields. We'll take it offline then.
So, I left a comment on Felix's PR, like, one minute before this meeting.
I'm sorry, Felix, Oh my gosh, my… my AI did a bad thing. I'm sorry.
**Trask Stalnaker (Microsoft Corporation)** 27:01 It happens to us all.
**Liudmila Molkova** 27:03 Yeah, so this… this is the human author to comment, the rest is… I have no idea.
I was just making suggestions on how to, Explain better that the value is the… Is either the whole result, or… only the data returned along the parts, but, we'll see what Felix replies. I don't think we need to talk about it right now.
I'll drop my… Roger, yeah, comments.
So we probably shouldn't discuss it now, because nobody knows what is it about, at least I think, on this call.
Let's see what this tour… Or…
**Mikolaj Knap (Google LLC)** 28:05 Oh, yes, I think that's me.
Yeah, so I brought up an issue for attributing token metrics to agents, and I wanted to look into it. I wanted to ask, before I even start up, opening up a PR, since we added the metrics in the PR, 4… 374… thinking about it, there's two kind of main options if we want to be able to group by agent.
we wanted, option A would be adding the main agent.
Name on the inference level.
counters for tokens. That'll be probably the easiest, and you can just sum up by the agent name.
And then, I think the other option I looked into would be adding two new sets of metrics on the invoke agent level. One for the direct tokens used by an agent, and the one for the inclusive. So, like, the agent, and then all its nested tokens of the sub-agents.
**Liudmila Molkova** 29:13 Oh…
**Mikolaj Knap (Google LLC)** 29:14 Yes, that would be more metrics. The question is which… which… Approach would be more likely to be a good approach.
**Liudmila Molkova** 29:26 I think it's both. So for, like, the breakdown things, like the cache and… all the counters that permodality thinks. Adding agent name to them, and main agent name, both, right? My immediate agent and my… main agent.
Would make sense, and then you can break down the details by Either of the edges.
But then…
**Mikolaj Knap (Google LLC)** 29:58 That's a good point, but the cardinality, is that not an issue, or no?
**Liudmila Molkova** 30:03 How many agents do we expect?
**Max Ind (Google LLC)** 30:09 Well, as always, if you're, like, Google-sized, you have… you have many agents, but if you're, like, smaller, then it's probably an issue.
**Liudmila Molkova** 30:20 I mean, within one tenant.
That's probably a reasonable amount. Plus, we should make it configurable, like this main agent propagation, or just the propagation. Maybe it should be, like, opt-outable. You can disable it.
**Max Ind (Google LLC)** 30:36 Yeah, yeah, yeah.
**Mikolaj Knap (Google LLC)** 30:39 I mean, you could disable the propagation of…
**Liudmila Molkova** 30:43 the main agent.
Or propagation across instrumentation layers.
**Mikolaj Knap (Google LLC)** 30:52 Interesting, I didn't know that.
Take a look.
**Max Ind (Google LLC)** 30:55 I, like, because me and Miko, I discussed this prior a bit.
**Liudmila Molkova** 31:01 Huh.
**Max Ind (Google LLC)** 31:02 And the main agent and the normal agent, kinda… means that you can't… you can't look up the total tokens of, like, a subtree. So if you have, like, a… an agent, and then a nested sub-agent, that works perfectly, you can know everything. But if you have… Triple nesting.
Then you can't have the total tokens on the middle agent.
**Liudmila Molkova** 31:29 Yeah, so, like, you still probably want histogram per… Agent invocation.
Right, so the breakdown for, like, cache and permodality is on inference, because this is where the difference exists.
But, like… The total spent for input and output for individual legends distribution is still… Not covered, and it's interesting.
**Mikolaj Knap (Google LLC)** 32:01 Okay, so for the permodality and for the cache, we could stamp the agent name and the main agent name on the inference-level metrics.
And then for the total input-output tokens, for nested Subagents weekly.
Still have to think about it a little bit.
**Liudmila Molkova** 32:19 Before, for all agents, right?
Yeah, Max?
**Max Ind (Google LLC)** 32:24 Yeah, I'm curious why not have cache tokens per a… on, like, the invoke agent level as well?
**Liudmila Molkova** 32:34 Because you get it by clearing… token, the cash by… with the Sergeant name.
**Max Ind (Google LLC)** 32:45 Yeah, yeah, yeah.
I mean, you, you would have, like, you would have on the inference, And… this gets into, like, another issue, but, like, on the inference, you have cache hit for a model level, but I think the cache behavior is largely determined by how your agent is implemented, because, like, if your agent, you know… Manipulates the prompt in such a way that it puts something in the front, And then busts the cache.
That's the… you know, you… you can… You can determine by the agent name that the cache was… is, like, not great for this particular agent.
Whereas, like, an inference API, it, like, whether a cache hit… Whether a cache is hit or not, it depends on, like.
Mostly what's going on the layer above.
**Liudmila Molkova** 33:49 So… when you're… Okay, where I'm coming from. So you only get cache information from inference layer?
That's true.
**Max Ind (Google LLC)** 34:01 for you.
**Liudmila Molkova** 34:02 And when… Probably, you cannot You only care about the calls made by This agent.
When you talk about cash.
So, like, it's… you don't care about… well, you may care, but probably less of what sub-agents did was their cache usage.
**Max Ind (Google LLC)** 34:30 That's true, that's true, that's… that's a good point, yeah.
**Liudmila Molkova** 34:35 Yeah, maybe you just… you can get almost everything you need by… the existing confronts.
**Max Ind (Google LLC)** 34:47 But then… then main agent on the cache metrics probably… Doesn't net you anything?
**Liudmila Molkova** 35:04 Yeah, but I'm thinking if we are propagating main agent, we are propagating it to all the metrics, and… Spreads.
**Mikolaj Knap (Google LLC)** 35:12 Could probably be useful, because then you could query… How many tokens may an agent uses total, which are cached?
Right? So it's probably useful for calculating cost.
**Liudmila Molkova** 35:27 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 35:29 I'm a fan of… Push main agent all the way down onto everything.
At least, at the very least, has an opt-in mechanism.
**Mikolaj Knap (Google LLC)** 35:39 Okay, with a… with agent name as well.
Or just me an agent?
**Liudmila Molkova** 35:47 I think we should have both.
**Mikolaj Knap (Google LLC)** 35:50 Yeah.
**Liudmila Molkova** 35:51 We… if we can.
Well, there are people who won the whole tree of agents, I heard. Stone everywhere. Maybe it's too much.
**Trask Stalnaker (Microsoft Corporation)** 36:01 the one that Max described, where that one in the middle, like, when you have three layers, like, we're not gonna do… I don't think we're gonna have dynamic attributes, Agent 1, Agent 2, Agent 3.
**Mikolaj Knap (Google LLC)** 36:15 Okay, okay, I can look on that. And then… I'll take a second look at how we can maybe… Accumulate the metric… the tokens for the middle agent, somehow, for a metric, because that might also be useful.
**Liudmila Molkova** 36:31 I… it's a new idea that further… We have… would have two sets of… Agent token metrics. One is, like, my immediate use, and another one is my total across all I don't even know… how would we do this? How would we know what… how much suburgent consumed?
**Mikolaj Knap (Google LLC)** 36:53 it would have to be within the context of the same process. I think that's the issue.
**Max Ind (Google LLC)** 36:57 Will it… so… It is simple in the same process, and if there's a remote agent, it would have to return, like, as part of the API, like, the remote agent would have to return, like, usage metadata that this remote agent used this many tokens.
**Liudmila Molkova** 37:16 And they do.
**Max Ind (Google LLC)** 37:17 Yeah.
Yeah, but not… I assume not all of them do, so this would have to be best effort, yeah.
**Liudmila Molkova** 37:28 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 37:29 I think we start break… like, to breaking aggregatability, also, of that, token count metric.
If we… because we want just one set of attributes to record for each… Measurement, and so main agent and nearest agent work.
But if we're gonna track… if we're gonna report it multiple times for multiple… Agents in the tree, then… That starts to be weird. That's where I was kind of saying, like, we would need an Agent 1, Agent 2, we'd need other attributes in there, or… You end up with.
A metric that… The whole aggregation of it doesn't… is kind of meaningless, because there's overlapping measurements.
**Liudmila Molkova** 38:22 would be two different metrics if we do this, right? So my immediate usage… And my subtree usage.
Sorry, my… the whole tree under me usage.
If we do this.
**Trask Stalnaker (Microsoft Corporation)** 38:35 Yeah, but if that's one metric for the whole subtree under me, that one metric If you aggregate away the.
**Liudmila Molkova** 38:45 Whoa!
**Trask Stalnaker (Microsoft Corporation)** 38:46 That.
attribute. Now you have some weird overlapping values, which kind of goes against our recommendations.
**Liudmila Molkova** 38:54 Yeah.
This could be interesting, because, Span attribute.
If you ha- if you know it.
**Trask Stalnaker (Microsoft Corporation)** 39:08 Yeah.
**Mikolaj Knap (Google LLC)** 39:09 Having, like, aggregate token counts for all the subversions.
Okay.
**Trask Stalnaker (Microsoft Corporation)** 39:16 I mean, we could do something, just because it's sort of… it's against our general policy on aggregability of metrics. It doesn't mean we can't break that for a good reason. I mean, if that becomes an important use case.
**Mikolaj Knap (Google LLC)** 39:31 Okay.
**Liudmila Molkova** 39:34 Yeah, I think there are two very uncontroversial pieces from this discussion. The first one is to… Include main agent.
On the metrics and spans, and then include agent name, on the… Inference metrics, if it's not there yet.
**Trask Stalnaker (Microsoft Corporation)** 39:54 And the second one… So, main agent, I totally get, would propagate it down, it stamps everywhere. For agent… Would that be the same thing where, essentially, we're saying.
It's the nearest agent, we just, again, propagate it down, stamp it on everything, but… Further down, agents will overwrite that, and… Yeah. And, yeah, okay, that makes.
**Liudmila Molkova** 40:18 So the nearest one.
Yep. Yeah.
and then the second, what seems to be non-controversial piece is that My immediate agent token spent As a histogram.
**Mikolaj Knap (Google LLC)** 40:39 Immediate agent. So, okay, so the agent on that level, how much they spent?
**Liudmila Molkova** 40:44 Yeah.
**Mikolaj Knap (Google LLC)** 40:46 Uncle.
And then for the aggregate tokens, maybe on spans, but still not determined for a metric.
**Liudmila Molkova** 40:53 I just need to think about it more, and maybe… Effort.
Put… not put it in the scope for stability.
Because it's hard, it's long… initial stability. It's hard, it's long, and… It's… It can be added later.
**Mikolaj Knap (Google LLC)** 41:15 Sounds good. Alright, so two concrete steps, and then maybe a third.
Yeah. Coolah, thank you.
**Liudmila Molkova** 41:24 Thank you. Wait, oh, wait, over time, there is this friend as well, I just want to see what's in there. Oh, I added this, it's Dylan's, and Dylan has left.
I'll review.
Okay, and thank you all.
**Trask Stalnaker (Microsoft Corporation)** 41:43 Alright.
**Liudmila Molkova** 41:44 Oh, we should cancel next week, right? Me and Trask will be out.
**Trask Stalnaker (Microsoft Corporation)** 41:49 Yes.
I will… I will go cancel all, because they gotta cancel it in the LFX.
And in the Google Calendar.
I keep forgetting that we have duplicate calendaring problems now.
**Liudmila Molkova** 42:06 Okay, then enjoy the quiet week, everybody.
who's not coming? If you're coming to KubeCon.
Which you aren't accept Trask on me. Happy to see you next time!
Maybe in Barcelona?
**Trask Stalnaker (Microsoft Corporation)** 42:20 Heh, yeah.
**Liudmila Molkova** 42:22 Oh, it's delayed to submit proposals. Shit.
**Max Ind (Google LLC)** 42:26 Anyway…
**Mikolaj Knap (Google LLC)** 42:27 Where are you?
**Max Ind (Google LLC)** 42:29 Yeah, where are you going for… for the… for the week? The… the KubeCon, yeah?
**Liudmila Molkova** 42:34 Conventions of, like, cities.
**Trask Stalnaker (Microsoft Corporation)** 42:35 city…
**Max Ind (Google LLC)** 42:36 Yeah, yeah.
Yeah, yeah, heard about it, yeah.
We considered bugging our manager to send us, but… But we… I don't know why… why we opted not to.
**Liudmila Molkova** 42:50 bugged them to send you to Barcelona, in…
**Max Ind (Google LLC)** 42:54 Oh.
**Liudmila Molkova** 42:55 March 2027.
**Max Ind (Google LLC)** 42:57 Oh, we need to do that. Yeah, I was just in Barcelona, it's really cool.
So yeah, we need to do that.
Yeah.
**Mikolaj Knap (Google LLC)** 43:07 Luminous.
**Liudmila Molkova** 43:08 Okay, have a good weekend.
**Max Ind (Google LLC)** 43:10 Have a good weekend. Bye-bye.
**Mikolaj Knap (Google LLC)** 43:11 You too.
