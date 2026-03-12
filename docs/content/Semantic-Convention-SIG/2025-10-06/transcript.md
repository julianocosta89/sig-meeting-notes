SIG: Semantic Convention SIG
Date: 2025-10-06
Duration: 34 minutes
============================================================

## Zoom Recording Transcript

**Joshua Suereth** 00:21 Alright, can you hear me?
**James Thompson** 00:23 Yes, I can.
**Joshua Suereth** 01:04 Alright, apologies, I was getting the, Agenda up and ready. So folks, we have… I think we have a bunch of vacations today.
For holidays, I should say. So please add your topics under General Topics.
I think this was discussed last week, too.
Yep.
Cool.
Alright, I'm gonna give it, like, 2 minutes here, I need to fill out a few things, and then we'll get started, while we wait for some people to join. Sound good?
Alright… Okay.
Alright, well, welcome everybody, we'll get started. Cool. I think first we'll do a little bit of… telemetry, man, my brain is dead. Do a little bit of triage. I think… We'll start with PRs.
Alright So what I want to do is go through and do a quick check on some of these that are blocked.
And, make sure that, we understand why they're blocked and whether we can make some progress on any of these. Heroku semantic… Conventions matching official documentation.
Match our existing documentation for fur generation applications, PR line semantic official Heroku symbols… Right.
Why is this one blocked?
**James Thompson** 03:48 Because they deleted attributes rather than deprecated them.
**Joshua Suereth** 03:52 Gotcha. So we just need to make sure this is safe. Okay.
And we have no updates on this.
Alright.
**James Thompson** 04:00 It's only been a couple of days.
**Joshua Suereth** 04:02 Yep, that's cool. Alright.
Let's come back and check out… Ad spans for app launch screen, load time visible.
I think this one is blocked by the front-end folks.
And… Just to check the last thing… yeah, 5 days ago. Okay, so this one's still appropriately blocked.
These are in recency order, so let's actually go to the older ones first to see if any of these are explicit ID for FAS entities.
I believe this one… is blocked by a gel. Let's take a look at what that was.
**James Thompson** 04:43 It was a discussion about using cloud resource underscore ID as identifying for the FAS function entity.
**Joshua Suereth** 04:57 Gotcha.
Yeah, okay, this… this basically is… it needs to go through the SIG.
Which I believe is, I think Oberon might recommend, Oberon and Tyler are two that we need to get.
on board for this one. Okay, cool.
So that one's still blocked.
We'll spot check one more.
Check collision… no. App details.
This one, I think, needs to go through our front-end folks. Looks like they're on the review.
Okay.
It looks like this is blocked based on what the definition of app is.
**James Thompson** 05:59 but I think there was a misunderstanding.
**Joshua Suereth** 06:01 luck.
Yeah.
to use service name and friends instead of having explicit app equivalents. Okay, so they are moving towards service name. Gotcha. Does this one need to get closed, then, and get, updated?
Based on that direction. Like, I feel like this, probably, you want to discuss with the client-side folks.
**James Thompson** 06:25 Yeah, because, like, I'd still have service.
**Joshua Suereth** 06:29 Yeah.
**James Thompson** 06:31 Alright, like, service is perfectly valid.
**Joshua Suereth** 06:36 What I'm asking is the path forward for this PR, should we actually close this PR and reopen things against service, or have that discussion and design before we make a PR?
I'll discuss it with Klein, Right? Because, like, it doesn't change any of the existing guidance.
I understand… what I mean is, when this is a PR, we have 134 pull requests that I'd like to start going through. If this is still in a discussion phase, let's keep it as an issue.
Until we know what we're actually going to do or move forward with, if possible. Especially when you get feedback saying, hey, we're not going to use application anymore for this. So, like.
I think, this one, unless anyone feels differently, we should close and continue discussion in an issue or design.
Of how we're gonna move forward for client-side applications.
just so that it doesn't sit here, we don't keep reviewing it every week, in terms of, this is blocked, how does it make progress? Because it's blocked, and we're not… we're basically… I don't think we're able to make progress in the PR as it's implemented in this PR. So, That's, that's, that's my point there.
Anyway, let's move on, because that one looks like it's still appropriately blocked. Did a few spot checking these. Folks, the ones that are awaiting code owners' approvals, please, try to get through these. Like, again, if you look, we have a lot of PRs backing up in semantic conventions, and I do want to try to make progress, so we're going to try to make it through In this meeting, we're out of our time box, but we're gonna try to make it through about 7 minutes of checking on blocked PRs, see if we can make progress on things, and move forward. Unfortunately, I think all of those actually were continuing to be blocked.
**Christophe Kamphaus** 08:31 I think the guidance and Informetric 1, we can close.
**Joshua Suereth** 08:35 Which one?
**Christophe Kamphaus** 08:36 C, CICD one.
Guidance and InfoMetric.
**Joshua Suereth** 08:43 guidance on InfoMetric per CIC pipeline? So you want to close this down?
**Christophe Kamphaus** 08:48 Yeah, I think that one also needs some more discussion, what it even means to use Infometrics.
**Joshua Suereth** 08:55 Okay.
**Christophe Kamphaus** 08:57 I created the issue, but yeah.
**Joshua Suereth** 09:00 Wow, am I not logged in?
Alright, let me share something else while I log in. Do you mind… do you mind marking that closed and say that you'll bring it back once the discussion, has.
**Christophe Kamphaus** 09:09 Yeah, I can do that.
**Joshua Suereth** 09:11 Thank you, thank you Okay, yeah.
Cool. Right, and just… just for context, you know.
we have, I think, 8 maintainers right now, and we have 100-some open PRs. I have about 30 minutes I give to triage in the morning, and I am basically unable to get to things I can merge in that 30 minutes. So, One of the things we need to start doing is make sure that, like, status of PRs are cleaner. I think you've seen Yao, spend a lot of time on a triage process where we're going to be moving PRs around, making sure that they have the appropriate annotations and go to folks, but, yeah, I think we're doing a lot in PRs that maybe we need more issue discussion, and like, we need help here making it through, making sure that, things are reviewed and things are updated. Because I think right now.
A lot of those PRs are pretty stagnant, and I'd like to fix that.
Okay.
With that said, we're 10 minutes in. Do we have any general topics? I have one thing I want to discuss from last week. Does anyone have anything else? I'll open it up before I continue.
Okay, cool. So I think there was a discussion the previous week from, Michelle from, Dasho about peer.star.
Let me add this here.
So, I think one thing I want to detangle is this discussion is very focused on service name.
In that, that's fine, but for context.
There's a PR here to update the peer namespace to match the service namespace.
Inside of semantic conventions, and I think I can show this if I go here, and we make this visual, there's a peer attribute that talks about the remote service you're talking to.
And so we had this notion of peer.service, that would be the service name.
And they want to update this so that we deprecate the previous one, and we have it match the new, the new set of attributes for service.
There is a SIG that got started, which will start stabilizing the service attributes.
I think the main problem with peer is that PEER is one of these namespaces that Anything could be part of?
Possibly.
I think we used to have peer IP address, for example, and I believe that got removed before we moved into YAML.
But, yeah, anyway.
I want to have a general discussion about this notion of peer and the peer namespace.
So, what I want to avoid, which I would consider a failure state, is if we have to update Every time we make a change to namespace A, we have to make a change to namespace B that is exactly the same change. I think this is problematic.
Alexandra, I see you're on the call. I think this is where the… the notion of, like, a role, or a, I forget, what did you guys call it in ECS?
**Alexandra Konrad @Elastic Security** 12:31 A rule, you mean? .
**Joshua Suereth** 12:35 No, where we had, like, the attribute prefix, like you were gonna use for geo and latlong.
**Alexandra Konrad @Elastic Security** 12:47 Hi, you mean, the client and the server?
**Joshua Suereth** 12:52 Does…
**Alexandra Konrad @Elastic Security** 12:54 This is why we have used the geo only.
**Joshua Suereth** 12:57 Yeah.
Yeah, but it was, you were working on, like, having a standard prefix to this, where you would have… you define geo… As, like, a group, and then you could reuse it in different areas with, like, a prefix to it, right?
**Alexandra Konrad @Elastic Security** 13:12 Yeah, but this is just a generic injection of namespace into another NXP.
What we have discussed, yeah, for reusing any namespace, it's not related to the geo, particularly.
**Joshua Suereth** 13:35 Okay, right, that's, that's… that's the thing I was talking about. So previously, we had this notion where You could say the service namespace, or the service set of names, you could define a new namespace that would kind of be a prefix to it, that would add context to that namespace for, like, a different usage of it, and would allow you to kind of have the same things in.
I don't think we have a way to do this in SEMCOM today, and this makes me slightly nervous in that, you know, anytime someone changes the service namespace, they might not be aware of the peer namespace to make changes here.
Especially as we, like, standardize and fix things. So, this kind of coupling between the two is something I feel like we need a more general mechanism to handle, if it's something we're going to support. But then it.
**Alexandra Konrad @Elastic Security** 14:34 It seems to be very close to the embedding.
**Joshua Suereth** 14:38 Yes.
**Alexandra Konrad @Elastic Security** 14:40 Let's say, in general, embedding structure that we have discussed, maybe we should, start it again with additional example, like the peer service.
**Joshua Suereth** 14:51 I think…
**Alexandra Konrad @Elastic Security** 14:52 example, I mean, one of the examples we also had before, though.
**Joshua Suereth** 14:56 But…
**Alexandra Konrad @Elastic Security** 14:58 Maybe with a new…
**Joshua Suereth** 15:01 Examples coming to the semantic convention, it would be easier to implement it.
Well, this actually runs into the same problems we had before. For example, is it, is it going to be the case that everything in service shows up in peer, or only a subset?
**Alexandra Konrad @Elastic Security** 15:18 Yeah, we have discussed different options, how we could fix it, yeah, so that you might either split them between, let's say, base fields, extended fields, or maybe every time when you reuse fields, you provide a selection of the fields.
I think… What is important to discuss is that We need to distinguish between, embedding as, paradigm, like, we just allow to embed service as a namespace. But, you should define which fields you want to use in that particular use case. So, those are different, I feel, things, and they got mixed, that's why I believe, there was so much, pushback, because.
**Joshua Suereth** 16:16 you…
**Alexandra Konrad @Elastic Security** 16:17 You might use all of the fields if you want to, but you might also use only specific fields if it's relevant for your application, for this specific use case.
So… So definitely go.
**Joshua Suereth** 16:30 I personally think… I'm not… Personally, I still have problems with the peer namespace.
I can, I can show an example.
So, right now, what we have is in OTLP, we have a resource, right, which will be service.name equals A.
Then, underneath that, we have scope, and then we have span, and under span, the name will be, you know, like, get slash dot dot dot, whatever. And then we'll have here, peer.service.name, right? Equals B.
But my question would be… Option 2.
Why not just make this be… Service.name.
Right?
Because here, I know… Let's just say… Kind equals client.
That wasn't meant to all be caps.
I know that it's a client spin, so I know I'm talking to a client, so I actually know that the attribute is, Oh, let me make this bigger, so it's more readable.
I know the attribute, It's actually, like, contextually about the spin.
So why do I need peer?
**Alexandra Konrad @Elastic Security** 17:53 I think this is because of our flattening the structure, yeah? Because if you, unflatten all of this, you don't have this tree structure, and what you have in the end, you just have service name A, and then you just have service name B, because you need some kind of prefix, and you cannot have two similar fields. This is the problem we have, yeah?
**Joshua Suereth** 18:18 That's a problem that some databases have, I would agree, yes. But from the OpenTelemetry data model, right?
doesn't this actually mean the same as this? And so, if you have a data source that needs to put peer in front of it, great, put peer in front of it, but if we were to actually send this on the wire.
That's li- that's valid today. Someone, like, someone could actually do this today.
in OpenTelemetry. There's nothing that would prevent them.
**Alexandra Konrad @Elastic Security** 18:47 But that means… Okay.
Yeah, maybe, maybe for this particular example, for the pier… You might solve it differently.
**Joshua Suereth** 19:04 I think the.
**Alexandra Konrad @Elastic Security** 19:05 The problem comes when you have multiple service names in one set of the data. Like, if you… if we come back to the geo, yeah, question, if you have both client and server, and they both have geo information, you need to have that prefix client or prefix server.
With the peer, if there is only one peer service name available in the set of the data, like, in one chunk of the data, then probably it's not a problem.
**Joshua Suereth** 19:37 Yeah.
I… so, another way to phrase this… I've been thinking about this in two ways, right? So, this is, like, how I think about it raw, with raw attributes. The second way is, in context of entities.
Alright, so, in context of an entity, we define an entity called service, and service has a name, you know, namespace, etc.
And so, the way, the way I think of this here is resource has service entity.
And then, the span… Has service entity with context, like, you know, this is the pier.
So that's actually how I would think about geo, right? Like, Actually, with geo, I think of it in terms of types, and we talked about this before. So, I can define… let me… let me do this a little bit better.
geo, right? I can define, geo that has a lot, and a long, and maybe other things, so this is types. And then what I can do is in, in semconf, I would say, you know, I have a client.request.location.
is, type GEO.
And so this would be a way of saying, cool.
geo is lat and long. When I say I have client.request.location, implicitly means I have .latin.long, but this is what the attribute is that I would… that I'd be referencing.
Similarly, if we wanted to do service, we could say peer has type service.
And then any of the attributes from service are available. That's kind of… that's kind of the way I've been leaning for SemConf, for the way we do embed.
**Alexandra Konrad @Elastic Security** 21:33 And for the example of… Let's say, process, yeah? So the process… Has also… we have a process namespace, and then we also have a process.parent, which itself is the namespace.
sorry, the process namespace. We cannot have both namespace and the type, because, you know, this should be…
**Joshua Suereth** 22:00 This…
**Alexandra Konrad @Elastic Security** 22:01 like, in ECS, we distinguish between, namespaces that could be on the top level, top level, like, I don't know, process, client, etc. And then we have those specific set of, like, geo, set of namespaces that allows to be only embedded, so you… you cannot have geo just without parent, because it makes no… no sense. Like, you say it, it's kind of type, geo, because it's always connected to something. And, we might define it in the semantic convention also differently, because I really see how it fits into the type. So if you can only attach that namespace as a geo to something, it fits perfectly into the type. But if it's something that might be both kind of namespace and type as well. I'm not sure if it's, nice.
**Joshua Suereth** 23:06 Mixed, you know.
Yeah, this is where I think maybe we can do things… again, this is like designing an API, but we can do things like, okay, cool, for process, we'll have a process reference.
And the process reference would be just some of the attributes. And then we could reuse that in places that need to refer to a process.
that have context of the process, but aren't gonna send the whole entity, or the whole namespace. Same as service ref, right? Service ref could be service.name and service.namespace.
And then, The peer would be of type service ref, if we want peer to be service ref.
The problem I have right now, by the way, with Pierre, is that I think Pierre is way too frickin' generic.
As a namespace, because you could put anything inside of it.
Any possible attribute could go into a peer.
Right? It's not… it's different than geo.
Because GEO… we were talking about doing, you know, client.requestLocation, or server.request.location, or, you know, like, resource location, of, like, where physically is my thing. That… or… that makes sense to me, as, like, different things with GEO.
Because you can limit it and say, oh, that location kind of tells you it's only geo.
Pierre is very interesting, because basically underneath Pier, Oh, I guess we could say peer.service.
might be type service ref, and that'd be fine. Peer itself is way too generic, though, because I think any possible Zemconv… could go into peer, the way it's defined.
And, to me, that is awkward as heck, because when we look at spans, and we'll say, like, okay, cool, I have a span that's a client, and I say, what is the, The address, right?
or the URL of that client, it's implicit in the span that it's at the peer or the remote at times.
Sometimes it's not, sometimes it's explicit. Actually, let's take a look. We can just show that.
Anyway, apologies, my thoughts are somewhat loose today, so hopefully this is making sense for the discussion.
**Alexandra Konrad @Elastic Security** 25:29 I agree with you regarding the pier, because if you just look… if you just take the name, you don't understand what it means. It's, like, we had similar with the rule, yeah? It's a rule, but, like, that's why we changed to the security rule to be more specific. And I feel the same with a peer. It's just too broad to understand what exactly it, reflects what semantic meaning it has by its name.
**Joshua Suereth** 26:00 Yeah, like, for example, here, we say server.address, right?
We don't… we don't say peer.server.address.
We say server.port. We don't say peer.server.port when we have a client that's talking to a server.
**Alexandra Konrad @Elastic Security** 26:16 But don't we have pier here somewhere?
Yeah, I think I saw the pier.
**Joshua Suereth** 26:25 I'm looking at all the HTTP things where it was appearing.
Network.peer.port. Yeah, that is… that is a place where we do have a peer, and network.peer.address. Okay.
That is a bit more specific, though, because it's a network peer, but still.
Alright.
And I believe that this is used in the event of a, what do you call it? A reverse proxy. I'd have to go look at that.
And we have the user agent that we're sending, yeah.
See, my… this is… this is why I feel like Pierre is somewhat problematic raw, although we do have it here.
**Alexandra Konrad @Elastic Security** 27:14 But it's… it has prefix, so this is a bit different.
**Joshua Suereth** 27:18 Yeah, like, peer.service versus service.peer, right?
That's kind of the difference. So we actually have a naming convention issue here, too.
If we scroll down, I think there's a diagram here of… sorry for the jumpiness.
Server address, server port. This is the attributes reported by client, attributes reported by server. Notice that the server.address is always the server, like, it's always the peer.
from the client.
And then, when they do have peer… let's look at the server side. Again, that's less important, because I don't think peer would show up here, but it might.
Pure.port does show up here. Yeah, go ahead.
**James Thompson** 28:13 If you go to the general folder and the attributes one, there's the three diagrams which show more information about how those attributes are used.
**Joshua Suereth** 28:25 Yeah, I know, but Pierre is somewhat of an old SimConv, and, like, some of our thinking has changed and adjusted over time.
So, I… I actually am… this is causing me to start questioning Pierre a little bit.
You're talking about this diagram?
**James Thompson** 28:43 Yeah, right, because that actually shows… that shows some more details where network.peer differs.
**Joshua Suereth** 28:49 Yes.
So this is the address that's actually over here, and this is the address that's over there. And this is something you absolutely need.
However, like, for the purpose of tying together service name, if you look at server address here, right?
there's no peer in that. If you look at client address.
there isn't necessarily a peer in that. Like, we could have… I feel like this is the thing I'm more looking at when I think of peer.service.name. This is kind of a specific, I need to debug, like, lower-level networking things.
And that's where peer starts to become important, because you need to know who you're communicating through, and I believe reverse proxies matter here, right? Because that's where peer starts to get confusing.
But I don't know, like, I don't see a convention where we're using peer with service name kind of still makes sense.
In my mind. But I wanted to kind of talk it through with folks and get some feedback on that before I make comments on the… on the bug, just to see, like, where we all sit, you know?
If you look at server.address, it's called server address. It's not called peer… this is not network peer address. This is not network peer URL.
And over here, it's client address, it's not network peer address. Even though, for reverse proxy, it'd be different, and that's an important thing for us to understand, but we don't say, like, you know, server.peer.client here, right? Peer isn't showing up in these two things.
And yes, it does show up here.
But when we think of the notion of a service A talking to service B and tracking that A talks to B, that's similar in my mind, of talking what client is talking to what server.
And so, I don't think that the peer usage with service name matches the peer usage here for network port.
So… Anyone else have thoughts on that? Just curious, after walking through this.
**James Thompson** 31:04 One scenario I do see for PR, right, is currently, if you look at stuff like the S3 conventions, they're using RPC service to specify if it's… talking to S3 or DynamoDB, for example.
There's a scenario of it wanting to describe what it's talking to.
Alright, and… There, it's specifying the app it's talking… the service app it's talking to on the other end.
**Joshua Suereth** 31:41 Yeah, but it doesn't say pier.
It literally says RPC server. Again, every time, every time we have… we have a client span, and we talk about the attributes on the span, we don't… we don't clarify it's a peer, because it's always a peer.
that you're describing. You're talking about a span that's communicating as a client to a server, or as a producer to a consumer, right? And so, it's implicit that it's a peer.
Like, this just says RPC server, it doesn't say service, it doesn't say peer.rpc service, or rpc.peer.service, just RPC service. Same with RPC method, right? It's implicit that that's the method, the peer method that you're talking to.
I mean, RPC service and method are kind of… They're somewhat special, because that's actually how you, like, formulate the request.
But, like, you know, cloud region, it's not the pure cloud region, it's the cloud region of the thing you're talking to.
So, I personally think peer is just problematic, because I feel like it's implicit in the design.
And I know that a bunch of people will absolutely hate this as a model if we move from having peer service name here to just putting raw service name.
It's just, I… this… this, in my mind, is more open telemetry.
And matches more of the other SEMCOMF. And maybe we come up with a different name for it here, but I'm very hesitant to just greenlight peer the way it is, because of how you know, intense it is… how expansive it would be and how invasive it could be. And I can't come up with a litmus test in my head of when do you put peer and when do you not.
Right?
So that's… that's kind of my… my personal thinking. I will write this down on the bug, just so folks have it. I need to formulate more of my thoughts, but, Cool, if no one has any other topics, I don't want to waste everyone's time. Thank you for… listening to me rant about Pierre, Seems to be a quiet day. Anyone have anything they want to talk through?
If not, everyone have a great day, and yeah, we'll see y'all next week.
**Alexandra Konrad @Elastic Security** 34:04 Thank you. You too.
**Christophe Kamphaus** 34:05 See you.
**Armin (Dynatrace)** 34:06 Bye-bye.
