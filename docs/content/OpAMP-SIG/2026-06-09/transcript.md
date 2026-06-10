SIG: OpAMP SIG
Date: 2026-06-09
Duration: 22 minutes
============================================================

## Zoom Recording Transcript

**Tigran Najaryan** 00:33 Hello, everyone.
**Juande Manjon** 00:48 Hello.
**Evan Bradley** 00:49 Hi, everyone.
**Tigran Najaryan** 00:53 Alright, woman.
How was your vacation?
**Evan Bradley** 01:01 Pretty good, yeah.
No complaints. I mean, I just stayed home. I had a friend come into town, so we just bounced around town a little bit.
**Tigran Najaryan** 01:33 Okay, I think we can get started. We have a couple topics.
We shared.
Alright, the first one, Sean, that he, the proto… the proto-structure, yeah, just changes.
**Juande Manjon** 01:58 So, for me, it's not the problem. I restored the dot proto in the Opam Proto V1 package.
In the protobat definition, that's fine to me.
But sometimes I'm getting different signal when Opan should be independent, and now Open should follow OTRP protocol, I would like to have a clear direction about what we should do regarding to the Opinion specs.
**Tigran Najaryan** 02:23 Yeah, sorry, I may have caused confusion here. So… Yes, OPAMP is not just for hotel, but it's first and foremost for hotel, right? So we do want to keep OPAM's functionality decoupled from OTL as much as possible, and I think we succeeded in that with the spec and implementation.
The reason for that is that we want agents outside OTEL to also use OPUMP.
where it makes sense, but obviously, we're still part of OpenTelemetry Project. We don't… we don't want to ignore OTL's best practices or learnings.
On the contrary, right, we should rely on the past experience where the open clients we had with Relevant topics, namely with, how do we define the protobufs for a protocol, and we want to stay consistent.
unless there is a good reason to be inconsistent. For a situation like this, I don't see that good reason, right? So if we do the .proto or package names in OTLP.
That's a good enough, I guess, reason for me to do the same thing in OPA. It has no impact in… the… that conceptual independence of the open protocol from… from… from, let's say, open telemetry.
**Juande Manjon** 03:43 Okay, in summary, my take is, for protobar definition in a pan, we should follow the best practices apply in hotels.
**Tigran Najaryan** 03:51 Yes, the generic practices of having a protov-based protocol, yes.
**Juande Manjon** 03:58 Okay.
**Tigran Najaryan** 03:58 And that also helped us to reuse the tooling and all that stuff, everything else, right? The concepts and the mental space for people who work on both.
Like myself, to… not to try to remember what is the difference between the practices between these two repositories.
**Juande Manjon** 04:15 Right, so in this case, the 338 is 100%, compliant with OTLP, because it has separated B1 folder for the protocol.
And he has adopted…
**Tigran Najaryan** 04:27 Which we were missing in OPAM, right? So you added that to be similar to what we have in OTLP. I think that's great.
**Juande Manjon** 04:34 100%, and it's ready for review again.
**Tigran Najaryan** 04:38 Did you update it after… Yes, yes, I did. Okay, cool, great, great.
**Juande Manjon** 04:43 Yeah, two minutes ago.
**Tigran Najaryan** 04:44 I'll take a look.
Excellent, thank you. I'll pick one.
Alright, Michael?
**Michel Laterman** 04:55 Yeah, so I have the next topic, I've noticed that the Gorilla WebSocket library was used for Client and server hasn't been updated.
I haven't had an UPR in… Over… A year and a relief in over two.
So I'm investigating switching the library to coder.
Right now, the PR's rather large, because… the switches behind the build tag. Say you include the the WebSocket build tag, and it will use the new library in the transport instead of just Instead of a… Single the tonic change.
So I'd like to go over what the actual next steps for this is, and I was thinking it would be… do the same for server.
Get some benchmarking done to make sure that We're not losing any scale capacity, and then… release a version of the Opac Go Library with the bullet.
And then, in the next version.
We would switch it so that… you would restore Gorilla WebSockets with a… we would switch the default to use The new dependency, but keep.
Gorilla as a separate build tag, in case someone wants to restore.
Previous functionality and… Eventually mark the build tag as deprecated and removed it.
Sweep.
**Tigran Najaryan** 06:40 This is great, Michael. So, I didn't realize this is going to be so small in reality, in my opinion, although it seems large, but I was anticipating much bigger changes. This is great. I think we do want to move carefully on this one.
I see you added the build tags, that's great, so we should do that, introduce that as an opt-in capability first to get it tested.
widely, as much as possible, before we commit to a switch. What you said, I think, is important for us to confirm we don't have performance regressions if we use the other library. If you're doing… I think you won't need at some point to do performance testing of the existing implementation. If you could testbed running and run a comparison between the two implementations, that would be great, if you can do that.
**Michel Laterman** 07:32 Yeah, I included a… Scale test driver for the example agent, so we can at least get, Our previous work, I… Defined the ability for the example agent to be used as a scale test runner, so… We can move ahead.
**Tigran Najaryan** 07:50 Do you have the wrong results here? You don't, right?
**Michel Laterman** 07:53 No, not… not for… not on the client side, not on the server side.
**Tigran Najaryan** 07:58 reality, yeah.
Yeah.
Okay, so that's what I would recommend to have, to see whether performance-wise we're not doing any major regressions there, number one. Number two, I imagine you may have introduced some abstractions so that you're able to swap out the implementations using build flags. Is that the case in the codebase?
**Michel Laterman** 08:19 Very little. I think right now, because it's only the client, I think… It's just the, like, WS sender or WS receiver, which… we strap up… we swap out the struct based on which field type is used. Yeah.
**Tigran Najaryan** 08:38 Okay, let me take a closer look, because I only saw your very initial version, which didn't have the build flags. Let me take another look at it. We may have to break it down into maybe two phases. In the first one, we do a bit of refactoring that is necessary.
So that you can have a replacement implementation without actually having that replacement in place.
once we bring that in and merge it and test it and make sure it doesn't regress anything using… still continuing using Gorilla, then we do a second PR, which brings, essentially, an alternate implementation, which is enabled using BuildFlex. I just want to be confident we're not merging a 3000 blind PR, which may accidentally introduce some sort of a regression there.
**Michel Laterman** 09:23 No, of course.
**Tigran Najaryan** 09:25 Okay, but this is otherwise great. I think, let's have it, let's keep it in place for a while for people to test it out.
it needs to live there, I would imagine, for several months before we do the swap for default to be the new library, but thank you for working on this.
**Michel Laterman** 09:44 Okay.
**Tigran Najaryan** 09:50 Right? Anyone, any thoughts on this one?
**Evan Bradley** 09:55 I'm in agreement, this is great. I wanted to do this a long time ago, but I don't think there were any, like, viable libraries, or at least I didn't find this one. But I think in particular, what is it, the… The fact that it accepts context for reading, is alone, I think, worth the switch.
Yeah, I think it's too bad that Gorilla's, Not maintained, but there definitely are some deficiencies, so it's great to see those addressed.
**Tigran Najaryan** 10:30 Okay.
I think we're good.
Thank you. Let's see… Next one, Kelsey.
**Kelsey Ma** 10:42 Yeah, this was kind of a continuation from, what was discussed last time regarding the resource attributes. So, I opened this PR to add, piping that through the supervisor, so now you could configure it, and it'll update the op-amp extensions template to, to have it include resource attributes.
Yeah, I would appreciate if anyone could take a look at this.
and… and… I think, yeah, I also added, like, a small change for sick term, but, yeah.
**Tigran Najaryan** 11:25 Okay, Evan, can you maybe take a look at this one? I think you were… you know this piece much better than I do.
**Evan Bradley** 11:32 Yeah, no, this looks pretty straightforward. If anybody else would want to take a look before, feel free. Otherwise, I'm gonna, hopefully give this one a look, sometime this week.
**Kelsey Ma** 11:45 Awesome, thanks.
**Tigran Najaryan** 11:49 Okay, thank you.
Israel?
Bye.
**Israel Blancas** 11:57 Well, so this… this thing is actually something that I… I think in the past I came to the… to this week to talk a little bit about it.
I think that's something that we noticed while working with the supervisor on this thing is that Sometimes, right, you apply a configuration or something, right, on the agent exit, right?
And it can be a little bit difficult to know why exit, not while you are running the thing, right? And, well, it crashes, or whatever thing. More like something while the… aging, it's starting, right? Like, let's imagine a bad configuration because something is not there, or let's imagine that you are using, Distribution with a component that is not… it doesn't have a component, right, that you are specifying in your configuration or something like that. Things like that kind of things, right? When you are checking the logs from the supervisor, it's not easy to know what happened, right? Because I… I don't remember exactly what you will see, but it's like, you will see something just like exit code 1 or something like that, right? Not… not getting exactly what's happening, right, on the… on the side of the agent.
In those days, what we found is that Well, you had to go right to the host.
And check the log that was quoting, writing, writing the… the… In the host, right? The file. Because it's like you don't have any information, right, from the side of the supervisor or anything.
So, I would like to… to… something that we would like to have, I even send a PR, so… but if there is something that… better ideas, or whatever that you think that can be applied for this case, we are open to that.
Oh… to maybe something, one idea that I got was to check, right, like, using the pass-through, mechanism that the supervisor provides.
like, to check, right, the… what happened in the logs, right? Or maybe even reading from the agent.log, or whatever.
When there is a… And I normally ride in the exit of the… of the agent.
And with that, we will be able to send something in the open message, right? Saying, hey, this happened, right? So, in the backend, you will be able to have… Something?
to work with, right, and know what happened to the agent.
**Tigran Najaryan** 14:36 Okay, I think I understand the pain, but we also need to be careful with It is not turning the supervisor into a log collection agent, right? So, there's a fine balance to hit here. I'm… I'm forgetting what exactly do we do, Evan, when the collector process exits with a failure. How do we report it to the server? In what form?
**Evan Bradley** 15:00 Ready Cruz.
**Tigran Najaryan** 15:00 Results in an exit code being reported?
Do you remember?
**Evan Bradley** 15:03 it would either be… I mean… It would either be component health or the, agent… or what do you call it? The remote config apply status.
I'm not sure off the top of my head. My… I mean… so, both of those messages have, like, string error message, fields in them.
I think we could probably tail, like, the last line, or maybe the last couple lines.
Because I agree, we don't want to turn this into a log agent where you have, like, a, you know, a gigabyte, size string.
**Israel Blancas** 15:38 No, yeah, yeah, we can limit, or even, if you think that you want to do it more flexible, right, something that can be configured, or… I guess just establishing a limit, right, a hard limit, like, I don't know, the last 10 lines… lines, or whatever ride will be… will be more than enough.
For having that. But yeah, it's like, currently, there is that pain, right? So we don't have a way to… To swap out, right?
**Tigran Najaryan** 16:06 So, yeah, I think it's… it's a good idea to see if the res… if whatever we're… I'm not remembering exactly what is the message that we're sending on this failure. If there is an error message field there for us to use.
And we're already tailing the logs, somehow they are… Where, if the supervisor is, is watching those.
We could do what you said, might include the last.
Whatever number of bytes there, as an error message, or something like that.
So, somebody has to go and look at what exactly the supervisor is doing right now, and what's the way to modify that? Make a concrete proposal.
**Israel Blancas** 16:46 Yeah, that is… that is what I am doing in the… in the PR, right? I don't remember.
**Tigran Najaryan** 16:51 Where is… do I have a PR linked here?
**Israel Blancas** 16:54 Oh, yeah. Yeah, yeah, it should be, it should be linked on, like, in the last… I can link it to the, to that one.
**Douglas Camata** 16:59 At the top there.
**Israel Blancas** 17:00 today. Yeah. Is there…
**Tigran Najaryan** 17:02 This one?
**Israel Blancas** 17:04 Yo.
**Tigran Najaryan** 17:04 I see.
**Douglas Camata** 17:05 By the way, today, the supervisor will just log Agent exited.
Unexpectedly, with exit code, this one. This is the only thing that the supervisor puts in the remote config status when When it reports a failure.
So, no exit code, and nothing else, so it's… It's pretty much useless today.
**Israel Blancas** 17:31 Yeah, and something that also can be, like, maybe an improvement, I remember that I created another PR at some point, right, related to this.
Was, like, you know, you're gonna get the exit code, right?
sometimes even it's not… it's gonna… it's not gonna be able to start the agent because of something like, I don't know, too many open files, or whatever things, right? You know?
For different, systems. So maybe even providing, let's say, ununified, right? Or, or something, like, more context about what that… exit code means, right? That sometimes you can provide just based on… on the documentation from the different operating systems, right? Or whatever. Because it's not the same… let's imagine that you are running agents, the same configuration across Windows and Linux, for whatever reason, right?
and you get, exit code 1, right? That will mean something totally different.
Very likely on Windows and in Linux, right? Things like that.
**Tigran Najaryan** 18:30 So, the question I have is, what do we do if the collector exits unexpectedly? Not because we're applying the remote config, but for whatever other reason in any other state.
We would not have a way… if we're not in a state when applying the remote config, where there is an expectation to send back the remote config status as a message, we won't have that medium for us to use the error field. So what do we do in that case, is an open.
**Israel Blancas** 19:01 Oh, shit.
**Tigran Najaryan** 19:01 Ben.
**Evan Bradley** 19:02 We, we actually do. I'm looking at it right now. We send component health messages regardless on a space.
**Tigran Najaryan** 19:08 Okay.
**Evan Bradley** 19:09 the same thing.
**Tigran Najaryan** 19:09 Okay. Okay, cool. So we have… we have a way to generally report a bit of additional information when something bad happens with a collector, essentially.
**Evan Bradley** 19:19 Right.
**Tigran Najaryan** 19:21 Okay, I mean, conceptually, it makes sense to me to have a bit of extra information included, if we have that available to us, and it seems like if we're doing the pass-through of the logs, then… should be readily available, so not a big deal to include. I don't know why we have this much code there to do that. I would expect it to be easier to do, but maybe there's a reason.
**Israel Blancas** 19:41 Yeah, I tried, this, this is actually, I ported to the current state of the repository, so all PR that I created, right? Where I was trying to… to get that information, but maybe if you think, after reviewing, right, if you think that it's trying to do too much stuff, I will be okay with simplifying that.
Because, well, at the end of the day, right, if we are able to do that.
It would be great.
Yep.
**Tigran Najaryan** 20:08 Okay, yeah, this needs a redo then.
**Israel Blancas** 20:11 Okay.
Thank you.
**Tigran Najaryan** 20:17 Okay.
And… Okay, again, about the produce? Yeah.
**Juande Manjon** 20:26 I have another entry, yeah, so, because we want to follow, OTRP… OTRP actually is publishing their protocol into a public repository, where all the applications can automate and load the protocol definition and documentation. So if you follow the link, you will see that the whole OTL schema there, I think it, as part of my next PR, where I want to add a linter and a breaking chain tool to validate that the opine spec followed the best practices, like, for example, lower camel case for field names and upper camel case for messename, and so on.
Also, it's optional, but we can also publish the OpenSpec proto in that public repository.
**Tigran Najaryan** 21:19 Yeah, and that's what we're doing for OTLP, so I like that let's borrow whatever… whatever is the tooling there is, if it's calling buff registry, like, that does buff tooling directly, or maybe we're using Docker images for that, if I remember correctly, so we can just borrow whatever OTLP is doing there, but yes, I think it's a good thing to do.
**Juande Manjon** 21:38 I will try to address that after 338 is complete.
**Tigran Najaryan** 21:44 Great, thank you.
**Juande Manjon** 21:45 Yeah. Alright, that's all from me.
**Tigran Najaryan** 21:49 Okay, that's all we have in the agenda. Anything else, anyone?
Okay, thank you all.
**Evan Bradley** 22:09 Bye, everyone.
**Tigran Najaryan** 22:10 Bye.
