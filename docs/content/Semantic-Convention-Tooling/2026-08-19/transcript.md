SIG: Semantic Convention Tooling
Date: 2026-08-19
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Laurent Quérel** 01:13 Hi, JV.
**Jeremy Blythe** 01:16 Hello?
**Laurent Quérel** 01:21 Right, it's true that, I was looking at, Slack checking if there is a meeting this morning.
**Jeremy Blythe** 01:31 I know the miller can't make it. That's why I ended up having a long, Slack conversation with her.
About the only thing that I was gonna bring up today.
**Laurent Quérel** 01:44 Okay.
**Jeremy Blythe** 01:45 I don't… I haven't heard from Josh.
**Laurent Quérel** 01:52 Yeah, me too. I don't know.
**Jeremy Blythe** 01:54 So I don't know.
Let's try, see if he's gonna join.
**Josh Suereth (Google LLC)** 02:09 Hey, sorry I'm late.
**Jeremy Blythe** 02:11 Oh, hey.
**Laurent Quérel** 02:14 Hey, Josh.
**Josh Suereth (Google LLC)** 02:16 How we doing?
**Laurent Quérel** 02:18 Thank you, man. Thank you.
**Jeremy Blythe** 02:21 Good.
**Josh Suereth (Google LLC)** 02:24 So… I've had this experience the past, like.
You know, 5, 6 days where… I wake up.
I'm going through my email, and I'm checking what happens, and Jeremy has fixed a bug, and Milla has approved it, and it's merged by the time I get to even see that there was a bug.
So, I'm really happy with that experience, that's pretty nice.
Anyway, I don't have a… I didn't have a chance to look at the agenda. I think we should be talking about, like, release and where we are for that. How's that sound?
**Jeremy Blythe** 03:01 Yeah, we can.
I guess just to… Norm Get up to speed on that.
There's a… I've lost it now. No, who does?
So that, issue tracking that I… that I have for the entity association stuff?
Pl1710.
needs to be reviewed. Once that's in, that unblocks the last three that can happen in parallel. Yes, there'll be some conflicts, probably, but those final three PRs can then all happen in parallel, and that would close that bit off.
**Josh Suereth (Google LLC)** 03:46 Alright, so… let me present this. So that is… that's the one I… was it this one I was just looking at, 1710 here?
**Jeremy Blythe** 03:52 Yeah, yeah, yeah. Yeah, that one. That's… that will unblock the last little bit of work.
**Josh Suereth (Google LLC)** 04:00 Alright, so, but in terms of issues, I wanted to go through quick and see if we're… we have missing attribute finding ID is misleading.
Oh, that's from live check. I think we have a lot of things going on. That's the second discussion I want to have, was, like, the live check, because we had a bunch of discussion in the spec meeting yesterday about it, Jeremy, that we should talk about.
**Jeremy Blythe** 04:22 And…
**Josh Suereth (Google LLC)** 04:23 Cause I don't know if you were there, God, to see the recording.
This is the major thing for release. Let's take a look at our… Projects.
Quick…
**Jeremy Blythe** 04:36 I never know what other meetings are good meetings to go to, so I only come to this one.
**Josh Suereth (Google LLC)** 04:40 The spec one is not… like… The number of times it would be useful for you with what you're focused on.
Is, like, once a year.
Maybe twice a year, yeah. So, like, the reality is, some of us go to all these meetings, and so I consider it my job to tell you when we talked about something relevant what it was. So you don't have to go.
You know?
But, like, if you wanted to get more involved with overall OpenTelemetry instrumentation spec work, like, then it's a good meeting to attend. It's where all the maintainers attend, and so you can talk about overall OpenTelemetry things.
It might become more important going forward, as every piece of instrumentation adopts LiveCheck, all of your users are there.
From OpenTelemetry, yeah.
**Jeremy Blythe** 05:30 Okay, that sounds good.
**Josh Suereth (Google LLC)** 05:31 Yeah, because Trask demoed, the… I don't know if you saw the conformance work that he's been doing.
the conformance Project?
Okay, let's, let's finish the next release planning, and then.
I'll add… I'll add that as an agenda. Okay.
**Jeremy Blythe** 05:47 I have some good work.
And recordings to watch, maybe.
**Josh Suereth (Google LLC)** 05:52 Yeah, yeah, because I think you, like, it's funny, you've been… live check has mostly been used not by OpenTelemetry itself, initially.
And now OpenTelemetry's using it, so everyone has feedback on it. And it's actually a good place to get feedback, because it's all in the open, so…
**Jeremy Blythe** 06:08 this was a lot of the conversation that I was having on Slack with in GitHub, and then in Slack with Lamila.
**Josh Suereth (Google LLC)** 06:14 Yes.
**Jeremy Blythe** 06:16 Yeah.
**Josh Suereth (Google LLC)** 06:18 Yep. Okay, so if we look here quick, we have… I think this is fixed, the downstream check failing. Did this… does this get fixed?
**Jeremy Blythe** 06:28 There were some errors last night.
**Josh Suereth (Google LLC)** 06:30 There's more errors again, okay.
What is it now? Do you have a chance to look at this?
**Jeremy Blythe** 06:36 I haven't looked yet.
**Josh Suereth (Google LLC)** 06:38 GenAI main generated docs is broken, test policies are broken, Why… Okay.
Can you actually show me the error?
Live check OTLP group is failing. What is that about?
Do you see what the failure is? Or it's just somewhere up here?
**Jeremy Blythe** 07:17 I will admit, I've not looked at any of these ever yet, so… I know this exists, but I don't… I've never actually looked into it.
**Josh Suereth (Google LLC)** 07:28 Yeah, here's the failure. Execution… make file, generate registry error.
Attribute is marked as excluded from dependency resolution cannot be used. Okay.
So we have a bunch of excluded things from dependency resolution, but we also have them as dependencies, and we're failing because of that.
This is probably a Lyudmila question.
I think it's something to do with how we're doing docs in Gen AI.
And one of our new… rules, okay. What was the other failure we had? So we had docs, but policy's one I want to check quick, if that's okay?
Failed, generated docs group above, diagnostic report. We are getting… attribute is marked as excluded from dependency, cannot be used for the metric.
Okay?
How is this a policy test? Is that the right one?
No, that's generated docs. Oh, test policies is here. I got… okay, I understand this now. Here we go.
Oh, hey, your new error is working, Jeremy. But guess what?
Our unit test made of bad entity.
We made a unit test with an entity association where the entity doesn't exist.
**Jeremy Blythe** 08:57 Boom. There you go.
**Josh Suereth (Google LLC)** 08:58 We're actually issuing a real error now.
And so, in the diagnostic report, we're getting an error that didn't show up before, and so we're failing, because suddenly our test policy has an error it doesn't expect, because our test.
**Jeremy Blythe** 09:12 An error that you want.
**Josh Suereth (Google LLC)** 09:14 It's an error we want, yeah, yeah, yeah, 100%.
Okay.
So, we need to go update Weaver packages before we cut the release, probably, to make sure the test passes.
So that, that's an easy one.
Okay.
And then… now that I understand how I'm… what I'm reading, Weaver Examples broke. So what did Weaver Examples break?
Current example believes it's in a workspace when it's not. I think this might just be an issue with the build harness for Weaver examples around live check.
Somehow, the makefile is broken for live check. That's fun.
**Jeremy Blythe** 10:02 Weird.
**Josh Suereth (Google LLC)** 10:05 Yeah, like, that's… that… this tells me it's just a build configuration error, if anything. So that one… that one seems like, We should look into fixing it, but the rest of these all look okay.
**Jeremy Blythe** 10:18 That might be a failure in the new GitHub action, the live check GitHub action.
**Josh Suereth (Google LLC)** 10:24 Oh, okay.
**Jeremy Blythe** 10:25 There's a bunch of Python there.
In the Airman Center.
**Josh Suereth (Google LLC)** 10:28 We'll have to take a look at that, then. Alright.
Cool. So… I… am I gonna have time? I think I might have time to take a look at these. So, I think we want to fix these before we cut a release and have a clean nightly.
I think that should be one of our new goals, is that this is not true.
Does this close and reopen every time It's fixed?
Or it's just always been failing. It's always… it's always failed. Ever since we set it up. Okay.
Alright, so let's get that clean.
You're working on the, I'm moving that to next release, because I think we're gonna clean that up. Is there anything else here we want to pull in?
The strict mode… Oh, Laurent, you're here. I wanted you to take a look at this one. 958.
**Laurent Quérel** 11:30 958, okay.
**Josh Suereth (Google LLC)** 11:32 This was the include hidden.
Someone has a fix for it, and I… is it still open?
**Laurent Quérel** 11:43 Okay.
**Josh Suereth (Google LLC)** 11:44 There was a fix where somebody was actually changing how we did dot directory exclusion to only do, like, parent dot directory exclusion that I wanted you to take a look at. It may have already gotten merged or been closed, I'm not sure.
But it was, it was in the thread. It was around this.
**Jeremy Blythe** 12:03 I think that was, nimrod?
You know, it says, hello?
**Josh Suereth (Google LLC)** 12:10 Yeah.
Is that one still open, or is it…
**Jeremy Blythe** 12:15 I'm not sure it was associated with the issue.
**Josh Suereth (Google LLC)** 12:18 It was not, no, but it was, like, related.
Let me check closed here.
It's awesome when there's so much going on that something I… like, a patch I remember I can't find because of all the activity.
**Jeremy Blythe** 12:36 It's definitely getting busier in the.
**Josh Suereth (Google LLC)** 12:38 Yeah.
Yeah.
I consider this a good thing.
I can't find it, I'll have to look for it later, but it's a thing to… a thing to think about, like, how we handle the underscore directories. Okay. Move SSL dependency decisions into features. This is another one if somebody has time to deal with.
This is just a pain in the ass. Maybe we just throw tokens at it.
But the way we build with Rust TLS and SSL dependencies, and making sure it works on Docker versus not Docker, it's a huge pain in the ass. So I think what we do… Is make sure we're using all the feature sets appropriately.
anyone who has a dependency on TLS and Rust has a ginormous amount of feature sets to let you select all of the original feature sets of the TLS library.
This gets me into why I think feature flags are somewhat problematic, because they are, like, propagation nightmares of doom.
Which is what we're dealing with here.
So, people want to consume… And people, I think this is you, Laurent, want to consume Weaver as, like, a library?
**Laurent Quérel** 13:51 Yes.
**Josh Suereth (Google LLC)** 13:52 Yeah, and we don't really want to force you to have to use OpenSSL everywhere, because we're on Docker.
We don't even want to use OpenSSL when we're not on Docker.
You know, it's just not… Doesn't make sense, so… I think we, we should have a set of feature flags for Weaver, where Docker has a set of feature flags that makes it work.
And we use, like, the default feature flags can be for, like, native deployment on, like, Linux, Mac, Windows. What do you think?
**Laurent Quérel** 14:21 Yeah, I don't remember the detail, but we have a set of, features like that.
I don't tell a row, I can take it if you want, I cannot produce what we have.
And make that configurable.
That's smooth.
**Josh Suereth (Google LLC)** 14:36 That would be awesome if you can. Yeah, so, like, we can have a…
**Laurent Quérel** 14:39 The, the 1382? Okay.
really well. I will, I will work on that. Thank you.
**Josh Suereth (Google LLC)** 14:45 I'll assign it to you if you have time, yeah.
This is one where I think if you make the specification, you can probably throw an agent at it, but if you don't make a specification, it's gonna come out with something trash.
**Laurent Quérel** 14:57 Damn.
**Josh Suereth (Google LLC)** 14:58 Yep. Okay, and then live check namespace registry coverage and fail on coverage below. Is this something you want to fix for the next release?
**Jeremy Blythe** 15:08 No, because I want to get through… The proper support that we've been talking about before we then add this, because that's going to have implications into how this is done.
**Josh Suereth (Google LLC)** 15:20 Yep.
Yep, okay.
Cool. So downstream check is failing. I'll… I'll take this myself and see if I can get that fixed.
you're on entity resolution, Jeremy. Laurent, I'm not gonna put this for next release, but it's something we should look into, and then… cool. I think we're good.
**Jeremy Blythe** 15:41 It's,
**Josh Suereth (Google LLC)** 15:43 Good.
**Jeremy Blythe** 15:43 Do you want to also have the V… the V2 live check, or is that… It depends when we want to do the release.
**Josh Suereth (Google LLC)** 15:53 How long do you think V2 LiveCheck will take?
**Jeremy Blythe** 16:00 After I've done the entity stuff.
I think I would need… it's gonna push it into the following week, I think.
**Josh Suereth (Google LLC)** 16:09 I'm… I'm thinking about, and you can tell me how you feel as a maintainer with this, I'm thinking about doing, like, bi-weekly or, faster releases.
**Jeremy Blythe** 16:19 I'm just…
**Josh Suereth (Google LLC)** 16:19 Because…
**Jeremy Blythe** 16:20 Yeah.
**Josh Suereth (Google LLC)** 16:21 Yeah, we have so many users now, and we're getting bug fixes, and I want to be… like, you're fixing them rapidly, I want to be getting releases out relatively quickly.
**Jeremy Blythe** 16:30 Okay, that's great. So if we do one this week and next week, it doesn't matter. We'll just keep.
**Josh Suereth (Google LLC)** 16:34 Exactly. Like, if we did a release every week while we have active bugs coming in, I'm perfectly fine with that.
**Jeremy Blythe** 16:41 Okay.
**Josh Suereth (Google LLC)** 16:42 Yeah.
**Jeremy Blythe** 16:43 then I would defer the live check V2 until the following week, then, because, Yeah, I still have to… I kind of want to write up what I'm going to do before I do it, and have it circulated a bit.
Because it's a little bit different.
**Josh Suereth (Google LLC)** 17:04 I… I imagine, yeah.
I saw the thread with you and Ludmila, so that has a bunch to talk about. Okay, so we're gonna do… We need to start doing faster releases… Fixed slightly.
And, entity, rest.
Final bug fixes before the 11th this week.
Okay.
Cool.
Oh, I have this, like, in microscopic font, sorry.
There we go.
Alright, so, conformance, live check. Let me put some notes here.
I think it's called Open Telemetry Conformance.
Let me look for it quick, and I'll put the notes down, because I forget the name of the project, and you'd think I'd remember, because I'm a maintainer of it.
**Jeremy Blythe** 18:10 It's Semantic Conventions, conformance.
**Josh Suereth (Google LLC)** 18:13 It's Semantic Conventions Conformance, not open telemetry, huh?
Yes.
Thank you.
Alright, so there's a new project called Semantic Conventions Conformance.
And let me just walk you through basically what it does. So, the idea is there's, tool runners that don't have semantic inventions, they just run things, and then there's specific Semantic conventions tests that test for compliance to different semantic conventions, and then there's, things that can be shared across, like, JVM or Node and that sort of thing. A lot of this is a crazy amount of Python harnessing.
And then scenarios that we run to test for compliance. So, like, in a scenario, I think if we take, like, a GenAI scenario, We'll do maybe Langchain?
there's a scenario config here with a workflow, an invoke agent. So invoke agent will be like, okay, create an agent, invoke it with a message.
And then we use this to kind of stimulate the OTLP that will get fired out to live check, and we make sure that it has you know, the right labels and things, and we're trying to get, like, a green, yellow, red kind of checkmark that you get for your instrumentation. So for the Lang chain scenario, this OpenTelemetry Lang chain, the conformance YAML describes, like, what we're looking for.
and how to run it, right? So the workflow is basically run this, invoke it, and then these are the different Scenarios that we are testing against.
Yeah, configuration for how you set up, apparently we're using fake open API keys. Then, data.json, I think this is… expected things, like what spans we want to have, and what the operations are. This is derived right now.
from OTEL, and these are findings we expect from Weaver.
Anyway… So it goes through a bunch of scenarios, does a bunch of junk.
There's these tools for how you can run things. Like, for GenAI, there's a runner that, wraps stuff.
So the runner will actually take your session, it takes a set of policies that we use to advise Weaver on things that we need to check in Gen AI above and beyond the default, right?
And then, coverage.py is a thing that it uses to say, here is what a GenAI span is, look for things that are in here, right?
don't eat… Because we don't have span type, we're keep doing this, like, fuzzy span matching.
So, all of these things have, like, fuzzy span matching, and it's… this is all… Rapidly kind of built out.
I hope over time, as we improve both Weaver and LiveCheck, that, like, these kinds of things become almost trivial or minimal in terms of code. Like, the better we do.
But, I think… does this have an example output?
I don't think we have example output yet, you'd have to look at Trask's… the Trask version of this to see it. But you can see in pull requests, I have one to review today, which is about how to do resource entity support.
But we're trying to rapidly add different conformance tests and make sure that we can, you know, check different instrumentation, use LiveCheck, and get a feedback and a report. So it's like using LiveCheck in anger.
we have to paper over some of the issues we have in, like, OTLP and things, like… The inability to look up a particular spin, that sort of thing.
One of the things that was frustrating, I think the folks working on .NET, and this is from CJO, Some of the reports that come back, maybe this was with Rust or with .NET, I can't remember which one, Right now, the way Weaver works is you give it a repository, and it reports against every single attribute in that repository, what's missing, what's there, and that can be a flood of things.
If I'm working on just HTTP Semcov, you saw that filtering thing for, like, what makes a GenAI span?
Yeah, you know, there's… there's this notion of, there's two concerns that I think we have to address. One is.
How do we limit… The report coming back to be about the, like, conventions that you're looking at?
And so… The second thing would be, And I'm tying this in my head, but maybe they're not tied, so I'm gonna mention it separately.
using the schema URL of the instrumentation to do the validation.
As opposed to, like, downloading a regist… like, where I can say, here's where you find the schema URL registry, and validating against that schema URL, but not all of the schema URLs in the bundle.
For a particular, like, span. So that we can, like, hyper-focus what our feedback is, and whether or not, you know.
if the goal is schema URL tags the thing appropriately, the conformance test should really be focused on, if I have a span in a schema URL, does the span and the schema URL match and line up? Like, is it doing the thing that it says it did?
**Jeremy Blythe** 23:56 Yep.
**Josh Suereth (Google LLC)** 23:57 Yeah.
So, anyway, there was a demo of it at the spec meeting. There might be continued demos going forward, so you might want to think about going to the spec meeting if we continue to.
I don't know how fast the adoption's gonna go, but, like, Trask is moving pretty rapidly. You already have a good channel to talk to him, and Ludmila, and folks, like, on GitHub, I think. So… The spec meeting is just another place you can talk to the rest of your users that don't attend here.
**Jeremy Blythe** 24:27 Okay.
**Josh Suereth (Google LLC)** 24:28 Yeah.
**Jeremy Blythe** 24:29 Have a look at that.
to what you just said.
**Josh Suereth (Google LLC)** 24:35 Yeah.
**Jeremy Blythe** 24:37 in… Thing… things that are upcoming, right? So the… the… issue from… from CJO is about… sort of tuning live check down to namespaces.
Or, you know, glob set, or whatever, you know.
So that… that is a thing.
The thing that I was struggling with, that we got to a good conclusion last night.
is about, matching.
So… The thing that I was struggling with.
In V1, everything is very sort of loose, and you just get this, like, giant… you get this giant ball of attributes, and LifeCheck kind of just sort of works-ish.
But if you try to… if you try to… be more precise, which you're trying to be here with the conformance, it kind of quickly falls apart. With V2, everything is much more strict and precise, and… and… Sort of locked down.
Which is great, and it makes projects like this conformance one work a lot better.
Yeah. But then the problem is, for people who are used to working And having LiveCheck being a useful tool in the, sort of, loose looser sense where you're using attributes, because attributes are really good for keeping things consistent, even if you're not defining all of your signals down to a thing, like, my company does in a lot of places, or for logs.
I love this attribute, I want to use it on my look.
All right, but that's not a signal I can match on, right? So all those problems start to come up.
what we landed on, actually, and that Miller sent me a pull request from the conformance project, that's how I knew its name.
Is about defining that, that, matcher.
At the… at the, sort of.
the front. So we… we can absolutely match on a metric, because it's named, and an event, because it's named, right? But then there's a whole bunch of other stuff that… You want to have some kind of match That then tunes you into a… Section of your registry that you want to go… When I… when I see things that match in this sort of way, this is how I want to track them.
Right? So for spans right now, there's no ID, so there's some kind of way of going, if it's a span that maybe has this attribute in it, or it has this attribute and it has this value in it, or it matches this regular expression, or whatever, whatever, whatever, whatever.
I've identified that as a thing that I want to check in this way with this section of my registry.
And what I'm saying is if we pull that… And the minimum was… like, between us, we kind of got to this point where, like, okay, that's good, so what we can do for the people who want to sort of be really loose, like V1 style.
They can have a matcher that's very permissive.
**Josh Suereth (Google LLC)** 27:58 Hmm.
**Jeremy Blythe** 27:59 Hey, match all of my logs.
with this… Set this section of my registry.
Right? Which is, like, probably makes people who are being very precise in defining things kind of go, oof, I don't like the look of that, because that's not precise anymore. But in the real world, it's still really useful to go, but I want to… I want to check that I'm specifying my S3 bucket correctly when I've emitted that in a log record.
Alright.
So I think… I think that… we're solving multiple things. It was like a stroke of genius, I think, from the Miller in there, to go like, hey, but use this thing. I'm like, oh yeah.
It just clicked last night, so…
**Josh Suereth (Google LLC)** 28:41 I like that, yeah. When you can solve two things with one feature, it's, like, way better, right?
**Jeremy Blythe** 28:47 Yeah, so I think it's gonna be really neat.
And so, I… my plan is to, like, write up What that flow would be through in this sort of concept this concept of matching.
Which is a thing that is already kind of happening in that project, but, like, to bring it in so it's properly a feature of… Life check.
And so that… however it's being done at the moment with, like, YAML files and Python scripts and things, that would actually be a feature in LiveCheck itself.
to solve those two problems. So I think… Some of that, Python code that we were looking at just now.
Hopefully, would this be able to be… it would go in that you'd put your matching rules inside your Weaver tomel.
That's fine.
**Josh Suereth (Google LLC)** 29:47 Okay.
**Jeremy Blythe** 29:48 So I was going to write it up, and then circulate it, and we can have a look.
And go, like, hey, this is the thing. So that's why I think we need a bit more… Apart from maybe not getting the time to work on it. But that's why… Next week seems… More doable, to speak.
**Josh Suereth (Google LLC)** 30:08 Yeah, I'm fine. That all make… that makes sense to me. I'm really curious to see what it, what it looks like, Yeah, but that… I, I do think, how do I want to phrase it? Weaver starting to be used in anger now.
Yeah. And so I expect all the real fun pull requests to come in.
And by used in anger, I mean used by a lot more people than before. Before, we had, what, like, 3 people using it for… we had clear use cases, now we're starting to get to, like, you know, tens and hundreds and that sort of thing. So I think we're in the… we're gonna get a bunch of feature requests that we might need to not say yes to all of them.
And we need to be careful about what we build and how we think of it, but it's gonna be an exciting time.
**Jeremy Blythe** 30:54 It's funny, I'm… I'm even… even in my company.
I have people… I've received Messages from people who are in completely different teams.
Yeah. They're going, hey, how do I do this with Weaver? I'm like, Who are you? So…
**Josh Suereth (Google LLC)** 31:11 That's awesome.
**Jeremy Blythe** 31:12 Yeah, that's really good.
**Josh Suereth (Google LLC)** 31:14 God.
Cool?
I don't have any other topic, by the way. Is there anything else that we think we need to talk about that's urgent here?
I don't know if you guys, pay attention to any of the, like, OpenTelemetry Weaver packages or examples.
Repos and their pull requests and things, but just, you know, if you have time, feel free to, Update, merge… you know, that sort of thing. We get a bunch of, like, just random dumb dependency updates and things every once in a while, so it's… Yeah, just… just a reminder, those two exist, and we actually are maintainers of them.
And they're usually relatively trivial to keep up to date.
**Jeremy Blythe** 32:01 Yep.
**Josh Suereth (Google LLC)** 32:02 Cool.
With that, why don't we call it?
I'm gonna go…
**Jeremy Blythe** 32:08 Look, can you…
**Josh Suereth (Google LLC)** 32:09 yard.
**Jeremy Blythe** 32:10 Yes, if you can look at my PR, that would be awesome. That's the unlock.
**Josh Suereth (Google LLC)** 32:15 Are we… once that one's through, are there more PRs behind it, or is that the one that we then…
**Jeremy Blythe** 32:20 There's three, right? There's three… there's three more, but they can all… they can all come in in parallel, and I can work on them.
**Josh Suereth (Google LLC)** 32:27 Okay.
**Jeremy Blythe** 32:29 Probably… Today, tomorrow.
**Josh Suereth (Google LLC)** 32:32 Okay, so then…
**Jeremy Blythe** 32:33 to the books.
**Josh Suereth (Google LLC)** 32:33 plan on tomorrow, I'll do the review, and maybe we cut the release tomorrow, if they're all through and we feel comfortable. I'll work on the build fix, too.
**Jeremy Blythe** 32:44 Okay. Yeah. Yeah, they should be small.
**Josh Suereth (Google LLC)** 32:47 Cool.
Awesome.
**Jeremy Blythe** 32:48 They're just the helpers to go and do the lookup in the various places, that's it.
**Josh Suereth (Google LLC)** 32:53 Yep.
Okay.
**Jeremy Blythe** 32:56 Alright.
**Josh Suereth (Google LLC)** 32:58 Good to see everybody!
**Jeremy Blythe** 32:59 Right?
**Laurent Quérel** 33:00 You're both…
