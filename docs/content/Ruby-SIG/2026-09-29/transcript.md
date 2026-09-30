SIG: Ruby SIG
Date: 2026-09-29
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Matthew Wear (Dash0)** 00:51 Pain.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 00:54 Hello!
**Matthew Wear (Dash0)** 00:57 How's it going?
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 00:59 It's going okay.
How are you?
**Matthew Wear (Dash0)** 01:02 Not too bad.
I think Caleb will not be here. We can hang out for a little bit and see See who shows up.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 01:16 Yeah.
**Matthew Wear (Dash0)** 01:27 It looks like you were at this past meeting.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 01:30 Yep, it was, it was mostly, Ted joining us to talk about, some things that had been brought up at the SPEC SIG last week.
Most, in the theme of, auto… well… Auto instrumentation. The packaging SIG's auto injection.
**Matthew Wear (Dash0)** 01:51 Yeah.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 01:52 Wishes.
So in… in, I had talked to him about how we had, we had that nice survey of where the, implementation gaps are for metrics and logs, and… and he had said.
Would… The C++ bindings help.
Like, if we were to… have an option in the SDK, in the… I guess it would be SDK. Maybe the API. Both. Of wrapping C++.
basically doing C extensions to be able to piggyback on implementation that already exists.
I'd said that probably wouldn't solve it for all of the users, because there are many people out there who don't want to do C extensions.
And it would probably be a blocker for auto-injection, since… Unless we all… unless we also took on producing, you know.
Builds. And not just libraries.
It was a wide-ranging discussion of, possibilities of the future.
**Matthew Wear (Dash0)** 03:04 Cool, yeah, I saw the notes here.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 03:06 Yeah.
And he was also just, stopping by to, to touch base as our.
Our GC rep.
**Matthew Wear (Dash0)** 03:24 Death.
Poof.
Well, I'm gonna share my screen. I guess we can get started if more people come.
They can come. I do have to… Leave at… by 1030, or by half past the hour. Okay.
So, we'll see how long this goes.
But I may have to hand this off.
If it is going to extend.
We have a nice and empty agenda, so we should be able to get through this pretty quickly.
Feel free to add things if you have anything. We'll just take a quick look at the SIG SIG.
There is… this Security SIG?
And a draft of security levels.
ultimately, I think… The idea is that there will be that each kind of open telemetry project should declare their level of security.
If you don't, you're undeclared, which is the least secure.
But… Above that, you have low, and then you kind of have the, criteria for low… Then you have my…
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 04:52 It's like the project management of a particular repository and who contributes and whatnot, not the… Not what we… not really about what we produce, but how we produce it.
**Matthew Wear (Dash0)** 05:06 It's… Kind of… It… it touches on some of those things. If you go up to, like, medium, I guess, like.
Kind of how long you take to… Address advisories, or address, like, vulnerabilities.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 05:22 Yeah, I'd still categorize that as a… How we do things.
**Matthew Wear (Dash0)** 05:26 And then high tells you how you can release as well, like, I think.
I think both of them tell you a little bit about how you can release.
Oh.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 05:40 Okay.
**Matthew Wear (Dash0)** 05:40 But at any rate, this is something that will probably come along at some point, and we will have to… pick a level, And… stick to it, and I think… From what I was hearing, like, medium is kind of the target.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 05:54 Okay.
**Matthew Wear (Dash0)** 05:55 So…
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 05:58 This seems reasonable, goal to shoot for.
**Matthew Wear (Dash0)** 06:04 Yeah.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 06:04 Devil's in the details, but yes, our stuff should be… Secure.
**Matthew Wear (Dash0)** 06:09 Yep.
Other stuff, I mean, we did talk a little bit about C++ and a CABI for.
for OTEL generally, like, are people interested in this? And.
And I think, in general, people are interested in this. I think, like, Alex was saying that he… Did a little bit of work.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 06:38 Yeah, there was a… he did an experiment with Python in, trying to improve context manage… just, like, memory and… and context… the memory involved in doing context management, the… the context stack, and… and lifting more and more from C++ for its.
More streamlined memory use, and… Better performance.
**Matthew Wear (Dash0)** 07:04 Yeah.
Yeah.
So he was saying he tried to kind of do a little bit of that with Ruby and with Node.
And… Saw very mixed results compared to what he saw in Python.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 07:20 Okay.
**Matthew Wear (Dash0)** 07:21 So.
So we'll see if this starts getting traction, and if…
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 07:27 It's intriguing to be able to, like, just wrap a single thing that performs well, but I'm intrigued by the promise.
I.
**Matthew Wear (Dash0)** 07:38 Yeah.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 07:39 Again, there's lots of devils in the details, but…
**Matthew Wear (Dash0)** 07:42 Yeah, I think the devils that end up in the details is that you have to create, like.
a lot of objects to kind of, like, pass that FFI barrier back and forth, and those sometimes end up being more expensive than, you know, the thing that you're trying to optimize.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 07:58 Yeah.
**Matthew Wear (Dash0)** 08:00 And, and yeah.
So Nevertheless, like, I do think this will probably be a thread that, that… Open telemetry kind of starts.
Starts going down a path, they start going down, and just seeing what, what a common kind of, like.
Like a Lib Otel, kind of… Native library would look like, and then, potentially what… Most likely, the dynamic languages could… Could do with those.
not really related to us but semi interesting there is like a collector RFC for kind of their proposed V1, so if that stuff interests you, take a look at this.
Oh.
Other than that, I don't think there's… I think we covered most of it.
Boom.
which brings us to the empty agenda staring us in the face.
Is there…
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 09:20 It's an opportunity to fill it.
**Matthew Wear (Dash0)** 09:23 is.
Of?
I was just gonna see, is there, like, anything… anything on core or contrib that, we should look at that needs attention?
Boom.
I was out last week, so I'm just… getting back and caught up on stuff this week. I did see Xuan that you opened quite a few metrics.
PRs, which I, hope to start working through shortly.
I will say that, yeah, I was kind of… Last time, talking about how we could, how we can make the metrics and logs Apis available to our instrumentation without Oh.
Carelessly exposing them to users.
and and I had some draft Prs up. I close those drafts, and I have Chunked this up into, into the actual… kind of Prs, I think, that we need, and kind of went through the Bob's.
I guess… thought through, like, the release sequencing, and I made this, this issue, and… I guess one thing that I did find.
That was unfortunate when actually kind of going… going through the details, was that our, Our… our SDK, kind of, Pins only at, like, a floating minor version.
Which means that any existing SDK out there will take anything less than 1.0.
And… When you, and basically, like, a lot of this work is kind of… Hiding those globals… making the making the globals like the logger provider meter provider. Not available to users just by requiring the Api, because that's kind of the The… the issue today is, like, as soon as you require the API gem, those globals become available, and it looks like you can use these things for the users, and that's what we don't want.
So the changes that I had was that the… Thumbs.
Requiring the API give you access to the, kind of, the API, Oh.
the API objects that we need, but I didn't wire them up as globals, and then requiring the SDK will actually, like, wire up the globals. That's kind of like your opt-in.
So… Oh.
So… so…
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 12:18 And that's… and that's… and that deviates from the, like, a stable like, what a stable API would do, it would give you… it would give you a real global… it would just be no op.
**Matthew Wear (Dash0)** 12:33 Yeah.
Yeah, and and we will give you a.
We will give instrumentation kind of a global no-op, but it's kind of, It's… It's on the OpenTelemetry internal.
Module, so it doesn't look like it's available to the user, if that makes sense.
Oh.
It's on OpenTelemetry internal, so that's kind of how our instrumentation gets access to a.
a global logger provider or meter provider, and it will be no-op if you aren't using an SDK, but if you are using an SDK, we will.
It will delegate to an actual SDK.
But because these are kind of in a different spot, they don't look like they're something that a user should be using.
Shame on the user who uses something on OpenTelemetry internal.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 13:34 Like, it's, it's got the warning right there. Yeah.
**Matthew Wear (Dash0)** 13:37 And it's API private. So that's kind of the idea behind a lot of this.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 13:43 So the, the, the issue, I'm a little behind. The issue is, if somebody requires the current Logs API gem.
Which is… Not the OTEL API gem.
**Matthew Wear (Dash0)** 14:01 This happens. The stuff in red happens.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 14:03 Oh, I see. Okay. The, The latest release of the Logs API gem still puts something in the global module namespace instead of under that internal.
**Matthew Wear (Dash0)** 14:15 Yep, so as soon as you require the logs APIs, it kind of… the cat is out of the bag, and it looks usable by users.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 14:23 Okay.
**Matthew Wear (Dash0)** 14:24 So, the idea is just put this in this global file, requiring… and the global file, for now, wires this up, on internal.
or it delegates to internal and then If you require the SDK, the SDK… will, The SDK will require the global.
So the SDK is kind of the opt-in for, setting up the, the… Logs, global.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 15:07 And the problem that we're trying to solve here is the, communicating Through the module namespace, the… Not stable nature of the… Of the logger?
**Matthew Wear (Dash0)** 15:22 Yeah, I mean, ultimately, the thing that we want to do is allow instrumentation, our instrumentation, to be able to use.
Boom.
The… Able to use logs and metrics.
Without exposing those to users, so that we can kind of dog food our APIs, and And we can kind of make forward progress on.
on actually, like, adding, you know, like, HTTP metrics and all these things to our, to our instrumentation.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 15:54 Okay.
**Matthew Wear (Dash0)** 15:56 so in instrumentation base you already get a tracer it's like now you would get like a meter and a logger And these would just default, you know, to no ops, but it allows us to actually, start using them, and.
Using them from our instrumentation, making sure that they work, making sure that they're ergonomic, and then if you actually wire up an SDK, you can, export, this experimental data from it as well, so we can kind of build build faith in our, implementations,
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 16:27 And it's that OpenTelemetry colon colon internal namespace that sort of communicates to a user that.
You shouldn't use this.
Exactly.
**Matthew Wear (Dash0)** 16:36 Exactly.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 16:37 And that's the problem we have today, that a logger provider or a meter provider will be available under the global open telemetry if we don't do this, and somebody might start trying to use it.
**Matthew Wear (Dash0)** 16:49 Yes. They might unknowingly think that the stuff is ready and start using it. So, like.
The internal module, this exists today, and we have a lot of stuff on it, actually.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 16:59 it.
**Matthew Wear (Dash0)** 17:00 in the SDK. So this is not a new module.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 17:03 Okay, so that we're… Prior art exists for this.
**Matthew Wear (Dash0)** 17:07 Yeah, Prior Art exists for us, and it has been, and it is API private. Okay.
so so this exists in our currently like you know 1.0 tracing SDK there's a open telemetry internal module.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 17:19 Okay.
**Matthew Wear (Dash0)** 17:20 Which has stuff that is hands-off to the user.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 17:24 Well, I figured that if we'd never intended to expose that logger globally.
Pulling it behind internal is, legitimate option.
Let's do it.
Why wouldn't we do this?
**Matthew Wear (Dash0)** 17:41 Yeah, yeah. So, So I think most people, when I presented last time, are on board with this. It was just… Thinking through how we actually need to, releases, and that, yeah, I think that was what I was getting to, is that I found out that because our SDKs… because our SDKs, allow them.
The minor version to float.
you can get this newer API version, where those globals.
Does it exist on the OpenTelemetry module?
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 18:16 So somebody who reached for these things earlier.
will break.
**Matthew Wear (Dash0)** 18:22 You can get some kind of a breakage. If you… if you upgrade your, your API, but not your metrics SDK. I don't know who that person is.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 18:33 You know? Yeah.
**Matthew Wear (Dash0)** 18:34 But like.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 18:35 Saveable.
**Matthew Wear (Dash0)** 18:36 But it's conceivable, and it is kind of fixable.
So that was the thing that is kind of new this week, from what I presented last time, is that… Is that… I was able to solve this with method missing.
And basically, if a logs SDK, that still exists. That yeah predates the global Oh.
Then, ultimately, when they try to call those, accessors, the… To assign, like, the global, or read from the global.
They'll get a no method error.
So we can, detect this with method missing, and then kind of wire up the global and then log that Log that you have a, older version of the SDK, and that you should and a newer version of the Api. And you should update your your SDK.
To match, and then everything will be fine.
And then, going forward, You know, with newer releases, we will pin the, We'll pin the… Oh.
the API more closely, like, at a patch version, so that you don't get into this situation where basically anything that's not 1.0 actually satisfies your requirement, because that's the main…
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 20:16 So there'll be, like, a minimum and maximum.
From a minimum patch level, Up to less than 1.0.
**Matthew Wear (Dash0)** 20:27 Yeah.
So… So this is just, like, a temporary patch that we would have, presumably, you know, until we actually 1.0. We could remove it earlier, like, once.
once these more tightly pinned API, kind of SDK, combinations have been out there for a while. That would be another point in time that we could remove this, but… Okay. This was a way to, like.
this was a way to kind of ensure that we don't break people. Sure. And we don't necessarily need this. Like, we're kind of going out of our way here, because these are.
experimental packages to begin with, and we could just break people. That's, like, also an option. But I added this because it was easy enough.
Oh.
Okay.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 21:16 I'm okay with breaking people, which is where many of my questions were coming from, but, something that makes the breakage Less bad.
It's good, and it's already implemented, so…
**Matthew Wear (Dash0)** 21:28 Yeah, that was kind of my thought. If we can not break people, and it's sensible, we should do that. So that's kind of… That's what I did, and that's kind of what, what these PRs do, and then the… Bob.
This issue describes how this will all kind of play out, and.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 21:48 So, if we got approvals on that one, do you think we could merge it soon, and then follow through with the… The release sequencing here soon.
**Matthew Wear (Dash0)** 21:59 Yes, yep, so there's, there's that PR that we were just looking at for loggers, and there's a PR for metrics on core. Those have to go.
Well, those kind of… those touch the SDK and API for each one of those. Those would go.
Then we need to.
we kind of need to release the API gems first, and then bump the SDK's PIN, and then release the SDK's, you know, right after that, kind of, you know, same day.
And then we kind of have this PR that, That depends on those, because, Oh.
This updates base base will need to depend on that new version of the API.
And then.
After that, then we can update our instrumentation to use the new base, and then all instrumentation from there on forward can get access to a Boom.
meter or logger.
We can start using our Apis from there.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 23:12 I'm happy to review these things. How do I find them again?
**Matthew Wear (Dash0)** 23:17 So, If you want to find them.
I feel like the best way is through this issue.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 23:26 2413.
**Matthew Wear (Dash0)** 23:27 Yeah, 2413.
Drop that in the chat, at least.
And I think… Yeah, I think you will find these all linked down at the bottom.
All right, so I have five-ish minutes left.
Any questions about this process at all?
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 24:01 Nope, that makes sense.
**Matthew Wear (Dash0)** 24:04 Anything that we… Did want to go into more detail on, core or contrib?
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 24:22 No. On Contrib, there was the PR to, do things with dev containers that was… it's been open for several months. I had a.
conversation with Oh, gosh. Names.
**Matthew Wear (Dash0)** 24:38 Thompson Tunnel?
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 24:39 Yes.
About, like, what problem that's solving. And I… I think I'm on board. It's sort of a matter of getting the.
There's an issue that he opened related to this, and then a series of Prs mapping back to it that could maybe just use more words on it about what the problem, as I understand it, this is an attempt to put the development environment into CI, so that we will Exercise, the development environment.
through the CI test suite.
Sort of like a… Feed two birds with one scone situation.
It's a lot of changes to review, but I think I agree with the spirit.
Of the problem to be solved, but if you're gonna open up the dev environment to work on this stuff. If the dev environment also provides some of the gets exercised in Ci, we'll know if the dev environment's broken.
That's the quick, what problem is attempted to be solved here. I haven't reviewed yet that this solves that problem.
But if we agree, that's a problem worth solving.
We could move forward with moving on.
**Matthew Wear (Dash0)** 25:53 All right. Yeah, I need to look a little bit more at this as well.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 25:57 I'll… I'll add a comment to this PR, with the link back to the issue that he had said that he had opened.
**Matthew Wear (Dash0)** 26:07 Okay.
Yeah, that would be helpful.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 26:10 Once I find it.
Okay.
2318 is the issue that was opened.
Wow.
It got edited recently.
the Okay, there's a lot more content on that, on that issue.
2318.
**Matthew Wear (Dash0)** 26:32 Okay, cool.
Useful, useful to know, so…
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 26:37 Yes, that explains the… what the problem is, and… That was good, so…
**Matthew Wear (Dash0)** 26:46 Cool. Anything else you wanted to chat about while we're here?
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 26:53 Amen.
**Matthew Wear (Dash0)** 26:55 Cool, yeah. I guess my last thing is I… I will start looking through your metrics PRs, Schwan, probably.
try to, you know, look at one or two a day, until I make my way through them.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 27:14 I'm happy to look at them, but metrics aren't my strong suit, so…
**Matthew Wear (Dash0)** 27:20 And those are all the promises I'm gonna make that I probably won't be able to keep for this week.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 27:27 Stan.
**Matthew Wear (Dash0)** 27:29 All right. If there's nothing else. Yeah. It's good to see everybody. And.
I will see you around on Slack, and… probably… had a SIG meeting, In the near future.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 27:42 Okay.
Be well, everybody.
**Matthew Wear (Dash0)** 27:45 Alright, bye.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 27:46 Bye!
