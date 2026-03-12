SIG: RPC Sem Conv Stability SIG
Date: 2025-09-10
Duration: 47 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 01:35 Hey, folks!
**Steve Rao** 01:38 Hey, Steve.
Yeah, hi, Strasker.
**Trask Stalnaker** 01:41 Yeah, Albanon, nice to meet you.
**Steve Rao** 01:45 Nice to meet you, too. Hello.
**Trask Stalnaker** 01:58 Give folks a couple minutes.
And.
**Matthew Hensley** 03:19 Hello.
Food Miller posted in Slack, she's gonna be… 5-10 minutes late.
**Trask Stalnaker** 03:29 Oh, okay, thanks, I hadn't seen that.
**Matthew Hensley** 03:34 I've been trying to get in the habit of checking the channels.
Before the meetings.
**Trask Stalnaker** 03:40 Good idea.
Alright… So, last week, we were… Going through the project board, trying to… Figure out… all these ones with no status, Lyudmila had gone through the SEMCOM issues and moved things to the board that were RPC-related, so… We're sort of just going through…
**Steve Rao** 04:38 you'll see events, hi.
**Trask Stalnaker** 04:39 So we can continue doing that. Guessing it'll probably take us, another couple weeks to get through all these. I think we got through… 5 or 6 last time.
I guess you may as well start at the top.
Unified… oh, we discussed this last week.
So… I guess we'll skip that, and…
**Matthew Hensley** 05:10 Do we need a, another status or something?
For things that we're not even gonna consider.
Or whatever, just, like, not actionable items is just a thought.
**Trask Stalnaker** 05:26 Yeah, so we should have a, like, a post-stability. What we've done with, like, a database and HTTP is we'll have, like, a post-stability one that will just… anything that we… Yeah, aren't consider out of scope for this group, then we can drag over there.
And it looks like we ha- don't have that yet.
**Matthew Hensley** 05:53 Let's see how many of them… End up in that state.
Only a few, it won't be a big deal.
**Trask Stalnaker** 06:01 Yeah, it's a very handy state. We used it a lot before, Let's see, we've got, oh, okay, we discussed this last week also, so I'm gonna go ahead, maybe I can just… Move these to the bottom… Our BC metrics do not list any attributes.
That sounds like a problem.
Actually, do we even have RPC metric?
**James Thompson** 06:43 Yes, we do.
Alright.
So, if you look at the page, there's an attribute group of attributes listed that says these should be… appear on all the attributes, on all the metrics. Just in the YAML, it's not linked to the metric definition.
**Trask Stalnaker** 07:03 I see, so we don't have in the… so if I go to the RPC metrics YAML…
**James Thompson** 07:15 Yeah.
So, it has the group there, but if you look at the metric definitions, there's no attributes or no extents.
**Trask Stalnaker** 07:24 Okay, okay, yeah.
So, that seems like a pretty obvious one. Oh, you have a PR?
**James Thompson** 07:34 Yes, I understand.
I just did double-check the other day, and I realized I missed one extends, so I'll go… once that's done, I'll… Move that out of draft.
**Trask Stalnaker** 07:44 Okay, great.
So, let's just move it straight into in progress.
Json RPC, deprecate duplicate valid attributes.
Right… Right, okay.
Into, like, that category by using… It's the error code… Gotcha. Yes, so this sounds like a to-do?
I guess we haven't… Said, which… RPC frameworks we're gonna be in scope for.
But given that there's not many I think we want, multiple… we don't want it to only be GRPC, which is, also partly why, we've got, folks from, apache Dubbo.
albumin, you're, from… the Apache Double Project?
**Albumen Kevin** 09:03 Yeah, I'm the PMC member on Planet, but for myself, I think I'm new to, open telemetry, but, still previously I have learned some Telemetristings before, but… For the open telemetry project itself, I think I'm the newer for that.
**Trask Stalnaker** 09:30 Sure, yeah, that's great. We appreciate, you joining.
The first couple meetings, as we're kind of going through the backlog,
**Albumen Kevin** 09:42 I mean?
**Trask Stalnaker** 09:43 not be quite so interesting for you, but it also might give you some kind of a sense of what we're doing. But once we get down to figuring out how to have common… we want to have a common, semantic conventions that work across gRPC, JSON RPC, Dubo.
maybe, like, an RMI or a .NET has an RMI, remote, an RPC framework, I think, also.
Hey there, Miller.
We're just… started triaging…
**Liudmila Molkova** 10:29 Wonderful. Hi, everyone.
Great to see, you new folks and old folks.
**Trask Stalnaker** 10:40 So RPZ conventions without span events… I'm here.
**Liudmila Molkova** 10:51 Think, or he… from the triage?
perspective. This is streaming only problem.
**Trask Stalnaker** 10:59 Yeah.
**Liudmila Molkova** 11:00 theoretical.
**Trask Stalnaker** 11:02 Cool, I agree.
inconsistent values… Yeah, we will need to deal with, the… RPC system.
**Liudmila Molkova** 11:21 So I think we would need to describe what is in scope of RPC, and maybe we'll have some phrase somewhere that We… it's limited to RPC frameworks, I'm thinking about creative… creative way how we can solve it. So.
We're going to deprecate rpc.system anyway, right? We are following the RPC, I think, protocol name, or whatever, we will decide.
**Trask Stalnaker** 11:52 Yeah. And AWS conventions will take care of themselves. They will keep using our PC system, and somebody who comes to clean them up.
**Liudmila Molkova** 12:01 At that point, would… decide how to capture REST API operation.
name.
and could remove RPC system as deprecated attribute.
**Trask Stalnaker** 12:18 Sue, do we want to, Go ahead and create a postability column to dump this, or do we want to just remove it from the board altogether?
**Liudmila Molkova** 12:35 Good question.
I would remove it from the board the moment we would introduce our PC protocol name, or… the new thing, but Having a possibility column.
I think it… It's useful.
**Trask Stalnaker** 12:55 Yeah, Matt even had brought that up earlier on the call.
So I think let's go ahead and create that. It's just a nice, easy dumping ground for us.
**Liudmila Molkova** 13:07 Right.
**Trask Stalnaker** 13:09 I can figure out how to do that.
Add options first, stability… There it is.
Okay.
**Liudmila Molkova** 13:47 Should move it closer. We will use it.
**Trask Stalnaker** 13:50 Yeah, before done, yes, that's… Rpc.grpc.statuscode…
**Liudmila Molkova** 14:09 I would imagine we also would get rid of the RPC.
Reflex, it'll be just gRPC.
**Trask Stalnaker** 14:17 Right, right.
Okay, let's move, make that comment.
**Liudmila Molkova** 14:56 What do you think?
So unless we would decide to… make it.
a generic attribute for this. I think there are a few RPC protocols that have status code.
And in theory, we could remove gRPC.
**Albumen Kevin** 15:19 Mmm… Is that however likes REST API, or… Yeah, especially for JSON PC or REST API, they provide the HTTP state code here.
**Trask Stalnaker** 15:38 Do you just pass along, like, in Dubbo, do you just pass along the HTTP status code, or do you have your.
**Albumen Kevin** 15:46 Mmm.
**Trask Stalnaker** 15:47 Set of stuff.
**Albumen Kevin** 15:48 Wee… We have several types of the… Protocol… underlying double. One of the protocols is triple, which is based on HTTP protocol. So, we will reuse the state code from HTTP. The same, like, I think, gRPC and previously we support JSON APC. These two… protocol R provides the status code here.
Besides the… the codes, I… I think maybe the status would be better for it, like, Intimidation of fault, or… outward, or parameter error, or something like that. It can convert to a more… concise, concise things, like arrow, or OK, or something like that.
Because for different systems, we have different ways to figure out the status by code, but it's meaning some of the status, the meaning they are the same.
**Trask Stalnaker** 17:17 One of these, we were just looking at, error… So we do have, an error.type.
That we can use… that we would use for… Like, that kind of general, like, hey, this is the error, and this is the description of the error.
The thing that's unique about gRPC status codes is just that they have this very specific definition.
Of the…
**Albumen Kevin** 17:55 Yeah… I think… I think there are two types of the status code in GRPC. One is, like, the exception, or inside GRPC protocol. The GRPC has the… I think it should be the status object inside it.
And, yeah, there are 16 types of the, status codes, and they are totally serialized into the body.
Above it, the strategies also follow the status code in HTTP status code. So, there are two types of status code here.
And, like, for 404, which means, method not filed, or implementation… implementation not found, or… or something not wrong, yeah. They have the mapping, mapping structure between the HTTP status code and… the, the GPC status code. And also, for the RPC system.
to observe this HTTP status code and the system or the RPC-specific status code are also important here.
Yeah, and likes for 12345, the code is… here is a little weird, like, for Japanese, likes for 16, We… most of us don't know what is it, yeah? Yeah. If it's an impairment, or if it's, like, something not found here, it would be more clear. Or 404.
**Trask Stalnaker** 19:57 Right.
Okay.
So, we've got a couple notes there, and I think… but definitely there's work to be done that needs to be addressed.
One way… In some fashion.
Change RPC and messaging body pillow size attributes from recommended to opt-in.
Okay, so we already did the messaging side, so I'm going to rename this… I'm pretty sure that we want to do this.
So, I will drag it over to to-do.
Oh, yes, this one we have to do.
You are muted.
**Liudmila Molkova** 21:13 Yeah, I was just saying yes.
**Trask Stalnaker** 21:18 Message count… Received message count sent message count.
Span… okay, span attributes, so this is streaming again.
So let's drag it to our streaming stretch goal.
Db Messenger, clarify nested client spans.
**Liudmila Molkova** 21:51 So I think… What we do, usually, we… say it's a logical operation, right? So, for example, if it's a gRPC, and underlying HTTP is configured to handle writ rise, then this span is a logical thing that represents the gRPC call.
After the protocol level, tries.
And it's probably just a few extra words we would put into, span definition.
**Trask Stalnaker** 22:37 Whoa.
Alright, to do… Convention for canceled Spans…
**Liudmila Molkova** 22:50 Yeah, I don't think this is RPC-specific, but it came up in some, issue relevant to gRPC. So, gRPC has this pattern of hedging, I think, when they send… The same request to multiple servers.
And then they consider the first one to reply as a response, and the rest is essentially canceled.
And what happens today, that usually… Our instrumentations consider cancellation as a failure.
And there is no right answer here, right? It's sometimes failure, sometimes not.
So… Even it's somewhat more common in JRPC world to have canceled spends.
I think we need to be extra cautious on what we describe as a… Failure.
And that we have enough wiggle room for instrumentations to… Represent consolation success.
Failure or not failure.
So, it's a general problem, but I think we should do our part in the gRPC… sorry, in our PC.
**Trask Stalnaker** 24:19 And is this something, that we would… that would affect metrics?
**Liudmila Molkova** 24:27 Yeah, we would intersect… Well… We would set the error type, right? Or not set the error type.
**Trask Stalnaker** 24:37 Right.
Yeah.
Alright, so this sounds like… a hard one, but one that we need to put in our to-do. I'm gonna drag it to the bottom there.
Adopt system-specific naming, practice… Yes, we talked about this, and yes, we need to do this… Capture similar information to HTM messaging… oh, oh yes, okay, so we're down to the last two, or the two that, we discussed last week from James.
**James Thompson** 25:28 I've put one issue that you just quickly flicked through back on the agenda list, because I don't actually see where those attributes are being used anywhere.
**Trask Stalnaker** 25:40 Sure, let's see… parent size…
**James Thompson** 25:45 Right.
**Trask Stalnaker** 25:48 Yeah, I mean, we could just remove them completely.
**James Thompson** 25:54 Because at the moment, they are just in the attribute registry, they're not actually on any signals that I can see.
**Trask Stalnaker** 26:01 Yeah, I think for HTTP… We didn't stabilize those… Anyways, so maybe we can just move this straight to post-stability.
**James Thompson** 26:19 But on HTTP, you actually have it on the span, the attribute.
Right? For RPC, these aren't on the spend. They're not on the… I can't see where they are diffused.
**Trask Stalnaker** 26:31 Oh, I see what you're saying, is the… in… I thought you were saying we didn't have instrumentation capturing them, but you're just saying that the… RPC span page here doesn't list them.
**James Thompson** 26:44 Yeah.
**Trask Stalnaker** 26:47 Sure, I will make that note.
Here…
**James Thompson** 27:12 Yeah. The only spot I can find it is on the span events, and we already have an issue to rewrite those.
**Trask Stalnaker** 27:24 Right. Yeah, I mean, so for… This would be probably one of those cases where we would have different behavior for unary versus streaming.
**Liudmila Molkova** 27:40 Yeah, and these are also the message attributes, so I would imagine If it's a single message, it can be on the… Span?
On the… the request span, right?
If it's streaming, then… and if we tackle this… Then message… Per message, things would be… Whatever it will be. Anyway, yeah, we probably… We can do… If we don't do streaming, we still can do this possibility, nothing stops us from adding this attribute after, or a metric, right?
**Trask Stalnaker** 28:32 Yeah… Yeah, so, I mean, I'm tempted to just… Drag this straight to post stability.
And if we clean it up along the way, we clean it up along the way, but it's not something that… Yes.
Yeah.
Alright, so… let's look at our to-do list.
And… Maybe we can make some… Goals for next week.
This one… Let's drag to the top. This one, I think, is important to get in early.
Before we start landing other… So, I will… oh, you have, nice comment here.
**Liudmila Molkova** 30:02 Yeah, so I was… I was checking if… Anybody uses the current warning with some constability opt-in.
**Trask Stalnaker** 30:13 Oh, right.
**Liudmila Molkova** 30:14 And the answer is yes, but only JavaScript.
So JavaScript actually follows it literally, and if the HTTP opt-in is enabled, then it sets server address and port.
I think they can keep doing this, and in addition, they can support RPC.
But… they… it's… I think it's up to them whether they decide to drop HTTP or keep it.
So I would be in favor of just… replacing what we have with HTTP… oh, sorry, with RPC and, forgetting the previous version of the blurb.
**Trask Stalnaker** 31:33 Yeah.
Okay, I will… But… not… not a… that's an easy one. I will go ahead and… Put my face there.
Let's see…
**James Thompson** 31:56 I just put it on the agenda, too, that it could potentially be moved to in progress.
**Trask Stalnaker** 32:03 Yeah, and this one, I'm gonna put, your face there.
So you have a draft PR for that.
Date status of 2-22… Let's see… Find our PC… Attributes on invalid requests.
Alright. That's it.
**James Thompson** 32:36 So that's where we spoke about having the dedicated pages?
Alright, rather than just having a page for JSON RPC saying, here's the attributes, we instead have a page, here is the JSON RPC span.
**Trask Stalnaker** 32:52 Right.
Okay, and so you have a PR… for that…
**James Thompson** 33:02 Yep.
**Trask Stalnaker** 33:03 Yes… Yes.
RPC, so this creates… So we have…
**James Thompson** 33:17 Because chasing RPC wasn't even a defined system.
**Trask Stalnaker** 33:23 Okay, okay, and so… Okay, so… Lydmila, do… do you have any preference for the… is there any reason to order these one way or another, of creating this page first, and then renaming?
These, or just kind of leaving them as is until we…
**Liudmila Molkova** 33:48 I don't have a preference, the only thing I would, I would like to update the naming, update our PC conventions to the latest naming, but I don't want to clash with other pull requests. So let's, try to merge those, and then I can… I'll follow up with the naming.
**Trask Stalnaker** 34:13 Right, yeah, yeah, good point.
So… what do we got here?
Got… a server… So we've got a new system ID.
I'm just kind of scanning, trying to figure out if this is an easy one for us to…
**James Thompson** 34:51 Yes, so literally what all I did was… we had our standard client service span. I wrote JSON RPC span, which extends those, and added the JSON RPC attributes listed on that page.
So that way, whatever was already on the standard span came straight across, and it just added the JSON RPC-specific attributes to it.
**Liudmila Molkova** 35:17 Yeah, you mentioned the JSON RPC didn't exist, and just the most.
**James Thompson** 35:23 Correct.
**Liudmila Molkova** 35:23 Ugh.
Do we want it to be JSON RPC, no spaces? Should it be JSON underscore RPC? I think that it should be underscore RPC, right?
**Trask Stalnaker** 35:37 So clearly not dot.
**James Thompson** 35:39 Yeah.
Right? The reason I did it without spaces, without pythons, is because that's what the descriptions were all saying to use.
So, it was mentioned in the description, use this.
But it just wasn't defined.
**Liudmila Molkova** 35:54 The Litmus test trust, you invented the domain name. It's JSONRPC now.
**Trask Stalnaker** 36:00 Oh, yes, there we go.
Alright, let's do it.
**Liudmila Molkova** 36:08 Cool. The other thing is, we, like, I know it's, it's problematic right now, it's not perfect, but we don't usually put the, the system inside the attributes, because then it creates confusion. You're saying, okay, the RPC system is this, and then you also have this list of other systems. I don't have a strong preference, and we'll eventually fix it.
**Trask Stalnaker** 36:36 What did we do for database?
**Liudmila Molkova** 36:39 We don't put it on the specific, I'm opening up…
**Trask Stalnaker** 36:47 How do we even do that?
Oh, we just, like, literally don't list it here in the rep?
**Liudmila Molkova** 36:52 Will it… yeah.
**James Thompson** 36:56 But it's a little bit more than that, though. It's… you can't inherit from the baseband.
**Liudmila Molkova** 37:04 We get creative.
**James Thompson** 37:08 Yeah.
Alright.
Alright.
**Trask Stalnaker** 37:14 But I agree, it's not a… it's, for… especially given that, the problem with the database one was more egregious, because there were, like, 50, and it was really long.
**Liudmila Molkova** 37:28 Yeah, I mean, we can ignore this here as well.
We are great to ignore it.
**Trask Stalnaker** 37:33 Let's see, what's the… so… Whoa.
I think let's just create… an issue.
**James Thompson** 38:28 But the problem I have is if you remove it, if we were to do code generation, the span would lack the attribute.
So it would be a blocker to spend card generation, but there is no span card generation today.
I thought Go was doing it.
**Liudmila Molkova** 38:46 Go is doing metric generation.
**Trask Stalnaker** 38:51 I mean, it would be… ideally, we would have a way just to not render it.
Or to make it hard-coded in the… span, definition.
**Liudmila Molkova** 39:06 Yeah, so ideally, and I think James has a proposal, the thing we should tackle in the tooling, that we should be able to define enum, and then when we reference the enum attribute, we should be able to say, oh, okay, I'm only using this specific value, And once the tooling supports it, we would definitely reference this attribute, right? It appears on the spans, we should reference it.
For now, it might create too much confusion.
**Trask Stalnaker** 39:40 And it's definitely not a stability blocker.
because we stabilize database… I mean, we can do… Whatever we did.
for databases.
What did we do?
How do we solve that for databases?
**Liudmila Molkova** 39:56 We just say in Markdown that this attribute should be there, and it should have… it must have this value.
**Trask Stalnaker** 40:03 Oh, okay.
Got it. So we… yes, so the span generation… We prioritized the markdown over the span generation for now.
**Liudmila Molkova** 40:14 Yeah.
**Trask Stalnaker** 40:15 I think we should, just for consistency, I think we should do the same in our PC.
Until we have a better solution.
I'll just leave a comment here.
**James Thompson** 40:33 Are we using sampling-relevant attributes? Because If we do them, that also needs to be copied across, because you can't inherit from the baseband.
**Liudmila Molkova** 40:46 Yeah, so in the markdown, we mentioned that for databases, that the system name must be set to this and provided that span creation time.
**James Thompson** 40:58 Yeah, no, but more than that, it's the other attributes as well.
Right? Because… You can only specify sampling relevant on the span definition.
Right?
**Liudmila Molkova** 41:12 I mean, we solved it for databases, we can solve it in the same way for our PC.
**James Thompson** 41:17 But on database, it's not consistent, though.
Some databases have namespaces sampling relevant, some of them don't.
**Liudmila Molkova** 41:26 And actually, we've spent a fair amount of time on this one, and it's probably intentional, so… Let's… let's focus on our PC system for now.
It's… for this, we can probably be consistent.
**Trask Stalnaker** 41:52 I guess I'm sorry I got lost.
So, if we look at MySQL… sampling…
**Liudmila Molkova** 42:06 So we don't mention it here, because we… we can't… But unfortunately, we have the sentence in the beginning.
that says… .
**Trask Stalnaker** 42:17 Sorry, we don't mention what here.
**Liudmila Molkova** 42:20 the DB system, right?
**Trask Stalnaker** 42:23 Oh, I see what you're… okay, sorry, yes, it took me a while to catch up.
I see, it must be set and must be… yeah.
So, let's just do, James, the exact same thing as over… I mean, I think this is… A good example to copy from.
Because I'd rather stay consistent with data… what we did in database, and then, you know, as there's a… in the future, we can do better, but… if… to me, if it was good enough to stabilize database, it's good enough to stabilize RPC, which is… my… only goal in this SIG.
And you put one other on here… River. Aww… Conventions…
**James Thompson** 43:48 So the same approach was done for the, the other two pages, I think it was.
Right, the gRPC page.
And the Kinect, obviously.
Right? So, the adjacent RPC page, a gRPC page, and a KinectRPC page.
**Trask Stalnaker** 44:08 Oh, in…
**James Thompson** 44:10 separate PRs.
There's one PR per system.
**Trask Stalnaker** 44:14 Okay, so… Our PC… Connect…
**James Thompson** 44:33 Did you say there was one for gRPC?
Yes?
**Trask Stalnaker** 44:39 There we go, okay.
And… is this tied to… An issue, no. Okay, so let's put it on the…
**James Thompson** 44:51 So they are tied to an issue, but they're tied to the same issue.
Right, because the problem you have is if you have multiple PRs to one issue, as soon as one of the PRs closes, the issue gets closed.
**Trask Stalnaker** 45:06 Yeah, okay, that's fine. let's, we can just… I think it's good to add the… I like to add the PRs directly to the board anyways, in progress, because it makes it easier to find them.
And… We're almost out of time, but I think we're doing good here.
Database, RPC… What am I doing? In progress.
Yes, and… What was the other one you said? Connect… gRPC, and what was the other?
**James Thompson** 45:59 JSON.bc, which is the one we discussed earlier.
**Trask Stalnaker** 46:16 Alright… So… Okay.
So, Lyudmila, let you and I… or actually, James, if you can today, since this is your day of starting, or whenever you can.
update these three PRs to follow the existing database, semantic convention format.
**James Thompson** 46:43 Nope.
**Trask Stalnaker** 46:43 And then, Lydmilla and I will try to get those, reviewed and… Quickly, so that… They don't cause merge conflicts for other changes.
**James Thompson** 46:58 Yep.
**Trask Stalnaker** 47:00 Awesome.
**Liudmila Molkova** 47:01 We… yeah, we then should wait for… if we happen to release semantic conventions, we should wait until we have the blurb.
Right.
**Trask Stalnaker** 47:12 Oh, yes, yes, okay. Do we put the blurb… We don't put the blurb on these individual ones.
Right.
**Liudmila Molkova** 47:22 Didn't we do?
But also, it's not… there is nothing breaking in those PRs, they're just describing spans instead of attribute groups, so we're good to go regardless.
**Trask Stalnaker** 47:34 Okay.
**James Thompson** 47:35 Yeah, it's describing the current state.
**Trask Stalnaker** 47:37 Yeah, yeah.
I think we're not today.
But okay.
Yes, sounds good. Alright.
Wonderful, thank you. Thanks, everyone.
**Liudmila Molkova** 47:50 Bye.
**Trask Stalnaker** 47:51 See ya.
