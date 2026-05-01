SIG: Go SIG
Date: 2026-04-30
Duration: 54 minutes
============================================================

## Zoom Recording Transcript

**David Ashpole** 00:18 Take.
**Tyler** 00:22 Hey, dude.
How's it going?
**David Ashpole** 00:31 It's going well.
I spent way too much time prototyping random stuff this week.
**Tyler** 00:40 Yeah. I've spent a day and a half writing, registries in Java, so, yeah.
**Pellared** 00:51 Cheers!
**Tyler** 00:52 You know the feeling.
**Pellared** 00:53 for you? Yeah.
Hey, Robert.
**Tyler** 01:06 Yeah. Where are we at? I think we're… 2 minutes in? Okay, cool.
Yeah, so, welcome everyone. If you haven't yet, go ahead and add your name to the attendees list, and, if you have agenda items you wanted to talk about, go ahead and add them there as well, and I'll… Start sharing my screen here in just a second, we can get started.
**David Ashpole** 01:37 Robert, should I put agenda items above yours?
Or do you want to talk about the release first?
**Pellared** 01:47 I have to unmute myself, feel free to put above yours.
**David Ashpole** 01:54 Okay, that's what I thought.
**Tyler** 02:58 Cool. David, do you want to talk about this?
Follow-up on your exemplary reservoir parallelism?
**David Ashpole** 03:09 Yes, I just wanted to… I haven't decided what I want to do yet, but basically, where we ended last week was, was with… this… was with the idea that I was going to implement something that did an initial fill of all the Buckets, right? And then did random assignment after that.
But still use the sharded model, right? So that was, like, the thing I was gonna try and implement.
I was able to implement it. It was… It's a tiny bit slower, but not meaningfully. The main issue is that it actually turns out not to be… Time unbiased anymore, because once you have Different numbers of exemplars that can be… Randomly given… like, one bucket can get offered a lot more exemplars than another, and actually it skews… if they don't have exactly the same number, it ends up skewing The time unbiasedness of the algorithm.
to favor later, to favor it being more likely to record. So if you scroll up to the previous comment… The easy way to think about it is that, like.
the probability of keeping it exemplar, if… You have two buckets.
And each one has received 5 previous offer calls.
is… High or is lower than if you have two buckets which have received 4 and 6 offer calls previously.
So basically.
Unless you have an even bucket spread, you can't do random assignment and use individual copies of Algorithm L.
There are other out… there are other algorithms that do this in a distributed way.
The way that they do it is they start with way more buckets than they need.
And then during collect, You wait which… you, like, let's say instead of 2 buckets, you actually recorded 4.
And then, afterwards, you can down… like, sort of downsample the number of buckets you have, and do a weighting at that point, so that they… so that it becomes time unbiased again.
But I don't think that makes sense for us here. So, the TLDR is that we can't do random assignment and sharding together.
So our options are to either stick with what we have.
Which I think is actually a reasonable choice to make.
Given that, like, exemplars aren't… I know some people run with, like, always-on exemplar reservoirs, but I don't think it's actually that common. Or people do 100% tracing, but then maybe usually don't do metrics.
So maybe, like, the 300 nanoseconds for a reservoir call isn't that bad.
Or the other option is to do the round robining.
For the fixed size reservoir.
**Tyler** 06:14 What's the performance difference?
**David Ashpole** 06:17 Scroll up to the top.
So it's… It's, 60ish… 65%.
It's meaningfully better, but it's not.
Yeah, you know, it's like… 200 nanoseconds for a measure call.
On my machine, at least.
**Tyler** 06:44 When we were writing these, we originally… Like, even in the spec, decided that, like, it'd be ideal if people could provide their own implementations here.
Have we done that yet? Like, is it possible for a user to do that?
**David Ashpole** 06:57 Yeah, it's totally possible.
**Tyler** 07:00 So should we add, like, this other reservoir as, like, something in Contrib?
Or, or, or here, I'm just somewhere, like… Put it as the default, and then have it so that people can try it out first?
**David Ashpole** 07:17 Yeah, I think that's totally reasonable. I think we could even maybe just put it in an exemplar slash X Directory, like we have been doing.
**Tyler** 07:25 music.
**David Ashpole** 07:26 the easiest way.
Yeah, I'll have to copy the algorithm L… thing, but…
**Tyler** 07:34 Yeah.
**David Ashpole** 07:35 But, I mean, it's just… I can even template it if you want.
**Tyler** 07:39 No, please don't do that.
**David Ashpole** 07:40 Okay.
It's okay, we…
**Tyler** 07:44 We're ready.
**David Ashpole** 07:45 I only change this once a year when I find a bug from my previous year's change.
**Pellared** 07:50 Make a comment from where it was copied.
**David Ashpole** 07:54 Yeah.
**Tyler** 07:55 We're not crossing any package… we're not crossing module boundaries, right? It's just gonna be in a different package, or…
**David Ashpole** 08:00 Yeah, it's just a different… it's completely standalone. These things are pretty simple.
**Tyler** 08:06 Yeah, I would… yeah, just…
**David Ashpole** 08:08 Okay, I can do that. I'll take this PR, and I'll trim it down so that it only changes the histogram one.
I think the histogram change here is correct.
And it does actually save on performance as well.
So… For reference, this is, histogram reservoirs being time unbiased instead of being, like, last one wins.
**Tyler** 08:31 Oh, I'm sorry, so this is the histogram with an algorithm L, like, implemented in it?
**David Ashpole** 08:36 Yes, so that's why there's a performance benefit there, is because it's cheaper to not do anything.
**Tyler** 08:44 That's cheaper to not do anything?
**David Ashpole** 08:50 Sorry, so if… if the exemplar reservoir Each time a histogram.
**Tyler** 08:58 Oh, okay.
Yeah, yeah, okay, I gotcha.
**David Ashpole** 09:00 If you have to overwrite it every time, that's.
**Tyler** 09:02 more expensive.
**David Ashpole** 09:03 then… then…
**Tyler** 09:05 You're doing an operation every n times versus some random subset of that. Okay, I gotcha, yeah, okay, sorry.
Yeah.
I still have my first cup of coffee. Okay, I gotcha. Yeah, that sounds good.
**David Ashpole** 09:17 Okay. Well, I think that's an okay outcome. I… I'll think about whether to do the fixed-sized reservoir or not. I'm not sure it's worth the effort, unless somebody asks for it.
It's already well documented in these PRs. Do you think…
**Tyler** 09:36 I like the X idea, like… Yeah. Because, I mean, like, yeah, like, I hear what you're saying, like, it is… Unless somebody wants it, but the problem is that, like, if somebody wants it, and then… I don't know.
**David Ashpole** 09:51 Apart from me to find it.
**Tyler** 09:52 Yeah, like, yeah, if you're not around to, like, remember this, like, it's a lot easier if it's already published, and being like, okay, here you go, have you tried this out? Yeah.
**David Ashpole** 09:58 I guess, like.
In my mind, it seems likely that 3 years from now, it'll still be sitting in the X directory.
But maybe, maybe that's fine. Yeah, okay.
**Tyler** 10:08 And that maybe answers our question, you know? Like, yeah. Yeah.
**David Ashpole** 10:14 Alright.
**Tyler** 10:15 Cool.
Awesome. Okay.
Next up, Robert, you want to talk about the next release, the V1… 44.
There's a lot of opaque URLs here.
**Pellared** 10:29 Yeah, so maybe it will be easier for you to just click and check all those things, so, you know, these are filters already.
So, I would like to work on creating a release, next week. Tomorrow, I have a day, we have a holiday in Poland.
So I could work on Monday. I think the only blocking stuff is still the, is still Sam's PR.
From this, I don't think anything… it's blocking, unless David has these configuration options. I'm not sure if this one is not something that you would like to have addressed in this.
Migrate to new configuration options.
To have the, you know, To have the migration rolling faster.
I have not checked what is the status of this one. I'm guessing Arthur, maybe, or you may be, or you need, I'm not sure.
**David Ashpole** 11:24 deprecating them. Okay… I think they still need to be deprecated at the spec level.
**Pellared** 11:37 Okay.
**David Ashpole** 11:38 I don't think this can happen in this milestone. You can bump it to the next one.
**Pellared** 11:43 Okay.
So, everything.
**David Ashpole** 11:53 We are so close on SDK observability, it feels like.
**Tyler** 11:56 Yeah, we are.
Yeah.
**Pellared** 12:02 Next one…
**Tyler** 12:02 Ugh.
**Pellared** 12:03 Yours?
Getting this hyperlink.
Cool, son.
So here, the main blocker is Sam's PR. I added, Ash2K PR as well, but Copilot added some comments, so I don't think it shouldn't be a blocker, and I think these comments are also reasonable, but yeah, these are… close to be addressed for sums as well.
Or has co-pilot found the same thing as me?
**Tyler** 12:44 Yeah.
**Pellared** 12:46 Okay.
**Tyler** 12:48 Yeah.
Okay.
I haven't looked over this one again, either. Is this… Robert, you seem to be pretty active in this. Is this so close?
**Pellared** 12:59 Yes, it looks very close.
It was the only thing that I was able to catch by, like, yeah.
**Tyler** 13:10 Yeah.
**Pellared** 13:10 when I was reviewing, I just did it by myself, usually I also ask Codex to double check. This time, I was not looking at codecs, but I look at the diff, and it was reasonable, and here I see that, yeah, I see that there are similar things.
**Tyler** 13:25 Cool.
Sam, are you able to address this and handle the merge conflict?
**Sam Xie** 13:29 Yeah.
**Tyler** 13:31 Okay.
Cool.
And then this one, Robert?
**Pellared** 13:37 Yeah, this one was approved, like, today, by… just before the meeting, by me and David. I ran… I just… just in case I added Copilot, and yeah, of course, it sounds fine, things that we have thus far.
**Tyler** 13:49 Yeah.
**Pellared** 13:55 So, it's not a blocker, but I… think this is a good PR, because, It removes from the things which are in the… which are pulled, which should be res… like, reset anyway.
**Tyler** 14:10 This… this… this shouldn't be addressed in this PR. There's… this is… This is, like, a templating syntax.
**Pellared** 14:18 Really?
**Tyler** 14:18 This is not… yeah, because this is almost certainly coming from, semantic conventions.
And, like, the documents that they have there have this, pound sign in them.
And so, it's just, it's putting it in there. Like, so, to do that, you'd have to filter with the comment Jinja template?
and say, like, okay, take this out if you find this at the beginning of a sentence or something like that. Like, that's not… this is definitely not…
**Pellared** 14:43 you fixed it… so you fixed it, Heather, recently by yourself?
**Tyler** 14:49 I wrote the Jinja syntax, and, like, a ton of this stuff happens in semantic conventions. People write really bad descriptions and.
**Pellared** 14:57 No, I mean because… I mean because it was regenerated, I think, everything, and I think this was the only difference.
that, that was here. Like, if I looked at the other stuff, it was the only place when this prefix was added.
**Tyler** 15:11 Okay, so maybe it was, like, misgenerated, or it was edited after it was generated, is what.
**Pellared** 15:16 Yes, yes, that's my guess. Maybe it was, you know, just a mistake, you know, someone, a cat, just jumped on the keyboard.
Double-checking would be another misweek.
Maybe just double-check with some other one.
**Tyler** 15:32 Yeah, Where was it in the… Anyways, I guess I can find it.
**Pellared** 15:39 the one…
**Tyler** 15:41 So, yeah, it's just… it looks like you're probably right, then. It… it was just a… Oh, it didn't load this.
**Pellared** 15:47 That's.
**Tyler** 15:50 It really doesn't want to load.
I guess I can just look, yeah.
Yeah, it's gonna be super specific to that dock, though, right?
I mean, it's not gonna be another metric, it's gonna be… Of course.
**Pellared** 16:10 There's another one.
This is a new one. Same problem.
**Tyler** 16:14 Is it?
**Pellared** 16:16 This is good for this one.
**Tyler** 16:18 Oh, this is your comment.
**Pellared** 16:20 Okay, you have a different…
**Tyler** 16:24 Oh yeah, look, here's another one.
God.
Yeah, what?
I… that's weird, it's only this file.
Okay. I mean, it has to get addressed. I… Or at least figured out, maybe not addressed, I don't know why it would change like that.
The logical… this looks like it is coming from semantic conventions, though.
**Pellared** 16:55 Yes.
Yeah, so probably you're right.
**Tyler** 16:59 Yeah.
It may be that, like, they updated the semantic conventions, and that's why it's coming in. If that's the case, I would not address that in this PR, but if it… It's like an edit, then… yeah, that… sure, yeah, let's fix it.
**Pellared** 17:13 Sweet.
**Tyler** 17:16 I guess you can find this really easy.
**Pellared** 17:27 But usually, when you're regenerating semantic versions, are you not doing it against some target version?
**Tyler** 17:33 Yeah. The version changes, though. Like, the… so the… Mmm, oh, I see what you're saying. Like, the released version?
**Pellared** 17:42 Yep.
**Tyler** 17:42 Yeah, it should be tagged.
That's a good point.
Yeah, I don't know. Yeah, it's gotta get looked into.
We could try regenerating it, but that's probably a little too far.
Man…
**Pellared** 18:03 Or maybe the tooling that is used for regenerating is not pinned. I remember there's some Docker image.
That you are using.
Maybe you were just always using the latest?
**Tyler** 18:16 No, it's pinned.
**Pellared** 18:18 It's been…
**Tyler** 18:19 The… it's the Weaver image, and then, yeah.
**Pellared** 18:22 So.
**Tyler** 18:22 So, I don'.
**Pellared** 18:22 just using a newer Weaver image, and maybe… Could be.
**Tyler** 18:26 I don't know why that would be just on that one… That one file, though. Yeah.
**Pellared** 18:33 Yep.
**Tyler** 18:36 Okay.
Yeah, that's really weird. And then… Yeah, this kind of stuff definitely needs to get fixed.
This kind of stuff causes a lot of thrash in the generate versus the linting.
Yeah, alright.
Okay, cool, looks like, yeah.
So you've added this to the milestone, right?
Yeah.
What's next, Robert?
**Pellared** 19:16 The next one is the co-constrips issues.
I think it's empty.
Yep.
**Tyler** 19:30 Yep.
**Pellared** 19:33 Next one, our pool… the executive request, right? Okay. So this is the one… And I think I blocked it.
And I can review it again.
I'm not sure why it's not merged, maybe it was just waiting for me. So, I'll… I will for sure take a look, and I will decide if it's… if it's very closed, or… there are some conflicts back I handle myself, but if it's just some conflicts I can resolve myself, I will also… if I also have any doubts, I will also double-check with Damien, given it's auto-http.
**Tyler** 20:12 Yeah, it looks like it's just changelog semantics here, which… I just… as a maintainer, like, I think just… just push the changelog you want to see, I would say, yeah.
**Pellared** 20:23 Yeah.
**Tyler** 20:26 Okay.
Cool. That sounds good.
Okay. And then…
**Pellared** 20:36 I just had any issues, pull requests, issues, and open, maybe if we need to double-check if you are not missing anything.
Just to quickly, you know, just… Look at these latest ones, if there's nothing.
Important.
**Tyler** 21:08 Yeah, this map type is the next.
**Pellared** 21:10 Yep.
**Tyler** 21:11 It was…
**Pellared** 21:11 For the next milestone.
**Tyler** 21:29 attribute… panic in places that should be unreachable? Oh, this is, like, change this, okay, I gotcha.
**Pellared** 21:34 This is just a refactoring. I'm not sure if it's not… it's very subjective.
**Tyler** 21:40 Yeah.
**Pellared** 21:42 The question is if you want to report errors or panics for code which is unreachable, and do you have any preferences? So maybe I can ask you here.
**Tyler** 21:51 Is this a duplicate? What's going on here?
**Pellared** 21:53 No, the previous one, exporter. I think it was for exporters to handle.
**Tyler** 21:57 Oh.
**Pellared** 21:59 And this one is just to add the new type, just to make this appear a little bit smaller.
**Tyler** 22:04 Hmm. Okay.
What's this support new attributes type?
Just, like, a parent issue?
**Pellared** 22:14 or something? Yeah, exactly.
**Tyler** 22:15 Okay.
Okay.
Anything you need me to… Check off here?
**Pellared** 22:24 Nope.
Okay.
**Tyler** 22:28 And then… you wanted to look at the pull requests as well?
**Pellared** 22:31 Yeah, maybe David has something, which I think David has the most… biggest amount.
I see that… I think CGS can be also merged.
the document enabled.
**Tyler** 22:45 Sea Joe's, really?
**Pellared** 22:49 Yeah.
**Tyler** 22:51 What's CJ's username?
**Pellared** 22:55 C, I… J…
**Tyler** 22:57 Oh, there it is, okay, OCI, okay.
**Pellared** 22:59 You can… Thank you.
My gosh.
You know.
**Tyler** 23:08 Yeah, what…
**Pellared** 23:09 I detailed the milestone.
**Tyler** 23:12 Okay, yeah.
**Pellared** 23:14 Someone will forget about it.
Technical.
Repeat any… any of yours from you, from your side?
She said she would like to have immersed.
This is true.
**David Ashpole** 23:40 I don't think any of them have any reviews yet, so probably not if we're doing the release soon, soon.
I wanted to just list out… I know I've been opening a lot of stuff, so I wanted to just list out the ones that are ready.
There's… there's another one that's pretty simple.
the always-off filter.
**Pellared** 24:07 First, from top.
**Tyler** 24:09 This one? What?
**Pellared** 24:11 Optimized resources SDK.
**David Ashpole** 24:12 Yeah, so that one's pretty simple. If… It might be easy enough to get in.
It turns out, calling reservoir.offer Because it's an interface, it just carries, like, some overhead.
And so there's more we can do. It's similar to the previous one, where we can check to see if it's the always-off filter.
And this save… this is mostly noticeable in the pre-computed cases.
Because it actually represents a pretty… Sizable, portion of the… FastPath call overhead, if you're using an always-off.
Exemplar filter.
So you basically… Check it at the beginning, so that you don't have to make the function call every time.
**Tyler** 25:01 I see, yeah.
**David Ashpole** 25:04 But I don't care too much if this gets in or not.
**Tyler** 25:11 When are you trying to do the release, Robert?
**Pellared** 25:17 I thought about Monday.
Just think we can do this.
**Tyler** 25:22 Reviewed in 2 days.
Yeah, I'll add it.
**David Ashpole** 25:29 The rest of them are probably larger, and not… I don't think we'll be in by Monday.
**Tyler** 25:37 Okay.
Wow, some of these have… Quite a lot of… Okay.
**David Ashpole** 25:46 Yeah, co-pilot and I, we're best friends.
We just… about our lives.
**Tyler** 25:54 Yeah, I mean… So, it's the new thing, man.
PR's… PR's become just, therapy sessions at that point. So, dinkatrib?
Robert, what did we need to look at here?
**Pellared** 26:13 I didn't see anything myself. I remember that there was something, David, I saw that some issue regarding interceptors for OTL gRPC. I'm just a little…
**David Ashpole** 26:28 Yeah.
**Pellared** 26:29 Because I remember that we wanted to remove these interceptors and remove them. I do not remember what's the reason that the gRPC guys didn't want to have them, but yeah, so do they.
**David Ashpole** 26:40 It turns out you need both.
So the answer is actually.
Parts of the information that we need to satisfy the semantic conventions are accessible from interceptors.
And other parts of what we need to satisfy the semantic conventions are in the stats handler.
What you end up actually having to do.
Unfortunately, is have an interceptor that Get some of the… metadata from the gRPC request.
Puts it in the context, and then have your stats handler pull it.
And add it to your telemetry.
**Pellared** 27:17 But in such a case, doesn't it make sense to just have the interceptors?
**David Ashpole** 27:24 I thought there was other pieces we weren't able to get via interceptors, but I may be mistaken.
I… I… if that's… That's a good thing for me to look into.
**Pellared** 27:35 Maybe I'm wrong, but I think that the interceptors were… taken away, I just know it was some performance reasons, or something like that.
**David Ashpole** 27:43 Yes, yeah.
**Pellared** 27:45 And if you will be using it anyway, then, yeah, maybe also… create an issue in the GRPC, or even making PR, I… yeah, just… just lose ideas. I think you should not take this decision, you know, lightly. Yeah.
**David Ashpole** 28:01 Yeah, I agree. This is also what GRPC itself does for their OpenTelemetry, like, stats module.
That's… that's partially where it comes from. It's like, oh, this is how they decided to do it.
But I can look in and do due diligence to make sure that that's actually necessary.
**Pellared** 28:23 Okay, thanks.
**Tyler** 28:27 Does the hotel, or the gRPC OTEL library, like, provide semantic conventions, or is it not compliant?
**David Ashpole** 28:33 I think they did their own thing, but they only do metrics.
**Pellared** 28:38 Yes.
**Tyler** 28:41 Okay.
Alright, Robert, anything else on that one?
**Pellared** 28:49 No, that's all.
**Tyler** 28:51 Okay.
Alright, David, do you want to go back to metric SDK performance-related PRs that need review? Always off, we just talked about the With Unsafe Attributes Part 1.
**David Ashpole** 29:04 Yeah, so this, this we've discussed a bunch. This is just… I tried to split this off into multiple PRs, so this is mostly just boilerplate.
It defines the API, and then immediately converts the attributes you pass into a set.
And does the existing code path that the SDK already does.
So this won't have any, like, performance benefits yet. It's just… just adding the API and documenting it and stuff.
Yeah, so this is one PR that's… hopefully shouldn't be too hard to review.
Yeah.
**Tyler** 29:41 Okay.
This is just more about saying, like, how we want to implement the experimental things, which is what we talked about, so… yeah, okay.
Yeah, that makes sense. And this other one is optimized filters.
**David Ashpole** 29:54 Yeah, so this… If you remember.
I did the big proof of concept to show that we could get to zero allocations on the hot path.
When attributes aren't known ahead of time, right?
And it turns out we can actually just greatly improve the current API's performance when there's a filter present, using some of the same approaches. So… all this That what this basically does is that we… we take as input an attribute set and a filter, right? So, like, those are the two inputs to any… measurement we make in the SDK.
Right, because there's maybe a filter present, and you get an attribute set.
And it turns out that you incur a lot of the allocations.
when you… Either try and make a new attribute set, like, when you apply the filter to the set.
To either get the new subset, or to get your dropped attributes. So that's where two… two of the potential allocations come from.
And so… this PR basically defers computing the new… attribute set, and defers computing the dropped attributes, unless it's actually necessary, which If an attribute set is already present in the SDK, isn't actually necessary.
on the hot path, so… This… if you look at, like.
The benchmarks, especially in the case where you have a big attribute set.
To look at, like, The dynamic… one of the dynamic cases.
With 10 attributes.
Right, so you get rid of all your allocations, but also even just the runtime improves a lot. So some of them are, like.
Like, if you look there, 1448 nanoseconds down to, like, 400.
pretty good. The pre-computed cases are actually even wilder, because You go down to doing almost nothing, even when there's a filter present.
Because all you have to do is hash, instead of… Copy the attribute set.
Hmm.
**Tyler** 32:08 Yeah, I think I see what you're saying, but, like, so wait, when is it actually computed, then?
Like, when do you need to actually do this computation?
**David Ashpole** 32:16 When you add a new element in the sync.map. So when you first see an attribute set.
That's when you hit the slow path, and you have to actually… take your… take your initial set, apply the filter to get the new set, to store it in the map. Otherwise… We've already seen…
**Tyler** 32:39 the set, we already have a hash for it, and we've already applied the filter to it, so we know, don't do that operation again, and it's only when you're like, oh, here's a new set, now do that again, and like… so we're just storing, like, the hash and assuming that the filter's gonna be… Deterministic, and, like, it's gonna apply the same every single time.
**David Ashpole** 32:56 So this, if you look at the public API editions, this adds a set dot… this adds a way to get it distinct from an existing set while applying a filter, right?
New distinct with filter just computes the distinct.
For the attributes that are in a set.
And applies a filter.
And that basically lets you do the lookup without ever doing the full work of making the new set after the filter's applied.
**Tyler** 33:27 So… I hate to be that guy, but is it… is it… Always true that a filter is deterministic, like… Isn't a filter, like, a function that could be defined by a user?
I don't know how this is defined.
**David Ashpole** 34:05 I mean, I think a filter is not deterministic.
But I think that also, like.
Like, that also would break this, like, this function that you're actually on right now, like, where you can take a set and filter it and get a new set.
Like…
**Tyler** 34:25 Well…
**David Ashpole** 34:27 You would get a different… Like, in the existing code… code path?
We basically take a set, apply a filter to it to get the new set.
And then take the distinct from that.
And do the lookup.
Right.
**Tyler** 34:44 Yeah, but what I'm saying is, like, what if I have a dynamic filter? So, like, I've got some sort of dynamic config that I can push to my SDK, and so I've got it so it's like.
you know, tune up or tune down these attributes. Like, I don't want… I don't know, this high cardinality attribute, so I send… push… send some sort of, like, config down to my SDK. That SDK then takes that filter and it updates it in place. So now, if you call this setFilter operation.
It'll return a different set after some sort of point in time when that config has been updated.
**David Ashpole** 35:19 So I think that would still work here. Like, in that case, you would be taking a set we're not, like, hashing the filter function or anything, right? We're just…
**Tyler** 35:28 No, right.
**David Ashpole** 35:29 Skipping the step… we're just skipping the step of copying the data from the original set into a new set.
And we're insane.
**Tyler** 35:39 The thing is just, like, just…
**David Ashpole** 35:40 executing that. Batch.
**Tyler** 35:42 That wouldn't be true after that point in time, though.
**David Ashpole** 35:50 Sorry, what would that be true?
**Tyler** 35:52 So now, let's say I've, like, like, so at… So, so the… I've sent down that new config, that filter, is essentially dynamically updated.
That hash that we originally computed is not valid anymore.
**David Ashpole** 36:10 So I guess you're saying, like, our existing set design also isn't correct, right? Because we want.
**Tyler** 36:16 No, our existing… so our existing's fine, right? Because, like, it's… it's not… it's not computed lazily, right? So each time that it goes down, it computes that… that new attribute set, and it uses that new… attribute set for its computation, right? But, like, on the lazy design, it doesn't use the new attribute set, it just assumes the new attribute set is going to be the same as was computed before, so there's no point in trying to, like, recompute that, but there is if that's going to be a different Set, is the thing.
**David Ashpole** 36:49 Not entirely following, like…
**Tyler** 36:51 So, like, so, like, let's say… so time zero, right? Like, right at the start, you have a set that contains the keys A and B, right? Yep. So, you compute that on the startup, and you get your hash, right? So now, you don't do that filter any… you don't do that filter operation anymore, right? So… The next time you see a set with A and B, you just assume that it's gonna be the same output when you're on the filter, so just use the same hash that you did. Now, at some later time…
**David Ashpole** 37:14 Don't do that, yeah.
We don't assume anything about what you get when applying the filter. The filter function is applied For each call.
It's just, instead of producing a new set.
And then taking the distinct from the set, and doing a lookup on the distinct.
We just directly compute the distinct and do a lookup on that.
Right, so we're just…
**Tyler** 37:37 So you're saying… oh, so what you're saying is, like, after time T, when the filter changes, you will still be doing another hash call, and you'll get a new hash from that?
**David Ashpole** 37:46 Each call, yes. So we're still hashing on every single call, it's just that we're no longer doing the data copy. I see.
**Tyler** 37:53 Okay, alright.
**David Ashpole** 37:53 Set until… so we're deferring the data copy part of it.
**Tyler** 37:57 Yeah, yeah.
**David Ashpole** 37:57 We're not deferring… we're not eliminating, hashing the inputs.
**Tyler** 38:02 I see, so this will still, this will still handle that update of the filter, then, is what you'.
**David Ashpole** 38:05 Yes, yes.
**Tyler** 38:06 Okay.
Alright, yeah.
**David Ashpole** 38:08 Sorry, I thought you were saying that there's, like, a race between… We make this.
**Tyler** 38:13 No, no, no, no.
**David Ashpole** 38:13 And then, okay.
**Tyler** 38:15 No, it was just, like, yeah, it was the, yeah, the impotence of, like, the, the filter function, whether that was taken into account, and it was, it sounds like, so, okay, cool.
Cool, yeah, alright, yeah, I'll take a look at that as well. It's on my list. Any other… looks like that was the end of the list.
Yep.
**David Ashpole** 38:34 Yeah, those are the performance ones.
I did… I will… we have a couple minutes, so I'll just discuss it, but I did do a prototype I'm curious for the folks who represent companies that have Backends that primarily look for deltas, whether it's interesting or, like, whether it's something that has come up.
It came up in discussions around bound instruments that Applications can see jitter.
After collection, because you… we… right now, we, like, clear the entire… Sync that map.
Right, and so when you do collection, like, all of the measurements to all the attribute sets are gonna have, like.
I think it's 3 allocations and 3,000 nanoseconds of overhead today, or something like that.
When you actually go and construct the new reservoir, and construct the… aggregations, and make all the sets and all those things. So, I did a prototype that defers that, or that lazily, basically.
Kind of garbage collects.
The actual entries in the map?
For deltas, so that we would be able to reuse The storage and just reset it instead.
Bye.
I don't use delta metrics very much, so I'm not sure how big of a problem it is, but… If people are interested, I can open an issue to track it. It's also sort of being dealt with by Bound Instruments, potentially.
So maybe it's, like… Maybe it's not worth the complexity, but.
**Tyler** 40:12 I think that depends on the specification definition, on that.
**David Ashpole** 40:16 Yes, it does. It does. So, like, I guess… Probably, I wouldn't do anything until that, like, definition gets resolved, but I'm also just, like, asking if people have heard of this problem, or if it's, like.
**Tyler** 40:33 I haven't.
**David Ashpole** 40:34 But… Okay.
**Tyler** 40:35 I mean, I'm not… It's like, I'm interested, that's a cool optimization, I love this idea.
Yeah, we've probably always been of the assumption that, like, collects are kind of, like.
3, as long as it's not, like, seconds, right?
**David Ashpole** 40:50 Well, it's like, I could care less how long collect itself takes. It's more the impact on… It's more concerning if there's an impact on all of the supposed… like, potentially performance-sensitive measurement calls that are being made afterwards, right? I think that's… Maybe the concern here.
**Tyler** 41:12 Yeah, and I think that, like, I guess there's a synchronization happening there, because the maps have to get reset, but, like, it's actually… I mean, I think it's actually even.
**David Ashpole** 41:22 How do you fix that? Because we do…
**Tyler** 41:24 I do the hot cold, so it's like… like, there's really nothing blocking in-thread for the new measurements, so, like, I don't see… Well, I really don't see the…
**David Ashpole** 41:34 Yeah. Because we clear the map, you basically have to put the new element in and reconstruct the aggregation type and stuff like that.
**Tyler** 41:42 Yeah, but I mean, that's just, like, that's just pressure on the GC and, like, out of thread, right? Like, it's not… it's not blocking hot path thread, so it's, like, it's definitely, like, more overhead than… than it would be if you didn't do that, but… It's like… I don't think that's, like, a serious, like, concern, right? Well, not, like, trivializing it, but, like, it's not something that you're gonna see from, like, a user using this.
**Bryan Boreham** 42:06 If you outrun the background GC, it will start… Go will start blocking your hot path threats.
**Tyler** 42:12 Sure, yeah, sure.
But, I mean, I think that's, like… I think that's, I think that's the edge case. I don't think that's the common case, is what you're seeing there.
**Bryan Boreham** 42:26 Well, I'm… I've never written a filter, so I… I haven't seen this personally, but someone who… This absolutely will impact performance. It's… it's not.
**Tyler** 42:39 It's not a filtering thing, it's a collection thing, right?
So it's a… so in, like, one thread, you're doing measurements, but then in the other, like, you know, eventually you need to sync these measurements and then send them somewhere. It's that collection process, is what Dave was talking about. So, in that collection process, like, you need to take all those, switch out a map, and then, like, when you do that switch, you need to then clear what used to be there.
And in that clearing, you're doing a lot.
**Bryan Boreham** 43:03 memory… The memory pressure is only on the background thread.
**Tyler** 43:07 Yeah, yeah.
**Bryan Boreham** 43:08 Okay.
**Tyler** 43:09 Yeah. Which, you're not wrong, like, if, like, the system's super overloaded and, like, the GC's getting behind, like, yeah, like, that could impact the other threads as well, but, like… Yeah, it's not.
**Bryan Boreham** 43:20 You have to be doing significant memory allocation in your hot path to be affected by somebody else doing memory allocation.
**Tyler** 43:28 Exactly, yeah, yeah. So, I mean, I think your optimization, David, is… Worth documenting, at least, but…
**David Ashpole** 43:35 Okay.
**Tyler** 43:36 Yeah, if I were gonna prioritize it, I wouldn't… I wouldn't put it top of the list.
**David Ashpole** 43:42 Okay.
Cool. Maybe I'll just open an issue then, and I'll close the prototype.
**Tyler** 43:48 Yeah, I mean, that sounds.
**David Ashpole** 43:49 Sounds good.
**Tyler** 43:51 It also is, like, one of those ones where I'd be, like, really worried about getting it right.
Because there has… of, like.
**David Ashpole** 43:57 Yeah, it's at least, like, kind of self-contained, right? We basically mark everything as stale instead of deleting it.
**Tyler** 44:03 Hmm.
**David Ashpole** 44:04 Right. By atomically incrementing, like, a cycle counter. So, like, this is collection cycle number 5, and then when it goes to 6, everything that is marked with 5… is an active… yeah, yeah, I know, it's complexity.
**Tyler** 44:18 No, it's not, it's like, you're cracking me up, because you literally, like, we are… we are full circle. This was the original, like, Josh McDonald, design of the SDK at this point, yeah.
**David Ashpole** 44:30 I'm honored.
**Tyler** 44:32 Yeah, it's just taken us 3 years to get here instead of, you know, one massive PR. So, yeah.
Yeah, I mean, I don't know, I think that that's cool. I like the idea, it's just, I imagine that PR is also quite big.
**David Ashpole** 44:51 It's mostly big because there's a lot of AI-generated tests That I couldn't be bothered to write myself. The actual changes, I think, are around… I think it's close to 100, maybe, lines?
I also didn't want to replace the existing… so you basically, you implement… like, we have this limited… we have the limited sync map concept, right? Where it's, like, a sync.map that has a limit.
It… it can all be implemented.
Like, as a replacement for that, where… It's all internal to that map thing.
And then everything else doesn't really need many updates. It's just a question of whether you trust the logic there.
**Tyler** 45:35 Yeah, I… I don't… I don't know if I'd close this. I might wanna… I might want to try to push this one through.
like, I… I don't know, it doesn't sound like… oh, I mean, I'm even… sorry, I'm looking at it right now. Looks like you also have some benchmarks here. Maybe that could help motivate this.
**David Ashpole** 45:52 Well, so the benchmark… there's, like, a bunch of different benchmarks, and the benchmarks are hard because… you… you can't… Like, to have a… you want to benchmark the impact of a measure call that happens right after a collect.
really expensive and measure is really cheap, and so if you put the go start-stop timers.
taking the time dominates the benchmark, and you get weird numbers.
So, there's, like, 6 benchmarks in here, and only one of them is actually useful.
**Tyler** 46:25 Oh, really? Is that the measure width collect?
**David Ashpole** 46:29 There's one where I had to do a fake implementation of Collect.
Sorry, this is very prototype-y.
**Tyler** 46:37 No, that's fine.
I mean, that's fine for me. I'm sorry if other people are getting really bored on this.
**David Ashpole** 46:44 It's like…
**Tyler** 46:45 We are at the end of the meeting, I guess, but… So, I've got… hopefully she can see my screen. Which one are we looking at, David?
**David Ashpole** 46:52 The one that's in the description is the one that actually is useful.
So, this is… the… The limited one is the existing behavior.
**Tyler** 47:05 Yep.
**David Ashpole** 47:05 And then the lazy one is the new implementation.
And so what you have to do for each is you have to take measure, no collect, Right?
Which is just a regular measurement.
**Tyler** 47:18 Oh, okay, see.
**David Ashpole** 47:19 And compare that to measure with collect minus only collect.
So…
**Tyler** 47:26 Yeah, okay.
**David Ashpole** 47:27 You end up with about 200 nanoseconds.
Further.
**Tyler** 47:32 CRM.
**David Ashpole** 47:33 And then for the lazy one, you end up with about 30 nanoseconds.
So… it shaves a little bit off there. I think the bigger, deal is maybe the four allocations you get.
**Tyler** 47:45 Yeah, that's…
**David Ashpole** 47:46 When you're basically populating the map.
So… and the main reason why this would potentially be impactful is because it happens across the entire SDK at once, right? So you do a big collect, and then just, like.
for every cardinality you have in the SDK, you're getting 4 allocations, and that's all gonna happen in, like.
a second.
**Tyler** 48:09 Hmm. Yeah, so if you have something with really small collection cycles, this actually may have a lot more churn on the memory, or a lot less churn on the memory, yeah.
**David Ashpole** 48:18 Yeah, if you had small collection cycles, maybe less, because it would be spread out over time more.
**Tyler** 48:23 Yeah, yeah.
**David Ashpole** 48:25 CJO seemed very concerned about it in the discussion, so this was… this is partially to, like, to at least show that… it's possible to get rid of this problem for the most part. That's cool. If you're motivated enough, yeah.
**Tyler** 48:39 Yeah, I… I didn't look at it because it's still a draft, but I would be into looking at this if you wanted to promote it.
**David Ashpole** 48:45 Okay.
Yeah.
Well, that's good.
**Tyler** 48:51 Yeah. My goal is that, like, you need to stop, like, your performance optimizations with, like, some sort of comparison with Prometheus. You need to compare against Rust.
Eventually, you have to be faster.
**David Ashpole** 49:03 then go to Rust.
**Tyler** 49:04 Yeah, I need you to beat CJO, with his, like, zero allocation, 2 nanosecond measure… Measurements, or something like that, like, yeah.
**David Ashpole** 49:11 Ours is never gonna get below, like… Yeah, maybe he just has a faster computer. I needed, like, a Mac Mini or something sponsored by.
**Tyler** 49:18 He's… yeah, he's down to one CPU cycle, is what he's pretty much told me, and I'm like, there's just no way we'll ever get there, like, yeah.
But… You can always dream, right? Cool.
Awesome. Alright. At the end of that, I think we're at the end of the meeting as well. Any other topics, ideas, things people want to talk about here?
People coming up with topics for KubeCon talks?
Got, one more month.
I don't know, David, it seems like we just had a few topic discussions right there.
**David Ashpole** 50:06 I know.
**Tyler** 50:11 Cool.
Alright, well, if that's the case, then we can probably end the meeting early here. Thanks, everyone, for joining. We'll see you all in a week's time, or asynchronously. Until then.
Bye, everyone.
**Pellared** 50:21 P.
**David Ashpole** 50:22 Dear.
