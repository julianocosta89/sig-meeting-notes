SIG: K8s Semantic Convention SIG
Date: 2026-04-14
Duration: 13 minutes
============================================================

## Zoom Recording Transcript

**Victor Lu** 02:37 Hey, Steven.
**Stephen Lang** 02:41 Hey, Victor.
**Victor Lu** 02:42 killing.
Yeah, I was wondering, whether it's… I believe I joined this meeting before, but nobody Shut up.
**Stephen Lang** 02:50 Huh, yeah, that's, happened a couple times for me, as well.
**João Marques Correia** 02:58 Hey, folks.
**Stephen Lang** 03:02 Fairy.
I'm just trying to find the agenda.
Is it moving?
**João Marques Correia** 03:36 No, I think… I know Chris has won't be joining as well, so that… mention, but… I think the agenda was empty last time I looked.
**Jina** 03:48 Yeah, there's nothing on the agenda.
But they're there?
Does anybody on the call have anything to discuss?
**Victor Lu** 04:26 Yeah, first time joining here. I'm Victor Viculo, based in Tampa, Florida, independent. The reason I'm interested in, I'm a journalist, so I've been actually going to the OpenTelemetry, community, where they have a semantic convention meeting, and, including, semantic convention about Kubernetes.
I'm also interested in things like ontology, taxonomy, etc. That's why I'm just curious how the… in a way, this actually semantic convention is quite important, because, the ontology of the Kubernetes stack can determine how the API machinery is defined, etc, and the relationship between the different, concepts.
So that's why I'm here, trying to see how… what's the current, Actually, I financed meeting before I joined here before, before, but I guess, sorry, everybody was off. What is the current status of the Semantic Convention, and what is the, I guess, the roadmap for, Semantic Convention?
**Jina** 05:43 Hmm.
Does anybody want to do that?
data scientists.
So, to be honest, we have, you know, the way we are looking at semantic conventions for Kubernetes, at least, is, we already have a lot of, like, components in the OpenTelemetry, contrib.
Which currently are kind of, like, well used. So we are trying to concentrate on You know, the more common metrics and attributes which are already implemented, and we are trying to go through that list, and… Stabilizing those, renaming those if needed to be.
You know, to follow the convention, guidelines, and especially the Kubernetes-specific, guidelines that we have.
So, to be honest, right now, we are at a phase where we are just trying to… I guess, bring these components to, like, you know, do… GA stability.
**Victor Lu** 06:49 Actually, I apologize. I just took a look, closer look at the meeting description. It is part of OpenTelemetry. I thought it was Kubernetes convention, which in turn is kind of related to how, like, API machinery is defined. Yeah, it looks like it's part of OpenTelemetry. That's my mistake.
**Jina** 07:09 Oh, yeah, this is all, OpenTelemetry, yeah.
**Stephen Lang** 07:19 Victor, there is also Kubernetes SIG instrumentation.
Which is kind of related.
Although… You know, they don't discuss open telemetry semantic conventions, but they do, you know, discuss things like the metric naming conventions for the Prometheus metrics.
And things like the, you know, status set, and… Flags at, endpoints.
**Victor Lu** 07:44 Okay, yep, makes sense, yeah, thanks.
**Popham Beach (us-cam-5cc)** 07:47 Yeah, I'm one of the SIG leads there as well, so happy to answer questions if people have them.
**Victor Lu** 07:54 Oh, yeah, actually, since you just joined, I was… I'm interested… when I'm looking at this, I saw this… I didn't realize it's actually part of OpenTelemetry, because I joined a semantic convention for OpenTelemetry, and I see this one as Kubernetes. I say, okay, cool.
How about the semantic convention for Kubernetes? The reason I'm interested in it is I'm a generalist, so the part I'm interested in is, like, the taxonomy and ontology of Kubernetes. You know, so when you define the API, resource, etc, right, how do you define it based on the… ontologically corrected concepts, right? Like, what's the relationship between the different concepts, etc. So I thought this meeting is kind of related to that. It sounds like the, The other meeting you just mentioned, I know the meeting, but it's not the machinery, what is it called again? The.
**Popham Beach (us-cam-5cc)** 08:47 like instrumentation.
**Victor Lu** 08:48 Instrumentation, okay, yeah, I guess that's where it's probably discussed, that how… Longtool logically, how do you think of, I actually brought it up in another community reading, CNCF, not sure you… there's a community called AEP, It's, called Application, API Enhancement, working group, posting their, proposal, yeah. So, so it's, it's an extension from, AIP, it's part from Google, I post the link here.
So I asked them the same question, you know, when they define the resources, how do you define the API, name the APIs? So, so they're… they're not… it's not based on any particular ontology, per se. It is pretty hard, because they're not focusing on a particular, project, so it's kind of generic.
But for Kubernetes, I think it might be possible to kind of, I guess, clearly define the different the different terms and relationships, which basically is the ontology of Kubernetes, can make it the API design naming more consistent.
**Popham Beach (us-cam-5cc)** 10:05 Interesting.
I think the thing that comes to mind is the Kubernetes instrumentation. Sega's been talking a lot about, how to do state metrics for custom resources.
So it's like… Very generic.
Metric definitions and trying to reason about What to do when you don't know very much about an object, but…
**Victor Lu** 10:33 Yeah, I think especially with, like, new things, for example, AI, right? How do you incorporate AI, the new hardware types, and etc? And also, I know this is also not related to Kubernetes directly, but when it comes to applications, there are also decentralized identity versus centralized identity. So, when those are incorporated, the concepts could be something that Kubernetes itself is not used to.
So how to incorporate it into the ecosystem? Name them the… In the… when people look at the new API, they know this is related to a particular term, so that's the semantic convention, coming into play. Yeah, just curious.
**Popham Beach (us-cam-5cc)** 11:19 I don't know if our group touches on many of those, but… We do model Kubernetes resources as metrics.
**Victor Lu** 11:29 I'll probably sneak into the instrumentation meeting there to listen there. Yeah, thanks.
**Popham Beach (us-cam-5cc)** 11:36 True.
**Stephen Lang** 11:38 Victor, I'll drop you a couple of links in the Zoom chat. One is just to the roadmap, because you asked about it before.
And another is for the existing semantic conventions for K8s at this SIG.
Is kind of, interested in.
But it is kind of… There are many other conventions as well for open telemetry, so some of what you're saying might be covered by you know, other semantic conventions, possibly by other SIGs as well, so just because something runs in Kubernetes, it doesn't mean that it would necessarily be covered by this SIG, whereas this SIG mostly focuses on just, you know, the generic K8 properties that wouldn't fit into One of the other, kind of, semantic conventions buckets, if you like.
So, you know, when you're talking about AI, like, it might be covered by, like, a separate convention document, for example.
**Victor Lu** 12:31 Did you say you posted some link in the chat?
**Stephen Lang** 12:35 Yeah, there's two in the Zoom chat, if you can… if you can see it.
**Victor Lu** 12:38 I see.
**Stephen Lang** 12:38 Oh, actually, I think I might have posted them accidentally to, just Andrew's noteetaker. Let me, let me recopy those and put them in the everyone chat. I didn't realize it was… Zoom had somehow just defaulted me to, I only talked to Andrew for some reason.
Okay, can you see them now?
**Victor Lu** 12:58 It's the same now, yeah. Thanks.
**Stephen Lang** 13:08 Otherwise, is, anybody got anything else they'd like to bring up?
So, I'll drop one final link to the, to the Slack, CNCF Slack, if anybody thinks of anything, feel free to ask in there, async, it's the OTELK8 SenConf SIG channel.
If there isn't anything else, I think we can pull it.
**Popham Beach (us-cam-5cc)** 13:40 Cool.
**Jina** 13:40 Good. Thank you.
**Stephen Lang** 13:43 Alright, thanks all.
**Popham Beach (us-cam-5cc)** 13:45 Everyone.
