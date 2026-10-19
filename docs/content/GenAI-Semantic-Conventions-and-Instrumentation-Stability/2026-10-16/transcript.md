SIG: GenAI Semantic Conventions and Instrumentation Stability
Date: 2026-10-16
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker (Microsoft Corporation)** 01:14 Hey, Max.
Happy Friday!
**Max Ind (Google LLC)** 01:17 Hey, hello.
Are you doing?
**Mikolaj Knap (Google LLC)** 01:22 Hello.
**Trask Stalnaker (Microsoft Corporation)** 01:22 Good. Thank you. Hey, Mikola.
**Max Ind (Google LLC)** 01:32 Thanks for the.
For the references to.
Avoid the duplicate metrics.
**Trask Stalnaker (Microsoft Corporation)** 01:39 Oh, yeah.
**Max Ind (Google LLC)** 01:40 Yeah.
I didn't have a chance to look at it yet, I just got reminded.
Of it right now.
Yeah.
But,
**Trask Stalnaker (Microsoft Corporation)** 01:53 I'm not sure if they're, like, fully on point, but, hopefully give some ideas.
**Max Ind (Google LLC)** 02:00 Yeah.
Definitely will be a good read so that I know stuff outside of the GenAI world, yeah.
**Trask Stalnaker (Microsoft Corporation)** 03:01 Alright, so… for… Let's see, for… Things we are going to look at… Let's just check in… There's a couple I know that are worth… discussing here… But why don't we, start with anything that… Folks here want to raise.
**Max Ind (Google LLC)** 04:40 Okay, I could raise the… 571, I could give an update on that.
And… I have, since the last time.
I have removed most of the controversial stuff, which are the… term, terminology, and now I think the scope of this is much smaller, because.
Because basically, what I wanted is, like, a third thing other than the agent and the workflow.
And, this was a turn, but the turn also had other properties, which is like Being emitted only once per subtree in a trace.
And that one, Trask brought up a good point that this kind of hurts local reasoning that like If… whether the span is emitted or not is kind of influenced by it, by what happened Way, higher in the… Trace, that's kinda unintuitive.
And I definitely agree. So now I think this scope of this PR is twofold. One, it's the… Folding of the invoke agent and invoke workflow under a single span type, which is the invocation.
And the second one is just adding an operation name for… The… like a… an operation name for something which is not an agent or workflow, and two examples of this that I could find were entry points to ADK and OpenAI agents, and coincidentally, they are both named Runner.
Now, I don't want to… Enshrined runner in the.
In the Semconf?
But I'm thinking that, like, invoke underscore and the name of the framework entry point, that it's, like, a reasonable… Operation name to have.
And so this is the now the extent of this of this Pr, yeah.
**Liudmila Molkova** 06:53 I think we need to decide on the span type and metric name first, and invocation alone I feel is… Not specific enough. It can be an indication of anything.
**Max Ind (Google LLC)** 07:09 Sure, sure, yeah. I have some… Comparison for the naming in the.
In one of the comments under the PR?
Some candidates other than invocation are… There's orchestration, maybe?
And… I haven't seen the naming, which is less vague than orchestration.
Perfect.
**Liudmila Molkova** 07:37 So the orchestration would describe the overall thing.
And we need something that equally represents invoke agent, invoke workflow, and invoke foo.
**Max Ind (Google LLC)** 07:50 The entry point of an Agentic framework. Yeah.
**Liudmila Molkova** 07:53 Right.
**Trask Stalnaker (Microsoft Corporation)** 07:56 Oh, Ludmila, you're talking about the name for the internals… I mean, the name for the span type?
**Liudmila Molkova** 08:02 Spend type metric name.
**Trask Stalnaker (Microsoft Corporation)** 08:05 A metric name, okay.
So not necessarily, not that third thing, but that generic umbrella term.
**Liudmila Molkova** 08:13 Yeah.
And then I feel operation name, we can define some values today, but long term we don't need to. It can be anything for operation name.
**Aaron Abbott (Google LLC)** 08:26 Just to clarify for me, we want the span type to be one-to-one with the metric.
And that's the reason that we wouldn't give them separate spend types.
**Liudmila Molkova** 08:38 I think we want the same span type, because if you query… Agent invocations, it doesn't matter how Agentic API looks like.
You want to query these things in the similar way, because they are the… Agentic operation that resulted in user.
And output to user.
**Aaron Abbott (Google LLC)** 09:09 What if you wanted to know, like, how many… how many, Agents started with a workflow instead of, like, a… Agent, like, how many people are using Workflow, or something like that? Like, you would…
**Liudmila Molkova** 09:23 You would query the same, but add another filter where workflow name is not Empty. Word. Present.
**Trask Stalnaker (Microsoft Corporation)** 09:32 Or look at the operation name.
**Liudmila Molkova** 09:35 where I look at operation name by the operation name.
Then you need to know your system, and which SDKs you use, and operation names might change over time, but spend times are… spend types would be much more reliable.
**Trask Stalnaker (Microsoft Corporation)** 09:52 And I would think, Aaron, that most people will be looking for, by agent name, like, the… How many agent invocations there were by agent name, and… My understanding is all these things, whether it's run… or workflow… They have an agent name on them.
Like, they are… An agent? Is that… Which is where, like, I keep thinking of them all as… I keep leaning towards Invoke Agent for them all, because they all have… They're sort of all agent-centric.
If I understand.
**Liudmila Molkova** 10:56 So I need a noun.
That's… And a verb or some verb made of an invocation.
Right, so, that would.
For the span type and metric name.
Plain invocation is too vague because of it can be invocation of what, right?
**Max Ind (Google LLC)** 11:21 Yeah, yeah.
**Liudmila Molkova** 11:22 Yeah, and we have an option to call it agent. We can. We have an option to call it something more vague.
**Max Ind (Google LLC)** 11:31 How does orchestration sound?
**Liudmila Molkova** 11:38 But it represents a single agent invocation as well, right?
**Max Ind (Google LLC)** 11:44 Oh, yeah, the… so orchestration… Maybe… maybe orchestration is not good, because I was thinking of orchestration, like, you orchestrate tools and, And, inference.
With an agent, or you do this with a workflow, or you do this with any… Anything that's more than just calling the inference client.
But sometimes people also.
Talk about orchestrating multiple agents.
**Mikolaj Knap (Google LLC)** 12:21 Maybe execution or dispatch?
One of those two.
**Max Ind (Google LLC)** 12:33 Another.
**Liudmila Molkova** 12:33 Although the…
**Max Ind (Google LLC)** 12:35 Liz Bates.
**Trask Stalnaker (Microsoft Corporation)** 12:35 That covers the verbs.
**Mikolaj Knap (Google LLC)** 12:37 No.
**Trask Stalnaker (Microsoft Corporation)** 12:38 I think Ludovilla was also asking for a noun.
**Max Ind (Google LLC)** 12:42 down… So we were kind of looking for a noun that, Covers both workflow and an agent.
**Liudmila Molkova** 12:54 Yeah, the thing that does the operation, that invokes.
**Max Ind (Google LLC)** 13:05 I'm gonna ask AI Overview.
**Liudmila Molkova** 13:13 Yeah.
I, like, I think there are two options. One, we found the course agent to be this thing, where we come up with another Name for that, the umbrella name.
That's less cryptic, or, like… Less specific.
But then I tried and I kind of failed.
And my.
Stances probably invoke agent or agent invocation if we want them to be like.
Nouns, all of them inference embeddings.
Invocation.
Hmm.
I think that that's the best I could come up with.
**Trask Stalnaker (Microsoft Corporation)** 14:04 Do we, just to make sure I understand correctly, do we expect Like, does RUN have an agent name?
Attribute.
**Max Ind (Google LLC)** 14:18 Oh, the, oh, the invoke run.
**Trask Stalnaker (Microsoft Corporation)** 14:20 And… Yeah, the Invoke Runner.
**Max Ind (Google LLC)** 14:23 I don't think it does.
It may be good for it to have, because it would… it may be, like, the entry point agent, like, the agent which runs as the entry point to the… And.
to this Okay.
Like, framework invocation.
**Trask Stalnaker (Microsoft Corporation)** 14:48 the.
**Liudmila Molkova** 14:50 Go ahead.
**Trask Stalnaker (Microsoft Corporation)** 14:50 Go ahead.
**Liudmila Molkova** 14:52 In my mind, they both… they… it has… Attributes identifying the… the thing that… is being invoked. So it has Agent name, Workflow name.
**Max Ind (Google LLC)** 15:04 or.
**Liudmila Molkova** 15:04 What are future entities that could execute it?
**Max Ind (Google LLC)** 15:11 Yeah, that sounds fair. I can add that, because right now, I think the agent name and workflow name are conditionally required, so that would only change the condition.
**Trask Stalnaker (Microsoft Corporation)** 15:27 I can't.
**Ankit Singhal** 15:28 Oh, one quick question here, so… Would this new span be created when I'm just invoking one single agent?
Or is this… yes?
**Max Ind (Google LLC)** 15:41 The… if you're invoking one single agent, that depends on… If there's, if the entry point to Your framework is the agent that you're invoking, if it's If it's a word…
**Liudmila Molkova** 15:56 It would be created regardless, right? That's the point of it, including Invoke Agent.
**Trask Stalnaker (Microsoft Corporation)** 16:04 But you wouldn't have an extra wrapper, you wouldn't have an invoke runner.
**Liudmila Molkova** 16:10 Right.
**Max Ind (Google LLC)** 16:12 specific.
**Trask Stalnaker (Microsoft Corporation)** 16:12 That was your question, Ankit, but you can clarify.
**Ankit Singhal** 16:15 Yeah, yeah, so I just want to understand, like, so Invoke Runner, I know, like, name is not finalist, but that's the new span that we are proposing here, right?
**Max Ind (Google LLC)** 16:24 That's the operation name for the the unified span that kind of captures The agent, the workflow, and the… Like, some entry point to a… Agentic framework that's neither.
**Trask Stalnaker (Microsoft Corporation)** 16:42 So you would only… you would only add an extra… Most scenarios won't. You're not going to add an extra span to them, but in cases where, like, ADK Runner, OpenAI Agents, Runner.
And maybe other things, which are, you know, orchestration, and pieces.
That's where you would now have a new span in your hierarchy to group those things that are under there.
**Aaron Abbott (Google LLC)** 17:22 I thought, like, last call, it seemed like we were still on the fence about always including it or not. I think Trask, you were saying maybe it's kind of like a line that has to be discussed every time about the deduplication versus noise.
Yeah.
**Max Ind (Google LLC)** 17:38 I actually got the empirical example. I have it included in the tab.
On the document, in the… there's the… 571 summary.
In the notes, and there I have, like, a… production Google agent, with all the names redacted, so that, I don't share.
No, some secrets, or… And yeah, and here, it looks pretty manageable. There is, like, not an overwhelming amount of, Invoke runner calls, so… So I was expecting it to be more robust, but yeah, it doesn't look too bad.
**Aaron Abbott (Google LLC)** 18:21 Yeah, I guess.
**Trask Stalnaker (Microsoft Corporation)** 18:22 Yeah.
But I think, Aaron, there's two different questions being discussed here.
One is whether Ankit was asking, my understanding of Anika's question is whether he's got a lot of invoke agents, right? And whether he needs to start wrapping those all with a synthetic invoke runner.
**Ankit Singhal** 18:46 Yes, and then, like… in what situation I would do that right? But probably that's also another part of it. But yeah, like, do I really need to Wrap all of them up.
under another standard.
**Trask Stalnaker (Microsoft Corporation)** 18:59 Yeah, no, you… you don't. You wouldn't.
**Aaron Abbott (Google LLC)** 19:04 Okay, cool. Yeah, I guess we, so you would include this Invoke Runner at the top level still when you enter like the harness or whatever?
It would be kind of an unconditional thing.
**Max Ind (Google LLC)** 19:16 Yes.
**Trask Stalnaker (Microsoft Corporation)** 19:17 If you have a harness, yeah, for ADK.
**Aaron Abbott (Google LLC)** 19:23 Okay, cool. Got you. Sorry, I misunderstood Ankit.
**Felix Becker (Anthropic)** 19:28 Is there an equivalent of this in the Anthropic world, or is this only a Google and OpenAI thing?
**Max Ind (Google LLC)** 19:35 I haven't seen the… So, I… I checked Anthropic World, and I… I think I only checked the… Cloud Agent SDK. I haven't checked the managed agents, and I think the managed, like, the Cloud SDK doesn't emit the GenAI spans yet. You may correct me if I'm wrong, but…
**Felix Becker (Anthropic)** 20:08 We met some of them.
**Max Ind (Google LLC)** 20:12 working.
**Felix Becker (Anthropic)** 20:13 Fair.
**Max Ind (Google LLC)** 20:13 I probably…
**Felix Becker (Anthropic)** 20:14 I, what I'm wondering is like, if, if I'm obviously not as familiar with, with the Google ADK and the OpenAI SDK.
But, I guess in the agent SDK, there's, like, a top-level, query function.
**Max Ind (Google LLC)** 20:34 Oh, yeah.
**Felix Becker (Anthropic)** 20:36 But I wasn't, before this PR, I guess I assumed that as invoke agent.
**Liudmila Molkova** 20:42 And it is. It's totally valid. That's the point that it doesn't matter the encompassing thing. You only create it when you need to, when the agent is not top level.
**Max Ind (Google LLC)** 20:58 Yeah, now that I remember, I checked the Cloud Agents SDK, and the query, kinda encompasses, like, everything in… like, everything that the query does is kind of encompassed in the… what the agent does. So… so I would say that… There's no need in the anthropic world.
To emit this.
**Felix Becker (Anthropic)** 21:18 And why does ADK and OpenAI Runner, why are they different?
**Max Ind (Google LLC)** 21:24 Yeah, so… yeah, yeah.
**Felix Becker (Anthropic)** 21:25 What cannot not be invoke agent?
**Max Ind (Google LLC)** 21:27 Yeah, so in ADK, the runner kind of drives the… Agent loop, and you have many agents, so we run into the issue where If there's an agent, and it finishes execution, but it then requests another agent to continue This given turn, or however you call it.
Then we don't have a root span for both of these agents. These agents are sibling spans.
And so that doesn't allow us to track end-to-end duration, which is… and also we have other issues where, like, compaction may happen after the agent invocation.
Or like, We have also user hooks, which can run before or after an agent. So there's… there are, like, a lot of things that we would miss had… if we didn't have this… this overarching span just for the entry point in ADK.
**Trask Stalnaker (Microsoft Corporation)** 22:28 And so, in a lot of… in a lot of other systems, you probably just have that entry invoke agent.
And that will call other agents, which will then be nested under there, etc.
This is… Slightly unique, but not, you know, super… unique,
**Max Ind (Google LLC)** 22:50 Yeah, and I think, like, other frameworks do a similar thing, but then they use a workflow terminology to, like, call this, like, Microsoft Agent Framework, I think, calls this, like, a hand-off builder, and hand-off builder Creates a workflow.
So then it feels off to then.
Like, like this under the current naming this.
Entry point would emit invoke workflow.
Instead of Invoke Runner.
**Ankit Singhal** 23:24 Max, have you also taken a look at the GitHub Copilot SDK?
just as another data point in addition to OpenAI SDK and ADK.
**Max Ind (Google LLC)** 23:35 I will check right now.
**Trask Stalnaker (Microsoft Corporation)** 23:38 That'd be interesting, because they actually do emit open telemetry.
**Ankit Singhal** 23:43 Oh, yeah, they do. They do emit open telemetry, Semantic compliant traces, and I think that's also, like, another harness that's widely adopted.
**Max Ind (Google LLC)** 23:52 That's great to… I didn't know that, that's great to hear. I'm gonna check it out after.
After this meeting.
**Trask Stalnaker (Microsoft Corporation)** 23:59 Cool.
**Ankit Singhal** 24:00 Awesome, thank you.
**Trask Stalnaker (Microsoft Corporation)** 24:03 Oh, anything… our last… comments on this… PR?
**Liudmila Molkova** 24:16 I'm thinking what could be the next steps. It seems like we tried to build some common understanding what it is. I'm not sure if we did it, but I think we went pretty deep, and I hope we did.
In my mind, the only thing that's not closed is the naming, and this is the baby.
The tricky problem.
And yeah.
I think we, like… Maybe by next time, we can think about… Operation name and, entertain options for span type and metric name.
More, and maybe create a list of possible options that we don't hate.
**Max Ind (Google LLC)** 25:03 Yes, sounds good.
I tried to find something, yeah.
**Ankit Singhal** 25:08 Oh, thank you. And one more request, like, I think if you can have some, like, just guidelines on when I would use this versus, say, workflow, when I'm orchestrating things, right? I think that'd be very, very helpful.
**Liudmila Molkova** 25:23 You use it whenever you use the workflow.
**Ankit Singhal** 25:27 Okay, so would this be a replacement for Workflow?
**Liudmila Molkova** 25:30 Yes, it replaces the invoke agent and invoke workflow.
**Trask Stalnaker (Microsoft Corporation)** 25:35 Oh.
**Ankit Singhal** 25:36 Oh, I see, okay, so if you're using Invoke Agent as an orchest… okay, for the orchestration, if you have an agent and you're using Invoke Agent Span, then you replace that with this. And if you're using Workflow for that.
then replace workflow with this spam. Right? Okay, got it. So yeah, that's I mean, if you can have this documentation or like that guideline, I think that'll be helpful whenever we can just see it out.
**Max Ind (Google LLC)** 26:01 I'm curious, does the hotel API currently… Do you specify the span type and the… Okay, sorry.
**Ankit Singhal** 26:11 No, that's the operation name only, right? Right now. No, Spanton.
**Liudmila Molkova** 26:14 Semantic name.
is there.
**Max Ind (Google LLC)** 26:16 Yeah, yeah.
**Liudmila Molkova** 26:19 Trask, you seem to be surprised by what I said about workflow.
**Trask Stalnaker (Microsoft Corporation)** 26:24 I just wanted to maybe clarify for Ankit's purposes that, I mean, workflow.name is getting moved into this common span now. So…
**Ankit Singhal** 26:39 Hmm.
**Trask Stalnaker (Microsoft Corporation)** 26:39 from.
**Ankit Singhal** 26:40 Yes.
**Trask Stalnaker (Microsoft Corporation)** 26:41 Yeah, so there still is a workflow span, it's just… A.
It's just, we're condensing into this one span type.
But there's still those 3 spans… Kind of… Different operation names can stamp different things on them.
**Liudmila Molkova** 27:03 Actually, for instrumentations, the only thing that changes is the metric name.
And you can have an extra span or you could before had an extra span as well. Just the metric name is all that you change.
For instrumentation.
**Ankit Singhal** 27:18 I see. So if I had the workflow span that I was emitting before right at some point, so would I not replace that by work runner? Now.
What?
**Trask Stalnaker (Microsoft Corporation)** 27:29 That's what I think is the interesting question, is when to… when… if we can have some guidance on when to use.
**Ankit Singhal** 27:36 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 27:36 Workflow, when do we use the workflow terminology versus the runner terminology?
**Liudmila Molkova** 27:43 She in.
**Ankit Singhal** 27:45 Yeah.
**Max Ind (Google LLC)** 27:45 I haven't… I haven't found any… any instance where runner is necessary outside of ADK and OpenAI agents so far, so… I hope that, you would default to the Er.
That usually the default to whatever the framework calls it is a good default.
And then, like, I have some… Wording in the… in the… And the semantics of given operation names, which go a bit more into detail of, like, what an agent is, as opposed to what the workflow is.
It's more or less… I think applicable to most cases, yeah.
**Trask Stalnaker (Microsoft Corporation)** 28:37 Cool, awesome. I do think we're getting there, at least we're getting the shared understanding, slowly. And then, yeah, and then terminology.
Naming.
I could.
**Aaron Abbott (Google LLC)** 28:52 Quick note, there's like this agent workflow. Yeah, in this doc, the tab agent workflow, there's like eight comments. I think myself and Felix, we left some comments there, Max, and then we added the summary one afterwards.
Yeah, there was some discussion there, but I could try to move my comments to 571 summary tab, if that helps.
**Max Ind (Google LLC)** 29:13 Okay, I'll check them out, thanks.
**Trask Stalnaker (Microsoft Corporation)** 29:20 So we're almost at time, but I wanted to.
Call out a couple of PRs.
One was this one.
This came out of the discussion, Felix, from… of what to do about the inference spans, the multiple server-side inference spans underneath one client inference span.
So, if you could take a look, we're hoping to get your feedback on that, that… Before we merge.
This one, I was… And probably we'll just take this one offline, or we'll discuss it more next Tuesday or offline. I had… just, it's looking good to me, I just had thoughts on naming, as always.
And this one, I was thinking about… so, on the metrics, the usage metrics.
I know we discussed previously about this idea of recording zero on them, because of, like, his, like, the metric views, something or other, somebody could have a different metric view, and maybe zeros are relevant.
But what I realized is that there's… kind of two categories of metrics. One category of metric where there is a single record op… a record… metric record per operation.
And those make sense to record zeros, because, like, you can build up histograms that can make sense afterwards.
But in ones where, like, modal… where you have, like, a modality.
Dimension… And you may record, you know, two, you may have to call record twice.
Basically, I don't think that You get any value from zeros on those.
Anyway, I was, I'll put together a… Something that makes more sense than my… Got it.
**Aaron Abbott (Google LLC)** 32:00 you You're talking about the counters?
The counters, for example, and the token counts.
**Trask Stalnaker (Microsoft Corporation)** 32:07 Yes.
But I… and I think there's a diff… well, I guess the… so there's the input token counter.
Oh, but even that, even that counter is broken down by modality.
So I think they're all broken down by modality, and therefore, I feel like zeros Don't have any meaning that are not useful on any of those.
**Liudmila Molkova** 32:41 Yeah, I think we added the… we decided to set zeros on counters, because We thought that maybe there are some scenarios depending on aggregation, and that we can set exemplars and counters as well in theory. And it drove the decision to put zeros.
I think it's so advanced.
And it raises so many issues like this one with, yeah, you like, do you set it up with each modality or with a known modality? And then it's impossible to interpret.
**Trask Stalnaker (Microsoft Corporation)** 33:23 Yeah, and then you would have to stamp… Anyway, I'll put together, maybe, either an issue or a PR, and I'll try to lay that out.
Clearly, somehow, it's… kind of starting to make sense in my mind, but I obviously can't explain it. It doesn't make enough sense for me to be able to explain it clearly yet, but… Yes.
Alright, anything, anyone… really wanted to… Call out Felix.
**Liudmila Molkova** 34:06 Why do you need to bring it up?
**Trask Stalnaker (Microsoft Corporation)** 34:12 Thanks.
**Liudmila Molkova** 34:22 Felix, tell us a joke or like how serious you are about this idea.
**Felix Becker (Anthropic)** 34:27 Oh, I mean, half serious. I feel like, the… the fact that it's named GenAI was one of the first things that… seemed a little weird to me when I first, saw the conventions.
Because.
Having them be Gen AI, like generative AI, kind of implies that there is another thing that's non-generative AI, and these conventions only cover generative AI, and not the other thing that's not generative AI.
And not cover the whole of AI.
And I feel like that's not actually… True for.
For the… for the app… for the conventions, right? Like, they're trying to cover… model any AI, and pretty much any, like.
Isn't like all AI generative AI? Like, they're all kind of token machines under the hood.
So, I think in my experience, The… I don't hear any, like… Frontier Labs or any, like, companies very seriously in this space calling it generative AI as much as just AI. It seems more like, kind of, speak that consultancies use, or, you know.
Company's not as much on the frontier.
And so…
**Trask Stalnaker (Microsoft Corporation)** 35:53 To use Ludmilla, to use your phrase, it's so 2023.
**Felix Becker (Anthropic)** 35:59 Yeah, so I just wanted to bring it up, because I feel like with the Stabilization effort, and now, while it's still in development, this may be, like, the very last chance to ever even discuss it, and then afterwards, it's probably, like, you know… just be silent and accept that this is just how things are. But sometimes I have a little bit of FUD that actually, like, people are turned off by when they see the conventions, and they're like, oh, GenAI, this doesn't seem like designed by people who, you know, are really on the frontier of the space, or maybe know what it's about, which, you know, I'm not saying I believe that, but… That's how it can come across.
It's also shorter.
**Trask Stalnaker (Microsoft Corporation)** 36:51 Well, we've broken everything else, since the last release, Ludmilla.
**Liudmila Molkova** 36:56 No, it didn't rename a single attribute.
Oh, maybe at 1 or 2.
This would be rename everything.
**Felix Becker (Anthropic)** 37:12 I mean, has there ever been, was there ever a discussion on the naming? I'm curious. So like, what do you guys feel about it?
**Liudmila Molkova** 37:18 They used to be called LLM, you know, LLM dot, so we are not… it was 2023, so we are 2024.
Sarah Graff.
I, I mean… I don't know.
And if people think that's what we should do, Provision.
**Trask Stalnaker (Microsoft Corporation)** 37:41 Throw it out on Tuesday… let's throw it out on Tuesday.
as a… topic get… People's thoughts on whether people are…
**Christopher Cordi** 37:51 the whole conversation on Tuesday.
**Felix Becker (Anthropic)** 37:55 It would definitely be, you know, a breaking change for… Platforms that use it now.
it could definitely also be something where, like, you know, we just launched, like, 12 launch partners, you know, like, the biggest platforms where I could talk to everyone, like, hey, would you all, like, you know, accept the new names, too? And then it's basically only on writers slowly upgrading, because all the major platforms would already accept it. So it may be a way to, like, orchestrate this across the ecosystem.
That it doesn't actually feel super breaking. But it may, yeah, it may also have been, like, the last time to do it, and just, like, if you think about this in 5 years, would you think back and be like, man, I wish we had just… Done that at the very start when it was still possible.
**Liudmila Molkova** 38:52 Yeah, and I mean, if everybody by Tuesday gets comfortable with the idea of updating all their partners, the update is kind of trivial, right? And everybody, all the backends would… Probably have a lot of layers of compatibility.
**Felix Becker (Anthropic)** 39:10 You could even, in the, like, writing instrumentations, you could have some, like.
Legacy NFAR that, like, toggles it to, like, a legacy name mode.
Just temporarily, so that, you know, you can still upgrade to the latest instrumentation if you can't switch the names yet.
We used to have that.
**Liudmila Molkova** 39:30 Drop them in the new version.
**Felix Becker (Anthropic)** 39:33 Huh?
**Liudmila Molkova** 39:35 We used to have the toggle. We dropped it in the new versions of.
**Trask Stalnaker (Microsoft Corporation)** 39:38 Oh, for LLM.
**Liudmila Molkova** 39:39 information.
Not.
**Felix Becker (Anthropic)** 39:41 What was the context behind the rename from LLM to GenAI?
I feel like LLM is actually maybe.
Better than Gen AI.
**Liudmila Molkova** 39:49 Multimodals, sorry, modalities, multiple modalities.
**Felix Becker (Anthropic)** 39:56 Yeah, that makes sense, I guess. Like, so to model images and videos and like that sort of stuff.
Yeah.
**Liudmila Molkova** 40:06 And small language models.
We don't want.
**Felix Becker (Anthropic)** 40:09 Fair.
**Liudmila Molkova** 40:11 Limited to a large size.
**Felix Becker (Anthropic)** 40:18 We've done it before, so that makes me feel a bit better.
Yeah, let's discuss it on Tuesday, I'm happy to… Sleep on it. Sleep on it.
**Trask Stalnaker (Microsoft Corporation)** 40:30 Yeah.
Alright.
I'm… I'm always in favor of having these discussions, like you said, like, that's the… the time… That we can do it, possibly without… yeah.
And be defensible, depending on… Yeah, question of how many people will be mad at us for… Changing it, but, we… Yeah, it's… Let's sleep on it.
Have a good weekend. On that note…
**Liudmila Molkova** 41:12 You too.
**Trask Stalnaker (Microsoft Corporation)** 41:13 Yeah.
Bye, y'all.
**Liudmila Molkova** 41:15 you.
**Max Ind (Google LLC)** 41:16 Bye-bye.
**Mikolaj Knap (Google LLC)** 41:17 Bye.
