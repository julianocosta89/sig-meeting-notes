SIG: JavaScript SIG
Date: 2026-02-11
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Andrei Borza (Sentry) 00:00:41 Hello.
Marc Pichler (Dynatrace) 00:00:56 Blue?
Andrei Borza (Sentry) 00:00:59 Although…
Trent Mick 00:00:59 You know…
Marc Pichler (Dynatrace) 00:01:22 Right.
Let's wait a little bit longer for some more people to join, in case anybody's joining still.
And then we can get started.
The first topic here is from Martin, but I don't think he's on the call yet, so…
Let's start with… Marilla's topic here…
Marylia Gutierrez 00:02:15 True.
Yeah, just wanna…
share some things that happened, like Auto Unplug. There was, like, a lot of discussions. It was, like.
pretty helpful and, like, useful. And one of the sessions we had was, like.
Basically, a roadmap, just to see, like, what people are interested on, so how it works.
We had the list of things that already exist, like roadmap in general, and then people could add more taste to it, and then people would be able to vote.
So I just found it interesting, some, like, JavaScript-related things. The thing that was, like, most voted was the browser support, and we also have things, the Line 6, the JavaScript ASM support as well. So yeah, just nice to see
interested of people. That doesn't mean, like, this list does not mean, like.
Oh, that is what, like, the GC would tell that is the roadmap. This is more for, like.
see what people are interested about, give the feedback back to the 6, and just, like, things you're considering, and also the things that got
not a lot of votes, does not mean that people cannot work on that, but yeah, they can still work. It was just more like, open discussions, but I just thought I should share it here as well.
Trent Mick 00:03:31 What was the process? Did it start with, like, okay, let's do first segment, everyone propose.
list items, and then it was voting on that? Is that how it worked, or…
Marylia Gutierrez 00:03:41 So yeah, they… we had the list of…
already the existing things that exist on the roadmap, and then for a few minutes, attendees could add to the list. So basically, they created, like, an app, and so it was, like, we were sharing on the screen, like, this is the exists, now we can put, and everybody was, like, typing and putting, and then when everybody was like, okay, I'm done putting, so we had, like, voting, and each person had
10 votes, they could use the 10 votes to the same topic if they wanted, but… Yeah, interesting.
Trent Mick 00:04:09 But the items came from existing roadmaps from the SIGs.
Marylia Gutierrez 00:04:13 No, not necessarily, it was just the… from people there at the events, like, what are the things that they think are important, because we had, contributors, and we actually had a lot of end users as well, so the things that they find important, they…
They want to work on.
Trent Mick 00:04:29 Okay, cool.
Marc Pichler (Dynatrace) 00:04:32 Thanks for sharing that. I'm very surprised that,
logs, stability is not on there. This was something that, was very prevalent, in, KubeCon EU,
last year.
I feel like everybody came up to me and asked about that, so…
Marylia Gutierrez 00:04:54 Business.
Marc Pichler (Dynatrace) 00:04:55 Yeah, but browser support, was also very much a topic that everybody was very eager to, to see, in Oter.js, and,
It's not surprising to me that it's so high up the list.
Marylia Gutierrez 00:05:09 Yeah, there were things that were, like, very, like, general, so I didn't mention here, because they're not, like, JavaScript-specific. But yeah, just, like…
we want to have, like, a install experience of hotel, so that would, like, affect all six. Or we've, like, there were sessions about, like, the quantity config, so that affects all six, so I just was… just mentioning the ones that are very specific for JavaScript.
Marc Pichler (Dynatrace) 00:05:37 Alright, thanks for sharing that.
Any, questions or comments about this?
If not, then I guess we can…
Stay on the topic of, browser support and, talk about the…
diagnostics logger topic, button.
martinkuba 00:06:03 Yeah, hello. Sorry I was a couple of minutes late.
I… so, this is… Something, Mark, that you commented on, thank you.
We're trying… we have… we're trying to introduce a console.
Instrumentation that captures, console messages, and that there's an issue with the diagnostic logger which uses console.
So this was basically, as Mark pointed out in this conversation here.
That would result in, kind of infinite loop.
Potentially, like, if customers had diagnostic Logger enabled.
So I, I, I think I, I discussed this with, in the browser, like, a couple weeks ago, and Daniel.
Daniel's recommendation was to maybe use, like, a similar
Approach that we use for tracing, where we suppress tracing.
But I think, Mark, you had a different preference for…
Maybe, solving it in the diagnostic logger itself, where we just…
Make sure that it always uses the unwrapped, console methods.
So I opened… I opened two draft PRs for those things,
And I would just, I guess.
Leave it up to you to see, like, which ones your maintainers here prefer.
Hmm.
Marc Pichler (Dynatrace) 00:07:31 Yeah, just some, adding some context on why I prefer the,
This one here is that,
In the browser specifically, we, found that, the context managers aren't,
perfect, because we don't have, async local storage in the browser. We cannot, like, just set a context key and read that back later, and, for sure, be able to,
suppress stuff this way. So, that's kind of my preferred solution here is,
using the original console method. So if you were to, mark that as ready for review, I would put that on my priority list and review that one.
If anybody has any additional ideas, please feel free to also comment and suggest stuff there.
martinkuba 00:08:30 I'd just like to, to add on to that,
I did implement the other PR, I implemented it as using the context, but maybe I shouldn't have, because actually the idea that Daniel had was just use, like, a global flag, like, temporarily.
Not even, like, in context, it's just, like…
you know, while… when the diagnostics logger is logging, just set global flag, and then… then unset it when it's done.
Marc Pichler (Dynatrace) 00:08:59 Right. So, that could actually… Work reasonably better.
martinkuba 00:09:05 Yeah.
But I think maybe, like, I do a…
After thinking about this some more, I might prefer, like, the, this, this one.
That's what we're looking at, which is, preserving, like, the original console methods, but…
Yeah, I don't know, like…
Either one would work, I guess.
Marc Pichler (Dynatrace) 00:09:29 Yeah, I think this one, is also… maybe a…
it easier to work with in the sense that it doesn't change the public API at all. So we can just put this in there and iterate on it later as well.
it wouldn't… wouldn't necessarily affect a lot of stuff. One thing that I saw here is there was a comment somewhere.
That said something about, that console only becomes available later, were you able to try that somehow, and see if that affects, functionality at some,
In some way, shape, or form, because I assumed that the concert instrumentation would, wrap stuff early, and if the…
stuff that we have obtained doesn't actually log stuff, then we would still lose diagnostics logging. Not sure if you were able to try that out yet.
martinkuba 00:10:33 I think it's just a theory, like, a theoretical… .
Marc Pichler (Dynatrace) 00:10:37 I don't know.
martinkuba 00:10:38 Like, if this actually can happen in…
I'm not… I'm not sure, like, if the…
Yeah, it was just a fallback, just, like, in case we were not able to capture it for some reason, but I.
Marc Pichler (Dynatrace) 00:10:50 Mmm.
martinkuba 00:10:51 But if you… yeah, I cannot actually think of…
Think of, like, what environment would behave like that.
Marc Pichler (Dynatrace) 00:10:58 Yeah, if there's… if there's any one of the… of the obvious browsers that does that, if…
not… I think we should be fine with this way. It's just something that I saw and I wasn't really sure.
Which environment would do that, so…
martinkuba 00:11:15 Yeah.
Marc Pichler (Dynatrace) 00:11:15 Possibly good to double-check that.
But yeah.
martinkuba 00:11:19 Okay, I'll open… I'll open the PR… PR for review.
Marc Pichler (Dynatrace) 00:11:23 Thank you.
Does anybody else have any, thoughts on this particular topic?
If not,
I guess we can move on to, Avat with initial thoughts on the attach-detach API for tracing general instrumentation.
Abdelrahman Awad 00:11:50 Nope.
thanks, Mark, for taking the time to, Like, draft this out.
I took a quick look at this, thing yesterday, and I had a few questions slash concerns, with it.
The first thing is, since it's using, like, a two-point system, like, attach and detach, so it means, the burden of managing the context falls on the instrumenter, right? They need to remember to attach, and they need to remember to detach.
And that can become tricky with tracing channels, for example, because, for tracing channels, you can have the start event and the sync start event
both emitting for a single trace, so it means we can have double attached. So I guess my question here, is this a problem or not?
then the second part would be we have also end, sync end, and error, and all three can, be emitted for a single trace. So the error event can actually, like, emit multiple times for a single trace. So…
it's… I guess it's a point of predictability, of knowing when to detach. It's mostly the problem here, because what would happen if…
Let's say multiple detaches happened for the same context.
And same question for… Attaching the same context multiple times.
Marc Pichler (Dynatrace) 00:13:18 Yeah, so, attaching it multiple times, through the, async start and async,
what was it? Start and async start? As long as it's just these two, it should be fine. I'm not sure if it can happen that start is emitted multiple times, within one trace operation, I think it's only emitted.
Abdelrahman Awad 00:13:44 No, yeah, it will emit only once, but start and a sync start can happen at the same, for the same trace, but it's easily workaround, like, people can listen. Start is guaranteed to always execute, so we can just attach it there, but I guess my… the biggest problem is with detach there.
Marc Pichler (Dynatrace) 00:14:02 Yeah, the, like… The thing with, with attaching, I saw that,
pretty early when I did the prototype here, that…
Right now, I'm just attaching it twice, once to the async part of it, and once to the other part, but I keep the span around.
And then I just end that later on. For…
detaching, on end and async…
And I think it should also be fine. For error, this is one of the cases where I'm not sure. And I've, kind of looked through the documentation on, tracing channels, but…
wasn't fully able to figure out, what exact order can happen all the time. So… M…
haven't handled the, error states yet, so that's something that I still have to look into. I cannot.
completely answered that yet. Maybe you have some more insights, since you know already that the error can be emitted multiple times. Do you know if AND will also be emitted once error is emitted?
Abdelrahman Awad 00:15:20 It is possible for, end, to be emitted with error. So, the node, node,
documentation, I think, recommends listening to both.
Because it's very possible that, like, if it's an async… sorry, if it's a synchronous error, then error would be triggered. Also, int would be triggered with the error object in the message payload.
But, they also recommend listening for errors separately, because if multiple errors happen, then the end will only have the last one, or the synchronous error that has occurred.
So yeah, it becomes… it's… I don't… I think it's more of a problem of the predictability of tracing channels, because it mostly depends on the…
the trace caller, so if they use trace promise.
and then provide, like, an asynchronous function, then it becomes more predictable. But if they don't use an asynchronous function, then it becomes less predictable. It depends on the return type, if it's a promise or not, or something like that. So, yeah, my concerns with this API is it doesn't really,
Yeah, it kind of requires the tracing… the trace itself to be, like, the trace event to be…
Predictable, which it isn't.
So yeah, the other approach that we are currently using, building right now an SDK with tracing channels.
We are using Bind Store to… with the… and grabbing the… I'm sure you are aware, we are grabbing the, sync local storage privately and binding it to store, and it works well because we are only managing the spam lifecycle, and we don't really care about anything else.
seems to work just fine, and it doesn't really, it's not a big problem with this, like, multiple in… possible ends of the trace, because it's, if the span has ended, it's fine. If it hasn't, then it's also fine, right? We can end it in that end.
But yeah, so… That's, sorry if I talk too long, but it's just my.
Marc Pichler (Dynatrace) 00:17:30 Oh, that's, that's fine, yeah, I completely understand those concerns, the,
like, I feel like the context attach and detach stuff is also, kind of a…
Utgang, in a sense, that.
Abdelrahman Awad 00:17:45 Hmm.
Marc Pichler (Dynatrace) 00:17:46 Like, if you use it wrong, it will just mess up everything. So, I don't know. I feel like both approaches kind of feel a bit, hacked together.
Abdelrahman Awad 00:17:59 Yeah.
Marc Pichler (Dynatrace) 00:18:00 Yeah, so in a sense now, it would be on us to kind of figure out how to… how to do it. One of the other things that I've,
thought about, but then discarded as an idea, was to have the bind,
The bind function on the context,
Be overwritten in a sense that you can…
Put a tracing channel in there, and then, like, have that context manager bind to it automatically, so that the control is kind of inverted, in a sense.
that's one other possible solution that we could, look at. The API then wouldn't make sense, I think, for a lot of the other,
For the other context managers, one of the problems with the bind operation that we have right now is that it takes the active context, but if we bind the tracing channel, then it's obviously not the active context that we want to bind, it's something else.
Abdelrahman Awad 00:19:03 Yeah.
Right now, we bind… we use bind stores in… I know it's not the same thing, but we use bind stores in… for the start event, because it's the only one.
Marc Pichler (Dynatrace) 00:19:12 We are.
Abdelrahman Awad 00:19:13 We're guaranteeing for it to, to actually execute.
So yeah, if they use bind before the start event, then it wouldn't have the right, context, like I said.
Marc Pichler (Dynatrace) 00:19:28 Yeah. So, we would have to introduce something where you don't provide any context.
I've been thinking of, like, providing some magic context object, but that also feels like kind of a hack. I have no idea how to make the shape of the API be…
somewhat digestible. That's why I gravitated towards the context attached, because that already exists in the spec. Other SDKs have it already, so, if we could make it work with that, that, I think, would still be my preferred solution.
I could also enable other use cases that we didn't think of yet.
Abdelrahman Awad 00:20:10 Mew.
I guess we have, like, a few things to juggle here, like, one, we don't want to expose the async local storage, because maybe that's not the only context propagation strategy available.
Marc Pichler (Dynatrace) 00:20:22 And it's very specific to the Node.js runtime, right? Yeah. Also, tracing channels are very specific to the Node.js runtime, so it changes the way.
Abdelrahman Awad 00:20:32 It's a compromise, like, are we… should we optimize for…
One runtime or not. But yeah, thank you.
Marc Pichler (Dynatrace) 00:20:38 Yeah, I will, so I will look into, how this…
I will look into the orders that the events are emitted here, and dig a bit deeper into,
How this works.
just maybe one, question to, like…
finish my understanding of this. The, end is always,
Like, that's guaranteed to be omitted unless you use the tracing channel events and, like, fire them yourself, basically, somehow, right?
Abdelrahman Awad 00:21:22 Yeah, yeah, end is guaranteed to execute, but it may not represent the true end of the asynchronous work, because a sync end may, trigger after it, if they, execute a… if they execute risk promise on a sync function or a promise.
Marc Pichler (Dynatrace) 00:21:38 Yeah, so, as long as these are guaranteed to,
be card, and they can both be card,
Abdelrahman Awad 00:21:48 Cool.
Marc Pichler (Dynatrace) 00:21:48 I have here a context token and an async context token, and I detach… I attach them separately, and I detach them separately.
So these are, like, two separate.
Abdelrahman Awad 00:22:00 Operations, more or less, that are tracked.
Marc Pichler (Dynatrace) 00:22:03 on their own, so it shouldn't be a problem, but I will double-check.
Abdelrahman Awad 00:22:07 Okay.
Marc Pichler (Dynatrace) 00:22:08 Yep.
Abdelrahman Awad 00:22:09 Yeah, thank you.
Marc Pichler (Dynatrace) 00:22:11 Sure.
Any, does anybody else have any thoughts on… this… Peter.
Not then, we could move on to…
The next one, if you have any time,
please also feel free to have a look at the prototype that I built here. If you see any, other obvious,
downsides or problems to this beliefs, feel free to let me know. With new API functionality, it's always good to, apply a lot more scrutiny than,
with, just stuff in the SDK, which we might be able to remove sooner, again.
Alright.
This here is just a little,
thing that I saw, I was,
reviewing this PR that adds the new specification to support exceptions in the logger API. Essentially, what it allows you to do is you can put an exception into logger emit, and it will automatically populate the attributes
That are, prescribed by semantic conventions, from that exception.
And I was just wondering if anybody has any opinions around, which type to use for this. In the API, we now have this exception type, but if you,
try-catch in TypeScript, then, the actual exception that you're… or the error that you're catching will be unknown, so you would have to do some…
something like this to emit it, and it might not be ergonomic. So I suggested to use unknown for this,
And then also, there's different…
Ways, of course, that people can name the errors that they're catching, but, having to type out exception, and then…
This might also not be, the most ergonomic way, so I'm wondering if anybody has any data on what is the most commonly used way to name these things.
No.
Trent Mick 00:24:53 On what that attribute is named?
Marc Pichler (Dynatrace) 00:24:56 What…
Like, people usually use to name the errors that they're catching, because if we can, have something, like, if this was named
error, for example. You could just pass it in as it's named already.
Trent Mick 00:25:15 Yeah, I mean, the… like, the attempt at ergonomic APIs in Bunyan and Pinot, at least, I'm not sure about Winston, used ERR as the kind of… because that was the common shorthand being used.
I don't know if…
You want to be more explicit and not be using kind of a relatively common shorthand in…
an OTEL API, but… sure.
I haven't read up on this, have I?
Good suggestion.
Marc Pichler (Dynatrace) 00:25:49 Okay, yeah.
Trent Mick 00:25:51 Like, it is more con… like, it's exceptions in the software world, but in Node land, it's… they're basically called errors, whether or not.
Marc Pichler (Dynatrace) 00:25:58 Yeah.
Trent Mick 00:25:59 That error happens to be an exceptional.
Marc Pichler (Dynatrace) 00:26:01 Case.
Trent Mick 00:26:02 So, it would feel a little bit weird to be using exceptions instead of error.
Marc Pichler (Dynatrace) 00:26:07 Yeah, I think I, I agree with this, and I guess I will suggest using…
Is here, and then, I couldn't.
We can continue with this.
The other thing is the type, I guess I'm just asking if anybody has any opinions on using unknown here, because that's the default, we get from TypeScript.
And then doing, like, basically checking what is being passed in there, or serfs, before actually setting it on the attribute.
Trent Mick 00:26:54 Yeah, probably. I… I haven't looked at the code path here to know its strong thing, but…
I'll put it on my list to take a look.
Marc Pichler (Dynatrace) 00:27:08 Thanks.
Trent Mick 00:27:09 I don't want to give an uninformed opinion.
Marc Pichler (Dynatrace) 00:27:12 Yeah, it's essentially just the exception type that we have in the API that was now used in the trace API, because there you can record exception.
But it is this very specific type that has either a code or is a string or something like that.
So, yeah, thanks for looking into it. If anybody has any other opinions, please feel free to just comment on the PR there. I'll,
try to keep that one open, for a bit after I approve it. I would just suggest them to use a different name for the property.
And approve this one.
Alright.
And…
Trent Mick 00:28:01 And Jackson just had to drop, unfortunately.
Marc Pichler (Dynatrace) 00:28:04 Oh.
Didn't read the chat… There's…
the other resource attributes is an update from Carlos, who had been driving that on the spec. The PR has been merged.
So, I guess now we can align with, whatever the specification says here.
Yeah, that's essentially what we talked about in the last few -oh.
Weeks here.
So… Jackson also is asking for a review on that very PR. So,
Yes, it's very much a car for reviews, if anybody…
Has time, please have a look.
Now, with the specification updated, it should be…
Fairly straightforward to figure out if, what it's doing is… spec compliant there.
Trent Mick 00:29:13 Yep.
Marc Pichler (Dynatrace) 00:29:18 Alright.
to discuss…
If not, then we can move on to bug triage. As always, if you have anything that you would, like to discuss.
Feel free to interrupt me while we're doing park triage, and we'll get back to your comments.
The first one here is author.js, seems to be no new bugs reported.
AutoJS Contrip, we still have… These two that are Lambda-related.
We already talked about these a few times, but I still wasn't able to find some time to look into this one.
Trent Mick 00:30:14 Name, though I'm tagged on that one.
I still… yeah, if no one gets there, I'll, at some point, I'll… Try it out.
Marc Pichler (Dynatrace) 00:30:24 Yeah, I will… also try to have a look eventually at this one.
I guess the other one is also… Similar.
But this is, when not using layers, and this one is when, sort of building a layer.
Trent Mick 00:30:50 We had a question still waiting for feedback on what their architecture was, because I thought that that one was about lambda to lambda.
We got about just…
getting anything, or was that a context propagation between the two of them? I wasn't sure.
Marc Pichler (Dynatrace) 00:31:05 I think that was a context propagation thing, this trace is split here.
Trent Mick 00:31:13 And so I asked the reporter for what they're…
the trigger was on the second lambda.
Marc Pichler (Dynatrace) 00:31:20 And what?
Trent Mick 00:31:21 Kind of.
propagation transfer we might expect, because if it's through
an RPC one as opposed to an HTTP trigger, then we probably won't expect anything to happen yet.
Marc Pichler (Dynatrace) 00:31:35 Amen.
Trent Mick 00:31:36 drop, but…
Marc Pichler (Dynatrace) 00:31:43 Mmm…
I guess we could still leave that open for one more week. I'll pinged them again.
And,
Ask if they can, answer the question here.
Generate, yes.
Don't pass me… I don't know if… The path… is actually instrumented, too.
Strict.
Unchecked.
Text.
Alright, and then we can see if there's, any activity there.
Alright… CR triage…
Let's see, we have, 56 on…
Core, and fewer than that on…
I'll drip, so let's get started here,
First one is the delegating NOAP meter provider assigned to me. I haven't had a chance to look at that one again.
In more detail, if it also does the instrument, forwarding here.
And the next one is…
integrating the API package, maybe a little update on that, while we're here.
I… Added a bunch of new,
issues to the milestone, because I was, just going through, the implementation and…
was just trying to, review that against the specification and figure out if there's anything that we are missing.
So…
one of the things I found while working on something else is that forced flush was missing on the log record exporter.
There's a PR for that,
in… in case anyone's interested to look at this one. This one is also,
changing the processor to invoke first flush, proper way.
And that will also allow us to get a quicker shutdown time.
with… the SDKs, when the OTRP exporter is used and it's doing its retries.
And there's also another one.
We're implementing logo enabled.
Thank you, David, for working on it. He's not in the car today, but there's that, and
then there are a few questions. So I'm going through these, because, they were…
unblock the, blocks API integration thing, so maybe we can use the time here to also, discuss a little bit about, open questions here. I opened this discussion, thing here for
Scope attributes?
and if they should be of type log attributes,
As you probably know, the specification has changed to accept
A wider range of, attributes.
You can have arbitrarily nested maps now, and stuff like that.
However, scope attributes, in all the other APIs, we still have.
the ORT attributes type there, so I'm wondering if we should change that.
To accept block attributes there as well.
Trent Mick 00:36:36 There's also the ticket to rename log attributes, too.
Something else, right? Complex attributes? Is there a name that's established in the spec, or other languages? Do you know?
for me.
Marc Pichler (Dynatrace) 00:36:46 Yeah.
Trent Mick 00:36:46 you already…
Marc Pichler (Dynatrace) 00:36:48 I think they didn't really introduce a new type. They had it all structured in a way that it's possible to extend it without it being a breaking change. So I guess they just call it attributes there.
In the spec, I haven't really seen any, suggestion.
Trent Mick 00:37:07 Would we try to do that, too? Just call it attributes, but all of a sudden, attributes is a wider…
Sing, or is that…
No compatibility issue in the API.
Marc Pichler (Dynatrace) 00:37:17 I think that's a compatibility issue in the API, in the sense that, when you… So…
It's the same problem that we have with, extending the pipes
Or, let's say, meet a provider, or,
logger provider, or any one of these, really. So the types shift, and then if you implement it, you're running into compile errors.
For attributes, this is a lot worse, because people are using the attributes type everywhere in their apps or in their instrumentations.
So if they go through the properties and they do some,
They read them back somehow, and they assert on the type.
And that type suddenly expands, then, they might…
get compile errors there all over the apps, so I think replacing it is still…
Much safer option for this.
One thing that we can do, though, is we can change the…
APIs, the trace API, for example, to accept complex attributes later on. So it would accept either attributes or complex attributes.
Pardon.
Trent Mick 00:38:34 pepper.
Marc Pichler (Dynatrace) 00:38:35 Because that then is only breaking for implementers and not for, actual users.
So that's kind of why I'm suggesting the rename there.
Trent Mick 00:38:48 Yep, I… okay, I definitely think we should…
rename it away from log attributes, and then I would say yes to this question.
Marc Pichler (Dynatrace) 00:39:00 Right, so, I guess in general, for this one here, there's probably no… Objections to it, right?
I'm not sure if scope attributes is actually widely used anyway, but…
Trent Mick 00:39:26 I don't think I've ever seen scope attributes in their tests, so we actually support that.
Marc Pichler (Dynatrace) 00:39:31 We…
That's a great question, actually. My first instinct was to say, yes, we do, but I'm actually not so sure now.
Trent Mick 00:39:43 Guess we'll find out.
Marc Pichler (Dynatrace) 00:39:52 Yeah, if anybody has any opinions on that, please feel free to, comment here.
I'll leave that open until…
next week or so, then this has been open for a few weeks, and if there's no comments, then I guess we'd be fine to just go ahead with that.
And then also the… renaming stuff we just discussed here.
And then there's a few,
other tickets in here. This one is,
Let's spawn this side quest here, and…
This is one thing that, Dan opened, a while ago.
It's about auditing the logs API for,
extensibility. So, the idea of that one is to look into strategies to change the API in a way that
Additions wouldn't be breaking to,
to implement this, so if anybody implements their own logs SDK, they wouldn't be broken as often as people are right now with
Metrics and traces.
Does,
something where we can go, quite deep into, the discussion here, but I think the way that we have structured the emit function with the options is
working pretty well, so I'm not sure if we need to make any large changes here, but if anybody has any opinions, please also feel free to have a look at this one.
And… Note them down.
Down here. And that's pretty much everything that's left for…
the blocks API SDK stabilization until we can… Look into requesting, PC.
Review on the whole thing to eventually get it to stable.
Which would end in us merging this PR here.
Alright.
Next one is, Entities Prototype.
I'm actually not sure what the current state of the work there is. Has anybody followed that?
Trent Mick 00:42:37 No, other than Dan has a V3.
prototype of entities, so this one is presumably going to die, but I haven't read… he has a newer one. If you scroll to the next page, there's a…
There's another one.
Down right at the bottom of your screen right there.
Marc Pichler (Dynatrace) 00:42:58 Oh… Oh, I screwed too far.
Trent Mick 00:43:00 No, it's halfway up.
Marc Pichler (Dynatrace) 00:43:02 There it is.
I just asked Dan here if.
Trent Mick 00:43:09 If that obstetes the other one, yeah.
Still draft, also.
Marc Pichler (Dynatrace) 00:43:44 Kicked myself out of the…
Current state here, let's go back to that,
Yeah, once we figure that out, then maybe we can cross that one off the list.
This here was advisory attributes, commented 2 weeks ago.
If they're still working on it, but no activities, I'll close this one here.
If anybody wants to see that, implemented, please…
Feel free to go ahead and pick up the ticket on that one.
It is a specification feature, but I think it's still,
Experimental, and it is in need of additional… prototypes there.
Then we have this here,
the experimental trace decorator support. So, I've actually been thinking of what to do with these,
Every once in a while, we get a proposal for,
API, extensions, more or less, that…
are basically just sugar on top of the existing API, and I've been wondering how to, handle these.
one of the things that I was going to suggest was to have a sort of,
OpenTelemetry API extensions decorate the package.
That people could import, and that would just depend on the API.
So then you could use these, and we would have to make them kind of subject to a similar
stability guaranteed in the API.
And this way, we wouldn't have to include a bunch of stuff in the API that isn't, like, necessary primitives there, but still get some flexibility on
providing these sorts of things. One of the other things was, I think right now we have some API in,
experimental, that's called a sugar tracer or something like that, which has some extra functionality there.
Does anybody have any opinions on…
How to deal with these sorts of things.
Trent Mick 00:46:28 Not strong opinions, but I… I don't mind the idea of moving it out to a separate package, because let's API focus on being stable.
Marc Pichler (Dynatrace) 00:46:36 No.
Trent Mick 00:46:39 Yeah, I don't know. I don't see anyone using the sugar tracer.
Marc Pichler (Dynatrace) 00:46:43 I don't think so.
Trent Mick 00:46:44 I don't have strong opinions on the decorator thing here. Decorators in JavaScript are a little bit of a…
Disappointment to me, because you can…
You can't decorate a function that's not part of a class, so…
Yes, it's kind of a limited sport, but yeah.
Marc Pichler (Dynatrace) 00:47:01 B.
Yeah, so, iterating on stuff would probably be easier to have that, be in a separate package. We just have to
Figure out where we want to land that, if we want to put it somewhere.
If we put it in the country pre-po, or here.
We could probably go either way.
Trent Mick 00:47:33 I think probably contributors isn't really a core thing, unless it gets to a certain level of…
this feels like it's settled, and it's popular, and I don't know. I don't know what…
The justification should be, but yeah.
Marc Pichler (Dynatrace) 00:47:47 Yeah. We could also separately monitor downloads on NPM this way, could figure out how well it's used, unless we also start using it in our own packages in that case.
Trent Mick 00:47:59 AI, then forget it.
Marc Pichler (Dynatrace) 00:48:02 Right.
So…
I think it will create an issue for that, to kind of have some point where we can discuss these sort of things.
figuring out where…
We put this, and in the end, if we decide to go that route to have separate packages, we can always,
once we feel confident that it's not going away and that it's well used, we can integrate it in the API package as a stable thing, because we then obviously already know that it's
It's working and working well for everybody.
So, I'll write these… things down.
And, we can discuss further on that one.
Alright, the next one is also draft on, generating types from… config.json schema…
I guess train mute.
I'll be out of office for a bit, so…
Let's skip this one for now.
Unless anybody has any, thoughts on using,
Generate a thing to generate the types.
Any initial concerns, maybe, you would like to talk about?
Not doing something like this.
Trent Mick 00:49:51 I think we can move on.
Unless Aurelia's got some insight there, but I'm guessing the latest work that Aurelia did to get to the latest
RC version probably means that Jamie's work is out of date. He's currently there.
Marylia Gutierrez 00:50:05 Yeah. Yeah, I think a lot of things I need to… yeah, I just closed, like, this morning, the PRs that I had open before my changes to RC, because, yeah, there's a lot of changes that have to come.
Trent Mick 00:50:17 I see. Okay.
Marc Pichler (Dynatrace) 00:50:19 Do you know what the current state is? Will it, will this be the last release candidate, or will there be another one?
Marylia Gutierrez 00:50:26 Yeah, the goal is now… it's just waiting to be market stable once we have a few, like, proof of concepts, so that is what is waiting at the moment. No plans to create another one.
Marc Pichler (Dynatrace) 00:50:38 Alright.
So I'm a bit out of date on the, currently open pull request. Is there a new PR already for.
Marylia Gutierrez 00:50:49 No, for the… for my thing, no. Perfect.
Marc Pichler (Dynatrace) 00:50:51 That's… okay.
Marylia Gutierrez 00:50:51 Yeah.
I'm probably gonna open, like, by the end of the day or tomorrow. I was just finishing up.
Marc Pichler (Dynatrace) 00:50:59 Yeah, I will, have a look once that opens, once that's open, so, that we can move that forward as well.
Marylia Gutierrez 00:51:06 Cool.
Marc Pichler (Dynatrace) 00:51:09 Alright, then this one here…
Is the configuration depth.
Think, I think…
This one is marked as outdated.
Trent Mick 00:51:39 Yeah, I was looking again at that, what I said, but then I think I just repeated stuff that had already been discussed above.
Marc Pichler (Dynatrace) 00:51:44 Oh.
Just bonus, so I think I…
Trent Mick 00:52:01 Yeah.
maybe this has already been agreed upon, but I think this would be easier to get in if we just bumped the default depth in the console dura usage as one change. That solves the GenAI issue.
basically what I said, but sort of an outdated thing. And then we have a separate issue to discuss if we want to have some workaround for a console that we're not existing in…
What is it?
Cloudflare workers.
And then on the Cloudflare workers thing, I'm not deciding if we want, like, to just…
Though it's the tail wagging the dog, should we try to detect Cloudflare workers? Because there's an official way to do that, and if so, avoid console.dur, because avoiding console.dor to do a JSON
Representation dump, and then having to decide on this undefined versus null representation feels unfortunate.
Because… Console.dur is… the safe way in Node to get an accurate representation of what that thing is.
Or debug.
Marc Pichler (Dynatrace) 00:53:08 Yeah.
Trent Mick 00:53:08 purposes, JSON representation is not necessary.
Marc Pichler (Dynatrace) 00:53:14 Yeah, I think I, agree on that. I would, ideal solution would be Cloudflare workers implementing Consortia, and then everybody lives happily ever after.
Trent Mick 00:53:27 Yep.
But, like, I mean, if the realistic side, if they're not going to implement that, we can just detect Cloudflare workers at the top level and just use console.log, and I'm sorry, you don't get better than console.log. Because if you're in Cloudflare workers, presumably in console.log, you're in a browser.
E… environment, I'm not sure what… if they just get a reduced view of the thing, or if they get, like…
In a debug console where you can click through and see the full structure there, so if console.log would suffice for that.
Marc Pichler (Dynatrace) 00:53:57 So, in a browser, or at least in Firefox, what I'm using is, I usually get a full expanded, like, a thing that you can expand and have a look into. Yeah.
So…
Trent Mick 00:54:14 I'm not sure what the experience is for developers of using Cloudflare workers. Do they… if we did a console log of this thing, is it just a string representation in the logs that they're browsing? So they would just get, basically, a not super useful view of it?
Marc Pichler (Dynatrace) 00:54:29 Oh, good.
Trent Mick 00:54:30 knocks with… If… I don't think we should…
I don't know, I guess I am hesitant to do the heavier implementation here, just because Cloudflare Workers doesn't have console.
Marc Pichler (Dynatrace) 00:54:44 Yeah, I agree. I just write it down here,
I think this PR would be, easy to merge… If… Cloudflare.
Sure was.
Purdist.
I can't… I cannot English.
Trent Mick 00:55:20 Bing.
Marc Pichler (Dynatrace) 00:55:21 Or any day, actually.
Artboot suggestion…
Let's just, the, yep.
Grace.
Perfect.
That's this one, and then…
You have warning preloaded modules function does not show warning. Looks like David commented on this one.
Unnecessary module preload warnings here.
There's a lot of steps here.
Trent Mick 00:56:54 I can try to take a look at this one.
Marc Pichler (Dynatrace) 00:56:57 Thanks.
Seems like a failure.
Small change, but… Figuring out what the impact on these is.
It's always a bit difficult. The warnings here, they are always very helpful in suggesting fixes to users.
-
Thanks for looking into that one.
Alright, and then we have…
I'm trying to renovate… Things that I…
said multiple times that I was going to have a look at, but didn't.
Assign this to me.
So that it actually shows up in my list here.
And the next one is the create instrumentation factory function. This also seems to be in draft still.
Decide if the approach is the right one.
I had a brief look at this one, and I generally agree with the shape of the API. I think it's,
a lot better Than what we have now.
Still just a lot of…
Moving parts that need to be considered, since we have so many packages, depending on the,
On the shape of the instrumentation interface, so…
We'll have to look into that in a bit more detail here.
I don't have any,
concrete opinions on this. I'm not sure if anybody else has taken a look at this PR before.
Trent Mick 00:59:34 I had hoped to, but I haven't yet.
Marc Pichler (Dynatrace) 00:59:39 I will, also try to get to this one once I… Back through the… I love, peers.
on the list.
Looks like we're out of time anyway for today.
So… Thank you, everybody, for joining.
Have a nice week, and see you next week.
Trent Mick 01:00:04 Thanks. Thanks for funding.
Marc Pichler (Dynatrace) 01:00:07 Thank you, bye.
