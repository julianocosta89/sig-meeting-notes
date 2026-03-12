SIG: Agent Management WG
Date: 2025-10-15
Duration: 53 minutes
Zoom Recording URL: https://zoom.us/rec/share/c5XoZmN_jcskoG1oKewV_Xd_N2KfKJ8gKN-ZaGKbbxfHAGEb4N-2C0r3Egx15qvU.xLGRgf3pPr5YmkLj
============================================================

## Zoom Recording Transcript

**Tigran Najaryan** 05:13 Can anyone hear me?
If… Okay, real quick, Mike.
Airport, okay.
Yeah, I think we can start, Jack. You have the first item.
**Jack Peterson** 06:13 Hello, everyone. I will introduce myself. I'm not sure if I have met everyone on the call, but I am I work on… my name's Jack, I work on the OpenTelemistry team at Datadog, and I've been… Working on a proposal to, add some verification.
for payloads to the op-amp spec. I will… I'll share my screen.
Basically, the high level, the… The overall desire for this is to split to… Split the distribution source, being the op-amp surfer.
From the origination point of the message, whether that's, you know, a config message, whether that's a restart command.
Whether that's… we already have, obviously, the bike signature, you know, field for the packages available. But in general, the concept of you know, let's allow the op-amp server to be the distribution point, but not necessarily the end-all, be-all.
origination of these messages, if that is, you know, desired by the agent and the, you know, the vendor operating the server, in this case.
So we, I had some, you know, we got some good feedback, last week. I know, Tigran had left some comments, as well, you know, between, you know, at maybe during or after the meeting last week, as well as a few today. I had made some.
Changes, to the proposal to try to simplify, some things here.
One of them being… Removing… Initially, the proposal was saying the agent should send over a hash of a certificate that it expects the route to be, but it, you know, it could be, You know, it would be, likely that, you know, a vendor would have one route, and, you know, they should… this should be out of scope.
Of this spec, how they, you know, coordinate, distributing that route, or coordinating which is the route.
So there is a, Sorry, I can… I'm not sure if everyone was here the last time I know Tigran was, but is there any desire for me to kind of go into more depth about… You know, about the proposal, or go over some of the, you know, message exchange, flow here.
**Tigran Najaryan** 08:55 I did take a look at the document one more time, so I don't need to, but if others want to, sure, feel free to do that.
**Jack Peterson** 09:07 Alright, so I will… so, yeah, I'll just do a quick high level. Basically, if the agent When the agent slash client connects to the server on the first time, they would set a flag.
The requires payload trust verification flag.
You know, would be the next bite.
Or so on the, Agent capabilities.
This would indicate from the agent to the server that this agent expects that… All server-to-agent messages should be signed.
And this… that they're opting into this feature, essentially. So if an agent does not set this flag when connecting to the server, everything functions as normal, fully backward compatible.
So if this flag is set, then the server will… If the server does not actually support this feature, right, they'll send their server to agent.
And they will not include a, offers payload trust verification, right? They will not send any of this trust You know, any of the response fields for a trust chain response. And at that point, the agent, you know, in my proposal, it says the agent should disconnect at that point, must disconnect at that point, but, you know, that could be out of scope.
Of how the agent should proceed, if the agent wants to proceed anyway.
Maintain the connection, or if they drop the connection, so that's… Something… don't feel that strongly about.
But then, essentially, if the service supports this, they will… Send along, in a bytes format, the chain of certificates, so starting with the root, all the way down to, you know, however many steps, maybe 2, 3, 4, certificates, down to the leaf.
And then from there on out, essentially every server-to-agent message would be expected to be signed by that LEAF certificate, and the agent would either reject the payload, reject the server-to-agent message if it's not signed by this, leaf, and, then, you know, close the connection, or continue, or whatever, you know, is the best option there. I believe in my spec, I say, hey, let's should disconnect at that point. But, this basically allows there to be a route Certificate that is, you know, held securely by the vendor or the operator, and… This allows the agent to verify that each of these messages has actually come from a authorized… authorized origination point that is not necessarily the op-amp server, right? So I go into some… talk about, you know, why… why… what is this protecting against, right? What is this… So let's say, you know, if there's a compromised distribution server, right, the… Takeover of a single op-amp server, you know, such as recent vulnerabilities could allow An attacker to take over your fleet, since currently the server is both the distribution point and the source of origination.
There's, you know, this could help limit the blast radius, from a compromised, server, right? So, let's say the, you know.
The messages could be modified in between the… The actual distribution point and the origination point.
As well as a weak change attribution, that it's, you know, hard to… Be sure, essentially, on the side of the agent, that a message or a command, you know, a config or a command or restart, things like that, that are… come from an authorized, point. So this is not… there's not full… you know, there's not wholly… this is somewhat similar in concept to something like an app store, right? Where, obviously, you have a secure connection to Apple's server to download the app, but along with the app comes with the… the signature, right? Same thing we have for the… binary, the package is available, just wanting to, you know, expand that to the op-ed messages as a whole.
**Raphael Menderico** 13:30 So it's not a… yeah, I'm not proposing encryption of message contents, or…
**Jack Peterson** 13:33 A way that the server can verify the agent who Is saying who they are.
But yeah, I did make some changes, even, some small changes to Gon, based on your comments. A few things, like, you know, lined out, taking out a few, required messages, clarifying, hey, on the signature field.
You know, the server would sign the whole… the remaining flattened fields, essentially, like… like you suggested, but just not the signature field.
Right.
So I'm not sure, clear as mud is there.
Any thoughts or questions?
**Tigran Najaryan** 14:12 Thanks, Jack, for, for clarifications. So, the concept makes sense to me, right? I understand why you would want to do this. There's a few open questions, like the usage of separate CA servers, or more than one CA server, or whether we want to sign the entire message, or just the config payloads. I think those… we can work on those, right? At this point, I don't think… I think that's a priority, to figure out the answers to those questions.
More important at this stage, I think, is whether we want this… we want a capability like this in Open Protocol at all. And the answer to that is not clear to me. I think I mentioned it last time, I want to see a significant community interest, first.
So, that would be, I guess, a top priority for me if I were to work on this. My advice would be to work on that, right? To collect the community support.
You can, I guess, feel free to open an issue or a PR in the spec repo with the proposal, I guess in a bit more refined form.
if you want to show a prototype, that would be even better, I guess, attached to the proposal, and engage people in the discussion, people from the community, and more people… others that are not necessarily regulars in this call, right, but who may have an interest in a feature like this. And, I would… I would take, so, an active discussion and interest and… and approvals.
from people, on that PR, or thumbs up on the spec issue, let's say, at the minimum, would be the starting point for me to consider that as something that is worth being included in Moab.
If we don't get there, I think that would be a barrier to getting it included in the open protocol, regardless of whether I think it's a sound technical proposal, right? Module or some refinements.
But to me, that's not enough, right? I want to make sure that this is something that the significant, let's say, a significant subset of the community is interested in and will benefit from, and not just one company. It doesn't really matter which company, right? This would be the same for any other proposal.
**Jack Peterson** 16:42 Yeah, excellent. I appreciate your feedback and your suggestions and questions throughout the process, and I'll certainly be able to, you know, start working on RFC and implementation.
**Tigran Najaryan** 16:53 To, to get that public input.
I don't know if anybody else has any other proposals. And yeah, I think on a different proposal, you suggested to use the custom messages, the proposal for the metric sampling.
I don't… I guess that could also be done as a way to experiment with this capability using custom messages, although it would mean that you're also using custom messages to deliver config payloads, so kind of your.
**Andy Keller** 17:31 Yeah.
**Tigran Najaryan** 17:32 Kind of, like, you divert from the regular way of doing things a bit more.
But maybe, I guess, right? It would be a possibility as well.
**Andy Keller** 17:41 Well, I think, I think, It's possible to send a custom message along with message. You know, it's part of the… part of the message in both directions. So, in effect, you could send the signature along with the custom.
**Tigran Najaryan** 17:54 Yes, yes, yes.
**Andy Keller** 17:55 And I think… You know, with that, you could… effectively prototype this.
**Tigran Najaryan** 18:05 To have the custom message response with the certificate chain, and .
**Andy Keller** 18:10 Another custom message response with the signature.
And, and obviously, it's just on the… on the agent side, it's just the capability that you would need, but it's a custom capability that you would declare support for. So, you know, it's… I think… I don't think there's any barriers to implementing it that way.
Jack, I'm not sure if you're familiar with that other proposal that was, Regarding, metric configuration that was made?
**Jack Peterson** 18:40 I'll… I'll take a look. I mean, obviously, if you have the link, it will be nice, but I should be able to find it, right?
**Tigran Najaryan** 18:47 It's in the specification repo, not OPAM specification, the OpenTelemetry specification, and the level is unrelated to what you want to do here. The only common thing is that it's a new thing for the OPAM protocol.
**Andy Keller** 18:59 Great.
**Tigran Najaryan** 18:59 We had a suggestion about how to… make progress using custom messages without, I guess, waiting for it to necessarily be part of the open protocol core.
**Jack Peterson** 19:10 Right, yeah, that… I appreciate that, and that does sound like a good way, to… Be able to, you know, demo and iterate this without necessarily, building everything into the OpAmp Go and building custom.
**Andy Keller** 19:25 Yeah, and stuff. Just to speak to that a little bit more, part of the intent with custom messages is to allow this sort of… Extension of the protocol, and… and… To the extent that that… Those extensions are published and documented, and other people can implement them and, You know, it could stay that way for a long time.
But I think if there's broad support for something, then it could be promoted into the actual specification.
So, I think that, you know, creates a good pathway for… Something, not just prototyping, but also… .
**Raphael Menderico** 20:04 You know, interim support until there's…
**Andy Keller** 20:07 wider adoption.
**Jack Peterson** 20:11 Right. In other words.
**Andy Keller** 20:12 Thank you. It was always intended as a way to… to potentially Graduate something into the protocol itself.
I guess one thing I just wanted to clarify, the idea is Is it… the… the agent sends… normally the flat… the, like, agent capabilities are sent… are consistent, but is the idea that this particular capability, when specified.
The chain is re… respon- the server responds with the chain, or is it just the first time?
**Jack Peterson** 20:51 I think it would just make sense to do it the first time, and I can… I mean, you can keep the flag set, or… not… you know, you keep the flag set the whole time, but, like, this… this… this flow should happen on startup once. And, you know, out of scope is, hey, how would the, you know.
is the… does the server… is the server gonna use a different route at some point? At that point, that would be out of spec. Like, you know, that… that vendor or whoever has to communicate with their customers, hey, we're gonna upgrade on… on this date, or whatever, and, you know, we'll drop the connection to them.
**Andy Keller** 21:25 It seems like it… The server could potentially, you know, track that and return a trust chain response whenever necessary to You know, migrate to your new certs.
But I do think that that's something that we should consider, is what that flow looks like.
As… you know, Obviously, expirations on… Usually on trust chains are pretty long, but, they do expire, so, Knowing how to handle that appropriately.
That would be helpful.
**Jack Peterson** 22:03 Right. I guess in this case, it would be, you know, hey, the…
**Raphael Menderico** 22:07 The leaf certificate or whatever is no longer valid, and at that point, the agent.
**Jack Peterson** 22:11 Disconnects, and then… up to the… to figure out, oh, I should reconnect, and then at that point, I'll get a new trust chain, but there could be room for adding a, you know, renegotiation.
**Andy Keller** 22:22 Yeah, let me…
**Jack Peterson** 22:23 Message or face.
**Andy Keller** 22:24 Sure.
**Jack Peterson** 22:25 Without a disconnect.
**Andy Keller** 22:27 Sure.
Okay.
Good, thank you.
**Jack Peterson** 22:38 Alright, I yield the floor.
**Tigran Najaryan** 22:43 Okay, thanks. Let's see what's next.
Joanne, am I pronouncing your name correctly? Is that Joanne?
**JM Juande Manjon** 22:54 You can say, Juande?
**Tigran Najaryan** 22:55 hungry. Alright.
**JM Juande Manjon** 22:57 Okay, so, this is the first issue sewage issue that we talked about last time. This is pending for review.
that PR is sitting there for 3 weeks now, I guess?
So, I need someone to review it. And the second one is a request from a user that was creating a Python client.
In order to leverage the server app.
For the server example, in order to… to reset the configuration programmatically to the Python client, something like that.
I'm thinking that maybe the Sisu could be adding a REST API to the server example?
So, in that case, the client can send post requests to do the same way.
to do things in the same way that the UI does.
Currently, the UI… the UI is using the form submission?
Using basic HTML, and adding a REST API would improve the uses of the server example.
**Tigran Najaryan** 24:05 So, on the… I guess, on the config, on the default config for the… for the example server.
I haven't had a chance to think about it, but I guess my… Initial reaction would be to keep it simple, just implement one of the approaches.
maybe just have the command line version. I don't see the need to have two different mechanisms to support one specific use case, but there… again, just my initial reaction, maybe there is a valid use case for both of those, and…
**JM Juande Manjon** 24:40 Right, so I think it's having a REST API will improve the UI, because the UI can leverage the REST API instead of using this transformation, so maybe in the future it could be useful as soon as we add in more features to the OPAM.
protocol that we can use REST APIs to implement that feature. That doesn't have to require UI actions.
**Tigran Najaryan** 25:04 Yes, maybe… just one thing to keep in mind, this is an example, right? We are not aiming to have a production-grade code here.
primary purpose of example is to demonstrate how to do something in the most, I guess, straightforward way, simple way, so… what you wouldn't necessarily consider to be the best way to do for a production-grade software may actually be the best approach for an example, right? So.
One of the criteria would be how easy it is to see in the code and follow the code.
I don't necessarily… imply that an API is a harder way, but… seems to be… Again, hard to make a call immediately, but… I would keep it simple, right? That would be my advice.
**JM Juande Manjon** 25:58 For me, a CLI and API is simpler than UI.
**Tigran Najaryan** 26:04 Sure, yeah, I think I'm not… that… I guess I'm saying choosing between a command line or an API, right?
Choose the… whatever looks simpler, on paper, in the code, right? Easier to follow, to understand, as an example.
**JM Juande Manjon** 26:23 Yeah, okay.
**Tigran Najaryan** 26:26 Your other… yeah, go ahead.
**JM Juande Manjon** 26:28 No, I think it's, also for the example point of view, it could be the easy… how it's easy to have an API in the… a PAN server that can fill some kind needs to… to remote configs and clients.
Yeah, programmatically.
**Tigran Najaryan** 26:53 Sorry, I didn't get that.
**JM Juande Manjon** 26:55 Look, when I say that providing example of the uses of the REST API, Come help, client that is willing to use the OPAM protocol.
to see how easy it is to leverage the REST API to… To programmatically send configuration to the agent.
**Tigran Najaryan** 27:15 Okay, yeah, maybe, yeah, possibly.
I guess I would want to see, maybe, what it looks like in the code to… To be able to have a bit stronger opinion.
**JM Juande Manjon** 27:28 Okay, I already implemented that part, but I didn't push anything because I have my previous PR pending to that.
Yeah, so…
**Tigran Najaryan** 27:36 By the way, your previous… so, the one you said is open for a few weeks, can you add the link to that? Because I'm not…
**JM Juande Manjon** 27:42 It's there in the document?
**Tigran Najaryan** 27:45 Which one? Sorry, you have two issues.
**JM Juande Manjon** 27:47 Agent server example cannot find the certificate.
**Tigran Najaryan** 27:50 Yeah, that's, that's an issue. Is it linked to the.
**JM Juande Manjon** 27:53 Yes.
**Tigran Najaryan** 27:53 You know what is that?
**JM Juande Manjon** 27:54 Yeah, oh, maybe this is the PRS. Let me open it.
Yeah, this will lead to the issue, and the issue has… On the bottom.
**Tigran Najaryan** 28:08 Is it PR number…
**JM Juande Manjon** 28:10 or…
**Tigran Najaryan** 28:11 No, that one is merged, right? What's the PR number?
**JM Juande Manjon** 28:16 Hold on, so the PR number… is for one… for… 5-4.
**Tigran Najaryan** 28:27 Or… 5… 4? Yeah. Yes, okay, I see.
Okay, I see. No. Yeah.
Okay, I'll take a look.
**JM Juande Manjon** 28:43 Yeah, so in the Upon channel, I request to assign this issue to this PR assigned to me. So how is the best way to communicate with the… Upon reviewer.
**Tigran Najaryan** 29:01 you want… sorry, you're… you want to assign the PR to.
**JM Juande Manjon** 29:05 So I request in… to… because this issue is not assigned. I don't know if there is a way that… I don't know how this is… you provide an issue, you request help, you assign this issue to someone else, and someone else implement the PR, and send the PR for review.
Yeah.
So, I'm asking, who is the reviewer that we need to contact to to ask for assignments?
**Tigran Najaryan** 29:32 we don't… I don't think we necessarily have a formal process for doing that, if that's what you're asking for.
**JM Juande Manjon** 29:37 Right.
**Tigran Najaryan** 29:38 Yeah.
We don't necessarily have a well-streamlined process of how do we go from an issue to a PR to a reviewer to get matched.
It has been more on an ad hoc basis so far.
But for the, I guess, for the particular PR that you created with, that 454, I think, yeah, I, I will take a look at it.
**JM Juande Manjon** 30:07 Also, these PR decoupler dependencies of using the cert in the pilot already, because it moved to this example.
It's completely decoupled, and I modified one test.
that, was using the certs directly, the search folder, and now we are using a different strategy. Is it in the PR.
**Tigran Najaryan** 30:30 Yep, yep.
Okay, yeah, I'll review it.
**JM Juande Manjon** 30:39 Alright, thank you. So, so in the second entry, so you're asking for help?
So we're willing to help on that.
Issue.
**Tigran Najaryan** 30:49 Makes sense, yeah.
I'll, I'll think a bit about the… whether we want the command line or the API, and we'll see… I'll try to comment on it.
So that you know which… which way to go.
**JM Juande Manjon** 31:03 Okay, thank you.
**Tigran Najaryan** 31:04 And I guess, the person who opens the… The, the issue originally.
I think they are a Python maintainer?
So, maybe it's also worth seeking their feedback directly.
Because one of the approaches may be easier and preferable for them, because they are the one who need to use it, right?
Ricardo, I don't know him, but…
**JM Juande Manjon** 31:37 Okay, I, I would be me.
**Tigran Najaryan** 31:39 I'll ping him, yeah, I'll ping him and see what… what does he think, because he didn't reply after your comment.
It's unclear what his position is.
**JM Juande Manjon** 31:53 That's all from me. Thank you.
**Tigran Najaryan** 31:56 Alright, thanks.
Next one. Andy, you're off the next one.
**Andy Keller** 32:03 Yeah, I just posted an issue a couple days ago, And, it looks like, there's a bug in the supervisor regarding… But then I realized I… it's… I think it's a little bit unclear, exactly how this should be handled, and the… basically, with an agent identification message, you can change the instance UID, But that doesn't directly impact the agent description, currently?
In other words, the service instance ID is… Remains the same.
But I… I think generally, and with the supervisor, the service instance ID matches the instance UID.
The spec doesn't say that that's necessary, it just says… It could be equal to, or any other value that uniquely identifies the agent.
So I guess there's really two… the reason I wanted to talk about it is… is do we want to take a more opinionated stance and say that it needs to match the agent ID?
And then in that case, I think we can have the library update the agent description as well. And I started to implement that, and then realized that that's… Not what the spec says, so… The other thing is to just implement, the… in the onMessage handler of… the supervisor, an update to the agent description when the instance ID changes.
**Tigran Najaryan** 33:36 Yeah.
I think, so… The spec doesn't have a… it doesn't say that… having the instance ID as part of the agent description is a must, right? So it says it's a possibility.
**Andy Keller** 33:51 Yeah, I just… I have it quoted here. Right.
**Tigran Najaryan** 33:56 Yes. We also… there's no precedent of the, of the client library touching the agent description at all, right? So it assumes that it receives it from the… whoever uses the client.
And then it passes on… on to the… to the server as is.
I think… What… we could maybe… Have a sort of a… Reminder there that if you receive a new instance ID from the server, and you happen to also use it in the agent description, make sure you update it.
But I think if… if the spec doesn't make this a strong requirement, we shouldn't be doing that in the OBAMPGO implementation either. So OBAMPGO should be, like, should follow as closely as possible what the spec says.
**Andy Keller** 34:50 Right.
**Tigran Najaryan** 34:51 At the same time, if we can have the wording in the spec which says, make sure, be careful, if you're Okay. There, then make sure you update it on the… on the… when the server gives you a new instance ID, and then that would be actionable by the supervisor, right? And we can go and fix it in the supervisor.
**Andy Keller** 35:08 Right, okay. I'll just open a PR in the spec, and then we'll fix the issue in the supervisor.
**Tigran Najaryan** 35:14 I think it would look a bit weird if we… if we touched the agent description in the client implementation.
**Andy Keller** 35:23 Yeah, it is weird. I did it. And then I decided not to post the PR, because I realized…
**Tigran Najaryan** 35:29 I realized this issue.
**Andy Keller** 35:31 It's certainly doable, but I think part of it, as well, is the formatting of it, because it comes through as…
**Tigran Najaryan** 35:38 Yeah.
**Andy Keller** 35:39 as bytes, and then you need to decide, is it a UUID, and etc.
**Tigran Najaryan** 35:44 Yeah.
Yeah.
**Andy Keller** 35:49 Okay.
**Tigran Najaryan** 35:49 And also, service instance ID is… you use it when you use OpenTelemetry, centric agent?
**Andy Keller** 35:58 But…
**Tigran Najaryan** 36:00 what if you don't, right? What if you use something completely outside of OpenTelemetry ecosystem, which is… Which we think that… should be fine, right, if you want to use Open, but that's okay. In that case, you may put the instance ID somewhere else, under a completely different attribute name, and we have no way of knowing that.
So, and then… then that capability, which you thought is a responsibility of the client, is going to be broken now by the no longer works. Agreed. Make it a responsibility of the… of the user, the client.
**Andy Keller** 36:33 I'm comfortable with that. I think we should make a note of it, because I think that's partly why it was overlooked in the supervisor and… Yum.
I'll add a note to the spec.
**Tigran Najaryan** 36:45 Okay.
Okay, there's no other items in the agenda. Anyone has any topics?
Alright, thank you all.
**Andy Keller** 37:10 One thing, Tigran, regarding that other PR that we were talking about, the, metric.
Well, the configuration, have… I know they… there was a proposal to discuss that in a separate SIG, is there…
**Tigran Najaryan** 37:25 I think we were expecting… someone to join the… this call to…
**Raphael Menderico** 37:32 How for you.
**Tigran Najaryan** 37:33 Oh, sorry, you are the author.
**Raphael Menderico** 37:36 Yes.
**Tigran Najaryan** 37:37 Oh, great.
**Raphael Menderico** 37:41 Yeah, so, okay, I think, like, what I'm getting here is, I got the suggestion to use the custom capabilities, and to be fair, this is, We are looking on how to use it, and this was my original suggestion internally.
So… So it's probably, yes, implementing… starting with that seems reasonable, and I think if, we can demonstrate it… we can demonstrate how it works. The other one is the prototype. This is something I want to talk to Josh.
Because, to be clear, the protocol we described is the one we… I mean, it's an adaptation of the one we use internally.
To scale our, agents, our internal agents.
So, the question is, you know, because Google, you know, companies, I need to figure it out if I have… if I can show that.
because this would demonstrate a lot, or if I have to come up with a clean room implementation.
I will discuss with Josh and others, because bureaucracy, but I think it's totally fair, and yes, we would, That is… that is… Yeah, there is prior art, and there is probably a good prototype.
I think some of the concerns raised, they are valid.
But historically speaking, we, we had addressed some of them, so, like, scalability, someone said, oh, but then it means that there is one exporter for every metric, no.
We, we grouped then, and We learned some of those lessons the hard way, let's put that way.
But, yeah, I took the point… I take the point that, yes, custom capabilities, and indeed it was the first way… it was the way we were planning to go anyway, so, first. So, I think, yeah. One question about custom capabilities, you… you might help me.
When I was looking, I assumed that custom capabilities was more, like, per… was more vendor-specific custom capabilities, because they usually are, like, named, and I assume there was. But if I understand correctly, that's not necessarily true. They… there can be a custom capability that's, like, OpenTelemetry custom capability, or something like that?
Is that the case?
**Andy Keller** 40:05 I think that depends on where that's coming from, and I think the idea is to really identify the source of this capability, and also to avoid naming conflicts between different capabilities, so if… this is an OpenTelemetry custom capability, then it should be coming from OpenTelemetry and discussed within OpenTelemetry, and not conflict with other OpenTelemetry custom capabilities, and if it's you know, coming from Google, and then it should probably be named with Google, and then it can be documented as such, and I would certainly encourage you to, you know, document the messages and their formats, and how it can be used, and I think that would really aid in the understanding of What the message flow should look like, and how it would be used?
**Raphael Menderico** 40:56 Yeah, so that was one thing that I maybe… I did not find, like, if there is a way to, say.
let's say, claim the name of a custom capability in OpenTelemetry. Something that I can say, look, this is a custom capability that belongs to Google, or maybe it evolves, but, like.
**Andy Keller** 41:11 Even if it's not… even if it doesn't matter that much what's inside the custom capability? Yeah, it's a good… it's a good question. We don't really have, like, a registered.
**Tigran Najaryan** 41:18 We don't have a registry, yes. We would need some solo registry, and I guess there's an opportunity. We could do that, right? You would be the first, I guess, official custom capability introduced by OpenTelemetry. We could definitely do that. We would prefix it by io.opentelemetry.whatever is the name of the new capability you want to have it.
I think it's doable. I don't see a problem. We could introduce some sort of a registry, basically a file in the spec repository.
we would list the capabilities that OpenTelemetry introduced.
I am not entirely sure whether this needs to be an open delivery capability, or can be broader, or you would limit that to Google. That's a decision that probably needs to be made, but I think it's doable, one way or another.
**Raphael Menderico** 42:05 I think in this case, it might be even nicer, I mean, we could start with something just Google claims the name, Google. That would start.
Yeah. That's no problem, because we're saying you prefix it by an FQDN, obviously you have com.google as your prefix, no one else is going to claim that, right?
Yeah. Okay, maybe it's something, like, yeah, because it wasn't clear to me how we should find those. Okay.
**Tigran Najaryan** 42:30 Sure. Yeah. And by the way, I guess the part of your proposal where you need to be able to communicate the incremental changes in the configuration in the efficient way, I'm in favor of having a generic solution in the OPAR that solves that problem, right? I just don't know what that solution looks like, so if there is a… if there is a proposal that tries to address that, I think it would be useful, and I think others in this group would also be interested in seeing something like that, because It came up a couple times in the past as well. We saw that it can be a problem. Sometimes the configuration of an agent is a significant chunk of data, and you do not want to resend it every time there is a time change in the config, right?
So… that… you would benefit from that, obviously, as well, right? You could use that, even if it's in conjunction with maybe some of the custom capabilities, just to express the desire for the agent to receive that particular config. But then, through the generic mechanism of propagating the config changes more efficiently, increment… having that incremental update mechanism, which we don't have today, would make it also more suitable for your particular use case.
**Raphael Menderico** 43:54 I can definitely split the proposal in two, let's say, the incremental part versus the.
**Tigran Najaryan** 43:59 Could be, yes, could be two separate things, right? So we… we have a… we are the generic… way of… sending incremental changes to the config in the OPAMP.
And that would… can be used by any… any feature, and then you add another… essentially custom capability, to… to ask the server for the… for the metric sampling, or whatever is. In particular case, it's metric sampling, but we can have a trace sampling, other capabilities, right, that OpenTelemetry is interested in.
**Raphael Menderico** 44:32 That sounds fair. Okay.
**Andy Keller** 44:37 I don't know where the, effort is in… with the Java SDK. I know that there's some… there was some effort to, build op-amp support into the Java SDK for… configuration. It might be worth looking at that and seeing How they're handling the, formatting of… The config map, You know, if there are multiple keys, what those keys are.
And if they're establishing semantic conventions around the config map, that's returned.
Because I, I, I do appreciate that The config map is… Extremely generic, it's basically key-value pairs, and it's not… Clear how that key-value… those key-value pairs should be processed.
And this is an area where I think we could… Benefits from… for some… From some more specification, so it'll be… it'd be… Useful to see what they're doing, and also, try to… Both, you know, document what we're doing and what we're expecting, and then also add support for things like incremental changes as needed.
**Tigran Najaryan** 45:58 Yeah.
Yeah, that's a good point, and I think there's another, like, there's a file configuration SIG as well. They define a format for specifying the whole config for the SDK.
**Raphael Menderico** 46:10 I don't think we had a chance to…
**Tigran Najaryan** 46:13 speak with them either. It may be the time for us to figure out, okay, I have a file config, how do I propagate it through all pump, if I want to do that? And we may have a stronger opinion on how exactly it should be done, other than hand-waving and saying, just send it through a pump, however you want to do that, right?
**Andy Keller** 46:34 Yeah.
**Tigran Najaryan** 46:37 And also, like, if… If the sampling… Feature that you want to have.
Can be part of that file config, and that file config is some sort of… it… It's composed of multiple sections that can be changed individually, sampling being one of those, how are you supposed to record that in the config map, such that the incremental changes.
**Andy Keller** 47:03 Can be sent.
**Tigran Najaryan** 47:05 Without sending the whole thing.
**Raphael Menderico** 47:07 How do you break it down into… is it, like…
**Tigran Najaryan** 47:10 literally some sort of combination of sections? Is it, like, to do a diff of… what does that diff look like?
**Raphael Menderico** 47:21 Yeah, it's strictly… Yeah, fair point. Historically speaking, we don't use files, but I think it ultimately could be abstracted as a, like, at core, it could be abstracted as a file. It's more… Yeah, the… the problem, like, we also use this, In our internal system, we don't propagate the same configuration to all agents, because we want to roll out slowly.
So there is, like, some level of control on… depending on the agents, we send one version or another of the configurations. It's… that's one reason it's not unified, but…
**Tigran Najaryan** 47:57 Yeah.
**Andy Keller** 47:58 Yeah, I think I saw that comment, and I think, you know, Tigran mentioned that the spec really is intentionally Leaves out the… process of rolling out, it really defines the server to agent to one agent.
interaction, and it's up to the implementer to decide, is that one agent at a time across 100 agents? Is it 10 at a time, or is it all 100 at one time, or what does that look like?
it's not defined in the spec, because I think there's a lot of different ways you might want to handle it, so…
**Raphael Menderico** 48:32 No, it's more to say why file might not be exactly the right abstraction, because, like, we have two instances of the same file, or more than two instances of the same file at the same time.
So maybe what's missing is File Plus version, or something like it. That might be the notion that might be missing.
**Tigran Najaryan** 48:48 you… you can send different files to different agents. There's no… nothing prohibits that, right? There's nothing in the spec or in the implementation which says.
You need to send the same thing to all the agents that ask for it.
Even if the agents are of exactly the same type, or the same version, it's still a decision that the server makes when to give which config to the asking agent.
And that defines your rollout strategy. You can give it all at once to all the agents, or you can stagger it, or whatever, right? It can be… it's a server decision that's deliberate that we don't have it specified in the spec.
**Raphael Menderico** 49:32 That's fair, yeah. The problem is that the agent right now doesn't ask for the file, it actually, like, ask for the configuration.
**Tigran Najaryan** 49:37 The agent says, yes, I am… I am this… this agent, right? Give me something.
**Raphael Menderico** 49:44 Exactly. That's the part. The bit missing is the agent actually saying, I want that.
Specifically.
**Tigran Najaryan** 49:50 Which is, yes, and that part, like we said, that one of the possibilities is to describe it through the custom capabilities, right? Or through extra key-value pairs in the agent description.
Or, as a custom message, would be the third option that Andy described.
once, I guess… and then you can settle on one of those if that works well. If it doesn't work well, then we'll consider whether there's a need to have something else at the core of the protocol.
**Raphael Menderico** 50:24 Okay, fair enough.
**Andy Keller** 50:30 I did think it was… might be reasonable to, in the, In the remote configuration set by the… The remote config status sent by the agent to also indicate what sort of configuration it's expecting.
Or supports.
But that is, that is, you know, an extension that… We would need to consider and understand exactly how that works.
You know, for example.
**Raphael Menderico** 50:57 there was a…
**Andy Keller** 50:58 With the supervisor, there was some question of… you know, is this collector.yaml? Is this just an empty string? You know, do we want to support other configuration files? And if so, what do they do?
Do we support multiple configuration files and allow the collector to merge them together? There was definitely a lot of discussion around how that should be handled.
And I think there's an opportunity to… To be able to indicate That you support it in… you support or you expect additional configuration keys in the config map.
And then the server can send those as appropriate. But again, we're in… kind of unchartered territory then, and I think that that's something that we need to clarify and explain, and…
**Raphael Menderico** 51:50 Okay.
**Tigran Najaryan** 51:51 Just, I guess, just to be clear, Rafael, we're open… to adding… The missing bits to the protocol, but we want to be careful here.
To make sure what we're… that we're making changes in a way that we don't introduce stuff that is narrowly targeting one use case. Hopefully, the changes we make they… they help with more than one specific use case. And the example I had there is that this is just metric sampling, but we have trace sampling that is pending there, most likely they will want something like that. It's probably not going to be feasible for every use case to modify the protocol, right? It's probably not the right approach. We need to have something that works for more than one use case here.
**Raphael Menderico** 52:44 To be fair, Josh warned me that this could be the case. So, yes, I knew.
**Tigran Najaryan** 52:51 Okay.
Cool.
**Andy Keller** 52:56 Alright, I think that's it.
Thank you, everybody.
**Tigran Najaryan** 52:59 Thank you all.
**Evan Bradley** 53:00 Bye, everyone.
**Tigran Najaryan** 53:00 Bye.
**Andy Keller** 53:01 Thanks for joining.
