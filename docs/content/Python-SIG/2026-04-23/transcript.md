SIG: Python SIG
Date: 2026-04-23
Duration: 51 minutes
============================================================

## Zoom Recording Transcript

**Riccardo Magliocchetti** 00:43 Hello.
**pabcolli** 00:50 I didn't.
**Surya Teja** 00:51 Colorado, how is your day going?
**Riccardo Magliocchetti** 00:55 It's late afternoon for me, so… like… Closing on my working day already, so… Yeah.
**Surya Teja** 01:05 One more day next weekend.
Hope you're good.
Have some fun weekend.
**Riccardo Magliocchetti** 01:10 Thank you.
Hope you're… you'll have fun, too, as well.
**Surya Teja** 01:15 Yes, Ricardo. Thank you.
**Riccardo Magliocchetti** 01:31 Okay, as usual, we're waiting a few more minutes for more people to join.
And welcome to this week's Python SQL.
And while you're with the more people, please add yourself as an attendee.
To the SIG notes.
And also feel free to add any topics you want to discuss. Thanks.
**Aaron Abbott** 03:04 Hey everyone, how's it going?
**Surya Teja** 03:13 Ricardo.
**Aaron Abbott** 03:17 Hey, Diego.
**Riccardo Magliocchetti** 03:17 Hey, Diego.
**Diego Hurtado Pimentel** 03:19 Hey, how's it going?
You know, oil.
**Riccardo Magliocchetti** 03:22 Yep.
**Aaron Abbott** 03:23 It's alright.
**Riccardo Magliocchetti** 03:25 Yeah.
Always good.
**Diego Hurtado Pimentel** 03:27 for you.
**Riccardo Magliocchetti** 03:28 Yeah.
**Diego Hurtado Pimentel** 03:28 Excuse me?
**Riccardo Magliocchetti** 03:30 Like, how is it going for you, like, Sabine, like… Quite a while, yeah.
**Diego Hurtado Pimentel** 03:35 Oh yeah, totally.
Happy to be back.
**lechen** 03:39 Oh my god, it's Diego. What's up, man?
**Diego Hurtado Pimentel** 03:41 Hey, later. Been alright. How's it going?
**lechen** 03:44 Yo, pretty good, long time will seek.
**Diego Hurtado Pimentel** 03:46 Oh yeah, I went to Harley's…
**lechen** 03:50 Yeah, yeah.
**Diego Hurtado Pimentel** 03:53 So many people. I'm glad that this project is even more popular.
**lechen** 03:58 Yeah, man.
**Diego Hurtado Pimentel** 03:59 Nope.
You guys have made a great job at, bringing new folks in.
**Riccardo Magliocchetti** 04:20 Okay, so welcome again to this week, Python Circle. I think we can start. 16 people.
Please add yourself as an attendee in the notes, and also, if you want something… to discuss something.
Please add any topic.
Also, I think, Jayash, you are the first topic, and please add your name before the topic.
And we can start with the triage.
Okay, well, I should… Mac.
That should be better.
Okay, so one thing before we go through the new issues, I've added a ready-to-merge column, and would like to tie this to, Discriminate between the… staff that are already approved, since we have 49 PRs approved to the staff at, as a maintainer, I mean, going to merge.
And just, like, select… in case, like, maybe, like, the CI failed or something like that, I just don't have to go through all the… the one, and I just have, like, subset here.
Oh, Tammy, I see you're here, maybe you want to… you want to… Present something, or…
**Tammy Baylis** 05:58 Hi, Ricardo. Yeah, I actually wanted to ask about that Ready for Merge column, but that makes total sense, to me, and yeah, that description helps. I'm wondering about the easy-to-review column, Because what's easy to review might be subjective between approvers. I'm wondering if anyone does like this column, or if it's something we could remove.
**lechen** 06:30 I've been using it so far, I like it.
**Tammy Baylis** 06:33 Okay, we'll keep that then.
Then another one, just to try to consolidate, the ready for review column versus Sorry, we have… Reviewed PRs that need fixes, that makes sense. Approved PRs that need fixes.
We'll leave those. Is it… Would it be possible that… so let me see. Sorry, we have some automation in place already, which has been awesome. New PRs go into the first column, no status.
Marking PRs as approved, this is recent, moves them to approved PRs, and then merging or closing of PRs puts them in done.
Is there any way we can automate moving PRs into the… one of the needs fixes columns? Does anyone know?
**Mike Goldsmith** 07:37 Oh, you can… based on a request changes, PR review, you can move it. So we… that's what we've already got set up to… to the, requires changes.
Column.
But I don't think you can do it… so if you approve, but want changes, then it wouldn't know where to put it. So if you, like, approved with suggestions, but you're okay for it to go, it's still going to approved.
**Tammy Baylis** 08:09 Okay.
**Mike Goldsmith** 08:10 So I don't think we've got any automation that goes into approved PRs that need fixes. I don't think we could do that one right now.
**Tammy Baylis** 08:17 Okay, yeah, that's fine. Thank you for knowing that answer, Mike.
**Mike Goldsmith** 08:22 Okay.
**Tammy Baylis** 08:23 Yeah, those are just my board general questions for this week. Thank you.
**Riccardo Magliocchetti** 08:31 Thank you.
And… so we have a couple more minutes.
forfeits a lot.
I'm seeing if we are something new, from last week.
Yeah, I think we have this new line chain, like, this series of 5 long-chain PRs.
Osefing, also Surya did some PR, some Anthropic, and… OpenAI, yeah, this one.
What else?
Again, so… okay, this is new, I haven't seen that.
Okay, interesting.
Okay, well.
Using TI, nice.
Okay, anyone has some peers to highlight, or that you want to discuss?
Okay, well, let's move to the topics.
Okay, like… By the way, like, since we discussed this piece, like, last week, Leighton suggested to… Maybe, like, add a note to what you're working on.
During the week.
Feel free to… add… An entry here.
If you want to share.
Okay.
So, first stopping from, Jayesh.
Are you here, Jayash?
**Jayesh Hire** 10:47 Yes, Ricardo. So, I'm adding this, fleet simplify rules, for roughly, but, what, like, those rules will add a lot of restrictions in terms of, you know.
the kind of, code that will be accepted. Like, if there are multiple, if… if statements which are nested, then instead of those, you can just have, ending of those if statements, and like, many of those rules are there, so I just want to, like, have opinion of other contributors.
Regarding those, like, what, rules, should we… add to this. So, like… I have, in… in those list of rules, I've just, compiled those rules over here in this document. So you can just say, like, add your name there.
And, like, tick yes if you think that rule should be added, and, like, your opinion, if it is, like, if you think, if you don't think that rule should be added, then please type down your opinion there, and your name, Yeah.
**Riccardo Magliocchetti** 12:12 Okay, thanks. Thanks, I see there are… Quite a bit of rules.
**Jayesh Hire** 12:19 So, like, Many of the rules, like, I've decided some of the rules that, I'll be adding, to the ref, but some of them, I need opinions of other contributors.
So, those which, like, those which rule… those rules which are feasible, I've also mentioned them, and if, other people want, like, think that, like.
have some POV regarding those rules also, they can add, their POV there.
**Riccardo Magliocchetti** 13:06 like, from a quick look, like, I don't have strong opinions, but… looks like…
**Jayesh Hire** 13:10 Hi, yes, yes, just,
**Riccardo Magliocchetti** 13:11 Sensible, the default.
Like… The, you know… Does it look where there could be, like, much discussion? Looks like… sensible changes?
Yep.
But yeah, I'll take a look.
Thank you, but, like, speaking of, Adding these, like, models to the rough configuration.
I think, like, the first thing, I should probably review the one to sync the country bank or repo, so we have the same rules in both repositories.
And then maybe, like, we can build from there.
Looks like I think we have quite a bunch of still open PRs, right, from you?
**Jayesh Hire** 14:03 Yes, yes.
**Riccardo Magliocchetti** 14:04 Yeah.
So, yeah, like, maybe, like, before opening new PRs, we should probably just… review and merge the current ones. But yeah, so it's nice that you… But you've done these documents, so we can… Discuss before doing more work.
**Jayesh Hire** 14:24 No, okie, okay.
**Riccardo Magliocchetti** 14:28 Anyone else?
No? Okay, so… next topic is from Jeff.
**Jeff** 14:41 Hello? Okay, can you hear me?
**Riccardo Magliocchetti** 14:44 Yes.
**Jeff** 14:45 Yep, so I'm basically just, wondering, like, I saw that from the, blog post on open telemetry, like, the whole community is, pushing for, like, a stable by default strategy.
But I look at the, stability level in the, Python contribute folder.
None of the libraries are currently market-stable in the, the spec file, so I'm just wondering whether the… there are some certain, like, de facto list of stable libraries out there. For example, like, HTTP instrumentation libraries.
Yeah.
That's just, like, my questions for… That's.
**Aaron Abbott** 15:32 Yeah.
**Riccardo Magliocchetti** 15:33 I'll answer you. Please go ahead.
**Aaron Abbott** 15:35 No, no, no, I want to hear what you have to say, Ricardo. I was gonna say… you know, basically, I don't… I think we've started working on this, and it's something we should absolutely do. There's so much de facto stable stuff that we're allowed to make major version releases of, so we should… should do that and use, you know, the versioning to kind of communicate what's going on. But, Ricardo, please go ahead.
**Riccardo Magliocchetti** 15:59 Now, like, I was going to say that we have a lot of instrumentation that Does not have a stable semantic convention implemented.
I think we have some… PRC open from Tammy, I think.
Yeah, so, like, before tagging a stable release, probably we should at least have, stable cementing convention, I guess, for the instrumentation.
**lechen** 16:34 Yeah, there are definitely some that have… been stable.
For a while now.
So I'm sure we can find some subset of, instrumentations to start Rolling out for this effort.
I'll do the middle, you have your hand up?
**Liudmila Molkova** 16:56 Yeah, I was… Thinking, like, do we… We should have a strategy on how we do this.
Like, do we ship a stable?
Agent… oh, sorry, stable distribution, like Java Agent.
And include everything? Do we include… only stable things by default, do we include everything, but only enable stable things by default, and allow to opt in. I think the stable by default effort, which has not merged the Zotop yet, but the announcement was moving in the direction of Having one distro.
But only enabling instrumentations that are… Stable, by default.
plus having an opt-in flag for unstable, How do you folks think about it? What should we do for Python? What makes sense for Python?
**lechen** 17:57 Hey, Lamila, can you talk a little bit more about the distribution that Java has?
**Liudmila Molkova** 18:04 So what they do in Java, they ship the whole Java agent as stable.
they… don't… Make breaking changes to, telemetry.
They have a somewhat regular cadence, so every once in a while they cut a major release. I think they are surreal for the distribution.
They are allowed to opt in into certain features.
They also recently added configuration options, where you can say, okay, I want HTTP semantic conventions.
like… current, right? If we ever have a new version of semantic conventions, you can Choose between, like, the current version and the future version.
And in both cases, you can have is some experimental flag saying, okay, enable all experimental features. But, I mean, this is the future to start with. We could say… There is whatever current version, and there is an opt-in mechanism, too.
enable all the experimental stuff. But I think what Java does today is not what's written in Stability by default.
And stability by default is not merged.
So I'm interested in your input, in a way, like, as a way to… Make sure we put right things into stability by default.
**lechen** 19:39 Are we in the… Not business, but, like.
The idea that we want to have a distribution that includes all instrumentations?
And the… you mentioned the, there's, like, some opt-in, and then… flags to control, like, semantic ventions. We have that implemented for some instrumentations, but… Definitely, Two things, like, one, we have to apply that for all instrumentations that we think that are popular, or… Wanting to move to stable? And secondly, for… All the, I think right now it's just HTTP right now. So, and… Sorry, what I meant was, like, It only applies to semantic conventions. We don't really have flags to control Opt-in for features, as well.
So, like, I feel like we are missing right now the, the framework even to do opt-ins.
It's just, right now, like, contributors are adding, like, features piecewise.
There's not really a consistent, I guess, guideline, or template that we're following right now, so… I think a lot of those are native as well.
Ricardo, Aaron, I think you want to start this first, And I know we've been talking about it for a while, is there… Perhaps something we can do to start this off piecewise to make it less… Of a… of a cliff.
like a jump, I guess, in effort.
**Aaron Abbott** 21:43 Well, I mean, the only, like.
So because this is Python and we don't really need to build anything, the main thing that we ship, as far as distros go, is there's a package that I think is called Contribute instrumentations All.
Which, tells people which packages are, you know, instrumentations are available, so that one's currently just kind of like a superset.
And then we have, obviously, like, the OpenTelemetry Bootstrap script, which looks at your dependencies and tries to pull stuff in, so… From my perspective, those would be the two places to implement this table by default if we had, you know, assuming all the other work was done.
**lechen** 22:24 But does a stable diaper by default imply, like, we need to have some… Singular place of distribution where all the… the components I'm getting, is promised to be stable? Is that what the… Is that what the incentive of doing that is?
**Liudmila Molkova** 22:43 So I think the court… piece of stable by default is that Customers.
First should have a stable.
Distribution.
And second, that… When we deliver something, when we ship something, it should be… Obvious.
What people are signing up for.
**lechen** 23:07 I see.
**Liudmila Molkova** 23:07 So, if we call it stable, it should… we should treat it as stable. It should not, by default.
change behavior API or telemetry shape.
Well, should not change in breaking manner.
Young Lucas?
**Lukas** 23:29 Yeah, is this discussion just around the instrumentation libraries, or also the SDK? Because I, like, for example, we recently added the… some of the SDK… metrics?
And I'm not sure… I don't think those are stable.
Someone can correct me if I'm wrong.
So, at least as far as the SDK goes, we probably need to add… Some sort of ability to configure feature flags?
With… You know, if they… by default, all the feature flags, at least the experimental ones, would be disabled by default.
And then for the instrumentation libraries, at least, like, with the HTTP migration.
Currently, it's opt-in for stable, although I think we actually changed it now so that you use stable HTTP semantic conventions by default, but… From what I can tell, like, I don't think any of the instrumentation libraries are actually stable.
Which is kind of indicated by their… Diversion?
So… Maybe, like, once… a library, like, a HTTP client is ready, we can… just cut a 1.0 release, and then at that point, that would be… you know, available in the default distro, I guess, so we'd only include 1.0 packages. I'm not sure if, like, that's maybe preferable, or… what others kind of think there, because a lot of packages, they currently don't even support stable, so there's nothing you can really do there.
**lechen** 25:15 I'm wondering if we need to differentiate this stable distro from the already existing, OpenTelemetry contribute instrumentations and bootstrap packages, right?
Like, right now, those have always just been, like, this is the Uber… Uber list of all the instrumentations we get, and you can install all of them.
Or this is auto-instrumentation. Sorry, auto instrumentation, so… there's nothing related to stability, related to these, so… Oh, Lumila, you said the, the stable by default is still in a OTEP, and it's not immersed yet, or…
**Liudmila Molkova** 25:55 It is a nut tip.
**lechen** 25:56 Yeah, not too. Yeah, I… It's not…
**Liudmila Molkova** 26:00 Merged, and is…
**lechen** 26:01 Number?
**Liudmila Molkova** 26:02 Sorry, I hear echo.
**lechen** 26:05 Sorry, that's me.
**Liudmila Molkova** 26:06 Oh, sorry. Yeah, so, it would be cool if we… decide how we want to do this, or at least we have an idea, and we would comment on this hot tab, saying, okay, this is how it would work for Python.
would anybody among maintainers be interested in, like, reading the ATAP through? It's not too big, it's not too prescriptive, there is not, like, low-level details, it's just the directional things, and sharing how it could apply to Biden.
**lechen** 26:41 I'll take a vote.
**Riccardo Magliocchetti** 26:46 Yeah, same, I can take a look as well.
**Liudmila Molkova** 26:49 Awesome.
**Aaron Abbott** 26:52 Yo.
I think there's always the question of, like, you know, whether you use versions versus, like, environment variables to control the stable-by-default experience.
I'm guessing… is that covered in the OTEP wood mill, or is it… is it less prescriptive and more just about the spirit of the… Thing.
**Liudmila Molkova** 27:15 I think it's less prescriptive, but in probably it's language-specific. But I think we should have an idea, and… Once we have an idea.
we should say… comment on that up and say this is how we think it should be done in Python.
**Aaron Abbott** 27:33 Absolutely.
Maybe since we… we all set our piece, like, Jeff, do you want to kind of share your perspective?
on, you know, like, why is this important? What do you think?
No.
**Jeff** 27:47 That's just basically, I'm trying to just say, okay, wanna, like, instrument our customers' workloads, like, using the auto-instrumentation library and build solution. On top of that.
I just want to sort of know, like, what are, like, which library are, like, stable, right? And also according to that, I'm not sure, like, I'm not following the OTEP stuff, I'm not too familiar with that, but just reading that blog post and thought that the stable by default is the, thing that's already happening in the community.
that's just my perspective that I want to just say, okay, that sounds cool to have something, like, stable by default, and I want to know, like, in the Python country, which libraries are stable.
**Liudmila Molkova** 28:31 Yeah, thanks for bringing it up. It's been, it seems it's been a… consistent feedback from some of OpenTelemetry users that we could do a better job.
setting stability levels properly. We don't do it right across Otto, and it's a good opportunity for us to Clean this up.
**Aaron Abbott** 28:55 Yeah.
I think, Jeff, your feedback on the blog post is actually interesting, like, is there anything we can do to… make it more clear the status of the OTEP itself.
**Jeff** 29:17 Oh, sorry, is that a question to me, or…
**Aaron Abbott** 29:19 Well, it was… it was kind of to the… to Lyudmila or to the group. I don't… I don't know if this has come up, but… You know, if that was the root of the blog post, then maybe we can amend it, I don't know.
**Liudmila Molkova** 29:35 And the fact that that app is not merged doesn't mean we… I shouldn't be doing this, but I think we… We kinda… it's… We need to figure it out regardless of the OTAP.
**lechen** 29:53 Aaron, you mean if, like, there are other people that come in and view the blog post, like, would they have the same confusion?
**Aaron Abbott** 30:00 Oh yeah, I mean, I guess so, but…
**Liudmila Molkova** 30:02 Oh, right, you mean the people who use OpenTelemetry? How come we haven't had a stable release of the Destroy in 7 years?
**Aaron Abbott** 30:13 Yeah, I think the spirit still holds, and it's something we should work on, regardless.
So, Zara, while we have you, Ludwoman, we're on this topic, just in the current state of the OTEP, I'm curious if it is prescriptive about things that don't have semantic conventions. Does stable, by default, apply to… All of that as well, so just for example, you know, like, we get instrumentations for, kind of.
for things like async.io and Python, right? Where it's like, this is… this is the async task runtime, and is it okay to mark… mark that as de facto stable by default and say we won't break the telemetry before there's semantic conventions, or do we really need to have, like, a stable semantic convention to be included in the default distro?
**Liudmila Molkova** 31:04 So, according to, well, We can go in a deep level of details, but the purest approach is that N-you cannot.
Break semantic conventions, in the component marked stable.
The… approach people took in the past, that they don't break API, but sometimes they break semantic conventions.
I think if we have an opportunity, if we still can, put… metrics or other things in SDK that we report behind feature flag, that are not stable, we should do it. And it could be one feature flag for everything, at least, to start with.
**Aaron Abbott** 31:53 Okay, yeah, I think we would want to employ Weaver here, because it can be pretty difficult to figure out, All the little places.
Just… just because things grew organically over, like you said, the last 7 years, there's some places we don't have conventions at all, but…
**Liudmila Molkova** 32:10 I mean, oh, you mean instrumentation libraries or SDK? In SDK, it should be easy, right?
**Aaron Abbott** 32:15 Yeah, I know, in the instrumentation libraries. Like, we have a scikit-learn instrumentation, which Leighton always brings up, for example, like, if there's no convention, somebody just contributed it, and something we accepted maybe, like, you know, 5 years ago or whatever.
**Liudmila Molkova** 32:29 Yeah, we should assume everything that we have currently is unstable, and we know that some of the HTTP libraries are closed.
Some of the DB libraries may be closed.
And maybe logging… will be close at some point, but, like, we start with everything experimental. We create a list of things that Or stable, or could be stable, and we… put the target on, like, when do we ship stable distro, and which… what are the things we're targeting for stable distro. Today, it just cannot be done, right? Nothing is stable.
But we can put a target, and something will be stable.
**Aaron Abbott** 33:16 Alright, awesome, thank you, thank you all.
**Liudmila Molkova** 33:21 Thank you.
**Riccardo Magliocchetti** 33:26 Thank you. So, let's move to the next topic.
Agentification.
**Erdenesaikhan Tserendavga** 33:35 Hi, Kurt, yes, I have addressed, comment and answer to open questions. Also, it got, Approse from the, quite the four approach.
Right now, I think it's ready to merge.
**Liudmila Molkova** 34:00 Nice, thank you. Do we need a second reviewer in Python?
**Riccardo Magliocchetti** 34:08 If you read the arrhythmia contributing, yes, but in practice, We merge only.
Most of the time, it's just one everywhere, yeah.
Like, it's fine for the GenA people.
I can take a quick look and merge tomorrow.
**Erdenesaikhan Tserendavga** 34:25 Yes, please.
**Keith Decker** 34:25 I had already revert… reviewed that one. It just looks like it's stale, so all good.
Review it again.
**Liudmila Molkova** 34:33 Totally.
**Surya Teja** 34:35 Yeah, I reviewed it, and it looks good to me, just to… I left a small commit, and the person made the change, so it looks good to me.
**Aaron Abbott** 34:46 Alright, I'll merge it now. Oh, Dylan left a comment.
One minute ago.
**Dylan Russell** 34:54 Sorry, just left one comment.
**Aaron Abbott** 34:56 That's alright.
**Erdenesaikhan Tserendavga** 35:00 Yeah, it's, because of the, based of the, Syncode versions, which we are using right now.
And I'm trying to add all attributes for the… At 3 times from this amount of connections.
**Aaron Abbott** 35:18 I didn't… I didn't… I didn't get it.
**Erdenesaikhan Tserendavga** 35:22 Yeah, because of that, I'm not using the, latest Simato Convention versions, and also I'm trying to add the All attributes from the latest, table.
That's why I was added here individually lectures.
**Aaron Abbott** 35:39 Oh, okay, are you talking about the get adder? Like, Dylan's comment? Yeah.
**Erdenesaikhan Tserendavga** 35:43 Yep.
**Aaron Abbott** 35:44 It's kind of hard to tell without the code, but, maybe we can take it offline and try to get it merged in today. Sound good?
**Erdenesaikhan Tserendavga** 35:51 Sure.
Thank you.
**Aaron Abbott** 35:55 Thank you.
**Riccardo Magliocchetti** 35:58 Thank you.
Next topic is Sriya.
some PRs to review, as well.
**Surya Teja** 36:06 Yeah, I erased a couple of PRs. One is for adding instrumentation around OpenAPI responses create method.
And the other one is, moving the validation in Anthropic use Pytantic.
For strong typing, since, Anthropic uses Pydantic.
janai, folks, if you get some time, and if you can review this, it will be helpful.
And there is no rush on this one. Sorry, I got you.
**Liudmila Molkova** 36:44 I cut you off, I'll take a look, thank you.
**Aaron Abbott** 36:48 Did we discuss this one, like, a little bit ago?
Or it was a different one with something similar?
**Surya Teja** 36:58 the pedantic one, right?
**Aaron Abbott** 37:01 Yeah, yeah, there's another Anthropic PR with Pyntic changes.
**Surya Teja** 37:05 No, no, that was OpenAPI… OpenAI, sorry. Oh, okay. And, yeah, you had the same question, and I discussed on what I'm doing here.
**Lukas** 37:19 Yeah, did we discuss if we want to actually start including Pydantic?
like, obviously, it's a dependency of Anthropic, but if they… you know, I mean, this is unlikely, but if they were to change a version or whatever, then we would be forced to change Right.
**Surya Teja** 37:39 Yeah.
But, right now, I'm taking it… I'm not making it as a hard dependency.
Just leveraging the Pytantic version that is coming in from OpenAI or Anthropic packages.
**Lukas** 37:57 Right, but… still, it's… I mean, I can see this being somewhat brittle, like, I don't know if anyone else has this concern of bringing Pydantic in here, even though it's already included with Anthropic.
Just… At least, like, my philosophy is, like, we should try to keep the instrumentation libraries as dependency-free and lightweight as possible, and not try to depend on really anything else.
I'm not sure if anyone kind of shares, like, what the general concern is here.
**Aaron Abbott** 38:39 Yeah, I… I kind of agree. So, Lucas, is the concern that if we depend on the, you know, the transitive version through the thing that's being instrumented, that it might conflict with the… there might be, for example, an API breakage in Pydentic that breaks the models that we're defining here?
**Lukas** 38:55 Yeah, exactly, and… I mean, that's… I mean, Anthropic might decide, you know, they want to stay an older version, or newer version, or whatever, like… I mean, like… It's kind of, you know, dependent on what the Anthropic Library decides to do, right?
So… I haven't actually reviewed this PR too much, but, like, I mean, how much value is adding… is, like, the pedantic really adding here? That's another question.
**Surya Teja** 39:30 Yeah, that, we are validating the models that are coming in, and they are using Pydantic for, they're exposing their models as Pyrantic, so that is the reason why I am using that over here, and the main purpose is for validating the… Attributes that are coming in from those APIs. But yeah, I do agree that there is… Transitive dependency with… the version coming in from Anthropic, and OpenAI. The reason why I went ahead with this is both of them are using the same kind of vendor for exposing their APIs in Python.
And, they have been using Pyrantic as a stable version, and they mentioned that Pyrantic is a version that they require, or as, they need as a dependency if you want to use this, use these APIs.
In, your, codebase.
**Aaron Abbott** 40:35 Can we take a look at the code really fast? Because I'm having a hard time understanding what the… So, where do… so, for example, like, the, Message request params, can you search for that in this file?
It's, line 97 there, you just kind of search for it.
Maybe that's not a good example, because it seems like it was already in here, but it was a data class, and we're moving it to Byte Intake, is that right?
**Surya Teja** 41:27 Yeah.
**Aaron Abbott** 41:29 Okay. Yeah, I mean… I kind of am also a little fuzzy here, like, if we're given a Pydantic instance through the thing that we're monkey patching, can we just use that instance instead of redefining the models?
**Surya Teja** 41:44 I think we can do that. I haven't explored in that way.
**Lukas** 41:50 Yeah, I would be in favor of that approach. Like, I would say, if we can avoid… like, I'm not totally against it, but if we can avoid having to do any pedantic imports.
That would be ideal here, just from a maintainability perspective.
**Surya Teja** 42:08 Okay.
Yeah, that makes sense.
let me rework this a little and see how I can use those models directly and avoid using Pytantic. So let me close these and, reopen after making the changes then.
**Aaron Abbott** 42:29 Cool. Lucas, would you mind just dropping a comment here, just.
**Lukas** 42:33 Yeah.
**Aaron Abbott** 42:34 Bookkeeping. Cool. Thank you.
**Liudmila Molkova** 42:38 And so yeah, remind me, I think this is what we've done in OpenAI. We didn't use identity because of dependency in… Opening air.
It was only a test dependency.
**Surya Teja** 42:48 Yes, we were using it as a transitive dependency and not making it as a hard dependency.
Initially, I made it as a hard dependency, and Ricardo recommended using the dependency that was coming in from OpenAI, and I moved.
I removed that, but, let me… that… if we are not using Pydantic over here, it means I need to rework a little bit on OpenAI stuff also.
**Liudmila Molkova** 43:20 awful. Thank you.
**Surya Teja** 43:24 No worries, thanks.
**Riccardo Magliocchetti** 43:38 Thank you.
So, if this was, like, The last topic for today?
And then also on added a new line here.
Okay, it's… Comment? Okay.
**Liudmila Molkova** 43:52 Yeah, it's me, I'm typing. I wanted to get your, yay or nay, I hope we could have merged it. Sorry, I cannot… Change the lay… level of… this for some reason. So I've been adding the AgentsMD And, copilot review instructions to help us review instrumentations, most of the GenAIPRs, but I've got feedback that it would be cool to add To share some parts with all instrumentations.
I have some approvals, but I think… and, like, I would appreciate more eyes on this. Otherwise, it should be ready to go.
GitHub is very… unstable today, I wasn't able to make it green, but it doesn't seem to be related, so I wanted to ask to merge, but we cannot really merge anything.
Or maybe now it will pass.
Yeah, it looks like it will pass now. Anyway, so I would appreciate it merged, or if people want to take another look, please go ahead.
And to those who haven't seen, the Agents MD, or for the altering Stuff.
And they would include some best practices, I hope, that we develop over time.
For GenAI. And the Copilot instructions are for review is Copilot, so if you have access to Copilot, or maybe we even have it from the CNCF perspective now.
You can… assign PR to the copilot, and it will do the first pass of, let's say, assessing that it follows semantic conventions.
And some other things.
**Aaron Abbott** 45:55 Okay. Yeah, my impression is we should just, like, merge it, Because we can kind of iterate on the instructions, right? Like, there's… Like, what would a reviewer look at here, anyway?
**Liudmila Molkova** 46:10 I mean, I don't know, but, but… Okay. At least you know what, what is… how to assess the future copilot reviews, whether they got better or they got worse, if it was addressed or not. Anyway, I think this is something that's very cheap to change after, it does not affect users at all, and if we just merge it, we can always come back to it and, I don't know, burn it if we don't like it.
**Aaron Abbott** 46:38 Yeah, exactly.
Well, I could ask you to make, like, an eval suite for this.
**Liudmila Molkova** 46:44 But… Aaron is a judge.
**Aaron Abbott** 46:47 Heh, yeah.
Okay, cool, thank you.
I'll burn it.
Yeah, agreed. Okay.
**Riccardo Magliocchetti** 46:59 Okay.
So… This was the last topic? Yes?
Thank you, everyone.
Rabusti.
**Liudmila Molkova** 47:12 Thank you.
**Aaron Abbott** 47:13 Peel. Bye.
**Mike Goldsmith** 47:15 Thanks, Al.
**Surya Teja** 47:16 And that's the case.
**Diego Hurtado Pimentel** 47:17 Whoa.
**Jayesh Hire** 47:20 Thanks, Holo.
