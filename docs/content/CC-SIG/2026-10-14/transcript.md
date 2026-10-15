SIG: C/C++ SIG
Date: 2026-10-14
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Marc Alff [MySQL] 00:01:47 Hi, Doug.
Douglas Barker 00:01:48 Hey, Mark.
How are you?
Marc Alff [MySQL] 00:02:17 Hi Doug.
Douglas Barker 00:02:18 Hey, Mark.
Marc Alff [MySQL] 00:02:20 Okay, sound is working then.
Douglas Barker 00:02:22 Yeah.
How are you doing?
Marc Alff [MySQL] 00:02:25 Doing okay.
How about you?
Douglas Barker 00:02:34 Pretty good.
Marc Alff [MySQL] 00:02:36 Very good? Okay.
I don't know if Lalit will join. He was online earlier, and I'm sure he wants to discuss.
How we deal with exceptions in general.
Douglas Barker 00:02:53 Yeah.
Marc Alff [MySQL] 00:02:57 And, I've… so… I saw in the meeting notes, did Ehsan join last week?
More or less.
Douglas Barker 00:03:10 I think you tried to, I don't know if, I posted the, the new Linux Foundation links there, but I was in the meeting for about 15 minutes, and nobody joined, so I think maybe…
Marc Alff [MySQL] 00:03:20 Okay.
Douglas Barker 00:03:21 It's possible that he was joined on the… Meeting link.
Marc Alff [MySQL] 00:03:25 Oh, yeah, could be.
I'm wondering if you have seen the… the PR for Mateen to become approver, because he needs to approve it at some point.
Douglas Barker 00:03:39 Yep.
But it seems like we leave that open for a week, and then…
Marc Alff [MySQL] 00:03:51 Yeah, so typically we leave it… we leave it open for a week.
I was hoping to have everyone approve it so that we can close it right away, but the worst case, we leave it open for a week, and we have a majority already, so… Yep.
Douglas Barker 00:04:11 I just add the please review label to that PR.
Marc Alff [MySQL] 00:04:19 Do you want to share my screen, or do you want to share yours?
Douglas Barker 00:04:25 I can share mine. I think probably we can just focus on the no exception, or the exception handling, it seems like.
Marc Alff [MySQL] 00:04:32 Yes, yes.
Douglas Barker 00:04:33 Hot topic. One second.
window… Okay, hopefully I'm sharing the right window, let me know.
Marc Alff [MySQL] 00:04:43 I The one with your social and banking account?
Douglas Barker 00:04:47 Yeah.
Marc Alff [MySQL] 00:04:48 Yeah.
Douglas Barker 00:04:59 Let me pull over the notes…
Marc Alff [MySQL] 00:05:11 Okay, just just a sec. I'll be right back.
Douglas Barker 00:05:17 Alright.
What, West Green, DC?
Marc Alff [MySQL] 00:05:20 Yeah, so let's go to the functional alcohol.
Douglas Barker 00:05:25 Okay.
Marc Alff [MySQL] 00:05:33 Okay, I'm back.
Douglas Barker 00:05:34 Okay.
All right. Well, maybe real quick. So I did notice that the configuration 1.2 is available.
So we can…
Marc Alff [MySQL] 00:05:46 Yes.
Douglas Barker 00:05:47 I don't if there's anything… Major in there that I want to address, but I think there's, like, some new limits on the.
Marc Alff [MySQL] 00:05:54 There are some minor things, yes.
Some… something which has changed in the… I think it was in TLS, I don't remember exactly.
some limits.
for exporters, I mean.
It's minor things anyway. We just have to adjust for it, and we would have to make sure that We are not surprised by the new version number and the format.
Berditsa.
We haven't done that already, so we don't want to do it.
Douglas Barker 00:06:27 Good.
I guess on these kind of updates, we don't have a category for CI, but we need to… we have a few.
issues open to upgrade to 2604. I don't think they're doing the right thing, so we should bump the 2404 to 2604, and 2204 to 2404, and we don't have any… like, Renovate's not doing that, and I think the… Other PR that a contributor has is not doing that either.
This one.
So, I think… I can take this on this week, but I'm just gonna… and replace… 2204 with 2404 and 2604 with 20.
Marc Alff [MySQL] 00:07:13 True.
Douglas Barker 00:07:14 24-4 to 26-4.
Marc Alff [MySQL] 00:07:19 And I don't know if you noticed, but I've I've been accepting a lot of renovate prs in Cpp contrib as well.
Okay. Just to try to keep this thing up to date.
And we're still… we're still waiting on Owen's PR there, and It's not Tom Tam. There's another guy named Thompson, something who is really really helping there.
with all your innovate and clean up PRs. So It's finally taking shape.
Douglas Barker 00:07:51 Yeah. How are you feeling about the frequency? Because I, I, actually because of all the re renovate emails, I was subscribing to all the PR emails, but, but now I've, I've like had to filter it 'cause my inbox is just flooded and I don't know if that's, you know, I guess it's fine, but… It is creating a lot more work to manage all the Renovate PRs, and I wonder if they're.
Marc Alff [MySQL] 00:08:11 so…
Douglas Barker 00:08:11 We should… or how you're feeling about it.
Marc Alff [MySQL] 00:08:15 It's okay, because they are very small, so either they pass or they fail, and the only thing to do is.
Click for the review and click on merge. So… Oh.
Vision.
It's generating a lot of noise for… yes, we have a lot of PRs, but they're extremely simple to.
200.
So I don't mind. And also, the timeline for this is, like, every day at 6 in the morning, or something like that.
And because I'm in Europe.
I most likely see them before you, so I have time to merge them already.
So that we get out of the queue in, in review.
Douglas Barker 00:09:03 Okay.
Okay.
Alright, was there anything else while we're on Renovate that you wanted to discuss in the.
Marc Alff [MySQL] 00:09:16 Yeah, I think we should use the time for this.
The no accept thing, because it's, So the the 1st thing is so you did add some warnings in ceiling tidy for the new exceptions which are Not good in new.
which is fine. That created a lot of ceiling tidy warnings that we have on top of the one we need to to clean up.
No, the thing I'm concerned about is random prs trying to fix random things in random places, because there is a warning here, or a code change there leading to chaos. Chaos. So I think we first need to agree on what is the end result, to start with.
Because even that is not totally clear.
And then, even if we have that well-defined.
Oh.
Maybe have a plan to fix warnings in one area in particular, before attempting to to spray all the code with try catch blocks everywhere.
Douglas Barker 00:10:35 Yeah, I think that makes sense.
Should we go through your proposed plan and my comment?
Marc Alff [MySQL] 00:10:42 Sure, absolutely.
Douglas Barker 00:10:47 So I think you're proposing that the API should most likely not use try catch blocks. I think that would have.
Marc Alff [MySQL] 00:10:57 I saw your… well, can we go back and see the current state first?
Sure. Because the… Today… So… Today we have builds with and without exceptions, even though I don't. So I think there is a basal build which is trying to compile without exception. But that's pretty much it. And every other thing, including CMake, is built with exceptions, as far as I understand.
For so.
I don't know where the idea to support a build without exception came from.
Because it's a decision which is very ancient.
So I don't know… We have that, but the thing that I don't know is what was the rationale for that.
And, whether it was because, well.
Some people are not using exception anyway, so we should comply, or if it's… If it's because of some compiler that does not work in such and such platform, or whatnot.
But overall, with all the code we have, and we see that with the Silent ID warnings already.
The code as is as of today, there is no way that this works without exception.
We have code all over the place doing new, using… things in the C++ library that do raise exception anyway. So We certainly do not have a working solution without exceptions at all.
Oh… The thing is, for the API only.
I think I can. I can see So for people instrumenting an application, they may want to have an API which is not using exceptions.
Because otherwise it forces you to to build your own application with exception. And some people don't do that.
For example, MySQL, the code in MySQL is not built with exception, so… If we do use exception in the API, that would be a problem, I think.
So, for the API alone, I think we should support both with and without exceptions.
Oh.
For the rest of the good, like SDK exporters and all that.
So we we have a bit with exception.
but which is working.
We might have a bridge which is compiling without exception, but I don't think it will be.
Working very well.
Because the moment there is a problem, it's going to fail anyway and terminate your process.
So, the question is, on expectations, I mean.
My point of view is that we can expect Api with and without exception. But then the Sdk and exporters It's much more likely that people will need to compile a library with exception handling.
with the understanding that we don't leak exception anyway, because the APIs are tagged no except.
and then that you can link that library built with exception with your application, which is built without exceptions. I think that should work.
Any, any, any thoughts on that, or…
Douglas Barker 00:14:33 Yeah, I think it… It mostly comes down to.
The out of memory exceptions, I think.
Marc Alff [MySQL] 00:14:40 Yes, yes.
Douglas Barker 00:14:41 API, and, like, the question is, is can we actually Guarantee that in a no exception build.
a Alex exception cannot be thrown, and I don't… I think the answer is no, because we're using standard SharePointer.
Marc Alff [MySQL] 00:14:58 And…
Douglas Barker 00:14:59 It will allocate a control block, even if we allocate the object with no throw, like we can't.
And C++14 prevent the shared pointer from Using the standard allocator, so…
Marc Alff [MySQL] 00:15:14 Yeah. And it's it's not only shared pointers, but I haven't looked closely at things like vectors, maps, and so on, but I would be surprised if every one of those supports a way to To have a no-accept method.
That sounds very unlikely.
So the moment we use a map, I mean, if we insert on a map and the map cannot allocate memory, what happens?
Douglas Barker 00:15:44 Exactly. So… I guess then the question is, like you said, like what's driving the.
then… No exception requirement for the bill.
I get that, you know, in the API, if you're including the headers, and you're building your own application without exception.
Marc Alff [MySQL] 00:16:01 Please.
Douglas Barker 00:16:01 Then that just flows through, but then what do we guarantee when that occurs?
Marc Alff [MySQL] 00:16:07 Well, I guess we guarantee that, so… The API layer itself is, basically all the virtual methods which are implemented in the SDK, like start span, for example.
So the API guarantees that no matter what happens, start span will work.
I mean, will not… will not raise an exception.
Now, the second thing is, as you pointed out, the definition of working.
Silently doing nothing with a no-op span.
is one way.
We can have also things like metrics which are not recording anything when you pass a value to it, for example.
So this is also working in a degraded mode in another way.
Okay.
And… So, when we have that with all the entry points in the API flagged as no except, Oh… the SDK… I mean, the guarantee that we have is that the SDK will not leak exception back to the application, so it must somehow deal with exception inside the SDK itself, and not let it go outside.
So, in that case, things like start span, as a try-catch block and return to the warp.
But I… that can work, and see… I think we got it working.
As far as every single entry point in the SDK working this way, I'm not totally certain yet.
Especially for weird cases, like, well… If we have an entry point that exports, I mean returns a shared pointer or returns Things that, cannot be represented cleanly.
If if there's a failure like what?
We also said that we cannot return a null pointer, because that will likely force the application to crash, and we don't want the instrumented code in the application to test every single pointer every single time.
So… I'm hoping we will not have any surprise the way the API is designed and find a case where we don't know what to do.
But otherwise, eating exceptionally everywhere, that seems feasible.
But it assumes that we can have a tricarge block, which means… We can do a build with exceptions.
If we cannot even have a try catch, I don't see what we can do at all.
Douglas Barker 00:18:52 Yeah, I think that makes sense. I think… Maybe you, said it in the plan here, but… Yeah, no attempt is made to support item 6. I think item 6 is… Fill in runtime without a memory, yeah. I think there's… I think we're stuck on this with the no exception build. There's not much we can do because we're using shared pointer everywhere.
Yes.
Marc Alff [MySQL] 00:19:19 So, I mean, it's a… The interesting part is that you can still build the code.
And in fact, this is what we do, I mean, I, I have to double-check the makefile, but I think we build without exceptions, because it's part of our makefile everywhere.
With the understanding that if… so.
If we have a bug like, oh, an index out of range in a vector or things like that, then it will fail fine.
But this is a bug in the code that needs to be fixed the same way. If we, if we use a null pointer, that will be a bug in the code and causing a crash. So Those are things… We may have defects, they will be found, they will be fixed, and then it will work after that.
The next family is, well, if you don't have any… if you are out of memory.
Things… things will terminate the process anyway, and this is.
depending on which application and how the and the design choices.
That can be fine as well.
Douglas Barker 00:20:32 Yeah, so this sounds reasonable, like, if we say, just make the expectation explicit somewhere in the documentation, that if you're building without exceptions on out-of-memory.
You would expect the application or the API to cause it to terminate the process.
Marc Alff [MySQL] 00:20:48 Yeah, so typically should work up to the moment you get out of memory.
Douglas Barker 00:20:54 But then on the… Build with exceptions.
not strive to… memory be non-terminating.
Marc Alff [MySQL] 00:21:05 Yeah, so in that regard, the build with exception.
With a try catch and returning a knob.
I think it will be more robust.
Because at least that… whose out-of-memory condition will be cleanly good.
So… It will be more robust than you have to accept to.
To link your application, with library compiled with exception. Anyway.
Douglas Barker 00:21:38 option.
Marc Alff [MySQL] 00:21:39 As far as how to do that. So what I just wrote for the Api like, Oh, don't use striker. Surely use Sed4. Looking at the code you you posted for For the performance optimization in the… in propagation, Oh.
You actually have a different way, which is working as well.
Oh.
Basically, you… Yeah, if you go back to go to the the Pr for that.
Yes, that thing, for example.
So, it's… So we have one line which is creating a shared pointer. And it's changed to basically 2 different implementations.
One with exception, with a tricouch and another one without exception with a no-fault.
So… That can work, I think.
Well, in that case, you have a make shared. I think I've seen other code where you add a new with no fault.
Somewhere.
Douglas Barker 00:22:56 Yeah, I think this is a part I did want to discuss, so… The advantage of make shared is that on pretty much all the compilers, this will result in one dynamic allocation that includes the object and the control block for the shared pointer. If we do new no throw.
then the object could be instantiated, you know, without throwing an exception. It would be a null pointer if it, If, it failed.
But then once we create this no STD shared pointer inside that wraps a standard shared pointer. So it's gonna dynamically allocate the control box if you are out of memory. Yes.
Marc Alff [MySQL] 00:23:35 you.
Douglas Barker 00:23:36 then that's gonna throw anyways. So it seems like, you know, what are we getting from trying to do that? Is it worth it?
Marc Alff [MySQL] 00:23:44 So, you know, it's… so, the bottom line is, it may work on some cases, but not always. Right. Like, it doesn't… so, if we were to return a unique pointer, for example, I think it may work.
Oh… But, the other thing is.
Well, even with a unique pointer, I mean, do we allow to return a null? Then the caller has to check for null all over the place, and they… Female.
Douglas Barker 00:24:11 Yeah, in all those paths, we'd have to have, like, some default object that we return when allocation fails.
Marc Alff [MySQL] 00:24:17 Yeah.
So basically, yeah, we have. We have to have a default result that works.
the same way we have a no op for start span.
So… The other thing that concerns me. So it it depending on which what the Api prototype looks like it. We may get it to work in some cases. The question is, can we make it work in all cases? It's not a given.
And the other thing is, we have one line of code which is, a make shared that expands to 20 line of code with conditional compilation and try catch and things like that. And I've not… I wanted to do that. I have not checked how many new we have in the API alone.
Douglas Barker 00:25:07 Oh, there's a lot.
Marc Alff [MySQL] 00:25:08 If we expand that pattern, it will quickly become a mess.
Douglas Barker 00:25:13 Yep.
Yeah, I was thinking about that, too. One thing we could do is, like, a templated helper function that's, like.
Make… make or default.
Marc Alff [MySQL] 00:25:25 Oh.
Or you pass that up.
Douglas Barker 00:25:28 Default object, and it returns…
Marc Alff [MySQL] 00:25:32 Yeah, well… we have so many layers of code, like no std, which is already a layer on top of something custom or on top of std. And.
Douglas Barker 00:25:41 Right.
Marc Alff [MySQL] 00:25:42 It's… If, if, yeah, let's see… How we can do that, So the other thing is, can you scroll just up a bit?
I think the most critical part to decide is what method like expand a couple of lines, so that we know which method that is.
Yes, here.
Okay, so this extract thing.
I oh, and this so this is really part of Api, because this is what.
Douglas Barker 00:26:32 Right.
Marc Alff [MySQL] 00:26:33 Application can call, we can, we can call extract on, on a Lucario.
Okay, so in that case, we have no choice, the extract must be no accept.
The thing is, Yeah, so we have a default object, which is default context, which is already used in, In some cases, like when we don't find the keys in the context, for example.
So, there is a way to pass… A default, a reasonable default that will work.
Boom.
The thing is, for other things, I've seen as… I've seen… I think I've seen that for, Instrumentation scope, I think.
for other things. The no, except maybe overkill, and maybe we have. We have a way to remove it.
In which case, that will simplify a lot of things.
If you go to the OpenPLS, for example.
And the first one?
So the code there like in this thing like attribute, insert or assign.
So there was some code before just doing using a map. And then Now there's a TriCash blog, there's… A lot of things.
But… all that patch just assume that this method has to be no accept, no matter what. And I think before going into fixes like that, we first must question whether no accept is really justified or not.
Because in that case, all the code It's only in the SDK. That patch is only touching SDK things.
So, inverse decay, we we can change things without breaking the Api.
And if we change this helper to… To not be no accept.
when all that code goes away. And I'm assuming that the exception will be propagated, propagated up typically to something like start span.
Because, the entry point is not, manipulating attributes. The entry point is start a span, and then on the span you can add an attribute, for example.
So, adding an attribute on the span will be an ORB.
Sorry, a no accept method.
But it can… it can do a try-catch there, leaving that code alone.
And… For the SDK at least, I think that will save us a lot of complications.
Does that make sense?
Douglas Barker 00:29:28 Yeah, I think so. I think you're… you're making the case, like, we should push the try-catch Blocks higher, higher, higher in the stack.
And, make these lower-level helpers not know except if we can.
Marc Alff [MySQL] 00:29:41 Yeah, basically push it up all the way to the entry point in the SDK.
Because… It makes no sense to have a… to have… like, if we have a call stack of 10 things calling each other with a nested depth of 10, We are not putting no except in all the 10 methods in that call stack.
That would be a mess, with try-catch block everywhere, and then returning null pointers and checking for nulls and whatnot.
So… Only the… only the top level.
Inverse decay, which is really the entry point coming from API.
Should be no exception.
Yeah.
Douglas Barker 00:30:27 I think that makes sense for the bad Alec, but if it's like a specific method that we know different types of exceptions that we should handle.
Then potentially we put the try catch in the specific method.
Marc Alff [MySQL] 00:30:41 Yeah, sure. We, we, well, we can, we can handle specific things, but.
And also we do have some methods which are flagged. No, except when they don't raise anything, so that they have a stronger type.
But if if a method today is raising an exception.
The fix may not necessarily be to add a tri-catch, it might be to just Release the constraints that it should not be no accept.
Douglas Barker 00:31:21 Yeah, I'm just thinking if there's a… Or some guidance that we could write down to help.
kind of standardize the approach that we want to see in these PRs, and I think.
Part of it is also driven by our policy, like, around this issue on the catch-alls.
Marc Alff [MySQL] 00:31:40 Yes.
Douglas Barker 00:31:42 And when these are acceptable and when they're not.
desired.
Because, like, one approach, like, I think maybe you're saying is, you know, we… Mark all these lower level functions as not, no, except.
They propagate exceptions, but then we don't catch in those functions, and we put a catch-all at the top, you know, start.
Marc Alff [MySQL] 00:32:05 Yeah.
Douglas Barker 00:32:06 As a catch all.
Marc Alff [MySQL] 00:32:06 It will be quoted on the top, so… Basically, the entry points are the different providers.
like tracer provider tracer and and span.
That should be pretty much it for the entire trace signal.
Douglas Barker 00:32:30 Some of these, like… Client, when there's file operations.
Marc Alff [MySQL] 00:32:34 Well.
Douglas Barker 00:32:35 I think that's where… Maybe the argument, you know, that we put the catch and handling at the spot where we're actually calling the function that throws, right? Yes.
Marc Alff [MySQL] 00:32:45 Well, obviously for things like infrared I/O, you can have some I/O failures. So those should be handled at that level.
Oh.
Like, if you cannot read from a file or write to a file, your… It needs to be handled at the exporter level, and maybe the thing will be retried later, things like that.
And then, yeah, so there is also the case of Yaml parser.
In that case, the whole… the whole thing is… I don't think there is a way to have a Yaml parser without exceptions.
Even if there is, it will make the parsing code extremely painful, checking return codes all over the place.
And I'm really questioning whether it's… it's… were fit, in terms of, development.
And even if it's technically possible, whether it's actually… robust, because we have code which is extremely untested. I mean, if you miss a single path somewhere where you don't shake on a pointer, of course, one day that pointer will be null.
And then you will have a cost there.
Oh.
So… Compiling with exception makes some, Makes the code much cleaner.
And easier to maintain.
Douglas Barker 00:34:10 Yep.
So, one thought I had when looking at this issue was that The catch-all… you know, is often used when we think we don't know what the exceptions that possibly could be thrown are, and I think that there's cases where that's profoundly unknown. That would be anything that wraps the user callback, you know, which could throw anything.
And that is a case for the providers, which call the configurators, which can be any user callback.
So, all of these are legitimate cases where we want to do a catch all. I don't know about RYML.
document. It seems like that one we probably know.
Marc Alff [MySQL] 00:34:55 Oh, okay.
Douglas Barker 00:34:56 exceptions can be…
Marc Alff [MySQL] 00:34:57 So, it looks like I misunderstood the… the issue report itself, I mean… I took that as a concern about having so many try-catch blocks.
But it seems the concern is the catch-all part.
Douglas Barker 00:35:13 Yeah.
Marc Alff [MySQL] 00:35:14 Okay, so the catch-all part, we definitely can… I mean, this is laziness on my side, we can… We can catch exactly the exceptions which are thrown, because SIGINTIDY will tell us anyway.
Douglas Barker 00:35:28 Yep.
Marc Alff [MySQL] 00:35:28 and have more robust code.
The only part is, as you said, if we are invoking some user control code in a callback, typically for metrics.
We don't know what's going on there, so in that case, we will have a catch-all, but only at very… Very precise points where we know we are calling a callback.
Douglas Barker 00:35:54 I think that makes sense.
So one idea I had there is there is a clean tidy check that we can turn on that will flag the catchalls and then.
That would force us to no-lint them with a comment, and then in that comment, we can describe, you know, why this catch-all is required. And I think, like we talked about before, there's those legitimate cases where we just don't know what the exceptions would be.
But then all the other cases where we could reasonably know the exceptions, we put the… Exact exception types, in there to catch.
Marc Alff [MySQL] 00:36:29 Yeah. Another thing also. So The complaint with the catch-all is that, yes, it may hide things.
Which is correct.
One other thing we should do as well is not only to catch exceptions, but also log them, especially… well, in API, there's nothing we can do, but in the SDK and exporters, log them.
Oh… so that if something so if something happens, at least we we can see that in the log and have some bug report about it.
No, especially the case, like, say, oh, back to the example with a vector with an index out of range. Well, if we start to to have a try cash block with a catch all.
A bug somewhere not using the proper index will be just ignored and… And the thing will just not work, and not record some data.
when Vivekto is used. So It's dangerous to just eliminate, All the signs that something is not going well.
So if we log it, at least we will have some… well, first of all, in our test case, we will see something.
and also in we can have per reports that say, Hey, I have this exception in my log.
So, sure, yes, the application was not taken down, which is good.
But I still would like this exception to.
I mean, this log record to go away in my own log.
Douglas Barker 00:38:07 I looked at this a little bit in the past. I think one of the challenges that we have with our SDK logger is that it also does dynamic memory allocation and can throw exceptions. So…
Marc Alff [MySQL] 00:38:17 SW2.
Douglas Barker 00:38:18 I think we need, you know, I don't know if it's been discussed, but maybe we need some effort to look at, you know, our diagnostics strategy for errors, and come up with something that is, you know, safe to call from, say, like, a bad alec, you know.
Marc Alff [MySQL] 00:38:35 Yes. So, it could be that we need to… To make the general logger more robust, so that… Especially, like, in out-of-memory conditions. Okay, so we don't have memory, we log something, and the very first thing the logger does is concatenating Concatenate strings together to build an error message, which, of course, use memory and raise an exception and so forth.
So… The logger probably needs to be much more robust, so that… At least it doesn't recursively raise more exceptions.
If it's too bad, then it just gives out, but at least not… Not add more more care as well.
Douglas Barker 00:39:21 Okay.
It sounds like a reasonable response, then, to this one is, well.
Try to remove as many of these catch-alls as we can, and then… I can turn on the.
Claim tidy check to flag these, and then we'll add comments exactly where they're… really needed.
Marc Alff [MySQL] 00:39:41 So, do we… Do we really want to remove them? Or do we want to catch this, catch that, catch everything we know, and only then have a catch roll next to it for something we We forgot.
because there is also the risk that if we, if we don't catch something that technically can be found, then we are back to the case where the application is taking is is down.
Douglas Barker 00:40:11 Yeah, I think… I think it's definitely valid, because… It would rely on us knowing exactly what types of exceptions can be thrown from a given function.
Marc Alff [MySQL] 00:40:20 Yes.
Douglas Barker 00:40:22 And I don't know of a good way to test for that, to make sure that we've caught everything other than to have a catch-all.
Okay, so maybe the… the direct response right now is… We just need to go through and make sure we're catching and logging what we can on the SDK side.
Marc Alff [MySQL] 00:40:41 Yes.
Douglas Barker 00:40:42 And then,
Marc Alff [MySQL] 00:40:48 Yeah, we definitely need to log it.
So that we see what's going on.
Douglas Barker 00:40:53 Okay.
Marc Alff [MySQL] 00:41:00 In case of the YAML parser, the list of exceptions found there is known.
It should be… it should be okay to make the list.
Every other place, well, we don't raise exception ourselves.
So… The only things we get is our exceptions, which are… formed by, say, the standard library or out of memory conditions.
I don't know… Like.
For example, for shared pointers and make shared, I mean, I don't know if a C++, prototype says explicitly which exception it can throw.
If it does, then Sirian Taidi will tell us that, hey, we need to catch this and that, but if it doesn't, We don't know what to expect.
Yeah, and back to the PI, it feels like throwing Batalog on top of that. I mean, it's.
It's going the wrong way, I think.
Bob.
One thing just to explore. Do you think it's worth to make a Pr.
But cleans up, no accept.
Oh.
And see if it builds, and see what will be the final result.
We've still anxiety with that.
just to get a feel of if we remove all the no accept code except in the Well, if we remove all the no except in the SDK, it won't build.
Because… Stolzban.
We'll have a different prototype compared to the Api.
So… We can remove no except from everywhere, fix the build failures so that we add back no except for all the the then found SDK entry points and see where we stand there.
I think it will be interesting to see what SILANCTID warnings are remaining after that.
Douglas Barker 00:43:44 Yeah, I'm not sure if Clean Tidy Like, if we have a method that's not no except.
And we… Do catch exceptions inside of it if Clank Tidy will know.
That method can't throw.
Exceptions, because they're all caught.
Or if it's still going to flag that as something that needs a try catch around that method. I don't know if that… Okay. We'll call them. Force us to add traffic.
Marc Alff [MySQL] 00:44:09 That's right.
Douglas Barker 00:44:09 Catch everywhere.
Marc Alff [MySQL] 00:44:11 Okay, I will try to make that PR just for, investigating things. I'm not saying it will be a final fix, but just to investigate to see where we stand.
Douglas Barker 00:44:34 Maybe we just, like, pick one signal, like, logs or something, and see.
Okay.
Oh!
Marc Alff [MySQL] 00:44:52 It's a It's a smaller topic, but I tried, so… I don't know if you noticed in the CLINK ID log.
Which is nicely produced by your tooling.
In the current log, there are very few things remaining for traces, if at all.
The things remaining affecting traces are more in the Api like propagation.
And there are a couple of things for logs, and there is a huge list of things for metrics.
And in particular, For metrics, there are a lot of issues related to variants which are used.
because we use get instead of get if in many places. And so, of course, that can raise an exception, and that makes Serentally returning, complaints.
I have no idea why the design is that way, but for some reason, for Matrix, for example, we have… long met. Well, we have int metrics, and we have double metrics.
But instead of storing a value which is a long in long matrix and storing a double in double matrix.
We have a variant there, which can be either one or the other.
and the use of that variant is creating a lot of things which are not Which are bad, cooling-wise and exception-wise, so… It could be, but we might have to refactor some code in the aggregation code for For metrics, independently of that.
Douglas Barker 00:46:41 Yep.
So for all of these, cases, what do you think of the idea of creating a helper function to kind of wrap? That way we just have one One line to change, as opposed to adding 15 or 20 for every single one of these news.
Marc Alff [MySQL] 00:47:05 I guess the first thing is to decide.
There is a warning because that thing in Meter, so whatever method that is in Meter.cc is not accepted.
So, if it's justified that it is no accept, then we can see how to fix the code.
But I think… Finding the points which are marked today as no except that could be relaxed will solve a lot of problems first.
one one challenge there is just dealing with noise like, yeah, this thing like in histogram aggregation, for example, merge diff.
If you look at the code there, this is a typical example of the use of Yeah, this one, for example. This is a use of a variant.
Causing what?
Douglas Barker 00:48:26 So, it sounds like the next step is, we'll go with your experiment, and then review it at a future series.
Cool.
Alright, anything else we should go over?
Marc Alff [MySQL] 00:48:49 Well… Just so… I don't know if you noticed, I've been merging quite a few things also recently, trying to get the queue down.
The part which is remaining is that list of please review PRs.
Some of them are actually very important, like the like in the middle, when we drain the queue in the batch span processor, for example, this is a fix which is really needed, especially for performance reasons.
And, it has been… there's a lot of discussion there, because the fix has been reworked and corrected, and I think it's in a state where it would be final, and we need to take a look at it.
And the other big thing is, all this singleton, thing on Windows.
So… That one, so… Windows has been a real pain for a lot of time.
for a long time with this Singleton thing, and we finally have a fix for that.
which looks… so, I don't know.
I don't know all the windows, Things in particular, which are specific to this platform, but just looking at the code.
We have a fix which, Good work. The question is.
If we take it, and we have to document it very clearly, because there are some weird things to do.
You have to… link with a special library, but only when you use the SDK.
If you only instrument an application, you still compile with header files in the API alone, and in that case, you don't need an extra library, which is the whole point.
Oh… But when we… Assuming this thing works, we need also to Update the documentation to clarify exactly how it should be used, so that people know that.
Douglas Barker 00:51:07 Yeah, that makes sense.
I think I think Owen has commented on this. Hopefully some of the Windows users, Experts will comment on this one.
Marc Alff [MySQL] 00:51:19 Yeah, I think that Owen looked at it already and had some comments.
Douglas Barker 00:51:24 Okay.
proof.
I think we also have a release.
Marc Alff [MySQL] 00:51:36 Yes.
Yeah, so yeah, the last two… items. So the batch span processor I just mentioned, and there is the same thing with the log.
Record processor.
typically what's going on. The whole idea of batching is that you pile Data inside the buffer, and then there's a thread that picks the buffer and sends everything on the wire.
And then it's supposed to wait until that buffer fills up again.
To start, basically, a bunch of records at once, and today we don't do that. When… when we send something, we come back, and if even if there are very few records in the buffer, we export it again and again, so that we end up being Instead of doing few exports with a lot of data in them.
We do the opposite. We do a lot of exports with very few data in them, which is bad.
Douglas Barker 00:52:35 Okay.
That makes sense.
Any reason not to mark this help wanted?
Marc Alff [MySQL] 00:52:44 Mr.
So we we can do that. But I think the the point is to make sure to approve the 1st Pr on batch, I mean the on the trace processor.
So that when the code structure is approved and final, it's a matter of doing a copy and paste and apply it to logs.
So I think the author wants to do the logs as well, but he wants to make sure that the first PR for for the Batch Span Processor is approved first.
Which makes sense to me, because It's… there's nothing specific to a signal, it's just the same pattern.
Douglas Barker 00:53:48 Okay.
Are you familiar enough with this to review it and approve it, or should we wait on Tom, or should I dig in?
Marc Alff [MySQL] 00:53:56 So I.
There is a lot of things to read, a lot of discussions there. But yes, I can. I can approve it. I was hoping for Tom as well to to comment and approve, because he he made some earlier comments in that Pr.
But as far as I know, so it was open a while ago. I don't remember the date.
Douglas Barker 00:54:18 Yeah.
Marc Alff [MySQL] 00:54:20 Yeah, so… We should not let it out.
And in a state, as of today, it's in a state which is good to go, I think.
So, I will take a look and review it.
Douglas Barker 00:54:33 Alright.
If you think it's good to go, then I'll… I think we should mark this other one as, needs help, so that we can get it in for the release, if that makes sense.
Marc Alff [MySQL] 00:54:43 Okay, yeah, makes sense.
Douglas Barker 00:54:50 All right. I had a few on performance, which hopefully are reasonable. I think this one.
This one is… is a… Pretty big performance improvement, so with the last release, the composite and Rule-based probability samplers are… very heavy, So they can add microseconds, you know, on top of…
Marc Alff [MySQL] 00:55:24 Awesome.
Douglas Barker 00:55:25 the trace or milliseconds if you have a lot of spin as it spins.
Marc Alff [MySQL] 00:55:29 if.
Douglas Barker 00:55:30 So… you know, it's like a whole couple of orders of magnitude more expensive than the traditional, you know, trace ID ratio, so I'd really like to… Get these, performance improvements in.
Yeah.
Marc Alff [MySQL] 00:55:45 I I looked at the code overall. But I need to make a second pass to to approve it. But yes.
Douglas Barker 00:55:53 I think Mateen worked on this originally, the composite sampler, at least, so I'm gonna ping him to see if he can take a look as well.
Marc Alff [MySQL] 00:56:00 Okay, yeah.
And… When looking at things also on… So this is for the samplers, but I think you did also something for, propagation performances?
Douglas Barker 00:56:18 In this one, the big… big win, I mean, it's not a crazy amount, but, you know, we're doing extra dynamic memory allocation whenever there's an empty contact, so if somebody has a sample.
Marc Alff [MySQL] 00:56:29 Yes, yes.
Douglas Barker 00:56:30 Sampled span, you know, it's just unnecessary work, and then some of these other cases are…
Marc Alff [MySQL] 00:56:35 And the Http trace context. This happened to be the the case which is the most used, I think.
Douglas Barker 00:56:42 right.
Marc Alff [MySQL] 00:56:43 No.
Yeah, and I've seen many things, just… small changes, like in… I don't remember where it was in Vapi, but typically.
There is a local variable which is assigned, so it's a shared pointer, so it's assigned some memory allocation and whatnot. And then there is an if-then-else, and it is only used in one branch, not the other.
and a lot of things like that like we construct an object. We pay the cost for it. And In one case it is used, so okay. And in the other case it was just pure overhead for nothing.
And just by moving one line, we can… we can improve things.
So… This shows that this code has been well, it is very old. First of all.
And also, we don't… We also don't want to touch the API code in general because of risk for breaking things and whatnot.
They choose some, some age.
In places.
Douglas Barker 00:57:58 Yep.
Okay. I'll, for the release issue, should I just edit the… Issue description directly and add some desired here.
Marc Alff [MySQL] 00:58:11 Oh, absolutely.
Douglas Barker 00:58:12 Okay.
Alright, I'll do that.
What do you… I know you wanted to do the release in October. You still want to try to target, you know, at least by… Next week or two.
Marc Alff [MySQL] 00:58:25 I don't have a firm date yet, we'll see, the main thing is, So these these things for the batch should be should be fixed, and Also… Whether we do some small fixes, like, adjust to… Cpp, the the Yaml config, for example, things like that. It's just to keep up with it.
Or if we do some major changes with exception handling.
Exceptions… There are so many things to fix that it may take some time to stabilize.
So I don't know if we should start right away, do a minute in the middle, and then finish the cleanup.
Or if we should plan for more time to clean up a lot of things before making a release.
No.
I haven't thought about it yet, so… You'll see.
Douglas Barker 00:59:30 Okay.
Yeah, it'll probably depend on your prototype for the no acceptance, see if, like, that's a pathway Pursuit, because then that may resolve a lot of the warnings, and… Focus the changes in a very small set of files.
Marc Alff [MySQL] 00:59:43 Yes.
Douglas Barker 00:59:44 So… All right.
To be discussed in the next meeting.
Marc Alff [MySQL] 00:59:49 To be discussed, but I will have some time next week, so… So we can… If we choose to do a release, we can make one.
Douglas Barker 00:59:59 Okay.
Alright, sounds good.
Marc Alff [MySQL] 01:00:03 It also depends if you need a release for something, as usual.
Historically, sometimes the release is done because it's driven by a calendar, and sometimes the release is done because some maintainer needs it for… For its own application.
Douglas Barker 01:00:21 Yeah, I'd advocate we do try to get a release out in the next couple of weeks because we have that issue with I think it's 2604 and GCC 15, where there's a compile error because of that.
Marc Alff [MySQL] 01:00:32 yes.
Douglas Barker 01:00:33 That predicate factory header issue. So if we, can. I think we get that out and available, so it builds on more platforms.
Marc Alff [MySQL] 01:00:42 Yes, definitely. And this is showing up in Cpp Contrib as well. Some upgrades to OpenTelemetry 29 failed because of that. So yes, we should fix that.
Well, we should make a release that will fix that.
Douglas Barker 01:00:56 Yep.
Marc Alff [MySQL] 01:00:57 Okay.
Douglas Barker 01:00:58 All right.
Cool. All right.
Marc Alff [MySQL] 01:01:03 Well, thanks for your time. Yeah. And, It's I see one line again this week. So.
Douglas Barker 01:01:14 Alright, sounds good. See you, Mark.
Marc Alff [MySQL] 01:01:16 See you. Bye.
