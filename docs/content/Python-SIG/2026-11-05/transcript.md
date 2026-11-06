SIG: Python SIG
Date: 2026-11-05
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Emídio Neto 00:03:53 Hey, Lukas.
Lukas Hering 00:03:59 Hi, Emidio, how are you doing?
Emídio Neto 00:04:02 Great, great. And you?
Lukas Hering 00:04:04 Yeah, we're good.
Riccardo Magliocchetti 00:04:41 Hello.
Lukas Hering 00:04:45 Oh.
Emídio Neto 00:04:46 Hey, Cardo.
Tammy Baylis 00:06:54 Hey y'all! We'll just get started in one more minute.
Aaron Abbott (Google LLC) 00:07:46 Hey everyone, how's it going?
Diego Hurtado (Dash0) 00:07:49 A…
Tammy Baylis 00:07:53 Hey, guys.
Okay, it's, 5 after, we'll get started, No, everybody here, welcome back to the hotel Python SIG meeting. Docs link in the chat for today's topics. Please add your topics to this list if you want to talk about something. And I'll just do some triage for 5 minutes.
Let's look at the core issues first. Sorry.
My cough has just never gone away from being sick.
And holy crap, there's a lot of PRs.
Mmm… Reinstantuate.
Concurrent multi-log record processors, executor after a fork, oh my goodness.
Shalla process hangs, that's not good.
Aaron Abbott (Google LLC) 00:09:00 This is, like, a never-ending… Stream of whack-a-mole.
Tammy Baylis 00:09:07 Very good ticket.
Yeah, let's have a look at this one.
Got, non-green checks. Sorry, yes.
Lukas Hering 00:09:18 I was just gonna add, I think at some point we need to probably add the… the shared, fork handler that I think Aaron suggested, because, like, yeah, every time I register one, basically, it'll leak, so… That's the only concern with, like, fixing all these.
Tammy Baylis 00:09:41 Okay… Sorry, I didn't quite catch that, but should I make a note of something here?
Lukas Hering 00:09:53 I can… I can also follow if it's… it's… basically, yeah, we should maybe try to centralize our fork handler logic,
Tammy Baylis 00:10:04 Yeah, I'll leave that. Thank you.
Big some metrics. Oh, thank you, by the way, for the other patch release last week. Fun formatting.
Dash. Dash, oh, yo.
Last value aggregation, no TLP encoders omit the start time for gauge.
Is this… We had a lot of talking about gauges a couple years ago, I'm just trying to remember if it's related to that or not.
Aaron Abbott (Google LLC) 00:10:53 I want to say there was a spec change at some point for this.
But it sounds like a pretty simple… Change.
Tammy Baylis 00:11:01 Yeah.
Yeah, if it's not… Too crazy, then.
Oh, thank you, Dotafire.
Yeah, okay, ready for review, for sure.
Aaron Abbott (Google LLC) 00:11:21 Yep.
Tammy Baylis 00:11:21 2 more minutes.
Lukas!
Treat timeout of 0 as infinite.
Declarative… declarative config schema.
Oh, no, okay.
Yeah, so… This, like, before declarative config, it kind of meant a different thing to each language.
But… now… Now that we have something more unifying, then…
Lukas Hering 00:11:57 Yeah, this doesn't change how we… Our arguments are passed, it just does a translation at the configuration… in the configuration package.
Tammy Baylis 00:12:07 Okay.
Lukas Hering 00:12:08 So, yeah.
Yeah, Riccardo already reviewed, there's this one comment, which… Responded to, but…
Tammy Baylis 00:12:19 Awesome.
Yeah, thank you, that's on our plate.
One more from Lukas. TLS, MTLS support.
Lukas Hering 00:12:33 Yeah, this one could definitely maybe use some reviews. I, the one kind of neat thing is I did add, like, actual, end-to-end Docker tests with, like, like, mock cert generation.
So… Yeah, so you can kind of… So, like, yeah, now we fully test… TLS and MTLS and… at least with the HTTP ones, so…
Tammy Baylis 00:13:06 Wait, where did I…
Lukas Hering 00:13:07 You can, yeah, you can see inserts.py, where the… the CERT generation.
Tammy Baylis 00:13:14 Where did the whole thing… Sorry, did I collapse something? Okay.
Mmm… certs.py, yes.
Lukas Hering 00:13:27 Yeah, so this builds, like, a fake CA and everything, So, yeah, and then it also adds the… if we want, I can break up the test additions into a separate PR, but I thought might as well add them while we're adding it to declarative config.
Aaron Abbott (Google LLC) 00:13:46 Cool.
Quick question, Lukas, is this in… is this, like, in declarative config already, and is it stable or development?
Lukas Hering 00:13:56 It's stable and declarative config.
Aaron Abbott (Google LLC) 00:13:59 Okay. Awesome.
Lukas Hering 00:14:04 But we haven't implemented it yet. So that's, yeah, what this does.
Aaron Abbott (Google LLC) 00:14:09 Yeah. I guess one other option would be to just commit the certs in here, but it might make some secret scanners mad.
Lukas Hering 00:14:16 Yeah, that's what I was worried about, is that we'd get a bunch of… A bunch of complaints.
Aaron Abbott (Google LLC) 00:14:22 Yeah.
Cool.
Tammy Baylis 00:14:31 Yeah, well… Thank you. Let's call it that for triage for today.
And, I'll just take a look. What am I working on this week? Riccardo's doing sampler visibility to span attributes for messaging instrumentations. Awesome, thank you.
move on to the main topics. So, Emidio and Python 3.15 support.
Emídio Neto 00:15:00 Hey, I was reviewing some PRs and got those ones from this contributor.
Python 3.15 was released one month ago.
our policy says to add support no later than 3 months, but I'm afraid this PR got, to get, Lost in the, never measured. So, from the perspective of contributor to be bad.
So I'm wondering if… Anyone is against, too.
Like, introduced the support a few months earlier.
I can review this and help this get merged.
Lukas Hering 00:15:52 Yeah, I think it's fine. Yeah, there's, like… a bunch of issues with this PR, though, that I see, and, like, maybe drop… why I want to drop 214T, and then… Yeah, it's also, like, raising our minimum tested versions, which probably isn't good. We want to keep testing, like, the oldest version of Protobuck and everything.
Emídio Neto 00:16:11 Yeah, yeah.
I've noticed some. I can review and, Take a look on both card and contribute.
So, I'm assuming… All you folks are okay.
Tammy Baylis 00:16:29 I am okay.
Emídio Neto 00:16:31 Alright.
Tammy Baylis 00:16:38 Introducing.
Thanks, Emidio.
Emídio Neto 00:16:45 Cool, thank you.
Tammy Baylis 00:16:48 Diego, packaging updates.
Diego Hurtado (Dash0) 00:16:52 Right, so we were discussing this last week, and I promised, to investigate another approach that could be… Extending the… try to… by modifying our code in OpenTelemetry instrumentation, right, try to support more versions.
approach, unfortunately, wouldn't help us with, the injector, so I pretty much discarded it.
Then, I found this, comment from… Dylan, and, it's, pretty clever, it, It's based on the fact that, we are… Using a small subset of, the… Packaging functionality to compare Version strings, and Dylan… provided, A little script here.
I tested it, and this script works for everything we have now.
The issue is that, This script also has to work for… Any… version string that the user may have.
In their virtual environment, and there are… I found several examples.
Of strings that wouldn't… That would break the script. Now, of course, this script can be fixed, so that we support also those version strings and so on. But if we follow that path, we pretty much will end up reimplementing, this depth, I think it's 4 or something, that, defines the… the… how version strings are. Now, I already did something like that in a previous PR, Yeah, thank you.
No, no, that one. Oh, did I… I probably just typed the overall number.
Whoa.
Tammy Baylis 00:19:04 Yeah, they're.
Diego Hurtado (Dash0) 00:19:04 That's probably the other one, yeah, yeah, that one, right? So, in that PR, pretty much, we implemented this part of the PEP, And, the reason why this PR was subjected was that this would require maintenance on our part, right? Which is true.
Which is true. So I switched it to this other approach of vendoring packaging. Now, vendor and packaging does introduce I don't know, like, 7,000 lines of code?
But, on the other hand, we don't have to maintain those 7,000 lines of code. We will not be touching them.
In fact, we can, pretty much at a CI… Check that makes sure that these lines are not being changed.
by hand in any PR.
So, there is not really any maintenance to do on vendor code.
It's just sitting there.
And we use it, and it gets updated automatically as soon as there is a new Version released.
So… I… I am a lot more okay with having a lot of code.
Because, at the end of the day.
it doesn't matter, we don't have to maintain it, it's just there, we can just forget about it. So, I am now, More on the side of vendoring? Packaging?
And I would like, of course.
To hear your opinions about this.
Tammy Baylis 00:20:55 Lukas has a stand-up.
Lukas Hering 00:20:57 Yeah, did you ever… so, I think either last meeting or before that, I brought up just… Trying to widen the accepted version ranges.
Diego Hurtado (Dash0) 00:21:09 Yeah, trade that. It, I mean, it's not something that, I think it would help us, in the injector case.
And, at the same time, I don't think it's a… It's an approach.
that, makes things, easier for us.
In the sense that, doing that… Kinda forces us to… Not do a… not having to maintain packaging, but to maintain code that uses packaging.
We will need a bunch of ifses and elsees, like, okay, if this is… if… Packaging is this version, do this, packaging is this other version, do that, and… and we never know when some feature is going to show up in packaging that doesn't show up in previous versions, and there is no backboarding, and… So it doesn't make things, really easier.
I… I still think that rendering is the easiest thing to do now. It's… It's more code, yes. Doesn't matter.
That's… As I mentioned before.
Lukas Hering 00:22:32 I guess, yeah, the only reason I suggested that is I think the example you gave was… it was either FastAPI Instrumentation or Flask or something.
And that specifically had a… Higher, lower bound on… The version than the instrumentation package itself had.
So, if we could just bring down… the version to… I think it's, like, 14 or something.
Diego Hurtado (Dash0) 00:23:03 The… Yes, but at the same time, that's… Wee… It wouldn't help us with the vector if the end user has another version of packaging, and at the same time.
I don't know what's gonna happen in the future, right, sweet?
some other instrumentation, and some other version of packaging, right? So… It, it could be a fix.
That works today, but doesn't work tomorrow.
Aaron Abbott (Google LLC) 00:23:46 Riccardo.
Tammy Baylis 00:23:46 Yeah.
Aaron Abbott (Google LLC) 00:23:47 Yeah, go ahead.
Riccardo Magliocchetti 00:23:50 I think, Aaron, you will, before you were first.
Aaron Abbott (Google LLC) 00:23:54 I don't know, it was pretty close.
Sure, I'll go.
I was gonna… I was gonna ask Diego, like.
the thing that you mentioned about supporting Python versions and backports and such, like, is it possible that we try to vendor the code and it doesn't support Or they say they've already dropped support for, like, Python.
3… whatever the lowest one we support is, and then the code doesn't work.
Like, I know… I know we could kind of upgrade it at our own, but if they do a backport… don't do a backport for a security fix.
It's kind of the same situation as, like, using the dependency directly.
And also, like, this one seems like a pretty minimal usage.
We're… like, vending… I guess, like, for gRPC, it seems like rendering would be… A better approach, because we need pretty much all the library.
Whereas for this one, we're using something pretty small, so… What I was gonna ask is, is it possible to do vendor, but just for the code we need somehow?
Diego Hurtado (Dash0) 00:25:03 I mean, we… Depending on how the… design of… packaging is, right? Because, I mean.
we pretty much… what we pretty much do is, from packaging, import X, Y, and Z, right? And X, Y, and Z is what we do. It's what we use, right?
Now, are X, Y, and Z… contained in independent modules in packaging? I don't know. Maybe they do, maybe they don't. Maybe they… Depend on other internal models of packaging, and we end up, having to… Belina, pretty much… everything from packaging, right? So… Not sure.
Even… Even so, I think, Right now, there are pretty much two approaches.
Which would be… Implementing what we need from vendoring, sorry, from packaging.
Or, or vendor packaging, right?
The point that you mentioned about security… What do you say? Security updates, right? That we need to backboard, it's valid, yes.
It is true that, it's, essentially the same as having the dependency, right?
in the sense that we are still… Like, on the hook, or… Of, getting those backwards, but… but we would… be getting those backboards from the upstream package, upstream rendering any… anyhow, when we update vendor into, our rendering to a new… new version.
The… that's the same for both scenarios, for using the dependency, installing the dependency, or having our vendor dependency.
But the problem that we want to solve, the… The collision with the… The use of virtual environment is that we solve by… By having our… our… a render version of packaging, right?
Aaron Abbott (Google LLC) 00:27:32 Yeah.
Maybe, maybe I'll let Riccardo go.
Riccardo Magliocchetti 00:27:39 Yeah, I have a more generic question, so if you want to dig into the… Legal response, please go ahead, I don't.
Aaron Abbott (Google LLC) 00:27:49 Yeah, well, not that I had a more generic question, too, it was… it was gonna be, like, what's the… the end state of the vending like?
Oh, I saw the… is that what you were gonna ask too, Riccardo?
Riccardo Magliocchetti 00:28:00 Yeah, like, I see your packaging, and was wondering, like.
Are there any packages… other packages we need to vendor? Like, what's the big picture, or the end goal, yeah?
Diego Hurtado (Dash0) 00:28:12 Yeah, sorry, Aaron, are you gonna say something else, or… No, that's exactly…
Aaron Abbott (Google LLC) 00:28:18 That's exactly what I was gonna ask.
Diego Hurtado (Dash0) 00:28:21 Yeah, I understand the concern, Right now, I am thinking about vendoring, Three things, Well, let's… okay, let me start again.
I am now trying to find a solution for The dependency conflicts that we may have with, PyProto, JRPC, JSON schema, and package, right?
And I am stating it in this way.
Instead of just saying, I'm trying to vendor this Or things, because… there are several ways of fixing these dependency conflicts, right? Vendoring is one way.
the approach that, I want to suggest for JSON schema is different.
It doesn't involve rendering, it involves, Another library that, generates, JSON schema… Blah blah blah.
parser or something.
The approach for, bipRoto, gRPC, could be the… 15,000 plus.
line PR that, that is a pure Python implementation with With an absolute metric ton of testing.
And, for packaging, we could, could use Fandering, right? So, for… Fourth… For dependencies… And we could have 4 different approaches if we also consider that we may implement Or, or use, Rust, or… Rust-based implementation of PyProto or gRPC as well, right? So… Yeah, my philosophy on this is, tweet every dependency It's a separate case, I don't have any… Talk 3 in our policy that, we should get rid of all dependencies or not.
the, everyone needs its own separate, investigation and engineering and discussion and consensus and everything, so… So yeah, I'm trying to… I mean, I would like, of course, To have a solution for… all of those, PyProto, gRPC, JSON schema, and packaging.
the solution?
It's, probably gonna be different.
For everyone.
If… Of course, we even decide That, to, to change something, to not use the dependency rate.
Tammy Baylis 00:31:19 Lucas, hello.
Lukas Hering 00:31:21 One last comment, just so we can timebox this, but, something I think I brought up before is, like.
for, for example, for the injector specifically, like, I mean, it doesn't seem like users are complaining about compatibility issues, so if this is specifically for the injector.
we could, like, have you considered, like, creating, like, an open telemetry agent package that just vendors every single subdependency and just import rewriting. That way, like, you don't… like, that could live in the injector repo, for example, and we wouldn't need to change anything on our end.
Diego Hurtado (Dash0) 00:31:56 We already kind of do, I mean, that… that… that, I think, will be pretty much… I mean, Can you, Tammy, can you please open the, the OpenTelemetry packaging repo?
Tammy Baylis 00:32:18 Sorry, the, there's a question. Yeah, the…
Diego Hurtado (Dash0) 00:32:23 Yeah, there's a telemeter packaging repo.
Tammy Baylis 00:32:26 What, called packaging?
Packaging, packaging.
Diego Hurtado (Dash0) 00:32:31 Right, so if you go to… let me check packaging… Come on, Python… Bender.
Yeah, if you go to the source code, and if you scroll up, please… Go packaging, the packaging directory, please.
Common… Python?
Vendor.
The directory vendor, please? Right there. So, we have done that in the… I mean.
the injector is, I mean, at least for packaging, we… We have been doing this, packaging something that uses the injector, right? So… Actually… I think packaging is the thing that needs this the most, right? So we have done that. We have, kind of rendered our own implementations. So what I think, Lukas, what you're suggesting is, like, everything else, everything else.
Can we… Vendor it here.
In theory, yes. In theory, we could.
Then, we have tried to have it upstream.
As much as possible, right?
But… but yeah, this is also a possibility. It can get a little bit hard, to vendor downstream in more downstream projects like… like this one, because, for example, packaging is something that, gets used, In, the telemetric instrumentation, and… The amount of… Little things that we need to, vendor downstream, increases.
But, we also can do that. It's also actually something that we're doing right now.
I'm gonna be honest with you, I mean, right?
Lukas, did I answer your question?
Lukas Hering 00:34:49 Yeah, I kind of, I guess, so, so, so why exactly can't… so… why can't you do that with packaging, then? I guess is my question, like, the same approach, for…
Diego Hurtado (Dash0) 00:34:58 Yo.
We can do that. We would prefer to have it upstream, because the injector is not the only case.
Where, these dependency conflicts can, cause an issue for the user, right?
Regular instrumentation can also, I mean, a user that, is… is using, A version of packaging below, or… Below a floor, in… in the… in the puntolymetry instrumentation package can also get an issue. Json schema, in particular, is problematic because it's, it, it has a dependency with attribute, the attribute, the ATTRS package, and, at the same… same time, I think we have also struggled with, with, I don't know if it was PyProto or gRPC years ago, I remember, because of which version we support, and so on, right? So… So yeah, this is not only… a topic that matters for the injector Slack packaging projects, can also help us with our, day-to-day Limetry instrumentation?
But, I do want to be honest with you, the possibility of having this in the packaging, or… Repo all exists, but it will provide a less complete solution if you do that.
Aaron Abbott (Google LLC) 00:36:51 Yeah, I haven't fully digested the OTIP I shared, Diego, but one… one thing I noticed is, like, and somebody, please keep me honest, my understanding of the way, like, Java instrumentation works, which is probably the most, like, successful and… hardened, auto instrumentation and hotel.
Is that it… pretty much the agent they ship is, like, the thing where all the shading happens.
And you can only use a bunch of the instrumentations in the agent, whereas we have kind of a more flexible design where the instrumentations could be added, you know, dynamically.
It's Python, so you can do whatever you want.
So we kind of provide them on the basis that people might, like.
use them in, like, a typical, you know, I have a Pi project file.
Versus needing to do injection on the side.
And we have, like, one… we ship one artifact for that.
As opposed to having, like, a bundled thing with all the vending happening. So, I guess my question is, is that where some of the friction is coming from? Like.
If we had a separate artifact for the auto instrumentation, which was, like, a fully vendored you know, bundled thing. Would that make things a little bit easier?
Diego Hurtado (Dash0) 00:38:05 Mmm… I think, sorry, is what you're proposing… what are… what you're proposing is to have… The vendor removed, like, in the instrumentation package?
Aaron Abbott (Google LLC) 00:38:22 No, no, I think I'm trying to separate the two, because that's kind of what I'm getting at, is it seems like to achieve this rendering, we're putting it in the instrumentation packages, which are just.
Diego Hurtado (Dash0) 00:38:32 Huh.
Aaron Abbott (Google LLC) 00:38:32 Python libraries, effectively.
Whereas the approach, I think, for Java is there's a shaded jar that they ship for auto-instrumentation, and that's where All this stuff comes together.
Lukas Hering 00:38:44 Yeah, that was actually exactly what I was trying to get at and suggest. Like, we'd have an open telemetry agent package, which would have no sub-dependencies and vendor everything internally. Yeah.
Yeah, everything.
Aaron Abbott (Google LLC) 00:38:57 Yeah, including the.
straight.
Diego Hurtado (Dash0) 00:39:00 Okay, so, sorry, but, then this package… Would include all the instrumentations that we have As well, right?
Aaron Abbott (Google LLC) 00:39:13 Yeah.
Diego Hurtado (Dash0) 00:39:14 So people just go and basically Install this thing, and they get… Every instrumentation.
Every… every dependency is vendored, and That's also… and that's pretty much what Java is doing, right? That's what you say, but but then we… there is no… Testing.
for… the user, trying a new instrumentation of a node library, right?
I haven't considered this approach.
It sounds like it could work.
Lukas Hering 00:39:56 The injector is mostly… it's almost automated, right? Like, you wouldn't be doing that, right, if you're using an injector.
Diego Hurtado (Dash0) 00:40:01 Yeah, exactly. In fact, the injector is, is what I like to call automatic, automatic experimentation.
I mean, what you're suggesting, Aaron, and Lukas about the agent, about what Java does, is also another solution. I… I think it could also work, we could also explore that path, I… I am not a… just trying to vendor things. I mean, my major goal is to solve the… tendency problems that we have with, instrumentation.
Aaron Abbott (Google LLC) 00:40:41 Yeah.
Diego Hurtado (Dash0) 00:40:42 that works, I mean, that… we could also totally do that, yeah.
Aaron Abbott (Google LLC) 00:40:45 Yeah, I think… I think that's fair.
Diego Hurtado (Dash0) 00:40:47 Yeah, but… But on the other hand, we would end up having… like, two projects, right? The… I mean, the, the API, the SDK, and… And then, separate from that the instrumentation, auto-instrumentation, and everything else, so… This agent that we would be maintaining would have Android code, And, what about the exporters, for example, right? The exporters are not part of the… instrumentations, but they are also one of the things that can benefit the most from vendoring, right? Because of gRPC and a prototo, right?
Lukas Hering 00:41:40 Yeah, that would be in the agent. Like, I think Java does that as well. They'd enter… Or they shadow all their exporters, right, Aaron?
We've done great.
Aaron Abbott (Google LLC) 00:41:50 Yeah, I believe so, and I think it includes a bunch of contribib ones as well.
Diego Hurtado (Dash0) 00:41:54 Right, then my point is, why stop there? Why don't you put everything in the… I mean.
if, for example, the SDK has a dependency on Wrapped, for example, right? Why don't vendor that? Why don't just… One gigantic chunk that has everything vendor, it includes absolutely everything we do, and…
Liudmila Molkova 00:42:19 That's the point. Vendor everything. This is the self-contained thing that works in and validated to work together in…
Diego Hurtado (Dash0) 00:42:27 Huh.
Liudmila Molkova 00:42:28 The environments we care about.
Diego Hurtado (Dash0) 00:42:30 Exactly. My point is, why have any dependencies at all in any one of our components?
Liudmila Molkova 00:42:36 Oh, so for Java, how they work, they are… the main thing that gets the most usage is this agent, that's everything. Well, it's not everything, everything, it's just the curated side of everything that's here, that typical application needs.
And then they also publish instrumentation libraries, which are just the normal components, like we have them today. For example, they stabilized the distro, the agent, but they didn't yet stabilize instrumentation libraries, because they are worried about API and whatnot.
And this is the kind of easy path to get the stability and well-tested thing that works nicely together.
Diego Hurtado (Dash0) 00:43:23 Yeah. Right, it's more just a philosophical thing, because if we're gonna follow this approach, I kinda don't see any reason why I stopped there, and also vendor or everything, that… every dependency that the SDK depends on, and so on. Now, the other thing… I mean, but what I'm saying is, like, why even have libraries, right? They just… provide one thing, but… but that doesn't matter, right? We can discuss that later. The other thing is that I think there are a few environments that… like Lambda, I think, that… where this approach is not viable.
Am I right?
Lukas Hering 00:44:02 It should be. They would just need to replace what they have now with With the agent, they would just have a single package.
And then the.
Diego Hurtado (Dash0) 00:44:12 Right.
Lukas Hering 00:44:13 Let's install API.
But yeah.
Diego Hurtado (Dash0) 00:44:15 God.
Lukas Hering 00:44:15 Hardovers are probably timeboxes.
I'm not sure.
Diego Hurtado (Dash0) 00:44:19 Anyways… Probably other things to do, but thank you, everybody, for your attention to the subject and your comments.
Tammy Baylis 00:44:29 Yeah, thank you. We can talk about this next week.
Another topic from Lucas, enhancement, add-forward compatible instrument creation APIs.
with the PR, go ahead.
Lukas Hering 00:44:44 I think Seth, I think most… a lot of people already looked at this, but I just wanted to, It sounds like we're more aligning on, This first option here for adding, like, additional arguments for, for example, creating instruments, and then also for, Ludmila's OTEP for the span creation, So I guess the… the one question I had, or clarification at the bottom.
is how we want the specific crate with options to look like, whether we want it to be… A separate options object, or we can just have it have the keyword arguments, If you scroll down, to the very.
Tammy Baylis 00:45:26 Keep going.
Lukas Hering 00:45:29 Oh, apparently.
Tammy Baylis 00:45:32 Yours or Aaron's?
Lukas Hering 00:45:34 Yeah, so, like, We can, also use… That option, so… Yeah, but it's… so I guess just to… just to clarify, like, are we generally, in consensus that we… we want to do this, or is, like, does anyone have anything they want to say, or…
Tammy Baylis 00:46:02 Diego.
Diego Hurtado (Dash0) 00:46:04 Right, okay, just a question. So, basically, what you're proposing here is to have some functions, the… can receive, they accept an object, and that object can have, an undefined set of attributes.
Lukas Hering 00:46:24 Or it can just be extended in the future, that's the idea.
Diego Hurtado (Dash0) 00:46:27 Yeah, okay, so that seems pretty similar to… Just using KWRs.
Lukas Hering 00:46:35 That's why… that's what I was getting at. So we could just use the KWRs, which is what I put in.
It's a little more Pythonic, I think.
Diego Hurtado (Dash0) 00:46:45 Mmm… I think, KW Arks… is, right, Let, let me try to… Make an example.
Lukas Hering 00:47:06 Yeah, it's a little more ambiguous, the signatures, which I was trying.
Diego Hurtado (Dash0) 00:47:09 Yeah.
Lukas Hering 00:47:10 But it is… It's more Pythonic, and technically is a little faster, since you don't need to create that intermediate object.
As Aaron pointed out, so… I guess, yeah, I mean, we can just… I can table this if we're still not, if we still,
Diego Hurtado (Dash0) 00:47:30 Just a question, if in the future.
Let's say that we go with KWRX.
And in the future, we decide that one of those arguments Or my question is, like, let's say that we go with KWRCs, and we decide, And one of those arguments is, like, his name Fu, for example, right?
Can then, in the future, we decide to move full… To a… to a regular… named argument.
kind of promote it.
Did you go…
Aaron Abbott (Google LLC) 00:48:06 Comment here, at the bottom. The… There… sorry, one above that.
The… yeah, right there. So those two are, like.
those two signatures in the code snippet below are considered identical by, like, most type checkers, and also for the, you know, like, in reality, the real purpose of calling them, these two are identical. So we can… Implementations can move them out.
Which is also a bit faster, and the key thing is they have to keep this star star keyword args as, like, a fallback for future compatibility, which is a thing.
That we don't have, for the most part, right now.
Diego Hurtado (Dash0) 00:48:44 Right. In that case… in that case, kind of sounds like… Kid of the Arts?
Is this viable?
Lukas Hering 00:48:54 Yep. Yeah, the only call is that that argument we move out still has to be keyword only.
Like, like…
Diego Hurtado (Dash0) 00:49:02 You could also have, ARGs.
and KWRs.
Lukas Hering 00:49:09 Yeah, we could, but it gets a little messy if we had, like, private stuff.
Diego Hurtado (Dash0) 00:49:15 Okay.
Lukas Hering 00:49:16 In the supply, yeah, better to keep it as is,
Aaron Abbott (Google LLC) 00:49:20 Yup.
Lukas Hering 00:49:21 Fair enough.
Aaron Abbott (Google LLC) 00:49:22 Yeah, I wanted to call out one other thing, which we kind of discussed here, I don't know if… If everyone saw this, but… I… there's this init subclass hook, and… I'm… I'm thinking, like, I think Dylan was pushing for this too, but… if we do some… you know, it's… this is Python, we can do a little bit of hacky stuff.
I found this used in SQLAlchemy, for example.
And what you can do is you can force add the star star keyword args, like, fall-through.
At subclassing time, so… We could potentially reuse the existing signatures without introducing a breaking change.
Because this would rewrite the signatures at subclassing time.
Diego Hurtado (Dash0) 00:50:05 In its subclass.
Huh.
Lukas Hering 00:50:08 Actually, yeah, this is, like, really clever. Yeah, actually, it sounds really appealing, so maybe we can just, yeah, we can… we can stop the discussion here, but yeah, it would be nice, like, Aaron, if you wanted to… I mean, it looks like you have just, like, a full prototype, like, we can look at… Yeah.
Aaron Abbott (Google LLC) 00:50:24 Yeah. Yeah, sounds good, and it's kind of related to the stuff Limila was doing, so if everybody can just at least comment some agreeall… sorry, agreement on the issue, I'm happy to do this first part.
Lukas Hering 00:50:36 Yeah, I would be, like, 100%. Yeah, this, this, I think, would satisfy everyone's, everyone's, corals.
Okay, yeah, that's that. Yeah, the next one is just a general call-out.
I think Emidio reviewed this. I don't know if anyone else uses Valky, but I kind of want this, Bird.
Work on my employer, so, yeah.
Tammy Baylis 00:51:07 Chris, was this, a continuation of… Right, yeah, this is the one I was thinking of, so you've… You've taken control, thank you. Sorry.
Lukas Hering 00:51:18 Yeah, oh, I need to update the description, but yeah, the original Valky package we had to… I had to switch it to DelkiePie, because… The name was, like.
It was sniped, but it was also, like, posting malware, and under that condition, you can't, like, reclaim it.
with PyPy for some reason, so, like, we can't get that back, ever.
So, I've, updated it to Velky-pie.
Aaron Abbott (Google LLC) 00:51:52 Lucas, did you reserve this one in the PyPy account? I updated the instructions on how to do it in the repo.
Lukas Hering 00:51:58 Yeah, I need to… or, I can't remember if I… I can't remember if we actually just released a dummy package, or if we,
Aaron Abbott (Google LLC) 00:52:05 Okay, yeah, I think we could do it.
Lukas Hering 00:52:06 I can preserve it again, I think, yeah, yeah, I can work on that.
I ran into some issues, like, verifying, logging in, but yeah.
Liudmila Molkova 00:52:19 Not for the SPI, but would we be interested in having a conformance test for this in the conformance repo? There is one for Java Redis.
Lukas Hering 00:52:29 Yeah.
Liudmila Molkova 00:52:29 We don't have any for… one for databases there for Titan.
Lukas Hering 00:52:34 Actually, a separate discussion maybe I can talk to you about, but I tried opening a PR to add Valky to the database, like, Databases list, and it got, like, auto-closed.
Liudmila Molkova 00:52:46 Oh.
Oh, and semantic conventions.
Lukas Hering 00:52:50 Yeah, yeah. Let me find it. Different, but kind of related, but yeah, and then I tried asking, and, like, I didn't really get any responses, so I'm just like, okay, fine, I'm just gonna keep it as Valky, and just… but yeah.
Liudmila Molkova 00:53:02 Sorry, I'll find it, I'll open it, I'll approve it. It's just, The amount of select notifications,
Lukas Hering 00:53:11 Yeah, no, no worries. Oh yeah, it's in a different repo, Tammy, but yeah, I can, I can connect, offline on that.
Okay, yeah, that's all I have there.
Move to the next, next one.
Tammy Baylis 00:53:26 Yeah, thank you. Thank you for updating. Another from Diego, the documentation PRs.
Diego Hurtado (Dash0) 00:53:32 Right, okay, so… Our documentation is right now in pretty bad shape. We have… incomplete documentation, and we also have wrong documentation, right? So, I'm gonna be honest with you, I just, pretty much grabbed an AI agent and told him, told this agent.
Take a look at, our documentation.
Document everything.
That is not documented.
Takes a documentation… Any documentations… any documentation issues?
What I want at the end is that absolutely every function, every module, every class, every method, everything is documented there with their return, with their… what day they return, blah blah blah, so on, every argument, everything, okay?
And yeah, can I run other agents to review the work and so on, okay. Then, I… open the 1PR per component, and here we are. Now, I think Lukas commented that, We could use, maybe a better approach of separating documentation, something else, and so on. I think I haven't read that, comment yet, Lukas, sorry.
Yeah.
Lukas Hering 00:54:58 annoying.
Diego Hurtado (Dash0) 00:54:59 The point I just want to make with this is that right now, our documentation is in very bad shape. By following this approach, we can get documentation that is in much better shape. I don't promise it's going to be perfect, right? At the end of the day, it's a bunch of AI agents fixing this, but I think it's still a big Game.
From what we have right now.
So… Your comments, Lisa.
Lukas Hering 00:55:27 Yeah, just one, one really quick one. I think, like, documenting, like, the public API is, like, always a good thing, but, I mean, for private, I kind of debate the value, mostly because If you had Claude actually generate this, which it sounds like you did, then…
Diego Hurtado (Dash0) 00:55:43 Oh, yeah.
Lukas Hering 00:55:43 should be able to read and understand it already, right? Like, it's kind of, you know, you're just duplicating information, right?
Claude's pretty smart, right? So, if you have the code there, it already knows what's going on, it doesn't need an extra comment that was generated by another Claude, right?
And then, yeah, other minor things, like, I mean, it'll also maybe burn more tokens, not a huge deal, but… I guess, yeah, the concern is, like, if we document everything, you make a tiny change, also, like, you'll have to update all the comments in, like, a bunch of different areas, right? I just don't think, like, if we have a private function that's, like, two lines of code, and we have, like, 8 lines of comments on it, like, that's kind of going too far, in my opinion. So, yeah, those are just my thoughts.
Diego Hurtado (Dash0) 00:56:27 Yeah, it's, I just, I could, I mean, like, say, okay, let's document this, let's not document that, I mean, at the end of the day, it's a… It's cheap, it's just a matter of… And, it doesn't hurt, so I just decided, okay, just go out.
Document everything.
I know it's, I mean, it sounds like, maybe it's not necessary. If you prefer, if this is a blocker for you, I can undocument the private things, but, I mean, it's, I just thought, I mean, it's… Doesn't matter that much, just go and fix everything, and let's get done with this, but But if it's a blocker for you, I can… Undocument the private things?
Tammy Baylis 00:57:25 Riccardo.
Riccardo Magliocchetti 00:57:26 Yeah, I agree with what Lukas said, but also I would add that if I'm going to do this, I'll probably start with the API instead of the SDK.
Diego Hurtado (Dash0) 00:57:35 Yeah, I already have a PR for the API.
Riccardo Magliocchetti 00:57:38 Yeah, maybe, like, Bismosh… chance that people will look at API, and the agent will look at SDK, so…
Diego Hurtado (Dash0) 00:57:48 Right, just guys, keep in mind that our documentation right now, it's in a very bad shape, right?
It's still, better to have this.
Tammy Baylis 00:58:14 Okay, we'll come back to that offline. Also, I think last one, Lumila, about the OpenAI deprecation follow-ups, go ahead.
Liudmila Molkova 00:58:25 Yeah, thanks. So, we talked about it a little bit last time.
So, currently, the contrib instrumentation, the OpenAI one, we kind of deprecated it in the docs, in the repo. We never released the last version. The PyPi README doesn't talk about new package, but most importantly, it's completely broken.
It doesn't work with new OpenAI version, which it doesn't pin, so it's allowed from the PyProject TAML.
It doesn't work with the latest Util Gen AI, it also doesn't, limit the higher version. So this is, the stack of PRs that's split in four.
And the point is that with the first one, I'm just deprecating it in the docs and putting the upper limit on OpenAI.
This makes it a little bit, less broken.
We can release after this, for example, Maybe it was a little bit more. But, it… the question remains, like, what should it do with the new versions of, Sorry, what should it do?
Can I do anything better?
And the thing I'm proposing, I think we're probably similar to the bedrock one, is where we say, okay, this guy, for the new code pass will just be a proxy To the new package.
And if the experimental flag is on for GenAI telemetry, then it will just enable the new package, and this is the Second PR… Sorry, the second PR just removes… Sorry, it's complicated. So the second PR removes support for a new code pass altogether. It's not okay to release it after this.
But the third one, this is where we can kind of discuss what to do.
For the third one, it adds… dependency on the new package from Python Gen AI when this flag, the experimental flag, is on.
We don't have to, like, digest it all at once.
It's just, maybe we can talk about the idea of Old package, taking dependency on the new one, and then we would release it and deprecate it forever.
And it will be… it will appear on the PyPi that is deprecated, it would forward to the new package for everybody who installs it fresh. If there's still a lot of people who download and install it, the number of downloads grows.
And we want to… to offboard them from this one, onboard to the new one.
And this would be the pass.
Forward.
Yeah, I think, Riccardo, you raised your hand first.
Sorry for the unprepared speech.
Riccardo Magliocchetti 01:01:35 Nose. And… yeah, like, I haven't looked at the PRs yet, but once I've seen this in the topic list.
Have we checked how many downloads we have for new versus old?
I agree, we need to do something, because it's, like, 20 times more downloads for the odd one.
When the new one?
Liudmila Molkova 01:02:00 Yeah.
Riccardo Magliocchetti 01:02:01 And so… Yeah, whatever solution will be, like, we need to find something, because it's… a problem, I guess.
Liudmila Molkova 01:02:11 It is, and I… it's kind of… I'm most worried because it's broken, like, if you install everything latest, it allows you, but then it fires at runtime.
Aaron Abbott (Google LLC) 01:02:26 Yeah, I was gonna ask, do they have the same import paths? Like, OpenTelemetry.instrumentation.whatever?
Liudmila Molkova 01:02:35 No, this one is OpenTelemetry Instrumentation, OpenAI V2, and the new one is Open Telemetry Instrumentation, GenAI, OpenAI.
Aaron Abbott (Google LLC) 01:02:44 I see. Okay.
So if it forwards, it has to have actual code.
Like, to load from the other import path, right?
Liudmila Molkova 01:02:53 Right, yeah.
Aaron Abbott (Google LLC) 01:02:55 Okay. I wonder if we should move this one into Python Gen AI, if it's gonna have to be around for a while like that.
Liudmila Molkova 01:03:03 Oh, I see.
Aaron Abbott (Google LLC) 01:03:06 Or we could delete it from this after we do the release, I suppose. If it's just gonna forward forever, that would probably be okay, too.
Liudmila Molkova 01:03:12 Yeah, that was my point, to, like, do the final, release, that kind of helps you, it will pin all the versions, it would not, work on anything newer.
And we still promise some security patches for, whatever, 3-6 months, I don't remember. Maybe nothing, because it's the experimental one.
Aaron Abbott (Google LLC) 01:03:36 Yeah.
Liudmila Molkova 01:03:36 Yeah.
Aaron Abbott (Google LLC) 01:03:38 That sounds good to me, but it might be kind of hard with the version, because you'll have to keep bumping the lower version,
Liudmila Molkova 01:03:44 Why?
Aaron Abbott (Google LLC) 01:03:45 Oh, no, you're right, because we still would depend on the other one, which has the correct version specifier.
Liudmila Molkova 01:03:50 Right, and it will be pinned, so it's just one-time upgrade, it's just the… for users to know that they cannot upgrade this one, and, but it still works.
Aaron Abbott (Google LLC) 01:04:02 Okay, yeah, this stack sounds good to me, then.
Liudmila Molkova 01:04:05 Yeah, for the bootstrap gen, I think there is the… the cert PR. It removes this project… Oh, the bootstrap Jen.
It doesn't need to… yeah.
Riccardo Magliocchetti 01:04:18 like, we had a discussion with, like, who should generate the list of Jenna AI instrumentation available for our bootstrap tool, yeah. I don't think we never acted on that, but…
Liudmila Molkova 01:04:32 There is some hacky way that I've done in the CertPR, so that the old instrumentation knows that the new one is available, and then it turns itself off.
But maybe it's too hockey.
Is there, like, an issue I can read about the bootstrap generation?
See if I can do it better.
Riccardo Magliocchetti 01:04:54 I think we have a PR from… I can make the PR to the notes. I'll share with you.
Liudmila Molkova 01:05:01 Yeah, thank you, appreciate it.
Tammy Baylis 01:05:10 Okay, we are a little bit over, so we should close our meeting for today. And, thank you for so many hot topics today, this was great.
Liudmila Molkova 01:05:23 Thank you all.
Dylan Russell 01:05:24 You guys…
Diego Hurtado (Dash0) 01:05:25 Thank you.
Take care. Bye. Bye.
