SIG: JavaScript SIG
Date: 2026-05-13
Duration: 61 minutes
Zoom Recording URL: https://zoom.us/rec/share/xDAFBsdJRfikY6Z8qKxa9uOeue40uuDQH_TgGxEM1beEO-EKmwxnoEjr92CX4w.-LESMG58vr1l7H3u
============================================================

## Zoom Recording Transcript

Trent Mick 00:00:50 Oof.
Marc Pichler (Dynatrace) 00:01:44 R.
Looks like… David is… Not on the card yet.
But… There it is.
Trent Mick 00:01:54 I'm just connecting.
Marc Pichler (Dynatrace) 00:02:01 Hello?
Alright, David, do you want to kick it off?
FD inspect topic.
David Luna Bistuer 00:02:14 Yeah, maybe just… So the question, so we got this, PR.
That's adding a new symbol in the span implementation.
It looks okay, but, well, it's… I don't know if it's a problem or not, but it's a very specific symbol for… just for node.
I guess we can, I was thinking we should allow… have something that is specific for non-Hispanic implementation, since For the next major, we want to kind of get rid of any… platform-dependent code in… in Trace SDK.
Or maybe try to make this implementation work for both, At least for the two runtimes that we are supporting right now, which is browser and Node.
I wanted to know your opinions on that.
Marc Pichler (Dynatrace) 00:03:16 Yeah, I think I'm kind of in the same boat. The way that it's structured right now, it seems that it would work with Node Inspect.
But it wouldn't really… break anything, right? So if we were to merge this today, the inspect feature starts working on Node.js, but the browser doesn't have it, so it… Essentially, yeah.
David Luna Bistuer 00:03:52 that.
Marc Pichler (Dynatrace) 00:03:52 But it is that code that adds to the bundle size, I guess.
No.
Trent Mick 00:03:58 much, though.
David Luna Bistuer 00:04:01 Yes.
So, I don't know, so… it's okay to make an exception, maybe. I know browsers, they have the console logins, it's, at least it's easier to inspect.
Marc Pichler (Dynatrace) 00:04:13 Interesting.
David Luna Bistuer 00:04:13 On the browser console, so… Yeah, I was having this.
Don't.
Marc Pichler (Dynatrace) 00:04:21 Yeah.
I think I'm not, like, completely opposed to adding it. It does seem a bit, I don't know.
Weird to edit this way, but as long as it doesn't break anybody.
I'm not completely opposed to it, I think one question we should ask is, Why?
Debugging, of course, is one of the Things that we should… Improve somehow, but… the console logger… Already logs stuff to the console, it just doesn't log everything.
Trent Mick 00:05:19 The console logger? Sorry, not the internal SDK.
Marc Pichler (Dynatrace) 00:05:21 Yeah, sorry, No, I understand, yeah, the console… the DR console logger actually just takes the thing and then probably makes object-object from it.
Trent Mick 00:05:41 Or, I mean, you can… so… if… maybe this hits on the head for me right now, because I'm working on declarative config stuff, right? Where, you… as… As a rough… test, you have whatever config, and you create SDK components, and then you want to see if those SDK components are what you expect.
And… dumping them gives you the hundreds of lines of output right now, if you console.durtham or util.inspect the equivalent. And I haven't looked at this PR, but, like, theoretically, this makes it way cleaner to be inspecting what the internals of this thing are. It's the moral equivalent of adding Under, under wrapper.
methods on classes in Python, if that means anything to you, except that that's built into Python.
Core is a well-known thing, and doesn't have, like, different runtimes can I have in questioning, so… Yeah, if it's not considered too much of a hit on bundle size, this is probably a huge… Win for, like, internal maintenance and debugging.
I would think.
Slightly related for… because I've been thinking about tests and how I would want to test them.
For the config stuff.
So, on having that representation, so if you want cause… so… for testing that a given config results in the SDK components… SDK components that you expect. Some of the tests right now are reaching into… private internal methods of the returned SDK components, so, like, you… you define a config as a fixture, you ask the… SDK node and config… config configuration packages to generate the SDK components, and then you want to look at those SDK components and say, okay, did you build what I expected? And so, right now, those are internal details, right? To know specifics of the exporter that was built on the returned tracer provider kind of thing. You have to dig into these under methods and do these things. Having this representation that gets kicked out that you can inspect is… an interesting way to look at it. What I was considering doing was writing to string methods on these classes so that we could dump the whole thing in, we'd give kind of a string representation.
Motivated somewhat by noticing that the Hotel Java does the same thing, so they have a thing where I think they may log at some debug level. You can log a string representation of an SDK object.
We're already doing this, copying what Java was doing for the comp… composite samplers, so you can get it to string of a composite sampler, and because it's, like, a nested data structure of composable samplers.
You can kind of get a view, or a string representation of this object thing that you built up, so… That's… Yeah, related to this.
It's a long-winded way of saying I like the idea. I haven't looked at the implementation.
Marc Pichler (Dynatrace) 00:08:54 So, would you prefer, 2-string?
10, or is it…
Trent Mick 00:09:02 I took programming Python, and you have both in Python, right? You have under, enter, string, under, enter, and same for reprod?
And the repper… I don't know, what I got used to there is a string is kind of a readable representation. REpper is going to give more… is going to be more verbose and give you more details on the thing, even to the point sometimes of the wrapper can be cut and pasted and used to create a new Python object, but that's… that's not always a guarantee.
So, I would potentially like both. Like, I would expect this one would just be for debugging by… node developers of the SDK.
components, and I think it would be a big boon there, because usually when I'm trying to see, like, okay, what's this thing that I have at this point in the thing, and you console.dur.
with this SDK object, and then you gotta go back through hundreds of objects, and like… God help you if it's got an HTTP request on it, right? Because it's… it's going to be a big ugly object, but… So I think that would be a win for this. The toString thing, I would consider also adding for testability. I'm not sure I would use this in tests, because testing the string output from util.inspect is probably, not gonna be very robust, or… maybe not robust, it's just gonna be wordy and not very elegant to be using and testing, but, good for debugging. So I think they're two separate purposes. I mentioned the other one, maybe it was just distraction, but it's related.
Huh.
Yeah, I like the idea.
Potentially both. I think they're independent.
Marc Pichler (Dynatrace) 00:10:43 Alright, so I'm not sure if we answered the question now. Our thoughts are we would like to have something like this, I think, but.
Trent Mick 00:10:55 Oh my god.
David Luna Bistuer 00:10:55 Yes.
Yeah, I guess we can say that the benefits of having this, worth the… To have, to have… well, if you, if you check the, The implementation is just adding a couple of methods to a tracer and a span, and then using a… format function, but I think that it's… it's expect… so there is the inspect function, but I think it's not… But it's passing it, so it's using the… So it's not… it's not too much photo, actually, for the benefit that we're getting from… from Inspect.
Yeah.
That's a function. Anything that inspect parameter, the inspect function, that it's receiving as the last parameter.
Is something that it's… Passed directly by now.
Yeah.
So it's pretty straightforward.
Marc Pichler (Dynatrace) 00:11:49 One thing I was… I'm… I'm not sure about is… If this, ends up in the types… At the end?
I'm not sure if we can somehow make it erase so that this isn't there, because if I understand correctly, it doesn't really matter if that's part of the types or not.
So if this is hidden, then… I guess it's also a bit more difficult to depend on that specific behavior of this thing.
I'm not sure if anybody would do that, but, I've seen things. People doing stuff with it.
Trent Mick 00:12:46 I agree, probably on one of the types, I don't know if it shows up there.
Marc Pichler (Dynatrace) 00:12:52 I think we would also have to have the same thing in resource.
Because… Accessing the attributes like this.
Can block a warning.
If you have async attributes that haven't settled yet.
So we would probably have to do that in the dependency.
That's weird.
Trent Mick 00:13:21 What do you have to do in the devs? Oh, add and inspect?
Custom?
Marc Pichler (Dynatrace) 00:13:25 Yeah, add an inspect to resource to, because this works.
Trent Mick 00:13:33 and the metrics and logs SDKs as well, right?
Also, some language to say that this is not a… promised interface at all. This… What the representation here can change.
On the particular daily whimsy of maintainers.
I guess because I, yeah, I wouldn't ever want to have to… rely on that, even changing, like, changing this thing, like, basic tracer provider, we're gonna change that to tracer provider, right? So… Even the name of this thing.
Hold on.
Marc Pichler (Dynatrace) 00:14:29 Yeah, people… we definitely need some language to say that people should not rely on the output of this too much.
Especially with the console span exporter and stuff like that, I've seen people try to build, Try to build exporters on top of the output of the console output, where they just read the standard, standard out, and then, used the output from that, and I was, like, a bit confused by the approach, because it's… yeah. Anyway, People do things, and we probably want to make sure they don't do things that we don't want them to with it.
But yeah.
Trent Mick 00:15:24 So that inspect custom does show up in the types. I don't know if that's.
Marc Pichler (Dynatrace) 00:15:28 No.
Yeah.
We can…
Trent Mick 00:15:35 I mean, it's a… it's a standard node interface thing that shows up. I don't know if this causes problems in the browser. Oh, wait a second, what is inspect… Custom.
Marc Pichler (Dynatrace) 00:15:45 I think that's just the thing that's defined here, because you can… Just use symbol for…
Trent Mick 00:15:51 and… Yeah, nevermind, it is… Defined in the… is it?
Marc Pichler (Dynatrace) 00:16:04 Yeah, it's defined here.
In inspect.ts.
Yeah, it would be nice if the type.
wouldn't be there. Maybe we can make that happen somehow.
Not sure yet.
Trent Mick 00:16:23 Do you know if anyone's ever looked at post-processing the DTS files to… Remove… like, the thing when we export classes and the private… properties are in the DTS files that we're exporting, which is one of the major reasons for wanting to avoid classes.
Marc Pichler (Dynatrace) 00:16:43 I think you can strip internal stuff somehow?
David Luna Bistuer 00:16:51 Maybe, do not export the class itself with the type.
Raphaël Thériault 00:16:59 TypeScript does that.
David Luna Bistuer 00:17:00 Meaning that, meaning that… Sorry, Raphael.
Raphaël Thériault 00:17:04 Oh, go ahead, sorry.
David Luna Bistuer 00:17:06 So, meaning that, from the SDK, we did the… Tracer provider, right?
In that case, the tracer, but instead of returning the tracer class, or at least on the definition of the method, instead of returning a… Tracer class, just return the Tracer API.
type.
Marc Pichler (Dynatrace) 00:17:26 Yeah.
David Luna Bistuer 00:17:26 so that.
Marc Pichler (Dynatrace) 00:17:28 That is, that is one way of going about it.
But I think what, Raphael was going to say is, there's a TypeScript option.
Raphaël Thériault 00:17:40 Yeah, there's a flag that if you mark it in JSDoc as internal, it's not gonna emit it.
David Luna Bistuer 00:17:46 Hmm.
It's done.
Trent Mick 00:17:50 Strip internal, maybe?
Marc Pichler (Dynatrace) 00:17:51 Yeah.
David Luna Bistuer 00:17:52 which person?
Marc Pichler (Dynatrace) 00:17:56 I think it's been here for some time already.
Trent Mick 00:17:59 It's 1.5.
David Luna Bistuer 00:18:02 Okay.
Marc Pichler (Dynatrace) 00:18:04 - So that's… that's one way to do it, but you have to remember to put the ad internal on there.
David Luna Bistuer 00:18:12 Okay.
Marc Pichler (Dynatrace) 00:18:16 So… You might still run into the issue where you define a private Property, and you don't put the internal on it, then it's not.
So, doing both might also be helpful, Strip the internal stuff.
by default, because I know we have some things that are… that are marked as that, marked as internal, so you prevent, accidental export of stuff.
And then we can also have the factory functions.
David Luna Bistuer 00:19:00 Okay.
Marc Pichler (Dynatrace) 00:19:01 Could be one option.
Trent Mick 00:19:10 Let's try it.
Marc Pichler (Dynatrace) 00:19:15 I think that leads us, into the 3.0 topic as well.
Does anybody have any more thoughts on… to inspect stuff.
Trent Mick 00:19:31 That works.
Anyway.
I have, how do I share diffs?
I'll go add it to the gist.
Marc Pichler (Dynatrace) 00:19:53 I'm eagerly awaiting.
Trent Mick 00:19:55 Yeah, I know, I know, okay.
Wait a second, I think I just deleted the file that I added, instead of… Oh, no, that's sad.
Marc Pichler (Dynatrace) 00:20:02 There it is.
Trent Mick 00:20:05 So that works, and then inspect goes away from the types, so we could do that.
Marc Pichler (Dynatrace) 00:20:09 Nice.
Trent Mick 00:20:11 If that helps, I don't know.
Marc Pichler (Dynatrace) 00:20:13 I wonder if I…
Trent Mick 00:20:14 I'm fine.
Marc Pichler (Dynatrace) 00:20:15 annotating more stuff with add internal, we could also get the package.
Precise dumb.
Because we ship a lot of types that aren't used.
By consumers, so if we don't ship the types, the package size will be smaller.
Trent Mick 00:20:33 1,000 paper cuts, though, right? It's gonna take a lot of work to get…
Marc Pichler (Dynatrace) 00:20:38 Yeah.
Trent Mick 00:20:38 bits and bobs. Your time's way better spent on the proto-buff stuff that you're doing.
You're never gonna… you're never gonna beat that one. Yeah, that's a good thing.
Marc Pichler (Dynatrace) 00:20:48 Good return on investment there, yeah.
I was also surprised to see that it's 10 megabytes in the end.
I thought it was less, but… Alright, So, I guess… We are at the point here where we say if we can make sure that stuff is not exposed, that we don't want to be exposed, and if, it is Not adding too much.
Stuff to the browser bundle, then we should be okay with it, right?
David Luna Bistuer 00:21:38 Yep.
Trent Mick 00:21:38 I mean, so I would like to see it in. I struggle on the… like, anything adds to the browser bundle size, so… I don't know what… the decision criteria is, so… I don't know how we decide.
Because, I mean, methods on a class do not get… stripped, right?
David Luna Bistuer 00:22:02 Yeah.
Trent Mick 00:22:02 Like, there's… this… this'll be in there. There's no way to… there's no way to tree-shake this thing up.
Or is there? I don't know.
David Luna Bistuer 00:22:15 No, no, you get the whole thing. Using glasses.
But that's fine.
Trent Mick 00:22:23 Okay.
the ship.
David Luna Bistuer 00:22:33 We have, maybe just for completeness, we do have, conditional exports for… for example, ID generator, and this kind of stuff, so boundaries get just one class or the other. Maybe it's that… my opinion, that's not too much code, just to have it, so… if there is something, you know, in the future that we need to add more features or not in some specific… this plan implementation, maybe we can just fork it and have it kind of one specific for browser and another one specific for Node.
And then, well, you just, you know, use the exports, or… Again, the package JSON, so you point… for browsers, you point, okay, that's this plan.
Class that we want to use this time, the file that we want to use for browsers.
Caravan.
Trent Mick 00:23:28 Or do we have our first real reason for a node tracer provider down all of a sudden?
David Luna Bistuer 00:23:33 Yeah.
Trent Mick 00:23:34 Bring the class back a week later.
Marc Pichler (Dynatrace) 00:23:42 Yeah, I think that's definitely a possibility to have, Have it split like that, or… If we have the factory functions, we can also define the property on it.
David Luna Bistuer 00:23:54 Yeah.
Marc Pichler (Dynatrace) 00:23:55 which would be one way to go about it.
Trent Mick 00:24:02 Yeah, that's true.
Marc Pichler (Dynatrace) 00:24:04 Or is it way less…
Trent Mick 00:24:05 strategic.
Marc Pichler (Dynatrace) 00:24:05 Yeah.
So there's ways forward, which is good to know, I think.
Alright. Okay. Should… should we talk about 3 total, then?
Trent Mick 00:24:24 Yep.
Marc Pichler (Dynatrace) 00:24:29 should we start? I think we should first, so, before starting with it, we should look into… getting the… Release workflow setup, so that we can do it on the… on a newly introduced 2.X branch, So, we can still release bug fixes and security fixes during the time when we work on 3.0, and once that's ready, I think we can get started with it.
We would just… Create an issue, let everybody know that It's starting at this state, and… then we start chipping away. We should also set a deadline, of course, until when we want to be finished.
To avoid dragging on too long, with the 3-digital work.
And to create some urgency, but… I think if we have the tutor decks, brunch.
And we can still release from it, that's a good way forward. And then some features will be delayed, but That's the cost of doing that, I think that's fine.
Trent Mick 00:25:49 Related, do we… I agree with everything you said. On the… Blogs API SDK?
Did we want to get I mean, I guess we can't… We're not gonna sit and wait for that to finish, because some of it's… dependent on… the external TCE review and stuff, and whether… whether that's sufficient. So… I think, probably likely that's gonna slide out to the 3.0.
time frame.
If… and my bad, since the discussion last week about the widening the attributes type, I haven't followed up on that at all.
But is that a thing that is… helps if it's in 2.x first? Or is it a thing… or is that independent?
Marc Pichler (Dynatrace) 00:26:37 Mmm.
Trent Mick 00:26:40 Because it's an API question, so maybe it doesn't matter at all, because we're not doing a major API, so… Maybe it's independent.
Marc Pichler (Dynatrace) 00:26:48 Yeah, I think it's… it's fairly independent, The question is if we want to release, one dot… 10. I guess 1.10 would be the next version of the API. In… the same… cycle as… a 3.0 SDK.
Or if we would be fine with postponing that for a bit. One of the things I would love to do with, API 1.10 is to include the logs API as stable already, So, if we're gonna do it with, the SDK reader, though, then that might be a bit… difficult to time and get right.
we say we're not gonna do a 1.9… a 1.10 API release, then… We can just delay that until later. So, 3.0 wouldn't have logs.
Immediately, but get it as a feature later on.
Trent Mick 00:28:07 Yeah, do you know of anything that… will need to do an API release for 3.0?
Where are we fine?
Marc Pichler (Dynatrace) 00:28:14 I think you should be fine.
I'm not aware of anything that's…
Trent Mick 00:28:24 I guess we're still… are we… Well, here's a question. We're dropping support in the SDK for Node 18 and 20.
Are we gonna move the API for it at all?
I mean, we don't do a whole lot of work in the API, so it's not… doesn't feel as painful, but I guess we're gonna get to this point where… Actually, it's been so long since I've made any changes to the API, I don't have a good sense of, like, how painful the tooling story is there.
Because… Note 8.
Marc Pichler (Dynatrace) 00:28:52 Yep.
I think for the tooling, we said that we are just gonna upgrade it, And we have to manually check if the old, if it still works on old runtimes. And that's also what I did before doing the last API release. I just did a bunch of manure tests, and then figured out one issue, with Node.js 8.
Support.
And then changed that. So… since we don't release the API that often, it's… somewhat fine to just do manual checks later on. It's just tedious. With AI, it's a bit more… Quick, in that sense.
Because you just tell it what to do, and then it just runs through stuff.
Trent Mick 00:29:48 Okay.
Okay, so then back to… 3.0, yeah. So, we start with an issue for… being able to do 2.x releases.
And then we pick a time, and we freeze main.
Marc Pichler (Dynatrace) 00:30:06 Yeah, we actually don't need to freeze main at this point, we can just merge to main, and the 2.ax branch will be… what we need to backport, security fixes and bug fixes to.
Trent Mick 00:30:23 Yep.
Marc Pichler (Dynatrace) 00:30:24 So we can release from that.
I think going this way will be a trick.
Trent Mick 00:30:28 Tristan.
Marc Pichler (Dynatrace) 00:30:30 Yeah, so going this way around it will be a bit easier than what we did last time with the next branch.
Because it will be very clear where stuff goes, I think. And it will also be the same process that we will use later to, backport priority pack fixes to the 2.X line, which we have to support for a year, I think.
Trent Mick 00:31:00 Okay.
Marc Pichler (Dynatrace) 00:31:07 Right.
The feature freeze will be mostly a thing that, like, people can merge their features, but they won't see them until, the time Time has passed, and we are ready to release 3.0.
So, feature release freeze rather than, facial merge freeze.
Trent Mick 00:31:38 And we… Last time, I don't think we ever had to do releases of the previous, and I'm thinking about Contrib.
We basically just never did. We just got to a point where the new set of contribute releases used 2.x.
Or package dependencies and moved on.
Marc Pichler (Dynatrace) 00:31:58 Yeah, okay.
Trent Mick 00:32:00 Okay.
Marc Pichler (Dynatrace) 00:32:01 Or, for most things, I think congrip is fine if we bump the… the major versions there. Because for auto-instrumentations node, the setup stuff will remain the same, I think. People will still use environment variables, and we're still, I will be completely transparent to them. For instrumentations, they will need to update the instrumentation package, and might lose some runtime support.
But there shouldn't really be too much… of a change.
boredom.
Trent Mick 00:32:51 Yep, agreed.
Marc Pichler (Dynatrace) 00:32:54 An API. And then it gets weak.
Trent Mick 00:32:56 Do we need to do?
Marc Pichler (Dynatrace) 00:32:56 secure.
Trent Mick 00:32:57 release for a 2.X user, then we'd have to do it on a… Patch level release of those things, and basically manually.
Okay.
Marc Pichler (Dynatrace) 00:33:16 Alright.
Because let's move on to the next topic, then. If something comes up about the 3.0, we can still discuss in the JS Dev Slack channel.
I guess it's a good place to, talk about these things as well.
Just a request for reviews.
on the… Max export batch size option in the periodic exporting Metric Reader.
Pranav Sharma 00:34:01 Hi, folks. Yeah, this PR is from, me. It's to add this recently added, request in the OpenTelemetry spec, so…
Marc Pichler (Dynatrace) 00:34:14 Oh yeah, it does.
the same thing as in trace and logs, right? .
Pranav Sharma 00:34:23 I'm not sure if, this was across signals.
Marc Pichler (Dynatrace) 00:34:31 Yeah, it seems very similar. So this option already existed in the trace SDK and the logs SDK to limit the batch size of, like, how many things you're exporting.
So I think, yeah.
I mean…
Pranav Sharma 00:34:48 In the logs, it was based on the number of bytes, right?
Marc Pichler (Dynatrace) 00:34:52 No, it was the number of actual log records, because you don't know the bytes yet, for that, We only know during serialization, in the end, what will actually be sent on the wire.
I'm actually, error… take some time to review this. I will only be back on Monday, so I'll try to get to it then.
I'm not entirely sure that… This is the right way to go, but since it's in the spec, I guess we can still go through the motion there.
I do have, like, an alternative idea of how to accomplish what I think this is trying to do, which is to limit the export size on the OTRP side, so that You don't go over the limit of whatever the backend is prescribing, right?
Pranav Sharma 00:36:00 The, this… this one is doing batching based on the number of metric data points.
What was your alternative that you were thinking?
Marc Pichler (Dynatrace) 00:36:11 So, it seems to me that the feature is designed to Implicitly limit the size of the exported message in the end.
By limiting the amount of data points that are in there.
Pranav Sharma 00:36:32 Some of the backends, limit the… can only process a certain number of points. I… I think.
Marc Pichler (Dynatrace) 00:36:39 The editor?
Pranav Sharma 00:36:40 messages that I saw were, like, based on number of points.
Marc Pichler (Dynatrace) 00:36:43 Then…
Pranav Sharma 00:36:43 Number of, rather than the size of the message.
Marc Pichler (Dynatrace) 00:36:47 Okay, interesting.
Pranav Sharma 00:36:49 Yeah.
Marc Pichler (Dynatrace) 00:36:49 I… because… Yeah, I'd have to look into it a bit more, I know quite a few backends use… the request size is the limit. But if there's both, then I think it makes sense to have, kind of, both features there. One in the exporter, and one in the, In the metric reader, to be able to split these messages.
Boom.
So, yeah.
Trent Mick 00:37:20 Yeah, it might be two separate things. The upstream, PR and the hotel spec.
Said limit by bytes was a non-goal.
So, yeah.
Pranav Sharma 00:37:34 Yeah, just as an FYI, I recently, like, this feature is already implemented in Go and, and in Java as well.
Marc Pichler (Dynatrace) 00:37:45 It's a weird, third, Third prototype that we need to, to stabilize it.
Pranav Sharma 00:37:57 Thank you.
Marc Pichler (Dynatrace) 00:38:00 Alright, yeah, I will have a look at that one. If anybody else has time, please feel free to have a look at it.
It seems to be fairly straightforward, a bunch of tests, but, should be fairly simple.
Right.
Pranav Sharma 00:38:20 Alright, thank you.
Marc Pichler (Dynatrace) 00:38:23 Thanks for bringing it up.
And working on it.
Alright, any questions regarding this?
If not, then, and there's just an FYI from my side, I'm not sure if the same conversion is right, Trent, you released it yesterday, right? To 1.40?
Trent Mick 00:38:54 It's not.
There, that's 141.
Marc Pichler (Dynatrace) 00:38:57 Okay, yeah, thanks for doing that release, and, this morning, we also released 0.
218 of the experimental packages and the contribo, to get rid of some of the, security warnings that you got from installing Protopath.js, the version that we had pinned it to.
Two weeks ago.
So, NPM in-store.
Should now be back at zero, zero warnings in the end.
Yeah.
That's it.
Anybody else have any topics you would like to discuss?
Trent Mick 00:39:48 Alright, I caught the end of that sentence. NBM install should have zero warnings, that's… No way in hell that's true, is it?
Marc Pichler (Dynatrace) 00:39:55 Npm Audit has zero warnings.
Trent Mick 00:39:58 Audit, there you go.
Marc Pichler (Dynatrace) 00:39:59 Thank you.
NPM lean start, always once.
Trent Mick 00:40:06 Willow is wearing that.
Marc Pichler (Dynatrace) 00:40:12 At least in the, when you're developing, on the repo, then it will won if you just… try to install OTER, you shouldn't get any warnings, I think.
Because we barely have any dependencies.
Trent Mick 00:40:31 No, I don't want to go check, but yeah.
Marc Pichler (Dynatrace) 00:40:37 Maybe one of the contrib… maybe one of the country packages has its, not true.
Trent Mick 00:40:44 Oh, let's try SDK node.
No, you're right. It's all good.
Marc Pichler (Dynatrace) 00:40:51 Nice.
Okay, so let's go on to park triage, and if anybody has anything you would like to talk about, please feel free to interrupt, and then we can talk about this.
This is for the… Ultimately, export a base… Yeah, coach.
And it seems that… Some silent telemetry loss.
So… 2…
Trent Mick 00:41:40 Well, those are… those are new node features, right? So I'm not sure I call it a bug.
this node user Proxy is fairly, fairly new in Node, I think. Because, like, Node had, for a long time, not supported picking up on… HTTP proxy environment variables that are pretty common.
And then, fairly recently, added support for that.
Marc Pichler (Dynatrace) 00:42:00 Hold on.
Trent Mick 00:42:02 I might be wrong, but this is my understanding.
Marc Pichler (Dynatrace) 00:42:10 Since they tested against Note 22.
I guess this is the internal… thing, because it doesn't merge it together with the options.
There seems to be a PR here.
Yeah, so this is a negative development.
I guess we could still leave it at P2, People want to use this.
I assigned this PR to myself, and I see that… My review also requested here, so… I tried to get to this, from quick overview, this looks fine. I guess we just want to make sure that we don't… Do anything with that on runtimes that don't support it, so that, like, we don't… essentially backport that features somehow to, order Node versions.
That shouldn't have it.
Alright, so I think that's it for the core repo.
Let's also check if there's anything that's not labored as… A bug, but looks like one.
Looks… looks to be all good.
Alright, let's move on to Contrip, then.
We have one for… AWS SDK.
Seems to be related to… This specific version of that package.
Trent Mick 00:45:21 Well, I was working with Rory on this one.
Err, sorry, I was following the work he was doing.
Yeah, this one's gross. I took a little bit of a look at it right up on there. Someone's gonna have to spend some time on… Updating how we patch the AWS SDK stuff, because newer ones, I'm not exactly sure which AWS client.
Star packages are using that newer version of SmithyCore, but SmithyCore has moved Things around internally, so that the way Monkey patching doesn't work anymore.
Marc Pichler (Dynatrace) 00:46:01 Are we… are we patching interners?
I'm not sure.
Trent Mick 00:46:08 We were… Patching this construct stack function that was in… I have to look again, I can't.
Marc Pichler (Dynatrace) 00:46:29 Redclient.send.
Trent Mick 00:46:32 Oh, yeah, I guess it's a bug, or… but…
Marc Pichler (Dynatrace) 00:46:36 Yeah, but it's not crashing anything, right?
Trent Mick 00:46:40 You just don't get instrumentation.
Marc Pichler (Dynatrace) 00:46:42 Yes.
Trent Mick 00:46:42 bet.
David Luna Bistuer 00:46:43 Me too, then.
Marc Pichler (Dynatrace) 00:46:44 Alright, let me just put P2 on there.
And… I'm kind of hesitant to put, what was it? There was, like, a help needed?
Trent Mick 00:47:11 Oh, that up for grabs? Because it's immediate.
Marc Pichler (Dynatrace) 00:47:13 Yeah, okay.
Trent Mick 00:47:14 some AI contribution.
Marc Pichler (Dynatrace) 00:47:16 Yeah, the…
Trent Mick 00:47:18 We'll start timing it to see how many minutes.
Marc Pichler (Dynatrace) 00:47:22 AI-based. Yeah.
It's a free token, free token labor.
Let's leave it like this for now.
Since test our versions is failing, we… We'll probably get annoyed by this rather quickly, and then looking to that.
And this one is already marked as up for grabs.
And it also has a PR already.
Doesn't find DB properties… But, to park as well, I think.
Trent Mick 00:48:39 Yeah, I hadn't started reviewing this one because it's… guests also an AI contribution, but, they haven't signed a sale yet, so… Thanks for asking, dude.
Marc Pichler (Dynatrace) 00:48:59 Alright, then I guess, we'll leave that now and see if the person comes back and signs the CLA.
And… this one is… Question about memory leak. I seem to remember that there was a PR that… recently merged… Not to me.
Dude.
Fix it, and… I'm not sure if that is the only one that caused that, or if there's multiple instrumentations that run into the same problem, I haven't…
Trent Mick 00:50:01 I see the last comment at the bottom, Martin Hennik has a repro.
I haven't read the whole thread.
Marc Pichler (Dynatrace) 00:50:10 I'll actually just ask, the person that… by the… What report initially… And we can see if they… You'll see it.
And if they don't, then we can close this.
Right.
slash null .
topics here, we can move on to… PR triage… looks like more PRs in… A quarry will know.
Oh, I see that there's lots and lots of PRs with my, with my face on it. I should, get to these.
some point.
the first few… I think we're gonna skip over… There was this always record sampler.
Looks like there's been no movement on that one.
The CLO monitor thing… And ours will skip for now.
One had some failing limb to check.
I also need to get back to this here. I think I only made this change for logs, but we still need to do it for metrics and for… or traces… That's still open, I think.
Yeah, I'll just pull out the… changes from this PR and move them to two separate PRs, and we can go ahead with this. The main reason I think this is blocked is because right now, when you shut down, the… Ultra SDK were blocked for quite a long time, or the exporter shutdown were blocked for quite a long time.
Because it cannot reach an auto collector or something like that, if… if it can't access it.
So there's… quite some delay. So if we make better use of the retry timeout, we're just… do that for longer, which is probably not a great experience for users, so I think we need to do that first.
Make sure that's all sorted out.
And then, we can go ahead and… actually makes better use.
Trent Mick 00:54:20 Do you…
Marc Pichler (Dynatrace) 00:54:20 the replay time out there.
Trent Mick 00:54:22 You had a PR for that somewhere, didn't you, that I…
Marc Pichler (Dynatrace) 00:54:26 I think I…
Trent Mick 00:54:27 reviewed and I haven't… I haven't gone back to you in ages, so you're waiting for something on me?
Marc Pichler (Dynatrace) 00:54:31 I think that was that one that's already merged. I just had this draft here, Because I went through all the SDKs and fixed the bug there, and then also made some changes to the exporters, but it was… quite large and unwieldy of a PR, because it… it's not that many lines, but it's very dense of a change. I just wanted to split that into… different PRs, so that it's a bit easier to review.
Technology.
Trent Mick 00:55:06 So… Back to the previous tab.
No, go to the left in your tabs.
Dope.
The one that we're actually reviewing, not your… Okay.
Marc Pichler (Dynatrace) 00:55:23 Oh, yeah.
Trent Mick 00:55:23 this guy. Is that something we want now, or what's… what's next on the…
Marc Pichler (Dynatrace) 00:55:29 Retries.
Trent Mick 00:55:30 And… handling shutdown.
Marc Pichler (Dynatrace) 00:55:32 Yeah, I think we want that, we just want to make sure that it doesn't make other problems worse.
By merging it. So, if we would merge that now, if there is, for example…
Trent Mick 00:55:47 And the really slow shutdown problem, because it's going to sit in this retry loop instead of shutting down quickly yet.
Marc Pichler (Dynatrace) 00:55:53 Yep.
So… I think…
Trent Mick 00:56:09 Like, if the answer is yes.
Marc Pichler (Dynatrace) 00:56:10 need to…
Trent Mick 00:56:10 You need to get back to this at some point, that's cool. I just don't know what to…
Marc Pichler (Dynatrace) 00:56:14 Yeah.
Trent Mick 00:56:15 the next plan is. Or…
Marc Pichler (Dynatrace) 00:56:16 Yeah, so the next plan would be to, merge the three PRs that I'm gonna spin off the draft PR, and then, get to this one.
Trent Mick 00:56:30 Gotcha.
Marc Pichler (Dynatrace) 00:56:34 So… because then we also have tests in SDK node to make sure that it shuts down in time, which would be helpful to prevent these things in the future.
Alright, and… is… Here, here is some optimization.
on TraceState serialized.
David Luna Bistuer 00:57:03 Yeah, but this was completely changed by me. I don't know if this, applies anymore, so maybe there is a… a path to also improve this, but I changed the logic almost completely, so… So for sure there are conflicts here, so…
Marc Pichler (Dynatrace) 00:57:24 Yeah, I think I also put a comment here saying that if they're interested in picking this back up, Good. I think you… Didn't move the… Optimizations that… This contributor did to… your PR, right? If I recall correctly, the logic mostly stayed intact, but then… It's just delayed until it's actually needed, right?
David Luna Bistuer 00:57:59 Yeah.
Marc Pichler (Dynatrace) 00:58:03 Alright, then, there's also nothing to do for this one for now.
there might still be some… Potential for improvement, but not sure yet.
And this next one is… migrating from… TSC to TSTown, and to our… such as ESM experts.
That's actually an interesting, bing.
Would we want to do that with 3.0?
would be perfect.
Trent Mick 00:58:52 Because it's breaking?
Marc Pichler (Dynatrace) 00:58:54 It might be. We don't… I don't think it is breaking.
Trent Mick 00:59:03 It has the letters TS in it, so it might be breaking.
It's kind of the fear with which I approach these peers, but… I'm just trying to get David to laugh, that's my only goal here.
Oh, no.
Marc Pichler (Dynatrace) 00:59:19 Yep.
Trent Mick 00:59:19 Excuse me.
Marc Pichler (Dynatrace) 00:59:20 Right.
David Luna Bistuer 00:59:20 Amazing.
Trent Mick 00:59:21 I mean… We've, like, we've had this thing lingering for a long time, and… Jared… Does a good job, usually, so, like, and it's coming from the browser side, so, like, if it's got… browser folk stamp of approval, like, it seems like a potential glorious… Chance, sorry.
to do it, so… Yeah, sleepy.
Marc Pichler (Dynatrace) 00:59:45 If, for 3D, though, we manage to get pre-releases out.
And we merge this in, we can test it out in, like, a low.
David Luna Bistuer 00:59:58 That's interesting.
Marc Pichler (Dynatrace) 00:59:59 impact, we.
Which I would prefer for a change this large.
David Luna Bistuer 01:00:08 Hmm.
Marc Pichler (Dynatrace) 01:00:09 And then there's also maybe a benefit of upgrading to 3.0, for paper.
That will help them move to 3.0 a bit quicker.
Raphaël Thériault 01:00:22 Oh, I added to that.
Trent Mick 01:00:24 must.
Raphaël Thériault 01:00:24 For a second, but I will happily go through the review cycle on that one.
Trent Mick 01:00:31 Sweet.
Marc Pichler (Dynatrace) 01:00:32 Nice.
Right, I think you're…
Trent Mick 01:00:35 I put it on the milestone for now, if we baseplant and can't take it for the milestone, so be it, but let's try.
David Luna Bistuer 01:00:42 I'll mention it tomorrow, then, in the processing.
Marc Pichler (Dynatrace) 01:00:46 Nice. Alright.
Sounds good. I guess we're out of time already today.
Thank you all for joining. Thank you. See you next week.
David Luna Bistuer 01:00:59 Yeah. Thanks. Bye.
Pranav Sharma 01:01:00 Thank you. Bye-bye.
Marc Pichler (Dynatrace) 01:01:01 I mean?
