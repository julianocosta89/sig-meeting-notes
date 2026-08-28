SIG: Java SIG
Date: 2026-08-27
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker (Microsoft Corporation)** 01:28 Hello.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 01:28 She's trying…
**Trask Stalnaker (Microsoft Corporation)** 01:29 preferred.
Yeah, finally got the mic working.
**John Watson** 01:43 Jay, it looks like you are in the comfy chair.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 01:48 Yeah, I'm in my, 3 hours of meetings, chair.
**John Watson** 01:52 The comfy chair!
**Jason Plumb** 01:54 A comfy chair.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 01:57 I feel like I might be missing a reference here.
**John Watson** 02:02 Yes, you probably are. It's, there's a Monty Python sketch.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 02:08 We blew it after.
**Jason Plumb** 02:46 Trask, thanks for getting that, client… SimConf repo created. That's awesome.
**Trask Stalnaker (Microsoft Corporation)** 02:53 Yeah, yeah, I saw there, you all have SEMCOM in Android, Android-specific SEMCOM in your repo, and the browser folks are doing the browser stuff in their repo. Yeah.
**Jason Plumb** 03:06 Yeah, I think it'd be cool to have that common area instead.
**Trask Stalnaker (Microsoft Corporation)** 03:11 Or an addition?
**Jason Plumb** 03:12 Or in addition, yeah.
Yeah, it could go both ways, right? Like, well… Topic for another time.
I will say that experience of setting up the Federated SunConf was actually great. I thought it was going to be such a pain in the ass, and it turned out to be just smooth. It was nice.
**Trask Stalnaker (Microsoft Corporation)** 03:41 You should post that in the, the Weaver channel.
**Jason Plumb** 03:44 I know, I should.
**Trask Stalnaker (Microsoft Corporation)** 03:45 to hear that.
**Jason Plumb** 03:46 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 04:08 Alright, let's kick off… with… milestone-y stuff, I've added a couple of things… That are optional here, the RPC… Semantic conventions are… pretty… they're… RC, we're… still not quite stable, because we're negotiating with gRPC team on what stable looks like, at least for gRPC on… So it might not be stable for a 3-0, but I think… We should… Bump, take the breaking change to whatever the latest is in 3.0, kind of the way we're doing for messaging.
Otherwise… And then, you know, we'll be pretty close, and otherwise we have to wait till 4-0.
Gen AI, I'm a little less… certain of what the current… the RPC, we've actually done most of that, or all of that, I'm not sure, I'll have to look.
behind the flag.
Gen AI, I have less… I'll have to look and see if that's reasonable or not to try to do.
I'll wait… I want to wait to go talk about this one for Jack, because I think he has some thoughts on it.
Or is he out?
Maybe.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 06:03 I think he's traveling right now.
And then we have, Grafana Fest next week, too, so I'm not sure if he'll be here.
than either.
**Trask Stalnaker (Microsoft Corporation)** 06:11 Okay.
Cool, I will… Seeing him on, Slack, but, I was… oh, this came out of… first, I was thinking about, Laurie, something you had said, about being, you know, why not make some more things stable, since we kind of… our… following stability, anyways.
And these properties all looked like good… Properties to… Declarice table in 3.0.
So, if anybody has… Thoughts on… concerns about any of them?
Let me know here on the issue.
A lot of the properties are… there's a lot of logging properties, so I was kind of looking at what That would take to mark some of the logging ones as stable.
And one of the things that came out is, Let's see… Yeah, we've got a bunch of different… attribute names for capturing structured logs, so for MDC, template, we've got a few, I didn't list them here. We've got a few common logging properties, configuration options across all the logging instrumentations.
That are nice, and so those would make a lot of sense to declare stable.
These ones, we have a bunch of variety of, kind of, structured attribute Naming… reflecting the… how different logging libraries name their structured attributes.
But I was thinking about, just… Making it common, Structured attributes include, exclude.
And mapping those to whatever the… All, like, everything that is structured attributes for each given logging library.
And turning that on by default, which is maybe a bigger… Deal.
But it does feel like… Like, if you're using structured logging.
Why wouldn't you want that to go into your OpenTelemetry logs, if you're capturing them as OpenTelemetry logs?
Alright, well, I'll bug Jack, because I know he's thought about the… He has… I think he has opinions about logs.
Yeah, the one other thing I just wanted to, well, since I'm… Thank you, well, this is… what I've, currently cluttered up.
the instrumentation repo with draft PRs. Sorry, Lauri.
But this is, and I saw you were asking about this in one of the PRs a couple days ago, the draft PRs that I was… experimenting with. So, server.address… is… It's confusing currently in semantic conventions, what to do if you have multiple, like, if you're doing multiple seed servers, client-side load balancing, service discovery, registries, that kind of thing.
And… we had… we went through this in the RPC semantic convention work recently, because it's… common over there, for both gRPC and Dubbo.
And what we did for RPC, and so I'm looking at… I'm proposing extending it to database semantic conventions also.
Is… server address already is defined as the logical address, of the server.
As opposed to the physical address, which is network peer address.
Which would be the actual… Server you connected to on a given request.
And so, for… what we said for RPC was that server address Couldn't be, like, a common delimited list.
It can be, like, a zookeeper, a registry service, service discovery registry URL… Something more… Something that represents the logical Connection.
Which… is gonna be a little bit weird for people. Certainly, who think, you know, see server.address and think, oh, that's… should be a server.
but in cases where there's multiple It seems better than not capturing anything there.
And it makes still, like, app… application maps, that people build, Work, where you group things by these logical connections, server service names kind of thing, and You still have the network peer address.
To fall back to for the individual, Server… servers…
**Gregor Zeitlinger** 13:05 Yeah, and also, keeps cardinality lower,
**Trask Stalnaker (Microsoft Corporation)** 13:11 Or server address, yeah.
**Gregor Zeitlinger** 13:14 But how would that work in case of client load balancing?
Is that some HTTP header that you can extract the information from?
**Trask Stalnaker (Microsoft Corporation)** 13:27 So client-side load balancing, so this would be captured on the client side.
So…
**Gregor Zeitlinger** 13:35 Only on the client side. Yeah, it would be so nice if you could have that on the server as well. This is, Problem for years.
**Trask Stalnaker (Microsoft Corporation)** 13:46 That matches… yeah, so that… that's a downside, certainly, is that the server address on the server is not gonna match the server address on the client.
Which, in the nice, simple case of one server.
And where you're sending, that typically is the same, because we get server.name from the host HTTP header.
**Lauri Tulmin** 14:17 I think one more… place where this might be used is the Kafka Bootstrap servers.
We currently had, somebody added, like, a special attribute for that, and I think they tried to get it added to the SIMCO also.
**Trask Stalnaker (Microsoft Corporation)** 14:41 Yeah, yeah, good point.
So this was sort of… I mean, it happens across a lot of database instrumentations.
And that's why, our repo is… Currently, flooded with… PRs, exploring this option.
I did bring it up in the semantic convention SIG meeting on Monday, and general… Consensus to move forward with this.
So, I'm gonna take back… my findings specifically around all these… the Java PRs, Java implementations next… this coming Monday.
And so I'll probably end up setting up PR over there.
It's unclear… I'm not clear whether it will be a breaking change in semantic conventions.
So, we may… it may have to be… a non-stable thing in… it may have to be experimental, like opt-in something in the semantic conventions, but… I think we could still… we… since we're doing a major version bump, we can take that in.
If that's the direction we decide to go.
which I think we should, but I just… I want to get through, kind of, all these PRs, and some of them are… they're… they're stacked.
where… now that we're not cap… in some places, we were capturing the network peer address, the… the local… the… Direct connection in the server address.
So by… changing that, and I think the network peer address becomes more important in this case, where we are capturing the server address as the logical group.
So, that's also what a bunch of these PRs do, is… Add the network peer attributes.
As well. So it's kind of all of… all of the above.
I'll open an issue to kind of link them all to in this repo.
So, to give a kind of overview of… the mess of PRs.
And… Yeah, hopefully I'll have them.
out of draft, I don't know, in a day or two.
Bruno, yes, yes, meeting recordings are somewhere different now.
So, as you probably noticed, this… this link here, the Linux Foundation has their own, sort of.
Zoom wrapper or something or other.
And… Let me see if I can… To get the… links… I forget how to do this.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 18:10 I think if you go to the calendar invite for, like, the previous week, I think they're… Linked to them now.
**Trask Stalnaker (Microsoft Corporation)** 18:20 And so here…
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 18:23 Or maybe not.
I thought Moralia showed me that.
**Trask Stalnaker (Microsoft Corporation)** 18:28 I think it's if you go… you have to go to the… this calendar.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 18:34 Oh, right.
**Trask Stalnaker (Microsoft Corporation)** 18:35 Google Calendar.
And… So… We go here… August 20th… find the Java SIG here, recordings here.
And I think it's on somebody's… I think Pablo is going to update the community repo on how to do that, because, yeah, that's a… Frequently asked question.
**BRUNO Baptista** 19:13 Thanks, Trask.
**Trask Stalnaker (Microsoft Corporation)** 19:14 Yeah.
So I think that's the 3-0 update from my side, at least.
Thank you, Laurie, for, as always, for, all the reviews.
**Gregor Zeitlinger** 19:41 Is the plan that the next release is 3.0, or the one after?
**Trask Stalnaker (Microsoft Corporation)** 19:46 The next one is supposed to be the final, because we want one 2X release that has… All the stuff in it, and so… especially the messaging, that was… that was the main thing that, I want… And we're almost… Done with the messaging.
There's a couple that I just put into, ready for review today, and a couple more.
That are still in draft.
And… Of course, I thought database… databases were done a while ago, but I keep finding more things to… Fix in them.
So we'll see. I may not do as… I probably won't… I won't do as heavy of an audit of the messaging. I've been doing the kind of a heavy, you know, AI, obviously, driven audit of the database instrumentations, which is why I keep finding more More stuff there.
I probably won't do that for the messaging.
Or at least not as aggressively, because it's not stable. Those semantic conventions aren't stable anyways, so… Not as critical.
**Gregor Zeitlinger** 21:11 I can't find any issues for the 3.0 milestone in the repository. Am I looking at the wrong thing?
**Trask Stalnaker (Microsoft Corporation)** 21:22 Probably. I thought I just had it… Up here, milestones… this list?
**Gregor Zeitlinger** 21:35 I cannot see it, maybe it's a hiccup in GitHub, okay.
**Trask Stalnaker (Microsoft Corporation)** 21:48 Oh, somebody's having a good day today.
That's, like, the one system that generally, like, nobody, nobody wants to go down. Well, I guess all the systems, but… Internally, those are always the… 5 alarm fire bells.
If you haven't seen… I'm just gonna keep talking since there's… nobody has agenda items here. And, the conformance repo, we have merged, all of… a bunch of Java… HTTP conformance tests over here.
That's actually where four of, the PRs related to HTTP, semantic conventions came in.
Today.
You can see… so these check-in, There it is.
So we've got, the data JSON. So this… Shows, like, what was captured, when the test is run.
But… The better view is coming soon.
In… So Jay's building a UI on top of that data.
And so we can look at… let's look at… Java… Can I filter by Java?
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 23:48 No, I should add that.
**Trask Stalnaker (Microsoft Corporation)** 23:50 Okay.
But.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 23:51 It's in that one section there, yeah.
**Trask Stalnaker (Microsoft Corporation)** 23:57 Yeah, so we can see all these different HTTP… Java instrumentations, and… Which… Attributes they emit.
And so, yeah, we were missing network peer port in… I think 2 of them, one or two of them, and… Oh yeah, these… I think we were missing these in a couple.
And you can filter… Oh yeah, so that's server instrumentation. Okay, here's client instrumentations.
And right now, we're just focusing… we're just doing HTTP and GenAI, although I think I'm gonna add some database stuff soon, because also the .NET folks are supporting the stable database semantic conventions.
Cool, well… Anything anybody else?
Wanted to raise today.
Alright, quiet day. Let's get some time back.
**John Watson** 25:21 Thanks for running in the intro.
**Jason Plumb** 25:23 Fair.
**Trask Stalnaker (Microsoft Corporation)** 25:24 Bye,
**Jason Plumb** 25:25 Bye-bye.
**Pranav Sharma (Google LLC)** 25:26 Bye.
