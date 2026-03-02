SIG: Agent Management WG
Date: 2025-09-03
Duration: 27 minutes
============================================================

## Zoom Recording Transcript

**dpaasman** 00:25 Alright, Michael.
**Michel Laterman** 00:29 Yay.
**dpaasman** 00:31 How you doing?
**Michel Laterman** 00:34 Pickles?
**dpaasman** 00:36 What was that?
**Michel Laterman** 00:37 I'm alright, how are you?
**dpaasman** 00:39 I'm doing good. Doing good.
**Evan Bradley** 01:02 Hey, everybody.
**dpaasman** 01:06 Hello.
**Tigran Najaryan** 02:09 I think we can start.
Although, Andy is typing in the document, but he's not… okay, he's right.
I am.
**dpaasman** 02:24 -Oh.
**Andy Keller** 02:26 I had a problem joining for some reason?
But…
**Tigran Najaryan** 02:32 Here, I saw you typing in the document.
Okay, you wanna go ahead, Takoda?
**dpaasman** 02:41 Yeah.
Yeah, so… I have a couple of items.
So the first one, we noticed something,
It feels like a bug, but there's nothing explicit in the spec.
that addresses this. So, basically what we're seeing is, right now, the supervisor only responds to a remote config message from the server if it decides to either apply that config, or renderings and evaluating the config fails.
So something we're seeing is if…
The hash of the config changes.
But…
Functionally, the config is still equivalent, and that can be done easily by just rearranging the order that components are defined. That changes the hash, but the supervisor will evaluate it.
as the same config. In the event that that happens, the supervisor just ignores the remote config message. It doesn't send any sort of new status back to the server.
About, like, whether or not it's applying it or failing it.
You know, obviously, in this case, it doesn't do anything, because it's the same config.
So… yeah. We think… The supervisor should be sending some sort of status back.
So I was working on an issue for it, but… yeah, like I said, the spec itself, the opium spec, doesn't explicitly say that.
So, not really sure… What the group thinks about that.
**Andy Keller** 04:32 Dakota and I discussed this for a while this morning. We proposed that we bring it up today, and
You know… Basically, because the hash is different, it would be great if they…
The supervisor responded and said, I'm using this hash.
**Tigran Najaryan** 04:48 Yeah, I agree. I think it should indicate somehow, acknowledge the fact that it did receive and did something with the config. I think the question is, what exactly should respond? Is it just that applied status, or something else which is…
no op or some… whatever, right? Is it the same subjects or different?
But I think it should say something, right? Respond with something.
**Evan Bradley** 05:12 I think applied is okay. Even if it doesn't necessarily restart the collector, I think that's an implementation detail from the service perspective. All it wants to know is, is the…
agent running this configuration, and from the supervisor's standpoint, the answer's yes. Like, if it's just rearranged, and it's just, you know, it ends up being functionally equivalent, then yes, it's already running it, it's applied with this, you know, this hash is applied in the agent.
From a spec standpoint.
I… I would be okay putting, like, a should in there. I mean, it seems like a good, you know, neighborly thing to do. Like, you know, you'd want… you'd prefer to know this, but I'm… I'm reluctant to make it a must.
**Andy Keller** 05:54 So my concern is how you end up
kind of closing the loop on this. If the server tells the agent to do something, Edit.
doesn't say anything. You know, should the server try again after 10 seconds? Should it…
just assume that it's doing it, even though it hasn't responded, you know, it's… it's… I think it…
You know, I was trying to think of…
Messages that don't require a response from the agent. You know, I…
I definitely think, I would expect…
A remote configuration message to return a remote configuration status, even if it's…
Even if I pass the same hash, And the same config.
And it could just tell me it's applied it. You know, maybe that's an error in the implementation of the server that shouldn't do that if the remote config status already says that it's running that, but…
But it still feels like appropriate behavior for the… Agent to respond.
With the status.
**Tigran Najaryan** 07:01 Why are you concerned with a must close, Evan? What's the problem with that?
**Evan Bradley** 07:06 Well, I guess to Andy's point,
like, I think, yeah, you should get a response even for, you know, just… each message should, I think, in general, give a response. I guess my concern is if…
you… and I don't know that I have an explicit issue with the must, I just haven't thought it through. But my… I guess my question would be, how do you handle, like, error conditions or the fact… I mean, I guess, fundamentally, this is an asynchronous network call, right? So, I think I… would want to make sure that we have the…
the failure cases specified as well, if we do make it a must. So, the server sends a message, and it doesn't get anything back, you know, that could be it was lost, or it just hasn't been sent yet. And…
I…
just how do we spec… what's the… what's the expected behavior in those scenarios? Do we… And can we specify that at the spec level, or do we have to kind of bake, you know, failure expectations into the spec and say, like, if you don't get anything back, then, you know, it's kind of up to you to negotiate what's due next?
**Tigran Najaryan** 08:11 That's a good point, and the server normally would have some liveliness expectation from the agent, right? When it expects to receive something and doesn't.
it can make sort of a… a conclusion can be that it's dead, right? It's not live anymore.
And it should apply universally to all of the expected responses, not just in this case. I don't know if we say that in the spec anywhere, but…
I would expect that if the spec says the agent must do something, must send a response to a message, that that would be the reason why it's a must, so that
The server can reliably know that if it doesn't arrive.
then something is actually wrong with the agent. It's not live anymore.
**Evan Bradley** 09:02 So, my question to that then would be, okay, so I send the remote config, I don't get anything back, I send a ping, and I do get something back. I never get back the remote config message.
What… what's the current state of the agent in this case?
**Tigran Najaryan** 09:17 Which would be an indication that the implementation is incorrect, right? So the agent is misbehaving, essentially. It's not responding to something it should, but it's responding to something else.
So, it's, yeah, it's a bug, maybe it's fine, and that's the server's choice what to do about that, right?
**Evan Bradley** 09:36 Right,
Okay. I mean, I can… I can see this… just because it's a network call, I can see it happening at, like, the network layer, too. I guess I'm just…
**Tigran Najaryan** 09:46 Well, you're actually… you're actually quite correct about that. If we… if we're talking about the HTTP transport, not the WebSocket one.
There is no guarantee that one of the agent messages won't be lost, for whatever reason.
And the subsequent ones are actually delivered, so you may not get the response to the remote config.
The status may be lost, but…
all the subsequent agent messages are actually delivered properly, and we don't do…
We don't do retries, as far as I know.
From the agent side, right? For the statuses.
The… the server can ask for the full report?
If it wants to.
But… Unless it does that.
that's the one shot the agent has to deliver that message. If it's also closed, right?
So, I think…
I think it's fine to say that it's a must for the agent, but the general wording that you're bringing up, Evan, applies anyway, right? The server needs to know, needs to understand that, yes, this is a network call. It may be lost.
**Evan Bradley** 11:04 I think… so, and you would know better than this than I would, I haven't done a whole lot of spec work, but,
The must, if… okay, so we say that's a must, and the server doesn't get that message, are we…
I mean, can we assume a… a graceful failure mode? Well, I mean, I guess you would always want graceful failure, right? I guess my only concern is if we say it's a must, and the server doesn't get it, that your implementation
Make certain assumptions that the protocol is now, violated in some way that requires more drastic actions than it would if it were or should.
I don't mind saying a… a must in principle, just because I agree, like, you should just get a response back for every message you send.
I… I think we just… I am wondering how we can word that so that the failure case, it's understood that it could be a faulty network connection at play.
**Tigran Najaryan** 12:00 Yeah, yeah.
**Andy Keller** 12:01 Well, I think… I think that it's… it's a must, you must send the message. It doesn't… it isn't saying it must be received by the other side, you know? It isn't… it isn't implying that.
**Michel Laterman** 12:09 You know.
**Andy Keller** 12:11 There's some guarantee there.
**Michel Laterman** 12:13 Yeah, and I think we have a section in the spec which…
**Tigran Najaryan** 12:16 Which says, not for this particular message, but for other status updates, it says that.
**Michel Laterman** 12:22 X.
**Tigran Najaryan** 12:22 They may be lost, and the server has a way to ask the agent to send the full report.
I think it can apply to this one as well.
**Evan Bradley** 12:31 Right.
**Tigran Najaryan** 12:32 So, maybe a disclaimer in this part? Refer to that other section?
But otherwise, I think it's okay. So, must send doesn't mean it's guaranteed to be delivered, right?
**Evan Bradley** 12:45 Right, no, that's fair. I guess what I… the standpoint I'm coming from is sometimes when dealing with things like OTLP and the collector, we say, like, okay, this is an invalid state, you know, like, you don't have to address this, and I just want to make sure that we don't end up there from the server's end in this situation.
**Andy Keller** 13:02 Yeah, I think what we're trying to clarify is that this is a bug in the supervisor, that it's effectively a non-compliant
op-amp implementation. It's just…
non-compliant with the future state of the spec that we are correcting. But, you know, we need to… we need to explicitly call out that this… this behavior is not desired, because it…
it causes problems, you know? Particularly in this case, because it doesn't update the remote config status, it never reports the new hash.
The server keeps trying to send the new hash, and you just… it's never gonna get resolved, because the supervisor's gonna just throw away
those messages. So, so we definitely want to fix the bug, but I think it's… it's right to also tweak the spec to… to identify it as…
**Evan Bradley** 13:49 I was not compliant.
**Tigran Najaryan** 13:51 Yeah, yeah, I agree. Let's open the PR to fix it, and we can discuss the should versus must.
on the PR itself more.
**dpaasman** 13:59 Yep.
One other thing I'm thinking about, I don't want to open this can of worms, but…
Does it make sense to also add a new status rejected for the remote config status? Because right now we have applied.
Applying and failed. And in the spec, it does say the agent may ignore the remote config offer if it does not want its configuration remotely controlled by the server.
So I feel like, would it make sense? Is there value in adding rejected?
To differentiate that between, like.
Like, we just are ignoring this because we don't want to use this remote config versus, like, we failed to use Remote Config.
**Evan Bradley** 14:38 I think that there is motivation for rejected. I think the one concern I would have there is I'm not sure where we would use that right now.
**dpaasman** 14:48 True.
**Evan Bradley** 14:49 But in general, yeah, I agree. I think that there should be something for the agent to say, this wasn't a failure, this was explicitly disallowed, and for the operator to make a decision based on that.
**Tigran Najaryan** 15:00 What… what does… What is the purpose of…
having that distinction from the server perspective, what… what would server do differently when it receives failed versus rejects it?
**dpaasman** 15:13 I think… In the case of failed.
you know, it doesn't necessarily know why it failed. Maybe it tries again, or maybe it…
**Tigran Najaryan** 15:22 There's an error message for that, right? There's a… there's a…
**dpaasman** 15:25 Dude.
**Tigran Najaryan** 15:25 With an error message.
**dpaasman** 15:27 There is, yeah, but I think…
Having a rejected status makes it more clear to the server that it shouldn't try this again, because the config is not being
The agent doesn't want its config managed by the server. It makes that clear, rather than needing to parse that error message and determine that.
**Tigran Najaryan** 15:49 So, what you're describing is retryable versus non-retryable situation, essentially.
**dpaasman** 15:56 I guess, yeah.
**Tigran Najaryan** 15:57 that…
That would be the difference between these two states. The problem I have with that is that it's not always possible to know the reason for the failure.
**Michel Laterman** 16:08 Hi, sweetie.
**Tigran Najaryan** 16:09 for the… I guess you couldn't write a file. Is that because… what is it, a failure? That the permissions are the problem? Is it temporary?
Is it Tribal?
It's a bit… it's a bit hard to have that distinction from the… from the reporting side, to… to clearly
Understand the reasons for the failure and provide the right state there.
So… I don't know if the supervisor can do that cleanly, right? Trying to apply the config.
Something goes wrong there.
What do you put there? Is it, like, the file can't be written? Is it a rejection, or it's a failure?
**Evan Bradley** 16:49 I would call that one a failure. I would say that the rejected would be, something along the lines of, I know we haven't made any, we really haven't touched on this in a while, but,
In the specification, there's an outline for the ability to restrict
Like, which files the collector can read, for example.
I would say that if one of those is detected in the config, that would be motivation for a rejected message.
Like, the supervisor has made a decision versus it tried to start the collector and something happened.
**Tigran Najaryan** 17:28 Well, and that's a… that's a permanent problem. It shouldn't be retried.
**Evan Bradley** 17:34 I would say… I mean, that's a… I would say so. I would say that that's a, you would send a rejected response when a policy decision prevents the supervisor from running something, or…
There's some other explicit setting that we can statically confirm.
Is, and is causing this config not to be applied.
**Tigran Najaryan** 17:58 Yeah.
Okay. I guess…
I guess I would want it to be described in those terms, right? Whether it's a retribal failure or a non-retribal one, versus saying it's a failure
Or a rejection, because it's not entirely clear to me, right? Whether… or I rejected it, but…
Because that's… that's what makes a difference from the server's perspective, right? That's where the server may decide to behave differently.
For a permanent one, don't retry anymore. If it's a retryable, the server in a while may send the same config again.
That's what… The server, in the end, cares about, right?
Another Bob.
Some sort of, whether it's philosophically rejected or failed because of a technical reason.
**Evan Bradley** 18:50 So, I see the value in that. I guess from… for… I think what Dakota's trying to propose, though, is more from the operator's standpoint, trying to make the…
the reasoning more clear? Like, is this a technical problem I need to solve, or is this more of a…
Like, something that I have misconfigured, so to speak.
**Tigran Najaryan** 19:08 Yeah, and I think for that, we have the error message, right? Put the reasoning there, why that is happening, for the operator to read and understand what went wrong. For the
for the, I guess, for the automated response to that, you don't want to rely on the message. You want the server to look at some
enumeration and make a decision about how to proceed, so I understand why the…
Human-readable error message is not enough for that.
But for operators, I think that's fine, right? You can say whatever you want, put whatever you want there. The file is not readable, there's a restriction, etc, whatever.
**dpaasman** 19:48 Okay.
Cool.
**Tigran Najaryan** 19:51 but still try to frame it in terms of retryable versus non-retribiable. And we have something similar
you know, TLP failures, I think, as well? Yeah. We had something, and that's the same terminology we use retrieval errors versus non-retribable ones.
**dpaasman** 20:15 I'll, yeah, so I have the one issue.
about the spec terminology, and I think I'll make this one a different one, but… Related through this.
The idea of having a retribal versus non-retribal area?
Cool.
The second issue I have, and Tigran, I saw you edit these issues, those were helpful. I had not found that first one. It was kind of being discussed between you and Dan about
How to do this.
So… Some background here, we've got a user.
We think their WebSocket connection is getting,
It's basically going stale, but, like, not totally. The server can't… doesn't realize it's stale.
So I was just kind of looking into heartbeats, and this idea of just sending an empty op-amp message over
the connection. I was looking at the Gorilla WebSocket library, which is what's being used.
They have a specific pattern.
It's in the WebSocket spec as well. It's this ping-pong pattern. I was just wondering if…
there is any discussion done at the time of heartbeats about implementing this, and if this is something
We see value in.
And then Tigran, you responded with that issue. Looks like it was discussed, but not included in the…
implementation we got for Heartbeats last year, so… I guess, yeah.
**Tigran Najaryan** 21:54 I think it was discussed, I'm not…
I'm probably forgetting the details, but it's in the very first issue.
Yeah. It's there, so I think we must have discussed it, but I don't know if, Andy, maybe you remember what was the discussion like?
**Andy Keller** 22:10 I don't remember, and I told Dakota to ask when we had our meeting later, so… We talked about this this morning as well, so… Okay.
**Tigran Najaryan** 22:19 But since we already have that capability there, it should solve the particular problem you have, right? And I don't think we need two different mechanisms for maintaining the effectiveness of a connection.
Would… are you looking at… The ping pong as an additional…
**dpaasman** 22:40 Yeah, just because right now…
Heartbeats only work as, like, we can send a message across the connection. It's not validating that we can also receive something.
So, the ping pong would allow us to send the message, and then we were sitting there waiting to get a message back.
And then when we don't get that message back after some interval, that's when we'll terminate the connection. But right now, as long as we can just send a message, we think the connection's fine.
So, that's… that's the value I see on adding a ping pong.
**Tigran Najaryan** 23:14 So… don't we have any requirements for the server to respond to the heartbeat in any form?
**dpaasman** 23:22 No.
Not… not that I saw. Maybe I missed something.
Yeah, maybe I missed something, but it looks like it's just sending a message across the…
**Tigran Najaryan** 23:33 Yeah.
**dpaasman** 23:34 connection, that's all the heartbeat is doing. The server doesn't have to respond.
**Tigran Najaryan** 23:37 That's just for the server to know the agent is alive, not the other way.
So it's… One-way heartbeat, essentially.
**dpaasman** 23:47 Yeah.
Well, so there's…
It's client-initiated, so it's really just the client keeping the connection open, is what's going on. We're configuring the client to send the heartbeat, just to keep the connection open. The server isn't really…
Doing anything with that heartbeat message.
Again, I… Maybe I missed something small about it, but… you know.
It's kind of what I was looking at 20 minutes ago and what I saw.
**Tigran Najaryan** 24:22 Yeah, I think you're right, I'm reading the spec, I don't see anywhere…
A requirement for the server to respond to that.
**dpaasman** 24:30 Yeah.
**Tigran Najaryan** 24:32 Okay, so what you need is essentially detection in the opposite direction for the agent to know that the connection
went wrong, for whatever reason, essentially. And what we have doesn't help with that.
**dpaasman** 24:46 Yeah, basically, right now, we have…
ping, you know, we're sending a ping message, but we're not receiving a pong.
**Tigran Najaryan** 24:52 Yeah, yeah.
Okay.
I think we should look at the possible options here. One is adding that ping pong, the other is requiring a response to the heartbeat from the server.
And… I think, since we already have that as a heartbeat message.
It makes a little more sense to me to just require a response, rather than adding another mechanism.
**dpaasman** 25:22 It's the ping pong thing.
**Tigran Najaryan** 25:24 Sure, yeah.
But let's maybe open a discussion, maybe let's think a bit about it, but that's my initial reaction.
**dpaasman** 25:34 Yeah, no, that sounds good to me.
Cool.
Oh…
**Tigran Najaryan** 25:41 Because if we have both, then it's unclear how they interact together, right?
**dpaasman** 25:47 Yeah.
**Tigran Najaryan** 25:47 Are they on the same interval? Do you see… Bye.
And it's a bit weird, why do you have two different mechanisms for heartbeating, also?
**dpaasman** 25:56 Yeah. No, that makes sense.
**Tigran Najaryan** 25:59 Is there…
Is the… is it client-initiated only in WebSockets, or the server can initiate a ping-pong as well? Is it symmetrical?
**dpaasman** 26:09 Yes, I understand it, it can go either way.
So, right now in op-amp, we just have client-initiated heartbeats.
**Tigran Najaryan** 26:16 Yeah.
**dpaasman** 26:16 So…
And I, yeah, I know in bind plan, before bind-initiated heartbeats were a thing, we had our own implementation for server-initiated heartbeats.
Which was identical, we were just sending an empty op-amp message.
Again, just doing a ping, there's no ping pong.
So yeah, I'll open up an issue.
**Tigran Najaryan** 26:41 Okay.
**dpaasman** 26:42 To discuss it more?
Get an implementation going.
Cool. That's, that's all I had.
**Tigran Najaryan** 26:53 Okay.
That's all we have in the agenda.
Does anybody have anything else they want to talk about?
Okay.
Thank you all.
somewhere.
**Andy Keller** 27:11 Cheap.
