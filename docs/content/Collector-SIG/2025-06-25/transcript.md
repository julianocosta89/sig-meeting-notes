SIG: Collector SIG
Date: 2025-06-25
Duration: 34 minutes
Zoom Recording URL: https://zoom.us/rec/share/mDlTXBr3IZUlcFB5OEYRMU1AeQRf7jktYEHNBE6QjPSoBf7PF3fOprgrLbxTq6Fd.K0qYqZ336jcJr_aC
============================================================

## Zoom Recording Transcript

**Andrew Wilkins @ Elastic Observability** 00:23 Hello! How you going?
Hey? Good afternoon.
**jmacdonald** 01:01 Hello!
I don't always come to this meeting, and I certainly have never run this meeting. I wonder who will.
**Paulo Janotti** 01:16 I will, I would say same for me, and I've been even less on the collector. So.
**jmacdonald** 01:25 well, I certainly could. I just have to find the documents if anyone wants that I'm certainly hoping to talk to Andrew today. So I did come for a reason.
But let's find the agenda there. It is.
**Andrew Wilkins @ Elastic Observability** 01:39 Just linked it in the chat.
There's nothing on the agenda at the moment, so fill it up.
**jmacdonald** 01:46 Well, okay, everyone put something on the agenda if you have it. And I'd be glad to share my screen in a sec.
Yeah.
Proper window.
Alright, everybody. A recording I'll share. Here it comes.
and I'll say Hello! Topic that I had to talk to. I think Andrew knows it's continuation. This is at least the 3rd or 4th time.
so I'll call it a conversation referring to, and I have. I'll I'll share the Pr. In a second.
Josh has recently opened Pr. Which I don't know the number of yet.
so that would be my my starting point. If anyone wants to hear and I'll give us a brief introduction. So Andrew has a a component called rate limiter processor, it's an elastic component in the elastic Components repository. And I've been working on limiter extension design work between, I'd say 3 or 4 or 5 interested parties within the Collector code base to formalize these extension interfaces. And we're really getting close. But the the details are, it's a big project. So this is my 7th draft of a set of changes that I've been working on, and I want to show it to you.
Andrew has been following along. So here we go, I'll just show you. I I opened one that's called Draft 7.
It's a minor change relative to Draft 6, but I just want to keep it clear when I start changing stuff relative to what was in a Pr so I I I wanted to open up the open questions where I couldn't really finish my work before the meeting here, but I was. I was really almost there. So I'm just going to find the read me and let's take a look at this together.
it didn't change this top matter. It's not very different from before, and it's not specific enough to help us discuss the questions at hand, and ignore this stuff till I get down to what I what I just wrote and I wanted to discuss. So this is sort of like a starting point for for where we could be, this is actually not where the code is, and I'm not sure it's where we want to be, but it's 1 option, and it's not exactly what you wrote in the comment last week.
Andrew. So just for everybody else's benefits. It's the idea that there are 4 extensions in this, and I would I would have configuration for each one.
In this design we have these, these weight keys. There are 4 of them. It's like request, count, request items, request bytes. And then we have one network bytes for compressed data. So the question. This question really is, where do we put the configuration of our weight? Keys are the is that configured in the in the limiters? Is it configured in the bindings somehow, maybe the middleware bindings. And is it configured also in the receiver?
In addition to other places where it might be used? And I've been looking at adding receiver support. And the reason why is that I know of cases from my work in Hotel Arrow, where the receiver has to do something a little different. The straightforward thing putting it in the consumer doesn't work the straightforward thing, putting it in the and the middleware doesn't work. So I want to do it myself. So I want to call. I wanna be able to disable the wait keys for certain like the Middleware, and only get the weight keys and do the do it myself. So I'm so that's what we're kind of discussing here. And in this version of the of the configuration discussion.
I have listed 2 limiters as the rate limiter as 1 1 rate limiter and one admission limiter those are my prototypes for the for the big rate limiter extension of Andrews, and the thing that I built for Hotel Arrow, which just counts like in use live quantities. So so the admission limiter is from Hotel Arrow. The rate limiter is from elastic and in this configuration you have 4 of them, and they're configured in 2 places. I wrote a few other alternatives down to get this discussion going, and I'm really not sure what I want, and I'm not sure anybody is so one that I wrote down here was to have like a multiplexer limiter. This could be like, I'm trying to move the complexity out of the core interface. And and you could have an extension that has configuration on per weight work per weight key. So this has got some sort of indirection that refers to other limiters with a specific binding that's got like a potential to have more configuration. So you can list one request, Count Limiter, one network bytes, 2 request bytes, and that allows you to combine both a rate limiter and an admission limiter. I have to work out the details right now. That wouldn't work in my my implementation.
I wrote down another option here. That I'd like to show you before we discuss.
and this is that Presently the middleware is configure configuration is has been committed. It's in there, but there's no existing middleware, so let's treat it as the most unstable it gets, and I found a bug right now we've all made this mistake. I say we, it's including you, Andrew, like in the Ca, in the the examples of the code I like, there's a currently there's an Id prefix. So a middleware configuration is a struct that has named Fields. But there was only one field named id. And so I kept forgetting to write that, you know, like this id prefix.
So it seemed natural to me to to remove that, and that means that the Middleware config is just a string. It's just the name of the component. That means that there's a very simple binding at the Middleware.
And that's the way I showed it here. Here, this is a list of limiter of Middlewares. Sorry. This is a list of Middlewares above.
and this is a list of limiters here. They're all just component references. There's no more information there, just components in this last option I've discussed. We go the other way instead of having an Id which doesn't make any sense to anybody we have like a subtype for middleware, and the ones we know about would be the limiters.
And so we would declare that a field named Network bytes means limiting by network bytes, we would declare a field like ref request bytes in the Middleware configuration object means a limiter for that.
and then you could have a decompression. Middleware, that would have a type that says it's decompression. This lets us check and like verify that the limiters are doing the right thing, especially for Htp, where we have to do rate limiting before the middleware. That does decompression.
If you want to limit network bytes. But there's currently no way to configure that. So the work I've been doing just recently on this Pr is to like well back to the 1st proposal is that we simplify the the receiver configuration. We simplify the Middleware configuration, and I'm assuming I push it into the limiter configuration.
And in my my current Pr, actually only have a single limiter in the receiver.
But I think that's not good enough, anyway. That's that's kind of where I am with the current thinking. And I'd like to hear what you think. Of course, Andrew and anybody else here who's listening.
**Andrew Wilkins @ Elastic Observability** 10:08 Yeah. So 1st of all, I'm I'm mentioning that chat was intentional on my part to drop the Id just because I thought it didn't really make sense. Anyway, it's just a minor detail. For the for what? Where we bind the white keys. I might need to think about this some more, but I think the last one made some sense for the Middleware.
I would probably have a limiters like a another level above the names of the Wait keys, but.
**jmacdonald** 10:39 In the in the middle of our config object.
**Andrew Wilkins @ Elastic Observability** 10:41 Yeah, minor detail. But yeah, I would probably have that. Just so it's clear that they're limiters rather than something else related to message bytes for the receiver specific ones, though I'm not sure about that slight.
**jmacdonald** 10:56 Okay.
**Andrew Wilkins @ Elastic Observability** 10:56 I think one of the examples I raised was bulk requests to elasticsearch. For example, sorry, sorry for the elastic specific example, but just something on my mind like we might want to rate limit something very specific to the back end.
In that case.
does it really make sense to put the weight key in the limiter itself, because the limiter extension doesn't need to know about the details of what the receiver is doing. It's just an arbitrary opaque identifier for a weight.
Does that make sense like what? I'm yeah.
**jmacdonald** 11:38 I? Yeah, I think the objective makes sense. The. I guess the reason that I've mentioned why I've I keep thinking about double counting is.
And and I liked going back like 2 weeks or so I liked when you made a proposal in one of my my prs. That. Essentially, said Josh. Stop thinking about double counting like, if the user configures it that way, let them do it. And that made sense to me as well, it's a nice simplification. I was. I was also thinking, though, that the there's a nice appeal in being able to sort of rigorously Co. Collate all those counts but the the 4 different weight keys that we know about, and to to both protect ourselves from double counting, but also, to be sure, at the end of the like sort of chain of middlewares and receiver Zoomer limiters, we'll call that that you have complete information. You could actually turn it into an observability signal self. Metric yourself with information about that stuff.
So that's why I put a little bit of investment into just thinking about it. The code's not ready even to look at. But I but what I was the concept was that I would have a context object that you initialize the 1st time you see the context, and the assumption is that you always return that so that you can add context values. The context value would have a place to do the like. Actually mutate as you count as you as you get the limit, request even before you request.
even before you know success or failure. There's some questions about like how we would encode the actual successes and failures which is open, but the idea would be that they would be tied together. So like after your middleware, after you receive after your receiver, there's some sort of cleanup operation that takes that stateful limiter thing and turns it into observability.
Actually wait. We can do this all the way back in the limit in the Middleware.
Like, there's an observability Middleware that can catch this, but I want it to be correct. That's why I was thinking about it. So I'm wondering if there's a way to have like there'd be standard limiter weights that are kind of automatic, and then additional potentially additional limiter calls that would not fall into the same key. I guess.
**Andrew Wilkins @ Elastic Observability** 14:09 But I might just need more examples of of what you're thinking about.
Yeah, I I didn't follow that I might need to. Do this like. Go back to this Async. Have a look at the latest draft, and then.
**jmacdonald** 14:24 That's fine!
**Andrew Wilkins @ Elastic Observability** 14:24 Leave some more comments.
yeah. So like I, I think my biggest sticking point would be where the white keys are defined. Still, so I need to think about that some more.
**jmacdonald** 14:38 Yeah, this is the part where? I almost.
Here's the thing I I came into this just wanting to get memory limit are working.
and my objective was to sort of like, I know how to count memory, and it's been very effective. It doesn't imply a rate limit at all. It's like, 1st come 1st serve or actually last. Come 1st serve is better. That's what it was doing, that's all I wanted here. So then we started talking about weights, and it makes sense.
I actually don't care at some level just that we find the best design. I have no strong feelings. And so I would definitely look to whatever you'd recommend. It's come. It's coming down to like Bogan, you know, is the main reviewer for this who I count on. But I'll tell you what he said in our our Monday meeting was, roughly speaking, look, users shouldn't have to like. Go read the Manual to figure out what this means. Here we're gonna look at those Yaml segments, and they're never going to read the documentation.
It better be clear what we're getting. And you know, thinking about that angle?
Maybe let that influence your thinking as well cause that's kind of the way he's gonna judge what I do.
is it clearer? I I like the reason why I'll go go back to why I started with this example is that this example is very clear. But it's just one you know, and I have, as I mentioned now, the context value can make sure that whether there's a rate like whatever limiters there are. I'm not gonna double count, and that means you can have except here's here's maybe what you you're thinking. And I really listen to your words again in my head, you know, like there's no such thing as double counting. They are separate limits. They're separate limiter bindings. You. You can't double count because they have separate. They have attributes to make them unique.
and you'll see 2 counts. But there'll be 2 limiters.
that's that's a compelling statement. I will say that so here, here's the re. So so in my 6th draft the prior pr, it was mixed. We could go back and look at that. The read me there. But but maybe I will.
The. In that case I had mixed the realities. There was a the Middleware was just a straight string.
I'll get there.
It won't take very long. Here we are, this one, this one.
and it's like at the bottom.
But there, there it was.
So I have this example, where middlewares are bare, bare identifiers because they're just ids.
Limiters have a name. And I. This was what I was having trouble justifying to Bogdan on the call on Monday like this looks complicated. Why are there limiters in one place that are like bare and other places have these qualifiers?
So that's what I was up against.
**Andrew Wilkins @ Elastic Observability** 18:00 Yeah. So this, I think, what what I was trying to say before is the middleware is for rate limiters or resource limiters that are cross cutting. So they're independent of the receiver. So this would be things like the at the Http level or the Grpc level. And it's gonna apply to anything that uses Http or Grpc, so it would be requests.
be network bytes. Whatever something like that. Where is the limiters at the protocol or the application protocol, level, Otlp, or.
**jmacdonald** 18:34 I've called it consumer, like the pipeline abstraction level.
**Andrew Wilkins @ Elastic Observability** 18:39 Yeah. Yeah. So that's that's some of them will be shared across different types of receivers. But they may have subtly different meanings.
I don't know how to qualify that more. But you know. For example, one protocol might support events, whereas another one only supports logs. And you might want to be able to write limit on one of those things, and it doesn't make sense for another protocol. So this is when it doesn't really make sense to have it at a at a common middleware level.
and that's why I would say it makes sense to to have a configuration in the receiver. Versus middleware.
**jmacdonald** 19:24 I mean, I was thinking that you would configure different limiters for those different protocols, but still use the Middleware configuration, not the receiver configuration.
and that you only need the limiter configuration when what? When? The it's the item, count, which is protocol specific?
But I and and I I know that context keys and metadata and client Meta Meta. Information like that gets added. So it's available in the receiver.
And if you look at the ingest path for both Grpc. And Http. It's pretty tricky to understand exactly when that gets introduced relative to the different Middlewares. But it it is introduced before the Middleware, so you could argue. Well, you've got your context keys.
At least, that's my understanding. The headers are parsed. Now you call the Middleware.
That, and that might change for the uncompressed bytes. I'm not sure anyway.
So so I'm I'm having trouble finding reasons why E, even in my current Pr, the the draft 7. It almost. It feels like Overkill, because I've put like these 2 checks for every for every request. First, st you're gonna go into the Middleware. And you're gonna like, do I have any limit or binding that I can find? And you're gonna try to apply it.
And let's say your Otlp receiver.
You're always going to have Middleware that works like, let's suppose, like, unless something's broken your Grpc. Middleware works, your Http Middleware works, you're definitely going to have limited the request bytes the the request, count, and the network bytes. By the time we get this working you only need a limiter on the receiver because of.
Well, the special cases that I know about in Hotel arrow, like I, the Middleware is not the right place to do it, and then there's the case, of items, which is protocol specific, and that has to happen. If it's going to be automatic at the at the P. Data level.
Alright. So I actually just all I'm saying is, I'm confused, and I don't know what's best. I I kind of just know the mechanics of limiting, and the configuration makes me feel like I just. I'm not doing in my job, or something like that. Help me! I'd like I think I can do it. But I I need. I need input from people.
**Andrew Wilkins @ Elastic Observability** 21:51 Yep, I have to go. I have to go back and look at the latest draft and see if I can provide some more concrete.
**jmacdonald** 22:01 Cool. Thank you. The the place it is right now is the the version. I am show not the version. I'm showing you right now, but it was that 1st one. Anyway, it's it's none of the above but the question stands and it is, I think, a fair fair game for you to review. So thank you.
**Andrew Wilkins @ Elastic Observability** 22:22 True.
I'll try and get to that as soon as I can.
**jmacdonald** 22:26 Well, I'll go back to the notes.
And thank you.
does anybody else have anything they'd like to discuss on the hotel collector.
I You know time is valuable. I do have your attention, though I will say that.
I from my, from my work. I've learned a lot about the style of collector Api design that I didn't understand before, and I figured I should try and document it. So the next person doesn't stumble over it the way I did. I opened this Pr from that work. It's unrelated to actual rate limiting, but it does use the rate limiting examples. So so you see this is how the collector is written. calling this pattern functional composition.
And you'll see, like you redefine an interface. It can have multiple methods. You define a function type for every single method.
Have that function type. Be a no OP have that function type called correct function as the interface value as the interface method.
and then you can compose them. You know this is how the collector looks inside. And finally, there's a document. So if anyone's interested in that.
I will put it in the notes, and that's all I have for today I'll put a link to the other pr, that we started with.
**Andrew Wilkins @ Elastic Observability** 24:12 I have an ad hoc topic. Just a kind of a question for this group. If if anyone has, so is anyone using open cemetery collector in a multi-tenant setup.
And do you need internal telemetry to include some kind of tenant identifier?
Does that mean anything to anyone?
Yes, Josh, you're trying to do the same thing.
**jmacdonald** 24:39 no, but I'd be glad to to speak about it. My experience with the last company where we did. If, Jeff, if you have something to say. It pleased to hear you.
**Jeff Alder** 24:48 My only experience with hotels using it in a in a single tenant type of way. Not you try to use it in a multi tenant. We haven't gone there, but I did see a proposal somewhere about routing pipelines based on attributes, and that's all I've ever looked at.
so that's it. No, not yet.
**Andrew Wilkins @ Elastic Observability** 25:10 Alright for some context we're using. So we're we're running a deployment of open cemetery collector in a kind of special way. But it's a multi tenant setup, and the the tenants are sort of dynamic in that. We don't know ahead of time what they're all gonna be we we could know. But it's more efficient that we don't rate reconfigure the collector every time a tenant comes and goes And we would like to know, you know how many logs have been processed for this tenant, for example. And ideally, we would use the internal telemetry of the collector and we would include a tenant Id in each of the metrics that the collector produces as a dimension.
There is an issue open in open summitry collector core about this.
It's kind of blocked because there's no way to do dynamic processing of metrics in the open telemetry sdks. Or there, there's a proposal. There's a spec proposal about it. And it seems to not be going anywhere fast. So I was wondering if this is a challenge for anyone, and got any suggestions on what to do.
**jmacdonald** 26:23 Yeah. Well, I definitely know that story. And I've seen the kind of stalled issues I might be, even on those threads with the stalled issues.
you know, I know what it takes to move open telemetry specs around, and it's just a tremendous amount of work to convince everybody else. I'm not sure that's good. It's the way it is.
I did this for the exactly the reasons that you said at my old company. And that's why I know about those proposals. I I was maybe even involved in them. I'm a believer in open telemetry, and I remember the early days when open census was the thing we were doing, and open census was one of its selling points. Exactly was this, that you have the ability to put metadata in context and then to do like dynamically turn on those things because it's expensive, but like sometimes essential. So wouldn't you like to be able to do that.
So extracting con metric attributes from context has always been part of the open telemetry story, and we're still not doing it. I don't know exactly why.
That's my position. while you're still watching my screen, let me show you something.
Oh, and of course, I'm just gonna trust Google can find this. But here, here it is.
The old company was lightstep. And we I I've worked in hotel metrics for a very long time. So so this was for me my proof of concept ground. This is where I prototyped stuff.
And then, as hotel go, established itself as a stable metrics. SDK, this was kind of irrelevant, except I still had done some stuff. So And it's looking like hope. It's still here. I don't work there anymore.
did we document it?
I'm looking like it's not documented. But this this code is an alternative. SDK, for go that we were using at the end there for myself, at the company within the Hotel Arrow exporter and the Hotel Arrow receiver. So on our Sas side, we were running that receiver and we needed exactly what you were saying to be able to monitor which customers were slamming our collector pool.
So that was the tenant information. And we had, you know, like a vendor specific header, that we were using for that in the Here it is.
**Andrew Wilkins @ Elastic Observability** 29:02 Measurement presses. It's exactly what we need.
**jmacdonald** 29:04 So I did prototype the measurement processor. If we need a prototype for the SDK, here's 1. But it's not really enough.
This is why we did it. This is exactly what we were doing was taking the so our envoys in the head at the at the ingress point would look up that metadata themselves in a fairly scalable cache server, or like rate limit server integrated at the envoy level, they would have pre computed the like group identifiers and all the like internal ids that they needed, that we were gonna use again to like, actually do some stuff downstream. So then you could just like go into the context, figure out which customer id you were. And then that was dynamic context available to the receiver for all those standard metrics.
So when we put in, injected our own SDK, we were able to configure it through the side to like extend those things, using this measurement processor, and it worked.
that's why I like that issue in the hotel spec. And if you thought that there was resources in elastic or anywhere here to to back that I would certainly sponsor in any any way I could, having been there at the time, and this having this prototype.
**Andrew Wilkins @ Elastic Observability** 30:26 Alright cool. Thanks. I'll I'll see who who we can rope into doing it on our side. And I'll let you know.
**jmacdonald** 30:32 Okay, let's here.
**Jeff Alder** 30:34 What else have you like considered and rejected like this is kind of a process injecting a processor that would do that work is was kind of my 1st thought. What else have you thought about.
**jmacdonald** 30:47 so the by the time the metric there's no such thing as a metric processor in hotel. There are sdks, there are logs, processors and trace processors which are but because those events are like one to one with an output. But metrics are aggregated through a through the SDK into a reader interface where? By which point you've lost that context.
So the measurement processor idea is one that says you're gonna intercept that context on the front, like front door on the way into the SDK, because that's the last point where you have it, where, prior to the increment OP operation, or whatever it is that like actually registers to change the metric, you need to pull out those context values and change the metric basically on the fly.
**Jeff Alder** 31:37 Okay, so, and that wasn't my questions more towards Andrew's side, right? Because Andrew is the one who was trying to figure out what this was so, my current. So my question was like, What was Andrew? What were you thinking? As far as like solutions for this kind of problem.
**Andrew Wilkins @ Elastic Observability** 31:53 Yeah, one option would be in the collector itself. We could configure a bunch of metadata keys, for example, that you can. The the collector would inject into all of the metric dimensions. It would just, it would be very collector specific there would be no need for extensions to the SDK but I feel like it's a bit limiting. Like it, would it? Would it would solve the problem for the collector, but no one else. So I think the measurement process is the ideal approach.
The other option we would have is more what you described before Jeff. Where we would have multiple pipelines using a pipeline processor, or whatever it's called that route. Sorry the routing process, so that would routing connector. Rather, that would look at a header, and then send it to a different pipeline, but that again, that that means that we would need to reconfigure the collector every time a tenant comes and goes which could be thousands of them. So it's not going to.
**jmacdonald** 32:53 Yeah, that's not good.
**Jeff Alder** 32:55 Yeah, it does not. It's not a it doesn't. The the approach I was looking at like the the request was more about like, I have a limited number of tenants that change infrequently, and it sounds like you have. You have more tenants that are going to change more frequently, and that doesn't seem like the right solution. In that case. Yeah.
**Andrew Wilkins @ Elastic Observability** 33:12 Exactly.
**jmacdonald** 33:17 It's it would be okay with me, and and I would approve the the work if the collector were to just go ahead and do this. I know that. The current work being done on the collector telemetry.
There's an Rfc. Done by jod.
they have made progress. And and it seems very doable to inject to to inject that data. But just above the hotel layer. And that's okay.
I think that's okay for for us, for now, cause you only have a few call sites.
**Andrew Wilkins @ Elastic Observability** 33:55 Alright. I think there is an issue about all. I might. Dig it up later, and then point you at it on.
**jmacdonald** 34:01 And then you could use that as a like prototype to push the hotel community forward. It just requires someone to say, Look, we've done this a bunch of times. It keeps working ideas sound. Let's make a spec.
**Andrew Wilkins @ Elastic Observability** 34:11 Yeah.
Sounds good.
Cool. Thank you.
**jmacdonald** 34:16 Well
**Andrew Wilkins @ Elastic Observability** 34:18 Thanks. Jeff.
**jmacdonald** 34:24 I will keep typing, but I think we've finished our agenda.
Well, I don't mind running this if I have to. I enjoy learning about the parts of the time zone slice that I don't always get to talk to. Thank you all.
See you in 3 weeks, I guess.
**Andrew Wilkins @ Elastic Observability** 34:44 Thanks. Catch you later.
**jmacdonald** 34:46 Right.
