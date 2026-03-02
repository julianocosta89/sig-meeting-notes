SIG: Go SIG
Date: 2025-08-28
Duration: 45 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn** 00:15 Hey, Brian.
Hey, Robert.
**Robert Pająk** 00:47 Hello, hello.
**Tyler Yahn** 00:50 How's it going?
**Robert Pająk** 00:52 It's good.
How old you?
**Tyler Yahn** 00:55 Yeah.
Good.
Yeah, busy.
**Robert Pająk** 01:01 It's always….
**Tyler Yahn** 01:02 Yeah, right.
**Robert Pająk** 01:05 Damien's not gonna join today….
**Tyler Yahn** 01:09 Yeah, thanks, I was just looking for that.
David, I'm guessing, as well, right?
**Robert Pająk** 01:14 Yes.
Sam is here.
**Tyler Yahn** 01:17 Oh, yep, there's Sam.
**Sam Xie** 01:20 A….
**Tyler Yahn** 01:22 Hey.
**Robert Pająk** 01:28 I see… Oh, we saw Brian two times, so….
**Bryan Boreham** 01:33 Yeah, I was here twice. I'm….
**Robert Pająk** 01:35 Yeah.
**Bryan Boreham** 01:35 I'm not powerful.
**Tyler Yahn** 01:40 Yeah. Well, cool. Alright, I think it actually that might be Quorum, then. …
So we can jump in here. If you haven't yet, please go ahead and add your name to the attendees list, and if you have agenda items you wanted to talk about, please go ahead and add them as well, and … we can…
Start by… Sharing my screen.
Yum.
Okay, cool.
Alright, so to start us off, I wanted to talk about the SDK observability. So this is an issue that we've had for a while, and we've had a lot of work on it as well.
…
So, I've done a lot of reviews, and I've done a lot of fixes to things, and changes to things, and…
…
there's still a lot more to go. There's 14 more issues to resolve here. And so I think that, like, there's a lot of things that we probably want to try to, like, document to try to just…
change for the better, in some sort of, design and best practices for this observability.
I think there's been a lot of, definitely, like, review things that I've noticed I've just repeated, mostly just because a lot of things were copied, so, like, it's not really, like…
it's not anybody's fault, like, you know, spelling mistakes or something like that. It's just more about, like, trying to head these sort of things off, as well as, like, just patterns in general that we want to try to, address.
So I've kind of captured what I have just seemed to find multiple times
Commenting on, as well as just, like, general design practices.
I think that maybe we could go through these, but I'm just wondering, like, does this seem reasonable? And, like, where should we keep this? Like, does this need to exist? I mean, probably in the long term, it probably should exist in our contributing documentation, …
Or the contributing documentation needs to get refactored into also having some sort of, like, design and best practices thing that it can reference, because it's getting pretty long as well.
So, I… yeah, I'm…
I'm open to thought, maybe that's just… I'll just stop there before we even review this. Thoughts on where this should live, or if it should live in just this issue?
**Robert Pająk** 04:07 I think Contributing MD, or a place where it is ref… it can be even a separate document, but reference from Contributing MD is the place place, because I imagine even when we do it now, we'll have new signals, new exporters, so this…
so these guidelines will be, you know, continuously needed, probably. And also, if there will be some bugs, etc, we can double-check with this. And also, Tyler, I just also want to thank you on taking a look at it, because my initial
perspective on this feature was, let's have kind of anything, it's experimental, just to have the semantic conventions going, but I think your approach is better, because with this performance overhead, it might not be acceptable, and people will say that it's a crap.
Basically. So I think that's… yeah.
**Tyler Yahn** 04:55 Yeah, I definitely think performance is definitely something we want to keep an eye on. Like you just said, like.
Yeah, I think people may try it out and be like, this is unusable, when we weren't really even thinking about it, you know? And so, like, I think that we need to probably think about this from the beginning, because it also will help implement the overall design. But…
Yeah, I think there's also just, like…
Yeah, so maybe we can go into the details here, but I think what I'm hearing from you is I'll try to maybe, like, after this, submit this to the BAPR for the contributing document.
I think that document's getting large, and I think we probably want to put this somewhere…
break that out into somewhere else, but, like, that's fine. It can live there for now. We can do that as a second step.
I have, like, kind of a high-level, checklist. This is just really all the other things that I've seen below, so, like, maybe we can just go through the design outline. So one of the things is definitely, like, this, side effects programming. This is definitely something where we have a lot of initialization methods that will take an object, and then it will do something to that object without returning anything.
it is, I think, like, problematic because it doesn't actually…
It's very much an imperative style, where, like, you don't know if something's been…
initialized, and if it has been initialized, what effect did that have? Does this need to exist here? Does this need to exist below? Like, there's a lot of, like, questions here, so I think we want to try to provide some, like, as pure a function as possible. Obviously, there's going to be, I think, some externalities here, because…
if I remember correctly, yeah, like, here, like, we're just looking for, we're literally looking for, you know, environment variables, but…
from the perspective of just, like, the coding, I think we try to make this inline as possible.
There's a few other examples there, but yeah, I think that's something I don't want to… I think that that was one thing that kind of stuck to me. One of the other things is, …
encapsulating this observability setup, so some sort of, like, thing to make this constructor, I think, make more sense, like…
One of the things that I did see, and it's kind of, something I also noticed, is, like, one of them… one of these prototypes has, like, a package called, I don't know, maybe self-observability or observability.
And I really liked that idea. I'm not necessarily saying it has to be in its own package, but I did like the idea of it being its own type, which it could then be totally encapsulated within that struct. It's kind of like…
you know, whether that lives in its own package or not, like, I think that there's…
reasons it should or should not, or… yeah. But, like, I think that, like, having something to abstract it, one of the things that you notice here is that, like.
you're already starting to see a lot of things, like, bleed into the original type, and so, like, you have a lot of fields that are getting populated here from the original type, and, like, this is fine, it's just that, like, it grows organically. And, like, you're starting to see things like, well, you have to know
you know, span and flight metrics is not something to do anything with the exporter, it has to do with observability, so encapsulating that in its own struct, I think, is probably also something I would recommend. I haven't been, but I think it's a positive thing. Robert, yeah?
**Robert Pająk** 07:57 I think, as well as the temp, can be simply
Separating to a separate file, which will usually involve creating a separate type, or at least pure functions, or things like that.
**Tyler Yahn** 08:10 Yeah, I agree. Like, I think at least a separate file, for really small things, I mean, I don't think there's a hard requirement, but I do think that, like, a separate file is very helpful.
I think if you have very complex, like, multi-orchestrated things that you need to isolate, having a different package, like an internal package, also makes a lot of sense. So, like.
Yeah, I mean, I think that we can make some recommendations there.
But I do think that we try to, like, stay away from what we're doing already, which is, bleeding observability, like, fields into the underlying type is kind of what I think we should try to not do, yeah.
Okay.
That's not really included here, I can try to make that a little bit more explicit, so, like, we can try to iterate on this. This was also just a first draft, so, if you have other suggestions, please, yeah, comments in this or the PR that I'm gonna open.
So yeah, next up, isolating and encapsulating the self-contained instrumentation. This is kind of what I was just talking about. Minimal hot path is kind of important, so the isolation's, like, really critical here, so, like.
when observability is disabled, like, code paths should be optimized, so, like, it should have little to no additional performance overhead. Obviously, like.
some sort of, like, if statement is kind of, like, the minimum, or even less, you know?
I guess, a function call that's a no-op is also, like, seems reasonable to me, but, like, we're looking on the orders of, like.
something that the compiler can optimize with branch prediction, or something that, like, is just, you know, a single CPU cycle to make a detection, is ideal. And then, like.
You know, memory as well, footprint, like, try to keep that small, is kind of, like, the recommendation here.
Yeah, so, like, I put, like, fast branch prediction, so doing something like this, which we do in almost all cases. This actually isn't something I've had a review for, it's more just, like, something I've noticed we already are doing, let's keep doing it. So yeah. And I think, yeah, maybe one thing was, like, deferring, instead of
It's a little bit different, but, like, deferring instead of…
Using the branch prediction, like, there's really no need, so, like, maybe we can make some… some…
recommendations around that. This was something I added that was just kind of…
It's… yeah, use T-Cleanup instead of deferring that, but that's not really related to this. I think this got merged in the wrong place. Anyways…
Moving on, performance optimization. So the attribute, and option allocation. So this is another thing that, like, kind of what, you were talking about, Robert, like, performance is kind of important here, because I think, well, for one, its usage is going to be really critical in people evaluating whether or not this is useful or not, but also, like.
Keep in mind, this is… this is going to become reference for a lot of people when they're building instrumentation, so when they're looking at this, they may say, like, this is the way to do it, and if we're doing something that's very, you know, not performant and not…
… something that should be copied, then that's going to be copied everywhere. …
So I think we try to, like, be the, you know, a good example here, and try to address these from the beginning.
One of the things is our, our attributes, … …
situation, I guess? It's one of my least favorite parts of our codebase, but anyways, like…
Our options to do this require allocations, because we use sets, attribute sets within metrics, and so, like, there's always going to be an allocation for each creation of a set, just because it's going to do some sort of copy into an array, from whatever the attribute values are, right?
It also is going to do, sorting of the input.
… Slice, which…
I was really hoping we could maybe try to fix that eventually. But anyways, this is the world we live in, and so, like, the idea is to maybe look into, …
you know, trying to do these copies to not mutate any sort of user input, trying to, you know, use sync pools to amortize any sort of allocations when we do know the exact explicit size. This becomes a little bit more nuanced, obviously, because, like, if you're accepting, like, a dynamic size of slices.
The pool size actually is really important, because, like, whatever it's new is always assumed that that is going to take, like, the same amount of time for every new allocation, so if you're dynamically changing the value that you're actually returning from within the pool, this can be very, like, tough on memory pressure, so there's a lot of nuance here, …
So maybe this can get spelled out a little bit more, but, like, I think this is kind of, like, keys to try to use that, …
Caching common attributes, this is something maybe we want to talk about in just a second. I think that there's this new idea of, like, trying to bind, especially for things that are just, like.
always going to exist. Like, there are definitely ways that you can, define things from the start on creation to remove any sort of allocations in the hot path, so let's try to do that. Whether we use a separate package or not, like, I think we should try to still do that.
Yeah, and so essentially, just like the hot path, you try to just, like, unless, like, you're in a very specific situation, like, where you can't, avoid an allocation, which they exist, like, if you need dynamically created
attributes that are not pre-known, like, there's no way to actually pre-allocate these things, because you have to create a set at some point. So, minimize it as much as you can in those situations.
Also benchmarking. I think from the start, we should have benchmarks. I think that micro-benchmarks for, like, what you're trying to introduce are important, but, like, we definitely want to see things, from the start that show
how this is performing, I think, for this exact reason that we want to provide something useful for users, and we want to provide, something that we can validate going on.
Correctness, there's context propagation, I just… that's something I keep seeing in, reviews. Partial failures need to get handled, correctly. Like, this is something that, like, if you are partially successful, you need to, like, in an export, show some of them were successful, some of them were not.
And deterministic testing, like, this is something for the IDs of the component, like, this needs to be something that's not gonna depend on, like, the testing structure.
I have examples of a lot of these things here.
And then, obviously, like, semantic conventions, this is something just to keep in mind, like, yeah, like…
Again, not something that has been missing, just we want to keep following these sort of things.
Yeah, and then I put some, you know, more examples of, like, attribute pooling. This is incomplete, really. It's just kind of like a stub, essentially, for a lot of these things. But yeah, these are kind of, like, the main points that I wanted to include in this that I've seen a lot in this review.
If there's other things that people have, I'd love to hear about them now. I'd love to also, if you want to think about it, if you want to just maybe add a comment to this issue, that'd be great, and I can try to include them as well in the PR that I'm going to try to put out.
Okay.
**Robert Pająk** 15:09 one comment in the chat, I don't know if you want to look at it now. Basically, the structure, I don't know… I guess you had read the S-Log handler guide, right? When you were implementing the S-Log breach, if I remember correctly. So this kind of even structure reminds me of this. I think it can be also used as a reference.
**Tyler Yahn** 15:30 ….
**Robert Pająk** 15:31 Good idea.
**Tyler Yahn** 15:32 I… I don't… if I did, I don't remember.
**Robert Pająk** 15:35 So, I put it in the chat, if you want, I can put it in the comments.
**Tyler Yahn** 15:39 Yeah, if you put it in the Zoom chat, please put it in this comment, so then it doesn't get lost after the meeting. It'd be ideal. Yeah, yeah, thanks. Yeah, if there's already existing references, like, that'd be great. Let's try to keep doing that, yeah.
… Okay.
So, on this idea of, caching common attribute sets for repeated measurements, this is something else I wanted to take a look at. There's this proposal, like.
There's a lot of iteration on this, …
standard.trace exporter, if I remember? Yeah, standard.trace exporter.
And, we got to the point where, like, we're doing, I think, a pretty good job in trying to avoid allocations where possible. Like, there are still some in error conditions, …
That being said, like, it required a lot of, pools, it required a lot of… it required a lot of code, I think is kind of the idea, and a lot of that code is just reusable code, so when we're doing things like this, where
We're recording an in-flight, metric. We're always adding it with, like, the same attributes, hence why we're always adding
the self-observability attributes. Sometimes if there's an error, we're going to be adding additional error, types, but, like, for the non-error case, it's always going to be adding the same.
So, this is one thing that, like, has existed for a long time as missing in the OTEL API for metrics, is, like, the ability to just bind an instrument to attributes you always will be measuring with.
I created this package called Bind itself, and, it does that for you.
Actually, I updated it, yesterday to do this even simpler. Essentially, what you're doing is you pass in… you can do it on an instrument level, or you can do it at the meter, as well. This is something that I also added. When you do it at the meter, this component attribute and this component type attribute.
will be bound to any instrument that's created from the meter, synchronous instrument. Yeah, the asynchronous instruments, that's… that's on you. You have to record those in a, callback, so if you're gonna do an optimization, like, you would already be doing it there. But let's just say, like.
just to clarify, it's all, when I say instruments, it's synchronous instruments here.
we're only using synchronous instruments in this as well. So what that's doing is it holds, essentially these two values, this option and this key value are cached within this type itself, and so there's no allocations when
the measurement actually happens. When a new instrument happens, it does make, I think, one additional allocation, but that's, again, like.
covered here, in the setup, it's already done. So in the hot path, we're no longer doing that. So you're able to take away all of these pools. These pools are…
Common within the, actual, … package itself.
And, it…
it cleans up the code a lot. You don't have to do any of this pool management, like, these call sites don't pass any additional attributes, unless you're doing something like this, where…
you want to pass in an additional attribute because you're in an error situation. So, I think that, like, this is pretty helpful. I haven't… I've been looking through other parts of the code. I do think this is going to be helpful in other exporter, things, where this is always a very common attribute that has to be included.
So I was wondering if this is just a proposal right now, like, if we want to include this. Right now, this bind package is not stable, and it's owned by, in my GitHub organization.
where that ownership, I think, comes in, like, Robert and I have kind of talked about this. I just put it there because the hotel organization's pretty adverse to adding these one-off packages, that are not, like, high-level offerings of products from, from, like, Go, from the Go perspective in, like, OTEL, so keeping it there was kind of my idea.
There's obviously a few other places it could exist, it could exist here, … I don't think we want to expose it as a public type, because that's not the…
The metrics API actually needs to have its own bind implementation, and that needs to be
defined by the specifications, so defining this as a public package inside the OTEL ecosystem is not ideal. Defining it internal would mean that we'd have cross-module dependencies, which means that we would want to generate this. It's quite a large package, which I don't think we want to generate, …
So, I, you know, and I think we're just getting around the typing system by doing that generation.
Putting it in contribib means that there's going to be a cyclic dependency on contribib and OTEL. It's not something that we can't do, but it is something that's extremely annoying in, like, updates. You'll never actually be fully updated at that point. So there's, like, I think reason to keep it external here.
I'm fine releasing this as stable as a 1.0. I'm also fine including anybody who wants to collaborate on this as a collaborator to the project. I'm also fine…
moving this to, some other organization, something like that. So, like, where this should live, I don't know. I think this is fine. I'm happy to include more collaborators on it.
But I'm looking, I guess, for feedback if this is a proposal that we're okay with moving forward on.
**Robert Pająk** 21:00 So, maybe I can start. So, from my perspective, having even, like.
In your, like, in your account, like, bounded to your account when it's stable.
It should not be an issue, we can always fork it and do whatever later.
And I think it's the most straightforward approach, unless anyone has concerns for it.
**Tyler Yahn** 21:25 Yeah.
**Robert Pająk** 21:26 As you told, you can give always, you know, permissions for us, etc.
So, I think it makes it simpler, and we can just move faster this way. But just… this is just my opinion.
I reviewed the code, and it looks good, good enough to make it stable, in my opinion.
**Tyler Yahn** 21:45 Cool, yeah, thanks for reviewing. That's a good point, I forgot to mention, like, we can always, like you said, fork it. If there's ever an issue, we can fork from a specific version, too, so… or, just pull it out.
Completely. So, yeah, however we want to, like, move forward in the future. I don't plan on… …
I plan on supporting it in the future, but if that ever changed, like, … thing.
**Robert Pająk** 22:13 What is important, that even if we mark it at stable.
and we need a breaking change, we just make a V2 of it, and we don't have any conflicts, you know, building modules, etc. So, I think it's safe
Assuming it's, it's stable.
**Tyler Yahn** 22:32 And I do think that, like, there's a long-term deprecation strategy as well if, the Metrics API does allow you to start binding, instruments as well, so, like…
Yeah, like, I think that's also an endgame there as well. I don't have any…
Expectation that's gonna happen soon, though.
If at all. But anyways, okay.
I can change this from a draft to a…
ready for review after the call then, and we can get more thoughts on it. Obviously, it's tough to think of.
**Robert Pająk** 23:04 I just now… I just now realized one thing. …
This bind package was creating a new meter, Or am I wrong?
**Tyler Yahn** 23:16 It was, yeah.
It was wrapping the meter, yes.
**Robert Pająk** 23:20 Yes, it's a wrapping emitter.
So, the only potential thing which may be good to call out, what will happen if there will be new functions that are added to the meter, like, you know, new instruments?
**Tyler Yahn** 23:36 Yeah, it wraps the meter type, it doesn't wrap embedded meter.
**Robert Pająk** 23:42 So.
**Tyler Yahn** 23:43 Whatever… whatever is added there is added here, as well, was kind of the….
**Robert Pająk** 23:48 So that's… That's good.
**Tyler Yahn** 23:51 Yeah, yeah. This is obviously a runtime panic, but it… since we're wrapping something that's coming from the user anyways, like.
If the user's meter doesn't implement the meter, then that's what the behavior is.
**Robert Pająk** 24:03 Yeah, but let's assume that we are putting the meter from the SDK, right?
Like, like, I….
**Tyler Yahn** 24:12 Yeah, yeah.
**Robert Pająk** 24:13 I mean that in typical scenarios, it won't create any issues. If it will panic, it will also panic in other cases, even if this package is not used.
**Tyler Yahn** 24:23 Yeah, that's what I'm saying. Like, if there's no error from the user's past meter, there won't be an error here, and if there is.
**Robert Pająk** 24:29 Exactly.
**Tyler Yahn** 24:30 It's just whatever the user gave us, so, yeah.
Yeah, okay. We can keep taking a look at this, then.
Okay.
Next up.
wanted to talk about, release of the 138, I think we're there, and so…
Way overdue off for this one, and so I would like to get this out, hopefully sooner rather than later.
The, …
There was another PR in here that I moved to the 139, and that was to do with the instrument attributes. I don't think that that's…
ready to merge as it is, and I'd like to get this out within the next day or two.
We can obviously, like, if we need to do a patch release afterwards, I'm fine with that as well, but I'd like to progress this one that's been…
I think it's 2 months since we've had a full release, so I want to keep this going. …
I think the more important.
**Robert Pająk** 25:31 Could you just quickly say what's concerning in this PR, if there are big changes to be addressed?
Because….
**Tyler Yahn** 25:39 Semantic conventions?
**Robert Pająk** 25:43 No, no, no, I mean the one related to with instrument options.
Because this is.
**Tyler Yahn** 25:49 Oh, good.
**Robert Pająk** 25:49 But you probably moved to the later milestone, right?
**Tyler Yahn** 25:52 This, this one here?
**Robert Pająk** 25:54 Yes.
**Tyler Yahn** 25:56 Well, yeah, first off, I don't think this is a bug.
There's no….
**Robert Pająk** 26:01 I think….
**Tyler Yahn** 26:01 There's no concurrency guarantees on this function, there's no concurrency guarantees on the option type.
And they're using it in a concurrent way that's assuming it's concurrent safe.
So, I… like, that… that's not….
**Robert Pająk** 26:13 That's true, you are right.
in the SDK, it's always synchronized, right? The calls to it.
**Tyler Yahn** 26:23 Yeah, and so, like….
**Robert Pająk** 26:24 I see. Calls to, like, meter, or Tracer, or logger, like, those are concurrence safe. Like, we don't provide any guarantees on the options that you pass to them. Like, if you're gonna share those across Go routines.
**Tyler Yahn** 26:35 I think that you may, like…
Yeah, I don't think that the current behavior is appropriate for another reason, but I do think that, like.
trying to say that this is concurrent safe, is not right. First off, like, it's not documented as concurrent safe, this isn't changing it to be documented as concurrent safe, but it's just testing it to be concurrent safe when it shouldn't… shouldn't be assumed to be. I do think that… that, it is… this is something, like, I mean.
**Robert Pająk** 27:01 Yeah, yeah, I see. Yes, I agree.
**Tyler Yahn** 27:04 It's the same reason that, like, if you pass a slice to something that's concurrent safe, and then you modify the slice another.
**Robert Pająk** 27:08 Yes, of course. Yes, of course.
**Tyler Yahn** 27:10 you're… you're doing something wrong. And so, I do think, though, that, …
There is valid reason to do this, to not lazy evaluate the set.
Because then you get into these situations like this, where you modified the original attributes, after you pass it, and, like, that's…
I mean… Technically, I guess?
**Robert Pająk** 27:31 That was my reason why I proved it, because I thought that it's a safer code anyway. I just… yeah.
As a principle.
**Tyler Yahn** 27:40 I… but I… but the current tests that are included here are not appropriate. Like, testing that it's a concurrent safe across go routines, like, this test, I think, can get added. The other ones, like.
I'm standing by that position that, like, we don't provide concurrency guarantees around that option. So, yeah.
Like, as any other thing, like, it needs to be documented as such, otherwise, like, you can't assume it. …
So, yeah, that's kind of where I stand on that one.
So, yeah, I moved it to the next, … It works for me.
**Robert Pająk** 28:13 Thanks for explaining.
**Tyler Yahn** 28:17 …
Yeah, so the only thing that's left is this last PR to, synchronize, with hotel dependencies, essentially, and upgrade the semantic conventions here. So, …
But this is… The only thing… so, upgrading to the 137 semantic conventions is…
pretty straightforward. It's synchronizing the repository.
The only thing that I don't 100% know on is, …
the, config setup. So, here we have these…
… wow, this is gonna take a long time, isn't it? Anyways, so, like, we've just released deprecations for this, like, …
with counter suffix and with, without unit, I think, are the two options from the Prometheus exporter package. The config still uses these.
So, I don't know what we want to do there.
**Robert Pająk** 29:17 No need for now.
**Tyler Yahn** 29:19 Yeah, okay, then… then that's….
**Robert Pająk** 29:21 Actually, this is, you know, a nodel config for 02 version, etc, 0 free world is….
**Tyler Yahn** 29:28 Where we aren't going to change the config there, so this just needs to keep supporting this.
So, yeah, that's what I did. I added a null in. So if that's… if that's… yeah, if that's fine with everybody, this should be pretty straightforward to review. Yeah.
And after this, I think that's it.
For the milestone.
Okay, that's enough of that.
… We can double-check on that, actually.
So yeah, maybe I'll just ask, like, is there anything that people know is active that needs to get included in this milestone that we need to wait on?
Nothing really stands out to me.
Here, at least. … Maybe you can take a look at contribib.
Ideally.
This gets upgraded as well, but we can work on that.
Yeah, I don't see anything… Here, either. That is, …
within the last release that we were really trying to prioritize. So, okay, then let's… let's keep moving on that one. I'll wait for this Contrib repository, PR to merge, and then I'll start the release process in OTEL, or…
Yeah, at least I'll get that together to start the release process, and OTEL at least, and we'll start… we'll start making this happen.
Okay.
Next up on the agenda, Robert, you want to talk about this proto-all drop attribute value restrictions?
**Robert Pająk** 31:48 Basically, just look for approvals for…
making, you know, it sooner to happen, and it's just that. So basically, it's the thing about, … so right now, we are still… it's still blocked, but some people of the TC already agreed that it's kind of approved. It's even approved by Tigrant, you just block it, just to not accidentally merge it.
It's basically removing from the proto all this kind of information that
I added also some additional clarifying comments, which other people liked. Oh, I removed these constraints, that attributes values cannot contain, you know, this kind of types. The idea is that the receivers
who read and take care may start preparing their receivers to accept these values. Even before the API and SDKs send it, the collector already can handle it anyway. This is what collector is doing already right now, so it's more about, you know, kind of
Making sure transparent communication and making things more explicit.
**Tyler Yahn** 32:57 Yeah, I'd probably, ….
**Robert Pająk** 33:00 Change the name.
**Tyler Yahn** 33:00 got a little clearerier, like, ….
**Robert Pająk** 33:03 If you have any suggestions, yeah, I've opened that.
**Tyler Yahn** 33:05 Like, what you did in the specification is probably similar, I would do that there. Like, put a little, emoji or something like that, and then say, like, you know, important….
**Robert Pająk** 33:14 important.
**Tyler Yahn** 33:16 Yeah.
**Robert Pająk** 33:16 But do you think I should also explain things more here, or not really?
**Tyler Yahn** 33:21 Yeah, so, I mean, I think that, like, I would say, I would say, like, important consumers of this proto…
should expect values that were not coming before, to some effect. Like, saying that, like, the consumers of this proto, like, that were, like, basing all of their decisions and basing their code off the fact that these sort of things will never receive particular value types.
They need to update, because that's no longer a guarantee that they can rely on.
**Robert Pająk** 33:49 Do you want to put it as comments, just for transparency?
**Tyler Yahn** 33:54 Yeah, you haven't heard me fumbling around my words here. I can try, yeah.
**Robert Pająk** 33:58 Yeah. I will understand, and you know, I just, you know, if people just add comments and not blindly approve, it's also, you know, people see that people are taking care during, you know, reviewing process.
**Tyler Yahn** 34:11 No, I mean, I think it's fine, I think this is… this is good, I just…
Because, like, these, I think, get turned directly into release notes.
**Robert Pająk** 34:17 You are right. The main idea is about, you know, passing the information, so you're, you know, making sure that… so your comment is perfect, you know.
**Tyler Yahn** 34:26 Yeah, okay.
And then the 1.8 thing, is that because this specification, the 1.8 specification, is the one that dropped that restriction?
**Robert Pająk** 34:36 18 will add it, as you see in line number 9, so we first need to add these restrictions, and then drop it. So we are waiting for the one…
180 release, so that.
**Tyler Yahn** 34:48 Oh.
**Robert Pająk** 34:49 restrictions are there?
**Tyler Yahn** 34:51 Oh.
**Robert Pająk** 34:51 You have this communication, you like, step by step.
**Tyler Yahn** 34:55 Oh, huh.
I see. That's interesting.
**Robert Pająk** 35:02 Yeah.
**Tyler Yahn** 35:04 …
Yeah, I might recommend also changing that this is going to, like, giving a warning it's gonna change as well in this initial… in this release as well, but….
**Robert Pająk** 35:14 I'll be working on creating changelog for 180 tomorrow, so I'm also trying to capture this and add this.
And you can also add, you know, this kind of comments for the changelog creation, for the changelog PR.
**Tyler Yahn** 35:31 Yeah, yeah, okay.
Or that seems fair.
Okay.
Okay, looking back at the agenda, it looks like we're at the end of that. I'm gonna stop sharing my screen here.
Oh, sorry, I'm just seeing your chat at this point, assuming I don't play well when we're sharing. Okay, any other topics people want to talk about? Any other projects you're working on? Any other…
Hotel-related things you've seen?
Are folks planning to make it to KubeCon North America?
I see a note from Brian.
Not from Sam.
**Bryan Boreham** 36:23 And not in this economy.
**Sam Xie** 36:27 So, probably in China at that time.
**Tyler Yahn** 36:30 We gotta get you to go to the KubeCon, APAC, or, maybe… I think there is a Chinese one, right?
**Sam Xie** 36:41 I don't know.
**Tyler Yahn** 36:42 I think Steve might have… anyways, like, yeah, I think there might be one, …
I definitely know there's one over in Asia somewhere. But, …
Yeah, okay. I guess anybody who's listening to the recording, if you haven't, you should try to get into the Maintainer Summit as well, if you're gonna go, but, …
Yeah, I'd love to see you all there.
**Bryan Boreham** 37:02 Can I ask a bit of a… A possibly stupid question, … If you're…
as a Go program, producing a lot of metrics, …
And you feel that you might like to batch them up on the upward path.
I found a couple of things in the collector codebase that will batch.
But… yeah, so I guess my question is, is that a thing?
that the basic Go SDK will do, or if not.
Why am I asking the wrong question?
**Tyler Yahn** 37:42 …
So, no, probably not. Like, there's obviously, like, aggregation, like, it's gonna do that, and you can use views to combine things, but, like, outside of that functionality, like, the collector is kind of the de facto hotel standard of how to do advanced.
Filtering advanced, like, batching and that kind of thing, for the metric signal is kind of, like, where everyone is going to point you to, to try to do that kind of processing.
I think there's, … there was an ask to also do additional filtering, which is maybe some additional features that would be added to the view itself, but outside of that, like, in the exporter.
The ones that we provide, at least, no. Obviously, you can… you can write your own exporter, and you can write an exporter that wraps another exporter, and so, if you wanted to do…
some advanced processing there, you're always welcome to… I mean, that extension is always open to you. But no, like, by default, that's not something added, …
offered by the OTEL SDK.
**Bryan Boreham** 38:44 Okay.
**Tyler Yahn** 38:46 I mean, I guess I'm assuming, like, you're talking about…
Reagreation across, like, different metrics, right?
**Bryan Boreham** 38:52 No, just backing.
Like, if you…
If you produce a million different metrics, then that's… just sending them all in one go is a big message.
**Tyler Yahn** 39:03 Oh, I see what you're saying, yeah.
**Bryan Boreham** 39:05 So you should, you should, …
Well, in my book, you should… Like, chop that message up.
And there's a thing called Exporter Helper.
But the point where I got confused is that, like I say, that's in the collector.
And… If you're writing an exporter and there's a thing to help you.
I sort of expected it to be in the SDK.
**Tyler Yahn** 39:33 Yeah, no, that's… that would definitely be something at the collector level. Like, if you wanted to do some additional batching, like, I think that'd be something you'd have to write your own exporter for. Obviously, you can generically do it, I think, because of our exporter definition.
So, like, you could take an exporter, wrap that with your own, like, batching processor thing, and essentially break down whatever signals you get into smaller pieces to send down the pipeline from there. But no, like, that's not something we currently provide.
**Bryan Boreham** 40:00 So write… write your own batching, is… is what you're saying?
**Tyler Yahn** 40:04 To break… to break up message payloads like that, yeah. Like, we're currently, like, the Go SDK, we… I mean, we rely on, like, the transport protocol to handle that. Like, if you wanted to do, like, batching, we're expecting, like.
whatever that messaging protocol to do, like, frame batching or something like that. But on, like, the receiver side, I get what you're saying, like, if you're… if you're told, like, hey, wait, there's a… there's a, you know, a gRPC connection that's gonna stream you over, 10,000 records and they're all gonna come at once, like, maybe you're gonna try to keep that all in memory at the same time, so that's not really ideal.
And so, if that's gonna be the case, then yeah, like, you should be able to write your own export to handle splitting up of a payload any way you want.
Like, for….
**Bryan Boreham** 40:42 matching in chat. I mean, it was a… it was a thing that was in Slack, …
That… that issue, the Knative issue.
…
… yeah, so I don't know if that helps. That's the context, that they, … they found themselves sending 5MB messages, and the thing they were trying to send the messages to said, I will not accept more than 4MB.
**Tyler Yahn** 41:15 Yeah, yeah. I mean, I, like, again, like, from the Go perspective, we're pretty agnostic here. Like, how you want to solve that. Like, if you want to change your client configuration to handle this differently, if you want to change the server configuration to handle this differently, like.
I think… I think there's a lot of different solutions that you can do there. I think one of them is exactly what you're saying. You could also wrap your exporters in an exporter that, you know, ensures a payload size… well…
That gets hard. PaloSide's actually really hard from a…
perspective of, encoding, because, like, you actually don't know the payload size as you're looking at the resource metrics that you're trying to export. You only know the payload size once it's been encoded into a gRPC message, so that's, like…
It's a little bit harder there. So, like, again, like, that's why, I think, why we don't do those sort of things. Like, I think that you could, and I think, like, there's space for providing something like that.
There's… I mean, like, this is one of those things where, like, if you do come up with a solution.
You can probably make it very generic so that it can work for most exporters.
It, …
It is going to be hard to try to predict what the payload size is gonna be, but, like, let's just assume that, like, you don't really care, like, you just say, like, max out on…
you know, 50 metrics or something like that, and then you could split up a message, resource message to the exporter there. Like, you could provide that, and if you do, I would recommend, …
you know, registering it with the hotel registry as an extension. That's definitely something that, like, as a community member, you could always provide. I think, like, seeing if there's utility from there.
**Bryan Boreham** 42:49 Okay.
Yes, sir.
**Tyler Yahn** 42:51 No, I don't think you're… I don't think it's a stupid question. Like, like you said, like, there's an issue there. I definitely don't think that there's, like, it's not something that we're gonna tackle, I think, as a goal here, specifically because the collector does offer these sort of things.
….
**Bryan Boreham** 43:05 collector as a separate process, right? So in this particular context, you have to get yourself a collector that's configured to accept
6MB messages.
and then configure it to batch them down into smaller ones and send them on. That's a self-contained solution that I understand.
**Tyler Yahn** 43:26 Right.
**Bryan Boreham** 43:27 And so there… there is… Nothing to look for in…
like, go code without adding a second process. That's… as far as you know, that's not a thing that exists.
And the thing that's…
The thing that I had found that I thought was a goal library is… is not something that you would use in your goal program. That's the exporter helper.
**Tyler Yahn** 43:53 …
So, I, yeah, it's not designed that way, like, there's definitely not been, like, testing and that kind of thing, but, …
I do know that, like.
I've wrote extensions to collector exporters to be able to use collector exporters as OpenTelemetry Go SDK exporters. So, like, there are ways to, like, provide a compatibility layer around those things and just a shim.
It's been a long time since I looked at that, so I don't… I don't know the state of it. I don't… I definitely don't know, like, an export helper. I don't… I definitely don't think there's a translation layer for that, but I… I could, like, that exists, but I think that it could. Like, I think you could maybe take that existing code.
Try to wrap it, into something that, you know, could serve what we were just talking about, like some sort of export, wrapper.
But I think, like, I'd have to look way more into the details there, to try to find it. But yeah, I think that's a great, like, side project, like I was saying, like, and if you do something like that, like, registering it with the hotel registry is a great idea, and, and advertising that it exists.
**Bryan Boreham** 44:59 Okay, thanks very much.
**Tyler Yahn** 45:00 Yeah, yeah, thanks for the question.
Cool. Anything else y'all want to talk about?
If not, we could probably end it early. Thanks, everyone, for joining, good seeing you all again.
And, happy to have y'all back. Looking forward to keeping the momentum going as we get towards the end of the year. So, yeah, lots to do.
Alright everyone, I'll talk to you in a week's time.
