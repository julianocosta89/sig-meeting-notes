SIG: RPC Sem Conv Stability SIG
Date: 2025-11-06
Duration: 49 minutes
Zoom Recording URL: https://zoom.us/rec/share/K_14CHI0m5n5Yko_kddc9o5avPZ0lswZ80TcSfDiDPnv_M-wBLxZw8uqy8d6iZqB.rDCI1AAsvuMJ_LTS
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 03:35 Hey, folks.
**Steve Rao** 03:37 Hello.
**Matthew Hensley / Grafana Labs** 03:43 Hello.
**Trask Stalnaker** 03:48 I've given up kicking out Andrew's notetaker.
**Steve Rao** 03:53 Okay.
Yeah, yeah, because we don't have winter time, so I entered the meeting in advance.
Okay.
**Trask Stalnaker** 04:07 Alright, so that means it's… Later for you?
**Steve Rao** 04:12 Later. Well, yeah.
**Trask Stalnaker** 04:17 Yeah, maybe we… I mean, we could… Move this meeting… Ahead an hour.
**Steve Rao** 04:26 Yeah, it's good, yeah, if we can.
**Trask Stalnaker** 04:30 That would probably be… I mean, I imagine the U.S. folks wouldn't mind it being an hour earlier.
Cool. We'll… I will do that.
Okay…
**Liudmila Molkova** 04:47 Hello.
**Trask Stalnaker** 04:49 Hey, we should check with you. Are you good with moving this meeting an hour earlier during… Winter…
**Liudmila Molkova** 04:59 Yeah, yeah.
**Trask Stalnaker** 05:00 Standard time? Sure. Okay.
**Matthew Hensley / Grafana Labs** 05:03 I certainly wouldn't complain. I'm, This is just before my bedtime, so…
**Trask Stalnaker** 05:10 Oh, I just didn't miss that you're… East Coast.
**Matthew Hensley / Grafana Labs** 05:14 Yeah, yeah.
**Trask Stalnaker** 05:16 I'm so…
**Liudmila Molkova** 05:17 But we promise to be boring enough, so you'll follow us.
**Trask Stalnaker** 05:23 Help you!
Alright, we've got… Okay.
**Liudmila Molkova** 05:53 First, will you take care of the calendar, or I can do it right now while we are…
**Trask Stalnaker** 05:59 Sure, you can, I can do it later, or you can do it now.
**Liudmila Molkova** 06:03 All good. I'll just do it.
**Trask Stalnaker** 06:09 Which protocols, frameworks? Alright, so I think we… Finally made… Some good progress. Last.
Weak on this, and alvin and our… Haven't… I haven't read this… But… let's see… Double… Okay.
Did we write down, what we decided last week?
**Liudmila Molkova** 07:05 Oh, no, we, we didn't.
**Trask Stalnaker** 07:07 Okay.
**Liudmila Molkova** 07:08 Sorry.
**Trask Stalnaker** 07:09 No, I've decided… to model our PC as… logical… Operations… So… train, RPC… System… Name… And we would have gRPC… Double… Connect… our PC… And JSON RPC… And as far as which ones, do we want to target for stability, Feels like, I mean, JRPC and Dubbo, are the… to… That seemed most… Relevant for this group.
Do you think that's enough for initial stability, or do you think we should add one of these?
**Liudmila Molkova** 08:43 The connector PC is close enough to GRPC.
So it… does not… really matter.
does not give… A lot of input.
I've been thinking about JSON RPC, and it's actually more a convention than a… Framework.
Yeah, so let's… let's talk about connector PC first.
**Trask Stalnaker** 09:24 Do we have…
**Liudmila Molkova** 09:27 I don't think… yeah, you don't…
**Trask Stalnaker** 09:30 JSON RPC.
**Liudmila Molkova** 09:32 So the JSON RPC library, if anybody would consider using it, there are some.
But it's just a few models, plus, in case of Java Jackson plus JSON library.
So it just doesn't make sense for anybody to… have a library, or have a common library, and then instrumentation also doesn't make sense. So I'm thinking, like, we… I don't want to remove it or so, but I don't want to stabilize it, because we… What are we going to even stabilize?
**Trask Stalnaker** 10:12 Fair.
Okay.
**Liudmila Molkova** 10:17 This is about JSON RPC. ConnectRPC, I think it's just that it's… Super close to GRPC.
**Matthew Hensley / Grafana Labs** 10:28 My understanding of ConnectRPC is that it is gRPC, it's just, like, an opinionated setup to remove a lot of boilerplate. So it only uses gRPC under the hood, if I understand correctly.
**Liudmila Molkova** 10:45 You could talk… oh, go ahead, go ahead.
**Trask Stalnaker** 10:49 Do you think it would… Just use the gRPC semantic conventions, then?
Or is it opinionated enough, like, there's, like, a route concept or something that… They kind of layer on top of gRPC that's worth capturing separately.
**Matthew Hensley / Grafana Labs** 11:22 I'm looking through my notes here. I looked through this last week, and… Trying to find this one.
Okay, here is, I think, one of the differences is that, out of the box, I think, Yeah, gRPC is not something that browsers can speak, and ConnectRPC has… an extension that is… it's all using the same tooling and same protobuf specs, but there's extensions to allow direct communication from browsers.
So it… so as far as, like, whether or not it matters to name, it does because of the compatibility aspect. It's not just speaking gRPC, it has… it's like a superset of it at this point, because it supports these other, transport types.
**Liudmila Molkova** 12:17 Right, this is also my understanding that they support gRPC over HTTP. It's what also DABO supports.
And if we solve it for double, if there is any semantics, we could… apply the same to conductor PC.
**Trask Stalnaker** 12:38 Or Dubbo, would we target Dubbo… 2 and 3, or just double 3, or… Are they the same?
Do you think they're the same?
**Albumen  Kevin** 12:53 I think double is enough, because we can treat DABL as a framework, and it can be a protocol.
Still, we have several versions, but… For the RPC framework itself, we would… recommend you use the Tableau.
Yeah, and our brand is…
**Trask Stalnaker** 13:21 Okay.
**Albumen  Kevin** 13:23 Into the city.
**Trask Stalnaker** 13:24 And so the conventions would… Do you think the conventions are gonna be… The same, essentially, for… The two versions, or it doesn't really matter, and we just target.
**Albumen  Kevin** 13:36 It hasn't really.
**Trask Stalnaker** 13:37 Latest.
**Albumen  Kevin** 13:39 version I don't really match. Yeah, we just, to identify for which version supports triple protocol or not.
That's all fine, yeah, that one is… it's okay.
**Trask Stalnaker** 13:54 Alright.
We've decided.
Boom.
Boom.
Alright, review open PRs… Okay.
Per RPC status codes… Yes.
**Liudmila Molkova** 14:25 Okay, so the long story short, we had… Quite a few different… status codes for RPC calls.
Okay, and… they are… Sometimes generated on the client.
Sometimes are returned from the server.
So instead of having multiple different status codes, we have one, and it's just rpc.statuscode.
The SPR, updates, everything.
To use this one status code, and it also mentions Which of them are errors?
And also, James noticed that the generic error type description mentions gRPC status code, and we need to fix it.
So one thing we lose with that is this, enums.
Oh, Trask, you brought up a great concern about the error message.
So… What happens in practice that… You throw exception on the server.
And it potentially contains sensitive information.
then the server, the gRPC on the server, would put your exception message into the product call error message. It would also return it to the client.
And all of them would capture Error message that potentially contains sensitive information.
So, I… Remove this part for now.
I think I have an issue.
2… Come back to it later, but now… We… in this PR, we should not be talking about their message.
**Trask Stalnaker** 16:59 Okay.
Did we run in database, we didn't… Do we run into this at all, or do you think we missed it, that… some… Status codes may be generated client-side.
**Liudmila Molkova** 17:37 I think in case of databases, we didn't run into it.
We also define it as something that's returned from the server.
But they could be in theory.
**Trask Stalnaker** 18:02 Like, a timeout.
Status code or something.
**Liudmila Molkova** 18:09 Yeah, or I would imagine clients can… Fake something, or some special clients could have a status card instead of exception type.
Are you concerned about lack of response in it?
**Trask Stalnaker** 18:37 No, it's just confusing across the different, like, see that as a question that… People will naturally wonder, HTTP response status code, and RPC status code.
**Liudmila Molkova** 19:01 Yeah, I… I… Don't have a strong opinion in their way.
You can think about response as something that your API returns.
**Trask Stalnaker** 19:12 Yeah.
**Liudmila Molkova** 19:13 Or result status code.
**Trask Stalnaker** 19:16 Yeah, I mean, that's a… an odd point, worth considering, given that we're… Especially logical… at the logical layer.
for both database and RPC.
That response code.
Can mean the response at the logical layer.
**Liudmila Molkova** 19:50 Yeah, I think I like it. I'm also not excited about It being inconsistent with everything else.
**Trask Stalnaker** 20:00 And that, gives us, then, an out for the database response status code.
If we did miss… any there.
**Liudmila Molkova** 20:17 Cool, yeah, so let me leave a comment.
**Trask Stalnaker** 21:22 Alright, oh, was there anything else that we should talk about on… There's, I guess… No, it doesn'.
**Liudmila Molkova** 21:33 Thanks so much.
**Trask Stalnaker** 21:33 I mean, there's the losing the enum, but that's… Both good and bad.
**Liudmila Molkova** 21:48 We could add the enum in the note.
**Trask Stalnaker** 21:51 We could have a YAML.
**Liudmila Molkova** 21:53 Tooling, like, the schema could allow us to… support a limited set of failures. It's not the modeling problem, more like a tooling problem, right?
**Trask Stalnaker** 22:08 Yeah, and I like that it aligns with the database, and there's so many, and there could be more.
I like it.
**Liudmila Molkova** 22:22 Nice.
So the duration is way more interesting.
So, first, it… Applies to the logical layer.
It's aligned with what Java instrumentation does. It's not the, like, the API call.
It's the whole call duration, even in existing instrumentation.
So, even if you use streaming, And you give it this… They call it Stream Reader or something, essentially a callback thing.
mid… the Java instrumentation.
tracks, time from… the moment RPC was initiated till all the streams have ended.
And this also aligns with what gRPC native metrics do?
But they have two layers. They have the call layer, and they have a temp layer.
where I propose that we… Focus on the core layer.
**Trask Stalnaker** 23:47 What's the temp layer?
**Liudmila Molkova** 23:49 Attempt, sorry.
**Trask Stalnaker** 23:50 Oh, attempt.
Okay.
Yeah.
Attempt, is… Would it still, be from the attempt till the end of the streaming operation, or attempt meaning just the… The… the async one way…
**Liudmila Molkova** 24:21 Good question.
**Trask Stalnaker** 24:31 probably not relevant, because, I mean, our… for this, that would be a future metric that we could add.
Okay. I mean, Yeah, it seems like, based on prior art, That's the way to go.
**Liudmila Molkova** 25:00 Yeah, I'm trying to remember… If there is anything interesting to discuss there. Oh, one thing is naming. So, currently.
These metrics are called RPC Client Duration, RPC Server Duration.
And I'm adding a call there.
But the call is already part of our PC.
I'm adding a call precisely to leave a space for attempt.
And that's the only reason.
And we… we don't have to.
It's just more… Obvious there.
**Trask Stalnaker** 26:10 I want to look at what we do for HTTP.
Request and response.
I see, so this helped.
Because… to then include the streaming case.
**Liudmila Molkova** 26:36 This covers the streaming, right? It would help to include If we ever want to include attempts, we… Should be able to do it.
**Trask Stalnaker** 26:53 So, I mean, it… Just curious your thoughts on… The mixing the streaming and non-streaming together.
I mean, it seems like there's good prior art for mixing them together, But they do seem like they have very different… Characteristics…
**Liudmila Molkova** 27:22 That's right. So okay, there are four types of calls, right? There is, unary?
There is multiple inputs, one response.
There is single input, multiple responses, and then there are multiple to multiple, the full Duplex stream.
Let's try to play the scenario where we say, okay, the… Streaming.
Like, there is… there is a metric for Unary, right? For sure.
And there is a metric for any other Type any streaming.
**Trask Stalnaker** 28:09 Yeah, I called the other three streaming.
Right.
**Liudmila Molkova** 28:14 We… Consider them, they have different, like, you wouldn't put them on the same dashboard.
They might have different alerts.
They might have different semantics.
And then we would call one… our PC server… Request… ordinary… Just call duration, and the other one, streaming call duration.
**Trask Stalnaker** 28:57 Steve Alberman, what do… you all probably have some practical experience from monitoring double… How do… do you… think there's… A downside to mixing… the unary calls… Synchronous calls and the streaming… Calls.
In the same metric.
**Steve Rao** 29:39 Yeah, yeah, from my personal experience, if we mix the, If we mix them together, without, specific, information for users, maybe they will… They were confused why the call is so long.
Sometime.
This is a concert.
From my perspective.
**Trask Stalnaker** 30:14 Would we have a dimension?
on it… Or whether it was streaming or not.
Do we even know?
**Albumen  Kevin** 30:29 Yeah, we can know that based on this parameter, Both on Trappist and Adabo.
You can identify the request as a streaming request or not.
Basically… Although the… request can be a streaming request, like, a bi-directional stream, or another sign. Yeah, it should be… Bus stop by a runnery car.
From the client side, yeah, it should call first, and the servers will respond.
Maybe in a short time.
Then… mmm… I think there should be two… Types of, metrics on such invocation, which is for the first bus job, then… For the streaming request.
And based on our practice, the duration for the streaming Might be, useless. Yeah, we just need to… Records the… It's real time for each… I don't shock.
Yeah, I understand the question, I think, for the SAT protocol is for… The left socket, and Celestial event.
Yeah, that's… that's all… That was, drop it.
**Liudmila Molkova** 32:40 So… the…
**Trask Stalnaker** 32:49 Oh, this is what they're… doing.
**Liudmila Molkova** 32:53 Yeah.
**Steve Rao** 32:55 So, one thing I'm remembering…
**Liudmila Molkova** 32:58 In case of GRPC.
Duh.
streaming. You receive status code after your stream is complete.
So it's the last thing that happens.
So, so one thing, what, what Steve's been talking about made me think that maybe we should have time to first I don't know.
The response start, and it would be… The time of the unary call?
But it wouldn't work.
Well, because there is no response for the streaming.
**Trask Stalnaker** 33:57 Client protocol…
**Liudmila Molkova** 34:03 This is Dante, yeah.
**Trask Stalnaker** 34:17 Stream done.
**Liudmila Molkova** 34:22 And they… actually, I was surprised about it, and it actually works like this. This is until the stream actually completes.
But… There is a point in… Separating streaming and non-streaming.
Like, we would provide different histogram boundaries, maybe.
And the call, by call, you mean the unary call.
**Trask Stalnaker** 35:34 Yeah.
**Liudmila Molkova** 35:40 from our PC perspective, the call… the streaming call is also a call.
**Trask Stalnaker** 35:48 Yeah…
**Matthew Hensley / Grafana Labs** 36:12 Just a random thought, looking at some of the streaming stuff.
It reminds me of some of the metrics you might want around, The database query things, where you have a client making calls, but we also… have metrics for the connection pool. And so they're, like, the same thing, but… It's… the relationship between the RPC stuff, the UNR and streaming, and… Some of the database things start to… sound familiar. It's like, does it… does the total stream duration… Matter.
Or is it, like, how… or do we need to know more about how many streams are active?
At a given time, or something.
Because won't the stream duration just be as long as possible, typically? I mean, that's the point behind… The streaming connections often.
**Liudmila Molkova** 37:14 often.
But… I would, like, because there are this multiple inputs, one output, one response, and multiple… responses.
I… Maybe not because of it, but I would imagine there are cases… okay, let me give you an example. This MCP thing.
the client initiates a connection, it interacts with tools, it takes maybe, I don't know, a minute or five minutes, but then maybe it disconnects. It's not that you're talking for hours.
But still, it's not one simple call that you're making.
**Matthew Hensley / Grafana Labs** 37:54 That's a good point. I was thinking out loud since, this stuff seems… Vaguely similar, and what aspects of it do we actually… want to collect here. So, yeah, that definitely makes sense where it's… Not very long-lived.
**Liudmila Molkova** 38:13 Yeah, and I also totally agree with you that in some cases, it's probably intense for hours, or as long as possible.
**Matthew Hensley / Grafana Labs** 38:25 So in that case, the stream duration makes sense.
And within that, how do we want to model the ins and outs of the… Underlying messages or calls.
So you could find out, like, you have a lot… you have a stream that's 5 minutes long, and this many… Tool calls, on average, are happening in your streams or something.
**Liudmila Molkova** 38:46 Oh, I think we are trying to be lazy, and I think we're trying to say, let's instrument Unary, and let's push away streaming for as long as possible.
**Trask Stalnaker** 38:58 Ludmila, for the example of the MCP server, is it an actual… stream, like, would you actually implement that as an RPC stream?
Versus, like… just a bunch of HTTP request responses.
**Liudmila Molkova** 39:26 Normally it's a bunch of HTTP requests and responders, but they are… Hmm… they are grouped in session, and you would say, okay, I actually want to monitor a bunch of things that you have, and send me notifications if this file on the file system changes, and let me… do the thing, and then I'll disconnect.
from Europe, but there are… Scenarios where the client makes a request to the server, and server needs something from the client, and within the scope of this request, it makes a recursive call back to the client, and then it becomes…
**Trask Stalnaker** 40:13 I see.
**Liudmila Molkova** 40:14 Funny.
Bing.
**Matthew Hensley / Grafana Labs** 40:21 If I remember correctly, both supported protocols for MCP are always bidirectional, because it's standard I.O, or, was it streamable?
**Liudmila Molkova** 40:33 Yeah.
**Matthew Hensley / Grafana Labs** 40:34 Do you like SSC or something?
**Liudmila Molkova** 40:36 Yeah, yeah, either or… but I think MCP is not an RPC framework, it's something else. I'm just using it as an example to show that The streaming thing may last for minutes, or for hours, or for days.
So if we separate Unary from streaming, what do we do with spads?
It's the same… Semantics of the spend.
It's not important, probably.
**Trask Stalnaker** 41:31 I mean, I like the idea of a span covering the whole stream duration.
**Liudmila Molkova** 41:42 I don't even think we… we could instrument your PC in… Are there meaningful ways than that?
Practically.
**Trask Stalnaker** 42:06 Yeah, okay, and so if we map that to our idea of, It's like a span to metrics pipeline.
Is, I think, what you're… where you're going with that.
**Liudmila Molkova** 42:21 Yeah, and that we always define a metric to the course that we create.
**Trask Stalnaker** 42:27 Yeah.
That, that is… that is convincing to me.
**Liudmila Molkova** 42:34 And we still can have two different… metric.
names for this.
And the alternative, as Steve mentioned, we would have to have a dimension that tells what kind of Call is it?
**Trask Stalnaker** 42:51 Yeah, and so with the dimension, if we're going the dimension route.
We would need to define that dimension In the initial stability.
Due to our… stabilization rules.
**Liudmila Molkova** 43:09 Right.
The only worry I have with this is that Initially, we will provide Zero.
Conventions, but zero stable conventions for streaming.
Even if… It's a short stream.
We would say that it's experimental.
**Trask Stalnaker** 43:42 I mean, if we're going to just… I mean, if we could do the simple… I mean, it seems like what you're proposing of… you know, span… For the full stream.
And… That pipes into the metrics, and yes, we lose… we're not capturing any detail in between… in between there, initially.
And you said that's what we're doing capturing already in Java?
**Liudmila Molkova** 44:22 Yeah, well, we capture this pen event?
**Trask Stalnaker** 44:27 Right, but we capture a span for the full stream.
**Liudmila Molkova** 44:31 Yeah, yeah.
**Trask Stalnaker** 44:33 Steve, do you know what, we're doing in the Dubbo Java instrumentation?
**Steve Rao** 44:41 Around streaming.
Yeah, I'm not very clear about that point, but in double instrumentation, I guess we don't do anything specific for this.
I'm not very clear about that point, and maybe I can, bye.
Check out later.
**Trask Stalnaker** 45:13 Sure, sure.
**Steve Rao** 45:14 Yeah, but according to my… if I remember right, we don't do specific things for this point.
In Davos.
instrumentation.
Yeah, I have a small question. Do we come across a similar question in HTTP's semantic convention?
HTTP… HGTB choose?
**Liudmila Molkova** 45:56 So there, we're… Actually, in many cases, don't capture stream, because we capture, realistically, the time to response.
To response status code.
So if somebody would use HTTP2 with streaming, most instrumentations.
Probably all of them. We would not wait for the stream to end.
**Steve Rao** 46:26 Okay.
**Liudmila Molkova** 46:34 And it's actually good, because if our PC is based on HTTP, our HTTP instrumentations can capture the missing detail.
Some of them, of course.
**Steve Rao** 46:49 Yeah.
**Trask Stalnaker** 46:54 So we're getting to our time, I mean, this… is sounding… Pretty reasonable to me.
It aligns with… our current practice… Our, our… Prior art, I… Think that, spam the metrics, Kind of… Correlate, aligning span and metric.
durations… Is a good reason to go down to… Have the single… Metric for both.
Aligns with what GRPC is doing.
**Liudmila Molkova** 47:56 Cool, so Dan, I think I'll create an action, I'll create an issue to… define… Stream type, or call type.
Or I'll find an existing one, and I'm pretty sure we have an existing one.
**Trask Stalnaker** 48:17 Cool, and so you're… Okay, and so that's… what… so, yeah, I… I like that.
I also like that it's renaming at the same time we're changing the unit, because that's… Barney?
**Liudmila Molkova** 48:38 Yeah.
Go then, take a look, Next week, me and Trask are going to be out, so we probably won't be able to make it.
**Trask Stalnaker** 48:53 Yeah, I will go ahead and cancel.
Our first one at 4 o'clock.
Get this, Alright!
**Steve Rao** 49:11 Yeah, do you have time to attend a back meeting next week?
**Trask Stalnaker** 49:15 Oh, next week, no, I won't.
**Steve Rao** 49:18 Yeah, maybe you need to…
**Trask Stalnaker** 49:19 That also, yes, thank y'all.
**Liudmila Molkova** 49:30 Enjoy the quiet time.
**Steve Rao** 49:33 Yes.
Yeah, bye.
**Trask Stalnaker** 49:35 Fear.
**Liudmila Molkova** 49:37 Have a good day.
