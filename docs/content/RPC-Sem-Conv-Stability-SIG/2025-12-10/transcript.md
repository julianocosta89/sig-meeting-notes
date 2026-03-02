SIG: RPC Sem Conv Stability SIG
Date: 2025-12-10
Duration: 45 minutes
Zoom Recording URL: https://zoom.us/rec/share/QCr3qXdI9LI3dFt4lteZGOj7o-Ph9C4P6b-o4g57LiK16ztVLJ-Vr6PLpcF2FWwR.6_WNRNW1dQrQYvps
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 01:18 Hello, I met.
**Matthew Hensley** 01:21 Hello.
**Liudmila Molkova** 03:43 Hi, Steve.
**Steve Rao** 03:44 Bye.
**Trask Stalnaker** 04:01 Hey, Fox!
**Liudmila Molkova** 04:03 Ayy.
**Matthew Hensley** 04:07 Hello?
**Liudmila Molkova** 04:09 We don't have a bot today, which is surprising.
**Trask Stalnaker** 04:15 Interesting. Maybe Zoom finally listened to the… all the complaints.
**Liudmila Molkova** 04:24 Maybe.
Okay… So, let's get started!
I'm sharing, right?
**Trask Stalnaker** 04:38 Yeah.
**Liudmila Molkova** 04:39 Yeah.
Okay, we, I have a couple new issues, I created them.
So I think migration guide is non-controversial, we should edit.
I want to chat more about this one.
I added it to the agenda,
whether we need distinct RPC service and RPC methods.
Okay, so there's a trivial pull request to take a look about sampling attributes.
We didn't have any… any of the span attributes marked as sampling relevant.
On our PC, so, should be pretty straightforward for this one.
And…
**Trask Stalnaker** 05:35 The other one on… Which one did I review today?
Maybe you merged it already.
**Liudmila Molkova** 05:45 Yeah.
**Trask Stalnaker** 05:46 Made me, the whole inheritance thing is still so hard to review.
like, I had to go still with the reviewing the Markdown files.
is the only way I know how to… I can… Keep track of that.
Pipe.
**Liudmila Molkova** 06:09 Is that cheap?
**Trask Stalnaker** 06:10 gene in V2.
**Liudmila Molkova** 06:12 Yeah, it will be, like, as we will switch to V2, it will become…
more straightforward. Like, there will be no way to…
like, you can inherit from multiple groups, but they are… it cannot be… there couldn't be conflicts. So what, realistically, it would mean, that if we have multiple groups, we'll have several
groups dedicated to certain things. So, for example, network attributes and I don't know. Rpc…
Service attribute is separate.
And then you can mix and match the groups, but you cannot have intersection. So you inherit attribute only from one group, but not from multiple.
**Trask Stalnaker** 07:02 Okay, so in practice, we would end up having, sort of, smaller…
Attribute sets that then get pulled into places.
And it would only…
**Liudmila Molkova** 07:16 You can walk.
**Trask Stalnaker** 07:16 level. You wouldn't have to go to multiple inheritance levels.
**Liudmila Molkova** 07:22 Yeah, and I think as a part of this migration, we should also
I don't know, be more disciplined and avoid multiple inheritance, we could have written this easier, and if we didn't plan migration to V2, I would try to rewrite it to be
As orthogonal as possible.
**Trask Stalnaker** 07:47 Cool. Well, I look forward to… reviewing the V2, yeah.
**Matthew Hensley** 07:54 Sounds very, composition instead of inheritance.
That's been a process.
**Liudmila Molkova** 07:58 Yes.
**Trask Stalnaker** 08:03 Good, good.
Yeah.
**Liudmila Molkova** 08:06 So sh…
**Trask Stalnaker** 08:09 I don't generally have a problem thinking in inheritance, coming from, Java, it's so commonplace, but for some reason with these, it's just…
Really hard for me.
**Liudmila Molkova** 08:23 It is.
It's, yeah.
I think it's hard for everyone.
Okay.
So, moving… on…
to the discussion I wanted to have. By the way, if any of you have any topics, please feel free to add them to the agenda.
Okay, so I've been looking into something related, but not… not strictly like this, and I realized that we have
I don't understand what is the good reason to separate
Service name and method name into two different… attributes.
We merged them for the spending.
It's essentially the fully qualified… together, they're fully qualified.
Medit name?
gRPC uses it as a… single construct.
Double, though, has two different… Things.
Etrusk found a good reason.
That method, in theory, could be anything.
And there is a high cardinality, potentially high cardinality.
**Trask Stalnaker** 09:56 Yeah.
But that's… that's orthogonal to this question about whether they should be merged or not.
**Liudmila Molkova** 10:05 Well… Maybe. I don't know.
Not fartha will only be ATU.
Not fully orthogonal, but yeah.
I'm…
**Trask Stalnaker** 10:19 I'm missing… maybe I'm missing something, then, because either, like, it's…
**Liudmila Molkova** 10:31 So, if… it might be easier to explain that RPC method can be, what if we call it, other.
And the service name is Steel.
Relevant.
**Trask Stalnaker** 10:45 Oh, I see what you're saying.
Interesting. So, can service… I was assuming that service name could also be… High cardinality…
Depending on where you are capturing, like, if you're capturing it just… over the wire.
Before it's processed, before it's routed, I guess.
It would be high cardinality after it's routed
It would be low cardinality.
**Liudmila Molkova** 11:29 Oh, I see, yes. I, I, I just, I don't know how I read this text. I somehow assumed that only this portion is…
arbitrary.
Now, you're.
**Trask Stalnaker** 11:40 Okay.
**Liudmila Molkova** 11:41 Yeah.
Okay, yeah, then it's completely autonomal.
**Trask Stalnaker** 11:49 I fully support merging I think, given that
A, given that gRPC does it already.
Even though they have two different things, and that we did the same for… Function… name… Aligns well.
And… it just makes it a little bit…
Simpler than just you always have that, then in some cases you have it, in some cases you don't.
**Liudmila Molkova** 12:27 Right. It… it is then more consistent across different frameworks. Some of them, like JSON RPC, doesn't have a service. They just have a method.
I wanted to check with Steve, so when I look into the double.
I, I don't know, maybe it's just the implementation detail, but, it… the double invocation.
**Steve Rao** 12:59 Has method name, and the method name is just the method, it's not fully qualified.
**Liudmila Molkova** 13:06 Do you know if it's meaningful? Like, does it… does it matter?
**Steve Rao** 13:11 Yeah, yeah, just, just as you, said, yeah, the method name, just a method. It's not a qualified method. And the, service name is qualified, name, include the package name.
In Dabo.
It looks like a similar GRPC, just like you showed in the previous case.
Its structure is similar.
**Liudmila Molkova** 13:38 Yeah, like, would it be in artificial or incorrect in any way if we merged them into one thing and would have fully qualified method name on span and metric attributes?
**Steve Rao** 13:53 Yeah, if we,
merge them together, maybe it's, similar to the spend name, in double recently.
**Liudmila Molkova** 14:06 Yeah.
So it would, like, the method name would be the span name.
**Steve Rao** 14:15 Yeah, no. Currently, we use the service name, plus the master name to, construct the spend name in double.
**Trask Stalnaker** 14:29 What do you… what's the separator?
Between them? Is it just…
**Steve Rao** 14:32 I guess, yeah, it follows the, RBC semantic convention currently.
use the…
**Liudmila Molkova** 14:48 I don't see the spend name.
**Steve Rao** 14:51 Hmm…
**Liudmila Molkova** 14:52 But anyway…
**Steve Rao** 14:55 No, this is a test. Yeah, maybe you can, go to the OpenTelemetry client filter. Yeah, maybe we can check.
**Liudmila Molkova** 15:06 Oh, this one.
**Steve Rao** 15:08 No. Yeah, maybe, chasing filter, you can check.
Yep.
Or you can go to the double telemetry Builder.
**Trask Stalnaker** 15:37 Oh yeah, search for spam name here.
**Steve Rao** 15:40 Yeah.
**Liudmila Molkova** 15:44 Oh, because the span name extractor is generic.
It doesn't need to be…
**Trask Stalnaker** 15:50 RPC looks like it's def… what's the default? The…
**Liudmila Molkova** 15:57 Spending extractor…
**Trask Stalnaker** 16:04 Oh, look at that.
Yeah, that's… GRPC…
**Liudmila Molkova** 16:15 Yeah, and this is what is written in the convention. They, they want the slash.
**Steve Rao** 16:21 Yeah.
**Liudmila Molkova** 16:26 Chad, I don't hear any… Objection to… merging them.
**Matthew Hensley / Grafana Labs** 16:35 My only thought here is, I think JSON RPC and its old-school friend XMLRPC are the only ones without the notion of a service.
I think pretty much every other
Protocol or framework, whatever you want to label them, has that distinction.
So…
**Liudmila Molkova** 16:56 The distinction is there.
But, like, what I'm thinking, if you look into HTTP controller, you have a controller class.
And you have a method that handles an HTTP request.
We don't require this to think as two separate entities, right? It's… It doesn't… Matter.
That they're… That you can think about them as separate.
**Matthew Hensley / Grafana Labs** 17:29 Yeah, I don't disagree, I just wanted…
to just share that one, because I'm pretty sure JSON RPC is the odd one out here.
Compared to basically everything else.
So… Not sure the distinction matters, but I think it's worth just considering before it gets…
In case it's too simple, for whatever reason.
**Trask Stalnaker** 17:50 what does JSON RPC, does it have a survey? The service and… Not a method…
**Liudmila Molkova** 17:59 just a method.
**Matthew Hensley / Grafana Labs** 18:00 Hmm.
**Trask Stalnaker** 18:00 Just a method.
**Matthew Hensley / Grafana Labs** 18:03 Yeah, the… I think the closest you get to a service is, like, the URL endpoint that you're…
Or the equivalent, but it's, yeah, it's just service only. There's… or, sorry, only… only method, there's no service.
**Trask Stalnaker** 18:16 And what does method look like? Is it, like, Programming language method… Or if…
**Liudmila Molkova** 18:25 No, so, like, the example I know of is MCP, and method looks like… Let's see…
**Trask Stalnaker** 18:40 Oh, is it just, like, an arbitrary route?
**Liudmila Molkova** 18:43 It's an arbitrary route, but it's, fully qualified within the…
Service, in terms of service as an application.
So you cannot have two implementations of the same method on the same server.
**Trask Stalnaker** 19:03 Okay.
And conventionally, are they, do they look like this? Like… like URL paths?
**Liudmila Molkova** 19:16 No, they are, like, a static string, like this one, for example.
**Trask Stalnaker** 19:21 But, I mean, this one is… has, like, a… it's a forward slash separated.
**Liudmila Molkova** 19:27 Mmm.
I don't believe Jason RPC has any convention around this.
**Trask Stalnaker** 19:33 Okay.
**Liudmila Molkova** 19:34 It doesn't cure.
**Trask Stalnaker** 19:35 It's just arbitrary route.
**Matthew Hensley / Grafana Labs** 19:37 Yeah, it's all streamly typed.
Basically.
**Liudmila Molkova** 19:41 String with Hivetail.
**Trask Stalnaker** 19:48 begin with the word RPC.
Oh, are reserved, I see. Yeah, yeah, yeah, okay.
Okay, so it's just… arbitrary strings, so…
That would just be our arbitrary… Yeah.
So it's basically like HTTP route.
Is that fair?
**Liudmila Molkova** 20:19 I think so, but also, I think that in terms of gRPC, the distinction, we imagined it.
To Matt's point, there is no distinction on the gRPC itself. GRPC thinks about it as a fully qualified
Medic name.
And we broke it down into two independent things.
Right, so this is also, HTTP route.
**Trask Stalnaker** 20:55 I mean, they are kind of two different things in… gRPC…
**Liudmila Molkova** 21:03 the, the… Okay, can you help me understand? Where is it, where does it come from?
**Trask Stalnaker** 21:11 Yeah, I think it's in the proto file. Let's look at… let me pull up.
**Liudmila Molkova** 21:17 Right, right.
So… In terms of the protocol, yes, you define the… I don't know.
the… Service?
**Trask Stalnaker** 21:36 Let's see, do we…
**Liudmila Molkova** 21:40 Oh, we never defined a service in ours.
**Trask Stalnaker** 21:42 Yeah…
**Matthew Hensley / Grafana Labs** 21:44 I dropped a link in the Zoom chat to the… an example in the gRPC docs.
**Liudmila Molkova** 21:49 Oh, thank you.
**Trask Stalnaker** 21:51 Yeah, here's another link to ours.
If you wanted the trace service.
But yeah, so service… that's the service name is hello service, and the method name is, sayHello.
**Liudmila Molkova** 22:11 Yeah, the moment you deal with gRPC APIs, they no longer separate it.
the gRPC… like, Interceptor never thinks about them as distinct.
things. And this is… was my analogy with controller. You write the controller class, You… have multiple…
Methods within the same controller.
That can have different suffixes.
Anyway, I, I think I'm… yeah.
**Trask Stalnaker** 22:50 I mean, so I'm just arguing that they're… they are separate things. I mean, they… they have…
They do have individual meanings.
in the gRPC world, but I don't…
I think that means we have to model them as separate things.
Same as… Function, code function, name, I mean, certainly there…
In a lot of cases, there's class and function are separate things, but we merge them.
Because it… Made things more uniform across languages.
And so… That's enough of a… Reason for me to… Combine them here.
to give us… a consistent… consistency across RPC frameworks.
**Liudmila Molkova** 23:50 Right, and then the main point, is that you probably would never aggregate On service only?
Because aggregating across different methods.
In the same service doesn't make sense.
**Trask Stalnaker** 24:08 I don't know, I mean, I could make the same argument for aggregating across class name…
That I might care about, you know, one class, one service class.
It's owned by one team.
But I don't think it's… big problem?
I don't think it's the main use case.
**Liudmila Molkova** 24:40 Yeah.
Okay, so then I, I can make a change, we can, if, we can review it if,
There are any counter-arguments, we will, pull up.
I'm gonna do-do-doo… And, so… Let's take a look at…
The… another, discussion I wanted to have is around operation co… sorry, the method type.
So I think we should probably merge the two issues together. There is this one, And there is,
RPC… Transpert type.
Which I… I think is…
Boils down to recording, whether we're streaming or not, and maybe a type of the streaming.
**Trask Stalnaker** 26:05 Hmm.
**Liudmila Molkova** 26:08 We would add it to metrics, and you can break down metrics by just
Look just tunery, or just streaming?
Perpiscimi.
**Trask Stalnaker** 26:21 Method type is interesting.
Are… I mean, certainly in GRPC,
Method… each method you declare as… Unary, or streaming.
I would assume you would…
sort of have to do that for all. Like, you couldn't have one method that supported both, right?
Would that help?
That wouldn't really…
**Liudmila Molkova** 26:59 No, from the API perspective, you, you cannot, and it's true…
or gRPC for connector PC, I imagine it's also true for double.
You have unary and streaming calls. Is this right, Steve?
**Steve Rao** 27:17 Yeah, I, I guess, yeah, it's, similar to GLPC, yeah, in, in double.
**Trask Stalnaker** 27:27 JSON RPCs support streaming?
Okay.
The XML thing that you mentioned, Matt, earlier, I'm assuming that doesn't support streaming either.
**Matthew Hensley / Grafana Labs** 27:46 Oh, it's…
Probably exactly the same as JSON RPC. It's been a while since I looked at it, but I know it's…
Darling news. I'll double check.
**Liudmila Molkova** 28:02 So, I think that there are two somewhat, interesting questions. First.
What do we want to capture?
So one idea is that we capture meta type, and then it includes Unary, and maybe different types of streamings.
Practically, I… I really don't… Thing.
it matters. Like, if you're either streaming or not streaming.
**Trask Stalnaker** 28:37 Yeah. I mean, gRPC doesn't…
I don't think there's any dis…
distinction there. Like, that you can tell…
**Liudmila Molkova** 28:45 Nice.
**Trask Stalnaker** 28:46 Oh, there is?
**Liudmila Molkova** 28:48 Yeah, like, for example, there is this, method info in Go, I think there is a similar one in Java.
Where they have Boolean flag for client stream or server stream.
And from API perspective, you kind of can explore the type of your request and response, and how
Whether either of them is streaming.
**Trask Stalnaker** 29:13 So does that mean if it's server streaming, that means you can't…
You can… you can't continue sending client requests, client…
requests. You just… one client request, and then multiple server requests.
And then the server closes it.
**Liudmila Molkova** 29:32 Yes.
**Trask Stalnaker** 29:33 Okay.
**Liudmila Molkova** 29:37 From an observability perspective, I…
I don't know if it's an important distinction.
It makes things slightly complicated, right? If you want to break down The duration of your… just Unary calls.
You only care that it's sonary. Do you want to…
Compare duration of different streaming calls, probably not. You wouldn't even aggregate on this.
And it brings the question, do we even need the enum, where we can have a Boolean flag and then call it streaming type? And I think it's too narrow. It's like we are closing the door for an evolution.
So, I would…
**Trask Stalnaker** 30:39 do we think RPC is going to evolve?
**Liudmila Molkova** 30:46 Good question. It didn't, right?
**Trask Stalnaker** 30:51 Yeah… I mean, from… I mean, at least…
The choice of unary or streaming Cheers.
pretty…
that kind of covers… I mean, every… all the other stuff is, like…
done on top of streaming, like, the advancements or more stuff, but either you're… basically, either your HTTP
one unary, or your HTTP… to, streaming?
**Liudmila Molkova** 31:31 Yeah, and if we do this, we still don't close the door for evolution, this or the Boolean, because you can have an extra attribute that adds.
information. So then, maybe we should rather explore, the rpc.streaming That's something,
Because then we would only add this attribute when streaming is… happening.
And I guess it… I just feel wasteful to add Unary on, like, majority of calls.
**Matthew Hensley / Grafana Labs** 32:11 Definitely. I mean, obviously there's gonna be a lot of volume here, so I think trying to simplify the common case.
Would be great, and then for the few… I can't imagine…
off the top of my head why you'd care about which direction it was streaming, but someone clearly will, so leaving them that option, I think, makes sense, but for most cases, it's…
You only need to mark if it's streaming, I'd say.
**Trask Stalnaker** 32:43 From a wastefulness perspective, if we do a Boolean…
I forget why we came down on, like, if… on having a default value.
Like, if we say it's a… can we say it's a required field, and have a default to avoid…
The wastefulness.
**Liudmila Molkova** 33:10 Yeah, so there we…
We didn't want to have default fields where you cannot… where you need to distinguish the… the not known versus default.
I think this is always… known.
Yeah, you should always know it. We can have… This old value.
cannot have RPC streaming type.
bit something.
Okay.
And now let's go ahead with Boolean flag.
Or… this one.
**Trask Stalnaker** 35:33 if we do RPC stream type, so we would not, if it's not present, it would mean…
**Liudmila Molkova** 35:42 culinary.
**Trask Stalnaker** 35:42 lunari.
And do other, well, I guess others also have the… probably the client-server…
distinction, given that they're heavily influenced by GRPC, the other streaming One's ConnectRPC and Dubbo.
**Liudmila Molkova** 36:12 Yeah.
ConnectRPC also has this distinction.
And Dabo, I didn't find the API reference, but according to Steve, they also… .
**Trask Stalnaker** 36:29 I'm trying to think why we care about…
Whether it's client, or server, or… Bidirectional.
**Liudmila Molkova** 36:36 Just because they're… they're… this is the… kind of patterns.
And it's available.
**Trask Stalnaker** 36:46 Does, does gRPC Metrics… capture anything…
For whether it's streaming or not.
**Liudmila Molkova** 36:57 No.
**Trask Stalnaker** 37:15 Hmm, that's interesting. I guess… The idea there is… That you know… from the…
I mean, you probably aren't… I guess the idea is you aren't really aggregating over all of… what's the point of aggregating over all routes?
**Liudmila Molkova** 37:43 It brings an interesting point, that adding this attribute.
To that metric. It's not breaking, because it's a… it's… you are not splitting the time series.
**Trask Stalnaker** 37:57 You're right, yes.
**Liudmila Molkova** 38:00 But maybe we don't need to define it at all, unless we also want to define streaming case.
Yes, it won't be breaking.
**Trask Stalnaker** 38:08 Yeah…
I like this.
**Liudmila Molkova** 38:20 Okay.
So… I kind of feel bad about defining something in the streaming or stream namespace without clarifying.
Streaming cases, anyway.
So, let's…
Let me write it down on the issues and just move them to the post… to the stretch goal, to the streaming tab.
**Trask Stalnaker** 38:50 Yeah, and even in the… even in the stretch goal of defining streaming, I mean, like, we are defining
I feel like we could potentially define the span and the duration metric.
for streaming.
I felt like we had some…
Good consensus, sort of, following the…
gRPC model of what the duration means in the streaming case.
And… we wouldn't have to have… we wouldn't… I don't think we'd necessarily have to add a flag.
to split.
**Steve Rao** 39:33 B…
**Trask Stalnaker** 39:35 Streaming versus Unary.
And we could wait and see, you know, if… what kind of feedback we get from people, like, if they find that something important to be able to…
Split. I'm trying to think, what… what will users do with that flag?
**Liudmila Molkova** 39:58 So if we have a dashboard.
Right? The default dashboard. We would… not…
we could either split by method, right? And then, potentially, if you have tons of methods, the dashboard becomes unusable.
The stupid dashboard can split by… This by streaming type.
Whereby, is streaming is not streaming.
It's still not interesting to compare performance across different methods, right?
So… Yeah.
And, like, this metric being there for…
No, half a decade, and we didn't get this feedback yet.
It's hard to imagine we would get any new feedback.
**Trask Stalnaker** 40:54 And it's also… it's… I'm kind of taking a lot of influence from GRPC's metric.
The fact that they're not… They don't have a… split. They're, an attribute there to flag.
Unary versus streaming.
**Matthew Hensley / Grafana Labs** 41:31 Trying to think. So, in the case of gRPC, that's because streaming is kind of baked in from the start, and…
I think the intention, for the most part.
So I'm trying to think about the counter case of, does it matter for the other ones?
So, like, something like, WCF theoretically supports streaming, but no one really uses it.
And so it's just more about how
I guess the conventions that those communities tend to…
expect. So, I don't think it's a problem, just trying to…
Yeah, I think following the gRPC stuff probably makes sense in that case.
**Trask Stalnaker** 42:13 The question is more, what would… and what would users do with that flag?
And I think the argument
that what they would do, what they could do with it, that Ludmilla's making is, I mean, legitimate, like, that…
if you… kind of in the same idea that for your HTTP server.
Even though each of your routes, your login time is probably way different than your, you know.
Simple get.
request,
Timing, so merging them is kind of iffy anyway, but people still… it's very common to say, what's my average response time? What's my 95th, 99th percentile response time for my server?
And so, I think the argument for RPC is that if you wanted to do something like that, you would…
Probably want to…
**Matthew Hensley / Grafana Labs** 43:20 Ignore all the streaming.
**Trask Stalnaker** 43:23 calls… And say, what's my… 95th percentile for all RPC Calls.
**Matthew Hensley / Grafana Labs** 43:33 Yeah, that… that tracks.
**Trask Stalnaker** 43:40 And it seems like… it seems like a legitimate thing to track. I mean, at least at a surface, but I also know it's the same with the HTTP routing.
I wonder if… And given that we haven't had that If that has… Actually been something that people…
Want.
I don't know.
**Liudmila Molkova** 44:10 Given that we don't know.
And given that, it won't be breaking?
Luidan has to do this.
**Trask Stalnaker** 44:16 Yeah, I think that's the important part for us, is that we can add it non-breaking, because I think that's been why, like, in some other cases with metrics.
We've maybe been a little bit more aggressive, even though, like, and been like, okay, we need to add this, even though we're not, like…
100% sure it's… that we wouldn't be able to add it later.
**Liudmila Molkova** 44:43 Okay, this is wonderful, so let's not do this. I'll update the issues, and yeah.
Cool!
Dan, thank you all. We are…
**Trask Stalnaker** 44:56 Progress. Yeah, thank you for driving us forwards.
**Liudmila Molkova** 45:00 Yeah, thank you.
Okay, we still have one more meeting this year.
**Trask Stalnaker** 45:06 Yes.
**Matthew Hensley / Grafana Labs** 45:08 I was about to ask if, everyone… enough people are gonna be available next week.
I know a lot of the other, It's kind of 50-50.
And some of the other groups.
**Liudmila Molkova** 45:20 I'll be here.
**Trask Stalnaker** 45:22 We'll try.
**Steve Rao** 45:23 Yeah, I will be.
**Liudmila Molkova** 45:26 Awesome.
**Trask Stalnaker** 45:27 Cool.
Yeah.
**Liudmila Molkova** 45:30 Y'all.
**Matthew Hensley / Grafana Labs** 45:30 Catch you next week?
**Steve Rao** 45:32 Thank you.
