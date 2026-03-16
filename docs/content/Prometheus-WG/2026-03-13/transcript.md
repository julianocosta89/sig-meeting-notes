SIG: Prometheus WG
Date: 2026-03-13
Duration: 61 minutes
============================================================

## Zoom Recording Transcript

Arthur Silva Sens 00:01:00 Hello!
David Ashpole (dashpole) 00:01:27 Hong Kong Nursi?
Arthur Silva Sens 00:01:29 Yep.
Looks like a new rule.
David Ashpole (dashpole) 00:01:37 There we go. Okay.
Yeah, yeah, this is my wife's nicer office.
Arthur Silva Sens 00:01:44 Nice.
It indeed looks nice… nicer.
David Ashpole (dashpole) 00:01:49 You don't like my bed? My unmade bed?
Arthur Silva Sens 00:01:55 You even have two cameras now. Hello.
David Ashpole (dashpole) 00:01:58 Well, it's… Yeah, that's.
Andrej Kiripolsky (Grafana Labs) 00:01:59 Bye, folks.
Arthur Silva Sens 00:02:05 Let me start preparing the notes.
PhD.
Andrej Kiripolsky (Grafana Labs) 00:02:26 In the meantime, I can just quickly introduce myself, because I haven't met with David yet. Hi, David. I'm Andre, I am a user researcher from Profile Labs.
And I believe we actually were in touch about some stuff a while ago?
But it's, yeah, it's been, it's been a while.
David Ashpole (dashpole) 00:02:46 possible.
Nice to meet you.
Andrej Kiripolsky (Grafana Labs) 00:02:49 Yeah, nice to meet you too.
Arthur Silva Sens 00:02:59 I talk too much.
So I put your topic as first one, Andre, is that okay?
Andrej Kiripolsky (Grafana Labs) 00:03:06 Yeah, yeah, although, like, this is very much of, like, an open-ended topic that we can… we can just keep talking about for a long time, but I can… I can start. So… Yeah, or shall I start?
So, it was… Arthur Silva Sens 00:03:19 Go ahead.
Andrej Kiripolsky (Grafana Labs) 00:03:20 Okay, cool. So… I work with Seek End User in OpenTelemetry, and we do surveys quite regularly, and a while ago, you folks did a survey together with Seek End User about pentelemetry and Prometheus interoperability, and we now have empty survey backlog, so I reached out to Arthur if you folks would like to run another one.
And, yeah, Archer came back to me with 3 questions that you folks came up with. It's a… one is about SDK preference, one is about… exporter, preference, or it's, like, exporter versus… what's the second thing? Receiver. And the third one is about… Query less, or query… like, manual query writing versus query less, experience.
And, yeah, first of all, I just want to say hi, that, like, I am going to, like, a… pop up here, or we might meet at KubeCon as well. That's… that's one important thing. The second is, I want to ask if there are any other Questions that came to your mind in the meantime, like, since last week?
Arthur Silva Sens 00:04:37 Yeah, and for some extra context, I asked… Andre reached out to me, and I… we had a meeting, the last meeting. Neither David or Crya were present.
David Ashpole (dashpole) 00:04:50 It was mostly Kyle and Arv and I.
Arthur Silva Sens 00:04:55 Coming up with questions.
Andrej Kiripolsky (Grafana Labs) 00:04:56 Yeah, so that's even better, that we now have folks that didn't have a chance to, like, give their input.
So, cryo, David.
Yeah. Yeah. Anything in this area interesting for you?
David Ashpole (dashpole) 00:05:11 Well, I'm… first… So, exporter preference is clearly, do you want to use a Prometheus.
Andrej Kiripolsky (Grafana Labs) 00:05:18 endpoint, or do you want to push with OTLP?
David Ashpole (dashpole) 00:05:21 Right.
Andrej Kiripolsky (Grafana Labs) 00:05:23 So the way how Arthur phrased it is that, do people prefer to run Prometheus exporters or hotel collector receivers?
Is it the same thing, or is it something different?
David Ashpole (dashpole) 00:05:35 Prometheus Exporters, or… Arthur Silva Sens 00:05:38 Oh, so this… So this is perfect for infrastructure.
David Ashpole (dashpole) 00:05:42 ICAC. So, do they prefer the node exporter or the host metrics receiver?
Arthur Silva Sens 00:05:47 Yeah, we don't need to be very precise, like, node exporter versus host.
David Ashpole (dashpole) 00:05:55 But… I'm just giving an example, yeah.
Arthur Silva Sens 00:05:58 Yeah, okay, yeah, that's an example, yes.
Andrej Kiripolsky (Grafana Labs) 00:06:02 And, David, can you repeat what you mentioned at the beginning? Like, how did you understand it first?
David Ashpole (dashpole) 00:06:09 So, when I read it, I first… because one of the things… we have, like, two nearly identical export paths from SDKs. You can set up a Prometheus exporter, which is Exposes metrics in the text format.
as an HTTP… Andrej Kiripolsky (Grafana Labs) 00:06:27 scrapable thing.
David Ashpole (dashpole) 00:06:29 Or you can push via OTLP, right? So I thought this was a, do people prefer the pull or push approach? Say they're going to a collector.
I assume they would prefer OTLP in some cases, but I've also I also feel like many users I think it kind of depends on whether you're, like, mostly open telemetry with some Prometheus sprinkled in, or mostly Prometheus with some OpenTelemetry sprinkled in.
Which is also an interesting question.
Andrej Kiripolsky (Grafana Labs) 00:07:03 Yeah, yeah, absolutely, absolutely.
David Ashpole (dashpole) 00:07:06 hotel, like, the… OTLP exporters are just better supported across the board right now, so that is probably also a thing that sways people.
But I would love if people were able to be successful with the scrapable endpoints as well.
I agree.
Arthur Silva Sens 00:07:24 Is this information, like.
if we understand if people prefer Prometus Exporter or OTLP Exporter, would that change any of the things that we have planned for the future?
David Ashpole (dashpole) 00:07:37 No, I don't think it would.
Arthur Silva Sens 00:07:39 Yeah, so I… yeah, I feel like this is… David Ashpole (dashpole) 00:07:41 I don't think this is a question. I was just saying how I interpreted the exporter preference.
Item.
Andrej Kiripolsky (Grafana Labs) 00:07:50 But this is still very useful to understand, because, like, I think the first thing that we'll have to do in the survey is that we'll have to make sure that we have good understanding of what people's setup is, so then we can understand why they make… why they have certain preferences.
So we have to have this… Possibility covered as well.
Arthur Silva Sens 00:08:13 If we mention that I'd be very clear, for… for infrastructure, I think this… This word infrastructure makes very… clear that we are talking about the premises exporter and auto-collector receivers?
David Ashpole (dashpole) 00:08:30 Yep.
What are we trying to gain by comparing the two? Just, like, are we trying to get adoption?
Numbers.
Or is it, like… Arthur Silva Sens 00:08:44 it… what I had in mind is, like, I'm… I'm considering… pushing, the Prometes exporter adoption inside the collector.
But only if that makes sense. Like, if the user base already says that they prefer the exporter and they don't want to move to receivers.
Then that's a very good project to work on.
David Ashpole (dashpole) 00:09:12 Yeah, yeah, I think maybe an even better scoped way of trying to ask this is.
Do most people who use Prometheus exporters But basically, are Prometheus exporters and the OpenTelemetry collector used together?
Are they ever used together, or is it, like, people who… people don't really do that, essentially. Like, if you're pushing OTLP everywhere, then you just use the collectors and receivers, and if you're… scraping into a Prometheus server directly, use… use the Prometheus exporters.
I don't know if that makes sense.
Arthur Silva Sens 00:09:55 I think the audience… they are looking for the audience that are specifically about… who are using both, I think. Like, Ben and Trey, yeah.
Andrej Kiripolsky (Grafana Labs) 00:10:03 So… actually, not necessarily who, or… this depends how we… how we… how we design. It's… we are still early on, so we can change things, but… I think we can… ask even people who don't use both, but who have considered both. So this is more interesting, as far as I understand, because even if somebody decides to use purely only Prometheus.
It might be interesting for us to understand why they decide to go with, exporters instead of receivers, or why do they… if they still have any, like, special preference about querying and so on.
David Ashpole (dashpole) 00:10:49 I guess I kind of want to know if that's a real user group. Like, people who use Prometheus, Node Exporter, and the OpenTelemetry Collector.
Part of me thinks that that's actually not really a real group today, just because of how much harder it is. But if it is a real group.
then they would certainly be interested in, like, Prometheus exporters as collector-receivers, because it would… Make their lives a ton easier.
Right.
Andrej Kiripolsky (Grafana Labs) 00:11:20 Yeah, I am trying to make notes, but I'm not sure if I was able to.
David Ashpole (dashpole) 00:11:24 So far, it's good.
Andrej Kiripolsky (Grafana Labs) 00:11:25 So… Okay.
David Ashpole (dashpole) 00:11:33 I would just say, like, if so, Exporters as collector-receivers would be very helpful for them.
Andrej Kiripolsky (Grafana Labs) 00:11:45 Huh.
Okay.
So we have two… two more questions there, and yeah, it already took 10 minutes, so I will take, like, 5 more, if possible, and then I will… I will let you folks go ahead with… with the other.
Arthur Silva Sens 00:12:07 Looking… looking at the agenda, we've… Probably will finish it very quickly, like, don't worry about the time.
Andrej Kiripolsky (Grafana Labs) 00:12:14 Okay.
Okay, good, good.
David Ashpole (dashpole) 00:12:16 Beautiful.
Andrej Kiripolsky (Grafana Labs) 00:12:21 Okay.
So, in that case, Owen, Cryo, any comments about this question, or about the other two?
Or maybe any other questions that came to your mind that we could include?
David Ashpole (dashpole) 00:12:33 What do you mean by a queryless experience? Like, of course, I don't want to do work.
Arthur Silva Sens 00:12:40 Yeah, I can, I can put some… David Ashpole (dashpole) 00:12:43 Yeah, go for it.
Arthur Silva Sens 00:12:44 clarify this. I, I… Andrej Kiripolsky (Grafana Labs) 00:12:47 In a world… Arthur Silva Sens 00:12:49 Where people are only using open telemetry.
they need to decide where… where they are sending open telemetry to.
There are very different approaches on how to do, how the backend, does this, like, for example, Prometheus.
we don't have anything besides the query, like, you send OTLP to Prometheus, you write a query on your own.
And that's how people use it. If they are sending for particular vendors, there are very… some options are very opinionated solutions. For example.
You send… LTLP data from your Kubernetes clusters, there is a very Opium-nated Kubernetes monitoring solution.
There are… there may be other vendors are sending… they… they don't have an opinionated solutions, but the way people navigate through the data is not by queries, it's, like, a very pretty UI that gives you hints on how to… how to do this stuff.
Which is what I had in mind with Querilist, and… Andrej Kiripolsky (Grafana Labs) 00:13:58 So, like, basically, do people… David Ashpole (dashpole) 00:14:01 Want.
pre-built… Grafana dashboards for common open telemetry metrics? Is that the question?
Arthur Silva Sens 00:14:10 This could be one of the interpretations, if they want to very opinionated.
David Ashpole (dashpole) 00:14:17 you install the Cube Prometheus stack?
It comes with a dashboard for all the metrics that come with it, right?
Yes.
Arthur Silva Sens 00:14:24 True.
David Ashpole (dashpole) 00:14:25 Didn't we… isn't there, like, a Cube Hotel stack that's being worked on?
Somewhere?
Arthur Silva Sens 00:14:31 Yes, yes.
David Ashpole (dashpole) 00:14:35 Okay, so… Arthur Silva Sens 00:14:36 There are other… there are other solutions, like Dasho or Grafana entities, that they don't have a pre-built dashboard, but they give… they give a way to navigate through data, which is through resource attributes.
David Ashpole (dashpole) 00:14:57 I see, so that, like… Yeah, I mean, I guess the hard part is… Like, PromQL is a query language.
And it's open source. It's… Like, loosely tied.
to OpenTelemetry, in that it's the best open source query language for OpenTelemetry that exists today.
But it's not, like, OpenTelemetry's query language.
Andrej Kiripolsky (Grafana Labs) 00:15:23 Yes.
Arthur Silva Sens 00:15:27 like, but if people, for example, they don't want to go to Prometheus because Prometheus uses This methodology where you need to write your queries.
that we are losing adoption on from each side, because OpenTelements don't like Ferris at all.
Andrej Kiripolsky (Grafana Labs) 00:15:47 Right, totally.
David Ashpole (dashpole) 00:15:48 I guess it's… I, I agree.
Andrej Kiripolsky (Grafana Labs) 00:15:52 But Prometheus?
David Ashpole (dashpole) 00:15:54 It's, like, kind of weird, right? Prometheus, the project.
Also doesn't come with dashboards, but it's the, like.
it's the Helm charts and stuff built around Prometheus, like the Prometheus stack that usually come with the fancy dots.
Andrej Kiripolsky (Grafana Labs) 00:16:08 Yeah.
David Ashpole (dashpole) 00:16:09 Right?
Andrej Kiripolsky (Grafana Labs) 00:16:09 Sorry.
Arthur Silva Sens 00:16:10 Yes, that's true.
David Ashpole (dashpole) 00:16:12 It's like, I don't know if this is a Prometheus problem as much as it is, like, a… Should we… should we… encourage the OpenTelemetry community when they write… I guess the OpenTelemetry demo does have a bunch of dashboards, but it would be cool, like, if the OpenTelemetry Prometheus stack came with something. Or are you suggesting that Prometheus should work on a queryless experience. Like, I guess that's the other.
Arthur Silva Sens 00:16:39 Yeah, I… Yes, yes, a queryless experience, but it doesn't necessarily mean include pre-built dashboards.
David Ashpole (dashpole) 00:16:48 Yay.
Yeah, I'm new to that topic, but it sounds cool. I think if you could… If you had a way of… Putting that in a… Survey, or, like, showing someone a mock-up and saying, do you like this?
Andrej Kiripolsky (Grafana Labs) 00:17:07 That would be a cool… David Ashpole (dashpole) 00:17:08 cool thing to send out, potentially, right? I think… I… I guess we just need to make sure that.
Andrej Kiripolsky (Grafana Labs) 00:17:16 we know… David Ashpole (dashpole) 00:17:17 Like, if we get some result that says 100% of people responded and they love queryless experience, like, we should know what action we should take.
At the end of it, my only, like… So, if we can clarify.
Arthur Silva Sens 00:17:30 Yeah, that sounds fair.
David Ashpole (dashpole) 00:17:32 Yeah.
Andrej Kiripolsky (Grafana Labs) 00:17:36 And we don't have to, like, figure it out now, but yeah, that would be great. That's my second point, like, what are the decisions you folks want to make based on these things? Because then we can… like, right now, we are in a phase when we are… when I'm collecting, like, all the questions that you folks might have, and all the things we could potentially ask about, and then we'll have to prioritize which we will actually have time for, or, like, the space in the survey.
form.
So, like, understanding which data is tied to what kind of decisions, or, like, what are your expectations about what the data will tell us? It's also, also interesting.
But yeah, okay, so that's roughly, roughly it.
if… other folks don't have any… anything else, I think I can just… we can… we can just move. Oh, yeah, Cryo, please, go ahead.
krajo Krajcsovits 00:18:29 Yeah, I've been thinking that you… Put us on the spot a little bit, but so… There's… two areas that I'm thinking about. One is the unknowns, which is that we are kind of starting from ourselves, so maybe you need a question to say, what's your top one or three things that you want to improve in the interoperability? So we have kind of a prioritization input.
And the other area is the naming conventions.
And, I don't know how to formulate a question there, really, but, like… Yeah, I don't know, I have to think about it.
Andrej Kiripolsky (Grafana Labs) 00:19:13 I've… Yeah, yeah.
krajo Krajcsovits 00:19:14 Any ideas, though?
Andrej Kiripolsky (Grafana Labs) 00:19:16 Sure, sure, and I would like to… I would like to run this survey at Yuko in… in two weeks.
David Ashpole (dashpole) 00:19:22 So, I'll be walking, I'll be, like, running around together with Anna, who's also on the call.
Andrej Kiripolsky (Grafana Labs) 00:19:28 I will be asking people to, to, fill in survey. It will be fun, never done this before.
So yeah, but what I'm trying to say, we still have one more week, so if anything, anything pops up, I will, like, once I have, like, more or less polished version of, like, a questions list, I will, I will, post it to the Slack channel, and I would love to hear your feedback or any, any… other suggestions, what we might… what we might add. But this… this question about what could be… could we improve is… is a good one. That's… that's for sure. Like, it's… it's a simple one, and we can, we can collect a lot of… lot of feedback there, so yeah, thanks.
Arthur Silva Sens 00:20:10 But what Cryo said about, naming conventions, like, do you feel like this is still unsolved? Like, I have… David Ashpole (dashpole) 00:20:21 We've done a lot. I feel like this is… Arthur Silva Sens 00:20:23 Yeah, I don't know how to phrase this as well, but, like, it feels like since we implemented UTF8, people are… They can choose whatever conventions they, they, they, they want.
krajo Krajcsovits 00:20:39 You mean, wait, but naming conventions include semantic conventions in my head, like, are… Prometus exporters are not exporting.
According to… The conventions, right?
Arthur Silva Sens 00:20:52 To the hotel conventions? Okay, that's true.
krajo Krajcsovits 00:20:55 Yeah.
Arthur Silva Sens 00:20:55 it.
krajo Krajcsovits 00:20:56 And I don't… but again, I don't know what I want to ask there. Like, I have many ideas, like… David Ashpole (dashpole) 00:21:01 Hmm.
krajo Krajcsovits 00:21:02 one is, would you mind if the SDK would enforce or, like, lint for you the names that you choose and stuff like that? But I need to come up with, like, a… David Ashpole (dashpole) 00:21:12 Good question.
The thing that really comes to my mind is that Bartek and others have talked about Using schema transformations to convert between the Prometheus existing conventions, like, define those in OTEL's schema format, define the correct mappings from one to the other, so that you could use an exporter, and then get the equivalent of the host metrics receiver, or vice versa.
If that's what you want. I think… yeah, there have been some very cool prototypes there. It would be useful to have a signal that says, I would really like to be able to start with the Prometheus HTTP metrics and end up with the OpenTelemetry ones, or I'd like to be able to take the OpenTelemetry ones and end up with the Prometheus normal HTTP or gRPC metrics. Like, something like that, that.
krajo Krajcsovits 00:22:10 Yeah, but what's the question, you know? That's why I don't.
Arthur Silva Sens 00:22:13 I have, I have one question, that I hope is not leading.
David Ashpole (dashpole) 00:22:18 Maybe, like, do you often find yourself needing to use processing to translate between the Prometheus name of a metric, and the OpenTelemetry name of a metric.
And then give an example of, like, the two HTTP ones.
to unify? Something like that. Or do you often find yourself writing queries over… the Prometheus… version of a metric, and the OpenTelemetry version of a metric.
Arthur Silva Sens 00:22:46 One suggestion is how much of a pain it is on your daily life that Prometheus and OpenTelemetry conventions are different.
David Ashpole (dashpole) 00:22:57 I think that's too… I guess, like, my thought was, if we could get a clear signal that people want the schema transformations, that would be helpful.
I don't… I feel like that might be a little too general.
But maybe… Andrej Kiripolsky (Grafana Labs) 00:23:15 Yeah. We're trying to… Yeah, yeah. We don't have to come up with, like, specific, question formulations right away. I think it's good to just identify areas where… that… that, You are curious about? And we can, we can then… do the… the questions later on. So this is… this is great that you… yeah.
mentioned the semantic conventions as one of them as well. Alrighty, and we are already 20 minutes into, so thank you very much for all the input.
David Ashpole (dashpole) 00:23:48 remains one area, and I'll just leave it.
One area is… Type compatibility. So right now, there's… 3 or 4 types.
or there's, like, some types in OpenTelemetry that don't have a representation in Prometheus, and there's many types in Prometheus that don't have a representation in OpenTelemetry. So, basically, just gauging interest in… how many people wish OpenTelemetry had a… State set type.
Or how many people wish Prometheus had a… an up-down counter? Probably zero, but… It's an interesting question to ask, because I think maybe after the first round of stabilization, we could revisit some of those other types, and there has been interest from some OpenTelemetry, like, TC members.
In having better… More official, like, state-set type stuff.
Because we do have a lot of states set.
Kind of, metrics.
Okay, that's all.
Andrej Kiripolsky (Grafana Labs) 00:24:49 We can move on.
Cool, thank you.
Arthur Silva Sens 00:24:53 I'll just make one correction in your notes.
Andre.
Okay.
Then I'm moving on to the next topic, I'm not sure how many of you follow the OpenTelemetry website repository.
There were some conversations during Old Town Unblocked.
That people are having a hard time moving from Prometus SDK to Autel SDK, and from Autel SDK to Prometus SDK, Because they have… like, they're a complex piece of software. It's not easy… like, it might be easier for us, but, like, we work with this on basically every day.
But people who are not really into observability.
they have a hard time picking which SDK to use, and if they… Use one, they have an even harder time migrating to another in case they want to.
So, check, open a PR to the website with a guide.
Explaining common patterns in one SDK, and how to do the same pattern in the other SDK.
And he intends to merge this.
but, like… Migration guides are very… tricky, because it, like, touches emotions of people who work on one SDK or the other.
like, if Jack just published some… some… a guide, and people interpret that this is a guide for you to move out of Prometheus SDK, because hotel is the new, cool thing, and people should not be using Prometheus.
that touches… That will bring memories… from the time where Prometus and Ottawa had a very bad relationship, and we don't want to get into that state again.
So, my ask is, go to the PR, Like, if you are emotionally attached to one community or the other, go to the… go to the PR, Read the post and, like.
See if you feel attacked, somehow. If this… If the wording is not correct, if something feels… awkward, and you're feeling like people, like, check is suggesting people to not use Prometus SDK, we should be speaking up.
Because this is also not his intention, like, he don't want to suggest that. But, like… It's hard to write this kind of content without… Suggesting a migration, you know?
Yeah, Owen?
Owen Williams (he/she) 00:28:20 Is there… has that conversation been started?
Like, have you… have we said… asked him in… if we… if it should be in a migra… called a migration, just as opposed to a comparison?
Arthur Silva Sens 00:28:36 Yeah, like, we called it out, and jack said, but there's no good place. The migration was the best place he could find.
Owen Williams (he/she) 00:28:45 Where… Arthur Silva Sens 00:28:46 God.
Owen Williams (he/she) 00:28:47 is… David Ashpole (dashpole) 00:28:48 I do also think… the thing people are actually trying to do is migrate. I think we're just trying to be neutral about the direction. Like, there are people, it sounds like, who Actually want to go one way or the other.
For various reasons, right?
Yeah. So, like… We also shouldn't hide it, or… Yeah.
But, yeah, anyways.
Owen Williams (he/she) 00:29:15 Yeah, I think it's a matter of framing, not… not… not hiding.
I mean, it could go in getting started, like, hey, you're familiar with Prometheus, this is how you'd do it in Yeah, where's that conversation happening? Because I don't see it in the PR itself.
Is it happening in Slack, or am I just… is it, like, a collapsed thread I'm just missing?
Arthur Silva Sens 00:29:47 I've… there is a lot going… Jack works in my team, right? So, there is some conversations happening, synchronously between Jack and I.
But this is a good call-out, this conversation should be public.
Owen Williams (he/she) 00:30:04 put it this way, I was looking for a comment that I could plus one, to just sort of… because I don't… I don't… I don't necessarily think it helps. It's already a pretty busy PR, and I don't think it maybe helps to have 5 new people sort of all suddenly comment. But I think… I think it's a good question, and like… yeah, I'm more inclined to kind of plus one… The argument that, like, hey, let's try to be a little more… a little more even… well, yeah, be… we have to be careful about these things, so I… I agree with your… with your position on that.
and I… yeah, just looking at the, looking at the… the tree… of docs, it seems like there's plenty of places something like this could go, so I don't quite… I don't feel like it has to go to migration.
Arthur Silva Sens 00:30:59 one suggestion that Jack made after I called this out was creating a new a new section called Compatibility.
Owen Williams (he/she) 00:31:09 Sure.
Arthur Silva Sens 00:31:10 we could put, like, tons of other things that are not only Prometheus, like StatsD compatibility, p-proof compatibility.
Owen Williams (he/she) 00:31:19 Yep.
Arthur Silva Sens 00:31:19 like, does that sound better?
Then migration.
Although it is a migration guide.
Owen Williams (he/she) 00:31:28 Sure.
Well, I mean, I, I mean, it's a comparison.
It's… Prometheus be like this, OpenTelemetry be like that. Like, it's, Unless it's specifically written for, like, hey, you've got everything in Prometheus, how are you gonna rewrite it? Like, I thought it was… I thought it was more meant to be, like, an introduction to OpenTelemetry for people who are familiar with Prometheus, which is kind of a different framing.
Arthur Silva Sens 00:31:59 I like this framing of comparison. Like, we don't need to tell people, hey, this is the migration guide. Like, this is how SKs compare to each other. And of course, people who won't migrate, they will look at this comparison.
Yeah. Even if we don't call it migration?
Owen Williams (he/she) 00:32:16 Yeah.
Yeah, I mean, I think compatibility is good. I mean, getting started, like, hey, I'm getting started as somebody who's familiar with Prometheus. I don't know, as long as a search engine can find these things, it seems like the… Exact location is not… And I assume we'll have a little blog post, maybe, to… to… advertise it.
Yeah, I think there's a… the main thing I'm trying to figure out is, is there actual resistance to moving it out of migration, or is it more just a matter of, hey, we just need some ideas for how to do it? Because it sounds like it's not really… yeah.
Arthur Silva Sens 00:32:53 The resistance is… it's extra work, and then… Sure. Yeah, but that's all.
Owen Williams (he/she) 00:33:05 Okay, yeah, if… if… maybe… if you can just start the discussion in the PR, sort of introducing it, then I'm happy to chime in and even, like… because a lot of this just seemed to be code examples, like the actual… Yeah, it's pretty, And even the way it's presented is pretty neutral anyway. Both systems support classic histograms, like, it's not… if you've got a histogram written for Prometheus, this is how you will change it, so that you are not using Prometheus anymore. Like, that language isn't even in there. So I actually… I… yeah, I'm happy to do a pass on it if that's something that is welcome for just, like, slightly reframing things.
That is great, that's all we need. I think Jack is happy to not put in migration, we just need to find the… Arthur Silva Sens 00:34:00 Not the perfect, but, like, not that bad of a place.
krajo Krajcsovits 00:34:05 We already have an example of this on the specification level.
Where it talks about compatibility.
Arthur Silva Sens 00:34:14 Yeah, but it's a bit different, like, a specific pack is a guidance for developers on how to implement certain things.
And this is not really where end users should be looking when they're trying.
krajo Krajcsovits 00:34:30 I wasn't suggesting to put it into… Arthur Silva Sens 00:34:32 Okay.
krajo Krajcsovits 00:34:33 No, no, no, no, no, I'm just saying that it doesn't have to be migration. I agree with Oban, and I agree also with… you don't need plus 5 people, so I will not do that.
Also, putting on my… business hat.
for… I think it doesn't really matter.
for… for our business, if people went over to Ulta, because… We have the… You know.
we should have good products, and then we will attract the data anyway. Doesn't matter if it's remote right or not, like… It's fine.
Arthur Silva Sens 00:35:08 Cool.
Alright, great.
Next topic is also mine.
It's just a heads up.
David and I… were requested by the TC to present what we have been doing.
I think David volunteered first, so I'm… I'm there mostly to support David if needed.
But, yeah, they are… they're asking what we've been… TC is technical committee.
Is the… It's a group of… folks in OpenTelemetry who… Not the site, but, like, they… they… They give support to the… all the six to ensure that we are building something coherent, and not just a bunch of people doing random stuff.
But yeah, they are… they're interested in understanding what we are currently working on, what we have been doing lately, what help we need to accomplish the projects we want to accomplish.
So if you have anything in mind where… that we should add or ask them.
This is a good moment.
David Ashpole (dashpole) 00:36:28 No, it… I haven't, like, written down anything for what I'm gonna say yet, but I think… I think I have pretty good context.
I think the most… the most interesting things may actually be the stuff in the… that's happening in the Prometheus community. So some of the… like, the new info function.
And… What else is happening on the Prometheus side?
Arthur Silva Sens 00:36:57 Arvid has been working on Methodistore, Owen has been doing the Deltas part.
David Ashpole (dashpole) 00:37:04 Oh, yeah, yeah. It's a loud thing.
Arthur Silva Sens 00:37:05 note.
David Ashpole (dashpole) 00:37:06 Yup.
krajo Krajcsovits 00:37:07 Well, open metrics, too.
David Ashpole (dashpole) 00:37:09 Yeah, yeah, well.
Arthur Silva Sens 00:37:09 Well, electricity.
David Ashpole (dashpole) 00:37:10 I've heard about… I've heard.
Arthur Silva Sens 00:37:14 I would love to see this metadata storage evolve into a good entity support.
But being very realistic, since entities itself is not well developed in Hotel yet, this is going to take a while.
David Ashpole (dashpole) 00:37:30 Yep.
Arthur Silva Sens 00:37:34 Like, we could be talking about the problems we've been having with target info as well?
that this translation for service instance ID is not really working in the infrastructure components.
David Ashpole (dashpole) 00:37:48 Yeah, that's a good thing to bring up.
I don't know if anyone's taking notes.
Arthur Silva Sens 00:37:53 I can… krajo Krajcsovits 00:38:26 ask them, when can I approve PRs?
Arthur Silva Sens 00:38:31 When can you approve PRs?
krajo Krajcsovits 00:38:33 No, sorry, where can I… Oh yeah, I think I can approve, but can't merge. Why can I merge PRs? That's make my life easier. I'm just joking.
No, I think for a technical committee point of view, you probably want to ask them about where do they see this in a couple of years, priority, that sort of thing, because I don't… I'm not sure if they are aware of the details anyway, like, just more, you know… Ask them about… David Ashpole (dashpole) 00:39:02 I think our vision.
Their biggest thing is they just want… the… so the… I'm sure everyone here is probably familiar with the, OpenTelemetry graduation process.
krajo Krajcsovits 00:39:14 And the technical committee sees.
David Ashpole (dashpole) 00:39:16 stable… Prometheus-compatible artifacts, like exporters, receivers, and such, as a big Line item for stuff we want to stabilize.
To… not necessarily just to reach graduated, because I think that may happen without it, but, like, But… That they… the project should have stable… Components that interoperate between the two.
communities, right? So I think that that's, like, probably their biggest interest, is they're kind of just, like.
Less concerned about the details of how we solve things, and more… Let's get to stable. Let's mark things stable.
Let's pick… pick whatever's gonna be best for users right now, and… stabilize it and do V2s if we have to.
krajo Krajcsovits 00:40:09 So that's, I think… David Ashpole (dashpole) 00:40:11 Yeah, I'm on the technical committee, by the way, so I… I do talk with them about stuff related to Prometheus and interoperability sometimes on the… False.
Arthur Silva Sens 00:40:27 Oh, I have one last topic, if we're going to KubeCon.
And you are joining the Maintainer Summit on Monday?
There is a form that we've been sharing around.
We… we're doing a… Prometheus Plus Hotel project meeting.
And we only have 30 minutes, and if we have to do a lot of logistics to start the meeting, we'll just talk for 5 minutes.
So, this form is for you to tell I am going to the Maintainer Summit.
And if you have any ideas to… that, like, things you wanted to discuss.
You can add, to this form.
This is being organized mostly by Pablo from HotelGC and myself.
So, it will make my life a lot easier if you answer this form and you are going.
Thank you very much.
We still have 20 minutes.
You could go through the board.
Of the projects we're working on?
We could end the meeting, we could… I don't know.
Talk about life, what do we want to do?
David Ashpole (dashpole) 00:41:50 I… for this group, I'd like to call out that I think there's, the stabilized exponential histograms.
spec PR from Cryo on the spec repo, love if… People who are in this group could take a pass at that.
I approved it earlier today, so I'm happy with it. But, I'm trying to think if there's anything else on the spec side. I don't think so, I think that was… did we ever merge the histogram? We did merge the histogram and the summary one?
Arthur Silva Sens 00:42:22 Yes.
David Ashpole (dashpole) 00:42:23 Great, great. So we should… If we do look at the board, maybe pick the next couple that we want to work on and see if we can get some volunteers.
Arthur Silva Sens 00:42:32 Okay, let me, let me show my screen.
David Ashpole (dashpole) 00:42:37 Is there anything you wanted to say about it, Cryo?
krajo Krajcsovits 00:42:39 Not directly about that.
But, I'm doing, like, nitty store migrations in Grafana.
David Ashpole (dashpole) 00:42:49 Bobby… krajo Krajcsovits 00:42:51 supported by AI, which is… Fun and painful at the same time.
But I was thinking that I haven't done one where there was the OpenTromatic collector in the middle.
where… We are going from, you know.
classic histograms to native histograms. So that might have some impact on… on the, I don't know, maybe the spec, or maybe the implantation.
So that's kind of pending.
But… This… like, this month is… is too busy.
For me, next month, I hope to spend more time on OpenTometer, for sure.
David Ashpole (dashpole) 00:43:28 Are you saying you'd prefer if this part of the spec was not marked stable yet for another few months?
krajo Krajcsovits 00:43:35 No, I think this is perfectly fine.
David Ashpole (dashpole) 00:43:40 It can be stable.
krajo Krajcsovits 00:43:42 And, like, a migration is, is a… It's like a next… It's on top of this, basically.
David Ashpole (dashpole) 00:43:50 Yep, okay.
krajo Krajcsovits 00:43:52 So I think it's fine.
Arthur Silva Sens 00:44:01 This thing that you want to work on on top of this one, should we be adding as an issue to the bar?
krajo Krajcsovits 00:44:10 I have to research it a little bit to even know if there's… what are the things to do? Like… Not yet.
Arthur Silva Sens 00:44:17 Got it.
krajo Krajcsovits 00:44:17 I mean, it will be added by somebody if they run into… they try it and run into issues anyway, but… Yeah, let me research it a little bit before.
Running my buff, basically.
Arthur Silva Sens 00:44:32 Okay.
Okay, so for the remaining items.
all of them are in discussion needed, so I am assuming those are not really easy things to tackle.
A drop type seems easy.
Start time… maybe the next easiest one?
David Ashpole (dashpole) 00:44:55 Yeah, God.
I'll just put up PRs for those.
I don't think I've done anything for him.
you can.
Arthur Silva Sens 00:45:02 Yeah, but like… Is discussion needed because we need to discuss, or we just forgot to put it in workable?
David Ashpole (dashpole) 00:45:09 I think the PR just needs to, like, if you click on it.
I think we just forgot to put it in Workable, so let's maybe look at it, discuss, and then put it in Workable.
krajo Krajcsovits 00:45:22 Also I see the… On top of the list, this super translation of native serum custom buckets to OTRP, that's pretty much being done in the PR.
For destabilizing the exponential, because it belongs there.
So, I would consider this in progress.
Arthur Silva Sens 00:45:49 registration number.
David Ashpole (dashpole) 00:45:51 You can just make it fix it as well.
Arthur Silva Sens 00:45:56 I cannot edit.
Yeah.
But you could put… you can put this here, right next to this one.
krajo Krajcsovits 00:46:05 Okay, I'll do that.
Arthur Silva Sens 00:46:11 I put this… Oops.
Should probably delete this section and add a note about start time to each of the timestamps.
That sounds… Easy.
David Ashpole (dashpole) 00:46:36 Yeah, you can move it to workable, as long as everyone is okay with that, those changes.
Arthur Silva Sens 00:46:45 ain't… It should just say, I'm okay?
David Ashpole (dashpole) 00:46:54 Cool.
Arthur Silva Sens 00:46:55 Yeah, okay, I'm okay.
Metadata.
Like, this is a little bit complicated, until we have OpenMetrics 2.0.
because OpenTelemetry allows… Same metric name, as long as they have different metadata?
David Ashpole (dashpole) 00:47:27 Is this… I don't think that changes anything, because the OpenMetrix20 will just not have any suffixes to be removed, so this will be a no-op, right?
Oh, I guess maybe total?
Arthur Silva Sens 00:47:42 Yeah, but the suffixes are… they… they are not must anymore, but they are should.
David Ashpole (dashpole) 00:47:48 Yeah. So they are still there.
Yeah. Yeah, that's tricky.
we… I'm okay stabilizing the other parts of this, and making this statement here.
Development, or something like that?
What do people think? Because I think the general idea that, like, type unit and help get mapped to type unit and description is non-controversial.
And… If we don't have this translation, whatever.
I don't care, very much.
Or if we keep it behind a feature flag in the receiver.
Arthur Silva Sens 00:48:44 what… What catches my attention here is that this is called configurations.
And I don't see how a data model relates to configuration.
David Ashpole (dashpole) 00:48:55 You're right. We could have a separate document about But we have a… we just have an SDK exporter document, but we don't have a… like, an SDK receiver, like, there's nowhere for receiver-related stuff to live.
This could also just be completely not specified at all, and just be, like.
Yeah, the Prometheus receiver does it.
Arthur Silva Sens 00:49:24 But, like.
krajo Krajcsovits 00:49:31 I don't see… like, what is the problem here? I mean… hotel… hotel allows you to have the underscore total. It's not going to, you know, reject stuff if there's that name, right?
David Ashpole (dashpole) 00:49:45 I think it's the inverse of… the main thing was, it was the inverse of the… .
krajo Krajcsovits 00:49:53 Export.
David Ashpole (dashpole) 00:49:54 So there's, like, an option in the translation strategies for exporters that says, with underscore, it's like, with underscores and suffixes, right? So it'll add total and seconds. This probably isn't necessary, now that you can just have Prometheus send it without that.
So because there's a no translation option, you should just use that on your exporter side instead of using this on the receiver side?
Does that make sense?
krajo Krajcsovits 00:50:24 Yeah.
Arthur Silva Sens 00:50:25 And then in the receiver, we can just not tell to remove.
anything. If it comes with the suffixes, we'll transform with suffixes.
But if it comes without, that's the ideal world.
krajo Krajcsovits 00:50:39 Yeah, and Open Analytics 2 will allow that. And then, if you want to actually… remove it. I think that's the area of that schema compatibility thingy where you can tell what conventions to do. So I think this is kind of getting solved slowly.
David Ashpole (dashpole) 00:50:55 Right. I think this exists because the Prometheus receiver implements it.
Which is because almost all the exporters add type and unit suffixes today. So, I'll need to see metrics that are coming from, like, OpenTelemetry HTTP instrumentation.
Have these, and then people who want to get back to the original OTLP, we're using this stripping config. So, I think we could just remove this from the spec.
And the Prometheus receiver, over time, can deprecate it and encourage users to use the no translation mode on the clients instead. But I think it'll… that'll take some time.
krajo Krajcsovits 00:51:34 Yeah, this is definitely one topic that I want to talk about in the Prometus.
Deaf Summit that we… that we'll have.
After KubeCon?
Yeah. Where we are going to talk about the SDKs, And, it's just… Yeah, I think we should try to go towards this future.
David Ashpole (dashpole) 00:52:04 Delete stuff and mark it stable.
I'm gonna have to drop.
Because I need to do some prep for my next thing. Feel free to continue, and if anyone wants to take any of the remaining ones, maybe accept resource attributes.
Which is a little scary.
then, feel free. But, thanks, guys.
Arthur Silva Sens 00:52:29 Kia.
So I'm moving this to Workable as well.
So this is related to target info, which has been a thing for… I don't know how much… how much time, this is too hard. I would suggest that we solve this last.
Instrumentation scope.
We… David just said that we probably just need to implement this in the Prometus receiver, and I do have a PR opened.
that I need to fix texts, apparently.
No.
Yeah, but I, like, I do have a PR open that… Let me go back a little bit.
Does everybody know what we are talking about when we say Translation of instrumentation scope.
krajo Krajcsovits 00:54:22 Is that, when you put those scope underscore things in the target info?
Arthur Silva Sens 00:54:27 No. Okay.
Okay, but it was closed, though. I'll tell us cope.
is… added as, like, a telescope has a name, a version, a schema URL, and a set of attributes.
differently from Target Info, where Target Info is only one.
Metric, and then you have to do the joins to correlate to target info.
One set of metric.
Scope info is not added as a separate metric, it is added as labels to all the metrics.
krajo Krajcsovits 00:55:09 Oh, okay.
Arthur Silva Sens 00:55:14 So, the… on the receiving side, when we receive a metric, we need to take a look at all the labels.
And if the… all the attributes, the name, the version, and schema URL match.
All those metrics are put together in the same scope.
We are not doing this today in the Prometus receiver, and I have a PR open to do that.
Once this PR is merged, we can just declare this as stable.
There's nothing to change in the world.
April is… This last one is also… is related to Java. This is a hard problem. Oh, sorry, GoPrime.
krajo Krajcsovits 00:56:19 Yeah, you just said you have a PR for that instrumentation scope. Don't you want to move it into… in progress or something?
Arthur Silva Sens 00:56:26 But does this… for the collector.
Yeah.
I'm putting progress… But, like, This PR will not close this, this issue.
But still, you are working on it.
Yeah, yeah, fair. I'm putting progress.
Okay. For this one, we made a change to this… to this pack, or to the behavior, I don't understand correctly what change we made.
But since we created the translation strategy, Owen.
Java has been… has having a hard time.
Adopting these translation modes?
And one of the problems is that When they had special characters, Like, multiple special characters together.
It was translated into multiple underscore.
and it's now translating into a single underscore, or it's the other way around? I honestly don't understand. It could be that it was a single underscore, and they are now becoming multiple underscore.
Owen Williams (he/she) 00:57:38 Damn.
I mean, we solved this in one of the Go areas by adding a special flag there's a flag for the translator to do that or not, so they can expose that in Java and use it as they please.
Arthur Silva Sens 00:57:56 Okay, so do you think Java… Java can adopt whatever we say here.
Owen Williams (he/she) 00:58:06 I mean, I… well, so that's… that just refers to the Go translation library that we wrote.
The point being, we have… a precedent for if a particular SDK was doing something the way that is currently considered non-standard, you can have options and flags to do it the way they want to do it.
Arthur Silva Sens 00:58:36 So, if it's possible, I guess we just need to clarify.
And this pack, if it's… I wanna see… Owen Williams (he/she) 00:58:47 I'm not sure how this relates to UTF-8 support, because the whole point of UTF-8 support is you're not doing escaping.
Arthur Silva Sens 00:58:58 What do you mean?
Owen Williams (he/she) 00:58:59 Well, what does this have to do with UTF-8? In UTF-8, you're not converting characters.
So… Arthur Silva Sens 00:59:09 could be without… UTF8.
He just… Like, when we do, UTF-8 scaping with suffixes.
Multiple consecutive characters should be replaced with a single underscore.
Owen Williams (he/she) 00:59:31 Right.
So this is talking about… .
Arthur Silva Sens 00:59:37 Without what if.
Owen Williams (he/she) 00:59:38 So you're talking about… Arthur Silva Sens 00:59:39 just wrote… Owen Williams (he/she) 00:59:40 The escaping… he's saying the escaping is being done at… the, on the exposition side, So I believe there… I'm a little confused about the word client and server sometimes.
Arthur Silva Sens 01:00:05 Yeah.
Owen Williams (he/she) 01:00:07 The problem converter in the Java SDK doesn't change double percent to underscore anymore, because underscore escaping is done at scrape time. I don't know what that means. Like, is he talking about Go code, or is he talking about Java? The point is, you can implement things so that it works and does not break. That is okay.
None of this has anything to do with… UTF-8, because escaping doesn't occur when you're doing UTF-8. That's a different question. So I'm a little confused about the problem statement.
Should clients add a flag?
Arthur Silva Sens 01:00:41 Oh, sorry, you were reading?
Owen Williams (he/she) 01:00:43 Yeah. Wait, go back to the bottom.
Users usually want to control transition on the ingested side rather scrape times, so it's good to keep a UTFA support setting in the hotel SDKs.
Yeah, I don't understand what the… problem is. I could say… while the standard is to collapse escaped characters, it is fine to have configuration settings to maintain compatibility and not break people. That can even be the default.
I don't care how escaping happens. That's really, yeah, unrelated to UTF-8.
Yeah.
Sure.
Arthur Silva Sens 01:01:33 Can I comment?
Owen Williams (he/she) 01:01:35 Yep.
Arthur Silva Sens 01:01:38 Okay, we are at time.
Owen Williams (he/she) 01:01:40 Correct.
Arthur Silva Sens 01:01:41 Well, thank you all for the discussions.
See you at KubeCon, I think.
krajo Krajcsovits 01:01:48 Sure, not me, but… But, yeah.
Arthur Silva Sens 01:01:51 Alright, see ya.
krajo Krajcsovits 01:01:52 Bye-bye.
