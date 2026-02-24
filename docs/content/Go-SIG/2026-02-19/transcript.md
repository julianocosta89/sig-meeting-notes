SIG: Go SIG
Date: 2026-02-19
Duration: 58 minutes
============================================================

## Zoom Recording Transcript

**Tyler** 00:14 Okay.
**Damien Mathieu** 00:17 Hey.
**Tyler** 00:19 Hey.
**Damien Mathieu** 00:20 Did you get anything specific, or was… did it just happen?
**Tyler** 00:24 I think it just happened.
I'm gonna… I pinged Trask, he looks like he might have…
Okay, hmm, yeah, alright, well…
**Pellared** 00:40 Do you have problems with joining this meeting?
Or not.
**Tyler** 00:43 Yeah.
**Pellared** 00:44 Okay.
**Tyler** 00:57 I'm just thanking Trask for doing, some sort of magical thing that… he probably didn't do anything, but…
Okay.
Yeah, we were having issues, so…
That used to be the case when, like, we ran out of licenses, so I'm not exactly sure why…
It happened now, but… Anyways, Moving on. How's everybody doing?
Quiet bunch today.
Nice.
Damien, are you doing some renovations over there?
**Damien Mathieu** 01:40 In a way, this room is going to become,
my first kid's bedroom, and I will be moving to the other side of this wall, which is a guest room.
**Tyler** 01:55 Oh, okay.
Yeah, that's exciting.
You gonna bring the posters with you, or are you gonna leave those for your kids?
**Damien Mathieu** 02:03 Oh, no, I'm bringing in Ben with me.
**Tyler** 02:08 Come on, I'm guessing that means you're just gonna have to read Lord of the Rings to him, right?
**Damien Mathieu** 02:13 Later.
**Tyler** 02:18 Yeah, fair enough. Well, cool. Yeah, let's, let's jump in here.
If you haven't yet, go ahead and add your name to the attendees list, looks like somebody already added me, and if you have things you want to talk about, please go ahead and add them here.
I wanted to start off by talking about the next release. One of the things… there's, I think, two major things about the release I wanted to talk about. I think Sam's posted the thing, one of them.
The other one is the…
sunsetting of our support for Go.
124 is helpful. A lot of things are updating, we're not gonna be able to get a lot of updates because they only support Go 125 or above, so the sooner we get the release out, the sooner we can bump it ourselves. We're already deprecating the 124 support in this next release, so we can drop it, after that's been done.
So that'll help with our dependencies. The other thing is this, security issue that Sam's been working on is kind of, I think the other one that I'd like to get
out, and approved.
It looks like there's some feedback that's been provided to this, Sam, so maybe you can give me an update on, like, where we're at on this?
**Sam Xie** 03:30 I just updated PI yesterday based on the comment, so now the baggage.new message can also return partial results.
**Tyler** 03:42 Okay.
**Sam Xie** 03:43 But I'm still fine-tune some, kind of, the limit, because some part of the implementation use
kind of map to filter out the value, but that is not in order, so I need to address that.
**Tyler** 04:05 So, the order doesn't actually matter, right? Because there… we can come up with our own algorithm, for however we wanted to do that. Is it more just a consistency thing, is what you're saying? And we wanted.
**Sam Xie** 04:15 But yeah, because I saw we want to keep the first N items, and if it has a map, then it's a random item.
**Tyler** 04:24 Yeah.
Is there… I mean, there's a… there's not a problem with doing that either, though. We could just do a random thing, right?
**Sam Xie** 04:34 So, that… That that's okay.
**Tyler** 04:38 Yeah, I mean, yeah, right? Like, there,
My reading of this was, like,
It's kind of an implementer or platform made to find, no, sorry, yeah.
may drop list members, until both conditions are met. The selection of which list member is dropped and the order, is unspecified and left to the implementer, right?
Yeah, I mean, I think we probably want to be…
**Sam Xie** 05:08 consistent, I would guess? So, if we do one algorithm one place, we probably want to do it the other place, but, like…
**Tyler** 05:15 If you're trying to retrofit, like, our structure on how we're, like.
parsing things just to… just to conform with this, like, first N, like, I would say… Don't bother,
just… I mean, like, doing a random drop is also a valid implementation here, right?
**Sam Xie** 05:33 Yeah, just the result is not that easy to predict.
**Tyler** 05:37 Oh, for, like, testing, you're saying?
**Sam Xie** 05:40 That's one part, and I think for the multiple baggage header, we do… implement the first and item.
And… Yeah, that's kind of inconsistent.
**Tyler** 05:54 Okay.
So, do the translation between a map and some sort of slice, is that gonna be…
In a hot path somewhere, where it's gonna cause performance overhead.
**Sam Xie** 06:10 Yeah, I think so. It will cause some problems, right?
**Tyler** 06:13 Where… so where's it at?
**Sam Xie** 06:15 Oh, I haven't, I haven't pushed it, I just…
Because that's what's the co-pilot's feedback, and I think, oh, that kind of makes sense.
Just starting to implement it.
**Tyler** 06:27 Yeah, I saw, maybe we can take a look at the comment.
So not this one…
**Sam Xie** 06:36 Mmm…
Yeah, I think that's one of them.
**Tyler** 06:56 Yeah, I… Don't know if I'd…
Spend too much time on this.
I'm happy to hear other people's opinion.
But this non-deterministic nature is, like.
the whole point, I think, of why the baggage spec wrote it this way, because, like, you're in an error state, and, like, you already are overloading, like, limits in a baggage, like…
This is just… this is just the world.
In that error state, that it may be non-deterministic.
Yeah, I don't… I think I… I mean, the thing is also, like, if you,
I would ignore this, and maybe create an issue for it, personally, if you wanted to track this. I would also maybe just not create an issue and wait for a user to say, like, I need something deterministically, and here's why.
But, I mean, like, in compliance with the baggage spec, like, there's nothing, like.
from my reading of the baggage spec, it says we can't do exactly what you're doing and what it says that we shouldn't be doing here, like, that's… I think that's… that's a hundred… like, I think this is…
I think a great programming thing, but, like, not a compliance thing with the baggage spec.
**Sam Xie** 08:14 Yeah.
**Tyler** 08:15 Yeah. So I don't know if I'd waste too many cycles in this PR to try to address that. If you feel it's needed, maybe we could look at it in a subsequent PR, but I think maybe just scoping what you're working on here to
to hitting the limit, not necessarily the implementation of that, is probably what I would recommend.
**Sam Xie** 08:35 Okay.
**Tyler** 08:36 Any other ones on this one?
From the co-pilot, review.
**Sam Xie** 08:43 Mmm… No, the previous stone, I think that's the major one.
**Tyler** 08:49 Okay.
Hmm.
Yeah, I don't… that's interesting. Yeah, I haven't read a lot of these feedback. So, are you still…
Could you go through here, and the ones that you have resolved, can you resolve the comments? And so then, sure. Okay, yeah, because I'm happy to give this another review. You've been doing great, on this, so yeah, I'd love to take a look at this. Where did we land on this issue here?
With the partial package and then the error handling?
It looks like you created an error handler package.
**Sam Xie** 09:39 Yeah, I moved the arrow handle package to another internal task, so… decay.
It could be used for propagation.
Hmm.
**Tyler** 09:57 Yeah… okay.
So… Hmm.
I think this might be more problematic than…
The error handler at the hotel level can be set.
Can this error handler be set? And is it set to the same one that the OpenTelemetry.
**Sam Xie** 10:18 It says to us the same way.
**Tyler** 10:21 How does that work?
**Sam Xie** 10:23 So I basically moved the implementation to the error handler package, but leave a reference to the global, so that if you check the global handler…
**Tyler** 10:34 Yeah, this isn't internal to the baggage, it's.
**Sam Xie** 10:36 Yeah.
**Tyler** 10:36 The top level… oh, okay, I'm sorry, I missed that. Oh, okay, I see.
**Sam Xie** 10:39 I didn't change the API.
**Tyler** 10:41 Okay, okay, okay. Alright, that… yeah, sorry, I missed that. That makes a lot more sense. Okay, cool, yeah, I can take another look at this. This makes, I think.
a lot of… Great, change then.
Okay, but yeah, this is another one that we need to get out in this next release, so this is blocking the release, so,
This is good. Any other comments from other, folks on the call about this PR?
Okay, well, yes, Sam, we'll wait for updates, or resolutions of those comments, and then I'm happy to take another review of this, and we'll try to, yeah, get this one moving.
Okay, going back to the milestone on here, I don't think there's actually anything else, blocking this…
the SDK observability, we, you know, are chipping away at, including these.
this exporter Prometheus migrate to the new configuration option, I think is… actually, I don't know where we're at on this one. I think this one was just, like, waiting for cleanup on this? I guess I did.
**David Ashpole (dashpole)** 11:50 Do we have, like, a feature gate or something, Andrew? Let me remember.
**Tyler** 11:54 Yeah, I'm trying to.
**David Ashpole (dashpole)** 12:02 This is,
This is a spec question, so that there's still the previous options, without countersuffexes and without units.
**Tyler** 12:11 Right. That are kind of, like…
**David Ashpole (dashpole)** 12:14 Cross, like, the…
They kind of make a little bit less sense now that we have the new translation options, but they're also more granular.
So, we would be removing functionality by removing them, so we'll have to decide that at the spec level.
**Tyler** 12:34 Ugh.
**David Ashpole (dashpole)** 12:35 I'm also okay to include this, and then, like, we can open a new one to track removal, if and when it gets removed from the spec. So, I don't know if that's more helpful, so it doesn't just sit open.
**Tyler** 12:44 Yeah, I think maybe that's… that's what I was thinking. What are other people's thoughts on this?
Yeah, do we have an issue in the spec that's tracking that work?
Guessing this, right?
Or is this… no, this is just a… Yeah, section of the spec.
Yeah, I mean, I think if we have something tracking it in the spec level, then we can close it in favor of that, but otherwise, maybe keep it until we have something tracking? Does that make sense, David?
**David Ashpole (dashpole)** 13:16 Yeah, that sounds good.
**Tyler** 13:18 Okay.
I'm gonna move it out of this milestone, though, because it's… definitely don't think it's something we're gonna resolve,
Before we give this release.
Next up is support the new W3C random flag. I think there's some work being done on this.
Yeah.
Ted, one review from David.
**Pellared** 13:55 Here are some questions, I think, at the end.
**David Ashpole (dashpole)** 13:59 Yeah, I felt like they were misinterpreting the spec. I'm not, like, super familiar with it, but they were… they were just passing along all trace flags
opaque. So if someone sets, like, the third flag, which is yet to be defined, then this changes the behavior. We used to zero those out, and now it changes the behavior to pass it through.
And I don't think that's correct. The current spec says that we must set Other flags to zero.
Or, it says vendors must set the flags to zero. I don't know if we qualify as a vendor.
I'm assuming that they mean basically anyone who handles it.
**Tyler** 14:42 Yeah, that's what I would guess, too, yeah.
Yeah, I mean, that sounds right to me. Okay.
**David Ashpole (dashpole)** 14:51 So, I…
**Tyler** 14:51 We just need…
**David Ashpole (dashpole)** 14:52 They were blocked on that. And then, otherwise, it looked fine, I think.
I haven't, like…
been super detailed, I just was confused as to why we were removing a bunch of stuff.
**Tyler** 15:04 Yeah, that makes sense.
Okay, I will… looks like you commented yesterday, so we can wait on this. We're not in an immediate rush to get the release out, we have those other PRs.
So I'll add this there, but I don't think this is blocking the, the release, so…
I think we'll just keep that… keep that there to track it.
Another self-observability… yeah, this is, I think, the other one I was wanting to ask about. Not necessarily just this PR, but more, I guess, this…
issue here. This is the thing about the concurrency guarantees that we provide for our API, well, not the guarantees we provide, but the API, but the implementation restrictions that we have with our API.
And I think, this is something we want to try to get out in this next release, is update our documentation around, like, what we expect from the, implementations, right? Like, we have it in the logs API, but, like, just copy that to the other ones, right?
**David Ashpole (dashpole)** 16:02 Yep.
Sorry, I said I was gonna do it, and I didn't. You can assign me if you want. I just fell behind on other stuff.
**Tyler** 16:09 Oh, that's fine, I don't… Yeah, I'll assign you, but the other thing, David, I haven't been…
paying attention to the trace API one in the specification, there was a conversation there.
that I'm behind on that. Are we able to move forward with that?
**David Ashpole (dashpole)** 16:26 So I think it's fine for us to move forward with the documentation on the tracer provider, tracer, and span.
**Tyler** 16:33 Yeah, I agree. I think there's…
**David Ashpole (dashpole)** 16:36 I… I don't like the current language for Link, because…
In theory, the current language would say we are supposed to document link as being concurrent safe when anyone who looks at the struct can clearly tell that it's not.
So, that would be… I think we would be forced to kind of ignore the spec until 2.0, if that was the language that they settled on.
**Tyler** 17:01 Oh, man. Okay, well that's… yeah, we definitely can't do it.
**David Ashpole (dashpole)** 17:04 I'm hoping, actually, You can read my latest comment. I think…
We actually should have made a concurrent safe link.
Or, like, an immutable one, basically.
**Tyler** 17:19 Yeah. Similar to what we did in the logs API, like, that was probably a mistake on our part.
**David Ashpole (dashpole)** 17:24 And so, I'm… I'm actually okay with the language being that link must be concur… immutable and concurrent safe.
I don't think that's, like, a change from what was there before. I… and I… we just won't be. But I don't, like… it would be silly if it was document… if it was, like… I think the, like…
Documentation only really applies to interfaces, and link is not.
link and event are not interfaces, so I think that'll get cleaned up. But I think for Tracer, provider, Tracer, and span.
We can just continue with documentation, we'll be fine.
I don't think anyone who reads the link struct either is, like, super confused about whether it's concurrency. So, we will not be compliant with that part of the spec, but I think it's okay and not worth a 2.0. That's my take.
**Tyler** 18:13 Are there methods on the link type?
**David Ashpole (dashpole)** 18:15 No.
But, like… I… I interpret…
Must be immutable and concurrent safe, as meaning that you should not allow direct access to the fields.
Like, clearly this isn't immutable, right?
But…
they… we could write it such that the fields were internal, and you could only set them with a new function, right? But that's not how we did it, and we're not changing it.
Right.
So…
**Tyler** 18:44 But the thing is, is I don't think we ever have any plans of releasing a 2.0 API.
**David Ashpole (dashpole)** 18:48 I mean, if… I would say…
this doesn't warrant a 2.0 API. If something else did, for whatever reason, then I would encourage us to make this change as well.
But I also agree that that probably is not gonna happen.
I don't know if that makes sense.
**Tyler** 19:05 Yeah, I hear you. But my concern is that, like, if we're writing specification retroactively to try to fix this there, but our implementation is literally the opposite of that, like…
We would, like.
**David Ashpole (dashpole)** 19:18 I know.
**Tyler** 19:19 That doesn't make any sense, because, like, then we're not compliant with the specification. We are compliant today. That defines a break and change in the specification, right?
**David Ashpole (dashpole)** 19:26 I think you can make… so…
I agree that currently it doesn't use normative language, and that that means that technically there is no requirement for it to be that way.
But, like, I think a reasonable reader of the spec would say that we probably should have made it immutable, right? And, like, I also don't think it's the end of the world for us to be non-compliant with this. It's clearly usable today.
Our users don't want that.
**Pellared** 19:54 So that's my take. I also think that it is pretty common in Go that if a struct has a slice, then people know that they need
you know, Usually, you do not alter it, etc. You should take care when you have maps and slices.
I don't think he's endometry.
**David Ashpole (dashpole)** 20:12 a slice. It's like, span context isn't immutable here, either.
**Pellared** 20:15 I see. Yeah.
**David Ashpole (dashpole)** 20:17 The fields are just there, yeah.
**Pellared** 20:19 Yep.
**David Ashpole (dashpole)** 20:22 Yeah, the slice is a different story, because then, in theory, we'd have to copy it, which also would stink.
Yes.
**Tyler** 20:32 Yeah, I'm not…
in favor of that spec change for the link. That's definitely something I had to get back to then. I'm in favor of blocking that change, if that's going to be the case.
**David Ashpole (dashpole)** 20:41 You can… you can read my comment.
Okay. And then maybe you and Riley can work it out.
**Tyler** 20:48 Yeah, I'm happy to take another look then. I do think that, like, all of the different methods and things where we can provide that, I think that makes a lot of sense, but…
Yeah, like, I can't…
Yeah. The specification can't come along and make a braking change and then expect everybody to…
Be okay with that without, like, Pre- before going at Lucas.
**David Ashpole (dashpole)** 21:10 I, I think… I think there's disagreement within the community as to whether it's a breaking change to, like.
whether this is a language cleanup, or whether this is a breaking change. So I… yeah.
Anyways, either way, it's not gonna change what we do in our code, so… I don't think it…
**Tyler** 21:30 Yeah, I'm just concerned, though, because, like, it's one of those things where…
we don't… we have this in our code, we come along, and the specification changes, now we're not compliant, and we have a user come to us and say, like, look, I'm using this as its concurrent safe, because it's literally defined that way.
in the specification. You're not compliant with the specification, you need to be compliant.
So, then…
like, is it also a bug that we need to break our API guarantees at this point? And, like, we're gonna have a backwards incompatible change in our API to support this?
**David Ashpole (dashpole)** 22:03 I… I wouldn't… I would say that, like.
Like, we can open an issue and add it to the, like.
2.0 milestone, and then let the 2.0 milestone sit. I don't know.
**Tyler** 22:14 Yeah, but you see how, like, that… that…
**David Ashpole (dashpole)** 22:16 I understand.
**Tyler** 22:17 That incorrect logic propagates into the actual, like, user experience here, is the problem, right? Like, if people want to, like, I don't know, somehow blind themselves to the fact that, like, they're making breaking changes to the specification.
and then force that upon implementations, it seems to, like, that same illogical step has to follow in the implementations, like…
it's not… like, changing this link to a concurrent saved model that you just described is not a breaking change anymore, because it should never have been that way, right? But, like, it is, because that's literally how we define breaking changes.
So, like…
Like, you're left with a contradiction here, and, like, the contradiction starts because, like, the premise was actually illogical, like, it should not have been omitted to the specifications, the problem.
**David Ashpole (dashpole)** 23:04 I think even today, someone, if they were really
You know, paying attention could come along and point out the language that exists today that says, you know, needs to be concurrent safe and open an issue.
And, like, Like, yes, it's the public language, but that… I don't think that would… But other parts…
**Pellared** 23:24 In the main README of the specification, it says that only things are normative which follow the RFC.
**David Ashpole (dashpole)** 23:30 I understand.
**Pellared** 23:31 Yeah. I…
**David Ashpole (dashpole)** 23:33 And, like, but, like, that's exactly the point.
**Tyler** 23:35 And, like, you've been involved in the SIG long enough to know that, like, when we do audit compliances of what we release, we literally look at these things and go, like, too bad, it's not normative, and we make the distinction on that. Like, we have literally made this distinction that, like, yeah, it says it should do this.
That's not normative language, we're not gonna follow it, we're gonna go ahead and do whatever we need to do here.
like, we've made choices in our API design and our specification, or our SDK design.
On the fact the specification does not have normative language.
And to come back and then literally change that, because they rewrote it wrong?
like, I get that, like, there's a desire to say, like, at the specification level, like.
We made a mistake, but you can't fix a mistake by saying, like.
well, now we're gonna just impose additional restriction. That's… that's not…
That's not how you fix a mistake.
Like, if you… you build a building and your foundation is… is, like.
in the wrong angle. You can't come by and just say, like, well.
alright, now we're just gonna fix the angle of this foundation here, and the whole building crumbles underneath it, right? Like, I mean, like…
That doesn't… that's just, like, doesn't… that's not how that works.
**David Ashpole (dashpole)** 24:44 Yeah, I understand. I… I just… I don't think…
like, for better or worse, I don't think that's how a lot of other spec approvers… Types.
Read the spec.
**Tyler** 25:00 Yeah, and I think that that's what got us into this problem, is that, like, we have a lot of authors that don't understand how to write specification, and they don't understand the requirements and, like, the actual standards that are defined in the specification.
And so they wrote the specification in this lax way. And that's… I mean, I get that. I understand that. I understand the reality of it.
The problem that I have, though, is that, like, you can't have those people then come through and say, like.
Because they made this mistake, and because they had a misunderstanding.
That they're going to fix the problem by imposing additional restrictions on people that did understand this.
Like, that's… That's the illogical part.
**David Ashpole (dashpole)** 25:35 Don't even…
**Tyler** 25:38 I mean, I can say the same thing here with our API, right? I can say, well.
I'm not a really good Go developer, and I didn't realize that people can actually mutate these fields the way they are. I didn't want them to. So, it's not an API-breaking change because I never wanted them to do this, so I'm just going to change this now, even though I have compile guarantees, and this is gonna break that compile guarantee, I'm just gonna change it because I didn't actually want that.
like… Like, that…
I mean, yeah, like, in theory, that could fly, because I didn't know what I was doing, and therefore I need to get a pass on it, but, like, that's not how the world works.
**David Ashpole (dashpole)** 26:14 I guess here…
Do you think all of these language cleanups that we're doing are breaking, or just this link one?
**Pellared** 26:23 I think the ones… I think the ones that other languages implement differently.
**David Ashpole (dashpole)** 26:30 I see, so it's like, we can add muscle.
**Pellared** 26:32 make it all, D.
We do an audit, and we make sure that it doesn't break any, you know, implementation. I think…
it's fine to add this, you know, clean up. But if we know that for some reason, some languages implement differently, you know, there may be other languages which went this way.
**David Ashpole (dashpole)** 26:51 Okay. Maybe then our request is to leave the language non-normative?
**Tyler** 26:58 Yeah, that sounds fine.
**David Ashpole (dashpole)** 27:00 Okay, we can ask.
**Tyler** 27:03 Yeah, yeah, that makes sense. I mean, to your point around, like, all of this additional restriction that we have to have documentation that we're adding, I agree, like, that is not backwards compatible, but I don't think it's, like, in the sense that, like, we can't fix it is the problem.
**David Ashpole (dashpole)** 27:16 Right, like, we can always add documentation. That's not something we have a problem with, and that's something that, like.
**Tyler** 27:20 we have defined in our version compatibility guidelines at the specification level, saying that, like, yeah, there may be, like, technically backwards incompatible things, but, like, here's the subset of things that you should be able to support, like adding methods, right? Like, that's always been a problem for us, and, like, we've…
talked ad nauseam about that one, but, like, yeah, but, like, so… the…
Yeah, I could definitely see the argument saying that, like, this is not a backwards compatible thing by just saying we have to add additional documentation, but, like, I can see that as, like, a reasonable one. I think when you have breaking changes that are in direct
conflict for the existing implementations, like Robert said. Like, that's… that's where…
**David Ashpole (dashpole)** 27:57 Or would they have to make a big change, yeah.
**Tyler** 28:00 Yeah, yeah, yeah.
**David Ashpole (dashpole)** 28:03 Let's continue the discussion on the spec issue, but I think for our purposes, we should go ahead with language.
In the tracer, tracer provider span interfaces.
And just ignore event and link for now.
I think regardless, our event and link are not going to change.
So, I… yeah.
**Tyler** 28:25 Yeah.
Yeah. I mean, and like, I…
like, this is something that's gonna have to get raised to the TC if it does. Because, like, this is… like, we literally are a very cautious SIG for these exact situations. We do not want to end up in a place where we're out of compliance.
Like, in our implementation, and like, this is…
it's putting us in a place where we're out of compliance. Like, we spend a lot of time and effort to try to get here, and to…
So…
**David Ashpole (dashpole)** 28:52 I think it's, like, maybe also a reasonable question to ask, but if…
It feels like there's often small things.
where SDKs are out of compliance or something, they just accept it.
And, like, culturally, we seem okay with that, where, like.
small bits of APIs or SDKs get missed, and we don't make people do…
you know, major version revs for it, so I… like, I assumed that that was what would happen, is that nobody would actually go
and force us to do a 2.0, and that they would be okay with us just being out of compliance. Maybe documenting it, or something, but…
Like, it… yeah, obviously, if… if it forced… if this language change forced us to do a 2.0 in our trace API, I think that would be a non-starter.
From my perspective.
**Tyler** 29:46 Yeah, I guess there's…
**David Ashpole (dashpole)** 29:51 I think there's something to be said about what people's.
**Tyler** 29:53 take the responsibility as maintainers to be. Like, I don't… I don't take the role lightly. Like, when I assumed the role, like, I took that idea that I have a responsibility to make a compliant implementation of OpenTelemetry very seriously, and I've, like, upheld that for years at this point.
And I don't, I don't plan to not have that upheld.
At this point. And, like, I get that other SIGs and other maintainers may not take that as seriously, and I think that that's…
something I have opinions about, but, like, I don't think that, like.
If you are in an organization that defines a specification that is saying this is the gold standard of what you need to do and what you need to not do, and then you say, like, well, that's okay as long as there's an asterisk in some places, in some places you're not allowed to, like, you don't have to actually follow this.
like…
that was… that was improper to restrict me to start that way. Like, I should have just been able to say, like, I can do whatever I want, and then I'll just come back after the fact and retroactively tell the spec what I did and what I didn't do. Because, like, we would have designed the Go API completely differently.
**David Ashpole (dashpole)** 30:54 I agree. I mean, all I'm saying is, like, I think there's some room for human error.
And, like.
**Tyler** 31:01 Yeah, but there's a difference between human error and intentional error, right?
**David Ashpole (dashpole)** 31:05 Yeah, of course. I'd…
**Tyler** 31:07 Yeah.
I mean, I get that people make mistakes, but, like, when people…
like, woefully and knowingly do not add a metrics API, or, do not add a trace API to their implementation.
or knowingly change the specification in a way that will conflict with what implementations are already doing. Like, that's not human error. Like, that's… that's just…
**David Ashpole (dashpole)** 31:29 Yeah, I don't.
**Tyler** 31:29 Knowing error.
**David Ashpole (dashpole)** 31:33 I, I agree.
**Tyler** 31:35 Yeah.
Yeah, it sounds like we're…
**David Ashpole (dashpole)** 31:38 Violently agreeing with each other, so… so…
Let's keep going, we have 25 more minutes. Sorry.
**Tyler** 31:44 Ranting at this point.
**David Ashpole (dashpole)** 31:46 Do we have anything else on the agenda?
**Tyler** 31:48 So we still wanted… I still wanted to just go through, finish this up. I don't think there's anything else here, in this
milestone?
In the contribute milestone, there's, I think, minor things,
I don't know if anybody else has opinions of whether these need to go into the next release, or if there's other things that are missing here.
**David Ashpole (dashpole)** 32:16 I thought the labeler we had some issues with.
**Pellared** 32:18 Zoom?
Can you hear me, or not really? Because I'm sure.
**David Ashpole (dashpole)** 32:23 Yeah, sorry, I think I talked over you, I'm sorry.
**Pellared** 32:25 Okay, it's fine.
**Tyler** 32:30 Robert, you've blocked this, yeah, this is something I think we asked.
**Pellared** 32:33 Some books.
**Tyler** 32:35 Yeah, okay.
**Damien Mathieu** 32:37 We actually discussed fat a few weeks ago, I,
why work did not happen, maybe we should leave a comment. I think we agreed that, to fix it, we would just need to add context to… with metric attribute function.
So that the function could use the HTTP context, which would be a replacement for the labeler.
I definitely remember discussing that in a SIG meeting.
**Tyler** 33:15 Yeah, I can't remember that as well. I don't think Robert was here for that.
**Pellared** 33:18 I was not.
I would appreciate a comment, and, you know, prototype example of how it would look like.
It is not a problem.
my… but my issue is that I think the labor,
If you just add the context.
you still… I think you still do not have the access to the business stuff, you just have the context, right?
And here, with the laborer, you can have access to anything which is in the handler right now.
**Damien Mathieu** 33:55 Oh, should we pass something… In addition to the context?
**Pellared** 34:03 I think it's just a different concept that you, you know, you just have a handler, and you can use a laborer in your handler. It's just, you know, just…
it's a different… it's an inversion of control. Here you are, you have this with metric expansion attributes, and…
And you have a limited scope, but with labor, you have to scope to any logic.
I think one of the ideas was to have to, like…
If it's not a problem, if people agree, I don't know how many people are using the labeler.
We could just use it, we could, you know, just agree that we do not need this functionality at all.
But on the other side, I do not remember at this point of time
If we have a laborer, what is the…
What is the benefit of having good metrics attributes, instead of the kind of a library?
**Damien Mathieu** 35:02 On that question, it's worth noting that the person who requested the labeler agreed that it can be removed in favor of widmetric attributes.
**Pellared** 35:11 But it was only one person.
**Damien Mathieu** 35:14 Yes, but the person who requested it.
**Pellared** 35:18 Yep.
**Tyler** 35:26 So do we have a path forward here?
**Damien Mathieu** 35:33 Nope.
**Pellared** 35:37 Damien, is there anything that you can do with metric attributes that you could not do with the laborer?
**Tyler** 35:49 I thought that there was because, like, there's trace context that comes with the width metric attributes function.
**Pellared** 35:56 What is coming?
**Tyler** 35:57 So in the with… yeah, context comes with… and that includes, like, trace attribute… or trace, identifiers, like, trace ID and, spanity.
**Pellared** 36:05 Yeah, but labor interior could also access it, right? If you're in a…
**Damien Mathieu** 36:10 This labeler also has the context.
**Pellared** 36:13 Yep.
**Damien Mathieu** 36:18 Our suggestion is to keep label and remove with metric attributes.
**Pellared** 36:23 Yes, exactly, or maybe I remember also there was a comment that I think an idea that labor is basically
not a concept only for hotel HTTP, it's probably a more generic, but yes, I would rather lean towards having laborer, even if this concept will be copied in all instrumentation.
libraries, rather than getting reflected, because I think it's a more powerful mechanism.
**Damien Mathieu** 37:00 Sorry, go on.
**Tyler** 37:01 capture… no, I'm just gonna say, like, it sounds like that's a great recommendation. If Damien's on board with that, can somebody capture that in an actual
Comment here to provide guidance that we don't I have to… Guess.
Or go back into meeting notes to figure this one out in the future?
**Damien Mathieu** 37:18 Oh, the fact… works for me, I guess,
outside of… I'm pretty sure lots of people are using with metric attributes, but they're also using unstable instrumentation, so…
**Tyler** 37:32 Well, that's a good point. So, if they're using with that metric attribute function, is there a way to tell them how to migrate to using the labeler?
If there is.
**Damien Mathieu** 37:42 It can be… it can be documented.
**Tyler** 37:45 Yeah, okay.
Yeah, just as long as there's not loss of functionality, right?
**Pellared** 37:55 They mean, do you want me to write a comment, or do you want to do it yourself?
**Damien Mathieu** 37:58 Either.
**Pellared** 38:01 You will, okay.
**Damien Mathieu** 38:03 No, I said either. I can do it, or you can do it. I don't mind.
**Pellared** 38:08 So you can do it, and I can review it later.
**Damien Mathieu** 38:10 Okay.
**Tyler** 38:13 Okay, cool.
Also up, looks like this is actually approved, deprecate, read.
a bunch of stuff from… same kind of keys…
I don't know what I'm missing here, the changelog's not very clear. Looks like there's just… oh, there's been…
Okay, I think that's just this needs more review, right?
Robert?
**Pellared** 39:13 He's just looking at it.
But the command was not addressed, right?
Soap.
Yeah.
**Tyler** 39:27 is…
Oh, so you didn't want this thing after, if anything was read from the request was… you just wanted to remove that?
**Pellared** 39:35 No, I wanted to use the semantic convention to reuse the, I want.
**Tyler** 39:40 Oh, I see what you're saying. Oh, oh, okay.
**Pellared** 39:43 I didn't want to have, you know, strings, hard-coded strings, which are already the same content.
**Tyler** 39:47 I missed that part. Okay, that's what you're saying here, yeah.
Yeah, it looks like that hasn't been addressed, yeah.
Okay.
Cool, alright. Then we'll look for updates on that one.
Okay, environment variable propagation, that's a whole other thing. That's not blocking.
So, I think that's it for the milestones, then. We've got a few PRs, we're blocking mostly, Sam's PR, I think is kind of the big one, so please pay attention to that one.
And then we can move on.
Sam, you want to talk about refactoring the benchmark CI?
**Sam Xie** 40:34 Okay, I basically just want everyone to check this.
And… Yeah, just take a review.
Because it's been a while.
**Tyler** 40:52 Yeah, looks like Damien's taking a look. So you're just looking for another reviewer, it looks like, right?
Cool, looks like it's sharding?
Code Speed HQ, is this something…
Where does this come from? Is this just a… something you found…
Online, or is this something that the hotel community has kind of.
**Damien Mathieu** 41:21 I recommended it after the collector started using it.
**Sam Xie** 41:25 Oh, okay.
**Tyler** 41:27 Cool, alright, yeah, good to know.
**Damien Mathieu** 41:29 Yeah. Not perfect either, to be fair.
**Pellared** 41:34 Yeah, I mean…
**Damien Mathieu** 41:36 In the… it's… it's a question… it's always the same thing with benchmarks. It's a question of shared notes, and, like, in the collector, we're seeing, like, PRs that change code owners, and saying that benchmarks have been improved by 25%.
We have started changing code owners more often after that.
**Tyler** 42:00 Yeah, I'd do that.
**Sam Xie** 42:02 That's because we, they're, they're using Ubuntu code, what is that, a runner, GitHub Runner, but we were using bare metal, so…
a bit different.
**Tyler** 42:13 The, I have noticed in the OB project that our… the CI system's become extremely flaky… flaky lately, and I saw, Damon, you open an issue this morning about that, or PR.
**Damien Mathieu** 42:24 Yes, I tried looking into it yesterday, it's really… I don't know why it's flaky, but it's always on macOS, so I disabled macOS.
**Tyler** 42:36 Yeah.
**Damien Mathieu** 42:37 Windows is already disabled, so we still have Linux.
**Tyler** 42:41 The Linux one as well, Adobe is extremely flaky, but we're doing a lot of QEM, like, virtualization as well, so… things… I think moving to…
they've moved to different, like, underlying CPU, or underlying, like, VMs upstream, and so, yeah, I think that there's… there's a lot of instability in the CI systems right now.
Okay, this needs another review. I tried to take a look afterwards. Other people on the call, please take a look.
Robert, moving on, you want to talk about this?
**Pellared** 43:12 I want to have your opinions here. It's the latest comment.
Yeah.
So, I haven't started working on it yet, but there's one…
there's one person who is asking, as far as I understand the comment.
that they want to have something that looks API would work for the both
type of the attributes, like the old ones and new ones. This is how I understand, this comment.
And my opinion is that I do not want to support it, because
I even do not have an idea how to… I want to name the methods, for instance, add attributes, using the new, you know, the new types, and I do not want to have, I don't know, add the adder for the attribute package, and then for the existing one for the log package.
So, I'm just in favor of making the changes to the experimental package, and just, you know, getting rid of the log key values. That's my preference.
I think it will be also a huge burden for the maintenance perspective to… for the Lux SDK to… to work with it above all of these, but maybe I'm wrong.
**Tyler** 44:30 sorry, sir, can you explain what, what your…
What's your suggestion here? Do you want to just, like…
So the problem is, is, like, right now we don't have things like a byte type and, like an empty type in.
**Pellared** 44:43 No, no, no.
**Tyler** 44:43 package.
**Pellared** 44:44 I… if I understand the comment, is that someone wants to have the current… they do not want us to make a breaking change for the logs API, so they want to give a transition so that they want to have something, like, in transition, that when we are adding these new attribute types.
And we…
**Tyler** 45:05 Oh.
**Pellared** 45:06 They want still to have… they do not want to have one release which simply stops working.
for their existing bridges, or, you know, direct log API usages, and things like that. So they want something in between, and, you know, probably having logs API that supports both attributes, right? That's how I understand it. Or this is how I see it possible to work.
**Tyler** 45:35 Yeah, I'm with you on that one, that doesn't make a lot of sense to me.
Because, like, the idea of having, like, this opt-in time is, is,
So the way that this gets implemented is essentially in the logs API, you have two methods, one that accepts the old attribute, and one that accepts the new attribute.
Yeah.
**Sam Xie** 45:53 And then the next release, the old app attribute.
**Tyler** 45:56 Method gets removed.
**Pellared** 45:59 the problems?
**Tyler** 46:00 The question to that person is, like, I don't understand, like, in the semantic conventions, that made a lot of sense, because there was an environment variable, and, like, we could do this duplication on your behalf in the backend, but, like, you were literally gonna have to change your code. So, if…
there's an upgrade path where you want to change your code, then you upgrade the package and you change your code. And if there is a time where you don't want to do that, you just don't upgrade the package, and you still use the old…
API in the old package, right?
**Pellared** 46:27 Yep, I agree. Just wanted to double-check with you.
**Tyler** 46:31 I mean, I don't know, like, I don't see how you win anything by adding another method. Like, all I think you do is you create more confusion at that point, because then there's a release where there's two ways to do the same thing, one with two different types.
And then the next… then immediately the next release, there's not two ways, there's only one way, in that people who adopted that original… that package with a duplicate are super confused, because they had maybe adopted the wrong one.
Yeah, that doesn't make any sense to me.
**Pellared** 47:02 I agree, especially that
the other things… nothing apart from the logs AP, or logs stuff is not coupled to log… to the Logs API or SDK, so I agree with you. They can just upgrade other stuff, and leave the logs API and SDK in the version that they currently are.
**Tyler** 47:24 This does kind of… So, so, okay, if we decide that we're gonna do that, like.
How… how do we want to add these new features to the attributes package?
**Pellared** 47:38 I just want to add new functions, etc.
**Tyler** 47:41 Yeah.
**Pellared** 47:42 Business is stable?
And this is something which we will do anyway before, you know, it's a prerequisite anyway.
**Tyler** 47:49 So…
I think that that sounds like what I would… I don't know if there's a better way to do that, other than, like, creating a duplicate attribute package that we would then try to prototype with, which isn't gonna really… it's just gonna be a lot of work.
So, I think we need time to work with it when it's on main, though.
**Pellared** 48:05 So the question is, is like.
**Tyler** 48:08 is this going to get prioritized after the next release? I guess is kind of the question. Or after a release, because that's when you have the most amount of time to actually play with it before it gets released, right?
**Pellared** 48:20 Yeah, I want to prioritize it.
This one's at least.
**Tyler** 48:24 Well, if that's the case, I…
**Pellared** 48:26 I just have one question before… because I already had… we already had prototypes for it.
And I also started to think about one… about the immutability. Do you want the attributes to be immutable, as it is right now, also for the new… for the new types?
**Tyler** 48:46 Mmm… like a bite slice?
**Pellared** 48:48 or a map? Yeah, or a map, do we… if there's an accessor, do we want to make a copy each time of it?
**Tyler** 48:55 David, I think you should pay attention here.
**Pellared** 49:01 I'm mostly concerned about the resources.
**Tyler** 49:04 Yeah.
**Pellared** 49:05 And kind of entities.
Yeah, I'm just afraid that it's a food gun. And also, I think that these types
Complex types should be used… should be not used frequently. And if you should even warn users that, you know, it's a performance overhead, it's a problem to index this kind of stuff, just use it with caution.
**Tyler** 49:32 How are we gonna do a map type?
Doesn't this need to be comparable?
**Pellared** 49:38 It is. I already did it.
It will be comparable, so it will be sorted slice, basically.
occupied.
**Tyler** 49:43 Oh, that's right. Yeah, that's how we did it. Okay, yeah, sorry, thanks.
Yeah. What are we doing right now in the logs API?
Are we copying there?
**Pellared** 49:56 No, we are not stopping.
Right now, there's some… I think… I think there's a documentation. Because, you know, there's no… it's not… yeah, we are not doing this. I just followed S-Log.
which doesn't copy, to reduce the amount of HIPAA locations, when the SDK, you know.
**Tyler** 50:14 And then…
**Pellared** 50:14 That's me, bro.
**Tyler** 50:15 In the attribute package, we are copying for reference types, right?
**Pellared** 50:18 Yes.
So probably you'll do the same, and just decrease the performance.
**Tyler** 50:28 Which way is, is,
can we change our ways in the future? Like, if we do not copy, and then we want to copy.
Is that a breaking change, or… I mean, obviously none of them are, like, compile breaking, but, like, functionality-wise, like…
**David Ashpole (dashpole)** 50:48 If you were.
**Tyler** 50:49 That's the safer way to start.
**David Ashpole (dashpole)** 50:55 I think neither one is, like.
that's safe? Like, one, you'll add a big performance regression if you go from not copying to copying, and then the other…
You'll allow… you'll… Make some code that used to be safe.
no longer safe. If someone was, like, passing the slice and then modifying it in a coroutine or something, right?
**Tyler** 51:18 Yeah.
**David Ashpole (dashpole)** 51:19 Or modifying it, period.
**Tyler** 51:28 I'm like, I… So, I… we originally wrote a lot of this stuff to be very safe.
So that… There's a lot of… we take away a lot of these foot guns, right?
And then, you know, years and years of using Go at this point, like, I don't think that that's common in the Go language.
I don't… like, obviously, you just copied from S-Log, right, where they don't do any of this copying there, right?
The problem, I guess, maybe, is then you'd have inconsistencies in the attribute package, one place where we have, like.
**Pellared** 52:04 Resource will be…
**Tyler** 52:05 Well, no, I mean, like, no, that's not what I'm saying. Like, what I'm saying is, like, if I pass you an int slice, that's gonna get copied, and then now if I pass you a map type, it's not. So, like, I guess I have to read the docs to figure it out, but, like, there's inconsistencies there, right?
**Pellared** 52:19 That's why I probably prefer to follow… follow the thing we… follow the current design.
**David Ashpole (dashpole)** 52:28 Do we want to introduce, like, unsafe methods?
Across the board or something?
It's a lot of API surface, but it's like…
Makes sense. And we're kind of just aiming back to users, but…
**Pellared** 52:45 Good idea!
**David Ashpole (dashpole)** 52:47 I don't know, it feels kind of gouish to have…
**Pellared** 52:50 It's where it goes.
**David Ashpole (dashpole)** 52:51 on Facebook.
**Pellared** 52:52 It's very ghostish, and it could be more performance.
**Tyler** 52:59 So wait, like, we could have, like, a… an unsafe package that would contain creation?
**Pellared** 53:03 No, no, unsafe methods to the attribute package, like, unsafe slice, unslice…
**David Ashpole (dashpole)** 53:10 unsafe with attributes, and it just doesn't copy, and you have to read the docs, or…
**Tyler** 53:17 Well, so it's all functions, right? So it's, like, unsafe, inslice, or something like that is what the function name would be, is what you're saying? Okay.
**David Ashpole (dashpole)** 53:29 We usually…
**Tyler** 53:30 I don't know, we're getting caught in the weeds, but I see what you're saying, like, but yeah, just adding these things that are, like, a no copy, right, is what you're saying.
And then the default one is the copy, yeah.
**David Ashpole (dashpole)** 53:41 the one that users will use by just dint of, like, reading the GoDocs is probably not the one that says unsafe, and then…
If they're like, oh my goodness, why is this making copies?
This is on my hot path, they can read it, and…
**Pellared** 53:56 SDK will lose it.
**Tyler** 53:59 That was a great fan, yeah.
**David Ashpole (dashpole)** 54:02 Yeah, true.
**Tyler** 54:03 I, yeah, I like that idea.
**Pellared** 54:05 I just like it.
**Tyler** 54:07 Yeah.
**David Ashpole (dashpole)** 54:08 Okay.
**Tyler** 54:10 Okay, so Robert, I think that's your answer. Let's do the copy, and then if we want to… okay.
Okay, we are coming up on the end of time. We've got 3… less than 3 minutes left. Any other topics people wanted to bring up, or things to mention? Who's going to KubeCon Europe, by chance?
Yeah, Robert, he, Damien… David?
**David Ashpole (dashpole)** 54:35 Nope, sorry.
**Tyler** 54:36 Oh, dang it.
**David Ashpole (dashpole)** 54:37 Can't be bothered to leave the country.
**Tyler** 54:39 Yeah, fair enough, I get it.
Well, cool. Alright, yeah, that… I'm looking forward to that. That should be fun.
Yeah, awesome. Any other cool projects or uses of OTL Go that people have seen in the wild? How's the Kubernetes space, David?
**David Ashpole (dashpole)** 54:56 It's good. There's, some guy from Netflix, I wanna say, who's, like, really gung-ho about getting tracing in the scheduler and, doing context propagation.
properly. So, I think we have a plan that's, like.
it's quite interesting, I can pass it along, but, it's a KEP, and they're gonna use span links instead of… like, our previous attempts were with parent-child relationships, where, like, if you had the deployment controller make a replica set, and then the replica set do something, you'd get a tree of parent-child, but because it's all async.
we're gonna use links, and that solves some of the problems that we were having, or that we had with the previous design. So I think this one is maybe less usable right off the bat, but…
More likely to succeed. And has someone behind it who's excited and seems to have time, so…
Nice. All good things. And then…
Yeah, I'm hoping to adopt the declarative config instead of the Kubernetes homegrown file format for configuring OTEL.
**Tyler** 56:00 So… Oh, cool.
**David Ashpole (dashpole)** 56:01 But maybe that'll be a follow-up to some of this other work.
**Tyler** 56:05 Yeah, we should probably talk more about declarative config, but that's gonna be a next week thing, I think, so…
Yep.
Cool.
Well, awesome. Yeah, we're right at the end of the hour. Thanks everyone for joining. Good seeing y'all. I will see you all in a week's time, or asynchronously. Till then, bye.
