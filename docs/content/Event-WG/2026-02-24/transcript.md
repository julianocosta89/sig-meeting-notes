SIG: Event WG
Date: 2026-02-24
Duration: 51 minutes
============================================================

## Zoom Recording Transcript

**Pellared** 00:38 Overall.
How are you?
**Trask Stalnaker** 00:43 Doing good!
How you doing?
**Pellared** 00:46 Fine as well. Good to hear.
**Trask Stalnaker** 00:51 started joining the GenAI SIG, that's right before this,
So, I know that's where Lyudmila still is, because it was running late.
**Pellared** 01:03 Yeah, I… if I understood correctly, rest time is a little bit exhausting, right?
**Trask Stalnaker** 01:10 Oh, it's… there's a lot of people join… And there's, sometimes hard to get discussions.
**Pellared** 01:23 Yep.
**Trask Stalnaker** 01:24 So, I think today was… Today,
we had a couple of discussion… good discussions, I had worked with a couple of Microsoft folks on, kind of, improving the… refining their proposal, to be…
More, easier for people to engage with.
**Pellared** 01:50 Okay.
digestive.
**Trask Stalnaker** 01:52 Yeah, yeah.
**Pellared** 01:56 That's good.
**Trask Stalnaker** 01:59 Yeah…
**Pellared** 02:03 You're also going to Amsterdam, right, Trask? For KubeCon?
**Trask Stalnaker** 02:06 I'm not, no, no.
**Pellared** 02:09 Not this time.
**Trask Stalnaker** 02:11 Yeah… Traveling is… A lot of work.
**Pellared** 02:18 Yeah.
Especially when time zone difference is a very.
**Trask Stalnaker** 02:24 Right, right.
**Pellared** 02:25 I agree.
**Trask Stalnaker** 02:25 as much as…
**Pellared** 02:26 I guess with the H, it's a bit harder.
Yeah.
**Trask Stalnaker** 02:31 Yeah.
As much as I'd love to go to Amsterdam.
I'd really love, like, if I'm gonna go through that effort, I want to go there on vacation. Yeah.
**Pellared** 02:44 At least a few days longer.
I will say.
**Trask Stalnaker** 02:50 Yeah, Jason Plum always does well and manages to, like.
**Pellared** 02:58 Yeah, I noticed it. I do it one day or two days, and he's like… A week.
Yeah.
**Trask Stalnaker** 03:06 Hey, Lydmila, finally escaped the, GenAI meeting.
**Pellared** 03:12 Yeah. She's smiling.
**Liudmila Molkova** 03:15 I'm so excited that Trask is there, having more than a few people
Familiar with up in telemetry is helpful. Very helpful.
**Trask Stalnaker** 03:28 Yeah… Yeah, it's good, it's good. I'm starting to,
Understand some of what's going on.
**Liudmila Molkova** 03:41 Server side is fun.
**Trask Stalnaker** 03:49 Cool, I will share and drive.
This is the easy bus to drive.
**Liudmila Molkova** 04:01 Not easy, but I really appreciate you doing it.
**Trask Stalnaker** 04:05 Yes, we got a big agenda.
So, I did have something I wanted to chat with y'all about. So, I…
been… as you know, I've been, prototyping… exceptions as logs in Java.
And so… the… Severity question,
I am happy with the SEMCOM semantic conventions.
Severities that we've defined.
My, Remaining question I have… in Java is…
What to do for instrumentations that Don't follow semantic conventions.
So, there's… couple types, one is… Internal spans.
Like, model view controller, like, controller spans. I… Honestly, not sure that those…
Need to be emitting exceptions at all, or that it should always be debug?
Probably just always debug.
But there was… Another, what,
Oh, yeah, so what I was… what I wanted to do, actually, was I wanted to have, like, a default policy in Java.
Where if the semantic… if it's not semantic conventions, so semantic conventions would set their own exception…
Their own severity, exception name and severity.
But others… I was thinking of this local, local route.
Idea of, like, if you're a local route, it means it's bubbled up all the way, and so it's more important.
Whereas if your span is not a local route, it's down lower, it's probably gonna get caught and logged by your framework, or bubble all the way up.
So, those are not as important.
But what I realized when I was implementing this is that… At the…
Determining if a span is a local route.
I don't think you can do that via the API.
on the API side.
Yep. In Java… yeah, okay. We kind of can, in Java instrumentation, we stick all the local root
into this local root span, but this is not foolproof, if you're not using our instrumentation API thingy.
So, yeah, that had me rethinking, because I know I proposed that multiple times in the past, these sort of local route span…
based decisioning… In your… your OTAP, I think, Lydnila, about recording errors, exceptions… And elsewhere, so…
So we can do span kind… yeah, yeah. So anyway, looking for thoughts.
**Liudmila Molkova** 08:04 I think this is a better approach for the local root spend.
But…
Yeah.
**Trask Stalnaker** 08:18 I mean, we could probably pursue…
API spec thing at the API that lets you
Know if something's a local route.
If we wanted.
I mean…
I think we can, yes, because the span context has the parent in it, it's just that you can't…
get it out via the API. Am I getting that right?
**Liudmila Molkova** 09:03 There are two problems.
First one is that… Severity is contextual.
And… Local route is one of the possible strategies how you can… change it.
Could be others.
If we… can support more than one strategy. We can… Untie this to problems.
So, like, why wouldn't you be able to control severity based on some random context flag?
And we have this…
**Trask Stalnaker** 10:01 is…
**Liudmila Molkova** 10:04 Have the callback for stacked trace. Could it be callback for more than that?
**Trask Stalnaker** 10:24 I see, so you would pass in a D… you would still set a default, you would… the instrumentation would still have to set a severity.
But your callback or your hook could override that severity.
**Liudmila Molkova** 10:41 Right.
**Trask Stalnaker** 10:51 Yeah, I think that's what I was struck… that maybe wasn't thinking of, because I was…
trying to think how the SDK… Could do that.
And… But it felt like the instrumentation
like, the SDK can filter based on things,
And it could filter… like, the question, I guess, would we want to pass… would we want it to be a filtering decision?
And keeping the same severity as whatever the instrumentation stamped.
Or… More like a… Severity escalation, or severity bumping the severity itself.
I kind of like the bumping the severity, like, from a end user, like, you want… you kind of want to see it as…
a warning, not just like, oh, it's… why… what is my… this debug log doing in here? Oh, because it was a local root span.
**Liudmila Molkova** 12:05 -
Sorry, I need to get it out of my system. I was thinking, like, as if enabled returned a severity.
**Trask Stalnaker** 12:27 Yes, enabled. Oh, yes, yes.
**Liudmila Molkova** 12:47 Like, if we ask every instrumentation, To check whether
something as a lock over its span, it wouldn't fly. It's… it's a behavior in the SDK anyway. And if it's a behavior in the SDK, it's probably configurable. And if it's configurable, it's probably
Should support more than one case.
**Pellared** 13:34 What do you mean option C that returns? I think its language requires severity, or… I do not follow.
**Liudmila Molkova** 13:40 Oh, right.
**Trask Stalnaker** 13:42 It takes the default search, based on the context, gives you the user preference.
**Liudmila Molkova** 13:51 But yeah, I think it's…
It wouldn't fly, because you probably need more than just severity to make this decision.
**Trask Stalnaker** 14:05 But that's a good point.
But… If… so if instrumentation sets… Severity SDK… Bum.
Override severity based on… How does… But… Overlap with is enabled.
**Liudmila Molkova** 14:39 -
I mean, as enabled as an optimization.
**Pellared** 14:45 Yes, it's an optimization.
Yeah, so it can also override the same kind of severity when returning.
I think it would be very awkward if something… Basically, changes the severity, but…
It also has the context, if it's important. The span context, for instance, is still available… should be also available in the enabled.
**Liudmila Molkova** 15:12 It has to use the same strategy, because it has to happen before it's enabled, because otherwise log will not be overwritten.
The debug log, for example.
**Pellared** 15:27 Yes, it will have to be the same strategy, that's true.
**Liudmila Molkova** 15:30 Where we can see that it can only override higher.
Or… wait.
Lower.
Kinda difficult to explain, but easy to implement.
**Trask Stalnaker** 16:02 Yeah, but you lose the, sort of, like, say you emit everything as… Stay the… Span… emit everything as…
warning or error with the idea that you're gonna lessen it down to debug if it's not a local root span. Now you're losing all these optimization opportunities.
Of filtering it out earlier, not collecting stock traces.
**Liudmila Molkova** 16:31 Yeah.
What do we give to is enabled?
**Pellared** 16:54 We also.
**Trask Stalnaker** 16:54 Marity and context?
**Pellared** 16:56 We also added the event name.
So, in January, there could be using, you know, it can… Check the name…
it, it have… I don't remember the .exception suffix, or things like that.
I don't remember right now the proposal, but I think that was the proposal, right? In your Louis Domua, your proposal?
that the event name could have the .exception suffix?
Yeah, so this is the only way I think the optimization could still work with is enabled, if it just checks if the suffix has accept… is .exception.
**Liudmila Molkova** 17:50 All the… the… the… Extensibility point could look like… give me a…
severity, based on my event name, severity, and something else, and then use it as the event name.
**Pellared** 18:09 It should get a dog, or a cat.
**Trask Stalnaker** 18:17 Yeah, so… how bad… Okay, so… for semantic…
conventions, I… I think we're, like, we're kind of happy with this.
Client span warned, server span error.
Situation…
do we… is this a problem we… what can I say? Is this a problem we need to solve? Can… can we just…
So, for Java… for example, could…
How bad would it be if I just did debug?
For all of these.
for anything… That's not… Server span… client span…
I guess maybe just based on spankind? Why didn't… why did I not, like, Doing it based on spankind.
**Liudmila Molkova** 19:28 Because if there is no… Server instrumentation?
Damn… You wouldn't get any exceptions.
I think we also talked that if you don't have, like, server or consumer spend, or some other top-level thing, even if we call it internal.
Don.
You don't get a great experience, anyway.
**Trask Stalnaker** 20:15 The consumer one is a little tricky, right?
no, produce… Consumer, yeah, because…
Sometimes it represents processing, and sometimes it represents a receive.
**Liudmila Molkova** 20:34 I don't think it's the case anymore.
Let's see…
**Trask Stalnaker** 20:38 Really?
**Liudmila Molkova** 20:40 I think we spent… we bike-shed a lot of buses, that's all I remember.
Protest is always consumer.
The receive is always a client.
**Trask Stalnaker** 20:57 Oh… How did I get that?
In my mind.
There's a…
**Liudmila Molkova** 21:10 able about spankind.
Okay.
**Trask Stalnaker** 21:15 Consumer… Okay, producer… Send consumer…
Oh! I'm seeing consumer here probably mixing that with…
But Spankind is client. Okay. Okay. Oh, this is… This is good news.
Thank you for… Fixing me.
Consumer… okay, yes, and this is actually a consumer.
Okay.
I like that. That… that fits… yes, that fits a lot better than…
Source… Okay, let me go back to…
don't exactly… I know I had… I had actually started with something like this, and then ended up
Going away from it, and then…
So let me go back and see if, it fits better now.
that I've exhausted this other… these other options.
Client… Dude, sir.
Yeah, we really need to, decide… I need to decide the, the scheduled job question. I think it was… was it Martin who asked that?
In Java, we use internal .
**Liudmila Molkova** 23:10 If we keep doing the internal.
Even if we keep doing the internal.
This comes with should.
An internal is never a clear story, so we could have
Instrumentation submitting internal do something custom for their own needs.
**Trask Stalnaker** 23:31 Yeah, yeah.
**Pellared** 23:35 So maybe even by default, it should not be emitted to reduce
The emission of logs by default.
So that it should be only opt-in.
Or, I don't know, opt-in configuration for internal… So the…
**Trask Stalnaker** 23:50 If we're checking is enabled, right, won't we short-circuit?
**Pellared** 23:56 You're right.
Then just a little nitty question, should they maybe even be traced, even to lower it down more?
But, yeah, whatever.
**Trask Stalnaker** 24:19 I don't know the difference between debug and trace.
**Pellared** 24:27 To be honest, For me, personally, I was really using debug only for debugging purposes.
So if I had production code, I was always using, you know, the other levels, but I really wanted something for debugging, you know, just… Like one-time debugging. Yes, I really used just the debug level, so I was making sure that I do not get this trash that I had for the trace level.
Excellent.
**Liudmila Molkova** 24:51 So in my…
**Pellared** 24:54 Okay, gone.
**Liudmila Molkova** 24:55 Yeah, sorry, in my mind, trace level, you get the actual content of, like, TCP packets, or something, and debug as something reasonable. You can actually read it. Trace level, no, you cannot.
**Pellared** 25:10 Yeah This also works.
**Liudmila Molkova** 25:14 But yeah, I agree, it's… Not… not a useful distinction.
**Trask Stalnaker** 25:22 Alright, let's move on.
On a related note…
**Liudmila Molkova** 25:31 So, I think I addressed… we had a bunch of comments last time.
I think I addressed them. If you ask me what they were, I would probably need to dig into the history.
**Trask Stalnaker** 25:43 That's right.
Aha. Yes, very related. Indeed.
Okay, so we've got…
Event name…
**Liudmila Molkova** 26:56 Alright, so one of the changes from the last time, the lowest applicable severity number must be used.
Not feeling strong about must here, but it's… it's vague enough that… Yeah.
**Pellared** 27:24 I'm not sure here about this mask.
Because, for instance, I think there are cases when there's, you know, a client's panel can have an error.
Or no. Or maybe not?
**Trask Stalnaker** 27:39 I would just say should.
**Liudmila Molkova** 27:42 Yeah, hopefully.
**Pellared** 27:42 I also say should, because, you know, if you have, I don't.
**Trask Stalnaker** 27:45 It's all so vague.
**Pellared** 27:47 Yeah.
**Liudmila Molkova** 27:48 Yeah. If it's rag, it should be should anyway, yeah, okay.
**Trask Stalnaker** 28:32 So, do we want to… Talk about internal.
**Liudmila Molkova** 28:41 No way, yeah.
So let's take an example.
The GenAI convention has internal spans.
Or, let's say, invoking an adjunct. If an exception happens, There.
**Trask Stalnaker** 29:07 It's not really any different than, like, a client in that cave.
In that case…
**Liudmila Molkova** 29:12 Yeah. It's probably gonna get…
**Trask Stalnaker** 29:15 Handled, but it's still… Potentially useful.
**Liudmila Molkova** 29:22 Yeah.
in… there are different examples of Spring or controller Level exceptions where you'd rather Have them as debug.
Because they are noisy, and they will bubble up.
Likely to bubble up to the server.
level.
**Pellared** 29:56 social… Should we consider having a separate section for internal?
Spence?
**Liudmila Molkova** 30:07 In my mental model, internal spans are in the unknown area. It can be anything. Maybe we should drop them from this stock.
**Pellared** 30:17 From the systematic conventions, yeah.
At least now, and we can always revisit it later.
**Liudmila Molkova** 30:32 Like, we understand what producer, consumer, client, server do, what internal spans are, we just don't know.
**Trask Stalnaker** 30:49 Yeah, I like that. Because, I mean, if we define semantic conventions for controllers fans, maybe we would decide…
Internal should be debug.
Also not… I mean, I can see a… both ways. The Warren already… you're probably… like…
It's probably useful to suppress these at Warren level, it's probably gonna be…
Might be more noisy than you want.
Oh, the… Yeah, controller spans… okay, so controller spans may be…
you could, like, semantic conventions, I could see internal spans being worn, but, like, our widthspan annotation stuff, where people throw all over the place.
That should probably be debug.
**Liudmila Molkova** 31:57 Oh.
So, oh, I see.
**Trask Stalnaker** 32:04 I guess the distinction I'm making is at least semantic conventions are a more limited set, they're not, like.
I'm worried about duplication of, you know, capturing the exception all the way up the stack.
But with…
at least if it's sort of limited to semantic conventions versus in Java with these width spans, where people put them.
**Liudmila Molkova** 32:31 So we are kind of confident in this guidance, whatever it will happen to be, because we have events, redefined events.
None of them are internal.
So we have zero confidence in what we should put for internal.
So, maybe we can remove it, and…
Then it's a question to each semantic convention.
To define what they want, and maybe we will generalize it once we have… An example or two.
**Trask Stalnaker** 33:05 I like it.
**Liudmila Molkova** 33:07 Cool. I left a suggestion to remove the internal from this.
**Trask Stalnaker** 33:52 Info or debug?
Like, I tend to think of info as… As, like…
configuration… I don't know, like, info… information…
I tend to use it for…
configurations, but I know there's… some things have a config.
Separate config mapping.
**Liudmila Molkova** 34:40 I would… and we did in Azure SDK use info, let's say, in absence of tracing, we would record
logs about request. Okay, request ended.
It's verbose enough.
But it's still kind of useful information.
It's neutral.
And if you did something, and it failed, It's probably…
Not less important than you did something and it succeeded.
We, we know it's failing.
**Trask Stalnaker** 35:21 Oh, I see what you're saying.
**Liudmila Molkova** 35:27 Realistically, we wouldn't… Like, would we ever…
Produce an… well, we would produce an event that informs semantic conventions.
Would we ever… This is a guidance to semantic conventions, authors, and maybe application developers, if they care.
Would they ever want to use InfoSeverity?
I don't know, so that's why I was…
**Pellared** 36:12 I don't think so, to be honest.
**Trask Stalnaker** 36:21 What don't you think, Robert?
**Pellared** 36:22 I don't think… I don't think we need info from instrumentation libraries.
**Liudmila Molkova** 36:35 Well, there are some, they're not exceptions, though.
**Trask Stalnaker** 36:39 But then we're just, like, leaving, unused… Severity on the table that…
**Pellared** 36:47 For instrumentation libraries only.
Not for actual use.
I will say, yeah.
But at the same time, I remember about some use case, for some APIs, Which are more, like.
Kind of messaging?
like, a sink?
That it's hard to create a span?
Or just, you know, produce events.
But yeah, but these are not errors. These are just for errors, right?
Here.
**Liudmila Molkova** 37:28 Yeah.
So, I'm thinking… Span is… But let's say spend is written on Zlog.
In the instrumentation, this is info.
And the exception under is a detail about the separation, which is at info, so it has Lower severity.
**Trask Stalnaker** 37:55 I assume.
**Pellared** 37:55 For exceptions, yeah, for exceptions, yeah, I don't think, yeah.
I can see events which have info, but I don't think it should be, yeah, like, exception… exceptions.
**Liudmila Molkova** 38:07 So then maybe we'll do this. We say instead of info and bellow severity, we can say other exceptions, and say that other exceptions should be recorded with severity
Debug.
Period.
**Pellared** 38:25 or below.
**Liudmila Molkova** 38:28 Oh… If you're recording a trace from the instrumentation, you probably shouldn't.
Or, yeah, well, anyway.
**Trask Stalnaker** 38:39 I don't… that gets back to the… yeah, I… I kinda like…
There's something I kind of like about, for semantic conventions, simplifying the choice to…
Fatal Error, Warren, and Debug.
And skipping info and trace.
Because…
**Pellared** 39:02 Trudently, Hard to different…
**Trask Stalnaker** 39:04 shoot.
**Pellared** 39:05 Personally, I would use rather trace than debug, because of… but this is only because of my…
personal use cases, that I use Debug just for this ad hoc thing.
So that if I have something for debugging, I do not need to look as info level, if debug is, you know, just crazy overloaded with all errors and stuff like that.
**Liudmila Molkova** 39:31 I mean, it's not crazy overloaded.
It's just, okay, I tried something, it failed. The status is still.
**Trask Stalnaker** 39:39 lit…
**Liudmila Molkova** 39:39 Okay.
**Trask Stalnaker** 39:40 Yeah, it's… it's a legitimate… Well… Some of them… Where did I lose?
**Pellared** 39:54 I think there are a lot of systems that create a lot of errors, and you retry them, and you know. And if you just emit, you know, a lock for any error, and it doesn't mean that there's something wrong.
Because it can, you know, just recover.
And I'm just afraid, at scale, that it will be… Yep.
**Liudmila Molkova** 40:15 But they're debug. You don't enable debug logs at scale, are you crazy?
**Pellared** 40:21 Yep.
**Trask Stalnaker** 40:28 So this,
Oh, okay, we're already saying should not record these artificial exceptions. This is the one case where I would say, maybe trace.
Yep. Because it's…
**Liudmila Molkova** 40:42 Mmm!
**Pellared** 40:45 Exactly, that's my only suggestion.
**Trask Stalnaker** 40:48 If it's really not, except, like, if it's really not an exception.
If it's, like, a happy path.
**Pellared** 41:00 Yeah, because otherwise it will be probably worn, or something like that.
**Trask Stalnaker** 41:05 But, like, it canceled this one, I would, I mean, debug… Arrows turned when checking…
Yeah… I struggle with that a little bit, like, if it's…
If it's known to be a happy path, like.
**Liudmila Molkova** 41:33 Let's remove it, if you know it's a happy pass.
Let's remove it. Do you feel good with the first example?
**Trask Stalnaker** 41:44 Yeah.
**Pellared** 41:46 You think it's an info for us?
**Liudmila Molkova** 41:50 We should change it to debug, in general.
**Pellared** 41:52 Yeah, yes.
For the buck, I'm fine.
**Trask Stalnaker** 41:56 But this should be a… this should not be… I mean, this… this is a legit debug.
**Pellared** 42:12 This one's well.
**Trask Stalnaker** 42:26 Yeah, I mean, I think these are…
Good examples of things that we don't want to capture that is still good to have in the… in the spec as something that we don't want to capture.
**Liudmila Molkova** 42:43 Okay.
So, I've left a bunch of comments,
I'll spend 5 minutes after this call to apply them and clean things up, and it should be… Ready.
**Trask Stalnaker** 43:02 Awesome.
**Liudmila Molkova** 43:07 I like how we finally get together different signals.
**Trask Stalnaker** 43:18 Explain.
**Liudmila Molkova** 43:21 I mean, that…
it's a stupid question, which signal should you use, right? It's probably all of them in some variation, in some combination, and we finally have all the signals defined and semantic.
**Trask Stalnaker** 43:35 Oh, in September. Oh, yes.
Yes.
Oh, yes, yes, I see, yes, yes, yes, like…
Yes.
Yes, okay, let's assume that, and… But…
**Liudmila Molkova** 44:04 Cool, thanks.
**Trask Stalnaker** 44:12 Whoa… We're doing this…
**Liudmila Molkova** 44:17 Yeah, and I'm actually excited that we'll be bringing it up to the spec folks, because
We need to explain this.
**Trask Stalnaker** 44:28 Yeah. Yeah.
We need a broader… yes.
We're gonna have to… yeah, there's gonna be a lot of questions.
**Liudmila Molkova** 44:41 Yeah.
I have… I've added one more topic. I don't think we need to do anything… In this group.
But we've got the user… on Slack… Oh…
**Trask Stalnaker** 45:00 Oh, I saw that.
**Liudmila Molkova** 45:02 Yeah, there is a thread in semantic conventions, there is a thread in Weaver, there's more details.
But essentially, this user… Their company created their own semantic conventions.
And they have some use cases for body.
I… if I understand correctly, They're… they essentially have different…
Strictness for body fields and attributes.
They would spend more time validating attributes, and it's not a question of complex type, but more…
of, expectations.
They would like to keep using body.
It doesn't seem to be a concern for this group.
It's a concern for Weaver, because in the new syntax, we don't even have the ability to define body.
Type.
And it would probably be a…
Some, maybe, blocker to stabil… like, to moving over to… V2.
We will talk about it in the Weaver crew.
And I wanted to bring the tops…
**Trask Stalnaker** 46:29 Yeah, my question for the user would be,
Could they use the any type As the equivalent… Definition of a garbage bucket.
as body.
Like, that could be… I mean, that could be their differentiator.
**Liudmila Molkova** 46:55 Yeah, I think they… I've asked,
Yeah, I'll… I'll check.
more.
I don't… like, it's probably an option, but maybe… it's limited option.
The validation needs to happen, and it's…
the same story with complex attributes. It's very useful to describe their structure in a formal way and be able to validate if
Attribute value follows the structure.
So if we find solution, yeah.
**Trask Stalnaker** 48:00 What I meant for… for them, like, if they don't care about structure of complex attributes.
I assume that Weaver has a way of just saying any…
Any value with no specific structure?
**Liudmila Molkova** 48:20 Yeah. Yeah, it does.
**Trask Stalnaker** 48:22 And so they could, could they use that?
as their… Again, their garbage bucket.
Things that they don't really apply strict scrutiny for…
**Liudmila Molkova** 48:41 Yeah, and somehow I met…
**Trask Stalnaker** 48:42 Litmus… they have a litmus test.
Right? That they're saying, okay, We're… we're going to apply a…
More rigorous process to attributes than to body.
That's what I understand.
**Liudmila Molkova** 49:02 I imagine there is a spectrum between, okay, it can be absolutely anything, any garbage, and okay, if we apply, scrutiny over tiny details, there is a spectrum, but I don't know where they are, so maybe…
**Trask Stalnaker** 49:16 Okay.
**Liudmila Molkova** 49:17 Somewhere in the middle. But it's not essentially,
the concern here, but more like that people are using body for something.
**Trask Stalnaker** 49:34 Yeah, I just wonder if they would have used body… If we, like…
If we had had this guidance from the beginning, and we'd had tooling around complex attributes, and that sort of thing.
**Liudmila Molkova** 49:51 Yeah, that's a good point. And they, they could… Also… implement this.
In a way, saying, okay, I actually don't care about this attribute.
I only care about this set of attributes, and so on.
**Trask Stalnaker** 50:10 I just hate for the Weaver crew to have to do more Work.
Or to block B2 on something like that.
**Liudmila Molkova** 50:22 It's not a blocker for V2, it's a blocker to… throw away V1.
Right, and we can move on with V2 for semantic conventions, it's just more mental load to support it, and yeah.
Maybe this contributor… Would be interested in bringing it.
In a better shape.
**Trask Stalnaker** 50:51 I mean, isn't that what major versions are for, is breaking changes?
I'm not.
**Liudmila Molkova** 50:58 Correct.
**Trask Stalnaker** 50:59 I'm dropping V1… support, like… Do we need to maintain V1 support?
We would, I think we…
**Liudmila Molkova** 51:13 Not indefinitely, right, but at least for one year.
**Trask Stalnaker** 51:17 Yeah, yeah, that's fine.
**Liudmila Molkova** 51:19 Yeah.
Yeah, we can find ways out, and yeah, it's not a hard block or anything.
Cool, then that's all I had.
**Trask Stalnaker** 51:36 Yeah.
All right.
Good to see you both.
**Liudmila Molkova** 51:43 Good to see you!
**Pellared** 51:44 Good to see you. See you. Bye. All the best.
**Liudmila Molkova** 51:46 around, bye.
