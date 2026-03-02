SIG: Specification SIG
Date: 2025-10-21
Duration: 63 minutes
Zoom Recording URL: https://zoom.us/rec/share/grTgw03OZSoUWkVbv5rQkhY_V9YN40IvsUrM-nwpE3gDYOvl6vY32K4SMkBkO68I.mIJ9CbqGccekyBjm
============================================================

## Zoom Recording Transcript

Reiley Yang 00:03:02 Hello, Austin.
Austin Parker 00:03:05 Howdy.
Liudmila Molkova 00:03:56 Hi, everybody.
Reiley Yang 00:03:57 Era. I don't know.
Give 2 minutes for folks to join.
Hey, Todd.
Ted Young 00:04:14 Hey, what's up, yo?
Reiley Yang 00:04:21 Yeah, let's give one more a minute while folks will join.
Hey, Era, thanks for joining. Let's get started. So, Austin, you have the first topic.
Austin Parker 00:05:22 Yeah,
Not a lot of maintainers on yet.
But I wanted to… Take some time at the beginning to talk about,
The graduation process and a few of the…
Sort of what we've gotten back from,
The Technical Oversight Committee at the CNCF.
And we'll be… there are some comments, actually, let me put the link to the graduation issue so that people can see the public.
Comments… But there was…
The short version is, is, you know, while the project overall, you know, is in a pretty good spot with things like governance and
So on and so forth. There's… Some concerns from adopters… about…
The quality of, releases, and… Now… That's a…
There's a lot that goes into that.
And the first reaction, you know, is very… it's like, well, you know, what… what do you mean?
And when we dig into it a little bit, and we kind of, you know, look at what specifically people are talking about, a lot of it comes down to…
Sort of this mismatch between the perception,
of users, and sort of the reality that we try to codify through all the various things that we say about stability, right? Like, if you're familiar, you know.
we have, I think, a very comprehensive way to describe, like, the expected stability of components, or, you know, the various quality bars, and so on and so forth.
But… that doesn't necessarily… Make it to, the purview of, sort of, an average adopter.
To be a little more flip about it, like.
right now, you know, if you want to get started with OTEM, and you want to really understand it, there's a lot of required reading.
And people… Broadly, don't read.
We have, you know, a ton of information, and we've done a very good job about documenting things, but making that documentation accessible and making it obvious to people what exactly they're getting is…
Not necessarily, something that we have done a great job of, I would say.
So, one of the things, you know, some of the feedback we're getting is definitely on the lines of, like.
hey, you know, I installed this thing, or took this update, and that caused a performance regression, or that broke my config, or da-da-da-da-da-da-da. And in a lot of cases, when you dig down deep, you find it's like, okay, well, you were relying on some unstable thing that we said was gonna change.
you know.
And it's not enough for us to say, especially as we kind of want to move… as we want to make the project more mature, it's not enough for us just to say, like, well, you should have read better, right? You should have just…
You know, done a better job.
So…
to help ameliorate this, and I also want to say, like, this is not… I don't… I would hope that what I'm saying is not a surprise to anyone.
I think that…
you know, one specific thing that was brought up is that it's difficult for people to understand, like, the, you know, the way we talk about OTEL, right? We talk a lot about the things we can control. I'm on the spec call, so let's talk about the spec. The spec has a lot of things that are stable. And we will go out and we will message around, like, hey, we stabilized this thing in the spec. And…
But if you look at, like, what is the actual, like, implementation of this in the SDKs, or in the API, or at various other levels of the project, like, it doesn't really match up, right? And I understand why we do this, and I'm as, you know, if we're gonna start
taking… being accountable, like, yes, I'm as guilty of this as anyone, we will go out, you know, at KubeCon or during these big marketing things, and say, like, yeah, hey, we've stabilized this thing in the spec, and we don't necessarily, like… we assume a lot of familiarity with what that means.
And then through the game of telephone, you know, it turns into, like, oh, blah is stable.
I should go use blah, and that might not actually be the case in, like, PHP, or Ruby, or…
or Web.js, or whatever, right?
Does this, just before I continue, does that, like, mostly tr- do people feel like I'm being…
This is not supposed to be just me telling you things, this is… I do want this to be a kind of a discussion with, the people that are here.
But does that sound… does this at least sound like I'm… In the realm of realism.
Reiley Yang 00:11:19 Yeah, and I remember the discussion, so one feedback is people are saying, yeah, we understand, like, the stability status of each component could be different, but there's no central place for the user to understand. It's just scattered all over the places and in an inconsistent way.
Austin Parker 00:11:36 Yeah.
Reiley Yang 00:11:36 Most users, by default, they would assume this product is, like, widely used, will just take something. So, one suggestion might be great to have a central place.
to encourage consistency. And we show the example to the reviewers, the spec, like, compliance metrics. So, one possible idea is we'll have the component-level stability guarantee organized in similar fashion.
Okay, Pat.
Austin Parker 00:12:07 Yeah.
Ted Young 00:12:09 Yeah.
One random note before I get into what I want to say, is that there is actually one place where we may have gone too far in the opposite direction, which is not declaring instrumentation stable
Because we think that the telemetry, it emits might change.
That seemed very, very important to us, but we've been getting, actually, feedback from users that they perhaps misinterpret what unstable means.
And often organizations have rules in place where they aren't allowed to deploy anything that's in a beta or unstable place. But if they understood that what we meant by unstable was simply that the telemetry might change, there might be a major version bump, and you might get different telemetry.
That would actually… they would…
be more aggressive about installing these things, because they interpret it being marked as unstable as meaning that it might break or explode or cause an error in their app.
So there's some places where we've overclocked the other way.
But the bigger thing, to my mind that I've gotten from a lot of end users trying to install OpenTelemetry is we've been on kind of a dead run just to get all of the features in across all of these signals, for years, just trying to get all of the signals in and stable. And we've kind of done that.
But something we delayed along the way was kind of productizing open telemetry, is the best way I can think about it. So there's a lot of low-level details that often get presented to you as an end user, like providers and registration and all of these things.
Austin Parker 00:13:48 I hope to clean a lot of that up using the config files.
Ted Young 00:13:55 But… but it's not just that things are unstable, it's that the stable things aren't necessarily, like, packaged up in a way where you can just easily install them without first having to learn quite a bit about how OpenTelemetry works under the hood.
Austin Parker 00:14:09 Yeah.
Okay, so I… what I… Wha…
So, adjusting this is not going to be a thing that we can stamp our fingers and do overnight, right?
But… what I… what I'm…
What we are going to do, what we are going to commit to doing, is start
is start doing the work to, like, steer the ship into a different journey. You know, we're gonna start steering the ship in a different direction with all this. And I don't want this to be, you know, this isn't supposed to be, like.
no, bad, you've been doing… you know, this is not… we're not smacking anyone's hand, and we're not trying to tell people they have to change how they're doing things.
What we want to do is we want to, you know.
We want these changes to kind of work like any other change, and be, you know, go through the normal process, so…
there's, I think, right now, 1, 2, 3, 4 OTEPs that we're… that are gonna be proposed, that kind of each handle a different
that are related… And they each kind of cover a different part of this.
And I, you know, I strongly encourage people to, you know, provide feedback on those OTEPs when they go up. It'll be within the next… the goal, my goal is to have… I think our goal, I should say, is to have those OTEPs done by…
Are those OTEPs posted, drafted by HubeCon in a few weeks.
This is the goal, so that we can talk about them in person, but obviously, you know, we're not…
Tying it to that, it's just we want to be able to have them done by them.
Right now, the…
topics for each of them, broadly. One is going to be updating stability guidance, extending and modifying OTEP 143 and 232.
This is probably going to be the most ticky-tacky one, just for reference, 143 and 232 are the versioning and stability documents that kind of define our whole system of things.
there's a lot of, like, shoulds in there, and this is gonna turn some of those shoulds into musts. It's also going to… like, the… the…
Four big points right now that we're thinking about is, one.
Adding specific documentation requirements, to… Stability, and also defining Where documentation must live.
user-facing documentation. Another clarification is going to be around
The… specifically having the idea that there is end-user documentation, and then there is developer documentation.
Developer documentation strictly refers to what do you need to know to make a
to modify the underlying source code here, or to make a PR or whatever, and then end-user documentation is sort of everything else, more or less, and the end user documentation has to be discoverable, it has to live in the website, can't live in GitHub anymore.
There are… some… You know, there's… Again.
Nothing is final, but, you know, one of the big, big things we consistently hear is that
like, the GitHub documentation, or even Easter stuff is just very undiscoverable, and I know that, like, some SIGs are already working on this, or have already done this in a lot of ways.
And also, these, I should also point out, this is not an unfunded mandate. We…
We'll be able to… Get… Probably…
More assistance with documentation, if we can kind of point to specific things to do?
But yeah, that's one. Another is gonna be, explicit guidance around performance and compatibility. Again, this is…
Making some of those shoulds into musts.
Another is going to be kind of defining this new idea around
Stable components versus unstable components, which is really just putting a wrapper on some stuff we already have, but the idea is that things that are beta or better are stable, and then, things below that are unstable.
And then also, we're gonna prescribe a metadata format for reporting stability and all this stuff.
across every SIG, so that we can actually have tooling to… Sort of help with this?
The second OTEP is going to be very… is a much smaller one, it's very related to what I just said, though, and it's going to be, perhaps the more controversial one, which is a new default for, stable artifacts. And the new default for stable artifacts will… of any kind will be that they can't
automatically enable unstable artifacts. So a good example of this is, like, the Java…
Java Instrumentation agent would not be able to, by default, import a…
or enable an experimental or an alpha instrumentation library without a specific, like, flag to be passed via config or MVAR or whatever.
This would also apply to the collector, once the collector has A stable release.
Antoine Toulme 00:20:01 Is that the case today?
Austin Parker 00:20:03 The case… that is not the case today, no.
It's also a little… It's also something that we don't necessarily prescribe at the… Project level?
Antoine Toulme 00:20:17 Okay. No, we've… for $1, with the collector, we've been very good about, having no API dependencies, at least, between stable to unstable, which has… which is why the collector's been working on $1 for two years.
Austin Parker 00:20:30 I understand that, and this is more…
there's… the collector's a bit of an odd duck here, but this is really more about, like.
I guess a better example of this would probably be stuff like, web?
WebJS, where…
Antoine Toulme 00:20:52 Nothing is really stable.
No worries.
Austin Parker 00:20:55 The way it's packaged and presented kind of… doesn't line up with that.
Antoine Toulme 00:21:00 Okay.
Austin Parker 00:21:00 This… it doesn't… and I will say, like, this is not necess… this is… this is definitely one of those perception over reality things, right? Like, the reality is we are very good about separating unstable and stable stuff. But the perception that people get is.
A good example here is the operator. People will just be kind of guided into, like, oh, you have Kubernetes, so go install the operator, and the operator brings in collector contribib. And the operator is technically…
Antoine Toulme 00:21:28 Okay.
Austin Parker 00:21:29 stable, right?
Antoine Toulme 00:21:30 What? But…
Austin Parker 00:21:32 In… Helm charts? Are they 1.0?
Antoine Toulme 00:21:40 stomped me here, but I don't… I… I… the operator is not, does not portray itself as stable, but, maybe it could be more evident, for sure.
Austin Parker 00:21:51 Yeah, either way, again, this is a perception thing. The perception people get is like, oh, I installed this thing, someone told me to install, and it was good, and then I took an update, and this other thing, and this thing that it brought in changed configs, or broke, or something, right?
Antoine Toulme 00:22:07 None of you have charts at 1.0 for what it's worth.
Austin Parker 00:22:10 the Helm charts are or not.
Antoine Toulme 00:22:11 No, they're not. Okay. None of them are. I mean…
Austin Parker 00:22:16 Also, I should also point out again, people don't read.
Ted Young 00:22:18 Just for time. Can… can we maybe get out of the weeds?
Antoine Toulme 00:22:22 Yeah, we can discuss all this on the OTEP. The last two are…
Austin Parker 00:22:29 to what Ted just said, one will be updating stability requirements of instrumentation, libraries and components with respect to semantic conventions, so this will be…
Changing the definition of stable for simconf.
And the last one will be, we would like to start doing… Project-wide releases?
And having a project-wide release SIG.
Similar to what Kubernetes does, and the idea there is that there would be quarterly, or three times a year, or some… on some regular cadence, there would be a
official, stable, tested release of OTEL that we would stamp and say, okay, this version of OTEL contains all of… here's a manifest, all this stuff is in it, all of it has been tested, it all works together.
You know exactly what it is,
Yeah, those are the four OTEPs. Again, we can discuss and debate and argue about them.
in the PRs, but I do want to leave a little bit of time for questions or discussions on this point.
Before we move on.
And if there's no, and if people just want to wait until there's things to argue about in the PRs, then that's great too. We can do it async.
Antoine Toulme 00:23:53 release…
do you want a separate, really, SIG? Is that, like, a SIG? Do you want to make a proposition for that SIG? Is that a part of an OTEP, or is that not? That should be an issue under community, right?
Austin Parker 00:24:04 It's… I would like for it to be… I would like to discuss it as an OTEP, because it is a…
Antoine Toulme 00:24:10 Okay.
Austin Parker 00:24:11 project-wide… policy change.
Antoine Toulme 00:24:15 Okay.
Trask Stalnaker 00:24:18 So, I think this is what you said, but I just want to clarify, that the semantic convention stability requirement would go out the window for stable instrumentations?
Austin Parker 00:24:34 I… think… I, I…
Trask Stalnaker 00:24:38 if I can give some context there for the Java agent, for example, it has no public API, so that's why we were more aggressive in declaring it stable.
but if we could only enable things that had stable SEMCOMs.
I think there's two issues there. One is, there's way too much unstable SEMCOM currently.
And B, and the second issue is, I think that would create a crush on the semantic convention SIG of
people… I mean, maybe it's a good crash in that we want people to care about some calm stability, but we've said that for so long, and it hasn't happened.
Austin Parker 00:25:27 So, I… I wanna just… So, my thinking right now, and I'm certainly willing to…
Trask Stalnaker 00:25:32 Is there one last question.
Austin Parker 00:25:33 Oh, yeah, so…
Trask Stalnaker 00:25:34 Yeah. That, I'm not saying that… I wouldn't expect
I think we can still say that they have to treat telemetry stably, meaning if you… you still have to follow the breaking telemetry conventions, that if you break telemetry, you need to do a major version bump.
But the only thing that I'm asked… that I'm…
would… don't want to… that I would like to see us throw out the window is tying it specifically to CEMCOM being marked stable.
Austin Parker 00:26:09 So… right now, and again, we… none of… nothing is written in stone. My thought is that we could…
be a little bit more aggressive about marking… about saying… it goes back to what I said about saying, like, okay, the bar for stable is beta, and being more aggressive about pushing some comms to beta.
Ted Young 00:26:33 Yeah, I think… I think we want to potentially just look at separating how we communicate semantic convention telemetry stability versus stability of, like, like, packages, like code… code stability.
That's… and I'm not saying there's one right answer to this, but it's maybe something as part of stable things and unstable things not relying on each other.
Conflating telemetry stability with the stability of the instrumentation package is just a thing we want to look at, and just discuss whether… is there some way to maybe separate those two concepts, rather than having them conflated.
Because we're getting feedback that end users are misinterpreting what we're saying, and… On that front.
Austin Parker 00:27:21 I… I also should just point out, one goal with this… Is to better…
Be able to drive contributors to, sort of.
project priorities, and being able to… like, not for nothing, like, I…
And I think, Ted, you're gonna talk about this next.
But not for nothing, but, like, there's a lot in OTEL, right? And the… and the amount of stuff in OTEL keeps increasing rather than decreasing, and I don't think it's… like, I don't want us to say, like, oh, let's cut scope, because I don't think… I mean, because our scope is definitionally huge, but I do want us to have
Better ways to be able to push contributors Towards, like, overall
What needs to be done, and make it easier for maintainers to kind of make their work interpretable to both the rest of the project
To contributing companies and individuals, but… and also to, like, end-user adopters.
And right now, I think that's really… I… the feedback I get is that it's very challenging.
for… external orgs.
And I think we could talk for an hour specifically about this thing alone, and so I don't want to, because it would go into a lot of directions.
But a goal of this is to be able to…
Both loosen up stuff… like, shake some stuff loose, but also tighten some other stuff up, so that it's possible for, you know.
people to kind of pile into productive… to highly productive or high-impact directions, rather than, like, being very diffuse.
Josh.
Josh Suereth 00:29:17 Yeah, thanks. I think… sorry I missed the early part of this discussion. I was at, had a doctor's appointment, but,
I want to make sure that we all understand one key thing that I think we all implicitly know, but is, like, made clear with what the tag told us, which is.
If you are using OpenTelemetry today, practically, you are engaging with unstable pieces of OpenTelemetry. I am not aware of anyone who's successfully using only our stable components and getting the observability they need.
Like, let's just acknowledge that, right? They're either engaging with unstable SEMCOM,
They're engaging with collector contrib pieces, which are not mark-stable. Like, there are unstable pieces of OpenTelemetry that are necessary for people to be successful with OpenTelemetry. And one thing I don't want to lose in this discussion is we should be finding a way to get those things to a point of stability for our
people who use us, right? And I think some of this is we might need to commit to interfaces before we're sure they're not going to change.
And we're gonna have to lean harder into evolutionary changes.
for those components.
Going forward, that we were unwilling to do before. And I think that that has been holding back our community a lot with stability.
One example is in chat, this discussion around semantic conventions. I'd love to get to the point where we are okay if you publish your own convention as, like, a collector-constrip thing, of here's what I produce, and you have a notion of stability that we can share for that thing.
And then eventually it gets into SEMCOM, and that might be a breaking change or, like, an opt-in thing, but we're okay with that because we can give users a stable interface they can rely on through that whole process, right?
And I want us to make sure we're focusing on that aspect of it. So it's not just like, you know, there's a bit about documentation, there's a bit about stability, but the key thing to remember is, if you are adopting OpenTelemetry.
Think of the unstable components you need.
To make it successful, and how many of them there are. And let's start knocking those out.
Austin Parker 00:31:30 Yeah, like I said, I think the…
I think being able to set the bar and say, like, okay, we think things that are beta quality, you know.
The beta is stable.
for purposes of being included as kind of, like, the core part of OTEL. And I think that gives us a lot… it makes a lot of… it makes the problem much more interpretable, because it lets us be able to say, for example, okay, here's the things that are actually not beta.
Here's the things that we actually have, like, super high confidence in, and then we can make a list of the stuff that's like, okay, this is all the necessary things that are unstable, but, like, people are using them. They're, like, they're literally beta quality in the sense that we've reserved the right to change them.
But functionally, the functionality is there.
And that doesn't mean that there aren't problems, but we can make that clear, and then we can say, okay.
now let's drive towards getting those things, like, let's improve those things, right? Rather than sort of right now, which is we have this huge undifferentiated mass of, like, well, everything's unstable, everything could be broken.
I think the biggest thing is, you know, answering that question,
And to Ted's point, thinking of hotel a little bit more like as a product.
Like, thinking of it a little bit more, like, rather than this diffuse collection of…
Specs and components and whatever.
you know… I, I, speaking personally, I… I… when we started, you know, when OTEL started, I think
I always perceived… that… There would be more,
That more people would implement the spec.
there will be more competing SDKs.
And… I think… you know… That hasn't happened.
We can argue if that's a good thing or a bad thing.
Daniel Dyla (Dynatrace) 00:33:40 That's not the case, at least in JS. There's, like… I'm aware of at least 4 or 5.
Implementations that we don't control.
Austin Parker 00:33:51 Yeah, but that's, like, kind of the exception that proves the rule, isn't it?
Ted Young 00:33:56 People…
Daniel Dyla (Dynatrace) 00:33:57 say it's… What is the exception that proves the rule even mean in this case? It's competing implementations, you just said they don't exist.
Austin Parker 00:34:06 They don't eat…
Let me rephrase it. The expectation I had would be that each vendor would basically have their own distribution.
Daniel Dyla (Dynatrace) 00:34:17 But what vendor would want to re-implement the SDK? The whole point of all the vendors contributing to the SDKs was to not have to do that.
Austin Parker 00:34:26 we're off. We're off topic.
Ted Young 00:34:31 super often.
Austin Parker 00:34:32 But I mean, again, like, if the…
if the end thing is, like, okay, it is just gonna be, like, we're gonna be responsible for all of this, then I think we need to think of it more like an actual boxed product, as it were, and, think about how we're building OTEL and delivering value to end users along those lines.
Ted Young 00:34:57 So… I'd like to maybe call time a little bit, or at least transition into the.
Austin Parker 00:35:05 Yeah, I think
I will say, on the OTEPs part, we'll get the OTEPs out there, people can chime in, and we can hash all this out in the comments. I appreciate your all's patience and the discussion this morning.
And… you know.
I also, I just want to say, because I've said it every time I've said this, again, I don't think you should take this as a reflection on the work that you have done, regardless of your role here, as a spec maintainer, as a SIG maintainer. I think
We are doing an awful lot of really good stuff.
I think we have, as a project, a extremely high bar for quality.
I think we are kind of coping with an almost impossible situation at times, but, you know, we're…
We are all doing a really good job, and everyone deserves a pat on the back.
for their contributions. So please do not let this… do not take any of this as a reflection on the quality of what you've done, or your… your…
Personal self-worth or whatever.
I think you all are doing great.
Reiley Yang 00:36:16 Okay, thank you, Austin. Thanks, Aaron, for discussion. Ted, do you have something to add, or you want to move to the next topic?
Ted Young 00:36:22 So, the next topic is the one I added, just a follow-up to this. So, we've talked about, like, the kind of changes that we want to make, which is…
But the next question is, is how, as a community can we do that? And one of the things we've learned a lot over the years is we can't focus on everything, everywhere, all at once. When we try to do too many things at the same time, everything starts to go slow because we're context switching.
Across such a broad surface area.
So, a question for the maintainer community, and I really want feedback here, is,
we've been basically focused on shipping features, right? We needed to finish the spec out for tracing metrics and logs, plus a bunch of auxiliary things that come along with that, and so we've been shipping features hard for years.
And to my mind, that's why we haven't focused on, kind of, productizing things, cleaning things up. We've talked about that stuff
A lot.
But a question I have is, if we're going to switch to focusing on that, what can we do to help maintainers maintain that focus?
Is it helpful to, for example, put a explicit freeze on spec features in some way? Do maintainers feel like there's still a backlog of spec features coming at them like a fire hose that's keeping them away from doing this?
Or are there other ways we could do just sort of cross-sig, some kind of, like, cross-sig open telemetry motion to kind of help people push?
Together, so we can communicate with each other.
Basically, I think we need, focus. Focus is helpful, but I really want feedback from end users and community members about, what kind of focus they would find helpful.
I see a bunch of hands. Daniel?
Daniel Dyla (Dynatrace) 00:38:15 Yeah, I guess as a maintainer, I was vocal in the past about the firehose of spec, making it difficult on SDK maintainers. I would say that that has…
Alleviated a lot recently, just because the spec doesn't change nearly as much as it used to.
We've completed a lot. I know that, at least in JS, I assume this is true in all SDKs, or most.
We do not have a complete implementation of the spec, but it's not because of the fire hose, it's because our users don't ask. Like, we implement what our users ask us to implement.
And…
That's how we prioritize our backlog, and there are specified features that are stable that nobody asks us for, so we don't get to them.
And… we… You know, it's difficult for us to prioritize the roadmap
Buy anything else, because the only feedback we get is when people come and open issues on the repo, which a very limited number of end users do.
And then you go to a conference and you hear people talk about how this or that is missing, and it's like, well, you never told us that you needed it.
I think there's a… a missing…
Line of information from what users need implemented.
I don't know why, they just… they don't ask for it on GitHub, and there's no… communication from…
the GC or TC saying, like, these are the features you're missing that need to be implemented because users need them.
We have no way of, like, prioritizing our backlog beyond the information we get, and we just get a very limited amount of information. I know from being on the GC, the GC also gets a very limited amount of information. That's why I'm saying that there's a broken…
information inlet somewhere that, isn't being used, or doesn't exist, or something along those lines.
Ted Young 00:40:32 That's… that's great feedback. Yes, there's…
The case that in every language, you know, feature implementation is spotty, and we do get, like, when we go out there and rustle up feedback from end users, like, when we actively go out there and track end users down and ask them, they will sometimes point this out.
Right? That there's something available in one SDK, but it's not in the other one, and it's confusing to them.
What's available where.
But given the staffing levels are so different amongst all the different SIGs, saying that we all have to
Shift the exact same feature set seems difficult.
So, that's good feedback.
Maybe we can think about how to better communicate that with our end users, or better get that feedback from our end users.
To that end, there's OpenTelemetry Unplugged in Brussels in February as part of Fostem. I put a link to it in the docs, so this will be an opportunity to meet end users.
Trask?
Trask Stalnaker 00:41:43 How much of what we were talking about the first half hour is about SDKs, though? Like, it seems to me the more the problem areas tend to be more around instrumentation, semantic conventions, collector…
I feel like focusing on the SDK is…
Ted Young 00:42:05 I can give some nuance there. So, when people talk about the SDKs, it tends to be more,
things being difficult to install, in the sense that in every language, there's a different way to install it. We have, like, a broader issue, which is
you have to be an application developer to install this stuff right now. A lot of competing products in this space use some kind of injector mechanism, so that an operator can install all this stuff.
We actually have spun up an injector SIG to start addressing that problem, and we'll be talking to different SDK maintainers to figure out how to clean that up.
But the confusion there is still more around actually installing the instrumentation. Like, if all people ever had to do was install and stand up the SDK, it would be a very normal task.
But you're right that, like, what makes it all tricky is this matching game of trying to figure out what instrumentation you need, and, like, getting that stuff installed, and whether that stuff is stable.
and maintaining all of that Contrib stuff, I think that's the part where we struggle as a community, because that's where the surface area just gets so vast.
Austin Parker 00:43:21 Can I… on something to this too, Ted.
The other point, which makes this even worse, is that…
Typically, yes, it's exactly what Ted said. But then, there are people with…
Very high… very, high perform… like, very stringent performance requirements?
that, for a variety of reasons, like, the SDK itself maybe isn't great.
Ted Young 00:43:55 Get feedback on performance overhead in a lot of languages.
Austin Parker 00:43:59 Right, and like.
Ted Young 00:44:00 Not something we have traditionally focused on. We've focused on shipping people a flexible framework, not a performant one.
Austin Parker 00:44:07 Right, and so… but, you know, it's like…
In a large enough org, you're gonna get, like… and this is kind of the interpretability problem.
in a large enough org, there's going to be 5 different, you know, there's some people that need what Ted says, right? They need the… you know, they're just trying… they don't care about any of this stuff, they just want to push button, receive observability. There's people on, like, ML teams that…
are super annoyed at the overhead of OTEL, you know, We… we're…
We're so many different things, it's hard to meet all of those things, and…
The broken inlet from the vendor here is that
The vendors aren't necessarily looking at it holistically either.
In a lot of cases, they're looking at it like, well, I'm trying to sell into X team, And…
Oh, hotel doesn't work? Okay, then we… fuck fixing hotel, we just… we need to make the sale. We need to close the deal, so we're gonna go find, like, option B.
Ted Young 00:45:10 So to that end, I think I want to wrap this up and hand the whole conversation over to Pablo. Pablo, I see you have your hand up, but I know we also want to pivot to the rest of the meeting topics, which I think are yours.
So…
Pablo Baeyens 00:45:25 Yeah, so I had my race… my hand raised just because I wanted to mention one piece of feedback that I've heard.
consistently from several SIGs is, like, we don't know how to say no to contributions, and, like, I feel like maybe…
even a spec freeze would not necessarily reduce the amount of work that maintainers have to do, insofar as people are going to keep coming with PRs for…
Ted Young 00:45:53 Yeah. Bespoke.
Pablo Baeyens 00:45:55 Things?
Ted Young 00:45:56 Even amongst what we just said, right? If we're like, we're gonna do a spec freeze, but now maintainers need to focus on stabilizing instrumentation packages, improving the installation experience, and improving performance.
saying focusing on those 3 things doesn't actually sound like focus to me, right? That's an enormous mandate, to say, do all 3 of those things at the same time.
So even amongst those things, I kind of have a question of, like.
Would it be helpful to maintainers if we tried as a community to just, like, take them down in order, rather than say, go pick from this grab bag of priorities?
Pablo Baeyens 00:46:38 I definitely feel like some kind of project-wide messaging on, like.
maybe we won't respond to your PRs if we're not related to the score areas within the next, whatever, many months.
Ted Young 00:46:51 Yes.
Pablo Baeyens 00:46:52 the tube.
Ted Young 00:46:53 If we can be more… something we've found in the past, the more organized we get, the easier it becomes to say no, because users can get a sense of, like, we're not saying no forever, or for arbitrary reason, we're saying we're focusing on X right now, and we'll get to Y, you know, like, in 6 months.
Then people can be more understanding about, like, why we're not focusing on why right now.
But, this is all food for thought. We've got 15 minutes left. We're definitely gonna keep talking about this, so maintainers, please, please, you know, let's discuss this in the maintainers Slack channel.
And figure out, we definitely want feedback from people about different ways to approach eating the rest of the elephant that we have to eat now that isn't features.
And on that note, I'd love to hand this over to Pablo to talk about the collector specifically.
Pablo Baeyens 00:47:48 Okay, yeah. So, I am bringing back a topic that we discussed on January. I…
don't know that we need to make any decision on this meeting, but I wanted to talk about why I'm bringing it back. There's…
Three reasons, basically.
So, one of them is, we got a comment on that issue from an end user, and…
like, that's something that we were hoping to have. I don't think a single comment is… is useful enough, but, just…
Kind of sparked me into thinking about this.
Yeah, I'll send it on the stream chart.
The second one is, the declaratory configuration is nearing, 1.0 version, and there's one field called disabled, that, is going to be…
Part of the 1.0.
work, and so I think it's fair to ask the question of.
Daniel Dyla (Dynatrace) 00:48:55 Like, do we want to do disabled or not?
Pablo Baeyens 00:48:58 And lastly,
And I realize maybe I should have given you some context in case you were not here on the January meeting and don't know what I'm talking about, but…
If you read the issues.
I hope fairly simple to understand.
Lastly, I'm working on a collector change to, enabled in a bunch more places, and I don't want to make this…
division between the collector and the Java instrumentation versus
the spec stuff, on choosing enabled or disabled, wider, if I can. So, I don't know, I wanted to bring it up here in case
we can think of a way to come to a decision here, even if the decision is every Sikh does whatever they want, every…
Reiley Yang 00:49:57 The middle?
Liudmila Molkova 00:49:59 Yeah, I would be in favor of changing the tracer config, matter config, logger config, from disabled to enabled.
And updating the guidance we have.
We obviously cannot change anything existing, like the hotel SDK disabled environment variable, but we don't need to.
Tyler 00:50:31 I was gonna say, I'm also in favor of, like, changing the collector
To follow the other GO… Patterns in using disabled.
And sticking with what the specification specifies.
Pablo Baeyens 00:50:45 To be clear, the collector's decision to use enable predates any spec decision. There was no consultation, so I think there's, like, just different groups of people that decided on this independently, and, like, I don't think any particular group is more right than the other on making that. It's just… we should…
try and resolve this situation, but I don't think neither the spec nor the collector have, like, the authority here.
Tyler 00:51:14 Yeah, I'm not too sure it's resolvable, then.
Reiley Yang 00:51:20 Lumila, you still have your hand raised to… okay.
Trask Stalnaker 00:51:25 Go ahead, Ludmilla.
Liudmila Molkova 00:51:27 Yeah, I just wanted to say that the last time and the PR to change things got stuck.
And I'm trying to understand for what reason. I don't think anybody was strongly against it.
Trask Stalnaker 00:51:44 Yeah, I just wanted to say that, I… my personal opinion is that there is a better
But I know Pablo said that one is not enabled versus disabled is not… one's not better than the other. I personally, from my experience with the Java agent, where we have lots of these enabled flags.
Enabled is better than disabled from a user, perspective. It's clearer to the users what's going on. You don't have this weird dis…
Double negative of disabled equals false.
Trying to use, you know, figure out what that means.
It also avoids some weird behavior if you, like in the Java agent, where we have, from major version bump, changed our defaults.
From true to false on some enabled flags, or rather, from false to true on some enabled flags.
And if we were following this disabled, you have to use disabled, we would have to change the name of the property, itself in that case.
So I do think that the enabled is better, and I would…
personally support a PR to change that in the spec.
Reiley Yang 00:53:16 Yeah, I also want to add, I remember we talked about this, and…
I remember most folks gave the feedback that you don't want double negation, so enabled is the choice. I… I want to know who's disagreeing with
That, like, who wants to have a mixture of enabled versus disabled, because your language has some default.
Tyler 00:53:39 I'd recommend, like, reviewing.
Because, Riley, you've also said that exact same thing twice, and multiple times.
You know, the context And it… and it really, like.
Makes the other people's side of the conversation, and the people who have had this conversation with you, feel like you haven't listened to them.
So, I would recommend maybe just going back and reading the issue, and the other issues where this has been discussed.
Reiley Yang 00:54:05 Yeah, so, Pablo, do you have a summary to see, like, because there are multiple options, and I think it'll be good to understand, like.
Like, the overall summary, like, who's against what?
Pablo Baeyens 00:54:18 I can try to make a summary. I would like Tyler to correct me if I… if I get anything wrong. So, there's two parts, I tried to make a summary of some of the points raised on the last meeting on…
this comment, but there's also some conversation above that, like, it's basically the points, against it.
So… I think… Ultimately, there's one of…
not really litigating things, like, we made the decision, and… or, well, we as, like, the specification SIG made the decision, and… and we don't want to re-litigate it.
Then… And the decision was made, my understanding is, because, it was…
important for environment variables. Not necessarily for the YAML config, but for the,
environment variables they wanted the default to be false. Tyler, I don't know if you can talk more about the decision when it comes to environment variables?
I think that would be useful to… to give you context to Riley.
Tyler 00:55:32 Sure.
So, the idea is that…
When you define an environment variable, or you define some sort of configuration with a default value.
And it's a Boolean.
The default value is assumed to be false.
So, saying something is enabled false by default is wrong. So, like, take, for instance, the tracer config meter config, or the logger config.
the user does not provide that configuration, is the SDK disabled at that point?
Because I think there's the confusion that a lot of users have actually had, and it is a documented case in many languages, and it's made the decision.
To have configuration defined in this way.
And I think this is something that we've…
seen in… in the environment variable and in the configuration space. I know that I've also seen this in other projects, where they've gone back and forth on this sort of thing, and I agree, like, there is an issue where people don't understand, like, this double negation, but I think that you can also say that they don't understand this double negation, and saying that, like, oh, by the way.
the default is not enabled, but it is an enabled config. So, like, I think you're… you're going to get into a place where users are going to be config… or confused one way or the other.
When you have developers?
when you have developers working on this configuration space, I think they're a lot easier for them to understand that, like, yes, default of false is… it makes sense to them.
Reiley Yang 00:57:06 Yeah, so it sounds like we have… we have some good principles, and…
And they're… they're conflicting with each other.
So we have to give up a principle. Like, essentially, for the list of principles we have, we know we cannot be compatible. We have to, like, decide which principle are we going to give up, just to allow the other principles to hold, or the worst case, we don't hold any principle, we just do it case by case in a very inconsistent way.
Josh Suereth 00:57:36 So, I'm
real quick, because I just want to call out that, like, to re-emphasize Riley's point, I think we're in what's called a paradox mapping scenario, okay? You have two principles that are at conflict. It's not that you give one up, it's that you find a way to carve yourself between those two principles.
And this happens all the time in software. Like, we have to be really efficient.
But we also have to be very reliable, and sometimes those are at odds, because the way to be reliable is to make things redundant, which actually takes away your overhead. But then we don't want high overhead. How do you map those paradoxes in software? We are in a land of that. We have a couple principles around stability.
And, and things. Software dialectic, yes. That's, that's, that's a better phrase, Ted. But this is, there's actually, anyway.
We have to map what we're doing here, and there is no good answer. Like, we can just agree, if you look at the discussion that happened, I think a lot of discussion went into this, and what I thought the end result was, we would have one single disabled flag.
And that was the only one we would continue to allow. And that was the cot we were carving.
For now.
In terms of holding up all our principles.
I'm comfortable with that, because I think there was a lot of thought that went into this, where enabled is the way forward, and we have a single disabled flag that we will allow, and that's it.
However, if we want to continue this discussion, I just want us to all understand that we all have values that we hold, and we all might disagree about which values are more important on the spectrum of the two parallax.
But they're both important, and so we need to figure out the right middle ground. This is not a, like, A versus B, this is a what's the middle ground we're gonna pick?
So, I just wanted to throw that out there, because we've had this discussion a thousand times. I thought in the chat with Jack, and I don't remember if this was, like, a discussion that
was, like, between Pablo and Jack, and I was privy to, or this is in the spec one, I don't remember where this discussion was, but I know, I think Jack Berg also said the same thing, and I want to re-emphasize that and kind of be his presence in lieu of him here.
Because I think that might be a decent path forward.
Reiley Yang 00:59:53 Okay, so for sake of time, we have 4 minutes left.
Josh, move to your topic.
Josh Suereth 01:00:01 Alright, so this one will have to be an FYI. If you look at the, trace Zipkin exporter specification.
Do you mind opening it a sec, Riley?
We launched stable semantic conventions.
And when we did, I don't think… and you can blame me for this, because I totally forgot about this part of the spec. If you scroll down, there's a set of attributes that are used for mapping to Zipkin concepts in our Zipkin exporter. I have to go down a little further, right here, these attribute names.
We have actually started to break these.
in SEMCOM. We've created new things.
So, the way this is phrased, it's a should, and it's a priority order of what to pick.
So, I think because this is a stable document, you know, I'm trying to sort out what to do to correct this. I think what we can do is, add in the new semantic conventions to make use of in this document.
I think they would have to go at the bottom to be non-breaking, but I think there's a non-breaking way we can keep Zipkin compatibility.
The second thing I want to ask, though, is because no one noticed, and this is a theoretical breakage, right? My question is.
are people using this? Is anyone aware of this being used in practice with semantic inventions? Is this a part of the spec that we should basically say, okay, this exporter we don't think is needed anymore, and folks should prefer OTLP direct ingestion, kind of a thing?
Anyway, we don't have enough time to talk about this in detail, so apologies, I was hoping for 10 minutes, we had 2.
I'll give, Ted the last… so think about this, we'll talk about it next week. I'll give Ted the last minute for his advertisement.
Ted Young 01:01:59 Oh, yeah. I just mentioned this before, but it's good to keep mentioning it. So, we're gonna try to have an unconference with end users.
we decided to attach it to Fostum, because, in terms of, you know, having something that's not in the US and something in Europe, we don't have a lot of events in Europe.
So please, consider coming to this.
that's especially valuable the more maintainers we have. We threw one of these on conferences, way back in the day, also called OTEL Unplugged, and it was really great.
Likewise, when we used to have time to have the project meetings at KubeCon, I felt like those were really great. They were great, concentrated places to… for end users to get their questions answered, but also for us to get priorities and a sense of what's important from our user community.
So, please consider showing up. If it's hard to get travel budget for an unconference, let me know if there's, like, anything, kind of wording or things we can put up, or, like.
some kind of, like, not exactly a speaker award, or, like, something we'd… you're a maintainer, and we want you to be there. If you need something in order to get travel budget approved, I'd like to figure that part of it out as well, so let me know if that's a problem for you.
And that's all…
Reiley Yang 01:03:27 Thanks, Todd.
Okay, we're on time. Thanks, Ara.
Trask Stalnaker 01:03:32 Bye.
