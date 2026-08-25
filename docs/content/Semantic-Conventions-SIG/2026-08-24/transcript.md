SIG: Semantic Conventions SIG
Date: 2026-08-24
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Christophe Kamphaus 00:00:23 Hello?
Jay DeLuca (Raintank, Inc. – Grafana Labs) 00:00:28 Hello.
Liudmila Molkova 00:02:36 Hello, hi everybody.
Christophe Kamphaus 00:02:40 Hello.
Liudmila Molkova 00:02:41 I'll see.
Trask Stalnaker (Microsoft Corporation) 00:02:43 Oh, that's the wrong camera.
Victor Lu 00:02:45 Good morning, before you start, I just want to share a, A document, link.
a progress from COSI.
It's a proposal for, security.
For both, hotel and, OCSF?
So this is coming down the road. So this is… usually they publish, do a lot of thorough work before publishing it, but this is kind of a, I guess, publish first and get the opinion.
So, so I'm not sure when it's appropriate to discuss in the hotel community.
Liudmila Molkova 00:03:24 Would you be interested in giving us some context during this call? Maybe we'll put it on the agenda.
Victor Lu 00:03:31 Sure, I'm a generalist, I know what's going on, but I don't need to actually create that document. There are people in that community who are planning to come here to give detailed technical, going through it in detail.
But yeah, I can give some of the background information on what it's about.
Liudmila Molkova 00:03:52 Yeah, thanks. Boo, should we do it today?
Victor Lu 00:03:57 I can do it if there's enough time.
Liudmila Molkova 00:04:04 Okay.
Not sure whose turn is it to run, but I'm going to assume it's mine.
And so I've been…
Christophe Kamphaus 00:04:22 I can do it next time.
Liudmila Molkova 00:04:24 Okay, sounds great.
Okay, I'm getting ready.
Okay.
So… Let's put it on the agenda.
Should we… before we start, let's take a quick look at our… Project board.
Sorry, not the project board. We have better things now.
Okay, maybe I want to talk a little bit about this one.
I'll just put it to the agenda… And there are a bunch of things that are waiting on the reviewers.
This one looks like… Oh, we are waiting for system approvers to take a look.
Not sure why, though.
Trask Stalnaker (Microsoft Corporation) 00:06:41 Yeah, I see, David and… Tyler… Approved it.
Liudmila Molkova 00:06:51 Yeah, sounds like it's ready to merge.
Okay.
Any concerns, if I merge?
Great, so this one is still waiting for somebody to actually take a look.
From the client SIG.
And the rest seems like it's in the right place.
And it's still waiting for reviewers.
Oh, okay. Trask, this… this… gray one means they are… they are not in approvers, right? But they are inapprovers, the code owners.
Right? Yeah.
Trask Stalnaker (Microsoft Corporation) 00:07:56 Yeah… So we can add, it's just based on a list of, GitHub teams.
So, we can add all of our SumConf Domain, approver groups to that list.
Liudmila Molkova 00:08:17 Yeah, I mean, I think it's good enough, because at least it's important for maintainers to know when it's time to merge.
And I think we maintainers know all the GitHub aliases.
Trask Stalnaker (Microsoft Corporation) 00:08:31 Yeah, but I might add them. It's just… it's just a file to add them into, because I think the point is that they had… they do have green checkmarks.
In this repo.
Liudmila Molkova 00:08:45 Right.
Trask Stalnaker (Microsoft Corporation) 00:08:46 So, I'm not sure why I didn't add them.
Probably just oversight.
Liudmila Molkova 00:08:54 Great.
Cool, then, and there is a bunch that are waiting on the others to address.
Whatever.
Lewis Lewis 00:09:02 Should I… talk about that for a minute?
Sorry.
Trask Stalnaker (Microsoft Corporation) 00:09:07 Yeah.
Lewis Lewis 00:09:07 So I'm here to talk about a PR that is currently categorized as waiting on authors on a, LLM review that doesn't seem to be appropriate.
Because there's a comment about title casing that's actually being controlled by, the actual generator of the docs.
So…
Trask Stalnaker (Microsoft Corporation) 00:09:29 There's sh…
Liudmila Molkova 00:09:29 That's fine.
Lewis Lewis 00:09:31 Yeah, this one.
Trask Stalnaker (Microsoft Corporation) 00:09:33 Yeah, there should be, if we find the comment that it's from the dashboard, it gives you a, command you can… a comment.
Yeah, let's try the bottom, Ludmila.
Lewis Lewis 00:09:52 I can link the specific comment if that helps. It's, on Docs and registry entities Azure.
Liudmila Molkova 00:10:01 Oh, okay, so it says there are two threads?
1 and 2, and…
Trask Stalnaker (Microsoft Corporation) 00:10:09 But right below that, Liudmila, the head run that command, the dashboard route reviewers.
So scroll down. You can just run… you should be able to run this again, and it should route it.
Rounded…
Lewis Lewis 00:10:30 Alright, I'll try it again.
Trask Stalnaker (Microsoft Corporation) 00:10:32 Yeah. Yeah, there was a bug at some point in this command.
Hopefully it… should work.
And it'll… it basically overrides it.
And it used to not override it permanently, but now it does override it, more permanently.
Lewis Lewis 00:10:51 Okay, thank you for the bug fix, didn't realize that.
Trask Stalnaker (Microsoft Corporation) 00:10:55 It's a fairly new, bot that we've, started using in OpenTelemetry. So, yeah, apologies.
Liudmila Molkova 00:11:08 I think it would make sense for somebody… who works on… Azure, to take the first look at this.
I wonder… Maybe, I don't know, Trask, if you want to take a look, or maybe we can ask, Leighton, who's working on the resource detection, I think, for Azure.
If Uku could use his help.
Trask Stalnaker (Microsoft Corporation) 00:11:37 Yeah, I can ask, Blayton. I, I have… I know this has been in my… I didn't book it for a while.
Liudmila Molkova 00:11:54 Okay.
Cool. So, we have this, on the agenda, Lewis, so we can talk about it more there.
Awesome. Okay, so then, let's… Move on to the next topic, the first one, the conformance.
I think, Trask, you added this, right?
Trask Stalnaker (Microsoft Corporation) 00:12:21 I didn't.
Liudmila Molkova 00:12:23 Oh, Jay!
Armin (Dynatrace) 00:12:26 Hey,
Jay DeLuca (Raintank, Inc. – Grafana Labs) 00:12:26 No, I didn'.
Armin (Dynatrace) 00:12:27 Links for it, but the heading was added by someone else.
Trask Stalnaker (Microsoft Corporation) 00:12:33 It was under next, and so when I put… when I created this today's meeting, I copied it down, but there was no name next to it.
Liudmila Molkova 00:12:44 Okay.
Trask Stalnaker (Microsoft Corporation) 00:12:46 It might have been leftover.
Armin (Dynatrace) 00:12:48 Last week's Trask, perhaps.
Trask Stalnaker (Microsoft Corporation) 00:12:52 Yeah, possibly, or the week before.
Liudmila Molkova 00:12:56 I am curious here, what… are the… what are we doing? So, you trust, you have a lot of PRs, and I'm happy to approve all of them. I'm wondering if we need maintainers for the corresponding languages to take a look, or, like, what is the criteria to merge things here?
Trask Stalnaker (Microsoft Corporation) 00:13:23 I don't think we have to have the maintainers, but I… do want to give them a chance. So… I will probably ping them again this week for the ones that haven't reviewed.
And, Then maybe give one more week, and then we can… Approve and move forward.
I'm starting… I'm gonna move forward on the languages that we have merged, working through the… bringing over the… HTTP instrumentations now for Java, and Python.
Liudmila Molkova 00:14:14 Nice.
I'm also… was wondering… I want to add the GenAI native instrumentations here.
And native seems to be… Well, okay, so ideally, we want all of them, right? The native, the different flavors of instrumentations, like open inference or open allometry, who claim support.
Would we… wait for people who work on that other third-party instrumentations to contribute, or would we… Add them ourselves.
Trask Stalnaker (Microsoft Corporation) 00:14:59 I think we would add them, and maybe, if they're not either tag folks, or we could even open an issue over in… One of their repos to let them know, just to give them a chance to review.
Especially in cases where we have Similar instrumentation?
It should be pretty… similar. The test harness, the tests themselves.
But yeah, yeah, I think we should… Move forward on those.
Liudmila Molkova 00:15:52 Oh, yeah, I agree. I… it… It would take us a while, and some… some people would not participate, and… We can't change or take it down if they, complain.
Trask Stalnaker (Microsoft Corporation) 00:16:07 Yeah, or if they give us correct… I don't know if we have to take it down, but we can take in their corrections.
Michele Mancioppi (Dash0 Inc.) 00:16:13 Yeah, exactly. Check it out.
Liudmila Molkova 00:16:21 I would imagine somebody would complain, because the instrumentation, they claim native OpenTelemetry support, and we prove it otherwise.
And they won't be happy about this. I… I think we can still keep it.
Trask Stalnaker (Microsoft Corporation) 00:16:35 Send them to me, I want to have those conversations. That's kind of one of the points of this conformance repo.
Liudmila Molkova 00:16:44 Right.
Michele Mancioppi (Dash0 Inc.) 00:16:45 The fact that you can send data via OTLP, it doesn't mean that it really works well with OpenTelemetry, right?
Liudmila Molkova 00:16:52 Absolutely, yes.
Jay DeLuca (Raintank, Inc. – Grafana Labs) 00:16:57 Hey, Trask, on that topic, I was thinking now that we're starting to have a larger collection of, projects that we're running the tests against. Do you have an idea of what you want the… the reports to look like? Like, I know you have the proof of concept from your… your personal project, I think that had, like, some different categories and, the different labels for recommended versus required, things like that. Would it make sense for us to start putting together something similar for this project?
Trask Stalnaker (Microsoft Corporation) 00:17:30 Conformance-prototype, no.
Ludmila.
Oh, it was the same… sorry, it was the same URL that you had right there?
But with a dash.
Dash prototype at the end.
Yeah.
Liudmila Molkova 00:17:50 Nice.
Trask Stalnaker (Microsoft Corporation) 00:17:51 Because I had to claim the… reclaim the original as my fork of the upstream.
Jay, no, I don't, have any… Real thoughts, The… the goal of the, sort of.
The… this one was designed around, like.
Compressing the data into, like, small, like, Where you can kinda see… easily.
on different things, but I don't know if that's… It also loses a lot of data.
In here, and so… I'm very… I don't really have a strong preference on anything at this point.
Jay DeLuca (Raintank, Inc. – Grafana Labs) 00:18:39 Okay.
Cool.
And you don't have anything in flight, if I were to start poking at that?
Trask Stalnaker (Microsoft Corporation) 00:18:46 I don't. Nope.
Jay DeLuca (Raintank, Inc. – Grafana Labs) 00:18:48 Okay.
Sounds good.
Trask Stalnaker (Microsoft Corporation) 00:18:51 Cool.
And, Ludmila, if you could go to the PRs, there was one PR that you could, the .NET one.
has a maintainer approval, and I just need a… I mean, it has a .NET maintainer approval.
I just need a green checkmark from… Martin approved it.
Liudmila Molkova 00:19:18 Yeah, I… You can look over at that.
Trask Stalnaker (Microsoft Corporation) 00:19:19 later.
Liudmila Molkova 00:19:21 And I've seen it, I didn't approve only because it has expected, violations in the YAML.
Trask Stalnaker (Microsoft Corporation) 00:19:30 Expected money.
Didn't… I didn't fix it?
Liudmila Molkova 00:19:34 Oh, you did? I reviewed it before you fixed it.
Trask Stalnaker (Microsoft Corporation) 00:19:37 Oh, okay. Yes, yes, no, you had a… I… that was a good… Good catch, thank you.
Yeah, because that had to… I had to fix that in my other PRs, too.
Liudmila Molkova 00:19:52 Cool.
Great discussion. Anything else? Should we move on?
Okay, then Trask, it's yours.
Trask Stalnaker (Microsoft Corporation) 00:20:06 Yeah, so server address… In gRPC, we had… we… in the RPC, Semantic Conventions SIG, we decided to expand, sort of relax, I guess, if you will, or… expand what it could be. I think there… previously, the idea was, oh, this was, like.
an actual DNS name, say, although not… not exactly, because there was also Unix sockets and a couple other things.
in… with gRPC, they have this target string, which, for example, could be a zookeeper, look… lookup.
Or it could be, a, you know, comma-delimited list of multiple servers to round-robin across.
And so we decided to… Like, that is… the only other option, really, in that case is to not capture anything in server.address.
We already have network peer address for the… IP address that is actually connected to on any given request.
I guess you could pull that up into server.address, but that would be probably worse.
Because server address is supposed to be the logical address, it's supposed to be the same, like.
the same, or… All of your requests.
And so I've been going through, in the Java instrumentation, repo… We are, applying all the stable database SEM for the 3.0 major version bump, big… lots of breaking stuff.
And ran into this in database servers as well.
Where there's several database, clients, server clients that you can give comma delimited, like, multiple seed servers in Cassandra case, or, like, multiple round robin, things, Postgres, to… to round robin across.
And so… I guess a couple questions, and then… We'll get to discussion here. Should, Well, anyway, yeah, let's just… let's get discussion here, and then we can kind of come to my questions for… specifically for Java instrumentation.
Christophe Kamphaus 00:23:08 So this would also apply to any kind of cluster-based system, also Reddy Sentinel, for example.
Trask Stalnaker (Microsoft Corporation) 00:23:17 Anything where your connection string Has multiple server, like, it's sort of like a… some other format, connection string where you have, yeah, multiple servers that you specify.
Christophe Kamphaus 00:23:33 Also, if it's done via DNS, if the DNS returns multiple IPs.
Trask Stalnaker (Microsoft Corporation) 00:23:42 I think in that case, it's just the DNS… the… the DNS name.
the server name?
As long as it's just a single you know, server. Like, that is the logical server.
the IPs that come back from that are gonna be your physical connections.
Michele.
Michele Mancioppi (Dash0 Inc.) 00:24:07 We have, I came across recently something Like, the very same problem, but worse.
In the Semantic Conventions for virtual control.
When you have… Systems that, like, the code is in one repo, the deployment descriptors in another literally have no mechanism We'll do this.
Technically, at the protocol level, It is allowed to have… The same key is specified multiple times, but we declare it as invalid in a bunch of different places.
And I'm wondering if we need… Something a little more structural as a solution.
Trask Stalnaker (Microsoft Corporation) 00:24:55 So… That, for that example, there's two different servers for two different purposes.
Michele Mancioppi (Dash0 Inc.) 00:25:04 Depended.
Trask Stalnaker (Microsoft Corporation) 00:25:05 Yeah.
Michele Mancioppi (Dash0 Inc.) 00:25:06 Different repositories for two parts of the same story, yes.
But it is very similar to your examples about database replicas.
Trask Stalnaker (Microsoft Corporation) 00:25:21 In the database replica case, though, there's, like, one… Sir, there's one connection string for both…
Michele Mancioppi (Dash0 Inc.) 00:25:40 And I've met more than one database that would put multiple attributes with one keynotation as the connection string.
To allow the client to do client-side load balancing.
Trask Stalnaker (Microsoft Corporation) 00:25:51 Right.
Right, so for the client-side… for client-side load balancing, the proposal is… To have a comma-separated list of those things in the server address.
Is the case you're describing, though, with VCS, sounds like it's not a load… it's not a client-side load balancing, it's two different servers for two different purposes, and… I would argue that that… Should be…
Christophe Kamphaus 00:26:24 We actually thought about that case.
Because… in, one CICD run.
You might pull code from different VCS systems.
But it was not obvious how we should handle it.
And, for now, I think the… Best answer I can give you is to have separate spans, Where you just use one.
Michele Mancioppi (Dash0 Inc.) 00:26:54 It's all semantically not correct.
Christophe Kamphaus 00:26:58 Yeah.
Can you open an issue about that, if there isn't one yet?
Trask Stalnaker (Microsoft Corporation) 00:27:07 Yeah, and I'd like to, like… Narrow this discussion to client-side load balancing?
And…
Michele Mancioppi (Dash0 Inc.) 00:27:16 The reason why I brought it up is because I'm not happy about your proposal either.
Trask.
It makes the querying of the data so awkward.
Trask Stalnaker (Microsoft Corporation) 00:27:28 Yeah.
Michele Mancioppi (Dash0 Inc.) 00:27:30 That's what I was saying, given the fact that it's not just a matter of client-side load balancing.
Maybe we need to think.
How about something a bit more structural?
Liudmila Molkova 00:27:44 What is the alternative? So, it makes querying bad, but that's the closest we get to the server address, the logical group of things you Talk to, and… I mean, something structured, let's say.
At least off, IP addresses, or at least off… Kafka nodes, or Elasticsearch nodes. Makes sense, but it's, like, the extra. Like, domain-specific extra. And the server address we want to have, because this is the universal grouping key for anything client, right?
Michele Mancioppi (Dash0 Inc.) 00:28:24 I'm also not proposing to use arrays Values, because that is equally terrible to query.
I am honestly not sure what the… what a good ergonomic solution is for everybody involved.
Liudmila Molkova 00:28:41 Cha.
Shove the string.
Why is it hard to query? It's in a backstreak.
Michele Mancioppi (Dash0 Inc.) 00:28:51 Okay, because now the user, what do you want him to do? Go and create a regex with capture groups to be able to split the value correctly?
Liudmila Molkova 00:29:02 Oh, they don't need to split it.
Michele Mancioppi (Dash0 Inc.) 00:29:04 But if they do, if the query is, hey, I want to see all the spans.
that go against that URL.
Or that server address. Now you go, you need to split it, so that the value that is conveyed, or one single attribute key, can be interpreted as multiple.
Liudmila Molkova 00:29:21 Oh, no.
they just get everything for this string, whatever it is. So, if they want to get everything against this URL, this is the URL. Sorry, the host part of it. You can think about it this way.
Sven Cowart (ElastiFlow Inc) 00:29:38 And if they're looking for specific nodes, then they would likely use, or should use, network.
peer.local.
Addresses.
Right, because those.
Liudmila Molkova 00:29:52 Yeah.
Sven Cowart (ElastiFlow Inc) 00:29:53 addresses.
Liudmila Molkova 00:29:56 I think so.
Sven Cowart (ElastiFlow Inc) 00:29:58 And if they're not there, that's, I think, the mistake here, because I… I think this is a good proposal, because this is, like, in lieu of a URI or some type of domain name.
Like, where you just have a connection spring, it is the identifier of all the things that are in the back, and because server And client.addresses are… Not trying to actually represent a connection It's a logical address of something, this does make sense to me.
Michele Mancioppi (Dash0 Inc.) 00:30:30 So your point is, we should treat it atomically, because At that point, the weight is intended to be used, for example, on client spans.
It's… one thing… And then the client only later picks one? I'm not sure I did it.
Liudmila Molkova 00:30:53 Yeah, you think about it as a representation of some form of a cluster ID.
Or the central name of the cluster, or the central name of the component that, you talk to.
And… than… there is a layer that's missing. Maybe we will need to edit at some point, but this is, like, the ultimate logical layer. The network, peer… Address is kind of an IP address, and there is something in between the domain name of the node you're talking to.
Which is nowhere in the attributes.
So we have sorry things, and we… that we could record, and we only have two attributes for them, but maybe that's enough for the time being.
But in the video, like… oh, sorry.
The… you would have this as the Bureau cluster, The atomic thing.
And these guys as what you actually talked to.
Michele Mancioppi (Dash0 Inc.) 00:31:59 No cut.
Trask Stalnaker (Microsoft Corporation) 00:32:09 I mean, I… I… Agree that it, Kinda, it probably will not be a user expectation.
Like, that server address has… Multiple servers in it.
And that's… Kind of my main… Concern… But I… Do you… It's a lot better than leaving server address empty, at least.
Michele Mancioppi (Dash0 Inc.) 00:32:47 But it's not a very high bar.
Trask Stalnaker (Microsoft Corporation) 00:32:54 That's fair. But I don't have, yeah, I mean, so, like, what… What would the… our… our… alternative…
Michele Mancioppi (Dash0 Inc.) 00:33:06 I don't know, I feel that in these cases.
We are missing a trick in the spec.
Trask Stalnaker (Microsoft Corporation) 00:33:13 Missing a what?
Michele Mancioppi (Dash0 Inc.) 00:33:15 a trek. We were missing a way to effectively Express in a structured way that is actually supported and worked out.
And adoptable, complex values.
That's how it feels. Like, at the level of the protocol.
We could technically send the different values.
like, the OTLP doesn't force us into a map, technically. Purely technically.
We said in the specs and implementations that there is one value for one attribute key.
And… Sure, that's…
Trask Stalnaker (Microsoft Corporation) 00:33:58 Isn't that just a ray? Isn't that just arrays?
Michele Mancioppi (Dash0 Inc.) 00:34:02 Arrays, technically, yes. I mean, for this case here, that would be array, but we have been very skittish with adopting arrays in the past.
Which has led, effectively, nobody in the backends to actually do this in Java Touch.
Like, I've yet to see a tool, an observability tool, that actually can deal with array values and open telemetry.
And that, at the power of 10 for dictionaries. Like, have you ever seen a tool? Give me actually decent querying capabilities on structured values?
I have not.
So, we are in a bit of a… Feels like a chicken and egg problem, like, we have the primitives to maybe do that.
But you haven't used them, so nobody… Can use them reasonably, and that's why we don't use them ourselves.
Trask Stalnaker (Microsoft Corporation) 00:34:57 So, there's a slightly another… if we look at gRPC case, and we look at, like, the Zookeeper example.
This is more than just… client-side load balance, like, it's more than just an array. Like, I agree that an array could potentially address A common case of client-side low balancing, But it doesn't handle this. And this is where, sort of, the… OpaqueServer.address.
extending that, like, in the same way it's extended for Unix, sockets.
deals… A little bit natural.
Michele Mancioppi (Dash0 Inc.) 00:35:46 It is not my intention to send back this proposal. I want to raise the point that I feel that we are… We are finding the least abominable solution for these things since a while, with no hope in sight of making it… giving it an actual good solution. And it's not even something that is on the spec side, because technically, without the structural values.
But then it becomes not usable in the state… in the practice.
It feels like… Doesn't feel great.
Liudmila Molkova 00:36:24 I think it's not mutually exclusive.
So… a lot of things have server address, right? I can host my… self-host my MongoDB or use the SaaS offering, right?
And the client side should be comparable.
And, I would have, server address that, in one case, says, okay, this is my managed offering. In another case, it's my self-hosted Foo.
Right? Address.
Whatever. And then, you also want to know about the details of your cluster.
in a structured way, maybe it's an array, but maybe it's Mongo-specific, maybe it's generalized, and they coexist. When you build a dashboard, like the default dashboard, you use server address as your foo, and maybe you're not happy with, like, this awkward string that you see.
And maybe we will provide some way to make it better.
Through, I don't know, processing or context sculpt attributes or something.
But, like, this is the fallback. Like, this is the best effort.
To make, like, the default dashboards somewhat… Useful.
Michele Mancioppi (Dash0 Inc.) 00:37:47 And we fall back to strings, because everybody can display strings.
Liudmila Molkova 00:37:51 Oh, no, not because everybody can display strings, because we want server address to be this uni… like, the common grouping key, and it's a string.
Trask Stalnaker (Microsoft Corporation) 00:38:00 People are… people… yeah, people are already using server address for their groupings. They're already using server address for, like, their application map.
diagrams… So I think that… that was what sold me on the GRPC case, was thinking of all these application maps out there that people build that are… Server.address is the critical component there.
Michele Mancioppi (Dash0 Inc.) 00:38:27 Yeah, don't you think that grouping and service maps Are exactly one of those situations where Packing multiple values in a semicolon-separated or column-separated string.
Hides the complexity of the real world from them.
Because now, they have one note instead of three, or two.
Trask Stalnaker (Microsoft Corporation) 00:38:48 Well, that's where you have to do the network peer address.
If you want a physical application map.
then you have to use network peer address. If you want a logical application map, you use server.address.
Michele Mancioppi (Dash0 Inc.) 00:39:08 Alright, I think I get your point. Okay.
Liudmila Molkova 00:39:11 Okay, so yeah, then I'm not going to show it, that's… I was going to just illustrate it.
Michele Mancioppi (Dash0 Inc.) 00:39:20 Okay.
Liudmila Molkova 00:39:21 Okay, I… we spent good… we had a good discussion. I am…
Trask Stalnaker (Microsoft Corporation) 00:39:28 We're gonna experiment some more with the database, Submit the database instrumentations in Java.
And I'll post back my findings to the SemConf channel there, with, you know, what kind of changes that would be, and we can maybe get more feedback next week.
Liudmila Molkova 00:39:52 Awesome. And my initial reaction is, yeah, let's do it. It's the same messaging kind of everywhere, and… The only concern is that, can we do it in non-breaking manner?
For Java instrumentation, it seems obviously…
Trask Stalnaker (Microsoft Corporation) 00:40:05 coming up.
Yeah.
Oh, I see, in Sem Conv… yeah, yeah, so I was… That's kind of my next question, is if, we can say that if… This is sort of some ambiguity in the spec that we can… accommodate.
Or, yeah, if it has to be breaking. Either way, if we think it's a good thing.
I would probably wrap it into the… 3.0 major version bump.
Liudmila Molkova 00:40:41 Awesome.
Sven Cowart (ElastiFlow Inc) 00:40:43 Can I ask a real quick question? Because, the things that we're talking about in the network SIG right now, and I linked to it here, it lines up with what you're saying here, and it'll work.
I had a question around… I think it was 2 or 3 SIG Meetings ago in here, where we talked about, there's the general attributes documentation in the docs. I think, Liudmila, you were talking about how it's awkward where it is, and there's all this duplication between that and the various other points that, touch it. I think it's generalattributes.md.
Where it's just guidance on how to, like, how… when to use certain addresses.
bet.
as a result of this comment that I linked, I'm going to rewrite.
This in a hopefully much more clear way, that resolves some of the open outstanding issues around when to use what.
And also make some suggestions around particularly source and destination, and then we're still ideating on networklocal.peer and how that can be used for, routing protocols, network routing protocols. So… My question is.
Do you… are we still planning to keep that general attributes MD around?
And… Do you want me to take on this… Changing the server address description, or… You wanna handle that?
Liudmila Molkova 00:42:20 I… what I was thinking… Is that we need to refactor this document?
And it's… I don't feel it's controversial to refactor it, like, we keep the attributes, we keep the groups, right? This remains a public group, it's now a public group.
So it's visible from the outside, you can reference it from multiple places. So as long as YAML, keeps making sense, this document can be changed in whatever way I feel.
If you want to make a step on, like, making it structured and focusing on, like, different layers of networking, it would be… Awesome. I, I think it's great.
Sven Cowart (ElastiFlow Inc) 00:42:59 Okay.
Sounds good.
Liudmila Molkova 00:43:06 And I, I think… for… then the outcome of the Trask or investigation database would be to change the database, right?
And then we can tackle the general server address separately.
Sven Cowart (ElastiFlow Inc) 00:43:25 Okay.
That should be fine, because I think, logically, it still makes sense. I mean, in most scenarios.
DNS name, like eSample.com, Logically resolves to any number of addresses.
Okay, thanks, sorry.
Liudmila Molkova 00:43:48 No worries, yeah, thank you for bringing it up.
Okay.
So, Dan Lewis, Azure Container Apps.
Lewis Lewis 00:43:59 This should be pretty quick. Thank you guys for letting me know about the bug. Hopefully that will get it back into the revision queue. We're expanding support for Azure in general, so if this gets approved, we also want to try and propose an instance ID for Azure App Services.
But waiting for feedback on this. If you guys want us to try and combine that into this PR with this long history, let me know. Whatever will make it easier for you guys.
But, yeah, more Azure.
Trask Stalnaker (Microsoft Corporation) 00:44:33 Lewis, Would you be, for having a, a separate meeting? Maybe myself, you, and Kathy, if she's still working on it? And maybe we can try to just… Work through it together.
I apologize, it's… I know this has been on… people are waiting for me to, to, look at this, so I feel like I'm effectively blocking it.
Lewis Lewis 00:45:03 Whatever works for you. Just let me know how you want to arrange that.
Trask Stalnaker (Microsoft Corporation) 00:45:07 What's your, what's your time zone?
Lewis Lewis 00:45:10 East Coast. Me and Kathy are both East Coast.
Trask Stalnaker (Microsoft Corporation) 00:45:14 Okay, I think we have a… do we… are we… I know Kathy has… Reached out on Slack.
I don't remember if I have you…
Lewis Lewis 00:45:25 I have her schedule, too, and I'm sure she would be agreeable to something, if you want to propose a time right now.
Trask Stalnaker (Microsoft Corporation) 00:45:33 Cool. Yeah, how about tomorrow, Noon Pacific, 3 o'clock your time?
Lewis Lewis 00:45:43 That should be doable.
I will invite her and, an email for you.
Trask Stalnaker (Microsoft Corporation) 00:45:50 Yeah, or on Slack.
Lewis Lewis 00:45:52 Or on Slack? Okay. Yeah.
Trask Stalnaker (Microsoft Corporation) 00:45:53 Yeah.
Awesome. Thank you.
Lewis Lewis 00:45:59 Great, thank you so much.
Liudmila Molkova 00:46:01 Thank you.
Okay, Victor, do you want to present? Do you want me to present?
Victor Lu 00:46:11 Yeah, I can, either way is fine.
Because I have multiple links to share.
Yeah.
Liudmila Molkova 00:46:21 So then… Go ahead, present, please.
Victor Lu 00:46:25 Yeah, okay.
Let me share my screen, Ben.
So… Just, a little history of it. So… the understanding is, in OpenTelemetry, the, there's… when it comes to security, telemetry.
There's not as much at this point, Is that an accurate statement?
Liudmila Molkova 00:46:58 When it comes to security, yeah, I would agree.
Victor Lu 00:47:01 Yeah. And so, what's happening is, this is a proposal to, bridge telemetry that exists in both, OCSF and OTEL.
a little history about it. So, first of all, I'll show you, this one.
For… this is, an issue that was created in… OSI, COSI community about, telemetry using OCSF, And then later on, it's basically a combination of OCSF and OTEL.
So, you can go to… one actual OCSF, I know Trask know OCSF very well. So, this one, Mitre DeFend is an ontology, for security.
And it is being followed by, OCSF, as an ontology standard. So… so it's, not directly relevant. So, back to this, main article being published. If you are interested in looking through it, I will go to, Appendix D, That's where this is being discussed.
Let me see… D, yeah, D.
is… what do you mean for OTEL, basically?
And Appendice E is also relevant.
So, at this point, so yeah, so this is… I won't go into the detail, because I know about it, but I'm not expert, so I don't want to misrepresent it. So, this… some of the telemetry will be existing in OTEL, some will be in OCSF. Yeah, detail is documented here.
When it comes to, I think Trask was in meeting with OCSF folks, I think that's more of a broader how to sync the two going forward, right? But this is… separate. This is specific for AI, because OCSF was designed for security, monitoring. However, it did not cover AI. So this is basically extending what OCSF has. So this is… doesn't exist in OCSF either, this is a proposal. So this is a proposal being proposed to both OCSF to extend what they have to cover AI, and to extend to, proposed to OTEL to add security matrix.
When it comes to the history of OCSF, my understanding at least, at Amazon, AWS play a big role in it. So, they have OCSF, originally, a separate group leading AWS also have OTEL, for security.
So… so this is kind of also mitigate what's happening in those communities, including within, you know, our same company.
So that's what it is. So I… that's probably… I can… I can probably talk more specific details, but as I said, I'm not really expert at it. I know the general, picture history of it.
Though?
Any questions?
Trask Stalnaker (Microsoft Corporation) 00:50:26 How much, of this is… General Semantic Conventions… Versus AI-specific.
Reason I'm asking is, I wouldn't, if it's all AI-specific, then… probably the GenAI SIG, that meets on Tuesday.
would be the… the, better place to present, and ideally have the… someone from COSI come who can kind of talk to more of the details.
Victor Lu 00:51:05 Yeah, that's a good question. When it comes to a semantic convention, as I mentioned, that's why I actually shared the micro-defense ontology. So that's the ontology that OCSF already, tried to follow.
And OCSF, and Mitrodefense, which is very well, adopted ontology standard in the cybersecurity community, which include AI now.
So in turn, miter defense follows an upper ontology called basic thermal ontology.
So when… when you mentioned, Trask about, telemetry… symmetry convention.
Is there any upper ontology? Does… My understanding is the hotel doesn't follow any protocol at this point.
So… so, dear… probably should be some discussion about Semantic Convention. Is opera ontology… is it necessary to adjust that, or… etc. Yeah, but I… on the other hand, it is primarily an addition to AI-related, metrics.
Trask Stalnaker (Microsoft Corporation) 00:52:23 Yeah, maybe, I mean, I'll… probably does make more… probably get more interest from folks in the GenAI SIG.
And if there are general things that We would want to push up to General Semantic Conventions.
That could still happen from that group, but… Then we might get more interest in the initial discussions over there.
Victor Lu 00:52:52 Yeah, that's probably the right approach. I just want to bring it up, because I know this is the main meeting. I want to make sure you're aware of it. And as I said, I'm not the right person to present about it, so, the… I think Arthur from Meta is going to be the person who's interested in presenting. He's deeply involved. He's also the lead for that group.
So he will probably present.
To this group when he's ready. Yeah, I'll just let you know this is coming.
Liudmila Molkova 00:53:19 Thank you.
Trask Stalnaker (Microsoft Corporation) 00:53:20 Cool.
Liudmila Molkova 00:53:20 Yeah, and I would encourage to present in the Gene AI SIG, because there is a idea that the consumption format is the trajectories for AI, and then it's yet another Thing that's neither tracing nor Security.
Christophe Kamphaus 00:53:39 Yeah, I also saw in Appendix D, it proposed several changes to the Gen AI Conventions.
That would be good to present there.
And then for how to represent OCSF, over OTLP.
We discussed it, and I think Trask Hugh also joined OCSF meetings?
Trask Stalnaker (Microsoft Corporation) 00:54:04 Yeah, there's, we had some good discussions, but then it kind of earlier this year, but then we kind of lost that, train.
But there… the… there seems… there seemed interest in basically using the… Semantic Convention Tooling.
To… for their, their conventions?
Which would be kind of, easy for them, and… Not, you know, non-breaking, not, and a plus for them, They seem to… One of the folks over there has used the Weaver tooling already, and, liked it, and thought that that would work well.
And while it doesn't solve the question of okay, what do we do with overlapping things? At least then we have Modeling the same, and then potentially we could start the discussion after that of what do we do With overlapping concepts.
One idea that was thrown out was, like.
You know, maybe we just, you know, could we create something called, like, an alias in Semantic Conventions, something that would allow us to, more natively bridge, things that had developed independently, but represent the same things and are just different by names?
Victor Lu 00:55:42 thing, I'm not sure is being done in a hotel community is the adoption of common ontology.
This is, basically more than just a semantic convention, in a way, because they allow you to do, the, reasoning, based on the ontology. So this is actually, let me show you the, the one that's, this one. OCSF follows this standard, the upper ontology standard. By following this standard, it allows you to do, reasoning, basically, when processing a huge amount of OCSF data, they allow you to read them through the, the data, and let AI do a lot of findings and monitoring, etc.
Liudmila Molkova 00:56:33 I want to call time on this. We have just a couple of minutes left, and I think we need to… maybe chat a little bit about, other topics. I appreciate, Victor, the presentation. Let's continue in the Gen AI SIG, and if there is anything general, please bring it up.
Okay, Martin, you're the next.
Yeah. So, anything we can do in a couple of minutes?
Martin Kuba 00:57:00 No, so my topic is just to inform and also just get a sense if we're in the right direction here. In the browser SIG, we are in the process of adding our own registry in the browser repo for… browser-specific Semantic Conventions, which I understand is the right approach for conventions that are very specific to the component, or… the domain… Android has already done this as well, so we're kind of following their lead on this.
We're also in the process of, you know, talking about, kind of having a common… Client side, registry.
So there would be kind of 3 levels, browser-specific, client-side specific, and then the core, registry. So I wanted to just, put it, put this out there, and just, like, see if we're on the right path here.
By this approach.
Liudmila Molkova 00:58:07 I think so, I'll take a look. I will probably leave a comment around the schema, because we have a better schema now.
the V2 schema, and it… it will become the default at some point.
soon, I hope? But it's… it's much better. You will like it, I hope.
Martin Kuba 00:58:25 Yeah, yeah, that's… I would like some direction on that, yeah.
Liudmila Molkova 00:58:31 Yeah, so I'll, I'll, review.
Martin Kuba 00:58:35 And as far as…
Trask Stalnaker (Microsoft Corporation) 00:58:36 Which is great. I, I, I fully support, This kind of narrow, like, ownership model.
Martin Kuba 00:58:47 Okay, cool. This, this PR that, was opened.
Just recently, I think, is… that I just noticed.
I think it actually should go into the browser registry.
But maybe, Trask, like, you… I know that you also wanted to talk about, like, how we would communicate between these… Make sure, like, the… Proposed semantic mentions go in the right place.
Trask Stalnaker (Microsoft Corporation) 00:59:19 Yeah, it looks browser, so yeah, it should go into the browser repo.
And the… what I would, What I would love to see is, like, when you all get a PR or a proposal that, you know, is kind of ambiguous how semantic conventions, like, we don't have strong precedent for how you should model it in semantic conventions.
It would be great if you could bring that, you know, to this meeting, and kind of share, you know, the options you're considering, and just, you know, allow us to, like, consider that as well.
Martin Kuba 00:59:57 Okay.
Liudmila Molkova 01:00:02 Yeah, sorry, we are out of time, and I'm sorry, Eva, we didn't get to your intro, I'm so sorry.
Trask Stalnaker (Microsoft Corporation) 01:00:11 You,
Liudmila Molkova 01:00:12 Hopefully see you next time. Appreciate your coming.
Iwa Wong 01:00:17 That'll be in the next time.
Neil Yashinsky 01:00:18 Thanks, everyone. Bye.
Trask Stalnaker (Microsoft Corporation) 01:00:20 I,
Christophe Kamphaus 01:00:20 See ya.
