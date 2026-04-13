SIG: Prometheus WG
Date: 2026-04-10
Duration: 64 minutes
============================================================

## Zoom Recording Transcript

Arthur Silva Sens 00:01:41 Hello.
Kyle Eckhart 00:01:42 Hello?
Jonathan Santos 00:01:57 Hey, hello, guys.
Arthur Silva Sens 00:01:59 Hello.
What?
Sarah, to you, April 10th?
Did you… were you able to listen to this very noise motorcycle that just passed through my window? Okay, cool.
Jonathan Santos 00:02:58 Nope.
Arthur Silva Sens 00:03:21 Let's wait a few minutes… I'm gonna ping David, because he has this first topic.
He's not answering, so I'll just… Just start.
Show screen… Okay, the first topic's from David.
Let's move this below, actually.
Maybe we hate joints later.
First topic is from Cryo, who is also not here, but he says… He has a private appointment.
The… Said he's… he has sinned, the PR from Jonathan.
And he wants to reveal by next Wednesday.
The PR already has two approvals, though.
How…
Jonathan Santos 00:06:28 How are you feeling, Jen?
The only thing that's missing is the… I don't remember the reference that we are… that we need or don't.
to pass through the functions to… I don't know why you need that reference variable.
Arthur Silva Sens 00:06:44 Because before…
Jonathan Santos 00:06:45 For that, that change?
This reference is, was not used across the codebase.
Arthur Silva Sens 00:06:55 Yeah, I think Kyle also saw this problem before. What we are talking about here is that when… Jonathan switched from a Pander V1 to a Pander V2.
he realized that series ref is not used by the Prometus receiver.
And we were wondering why this ref is even needed.
In the append method.
So for Prometheus, if we are not mistaken.
The reference is used to track the staleness marker, But in the receiver.
It… yeah, it doesn't need, for some reason.
Kyle Eckhart 00:07:38 So, on the input, it's a hint for downstream.
So, like, for the receiver implementation.
What ends up happening is, regardless of the input, it recalculates the series ref to return.
And the one that matters is the series ref that gets returned.
The one that's input is a hint, and you can choose to use the hint, or you can choose to ignore the hint, essentially. But as long as you're returning stable refs from append, staleness tracking works as you would expect it to.
Arthur Silva Sens 00:08:13 Okay, that makes sense. Yeah, and we cannot use what we received, because we do all sorts of transformations Like, we process scope labels, we process resource attributes, and that changes the identity.
Kyle Eckhart 00:08:31 Yeah. Like, in Upstream, it's used for a very fast path in the write-ahead log lookup, essentially, right? Like, it's like, oh, cool, scrape has a cache, I know it's series ref1, I don't have to do a label set lookup, I can just trust the label set, like, trust that it's series ref1.
Arthur Silva Sens 00:08:50 Got it.
Okay, I… Jonathan, to progress here, I think it's faster to just… Accept, David's comment?
And you… once you rebase your PR, all those vulnerability checks will be green?
And we don't need to wait for Cryo, because Cryo will look only on Wednesday next week.
Jonathan Santos 00:09:16 Okay, I can do it, like, right now.
After this meeting?
Arthur Silva Sens 00:09:21 No rush, once you, once you're free.
Yeah, another point is more like a FYI.
Kyle and I are still working on making Prometus exporters embeddable in the collector.
And I have news for you, Kai. Every week, I have more news for you.
This is being… Like, Brian… Brought this problem, to the hotel community again.
Brian Barham.
is, another… problem that he's seeing is that the Prometheus SDK for metrics is a lot more performant than the Othello SDK.
and the Prometheus exporters I implemented in… with Prometheus SDK, While the collector receivers are implemented with the hotel SDKs.
And then… We are not only replicating work, duplicating work with the collector receivers, we are also making them worse, and more slow, and more memory consu… consumers?
I don't know, like, as time passes, this feels… More and more important.
And I don't want to say that as, like, putting pressure on you, like, let's do this. It's just, like, extra motivation. This is important.
Kyle Eckhart 00:10:54 Yeah.
It's always good to continually hear it.
Arthur Silva Sens 00:10:59 Okay, yeah, I can continue bringing that up.
Kyle Eckhart 00:11:03 Mostly because, you know.
I don't know how long it was that we talked about doing it before we actually were like, we should do it, and now it's just continually being reaffirmed, like, yep, we should keep doing it.
Arthur Silva Sens 00:11:17 Jonathan, are you aware? Like, do you understand what this… what we're talking about?
Jonathan Santos 00:11:25 remember that Brian bring that topic, not only Brian, but other Prometheus maintainers.
About the performance issues that… That's the Hotel Labrise.
have compared with the Prometheus one.
Especially in the metrics, I think that that's about it.
Arthur Silva Sens 00:11:45 Yeah.
Jonathan Santos 00:11:45 - I… You said that inside of the hotel library, we are not using the Prometheus SDK. We are using other Implementation.
Arthur Silva Sens 00:11:59 We're using the hotel SDK.
If we look, for example, Postgres exporter from the permiti side, and Postgres receiver on the collector side.
They're basically doing the same thing.
But they are using different libraries.
Yeah, so… And, like, we have… two codebases that do the same thing. We have two sets of maintainers who don't collaborate, And we are… And the collector using a slightly less performant library.
Jonathan Santos 00:12:39 And the suggestion is just replace… by the Primeters SDK?
Arthur Silva Sens 00:12:45 I didn't know, not replace the SDKs.
but make the exportable embeddable in the collector using OCB?
You know, you know OCB?
And and promote this strategy more, like… somehow convince the Postgres receiver maintainers to collaborate with the Postgres exporter maintainers, make sure that the exporter can send semantic conventions on the long term.
Like… Instead of us working separately, we find ways to work together and solve both.
solve the requirements from the Prometus side, and solve the requirements from the hotel side at the same time.
But anyway, it's a very cool project, very impactful.
If more people want to help, we'll definitely… we definitely need the hands.
Moving on, andrei Kriposky from the hotel end-user Sikh?
it's a SIG that focuses on UX research.
he did a survey in person during KubeCon. He started asking a bunch of questions to… To the people who are there?
And as he was… Asking questions, for example.
he would ask, hey, do you use Prometheus? And people would say, no, I use Mimir, or I use Victorometrics, or I use Thanos.
And I had to explain to Andre, hey, this is actually the same thing.
So it counts.
Others were like, hey, do you use Prometheus and OpenTelemetry?
Yes, but they use Prometheus for metrics, OpenTelemetry for traces, and they would never, like… it's not about Prometheus Hotel interpretability, because, like, they… the way they use, it never touches each other. Yeah, we had to make a few adjustments on the survey.
And I think he wants to publish as a banner in the hotel website?
And it also has a banner in the Prometheus website.
And we want to get, like, 500 responses, or something like this?
And then, we'll have some answers. You can look at the survey in the link.
Another FYI, Pablo and I wrote a doc about conversations that I have with KubeCon, if you want to take a read.
And then we are… And, spec pars.
how are you feeling?
Do you wanna take a look at the PRs, or do you wanna just skip? And…
Jonathan Santos 00:16:05 what they would want with these PRs. They are in the reviewing mode?
Arthur Silva Sens 00:16:14 They are all up for a reveal.
Jonathan Santos 00:16:17 Huh.
Arthur Silva Sens 00:16:18 And there are a few approvals already.
But, the hotel technical committee usually merge things faster if there are a lot of approvals.
But I don't know, like, usually from the group that we have here.
You don't do much spec stuff?
So, it's okay if you want to skip this, that's totally okay, I don't want to steal your time with something that we are not interested in.
Jonathan Santos 00:17:04 Don't know, I never read the specification or review, or specification before, but we can take a look.
together, don't know. Maybe it would be cool to know what David is changing.
Arthur Silva Sens 00:17:20 Alright.
Let's take a look.
At this one, for example.
Oh, just got merged.
Literally 10 minutes ago, okay.
Let's take a look at the next one, then.
So, what he wants to do, So, Do you know what this pack is, Jonathan?
Alright, it's a document where we tell SDKs how to implement something.
And this PR wants to stabilize how exemplars from the Prometheus format, No.
the other way around. How exemplars from the OpenTelemetry format are translated into Prometheus format.
So he says, exemplars from open telemetry garages should be dropped.
Because Prometheus doesn't have exemplars on gausses, for example.
If some is converted to a Prometheus counter, then exemplars must be converted, Otherwise, exemplar should be dropped.
Is there a way where OpenTelemetry sum do not become a Prometus counter?
Jonathan Santos 00:19:06 I don't know.
Arthur Silva Sens 00:19:13 This is a question.
Kyle Eckhart 00:19:34 There he is.
David Ashpole 00:19:35 Hey, sorry folks.
Kyle Eckhart 00:19:36 Pirate.
Arthur Silva Sens 00:19:36 Oh, hello.
We were starting to review the… your PRs.
David Ashpole 00:19:45 Agreed.
Arthur Silva Sens 00:19:49 So, you can answer this question already. We're looking at… OpenTelemetry exemplars, 2 Prometus exemplars.
There is, a phrase here. If sum is converted to a Prometheus counter.
I don't understand this if… if there is… is there any way where a sum does not become accounted?
David Ashpole 00:20:08 Yes, up-down, or non-monotonic sums become gauges.
Arthur Silva Sens 00:20:17 Non-monotonic summits.
David Ashpole 00:20:19 I.e. up-down counters.
become engaged.
Arthur Silva Sens 00:20:23 Nope.
Okay.
David Ashpole 00:20:27 Basically, like, if you end up with a Prometheus gauge, don't throw a bunch of exemplars on it.
Arthur Silva Sens 00:20:32 Yeah, yes.
Okay, makes sense.
Alright, do you want to take over? This is your topic.
David Ashpole 00:20:39 Yeah, sure.
Did we already talk about everything else on the agenda?
Arthur Silva Sens 00:20:49 Yes, we did.
But if there's anything you want more information about, I can totally… Say again.
David Ashpole 00:20:59 Very cool.
What's the first Prometheus exporter you ported?
Arthur Silva Sens 00:21:06 A SecDriver exporter.
David Ashpole 00:21:10 That's funny.
Arthur Silva Sens 00:21:11 It is… this is just because Kyle was the maintainer, so it's easy to get reviews.
David Ashpole 00:21:18 Good.
Kyle Eckhart 00:21:24 It's funny, it's still named Stackdriver Exporter, too.
David Ashpole 00:21:27 Yep.
Okay, and I will definitely read the KubeCon trip report.
Is there anything in particular that's worth calling out at this meeting?
Arthur Silva Sens 00:21:44 I think the SDK stuff is… quite an emotional topic. Yeah. But you were… you were there yesterday as well.
David Ashpole 00:21:55 Yeah, it caught me by surprise.
Arthur Silva Sens 00:22:00 Yeah, me too, to be honest.
David Ashpole 00:22:16 Okay, okay, let's… let's move on. So we looked at… I think I merged the metadata one, so we're good there.
And then, exemplars, there was one open question I had to bring to the group.
Let me share my screen.
This looks like the right one.
So the one question I had for this group is… So for histograms… For histograms, we take When it's bucket-aligned, right, we need to pick one exemplar from a list of potentially, you know, a couple, right, that fall into a given bucket.
And so, what the spec currently says is that we take the latest exemplar by timestamp.
Right, so if you have 3 exemplars that fall into a histogram bucket, and we need to pick one.
We end up picking the one that's latest timestamp-wise.
no particular.
Arthur Silva Sens 00:23:22 other pieces.
David Ashpole 00:23:23 They're clearly…
Arthur Silva Sens 00:23:24 We're talking OTLP to Prometus, right?
David Ashpole 00:23:26 Yes, so OTLP exemplar, so you could have a a histogram that uses, a… just, like, a random set of exemplars, right? Not… Necessarily bucket-aligned, and you may want to… and you would want to convert those into bucket-aligned exemplars.
So this… this isn't the case most of the time, because… OpenTelemetry also does bucket-aligned exemplars by default, but you can change that. So you can, for example, if you want to save money or something, instead of… if you have 20 buckets, you could just have a random set of 3 exemplars, right? It's probably the main use case for people.
This… but what we say is basically, You picked the latest one.
When multiple exemplars fall into the same bucket.
And so the question is, the current spec, for example, is… that I moved, right? So this is, came from here… Did I even move it?
No. I didn't even move it. So, the question is, how do we pick Was it largest?
No.
So this is a net new spec. I think we should match the histogram one and use the latest exemplar.
For a counter. So if you have 10 exemplars on a counter.
And you need to pick one of them to put on the open… or the Prometheus counter, then you would just pick the last one.
And that mostly is to align with how Prometheus clients store exemplars.
Where… You just tracked the latest one.
Arthur Silva Sens 00:25:20 Oh, okay.
Yeah, I was curious why you decided for latest.
David Ashpole 00:25:30 So, like, Prometheus clients, when they collect exemplars, always keep the last one, right? So if you do, like.
metric.addWithExemplar, I think, is the function.
But you just always get whatever… the latest one that was added.
Arthur Silva Sens 00:25:46 Can we somehow add a comment to this pack that is… That is… doesn't get rendered.
But that we… over time, we… We understand why we made this decision.
David Ashpole 00:26:08 What… what to you is… Is it just, like, why is it necessary to have this?
Arthur Silva Sens 00:26:14 Yeah, like, why did we decide to pick the latest? I'm pretty sure that people who don't…
David Ashpole 00:26:21 I see.
Arthur Silva Sens 00:26:21 don't know the… doesn't have the context that this is what the Prometus SDK do, they will ask… Like, why?
David Ashpole 00:26:36 I can just add it. It can be part of the spec. Not every statement has to be normative.
Arthur Silva Sens 00:26:41 Okay.
David Ashpole 00:26:42 You guys can still see my screen, right?
Jonathan Santos 00:26:46 women.
I have one question around it.
Why… why this rule is important? To pick the first or the last one?
Why not pick all as employers?
David Ashpole 00:27:05 So this… so this is only if the Prometheus protocol only supports a single exemplar on the countersample. So if, for example, you're using OpenMetrix 1, I think the Prometheus Protobuff format also only supports a single exemplar. I can double check.
Jonathan Santos 00:27:28 The XFLAR carries some metadata about the data point, right?
David Ashpole 00:27:34 Yeah, it's like an example… it's an example of a… an event that is part of the counter aggregation, or that's part of the aggregation. Yeah, so in the protobuf format.
You have a single exemplar on a counter as well.
So this is gonna be a thing that people will have to do, probably for some.
Jonathan Santos 00:27:56 Got it. Thank you.
David Ashpole 00:28:24 testing as well I made both of those changes.
Is that helpful?
Arthur Silva Sens 00:28:52 Yep, yep.
David Ashpole 00:28:52 Okay.
And then, looks like I'll see if I can get Josh and, one other… maybe Arv to… Sign off on it.
Arthur Silva Sens 00:29:17 Oh, wow.
David Ashpole 00:29:20 What, you see all the ones we've merged?
Arthur Silva Sens 00:29:23 No, I didn't know you could solve conflicts this way, I always… Check out the branch locally and do all kinds of good stuff.
David Ashpole 00:29:32 Yeah.
I only really use it for changelogs, but it is really nice for changelogs.
Jonathan Santos 00:29:40 I never do that locally, because, especially in the contrib repository.
there's a lot of different files, and my… my VS Code just… just breaks.
Arthur Silva Sens 00:29:50 F. Yeah.
Yeah, contributes the pay.
David Ashpole 00:29:55 I think this one is still… I think this one's still good to go. I'd like one other person from the Prometheus SIG to take a look.
Arthur Silva Sens 00:30:06 Like, by the… By the way, now that you say permit to Seek, like, can we… Adjust that group?
Like, remove old people, add new people.
David Ashpole 00:30:18 We, we, the latest discussion in the GCTC room was to just delete the group.
Arthur Silva Sens 00:30:25 Oh, really? Okay.
David Ashpole 00:30:27 I was like, I kind of just use it as a mailing list, but it's not a very good one, and we don't have any real power anywhere, so…
Arthur Silva Sens 00:30:34 We do have…
David Ashpole 00:30:36 We have our own repository that we don't use.
Arthur Silva Sens 00:30:39 No, but, like, in this pack, when you… I don't know. Don't we count as a… A spec approver for our part, or something like this?
David Ashpole 00:30:53 Not officially, at least. Like, your check mark is not green here.
Okay, and then… Let's see, I think we are… So for instrumentation scope, Arthur, you have a PR out? Oh.
Arthur Silva Sens 00:31:14 Yeah, thank you very much.
David Ashpole 00:31:16 You're welcome. I'll use my… My browser-based editing powers. I think we're… I'm happy with this change, but it does need eyes from other people, so if anyone's interested.
Please take a look.
And yeah, we'll need other TC people and stuff.
Arthur Silva Sens 00:31:41 Yep.
David Ashpole 00:31:42 And then the very last… so if all those get merged, the very last one for the Prometheus receiver is resource.
I wanted to take some time and walk through this.
Just to answer any questions that people have. Is that okay?
Arthur Silva Sens 00:32:00 Yeah.
we… I mean, RV and Cryo, we will also need to understand this.
But…
David Ashpole 00:32:11 Arv… Arv seemed to think it sounded okay.
But it is a… it is a pretty big… So, let's see, so the motivation for this is… We've had a lot of discussions about Like, how job and instance aren't exactly the same as service.
Attributes.
And in some cases.
I think the semantic conventions has kind of waffled on whether you should always expect service attributes, like, should… Collector-receiver always produce service attributes.
Or whether, whether it's, like, a separate thing that's really only for applications.
And so I wanted… I think it's important that we make Job and instance a little bit more explicit.
And its own thing.
One, because there are cases where… that we have, where users want to set Java and instance.
But want it to be distinct from… Their service name.
So this, for example, would happen if you… have an OpenTelemetry instrumented application.
You use the Prometheus exporter in that application's language.
and then you scrape it with the Prometheus receiver, right? So you'll end up with a service name and a service instance ID that comes from the OTEL SDK that's present on target info.
And you'll also have a job and instance.
Based on your Prometheus receiver config.
And so, in that eventual world, like.
It would be nice to be able to keep both.
And to preserve the distinction in the receiver, and also in the exporter again, right? So that the exporter is able to properly send the job and instance based on your Prometheus receiver config.
and the service name, service instance ID, and such.
Based on how you configured your OTEL SDK.
Arthur Silva Sens 00:34:19 And how does this relate to the owner labels?
config option.
David Ashpole 00:34:27 I… doesn't… Doesn't relate too closely to it.
So… Honor labels has always only applied to Java and Instance, right?
And it only is a thing in the Prometheus receiver itself.
So… We've never had… SDK exporters.
Setting, job, and instance.
Arthur Silva Sens 00:34:56 Okay, okay, yeah, yeah.
David Ashpole 00:34:58 on their metrics.
And so… Unless… I think the one place where it might impact things is if you're using the collector's Prometheus exporter.
the things that end up being put in Java and Instance.
Might be different after this change.
Compared with what was happening before, because now we can… Before, we couldn't really preserve your job and instance separately from your service name and service instance ID, so you have… we would have to pick one.
I think we override with job and instance, right?
Arthur Silva Sens 00:35:41 Yep.
David Ashpole 00:35:41 I don't actually remember the behavior.
But I think we override, so it's possible that you… would get… a different job and instance on the Prometheus exporter than you do today.
But I see that mostly as a good thing.
And it's very easy for users to correct.
With, like, a simple transform processor.
Arthur Silva Sens 00:36:04 Okay, let me ask something else.
So, what you're trying to accomplish here is not related to, for example, a Pulse receiver who is… receiving metrics from two different Postgres?
And that they send, their resource attributes separately.
It's something that Arv has been discussing with the Postgres receiver maintainers lately. This doesn't seem 100% related.
David Ashpole 00:36:38 It's orthogonal to that.
So, if you got something from a Postgres receiver, it would obviously not contain Prometheus.job or prometheus.instance.
So… and all the Prometheus exporters.
would look at… for a Prometheus.job and Prometheus.instance, As, like, the first… the first fallback, and then would fall back still to service.name and service.instanceID, which is what ARB is negotiating with various receivers over, is setting that. So, that is still, like… The same problem it's always been.
I think what's interesting now, potentially, is that Regardless of what the server does.
or regardless of what the Postgres receiver does, a user could with a processor, decide exactly how they want job and instance to be set by setting Prometheus.job and Prometheus.instance based on whatever other attributes are already present.
So, I think in some ways, this gives them more control. Now, they could have just set service.name and service.instanceID.
Somehow, in the same way, but this, I think, is, like, slightly more explicit.
You… The idea would be that you… you would get your job and instance the way you want them, but you wouldn't get a potentially misleading service name and service instance ID if the Postgres receiver folks thought that that made no sense, right?
I don't know if that… It's, like, helpful, because the issues that a lot of the receivers have with setting service name and service instance ID? Is that… they don't think of themselves as a service, right? They're not an open SDK. So, I think maybe… I think this might help, but it doesn't, like, address the core question there.
Arthur Silva Sens 00:38:36 Okay, and then, do we need to address this question before we stabilize this pack?
Because if we do, I am afraid we'll only stabilize this back once Entities is out.
David Ashpole 00:38:57 Oh, you mean, should we block on… so… so that's the… that's the thing, is… This is the receiver portion.
And… My feeling has been that it's… it's gonna be much harder to stabilize the exporter side of this. So, right, this is the… Prometheus to OpenTelemetry.
I actually feel like that is a bit easier to stabilize.
Because… If we came up with a new representation for OpenTelemetry resources, Right? Whatever that is.
in Prometheus land.
The receiver could have support for… The old way, and the new way.
quite easily.
Right, so we could stabilize it, and then… when we come up with our new way, add it as development, and stabilize it later, as a new supported way of setting yourotel resource via Prometheus, right?
And that, I think.
Arthur Silva Sens 00:40:08 Cool.
Only if the script manager also makes this optional.
David Ashpole 00:40:16 Makes one.
Arthur Silva Sens 00:40:16 We depend, if… if we find a new way of… like, we depend on the script manager code.
Okay, no, but transforming to LTLP is on us, then, yeah, yeah, forget about it.
David Ashpole 00:40:32 But on the exporter side of things, when we're talking about, like, SDK exporters, we need to pick One representation for resource.
And we can't just, like… send 6 different ones because we've evolved over time, right? So I think that's why I'm… I'm actually more okay with… Stabilizing target info, more or less as is.
On the receiver side, with the intention that we can easily support other representations of resource.
That I am.
Stabilizing target info on the exporter side.
Arthur Silva Sens 00:41:15 Yeah, that makes sense. That makes sense to me.
David Ashpole 00:41:18 But I do feel like this particular change would be beneficial.
To make before we stabilize it.
Arthur Silva Sens 00:41:31 Okay, I'm happy to approve. Of course, I'll read this more deeply later, but…
David Ashpole 00:41:38 I will…
Arthur Silva Sens 00:41:38 the book.
David Ashpole 00:41:39 I'll mark it ready for review, then.
I wanted to chat about it first, before I just threw it up.
This doesn't stabilize it, by the way, this just adds…
Arthur Silva Sens 00:41:54 Yeah.
David Ashpole 00:41:55 Stabilization would come later.
Arthur Silva Sens 00:41:57 So, to add this to the spec, I think we will need PRs, right?
David Ashpole 00:42:02 In the collector?
Arthur Silva Sens 00:42:04 Yeah.
David Ashpole 00:42:05 Yep. Well, right, so it's development right now, so I'll add it to the spec, and then I'll implement it. I have a PR… In the collector here.
That adds it to all the exporters and receivers.
Got it. It's fairly trivial, right? Because it's like… Look.
look for job, look for this special job, otherwise fall back to the existing behavior, look for the special instance, otherwise fall back to the existing behavior. And that's just… oh, the one interesting piece is maybe the config, where One complaint users might have is that now we're duplicating the job and instance, into service name and service instance ID.
So I'm adding an option to turn that off.
We can discuss whether that… makes sense, but I feel like it's probably necessary, and otherwise we would just get user feedback that's like… Why did you make everything… 10 cents more expensive.
Arthur Silva Sens 00:43:10 Oh.
David Ashpole 00:43:11 I will cut this up into multiple PRs, though, before I send it out.
After this.
Arthur Silva Sens 00:43:17 But…
David Ashpole 00:43:17 One word.
Arthur Silva Sens 00:43:18 The PR is very small, less than 20… Less than 200 lines?
David Ashpole 00:43:24 Was it really?
Arthur Silva Sens 00:43:26 Yep.
I think you can just do one.
David Ashpole 00:43:30 Did I not put tests in here or something? No, there's a test.
I don't know if there's actually good tests, but… This was meant to be a prototype, but I can also clean it up and just put it out. I guess the same approvers are going to approve all the components.
And then I wanted to do a quick check-in.
For Prometheus to OTLP, this is required for the Prometheus receiver stabilization.
We're almost there. So, we have start time and instrumentation scope, which I think are good to go and just need reviews.
And then, I think there's a path to having the target info handling in the Prometheus receiver stabilized, and then we're good to go. Yeah, wow.
Arthur Silva Sens 00:44:15 That was intentional. This is the first time I did this with the intention.
David Ashpole 00:44:21 Oh, yeah?
Okay.
Arthur Silva Sens 00:44:23 We also need, that brand on RFC, and then we can stabilize the receiver.
David Ashpole 00:44:30 That's right, that's right. We still… at least for the spec side of things, we're… we're close.
And then for the exporter side of things, we're still quite a ways away. I had a couple PRs open.
That looks like we got through.
I think maybe the next step will be to go through, like, all the types, gauges, sums, histograms, exponential histograms, and summaries.
and open PRs for those, I don't think that'll be anything crazy.
scope.
Arthur Silva Sens 00:45:03 Yeah.
David Ashpole 00:45:03 is probably actually gonna be good to go. I don't have any issues with our current handling of scope in the receiver.
And then, I think resource attributes is going to be a longer discussion. But I'm more comfortable putting that behind feature flags and disabling them by default in SDK exporters.
Arthur Silva Sens 00:45:21 Yeah, this is a… this is a big problem, because I was talking with the Collector folks, they want to stabilize Prometheus. Sorry, they want to stabilize Collector, and this includes the metrics that Collector exposed.
And this means that they will not release Collector V1 until… the Prometheus exporter spec is stable.
Yep. But, like, exposing… but then exposing target info, we are not stabilizing until entities are out.
David Ashpole 00:45:56 Are entities not stable?
They're… they're out, right? They exist.
Or is that…
Arthur Silva Sens 00:46:03 No, I think they are still making changes to this data model.
They're adding, like, and… yeah?
David Ashpole 00:46:16 So we can't… Yeah, I don't…
Arthur Silva Sens 00:46:26 this… somebody will need to give in, because we are in a circle, I feel.
David Ashpole 00:46:32 Yeah.
I think… I think the best thing we could possibly… but… hmm… It's in the protocol?
Status development.
That's… Yeah, I don't know how we build on that.
Because I… what I would like to be able to say is, Any attribute that is present Any attribute that is associated with an entity should be dropped.
And put that in, and then… And it basically just gives us the freedom to do what we want with it later.
But… I'm trying to come up with a way to mark it stable without Dealing with entities, but…
Arthur Silva Sens 00:47:35 Yeah, let's try to get everything out, and then only resource attributes are left, and then we have more mental capacity, I guess, to discuss this.
David Ashpole 00:47:44 Yeah.
Yep, I think that's good. I think there's a path to getting… Quite close in the next… Like, before our next meeting, so…
Arthur Silva Sens 00:47:53 Okay, I'll try to get PRs open for most of the… Of those types of transformations?
David Ashpole 00:48:03 Yes, sure.
Arthur Silva Sens 00:48:04 I'll let you know.
David Ashpole 00:48:05 That'd be great.
Okay, we have one more topic on the agenda.
Naman?
Naman Parlecha 00:48:21 Yup. So, this issue was open and was recommended, by Jonathan to be picked up, so… but there is already an existing PR, which is stale and requires… Changes, so… would it be good to pick it up and make the changes, or… Since there is already a PR…
Arthur Silva Sens 00:48:45 Yeah, the PR is not abandoned, actually. The PR is blocked, because we need to make some adjustments to an underlying library.
David Ashpole 00:48:54 Yep.
Arthur Silva Sens 00:48:55 And and this… making this adjustment to this library is more complicated than we expected.
I… this will require, like, a regular, like.
a formal proposal to the collector maintainers, and that's why this PR is not… moving. It's not like the… the outdoor abandoned, it is… we can't… we can't… we can't advance until we get the… the proposal open.
David Ashpole 00:49:23 Did I open the issue? Where is this?
Nope.
This one.
Okay, let me make this more explicit, so we don't have confusion in the future.
Arthur Silva Sens 00:49:44 You can add a… a blocked relationship, I think.
David Ashpole 00:49:49 Okay.
Arthur Silva Sens 00:49:53 As a below? Below, below, below?
There's relationships… A little bit below.
Yep.
I think there's a mark blocked by…
David Ashpole 00:50:11 Crazy.
GitHub has really stepped up its…
Arthur Silva Sens 00:50:20 Yep.
David Ashpole 00:50:21 It's game.
Arthur Silva Sens 00:50:25 Yeah, so, sorry for the confusion in a month. I think this is not something we can work right now.
Naman Parlecha 00:50:34 So, is there any other ticket on any project that could be picked up, possibly?
Arthur Silva Sens 00:50:45 check.
David Ashpole 00:50:46 I don't know about stabilization work, I feel like there's… actually, I have a good one for you. Here, I'll make it right now.
Because I was about to go do this, or tell an agent to go do this, but you can do it instead.
It's fine.
Which is the one that has this one.
Okay, so if you look at this table here, Maybe this isn't the most exciting one.
Arthur Silva Sens 00:51:49 Yeah, I feel like Naman will fix this 30 seconds.
David Ashpole 00:52:12 What's that?
What's your GitHub, Naman?
Naman Parlecha 00:52:37 Let me just drop it there in the docs.
David Ashpole 00:52:55 Okay.
Arthur Silva Sens 00:53:00 David, what do you think about the… the… Memory limiting the script loop.
David Ashpole 00:53:12 I'm super excited. I mean, I'm happy to present that.
Arthur Silva Sens 00:53:17 Yeah, like, this is something that is not as easy, but I don't know…
David Ashpole 00:53:22 It's not that hard. It's, like, 100 lines of code. I mean, it's in the scrape loop, so it's not like… But I'm happy to… for anyone who's not familiar, I'm super excited by this. I've wanted this for a long time, and… yeah, I, like, I looked into it, and it was way simpler than I thought it would be, but… Yeah, the idea is… Pick the memory limiter config.
and make… Prometheus recognized something similar.
And then, when you get close to your limit, instead of, like, with OTLP, you would… drop.
the metrics that you had just gotten over OTLP, but with Prometheus, it would be even better if we could just not do the scrape in the first place, right? So… When… when you're memory-constrained, it'll just… skip the scrape, and mark it as failed. So you'll get a up equals zero metric.
And if you go to your targets page, you'll see that the target is down, with the reason being memory limiting.
And then… yeah, I ran some, like, little experiments as well, and you can implement fairness algorithms To make sure that different Targets don't get starved, even if one is… It has massive scrape size.
It doesn't… Yeah, I think it's…
Arthur Silva Sens 00:54:54 the…
David Ashpole 00:54:55 Yeah, worth… Worth doing.
Arthur Silva Sens 00:54:58 I feel like this is challenging enough for Naman, because Naman has been contributing to Prometheus before, though, like, this… Tara… terabytes, I know TLB translator is too easy for him, but it's limiting is a good challenge.
David Ashpole 00:55:15 Yeah, I mean, if… I think… My plan was to wait till the next Dev Summit, which I don't know when it is, and bring it up, but if somebody… if someone wants to pick this up and work on it, I'm… I have, right, I have a proof of concept.
the… works.
And it's…
Jonathan Santos 00:55:37 Can you drop the link here?
David Ashpole 00:55:40 Yeah, yeah, I can… so this is this, and the proof of concept is linked from the description.
Arthur Silva Sens 00:55:47 And, to clarify, Naman, like, whatever you do in the script manager package in Prometheus, this also benefits the collector, because we reuse the Prometheus library.
David Ashpole 00:55:59 Yeah, it's… it's actually a really big issue, In practice… here, I'm gonna stop sharing, unless there's other… There we go.
It's a big issue in practice, because you'll use the OpenTelemetry memory limiter, with your Prometheus receiver.
And the Prometheus receiver will do all this work to scrape some massive endpoint.
Right, like, it scrapes cube state metrics with a billion series.
parses it all, translates it all to OTLP, does all this work, makes all these data structures.
spikes your memory, and then the memory limiter's like, oh wow, we're close to our memory limit, we should probably get rid of all this.
All these metrics we just got.
And so it has this, like, inverse effect of… Dropping all your metrics after the memory pressure.
isn't really relevant anymore. So it… it just, yeah, it doesn't make sense, and it was a… I… at one point, I built, like, some managed service that used the Prometheus receiver and the memory limiter, and it was just… They just worked so poorly together.
So…
Arthur Silva Sens 00:57:15 Alright.
I think we are… Out of topics, and 3 minutes ahead.
Woohoo.
David Ashpole 00:57:24 If anyone didn't see it, Open Metrics 2 had a release candidate as well.
Switches.
fun, and probably relevant to this group. Like, a lot of changes are good for Prometheus and hotel compatibility.
Arthur Silva Sens 00:57:39 I wonder how… how we can incentivize more people to… to help?
And, like, implement OpenMetrix 2.0 in the SDKs.
David Ashpole 00:57:51 Yeah, I've got the first PR up for Go.
Arthur Silva Sens 00:57:54 Oh, really?
David Ashpole 00:57:55 Yeah, let me… I can drop a link.
Jonathan Santos 00:57:58 But there is a project that group all the… Other things? Related to OpenMetrix 2.0.
David Ashpole 00:58:09 There is a repository where we track all the issues.
spec itself is on the Prometheus website.
Right, you probably didn't see it.
Jonathan Santos 00:58:36 What is the name of the repository?
For me to suspect.
David Ashpole 00:58:40 There is a Prometheus slash OpenMetrics repository.
Where we… Track issues.
If you… if you go to Prometheus.io.
You can find the open metrics spec Listed among the specifications.
And… Yep, and I linked my PR if anyone's curious.
Arthur Silva Sens 00:59:16 Animal?
Naman Parlecha 00:59:19 So, one question I had from the open metrics thing is, why would you… like, I was seeing these PRs, right, from everybody in the channel, but then, I was confused that… Why would we implement something before and later write the specs, rather not… rather writing the specs before and then implementing it, right?
David Ashpole 00:59:41 Like, why did we write the spec before implementing it?
Naman Parlecha 00:59:44 No. I guess the Open Metric 2.0 is already implemented, right?
David Ashpole 00:59:49 No. So I have… I have a PR open, which is the first code that's been written Oh, God. I don't know what?
It relates to open metrics, too.
Naman Parlecha 00:59:57 Oh, okay.
David Ashpole 00:59:59 So we wrote the spec completely out, and now it's release candidate, and now people are going to implement it, and find lots of problems with it, and then we'll go iterate, right?
Naman Parlecha 01:00:11 Got it. Okay.
David Ashpole 01:00:17 And, unless there are other questions, we're at time. So, sorry for being late.
Arthur Silva Sens 01:00:23 Yeah, no worries.
See ya, bye-bye.
David Ashpole 01:00:27 Hey, everyone.
Jonathan Santos 01:00:29 Alright, thank you, guys.
