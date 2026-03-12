SIG: RPC Sem Conv Stability SIG
Date: 2025-09-03
Duration: 46 minutes
Zoom Recording URL: https://zoom.us/rec/share/vi2zS-fraYKz4--87uo-aBSqKGVZtCngbQNf-EO7FqcAIAcWuLADUsOwMFldahVg.VbR8_I3kEmdUNfjM
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 01:05 No, Andrew, I don't consent to your recording.
Hey, man.
**Matthew Hensley** 01:19 Hello.
Gotta love all the butts.
**Trask Stalnaker** 01:33 Yeah… I don't understand the ones that join the Zoom.
Cause. That one is really… A weird one.
**Matthew Hensley** 01:49 I'm mostly just surprised that Zoom doesn't have a solution to this, considering how Often I hear about these issues.
**Trask Stalnaker** 01:58 Yeah, I think it's particular to… I don't think that many people do, like, these public… Anybody can join… kind of… me, I guess? I don't know. I've reported it, like, 10 times to Zoom, and they always tell me it's not a violation of Their policy or something.
**Matthew Hensley** 02:26 Sure.
**Trask Stalnaker** 02:28 alike.
okay, but… Can you add a feature or something so that we can opt out of them?
Oh, we can't hear you, Lydmilla.
**Liudmila Molkova** 02:43 By the way, why don't we like them? I mean, I don't like them, but why?
**Trask Stalnaker** 02:48 Because they tell you that you're agreeing to… you're consenting to something by just being present in the meeting.
**Liudmila Molkova** 02:59 I see.
**Trask Stalnaker** 02:59 And then they consume space on the, The windows on the view, and just generally distracting.
**Liudmila Molkova** 03:10 Okay.
I'm glad, Mathieu, you made it to the first, and Trask, you both made it to the first call.
**Matthew Hensley** 03:25 Yes, indeed.
**Trask Stalnaker** 03:35 We've got James. Hey, James.
**James Thompson** 03:40 Hey.
**Trask Stalnaker** 03:43 one of our, few APAC-friendly, timed meetings. I'm hoping that the Alibaba folks will be here, since we… Scheduled it at this time for them.
I have a Java meeting with, An hour from now, so… I will.
Find out.
Then… hopefully…
**Liudmila Molkova** 04:25 Should we wait for them? Should we ping them, or…
**Trask Stalnaker** 04:30 I'm not really sure… I can… Peace.
Steve, I don't know the other ones on… Slack, though… Cool, yeah, we should just get going.
**Liudmila Molkova** 05:20 Yeah, I started sharing, I think there are so many things we need to do.
And one thing we can start to is we can… Take a look at the project board, and maybe start… triaging work items.
I've found everything that's related to RPC.
I might have missed something, but I tried to find everything.
And… Well, as we work on this, we'll probably discover more.
Right?
We can go through them.
The other thing I think we should probably do at some point is… Revise the instrumentations we have across languages.
And just see what's available where.
We might discover that there are some frameworks that are not represented in semantic conventions at all.
**Trask Stalnaker** 06:25 Oh, reviewing the existing ones?
**Liudmila Molkova** 06:29 Yeah.
**Trask Stalnaker** 06:30 Okay.
**Liudmila Molkova** 06:34 So, maybe, yeah.
Maybe we'll do it… this. I can create a work item.
Here on semantic conventions, I would be actually interested in doing some research across repos.
**Trask Stalnaker** 06:50 Cool. Do we have, a work item already for… Adding our standard notice.
to, not, like, to freeze the current level.
As we start this.
So we can start pushing…
**Liudmila Molkova** 07:09 I think we already have that.
But it…
**Trask Stalnaker** 07:23 Oh, okay.
**Liudmila Molkova** 07:24 It's a good question, what should we do with it at all?
**Trask Stalnaker** 07:28 But this is… oh, what is this? This is talking about… HTTP… So, yeah, I think we need to update that, because I suspect it was more frozen for the address, the common stuff, like client address, server address.
yeah, I'll create a… Work item for that.
**Liudmila Molkova** 08:00 Okay.
So, one of the reasons, I'd like to do the revision of what we have is to see, does anybody actually supports this. Maybe we can replace it with one, whatever, 38.
37.
**Trask Stalnaker** 08:25 Yeah.
Have there been changes?
Is it relevant to… Not relevant.
**Liudmila Molkova** 08:35 I would love to just put something like, okay, Now, we have RPC opt-in.
**Trask Stalnaker** 08:44 Yeah.
**Liudmila Molkova** 08:45 We could keep both, right? But it would be easier if we just had the RPC blurb.
**Trask Stalnaker** 08:54 I see what you're saying. Yeah, I was assuming we would… Yeah, also just have the RPC blurb.
Because, wow, that will be complicated.
To have both.
It's already complicated.
**Liudmila Molkova** 09:13 Yeah.
Okay.
Okay.
So, should we do the exercise of going through the issues and try to trash them?
**Trask Stalnaker** 10:22 Yeah.
**Liudmila Molkova** 10:25 Okay… Our PC Transport Type.
Oh… That's something complicated.
Oh, this is the separates… different… Different streaming.
Well, it sounds RPC-related.
**Trask Stalnaker** 11:09 Did we… we did include… say we were going to We left it open whether we were going to tackle streaming.
**Liudmila Molkova** 11:19 It's a stretch goal.
Okay.
So… We can have a common strategy goal.
**Trask Stalnaker** 11:33 Is that… Is that needed?
What is this? Is… Network. Can you scroll up? What's the title?
our BC transport type.
Do you remember why you were proposing this?
**Liudmila Molkova** 12:03 There is a problem with MCP, it supports different transports.
Different HTTP versus S-to-day IL transport.
And they were…
**Trask Stalnaker** 12:19 Can't be captured in the network.transport.
**Liudmila Molkova** 12:29 it can be the HTTP versus STDIO, but when it comes to the flavors of HTTP, it cannot.
**Trask Stalnaker** 12:41 Let's see… And do you think that is a general… Something that needs to be solved, should be solved generally, versus… just an MCP… attribute…
**Liudmila Molkova** 13:04 So the problem as generic, it might be worse, it might be interesting to record if our RPC call was unary or… streaming.
It… can be incrementally added. It feels orthogonal to anything else.
**Trask Stalnaker** 13:28 Okay, that's… True… I mean, short of metrics… Gonna say just post… markup post stability.
**Liudmila Molkova** 13:42 I mean, we can definitely try to approach it after we decide what to do with streaming. If we say.
We only focus on the unary cause.
Then it doesn't make sense to solve this problem.
**Trask Stalnaker** 14:00 for the MCP… The difference here would be streaming versus… Unary… Does that capture it for the MCP?
**Liudmila Molkova** 14:23 For MCP, the difference is HTTP plus streaming versus STD I.O.
Which we call pipe.
**Trask Stalnaker** 14:31 HB Plus streaming.
**Liudmila Molkova** 14:34 it… MCP is… is… let's not… I don't know, it's not the RPC… call per se.
So, we don't need to solve MCP problem. I think we need to see if it's a general problem that applies to our PC at all.
**Trask Stalnaker** 14:56 And so… Unary cause… RPC… trying to think what the… What is… what is streaming?
mean…
**Liudmila Molkova** 15:20 Journey.
**Trask Stalnaker** 15:21 Not… not a request response.
I mean, to me, I guess. Unary means I send one request, I get one response.
Streaming means… I just send requests, I may receive responses, but there's no correlation between the two.
**Liudmila Molkova** 15:44 Or you send a request, and you open a stream, and you may receive Multiple responses to a single request.
**Trask Stalnaker** 16:00 So, yeah, I… I agree that would… we would… If, when we tackle streaming, we would… There would be some way to identify that it was a streaming… Versus… Unary.
**Liudmila Molkova** 16:27 Yeah.
So, we can keep it in the backlog.
I'd like to have some indication that we had some Basic triage on this, and it's… It's something we might tackle.
**Trask Stalnaker** 16:44 Can we… maybe, should we have a brew… Label, grouping, something for column for streaming.
I suspect there will be multiple…
**Liudmila Molkova** 17:00 I think, my tier James, I think I saw somebody unmuted. Did you want to say something?
**Matthew Hensley** 17:07 I'm wondering about this transport type, because we're talking about… the easier part, maybe, is, like, the protocol versus its behavior. We just need to go ahead and split it, because… Into two issues, but… Especially if we're gonna… deal with any of the streaming things later. We'll still need… Transport sooner, regardless of… What we do is streaming.
**Liudmila Molkova** 17:34 We should have a transport, right?
The network transport.
Network protocol version. Oh, sorry, network protocol name.
Is this what you mean by transport?
**Matthew Hensley** 17:46 Yes.
So I believe that was in the top of the That, issue was talking about.
**Trask Stalnaker** 18:01 Do you want to pull up the RPC SimCon and see what… Network attributes we have on there already.
**Liudmila Molkova** 18:10 Yeah.
We have a network transferred.
The address family… huh, we don't have network protocol name.
Which is funny.
**Trask Stalnaker** 18:26 Hmm… Yeah… Good call.
Do you wanna… not… do you wanna just… how to create an issue for…
**Liudmila Molkova** 18:48 Yeah.
**Trask Stalnaker** 18:48 net protocol…
**Liudmila Molkova** 19:34 Okay, and this… Sounds like to-do.
For sure.
**Trask Stalnaker** 19:45 Yes.
**Liudmila Molkova** 19:47 And then we can have… Okay, the next one, Unified Message Transmission Namespace.
James, do you want to talk about it?
**James Thompson** 20:26 Yeah, so when I was looking through the conventions, there's a lot of similar attributes and that across HCP, messaging and RPC, so I'm wondering, does it make sense to have them Directly defined in each of the namespace.
Or is there opportunity to unify them?
Alright, because, like, if you have a C there, there's RPC server request size and HTTP server request body size.
Right, could we bring them together?
**Trask Stalnaker** 21:17 So, specifically, anything besides the… The request and response sizing, or this is very specific to those…
**James Thompson** 21:29 See, it was pretty much around… request and response sizing, I think, Alright, and then also, like.
In HTTP, you have headers. In messaging, you have headers, RPC you have headers as well.
Alright, it's, yeah, those common things between them.
Is it benefiting unifying them?
**Trask Stalnaker** 21:57 So, the first problem I see is that HTTP is stable.
So…
**James Thompson** 22:04 Yeah.
**Trask Stalnaker** 22:06 whoop.
I don't think we would… oh, are these stable in HTTP?
**Liudmila Molkova** 22:13 Mmm, lovely.
**James Thompson** 22:14 Bye.
Yeah, not sure.
**Liudmila Molkova** 22:23 Nope.
**Trask Stalnaker** 22:24 Development. Yeah, because I think we had… It was kind of trick, like, actually defining these, if I recall, was harder than… We thought…
**Liudmila Molkova** 22:43 I think that there is always a question, how do we define something?
And, you can assume, like, there could be And messaging, body size, coexisting with… The request size, they are not the same.
They describe different things, and if we call something request size, it loses It's specificity, and we can no longer use two of them on the same telemetry item.
And I don't see how it's helpful to merge them, what we achieve by this. Fewer attributes, fewer metrics, but then they are too abstract.
**James Thompson** 23:32 Yeah, like, if you have a look, there was additional attributes there to split them.
Alright.
Alright, so…
**Liudmila Molkova** 23:41 Can you repeat that?
**James Thompson** 23:42 So, if you look further down, there's separate attributes to describe Alright, if it's a request or a response.
So, yeah, it was just an idea.
**Liudmila Molkova** 23:57 So they are different because you can have an event that describes your operation, and it would have Information about both.
And it's kind of useful to… have… them separate.
In this case.
**James Thompson** 24:13 Yeah, yeah, so we could certainly… if that's… for that scenario, we could certainly, rather than Just have one body size, have the request and the response body sizes separate.
Alright.
So, but the question is, would we have HDP, body size, and RPC body size.
no, sorry, HTTP request body size, and IPC request body size.
Right? And what happens if you do RPC over HTTP, or GRPC over HTTP? Where do you… Yeah.
**Liudmila Molkova** 24:55 the problem of RPC over HTTP exists anyway, right? There is HTTP request method and RPC method.
And there are layers.
There are ambiguities.
If we solve it for request size… Wow.
**Trask Stalnaker** 25:17 What might be use… interest… more interesting here would be if we had, like, the embedding concept.
Like, we, like, user namespace, which could be… can be embedded into different domains… Could potentially have a request and response.
But it wouldn't mean anything on its own unless it was embedded.
Let's try to… Move… And I don't know what… I mean… I think it's… this would be… a big… Yeah, I, I think, not sure.
I'm really in favor of this.
Either… Maybe a… Some specific, like, How does this… improve things? Like, what… what do… does this make it easier for… How does this improve users?
Experiences… Or is this only about, like, de-drying up, you know, don't repeat yourself, kind of, in some kind of itself?
Cool.
**James Thompson** 27:14 I've actually added a issue that's not on the board, but It's in the Google Drive file.
Which mo…
**Liudmila Molkova** 27:30 It's in the boards.
**Trask Stalnaker** 27:31 It's on the board.
**James Thompson** 27:32 Oh, I couldn't say…
**Trask Stalnaker** 27:35 Maybe it's not public. Do you not see, when you go there, do you not see this project that Laudmila's showing?
**James Thompson** 27:42 No, I can see the project, but… For me, I… I only can see the no status.
**Liudmila Molkova** 27:50 Yeah, so because we didn't triage them yet.
**Trask Stalnaker** 27:53 Yeah.
**James Thompson** 27:54 Yep, but… okay, but I… I couldn't see that.
Oh, yeah, I don't know how I missed it, sorry.
**Liudmila Molkova** 28:06 We can talk about this now, since we are triaging them in pretty much random order.
**James Thompson** 28:14 And there already is a PR which seeks to address it.
If that makes it easier.
**Liudmila Molkova** 28:20 No, it's not.
So what is this issue about? Can you guide us?
**James Thompson** 28:29 So, so the issue is… On the spend… Alright? So… JSON RPC has its own span page.
Huh?
Has its own page in the specification.
what that page does is adds in an attribute which is conditionally required, and the condition is if it's for JSON RPC.
The problem is, for metrics, it doesn't apply.
It doesn't apply for an error state in a metric, because you don't have the method.
**Trask Stalnaker** 29:09 Oh, because RPC method is required, is that…
**James Thompson** 29:12 Yeah, so it's not required for all of them, it's only required for the JSON RPC version, which implements the met… which affects the metric. So if you read it.
Right, so this was all fine?
Right? But the problem is, if you look at the JSON RPC span.
It now becomes a required field.
**Liudmila Molkova** 29:41 Oh, sorry. So, RPC metrics…
**Trask Stalnaker** 29:44 So, go to the J… I think go to the JSON RPC page.
method is marked required here.
**James Thompson** 29:56 Yep.
Alright, so… and this is the JSON RPC attributes.
Alright.
So, if you're doing a metric for JSON RPC, If you're reading this, it says, RPC methods now required.
**Trask Stalnaker** 30:13 And is RPC… if you… if you go to the general RPC… conventions, is RPC method required?
**Liudmila Molkova** 30:25 Yes. -Oh, sorry.
I recommend it.
**James Thompson** 30:31 Yep.
**Trask Stalnaker** 30:35 And is the idea that our JSON RPC is method the HTTP method?
**James Thompson** 30:42 No, but the scenario is if there is no method, Alright.
Right, so when you report the metric, you don't have a method to report.
**Trask Stalnaker** 30:55 So, I mean, is this as simple as we need to change RPC method to not be required?
**James Thompson** 31:02 Yes.
**Trask Stalnaker** 31:03 Perfect.
**James Thompson** 31:05 Right? And that's literally what the couple of lines in the PR does.
Yeah, so it, it removed…
**Liudmila Molkova** 31:27 No, it removes it, but it shouldn't remove it.
**James Thompson** 31:33 But…
**Liudmila Molkova** 31:39 So it changes something… It does not… it removes the RPC method from… JSON RPC, it's not what we want to do, right?
**James Thompson** 31:52 But if you have a look at the… if you… but what's now done is put a conditional requirement on it.
Right.
So, dude.
**Liudmila Molkova** 32:01 And this is… it disappeared from the JSON RPC.
**James Thompson** 32:06 Because the JSON RPC page only… because the problem is, if it's on the… JSON RPC page, that applies.
Generally, across metrics and spans.
**Liudmila Molkova** 32:19 We don't have a documented, and it's not what we do usually, so we document every attribute that applies to JSON RPC here.
**James Thompson** 32:29 Hmm.
**Liudmila Molkova** 32:29 What do we do for other places?
**James Thompson** 32:31 But that's not the way these documents are written, though. These are just…
**Liudmila Molkova** 32:35 Should… we should rewrite them, right?
**James Thompson** 32:38 Yeah.
Right, because if you have a look, these attributes are just the ones that are adjacentRPC.
**Trask Stalnaker** 32:44 Yeah, so we changed our… how we handled these, sort of, Vendor-specific or system-specific.
Documentation when we did the database semantic convention stability.
**James Thompson** 33:00 Yep.
**Trask Stalnaker** 33:01 So, I think the short answer is this one… We can mark as to-do.
Oh, yes, but yes, we should… that… yes, thank you for opening the issue for…
**Liudmila Molkova** 34:02 Okay, and this? I lost the issue…
**James Thompson** 34:09 Yeah, that's… that's something, yeah.
**Liudmila Molkova** 34:46 Okay.
So let's try a few more.
Capture similar information to HTTP messaging for gRPC.
Okay, James, can you explore… is it the same one?
**James Thompson** 35:10 So this is… if we were to do it, go down the path of having capturing that information in just an RPC space.
**Liudmila Molkova** 35:21 Do we just want to invent attributes and metrics for the sake of consistency with HTTP? Do we need it?
**James Thompson** 35:32 So… bike.
If you… hmm… Where… what is it? Like, method type…
**Trask Stalnaker** 35:44 Maybe, James, check out the Java gRPC instrumentation.
I don't remember if we capture… If we have, like, the… Headers, or we might capture metadata headers…
**Liudmila Molkova** 36:06 the gRPC?
**Trask Stalnaker** 36:08 Yeah…
**Liudmila Molkova** 36:12 Request navigated keys.
**Trask Stalnaker** 36:18 Yeah, and what do we put them into?
I wonder if we can use Jay's… Have you seen… I don't know if he's covered… oh, I think he has a PR up right now for gRPC, so GRPC won't be in… this cool explorer yet.
**Liudmila Molkova** 36:39 This one?
**Trask Stalnaker** 36:40 Yeah, yeah.
So it actually captures it from our tests what attributes we capture, so here…
**Liudmila Molkova** 36:55 in the YAML.
**Trask Stalnaker** 36:57 Yeah, look at that YAML, the… the…
**Liudmila Molkova** 37:01 The metadata, or the first one?
**Trask Stalnaker** 37:03 The first one.
Search for GRPC… But not that gRPC. If you go back to the diff, it was there.
**Liudmila Molkova** 37:24 Okay.
**Trask Stalnaker** 37:27 So here, configurations, and scroll down… This is configurations, here is the telemetry that it emits.
Hmm.
**Liudmila Molkova** 37:38 Nice.
**Trask Stalnaker** 37:39 Yeah, so… okay, those are… that's VIN default, so scroll down, and there should be a win… The opt-in attributes, like the… here.
So here is VIN experimental span attributes, you can see the telemetry, but we want to see the metadata, so keep scrolling, and let's see if there's another WIN.
There isn't. Drat. That means we don't have a test that…
**Liudmila Molkova** 38:12 Explicitly opts into that.
**Trask Stalnaker** 38:15 thing.
**Liudmila Molkova** 38:16 This is the… they're, like, the individual headers.
**Trask Stalnaker** 38:22 Yeah, it's whatever gRPC calls metadata.
**Liudmila Molkova** 38:29 Did you have an issue for this?
Do we have an attribute that captures, you know, the data?
We don't.
**Trask Stalnaker** 38:40 I think so.
**Liudmila Molkova** 38:42 We should, right?
**Trask Stalnaker** 38:45 For GRPC specifically.
**Liudmila Molkova** 38:48 Oh, GRPC, right.
**Trask Stalnaker** 38:50 It's a… it's a gRPC console.
**Liudmila Molkova** 38:53 Oh, we have it, yeah.
**Trask Stalnaker** 38:57 Okay, perfect.
Yeah.
So this kind of points to potentially issue with… Calling it, like, being too generic about calling them headers is then we lose… System-specific terminology.
**Liudmila Molkova** 39:19 Yeah, and they're called params, and JSON RPC, or maybe they're called params in MCP.
But the terminology is different.
**James Thompson** 39:32 In the case of gRPC, if we're calling it metadata, aren't we losing whether it's headers or trailers? Because gRPC has both.
Haters and trails.
**Trask Stalnaker** 39:43 I don't think these are actual HTTP headers in trailers. This is… Would have to look at the…
**James Thompson** 39:53 Java instrumentation to see what exactly.
**Trask Stalnaker** 39:57 metadata means in the gRPC case.
**James Thompson** 40:01 Yeah, no, because I know gRPC uses headers and trailers.
**Trask Stalnaker** 40:07 Http headers and HTTP trailers.
**James Thompson** 40:11 Yeah, from my… from what I've… when I was using them, that… there was just the GRPC headers and trailers.
Yeah.
**Trask Stalnaker** 40:20 Yeah, so maybe you can do some research on this, James.
Comment back on the issue.
**Liudmila Molkova** 40:35 The issue, though, what about the size, and… It's… generally not possible to know the size of the headers or trailers. It's just not something that exists, usually.
And… it would be… like, I… I would struggle to… to find a reason to rep… Pour this information in the first stability phase.
**Trask Stalnaker** 41:06 Yeah, we don't capture this for HTTP, so I would… I would agree that it's… doesn't seem like it's… if it's not important enough for HTTP, it's probably not important enough to do, at least initially for RPC.
**James Thompson** 41:25 But we do do the body size in HTTP.
**Trask Stalnaker** 41:28 Yeah, yeah, I think the body size is a good, would be a good addition.
Again, the HTTP it's not stable, so it may still… it may be okay, or I would say it would be okay Not… for it not… for it to be post-stability.
**James Thompson** 41:53 Nope.
**Trask Stalnaker** 41:53 Even the body size.
The other thing in the context of gRPC that We, will want to… Look at… Closely is their native instrumentation.
**Liudmila Molkova** 42:45 And…
**Trask Stalnaker** 42:49 Seeing what they have.
What they're capturing natively, because ideally, we want to try to sort of align With them, and we do like that they're capturing it natively.
Unfortunately, I don't think we were able to get anyone from the GRPC team to join this group.
But we can… bug Josh.
More, as needed.
**Liudmila Molkova** 43:15 And we should have an issue about this.
I think we should move it to to-do.
**Trask Stalnaker** 43:21 At least we should.
**Liudmila Molkova** 43:22 Awesome.
Write up on this.
**Trask Stalnaker** 43:26 Yeah, I think this is a… this is a must.
due for… our initial stability.
People will look at us funny if… We don't have an answer, at least. Even if it's that we're diverging, but just… we… we need to have a… consensus.
**Liudmila Molkova** 43:48 Yeah.
By the way, we… I think this is 45 minutes call, and we are almost at time.
Yeah.
**Trask Stalnaker** 44:00 I'm in favor of… Keeping it to 45.
**Liudmila Molkova** 44:07 Cool. So then, it sounds like we have some things to do.
Some of them are very big and very vague.
We have some… Work to do.
Do you have any additional… Action items.
**Trask Stalnaker** 44:29 If anyone wants to pick up one of those to-do ones that we've marked, just comment on the issue, or if you have right permission, just assign it to yourself.
Or triage permission.
Assign it to yourself.
**Don B** 44:45 Can I ask a quick question, Ludmila?
**Liudmila Molkova** 44:48 Yeah.
**Don B** 44:49 So, I normally join, or occasionally join the semantic working group for LLM, So I was just wondering, have you guys discussed overlap with, like, agent-to-agent type?
Messaging and protocols?
Because it is a JSON RPC-based message for agent-to-agent.
**Liudmila Molkova** 45:15 So that's… that's a great question. One of the things… I'm not sure if we have a work item, but maybe… Don, would you mind to create one?
And…
**Don B** 45:27 I can think about it, and I'll also look, because I know it's come up in the LLM working group, but it's been that question mark, is it relevant or is it not, right? Because it's more of a messaging type, like, agent-to-agent communication, rather than LLM telemetry, so it's… So part of the research.
**Trask Stalnaker** 45:47 You don't have to…
**Don B** 45:48 way between.
**Trask Stalnaker** 45:51 You don't have to answer that question to open an issue.
**Liudmila Molkova** 45:54 Yeah.
**Don B** 45:55 But I will figure out where I think it's appropriate, and also take a look at the notes of both to see where it may have been discussed already, but I think it's worth bringing up next week, and I'll.
**Liudmila Molkova** 46:08 Yeah, definitely.
**Don B** 46:09 Attend both meetings next week.
**Liudmila Molkova** 46:12 Wonderful.
**Don B** 46:13 Alright, thank you very much.
**Trask Stalnaker** 46:17 Thank y'all.
**Liudmila Molkova** 46:18 Thank you.
**Trask Stalnaker** 46:19 Bye.
