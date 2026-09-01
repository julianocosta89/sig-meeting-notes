SIG: Semantic Conventions SIG
Date: 2026-08-31
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Christophe Kamphaus 00:00:22 Hello?
Sven Cowart (ElastiFlow Inc) 00:00:24 Hello.
Uri Smiley 00:00:25 Hello, good morning.
Sven Cowart (ElastiFlow Inc) 00:00:27 Good to see you.
Hanson Ho 00:00:51 Hello, everyone.
Sven Cowart (ElastiFlow Inc) 00:00:56 Hello, buddy.
Hanson Ho 00:00:57 For Sunday.
Good morning, and good afternoon, and good evening for some, I'm sure.
It's the first time for me attending this meeting. Should I put in a topic, in the doc, in the next section, or should I wait until… I'm here to talk about client-side, Semantic Convention Federated stuff, so…
Sven Cowart (ElastiFlow Inc) 00:01:21 Should drop it on the agenda, and the next section is there. When anything in the agenda doesn't get covered, it gets added to the next section for the following week's call.
Hanson Ho 00:01:31 Perfect.
Christophe Kamphaus 00:01:32 Add your name to the attendees for today, and any topic you have, add it here to the agenda.
And to start with, let's do some triage.
We have our nice full request dashboard.
Let's take a look.
Let's see these two PRs.
the JVM one… Let's see here it's awaiting code owners.
Do we need any additional… We'll see her?
Trask Stalnaker (Microsoft Corporation) 00:02:43 I think it's probably okay, I'm, I'm in that code owner's…
Christophe Kamphaus 00:02:52 And we can merge it.
Trask Stalnaker (Microsoft Corporation) 00:02:55 Let's do it.
Christophe Kamphaus 00:02:59 And the other one, what's the hotel SDK span started.
I see we have a lot of approvals here.
I think we can merge that one as well.
Trask Stalnaker (Microsoft Corporation) 00:03:30 Not count spans from… I remember there was a spec…
Christophe Kamphaus 00:03:38 Now I see here is this one.
Trask Stalnaker (Microsoft Corporation) 00:03:52 Maybe just ask CJ… Yes.
It's… Ready to be merged, or…
Christophe Kamphaus 00:04:31 avoid some… Let's take a look at the waiting on reviewers… We have here a few.
With approvals already.
Oh yeah, I remember this one.
It added, see more.
for all enums.
Yeah, so… Maybe let's take a look and… If you… Give a few more approvals, we can merge that one as well.
Liudmila Molkova 00:05:43 Hello, hi everyone.
Christophe Kamphaus 00:05:45 Hello.
How's this one?
What's that an approval?
But it's about messaging.
Liudmila Molkova 00:06:14 It would need someone to… yeah, go ahead.
Trask Stalnaker (Microsoft Corporation) 00:06:18 Does it have a prototype?
Christophe Kamphaus 00:06:27 Yep, looks like it.
Trask Stalnaker (Microsoft Corporation) 00:06:29 Okay.
Oops.
Good.
I can… I can, I can look at that from the… the Java side, at least.
Liudmila Molkova 00:06:47 Yeah, I can look at Brighton.
So I reopened it because we had this agreement with, Chashank, I think?
That… You would send a few.
Pointed.
Or requests for messaging.
And, We will take a look. Like, he's very interested, and he's contributing a lot to instrumentations in Python, and, like, whatever findings that exist in the current instrumentations, I think, are fair game.
Trask Stalnaker (Microsoft Corporation) 00:07:27 Yeah, I'm good with that, because we just updated all of the Java messaging instrumentations to the latest semantic conventions, so it's… At least fresh in my mind of thinking about them, so I can… I can look at… messaging stuff.
Liudmila Molkova 00:07:52 Awesome.
Christophe Kamphaus 00:07:55 And maybe I lost PR to take a look.
Yeah, I think this one wasn't… Small one.
Liudmila Molkova 00:08:06 Yeah, I think… What's the deprecation?
Christophe Kamphaus 00:08:08 It's different.
Liudmila Molkova 00:08:12 Thanks for looking. I have sent a bunch of PRs to… small PRs to… Helpless V2 migration, these are the blockers for V2.
Christophe Kamphaus 00:08:25 Yeah, I see some here.
I will take another look at the other ones.
This evening.
Liudmila Molkova 00:08:34 Thank you.
Trask Stalnaker (Microsoft Corporation) 00:08:34 Yeah, I'll look through them also.
Thanks for moving the V2 stuff forward. The refinement, I am seeing the advantage of getting the V2, especially the refinement stuff, in the, Conformance testing would be nice, will be nice.
Liudmila Molkova 00:08:55 Yeah.
Christophe Kamphaus 00:09:01 White, I think we are out of time for triage.
Let's go to the agenda.
I am.
Do you want to Presents this one.
Uri Smiley 00:09:16 Hey, so actually, yeah, so actually Rahan is out today, I'll be presenting, I'll be presenting the Atrace context propagation.
Christophe Kamphaus 00:09:27 Do you want to share, or should I show something?
Uri Smiley 00:09:31 you could, is this the… is this the issue, or is this the design here?
Christophe Kamphaus 00:09:37 It's the pull request.
Uri Smiley 00:09:40 Oh, the pull request. Yes, you can just share that one, I can talk through it.
So, two weeks ago, we came here and presented an issue, For, trace con… trace, context propagation, from client to server.
And the idea is that, just to give a brief overview for those that haven't seen the design or seen the issue, the problem is that client instrumentation can create database client spans.
And a server can create its own spans, but there's no broadly usable client-to-server… I'm sorry, there's no broadly, usable client-to-server context propagation that exists currently for MongoDB-compatible databases.
So, this PR, this PR aims to address that by providing a mechanism in the, comment field.
So the proposed value is a BSON document, with required trace parent and optional trace date.
And an optional text, for a string comment, which replaces the use for a baggage there in the, in the command operation.
So the receiver, receives the envelope only when it is a document containing a valid top-level trace parent.
Which means that any invalid, context, does not fail the database operation.
The comment is used here because it is already understood, by current drivers and servers, including compatible MongoDB services, and it does not require a new opcode or additional round trip.
It also keeps propagation separate from query expression or operation text, which makes it a practical carrier that instrumentation… instrumentation can use in today's ecosystem.
So we actually have a public prototype of this working already in the DocumentDB project.
And it kind of proves the path here, so in that project, we have a propagator inside of the gateway, that extracts the trace parent from the JSON encoded string in the comment.
And it treats that, trace parent as a remote parent, and it leaves the, malformed, or ordinary comments alone.
So, what I'm looking for guidance in this, meeting is, do we want to accept, the shape that we are, proposing here for the comment field?
And, what are the, the future requirements for this, this PR to… emerge here, and any other guidance that we have, for, like I said, the shape of the comment field, or any concerns that we have for data that is being passed in, in this proposal.
And I'll just keep that opening brief here so we can open it up for discussion.
Liudmila Molkova 00:12:53 I think in the past… thank you for presentation, by the way.
We have it documented for some other database, I don't remember which, and the problem with SQL, at least, was that, having it in common ruins the cache, or ruins the Yeah, so, like, because the trace parent is different on every query.
Then, the database would have… rebuild, everything around query.
Is it the case here?
Do you know?
if I think…
German Eichberger 00:13:31 No, no. Yeah, no, that's not the case here, so the Mongol thing doesn't… doesn't have prepared statements like they have in SQL, so that wouldn't be a problem here to use the common field. In fact, we know people already use the common field to have their traces being submitted. It's just not standardized.
Trask Stalnaker (Microsoft Corporation) 00:13:53 We do also know, though, that people are using the SQL comment field, the whole SQL commenter, to pass them.
Uri Smiley 00:14:03 Yes.
Trask Stalnaker (Microsoft Corporation) 00:14:03 Today, but it doesn't, make it a good thing because of the prepared statement stuff, but that's good to know that it's not a problem for Wongo.
German Eichberger 00:14:13 Yeah, no, no Mongo doesn't know about prepared statements, they don't know that.
Liudmila Molkova 00:14:21 Yeah, then on the first site, I don't have any… big concerns.
Trask Stalnaker (Microsoft Corporation) 00:14:30 Yeah, I think it's great to, you know, to document, to specify these, database-specific.
Trace propagation protocols, And, yeah, as far as moving the PR forward, I would just, you know, look at the… comments. Right now, it's… it's waiting on… in our dashboard, it shows up as waiting on author, because there's some open comments. Right. So as soon as you… Once you reply to those. You don't have to accept them all, or any, but just reply one way or another what makes sense, and then it'll go back to the reviewers.
Christophe Kamphaus 00:15:18 Yeah, there's also a failing check here.
German Eichberger 00:15:21 Yeah, yeah, the…
Christophe Kamphaus 00:15:22 I think this should fix it.
German Eichberger 00:15:25 Yeah, the big problem we have is, Rahan's out for 3 weeks, and so… Yeah, we would like to move that faster, if there's a way to… But, yeah.
Uri Smiley 00:15:35 Most of the suggestions I saw, we can go ahead and apply here. I don't see a problem with that. I don't have these buttons on my UI.
German Eichberger 00:15:44 Yeah, probably because we're not the authors, yeah.
Uri Smiley 00:15:46 Yeah, so…
Trask Stalnaker (Microsoft Corporation) 00:15:52 Yeah, you're also welcome if you want to just open up a new, you know, just port the PR Open up a new one on a, you know, somewhere that you have access to update is fine from a… from our perspective.
Uri Smiley 00:16:08 Makes sense.
German Eichberger 00:16:11 And, yeah.
Trask Stalnaker (Microsoft Corporation) 00:16:12 That was… could be awkward.
Neil Yashinsky 00:16:15 Thanks. Hey, Uri, how's it going? Did I pronounce it right? I was just curious, and you probably already said this, so forgive me if this is a repeat, but, did you say how you are, for lack of a better word, like, adding this information to the trace? Did you say that? I'm sure you probably did, but are you using, like, is that injected via code, or…
Uri Smiley 00:16:34 Yeah, injected via the OTEL propagator. So they use the OTEL propagator to generate the… generate the trace parent, and span ID, for the For the comment field.
Neil Yashinsky 00:16:47 I see, I see, okay. And that's, okay, I've just been experimenting, with the OTTL a little bit, and I was just kind of curious if that was something you could also do this way.
to… if it would offer any advantages. I'm really new, so I'm… I'm… way in front of my skis. Everybody on this call probably knows a whole bunch more about the OTTL than I do, but it seems like it's, really useful and capable, and I was, yeah, wondering if it could do that here, too.
Liudmila Molkova 00:17:17 I think here, it's important to propagate the context to the database, so the injection needs to happen in the process.
Uri Smiley 00:17:24 Yes.
Liudmila Molkova 00:17:26 An OTTL would only run on the collector, where it's too late.
Neil Yashinsky 00:17:32 Okay, thanks so much, Liudmila, for that, for the, for that, clarified point.
Liudmila Molkova 00:17:38 Thank you for bringing it up.
Neil Yashinsky 00:17:40 Yeah, good stuff, Uri looks cool.
Uri Smiley 00:17:42 Thank you.
Christophe Kamphaus 00:17:47 Right then, should we move on to the next topic?
Trask, it's yours.
Trask Stalnaker (Microsoft Corporation) 00:17:56 Yeah, just, bringing this back from last week, opened, issue. This is about, clarifying the database semantic conventions, what server.address should capture in the case of multiple logical servers, such as a cluster, or seed server, multiple seed servers, or… Some… or discovery… some other discovery protocol.
And so this is following what we have done in RPC already.
And, realize this is… You know, it could take a few people, it could take folks, a little bit by surprise, the server.address.
field, not being a server.
But… It… Does seem like the, best… case there. Otherwise, basically, we shouldn't capture anything there. If there's multiple, it would be incorrect.
And it still… it does allow you to group and see that logical server. It is… it is… and server.address is defined as a logical server, so… It does make sense, yeah.
I… I think, it's just a… You know, that's the one concern, obviously, is… it's probably gonna look odd to some folks seeing this comment delimited list in server address to begin with. I think people will grow to appreciate it.
As, hey, this is really my… what I've pointed my driver at, this cluster.
And then there's a couple… if you scroll down, to Ludmila's comment, she kind of calls out the… some important pieces, as far as… You know, a standard way to format it, comma separated.
Sorted alphabetically if it's a true, like, cluster and ordering doesn't matter.
And… Yeah, so I've done… I've basically prototyped this in Java across all the database instrumentations.
And if you go to the second link in the agenda.
Sorry, the Java implementation link.
Yeah.
So this… documents, and it does, It was a good exercise, because also I found that network peer address was not being captured, correctly in a lot of places.
And network peer address is a really key piece here, and answers the user's question of, well, if my server address isn't the one I actually connected to for a given query, where is that information? I still want that information, and that information Should still be there in network peer address.
Liudmila Molkova 00:21:37 Should there be an AP, or the DNS name?
Trask Stalnaker (Microsoft Corporation) 00:21:44 Network PR address, I think, is defined as an IP.
Christophe Kamphaus 00:21:50 Makes sense.
Trask Stalnaker (Microsoft Corporation) 00:21:51 IP.
Christophe Kamphaus 00:21:53 Yeah, if server Trust is the DNS, And then it's resolved. It could be different IPs.
Trask Stalnaker (Microsoft Corporation) 00:22:03 Yeah, and that was… that whole DNS thing was one thing that made me feel better about sticking… Some kind of service registry thing into server.address.
Because, essentially, DNS is a service registry Anyways, a name, DNS name.
So… It makes sense to me, to… extend that to any kind of… because at first, I was like, oh, should we have some other indicator, like, oh, this was a registry service that it used to look up the real server names?
But I'm thinking no… in that… DNS is a service registry itself.
Yeah, Iwa.
Iwa Wong 00:22:59 Yeah, I'm curious about, if, it sounds like, the domain name is not something that you would want, to fill in in the telemetry. I'm curious, like, if not here, then where, because one of the things that, I'm struggling with, with, some of the bad actors is that because IPs are really, dynamic. Some of them actually, swap them, some of them don't really trust… I can't even trust it, because, they craft some kind of, special packets, to do… so some of the times, like, IP, I couldn't trust, like, what is being said, is from.
So sometimes, like, we can find traces of bad actors, like, if they are being resolved to a certain domain name, so there's more context around that. Otherwise, like, we… I mean, I have to actually build some, like, man-in-the-middle.
accuracy.
just to get that information. So I'm curious, like, if not here, then, like, where do you think we can capture some of the… DNS name.
Trask Stalnaker (Microsoft Corporation) 00:24:18 Yeah, so a couple… things, server.address, can be, a DNS, often it is a DNS name.
In the single connection case.
Or a comma-separated list of DNS names, if that's how the, connection was configured.
I think the other thing is, I think you're talking more about the, client IP, scenario, as opposed to the server IP.
So on server telemetry… so this is client database telemetry, where it's reaching out to Presumably one of our known, you know, something that you know, and is trusted.
Versus on server telemetry, where you're… we're capturing client.address, which is that IP address of the, the client.
Iwa Wong 00:25:26 Okay, interesting. Yeah, I can, talk more with you, also to understand more about thinking. The use case I'm thinking about is that because, some of these AI agents, there's a lot of, approvals that are being done under the hood, like, without even human oversight. So the trust there, is questionable, when you have non-denomistic controls. Yeah, so, let me slack you and understand your thinking from there.
And, go from there, but yeah, I mean, it's a great PR. It's the toughest thing out there right now.
Trask Stalnaker (Microsoft Corporation) 00:26:06 So that's a good… I think I understand what you're asking from the… the… yeah, from… In that case.
Are those, you're thinking, like, HTTP client, or I guess it could be database client connections, even.
Yeah.
Iwa Wong 00:26:24 Yeah, for example, like, MCP connections, like, these are non-deterministic controls that are making these connections. Sometimes, like, the agent itself could also be compromised, through, like, supply chain attack and whatnot. So, one of the challenges I have, is to.
hey, I mean, identify, like, if these IPs can even be trusted, number one. Number two is, like, I mean, where… what is this IP being mapped to, for domains, for HR contacts on, hey, if it is actually malicious or not?
So because IPS is, can be churned, from what I've seen. So, yeah, I mean, I can take it offline.
Trask Stalnaker (Microsoft Corporation) 00:27:12 Yeah, just to close on that, the… and yeah, feel free to ping me. Server address would typically be the DNS name, and network peer address would typically be the IP address.
Iwa Wong 00:27:25 Okay, call it. Thank you.
Christophe Kamphaus 00:27:29 One question.
if you select one Of the possibilities in the server address.
And that itself is a DNS name.
Would that be captured somehow?
Or would we lose that information, and we would just keep CIP in the network address?
Trask Stalnaker (Microsoft Corporation) 00:27:53 Currently, we would lose that information, and we would just get the IP address.
Christophe Kamphaus 00:27:59 Yeah.
Trask Stalnaker (Microsoft Corporation) 00:28:00 Yeah, I think there's a couple of other, like, the… there's some weird cases where you might have a proxy server also in there.
Where we might lose something… Huh.
Hey.
I think those… problems… Are, you know, worth calling out, but probably need a new lay… like, additional things As opposed to affecting… what I think server address should be the logical server, and net… Where peer address should be the actual peer IP address, and we may need some extra things in the middle there.
Christophe Kamphaus 00:28:46 I've seen.
Liudmila Molkova 00:28:47 transport spend.
It's like if we had the actual span for individual network call.
We would capture the server address there.
Would have a chance of being right.
Trask Stalnaker (Microsoft Corporation) 00:29:02 Hmm.
Liudmila Molkova 00:29:03 But also, like, with service discovery, there is no guarantee It will be… there will be a sort of redress at all.
Oh, sorry, the, the dominion, the main name.
Christophe Kamphaus 00:29:35 Should we move on to the next?
Topic?
Sven Cowart (ElastiFlow Inc) 00:29:43 I'm ready.
Everyone else is ready?
Christophe Kamphaus 00:29:47 Go ahead.
Sven Cowart (ElastiFlow Inc) 00:29:48 Okay, so the first one, Hopefully this one will be a little quicker. So as the network SIG is working on figuring out what each address means.
And, if we need more of them or not?
Which I'm trying to avoid, but I can give… I'll get back to that in my next question, but there is this idea that, typically when… you have an address, or an IP address specifically, you have a bunch of other additional metadata that you want to relate to that specific address, something like, think of ASN number, the ASN name, geolocation information, what CIDR is this in, all that kind of stuff.
And the question is, is I don't think there's this concept of, okay, this is an IP address type, or an address type, and when an address type is present, here's all the Dozen to two dozen attributes that could also be Put next to that the sibling addresses so that they don't have to be restated in a bunch of different places, and potentially introduce, what… opportunities for them to diverge over time. Because that's… that's kind of one of my concerns, is that, okay, we have that address now in 6 different places, and maybe more in the future, and… We want to… already someone has brought up one issue about prefix, for that address, and now do we need to go through every .address and add the… well, client server actually might be because we're so… Specifically, I'm calling that the logical one might actually be excluded from that, this conversation, so maybe it's 4 right now.
But do we want to repeat all those attributes across all common All the registry files that have .address, or is there some way to say, like.
If you have .address, this is the best practice, or there's an IP type that, if there's a .address, you can have all these other sibling attributes that relate to that.
Does what I'm making make sense?
Or what I'm saying makes sense.
Liudmila Molkova 00:32:02 I think so. We had these discussions in the past, and they've stuck with the implementation, but essentially the idea was… I'm just pasting the issue with the previous proposal.
that we have a concept called embedding. We would say, okay, there is a… namespace.
And then, like, in the late… later thinking it was a type, like, an address.
Sven Cowart (ElastiFlow Inc) 00:32:33 Right.
Liudmila Molkova 00:32:33 like, IP address in Java or some other primitives in a language, and it has a bunch of properties.
And if we have this type.
And can we put this type in different namespaces, and it would be in the same and evolve consistently everywhere?
Yep. This example is about geolocation.
But then you can specify, okay, like, there is an additional prefix. I think it… the proposal got stuck in two different places. The first one is, what are the rules? Like, what are we allowed to change? Is it always a prefix?
Or is it, like, can we change arbitrary… Places in the name.
Sven Cowart (ElastiFlow Inc) 00:33:18 Hmm.
Liudmila Molkova 00:33:19 I think the second one is I'll try to find a Weaver issue, on how to implement it. It has this proposal of types. That's, like, a type as a group of attributes.
And it's pretty much aligned with the thing we are adding in V2 called Public Attribute Group.
So it's, it's like a group of attributes that has an idea around them. They always come together, they, We have some stability guarantees around them, we cannot just remove things.
I, I don't remember all the details, but let me, see if I can find Weaverish here.
Does it ring a bell? Is it, like, are we talking about the same thing?
Sven Cowart (ElastiFlow Inc) 00:34:02 Yes, yeah, this is basically exactly the thing that we want in our need to make sure that as time goes on, these things evolve together, and not independently, because they are in different, areas and different namespaces. So yeah, this is exactly it.
So it sounds like there is some work Being done, but it's somewhat stuck or stale.
At this time.
Liudmila Molkova 00:34:28 It's completely stale, you can see it's, like, 2 years old.
Sven Cowart (ElastiFlow Inc) 00:34:31 Yeah. Okay.
So would the recommendation then to be for… I should look at this and see if we can move it forward, or, I think that's what I'm hearing.
Because it didn't get rejected or closed or anything, right? So…
Trask Stalnaker (Microsoft Corporation) 00:34:49 The concept came over from, Elastic's common schema.
Sven Cowart (ElastiFlow Inc) 00:34:54 Okay.
Trask Stalnaker (Microsoft Corporation) 00:34:55 Which has, embed… I think they have that concept, so it's worth looking at how they've…
Sven Cowart (ElastiFlow Inc) 00:35:03 Yep.
Trask Stalnaker (Microsoft Corporation) 00:35:04 Implemented it also.
Sven Cowart (ElastiFlow Inc) 00:35:06 Okay.
Yeah, we actually.
Trask Stalnaker (Microsoft Corporation) 00:35:10 I don't remember any…
Sven Cowart (ElastiFlow Inc) 00:35:11 Same concept, too, in our internal schema that we have today.
Trask Stalnaker (Microsoft Corporation) 00:35:16 I don't remember any… Problematic, like, objections to it, other than… We just never dug into the details and saw nobody really made it happen.
see what.
Sven Cowart (ElastiFlow Inc) 00:35:32 Yeah.
Trask Stalnaker (Microsoft Corporation) 00:35:33 The corner cases were that we need to worry about, or anything.
Sven Cowart (ElastiFlow Inc) 00:35:38 Okay, sounds good. That's really helpful. It's probably a case of there's a lot of work that needs to be tackled for something like that, to be done effectively across documentation and such.
Liudmila Molkova 00:35:50 I don't…
Sven Cowart (ElastiFlow Inc) 00:35:50 Highest priority.
Liudmila Molkova 00:35:52 I think it's just nobody put an energy into building a proposal, and the tooling question is the… the hardest one. So, like, what you see here is… It's… Additional scope that we don't need yet.
I'll probably have a comment on this waiver issue, because it conflates this, attribute groups, which are types, with the type of, like, event body, or an attribute, I think they are different things.
No.
I'll… I'll leave a comment on this, and maybe we can detangle it. And then the question is, what is the… to make a proposal in Weaver, and how to represent it in schema?
And probably, in some way, touch attribute groups.
I'm going to guess that Josh will be extremely happy to get something better than attribute groups.
And I… like, as long as we agree on the design and, like, the… what it all means, like, what does it mean to add something into this type? Is it, like.
Breaking? Should it be propagated everywhere?
all these edge cases, but I think we are all bought into the idea that it needs to happen, it's just somebody needs to have the… put the energy to make it happen.
Sven Cowart (ElastiFlow Inc) 00:37:20 Okay, that sounds good.
Christophe Kamphaus 00:37:23 Yeah. Afterwards, you can also then think about what does it mean for Weaver Life Check.
How would you generate CD docs from it? How would you generate code from it?
Liudmila Molkova 00:37:37 Yeah, great point.
Sven Cowart (ElastiFlow Inc) 00:37:42 Okay, I'll review those things you sent, and then give more thought, and then probably… Yeah, I'll… after that, next steps will probably become more clear to me from… on my side.
All right, on the next one, do you mind if I take over the screen share?
Christophe Kamphaus 00:38:01 Sure, go ahead, I will stop sharing.
Sven Cowart (ElastiFlow Inc) 00:38:04 Yeah.
Alright, so, I opened up a PR to… Hopefully make it more obvious and clear for people trying to create instrumentation to decide on which addresses to pick. A lot of this comes from when we were starting our work around how do we represent Routing protocols?
it was very un… routing protocols and NetFlow, it was very unclear based on the documentation, and the guidelines as to what address port pairs we should be using. And so… this is my attempt at rewriting the general attributes, where, markdown file, where this is discussed in the past under Server Client and shared network attributes, to try to demystify some of this. It's a little too much to all cover in this call, so I'm gonna give some key highlights here, and then, Open… I have some open questions, for the group at the end.
So… First, I just kind of give a introduction as to why there's three different things, and part of that is some of the stuff that you just discussed, like, Trask, like, this is the logical representation, and so it means you can also actually attribute, Something with the physical socket and the separation between them, and then how that can change depending on where the actual observation point is.
different pairs can make sense. And so, I talk about that there, but my hope is to make it pretty… let me see… I can't make this a little… it's kind of hard to read when it breaks it up like this.
But I try to make it pretty clear with some tables and some… ASCII diagrams of what is each one of these addresses telling you about what is happening, and when you should choose what. So… what you see here is… what I'm trying to say is, when you're using client and server.
You're typically observing almost always at Layer 7.
And so, you… And this is then the logical and deproxied, meaning that you're not… it's not the physical connection.
address or connection string or something of that sort, so none… that doesn't change at all. The definition there doesn't change.
For client and… or, sorry, for source and destination, it's about who sent and versus, received this exchange.
And that is typically happening in L4, so NetFlow, right, is an L4.
Protocol, or when there's no clear client-server role, and that typically happens in peer-to-peer networks.
And in peer-to-peer networks, there is no, there typically is no intermittent area, like a proxy or… or load balancer, or something of that sort. So, there… is a change that, and I'll get to this, but a change in the definition for source and destination, that I'll get to in a little bit. And then network local and network peer doesn't change. It's still the same thing, the actual physical connection. So I try to make it really clear, okay.
What are you observing? What layer? L7? Use… and it's clear what the protocol you're using is, and it's not a peer-to-peer protocol, then you know who the initiator is, client-server. If it's symmetric peers, or anything like BitTorrent blockchain, it's source destination.
If you're observing layer 4, source destination, and you can add, network.local and peer if it's an endpoint and done through, like, eBPF, which we'll be adding to OB. And then there's an open question around how do we represent L3 and L2 address addresses, because that is where the lots of the routing protocols live, and right now there is no clear guidance on that. So I opened this PR, by the way, as a draft, because there was still open questions and things to figure out, so I didn't want to open it yet until we had this discussion.
So, I'm gonna skip down a little bit.
And I give an example of how things can coexist, and then just a decision guide, which is… just, textualized version of what I just kind of discussed here.
And… and then also, like, why things have to coexist, even for source and destination, and it's because… That they can flip, depending on the direction of traffic that's happening. And then, yeah, so… Let me just pause real quick.
D… make sure I'm… Is there any questions about that? Like, do you think this is useful or needed?
And I know I didn't… I just kind of really briefly skimmed. I don't want to take up the whole call, so I'm hoping this clears up a lot of the questions that exist and issues that have been open in the past about where I should use what.
So, the…
Trask Stalnaker (Microsoft Corporation) 00:43:31 The L7 and L4 make a lot of sense. You lost me once you go below L4, sorry.
Sven Cowart (ElastiFlow Inc) 00:43:38 Okay, yeah. No worries. We'll get to that. So, there is one ques… so, there is no real change in client server definitions. There is one thing I wanted to call out, though, which… In client and server definitions, it says something about, Like, if you don't… I forget where exactly it is right now, but if you don't have… If you don't know which side's the client, which is the server, which would typically just be the case for peer-to-peer, fall back to source and destination. Otherwise, if you're an instrumentation library, you should always know, or at least you can know.
if there's absolutely no way to do it, which I would find incredibly strange, but maybe it's a limitation of the language you're working on that might be a little bit of a fringe case that I'm not aware of, then you should use some type of, like, a… A port-based heuristic, where it's highest port is the client, lowest port is the server.
And that would probably be in a less than 1% case where you'd have to do that. But if you're instrumenting L7, you should always use… unless it's peer-to-peer, you should always use client-server.
And make that the recommendation.
Would we… would we be okay including something like that? Like, that kind of heuristic?
Liudmila Molkova 00:45:08 Yeah, I think it's useful, and I'm going to read your PR that anytime… it's education for me, so, like, as Trask I'm lost under L4.
And, it would, like, be a great way for us to learn about, edge cases we never even thought about. Right, okay. I maybe have a couple of suggestions on, not the technical content, but the process.
I think it might be useful, and I'm curious what other maintainers think. If we kind of separate the changes to guidance in, like, in YAML, Versus a comprehensive guide in Markdown.
If they are, like, orthogonal, or if you think they need to come together, it's also fine, it's not too much content.
Sven Cowart (ElastiFlow Inc) 00:46:07 Personally, I think I'd like to see them together, because there would be opportunity for them not to… Be consistent, then.
Because the definition of the recommendation in some of these files is changing, where I… so… And let me get to that next part, too, because the source and destination one, what I'm saying is that on those, and you can see… The recommendation right now is that When it's communicating through an intermittentary.
They should represent the destination address behind any intermittent areas, for example, proxies, if it's available. But that is not possible.
In most scenarios, or not how it works in most scenarios, where you would use source and destination.
For example, if you just have some network gear sitting there exposing an interface and switching like a typical network switch, and it's producing flow records, you're not going to know what's on the other side of the pack, because it's just pass-through.
So… what I'm changing here on the definition, and this is the same on source, is that I specifically call out that this is what, should be the receiver addresses served at the point of instrumentation, and then it should not resolve to an address behind admittent areas or proxies or load balancers, so it's always an IP address.
Liudmila Molkova 00:47:34 Okay, cool. Then the other small ask is, this general attributes. It's a giant file with a lot of unrelated things. Maybe we should, move the networking guide, put it in the maybe same folder.
Aww.
Sven Cowart (ElastiFlow Inc) 00:47:53 Happy to do that. I've always hated this file, so I think that's great. So, and then I could just remove all this other stuff that's related to networking in this file, is that what you're saying?
Liudmila Molkova 00:48:04 Yeah.
Sven Cowart (ElastiFlow Inc) 00:48:04 Yeah, no.
Liudmila Molkova 00:48:05 Or maybe just keep a link that there is also a networking guide to you.
Sven Cowart (ElastiFlow Inc) 00:48:09 Yeah.
Okay, that makes… that makes a lot of sense. Cool, I can do that.
Liudmila Molkova 00:48:16 One more…
Christophe Kamphaus 00:48:17 Isn't the most part of this file about networking?
Sven Cowart (ElastiFlow Inc) 00:48:22 It is, yes.
There's a little bit about services at the end.
Liudmila Molkova 00:48:29 I think there is also thread, cod,
Sven Cowart (ElastiFlow Inc) 00:48:33 And so…
Liudmila Molkova 00:48:34 mother's tough.
But if it files… if this file disappears, I, I wouldn't mind.
If we have the content captured.
elsewhere.
Sven Cowart (ElastiFlow Inc) 00:48:47 Yeah.
Trask Stalnaker (Microsoft Corporation) 00:48:47 Right now, it feels like a junk drawer.
Sven Cowart (ElastiFlow Inc) 00:48:52 Yep.
I could see this becoming a, like, a table of contents, maybe, for the rest of the… general… Guides, if anything, like, one place to land?
Wow.
Liudmila Molkova 00:49:08 It's kinda the top-level folder in Docs.
Sven Cowart (ElastiFlow Inc) 00:49:11 Yeah.
Liudmila Molkova 00:49:12 I'm thinking, do we want to keep, like.
For other areas, we have a top level.
dedicated area, and I think Network deserves it.
Or what… Create the network, we would put this guide there, we would put any future spans and metric definitions, or link to existing ones.
Sven Cowart (ElastiFlow Inc) 00:49:42 Yeah, yeah. Oh, I see what you mean. Yeah, this is already the tip, like, the table of content.
Yeah, okay.
That makes sense.
Alright, I would be happy to do that.
So let me come to my last question, then. And I know you said you're not too familiar with L2, L3, so maybe we need to just talk about it a little bit, and then come back with some more details.
So there's these routing protocols, BGP is a popular one, OSPF, LD, you see them right there, OSPF, BGP, LLDP, ARP.
they operate at L2, L3, and this is typically how… from the networking space, you would do topology discovery, saying, like, it's like, alright, who am I connected to? Show me everyone. And when you want to do topology discovery, to find all the physical devices that are connected via the network, you'd use something like this, and that's also how they could figure out where things are.
And, so… The… the question is, is we have… The unfortunate part is the… usage of local and peer by the Linux kernel, which is where I think that came from, because it maps to the, those Linux methods where get peer name returns, right, the address that you're actually connected to based on sockets, so this… These words are overloaded in a lot of ways, especially when you combine sockets, with… routing protocols. So the question here is, Do we want to?
reuse and open the… expand the definition of this to also include the addresses inside of routing protocols? Or do we want more address attributes for each one of the Routing protocols, which would mean that we'd have something probably like network.bgp.local.address, And… One, and then local.pgp.peer.address, or whatever makes the most sense for one of those routing protocols.
I worry about… this… the explosion of attribute?
that that would create, just like, now I, like, this guide that I had before would become, okay, if you use BGP, use the BGP address. And then additionally, what I even worry about even more in this case is, if you are an end application.
like, any observability platform that exists now needs to be aware that, oh, if I want to find everything related to this IP address, now I have to look and not… 3 potential, because you probably know… well, you might not even know for that query. I have to look in 6 places, now I have to look in 12 to 18 places, and… That is a concern to me. So, I would love to be able to open up that definition to include L2 and L3 things.
And then give them… like, really define… but it does break, then, the concept of network.local, that address is only a logical address. So, it would be that Network.local.address and its peer, sibling are… logical addresses, if you're observing at L7, but if you're observing at L2 and L3, then they are… physical addresses.
Of neighbors and peers.
Christophe Kamphaus 00:53:41 One question I would have is.
Would you use these attributes together?
like, if you are now describing BGP, which you use network local and network peer, as well as the BGP-specific attributes.
Or would you… Always only, use one set.
Sven Cowart (ElastiFlow Inc) 00:54:09 I think you'd… you'd only use one set, because if you're… If you're instrumenting… if your goal is to, provide telemetry about BGP?
there would not even be sockets, because at L2 and L3, there is no sockets.
So that part of it wouldn't become relevant.
I think that's what you're asking.
Christophe Kamphaus 00:54:35 Yeah, yeah, because I was wondering, is it only a matter of, The concept, is it now the physical connection, or the logical?
Address.
Or could you always use?
These attributes, network local and network peer, and… Maybe distinguish, at which level you are describing stuff.
By specifying, maybe, network type, or no protocol type, something like that.
Sven Cowart (ElastiFlow Inc) 00:55:08 Yeah, exactly.
Christophe Kamphaus 00:55:09 to, describe… Refinement, or, What it now means in the context of a specific protocol.
Sven Cowart (ElastiFlow Inc) 00:55:23 That's exactly how I would see it happening. It's like, that network type would then tell you what is… like, what is the definition, or the meaning of .local and .peer in this context.
And same with protocol, would be a further refinement.
D.
the alternative that, well, if I had to, rebuttal myself here and play devil's advocate against my own argument about address sprawl, is that it does overloading these… These attributes… makes it less clear exactly what they are, and so then I need to look at something like network.type and .protocol to even know Okay, is this a logical one, or is it a physical one?
Liudmila Molkova 00:56:22 I'm thinking that's exactly the… the thing that… where we would be delegating to the SIG?
To make the decision.
And, like, have built a consensus, and, it's awesome that you're running it via, like, in front of the SAMConf SIG, and please keep doing this, but it's like, If there are people here who have the level of expertise and opinions.
to contribute, maybe it's good to decide that this and the SIG, and then bring this decision back.
Sven Cowart (ElastiFlow Inc) 00:57:00 Okay, yeah, sounds good. What I can do, too, is I can go… would it be helpful if I go to the, specification SIG with the same thing, and, Maybe, like, the system SIG or something like that to…
Liudmila Molkova 00:57:13 I mean, you have network in SIG, right?
Sven Cowart (ElastiFlow Inc) 00:57:15 Yeah, yeah.
Liudmila Molkova 00:57:16 This is this thing that should make the, the proposal.
Sven Cowart (ElastiFlow Inc) 00:57:20 Oh, yeah, no, what I mean is make the proposal, and then just cross-reference with them to say, like, hey, does this make sense? And, Because…
Trask Stalnaker (Microsoft Corporation) 00:57:29 Well, that… that would, I think, be during the PR review, right? Okay.
Sven Cowart (ElastiFlow Inc) 00:57:33 Okay.
Trask Stalnaker (Microsoft Corporation) 00:57:34 you all would make a decision and put up a PR, and then, yeah, it would be great to advertise that PR in, like, the specification slash channel, the one I was just… The one piece of, like, kind of… Prior to, thing I… but, like, I could give was that… I mean, I think you're, we've made… We put priority on, Observability backends and users querying things.
Where, like, if you're, kind of to the… even the server.address discussion we were having about that being logical is… That… But that allows a super common use case of building an application map.
Of your connections.
And… You know, in that case, all you care about is server address being, you know, low cardinality, groupable, you know, representing where you're connected to, to build that graph.
And so those are the kinds of things, you know, that I would look at, is look at what the user experience Yeah.
Navigating their telemetry, building those kinds of flow charts.
What's the simplest, what sort of… Allows, you know, future… You know, things to fall in, and then, you know, and then weigh those against the technical precision.
Sven Cowart (ElastiFlow Inc) 00:59:20 Yeah.
Trask Stalnaker (Microsoft Corporation) 00:59:22 But we have… I'd say we've… In the past, we've kind of tried to steer a little bit more towards simple for, Building those charts, trying to think around, like…
Sven Cowart (ElastiFlow Inc) 00:59:45 Yeah, I, I… the… I hear you, and I agree with you.
The… The part that's difficult is if you want to… If you want to be able to also speak to the NetOps people.
Like, they see an application service map and say, I don't care.
I want to see what all things are actually connected by the network, and that's where they need that, like, to your point, like, they typically see a network topology map, which is very, like, a DevOps person's service map.
And, and… and to… to do that, we need to… we just… just right now, it would be not possible in OpenTelemetry to do that unless we change some of these definitions. And… So I'm trying… the crux of what I'm trying to figure out is how to bring those two together so that Someone could show an app.
Map, and the other person sees a topology map of the same traffic and the same communication happening, and it's just a different lens on the same data.
Yeah, so that's kind of… that's how…
Trask Stalnaker (Microsoft Corporation) 01:00:57 And it's okay.
okay, networking is a complicated, complex area. It's okay if the solution ends up being more complex than, you know, what we have.
Today.
Christophe Kamphaus 01:01:09 Yeah, we are out of time. Great discussion, everyone.
Trask Stalnaker (Microsoft Corporation) 01:01:15 Right?
Christophe Kamphaus 01:01:16 Bye. Thank you. See you next week.
Liudmila Molkova 01:01:18 Sorry, Ricardo, I didn't get to your topic.
