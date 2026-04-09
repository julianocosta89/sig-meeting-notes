SIG: eBPF instrumentation
Date: 2026-04-08
Duration: 60 minutes
Zoom Recording URL: https://zoom.us/rec/share/HhugnxBy6anWrqjR8R6szaSiSdZoC_G4aV0TvCIVL4AP44iyf4BVevxk-LWLKrfn.W4zP2uSoP8TxeC3c
============================================================

## Zoom Recording Transcript

Mike Dame 00:01:13 Worse of habit, I almost typed Google.
Tyler 00:02:03 Hey, how y'all doing?
Mike Dame 00:02:07 Blue.
Stephen Lang 00:02:09 Alright.
Tyler 00:02:12 Mike, I don't know if I can take you seriously anymore.
Mike Dame 00:02:18 Homp.
I'll grow it back for you.
Tyler 00:02:24 Yeah, right, just, just for me, yeah.
You look good, man, I'm just joking.
Mike Dame 00:02:28 Yeah, it's so nice. Like, my face is free, I can, like… I can eat chicken wings again without having to have… Bunch of paper towels.
Tyler 00:02:41 Yeah, it's a different life, right? Yeah.
Mike Dame 00:02:43 Yeah.
Tyler 00:02:44 I guess you are, you're now, slaves to the shaving routine, though, which is kind of a pain, but, you know.
Mike Dame 00:02:52 Yeah, but you still have to, even when I had the beard, you gotta do, like, trimming and keeping it up to date, too, like… Yeah, good point. …get all the scraggly parts off so it looks presentable, so I'm like, I'm still shaving anyway.
Tyler 00:03:05 Yeah, no, good point.
Mike Dame 00:03:06 Like, classic engineering problem. I was like, I've solved the inefficiency, let's remove the deprecated beard.
Tyler 00:03:14 Right? Yeah, absolutely.
Shaving interest group. Yeah, exactly, Raphael.
Cool. We can get started here in just a second. I've got things loaded up. If you haven't yet, go ahead and add your name to the attendees list. If you have agenda items, go ahead and add them there as well. There's a fair amount on there.
Yeah, and then, yeah, we can jump in here in just a second.
Okay… Yeah, alright, let's, jump in. Welcome, everybody. So, to start us off, Mario, you wanted to talk about controlling, cardinality in the default config and proposal to use the default of exponential histograms?
Mario Macias 00:04:25 Yeah, we had some complaints from some users.
Telling us that their default… the cardinality of Obi with the default configuration is too high, and they have to still to do some… even if we provide some tools to keep it under control.
They still have to do some fine-tuning, manual tuning of their cardinality. One of the common sources of complaints providing high cardinality are the histograms.
The default histograms, buckets in the OpenTelemetry specification.
the number of buckets is too height for some users. So, yeah, one of the… one of the advices we do is to use exponential histograms in OpenTelemetry.
also in Prometheus.
So I don't know what would you think on defaulting to exponential histograms. That will imply that Adding a breaking change.
Just because, the kind of metric that is exported will be slightly different for… for histograms.
Tyler 00:05:56 So, I don't know what…
Mario Macias 00:05:57 What do you think?
Tyler 00:05:58 I got a few questions here. So, on the exponential histogram thing itself, I'm pretty sure that we need to look at the specification, because I think that's not the default behavior as specified. And I think that the default behavior says that we need to be producing, not exponential histograms, that's, like, default histograms.
But I'm a little bit more concerned about, like, the underlying question, because, like, changing histograms isn't gonna actually affect cardinality, right? Cardinality is set by, like, the attributes that are recorded For the metrics.
And, like.
Mario Macias 00:06:29 Isn't the number of buckets affecting the cardinality?
Tyler 00:06:35 No. No, so the cardinality is gonna be, a representation of, like, the unique grouping and combination of attributes that are being recorded. So, if you have attributes that have… are open-ended and are not, like, bounded to a particular, like, number set. That means that that's… that's going to produce the number of data, points to… be unbounded as well. You know, it's like, for instance, like, if, like, we don't have this, well.
kind of have this. But, like, if you have, like, a route, and that route is being added to the metric, and that route has, like, a user ID in it, and every, you know.
user ID is unique, that means that you're gonna have as many user IDs as you do metrics at that point. That's the cardinality. Plus, if you have any other distinguishing attributes, then you have, you know, essentially the cross product of that entire, dimension space. That's where the cardinality comes from.
Mario Macias 00:07:29 Yeah, I may be thinking on… maybe I'm thinking on concrete implementation detail, because when… when Prometheus ingests it and converts it to Prometheus metrics, they attach these LE attributes, basically enumerating the bucket.
Number, so… Right.
Tyler 00:07:54 Right. Yeah, that's… you're right, in the Prometheus representation, it does become additional lines in their scrape protocol. Okay. So that… that is the case. I'm not actually sure how the Prometheus, what they call native histograms work.
I, I… Actually, I can't remember. I looked at them a while ago, but you might be right, like, that may help cut down on buckets, just because it will dynamically scale those.
But, like, you still won't have solved your carnality problem, if that's the main thing that you're trying to do to resolve it, though.
Mario Macias 00:08:29 Okay.
Tyler 00:08:31 I would also, like, yeah, maybe, maybe to the person who's asking you this, like, asking, like, what their attribute space looks like is gonna be important, because what we've done for, like, route pattern matching, could be used, like, maybe it's routes that are causing this issue, but maybe there are other attributes that we can try to provide, like, templatized versions of, in other ways that could help reduce the cardinality here. Because I think that's going to be the more… Durable solution, not necessarily the instrument type, yeah.
Mario Macias 00:09:03 Okay, okay, okay.
Tyler 00:09:07 But yeah, it definitely is going to be very user-specific. So, so that's… if that's the case, it's also, I actually don't know if we fully implemented the… because I know we redid a lot of the metrics SDK work here in Obi, or in, like.
I don't know what the view situation is, but, like, that's usually where we use views if we did want to switch to using a different instrument, for aggregation for these particular things, so you should be able to do that, and just have the user provide its own… provide their own view, or…
Mario Macias 00:09:35 Okay.
Tyler 00:09:35 Or maybe, like, in Bela, like, you guys are like, I don't want to do this by the default, but, like, you could always set the set with a view there, should work.
It doesn't, we should try to fix that, because that's what views were intended for, so, yeah.
Mario Macias 00:09:50 Okay, okay, okay, okay, thank you for the advice.
Tyler 00:09:53 Yeah. And I think, Actually, now that I'm saying it, so that's gonna be for a particular, like, stream, so it's like a instrument name or something like that, but if you wanted to just, like, completely change the defaults, I think there's a way to also do that by setting the default aggregation selector.
is another thing in the metrics SDK that you can do? I don't know if… I'm, like, 99% sure I saw that, that we copied that in here as well, so that should be another way if you just wanted to just turn everything into, exponential histograms.
So, you know…
Mario Macias 00:10:22 Okay.
Tyler 00:10:24 Yeah, we've seen this as well, like, downstream in the Go SDK, where people want this as well, and, like, I think we provide a way… it's like a low memory selector or something like that? Don't quote me on that one, but essentially, it's that change that you talked about as well. It's just that we kept the original defaults, because that's a breaking change for us as well, but I think it's also something that came from the specification. So, yeah, worth pointing out.
Mario Macias 00:10:48 Okay, okay.
Yep.
Cool.
Tyler 00:10:52 Okay.
Yeah, I hope that helps. If you have more on that, like, if you wanted to get some data shapes or something like that, and we could talk through, I'd be happy to… To see if we could try to make that a little more optimal as well.
But, yeah.
Okay, that sounds good. Mario, you ready to move on from that one?
Mario Macias 00:11:17 That's fi- it's fine, yeah, let's move.
Tyler 00:11:21 Okay, cool.
Giuseppe, you have two more issues, closing the following issues?
Go ahead.
Giuseppe Ognibene | Coralogix 00:11:31 Yeah, the first one I already asked on a slug. I think we can close it, I mean, I don't know what you think, but… The minimum kind of version we are supporting is 5.8, I don't know why we should support 5.4.
It will be a mess, I think, to support it. I'm not sure if it's convenient.
So I think we can close it.
Tyler 00:12:00 Yeah. Any opposition to this?
Rafael Roquetto 00:12:11 I think it's good. If we don't have any customers that depend on that, that's, less is more.
Tyler 00:12:17 Yeah.
I think the original concern was that maybe there was, like, a cloud platform or something, but it sounds like this user was just running in their own… setup, so, I think the answer there is to… Upgrade.
So, yep, right.
Antonio Jimenez 00:12:31 I have a question, Taylor. Is that documented? That we are not supporting… I mean, it's not supported, that version?
Tyler 00:12:37 Correct, yeah. That's also something that we've documented upstream.
Giuseppe Ognibene | Coralogix 00:12:45 The status?
Nikola Grcevski @ Grafana / OpenTelemetry 00:12:47 Yeah, it's darker.
Antonio Jimenez 00:12:48 this, sister.
Nikola Grcevski @ Grafana / OpenTelemetry 00:12:48 5'8 and above, yeah. Or…
Antonio Jimenez 00:12:51 next quarter.
Nikola Grcevski @ Grafana / OpenTelemetry 00:12:51 418 Redhead with, the eBPF patches, which they've… Redhead is backboarding a lot of changes, so I think… Yeah, it's all documented.
Giuseppe Ognibene | Coralogix 00:13:03 Yep.
Antonio Jimenez 00:13:04 Hmm.
Nikola Grcevski @ Grafana / OpenTelemetry 00:13:06 Yeah, it's kind of like, it's annoying that 418, you can… people get confused, but it's not every 418. Yeah, it's not every 418.
Tyler 00:13:17 Hey.
Nikola Grcevski @ Grafana / OpenTelemetry 00:13:18 Okay, yeah, I think I finished, I finished for you, sorry. I said it was supported, with 5.8 and 418.
Tyler 00:13:26 Yeah, perfect, thanks. I… I don't, I'm guessing, I think, Docker just had to take off while I was in the middle of, Yeah.
Nikola Grcevski @ Grafana / OpenTelemetry 00:13:36 They're seeing your screen, just by the way.
Tyler 00:13:38 Okay, thanks.
That's, you get to troubleshoot with me. Okay.
Sorry about that. I don't know if we're back under control, but we'll give it a try.
Okay, so yeah, followed it up, yep, that sounds good. And then, next up…
Giuseppe Ognibene | Coralogix 00:13:59 Do you wanna…
Tyler 00:13:59 We'll talk about this.
Giuseppe Ognibene | Coralogix 00:14:01 Yeah, I tried to understand what the guy wanted, but I'm not sure. I saw that, I mean, the issue is stale, nobody's commending it, so… Maybe we can close also this one.
I saw that he opened up, PR on Mila. He got some comments.
Long time ago.
Nikola Grcevski @ Grafana / OpenTelemetry 00:14:23 Yeah, I can explain. The idea is that now that we are back to Jenobi into the collector.
And we did that in the past with, Bayline Alloy.
He just wanted for Obi, in this case, to output a log of which… Capabilities are actually being used.
So that… People investigating, somehow, like, capabilities or security things, mostly in the world of… The collector and so on would get this information.
Giuseppe Ognibene | Coralogix 00:15:08 is something that we may need in Obi, or not?
Nikola Grcevski @ Grafana / OpenTelemetry 00:15:15 Yeah, I don't think it's, It was just an idea. I don't know if there's many people that… want this or care about this, at least we haven't heard. I think it's just an engineer that thought that this might be a good idea.
to trace the… I don't know, the capabilities.
I don't know if there's any… User feedback or customer feedback that drove this.
Florian Lehner 00:15:44 We are getting similar requests sometimes, and we have the standpoint that we are an observability solution, and we don't track 100% these capabilities. So, if you want to have a security solution to track these, you know, capabilities usages.
then maybe something else might be better. We don't have a 100% guarantee to catch them all, so… That's why we try to separate from these use cases, at least on the profiling side.
Nikola Grcevski @ Grafana / OpenTelemetry 00:16:16 I just…
Rafael Roquetto 00:16:16 I wanted to add… that another… if we one day decide to do this, because I briefly looked into it, we should profile it, because the… The K-Proes where you would attach to get this information, they fire all the time. They are… they are, like, indirectly called by lots of system calls and things like that.
So, just something to bear in mind.
Nikola Grcevski @ Grafana / OpenTelemetry 00:16:41 Hey, maybe, I mean, I like Florian's idea, maybe the answer here is that this belongs into, security monitoring solution, not OB. Because even if we said this for OB itself, it would not be the final answer anyways. You might have the profiler in the collector, and then… Right? So you can be packaging both.
we probably want to suggest something like, I don't know, Falco, Tetragon, there's… Both are CNC projects, so… They can use that.
Tyler 00:17:19 Well, and so the thing is, like, if I'm reading this correctly, there's already a script here that, like, it does this. It's just that.
Nikola Grcevski @ Grafana / OpenTelemetry 00:17:25 I'm sad.
Tyler 00:17:26 set it up, you know, and it's not as easy as if we had built this in. So I don't think it's, like, there's no way to already do this.
And for that reason, like, even if there's another product, like you're saying, like, yeah, maybe that's just… should be focused in there.
Yeah.
Nikola Grcevski @ Grafana / OpenTelemetry 00:17:45 Yeah.
Tyler 00:17:45 Okay.
how do you spell a creep? Yeah, that's how you spell creep. Cool, alright.
Let's close it.
Okay… Awesome. Nice cleanup. Giuseppe, moving on, you wanted to talk about moving this issue to a discussion?
Giuseppe Ognibene | Coralogix 00:18:44 Yeah, I don't know if it's a best practice or… but it's an idea to move it to discussion, because I saw that it was closed, then it was reopened, because maybe it's something that people, like, usually complain about.
But maybe we can close it, like, move it to discussion, where… I don't know, I don't like to see so many open issues. I'm trying to, like… Closing.
It gives more, the idea that the project is… There are people that are working on the project.
Tyler 00:19:23 Yeah… So, it, Is there… it looks like there might be an outcome here, though? Like, are we looking to reduce things, or is this just asking for strategies around this? It seems like Mark thinks there's, like, a bug, if I'm reading this right.
Nikola Grcevski @ Grafana / OpenTelemetry 00:19:39 I think it's…
Mattia Meleleo 00:19:39 Is this what we fixed yesterday, Giuseppa?
Nikola Grcevski @ Grafana / OpenTelemetry 00:19:43 Previously, yeah.
Giuseppe Ognibene | Coralogix 00:19:45 I… I thought… I thought it because there was the environment where it was the same, but I'm not sure.
Nikola Grcevski @ Grafana / OpenTelemetry 00:19:53 Yeah, this was already fixed, I believe, because we had an issue with the tracer exporter.
Giuseppe Ognibene | Coralogix 00:20:02 I mean, the last comment, the… the guy said that it's fixed, the error is gone, and blah blah blah.
Mattia Meleleo 00:20:09 Yeah, but you had to do some workaround, which is to reduce the max queue size. If you actually increase that, that won't fit into the 1000 default, yeah.
Nikola Grcevski @ Grafana / OpenTelemetry 00:20:20 Thanks, hon.
Mattia Meleleo 00:20:20 Yeah, I think… I think we can write to… to retry again with the new version that we are gonna release, the 071, if everyone agrees to release a patch release.
Nikola Grcevski @ Grafana / OpenTelemetry 00:20:34 Yeah? Let's do it.
Giuseppe Ognibene | Coralogix 00:20:36 That's another…
Tyler 00:20:55 Yeah, okay, cool. It's the milestone.
Although I don't know if this is gonna go with that one. Okay, anyways.
Okay, cool. Yeah, I guess we can see if there's verification on that, otherwise we'll probably just close it, assuming it gets fixed.
Okay, next up, I wanted to talk about, work… being done on the stable release progress, so, I've updated the dock, this was kind of like, Just a… a stub?
And I've updated a little bit more of a concrete as, like, a gate, for trying to get this done.
And going through what we have, this is one of the bigger goals I think we want to accomplish this year, and we seem to have committed to it, which is a good thing. I think this is going to light a fire under us.
So, essentially, I've tried to go through this and update it in… find some, I think, concrete things to do. So, I think the configuration is a big one that's blocking this right now, so that's still something I've been working on. But I wanted to also, like… Talk about what it… what it talks about. So, it talks about… Dealing with the configuration, its integration with the declarative config is kind of, linked, but there's a little bit of an overlap there, because the declarative config actually needs to, I think.
Tell it where to put its config, but that's a whole other thing.
The CLI flags are definitely something that are in it. Release binaries, submitted telemetry surface, supported matrix, and then upgrade and version policy.
all of these things, the support matrix, I want to talk about in just a sec. Anything not explicitly included, I think is going to be out of the scope, but, like.
that's up for discussion. I'm asking people to review this. One of the things that, like, I wanted to say, I'll say is that, like, The non-goals for the V01 are kind of important, so having the full declarative configuration capabilities may not be something that, like, you have to have, it may be something we can continue to iterate on.
Meaning, if we don't support particular, configuration paths for, like, pipelines or something like that, I think that that's fine, as long as we're working towards it after the V1. Yeah, every possible per-per-service or per-service configuration refinement, obviously, like, you can't boil the ocean, you gotta cut it off somewhere.
Same with protocols, like, it's, obviously, there's gonna be an open-ended amount there. All of the bugs in the repository, obviously there's some that we need to fix, some that, like, don't make that line, so I think that we need to audit that, but that's included lower.
And then, obviously, feature expansion, we'll have to kind of find a line for that as well.
Which I honestly don't think is gonna be too hard, but just wanted to call it out.
So… kind of as that, I think with those in mind, define those as, like, the blockers. So the big thing right now is just defining that compatibility contract. So what is, like, in scope for this V1 is kind of the important thing.
everything else kind of falls from that, I think. So… We can talk a little bit about this, defining a support matrix, coming up, but yeah, essentially, like, defining the scope's really important. The configuration stabilization, so there's obviously iteration and a desire to land a V2 for the configuration model, I think is important. Iterating after a V1 on the configuration is going to cause some churn, so… trying to do it before the V1, I think, is my goal, and it's progressing, so, yeah.
The other thing is telemetry stabilization, so we definitely need to, I think, provide telemetry in a stable way, for users that want to depend on it. Obviously, like, there's gonna be some… changes, so if we wanted to add new things or something like that, obviously telemetry for those new things, especially if it's not defined as stable and semantic conventions, may change. So… I think kind of understanding where that scope is for the telemetry that we're producing, is going to be important. Things like HTTP, which have stable semantic conventions, I think is something that would fall into our stabilization guarantee, like, we're going to provide stable semantic conventions there into stable telemetry.
things like, Gen AI, which is still very, new, I think is… Depends on when we get the stable… like, it may be something that may not fall into the scope of this stabilization, so… Yeah, just kind of a heads up on that.
Documentation and known limitations, so these are things that have existed in this issue beforehand, essentially just gaps that we wanted to try to shore up, before the actual release. This is just something that's kind of been building up.
And then, this lastness, or the last few, this correctness and stability bar, so one of the other things is, like, once we have the scope defined, so this idea of a support matrix.
I'm finding… Or auditing all of the issues that we have, or auditing any bugs that we can identify during that time period.
is, I think, important, and making sure that we find things that are… that need to be fixed, and then things that can be fixed after the fact. So, I think more to come on this one in the following weeks, but yeah, this is kind of, I think, like, the big triaging to make sure that we're actually addressing all of the things that we need to prior to stabilizing.
you know, keep in mind that V2 is always possible for this repo, it actually works really well, but, you know, we want to try to make sure we're starting on the right foot, I guess.
Validation release pipelines, so, essentially, this is just… making sure that we have everything… actually, I don't think… I think we're there on this one. It's just more about, like, the releasing RCs and that kind of stuff, need to be right. So, but yeah, I think this is actually pretty much done, believe it or not. We're pretty close on this one.
There's obviously things we can improve here, but I think from our binary standpoint and our container images, it looks good.
There's also a, proposed release candidate phase, there's… a little bit, you know, something to pay attention here is maybe just something about the RC, asking for… you know, I don't… I put down numbers here, not telling you, like, from on high what the solution is, but more just because I wanted to have, like, concrete steps here. If people have disagreements on any of these things, like.
that's… please comment on the issue, also, like, that's not… I'm not trying to tell you what things are, I'm just asking, but I'd rather it not be something where I put a question mark after every sentence, or, I put, like, X instead of 7 days, but… so… I definitely… think this is an interesting one, it may be too short, but essentially, having the RC open for a definite period of time, I put 7 days here, unless all maintainers agree to shorten it, Essentially meaning, like, if we're ready to go and everybody's already validated things, like, there's no real reason to say, like, let's hold up on this.
Unless people think that there is. So, yeah. I guess it's more just about… some sort of policy and some sort of procedure here. Please review this. It's not written in stone, it can be changed. So, yeah.
But other than that, I think that's pretty much at a high level where I've refactored this issue to be.
I definitely want to talk a little bit about, like, this scope, and this, support matrix in just a second, but I'll just pause here if there are other questions.
Nikola Grcevski @ Grafana / OpenTelemetry 00:28:07 Yeah, it's good work. A lot of stuff in here.
Tyler 00:28:10 Yeah, more than it was. It was kind of weak before. I think this is… this, in my mind, gives me… gives us a clear path to getting to, stability, so… Yeah.
Nikola Grcevski @ Grafana / OpenTelemetry 00:28:22 You know, thanks for doing this, this is amazing.
Tyler 00:28:25 Cool.
Okay, then let's… let's talk a little bit about this, the support matrix document. So… Yeah, that.
I can't forget that. Sorry, I'm trying to find the issue. Or, sorry, the PR, but I guess it's not well linked here.
Okay, so there's this support matrix, PR that I've opened, Stickle's already taken a look, Nimra's already taken a look.
And it essentially goes through… And it is defining the scope that we were just talking about, like, what is going to be included when somebody comes to us and they say, like, hey, you changed this thing, like, this is the thing that says, like, yeah, that was a part of our stability contract, or no, that wasn't a part of our stability contract.
So this is, I think, like, us being upfront with what we're going to do, and then doing what we say we're gonna do is the idea here.
So, from a high level, I've got release artifacts, these are things we talk about a lot, the binary of Obi itself, the Cates cache, just because it is something that we distribute, and then the container images, and then these are for Linux systems, and AMD64, and ARM64. Shouldn't be too odd there.
The runtime requirements, this is a little bit, maybe, we're talking about, so right now, like, we've got it documented, in the repo. This is something that we already have documented here, as, you know, kernel Linux 5.8, the Red Hat Enterprise Linux, we go a little lower, because we're able to support that, because they backported a lot of things in the BTPF, space.
Obviously, you need kernel capabilities for BTF, the CPU architectures are defined here, and then, Privileges, essentially just saying, like, what the requirements are to run this thing.
I did notice, though, that, like, upstream, like, on the main website, we, like, actually, say more here.
Around, like, particular distributions of, operating systems that I was like, oh, that's kind of interesting.
I don't know, at least we did, maybe… there we go, somewhere here.
Nikola Grcevski @ Grafana / OpenTelemetry 00:30:41 Requirements, yeah, yeah.
Tyler 00:30:42 Yeah, there it is.
Nikola Grcevski @ Grafana / OpenTelemetry 00:30:43 Alright.
Tyler 00:30:45 Yeah, so… I… I don't know… so the thing is, is, like, I think this is fine, honestly.
Well, I, I, I know this is fine, but, like.
I haven't tested a lot of this stuff, and a lot of this stuff is untested, and so I don't know if we want to… keep this, and try to make the support matrix include all of these things and start testing on these particular platforms.
Or, if we want to try to tone this back and keep the support contract that we already have in the support matrix and in the main repo.
Nikola Grcevski @ Grafana / OpenTelemetry 00:31:25 I like your support metrics better, because this talks about specific versions, and, you know, there's gonna be another version 10 of all my Linux, and then we'll forget to add it here, and people will be like, oh, it's not supported.
Tyler 00:31:36 Hmm.
Yeah, right, right.
Nikola Grcevski @ Grafana / OpenTelemetry 00:31:39 Right? I mean, it's… if we have nothing specific distro-wise, it's more like kernel and capabilities on the kernel.
Tyler 00:31:47 Yeah, right, and honestly, I don't think this is actually that great, because it's not, like, comprehensive, because, like, it doesn't say anything about Amazon Linux, right? Yes, exactly. Yeah, or, like, yeah, so… Yeah, I feel like just getting… cleaning this up and going back to that support matrix was my idea as well. I think it's a lot easier just to… To say that, yeah.
Nikola Grcevski @ Grafana / OpenTelemetry 00:32:07 Yeah.
Tyler 00:32:09 Okay.
Cool, alright. Then… If people have other thoughts on that, please let me know in the comments here. But otherwise.
Keep wanting to take a look at this.
So, validation coverage. So, this is the area that we're actually currently validating. I feel like this section may just get split, depending on if we can cover all of these things and just, by default, say that there's validation, but essentially, like, this is essentially saying what we test and what we're going to continue testing, our release artifacts, our cross-compilation, and the functionality in these particular, like, architectures, essentially, you know, with the VM integration, That's something that we're covering in the stability, meaning that we don't want to, like, get rid of this after we start releasing something stable. Mattia, go ahead.
Mattia Meleleo 00:32:55 Yeah, I was wondering, is there a way to… to point, maybe, to a kernel directory here, or to some CI jobs?
Because we should keep this in line, right? It's the kernels that we will, eventually hide or remove.
Tyler 00:33:15 Well, so that's… that's… The remove part is something we can't do, if it becomes stable.
But adding them, I think, is something that is something we could try to update this stock. Yeah, that's a good idea.
Mattia Meleleo 00:33:29 Okay.
Nikola Grcevski @ Grafana / OpenTelemetry 00:33:30 Yes, Mattia's asking is, can we make this point to the CI so that this doesn't get out of date?
Tyler 00:33:38 Yeah, yeah, we can. It can't be a dynamic… Lists, though, is the point I'm making, though.
I mean, I think there's nothing stopping us saying, like, here's a link to our CI where you can see the full coverage support, right?
Saying that we're testing on kernel 515.152, right?
like, that means that, like, if we go and we're like, well, okay, let's move on to, like, 6.1 or something like that at this point, like, we still need to be able to provide guarantees and validation that we're compatible with 515.152, is the idea.
Nikola Grcevski @ Grafana / OpenTelemetry 00:34:11 Gotcha.
Mattia Meleleo 00:34:13 kid.
Tyler 00:34:15 I… I mean, that's just gonna, like… and these numbers can change, like, so let's say, like, as the V1 comes up, like, we actually want to drop testing for this, like, that's fine, but whatever that minimum version is, like, that's the minimum version that we need to support for the V1 is the idea.
Nikola Grcevski @ Grafana / OpenTelemetry 00:34:32 Right. Okay.
Mattia Meleleo 00:34:33 Okay, clear.
Tyler 00:34:36 Yeah, and like, I… again, like, I… I'm happy to… to link to the CI directories for people that want to find more. Like, that makes sense, just as long as we understand that, like.
This is the… this is the thing that can't change, is the idea.
Nikola Grcevski @ Grafana / OpenTelemetry 00:34:51 That's the commitment we're making, yeah.
Tyler 00:34:52 Yeah, right, exactly, yeah.
Yeah.
But yeah, Batia, if you have other ideas on, like, a linking that kind of stuff, please go ahead and leave a comment or a suggestion here. I'm happy to… I'm happy to include it.
Mattia Meleleo 00:35:05 Yeah, I'll have a better look later.
Tyler 00:35:07 Okay, sounds good.
And then on Nimrod's, suggestion protocol, like, that we actually support, I think this is a great one. So this is essentially just a copy of the dev docs right now, but it's essentially committing us to saying, like, these are all the things that we are going to continue to support in a stable way going forward.
I just copied everything. I don't know if we want to, say we're committing these as a stable yet. You know, things like GenAI are pretty new. SQL++, I think, is kind of new.
But I don't think that we're gonna, like.
turn around and say, like, hey, let's drop this feature.
Nikola Grcevski @ Grafana / OpenTelemetry 00:35:44 What's that?
Tyler 00:35:44 So, yeah, I just included it, But yeah, again, go ahead, please review this, this is what we're gonna commit to. I'm guessing this is going to increase as we come closer to the date, and so this will need to be updated, but yeah, this is just where we're at right now.
Yeah, and so then next is talking specifically about the runtime, and services, with library interpretation, so runtime, or the service, so these are Go applications, Java applications, Node.js applications.
Python?
Which is exciting that we're doing that now. Ruby as well, and, NGINX. So the NGINX is a service that's a little bit out of ordering. I didn't know where else to put it, but I added it here. I've got minimum versions for all of these things. The Ruby and the NGINX, I've… got PRs to try to validate these. I looked back through the code, and this was originally the versions that we were testing. We've since moved on, but I've added backtests to test these things.
This NGINX is a pretty recent version. I'm, like… Based on, Nicola, what you've said, there's no way this is, like, the minimum version, but this is what I'm testing against, and this is what I found, so I… yeah, I'm just gonna go with that for now, but yeah. Go ahead, just ask me.
Giuseppe Ognibene | Coralogix 00:36:59 Yeah, sorry about the line, 82, I think we can add also the statistical matrix.
Tyler 00:37:08 I'm sorry, say that one more time?
Giuseppe Ognibene | Coralogix 00:37:09 Statistical methods, that's only, like, TCP, RTT, and, also adding TCP file connection.
I don't know if you… you want to add that, or… some that, Nikola Grcevski @ Grafana / OpenTelemetry 00:37:24 Yeah, we should probably add this stuff you've been working on. I mean, maybe you should review the PR and maybe add a suggestion.
Giuseppe Ognibene | Coralogix 00:37:30 Okay.
Nikola Grcevski @ Grafana / OpenTelemetry 00:37:30 Yeah, because… Is it a patient, yeah.
Tyler 00:37:34 That would be great, actually, I'd really appreciate that. That would be helpful, yeah.
Giuseppe Ognibene | Coralogix 00:37:39 Thank you.
Tyler 00:37:39 Yeah, I think all of the features that I haven't captured here, I'm happy we're reviewing them. I haven't omitted them because I don't think the feature's good. I just omitted them because I missed them. So, if you see things that I've missed, Please do, go ahead and, and Adam, yeah.
Okay, same here with Go. I tried my best to find these things.
I feel like this may actually change with some of the work that Nicola's doing as well, but, yeah, this is, I think, what I've found right now that we explicitly are… are working to support and testing against, so, I've included these versions here.
Nikola Grcevski @ Grafana / OpenTelemetry 00:38:19 Yeah, here's what I was thinking. I want to get the generic support working, and if I get it to work, we may actually reduce this list, because I want to keep the library instrumentations to minimum, only when we explicitly need them for, say, context propagation and stuff like that.
Or it cannot be possibly be done with the generic support. Otherwise, it's just more maintenance and offsets and all this stuff that we need to track.
So, potentially, before we go RC1 with 1.0, this release might reduce.
Tyler 00:38:52 That sounds great. I love that idea, reducing the ability, or what we have to support.
Did you want to leave this now, or remove this and then add it later?
Nikola Grcevski @ Grafana / OpenTelemetry 00:39:04 No, it's good as it is now, because I don't know if I'm actually gonna manage to pull it off. I mean, it looks promising, but I still have tests failing, I'm still debugging, trying to understand, what did I break and why.
But once I find that, and I have a clean CI, then we can… Okay, yeah.
Tyler 00:39:23 Alright, that sounds good. I guess we'll review this, obviously, before the V1, so we'll double-check then as well, but yeah, I guess after you're… you want to start removing that support, please go ahead and we can just edit this after there.
Okay.
Yeah, that sounds great. Next up, context propagation frameworks. This is, I think, what we are currently supporting, again, copied from the dev docs. This is something that was, mentioned by, Nimrod, so nothing too surprising here.
I'd love to see things like .NET and Rust on here, but this is the way the world is right now, so we'll see if we get there, yeah.
And then, last step, I put the GPU, instrumentation as well. I… this is just kind of like, we also have it, I don't see why we're gonna remove it, so I put this in as well here, but yeah.
Nikola Grcevski @ Grafana / OpenTelemetry 00:40:09 Yep.
Tyler 00:40:11 Cool. Yeah, so it looks like we've actually talked a little bit about a lot of things here. There's a lot more to talk about, so if you have things that you wanted to comment on here, please go ahead and do so. If you have things that are missing, please go ahead and do so. And if it looks good, please also just give me a thumbs up or an approval. That'd be great.
I think that was it for this one. I think we've actually talked a little bit about that.
Yeah, so that was all, all things I wanted to touch on. Perfect.
We are running out of time, so let's keep it going. Next up, I wanted to ask about Mattia, you, pointed out this PR and asked if we can get a patch release out. I'm guessing that's still the thing we were looking to do.
Nikola Grcevski @ Grafana / OpenTelemetry 00:40:51 Yeah, Matthias had to draw, he left a message, but I think, yes, we should probably do a release.
Okay.
Tyler 00:41:00 Yeah, that sounds good. I… actually don't have a good way to… look at what else has been merged, but I don't think there's been too much merged since the last release, so a patch release seems reasonable, like, there's no big features, right?
Nikola Grcevski @ Grafana / OpenTelemetry 00:41:16 Yeah, nothing… major, if my memory serves me well, because we just did 07 just a moment ago, right? I mean, last week or so.
Tyler 00:41:26 Yeah, yeah.
Yeah, it was last Friday, if I remember correctly. Yeah.
Yeah, right here.
Nikola Grcevski @ Grafana / OpenTelemetry 00:41:33 Cool.
Tyler 00:41:34 There's a… Nikola Grcevski @ Grafana / OpenTelemetry 00:41:35 Listen.
Tyler 00:41:35 et ceterization.
Nikola Grcevski @ Grafana / OpenTelemetry 00:41:36 That's fixed, that is a fix, and then… You made a fix for, Go, Go, Redis, so…
Tyler 00:41:46 Yeah. What, raphael, what about this export net NS functionality? Is this… Worthy of a feature, or a minor release?
Nikola Grcevski @ Grafana / OpenTelemetry 00:41:56 No, it was just a helper function exposed, right?
Rafael Roquetto 00:42:00 Yeah, yeah, yeah, it was just a helper function that got exposed, so I can use it elsewhere.
Tyler 00:42:05 Okay, cool.
Nikola Grcevski @ Grafana / OpenTelemetry 00:42:09 There's this semantic convention, a URL scheme label, That has a URL scheme, on Go where it was missing, but it's… you can consider this a fix as well, in my opinion, because it was there for non-Go, but we never made it happen for Go.
Tyler 00:42:30 I think you're right, yeah, I think that's a good idea.
And then… these are all docs or examples, nothing feature… yeah, okay, look, oops, good to me. Yeah, I think, The patch release sounds good.
Cool. Alright, I can… I can work on that later on today, actually, Cool.
Awesome.
Mateo will be so happy.
Cool. Next up, I just wanted to bring this to people's attention, a few things, just more announcements. I've got a blog post going out. Nimrod, has helped, iterate on this one, so it's both going out, but I'm also looking for other co-authors, if you would like to provide edits or other things here. It's essentially my goal from last time, since we talked about, the Obi project. Nicholas pointing out one of the things at KubeCon that was, like, just people are unaware of it, so trying to bring some of these cool features that we are getting merged and releasing out into more of a public space. So this is kind of the idea here, is just highlight something that went out in the V07. I think this is a really cool thing. Of course, it's always, like.
fun building demos for this, because you find out it's even cooler than you think it is. but yeah, so this is a demo for the header enrichments, meaning that, like, HTTP headers can come in and we can annotate spans with them.
This is great for a debugging tool. Obviously, OB doesn't touch your service, so you don't need to do any recompiles of your service. Turn it off, turn it back on again, whenever you need to. And it provides a lot of really great segmentation for finding, like, data as it's coming in, so a great debugging tool, as well as, like, incident response, so… Yeah, just a heads up on this, take a look, it talks about how to turn it on, it's got some great, images of traces, and just shows, essentially how to do that, but yeah.
The idea is it to go out on Friday if you, if you want to also… if you're into the social medias, I think that's great. I'm not, so, yeah. I'm looking for your help on that one.
Nikola Grcevski @ Grafana / OpenTelemetry 00:44:37 Sure, we'll post on LinkedIn and stuff, yeah.
Tyler 00:44:39 Yeah, perfect, perfect.
Also up, KubeCon North America, I did see the CFP open for this, super early, I think May is, when the… closes, yeah, May 31st, end of May. So, just a heads up, start thinking about this. It's, I think that's 8, 7 weeks away, or something like that. If you have ideas, if you want to talk to people about ideas, that kind of thing, just wanted to bring it to forefront of people's minds. I'd love to see more OB Talks, going to KubeCon.
the… I didn't actually look at the CFP for the observability days, but I imagine if it's not open, it'll be open very soon as well. So just a heads up on that one as well.
Okay, Next up, a super opaque thing that I added at the beginning, this OpenTelemetry Go, instrumentation project. So, we're getting to the point where, like, maintaining just the, dependencies is… is fine, I'm not saying anything… against that, it's just that we're running… we haven't done a release in so long that our support for Go 124 is blocking a lot of dependencies from being upgraded.
I guess this is a question, I hope Mike's still on the call. Yeah, I guess this is a question more for folks that are maintainers over there.
like, what we want to do. Do we want to try to get out a release to then unblock a lot of dependency updates there? I don't see much other, like, development going on over there, so I didn't know if we just want to, like, let things stagnate. I'm asking, I guess, more suggestions.
Mike Dame 00:46:09 Yeah, sorry, I, I think that… I mean, how hard would it be to at least just do a release there for now? I'm… I'm definitely still pursuing a lot of the, trying to take functionality from, that at least we were using out of Go Instrumentation, the whole kind of SDK approach, and seeing how that can fit into OBI.
But I… I do see a future where, at some point, that's kind of archived or stagnated.
But for the time being, I feel like if this is a blocker right now, we could probably push out a release.
Tyler 00:46:45 Okay. Yeah, let's… let's push out a release. I… I can take that out as an action item, unless you wanted to do that, Mike?
Mike Dame 00:46:52 Yeah, I can do it. Been a while since I've done anything over there.
Tyler 00:46:56 Okay.
Cool. Yeah, I mean, I think that would just help clean things up. It's just the security posture over there.
Mike Dame 00:47:05 Yeah.
Tyler 00:47:05 This would improve it a lot, so yeah, that sounds great.
Mike Dame 00:47:08 Anything that needs to be updated on that, or is, like, Dependabot all kept things up to date?
I guess.
Tyler 00:47:14 Yeah, Dependabot and Renovate are pretty good at keeping it up to date. There's definitely some things that, like.
the latest version of OTEL Go isn't upgradable, because it needs 125 for the Go version, so… so once the release goes out, we will have to update the minimum Go version over there as well. So, I guess we do need to make sure that's clear in this next release, that Go 124 is being deprecated in the process of the release, yeah.
Which is similar to what we did last release for the 123, yeah.
Mike Dame 00:47:43 I'll look at what we need over there, I might end up pinging you with some questions, but… sounds good.
Tyler 00:47:46 Yeah.
Yeah, perfect. Sounds good.
Okay, we definitely don't have time for this, I'll try to put this as an action item for next week, We did talk a little bit about, the next steps for stable, so that's a good one, but Florian, I want to prioritize this. You wanted to ask about the hotel specifications, so you asked for an update.
Florian Lehner 00:48:09 Yeah, as a big, quick, quick, background, the hotel specification SIG is also merged with the maintainer SIG, so it's… two, six, and ones, basically, happening every Tuesday. And, they introduced the concept of, getting an update on various projects, and OE was, was named off one of the projects that they are interested in to get an update.
And maybe someone from the group can join the call, and give an update, maybe a maintainer or approver, so, someone who has a bit more insights.
The idea is to get a more alignment, and maybe get also things unblocked from other, specification and, GoMain… Not Go Maintainer, auto maintainer, so that's a central point, and, yeah, they, they asked, if someone would be able to give a short update, maybe name some blockers, that the project runs into, so they could help, maybe, or get feedback on something, yeah. Just wanted to mention that, maybe OBE wants to give a quick update.
Nikola Grcevski @ Grafana / OpenTelemetry 00:49:22 Yeah, I can join. When is it? Do you know?
Florian Lehner 00:49:26 How's Tuesday and Wednesday.
Tyler 00:49:27 M.
Florian Lehner 00:49:28 Yeah, yep.
Tyler 00:49:29 Pacific time.
Nikola Grcevski @ Grafana / OpenTelemetry 00:49:31 Tuesday… Yeah, I can join. I don't have to move an internal meeting, but…
Florian Lehner 00:49:38 It's not like the OB update should be next time, but more like, hey, at some point in the future, that you can prepare or just watch.
Yep.
Tyler 00:49:50 Yeah, it's more you would sign up for it, Nikola, so it wouldn't be next Tuesday. It's almost certainly not going to be next Tuesday. And they're trying to… yeah, it's more of like a… They block off, like, a half hour, and they've been… giving full, like, discussions on particular sub-sigs of the specification, but now they're looking for, I think, more things other than that. Yeah, is the idea. So it would be essentially, like.
I honestly don't know where you'd sign up, that wasn't really clear from the last meeting. I think it's more just you ping the TC and say that you're willing to do that, and that they could ask you to then coordinate with them.
Which the TC, again, is a group, so I don't know how to ping the TC, but maybe in the maintainer's channel, I guess is the best place for that, yeah.
Nikola Grcevski @ Grafana / OpenTelemetry 00:50:34 Okay.
Tyler 00:50:37 But yeah, that'd be great, Nikola, if you're up for it, that'd be awesome, again, helping to popularize, Obi.
Yeah. Just for reference, people there don't know that we solved context propagation, so just keep things light, and yeah.
But yeah, cool, that'd be great. Thanks, Florian, for bringing that up. Nikola, yeah, thanks for, for, Representing the project.
Nikola Grcevski @ Grafana / OpenTelemetry 00:51:02 Yeah, thank you.
Tyler 00:51:05 Okay, Antonio, you wanted to talk next about network flow.
Antonio Jimenez 00:51:10 Yep, so there… there was a question from Stefan or Mario. Mario mentioned last meeting that, Next door flow could belong to not only one trace, that could belong to several, and we need to take some sort of decision if we are going to have duplicated spans, you know, through several traces, or we are going to have, like, a trace with a single span, if understood correctly, link it back to the application one.
Because I think Stephanie's on the call… Stephan, sorry. When you mention, like, having a separate span, you mean, like, that span will be unique in that trace? It will not be more spans over that trace, because how do you correlate? I mean, there is not… Any other thing you're right?
Stephen Lang 00:51:55 Yeah, no, so you're, your reply was… maybe… Trevor, you'd thought… you had thought further than I had.
With introducing the spam link, because I thought.
The spam link would have been, like, a quick way just to say if you had a completely separate span or set of spans to represent the network flow, then you could link many traces to that same Network trace by using a spam link.
But then you said, you know, what happens if there's multiple applications going over, you know, each flow? Then it kind of breaks apart, because you're not just linking to, to a single network trace, you know, then there's potentially many applications, so… No, it's, it's still kind of open to discussion from my side. It's not… it's not purely just solved by using spam links.
At least from the simplistic initial point of view that I'm always hoping for.
Antonio Jimenez 00:52:56 That's what I'm thinking. What's your opinion, Mario, also that you bring that topic?
Would it make sense to have, like, duplicated? I mean, I don't really understand… I'm good.
Mario Macias 00:53:07 Thank you.
Antonio Jimenez 00:53:07 phase where you have network flow through several traces, but I couldn't understand, like, from…
Mario Macias 00:53:15 I think since… they are… since they are different levels of abstraction, I think we can even have multiple… or either multiple trace IDs, bounded to a single flow, or even multiple flows, bounded to a single trace ID, because even during a trace, you… you can spam multiple, multiple connections in a distributed trace.
Yeah, I… I think now, just thinking in raw data.
I think it… we… we could do it, but… I'm afraid I might be missing something, since we are merging different layers of the network stack, from the application to the… to the… to the… to the network. I think we can add it as an experimental attribute and see what happens.
Mmm… Maybe we need to discover…
Antonio Jimenez 00:54:16 But altitude, I think that was mentioned also somewhere else, but I think that's quite… simple, because there will be way more metadata, and I think if we mix application metadata and network metadata, that will be confusing. I think what Nikola did for DNS, sorry, makes… it's similar here, like, we will support other technologies, like TCP, UDP, or, I don't know, you name it more.
would follow what Nikola did, right?
Nikola Grcevski @ Grafana / OpenTelemetry 00:54:43 Yeah, I think… I think… I know what you want. Yeah, I think we… we can do it. It's just, I guess we… So, correct me if I'm wrong, but what you want is to get the… the TCP spans, let's say if we talk TCP protocol, that happened during a transaction.
for example, we had a HTTP client call, you would like to get TCP information of each packet As it happened back and forth. Is that… the idea, or you would like them combined? I mean, I guess is my question.
So, you know.
Antonio Jimenez 00:55:25 Correct, it's… Nikola Grcevski @ Grafana / OpenTelemetry 00:55:26 It's fine.
Antonio Jimenez 00:55:27 It's extra information. I mean, what you did for the DNS actually describes that well. Like, you have your application flow, and then as part of your application flow, there are, like, DNS interactions, like, retry, reconnect, all those things are important to understand, because those things don't appear on the application side. As you mentioned, actually, on the conference.
If you're… the application, the duration takes, I don't know, 20 milliseconds, but in reality, it's taking way more. Where is that coming from? And you have… if you have that visibility, it's, like, totally a network layer that we are totally… unaware.
I think that is where the benefit came from.
Nikola Grcevski @ Grafana / OpenTelemetry 00:56:05 Yeah, I think I totally understand it, yeah. So, so essentially for us, what that would be is a new event that we're gonna have to ship, because right now, all the existing events we have try to combine. So, let's say, for example, you're doing a regular HTTP client call, so first thing happens is maybe you… maybe it's like a… with large body, so you have a lot of data to send, so that will get split over. Now, the current implementation for HTTP Client that Obi does will not actually, send all of those, but we will just keep on counting how many bytes, because we don't actually don't make any new event if it's sending upstream, the body of the request. Once it actually starts responding, we capture the response, and then we kind of watch as the new bytes are coming back, let's say it has a big response back, then it's responding with many, many requests. So, I guess for us, what we need to do here is that have a generic if this feature is enabled, generic event, that every time something like that happens, we ship an event saying, hey, we saw a TCP event, or we saw a new DP event happen, and we know the trace ID, And it's just a matter of creating spans. That's effectively what, Mario, I think… if I understand what Antonio wants, is… is that.
Mario Macias 00:57:29 Okay.
Nikola Grcevski @ Grafana / OpenTelemetry 00:57:30 It's like, for DNS, we did the same thing. Every packet coming through, we ship it, and then DNS just reports back and forth.
So this would require that, oh, you saw that for this particular HTTP event, you had to do, like, 10 packets upstream, and each one had, like.
I don't know, 4 kilobytes, let's say, for example. So you'll be able to see the network activity, and, you know, how much each one maybe, how many times it happened, or if there was a retry, that would be nice to have, kind of like, when Giuseppe's working with MTTR, and then, you know, like, you can kind of say, oh, this failed, and we retried the request, and so on, so… Yeah, yeah. I mean, yeah, we can do it. It's just a prioritization, yeah.
And we'll see if, yeah, some initial, maybe… we'll do some initial… Support and see if that's what you want, and then… We keep on iterating.
Antonio Jimenez 00:58:37 Awesome, so I'm gonna try to put the comment that we just discussed from the… on the comment into the ticket, and I will create, like, follow-up ticket, like, let's start simple with each… Nikola Grcevski @ Grafana / OpenTelemetry 00:58:47 Yeah.
Antonio Jimenez 00:58:47 ATCP, like, what is one of the most common, most likely, and then we can, see, like, connection retries.
Sending, all of those things.
Nikola Grcevski @ Grafana / OpenTelemetry 00:58:56 Yeah, I think you're… Yeah, I think what… I think the implementation should be… TCP, then UDP, then maybe other stuff. I think right now, because TCP won't… I'll do it for all TCP. It won't be just HTTP, so you'll see all TCP traffic coming through.
the UDP, then next, and then… I don't know what else we have… Probably not interesting. Unix sockets, this doesn't fall into that category. I don't think we track anything else than TCP and UDP at the moment.
I don't know what I don'.
Antonio Jimenez 00:59:32 I think that will be a huge improvement, honestly.
Nikola Grcevski @ Grafana / OpenTelemetry 00:59:34 Okay, alright.
Yeah.
Antonio Jimenez 00:59:37 Perfect, perfect, yep, I will create the ticket and put the information that we have discussed. Thank you, Tom.
Nikola Grcevski @ Grafana / OpenTelemetry 00:59:43 I'll try to do a POC and see what that looks like. Experimental, it will have to be explicitly enabled, because otherwise there's too much noise.
Antonio Jimenez 00:59:50 It is, yeah. It is.
Tyler 00:59:54 Okay, well, cool. Thanks for that discussion, the plan moving forward. We are right up, close at the end of the hour, so I think that's where we're gonna have to end it.
Yeah, thanks everyone for joining. Good to see you all. We will, see you all asynchronously in some of these issues if you have more to talk about. Otherwise, see you all next week.
Bye.
Rafael Roquetto 01:00:14 Yeah, right?
