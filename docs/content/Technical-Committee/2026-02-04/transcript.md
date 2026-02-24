SIG: Technical Committee
Date: 2026-02-04
Duration: 62 minutes
============================================================

## Zoom Recording Transcript

**Jack Berg** 00:30 What's going on, David?
**David Ashpole (dashpole)** 00:33 Hey, Jack.
Not too much. Have you seen the thread on…
**Jack Berg** 00:37 Concurrency?
**David Ashpole (dashpole)** 00:39 Yeah.
**Jack Berg** 00:40 I was gonna ask you about that, like… Thank you.
**David Ashpole (dashpole)** 00:42 And it came out of nowhere for me, so I… I'm… I'm mostly curious to learn the backstory.
**Jack Berg** 00:48 Yeah, I don't know the backstory either, but, you know, just, like, my knee-jerk reaction, and I just got back from traveling, so I haven't, like, fully read through the thread or anything, but my knee-jerk reaction is, like, like.
it's not very useful to have an API if we can't
If we can't make guarantees that callers can call it concurrently.
**David Ashpole (dashpole)** 01:08 Right, yeah.
**Jack Berg** 01:10 But I think there's more to it, right? Because that's just, like, the really obvious thing, so there's got to be more to it.
**David Ashpole (dashpole)** 01:20 I… that's what I'm trying to figure out as well. I'm not sure I know if there's more to it.
**Jack Berg** 01:25 But we make that assumption all the time, like, think about, think about Tracer and Logger. Like, implicitly, those are allowed to be called concurrently. Because imagine if you couldn't.
**David Ashpole (dashpole)** 01:36 I do.
**Reiley** 01:37 So, which API are we talking about? I'm surprised, like, why people assume.
**David Ashpole (dashpole)** 01:41 All of them.
We don't use normative language in the statements requiring concurrency, and so… .
**Reiley** 01:49 We cannot, because there are languages that have no idea about this.
Like, some language, like, JavaScript, it's, like, asynchronous. There's no concurrency, except if you have, like, Workhorse or something.
**David Ashpole (dashpole)** 02:03 That's a good point, maybe.
**Reiley** 02:05 But, like, if maintainers don't understand the intention here, that's, like, a huge surprise to me. It's like, you don't have to… you don't have to tell people your API cannot take indefinite amount of time.
Right, this is, like, the basics, and I don't expect us to cover all this, like, fundamentals in the spec.
**Jack Berg** 02:28 Right, exactly, like, you know, inherent in the design of these things is, you know, metric systems need to be called concurrently, and not every language has… that concept isn't applicable to every language, but the languages that it's applicable to, this is implied.
**Reiley** 02:46 And for example, like, we… do we need to say, like, your API shouldn't cause a deadlock or something?
**Jack Berg** 02:52 Price.
I hope not.
**Reiley** 03:00 But one… one thing I, I, I think in…
in some languages, like in OpenTelempia .NET, I think people put specific effort to, support re-engency.
So, for example, if you call a metric API, and that API eventually leads to some, like, exporter, and the exporter is also calling metric API, things like that, like, you don't want this, like…
live loop or stack overflow or something. So either you will have a mechanism to surprise the exporter or the plugins being instrumented.
Or you do that asynchronously.
this is something, like, the operating system typically do. If you're running inside an interrupt handler, then another interrupt, came, then you should be able to handle that.
**jmacdonald** 03:56 Hello, everybody. I joined late. I started taking notes, since I'm on the rotation this week, so I listened, I hear what you're talking about, but I haven't, opened the issue yet.
I… maybe I shall.
**David Ashpole (dashpole)** 04:11 I didn't… I didn't necessarily mean to add it as a topic for discussion.
**Jack Berg** 04:15 Did Tigris added it, doesn't.
**jmacdonald** 04:16 Tigran did, yeah, it's on the top of the agenda, so I'm… I've opened this… I can actually share it, I mean, Yale and I,
So here we are.
Currency requirements.
Okay, this is giving me thoughts and feelings, which I will share.
**Jack Berg** 04:53 It's actually a long read.
**jmacdonald** 04:55 Yeah.
**Jack Berg** 04:56 Okay, perfect. Maybe 20 total comments on it, and I think it would probably take me, like, a half hour to get through.
**jmacdonald** 05:01 Yeah, I don't think we should try and read it right now. I was gonna read the top,
David, I would… since this touches on Go so much, I would, like, just defer to your opinion on this topic.
**David Ashpole (dashpole)** 05:18 Okay, let me open the TC… I mean, I'm…
**jmacdonald** 05:25 Only because I know that you're involved with the Go SDK, and I'm looking for opinions before I say… I guess I say my…
My opinion, as I've…
**David Ashpole (dashpole)** 05:34 stated in comments is that, a few things. One, I think
I do think that even though the language is non-normity, non-normative, that, like, clearly the spec is meant to say that,
APIs, Should require implementations to be…
concurrency. Like, I… I think the language, like.
the language is maybe a bit weird, because, of course, having something in an API spec that says the API has to be concurrent safe.
might imply, like, that the API needs to do locking itself or something, which…
I don't think anyone reasonably thinks is actually the intent of the API spec, right? Right.
Really, my interpretation of the document is that
APIs where concurrency is a thing.
should document that implementations need to be concurrent safe. Something to that effect, right? Like, in terms of, like, actual…
If I were to actually read that out as a series of must statements, maybe.
But I don't think… I…
we even, in the GoSig, actually have some of our interfaces documented as requiring implementations to be concurrent safe. As soon as I pointed that out, Tyler raised a PR to remove the language. But…
Like, currently, like, we have a mix of interfaces that say nothing, or that say it needs to be concurrent safe.
We also… we do explicitly have other language in the spec.
Saying that, for example, callbacks Need to document that the callback needs to be concurrent safe.
So, like, we have similar language elsewhere, but it's phrased in a normative way instead of not being.
I also think…
I'm somewhat surprised by it, because the Go ecosystem has a wide variety of examples. My last comment on the thread is talking about the new S-Log interface, which
Has very similar language, says handlers need to be, you know, need to deal with concurrency.
And so…
Yeah, I'm surprised that it's really a topic of discussion. I support improving the language to make it normative, if we can find a way that makes sense for languages. But generally, I agree with Tigrin's position.
that, it is a requirement on the API, and that does extend to the SDK.
And that even though it's not phrased as a normative requirement, that still, like, APIs should…
put this on there, and SDK should be compliant, right?
Riley.
**Reiley** 08:17 Yeah, so I… I remember, like, when I…
when I put the concurrency requirements in the API and IST spec, I think I should cover
All the cases here.
So, which part is… Is this a part that I didn't cover in the spec? I want to know.
it sounds like…
from the description, we're saying, like, I shared the link. You can find the concurrency requirement from both the API and the ICK, and we put specific wording saying for languages that have this concurrency concept, what's the expectation?
So… My gut feeling is this is already covered.
And I want to understand, like.
**David Ashpole (dashpole)** 09:01 Tyler's point is that it doesn't use any normative language. It doesn't say, you must do X, or you must do Y. Therefore, it's just flavor text in the spec. It's not binding.
**Reiley** 09:13 I see.
**David Ashpole (dashpole)** 09:14 So that's… and he may be technically correct. This is the first spec-related project I've worked with, so maybe some communities would interpret it that way, but I certainly don't, and we've written, like, for better or worse, so…
**Reiley** 09:30 Yeah, so the… the… yeah, it's not about whether that description is clear, it's about… it's not normative, so people can… can treat it as a nice-to-have or whatever thing, right?
**Liudmila Molkova** 09:45 I think Tyler, if I didn't read through it, but it seems he is in favor of not making it a requirement. Is it the case? Does anybody know? What is his motivation?
**David Ashpole (dashpole)** 09:56 I… see, that… that's where I'm not clear. I… he…
He proposes, halfway through the issue, a mechanism for interfaces to report to their callers.
whether they…
or sorry, a mechanism for implementations of the interface to report to the caller whether or not they are concurrent safe, so that instrumentation can have different code paths for concurrent safe and not concurrent safe ones. And…
Yeah, largely, I think,
CJO and others have said that that seems like not a really viable approach.
**Reiley** 10:39 Okay, so in order to solve this issue, if I send the PR, changing the tags to have must, are we done, or not?
**David Ashpole (dashpole)** 10:49 I think…
**Reiley** 10:50 In the car right now.
**David Ashpole (dashpole)** 10:51 So, right, so you could… what I've proposed halfway through the issue is to change the text to say that APIs must document that…
implementations must be concurrent safe. Because then, like, you can…
decide whether you've completed it by whether your API has that documentation.
**Reiley** 11:10 Pardon.
It must be concurrent safe, or it must document whether it's concurrent safe or not, or it must be concurrent safe, and it must document that, both.
**David Ashpole (dashpole)** 11:20 Tyler's point is that APIs have no notion of concurrency in the interface definition, at least not in any languages I'm familiar with. I don't know, maybe.
**Reiley** 11:30 I sleep.
**David Ashpole (dashpole)** 11:30 Okay, cool, like this. Like, it doesn't make any sense to say that an interface is concurrent safe. He wants, like, how can I write a unit test for my API that determines whether…
**Reiley** 11:41 The thing is fulfilled, right?
**David Ashpole (dashpole)** 11:44 So that's, that's his, like, Yeah, anyways.
**Reiley** 11:47 So, interface should… So…
make it clear in the contract that the implementation should be concurrent safe. That's your point.
**David Ashpole (dashpole)** 11:54 My… that's my proposal.
**Reiley** 11:56 Okay.
That makes a lot of sense to me.
**jmacdonald** 11:59 in,
you know, I've been working in Rust now, and in Rust, there's a, like, a compiler feature, basically, that's telling you whether you have a safe path to the data or not. It's, like, there's no ambiguity at all. And we've gone out of our way in this project, Otel Arrow.
to, like, offer you building blocks that you can decide whether you want concurrency or not, because if you're running on a different CPU core, you might actually just want a completely different SDK. And I just don't know how to do that in Go.
Yeah, so I sort of agree with Tyler, but I also, like, I'm sort of rolling my eyes right now, because I don't, I feel like it's unhelpful to say that an API is not guaranteed to be concurrent safe in Go, which is a very concurrent-friendly language.
And I remember a piece of just… I just want to share this debate so that y'all have some context that I'm kind of thinking about.
early, like, years ago in the Go Metric SDK, there was a moment where there was a concurrency bug, that we had to debate, and so I've had to debate at least one with Tyler on this.
And my… it was my architecture in place at the time. There's this attribute set type.
Which, it's still there, because it was part of the stable API early on, but it… what it would do is sort in place. So you pass me an attribute set, I will sort it in place, compute a fingerprint,
avoid an allocation, because I don't need to reallocate, I just want to make sure my keys are ordered and deduplicated. So I would sort them in place, and that was a moment of unsafety.
thread unsafety. And my position was, the caller shouldn't… that the attribute set is not defined as concurrent safe.
each color should have their own attribute, because otherwise we can't make this optimization, and you're going to be forced into an allocation. And so it was choice between a concurrent optimization that required some safety and some documentation, and some, like, clarity for the developer, versus a forced allocation and, like, guaranteed to work. And we ended up with a forced allocation, and I, like, I've been unhappy with it ever since.
But it wasn't my call, and I… I mean, like, I don't…
I don't know what to say about the language, either.
So I can see an SDK wanting to provide an unsafe mechanism for callers that want no synchronization, but I don't know how to test it or require it or specify it.
**Liudmila Molkova** 14:22 Yeah, I also was thinking that it… we should provide… we should require
for the specific instrument methods that we have to be thread-safe. But in theory, somebody could add
non-thread-safe method in the future that would make caller take care of concurrency or… or something else?
**jmacdonald** 14:49 in a Rust SDK, this could just be, as far as my intermediate understanding, this could be a feature. Like, here's the library if you want the no concurrency, you could just do that. Here's the library if you do want the concurrency. If you've got threads, you're going to need this one. Otherwise, it won't compile.
**Jack Berg** 15:05 Does anybody want that? Is anybody wanting, like, you know, a library that is…
Gives up concurrent safety for something in return, probably performance.
And is there actually a performance increase? I know you have to do, like, a little bit less locking and a little bit less work, but when all that locking, or whatever it is that allows the concurrent safety to… when all that's in place and there's no contention on those, it's pretty fast.
**jmacdonald** 15:35 In the case that I'm aware of, it's a niche interest, but when we talk about these very large machines with their, like, NUMA memory regions and so on, it might not work out that way. So you might say, okay, I have a big machine with NUMA regions, and I'm gonna have one SDK per region, and that, you know, you'd still have some synchronization, and it wouldn't be costly.
But what we're saying is that to a Rust programmer, this is just a building block in the program. You decide where you want your synchronization, and the SDK gives you the unsynchronized form, and maybe it gives you a synchronized form as well, and you need to choose the right one. I don't have a great answer, Jack. I think it matters someone to someone, somewhere, sometime.
**Jack Berg** 16:14 Yeah, right. So it matters to someone, somewhere, sometime, but, like, that's definitely the niche case. I think, like, that's a reasonable statement that isn't controversial. And so, like, you know, when I read this, it's like the,
you know, to interpret the existing spec as having meaning, like, you don't need to be thread safe. It's just like an intractable position.
Like, you know, to assume that instrumentation for all this time was assuming, like, you know, no thread safety, and was taking precautions to, you know, to have single-threaded access, to do the locking mechanisms themselves.
That's not what anybody interprets when they were seeing these APIs. And so, the language that, like, you know, doesn't have normative language in it right now around this, it's a spec bug.
Like, it was everybody's intent the whole time that these… that these methods were safe to be called concurrently, and the fact that there's not normative language in it, we just… it was an oversight.
**David Ashpole (dashpole)** 17:17 Tyler has said… That… he would have blocked a PR.
That added normative language to make it a requirement.
**Jack Berg** 17:27 What about normative should?
Like, must is pretty strong, because, like, it means there's, like, no exceptions, there's no languages that, like, you know.
are allowed to consider this, but, like, you know, maybe there are situations, like, you know, JavaScript or something like that, that are single-threaded, where this is just not applicable, and you need to carve out an exception for them, but by and large, I think we need to communicate…
**David Ashpole (dashpole)** 17:50 For him, but he… given that he wants to remove it from our… Go APIs.
I think he might oppose that as well.
**Jack Berg** 18:02 Yeah, like, you know, and on the other side of this, if we were to remove the language that says, like, hey, that suggests that instrumentations can assume that these methods are concurrent safe, I would block that.
Because, like, that's going to be terrible for our adoption. It's just going to be… like, nobody's going to use our APIs if instrumentation has to do locking themselves.
**Liudmila Molkova** 18:27 But can we do the should PR, and talk to this Tyler and see? Maybe he doesn't mean it in general? So, like, blanket statement, like, all methods on this class should be, thread-safe, doesn't make sense. But these specific methods
Should there must be thread safe, maybe this would be the common ground.
**Reiley** 18:50 So we…
Like, from the description, we just don't have the normative, like, the uppercase should, but the intention is essentially should.
For all the classes mentioned there.
Josh, would you open the link in the chat, or…
**jmacdonald** 19:08 I will open it again, yes.
**Jack Berg** 19:11 Oh, it's a different one.
**jmacdonald** 19:11 Oh, in the chat.
I'm having trouble with Zoom at the moment, let me find my computer.
**Reiley** 19:16 I'm finding it from this group.
If I'm going to send a PR, like, what do we want here?
My, my take is very simple, we just…
Change the wording to uppercase should.
like, currently, we're saying all methods are safe to be called. I'll just change that to all methods should be…
safe to be called concurrently, the concurrent…
So just add shoe to all of them. We're done.
That's my take.
**David Ashpole (dashpole)** 19:45 I think he would ask that it be…
like, phrased in such a way that it's a requirement on the API documentation, or something. Like, well, he did thumbs down my comment, so maybe he doesn't like that, but I think he would say that APIs cannot…
implicitly… or, like, we all know what the language means, so maybe should is fine here, but I don't know if the.
**Reiley** 20:08 I… I think we're… we're getting into the rabbit hole, because if you look at the API spec, OpenTelemetry API has never intended to be a pure abstraction. Like, the API, sometimes they come with a no-op implementation. We're saying if the ICK is not injected, the API should behave, and you can also…
Imagine that the API might have a very thin layer to detect whether the provider is injected, then call the actual SDK implementation. So…
in order to make it super clear there, we need to have a lot of explanation. I mean, I don't have a problem to explain that, but I…
I wonder if that's what people really need.
**Jack Berg** 20:46 Yeah, I don't think it's productive. Like, you know, we can… we can have a big, elaborate explanation, basically describing that, hey, it's not always practical, or it's not practical to have this as an API-level enforcement.
But, you know, that just makes it a more difficult read for users picking up these APIs and for, you know, maintainers to implement. Simple statements where things are implied, but almost everybody reads them as intended, have benefits.
**Reiley** 21:19 Yeah.
Sleep.
**Jack Berg** 21:21 Can I… when I have Zoom, I don't know how… when I'm presenting, I don't know how to raise my hand, so anyway, here's my hand up.
**jmacdonald** 21:27 Could we just say something about how SDKs, should be safe, unsafe APIs must be documented?
**Jack Berg** 21:37 Yeah, so kind of go the other way. Everything's assumed to be concurrent safe, except if noted otherwise.
**jmacdonald** 21:43 I just wanted to say safe. Like, we have a safety policy that's broad. It's even broader than concurrency. It's like, by default, safe is the choice you make. I mean, there's, like, running out of memory is a safety issue, too. And I like to think that we…
Have that principle in mind.
**Reiley** 22:00 David's very… It's vague.
**jmacdonald** 22:03 Yes, intentionally.
I mean, concurrent safety is also pretty vague. I mean, when you get down into the nitty-gritty details, there's so many.
**Reiley** 22:13 even more vague, like, do you require re-entrancy? Like, if a metric API being called in the middle, the SDK implementation actually called another metric API?
do you allow SDK to say, stack overflow, good luck, or the SDK should.
**jmacdonald** 22:31 That is the type of safety requirement I would make of an SDK. Yeah, if you're a logging SDK and you have a dynamic handler, you better prevent the logger from logging in the handler. That's the safety issue.
**Reiley** 22:41 Recursion prevention is, is like, for example, yeah.
So there's a lot of details, actually.
We, like, are we good with, like, the general, like, safe statement? I mean, I'm fine. I expect maintainers are pretty experienced.
developers.
So, like, if we need to babysit them and explain, like, in a way that maintainers can just ask, like, some AI to automatically generate code, then I don't think they… they can beat maintainers anymore.
**Jack Berg** 23:14 Yeah, right, like, when I think of Josh's safety statement, in the concurrency, statement as well, I think about, like, correctness.
So, like, hey, when I call this API concurrently, I expect no errors to be thrown, and I expect, you know, the output to be correct, where it's indistinguishable if those concurrent calls were made concurrently or sequentially.
Right? So there's no lost rights, there's no partial rights, and there's no double rights, duplicate rights. And, like, all that is implied.
And, like, if we have to get into the business of saying, like, hey, when I record something in the API, it's correct. Like, that's a bad… that's a bad spot to be.
**Reiley** 23:56 Yeah, so you can safely observe your stuff by calling the instrumentation API without worrying about it. It's giving you some, like, surprise.
**Jack Berg** 24:05 Right.
**David Ashpole (dashpole)** 24:06 I don't want to speak for Tyler, but I think he would say that those are all SDK considerations.
And that he would fully support.
having it specified on the SDK, but…
**jmacdonald** 24:18 Yeah.
**Jack Berg** 24:20 No, but it's important for us to… I agree. …to communicate to API… to instrumentation, you know, authors who are going to be reading the API document, that they can safely call these concurrently, even if we can't practically enforce that with any mechanism. Like, we need to communicate that, because,
it's like… and, you know, I can comment on this issue as well. I know you're… you're just kind of channeling Tyler, right? But in…
But yeah, like, it were…
We are writing an incomplete spec. We're sacrificing too much if we are so strict about, like, you know, how we write the spec in that regard.
We have to, like, you know, we can't let, you know, that pedantic… that pedantic point sort of get in the way of the broader goal of ours, which is to communicate to instrumentation authors that they can safely make this assumption about concurrent calls.
**Reiley** 25:18 I think you're literally saying we need a law and we also need a judge. We cannot just use law plus a bot and solve everything.
**Jack Berg** 25:25 Right, yeah, exactly. We can't,
We could talk about this over and over again. We need to… we need to have, like, room for human judgment. We can't, like… we talk about this with our processes, like, we can't try to boil everything down into a process. We need to leave room for judgment.
**Reiley** 25:45 Yeah, I agree with that.
**jmacdonald** 25:51 I feel like now the actual issue is so far from the conversation that I need to go read it before I can say anything useful.
**Jack Berg** 26:02 So to move forward on this, though, like, so, Riley, you're talking about potentially opening a really simple PR. You know, I've volunteered to comment on the issue and, you know, at least provide my piece on it. So…
why don't… why don't we do both those things? Like, why don't we, you know, all contribute our comments, given this discussion? And also, this discussion is public, so maybe Tyler will see this as well, but in case he doesn't, we should repeat any points that we think are relevant.
And then, you know, after those marinate for a day or so, maybe, Riley, you can open that PR.
if it's… if it's still applicable. I don't know where the conversation will lead.
**Reiley** 26:41 Yeah, so first, I guess I'll just open the PR right after the meeting, because we know, like, the spec better have this normative language, right? So I'll just do that, like, whatever makes sense for this group.
And then, like, we can take the feedback from Tyler and see what's a reasonable thing to do there.
**David Ashpole (dashpole)** 27:01 I think this also may apply to all signal types. So, I think the debate has started on metrics, but
I believe the language was copied from Trace.
**Reiley** 27:12 I'll start one. Once we handle metrics, I'll just, like, copy-paste.
**David Ashpole (dashpole)** 27:17 Okay.
**jmacdonald** 27:21 Alright, well, I'm taking notes, pretty well, at least. Nothing else is on our agenda.
And I don't myself have anything else to add.
I am trying to fulfill all of my responsibilities as TC on Call this week,
And I may have an accurate list of what that means.
Anyway, I think we're good.
Shall we call it?
**Jack Berg** 27:48 Actually, stop.
**Reiley** 27:49 I have one. Oh, sorry.
**Jack Berg** 27:51 Go ahead, Riley.
**Reiley** 27:52 Oh, I have one, so if you look at the current, open PRs under the spec report, they're a lot. I think last week it once reached, like, more than 30, and I tried to…
resolves, like, merge some of them. So, like, what should we do here?
Justin, can you open…
I looked them over on Monday, so if things need to be merged, I'd be glad to go, like, look at them and start clicking buttons. I can do that.
No, so it's more like a general question. If you look at the number of PRs and try to categorize them, I kind of see, like, three…
three types. Can you look at the, like.
**jmacdonald** 28:32 carry on.
**Reiley** 28:33 You saw the PRs?
**jmacdonald** 28:34 Yep.
**Reiley** 28:37 Okay, so now it's 25, and,
the… the first, set of things are the… the thing marked as do not merge, as you see there a lot, and seems to be both generated.
**Jack Berg** 28:52 No, this person, Fractal Wrench, is.
**jmacdonald** 28:55 Yeah, that's…
**Jack Berg** 28:56 They're… they're one of the maintainers for this new Kotlin SIG.
**Carlos Alberto Cortez** 29:00 Yeah, correct. Actually, I was talking to him because he was a little bit confused, and I promised him to review these things, but we had a call on that.
Because, honestly, he's, getting onboarded.
And he… I think this is the first time he's working in an open source project.
And I mentioned that I wanted the PRs to be only 2, but then I didn't realize that he kept other… other ones open, so I will check that after. So give me a couple of hours, and I can…
a close recommend. But yeah, we shouldn't have this many from Fractal, you know?
**jmacdonald** 29:34 I also don't like seeing so many old PRs, honestly. I would probably… I don't ever look…
Below, let's say, stable by default.
Like…
anything before December 30th, I'm not sure I want to look at it ever again, and I don't know… and I feel that way across many repositories. Do you all have feelings about
everything below… Including Dash… including David's.
No, I would include David's in the list of things that we haven't finished yet from December, but, like.
**Reiley** 30:05 Yeah, so my…
**jmacdonald** 30:06 Okay, I keep looking at these and be like, yeah, those are happening.
**Reiley** 30:11 So my share is we have some old PRs there, and people still want to make progress. Like, otherwise it will be automatically closed, right?
**jmacdonald** 30:20 It's all been… it's all about.
**Reiley** 30:21 We keep removing the stale tag, and sometimes, like, I think we don't have enough TC coverage, so, like, everyone was assuming it's taken care of by someone else.
And that, that looks bad for the community.
**jmacdonald** 30:41 So Riley, since I'm on the call, should I… are you recommending that I go spend some time on this? Because I will.
**Reiley** 30:48 I'm not, I feel we need to have some accountability here, like.
Previously, we had this, like, assignment, so someone will be assigned on a PR.
And I… I think that would be a good approach. Like, if we're saying… if it's less, then we don't bother, but if we're seeing more, maybe we should use this meeting to say, oh, we have this 3PR, and what makes sense for this PR? Like, maybe this PR should be handled by Riley, that PR, like, Jack, should follow up.
**Carlos Alberto Cortez** 31:15 So, my take on this is that we have been probably been busy for this month. Usually, like, people like Josh, myself.
Or you yourself, Riley, like, we are paying attention, and we are merging things as soon as they seem ready, but I think we're just having it slow. Honestly, I don't think it's a problem, and probably to just start the year.
And actually, I'm going through the PRs now, and I see a pair of, like, two or three that have more than enough reviews and can be merged right now. It's just that we have been busy doing different stuff.
**Reiley** 31:46 Yeah, probably merged 5 in the past week. That's why we're down from, like, 30 to 25, but there's still, like, some old PRs. When I look at it, I have no idea. Like, I have zero contacts. Then my question is, do I need to spend, like, a couple hours to pick up the contacts, or maybe
Carlos, you already have the contacts you're working on, I don't know. So, in this way, like, I'm betting with some Microsoft work, so I'll assume, okay, someone else is taking care of that.
then after another week, I bet you that the PR is still there, and no TC member is going to give a comment, so that's my question. What should I do?
**Carlos Alberto Cortez** 32:20 Okay, yeah. Yeah, that's a good call. Okay, I guess that, yeah, the point is that if you're a FTC member and you already have contacts on something of the, you know, here, just go and merge that one.
If you are bumming, as long as you're confident.
I wouldn't do the cold.
**Jack Berg** 32:34 Well, I agree with Riley on this. So, like, at one point we had, you know, I think what Riley's saying is that, like, it'd be good if every PR that was open had an assignee to it.
Right? And, because at least then, me, I know that, like, Riley is largely, like, shepherding this PR, and, you know, maybe I'm doing another set of ones, and, like, you know, somebody is already caught up on the context, and I don't need to spend all that effort doing it myself.
And so, at one point, we had round robin assignees, and that didn't really make sense, because nobody was listening to it, and and, you know, everyone was getting assigned PRs that, like,
you know.
too many and were irrelevant to their, you know, domains of expertise. And so, you know, I'm with Riley. If we can, like, add… I think it'd be good if we could add a sort of section to this meeting on a weekly basis to go through unassigned PRs and find the most appropriate person to be responsible for, you know, staying up to date with them.
And if we couple that with, like, a posture of, like, hey.
if it's okay to get stalled out on a PR, to, like, have to go work on other things, like, we can close PRs and reopen them when they're relevant again.
Right? Like, I have a PR that's open that I'm still, like, working on, but, you know, I'm waiting for things, so I should close that PR, and when it's relevant for people to look at again, reopen it.
**jmacdonald** 33:51 I agree.
**Jack Berg** 33:51 If we can do that, then we can keep this more tidy.
**jmacdonald** 33:54 And I also worry, like, I would love to close these 5 PRs right now, but I fear I'm gonna offend someone, and anyway, there's… there's social dynamics here. Yeah.
**Reiley** 34:02 Yeah, exactly. And another, if you look at the misspelled PR, there's an info perform to switch.
The one just next to it, yeah. So that PR touched about, like, 90 files, I think.
If you look at the numeral file… oh, no, there's another change, another PR touchline. Oh, the other one, yeah. So when I open that, like, I'm running out of memory.
**jmacdonald** 34:27 Perfect.
**Reiley** 34:29 Yucks.
**jmacdonald** 34:30 Hey, Noah?
**Liudmila Molkova** 34:31 Yeah, there are draft PRs that is probably fine to keep open and not assigned to anybody. I support the suggestion of signing things. I think we should not assign OTAPs, because if nobody wants to look at the ATAP, it's also a sign that, okay, maybe nobody is interested in it.
**Reiley** 34:50 Yep.
**Jack Berg** 34:51 That's a good call-out.
**Reiley** 34:53 Yeah, for this one, like, I also feel the social…
like, the social dynamics there. If, like, Josh seems to have gone through the PR and made some suggestions, I…
I reviewed 50%, then I got a call from someone, I came back, I got lost, I have to start over. So, I have an intention to ask the author to
abandon this PR and break that into smaller, like, PRs. Maybe, like, 5 files or 10 files each time.
But I'm not sure, like, if Josh is going to give approval, like, he already reviewed the PR, right?
**jmacdonald** 35:29 It's assigned to Josh now.
**Liudmila Molkova** 35:32 This is also a good place for us to collectively see if the PR makes sense at all, and if it brings enough value to be merged, and maybe we could somewhat collectively say sometimes we don't want it.
**Reiley** 35:46 Yeah, so I pinged Josh multiple times last week, because the same author, he created a PR, like, last year, I think in November, and he fixed a lot of typos. Those are, like, awesome. But the problem is that that PR is touching a lot of files, and when people update the spec.
the author keeps, running into merge conflict, and we have to manually resolve a lot of things, and almost, like, every week, you go and resolve something. So I… I try to push for that PR to be merged, because
Anyways, it's typo fixed. It's great, right? Then, the author seems to be…
pretty encouraged by that, then we end up with more PRs. Those are great, but I… I'm lost when I… whenever I see a PR with, like, 94 files, I have this, like, very tiny scroll bar.
**jmacdonald** 36:37 Yep.
**Reiley** 36:38 Carl's?
**Carlos Alberto Cortez** 36:39 Yeah, I want to say, two things. The first one is on the editorial side, that I feel the same, and I think that the correct call is telling him to split things, because
I remember old PR that he sent, this person, and there are things that are totally fine, and they are giving great, but there are parts I don't like to see, and I don't want to be talking to him about, please fix this, I don't like this, I disagree with this, the rest is fine, you know? So, I think we should do that,
A lot of things, honestly, feel like…
Yeah, they are not good, in general. So we can, you know, splitting that
That should help. The second thing is that I do remember, actually, in the past, that we were trying very hard that before anybody sends a PR,
they have to fill an issue, and then the issue is reviewed by the TC and all that, and then if there's no issue, there's no PR. But I think that we should try to enforce that. And that was the idea, for example, with OTEPs. Like, before you open an OTEP, you open an issue, we discuss that, then that issue, once it's assigned, it gets a TCME,
And then you are basically driving that, you know? So probably we should go back and create issues first.
And then do the usual, you know, path of the GC reviewing them and assigning that to us.
When there are… when there are actually bug fixes, probably we can… we don't have that, and then we can do, as Jack said, which could be assigning things to ourselves in this call. Around robbing, I don't think that will work at all.
**Jack Berg** 38:12 Yeah, so just, like, maybe we have the processes for this, and we've been sort of, we've been skipping the process a little bit, and getting clutter as a result. I think there are some classes of PRs which, you know, requesting an issue is too cumbersome, and you mentioned bug fixes.
Maybe that's one. I think maybe we could debate about that, but, like, the spec compliance matrix updates, like, that's kind of silly, because you just… that's when a maintainer for a language is just, like, find some time to update their status. That… we don't want issues for that. So…
Yeah, like, I'm with you, Carlos. Like, let's follow our own process better, defer, you know, PR openers to open an issue first, and if we wanted to, maybe we could get us… we could call out some of these exceptions in our… in our contributing guide, like, that you don't need an issue for, spec compliance updates, something like that.
**Carlos Alberto Cortez** 39:08 Yep, it would be good.
**Liudmila Molkova** 39:12 I kind of feel hesitant about it, because first, we are breaking this rule ourselves.
And everybody does. Second, we're… The only reason, the only way to not break it.
Is to have enforcements in place, and building these enforcements
is not a good use of anybody's time, I think.
**Jack Berg** 39:38 But then, like, to take the other side, Ludimo, if we… if we have a process and we're not gonna enforce it, either automated or manually, then, like, why do we have the process at all? Like…
Doesn't that suggest we should delete the process? And, you know, I wouldn't advocate for that.
**Liudmila Molkova** 39:59 Yes, I mean, if… this is a subjective judgment of whether the PR deserves an issue.
Okay. And the subjective judgment, needs to be applied, somehow.
**Carlos Alberto Cortez** 40:24 I remember… I don't remember where I saw that… well, this was a silly thing, probably, but it said if your PR represents more than 20 lines, or what…
you have to fill an issue, something like that. Sadly, we cannot apply that here, because probably it's one line change, but it's changing from moss to shoes, or the other way around, and then we are destroyed.
**Reiley** 40:44 Yeah, I…
**Carlos Alberto Cortez** 40:44 We're just…
**Reiley** 40:45 I'll check, and then it's… it's trivial.
Yeah, I have some idea, I can probably look into this. I feel this is similar to changelog. Like, if we're saying this is enforced, but these are some exceptions, and this is subjective, but if you believe you don't need a changelog, and
you don't need to create an issue. There's a tag you can apply to the PR.
So this is a conscious choice.
**Jack Berg** 41:12 Yeah, so no change log, no issue. Like, it's a heuristic.
**jmacdonald** 41:16 It's called Skip Change Log in the Collector.
**Reiley** 41:19 Yeah, we also have the same thing in the SPAC repo.
**jmacdonald** 41:23 Alright, yes.
**Reiley** 41:24 So we'll just say skip issue or no issue or something, like, similar. But that's an explicit action.
Essentially, like, if you create a PR, you better think about it before you apply the tag.
**jmacdonald** 41:40 So, I think I missed something. Are we proposing to, like, auto-close PRs that don't have issues?
**Reiley** 41:47 No.
We're trying to enforce it, so if you create a PR without an issue, you will get blocked. The PR will show red.
And then it will tell you in the error message saying you don't have an issue associated with the PR, and here's the general guidance, like, how to contribute doc from the SPAC.
It's logically auto-closing. I'm making a very small change, so I'm going to tag this with, like, no issue. Then go and do it.
Sorry, Gamila.
**Liudmila Molkova** 42:18 It's logical that we ought to close it then.
Why?
**Reiley** 42:23 But we have the same thing for… for, like, skip changelog, right? So I feel like instead of close, it's like, just don't bother us, go away. This one is like, we block your PR, and if you don't take action, then after a certain number of days, the PR will mark as still, and then it'll get automatically closed.
So that, that seems like a reasonable balance.
**jmacdonald** 42:46 Are you sort of… are we saying that if you don't put an issue, we're gonna give you, like, one day for staleness? If you do put an issue, you can have three weeks or whatever.
**Reiley** 42:56 I mean, if someone can write that code, it's fine.
**jmacdonald** 42:59 I'm sure…
**Reiley** 43:00 I'll copyright that code.
**David Ashpole (dashpole)** 43:02 I mean, it's doable.
**Reiley** 43:03 I don't want to make it too complex.
**David Ashpole (dashpole)** 43:08 I've generally found that auto-closing issues can come across as a little bit rude.
**jmacdonald** 43:14 Yeah.
**Jack Berg** 43:16 I think if it's, like, if the auto-close comes with a message that, like, communicates, like, hey, we're closing this, but this is temporary, this is just for our process, you know, feel free to go open this, reopen this if you think that we got this wrong, or something to that effect. You can kind of
Reduce the, the kind of social tension.
What if, like, what if we did something like a combination of this? If we, as part of the TC meeting, make sure that any non-OTEP PR has, like, a TC member assigned to it that is responsible for…
for just, like, interpreting it, like, you know, figuring out if it already has an issue, and if so, you know, shepherding it along in whatever way makes sense. Or, if it's not appropriate, giving the user guidance about, like, hey, you need to go follow our process, you need to open an issue first, and we're going to block it until then.
And, you know, maybe we can automate all this later, but for now, I feel like, you know, if we do a pseudo-round robin that's, like, done manually in the TC meeting, there's not so many new issues on a weekly basis that this would overwhelm me.
Right? You know, the number of issues divided by 10. The number of new issues per week divided by 10 would be, like, half of an issue per week for me.
That's not… that's not that many.
**David Ashpole (dashpole)** 44:44 it might be helpful just to go through and tag the relevant groups. Like, this one is at Metric Spec Approvers, this one is at… I feel like usually when people see an issue that's in their domain.
They hop on it, or…
**jmacdonald** 44:58 Yeah, I was gonna say, like, I feel very comfortable with David's PRs, and I can help him with them, but I don't feel comfortable with any of the entity PRs, and I'm kind of waiting for Josh or somebody to, like, do something there, and there's a bunch of them.
**Jack Berg** 45:11 Well, and that's why I'm suggesting, like, so, just to be more concrete, I'm suggesting as part of our TC meeting, we have a short triage session at the beginning, where we're doing this assignment, and the assignment, it's not true round robin. It's not random. We're using the context that we know, where we, you know, everybody has their different areas of expertise.
And so, we assigned Josh Surreath to the entities one. We assign, you know, some combination of, like, Josh McDonald to sampling, and, you know, some of us to metrics ones, and things like that.
**Liudmila Molkova** 45:44 How do we feel? Because we have… not sure if we… yeah, we have spec maintainer role.
And essentially, in the spirit of delegation and expanding the community, we should Spec maintainers should own it.
And then it belongs in the SPAC meeting.
And SPAC meeting is sometimes brave, sometimes very… Long.
But logically, it should happen at the SPAC meeting, and we should assign any SPAC sponsor to the related area.
**Jack Berg** 46:16 Yeah, I'm with you, but we don't have spec maintainers right now, we have spec sponsors, and it's a little bit different because they don't actually have merge rights. So, like, effectively, right now, the TC is the spec maintainers. I'm in favor of creating a proper spec maintainer role that is disjoint from the TC, but, like, you know, I don't know, at that point, I think that it would be, you know, a proper
you know, task for the specification meeting. Until then.
We're effectively the spec maintainers.
**Liudmila Molkova** 46:43 Agree.
**jmacdonald** 46:47 I'm sort of just, like, enjoying this process where I assign people. I'm assigning Tigran Josh's PRs, and I'm assigning Josh Dimitri's PRs.
But, so, so, if this is our triage session here, then,
what I hear is that we should be going through this, you know, I've started assigning some… some of these are about to merge.
Some of these are OTEPs. Oh, wow, two of them are already merged.
Right? We're down to 22, Riley.
**Reiley** 47:19 Yeah.
**jmacdonald** 47:19 So… So…
We've triaged some of this. I just looked through them all. I don't know that there's much more, since it's old stuff.
I, you know, switching from Seaspell.
I have a, like, I don't know. I… linters get me, you know, like, trouble versus how much they're worth.
But…
So, we should probably just have, like, somebody push this button and deal with it, people. Deal with your merge conflicts.
I'm gonna assign this to myself.
We can, jack, we can move on to your, next item, the packaging SIG.
**Jack Berg** 48:01 Okay, so, you know, it seems like we have at least soft consensus about this. There's not all the TC members here. At the beginning of the next TC meeting, I'll bring this up again as, like, the first item on the agenda. We can collect feedback from other people and just, like, see if it's working or not, and go from there.
But, you know, hopefully in, like, a week's time, every PR has, like, that isn't an OTEP, has, like, a TC member assigned to it, and then we can… it'll be a small amount of work to keep that up on an ongoing basis.
**jmacdonald** 48:33 Alright.
**Jack Berg** 48:35 All right, I have the next topic. So I was just at Hotel Unplugged in Fostum in Europe, and there's, you know, Ludmila was there, I think she was the only other TC member, but there's, there's been a lot of talk, and there's an OTEP, related about, like, packaging.
And so, I just wanted to sort of give a brief summary to the TC about some of the thinking here, so, to kind of connect everyone together, so that we don't have these kind of disjoint conversations.
So, roughly the idea is some folks think that it's really important to be able to have a Linux package, you know, Debian or RPM, called OpenTelemetry.
And, you know, the idea would be, you can just say, apt get install open telemetry. And the question is, what should happen when you call install open telemetry? What components get installed? What's their configuration? You know, but…
you know, the point is, is that there's value in us coming up with a simple, opinionated install flow for OpenTelemetry on Linux.
And, yeah, that's what the packaging sig is all about. Like, you know, coming up with the package topology, like, you know, what are the different packages, what are their dependencies between them, you know, how do you use them in a sort of,
in a modular way, like, you know, we don't want to force everybody to use this, like, kind of super package open telemetry. Maybe you can use, like, child packages on their own, things like that. But just, like, roughly, some of the things that might be installed and managed by this
OpenTelemetry package would be, like, the collector running as an agent on an agent mode on that local machine.
you know, the OpenTelemetry injector to install auto instrumentation packages automatically in all the appropriate languages.
Maybe something with eBPF. We got a lot of eBPF tools these days. We got OBI for lightweight, you know, APM-style observability. We got a profiling tool. There's a network observability tool. So, you know, how do all these things fit together? And so, yeah,
That's, like, kind of the packaging sig in a nutshell. I think it's kind of along this theme that people have been pushing on, of making OpenTelemetry easy, and kind of crossing the chasm, and you know, becoming extremely mainstream. There's this kind of ongoing critique that OpenTelemetry is a sort of enthusiast tool, where it's like a Swiss Army knife with a bunch of different parts.
And if you know everything really well, you can stitch them together and have a really great experience. But what if there was, like, an easy install experience that was, like, accessible to everybody, that wasn't kind of in the loop?
So that's kind of the… the problems that we're… that this group would be thinking about.
So if anybody's interested in participating, or if people on their teams would be, like, good fits for this, if they're, like, you know, Linux packaging experts, or, you know, kind of have good ideas for what an opinionated OpenTelemetry install flow should consist of, you know, I encourage you to go look at this… this OTEP on the community issue and participate.
Riley.
**Reiley** 51:50 Okay, I've got, two questions. The first one is,
Do you feel this sounds similar to this show? And, like, you want to… like…
like, people think about, like, aligning the term there, it's just another distro, maybe a jumbo distro or something, or…
this is a totally different concept. The second one is, you know, we have…
like, some feedback from CNCF during the graduation push, that, customers already, get some feedback about, hey, like, we just installed this, like.
OpenTelemetry XYZ component, and then we ended up with all this, like, breaking changes, unstable stuff. So now it seems…
We're trying to say, let's just bundle all this, like, unstable stuff together to give you a jumbo package, and it appears to be easier for the user.
like, once you make it super accessible, it's like, if you have an engine, the engine has no problem, but only the car manufacturer can ship it. But now you make the engine super available on Amazon, everyone can buy it and swap the engine, then there might be more negative feedback, so what's the sentiment there?
like, I can imagine if they make it super clear that these are, like, alpha version, then probably fine. But I, like, I can always imagine, because
OpenTelemetry is, something, like, I imagine, like, all the software developers would use at some point, so this will become very hard, and people use that, and if we don't do it with a high-quality bar, then the negative feedback might come faster than we thought.
**Jack Berg** 53:29 Yeah, I'm with you, right? And so, just on the… to address the last thing you said, like, I installed Ubuntu on a fresh machine the other day, and like, in the install flow, I was prompted to select if I wanted to install any of these really common, popular packages by default.
things like, you know, OpenSSH and things that, like, a lot, a lot of users install. Like, what if OpenTelemetry could be in that list that Ubuntu prompted me to install in, like, you know, 10 to 12 packages? Like, that'd be a really good future to get to. But in terms of, you know, these trade-offs, right? So, like, we have all these packages… we have all these components which are being orchestrated by this OpenTelemetry package.
All different levels of stability, potential braking changes, things like that.
Yeah, so, like, I…
I have thoughts on this, I don't have, like, answers, because this is all, like, an emerging space.
I think the sort of stable by default things that we've been talking about with Austin Zotep become particularly important here. Like, you need to have a high-quality bar to get into this default package, or to be included as… and, like, turned on by default in this package.
And, like, another thought is, like, you know, you have all these components which could potentially be installed at the same time. Something has to be doing orchestration to make sure those things work well together. Like, a classic example is OBI does, like, has, you know, wide breadth of instrumentation, but not a lot of depth.
and the injector is simultaneously installing, like, you know, auto instrumentation modules and SDKs.
Those are going to be double-dipping. How do you make sure that those components are installed in such a way that they don't, step on each other, and that, you know, they collaborate versus, you know, get in each other's way?
And yeah, like, all sorts of interesting questions with this, which is why, like, I think it has to be a SIG. Somebody has to sort of identify what are the, you know, the key decisions to make that will allow this to either be successful or fall on its face, and make sure we get good answers to those.
on the distribution question, I don't, I don't, I don't know, is this a distribution or something else? Like.
vocabulary. Like, all sorts of words carry different, sort of, preconceived notions about what they mean, and yeah, I don't know whether this type of thing, it meets people's intuition about what a distribution is, or whether we should come up with a different term.
**Reiley** 55:59 For example, like, the collector has a couple distributions. The OpenTelemetry demo also has distributions. If the packaging seed, like, officially, like, started, maybe they should own those components.
**Jack Berg** 56:19 The demo and the collector? Is that what you were saying?
**Reiley** 56:22 example, if the collector maintainers decides, we're going to use this, like, you can… you can use, like, APT install OpenTelemetry Collector, then the packaging sake has a different opinion, who should own that.
**Jack Berg** 56:34 Yeah, right, like, there's this question… there's this… there will be an ongoing question of ownership. The packaging SIG is hopefully going to collect people from a bunch of different sub-areas of OpenTelemetry and bring them together to kind of work in a collaborative way in some way. But then there's, like, ownership boundaries, like, hey, to what extent does the packaging SIG own the integration of the collector subpackage?
Versus the collector SIG owns that.
Right? So, the packaging's say…
If they own it, the more they own of it, the more coherence they have, because they can ensure that it works consistently and in a coherent way with the other sub-packages, but the more the collector owns it, like, you know, the more that will be sort of in touch and in sync with the things that are ongoing with the collector community. So there's a tension.
**Reiley** 57:25 Yeah, and they also own the security now, because if they package everything, then they have all the CVEs.
**Jack Berg** 57:32 Right, the best case, in my opinion, would be some sort of, like, hybrid thing, where there's sort of, participants from the collector also participating in the packaging SIG, and they can, like, act as liaisons between both SIGs, and make sure that everything is, like, sensible and coherent.
**Reiley** 57:49 Yeah.
**Jack Berg** 57:56 Coming up on time.
**jmacdonald** 57:58 Yeah, so that's… I mean, this is a great sign of maturity, like, packages sound good, they're gonna be hard.
Time is here. Thank you all. I think we end it, I will follow up on the, the, the thing we said we would follow up on. I'll… the…
Top of the item, the issue about concurrency, I'll follow up with. Jack said he would, too.
And, triage, we'll talk about that next Tuesday, and I'll see you next week.
**Jack Berg** 58:26 See ya.
**Liudmila Molkova** 58:27 Alright, beautiful.
