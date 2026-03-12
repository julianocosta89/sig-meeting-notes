SIG: Event WG
Date: 2026-03-03
Duration: 56 minutes
Zoom Recording URL: https://zoom.us/rec/share/1uXxCkkkwjOHnafG_LVuoFCu1bNuac1kQDH_Thq8eJ5gcJCDOpo6c76fOvzlqakF.i5cgP0HL7tYNBXSY
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 00:15 Hello again.
**Liudmila Molkova** 00:16 Fuck.
Start time.
I'm not sure I can make it to tomorrow's RPC call. I have a flight.
And I might be able to join from the airport, but I'm not 100% sure.
**Trask Stalnaker** 00:40 Cool, yeah, it's not a problem. We… last week, we just had a quick, kind of, sync on implementation prototypes.
I figure that's all we'll… Continue doing… At this point.
**Liudmila Molkova** 00:58 Yeah, I left a comment with my prototype findings for Python.
on the… I'll add it to the agenda anyway, so yeah.
**Trask Stalnaker** 01:09 Yeah, thanks.
**Liudmila Molkova** 01:10 But nothing major.
Is Robert joining, do you know?
**Trask Stalnaker** 01:40 I don't.
**Liudmila Molkova** 01:45 He left a good question in the chat, I didn't have a chance to reply.
**Trask Stalnaker** 01:54 Oh, yes, yes.
I'll dump it here.
So this is… was kind of related to what I was mentioning in the GenAI SIG.
So initially… Initially, I'd… taken out, not had a default, so for our instrumenter, I didn't have a default, which meant that no… Exception events were omitted.
Unless you configured what you wanted as the event name.
and the severity .
**Pellared** 02:50 But I think…
**Trask Stalnaker** 02:52 Hey, Robert.
I… I think it makes sense for us to have Default, it could be surprising behavior to not Get your exceptions recorded.
**Liudmila Molkova** 03:11 Oh, so The instrumenter records exceptions, and it needs to know the event name to record it properly, and then you need an extractor, and it might not be there, and then you need a default.
**Trask Stalnaker** 03:27 Yeah.
So, for… basically, to have a default, we have to decide on a name, and that's where I always say, like, you know, it could be, like.
Could kind of see an argument for just… Exception.
And a severity. I wasn't sure about this. Originally, I was trying to make the default severity be… That whole local root-based thing.
But since that failed, and based on discussion we had last week in SEMCANT, Or yesterday. I don't remember which.
Severity worn felt reasonable.
default.
**Liudmila Molkova** 04:14 Thinking about defaults, let's say you have a global exception handler.
like, per process. In some languages, you can.
There should be… Like, what would you put there?
Maybe we keep the exception?
Or maybe it should be… It's an instrumentation, and then instrumentation name works fine, right? I don't know, global… .NET Global Exception Handler, or GoPanic.
What is instrumentation name? Is it instrumentation scope name?
**Trask Stalnaker** 05:15 Yes.
**Liudmila Molkova** 05:21 Lowercase.
Special characters removed.
**Trask Stalnaker** 05:43 I mean, doesn't have to be.
**Liudmila Molkova** 05:50 It doesn't have to be. I'm just curious what happens if you add, acts or spaces.
**Trask Stalnaker** 05:57 Yeah.
**Liudmila Molkova** 06:14 And just plain exception also makes sense, because… We know the structure of this event, it's just an exception.
Maybe just… let's just keep it?
It's like, we could say that instrument… the exception… or I'm now saying exception should not be used. I would say it… Should not be… it could only be used by the… Exception handlers that don't have any information about specific.
**Trask Stalnaker** 06:53 semantic conventions.
**Liudmila Molkova** 06:55 Yeah.
**Trask Stalnaker** 06:56 Yeah, like, we wouldn't use it in semantic conventions.
But it is… Fine as a… fall back.
**Liudmila Molkova** 07:07 Pull back, yeah.
And then the… if somebody cares about instrumentation school, they would still see it, right?
**Trask Stalnaker** 07:18 Yeah.
**Pellared** 07:25 Maybe something, like… unfundled exception.
**Liudmila Molkova** 07:37 Yeah?
What severity would you report it with, if it's… If you don't know where it came from. The instrument on your… But fatal, unless you have strong reasons to report it as something else, like it's global handler, and it's… you know the process will crash.
And, out of memory, what happened in this global… may happen in this global handler, or go panic, right?
**Pellared** 08:30 out of memory, not really… it's not possible to catch it, as far as I remember.
**Liudmila Molkova** 08:40 It's possible to catch it in Java, but is there a global handler in Java? Maybe not.
Any GoPanic, like, what… how would you record GoPanic?
**Pellared** 08:55 Hard to say, probably as a name, you mean?
**Liudmila Molkova** 08:59 Huh?
**Pellared** 09:00 I will name probably same as in other languages, even if it will be an added exception.
Just for, you know, clarity. But if it will be a real panic, it will mean that you do crash the application, then it should be fatal.
But then the problem is that it depends… how someone structures and uses, basically, this kind of, you know, unhandled panic instrumentation. Because then, if it drops further in his own middle layer, or whatever, then it can no longer work.
**Trask Stalnaker** 09:33 Crush.
**Pellared** 09:34 Maybe configurable, severity, I'm not really sure.
**Liudmila Molkova** 09:39 So you don't know whether, when you… .
**Pellared** 09:43 So learn about… huh?
I'll give you an example. We have, like.
we have some middlewares, in some, for instance, HTTP libraries, where we catch some unhandled panic, and then we just report it as a span… as a span error.
So, this will not lead to a crash.
And the other case would be, like, some global, global handler, which catches when… There is an 100th exception if you call the crash, then we will look it as fatal.
**Liudmila Molkova** 10:19 So you know when, you get the exception that's about the crash application. That's my question.
**Pellared** 10:26 Nope.
**Liudmila Molkova** 10:30 Okay.
So you would never be able to set fatal severity in Go.
Or would you?
**Pellared** 10:37 Only if it's configurable.
Meaning that the user who uses it, would need… it depends when this instrumentation or non-Hub exception is happening. If it's globally, if it's the outermost.
If it will be the antermost unhandler, kind of, unpanic handler, then we'll know that it will crash the application, because nothing before has handled it.
**Liudmila Molkova** 11:02 Do you know if it's out there most?
You're saying you don't? Okay.
He's good.
I'm starting to think there will be no instrumentations that can set battle, or it's a very rare case that they could.
**Pellared** 11:30 But I remember that, I think in those nets.
If I remember correctly, in different auto instrumentation.
If there's an 100th exception, I think there was an argument Which was telling you if it's crashing or not.
And I remember in automatic instrumentation, if we know that it is supposed to be crashing.
we are flash… we are basically shutting down the SDK to make sure that Give a chance to emit the telemetry.
This feature is configurable, so if someone has a custom unachended exception handler, they can disable it.
But I think it's enabled by default.
**Liudmila Molkova** 12:14 Yeah.
**Pellared** 12:15 If it helps you, because I know that marino.net, I can show you the code.
Do you want it or not?
**Liudmila Molkova** 12:22 No, no, no, I can guess that there are some edge cases where .NET would be able to do this.
And then between error and warn.
If you get an unhandled… Exception.
**Pellared** 12:40 I agree with Trask that if it doesn't crash the application, it probably should be warned, because it means that, you know, based on your previous severity definition, trying to use the lowest those things.
**Trask Stalnaker** 12:58 Kind of depends, though, like, I don't really… because Java doesn't have a kind of global.
**Pellared** 13:04 Examples…
**Trask Stalnaker** 13:04 reception handler.
Like, we have the red.
Could it be… like, if it's… Saying, oh, this… Yeah, like, if I had, like, a Tomcat, like, a server, like a global exception handler in a server instrumentation.
I would probably report that as error.
**Pellared** 13:35 Similarly, like, we do in HTTP middlewares. If there's an error which happens, we also report the span as error.
**Liudmila Molkova** 13:44 So, like, yeah, no context worn. Some context then use the guidance that we have.
Okay.
What do you folks think about exception versus unhandled exception? I like unhandled exception more.
**Trask Stalnaker** 14:21 Let's also consider in the context of, are some con… We've got Is that what we did?
**Liudmila Molkova** 14:40 bunch request exception, I think.
**Trask Stalnaker** 14:51 unknown exception.
**Liudmila Molkova** 14:54 Unknown. Oh. Right, good luck.
**Trask Stalnaker** 14:58 Like, this is unhand, I mean… Somewhat.
Oh, like, this is unhandled.
**Liudmila Molkova** 15:05 Hmm.
**Pellared** 15:07 response, right? HTTP server? Response, probably.
**Liudmila Molkova** 15:12 Oh, we called it your clothes.
**Trask Stalnaker** 15:14 Probably a content request.
request duration.
**Liudmila Molkova** 15:18 Yeah.
**Pellared** 15:19 Okay. I see.
**Trask Stalnaker** 15:30 The other question I was gonna ask is.
How valuable do we think it is to have these names?
And… Or should we just coalesce on… One event name for all exceptions.
**Liudmila Molkova** 15:53 So, if we call a…
**Pellared** 15:55 I like this proposal here, which you have, because, for instance, someone can have, you know, this middleware.
for instance, for some HTTP server, which handles the exceptions, the errors, and handled, and you can have, you know, HTTP server request exception, and use a separate panic, which is totally crushing the application, and HadnessException, yeah, I think it's a nice convention for event names, and you can distinguish them.
**Trask Stalnaker** 16:25 So, maybe unhandled exception has more… is more than just generic. I mean, is unhandled for… Yes.
**Pellared** 16:34 After that, like, crashing, something like that.
**Trask Stalnaker** 16:37 Global.
**Pellared** 16:38 crash?
And it should be a fat pedal.
**Liudmila Molkova** 16:58 And that's… that's equivalent to exception with severity fatal, right?
**Pellared** 17:09 Equivalent, but it means that it was not emitted manually.
someone has not, I don't know, has created some library, and manually, you know.
created an exception, like, oh, you have an invalid configuration, you know, fatal with the content of the configuration, you just get, you know, an exception, some struck race, etc.
It means that, basically, it was not handled… it was, you know, it's just an unhandled code path.
**Trask Stalnaker** 17:42 How does… I mean, for users, the… Is that more… I mean, they're already gonna see fatal… I mean, all fatal exceptions are unhandled.
**Pellared** 18:04 I see, because these are exceptions, this is not an error.
This is not a logger, you're right.
**Liudmila Molkova** 18:16 What a fraud.
Don't have individual event names.
I think we're closing the door.
by doing this.
to… half, like, Useful.
Exception events.
**Trask Stalnaker** 18:42 Oh, I see, with the structure.
That's a good point.
**Liudmila Molkova** 18:55 Sick.
We… Didn't add any attributes to them.
Because we're too early in this process, we don't know what's useful, but we wanted to.
**Trask Stalnaker** 19:10 Right.
That's a good point.
I like that. I mean, just… I mean, so this for SEMCONS, and this as sort of just the fallback.
no SEM… there's no SEMCON… well, it does have some SEMCON meaning.
Because we would have the exception attributes under it, so we could actually define this in semantic conventions.
**Liudmila Molkova** 19:59 I'm adding a comment to my PR to reflect it there.
**Trask Stalnaker** 20:06 Whoa.
**Liudmila Molkova** 20:37 While we are on it, can we talk about… The semantic conventions, pure…
**Trask Stalnaker** 20:52 Yeah…
**Liudmila Molkova** 20:53 Sorry, Robert, to Heding it before.
**Pellared** 20:56 No, no, no. No, no worries. Your PR needs to be shipped.
**Liudmila Molkova** 21:00 No, it's just, very related to what we just discussed, so I don't want us to lose context.
**Pellared** 21:06 Both of these true.
**Liudmila Molkova** 21:10 So I'll update this, Two points. Maybe we should start with the… Trace versus debug.
So I updated this PR to say that you should not record artificial exceptions at all.
That we recorded with trace, and essentially that you'd rather not to record them. So I removed section about trace.
Robert, you wanna allow trace? I don't mind, I just want to be… more prescriptive.
than… than, necessary. So, like, if… if everybody would start emitting exceptions, sometimes with debug, sometimes with trace.
**Pellared** 21:58 Okay, I have a question. Stop on and read it.
then does that mean that they should never use trace if you're manually instrumenting something with logs?
**Trask Stalnaker** 22:08 For errors. No. For errors.
**Pellared** 22:11 Because someone can understand it like that. And that's why I just wanted to add it.
Or maybe I have lost something when I was reading it.
**Liudmila Molkova** 22:24 So.
**Pellared** 22:25 very possible.
**Liudmila Molkova** 22:26 Yeah, it went through a bunch of, changes. So, I've added a note based on also CJR's comments.
That, who this guidance applies to.
**Pellared** 22:40 You just… .
**Liudmila Molkova** 22:42 Here, open telemetry instrumentations and semantic convention authors.
It does not apply to login bridges, and it's how exception events should be recorded.
Guidance on when to record exception is left to specific semantic conventions.
So what I try to say here is that it's not prescriptive on when to record exception. It's only prescriptive on When not to, and… how to…
**Trask Stalnaker** 23:20 I have a question on the… yeah, this is really, yeah, I think this is a really important… Is it guidance to… Instrumentations, or is it only guidance to semantic conventions?
**Liudmila Molkova** 23:38 Mmm.
**Trask Stalnaker** 23:39 what's… the difference, I guess.
**Liudmila Molkova** 23:45 Think Symmetric conventions, right?
Yeah.
**Pellared** 23:50 So probably this should… this part should be moved to the document… to the part about Recording errors, right?
Which is more forward… the users.
**Liudmila Molkova** 24:05 Mmm, yes, similar.
**Pellared** 24:07 General recording errors, I think…
**Liudmila Molkova** 24:14 Yes, probably.
This is the meta guidance.
Yeah, go ahead.
**Trask Stalnaker** 24:22 To this page. Sorry, I'm, was… yeah, I was kind of asking it.
Robert, what's the difference there? You were saying it should be moved Is recording error.
**Pellared** 24:34 understanding, I… for me, I… yeah, just… I think they are somehow overlapping, but I think most of the users, people who are writing instrumentations, probably should start here.
Yeah, I think this is targeting the instrumentation authors.
And then we reference from here to the other one.
**Liudmila Molkova** 25:10 So I think there are two parts. One part of guidance is…
**Pellared** 25:13 exceptions.
**Liudmila Molkova** 25:14 If you write semantic conventions, this is how you do it, but if you are a user application, you can still use this guidance, it's just not normative to you, it's best practice.
**Trask Stalnaker** 25:41 Yeah, I don't know how to communicate, like, I do agree it's important to kind of communicate that We're… we're making choices… here… Specifically for, semantic conventions, because we want… we want to narrow our choices down when we define semantic conventions, because of other constraints. Namely, we don't want to always be debating among ourselves, should it be debug or trace? We like to have more strict guidance.
Whereas, for users, Like, there's nothing that says Trace is… isn't just as good for users to pick. Like, backends shouldn't… Have any preference for debug over trace or something?
But that was… that was sort of my… And, yeah, I don't know if it's… Spilled out, but that… was… how I was kind of viewing this whole page, and maybe why I didn't quite follow some of CJO's concerns.
There, because I was thinking of this document in terms of just… It's like a how-to-write exception, how to write, semantic conventions Guide.
**Pellared** 27:22 you know, so.
**Trask Stalnaker** 27:23 maybe…
**Pellared** 27:23 So it's the other way. People find it as a meta-semantic conventions, basically.
**Trask Stalnaker** 27:30 Right.
**Liudmila Molkova** 27:30 Yeah.
**Pellared** 27:32 I think this is how I read it. This is just a matter, you know, it's applicable for all, you know, exception logs, etc.
**Liudmila Molkova** 27:43 it mixes, right? So there is meta.
And there is, there are attributes.
So, like, the attributes are… For everybody.
**Pellared** 27:55 the…
**Liudmila Molkova** 27:57 Event definition.
It's for everybody.
**Pellared** 28:01 Yeah, that's what I mean. For me, I mean everything is from everybody here.
**Liudmila Molkova** 28:07 So, maybe… I can structure this document.
In slightly different manner, right? So, it could be called It could be separated into major sections. One is guidance for semantic convention authors, and the other one is event The base event definition, exception event definition.
**Pellared** 28:31 I may be wrong, but I think you had something like that for metrics, or somewhere, for naming metrics. I think you did have some sections like that, which pointed out very clearly that these are targeting the authors of, you know, of, authors of your semantic conventions.
**Liudmila Molkova** 28:49 Yeah, if we put it just there… Well, we can put it there, and we can link to… add a link from this page there.
But… prob-probably.
**Pellared** 29:09 If it will be easier, even for us to review, we can also split it into two parts, which is one, you know, PR, the recommendations for everyone, and second, which is for semantic conventions offers.
**Liudmila Molkova** 29:26 And we already have recommendations for everyone, right? It's what's already in the doc.
**Pellared** 29:33 I will say that a few things here are also good recommendations for everyone, like the exception…exceptionName. I think it could be a recommendation from everyone, for instance.
the severity suggestions, I think most what you have written here It's kind of also a good guidance.
**Liudmila Molkova** 29:54 Right, so that's why I wanted to keep it here. It's the requirement for semantic convention alters and recommendation.
**Pellared** 30:02 Yes. Lower case for everybody else. Yes.
So, the thing is that I was not sure if not allowing trace, for instance, is a good recommendation for everyone. That was my concern, because this is how I was reading this document. I think not recommending info is a good recommendation, because having an exception with this informational Yeah.
I don't know, in my mind, it's… At least awkward.
**Liudmila Molkova** 30:32 I didn't… we, like… We can… I can add sections for info and trace, just to provide clarity. Nothing says that you should not use it, but we can… I can say this is not for semantic convention authors, but application developers may use it if they want to.
**Pellared** 30:49 That's… that'll be perfect, I think.
**Liudmila Molkova** 30:53 Yeah, I like that.
**Pellared** 30:56 You can always refine it later. If someone says that it's not… Clear.
The number is wrong.
**Liudmila Molkova** 31:08 Yes, thank you, thank you for noticing, I really appreciate it.
Yes, yeah.
Embarrassing.
**Pellared** 31:14 Hard… hard blocker.
**Liudmila Molkova** 31:20 I don't know.
Okay, I left a couple of comments, the last, but probably the smallest one.
the lowest applicable severity number should be used. I think, Robert, you left a comment. I… I don't mind. I just felt it provides some… some clarity that if you… if you're in doubt, use the lowest one.
**Pellared** 32:37 The reason I give this suggestion is that the first I saw it, I had to think a little bit.
And I have… I had a feeling that for Trask, it was also not clear when he was reading it. Maybe I was wrong, maybe it was just my bad facial recognition.
But…
**Trask Stalnaker** 32:54 No, I…
**Pellared** 32:55 it'll be…
**Trask Stalnaker** 32:56 I agree, it doesn't, you have to really think hard about what it means.
**Pellared** 33:03 I think the cost-benefit is not worth it.
**Liudmila Molkova** 33:07 Okay.
I'll address it too. Let's… let's… let's commit, so… Robert shows up as code.
**Trask Stalnaker** 33:18 I think it's fine not to have it. I think it's sort of natural that you have to pick, sort of.
the best one.
**Pellared** 33:27 Whatever feeds the… whatever feeds the best one, right?
Please visit us.
**Liudmila Molkova** 33:32 So you have high trust in readers.
**Trask Stalnaker** 33:35 Well, I have high trust in the semantic convention authors, who… Oh.
take that.
**Pellared** 33:42 I'll convert it to you.
**Trask Stalnaker** 33:42 semantic conventions, and for end users, I don't, like.
They can emit whatever makes the most sense to them, is gonna make the most sense to them in the back end anyways.
**Liudmila Molkova** 33:54 Right.
Cool.
**Trask Stalnaker** 34:03 Yeah.
**Liudmila Molkova** 34:05 Thank you.
**Trask Stalnaker** 34:05 Progress.
Oh yes, blog post.
What did we… Austin had blogged once about it, right?
**Liudmila Molkova** 34:19 Not about that! It's… he blogged about… Oh, complex actions.
I blogged about complex attributes. Austin blogged about vision.
But not about spandon event deprecation.
**Trask Stalnaker** 34:36 Yes, I was… sorry, I did not even open the link. I made this assumption that it was about complex attributes.
Experiment, yeah.
Yeah, I think we have… We haven't really had a… we haven't had a plan yet. We're kind of… we're kind of starting to hit that, though, now, with the exception discussions.
What did we say we were gonna do?
**Pellared** 35:13 In the alt-up?
**Trask Stalnaker** 35:15 Yeah…
**Pellared** 35:16 long story short, what we are doing now, which means stabilizing stuff in… basically, I was surprised when I read the article that we are doing stuff so much aligned with our plan.
**Trask Stalnaker** 35:32 Yeah.
**Pellared** 35:33 This is weird.
**Liudmila Molkova** 35:35 Well, we are about a year later, but.
**Trask Stalnaker** 35:38 Yeah, but it proves that the OTEP process works.
**Liudmila Molkova** 35:46 I can write the blog, but it might take me… Like, 3 weeks to get to it.
**Trask Stalnaker** 35:58 So we're planning to do a spec, I'm planning to give one of the things that Ledmilla gave today for… Span event deprecation.
In the spec meeting, In some upcoming week.
So, yeah, it… if I… I might get to it before you, or you might get to it before me.
Cause I could… Do it as, sort of…
**Pellared** 36:26 hard…
**Trask Stalnaker** 36:27 propane.
**Pellared** 36:28 Do we want to have this blog post before KipCon?
So that people who take X and throw at us.
**Trask Stalnaker** 36:37 Sure.
**Liudmila Molkova** 36:39 You're doing a talk about logs, right?
**Pellared** 36:42 Yes.
**Liudmila Molkova** 36:43 Awesome.
**Trask Stalnaker** 36:44 There you go. You just volunteered.
**Pellared** 36:48 Yeah.
I'm just sorry about the English, but I have done AI.
**Liudmila Molkova** 36:53 Yeah, charge, yeah, GenAI is awesome at it.
**Pellared** 36:57 Yeah, yeah, I will start working on it, you can give me an action item.
Ehh… Even though it was not my proposal to deprecate it, I think. But yeah, I'm with you here.
**Liudmila Molkova** 37:11 Feel free to add me…
**Pellared** 37:13 I will actually both of you.
I see.
**Liudmila Molkova** 37:16 Yeah, so we can share their.
**Pellared** 37:19 incredible.
**Trask Stalnaker** 37:19 Oh, yes, yes. No, you can always point the blame back to me because of the, or the OTEP.
I did the trick on the complex attributes. I didn't want to be the only author of this blog post, so you all are there.
**Pellared** 37:37 I think it's, I think it's fair, because, yeah, because we are working together.
Alright.
**Trask Stalnaker** 37:49 Good deal.
**Liudmila Molkova** 37:52 Cool.
**Trask Stalnaker** 37:55 Yeah, I got nothing else.
**Pellared** 37:58 I have a quick question regarding the… I think hands of warm regarding this instrumentation scope attributes.
Do you think we should do something right now, or should Udemyo just wait for the TC to react? Do you have any preferences?
**Liudmila Molkova** 38:18 The only reason I didn't send a PR yet is because we don't have means to say that it should be reported as instrumentation scope attribute in… in the tooling, in the schema.
We can document it around and mark down.
**Pellared** 38:35 I mean, I mean, I think you… I mean the… I do not mean adding the bridge's name, this issue, I mean the fact about limiting.
**Liudmila Molkova** 38:44 Whoa!
**Trask Stalnaker** 38:48 the… yeah, the, the instrumentation… the library… instrumented library name one, I was also going to send a PR, but would… seems we don't have agreement on, even on the, like, which ones, like…
**Pellared** 39:06 Let's discuss it.
**Liudmila Molkova** 39:08 Yeah.
**Trask Stalnaker** 39:09 Yeah.
**Pellared** 39:09 I don't have an agreement, because I thought we… we almost do.
Yes.
**Liudmila Molkova** 39:18 Oh, this is a different one, actually.
**Pellared** 39:21 This is a different one, but yeah, but yeah, really.
**Liudmila Molkova** 39:24 places.
**Trask Stalnaker** 39:27 Is this… nope, this is not it.
**Pellared** 39:29 No.
**Liudmila Molkova** 39:30 Look for login for bridge.
**Pellared** 39:34 Fight me as an author, I do not have many issues here.
Oh, yeah, that's… Wonderful.
**Trask Stalnaker** 39:40 Yes, 23 comments, that sounds more like it.
Okay.
Yes. Okay, walk me through this, Robert.
**Pellared** 39:51 Yep.
So, you have Java.
And you have… when you have, Let's assume you have… you're using Log4j for logging.
So, you are using, and… and, the automatic instrumentation is having this long drive.
Look for the offender.
**Trask Stalnaker** 40:19 Okay.
**Pellared** 40:20 You want to… you want to have… you want to have, you know, this kind of telemetry.
So that's one thing that you want to report, and this version, but let's just talk about names.
So, there's one part. Second… You have the instruments library.
for instance, you are having… you love Spring, so you're talking about speed very often. So, let's say you have, you have Spring, you're instrumenting some string, HTTP, server, library, whatever. So this is the instrument test library name.
And the third thing.
**Trask Stalnaker** 40:56 Right, okay, let me… Let me catch up in the notes here, so… instrumentation… Instrumentation scope name…
**Pellared** 41:07 No, interpretation spoken for logs is different, but I just want to… I just want to first define the three points of data that we want to emit, and then we will say how we want to emit them.
**Trask Stalnaker** 41:19 Okay, so one of the points of data is… Log formation.
Bridge.
So… Which is like… Okay.
**Pellared** 41:30 So, kind of the instrumentation for the login library, kind of.
**Trask Stalnaker** 41:36 Yeah.
Okay, yes.
**Pellared** 41:43 The other thing is, so, I know that Spring probably has its own instrument logging stuff, that's my guess.
But let's assume… Or no, maybe, let's assume… we have the… this is one thing, we have the instrumentation library for Spring.
And the instrumentation library, which is probably hosted in, for instance.
in OpenTelements DIV instrumentation has some name, right?
**Trask Stalnaker** 42:13 The Spring Starter?
**Pellared** 42:15 I just know. Yes.
**Trask Stalnaker** 42:17 Because, to me, this is the ins… so, okay, so, like, Java Agent Spring in… The Java ecosystem, we've got these Java Agent and Spring Starter, but those are… we're modeling those, emitting those as… those are distros.
**Pellared** 42:34 Alright.
So, for instance, in .NET, this will be just, you know, an instrumentation library name.
**Trask Stalnaker** 42:45 I'm not sure if that's correct, though.
Oh, I…
**Pellared** 42:51 We are making bytecode instrumentation and stuff like that, we're just, you know, saying that this is, for instance, open telemetry instrumentation for Spring or whatever.
And this is following the specification, which says that instrumentation scope name is the thing… is the instrument… yeah, instrumentation scope, so… The name of the stuff that's instruments.
**Trask Stalnaker** 43:13 Right, but that's this thing.
**Pellared** 43:15 Beautiful.
**Trask Stalnaker** 43:16 Okay, so maybe you're talking about…
**Pellared** 43:19 5 people.
**Trask Stalnaker** 43:20 Auto… Instrumentation.
**Pellared** 43:25 Can you check the, the comment in the PR?
**Trask Stalnaker** 43:28 Yeah, yeah.
**Pellared** 43:29 Correct, because… Maybe there… Do you have something black, .
**Trask Stalnaker** 43:34 Okay.
**Pellared** 43:36 Because I, yeah, I was using…
**Trask Stalnaker** 43:41 Or it spans, also emits logs, okay, if you're a log bridge… Instrumentation Library.
**Pellared** 43:54 is…
**Trask Stalnaker** 43:56 Oh, I see.
You wouldn't use… your instrumentation wouldn't use log for J, your instrumentation would use…
**Pellared** 44:09 hotel log.
**Trask Stalnaker** 44:11 API.
**Pellared** 44:14 I'm not sure, I have different… I have heard in the past that some people want to use an instrumentation library, those things as well.
This is, like… Ideally, I agree.
But I'm not sure what will happen in the battlefield.
Did she?
**Trask Stalnaker** 44:35 Yeah, I guess… so that's where I'm, like, I… I liked the…
**Pellared** 44:47 Yeah. Even if we agree that this is not a desired scenario, We still need to define How we will name it, and which one has preference over the other in such scenario.
Yes, He's wrap.
And…
**Trask Stalnaker** 45:11 So to me, okay, so in this scenario, your instrumentation library is this.
You're using Log4J… In that case.
Log4j is what's going to ca- your Log4J bridge is what's going to capture that logging telemetry. You've lost the Mongo connection.
At that point. Why?
Because it's a different instrumentation… the appender is what's converting log for J.
**Pellared** 45:43 Yeah, but it's still coming from the instrumentation library. I know that there are a lot more translations to it, but it's still coming from the instrumentation library.
**Liudmila Molkova** 45:52 So, the instrumentation library name.
Sorry, not the instrumentation, the one who created… who emitted log, who used login API.
**Pellared** 46:02 Yes.
**Liudmila Molkova** 46:03 That… One would be reflected in the logger name, an instrumentation scope name. It would tell you, oh, it's coming from the MongoDB.
**Pellared** 46:13 That's…
**Trask Stalnaker** 46:14 You're using.
**Pellared** 46:15 That's cool.
**Trask Stalnaker** 46:15 We're using OpenTelemetry Log API.
**Pellared** 46:19 That's what we'll Jaffa do.
Appendix as well.
**Trask Stalnaker** 46:23 This is a weird case.
**Pellared** 46:24 I will.
**Trask Stalnaker** 46:25 Where your instrumentat- your instrumentation library, for some reason, is emitting logs over a log for J.
There's no place to push the scope.
I just… I don't see the… I feel like you're going to break that, and I don't feel like that's a really well-supported scenario that we care that much about.
**Liudmila Molkova** 47:00 Yeah.
**Pellared** 47:02 Okay, so now the thing is that… I am… 50% or maybe even 60% sure that people would use S-Log and S-LogBridge in Go for logging.
**Liudmila Molkova** 47:20 in… in…
**Pellared** 47:21 they…
**Liudmila Molkova** 47:21 Autel Experimentations.
**Pellared** 47:24 Not maybe in auto-instrumentation, but maybe some vendors will use it, some… some people will basically use their own oak or their own wrappers, etc.
**Trask Stalnaker** 47:39 Is there a place to put, Scope.
to pass instrumentation scope name… I see, and that's why you want to pass instrumentation scope name into there from the instrumentation.
And that's why you have these kind of double layers of instrumentation scope name.
**Pellared** 48:03 Yep.
To be honest, but to be honest, trust, After what you described for Log4J, I am not so confident as before, that I needed so much.
**Liudmila Molkova** 48:29 Do we, like, from the standpoint of… the bridge itself.
It's not… It knows it was cold.
**Pellared** 48:40 Yes.
**Liudmila Molkova** 48:42 But it does not necessarily know who called it, right?
**Trask Stalnaker** 48:47 Unless you passed the… caller, the instrumentation scope name, into the logger, as an attribute.
**Liudmila Molkova** 48:59 Well… Yeah, like, the logger name is pretty consistent across different login APIs. You would pass it through without.
**Trask Stalnaker** 49:09 semantical.
**Liudmila Molkova** 49:10 meaning.
**Trask Stalnaker** 49:10 I see. Yes, yes, sorry, I always get confused that the logger name is the…
**Pellared** 49:14 I have a question, now it reminds me one question, like, it's a new question.
Where would you use the instrumentation?
Name and version.
Apart from logging, do you see any other scenario where you use it, even?
Yeah. Okay, go on.
**Liudmila Molkova** 49:34 So in GenAI Seek, every several months, somebody comes and wants to record the genei.framework.
attribute to know where the telemetry is coming from. Not the instrumentation, but instrumented library.
**Pellared** 49:48 Yeah, yeah, but here we are talking about instrumentation library. I do not… instrumented library, I do not, no problem. Instrumentation library.
I…
**Trask Stalnaker** 49:58 I think it's this.
**Liudmila Molkova** 50:02 Yeah.
**Trask Stalnaker** 50:04 Where you might want more granular scopes than instrumentation library name.
**Liudmila Molkova** 50:13 if we were designing things from scratch, I would… I would… want to make instrumentation scope name part of conventions, and I would like for it to be consistent across languages, so you can filter, for example, instrumentations in the same way. Say, okay, I don't want… in declarative config, disable this instrumentation is not Pied to a specific library name.
And this could be achieved with different scope names. I think we're past this point, but… It could happen one day.
It reminds me of the instrumentation name.exception we just talked about.
**Pellared** 51:16 Yeah, because what my concern is that right now, the only use case I see for instrumentation library name and instrumentation library version is the login bridges. This is my concern for this proposal.
**Trask Stalnaker** 51:36 Let's… yeah, let's talk about this, then, because I agree with that. This was sort of… it made sense in my head at one point, and that's where I came around to this proposal, but now I'm trying to re-parse this.
Linmila, do you remember…
**Liudmila Molkova** 51:58 that, essentially, let's say we call instrumentation, like, let's say I have an AWS or Azure SDK.
**Trask Stalnaker** 52:06 My library, the same library.
**Liudmila Molkova** 52:09 emits two different layers. One is logical, another one is physical. I don't know, let's say AMQP.
It's the same library.
but multiple layers. And I want to name scopes differently, so that, the tracer enabled, metric, meter enabled.
**Trask Stalnaker** 52:31 Yeah.
**Liudmila Molkova** 52:32 You can…
**Trask Stalnaker** 52:33 Enable and disable things at the tracer level.
**Liudmila Molkova** 52:37 Right.
**Trask Stalnaker** 52:38 Based on these names.
**Liudmila Molkova** 52:39 Yeah, and it kinda sucks that today it's per library, plus arbitrary configuration options, and also it's… Library name is part of the configuration feature.
It's not awful. It's not great either.
**Trask Stalnaker** 53:07 Yeah, so I think it makes sense, like, say, if you have a… yeah, you're instrumenting something big, like… say, if in… theoretically, you had one instrumentation for all of spring, That instrumentation library You would want to have more fine-grained scopes.
But the instrumentation library would still be this sort of more monolithic.
**Liudmila Molkova** 53:37 Yeah.
And… we have this in messaging, we have this in GenAI, where we have multiple layers.
And Gen AI specifically. There are maybe 2 plus layers That exists, there's 3 layers.
And they ideally should have different instrumentation scopes.
**Trask Stalnaker** 54:09 Yeah, actually, we have that example, good example in the, Java, where we combine, like, Netty, Armuria, GRPC both have, both client and server instrumentation in the same instrumentation.
**Liudmila Molkova** 54:29 package.
**Trask Stalnaker** 54:31 And so… that would be nice to have.
The scope be more… Client… have one for the client scope and one for the server scope.
**Liudmila Molkova** 54:44 Yeah.
**Trask Stalnaker** 54:46 Again, so people could turn on and off just one of them.
**Liudmila Molkova** 55:06 In case of login breach, though.
Like, it's, it's… it's a hairy problem, right?
In the case of Login Bridge, isn't it instrumented Library?
**Trask Stalnaker** 55:23 Oh, instruments…
**Liudmila Molkova** 55:24 It's both, yeah.
**Trask Stalnaker** 55:26 Yes, it's both, yeah.
**Liudmila Molkova** 55:28 Yeah.
**Trask Stalnaker** 55:29 We want this to be… Hey, you're using the log for J… the OpenTelemetry log for J appender.
And this is, hey, you're using Log4J version… to… dot something.
**Pellared** 55:48 birth.
**Trask Stalnaker** 56:04 Cool. I'm gonna put this on our agenda for next week.
**Liudmila Molkova** 56:09 Alright.
**Trask Stalnaker** 56:17 con… Give us a chance to… Think a little bit more, and come back with some fresh Brain salt.
**Liudmila Molkova** 56:29 Yeah, and I also got the impression that we need to reiterate on the spec call why instrumentation scope attributes even exist.
**Trask Stalnaker** 56:47 Alright.
**Liudmila Molkova** 56:48 Thank you.
**Pellared** 56:51 Thanks.
**Liudmila Molkova** 56:53 CNN.
**Trask Stalnaker** 56:54 Until next time.
**Pellared** 56:56 Bye.
