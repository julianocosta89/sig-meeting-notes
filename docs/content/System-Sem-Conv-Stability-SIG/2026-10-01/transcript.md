SIG: System Sem Conv Stability SIG
Date: 2026-10-01
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Roger** 00:31 Nope.
**Pablo Baeyens** 00:36 Hey.
**Christos Markou** 00:55 Hello.
**Pablo Baeyens** 00:59 Lou.
Hey.
**Braydon Kains (Google LLC)** 02:05 Hello.
**Pablo Baeyens** 02:10 Big… Maybe we can get started?
**Braydon Kains (Google LLC)** 02:14 Most likely.
**Roger** 02:18 Include them.
Mmm.
Yeah.
I wanted to bring this topic, basically it's the… I added the link, but it's the RFC for the stabilization of the core collector, and… Contrib components that, pablo wrote, and… Well, basically, there's, like, a statement on this RFC regarding the… Well, the same common relationship with the.
with the components, right, that it's still being discussed, but, yeah, I think it's… well, it's a bit controversial, and, like, well, a few folks, Within Elastic, we have been discussing that.
And Yeah, although we basically agree that we need somehow to to go for a stabilization, all the components, especially the host metric receiver. It's been used in production environments for a lot of people at the moment.
As well, but… On the other side, we are a bit afraid or worried about, What will happen with the semantic conventions?
In the future, Because… Let's say that from… From our perspective, if, If we let, for example, components to be stable without the telemetry that they are emitting.
being stable, well, it creates a precedent, right, in the sense that.
**Pablo Baeyens** 04:00 you.
**Roger** 04:01 It can be seen that We don't need to put effort in creating some semantics around all that telemetry, or agree on semantics.
For those components. And… Basically, for us, that we really believe on having a defined schema and an agreement on On the telemetry, basically, we… We foresee that maybe people won't be as much interested in defining the semantic conventions. That's one of the… That's one of the first issues, also, because We kind of justify the work in semantic conventions and host metrics towards the stabilization. So basically.
**Pablo Baeyens** 04:52 the.
**Roger** 04:52 Our way to justify why we.
Work in this working group and semantic conventions in in fact is.
Because we want the host metric receiver to be stable.
And that's basically the justification behind it, so… If…
**Pablo Baeyens** 05:09 Yep.
**Roger** 05:10 This semantic conventions is not needed anymore. It will be, let's say.
Harder to justify the work in semantic conventions.
Now, if I explain myself well.
And.
Also, it feels a bit odd as well to… For example, right now, stabilize the host metric receiver as it is.
Because, for example, well, it's… As we have said a lot of times, the metrics that we are emitting They come from one of the first versions of semantic conventions a long time ago.
And just the other week, we saw one of the metrics that maybe Probably it will change a lot, right? Like, and it will be a huge breaking change. The one that we were saying about the… System memory usage, right? This will… change the attributes, maybe we will generate metrics, Linux-specific only for the free, et cetera, et cetera, or at least this kind of agreement, so it's a… Big breaking change and it raises questions like When will we then be able to ship these metrics in the host metric receiver?
Yup.
Do we need to wait for a new core major release, or can the Hostmetrics receiver do as many, you know, major breaking, well, major releases as much as we as we want.
So this is, like, a little bit the… Concerns.
**Pablo Baeyens** 06:51 Yeah, okay, thanks. On… Your preferred… approach for this would be that we do not mark the host metrics receiver, for example, as B1 until we have Stable semantic conventions. Is that right? Or do you have another… proposal alternative.
**Roger** 07:15 Hmm.
No, not really, yeah, I would… Be in favor for the, also because.
Yeah, let's say that a few people is asking why it's What is the reason of marking a component stable if the telemetry that it's emitting, it's not stable? It's just because we want to ensure users that the configuration won't change, or…
**Pablo Baeyens** 07:45 So, the way I see it, and I would be interested on… maybe Brayden, for example, was in his opinion here, but.
what we say if we release the host metrics as receiver as V1 is that the configuration is stable, and that we won't change the semantic conventions emitted during that major release. And so you can keep on using it, and we will release a new major version in the future.
that major version, should have the stable semantic conventions, but you know that the V1 line will continue to be supported for, whatever we promised, I think it's, like, 6 months, and it will continue to have the the semantics it has whenever we mark it as B1.
the semantic conventions it has whenever we market SP1. So it's not a promise that these semantic conventions are stable, but more that you can upgrade without fear, like, you can upgrade without things changing. That's how I see it. I think Dmitrii raises his hand first.st.
**Dmitrii Anoshin (Splunk Inc.)** 08:50 That makes total sense to me. The problem I see with the current situation of source metric is the SIV, and I'm, like, more… aligned with Roger in that… in that sense, because we released 1.0 in the current state before we, have… before we migrate to stable semantic conventions, but V1 will be… not aligned with semantic conventions. It's right now not aligned, and it's fine, because it's zero, right? But once we release it 1.0, we are saying, hey, this is stable, but it's not aligned with semantic conventions. That kind of… Seems like not ideal to me, to be honest.
But in general, as you're saying, for the rule, it makes sense to me. Like, once we have, like, stable semantic conventions, we can say that there's nothing gonna change until next version.
**Pablo Baeyens** 09:46 And, sorry, before Raydon speaks, so do you feel like… This is something specific for Hostmetrics Receiver, or…
**Dmitrii Anoshin (Splunk Inc.)** 09:56 Yeah.
**Pablo Baeyens** 09:57 Like, in general, we should avoid releasing things without these semantic conventions being defined on the semantic conventions report, or…
**Dmitrii Anoshin (Splunk Inc.)** 10:05 It's fine to release it when it's not defined. So, for example, we have, like, I don't know, let's call, like, Kafka Metrics Receiver, whatever. I'm fine with 1.0, because there is no semantic conventions for that. Hmm.
Currently, for host metrics, there are semantic conventions that are actively being developed, and they don't even mention the state that host metrics receiver is in.
**Pablo Baeyens** 10:31 Yep, yep.
Okay, yeah, Brayden.
**Braydon Kains (Google LLC)** 10:39 So some of this.
like, the way the RFC's written ends up coming from, like, my opinion that I ended up stating in the Collector Stability meeting, but I didn't, like, write down my thoughts end-to-end, so it probably made it a little bit confusing when it made it into the RFC. But the way that I've been conceptualizing this is Essentially, with the host metrics receiver specifically, and not even thinking about what other components are saying, but just with the host metrics receiver, it's almost like We're, like, grandfathering it in, and, like, admitting that Because it's so old, and so many people have been using it for so long, it existed before the concept of semantic conventions even existed, as far as I know, the timeline.
We're essentially admitting that.
These… The metrics as people have been using them coming from host metrics receiver are kind of a convention in themselves because they've been used for so long. And it feels strange to say the only way we can call it stable.
Is to break it like crazy first.
I would rather say, We call, we, we basically just admit defeat, we say.
The metrics that are being emitted right now, that's V1. And you can rely on these.
not changing for V1.
And essentially they are frozen. The motivation to continue working on semantic conventions.
Is that we would never accept.
any change.
Or any new metrics.
or anything.
Unless it came from semantic conventions. From this point forward, like, now that we're at this point where we've proven with the process scraper that we can migrate a scraper to semantic conventions in a way where, like, the user can choose.
And we only ever provide new functionality, or new metrics, or changes to make the metrics better, Only through semantic conventions, and that ends up being the motivation, but… We don't require stabilization to be guarded behind Totally erasing all the de facto conventions that people have been relying on for so long, and I would think, presumably, the idea behind semantic conventions is that when everybody's producing the same semantic conventions, vendors can produce better experience around the semantic conventions versions of these things, and so the support for HostMetrics Receiver versions of the metrics, the stuff that isn't in semantic conventions. The features we would build would only be around, like, the semantic conventions versions, where we've fully audited and feel good about these metrics as we're producing them right now.
That's the way I'm thinking about it.
I… I could maybe be persuaded.
To… to back off?
The… it just feels weird to say we can only stabilize.
If we break everything first, that's the, that's the part I'm not a big fan of. I would rather freeze what we have, and say, for V1, you can rely on this. When V2 comes, where presumably we will have new and better Functionality, new metrics, better shaped metrics. You have to upgrade.
To… like, you can only get that stuff out of going through semantic conventions.
I don't… I don't know if this logic applies to any other receiver, too. I'm only thinking about it for HostMetrics receiver, just because it's super popular and it's existed for ages.
**Christos Markou** 14:18 I think this rationale is missing from the RFC. That's what I was trying to explain in this discussion in the comments with Tyler.
I would be fine to… to see the components going V1. As soon as we have this strategy documented and the guidelines written down as a collector project. Otherwise.
If we just leave it as is, it's easy that we either forget it, or, create wrong assumptions around the project. And.
like, not explicitly… Stating that this divergence is not, permanent, I think it's a miss, if we do it as a project.
So, I would feel better if we have this documented, both from the user perspective, because users would come to the Collector project and see, and would ask, what is the current source of truth, the single source of truth about system metrics, for example?
Should I look in the documentation of host metrics, or should I look into semantic conventions? I see two different things. So, not clearly stating why this difference exists is, like, seems very bad to me. And that's from user perspective, and from contributor's perspective. Let's say that tomorrow someone wants to introduce a new component or something like that, or even new metrics.
We need to have a concrete way to explain how things work, because if we don't do it on our sides for these components, then people will say, okay, we did the same for host metric receiver, why now you ask me to go to Semant Convention to find the new metrics?
Or, stuff like that. So, both from contribution perspective and project maintenance, but also from user perspective, I think we need to, be very specific and clear about, what we're going to do, in the future. And I'm fine marking V1, with… this specific thing stated, somewhere, either in the RFC or in the docs.
**Dmitrii Anoshin (Splunk Inc.)** 16:33 In that case, we need to also put a lot of references and semantic conventions to the host metrics receiver because otherwise, it's it still would be very confusing to the users. I guess semantic convention is, for the newcomers to OpenTelemetry, it's probably gonna be the first thing they see rather than metadata, YAML, or documentation created by host metrics receiver.
So, yeah, we would need to put some statements there for sure. And I'm wondering what's going on with the instrumentation libraries. There are some of them that are emitting host metrics as well. Have they migrated or not?
It also… I guess it's important to consider, because if they have migrated, it's gonna be even more… Like, in… Divergency and kind of confusion.
**Braydon Kains (Google LLC)** 17:24 I haven't checked.
for… Go has all these libraries in their SDK for, like, emitting host… some host metrics and process metrics, and I actually don't know the state of their adoption of our schema yet. They may have come up with their own shape for that.
**Pablo Baeyens** 17:43 We do have a warning, though, on the… Like.
Page of the system metric saying, like, please don't migrate until… But we figure things out if you are prior to. I think it's 1.22.
**Dmitrii Anoshin (Splunk Inc.)** 17:59 Okay, so in that case, we should, yeah, we should put it as at least all the references to the… all the implementations, like, references to all the languages, essentially, and the collector in that case, because Stating the fact that they are not aligned.
**Pablo Baeyens** 18:18 Okay. I… I am worried, though, about what you mentioned, Roger, about this being… This making it difficult for people to work on semantic conventions.
Because, like, right now, the rationale for working on semantic conventions is that that leads to stability.
of the component.
Do you feel like if we clarify things in the way that Christos mentioned.
B. That concern would go away, or would that still be a concern?
**Roger** 18:51 No, I think that helps, and also what Brydon said about, okay, maybe this is, like, a free version of the host metric receiver, as we have.
But we made explicitly that we won't accept any new metric or any modification for B2 that it's not in semantic conventions, and this is, like, stated, I… I guess the motivation is really there as well.
Umm.
But on the other side, my… then my other question is, what would be… what will be the release cadence between major versions? How long we will need to Keep maintaining, let's say, the… Well, the B1 for the.
**Pablo Baeyens** 19:37 people.
**Roger** 19:37 I couldn't receive them.
And also the other, let's say, question that I have is that Then we break the relationship, I guess, from the components to the semantic conventions, because I guess that if we mark the current host metrics as V1 and as stable, We need…
**Pablo Baeyens** 19:57 could.
**Roger** 19:57 to move the metadata metrics.
Stability to stable as well.
Right? Which won't be aligned with semantic conventions.
For that one.
Which makes it like a little bit weird, the relationship.
**Pablo Baeyens** 20:21 Okay, so, sorry, let me write down the… Like… the points that you made. So, there's one that is… You think it would help to have.
**Roger** 20:36 It.
**Pablo Baeyens** 20:37 The strategy written down?
Yeah.
**Roger** 20:40 Exactly what just, yeah, what Dan was mentioning about the…
**Pablo Baeyens** 20:46 Yeah.
**Roger** 20:47 For future major versions, we don't accept non-semantic conventions.
**Pablo Baeyens** 20:54 Yep.
**Roger** 20:54 And yeah, the release counts, but I think this is also like a general discussion for these components and for how long we need to keep this frozen version of… Oh, the whole metric receiver.
**Pablo Baeyens** 21:09 Okay, and then it was the relationship between component.
So, like, metric… And DataGen declared Stability and Semantic Convention Stability, I guess.
**Roger** 21:24 Yeah, exactly. Thank you.
**Pablo Baeyens** 21:27 Okay.
**Dmitrii Anoshin (Splunk Inc.)** 21:30 I'm sorry, but why is that so important to include host metric receiver in the 1.0?
**Pablo Baeyens** 21:36 That is an option we have. We could not include it in 1.0. It is.
a widely used component, and, like, it was on the list of high-priority components, but honestly, like.
**Dmitrii Anoshin (Splunk Inc.)** 21:48 We could.
**Pablo Baeyens** 21:49 I could change the RFC to say something like, Whatever components are ready to be marked stable, those will be stable, and… whatever else.
It will be marked stable later. I…
**Dmitrii Anoshin (Splunk Inc.)** 22:04 Yeah, so the migration to the semantic conventions is still important, and it's not going, like, as smooth as we would like. I'm not, like, saying, like.
It's like, it is what it is, but my… I'm worried that if we make it 1.0, it'll be, like, slowed down even more, and we, like, it'll take another 5 years.
To migrate.
**Pablo Baeyens** 22:33 Right, yeah, so I think the options we have are, and I wrote that on the notes, at least the options I can think of are, we keep things as is on the current state of the ROC. I think that's a bad idea.
We don't mark the host metrics receiver as V1 until the semantic conventions are stable, and we change the RFC to say that some components may not be V1 by the time the core distro goes V1.
Or we don't mark the host metric receiver as V1, and we don't mark the core distro as V1.
I feel like that one, that last one would be… Bob? I, I… at least if we are able to get other components to be one, I don't feel like… We should block it.
I think was.
**Braydon Kains (Google LLC)** 23:21 We can rule that last one out. We can rule that last one out for sure. I don't think we would block the V1, like, if we make the decision.
We wouldn't block the V1 distro on host metrics.
I think it would… there would probably be users that would be, like.
I need host metrics receiver, I need host metrics receiver, therefore I will not move.
But… That's fine, it's in the.
**Pablo Baeyens** 23:46 Yeah.
**Braydon Kains (Google LLC)** 23:47 Exactly.
**Pablo Baeyens** 23:49 know.
**Christos Markou** 23:50 What in what condition the rest of the components from that list are.
Like, file log receiver, and… when it comes to this discussion compatibility with semantic conventions.
**Braydon Kains (Google LLC)** 24:05 FileLog receiver, at least, is in a decent shape. I have a few things that I want to go on a personal crusade to go fix before we decide to mark V1, some fundamental things that I dislike about it.
But, It's in pretty good shape overall, like, I don't think we're gonna go fundamentally rewrite the way stanza work anytime soon before, before V1, so I think it could make it for, for KubeCon EU.
**Dmitrii Anoshin (Splunk Inc.)** 24:32 That, like, the whole rewrite of Stanza's concept, it kind of makes sense.
In general, but I do agree that it's definitely not something we would like to… delay we want for. It's completely different from semantic conventions with the host metric shield. There is no, like, real big.
Diversions from something else, which is stated in OpenTelemetry.
**Pablo Baeyens** 25:00 Okay, then, I mean…
**Braydon Kains (Google LLC)** 25:02 Pretty good shape too, right? I think, I think it's close.
**Pablo Baeyens** 25:05 Yeah, Prometheus receiver, there's… One big discussion on the spec that needs to be, resolved.
I've spoken with Arthur about it, he felt like, yeah, it will get resolved.
But otherwise, I think it's in pretty good shape.
**Dmitrii Anoshin (Splunk Inc.)** 25:28 Pablo, what's the… what's our, rule, guidance going forward, of marking really builds particular versions. So, for example, we're not gonna be aligning all of the components to particular major version.
Within.
**Pablo Baeyens** 25:48 the.
**Dmitrii Anoshin (Splunk Inc.)** 25:48 It's right within one, like, core distribution, whatever. What do we say? We say that distribution version is the minimum version of all of the companies, or there is some other role? Because they will diverge going forward anyway.
**Pablo Baeyens** 26:05 So, the RFC says that we will define a mechanism to opt-in into unstable parts. I've been speaking with Brayden about that, on… we spoke about it on one of the KubeCons as well, I think a bunch of you were there. Like, having some sort of min stability level CLI flag, or something along those lines, that by default is stable on a… distro that is B1, but if you want to use unstable components, you can do it by passing that flag and saying, like.
Beta, and then you can use beta or other components, or alpha, you can use alpha, beta on Oh, sorry.
**Dmitrii Anoshin (Splunk Inc.)** 26:49 So.
**Pablo Baeyens** 26:49 Stables.
**Dmitrii Anoshin (Splunk Inc.)** 26:50 So you… yeah, my question was mostly about diversions between V1, V2, V3, etc. But even if we speak about stable and unstable, you're saying that will be additional, like, kind of feature flag that you need to explicitly set. So we build We can build V1 distribution with zero components, but zero components will be behind kind of a feature flag.
**Pablo Baeyens** 27:16 Yeah, that's… that's the gist of it. I think that will be the.
the whole discussion of a different RFC, but yeah, that would be, at a high level, what I would want to do.
**Dmitrii Anoshin (Splunk Inc.)** 27:28 I think that makes sense, and that… that how can we include the host metrics receiver in that one.
**Pablo Baeyens** 27:33 Right, yep.
**Dmitrii Anoshin (Splunk Inc.)** 27:34 Okay, that makes sense. But I was talking mostly about future, like, for example, if we decide to freeze HostMetrics 3.0 for V1, and we want to make it still quicker to V2, It'll be V2, but distribution will be V1, at which point distribution becomes V2, essentially.
**Pablo Baeyens** 27:54 Yeah, I don't know what will happen with me to… versions of components, but… I… I don't think…
**Dmitrii Anoshin (Splunk Inc.)** 28:03 problems.
**Pablo Baeyens** 28:03 Resolve that right now.
**Dmitrii Anoshin (Splunk Inc.)** 28:05 Different discussion, yeah, just like… Just for thinking.
I'm sorry.
**Braydon Kains (Google LLC)** 28:10 It is somewhat tangled up with this, though, where, like, I actually still don't have a good sense… maybe the RFC does say this, and I forgot, but, like.
Are we thinking that a component can decide to go V2 whenever it feels like it? Or is there going to be a release train? Like every six months, everything that's…
**Pablo Baeyens** 28:27 be.
**Braydon Kains (Google LLC)** 28:28 Stabilize can…
**Pablo Baeyens** 28:30 The RFC doesn't say anything about that. Okay.
**Braydon Kains (Google LLC)** 28:32 Okay, yeah.
**Pablo Baeyens** 28:36 Okay, so going back to the question about the components, the resource detection processor, it's in a similar state, I would say, to the host metrics receiver, in that there's a lot of conventions there that are unstable, and a lot of things that were there even before semantic conventions existed.
as a concern.
**Dmitrii Anoshin (Splunk Inc.)** 28:55 Yeah, it makes sense to do the same for that one.
**Christos Markou** 28:57 That's even more important, I think, resource detection, because SDKs have their own resource detection.
Research detector, so… When an application runs on GCP, for example, it detects a cloud, fetches.
**Braydon Kains (Google LLC)** 29:11 Sorry, I'm losing my room. I'll… I'll…
**Christos Markou** 29:14 So if we have divergence there, I'm saying is more critical because signal.
**Pablo Baeyens** 29:21 additional.
**Christos Markou** 29:21 be impossible, specifically for this one. Even more impossible compared to host metrics, I guess.
**Pablo Baeyens** 29:29 Yeah.
So I think we have a few options there.
One… So… Okay, let me write similar state to host.
I think it is more… permissible there to gate a bunch of detectors, and say, like, these detectors are unstable. That… that I think would be fine for the resource detection processor.
But still… There's going to be a few that are widely used on that, like.
we're not going to have the semantic conventions stable by Kipcon EU, I would say. At least not all of them.
Maybe one thing to think about there is look at what the… Different SDKs do?
Because I think there are… SDKs that have I don't know, a host ID detector, or an AWS detector, and those are… V1 or V2 or whatever, even if the conventions are not V1 or V2?
Yeah, okay, I'll shoot you on Slack, Roger, and… We can talk about a couple of things.
**Dmitrii Anoshin (Splunk Inc.)** 31:00 I think a similar problem Pablo is offline.
Similar problem with receiver, so if we choose one or another, I think we should stick to the same. I don't have any agenda. I can talk about, my stuff.
**Pablo Baeyens** 31:12 We can hear somebody else talking, I think, Dmitrii.
No.
Yeah, maybe.
Maybe the research detection processor is one that we need to look into in the same way as the HostMetrix receiver.
**Christos Markou** 31:31 Yeah, and on another note, I would maybe try to see what it would take for us to… I mean.
Is this that unrealistic to say that by March, we really focus on stabilizing a subset of semantic conventions that are required by these components? Even only the ones that are — I'm thinking of research detection processors specifically.
**Pablo Baeyens** 31:56 Maybe.
**Christos Markou** 31:56 Maybe the attributes that are enabled by default are not that many. So, potentially, if we manage, if we make it to stabilize them.
We can proceed and have a subset of enabled by default attributes that are stable, the component is also stable, and the rest of.
**Pablo Baeyens** 32:18 sounds.
**Christos Markou** 32:18 are still experimental, which is fine. So… At least that makes the situation a bit better, I guess.
**Pablo Baeyens** 32:26 Yeah, Okay, I could look into that. To finish the list, so we have 1, 2, 3, 4, 5, What else was there?
Sorry, let me check.
Well, the security attribute processor we are done with the And then there's another one that I'm not remembering right now.
Well, while I look at it.
Since there's some of this strategy that is specific to the host metric receiver.
What do you think about… having some sort of document on the host metric receiver folder, saying like, this is how we we envision this.
And I can link to it from the RFC, but, it would live independently of it.
Yeah.
Yeah, of course, the one that remains of Elms Ridge, which we're seeing. Yeah, so this is the full list of clients.
Yeah, we could announce that.
Brayden, would you… I mean, I don't know. You volunteered to do the other one about, mint Stability, but if you have the… Idea in your mind, would you be willing to write something down on the postmetrics receiver?
Okay, yeah, I mean, if it's… if there's something from what you sign up that you don't want to do anymore, let me know.
Okay, I'll… I'll try and post a summary of this discussion on the RFC And.
Yeah, I'll talk with Roger.
I'll probably put something on on auto system metrics so that everybody can see it, but I'll Post something on Slack.
We are a bit over time, so I don't know.
Maybe we can leave it here, or… Yep.
**Christos Markou** 35:07 Sounds good. Thank you. I'll see you.
**Pablo Baeyens** 35:11 Alright, see you.
