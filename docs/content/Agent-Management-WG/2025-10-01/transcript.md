SIG: Agent Management WG
Date: 2025-10-01
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Johanna Öjeling** 00:59 Hi!
**Andy Keller** 01:08 Hello!
**Johanna Öjeling** 01:11 Hey!
**Andy Keller** 01:13 Sorry, I had to step away from my desk, so I'm joining from my car.
Oh, okay!
**Johanna Öjeling** 01:18 Yeah, no worries!
Hey, I'm Johanna, I work at Grafana Labs.
**Andy Keller** 01:24 Oh, nice to meet you. Welcome.
**Johanna Öjeling** 01:26 Thank you.
Me too.
**Andy Keller** 01:31 I'm from, Bindplane, and I'm one of the, maintainers.
**Johanna Öjeling** 01:36 Okay.
Cool.
Hey there, Rob.
**Evan Bradley** 01:40 Hello.
**Andy Keller** 01:58 Evan, I don't know if you were here.
**Tigran Najaryan** 02:01 everyone.
**Andy Keller** 02:02 what I was saying that I'm joining from my car, so I can't see the agenda.
I'm here to elicit it.
Hi, Tigrant.
**Tigran Najaryan** 02:10 I am.
Okay, I think we can start.
I see a couple items on the agenda.
Jack, I'm not sure, is this your first time you're in this call? I can't remember.
**Jack Peterson** 03:12 Hi, yeah, I've joined a couple times, over the last few months, but… but this is the first time I'm maybe, you know, really speaking or proposing anything, so…
**Tigran Najaryan** 03:25 Yeah.
**Jack Peterson** 03:26 I can give a quick introduction, because I don't think I recognize all of the names here anyway. But yeah, my name's Jack Peterson. I work at Datadog for the last year and a half on our OpenTelemetry team, done some work in the OpenTelemetry Collector with Evan.
And on some of our, other, OpenTelemetry-related, projects. Our… products, rather, here at Datadog, so…
**Tigran Najaryan** 03:54 Okay, you want to talk about the… what the proposal is?
**Jack Peterson** 03:57 Absolutely. So, I will open up the… so I did… I do have a Google Doc here. I don't have a issue open or implementation open yet, since it was… since a little more high level right now, and I wanted to make sure.
that I was on the right track, so to speak, and that we didn't, you know, resolve any sort of, you know, initial concerns that anyone might have prior to, you know, building something. But basically.
As, the current security model, for, op-amp being TLS, TLS-based security, the actual transport layer is, secured, via certificates, However, there's… just because the agent is receiving the message from the server, there's not necessarily a way, at least from my read of things, there's not necessarily a way to verify the actual authoritative source of the message, so something that I wrote up here and wanted to propose was a way to If the vendor or, you know, op-amp server is providing a config, or some sort of other message that the agent Or client would actually have a way to verify that this message is authentic from the… from the root certificate authority.
So that can be done via… Certificate chain.
Basically… So you can see this little diagram here, right? If you have the root certificate, that will sign an intermediate certificate, that might sign a, you know, short-lived certificate at the endpoint, and if the Each, you know, those 3 certificates being the signature.
And the, you know, public key, essentially, are provided to the agent on startup, then the agent can actually… and it's… the actual payload is signed by the… Damn.
leaf certificate, so to speak, then the agent can actually verify, great, this message is authentic all the way back to, the root. So that basically is what this boils down to, is a way to, on startup.
Advertise a capability.
of… I require… as the agent says, hey, I require payload verification.
And then… If the server supports it, they'll send back a message that says, yes, I support Payload verification, here's my certificate chain, essentially. Expect all the messages that I send.
to be signed by that LEAF certificate.
And then from there, the agent We'll be able to verify each of the message content.
is… valid and from the authoritative route. Not just since with various cloud providers and things like that, users may not actually be directly managing the certificates that they're using for TLS. It's… it provides another layer of Essentially, security or, you know, feel-good for the, client and agent to verify that this message is authoritative from the root source. What this proposal is not, it is not a way to encrypt the message traffic.
It is not a way for the server to know authoritatively who the client is, or who the agent is, and that they have not changed. Although, of course, those are still important issues. But all it is is a way for… the on startup to… as part of that negotiation, to receive that certificate chain and the agent from there on being able to verify that messages came from the root. So I'm happy to dive into any more of the details here in terms of, you know, the connection flow or proposed, you know, types of capabilities or additional fields or messages required, to make this happen, but I wanted to, at a high level.
at least get some sort of, you know, input or questions or whatever to make sure that I am… that this is something that would be… You know, useful, right?
**Tigran Najaryan** 08:25 So, a couple questions. So this… what you propose essentially finds the config and packages available messages, not other messages, right? This is specifically for the config and the… those two messages, essentially.
**Jack Peterson** 08:40 Right, for our…
**Tigran Najaryan** 08:41 assigned.
**Jack Peterson** 08:42 Yeah.
There could be other types.
**Tigran Najaryan** 08:45 Yeah.
And the idea here is that… okay, let me, I guess… in OPAMP, the authoritative source of the messages is the OPAMP server today, with the exception of the package binaries themselves, which are supposed to be signed, where the source is essentially the download server.
which can be separate from the OPAM server. What you're saying here is that You would like to have a similar separation for the configs, essentially, for the OPOM server.
not to be the trusted authoritative source of the configs, but some other server to be that, and the signature… essentially, and the certificate of that server to be signed by some sort of a CA that the agent trusts.
And has a way to verify those, those configs, essentially, the payloads.
That it receives. Is that what you're trying to do here? So, essentially, to say that I don't want to trust the OPAM server to be the source of truth for the configs, but I want to be some other separate server, essentially, to be that, to play that role.
**Jack Peterson** 09:59 Yes, correct, exactly.
**Tigran Najaryan** 10:01 Okay. I… it's, okay Okay, I guess… understood, okay. The idea, I understand what the idea is about. I think we should discuss that.
But maybe before we do that, just to set the expectations, right? So, when non-trivial proposals like this are made to all pump.
which essentially require changes to the specification, a few things are expected here, right? One is the proposal obviously needs to be technically sound, and we can have that discussion and review it, etc. The second is that The capability that he proposed needs to be wanted by the community, so we need to see some sufficient interest in that.
**Jack Peterson** 10:48 Right. And then… and would like then…
**Tigran Najaryan** 10:51 We would like to see a prototype demonstrating how the proposal works, so an implementation of it, but before you go to the implementation, I would want the first two, essentially, points to be there, right? Technically sound and wanted.
Just… just setting the expectations here, so to make sure that You know what the process looks like here, right?
As far as the proposal, I think I understand it. I will take a look. I had a very cursory glance at the document.
I can take a more detailed look and comment on it and review.
But, yeah, I think, this is as, I guess.
so far, this is all I can tell about it. I don't know what other things… others think about it, so… Any other opinions, anyone?
**Evan Bradley** 11:43 Yeah, I, I reviewed this with Jack a couple weeks ago. I think it sounds good, I think it makes sense for large-scale op-amp deployments, that maybe you want the messages to pass through an intermediary, and would want those to be, like, some way to attest that those came from a trusted source.
So I think it mostly makes sense, but, I think that you'll probably have more.
More detailed ideas there.
**Tigran Najaryan** 12:09 Is it, is it… It's a bit unusual, I think, but it may be just that I haven't had an experience like this.
I haven't seen a separation like this, where essentially the endpoint you communicate with You don't consider it to be trusted, so that whatever message you receive from it, you independently verify.
It's a bit unusual, I guess, to me, right? I don't know if there is any other prior art in other protocols where something like this is also present.
**Jack Peterson** 12:44 Right, so we actually have a, we have a current, internal, so Remote Config, product for, for Datadog, actually uses a library called, the Update Framework, which is actually a lot more invasive.
Than this, well, not invasive, but a lot more comprehensive in terms of verify that this actual message, that the hash is correct, that the length of the message is exactly the same, and that it was issued by a separate, you know, trusted authority.
And so that there are some existing And I believe that framework's actually used a lot in, like, the automotive world, right? That the, you know, head control unit actually is sending a proper message to the motor, or whatever, so your car doesn't drive off the road, right? And so there are some definite use cases out there for That, that, that type of, thing, that type of, you know.
Not trusting, blindly, and maybe separating that trust chain from the actual transport layer, security.
But I can, you know, I can try to maybe add some more info, in the background,
**Tigran Najaryan** 13:59 That would help. Yeah, if you have any links to similar protocols, any prior art, anything that… the protocol you mentioned about, would be good to take a look at that as well.
And also, one other thing I think I would want to see is what exactly is the attack vector here, right? What exactly is this preventing, and how?
what's the What's the scenario here where you… don't trust the OPAM server.
But still connect to it, and all the other messages are fine, you accept those.
But you don't trust the particular subset of messages, the config message, and what is the other one, right?
I don't… why would… then I guess, if you do this, why wouldn't you then do the same thing for all of the messages you receive from the server?
And I guess the answer to that could be that the configs are static, you could then sign them in advance, whereas most other things are dynamic, so the… The server has to compose the messages, so there's no way For… for those things to be signed by a third party.
But anyway, I'd like to maybe understand that as well.
**Jack Peterson** 15:16 Certainly. And I had only mentioned specifically the, you know, the binary and the config, because those were what I needed for, you know, my purposes, but I… it certainly could be, you know, any type of message could be required to be signed, and I discussed, you know, with, at least the engineer here I was working on it with, the potential of having a, you know, whitelist, providing a whitelist on startup of, hey, I don't need you know, I assume that all messages are going to be signed by this authority, and that, you know, I will whitelist, you know, XYZ type of messages not needing to be signed, and if that, you know, if that enhances the overall or, you know, if it makes it more generic or more applicable, or even enhances the security, that is something that could be in scope, but it was something that I specifically left out of scope in this version of the write-up.
**Tigran Najaryan** 16:13 I'm not necessarily trying to expand the scope, to be honest. I'm just trying to understand why specifically this message is, but not the others. Is it… Right. They may be… they may be actually special, right? But if so, in what way? That's what I'd like to understand.
**Jack Peterson** 16:29 Certainly. I think from my standpoint, it was just, you know, these are more the messages where You know, we're asking the… agent to, you know, apply a change to… You know, the configuration, or…
**Tigran Najaryan** 16:45 There's our…
**Jack Peterson** 16:46 These are the more…
**Tigran Najaryan** 16:46 High-risk messages, you're saying. Right. Yeah.
**Jack Peterson** 16:50 So, can I add another endpoint and start sending my telemetry to a different endpoint, or whatever, and now I don't realize that I'm, you know, shipping my data to the hacker, right?
**Tigran Najaryan** 17:02 Okay.
Okay.
**Jack Peterson** 17:08 But yeah, I would welcome any comments on the doc is linked in the meeting note. I do plan to, you know, potentially open an issue and, you know, start an implementation, but like I said, you know, I just wanted to get some eyes on it, so to speak, so I appreciate any of you.
If you have time.
And thank you for your specific questions and feedback, Tigran.
**Tigran Najaryan** 17:32 Sure, sure. Yeah, I'll try to… I'll try to take a more detailed look at the proposal, we'll comment on it.
Okay.
Anyone else, any other thoughts on the proposal?
**JM Juande Manjon** 17:51 Yes, I have. So… so this is one day… this is my second time participating in this meeting.
I'm located in Sunnyvale, California, and work at Intuitive Surgical, but I'm here for myself.
I have a couple minor topics in the agenda.
The first one is, should you mind to open it, or should you open it?
**Tigran Najaryan** 18:15 Yeah, feel free to open and share your screen if you want to.
**JM Juande Manjon** 18:19 Okay, I need to find the alchemy first. Okay.
Here we go.
Okay, so give me a second.
Alright, so, The first thing is a small PR to remove, code from the example that our logs are deprecated.
This is very simple PR, if you have time to look at that.
And the second scene is… I realized that when you, as a user, that is my case, when you run the example, if you are not in the right working directory, and the… The certificate are not loaded, and the example that didn't work.
So I have done a change, so if I open this guy… Inside this issue, you can find a link.
to the solution that I'm working on that basically is not, using relative files.
And in stealth, my proposal is embedded the files, the certificate files in the binary, so it doesn't matter where you are writing that binary, the certificate will be always available in the example.
**Tigran Najaryan** 19:46 you're… you're embedding the certificates in the binary itself at build time. Yes. I am… okay, understood. I am… I can't remember whether we do any updates to those files at runtime, though, because we are… there's a wait for the client to… Provision a new certificate from the server.
I can't remember where do we put that? Is it in some sort of temporary directory, or just in memory at all?
**JM Juande Manjon** 20:14 I think it's in memory.
**Tigran Najaryan** 20:15 In memory? Okay, so this won't affect that.
**JM Juande Manjon** 20:18 Yeah, so I think it's some changes.
**Tigran Najaryan** 20:21 Then, yeah, then I guess it's, it's fine, I don't see a problem. This, yeah, it's a… it's an improvement to the example that you don't have to care which directory you're running from.
**JM Juande Manjon** 20:32 Right, so I have a comment at the end, so what I suggest is to move the internal sets that actually is in the pan library into the example, because those are there for the example, so I don't know why we had to have a certificate in the Open Library.
**Tigran Najaryan** 20:52 just double-check that it's not used anywhere else. If they are just for the examples, then, makes sense. Yes, we can do that.
**JM Juande Manjon** 21:01 So, I should do that in this PR, or in a separate one?
**Tigran Najaryan** 21:04 You're… you're embedding the files so they won't be referenced at runtime anymore, right? So this is purely the location that could be used by the build process, essentially.
**JM Juande Manjon** 21:14 Yeah. And, yeah, up to you, I guess. You could do that in the same PR, or in a separate one.
It's okay, I would've done one to be better.
**Tigran Najaryan** 21:23 Yeah.
Sounds good to me, yeah.
**JM Juande Manjon** 21:27 Alright. Maybe one PR.
So, that's all from me, thank you.
**Tigran Najaryan** 21:32 Sure, you're welcome.
And the other one, let me take a quick look… sorry, just one second, I wanted to take a look at the other, the first one, the safe capabilities. That's, I see. It makes a call instead of using the settings.
**JM Juande Manjon** 21:48 Yes.
So… Basically, what the… the UPAN… Kinda's in the… Auto-collector implementation.
**Tigran Najaryan** 22:00 Okay.
Sounds good.
**JM Juande Manjon** 22:06 Good.
**Tigran Najaryan** 22:10 Cool, thank you.
**JM Juande Manjon** 22:11 Thanks for making the fixes there.
So, because the example is the first thing that the client is going to do to start understanding better what the Panda. So, if we have a clear example, and the sample can run anywhere, it could be good.
**Tigran Najaryan** 22:27 Yep.
I agree.
Okay.
Let's go to the next topic.
Joanna, am I pronouncing your name correctly?
**Johanna Öjeling** 22:45 Yes, thank you. Hi, I'm Johanna. I work at Grafana Labs, and I started to explore this year and made some updates in the documentation, both on the website and in the readmiss for the agent extension and supervisor and bridge.
And the documentation can be improved, further, so I started to collaborate with Tiffany from the Communications SIG, And she's working on a new architecture for the collector, and we started to think about how documentation could be improved. So, we did some initial analysis.
And I posted in the meeting document what we came up with.
first proposal, which would be to, have the, OpAMP or the collector management main page with some, overview and concepts, of what OpAMP is, and then subpages with Getting started, like, with requirement, prerequisites and a tutorial, to get the, example, server running and using, the supervisor.
And then another subpage with… Deployment patterns, explaining, What the agent extension is, and the supervisor, and the bridge, what are the capabilities, and when is each suitable.
And then subpitch for operations and troubleshooting, which could contain some common issues and how to resolve them with the supervisor itself.
And then a fourth subpage for, for developers for how to build, a client or how to build a server, So, we just recently started to work on this, but I wanted to come here and bring it up and hear if the rest of you have any thoughts around it, or any initial feedback on this structure.
Or, yeah, any ideas of what you would like to see?
**Tigran Najaryan** 25:07 So what you're suggesting is, in the collector documentation, in places where… where OPAMP is essentially relevant.
You would add, you would include all that relevant information, right? So, how do you do the configuration using opam? Is that the way you're thinking about it? So, this will be part of collector documentation, right? Not separate, topically, separate OPAMP documentation, that's not it.
**Johanna Öjeling** 25:31 No, no, so it will be part of the collector documentation.
**Tigran Najaryan** 25:34 I don't, yeah.
**Johanna Öjeling** 25:35 Today, there is a page called Management, which is quite a long page and contains some introduction, and then an example, but then… Much of the information, also.
resides in the readmiss for the different projects, so we'd like to kind of bring some of that information into UGMA Telemetry.io, and also, have a better structure, not have, like, all of the information on a single page, but create this, tree.
**Tigran Najaryan** 26:08 So, that means things related to OPAM, they will be spread across different sections of the documentation, essentially, instead of being centralized in one place.
Is that what we will see in the end?
**Johanna Öjeling** 26:23 Yeah, let me… Share my screen.
Hold on a sec… Okay, so Tiffany has been working on this, re-architecture for the collector docs.
And… Oops.
she suggested… Okay, so this is… the management is where the OPAM documentation currently lives. In the new architecture, she proposed.
To have it in… manage the collector in production, scaling and high availability, and then off them.
And what we're looking into now is to break this op-amp down.
further, so… To have these for sub-pitches.
**Tigran Najaryan** 27:49 Oh, I see. So it's… this four documents will be contained under, essentially, all pump.
heading. I misunderstood initially. Okay.
**Johanna Öjeling** 27:57 Okay, okay. Say, yes.
**Tigran Najaryan** 28:00 Okay, yeah, makes sense then.
**Johanna Öjeling** 28:06 Any other opinions or thoughts?
From anyone.
**Jack Peterson** 28:13 So the op-amp docs would just live under Collector, or it wouldn't be, like, a high-level, like, hey, this is open agent management, this is just how it applies to collector? I'm just curious.
**Johanna Öjeling** 28:26 Yeah, it already lives under collector.
So, yeah, the intention is to…
**Tigran Najaryan** 28:35 Okay, yeah. I guess those doc… docs can… they can talk about specifically how OPUMP is used by the collector, right? So they don't need to be generic anymore. They can explain here's an extension in collector you can use for OPAM, here's how you use the supervisor, etc. More specifically, how the OPAM is used by the collector, rather than being completely generic, where we don't… mostly don't talk about the collector.
That's… that's the.
**Johanna Öjeling** 29:05 Yeah.
**Tigran Najaryan** 29:05 Right? If I understand correctly.
**Johanna Öjeling** 29:07 Yeah, and then the op-amp spec page, it lives under the spec page.
**Tigran Najaryan** 29:14 Yes.
**Johanna Öjeling** 29:14 Yeah, etc, yeah. Correct.
**Tigran Najaryan** 29:16 Yep, yep.
**Jack Peterson** 29:17 Thank you, I may have misunderstood, I just wanted to make sure that that wasn't like, oh, we're gonna move the op-amp spec under the collector, and I was like, well, that doesn't make sense.
**Johanna Öjeling** 29:25 Yeah, okay, okay, I see. Yeah, not…
**Tigran Najaryan** 29:29 Okay, makes sense. When you have any drafts there, I'm happy to take a look, review the docs.
**Johanna Öjeling** 29:36 Yeah, thank you. Yeah, when we have refined it a bit further, then I can share it in the Slack channel.
Great.
Perfect. Yeah, that was it for me.
**Tigran Najaryan** 29:46 Sounds good. Thank you.
Okay.
Any other topics? Anyone?
Okay, thank you all.
Bye.
**JM Juande Manjon** 30:13 Bye.
**Andy Keller** 30:14 Bye.
