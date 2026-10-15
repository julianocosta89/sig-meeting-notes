SIG: Collector SIG (EU/ET)
Date: 2026-10-14
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Evan Bradley** 06:16 Hi, everyone. We're at 5 after, and I see that we still don't have anything on the, agenda for today, so please add something if you'd… I'd like to discuss it. Do we have anything that we want to discuss around stability?
**Pablo Baeyens** 06:35 Well, we have the… OTTL PR, right? That's going to be merged today, unless anybody says anything, so… Yeah, last chance to say something.
**Evan Bradley** 06:49 Let me link that.
Yes, please, please take a look.
at that, whether you're assenting or dissenting.
But I think… I think in all likelihood, it should be ready to go.
Anything else around stability?
**Pablo Baeyens** 07:44 Yeah, I guess I'll mention, we… presented, or I and Alex presented the RFC around Collector V1 yesterday on the specification and maintainers goal.
And it… Positive reception, I would say, so… Yeah, I'll go through the current comments, but… It feels like.
In general, the rest of the communities.
It's okay with it, with us doing it, so we just need to… Get it through.
**Evan Bradley** 08:21 Great.
Okay, in that case, Nimrod, do you have the first item?
**Nimrod Avni** 08:46 Hello, everyone.
Do you want me to share my screen and show the issue, or is someone… Oops.
**Evan Bradley** 08:58 Feel free.
**Nimrod Avni** 08:59 Yes.
Yeah, one second… Yeah.
So I want to kind of discuss this issue a bit about.
enriching peer attributes on the Kubernetes attributes processor. This is something that in OB, the, like, EPF instrumentation we're doing.
Basically, when we're… When we're monitoring, mainly for network flows, but also for normal application spans, we get both the source and we enrich it with, like, Kubernetes attributes, kind of similar to the existing processor, but Also, the destination.
For… for example, and we set it as, like, the service peer name in the… in the… examples of, like, application metrics and spans, and we have, like, also, like, more, like, network flow metrics that we enrich the source and destination IP enrich Kubernetes metadata over it. And the main issue why, like, so we're doing it currently in OB, and now we have the OB receiver, which we, want to be embedded inside the collector, and Try to strip all the implementations that already exist in parts of the collector. So, this is, like, one gap there.
And the main issue why we theoretically can use… Okay, so it's kind of two issues in one. One of them is actually allowing the peer enrichment.
Which basically is saying, like, not take it from resource attributes, take it from, let's say, another attribute, which is an IP, and then add attributes per record of the You know… The peer of the, who we are talking to. And the other thing is to make it work at scale, we basically need information from the entire Kubernetes metadata, not only from the current node.
So I've written down a suggestion here. There was some a bit back and forth in the discussion here.
about getting some sort of, like, central… that's at least how we do in Nobi, and I see some other products doing that, some sort of, like, central listener, running, let's say, as a deployment instead of a daemon set, and then it's, like, distributing all that information, to each daemon set collector.
And I thought, like, I don't know how we can integrate it into OTEL, maybe as, like, an extension, and then… Kubernetes attribute processor can fetch it, let's say, from from that resource instead of talking directly to the Kubernetes API. So, I know it's, like, a lot of stuff here, but, First of all, I want to know if I could… it's something that you think makes sense like as a as a feature of enriching not the the source like based on resource attributes, but the like peer attribute. And if this is the like a good approach to do it, or someone thinks of other solutions.
**Jade Guiton** 12:32 I don't have a strong opinion on on what features the Kubernetes attributes processor should have. But I feel like this should probably be two separate feature requests.
Because, I mean, maybe there's dependency that I'm not understanding, but it sounds like they are fairly independent.
**Nimrod Avni** 12:51 Yeah, I think I think the main Like, the main feature is enriching, peer attributes, and the thing to make it work at scale is some sort of, like.
Shared cash, so… like, and I think that was something that was brought up in the discussion that we're saying, like that we can.
Work on those separately, and we can even develop one, and then… and say, like, the other approach, like, the solution to make it work at scale is not a shared metadata cache, but something else?
I can, I can separate that to two issues if… you think is necessary.
So, and there's also, like, at least in Obi, the the cash is kind of implemented, and so we can, you know, do some work and and donate it.
So I'm just wondering if it's something that we need more, just more eyes on it, more discussion.
I, I mean, I can… Do whatever people here think is the best course of action.
**Jade Guiton** 14:07 Do we have any code owners of the component here today?
Christos?
Maybe.
**Pablo Baeyens** 14:29 If you're speaking Christos, we can't hear you. At least I can't.
**Jade Guiton** 14:34 Yeah, me neither.
Okay, mic problem.
I'm not a code owner, but another thing I was wondering about is, Are there semantic conventions for this?
for specifying attributes of the peer In the same way we do for the resource?
**Nimrod Avni** 15:07 No, and that was… that was one more thing that was discussed in the… In the issue that.
I mean, besides the normal, like, service peer name and peer… I don't know if there's a peer namesake, but service peer name. There's nothing that's, like, specifically for Kubernetes, like, you know, peer, Kubernetes namespace, peer, Kubernetes pod.
That's stuff that OB already does, and we can… Like, open some issues, like, suggestion there, and give… Reference points back to what Obi does, and… Until we decide. So, I think what I suggested there is using… not using semantic conventions, but, like, allowing the users to specify the destination, like, the keys that it extracts from, and the destination keys.
the destination attributes, but I don't know if it's a blocker that we don't have semantic conventions for it, and we can, like, work on that separately, like, in parallel.
I see also krajo you wanna.
**krajo (Grafana Labs)** 16:17 Oh, yeah, I'm sorry, I'm… First time I'm seeing this topic, so excuse the dumb question.
But this is kind of a… kind of an optimization, right, in the sense that… or a little bit redundant, since if you have the peer.
IP and port.
Then you could potentially look up the same information.
Boom.
From other metrics, right? So this is just enhancing… Like, you're saving yourself the trouble of associating Your metric with the peers?
Information…
**Nimrod Avni** 16:53 Basically, in our case, OB, like, when OBC is a network connection, we only have the IP of the, let's say, the destination, and we don't have, any information about, like, when we're running on our node, like, who is it talking to?
So it's basically an enrichment that we're doing to… to get, like, you know, to match that IP to, let's say, a pod IP, a service, and Something like that. And the reason that we need some sort of this central cache is, that… if every node will listen to the full Kubernetes API, like, that's something that, like, we at OB, like, experience that, like, it puts heavy load on the Kubernetes API and can cause major issues. So that's why I think a lot of systems use this kind of central, like, architecture of, like, central listener.
Instead of everyone listening to everything.
**krajo (Grafana Labs)** 17:54 So it's not just an optimization and, like, a convenience feature for easier lookup, but actually, you just cannot solve it, because you don't have the enough information without this. I see, okay.
**Nimrod Avni** 18:04 Yeah, unless, like, you know, you can… the PRP, like, you definitely can't.
Right now, with the Kubernetes attributes, precisely, you can't solve it, because, I mean, it only enriches the… the local, like, basically the source of, like, what.
The resource attributes not per.
per signal. And regarding the optimization stuff, you can maybe, like, route all the telemetry into a gateway, or, like, some central deployment that only there you listen to Kubernetes attributes and the whole… you listen to the whole cluster. But that's.
It's hard to force users to move all their telemetry to some central collector in order to do that enrichment.
I think.
**krajo (Grafana Labs)** 18:49 And… but then… Oh.
But if you have, like, multiple peers, what is the, like, don't this conflict, or is this resource that you're talking about one client inside the program or something?
**Nimrod Avni** 19:07 So the re like the resource attributes is basically like what, let's have a pod A talking to pod B and I'm observing the telemetry from the side of pod A. So I know my, and I put that as resource attributes and saying like the pod name and the, I don't know.
**krajo (Grafana Labs)** 19:24 Yeah, I…
**Nimrod Avni** 19:25 Yeah, enrich it, and then basically each connection, each request from that pod can go to different peers, and each one needs, like, to be enriched independently.
**Jade Guiton** 19:37 And I assume here the assumption is that we don't have instrumentation on the receiving side.
**Nimrod Avni** 19:43 Even if you do, like, first of all, you can, like, if you have instrumentation on the other side, you will view it I mean, you can say that that you view it as the whole trace, and then you can see but the peer attributes on a span are still important for you know.
Probably also for fast, fast lookup, and for example, stuff like service graph metrics and network metrics.
That you want to see, that information both from the client and the server side, you want to see the, I don't know.
Network flow and, and, All that stuff you want to see from both sides, and it might differ from both sides, but you still want to… Have those, attributes, those peer attributes.
**Jade Guiton** 20:36 Fair enough.
**Christos Markou** 20:41 Can you hear me now?
**Jade Guiton** 20:43 Yes.
**Christos Markou** 20:43 Yeah, seems to be working. So… I think… it makes sense to split the conversation into different parts. The casting one is something that we had discussed in the past.
I remember multiple times, so maybe that deserves its own issue, and try to see how we can tackle this in a nice way in general.
And I would be, like, supportive, if other code owners, find this idea useful to start the conversation and see how we can tackle this.
Regarding the… Peter and Richmond, I haven't really understand what problem he's trying to solve. I would like to see the issue in detail to try to see what he's trying to solve. But my concern here is that I wouldn't like to see the component to be overloaded with functionalities and different, enrichment.
Let's say, ruling strategies, that would make the component to be hard to maintain.
Because now the goal of this component is that you, send to it telemetry that already has some attributes attached to it, and you define some specific rules, and if… that would rely on this already attached telemetry, and this telemetry is only… the rules only work or mostly work with Kubernetes related metadata.
And then you enrich the telemetry with additional metadata, Kubernetes metadata.
And this is straightforward. However, the component is already quite complex, the implementation with the rules and pod associations and stuff like that. So, if we want to enhance it with a different dimension of problem that we're trying to solve here. I'm really hesitant about this. I would like to see what other code owners believe, however. Maybe I missed something here. And I wonder if we should… Try to tackle this in a different way. I'm not sure if this 100% relies on the Kubernetes API, or if you can split, maybe, the logic and rely on data that the Kubernetes attributes processor already attaches, and then you have another additional component that does this logic as a secondary step.
Maybe, that would be better, like, in theory. But that would be my initial, thought on this. If that makes sense.
**Nimrod Avni** 23:23 Yeah, I'm not sure if it can rely on already existing data, because it needs the same kind of lookup that, like, the full.
you know, Kubernetes API access, basically, like, the Kubernetes Attributes Processor can look at, for example, an IP and look up that pod information, right? That's an ability that Kubernetes attributes that it has, and then it adds it as resource attributes. So we need the same kind of capability, but even maybe kind of wider, because you need it not per resource, but per, you know, span data point. And you need… theoretically, you need, data from the whole cluster, and not, the usual deployment strategy, which is filtered by only data on this node.
We can suggest it as a different component, but then you have two components that talk to the Kubernetes, kubernetes API, you'll have, like, a Kubernetes attribute processor and a Kubernetes peer attributes processor, I'm not sure, but if that's something that we think is the correct way, I can also suggest it like that.
And I can… I can definitely split it to two issues, referencing… or, like, two sub-issues on this one, referencing that this one is, like, the main, you know, the starter, and just splitting it up.
But I definitely understand your concern, so… If.
If splitting it splitting it to 2 issues.
I think that definitely I can do that.
**Christos Markou** 25:22 Yeah, I think, makes sense to… Separated discussion about this, let's say centralized shared caching.
In a different issue, and then reduce the scope of the problem and see how we can approach the… peer enrichment, problem that… You're describing here.
Let's give it some time, I would say. I would like to see what Tyler, Dimitri, would have to add here. Maybe this can be raised again next week in the… US-friendly time meeting, if that's possible, from your side as well. And yeah, we can take it from there, then.
**Nimrod Avni** 26:04 Okay.
Sounds good.
Thank you very much.
**Christos Markou** 26:09 No problem.
**Evan Bradley** 26:37 Mikol, you have the, next item on the agenda.
**Michal Jarmółkiewicz** 26:42 Yeah, okay. So, I would like just to inform you that I've created a PDD request for a new verified processor.
It's basically verified logs that will be coming out of the signing processor.
And I'm currently looking for one good owner and reviewer as it's my first.
Podolicos.
For community.
And, yeah, that's basically all from my side. Thanks.
**Evan Bradley** 27:53 Alright, that's everything on the agenda.
Anything else from anybody?
**Ilia Petrov** 28:03 Probably one question from my side.
Sometime… I go, Okay, probably we'll phrase it like this. Currently, we have a telemetry gen, and it's used like a separate service.
Maybe not separate, but separate process, like a CIY, but I was wondering, do you find it, beneficial if we, strip the common logic from telemetry gen and create a dedicated receiver for that?
This would be very useful in cases where you want to make some load testing, and the receiver directly can do that. For instance, when Bit has such They call it inputs, but they have dummy input where you can control the data, folks, or something like this. And I was wondering, do you find this idea okay?
**Pablo Baeyens** 29:17 I think this is something that we have… Discuss in the past, 3.
Put this up.
Okay, yeah, so there's… Somebody mentioned this from Lightstep that I think is pretty similar to what you're saying.
I don't know to what extent that is updated, though.
And…
**Ilia Petrov** 29:56 Didn't know about this one, okay.
**Pablo Baeyens** 30:02 Anders.
This order link from Weber… sorry, from Arrow, on the… Discussion.
Umm.
Yeah, there's a couple of people from… from the community, that I think would be supportive of this, so if you open an issue.
I could share it with them.
**Ilia Petrov** 30:38 Okay, I I.
**Pablo Baeyens** 30:39 can.
**Ilia Petrov** 30:40 Later, prepare something.
**Pablo Baeyens** 30:43 Okay, yeah, you can… ping me on Slack, and I'll share the issue with them. Sorry, it's on a private channel, so I cannot share the thread with you, but basically it's somebody describing pretty much your same use case.
**Ilia Petrov** 30:57 Okay, I mean, I've went through… I mean, I donated, one extension already, so I'm overall familiar with the process after, initial finding of the… Sponsor. So, okay.
**Pablo Baeyens** 31:13 Okay.
Yep.
**Ilia Petrov** 31:20 Yes, that's from my side, thank you.
**Pablo Baeyens** 31:41 Okay, I think that should be all then.
Alright, thank you, everybody.
**Christos Markou** 31:56 See you folks. Bye.
**Evan Bradley** 31:57 Bye, everyone.
**Ilia Petrov** 31:58 See ya.
