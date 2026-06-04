SIG: eBPF instrumentation
Date: 2026-06-03
Duration: 70 minutes
============================================================

## Zoom Recording Transcript

**Tyler** 01:04 Hey.
**Florian Lehner** 01:08 Alright, we'll come back.
**Mike Dame** 01:10 Hello?
**Tyler** 01:10 Yeah.
How y'all doing?
**Mike Dame** 01:15 Good.
**Tyler** 01:39 So it looks like some of the CoreLogix guys aren't going to be able to make it today.
But I'm seeing folks still filter in here.
If you haven't yet, please go ahead and add your name to the attendees list, and if you, have agenda items you want to talk about, go ahead and add them there as well. We can probably get started here in just a little bit.
Still just filtering in.
Awesome. Yeah, let me double check some… Dang, looks like we're all set to go.
I'll start sharing my screen, we can jump in here in just a second.
Okay, welcome everyone. To start us off, Roy, you wanted to talk about, Grafana Bela Survey Mode.
**Roy Reshef** 02:54 Correct. First of all, hi, it's the first time I participate in this meeting.
I've met some of you at KubeCon Salt Lake City, and I know Nicola from Toronto from before.
So yeah, survey mode, I ran into it after chatting with Nikola, last week, or the week before.
for various observability purposes that we see, I mean, we are in the business of resource optimization, so we feed off observability, specifically metrics.
Floating the application runtime of a container is extremely valuable for many purposes.
We get requests from… You know, like, show us, CPU or memory consumption of Java applications, in some cases, when you need, based on you know, resource consumption and allocation that we see. You want to do in-place resizing Kubernetes, You need, in some cases, to treat it differently depending on application runtime.
Now, this feature, I understand, or the feature of survey mode, when OBI was donated to OTEL was in infancy, so it… it did not make it to OBI.
It is now in Grafana Bela, and in my opinion, and I shared it with Nikola when I discussed it with him.
It should actually be part of OBI.
I'm just floating… talking about floating even a simple metric, like Bela does now in survey mode. I mean, you may not even want to instrument that container.
But just to know that it is running Java, or Go, or .NET, or Rust, or whichever other It's very valuable.
Yep.
That was my safe.
**Nikola Grcevski @ Grafana / OpenTelemetry** 05:02 Yeah, let me add some color on what this is and what we use it for, if that's okay.
But, so… Survey mode is essentially, half of the pipeline that we currently have today for instrumentation. You define your instrumentation criteria in a separate section.
And… it… You give it whatever you want it to find on a… On a cluster or on a system, you have your definition say, all namespaces. Discover everything.
So it does everything as normally it would, and it just stops short of instrumenting the application. So… what we use it for is, in Grafana, it's a ClickOps way to instrument applications. So, if you will.
It can feed a UI.
That people can then pick and choose what they want to instrumented.
And then you can imagine, once you pick and choose what you want to instrumented, you can push an OPAM configuration change, remotely to your, collectors. With that being… having OB in the future, you can just deploy a new instrumentation strategy, or You decided something was wrong, it wasn't instrumented well, you can uncheck that service or namespace, but… So this is sort of like a precursor to instrumentation, if you want to package it in a UI solution, more or less. It has no impact on… On any actual, instrumentation side.
So, I mean, from Grafana's perspective.
no issue donating this in any way, or adding it to OB, we… Yeah The question is how much of it is actually part of this project, or it should be… care, you know.
Or should it be a separate component, or do something else? I don't know.
Chlorine?
**Florian Lehner** 07:17 I'm not aware of the SO emote, but from what I'm listening, I think it can be already done with a different approach.
So if you take, sorry for the… For talking about profiling again, but if you take the profiling signal and, generate metrics based on the, reported, frames, then you will have this information already in Autel.
So, what we are doing at Elastic is, taking OTA profiles.
running, profiles to metrics, processor against it, that extracts the information about, hey, how many Python frames do we see, how many, Java frames do we see, and then we have this classification already. So we are, we are doing very similar, probably in maybe a different way than… Grafana Baylor is doing, but, yeah.
I think there are options.
**Nikola Grcevski @ Grafana / OpenTelemetry** 08:14 The only thing is, like, so it's essentially almost like… yeah, I think you're right, Florian, that approach will work too. I didn't think of that.
They, It almost could be done with a simple kind of component that kind of finds everything, like, almost a collector component, but you do need some extra permissions to dig into, the executables to find out what the programming language is, or if Roy, I think he mentioned to me he wants to extend it to find out even the version of the runtime. Let's say, you know, it's Python 3.9, or Python something else, right? Which… will be really cool, or I think he also wants to go deeper and find what JVM GC mode is enabled, and things like that.
Well, we don't have that, obviously. This is just, the only advantage, I would say, is that is that this works without eBPF at all, so it will work on clusters where there's no eBPF support, like if, say, Fargate.
You can still make this work, because at the end of the day, it doesn't use any eVPF to… to actually do anything. It's just that… short circuit of the pipeline that does the discovery, decoration with Kubernetes, metadata, and language.
and so on.
We, right now, do not… show the information about what's the process ID or the command line.
I know Roy wanted to add that as well. We… I mean, for our purpose, that's not useful, because we just want to know what services are running, so we could, show them in the UI, but it could be an optional attribute that we can add, and should be… can be added to this survey, if we decide to… Add this to the project.
Yeah.
**Tyler** 10:14 Yeah, so I think that, a few things. One is it sounds also really similar to what the injector SIG was looking for as well. Like, right now they're doing their own process discovery, and there was talk of integrating with, like, our process discovery, given we have, like, a much more… featureful, Set here, and so I think it, like.
I think that's great. I think there's, like, there's a project here.
I would say, though, that, like, it needs to get… put through a project pipeline. So an issue needs to be created for this feature request. Roy, I would suggest you create this feature. I would… Appreciated if you could include… in their… not only, I think, like, the solution space that you're looking for, but also, like, what you're trying to accomplish, because it's really interesting.
Like what Nicholas is saying, like, the dimensions that you're looking for, the breadth that you're looking for, what you're trying to use this for.
I think also, annotating it with what it already is used for, what Nicholas is talking about. I think if we can get a full set of, like, use cases here, I think we could do a better job at producing something, and then prioritizing when we would be working on this, I think is another thing as well.
**Roy Reshef** 11:30 Yeah, sure, I can work on that. I'll… I will need to contact some people, like Nicola or whatever, to… because my… I have a… a very, you know, limited knowledge of OBI and of Baylor. I played with it a few times, but, I mean…
**Tyler** 11:48 that's not… that's not too wor… too problematic. Like, the solution space, like, obviously, like, something's already working for Baylor, right? So that's not a big deal. It's more, I think, about, like, what you as a user would like to see. That I find to be way more valuable than a feature request.
**Roy Reshef** 12:01 Yeah, I can… I mean, Nikola mentioned some of it.
what's the… what I'm looking is… like, I mean, as elaborate as possible of runtime information.
Okay, what is running in the container? There's also an issue, by the way, that I have detected.
With the Bela survey mode, we also have to think about what if the container spins up more than one process? What do we do then?
Which is… I know it's been frowned upon, but it's been done. I've seen containers doing it. Do we take one? Do we take… whatever, but that's… and then to try to get, okay, which runtime we have, what version it is, and for specific runtimes, especially JVMs, I mean… from decades of experience with Java, I mean, the number of garbage collection mechanisms that they have, and the power meters that… You can provide them is… is incredible.
And… I mean, in Go, it's rather simple, because it's a Go version, it's maybe 2 or 3 parameters. In Java, it's like… I don't know if dozens of them, but there's a handful.
And… And they may impact what you want to do with that workload.
So, obviously, it's a work in progress, I mean, or not work in progress, I mean, you can do it in a phased approach.
**Tyler** 13:32 Yeah, yeah, so this all sounds good.
**Roy Reshef** 13:34 Make a feature request and figure out, And get some help, and… and start it up.
**Nikola Grcevski @ Grafana / OpenTelemetry** 13:43 I can hook up with that, no problem.
**Roy Reshef** 13:45 Thank you.
**Nikola Grcevski @ Grafana / OpenTelemetry** 13:46 And we'd like to get rid of this Oveila and move it into OB, that would be great. So one less dependency for us to worry about, yeah.
Yeah. We're a lot better.
**Tyler** 13:56 I don't think there's any opposition moving it in. The only opposition would be if the payload folks didn't want to move it, but that doesn't sound.
**Nikola Grcevski @ Grafana / OpenTelemetry** 14:01 No, no, no, it's quite the opposite, like, I… this needed to be billed during the whole process of donation, and we were like, okay, well, I don't even want to start on this, because it's just gonna… maybe delay or move things around, or now there's another thing in here, so, we just played it safe and kind of said, okay, let's just build this for this purpose. But Tyler, you're absolutely right, actually, we do use the same approach for almost like an operator way for SDK instrumentation. So, like, the bail provides a survey mode, and even if non-EVPF-enabled platforms, as long as it's Linux, obviously, it can give the information back to users, but then they can actually use it to instrument with the hotel injector, rather than… Rather than eBPF.
**Tyler** 14:51 Yeah, so this definitely ties in, I think, with the broader hotel.
**Nikola Grcevski @ Grafana / OpenTelemetry** 14:55 Yeah.
**Tyler** 14:56 Yeah, featuring.
**Nikola Grcevski @ Grafana / OpenTelemetry** 14:57 Cool.
**Tyler** 14:59 Cool, alright, alright, got a good plan forward on that one. We can jump ahead. So, next on the list, Mike, you wanted to talk about dynamic selector expansion Proposal?
**Mike Dame** 15:11 Yeah, this is something that I've been working on for a couple weeks, kind of trying to take that idea of the dynamic selector that we added.
you know, I guess a couple months ago, that lets you encode, select apps to be instrumented with, and you can see kind of the code sample here. I want to extend that to be able to support other signals, too, that we have in OVAD. The metrics, network metrics, stat metrics. The dynamic selector itself has been working really good for us. We've been using that, again, kind of similar to what Nichol was saying in, like, an operator, pattern.
So, we're able to dynamically run that and not have to reconfigure, redeploy OB to enable new apps in it. This kind of takes the same approach and extends that to metrics. And so, going through this, I've been working on it and kind of prototyping it a bit, and seeing, learning a lot of the differences between the App OLLI pipelines and the metrics pipelines that we have.
And I thought it would be a little easier to kind of do this in, phases.
So that we can review the changes, you know, independently, kind of keep them isolated, and so I broke it into different phases that, you know, it starts out with just kind of, like, internal refactors, then goes into slowly adding more of this functionality until, at the end, everything is gated, and Yeah, and kind of thought about some of the options for… I think, like, the bigger takeaway from this is that I really, even from adding that dynamic selector at the start, kind of saw that as, the, like, a lot of options that you can do through code and, like, kind of mirror a lot of the OB static config that we have, but also, just from a dynamic approach, there's a lot of, you know, different things. So I gave some examples of You know, we could start adding, you know, per-signal configuration, or resource attributes, or, you know, anywhere that, you know, now we get these, these subviews, they can hold an independent config and get really flexible.
Yeah, this is… really, yeah, extending that traces approach to other… It doesn't impact any of the static… it shouldn't… it's not designed to impact any of the other config approaches. It's kind of similar to how Dynamic Selector right now in AppVolly drops in as its own swarm node.
Should really just run independently, only matter to people that are using it, and not impact any of the existing API, or the config, or that functionality.
So yeah, I wanted to put it up, get some feedback, more kind of make sure that my understanding of these pipelines is correct in the way that I'm trying to wire it in, and that I'm not thinking of doing anything that, you know, doesn't match, like, semantically how things are set up, but if anyone has any feedback on it… It… it is a long proposal, but I think, you know, if you guys understand Obi a lot more than me already, you'll probably be able to skim through the sections and kind of get it, Yeah, anything that you have to say, I'm gonna be working on the PRs, or we might have some other people from Oticos work on them too, try to bring some more contributors in.
But, yeah, then I'll be looking for review on that, so… Yeah, thanks. Feel free to leave any comments or feedback, but I think it shouldn't be too much of a problem. If anyone has any objections to it, you know, let me know, or anything that I'm doing wrong in here, but… I didn't think that it was too, you know, controversial, but again, that's why I wanted to bring it up.
**Nikola Grcevski @ Grafana / OpenTelemetry** 18:52 No, this is great. I mean, I didn't read it in that much detail, just skimmed over it. It sounds like a good idea to me. If you want, I can actually… Oh, we're even more careful there.
See if there's anything that stands out that might be, but I think it looks good.
**Mike Dame** 19:09 Yeah, yeah, I wanted to do my homework on it first and really say, like, okay, this is actually how it would be implemented, and make sure, instead of just, you know, the idea was there of these, like, traces, subviews, and metrics, subviews, but how does that actually get wired in and make sure that.
**Nikola Grcevski @ Grafana / OpenTelemetry** 19:23 Hmm.
**Mike Dame** 19:24 the layout.
**Nikola Grcevski @ Grafana / OpenTelemetry** 19:25 to be able to fully configure OB remotely without restarting it, essentially.
**Mike Dame** 19:31 Yeah, exactly.
**Nikola Grcevski @ Grafana / OpenTelemetry** 19:33 That's cool.
**Tyler** 19:36 Yeah, great, great. So yeah, if folks, want to take a look, please do. Yeah, this looks great. Moving, moving forward, Mike, awesome, awesome work.
**Mike Dame** 19:46 Thank you. Thanks.
**Tyler** 19:49 Okay, next up, Antonio, you have a question for Nicola about this proposal?
**Antonio Jimenez** 19:58 So, that was a proposal that we did at that time, so I was lucky to be on the Observability Summit with Stefan, and we were chatting a little bit about that, so it could be great that we kind of start on that, as I was mentioning, like, once you start and provide me some guidance, I can… I can try to follow up on… on the direction. So I created a… That was kind of an epic ticket, the one that Taylor is showing, but I created a follow-up issue to start with, so I think, Nicola, when you find out time, would be great, and then we can try to work together.
**Nikola Grcevski @ Grafana / OpenTelemetry** 20:31 Yeah, I was gonna say, personally, from my work side, I… the… this week and next week, I'm, like, swamped, but after that, I promise I will get to it.
**Antonio Jimenez** 20:43 Yeah, so I would say.
**Nikola Grcevski @ Grafana / OpenTelemetry** 20:43 Sure. I've just been busy about, you know… .
**Tyler** 20:49 What's the… what's the blocker, Antonio?
**Antonio Jimenez** 20:52 I mean, it's… it's… the main thing is, like, Nicola knows how that works, and I don't, honestly. I don't know much about the code, so it could be great that he maybe can start building some spam logic for TCP, and I can follow up on other use cases for TCP, or once we solve that, if we see value, we also do it for UDP. That's kind of the plan that I have in my head.
I'm there.
**Tyler** 21:17 Well, it sounds like Nicola's pretty overloaded. Are there other folks that are interested in this, or is this just something that needs to wait?
**RC Robert Cowart** 21:28 Let me check my… yeah, my mic's on.
I'm just scanning through here what, So, I don't know if Sinh has brought it up on a previous, call.
But, y'all may be aware of the Merman project that we have that, is more focused on the network side, and we've had internal conversations around actually taking pretty much all of that stuff that Merman does today, and just bringing it into OBI, because it seems to be the place where it would make more sense, which kind of fits… would actually do what this… just reading this title is. I don't know if Sven has brought that up on any previous calls or what have you, but, That is our intention, is to take everything that's current… it's written in Rust at the moment, so, right, we'd have to port it over to Go, but we actually were more of a Go shop before we were… before our team started doing Rust, so it's not that big a deal to do.
So, yeah, I don't know where there'd be… there would surely be some overlap, because there's plenty, like, I see UDP and ICMP could be other… like, we kind of do all that already, and would be moving that over. So, I mean, I'm sure we're happy to collaborate. I'm not trying to say we do it and no one else does. I just… Like, we literally have been having these conversations internally, like.
why is Merman separate? It seems to make total sense to make it part of OBI, so…
**Tyler** 23:04 Yeah, I think Sven has been here, and we've talked about it. We've definitely also talked about it at, like, the Semitic convention level as well, because there's just a massive amount of stuff that you all had, was kind of the big thing.
But yeah, I mean, I think if… if you could find somebody like Sven or somebody else that could have, have the time and maybe start… start chipping away with some PRs, I think, Antonio's looking for help on this one, so… Yeah, if you have bodies, yeah, that'd be helpful.
**RC Robert Cowart** 23:32 Yeah, I think… I think we… well, I better not speak for them, but, you know, I'll let the engineering team decide themselves about their schedule, but nonetheless, I… like I said, I think we are prepared to… Allocate some resource here, so…
**Tyler** 23:47 Cool.
Yeah, I mean.
**Nikola Grcevski @ Grafana / OpenTelemetry** 23:49 Sorry, sorry, Tyler. The first step that I think, for this one is actually, for TCP, is not that hard to do. I just haven't had the time, because all TCP events that we currently process, eventually make it to the user space side. So, every TCP event coming through we sort of accumulate a little bit on the eBPF side, and then ship it over when it's done to the… to the server side, to the, sorry, user space side. And then it… If it's a recognized protocol, we generate Data for it, and if it's unrecognized protocol, we just drop it.
so, I think… what Antonia needs here is that instead of accumulating the TCP events should… Each one should make it to the user space side.
Apart from being accumulated, we're just… Number of bytes being sent or received.
And then… we already tag in the TCP protocol there, what is the current trace ID? We find it from if there's a wrapper HTTP trace around it, and stuff like that. And then, It just needs to be through an option exposed, and make it into traces.
As an internal span.
So, most of the stuff is there, that's what I said, But it needs to be properly done in the sense that we probably don't want this on by default, so it needs to be an option that somebody enables, that enables the eBPF side and the adding.
Otherwise, it's just gonna get too noisy for people.
To do it. And then, once we get that going, I think, like you said, like, UDP or ICMP and all the other stuff.
Yeah, so I don't think it's a huge amount of work.
Yeah, I haven't had the time, so I can help anybody who wants to do this to guide them on the right path, too.
To get this done.
**RC Robert Cowart** 26:05 Yeah, the other thing I would add, though, is even once you kind of move things over into user space, like, if you're parsing any parts of later payloads and all that… so, like, our thing anyway is network traffic flows, and so one of the things, like.
Take, for example, Sflow. One of the ways it communicates flow is it actually says, like.
here's the first 120 bytes of the header that I sampled. So we… we already have, in Go, which, if I could say so myself, better than GoPacket, our own packet parsers that understand tons of protocols and things like that, that just could be… You know, we just have to expose some of that a little bit more publicly.
But there's a lot there already. I figure… I think if we probably came together, we could figure something out.
**That has some quick wins, so… Nikola Grcevski @ Grafana / OpenTelemetry** 26:56 Yeah, absolutely, so… Yeah, I… like I said, I'm busy for this week and next week, but if anybody else wants to, just Slack me on CNCF Slack, and I'm happy to spend an hour explaining what needs to be done, and helping guide whomever if you want it sooner.
Pretty much it.
**Antonio Jimenez** 27:18 Awesome. In case someone follow up with Nicola, feel free to invite me to that meeting. That would be great in my slide. And then something else that, Robert, I want to mention, this is exactly what we want, so the network flows to be part of the application phase. This is where I see, really, the huge benefit for a customer's perspective, because you guys have the network flow.
OBI, I mean, any instrumentation have the application, but connecting each other is where the main magic happens. Okay, yeah, I don't want to take more time for that topic, but yeah, I wanted to mention that.
**RC Robert Cowart** 27:48 If shared on top of you, I would have shared a screenshot of exactly what you're talking about.
**Antonio Jimenez** 27:58 to…
**Tyler** 27:59 Okay, well, we'll keep tuning on this one, obviously… Life is busy, so that's the way it goes, but yeah, please… Nikola Grcevski @ Grafana / OpenTelemetry 28:06 Thanks for reminding me, Antonio, like, I appreciate this, don't think you're nagging me or anything, I'll forget if you don't do this, so… yeah, I'll get it done, yeah.
**Antonio Jimenez** 28:16 Awesome, lovely.
**Tyler** 28:19 Okay… I don't know who put this… Next, oh, that, that…
**RC Robert Cowart** 28:29 Which one are you on? That might be me.
**Nikola Grcevski @ Grafana / OpenTelemetry** 28:32 Yeah, that's yours, yeah. Okay.
**RC Robert Cowart** 28:34 It looks like he's… Giuseppe's not here. I had a really long response there, part of which just goes into, like, some issues with some of the places on the kernel parameters he wanted to get some stuff. And then, also, the main argument that I kind of had here was, like.
Like, you look at an end-to-end network transaction, and it's like… Depending anywhere on that path where you measure, you have a slightly different perspective.
And… and it would be… we've done… done this before, we made this mistake in some other sources, where it's like.
you know, TCP round trip, one way, this, that, like, and you end up with, like.
157 different attributes. And it's like, no, I think we need… the main point I was trying to make is… well, there was one of probably look at this place in the kernel to get the round-trip value, but the other one was more around it probably makes more sense to have, like, two metrics, latency and jitter, and then a field that's kind of like, where did I observe this from? What was the target I was observing? Like, was it just the network layer? Was it the application layer? And that type of thing. So, I didn't know if he was gonna be on the call, I was just going to kind of review those things, but it looked like in the comments he said we could also talk about it one-on-one, so.
**Tyler** 29:52 Yeah, I… Yeah, I'd really love it if we could get that conversation in this meeting next week. It sounds like he'll be back next week, Giuseppe.
**RC Robert Cowart** 30:02 Bye.
**Tyler** 30:03 Because, yeah, this is… this looks great.
from what you put here, just skimming over it, at least, like, you have a lot of thought already in this, and I would rather it be disseminated across the whole SIG, And then, yeah, I'd love to have that conversation, here, if we could do that next week.
Yeah, this is great.
**Nikola Grcevski @ Grafana / OpenTelemetry** 30:24 Yeah, if you can make it next week, Rob, that would be awesome.
**RC Robert Cowart** 30:28 Yeah, I'm, I can double-check, but I'm pretty sure I can, so… Nikola Grcevski @ Grafana / OpenTelemetry 30:32 Okay.
**Tyler** 30:33 Yeah, I mean, if not, obviously, like, having any conversation with Joseph is great as well, but, yeah, I'd love to hear it.
Let's… okay, let's postpone that, for… for next week, and then… Cool. Next up, Steven, RFC for selection by language runtime version.
**Stephen Lang** 30:58 Yeah, so I did the complete opposite of Mike, and did no due diligence whatsoever. All I have is an idea. But I'd love, if people have ideas on, first of all, whether or not this feature would be useful, and secondly, any pointers on how we might be able to extract this information from the target processes. So the idea is.
Imagine you have a large Kubernetes cluster with hundreds of services. Some of those services that are already instrumented, may or may not be with OTEL.
And likely, those manually instrumented services are going to be using, or some library which depends on a more modern runtime version.
So, in this case, I saw a cluster with just a single namespace, with hundreds of services.
And all of the .NET 3.1 and below services couldn't be instrumented by the library that was in use, because the library required a newer version of .NET.
And in our configuration currently, there isn't really a way to say only instrument those services which match the language.net, but also only if their runtime version is, for example, less than or equal to 3.1.
So the alternative in the current configuration Is to… you can select by language, but then you have to list by name every single service that you want to match.
Or exclude those, that you want to be excluded, or some combination of.
So I thought it would be ideal if, in this case, we'd be able to select by runtime version. And I know that the logic is going to have to be different depending on the runtime.
And I know that for some languages, it's going to be more difficult than it is For others, but I thought I'd just put this out there first, before I did, like, a ton of work looking at, you know, implementing this.
Just to see what, generally people thought, if there's any comments, I think this would be useful.
I think Mark has already said, that, like, an extension to this is not only… there's a comment at the bottom, Tyler. Not only would it be maybe a good idea to select the runtime version for selection.
but also maybe the framework as well, so, you know… Ruby on Rails, certain framework, or… I don't know, maybe for… Java, maybe we'd have, like, a different behavior if, you know, some kind of reactive framework was used, or… I don't know, that could always be an extension, or, you know, could be considered in addition to how this new configuration option would be present.
And finally, I'll just say that I think we have currently 3 different forms of configuration for service discovery. Like, we have the legacy Discovery… what is it?
not Instrument, I think Instrument's the newest one.
I think we had an older discovery.services.
Possibly.
Which I've just kind of left out of there. And then, obviously, we have the new declarative conflict.
So I thought we'd only implement it for the newer ones, and not for the oldest version of the discovery section.
**Nikola Grcevski @ Grafana / OpenTelemetry** 34:11 Yeah, that makes sense.
**Tyler** 34:12 That makes sense, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 34:13 I like it. I like this proposal. I mean, it'll push us to actually even find the runtime version, which is not only information we currently provide, which is to provide the language.
So that would be great, but as you say, like, it's a separate implementation for every programming language that has a runtime.
The second approach… to find even further packages or some internals in it, that's even harder. I guess it's even less… program… I mean, maybe it's specific to certain programming languages, possible.
But… may not be possible for all. For example, if Yeah, Java.
You can find what packages may be used by application, but you cannot tell what version of that package they have.
**Roy Reshef** 35:02 That's not exactly true, Nicola. If you find the jars on the class pass, they… Typically, even the name includes a version. Yeah. Although… Nikola Grcevski @ Grafana / OpenTelemetry 35:13 If it's… but if it's a shaded jar, then…
**Roy Reshef** 35:16 Yeah, and sometimes you find two jars of the same, work with different versions, so which one is used is a bit of a Russian roulette in that case.
But.
**Nikola Grcevski @ Grafana / OpenTelemetry** 35:30 But the first one is just finding what version of Ruby you have as a… or a Node.js runtime, I think that's extremely useful, and being able to, like you said, like, say, all the old .NET applications use OB, and for all the new ones, use SDK instrumentation.
**Roy Reshef** 35:51 That ties a bit to my proposal, because that's… detection of the runtime version is part of, well… Should be part of it.
**Florian Lehner** 36:02 I've put a link to how we detect the patch version of the runtimes into the comment, maybe this helps as inspiration. We do this for all the languages we support.
And we also required, knowledge of the runtime version.
As, the internals of the runtimes often differentiate, or the internals are different for stack unwinding, that's why we also have the information now.
The runtime version, is extracted.
Maybe this helps implementing this.
**Nikola Grcevski @ Grafana / OpenTelemetry** 36:36 Oh, 100%. Can we not just use this package, then?
**Tyler** 36:40 Yeah.
**Florian Lehner** 36:41 You get stuck on one link for free.
**Rafael Roquetto** 36:46 And then for… for languages or… or tech technologies that don't have the actual concept of runtime, we're just not support.
**Nikola Grcevski @ Grafana / OpenTelemetry** 36:56 Not reported, yeah.
**Rafael Roquetto** 36:57 Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 36:59 Yeah, my only comment on Slack that I put in was, if you had put the version in there.
and you… But we couldn't find it for whatever reason.
What do you do then? Do you just… Report an error, do not instrument, or just say, will instrument, but we… whatever. Yeah, so we need to decide on the semantic.
**Tyler** 37:24 Oh, you log an error message, right? Saying something like.
**We failed to do this, and just… Nikola Grcevski @ Grafana / OpenTelemetry** 37:30 But the question is, do you instrument with OB or not? Because you said, you know, I want .NET, but we couldn't find the version, so… Should we instrument a .NE application, or just ignore it?
**Stephen Lang** 37:42 It's like you want to define the fallback behavior. Should you fall back to default instrument, or fall back to, you know, default back off and do nothing?
**Nikola Grcevski @ Grafana / OpenTelemetry** 37:51 Right, we can make, I guess make it an option to what to do in that case, and then… But you choose a default that's safe, like, do not actually instrument. If somebody wanted version and we couldn't find it, well, tell them you couldn't, or something.
**Stephen Lang** 38:06 Yeah, or what happens if you could find the runtime?
But you couldn't find the version.
**Nikola Grcevski @ Grafana / OpenTelemetry** 38:14 Yeah, 10 years.
**Stephen Lang** 38:17 So yeah, maybe it needs, like, a fallback configuration option as part of the config.
To decide what you want to do in that case.
Thanks for the discussion. Appreciate it.
**Tyler** 38:33 Okay, alright, moving on… sorry, I'm trying to share my screen again here.
So, I did want to go over the roadmap, It's nice on the agenda. We are halfway through the year, believe it or not.
But I do also think that there's only 20 minutes, so we probably aren't gonna get too far in that. I'm gonna just bump this down to the bottom here.
And maybe next, I think it's blue. Next to me, we can talk about that. Mike, next up, you wanted to just give a reminder on the Go Sunset, or the Go Auto instrumentation sunset?
**Mike Dame** 39:23 Yep, that meeting is tomorrow. It's on the hotel calendar. It's, time do we have… actually the same time as this meeting today, but tomorrow, so you can do the, time zone.
yourself there. We'll go through.
That. So, last reminder, come, check it out.
Yeah, we'll post updates, too, if anyone's interested.
**Tyler** 39:46 Yeah, absolutely.
I will be there. I will see you then.
**Nikola Grcevski @ Grafana / OpenTelemetry** 39:51 Gotcha.
**Tyler** 39:53 Okay, next up, Antonio, you want to talk about Semantic Convention Sig's network group?
**Antonio Jimenez** 39:59 Alright, so JCK was there because I am proposing some… network attribute, quite generic ones, like IP prefix, or autonomous system name, or reverse DNS, so quite simple ones, but they don't exist today. And they were quite interesting, but they said that they are not the… experts from the domain, it would be great to discuss those ones with a group of network people. Seems like there was before a SICK meeting, sorry, a semantic commercial network group, but it's kind of dead, so they are gonna try to invite people that are interested, and I thought about Mario.
**Mario Macias** 40:35 Yes, please.
**Antonio Jimenez** 40:36 CoreLogix, it was also interesting, so yeah, I will… once they create that group, I will talk to you.
**Nikola Grcevski @ Grafana / OpenTelemetry** 40:42 Yes, it's.
**Mario Macias** 40:43 Is there a… is there any Slack channel, ongoing?
**Antonio Jimenez** 40:46 Not yet, it's, I think.
from Google, he took the action item to set up that virtual group for the moment, and if we need, like, set up a monthly meeting or a bi-weekly meeting or something, we'll do it on there. That's it, yeah.
**Mario Macias** 40:59 Okay.
Okay, cool, thank you.
**RC Robert Cowart** 41:01 I just wanna say… Sorry for the religious undertones, but hallelujah!
Brought this up ourselves about 2-3 months ago, and then they kind of, oh, maybe there's community things and some other stuff, but, Yeah, just go ahead and sign Elastiflow up to participate. I… we probably have… and we're thinking net… not just, like, endpoint server networking, but networking as a whole. I think we're probably gonna have, like, 3,000 or 4,000 semantic conventions to add in the next 6 months.
**Antonio Jimenez** 41:39 So… Okay, that's huge.
**Mario Macias** 41:42 Oh my god.
**RC Robert Cowart** 41:43 knows. But, you know, yeah.
okay, we're…
**Antonio Jimenez** 41:49 Mine also.
**RC Robert Cowart** 41:50 Definitely all in. We were gonna… we were actually, again, putting together, Yet another argument why we should be allowed to revive that, and so we're happy to take a role in that as well, so…
**Tyler** 42:02 Robert, are you… do you want to be the point person on that for Antonio, when he mentions names?
**RC Robert Cowart** 42:07 What's that?
**Tyler** 42:08 Do you want to be the point person for when Antonio mentions that?
**RC Robert Cowart** 42:10 Absolutely, yeah, yeah. Internally, we had already said I'd probably be the point person on it from our side, so…
**Tyler** 42:16 Okay, cool.
**RC Robert Cowart** 42:17 This'll be, like, the fifth time I've done a network schema in my career, so yeah, I'm more than happy to… Had some input, so…
**Tyler** 42:27 Yeah, absolutely.
**Nikola Grcevski @ Grafana / OpenTelemetry** 42:29 Yeah, probably Pina would like to participate as well, I'm guessing, but…
**Antonio Jimenez** 42:33 Okay, have the same feeling.
**Nikola Grcevski @ Grafana / OpenTelemetry** 42:35 Yeah.
**Tyler** 42:36 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 42:38 Oh, Giuseppe, yeah.
**Tyler** 42:45 That looks weird. Like, I don't know his affiliation.
**Nikola Grcevski @ Grafana / OpenTelemetry** 42:50 CoreLogix.
**Tyler** 42:51 Yeah, I know, I know his affiliation, I just want to make sure that it's clear that he hasn't confirmed.
**Nikola Grcevski @ Grafana / OpenTelemetry** 42:55 Okay.
**Tyler** 42:57 Sorry.
**Nikola Grcevski @ Grafana / OpenTelemetry** 43:02 You volunteer at Mina, yeah.
**Tyler** 43:03 Yeah, yeah, exactly, yeah, yeah.
Okay, cool, yeah, well, Antonio, thanks for mentioning this, and yeah, thanks for, Bringing these people into the, into the, into the group.
Okay, Mario, next up, you want to talk about unresolved hostnames in address.
**Mario Macias** 43:23 Yes, yes, some, some, quickly. We, we decided last, in the last meeting to close this as, as not an issue, but, you actually provide a, A good point that was that this address is a… this attribute, server address and client… only server addresses are already being used by default.
But then I think that what we should do is to, I mean, this server address attributes shouldn't be… provided by… and shouldn't be enabled by default in some metrics, so we should replace it by server, which is the one that is providing the functionality we want, that is the host name.
or unresolve it if the IP address cannot be resolved.
**Tyler** 44:15 Hmm.
Yeah, I agree. I think that… I think… I agree with all of what you just said, yeah.
**Mario Macias** 44:23 Yeah, so I can create the follow-up action if you, if you want.
**Tyler** 44:27 Yeah, if you wanna… if you wanna take that as an action item, I can assign this.
**Mario Macias** 44:30 Okay.
**Tyler** 44:31 And we'll just use this issue to track that work, and then… Okay. Yeah, I think it… that was my intention as well. I wanted to.
**Mario Macias** 44:40 That's…
**Tyler** 44:40 with y'all, but, like, I think what you just described was what I would propose as well, so, yeah.
**Mario Macias** 44:46 Okay.
Good, thank you.
**Tyler** 44:52 Okay.
With that, we are right at the end, so I'm gonna leave the roadmap again. Let's move this to… We don't have it next week anymore.
Okay, don't worry about it then, I'll figure it out. Let's jump into some open PRs, and let's see what we have here.
So… starting at the bottom, we're actually doing pretty good. What are we at, 19? Yeah. And, looking through my 800-something notifications while I was gone, there's a lot of stuff that's been going on here, so… Yeah, great, great work.
Maybe starting at the bottom, Mario, you still have the selectively replace tracing programs if the system supports them. Work in progress, guess I'm gonna need to jump into there.
**Mario Macias** 45:37 Yeah, yeah.
**Tyler** 45:39 The support linking spans connected with GoChannels, this is on my plate, actually, now that I'm back, to get this into a working state, so nothing to jump into here, but hopefully next week, we can talk, or over the next week, we can discuss this. Again, I'm not looking to expand this to Selects yet, but just trying to get this into a working state and… Rebase it.
Rafael, you have a new socket tracer here, also a work in progress. Guessing we could probably just pass this one over as well.
**Rafael Roquetto** 46:06 Yeah, I'll probably pick that up again on, next, maybe July, when… or end of June, when, Grafana Hakaton happens. That's when I'll use the time for it.
**Tyler** 46:18 Nice, yeah. Great.
Okay, also, last draft is, Florian, you have this ad process context enrichment. I'm guessing this is still something you're working on?
**Florian Lehner** 46:28 Yes, at the moment, still blocked, because I'm waiting for a release of Hotel Proto, that you don't have the dependency on profiling.
I think that would be great.
**Tyler** 46:42 Okay, cool.
Okay, cool. Next up, Steven, user space, Go user space, HTTP, server request, body extraction…
**Stephen Lang** 46:52 This is…
**Tyler** 46:53 this one.
**Stephen Lang** 46:53 This is in progress. I've had some great feedback from Raphael, which I'm in the process of working through, so I've got a couple more bits to… To do on here.
**Tyler** 47:04 Okay.
Alright.
Next up, smeboob, I don't know… Okay. Add chunk tail call, transparent scanner for large HTTP, headers.
**Makes sense. Like… Nikola Grcevski @ Grafana / OpenTelemetry** 47:22 File has been…
**Rafael Roquetto** 47:23 Yeah, I… I have to look into that again. I mean, there's been a lot of it… a lot of it trading.
with this, a lot of… lot of AI that made it hard to know… to understand if the author, like, has fully understanding of what's going on, so I need to pick a… and kind of look into it again, but I'm not prioritizing it for this week.
**Tyler** 47:48 Yeah, fair enough.
**Rafael Roquetto** 47:49 Okay. Yeah.
**Tyler** 47:52 Where are we at? Okay… Test tracing, add TLS and go Uprobe. I don't think the author is on the call, this is a draft, so… I'm gonna skip over that one.
**Nikola Grcevski @ Grafana / OpenTelemetry** 48:06 Part of the same kind of, con… like, fix that, they want to pro… introduce, which is a good fix to have, but I think it's just, So that's the testing side of the previous one, so…
**Tyler** 48:22 They're 2PRs, huh?
**Nikola Grcevski @ Grafana / OpenTelemetry** 48:24 Yeah.
**Tyler** 48:26 How big are these viewers?
**Nikola Grcevski @ Grafana / OpenTelemetry** 48:27 Because the first one was too large, we asked him to split.
Yeah, usually.
**Tyler** 48:33 splitting out testing from a PR is not the right split.
Hmm.
**Rafael Roquetto** 48:39 I agree with you, Tyler, in that sense. I mean, he split it, but I think he… The other PR… I gotta look into it again, but last time I looked at the other PR, it was huge.
**they'll… Nikola Grcevski @ Grafana / OpenTelemetry** 48:53 It still contains the test. Yeah, I think it still contains the test.
**Rafael Roquetto** 48:56 Yeah.
**Tyler** 48:58 Okay.
Okay.
Yeah, alright. I… I would recommend, if there's not a lot of, effort being put into the development, I would… do what you did, Rafael, and limit your review development at this point, is what I would recommend. So, yeah.
Okay, cool. Next up, Florian, add event-based Docker container info caching?
**Florian Lehner** 49:24 Yeah.
**Tyler** 49:25 Bucked.
**Florian Lehner** 49:26 Should be… Oh, I forgot.
**Rafael Roquetto** 49:30 the Mr. Alias that blocked it.
**Tyler** 49:33 Yeah, wow, sorry.
**Florian Lehner** 49:36 It was blocked for a perfect reason. I think I addressed all the comments, updated everything, yeah.
If you have fun time.
**Tyler** 49:48 Okay, it looks like it's just waiting on me, then, to get another review.
**Florian Lehner** 49:52 Yep.
**Tyler** 49:52 I wouldn't…
**Florian Lehner** 49:53 test failing at the moment, it times out, but I think it's not related.
**Tyler** 49:59 Interesting. Yeah, 55 minutes, wow.
Hmm.
How many runs?
Java, Kafka, huh?
Hmm.
does… Rebasing onto main… How stale is this, I guess?
This is hard.
**Florian Lehner** 50:24 It happened, that, after I rebased on Maine.
**Tyler** 50:28 Yesterday?
**Florian Lehner** 50:29 Yeah.
**Tyler** 50:30 Yeah, okay.
**Florian Lehner** 50:31 Yep.
**Tyler** 50:36 Yeah, I don't know. I mean, I can try rerunning this, It's weird that it didn't automatically rerun.
**Nikola Grcevski @ Grafana / OpenTelemetry** 50:44 Maybe because it didn't fail, but it was just canceled.
**Tyler** 50:48 Oh, is that… okay, yeah, I missed… Nikola Grcevski @ Grafana / OpenTelemetry 50:50 So.
**Tyler** 50:51 Yeah.
That does look right. So yeah, it looks like maybe there was something. Okay, I'll… I'll take a look.
That's wrong.
**Florian Lehner** 51:00 Yep, thank you.
**Tyler** 51:02 Okay… Where are we at? This Integrate Configv2, again, also something I'm actively working on. I don't plan to actually turn this into, I think, a real PR.
Itself, but probably split this up.
one of the last things we talked about when we reviewed this was that, like, it didn't have an implementation. I started working on actually implementing, like… there was just wireframe, like, structure here, and now it's trying to, like, actually do configuration of OB.
So, we're looking at, you know, quite a lot of lines change, so I don't plan to actually submit this as this is, but it's more of just kind of like a steel thread to get a reference that we can actually do this on.
It's more, I think, just to develop in public sort of thing, and then I'll try to do… split this up into smaller PRs so that people can actually review this. Mario, go ahead.
**Mario Macias** 51:53 Yes, I'm afraid that this can even have become outdated, because we are adding so many things. Yeah. So, I don't know, we should… find or agree a strategy to be able to… to actually make this config be too effective. But… but I have the feeling that we… we are going so fast.
that this will require another iteration, and maybe once we have this iteration, before even implementing it, we will continue going so fast and adding other configuration options in the old config. So, yeah, I don't know if… In other… this… In other projects, what did they do? If they started to implement it in parallel?
progressively, or… yeah, I don't… Yeah, it's a good point. I'm afraid this will never end.
**Tyler** 52:51 Oh, it'll end.
The reason it'll end is because somebody actually cares about it, and I care about it. And so I'm actually gonna work on this. I do think that, like, it is prone for drift, like you're saying. It's hard to have somebody who wants to add a new feature and a new option and to not think about both places, because it is a burden to do that.
I, I think that… unfortunately, this happened right when I was going on vacation, so I haven't touched it for 2 weeks, but yeah, my plan is to try to get some development momentum behind this again, and try to chip away at this. I think you'll start to see some… some changes coming in. I mean, obviously, like, it's easy to just… Have it languish, I don't want that to happen.
this is one of the big things for the stable V1, that we actually need, so… I'm pretty motivated to get this done. I would say…
**Mario Macias** 53:46 Okay.
**Tyler** 53:47 your concern's valid. Please go ahead and raise it at next week's meeting as well, if you don't see progress in the week after.
**Mario Macias** 53:54 Yeah, but sorry, I didn't… I didn't want it to seem that I was blaming you. I think it's the nature of the task that it makes difficult to… to… to get it on sync. I was not telling, hey, you need to work more on this, sorry.
**Tyler** 54:14 Well, yeah, I mean, it kind of is. I do need to, like, it does need to be a little bit faster. There is still no conf… flicks yet, which I'm actually kind of surprised on. I… but, like, I think it's more about, like.
It's not actually about the integration that's the hard part, because, like, really, you can get this wireframe, it's about the config drift, so if you add functionality to the old config, like, not losing that in the first one.
What I would say is, like, my plan, at least, is there's a considerable amount of work to getting this integrated.
I don't think it's too… too much, but, like, it's not, like, 1PR. And then… Once that's done, I do think that I need to do another audit, just to, like, double check. Like, I have a lot of tooling already built in, when we originally merged the V2, which I think is going to be really helpful here. And it's really easy to go through that tooling and say, like, hey, like, this… is there an equivalent from this configure option to this config option, and just to re-sync on that, and just to double-check to say, like, hey, is there still, like, a full parity between the two of these configuration options after the implementation's done? And if there isn't, then, you know, that can be addressed at that point. So, like, I did try to build some tooling in place to understand that, It's more just, like.
if this language is forever, then that tooling becomes even more out of date. It's harder to get that sync, but yeah, you're right.
**Mario Macias** 55:32 It's a good.
**Tyler** 55:32 point, yeah.
**Mario Macias** 55:35 I think, Stephen?
**Stephen Lang** 55:37 Yeah, Tyler, just on that, is there any part of the tooling that you've built that we could maybe reuse for contract testing, such that we could detect drift and actually fail PRs that introduce new config if they haven't also ported it to V2 as well?
**Tyler** 55:51 Yeah, I mean, yeah, we could start integrating that, like… Yeah, I don't see why we couldn't. There's, like… I'd have to spend a little time looking at it again, but, like, I think it's essentially just, like, regenerating, like, a default config.
looking through that and finding if there's, like, there's already, like, equivalence mappings in the tooling that I had wrote, and if there's a missing equivalence mapping, like, it already fails, so it's just more about, like, plumbing that in and making sure that, like, any new config options are regenerated into that default config.
So, yeah, that's a good, good call. It would add development burden for a little bit for users just to understand that, but maybe that's a good thing, because then they're thinking about the config v2. So, yeah, I'm happy to take that on. I can take a look at that.
**Stephen Lang** 56:39 Yeah, or I can, I can help if you like.
**Tyler** 56:41 Oh, yeah, I would love to help, yeah.
**Stephen Lang** 56:47 I mean, it's a little bit more burden for people who are creating new configuration, but it's sharing the burden over time, rather than landing it all at once and potentially having quite large drift when this is ready for…
**Tyler** 56:59 Absolutely, yeah.
Okay, cool. Yeah, these are great suggestions.
Okay.
We are right up at the time, actually. Is there anything… maybe I'll ask this, we have, like, a bunch of PRs. Is there anything left in the PR list that people are really hoping to get somebody to take a look at, or are waiting on review, or they're blocked in some way?
**Mike Dame** 57:53 I had one, and it can be done async, on my SunRPC one. It's adding another RPC protocol, and Nicola raised up some good points about, we have RPC metrics, technically it's only gRPC that's using those metrics right now.
And so it's… like, there's definitely some that, like.
two RPC systems should be, you know, reporting to RPC client duration, but we include, GRPC status as a default attribute on those, so that's where it kind of gets messy, and from what I can tell, in the OTEL exporter, we can split it out and have two different, like, metric label sets, but for the Prometheus histogram.
it… like, any labels that are in there, so we can't just have gRPC reporting with its status label to the… to the one parent metric, and, SunRPC not, so… That's kind of… I'm really rushing through it, but that's if you… the comments are in the PR, if anyone wants to take a look at it and get back to that.
**Tyler** 58:52 Yeah, I'm kind of bummed we don't have a little more time, because I was just taking a look at that before this PR, and I was thinking through it as well, so.
**Mike Dame** 58:58 Okay, I will… no big rush on it. We can also save some time for next week. We were able to ship that through a fork, so we can take time to really solve it upstream and… I think that if we add more RPC systems, too, that'll be relevant.
**Nikola Grcevski @ Grafana / OpenTelemetry** 59:14 Yeah, there's an upcoming feature, right? Somebody's working on fixing what we do with JSON RPC, so… Alright, we'll have 3.
Yeah, then…
**Tyler** 59:25 Yeah.
**Mike Dame** 59:26 Thanks.
**Tyler** 59:27 Okay, well, cool, we're running up right on the hour here, got a minute left. Any other community announcements or anything really quick? Otherwise, we can end the meeting here.
Awesome. Well, it was good seeing you all again. I look forward to seeing you all in a week, or asynchronously until then. Okay, talk to y'all later. Bye.
**Nikola Grcevski @ Grafana / OpenTelemetry** 59:48 Bye.
**Mario Macias** 59:49 Bye-bye!
