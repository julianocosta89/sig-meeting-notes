SIG: Go Auto-Instrumentation SIG
Date: 2025-07-08
Duration: 42 minutes
============================================================

## Zoom Recording Transcript

**rafael** 00:21 Hey, Tyler.
**Tyler Yahn** 00:22 Hey, Raphael, how's it going.
**rafael** 00:24 I'm good. How are you?
**Tyler Yahn** 00:27 Doing? Well, yeah. Just starting the day, getting all the all the things done.
**rafael** 00:34 Including coffee.
**Tyler Yahn** 00:36 Yeah, that's a big part of it.
**rafael** 00:38 That's the most important part of it.
**Tyler Yahn** 00:41 Yeah.
I try to limit myself. So it becomes all the sweeter when you get a coffee time right?
**rafael** 00:49 Yeah, yeah, I try to only drink in the morning, like after after lunch. I I'm done otherwise. I you know I keep going downhill.
**Tyler Yahn** 00:59 I'm the I'm the same way. I usually have a hard cut off around like 1010, 30, something like that. So, yeah.
which essentially means I have to drink my coffee during this meeting, although it's almost.
But yeah.
**rafael** 01:12 Reach it all.
**Tyler Yahn** 01:13 Hi, yeah, I don't have a problem with that. Trust me.
hey, Ron, how's it going.
**Ron Federman** 01:22 Hey? What's up?
**Tyler Yahn** 01:24 Not much.
Ron's over there switching to beer at this point.
**rafael** 01:36 Art.
**Tyler Yahn** 01:36 Yeah, Hi, Nicola.
so I'm looking at the agenda. We've got some items Nicola. I had seen that you'd put some stuff on the next item, so I'd added them, if you have other topics you wanted to talk about, go ahead and add them there as well. If you haven't yet already added your name to the attendees list. Please go ahead and do so as well, and I will start sharing my screen, and we can get started here in just a second.
Cool, alright well, welcome back everyone for those that were out last week on holiday.
I think to Nicola. You wanted to go ahead and start us off by discussing. This is, I'm guessing from last week's meeting in the Ob project, discussing the project plan to bring the multiprocess functionality. So we can vendor directly from Ob. This is, I'm guessing a little bit of an action item here, maybe.
Sorry.
I can also link Mike's issue.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 03:10 Good idea.
**Tyler Yahn** 03:13 Yes.
Okay, cool. Yeah. Cause this kind of talks. I think a little bit about a lot of the other things. I don't think anybody on the call wasn't at that other meeting, so I won't do a recap. But yeah, go ahead, Nicola.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 03:35 Yeah, I don't know if Ron was on. Were you on the ob meeting when we discussed this Ron? I just.
**Ron Federman** 03:40 Yeah, I joined the lately, but I was.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 03:44 Okay, cool. Yeah, I was just like, as a result of that meeting, I started thinking, well, I mean, if we want to make this happen. We need to kind of like, create a sort of action items and plans to start working through some of these changes. If they're acceptable in this project.
which main thing is like adding some level of multi-process, supports to the probes.
at least on the Ebps side.
And start going in small steps that way, like which means the 1st thing I personally do is the office table.
Adding this process, information things, and and so on.
I was thinking that we can make this work in a sort of a gradual fashion, in a sense that we don't have to do the full blown thing in one go we can slowly kind of get better and better at being able to reuse code and maybe the 1st goal could be. Just make sure we can actually vendor the C source files and then build with Ob user space and then slowly go through this manager and be able to kind of reuse the probe.
go files as well, and so on.
And see how that goes.
Because I yeah, once the probes are multi. The Ebps side in the C code is multi process capable? Then then we can.
We'll be able to reuse it. I would pick one probe to be honest, to start with.
I think the the 2 approaches could be interchangeable like. If, for example, like one thing, is this also stable and process information. I don't think it should impact anything on. Go auto. If we supply a new way to supply constants to the Seep code and we can start with one probe and say, let's attempt to vendor this one alone first.st Whatever is the simplest one. I don't know which one is the simplest. Maybe the database one make that one work with multi make sure that it works exactly the same in go auto.
**Tyler Yahn** 06:10 So we want I think we want the simplest one with the full feature set is probably how I would start there. I definitely know that the database? Yeah, I actually don't know a single probe that doesn't use offsets. So I don't think that's a problem. The process information to events.
I don't think there's.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 06:31 Only a pro, no.
**Tyler Yahn** 06:32 Yeah, I think.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 06:33 Any problem.
**Tyler Yahn** 06:33 I think the only one that might be a little bit different is like the the Hotel SDK probe just because it may contain well, it's still going to take just the one process information. So like, I don't like, yeah, okay, so maybe that's not really a problem.
And then sharing maps using file descriptor rewrites this. I don't think that there's going to be any difference in any one of the probes, so I think you're right. I think it's just more about like what the simplest probe is.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 06:58 Yeah.
**Tyler Yahn** 07:00 So I think database probe seems seems reasonable. I do. Yeah, go ahead.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 07:11 Yeah, I was thinking, the number 3, they're sharing maps that could be done after this initial late, because I don't think we need it. If we just start by saying, Okay, let's 1st attempt to reuse the C file.
then the rewrite will happen in Obi's instrumenter, as it does right now which is equivalent to the manager in go order. So we can start with that and then see how that goes. And once we've done that. Then we can start.
you know, migrating this code over to rewrite the Bps maps into the go out of manager, and then we can maybe leverage that.
**Tyler Yahn** 07:51 So one of the questions I have is like, what's do? Do we all have the same end? Goal in mind? Here is like, is the end goal always going to be to vendor the C code? Or is there a way where we can have, like Standalone.
like probes defined like like a 3rd party probe. We were talking about last week as well. Where.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 08:08 Yeah, I think we want to get to a full thing. I would just say, like in my mind, I'm thinking, how do I get things rolling right. I don't want to work on a project 6 months, and then.
**Tyler Yahn** 08:18 I agree, I definitely don't want to like bite it off all off at once. Right? So I'm a yeah. I just want to make sure that like, because there's probably a lot of unknowns that I don't see in this vendoring process of like going from vendoring the C code to then splitting that off is like it's it's wrapped in some sort of psyllium like wrapped thing around it, right like.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 08:37 Yeah.
**Tyler Yahn** 08:38 So I just want to make sure that, like, we're all working in the same direction. And it sounds like we are. So if that's the case. I think this vendoring the C code sounds like a great idea, because one it'll show compatibility of like like you're talking about like the the Abi essentially at that point. Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 08:53 Yeah, and we have tests for all these things. So now, what I want to do is like, I want to be able to kind of remove the ob version of the dB instrumentation, swap it and test your pass. And if they don't, we need to find okay? Well, this is missing, or we have to do this, and then slowly, kind of make sure that this works.
**Tyler Yahn** 09:11 So how do we? How do we not maintain 2 copies of something.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 09:15 So.
the the one approach we took. We have already some experience with this vendoring, which is why I propose that might be the 1st step. Obviously, because we did that with Bayla vendor. So we then we did a give sub module, and we brought in the full. So in this case will be go. Auto would be a submodule into ob.
to begin with, just the 1st step. Okay? And then, we're gonna implement the same make while changes we did for Bela to when it builds the Bpf programs to also build sub module programs as well and do the exact same thing.
So now we have this additional step.
And since.
like, we don't build the binaries and we don't store them in the repo, this is needed.
but we've already done it for Baila, and I think we can do it in ob the same way to build the Go auto binaries and use them to look.
**Tyler Yahn** 10:19 Yeah, and that that would definitely help. Because then all the work on like, obviously, there's overlapping probes here. Right? So like, then we could we could consolidate any work on whatever one probe it is, it'd be in one location is kind of the key thing.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 10:32 Exactly right. So I mean, I think it's a when to begin with, if we share the same C code, and then we can start sharing the user space code, I think, as well as the next step. And we can decide where we want to go.
If we have one successful that we are able to vendor, I think.
makes makes me a lot happier, more confident than we can then decide. Do we want to keep working on the C programs to kind of expand? Or do we try to tackle? Get this one working fully with the manager and the probe injector like.
**Tyler Yahn** 11:07 Or parallelize it. Yeah, yeah, I think you have people that may be more interested in one versus the other. And I think that then that's where open source is the you know, you benefit because people get to work on one path versus the other. Yeah, so yeah.
I agree. I think that that's a great like, a great entry point to this. So yeah, I think I think that's a great idea.
Ron Raphael does this all sounds reasonable to you.
**rafael** 11:38 Sounds good to me.
**Ron Federman** 11:41 Yeah, same. Sounds. Good.
**Tyler Yahn** 11:45 Yeah, this sounds. I thanks for bringing it up. Action items from this. Nicola. Did you want to create an issue to try to capture and probably multiple issues to capture a lot of this processing? Or is this something that I can help with.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 11:58 Yeah, I don't know what I was thinking of creating one Meta issue to kind of like, prove it out. But but it's up to you. If you want to create, separate and maybe cross, link them in one Meta issue. That tracks the whole thing. I don't know.
**Tyler Yahn** 12:10 That's probably what I would do, I would say, like, have a have a high level issue to track the the end goal of having this. You know, cross functionality vendoring. And then each one of these can be its own sub issue. There's a lot of functionality there in Github these days to do that kind of stuff. So yeah, I think that's a great idea. And then, yeah, I mean, you could really break it down. So yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 12:32 Cool.
**Tyler Yahn** 12:37 Okay, I will put that down as a action item for you.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 12:42 Cool.
**Tyler Yahn** 12:45 Okay, cool. All right. So with that your next topic was, discuss how we fully reuse the manager probe. Can you extend support for different epf probes. Where should.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 12:57 Yeah, there was some comments between Mike and I, and we were kind of discussing either way, like I personally don't mind either way, because but so, my, if, unless I misunderstood, I think Mike wants to keep the the ability to launch Ebpf programs in one place.
So so what this means is like this manager and probe concepts should be shared in common between the 2 projects.
There shouldn't be like an instrumentor and a tracer, whatever we call them.
And then we should reuse that one challenge is that is that Ob has many of these different kinds of programs. So it has K. Probes trace.
I don't know if we use trace I think we might have in the past. Code is definitely there, just maybe not used. There's this escape buffer thing, message programs. There's the Linux traffic control and all these things. So it has a lot more different kinds of Ebpf probes that we can create.
So I guess the question is, do we create like, do we move all that code into, go auto.
keep it in ob, create a separate repo where we we'll share this because one downside, if we move to go auto, then we have to write tests for all these different kind of programs that might be unnatural if Goada doesn't use them.
So you know, like, for example, K. Probes need to function correctly, so we can move the code to the manager and go auto. But unless there's a test, a test injection of K probes and integration test to make sure that data is actually flowing.
we could inadvertently break it, and we not know, and then when we vendor it in ob, then things will be broken, and there will be all this back and forth.
So.
But it's it's a valid point, like, like we want to share this code eventually as an end goal as well.
we.
**Tyler Yahn** 15:12 Yeah, I agree. I don't think that there's a you know.
I think everyone wants to share it, just because, like, then, it reduces overhead as well as like unifies the 2 projects. But I think to your points that like, if yeah, I mean, there's some intractable things that you just mentioned. Right, I think, at the the processing. Pipeline as well, is going to be really hard to like coordinate through the manager from multi process support. But I don't think it like I. I also am not sure that it's impossible.
I do think that you bring up a good point, though, is that just like, you know. If if we want to provide something in the Go auto project that is going to be used in ob.
it needs to support more than what is currently supported.
And if we're not gonna use that functionality here like that seems like a maintenance burden that we don't really want to incur so if that's going to be the case, like, what direction does this go in?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 16:11 Yeah.
**Tyler Yahn** 16:12 I don't know. I do think that like so there, I think there is a world where you can compartmentalize, though like, and you really can try to take this as like a glow, a go functionality thing, and, like, you know, start start building this out as like independent packages. So maybe, like the concept of a manager and the concept of a tracer, I might have got those wrong. But if this can merge into some sort of concept that is held in its own package.
and it lives somewhere right like, if it lives in ob lives. I don't know. It can live in its own repo. To be honest like, it really doesn't matter in the go parlance, right? It's just who is the maintainers of that. And like, who are the people that like are gonna are going to keep the lights on, ensure that the tests pass. I think that is like, you know, a model we've seen in many other parts of open telemetry, like specifically around, like the collector, the Go instrumentation. And like, there's a bunch of other languages that have like crossover right. And so it's just about like ensuring that that becomes unified.
I don't know if I think I think the specifics of this are starting to be like evolved. And I think this is a good place to like kind of capture it. But I think maybe maybe the place to start is to show, like the differences which you've already. You and Mike are already starting to bring up in a lot of this, because, like, I think, if you can show the Venn diagram of like what the manager provides, what the tracer provides.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 17:39 Okay.
**Tyler Yahn** 17:40 Where the overlap is, where the the you know, the areas that don't overlap are like, because if the manager is completely overlapped and it's a subset of the tracer. Then there really isn't a like a reason to say, like.
Keep the manager, it's more just to like, make sure the manager's functionality is exposed through a tracer. And then, whatever that like we want to like, put that maybe put that into a public package that could be consumed in both places that that seems reasonable to me. But if there's, you know, the manager has functionality, and the tracer has functionality that doesn't have like.
you know which one is, the larger subset that we want to bring into the other is is kind of the question, and then where that lives, then becomes like, well, who wants to be the the maintainer of this? Where do we want to do our work?
Does it live in a different repository? I think that all becomes a little bit more of a I think it becomes a little bit of an easier question, especially if you say like, Oh, Hey, there's there's 10 features that the Ob project needs. And there's, you know, one extra feature that the auto instrumentation function needs. It's like cool. Maybe Obi should have the the maintenance, the main maintenance burden of this. And maybe it's the opposite way. Maybe it's like there's 1 that ob needs. And there's 20 that the manager needs. It's like, let's keep this over here. But auto instrumentation world, because, like, we need to actually like we're going to be interacting with this more at the end of the day, like there's the location that it's housed doesn't really matter.
because you can. You can set up permissions in repositories to to make sure that there's ownership models in open telemetry. The the go system doesn't care. It'll import it from anywhere. Right? So I think that's kind of more of just like I don't know. Maybe it's like a vanity thing. I'm not trying to like reduce it, but it like it. Really. I don't see it as mattering. I do think that, like the the touch, points are going to be more important for the person that like has more features there is is the thing that comes to my mind how this gets integrated into the the pipeline, I think, is more important that it's unified, and that we don't have a manager and a tracer. We have a thing now that that replaces both of them. Yeah.
**rafael** 19:50 I just wanna add, like, when I spoke to Mike, I mean, he's not around.
I raise a question with him of okay, this only supports, I think, at the at the moment from the top of my mind. Only, like you probes, and that in, as Nicola pointed out, we need to support all these different kinds of use cases. So I my impression. And I guess.
yeah, in my view, the the variant go for this manager would be for it to support everything eventually, so we could use it otherwise. We end up with some sort of hybrid approach that that you know we're doing. Still, it's still like K. Probes. And you probably, for instance, right? They are the same thing, basically. And then we end up with similar codes in 2 different spaces, maintaining 2 different places. I think the way I I mean the way I see this manager thing going.
it would be something. It's like a big convenience. Api on top of ceiling. Bpf, so that, you know, don't have to do the small stuff so lives it, whether it leaves it like you said in in the Go repo or its own repo for me, the beauty of it would really be okay. I can grab this dependency and use it in my code and replace whatever whatever we're doing. Otherwise, I I feel like, if we have like Tracer and the manager, it's just gonna be a a hassle. Just just my opinion.
**Tyler Yahn** 21:19 Agreed. Yeah. So I think we're all saying the same thing. That's the world we don't want to live in, where we have. We have both of them right? And then it just becomes a question of like the functional support. Because I think also, if you think about like what the manager does. I mean this. This is also a good point, because the manager in Go auto will is a processing pipeline as well as a configuration and setup pipeline. So like, instead of it going through a map.
you know some sort of, or a ring buffer to try to like process these, and like all the it's like. It goes back to the manager. The manager like calls these asynchronous like functions to do the processing of each event. It handles that like coordination across that processing coordinates that into a single event stream that then gets processed down to a pipeline that will then export it right? So like that functioning exists in the manager right now. There's a functionality to support sampling coming down through the configuration, and it's dynamic sampling to ron. If I'm not mistaken. That's that's the ultimate goal. At least, I don't know if it's currently that. But yeah. So I mean, like, there's there's definitely configuration options. I think that are that are existing in the management pipeline right now. I don't know if they exist in the tracer pipeline so we'd have to look, I think, at those as well.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 22:30 Yeah.
Okay.
Okay.
**Tyler Yahn** 22:34 Ron. Are there any other things that the manager's doing like?
Like? Obviously the the silly and ebpf like setup for the specification, finding the maps, making sure that that's all constructed like that, I think, is like I didn't stay it. Say it because I just assumed that it's in both.
But yeah, I mean, I think sampling kind of stands out the processing pipeline stands out as differences.
Anything else. Ron, that comes to mind.
**Ron Federman** 23:00 And not, I think you mentioned like the the big ones. I also, I think I added, capability like to like turn on or off specific libraries at Runtime like.
like. If you use the this as a library and go like you can have some events from an outside like an an outside source that like tells you I don't want this Http instrumentation. Turn it off or turn it back on in one time. I think that's also something that that we added.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 23:37 That's very cool.
It's pretty cool.
**Tyler Yahn** 23:42 Yeah. So okay, I think I think that. Yeah. So I think there's configuration of the the active probes. I think there's configuration of the so the sampling one's an interesting one, like like the sampling concept goes all the way down into the the CC. Space. Is that something that is done in Obi, as well.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 24:00 No, no, it's it's actually Somebody recently opened an issue. And I have to look the sampling right now. We we just in many places assume sample one on that spring.
**Tyler Yahn** 24:16 Oh, just oh, okay. So it's just an always on yeah. Okay. Alright.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 24:19 No, we don't like somebody opened an issue recently, and it pointed out how like on the bayless side. Not unfortunately, but Somebody said, like this parent thing doesn't work. And yeah, I was like, it doesn't.
**Tyler Yahn** 24:35 Yeah. Turns out, parent sampling is that's that's the that's the hard part. Actually.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 24:41 Yeah, yeah, because they they were like.
you know, I, this should have gone through. I I put like 0 sample rate here. And I was using parent sampling. And this should have gone through. But you guys cut it out. So I'm like.
okay, yeah, yeah, I get it. So we don't have in our transparent info applied for. I think maybe we do, but we ignore it anyways, something that needs to be fixed.
**Tyler Yahn** 25:07 Well, so I think that's actually a good good point that goes back to your 1st point around like the C code, because, like it is. It exists like in the database. One like that's gonna it's going to be there right? Like the sampling is going to be a configuration option. So if you start vendoring it, you have to. You have to give it a you know, an always on at least, but like you have to give it something. And I think if that kind of like starts forcing these issues right.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 25:27 I think so. And I like to standardize the data structures as well. Like I, we have something we call Tp info, whatever it's same one that's called like context span whatever span context and go audit like this should be the same structure. It has the same information.
and I think.
like going through the one of these will definitely expose all these issues and will make us think about, how do we fit this together?
**Tyler Yahn** 25:51 So maybe maybe that's just the way to address this this point that you have listed here is that like we can, we can say that there's a dependency on this like this, this 1st vendor of the C files. And just and then we need to have, like a planned retro essentially of like what are like, what's the Venn diagram and define that Venn diagram after the fact or or just capture it along the way, I think is kind of the key, and then and then from there we can iterate and ask like, okay. So now we've gone through one probe like.
what's the next steps, like, obviously, like, we can start working on other probes. That'll be like the horizontal move. But, like, what's the vertical move to get us to getting the manager getting the probe definitions to unify there. And I think you're going to have a lot better of an understanding after the 1st 1st definition. Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 26:35 1st step. Yeah, that's what I'm thinking, like, I think we can.
we can go and look at and think about it. But unless we try it, some of these problems will not occur. So I want to kind of force the issue and do it. Go through one.
**Tyler Yahn** 26:49 And see what I encounter.
Yeah, this all sounds good to me. So yeah, I would just say, like, maybe this, just like, second point. We can pause on that answer for now, and and we'll come back to it.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 27:02 Yeah, I mean, I I maybe there, there's a future where you know. Go water hands go.
That's sort of like a side manager that we use for a goal.
But maybe that's not a good idea. Anyways.
I think there's a lot of duplicate functionality related to offsets and everything that we just want to comment across the 2 projects.
There's no reason why they're separate.
and you probes maybe maybe there's like the you probes is is the one that's coming from go auto, or that's a handler for you, probes, and that must be handled there, or something like that. I don't know like if we don't want to like, share them fully, or that's not feasible because we don't have any. You probes we used to until we ran into trouble we didn't have right now. The only new pros we ever have in ob are the ones that are go out of style.
**Tyler Yahn** 28:03 Hmm.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 28:03 Be careful.
**Tyler Yahn** 28:04 Okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 28:04 Red probes rarely work in my experience.
We found out that it's not just go that moves the stack. There's many other languages that move the stack, and you read pros. Just crash your program.
**Tyler Yahn** 28:17 Oh, really. Okay. Hmm.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 28:20 Yeah. So basically no. Js moves the stack to. So you. And surprisingly, you would not like, we couldn't understand what was going on but we had probe in the node runtime, because live Ssl. Is vendored inside. No, so it's part of the node binary, so they don't use the live Ssl.
Of the system they use cell in the node binary.
**Tyler Yahn** 28:48 You're reminding me of things that I've I've tried to forget long, long ago. Yes.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 28:53 So they have a custom version of Libssl. That's like a version they picked up. And it's in the source. So they build statically inside. So we used to tap into that Libssl until somebody reported an issue. Once in 5 times I run my program and you crash it. Once we have this on, and we looked into what's crashing, and it was like a red probe on something we needed that was reading the return message.
All the read, you know, read, we used to have a rat program read and effectively. She can't do it because no does move the stack as well.
and apparently even the Ssl stuff is.
**Tyler Yahn** 29:32 That's crazy. Okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 29:34 Yeah.
**Tyler Yahn** 29:35 So I mean, like, I think there's good reason is what you're saying.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 29:38 Yeah, there's a good reason to share this stuff I don't want to maintain, like, I think we both have versions of parsing symbols digging through this stuff that should all be shared.
**Tyler Yahn** 29:50 Yeah. And I think also, just like just, we were talking as well, like all the header files. If we could unify on types and unify and language across the projects it would, it would cut down a lot of confusion, but it would also help like that that cross pollination and sharing. So I think that's this is going to force that function. So I'm excited.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 30:07 I'm excited to. It's just I think I wanna stay, this is gonna take a long time.
it's not gonna be done in couple of months, or whatever, but I think we can make a dent forward.
**Tyler Yahn** 30:17 I agree. But I think that as long as we capture, I think that's why it's gonna be important to do a little bit of planning upfront, just to make sure that we have it captured in issues and saying like, this is the direction we're going. So you know, at least to the iteration points where we were like we're trying to do in this, you know, in this push, getting to this point where we have something vendored.
And then we can, you know, I think as if we should like you're saying, if we try to just bite it off all at once, like one. You're gonna see multi 1,000 line Prs, which is never gonna work. And then 2. It's just I don't.
I think there's there's just things that we need to iterate on. So I'm all aboard right.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 30:54 Yep.
**Tyler Yahn** 30:55 Okay.
alright moving on in the agenda. I just wanted to go through our open prs really quick. We've actually made some pretty good progress. I wanted to touch base on some of these. So I guess the oldest one is this ad cross platform. Perf reader, implementation. This one is something we talked about. Ron you were talking about. This is something you upstreamed.
I don't know.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 31:18 They? I think we come back. They have. They never respond anymore.
**Tyler Yahn** 31:22 Okay, so this is just something that needs to get closed. And we need to splinter off any sort of functional changes we want in our own.
yeah, okay, so this just action item for our Maintainer is just to close this and maybe tracking an issue, the things we wanted to add.
cool. I think I hit the wrong button before next up, I think, is the probe lifecycle management. So this is another one that we talked about last week.
This just needs more eyes on it. So I don't know if there's too much to say, because Mike isn't here. But we're trying to get this through, I think, regardless of this outcome here, I think this is help helps clean things up. So yeah, it looks like there's still some conflicts which could get resolved. But it just it still needs reviews. So that's on me, Ron, as well. I see you've also reviewed Rafael. I know you've gone through this as well. If you have time, and you would like to provide some some review that'd be great, we'd appreciate it.
Yeah, just I think the more support we can get for this, the faster it'll move along awesome.
And this also just needed reviews. I just looked at this right before the meeting, Nicholas approved. I've asked for a few cleanup tasks on this. This is dragging on to be longer than probably should from May 4.th But yeah, this is, I guess, just more cycles at this point.
And then last 1. 0, perfect. Okay, this is the one I actually wanted to talk about. So this is one we've talked about in the past. This add distro version, a name by default. The Hotel SDK handler, which is a great feature that we want. There's package import cycles. I got the tooling updated so that that was the whole thing. Let me tell you, this project is is fun. So what we can do now in our versioning file is, we can tell it which files are going to have these version refs. And so this is an example in the build tools. So this Pr can be updated to point to the files that it's including here in this version, dot Yaml, and we can say specifically that you know these new files, this new file here it should be updated to whatever the package version is during the the run of multimod. So it's tested it should work. This should this should work just fine.
You just need to update the version, dot. Yaml, yeah.
Ron, does that sound like something you can do.
**Ron Federman** 33:49 And yeah, do, do we need like to do a release of the multimodal? Or how does it.
**Tyler Yahn** 33:56 Already done. And this repository has been updated to use that new release. So yeah, it's just waiting for us to. I mean. So with that said you should be able to test it. So if you wanted to update the version that yaml and then do a little like test pre-release locally, it should update this file at that point to verify that it works.
Okay, we'll do that.
Yeah, let me know if you have any problems with the tooling. Yeah.
cool. I think that was it for open Prs.
Yep, it is. I do want to point out. Also, I didn't put this in the agenda, but I guess we're at the end. So I'll just point out that there's a There was a Pr for supporting resource, detection, configuration during Runtime. It was a little bit of a biased Pr. So I ended up coming through in the Go Sig. We have this new auto detect package that was just merged this morning, so it hasn't been released yet, but we can depend on like a point release or a commit hash of this. And essentially we can take a look at the examples here, so you can register custom detectors from like 3rd parties, meaning any 3rd party should be able to come through and say like, Oh, by the way, I want to import this package, I want to take my detector, which is not included by normal, and I want to register it, and then what you can do is in in auto instrumentation. This is kind of the key thing is, we can say we will support whatever comes in on this environment variable, and we'll parse it. Based on our own format, which you know in this example, is just, you know, a comment eliminated, you know.
identifier. And then we'll build you a resource detector based on that. So what this does is it'll it'll look up for the environment variable. It'll find all of the names that it knows. There's like a global registry that auto detect manages and that global registry. This is like that 3rd party like register thing. So yeah, what we'll do is we'll build a detector from that. And then we can build our resources on top of you know, custom resources that users provides plus the auto detect thing, and we can merge the 2 resources together. So this is really helpful for things that are, you know. Maybe. You know. Obviously you can use like the hotel resource attribute, and that'll put in whatever static attributes you want at Runtime. This will say like. Oh, I know that I'll be running in. Aws. Gcp azure, or something like that. It'll give additional, you know, resource information about that.
And even 3rd party like, maybe you have, like a 3rd party like cloud ecosystem that you want to support. All you have to do is make sure that this is imported during your build. But yeah, so this is supporting all of the contrib audit resource detectors plus the host and anything built in.
So yeah, hopefully, we can try to build this out. I've got a issue tracking this here. So this just requires a little bit more of a proposal. But I think this is kind of going through that. So yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 36:54 Cool. Can we do this in Obi as well.
**Tyler Yahn** 36:58 Yeah, I don't see why not? Yeah. That sounds like a I yeah, there's there's if you haven't also taken a look at
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 37:06 Say still.
**Tyler Yahn** 37:07 I don't know where this goes. So there's the auto detect package and this is this is inspired by 2 other packages.
The other is the auto export package. This again also handles the. This. One handles the environment variable itself, but it has a similar registry model. So if somebody wants to come in and build their own registers, register their own exporters. We use this in go auto right now. So this is how we set up our trace exporter.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 37:31 Cool.
**Tyler Yahn** 37:32 And then there is a propagator auto prop. So yeah, we have like these, these auto prop stuff.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 37:40 Oh!
**Tyler Yahn** 37:41 Here which does the same thing. So if you wanted to do, I don't know why you'd want anything other than trace context or like B 3. But like, yeah, you can, you can do the same thing here.
And I guess while I'm on it the hotel Conf package is also pretty cool. This supports the declarative configuration. So instead of using environment variables, you can pass in a single configuration file for all of open telemetry, it sets up the SDK, it sets up providers in a way that you want sampling in the way that you want.
this is still a work in progress. This is, I guess, more of a call out, because I'm part of the Sig. If you want to learn more about the configuration, this is the proof of concept in here. It's still supporting it. We're still stabilizing it so obviously like Caveat, I'm tour. But like it's worth checking out. This is going to be really helpful in the long haul, and I think we want to support this in any in Ob and open telemetry.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 38:30 Because this is definitely going to be critical, to providing configuration.
**Tyler Yahn** 38:34 Yeah, instead of whatever homegrown one we have there.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 38:37 Yeah, exactly. Exactly. I know.
So our guys are also heavily into this right?
**Tyler Yahn** 38:44 Yeah.
they're they're really into this. And like, they're kind of leading like the the main. It's funny, like the main configuration. For like the SDK is. Actually, it's it's pretty standard.
The hard part is actually instrumentation side of things. So if you want to configure instrumentation like, how does that hook into this because we want it to be extensible. And they're leading a lot of that, because things like spring and that kind of thing have their own configuration file so like, how do you then interpret it? How do you like integrate with that? And I think again, it's going to become way more critical, not necessarily, for the open temperature go as much as it is for us in like the No code configuration where, like, actually, I want to configure these components of this instrumentation.
How does that integrate? So yeah, I think if that's definitely something we want to definitely want to take more advantage of, we should probably be more active in that as well. But we've got some C code to vendor right now.
Well, cool. Alright sorry. A little bit of a tangent. There, that's the end of the agenda.
Any other topics people want to discuss.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 39:45 Yeah, I just wanted to kind of ask one question because I was doing this hacking on the the go manual spans. I noticed something, and I just wanted to kind of ask. I think it's an issue.
Well, what? When we have that map for span start and end?
Do you guys mind if I change that to an Lru map? I think it should be an Lru map, because if a user misses an end span eventually, if you hit it too many times, you'll just completely populate. The span mapping will never clear it.
So if it's an lru, then we're safe of people, forgetting the 1st pan and.
**Tyler Yahn** 40:21 I see.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 40:21 Does it make sense.
**Tyler Yahn** 40:22 It kind of handles it. A memory overflow in an error case.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 40:26 Yeah, I mean, you won't get those spans, but at least it will not impact the other spans the users might have, so they'll be like, oh, we're missing this one. Oh.
shoot! We forgot to put the span end. So I think putting in an Lru map should be sufficient.
**Tyler Yahn** 40:42 It seems reasonable to me. I would defer to Ron, though I'd love your opinion.
**Ron Federman** 40:49 And yeah, yeah, it sounds good. Like I, I've seen some cases like where the maps get full, like, usually it happens when you have high throughput, like you don't have enough space to save all the active spence.
But the what you said like, if someone and forget to do spend anything. Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 41:11 They'll exhaust our map. And we can't touch it. Right? Because basically, like, you have, yeah.
**Tyler Yahn** 41:18 Yeah, I think I think what you're saying is like, you know, in in normal behavior, this, you won't see a difference. It's just in the error behavior. You don't start crashing new spans from starting right? And like, that's kind of what you want anyways, like. You'd rather like.
you know anything that's super old is probably less relevant, and it may also be an error that they forgot to close it or end it right. So like dropping the older ones is, is makes sense to me. Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 41:43 Yeah, because if they don't put the end there's nobody to clean it.
**Tyler Yahn** 41:46 Right. And and even if if they do put the end, but it's in a high throughput situation like you're gonna have to drop something right. So making the choice of the older spans versus the newer spans is kind of it doesn't like. There's positives negatives to both. So the only thing that like really outweighs. It is like you're talking about like where they do explicitly make an error, and they aren't ending it. So I think that makes a lot of sense to put an lru span or lru cash there.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 42:10 All right.
I'll make feel I just noticed it. And I thought about it. Okay.
**Tyler Yahn** 42:14 Yeah, no, I don't think I didn't think about that. So that makes sense to me.
Well, cool, all right. Any other topics awesome. Well, if not, thanks everyone for joining. We can end it here. Appreciate your time. A lot of great work again. Also, Ob's meeting is tomorrow, so probably see you all in 24 h. Okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 42:42 Sounds good.
**Tyler Yahn** 42:43 Bye, Roy.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 42:44 Guys, bye.
