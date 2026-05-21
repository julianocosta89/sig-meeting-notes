SIG: Semantic Convention Tooling
Date: 2026-05-20
Duration: 65 minutes
Zoom Recording URL: https://zoom.us/rec/share/XWZcJ_Hdw2l38_-JOcQ0mMbBzGcEOHSPxr7EP8z_uEshE_D-GExzY-xXAH0E_AWX.ZDtQCDU3inoDqwNm
============================================================

## Zoom Recording Transcript

Jeremy Blythe 00:06:05 Hello.
Cijo Thomas (Microsoft) 00:06:10 Hello, can you hear?
Jeremy Blythe 00:06:13 I guess we'll, just give it a couple more minutes.
Here.
Cijo Thomas (Microsoft) 00:06:16 Sure.
Jeremy Blythe 00:06:17 Restraints.
Josh Suereth 00:06:37 Hey, sorry I'm late.
How are we all doing?
Jeremy Blythe 00:06:47 Good, how are you?
Josh Suereth 00:06:49 Not bad, not bad.
Okay.
Alright.
Let me get the agenda up.
I've been a bit distracted, sorry, I'm, like, organizing a work event.
So I, haven't had a lot of time for stuff. Alright.
Let me answer right now, hopefully I can turn the call, okay.
Let's, let's start with Cijo.
Just quick question, you know we have a GitHub action, right?
Cijo Thomas (Microsoft) 00:07:32 I'm using that one for installing PVWorld.
And then I was trying to do, like, more with Beaver. I tried a couple of instrumentation libraries in .NET and Trust.
Try to do a CI enforcement.
And then also in OpenTelemetry IRO, we tried this, but it looks like we had to write a lot of boilerplate code, so that's when I thought, can we work?
produce more than just the weaver install action.
So I made a draft PR, I validated it, it at least works, it reduces the amount of oil plate other instrumentations have to do.
So it's actually two actions. One is to start Weaver.
Make sure, we call the start action, check a health check.
Make sure it's ready, and then… Like, in between, like, then there is a stop, or finalize.
Which will stalk the weaver and get the report into a JSON, and it does a very basic analytics.
On top of that, so in between the start and stop, we have to fire our actual request, setting up a TLP to the people itself.
Interesting. Yes, yeah. That's the basic idea I created.
Josh Suereth 00:08:45 Have you… have you seen some of the stuff Lumila did in Python?
Cijo Thomas (Microsoft) 00:08:49 Yeah, actually, she was also doing this, boilerplate, which I was also doing, I don't think… I mean, I saw some issues in the past which discussed the idea of a, more GitHub actions.
But I don't think, even Ludmila's PR created a GitHub action. It's mostly, like, trying to code it in the Python repo.
Josh Suereth 00:09:12 Yeah, no, so the thing I'm wondering is, my question is the form factor.
So, the… what you're doing right now with GitHub Actions works, right? Like, and I think that this is a decent addition. My concern, though, is it means you need to run all of your instrumentation tests inside of, like, individual GitHub actions. So, like, let's say you're testing, like, 20,000 instrumentations, and you want to test them individually.
Are you planning to have a separate GitHub action pipeline for each one that would, like, start Weaver, stop Weaver?
Cijo Thomas (Microsoft) 00:09:49 Different instrumentations, yeah, so if my repo has 5 instrumentation libraries, that will be 5 different actions.
Josh Suereth 00:09:56 Five different… okay, okay.
That makes sense. That's basically what I was wondering. Lumila was doing something with Docker.
And, like, spinning things up in Docker, and, having, having, like, a little test suite that would do that. I remember that was, like, one option. Yeah…
Cijo Thomas (Microsoft) 00:10:12 Yeah, the main goal I had was… I don't know whether Weaver's stated goal is to act as a pure end-to-end integration test covering all the scenarios.
Or it's more like a smoke test, which we only test, like, the most crucial scenarios, and we rely on the normal unit testing, because we've been using, like, in-memory exporter as our actual validation. We fire up an in-memory exporter.
trigger the scenarios, and then create the inventory export, hey, did you get all the spams you're supposed to produce, and these attributes And then try all the combinations, because some of them are optional, and some of them are conditional based on another attribute being present. So, old sort of permutations and combinations we still plan to do in in-memory XPortal. This is more like a bigger higher order validation. It won't be covering all the… all the attributes, all combinations, but at least it gives a more fairer assessment.
There is an external tool which is validating your instrumentation library, proving that you produce what you claim to produce.
Yeah, because of that, I don't… yeah, I won't probably need a Docker-like thing, too, because it would make sense you start progress scenario, stop it, then start the next scenario, stop it, and then, in that case, I think Docker might be faster, or maybe, like, easier. I haven't tried this one with multiple, scenarios. It's like, start it, fire all my scenarios, then stop it, and then verify everything is so safe.
Josh Suereth 00:11:42 Yeah, so we're actually… I… I see, I see where we're at.
I… I'm not… so… so I actually think we add this, I just want to talk about, like, overall, where we're going. Like, one of the things that Weaver is, is it's a tool.
So, there's no, like… in my opinion, if Weaver supports it, it's not, like, a wrong way to use it. To some extent.
Cijo Thomas (Microsoft) 00:12:02 Okay.
Josh Suereth 00:12:02 like, it should be rather flexible, right? Because it's a set of, like, little components. And so that's kind of what I see you adding here. What I wanted to ask about was, from an OpenTelemetry standpoint, we're looking at using Weaver for, like, compliance.
So, like, the way I envision it is, unit tests, great, like, have unit tests everywhere. Weaver, as a compliance tool where we can say, this instrumentation is compliant or not.
we are looking at, like, having that be kind of an enforced thing. So it wouldn't be necessarily optional, it would be almost mandatory.
Trying to do, is put bounds around instrumentation problems.
So that we can actually use AI to do some of the really annoying things, like version bumps, where we can basically say, hey, here's the Weaver conformance test, that it has to produce this, here's what it did before.
Here's the aversion bump, like, go make this change and validate it, and this should work consistently across multiple different libraries.
to, like, bring them into semantic conventions, right? And we can actually ask it to, like, interpret errors and that sort of thing. So, like, there's a bit there that, from an OpenTelemetry standpoint, I want to start thinking about, because they're experimenting with that with GenAI instrumentation. So if you weren't aware of those discussions, I just want to make you aware of them.
Cijo Thomas (Microsoft) 00:13:20 Sure, sure. My goals were, like, slightly less ambitious, because I hate the issue when I try to add.
Josh Suereth 00:13:26 Oh, yeah.
Cijo Thomas (Microsoft) 00:13:26 Just for, like, just SDKs, I mean, instrumentation libraries in two languages.
We just had, like, other…
Josh Suereth 00:13:34 Before we run, absolutely, you know what I mean?
Cijo Thomas (Microsoft) 00:13:36 Yeah, just the first step, yeah. So, one of another goal is we were creating some performance testing in Arrow.
And we are trying to use those semantic conventions to produce, like, synthetic data.
Josh Suereth 00:13:48 Yeah.
Cijo Thomas (Microsoft) 00:13:49 And we were mostly interested in logs and events, not spans and metrics.
Then we realized that the pool of events in semantic conventions for events are, like, very small. It's, like, just 40 or 30 events. We are just cycling through them. It makes it very unrealistically compressible. So one of the ideas was, our project has around close to 500 events, named events, we have, but there is no… semantic, there is no registry where we are defining it. So our immediate goal is we'll define a registry within the Aero repo, define all the events we'll produce, and then use that registry as a source for our own, like, synthetic data. So we have… multiple goals, and this is the first time I'm looking at, like, we were, like, closely. I've used it briefly in the past, but… last week, I got some time, okay, let me… let me play with it, because this was part of Arrow's original goal, like, we'll be, like, self… observable and validated via view. That was something we envisioned, like, a year ago. I created the issue, but, like, last week is when I actually tried to validate things.
Josh Suereth 00:14:54 Yeah, that's cool. I don't know if you have any reviews here. I think, Jeremy, do you have any comments? Like, this… this kind of makes sense.
Cijo Thomas (Microsoft) 00:15:01 Yeah, can you suggest, like, what should be the, like, next…
Jeremy Blythe 00:15:06 I, I looked through it, I like it. There's a few things… I didn't… I didn't do a, like, a review review, because it's in draft, so I wasn't sure whether you wanted to, like… but there's a… there are a couple of things that I would, little minor corrections, I think, in, describing us.
describing a couple things I can't remember off the top of my head, but I can do… I can go through it again and do a proper… review, I think,
Cijo Thomas (Microsoft) 00:15:34 I wanted an initial directional arrangement before I spent time polishing it, so this is more like it's a draft. It does work, that's the… Only thing, like, it does work. I try to, intentionally create some violation, and it did, like, catch it in CI, and then I, of course, reverted it back. So if there is no directional, question, then I'll polish it and make it Ready for review, and then you can actually do the, deeper reviews.
Jeremy Blythe 00:16:05 Yeah.
Josh Suereth 00:16:06 Oh, go ahead, Jeremy. I was just gonna say, from my perspective, Weaver's a tool.
And so we need lots of little components that work well, that you can script together into solutions. So, like, I think the long-term solution I have in mind is going to be different, but as a tool, this absolutely makes sense. It's like, as long as we're comfortable maintaining this as a team. Go ahead, Jeremy.
Jeremy Blythe 00:16:30 I've been wanting this for ages, I just haven't got around to it, so I'm glad it's… I'm happy for the contribution.
Cijo Thomas (Microsoft) 00:16:37 I think you had shown it in one of your comments in a private report, I think I looked at that, because I was trying to see… This is not something which… they exist, so I, like, did a basic search, and I think, like, I don't know whether it's you, Jeremy, I saw it in, like, someone's fork, or a private repo where a similar thing was shown, so I used that as a inspiration, yeah.
Jeremy Blythe 00:17:02 The only thing I would say, also, is this kind of thing, I think lots of people will probably like it.
We have… there's another, repo, which is OpenTelemetry Weaver Examples.
There's an example in there for using the, the setup weaver action.
Cijo Thomas (Microsoft) 00:17:23 Okay.
Jeremy Blythe 00:17:24 That setup brief action, I think… maybe that's where you saw the code, because it does a setup, and then it runs the script to do the live check in the action.
And so it would be nice to update… either update that example, or add a new example that actually covers these off. Once… once this is… once this goes through.
As an example, I think it's really cool, because it's great to, like, point people at something, like, like you say, it works. You're like, yeah, it works, and it's working in CI, and then it's tested, like, a whole, like, end-to-end.
Cijo Thomas (Microsoft) 00:17:53 Yeah, got it, yeah, I can take care of that one, yeah. Hey, Lumila, good morning.
lmolkova 00:17:59 Hey, good morning.
Super cool.
like, probably I missed it, I'm sorry if you need to repeat yourself. Do you want, like, to start Weaver, run a bunch of tests.
And then stop the weaver, and then validate.
Cijo Thomas (Microsoft) 00:18:15 Yeah, so it's three steps, so one is setup Weaver, which we already have in action, and then I created this start, Viva start, which sets up the listening mode, and it also… does a basic health check that Weaver is indeed ready for receiving OTLP, and then I run whatever I want, like, instrumentation, like, all those things.
And then I do the end or finalize weaver, which stops endpoint and routes output into a JSON, and it also does a very simple parsing of the JSON and say, okay, you have X violation. So, so this PR just adds the start and stop, or start and finalize action.
lmolkova 00:18:51 Yeah, that's pretty cool. I'm really interested how it will, turn out to be. Like, you've seen in Python, we chose the route of, like, starting and stop in person, and more, like, control, but yeah, that's cool.
Cijo Thomas (Microsoft) 00:19:05 Yeah, this saved, like, a lot of boilerplate code. I had to write in the .NET and Rust instrumentation repo, where we are trying to use, like, Viva as a proof that, okay, we are producing what we plan to produce, and I intentionally kept it extremely simple. I don't intend to spend too much time writing instrumentation myself, but… there are people who are willing to do that, so they just asked, like, can you give an example of how to use WeWork? Then I realized I never used it in CI.
So that's how I, like, have it solo. In the related PR, which I have linked here, you'll see two PRs, one in .NET Contribu and one in Trust Contrib.
Where I just added it for, like, one instrumentation library. Hopefully the community can cover the remaining dozen plus Instrumentation recovery.
And one more thing, Rudmila, I mentioned this earlier, so we are using, or we are planning to use this in OpenTelemetry Arrow, where We intend to instrument the Arrow itself using events, and we already have around close to 500 events But it's not coming from any registry, we just created even with our own event name and some attributes. So we are trying to create a registry, internal registry of all the events, and then use Fever to prove that we produce the events when we are supposed to. So that PRE is also in flight.
Yeah, so many other pieces in play, but I think this is a, like, first step which I can leverage in all the three places, so… NET, Rust, which I maintain, so I should be able to quickly get things there, and Arrow also.
We'll be able to decrease that.
lmolkova 00:20:49 Super cool.
Josh Suereth 00:20:50 Yeah, yeah, definitely. Thank you for the, contribution, man.
I think, to Jeremy's point, the, like, places to document this?
the Weaver examples?
And then, maybe we can also update our docs to show this somewhere as well, in Weaver Docs, too.
I don't remember where we talked about the GitHub action, but… Yeah, if you look at our… our docs here.
I just want to make sure that people can find it, as opposed to it living in .NET, so we should advertise it somewhere.
lmolkova 00:21:28 Shouldn't we put it in the Weaver packages? This is where the reusable pieces live for Weaver?
Josh Suereth 00:21:33 No, no, we document GitHub Actions right here.
about how to use it in your CICD pipeline. So we say, here's see setup Weaver documentation and check Weaver examples. So I think if we have a Weaver example demonstrating how to use it.
And, the Setup Weaver documentation.
is specifically for the setup weaver action, okay.
I'm just wondering, like, this is the sentence I'm thinking about changing. This is in our README.
Cijo Thomas (Microsoft) 00:22:00 We should be able to expand that, yeah, we can expand that to, like, to leverage, setup, start, tail down, everything, like, there is an end-to-end example. I can probably point to the, instrumentation library as well, on top of the example, so people know it's not just a fake example, it's being used.
Josh Suereth 00:22:17 Well, I want to be careful of that, by the way. Like, I think it's fine to do that, but what I've experienced… so this is… at Google, they do that all the time, where they just link to where it's used, but then they…
Cijo Thomas (Microsoft) 00:22:26 change the…
Josh Suereth 00:22:27 in the other side, and you never change the original thing, and the example died. So, like, I would rather have the Weaver example be, like, independent for people, where they don't…
Cijo Thomas (Microsoft) 00:22:36 Okay.
Josh Suereth 00:22:36 Like, if it's in .NET, it's cool, it's being used, we could link to it, but we should also have the example. Otherwise, they have to learn your build tool.
and all the .NET ecosystem to figure out how to use it. And sometimes that's awkward. Like, in Java, I don't know if you've seen all the custom Gradle they have, I don't want to throw people at the entire Java build process with all the custom Gradles to figure out how to use Weaver. I want them to have a standalone example where they can, like, you know, spin it up, yeah.
Cijo Thomas (Microsoft) 00:23:01 Yeah, in the PR, the README I have, it says, like, there is a start and stop, which Viva provides, and in between, what you'll do is up to you, like, whether it's .NET, Java, like, whatever language you have. Yeah, yeah, yeah.
Josh Suereth 00:23:12 Exactly, yeah, and so, so Weaver examples, just, I think, I think, correct me if I'm wrong, Jeremy, I think it's, it's a Rust… Implementation, right?
Jeremy Blythe 00:23:23 So, it's actually, yes?
Yes, and… And no, in the examples has, you create another example for each one.
Josh Suereth 00:23:34 Okay.
Jeremy Blythe 00:23:35 But, the basic one, it's kind of reused.
with… like, it has the live check, and it has all of… and it has the CI associated with it, so that's the one I'm thinking.
The nice thing about the examples.
Is there intentionally kept as brief as you possibly can, so that you see how it works?
So it might just be checking, like, two things, and that's fine, because you're actually, like, you're seeing it flow through, and you don't have to, like, see it do a, you know, a million things.
That's sort of not helpful. It's the… it's like the… it gives you the flow, and then you know, like, oh, I put my code in there. That's what I like about it, kind of keeping it as simple as possible.
Josh Suereth 00:24:19 So, basically, like, the concrete suggestion would be we add a new job.
That could be Validate Basic with… You know, live test.
Cijo Thomas (Microsoft) 00:24:28 Can you… here.
Jeremy Blythe 00:24:29 Yeah.
Josh Suereth 00:24:30 Yeah, cool.
Awesome.
Cijo Thomas (Microsoft) 00:24:34 Okay, yeah, so I'll work on publishing it and make it ready for review.
Yeah, I don't… No if any other reports I have planned, but I'll just… like, check around with people, whether anyone else wants to incorporate, but at least I have 3 concrete use cases as soon as this is merged, where we will use it so that that should, like, catch any issues or anything.
I have one more question before I leave. Like, Josh, you mentioned, like, you had a bigger goal.
For auditing instrumentations. Can you briefly tell what that is, so I can keep that in mind while working on this?
Josh Suereth 00:25:10 Lyudmila brought this up, like, I would pay attention to what we're doing with the GenAI semantic conventions. So, like, one of the things we want to do is there's a conformance test that they have for GenAI.
that we want to start thinking about for instrumentations. So we could say, like, this instrumentation is conformant to HTTP, etc, etc. The other thing that they're doing, which I really like, is, you know, constraining the problem, where we try to focus our attention on you know, the test harness, if you will. So, like, making sure that we can set up a test, that it generates data, and that we have output, and then we have this capability where if we trust the test harness, we can do things like ask an agent to go bump the version.
From version to version, and fix the instrumentation, and we can… Hopefully, trust that the test will catch any, you know, hallucinated shenanigans.
And that we can, like, make maintenance easier over time. Like, that's one of the goals here. So this is where I think there's gonna be… like, one of the things we've been kind of talking about here is just, you know, using live check, heavier focus on getting these test harnesses up. Ludmila and Trask have been working on it, so you can actually… I don't… Ludmila, are there more? I think maybe Aaron, but I'm not sure.
Are there more folks working on this that I missed that would be good to reach out to?
lmolkova 00:26:30 So we, there… there might be, so maybe it's useful for usage, people from Honeycomb, Jamie.
And Volvgang, maybe you'll meet them at an observability Summit, not sure.
Cijo Thomas (Microsoft) 00:26:44 Yeah.
lmolkova 00:26:45 If you do, check with them. They've been starting to investigate using Weaver for JavaScript.
Okay, but…
Cijo Thomas (Microsoft) 00:26:53 all of them are using for validation purposes, right? Nobody has… because, Josh, I was kind of incorrectly assuming that the grand plan was to use Weaver to actually instrument itself, but what I hear is it's… people still write their instrumentation, and Weaver is just to validate that you did not make any mistakes.
Josh Suereth 00:27:10 We do want Weaver to generate code to make instrumentation easier, but I don't think Weaver will be generating the instrumentation. It's more, we want Weaver to, like, you know, give you the APIs, give you the validation, and then use AI to fill the middle.
Cijo Thomas (Microsoft) 00:27:26 Makes sense, yeah. So, Ludmila, what you were saying in JavaScript, they are trying to use Beaver to validate their instrumentations.
lmolkova 00:27:32 they were going to investigate it, I don't know where it landed, but it's definitely missing there. And, then the goal is to help with all the reviews, because this gives you the fastest review feedback, and, like, you can use it as a loop for the agent, as a harness, as Josh mentioned.
Cijo Thomas (Microsoft) 00:27:54 Okay.
lmolkova 00:27:55 that you're, like… There are a couple of… problems you will be aware of pretty soon, that it cannot really validate spans, right? It just validates that the attributes are known.
And this is something we'll need to fix. And, like, we will definitely need to go deeper, and, like, if there are complex attributes, we'll need to find means to validate that there, follow the structure, the schema.
But, yeah, it's probably, something, like, down the road.
And eventually, it will make your approach more… more interesting, much more interesting, because if we validate everything, we won't need Like, inside the test, validation, we will be fine with just the defaults.
Okay.
Cijo Thomas (Microsoft) 00:28:47 Makes sense, yeah, yeah. Yeah, my initial goals would be, like, on the instrumentation library and also on Arrow, we… we expect to have all the events we produce coming from a registry. I just started working on that yesterday. We created, like, first registry and defend an event.
And we are now producing that event, and I just incorporated in CI, to use the Weaver Light Check to prove that we are indeed producing the, event. But I already noticed there are, like, limitations with Viva, like, for example, it does not support stability.
Then I already saw Joshu had an issue open, like, long ago, so I did a plus one there. So my use cases would be, at least for the short term, it would be specifically validating events, whether these events are coming with the name we expect and the attributes.
And severity, if you can. Spans are metrics, maybe, but not immediately, but I think once the infra is there, we should be able to, like, expand on it.
lmolkova 00:29:46 Oh, for the generation, like, you probably know, and Lauren knows for sure, that you can generate the helpers for these events. Like, in .NET, you have this, nice static, compile time code generation. Reaver can do pretty much the same, based on the semantic conventions.
Cijo Thomas (Microsoft) 00:30:05 Yeah, we want to do that in Arrow also, because right now it's all, like, handwritten, and we had, like, people making mistakes all the time, so we… We are now surveying because I put some CA checks, which is not really Weaver, but some sanity checks to make sure, like, even names does not contain any… special character, it has an event name, it's not a blank thing, so we do, like, basic things, but we really want to, like, do a proper job, like, we define the events, then actually generate code to produce that event, then actually use it in the project, and then validate via life check that we are, indeed producing all those things.
All right, yeah, I think that's all I had. Yeah, nice to see you all, I'll now… start my journey, because I'm able to go to the observability Submit in another half an hour.
lmolkova 00:30:53 Have fun there.
Cijo Thomas (Microsoft) 00:30:55 Yeah. Alright, thanks everyone. See you, yeah, bye-bye.
Josh Suereth 00:31:01 Awesome. I may have to drop at 30 minutes, there's a meeting on my calendar that wasn't there a little while ago, and I don't know… I'm trying to figure out what the hell it is, so apologies. Let's try to get through some things really quick. Arianna has a PR for… generating docs. I don't remember the last time I reviewed this.
lmolkova 00:31:27 I'll take Coke.
Josh Suereth 00:31:29 Okay.
Cool.
Yeah, it'd be nice to get that through.
But, but again, I'm kind of curious, we should, we should… We might be merging this, then merging something completely different for the… what you're doing in Python, I'm not sure, or Gen AI. Like, do you already have docs, or what are you using for your doc gen?
lmolkova 00:31:51 Yeah, we will need to copy over the… so we are doing just the same conf, with some minor tweaks, And… There were some… Rough edges there.
So I think we should merge it, and maybe then replace it, and I don't know when we will get to it, right? Maybe it'll take us, I don't know, a month.
Josh Suereth 00:32:16 That's what I'm thinking, like, let's try to get it through with what it has, so we at least have something, yeah. Okay. Scorecards and PR badge, Jeremy. Anything you want to highlight here? Because thank you for doing that, that's awesome.
Jeremy Blythe 00:32:29 So, there's two PRs. One is to do with adding fuzzing.
And the other one is, pinning some dependencies.
If I can get those two in, then I can go back to the badge and say, yeah, we do fuzzing.
And then, we'll be able to get a passing badge.
That's the only thing that's missing, but I can't… I can't, in all honesty, say we do fuzzing until this is merged.
Josh Suereth 00:32:54 Okay. What, what do we know about, cluster fuzz Light?
It… it sounds… Creepy, honestly.
Jeremy Blythe 00:33:03 It's a Google thing.
Josh Suereth 00:33:06 I know, and I'm just saying, like, the name of it, I…
Jeremy Blythe 00:33:09 Yeah, I know, it's the one that's recommended, and it's the one that the OpenSSF actually recognizes in your project if you use it.
Josh Suereth 00:33:17 Oh, we have a different internal name for it. Right, right, right, got it, got it. Okay.
I know what you're talking about now. So, this, this, is this working, like, specifically with Rust?
Or is this something else? No.
Jeremy Blythe 00:33:34 It works… it's… it's one of the tools that does work with Rust.
Josh Suereth 00:33:39 Okay.
And you have just fuzzTarget with our Weber config. Okay.
Jeremy Blythe 00:33:46 Yeah, so you just kind of point at, He pointed at particular things that are… that actually, like, receive and interpret data.
Josh Suereth 00:33:54 Mmm.
Jeremy Blythe 00:33:55 which we've got some… we need… there's an issue that I… I think I made an issue.
Anyway, if I haven't… I intend to make an issue. We need to, like, change, we need to refactor the code a little bit to expose more areas, so that we can then fuzz it with this tool.
So, things like the OTLP, Needs to be moved into a crate, which it should, it should be anyway, but… Anyway.
Josh Suereth 00:34:25 Yeah, this makes sense, though.
Jeremy Blythe 00:34:26 like, I don't know, 60% of what it can do, maybe 70% of what it can do, which is better than… it's better than none.
Josh Suereth 00:34:34 Right, so basically, anytime a user can write config, or we interact with data, we fuzz to make sure that we don't just crash and die. I like it. Okay, this is good.
Jeremy Blythe 00:34:43 So I had this to run… it, like, runs nightly.
Because it can take a while, so it's just the thing that runs nightly. And it has actually already found a panic in the JQ library that we use.
So when… so when I get this in.
It's going to expose a panic, and then we'll have to solve that in some other way.
Josh Suereth 00:35:06 Is it a panic from us, or a panic from inside the JQ lab?
Jeremy Blythe 00:35:09 Panic from the JAQ.
crate that we… That we… so it's a dependency.
Yeah. And it's an unwrap. They have an unwrap.
Josh Suereth 00:35:21 Oh, God, yeah.
Jeremy Blythe 00:35:23 Yep.
Josh Suereth 00:35:24 Alright, I'm gonna rant just quickly, which is whenever I use Gemini, I have explicit instructions for it to never, ever use unwrap, and also to never use expect in code that… unless it's in a test module, and it always ignores it.
Every frickin' time. Always. So if you ever see me with an unwrapped code, it's because I was lazy and didn't, like, check everything in Gemini, because I, like, I tend to write a test and then ask it to write the code, or write the code and ask it to write the test. That's how lazy I am.
And, if you ever see an unwrap, you know, you know where it came from, so you can always yell at me.
Jeremy Blythe 00:35:59 Well, the nice thing, and actually this comes up in the… It comes up in the, in the, in the, I think it was in the badge, to get the badge, like, in the questionnaire.
in there. There was a thing about that specific type of thing.
Nearer.
And the fact that we have that in our linter settings.
Where we set it to do an error, not a warning, if we do that type of thing, means that we're deterministically protected and not… Not probabilistically.
Josh Suereth 00:36:30 Yes.
Yeah, and I do think that we should never remove that. Alright, cool. Since I might need to jump, real shortly, let me check my… I don't have a chat here… Okay.
Looks like I am canceling the other meeting, so I figured out what it was. Okay.
Let's, So basically, just review this. The fuzzing thing looks good. Are there any other PRs that we need to pay attention to here?
Jeremy Blythe 00:37:14 The… the other one is the pin dependencies one, so I need that one as well.
For the scorecard.
Josh Suereth 00:37:23 Independencies issues. So this is about what?
Jeremy Blythe 00:37:28 Oh, it's… for some reason, there are some dependencies that Scorecard's finding that our other mechanisms are not finding.
Why Renovate's not found that?
Josh Suereth 00:37:44 We could… we could look at the renovate, JSON to see what… what was going on with it. The… so… I think, James Thompson went in and tried to update our renovate to handle renovating both the cargo dist and the generated cargo dist files at the same time, and I think some of the regexes are a little too clever, and so renovate gets confused and doesn't do things.
That's my guess as to what it is. There's also a possibility that Renovate just, like.
is really struggling lately. Like, we keep… we have an issue in OpenTelemetry where we're suddenly not registered for Renovate.
On various repositories, and it just stops working.
And then we have to, like, re-register ourselves. So, like, Trask and the GitHub admins, we have a chat about, like, hey, what the hell's going on? And why do we keep getting unregistered from Renovate? Like… the collector noticed that they weren't getting a bajillion PRs from Renovate. I don't know if you noticed, we had, like, a two-week period where Weaver got no PRs from Renovate.
lmolkova 00:38:52 time.
Josh Suereth 00:38:54 Yeah.
I mean, it felt like heaven, honestly. It was wonderful, not having all those PRs, but still.
Jeremy Blythe 00:39:03 So if we… if… if I can get a couple of, reviews and…
Josh Suereth 00:39:07 Yeah.
Jeremy Blythe 00:39:08 Ticks on those, then they can… then they can go in. And then, since you've got the screen there, Josh, if you go to the… where the scorecard things come up, the security tab, I think.
Josh Suereth 00:39:21 Yeah, I might have access to things I can't show publicly, but yeah.
Jeremy Blythe 00:39:25 You go to code scanning, Right, so the only one I don't think I can do… Is the top one there, branch protection, because, and we have.
Josh Suereth 00:39:37 branch protection.
Jeremy Blythe 00:39:38 Yeah, but there's specific things it's asking for, and it's… the question is whether we… do we want this? Because some of the things are, like… you need two… you need two passing reviews instead of one, right?
Josh Suereth 00:39:51 Oh, this is salsa.
Gotcha, gotcha. I think, I think we probably could, I don't know, do you feel like we have enough that we could do two passing reviews? It might be a little risky, since there's only, like.
Like, three and a half of us active on reviews, you know?
Jeremy Blythe 00:40:10 I don't think so, so I'm not sure what we do with this one, and we're not going to get… We're gonna… we're not gonna get to zero, I think.
Josh Suereth 00:40:20 This is a warn, though. Can we get the score higher? Like, if we get the score higher, we're probably fine. It might just turn this from an error to a warning.
Took…
Jeremy Blythe 00:40:28 So if we could…
Josh Suereth 00:40:29 consolidation.
Jeremy Blythe 00:40:29 Just like… I don't know who… Somebody else has access to these settings, and not me.
Josh Suereth 00:40:36 Oh, we, we do, we do, it's in, it's in, again, I don't necessarily want to show it publicly, but there's an admin repo in OpenTelemetry that maintainers have access to that has all the Terraform settings for all these, where we can update our branch protection rules and stuff. And we should have branch protection set up correctly.
But the severity high things are the ones I think we have to do, so this is… branch protection apparently is not set up correctly, but the other thing is, this might be a bug. There's a new type of branch protection in GitHub we moved to that's more friendly for, actually, like.
GitHub has branch protection rules, and then this new thing that's like branch protection rules. Branch protection rules are so finicky, they're infuriating.
Like, you have to do them in the right order. If you change the order, all hell breaks loose. So they have this new thing that Trask moved us to.
And that new thing might fail the scorecard.
So I… I can… I can raise that in the GitHub admin chat to find out if other people are facing this, of failing the scorecard, but, In fact, I can show you the Terraform, I think.
Yeah, again, not… not everyone in the open television community has access to this.
But there is an admin, private repo.
Where you can see we have Weaver.
is defined in Terraform, and this is our config.
Jeremy Blythe 00:42:00 Okay.
Josh Suereth 00:42:01 And you should be able to… like, this is where I fixed Weaver to add merge queues. I may have broken things there, where I fixed… I don't know if you noticed I fixed our merge queues, but we no longer have to click update to Recent all the frickin' time to merge PRs. It will do so in a merge queue now.
But this is where we have our config, and if we look… I thought… yeah, we moved to these rule sets. So, like, our main branch is protected via this rule set.
And we have required status checks and things.
It is now called, a required, or a rule set, not branch protection.
And I don't… like, this… this is the equivalent of branch protection.
But it's not branch protection, so maybe we have to look into that and figure out the differences.
But the… I mean, the reality is only the main branch is protected. Every other branch inside of Weaver is not trustworthy.
Jeremy Blythe 00:43:00 Right. If scorecard is doing something odd, then there's prob… we probably have to put some .scorecard file in our repo, and then…
Josh Suereth 00:43:08 I don't think Scorecard's doing something odd. I think Scorecard is just not up to date with the latest GitHub capabilities for protecting branches. That's all. Like, this is a new GitHub feature we are using that is still in beta.
Yeah.
Okay.
But yeah, if you haven't seen this, and you ever need to do GitHub maintenance.
Around things, like the topics in the repo, whether or not you want to enable or disable our wiki.
Apparently, we have it enabled, I didn't even realize that, or discussions, right? If you ever… do you want to ever do maintenance, the way this works is you can submit a PR to make a change, and then one of the admins of OpenTelemetry will, like, approve it, and then the Terraform will automatically run and update Weaver for you.
So, this is the source of truth for all that stuff, if you ever need it.
Jeremy Blythe 00:43:53 Nice. Okay.
Josh Suereth 00:43:54 Oh, alright.
And by the way, thank you for looking into this, man, that's huge. Okay, so… to-do… Figure out, Y branch.
Protection. It's missing. I'm guessing, my thinking there, Jeremy, with the, like, to-reviewer thing, I've seen this scorecard pass.
without the reviewer thing, as long as branch protection exists. So I think it's just the branch protection failure that's the problem.
Jeremy Blythe 00:44:22 Fair enough.
Josh Suereth 00:44:23 Okay.
Cool. Lyudmila, you want to talk about exclude definitions?
Oh, I remember this one. Yeah.
lmolkova 00:44:37 Sorry, I've lost my Zoom window. Yeah, so… There's, I feel it's kind of important, because it… we end up doing a lot of hackery, because we don't have it, in GenAI places, and everybody who would try to move out of some country would have the same, so this… we discussed it, I think, a week ago.
So I'd like to mark all the GenAI conventions in the semantic conventions repo with this, so when we do dependency resolution, we don't sorry, when we use Autel, core semantic conventions repo. As a dependency, we don't see them.
So… If you end up referencing something that's marked this way, you have a special error.
Otherwise, it looks like it didn't exist.
If… We, like, there is some protection from adding this in… So you cannot exclude But you cannot reference excluded things without being excluded yourself.
Bye, this…
Josh Suereth 00:46:00 Y-you don't have that check, or…
lmolkova 00:46:03 I do.
Josh Suereth 00:46:04 You do, that's great. I think that makes a lot of sense, yeah.
lmolkova 00:46:09 Yeah, and then, essentially, that's it. There are some implementation details. So, for example, there is some interesting logic, thanks to Copilot, who founded that if we include everything, but also something is excluded, then we should silently ignore, because if you include everything, then, like, this includes a reference thing. It will go away with your PR, Josh, I think, but, it's still there.
It's mostly tribal.
Josh Suereth 00:46:41 Merge, did it.
Did I… I think I sent it, but I don't remember.
lmolkova 00:46:46 You sounded, yeah.
And maybe we should also talk about it if it's not on the agenda.
Josh Suereth 00:46:52 It is not, no. I think we should probably talk about it. Okay, so that… this… this all… this is kind of exactly what I thought we were gonna do, so that… that makes sense, I like that. My PR was this one.
Oh, it's still… did I… what did I screw up here?
I'm missing some code coverage, apparently.
6 lines, man.
Okay.
And I failed tests. What did I fail?
Jeremy Blythe 00:47:34 That is probably something flaky. I bet you if you rerun the job.
lmolkova 00:47:43 One of the tests, life check tests, became… flaky.
Jeremy Blythe 00:47:50 That's even before then, though.
lmolkova 00:47:55 Yeah, yeah, it's, it's unwilling.
Josh Suereth 00:47:57 personal account, I have been unable to run any OSX tests at all because of availability.
Like, any of my OSX jobs aren't running on my personal GitHub at all.
What? They just stalled out. Yeah, like, it was a bug, like, a week or two ago, so I have all these pending jobs that I need to go… like, I forget, because there's, like, so many GitHub CICD things that happen, but I had, like, all these, like, CICD OSX jobs I have to go kill every once in a while, because I forget that they're there and not running.
Anyway… Okay, so this one. What do you want to talk about in this one? Probably that I should have a description.
lmolkova 00:48:40 No, no, no, I don't care. If you… If we merge it.
Then, we won't be able to… Do the hackery needed to run life checks.
Because, I brought it up.
life check… validate… let's say somebody uses GenAI conventions.
JNA conventions does not import service.name or telemetry, SDKey, something.
And the only way to make it past today is to do this include our nerferenced.
And we talked about a lot of different ways we can fix it by looking in the schema URL.
And I… I added nods. I have an issue, and I added nods with different ways, but I think we… we should not merge it unless we have some other escape hatch.
Josh Suereth 00:49:46 For live check, that's… that's fair. Can you put a comment on the… On the PR, then?
lmolkova 00:49:54 Yeah, yeah, I will.
Josh Suereth 00:49:55 I will pull this over, yeah. Like I said, I have a… I have, like, a ginormous, really ugly branch that adds this to LiveCheck?
That, I think is absolutely throwaway, but it kind of, like, outlines some of the needs for some changes we need to make. So I think it probably would be good to come back here with, like, a design for, like, what we want the structure to be.
for LiveCheck and, Weaver itself going forward. Like, Jeremy, what I'm thinking is, you know how you have, like, the, those things that have arcs that have registries in them and all that, right? I want to create something that has the ability for you to basically say, hey, I have a schema URL, Go get me all the information about it.
as, like, a struct that you can embed in LiveCheck?
And then you can embed in the API thing, right? And so, if we encounter a new schema URL, we'd ask this for the information.
to resolve about, like, the other schema. So if we have, like, semantic conventions and dependencies and all that kind of crap, this all works. Like, we can actually find multiple things.
I think if we just do that initially, we don't need to do the dependency… Like, keeping dependencies around in… Forge?
Initi, like, yet, like… I think there's two ways we can go after this, right? One is, if we resolve, a dependency chain, we can keep around all the definitions and have them available so live check can just find them and see them, and you have them, like, pre-cached.
But then the other thing is I just want this, like, interface where it's, okay, I have a schema URL, go give me the information about the schema URL so I can do my enforcement checks, and then live check would be updated to actually look at the schema URL that's tagged on the data before it does its enforcement.
And those are two areas that we can eventually, like, converge on together, right? So this, like, lookup thing would eventually use the fact that if I resolve schema URL A, and it has dependency for B, I don't have to resolve B independently later.
Jeremy Blythe 00:52:09 Yep.
Josh Suereth 00:52:10 Yeah, okay.
Cool.
I don't know if anyone has time to do that. I can guarantee you that I will not have time to do it for 2 weeks. I am going on vacation on Friday, so I will not be in this meeting on Wednesday of next week.
But I'm happy to pick it up, like, after that, just for context.
lmolkova 00:52:37 Enjoy your vacation.
Josh Suereth 00:52:38 Thank you, yeah.
I'm hoping… I'm hoping I come back not more stressed out. It's a fam… like, big family vacation, so… Maybe I'll be working anyway.
Alright.
Let's see, I think, I think that… That's good. Okay, so we will… we will not merge mine. We'll take a look at this one.
Last thing, we have 10 minutes. Shall we do this? I am actually totally fine with this. I do think it might be worth running by the entity sake.
But… Yeah, I mean, for me, this makes sense.
Quick question, Jeremy, though. Would you… Would you require all of to be here, or can this just be raw?
Jeremy Blythe 00:53:33 Sorry, what do you mean?
Josh Suereth 00:53:34 So, like, basically, what I'm suggesting is the outer thing would be… Oh man.
What do I do here?
Jeremy Blythe 00:53:44 Sorry, I pasted that directly from Slack, and it did something weird.
Josh Suereth 00:53:49 Yeah, yeah, so, like, this here would be, like, this one and this one would be ORed together.
Jeremy Blythe 00:53:56 because I was…
Josh Suereth 00:53:56 the way it is.
Jeremy Blythe 00:53:57 Yeah, top level is, or…
Josh Suereth 00:53:58 Yep, top level is OR, but then you can specify an all of and a one of.
Jeremy Blythe 00:54:03 And you can have, like, just like you do in JSON schema, right? Same.
Josh Suereth 00:54:09 Yep.
lmolkova 00:54:13 Giving and growth?
Josh Suereth 00:54:14 Oh, go ahead.
lmolkova 00:54:16 Do we need both? Like, do we need all the complexity?
Josh Suereth 00:54:24 That's what Jeremy's saying, is we do need both. Like, we already know that we need ORs, Jeremy needs ANDs, and so that's why we need both. Now, do we need them nested to… the thing I'm nervous about, actually, and this is a gamble thing.
If we call this one of… There can only be one one of in the list.
If we have two one-ofs on the list, you have to name one of them, because YAML is YAML.
Jeremy Blythe 00:54:51 I guess, The real question, shall we do this, is, do we want to support this sort of way of composing the associations?
Josh Suereth 00:55:03 we…
Jeremy Blythe 00:55:03 I would then express that in YAML is… is YAML… is YAML phone.
Josh Suereth 00:55:09 This discussion around whether we support this was, like, the last time we had this discussion, the entity sig, was, let's not do it for now until we know we need AND. Like, we know we needed OR, let's just do OR. If we need AND, we'll figure it out when we need AND. Well… You just said we need an end.
So…
Jeremy Blythe 00:55:29 It was an issue as well, and it wasn't just me.
Josh Suereth 00:55:32 Yeah, yeah, yeah, yeah. I mean, you're not the only one who needs AND, but I mean, like, when we talked about it before, we tried to reduce the complexity, because we're like, okay, we know we need OR, we don't know if we need AND, let's keep this simple, now we know we need both. I think that, like, let's do the simplest possible thing with ANDs and ORs.
Together, yep.
Cool.
if there… if there… yeah, if you want to tweak the syntax or whatever, like, like, please do, but I… this… this makes sense to me in the sense of, I hope we picked the right defaults, and I also expect most people to be like, cool, I either have this.
Or I have this, and I don't do both ever.
For 99% of people. And then there'll be, like, the 1% that are like, hey, I have this crazy-ass nested thing, can I do it? We're like, cool, yes you can, but we're not really documenting it easily for you, so… but here's how you do it.
Yeah.
Cool.
Alright, I think… I think we're at the end, I'll do a quick update on, like, dependency resolution.
if we're not merging my PR and dependency resolution, that is the start of my big chain of all kinds of crazy dependency fixes to handle that, like.
the PR that's here.
I'll show you this, because I think this, To make more sense. Get out of the way, notifications. Alright. Where's my… Here we go. Dependency Resolution Part 2. This is where we can resolve dependency conflicts, which I think is going… like, we're going to need this relatively quickly, and it's currently blocked. If you look at the failing test, though.
I can show you what the failure is, and this is unfixable without us doing some of the other shenanigans we're trying to do.
In Weaver. So the failing tests… let's see, data fixture… is this circular registry test, I think?
Or no, Diamond Conflict. Here we go. So we have… we have a registry that has a manifest, right? Where, I depend on A, and I depend on B.
And then, A and B… One of them depends on C1.1.
And one of them depends on C1.0.
Or, sorry, C1.2.
And then inside of C, I have a, like, here's an attribute that conflicts.
And inside of here, I have an attribute that conflicts, and basically what we're testing is the output of that diamond conflict.
should get, you know, the most up-to-date C. It should get the 1.2, not the 1.1.
But what we see today, with the PR I have, is it gets the 1.1, not the 1.2.
So, I think we have two options here that I'm actually comfortable with either way.
I could mark that test as pending and a known issue.
And we merge it as is, just so we get more flexibility. And it's somewhat innocuous.
I'm hoping it's not a significant breakage for people, if that… if we pick 1.2 of, like, a span versus 1.1.
when we do this, like, crazy mergy dependency diamond L, So that's option one. Option two is we don't merge it, and we go through all the chain of things we have to do to, fix how we do dependency resolution overall, to make these things more pointers, to fix, like, you know, live check to be able to use schema URL, and then I can land, like, the full fixes here, because there's a lot of architectural things that we have to get in place.
Right? So, option one is, We say, you know what, this is relatively innocuous as a bug.
We're gonna open an issue to track it, we're gonna make the test be yield for now, move forward. Option 2 is, we say, no, we're gonna go start the big re-architecture, do the aggressive thing, and get it done. I mean, I'm gonna do number two no matter what. It's just, do you want to merge this with the known bug first?
lmolkova 00:59:59 Yes.
Josh Suereth 01:00:01 Okay.
How do you feel, Jeremy?
Jeremy Blythe 01:00:06 Why not?
Josh Suereth 01:00:08 Well, okay.
Alright.
If you need…
lmolkova 01:00:12 Are you blocked on…
Josh Suereth 01:00:14 Good.
lmolkova 01:00:15 Are you blocked on in code and referenced?
Do you depend on…
Josh Suereth 01:00:19 Include on ref… I was depending on include unreference for this, yeah, because I'm trying to shrink things up. Go ahead.
lmolkova 01:00:27 Can we find a way to unblock you without removing the flag?
Josh Suereth 01:00:34 No, because the flag makes everything else hellish. Like, that decision makes dependency resolution so painful to modify that everything goes, like, all of my architecture goes to hell, when I try to start changing things. It, it, like, I… anyway, there's a slew of bugs that I was creating.
That if I can remove that flag the way I'm removing it today, to have consistency, it's much simpler to review the code, do the algorithm, like, the… to even think about what the hell you're doing.
lmolkova 01:01:06 So if we remove the flag.
Can we… what else can we do?
On the life check, we can suppress that specific Violations, right. Jeremy, do we support it in the configs, suppressing violations?
Jeremy Blythe 01:01:22 Yes.
lmolkova 01:01:23 Oh, cool.
Jeremy Blythe 01:01:26 What is it you specifically need to do?
lmolkova 01:01:30 It's like… I don't have service name in my… registry, right? Nobody does, except the core repo, and nobody should.
You can… Huh.
Jeremy Blythe 01:01:43 You can say ignore… ignore the sample service.name.
And it won't tell you anything about service name.
lmolkova 01:01:51 In the config.
Jeremy Blythe 01:01:52 In the conflict.
lmolkova 01:01:53 Cool. So then, this would be a temporary hackery in consumers.
That people will have to do for now.
Until we resolve it, but it will untangle this part.
Josh Suereth 01:02:14 Yeah.
lmolkova 01:02:18 Okay, Dan, I will… Try it out. It will… work, and then I'll approve the… include and reference to removable PR And then I'll take a look at this one.
Josh Suereth 01:02:33 Yeah, for this one, I'll mark the test as pending.
And I'll open it for review, and we can decide. I actually think it's okay… like, like… Look at the test that's failing.
But I think the issue, it's subtle, it's something we absolutely need to fix, and I think it'll take some time, but I also don't think it's the end of the world, if we allow it temporarily.
By the way…
lmolkova 01:02:59 Do we know?
Josh Suereth 01:03:00 What?
lmolkova 01:03:02 Do we know if… when it happens? Do… do… can we detect that it happens? Can we issue some sort of a warning that, okay, there is… there is a known bug here, or a known problem?
Josh Suereth 01:03:14 I think we can… yeah, but we'd have to do it as, like, once everything is resolved, we can go look at all of the schema URLs and find the problematic one, yeah.
So basically, if you look at your dependency list, and you see the same schema URL, but two different versions.
Then you, you know, that's… that's the problem.
lmolkova 01:03:36 Oh, you know, like, Mavin has this dependency tree thing. We should have one for Waver, and we should warn on, diamond dependencies.
Just periods, always.
Josh Suereth 01:03:49 Okay, I mean… I… I think that… no, I disagree, sorry. I don't think we can… We should warn if we end up picking two versions.
in a diamond dependency, but when there's a clear resolution, you have to support diamond dependencies, and we're gonna have that, right? So, if we pull… we pull out Gen AI SEMConf, right?
would pull out… I don't know, what's the next thing? Like, messaging Semconf as its own thing? If I depend on both of them, they're both gonna depend on core.
So, I'm gonna have diamonds all the time.
lmolkova 01:04:25 Yeah, so maybe Warren is not the right word, maybe info, so you should know that you have this depend… like, until we have a good fix for it, we should tell people that this is the case, and they should expect stuff to happen.
Josh Suereth 01:04:40 Yeah, yeah, yeah. I mean, I can also detect when the issue happens and just give you a warning.
that says, hey, you know, I found that there's a dependency issue here.
here's something you can do to fix it yourself, which is directly import the thing from the other… from the… like, if you directly depend on the top registry and import that thing yourself, then everything's fine. So I could actually give you a fix as well, and write that detection. So, yeah. Okay.
Cool.
lmolkova 01:05:10 Cool.
Josh Suereth 01:05:13 Thanks, everybody.
I think we have a path forward here. Really quick question, did we want to cut a release?
Let's take that offline, but let's, let's chat offline about, like, cutting the release of Weaver.
Okay. Thanks. See y'all.
lmolkova 01:05:28 Thanks.
