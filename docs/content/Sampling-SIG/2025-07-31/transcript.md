SIG: Sampling SIG
Date: 2025-07-31
Duration: 32 minutes
Zoom Recording URL: https://zoom.us/rec/share/MNEQA9pYzl49W1hvTlEhY_VofCduX694UyEzQtBU2W_b1U1Lc2mzOOE5s8Yynp5P.On77PW919cK9Tz7O
============================================================

## Zoom Recording Transcript

**Kent Quirk (he/him)** 00:59 Good morning.
No audio yet, Josh.
Say, I don't hear it.
**jmacdonald** 01:19 Good, one device connected.
**Kent Quirk (he/him)** 01:21 There we go now I get it.
**jmacdonald** 01:24 Good morning. Here we are. I believe I've shared a screen. Is that right? Yes.
**Kent Quirk (he/him)** 01:31 Yes,
**jmacdonald** 01:32 And good morning. We have a few of our usual people here and it's pretty early in the meeting. I'd like to say hello to a new person who's joining us, named Patrick. It looks like.
**patrickpok** 01:46 Hello, Hello, yeah. I'm just like quite new to this. I just want to like listening for the for the 1st one.
**jmacdonald** 01:53 Feel free. This is a every other week meeting. It usually has a very small core of usual participants myself. Kent, Peter, there's a couple more that we might get today that we are regulars. Carlos has been joining us from the technical committee.
and I was just putting up some notes that I had for us to talk about today. Didn't quite finish. But One thing I thought I would do is follow up with last week last meeting because I missed it. It was my vacation week.
So I thought I'd start back at the beginning, unless unless someone objects. So welcome, Peter. I just opened this. Here we are.
And I was reading through it to make sure I could decipher it. I remember a month ago you explained what we what you were doing here.
**Peter Findeisen** 02:48 Yes.
**jmacdonald** 02:49 And it was a minor change about how you must not write threshold when you have an unreliable threshold.
I think, is what I remember high level.
**Peter Findeisen** 03:01 Right. And if you do this, you should not use the embedded randomness.
Because the yeah.
**jmacdonald** 03:11 Yes, that. Yeah. So if you don't use, if you have unreliable threshold, don't use the randomness either.
**Peter Findeisen** 03:17 Right, wrapped.
**jmacdonald** 03:19 Okay, I I agree with all that. It made sense a month ago. And now it makes sense again. What I'm gonna what I'm gonna try and do is not read it right in front of you here, but I want to read it one more time before I approve it. So I'll I'll I'll put some time after this meeting to do that 1st thing. And I appreciate this because it's like, you know, makes sense, and it's good to tighten up our specs.
There was a demonstration of the code. I will be glad to approve it. Oh, already got approved. Very good.
Okay, so we gotta get this. This merged I'll I'll just give it a little bit more credibility by reading it carefully before I do I think I said I would do that a year month ago. So that's not nice.
so this time it's a promise before 10 o'clock you'll have an approval on that.
So great! Thank you. I came with a couple of topics today. And I'll just start in. So at a specification meeting a couple of weeks ago.
the the people have started. The the SDK maintainers have begun to see the Otep specs that we wrote the the draft for SDK samplers, composable samplers and there was a fairly simple objection raised, and I agree with it. So I you know, sometimes you write these specs trying, choosing a course, and you don't really know but the idea of is that my my 1st approach was that trace id ratio based is got a big to do. It's never been specified. It's but been full of undefined behavior the whole time.
Therefore we could either fix it or replace it, and some when something's broken. I like to fix it rather than replace it. So that's the proposal we started with was to fix it.
The users who have it and the SDK maintainers are being cautious, and I think that's fine. To the idea that we might want to leave the existing behavior alone, or maybe an extended period like 6 months, or something like that.
so that users have a long, long horizon time to switch samplers if they are, in fact, using them. And of course, we we discussed how like the corner, it's like a very small corner case of user who could actually benefit from that timeline? Because, you know, we haven't even guaranteed that an individual tracer will be the same from one release to the next. So you have to have a system where every participant is using the same version of the same tracer in theory. But whatever so the idea is simply to get in there and change the name. In the meeting I propose something obvious, like probability sampler Carlos, is that the current state of that conversation.
**Carlos Alberto Cortez** 06:10 Yeah, that's correct. I think that's correct. Yes.
**jmacdonald** 06:13 Thank you.
Is I. I just remembered this from 2 weeks ago. I don't have the link in front of me. Is there a link that's been filed about that.
There we go. Thank you.
All right. Okay, so.
**Carlos Alberto Cortez** 06:28 Yeah, that's what you feel. By the way.
**jmacdonald** 06:31 That's which button.
**Carlos Alberto Cortez** 06:32 Digital, you open yourself. Is that what.
**jmacdonald** 06:35 My issue. It's been my own issue. Thank you. I had a vacation week in the middle there. Okay, cool. So then, this, this implies that we will do some very light editing of the SDK specification. Leave the trace id ratio and add a probability sampler.
that sounds pretty straightforward. I'm I'm sure I will eventually get to it if anyone else wants to. That's open task for and I think it's important, but probably not going to slow down people much other than like the the very pedantic ones. And that's okay.
Okay, so unless anyone objects, we can, we can move to my real topic that I wanted to bring to the group. And unfortunately, I didn't quite reach the end of my topic. I I thought maybe I'd have a bigger report ready for this but I I thought I'd mention it since we only meet every other week. And Peter, this this is gonna interest you, or at least I think I'm hoping to ask you a few questions right now.
Okay, so the backstory here and the report that I'm writing is actually not meant to address a sampling question. I'm working in the collector right now and picked up some some sort of like a wish list there. The collector has not formalized any sort of rate limiting interfaces. So these 2 topics are going to come together on the topic of rate limit configuration. That's where we're heading.
I say, rate limits. But I actually want to say general limits. We identified through sort of studying collector and and the ecosystem around it. There are really 2 kinds of limits, categories of limits maybe call them classes that we that we want to apply, and and the differences are one is rate limit. Those are based on a single count over time. And then there's what we call resource limit.
And that's like how much memory is actively in use, and they have different interfaces. So with a resource limiter, you have to increment and decrement for a rate limit, or you just increment and that distinction is nicely captured by our counter and up down counter models in the open telemetry metric space. So rate limiter means you're counting something and a resource limiter means you're up down counting something.
So the desire is clear and the the precedents are around us in other systems to sort of, say, well, there will be an extension interface for limiters, and you can go implement this extension interface for limiters, and you can go configure your pipeline. We'll call it for limiters. And you can have a rich set of like primitives for extracting fields and using those to be the key decision makers for your limit decisions. You can then have rule-based processing of requests as they pass through your pipeline.
All this.
is what's what we try to say. It's tricky. And this is a big space. So I've I've been doing some research. I looked at a number of different rate limiting architectures.
including envoy, which is probably the most substantial and interesting one for us. I looked at the tail sampling processor. I looked at Otep. 250 and I looked at Jaeger. Remote? So what's shot? What's interesting to me here is the existence of a configuration model, that is well, I'll say, quite complex and there are different models that we see. So the 2 architect types.
**Kent Quirk (he/him)** 10:20 Question on this. If I could.
**jmacdonald** 10:22 Yeah.
**Kent Quirk (he/him)** 10:23 Yeah.
**jmacdonald** 10:23 Yeah.
**Kent Quirk (he/him)** 10:24 This interface that you're talking about limiting?
Does it prescribe the mechanism of what happens when you decide to limit? Or is that up to the implementation of a limiter. In other words.
**jmacdonald** 10:41 Yeah.
**Kent Quirk (he/him)** 10:42 You know whether you're trying to drop things at the level of traces or at the level of spans, or at the you know per signal, or what sorts of what sorts of mechanisms are available for limiting. I guess.
**jmacdonald** 10:55 Good question. So this is really early in the design phase still, and I've recognized how complicated it is. I would ordinarily turn away from complicated things, but like the demand and the and the sort of clear expectation is there. So I will produce a report. I will come up back with more on this topic. But what but one of the things we see is that in the envoy model, which is my favorite so far, you have, several distinct concepts in place for your configuration. There's a descriptor for each limit, request and there are extractors on each route which extract keys and values from the requests to match the descriptors, and then in your actual filter configurations, you can then go execute rates.
So so it is an extension interface in the sense that there are well defined Apis, and you can come with your own implementation of a limiter in the envoy model. There's only rate limiters and the 2 different varieties that you have are local and global. So you define what your limit request will look like. You define how you'll get your keys and values out of the request, and then you do your limiting logic, which might be a local limit or a global limit.
the configuration model is fairly limited in this envoy example to token bucket limiters meaning you have a rate and a burst parameter. What I found in the resource limiting we had done in open telemetry. Arrow a couple of years ago. Is that a resource limiter also has a fairly similar model of 2 parameters? I want to say how much is in flight, and I want to say, how much will you block before failing fast? This is how much is allowed to wait parameter.
So sort of answering your question is that we found a you should have extensions that can be kind of like changed like you should be able to plug in one that does drop behavior, and you should be able to plug in one that does blocking behavior.
However, I also saw an explosion of complexity happening like, if you should, are we going to allow any kind of configuration for a rate limit? That's not something. Envoy allows every rate limiter is a token bucket at the local level and globally, you can do what you like, but but you're not configuring the global limiter. You're just pointing at it. So the configuration model is pretty strict on having token buckets baked in for my resource. Limiter, like the idea of limiting quantity of memory.
The same same story.
I want to be able to to block a limited amount, but not a lot like so a short burst should be able to to pause and continue, but a large burst will start failing.
so that but then and it's really quite varied. There's at least 2 more dimensions of of complexity in this space for the collector. You've got middleware doing processing, and you've got components like receivers doing processing. And those are different spaces for operations like you've got a parsed request in 1 point, and you've got some bytes in another point.
and there are different types of weight we want to limit. You can limit by compressed bytes. You can limit, by uncompressed bytes. You can limit by request, count, and also by item count. That's like everyone's asked for all these things, and you can look at existing. There's an elastic rate limiter for open telemetry that does much of this. So I'm trying to avoid too much complexity. I was originally thinking that there would be an extension interface that just let you be arbitrary like you can configure anything you want. You're an extension. But but the the number of degrees of freedom is too many.
and I'm starting to think that a simpler model, like just token buckets for limits and and weight, and and in flight counts for for resource limits as a good starting point. So this is a little off topic. I went way into the collector. And I know, Kent, that you have an interest in the collector as well.
So the interesting thing for this group is that 1st of all, the envoy model that I just described is radically different from the tail sampling model, although if you look closely, they seem to have basically the same functionality in the envoy model.
The way I describe it is that there are there's 2 sides. There's a request, configuration side, and there's a request evaluation side, and each side has a bunch of lists. So you have a bunch of lists of different requests, and you have a bunch of lists of different executors or or implementations, and you apply all the requests to all the implementations. And and there's a conditional and happening.
So either your your rule is bypassed because the condition doesn't match, or it's it's, you know, conjoined with all the other conditions. And so you have this like multidimensional list crossed with multi dimensional list where there are conditions that are that are dropping out. And then you're left with a bunch of conjunctions. Basically.
so the way I think of that is, there's there's a cross product happening of a bunch of rules with a bunch of requests and a bunch of conditions in the tail sampling model. We have much more like the Otep, 250 model, where it's a sequential rule, evaluation. And you can sort of like, choose a condition, choose a rule, choose a condition, choose a rule, choose a condition, choose a rule, and what I'm finding is that the tail sampling model is much more sophisticated. A configuration model is much more sophisticated in in several ways. And that's what I was typing up right before the meeting.
so so why? Why is this important? It's because I think open telemetry really needs a community owned tail sampling processor. That's like that's better like a little bit.
whatever that means it, it should be able to do Spani metrics, calculations, and all of our probability that we've been doing.
But it should also have a configuration model that people are happy with. If people are happy with with that model.
the the what I'm calling a tree-based model. Then we should keep it. I'm still on the fence about it. It's quite complicated.
and and I will come back with more more of a report on this topic. One of the things that envoy is capable of doing. That is also possible with tail sampling. But you end up with very different configurations, is to say something like, I have a tenant Id. I'm gonna have a high category of like important tenants with one rate limit, and I have a category of other users that are not important with a different rate limit, like having configurations of limits. Being detailed like that is something that is going to look different in a tail, a tree based configuration and a list cross product based configuration.
Nevertheless, it's something that people want.
Stepping back. There is a wish here that I'm kind of conveying to you that well, limiting configuration is super complicated. It's something that user operators are going to have to understand. And I think it would be nice if we could find a model that lets us apply rate limit configurations to trace sampling as well as to, you know, request limiting. It's sort of a it's sort of a crazy idea. Maybe I'm maybe I'm asking too much.
But that is the space we're in. I wrote down rule based with precedence. I could talk a little bit more about exactly what that means. And, Peter, I said I'd ask a question that that's where the question comes, I was going to type out the hypothesis. So this rule based thing.
Here's my my fundamental question. I'll try to ask it in Otep, 250. We say rule by rule, by rule, and it's the 1st come first.st Serve essentially. So if if this rule matches, I've got a probability sampler if this rule matches well, I should say composable sampler. If this rule matches, I've got a composable sampler in the tree-based model. What's actually happening is all the rules are being executed, and they have precedence relationships. There is a must not sample decision. And there's a must sample decision. And the if you have a a conjunction like an and and you say I'm I want to to do this. This anding of rules. If the drop rule matches. It will override a sample rule in the same clause in stanza. This is very complicated, but it exists so that you can have a mixture of statements, saying when to drop and when to sample, and the drop rules will override the sample rules.
And I was trying to figure out how to translate this back into an Otep 2, 50 model, where there's like one rule being considered out of time.
Because I believe there is a translation from this tree-based execution strategy to a rule sequential rule based strategy. But it might be a combinatorial explosion. When you do that.
I'm still on the fence about this design?
But I think that I think that there is a efficient non combinatorial explosion implementation of this tree-based algorithm. And it essentially says.
the precedence. Rules are outside of our probability scope. You'll you'll evaluate a bunch of decision making figure out which rule took precedence. That's your sampler. But I'm worried about the like conditional independence question. Like, if I'm making a decision in a must sample case and then a must not sample case comes along with a correlation with the randomness.
or these rules are correlated with each other. I'm just not quite sure that I can do this, and it left. It leaves me with a unhappy outcome. I don't know what to do with this complicated sampling logic, except to pursue it with these questions.
**Peter Findeisen** 21:06 Yeah. Well, so, the yeah, there, there is a number of issues here. Well, so fundamentally, what?
What bothers me a little bit is when you say, must sample and must not sample.
This is kind of hard to reconcile with our probabilistic approach.
Right? So her goal is to have the single value, the threshold value attached to each span throughout the life cycle of the span, no matter how many sampling steps it took to be faithfully used for metrics. Calculation I don't think this plays well with any must not sample decisions, because well, depending on your rules. Of course, if you apply this kind of decision, you will probably.
most likely, or even for sure.
destroy your capability to calculate metrics out of remaining spans.
**jmacdonald** 22:31 Yes, so let me see if we can fix it, though.
can we change a must not sample to the inverse of a sample with a different threshold?
**Peter Findeisen** 22:41 Right. So every I think the key is that every rule must tell us something about how to modify the threshold.
You can.
You're gonna suggest a new threshold value, which, of course, can be on the higher than the old one.
But
**jmacdonald** 23:14 It's so complicated that I can't quite figure it out myself, and part of camping.
**Peter Findeisen** 23:20 Yeah.
**jmacdonald** 23:21 There's another component.
**Peter Findeisen** 23:23 It's a different paradigm, right? We we are not have, must not and must sample. It's about all about threshold values.
You can have a number of rules. Of course you can have your predicates, and and so on. But eventually you manipulate the threshold, and that's it.
**jmacdonald** 23:50 This is my my combinatorial explosion algorithm effectively. It was to say that if if you if you take a a tree of logic and you find all the must not decisions, and and evaluate the the condition where it must not is true. Then then you go through again, and you evaluate all the conditions where I must not. Sample is false. And now you have 2 decision making predicates which can both be positive at that point. I think I don't like this.
**Peter Findeisen** 24:22 So.
**jmacdonald** 24:22 Well, okay. Please.
**Peter Findeisen** 24:24 Yeah, so must not should not be really used at all. You could. You could say, I want to have a very high threshold for a certain group of spans.
It it could be almost as must not sample right, but.
**jmacdonald** 24:44 Yeah, okay, so the I think, then, what you're saying is the same as saying that 0 probability is non probabilistic. You can't have 0 probability sampling, or else all bets are off right.
**Peter Findeisen** 24:54 Right? Because you get no data. Yeah.
**jmacdonald** 24:57 So then. And and I was actually fielding the user question in the slack in the last couple of weeks. That was not exactly what we're talking about. But it was a case of I want to keep 1% of my heavy, my my noisy span, and it was translated into a sample, a drop, 99%. So drop 99% is the same as keep 1%. Yeah. And then so okay.
there is still a question that's open to me about whether it's reasonable to or possible both of those to convert these, to do these tail sampling configurations with their complex, tree-based hierarchy and thresholds that's still open.
And I personally think it would be appealing to me to look instead at the even if you can convert by inverting thresholds and like playing out the combinatorial explosion. It's not clear that that's what users really want. And I think this envoy model that I've roughly described, and I'll come back with more again. It's mainly meant to do rate limiting and resource limiting, but but I think it's a fascinating observation to point out that the same limiting configuration that you've applied to your network bytes on the collector and to your request, count in. The collector also works for for tail sampling spans. Only the predicates are slightly different. So like you've got a predicate that says this span has 10. This trace has 10 spans, and that doesn't exist in the in the rate limiting of network bytes. So there's some. There's some similarities. And maybe if open telemetry gets its you know, get gets what it deserves. It will have a kind of standard configuration model that lets us put together predicates and rules, and then the collector can use it for rate limits, and the tail sampler can use it for for trace limits.
That was sort of a long and winding discussion. It can't back to your 1st point. It it getting into that rate limiting conversation. There's a lot of nuance there. And users. I'm the one who? Well, okay, I'm aware of users who are saying, like.
as I mentioned, there's complexity here. The the Middleware can do some stuff, but you don't have the full request. By the time you're in the Middleware, okay? So the the receiver can do some stuff and it has item counts. But the traditional factoring of open telemetry is to put your protocol into your receivers and your logic and your processors. So so now I've described how we can do course limits in their middleware. We can do. We can do limits based on data structure shape in the receivers. But now a user comes along and says, I don't know I've got this resource value, and I've got a tenant name or a service name in my resource value, and I want to restrict by service the rate of spans or by service, the rate of bytes. And that means I have to like, look at the data and actually do some logic. Now. So then the question might be, can I put my limiter into my processor? Well, why did we go moving it into the middleware or the receiver? Well, because we want to save memory. You can't. You can't limit in the middle of a pipeline effectively, without, without, you know, running on memory.
**Kent Quirk (he/him)** 28:12 You gotta have some place to put State Yup.
**jmacdonald** 28:15 Right? Right? So it's sort of the problem with limiting is that the answer is, Yes, all of it, please. We want to limit in the middleware. We want to limit in the receiver. We want to limit in the processor we want to limit, based on bytes. Before you know the parse we want to limit, based on the the length of the items in the data. And then we want to go and and buy particular keys in the data, extract further requests and do do more.
This is what envoy is good at is that, like the user community around envoy have done all of this, and you can do all this with the envoy model. And it's it's kind of proven.
I would like to see Kent a rate limiter type that's much more like a sampler in the sense that it will consult the rate limit, and it will drop the data that doesn't meet the the rate limit, because most users think of rate limit. They think of blocking the data on its way in. And I'm saying I got it's all one tenant here, but I've got a noisy service. I need to drop the noisy service, but the noisy service might be mixed together.
you know.
Maybe it's not a noisy service, but it's a noisy span operation I want to. I want to sample by span operation or something like that.
and I want to drop the spans that are too much and so then you're configuring. Instead of a blocking, oriented limiting equation, you're you're limited. You're you're configuring a filtering oriented limiter. Those should both.
**Kent Quirk (he/him)** 29:32 And you also have to sort of cope with the the bursting is problem, basically. What's your failure? Mode of your limiter?
Do you do you err on the side of too much or too little?
yeah. Sorry I on.
Yeah, I'm always, you know. Obviously the thing I work on refinery is is very, very stateful, and you know we we hang on to a lot of state. We do a lot of work to propagate state when we're starting to share load and that sort of stuff and trying to replicate this in collector without spreading it across. All of collector is the hard part.
**jmacdonald** 30:35 Yeah, yeah, we're yeah. We're we're not trying to tackle that harder problem. But but what I what I do know is that as my, my own user base, my own company demanding this something here is that we have a use for limiting by something in the data, so that, like, by the time you you don't, you want to get to a processor and say, Okay, there are 10 services here, and we need to make sure they're balanced. And so on. Which does mean extracting something from the resource, maybe and applying a limiter that's per per resource value, all of which is possible in that envoy model. You define a request. It extracts the thing from the resource.
Anyway, I think we've beaten this topic up. I appreciated the feedback. I got especially the like. Just the gut reaction Peter and Kent, from from both of you on on this tail sampler.
Even if it could be done. I think it would. You know very few people are willing to maintain this code already, and I don't want to maintain this. This model in addition to the envoy model that I'm already looking at. So so I appreciate your input.
**Kent Quirk (he/him)** 31:49 Cool.
**jmacdonald** 31:50 That was my.
**Kent Quirk (he/him)** 31:50 Sorry, but I have to drop, so I think this good timing.
**jmacdonald** 31:55 Okay. Well, thanks all. I think that we've have reached the end of a meeting. I I wanted to have a bigger report. I'm gonna make a report for the Collector group. I will share it with a sampling, because it's so much overlap and we'll go from there.
**Carlos Alberto Cortez** 32:07 By the way, there's a appear from from Peter, so probably we should check that out. You know.
**jmacdonald** 32:14 That's this one here. I said I would do this next. So what I'm gonna do is.
**Kent Quirk (he/him)** 32:18 Me too.
**jmacdonald** 32:18 Off the meeting and go do it right now. Thank you. All appreciate. You see you next time.
**Carlos Alberto Cortez** 32:24 Hello!
