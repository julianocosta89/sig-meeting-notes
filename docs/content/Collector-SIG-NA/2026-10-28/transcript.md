SIG: Collector SIG (NA)
Date: 2026-10-28
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Pablo Baeyens (Datadog)** 03:35 Did we start?
I think would go with some people now.
So, for the high priority issues… Is there… I don't think I have anything. Is there… Anything… from anybody?
I mean, I guess I will mention OTTL has reached P1, and the Collector B1, like, the core distro V1, RFC has been merged, so that's some progress, but I don't think there's anything to discuss right now.
From my side, at least.
**Yevhenii Kurasov** 04:37 Just kidding.
**Pablo Baeyens (Datadog)** 04:38 If not, I guess we can go to the first item.
from… SEOG?
Not sure if I'm pronouncing that correctly.
Alright.
No truth.
This person is in the call, if you are, feel free to present yourself.
**Alex Boten** 05:05 They… they are on the call. I don't know if they… they're muted, but… Alright, maybe we'll… maybe we'll come back to that topic?
Alright, I'll… I'll go with my topic, and then we can kind of talk about it. So I… I opened an issue in the Collector control repo. My main goal with this here is to have, to have a more broad conversation.
Specifically, the problem that I'm describing in the issue is that with the release of the Prometheus distribution, we make it possible to include, like.
exporters, as Prometheus defines it, them, in a collector distribution, which is great, because it tells the story of Prometheus and OpenTelemetry better together.
The one challenge that we'll have, moving forward, though, is this… this does present the… the choices for end users to either go with Prometheus exporters or, you know, collector, receivers integrations for things that have coverage in both integrations. And… I was hoping to have a conversation here to kind of discuss, you know, should we have a specific policy around what would we recommend to users.
There's a couple of components listed in the issue, for example, like the SNMP receiver has some development that's happening today. Some of the features that are being developed already are supported in the Prometheus exporter side of things, and I was hoping we could You know, have a conversation and figure out what we should do for our end users.
**Pablo Baeyens (Datadog)** 07:21 We talk a bit about this at KubeCon EU with some people from Prometheus.
I think the… one of the main things was what Arthur is mentioning in one comment here about having a schema of what the Prometheus exporters are emitting, and what the auto-receivers are emitting.
Because, I mean, right now, for me, that I'm not… at all an expert on Prometheus, it's… Maybe difficult to… Understand what the differences are.
And it's also difficult if I wanted to build some translation layer to do so.
Or more difficult.
**Alex Boten** 08:11 Yeah, I mean, I could definitely, put together, like, some examples of data being emitted by each one, and maybe that can help us make decisions moving forward.
Yeah, I guess, you know, one question is, if… If today someone is proposing a new component, and that component already has, like, a Prometheus equivalent.
Should we continue to accept those new components, or should we… defer to trying to use what's already there. And Antoine makes a good point that, you know, the… a lot of the Prometheus exporters don't necessarily have… a model that's defined anywhere in any semantic conventions, but I would… I would argue that since a lot of those exporters have been used for a very long time, that's Like, the de facto default that end users would expect.
So, yeah, I'm happy to… happy to try and put together some comparison for some of the components.
I guess, Pablo, if you want to add that comment in the, in the issue, that'd be great, and then I can respond there.
And if nobody else has other comments, we can continue the conversation async.
**Pablo Baeyens (Datadog)** 09:29 Okay, yeah, I'll… I'll add a comment.
**Kyle Eckhart (Raintank, Inc. – Grafana Labs)** 09:33 So I've been working with Arthur a bit on the Prometheus side. Yeah, if there's other concerns or stuff, you know, Pablo, feel free to document them, and then, you know, between Alex, Arthur, and I, we can… we can try to have… come up with answers.
Because as a part of this process, we're trying to bring exporters into the hotel ecosystem, which includes, like, strategies for semantic conventions and doing those types of translations and whatnot.
**Pablo Baeyens (Datadog)** 10:06 Okay, young, I'm gonna try and find if we took notes on the Guiton EU meeting?
Because I was.
useful, and there were some other people, like Richie, from the Prometheus side that had opinions about this.
Okay, I guess… I'm next.
So… I… recently made some PRs to remove the Zipkin and Jaeger receivers, or to eventually remove them, right now it's just a… Warning from the core distro.
not issue.
Now… I tried to do this just because I thought that was… Probably less controversial to remove it from the core distro, but it did make me think that Maybe we should… Think about deprecating some of these components?
Just because in both the… Jager ecosystem and the Zipkin ecosystem, there's ways to ingest OTLP now with Either natively or with, adapters built by Bidos Projects.
And yeah, I would be interested on… Knowing what people… Think about this, what are… We should keep them or not.
Evan?
**Evan Bradley** 11:56 So, I don't have a strong opinion on the exporters. I mean, in fact, I think it would… we could probably point toward deprecation, although I'm not sure, but for the receivers, at least on the Dynatrace side, I know that we… there's a lot of, you know, large enterprises that are using you know, essentially legacy data producers using these formats. So, at least from us, we would have an interest in keeping the receivers around.
**Pablo Baeyens (Datadog)** 12:31 Okay, yeah, maybe we should separate the discussion about exporters and receivers, then?
Although, I could see the same point being made about Like, you have an old Jaeger deployment or something like that?
**Evan Bradley** 12:54 I think it'd be fair to say that, you know, if somebody wants… we can, as a community, I don't know who, who the code owners for these are right now, but as a community, if nobody's willing to step up and maintain them, I think it would be fair just to deprecate them.
Particularly if they're not gonna… I mean, if they're not gonna be in the core distro and they're just in Contrib, I think that… That opens up that possibility.
**Pablo Baeyens (Datadog)** 13:29 Okay, I guess one more thing, don't know if there's anybody from the Jager or Sikki communities here? I could reach out to, like, Yuri, for example.
And… see what the perspective is from… From their project side.
But if there's anybody here with knowledge on the matter, Interested.
And if not… I guess that's it for this topic. We can move on to you.
The one we had before.
**SEONGSOO KIM (Kakao Corp.)** 14:20 Oh, yeah.
Hi.
I'm Songs from Kakao.
The company that makes Kakao Tok in South Korea.
We're at the peak post.
Or our agent connects to the same gateway node.
And Compik GRPC can't turn on gRPC's Shopper Address List option to fix it. Would you offset this feature? If yes, I can open up VR.
Thanks.
**Pablo Baeyens (Datadog)** 15:23 If I understand correctly, this is natively supported by gRPC Go, and it's just a matter of, like, plumbing things through?
**Yevhenii Kurasov** 15:31 Is that right?
Correct.
**Pablo Baeyens (Datadog)** 15:44 Okay, and do you know if this is an experimental feature on gRPC, or is this… stable.
I can quickly check myself.
Let me see…
**Joshua MacDonald (Microsoft)** 16:11 That's a standard option. I think it's actually the default, and it's usually one that is not preferred. We changed the default away from pick first to be round robin at some point, as far as I know, and it's perfectly acceptable to change back, it's just… it pins you to one IP address, usually.
And that's not always what vendors wanted, and that's how we got it changed.
**Pablo Baeyens (Datadog)** 16:40 Okay.
Yeah, I mean, from my side, I think it's fine to add this if this is not experimental.
Seems pretty straightforward.
**SEONGSOO KIM (Kakao Corp.)** 16:58 Yes, thank you.
**Alex Boten** 17:23 I guess if there's no other issues, this'll be a short one today.
Does anyone have any other topics?
Alright?
Have a great week, everyone.
**Evan Bradley** 17:42 on.
**Pablo Baeyens (Datadog)** 17:43 Thank you.
