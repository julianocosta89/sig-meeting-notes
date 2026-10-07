SIG: GenAI SIG (APAC)
Date: 2026-10-06
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Victor Lu** 01:20 Good morning.
**Liudmila Molkova** 01:23 Hey, good morning.
How are you?
**Victor Lu** 01:27 here.
Have you seen the cosi folks here in the Gen. And I meetings.
**Liudmila Molkova** 01:34 I don't think so.
**Victor Lu** 01:35 Okay, interesting. Oh, sweet.
**Liudmila Molkova** 01:39 I've been out.
**Victor Lu** 01:41 Oh, okay. Okay, yeah, I've been out for three weeks, so maybe, maybe they just… Yeah.
the, I believe there is… I mean, the cosine and… OCSF meeting have been going on regularly, and I believe the, the, the, OTEL, Ocsm meeting also restarted.
So, Yeah, we'll see you guys.
**Liudmila Molkova** 02:09 Hello, CSF.
**Victor Lu** 02:10 Yeah, yeah, I believe that's what I heard. I haven't joined.
**Liudmila Molkova** 02:21 It's in the OCSF community, right?
**Victor Lu** 02:25 No, there's a dedicated Monday meeting, supposedly, just OTEL and OCSF in general, not regarding AI specifically.
Trask might know.
**Liudmila Molkova** 02:38 Oh.
**Victor Lu** 02:38 Yeah.
Do you know, is the Monday meeting between OTEL and OCSF happening?
**Trask Stalnaker (Microsoft Corporation)** 02:49 No.
**Victor Lu** 02:51 Okay.
Okay. Before you start, maybe we should give you an update. So.
OCSF, COSI meeting have been going on regularly, making good progress, and, understood that, there was supposed to be people who, said gonna come, to restart the Monday meeting, as well as coming to this and all the new meeting.
I'm just come here to see who's coming here. But the idea is to have the same set of AI matrix to be agreed on between OCSF and OTEL. So, of course, OCSF already have a kind of foundation for security matrix.
And whether, what OTEL does with the same set of metrics, is up to, OTEL community, because there's no, other, related security metrics like OCSF at this point.
So, yeah, I think that's, the, the, the, the, suggestion. This will make the, OTEL and OCS matrix, when it comes to AI and AI agent specifically, to be more consistent.
**Trask Stalnaker (Microsoft Corporation)** 04:00 Yeah, so we did have, somebody… Let me find her name… join the Semantic Convention.
Me, Stephanie, from OCSF.
But it was not about the AI work.
It was… about classification, some other more general OCSF work. So, I don't think we've had anybody from… bring, sort of, the AI stuff to this.
Group, yet, but would love to… Have that.
those discussions.
**Victor Lu** 04:53 Cool, yeah, thank you. I'll go back to OCI people and see who is actually… It's supposed to come here in… give the details, because I have… I'm a kind of generalist as of type, not doing the… not the details. When it comes to.
the OTEL, another question, is, does OTEL cover.
Whole matrix, including, like, edge slash robotics-related, matrix as well.
supposed to?
**Trask Stalnaker (Microsoft Corporation)** 05:28 I mean, we're… Right, we're working on, sort of, core things and extending out from there. I don't know at what point we will… think that the GenAI semantic conventions also… could be, like, federated, there could be specializations federated. I think it's… it's… yeah, so sorry, I don't really have anything.
**Victor Lu** 05:56 the.
**Tyler Benson (Mainwave)** 05:57 The way I would probably answer that is something to the effect of, hey, the… I think OTEL can cover those kind of metrics, but there's not really standardization, there's not the semantic conventions that have been established for them yet.
**Victor Lu** 06:12 Yeah, the reason I'm asking that is another community, also part of Linux Foundation, called RF Edge. They're edge computing, so they are actually creating matrix, because they consider it OTEL, but more for edge. But for edge, there are other concerns, for example, you know, reduce the the bandwidth, right? So there's different kind of requirement. Do you think there'll be, kind of a.
She'll be part of this back here.
**Liudmila Molkova** 06:46 It depends on multiple things. It's it's best to create an issue in either GenAI, some transfer, some con depending on where where it is, and see if there is interest across the, big group of people, and it's something, like, in common.
I think we're… It always depends on how many people are interested, and, like, usually in semantic conventions, at least from what I see, we are currently trying to focus on things that already exist in OpenTelemetry.
And whenever somebody comes and, wants to, contribute conventions or work together on something that's not currently in OpenTelemetry, we, recommend to do the… their… their own convention registry.
**Victor Lu** 07:37 Okay, so at this point, there's no working group that does, like, edge or, like, robotics matrix yet in the hotel community, right?
Okay, thanks.
**Liudmila Molkova** 07:50 Thank you.
Okay, we have only one item on the agenda from Steve. I added some of the things we, are actively reviewing, or, like, a couple of things we didn't discuss yesterday on the stabilization call.
So this is the item from Steve. He asked us to take a look at… the user ID… Oh.
Okay, I wish Steph was here. I'm interested in… how many other… SDK supported.
**Trask Stalnaker (Microsoft Corporation)** 09:12 So this is more than just a contextual user… This is actually API supports running something as a specific user.
**Liudmila Molkova** 09:23 Yeah.
And… Remembering our concerns with user ID in general.
**Trask Stalnaker (Microsoft Corporation)** 09:35 Yeah.
We would… Maybe want it to be scoped to not clash with the contextual user.
**Liudmila Molkova** 09:44 Right.
**Trask Stalnaker (Microsoft Corporation)** 09:45 Is this on like a client spin? I guess it doesn't really matter. It would still clash.
**Liudmila Molkova** 09:52 It's on the internal.
Half of the agent.
And… yeah.
I guess.
I… From my side, I think I have two questions. The first one is, how applicable is it?
beyond the ADK?
And then… How do we… Scope it down.
Do something.
more specific, maybe it should be ADK user ID.
If it's just the ADK, and then… It… it would have enough.
A.
Specialization.
Okay, I'm just going to leave a comment.
Anything else on this?
Okay, then moving on… There were a couple of things from the agenda yesterday.
The first one was from Dylan.
We have a special environment variable in Python that controls event emission.
And given we are replacing it with logger-enabled hole, we'd like to get rid of it.
I think it's kind of non-controversial. I wanted to check if anybody on the call would be concerned about this.
Cool.
I take it as no.
Sorry?
**Tyler Benson (Mainwave)** 12:25 No objection here. I don't have a strong opinion there, but… I just joined the call, so…
**Liudmila Molkova** 12:34 Welcome.
**Tyler Benson (Mainwave)** 12:35 Hey, Tyler.
**Liudmila Molkova** 12:40 Okay, one more friend, then.
I don't think Nikhil is here.
And we probably would need him for… for this. This is for the handoff.
And… I… I'm not sure… Oh, he replied to my comments, but I didn't have a chance to… Bye.
Reply.
So, my, my concern… Here was was this friends.
Because in the wild it's not possible to know usually who called you, you you only know.
Who you are calling.
And I was suggesting to drop.
this France.
Let's see… So there is some edge case.
where it's possible to know in ADK, but I think it's also some magic in the test that, allows to collect this information.
But essentially, I don't know if Nikhil is interested in this in particular.
But I found no evidence it's possible.
I guess I'll just take another look at the PR, and… We'll let him know.
I have a general question.
Whether we consider this as.
In the scope for re… for the stability?
Let's see… So, what it… the net new things, there are two. One is the span refinement for the tool call.
And I think another one is the span.
Or… Spend refinements for this front.
I'll post in this proposal.
Oh, no refinement here, I think. Anyway, so this is a refine… two refinements at most, and some extra attributes on spans.
So we do not have to solve it for stability.
**Trask Stalnaker (Microsoft Corporation)** 15:45 My thought is that… I mean, agent to agent… Is… seems like a pretty common piece of… The… kind of core Agentic flows that we are targeting.
So… I feel like that part would be… Good to solve one way, or good to clarify one way or another.
But obviously we can… I mean, I don't think we're required to.
**Liudmila Molkova** 16:25 Okay.
Agent to Agent A2A, or…
**Trask Stalnaker (Microsoft Corporation)** 16:31 No, not A to A. Yeah.
Yeah.
This idea that, and it seems like from the research, most of… There's… most of the… Most of that is done via tool calls, so that… Helps, we already have that.
And I guess we already are capturing those tool calls?
**Liudmila Molkova** 17:08 I just wouldn't have, the information of who is being called.
This friend.
**Trask Stalnaker (Microsoft Corporation)** 17:19 Right. Which… in… Ideally, like, that would be the child Like, you would have that in the… span hierarchy, but it seems like with these loops, often you don't, and so… that would be useful. Now, the transfer mode… Seems… less… critical.
I mean, it's useful, certainly very useful.
But… at least… It wouldn't… at least we would have a solid trace shape product.
for defined… Yeah, you were.
**Iwa Wong** 18:10 I actually have a question related to, who called you. I'm curious why we're not possible to be able to tell from… So.
Call yourself.
**Liudmila Molkova** 18:28 So what, agent being called knows is the handoff information, whatever the caller agent decides to put.
In this handoff.
And… It… usually does not contain any information on where it came from. It can contain the chat history, or just a plain message. There could probably be some metadata, but it's… and we definitely would want To find ways to enrich this information.
But I… it's… yeah.
**Iwa Wong** 19:04 Yeah, I… yeah, I think this is something that we should follow, I mean, we should ask, like, the Anthropic, people, or, like, the Google people. I won't be able to make it to the, to the, the… the Monday, Wednesday, Friday call consistently now. Yeah, I'm just curious if something that we could ask them to actually do, they have to solve it for subagents anyways. It's something that I don't think I'm hearing from any of them, on Slack.
**Tyler Benson (Mainwave)** 19:39 I mean, I think this is probably a more general problem, that even, like, just general tracing experiences, like, it'd be great if an HTTP client or a database call could know who called them and report that, but general.
Programs don't have that information readily available unless you're looking at the stack trace and seeing who called you.
That… that's just not generally something that, is passed along to the Kali.
**Iwa Wong** 20:14 Yeah, I think traditionally, like, there are… so I'm coming from a security background, and I can tell you, like, why I'm particularly interested in this.
The reason why is because I think about, the… the agent itself, right? Like, now, like, traditionally, you have a process ID of, like, some kind of, things that are misbehaving. You have, like, the level 304 animation that you can kind of identify, like, what bad things are, like, you can probably guess, like, from well-known ports, right?
But when it comes to agents, that further breaks down, the identity problem, with the agent perspective. So, now, think about, like, I mean, you have, like, Clarklo or Codex, on people's devices now. It's actually, or even Gemini or whatnot, right? Muse, things like that.
You have different threats.
from these agents, each of them could, may or may not have memory management, context management, split, or whatnot, but New Milonga was able to tell, like, which, agent is actually behaving wrong.
And, like, and, and because of these agents being… needing to, have a way to actually identify who they are before they can actually talk to some of these, say, for example, now you have stablecoins.
like, how do you catch fraud that is done by agents, or, like, through humans using agents to actually achieve fraud? For who's able to stable coins, crypto, or whatnot, right? So, like, I think there is a real need, to be able, like, at least for the agent side, we're not, like, scoping all the way to, like, all the database and whatnot, but at least for the agent side, I think there is a… We need to actually capture the client-side identity, and we probably need to ask the people who are building these agents to surface some of this metadata.
**Liudmila Molkova** 22:23 Yeah, I agree it's useful, and it would be great if they provided it, and then we would capture it.
Okay.
**Iwa Wong** 22:30 all.
So should I…
**Liudmila Molkova** 22:32 Once they…
**Iwa Wong** 22:33 How should I, get this started? I won't be able to, make it to the, Monday… Wednesday, Friday?
**Liudmila Molkova** 22:43 The people who we wanted for are not in this call. These are the people in OpenAI, SDK, ADK. Well, sometimes people from ADK come.
But I would create an issue in the corresponding repos for the SDKs that do the handoff, and tell them how useful this would be for the logging and tracing purposes.
**Iwa Wong** 23:07 Okay, yeah, I'll slack you for, like, where the issue should land, and go from there.
**Liudmila Molkova** 23:12 Oh, I don't know, I'm not… I'm not the person working on ADK or OpenAI, this is where I would start.
**Iwa Wong** 23:20 Oh, okay, got it, and it's…
**Liudmila Molkova** 23:30 Okay, Anything else on this? I will check and get back to Nikhil on this.
We… I had a bunch of discussions yesterday about this, and I brought it up because… or the day before, because I hoped we could discuss it with Felix, who was concerned about the inference operation.
But he's not here. I don't know if it's useful to talk about it now.
Does anybody have any topics they want to bring up?
**Victor Lu** 24:16 If there's no other topic, I do like to understand the… what do you think… how do you… define what is the OpenTelemetry project. So, because I see a lot of people claiming to, you know, they're creating an OpenTelemetry spec.
for example, for edge computing right? But they don't come here and talk to you. Do you? How do you?
Consider them, hotel or not.
**Trask Stalnaker (Microsoft Corporation)** 24:46 So, from, I can take… try to take that. From a semantic convention, perspective, we're actually… we're… we're encouraging people, to do that. We've put a lot of effort into the semantic convention tooling, the Weaver tooling, to support federated semantic conventions.
Where people can build specialized semantic conventions for their domain, on top of the Core OpenTelemetry semantic conventions.
That way, you know, everybody agrees on server.address, server.port, you know, all the basic things, but they can specialize and have You know, all the domain-specific things in their registry.
And then consumers can consume.
both the registries work together. Basically, you can get an Uber registry, you can point to that multiple, you know, the core Semantic Convention registry, will get brought in transitively. You could point to the GenAI semantic convention registry, which is a separate repo now, and then a separate registry, can point to these third-party registries, and as a consumer, you get, basically an Uber registry that you can work with, validate against.
**Victor Lu** 26:15 So if I understand correctly, as long as a spec follow the semantic convention and you consider them hotel telemetry, is that correct?
**Liudmila Molkova** 26:28 We don't classify what Dottel telemetry is, right? So, it… if it complies with semantic conventions fully.
Then it's probably conformant or compliant, but it's not… the term is not defined, So maybe you can clarify what, what you mean.
**Victor Lu** 26:48 It's just out there, there's… because OTEL is doing so well, right? So everybody say, I'm OTEL. So, so there's a lot of specs saying, I'm going to create an OTEL spec for this particular use case. But how do you define? Is there a conformance test? Say, do this, then you're OTEL. Is there such a thing?
**Liudmila Molkova** 27:07 There is a conformance test, but it's slightly, different. So, there is this repo.
And… The… it validates if instrumentation library is conformant to the semantic conventions.
And this currently is limited to a few semantic conventions registries we have in OpenTelemetry.
So, like, you can see, I don't know, there is the… the open inference confirm and suit here, and there are some findings and report here of what's been produced and whatnot. We don't have, like.
a report saying, okay, it's conformant, or it's not conformant. It's just this file for now with some messages, but… We'll probably…
**Victor Lu** 28:01 Can you copy and paste the link, please? Yeah.
Sure. So there's some work being done to try to define the conformance, but there's no strict rule to say, do this and you'll conform, yet.
**Liudmila Molkova** 28:13 So if you want to be super conformant, what you would need to do is to, create a scenario like this, and if you don't see any findings here, and you see all the spans you expect to see, or spans, logs, metrics here, then you're fully conformant. This is the current definition. Then what…
**Victor Lu** 28:37 What else?
Is this the link you just pasted?
**Liudmila Molkova** 28:41 Yeah.
**Victor Lu** 28:41 Okay.
**Liudmila Molkova** 28:42 Oh, so I didn't include the data JSON because I don't want to spotlight open inference.
**Victor Lu** 28:48 So the one you pasted in the chat, in the Zoom chat, if someone say, follow that literally, then that's strict conformance.
**Liudmila Molkova** 28:59 it's.
**Trask Stalnaker (Microsoft Corporation)** 29:00 Just to be clear here, we're talking about conformance to the GenAI semantic conventions.
**Victor Lu** 29:06 Okay.
**Trask Stalnaker (Microsoft Corporation)** 29:07 Not conformance to, like, if somebody is developing a third part, like, Edge or, you know, some other domain, they would need to build their own conformance test for that.
**Victor Lu** 29:20 I see. So if someone want to build a domain-specific spec, they want to call themselves OTel, what is the criteria to — minimum criteria, actually?
**Trask Stalnaker (Microsoft Corporation)** 29:30 There's… There is no defined criteria at this point.
What I would say informally is that they, need to use the Weaver tooling. They need to use the YAML, or basically follow the format of the GenAI mainframe other using the federated semantic conventions. So, if you just kind of, you know, research the federated semantic conventions, there's a bunch of work around that, and that's our… How we would like people to.
Extend semantic conventions.
**Victor Lu** 30:08 Okay, alright, thanks.
**Liudmila Molkova** 30:11 and.
**Tyler Benson (Mainwave)** 30:11 there.
**Liudmila Molkova** 30:12 Confirmant to that registry, it doesn't mean that they are OpenTelemetry projects.
If it's third party, we're not in the position to… say it's conformant with OpenTelemetry.
At least was there.
with the semantic conventions. It could be OTLP, and it could be totally legit OTLP, but it, like… this is also not defined what conformance there means.
We are at time. Thank you all for coming, and see you around.
Thank you.
**Tyler Benson (Mainwave)** 30:49 Bye.
