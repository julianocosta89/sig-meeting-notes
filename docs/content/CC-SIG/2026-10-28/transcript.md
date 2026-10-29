SIG: C/C++ SIG
Date: 2026-10-28
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Douglas Barker** 04:24 Hey, Mark.
**Marc Alff [MySQL]** 04:26 Hi, Doug.
**Douglas Barker** 04:27 Sorry, I'm late.
**Marc Alff [MySQL]** 04:29 Yeah, that's okay.
Actually, it's, we are in wintertime now, so it's not the same time as usual for me as well, so… I think I'm a bit surprised by that.
**Douglas Barker** 04:47 bulk meeting notes.
**Marc Alff [MySQL]** 04:49 Yep.
Just quickly, because this is the last day, you know that we have DC elections, running.
Okay.
**Douglas Barker** 05:00 Yeah, I voted, yesterday.
**Marc Alff [MySQL]** 05:02 Okay. Yeah, I was able to vote, but had some technical glitch with GitHub for a while, so… To debug that, to finally be able to cast a ballot.
**Douglas Barker** 05:15 That's how that was. Yeah.
**Marc Alff [MySQL]** 05:25 Do you have any… anything special to discuss?
**Douglas Barker** 05:32 I have a few items on my list to do for, Hotel CPP. I gotta update my, PR, rebase it, and then… I need to reply to a comment on the configuration repo, because I logged a ticket there, but…
**Marc Alff [MySQL]** 05:49 Okay, alright.
**Douglas Barker** 05:49 I'm not critical for this meeting.
**Marc Alff [MySQL]** 05:53 Okay, so the… The main topic I have is basically related to all the… The no-exception cleanup, what we need to do.
And… So… I even forgot where that is.
Yes, so I finally did this, proof-of-concept PR just to see how it goes.
And, drill some… Overall, my impression is that fixing this no exception thing is not going to be very simple.
Because there are some… both pros and cons about having… having this tag all over the place, so… I'm… Earlier, I was convinced that removing the tag everywhere except the entry point will work, and now I'm… I think it will work, but also I think it will be too disruptive for the code, and… the place where we have this tag are actually, it makes sense to have vertex in most places, maybe not all of them, but in most places.
So, this thing is complicated.
So, one thing I tried to do… is, go back to why we have seen untidy warnings in the first place, and trying to fix the root cause. And one thing that stood up is, so far, we have been focusing mostly on, out-of-memory exception, which is bad luck.
But in fact, it's only one part of the problem. The other part is, exception related to the use of variants.
And… so… Whether we will be able to fix the out-of-memory is one big question.
Oh… And it's very intrusive.
But in the meantime, I think a strategy might be to try to fix everything else first.
And see where we are, and then decide, once we have better visibility, to decide what we do with out-of-memory.
And… So, looking at that, I found a gold mine of areas in the aggregation code, which is using variants that should not be, basically.
Which is… So… which is VPR, so what I did is, look at… Of the aggregation code itself, and to my surprise, why is that so… In the aggregation code.
we have this point data, so I'm only looking at some aggregation, for an example. So, in some… in that… some point data, we have a variant.
But can hold, either a nit or a double.
And it… so why not? But it turns out that every single place we use it, we use either one or the other.
But in a class which is dedicated to either, long aggregation or double aggregation.
We never have a code that uses both of them.
And actually make use of a variant, which makes me question why… We have this variant in the first place, and removing it solves, actually, a lot of problems.
And solves, all the exceptionality to get and get if…
**Douglas Barker** 09:48 That makes sense.
**Marc Alff [MySQL]** 09:50 Yeah, so…
**Douglas Barker** 09:50 I mean, we also have some other type issues.
don't we have unsigned integers? Or maybe that's just… yeah.
**Marc Alff [MySQL]** 09:58 Yes, so…
**Douglas Barker** 09:59 Bonsai integers, they were converting to integers, and then ultimately on the wire, they go over as integers.
**Marc Alff [MySQL]** 10:05 Yes, so the aggregation code has a lot of typing issues, especially… For integers, for example, because counters are so supposed to be monotonic, So that, So, counters are monotonic, so they are supposed to be inside, and then, of course, there is the… the gouge and what else, so that we can have some things which are, signed or unsigned, depending on the exact, instrument type. And that was not anticipated, Initially, so this is… we have an ugly cast going from one to the other, I don't remember where, but it's not, It's not what it should be.
And… So, we have that for foreign sign, signed and signed. For double, it's… it looks okay, because we don't have this issue.
But there is also the idea of whether we will have some other types in the long term.
Like, so far we are using 64-bit ints, but, oh… I don't know if we have to, but if we ever have to implement… Aggregation for smaller types, like 32 bits, for example, we don't have that code either, or things like that.
So, ouve… On the aggregation code, it was basically implemented one aggregation after another, and sometimes it just did fit with existing code, sometimes it did not.
**Douglas Barker** 11:53 Yeah, this looks like a good change. I can take a look at it, maybe this weekend.
I'll try one of these evenings.
**Marc Alff [MySQL]** 11:59 Yeah. I was hoping for Lalit. I'm not sure, I think Lalit implemented that code a long time ago, so I was hoping he could take a look.
the main question I have right now… so, looking at the code today.
We have… we have a class like, where is it?
So, we have a class which is long-term aggregation, which is supposed to use only ints, and then, of course, we have double aggregation, which is only using double.
The part I would like to confirm, and probably with Lalit first, is… Whether it is intended that, things which are typed like that only use, so long only use, integer, and double only use double.
If this is the case, then we can refactor.
And if… On the other hand, it turns out that, no, those things should deal with all the types we can possibly see, even the… The variant will make sense. And also, in that case, we have missing code, because the… You see, for example, on the aggregation code, this thing only aggregates integers, and there is another method which is to aggregate a double, which is not implemented.
So… The main point for me is Clarify what is the… For intended, behavior, whether… Each type degradation only deals with its own type, or whether each type degradation needs to deal with everything.
**Douglas Barker** 13:48 That makes sense.
The one part I also don't know about is, in the spec, if you have a metric stream with the same name, and somebody creates an instrument with a double and one with an int, and records to it, should it go to the same stream? I don't… distinguishes, By… by the type.
**Marc Alff [MySQL]** 14:11 Yeah, I looked all over, and… Typing… it's also likely that typing depends on which language is used, so… I don't know if a spec will go into that level of details.
**Douglas Barker** 14:25 Okay.
I know what we do right now, because I implemented part of it, was when we create those streams, we are, checking the type, so a double stream with the same metric name would be a different stream than an integer with the same metric.
Currently. I don't know if that meets the spec or not, but that's what we're doing.
Cool.
**Marc Alff [MySQL]** 14:50 Yeah. Yeah, so basically I did VPR just to refactor the code itself.
Oh, and so… it only changes a few editor files, and coding-wise, it only changes the… so Azure only fixed the sub-aggregation, so only sub-aggregation is fixed there.
There is some small impact on exporters, basically, because the… We've correlated to the… two different, variants, and there is a huge impact on the test. If you look at the PR, most of the… Most of the code change is in the test area, and it's, All the time, it's to, adjust, or adjust to remove all the… all the variant-related code. For example, like, in this case, well, the value, it used to be a variant, so you have to ask for the double data in it, and now it's just a double directly, so… A huge simplification, but this is touching a lot of test files.
So… Test is not really an issue, and on top of that, it just simplifies the code, which is always better.
And the main question is whether we can actually do that in the… investigate itself.
Where was I?
Yes, so wherever we can do that in SDK. And… One thing this simplifies, so all that goes away.
This cilia, or like, well, it goes away because, We never have a case where we have the wrong type.
And… So it simplifies a lot of code there.
**Douglas Barker** 16:45 Oops.
**Marc Alff [MySQL]** 16:47 So, at least… Independently of, whether we refactor even or accept code.
This simplifies and, resolves Some of the exceptions which are raised in, in, in the quarterly to, to, the no-except, warnings related to… detected by a ceiling tidy.
**Douglas Barker** 17:15 Yeah, I haven't looked recently since I turned on the, the clinktidy check for new, and when it throws, but I think we can probably focus on In addition to the variant.
ones we can focus on anything impacting the API. I fixed a couple of them in the propagator, but…
**Marc Alff [MySQL]** 17:34 Yeah. I don't know.
**Douglas Barker** 17:35 If there's any more left, but that… that seems like a higher priority, too.
**Marc Alff [MySQL]** 17:39 So, we have quite a few left. This is everything we have today, but most of them are coming from the check on new.
**Douglas Barker** 17:51 Yeah.
**Marc Alff [MySQL]** 17:52 I think we have something around 60 issues related to… Catching, well, exception escape, which was the original issue. So we have something like SISTI, and that code change only, fixed two of them, which are just two that were raised inside the aggregation code.
But the same pattern can be done with other aggregations.
And that should, that should simplify a lot and remove a lot of, those things.
In the ceiling tidy log, you can see that a lot of the remaining issues are coming from the metrics aggregation code.
**Douglas Barker** 18:38 Yeah, I'm bringing it up now.
**Marc Alff [MySQL]** 18:40 Yeah.
And this, so this change alone, it fixes, fixes a dozen things.
**Douglas Barker** 18:56 Yeah, so I'm seeing quite a few still left in the API, and I think, like, that… that one can be a priority.
For… that's really, really just a new, and then…
**Marc Alff [MySQL]** 19:09 So, API, there are a lot of things in baggage, there are a lot of things in context.
**Douglas Barker** 19:13 Yep.
**Marc Alff [MySQL]** 19:14 And they are… they are related to the use of, shared pointers, and… Yeah.
That is going to be complicated to fix, I guess.
**Douglas Barker** 19:27 Well, I think there's an opportunity there. We can switch to, make shared and safe one allocation, so that could be a decent performance improvement for some of these things that are in the hot path, and then… we can just do the try-catch, like I did in the propagators. Maybe that, if you're okay with that pattern, we can just apply that to all of these cases in the API.
**Marc Alff [MySQL]** 19:48 Well, we can… we can look, but I'm… even if we do a try-catch, there is the question of what will return, and if it's written under a pointer… Sure. It's… we break the… the API assumption.
Because people calling that are not, prepared to deal with a null pointer, and my fear is that this will open a huge can of worm.
If we take that path. So, if, yeah, if some cases can be simplified, sure, and whether we will get all of them, not convinced yet.
**Douglas Barker** 20:29 Okay.
Wow.
**Marc Alff [MySQL]** 20:35 Someone also, pointed that, there is a new version of CNN TADI which is coming.
And in the configuration for ceiling tidy, there will be a new way To report warnings with a final grain, for the exception escape.
So, maybe it will be easier also to investigate things there, once we have that.
**Douglas Barker** 21:07 Yeah, I haven't checked to see what version ships with… 2604, I think it's… that we're using LLVM22.
But we also need to complete that upgrade in the C… in the… Doha Brothers.
Do you know, Mark, when they're, phasing out the 22 of 4Runners?
**Marc Alff [MySQL]** 21:35 No eddish, but… Okay.
for the room… For all the runners we use internally for maintainer builds, like, things like CNN ID, include what you use, and so forth.
We have the freedom to take any arena we need. Yeah. So… If there is a newer runner with some most up-to-date tooling, we can take that.
And, Martin also looked at VPR and just pointed out that if we So, I just removed some point data, which is replaced by two alternatives now in the top level.
Variant for aggregation, and this has some impact externally to… one contribib, which is in Cpptribe, and also to, some, Google Cloud code.
So, if we do that, we have to be aware also that that will cause a braking change elsewhere.
**Douglas Barker** 22:50 No, that's a good point.
Yeah, and that impacts a lot of tests, because I think we're doing that in a lot of tests, too, right?
**Marc Alff [MySQL]** 23:08 Oh, yeah, but… so all the tests, it's tedious to adjust it, but it's, well, I just did it for one aggregation type, so… And actually, it simplifies the test code as well, so…
**Douglas Barker** 23:20 Yeah.
**Marc Alff [MySQL]** 23:21 Federal.
It's just tedious to go over all that thing.
**Douglas Barker** 23:25 It's definitely… yeah, it's good that you… my team searched that, because I think in my own project, I also am using that similar method in tests to, like, get the… some data point, and then access it, so… with the variant.
**Marc Alff [MySQL]** 23:39 Yeah.
**Douglas Barker** 23:40 It would be a pretty… Pretty big change.
But, maybe with AI tools these days, people are okay with that.
**Marc Alff [MySQL]** 23:50 So, you know, typical change… there are two places which are impacted.
At the top level, aggregation is a variant of a lot of things, and one choice is replaced by two choices.
So, there is this change to do… To tell exactly which aggregation Rakut is using.
And once you use one which is typed, this… This thing goes away.
Which is to extract the type value from that type aggregation.
**Douglas Barker** 24:29 I'm talking about the… Yeah, it's good, good to call out that this is potentially an interface that people are using now.
**Marc Alff [MySQL]** 24:37 Yeah.
**Douglas Barker** 24:40 Alright.
Was there anything else that you wanted to go over?
**Marc Alff [MySQL]** 24:47 Let me check. I forgot already.
Yes, so… As you are aware, we had, a security fix in 1.30, so Verliz is out, and someone already contributed a package in Bazel.
So that it can be used, so… there is a new package in Bazel Central Repository, and now people can use that.
new, new release in Basel itself.
For CMake, well, we do have support in CMake.
The next question, and that one was short-term, mostly, because I think he's also… the maintainer of the VC package.
And… It probably should be updated there, so that people can use it.
And there's the same question for Conan.
And especially for Conan, now that we do have tests involving Conan, and now that CPP Contrib is also using Conan, we should only have an updated package there so that we can upgrade CI.
Otherwise, the CIA and CPP country is still stuck on old, disease.
So, not something really in our control, except maybe VC package for, with Tom.
Otherwise, yeah, we have to wait for people to upgrade.
**Douglas Barker** 26:17 Okay.
**Marc Alff [MySQL]** 26:26 And no, I don't have anything else to, to discuss.
Except the number of, PR, but it's still growing and growing.
At some point, we were stable at around 50, but it's going up again.
Oh, yeah, David Ashport also.
filed a couple of PRs on Prometheus, so… will be, I'm assuming that food will be, approved and emerged soon.
Some nice… some… some nice skin up there.
**Douglas Barker** 27:14 Race.
Yeah, and I saw you upgraded the, config schema. Thanks for doing that.
**Marc Alff [MySQL]** 27:24 Yes.
**Douglas Barker** 27:25 exchange.
**Marc Alff [MySQL]** 27:26 Yes. Talking about that, so, the schema is updated with some new, new nodes.
I still need to file a couple of PRs, because for some of them, the SDK part is missing.
We have… we have a new sampler, type.
which is the always-record sampler, which is missing in the SDK so far.
And there are some changes into metric segregation.
And some changes to the OTLP exporters that now take a limit.
On both on sending and receiving, data to the… to the OTLP backend, so… The syntax is accepted in YAML, and we have classes to represent the config.
But it doesn't do anything yet, so we need to implement that in the SDK proper.
**Douglas Barker** 28:34 Sounds good.
**Marc Alff [MySQL]** 28:36 Yep.
**Douglas Barker** 28:36 Excellent.
Alright. Well, I'll try to find some time this week. I'm a little bit more busy these days.
**Marc Alff [MySQL]** 28:47 Yes.
**Douglas Barker** 28:47 Let's look at some of the PRs, and… Clean up my own.
**Marc Alff [MySQL]** 28:51 Yeah, okay.
So, I don't have… I don't have anything else, so yeah, election… You're aware of that song, sir.
And I have altered as well, so we're good on those.
**Douglas Barker** 29:07 Awesome.
Alright.
**Marc Alff [MySQL]** 29:09 Yep.
**Douglas Barker** 29:10 Thanks, bro.
**Marc Alff [MySQL]** 29:10 Thanks for… thanks for joining. I was about to close the call, but…
**Douglas Barker** 29:15 Couldn't.
**Marc Alff [MySQL]** 29:17 Alright, take care. Bye.
