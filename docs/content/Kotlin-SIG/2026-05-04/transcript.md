SIG: Kotlin SIG
Date: 2026-05-04
Duration: 21 minutes
Zoom Recording URL: https://zoom.us/rec/share/d1eF52zH1dwGpXaJ1VIty6TCNUwxgWtn7fzD5Wv6gKrEBYN5wV2cPEr0tqB21iC0.dccQp1j_XxcKC9ot
============================================================

## Zoom Recording Transcript

**Jason Plumb** 00:13 Might just be us two today, we'll see, right?
**Hanson** 00:16 Yes, although I don't think it's the only holiday in… oh, definitely Jamie won't be here, but, Carlos could be here, just because, I don't… it's… the bank holiday thing is just this weird British thing, so…
**Jason Plumb** 00:31 Yeah.
Well, I mean, today's a good day not to be online, because there's a bunch of Star Wars dorks.
Always on this day, I'm like.
**Hanson** 00:41 I feel like it… this is new. This has only been a thing in maybe… like, 10, 15 years. It didn't used to be like this.
**Jason Plumb** 00:51 Well, I think it comes, Along with the broadened cultural acceptance of puns being okay, which I'm not okay with.
**Hanson** 01:03 I'm okay with puns, but when you… when you overplay it, like, puns.
**Jason Plumb** 01:06 Oh, yeah.
**Hanson** 01:06 over plate. That's the problem.
**Jason Plumb** 01:07 Oh, yeah.
Yeah.
Well, so we have a pretty light agenda.
And I just threw this in on your behalf.
**Hanson** 01:19 They're so cute.
I actually have a PR that I should clean up and submit.
To deal with some of this.
**Jason Plumb** 01:31 That's cool. So this is a build time check, right, the require?
**Hanson** 01:34 No…
**Jason Plumb** 01:36 runtime check.
**Hanson** 01:37 Yes! Okay.
Which is why, which is why, For telemetry SDK to blow things up, in such a manner is, suboptimal.
**Jason Plumb** 01:51 I mean, we can't. Like, it… yeah, we can't… there shouldn't be any cases where we crash an app. Like, that's just full stop. We can stop generating telemetry if we're misconfigured, or if something goes terribly wrong, but yeah, that's… Kind of the worst case scenario is if you crash an app.
**Hanson** 02:07 Yep.
This is, like, this is completely side effect free if it doesn't work, we should notify. There's, like, a platform log that we have, where I guess, if you're running this on the server, you'll get a log that says blah. But, you know, if you're running this on mobile, that log doesn't say anything, but at the same time, it's easy to, like, to just not do this, or throw an exception, throw a checked exception if we use a factory method. There's a bunch of ways to handle this. This is, this is, you know, this is just… yeah.
So, my thing is, we shouldn't use anything like check not null or require, inside constructors, in production code paths, so…
**Jason Plumb** 02:53 Yeah, I mean, I don't think… I don't think you're asking too much. No, no. I think, so, like, in this particular case, right, if someone… and it's internal, so it's not directly user-facing, but if someone… like, the worst case scenario would be, like, somebody puts a trace parent, header on the wire into a service, and that service goes to decode it, and gets a version that is the wrong length, for example.
Or it decodes to a version that's the wrong length, if there's… I don't know what validates ahead of this, but then it would throw an exception here, right?
**Hanson** 03:25 Yep. If… if you validate before you actually get into this internal constructor, that's totally cool. Then this is effectively just a redundant check. And then I would say, why would you want to just… But I do want to have that check and just basically say it's a precondition, and have a test verify this, or something like that. Or have a test verify that the entry point validates. But… Yeah, throwing is… Throwing is bad.
Even if it's an invariant.
**Jason Plumb** 03:56 Yeah.
**Hanson** 03:57 It's fine, it's easy to fix, it's, you know…
**Jason Plumb** 04:02 So, I mean, then you're faced with the decision, right? In this case, if you do get an invalid version, what do you do? And in many cases, I know, at least in Java in many cases, they're effectively using, like, a no-op instance, or, like, a null object pattern, and that's what you end up with, right? Is, like, something where it's completely invalid.
**Hanson** 04:22 Yep, I think for, for trace and span IDs, it'd just be, like, the, the padded zeros, places where it takes empty string, it'd be empty string or null , a trace parent here, it makes sense to kind of pad it do the default, the default trace parent, where I have no, I have no trace parent, or I have no, you know, trace ID, or I have no parent.
So, that…
**Jason Plumb** 04:50 over this.
Unless you have other stuff you want to talk about, I'm just kind of down a rabbit hole now.
**Hanson** 04:56 Nope, it's… this is, it's one of these things that, It's fairly easy to check, because really, there aren't that gonna be that many, we could probably even…
**Jason Plumb** 05:11 Java doesn't have an object that represents trace parent, I don't think.
**Hanson** 05:16 Right.
There's, like…
**Jason Plumb** 05:20 Like, the propagator that sort of knows how to munch these, but… Like, you know, there's the version size.
Tracer. Which I'm guessing is the same thing here, right? Version LEN, I don't know where that comes from, but… I'm guessing that's 2?
**Hanson** 05:37 Yeah, some constant, probably, you know, the companion object below, or something like that.
**Jason Plumb** 05:44 There it is, yeah, so two, yeah. So that's… this is the equivalent of this, and maybe I had this feedback, too.
Did I…
**Hanson** 05:52 Yes.
**Jason Plumb** 05:53 This is the thing that's doing the encoding and the decoding.
And… I think the… I think the class name could match that better, like, maybe we should create separate encoders and decoders, like transparent encoder, transparent decoder, and that way it doesn't… make one think that it's the actual data object as well, which in this case it kind of is, but… Yeah. Yeah. But yeah, so what does Java do if… so, like.
**Hanson** 06:19 It probably just returns empty string for trace parent if there's no class, because…
**Jason Plumb** 06:22 Version size. There's probably a validation for it, let's see.
Size… Nope.
**Hanson** 06:32 I… I think… if… I think it just propagates the invalid… invalidness, or returns, like, a… A no-op instance, or… or some sort of empty string kind of thing.
**Jason Plumb** 06:48 Yeah.
**Hanson** 06:49 if they're not consuming it… if they're consuming trace parent just as, like, the value of the header, like W3C, blah blah blah, whatever, then… you know… Multiple ways to handle this.
There you go, returns nothing.
**Jason Plumb** 07:02 Yeah. Well, that's when injecting the context.
Extracting it is, like… Let's see, I don't know where this extract impulse, yeah, so… Yeah, just a bunch of invalid span contacts.
**Hanson** 07:16 Yeah.
if the method is, like, set this on a thing, it'll just be a no-op. If the method is.
**Jason Plumb** 07:25 Oh yeah, look at this. This is where… this is probably where it gets hit, actually, if it's…
**Hanson** 07:29 There you go.
**Jason Plumb** 07:29 Extracting it from the header.
It's like checking all these fields.
**Hanson** 07:35 Do we need to verify the version is hex and the version length is expected 1? Sure, why not? You're already doing this many.
**Jason Plumb** 07:41 If it's not valid, hunt. There you go. It's fine. I mean, that's… so we should really consider doing something similar, where if you call… where is the implementation here? If you call… if you try and… Create a transparent with these invalid ones, you just get back the invalid representation.
**Hanson** 07:57 Yeah, I'm pretty sure that's what you would… that's what the getters, like, whatever, anywhere that returns this, like, I think this is just doing required, because it's thought as being internal, so, you know, why not do that? But I don't even think we need to do that, like…
**Jason Plumb** 08:12 Yeah.
Okay, I think we're… I think we're pretty much aligned on that. So here's another PR… or is this the issue?
This is another piece.
**Hanson** 08:23 There's a bunch of places where, like, the sampler… there's, like, 3 or 4 places where it's, it's using requires. This is where you might have mentioned this if.
**Jason Plumb** 08:33 Yeah, this encoder… this is where I mentioned the.
**Hanson** 08:35 There you go.
**Jason Plumb** 08:36 Yeah, okay. That's just a continuation.
**Hanson** 08:39 No, I would wait for us to merge and submit my PR.
**Jason Plumb** 08:57 Hi, Carlos.
**Hanson** 08:59 Carlos?
**Carlos Alberto Cortez** 09:01 Hey, hey, hey! Yes. Hello.
**Jason Plumb** 09:06 What does this mean, no SIG today?
**Carlos Alberto Cortez** 09:09 There's no implementation.
Today, the, when, like, upon calling said attributes, it mirrors any existing attributes.
I wanted to double, you know, make sure that that was the case, based on the discussion we had last week.
But yeah, all…
**Jason Plumb** 09:28 Go ahead.
**Carlos Alberto Cortez** 09:30 Yeah, when, like, yeah, basically all six, like, like, I think I didn't review Erlang, probably, or Swift, but other than that, Yeah, there's an implementation currently that allows you to just go and clear everything that is spanned, or, you know.
Such a container has, and then just replace and start with a blank.
In a blank state.
Yeah, hope that provides some, you know, insight into what we should be doing.
**Hanson** 09:57 Other than call set attributes with, like, an empty map.
that would effectively erase everything, right? Because it'll… in Java, at least, it just replaces the existing attributes with what's passed in.
**Carlos Alberto Cortez** 10:12 Yeah, correct. So, for example, let's say that you have 3 attributes, like in the span, and then you just pass 3 attributes with 3 more attributes.
So they will be added, and if they are, you know, if some of them are duplicate, like, same key, then you just update them, you know? But you are not clearing anything, yeah.
**Hanson** 10:31 Oh, you're… Really? I thought the reason why we had this was that Java was, like, replacing everything, instead of updating.
**Carlos Alberto Cortez** 10:41 No, no, I wanted to, yeah, verify that, no, it's not the case.
**Hanson** 10:44 Oh, okay.
**Jason Plumb** 10:46 You did… you did talk to Jack.
**Carlos Alberto Cortez** 10:48 I didn't, I just wrote… I checked the code, I can't double check, but yeah, I was checking… let me share my screen, maybe, or maybe it's…
**Hanson** 10:58 That's…
**Carlos Alberto Cortez** 10:58 If it's still here. Wait a second…
**Hanson** 11:02 Interesting.
I wonder if it's a difference between, like, calling set attributes, passing in the attributes object, versus on the attributes object, there's, like, an update or something like that.
Because one thing that we don't have is that attributes object.
**Carlos Alberto Cortez** 11:26 Yeah, correct. But the way that's… No, I can… wait, the thingy cannot.
**Jason Plumb** 11:33 You want to share? I can stop.
**Carlos Alberto Cortez** 11:36 Yeah, I can… it's just something very small, anyway.
Sorry if it's too big for you. No, it's.
**Hanson** 11:43 Oh, that's great.
**Carlos Alberto Cortez** 11:44 Okay, so basically, you know, as you can see here, this is the, SDK span, so this is the one that implements the interface in Java, and we don't have said… we don't have set attributes at all defined here, we only have set attributes.
Which is, you know, basically just take one value, like, the key and the value, and just add it, you know?
And I was wondering why, and the reason is that the set attributes, at least in Java, it's defined at the base interface level, which is a default thing, which… what it does, simply, is that you get set… called setAttributes.
on the span.
So we are not.
**Hanson** 12:21 Oh…
**Carlos Alberto Cortez** 12:23 I can… if there's some doubt, I can triple, you know, check with Jack.
**Jason Plumb** 12:27 No, this is… this is clear.
**Hanson** 12:29 Yeah, this is clear.
**Jason Plumb** 12:33 So our implementation is accurate and consistent then, right? It both meets this… because I want to make sure I understand it, that our current implementation does the same thing. It does not overwrite existing ones when you pass in the collection And that's consistent with what Java's doing, we see it right here, and it's also consistent with spec language.
Which could be… we think the spec there could be improved a little bit, but at least it's consistent.
**Carlos Alberto Cortez** 12:59 Yeah, yeah, this is actually one of the reasons why I think we wanted somebody from the TC to help in New 6, because there are many things that Like, people who have implemented existing stuff know, but it's not super clear.
So yeah, yeah, I will create a note for myself to go and make sure that, you know.
it's clear. I don't know, maybe… they're having conversations about probably adding more languages in the future, of course, like Z. Like, I don't know if there's interest, something like that, and it could be useful for them, you know.
**Hanson** 13:35 Yeah, there exists both a set all attributes method that takes attributes, and a set attributes method that takes the, also takes the same parameter, but they behave in two different ways. And we looked at the one that has the same name, but we didn't look at this other one, which… does the same thing.
**Carlos Alberto Cortez** 13:59 Yeah, correct, correct. Yeah.
**Hanson** 14:04 I wonder how many people… use setAttributes, the method, then.
Because it'd be… it'd be pretty easy to kind of, you know, use one and then confuse and not… not worry about the other one.
**Carlos Alberto Cortez** 14:18 Yeah, seed attributes is also optional at this, you know, API level.
**Hanson** 14:24 Oh, okay.
**Carlos Alberto Cortez** 14:25 That's in case you want to set… well, the thing is that in Java, you actually are passing an attributes object, which is a container, but for example, in other languages, you pass, like, you know, like, a list, a variable list.
Which is Keith Bloss.
Values, so you just… So, yeah.
Oh, there we are.
**Jason Plumb** 14:46 Yeah, so this just says you can… you… you know, optionally, you can have a method that sets many, and it doesn't talk about replacing, but it's saying.
a single attribute with the same key should override, that's fine. I'm surprised that's even optional, but whatever. And then, it doesn't talk about the sort of collection case overriding, so I think it's good. I think that's, you know, I think there is some… some room to improve the spec language here, but I think what we've got is good.
**Hanson** 15:14 Agreed.
**Carlos Alberto Cortez** 15:14 That's correct.
**Jason Plumb** 15:15 Okay, so I think we can close this one.
Or do you want to keep it open?
**Carlos Alberto Cortez** 15:23 Jamie has some prototypes, there's a comment about he writing some details there, so it's up to you.
**Jason Plumb** 15:31 Yeah.
Oh, any value, yeah.
**Hanson** 15:40 Hmm…
**Jason Plumb** 15:41 This feels like a different topic, but…
**Hanson** 15:43 Yes.
**Carlos Alberto Cortez** 15:44 Yeah, absolutely.
**Hanson** 15:46 Yeah, I think that this one… is it this… Yeah, yeah, this one is not about the all attributes one, this is just about, So maybe if this issue is more than about the all attributes, we can at least tick off one point of it, and then see.
**Jason Plumb** 16:01 I mean, I guess if it's about adding attributes, he's like, should there be a way of adding any value as an attribute value?
And I think the answer's yes.
Wait, the spec says that it should be one of the types defined in any value, not any value itself. Ugh.
I mean, that's…
**Hanson** 16:20 Yep.
**Jason Plumb** 16:20 I think the spirit of the spec is that you should be able to provide any value.
As a, as an attribute value.
**Hanson** 16:31 It… in which case, then how do we do any mapping?
how do we know something is supposed to be cast down to any value? I guess you've explicitly provided, like, the any value off.
Okay, this feels like a different thing that we should discuss, but it's good to have clarification on the, the set attributes, so… one… checkbox.
**Jason Plumb** 16:50 Yes, I agree.
Okay.
**Hanson** 17:04 So for funsies, we could look to, update the spec and just add a language to clarify, This all thing, but it's certainly not blocking any of this stuff.
**Carlos Alberto Cortez** 17:15 Yep, I would say so.
**Jason Plumb** 17:39 Okay.
So then, the AnyValue PR I thought was interesting. I think I reviewed this one.
And I did bring up the null case, because that's not yet accounted for.
**Hanson** 17:59 Right…
**Jason Plumb** 18:01 Alright, so in the spec, they are pretty clear about that, I think.
**Hanson** 18:06 No, it's just removing, or do we keep the… we keep the key, but we know the value, so the value would.
**Jason Plumb** 18:11 Exactly, there needs to be some representation of, like, the language idiomatic null , or… And we probably… we… since this implementation provides, you know, string… let's… it's sealed, right? So there's, like, this… the string version, Boolean, blah blah, every… every specific type is here. I think we also need the null type.
**Hanson** 18:30 Yep.
**Jason Plumb** 18:31 So, I'm inclined to have it in that same PR.
But I'll leave it to the original author to decide if they want to do that as a follow-up effort. I think this… I think this PR looks good. I like the fact that we can leverage sealed. That's something Java doesn't have.
It's actually pretty nice.
**Hanson** 18:50 Yeah, I'll…
**Jason Plumb** 18:50 I guess future, like, modern Java actually does have sealed types, but… Yeah.
**Hanson** 18:57 Yeah, what version of Java?
Such a two? Yeah.
**Jason Plumb** 19:03 Yes.
**Hanson** 19:04 Yeah, it'll be a while.
Java 8 is still supported, right?
**Jason Plumb** 19:12 Yeah.
**Hanson** 19:15 Yeah, know about you makes sense, because we don't want to differentiate between… or you can't in a type-safe way.
In an… To make it, we don't have to explicitly specify type, there's no way to differentiate between the null long and the null double, so having a null value when we serialize down, like… Yeah. Yeah.
That should be easy.
**Jason Plumb** 19:38 Yep.
Alright, so that is this one… Yeah, that should auto-correct.
Why not?
There it goes.
**Hanson** 20:04 It says, whatever, that's… that's what…
**Jason Plumb** 20:05 Gotcha.
**Hanson** 20:06 That's what it's told you.
Cool.
**Jason Plumb** 20:13 Alright.
**Hanson** 20:16 We can end early if we have, no, nothing else?
**Jason Plumb** 20:19 I'm gonna show you my mug. Oh, it's getting blurry, here we go.
**Hanson** 20:23 Yeah, I'll… you're also… you have to stop sharing the screen, too, because I can't…
**Jason Plumb** 20:26 Oh yeah, let me stop that.
**Hanson** 20:27 You're tiny.
**Jason Plumb** 20:29 Yeah, there we go.
**Hanson** 20:31 Chinga Leming, bruh? What does that mean?
**Jason Plumb** 20:35 It depends on your translation, but it usually means, like, fuck immigration.
Yeah.
**Carlos Alberto Cortez** 20:46 That's… I approve that.
**Jason Plumb** 20:51 Cool, well, I think that's all we have for today.
**Hanson** 20:54 Cool.
**Jason Plumb** 20:54 Steve in the comments.
**Hanson** 20:57 Sounds good. Thanks, Carlos!
**Jason Plumb** 21:00 Thank you!
**Carlos Alberto Cortez** 21:00 For sure. Would you like to show.
