SIG: JavaScript SIG
Date: 2025-11-12
Duration: 61 minutes
============================================================

## Zoom Recording Transcript

**Marc Pichler (Dynatrace)** 00:47 Hello?
**AA Abdelrahman Awad** 00:53 Nope.
**Hector Hernandez** 00:54 Aye.
**Marc Pichler (Dynatrace)** 01:19 Alright… Welcome, everybody.
Let's get started. The first topic here is, Avat,
About exposing internal asynch locally storage.
We want to say a few words about this?
**AA Abdelrahman Awad** 01:42 Yeah, so we started experimenting with, using tracing channels, which used
Diagnostic channels under the hood.
to… emit the… Tracing events that we can use for instrumentation,
monkey patching stuff. So, what we noticed is the OpenTelemetry context gets lost, between the start event and maybe, like, something like a sync event.
Which means it wouldn't work well for…
Creating child spans and stuff like that, so they would get created as siblings, rather than, children of one another.
So…
Yeah, I found a way to do that through the grabbing the async local storage, which is an internal property on the context manager, and binding it to the start channel, which is down there in the code somewhere.
Yep, so…
And that works well for our use case, and the context is propagated correctly throughout the events.
So, what we would like to discuss is if there is a possibility to either expose the async local storage.
For use for stuff like this.
or exposing a public API that would, prepare a tracing channel, since it's a Node.js API.
for context propagation, so that any provider, like Sentry or others, can use it to basically use tracing channels for auto stuff.
That's all.
**Marc Pichler (Dynatrace)** 03:25 H.
Yeah, I think I had a look at this one, already before. Thanks for providing all that context, and I also had a look at the repo that you linked here, so that was, very helpful.
I think in terms of the two options that you brought up, we would likely go
About it at the… We would probably pick the second option, because exposing the,
Basically, local storage is… not something that, we would be comfortable doing, probably.
I wasn't around when this part of the code was added, so I also am kind of digging into that for the first time.
So, I'm running as I go.
But yeah, it would be great to have something like that to make that happen somehow. So, I think what we need to do is to figure out how we can either use existing APIs to kind of make that work.
Or, find some workaround as to,
as the package that you, for example, provided us, with accessing internal properties and stuff like that, to make that happen in the end. But…
Yeah.
it's, likely going to take some time until we've figured out how to, properly do that. As always, like, super simple examples, usually help.
for, like, conveying that message. So if you, for example, can come up with an,
Something like the example that's used in…
our docs on OpenTelemetry I.O, where, you would split out, let's say, a dice roller,
Library or something like that, that's being instrumented with tracing channels, and use that as an example.
that people can take and run and see how things would work. I think that is, something that, would accelerate the whole thing.
Because then everybody can jump on that and use, like, a very simple example to see how tracing channels are used to instrument stuff, how Otter would hook into things, and then there could be a third actor, like I mentioned here, where,
I don't know, that does something different, with this sort of information, and then we can make an informed
decision about what we're gonna expose and where. Because with these sorts of things, it's very difficult to,
add stuff to the API package, where, like, you know, it might work with the async local storage context manager, but it might not work with other context managers.
So we want to make sure that
we're doing the right thing there.
once we add that API there, we're likely going to be stuck with it forever. So there's a high level of scrutiny that needs to go into, adding such a thing.
yeah.
I think overall, the… feature that's being proposed is a good idea. We just need to…
figure out the details on execution. So, yeah.
**AA Abdelrahman Awad** 07:18 Okay, should I add, like, more examples in the issue, and…
Wait for more people to discuss this, or…
**Marc Pichler (Dynatrace)** 07:26 I think that would be helpful, yes. You already provided a bunch of examples, but what's mostly interesting for us is,
how it's gonna work with Ulta, right? So, if…
I suppose the idea would be that sentry stuff is decoupled from whatever Autel is doing, so it would be great to have an example like that, and also experiment a bit with,
Where this band is going to be started, if that's immediately on this bind operation, or if that can be deferred to something later on.
would also be interesting to see.
**AA Abdelrahman Awad** 08:07 I see. Can you open the package link, sorry, quickly?
**Marc Pichler (Dynatrace)** 08:13 This one here, right?
**AA Abdelrahman Awad** 08:17 Yeah, because I think it kinda does that, source…
Yeah, I think that's enough, but… Doesn't matter, no.
So, yeah, it's… it doesn't use anything centrally related under the hood, it just grabs…
the available API from… Autel, and binds it to the channel, and that's it, and then…
Like, the Sentry stuff is actually, like, the third-party listener.
Not the package itself.
**Marc Pichler (Dynatrace)** 08:49 Yes, so that's using the…
**AA Abdelrahman Awad** 08:52 Yeah, it's the previous notes, yeah.
Yep.
**Marc Pichler (Dynatrace)** 09:01 Yes, so,
cow.
**AA Abdelrahman Awad** 09:12 The implementation itself is simple, it even uses the span.
Hotel spend type, like, nothing external at all.
**Marc Pichler (Dynatrace)** 09:19 Yes.
So that's dead here.
**AA Abdelrahman Awad** 09:24 Nope.
So it takes a channel name, and… or a channel, and…
It assumes you're gonna return a span, otherwise…
Wouldn't be able to grab the context.
And from there, it just propagates it.
Yep.
**Marc Pichler (Dynatrace)** 09:41 Yeah, I think that that arm makes sense, the way that it is right now.
I think… so, what I'm saying about examples is that, people, when deciding about how to add stuff and where people usually like to, you know, run something and, see it in action, and then, like, go step by step and see what's happening, and then,
like, work backwards from that to decide, is there any other way that we could do it, like, explore other ways to, to accomplish the same thing, and then, make a decision about how to add it. So…
Especially with, like, more complex stuff like this one, it is… can be helpful to have some sort of a runnable example, that's…
Like, just, you know, generating other spans, from a very simple operation, or a very simple library, that's being used there.
**AA Abdelrahman Awad** 10:38 Yeah, sure thing. I can try to do that and add the examples.
So, yep.
**Marc Pichler (Dynatrace)** 10:46 That's awesome, thank you. But, yeah.
overall, I think the… thing is going in… in the right direction, the,
Internalers are kind of what are…
In the way for us at the moment, which…
It feels a bit painful to do any sort of this thing.
**AA Abdelrahman Awad** 11:10 I think so.
**Marc Pichler (Dynatrace)** 11:12 We just need to find the…
elegant way to do it, I guess.
Alright, but it's a very interesting, idea. I…
It's, definitely gonna be helpful, when people adopt tracing channels to also be able to instrument that. This is going to be… it's going to simplify auto instrumentations too, so I'm kind of excited for that.
**AA Abdelrahman Awad** 11:44 Yeah, we are as well. Thank you.
**Marc Pichler (Dynatrace)** 11:48 Alright, thanks. Does anybody have any questions, about this here?
there's no questions. I urge everybody to have a look at this issue.
And, yeah, if you have questions, then, please just post them on the issue and, start some more discussion there.
probably, like, if we're gonna do that, it's likely gonna shape quite a bit of how instrumentations are going to look like in the future. So, it's good to have as many eyes on this one as possible.
Alright.
As if there's nothing to add for this one, we could move on to the next topic.
Mozilla.
**Marylia Gutierrez** 12:42 Yeah, so this one, I was just wondering, because I saw, like.
even, like, on Hacker News, people talking about just general performance of hotel instrumentations, and I see we have a couple PRs that people are opening for, like, improving performances, like, here and there. Do we have anything, like.
more concrete on…
testing to see, like, which areas we could focus on improvement on performance. Is anything done on this? Kind of like this topic in general?
**Marc Pichler (Dynatrace)** 13:13 I don't recall any specific issue tracking any of that.
There are a few, benchmarks that we run, but they're very simple. Like, creating a thousand spans or something like that is the,
one of the things that we do, and there's graphs published to OpenTelemetry I.O,
I think there's some benchmark data somewhere where you can see commit by commit, how things change over time.
so… that's…
One thing that exists right now, and for all the performance improvements, of course, the first step would be to add more benchmarks to make sure that,
once there is a PR that claims to improve performance, we can actually verify that easily.
So… any issue regarding to initiatives about performance improvements, I think should start there.
And then, we can…
Iterate more quickly on any performance improvements of the sort.
there are a few places where,
things can be improved. I think…
One of the things that's happening quite a bit is we just create a lot of allocations, everywhere, which then,
Yeah. Makes the garbage collector take forever, to actually finish, so that's one of the areas where,
Things can be improved.
And then there's also the, OTLP serialization is a, like, huge part of the thing where a lot of, time is left on the table, where we could make a lot of improvements there.
So…
these are the things that come to mind, but that's definitely not an exhaustive list. A lot of the SDKs, they were written with
getting something out quickly in mind, and not really, performance. So…
There's a lot of bits and pieces here and there that can be improved.
So, long story short, I think there's no, like, initiative right now.
If there was an initiative, this is, like, kind of the corner.
stones that I would start looking into first.
**Marylia Gutierrez** 15:52 Okay, cool. Yeah, I can… I can create an issue just to have, like.
This somewhere, so when we have ideas, we can… add to it, Leah.
**Marc Pichler (Dynatrace)** 16:01 Yeah, I think that would be, already a good start, having an issue to track these sorts of things.
I'm also pointing out the need for, benchmarks and stuff like that.
Yeah.
Alright.
**Marylia Gutierrez** 16:23 Next one, also me. Yeah, that is something that…
other 6 brought up, so I'm kind of, like, sharing on this one as well. Because I don't know if anyone… everybody knows
the role, like, of GCE liaison, except for, like, maintainers. So, in case you don't know, like.
every single SIG has a GCE that is supposed to be the liaison for it, that they do check-in with the maintainers, but they're also there to help out
everybody from the SIG, so if you have an issue, feedback, or something, you can also reach out to the liaison of that SIG specifically, you don't have to be a maintainer to bring up topics. I can actually share the link for
every single one, in case you are curious about your own… on your other six, but the gist is for this one, now I am the liaison for this one. I just became for this one, so if you have any comments, feedback, feel free to reach out to me.
**Marc Pichler (Dynatrace)** 17:24 Yes, thank you, and congrats on getting elected to the GC.
**Marylia Gutierrez** 17:28 Oh, thank you.
**Marc Pichler (Dynatrace)** 17:36 Right.
Any questions?
Or I'm not really, on the… Chicily liaison topic.
flat, then I guess we could move on to… Hector,
The topic about ESM support and instrumentation hook expectations.
**Hector Hernandez** 18:05 Yeah, the reason I'm bringing this up is, like, we have several customers who are using ESM, they start getting issues with instrumentation, so they get to this support page.
And the… the question I have today is, like, if there's any plan
For these, hooks to be deprecated to, we actually support this without those?
Is that,
I'm not entirely sure what… how these hooks works, but it's just more about if we want to include this kind of documentation in our site, in Microsoft, if we want to include this
Extra stuff in the pre-assembled things that we create, or stuff like that, but we would like to understand what's the status of it, and if it's
Well, if it's going to be there forever, then we need to start, integrating this better.
**Marc Pichler (Dynatrace)** 19:07 Yeah, so, I think Trent…
Opened an issue, some time ago, to look into having registration of that.
book happen in, I think somewhere in the instrumentation package, or on setup, so that you don't need to specify it explicitly.
**Jamie Danielson** 19:30 issue that is linked there? Do you see at the bottom in the additional notes on it?
Additional notes on experimental loaders, yeah.
**Marc Pichler (Dynatrace)** 19:38 This one here, my…
**Trent** 19:40 Yeah, there's an issue there, it's kind of… is my audio working?
**Jamie Danielson** 19:44 Yes.
**Trent** 19:45 Yeah, that issue's there, it's kind of languished for a long time, so…
Hector, some of us have been discussing recently about getting focus topics up again for what we want to focus on. This is maybe potentially one that we want to consider as well.
Though I know we'd been thinking about other things,
Yeah, I think the first step is to…
Or a first step is to do that issue, where we call the,
the module.register, I think it's called.
inside… in code, so that could…
I mean, I guess for now, it could be in the register.ts call that,
In auto-instrumentations node, or people doing the equivalent.
I'm documenting doing that.
And then there was the other issue to go through…
doing, I think it's called First Pass, or something like that, on…
Making sure each of the instrumentations support
They work when they're called from ESM code.
It would… Hector, I guess it'd be interesting to get from your customers which modules they were…
Having trouble with, or particular details?
To help focus on which ones we want to work through.
And then, like, I could get you
started if you wanted to be picking off particular modules, or if it's some other issue.
One thing that's contributing to… I guess, maybe ironically making…
A bit harder to make a call on moving forward is,
we'd kind of settled on record in the middle and then import in the middle, but there's, the orchestra and work that's coming along in the tracing channel, so, I mean…
evidenced by… the Century discussion earlier, because I think Century's been working a lot on the orchestrian stuff.
So, there are kind of a number of things at play there.
I'll shut up now, because my audio probably sucks.
**Hector Hernandez** 21:36 That's good. Thank you very much, Trent. I'm glad to hear that there's… this is happening, right? Yeah, I'm happy to share customer details, and we'll take a look at this… this issue.
On that detail, sir.
**Marc Pichler (Dynatrace)** 21:53 Yeah, so to answer your,
question somewhat directly. I think we want to move away from this, like, having to load a hook. And ideally, we would have something like this, where it just…
works without you having to do anything. That's our ideal, way forward. But the way…
To get there might be a bit more bumpy than, we would like. So, yeah.
That's… that's all I have.
**Hector Hernandez** 22:31 Cool. Thank you, Mark.
**Marc Pichler (Dynatrace)** 22:33 And if anybody wants to look into that,
Of course, please feel free to…
do so, and share your findings on the issue here.
So, we can move forward with this.
Alright.
any… Questions or comments about this topic right here?
If there's… No comments, and also no…
other agenda items, then I guess we can move on to bug triage.
As always, if you have something that you would like to talk about while we're doing bug triage, please feel free to just interrupt me.
And we can go back to the agenda here and talk about your topic.
Alright.
In the core repo, looks like we don't have any new bugs here, so that's great.
In the country repo, we have quite a few new ones here.
There's one…
AWS SDK instrumentation, not applying patch.
There seems to be…
Looks like there was some discussion in Slack, and
there's some… suspicion that… Require in the middle… 8.
It's causing this patch not to be applied, won't have… enough insights, I think, to…
make a definitive call that this is actually the case or not, but…
**Trent** 24:53 I think in Slap, the… the…
person who opened this ticket said that they were going to come up with a smaller Lambda example repro.
**Marc Pichler (Dynatrace)** 25:01 Which might help.
**Trent** 25:03 It's possible that something will require in the middle, but I'm also not sure that the person's not using ESM here, so it might be something totally different.
So I think until we get that repro, it's kind of hard to tell.
**Marc Pichler (Dynatrace)** 25:16 Alright, thanks. I think I will put the P2 on here for now, because it's… Bye, though.
Incomplete telemetry or incorrect telemetry. And if it turns out that,
This is… If it turns out that,
it's actually just a ESM issue, and can be served in another way, then we can just close this as served.
Otherwise we might need to dig into it a bit more.
So, I'll put these on here for now.
I'm returning.
Continue looking into that.
One time. Alright, this one I assigned to myself, last week.
And I probably also said I was going to…
Follow up on it, but fell off my radar.
Alright, I was thinking that this might be an issue with… the Firestore instrumentation…
I don't want it to ping, was it Aaron?
Have a look.
So I will do that this time.
Actually, and…
This is the same person. I was confused there for a bit.
Alright, this is instrumentation, runtime, node time series errors when trying to send metrics.
This was the one that I pinged also Aaron on,
It looked like this is not actually an OpenTelemetry issue, but should go into… This repo right here.
So, I guess there's nothing to do for these issues right now. So we can move on to…
looking into old PRs. Actually, since we have more PRs in Core right now than in Contrib, let's start with…
this one right here.
First one is on Lord PR about…
adding a delegating node meter provider, which I think was blocked on Barcelon meeting.
Proxying of instruments, otherwise it wouldn't be too… Excellent.
And it looks like nothing has changed on this one yet, so…
**Hector Hernandez** 28:47 Yeah, sorry about that. I lost this one from my radar. I did have some changes for the proxy instrument stuff. I will… I will take it back and send it.
I just forgot about this one, but yeah.
**Marc Pichler (Dynatrace)** 29:02 Yeah, that happens.
**Hector Hernandez** 29:03 It's, it's.
**Marc Pichler (Dynatrace)** 29:06 From a long time ago, so, yeah.
But would be very much looking forward to the changes here, because every once in a while, people are still running into that.
**Hector Hernandez** 29:16 So.
**Marc Pichler (Dynatrace)** 29:17 Yep.
**Hector Hernandez** 29:18 Yeah, we have some niches in our site as well, tracking this. Okay, yeah, I will.
**Marc Pichler (Dynatrace)** 29:22 Thanks.
Alright, the next one, that one's actually blocked on some more changes in API logs, so I will skip that one.
Oh, question to you, Hector. Would it be okay if we convert it back to draft for now?
**Hector Hernandez** 29:46 Whatever works for you. Just let me know when this is ready, I can take it back.
**Marc Pichler (Dynatrace)** 29:51 Yes, I think I can't make that a draft, but you could.
**Hector Hernandez** 29:58 Yeah, I will make the change right now. Yeah.
**Marc Pichler (Dynatrace)** 30:00 I will, ping you once it's ready.
Once we are ready to, actually do this, there's actually not that much left.
Or, API logs to… be considered somewhat complete. We have
Where is it? This,
SDK and, API blocks, Milestone, and there's…
Just one thing to remove, this…
proxying logup provider from the exports to make sure that people aren't using it for other stuff, and minimize the API surface a bit. That's kind of blocked on some changes in tests, and there's a few other things that are,
Yep.
Shouldn't be too much work.
But… yeah, once all of these things are done.
we'll be able to request a review of the API and the SDK from the TC. I think that's how it usually goes. And then,
We can, formally move to… blocks things to Stabor.
**Hector Hernandez** 31:21 Yeah, glad to hear that this is making progress.
**Marc Pichler (Dynatrace)** 31:27 Yes, also looking forward to it, because it will unblock a few other things that we can stabilize as well. So, that is…
So, if anybody has time, feel free to…
hop, hop on over to the milestone and, pick up some work there. It will definitely, make a…
big impact.
Working on these things.
Alright, this one is something that…
I had opened a long time ago, and it's actually approved, but I didn't merge it yet, because, there is some,
problem with Webpack 4 and entry points that it just doesn't like it, but there's another PR open right now that adds a test for Webpack 4.
Where we will be also able to direct people to a Webpack config that they can use to make it work.
So… Yeah.
I'm not entirely sure yet if we want to proceed with
dead or not, but also if logs are stable, then, I can address the comment that,
David had here.
With not having the log stuff hidden behind a, like, slash experimental entry point.
So I'm gonna keep that open for now, and see…
How things progress, are also marked as dropped.
Those stairs.
Nothing to… immediately do here. It removed that forward. It's just locked in some other things.
Then we have a draft that is the entity's prototype. There's also nothing to do for that one, if I understand correctly.
So, we can skip that.
Bum… And we have… This is one of the…
things that are pending for, the logs API and SDK to become stable.
So, we need to make sure that
Any circular references are properly handled for any value attributes, which are complex attributes.
And…
that's not fully done yet. The main change this one needs is that the implementation code for attribute validation should go into the SDK package, not the API package.
yeah, it seems that the person that initially started this PR, probably…
stopped working on this, so if anybody has time, would also be appreciated if you…
If you're interested in continuing that work,
It's one of the main blockers for… Lock stabilization there.
Alright.
This one here, I reviewed a while ago.
But all the tests are failing. Well, not all of them, but many of the tests are failing.
Or actually ping the person.
secure.
Oh, "… I'll bring them here.
That one's easier to see.
Alright, you can see… What the response is there.
I'm not sure if the advisory attributes are stable yet or not.
Or if anything has…
change in the spec since this PR was opened, so might also be worth looking into that.
I will assign this PR to myself so that it shows up in my assigned list.
Then we have…
PR, that's a breaking change for the P3 propagator, which is stable, which we probably wouldn't wanna,
picking it like that, so, the issue that they are having here is that D…
I think that the way we, and… Head us here in the… B3 propagator is incorrect.
Because we are not, I think what we're doing is we have This lowercase one here.
But… What seems to be happening here is that…
There's just some miscommunication.
going on, or, some other instrumentations, not instrumentation, some other SDKs are doing something different. I think they were having problems with the Swift
SDK, and they don't recognize when there's a lowercase
header in there, which they should actually
Allow whatever casing there is, since it's case insensitive, actually.
According to the Sipkin spec.
So, actually, this would have been closed by the stalebot, but… Still put weird things, so…
I'm also gonna assign this to myself and make sure that this one gets… Ghost.
Or, updated to match whatever they're trying to accomplish here.
There were also some changes to the fetch instrumentation.
So this is probably something that we need to address here.
Oh, wait, this is the test. This is also the test. So…
I guess there's actually nothing for us to immediately tackle here.
Right.
And this one exports the Shima function that we,
pulled into the OpenTelemetry instrumentation package.
this just exports it, but the comments here that I may…
Arch tool.
also deprecate these here, because people are usually confused when we offer multiple ways to do the same thing, and Open Issue is asking for the right way to do it, so having it
having that sorted out somehow would be helpful. And I guess there's also a question whether we want to
export.
She loved.
Like so, or if we just want to export the actual functions there, so the rep, mass rep, mass unwrap, and…
unrep functions.
I'm actually not sure what to do with this one.
I was a scientist to myself.
And I will ping them.
To see if there's any, movement, or if they don't wanna… Exactly that.
For some reason.
Would always be interesting to know.
And moving on.
I think this is actually a performance improvement, since we were talking about performance improvements before, this might be interesting.
It simplifies the parse… pair key value, function here from… The car package, which,
is being used quite a bit, I think.
This is for… baggage.
And stuff like that.
So, looks like Trent looked into this one.
The implementation shows same time or slower.
David also looked into it.
Ordinal 20, seems like…
These ones are…
Or better for the new instrumentation, and…
For the new implementation. I was trying to say.
I happen to have,
M3 MacBook, so I will also have a look into that one.
Looks like it's working better for…
David and the author, so… If there's a third person that wants… oh, sorry, David?
**David Luna Bistuer** 44:44 It depends on the location, I think.
**Marc Pichler (Dynatrace)** 44:51 I… I will also have a look at that one and see if I can.
**Trent** 44:56 You mean, like, Spain versus Canada?
**David Luna Bistuer** 45:01 Yeah, it's hotter here, so it runs faster.
**Marc Pichler (Dynatrace)** 45:06 Okay.
**Trent** 45:07 Really, you gotta back us up on the Canada one.
**Marylia Gutierrez** 45:11 And, knees and frills.
**Marc Pichler (Dynatrace)** 45:14 Yeah, Marilla, if you want to represent Team Canada here, you can also run the tests and see, what it comes out, for you.
I would,
I will run this, and will post my results, and if anybody else also has some time to just quickly, check the PR out and, run the tests, it would also be, great for you posting your results there, and then,
We can see if that was, maybe just a…
One time-off situation, or, if there's something deeper that we need to look into for this one, and then,
Yeah.
If we find that it's actually…
But I guess we can just merge this into changes, should be fairly…
barely serve contained here, so, review itself shouldn't take too long. I guess it's really just the…
Difference in, in the results that's… Kind of.
It's throwing us off here.
Right. Boom.
But yeah, I wouldn't just want to merge this one in, quickly, because I'm also intrigued to see, what's… what's going on there.
adding, Austria to the mix of, places where we can run the…
The benchmark and see if that makes a different… difference.
Then, here is… And not a PR.
I looked into that one yesterday.
So what they're trying to do is they want to export,
Fetch export delegate, which is basically just an internal use here, and…
A reason why they want to do this is…
I want to have some sort of a similar concept to…
I just keep life.
Stuff… And they weren't happy with XHR or Sand Beacon.
Only viable approach.
was batch with Keep Alive enabled. So I think that's something that's, missing right now still, is to have some sort of, batch with Keep Alive, because
Right now, if I recall correctly, that is not…
that…
We have to export a piece…
Transport, fetch transport…
Oh.
Look at that.
So, if… This is a browser environment, and it does actually set to keep alive, so…
I'm just gonna comment here.
It is set to…
when… Or, in,
Carl's opening.
Alright.
I'm gonna put a needs author response on here.
And then we can see if they have a response here. There also seems to be some issue with,
ECCLA.
Stop.
In case they want to still do that, we need to look into that.
problem as well.
Oh, man.
And the next one is, experimental trace decorator support. This is something that Legendic has, so Shang Tsong has been working on this one, to just show that it is possible to have, this sort of
decorators?
To, like, start an active span on, like, your…
Class implementations and stuff like that.
This would go into the experimental entry point in the API, so if anybody has time to…
look into that, or review that, or give feedback on it. This could be one thing to make things a bit easier for folks that are instrumenting their apps, because then they wouldn't have to do a lot of management there, they would just
Say, like, start a negative span here.
And then… Do whatever things they're trying to do in their app, without… Needing to,
use the more complex API with the codebacks and stuff like that.
yeah, I think that's the gist of that one. I think it doesn't work with,
It says here…
does not support function declarations or expressions, it really just only is for class methods. So there's some risk that once we merge this, we'll get a lot of
Questions about why the other things aren't supported, and we should have some sort of a…
document ready to direct them to, why that is, if I recall correctly, that is because these… run…
I guess if you put these… decorates on there, they run… The very first…
Thing or something, and then…
that causes some issue, but I don't exactly recall anymore what that issue was, so…
**Trent** 52:44 I may… I may be wrong, but I don't think it's that. I think it's just JS…
decorators at the JS level, this isn't a no-tell thing, don't support functions. Tuple of functions, they only support class methods, which is kind of disappointing, because, I mean, JS is kind of more…
This may be my opinion. But functions rather than…
doing full-on Jabba, everything's a class kind of thing, so…
**Marc Pichler (Dynatrace)** 53:06 Hmm.
**Trent** 53:06 There's… there's an inherent limitation there.
**Marc Pichler (Dynatrace)** 53:10 Yeah, I wasn't aware of that. I haven't used these decorators too much, but that's a good insight, so…
I guess, in that case, if it doesn't work anyway, we don't need to document it too, which is nice.
Alright.
S. O.
What was I trying to say? Yeah, if that's a feature that any of you are interested in, having in Oter,
That's…
one example of how that would work. Then this one here is the next PR on the list.
the… locks.
filtering use case,
I think I was trying to, comment on this.
issue here, but I didn't, have the time to actually write down my thoughts here.
**Jackson Weber** 54:34 Yeah, I know we were attempting to, agree on an approach here. Last SIG, I believe we discussed, well, at least with the SIG,
I know folks hadn't had enough time to take a look at this, to make an informed decision on which direction it made sense to go, but I think that's still the standing status quo, so if folks could take a look at this, and, you know, just have opinions. I don't mind… I don't even mind which way they go at this point.
But yeah, I really appreciate your time.
**Marc Pichler (Dynatrace)** 55:08 Yeah, I will take another look at this one,
Dope.
at this point, I think, maybe we just…
walk back to the, logger configurator approach and do that, have it marked as experimental for now.
And, be spec compliant, and once the spec changes, we can figure it out from there.
I guess.
**Jackson Weber** 55:44 Yeah.
**Marc Pichler (Dynatrace)** 55:45 Yup.
**Jackson Weber** 55:46 I think that makes sense, and I can, work on getting us back into SPIC compliance if that does change, given that it's experimental.
**Marc Pichler (Dynatrace)** 55:55 Yeah, that makes sense. I think then let's go that route, hey.
Don't really like going against the spec in many cases, because it can lead to trouble.
Down the road,
Because it's expected that the SDKs follow a certain pattern, and then other specification builds on that.
And if we then are not able to support it in exactly that way, that kind of… kind of isn't a great place to be in. So,
let's just disregard whatever I said here with the log record processor, and go with Blogger Configurator, and
I will still comment on the issue here that I am… not…
Completely convinced that that's the correct way to go, but we can still have it like that for now. And then,
Yeah.
Cool, that makes sense. I'll.
**Jackson Weber** 57:04 I'll get that rolled back to the, the original implementation and, make a note on the PR that's ready for review again.
**Marc Pichler (Dynatrace)** 57:11 Yep.
Thank you.
**Jackson Weber** 57:12 Thanks.
**Marc Pichler (Dynatrace)** 57:15 Sorry for the, back and forth on this. Should have made up my mind completely before commenting here.
**Jackson Weber** 57:23 Oh, no, I mean, it's better figuring it out now than after submitting a PR and getting it merged.
**Marc Pichler (Dynatrace)** 57:29 Fair enough.
Alright.
Okay, so the next one is,
implement on ending in span processor. This is also a spec feature,
I also had a look at this one earlier today,
David commented here that, the order seems incorrect because, Span ended.
is…
the true earlier… I think that's just the temple here. So…
Yeah, I think this still needs to be addressed, but other than that, looks good. Probably needs a test for that specific behavior as well, because it's…
something that can cause regressions later on, if we are not careful and at the test for that.
But, overall, it looks… Good, so…
Yeah, because there's nothing to do immediately for this one, and we're out of time too, so, thank you everybody for joining.
Have a nice week.
And see you next week.
**Jackson Weber** 59:02 We're gonna know.
**Hector Hernandez** 59:05 Thank you.
**Marc Pichler (Dynatrace)** 59:06 Thanks.
**David Luna Bistuer** 59:06 Thank you, bye.
