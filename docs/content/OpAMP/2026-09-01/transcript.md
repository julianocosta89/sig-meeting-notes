SIG: OpAMP
Date: 2026-09-01
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Tigran Najaryan (Splunk Inc.)** 00:29 Hi, Andy.
**Andy Keller** 00:32 Tigran, welcome back!
**Tigran Najaryan (Splunk Inc.)** 00:34 Thank you.
How are you?
**Andy Keller** 00:38 I'm great.
How are you?
**Tigran Najaryan (Splunk Inc.)** 00:42 I'm good.
A bit of a sore throat, Bob.
Great, otherwise.
That good modification.
**Evan Bradley** 00:52 Hi, everyone.
**Tigran Najaryan (Splunk Inc.)** 00:53 Hey, hey guys.
You guys… Andy, maybe you can drive the call? I don't want to stick.
**Andy Keller** 01:00 Yeah, happy to.
**Tigran Najaryan (Splunk Inc.)** 01:01 Thank you.
**Andy Keller** 01:03 I just want to speak for a few more people.
Okay, we can probably get started.
First thing on the agenda, I just added this yesterday, I noticed, looking through PRs, that we've got a bunch of CI changes, Trask added a bunch of them from, like, 2 weeks, 2 or 3 weeks ago, refactoring of some of the CI process.
And some security checks.
And then a bunch of renovate.
PRs, I was going to just start merging… approving them and merging them, but I figured I… since we had the meeting today, I would just, Bring it up before doing that, if anybody… Any concerns?
**Tigran Najaryan (Splunk Inc.)** 03:01 No, we should do it. I already merged a couple of those, the scorecard ones, but yes, we have a bunch more.
**Andy Keller** 03:08 Okay.
Great.
Yeah, that's all I had, Dakota.
**Dakota** 03:15 Yeah, so it's been a little bit, but the… changes for Unix domain socket support, as well as Windows Namepipes. The changes needed for the supervisor, the extension, and the OpAMPO library are all up and ready for review.
So yeah, no, just… Radiating that and asking if anyone has a chance to take a look at it.
Greatly appreciate it.
the OpAMP GO PR is probably… Most important, since right now the… extension and supervisor are replacing to this PR, so it'd be great to get that merged and cut a new release of it and update that dependency.
and the extension supervisor. Yeah.
**Tigran Najaryan (Splunk Inc.)** 04:11 You mean 642 or 643? Which one? The flaky test?
just the UDS.
**Dakota** 04:17 4-2.
642. Yeah, the other one was just… I ran into while running CI for… 642.
**Tigran Najaryan (Splunk Inc.)** 04:28 We're adding domain socket support to the collector, that one is being blocked by the OpAMP call? Is that what you're saying?
**Dakota** 04:36 Yes, yeah.
**Tigran Najaryan (Splunk Inc.)** 04:37 Okay, got it, okay.
**Dakota** 04:43 Yeah.
Stanley, looks like you're… you're next.
**Stanley Liu** 04:49 Yeah, thanks.
Yeah, I just wanted to follow up to ask if there are any updates for the current status reviews for the message attestation proposal and prototype.
Just, I was wondering, like, if there's any parts of the proposal that you guys might be uncomfortable about, or if there's any blockers or questions. I'd be happy to, like, schedule a call if that's easier, or just discuss things in general.
**Andy Keller** 05:17 Thanks, Stanley. I, go ahead, Tigran.
**Tigran Najaryan (Splunk Inc.)** 05:21 No, no, no, I was just saying, I did take a look at the PR. I'm fine with the API as it is. We probably need to take a closer look at the implementation details, but first, I wanted to make sure you, Andy, and Evan you guys are happy with the API before we move forward. If you're fine, then we can go a step farther and do a more detailed review.
**Andy Keller** 05:48 I've… I've looked at it, you know, probably spent a half hour to an hour about I've heard it 6 times over the past week or two, just as I've had time to look at it, and sorry, I haven't had a big block of time available to really dig in.
I did have a couple small, clarification points that I will get into comments, on the spec.
I would like… to, There's some language in there about you know, doing the heartbeat, like, allowing unsigned messages as a future thing, I'd like to allow that right now.
Possibly, you know, some criteria for that, so either an empty message, which would be a server-side heartbeat.
Or if there's other messages we want to allow to be unsigned, I don't, you know, I think the most critical thing would be config and packages that you would want signed, but I could… I could also imagine saying everything should be signed except for heartbeat, so I want to give that a little more thought, just make sure.
Because the current behavior is… is to… if you see an unsigned message, to disconnect, and I think that's fairly harsh and could… could really lead to… to problems.
So… So definitely, I'd like to make that change for heartbeats, and then, I raised my concern with you, in Slack about, the OpAMP gateway. I know that's a fairly new component, and it's not broadly used, but we would like to contribute it upstream when people, you know, if and when people are interested, and we definitely You know, wouldn't want to add… you know, I don't… I don't wanna… Add this and break that, you know, even though, That's not sort of a standard component, so… I just want to make sure. I think, I think there was a minor issue about, possibly the DNS name, there's, like, a workaround, possibly, that we could use to allow that, signing to pass through the gateway, and then I know the gateway currently Has to create… or modify a message or two for custom capabilities, and so I want to revisit that to understand If that's required, if that's one of those cases where maybe we can allow a message to not be signed, or exactly what, needs to happen there. So, yeah, sorry, I don't, I… I… I don't wanna, just rubber stamp this, because I think it's a pretty significant change, but I also… I know you've been waiting a while, and I apologize for the slow process on this. It's just a… it's a… it's a big change, and I want to make sure we get it right.
**Stanley Liu** 08:58 Yeah, definitely. Yeah, thanks again for the reviews, and I appreciate all the help. I totally understand, also, there's, like, been delays with, like, just scheduling and, like, workloads, so… But would you say that the concerns on your end are, like, things that might block including… block it from being included in V1, or the 1.0?
**Andy Keller** 09:19 I don't think so, no.
**Stanley Liu** 09:21 No.
**Andy Keller** 09:21 I'm happy to say that we can get this into 1.0. It's just a, you know, that then raises the question of when is 1.0, but… Yeah.
But I, I'm… I'm happy to commit to that. I just… I just want to make sure we get it.
Let me get it right.
Because any, you know, vagueness or, I also had Claude take a look at it, and it claimed that there was something, I want to look further at what it said, but, that there were parts of the spec that… conflicted each other, so, obviously we don't want that, so I just wanna… I just wanna make sure it's… it's tight, and My cursory look of the sample implementation looks… looks good. So mostly… I'm concerned about the spec, and then obviously the implications, like I mentioned, on… Performance with heartbeats, and because, you know, a million agents doing that every 10 seconds is a lot, and if it's not necessary, then let's… let's not do it, so… And then the OpAMP gateway.
**Tigran Najaryan (Splunk Inc.)** 10:29 Andy, can you clarify that piece with a heartbeat? So you're saying after the… after the upgrade to use AutoStation.
you would still allow some messages, particularly the outbeats, to be on-site, right? That's what you're saying.
**Andy Keller** 10:46 Right.
**Tigran Najaryan (Splunk Inc.)** 10:46 a mix of…
**Andy Keller** 10:47 And just clarify that in the spec, that…
**Tigran Najaryan (Splunk Inc.)** 10:49 There will be a mix of signed and unsigned messages on the.
**Andy Keller** 10:52 Exactly.
**Tigran Najaryan (Splunk Inc.)** 10:54 you… I guess… the… The bit that we need to be careful about is to precisely define which messages are allowed, because otherwise… If something goes wrong, you may accidentally accept an unsigned message unintentionally, right?
**Andy Keller** 11:12 Absolutely, and
**Tigran Najaryan (Splunk Inc.)** 11:13 you shouldn't be. So it has to be very narrowly defined, what exactly…
**Andy Keller** 11:17 Absolutely.
**Tigran Najaryan (Splunk Inc.)** 11:18 criteria for the acceptance. And the heartbeats, I think.
We define heartbeats as… as, I think as an agent-to-server message that has only the instance ID set, or something like that, otherwise everything being empty.
**Andy Keller** 11:33 There's also server-side heartbeats that,
**Tigran Najaryan (Splunk Inc.)** 11:36 And the, yeah, the.
**Andy Keller** 11:37 Yeah, but it's the same idea, though, it's… it's… but again, I want to make sure we have that language correct, so…
**Tigran Najaryan (Splunk Inc.)** 11:44 We have to, yes, that language has to be there.
**Andy Keller** 11:46 It has to be very precise. Totally agree.
**Tigran Najaryan (Splunk Inc.)** 11:48 What is… what is… allow it to be there? Because… If we say that the fields should be onset.
How does that work if there is… fields added in the future, let's say, for example, is the… What does… how does that work in… in a… in a mode where… you have an agent that doesn't understand the new fields, and they are present, are they ignorable? So there's a bit of a… We need to be careful about how we go about that.
**Andy Keller** 12:16 Yeah, that's a really good point about future proofing, what's… what's allowed unsigned.
**Stanley Liu** 12:25 Yeah, definitely. Thanks for the input, that makes a lot of sense. Do you, would you prefer if I… because we kind of have those two threads where, unsigned heartbeat messages and then the DNS name fix, should I just go ahead and implement those, or should I wait for, your comments?
**Andy Keller** 12:45 I was going to take a stab at what I think the allowed to be unsigned, should look like, but if… if you beat me to it and have a proposal, I'm open to that as well. I will try to look at it again this week.
**Stanley Liu** 13:00 Okay, thanks.
Cool. Yeah, I think that's all I had, but, if there's anything that's, like, more difficult to address over Slack, just feel free to let me know, I can schedule something, so… But yeah, thanks again for the help.
**Tigran Najaryan (Splunk Inc.)** 13:14 Andy, are you otherwise happy with the… with the public API changes in the prototype?
all of this.
**Andy Keller** 13:24 I think so, let me…
**Tigran Najaryan (Splunk Inc.)** 13:25 is down, the start settings and all that stuff.
**Andy Keller** 13:28 Yeah.
**Tigran Najaryan (Splunk Inc.)** 13:29 as well, because I think it's important that we get.
**Andy Keller** 13:31 Yes.
**Tigran Najaryan (Splunk Inc.)** 13:31 Right, as well.
**Andy Keller** 13:33 Yep.
Nope.
Anything else on this topic?
**Stanley Liu** 13:47 Nope.
**Andy Keller** 13:53 Okay.
Kelsey.
**Kelsey Ma** 13:56 Yeah, so I know this is a little early to start bringing up, because we're still working on a top-level package support in the supervisor, but I was just starting to think about, like, what would be considered add-on packages, that… the supervisor, my support, specifically for the collector, because I know there's been a move to… to not have the collector run, like, subprocesses. So, for example, like, the JMX receiver was recently deprecated, and I think fully deleted, in… in… and then instead, you're supposed to use this, like, JMX metric scraper, which runs, like, a jar separately, so, I'm wondering if those would be considered, then, like, add-on packages that the supervisor might be responsible for managing? Like, as… They move more and more stuff like that, outside of the collector.
**Tigran Najaryan (Splunk Inc.)** 14:52 This was… this was the… the idea was that you would have some sort of a dynamic plug-in system, maybe, for your agent, like some of the other agents do, like, I think Fluent Pitas or Fluent DDoS.
We don't have them in the collector. We just… we had this on-and-off discussion about having some sort of dynamic plugins for the collector.
We don't have them, so… I think as it stands, there's nothing to manage that way for the collector. We could have something like that in the future, if we ever introduce anything like that.
I don't know if there's any movement on that, maybe Dmitrii can help us, if there is anything happening there.
From the supervisor… yeah, from supervisor perspective, you could maybe manage something else in addition to the collector and call that an add-on package.
But the intent… the original intent was that it would be something, some component of the collector that It's separately downloadable, installable, is not part of the collector per se, and then you would want to manage it separately.
**Dmitrii Anoshin (Splunk Inc.)** 15:59 So…
**Tigran Najaryan (Splunk Inc.)** 16:00 Meetings.
**Dmitrii Anoshin (Splunk Inc.)** 16:01 So, for the collector, it's, if we introduce some kind of extension framework, like, for example, like, Ruby is being used in FluentD and some something else in FluentBit.
And their approach is to provide some kind of machinery that you write your extension in the… in the interpretable languages.
Which is not ideal from overhead and perspective, and it also… Introduces some, like, limited… framework and limited, contract with those extensions, but we already have OTLP as a, like, pretty good, extension point, I think, so… and if we don't have that framework, we potentially just Can accept anything that can be run as an agent, and can be built in different languages, however user choose, and, like, Java is a pretty good example here. We don't want to introduce some, like.
Limited framework and ask all of those exist in copa… like… agents, like, let's call them agents, like JavaScraper, to be rebuilt, right?
So, it's probably better to have them separately, run on the same box.
And send data over a GLP to the collector.
And here, the problem comes how they're gonna be managed. If we have supervisor for the collector, I think it would be natural to… provide support for those additional plugins through Supervisor as well.
Does that make sense?
**Andy Keller** 17:55 I would say my perspective is just that they're, there hasn't been a… Proposal, or a use case for… packages, aside from upgrading the collector itself, and… but I think that the spec allows for it, and if there's A proposal for… A feature of the supervisor that we think makes sense generically.
Wouldn't be opposed to adding it into the supervisor.
**Dmitrii Anoshin (Splunk Inc.)** 18:28 Okay. Yeah, we can.
We can think about it and maybe come up with some proposal.
**Andy Keller** 18:36 I mean, the supervisor is going to receive that message and needs to know what to do with it, right? So, and… and it… the spec is… Pretty intentionally vague about How these messages are handled to allow… of different… clients to, To treat those packages differently. And even what a package is is… It's not very strictly defined, so… I know we've… we've considered things like, having maybe some enrichment, metadata or something delivered in a file, and would that come via config, or would that come via packages, and… You know, what's the appropriate Mechanism for that, and
**Dmitrii Anoshin (Splunk Inc.)** 19:29 Okay, so from both… Yeah, so from a pump perspective, we are… there is nothing that's blocking us. It's more… mostly on the supervisor side, whether we allow supervisor to handle anything else other than the collector.
**Andy Keller** 19:43 Yeah, we need to state a proposal for what the supervisor should do when it receives this message, and make sure that that proposal is, you know, that everybody's comfortable with that. We feel like it's secure and well-defined and well-behaved and useful, generally.
**Tigran Najaryan (Splunk Inc.)** 19:59 So, actually, there's an interesting bit here at Dmitrii. In the collector, we… we decided we don't want The concept of dynamic plugins, executable by the collector.
**Dmitrii Anoshin (Splunk Inc.)** 20:10 Yes.
**Tigran Najaryan (Splunk Inc.)** 20:10 One of the reasons we didn't want is that it introduces, essentially, a new attack vector in the collector, right? So you execute something, and it can be… It gave me a way for malicious payloads to be executed by the collector.
from the supervisor perspective, that is not a new attack vector. That is already there. It's part of what supervisor already does. Exactly. So, allowing supervisor to execute one more executable in addition to a collector, which is an extension, which is something that then uses, like you said, maybe OTLP transport to communicate to the collector, It's not a new… it's not a new threat in the supervisor. We already have that as part of our threat model in the supervisor. So, I think that's okay to do it there, even though we said no To doing that in the collector itself.
**Dmitrii Anoshin (Splunk Inc.)** 21:08 Yep.
**Tigran Najaryan (Splunk Inc.)** 21:09 That may be… that may be the right approach. We're saying collector is stricter from that perspective. It doesn't do dynamic loading of code, dynamic execution of of arbitrary code there. Supervisor does, because it already does, right? It's not a new thing there.
So, like Andy said, if we… if we settle on… some sort of a definition of what is an add-on from the supervisor perspective, then it's not that complicated to add the management of those additional bits in the supervisor. You can download those, can run them.
without the collector running them, the supervisor can be the thing that runs them, and then those extensions just use OTLP to talk to the collector.
There's maybe nothing even special that you need to do inside the collector, even, because it can then use the regular OTLP receiver to communicate.
**Dmitrii Anoshin (Splunk Inc.)** 22:06 Yes.
Okay, makes sense. Yeah, we'll put something together for the proposal, I guess.
Kelsey…
**Kelsey Ma** 22:23 Oh, yeah, that was it from… from my side, yeah, thanks, sounds good.
**Dmitrii Anoshin (Splunk Inc.)** 22:27 Thank you.
**Andy Keller** 22:31 Okay, Dmitrii, I know in Slack we discussed the… The non-gateway Gateway? Yes.
So there… there's, been a proposal, I don't have a link to the issue.
**Dmitrii Anoshin (Splunk Inc.)** 22:47 I'll… I'll send, I'll send the link to…
**Andy Keller** 22:50 Oh, I just found it. I can… Oops, I pasted it in the wrong spot.
Oh, he's true.
There's a… basically allowing the supervisor to… manage additional downstream collectors. The use case is really… around IoT, and so… I mentioned earlier in the call, the OpAMP Gateway is something that we built, and is… we have in our repo, it's open source, and is really designed for primarily two purposes. One is… To distribute load, so that, downstream collectors can all collect… connect to the gateway, and then the gateway connects upstream. So you have this sort of concentrating Connection path, and then, It also works well in a network where you… the collectors themselves might not be able to reach out to the OpAMP server, but they can connect via the OpAMP gateway, so… This is not that, which is why I said that it's sort of gateway, non-gateway. This use case is much more limited in that, there's probably less than… Less than 10, or maybe even less than 5 downstream collectors, and the idea would in an IoT use case where you are trying to limit the number of outbound websockets and connections to the control plane.
Being able to proxy those through the supervisor, so this would add additional supervisor capability.
I believe there was actually a PR associated with this that was created, I think you closed Tigran And I didn't have a chance to read through the PR, But I know Dmitri reached out to me on Slack independently about this concept, and… I suggested we discuss it.
**Tigran Najaryan (Splunk Inc.)** 25:06 Is this also about concentrating the connections into one, so that you receive multiple WebSocket connections, and then essentially multiplex the messages from all those connections into a single outbound WebSocket connection?
**Andy Keller** 25:22 So the changes required, and my cursory look at that PR was actually pretty similar to what I had in mind.
the changes required would be to allow the supervisor server to accept more than one connection, so… You could have other downstream And downstream, you probably have other supervisors. So, it's sort of a supervisor that manages the collector, and that is connected to a supervisor upstream.
And so that upstream supervisor, just allows And again, the use case is, like, a handful, like, like, you know, 5, maybe 10 at most.
So I don't think there's a lot of concerns about load and scale and things like that. It's not designed for that.
But it allows the supervisor to receive messages from multiple WebSockets, and it still sort of owns the one collector.
But it can… receive messages from other collectors connected to its server. And then the big change, above that would be in the client, which, in the OpAMPGO library, we would need a mechanism to send messages on behalf of a different collector. That's not the… because the OpAMPGO library maintains a lot of client state.
And we wouldn't want to maintain… client state for multiple collectors, we would want the downstream collectors to do that.
That job themselves, so… We would need the ability to basically send messages on behalf, and then receive raw messages that, aren't associated with the, let's call it the primary collector, that would then be forwarded on to the downstream collectors.
**Tigran Najaryan (Splunk Inc.)** 27:16 Yeah, so, we had… I think this requires… a little bit of changes to the spec as well. Some wording is necessary there to explain how this is supposed to work. We had… In the very early drafts of the spec, I had I had that as a section there, but we.
**Andy Keller** 27:34 I remember thinking.
**Tigran Najaryan (Splunk Inc.)** 27:35 may remember that, yes. So, we removed it because we were not sure about that. I think we need to then add it back, or something like that there. And then, yes, you're right, the client implementation has to be able… it assumes one-to-one mapping between the clients and connections that has to somehow be… We have to lift that restriction there as well.
I think it's doable. I think it's… it's fine to have that, but… there's a certain set of changes that need to happen in the spec, in the Go implementation, then you can do the corresponding part in the supervisor. It doesn't have to be the supervisor. Technically, you could call it an OpAMP proxy, right? Could be part of the supervisor, could be… collector OpAMP extension that implements that, right? If you're using the collector as a gateway.
for other collectors, that gateway today, it serves as essentially an OTRP gateway, right? A telemetry payload gateway.
could double… essentially, it could serve also the role of the OpAMP gateway, in that case.
So…
**Andy Keller** 28:45 Yeah, that's… that's how…
**Tigran Najaryan (Splunk Inc.)** 28:46 You don't necessarily have a supervisor in that scenario. You may have an OpAMP extension that does the concentration of OpAMP connections.
**Andy Keller** 28:56 Right, the challenge… the challenge… I… I haven't… I modeled that out and built that, and that worked. That's the way the OpAMP gateway works. It's an extension that runs in the collector, with the idea being that the collector's already an OTLP gateway, let's just also make it an OpAMP gateway.
You end up with one extra… WebSocket, because you have the WebSocket from the collector itself, or the collector's supervisor, potentially, and then you have the upstream WebSocket from the extension.
And there might be some tricky architecture. I've played with a little bit, where the supervisor actually Instead of pointing upstream, the supervisor points to the OpAMP extension, but then… And then the OpAMP extension?
**Tigran Najaryan (Splunk Inc.)** 29:47 It's a bit weird, yeah.
**Andy Keller** 29:50 I'll to save that one WebSocket connection, but, but, You know, like I said, this use case, which I'm pretty familiar with, is an IoT use case with communication over cellular, and an extra WebSocket, even if it's just one extra for this gateway, isn't a great solution, so… The goal is to really try to Limit ourselves to one connection and allow… Multiple… Collectors, downstream collectors, to be managed.
There were some other proposals raised That had to do with… namespacing, the configuration, and some things like that that I think were problematic.
See you, Tigran.
But I think, you know, the… It's important to keep the supervisor simple and stable.
And so, I would expect this to be… I haven't implemented it yet, but I expect it.
to be… Pretty small, in terms of, like, lines of code and complexity.
But, I don't know, Dmitrii, do you want to add anything else? I know, you know, we talked about this a bit in Slack.
**Dmitrii Anoshin (Splunk Inc.)** 31:13 Yeah, I'm… I don't have a strong opinion whether it's a supervisor or extension. I mean, yeah, I guess, like, one additional like, in the use case, when you have supervisor on the gateway, it kind of makes sense, but some… I would imagine that we also want to support.
gateways.
Not… non-managed.
Passing data, and…
**Andy Keller** 31:41 Yes.
**Dmitrii Anoshin (Splunk Inc.)** 31:42 legislate.
**Andy Keller** 31:42 And that's where I think the OpAMP, the existing OpAMP gateway really fills that.
**Dmitrii Anoshin (Splunk Inc.)** 31:47 Yeah.
**Andy Keller** 31:48 use case, this is particular to this sort of embedded environment where, you have a supervisor That's your main entry point. And, You want to do it all with one connection, so…
**Dmitrii Anoshin (Splunk Inc.)** 32:04 Yeah, so maybe we can have it as a shareable kind of company that can be easily enabled either on the supervisor or as an extension.
And for our use case, to clarify, we, like, there's some data coming through the gateways, right, or through the agents.
On the host, and they, like, enrich some information, but that information enrichment can be some kind of, like, hard-coded, let's say, per cluster or pure, like, per environment. And it's typically applied on the data flowing through that gateway, for example.
But ideally, we want to apply that to the, opAMP… messages as well, like, that are notifying that, hey, I have this this, OpAMP agent coming through the gateway, OpAMP gateway, and I want to add that additional information there as well. Like, let's say, descriptive attributes, so they match collector inter… emitting their internal telemetry, and OpAMP Emitting their internal… identifiable or descriptive attributes.
So, do you think that use case… first of all, it should be easy and no problem to add as a feature on top of that, right? What do you think?
So we are adding additional information on top of the data, on top of OpAM messages that are being passed through.
**Andy Keller** 33:35 I guess that brings up some questions about attestation, if we change messages, potentially.
**Dmitrii Anoshin (Splunk Inc.)** 33:42 Oh, right now, we don't even deserialize them, we just pass them.
Right?
**Andy Keller** 33:47 Yeah, but I… if… if we… if we start signing those messages, then,
**Dmitrii Anoshin (Splunk Inc.)** 33:52 Have to.
**Andy Keller** 33:53 Well, then we can't change them, or the signature won't match.
**Dmitrii Anoshin (Splunk Inc.)** 33:56 Oh, I see.
But we… we can… we can sign them on the gateway in that case as well, or that's not… that's not ideal.
**Andy Keller** 34:05 Stanley, thoughts?
**Stanley Liu** 34:07 Yeah, sorry, I missed the first half of it, but I heard the part about not changing the messages.
**Andy Keller** 34:14 Yeah, go ahead, you can…
**Dmitrii Anoshin (Splunk Inc.)** 34:17 I… the point is that if we have a gateway that is responsible for sending the messages and everything, all the messages sent through the gateway, is that something we would consider?
So, like, an agent, let's say, individual agents do not sign anything, and only send the data through the gateway, gateway, deserialized, like, send the messages, essentially.
**Stanley Liu** 34:44 So, would that be a case of, like, a local signer, where it's located, like, with the gateway, or would that be kind of… Using a trusted signing service in that case.
**Dmitrii Anoshin (Splunk Inc.)** 34:54 It doesn't matter that much. Whatever we decide for…
**Andy Keller** 35:01 The use case was to, To enrich the… maybe the agent… description.
The identifying and non-identifying attributes at the gateway.
Which would mean changing the message and affecting the signature.
**Stanley Liu** 35:20 Mmm.
Yeah, that's a good point. I can definitely look into that as part of the proposal as well.
Yeah. I don't have a solution in mind right now, but the capability that we want to offer is opt-in, so there is the option to, like, kind of progressively implement that change.
**Dmitrii Anoshin (Splunk Inc.)** 35:40 Yeah, but if we want, enrichment in addition to signing, I guess signing on the gateway would be the only option, right? And that… that should be feasible?
**Stanley Liu** 35:49 Yeah, that does sound feasible.
**Dmitrii Anoshin (Splunk Inc.)** 35:52 Yeah.
Cool, yeah, but if it's signed on the, on the, like, individual agent coming through the gateway, of course, you cannot identify it, and it's just gonna be… No, not supported in that case.
**Stanley Liu** 36:04 Yeah, I guess as long as the gateway is, like, a trusted, like, location and source, and then that's where the signing is happening, I think that makes sense.
**Dmitrii Anoshin (Splunk Inc.)** 36:14 Okay.
**Stanley Liu** 36:15 Yup.
**Dmitrii Anoshin (Splunk Inc.)** 36:22 But in that case.
If it's, okay, like, it's a future improvement, if you don't see any… any… if you don't see any problems with that.
I think it also doesn't matter whether it's Gateway or… or whether it's Extension or supervisor.
But, yeah, I think ideally, we should just support both and have it as a shareable component, I guess.
**Andy Keller** 36:49 Yeah, so, let me just, Just gonna put a link here so that other people can… go check it out, if you're interested, but that's the… that's the OpAMP gateway.
That we implemented.
And that runs as… that you add as an extension into the collector, and so the collector becomes… Typically, you're adding it to something that's already an OTLP gateway, and so now it becomes an OTLP gateway and an OpAMP gateway.
**Dmitrii Anoshin (Splunk Inc.)** 37:24 Okay, yeah, sounds good. So, essentially, we are… we would like to… If you're also seeing that But what I proposed makes sense, is an option to add, later on.
it would be great to proceed somehow with, like, either donation or accepting the PR from that contributor, so what would you prefer, how we go about it?
**Andy Keller** 37:49 We'd love, we'd love to donate it. I, you know, I… I also know that the upstream community is, You know, there's a lot of challenges with just accepting lots of donations, so… We, we, you know, are kind of waiting for people to be interested in… in wanting to receive it, so if… if, I don't know what that threshold looks like, but…
**Dmitrii Anoshin (Splunk Inc.)** 38:15 Yeah.
**Andy Keller** 38:15 But we're very happy to… we have no intention of owning this or having it be closed source or anything like that. This is… something we built that we think is generally useful. So we definitely would accept PRs, and I think, you know, if we do PRs first and donation later, or we do donation first and PRs after that, either way, I think…
**Dmitrii Anoshin (Splunk Inc.)** 38:38 Yeah, I think probably donation first might be easier. But the thing is, as you mentioned, yeah, donation is typically not an easy process, unless you have some other… someone else from the community interested, right? In that case.
**Andy Keller** 38:52 Yes, exactly.
**Dmitrii Anoshin (Splunk Inc.)** 38:53 In this case, we are interested, so we will be happy to… elephant.
**Andy Keller** 38:59 Yeah. Okay.
**Dmitrii Anoshin (Splunk Inc.)** 39:03 Cool, thank you.
**Andy Keller** 39:07 Alright, anything else before we wrap?
Okay.
Thanks, everybody. Have a great week.
**Dmitrii Anoshin (Splunk Inc.)** 39:16 trip. Right.
**Stanley Liu** 39:17 Thanks.
