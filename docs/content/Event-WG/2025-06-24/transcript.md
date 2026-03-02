SIG: Event WG
Date: 2025-06-24
Duration: 47 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 00:45 Hello!
**Trask Stalnaker** 00:47 Good morning!
**Liudmila Molkova** 00:49 Good morning.
I am going to Denver today.
**Trask Stalnaker** 01:06 Oh, yes, so Thursday a is the
the conference. Wednesday is the conference.
**Liudmila Molkova** 01:16 Thursday is the Conference Thursday.
**Trask Stalnaker** 01:19 Oh, tomorrow. Yes, Wednesday is the meeting.
**Liudmila Molkova** 01:22 Right, yeah.
**Trask Stalnaker** 01:24 Cool.
Yes, I will be there virtually.
**Robert Pająk** 01:27 Hello!
**Trask Stalnaker** 01:29 Hey!
**Liudmila Molkova** 01:33 I think I'll see Jason in Denver.
**Trask Stalnaker** 01:36 Nice.
I saw Jason in Portland last
last week just last week. Yeah.
**Liudmila Molkova** 01:50 You have a nice open telemetry community there.
**Trask Stalnaker** 01:54 We do? Yes.
**Liudmila Molkova** 01:56 It's I think it's bigger than the Seattle. One.
**Trask Stalnaker** 02:00 Well, but a lot of Microsoft people.
**Liudmila Molkova** 02:06 Alright!
**Trask Stalnaker** 02:11 But yeah, alright. What are we doing today?
Clock fig when in doubt?
Look at the agenda.
so I think we did pretty good on the oh, tap getting more approvals.
Daniel said he'd look at it today.
Josh said they probably wouldn't look at it this week.
I think. Given that it is.
I'm gonna ask him. I'll reply and ask check if he has
If he's okay with merging, and we've always got the spec, the actual spec to work out
details like if he's got any issue with the overall messaging
and then, yeah, I think we could probably
merge it end of next week end of this week or next week.
And then we can start. Yeah, actual spec. Prs.
cool.
**Liudmila Molkova** 04:22 Sure.
**Trask Stalnaker** 04:27 Robert, how so I totally agree with merging that one pr. Of yours, I think, sent
uncontroversial and has good approvals.
**Liudmila Molkova** 04:41 I can go ahead and merge it now.
**Robert Pająk** 04:45 Jack already merged.
**Liudmila Molkova** 04:47 Oh, okay. Nice.
**Trask Stalnaker** 04:53 Was there anything else that you wanted to?
We've got this one.
Okay. You've moved this one back to draft. Okay.
**Robert Pająk** 05:07 But you can take a look. I'm considering undrafting it, but I also think that maybe I could an issue
even before undrafting this one.
The thing is that from what I understand, you know the Java the Java prob proto pro, not pro. Yes, it's proto buff
the serialization and serialization that basically only endems, you know, which are inside the end. Them are properly working.
I'm just thinking how to basically how to make a like a pragmatic spec change
that would support all languages
and will mitigate possible issues, for instance, for you know, for auto lp. Java endpoints, etc.
So I was at the, because that's 1 1 thing that for Java, emitting anything outside 0 to 24 will be problematic, right? Trust.
**Trask Stalnaker** 06:11 Yeah, I mean, it'll just get mapped to 0.
**Robert Pająk** 06:14 Okay.
**Trask Stalnaker** 06:14 On the server side.
**Robert Pająk** 06:16 If you 2. Okay.
but because what? I was, because, on the other hand, for the other languages which already represent this as an enum, but not enum like in Java. But, for example, like in.net, or I don't know which basically is just a a syntactic sugar, for you know constant integers.
Such change in the specification will be breaking, because people will still be able to, you know, set the processing changes, etc.
So I was thinking about making this change, that the Otlp exporter basically must emit or should emit only values between 0 and 24.
What what.
**Liudmila Molkova** 07:01 But.
**Robert Pająk** 07:06 Yes, madame, go ahead!
**Liudmila Molkova** 07:09 And
it's already possible to meet other values. Right? So if everybody said 42, then we can, they cannot stop allowing it.
And the if there was a Java intend point that
treated as it somehow it should, it cannot. It shouldn't like us trying to
limit the support that set will not help
anyone, because the problem is already out. There.
**Robert Pająk** 07:43 I would say it can. I would say it can limit the impact. If people are using the sdks.
it will not. Yeah, because people will use the processors and will set minus 5. Yeah, it will just happen on the other layer. You're right.
Okay, trust.
**Trask Stalnaker** 08:04 I would. Just yeah. I think it would help me to
clarify, to come back to what is the problem we're trying to solve.
**Robert Pająk** 08:13 Yes, for me, for for me to explain.
**Trask Stalnaker** 08:20 Yeah, or or you know, document like, you said, like, but yeah, like, I, kinda
yeah, what are we worried about with the current language?
**Robert Pająk** 08:35 So 1st of all, I would say, the current language is very ambiguous. It doesn't
like this section from 301 to 300. No, not this one. The other one. Yeah. 421 to
the last one. This one
severity number can be compared to any 70 number, which in theory means to any number, because currently it is defined as a number, or to numbers one to 24, range, or corresponding short names. So 1st of all, why would you like how and why would you like to compare things from different types? Does it mean that this case? Yeah, this is kind of strange.
this kind of comparing severity.
So this is.
**Trask Stalnaker** 09:21 This line, this specifically.
**Robert Pająk** 09:23 Even even these numbers for 1, 24 range. We are talking about severity numbers.
**Trask Stalnaker** 09:29 Okay, okay, yeah, yeah. I mean, so do we
like, would, okay, that this makes sense to me. So striking this raise, yeah, okay.
**Robert Pająk** 09:44 So this is what basically. Yeah, yeah, feel should be used anything.
The other thing.
**Trask Stalnaker** 09:58 Right.
**Robert Pająk** 09:59 Yeah, because this was the main intention of this pr, just to striking this one and making some clarification, this special handling. If you thought that it may be good to add that 0 is a special value. This is the it's not. Here is the other. If you go to the spec. Change this last sentence. 421.
Yeah, you want it. Yeah.
**Trask Stalnaker** 10:24 Oh, right? Right? Right?
Okay, so this severity. Compare Sensor should be used.
Yes, isn't it?
Okay?
Okay, so that makes sense to me that feels.
**Robert Pająk** 10:48 The other change is just. I just replaced the the 301 to 304. I just re-remove the 1st sentence, as it is redundant with the comparing severity. It just says the same.
And I just added, I just added this kind of here, I just move it above
this section, because I think it's more it's a better place to put it there, because you can see, even in line 287.
**Trask Stalnaker** 11:22 Okay. So this was moved up here.
**Robert Pająk** 11:24 Yes, and I remove 301 to 300 free, because it's repeated the 1st time. Basically the same sentence.
**Trask Stalnaker** 11:31 Okay. Okay.
**Robert Pająk** 11:34 So it's about basically removing repetition, putting and simplifying this example.
I could revert this example. It's not a problem. It's yeah.
So this has, in my opinion, in my opinion.
**Trask Stalnaker** 11:53 Don't see any problem with it.
**Robert Pająk** 11:56 Yeah, that's what I thought. I tried to make this change
not related to 1, 2, 24, basically kind of restriction. And regarding to this 1 24 restriction it was, I think, point out by several people that
it could be problematic. But I see there's a breaking change
because of, you know, because of the current specification language
and all the specific of implement current implementations. Also that, as Ludumia said, it is possible to pass.
you know, different values using Otlp. So
I'm not sure if we even want to address this problem.
or we should maybe give some notice that it is preferred to use values in the range one to 24, maybe something like that. I'm not sure to be honest.
I'm not sure if it's worth even addressing this issue.
**Trask Stalnaker** 12:54 I, yeah, that's what I would say is just.
**Robert Pająk** 12:57 Yeah, if the cost is worth the value.
**Trask Stalnaker** 13:00 Yeah.
**Liudmila Molkova** 13:05 We. We already given a sign that we prefer one to 24 by giving them specific names, and then Java like, if you're right. Your Api. I think Java doesn't allow you to set numbers outside of the range. Python does not allow you to set and numbers outside of the range. And it's it's it. Technically, you can implement the SDK layer that prevents it. It's just not everybody did it.
**Trask Stalnaker** 13:30 Yeah.
all right.
**Robert Pająk** 13:38 Okay.
**Trask Stalnaker** 13:41 What else do we have? Logs.
**Nicole van der Hoeven** 13:44 Hi! I didn't want to interrupt.
All seemed like you're in the middle of something, but I just wanted to introduce myself. I'm new, so I'm still kind of like what is happening. But Hi! I'd like to get involved, and I'd like to try and figure out how exactly I'm Nicole Vanderhoven. I'm a senior developer advocate at Grafana Labs.
So I specifically work on Loki.
That's why I'm here.
T.
**Trask Stalnaker** 14:13 Awesome.
**Liudmila Molkova** 14:14 It's welcome.
**Nicole van der Hoeven** 14:16 Thanks.
**Robert Pająk** 14:18 Where are you? Back?
**Nicole van der Hoeven** 14:18 I didn't just want to be lurking here and not say anything, but I also didn't want to interrupt a conversation, because I was already a little late. I currently I'm in the Netherlands right now, but I go back and forth between the Netherlands and Portugal.
So I've I have a home in both.
**Trask Stalnaker** 14:37 Nice.
**Nicole van der Hoeven** 14:37 How about you, all of you.
**Trask Stalnaker** 14:42 I am in Portland, Oregon, in the Us.
About 200 miles south from where Lidmilla is.
**Liudmila Molkova** 14:55 Yeah, I am in Redmond. Well, technically, Kenmore.
Next to Seattle.
I'm at Microsoft. I work on
all the different open telemetry things
welcome to the group. And excited to learn like, what? What are your interests? From lucky side and
what are the things you find problematic with auto logs, or what do you like about them? And so on. But I think we also have Robert, who is closer to you than us.
**Nicole van der Hoeven** 15:32 Oh!
**Robert Pająk** 15:33 Yeah, I'm from Poland, from Krakow. So we are in the same time zone.
**Nicole van der Hoeven** 15:38 Well, that's handy.
**Robert Pająk** 15:39 So we yeah, it is, yeah. So.
**Nicole van der Hoeven** 15:44 Have you on?
Go on.
**Robert Pająk** 15:45 So personally, I just I'm working at Splunk, but I'm not working on any endpoint like you're, you know, in Locky. So you're kind of like on the endpoint. I'm working on the auto. Go thing so more on the producer side, I would say, not consumer side.
**Nicole van der Hoeven** 16:03 Awesome. To be honest, I'm still kind of new to the whole project, so I was just hoping to kind of lurk for a little bit and learn from you all, and start to get up to speed with all things hotel for logging. I actually I wrote an app for a talk. I wrote an app, and I instrumented it with hotel and very quickly found out that it wasn't as easy as I expected it to be.
And I'm like, okay, I need to make stuff for this to make it easier. But to be able to do that, I need to learn a little bit more about it. So I can actually talk convincingly about it.
**Liudmila Molkova** 16:46 Language, if you don't mind me asking.
**Nicole van der Hoeven** 16:48 Was in python.
**Liudmila Molkova** 16:50 Oh yes!
**Nicole van der Hoeven** 16:51 Yeah, there is just a lot of little things that I think need to be documented a little bit better.
**Liudmila Molkova** 16:59 And fixed.
**Nicole van der Hoeven** 17:01 Yeah.
**Trask Stalnaker** 17:07 Cool. Well, we we're
excited to have another member. We can see we're kind of a small group here we have the log. Sig has. Well, we we morphed from the event, Sig into a log, Sig. A little while ago, so I'd say the the main driving thing that we're working on is trying to stabilize events
which are built on top of logs.
But at the same time picking up
like Robert is working on stabilizing the log SDK in go. And so he's finding lots of interesting
edge cases that we haven't thought about or clarified in the specification.
**Nicole van der Hoeven** 18:05 Cool. Yeah, at Grafana we are. I mean, there's like the work interest, but also personal interest, which I'm sure is the same for a lot of you. But yeah, at Grafana we really want to make everything like hotel 1st Hotel Native, and we're finding some issues. So I guess I just want to make sure that we're not missing anything, and that we're compliant with with recent changes and stuff.
But also, just personally, I really haven't.
I come more from the performance engineering side of things. So the switch to Low Key is still, you know, I'm still relatively new kind of jump ship from from testing to observability and site reliability engineering. So just eager to learn.
**Trask Stalnaker** 18:55 Cool? So if you have, you found the the meeting notes, Doc.
**Nicole van der Hoeven** 19:03 Yes, I have.
**Trask Stalnaker** 19:05 Awesome.
**Nicole van der Hoeven** 19:06 I think I'm there.
**Trask Stalnaker** 19:07 Yeah.
**Nicole van der Hoeven** 19:08 I'm there now, right? Yes, I am.
Yes, just anonymous. For some reason.
**Trask Stalnaker** 19:17 Oh, oh, yes, yes, so feel free to add yourself to the attendees here. And you can see, we've got a big agenda this week.
**Nicole van der Hoeven** 19:27 So.
**Trask Stalnaker** 19:27 So welcome to, you know. Always throw any topics that you want to discuss on there, and
always welcome to lurk as well.
**Nicole van der Hoeven** 19:39 What I mean. I guess I would. Just sorry I don't want to. I don't want to take up too much time if if you wanted to talk about something.
Agenda.
Well, I guess if if it's okay, I would love like an overview of like, what what things we need and what what we're working on you mentioned. We're working on stabilizing events. What exactly does that entail.
**Trask Stalnaker** 20:05 Yeah. So I was just pulling up the board here. Which we
have neglected a little bit. But we come back to from time to time.
Which is probably a good
thing to look at, related to that to
this is part of the this.
So yes, this is this one is the 1st topic we were discussing. The pr, it should
do. Are we not closing?
Let's see, should we remark this one as getting resolved Robert, by this Pr.
**Robert Pająk** 20:58 Yes, works for me.
**Liudmila Molkova** 21:02 But wait! Should we close the.
**Robert Pająk** 21:04 That's this package, you that I would say that instead
like, if it will be resolved, we should also create an issue or something, just to make sure that we remove the section instead of keeping it as development or.
**Trask Stalnaker** 21:20 Oh, and this is sure.
Oh, Ted.
**Liudmila Molkova** 21:21 I just did you, yeah.
**Trask Stalnaker** 21:23 Yeah, yeah, yeah, no. That makes sense. This is just the hotel. So, okay, cool.
this is a another big
topic. We will want to.
**Robert Pająk** 21:43 For interrupting.
**Trask Stalnaker** 21:44 Yeah.
**Robert Pająk** 21:44 I wanted to put it in some blocked status, but I haven't found some. Do you need it or not?
Because I think that when we're building this, when this all type will be merged, I expect it will be more handy kind of this something like blocked when we just creating, you know.
**Trask Stalnaker** 22:05 Yeah.
**Robert Pająk** 22:05 To the door.
**Trask Stalnaker** 22:06 Yeah, I'll just put it in here, for now we don't really have a block.
**Robert Pająk** 22:12 2 years later. If it's only one, then it's not needed.
**Trask Stalnaker** 22:19 I feel like, okay, this was the Pr we were talking about. Okay, let's put this on.
Oh, next week I am.
I'm out next week. Okay?
So maybe the week after we can
resurrect this because I think once we merge that complex attribute.
**Robert Pająk** 22:50 If you have some time at the end of the meeting I have some feedback, and.
**Trask Stalnaker** 22:55 Ready!
**Robert Pająk** 22:57 I have some feedback around this one. Yeah. Because I was recently, we were recently looking at
reporting errors in go instrumentation libraries. I have not put any comment. Maybe I've
I think I may have referenced this issue somewhere.
But basically, I think that probably semantic conventions maybe even right now needs some care on the
for the spans which end as errors. But
we are just not sure if we need to report errors.
If there is an error which basically closes the span, and it is very not clear what how it should be handled. I think, right now.
**Liudmila Molkova** 23:53 Yeah, we. We have a section semantic conventions. Let's talk about it, though. I think
we have a somewhat related Pr and semantic conventions, and it's cannot make progress because we don't know how to what to do in go and rust where you kind of have stack traces, but you kinda don't.
and it's not exceptions. So I think your your feedback would be super
valuable on on this one as well.
**Robert Pająk** 24:21 Okay, I have. If you find it to be perfect. I have even recently added senior command, that for go
like there are 2 things.
One, each one ego is a panic
when, but which basically is like an 100 exception.
And for this kind of I would say, errors, we are even.
I'm not sure if stuck. Basically, the problem is that for go the struct race. When you're recovering, you're losing the initial stack trace.
You're not able to. You're only able to capture the struct trace when you're just in the place when you're capturing. So, for instance, in Python, you know, Java, when you're throwing exception. The the structure is persisted in. Go, you're losing it
when you're handling the exception. Basically.
**Trask Stalnaker** 25:18 Oh, you only have it when you, at the point where you record the error or not
like it doesn't bubble up.
**Robert Pająk** 25:27 Yes.
**Liudmila Molkova** 25:29 But there are some additional things you can do to preserve it, to trade, some additional libraries.
**Robert Pająk** 25:38 No, for unhelded exception, not really.
We can still have the Apis to record an error.
But this will be just in this will be like the current Api, and it will work which is not a which will be more like an event. Something happened, but it doesn't change the span. The span site to store error
correct
according to the semantic conventions. We do not even know when it is a good way to use them.
because even right now, I think this semantic convention says that record error should be not used for retries, so we don't even know what are even the use cases to use the record error.
**Liudmila Molkova** 26:21 Oh, the the current span event.
**Robert Pająk** 26:24 Yes, don't start right? Okay, that's good, because we assume there's no use case for it.
**Liudmila Molkova** 26:31 Well.
**Trask Stalnaker** 26:32 There is.
**Robert Pająk** 26:35 First.st
**Trask Stalnaker** 26:37 Is. But don't start, because then you'll have to migrate.
**Robert Pająk** 26:43 Okay.
**Liudmila Molkova** 26:44 Because it's fun events, right?
**Robert Pająk** 26:47 Yes. Yeah.
**Liudmila Molkova** 26:51 So I think in the scope of the top we will figure out whether we should record it as attributes on the span itself.
or as a log record, or both, or whatever.
**Robert Pająk** 27:04 But I think even right now the semantic conversion says that if a span, if there's an error which is ending the span, you can simply add the attributes.
**Liudmila Molkova** 27:17 Error attributes.
Well, maybe.
**Robert Pająk** 27:24 Can you open trust the semantic conventions? The current description of it may be exceptions.
I'm not sure if it was here.
Yes.
**Liudmila Molkova** 27:44 This is the span event.
There we chat.
**Robert Pająk** 27:46 There was a but there was another one. Let me find it. I recently created an issue, and I have all the hyperlinks.
Most probably you share screen.
**Liudmila Molkova** 27:58 I didn't notice your issue, maybe because we have a lot of.
**Robert Pająk** 28:02 No, no, they're only on go site, and I.
**Liudmila Molkova** 28:04 Oh, I see!
**Robert Pająk** 28:05 Use because I was not making sure to not not make a mess.
Is it.
**Trask Stalnaker** 28:14 Is it this document?
**Robert Pająk** 28:17 Yes, exactly. This is this document.
and if you scroll down a little bit further below, and this is this.
**Liudmila Molkova** 28:32 So this doc talks about errors right? And then the exception event is a separate beast.
**Robert Pająk** 28:45 Exactly so, for go I would say, most of the things are recording errors on spans, because usually, when something reports an error, we want to use this
when something panics, we treat it more as an exception.
and we can, which means that it's still which means that we can still probably add some attributes for the exceptions.
However, we are not able to get the struct race. We can add maybe an optional that someone may want to have the the struct race, but
it won't be very useful, but they can do have it. We have already it, but we are not sure if such exceptions should change the span to
to error or not, I think that it should, because it's an exception.
**Liudmila Molkova** 29:42 So if
it like, this document tries to say when to set status to error right? So if you believe that span ends with an error, she should set the status to
error.
And you would feel error type.
What I'm adding in the Pr. Is error message.
And then you don't have an exception as a language construct.
So I wonder if we should even leverage there is a code stack, trace, attribute to record.
Go stack traces.
**Robert Pająk** 30:21 But right now I think even right now, exception, you know the stack traces. I think it can be optional. If we do not have, we will just not admit them right? I think it's up to us. And right now, if you, if
thing is that if you refer to recording exceptions. If you pick your new task
here in this document, recording exceptions.
it doesn't say that it should set the span status to error, which is awkward, and I think it's a bug. But I'm not really sure.
**Liudmila Molkova** 30:53 Yeah, I think you're right.
You're right.
**Robert Pająk** 30:57 That's 1 thing.
And second thing.
What?
Why do we want to record this as a span event or rogue record?
What is the advantage of it. If it's thing, a thing that's finishing the span because it's a 900 exception.
**Liudmila Molkova** 31:19 So think about them as parallel things. The span is one thing, the exception is a separate thing.
**Robert Pająk** 31:27 That's what.
**Liudmila Molkova** 31:27 So year
can record the, it's just I don't. Actually, it's it's a great question. Historically, people really like to record exceptions.
right? Because they believe they are useful, like error, logs, or whatever.
**Robert Pająk** 31:42 Yep.
**Liudmila Molkova** 31:44 And that's that's why we want to record them.
**Robert Pająk** 31:45 So you want, basically, you think that it's better. And I agree to have a separate Api
to unhandled exception
from just a regular span error. For example, when an instrumentation library, when the library simply said that something failed
is my understanding correct?
That's what we do in. Go basically. Right now
see, you're you're you're special. You don't have exceptions.
**Liudmila Molkova** 32:14 But we have panics which are 100 exceptions. But we don't start right.
but they are and and handled meaning critical. It's something that is probably fatal. You would probably
restart your application after one happens right? You wouldn't panic on the transitor.
**Robert Pająk** 32:38 And yes, but right now I think our SDK stops them from being panicked.
so if there was a span I can check it right now, very quickly.
or maybe it's no. It's putting the panic further off.
**Trask Stalnaker** 33:02 You want, you bet.
**Robert Pająk** 33:03 You have a good point. I do not remember what what will happen right now.
**Trask Stalnaker** 33:09 Would you want that to show up in law in your log stream
or not like? I think that's
something that Mila said made me
think I I like that distinction of cause. I've been struggling with us, having these 2 concepts, errors, and exceptions, and like
how to why, we have 2 things and what they mean.
But I kind of like that idea of
errors show up on the spans, and exceptions are what go to the log stream.
**Robert Pająk** 33:55 Yes, I I think I think that's the idea. But I just wanted to double check it.
And yeah, I agree with it.
**Liudmila Molkova** 34:05 But, by the way, if you scroll down a little bit, trust
here just a little bit to the end of the example, we said, spend status error. So I just wanted to follow up on this one.
So the if we have this distinction, that exceptions go to events.
the logs and errors goes to spans first.st
Some errors don't have span and Spencer sample doubt, but people tend to
required logs, anyway, sometimes at least.
And also we've won the correlation right? So if
error like not even an exception, the error like I don't know certificate is invalid happened.
We want to record it consistently on spans and logs. Right
to me, exception is just a language. Construct. You record it in addition to error. If it's different.
**Trask Stalnaker** 35:20 Okay.
So I mean, won't exception. Message always be duplicative.
A error message.
**Robert Pająk** 35:34 I thought, I thought that exceptions here only means unhandled exceptions.
Is my understanding wrong or not?
**Liudmila Molkova** 35:42 What do you mean by unhandled exceptions?
**Robert Pająk** 35:46 It means that someone who basically was calling. And you know, for example, was calling.
for instance, making a Http request.
And it's thrown an exception, and the caller has not handled it.
**Liudmila Molkova** 36:05 So if you handle it, you would not report span status as error.
and you would probably report this. If you report this error on logs. You report it with lower severity.
It's not an error severity, but
if it's an instrumentation that every exception is unhandled, it doesn't know what happens
underneath. Right? It only instruments, 1.1 layer.
Everything that escapes is recorded, but it doesn't even know what happened inside. It shouldn't care.
**Trask Stalnaker** 36:54 So like, I like the idea that I mean
errors are the Gen. The more general thing. And so we want to have consistency. Want
uis to be able to basically use error. We don't want them to have to be like
check. Oh, if it's an error, or if it, there's an exception, so
so error should be there. If it applies no things like stack, trace type
message seems duplicative to me with error, error, message.
**Liudmila Molkova** 37:41 Yeah.
**Trask Stalnaker** 37:46 What else is on exception?
**Robert Pająk** 37:47 But.
**Liudmila Molkova** 37:48 There is a type.
There's there's error type, and there's exception type as well.
and they're slightly different. Because, for example, you can have. I don't know. Http request exception. It's the exception type. But the error type could be a subtype within it, like certificate, error
or connection reset.
**Trask Stalnaker** 38:13 Didn't we deprecate this.
**Liudmila Molkova** 38:16 We deprecated it. Yeah, does it show up
as deprecated? No, we don't render stability here.
**Trask Stalnaker** 38:35 This is the event.
**Liudmila Molkova** 38:57 Oh, there is a deprecated the the stability column. It just doesn't show up because the table is too wide and it's listed as deprecated.
**Trask Stalnaker** 39:07 We can probably remove it from this table. Right?
Oh, there we go. Yeah, yeah, right? Right? Okay.
so a stack trace type message. Okay?
And yeah, I I agree that error, type and exception type are different.
**Liudmila Molkova** 39:32 So the the Pr. I have to into semantic conventions. I'm not super happy about it, but what it suggests is
you only populate exception information first, st when there is a runtime thing called exception.
and it happened, and that you don't duplicate. So whenever you would
you do the best effort not to populate error, type or sorry.
You prioritize error namespace all the time, and
if you have reasons to believe exception, information will be duplicate. If you just don't populate it.
and then essentially, in some cases you would only have, let's say, exception, stack, trace.
**Robert Pająk** 40:20 Can I? Can I share my screen? I'll just double check if if we have mutual understanding
just to make. So this is the go code, I think, just make it bigger
of when span ends. So basically
so basically, if there is a panic which happens inside the span, it is being like recovered.
But we are still like we panicking like we were throwing it
like, this is answering your questions question, and we are adding this kind of, and we are recording just it as an as an event. Because I think this is what the semantic convention, basically in specification currently says that when there is an unhanded exception it needs to be set as an event.
So I not change the okay. Yes.
**Liudmila Molkova** 41:17 So the recovery. It's some goal mechanism. If you have an unhandled exception, you call it. There is some callback that maybe user code provides.
and if it recovers, then you don't set it as an error at all.
**Robert Pająk** 41:32 Exactly, exactly.
**Liudmila Molkova** 41:34 I see.
**Robert Pająk** 41:35 I think what we are
missing here is that we are not setting the span as error, because it was not mentioned anywhere in the spec and semantic conventions for exceptions. So I will basically just probably make a semantic convention change just to make it clear.
And the other thing is that when we have errors.
then we do not apply this exception types, exception messages. I just propose to set the error type error message
and set this the span status to error.
Not even want to call the record error the record exception. And we do not want to add events.
**Liudmila Molkova** 42:20 Yeah.
**Robert Pająk** 42:22 Okay.
So it seems that we are in line right?
**Liudmila Molkova** 42:28 Yeah. And it should all already be in the semantic conventions in the Dog Trust was showing.
**Robert Pająk** 42:34 Yes, yes, that's how I understand it as well.
Don't.
**Trask Stalnaker** 42:38 It is adding exception, type and exception. Message to the span itself.
**Robert Pająk** 42:46 No!
This only adds it to the event.
**Trask Stalnaker** 42:52 Okay.
**Robert Pająk** 42:55 Is it correct or not?
**Trask Stalnaker** 42:57 Yeah, yeah, yeah. I'm just bad at reading. Go.
**Robert Pająk** 43:02 No, no, it's fine!
**Liudmila Molkova** 43:04 The the. By the way, there is no spec that says how to populate exception. Oh, no, there is.
There is one for go sorry.
**Robert Pająk** 43:17 All right.
**Liudmila Molkova** 43:20 Sorry, Nicole. We took a long, round trip from the overview of what we are working on.
**Nicole van der Hoeven** 43:26 That's okay. I'm here to lurk. I'm lurking.
**Liudmila Molkova** 43:32 So essentially, we try to get through all of this uncertainties and what to record on the logs, how to record these things. So far it's been heavy on the errors. And there are some use cases we see, let's say, in Gen. AI or in in the in the browser, instrumentation and client instrumentation and things that are not spent right or metrics.
And we're kind of. We've been through a lot of discussions on what is that that we often want to report as logs in
open telemetry and what we would recommend instrumentation libraries.
I personally think we maybe lack some
application side perspective. On what? How would people do? Login with up and telemetry? What they would do with it?
That that's my personal opinion.
**Trask Stalnaker** 44:41 Anything else. We've got quite a kind of decent backlog.
Sorry?
Oh, the filtering and sampling stuff, Robert. I'm gonna
be looking at in July for Java. So
we'll have some, I'm sure. More discussions then.
**Liudmila Molkova** 45:18 Will you do? A threshold based filtering.
**Trask Stalnaker** 45:23 Trace based and threshold based.
Yeah, are the 2 things that are important for us.
But mostly, I mean, we can do in in a distro you can do threshold based
of in an exporter.
But the trace based.
Guess you could kind of do.
Yeah. But anyway, efficiently, yeah, so yeah, those are the 2 that
I'll be looking at.
**Liudmila Molkova** 46:03 Oh!
**Trask Stalnaker** 46:09 Alright anything anybody else like wants to chat about today. Otherwise we could, and barely.
**Robert Pająk** 46:23 I'll just send it to the
to the agenda. Just the reasons why we ended up with the log processor design
just in a sec. I think it was described here.
Something.
I think here were the.
I think. I think I pointed out some decisions and reasons here
which may be helpful for you.
**Trask Stalnaker** 47:07 Yeah, yeah, I will start with this design. I will attempt to implement it as spect in Java.
And see how I bring feedback.
**Robert Pająk** 47:21 Sure.
**Trask Stalnaker** 47:28 Cool, all right.
Well, nice to meet you, Nicole.
**Nicole van der Hoeven** 47:33 Yeah, nice to meet you. Also.
**Trask Stalnaker** 47:34 You all. I'll be out.
**Nicole van der Hoeven** 47:35 Explaining things to me.
Yeah. Well.
**Trask Stalnaker** 47:38 We'll see you all the week after next.
**Nicole van der Hoeven** 47:42 Alright! See you.
**Liudmila Molkova** 47:43 See you.
