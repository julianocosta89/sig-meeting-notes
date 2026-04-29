SIG: .NET SIG
Date: 2026-04-28
Duration: 51 minutes
============================================================

## Zoom Recording Transcript

**Julius Koval** 00:59 Hey, how's it going?
**Martin Costello** 01:01 Hey, Julius. Good, thank you. How are you?
**Julius Koval** 01:04 Yeah, the right, thanks.
**Martin Costello** 02:17 Just while we're waiting for anyone else to come. Hey, Alan, have you got anything to put on the agenda, Julius?
**Alan West** 02:24 Damn.
**Julius Koval** 02:27 Hi, Alan. Not really.
I guess I just wanted to… Okay, your thoughts on the PR?
If you have any that you haven't posted.
**Martin Costello** 02:41 I don't remember what I put on the PR when I reviewed it, but anything I said on it was it.
**Julius Koval** 02:49 Basically, I wanted to add, fastests, or whatever they're called.
**Martin Costello** 02:57 Oh, yes.
**Julius Koval** 02:58 Yeah, so I had Claude write something, and I'm trying to figure out what it does exactly, but it passes.
**Martin Costello** 03:08 But to be fair, I've used AI to write a lot of the fuzz tests. Basically, they just throw… Data at the functions to check that they handle unexpected input or don't crash.
**Julius Koval** 03:24 Oh, okay.
**Alan West** 03:31 Yeah, plus one to Claude. I bet he's in it a lot.
It's a pretty handy tool.
**Martin Costello** 03:39 I've been more of a co-pilot person myself, but It's all the same thing, really.
**Alan West** 03:46 Yeah, I've not used Copilot, but that's simply because… the company I work for doesn't pay for Copilot, it pays for Cloud.
**Martin Costello** 04:02 I don't know if Raj is coming or not.
**Alan West** 04:07 Yeah, I don't know either. There was a couple of things, that… I think Peter pinged us about, in Slack, and I haven't really had a chance to… Think about them, or… But one of them was logs-related, one of them was related to, I think.
It's a PR that he opened.
That presumably was meant to unblock something that Julius was working on?
With respect to timestamps, and setting the timestamps of logs?
**Julius Koval** 04:52 I agree.
**Martin Costello** 04:53 about.
**Julius Koval** 04:54 Yeah, so… One of the issues was that the Logs Bridge API didn't have observable timestamp.
as a property, so I wanted to add that.
And then I noticed that observable timestamp and timestamp should be null able, which they currently aren't.
So, yeah, I wanted to change that, but then Pyotr ended up making the change that… they won't be null able, but they'll be, datetime.mint date by default, I think, which I guess is equivalent, according to the spec.
Yeah, so that's SPR. That's the context, I guess.
**Alan West** 05:45 So… let's see, time… so… observable timestamp was… is not a part of our stable API yet, right?
He said we didn't have that.
**Julius Koval** 05:56 Yeah, that's right.
**Alan West** 05:59 But timestamp is, or is it just part of the, experimental API at this point?
**Julius Koval** 06:06 It's both.
**Alan West** 06:09 Okay, so it is in the stable API.
So that's… Likely why we can't just… Make it null able.
**Julius Koval** 06:20 Yes.
**Alan West** 06:23 Does… changing the default, as he's done, to min value. Again, I'm just kind of scanning over the PR right as we speak, just to get a sense of it, but it's changing the default value.
Is that a breaking change?
**Julius Koval** 06:44 No, I don't think it is.
I mean, I'm not sure… Water would break.
I can't think of a scenario, I guess.
**Alan West** 06:57 Okay.
I guess he says breaking changes.
Change pre-release version only.
I guess that seems okay to me, but I kind of question whether that's, I'd actually want to go look at the… Take a close read of the spec. I believe that the data model, probably?
Here, I can just share my screen since we're all just kind of, like… So, yeah, he said… represents an onset.
timestamp as defined by the OpenTelemetry specification. So I guess the thing that I would… the things that I'd want to look at, just to kind of, like, familiarize myself, or refresh my memory, I guess, of The spec is… So from the standpoint of the data model, I believe what he's saying.
at… a log record.
A log record's timestamp is likely optional.
Time's… TimeUnix Nano… The time when the event occurred.
Value… So this doesn't speak to any defaults, it just says… it just says that, Oh, I guess it basically is… this is indicating… kind of, like, null ability, right? Like, zero means that it's unknown or missing.
I think I see where he's coming from with respect to what this says.
And then observe timestamp. I'm forgetting, actually, what the heck that even… Is meant for, for events that originated.
In OpenTelemetry, the timestamp is… Typically set to generation time.
And it's equal to timestamp.
They're using a different term, timestamp versus, like, time unit stand. I think they're talking about this field, but it would be nice if maybe… This documentation was… cleaned up a bit. I think, I think it's referring to this field.
Prevents originating externally, This is the time when… OpenTelemeter's code observed the event.
So this might be, like, later than what this is, is, I guess, what this is saying. I think that's… interpretation. So you actually have a use case for this?
**Julius Koval** 09:50 Well, not really, I guess.
Pierre wanted to block stabilizing the LogsBridge API while there are deviations from the specs, so… That was my motivation.
**Alan West** 10:04 I gotcha.
I think that's fair. It's, So then I guess the question is… So this is the data model, like, okay, right? Like, it just explains the data model, but it's not… it doesn't necessarily describe what the log… API… Muster.
should do. So… let's copy this, because this is the… Let's just go see what the… Spec says about these fields.
So, it must accept the following parameters.
Marks a bunch of them as optional.
The operations defined include various parameters, some of which are marked optional.
Recired for each optional parameter, the… API must… Be structured to accept it.
But must not obligate a user to provide it.
For each required parameter.
So what I'm not seeing here… And I kind of would like… I'd like to see here.
is… Our current behavior is that It sounds like this is essentially optional.
And… When it's not provided, then we… the current behavior before, his PR.
is that we set it to daytime now, essentially, or, like, UTC now.
I'm not reading anything here that… Makes me strongly think that that's… that we're violating the spec in that way.
It sounds like it… it sounds like… You don't need to provide it, but we default it, essentially.
And this spec doesn't actually say what the default is. The spec here for the API, nor does the data model say anything about defaults.
**Julius Koval** 12:36 Yeah, I guess the point is that… This data model allows it to… Not be present, whereas we just fill in a default value, so… It'll always be present, I guess, that's the idea.
**Alan West** 12:56 Yeah, that's… that's a harder thing, too.
fix. His PR doesn't really fix that.
In the sense that, like.
Actually, this would be… I guess it does kind of fix it, right? Like, 0, zero essentially is January 1st, 1970.
January 1st, 1970 has the same meaning as zero, essentially, I guess.
That's kind of funky.
I guess I'll have to think about that a little bit more. I can respond to him in Slack.
Or on his PR.
Do you have any thoughts, Martin? In addition to, I guess, Just my rambling so far.
**Martin Costello** 13:54 I don't think so. I think this is one of those ones where… everyone else has a lot more existing context on them than I do, rather than I'm just looking at the change in the code and thinking it just seems legit.
Yeah, yeah, yeah.
**Alan West** 14:10 That's fair.
I was just curious.
Yeah, I guess the other question that I have on my mind is.
what have other languages done? I think he… I think he said that his PR reflects kind of what Go has done?
So I guess that's… that may be one data point.
I might poke it at another language or two.
Just for… just for funsies.
Okay, yeah, I'll just… I'll just comment. I'll… I'll speak with… I'll speak with Peter about this, and… Try to share my thoughts.
But Julius, from your standpoint, this is… this is not… really blocking, like… it's only blocking your work in so much as Peter shared the stance that he doesn't want to stabilize stuff without the, the timestamp.
Right?
**Julius Koval** 15:20 Well, I think this touches some of the same code that my PR does, so it would make sense to merge it first.
**Alan West** 15:30 Oh, okay, okay, okay.
Okay, good to know.
Then, yeah, I'll get back to… I'll get back to him on this, and then we'll try to… Close on a… on a path forward on… on this PR first.
**Julius Koval** 15:48 Although I was thinking that… I'm not sure what daytime.minValue is exactly, but… If it isn't… January 1st, 1970, then I guess it isn't correct.
**Martin Costello** 16:00 It's the 1st of the January year one.
**Julius Koval** 16:05 Oh.
**Alan West** 16:06 Oh.
Yeah, that's… Good thought. Yeah, I had just… I made the wrong assumption that it was 1970, but that… Hmm.
Yeah, that brings this even more into question, in my opinion. Let's, like… this… doesn't… really solve the issue, I guess.
I mean, I guess… I guess we could I don't know. It's like, this is only one part of it, right? Like, at the end of the day, like, from the standpoint of the data model.
If we wanted date time min to mean… Value 0 is sent over the wire, then we'd have to, like, change exporters or something like that, too.
You know, have, like, a special handling of daytime min, or… I don't know if he actually does that here. I'm not actually arguing that he should do that, I'm just, you know… Talking out loud. Oh, yeah, it looks like maybe he does.
Yeah, so…
**Julius Koval** 17:21 Yeah, so it might still be just easier to set it to January 1st, 1970.
So that he wouldn't have to handle that special case explicitly.
**Martin Costello** 17:35 I think it's more that… Min value is the default value of the type system.
So you, like, have to act… you, like, if you just do default over date time, you'll get the 1st of January year one.
You'd have to, like, go out of your way to make it epoch.
**Julius Koval** 18:00 Yeah, I guess that makes sense.
**Alan West** 18:05 Actually, what is… what is to Unix time seconds, or time nanoseconds?
do on daytime men, anyways. I'm just curious.
**Martin Costello** 18:14 I think that'll give you… A very large negative number.
**Alan West** 18:21 A negative number? Interesting.
**Martin Costello** 18:25 Because I think January 1970 is zero on that scheme. Yeah. So you get, like, 1,970 years worth of milliseconds.
**Alan West** 18:36 Right, right, right.
Interesting. I've never thought about these things before.
**Martin Costello** 18:44 I don't think any sane person would.
**Alan West** 18:52 Oh, okay, well, yeah, I don't… I don't… I don't know what my opinion is yet on… on this, but Thanks for talking… talking that through.
I guess I'll say I kind of have the opinion of, like.
why don't we just not touch it? But I don't know if that's… I don't know if that's right yet, I want to think about it a little bit more.
The other thing, What was the other thing? Oh, there, Raj?
Pinged us all about…
**Martin Costello** 19:33 I think it's Steve's one.
**Alan West** 19:34 Thieves, yeah… Not that one, but… Something to do with Context API.
Yeah, this one… I've not looked at, really, at all. I… I remember, like, way back, so… when… the… all the SDKs.NET included, was originally stabilizing.
The Trace API, or what, Trace API and SDK.
Which was… Then, like, back, back then, like, 2021.
The process that we all went through was that someone from the TC, Bogdan in this case.
reviewed our APIs, just, like, gave it kind of, like, a high-level review, and I think he opened up a few issues.
Some of which we just decided, meh.
And we didn't do anything about.
I'm assuming that this is one of those, from way back when.
Christian, Who's, this guy, Oberon.
He… has noted before that, you know.NET does not have a spec-compliant context API, and this issue being probably just, like, one small piece of NET not having a spec-compliant context API.
I think there's more to it than just this.
So that said, I think I… I think I share… Raj's… stands. I mean, I guess I'd want to know more, like… If… you know, Steve… Jumped on this because… He has, like, a particular use case.
that, he's blocked, by, because of the… because of the current behavior. If that's the case, I'd actually be very interested in… in learning more about that.
But if it was more just, like, looking this over, and… Okay, this issue looks like an easy issue to knock off.
I'd… Probably wanna, like, pause?
and look at the context API more holistically.
Because, again, I think that there's more to it than just this, and I… Be concerned that if we just narrowly look at this issue, that we're not… we may not… Like.
Take strides towards… a stable context API, or, like, a spec-compliant context API.
Which I think is the direction we should go if we're going to do anything at all.
So that's my…
**Martin Costello** 22:44 It looks… given what you've just said, it sounds like this issue is being a victim of It's a placeholder that everyone who looked at it at the time knows what it really means.
But it's not written in it, because, yeah, I think I marked it as help wanted, because I looked… went through all the old issues, and I was just like, seems fairly easy, follow this link, do that.
**Alan West** 23:08 Yeah, fair enough. I mean… And marketing as Help Wanted was probably, like, a good way of surfacing the fact that we're… That the issue is lacking information.
Albeit in an inefficient way.
**Martin Costello** 23:26 Yeah, I don't know if there's a specific motivation for Steve doing this one. I think when I looked at the PR, I just looked at it on the basis of it was solving what the issue implied.
But it was also one of those issues where I approve it, but it won't merge it, because there's a good chance someone will come along and go, oh, actually…
**Alan West** 23:48 Yeah, yeah, yeah.
Yeah, that's cool.
Yeah, I… I guess I'll probably ask on Steve's PR, like, hey, do you… you know, just… I'm guessing he probably doesn't have a discrete use case, but if he does, again, I'm all ears.
But if it's not solving a problem, anything anyone is complaining about, I'd probably pause.
That said, you know.
if we don't have an issue, maybe, maybe we have, like, multiple issues that are all, like, kind of, like, fragmented. Like, maybe it would be helpful to, like, have a… if we don't have it, as a… Like, a central issue on, like.NET does not have a spec-compliant context API, and we can kind of, cull together various concerns.
If they exist, on that one issue.
So that it can maybe… if it ever did become a priority, or if there were concrete use cases that people weren't able to solve today because we don't have a spec-compliant context API, then we can Use that issue as a… as a means for communicating and also potentially designing what we actually need, holistically.
A long time ago, I guess this is just one last comment, a long time ago, I had it… I had it on my mind to, like, oh, maybe it would be good to look at Java's context API?
Which this guy, Anarog, from the Java SIG, wrote years back.
He put a lot of thought into the context API that he designed for the OpenTelemetry Java SDK.
And it… I guess, from speaking with people in the Java SIG, it actually solved some interesting… like, an interesting gap that just the Java ecosystem had.
And, there's, I guess.
people using the OpenTelemetry Context API that aren't necessarily using OpenTelemetry, they're just using the Context API, because it's, like, this helpful… That's helpful, Component that they, Used in a variety of different ways.
And I had it on my mind to, like, you know, study that, and maybe see what it would look like to port it to, like, the .NET world.
just to kind of, like, try it on for size, because I think that it… the Java… the Java API is spec compliant.
I never did any of this.
I was only thinking about it from the standpoint of, like, oh, people are saying that we don't have a spec-compliant context API, but… the thing that I always wanted was, like, what… Are people not able to do today?
Given that we don't have a context API. I've never gotten, like, a… A strong… feedback or, you know, opinions from people on that. So I never really prioritize, like, you know, digging into that and trying.
trying to, like, port Java's solution to .NET.
All that to say… That's… that's the… that's the history of what's at least been on my mind.
on the, topic of, like, the context API and our non-spec compliance.
So I'd wanna… I'd wanna think about it more, I'd wanna, like, understand, the use cases more, and… Hmm.
Carefully design something, if we're gonna… if we're gonna endeavor into this.
**Martin Costello** 27:55 Yeah, I think that sounds fair.
**Alan West** 28:01 So yeah, that's my two cents.
Anything else folks want to talk about? Looks like…
**Martin Costello** 28:17 So, there's two things I'll mention, is I've created a milestone, like the one we had for the SQL client in Contrip.
Because there's moves to stabilize… excuse me, stabilize the Prometheus exporter.
So I've created a bunch of issues… Related to that some are… a couple are done, there's a couple in PR.
And the others I've put up as Help Wanted.
So, that's a… that's a thing I'm trying to move forwards.
Over the next however long.
**Alan West** 28:53 Cool.
Yeah, to be honest, the Prometheus exporter is something that I've not really involved myself in all that much.
the last I heard… Which was a long time ago, was that… Basically, stabilizing it was blocked because of some… discussions that were still happening at the spec. Do you know if, like.
basically, things are stable now. Our SDKs, like, shipping stable.
**Martin Costello** 29:22 premise.
**Alan West** 29:23 We have exporters now?
**Martin Costello** 29:24 So, I don't know about the other SDKs, but I do know that there's two other people at Grafana who are working to drive the spec towards stability, and parts of it are moving into stable, but I don't… I think the goal is to get the whole thing to stable, and I think they've got far enough along that they've got, sort of, the chicken and egg bit, where you can't stabilize it until enough people implement it, but people don't want to implement it until it's stable.
**Alan West** 29:55 Yeah, yeah, yeah. Yeah, sure.
Yeah, and I think the way that those things usually resolve themselves is that, like, spec advances to a State where, basically, it's, like, in a release candidate, kind of.
What is that? Is that the term they use in the spec? I think it's like a… yeah, I think they use the term release candidate.
And then… With enough prototypes.
And a little bit more discussion than they typically move it from release candidate to stable, eventually.
But cool, so it sounds like… it sounds like, yeah, there's work being done on the spec to… to move it… to move it towards stable, and then… and then you've got the work.
**Martin Costello** 30:42 Or if I did it properly, all the issues should link to the corresponding tracking issue in the spec repo of what we need to do.
Maybe not all of them. Maybe not.
**Alan West** 31:01 I just clicked on a random, whatever, you know, like, yeah, yeah, so here's… here's one to the… Review the stability requirements.
Yeah, okay, cool. Yeah, this looks great.
**Martin Costello** 31:13 And then… See, and then last week… we shipped… The releases that had all the security fixes in them.
amongst some other things, but that was the primary motivator. The last patch went out on Monday? Yesterday, for the Instana exporter.
Pyotes shared… all of the scan results that he did with, Codex, and all of those… so all the security ones have been done, and everything that's left has been reviewed, and either… we didn't think it was a real issue.
Or… getting another… getting me getting Copilot to try and prove it was an issue with the test, couldn't prove it was an issue, or there's a PR open, or has been merged to fix whatever it is. Some of the issues might… some of the PRs might fall into the bucket of.
there's context behind it that I don't know. So it might be that some of the PRs we might not actually take, because reasons But I've just viewed them on, like… based on the assumption that the codec scan said X is wrong.
And then Copilot has gone, yeah, it does appear to be wrong.
here's a PR. I've just done it on that basis.
**Alan West** 32:40 Gotcha.
**Martin Costello** 32:41 So, it might be that some of them, we just go, actually, it's that way because reasons, we'll just close it. But, we sh… unless something appears from the wild imminently, with zero knowledge, we should have got all of the pending security or security-adjacent stuff all sorted? No.
**Alan West** 33:04 Nice.
Yeah, that's great. Alright.
**Martin Costello** 33:14 Well, actually, just while I've got it on the screen, I just remember, does Steve open an issue in the last week related to the declarative convict stuff?
And something that I hadn't noticed… So I don't know the context behind this, is we've, like, a vendored version of the environment variable config provider in the repo.
Steve's proposing we undo that, so we use it from the NuGet packages.
But I don't know if there's some gnarly dependency issue Which is why it was done that way in the first place.
**Alan West** 33:52 Oh.
Like, this is sounding all vaguely familiar, yeah, we did… vendor something in. This was, like, something with the options API or something like that?
**Martin Costello** 34:05 So there's a different PR open for something from the options API, because I think there was a to-do comment in the code that said something like, after .NET 5, remove this.
So Steve's done that.
I don't think it's been merged yet, but then there's a different issue tracking why have we got a vendored config?
Thing.
Let me find the sh…
**Alan West** 34:31 my…
**Martin Costello** 34:32 I had it open a minute.
There's Issue 7141.
**Alan West** 34:50 Environment variables configuration provider. Yeah, it was probably just that we didn't want to take a dependency on this.
**Martin Costello** 35:00 Yeah, Steve's opened a PR on that. Like, I haven't approved it, but it seems fine, but… It… All hangs on the question of, should we do that?
Because I don't know if there's any context behind why it was vendors in.
**Alan West** 35:18 We were trying… look, yeah, I… we were trying to, minimize the number of external dependencies, and at the end of the day, it almost kind of became laughable eventually, because like… we… We basically, like, depend on… nearly the whole kitchen sink of, like, Microsoft extensions at this point. And it was actually, like, it was somewhat of a mistake. So again, backing all the way up to 2021, when… the .NET SDK released its first stable version that included, you know, just traces.
It, took a dependency on, whatever, like, Microsoft extensions like iLogger, or whatever it is.
**Martin Costello** 36:05 Yep.
**Alan West** 36:06 And… that… Has, you know, transitive dependencies of just, like, A ton of stuff, right?
And… I think… That if we were able to go back in time.
We… the SDK, we would have made the decision not to take a dependency on iLogger by the SDK?
But then, since we… we did take a dependency on iLogger. As we started venturing into, like, different areas, like configuration.
it became this kind of, like, slippery slope. Well, you know, like, we already have, like, iLogger, which has a transitive dependency to, like, probably, like, some, some, like, configuration stuff.
But, you know, maybe not… Specifically, environment variables, like, do we just… Do we just slide down that slope and just, you know, start depending on more and more and more and more?
And… I don't know. I don't know what the answer is, necessarily. I do know that, like.
people have had problems with the SDK before, with its… with all of its dependencies, conflicting, you know, with, like, their dependencies and whatnot.
So… so having a lot of dependencies, I think, does cause friction.
For some people.
**Martin Costello** 37:42 Yeah, we did improve that to a degree last year when we harmonized all the versions.
**Alan West** 37:48 Yeah.
**Martin Costello** 37:48 And I think Zero Code's also been doing a bunch of work around binding redirects and stuff.
**Alan West** 37:56 Right, and that group, yeah, the zero-code group, you know, that was… They were, they were, One of the groups that was most vocal about the fact that we had all these dependencies, and that it was making their life difficult.
But yeah, I guess… I guess that's the sense I don't necessarily have. I agree with you, I think it did improve, but I guess I haven't… I guess I haven't heard… too much recently. I haven't exactly been paying attention super closely, but, like, I haven't heard Recently, like, if people are still having problems, or if they're not, I guess maybe if we haven't heard anything, then that's a good sign.
So then, you know… It brings us back to this… This… Conversation that we've had over the years of, like, do we keep going down the slippery slope and just, you know, fully embrace like… the SDK already has all these dependencies, do we just, like, fully embrace, like, you know, Microsoft Extension's configuration and anything and everything that we might, you know, want to introduce? I think… I think part of… that determination?
I guess, I guess… I don't know. What's on my mind, like… sometimes I think it's a reasonable mental exercise to kind of, like, go back and… go back and say, well, if we had all this to do over again, then what would we have done? And then, like, get sort of a sense for whether there's any hope for steering in that direction, or not. Like… the answer may be that there's just no hope, right? But I think doing that mental exercise sometimes helps.
Kind of clarify… Things that we would like to see, so then maybe there's, like, you know, compromises that we can make, In this, in this situation, with respect to configuration, I think that, like… It'd be nice if configuration Was, like, its own separate package.
Like… If possible, right? Like, like the SDK, you could… you could use the SDK without any kind of, like, auto-configuration or… or whatever. But if you wanted that, then you'd take a… you'd take a dependency on, like, some auto-configuration package, you know, like a nice, like, division Of, of concerns.
**Martin Costello** 40:47 Yeah, I think… I think the one thing that… That idea has friction with is… implementing declarative config, I think it's just supposed to be, like, a core part.
adjust work. So if you have to bring extra dependencies on… along to light it up.
It doesn't… it's not in the spirit of what it's supposed to deliver.
**Alan West** 41:15 Yeah… Yeah, I guess, I guess, in some sense, it's like.
There are some things that are not in, like, the core SDK package.
But we still consider them parts of the SDK, like… like the OTLP exporter, for example.
is a part of the SDK. Should that be… should that, too, be folded into, like, one SDK package?
I might even… I might even argue, like, yeah, sure, maybe. I mean, like… like, the OTLP exporter is, like, you know, pretty core now, like, everybody's using it. As we currently have things structured, it does require somebody to take an additional dependency on it.
So in that way, like, the… the… Breaking things out into different dependencies.
It doesn't.
**Martin Costello** 42:12 I guess it's.
**Alan West** 42:12 really bother me.
**Martin Costello** 42:14 I guess, actually, you're right, because, the way things are now, if you… if declarative config was built into the main disassembly.
And you configured the app to export to OTLP?
If the OTLP's assembly's on there, nothing's gonna happen.
**Alan West** 42:32 Right.
**Martin Costello** 42:33 So, you would… so, excluding zero clutch, because that is a kitchen sink and does everything.
You would have to at least install OTLP to light that up. So, what's the big eight deal of bringing in the declarative config one?
**Alan West** 42:51 Right, right.
And also, to my knowledge, like, the vision for declarative config is that it should ultimately also support, like, custom components. Like, I should be able to, write my own exporter, or processor, or whatever, right?
And configure that via declarative config.
And in that circumstance, of course, you know, my thing is going to be a separate, you know, outside of the SDK package dependency.
Yeah.
**Martin Costello** 43:24 Okay.
So maybe when Steve's a bit further along with the design, maybe… We need to have a think about maybe spinning up a new experimental package for all that stuff to live in.
And then that could depend on the extra config packages.
**Alan West** 43:46 Yeah, yeah.
Yeah, again, I think it's one of these things where it's like.
it's… it's helpful to pose this as a question, like, in an issue, just kind of, like, as, like, something that we want to, you know, come back to and discuss, but I do think that, this is another one of those examples where we need… We need to see the full… the full vision somewhere.
And see how all these, like, little… little bits and bobs.
**Martin Costello** 44:12 Yeah, not to look at it now, but there is a PR that Steve's opened that he's… isn't intended to be merged and it's going to get closed. There's about 20,000 lines worth of… Clawed thinking markdown on how to design declarative config.
In there. I've only… I've only read the summary document, because there's far too much.
**Alan West** 44:35 Okay, okay, cool.
Yeah, that sounds great.
Anyways, yeah, I don't… I don't… I'd probably hold on… on, taking this as a dependency, at least at this point in time, until we… kind of get further down the path.
I guess the last thing I'll say is… On that topic of, like, splitting things out, that was, in part.
So this isn't, like, declarative config, but it's related to config.
Like… programmatic config.
Way back when, we… created this, Provider Builder Extensions?
package that… Basically, just has… A bunch of helper methods for configuring the various pipelines.
And, and again, we, we made the decision to… Split this out into a separate package.
Because at least, That was our thought.
that was our original thought, Back then, is that, like, configuration… could live… Or ideally, would live, kind of, in its own separate component.
So we were kind of trying to go down that direction, at least with these APIs here. And I think that there was, and… Blanche even did a… I wonder if I could… find it… He did this kind of, like, no-code… configuration… PR… it was nothing that we ever intended to merge.
But… That's not enough, I want to say something like… Autoconfig, maybe, was in the… Is this it?
Doesn't… Seem… environment sprinkled, blah blah blah… This is just about disabling stuff, but it was in and around this Time… I think he had another… Let's do config.
Anything else comes up?
I'm gonna have to dig around.
For a bit, but if I find it, I'll… I'll share.
I'll share it.
He did some prototype, basically, of… It was kind of… it was kind of declarative. It wasn't declarative config in the sense that it… Wasn't leveraging, like, the declarative config from the spec, but it was… Basically… demonstrating how to, like, bootstrap the SDK without code, which is kind of, like, a big part of declarative config, right? Like…
**Martin Costello** 48:41 Yep.
**Alan West** 48:42 Basically.
Declare what you want somewhere else.
I think, I think he was playing around with just, like, you know, like, eye configuration and whatnot.
Anyways, I'll try to find that, because that might be a helpful… thing to look at, as part of that work, too. I can share that with… With the group, and with Steve, and whatnot.
**Martin Costello** 49:07 Okay, cool.
**Alan West** 49:09 Okay.
That's all I got.
**Martin Costello** 49:18 And nothing else for me. Anything for you, Judas?
**Julius Koval** 49:24 Just maybe, Alan, could you take a look at the PR that Martin linked?
just… to get another set of eyes on it, I guess.
No, I meant the one in the notes.
**Martin Costello** 49:49 That is the one in the notes.
We were talking about that one.
**Alan West** 49:53 Yeah, this is the one that we, you said you have a PR open, Julius, that basically you think this PR should merge first, or we should…
**Julius Koval** 50:02 No, I meant, if you go to pull requests, it should be more or less at the bottom.
**Alan West** 50:08 Oh, okay.
**Julius Koval** 50:10 Yeah, the serializing key value lists.
**Alan West** 50:17 Oh, wait, that wasn't the one?
This one.
**Julius Koval** 50:20 Yep.
**Alan West** 50:25 Okay.
Is this the one that you were referring to earlier? Where you were saying that, like… Peter's PR.
**Julius Koval** 50:33 No, there was something different.
**Alan West** 50:35 Oh, okay, okay. So this is about key belt value this.
**Julius Koval** 50:39 Yep.
**Alan West** 50:40 But there was another PR from you that you said was… Blocked until this one merges.
**Julius Koval** 50:48 Yeah, it should be here somewhere, just can't see it right now.
**Alan West** 50:54 I see the bottom two are yours.
Those are the only ones that I see.
from you.
**Martin Costello** 51:03 I think the one… Judas has got 3 open, and the oldest one is 6979.
**Julius Koval** 51:10 Yes.
**Martin Costello** 51:14 It's probably gone onto page 2.
**Alan West** 51:17 Oh.
Multiple pages, I got it. Alright, alright.
I got it. Okay, observe timestamp. Yeah, yeah, yeah, this is what we were talking about. Okay, thank you.
Got it.
Okay.
**Julius Koval** 51:31 Yeah, so that's all for me.
**Alan West** 51:33 Sounds good.
Virgil?
Talk to you soon!
**Martin Costello** 51:37 See you next time. Bye.
**Julius Koval** 51:39 Bye.
