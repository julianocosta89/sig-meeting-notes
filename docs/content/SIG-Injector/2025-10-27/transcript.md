SIG: SIG Injector
Date: 2025-10-27
Duration: 26 minutes
Zoom Recording URL: https://zoom.us/rec/share/CltlR8kXxKH8L8gVVikk20aIw9j9UeNAkJ9tYU7ItsBEe2RkDmSJ2IwsZX8yKwyF.w6Ix7MO4SXekS3PE
============================================================

## Zoom Recording Transcript

**Ted Young** 01:02 Yo, yo.
**Bastian Krol** 01:08 Hey there! Hi, Ted, how are you doing?
**Ted Young** 01:11 Well, how you doing, man?
**Bastian Krol** 01:13 I'm fine.
So, Antwan just canceled, and I'm not so sure if we have… really have topics to discuss for today.
**Ted Young** 01:28 Yeah?
**Bastian Krol** 01:30 And if anyone else will join.
**Ted Young** 01:33 Cool.
I only have one thing to discuss. I just published, Project file.
**Bastian Krol** 01:46 Oh.
**Ted Young** 01:47 Nice, okay.
This is…
**Bastian Krol** 01:53 Hopefully not just some busy work, but…
**Ted Young** 01:56 helpful to the SIG.
Just clarifying.
who's working on what. This technically should have happened when the donation occurred, so it is just kind of funny.
That it somehow slipped through, but at any rate, I think it's helpful to clarify the main point is, like, why this is, like, so goddamn important.
Like, because otherwise, like, we absolutely would not be starting this project right now. But clarifying that there's a… it's not just, like, this is cool and slick.
But there's a whole group of end users Call them system operators, who at many organizations.
are charged with stuff like telemetry. It relates very closely to security and package management and other things, and that's just, like, who's tasked with this stuff at that org. They're also the people who have the access, where if we gave them something like the injector, they could… could deploy This stuff very widely, very quickly, and for distributed tracing, that's, like, a miracle.
So as part of, like, OTEL crossing the chasm, like we're trying to do right now, like, this has actually become a primary blocker.
And I feel like this is something there maybe is not a lot of awareness of within the OpenTelemetry.
**Bastian Krol** 03:24 Definitely not.
**Ted Young** 03:25 I feel like if you're talking to salespeople, you hear this constantly.
Right, that, like, end users are used to other APM products that have some package-based solution.
And OTEL just doesn't have it, and so they're like.
what do you want from us? You don't have the thing.
**Bastian Krol** 03:47 No, that makes sense. I mean, we discussed that in the last meeting as well, at length, so, I think that's good. Is that… is that based on Michaela's first draft, or… Okay.
**Ted Young** 04:01 Yeah, I cleaned it up, and whittled it down, but… The main thing, I think, that matters for this group is we're claiming, next month.
And, like, early next month, even.
We're going to be trying to deliver something at KubeCon.
**Bastian Krol** 04:24 Right.
**Ted Young** 04:25 So… That's kind of, like… If we're not having a meeting today, that's cool, but that would be my one question, is like… .
**JP Jason Plumb** 04:35 I will tell you.
**Ted Young** 04:36 What's the backlog look like for that bad boy? Hi, Jason.
**JP Jason Plumb** 04:41 I think Antoine is tied up, with some other stuff.
**Ted Young** 04:50 But are either of you working on, something to be ready for KubeCon?
**JP Jason Plumb** 05:00 So, Antoine and I are giving a talk about the injector.
or Ollie Day, I believe.
**Ted Young** 05:06 And so, yeah, the basic trajectory is just to give a background of the project.
**JP Jason Plumb** 05:12 talk about what it does, and why it's useful, and then do a demo. So it's, like, it's pretty… it's pretty basic. It doesn't… I don't know how much roadmap stuff we're gonna have on there, or, you know, trajectory… Yeah. Or if we even talk about packaging at all, I'm not sure.
**Bastian Krol** 05:30 So, what I understood last time, or the meeting before that, was that Antoine wanted to get the release.
or a very initial release out before that, and also includes a little bit of live demos stuff, but I'm not sure if that still is, is the latest status quo on what he planned, and I think there was some movement on the release script PR, but I didn't follow that closely. So, to answer your question, Ted, I don't have any action items for the KubeCon stuff. I'll also not be there.
My understanding was that Antoine and… Gayla wanted to maybe team up on that, or maybe you, Jason, I didn't know that.
Before.
**JP Jason Plumb** 06:26 Yeah, it's really just… yeah, it's just Antoine has a talk accepted, I'm helping out with it.
**Bastian Krol** 06:31 Oh, okay. Gotcha.
**Ted Young** 06:34 I just added a line item link, you know, this is, like, the one… Part of this, I would say, if people take a look at anything, just what we wrote here for timeline, you know, is this real? Does this match with, like, anything anyone is actually gonna do in the next couple of weeks? You know?
And if the answer is no, fine, but we should update this.
And if the answer is, like, we're gonna give a talk about it, come to our talk, that's also totally fine.
But it should just be accurate.
Not immediately out of date.
**JP Jason Plumb** 07:10 Yeah.
**Bastian Krol** 07:13 It matches my understanding, so what I also understood from the week's Previous?
jason, do you have any, any… Do you see the… did you see the link on the agenda?
**JP Jason Plumb** 07:30 It did.
**Bastian Krol** 07:30 Okay.
**JP Jason Plumb** 07:31 It did, yeah, it's talking about packaging.
I think Ted's link didn't link to what he thought it linked to, but I… yeah, I think it's talking about packaging.
**Ted Young** 07:40 Trying to link to the expected timeline.
Section of this document.
Did that not work?
**JP Jason Plumb** 07:48 I don't think so.
But, I mean, well, maybe it did and my shit just didn't scroll, that was real weird. Whatever. Probably because I had it open.
In another tab or something, I don't know.
**Ted Young** 08:00 Anyways…
**JP Jason Plumb** 08:01 Anyway, yeah.
**Ted Young** 08:01 There's a section called Expected Timeline, where we're gonna… Yeah, cut a first release.
of the OpenTelemetry injector, a proof of concept of, you know, apt install OpenTelemetry for Java and Node.js.
**JP Jason Plumb** 08:18 Oh, interesting.
**Ted Young** 08:18 And… And, first draft… of the packaging architecture, right? So we're not saying we're gonna solve it, but we're gonna at least have a proposal for, like.
How one should lay all this stuff out.
**JP Jason Plumb** 08:32 If you factor in…
**Ted Young** 08:34 You can't download one giant blob of everything, and also you want to make room for custom packaging, like, alternatives for various You know, like, language runtimes, be like, go grab this one instead of the standard one.
**JP Jason Plumb** 08:50 Good job.
**Ted Young** 08:51 Or whatever.
How, how should scanning work?
Right? If there's gonna be a stage… This, I think, is actually a place where Michelle is on a different page from some of us. I think he wants the approach to be… the default is this thing just grabs everything.
And certainly, at my organization, we'd want the default to be It does nothing but scan and tell you what You should now go and download, and optionally Install.
So… It could be fine that, like, the initial version just is, like, aggressive, but we should, as part of this planning process, be like, how Doth1 configure this thing?
Based on.
**Bastian Krol** 09:40 What do you mean with scanning? I'm not follow the, what's.
**Ted Young** 09:45 So there's two…
**Bastian Krol** 09:46 to be scanned.
**Ted Young** 09:48 There's two approaches to how this thing can work.
You, you, you have to either… either it… Decides what it's going to attach to.
Right, so it scans, it has some way, no matter what, where it figures out what's running on this machine, and.
**Bastian Krol** 10:06 So you mean scanning the machine it's running on for, targets. Target services, right, to… There is no scanning.
**Ted Young** 10:16 finding magic with.
**Bastian Krol** 10:17 So there's no scanning in none of the approaches that were technically discussed so far. It's… the LDP load just, means that whenever a process starts, there's a binary that is executed before the actual binary. So scanning is kind of a…
**Ted Young** 10:35 Well, okay, but there's the…
**Bastian Krol** 10:36 Yeah.
**Ted Young** 10:37 There's a decision. Yeah. There's a decision.
**Bastian Krol** 10:39 You can then, of course, make a… so we… you can only attach to everything, but of course, you can decide, then, in your… in the injector to stand down immediately and do nothing. Right, exactly. But then if you… if you mean that, then I got it, okay.
**Ted Young** 10:55 Right, like, there's… there's a stage where you decide what to do.
Yeah. But as part of, like, deciding what to do, you probably want to know what your options are. That's where some kind of scanning potentially comes in.
**Bastian Krol** 11:11 for SDK.
**Ted Young** 11:12 The other option is, like, at least just some kind of configuration language.
To be, like… But you… it's… it could be a separate project, but scanning is, like, the next thing, right? If you're gonna be, like.
I want options about what to install or not. You probably want that thing to tell you what it could bind to.
You know, if it so chose.
Right.
Does that make sense?
**Bastian Krol** 11:39 I'm not sure if I'm on the same page here, so we are in the stage where the injector starts as a pre-step to the actual process that starts, and then it can Inspect either the comment line, the environment, or it can also, of course, check for the presence of hotel SDKs or distributions on… on disk. So that's basically the three factors that I could see going into a decision whether or not to actually inject that particular process. And the configuration file or stuff like that can also, of course… I think we already have a configuration file that Currently, you can only disable and enable stuff based on the runtime, so you can say, okay, Node.js, where is, where is the, Node.js hotel packages, and… disable Node.js instrumentation or enable it. That's what the current status quo is.
**Ted Young** 12:46 Yeah.
**Bastian Krol** 12:46 Yeah, of course.
**Ted Young** 12:48 That's probably fine as, like, a starting point.
**Bastian Krol** 12:51 Right. Okay.
**Ted Young** 12:53 you know, that's… that's one area where, yeah, I think we wanted some clarifications. Like, in the long run, we should expect people To want to be able to configure this in various ways.
And that's probably not something we should try to tack on.
after the fact.
And it seemed like Michelle, there was maybe, like, was more interested in, like, just don't worry about that, just bind everything, that's what everyone.
**Bastian Krol** 13:20 Yeah, yeah, I think the difference is maybe here that from the dash zero perspective, where Michael and I come from, by the way, it's Michael, not Michelle, but never mind. Oh, sorry, Mikael, sorry. Yeah, So Michaela and I, we come from the Kubernetes angle, and we basically already have made the decision. We have this Kubernetes, let's say, port deployment, whatever, and either we attach to that or not, and then when we do that, then inside the port.
basically, the decision is already made, but of course, on a bare-bone metal host or in a VM that looks very different.
different perspectives.
**Ted Young** 14:04 Yeah.
**Bastian Krol** 14:04 But we can accommodate both perspectives, I'm sure.
**Ted Young** 14:09 It's always this problem of, like, we don't have a real distributed operating system that we can depend on being there. And that means every component ends up reinventing its own control plane, its own form of, like, service discovery.
There's, like, all this stuff that… and yeah, if you're using Kubernetes, then the approach is, through the Kubernetes operator SIG, we figure out how to wire all of that up. But we actually make it clear in this document that, like, we're actually not gonna mess with any of that in this SIG.
Like, when it comes to figuring out how to wire all of this stuff up with Kubernetes, that's, like, some other SIG. What we're gonna provide is, like, what if you just had Package management, but if you just had…
**Bastian Krol** 14:54 Yeah.
**Ted Young** 14:55 one form of Linux package management, and we'll give you that.
**JP Jason Plumb** 14:59 Because clearly a lot of your customers and mine are some of the ones that need the most help, or the most visibility into what their processes and systems are doing, and they haven't been able to make the leap yet to, you know, contemporary cloud-driven stuff. So, yeah, that's kind of the target of some of this stuff.
**Ted Young** 15:18 It's very much a high overlap when it comes to crossing the chasm, right? It's like… oh, now we want to onboard a bunch of people that have operators that are a bit more like sysadmins, they're operating a whole bunch of Linux virtual hosts.
**JP Jason Plumb** 15:34 Managed by some kind of hypervisor.
**Ted Young** 15:38 And that's just, like, the world they're in.
Yep. You know?
And if you're like, it's just package management, they would be like, cool, we know, we know exactly what to do with that.
**Bastian Krol** 15:54 Yeah, no, that's… that sounds good from… from… My perspective…
**JP Jason Plumb** 15:59 So, I can leave a… I can leave a comment on your PR, Ted, but I… I personally don't have cycles to work on, package stuff before then. Marty.
**Ted Young** 16:08 Totally.
**JP Jason Plumb** 16:08 overextended, yeah.
**Ted Young** 16:11 Again, not me attempting to dictate.
**JP Jason Plumb** 16:14 But Antoine might have some…
**Ted Young** 16:15 should be.
**JP Jason Plumb** 16:15 He might have someone identified, or he might be already working on it, I'm not sure.
**Ted Young** 16:20 Yeah. Need to talk more with him.
I mean, we're very hot to roll this out with my team and Jack starting on my team.
**JP Jason Plumb** 16:29 Yeah.
**Ted Young** 16:30 But, you know, we probably won't have our feet under us.
as far as, like, contributing anything upstream by KubeCon, because that's just coming up in a couple of weeks, so… Yep.
**JP Jason Plumb** 16:43 You know.
Yep.
Did… I mean, the question… I think, the question that was… one of the questions that was raised last time was around, package repository versus just having devs or whatever, like, and I think the.
**Ted Young** 16:57 Yeah.
**JP Jason Plumb** 16:57 was the… GHCR doesn't, like, cannot act as a Debian or RPM repository?
So, we'd need to identify one of those elsewhere, like, I think… I don't know, JFrog was maybe mentioned.
But then, like, do they have a free plan, or is it… can they… can they fund it? Do we know?
**Bastian Krol** 17:20 Do we not… we don't have any packages whatsoever in the OpenTelemetry ecosystem so far?
**JP Jason Plumb** 17:29 I'm not aware of any…
**Bastian Krol** 17:31 Yeah, me neither, okay.
**Ted Young** 17:32 Didn't we find some, like, random stuff with, like, OpenTelemetry, C++? There's some, like, just random hotel packages hanging out.
**JP Jason Plumb** 17:39 That was in Homebrew, yeah, I was looking at.
**Ted Young** 17:41 Okay, that was at home.
**Bastian Krol** 17:42 I don't know. Okay. I don't know what that one was.
**Ted Young** 17:46 Totally random stuff.
**Bastian Krol** 17:48 Correct? Yeah.
**JP Jason Plumb** 17:52 Yeah, let's see, I don't know, I'll just… I'll search the entire org, is there any sort of, like…
**Bastian Krol** 17:56 But I think for KubeCon, it would really be enough to just have a Debian package and do an app-get from that package without any repository. I think that is a question that can be solved very much after the KubeCon…
**JP Jason Plumb** 18:14 Yeah, because we could still build that as, like, a binary artifact, sign it and publish it, and then people could download it and depackage and stuff. Yeah, okay.
**Bastian Krol** 18:22 And I think most of that work is basically done, so, the, the… Debian and RPM packages are already built correctly. I think the only bit that's missing is really actually uploading them as a GitHub artifact, and that, I think for that, it can just be a file on…
**JP Jason Plumb** 18:43 Yeah.
**Bastian Krol** 18:44 on GitHub, as a build artifact, and that is good enough. And I think Antoine already basically has something… In that PR, which is in progress right now for that.
**JP Jason Plumb** 18:59 Cool.
**Ted Young** 19:02 Something I'm interested in is… so I'm a fan of conference-driven development.
And KubeCon is, like, pretty close.
But, we have Fostem and OTEL Unplugged February 3rd.
in Brussels, and that feels like… I'm curious, you know, we can punt this to Slack for the next meeting, but, like.
having that be, like, our next deadline, so it's, like, great to have KubeCon in a couple weeks is, like, here's, like, a demo, like, we can give you, like, a demo of a prototype, and that's a great goal, but if, like, the beginning of February, we could say, like, we have some form of this that's, like.
shippable in beta, or something like that. You know, like, here is the subset where we're saying, like, people go actually stand this up. It's beta, might blow up, but go stand it up.
And whether or not February… beginning of February is, like, a realistic… Gold to, like, pick something for that.
**Bastian Krol** 20:08 Yeah, I think that's… Could be doable.
But I think that ultimately needs to be a group decision with this.
**Ted Young** 20:16 Exactly, yeah.
**Bastian Krol** 20:18 Like, everyone and Michael at least be involved.
**Ted Young** 20:21 It could be the operator, like, it could be… it could be… or it could be, like, just… again, we're taking our Linux package management thing, and we're saying, like.
for Java and Node.js now, you know, starting in Feb.
This is, like, supported in beta. Like, like, go use it. We'll give you this beta level of support for it.
And then we can start trying to find people who Who are in that, that funny… situation where they want OTEL bad enough that they're willing to use Something in this state to roll it out?
There's definitely people out there, I think, who are potentially in that that state.
Cool. Okay.
That's all I wanted from this meeting.
I'm feeling good.
**Bastian Krol** 21:16 Good.
Excellent.
Jason, do you have anything on your mind?
**JP Jason Plumb** 21:23 Nope, I'm just kind of trying to get caught up to speed on some of this stuff, and helping Antoine out on the Splunk side, because he's also stretched thin, so… Yeah. Maybe two people stretched thin is, like, almost a whole person being stretched thin? I don't know.
**Bastian Krol** 21:37 Not really.
**JP Jason Plumb** 21:37 I don't know how to…
**Bastian Krol** 21:38 Fantastic.
**JP Jason Plumb** 21:39 But also, yeah, I just want to be around, to help put a demo together, that's really what I'm looking to do.
Awesome. Yeah, looking forward to that. Yeah.
And for me, I mean, this stuff… like, using LD preload, I mean, this is like… it's kind of obvious to me, like, that we've been doing this stuff for a little while, and to have it be open now is, like, great, and to see it… the directions in which we want to take it is awesome.
it's… it doesn't… I mean, whatever, I'm just, like, old and jaded, like, this doesn't seem novel to me, like, this is just, like, you know…
**Bastian Krol** 22:19 now.
**JP Jason Plumb** 22:19 you know, it's fine. And some…
**Bastian Krol** 22:21 I think the only novel part is really that, that it's, kind of in the open ecosystem now, because that trick has been around for ages. Every vendor under the sun has… or a lot of them have something that is early preload-based, but everybody comes up with their own… solution, I think.
**Ted Young** 22:43 I…
**Bastian Krol** 22:43 Yep.
**Ted Young** 22:44 I think Zig helps here, actually, right? Because you get this reflexive, like, this is unsafe, because it's true that the fundamental programming environment is unsafe, right? And so being like, no, no, no, no, no, we've got, like.
like, a legit effort to make that environment safe with Zig.
That does actually, like, turn heads a little bit in terms of some of the the weird… black you'll get. Yeah, I mean, I'm not.
**JP Jason Plumb** 23:14 Have you…
**Bastian Krol** 23:15 Bye.
**JP Jason Plumb** 23:15 experience?
**Bastian Krol** 23:17 So, yeah, we are…
**Ted Young** 23:19 more from, like, the EVPF people believe LD preload is the devil, and the reverse also appears to be true.
**JP Jason Plumb** 23:26 Like.
**Ted Young** 23:26 Both communities are committed to the bit of saying the other one is doing foul black magic.
**JP Jason Plumb** 23:32 Okay.
**Bastian Krol** 23:33 Right.
I'm not sure if Zig is such a… large factor. It's, it's, it's… a good language as a sweet spot for exactly this kind of thing, that's true, but of course you can write the same safe code in C or whatever, that's also possible if it's tested well enough. There is still really independent of the programming language, there's still a risk of breaking stuff, just because it's based on the linker, and if you, I don't know, expect a symbol that isn't there, or the other way around, and you still break stuff, no matter how memory-safe your language is.
**JP Jason Plumb** 24:19 And there's always a potential, because it's… when it loads, and it's loading configuration and stuff off disk, like, if that's tamperable by anybody, then they can tamper with what's being injected, and so there you go.
**Bastian Krol** 24:33 Yeah, yeah, yeah. It's all…
**Ted Young** 24:34 And just, from a… from a marketing standpoint, it's helpful to say we aren't just… freewheeling it, you know, we're working in a managed environment. But really, what I agree with is this effort only succeeds and continues to succeed based on the experience of the engineers that staff it. If it was, like.
a bunch of, like, full-stack, you know, cowboys who are like, wee, let's go learn about LD preload. I would be, like, slamming the door on this whole effort, like, so hard. You know, it's… it really is helpful that it's just… the people involved are experienced in the domain. That's… that's what makes it safe.
It's knowing what you should or should not be touching, right?
Like, knowing… knowing that there's… there's a well-trod domain, and that we're just going to go fraud in that well-trodden area, like, there isn't a… A goal to do something novel here.
I know.
**JP Jason Plumb** 25:34 I knew…
**Ted Young** 25:35 fold.
**JP Jason Plumb** 25:35 I'm sure that this has been talked about in other, like, injector SIG meetings, but I think there's also… I think I've even heard you say this, Ted, that there's, like, lots of room for other, Like, installer tooling, in whatever that looks like.
Like, you mentioned scanning, like, even having something that's not the injector, per se, but something else that's like, sure, we'll go look in common places, we'll look at your current process list.
**Ted Young** 25:59 Yeah.
**JP Jason Plumb** 26:00 Like, guided, like, command line style, and even interactive, like… Guide you through setting this up, and…
**Ted Young** 26:06 Yeah.
It would be part of op-amp and the collector, right? The collector and op-amp would get a little component that would learn how to drive the injector. If you wanted to use op-amp to drive the injector, you could totally see.
And then it's just giving that thing the permissions to drive the package management on your behalf. It's not actually, like, a complicated thing, but… but yeah, totally out of purview of thisig, potentially.
**JP Jason Plumb** 26:34 Yeah.
Yep.
**Ted Young** 26:37 Cool.
Cool, guys.
**Bastian Krol** 26:43 Okay?
**Ted Young** 26:45 I'll see you on the internet.
**JP Jason Plumb** 26:46 Yeah, take it easy.
**Bastian Krol** 26:48 You're around?
**JP Jason Plumb** 26:49 Bye.
