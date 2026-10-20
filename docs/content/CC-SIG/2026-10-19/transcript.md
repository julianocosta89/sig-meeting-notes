SIG: C/C++ SIG
Date: 2026-10-19
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Marc Alff [MySQL]** 03:12 Hi, Doug.
**Douglas Barker** 03:13 Hey, Mark.
How are you?
**Marc Alff [MySQL]** 03:18 I'm doing okay.
I think I saw this, and maybe he will join also.
**Douglas Barker** 03:26 Okay.
I haven't had a chance to look at the agenda yet. Is there anything in there?
**Marc Alff [MySQL]** 03:53 No, I just created it, but nothing special.
How are you, son?
**Ehsan** 04:21 Hi, Mark.
**Douglas Barker** 04:24 Ehsan.
**Ehsan** 04:26 Hi, Douglas.
**Marc Alff [MySQL]** 04:31 Okay, let me see if I can share my screen.
Okay.
Do you all see my screen now?
**Ehsan** 05:26 Yep.
**Marc Alff [MySQL]** 05:27 Okay.
Yeah, so Duga… As you have seen, I saw your pull request on performance optimization, so I approved it.
And, you are the number one with, Yes, breaking traces on the start span, when we have the… Appoint context.
I saw that today some… so, there were two parts on that. You fixed the one in SDK, and someone else just pushed the PR to fix the similar thing and start spanning the API.
**Douglas Barker** 06:12 Awesome.
**Marc Alff [MySQL]** 06:17 Which is this one, actually.
**Douglas Barker** 06:18 Okay.
So it's,
**Marc Alff [MySQL]** 06:31 I'm just surprised that we have things like that that show up. I mean, the… It's something that we most likely broke when the tracer config was implemented.
Because it's a new feature, and then it was implemented using a no-op span all the time.
But that was some mistake, obviously, so…
**Douglas Barker** 06:57 Yeah, it was kind of a footnote in the spec, so… at the bottom of the page, so it may have just been missed. I ran into it over the weekend when I was trying to get something working. I was like, shouldn't this, be able to disable a tracer and then not break the span?
**Marc Alff [MySQL]** 07:10 mature.
Yeah.
It's over… On this one, the part I'm worried about is, it sounds fixable in the API, but we'll have to be very careful about all the no-except story, which is… causing complications.
but also Once it is fixed.
Because the API is head-only, people will need to build with a recent API again.
To see the fixes.
So, someone who compiles, instrumentation with an old version of OpenTelemetry, and we'll see an old version of whatever code we have under API.
And once this is compiled and part of their, They're binary, They will not see the fix, so they would have to Make a new build with a recent, OpenTelemetry Version 2 to see the benefit of a fix.
**Douglas Barker** 08:21 Yeah, and this came up before with the log filtering, and we decided at that time, because it was an observable behavior change, that it was only gonna be implemented in ABI 2.
**Marc Alff [MySQL]** 08:32 Okay.
**Douglas Barker** 08:34 We could do that here. I think it is an observable behavior change.
**Marc Alff [MySQL]** 08:39 Serve.
**Douglas Barker** 08:40 Certainly, if it was an ODR violation type of scenario, like, it would be unexpected if it sometimes works, sometimes doesn't work.
So…
**Marc Alff [MySQL]** 08:52 Yeah, well, the expected behavior is that we don't break the trace, so the… I think it's okay, even if it's a behavior change, I mean, it's a bug which is fixed, so that would be okay to fix in the API itself, even in API V1, if we can… API V1, sorry, if we can do that.
Oh.
But the concern is to… to convey the information that… You need to do a build again and deploy again to see the fix, otherwise you would just don't see it.
**Douglas Barker** 09:22 Good.
**Marc Alff [MySQL]** 09:30 Sorry for the discretion on this thing. Ehsan, do you have any topics you want to discuss today?
**Ehsan** 09:38 Oh, no. No.
I just had one question, but can wait.
**Marc Alff [MySQL]** 09:45 Okay, oh… Or you can go ahead now, up to you.
**Ehsan** 09:51 It's a biometric, so I was wondering what's the state of exemplar?
**Marc Alff [MySQL]** 09:59 I'm not sure, it's… so Examplar… so, the first thing about Exemplar is that it's, still behind a feature preview flag.
Which is one thing.
And the status of it, whether it is fully implemented or not, I don't know.
**Ehsan** 10:16 Good.
**Marc Alff [MySQL]** 10:17 I don't recall what is, if something is missing, I don't know what it is.
**Ehsan** 10:23 Alright then, thanks, I'll check that.
Technically, basically.
**Douglas Barker** 10:28 We do have… probably 2 or 3 PRs that have been open for a while.
around exemplars, and one contributor's been really working a lot on Trying to, improve the interface and performance, so… If, that's an area you're interested, we definitely need help reviewing those PRs.
**Ehsan** 10:50 Okay, I'll check those then.
**Marc Alff [MySQL]** 10:52 Yes.
**Ehsan** 10:54 Thanks.
**Marc Alff [MySQL]** 10:55 And… I think exemplars also came up in the discussion about performances.
like, I don't recall all the details, but when we have an exemplar, there is also some sampling involved to decide when to take an exemplar.
Something like that.
And if we don't take any, basically we should have some shortcuts in the code so that we don't spend too much time Preparing something, offering a measurement to an exemplar that won't take it anyway.
In case of a drop or slow.
There is also a performance and benchmarking aspect to it.
But I don't know.
Much beyond that.
**Douglas Barker** 11:51 Yeah, I think we got some good benchmarks in there now. I added some on the metrics recording side, so it covers with exemplars built.
**Marc Alff [MySQL]** 11:58 Okay.
**Douglas Barker** 11:59 So… we, should be able to see the impact, I think.
the PR that makes a change for exemplar performance also shares some of the benchmark results.
**Marc Alff [MySQL]** 12:13 Okay.
I didn't write that in the meeting notes, sorry. But I have two main topics. The first one is, how to join this, Review you?
At least it's not growing anymore, but we are still at 50, and With a lot of things which have been hanging out for a long time.
So, we need to figure out how to… To be more effective in general for reviews, and to get these out of the way.
And the other topic is, how to deal with all this no-except thing, in general.
So… We have C9 Tidy, which is complaining about a lot of issues related to exception handling and things like that.
And the goal is to just get that cleaned up.
Last week, Doug and I discussed one possibility, which is just to remove all the No Accept code inside the internals themselves.
Which I've, I'm working on this in this proof of concept PR.
Verity being, we don't need to have every single method in the SDK marked as no except, because it's really a huge constraint on the code, and… To make that work, we'll have to have some tri-cache blocks all over the place, making the code very difficult.
The other way is to only try… only keep The no accept at the entry point, where we go from the API to SDK.
Typically for traces, that will be on a get tracer, or on a start span.
And then, have a try-catch block at that place only, so that all the rest of the code is not marked nor accept.
And he has more freedom to… To implement things involving memory, and then we will put the track hash block only at the very top level in the SDK.
So, to investigate this, I have this PR.
It does improve things a bit. There are less warnings reported to… we've seen Italy on that thing.
I still need to work on it because there are some… I cleaned up all the code in SDK include, but I also need to look at the SDK implementation itself to also remove some… some no-except prototypes there to simplify the whole thing.
I, I, I think… overall, there might be a way to actually simplify a lot of things to discuss. So.
the PR is still a… First of all, it's a proof of concept, so we will not do everything which is there, it's just for evaluation.
And I'm still working on it to, to make it cleaner, so… I think it will be ready to discuss next time, maybe.
Ehsan, since you've been here for a very long time.
Do you know what is the history, behind, no accept in general that we have in OpenTelemetry?
**Ehsan** 15:47 I don't know its history, but I think… If you are sure that you… you should not have an exception, you should not have it. It's… I mean, it's easy to make mistakes with exception.
**Marc Alff [MySQL]** 16:06 So…
**Ehsan** 16:06 who… If you throw… In a destructor, you might end up with an undefined behavior.
**Marc Alff [MySQL]** 16:16 Okay.
**Ehsan** 16:22 That's huge… I mean, in general, if I… If I see that it's possible, I had no exception, I would add it.
Just to avoid this.
It's as helpful in the long run.
**Marc Alff [MySQL]** 16:38 Well, if code is so simple that there is no way to have an exception.
We can add, no accept, and my understanding is that it… It allows the compiler to make more, assumption, and have some code which is more efficient, so it's helpful, helpful.
whoever… If we make a mistake, and if there is indeed an exception that can be raised there.
The outcome is that, basically the process stops and is terminated, because the exception is not propagated upwards, because the compiler does not generate precisely code to handle exceptions.
So, It sounds like a good thing to do, but overall, because we have so many code which is… we have code in places which is flat as no accept.
And still allocate memory, which can't fail with an exception.
And it seems actually counterproductive, because the whole point is To avoid raising exceptions that will kill the application, and instead it will just terminate the process right there, instead of trying to catch it and handle it somehow.
So… Because of that, I think it will be also… More healthy to, to… Remove some no except, methods, in general from SDK, and only keep them at the entry point.
**Ehsan** 18:15 Yeah, the other thing, right?
I think we are kind of made C++ similar to Golang, so maybe that's another reason we have this no exception.
**Marc Alff [MySQL]** 18:27 I see.
**Ehsan** 18:30 There are a lot of similar patterns with the Golang in this repo.
So, like, in Golang, you are expecting To, to, to always check the errors.
**Marc Alff [MySQL]** 18:49 I see, yep.
Yeah, VC… well… Yeah, OpenTelemetry CPP was not implemented in isolation, so yes, there are also other, SDK implementations.
So I guess people would look left and right to see how… Things are done in other languages, then.
One could explain.
So yeah, so overall, this is the… One big topic that we have to… To address and to simplify and clean up.
So… I'm still working on this proof of concept to see, If… what we can do to, to simplify things.
And I'm hoping to have, Something ready to discuss next time.
On recent things, I don't know if you noticed VPR… Someone proposing to basically, all the… All the regular exceptions.
So, there it is that we have We have a couple of places where we have some… Code that deals with, or… Transforming a character to uppercase, lowercase, and whatnot.
And it's actually spread all over the place. We have such tiny fragments, in different… all over the codebase.
And what he… what he did is… all developers in one place, which are, Implemented as is.
without relying on any C++ library or anything.
This is actually trivial, because we only need to check for ASCII characters, there's no… no complication with CodePage, Unicodes, and whatnot.
So it's actually trivial to do that. And, to my surprise.
Implementing that in this helper actually simplifies a lot of things all over the place.
Like, it's cool that we had… In general, But instead of implementing helpers left and right, we can have just… we can just implement them in once, and use them like this.
And he did a lot of cleanup all over the place to just get rid of Small helpers like that, with charges spread out everywhere.
So… I think this PR is definitely something we should look at.
And the added bonus is… If we no longer rely on regular expressions.
Well, first of all, it reserves some… So, the original point for that, that issue was that… using regular expressions actually consume a lot of stack, and can go with Stack Overflow in some platforms.
So this is… one thing I was not even aware, but just the fact that using regular expression actually can consume a lot of stock and can Kill the process. So we get rid of that.
We also get rid of, Possible exceptions that can come out of regular expressions, because we have… Koruchi's much, much simpler.
And I don't recall if there are some performance benchmarks for this, but I would also accept that the only place where we use regular expression is to see if a trace ID is formatted properly, or a span ID is formatted properly.
Or if a view name has some, is named, properly, things like that.
And… The regular expressions, they are extremely simple, so it's, It's actually simple to check with explicit code, as opposed to to use Oregas to check that… what characters are allowed and are not allowed.
So, not only this cannot require a lot.
Make it more robust, but on top of that.
I would expect that the code is actually more efficient.
Sue.
Overall, that PR looks like something we should take. It looks like some very good change to me.
And I swore Lalita.
Actually, I approved it.
Any other recent PR you want to discuss?
Or issues.
**Douglas Barker** 24:22 Whoa.
Yeah, this is the only one still, you know, for review.
**Marc Alff [MySQL]** 24:30 Yes, so I reviewed the other one, and I will look at this one next, so I didn't forgot about it.
**Douglas Barker** 24:45 Are there any others, for the release? I think we're just waiting on… What about draining the queue for the spans, I think?
**Marc Alff [MySQL]** 24:54 Yes, so that one I think I merged already. Let me see if one of these… where is that?
So, yeah, so draining the queue, I reviewed it and merged it, The part we are waiting on is the… so that was only for the batch processor, for spads, so for traces. The same issue exists for logs, so we need to… I think you… yeah, you marked it as, help needed, so we need the same fix for logs, the same fix for logs. And also, this is the issue you were working on, Doug, you fixed the SDK, but, the part with APR and it should be addressed as well, and we have a PR for that, so I'm hopeful we would have some… This thing merge, very soon.
**Douglas Barker** 26:00 Okay.
**Marc Alff [MySQL]** 26:02 As for the others, So I think this one is from Lalit, and it's quite old, so we need to take a look at it and… Finish my review for that.
Yeah, he's learned it.
And yeah, it's… we are really behind on reviews.
So, thanks for the review, Doug. I'll take a look as well, and And hopefully we can match one.
Other things we need for varies, so, this one, yes, I will… I will take a look.
The other two, I don't recall what the issue is exactly.
Oh, so this is to change the… The meter configurator dynamically?
While, metrics are being collected.
By the way, Duke, I saw that you also cleaned up the mutex that was used in the tracer configuration.
**Douglas Barker** 27:43 Yep.
**Marc Alff [MySQL]** 27:44 Yes, and… So, I don't know the… I don't recall the full story for that.
But I think it's, yeah, removing that was a good call, because the… The mutex was only taken on a write path, so it was preventing two updates to change the data at the same time.
But, surprisingly, the read buff was not even using the mutex at all, so I'm not sure what he was attempting to synchronize.
It looks like it was unfinished and broken anyway, so it's a good thing to… Remove it and simplify things.
**Douglas Barker** 28:26 Yeah, I'm responsible for adding it, because before the tracer was just holding the… Tracer config object, but then…
**Marc Alff [MySQL]** 28:33 nose.
**Douglas Barker** 28:34 in that PR where I added the ability to dynamically update it, I didn't… I left it, because I just assumed that maybe somebody would add some more elements or properties to the config, and we'd need it, but…
**Marc Alff [MySQL]** 28:45 Yeah.
**Douglas Barker** 28:46 So, I think it's better to prevent it.
**Marc Alff [MySQL]** 28:48 Trust.
**Douglas Barker** 28:49 Save some memory.
**Marc Alff [MySQL]** 28:51 Yes, and indeed, that also assumes that the tracer config can have more properties, which it does not have yet. It's only a Boolean anyway, so…
**Douglas Barker** 29:00 Right.
**Marc Alff [MySQL]** 29:02 I looked, but I haven't seen the same pattern applied for logs. Do you know if we have such a mint text there?
**Douglas Barker** 29:09 No, we don't.
**Marc Alff [MySQL]** 29:11 Okay.
**Douglas Barker** 29:12 Yep.
**Marc Alff [MySQL]** 29:17 Okay, so yeah, this one, I will take a look at it also.
**Douglas Barker** 29:28 I'm gonna have to, to drop off.
Yeah, that's good.
**Marc Alff [MySQL]** 29:32 Okay.
Well, I don't have anything else in general, so we can make a short call.
Okay.
Ehsan, any… any other things?
**Ehsan** 29:44 No, nothing from my side.
**Marc Alff [MySQL]** 29:46 Okay.
Okay, so just to summarize, okay, so, I'll take a look at… The reviews in general, and making sure that things progress for the next release as well.
**Douglas Barker** 30:02 Sounds good.
**Ehsan** 30:03 Thanks.
**Douglas Barker** 30:04 Thanks, Mark.
**Marc Alff [MySQL]** 30:06 Yeah, thanks, Ehsan. Thanks, Doug.
**Douglas Barker** 30:08 Great.
**Ehsan** 30:09 See ya.
**Douglas Barker** 30:09 Bye.
**Marc Alff [MySQL]** 30:10 See you.
Bye.
