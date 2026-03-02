SIG: RPC Sem Conv Stability SIG
Date: 2025-10-29
Duration: 26 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 02:15 Hello!
**Trask Stalnaker** 02:17 Hey, folks.
**Liudmila Molkova** 02:21 Give me a sec.
**Trask Stalnaker** 02:26 I'm only gonna be able to make the first 15-20 minutes here, then I need to drop…
**Liudmila Molkova** 02:35 Okay.
**Trask Stalnaker** 02:36 And Steve, sorry, I just posted in the Java channel, I won't be able to make the APAC Java meeting today.
**Steve Rao** 02:44 Oh, okay.
**Trask Stalnaker** 02:47 Ping… ping me if there's anything that… Books.
**Steve Rao** 02:52 Okay, yeah, there are some, issue, some folks, posted today, and I will let them to ping you on Slack.
**Trask Stalnaker** 03:02 Okay.
**Steve Rao** 03:03 Same thing.
**Trask Stalnaker** 03:04 X.
**Liudmila Molkova** 03:07 Oh, thank you. So then, maybe we can,
I'll write to see if we can make progress on the discussion last time.
It… Sounds like… We've been talking about two different… pieces, 1S…
the spec… what are we instrumenting, right? Which layer, maybe?
And I also… Through the protocols that we have.
which of them… are… Woof would include?
And those, those are related discussions.
**Trask Stalnaker** 03:56 Yeah, I think, I mean, which ones is not… I think we can make…
That decision easily, once we decide which… What layer, or… Yeah.
**Liudmila Molkova** 04:13 Yeah, I… I've been checking… what GRPC does, and what our instrumentations do.
for gRPC.
So they do… Consider retries part of the protocol.
And they… we would create… they would hand over trice on some low level.
Below our instrumentation.
So if you…
Use… okay, so if we look into what official, like, they also have their own tracing instrumentation.
They have, Grpc call level?
And this is the same what we have, in auto instrumentation.
They also have a temp layer.
And this was only in the gRPC native.
You need non-native plugin or something.
So… It's kind of different depending on the protocol or framework. If
I understood correctly for the Connect RPC,
They don't consider retries,
part of the protocol, but I didn't spend enough time on this.
**Trask Stalnaker** 06:03 I see what the argument you're trying to make, that gRPC actually, as part of their specification, define retries.
**Liudmila Molkova** 06:17 Yes.
And in their telemetry, they consider those as two different things, protocol, attempt, and, I don't know, library, or…
How do we call it?
**Trask Stalnaker** 06:31 Yeah.
Logical, physical.
**Liudmila Molkova** 06:40 Logical, physical, but there is also HTTP.
They're just… I'm curious, Steve, how do you think about it from Dabo perspective?
**Steve Rao** 06:53 You mean the protocol or framework?
**Liudmila Molkova** 06:57 Yeah, I remember we talked last time, and you mentioned that You probably consider, like, the… the outer layer…
more important, but you would also be interested, maybe, in both layers. Do I remember correctly?
**Steve Rao** 07:13 Yeah, maybe, yeah, I also, yeah, take a look about HTTP, semantic convention.
And,
Yeah, maybe, I, I, I, I, I saw DAI is, DAI is an attribute called, RBC protocol name.
in HTTP.
So…
**Liudmila Molkova** 07:41 The network protocol name?
**Steve Rao** 07:45 Http protocol name.
**Liudmila Molkova** 07:52 I mean, network.
Oh.
Whatever.
**Steve Rao** 07:57 you can scroll up HTTP…
**Liudmila Molkova** 08:07 We haven't… Network protocol name and network protocol version.
**Steve Rao** 08:18 Oh, network protocol name, sorry.
Yeah, so, in, HDDP's many convention, so we don't, we consider, it as a protocol.
We don't, record the, framework information in semantic convention.
**Liudmila Molkova** 08:40 Not for HTTP.
**Trask Stalnaker** 08:46 So we have kind of,
I mean, we have both sides. We have comparing HTTP and database.
Database, we made the decision that it was a logical
span. The span, it was, like, a logical operation, even if there was, like, multiple underlying Requests?
HTTP… We kind of… We said…
that is more of a… that is a protocol. I guess we're saying that's a protocol, and maybe that's the difference with database…
Is maybe not a protocol, maybe it's not really
protocol instrumentation, whereas HCB, we're saying it is, so ideally, we would capture the retries, each one, but we…
Can fall back to just capturing the outer… Which… You know, makes me…
lean, I think, towards RPC being also logical.
Similar to database.
Where does that… Where would that put us if we played out?
Treating it as a logical…
**Liudmila Molkova** 10:18 Let's try playing it out.
We would probably call it RPC… Sorry, RPC… System or framework name?
**Trask Stalnaker** 10:36 Just, yeah.
**Liudmila Molkova** 10:40 We would… Probably… well, we would define everything around coal.
I would imagine that we would say that Individual systems can define their own…
Tri-spans, but we probably would need to cover them.
**Trask Stalnaker** 11:05 Yeah, what would our system names be?
**Liudmila Molkova** 11:17 The same as we see today?
I would imagine double.
**Steve Rao** 11:29 Yeah.
**Trask Stalnaker** 11:31 Yeah, and not triple.
**Steve Rao** 11:35 kudos.
**Liudmila Molkova** 11:35 Not terrific, but there could be…
**Trask Stalnaker** 11:40 A network protocol name.
**Liudmila Molkova** 11:48 I still don't know how to call, maybe triple as well, it's… It's an interesting choice, Rick.
**Trask Stalnaker** 11:56 True, because, yeah, yeah, because that's just HTTP, yeah.
And Double could have its own…
Attribute to… if it… if we care to differentiate triple.
What other problems?
Right.
**Liudmila Molkova** 12:43 So the thing you mentioned before, that they kind of like, that if you… if you have a client double.
And the server gRPC.
in this… world.
We don't reflect that they use the same underlying critical.
Yeah. So, maybe it's both.
**Trask Stalnaker** 13:08 But I, I… I think that's okay, though, because we have that same problem, like, with
DB system name might be… Mongo, but on the server side, it might be Cosmos DB.
**Liudmila Molkova** 13:29 Right.
**Trask Stalnaker** 13:32 And… Messaging, we have the same…
Examples.
**Liudmila Molkova** 13:44 or HTTP client talking to… Double server.
We wouldn't solve, regardless.
**Trask Stalnaker** 14:01 Yeah, and I mean, I like the… I… I'm attracted to… Doing the, the protocol layer,
But I just… I am… we've been going down that road, and it just feels… very difficult.
**Steve Rao** 14:28 Yeah, you mean to give the, use the protocol, IPC protocol?
them to… to, to make a, S projection.
of abyss.
**Trask Stalnaker** 14:42 Yeah, to define the semantic convention, the RPC semantic conventions, at the protocol, trying to define it at the protocol layer.
**Steve Rao** 14:53 Okay.
**Trask Stalnaker** 14:57 where we would, you know, define it at the triple layer, at the double 2 layer, at the gRPC over HTTP.
I don't know, I…
**Liudmila Molkova** 15:25 The other problem that the physical, it seems interesting, but it seems less practical.
And so…
**Trask Stalnaker** 15:33 Yeah.
**Liudmila Molkova** 15:34 I do have…
**Trask Stalnaker** 15:39 Sorry, go ahead.
**Liudmila Molkova** 15:41 No, that's it, so we will just track something that users don't necessarily observe directly.
**Trask Stalnaker** 15:49 Yeah, and that's hard to… instrument. It's hard to instrument at that layer.
And I think we have a good…
Prior art in making the choice for database.
Semantic conventions to be defined at the logical layer… span layer.
**Liudmila Molkova** 16:17 Right.
**Trask Stalnaker** 16:20 And things just got a little bit more…
less obvious. It was… seemed… it was more obvious for database, it was… seemed less obvious for RPC, because…
It's closer to that there's some blending there with the protocol?
**Liudmila Molkova** 16:38 Yeah, and it… yeah.
I think gRPC is… I'm just maybe not familiar enough with double, but gRPC seems to be…
Way too complicated, and it makes, like, request hedging as a part of the protocol.
Which also means a lot of requests in parallel. I think double includes service discovery and load balancing, right? So it's also…
**Steve Rao** 17:09 Yeah.
**Liudmila Molkova** 17:10 complicated.
**Steve Rao** 17:12 Yeah.
Yeah.
**Liudmila Molkova** 17:19 Okay, so then I would say it out loud. Should we align on the logical layer, and say that physical is the…
Specialized thing we don't even target in this iteration?
**Steve Rao** 17:36 Okay, I have a small question. When we defined the HTTP azymatic convention, we defined, it in physical layer.
Or…
**Liudmila Molkova** 17:49 HTTP, yes. HTTP is… Physical, as physical as you can get.
**Steve Rao** 17:55 Yeah.
I don't see any attribute, they are, strongly related to, framework such as OKHTTP or, a sync, HTTP client, something like that.
**Liudmila Molkova** 18:11 Yeah, because it's… it's essentially… if we could map it there tightly to RFC, like, we try to map it as tightly as possible to RFCs, and they… it's a standard, we don't… we don't care for HTTP.
**Steve Rao** 18:25 Okay.
**Liudmila Molkova** 18:32 So the RPC, at least in my view, it's the layer above, and it's not… formalized.
**Trask Stalnaker** 18:45 I like it.
I think at least it… Give, like, unblocks us.
also… Because this… has been difficult. We've kind of… Been talking about this.
Stuck on this for a few weeks.
**Liudmila Molkova** 19:11 So, I think we can…
document it, and then we can review the PR, spend some time thinking about it, and finally, if we approve the PR,
That would be the way to go.
**Trask Stalnaker** 19:27 Currently, we have rpc.system, is that…
**Liudmila Molkova** 19:31 Yeah.
**Trask Stalnaker** 19:31 So we would just do rpc.system.name. All right.
Cool. Sorry I gotta run.
I will.
Catch up with y'all later.
**Liudmila Molkova** 19:45 Yeah, thank you.
**Trask Stalnaker** 19:46 Bye.
**Steve Rao** 19:48 Bye.
**Liudmila Molkova** 20:03 Okay, I would love to discuss…
Maybe some open PRs? Do you folks have anything,
Like, any preference, anything in particular you want to bring up?
Okay, so then, James, I have a question for you, and maybe we can discuss it and cut it short?
After… So, I have this… Rule request… where is it?
Sorry.
This one.
No.
Which one of them is pull request?
Here we go.
So, we had some conversation on RPC, status code back and forth. There is…
One thing I don't understand from your comment, would you mind explaining?
What is this? What is it related to?
**James Thompson** 21:20 Damn.
Let me…
So, if you look at the… description for… Error.type, the general one.
Right? It directly calls that using the gRPC status.
Throughout all the documentation.
Right? So, on a lot of pages, it says, use the gRPC status.
That's true.
**Liudmila Molkova** 22:06 True, perfect.
**James Thompson** 22:09 It's not… hasn't been changed in this?
Huh?
But it was already there because we had that dedicated attribute.
**Liudmila Molkova** 22:20 Sorry, so let's, let's take a look.
Let's say we look into jerky heat.
This is, this is a generic description, right?
**James Thompson** 22:40 Yep, right. And so, if you look at the line above the dot points.
Which one?
Above the dot points.
**Liudmila Molkova** 22:53 points.
**Steve Rao** 22:54 Yep.
**James Thompson** 22:55 The dots.
So, see where it says number 6?
**Liudmila Molkova** 23:02 On a 6.
**James Thompson** 23:04 You go up 3 lines.
**Liudmila Molkova** 23:06 Oh.
Yes, we need to override this generic error type node.
**James Thompson** 23:12 No, and it needs to be updated. The base note needs to be updated, because that's across everything.
**Liudmila Molkova** 23:19 Oh, this node should be overridden in the RPC conventions, this is generic error type definition.
**James Thompson** 23:27 Yes, but if you leave it as is, and you look at database.
then you'd say, use the gRPC status code.
**Liudmila Molkova** 23:38 Wait, so in the databases, the databases override this generic description already. We would need to override it for the gRPC. The question is, do we do this here in this PR? And I can certainly do this.
**James Thompson** 23:53 I would update the base note to say, remove the example of using the gRPC status code.
Cause you… cause what does it say?
What?
**Liudmila Molkova** 24:07 I see what you're saying, because the gRPC status quoad is… It's… oh… Okay, yeah.
**James Thompson** 24:15 Yeah, so the next point is use a domain-specific attribute.
**Liudmila Molkova** 24:22 Yeah…
I see.
Great.
Let me… Make sure I capture it.
Okay.
Cool, thank you.
That is all I had. I think the rest is… do you want to talk about it? I… I…
I think, you're… I'm not sure if you've seen the comment.
**James Thompson** 25:49 No, I haven't, but it's fun.
**Liudmila Molkova** 25:55 Okay, so then, maybe if you want to take a look, go ahead and take a look, I'll update the PR with your comments.
And… This is all I had.
Okay, so then, let's cut it short.
Okay.
**Steve Rao** 26:21 Okay, okay, bye.
**Liudmila Molkova** 26:23 Have a good day.
**Steve Rao** 26:24 Yeah, have a good day.
