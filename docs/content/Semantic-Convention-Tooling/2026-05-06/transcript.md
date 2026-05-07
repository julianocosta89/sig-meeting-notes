SIG: Semantic Convention Tooling
Date: 2026-05-06
Duration: 41 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 07:30 Hello, hi folks.
**Jeremy Blythe** 07:32 Hello.
**Laurent Querel** 07:34 And
**Jeremy Blythe** 07:40 There's always a note-taker.
**Liudmila Molkova** 07:46 This… this one comes to every meeting, it will leave us a comment saying that we… Can FF believe him?
Oh, let's see… We.
**Jeremy Blythe** 08:18 Excuse me.
**Liudmila Molkova** 08:28 Okay… Does anybody have any items on the agenda?
**Laurent Querel** 08:46 Maybe, yes, on my side, I think, I will have a question.
Oops, sorry.
Okay.
**Liudmila Molkova** 09:11 Oh yeah, Josh did some… Plan triage, it seems.
Sorry, I've been spamming, I've been trying schema V2.
And fix… fixing issues.
this.
Copilot.
I'm sorry.
**Laurent Querel** 09:42 Oh, we are all doing that, no worries.
**Liudmila Molkova** 10:21 I'm.
**Laurent Querel** 10:21 Like I said in the… In the chat, If we stop after 30 minutes, I will be able to… I will be able to use the next 30 minutes for review. What are the… the PR you think needs to be reviewed, sooner than later.
**Liudmila Molkova** 10:43 Yeah, so, first question I've had is, when do we release? And then the question is, what we can do before the release. So, Zhao… Who works on semantic conventions, who added metric requirement levels, just added just asked if we… if we can release VWERB, so we can start using it, in semantic conventions.
I think we released recently, but… Could… What does it take to release Weaver?
How hard is it?
**Laurent Querel** 11:31 It's not hard.
Basically, we have to tag To create a new PR, update, update the versions, in different places, create, push with the PR, if I remember well.
I didn't, yeah, there is.
**Jeremy Blythe** 11:55 The instructions you wrote, like, whenever you wrote them, I'm assuming you did it wrong. If you follow those.
**Laurent Querel** 12:00 Yeah, exactly.
**Liudmila Molkova** 12:02 Okay. Okay, cool, so then I should be able to do this, there is no secret sauce.
**Laurent Querel** 12:07 No. The only thing that, I don't know if it's required or not.
But, we… you should have a way to sign, your… your PR.
Push a sign tag.
That could be sometimes tricky, but, these days, with, plot code or ChatGPT, it's pretty easy to figure out how to do it.
That was sometimes tricky to do before, but…
**Liudmila Molkova** 12:41 Yeah.
**Laurent Querel** 12:41 I don't think it's normal, it's no longer the case.
**Liudmila Molkova** 12:45 Yeah.
So then, I think, let me… I will try to release… Fri- on Friday?
If anybody's around to approve a school, next week is also fine, but I'll start on Friday. And I… I would like to… GET.
this two in, because there are bugs in V2. Oh, Josh already approved this one.
**Laurent Querel** 13:18 Okay.
**Liudmila Molkova** 13:18 Okay.
So, if you are.
**Laurent Querel** 13:20 Oh, the other one is… so the 140 one?
**Liudmila Molkova** 13:26 I'll just put them here.
**Laurent Querel** 13:28 Okay, great. Thank you.
**Liudmila Molkova** 13:36 And… friend… I think that the PR Josh left, is still a work in progress, so I'm not sure if.
**Laurent Querel** 13:51 The one I checked yesterday was about, the multi-registry, he was still working for us.
**Liudmila Molkova** 14:01 Yeah.
This one.
**Laurent Querel** 14:05 Yeah.
**Liudmila Molkova** 14:07 Let's ask if Josh wants us to review that one.
**Laurent Querel** 14:13 Yeah, I can, I can ask.
**Liudmila Molkova** 14:15 Oh, yeah.
**Laurent Querel** 14:18 the 1377, 77… Just ask.
**Liudmila Molkova** 14:34 Wait, I think I left to… Let's… Fish… One of them is not… 12.
Wow.
Yeah.
And I think, Jeremy, you also had a PR, right? For… The…
**Jeremy Blythe** 15:14 Well, I… I only do giant ones, so… I've still got my dog fooding one from ages ago, which… I thought it was really cool. And then we talked about it, and we wanted to make sure that it wasn't, sort of, self-referential.
So I did fix that.
so it uses the… it will need updating, because I haven't touched it for a while, so it'll be out of step with main, but it'd be cool if, You could take a look, Lauren.
Okay. The other one, the other ones are higher priority than this, So, if this doesn't get in, don't use your half an hour right now to do it, but, like, maybe sometime.
that would be cool. The other one I did is… really big, and I'm a bit unsure of, but if you want to cross your eye over this… Actually, I would never have contemplated making a prop macro.
to do this, but with Claude, like, that… the proc macros are kind of really ugly thing to do, but with Claude, it's like, oh, actually, I can do this really nicely.
So now… you can, define… this… this complex thing about having config that is in a file that you override with the CLI, and you need to have defaults. Now you can just put extra annotations in your arguments struct.
And then… the Pragmatra makes all of the magic.
Which is kind of nice.
Yeah. I'm… If you take a little… if you have time.
A look on that would be interesting to get your feedback.
So yeah, so if you, if you go look down at, say, emit.rus at the bottom left of your screen.
All the way down there.
**Liudmila Molkova** 17:18 I meet.
**Jeremy Blythe** 17:20 Yeah, so that's one, as an example one.
you'll see that, like, you just put these extra pieces in, so you give it Weaver command, and then you say whether it's a shared thing, like the registry policy thing, or whether it's a config option.
Like, if you look at, standard out, that's a config option that has a default.
And so it's a mixture of things that you specify in CLAP, and then you put these extra annotations, and then that will then create the structs that you need, that then go into the JSON schema, that then you can, use the, plugins in VS Code, then you can write your TOML, everything kind of… Works back on itself, but all… but all you do, pretty much.
is you… do this, and I think in the README clause and I have a guide.
as a… has a, As a developer writing a command, the steps that you would have to do now.
There's a README there somewhere.
Yeah, the config one, I think, is where I put it, actually.
Or maybe… yeah, that… there you go.
So if you go to the top of that, you'll see, it tells you that there's an example, and… Anton.
**Laurent Querel** 18:42 Okay.
**Jeremy Blythe** 18:45 I think it's quite nice.
**Laurent Querel** 18:47 Yep, looks like, squirrel.
**Jeremy Blythe** 18:51 I ended up… it was… what was cool was I wrote all of the stuff, so I wrote a trait… so that you implement this trait onto the, you know, the clap struct that you had. You have that implementer trait, and then in there you put all the code that you needed to describe the overrides that you want.
And I had all of that, and then I had all this boilerplate everywhere, and I went, oh, okay, make a proc macro to create that boilerplate.
And then all of that disappears.
So that was the kind of flow I went through.
**Laurent Querel** 19:22 Yeah, that's nice.
Yeah, It's… I mean, having this bridge between the… the CLI parameter, the total configuration file.
The section that you have there, yeah, that's cool.
**Liudmila Molkova** 19:41 Yeah, it's really cool. And Vivaract Black life check is making a lot of adoption lately.
**Laurent Querel** 19:48 Yeah.
**Jeremy Blythe** 19:50 Yeah, I love it. It's great.
I'm conscious that I make these peers, and then I've… I'm, I'm not doing as much reviewing as I should, so I'm gonna try and… I'm gonna try and consciously switch to, like.
contribute more to the reviewing than just having fun making huge PRs.
**Liudmila Molkova** 20:17 No, it's so much thrill to make a huge pair.
Yeah, so then, I don't know about Josh's one, it's probably one to make it to the… Release, but we can try to make… Some of… this in… And then on Friday.
I'll try to start the release.
And… If something happens to… be merged before then, for those to be in the… in the early… sorry, I'm sleepy.
**Jeremy Blythe** 21:07 There was a… sorry, there was somebody else from Hotel Arrow, and that's your… that's your stuff, right, Lauren? Yes. Someone from Hotel Arrow said in the chat, hey, can we have a release as well?
For something.
Come on.
**Laurent Querel** 21:21 Oh, yes, that was David, I think. Yeah, there you go. Because I asked him to work on the security issues.
We talked about that two weeks ago, and I told this group, basically, that I will work on it. I didn't work on it. I asked one of my team members to work on it, and then he was able to fix the various It was mostly, building and adapting the APIs.
And then almost the security, vulnerability, go away.
Yeah, so… I think that you are talking about in, I guess.
**Liudmila Molkova** 22:09 And this is a person called Sarosh Kumar Patra.
But anyway…
**Laurent Querel** 22:15 That's Augustin.
**Liudmila Molkova** 22:19 But… Anyway, so…
**Laurent Querel** 22:23 Yeah, that's on his office.
**Liudmila Molkova** 22:25 So we want… More than one person wants to release, that's awesome.
**Jeremy Blythe** 22:31 Yep.
**Liudmila Molkova** 22:39 Cuir.
Do… Lauren, you wanted to talk about metrics, set, support, and semantic conventions?
**Laurent Querel** 22:47 Yes, so maybe, can I, share my screen?
**Liudmila Molkova** 22:53 Yeah, of course.
**Laurent Querel** 22:54 Okay.
And then I will, I think the best way to do it would be… Okay, Is it, big enough?
Or I can reduce it.
**Liudmila Molkova** 23:29 Oh, that's good.
**Laurent Querel** 23:31 Okay.
Entry to… It seems… So I will show you and give you some context, Sorry, I should have prepared that. Okay, channel metrics, that's a good example, I guess, of pipeline metrics.
Yeah, that's an example. Okay, so, We, for the Hotel Arro project, which is a Rust-based project.
We… we don't use directly for instrumentation.
We don't use directly the rest, Hotel collector. The hotel SDK, sorry.
One of the reasons is… Performance?
We… we really want to… Make sure that instrumentation, in our case, is close to zero in terms of overhead.
And, and, That's one thing. The second thing is, the most important instrumentation in our system are metrics.
And all the metrics are metric set.
Meaning that… For default entities into the… into the system.
We… We have multiple metrics that are collected all together with the same timestamp, the same set of attributes. Attributes representing an entity in that case.
An entity could be a node, like a receiver, a processor, an exporter, could be the entire pipeline, could be an engine, the controller that is managing those pipelines, and so on.
So the… so the goal is, let's define for a specific entity.
A bunch of metrics that are correlated together, because they belong and are basically an observation of the behavior of a specific entity.
So here we have… a metric set.
This metric set is composed of multiple metrics. Here you have, let's say, 10 of them.
Yeah, we have some… Tokyo one-time matrix.
Some of them are mandatory, some of them are… Optional.
But you see, sometimes we have metrics that are something like 30 to 40 metrics altogether.
So the benefits of that is when we have to report For all the entity into the system, periodically, every 5 seconds, we just report the number So, let's say for this, basic example, we have updated, observe contours, contours, gauge… Sometimes we have, kind of histogram, They correspond to one number for each.
So we, we basically report One identifier, which is a number for the metric set.
And the corresponding batch of, Values for the metric, plus the timestamp.
And only that.
So imagine that we have Hundreds of pipelines.
Thousand and thousands of, of, of, of, nodes.
We generate a tremendous amount of metric, in fact, in the system, and with this approach, it's close to zero in terms of, In terms of impact.
So, the… but right now, the approach is we define that in Rust, we have macros, thank you, Claude, or thank you, Codex, like you said, Jeremy, super easy to generate this macro.
And, and from there, we are also able to generate semantic correction.
So the… all those metrics, all those events, all the… we don't really use traces right now.
But they are auto-discoveryable, so they are exposed.
With a semantic convention, format.
with the… the, let's say, the drawback for metric, that we have to convert those metric sets into any variant metrics.
And that becomes not super well aligned, because we have Multiple metrics with exactly the same attribute set.
So… and the next… so that's… that's one thing, lack of support for metric set in, semantic convention.
And the second thing is, if we have… if we had, a support for Mitrix set in 7T Convention, then with Weaver.
And also, you'll see in the river.
Then, with River, I will be able to generate all this code.
And get rid of this black hole entirely.
And then we will have a beginning of a super-fast, Client SDK Forest.
So that's why I'm asking if we could consider A new, object, a new group.
into the semantic convention that… give away to represent metric sets.
Which are a group of metrics sharing the same attribute.
That could be a composition of univariate metrics sometimes. I mean, or even all the time.
If they… they really share the same metric… the… the same attribute set.
**Liudmila Molkova** 29:41 Yeah, it's a cool one. The trick is, they're not in OTLP, right?
So, what does it mean to have a metric set defined in semantic conventions?
for people who use OTLP.
**Laurent Querel** 29:58 So, my proposal will be the following, there is, A mechanical way to move from, univariate to multivariate, and from multivariate to univariate.
So, if we… If we specify in semantic convention registry a metric set, That will just… simplify the life of a semantic convention hotel, because, let's say you have a set of metrics, they share all the attributes, you don't have to… To repeat the fact that you make a reference to the same attribute, the same attribute set, same attribute group.
But that could be consumed as individual, univariate metrics.
For people, that it's just a way to group things that share the same attribute set And the translation into OTLP will be just immediate metric. You will pay the cost of Specifying again and again the same attribute set.
But that's what it is today for OTLP.
For… for us, we will be able to leverage this, interconnection between the metric… the univiat metric.
And we will build… A real metric set.
In order to remove this override of having to redefine and to encode, decode attribute set for each of those individual metrics.
So, I think that there is no real, in my opinion, but maybe I'm wrong, there is no real, issue even for people that It's not the technical.
**Liudmila Molkova** 31:51 issue, it's that, more like a spec issue, so I think if you're introducing some form of Autel SDK that produces metric sets, then this should be in the spec. Maybe it's just an API that… and then implementation can… Represent them in different ways.
And then… There should be something that explains that These guys should be represented as individual metrics over a current version of OTLP.
And that… it's a no-brainer.
Of course, we should introduce them in semantic conventions. But then, there is another, possibility that… We say, okay, this is some form of experimental feature and semantic conventions, we're experimenting with it.
And, we will not allow it, and, unless you, like, it's behind some feature gate.
I think you, you like metric sets enough.
that… we should try to put them in the spec. And I think something is happening there that's really…
**Laurent Querel** 33:02 When you say spec, because that's very, very broad, when you say spec, do you mean spec for semantic correction, or do you mean spec for OTLP and all the other things?
**Liudmila Molkova** 33:14 That's the.
**Laurent Querel** 33:15 You know the time that I'm able to spend on Weaver today. It's close to zero.
That will not change soon.
So.
**Liudmila Molkova** 33:26 Well, I mean, you have Josh McD, who is a TC member, and he's the right person to work on this specification. I mean, OpenTelemetry specification, the metrics API should include metric sets.
**Laurent Querel** 33:40 It's a… yeah, okay. Yeah, we already talked about that, yeah, okay, so I… Yes, I will work on that, but my own, let's say my need is… a little bit more, I have some other ways to deal with that. I could use a notation and just put, A tag to… let's say, int the Weaver generation that a set of metrics belong to the same metric set. And then, we will check that the attribute, are the same, and we will just generate the code. That will be the fastest solution, it's not… if you see, it's not the… the best one, but that's one that's from where I can generate the code tomorrow if I want.
The spec, approach.
I will work on it.
But I know how that works. I did that for multiple, things inside OpenTelemetry. That will take forever.
Look at the, the multi, the multi-registry stuff.
And the one where.
**Liudmila Molkova** 35:00 Don't, don't tell me, I know that.
years.
**Laurent Querel** 35:03 To do something this big.
It's the best thing to do, but it's just too long for me.
I'm too impatient.
**Liudmila Molkova** 35:12 Yeah, I'm sorry.
**Laurent Querel** 35:13 But I mean, I will work on that, but don't count on me for that, to do that tomorrow. That's just my message.
**Liudmila Molkova** 35:21 Yeah, of course, and I don't know if Josh McD has any interest, but he has all the opportunities to… Make it faster.
**Laurent Querel** 35:31 Yeah.
Okay, so, Honestly, I think that the metrics set are a very big, important, for ears problem inside OpenTelemetry, and tried to convince people inside OpenTelemetry now for years, from the beginning of the… not this project, the hotel-level project that, in fact, started before Weaver.
And and… and we are, and we are still there.
**Liudmila Molkova** 36:04 Yeah.
Sorry, it seems we all need to drop.
**Laurent Querel** 36:09 Yeah, okay, thank you.
**Liudmila Molkova** 36:11 Yay, thank you.
Sorry for this.
**Laurent Querel** 36:15 No problem.
