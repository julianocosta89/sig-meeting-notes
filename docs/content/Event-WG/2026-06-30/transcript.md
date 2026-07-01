SIG: Event WG
Date: 2026-06-30
Duration: 46 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 03:04 Hello, hi, Robert. How are you?
**Pellared** 03:11 Hello, hello.
we have… Extreme… we have extreme heat here.
**Liudmila Molkova** 03:18 Mmm.
**Pellared** 03:20 It's a few days, but it's stopping tomorrow, so it's hard for me to concentrate. Like, we have, you know Celsius, right? So we've had even 40 degrees.
**Liudmila Molkova** 03:30 Oh, wow. Yeah. Do you have an AC in your home?
**Pellared** 03:34 Nope.
**Liudmila Molkova** 03:35 Oh.
**Pellared** 03:36 Sorry. But at least my apartment is, does not have any site on the south, so for me, it's, you know.
I can withstand.
How about you?
How are you?
**Liudmila Molkova** 03:53 We don't… we don't have… yeah, I'm fine. We don't have any extreme temperatures here. Usually, it's pretty mild.
Because of the ocean and the cold stream there.
It's… even if the sun is very hot, the air is usually cool, and it's never hot in the night, so we are very lucky here, at least in the summertime.
**Pellared** 04:14 CFO, or am I wrong?
**Liudmila Molkova** 04:16 Seattle, yeah.
**Pellared** 04:17 Yeah.
**Liudmila Molkova** 04:21 Do you have any login topics? I heard something, I…
**Pellared** 04:27 only one.
which CGO asked us to discuss.
But I also not sure if Trask is here, because I think Trust was the one…
**Liudmila Molkova** 04:38 goes out.
**Pellared** 04:39 Yeah, who had the… who was pushing back on my NCGO proposal about the attributes naming for the log bridge, etc. He wanted to use the instrumentation name instead of the log bridge name, but I said.
**Liudmila Molkova** 04:53 I also want to use instrumentation name.
**Pellared** 04:55 Yeah, so CJ also gave examples, and I was also discussing with him that he thinks that it might be problematic, and it's safer to use log… log… log bridge name and log version, and he says that even for Rust, you know, you have this, we have this .NET, which may have different versions of iLogger. He said the similar can be… similar stuff can be for us, that people may want to… May use, you know, Even instrumentatory libraries.
some… more native.
**Liudmila Molkova** 05:55 Okay, this is clear.
**Pellared** 05:57 Yeah, this is clear, but we are concerned about Phase 2.
And still, we feel that this is… the safest way how to use it, because I remember what we were discussing during the Sikh meeting, that probably the logger name We'll include the name of the… Library.
instrument…
**Liudmila Molkova** 06:22 Wait, so, like, this is the… The logo name.
This is logger name, it can be full bar. We don't care at all what it is.
And through meditation's hope.
Name.
Then, then it will be full bar.
And then there is… The… the two things that are proposed in this issue, one is instrumentee, instrument… Hey.
**Pellared** 07:02 Lives.
**Liudmila Molkova** 07:02 name. It will be, let's say, Mongol.
**Pellared** 07:07 Yep.
without IOT telemetry, because this is instrumented. So, MongoDB.
Just…
**Liudmila Molkova** 07:18 Okay, whatever.
**Pellared** 07:21 And the one which you copied will be instrumentation.
Library name.
And this will be for case 2.
prop- our proposal.
**Liudmila Molkova** 07:33 What would it be?
**Pellared** 07:35 Are your OpenTelemetry constitu? No, no, no, no, no, no, no, so this is… So we prefer to have another, which is… Io open as you can't click, that's on GoDB. You can copy some.
Okay, don't true.
Et sont place.
Probably you can understand.
**Liudmila Molkova** 08:01 I understood Misha, but is it a name?
**Pellared** 08:04 Amisha, yeah, Emily Lee. Amelia.
**Liudmila Molkova** 08:07 Oh, hi!
**Pellared** 08:08 So, you know, you also, I think, in Russian, have, you know, this, this kind of, you know, short elements, etc.
**Liudmila Molkova** 08:15 Yeah.
**Pellared** 08:16 It's tough.
**Liudmila Molkova** 08:17 What is your short name?
**Pellared** 08:19 My…
**Liudmila Molkova** 08:20 So…
**Pellared** 08:21 Usually, nobody speaks my short name, but the… for Robert, it's not popular, but the two I know, like, Robert can be Robert Chic, Rob Cho, Robush. These are the I'll let you know.
**Liudmila Molkova** 08:36 That's cute.
Yeah.
Oh, yeah.
I don't even know how we would shorten the name Robert in Russian, like… Robczyk is, yeah, probably the one.
**Pellared** 08:54 Yeah?
**Liudmila Molkova** 08:54 It's no fault.
**Pellared** 08:56 Blair.
Even Poland as well.
To shorten Roberts.
**Liudmila Molkova** 09:01 Yeah.
Okay, so instrument… so, okay, so what you're saying, that… Long coverage.
**Pellared** 09:10 You have below.
So this is our proposal in… exactly.
**Liudmila Molkova** 09:21 So, okay, there is the instrumentation library.
That uses a log bridge.
**Pellared** 09:29 Yep.
**Liudmila Molkova** 09:32 And it wants to record… Ulcery.
What? What?
Why would it use a log bridge? Because of the .NET and Rust, where there is.
**Pellared** 09:46 Yeah.
**Liudmila Molkova** 09:46 Effectively one log bridge, and none.
**Pellared** 09:48 can happen.
**Liudmila Molkova** 09:49 Anyone else?
**Pellared** 09:50 in the wild, It will also happen for… for Go.
Because it's in the standard library.
And some people may prefer using, you know, the standard library, Instead.
So, I don't… it will not, you know… it will be probably extra-party instrumentations that may use it.
We will not probably do it in Otel, at least in Ottl Go, but… I totally believe that people from, you know.
Other companies or, you know, other authors may use it.
even native instrumentation, you know, may do it. I saw that some people are just emitting, you know, logs via S-Log.
And some libraries.
**Liudmila Molkova** 10:48 Well, the native… okay, yeah, the native would not… Okay, nature.
Patience.
How, like, how would they even provide this to friends? They cannot use instrumentation scope if they use a bridge.
Like, can this… this coexist?
Ever.
**Pellared** 11:22 So the only way I can imagine is that they, for the bridge, it will not be a problem, but for the first to re… you are right. For the scope name, it can be a bridge, you know, it can be the LEGO name, but for the instrumented library name, instrumentation library name.
The only way is that they will just include there in their own attributes.
**Liudmila Molkova** 11:45 But those are instrumentation scope, right?
**Pellared** 11:49 Yes, but instrumentation scope is the logger name.
**Liudmila Molkova** 11:53 Right.
**Pellared** 11:54 briefs, yep.
**Liudmila Molkova** 11:55 R-right. Oh, sorry, This, we would populate them as instrumentation scopes, so, like, you can populate them if you do logger, sorry.
group provider… Logger… Esther scope.
Name.
Version.
attributes.
how… If you use Bridge, you cannot use this API.
**Pellared** 12:41 Yep, you're right.
There'll be probably an… On the leaves, so, as log attributes.
But yeah, you're right.
I need to double-check one thing, because… I think that in Go, for instance, there is one librarian, which… allows you having, like, a logger name, and then attributes, a set of attributes connected to, to the attributes. I think right now we are bridging it as, you know, the leaf attributes.
Yeah, I think that's what we are doing.
Yeah, because, yeah, no, it's only Paris inside.
They could have, but probably it's extremely rare.
I just saw that right now, for instance, in Go, there's one which you can have, you know, this kind of logger level attributes, but then in the pipeline, they convert to, you know, to leak attributes. It's just an optimization.
That they casualties.
**Liudmila Molkova** 14:40 Okay, so then… We need all… Three attributes in the following.
**Pellared** 15:05 Yeah.
**Liudmila Molkova** 15:06 leaf.
Lock records.
Oh, maybe login breach.
Can have some logic that .
**Pellared** 15:28 It's cooled, but the problem is that it's hard to get back, because first you create a logger, before… Or maybe it can be done lazily. Yeah, it could be… You're right.
**Liudmila Molkova** 15:40 done and cached, right? So when the first time I get this logger name, I can, in theory, cache it, and with the high confidence thing that you should never get the same log record from two different.
**Pellared** 15:52 Actually, that's what we do.
If I remember correctly, in some bridges. That's exactly what we do.
**Liudmila Molkova** 16:02 Damn.
**Pellared** 16:02 Yes, we do it for the logger name.
Yeah.
**Liudmila Molkova** 16:11 it would get the library it comes from. It doesn't even know if it's instrumentation or instrumented, it's just that the the library that… created this record.
**Pellared** 16:32 You mean the bridge, or which one are you not, you're, you, You mean the right time to organize?
That's true.
**Liudmila Molkova** 16:41 I'm in the login bridge, catalog record.
It… if it'd never seen this logger name before… It can get which… library, this log record been written by? Some language-specific KPIs, whatever.
**Pellared** 17:03 Yes.
**Liudmila Molkova** 17:03 maybe unreliable.
**Pellared** 17:05 You mean some metaprogramming, like in Python or something?
That's what you mean?
OralDLL, information.net, or stuff like that.
**Liudmila Molkova** 17:15 like, the, the… yeah, executing assembly or something. Well, executing assembly is probably the… the binaries of the application, but then maybe you can… you can… it's just that it's a hard question to say which… which library this log record came from, right?
**Pellared** 17:32 Yes.
**Liudmila Molkova** 17:32 Like, but maybe you can.
**Pellared** 17:36 In some cases, I think people can just manually add those.
Just so you know.
**Liudmila Molkova** 17:44 the log record.
**Pellared** 17:46 Yeah.
you know, someone may use S-Log, and instead of, you know, replacing, and will want to make this Auto native, but not use our auto API, so they'll just, you know.
Create this manually.
That's another possibility, what they can do.
**Liudmila Molkova** 18:20 Great, I… I think that the… the pushback and… Third.
I have instead.
Yeah, there is an awkward situations and edge cases where all three can exist and they are different.
But most of the time, the log bridge name and instrumentation library name are the same.
Like, what do we do?
**Pellared** 19:16 I, like, if we do not have an instrumentation library, I will… will not have an instrumentation library name at all.
If there is just an application, Like, depending on the language.
Or maybe then you'll have the, you know, the name of the… or the assembly… name of the application.
If you would just… if… what… what would you like to have, if we have, you know, just regular logs coming from an application, like from Java or Python?
**Liudmila Molkova** 19:51 So the log record is created by the log bridge. The log bridge name, is also Instrumentation Library name.
**Pellared** 20:01 Yeah.
Yeah, I know.
That was your motivation, together with your central ask.
**Liudmila Molkova** 20:13 Yeah.
And then, if we introduce log bridge name.
Then we would say, okay, if you're a logger.
populate the log branch name. If you are not a logger, Populate instrumentation Library Name.
Unless it's your instrumentation scope name already, which you probably want to change at some point in the distant future.
Like, the… the asymmetry for signals is… the concern.
I kind of feel that… Oh.
The users recording things on log record, party on, use whatever attributes you want. Nobody expects people to do the right thing there.
**Pellared** 21:39 That's true.
Do you have a strong opinion here, by the way? Because personally, I don't.
**Liudmila Molkova** 21:51 I would start with Instrumented library, instrumentation library.
And if ever we need to differentiate instrumentation library and log bridge name, Okay, so…
**Pellared** 22:04 Oh, you.
**Liudmila Molkova** 22:05 We can't leave with it.
**Pellared** 22:06 How'd you say?
So you'll start it at the development.
and wait for some time before we get a pushback that it's wrong. That's what we suggest.
**Liudmila Molkova** 22:18 Yeah, but also if we…
**Pellared** 22:19 I happen to…
**Liudmila Molkova** 22:20 Stabilize it, and stabilize it in some log… bridges than…
**Pellared** 22:27 I like it, because if it's not working, then we'll get a pushback, and also, we'll have less, you know, lower number of attributes.
Less is better if it's… I like your proposal.
**Liudmila Molkova** 22:41 And even if we stabilize it, I feel like this distinction is so subtle that I.
**Pellared** 22:48 Yep.
**Liudmila Molkova** 22:48 I think we can live with it, even if we guess…
**Pellared** 22:51 also in the world.
**Liudmila Molkova** 22:51 Bro. Yep. Yeah.
**Pellared** 22:58 I think we can capture it.
**Liudmila Molkova** 23:02 Yeah, let me try to write it down.
**Pellared** 23:10 Like, that for now, we propose just to add Instrumentation library name.
Yeah.
as development, and… We can always add… Instrumented, like, log visioning if we get pushback.
**Liudmila Molkova** 25:51 And that's spell… Okay.
Okay, if you don't agree with something… Let me know.
**Pellared** 26:56 No, it's fine.
**Liudmila Molkova** 26:59 Cool.
Cool.
I wanted to chat about… okay.
**Pellared** 27:11 Only the last paragraph, I'm not sure if it was.
proper, like, proposal, let's start with instrumentation, library innovation, and this if while while.
Or maybe just while it's in development.
I don't know if, yeah, if it's not good.
Didn't we get? Yeah.
Yeah, this sounds good for me.
**Liudmila Molkova** 27:43 Okay.
I wanted to chat with you about something… There was this issue about prototypes.
For the log stabilization… exception stabilization.
Maybe I just need to read the spec more…
**Pellared** 28:17 from the top.
**Liudmila Molkova** 28:18 ones.
Yeah.
So this is the Pure Etrusc… Trusk's Pure.
And Alice… Curious what we thought about… Exceptions in general.
It's like, when we… when somebody calls a record exception.
What did we want to do?
Oh, so this is a flag.
So I can imagine, I'm a tracer.
And somebody logs… Calls record exception.
Did we want this flag to affect?
That.
This is…
**Pellared** 29:44 You mean… you mean from the Tracer API, if someone calls the exception, this is what you might mean?
**Liudmila Molkova** 29:52 Right.
**Pellared** 29:52 something else.
So these are only recommendations to not do it, for not doing it?
I'm not sure if we haven't… has something in the OTAP.
About this one.
I think what we agreed… I think in the OTAP, We agreed to deprecate is… So, it will not be used, and keep the existing behavior, because someone may rely on it, and if someone wants to switch to the new logs, we prefer that they also change the calls to use logs and no traces, so it's intentional. This is what I remember.
**Liudmila Molkova** 30:38 Right, let's see… So I'll spend…
**Pellared** 30:43 Or maybe if it's not… it was not the OTAP, I think, this was our…
**Liudmila Molkova** 30:50 Or for surety.
the Prada… specifications… Along with API.
**Pellared** 31:05 So, yeah.
**Liudmila Molkova** 31:06 Yeah, the…
**Pellared** 31:08 deprecated, and keeping, and I remember there were people in the… issue, which we created, that they really wanted to keep the existing behavior and have it deprecated, because some people rely on, you know, unspan events.
**Liudmila Molkova** 31:26 They, they do. Like, if I read this document, There's the span exceptions.
It has this blurb.
**Pellared** 31:38 Yeah.
**Liudmila Molkova** 31:38 So, you, you can read it as… It's obtained.
And if somebody opts in?
The record exception.
would…
**Pellared** 31:51 Yes.
**Liudmila Molkova** 31:52 actually made it as a log record, and there is a PR in Python that does it.
And…
**Pellared** 32:01 Okay.
**Liudmila Molkova** 32:04 I would… I think we… first, we should clarify, like, if we… wanted to happen, but for Python, so they… they kind of emit Exceptions.
So you, you write something, like, Sorry, this is the wrong one.
First friend.
So, you can write some code, like, eracer starts pen.
**Pellared** 32:40 Okay, but why cannot we start using the Lox API instead?
**Liudmila Molkova** 32:47 Because no severity?
No… Yeah, non-severity, mostly.
But they… well, they can.
It'll just suck.
**Pellared** 33:13 I think that was also one of the reasons that we wanted to, you know, think about the severity when they do it, and they can also leave it at and specify if they want.
**Liudmila Molkova** 33:24 Yeah.
Okay, so then let's talk about… That's separated.
One… Lawyers, opt in onto logs.
Should span exceptions be?
Span events. Good.
And then to be translated.
Gross.
**Pellared** 34:00 I think the question… question here also is.
Who is making this opt-in change? Is it the operator?
Or someone, you know, application developer or instrumentation library author.
Because if… it will be, you know, an operator, an SRE, then you'll probably want it to have it configurable via, you know, SDK, environmental variables, or something like that.
**Liudmila Molkova** 34:31 So, if it's the… I… Okay.
**Pellared** 34:34 pink?
I think… we had… I think in some… I'm not sure where was it, but I think we also had some… Or maybe not.
Did we have some spam processor that was changing spam record exceptions to lock events. I don't think so, because I don't think we have a hook.
**Liudmila Molkova** 35:01 It's the opposite, right? We… it has the back compat mechanism, so when… so if I'm a user, also, if I'm a developer, and I'm changing to logger.
Then the operator might want them as span events, and then you convert them to span events with the processor.
**Pellared** 35:22 Alright.
You're right.
**Liudmila Molkova** 35:25 Okay, so this France… Switch… the, new API?
Yeah. Operator… Right there.
Switch was n4, and switch to logs.
And can… Convert logs back.
to spend events.
If… to normalize.
Okay.
But in general, it seems you're thinking it's not a problem.
Right?
**Pellared** 36:21 It's not a problem to… that we, to change the API calls?
**Liudmila Molkova** 36:28 It's not a problem if… Thus… opt-in.
environment variable changes how SDK records Exceptions.
Let's see…
**Pellared** 37:02 Like, technically, I do not see a problem.
The only problem I see is just another feature that other languages need to implement.
**Liudmila Molkova** 37:15 Yeah, so let's take a look. Let's say I'm… I'm a Quadlane developer, and I'm just adding a new feature to… my SDK. I go look at the… To race?
And I look… API, and the request.
the board… Exception…
**Pellared** 37:42 And this will hopefully be deprecated.
In your future.
**Liudmila Molkova** 37:46 Yeah, but, like, I'm reading it now.
And I'm going to this outline exception document.
And it's in development, and this is… Or two semantic conventions.
The formal semantics of these attributes are defined in semantic conventions.
You can go here.
It's deprecated, and it tells you to use semantic dimensions for exceptions and logs instead.
So you can read it as… Okay.
I'm a Greenfield Singh.
And I should implement this opt-in flag, maybe, or just default to logs for.
**Pellared** 38:52 credit report, etc.
**Liudmila Molkova** 38:52 session.
**Pellared** 38:53 I now understand. Yeah, this is not for SDK, this is for instrumentation Library. Yeah, this makes sense.
**Liudmila Molkova** 39:00 I, I, I can't… I can, like, I don't feel the… problem in SDKs following this guidance, but as you mentioned, it's just a lot of work for nothing, right?
**Pellared** 39:14 Yep.
**Liudmila Molkova** 39:28 And then we can clarify.
**Pellared** 39:32 I think having these enematic conventions, like, I don't trust proposed.
It's okay, because then the instrumentation library decision, if they want to propose, you know, this, delegating via environment variable, and if they have some users which really want to play safe, I think it's a good call to have this.
I think it's a good call that, you know, semantic conventions allow this gating route, and there's… there's a formal way, if someone wants to do it, then how… how… how… what is, you know, the recommended way? But I'm not sure it should be forced on the SDK to have this.
**Liudmila Molkova** 40:12 Yeah, so, like, we can either say here that this is not the guidance for SDKs, or we can say… Maybe.
**Pellared** 40:21 I think it's… I think it's… I think it's pretty clear here or not, the semantic conventions.
We're recording… patient exceptions.
**Liudmila Molkova** 40:31 This is the… our application.
**Pellared** 40:35 If this instrumentation should work through this event.
**Liudmila Molkova** 40:39 Oh…
**Pellared** 40:40 Oof.
Also, this is good, because then if someone opts in, then people are using, you know, the logs API, which means that they have the severity, etc. If it will be an SDK feature, then they'll miss, you know, all of the fields that are coming from the logs API.
**Liudmila Molkova** 40:58 Right.
Maybe… I don't know. I kind of feel… It says should be recorded as an event.
And you know what?
Advantage?
So, okay, so maybe a more practical question.
Let's try to answer a more practical one, and we'll get… maybe it'll help us with the more general one.
Okay, so what happens in Python today?
You do this?
And this result…
**Pellared** 41:41 I'm good coffee.
**Liudmila Molkova** 41:42 Ben?
Exception.
an event.
So there is a PR in Python.
that… That con- that converts.
this guy into log records. So then the SDK wraparound spans for the mid-log records.
**Pellared** 42:11 I think it makes sense.
**Liudmila Molkova** 42:14 I think it doesn't.
Because… Well, first, in Python, the exceptions are a standard way to communicate status codes.
like, I don't know, HTTP, or, like.
**Pellared** 42:31 It's country inspiration.
**Liudmila Molkova** 42:32 404.
**Pellared** 42:33 Control flow. I see control flow.
**Liudmila Molkova** 42:36 Yeah, it's the most popular way of control flow in.
**Pellared** 42:40 I didn't remember.
Request library, I think, also uses it, if I remember correctly.
**Liudmila Molkova** 42:46 Yeah, and it's… exceptions in Pardon are so noisy, and they are so big.
And I think they should not have… Them recorded by default.
**Pellared** 43:00 Okay.
**Liudmila Molkova** 43:00 And I think this is a good opportunity for them to stop doing this, because if there is an opt-in flag.
I don't know.
It sounds like…
**Pellared** 43:18 I remember that we have a similar request, or… in Go.
to not… because right now, I think that's also what we do for panics.
That we just, at events, we do not spend the errors, and the problem is that It kills these tax races.
And also, there is no benefit, because some people do not, like, would prefer to have no span events at all. They'll prefer to have, you know, clean, clean stack traces when the application crashes.
**Liudmila Molkova** 43:55 Oh, because you essentially add a frame every time when you catch it and log it, right?
**Pellared** 44:00 Yes, sir.
**Liudmila Molkova** 44:01 Yeah.
**Pellared** 44:01 And when it's, you know, the problem is when you have it also cascaded, you know, nested.
Then you're reconstructed many times, and you have a big mess.
And we have an issue for it in Go, but I had forgotten.
That's probably Ajit.
**Liudmila Molkova** 44:19 Yeah, and also… If you do this, then you effectively need to record on every… Encompassing span, like, it bubbles up and you record it on every hub.
**Pellared** 44:31 Yep.
**Liudmila Molkova** 44:32 Yeah.
**Pellared** 44:33 Yep.
Exactly, that's what happens.
**Liudmila Molkova** 44:36 Okay.
So… It sounds like the practical problem is… not related. We would rather tell them, don't, don't touch it, if SDK wrote this fan event, that's fine.
**Pellared** 44:53 Yes.
**Liudmila Molkova** 44:54 You cannot change it now, because it's stable for years, but going forever, don't… replace it with log records, kind of deprecate this flag, let it die gracefully. Maybe with a different opt-in mechanism or without mechanism, because this one is for instrumentations.
**Pellared** 45:14 Yes?
Yep.
**Liudmila Molkova** 45:17 Okay.
Cool, then I'll follow up with Python, and… yeah, thanks for this dive into history.
**Pellared** 45:26 Thanks. And I also go to the… also, I will need to find the also go issue to add this opt-out in our SDK.
**Liudmila Molkova** 45:34 Hmm.
Yeah.
Cool.
Dan, I don't have anything else.
**Pellared** 45:43 No, that's good for me.
**Liudmila Molkova** 45:44 Yeah, good to see you. Stay safe, cool down.
So I'll…
**Pellared** 45:49 It will start… it will start… it will start tomorrow. We will have family rains.
**Liudmila Molkova** 45:55 Awesome, yeah. Nice. Enjoy. Bye.
