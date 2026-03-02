SIG: Event WG
Date: 2026-01-27
Duration: 60 minutes
Zoom Recording URL: https://zoom.us/rec/share/0ZoIkKPAZPhChRwWR7JtPop9_y3hO3T5mUVk2JHCdNYdib8VKXr-iMywuYHJbE-c.BDSMgijC9cezs6Kq
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:03:30 Hello! Hi, Robert.
Pellared 00:03:31 Hello, how are you?
Liudmila Molkova 00:03:33 I am good. How are you? I'm sorry for being late.
Pellared 00:03:37 No, it's fine.
Not sure if Frasco's today, so probably he will be also here.
Liudmila Molkova 00:03:43 Yeah, let's ping him. I have a call right before this one, and I… Usually, I'm exhausted after.
Pellared 00:03:59 We can wait a few minutes, if we need to.
Liudmila Molkova 00:04:01 It's very cool.
Pellared 00:04:02 Your cup of tea.
Liudmila Molkova 00:04:05 Oh, Trasko's here.
Pellared 00:04:07 Yeah.
Liudmila Molkova 00:04:07 Awesome.
Pellared 00:04:11 Hey.
Trask Stalnaker 00:04:12 Sorry.
Pellared 00:04:13 Secondly do.
Trask Stalnaker 00:04:14 to reviewing something.
Oh, can you hear me now?
Pellared 00:04:18 Yes, we can't hear it all the time.
Trask Stalnaker 00:04:22 Okay, a…
Liudmila Molkova 00:04:32 Okay.
Trask Stalnaker 00:04:34 I had homework to do for this meeting that I did not do.
Liudmila Molkova 00:04:38 That's fine, we can use this time to do the homework. Maybe we can talk about, the pressing topics first, and leave the roadmap to be second?
Maybe they are related somewhat.
This friend… I think I approved it, under the assumption that we can polish it along with… other details.
Pellared 00:05:09 I totally agree with it.
Liudmila Molkova 00:05:14 Trask, should we give you some time to catch up, or…
Pellared 00:05:19 I only.
Trask Stalnaker 00:05:19 Yeah.
Pellared 00:05:20 The question regarding a comment from Tomo or Tommaso, I don't remember. I'm not sure if I need to do anything. Yeah, Tom, some…
I'm not sure if I should do anything with it.
Liudmila Molkova 00:05:34 So, let's see… So what is… he's concerned about is some technical details that, are
important in my view. So, like, what I was concerned about, this is… This is an event?
It's an event that's a slog-based event, we don't define events.
Span events and semantic conventions, and we're deprecating it But… we might…
Still use it if we decide that this is the name we want to give to unknown.
arbitrary exceptions.
What he's concerned about is that
The way, like, the schema, the way we define the attribute group for the new thing might not work in the future, it will work.
It's not a problem.
Pellared 00:06:33 Okay.
Do you want to write a commander? So just, he at least… Does not feel ignored?
Liudmila Molkova 00:06:43 I mean, I already have ignored you, resolved my concern. I…
So, once we decide how to name the arbitrary events, and if named them at all, we can undeprecate it, I think.
Pellared 00:07:01 Okay.
Liudmila Molkova 00:07:03 We don't need to deprecate it right away, but then it's…
Pellared 00:07:08 So what's your preference? Not deprecate it, or just leave it as it is right now?
Liudmila Molkova 00:07:13 I think this belongs in my PR, like, the one that talks about naming. If we agree on the naming.
Pellared 00:07:21 That it should be exception, we will just keep it as is. If we decide on something else, we will deprecate it there.
Okay, so I can undeprecate it if you want.
So I should revert these changes, right?
Liudmila Molkova 00:07:39 Yeah, just this small thing, so let me… Yeah, you can write it.
Yes.
Pellared 00:07:45 Mmm… Yay.
Liudmila Molkova 00:08:24 Right.
So we will still deprecate the document.
But won't deprecate the event yet.
Pellared 00:08:36 Okay.
So, line number 7 and 8 will persist, but 27 will be reverted when I change the young file, right?
Liudmila Molkova 00:08:49 Right, yeah.
Pellared 00:08:50 Okay, hi. Little zoos for me.
Liudmila Molkova 00:08:56 And then… There'll be… Just a deprecation here.
And the key part will be recording exceptions.
Pellared 00:09:11 That's good.
Trask Stalnaker 00:09:31 I left one small comment.
Liudmila Molkova 00:09:43 Cool.
Do you want to discuss it, or…
Trask Stalnaker 00:09:52 No, Robert, if you just want to refresh, and I think it's…
I don't think it's… it's just a wording.
Pellared 00:10:03 I'm not sure if it's just the wording, that's the problem.
Trask Stalnaker 00:10:06 Okay.
Then we saw…
Pellared 00:10:09 Even in the example, We have one example, and it was even before, when there is an exception.
Which doesn't… but the operation has not failed. This something like resource already exists.
Which is, yeah, which is in the cold.
From as an exception, like, you know, for example, you know, resource exists, exception, or something like that.
And yeah, question if you want to…
And the proposal here is to add, just, you know, add a log, a worn event, or I don't think of it right now. No, warn was something else. There, I think, would debug.
I just want to remember. Yeah, debug.
Line 1… 114.
This is an example.
114.
Liudmila Molkova 00:11:04 011 for sure.
Pellared 00:11:06 So this is an example. When the operation has not failed.
according to maybe the definition of a failed operation.
We are questioning is the failure of oper… I think there is some notion that operation failed, and we set the span to our… yeah.
That's.
Trask Stalnaker 00:11:24 Fine, we can… we can find a way in between the… the thing that I, was worried about the current wording is it sounds like… makes it sound like instrumentation should catch all… like, if I'm instrumenting, spring.
that I should catch all exceptions that spring throws.
Liudmila Molkova 00:11:48 Shouldn't?
Trask Stalnaker 00:11:49 As a lock.
Liudmila Molkova 00:11:51 Oh.
Trask Stalnaker 00:11:52 Only on my… I mean, only in the context of my… operation that I'm…
I don't know, like, I don't want people to be putting…
Like, I've seen in the past, like, Java agents instrumenting the exception constructor, and basically capturing every exception that is grown, even though a lot of them are
You know, number format exception that's… Cop.
locally.
Liudmila Molkova 00:12:41 Such a can of worms.
Trask Stalnaker 00:12:43 Yeah.
Pellared 00:12:44 Yes. Yes, I had the same concern. The only… Yeah.
Liudmila Molkova 00:12:53 So, Albert, your concern is in my 2 is fail, so there's an exception, right?
And to ask your concern is that we shouldn't have arbitrary exceptions logged.
Trask Stalnaker 00:13:15 Yeah, let's look at that, your example, are you… You are catching… What is the debug example?
Is that exception bubbling up to, sort of, the operation?
Pellared 00:13:32 Yes, it is.
Liudmila Molkova 00:13:34 But the debug example is not bubbling up, it's handled.
Pellared 00:13:37 You're right, it's return false.
You're correct.
Liudmila Molkova 00:13:42 The worn one is bubbling.
Trask Stalnaker 00:13:45 Oh, yes, this is native instrumentation, right?
Liudmila Molkova 00:13:48 Yeah, so maybe, like, the confusion we have is here. This example talks about native instrumentation more, and what Trask, you want to see is, like, more guidance for the instrumentation.
Pellared 00:14:03 I agree with Trask, I have the same problem when I was reading this and even discussing it, that probably we may even need
Separate recommendations, depending if it's native instrumentation, like business instrumentation, or with instrumenting a separate library, when people can then catch their error, you know, also, yeah.
Trask Stalnaker 00:14:26 Even for native instrumentation, there's some kind of threshold, right? Like… My number format exception that I catch…
is… expected, or… expect, like, that would be very noisy, like, I never log.
I'm not gonna log that at debug level.
Liudmila Molkova 00:14:57 Okay, so… what are you… Wanna say that… First, apply judgment.
If… if it's… if it's… deserves… If it's… meaningful.
Trask Stalnaker 00:15:19 Should consider recording this exception as a log record.
Liudmila Molkova 00:15:33 Shitcut.
Pellared 00:15:34 Not a meaningful exception.
Liudmila Molkova 00:15:38 Zero's an exception, interesting.
Trask Stalnaker 00:15:41 From obserability to 10 points. Right, right.
Pellared 00:15:48 once I was reading, A blog post.
By a guy who is known in group observability, and he was saying, like, the record only locks.
Which you can take action on.
Liudmila Molkova 00:16:06 If only you knew.
Pellared 00:16:08 Yes.
Very upset, but he means that if there's something that…
It's non-actionable anyway, in his opinion, it's a trash look.
Liudmila Molkova 00:16:18 I mean, number format exception is actionable. Somebody's giving you the wrong number.
Depends.
Trask Stalnaker 00:16:25 Can we…
Liudmila Molkova 00:16:27 Yeah, if we break it down, and let's say, so what we… When people should…
When you are risk… okay, you are risk-rawing exception?
And… you don't… You think it's not logged before?
Trask Stalnaker 00:16:48 Yeah, so that's the original wording, right? When an instrumented operation fails.
With an exception.
Liudmila Molkova 00:16:56 I see.
I see. So, the one… I think I suggested this to change this to instrumented code.
Ciro's an exception, because… It's… when we talk about spans or metrics, we talk about operations, usually.
or at the span. So when we talk about logs, it stops being, like, operation, right? There are…
Trask Stalnaker 00:17:22 Right.
Pellared 00:17:23 Yeah.
Trask Stalnaker 00:17:24 It can be an event, something coming from outside.
Pellared 00:17:27 Reacting just…
Liudmila Molkova 00:17:30 But maybe it's… it's too picky. I think it's still understandable that when instrumented operation
But, like, if we keep the original form, it does not prevent
Somebody from also recording some other exceptions.
It's like, if we just return it back, I wouldn't mind.
Pellared 00:17:54 Could you find the comment when you do me or you proposed, just to double-check if I had the same wording or some other…
Loads. I think you need to load,
There was something in below… below…
Liudmila Molkova 00:18:09 Yeah.
Pellared 00:18:10 I think it was somewhere here.
Liudmila Molkova 00:18:25 Huh?
You… Didn't change this, I did…
Pellared 00:18:33 I think it was next one. I think you put… you may have put several comments from the same line.
He's here.
throws an excession.
Trask Stalnaker 00:18:45 Yes, yes.
Liudmila Molkova 00:18:48 Oh, Serral's an exception, right. So we decouple failure. I like it.
Trask Stalnaker 00:19:10 What do you like?
Liudmila Molkova 00:19:12 The then-instrumented operations arose an exception.
So, it used to be FAILS with an exception.
Which, remember, we don't, like, our failure criteria.
is context dependent?
Pellared 00:19:36 But I think now Trasp wanted to have failed back, failed back.
Trask Stalnaker 00:19:40 Instrumented operation… no, instrumented code… instrumented code… froze… an exception.
So that means…
Liudmila Molkova 00:19:57 Yeah, I mean…
If… if we return back to this. This is what we currently have, that's what you don't like.
Trask Stalnaker 00:20:04 Yeah. And I understand why.
Oh, I see, operation.
Got it.
When an instrumented operation throws an exception, yes, that worked.
for me.
Liudmila Molkova 00:20:26 this one.
Trask Stalnaker 00:20:27 Yep.
Pellared 00:20:28 What's the difference?
Trask Stalnaker 00:20:30 To me, it's, like, more coarse-grained. Like, an instrumented operation is an operation that I care about, that I've instrumented.
Whereas instrumented code feels to me like… any…
Pellared 00:20:48 code under instrumentation.
Trask Stalnaker 00:20:55 Yes.
Pellared 00:20:58 It was, would you like to change shoes to May?
So that people really think when they do it. Because Schultz, you know, kind of encourages.
Creating locks for all exceptions, whereas may say, oh, you can do it.
I thought it's very nitpicky.
Trask Stalnaker 00:21:22 I mean, on Span, are we…
I would be good with that if we have… For spans, right, we want… Should.
Pellared 00:21:38 Yes.
I think it's already there for spans. I think…
Liudmila Molkova 00:21:43 No!
Pellared 00:21:45 I think we have something for Spencer Shield.
Liudmila Molkova 00:21:48 I mean, we were saying that…
Pellared 00:21:50 set span status to error, error type attribute should set span status description. This is should always.
Liudmila Molkova 00:21:59 We could say that if you… if the… Pan and Vision Exception.
Done.
Also, you should record it as a log.
And it would apply to, like, our instrumentations. Whatever instrumentations. And then this, we could use May.
Trask Stalnaker 00:22:30 I like that.
Liudmila Molkova 00:22:56 Oh, okay, sorry.
Good.
Pellared 00:23:33 Yes.
If I remember correctly, David Ashpoch had the same proposal.
Liudmila Molkova 00:23:46 Awesome. None… we're getting there.
Let's move on.
Trask Stalnaker 00:23:58 Yeah.
Liudmila Molkova 00:24:01 Related… I, I think we should also talk about, this, this friend.
I don't know if we're ready to make any calls, but I think we need to make progress.
And I also didn't do the homework. So I think the concern now is…
We will record exceptions on logs.
the Aurora… The key question is probably…
How we should name this event, and should we name it at all?
And… do we have notes… Yeah.
Still a bit of guides from the last time.
So the… there are 3 options on the table, I think. Option 1.
It's a log record.
In.
generic use.
Option 2… It's generic exception.
Option 3… It's specific to…
What's failed.
Http server…
an option… 3… 2.5.
It's probably…
So I think the option one we don't like, because we want to emit good events.
The one that follows some conference best practices.
Yeah, Robert, go ahead.
Pellared 00:26:34 My preference is option 3, 4,
Since a month, at least, or even more.
HTTP server, yeah.
Liudmila Molkova 00:26:46 What did you say after?
Pellared 00:26:47 operations, And what failed?
Because then it looks a little bit like… the use case is also different. Sometimes you can have, like, event-based, some, you know, for example, you have some, I don't know, eventing library, or whatever, some… something which…
which basically reacts, I think there's one go library, which can sometimes just drop things like logs or events, that something is going on Kafka in the background, which just notifies, oh, something is going on with Kafka, just, you know, asynchronously.
And then I would prefer to have an event for basically, you know, I don't know, some configuration error, I don't know, configuration exception, etc.
Liudmila Molkova 00:27:36 I think…
I also like this, and I also like the beauty of option 2.5, because you don't need to
choose. You can say it's exception.http.server, where there is some
Specific format to this, so that you can still group them, and… No.
Something else about this event.
Pellared 00:28:09 I have no pro- it's… I have no preference here.
it can start with exception, it can end with exception, I have no…
I would say even though experience here was better, so…
Trask Stalnaker 00:28:23 So, let's think about the, grouping, the kind of filtering… K, like, I guess…
We were thinking routing, like, if you wanted to route or apply something to all exceptions.
I mean, you certainly can look at attributes and look for exception.
Message on the attribute already.
The benefit of it being on event name is that You don't have to crack the attributes open.
But I'm not really sure that…
That's a super common use case.
So, want to filter all your exceptions?
separately, somehow. I feel like the severity level is…
the most important…
Liudmila Molkova 00:29:30 So, in my…
I've done a little bit of research on Sentry, not in the context of this, but recently, and their business model is built on separating exceptions. The exception
And everloke are two different beasts.
And for exceptions, you apply all this additional logic, you fingerprint them.
you have a special view as your monitor separates exceptions from everything else. So I think there is a use case of routing exceptions separately.
It's a good question, like, would somebody care about exception on the debug log? Probably not.
Like, unless you are debugging.
Trask Stalnaker 00:30:21 Makes sense.
Liudmila Molkova 00:30:28 My broad thoughts is that
In the perfect future.
I think these events should have good names, and they should have additional attributes beyond exceptions.
So regardless.
Trask Stalnaker 00:30:50 Yeah, I like…
Liudmila Molkova 00:30:50 Thank you.
Trask Stalnaker 00:30:52 Yeah, I like option 3, like, in terms of also the,
having a name that, like… and if I have a particular noisy one, then I can filter that.
Out, if they have different names, whereas if… They're all named Exception.
That's… Harder.
Liudmila Molkova 00:31:17 Yeah.
Trask Stalnaker 00:31:18 I'm trying to think if the, yeah, if it's worth the prefix or suffix… And…
Making that into a rule, or not.
Liudmila Molkova 00:31:33 Yeah, and also, like, we are… not…
This is the future. I hope we can make some progress before we introduce
some of this. This should be conventional. There should be conventions for them.
Okay, and… This… this originates from what do we do in…
let's say Java instrumentation today to replace record exception call.
Right? And I think the… the… Choice… The choice is…
Like, what we can do now is either option 1 or option 2.
And this is the future.
Trask Stalnaker 00:32:25 I mean, option 3… I was imagining, dot.
I was imagining option 3 in Java,
But with something fairly generic, like httpserver.server.exception.
Right? Like, we have that much context, we know… Or http.client.exception, or… Rpc.server.exception.
Liudmila Molkova 00:33:01 Okay, so we would… Add this event.
to semantic conventions.
And move it.
stabilize.
Damn.
So you can go stable in instrumentations.
But… I don't.
Trask Stalnaker 00:33:21 I think we need… yeah, I don't… I… we can… go stable.
Liudmila Molkova 00:33:27 Right.
Trask Stalnaker 00:33:28 Major version bumps.
And I'm not sure, like…
In, like, for native instrumentation, might be able to provide more specific event names, like…
this HTTP client exception instead of that, like, DNS… resolution exception.
Liudmila Molkova 00:33:54 Or…
Trask Stalnaker 00:33:56 Socket terminated exception.
Liudmila Molkova 00:34:05 Okay, this is another can of worms at which granularity.
Trask Stalnaker 00:34:10 Yeah.
I think it's night, like… I think that more granularity can be…
Can be nice.
Liudmila Molkova 00:34:33 And can be bad.
Yeah. So if connection dropped, who cares? Like, first thing, you care that it's dropped. Second, you cares, you care why.
Both need to be recorded somehow.
Trask Stalnaker 00:34:48 And they both kinda are. I mean, we have the error type.
Should be on that exception message.
Liudmila Molkova 00:34:56 The error type is… Why? The socket…
I don't know, connection reset by peer, is there a type?
That the fact that connection dropped.
is, there's a what?
Error type is Y.
Trask Stalnaker 00:35:17 Oh, I see.
Liudmila Molkova 00:35:20 At least it's my mental model.
Like, you can build the metric.
With our type from the slogs.
And the event name becomes the metric name.
Trask Stalnaker 00:35:37 I like that.
That's nice.
So that… that would be argument in favor of it being… generic-ish, not… So, one… one…
Event name recommendation for a given semantic convention.
Operation.
Liudmila Molkova 00:36:07 Yeah.
Yeah.
And it's like, we want this event name to be… used across languages consistently. Otherwise.
It's better not to set any or just call it exception.
Trask Stalnaker 00:36:24 Yeah, that's a good point. Like, we don't want proliferation of
Like, lots and lots of event names.
Liudmila Molkova 00:36:41 And in this sense,
We can define the event.
We probably would keep it in development, because of just the discussions we had. It's probably worth testing it in the community.
And… then Java can go stable without it.
The…
Trask Stalnaker 00:37:10 Yeah, we can prototype it, basically use it, yeah.
Liudmila Molkova 00:37:14 Yeah, the alternative is… It's like, e… the option… like, the reason I like option one, I actually like…
Because it's… it's extensible, it's future-proof. You can do this today, And…
You can evolve it in the future.
However, whatever we would define in the events, we can still accommodate it with this approach.
Trask Stalnaker 00:37:47 Yeah, I mean, maybe that's the fallback if there isn't a specific semantic convention for it.
Liudmila Molkova 00:38:03 Okay.
Trask Stalnaker 00:38:06 The other option is… The option 2 as the fallback.
Liudmila Molkova 00:38:13 I think… The option to, like, it's not future-proof, right?
Because there is an event name.
But it does not give anything important, because you can already figure out it's an exception based on the attributes.
Like, it's the worst of them all in my mental model.
Trask Stalnaker 00:38:34 Okay.
Pellared 00:38:35 A crew is like… it's like a lock, basically.
It's just the nose.
Most probably.
Trask Stalnaker 00:38:46 Yeah, I think that aligns with… semantic conventions…
And with the… I mean, with the idea that event name is for semantically meaningful
Events that we've defined.
Not the trash bag.
And people could choose to give their… some… their own semantically meaningful event names.
To exceptions, if they want.
I mean, that's just extending… that's just doing their own semantic conventions.
Liudmila Molkova 00:39:45 You can even do this in the processor, if you, like, want the… Exception type to be.
Event name, you… you can do this.
Trask Stalnaker 00:39:56 Yeah.
But for open telemetry instrumentations, we would…
We generally… we would try to only…
Use event names that are defined in semantic conventions.
Liudmila Molkova 00:40:13 Okay.
Cool. So then, My PR… is…
Not… I will not be in APR. I think we need a prototype for this.
as well.
And I'll work on this. I think there is this other part of the severity considerations. Let's get to it next time. I think this… let's solve them one by one.
Maybe even break down the PR into separate parts, or… I don't know.
Oh, right. For the prototype, we will also need to figure out the severity, but then…
We'll talk to it then, it's an easier conversation.
Trask Stalnaker 00:41:01 Can we send already a…
like, I like option 3. Could we send a PR that just starts adding those events.
without… Doing the general…
Liudmila Molkova 00:41:30 Oh, I see where you're going to. Like, we have specific instrumentations.
the principal… Is… orthogonal to… well, not orthogonal, but we can provide practical guidance.
Trask Stalnaker 00:41:44 up.
Yeah, every… update HTTP, add the events to HTTP, database, RPC,
get by.
Liudmila Molkova 00:41:58 And could…
Trask Stalnaker 00:41:59 Fair.
Liudmila Molkova 00:42:01 Right.
I can send one for HTTP…
The questions will get immediately, and I'm already asking the… than myself.
Would we add any attributes?
And I, I kinda wanna say…
Yes, but not now. We will add them.
We will start with just the replacement.
And we will grow in this.
Trask Stalnaker 00:42:45 Do we want to start with error.type?
Liudmila Molkova 00:42:49 Yeah.
Sounds good.
Trask Stalnaker 00:43:20 Yeah.
Yeah, I will… Just a thought?
Pellared 00:43:23 I think there was some library, I don't know if it was in Python or somewhere, which treated stat… which basically was…
putting exceptions for, I don't know, like, for… when, for example, HTTP kind was 404, so then I think the status code could be, for instance, an attribute in such case.
Not sure if we want to have it in DPR or not.
Liudmila Molkova 00:43:51 So we would have… some…
Language saying that the error type should be populated consistently across spans and metrics and blogs?
And on spans, it could be 404. So it can be 404 on logs, but we wouldn't populate the status code.
At least yet.
It's like, okay, it's an exception. So you can have 404 without exception or with exception. We only record exceptions.
Pellared 00:44:25 Okay, cool.
Liudmila Molkova 00:44:29 So for 404 with exception, we will record this, along with our type, as a span, and we will record exception as log record.
Pellared 00:44:42 Okay?
Liudmila Molkova 00:44:42 with error type, but not… no HTTP.
Attributes, for now.
Pellared 00:44:49 Okay.
Liudmila Molkova 00:44:57 Oh my gosh, I see… like, no, no.
Oh, shut up.
Trask Stalnaker 00:45:09 Yeah, I think there's some leeway that instrumentations have there, like, if it's… If… an HTTP client library.
Happens to use exceptions to communicate, like, that it was a 404.
Like, you don't… I don't think you have to capture… The exception?
But I will say, I mean, in Java, we do.
If it's an exception, we capture it and… stamp it.
Liudmila Molkova 00:45:57 I had a sentence somewhere…
It's probably, if we need to talk about it, we should do it in the Roberts PR, in this Should and May section… sections.
And… Oh, for the…
Trask Stalnaker 00:46:19 span section, yeah.
Liudmila Molkova 00:46:32 So I think we, polished it a little bit on the… That RTAP.
Trask Stalnaker 00:47:00 Yeah.
Liudmila Molkova 00:47:08 Oh, this talks about the severity.
Not about hands.
I mean, I can… I think we can document it, but… like…
Everything we would document would have should.
annually.
Trask Stalnaker 00:47:45 Yeah, I mean, I like the… this note on mine… 140.
I mean, as a… kind of general… .
Liudmila Molkova 00:48:33 Okay, we have 10 minutes left.
And I think we know the next steps. We'll try with this…
And eventually, we'll see where we go.
So… What should we stabilize, right? I think this is the main question.
Trask Stalnaker 00:48:53 Everything!
Liudmila Molkova 00:48:55 Right there.
Trask Stalnaker 00:48:57 Ugh.
yeah.
Including, I would say, I mean, we need transitions.
Pellared 00:49:15 For recording… for the recording errors, I was thinking about
Starting… stabilizing it for spans and metrics first.
These parts, and have it as mixed.
And then follow with the next steps, but I want to hear your opinion, what do you think about it?
Liudmila Molkova 00:49:38 I like this idea. I think this is what we already have done on spans and metrics, and it would be a trivial.
Change, I feel.
What do you think, Trask?
Trask Stalnaker 00:49:54 So, Defiant, this would be recording… Yeah. Doing that?
What does… what does metrics… what do we say about metrics?
Oh, just the arrow.type. Okay, and spans, we say…
error type. Are we including… we're going to include now about, stamping a log?
For exceptions here in this section.
Liudmila Molkova 00:50:28 Maybe we will keep this, but we can't keep that part as…
In development of the first step.
Trask Stalnaker 00:50:38 I thought on Robert's PR that we were.
Liudmila Molkova 00:50:40 We're looking.
Trask Stalnaker 00:50:40 Matt, earlier, we were saying that
It would be nice here to have a should… Capture exceptions as… On… when a operation…
Causes… an exception is thrown that fails a…
Operation, span operation, something like that.
Liudmila Molkova 00:51:12 And you're…
if I understand, you're suggesting to kind of keep that a couple of sentences, the new one.
And probably this one in development.
Trask Stalnaker 00:51:28 So this… so error… recording errors on spins, I mean, this is effectively… Oops.
Kind of effectively stable already, since we… Implement it…
We use this on HTTP and database SEMCONG.
Pellared 00:51:48 I was muted. I think that even stabilizing it is not a problem, because it's not a normative language, it's just, look at this other part, it's like a note list, I would say.
That's… it's just my opinion.
The most important part are the things which are capitalized here, about error types, spend, status definition, etc.
Trask Stalnaker 00:52:20 Yeah, I agree that these…
Pellared 00:52:25 remember how I transited my PR. I think I made some simple changes in this, but I don't remember right now.
Liudmila Molkova 00:52:33 I think you reverted them, but anyway…
Okay, so it sounds like it's a good candidate, like, this… the sections are de facto stable. We can, yeah, make…
Pellared 00:52:51 You're right.
Are you revert? We can make it official.
Liudmila Molkova 00:52:55 I'd like us to…
commit to stabilizing the whole document in 2026, I think we can try at least getting there.
Pellared 00:53:07 And I think in order to have it stable, we also need to stabilize the logs and events anyway.
Or at least events.
Trask Stalnaker 00:53:18 What about events?
Do you consider not stable?
Liudmila Molkova 00:53:27 Let's see…
So most of this dock, it's actually a spec.
Just reiterating this.
pack, and there are a few opinions, right?
That we…
Wait.
I'm… I'm super scared.
Trask Stalnaker 00:54:07 He's like this.
Liudmila Molkova 00:54:08 It's your fourth!
Yeah.
This is the opinion.
Of the semantic conventions.
Pellared 00:54:23 The rest is just spec.
Liudmila Molkova 00:54:37 I… I would… like, so I think the only controvers… slightly controversial part is this one, more like…
Are we sure?
Like, because…
let's say somebody comes and says, okay, I am emitting this log record, and this log record can go to standard output for my CLI, too.
And I want to have a human-readable message there. Why wouldn't I put it in the body? And we'll say, of course you should. I think CJ raised this concern before.
Trask Stalnaker 00:55:12 Right.
Yeah, maybe we should just, we could probably change that line to be, like, Should not use body…
Instead, for structured attributes in… Something like that.
Instead of… In lieu of using attributes.
Liudmila Molkova 00:55:43 Type… Maybe events may use body, but only to capture human-readable representation of
Details available in a structured form.
On attributes, and event name.
Pellared 00:56:09 How a structured body is more readable than attributes? I don't understand this thing.
Liudmila Molkova 00:56:16 Now, more like I have, full bar as attribute.
And then… I can have a body that says that event happened and foo was a crowbar.
But it will be available on attributes.
Do you see what I mean?
Pellared 00:56:44 I think I do, but yeah, I think that…
for me, it will be the same readable if I just have bar attributes, and just have a message attribute.
Which says, you know, something happened.
I do not see the difference in reading two attributes.
Compared to one body which contains the same.
Basically.
Trask Stalnaker 00:57:15 I think the difference is whether we have, like, a common attribute, decide on, like, say, event.
display… As a common attribute that people can know as a human-readable form.
so that…
Pellared 00:57:37 than soon.
Trask Stalnaker 00:57:38 in there.
Pellared 00:57:38 Should it be also…
If it's human rebuild, shouldn't it be also a string, instead of, you know, body structure, so it can be a payload?
Liudmila Molkova 00:57:49 I… I think it's… it's common
In current world, that body is the human-readable string.
Right, and a lot of tools show you just the message and don't show you even the context.
And, like, if somebody's forwarding quartile to console, to a simple formatter of some sort.
Then they would print the body only.
And this is, like, the choice of the consumer. And it's already a convention, we don't need to invent an attribute for this, because it will happen if we just leverage.
Bloody.
Trask Stalnaker 00:58:33 It's sort of, like, embracing the, like, a sort of, like.
Pellared 00:58:36 Yes.
Trask Stalnaker 00:58:37 Backwards compatible with… Odd.
Old-style logging.
Pellared 00:58:43 Yeah, exactly. It's what Bidgers do, right? Because Bidgers are usually using body for the log message.
Trask Stalnaker 00:58:54 I didn't hear that word.
Yeah.
Pellared 00:58:56 I wanted to say that the log bridges, at least in Go, all of them are using body, yeah, log bridges or appenders are using the body for the string message, basically. So I think we may put something like the body can be used as a human-readable message.
For the event.
Liudmila Molkova 00:59:17 Yeah.
We are out of time. I… what I'll try to do, I'll try to find the issues. We have quite a few issues around this. Some of them are closed. There is an issue on the body.
And, we're… Probably can resolve them in some simple way.
Pellared 00:59:42 I tried to create a PR for you just after this meeting, because I think it will be…
Just to keep the momentum. It should be simple.
Liudmila Molkova 00:59:51 Awesome.
Cool, love it. Let's target destabilizing everything, but let's see how far we go.
Yeah.
Trask Stalnaker 01:00:00 Still early in the year. Yes.
Liudmila Molkova 01:00:02 Yeah.
Trask Stalnaker 01:00:03 Bye.
Liudmila Molkova 01:00:04 Thank you.
Pellared 01:00:05 Bye.
