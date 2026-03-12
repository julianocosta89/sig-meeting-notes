SIG: Go SIG
Date: 2025-08-14
Duration: 59 minutes
Zoom Recording URL: https://zoom.us/rec/share/fXI_UJYzzG8iHqz-2BtvIi1VONLiPRmAWxlyaP1XwxK1yVJ4WgFbofJbhTmuctVW.3t9s6o-R4tRjtchi
============================================================

## Zoom Recording Transcript

**Tyler Yahn** 00:15 Anyone?
**Owen Williams (he/she)** 00:17 Hello.
**Tyler Yahn** 00:18 How's it going?
**Owen Williams (he/she)** 00:21 Pretty good.
**Tyler Yahn** 00:22 Nice Yeah, I'm not too sure how many people are gonna be able to make it today, actually. I'm looking at… Slack, and looks like a lot of people aren't able to join.
So it might be us, actually.
**Owen Williams (he/she)** 00:45 Alright, I think Robert might be joining.
**Tyler Yahn** 00:48 Oh, really? Okay, I… last I heard, he was on vacation, so that's… yeah.
That would be….
**Owen Williams (he/she)** 00:54 I was just chatting with him, I think.
Yeah, after the meeting, he's finished for today, so….
**Tyler Yahn** 01:02 Whoa.
… Oh, okay, yeah. Oh, yeah, there's an exception in his comment. Okay, alright.
Yeah, okay, cool, we can wait, just a little bit, not too… Fast, looks like he's already added his name. And there he is. Okay, perfect.
What's up, Robert?
**Robert Pająk** 01:31 Hello. So, it's okay.
**Owen Williams (he/she)** 01:34 So….
**Robert Pająk** 01:34 Bye.
On our move lists to support.
**Tyler Yahn** 01:42 Cool, alright. So, let's, let's go ahead and get started. Yeah, so… looks like everyone's already added their name to the attendees list, there's some agenda items.
And, yeah. So, I guess David's not gonna be here, … But he's asked people to take a look at this, so I guess this is also maybe for people looking at the meeting notes or watching this recording. … because I think most people on the call have already taken a look at this. So, this is a proposed idea from a while ago, where our sets are currently using, an interface, that's pointing to some array.
As its key, and, … This works just fine, you can compare these arrays, in Go.
But fine being the key term there, it's not optimal. The… especially for, like, map comparisons. Using, this in a map is definitely, slower than a lot of the fast paths that, maps use for comparison operations, one of which is, like, UN64.
There's definitely a fast path there. So, the idea is we could take our, attribute, arrays that are sorted unique, for that for a set.
And create a hash, for these.
And that's what this is resurrecting, and it's using these new benchmarks that David has also added here to show, some pretty significant improvements, especially in the larger attribute sets.
I was looking at the scale factor on this, I'm pretty sure this scales linearly as well, so this actually, you know, becomes considerably worse for, you know, linear amounts as this goes up. So this is, I think, worth taking a look at.
There's, … oh.
I think I just saw David actually join. So there's definitely, I think, some more thoughts to look into here. I just was going through this again. It's obviously not, like, the easiest PR to review, hence why it's the second, attempt at it.
But yeah, I think it's actually worth taking a look at. I think the one thing… actually, I think there's… There's two, I think, high-level points I wanted to maybe get at, and this is, like, this, like, our compatibility guarantees, I think, is probably the number one, and, like.
what that looks like going forward. I think it just isn't as big of a issue. And then the other is, like, the collision rate, is something I just, left as a comment, but… Maybe we could just talk about this, like, compatibility. So, like, right now, what is happening is we're actually going to change, … the second structure is going to change. It's going to get another hash added to it, but the distinct, type itself is also, like, going to change.
And that's going to, … Oh, this is still loading. That's going to become just a hash instead of the data type, … Yeah, I hate this package, I really wish it never got released the way it did, but it is the way it is. And so, I think that, like.
Kind of the question is, is like… Where is this gonna bite us?
… I guess?
Is kind of my question.
Because one of the things that we do say here is that, like, there's no compatibility guarantees across versions, like, for equivalents. … So the only place that I could see that happening is, like, somebody is recording a bunch of different attributes, and, like, right now it's… it's, like.
Either considering them the same, or it's not considering the same, and then they're going to upgrade, and then that's going to be switched.
I don't see that happening, based on what we're doing here. Like, in fact, like, … Well, actually, maybe that's not true. I do see that only happening if there's a collision, with our hashing, because then that equivalence is going to be, determined, especially in, like, a map setting is going to be used. So, that has a possibility there.
it's a very small possibility, which we can talk about, I think, next. But, like, I think, like, otherwise, like, let's just assume there's no collisions and that it's, like, a collision-free hashing, for the sake of this argument. Like, I don't think there's actually a change in behavior that we would see going across this.
outside of maybe, this comments I left down here about this marshalling JSON, like, I'm not… That might be weird, so, like, if you were preserving some sort of, like, set attributes in an old format, and then trying to deserialize them here… the… that might be a problem, but I'm not exactly sure that we ever really supported deserialization, … So that might just not actually be a concern as well, … But yeah, I… maybe I'll just… I'll stop, because I've been talking a lot here, and thinking about it.
**David Ashpole** 06:37 I mean, we could presumably keep the old way of serializing.
The other thought I had was, if we didn't want to introduce Any breaking changes, we could add a new method called hash.
That just literally gives a UNT64.
And we can document the behavior, and then we can have the SDK adopt it.
It seems kind of duplicative.
And also, the equality function will also stay presumably, very slow.
But the quality, as far as I can tell, isn't on our hot path, and you can always do Dot hash equals equals dot hash, if you really want a fast quality.
**Tyler Yahn** 07:22 But it feels like….
**David Ashpole** 07:25 It feels like we're handing users a foot gun a little bit if we do that, because we're giving them a method that sounds like it does the right thing.
And secretly is gonna take an enormous amount of… like, you saw the benchmarks. It's, like, an enormous amount of time that these, like.
Lookups are taking, compared with all the other stuff we do.
**Tyler Yahn** 07:48 Yeah, and I, … I think I originally, when I was writing this, I started with what you just described, and I'm not opposed to it, let's… I just want to point that out. Like, I think that that's not, like.
out of the realm of possibilities, but it also means that the underlying implementation of the hash becomes exposed to users. So, like, in this case, like, if we use, like, a UN64 for this, like, a 64-bit hash, right? And we decide, like, hey, the collision rate's actually too high, we need to go to 128-bit, like.
too bad, like, because you can't, like, you have to… you have to do a new function now as well, right? Like, … so, like, I think that becomes… problematic, I guess, is what I would say.
**David Ashpole** 08:28 Yeah, I….
**Tyler Yahn** 08:31 So, also, on your point of, like, I don't… like, this actually isn't changing the serialization, … Right? Like, it's still… this is just a different location for that same data. It's the… it's the problem that it doesn't include the hash, so when you try to deserialize this now, the hash is gonna be empty.
actually, I think it's just gonna error, because it won't know how to actually deserialize this anymore, because it's, like, there's no, like, one field to one value, so anything that was being, like.
interpreted. I actually don't know if it was correctly deserializing this, so, like, this may just not be a problem, hence why my kind of wishy-washy comment here, but, like, I, like, if that's the case, then I don't think we're actually going to have any problems.
So, yeah.
You're muted, David.
**David Ashpole** 09:15 I mean, hopefully, if we have any concerns, we can just write a unit test.
Yeah, I think that's….
**Tyler Yahn** 09:21 That's… that's… Worth doing. Yeah, let's do that.
… So yeah, I think… I think if that's the case, like, I don't see any issue, because, like, if you're ever going to do a comparison in code, like, you're never gonna actually have this problem across versioning, right? Like, you're always going to be using the same version of this package, like, there's no way to compile a Go package with two different versions of this.
that I know of, maybe, if you use a different compiler? … I guess maybe that's… yeah. Like, if you're using the Go mod system.
And you… I guess you could vendor it. Okay, but, like, let's just assume you're not really trying to, like, go outside of the norm in that comparison. I think that, like, this guarantee here is already, like.
kind of… valid, right? Like, we don't provide this guarantee across, like, stable versions.
Also, Robert, I was confused, like, this seems like this is actually going to… No, no, I….
**Robert Pająk** 10:15 If you refresh, I made it wrong, I just got confused between distinct and set.
Oh, yeah.
**Tyler Yahn** 10:22 Oh, okay.
**Robert Pająk** 10:22 My comment was… my comment was wrong. I was… I was too careful in being careful.
**Tyler Yahn** 10:29 Alright, alright, yeah, okay, then I'm a little bit less confused, I guess, maybe. But yeah, so, like, I think that we're already saying that, like.
Yeah, like, we've already made this distinction across versions, so, like, if somebody's trying to do this, like, we already have documented, like, don't do that. And so, like, their comparison operations shouldn't notice the difference at all, so, like, I don't see this as any, like, behavior-breaking changes, I don't see… other than performance, like, it's going to change the performance, which is….
**Robert Pająk** 10:56 12th, yep.
**Tyler Yahn** 10:57 Yeah.
So I don't think that that's a problem.
That being said, I do think that, I mean, I already found a bug in the FNV1 implementation.
That I didn't catch the first time, where we're actually, like, I guess maybe, yeah, like… This is iterating over runes, … the… that's not… you need to iterate over bytes. So, like, things like that, like, we need to, I think, be careful. Obviously this is a POC, so, like, it was one of those things where, like, the tests cover it, but there's probably edge cases we need to pay attention to.
So, it's not, like… like, it's very wrong. I think that that's just more about, like, polishing this up to actually get it, like, in a final state. … I do think, though, that, like, the question of… Like, collision rate is kind of gonna be… important here, like, I think it's extremely small, given the fact that, like.
You know, out of the key space of, like, … so this is a 64-bit, like, hash size, right? Like… like, we already have a cardinality limit of, like, maybe a default of 2,000 one day, so, like, the key space that we're ever gonna actually be covering here is, like, really, really small, comparatively. … on, like, a normal running operation, I guess. So, like, the only time that you're ever really gonna see this is in, like, runaway cardinality, and it's just running for really long lifetimes, at a really high rate. Like, then you're gonna see collision rates.
So I really don't think that, like, our approach here with the 64-bit, like, FNV, like, approach is actually going to be a problem. I said that we should probably do a little bit more analysis of this, like, I was trying to do that before the meeting, and then just, like, ran out of time.
But I think, like, we're actually doing pretty good.
with what we have here. And if we don't expose this to the user, changing to… A higher, bit size by using, you know.
Two 64-bit integers are just going straight to the 128, bit FMP1. I mean, like, there's a… a 1024-bit size, FNV1, like, algorithm, like, if we really wanted to, like, get into this and, like.
But there's… I think there's other things we could do beforehand, if we ever had any, like, collision rates that are gonna cause us problems.
Yeah. So, yeah.
**David Ashpole** 13:19 I also wanted to say, like, part of the inspiration for this and the other change was doing a… like, comparison of the structure of the Prometheus Go client, and the… OTEL SDK for metrics, and looking at some of the major differences. So, like, the Prometheus client.
Has been around for almost a decade, and uses… FNV… You went 64-bit.
So, like, they've been doing this for a long time. I'm not aware of anyone ever complaining about collisions, so to me, that's, like, a pretty good signal. Like, we've had I don't know.
a dozen users at this point complain about the performance of the… and I've had a bunch of internal people reach out to me as well at Google, like… So, to me, just, like, The two problems are very different in terms of… Impact, and yeah, like… I'm not concerned. It's still good to do the math, like, but… I think experience says, like, this is probably the right change to make.
**Tyler Yahn** 14:27 No, I think that's a good point.
….
**Robert Pająk** 14:32 Also, I like in this change that it is very, like, internal. We are not changing an external API, which makes it very, you know, safe, and it just works for existing users.
**Tyler Yahn** 15:09 Yeah, okay.
… Yeah, I think, honestly, I think… I mean, I think this is ready to go forward. Obviously, like, there's some things we need to fix. I don't know what to do about this panic.
… I don't know.
Like, this is for the default case, when it's trying to hash key values, and … it doesn't know the type. I, like, you can't do any logging here, because of, like, an import cycle.
… At least that's what I wrote. I don't know if that's still the case. This might have changed its location, so….
**David Ashpole** 15:53 could we just do nothing? Or I guess we could hotel.handle?
**Tyler Yahn** 15:58 Well, if there's an import cycle for logging, there's gonna be an import cycle for the hotel handle as well, I'm guessing, but… Oh, right, there absolutely is, because, like, yeah, internal is going to import the attributes package, that's why, so, yeah, okay.
… Yeah, so I don't know, I… Doing nothing also seems, like.
not great, but on the scale of panic to do nothing, like, I'm not exactly sure which one's worse. Like, in theory, we should be able to catch the panic before we release it, but… That would mean that we're, like, exercising each one of these test cases in… or these cases in a test, and I don't, like, I don't know how to do that, like… dynamically. I think it's just one of those things that if you forget to update this test case, you're likely going to forget to update that test as well.
So, I… yeah, I'm open to suggestions, I'm open to just leaving it, I just wanted to make sure we document that we're thinking about it.
**David Ashpole** 16:54 One of those, like, impossible in theory.
**Robert Pająk** 16:56 Yes, for me, it's just, like, almost defensive programming, it should never happen.
For me, panic is kind of acceptable in this scenario.
**Tyler Yahn** 17:08 Yeah, and I mean, I guess if that's also the case and we do release it, like, that's a quick turnaround of, like, let's add that other test case, so… maybe just leave the panic.
… This… do some fuzz testing, I think that was just a general comment, I don't know if it's, like.
Critical, … this bug needs to get fixed.
I think, other than that, like, I didn't see too much else.
That's holding this back from….
**David Ashpole** 17:42 I did have a question, it's kind of weird, like, asking questions about a PR that I put up, but… for the… what are they called? The separator?
Unt64s, I think those were listed somewhere.
**Tyler Yahn** 17:57 Yeah, I think I saw the exact question you're about to ask, but yeah, go ahead.
**David Ashpole** 18:01 Can't someone… Is it possible for collisions if people have any of those strings?
In their keys?
**Tyler Yahn** 18:12 … no.
I thought about this as well.
but I might, like, no… but I may be wrong, so don't, don't, like, double-check what I'm saying here, but, like.
The idea is that, like, this is inserted in between a type, right? So if you… if you try to, like, put a string type that has this value here, right? Like, then this is going to be inserted before this, right? Or this is going to be inserted, and then this is going to be… so it's like, it'll always be doubled if the user is trying to input it, is the idea.
Is, is… If I remember correctly, how this is done.
So, so no, I don't think that it's possible, unless… there's a… payload that I'm… missing.
**David Ashpole** 18:58 I think Prometheus… the only thing I… the main reason I asked the question is Prometheus has, like, invalid… They also don't have the problem of actually needing to record Types at all, because it's all string, but they have, like, an invalid string that they've converted to an int.
like… backslash, backslash B, or whatever.
And they've got a list of those.
So, if we needed to, we could do something like that. I don't have any problem with these, as long as… we should probably document why We are certain that there's no… Possibility of collision.
**Tyler Yahn** 19:37 Yeah, certain… I don't know if I'd say certain. I have a strong, strong… I've thought about it a little bit, I guess, is what I would say, but yeah.
Yeah.
**David Ashpole** 19:49 But yeah, I think that that's worth….
**Tyler Yahn** 19:50 Like, taking a look at, at least, yeah.
But yeah, I think more review as well is just needed. But yeah, I don't see why this can't move out of being a draft, because I think we want to move forward in going in this direction.
I think it's a great, performance improvement, for sure.
Are you gonna be around, David? I remember you were taking vacation time.
**David Ashpole** 20:14 Yeah, so I'm on leave until September 8th, but I've been spending 30 minutes a day On various fun projects.
So, like, I… if… If someone else is like, wow, this is so important, it needs to land in a week.
or, like, Tyler, if you want to pick this back up, because you were the original author, like, that's totally fine by me. Otherwise, I'll probably get it done a month from now.
**Tyler Yahn** 20:41 Yeah, I mean, I might… I definitely want to try to get a release out before we really focus on this, but I think trying to get this in the next release seems totally reasonable.
**David Ashpole** 20:50 Sure. Well, I can keep, puttering along then, and if somebody wants to take over, that's fine.
**Tyler Yahn** 20:56 Okay.
Yeah, cool. That sounds great, then.
Okay, anything else you wanted to mention on this one, David?
I'm trying to think what was else.
**David Ashpole** 21:07 Feature gate? Sounds like no.
**Tyler Yahn** 21:11 Yeah, I don't think so. Like, I mean, I… I think it's, like… It's a performance improvement, like, if there are bugs, like, I think we could fix those with bugs, but I think it's one of those things that we should just… Fall forward on.
**David Ashpole** 21:28 Great.
**Tyler Yahn** 21:29 Okay.
Yeah.
Okay, next up, I wanted to talk about the release, the auto transportation is waiting on a release from us as well, so, and the EBPF transportation, would be great, mostly for the contrib things, in the auto-detect, but… Yeah, okay, this, I think, if I remember correctly, is waiting on me for a review, … or… It's waiting on everybody for a review. I don't think this has been reviewed, so this… Probably doesn't need to be blocking the release.
Given it hasn't, been reviewed, so… I don't know if that's actually blocking.
This, I think, is the more blogging one. There is a… … PR for this.
Yeah, that should be in this milestone.
… Oops, sorry, wrong thing.
Oh, there it is.
So this, I think, … What is going on?
Still needs to get, iterated on.
**Robert Pająk** 22:43 So… So, I think that, Taylor.
You can adopt the documentation changes that, you know, just put it in.
And I think we… you can just make changes on the PR. The thing is that we have holidays in Poland tomorrow, so Yevgeny will for sure not apply any changes unless he's working on holidays. And also, yeah, I'm not sure what is his plan for next week. And also, these are, like, I… I'm sure that he will not be any mad if we just, you know, apply these documentation changes. I'm 100% sure. If… maybe 99, you're never 100% sure.
**Tyler Yahn** 23:22 Oh, like, … apply, like, directly to this PR, is what you mean?
**Robert Pająk** 23:26 Exactly, exactly, or if you have some preference, you want to add something more, you know, just… just do it, and if you want, just to make sure that, Evgeny is finding it, we can maybe wait until Monday, just to double-check with him.
I think it will speed up a lot.
the process.
**Tyler Yahn** 23:49 Okay.
Yeah.
Alright, I'll take another look then, because he's not going to be in tomorrow, so… Alright, that's good to know, because that's, I think, really the last thing that's blocking this… milestone. Like, this is not really a hard blocker, this is, I think, something we want.
because we're releasing this as well, we want to get this fully over the line. Why is this 4 out of 6?
What else is left?
… What is this?
Is this… hmm… … This is… A part of the stabilization?
**Robert Pająk** 24:44 It doesn't have to be here.
**Tyler Yahn** 24:47 Okay.
**Robert Pająk** 24:48 It can be… the parents can be removed, I think.
**Tyler Yahn** 24:53 Oh, right, because this has something to do with more about, like, Yeah, okay.
Let's put this in the next milestone.
And then we can remove this….
**Robert Pająk** 25:10 I think the reason is that in Rust, they made it differently. I think they're making some pulls in Rust based on cardinality limits.
**Tyler Yahn** 25:20 Oh, really?
**Robert Pająk** 25:20 Yeah.
**Tyler Yahn** 25:21 Okay.
**Robert Pająk** 25:21 Yeah, I think they're just… yeah, I think they're just… I think they're using some pools, and that's why… Well, I….
**Tyler Yahn** 25:28 Yeah, I mean, it's definitely different in the book.
**Robert Pająk** 25:30 possible. Yeah, I think it's just a possible, maybe, performance improvement. It may be very also language-specific, so yeah, it shouldn't be a blocker at all.
**Tyler Yahn** 25:41 I… yeah, I mean, but this also goes back to the other thing, like, I think this has got to do with, like, the collection limit versus the cardinality limit, right? Like, that's.
**Robert Pająk** 25:47 Yes. No problem. Yes.
Yes. And, like, we, we….
**Tyler Yahn** 25:51 Yeah, we allow you to collect more than the cardinality, or vice versa, right, is the idea, and like, so… that… that may not be what you want to do, just based on the way we do the filtering, so I… yeah, I think that that's something… We can take a look at that after this is stabilized as well, because I don't think that these are… the API that's being introduced here is going to block that change. It would be an additional API, is what we talked about, so yeah.
Okay.
… Then, let's take a look at the contribib milestone… Oh, yeah.
I forgot about this one. This… I can get a PR up for this, actually.
Yeah.
Yeah, I mean, I can get a PR up for this if people are, in favor of it. That sounds good to me. We can try to get this resolved. Especially if, if Jenny is not until Monday, I'll try to get something up for this.
But yeah, okay. Otherwise, I think we're pretty good, like, this is being addressed, this is the last major thing, this can get bumped to the next, … let's just actually… let's just bump that, … Sometimes GitHub lets you do things, and sometimes it doesn't. It's a, like… confusing.
… there we go, okay.
Cool.
So yeah, I think that we're pretty good on this. Anything else that people are… Think that needs to get added to these milestones that's missing?
We got the upgrade to support 125 in Go, which is important into this release for both OTEL and Contrib. So, next release, we can remove this 123 support.
**Owen Williams (he/she)** 27:39 I mean, I guess there's the question of the translation PR, if that's something I'm not sure if that's too big of a change to go into this one.
**Tyler Yahn** 27:52 Yeah, well….
**Owen Williams (he/she)** 27:54 We do have a specific person who is, you know, when is this gonna get fixed? Which is, of course, what everybody does, but, yeah, I don't wanna… I don't wanna put it in if people think it's a little too disruptive, but if it can go in, then why not?
**Tyler Yahn** 28:10 Yeah, yeah, sure. Let's take a look at it. This is the PR, I'm guessing, right?
**Owen Williams (he/she)** 28:15 Yep.
**Tyler Yahn** 28:16 Okay, cool.
Yeah.
**Owen Williams (he/she)** 28:23 So, yeah, it's mostly ready to go if my reading of the reviews is accurate, and it's just… we're just sort of cleaning up comments, and then Robert, I was just trying to understand, yeah, which direction we wanted to go for the… the value to put in for the option, whether it should take a string, or an int, or the typed value.
**Robert Pająk** 28:55 For sure, it should be a type value, I'm just not sure if we want to have our own type value and map it, or we want to use the OTLP… not… yes, OLP.
OTLP translate directly.
That's the… that's my concern, and I do not say I have a strong preference, I just want to discuss and, you know, have opinions, yeah.
**Owen Williams (he/she)** 29:22 I mean, in general, the intent of the translator library is to have sort of a unified face for each of the user… of the, you know, projects that's using it. I think… Mimir might be doing something similar, where they have their own equivalent, enum… list. … But… is the worry… yeah, I guess I'm… what does having a parallel list get you, rather than using it directly? Like….
**Tyler Yahn** 30:03 Well, I think it's just that, like, any sort of changes to this type are external to this package, so coupling this package to that external package means that, like.
an upgrade here would change the behavior in this package. So an upgrade of the OTLP translator package, or a change in the OTLP translator package, changes the behavior within this, and it may change it in a very… breaking way. So say, like, you add a new option and we don't support it here, like, how does that get handled, I guess? Obviously, I think we're passing this back to the OTLP translator, but, like.
to Robert's point, like, we've done this before, where we… are using, like, our… even OTLP, like, in our exporters, in, like, the protobuf representation, and we've used… we've exported that in a, like, an option type before, and it has, like… it couples the packages in a way where, like, version mismatch all of a sudden becomes very problematic. Yeah.
**Owen Williams (he/she)** 30:57 I mean, the… Put it this way, if we want to add a little shim in between, that seems okay.
currently, OTW Translator's basically gonna be done. It's implemented based on specifications that we've written up for Prometheus and then OTEL, so any change to that interface will already require updating those specs, and then having to change all the downstream SDKs and callers, so it's like, this stuff is getting ossified really quickly anyway, so I'd put the chances of a change in a new translation option at very small anyway.
… it already contains the two most important ones, which is the, you know, Prometheus-style thing with suffixes and the… the no translation option, those are the sort of two big ones. … Yeah, I don't wanna… I never say never, of course. And if it's just… if this is something that buys peace of mind, it's a… it's a tiny function that'll be a shim, it does not seem like a huge, … a huge problem to me. It's… So, yeah.
**Robert Pająk** 32:06 I think I have written it to you, just on Slack.
I have not… because today I was very little low on time, I haven't checked exactly, you know, how this OTLP translate is used right now, but I think it's used in, I don't know, one or two places for, translating the meter, no, the instrument name, like, instrument name, or, you know, metric name, and unit name, right? It basically does those two things.
I was just thinking that maybe in… even to decrease the coupling, even to, you know, reduce this kind of… not even to have these options.
maybe put up some interface which just says, you know, you have some input, it returns you the string. The worry which I have is I don't know what the arguments will be needed to create the meter and unit name. I haven't checked that thing.
Because then it will need to be exposed, this input. Right now, it's not, right? It's being internal.
… Yeah, so….
**Owen Williams (he/she)** 33:10 So yeah, the history of the library is basically both Prometheus and OpenTelemetry had kind of a fork of the same code to do name translation, and this is for metric and label names. And they opt… they were different, and so this, package was created to match the existing API, And then provide a unified way to do it so everybody's calling the same code, and names get translated the same way both places.
Because that was… there were problems where, you know, do you remove duplicate underscores or not? And it was… they were not acting the same.
… at this point, it's not super feasible to change the API of this, because it's depended on, by now, like, 4 different packages that expect a certain The idea was to be as minimal as possible, and having this just be a drop-in replacement.
And that sort of helps people be confident that it would, … We've already had problems, you know, messing up people's metric names, and the whole idea is to make sure that that doesn't happen anymore.
Yeah, so changing, kind of, changing, sort of, the way that the….
**Robert Pająk** 34:27 I do not… I do not say meaning changing the OTLP translate at all. I'm just thinking about the way, how the strategy is selected.
So, for instance.
**Owen Williams (he/she)** 34:39 Okay.
**Robert Pająk** 34:39 the user may pass a function which basically then calls, for example, you know, this configured OTLP translator function, or whatever. And I do not say that it's, you know.
is a good choice, I just think it's probably worth exploring. The only thing which I… so, for sure, the output is the string, is the meter name, right?
I'm just not sure what are all the possible inputs.
Probably, if it's a struct.
then we could always add, you know, new fields to this kind of interface. So, for instance, you have an interface, like, I don't know, just translator, or meter… sorry, meter translator, meter namer, whatever. It can accept, you know, a struct, which will have the fields which are required by OTLP translator.
And we'll output the name.
And then people can basically, you know, put everything, any function which OTLP Translate basically uses.
And it could even decouple completely the code from the OTP translator, almost. People could, you know, even add their own translating functions if they need, for any reason. I do not say it's great, I just think it's worth exploring.
Because it will completely decouple the libraries, and then you could, you know, just rely on the documentation of what TLP translate, etc.
**Owen Williams (he/she)** 35:57 The, the, the main, … Yeah, so mainly right now, the exporter has a struct, and the main configuration is these Booleans without units, without counter surfaces, and then there's a UTF-8, … option somewhere. … And then the metric namer, label namer, unit namer, those are sort of instantiated to prevent making new objects every single time you want to make a name.
just because that would be… they're always going to be the same, they're basically… they're also a simple set of structs with the same… essentially the same set of bools. … And so it's really just a minimal amount of, state, and we just… because this is a fairly hot path, we didn't want to say, you know, new metric namer every single time. And then just copying in the same bools every single time.
So those are kind of cached, in other words. But yeah, exporter.go is where everything is sort of happening, and it's… it already had these Booleans for how to do the name translation.
And the translation strategy… basically, when you set the translation strategy, it just initializes those existing bools.
… And then… The… the stuff that happened with, like, … the translation library itself, it's basically where it's called in the exporter every time it needs a name. It calls the namer to get, you know, either it'll return the same name, or it'll return an altered name, depending on the strategy selected.
I… I don't know if that made a lot of sense.
It's, yeah, it's something where things are kind of done on demand, Which is… You could argue whether that's great or not, like, to be doing this computation every single time you want to generate a name on every single scrape, … I think there's a… there… we had explored some things in Prometheus for, like, pre-caching the translated names.
And you quickly run into problems of what if somebody changes the configuration.
With… and then the other… the other big issue was with content negotiation. Content negotiation could ask for one name or the other name.
And it just became really… Gross, really quickly.
So, yeah, we are… there is a concern of the sort of runtime implications of continually replacing dots with underscores every single time. … That's a little out of scope, because that's what it's already doing.
… I don't think it's doing it any worse.
Yeah.
**Yordis Prieto** 38:59 Hey, Oren, can you swap that component? I'm not too familiar, I'm just interested in the conversation.
So, you mentioned you don't want to break people, the, you know, naming, stuff like that? Yep. But I wonder if there is, like, a simple path of, like, okay, I can swap the… That translation as a whole.
The whole policy, so… If I want to pay the cost of performance, okay, make one that don't do that.
Or if you want to break changes, by all means, just rub your component in that layer.
**Owen Williams (he/she)** 39:27 Yeah, I mean, part of the thing that was happening was because there was inconsistency in how translation was done, fixing bugs caused breakage of names, and we have to do that one more time. This is the thing where the new default is this UTF-8 with Suffixes, which is a format that basically nobody wants, but that is what the thing is producing right now, so we're doing that right now, and then we're gonna switch it with a lot of notifications so people understand what's happening.
… as far as… yeah, the performance hit, if you've got UTF-8 no suffixes mode, it's a very fast, it does nothing.
If you're doing Prometheus mode, it does have to do that work.
And like I said, that was… that was what… that's what it was doing originally. This is, … It's not really changing that part of things.
… Yeah, I don't know if… like, it would take a pretty… it would take… a lot of work to go through and figure out, okay, if somebody's in Prometheus mode.
Is it we, you know, Pre… pre-escape things at… initialization time, or cache those somehow. Like, that might work for this component. That was problematic for Prometheus, but, like, that could work here. But that's sort of… that's sort of out of scope of the thing we were doing. We were just trying to say, okay, let's take this existing code and let's make it Shared so that everybody's doing the same thing, without trying not to touch the… architecture of how it's being done. So it was really just trying to drop in one-for-one function replacements.
And I think… I think that sort of brought attention to this code that people had not really been paying attention to.
**Tyler Yahn** 41:42 Robert, anything to say on that?
**Robert Pająk** 41:47 So, yeah, I do not have any… like, first of all, I think this library is great, and it's needed. For sure, it needs to be used internally.
So I'm not still sure if we should expose these options, you know, in our APIs or not. I think that's… that's the main thing for me, and if we… I think, Tyler, you have the same opinion, right? That it's better to have this kind of our options, or are you not sure as well?
That would be my first guest preference, probably. But….
**Tyler Yahn** 42:15 … if it's, like, stabilized, like, I mean, like, … I don't know. Like, there's definitely cases where, like, it makes sense to just take, like, a very known standard, so if, like, the OTP translator is, like, standardized, and it's, like, stable, then I don't see, like, too much of a problem.
But, ….
**Robert Pająk** 42:36 I'm more concerned about the V2, because I don't think we'll make a stable risk of the Prometheus exporter if OTLP translate is not stable.
Do not make no breaking change… breaking changes, so I'm more concerned about the future and V2 releases, and maybe… having as part of check… being part of the V1 stabilization of OTLP transport, because right now, even though, Owen, you say that there should nothing come more, because it's in the specification. We know with Tyler from experience that after a few months or years, people will want to have new things in Idotal Prometheus, Autel, there'll be some new concept, you know, we have, for example, a scope, we have some stuff, maybe there'll be a new concept which will require new kind of translations. So, yeah, that's… where I would probably prefer to have the APIs as much easy to extend as possible, and for instance, use, you know, structs and fields as many places as possible, and not use, you know, just fixed-sized arguments, because we name, especially that the OTLP translate is something that normal users will not use. We expect that it will be used by, you know.
by collector, by, by collector, by us, Autel Prometus Exporter. I do not think we… I don't think it's a normal user, you know, and library should be normally used by others.
by each, you know, application developer, or am I wrong?
**Owen Williams (he/she)** 44:10 So, yeah, okay, so, no, and I, yeah, and I'm happy, I guess, I guess, yeah, I'm, I'm happy to put the, the sort of intermediate type in between. That's… that seems fine to me. It's… it's… you know, it's cheap, it's easy to do.
**Robert Pająk** 44:24 I say that it may not be needed with Tyler. I think we may not need this type, just change the OTLP translator to make sure that we'll be able to extend it anyway.
for instance, when I looked at the meter, meter, I think it was called Metric nammer? Yes, meter nammer or metric namer. Yep. To be honest, after this kind of redesigns we did, I'm not sure why this strategy haven't become a field in success of these new suffixes and, … Like, you have added this new metric name.
Instead of changing the existing fields, which I do not really understand why it went that way.
**Owen Williams (he/she)** 45:07 Yeah, so I'm not….
**Robert Pająk** 45:08 two possibilities to, you know, kind of con… kind of construct this new meter… num-meter name, right?
**Owen Williams (he/she)** 45:14 Could you… yeah, could you… can you point me to what you're looking at specifically? Yes, I can share.
**Robert Pająk** 45:20 Sure, I can share my screen, because I think.
**Owen Williams (he/she)** 45:22 I was gonna… I was just gonna say that, like, I think it's… I think it's fair to say that the translation strategies will not change function given a specific string. So, like, we're not gonna… if somebody wanted a new strategy, that would be a new string.
we're not gonna do anything where, oh, underscores with escaping suddenly mean something different. So I think that they're stable in that sense, but yeah, let me take a look at what you're looking at.
**Robert Pająk** 45:50 So, this is one way of… creating a meter name? Yep. It's using this.
**Owen Williams (he/she)** 45:57 Yep.
**Robert Pająk** 45:57 And the other is using this.
**Owen Williams (he/she)** 46:01 Okay.
**Robert Pająk** 46:02 So, for instance, why we do not have only, you know, for instance, only the trans… only this translation, for example, strategy option, instead of these two fields.
**Owen Williams (he/she)** 46:14 Got it. I think, yeah, I mean… Historical reasons, because the way that the translation code was written… ….
**Robert Pająk** 46:26 And the thing is that….
**Owen Williams (he/she)** 46:27 Here's the answer. Here's the answer, yeah. So if you look at the translation strategy options, Where that will be, it's probably Strategy.go, … So, we have these four options, and then these two functions are the helpful ones. It is… It requires a bunch of if statements to know whether or not you should be, you know, adding suffixes, or… translating to underscores, just based on the name. And certainly… and it would be a waste of CPU, I think, to… store a string, and then continually have to say, do I need to add escaping, do I need to do suffixes?
Every single time, rather than… So the metric namer just sort of stores that… quick state, and then it becomes a very quick… you just check the bool and do the thing. So if you go back to Metric Namer, ….
**Robert Pająk** 47:35 Okay, so there are other ways how to do it. You can do it in sync once, for instance.
**Owen Williams (he/she)** 47:42 Sure.
**Robert Pająk** 47:43 you can… But yeah, I understand your point.
**Owen Williams (he/she)** 47:48 Yeah, so yes, the metric namer did not necessarily need to be… yeah, a struct with those… yeah, when we're just caching those.
**Robert Pająk** 48:01 I mean, I mean, these both could be, you know, these both could be, you know, unexported, and this field could be only exported, just to limit the possibilities, you know, just have one way to create this metric number.
And I think these are the things which, if we want to have a direct dependency on the OTLP translator, I think these are the important things that both the collector and we, especially we, because it will be part of our external API, we need to take a look.
**Owen Williams (he/she)** 48:33 So, so I totally agree that the metric namer fields should have been unexported. I think that's completely right.
… you should be just… you should just have New Metric Namer, yeah, I think that's… Correct. There's no good reason to have those be public.
… yeah.
And I think… You know, it would be… we could try, you know, we could try changing that, and hopefully nobody's depending on that. But I think it's important to note that, at least currently the OTEL Go… Code is not… I don't think it's… relying on those. I don't think it's… I don't think it's accessing those exported boules.
… We, I, yeah, we try to… we try to set strategy, and then we try to call should… should escape and should add, and should add suffixes.
Because, yeah, in the… in OTEL Go, we only use the translation hold on, metric random.
**Robert Pająk** 49:51 Yes, right now, from the export API, we have only.
**Owen Williams (he/she)** 49:54 Okay, yeah, it does create them.
**Robert Pająk** 49:56 But internally, it uses this new meter, etc. So, for instance….
**Owen Williams (he/she)** 50:02 Yeah, I can….
**Robert Pająk** 50:03 Probably will still have breaking changes, that's what I assume.
**Owen Williams (he/she)** 50:06 So I could… yeah, so I could… right, okay, so here's the… here's the reason why I did that. Because… This is why… okay, yes. Okay, now I'm remembering. So, okay, the current config in OTelGo is this config struct that has these bools already, and that is… we can't change it, because the specification is locked in. We're not… we can't… ….
**Robert Pająk** 50:35 It's… it's not.
**Owen Williams (he/she)** 50:37 So, we had this meeting earlier this week. The collector is stable, so we can't change how the collector's configured, so although the specification can change.
We can't remove support for existing configurations, so the existing without units and without color stuff….
**Robert Pająk** 51:00 You mean the… you mean the Prometheus exporter is stable?
**Owen Williams (he/she)** 51:04 Yeah, the… We had this meeting earlier this week. Ba-ba-ba-bum… We're in the specification SIG… the declarative… Greetings.
**Robert Pająk** 51:23 For sure, in declarative contract, it's part of development.
Right. It's not stable.
**Owen Williams (he/she)** 51:30 But, so I'm looking at these, notes. … although the Prometheus exporter is not stable, configuration is considered… locked in. Once you add a configuration option, you can't remove it. They were pretty… This, this.
Yeah.
So… okay, so anyway, what happened was, if you try to store the strategy in the configuration struct, then you've got two things storing the same… you've got two conflicting sources of configuration. You've got the without units boolean, and you've got a translation strategy, thing, and those could be out of sync. And now you've got two things.
So….
**Tyler Yahn** 52:23 But the takeaway from that in the configuration, like, declarative configuration, is that the newer thing takes precedence.
**Owen Williams (he/she)** 52:30 So, okay, so we could have the collector… Or, er, sorry, we could have the config struct take a… Translation strategy, could have us translation strategy member, and then when we run… When we run new exporter… okay, so then that's… We have the config, so then we've got to have some switches that say, okay, if you've got the translation strategy, then do that.
And then if you don't, you have to sort of, ….
**Tyler Yahn** 53:10 You would fall back to the old way. But the thing is, is, like, the idea being that, like.
The collector is stable, right, and it's accepting a non-stable….
**Robert Pająk** 53:18 It's not. I have checked, it's not stable. It's better.
Somebody was wrong somewhere. Yeah, right now I checked, the Prometus Exporter in Collector is beta.
**Tyler Yahn** 53:30 Well, I… yeah, that also may be… … more controversial than… than… a black and white issue. I think, okay.
**Owen Williams (he/she)** 53:39 So I think, yeah, what I'm hearing is, okay, we add, you know, translation strategy becomes the thing that we set in the config, and then when we create a new exporter, we first look to see if there is a translation strategy. If there is, we use that. If there's not, then we fall back to the bools that already exist.
And use that. … I think… so, the only trickiness there is… which default… the UTF-8 default stuff. I think I can figure that out, though.
… Alright.
Okay.
Well….
**Tyler Yahn** 54:26 ….
**Owen Williams (he/she)** 54:26 I'm out until Tuesday next week, so this is gonna be a next week problem.
**Tyler Yahn** 54:32 Okay.
I think on that one, first off, let me just say thanks, Owen, for tackling this, because you're… you're spanning not only different CNCF projects, but also, like, within internal OTEL, a lot of different SIGs, so I appreciate you taking the effort to make this work, because it's affecting users.
I think that since you're gonna be out till next Tuesday before you address this, we'll probably leave this out of the next release. I am hoping the next release to be a little faster than this previous one, so I imagine once this gets in, we could probably get this out pretty quick. In fact, we could probably prioritize making something with this change.
**Owen Williams (he/she)** 55:06 Cool.
**Tyler Yahn** 55:06 So… Yeah, I don't think that should be too much of a worry, but yeah, let's wait until we get those changes in.
**Owen Williams (he/she)** 55:14 Okay.
**Tyler Yahn** 55:15 Okay.
**Owen Williams (he/she)** 55:15 … Yeah, last thing I'll say is, yeah, this version will establish a bad default, and we have some text describing what people should do to make a good default, to have a good experience, and then we will want to break everybody's metrics by default in the next one, with the final understood, default of underscores with suffixes, and I just want to make sure that we announce that as loudly as possible, because every time We do these things, everybody gets mad. We at least want people to see that the thing is changing.
… Yeah, the thing that's right now that's been happening… has anybody ever heard of Knative?
I've never heard of Knative, but they just switched to OTELGO for, making their internal metrics, and they are broken because of all this stuff, and so we have a big customer that's all mad at us and wants us to be… fix everything yesterday.
that should not make us rush anything out the door. All I'm saying is that there are eyes on this thing, and I want to try to make people happy if I can.
And I'm also hoping to get to a place where things are much more calm, and there is a lot less of this uncertainty and instability. I look forward to finally having things a little more… a little more calm around making metric names. So, thank you for your patience there.
**Tyler Yahn** 56:39 Yeah, no worries. Like, like you're saying, there's nothing ever so bad you can't make it worse, right?
**Owen Williams (he/she)** 56:43 It's not….
**Tyler Yahn** 56:44 Copy that.
… Jordis, I see you have your hand up. Any last comment before we move on?
**Yordis Prieto** 56:51 Yeah, yeah. First of all, yeah, that sounds a lot of stress, dude. Goddamn.
Yeah, like, Robert mentioned something that I think, like, we started adopting it lately that is somewhat related to the topic, and it's, Most of these public APIs, we saw that on… You know, always the exact same signature of… if you have a context, first argument, and the second argument is in a struct.
And we return an instruct out.
But data structures have nothing to do with the domain.
of a given functionality was based on the function name, right? So, say, like, get user, then, I don't know, to make a point, get user return of results, or whatever. And the point is, no breaking changes. At the very least, you're gonna have the power to experiment.
And keep adding keys to it, right? Until, okay, this is too complex, okay, breaking change, but I give you the flexibility, but… Like, getting into the habit of struct in, struct out, that have nothing to do with the domain, but everything to do with the function.
And again, it was literally just a function name, command, function name, read model for us.
And the second thing related to that is that configurations start becoming actually a polymorphic thing, so we start versioning the configuration as well.
Sometimes you can do that, but, like, basically, you know, the arguments you pass in is, like, here's a V1, here's a V2, if you opt in for V2, you're gonna get this whole suite of, like, breaking changes, or, like, whatever, right? But… We start doing that as well, … Although the configuration is annoying, to be honest, especially making everything interfaces at that point, because of the lack of unit type, but… You know, that's food for thought.
**Owen Williams (he/she)** 58:34 Let's go for you.
**Tyler Yahn** 58:36 Cool. Alright, that sounds good. We have a minute left. I want to be respectful of people's time. Jordis, if you have more comments, please be sure to look at the PR that's in the docs, and definitely provide feedback there.
Okay, with that said then, we can end it here. Thanks, everyone, for joining, appreciate, everyone's time, all the feedback, and hopefully we'll, we'll keep making this, make this happen. Okay.
**Owen Williams (he/she)** 59:00 Cool, thank you.
**Tyler Yahn** 59:01 Talk to y'all later.
