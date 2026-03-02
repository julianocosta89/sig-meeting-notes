SIG: RPC Sem Conv Stability SIG
Date: 2025-12-18
Duration: 31 minutes
Zoom Recording URL: https://zoom.us/rec/share/7rwAGqxsZRTc_fQwaPDUk2G4932QWowGduXlglQ5eoYCoojmQ7MoP1jXmW4oGpym.VBPENmThqRVGxlxz
============================================================

## Zoom Recording Transcript

**Matthew Hensley / Grafana Labs** 00:29 Hello.
**Liudmila Molkova** 00:31 Hello, I met you.
I think Trusk should be around, let's pink him.
Bye, Steve!
**Steve Rao** 01:31 Hi, Lumina, Ludomiya.
**Liudmila Molkova** 02:17 Okay, well, we are waiting for trust quotes.
Take a look at the board!
We don't have anything new, we have a bunch of things in progress.
We should have them on the agenda?
Yeah.
And there are some to-do items that we will get to.
Yay.
Okay, Trask is online, so at some point, he probably will show up.
He created the migration guide. I thought it would be great to review. I think it just documents what we've done so far.
And it's something we will need for the stabilization for rotas.
So I think there is a…
Question here on whether we want pull requests.
I like pull requests here.
So it looks good from my perspective.
If you folks wanna take a look, please do.
Okay, so the other one I wanted to bring up,
Okay, maybe a new zero one to start with.
So… we… We'll have some fun with SPAN events.
So today, what we have, we are…
We don't have span events anymore. Well, we do have them, but they are, that the…
There is a deprecation plan on them.
But we have this nice little… Things and schema that… Say that this is a… span event.
I don't believe we want to stabilize, like, the messaging event.
Currently.
It's like a strategical, and… I… I don't know, it's not super useful. So I would rather not stabilize it.
And, following the other practices we have in semantic conventions, I would rather separate
Events into a different file.
And… Bose in Markdown, and in YAML.
This is what we do for…
metrics, and this is what we do in other conventions, right? So, like, we have doc for spans, doc for metrics, doc for events.
**Matthew Hensley / Grafana Labs** 05:49 Makes sense.
**Liudmila Molkova** 05:56 Cool, so then it's just a trivial cleanup, there is nothing substantial, I don't even have a changelog on this, nothing changes for existing instrumentations, if they emit span events, well, they probably can keep going.
Huh.
We probably should tell that the new instrumentation should not emit span events.
**Matthew Hensley / Grafana Labs** 06:22 Let's see, is that… That might not be covered in the…
**Liudmila Molkova** 06:32 It's not covered here, but there is a deprecation plan.
I think it would be, like, what we would do. The event would be… Experimental, still.
So, instrumentations that emit event would emit it
If they emit it, they would emit it under a flag, like, enable experimental stuff.
And then, they will be free to change it.
Two logs.
What is something else that might come up for the streaming?
So it shouldn't be breaking in the future.
**Matthew Hensley / Grafana Labs** 07:40 Bit of… yeah.
I don't see any issue.
**Liudmila Molkova** 08:02 Wonderful.
Okay, and the tricky part,
the emerging CarPC method and RPC service.
So, this part is not tricky. What's tricky is that the RPC method apparently has unbounded cardinality.
So you… It's hard, but you could probably send… Unbounded.
Call methods from the client.
Even with gRPC, definitely with JSON RPC.
You can definitely receive, on the server side, pretty much
Anything, because you don't control what's sent your way.
**Steve Rao** 08:52 the call.
**Liudmila Molkova** 08:53 The question is, how do we limit it?
So… in… I'm not really worried about the client side.
At least for gRPC. It's unconventional to not use… generated code, and I mean…
If you don't, then you can also disable instrumentation.
I am worried about service.
And what I'm suggesting is… Let's buy the necessary stuff.
So that, that new method name that we are introducing, so, in many cases, the GRPC double…
connector PC, there are… there is a product definition or something, and then your instrumentation kind of knows what's known, what's not known.
So you can… if you can res… if this method is resolved, you can kinda, say that
You can set it as a spend name, you can set it as metric attribute,
this is… this assumption is under validation. So what they figured out… That in case of gRPC,
We don't even… we're not even able to trace
The calls without was a known method.
GRPC interceptor does not even catch those.
So, Java instrumentation currently doesn't haract them.
At all?
And… I hope we can fix it. But anyway… So…
what I'm finding so far is that
On the server side, it's kind of possible to know.
Worst case, we can say, okay, if the method is not… if you see that the response code is method not found, then maybe you should not.
Add the attribute.
For JSON RPC, it's slightly different. JSON RPC, doesn't have any means to know
There is no code generation.
And for JSON RPC, I am making it… opt-in.
I don't believe there should be, ever.
plain JSON RPC instrumentation, because JSON RPC is more of a convention than a real, like, library that somebody would use.
So I'm… I'm not worried about that one, but I'm curious… If folks have any opinions.
Yeah, I mean, we can think about it,
If you wanna take a look, take a look.
**Matthew Hensley / Grafana Labs** 12:46 Yeah, I'm going to, want to look up a few things?
Around this… Because obviously it plays into, like.
JSON RPC handling does play into the LLM.
Stuff, of course.
Since that's what… Most of the tooling users, and…
**Liudmila Molkova** 13:07 Oh, the MCP is better, because it works on top of JSON RPC, and it does not usually use, like, the library for JSON RPC, and for MCP, you have a bonded set of methods that you can populate, you have a known set of things. It wouldn't be a problem there.
**Matthew Hensley / Grafana Labs** 13:27 Well, I just want to make sure that whatever we do here… This… Align with that one.
with kind of what they're expecting for the… on the MCP side, and…
Like, if you were looking at your…
Nested spans that it would make… Since…
**Liudmila Molkova** 13:47 I don't know if you've seen, we have MCP semantic conventions.
**Matthew Hensley / Grafana Labs** 13:53 PR.
**Liudmila Molkova** 13:56 And there, we don't even use,
Json RPC, let me find the latest version.
So there… We use MCP method.
And it has a list of, well-known belly-ish?
This one.
Mcp… none of the MCP
implementations I've seen rely on any of the JSON RPC implementations. They hand-rolled a few models that you would need to define for it.
It's like, you wouldn't even have MCP and JSON RPC spent.
you would have just MCP.
**Matthew Hensley / Grafana Labs** 15:12 Okay.
**Liudmila Molkova** 15:20 Yeah,
So yeah, then take a look to let me know what you think we will probably need to…
Think more about it.
The easy problem to solve, or maybe the hard one.
So we have RPC method name.
And what they've done with it is, like, if you know, then you said it. If you don't, if it's something unknown, you said it to other.
You can also… Kibda.
original value.
That's… that's self-unbound cardinality in the RPC method name original. This is a copy-paste from HTTP.
This is what we do with HTT Dispense.
And which makes me think, like, why do we call them differently?
We have HTTP request method. Should it be our PC request method?
Yeah, naming is hard.
But if you have, yeah.
**Matthew Hensley / Grafana Labs** 16:26 Yeah, that would be… One, definitely, to look at these.
Side by side and go down the list, since this isn't gonna change, I mean, these are all stable.
**Liudmila Molkova** 16:36 Yeah.
**Matthew Hensley / Grafana Labs** 16:37 unless there's a really good reason not to follow this convention? Like, it just doesn't make sense, or…
Not actually been working out, and no need to be revised.
for HTTP at some point, it's like, it'd be nice to align the naming as much as We can.
**Liudmila Molkova** 16:55 Yeah, the only reason I didn't, align is because at some point we've been talking RPC method type.
**Matthew Hensley / Grafana Labs** 17:03 Like, streaming, not streaming?
**Liudmila Molkova** 17:06 But I guess it could be RPC… Request.
Streaming something, or streaming type.
Like, it shouldn't be a big problem.
**Steve Rao** 17:28 Yes, I agree with you. Yeah, if we code its RPC method name, yeah, it's, easy to understand with ProWealth's RBC name or RPC servers. If we code its RPC request.
name, it's a bit confused for a user to compare with HTTP semantic convention, because HTTP semantic convention
a GDP method name is, describe the action.
like a GET post, something like that.
But, if, yeah, we, aligned with the naming of, HTTP-like RBC request name, it's, a bit confused for users.
Yeah, from my point of view.
**Liudmila Molkova** 18:26 No, so you're saying they are different, like, the HTTP or method is… Just a different concept.
**Steve Rao** 18:36 Nope.
**Liudmila Molkova** 18:36 our PCMed is more rich, and could have more properties than just the name.
**Matthew Hensley / Grafana Labs** 18:44 Yeah. Even though they are named similarly, semantically.
they are different. So, that's why I was saying we should probably look at them side by side and, like, intentionally decide not to use the names, or to use them, and make sure it makes sense.
Because in this case, I can see…
an argument over HTTP methods being very different than this.
I think that's,
But going through and double-checking the names isn't a big deal, it's just a matter of sitting down and looking at the two.
Try to do that tomorrow.
See if there's anything that… is obviously,
Should be named the same, or something.
**Liudmila Molkova** 19:35 Cool, yeah, and I think either way, it could make sense that there are pros and cons either way, so, like, I'm here to collect
any knee-jerk reactions or thoughts, if we… I'm up in either direction.
Cool, Dan, take a look, let me know what you think.
Hmm.
I don't have anything else.
**Matthew Hensley / Grafana Labs** 20:20 I'm not sure that I have anything.
**Steve Rao** 20:27 Yeah, me too.
**Matthew Hensley / Grafana Labs** 20:29 Oh, there… there was one that I saw. We've looked… I was looking at the gRPC, like, proposal repo, where we were looking at the metrics, I believe.
Yeah, there's metrics we'd been looking at,
That apparently have been, like, accepted and implemented for gRPC stuff.
There is a unimplemented, tracing proposal.
**Liudmila Molkova** 20:57 It is implemented, but it's… Not on by default.
**Matthew Hensley / Grafana Labs** 21:03 Okay. But it says… I was just going by the proposal being marked ready for implementation.
**Liudmila Molkova** 21:11 Yeah, so, like, if you… you can enable it, at least in Java.
There is some special environment variable.
You said… I don't know how I found it.
But if you set it, it will, emit stuff?
It's, let's see…
I'm playing with the… with what's available in Java, and…
this… these friends are actually coming from… sorry, have a lot of errors. They are intentional.
So… like… Here.
This is coming from GRPC Java.
They name stuff slightly differently, they call it send.
And… reset.
Save Dot, I think?
**Matthew Hensley / Grafana Labs** 22:13 Receive, yeah.
**Liudmila Molkova** 22:15 And… Yeah, this is also experimental, so what I hope we can do, we will
define a mapping for the metrics, right? The metrics are stable, they are emitted by default, we should figure out how to fix them, but we will…
Have a mapping.
We will show it to GRPC folks. Josh Torres, Promised us that he will…
Try to convince them to switch to a new stuff, maybe with a feature flag, or in some other way.
But there is… there… we hope to have at least one-to-one mapping.
For spans.
It seems we're in a better position, it would be easier for them to onboard, because it's essentially not documented on how to enable it, and it's experimental anyway.
**Matthew Hensley / Grafana Labs** 23:19 I… when I was looking through the tracing proposal, For gRPC, there's some…
Just some interesting background, where they were describing why they were using certain attributes, or how to do span events for retries to represent those.
It's, it's…
**Liudmila Molkova** 23:43 Oh, interesting.
**Matthew Hensley / Grafana Labs** 23:45 Yeah, it was,
Nothing too crazy, but at least, you know, someone else has already thought through these, and looking through what worked for
that proposal, and it's A72 versus the A66 for metrics, so…
**Liudmila Molkova** 24:07 A70…
**Matthew Hensley / Grafana Labs** 24:09 It's in the… yeah, it's a standalone file.
**Liudmila Molkova** 24:19 Oh, nice.
Oh, here we go, it's documented, okay.
**Matthew Hensley / Grafana Labs** 24:27 Looks like it is there.
But, you know, they explain how to set up the spans, including, like.
talking about the method naming, you can see the name resolution delay. I was wondering if that's something to do with gRPC. Is that DNS name resolution, or the gRPC server
Or client, you know, it's like… which… that isn't defined
There, but I thought that was interesting, that that could… be a problem?
**Liudmila Molkova** 25:04 Name resolution.
Oh… So maybe that's exactly…
Oh, it's probably the DNS name resolution, no?
**Matthew Hensley / Grafana Labs** 25:32 I… assumed so, but right before it, it has service name and method name, and it… it's just… it's ambiguous. I don't know if it's to…
Like, how could you name the span?
I guess you'd have to hold on and not omit the span until the name resolution process was complete. No surprise there, you have to attach an event. But, like, can you not name the span until that's done? And does that special event indicate that there was some delay?
But on the other hand, it could be DNS, because I know GCP has fun DNS resolution.
Where, like, your first request or two, just time out.
**Liudmila Molkova** 26:19 Interesting. So maybe… It's worth checking how they are doing the tracing, where they are doing it, because.
what I see today is, like, we in Java instrumentation, at least, we do it through Interceptor.
And interceptors don't work Was on the server, without… with… Unresolved methods.
And here, this is coming from the native gRPC stuff.
They tried… did they trace it?
And we don't. Like, this is ours.
We, we never, like, in open scholarship, we never trace the call. So they're doing it differently.
Maybe it's worth checking how they do it, so that
That this would start making sense.
And then maybe this is their way to deal with hypergenology, so that they start a SPAN, and once they know the method is known.
then they… Said the Sven name.
To avoid cardinology.
**Matthew Hensley / Grafana Labs** 27:29 That's what I'm wondering, trying to figure out, like… because there… like I said, there's some weird background, like how… the nuance of retries and such, and some interesting…
solutions.
But knowing that there's this job implementation, that, I mean, presumably a lot of this was implemented, In…
Java, so it… Might be obvious.
Prod… I have it up right now
Just gonna scroll through and see what I can find here.
But yeah, I just… we hadn't talked about this document, and…
That I can recall, and I came across it the other day.
**Liudmila Molkova** 28:11 No, that's great, yeah, thanks for bringing it up.
So I will, check, what they do for… Retracing.
And it's somewhere in the gRPC Java repo, if you want to take a look.
**Matthew Hensley / Grafana Labs** 28:31 I already found it. Okay. If you search for that environment variable, there's, five… instances on GitHub, and…
It's… the instrumentation.
**Liudmila Molkova** 28:50 Alright.
**Matthew Hensley / Grafana Labs** 28:51 Got the first one, got the proposal, and then forks of the proposal repo and the instrumentation repo, or the gRPC Java.
So…
**Liudmila Molkova** 29:02 Cool.
Oh, channel builder.
Nice.
Okay.
So, let's then study this. I'll apply to my APR, and hopefully it will help us move forward.
**Matthew Hensley / Grafana Labs** 29:30 Absolutely. All it means, if… as gRPC stuff, if we add attributes for it later on, apparently there's gonna be a bunch looking at that
proposal, because it… there's all kinds of nuances around retries and stuff that they want to capture, which totally makes sense.
That's one of the issues with the method name, like…
And the cardinality of it, because people can ask for whatever method they want, but also…
You would like to know if people are sending bad method names?
In case there's, like, a typo in, you know, your client or something, so it's one of those where it's…
Really useful information for debugging.
But, like, at production scale, it's just noise, it doesn't really help, it's…
One of those weird cases of…
Like, what really matters here? Obviously, we have to constrain cardinality, but it's…
**Liudmila Molkova** 30:27 Yeah, and I guess the method name is super useful, because
Unless you have one endpoint per your service, like, service.name.
So if you're creating a user, or creating a document, and reading the document.
You… you would want to know which one of those is called, you know, unproduction.
**Matthew Hensley / Grafana Labs** 30:53 Yes.
Alright, well, I don't have anything else besides, you know, homework, I guess.
**Liudmila Molkova** 31:04 No, thanks for bringing it up, it's super cool.
**Matthew Hensley / Grafana Labs** 31:07 Yeah, no problem.
**Liudmila Molkova** 31:10 Then?
Thanks for coming!
And this… this is the last call of the year. We're taking a break until… what is it, January 7th?
**Matthew Hensley / Grafana Labs** 31:23 Think so…
**Liudmila Molkova** 31:25 Yeah, the first… working day… oh, sorry, the first working Wednesday.
Of the next year.
**Steve Rao** 31:33 Okay.
**Matthew Hensley / Grafana Labs** 31:37 See you then.
**Liudmila Molkova** 31:38 Happy holidays if you celebrate!
In 2026.
**Matthew Hensley / Grafana Labs** 31:42 Singh.
**Liudmila Molkova** 31:43 Thanks. Goodbye.
**Steve Rao** 31:45 See you then. Bye.
