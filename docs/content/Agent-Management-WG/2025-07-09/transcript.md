SIG: Agent Management WG
Date: 2025-07-09
Duration: 38 minutes
Zoom Recording URL: https://zoom.us/rec/share/k2rnlTW_ij4dVKQYkS9gHAg8kKj7hwP50ifH9rcuZoPrNPwDzyGPG4XF8Y3HONY.aWteFmKGRGwRuvFa
============================================================

## Zoom Recording Transcript

**Michel Laterman** 00:24 Little.
**Andy Keller** 00:28 I'm.
**dpaasman** 01:37 How long.
**Evan Bradley** 01:57 Hi! Everybody!
**Andy Keller** 02:20 We just started.
I know tigrid's out by the way he's on his Pto, he said. Reach me, reach out to me on slack, but didn't mention it.
The agenda but I know we don't need to wait for him, so looks like Evan.
**Evan Bradley** 02:38 Yeah, so I mean, this is just an issue for context. But I think there.
it's probably just a good time to ask this question in general, which is, how? What kind of
I mean? Do we?
Does anybody have any like kind of thoughts or preferences, or experience? With what kind of telemetry we want to admit from the Supervisor, A and B.
How do we want to go about standardizing that like? Are there
certain things that we would like to see in the semantic conventions to make it a little bit more generalizable. I mean, obviously, right. Now, we're just working with.
you know the supervisor starting collectors, you know. Just one collector, really. But you know you can generalize that to any kind of supervising process. Starting another process or
you know, an OP Amp
supervising process. Not necessarily the Supervisor specifically starting agents.
I don't know. Again, it's just kind of a general question. I just was trying to think about this issue here, and realized that we really don't have any kind of roadmap for for this sort of thing.
**Andy Keller** 03:59 Is there is there anything in the Supervisor? Right? Now.
**Evan Bradley** 04:04 basically just logs. I think that there might be possibly some span somewhere, but just logs for the most part. Which is, you know, obviously kind of the
what I want to say. It's almost like a freebie, I mean, usually you have. You know, you print some kind of log from just about every application.
I in this one proposed events, which is.
you know, essentially just a log with a schema. So nothing really.
you know, 2 different there, but we already have.
You know, the SDK in there, and plans to admit traces and metrics.
**dpaasman** 04:44 I think I saw Pr. Not too long ago, adding a few metrics to the Supervisor. I don't know if that ever got merged
But I do remember seeing that Pr.
**Evan Bradley** 04:56 That might be the Pr. For this issue.
**dpaasman** 05:00 Okay.
See?
**Evan Bradley** 05:04 I haven't. I wasn't really able to look at it, but I am
not totally sure about all 3 of the metrics here. I think one of them makes sense, but the other 2 I need to. I think I need a little bit of convincing.
we can start with events. I don't know if I've had. I think Tyler Helmuth, from Honeycomb said that he wanted traces at 1 point. I don't know if other people prefer traces, I know.
The the person in this issue said that you know not necessarily. Everybody is doing tracing. So you know, it's possible we? We choose a an easier
signal like logs, or maybe metrics in some cases. But I don't have.
I don't have any good compass necessarily. Here.
**dpaasman** 05:55 I know we have a customer that uses a supervisor fairly heavily, and that's been a
something they brought up a few different times is getting metrics into it. And like, similar to what they have here, like metrics around, like how many startup attempts there there are! How many failed startup attempts
like messages from the collector, like they just wanted, like every single possible
metric added into it, which I think is, you know, on the
extreme side, but do know that there is
We have at least one customer that would be in favor of that.
**Evan Bradley** 06:41 So can you speak to a little bit of their motivation there? Like to me.
**dpaasman** 06:46 Yeah.
**Evan Bradley** 06:47 Far as startup attempts go like that that feels like that's a you know. That's a moment in time. That's more of an event.
and you can aggregate that into a metric. But it's
like, if they have something they want to do with that metric. Maybe that would help justify it.
**dpaasman** 07:01 I can't. I can't say like exactly
how they want to use it, just because I don't know but for them it's been
really just getting a good
it's really just monitoring the supervisor. They want to be able to get as much information as they can from the supervisor
in their case they don't really have
easy access to the supervisor. So they're looking to get as much monitoring information as they can
in that situation, you know, it's not easy for them to just go and get on the machine to see what's going wrong.
So that's why for them. They want, like an abundance of information.
**Andy Keller** 07:50 Yeah, just a little more context, it's like an IoT kind of deployment. So and there's like lots of them.
And
so even if you could get access to any one of them which you can't really there's just like too many to really they. They need some
it would be a lot of logs if they were getting logs, but they're not getting logs, because they're all on the device.
So if they can emit telemetry. I guess they could omit logs, obviously. But
They.
They were more interested in in metrics.
**Evan Bradley** 08:27 Okay, no, that's a good
**dpaasman** 08:29 That's a good kind of point of data.
**Evan Bradley** 08:32 And they aren't able to, or are they? Do you know,
are they able to like? Take the logs and then aggregate them in something could they like, send them to a collector, and then aggregate them into metrics and forward them that way? Or.
**dpaasman** 08:49 Yeah, yeah, that that would certainly be an option for them.
They also are concerned with like.
unrelated and a separate issue. But they're concerned with being able to
turn logs on and off remotely or like and change
basically like the telemetry settings. Remotely so like if they don't, they don't want to always be collecting debug level logs. But then, when something is going wrong, they want to be able to
turn debug level logs on.
So I it's not like a
great answer for your question. But you know that
it's kind of related to it.
**Evan Bradley** 09:39 No, it's good to get any kind of picture, because right now I don't. I don't have good visibility into how anybody's using this. So.
**Andy Keller** 09:45 Yeah. Yeah. Totally.
**Evan Bradley** 09:46 Yeah, knowing, kind of.
**Andy Keller** 09:48 Yeah, they're also.
**Evan Bradley** 09:49 Pattern helps inform.
**Andy Keller** 09:50 Do know. They're all on cellular connections, too. So the connections.
you know, like the bandwidth is an issue.
So they're they're not psyched about just like omitting a bunch of logs nonstop.
But they do want access to when things go wrong.
or have some at least some observability, you know. So.
**Evan Bradley** 10:15 Right.
**Andy Keller** 10:17 I think it was. I mean, I think also, partly, it's just kind of looking at.
I mean, we could. We can talk about this for a long time, probably. But you know logs versus metrics versus traces. Do you do all 3, you know. Which do you use when and you know how how much. And you know different different consumers are gonna feel differently.
partly depend on their telemetry backends and things like that. So
that's probably, you know, outside the scope of what we need to figure out. But
but they I do know that they were interested in metrics.
And I think.
I think these metrics
probably makes sense, except for maybe health status, I think, is a kind of a weird one.
Don't know if that's the best way to.
Maybe it's fine, and just like those those kinds of things that don't feel like metrics to me.
**dpaasman** 11:31 I could see, like number of config errors, if that's what they mean
with that one. But yeah, health status should be reported with OP-amp and up to the server today.
**Evan Bradley** 11:45 Right.
**dpaasman** 11:45 Interpret.
**Evan Bradley** 11:46 That's a that's kind of another question I have is, do we want to? I mean, obviously, OP. Amp has some things for monitoring the the health of everything. Do we want to double, publish that? Do we defer some of that?
My! My thought was actually health status was all right it, but we do it as like account of collectors, the supervisors managing, and then
as an attribute on that data point, say, what state the collector's in
you know. Think of it like a Kubernetes pod where you you know you have the pods in your your namespace, and then you know whether they're pending, or started, or stopped, or whatever.
and the other 2 do seem like helpful to me on a
you know a broad scale, but I think the the concern I had was more around.
you know, as a if I'm an operator.
and I like the supervisor account like, you know, I send a config right? Supervisor tries to start. It doesn't start up.
you know. I want something that you know comes back to the monitoring system and says, like, you know, this config was was bad, and maybe you know, I think that
of course, you know, if you're an operator working directly in the OP. Amp server like, you know, that's gonna be pretty clear, because that flow is a little bit more synchronous. But maybe if it isn't so synchronous like you have a you know, a system that delivers a nightly update or something.
That's where your monitoring system might come into play there.
And that's where I would see events being more helpful necessarily than metrics. And you know metrics you could just aggregate from the events. I don't know if we double, publish those, or if we just tell people to aggregate them.
But that was kind of my thought.
But yeah, I guess if you guys have, you know, if
if you have thoughts on this, feel free to comment on the issue, and we can, you know, that would contribute to the discussion?
because, you know I can. I can take a look at it from the signal standpoint of you know how I think it would work, but I don't have anything to to point to necessarily here.
but I do think that we should make sure that we're, I guess, thinking about this holistically. I think that's my primary concern is that we're not adding these on piecemeal. But we're really thinking about the whole story of
when somebody's running the supervisor. What
what signals do they expect it to admit? You know we I would, you know, think of like a published document of, you know, like, here's the things the Supervisor admits. And this is how you know. You can make sure that when you're running these things, you know you can.
You feel like you have a good idea of what's going on, and when something goes wrong, you know you have
actionable information in your back end on how to handle it.
**dpaasman** 14:55 Yeah, I'll
I can chime in on this issue for sure.
I'll spend some time thinking about it and evaluating it.
**Evan Bradley** 15:10 Appreciate it. And I don't think we. I mean, we can definitely take this.
You know, this issue is one thing, but like. I do think that we should probably think about. You know, how does this generalize to somewhere? Maybe in the hotel semantic conventions? And maybe the answer is, it doesn't go in there.
**Andy Keller** 15:26 Yeah.
**Evan Bradley** 15:27 But I have a feeling it likely should.
**Andy Keller** 15:34 Yeah, we should always take a look at what's there. And if anything makes sense.
**Evan Bradley** 15:38 I think we'll probably have to define something is my my guess.
But
You know I don't. I don't know what that looks like just yet.
or how you know. How, general, do we want to make that? How specific do we keep it, you know, etc.
**Andy Keller** 16:08 Cool. I just added one
This just kind of came up. I mean, it's come up a bunch of times over the years and came up again recently.
I know Tiger was on board a year or 2 ago of just adding another message. That's basically
a telemetry payload
I haven't thought exactly if it's just byte array, or if it's.
you know, something more specific. But basically
it would be great if you could, for the agents own telemetry. Choose the OP. Amp. Connection as
a route for the telemetry.
So that would involve, you know, basically probably having configuration that
use the OP. Amp extension to emit that data over the connection.
The reasoning is that your management server, and
you know, might be interested in that telemetry, and it you might not want that telemetry flowing to your telemetry back end
particularly because your toll free back end might be
part of the issue with your telemetry, and you're trying to observe your telemetry pipeline.
And you know, if if you're trying to observe the thing that's broken.
you're just gonna know it's broken. So
A lot of times people are setting up different.
Kind of localized like they'll just throw set up a Grafana server or something to.
or Prometheus to to get data from.
They're agents separate from their like main telemetry back end so that they can observe their pipeline
But it would be nice
for management. Servers are interested in this if they could receive this over OP. App without requiring another oclp endpoint and another connection from the agent.
Because you already have a
websocket connections which we're just sending data over it as opposed to
opening a new Http connection and posting it.
So
yeah, a little bit of an issue. But I was just kind of curious while we were talking anybody, any thoughts.
**Evan Bradley** 18:49 I don't have any major thoughts. I mean, I think that makes a lot of sense. You already have this open connection. You might as well use it, especially if you're dealing with a large fleet of things where you know opening a single connection, you know, a hundred 1,000 times is gonna have. It's gonna have additional effects that you have to consider.
I think I would probably favor just making it a byte array and not trying to specialize it too much, because I think it's gonna I wouldn't be surprised if in the future somebody wants to be more than just like Otlp telemetry.
I don't know what that looks like. Maybe they're running an agent. That what do they call those? It does like a you know, a memory dump on crash or something like that, and they want.
**Andy Keller** 19:32 Snd.
**Evan Bradley** 19:33 Over the wire. I can just see it going in the future where people want to send things that aren't Otlp and as opposed to, you know, adding a message on each time. Maybe we just get ahead of that and that, and like, I don't know
what I mean. Maybe if we can think of some really good specializations around Otop. Maybe that would make sense. But I think a byte array would. You know you can easily write a you know, a Protobuff payload, you know, to a byte array and then deserialize it on the other side. So.
**Andy Keller** 20:04 Yeah.
**Evan Bradley** 20:05 Just seems simple.
**Michel Laterman** 20:06 Yeah, I'm also in favor of bite arrays, because one of the things we're doing right now with our current manage one of the features we have
with our current management. Layer is the ability to connect diagnostics, bundles from our agents.
and our agents are written in ghost, so they can just collect P. Profs locally and send them up.
**Andy Keller** 20:30 And that saved us a few times. So just having the ability to.
**Michel Laterman** 20:36 Other ask for or just get, you know, what does my heap look like right now?
**Andy Keller** 20:42 Yeah, that can help a lot in debugging.
That's pretty cool.
That makes sense. I mean, like like, but
th, this could certainly be done with custom messages. But I think if we.
this isn't something that we feel like.
especially if it's going to be built into
own telemetry. Part of the collector using the OP. Amp extension. It feels like it should
use a real message rather than custom message.
But I can also see wanting to like, have some metadata about that byte array what it is. Is it a profile? Is it? Oclp?
So maybe there needs to be a little bit of structure.
**Evan Bradley** 21:27 So I could see it totally looking like,
how we're doing the what do you call it? Like the supported components
that message. I I think it could look a lot like that. You you basically just have, you know,
map of things that include, you know, metadata. And then byte array information. And that's basically the the message. You know. And you can send, you know, X number of Byte arrays that have, you know attributes on them that describe what they are.
I think if I was gonna draft it, that's how I would see it looking.
But no, I agree. Just because I think I think there's value in
I mean, 1st of all, I think that's a good point, like, if the OP Amp extension is, gonna do it like it probably should just be an official message rather than a custom message.
And then secondarily,
if you know, I think we should. I think people are going to want this. They're gonna think, okay, I already have this open connection like, how can I leverage it? And I think just having a capability that says like, you know, here you go, and you don't have to think about it too hard would be valuable.
**Andy Keller** 22:43 Yeah, okay, cool. Well, I'll those are. Those are good thoughts. I'll
I'll put an issue together ready for proposal. And
might even just spike it out using custom messages and see if
I never see any issues but
I do think back to that earlier conversation about that other telemetry proposal was linked to
another OP-amp. Go proposal.
That tiger ended up closing the Pr
because it was really extensive what it was doing
But I have found that the just the kind of
number of messages, frequency of messages, that kind of stuff. Maybe size of messages, would be useful
data coming from the top Hamco library.
Still a little more visibility into what it's actually doing.
You know, we've we found, for example, and I talked to her about this like Ubcon
back in London. But
When you have pods turn over and a bunch of agents reconnect.
they all basically send all of their data again. So all of their.
the agent description, their remote connection status, remote package status. So you know, basically all the messages.
And
you know, it could. Just it can be a lot of data. And we can obviously track that on the server side. But
it could be interesting to emit them in the library as well.
**Evan Bradley** 24:33 Yeah, I think that would make a lot of sense. I think there should already be some kind of I don't know if the semantic conventions include Websockets, but at a minimum they would include
Htp requests. But no, I agree that that seems like an obvious metric to track.
**Andy Keller** 24:52 Yeah.
Okay, cool. I don't have anything else.
**Michel Laterman** 25:01 Got a minor minor concern.
is there any interest in supporting long falling Http connections for those that can't use web sockets?
Oh, she.
**Andy Keller** 25:15 When you say that.
**Michel Laterman** 25:17 And.
**Andy Keller** 25:18 No, I'm it's funny you say that because I
in for my talk I actually talked when I was talking about OP. Amp mentioned that Http was long polling, and Tigger is like it's it's not long polling.
It just keeps reconnecting at an interval.
I I think I don't know if I was trying to figure out.
Is there a difference, you know, if the agent keeps reconnecting on an interval?
You know it's kind of up to the.
**Michel Laterman** 25:50 You eat, you eat a Tls handshake if you're using Tls, and
there are performance implications that differ between the 2.
**Andy Keller** 26:00 Here. But if if the server holds it open.
are you now basically long polling, it's really on the server right to decide whether or not. They want to respond immediately or wait until they're.
**Michel Laterman** 26:11 Yeah.
**Andy Keller** 26:11 Response.
So what would? What would need to change in the OP-amp go library? I guess.
**Michel Laterman** 26:18 I.
**Andy Keller** 26:23 Or is there anything in the spec that we need to change.
**Michel Laterman** 26:25 I think it would be.
You know how there's a heartbeat interval in the OP. Connection, maybe a negotiation board.
If the agent says, you know I want.
I want to try to long pull for 10 min. The server might know that.
Hey? My proxies can't support 10 min. I'm configured for 5.
So it could just respond, no, we're gonna do 5 min.
And that's back to my original point, though it's really on the server.
**Andy Keller** 26:59 To hold that connection open.
The client doesn't really have an option to
hold the connection open for 5 min or 10 min.
**Michel Laterman** 27:06 Sure, is.
**Andy Keller** 27:06 Thing.
**Michel Laterman** 27:07 It might just end up being a spec. Description. Change.
**Andy Keller** 27:12 Yeah. Good.
**Michel Laterman** 27:13 But I think we don't immediately respond to server implementations might orbit of Alarm Pool.
**Andy Keller** 27:22 Yeah. So I guess I'd be curious.
We don't actually support Http right now. We keep talking about it, but nobody nobody. We've talked to cares. And just so
it's it's it's on our roadmap that just isn't hasn't been a high priority.
it does. It does change, you know, as far as the server is concerned, there's a pretty big advantage of being able to preserve a bunch of state on an open Websocket connection versus.
**Michel Laterman** 27:51 Sure.
**Andy Keller** 27:52 You know something that's reaching out
periodically, and you don't know if it's even gonna.
**Michel Laterman** 27:56 Yeah.
**Andy Keller** 27:58 Connect to the same pot or not, and there's, you know, you can set up some affinity and maybe
maybe ensure that. But
anyway. I I think it would be interesting to see if given the current Http implementation, you could
basically do long polling with that. Or if there's something about that implementation. That is
what prevents that. But I think it's really just the server not responding until it decides to.
**Michel Laterman** 28:32 For.
**Andy Keller** 28:33 Yeah, basically.
And then and then, after a certain time out, 5 min, 10 min, whatever
decides, it doesn't have anything to say sends back an empty message, and and then the client can reconnect.
and it really be on the client to, you know, reconnect.
presumably immediately. But I also think that that interval is configurable.
**Michel Laterman** 28:58 No, that's.
**Andy Keller** 28:58 So.
**Michel Laterman** 28:59 Interval.
**Andy Keller** 29:00 Yes, if you set that really low.
and then have the server pull that open for a long time.
you know.
**Michel Laterman** 29:10 Is that one, or is there something missing? Right?
Think it is. But I think
I think just adding a sentence, saying like to the spec saying.
you know the server can can.
Server implementations can support long polling
and hope it can be used for reconnect, or
I'm not sure about wording, but saying.
I think, having it in the spec as like.
It's not just a synchronous connection, or Http would be good.
**Evan Bradley** 29:51 So I think it would still have to be a synchronous connection, wouldn't it? Just because so okay, let's say you. So the the client connects the server server, you know, sends back a message, holds open the connection. Even.
**Michel Laterman** 30:04 Wouldn't.
**Evan Bradley** 30:04 If it sends a message, the client's usually expected to respond.
So like you send it a new config. The client's expected to respond. It's not gonna be able to send another payload over a standard Http request like the server can send.
**Michel Laterman** 30:15 Yeah, no, no, no, it would be
You know the initial connection happens.
Client sends all its state server response client reconnects.
The server has nothing to say right now. So
it's gonna hold that Http connection open. Not send a response or 10 min or so.
Send it empty message Via Http.
and then the client will reconnect with.
**Andy Keller** 30:50 It's increment up, I guess.
**Evan Bradley** 30:53 That's the only change that would happen for her.
**Michel Laterman** 30:57 Message exchanging or the message exchanges.
So instead of every 30 seconds, you get a pulse going
where, in where server and client messages are
just incrementing. It would be every 10 min.
**Evan Bradley** 31:17 Yeah, no, I think I mean, I think that's definitely more of an implementation thing than expecting. But I don't think it would hurt to call out and expect that that's possible. Because I think to Andy's point, it's just a matter of how long the server holds the connection open, because from the client standpoint, right? They're just waiting for a response. You know, whatever the timeline for that is so.
But yeah, I I wouldn't be opposed to the spec, saying, like, you know, note, if you want to implement long polling. This is.
**Michel Laterman** 31:44 I mean, it's there's also you also need to.
If you're doing Http requests, then
you might also have to configure your Http client with a larger timeline for the request.
Right? So if you're assuming my heartbeat is 30 seconds my request should take.
I don't know a minute.
You don't want your clients starting to time out. If the server thinks I support 10 min long.
**Evan Bradley** 32:21 Right
**Andy Keller** 32:24 Oh, here's here's is an interesting detail I hadn't considered. It is in the spec.
So this is in the plain Http transport description.
**Michel Laterman** 32:35 Yep.
**Andy Keller** 32:37 and it says, when the agent wants to send a message to the server, and the agent has previously sent a request to the server that has not yet responded client must wait until the response is received before a new request is made.
**Michel Laterman** 32:49 Okay.
**Andy Keller** 32:50 Notes. It's a new request in this case
can be made immediately after the previous responses received. The client does not need to wait for the polling period between requests.
So that is interesting. So the problem with long polling really is that this is bi-directional communication
and long pulling kind of assumes that you're you've got a clients that are like subscribing to information that the server is pushing, but the client may need to send information.
So if the server is holding that connection open for 10 min and not responding.
The client won't be able to send anything for 10 min, either.
That's where I think it could be an issue.
Unless the unless there's maybe some mechanism where the client closes the connection
and then sends the message immediately, not waiting for a response from the server.
That make sense.
**Michel Laterman** 33:46 Yeah, yeah, no, that's that.
If that's a mechanism, then we would need to
account for it. And implementations are on the script or in the spec at least.
**Andy Keller** 33:59 Yeah.
Well, I'm open to ideas here.
**Michel Laterman** 34:03 Yup!
**Andy Keller** 34:03 So think about what you, what you need, and and.
**Michel Laterman** 34:08 You know.
**Andy Keller** 34:08 If if if it's feasible.
I hadn't really considered.
you know, the bi-directional nature of it, and how the client may need to suddenly send messages, and and if it's just already sent a message and waiting for response, it's gonna have to delay and that might not be desirable.
I think anytime the server institutes a delay. It's then gonna it's gonna block client messages.
So you're kind of stuck with latency
on either side of it right?
and and really the might, the the best thing might just have
be to have a a pretty short heartbeat interval. If you really want to reduce latency.
But then that's gonna be at the cost of a lot of.
**Michel Laterman** 35:00 Yeah, but I mean.
**Andy Keller** 35:04 Like you can get. You could reduce server latency by having the server open the connection.
But now you've introduced client latency.
unless, like I said. The client closes the connection and and reopens it immediately.
but then it's kind of cancelling anything the server might have been doing, or something so
alright. Well, let me know. Let me know what you come up with. Happy to discuss it some more.
**Michel Laterman** 35:34 Yeah, it's that definitely needs to be discussed in an issue.
**Andy Keller** 35:42 But and, by the way, I want to mention where or ask you where, what's the status of your various prs, I'm I'm ready to.
Take a look again.
**Michel Laterman** 35:51 Think the connection settings one is ready for review proxies. I haven't
haven't looked into swapping out the
Websocket Library yet, and the gorilla web.
**Andy Keller** 36:10 Right.
**Michel Laterman** 36:10 It.
The Maintainer is not very responsive right now, so
I'll have time in the next couple of weeks to actually look into investigating other Websocket libraries.
**Andy Keller** 36:26 Okay.
Well, just hit me up if you want me to look at something. I I just noticed this connection. Settings status is still in draft, so.
**Michel Laterman** 36:37 Yeah, I I never know when the toggle it off drop, because
right now that Pr is linked to
my branch of the spec, and not a released version.
Right? So.
**Andy Keller** 36:54 I see. So we need to merge. The spec needs to be merged first.st
**Michel Laterman** 36:57 Yeah.
Oh, one. The spec.
**Andy Keller** 37:05 Okay, we'll see she here and says, Let's keep it open until we're happy with 3 90
so.
**Michel Laterman** 37:15 Yeah, I mean, I can add more unit tests if we want higher coverage. But
I think all the comments on the implementation are being addressed.
**Andy Keller** 37:25 Okay.
I think if you think it's ready to go, then that's fine, I'll just
We all know. Usually when I see something in draft. It means that you're still working on it and aren't ready for review.
**Michel Laterman** 37:42 Okay, yeah, I.
**Andy Keller** 37:44 That's just my personal interpretation. A lot of people have different workflows and and and do things differently. But
that's helpful. I will take another look at it and and then we can merge this back.
**Michel Laterman** 37:57 I'll start calling out in my OP. Go, prs, that this is in draft because.
**Andy Keller** 38:04 What's that?
**Michel Laterman** 38:04 The spec change hasn't been released.
**Andy Keller** 38:07 Yeah. Okay. Sounds. Great.
**Michel Laterman** 38:08 Nope.
**Andy Keller** 38:10 Alright, anything else.
**Michel Laterman** 38:13 Sure Nope.
**Andy Keller** 38:17 Cool.
Alright. See? You guys.
**Evan Bradley** 38:22 Yep.
See you, everybody.
