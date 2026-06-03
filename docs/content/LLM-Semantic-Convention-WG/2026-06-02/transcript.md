SIG: LLM Semantic Convention WG
Date: 2026-06-02
Duration: 36 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 01:10 Good evening, Steve.
**Steve Rao** 01:12 Yeah.
**Trask Stalnaker** 01:13 I mean…
**Steve Rao** 01:14 For the money.
**Trask Stalnaker** 01:15 Morning, Ludmila.
**Liudmila Molkova** 01:17 Hey, good morning.
Good evening.
Great.
Okay.
Probably my turn?
**Trask Stalnaker** 01:32 If you're a little more awake, that would be awesome.
**Liudmila Molkova** 01:36 Okay, so… am I sharing the right screen? Yes.
Okay, wonderful.
Should we take a look at, Existing PRs?
We're from Eustiv?
**Steve Rao** 02:16 Okay, yeah. I sent a PR, two weeks, two weeks ago, and, yeah, I… I saw you, left some comments, and I… addressed some review comments, and I left Wang… problems.
**Liudmila Molkova** 02:45 We're looking forward… Do you remember the number?
**Trask Stalnaker** 02:52 9.
**Steve Rao** 02:53 Yeah.
**Liudmila Molkova** 02:55 179, okay.
So… Okay, yeah, I'm, I'm curious what, what we can… Dude, we don't have… Okay, we have inference… oh, we have the report, but we… don't have… any reference scenarios for this?
Would it be possible to add one or two?
I think Bedrock and OpenAI are the ones that would have it.
**Steve Rao** 03:48 Okay, yeah, yeah, I… Yeah, I of… I fixed this, problem, but I, don't, Yeah, send a com- commit.
Just now, and I will send it later.
**Liudmila Molkova** 04:08 Okay.
Sounds good.
**Trask Stalnaker** 04:11 Great.
**Liudmila Molkova** 04:13 Thank you.
chang Long added the… this, Do we have Paul Kim on the call?
Doesn't seem so.
Should we wait?
**Steve Rao** 04:37 Yeah, maybe we can skip the, agenda.
Firstly, yeah, I'm not sure whether he will join the meeting today or not.
**Liudmila Molkova** 04:50 Okay.
**Steve Rao** 04:50 The big, yeah, we can… Go ahead. And, yeah, I can introduce something about my, yeah, issue. I'm not very familiar with, history of Gen AI Osthena Convention.
And, yeah, I'm curious, whether, we have the plan to, add some, server, inference engine, semantical convention.
According to my knowledge, we just covered some, a span… a semantic convention, of spend from client.
And, yeah, recently, Yeah, my colleague have a requirement, he told me, without the, server, site, submitted convention, But he also, do some instrumentation for some, AI gateway.
To calculate the token.
In that scenario, Yeah, he wants to have a server side.
semantic convention, and, tell the developer how to, define the token, attributes in different sides, like client side, server-side, and, if we can do, this, and, it can make, easy for them to do some instrumentation for, AI gateway or server, site, system.
**Liudmila Molkova** 06:45 Yeah, I'm just looking for… there were a few previous discussions… on this, and… I think there was a PR… For, Ankit, right, Drysk?
Nice.
**Trask Stalnaker** 07:02 Oh, right.
**Liudmila Molkova** 07:03 It hasn't…
**Trask Stalnaker** 07:05 Probably on the old repo.
**Liudmila Molkova** 07:07 Yeah.
**Steve Rao** 07:10 Yeah, I also sought the, issue, add some inference metrics, yeah, it's similar. Yeah, maybe we have some similar aspect.
**Liudmila Molkova** 07:22 Yeah, and I think, I think we created some issues in the past.
But I don't see them here, I'll… I'll try.
Okay, let me just, I'll… I'll find and add more. So for… for that agendic stuff,
**Steve Rao** 07:58 Also added to this issue, yeah.
**Liudmila Molkova** 08:00 Oh, okay, yeah, sorry, yeah.
Okay.
So, for… Agentic stuff… We had a previous discussion, and I'll find the PR, I… Bing… It… was not, Merged, because we got stuck on Deciding which… Crying should it be.
Because, let me find it.
Yeah.
So, I think we, we're… we've been thinking whether… Okay, so, so far we have two engine server spans, the internal And client. And client span is when you invoke a remote.
Agent.
And then, on the server side, Potentially, someone would… use… HTTP server span, let's say, or JirPC server spend to receive the request, and then would create an invoke agent spend.
From the server site.
**Steve Rao** 09:50 Okay.
**Liudmila Molkova** 09:51 I don't remember exactly what was the final… problem here, but I think we never resolved this… this question.
Does it match what you remember, Trask?
**Trask Stalnaker** 10:10 Yeah, we were trying to decide between Like, should it just be an HTTP server span?
That captures, and then an invoke agent internal span underneath that.
Because likely, that's how it's being implemented, if you're using like, an agentic framework that's already, you know, is already instrumented, already capturing those internal invocation internal spans.
Does that make sense, Steve? In your case, What, are you already getting, invoke agent internal span on the server side. And you're just wondering what to wrap it in?
**Steve Rao** 11:09 Mmm… Invokage.
Yeah, currently, the, problem is, yeah, without, semantic convention from, suicide, for some different team, they will, just like, for some team, they work on AI Gateway.
They will, they will think it's very, it's necessary for them to, To add the attribute to calculate token.
from the side.
So, in different teams, they will do some, yeah, similar things, something like they will repeat to calculate a token in a trace.
**Trask Stalnaker** 12:04 So by Gate… AI Gateway, You're… are these… this is… oh, you said… you're saying inference. Okay.
**Steve Rao** 12:14 Hmm.
**Trask Stalnaker** 12:15 I see. Yeah, so the previous… PR was specifically about agent.
like, invoke agent…
**Liudmila Molkova** 12:29 Oh, right.
So, for inference, I think we dis… Casted, and we discussed that… It would be nice to understand what ELLM does, because I think they have some tracing.
For the gateways, it's yet another concern, possibly.
So… I think you mentioned VOM somewhere here, right?
**Trask Stalnaker** 13:34 Steve, how is the Gateway calculating… how are they planning to calculate the… token… token.
From… from the response?
**Steve Rao** 13:47 Yeah.
**Trask Stalnaker** 13:48 extracted? Yeah. Okay.
**Steve Rao** 13:49 Yeah, I guess maybe they just do the things, like, in client-side.
**Trask Stalnaker** 13:58 And so, on the gateway… but that's gonna be… I mean, on a gateway, you're gonna have the invoke… you're gonna have some… you're still gonna have the, inference client call.
**Steve Rao** 14:14 I'm just thinking… Yeah.
**Trask Stalnaker** 14:16 And that's… that can be… that's defined by semantic conventions.
And that has… That's just a normal… inference client.
Span.
**Steve Rao** 14:32 you, you think in AI Gateway site, yeah, maybe we can use the… Infrared client-side semantic convention.
Gee… To implement related instrumentation.
**Trask Stalnaker** 14:50 So, yeah, I mean, that… just as an option, not saying it's the best option, but that, kind of relates to the previous, the agent server span discussion we had, which is that one option is for the gateway to capture an HTTP server span.
And an inference client span.
Right, because that's… probably maps to how the gateway is implemented anyways.
in terms of, you're probably using an HTTP server framework to…
**Steve Rao** 15:36 Hmm.
**Trask Stalnaker** 15:37 to handle the request.
You could just use out-of-the-box HTTP instrumentation to capture that server span.
And then, if you're using, you're probably doing something more generic and probably making an HTTP call out.
For the client side, but you could… Capture that as a inference client span.
**Steve Rao** 16:16 Yeah, I have two questions. The, the first one, yeah, if we do something like, yeah, capture HTTP server and, plus, inference client in, getaway, Yeah, for, if there is a trace from, inference a client side, invoke the getaway. And in this trace, they are to inference client spam.
And, it will, calculate, twice.
About the program.
Yeah, how, how do we, distinguish the different, Span in this trace, yeah. Yeah, maybe a very simple way is to… we can… there is a attribute called the hotel scope name.
or something like that, we can distinct with, the… The type of token in this trace.
Yeah, this is the first question, and the second question, is, yeah, they are, Ludamila list some, solution to, deal with the scenarios. My question is, from hotel geni's side.
Yeah, do we have some plan to, document some semantic convention or guideline for, other… Yeah, user to… To, Instrument that… gateway application or inference, Engine, according to our guideline.
Or semantic convention.
In the future.
**Trask Stalnaker** 18:24 So, as far as double counting.
if you're counting them from spans, from, like, there's two different scenarios. One is… Counting up from traces, the other is counting it from metrics.
From the tracing perspective, I think that you would basically stop once you hit the first inference client span.
In your trace.
Because that… like, think of the Java instrumentation, where we have HTTP clients, sometimes wrapping other HTTP clients, like, that could be, Plus, in this case, you have the gateway. Anyway, that would be one strategy. The metrics… is… Tricky. I almost would want to say that you would not want to report the metrics from the Gateway, but… I mean, they're… they're also… Like, very… But I don't want to say that.
Because that might be all you have, for example, if you're not tracing… if the client isn't… Already capturing the telemetry.
**Liudmila Molkova** 19:55 Is it beneficial, though, to report?
Things on both sides, gateway and client.
You pick one or another.
Because if you instrument on both.
the GenAI stuff, fetch duplication on the gateway. Like, let's say you have an instrumented client.
What do you want from Gateway? At most, the… just the HTTP stuff?
or nothing, the server logs, the forwarding logs. Or if you have are… If you don't have instrumented client, or you don't want instrument clients, you only want instrument gateway, you get enough from it.
Than them being replaceable and the same.
like, reporting from Gen AI part, the same things.
is easy. And it's the same problem with HTTP, right? Like, when like, Envoy or the service meshes report.
Additional spense… It's somewhat noisy.
**Trask Stalnaker** 21:05 Steve, yeah, I mean, that's definitely, I think, another good option there is HTTP server span plus HTTP client span.
like… Does… what is the motivation for the Gateway to report?
Gen AI… telemetry at all.
**Liudmila Molkova** 21:41 available soon.
**Trask Stalnaker** 21:42 Yeah.
**Liudmila Molkova** 21:45 Let's give him a few minutes to come back.
I've seen Aaron join. Aaron, I think you looked in the gateway.
Instrumentation at some point.
Not sure if you heard the… any context. Curious what you think.
**Aaron Abbott** 22:16 I was… I mean, I was thinking about this in the context of, like, a inference… Server, and not necessarily a gateway.
Or rather, like, you know, when it's not a sidecar, Gateway kind of thing.
It seems… it just seems a little difficult for… To coordinate the instrumentation between the client and the server, if you want to completely avoid double counting.
There's, like, there's cases where they… where they don't, You don't have control of both, I guess.
**Liudmila Molkova** 22:55 I see.
And, like, some of your clients are instrumented at others.
are not.
**Aaron Abbott** 23:02 Yeah.
And, like, likewise on the imprint side, if you imagined, you know, like, say you're running BLOM in a GKE cluster or something like that, and it's serving A lot of different applications.
You'd have maybe the same kind of issue.
**Liudmila Molkova** 23:25 I think that the server, like, the VLLM level, makes sense.
And we should define it. We have VLLM metrics for VLLM, right? It's… non-controversial, I feel, to add.
the inference server's pen.
the, the gateway… War Agent is more… eerie.
Oh, you're a backstiff.
**Steve Rao** 23:56 Yeah, yeah, sorry, yeah, yeah, I… if I remember right, Chaska, you asked me, last question, what is the motivation for our Getaway team to, To calculate the token, or, create a trace, according to, JNI's metaconvention.
I, I, I guess, Yeah, for some team, they work, in… AI getaway.
they want to provide out-of-box observability for their user, if they don't, if they don't use, some, Python instrumentation or something like that.
I guess this is the, our main motivation.
**Liudmila Molkova** 25:09 Well, assuming… All layers are instrumented. There is a client client. There is, like, the user client. There is a gateway.
There is server, and then the server. There could be another client.
I think, like, I don't… the attribution… people who… count… who build dashboards or queries should take into account the server name.
Or server namespace.
Or something that's… identifies who reports it.
**Steve Rao** 25:53 Hmm.
Yeah, if, yeah, if there is a semantic convention to, provide a different namespace, Yeah, maybe a different team will follow the cinema convention, and there is a corporation.
To provide the… the… Relate to, Complight.
Trace, aspect for users.
Yeah, currently, I think, yeah, without the, related semantic convention, yeah, it's a bit hard to, coordinate different teams.
In these scenarios.
-
**Liudmila Molkova** 26:54 well, would… Would it be possible for them, like, to… Build their analytics based on the service name, so when they fake.
then they count tokens.
Somebody who monitors their system, they know the service name they are interested in.
And, like, not filtering by service name, Doesn't really make sense.
**Steve Rao** 27:31 Yeah, yeah, yeah, maybe, there are a lot of, different, approach to solve these problems, yeah. But, yeah, maybe we hit the sandbox, but, I have, Another question, yeah, from the hotel JNI, Sikh, do we have, anything planned to… Yeah, defined several site, sentimental convention, or provide a guideline.
For this question, in the future.
**Liudmila Molkova** 28:06 It's a question of who's interested in this, and how much energy they spend, right? It's not that… We have… we did the… roadmap exercise, and I think server-side instrumentation was relatively high there.
**Steve Rao** 28:21 Hmm.
**Liudmila Molkova** 28:22 But unless somebody like you comes and puts the energy into doing this, I don't know if it will happen.
**Steve Rao** 28:29 Okay, okay, makes sense.
**Trask Stalnaker** 28:33 It's definitely in the scope.
of the SIG?
Hmm.
So, you know, I would expect it to happen sometime in the next 5 years.
On its, you know, somebody's going to be, you know, it's just, as Lynn Milla said, whenever somebody is, Really pushing on this, running into this.
**Steve Rao** 29:01 Okay, makes sense, yeah, if someone have, interest in related fear, from… Sikh, generalized Sikh, site, we are open to, accept it.
Okay.
**Trask Stalnaker** 29:18 Yeah, I think the whole double counting thing is really tricky.
**Steve Rao** 29:23 Hmm.
**Trask Stalnaker** 29:23 I… I'm not sure that there's… Gonna be a satisfactory answer there for you?
**Steve Rao** 29:32 Hmm.
**Trask Stalnaker** 29:33 I think people… May need to… Figure out.
sort of like what Lyudmila was, putting in, some way to Or, or not to report metrics.
from that.
Gateway is another good… Option.
**Steve Rao** 29:56 Hmm, okay, yeah.
**Trask Stalnaker** 29:58 You know, make those opt-in, at least.
That's… Kind of the… approach we took with, like, Java instrumentation for… that overlaps with stuff that the collector captures.
Like, system metrics?
We made those all opt-in, just to avoid the common experience of them being double-counted.
**Steve Rao** 30:24 Hmm.
Yeah.
Yeah, yeah, maybe I think this is not a technique, question, yeah, it's a coordination question, yeah. My initial idea is if we can define the client-side semantic convention.
Yeah, maybe, it's a pros to, to solve this question.
**Trask Stalnaker** 30:54 Alright, good to see you.
**Steve Rao** 30:56 Yeah, good to see you. Thank you.
**Liudmila Molkova** 30:58 Thank you.
