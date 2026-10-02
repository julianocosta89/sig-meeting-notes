SIG: Arrow SIG
Date: 2026-10-01
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Drew Relmas 00:00:31 Hello, good morning, folks.
Aaron Marten 00:00:35 Good morning.
Gokhan Uslu 00:00:44 Good morning.
Pierre Mariani 00:00:58 Good morning.
Drew Relmas 00:01:03 I see Laurent has put in agenda items, but he's not here in the meeting yet.
Laurent Querel 00:01:26 Hello, everyone.
Drew Relmas 00:01:28 There. Hey, Laura.
Laurent Querel 00:01:30 the.
Drew Relmas 00:01:34 Truth.
Laurent Querel 00:01:51 I can share my screen today. Hi, Joshua.
Joshua MacDonald (Microsoft) 00:01:55 I would… Be glad to share my screen.
I thought.
Laurent Querel 00:02:03 I was saying that I can share my screen.
Joshua MacDonald (Microsoft) 00:02:05 Oh, sure. I thought I was having a network problem. Only one browser is having a network problem. Good morning.
Laurent Querel 00:02:12 Enrolling you in.
Okay…
Joshua MacDonald (Microsoft) 00:02:19 Since we were all together in a meeting.
Laurent Querel 00:02:21 Indeed, I didn't read, to be honest, the… the… A summary of the last week.
Windows Event Log Receiver, Receiver, Login, Binary.
Oh, that that I need to read.
What applied view centralized transport ID?
Joshua MacDonald (Microsoft) 00:02:41 I would say the last few meetings have just been kind of smooth summaries of all the open issues and, like, open discussion around them. I feel like we've been through a few glitches because the sort of standard boilerplate for our meetings, the triage section, has these links to needs discussion and labels stale, but we've noticed that because Especially when maintainers create issues, they end up being auto… automatically accepted, and so they don't show up in needs discussion unless we bring them.
Laurent Querel 00:03:11 Mmm.
Joshua MacDonald (Microsoft) 00:03:12 So, if there's an item that someone creates that they want to discuss, it's been missed a few times, and so I kind of want to just go through fresh issues, which neither of those links takes us to.
Laurent Querel 00:03:24 Okay.
Joshua MacDonald (Microsoft) 00:03:26 I'm.
Laurent Querel 00:03:27 So I already opened.
in the order that we have here on the, in the triage section.
Joshua MacDonald (Microsoft) 00:03:34 Right, and I have changed that link, so we'll see if it works today.
Laurent Querel 00:03:38 Okay, so this one is the first one.
Then we have the cell, and then we have… I think this one is a mix of multiple things.
Because I read… I can see some of the elements that we have here.
Priagene discussion… And, I think I saw… I don't know. We'll see. Can we start?
Joshua MacDonald (Microsoft) 00:04:15 Yes, I think we should start.
Laurent Querel 00:04:17 Okay.
Joshua MacDonald (Microsoft) 00:04:18 Hello, everybody.
Laurent Querel 00:04:19 So, we are here on the list triage need discussion.
So, we have the first one, OTAP logs view, silently exposed, exposed map and array log bodies as empty. Looks like a bug.
Do we have Bandu with us, maybe to briefly, Think about that.
Drew Relmas 00:04:44 Not.
I think, but I've… I think I had spoken very briefly, maybe to him and to Josh or Albert about this.
I'm trying to recall, I think we've just never had… Anybody have an explicit use case for non-regular string bodies?
Joshua MacDonald (Microsoft) 00:05:05 Is there a pull request attached to this already? I feel like…
Drew Relmas 00:05:09 I don't think…
Albert Lockett 00:05:11 advice.
Drew Relmas 00:05:12 there.
Albert Lockett 00:05:12 Yeah.
Joshua MacDonald (Microsoft) 00:05:13 Yeah, I thought I saw one, too.
Albert Lockett 00:05:14 Heroes.
Laurent Querel 00:05:15 Yeah.
No, that's not the, oh, maybe this one.
Albert Lockett 00:05:19 Okay.
Laurent Querel 00:05:20 Good map and slice, throw in emerge.
Joshua MacDonald (Microsoft) 00:05:23 And then…
Drew Relmas 00:05:24 Might already be fixed.
Joshua MacDonald (Microsoft) 00:05:26 There's one connected from Pratish, I think, that's open about accessing the CBOR values from the transformer.
Drew Relmas 00:05:33 That's different. That's in transform. This is the actual view itself, right?
Albert Lockett 00:05:38 I think this is… can you click on the… on the files change there? I think this is done.
Laurent Querel 00:05:44 Yeah, I think it's done here.
You can map and slice long record bodies from the CBRO cell column instead of Rutan EMT.
So, structured lung bodies are no longer suddenly dropped.
In the log view… in the other views.
Yeah.
Albert Lockett 00:06:01 Yeah.
Drew Relmas 00:06:01 Yeah, I guess this is done then.
Laurent Querel 00:06:03 Yeah, so we… let's do that.
Okay, great.
So… It should be marked as fixed.
My brain is not okay.
Joshua MacDonald (Microsoft) 00:06:22 4134. Cool.
Laurent Querel 00:06:25 41… 44.
Joshua MacDonald (Microsoft) 00:06:27 4.
Laurent Querel 00:06:29 That's it.
Okay.
Joshua MacDonald (Microsoft) 00:06:32 34. Well, anyway, moving on.
Laurent Querel 00:06:35 44, you said.
Joshua MacDonald (Microsoft) 00:06:36 34.
Laurent Querel 00:06:37 Oh, 30, I'm sorry, my brain is not yet fully operational.
Close this comment. Okay, great. Let's go back.
Implement component inventory, macro, attribute macro.
I think…
Drew Relmas 00:06:53 So this had been marked done, but I reactivated it, and I had a comment down at the bottom. I would love us to come… we had discussed it earlier, I would love us to come back to stability level.
And start doing that as part of component inventory. We had discussed it, and I think it got kind of glossed over in the first…
Laurent Querel 00:07:14 Yeah, she's good.
Drew Relmas 00:07:19 So, there was also an abandoned… a random first-time contributor had started trying to classify some of the nodes, but I think the PR was abandoned and never came back to. But, it should be as part of component inventory rather than just in the README docs, you know.
Laurent Querel 00:07:52 Okay, just notifying David, I'm sure he will be happy to… And this stability level makes sense.
Okay, structured security repo, Arnes.
Joshua MacDonald (Microsoft) 00:08:11 This one, we've been punting for weeks and weeks and weeks, and I asked CJO about it, and I have a feeling Well, he's not here today, we might… Want to just kick it back to him for more information.
Which we keep doing. And I can ask again.
Drew Relmas 00:08:29 You can… we have a Needs More Info, tag, as well.
Joshua MacDonald (Microsoft) 00:08:34 Yeah, I guess that's the right… that's the right approach. Kick it out of this list for first, yeah.
Meetings info.
Laurent Querel 00:08:43 Need info, okay.
Joshua MacDonald (Microsoft) 00:08:47 If you… okay, I'm gonna go fix it.
Laurent Querel 00:08:50 Let me, what do you want to.
Joshua MacDonald (Microsoft) 00:08:52 I'm gonna remove needs discussion, so we don't see it in this list.
Laurent Querel 00:08:54 Yes.
Indeed. Thank you.
Okay…
Joshua MacDonald (Microsoft) 00:09:03 And then the bottom…
Laurent Querel 00:09:04 And this one also need to… because we…
Joshua MacDonald (Microsoft) 00:09:08 didn't.
Laurent Querel 00:09:08 Defied.
Joshua MacDonald (Microsoft) 00:09:09 Oh.
Laurent Querel 00:09:11 Because this one has been discussed and we just notified David, so I just forgot to remove the need for discussion.
Joshua MacDonald (Microsoft) 00:09:18 Got it.
Laurent Querel 00:09:20 Okay, why it's still there? It's just a refresh issue. Yes, it is.
Centralized transport optimized ID were the… OTAP logs views assume OTAP Arrow ID column are already decoded before it being scoped in the attribute indexes.
Joshua MacDonald (Microsoft) 00:09:47 I feel like I've seen a few PRs try to… rationalize the transport ID encoding, and I never have known where that stands.
Laurent Querel 00:09:56 Yeah, I think I didn't read the entire description there, but I think that's Definitively, an additional sign that we need to to improve the PDATA interface. I think we all agree with that.
Albert and, and Jake, I'm sure that you also agree with that.
I bet did you read this one?
Albert Lockett 00:10:24 No, not yet. I'm aware of the issue.
But, but I haven't read this yet.
Laurent Querel 00:10:31 Okay. And do you agree that.
When we have time, we need to, yeah, to to look at the Pdata interface and And make it more… Type safe, and… remove any possible misuse of the… So, we should not be in a position where, if we forget to optimize the ID, We don't know as we had been.
Albert Lockett 00:11:02 Yeah, I agree that we should do that when we have time.
Laurent Querel 00:11:05 Yes, okay.
Okay.
And then, Jake, one week ago, I think there is actually some room for further design discussion here.
Joshua MacDonald (Microsoft) 00:11:21 Ben's here now. Ben opened the PR that we see linked, 4131. This is why it keeps coming back, and it maybe never gets solved.
Laurent Querel 00:11:30 Okay.
Yeah.
Joshua MacDonald (Microsoft) 00:11:33 Ben, do you have any thoughts?
Ben Du 00:11:36 I think my main thought was I was testing out, the OTAP endpoint to Azure Monitor Exporter, and it wasn't working due to this, and… This, ID, and so I was trying to figure out how to fix… To make it work.
That was most of my motivation.
Laurent Querel 00:11:59 Yeah.
So, Ben, I think we… If you want to fix that, I encourage you to talk with Albert and Jake.
The goal being to… Definitively… I mean… You could focus only on this issue getting the transport optimized ID.
But, we need to be in a position where at some point where the P. Data could not be misused like I mentioned.
And, and what you just explained is a misuse, but we should not be in this position. You should not be able to do this kind of operation.
So there is an issue into the API.
So we need to find the right balance between.
type safety and good use and performance. I don't have the… The right guidance to define what needs to be done on this interface right now.
But that's the the design principle behind it.
Ben Du 00:13:11 Okay, yeah, that sounds good.
Laurent Querel 00:13:16 Okay, great, this one is done. No, sorry, I need to… Do my job.
And… now… We are good.
I don't know why it's in there.
Joshua MacDonald (Microsoft) 00:13:37 There's a invalid filter in your list there.
EESWC, which is not helping, but…
Laurent Querel 00:13:45 Okay, so…
Joshua MacDonald (Microsoft) 00:13:46 Move on, and I can follow up and adjust labels if you'd like.
Laurent Querel 00:13:50 Perfect.
Okay, so now it's about the scale issues.
Windows networking, multi-threaded consumer support. Yes, I remember that.
Joshua MacDonald (Microsoft) 00:14:03 And I have…
Laurent Querel 00:14:04 a long time ago, I think it's still something, I guess, we need to… we want to address, right?
Joshua MacDonald (Microsoft) 00:14:12 Yeah, I… yes, it is. I don't see either Karsh or Lalit here, which I would ask to talk about it, but it's definitely still an issue that we're tracking.
Laurent Querel 00:14:23 Yeah.
Joshua MacDonald (Microsoft) 00:14:25 I'm gonna remove stale. Why don't you move on?
Laurent Querel 00:14:28 Okay.
Autogenerated telemetry documentation.
I think we have Andreas with us today, right?
Oh… Baby notes.
Joshua MacDonald (Microsoft) 00:14:41 He was here a second. He's here. Yeah.
Laurent Querel 00:14:44 Okay.
Joshua MacDonald (Microsoft) 00:14:45 Andres, if you'd like to speak, I know that the request is pretty straightforward, and we've now introduced a metadata.yaml file, so we're, like, one step closer.
And I have watched people updating docs and thinking, it's time to do something about this.
Andres Borja 00:15:03 This is super old.
Joshua MacDonald (Microsoft) 00:15:06 The Increasingly important.
Drew Relmas 00:15:11 How does this relate to Weaver?
Laurent Querel 00:15:14 Yeah, that's also my question. We should use semantic convention and not the metadata files.
And, and I have, unfortunately, one of those, multiple, branch open.
In my, fork, solving that.
And I'm sorry I didn't have enough time to… Absolutely.
Joshua MacDonald (Microsoft) 00:15:40 Was that the large import of a bunch of new Weaver content?
Laurent Querel 00:15:44 It's one where, I basically… use an LLM to extract all the instrumentation we have in order to generate a semantic convention.
That correspond exactly to… All the events and metrics.
And I posted, I think one month ago, a diagram representing all the… all those signals, with an SVG graph and so on.
In my opinion, that's the right way to go, because then we can use Weaver into the CI pipeline.
And understand the coverage.
Of the unit test and integration test.
To see how much signal have been triggered.
And then we can… we can set up some, special, say, okay, let's say… like we… we are doing for the… in general, for the test coverage. Let's try to reach 80% of the coverage for the instrumentation.
That's what River would give us. And the second step, was… the creation of an optimized and dedicated, and type-safe client SDK that will be generated from the semantic convention file.
And then we can use this API to basically report events and metrics.
with, An additional, so definitively with an additional, Protection in terms of, usage.
It will be also easier to discover, because directly into your IDE, you will see the… The API will be, Explicit, all the events are there, all the metrics are there.
And you can't report anything that is not there.
And.
I can't prove that, but I think we will get a slightly better performance for the… for the instrumentation. Not big, but because we already did a lot of work to To make that, super efficient.
Yeah, so for me, that's… Then, once we have Weaver, then we can auto-generate the documentation with the template system that Weaver integrates.
Yeah, I will strongly recommend to follow this path in my opinion.
Joshua MacDonald (Microsoft) 00:18:09 So, to summarize, the plan will be that we begin generating instrumentation As well as documentation.
Laurent Querel 00:18:19 Yes.
Yeah.
Joshua MacDonald (Microsoft) 00:18:23 And would we move away from the macros that, that we've been building on recently?
Laurent Querel 00:18:27 Just,
Joshua MacDonald (Microsoft) 00:18:28 center.
Laurent Querel 00:18:28 Yes, but there is, like, a progressive path to go there.
I think the first thing is to generate the.
to generate the semantic convention. Then we can generate the documentation.
And, basically fix this request.
And And put in place in the CI pipeline the coverage.
And then, last step, we generate a client SDK, which is TypeSafe.
And then we integrate this client SDK typeset client SDK.
directly, we replace the instrumentation everywhere into the code. So it's a long, long journey, but I think at the end, we… we are basically proving many things.
Joshua MacDonald (Microsoft) 00:19:17 I imagine at that point, our OTAP, we can directly write OTAP, maybe for the metrics. That would be nice. Yeah.
Laurent Querel 00:19:23 Yeah, yeah.
Joshua MacDonald (Microsoft) 00:19:25 Alright, not stale.
Laurent Querel 00:19:27 Not stylistically. So you said that you will.
Joshua MacDonald (Microsoft) 00:19:31 Yeah, I'll make…
Laurent Querel 00:19:32 That's okay. Centralized runtime version with build time.
Oh, I think… I was thinking that we fixed that, or maybe not.
Joshua MacDonald (Microsoft) 00:19:52 Gokhan is with us.
We could ask him to summarize.
Drew Relmas 00:20:02 This is also a pretty old one from March.
Gokhan Uslu 00:20:07 Yeah, let me just peek at it to remember. I remember what it was, but I want to remember the full context of it.
Laurent Querel 00:20:15 Yeah, no moon.
Gokhan Uslu 00:20:17 you.
Joshua MacDonald (Microsoft) 00:20:24 At a high level, I'm seeing something I'm familiar with, which is it's Tricky to set a version.
in our code, because you have to set it in a bunch of cargo tunnels, and and I don't know, there's never been a great integration with version control systems that I'm happy with that will automatically fix this problem.
Yeah, so…
Gokhan Uslu 00:20:45 So this is to be able to figure out what the DF engine version is.
Laurent Querel 00:20:55 And now that we have released, that's.
Because I think we… I mean, release are recent.
Gokhan Uslu 00:21:02 Actually, sorry, sorry for interrupting, but… So, I think part of it is possibly also being able to set the build version when we're building. It's… it's been quite a long time. Maybe Drew also remembered. It was about, one of our internal builds as well, that we were… we needed to… be able to… Set the build ver… like, set a version for the binary that we are building.
Drew Relmas 00:21:37 I don't recall off the top of my head, but I don't think we have any outstanding Oh, the fact that we did… Okay, the telemetry resource service diversion.
Or Azure Monitor Heartbeat version.
I mean, I think we satisfied whatever our internal use case was for this.
Gokhan Uslu 00:21:57 Yeah, so, okay, so I'm remembering. We needed the version of the current running DF engine when we are in the runtime.
Yeah, yeah, that was it, I think.
So that we can then send the version information, say, as part of the… you know, telemetry, right? So, we are, we are, soft telemetry, reporting soft telemetry, but what is the version of DF Engine we are running?
Laurent Querel 00:22:27 This is the version, right?
Joshua MacDonald (Microsoft) 00:22:33 Right, I think what we're asking for is a way to auto-populate some sort of attribute.
Laurent Querel 00:22:37 Yeah, and I think we need to revisit this entire thing, especially now that we have the release system.
We should have the release aligned.
I mean, the version, the service version, aligned with the corresponding release.
Albert Lockett 00:22:57 I.
Laurent Querel 00:22:57 And I think we need to be able to do that also.
That's why I like the… the… We can put this back to.
Joshua MacDonald (Microsoft) 00:23:09 needs info, I think. Albert has his hand up.
Albert Lockett 00:23:11 Yeah, can I just point out that I'm pretty sure we had a PR from.
Matthew at Dash Zero that at least, like, partially resolves this. Like, I think what was added was we now have, as part of the controller runtime options, a build info.
Struct, and that gets, automatically populated with, the… the cargo PKG version when you built it, and then I thought that in our internal telemetry system, we had some capability to specify… yeah, there's the link. I thought that we had some capability to specify, like.
use… service version, either from, like, BuildInfo, or.
From, like, a… detection of the service version using the OpenTelemetry SDK.
So, like… you know, I, like, just throwing it out there that I think that, like, you know, as we… Again, if we're gonna add, like, needs discussion on this, like, just knowing what has already been done would be, probably useful as part of the, informal.
Joshua MacDonald (Microsoft) 00:24:31 the.
Albert Lockett 00:24:31 The.
Joshua MacDonald (Microsoft) 00:24:32 Matt's PR in the issue. I think we need a bit more info, but we should move on, or we're gonna run out of time today.
Gokhan Uslu 00:24:41 Okay.
Laurent Querel 00:24:42 I'd just like to mention something on this one.
We have to take into account that We need a solution that will work well. Now that we have a release. In my opinion, we should make sure that it's the release version is used.
And second… We need a way for people that are creating a binary that is not the default one.
Like we do, and like I think Microsoft is also doing. So we should be able to, to underwrite also this, service version.
When we import the crates. So we need a solution that is working well for embedded solution.
And the open source solution.
Gokhan Uslu 00:25:26 Yeah, so just to add a slide more to it, it would be, like.
For us, when we look at internal telemetry, what matters is the version that we built, for example, the image that we built, and that, is running a specific version of DF Engine, but for us, for example, image version is actually more telling than the DF engine version. So, when we build the binary, and when we call the… give me the version information of the runtime, that should be the version number. Just be able to arbitrarily set a version number when we're building, basically, where a macro gives us, then, that information to you later, or something like that.
Laurent Querel 00:26:08 Yeah.
Yeah, we have the same kind of, request on our side. Okay, evaluate duplicating sender waiter machinery between. Oh, that's for me.
I don't remember this one track follow-up work to evaluate whether the sender Need to double check that. I think it's… I think that has been fixed, but I'm not entirely sure.
Okay.
Joshua MacDonald (Microsoft) 00:27:28 I recently asked someone in a PR to avoid duplicating a channel reimplementation. It was one of Tom's PRs. We should definitely try to avoid duplicating code in this codebase. It's becoming more and more of a problem.
Laurent Querel 00:27:41 Yeah, I agree. Shut down orchestration and message channel redesign.
Gokhan?
I think that has been…
Joshua MacDonald (Microsoft) 00:27:55 It's nice how these stale reviews remind us what we were doing six months ago.
Gokhan Uslu 00:27:59 I actually remember this one, so… We were talking about it with Joshua, if you remember, so the thing was, To make it so that.
there was no data loss or whatsoever when we were, for example, shutting things down. And then we decided… we thought that two-phase shutdown probably would be the Way to go. So… Well, because the receivers need to first shut down, and then the processors, and then exporters, but, to… meaning, like, they need to stop receiving data, like, accepting data, and then afterwards.
We need to drain exporters that, and then… Okay, so the whole thing is written there, but it's been a very long time, but the idea is to not lose any data, and have a deterministic shutdown sequence that enables that, basically.
Laurent Querel 00:28:59 Yeah, but don't you think that, because I remember around this time, I was also working on that.
together, we were working on this, this problem, and I think I fixed the issue with the new inbox, system.
We can double-check, but I'm relatively confident that we…
Joshua MacDonald (Microsoft) 00:29:22 Yeah, this sounds fixed. At least I remember the.
Laurent Querel 00:29:25 just.
Joshua MacDonald (Microsoft) 00:29:25 To drain receiver.
Laurent Querel 00:29:27 I can also check that, or you can check that, Gokhan, if you want, but I think we can move on and just add.
some cinematic.
Gokhan Uslu 00:29:39 Yeah, I want to look into it a little more, because I have a hunch that it wasn't fully addressed, what I'm trying to get out of this one.
Yeah, but yeah, we can maybe look, talk about…
Joshua MacDonald (Microsoft) 00:29:52 Back to triage accepted, and we can come back to it in 6 months if nothing happens.
Gokhan Uslu 00:29:57 No, or add more… needs more info, or something like that, so that I can get…
Joshua MacDonald (Microsoft) 00:30:02 That's… I mean, accept and have more info on it. Very good.
Gokhan Uslu 00:30:06 Okay.
Joshua MacDonald (Microsoft) 00:30:07 Right.
Laurent Querel 00:30:09 Okay, so I think we… we are done with this list.
Yes, let's move on on this one.
Which is the… the new… Okay, we… you see, we see again the salmon trees in this list.
Because that has been…
Joshua MacDonald (Microsoft) 00:30:33 I'm marking them accepted right now. We're still deciding.
Laurent Querel 00:30:37 Oh, okay, okay, okay.
Joshua MacDonald (Microsoft) 00:30:39 I'll fix the one.
Laurent Querel 00:30:39 Okay, support capability adapters and derived capability binding. Do you want to talk about that, Gokhan?
Gokhan Uslu 00:30:53 Yeah, so this is just a thought that I had to quickly put together yesterday.
And it's one possible solution, and I'm open to, you know, thinking and exploring other things as well, but what I'm thinking is that One of the issues that we have with the capabilities is to be able to actually say, okay, this is the capability that you have for a node, meaning, like, you do basic auth, you do… Sasol, stuff like that. Or, And the other thing is that these capabilities, because they need to be implemented by providers, if they're providing very, very similar functionality, like, almost so that they are same, but the differences is just maybe how they're delivered, or how they're packaged, or whether they're enhanced with additional logic that is related to the RFC of that specific Function, or something like that.
a provider, such as someone who writes an extension, they would need to implement the same thing almost multiple times, just so that they can provide different shapes of the capability. So what I was thinking is that maybe one of the ways that we can improve the reusability of the capabilities is Say, for, in this example, for example, basic, odd, could be, like, username, password, maybe it has an expiry date or something, and then it could also be, having helpers to, you know, basics, basics for encoded, but at the end of the day, it's just username and password. So, a capability that can, for example, provide username and password Could be the basis of this basic art capability, and then we could then see, like, create higher-level capabilities that are using those lower-level capabilities with some added function to it. And then.
Those high-level capabilities wouldn't need to be implemented, because the lower-level capability provides everything that high-level capability that it needs. So, username and password capability then could be used to create basic auth capability, just basic object-oriented programming, basically. So, just to be able to
Laurent Querel 00:33:18 So you want a shared implementation reusing the low level?
capabilities.
Gokhan Uslu 00:33:27 Yeah, like, being able to create, maybe, virtual capabilities or, like, capability adapters as capabilities, again, that uses other… use other capabilities. So, a username and password can be implemented once, but then Could be provided in 5 different shapes to different consumers, something like that.
Laurent Querel 00:33:50 Yeah, I think I understand.
Joshua MacDonald (Microsoft) 00:33:52 It doesn't sound like a bad idea. It also doesn't sound, like… it sounds like an implementation detail, maybe, that only you are going to really appreciate Gokhan. I don't think anyone would object.
Yeah, David.
Gokhan Uslu 00:34:06 So, yeah, so the thing is that We need SASL, for example, authentication, that's a concrete example. We need, basic auth. We need also just username and password, which has recently come up with this Oracle receiver implementation.
They basically all can use username and password, and I'm just trying to solve that problem by creating.
Joshua MacDonald (Microsoft) 00:34:33 This is because I had requested, like, the fourth PR for the Oracle receiver added a bunch of, like, password… username and password management code, and I had just reviewed Michael's change that added the same extension, so I was asking them to use the extension, and the blemish there is that the only extension we have right now for username and password is the basic auth extension, which makes it look like you're asking for HTTP auth when you're just asking for a username and password.
And… I don't think it's a great big problem, but I think GoCan's just basically describing a better solution.
Laurent Querel 00:35:12 Is it really that? Yeah, I think this one need to be.
I don't think we will be able to review entirely this request now. I think we need to read that carefully, and the risk I see, I mean, it's probably good. The risk I see is adding too much complexity into our entire system.
So we… I think that's typically the… the type of requests where we need to create an RFC.
And and having a review A deep review from multiple persons.
Gokhan Uslu 00:35:49 Yeah, so other things that… thoughts that I have is that I… accepting the code application, because AI can manage it now, AI can handle it very easily. So, what I'm saying is that, code application isn't necessarily really bad anymore.
What an extension that will offer needs to do is that, hey, look, implement this capability.
As well. And then… you know, then boom, bam, it's there. So, like, maybe we don't need to create more complexity to solve this problem, because capability names also need to be semantically somewhat accurate to describe what capability it is bringing. You cannot just say, for example, say.
secret provider capability, and then you don't know what it is doing. Is it bringing username, password, or what else is it doing? So… It kind of helps a little bit to have, The name of the capability to define what it is doing, despite the fact that it is a very, very similar thing that it is doing.
Joshua MacDonald (Microsoft) 00:36:53 Yeah, so I've added that we think this might need an RFC just to, like… it's not enough detail for us in this moment to evaluate, but it does sound like an improvement to me.
Gokhan Uslu 00:37:02 Okay.
Laurent Querel 00:37:05 Okay, next one. Add snapshot watermark support without column tracking.
Interesting.
Then…
Joshua MacDonald (Microsoft) 00:37:16 I… I don't know that we should go through every single issue, or we'll run out of time again.
Laurent Querel 00:37:23 Yeah, okay.
Joshua MacDonald (Microsoft) 00:37:24 Maybe if this is an interesting one, Ben, go ahead. Otherwise, we should skim through and find the more interesting ones.
Laurent Querel 00:37:31 So let me see.
Andres Borja 00:37:34 Let's try it accepted, so I'm not sure if it should…
Joshua MacDonald (Microsoft) 00:37:38 And I just removed that one, context entries, let's just… that's a… that's a sub-issue for my epic.
Laurent Querel 00:37:43 Okay, okay.
Joshua MacDonald (Microsoft) 00:37:43 I.
Laurent Querel 00:37:44 I was thinking…
Joshua MacDonald (Microsoft) 00:37:46 over the last week, what I would like to discuss is, a sort of trend towards larger and larger PRs, which is becoming unsustainable. I feel like we're almost normalizing this, and when I'm looking at this list here, I would say.
Well, it keeps changing.
the… some of these issues are just describing, like, a 10,000 line PR that we need to do, and I'm worried about 10,000 line PRs right now.
So… But I don't see any particular issues that are going to… elicit my discussion that I want. I think we should talk about the ones that are tricky and bug-related. So, I'm looking at the one here, which is OTLP protobytes metrics incorrectly handles multiple one-of protobuf fields. I know we have Pierre here with us. I thought that one might be one that we should discuss next.
Pierre Mariani 00:38:44 Hey, good morning, everybody.
Yeah, so the context is, I was working on, an iteration on non-items for OTLP protobytes that triggered a discussion into validating that the implementation was doing the right thing on.
ill-formed, metrics, portable bytes payload.
And based on my manual testing, it sounds like the current main branch yeah, the current main branch, PData, OTLP protobytes.
is parsing the bytes and stopping at the first found one-off field instead of the last one.
We use those fields in 3 locations in the matrix object. It's part of the data field of the matrix, 3 or 4 levels down.
It's part of the exemplar field, and it's part of the value field of, some number data point object.
So… yeah, so Falderberg, I think the… you know, the major part of the work is to find a good way to test this in unit test.
Which I'm looking at right now, as part of my original work, so I'll have at least some design input to share, in a day or two.
And then, changing the implementation, is not that challenging. I've done it in my MR draft PR.
But I don't know… I don't know about the rippling effects, right? I don't know if that bug is going to bubble up anywhere.
after that.
Laurent Querel 00:40:48 Because, so I, I remember the original Pierre, it was about the nine items.
What you did, was, yeah, basically determining the number of, Data point, or number of signals.
And… It was… the computation was not aligned with the… what… what the Protobuf specification is saying. When we are… when we have a… A malformed, one-off.
That's right. We should only take into consideration the last situation for the last item in the one-off.
And not containing all the… The invalid variant of the one of.
Pierre Mariani 00:41:35 Correct.
Laurent Querel 00:41:36 You fix that, and then you discover that instead, in our case, because we retain only one, which is aligned with the spec.
But the spec is saying, just retain the last variant of the one-off, and you are saying that we are retaining the first variant, right?
Pierre Mariani 00:41:56 Exactly, exactly.
Laurent Querel 00:41:57 Okay.
Okay, for me, that's definitely a bug we need to fix.
Joshua MacDonald (Microsoft) 00:42:03 For the record, I don't see any great ripple effects here. It would take an invalid data stream to display that, and I don't think we have that. It's really hard to test this, because it's really hard to produce this data, so I think we're okay.
Yeah.
Laurent Querel 00:42:17 You too.
Pierre Mariani 00:42:18 Okay. There's a secondary thing I wanted to ask you, it seems that if we are unable to parse the bytes payload.
Specifically in the non-items, use case, we return zero.
But, how do we distinguish a valid zero from, a broken payload?
Laurent Querel 00:42:45 Yeah, I think we have this issue in the… In the views in general, where… We don't really have an API that returns results.
We, we have, other… Scalar values or options.
But we are not able to return the fact that, okay, there is an issue during the decoding. And that's a general problem.
I started to work on that in the pluggable codec system.
to fix that.
need to be applied to Namiten also.
So we… we should be able to be in a position where we call numItem, we retrieve either a number or an error.
Okay.
Pierre Mariani 00:43:36 Okay, that probably is part of a larger scope.
Laurent Querel 00:43:40 Yeah, yeah, definitely.
Pierre Mariani 00:43:40 API service. Okay, sounds good. Yeah.
Joshua MacDonald (Microsoft) 00:43:45 Yeah, we have this problem where anytime you have bytes, like, we haven't validated the bytes yet, and If we convert to OTAP, then you're gonna get the error, but if you just access the protobuf, we don't have a solution, it sounds like.
Laurent Querel 00:44:02 Yeah.
Pierre Mariani 00:44:03 Thank you.
Laurent Querel 00:44:05 Centralizing time, and just reading rapidly, Okay, okay, job done, already done, review a type exponential histogram structure… Oh, I think this one has been fixed by Jake.
Jake, the… this one?
Albert Lockett 00:44:33 This is the follow-up to make it like required.
Laurent Querel 00:44:36 Oh, that's in PhotoWeb. Okay, okay.
Albert Lockett 00:44:37 Yeah, now we set it, but we still accept if it's not.
Laurent Querel 00:44:41 and.
Albert Lockett 00:44:41 So, like… Do the enforcement and all that.
Laurent Querel 00:44:45 Okay, thank you.
Jake Dern 00:44:46 Yeah, and I did add the… I accepted that one. I meant to earlier, but…
Laurent Querel 00:44:50 If it's okay for, for you guys, I'd like to discuss this one. Anyway, I think I put it, into the… The list in the agenda.
So… Sorry, where it is… Yeah, there.
Okay, so, this scene came from… Alrighty, I think it's better explained there into this PR.
So, the… the context.
At Fiveside, we had a QA session, and they did some scenarios, where, for example, we have the OTAP exporter.
The destination was no longer available or reachable.
Either for a DNS issue, or for, just the fact that the backend was not, up and running.
Then, for every… incoming batch into the hotel exporter, we are generating a warning. So you see, depending… and then the number of warning will be directly related to the number of received batch.
It could be a lot, obviously, depending on the traffic.
And those repetitive batch warning does not provide a lot of value, so what I'm… Suggesting here is to have a way to report this kind of event.
Keeping the same kind of, information.
But making sure that we are not producing or flooding the system with warnings that are Close to be exactly the same, except the time stone.
And I was thinking then that this could be.
applied not only to the OTFP exporter, but in fact to all exporters. And then, there are some follow-up PRs where we could apply. I just tried to investigate the various operations where we have a similar.
similar issue.
So we should, then have follow-up PR to reimplement the same framework.
To report a repetitive event.
On the… the value sled.
So, now, a little bit in more detail, it's a state diagram presenting how this thing will work, so we… We start with an unknown state.
Until we are in, we are successfully, for example, for the OTIP exporter, exporting A request, we are in a delivering state.
We don't really report, so we don't have warning there. It's, info level.
And, And there is this concept of episode, so we… because we are delivering.
delivering state. There is not really an episode, started. An episode corresponds to Or something bad happened, and we are trying to track how long this episode, will, will, will.
Will exist.
So the first failure.
happen, and then we open an episode, and we basically create a warning with the corresponding, event. So it's a structured event, as usual.
We enter into the degraded state.
And we stay in this degraded state until.
Until we are no longer observing this issue for a period of time that is fixed.
By default, to 30 seconds, but the goal could be to.
I mean, that's something that needs to be configurable with a policy.
And there is also, an additional element to that, so we have an initial warning saying, oh, we enter into, some trouble.
Then… Every 60 seconds, which is another timer, we are basically, re-emitting another message saying.
We are still in this episode.
And the event contains also the number of Errors that have been observed during this period, where we didn't emit any warning, but also potentially some success.
So, but… so at the end of the day, we have an opening event describing the the initial problematic episode. Then every 60 seconds, we have another event summarizing what happened during those 60 seconds.
And at the end, when During 30 seconds, when we didn't observe any issue, we have a closure event, basically summarizing the episode.
And this, thing that I just described will be, A set of code that could be reused in various, in various mode.
And then this PR is just the beginning, just creating the… this, this logic, this state machine, applying the… the approach to the OTFX starter.
Drew Relmas 00:50:40 I'd like to say something here, because I think this is, really interesting and related to another idea I've been toying around. It's… it's interesting to me, this is about… you know, when we see errors, we want to prevent a flood, right? So we want to summarize.
However, I think there's… Somewhat of an opposite… Approach to take, which is, if I see errors, I might want to zoom in.
Meaning, if my diagnostic level is like, basic, for example, but I see errors can I increase my log level to maybe catch debug? Can I temporarily increase the runtime, metric level to… Get some more information. So… It's actually really interesting.
These feel like two opposite ways of handling this degraded… I think the concept of a degraded episode is super awesome. I just think we might want to expose different ways to actually handle that.
Does that make sense?
Laurent Querel 00:51:53 Makes perfectly sense for me. I will summarize what you said with this.
Drew Relmas 00:51:59 I can leave a comment on here. We don't have to do it.
Laurent Querel 00:52:03 I think it's perfectly compatible with the approach. We could imagine that instead of getting rid of the initial warning, so when we are in this.
60 second period, where we summarize the… the… The previous 60 seconds.
If we are in a debug mode, we could, just… keep untouched the… all this mechanic, this logic, but also had the individual Warnings, they will be debugged in that case.
Drew Relmas 00:52:36 What I'm, to give a more concrete example, say we're looking at picking a random exporter, the Geneva exporter, we see an increase in the metric errors or failures.
And as a response, maybe configured via policy, we can say, if we see a rise in this error metric, enable debug logs from this component specifically.
Laurent Querel 00:53:03 Yeah.
Yeah, yeah.
Kenneth.
Drew Relmas 00:53:08 Yeah, you're right.
Laurent Querel 00:53:08 It's going, so if I understand well, the scope of what you are seeing is… partially related to that. We, so we need to take into account the fact that we are not replacing the current warning by just one warning, and then a subsequent summary event. And a closure event.
We do that, obviously, but we also keep the debug level in place.
And then you can, on your side, with some kind of controller.
Target the debug level for specific components.
Which could expose debug that are not in this logic, but related to the corresponding component.
Yep.
Drew Relmas 00:53:57 Yeah. Brian had a fun message in the chat, degradation capability.
Laurent Querel 00:54:04 Yeah.
Kennedy, you want to say something?
Kennedy Bushnell 00:54:08 Yeah, I kind of put it in chat, but I think if we build this on what we imagine to be the aggregation engine.
Andrew Lamb, Then you have this event that is occurring, and it kind of triggers this scenario, and you start aggregating all these events, and they have time windows, that's where you get, like, your timers and un… the 60 seconds, and then with what Drew's talking about, if we had The ability to, like, trigger on when we start seeing this happening, or when we end seeing this happening, then we can say, like, let's turn on up that debug level, we could do… you know, all sorts of other things. We've talked about triggers previously as well.
This could be a good way to kind of pull the start of that engine in.
Laurent Querel 00:54:52 So how did you name the engine? Adeline, I didn't hear you very well.
Drew Relmas 00:54:57 So, I think what you're referring to is Blanche's work in Record Set Engine, which does support aggregation of OTLP things.
Laurent Querel 00:55:05 Yeah, but…
Kennedy Bushnell 00:55:07 It does within batches, not over time, so we still need the time-based aggregation engine built. I think we're gonna need that for metrics for sure, and this certainly seems like an aspect of, like.
if we had aggregation, you'd say, I see an event coming, and I want to aggregate it for 60 seconds, and here's my aggregation logic for that type of event.
Laurent Querel 00:55:30 Okay, but where I disagree.
I think in a normal situation, except if we are in a debug mode, we should not generate This flow of event, because we are… Our engine is all about performance.
So, I'm not very well aligned with a situation where we generate, anyway.
Millions of events.
Just to aggregate them.
And expose, basically what this thing is doing.
I'd like to fix the issue at the source.
If we want the flood, that's okay, but we have to enter explicitly into this model.
So, personally, I prefer this approach.
Instead of fixing the problem after the fact.
You see what I mean?
Kennedy Bushnell 00:56:20 the same thing, right? Because, like.
If you're saying that your running state is not normally emitting these events, because you shouldn't be emitting these events, then… you wouldn't omit the event that would start the aggregation from happening. Like.
Right? And then you're basically.
Laurent Querel 00:56:39 Oh, okay.
Kennedy Bushnell 00:56:40 events and then what ends up happening is the aggregation engine knows that I've already got an event in memory. I'm just going to increment the counter versus publish a whole.
Metric.
Laurent Querel 00:56:50 Maybe I misunderstood what you were saying because what I understood from your description was We have an… we could imagine that we have an aggregation engine, Combining multiple events into one.
If we want. So it's… it's like… This aggregation engine is in the ATS, I guess.
So it means that we generate those events, so we generate a lot of allocation.
Just to aggregate them. What I'm saying is, no, I don't want those allocations by default.
And, if we want… If we are entering into the debug mode, then, yes, we generate the event.
So this aggregation is done at the source, not directly into the ITS. So for me, it's not exactly the same.
On one side, we generate a lot of allocation, on the other side, in this specific description, we don't generate any allocation.
Joshua MacDonald (Microsoft) 00:57:49 You guys'.
Laurent Querel 00:57:50 So 76.
Joshua MacDonald (Microsoft) 00:57:51 the.
Laurent Querel 00:57:51 sensing, but it's not the sensing in terms of performance.
Joshua MacDonald (Microsoft) 00:57:55 This is all about telemetry SDK support for observability right here. We're not talking about the engine anymore. I love it. I think we should not take this conversation too long.
Yeah, but…
Laurent Querel 00:58:07 I need this thing merge soon.
Joshua MacDonald (Microsoft) 00:58:11 What I wanted to say was, I like your proposal, where you started with it. We went way off into a tangent about debug mode and what we want our, like, fancy SDK to do, which I like that conversation, but just to bring it back to what you described, it was a stateful like, piece of logic that has several log statements.
That intercepts all the failures and does limited logging about it. Yeah. And I would totally accept that. We can have another conversation about fancy debugging capabilities, which is one of my favorite conversations, but it's different.
Laurent Querel 00:58:44 Yeah, yeah, I totally agree with that, yes.
Kennedy Bushnell 00:58:45 Yeah, I mean, on the dynamic… like, changing of log levels, I agree that that's a separate conversation. I think we're kind of… at least what I… I think me and Laurent were talking about was where the aggregation happens, whether it's a more general system or happens Purely at that log level.
And…
Laurent Querel 00:59:07 Yeah, and the design principle that.
Guide this solution for me is performance.
I mean… If we are generic versus performance.
We could imagine the same logic with post-aggregation.
That will be… that will provide the same output at the end. I agree with that. Semantically, it's equivalent.
But at the performance level, it's not. And because this system is all about performance, in my opinion, especially when we are entering into a degraded mode.
We should make sure that we don't kill ourselves.
And that's what this proposal is about.
But keeping the same, at the end, keeping the same kind of, troubleshooting capabilities.
And what I like with the… the… what Drew mentioned, we can… we already have a way to change the debug level, so let's use that to reproduce The cloud, if we need.
And personally, I don't think we need, but let's imagine that we have some additional detail.
That are not reproduced and integrated into the event that are summarized by this logic.
Then we can always do it.
I mean, the fact that we can post-aggregate is still interesting.
But I don't think it will be interesting necessarily for the internal telemetry, more for the… the telemetry that we transport and process, because there we don't have any other leverage. And obviously, if we want to reduce the flood from an external component generating too much event, we can use this aggregation.
But, for the ITS, where we have all the control.
Personally, I would prefer this, this approach.
Makes sense.
Joshua MacDonald (Microsoft) 01:01:18 It sounds like we have a little more to talk about with diagnostics in cases of debugging and so on. This does not worry me. We can do this. This is, like, our favorite topic in observability. We got this. But I would definitely approve this type of work that you're showing, and I think we're at time.
Laurent Querel 01:01:35 price.
Joshua MacDonald (Microsoft) 01:01:36 Thank you all.
Laurent Querel 01:01:37 Okay.
Joshua MacDonald (Microsoft) 01:01:38 the.
Laurent Querel 01:01:38 You are.
Andres Borja 01:01:40 Yep.
Kennedy Bushnell 01:01:40 Thanks.
Pierre Mariani 01:01:42 Thank you.
