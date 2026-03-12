SIG: RPC Sem Conv Stability SIG
Date: 2025-10-01
Duration: 48 minutes
Zoom Recording URL: https://zoom.us/rec/share/bU2OU2hkprb1bDg8nTT7BMhtVfkkwBXe2mPbY4ZxYUdD9mv7osxTBYyNIYQjdxf1.nFaK8dVREsxwB_x6
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 02:37 Hello!
**James Thompson** 02:45 Hey.
**Liudmila Molkova** 02:57 Okay, let's get started.
Present.
**Trask Stalnaker** 03:24 3 bucks.
F-1 team.
**James Thompson** 03:35 Here, we're gonna…
**Trask Stalnaker** 03:36 Hmm…
**Liudmila Molkova** 03:45 Is it October? Okay.
**Trask Stalnaker** 03:47 It is! I know.
**Liudmila Molkova** 03:56 Do we have anyone else? Not yet.
Okay…
**Trask Stalnaker** 04:01 It was October yes… it's already October 2nd for James.
**James Thompson** 04:07 Yep.
**Liudmila Molkova** 04:25 Okay, let's take a look at the project board.
What do we have there?
So I think we should take a look at the open PRs, and… see if we can merge anything… I think we've merged pretty much everything.
**James Thompson** 05:07 Yep.
**Trask Stalnaker** 05:07 I think we can merge the RPC stability warning.
**Liudmila Molkova** 05:14 Alright.
This one, I think, is pretty close. I've left a comment.
**James Thompson** 05:27 Yep.
**Liudmila Molkova** 05:28 on… Service and method.
The rest seems to be issues. Oh, right, there is the… this one.
We need another approval.
**James Thompson** 05:46 But… Nope.
**Liudmila Molkova** 05:55 This is an issue right.
This is an issue.
**James Thompson** 05:59 Yep.
**Liudmila Molkova** 06:03 this… the SRPRs, there is not much to discuss there.
**James Thompson** 06:11 Can we look at… the… automatically adding issues to the board when they have the RPC label?
Chris, there has been a couple additional Issues raised.
**Trask Stalnaker** 06:32 projects is the one part of GitHub that I don't know well.
**James Thompson** 06:37 Or auto-add to project on the left-hand side.
Right.
**Liudmila Molkova** 07:04 But it would not change anything for… Existing issues.
**James Thompson** 07:10 The water?
**Trask Stalnaker** 07:11 Click on the… click on the ad… let's see… Oh, I see. It's gonna add, okay.
We can try it, remove the label and re-add it on one.
**James Thompson** 07:27 But I remember seeing a way that it will automatically trigger it to run.
I just can't remember exactly where that is.
**Liudmila Molkova** 07:35 We've just done it, right?
**Trask Stalnaker** 07:47 Oh, maybe I did do it.
Oh, no, I see, it's not on there. Okay, sorry.
**Liudmila Molkova** 08:04 Yep.
**Trask Stalnaker** 08:07 Alright…
**James Thompson** 08:13 And that way we can see when the new should come up, they have the no status, and we can… Triage them accordingly.
**Liudmila Molkova** 08:24 Yeah.
**James Thompson** 08:38 Up, up it.
**Liudmila Molkova** 08:41 So this one… okay, so you've created a couple of new issues.
**James Thompson** 08:45 Yep.
**Liudmila Molkova** 08:47 The one for duration I just moved to to-do.
**James Thompson** 08:54 Yep.
**Liudmila Molkova** 08:55 And there are… message size… I think we don't need to stabilize, I would exclude it from the initial stability.
**James Thompson** 09:06 Nope.
Would we want… would we want to move it to… a beta?
Alright?
Or something?
Like, don't fully stabilize it, but progress it.
From development.
**Trask Stalnaker** 09:26 We don't really have, any prior art?
For that, we've gone… We've always gone… not that there isn't a place for that in the future, but we've always gone just development to RC, to stable.
So that would be something we'd have to figure out in the general SEMCOM meeting, I think.
**Liudmila Molkova** 10:01 Let's put it past stability, and let's try to focus on the things that we are targeting for stability, and let's not get distracted.
**James Thompson** 10:09 Yep.
**Liudmila Molkova** 10:11 Okay, what else do we have?
I created an issue, this one… We… I want to remove network type from our PC, we don't have it in HTTP, it's not super helpful.
And I propose to remove it from RPC.
**James Thompson** 10:36 Can you update the title?
**Liudmila Molkova** 10:38 Sorry?
**James Thompson** 10:39 Can you update the title?
Alright, because it says remote network type from.
**Trask Stalnaker** 10:45 Oh, I didn't catch that. There's a typo.
**Liudmila Molkova** 10:49 Right.
**Trask Stalnaker** 10:55 Yeah, if it's not on HTTP, it shouldn't be on our PC.
**Liudmila Molkova** 11:01 Okay, we'll put it on to-do, and it's super straightforward.
**James Thompson** 11:07 Done.
**Liudmila Molkova** 11:11 The stool we used to have, I think they're…
**Trask Stalnaker** 11:13 Do we want to try to assign it to Copilot?
**Liudmila Molkova** 11:18 Can we now? Can it create forks?
**Trask Stalnaker** 11:24 I don't know, it should… where… I thought I had set it… Let's see which repos… Enabled it on… If you go to that, you'll see right away if you go to the issue and see if Copilot is there.
**Liudmila Molkova** 11:50 I just assigned a DecoPilot.
**Trask Stalnaker** 11:52 Okay.
Yes.
So I had… I had added semantic. So we have to… Maintainers have to request for it to be added, and I, as a maintainer of this repo, requested for it to be added.
And we have to enable, EZCLA co-author checks.
Which is a new feature from EZCLA. That was a request from Couple folks in the GCE.
Initially that rollout had problems, but they got that sorted, so…
**Liudmila Molkova** 12:30 I think… I think that it… it previously stuck because it can… it tries to push to origin.
And it does not have forks.
**Trask Stalnaker** 12:40 Boom.
That might just be branch protection rules that I need to fix.
**Liudmila Molkova** 12:50 Well, let's see, let's see what happens.
**Trask Stalnaker** 12:51 Yeah.
I'll get that fixed, because we are using it in other Repos.
**Liudmila Molkova** 13:00 Nice.
Oh yeah, yeah, I need to…
**Trask Stalnaker** 13:08 Update the branch protection rule.
**Liudmila Molkova** 13:10 It failed?
**Trask Stalnaker** 13:11 It's… I need to add a… I can see, I need to add a branch protection rule for it to succeed.
**Liudmila Molkova** 13:20 Okay.
Okay, so moving forward, what should we try to solve today?
**James Thompson** 13:33 I also put in the agenda the fi… findings from the research I did.
The… yep, that one.
**Liudmila Molkova** 13:48 Mmm… So, Kate, can you summarize?
**James Thompson** 13:57 So the summary is, it's used by… the OpenConnect protocol, the Connect RPC protocol, those metrics.
Right? And what they actually seem to be is counters of how many messages are sent.
**Liudmila Molkova** 14:15 Right.
**James Thompson** 14:16 Alright.
So… It's… the metrics as they stand don't really convey that's what they are, but that's how they've been used.
And… When you know that, then it does make sense, but you don't… it's not intuitive to know that.
**Liudmila Molkova** 14:35 And this is part of streaming, effectively. It doesn't make sense outside of streaming, and streaming our… Thread you go.
**James Thompson** 14:45 But it also covers how many messages are sent, so how many requests are made.
**Trask Stalnaker** 14:52 We get that via the duration histogram.
The count on the duration histogram.
For unary, or whatever, non-streaming.
**Liudmila Molkova** 15:13 Yeah, so we know that these names are not great, and even if we want to keep this metric.
If we deprecate it now, Connector PC can happily use it going forever until there is something better.
**James Thompson** 15:28 Yep.
Right, or do we just update the description now?
Alright.
And then potentially rename it later.
**Liudmila Molkova** 15:38 So I sent a PR to deprecate them.
**James Thompson** 15:40 Without any update, like…
**Liudmila Molkova** 15:43 Zero, updates to the metric themselves, just deprecation.
**James Thompson** 15:48 Yep.
**Liudmila Molkova** 16:03 If we get to the streaming, we can figure out that this is a useful metric, and this is where we would rename it to something.
Cool.
**Trask Stalnaker** 16:19 Makes sense to me.
**Liudmila Molkova** 16:48 Okay… Back to the board.
I can continue…
**James Thompson** 17:04 I think a quick one might be the… the gRPC attributes.
Alright, so there is an issue that talks about… Alright.
Aligning… and let me just quickly look at the board.
**Liudmila Molkova** 17:20 Alignment was jerky.
**Trask Stalnaker** 17:21 Oh, yeah.
**James Thompson** 17:23 There's not… there's a… there's a smaller one.
That's what… talks about the gRPC error code.
Yeah.
So, do we… rather than going… Do we instead go gRPC.status?
then that way we have alignment with what the gRPC semantic conventions already have.
**Liudmila Molkova** 18:00 That's an interesting question. So, the first thing, we have plenty of status codes in RPC conventions.
So I think Connector PC has one.
**Trask Stalnaker** 18:18 We should check what that… Yeah, will you go to the link?
For the ConnectRPC… sorry.
**James Thompson** 18:26 That's the number.
**Trask Stalnaker** 18:26 Right.
**James Thompson** 18:28 It's a number that's totally different.
I believe.
Oh no.
It connects.
**Liudmila Molkova** 18:38 It's a code…
**Trask Stalnaker** 18:40 Chosen to match… That's interesting. They say it's chosen… They're HTTP status codes, but they're chosen to match GRPC I'm confused.
Oh, I see, the code, okay.
Interesting.
**Liudmila Molkova** 19:20 Is this the API construct?
Or the protocol construct.
Oh.
Oh.
**Trask Stalnaker** 19:42 Looks like protocol…
**Liudmila Molkova** 19:45 Yeah.
And it's a string.
And there is also… so let me copy… And we also… Chair, PC State of Squad.
Which is an integer.
**Trask Stalnaker** 20:26 Oh…
**Liudmila Molkova** 20:33 I also… of JSON RPC status code. Error code, okay, which is… integer.
**Trask Stalnaker** 20:46 What?
Do we have a link?
to that.
definition.
Codes. Oh, wow.
**Liudmila Molkova** 21:27 And, let me guess, we probably… Would have more if we had more documented here.
Yeah, we… in database, we chose to… Invent database generic code.
**Trask Stalnaker** 21:48 Can you pull up what we did for database?
Forget.
**Liudmila Molkova** 21:52 Hmm.
So… And…
**Trask Stalnaker** 22:15 I assume it's a string, yeah.
**Liudmila Molkova** 22:18 It's a string, and we document… What it is in each individual convention.
**Trask Stalnaker** 22:31 How's its advantages?
and disadvantages.
I, I suspect… Backed for… For databases, there were so many that it would have been probably overwhelming to split them.
for RPC… It could seem… Maybe having different ones?
But… I do like the… The reason we've used previously about, Consistent dashboards.
Metrics, even, because that's a low cardinality attribute, so…
**James Thompson** 23:22 Isn't there guidance that you should split it?
Also, in the documentation.
**Liudmila Molkova** 23:30 Splate it?
Good evening.
**James Thompson** 23:32 Yeah.
Right, so have a separate attribute.
Right, for ConnectRPC versus gRPC… Right? Because I remember reading that when there is a more specific A, dedicated attribute should be used, or something to that effect, I remember reading.
In the guidance. Documentation.
**Liudmila Molkova** 23:57 I think we have guidance that it's a tricky balance between generalizing or not generalizing.
So this is the place where… It's a tricky balance.
**James Thompson** 24:15 Yeah, like, I think for gRPC, it might make sense to have a separate one, so… because that way, we're always in alignment with the… metrics and that published by GRPC.
Right? Because I look… Otherwise, that's just another source of differentiation between the open optometry definitions and the GRPC.
**Liudmila Molkova** 24:41 It's not just the only discrepancy between gRPC metrics and what, hotel semantic conventions there is effectively Nothing in common, and having… So they call it gRPC that's status. Would they call a gRPC that's status? Not sure.
So we either say we… Also call it gRPC.method.
**Trask Stalnaker** 25:12 And right now, we have a generalized RPC. method.
**Liudmila Molkova** 25:17 Right.
**Trask Stalnaker** 25:29 Yeah… Yeah, I'm nervous… leaning too far into gRPC being, like, the… only… Like, I know that the gRPC, folks, even when coming to this, were asking, you know, what are other RPCs, out there.
But I… Do you think there are… I mean, as we've seen, there are, and they are in use.
And so… I don't know why we wouldn't try to… generalize… The basics, similar to what we did for database, and… To be able to have… For products and, to be able to design dashboards for… instead of having to have for different dashboards, whether you're using gRPC, JSON RPC, Connect, Double… RMI…
**Liudmila Molkova** 26:42 Yeah.
So, the only alternative we could have, And it's partial alternative, right? So, we still have error type, which is generic.
Not all of the statuses are errors?
But most of them are.
So… We would…
**Trask Stalnaker** 27:14 Are most of them?
Errors?
**James Thompson** 27:22 If you have a look at the GIPC page, there is actually a summary table of which ones are errors and which ones are not.
Even on the open telemetry docs, there's a table that summarizes as if it's error or not.
**Liudmila Molkova** 27:40 Yeah.
Mmm.
Pretty much all of them are, but that's questionable. It's canceled an error.
We're not found.
**Trask Stalnaker** 27:54 Right, and from which side you're looking at? Like, the 4XXs?
Well, they're…
**James Thompson** 28:02 Yeah, and there's a summary table for that in the OpenTelementary docs.
As well.
**Trask Stalnaker** 28:08 But how… how does that… how would that help us, Lydnilla?
**Liudmila Molkova** 28:15 So if we… We will have… Error type on metrics, right?
**James Thompson** 28:22 Yes. And…
**Liudmila Molkova** 28:24 Where is the status?
**Trask Stalnaker** 28:28 Yeah, and that is the most important… I mean, more or less, most important.
Thing to be able to split by.
With the errors.
**Liudmila Molkova** 28:42 Yeah, so Dan, okay, so for the server.
We would not differentiate our K from canceled, or we would have… well, we would have gRPC flavor of RPC metric, right?
**Trask Stalnaker** 28:55 Right.
**Liudmila Molkova** 28:59 And… Would we actually assume… let's… let's say we had a dashboard, And would we use both error type and RPC status quoad there?
**Trask Stalnaker** 29:20 Doing database… I assume… We could verify.
**Liudmila Molkova** 29:28 Yeah, we probably do.
Yep.
Okay, so the reason to do this is, it will bring unification, and these concepts are close enough.
The reason not to do this, I think the only one that we don't want to convert integer to string.
Or, like, what… is there something specific and unique about the status codes that are actually benefit from them having different attribute names?
**Trask Stalnaker** 30:27 I mean, given that they're… We could potentially have enums… for them… In these cases, like, for the databases, there was no chance we were gonna have enums, because they have, like, thousands of status codes.
for the RPC… We could potentially have ENA, a different enum for each one.
Which… You know, be a possible… benefit.
**James Thompson** 30:58 Palm… about the palm you have there is… If you currently have gRPC and JSON RPC as an integer, Alright.
If you have others with integers, what if they're using the same integers?
Alright? You… and the integers mean different things.
**Liudmila Molkova** 31:21 It used to have the constant name somewhere saying what protocol is it, so you interpret this integer along with the protocol.
**Trask Stalnaker** 31:36 I mean, that's a good point in a… like, if we're talking about a generic dashboard… The generic dashboard, the error type is really going to be the useful thing to drill into, less so the status code.
**Liudmila Molkova** 31:57 Yeah, you would not include it as… we wouldn't break by it by default.
We would group by default by our type.
But this is a detail.
**Trask Stalnaker** 32:15 Yeah, yeah, and I mean, you're drilling in by also the RPC protocol name.
**Liudmila Molkova** 32:23 Right.
**Trask Stalnaker** 32:29 Yeah, I mean, given… A, we have precedence in databases.
And… B, the… we haven't… The complexity of the… vendor-specific or protocol-specific metrics. Like, we haven't really ironed that story out in semantic conventions, how we have, like.
RabbitMQ-specific attributes in the metric.
I don't think we ended up… Addressing that at all in the database.
semantic conventions.
Who would… the more paved path for us, I think, is unifying them.
**Liudmila Molkova** 33:31 The only reason I think we could regret it is if gRPC folks would come back and say we wouldn't want to align with you because you have this as a string, and we don't like it.
They would probably repeat this for any other attribute, any other unification we would try to do.
**Trask Stalnaker** 33:55 Yeah, I was a good… Question… Can you pull up their… attributes, again.
So, these are the, these are the only attributes Looks nice.
**Liudmila Molkova** 34:23 I'm sorry.
**Trask Stalnaker** 34:25 Okay.
So, JPC method… That is… Oh, there's… It is a string.
**Liudmila Molkova** 34:39 Hmm.
Okay, it is a string, but it's also an.
For us, it's an integer.
For them, it's a… Okay, so this makes things a little bit more straightforward.
**Trask Stalnaker** 35:07 The strings are nice.
It kind of addresses part of James's concern of, like.
If different numbers mean different things, the strings are… Way more self-explanatory.
It looked like the JSON RPC… was strings… also.
Sorry, the ConnectRPC. These ones looked like integers, the JSON are, yeah. These looked like strings, yeah.
The JSON RPC one looked like integers.
**Liudmila Molkova** 35:50 Dang… R.
**Trask Stalnaker** 35:57 Oh, there is a message there, possibly.
I don't know what they… oh, but they probably send back the…
**Liudmila Molkova** 36:22 Oops.
Okay, anyway, those are probably numbers.
Okay, so, the paved pass is… Unify?
The downsides… Not much, just… Into conversion, which is not a problem.
Brady.
**Trask Stalnaker** 37:14 Yeah, and do… do we think that all… RPC, frameworks, protocols have.
Status codes…
**Liudmila Molkova** 37:29 Let's see…
**Trask Stalnaker** 37:34 It's a holiday in China for this week and next week.
So this D said you wouldn't make it.
**Liudmila Molkova** 37:53 I think so… Wow, Dubo Triple Protocol seems to have it, And if they work on top of your PC… well, let's not touch it.
Seems WCF works on top of HTTP.
**Trask Stalnaker** 38:42 Yeah, thinking of, like, RMI… don't think RMI has a status code, because it sends just Java exceptions.
Is that a problem if… I mean, it's probably fine if, Protocol doesn't have something we would consider as a status code.
**Liudmila Molkova** 39:16 Right, we wouldn't just… We would just not reference this attribute trait.
**Trask Stalnaker** 39:22 Yeah.
**Liudmila Molkova** 39:35 Okay, so let's unify then.
**Trask Stalnaker** 39:40 Yeah.
Yeah, I think let's try it, go down that path, and… See if we get… Run into any problems, pushback.
**James Thompson** 40:56 Is it a response status code, though?
**Liudmila Molkova** 41:02 Why not?
**James Thompson** 41:03 or the… I'm thinking… the streaming case.
Alright.
If you're doing… Server-side streaming, if you're doing client-side streaming, Would that be a… If you lose… what would it be? Service streaming?
Right? It wouldn't necessarily be a response, because you haven't sent a request. So, how can you get a response status code if you haven't sent a request?
**Liudmila Molkova** 41:37 So this data squad is response to something, right?
**James Thompson** 41:43 If it's streaming, it's just… A status sent back.
Because you have a connection open.
But that status might come half an hour later, potentially.
It's not necessarily a correlation to your oppressed.
**Trask Stalnaker** 42:09 Are you saying that, like, a client might send a status code to the server?
Or the… if we're thinking of the person who initiated it being the client and the person who's…
**James Thompson** 42:24 It's immoral…
**Trask Stalnaker** 42:25 server.
**James Thompson** 42:26 More in relation to having the response.
in the naming.
Because response implies replying to something.
So you're… something's requested, and then you get back a response.
At least that's the way I look at it.
Alright, and if you're doing a streaming.
You don't necessarily have that request to be generating a response.
**Liudmila Molkova** 42:58 So if at some point, somebody just sends a message with the status code, to the other party.
They are probably replying, maybe not to the initial request, but to something that happened.
In the stream before.
And they're responding to the… Previous message.
**James Thompson** 43:27 But…
**Trask Stalnaker** 43:28 Let's look at those… the gRPC status codes again.
I want to see if Sue… Operation… canceled…
**Liudmila Molkova** 43:58 Those are probably associated with the… Or is…
**Trask Stalnaker** 44:03 pawns, because…
**Liudmila Molkova** 44:09 the content of the message is arbitrary, right? It's not part of the protocol. Protocol doesn't care.
**James Thompson** 44:21 Didn't you show before an example of where the status codes were streamed? I think it was the… was it the Kinect example?
Deconnect.
to connect RPC example, where the status codes were streamed.
**Trask Stalnaker** 44:50 I need to pull up, also, like, the… gRPC, Java… Library to see where they attach.
Status code… like, status… I'm trying to think, like, canceled.
is… does canceled… like, does the gRPC… Does canceled mean the server is sending back and seeing… hey, it was canceled. Probably you canceled it, but I'm sending this back to you.
Versus… Is canceled something that the client Sends to itself, or something, it's like a client-side status.
Versus, if it's something that's always traveling from the server The client, then it feels… Okay, to call it a response.
**James Thompson** 45:54 What… what about hedging in… because I know that there's been… there's issues for implementing… supporting hedging, Way… Wouldn't that also be a canceled status?
Where it fires off the request to multiple instances, and it cancels as soon as it gets a response back.
**Trask Stalnaker** 46:18 Yeah, but, like, see how this diagram right here? The cancel comes from the… the client is the one that gets… does the hedging, right? It gets back the first one, and it sends cancel to the server, and then the server… my question here is.
Is the status code coming back in number 4 completed? Is that the status code canceled?
That's my… Guess.
But it's just a guess at this point.
So in this diagram here, The client says on number 2, says, cancel.
Number 3 comes back, response, with the status code being canceled.
**James Thompson** 47:10 But what's… what's interesting is that… why is it a dotted line as opposed to a sold line?
In the diagrams, what difference does the dotted versus solid make?
**Trask Stalnaker** 47:27 Don't know.
**Liudmila Molkova** 47:28 remains a history.
But yeah, so let's take a look at the.
**Trask Stalnaker** 47:36 Yeah.
**Liudmila Molkova** 47:37 Right?
Yeah.
**Trask Stalnaker** 47:39 I think let's just leave that as a to-do.
And… do a little bit more research, yeah.
**Liudmila Molkova** 48:11 Okay, awesome, and we are at time.
Thank you, boss.
I'll be out next week, but I'll be back the week after.
**Trask Stalnaker** 48:25 Right.
See ya!
**Liudmila Molkova** 48:28 Cool. Thank you, have a good day.
