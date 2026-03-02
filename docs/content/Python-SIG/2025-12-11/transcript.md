SIG: Python SIG
Date: 2025-12-11
Duration: 24 minutes
============================================================

## Zoom Recording Transcript

**Riccardo Magliocchetti** 00:10 Hello.
Hello again. Welcome, everyone, to this week's Python Seek call. We're waiting a few more minutes for more people to join.
In the meantime, please add yourself as an attendee to the… Notes document.
And also, if you have any topic you want to discuss.
Please add them too. Thanks.
Okay, it's a fight. Welcome again. I think we can start.
Okay, first toppings from me. I've released a patch release earlier today.
And, yeah, just a couple of backports, one for contribute, one for core.
And… yeah, like, we got, tribune.
Issue when releasing, if you're curious.
And… we have this problem, but… We are called,
CONTIP workflow, where we get the list of tests to run on core.
What is pointing to the main branch.
And so, this time, we added the anthropic instrumentation to Maine.
That is not available in the 1.39 release branch.
And so they were, like, true,
jobs that failed on RCI because, of course, Tox was not able to To find bees, but…
We were able to merge the…
the PR anyway, even if the CI was red, so… no big deal, but… yeah.
And then, the usual reminder, if you have time, please, review stuff.
We are accumulating in, country.
We have, yeah, a lot of PRs to take a look at.
Thanks in advance.
And then last topic for me for today, it's PSA. We got an issue.
From… User of PPEMV?
that we cut a release, I think, yesterday.
And they made, the tool not installing paralysis, by default.
And all our, packages that are, not stable yet are, released as a… with a pre-release version.
That is, 0.number B for beta and another number.
And… someone filed an issue there on PPEMV,
And they then changed the behavior, and now we install a pre-release, only if there were no release available for the package.
So, don't know if… This waiver will, you know, will be implemented by other tools.
And so I was wondering if maybe it's time to drop the,
B number, suffix on our package version.
Because maybe, like, the fact that the version is, lower than 1…
And we have the 12 classifiers, I think.
In the package metadata to signal these are beta packages, maybe is enough.
But… yeah. No need an answer right now, but if you have an opinion… I would like to know.
**lechen** 08:31 I think… I think I'm fine with the listing.
Version 1 as a beta indicator.
**Riccardo Magliocchetti** 08:44 Yeah, like, I agree.
like, I would very like to avoid, like, further tools.
Change your behavior in the future to have.
To rush something, because otherwise our stuff won't be installable anymore.
**lechen** 09:01 Right.
**Riccardo Magliocchetti** 09:10 Okay.
**lechen** 09:11 I think I will have to update a bunch of our release scripts if we do decide to do it.
**Dylan Russell** 09:20 So, it would just be for future releases, we just drop the B0.
**Riccardo Magliocchetti** 09:25 Yep.
**Dylan Russell** 09:29 That makes sense.
**lechen** 09:34 And then for, I guess, Patch releases, we… have we always incremented?
**Riccardo Magliocchetti** 09:42 The patch version?
**lechen** 09:44 Instead of, like, B1, B2, I think that's overdo, right?
**Riccardo Magliocchetti** 09:50 But I think we can add the… another, number, like… 060.1.2. Right, right.
**lechen** 10:00 Yeah.
Sounds good.
**Riccardo Magliocchetti** 10:05 But, yeah.
Okay.
**Dylan Russell** 10:08 Sorry, is pipenv, like… different from UV? Like, does UV use this pipenv thing?
**Riccardo Magliocchetti** 10:21 No, I think it's just a different tool implement, doing the same work, more or less, yeah.
**Dylan Russell** 10:27 Okay.
So if people are using UV, it doesn't… they don't run into this.
**Riccardo Magliocchetti** 10:33 No, this is specific to people using PPEM.
**Dylan Russell** 10:38 Gotcha. And it… so pre-releases is detected by the…
presence of that, like, B0 thing on the version.
**Riccardo Magliocchetti** 10:48 Yep.
**Dylan Russell** 10:52 Alright.
Yeah, I'm curious, because we, I think, are doing this for our packages, like our… GCP packages, so…
Good to… good to see this, or interesting to see this.
I think I have the next one.
**Riccardo Magliocchetti** 11:19 Yep.
**Dylan Russell** 11:23 Yeah, so we're looking to… Like, suppress instrumentation.
Of this package during auto-instrumentation.
and… I'm wondering… Like, this PR is using the, like, the suppress instrumentation key.
like, context key.
Which… Seems to be used by, like, a bunch of instrumentations, but maybe not all of them.
But I'm wondering… like… Should we add, like, a…
suppress instrumentation's key specific to this instrumentation? Is that, like… The recommended way to, like, Suppress an individual instrumentation?
**lechen** 12:24 Yeah, so the suppressed instrumentation Key, it is supposed to be used for…
the scenario you're describing. The fact that it's not being used across the board is just a…
Consistency issue, and some people are just… haven't implemented it.
You can see that there's other suppressed X instrumentation.
Keys, those are for specific scenarios, such as when instrument
It's… instrumented libraries have dependency on other libraries. Those are for other scenarios, but yeah, this… what you're doing right now is…
the intended… Way of using this, so…
**Dylan Russell** 13:12 Okay, because I think what we want is actually just to suppress this one instrumentation.
**lechen** 13:22 It's what it does, yeah.
**Dylan Russell** 13:25 But… Like…
Should we add a new key, are you saying? Or we should use this, like, generic, like, catch-all? Because…
**lechen** 13:36 If you add the suppressed instrumentation key just to the instrumentation, it suppresses only that instrumentation.
Like, so you're using it correctly. We don't have to add a new key or anything.
I haven't taken a look at your invitation, so…
I can't really say, yet, if you're doing it the way it's intended, but if you take a look at other instrumentations and how they use this, it's,
Okay.
**Dylan Russell** 14:04 Yeah, let me… let me look at that.
**lechen** 14:09 Alright.
**Dylan Russell** 14:11 Cool.
**Riccardo Magliocchetti** 14:20 Okay…
Next topic is from Alex.
**Alex Boten** 14:30 M.
Hey, everyone. I just wanted to talk about the declarative configuration implementation.
So, this issue was opened…
A long time ago, when we had kicked off the working group for OpenTelemetry configuration.
This is the configuration schema that allows end users to create a declarative config model inside the language of the user via…
Yeah.
Hey, Lynn, how's it going?
It's been… it's been a minute.
So the… the…
the stability level of the configuration working group's schema is now, we just released a RC3,
So, we hope it's going to be the last release candidate before we release a 1.0 of the schema.
And we're just looking at different implementations to see if we can either help with the implementation.
Or, if there's… if there's other things in different working… in different SIGs that we can help with to make room for maintainers and approvers to have time to review the work. So, currently there's an implementation in…
Java and Go, there's a PHP and a C++ implementation.
There's the beginning of an implementation in the JavaScript, SIG as well.
And, I know a long, long time ago, Diego had opened a PR for this particular, prototyping that he had done. I was just wondering if
like, this SIG has the capacity to take on reviewing the work for what a new prototype would look like, because if that's something that is available, then I would love to help with the implementation.
And if there is no bandwidth because of other projects, I'd also like to… to be able to take that knowledge with me and see where I can help to make room for this.
**Riccardo Magliocchetti** 16:44 I don't know if I will have the bandwidth to take over this, but it would be great to have the clarity config in Python.
So, yeah. Like, if you can help, it would be great.
**Alex Boten** 17:01 Yeah, and so I guess I can speak to how the implementation was done in Go. So in Go, what I did is I had originally created, kind of, really small blocks of the implementation to try and move the,
kind of make it easy to review the code. It's also in a contrib package, so it's not part of the core repository, which also helped a little bit.
And so if… if folks here have some thoughts and want to just respond on this issue, that's… that's great too. I can… I can take it from there.
**Riccardo Magliocchetti** 17:39 Thank you. Well, the first thing that comes to mind
Is that, at the moment, we don't have, a concept of a config.
So, like… Every part of code, for example, requires an environment variable.
They do that…
You know, they look at the environment variable name on the environment, on the environment variables.
And so, yeah, it'll probably require quite a bit of work to centralize this.
Yep.
**Alex Boten** 18:17 Yeah, yeah, so the…
I guess part of the reason why, it was done in a separate package in Go, outside of being able to develop it in a way that doesn't destabilize the SDK and the API, was to…
kind of make it an opt-in for end users. So I, you know, like every other implementation, I think environment variables support and the SDK is,
I'm gonna say non-deterministic as a… as a way… as a way of putting it nicely.
So I, I think… Dot… dot…
could be kind of sidestep if this was just another package that people opted into. But again, like, talking about the implementation details, I'm happy to talk more about it, or discuss ideas in the issue.
**lechen** 19:11 Yeah, Alex,
I think this is a great effort, and we would love for you to help out in Python. I think your idea of splitting this up into smaller PRs would definitely
Help us out. I haven't taken a look at any of the…
other prototypes or the spec yet, so I can't really say.
In terms of time commitment, but I think, like, starting fresh would be, like, the best way to go.
I'll comment more on the issue itself.
But… I'm sure we can, we can find some time to help you out, so…
**Alex Boten** 19:50 Okay, cool, thank you.
Appreciate it.
**Riccardo Magliocchetti** 20:00 Okay, I think this was the last topic for today.
Any last, you know, topic?
Nice. Van, thank you, everyone.
And have a nice day, and see you.
At the next sick call.
Right.
**Hector Hernandez** 20:25 Thank you.
**lechen** 20:26 everyone.
