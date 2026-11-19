SIG: GenAI Semantic Conventions and Instrumentation Stability
Date: 2026-11-16
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Mikolaj Knap (Google LLC)** 00:52 Hello.
**Max Ind (Google LLC)** 00:54 Hello?
**Liudmila Molkova** 03:40 Hello, hi everybody.
**Mikolaj Knap (Google LLC)** 03:42 No.
**Max Ind (Google LLC)** 03:44 Hello?
**Liudmila Molkova** 03:45 Thanks for waiting.
I don't know if Aaron or Trusk are around… But we can get started!
I'm gonna shut… Okay… Oh, Erin is here. Hi, Erin!
**Aaron Abbott (Google LLC)** 04:23 Hey.
Everyone.
**Liudmila Molkova** 04:27 Okay, please add your name to the agenda. I, Let's see what we have. Dude, the… we have a lot of PRs.
to review, and I posted them here.
I think, Max, you added this, should we probably… Start here.
**Max Ind (Google LLC)** 04:48 Sure, and… Yeah, I thought about the isNested a little bit.
And I think right now, this would only… Make any sense on the duration metric?
And I just have, like, some second thoughts that, like, maybe… Introducing this just for the duration metric is kind of like a… Not worth it, because the duration, in most cases.
I think that, like, most platforms or whatever, could do fine with just the HTTP server duration, mostly, and the FastAPI added the Metrics by default now?
So… I kinda don't see that much value anymore here. And also, like, the original idea with this was to also track end-to-end token usage.
With, like, a metric on the invoke agent.
And now it seems that there are, like, other alternatives and better alternatives than tracking end-to-end tokens on the Invoke agent.
And one of these alternatives is the main agent name.
And I came up with, like, a different alternative, which is, like, the 703 issue.
which… which I'm happy to get into, but… but I… I'm… I'm wondering if, if this, is nested can be… can be parked for a… for a while. I know that this is, like, a blocker for destabilization.
So, so I'm wondering… Okay. Yeah.
**Liudmila Molkova** 06:39 this metric would not necessarily come under HTTP, right? You can… it can be under gRPC, it can be in your hardness.
local. So, like, if we are going to… In a generic application, where you would build a dashboard, or… Just any Agentic-specific analysis would… Need to assume there is something above it.
**Max Ind (Google LLC)** 07:07 That's true, that's true.
**Liudmila Molkova** 07:08 It won't be, like, you wouldn't be able to build any generic dashboard or generic experience for agents.
**Max Ind (Google LLC)** 07:16 That's true, that's true.
And that is right, but also there is nested. It seems like there's, like, a lot of, Like, like, it seems like it's a novel… idea?
For not much gain, which is just the duration.
It may be… it may be, worth it, but I just, like, I have some second thoughts.
Because, like, for our use… yeah, for our use case, which is the agent platform, I would… I think that, like, the… capturing the end duration… capturing the end-to-end duration with just the HTTP server, And… would be… Fine enough, and then the generic use case.
Like, I'm happy to hear if… if there are other people that… want to capture and duration, but, like, just basing it off of our use case, I don't think that, it warrants the… all of the complexities that come along with the… with this nested.
**Liudmila Molkova** 08:23 The HTTP duration, even if you use it, it does not include any GenAI context. It wouldn't include agent name, it wouldn't include I don't know, model.
**Max Ind (Google LLC)** 08:34 if it's.
**Liudmila Molkova** 08:35 applicable. It would also include the HTTP requests that are, all of them, Agentic or not, so whatever duration that somebody would measure, would be skewed. And also, if you have the Agent platform and HTTP agents, it would also have the problem of well, it's the same problem with this nested, that it's just the local route, not the agents across. I just don't feel like any protocol-level metric can be a replacement for this. You cannot, like, build a dashboard for agents that is based on HTTP duration.
**Max Ind (Google LLC)** 09:15 That's true, that's true.
Yeah, I'm just wondering if… so this would be a blocker for… like, whether we include this attribute or not, this would be a blocker for stabilizing this particular metric, right?
**Liudmila Molkova** 09:32 Yes, because adding an attribute to a metric is a breaking change.
**Max Ind (Google LLC)** 09:36 Okay, okay. And so, from what I gather, this would be the only metric that would have this attribute.
The duration metric, right?
**Liudmila Molkova** 09:46 So for this one, there's two friends… discount only things that are in immediate… immediately done by this agent, so it doesn't make sense at all.
Yes, yes.
**Max Ind (Google LLC)** 10:02 Okay, do we know how it may be implemented? Because this, Yeah, I mean, this would require taking a dependency on the GenAI utils. In ADK, we're fine with that, because we… We're gonna have to do that anyway to solve a different issue.
Yeah, but anyway, but I think that's, like, yeah, if, like, the direction… like, Yeah, so sorry, I just had, like, second thoughts, and, like, it seems that, like, the… My second thoughts are, like, not shared.
Here, so I'm, like, I'm… I'm very fine to be reassured by the, by, by Liudmila and then to go forward with this.
**Liudmila Molkova** 10:53 Awesome. Yeah, and I think that the only thing that's remaining Is the naming, and we talked about the request.
Like, being problematic.
**Max Ind (Google LLC)** 11:04 Yes, yes, so I'm gonna put something together for the naming for the… for the Wednesday, because for… for last week, I was unclear whether this would… Go in its current shape or not.
But now, now I can, I can prepare something for Wednesday, yeah.
**Liudmila Molkova** 11:23 Awesome.
Thank you.
Cool, and 703… Can you give a quick overview?
**Max Ind (Google LLC)** 11:34 Yes, the overview, and actually there's the HTML page at the bottom that kinda, like, That, like, visualizes it?
better than I could explain with my words. So this is basically, like.
It seems like, from our last meeting, that the… End-to-end token usage for agents would piggyback off of the main agent.
Kinda idea. And the alternative… Like, the limitation that we agreed on is that this would only count the end-to-end token usage for the main… one main agent, basically. And all of the main agents in the middle, they would… you would not be able to count, like, sap tree.
Token usage.
With the main agent approach.
So… what… I, and I actually, like, like, what AI mostly came up with, is, this, like, roll-up metrics.
Is basically, like, instead of storing in the context just the main agent, you store the entire lineage, or, like, the entire call graph, and then you record the… a separate metric, which has the… which you record the point for each agent in the… in the lineage, basically.
And so what this does is this means that the metrics would have lower cardinality, and also you could, have, you know, you could have… you could query a subtree.
Of the… Of, like, an agent call graph, and you can get end-to-end token, End-to-end token usage for this subgraph.
Is that true?
**Liudmila Molkova** 13:29 Seven.
whenever we're doing Work Agent, where… Record.
Duh.
Measurement for this metric for each Agent in the tree.
**Max Ind (Google LLC)** 13:47 No, whenever you do inference, whenever you do inference, you record it for each agent.
**Liudmila Molkova** 13:54 Oh, okay.
And then, it's a counter.
Not, not to…
**Max Ind (Google LLC)** 13:59 Instagram. Yes, yes, yes.
**Liudmila Molkova** 14:02 Okay, interesting.
What?
Why do we… Where do we need it? Because then… If we just… oh, because if we stay in main agent, we are only recording it for the current agent and the main one. I see.
**Max Ind (Google LLC)** 14:19 Yes, yes. And also, this metric… there are other nice things that happen here, is that, like, you get metrics that have lower cardinality, because the agent name is, like, a high cardinality attribute, and also It removes the unclarity with the main agent.
Name what it should be, so… Right now, it's, like, it cannot be… for example, like, a root ADK agent, because it's kind of, like, supposed to be, I think, like, a resource attribute, which is stable across And vocations, and also it clears up, like, what do you do with the… A2A server that is, like, deployed on… Agent rundime, for example, because… Agent runtime has a display name, and A2A has an agent name, and then ADK has an agent name, so there are, like, there's, like, at least 3 candidates for what the main agent name can be, and this, like, squats it in that? The main agent kind of forces there to just be one main agent name.
And that example is also lower down in the… And this HTML page.
**Liudmila Molkova** 15:35 I see.
**Max Ind (Google LLC)** 15:36 I think it's… yeah, it's under… yeah, it's right here, yeah.
**Liudmila Molkova** 15:43 And for this, we can kinda… Provide some guidance on what… what is it?
**Max Ind (Google LLC)** 15:54 That's true, that's true, but then, like… This means that, like, only one… perspective, basically… Like, only one question can be answered, so here, like, And… If someone looks at agents, and their agents are named after the A2A agent name, then these… they would be… then we would, like, basically only… they would only be able to know the end-to-end token usage if they're using the A2A agent name. If they use the… Agent runtime? Agent name, they wouldn't be, and if they use the ADK agent name, they also wouldn't be able to.
To answer this question.
**Liudmila Molkova** 16:41 Choir.
Yeah.
**Aaron Abbott (Google LLC)** 16:49 If you go back to the top, yeah, right here.
I didn't understand, Max, like you said, there's two things I didn't get.
Why do we need to store it in context and then have this, like, reconciler record? If they're just counters.
Can we just record these, like, when the sub-agent executes directly.
**Max Ind (Google LLC)** 17:11 You can… yes, you can record them when the sub-agent executes, but then you need to… Then you kinda need to count, the token usages at the… Like, you need to aggregate the token usages for each inference at the agent level, and… You don't need to do that. Another reason why we do this here is because under a single agent invocation.
there are many inferences, and there… the many inferences can actually use different models. So if you recorded one data point.
At the invoke agent, then we would lose the model name.
**Aaron Abbott (Google LLC)** 18:00 I mean…
**Max Ind (Google LLC)** 18:00 So…
**Aaron Abbott (Google LLC)** 18:00 If you… if you have, like.
**Max Ind (Google LLC)** 18:02 separate.
**Aaron Abbott (Google LLC)** 18:02 metric like this, like the roll-up metric, that seems… fine to do that, you just wouldn't record the model. Like, I… They seem like the same thing to me, but maybe I'm missing something.
**Max Ind (Google LLC)** 18:13 Oh, like, the model is necessary because, you wanna also know, like, the… Hmm, I'm actually… Yeah, I'm now curious if the model is necessary, because… Without the model, you wouldn't be able to answer, like, what this, like, root agent How many tokens of each model it used. Or, like… any… with… while including the location, you would only be able to answer the question of, like, what's the direct usage Of a, of a given agent, but without delegation.
Okay. That may be okay, but I don't see the… I don't see any drawbacks in recording this at the inference level.
**Aaron Abbott (Google LLC)** 19:04 So what are we…
**Liudmila Molkova** 19:05 You can… you can record it at the… Like, in the middle.
Or anywhere, like… For anything that's not immediately using, because the sub-agent would not return the number of tokens it used.
**Max Ind (Google LLC)** 19:29 Yes, possibly.
**Liudmila Molkova** 19:33 Like, I mean, you can probably hack it around in one SDK, but if there is, like, some cross-SDK story, you would need some contract for agent to return to the parent how many tokens were used.
**Aaron Abbott (Google LLC)** 19:55 And yeah, I also didn't… Sorry, I didn't really get.
**Max Ind (Google LLC)** 19:58 Yeah, go ahead, sorry.
**Aaron Abbott (Google LLC)** 19:59 lineage. No, sorry.
**Max Ind (Google LLC)** 20:01 No, no, no, the lineage, no. The lineage is basically just the call graph. Like, it's… It depends. So, it can be the call graph, or it can also include the delegation. I think the delegation might be a bit more complex to do with the context.
But the… basically, the lineage following the trace… so in the summary example.
Or, like, this is the same example. So, basically, the storefront calls the catalog, which calls the checkout, which calls the reconciler. And at the reconciler inference span, the lineage would basically include the… all the agents which were… which were invoked right up until this point, right?
So, that would… and then, if you record the inference roll-up metric.
At the reconciler, then you would know, okay, how many tokens was the storefront and the catalog and checkout ultimately responsible for, like, including the agent delegation.
**Aaron Abbott (Google LLC)** 21:05 Okay, I see. So, like, where it says, and record these metrics on the right in this proposal, we would have the lineage, attribute as well, stamped on there with the…
**Max Ind (Google LLC)** 21:15 No, no, no, the lineage is only in the context. So, the lineage is not stamped on the metric, it's only in the context, and then for each element in the lineage, you'll record the separate Separate point in the… in the roll-up counter.
**Aaron Abbott (Google LLC)** 21:32 Okay, okay, I see.
Okay.
Sorry, and then one last question was the cardinality thing you mentioned, it being lower cardinality. Is that because we don't store the lineage, like you said?
**Max Ind (Google LLC)** 21:46 No, it's because this wouldn't need to store the main agent name.
This only needs to store the agent name, and then if you need… if you want to know the end-to-end.
token usage, you just, query the roll-up metric by… with the filter on the… where the main… where the agent name for the roll-up metric equals the main agent name. So…
**Liudmila Molkova** 22:15 So it's, like, sparse. So, recording the main engine attribute would record all the permutations of Main Agent plus subagent.
And here, it's just, like, the one Agent thing.
**Max Ind (Google LLC)** 22:28 Yes, yes. And the agent name can be the main agent name, it's just not spelled out.
And it can have, like, an additional boolean to signify if the given roll-up records What happens to be a main agent, and then you can identify what… with, like, little cardinality.
Overhead, yeah.
**Mikolaj Knap (Google LLC)** 22:53 Yeah, I was… I was gonna say, how would you know what the main agent name is, if you don't… Have something to signify it, so…
**Max Ind (Google LLC)** 23:02 you can join on it from other sources, but I don't know, we could go with the Boolean, I don't know.
I… yeah.
**Aaron Abbott (Google LLC)** 23:13 Okay, I'll take a look at the thing offline, too, but thank you.
**Max Ind (Google LLC)** 23:18 Yeah, thanks, yeah, but this, anyway, this seems to go… Way in the opposite direction of where… Like… Where it seems that we were going, which is, like, stamping main agent name on all metrics.
So how… how feasible?
Do you all think this, this can be?
**Liudmila Molkova** 23:41 I don't know if it's going in, like, completely opposite directions, so, Penny, to the, previous question of how do you know what main agent is, and which of those metrics you want to show.
maybe the main agent can be an attribute, and I get the permutations, but there… I would not expect, like.
that… A lot of different agents run under multiple… main agents.
Maybe, but, like, in practice, within one project, or one…
**Max Ind (Google LLC)** 24:20 That's it.
**Liudmila Molkova** 24:20 destination? Probably not.
Yes.
**Max Ind (Google LLC)** 24:24 This is actually the case in Google.
**Liudmila Molkova** 24:27 Hmm.
**Max Ind (Google LLC)** 24:28 Where… yeah, no, no, no, where almost every agent runs under the same root agent, always.
And the one exception is Gemini Enterprise, and Gemini Enterprise basically, basically, they're, like.
Almost as many root agents as there are, like, sub-agents, and… this is quite mixed up. It's not, it's not very, very stable. That, like… so, so I, I think that, like, the… Cardinality.
is basically a… like, we gain basically no cardinality if we remove Gemini Enterprise from the list, but then when Gemini Enterprise is added back, then this metric, like… Starts to have, like.
some, benefit when it comes to cardinality. I removed the numbers from the public doc here, but I can share them.
Show them offline.
**Liudmila Molkova** 25:32 Wouldn't it be the case anyway because of the resource attribute that we would put?
So, in platforms, we would also have the main agent ID on the… under a source.
**Max Ind (Google LLC)** 25:51 Yeah, I'm not… So I don't know, but the main agent ID… I don't know, the main agent ID is right now a part of any monitored resource.
at Google.
But I know, like, a very small sliver of monitored resources at Google.
**Liudmila Molkova** 26:15 In general, if you host agents, we would expect the main agent ID to be a resource, an entity, and then this metrics would be reported under it, and they don't need to even include main agent name, because it's… on the resource.
Maybe. But anyway, so I think, like, maybe the approach I would explore is that There is an agent name, maybe in some form, there is a main agent name.
And things in between are… let's say, can be additionally configured, or maybe a default behavior, but, like, I don't think it's completely opposite directions, just the different, slightly different way to take the same direction.
This is pretty cool.
**Max Ind (Google LLC)** 27:13 Okay, sounds, sounds good. I can… I can work on, Proposal for this, to, like, actually see if anything can come from this.
**Liudmila Molkova** 27:26 Nice, thank you.
**Max Ind (Google LLC)** 27:28 Yeah, thanks.
**Liudmila Molkova** 27:30 Okay, we have a couple of minutes left, so we don't make a lot of progress. I think there are a couple of things… So this one is from urine.
And I switched to the new AI-focused view for GitHub. I have no idea where things are in this UI yet.
But it seems it's almost good to go. There are some minor tweaks to do. I approved.
**Aaron Abbott (Google LLC)** 27:56 Okay, I'll touch it up, thank you.
**Liudmila Molkova** 27:59 Yeah, thanks.
And… Just to recall, we are… We were discussing not having it optional, so, like, type.
Like, any off type would disappear, but it's the separate viewer.
Great.
**Aaron Abbott (Google LLC)** 28:22 Which threw it?
**Liudmila Molkova** 28:23 Let's see… So this friend.
So… This is how it appears in JSON schema, and we can figure out how to drop this part, because it's unhelpful, and nobody does it. Well, most of the schemas don't do it.
But it's a separate PR, I think you were saying.
**Aaron Abbott (Google LLC)** 28:49 Okay.
Yes.
Sorry, I'm trying to remember what was going on here.
It's not near that.
**Liudmila Molkova** 29:00 So maybe my… I made a.
**Aaron Abbott (Google LLC)** 29:02 Oh, right.
**Liudmila Molkova** 29:02 And how to do this, and it seems it's not the perfect one.
**Aaron Abbott (Google LLC)** 29:06 Yeah, yeah, so the separate PR, to be clear, would make… it would make the… None versus missing, like, all of those would be kind of unified, right?
Okay.
**Liudmila Molkova** 29:17 Right, yeah.
Yep. Right.
**Aaron Abbott (Google LLC)** 29:20 Sounds good.
**Liudmila Molkova** 29:23 Cool.
Okay, and then, I don't know, did anything happen last week?
On this front… Oh, you approved her, awesome.
**Aaron Abbott (Google LLC)** 29:35 Yeah, I approved this one, like, actually a while ago, and then Felix… replied, and I'm… I'm… I need to get back to him still, but basically it was… he was surprised that I approved this one. He was like, I liked it better when there was two separate attributes.
Rather than having one attribute with two… Fields inside of it, and… I… I think you had the same reaction as me, and I'm trying to articulate why I had that reaction back to him.
**Liudmila Molkova** 30:03 Yeah, I think Trask, articulated Why we all seem to have the same reaction.
I don't know if it's in the notes, I don't think so, but probably somewhere in the recording from the post call.
**Aaron Abbott (Google LLC)** 30:22 Yeah.
**Liudmila Molkova** 30:27 Cool, so then I'll take another look at this one.
And I want to approve it with maybe some minor pivots.
Cool. Okay.
Cool, Dan, thank you for coming.
Excited to see y'all.
**Aaron Abbott (Google LLC)** 30:47 Thank you, good to see everyone again.
**Liudmila Molkova** 30:49 Thank you.
**Max Ind (Google LLC)** 30:49 Yeah.
**Aaron Abbott (Google LLC)** 30:50 Peter.
