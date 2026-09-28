SIG: Prometheus WG
Date: 2026-09-25
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Arthur Sens** 00:45 Hello!
**Carrie Edwards (Raintank, Inc. – Grafana Labs)** 00:47 Hi, how are you doing?
**Arthur Sens** 00:50 Pretty good, how are you?
**Carrie Edwards (Raintank, Inc. – Grafana Labs)** 00:52 I'm okay.
**Arthur Sens** 00:56 Merry's everybody.
**Carrie Edwards (Raintank, Inc. – Grafana Labs)** 00:59 I don't know.
I know, like, Cryo's on, PTO right now.
**Arthur Sens** 01:07 Yeah, yeah, I think cryo, I know.
Hello.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 01:12 Hello?
Hello, Carrie.
**Carrie Edwards (Raintank, Inc. – Grafana Labs)** 01:18 Blue.
**Arthur Sens** 01:51 Hello, Jack.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 01:55 Hey, what's up?
**Arthur Sens** 02:30 I assume we all… Discussing the same as, two weeks ago?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 02:39 Yep.
**Arthur Sens** 02:40 Okay, let's wait for David.
I send David a message.
**David Ashpole (Google LLC)** 04:05 Hey, sorry I'm late.
**Arthur Sens** 04:05 Hello.
**David Ashpole (Google LLC)** 04:07 At the half-hour mark as well, unfortunately.
**Arthur Sens** 04:11 Okay.
Then, let's get started.
**David Ashpole (Google LLC)** 04:20 Yep.
**Arthur Sens** 04:22 so David wrote a new page, like a very short summary of the 65-page discussion.
I saw that, Arve put some notes.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 04:41 Yes, and I also made sure to rewrite my designs, which are options C and C.1.
So they are much more compact, and I moved a detail into an appendix, just so that's clear.
**Arthur Sens** 04:57 Alright, I see.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 04:59 And I also added, like, a new design proposal.
Which is, like, option E, which is an extension of options C0.1.
Basically, kind of, to, to try to propose how… how we may phase out job and instance as the labels for representing auto resource identity, so they can represent scrape target identity instead, so… Yeah, just wanted to kind of mention that. That's also in there now.
**Arthur Sens** 05:39 Okay, I see that it is a lot bigger than when I saw a few days ago.
Has everybody had the chance to read this?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 06:33 What is this referring to? The thing Arve just mentioned, or David's one-pager?
**Arthur Sens** 06:39 Both, I guess. David's page and Arve's page.
**David Ashpole (Google LLC)** 06:43 had a chance to read Arve's. I did that earlier this morning.
**Arthur Sens** 06:50 I read it a few days ago, but it's a lot bigger than when.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 06:53 By… by page, do you mean, like, my, the science author? It's like, it's not like I have a… It's not like I have made, like, a dedicated page, except for the appendix.
I would… I wouldn't recommend reading the appendix unless you need to dive into the details, I would recommend just reading, you know, reading your options C, secret 1, and E. D is also there, but that's basically to do nothing, and just stay with the status quo.
**Arthur Sens** 07:27 Yeah, I meant the tab.
Option C and T1, and
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 07:32 The tab… that is the appendix, I believe. That's why I said this. It doesn't contain the actual, design proposal, it's like an extension with details.
**Arthur Sens** 08:11 And, Arve, do you believe that we need to read this to have a meaningful discussion today?
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 08:17 No, I mean, that's what I said before, that I would not recommend reading the appendix before you feel the need to dive into details, if you see what I mean.
It should… it should be enough to read, options C, 0.1, which… which have been much more… are much more compact now in the main tab.
And you can also read option E if you want to kind of see, like, my proposal for… a phase… like, a Phase 2 migration.
after CE or C.1.
**David Ashpole (Google LLC)** 08:57 Are there any updates?
to, what, C or C1?
Defined that you want to share with the broader group?
Are there any big changes, basically?
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 09:10 Oh yeah, I suppose.
**David Ashpole (Google LLC)** 09:11 I've read the previous version.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 09:12 I did… I did make one correction, which is what you made me aware of, David, that Basically, when you receive entities, you have to compose the identity from the identifying keys on the… on the identities, plus the… the… the research attributes, which are not mentioned by any, entities.
**David Ashpole (Google LLC)** 09:36 Great.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 09:36 So that's the.
**David Ashpole (Google LLC)** 09:38 this company.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 09:39 In the meantime.
**David Ashpole (Google LLC)** 09:41 That doesn't actually change anything about, like, what C and C1 are…
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 09:45 I, I think it, I think it mostly…
**David Ashpole (Google LLC)** 09:47 Teacher-facing stuff, or…
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 09:50 I mean, yes and no. Yes, in the sense that it doesn't change anything fundamentally, it's just a correction for CNC.1.
Like, it doesn't affect what they propose, But, on the other hand, CNC.1, they do mention, how to deal with, entities when they become, A thing in the future.
**David Ashpole (Google LLC)** 10:17 I thought that was part of E.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 10:20 That is not what E, is for. The point, the point of E is, Basically, in the title, that, it's like, a suggested second phase, where where, resource identity is no longer, mapped onto job and instance, and, scrape identity is instead mapped onto job and instance, so then Option E kind of proposals, like, a phased approach to mapping resource identity to a different label instead.
**David Ashpole (Google LLC)** 10:58 Okay.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 11:06 So… We've been talking about this for a long time. We meet every two weeks.
I assume other people have a similar level of exhaustion about, like, you know, going back and doing other things, and then having to spool up on this complex topic every two weeks.
And so, I'm trying to figure out, like, what a path forward looks like, you know, there may be more solution space to explore, but at the same time, it is… it has been pretty thoroughly explored. There may be still stones uncovered, unturned, but many of them have been turned over. And so, you know, what I like about the document, the tab that David put together, is it's sort of like a highlight reel, and that's how people make decisions, right? So, like, if you can sort of summarize the different options into one or two sentences.
Then, you know, you know, at least that's for me. Like, you know, I'm not going to be able to incorporate 10 or 20 different factors into my decision making. There's going to be a couple of factors that bubble up and become the most important and dominate my process. And, So, you know, if… if we can… David's done that. I think E isn't represented on there. I don't… I don't know that it… like, it's sort of, like you said, Arve… it's a sort of phased extension to C and C1, so maybe it doesn't need to be, but it also helps you maybe see the… the future intent. So, it's the… it's useful in that respect.
But, like, you know, if we… if we all agree with the statements in David's document, in David's tab.
Then, at some point, you know, we just have to put it to a vote, or, like, some sort of consensus-gathering mechanism that doesn't require that we all agree.
Right? And maybe a vote isn't the right thing. Maybe, like, a straight democracy isn't the right thing, but, like, something that, that, like, you know, allows us to, like, you know, say what everybody thinks, and then disagree and move on if we have to. Because it seems like we're probably gonna get to the point… we're probably at the point where there's an impasse. Like, I don't think we're going to all agree.
And so, you know, what do we do from there? And so, like, I think what could be a useful thing to do is, like, focus on David's summary document and, like.
the statements in there, and like, you know, does everybody agree with the statements? If not, like, you know, the conclusions that you make from those statements, but, like, you know, the statements themselves, are they accurate?
And I, for one, I have two open questions that I'm sure is in the details doc, but, like, you know, 65 pages, and I have other stuff to do, so I spool up and spool down on this, and I don't have a perfect mental picture in my head. But, I wonder if other people have questions about the summary doc.
if we think that that's a useful approach, maybe we can try to do that here, is like, you know, clarify the statements in the summary doc.
And, and maybe, agree on a mechanism for how to, like, you know, state a final vote or something that, like, you know, that doesn't require complete consensus. But, you know, we all agree on the mechanism.
Such that, like, even if we disagree with the result, we're still committed to the result.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 14:43 Yeah. I want to say, I mean, there are still, like, some outstanding points in the… in the, dashboard tab.
For example, requirement 4, I don't think, is fulfilled by, option B, or option A.
And there's also not yet a requirement stated that, which I believe is actually part of hotel.
the requirement that, when you convert metrics from OTEL to Prometheus.
the hotel resource identity has to be part of the time series identity, because otherwise you get, conflicts. And, it is my, it is my claim that option C and 0.1, they fulfill that, that requirement.
**David Ashpole (Google LLC)** 15:29 Say that again? Sorry.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 15:31 M… I'm talking about the fifth requirement that I asked to add.
**David Ashpole (Google LLC)** 15:37 Oh, there's a fifth one. Did I miss it?
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 15:40 There, this, we are… you and I are having a discussion on that, like, it's the discussion… it's the comments on the requirements.
header.
**David Ashpole (Google LLC)** 15:50 must… must be forward compatible with the OTEL data model, or… Oh, no, yeah, you had the…
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 15:56 Yeah, I had a comment where I asked to please add the requirement that often resource identity must be part of corresponding Prometheus time series identity.
**David Ashpole (Google LLC)** 16:06 Yup.
Option E is the only one that solves that, right? By using a UUID.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 16:11 No, well, I mean, you can argue that, but… But my argument is that, effectively, Prometheus, according… and it follows the OTLP2 Prometheus spec in doing so, it treats, service, instance ID, service namespace, service name, as the de facto identifying resource attributes.
**David Ashpole (Google LLC)** 16:35 I mean, you can… So I think that's… resource identity, just… according to the resource spec, is all of the resource attributes.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 16:45 Yes, yes.
**David Ashpole (Google LLC)** 16:45 Right?
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 16:46 Yeah, so that, that, that is…
**David Ashpole (Google LLC)** 16:47 Do you have to use a UID, or have them all?
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 16:49 That is a very warm… that's a very well-known argument.
**David Ashpole (Google LLC)** 16:53 You can choose, and we have.
You can choose any set of resource attributes you want, and say, these are the ones that we're going to use as a join key.
They're not the full resource identity. Instead, they're a subset that we're using as a joint key.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 17:08 Yeah, I mean, that's a very well-known argument, but that's not… that's inconsistent, because it's the OTLP to Prometheus… we cannot disagree on this fine, but this is my argument, that it is inconsistent, because the OTLP to Prometheus conversion spec, it says the… You should use those three attributes.
That's… can I just finish? And those are… that… those are the de facto, identifying attributes, according to Prometheus' definition.
**Arthur Sens** 17:40 This is exactly the thing that we, like, I would say the requirement is to change this.
Like, we… like, this is… like, this is not working.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 17:49 Well, but I mean, how does option B fix it? That is my question.
**David Ashpole (Google LLC)** 17:57 I think if the Zipkin spec said that it was going to use some… hotel resource attribute to populate some Zipkin thing, we wouldn't take that to mean that, like.
the definition of hotel resource identity has been changed, right? Like, compatibility specs don't… Decide the meaning of hotel resources.
like… Option B, right? So, first.
Neither option B nor option C use how OpenTelemetry defines resource identity.
to make our join keys, right? Both of those… Make join keys by selecting a subset of the resource attributes that come in.
Right? So, in that way.
You can argue that one is a better join key, or one is a worse join key.
But I don't think you can argue that either of them meet the definition of… The resource identity.
We could use a UID, which would.
But, like, I think that's just an alternative proposal, and it has its own downsides.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 19:01 Yeah, but we also have to take into account backwards compatibility. So, I mean, this… I mean, this… I mean, I have made my argument, and I stand by it. And then there's to say… and then there's the question… so this is a backwards compatibility argument, and then there's the argument of backward… forward compatibility.
Which is that when, when, entities start, going into production, the design CNC.1, they will automatically, be compatible.
Because then, when they receive entities, they will use entities to detect, or to determine.
the identifying attributes. So that is… that is my argument, that they are…
**David Ashpole (Google LLC)** 19:46 What do you say?
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 19:46 In fact, it's forward compatible.
**David Ashpole (Google LLC)** 19:49 So, entities are themselves forwards compatible, or, like, backwards compatible with OTEL, right? Like, nothing breaks by the addition of entities.
So… any solution is going… that we introduce today will be forward compatible with entities. Now, when you say we use entities, what do you mean by that? Just, like.
The service attributes are now part of the service entity, so that that's good, and, like, we haven't defined an entity for these attributes that we haven't defined yet. Is that the…
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 20:24 No, what I'm saying… what I'm saying is that the OTLP2 Prometheus converter.
**David Ashpole (Google LLC)** 20:30 It's…
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 20:30 It will, see which are identifying.
according to the IT ID keys fields on the entities, and then it will… it will use those to compute which are the resources identifying attributes.
**David Ashpole (Google LLC)** 20:47 sorry, that, like, today we can look at a resource and find the resources identifying attributes, and tomorrow with entities, we will be able to look at a resource and find a set of identifying attributes, and do the same thing, right? Like, what's… What's this big… like, what's changing that has any impact on us?
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 21:04 What's changing is that… once… once entities are part of an OTLP payload, they are explicit about what are the identifying resource attributes, and then… then we don't… we don't… when… when entities are in the payload, we don't have to fall back to our current, Identifying triplets.
**Arthur Sens** 21:31 We can, for some time, ignore the entity payload and keep the current behavior.
And then we make the move once we are ready.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 21:44 But why… that is not really part of what we're discussing. What problem would that solve? I don't get it.
**David Ashpole (Google LLC)** 21:52 I mean, entity… like, so entities basically gives us a bunch of extra metadata, right? Like, and it'll allow some attributes to be marked descriptive.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 22:02 I mean.
**David Ashpole (Google LLC)** 22:03 Like, that's new stuff.
Right, sorry, you can go ahead.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 22:07 Yeah, no, I mean, this is what we discussed before, that they… explicitly, have a… every entity needs to have a field which says which, which, lists one or more identifying, attributes.
Yep. So,
**David Ashpole (Google LLC)** 22:25 So, is the question, how would scrape Job, and instance be represented in entities? Is that the, like, question that you want answered?
Or…
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 22:35 Is it something…
**David Ashpole (Google LLC)** 22:36 Or, do you production of entities somehow, like, Makes existing resource attributes mean something different?
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 22:47 I'm just making the argument that option B needs to define, how the OTLP to Prometheus converter should handle entities, because option C and C.1, they do define it, the scheme.
**David Ashpole (Google LLC)** 23:04 Right, why do they need to define that, right? Like… we… like, solving hotel compatibility with entities is a big problem, right? And it's something we've talked about, and we need to work on. And I think we've even written some designs in the past. Arthur, keep me honest.
But… Like, this is a non-trivial… Thing for us to take on.
And as far as I'm aware, option B doesn't reference any of the metadata that's in entities, so it should work before or after.
Entity.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 23:36 I think, you know, seeing… seeing this from the perspective of an implementer of OTLP to a Prometheus converter, since years now.
I do very much think that option B needs to define which scheme it will follow for for dealing with entities, because I think that if it follows the scheme of options C, C.1, then option B's whole purpose of, mapping Scrape target identity to drop an instance will fall away.
Essentially.
**David Ashpole (Google LLC)** 24:13 Why?
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 24:15 Because if it does, what options C and 0.1 will do?
It will actually, it will actually instead map resource identity to job and instance, because that is what they, what they, say they will do.
**David Ashpole (Google LLC)** 24:32 That's option E, right? Where we use a U.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 24:34 No, no, no, this is, this is actually in, in C001.
**David Ashpole (Google LLC)** 24:41 But it's not resource entity. We've already been over this. I feel like we're going in circles, right?
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 24:45 No, we're not going in circles, because… Because when you have entities, the definition of resource identity is the, the, the union of, of, I don't, research… identified by the entities and the research attributes, which are not defined. So, options C.1, they are clear, they say that you make a hash of all those identifying research attributes, and you put them on the instance label.
And that is not compatible with the purpose of option B.
**David Ashpole (Google LLC)** 25:23 So, sorry, are we… is CDOT… that's why I asked earlier, for updates to CC1.
Do up… do CNC1 propose using service instance ID?
as instance, or do they propose using a UID With all the resource attributes.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 25:46 Well, I'm, saying that it… options C and 0.1, they… they have two paths. They have, pre-entities, and they have, post entities. So… so the scheme, depend… for defining the identity, it depends on… Whether entities are present or not.
**David Ashpole (Google LLC)** 26:04 I think someone… like, we're about to start switching all of our SDKs over to be entity detectors, like… if someone… Upgrading their SDK results in them… getting a wildly different value for… I mean, I suppose you could make the case that Yeah, still, it's like… It seems weird to me that someone adding An entity, which is meant to be this… Backwards compatible piece of additional metadata is gonna now get wildly different.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 26:35 Well, I mean, if you think my understanding is wrong, I mean, you are… I would be happy if you can kind of point out,
**David Ashpole (Google LLC)** 26:43 I don't…
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 26:44 And it's more just…
**David Ashpole (Google LLC)** 26:46 I don't know if your understanding is wrong, I just… Can you… Am I wrong about the rollout? Like, so, from… As soon as one entity, like, gets added to the resource payload.
then we're gonna change the way that the Prometheus… that the O telta Prometheus translation logic works.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 27:09 It would have to be not one, I think it would have to be exclusively entities, like, there are no resource attributes that are not represented in the entities, right?
But still, the question remains.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 27:21 Yeah, but, yeah, but I guess, I mean, I've been involved, or, like, I've been following the entity, development since early on, so I know, sort of, like, the intention. The intention is indeed that entities, they are supposed to, define what are identifying research attributes. It's a problem that… The current definition, in theory at least, says that all attributes are identified. That's a problem that… that is explicitly one problem an entity data model is supposed to solve.
So, so, my point is that… that the OTLP, the Prometheus converter, it has to respect what is in the entities.
Maybe it could be discussed whether that needs some sort of, like, backwards compatibility rollout phase, I don't know.
But that is, like, the… that is the goal.
**David Ashpole (Google LLC)** 28:17 When you say respect what's in entities, you mean that… like… We are required to use the… resources identity. Like, once entities exist in a resource.
then we should be required to use the resource's identity as stated in the resource spec.
exists in a resource, we're not bound by the resource's identity in the end, or in the resource vector.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 28:43 So, this is basically, I mean, the scheme I've defined, which is, like.
pre-entities, we do what we do now, which is essentially just use those three attributes. And when entities are in production, we start respecting their identity definition.
**David Ashpole (Google LLC)** 29:05 That's when we switched to UUID.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 29:08 Yes, that's actually correct, yes, yes. And this is, like, an old… this is an old idea that also Jurassi had while he was still at Grafana Labs.
he had the… he and I, we were, like, discussing how we may support entities, and he had exactly the same idea as myself, just for reference, to kind of to make a hash and put it in the instance label.
**David Ashpole (Google LLC)** 29:30 We considered this even, like, 5 years ago, when we wrote the spec.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 29:34 Hmm.
**David Ashpole (Google LLC)** 29:35 Wow. It's…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 29:37 Maybe it would have been better if we did it back then.
**David Ashpole (Google LLC)** 29:40 Well, I don't know, I mean… I don't… Oh, sorry, I'm over time, so I have to go.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 29:47 Yeah, you gotta go, like, okay.
**David Ashpole (Google LLC)** 29:49 stops.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 29:49 Let's make async progress on David's summary doc, and then let's, like, figure out a mechanism to disagree and commit.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 29:56 Yeah, sounds good.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 29:58 Alright, I… David's… I think he's gone, he's… he's frozen. Yep.
Is there… is there a point to continuing the meeting without David here?
**Arthur Sens** 30:10 Do we have any other topics besides this?
Do you have any? Jonathan, Carrie, who… Nothing?
Cool. Then, I also don't have anything. I guess we can drop.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 30:28 I mean, if you want, we could, you know, talk about, like, the backwards compatibility concerns, like, like, I mean, I have mine, I don't know if Jack, for example.
You seem quite, like, involved in this. I'm, like, wondering if… If you… if there would be, like, concerns on your side on how this would hit users.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 30:50 The, the, so… like I… like I said, there's a bunch of factors that contribute or, you know, oppose each of these… each of these, options, and… but it really boils down to just one or two, or it will… maybe, like, one to three in.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 31:05 Ms.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 31:05 in people's mind, and one of the factors that is of high importance to me is the breaking change to the collector default behavior. When you have a Prometheus receiver.
translating to an internal OTLP representation, and then some sort of Prometheus export or scraper, remote write. And, so that, to me, is a really strong candidate in favor of option B right now, because, you know, we don't have data on it, but I suspect that that path.
is extremely common. So a change in behavior there is… is consequential.
The… I mentioned that I have questions about, like, these, you know, things that I'm sure are in the detailed explanations, but that, like, are sort of lost on me at the moment. So one of them that I think you could help answer, Arve, is, like.
What is the impact, in your mind, of option B on the Prometheus OTLP endpoint in, like, the short term? Like, which is, like, what you can… can get done in a MITRE version, and then if the… in the long term, like, if there is anything you would want to be… want to do differently after, like, a major version bump?
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 32:19 I think this is both… I think option B… I've probably said this before, but I think option B is problematic both in the short term and the long term.
That's something I remember we discussed during Grafana Fest in person, that I made the point that it's both backwards incompatible, so we cannot do it before the next major version of Prometheus.
But even after a presumed next version of Prometheus, it would be problematic, because… So, when it comes to backwards compatibility, like, like, if, if people are sending, some, some input, that change, that, changes, Prometheus Prometheus to start using their scrape identity instead, then they get a new, they get, like, a new join key.
So that's, like, that's backwards, that's breaking backwards compatibility.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 33:18 So that…
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 33:19 No.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 33:20 I remember you saying that, and now, like, I'm reading this summary doc, and the assertion that David makes in the summary doc is that, like, option B has no breaking changes to anything. And, like, and so then…
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 33:31 This is David's perspective, you should see all my comments. I 100% disagree, and I gave exactly the argument why it's not… it's backwards… it's breaking backwards compatibility.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 33:44 So, like.
you know, the… the… what I propose is that we… we sort of, we argue and debate about, like, the facts on this summary sheet, and then we can take it to some sort of, like, voting mechanism to disagree and commit. This is, like, an example of, like, a fact that I want to get to the bottom of.
Like, and so I, you know, I'm gonna leave a comment on this document that is being… that just basically is calling this out explicitly. You know, does option B, have any breaking changes for the, the, you know, the Prometheus OTLP endpoint behavior in terms of the labels that people see?
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 34:22 I mean, David does say at the end that option B makes a braking change, then UTF-8 is enabled. I'm a bit uncertain if that means what I meant.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 34:32 I think he's referring to UTF-enabled, 8 enabled for the, the collector, like, the collector.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 34:38 Yes. Prometheus.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 34:39 receiver.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 34:40 Yes, I know, but it's a bit difficult to follow, like, mentally, the chain from there.
Yeah. So that's why it's difficult for me to pin down right now if that kind of leads to the scenario I described.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 35:01 Well then, I'll leave a comment and, like, you know.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 35:05 But it…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 35:05 We shouldn't get to the bottom of this, or we should, like, you know… I don't know, this seems like an area that is… it either is or it isn't, and, like, maybe we're not saying the right words, we're talking too generally right now, but this is an example of the type of thing I want to tighten up.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 35:21 Yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 35:22 And, yeah, because, like, I don't want to say that I support option B, for example, like, without knowing that it, like, breaks the Prometheus OTLP endpoint.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 35:31 Okay, let me see now. So I see requirement 3 is that SDKs sending OTLP to Prometheus must see no change in behavior. Option B doesn't meet that requirement. I'm going to comment on that.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 35:45 Okay,
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 35:46 I can tell you why it's not true, because if I, as an SDK, a REST SDK client, send OTLP payloads to Prometheus.
and I include Prometheus.job and Prometheus.instance, there will be a change in behavior.
like.
**Arthur Sens** 36:04 But nobody does that.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 36:06 But they can do it. So when we at Grafana Labs investigate escalations around OTL, and they are many, and they are increasing in frequency, we cannot assume that they have not done that. Customers do insane things.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 36:25 Okay, so, okay, so write that down, like, leave a comment to that effect. You know, it's useful information to have. Like, in my head, my first reaction to that is, like, it's gonna break some people, but, all these… all these solutions break at least somebody.
And, and so, like, I'm thinking about, like, orders of magnitude. Like, like, what's the impact of the break? And, you know, like, again, we don't have data, so we don't know. We should just have, like, intuition based on our experience with customers and experience in, you know, in open source and issues and whatever, so…
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 37:00 Sorry, sorry, I, I missed, I missed David's, escape hatch. He has an escape hatch in options… sorry, in requirement 3.
Because it says that, he, he makes an exception for when they send Prometheus.job on Prometheus. instance. So, I will leave a comment on that escape patch, because I think that, that escape patch, it does not help if you are, like, handling escalations. I already have, like, I already have, like, a bank of, of, escalations related to offline identity, and they are terrible to investigate.
So if we have this, like, if we have option B, if you're going to have another dimension, according to which we have to investigate. So it's going to put more load on the shoulders of, of, Mimi or team members.
It's, is the thing.
Right, so, you know…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 37:58 Should option C and C1 break? Maybe C1 doesn't, but, like, I guess that's a… that's a question. So, so… C1, This case is really heavy, it's really load-bearing in my mind, of, like, the Prometheus receiver with defaults and the collector.
So, like, Prometheus receiver to OTLP internal representation to Prometheus exporter, slash, like, Prometheus RemoteWrite. Like, I think that's extremely common. And so, breaking that common case, you know, is load-bearing. And so, I have it written down here that C breaks that.
But C1 does not.
C1 has, like, a special tweak that makes it so that case is fine, but it… in exchange for that special tweak, it gives up the UTF-8 consistency. Like, it's now dependent on whether you have UTF-8 enabled or disabled.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 38:51 Yes, I think I know what you're talking about, that C.1 has this, like, automatic translation built in, where it recognizes service underscore name, for example.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 39:02 Hmm.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 39:03 It recognizes it, and it says, this, hey, this is service.name.
So C, so C.1, it basically offers the alternative, that if you don't want this behavior.
of automatic recognition of identifying attributes, C.1 is your, is your math. Like, it, it allows, like, allows you to… so that's why I made those little two alternatives, that one can choose whether that behavior is desired or not.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 39:30 Yeah, and just, like, my read is that C.1 is far more desirable because it doesn't break the default case.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 39:37 And…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 39:37 My intuition is that the default case is much more common, and therefore it warrants a lot more protection.
So, okay, that's good info. So, B breaks the Prometheus OTLP endpoint when, when Prometheus job and Prometheus instance are present, and, you know, it's debatable how common that is, but at least that's a… that's a fact.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 39:59 Yes, And my argument for why it's, like, the wrong design, also, after backwards compatibility is no longer a problem, is that it introduces, like, schizophrenia, where, like, or an ident… like, an identical to the confusion, because… when… when Prometheus.job and Prometheus.instances are not there, the Prometheus behaves like now. It treats… it maps OpenTelemetry resource identity to job and instance. But if Prometheus.job and Prometheus.instance are present.
present, it says, hey, I'm going to map a scrape target identity onto a job and instance. So that is going to be an absolute nightmare to, to support.
Like, like, like, when our customers ask us why… the join… sorry, job and instance labels, the join… their join keys, are not what they expect, then all of our team has to be aware that job and instance can either be a scrape target or resource… or auto resource identity, depending on what the customer has sent, and typically this customer does not know what they have sent.
So…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 41:21 So I agree with that. Isn't it true, though, that we have sort of an escape hatch to that by just saying, like, hey, don't look at the values of Java and instance at all, treat them as an opaque join key, and go fetch the information you actually need from the target info?
Isn't that, like, universally good advice after, like, whatever path we choose?
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 41:42 I don't really… I don't really think that would help us. I don't think so.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 41:46 Why not? Isn't all the information?
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 41:50 Because we would… if our customer comes to us and says that, They, that, you know, the identity is messed up somehow, and that there can be, like, a number of ways the identity is messed up. I can just look at the escalations we got already.
then we have to go and, like, ask them, are you, are you sending scrape.job and… sorry, Prometheus.job and Prometheus.instance?
that's the first thing you have to ask, and we have to be aware of that. So it's basically going to make, like, the, The, the, like, the support procedure, troubleshooting procedure, much more complex.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 42:30 A big switch statement.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 42:33 Yeah, exactly. That is exactly the thing, and I… I cannot doubt that my team members, who most who, for the most part, don't dive into hotel.
I, I…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 42:45 You gotta find a way to have that represented on this summary sheet. Like, that, you know, like, maybe it is, but, like, it's… it's… the lead is sort of buried then.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 42:56 Well…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 42:57 It's not like… inch.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 42:59 The thing is that that's, like, David's summary. I… My, my summary is represented fully in the consensus section.
So I, I, I, I think… I think, personally, that we should follow normal design doc practice and, and, decide, put all our… our opinions in the consensus section.
And, and decide there. The David's tab is, of course, going to reflect David's, opinions.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 43:32 Yeah, right. The problem is that normal design docs aren't 65 pages long and, you know, debate over the course of 6 months, and.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 43:40 doc.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 43:40 constantly being updated.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 43:42 I think a problem… I mean, my sections are now short, or relatively compact, so the… I think there's content added by Cryo, maybe, which should be moved into an… into an appendix.
And the design doc was also not written in a normal design doc format originally, so it made it… I had to put, like, a lot of extra information into the C section that I normally would not have to do.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 44:10 Yeah, yeah, yeah, so there's challenges. Ideally, you know, at least in my head, there could be a summary section that stated things as fact, and, you know, you know, I think it's… David's is mostly fair, I think it's, like, bending in some ways, and, like, you should correct that.
I guess you don't have to. We can debate about.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 44:34 Yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 44:34 mechanism by which, like, we articulate, you know, our opinion and the summary of the different cases. But in my head, a short summary summarizing 65 pages is a decent way out at this point.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 44:48 Yes, sure, I mean, like, I've kind of, like, followed up on David's time by leaving, Like, a number of, of, comments.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 44:58 Yeah, right, you definitely have. So,
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 45:01 And then we… but then we end up… David and I end up discussing things like what should be… should there be a fifth requirement, for example? I… I think so 100%, but it's… it's still being debated.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 45:14 So I guess, like, what's sort of buried in your comments done, and doesn't jump out of the comments, is, like, the stuff that isn't strictly related to the requirements or the problems, but is still part of the reality.
like, you know, the maintenance burden of somebody that's supporting, you know, Prometheus and having to deal with these, this schizophrenic situation where you.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 45:36 Hmm, sweet.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 45:37 switch statement to decide where you're in. Like, that's… that's part of the argument. You know, it's not… it doesn't come out in the requirements, because, you know, technically, you know, you can still debug that, but it's just more complicated to debug that, because you have to be aware of these different cases.
So that's more of, like, a soft point. It's not, like, a hard point, like, you know, this option meets or doesn't meet this requirement, but it still, like, warrants consideration, and maybe for some people, a lot more than others.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 46:05 Well, I think that's, basically, an argument for using the consensus section as the reference.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 46:17 Yeah.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 46:18 Like, like, all my, you know, all my arguments are there. I'll see if I should add more.
In David's time, I can only, you know, interact via comments.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 46:30 Really? I mean, are you just, are you saying you don't have edit permission, or you don't want to jump in and, like, you know, take… sort of scramble the document by having multiple authors?
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 46:42 The lecture, because, I mean, it's David's tab, and I think, like, the main tab is, like, that is the source of truth.
Whatever.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 46:56 Well… So we're sort of… we haven't even reached consensus on the mechanism by which we reached consensus.
So we have work to do, and, like, I guess what I suggest is that, like, unless we wanted this to drag on forever, we work asynchronously to, and persistently to, you know, maybe not agree on the outcome, but agree on the mechanism by which we, like, decide the outcome.
You know.
I'm hearing from you that the traditional design doc, you know, thing where we… you state your consensus, and you can elaborate on all the bits over in the main tab, that's your preference. I've stated in the past, and, you know, I still think this way, that a summary of a 65-page document with, like, facts, where everybody can agree on those facts, is a good way forward, but we need to… the facts need to be not biased.
If that's going to be, like, the way that we look at the situation. And so, if that's the case, it can't be purely coming from David, and, you know, David has to sort of represent the other views. And so, But yeah, like, let's hash that out and get the.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 48:10 Right.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 48:12 to,
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 48:13 Yeah, exactly.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 48:15 Let's not wait 2 weeks, because it's… it's exhausting.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 48:17 Yeah, like,
**Arthur Sens** 48:19 like…
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 48:19 Yup.
**Arthur Sens** 48:20 And next week… as far as fun of folks, it's Hackathon.
The week after, it is PromCon.
So, we are going to miss the next meeting anyway.
And then… That just means to me.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 48:37 More asynchronous work.
**Arthur Sens** 48:39 Yeah, yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 48:39 this is higher priority than Hackathon, so, I'll… to the extent that other people are willing to engage, I'll engage asynchronously.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 48:47 I can join the next… so is no one of us joining the call? I mean, I'm not going to do any… I mean, I'm not formally joining that call.
**Arthur Sens** 48:55 Okay, yeah, me neither. I'm focusing probably on this.
Alright.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 49:01 So, yeah. And also, you know, I'm ready to commit and disagree, So, sorry, I'm ready to disagree and commit, I mean, sorry. But, yeah, I… but I will, you know, have to kind of discuss with Mimiu team about the potential ramifications of option B.
And I think it… I think we would not implement option B, just to make that clear. That's what I think, at least, because of the consequences.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 49:28 So, Just, like, a frustrating reality of these types of debates is that, you know, like, even if this group comes up and is like, hey, this is the direction we think we go, there's, like, still another threshold that you have to pass, which is, like.
you have to open the spec PR, and, you know, everybody else that isn't involved in these debates has the opportunity to block and, you know, derail it again. There's this issue that I was debating. It's the longest… it's the most commented issue in the OpenTelemetry spec history. It has something like 250 comments, or something like that. And, you know, I debated with the… this group, this declarative config sig.
For months, and we had all this proposal process, and, you know, we drew the line in the sand, and we said, like, hey, we're all gonna make our proposals, and then we're gonna, like, vote and commit to the result. And the result that we all voted and committed on, and the process that we agreed on, it didn't mean shit when we, like, proposed it to, like, the broader community. We had to, like, re-litigate the whole thing.
And so, like.
I don't know, that's, that, that's exhausting, it's, it's, but it's part of the reality, and so, like.
the takeaway for me is to not get too attached to any particular outcome now, because it's not the final say until it's, like, something is merged. And the other thing that you just said is, like, additional color to it, which is, like, you know, even if OpenTelemetry says something, if Prometheus if Prometheus does, as a community, doesn't, like, agree with that decision and goes in a different direction, then, like, the open telemetry governance cannot solve this unilaterally. And so that complicates this even more than, like, a normal.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 51:12 Yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 51:12 OpenTelemetry-specific problems.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 51:14 Yeah, I was more… I was more specifically referring to the Mimir product. I didn't really say anything about Prometheus, even though I have my opinion, for sure. Sure.
I'm just saying, like, I'm just saying that I don't think this would be, viable at all, for, for, Grafana tricks. I don't think so.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 51:37 Well, then, like, that's a really important thing that needs to be on the page. Like, whoever, whoever is, like, and we can, again, we can debate on, like, you know, like, who has a say, like, I'm not even sure I deserve to have a say, because, you know, I'm not enough of an expert.
So that's, like, a separate conversation, but, like, for whoever eyes you want to influence, or have a chance at influence, you have to, like, make that point about the maintenance burden and the repercussions clear. That's not just, like, it's just not represented right now, and it's a really important thing.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 52:09 I have to…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 52:10 It's represented… and your conclusion, like,
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 52:14 Yes, you're concerned.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 52:15 is…
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 52:16 And that is… that is, in my opinion, the source of truth. Sure. That is definitely, my argument. Like, like, I cannot, I cannot, you know, have my opinion reflected in David's, summary, if you see me.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 52:32 Well, I'm gonna talk to David about that, like, the summary section, if that is the mechanism that we want to use to.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 52:39 To summarize.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 52:39 Then it has to be, like, as unbiased as we possibly can, or at least representative.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 52:45 Yeah, so I think, you know, I might repeat the argument I made before. I mean, I think the better solution is to trim down the main design look.
I've done my part, you know, by trimming down my designs. I mean, you cannot, you know, you cannot count the appendix as, like, you know, part of the main dock. Right. So, so, if people can say that my sections should be more compact, I mean, feel free to do so.
But I think the fact is elsewhere right now. I need to trim down my consensus. I haven't got to that point yet.
There's also a time factor here, like, I don't, you know, work on… I don't work on hotel full-time, let's say. I carve out… I carve out time, so the length of my sections can reflect that.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 53:46 Yeah, yeah. And, you know, the longer we let this drag on, the more collective time it eats away at all of us, so… Okay, I'm gonna give that feedback to David. I think I understand your point of view, and Yeah, so I'm gonna, I'm gonna side-channel him, so…
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 54:05 Hmm.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 54:05 And let's work asynchronously. So, look forward to messages, comments, and… But yeah, let's not let this drag on without any conversation for another 2-4 weeks, so…
**Arthur Sens** 54:17 Okay.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 54:19 See you, see you in a week, I suppose.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 54:22 2 weeks.
**Arthur Sens** 54:23 We'll be a prong hunt.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 54:26 So then…
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 54:27 I'm joining next week, at least.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 54:29 There's no meeting this week, it's a bi-weekly.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 54:31 Okay, unless it's bi-weekly, though, that's correct.
That is correct. Okay, so…
**Arthur Sens** 54:38 We see each other in the mouth.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 54:40 see each other at Promconden.
**Arthur Sens** 54:43 Yeah, or at Prometheus, yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 54:46 Alright, take care.
**Arthur Sens** 54:48 Bye-bye.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 54:49 Thank you, bye-bye.
