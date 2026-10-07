SIG: GenAI SIG
Date: 2026-10-06
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:03:38 Hi, everyone.
Josh Bonczkowski 00:03:40 Hello.
Endre Sara 00:03:46 Thank you.
Trask Stalnaker (Microsoft Corporation) 00:03:53 I was Ludmila, I was thinking of volunteering Aaron to drive the meeting.
Liudmila Molkova 00:04:01 Okay. He's not here yet. Yeah.
Trask Stalnaker (Microsoft Corporation) 00:04:04 Yeah, that's a problem.
Liudmila Molkova 00:04:06 Okay.
Okay.
Okay, while we're waiting, if people want to add things to the agenda… Please go ahead, I'll paste the link here.
And we'll just continue the agenda from the previous call.
So I'm thinking I want to keep talking about agent versus workflow.
Max Ind (Google LLC) 00:05:20 Hello? Hello?
Liudmila Molkova 00:05:24 Hello.
Trask Stalnaker (Microsoft Corporation) 00:05:33 All right, I will volunteer myself now.
Alright, so let's kick off… Agent versus workflow discussion.
Liudmila Molkova 00:06:20 So yeah, I think we kind of have two parts.
of the problem.
The… There is a PR from Max, the 571 Which adds another operation.
that… Is the… the main agent.
Right? It's not… it's neither in Voke Engine nor in WorkWork Workflow. It's a third one, which is the outer most of them.
And I'm thinking… if we can… make it… Replace the Invoke Agent and Invoke Workflow.
All together.
Trask Stalnaker (Microsoft Corporation) 00:07:14 All together, meaning also in these lower steps?
Liudmila Molkova 00:07:19 Right, the lower steps will keep their operation name.
They will keep the… Agent or workflow specific attributes.
So you can tell by looking into them.
That they were done by agent or done by workflow.
But the metric name and span type would be the same for them.
Plus, we will have means to distinguish The outermost.
Operation in some way.
Max Ind (Google LLC) 00:07:58 What's that mean? What's the mean to distinguish the outermost operation?
Liudmila Molkova 00:08:04 Sam attribute.
Max Ind (Google LLC) 00:08:06 Mmm.
Liudmila Molkova 00:08:08 Or… So, in the draft PR I have, it's a little bit subtle, but the main agent Appears on the nested and not the outer and maybe it's too subtle.
Max Ind (Google LLC) 00:08:27 Yeah, so the.
Like the motivation for handle turn was, I think the fact that The agent which initiates the… The turn, as to say.
May hand off its work to some other agent.
And then there is no one root span.
So then… From what I gather, you're proposing to have Still a root invoke agent span, but then this invoke agent Span the notes… The execution kicked off by this.
By this initial agent, I guess.
Liudmila Molkova 00:09:18 I'm proposing the same… It's, hierarchy… Like, in the number of spans, as you… it's just that they have the same span type and the same metric name, with some distinguishing factor.
Max Ind (Google LLC) 00:09:32 Yeah, and the… this, and the spam name is… What would that be?
Liudmila Molkova 00:09:40 It can be specific to the agent or workflow. So it can be invoke agent in one case.
And then local workflow in another.
Max Ind (Google LLC) 00:09:55 Hmm, so then I'm curious if, like, what… should then be a workflow. Because right now, the… I think… NADK because.
And.
We kind of don't know if an agent is gonna hand off Control flow to another agent.
Then we just root everything.
In a workflow.
But then I think workflow is… To specifically, because we also have Workflows… Which are a different thing, which is like a graph-based workflow where an agent.
Where, you know, you can have nodes, and the nodes kinda… the output of one node is the input to the next node in the graph.
So, the kind of worry is that, like.
If everything is a workflow, then nothing is a workflow.
And maybe the root span could be an agent, but then I think we would deal with the fact that There are two spans named Invoke Agent, Main Agent Name.
And in some cases, this would, these would be equal.
And that's, this would be confusing that, like, it would seem as though, like, an agent calls itself.
Liudmila Molkova 00:11:15 Do you see the outer? It would be a turn. You don't need to decipher. It's an agent or workflow.
The operation name, you can… we can call it turn, we can call it run, we can call it…
Max Ind (Google LLC) 00:11:28 Okay.
Okay.
Trask Stalnaker (Microsoft Corporation) 00:11:30 So you… we're still proposing to introduce a new concept, which is a turn.
Which is… The top level something… Would you…
Liudmila Molkova 00:11:45 There's a… I think about the turn.
As.
If agent… if Agentic Flow, Agent Workflow, anything, if Agentic Flow produced something.
The output it gave to user, like the the the final output for this round, this turn, it's a turn.
It's… like, if we say, okay, it's only the outermost, then we're already in the weeds of… What is a turn? Why subagent turn is not a turn? What if it's remote? What if it's executed directly? And so on, like… but essentially, I'm thinking about the turn as we use it, or run that.
One execution of an agent is a run, or one execution of a workflow is a run.
Trask Stalnaker (Microsoft Corporation) 00:12:35 What if the… if it's just the simple case of a single agent, and you're just… Would you… not have the handle turn at the top? Would it just… would you ever just have invoke agent directly, or would that always be under a turn?
Max Ind (Google LLC) 00:12:58 I could probably… I would say that, I would say that it could be opt out.
And, like for frameworks that can reliably tell.
That, That an agent invocation is just 1 agent and there won't be an agent handoff, then we may.
Then we may not have this span be default on, maybe.
Definitely have an opt-out, yeah.
Trask Stalnaker (Microsoft Corporation) 00:13:33 Yeah, let's go to Anne Ankit.
Ankit Singhal 00:13:37 This new turn span, how would we know when the turn ends?
Especially when it's calling, like, nested agents.
Max Ind (Google LLC) 00:13:45 I would say that it ends whenever the trace ends.
It's kind of.
Ankit Singhal 00:13:54 No, that doesn't make sense, because when a handoff happens, right? Say, for one invoke agent… one agent invokes the other and does a handoff, and… Great.
It relinquishes the control, right? And now the other agent has the control, and then it's gonna do something for you. Sometimes it might respond to you, and sometimes it might just do a schedule, like an offline task, like, okay, send an email, right, instead of replying to me. In that case, you're not even getting the control.
Liudmila Molkova 00:14:23 So it disrupts the client, the framework method. When the framework method returns the output to user, then it's when it ends. If it's streamed, when the stream ends.
Max Ind (Google LLC) 00:14:44 Yeah, that sounds more reasonable than what I said, yeah.
Ankit Singhal 00:14:47 So we could do that and I think we missed some of our decisions.
Liudmila Molkova 00:14:53 So for the internal… agent. It's essentially where the agent responds. Response could be, okay, I scheduled the task.
And it's when the corresponding… if we're thinking about it as instrumenting framework method, this is when the method returns, or when the stream that this method The return ends.
Ankit Singhal 00:15:21 Would we have that information, like, when that happens, at the time when we are… at the place where we are actually… Starting.
Liudmila Molkova 00:15:29 We're instrumenting this metaphor, right?
Ankit Singhal 00:15:30 Through a different.
Sorry?
Liudmila Molkova 00:15:33 We're instrumenting this method so we know when it completes.
Ankit Singhal 00:15:45 I see, and this one would be only for the internals.
Or also for like cadence.
All the remote agents being called.
Liudmila Molkova 00:15:57 I think we have a wiggle room for remote agents. Maybe we decide for internal, and then we see if we need.
Ankit Singhal 00:16:01 to be changing the.
Liudmila Molkova 00:16:02 For the clients?
Ankit Singhal 00:16:04 Yeah, I think for the internal one, I think it's probably… Possible, right, to figure out.
But for the remote one, I'm… 700.
Unsure of.
Trask Stalnaker (Microsoft Corporation) 00:16:20 Nikhil.
Emil F 00:16:29 Is it possible that you're calling me Trask?
Trask Stalnaker (Microsoft Corporation) 00:16:32 Oh, Nikhil, is next in the hands up line, but we can't hear you, Nikhil. I saw you come off mute, but…
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:16:47 What now?
Trask Stalnaker (Microsoft Corporation) 00:16:48 Yeah.
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:16:49 Okay.
Wrong Microsoft.
Alright, so I was just saying, I was just catching up on this PR, so, maybe it's already answered. So, I have two questions. One is on the… So, why isn't the invoke workflow, sufficient to, represent the entire handle turn.
So that's question one. And then the question 2, building upon what Ankit said was, So, the, the handle turn, If we are saying we only wanted to represent the internal, like, internal invocation, so… Would… Do we want to, when the… So, when the handoff occurs, are we proposing that we propagate the handle turns parent context downstream. So is that the idea we're proposing?
Max Ind (Google LLC) 00:18:02 Yeah, for the first question, which is, like, the… why the invoke workflow is not sufficient, the… the issue is that… If we… Like the status quo in ADK is that the normal agent handoff.
We call that a workflow, but we also have a graph-based workflow, which is kind of the same as the regular handoff.
Which is… and we also call that a workflow in observability. And these two concepts are very different.
And we call them the same thing, and this leads to some confusion, which is Yeah, which is the… The motiva… initial motivating… A factor for this.
This third operation name.
Which is kind of more abstract and kind of doesn't go into if it's a workflow that handles the request, if it's an agent.
And.
On the second question.
Sorry, could you remind me of the second question? Oh, sorry, it was about the context propagation, right?
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:19:11 Yeah, so when, it… So, ideally, we see that we want the, you know, like, invoke agents, or, you know, like, the inference calls, or the… or things, so they kind of ideally line up against the… against the specific invoke agent that, you know, initiated it. But in case of a handoff, so are you proposing the.
Handle turn be the context that's getting propagated, and not, like, the workflow or the, or the parent invoke.
Max Ind (Google LLC) 00:19:54 Yeah, I would say that. So for local, like within the same process, context propagation.
I would say that yeah, for handoff, the handle turn should parent.
All of the agents?
And for the remote… Hand off.
That would require cross-process context propagation, and I think the… Conclusion from the last meeting is that we can handle this later, so I think that what I gathered is that We already, at some point, need to… Propagated the main agent.
In context, so… The turn at some point would, I think, it could just have a Like a predicate that if A main agent is in context, that means that… voviktsybulskyi: If isn't the cross-process context propagation.
If the main agent is in the cross-process context propagation, that means that it's… that this remote subagent is already part of another turn, so it wouldn't create luisdel van der another turn span. But initially, I think the… it's fine that Every… Remote subagent would also create the turn.
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:21:15 So if every remote sub-agent created its own handle turn, but… So are we trying to define handle… so we were trying to define Hamilton as the, like, a Uber… Uber's plan to capture the entire turn, right? So… but we are saying it is… for the time being, it's okay to have sub-agents also have their own Hamilton.
Max Ind (Google LLC) 00:21:37 Yes, yes, in lieu of the cross…
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:21:41 aircraft.
Max Ind (Google LLC) 00:21:41 Trust process context propagation, yeah.
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:21:44 Alright, thanks.
Max Ind (Google LLC) 00:21:46 Thanks.
Trask Stalnaker (Microsoft Corporation) 00:21:49 Emil.
Emil F 00:21:54 Okay, I guess I'm… I'm still stuck up a little bit on the idea of what is the, like, the… semantic difference between the handle turn and the trace. Like, both are items that group operations in a tree.
What would it mean, like, what information would we convey by having multiple traces inside of a handle turn?
Or the other way around.
Max Ind (Google LLC) 00:22:22 I think that… One handle turn shouldn't have multiple traces inside.
But I think the, the… I think the utility that is span.
It's trying to serve. It's the fact that A single call to an Agentic application may not create a single trace, so The example with the agent handoff.
If there is no parent span for the agent handoff, these would create two traces. And then at this point, you can't track the end-to-end duration of an agentic system, and you can't track the token usage of the agentic system. So this is where the need for an overarching span comes from.
Liudmila Molkova 00:23:08 But also, like, in a trace, there could be multiple spans, nothing, and up until Metry says that the… The handle turn or whatever we call it is the root span. We need to identify this span somehow, and we need to define it so it has clear semantics.
Max Ind (Google LLC) 00:23:26 Oh yeah yeah.
Yes.
Liudmila Molkova 00:23:28 Traces are orthogonal to… A span. Well, trace consists of arbitrary spans.
Emil F 00:23:38 So the idea is that that handle turn would be the root span for the AI activities or.
Liudmila Molkova 00:23:43 No, no, no, no.
Emil F 00:23:44 ultimately.
Liudmila Molkova 00:23:44 It is… it is S-Pen, right?
It can be a root span in a trace, but most likely it's not.
Because something initiates it, and this something creates its own span, and maybe a lot of things before it. There could be multiple handle turns within one trace.
Emil F 00:24:06 What would that mean? Like, what would they show us if there are multiple handle turns in a single trace?
Liudmila Molkova 00:24:12 And there are multiple agents working on things.
And the trace context propagation was enabled.
But we didn't detect, intentionally or unintentionally, that there was a root one.
Emil F 00:24:29 Okay, so it's avoiding the need to have a common route between those agents.
Liudmila Molkova 00:24:34 It's not avoiding, it's just quite impossible for us right now to guarantee context propagation end-to-end, and it's not clear if it's absolutely necessary. Like, if you think about HTTP communication, we're not saying that only the first HTTP incoming call is the HTTP call and everything else is something else. We're saying all of them are HTTP.
Emil F 00:25:01 Alright, but the turns, like, to have a consistent turn across multi-processes, you still need to do the context propagation.
Liudmila Molkova 00:25:10 Yeah, it's just we will not do it in a week. It requires everything to change.
we need to have, let's say, handoff to include parent context information, or A2A to cover the context propagation, or some other things to include a context propagation. And the best we can do today is to say, okay, locally.
Within one process, we can guarantee that the… we distinguish the outermost turn.
Accra?
Emil F 00:25:41 the.
Liudmila Molkova 00:25:41 But this is, well, we can say it's best effort. We will eventually get there maybe if infrastructure supports us.
Emil F 00:25:51 Yeah, I guess I still don't see what the difference is, because this is the same board that TraceID is in. If you don't have context propagation, then, you know, you'll come up with a new TraceID whenever you hit the new process.
And same thing for handle turn. If you don't have context propagation, you'll come up with a new handle turn in the new process.
What is the benefit?
Josh Bonczkowski 00:26:16 They are slightly different use cases in that there's already infrastructure to handle propagation of a trace ID as part of the context. That exists in OTEL, that exists in other platforms that are similar to OTEL.
The new piece where we have to be able to handle, we've already done something, is modifications to things like trace state context information, which is a much bigger change to be able to notify downstream, hey, we've already done this bit flip, right? And so you don't do it again later on.
That's the difference there, is that… Trace IDs, like, are well taken care of by… for years by OTEL. This is a new concept. We have to get through other teams in order to get that put into context. That goes over… Headers as part of the request.
Emil F 00:27:10 Okay, I am… yeah.
Neil Yashinsky 00:27:12 Can I send?
Emil F 00:27:13 I…
Neil Yashinsky 00:27:13 be?
Emil F 00:27:14 I think I need to read up more, but, josh, yeah, go ahead.
Neil Yashinsky 00:27:19 Oh, sorry, I was just gonna say, if I'm hearing you right, Ludmila and Josh, I think what you're saying is, like, there's existing infrastructure to… do most or all of this now using the traces, and then so, like, the overhead of adding this as a specific part of the specification carries additional, if you will, weight, given there's an existing process to do this, albeit not within this framework? Is that… might Kind of.
Summarizing properly?
or not.
That's okay. That's what I took away, Emil, is like, there's value in doing this, but, like, before it's made a convention.
We want to make sure that it's conventional. Sorry, that was a bit of a joke.
Aaron Abbott (Google LLC) 00:28:10 Yeah, I think Max said something like we would tackle this later, maybe just not in the current PR.
Liudmila Molkova 00:28:19 Yeah, like, they're… It seems two orthogonal problems, that we want to… understand what the… at least their local root is, and have a distinguishing factor, have proper semantics.
And then the semantics can be independently extended to distributed agents.
And if we try to solve the second problem first, we will not make progress.
For maybe months or years.
Josh Bonczkowski 00:28:52 Correct.
Emil F 00:28:55 Yeah, okay, I feel the floor. So Josh, I think you have your hand up.
Josh Bonczkowski 00:29:01 Chris Halle, I'm on probably the opposite side of most of you, right? I'm on the consumer side of all this, versus the production side of putting the spans in place.
So, I'm, like, having multiple services, or multiple, you know, services are the best words, as part of a larger communication trace, have handle turns, that's fine.
We're gonna look for the first one in time. Really, at the end of the day, is where, like, the first one that came through time-based, or the beginning of our trees, we re-establish it, that's where your turn begins. If you missed something above there, then you probably didn't instrument it. It's that simple. Add the instrumentation, it'll correct itself.
Right now, without doing that much deeper piece, which is why I originally raised my hand, was to talk about that.
Without having the ability to propagate this through the trace headers.
We can't actually just have a single turn yet. So having multiples, that's fine, as long as they are multiples per service, one per, kind of, subtree for a service running. I don't think there's any real… Problem or harm in that, on the consumption side.
Liudmila Molkova 00:30:23 Service name is a good one. Quick check, Josh.
You… it's assume… there is an assumption that you know the root service name, or the one, like, the hierarchy between service names.
You would build a dashboard for a specific service, let's say.
Josh Bonczkowski 00:30:40 Correct. So I'm thinking about this from… I start with, like, thinking about our, like, our trace product, where, a request comes into a service, a bit of code running, your endpoint.
We know where that is and then we watch where it goes from there through other requests going out. Is it going to another service? Is it going to a database? Is it going to a public endpoint?
Like, that's what the tracing gives us, so… for… our particular AI product, we look at the, kind of, the messages and the trace itself as it came through to figure out What services were involved in that communication?
Liudmila Molkova 00:31:19 I see, so you, like, use additional semantics to understand what was the… the… What were the services? Yeah, thanks.
Trask Stalnaker (Microsoft Corporation) 00:31:29 And pulling out what the main agent is.
Josh Bonczkowski 00:31:34 So right now, we are just determining that, heuristically by the first set of… you kind of, currently we have, I can't remember, like, Invoke Agent and… I think it's Run? Oh, there's another… there's another… span name for, like, one's for I'm calling an agent, one's for the agent is running. I forget what the naming differences between those are today, but that's… we look for the first one of those, and that, like, that's your first agent. But every time an agent runs, we actually just mark that as another agent in your service, or in your call, rather.
and just tell you, like, these agents took part of your conversation. That's really what the customers are trying to figure out, is what agents were used for that request, because, from a management or debugging perspective.
a company may have hundreds of agents, but me as a team, I only built 3 of them. I want to know which requests have my agent, not all the rest of them.
So it's a filtering rule at the end of the day for a lot of our customers.
Trask Stalnaker (Microsoft Corporation) 00:32:42 Limila, so the things that I like about this, I definitely like, The single span type.
For all 3 of these.
And therefore, the single metric, duration for them.
They do… All seem very much like.
People talk about agent, invoke agent.
The… even this one, as you were describing, trying to describe what a turn is, it's like you're… it's invoking an agent, it's invoking the main agent.
I think… I haven't quite got my head around the… Turn, being… General, for, like, if that… Like, I want handle turn… why it's different from invoke agent. I guess it just seems like invoke agent with a main agent.
Is that… What handle turn is?
Liudmila Molkova 00:34:08 This is the encompassing operation, right? If there is… If the main agent is the one which does all the work.
Then they would be the same, but here in the… Force example, the invoke… the first agent to invoke think is the planner.
Right? It's not the main agent.
So, you would have…
Trask Stalnaker (Microsoft Corporation) 00:34:33 Is that… like, I guess, like, when you're talking about this, what is this main agent?
You're putting a main agent name on this… BAM here, right?
So, is.
Liudmila Molkova 00:34:51 Yes.
Trask Stalnaker (Microsoft Corporation) 00:34:52 Invoking that main agent? Isn't this invoking that main agent?
Liudmila Molkova 00:34:59 It is.
It's just you don't care if it's an Agent or Workflow, or… Whatever. You don't care, right?
Trask Stalnaker (Microsoft Corporation) 00:35:12 Okay, so it's a… so… Then workflow, what we're trying to do, it sounds like, is limit… is semantically define workflow better.
to mean, like, a graph. Like, in my head, I was just merging Invoke Agent and Invoke Workflow and Handle Turn all into one, like.
Invoke agent.
As just a general, like, okay, we're, like, when people talk about these they talk about agents, I'm invoking my agent, they don't… like you said, they don't care if it's a workflow or… Or not. But internally, the goal, then, of preserving workflow would be.
Liudmila Molkova 00:36:04 I don't know. I don't have a strong sense on preserving workflow. I think if we preserve it, it's just the operation name.
And even then, the operation names, my long-term vision for them is that they are idiomatic to the SDK, they are anything, they're not a classifying factor once the spend time becomes a reality.
So, it could be a parallel… agent, which is a workflow in ADK. Right, Max, if I'm not mistaken. So, it's something that user actually called.
That's the idiomatic to the SDK they are working with.
And it can be called FUBAR.
But it's fantastic.
Trask Stalnaker (Microsoft Corporation) 00:36:52 Go ahead.
Liudmila Molkova 00:36:54 The spend type.
However, call it our metric name.
are unified.
And… What I hear is that you kind of think about the unified name being Invoke Agency.
Trask Stalnaker (Microsoft Corporation) 00:37:06 Yeah, I was gonna ask, what do we call the metric?
And if we're gonna call, like, the metric invoke agent, like, it… like, this is the most important.
Span.
And so then, like, it would feel off to me to, like, not have it Aligned with, sort of, that metric name, maybe.
Liudmila Molkova 00:37:30 I would say that if we call it handle turn, the dispense type, then the metric name should be handle type too. But Max probably has more to say.
Max Ind (Google LLC) 00:37:40 Yeah, I don't have a strong opinion on the metric name, I just wanted to give, on the workflow. So… I think there is kind of a small difference between a workflow and an agent where A workflow is kind of someone, you know, an engineer put in place, you know, set of steps, and this set of steps is, you know, executed somewhat deterministically, and an agent is just, like, it may kick off some orchestration on its own as it decides as you go, you know. For the metric name, I'm… I don't know, I… it feels maybe GenAI invocation, just a group.
At all, or maybe GenAI turn as a namespace, I don't have a strong opinion, yeah.
Trask Stalnaker (Microsoft Corporation) 00:38:38 Like, do you, what do you… See as the most, like, common… Verbiage, common phrasing, like, again, like, do… Because if we're going to lead with handle turn, and that's going to be our metric name.
Is that going to be?
clear. And maybe it's just going to take some time for my brain to shift from invoke agent to agent turn. Yeah.
Max Ind (Google LLC) 00:39:14 So… Yeah, so turn, I think it makes sense for Histograms, which are scoped.
For a turn, so if someone is interested in the you know, end-to-end duration of a… just, like, an abstract GenAI system. It doesn't matter if it's a workflow, it doesn't matter if it's a set of agents.
Then they are interested in the turn duration.
if they're interested in token usage, they want to know how much… like, they don't care about the exact… exactly how the GenAI system is orchestrated, but they care about the token usage per turn, so that's kind of the… Where the turn, I think, makes sense for counters, I think it would make.
Less sense, because then counters don't count Things per turn, they just counted, Whenever anything… No happens there, there is no any turn concept, it all kind of blends together.
Liudmila Molkova 00:40:22 I think Trask, you are kind of… Looking for the… the perfect operation, like the the name of the the metric or or span. And in your mind it's the invoke agent.
And you're worried about the terminology for turn, run, agent.
Trask Stalnaker (Microsoft Corporation) 00:40:46 Yes. As I said, though, like, this is only barely percolating into my brain here, the… the new… the proposal, and so… Maybe it will… this is just my first.
initial, reaction to it. But I really like the… I mean, I definitely like the unifying the span type and the metric name, I mean, and the metric.
And… So that, you know, leaves it then just… maybe it's just a terminology question that… to think about.
Josh Bonczkowski 00:41:22 The question is, how do customers think about turns? Like, every time that I hear about from a customer, whether something is a single turn, a multi-turn, it's about, like, the entire trace. That one request is a turn.
It's usually what they interpret when they're talking to us about it.
I'm not worried about the, like.
service A calls service B, you end up with two handle turns on the same tree, so I'm not worried about that aspect.
But I'm just trying to think, like, how are they gonna… how are they going to visualize and think about what this represents? And really, that's their representation of it.
Part of the reason why I bring that up is, while we put a handle turn, I think it has the same meaning that the customer is thinking about in that context.
I also think it ends up being potentially not the first Gen AI span in the trace either. Someone could do something that has nothing to do with agents before their first agent or their first workflow kicks off, in which case the handle turn comes, like, second, you know, second or later span in the request. I don't think that has any… Problem, but I want to at least, you know, throw it out there as a… something to keep in mind, that it just may not be the first thing they see in a trace.
Trask Stalnaker (Microsoft Corporation) 00:42:45 Yeah, Emil.
Emil F 00:42:47 Okay, so can we say that then the turn is the first point in the trace where user input or sub-input is given to the AI orchestrated system. Is that the semantics of a turn?
Max Ind (Google LLC) 00:43:06 Yes, yes, for a given framework, yeah.
Liudmila Molkova 00:43:11 Oh, or for any particular agent.
So…
Trask Stalnaker (Microsoft Corporation) 00:43:20 Is it really the… like, I mean, trying to define it in terms of what the user gives is tricky, because… Like… usage… Of those can be from external.
I mean, really, it seems like it's just the first age… it's… it's this main agent concept that we keep Kind of bouncing around.
Emil F 00:43:44 So so basically the entry point, whatever you know, input, however it came, is presented to the Agentic system. So this is how it enters. That's the idea behind there, is it?
Max Ind (Google LLC) 00:43:55 Yes, yes.
Liudmila Molkova 00:43:57 Wait, it's not just the entry point, it's any subagent, too, right?
All of them make turns.
Trask Stalnaker (Microsoft Corporation) 00:44:06 Okay, so it's not… so if you had another orchestration And then you called the Google ADK inside of that. You would still want a turn there for that.
to represent.
Thank you.
Liudmila Molkova 00:44:24 Would still have a turn span with semantics to say it's the agent invocation.
additional semantics.
Emil F 00:44:35 Okay. Is the desired end state, you know, when context propagation and everything is settled, is the desired end state that we have A single turn that spans all the sub-agent invocations.
Or is the goal to have, you know, a turn for every Subagent invocation.
Liudmila Molkova 00:44:56 I think there are two goals. The first goal is to… Find semantics to represent agent.
Invocation and workflow invocation, that's… reasonably good.
And they are de facto the the same. We we we hard find hard to differentiate workflows from agent reliably or meaningfully.
The second goal… Which is… maybe even more important, but it's orthogonal, is to have means to say which is the encompassing operation.
As you can think about, okay, like, I think Josh was saying, that there is a distributed Agentic application, and some customers only care about this agent.
Their agent, but not the outermost thing.
The business would probably care about the outermost thing.
And all of this layers should be possible.
And it should not be terribly different to build a dashboard for a specific agent.
Versus the encompassing operation.
Emil F 00:46:14 Okay.
But then in the same, let's say, trace, the same request bouncing through multiple subsystems and microservice, or what have you.
Then you'd end up with multiple turns in that case.
If you want to scope it to, you know, one turn as, let's say, a single team or single collection of agents, or whatever.
Liudmila Molkova 00:46:39 Yeah, you would query, okay, give me turns for the service name or give me turns for this agent or.
Emil F 00:46:45 Okay.
Liudmila Molkova 00:46:46 We should be able to build a generic dashboard that says, okay, give me the outermost turns only.
Emil F 00:46:55 Okay, so every layer underneath is basically starting a new turn, which will have a new A new wrapper for the sub-agents beneath it.
Liudmila Molkova 00:47:06 Yeah, because it's… they are semantically the same, right?
Like, there is literally no difference except that I'm an inner agent from the way I record my telemetry.
Emil F 00:47:21 Okay, I think it makes a little bit more sense to me.
Aaron?
Aaron Abbott (Google LLC) 00:47:26 Yeah, I.
I'm… I feel like I'm hearing multiple things, because I also heard this discussion about the context propagation, and I guess just one concern is that Hendel, I think colloquially, when people say turn.
They kind of mean like the thread of execution in a multi-agent system too.
So, like… I think it would be fine if there was… I don't think we need to handle it right now, but if there was something like a turn ID, And you had multiple agents, they were all handling turn, but they had the same turn ID.
you could tell that they were part of the same, like, colloquial term that people talk about. I don't think we need to tackle it now, but like, I guess… maybe this was your point, Emil, but, like, I don't think most users would think of it like Each agent has its own.
Turn.
In a single request. Is that what you were saying?
Emil F 00:48:21 Well, yes, the ID… if we say we have terms, we'll need to be able to somehow identify those terms, right? In the end of the day. So this is definitely one thing.
But also what you said about colloquial, to me at least, I see the turn as, you know, when you have a thread with your chat agent, maybe a turn is, I send one message to the chat agent, and it gives me one response, you know, full of actions and calls. But that is what I… Intrinsically understand as a term.
And here we're kind of overlaying a little bit of a different meaning, which is, you know, inevitable in some cases.
But it does confuse me.
Aaron Abbott (Google LLC) 00:49:03 Yeah, and I think…
Liudmila Molkova 00:49:04 Oh, go ahead.
Aaron Abbott (Google LLC) 00:49:05 Sorry, I was just gonna say, like, It's, it's almost like… It also depends how the subagents interpret it. So they might see it as an independent turn, or if it's something like A to A with a task ID propagated, they might see it as, oh, we're all working on the same turn. And I think that's OK. We're probably going to have to deal with both possibilities.
Liudmila Molkova 00:49:26 It's… it sounds like… There's 3 problems. The first problem is, how do we… what is the semantics? Second, how do we… Propagate the context and designate the outermost operation. And the third is, how do we call it?
So, if the most concerns are with naming.
I think the next step would be to do some research on the naming.
Trask Stalnaker (Microsoft Corporation) 00:49:53 I think we need the semantics defined first, before we can… decide on naming.
Liudmila Molkova 00:50:00 Okay, so can we park the discussions for the naming and define the semantics?
Trask Stalnaker (Microsoft Corporation) 00:50:06 Yes.
Liudmila Molkova 00:50:07 And can also spark discussions on the context prefagation because we will solve it in some way.
Trask Stalnaker (Microsoft Corporation) 00:50:13 Yeah, I think that the context propagation stuff We… we… Should find something that works today.
That makes sense today, is consistent today, without context propagation.
Liudmila Molkova 00:50:30 Cross-process context propagation, but in process is fine.
Trask Stalnaker (Microsoft Corporation) 00:50:35 Yeah.
Liudmila Molkova 00:50:40 Max, do you want to…
Trask Stalnaker (Microsoft Corporation) 00:50:42 Semantic.
Max Ind (Google LLC) 00:50:42 Yeah.
Trask Stalnaker (Microsoft Corporation) 00:50:44 Right.
Max Ind (Google LLC) 00:50:45 Yeah, so, from what I gather, like, the… I don't want to go back to naming, but… I instinctively also… Like the turn is just like a user initiated some work.
But then that's difficult to… from what I also gather, that's difficult to guarantee that You know, a user interaction only ends up being one turn.
But I… Do think that just, like… The.
Turn could be just like.
You know, a handoff to a generic agent orchestrator.
Which handles one user query.
And then what, what this agent orchestrator is, is You know, is omitted, just to have consistency.
Trask Stalnaker (Microsoft Corporation) 00:51:50 I don't… yeah, the way that I'm… Hearing the handle turn is… Like, that it's a… Almost a specialization of Invoke Agent for cases where.
the internals, like I said, aren't really… Are doing some kind of loop.
It's like a framework.
I would try not to define it in terms of user.
Boundaries, just because we don't know who's calling from externally.
Max Ind (Google LLC) 00:52:39 Yeah, would it be fair to just be like, You know, when the application hands control to the Agentic framework.
And this Agentic framework.
You know, it may be dealing with the workflow, it may be dealing with a set of agents that hand off stuff between each other, it may be dealing with just a single agent. Would it make sense to just call this handoff to the… of control flow to the Agentic Framework, would this make sense to call this a turn?
Emil F 00:53:17 I think it does, but then, again, there are more questions. Do you want to, to do this kind of recursively as agents call other agents underneath?
And call their handoffs turns as well?
The…
Max Ind (Google LLC) 00:53:33 No, I would say that as long.
Emil F 00:53:34 control.
Max Ind (Google LLC) 00:53:35 So, as long as control flow is within the framework, then it's one turn.
Emil F 00:53:45 Okay, and I'd assume there'll be an ID associated with this term. It's not just a marker here at Term Started. It will be this particular Term ID Started, so everything underneath would carry that information or would be filterable by that information.
Or not.
Max Ind (Google LLC) 00:54:05 Oh, maybe, maybe, By everything filterable, you mean spans would be filterable?
and logs.
Emil F 00:54:20 Yeah, okay. I mean, do you want to use this turn just as… marker that says a turn started here, like a line in the sand.
Or do you want it to be, like, Ticket ID, turn X started here, and maybe turn Y started a little bit down below.
Max Ind (Google LLC) 00:54:46 Yeah, I don't know. I would say that this is hmm.
Could you maybe draw, like, an example of Why the distinction would matter?
For like.
Emil F 00:55:07 Yeah.
I think what Josh said earlier about teams having their own, you know, scope of the workflow, and do we need to, in the larger context of a trace, maybe Be able to have a team.
That by using the term or a term property is able to filter, filter the traces or the spans only to the, to the terms that involve their agent.
Or in general, like, what is the… what is the usability of a turn? Like, if we have turn in the framework, and you ingest all the spans, and you have the perfect way to visualize them.
How would you use it?
Feature of having a turn, in that case.
Max Ind (Google LLC) 00:55:53 Yeah, I would say it's less for the individual creators of an agent. I would say it's more on the side of you know, a business which kinda incorporates many agents. They wanna know the duration of this Agentic system, and they wanna know the token usage of this system which composes many agents.
Liudmila Molkova 00:56:16 Imagine you had like a single agent.
Simple application.
And… It.
This agent.
Can be part of a bigger system.
In some cases.
It can be subagent in some cases, or it can be a root agent, and maybe even in the same application.
Emil F 00:56:45 Okay.
Liudmila Molkova 00:56:45 And it cannot produce.
Completely different telemetry, depending on the scenario.
Like, this agent invocation should be pretty much the same.
All the time.
And then… Do we… would we wrap it in handle turn if it's a route? I hope we shouldn't.
But we can… Stamp something on the same span to say, okay, I'm a root.
Trask Stalnaker (Microsoft Corporation) 00:57:15 I see, so you're saying that handle turn is sort of like… For frameworks that know that it's a grouping for frameworks that know they're going to Call multiple agents underneath them.
That they would emit handle turn instead of invoke agent?
Liudmila Molkova 00:57:40 What I'm saying that they mean the same thing.
The semantics differs only slightly.
In a way that.
Maybe it's an extra attribute.
Or something that says I'm the root, or the opposite, I'm not the root.
Trask Stalnaker (Microsoft Corporation) 00:58:03 For… yeah, for if it's not a handle turn.
Liudmila Molkova 00:58:08 It doesn't matter, right? Because if this if I'm the main agent and I'm the only agent.
Yeah. I'm doing the hand return.
Trask Stalnaker (Microsoft Corporation) 00:58:17 I agree with that. I'm asking about the ADK scenario.
Where you… you want to emit a handle turn.
Liudmila Molkova 00:58:27 I'm questioning why.
Trask Stalnaker (Microsoft Corporation) 00:58:31 Oh, okay.
So, why not just… Call it Invoke Agent.
Liudmila Molkova 00:58:37 Why not have one span?
However we call it, let's park the naming. However we call it, should it be one span? If there is just one agent, then we know there is just one.
Trask Stalnaker (Microsoft Corporation) 00:58:54 Go ahead, Aaron.
Aaron Abbott (Google LLC) 00:58:55 Yeah, I mean, I feel like we should keep it simple.
Like… It seems difficult to know that, and… Is the concern just this first case single agent being, like, having unnecessary nesting? Is that the main concern?
Liudmila Molkova 00:59:12 I think the main concern is consistency. If somebody calls me, however somebody called me.
I should emit pretty much the same semantics.
Aaron Abbott (Google LLC) 00:59:21 Yeah, I agree.
Max Ind (Google LLC) 00:59:29 Yeah, I think that the, like, when there's one agent, Then the handle turn.
Would probably never make sense, but I think the like the motivating.
Use cases is, if you have an Agentic system with.
Multiple agents, and you wanna… group this execution currently, that's… that's not possible. Currently, there is no, you know, multiple agents.
Or there is, but you have to call it a workflow and, and.
then you call anything a workflow, and in frameworks which define workflow specifically, that's confusing. So the idea is to have this be more abstract, so that you don't… name it, always a workflow, yeah.
Liudmila Molkova 01:00:23 So you don't… you call it… The… The… okay, I wish we are back to the… if I could query by span type. Imagine there is a property called span type.
Then you query by spend type, and it's handle turn regardless. Invoke agent and workflow, anything. There is no workflow, imagine we never invented it. It's the detail, you don't care what it is.
You say, okay, span type equals handle turn and is root equals true or is.
Something like this.
And then you would have the grouping. And it doesn't… you can create one span.
Max Ind (Google LLC) 01:01:06 Yeah, that would be great, yeah.
That would work, yeah.
Aaron Abbott (Google LLC) 01:01:12 I feel like this is much easier to look at and read when we have a separate span type, a separate span name.
It's my two cents.
Trask Stalnaker (Microsoft Corporation) 01:01:26 Yeah, but it becomes hard. Yeah, sorry, go ahead.
We are at time.
Aaron Abbott (Google LLC) 01:01:31 Yeah.
Liudmila Molkova 01:01:32 I'm thinking the next steps could be this. We can do a research on naming. I can make a stab if Max or anybody else wants to make a stab on the naming.
Go ahead. But I… We should probably have a table where it shows the metric names and spend types for all these friends.
Trask Stalnaker (Microsoft Corporation) 01:01:56 Yeah, and not just the name, but, like, if you… because… If… if we just had handle turn in all these places.
kind of to what I feel like what you were saying, Ludmila.
Click that.
Creates the consistency, and there's, you know… I don't know. It also goes against what Aaron was saying of being able to visualize, but it's… Yeah, I don't know.
Aaron Abbott (Google LLC) 01:02:34 Okay, I think we're at time, like, should we just all take a pass at this PR? Like, what's the current thing to help move this forward?
Trask Stalnaker (Microsoft Corporation) 01:02:53 Are you laying out the different options?
Yeah.
Try to categorize, because we've talked about a lot of different possibilities.
Just to frame the discussion for next time, so we can… Kind of look at.
various concrete options.
And I think the naming, like, like, that should be later, right? Like, if you can, let's just… Decide on the, you know, structure, Semantics.
If you have to name them Foo to make it… to eliminate the naming convention discussions, that's fine.
Aaron Abbott (Google LLC) 01:03:45 Okay, sounds good.
Thanks for the discussion.
Neil Yashinsky 01:03:50 Thanks, Tristan. Thanks, all. Thanks, everyone. Have a good one. Bye.
Liudmila Molkova 01:03:52 care.
Max Ind (Google LLC) 01:03:53 Thank you, bye-bye. Bye-bye.
