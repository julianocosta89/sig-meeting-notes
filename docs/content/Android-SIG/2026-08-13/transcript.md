SIG: Android SIG
Date: 2026-08-13
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Jason Plumb** 02:42 Well, I know that I've changed my meeting, with the new link, but clearly I haven't.
**Hanson Ho** 02:51 I went to the dock to find the link.
**Jason Plumb** 02:54 That's a smart thing to do.
**Hanson Ho** 03:03 Has put little cover…
**Jason Plumb** 03:05 Go ahead.
**Hanson Ho** 03:06 Oh, has Portland recovered from the, the fires? Like, can you breathe again?
**Jason Plumb** 03:10 Yeah, I mean, they're still… they're still blazing, but we got lucky, we had the coastal wind to kind of push things, like, on that side of the mountains, but it's… It's rough out there, like, you know, summer camping is ruined for a lot of people.
But at least I have the windows open right now, that's good.
**Cesar** 03:31 Hello?
**Jason Plumb** 03:33 Hello.
I'm still getting set up, one sec.
Oh, man.
Okay.
Where are we?
Sorry for that delay.
Okay, pretty light agenda, so let's, invite anyone to add stuff that they might have for today.
Dude, first do a PR bump on this thing.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 04:58 This is a PR just to update the demo app, the decompose navigation instrumentation that I added most recently.
**Jason Plumb** 05:06 Cool.
Cool, cool.
Yeah, that should be… that should be pretty straightforward, I think. Cool. Yeah.
Nice. So you're also using the demo app, then, to sort of kick these features around, see how the telemetry looks?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 05:20 Yes, I used the consumer there, yeah.
It's pretty funny. Yeah, it's really…
**Jason Plumb** 05:27 It's really, yeah, exactly, it's pretty, pretty helpful.
speaking of the demo app, I really want to continue shoring that thing up, you know, like the… the integration with the actual OpenTelemetry demo would be so nice to have, and I think we've got some issues open for that. It's definitely on the roadmap as well.
I'm sure that we saw that, but… Let's see… yeah.
So it'd be… it'd be real nice to do.
The other thing that's also a problem for us on the client side of things with this demo app is that we don't have a good… like, RUM backend, you know, like, for other languages, other instrumentation frameworks that, like, generate traces, like, cool, put it in Jaeger.
send the logs to whatever, to OpenSearch, or whatever they're using, and then, you know, see the data, that's… that's great, but, like, for us, we really want to see, like, a session timeline, some sort of, like, RUM view, but… We don't really have that.
But it would still be cool to get it integrated at some point.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 06:39 Does, any other… library, or, Is there a reference implementation? Like, how do we go about doing it? Like.
Do we use any, specific backend? Like, any, any, any, I mean, we… internally, we use Grafana.
**Jason Plumb** 06:56 Right, yeah, I think we'd want to try and keep it vendor neutral to the extent that we can.
I think what… there used to be a diagram… I think…
**Hanson Ho** 07:10 The problem isn't, especially for a demo, the backend. Any backend will do. The problem is there's no, canonical UI, to display, you know, session data. Right. Vendors have some, and different people have different opinions about how that stuff should work, but what you want to see is a session, and you want to see things happening, you know, you know.
But how do you overlay? How do you do traces on top of logs, on top of… you can show, you know, a big timeline, and then… It's… it's a… it's a UX problem. There's no… there's no, you know, open source, free UI to visualize this data, or even accepted, UX patterns.
**Jason Plumb** 07:58 Yep.
That's very true.
Now, we could… we could contribute something, right? Like, Jaeger might be open to us contributing, or not us, but someone in the community building or contributing some sort of, like.
very, kind of, lo-fi, incrementally built, like, session display? Like, they might be open to it, I don't know, but maybe also Jaeger is maybe not the right target for it?
**Hanson Ho** 08:23 Seems like an extremely fun project, that is 9th on my list of…
**Jason Plumb** 08:28 Yeah, I know.
**Hanson Ho** 08:29 I would be interested, like, genuinely, but…
**Jason Plumb** 08:33 Yeah.
**Hanson Ho** 08:34 As many things.
**Jason Plumb** 08:36 Yep.
Okay, cool, yeah, that doesn't look like it should be a huge review. Thanks for bumping it, I think we can do that.
Since the agenda is pretty light, let's just look at… Other… if there's any new issues, or issues that people want to talk about… I thought this one was pretty interesting.
The idea was that some users may not want some of these attributes, including the session, which I found very interesting. I don't know what the use case is that you don't want a session, but maybe you just want some… manual, like, instrumentation, and you just want some stuff, and you don't really buy into the opinionated story that we're giving them, so… we don't have a way to filter those right now. So we talked about that maybe last time.
And no real… new, PRs, although this one is exciting.
And I have not reviewed this one yet, either.
But it looks like Jamie has, and for that, I am very thankful.
Cool, yeah, I'm excited about this.
**Jamie Lynch** 09:53 I think there was actually a question for you on this around… I think it's about OpenTelemetry testing extensions, and whether we Yeah, I guess, like, how we want to use it and the ultimate… Incarnation of this, Yeah, I feel like, for me, I'd be pretty happy just getting this PR merged as is, but I want us to agree on a direction for it to go on, go in before we do that.
**Jason Plumb** 10:26 Got it. Yeah, give me… give me an opportunity to look at the PR and see how it's using… are they using Mock Server?
mock web server… Before responding, and then also look up and compare how we're doing it in the other instrumentation.
Trail forward responding.
And also maybe have more than zero sips of coffee.
Okay, cool, yeah, I will, make a note of that one, too.
Oh, I'll bring up one more thing that I've been thinking about, which is… Whoa, that font's got… Incorrect.
So one thing I've been thinking about is the fact that we have all this nice, like, semantic conventions and Weaver stuff now that we're generating.
Which includes Both our locally scoped semantic conventions, and also Borrowing, pulling in stuff from upstream.
Because, you know, that's… we're rooted in that federation.
And how that might relate to our instrumentation READMEs. So, we've done a pretty good job of building out the descriptions of what's in each of these.
So it's pretty easy for a user to find this stuff.
It's also pretty easy, as we improve these, for these to fall out of sync with what the code is actually doing.
And… it's also easy for this to kind of be inconsistent, like, it'd be easy to, like, omit, I don't know, the type or something, right? If we're just… if we're just… this is, like, ad hoc, right? There's, like, no real defined format here. And I want to contrast this with what some of this stuff is done in Upstream.
with this cool stuff that Jay DeLuca has put together.
which offers these metadata YAMLs, and so for each instrumentation module.
You can provide some interesting details about what telemetry it produces, what semantic conventions it uses.
What configuration options it has?
So that's an interesting thing as well. I think… we have a section about installing, and maybe a couple of them have a few details about configuration, but not really. But anyway.
I'm just thinking about this, because this is being leveraged in the Explorer… Which, if you haven't seen, is kind of cool.
So it allows one to dive in and C… Oh man, there's a lot on here that I haven't seen yet. Like, okay, what's the… what's the config builder?
Look at all this! Anyway, I'm gonna ignore that. I'm talking about instrumentation, and if you wanted to dive into that Cassandra one that we just saw… Guess it's this one.
We were looking at 4-4, And then you can see specifically, so here's the, kind of the summary, here's the telemetry that it produces.
And we could contrast that, right, with this stuff.
So that's kind of cool.
And I was thinking about it mostly in the context of our READMEs, and wondering if we could generate some of this based on… A metadata file that doesn't yet exist.
**Cesar** 14:22 Sounds very cool. Do you know if that metadata… is… At least in the instrumentation, Repo is somehow connected to the code.
Or, like, we still have to keep them both.
**Jason Plumb** 14:34 I think it's mainly…
**Cesar** 14:35 My name is…
**Jason Plumb** 14:35 Yeah, I think it's not. I mean, I guess the YAML is the code, but no, I don't think there's any tight coupling there.
**Hanson Ho** 14:44 What format, is this, like, is this, like, just a one-off format Jay has created, or is it, is it based on some, like, Weaver 2.1 or whatever?
**Jason Plumb** 14:58 I asked an agent that same question yesterday, and there isn't a real schema for it.
So… We could look at… one could look at proposing that, or trying to unify that. The other thing is that, Oh, where… where is it? It's in… there's another repo, or maybe it's the repo for the Explorer.
Let's see… No.
**Hanson Ho** 15:28 I mean… we could… There are things that we could do to generate portions of this, just by, like, grepping the code and looking for, semantic conventions that are used, and then, you know.
Yeah.
**Jason Plumb** 15:45 Yeah, this would… I mean, this would be a place to look for that, but I don't think there is an actual schema, but the thing I did find… does not… is not compatible with events, right? So, they're definitely focused on tracing and metrics.
So, events is, like, our focus, so…
**Hanson Ho** 16:07 it feels like something that Weaver might want to have, basically, another abstraction that is, like, a thing that uses semantic conventions.
I mean, all the kind of bits are there, right? It's… we need a new bit that says, this bit references this semantic convention, and this semantic convention that comes from this place in this version. And with that data, it's enough to basically crawl through and find all the actual, details about which sponsor conventions, and then what those details generate, README. It says, this instrumentation is called blah, and it uses these, you know, attributes, and… Bob's your uncle, right?
**Jason Plumb** 16:54 Yeah, and then I naturally start thinking about, like, well, I wonder if we could just, like, we could define kind of a template, and then a model could do it based on the code or something? I don't know.
This one.
**Hanson Ho** 17:04 Yeah.
**Jason Plumb** 17:04 Yeah.
**Hanson Ho** 17:05 like, I mean, the easiest way is just have, like, a file that lists all the semantic conventions that are used, and then have that just be parsed. It's… yeah, we have to maintain it, but it's… it's… it's easier to maintain than this, especially getting all the details, like the names, and the description, and the type, and the, you know, if it's an enum, all the possible values. That can just be… yeah, we just need that one definition.
**Cesar** 17:34 Yeah, given that we have the code that use… that generates this telemetry, I think… It probably will be possible to… generate something Without the help of an agent.
I think agents are great for… like, non-deterministic stuff, but I think this one is… I mean.
**Jason Plumb** 17:59 Yeah.
**Cesar** 18:00 Shiva, maybe!
The code to make it happen, of course, it's gonna be written by an agent, but… I think, I think it's something that we can… Kind of retrofit from the code, and it should… Should be better.
My opinion.
**Hanson Ho** 18:18 We can start with an issue, and just say, hey, you know, when someone has time, you know, you can take a look at this.
**Jason Plumb** 18:26 Yeah, that would be cool.
**Cesar** 18:26 Yeah.
**Hanson Ho** 18:28 Is there a semantic conventions milestone or something like that we can, like, lump all this stuff into?
**Jason Plumb** 18:34 I don't think so.
**Hanson Ho** 18:40 I guess… I guess we don't use milestones, alright?
**Jason Plumb** 18:43 Not really labels more than…
**Hanson Ho** 18:46 Labels.
**Jason Plumb** 18:47 wild.
**Hanson Ho** 18:47 Okay.
**Jason Plumb** 18:47 this project, but…
**Hanson Ho** 18:49 Cool.
**Jason Plumb** 18:50 There's a SemConv one.
**Hanson Ho** 18:53 Nice. Okay, that works. We create an issue, tag it with that.
And then, who's got time? They can take a look at it.
Oh, I'd love to take a look at it.
**Cesar** 19:11 Wanna take a look at it, Hans?
**Hanson Ho** 19:14 I WANT to take a look at it.
**Cesar** 19:16 Okay.
**Hanson Ho** 19:16 I will not commit to taking a look at it, because I… yeah, I need to get the other semantic convention stuff done first, when I have time.
**Cesar** 19:23 No worries.
**Hanson Ho** 19:25 I would love to, though. Or I would love someone else to do it as well. I just… I want this done, but…
**Cesar** 19:31 It sounds fun. Sounds like a fun chatting.
**Hanson Ho** 19:33 I can't beg of others… Of which I can't do myself, so… It's just out there.
Bite my tongue.
**Jason Plumb** 19:44 Okay, well, I think we've fallen off the end of the agenda, so maybe we'll end it a little early today.
Last chance for anyone to bring up any topics.
Alright.
That did it?
Appreciate you.
**Cesar** 20:04 Thank you.
**Jason Plumb** 20:04 See you next time. Bye!
**Cesar** 20:06 Right?
