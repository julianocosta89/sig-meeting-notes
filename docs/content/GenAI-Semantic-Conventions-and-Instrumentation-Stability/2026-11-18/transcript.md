SIG: GenAI Semantic Conventions and Instrumentation Stability
Date: 2026-11-18
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker (Microsoft Corporation)** 00:38 Hey, Max.
**Max Ind (Google LLC)** 00:41 Hey, hello.
**Mikolaj Knap (Google LLC)** 00:46 Hello?
**Trask Stalnaker (Microsoft Corporation)** 00:50 Amy McLeh.
**Max Ind (Google LLC)** 01:07 How was the… how was the KubeConf?
Trask? You went right.
**Trask Stalnaker (Microsoft Corporation)** 01:12 Yeah, yeah, that was… Good, long. Haha.
The sun would… with the regular coup, because Limila and I had a talk on Thursday afternoon, the last afternoon, so… Had to stay the whole thing, and then, but there's two pre-days, so the conference, like, started on Sunday and went through Thursday.
**Max Ind (Google LLC)** 01:41 Is the… was the talk recorded anywhere?
**Trask Stalnaker (Microsoft Corporation)** 01:45 Yeah, it… they… they're usually pretty good about getting out those recordings, Like, within a week or two.
Yeah, I'll keep my eye out for that, and yeah, we'll post it to the, to the channel.
**Max Ind (Google LLC)** 02:03 Sounds great, thanks.
**Trask Stalnaker (Microsoft Corporation)** 02:11 Alright, so, I did a little bit of organizing.
So, the pull request dashboard… so, we now have this stabilization wave, label.
And so I labeled… issues and PRs that I thought We're in the stabilization wave.
And it shows up now in the PR dashboard.
So this should give folks a good, sort of, indication of what to… like, if you're looking for something to review, please hit up these, And if you have any of the PRs that are tagged with that, Yeah, well, let's keep those.
Going… And then… Here, I just replaced, sort of, this… tracking issue. So now we have the… PRs, for this, the label.
Open issues, and then this is, I didn't know you could do this, but, you, this will show you all the issues.
with this label that do not have a PR linked to them already.
So this is a good… List of things to pick from.
for working on… And then, sort of within that, We were talking yesterday about making the release Soon, from this repo.
It won't be an RC, but we… it will be just a release to, let people… it's been a long time since we've had a release, and so… I think it's a good idea.
And these… I kind of looked at things that… nice to have for the release, definitely not must-haves. The… In terms of most breaking, so there's actually not a lot of, like, Big breaking things left.
There's a lot of, sort of, clarifications and, When to capture certain things. So certainly braking changes, in our definition of braking, but these are the biggest breaking ones, sort of.
**Liudmila Molkova** 05:00 Well…
**Trask Stalnaker (Microsoft Corporation)** 05:01 geometry shapes.
**Liudmila Molkova** 05:02 Maybe we don't have them as… Issues, but… or PRs.
But, like, all the additions for attributes and metrics.
That we had.
would be breaking.
**Trask Stalnaker (Microsoft Corporation)** 05:19 Yeah. Like…
**Liudmila Molkova** 05:20 Mildly, we would do this even after our seat.
But, like… not… not… Still something we have to address before stability.
**Trask Stalnaker (Microsoft Corporation)** 05:31 Yeah, yeah, so I took this, like, most breaking, like, we consider adding attributes to metrics to be a breaking change.
But yeah, I was just trying to scope it down to things that are… Majorly breaking versus minorly breaking, if you will.
**Liudmila Molkova** 05:50 Oh, okay. Okay.
**Trask Stalnaker (Microsoft Corporation)** 05:53 So these were the ones that I thought were, like, in that category of majorly breaking.
This one, Looked good to me, I approved it, makes sense to me to align, oh, Lynn Miller reviewed it, awesome. Alright, so that we're…
**Liudmila Molkova** 06:16 Couple of minor things. So, Dylan, whenever you push… Either ping me, or let me know, and I'll merge.
**Dylan Russell** 06:26 Okay Is this for the prompt variable thing, or… Yeah, yeah.
**Trask Stalnaker (Microsoft Corporation)** 06:30 Yeah.
And then the… result… I suspect we might.
Not… that might not make the release, since there's a couple alternative options, and… Probably worth a little bit more thought there.
This one, there was kind of the… One outstanding, like, this potential change, that…
**Liudmila Molkova** 07:05 Huh.
**Trask Stalnaker (Microsoft Corporation)** 07:05 I forgot to think more about. So anyway, I will… I have that on my list to think about this afternoon, and… If I think it's a good idea, I will send a PR.
And we can… Discuss more there.
**Liudmila Molkova** 07:24 I… Oh.
Want to get the… Opinions and temperature on… This, if you can open it for a sec.
**Trask Stalnaker (Microsoft Corporation)** 07:35 Yeah.
**Liudmila Molkova** 07:35 So, for the big things, let's put aside that, like, the noun versus verb target thing.
for management, like Manage Agent, Manage Memory, Manage Memory Store, Are we okay with it? I… I think we, at some point, have decided that the principle is that we should break things down.
as a default.
And then the manage, the create, update, delete.
It fills a lot of metrics and spans to define.
For what feels like no pragmatic reason.
And I kinda want to… Say that, okay, we have one thing, one metric, let's say manage… Agent?
but different operation names. I think this is a good middle ground.
But it still keeps the line of when do we create the new… operation versus, merge them. It's still blurry.
**Trask Stalnaker (Microsoft Corporation)** 08:50 And so, specifically, This is the proposal in terms of… there would be 4… I mean, 4… new metrics, but… As opposed to, like, 10 or… Yeah. So…
**Liudmila Molkova** 09:20 We can also don't solve this problem yet, because none of this front are in the stability wave.
**Trask Stalnaker (Microsoft Corporation)** 09:41 I like that.
Search memory is different from…
**Liudmila Molkova** 09:52 Data plane, so control plane versus data plane.
Cold pass versus hot pass.
Oh, maybe update memories also, Dave. Sorry, yeah.
So, when you start looking into this, it gets difficult.
And if we compare it with databases, then search in database.
Just query covers the read and write, so the search memory would be just some of the database queries.
An update memory is a different set.
**Trask Stalnaker (Microsoft Corporation)** 11:41 Okay.
I will try to think about that, also.
It makes sense to me, other than, like you said, the, the update.
**Liudmila Molkova** 12:05 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 12:11 And then… This one didn't… I don't think there's any strong reason to… for this to make it into the release candidate. I mean, not the release candidate, then the next release.
**Liudmila Molkova** 12:30 Yeah, and there is no PR, right?
**Trask Stalnaker (Microsoft Corporation)** 12:32 No.
So, yeah, I would say, yeah, let's just, target this one only… And make release.
Yeah, and then all the other one, PR's just rolling.
**Liudmila Molkova** 13:08 Do we want… Schema published.
Not a Nutella yet.
But, like, as a release artifact.
Or… Maybe I… I have Max say, sloped together the proposal for RitalIO.
On just starting to publish those.
Not in the… as the docs, it's the next step after the release, but as,
**Trask Stalnaker (Microsoft Corporation)** 13:49 Yeah… Just the schemas themselves.
**Liudmila Molkova** 13:53 Yeah, but probably they need to do the whole round of onboarding.
Anyway, I'll ping to tell your people. It doesn't block the release, and we don't have to do anything special now.
Until RC.
**Trask Stalnaker (Microsoft Corporation)** 14:09 Yeah.
But, yeah, let… I mean, it would be nice to get the… Get that ball rolling for the… schema. Yeah.
Itself, even if not the… docs. I guess the docs, too. I mean, now, once we have a release, then we can kind of have concrete discussions with the, But… Website folks.
Alright, max, do you want to drive?
**Max Ind (Google LLC)** 14:49 Sure. So, yeah, so since last time?
I updated the naming to, like, include the agent and invocation, and I changed the valence to be… Root instead of nested, and the reasoning is that root comes out slightly ahead, because Because for the isNestTed to work.
Kind of any agent not participating in this?
Breaks this nested.
Because… If an agent doesn't participate, it doesn't set the… The nested Boolean.
And then it looks like the root.
agent. There are also many cases where the root breaks, but they… I believe comes out to, like, a subset of… like, I believe it's less… than in the case of Nested.
**Trask Stalnaker (Microsoft Corporation)** 16:07 And, could you walk us through the, the prototype?
**Max Ind (Google LLC)** 16:14 the prototypes.
That's, actually… A great question, because I have mostly left that up to to agents, I mostly, focused on the Yamalu, wording, so…
**Trask Stalnaker (Microsoft Corporation)** 16:34 That's okay, just sort of, like, what, what kind of support, Like, these are framework…
**Max Ind (Google LLC)** 16:49 These are frameworks, yes.
So, basically, I think it doesn't impact inference at all. I think it only impacts frameworks, and basically.
We within… Like, basically, we would have, like, a short contract through the dependency on GenAI Hotels?
In the prototypes?
Actually, there's, like, a shared key.
It doesn't depend on, like, the GenAI rules.
Okay, but…
**Trask Stalnaker (Microsoft Corporation)** 17:23 key…
**Max Ind (Google LLC)** 17:24 Yeah, it's just like… It's, like, defined in, like.
Kind of the sh… the reference shirt.
dot pi.
Sorry, should I share the screen?
**Trask Stalnaker (Microsoft Corporation)** 17:39 Yeah, if you…
**Max Ind (Google LLC)** 17:41 Nevermind.
**Trask Stalnaker (Microsoft Corporation)** 17:41 That'd be great.
**Max Ind (Google LLC)** 17:43 Okay, and… I think this should be it.
Oh.
Actually, that's… it's not… that's the wrong… that's the wrong screen.
Okay.
It's this one.
And yeah, basically, this usually… this would come from the… Genai Hotels.
library, usually, but in the prototypes, I just defined it here, and then all of the frameworks set, like.
Read and write, through this key.
And then they… pass it through auto context.
And then if, there's a… There's an Agentic system built using many frameworks. They still share the same key, so they can… They can pass this information, whether something is nested for this key.
**Trask Stalnaker (Microsoft Corporation)** 18:56 And, I recall… I remember that some of the frameworks, like, we didn't get parent-child relationships.
Because of the way they loop, but I guess… Do we always… we always have a parent. It's the… it's the children that don't nest properly.
**Max Ind (Google LLC)** 19:19 Yeah, I think so… from the previous PR, from, like, the merging the Invoke workflow and Invoke agent.
I believe, pretty much every framework has one root agent, and, like, two exceptions were the ADK and OpenAI agents.
Where we introduced this, like, framework entry point, calling this also an agent. So these now also have one root, agent.
**Trask Stalnaker (Microsoft Corporation)** 19:52 Great.
And are there any, just for my… are there any… framework… are there any, agent… Running libraries that run agents that don't support nesting? Like, is this basically universal, that they all… Can run nested agents.
**Max Ind (Google LLC)** 20:17 Yeah, I'm sure, like, simple… Agentic frameworks that don't have any sub-agents.
I'm sure that they exist, I don't know any. Maybe, like, Genkit?
But I haven't.
I haven't, done the…
**Trask Stalnaker (Microsoft Corporation)** 20:35 Common one… not the common ones that we're instrumenting.
**Max Ind (Google LLC)** 20:40 I think so, yeah. I think, I think sub-agents are pretty, pretty universal across Most of the frameworks I've seen, yeah.
**Trask Stalnaker (Microsoft Corporation)** 21:14 And this was pretty straightforward. It looks like the, Updating, applying this was pretty straightforward.
**Max Ind (Google LLC)** 21:24 Yes, as long as there's a short key, I… I have, I have not written this code, I mostly just glanced over it, just to, like.
See that there's no, like, just, like, insane, Yeah, yeah, just to make sure that it's, like, not, Sorry, I can't find the words looking.
**Trask Stalnaker (Microsoft Corporation)** 21:56 Simple. While you were just scrolling through it, it looked simple.
Which is good.
I guess the last thing, could you go over, I know we discussed before, but the motivation… Did you fill in the motivation section, sort of, for why we want… The use, yes?
**Max Ind (Google LLC)** 22:25 Hmm, how do… how do I go back to the… I guess I can… Yeah, this, this was, basically the motivation is, just the end-to-end duration for a, multi-agent system.
Because… If there are many agents, then there's no way to know The duration of, of the… at the end to aid generation of Agentic system, because you would have to have prior knowledge of Which agent is the… actually the root one?
**Trask Stalnaker (Microsoft Corporation)** 23:15 Right. Now, I… you had an issue open about the idea of, metric… Err… agent…
**Max Ind (Google LLC)** 23:30 Yeah, like, roll-up. So, aggregation of tokens for… For each agent, including delegation and sub-agents, yeah.
**Trask Stalnaker (Microsoft Corporation)** 23:42 Right. In that case, though, it's sort of the opposite, where you would need, like, for that to be useful, you need to know the specific agent name that you're rolling up to.
Where, like, in this case, if you had that agent name you were rolling up to, you wouldn't need the is root.
Flag.
**Max Ind (Google LLC)** 24:06 I… So, to know that's… if you know the specific agent. So, so the roll-up, I think the point of it is to know Like, a total token usage for any subtree of An agent. And then, if you want to know the end-to-end token usage. You would need to know the… You would need to know which agent is the root.
But this could also be solved by, like.
but also adding a Boolean on the roll-up metric, which is to signify that, like.
In this particular, I call it, lineage.
This agent is the first agent.
Which, means that… You then would also be able to find out… the end-to-end… Like, the total token… count for the root agent, but I guess the total token count for the root agent It's just… The sum of all token counts.
Probably.
**Trask Stalnaker (Microsoft Corporation)** 25:22 Yeah, I think it's more complicated. Like, I'm not sure the… knowing the root helps in the token count. I think we've… Knap up in… Yeah.
So the primary use case here is the… yeah, the… duration.
**Max Ind (Google LLC)** 25:44 That's right. Like…
**Trask Stalnaker (Microsoft Corporation)** 25:46 for alerting…
**Dylan Russell** 25:57 I have a question.
Does the mechanism that you use… matter? Like, do we need to agree on that?
That, context key.
is the… Way we use to, like, decide if… We are the root or not.
Like, do we need to agree with the value of that key and the mechanism?
**Max Ind (Google LLC)** 26:25 the value of the key. I think it's, Yeah, the mechanism definitely has to be agreed on by the… so that all the frameworks Speak the same language?
And what the value the key holds?
I don't know if, If that needs to be solved, because, like, it may just be the presence of the key in the context signifies that That the, Yeah, that a given invocation is not the root invocation. I could add the specific wording for this.
Context key here.
I don't know if that would be, yeah, usually the implementation detail, or… I think it could.
**Liudmila Molkova** 27:16 be useful, but, like, first, we don't put them. Secondly, or from the language agnostic perspective.
they are packed. You cannot… Find the key by the name, by string name, by literal.
**Dylan Russell** 27:39 Why not?
You can't find it.
You don't use a literal screen.
**Liudmila Molkova** 27:44 It's a spec language that it says you cannot.
And I think Python violates.
**Trask Stalnaker (Microsoft Corporation)** 27:49 object… You have to have the actual instance of the… the same instance of the context key.
To get back the same value.
**Dylan Russell** 28:05 You can't just agree on a string value? Like, a unique string value?
**Liudmila Molkova** 28:09 No, you cannot make life easy. You have to take dependency on OpenTelemetry object, an artifact that defines this object.
**Dylan Russell** 28:20 Hmm.
**Liudmila Molkova** 28:21 You cannot do it without dependency.
**Dylan Russell** 28:24 Okay. Bye.
**Aaron Abbott (Google LLC)** 28:27 I think you… you… in Python, you technically can do. Like, it's just a type annotation that says you should call createKey beforehand, but… I don't know, shh.
Don't tell anyone.
**Liudmila Molkova** 28:38 Don't tell anyone that Python keep working, you cannot break it anymore.
**Trask Stalnaker (Microsoft Corporation)** 28:44 Right.
**Mikolaj Knap (Google LLC)** 28:56 I have a question?
For this… Proposal.
Instead of using isNested, why not just have main agent stamped on the metric instead? And then you could just check… on the metric, main agent, equal equal, agent name, and then C, Based on that, that would be the route duration, and then you would get the same… Take effect.
**Max Ind (Google LLC)** 29:22 Yeah, so that is because I think The main agent, at least right now, is supposed to be either a resource attribute, or it's… If A2A is involved, it's supposed to be the A2A agent name, and that… Yeah, I don't know if right now A2A emits an invoke agent spun, like, an internal invoke agent spun.
So, if main agent meant… Basically, the framework Define, like, the name of the framework, root agent object that would Perfect.
But I think it may also mean, like, the resource, or, like, the agent server, or, like, the A2A service.
In which case… That probably doesn't, doesn't, emit… the internal invoke agent span.
**Liudmila Molkova** 30:23 We could work around this, but I think, Aaron, you brought up that primedius would not be happy. It's very hard to actually write a PromQL query like this.
**Aaron Abbott (Google LLC)** 30:35 Yeah, I think you have to query the metric twice and join it against itself to do it in ProQL.
**Trask Stalnaker (Microsoft Corporation)** 30:43 Because it's a resource attribute.
Main agent as a resource attribute.
**Aaron Abbott (Google LLC)** 30:49 No, I think there's just no operator to compare attributes on the same stream.
**Liudmila Molkova** 30:54 The resource attribute makes it, like, 10 times harder, but even without it, it's pretty difficult.
**Mikolaj Knap (Google LLC)** 31:03 Okay.
So, most viable. Sounds good.
**Max Ind (Google LLC)** 31:30 unless… unless no one has any questions, I'm… I'm happy to wrap this up here, and… Like, finish the rest of life.
**Liudmila Molkova** 31:47 Yeah, I'll take another look. I like the name.
**Max Ind (Google LLC)** 31:53 Thanks.
**Liudmila Molkova** 31:53 Assuming query name, invoke agent to agent underscore invocation.
**Max Ind (Google LLC)** 32:01 I did.
**Liudmila Molkova** 32:01 the end. Yeah.
**Max Ind (Google LLC)** 32:03 Yeah, then… An agent under invocation, then… I'd have to think about it, but if it was, like, agent… If we are now discussing changing the dots to an underscore, then I would be… A little hesitant, because there's already agent.name, which make it… we already fell into this… this hole with cloud.resource.id and underscore ID, so… It would be… would be good not to fall in that hole again, yeah.
**Liudmila Molkova** 32:42 To ask, how do you feel about when we are thinking about the renaming operation names to switch the dots there?
To match the namespaces.
I'm sorry for bike shedding.
**Trask Stalnaker (Microsoft Corporation)** 33:01 No, no, no, I just… I have to make a note, so when I, Go through… Okay, I'm just updating my comment there to… Okay, cool, I will… Think on that. One… thought for this root PR… I was trying to think if there's any… generalization here, to… I mean, we have nesting… nested… spans for other… Instrumentation for other Semantic Conventions.
We can. It's certainly… more prevalent.
Here… like.
**Liudmila Molkova** 34:58 Or, like…
**Trask Stalnaker (Microsoft Corporation)** 34:58 VP.
Yeah, go ahead.
**Liudmila Molkova** 35:04 So, like, if we… Can… if… is it applicable in other areas?
Well, the HTTP example is, like, you have the… Controller and the web server, right?
And all of them can be considered HTTP.
**Trask Stalnaker (Microsoft Corporation)** 35:34 Yeah, I mean, you can have… HTTP… well, yeah, yes. You can also have nested HTTP servers, like… Tomcat capturing the HTTP server at that level, as well as at the servlet API level.
**Liudmila Molkova** 35:52 But then we… Kinda assume they represent the same operation, and even though they're not exactly the same.
They are…
**Trask Stalnaker (Microsoft Corporation)** 36:04 That's a good.
**Liudmila Molkova** 36:05 From some perspective, the same.
**Trask Stalnaker (Microsoft Corporation)** 36:08 Yeah.
Yeah, so maybe we haven't really had this.
example before.
Where we sort of have… Potentially, like… Recursive or nested?
Operations that are different.
**Liudmila Molkova** 36:37 Yeah, maybe it's applicable in other cases. So, like, there was this actor frameworks, and there are also this… complex things, I like agents, but deterministic.
Or maybe some stream processing things where you… Can have multiple layers of… Something similar.
**Trask Stalnaker (Microsoft Corporation)** 37:17 Okay.
Yeah, I agree, it's a good… does feel like a good problem to solve here.
Cool, we're… At time, and I think, oh, let's see, Dylan, let's chat briefly.
**Dylan Russell** 37:47 Sounds good.
**Trask Stalnaker (Microsoft Corporation)** 37:48 Pressing duplicate nested GenAI operations.
**Dylan Russell** 37:55 Yeah, so related to the discussion… We were just having, sort of… So yeah, this is an issue that occurs when, like, the same… Operation is instrumented By different libraries in the stack.
So, like, 80K… And the Anthropic SDK.
Both.
Instrument the inference call.
And we don't want two spans in this case.
And I'm wondering if the… Simplest solution is… Just put a key into the context.
the outermost instrumentation. Just put the key into the context.
And… The inner one, if it sees the key.
Suppresses all their instrumentation.
So it'd have to be a unique key for each span type where we think there could be… Where we think this issue could happen.
Which is, like… like, inference… embedding… Yeah, there might be, like, a few others.
**Liudmila Molkova** 39:20 All the client calls, probably.
**Dylan Russell** 39:24 Right.
**Trask Stalnaker (Microsoft Corporation)** 39:28 Would you need different keys for each client call, or… Would it be enough to just have one GenAI client?
Key.
**Dylan Russell** 39:48 I do think it's unlikely… You would get… like, you could probably just use one key.
Because you won't have, like, an embedding call triggered inside the inference call on the client.
I don't think.
**Max Ind (Google LLC)** 40:11 you would… if it was one key, you would, no, no, no, no, sorry, it's a different point. I think with one key for all the clients.
You would need to have, like, a sum type As the value for the context key, and that might be a little confusing that… One context key is not associated with one… Type.
**Liudmila Molkova** 40:39 Yeah, because…
**Trask Stalnaker (Microsoft Corporation)** 40:40 need one… like, you need a separate key for, like, HTTP.
client But do you need… Separate keys for… do you need more than one?
flag for GenAI client. Like, do… Hey, dude.
Other, do they nest in weird ways like that? And B, do we care if they do, or can we just capture the outermost logical operation?
**Liudmila Molkova** 41:18 I think Max just mentioned that, a good point, that It probably… they don't nest, or if they do, it's some… such an exotic case that we shouldn't take it seriously.
But, in… Dylan's, suppression mechanism, it… it is awesome, because it's not just the suppression, it's the enrichment as well.
So we kind of rely on the same type and the same structure behind the key. We can do the type checking.
But it's just… I don't know.
the… Is there a problem with multiple?
Keys, participant type.
**Dylan Russell** 42:05 I don't see any problem.
I did want to just start with just putting the key… just do the suppression piece to begin with, like.
Just put the key in by itself.
Like, in the prototype, we have this complicated logic around, like.
Put, like, all the attributes into the context.
As well, and then, like, which ones take precedence?
And the inner one can, like… add to it, but I think that's, like, too complicated.
**Liudmila Molkova** 42:40 Oh, you want to remove it?
**Dylan Russell** 42:43 No, no, I think just for, like, semantic conventions, just to begin with, we say, just put this key in.
And let's just solve, like, this duplicate telemetry suppression thing to start with.
And then maybe later down the line, we can add this, like, enrichment from lower layers thing.
**Liudmila Molkova** 43:11 Yeah.
Been avoiding putting this into semantic conventions so far.
Across the board.
**Dylan Russell** 43:26 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 43:28 Well, partly because it's… It's… language… I mean, it's sort of language-specific in terms of… Again, because of the opaque Ness of the context key.
We essentially have to tell people to use this dependency to… Get the context key.
At least until we have context scoped attributes.
**Liudmila Molkova** 44:04 And even then, it might be difficult.
Because, we would put… We don't want to just blindly stamp all these attributes on everything under.
And we want to… Like, let's say, enrich the… The same spend type above you for the same operation.
**Trask Stalnaker (Microsoft Corporation)** 44:33 Even if we set aside enrichment, though… Just focusing only on suppression.
We still have that problem today without context-scoped attributes.
**Liudmila Molkova** 44:46 Yeah, I'm kind of arguing with the context scope attributes that they are not going to solve it, really.
**Trask Stalnaker (Microsoft Corporation)** 44:52 Oh, the suppression?
Why not?
**Liudmila Molkova** 44:59 Like, you put some… some… something in the context scope attributes to say… to suppress stuff under you?
**Trask Stalnaker (Microsoft Corporation)** 45:09 Yeah.
**Liudmila Molkova** 45:11 But, like, the contract is that you put stuff into context called attributes, and it's… Stamped on the signals under.
**Trask Stalnaker (Microsoft Corporation)** 45:25 So by default, they don't get stamped.
Onto them.
I forget… and I forget if it's you… Allow them all.
to get stamped.
**Liudmila Molkova** 45:39 So you pick a signal, and I think it's on by default for spans, and not by default for metrics.
**Trask Stalnaker (Microsoft Corporation)** 45:45 Oh, I see. Okay.
**Liudmila Molkova** 45:48 I denounce.
**Trask Stalnaker (Microsoft Corporation)** 45:50 Okay.
**Liudmila Molkova** 45:55 I'm thinking, should we… Well… Trask, you know, but I… at some point a long time ago, I wrote a note up about this.
And it received a lot of comments, but I abandoned it at some point.
Maybe we should have, some form of guidance and Semantic Conventions core, how to do it in a generic way?
So if you want suppression, for the common layers.
I don't know, you should probably… Not in meat, one span for two operations… sorry, two spans for the same operation.
And then you can have, I don't know, a context-per-pen type, or a kind.
Or… something else, and then just to explain what's done in Java now in GenAI for the suppression and different strategies for the suppression.
And that it should probably be configurable?
**Trask Stalnaker (Microsoft Corporation)** 47:01 I think we could get that into the, API, like, give me the context key for this span type.
**Liudmila Molkova** 47:10 Give me the context key for the spend type.
**Trask Stalnaker (Microsoft Corporation)** 47:13 this… this suppression, I don't know, sort of… Yeah.
I guess sort of similar to what we've built in Java Instrumentation, but… Into the, I would feel a lot better about adding it to Semantic Conventions if it was in the API itself.
**Liudmila Molkova** 47:32 I… yeah.
I like it.
So it's just, like, the… Special Purpose Registered Context Keys.
Right.
**Max Ind (Google LLC)** 47:46 I am…
**Liudmila Molkova** 47:47 One for a spot, yeah, go ahead.
**Max Ind (Google LLC)** 47:49 Yeah, I'm curious, could, like… I'm struggling to find where the chat is on Zoom.
To share a link, but, like, they're… but they are… there are, like, open telemetry Semantic Conventions.
packages per language, which define the constants. So could these packages house the context keys?
**Liudmila Molkova** 48:20 But you would then need to depend on this library.
**Max Ind (Google LLC)** 48:24 That's true, and ATK, we already do depend on this library.
**Liudmila Molkova** 48:28 Oh! Seriously, Semantic Conventions?
**Max Ind (Google LLC)** 48:31 Yes.
**Liudmila Molkova** 48:33 Oh, oh my goodness.
**Max Ind (Google LLC)** 48:34 For, like, Constance.
**Liudmila Molkova** 48:36 Okay.
Okay.
It could be there, but, like, if it's in the API, if you only depend on Autel API, it's even better.
**Max Ind (Google LLC)** 48:51 That's true.
**Liudmila Molkova** 48:51 And the spend type is going to be part of the API.
Today?
Tomorrow it's released, or Friday it's released?
**Max Ind (Google LLC)** 49:04 Nice, yeah, but then… so, wait, so spend type is gonna be in the OpenTelemetry API?
Package. So, like, the… like, the… GenAI Invoke Agent internal, kinda… static string will be in the OpenTelemetry API.
And then… So, like, even non- GenAI… Instrumentations that depend on the API will depend on this.
This next drink.
**Trask Stalnaker (Microsoft Corporation)** 49:37 the… the concept of span types in the API.
**Max Ind (Google LLC)** 49:42 Okay, so it won't enumerate all of the spend types that exist in Semantic Conventions. Okay, okay, okay.
**Liudmila Molkova** 49:50 But the library, the Semantic Conventions library, you depend on might enumerate them all.
Yeah. So, Trask, let me think about this. I really like the idea as another question of capacity and prioritization.
I'll create an issue.
**Trask Stalnaker (Microsoft Corporation)** 50:12 Okay. Cool.
Alright, cool, so we will be… We'll chat in Slack about release stuff.
**Liudmila Molkova** 50:30 Yep.
I will start investigating it.
**Trask Stalnaker (Microsoft Corporation)** 50:35 Alright.
**Liudmila Molkova** 50:36 Awesome.
**Trask Stalnaker (Microsoft Corporation)** 50:36 Thank you all.
**Liudmila Molkova** 50:37 Thank you.
**Dylan Russell** 50:38 Biggest.
**Liudmila Molkova** 50:38 Tia.
**Max Ind (Google LLC)** 50:39 See you, baby.
