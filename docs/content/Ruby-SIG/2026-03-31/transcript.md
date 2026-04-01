SIG: Ruby SIG
Date: 2026-03-31
Duration: 45 minutes
============================================================

## Zoom Recording Transcript

**Hannah Ramadan** 04:12 Hey, Sean, how's it going?
**Xuan Cao** 04:18 Did we expect anyone to show up?
**Hannah Ramadan** 04:22 Sorry for being a bit late. Has anyone else came by?
**Xuan Cao** 04:27 Oh, I think Daniel, was here, and then I think he also thinks nobody will be here, so I should just be his fans.
**Hannah Ramadan** 04:35 Oh.
Looks like Arielle maybe also is here for a second. He posted in the Ruby Sig Slack channel. I just messaged him that we're here.
**Xuan Cao** 05:11 Okay.
**Hannah Ramadan** 06:18 Well, I can, share my screen.
I have to leave at 10.30, so maybe we can just… well… Do you have anything that you wanted to go over today, Shawn?
**Xuan Cao** 06:30 No, no, not for my side.
**Hannah Ramadan** 06:32 Okay, cool.
I do have one PR that, I… I'm working on… it's migrating to the stable semantic conventions. There's some open questions around, like, what the span should be named, as well as how to handle exceptions.
Maybe I'll just kind of put these conversations in… The doc and see if people can… Maybe jump in on it.
There's that thread?
There we go.
Okay.
Maybe take a quick look here.
This looks kind of interesting. Context scoped attributes.
Probably read about that later. Anything you want to dive into here, Sean?
**Xuan Cao** 09:03 can you just go up a little bit?
Oh, yeah. Nothing to share about, I just, wanted to point out this guy, he said that I made a PR for a suite implementation.
and nobody answered. It just… I think it's just funny, because I was also monitoring this information session, and this guy's, so desperate to make the move. And then he even made it to the Sikh meeting. Suspect SICK.
the complaint that nobody actually revealed is PR.
**Hannah Ramadan** 09:40 Oh, that's… that doesn't feel good.
**Xuan Cao** 09:44 you know.
Well, anyway, I just… I just didn't expect that he… make this matter into the spec scene.
image.
**Hannah Ramadan** 09:56 So…
**Xuan Cao** 09:57 I don't know how that is internal signals there.
**Hannah Ramadan** 10:00 Okay. Oh, there it is. Oh, enough.
Well, at least it was brought up in here, so hopefully somebody can jump in.
**Xuan Cao** 10:15 Well, I mean, in the case of this, TechSQ will have a lot of stuff, like, people expected some answers from the maintainers, but it didn't get anything.
Yes.
**Hannah Ramadan** 10:47 New issues, looks like… Was this last… oh, this was back in February, if anyone's looked at that.
And then dropping support for Ruby 3132, I think that is something.
I feel like I saw a PR up about that. Maybe from REO.
O.
Yusuf put it in.
I think that makes sense, I'm pretty sure… I can't remember, I feel like we typically stay matched to what Ruby supports, but I can't quite remember.
EL, yeah, probably.
Okay, Arielle, I feel like Arielle kinda looks at those.
**Xuan Cao** 11:37 Yeah, he has a PR for the country to, dropped the support plus 3.1.
**Hannah Ramadan** 11:43 Mmm. That's maybe where I saw that.
**Xuan Cao** 11:46 Got it.
**Hannah Ramadan** 11:48 Yeah, perfect.
Oh, Yusuf added that, yeah, yeah.
Alright, looks like that's… Pretty good. Okay.
Nice, okay, cool, nice, that looks great.
I guess we're on contrib… any new issues?
Hey, Ariel.
**Ariel @arielvalentin (ATX, USA)** 12:28 Sorry about that, y'all.
**Hannah Ramadan** 12:34 It is okay. I feel like when… when the calendar doesn't ring, no idea what's going on.
Well, we were just looking at contribib now, and I have to leave at 10.30, just… You know… Looks like we got a new bug.
**Ariel @arielvalentin (ATX, USA)** 12:55 Yeah, I think, schwan had engaged there, and… did somebody open a PR for this one already?
It might have been merged?
**Xuan Cao** 13:19 No, I don't think it's Pierre related to this one.
**Ariel @arielvalentin (ATX, USA)** 13:22 Oh, it's not? Oh, okay. Sorry, there's so many PRs going on.
**Hannah Ramadan** 13:25 There is.
**Xuan Cao** 13:29 Oh, oh, one thing about this one, So, as I said, S3 SDK node and Go use lowercase, but actually the S3 SDK Ruby still uses uppercase.
But I don't think that matters, since it's really just an SDK. But anyway, I think those… I think this is a case instance.
As is, described in some of the SDP.
**Ariel @arielvalentin (ATX, USA)** 13:57 Okay, so the propagator needs to be fixed. Now, is the… is the propagator for X-Ray in this repository?
**Xuan Cao** 14:05 Yeah, yeah.
**Ariel @arielvalentin (ATX, USA)** 14:07 Okay.
I felt like… oh, the other one was the Lambda one.
That's why. I'm getting confused, okay?
**Xuan Cao** 14:17 Oh, the Lambda line is, yeah, so that your input is, that's brilliant.
**Ariel @arielvalentin (ATX, USA)** 14:22 Yeah, yeah, yeah, sorry, I'm getting my PRs mixed up.
So no one opened up a PR for this one yet.
Okay.
Yeah, seems sensible.
**Hannah Ramadan** 14:48 Should we just need to go in and update the case?
**Ariel @arielvalentin (ATX, USA)** 14:52 Yeah, I think so.
I think… I think down casing should be in, like… Makes sense.
But the trace IDs are coming in over a rack, right?
They're either coming in over a rack, or they're being… So the inject and the… And rack3 is lowercasing everything now, right?
**Hannah Ramadan** 15:28 I'm not, I'm not sure, top of head.
**Ariel @arielvalentin (ATX, USA)** 15:30 Okay.
We just need to test some things.
**Hannah Ramadan** 15:40 Wow.
At least we have a simplified repro, that's always very helpful.
**Ariel @arielvalentin (ATX, USA)** 15:48 Yeah, okay, they're using gRPC to do this, and… Gotcha.
to the gRPC header is… oh, okay.
Yup, okay. Because that's inconsistent for GRPC headers must be lowercased.
Okay, yeah, yeah, now I'm starting to understand this, because I'm actually reading the issue.
Instead of guessing.
You there, Hannah?
**Hannah Ramadan** 16:30 Oh, yeah, yeah.
**Ariel @arielvalentin (ATX, USA)** 16:32 I don't have anything else to say about it.
Cool.
Yes, this is a valid bug.
**Hannah Ramadan** 16:42 Yeah, cool.
I'm in PR land, let's see… Thanks for looking at the Ruby 3.3.
Stuff I saw merging on April 1st, I believe?
**Ariel @arielvalentin (ATX, USA)** 17:17 Yeah, cause our last day is today.
Oh. Last day for support is today. 4-3-2.
**Hannah Ramadan** 17:24 Nice.
I have a couple draft semantic stuff, but waiting to open those officially until we have some things sorted out with names and handling exceptions.
Okay, does anyone want to talk about or look at any of these specifically?
**Ariel @arielvalentin (ATX, USA)** 17:56 Not yet.
I know that Juan has been waiting very patiently for that auto-instrumentation gem.
**Hannah Ramadan** 18:03 Mmm.
**Ariel @arielvalentin (ATX, USA)** 18:03 I think what's holding me back is time to test it out and try it.
I know that… Like, months was not an excuse for waiting to try it.
But I'm gonna see what I can do… Tonight.
See if I can do something.
for you there, Sean, to at least give it a dry run.
Let's see if it works for me, out of the box, essentially.
That's about it.
I was, like, putting together a PR using, like, a robot to get the clanker to, like.
Migrate to test doubles, and all it did was give me a system stack error.
So, it's just kind of sitting there.
And then James just has a lot of these, kind of, like, You know, CI… actions… mmm… Mess with this, mess with that stuff.
For… Improving performance of stuff there.
And, yeah, I don't have anything else to say, really.
**Hannah Ramadan** 19:21 Boom.
**Xuan Cao** 19:25 This, this fiber safe, context detachment? I think this kind of will be very interesting to look at.
**Ariel @arielvalentin (ATX, USA)** 19:34 Yeah, we have to have the person… we have to figure out what to do, because they generated the code with Claude.
And, we have to look at their EZCLA.
And see, again, kind of, what's up with the agreement on… Using AI to generate this code, and in particular.
The fact that there's, like, a missing co-authored?
Or something?
Or, like, the co-authored email hasn't been signed off on… I don't know exactly what the details are there, but it looks like Claude is the co-author, probably the lead author of this.
Hmm… And, as far as fiber safety is concerned, yeah, I mean, we don't have, like… I think one thing I… one thing I probably think we need is, like, some sort of code coverage, maybe, of some sort?
Let's look again at what this was. Like, the implementation, if y'all want to look at it.
So, in the implementation, now there's the context info. So, the rack request is fired.
And what it did before was rely on the implicit main fiber you know, it's attaching the… the rack context… Which… was pulled… It's attaching the rec context to… the current… Thread's main fiber attributes.
Oof! In the, sorry, in the… In the first one, in the attached context portion of it.
Like that, that first bit, yeah.
So Now it's saying, grab the current fiber, As opposed to… And it might be because this rack event is being executed in a fiber.
As opposed to being executed in a thread?
**Xuan Cao** 22:00 And so…
**Ariel @arielvalentin (ATX, USA)** 22:00 So… I don't understand how it is that… When it's… okay, so when it calls attach, it's attaching the context… the current fibers attribute.
Okay, that's happening on 65.
So now that it's on a fiber attribute.
The token and the span are getting passed in.
And the token just being an index value in the array.
Of… or the stack, or whatever, of the… Of the context objects.
And it's passing in the spam. So, when it goes to the… The detached context What's happening is that Because detached Context is getting called.
A separate fiber might be operating on it, a different fiber, so the state is incorrect?
So I think, I guess I don't understand exactly… the execution model of what's happening here, if I could understand it a little bit more. So let's see if we could share a whiteboard here. Do you mind if I share a whiteboard?
**Hannah Ramadan** 23:25 Yeah, please.
**Ariel @arielvalentin (ATX, USA)** 23:33 Doesn't allow me to share a whiteboard right now.
**Hannah Ramadan** 23:36 Stop sharing.
**Ariel @arielvalentin (ATX, USA)** 23:37 Yeah, yeah, yeah, no problem, no problem.
So, I don't know if this is a good way to do this.
I'm gonna try my best.
So… Let's see what I could do here.
If we have… Kind of, like, rack.
Rack running here… So RAC is, is, configured, or whatever, and then RAC has its, you know, its pipeline that it runs.
And one of the components in that pipeline is the event handler.
And the event handler has got… You know… little… little sub-components in it. In our case.
Because it could have one or many of these.
But, a handler's here, so this is a rack of vents.
middleware?
And that is gonna send those off to each one of the handlers.
Right, if it was iterating over them?
So, effectively… When a request is coming in… I'm sorry, I don't know, do I have a line here? I want to look like an arrow. When a request comes into rack.
When Rag is handling that request, let's say you're, you're in a model where it's a process.
Right?
So you have… One big old process here.
And inside of that process, You're gonna have a main thread.
Main thread that runs in here.
So this is gonna be your main, like, execution thread.
I don't know if I'm dr- if this, like, is helping.
But this is, like, the Unix process, or whatever.
And, you have the main thread here that's running.
And that main thread always has a implicit fiber in it. This is my understanding of how stuff is, somebody can correct me.
So, there's, like, a fiber that's running in here, inside of this thread.
Which is inside of this process.
Alright.
And, well, these labels are like… Bananas. Anyway… So all of this is happening, and when the thread is… whenever we add anything to, like, the OpenTelemetry context, it adds it to this fiber's variables here.
And a handler can come along, and it's like.
Oh, you know, when a request is started, call the handler.
When the request is ending, call the handler again.
And the handler is, the handler itself, it is reading and writing from this fiber right here.
Right?
So, the variable that exists… exists on this fiber.
So, it's like the on start, on end, that is… you're gonna get the attached, other words, the finish, or whatever? You're gonna get… when you create the… when you create the span, and create the context, it stores it on a variable here.
And what it does is that it gives back a token, which is like the placeholder.
Of where the context was.
Right?
So it's like, oh, it's the number 10. So that when it goes and detaches it.
It's gonna look for the 10th… Thing, whatever, and pop it out.
Of that context.
Now… If we have a situation where we have multiple fibers that are running.
They don't share their state, right? So, if you've got a separate fiber here, so let's say now that, instead of it being this model, we're gonna take this… let me… Let me ditch this whole, like, external process thing, it's, like, too much noise. Let's say we have a different model, the request is coming in.
And you have, like, a request fiber?
And then, like, a response fiber.
And one of these is handling the request part, and one of these is handling the response part.
And there's some sort of interaction that's supposed to be happening?
Well, what then appears to be happening is, or at least a report, is saying that When the request is started, And the event middleware calls our handler, our events handler, It is creating… A span and putting it on this… request here.
But then when it tries to… Finish the span and detach it?
Because it's on a completely different… Response.
Oh, I'm sorry, on a different fiber?
then the context is missing, causing an error, saying the context doesn't exist, it was probably already closed.
So I don't know if that is how this… Web server works, where it's like, you're getting a request in, that's handled in one fiber, something else happens, and then the response fibers spawn up.
And it's doing something.
Or, if it's, like, a fiber for per request or something like that.
Because I don't… it doesn't make sense to me, because the majority of the state is being, also transferred.
So if we look back at that code… Does this… by the way, is this stuff kind of making sense, or am I…
**Hannah Ramadan** 29:46 I'm tracking, I have to leave.
**Ariel @arielvalentin (ATX, USA)** 29:49 Did you have to leave? Okay.
**Hannah Ramadan** 29:50 Yeah, unfortunately.
**Ariel @arielvalentin (ATX, USA)** 29:52 No problem, no problem.
But, have a good day.
**Hannah Ramadan** 29:55 Okay, cool. See you guys.
**Ariel @arielvalentin (ATX, USA)** 29:57 Schwan, so… If I understand this correctly… My original implementation of this… Of this would have mitigated this problem, because we would have captured… We would have been carrying… no, not really. We couldn't do it. Carrying around the contacts wouldn't have made a difference.
So, it's the question of, like.
If we have to keep track of the fiber that's getting thrown around… How is the rest of the requests not gonna work right?
**Xuan Cao** 30:42 Are you… are you sure that, the rack is fueled in fiber?
**Ariel @arielvalentin (ATX, USA)** 30:45 Hold.
**Xuan Cao** 30:46 Like, the context he's using it for…
**Ariel @arielvalentin (ATX, USA)** 30:48 Yeah, so if we look back at that, right, that was one of the problems… Let's see here… Let me take a look, and let's take a look at the source code.
Oh… the SDK… Oh, probably the API, right? Not the SDK, because that's where the context object is?
So, the fiber stack, if you look here…
**Xuan Cao** 31:49 Are you serious? Or…
**Ariel @arielvalentin (ATX, USA)** 31:51 Yeah, well, I'm gonna also… I'm gonna… Oh, my screen in one second, sorry.
**Xuan Cao** 31:57 Oh, I see, I see the February year, okay.
Okay.
**Ariel @arielvalentin (ATX, USA)** 32:02 So… Whenever you make an invocation and attach, it's pushing it onto this stack, and the stack is a fiber… Fiber local variable, you know, attribute.
**Xuan Cao** 32:16 Okay.
**Ariel @arielvalentin (ATX, USA)** 32:17 And so… It's not a fiber lookup variable, it's a fiber lookal attribute. So, anytime a new instance of the fiber is spawned.
Then it's like… Oh, where would you… Like, where is the current context at the moment? Where do we see that?
variable, or where's a variable made available to us in this particular context, right?
And… If the… if it's true that what we were seeing here… if this is accurate, right? Or, like, if I understand how this is working, this… If I understand what's happening here, when… We have the request object, That request object is… The current fiber, whenever we call attach, it's attaching into a fiber.
And then when it calls detach, It's as if… The fiber has changed for some reason at the time that a call is detach.
So, when we look at one of these instances of the code.
It's as if, on start, Right?
And on error, or… You know, on, was it on commit?
No, not on commit.
Should be on start…
**Xuan Cao** 34:01 fish.
**Ariel @arielvalentin (ATX, USA)** 34:04 Say that again?
**Xuan Cao** 34:05 finish.
**Ariel @arielvalentin (ATX, USA)** 34:06 Right? Yeah.
Right, so either onError or on finish.
These are trying to detach the context. So, my question is, how is it possible Not even current span works.
In these cases.
Because CurrentSpan is going to look for the span on the context.
The context was… is not copied.
Right?
There's nothing here that's saying, hey, we're launching a new fiber, the new fiber… Like, in these cases, the span is getting… is getting passed along.
And then in these on-commit blocks, we're not pulling… We're actually not pulling the span… From the request, which is interesting. So that's asymmetric.
Something to note?
It's not pulling it out of there.
So, this is relying on the current fiber, to inject everything.
And then, Down when we call detach.
Detach is assuming… Detach… Is a request object That's… Like, at this point, it's saying that it's executing it in a completely different fiber.
I think that there's something suspicious about that.
I have to understand how this web server works.
Which web server… which web server were they using?
**Xuan Cao** 36:04 Oh, well, just a… Instant gas is possible caused by some weird risk condition, or that's totally not on puppy?
**Ariel @arielvalentin (ATX, USA)** 36:17 Say that again? I'm sorry, I was.
**Xuan Cao** 36:19 Yeah, Is it?
The case for the wrist condition?
**Ariel @arielvalentin (ATX, USA)** 36:31 A race condition where the request is… Where the, what, the events are being invoked by different…
**Xuan Cao** 36:41 Yeah.
**Ariel @arielvalentin (ATX, USA)** 36:42 By different fires?
**Xuan Cao** 36:43 bubble.
**Ariel @arielvalentin (ATX, USA)** 36:44 No.
**Xuan Cao** 36:45 I mean, by different, like, like, web server storage.
**Ariel @arielvalentin (ATX, USA)** 36:54 Well, if they were different web server threads, then they would have different fiber locals.
**Xuan Cao** 36:59 Everett, okay.
**Ariel @arielvalentin (ATX, USA)** 37:00 So, it would, you know… So, you know, in these calls, let's go back to what it was, you know, when we were looking at the source code. Let me go back and look at that source code.
So, we looked at the source code, right?
If, say, two threads were calling in here.
These request objects would be different.
And each of those threads would have a different fiber local stack.
they would have different fibers, right? Because each thread has one main fiber.
But if you have one thread that's using multiple fibers.
Then that means it's handling a fiber per request.
So, this on start would work fine.
Because when it attaches the context here, it uses the thread's current fiber.
Right?
And the token and the span.
correspond to this individual request. But when we get into the onError.
or we get into on-finish, these are using the implicit fiber.
Which should still be okay.
that they use the implicit fiber as opposed to the span that was in the request ENV?
Or the token that was in the request ENV.
Those should be fine, because this current span is still gonna look at what the current fiber stack is.
Right, because it's no longer using a thread local… the main thread fiber to do anything.
All of that is… Each fiber is getting invoked implicitly.
When it's pulling it along.
So… this is unusual.
Right, or not unusual, but this is asymmetric.
Like, it might be better for us to say… Go into the request, and grab this.
And pull the span out.
Right?
But it might be problematic for us to say, add the current fiber to the request. That doesn't make sense.
Because if the request is bound to the fiber, then the fiber should be calling… the same fiber should be calling onCommit and onError.
So that's the part I don't understand right now. That's the part I need to wrap my head around. Does that make sense, Juan?
**Xuan Cao** 39:31 Yeah, yeah, I, I understand what you, what you're saying. I think, probably, this person needs to buy some, reproducible code to… for us to test, so we can, like, dive in to see the… what is the fiber ID or contact ID, something like that, to make sure they're… If it's really something that's different during the… Like he said, it was 3ml's body, I don't…
**Ariel @arielvalentin (ATX, USA)** 40:00 Yeah, so what they're saying is that, like, at least what… yeah, what you're saying, and so what I want to see is what web server they're using, because they're saying, when using rack events, unfinished callback can be invoked from a different fiber than on start. So this is in the case of streaming response bodies. So, if you have a streaming response, like.
Like, an events… stream or whatever, then it's possible, okay, I see that… so, we need to find something that's using, like, WebSockets.
I think, done.
To figure out what's going on.
Cause I'm hearing him say that… the onFinish is happening on different… like, on start and on finish are happening in separate… fibers, because that's how it's implemented with WebSockets. So using the implicit fibers doesn't work.
**Xuan Cao** 40:55 Yeah, I think you need to put more on context.
**Ariel @arielvalentin (ATX, USA)** 40:59 Yeah, I think so. And, you know, what's gonna be even more problematic, I think, is… When we get into our automatic instrumentation.
or not automatic instrumentation, but library instrumentation. What does it expect when it calls, you know, rack current span, or is the context even being propagated at all?
Right? So, like… Whatever the ingested pro… Context that's coming in from the request.
If that context is being propagated to libraries, because… If it's switching to a different fiber.
Does the… say, like, I don't know, the active, you know, the, action dispatch span, does it find the rack span?
Because it's on a different fiber or something?
I don't know.
Anyway…
**Xuan Cao** 42:01 Yeah, yeah.
**Ariel @arielvalentin (ATX, USA)** 42:01 We need more details, yeah.
**Xuan Cao** 42:03 Yeah, yeah.
**Ariel @arielvalentin (ATX, USA)** 42:04 That's right, yeah, back to him.
**Xuan Cao** 42:07 And there also is a red span. Not this original span, which it won't cause the issue.
Yep.
You want to… you want to comment to get… to try to, get more, like, info contests, and produce the code for this person?
**Ariel @arielvalentin (ATX, USA)** 42:25 Yeah.
Yeah, I think that that's what I'm at least gonna do. I mean, I've got the two problems, right? One of them being that… The Claude signing, and the second is, like, I need a little bit more detail.
If they can help me out.
Hmm… If you want to respond to them, that would help me a lot.
Why don't care.
**Xuan Cao** 42:51 I can try to respond, but I'm not sure if I, like, I… I… my response will capture what you were saying, but I'll try.
**Ariel @arielvalentin (ATX, USA)** 42:59 No, it's okay, it's okay, I could try to get to them as soon as I can.
Because I need to have, like, a well-formulated thought here as well, right? Because I'm, like, I'm speculating about, like.
Something, but I think I…
**Xuan Cao** 43:11 Yeah, it's…
**Ariel @arielvalentin (ATX, USA)** 43:12 I really need a real…
**Xuan Cao** 43:13 F.
**Ariel @arielvalentin (ATX, USA)** 43:14 Yeah, please, go ahead.
**Xuan Cao** 43:16 No, sorry, I was gonna say, yeah, it's just, It's, it's kind of, strange to have, like, multiple fiber, then trying to put a thing out, like, pulling out those, attacks.
If they're in the same, Thread, the same context, so, yeah. I'm just wondering how they do, how they do that. It would be interesting to see the edge case, yeah.
**Ariel @arielvalentin (ATX, USA)** 43:45 Yeah, that's about it.
Okay. Sean, I guess we can call it, because nobody else is here at the meeting, and .
**Xuan Cao** 43:54 Oh, and then for the clouds, I think some repos, they actually allow the clouds as, like, the contributors, but I'm not sure that maybe you need to add the cloud as, You know, instant.
**Ariel @arielvalentin (ATX, USA)** 44:07 Well, that's an easy CLA thing. I have no idea, like, that's out of my… My wheelhouse here, where it's like, you know, some agents are… Have been authorized, or whatever.
It's a pro… you know… but we also don't have, like, an agent's markdown file, or… Or anything, like, there's one in the collector repo, that, you know, they want to standardize on.
We should probably break that in, because then at least that'll give the agent… Details on how to construct a commit message?
To specify that it's the co-author?
And that the.
**Xuan Cao** 44:44 Okay.
**Ariel @arielvalentin (ATX, USA)** 44:45 The person should be considered the author, and so on and so forth, so…
**Xuan Cao** 44:50 Hopefully.
**Ariel @arielvalentin (ATX, USA)** 44:51 Okay?
**Xuan Cao** 44:53 Okay, sounds good.
**Ariel @arielvalentin (ATX, USA)** 44:54 Alright, my friend, well listen, you have a wonderful day.
**Xuan Cao** 44:57 You too.
**Ariel @arielvalentin (ATX, USA)** 44:58 And until next time…
**Xuan Cao** 45:00 Sure.
Suga?
**Ariel @arielvalentin (ATX, USA)** 45:02 Take care.
**Xuan Cao** 45:04 Yeah, see ya, bye.
