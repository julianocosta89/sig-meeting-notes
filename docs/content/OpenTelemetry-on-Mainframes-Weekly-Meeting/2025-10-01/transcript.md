SIG: OpenTelemetry on Mainframes Weekly Meeting
Date: 2025-10-01
Duration: 31 minutes
Zoom Recording URL: https://zoom.us/rec/share/Zn1GnJrmMhj-HYEAITERXWVeltJtCOBQFPSjdGPCZW5iKPPYTW9KlEloD7rHmpTX.3sA99UlTLFP_GIv5
============================================================

## Zoom Recording Transcript

**Anand Somasundaram** 00:58 Hey, Jim, good afternoon.
**Jim Porell** 01:01 Hey, how are you?
**Anand Somasundaram** 01:02 I'm doing well, how about you?
**Jim Porell** 01:05 Can't complain, and…
**Anand Somasundaram** 01:07 Oh, I saw Morgan for a second.
**Jim Porell** 01:14 Oh…
**Anand Somasundaram** 01:16 Do you have access to IBM Slack?
**Jim Porell** 01:19 Yep.
**Anand Somasundaram** 01:20 Okay.
**Jim Porell** 01:22 Yeah, just hit me up on my IBM ID.
**Anand Somasundaram** 01:24 Okay.
**Jim Porell** 01:36 So, I saw Greg isn't coming, I'm just wondering about Rudiger.
**Anand Somasundaram** 01:45 Rodriguez was going to go to TechExchange, but that's next week, I guess.
**Ruediger Schulze (IBM)** 02:11 Hi there.
Hi, Jim. Hi, Antoine.
**Jim Porell** 02:17 Hey, Rigger.
**Ruediger Schulze (IBM)** 02:18 Morgan, so… Hey! Let's see what we got today.
**Jim Porell** 02:28 I know Greg's not coming, I saw his message on the channel.
**Ruediger Schulze (IBM)** 02:31 Okay.
So… 1st of October.
Just updating the meeting notes.
That's located? Okay.
So, what did we got? Let's look at the agenda from last week, just quickly to recap.
I think you had a good discussion on resources and entertainment… resources and entertainment, of course, I mean entities last week. One thing that I actually wanted to pick up is consider using projects in the SEMCON for APO.
I think this is a good one.
Because we also had these discussions around open… a couple of other issues or PRs in terms of… Making progress with the definitions.
Is there any… this is maybe a question to Morgan and Antoine, is there any restrictions on opening your own Project within these repositories. This is potentially a question to the… to the semantic convention SICK.
Opening our own repositories for mainframes? Proj… no project, .
**Morgan McLean** 04:18 Oh, like the GitHub projects for tracking work, I… I mean… Give them a heads up, but I don't think there's any restrictions around that.
**Ruediger Schulze (IBM)** 04:25 Okay.
**Morgan McLean** 04:26 Yeah. The only thing I could imagine is they might say they have a preference for, like, using a tag and sort of filtering their existing project tracker.
**Ruediger Schulze (IBM)** 04:33 Okay, yeah.
**Morgan McLean** 04:34 Neither would work, though.
**Ruediger Schulze (IBM)** 04:36 That makes sense.
**Morgan McLean** 04:36 In fact, the filter on their existing tracker might be preferable, because then they all see it, too.
**Ruediger Schulze (IBM)** 04:42 Yeah, okay, let me just take a note here.
That's good.
And as we touch on resources and entities, it's an awareness question. It's probably also something we need to ask to the semantic convention SIC.
Are you aware about any activities around representing virtualization?
I know that there's some activities and discussion around entities.
But maybe from a, you know, broader perspective, anything that you're aware about virtualization representation from an hotel perspective?
**Morgan McLean** 05:53 I don't know about ongoing activities. I simply might be out of the loop, though. I don't… I was trying to think. There are certainly some semantics that are defined around, like, hypervisors and things.
But I don't know if that's an area of active, like, people actively writing definitions.
**Ruediger Schulze (IBM)** 06:11 Okay.
Okay, good. Hi, Richard, thanks for joining.
Good. Then, Antoine, let's maybe move to the next one, which is the S390, Linux S390 support of the OpenTelemetry Collector.
And I had opened an issue, you had even commented there, let me get the number for that one.
**Antoine Toulme** 06:41 Yep, those are requested.
**Ruediger Schulze (IBM)** 06:44 Yeah.
Let me just open that one second.
So, this is… I think I had an issue open plus.
Right.
Oh, yeah, I think you commented on here, I could make it to the collector's sick today to discuss this. It's probably the best to join the collector call at the next occasion when it's possible, and discuss this.
Where's the… where's the sick…
**Antoine Toulme** 07:28 I would do it two ways, right? So… So there are multiple things that we can do in parallel. One is, yeah, we need to go to a collector sig. It's always good to have, you know, human contact and make sure we do this in some synchronous way. I believe there's already an issue open for,
**Ruediger Schulze (IBM)** 07:44 Yeah.
**Antoine Toulme** 07:45 mainframe support, we should try to… push that a bit harder. And the last item is the actual implementation of supporting this for infrastructure. So, I've been pretty close to the infrastructure of the OpenTeometry project, and I've seen multiple occasions where It would seem straightforward if, at least, we didn't have to sign TOS.
And, you know, terms of service type things. So that's when it gets a bit difficult.
Because you have to open a ticket with the Linux Foundation.
free to a particular use of a service, if it's not under some umbrella or some… some service use, or specifically, there's, like, some specific agreement that we need to sign or accept when we start to use a service. So I haven't heard back at all on, the request on… I think it was on the community repository where I opened the… the most important request is to add this GitHub application that you, pointed out.
Let me see…
**Ruediger Schulze (IBM)** 08:49 Yeah, it's, it's, 3018.
**Antoine Toulme** 08:53 That's correct.
**Ruediger Schulze (IBM)** 08:53 And, thank you.
**Antoine Toulme** 08:57 Looks like he's good to go, so he's done first part, we can do second part. So, we're not blocked, so… Let me… Let me see if I can just step to myself.
I might not be able to.
**Ruediger Schulze (IBM)** 09:12 Oh, it says I've installed the GitHub app.
I didn't proceed to step 2, hoping this can be done.
**Antoine Toulme** 09:21 Bro, you need to do something on your end.
**Ruediger Schulze (IBM)** 09:23 Yes, yeah, that's correct, let me… okay.
Right, okay, so this is… this looks good, I hadn't seen this yet.
**Antoine Toulme** 09:34 Meaning.
**Ruediger Schulze (IBM)** 09:34 Okay, very good. Yeah, we need to also get in… you know, once it's installed, there needs to be, again, an internal approval on our end to proceed. I can take that. Okay, that's good.
**Antoine Toulme** 09:46 moment to let me know that you've done the internal approval, we'll add a pull request against the collector repository to try out those GitHub runners.
**Ruediger Schulze (IBM)** 09:54 Yeah.
**Antoine Toulme** 09:55 And see if we're able to make them run. And then we can take it to the collector's SIG as a whole.
**Ruediger Schulze (IBM)** 10:00 Okay.
**Antoine Toulme** 10:01 They'll be very concrete for them, because they'll be able to see the PR running, and they'll understand the impact it has on CI, and well, one thing that may very well happen is that we run this once, and then we find out immediately a slew of issues, right?
**Ruediger Schulze (IBM)** 10:16 Yeah.
**Antoine Toulme** 10:16 or some issues related. In that case, what we'll do is we'll, instead of trying to go through the SIG right away, we can start to backfill a number of things that we see in the issues, so we can discuss that separately, and fix them before we go to approval.
**Ruediger Schulze (IBM)** 10:32 Right.
I'm gonna take notes.
Thanks, this is good, thanks for that.
Right. So this is, I think, the immediate items.
I also wanted to discuss, maybe generally a more proactive approach of Managing our work.
And this is not just semantic conventions, as we just said. We discussed here that we open a project within there.
repository, but there are other activities as well that… for instance, we had this survey which highlighted that there is an interest in the SDKs for at least Java and Python on COS, and we have the same discussion also for Linux on C.
I was wondering if to at least document that this work exists, and that we would like to drive this forward, if we should not should go ahead and as well, open issues in the respective repositories.
That obviously, you know, also to the platform specifics, will then require, you know, ways to figure out how to support that, and also to find volunteers to do that.
But, I think this would help us to also illustrate and maybe get… gain some attention on these activities that we want to drive in addition to the semantic conventions.
I wanted to bring this up as a discussion point.
Any thoughts around that?
**Morgan McLean** 12:58 I missed the first half of that Rudiger, like, what was the…
**Ruediger Schulze (IBM)** 13:01 Okay, I wanted to ask about or discuss a little bit the way of how we are operating as a SIC. So, we have semantic conventions, obviously.
And dare we say, it is probably the best to open a project and manage issues and, you know, work under this in the context of the semantic convention SIC. Now.
In terms of also other activities, like porting activities of SDKs.
This is something that we have on the agenda, but… Yeah.
**Morgan McLean** 13:35 It's one we haven't talked about a whole lot. Right, but we, you know, if we don't reflect those.
**Ruediger Schulze (IBM)** 13:40 you know, in the other repositories and the language SDK repositories, probably we will not get any traction on this sometime soon.
Now, if you think about…
**Morgan McLean** 13:51 Put it on the radar.
**Ruediger Schulze (IBM)** 13:52 Yeah, and there are dependencies, obviously, like we just discussed for the collector, right? You need to have a runner to do some of this work.
**Morgan McLean** 14:00 Yep.
**Ruediger Schulze (IBM)** 14:01 But I was thinking, actually, we may open the issues to reflect them.
And maybe they get some attention in some way, or at least we can figure out how to approach this, so that over time, we get a perspective of what is needed for which type of SDK, for instance. Some of this is maybe more straightforward, for others, this might be more complicated.
If you think about compiling on the platform and, you know, resolving dependencies and so on.
But, I would actually propose we We open issues in these repositories to document the work that is there, and also get some feedback.
**Morgan McLean** 14:45 Yeah. I'm trying to think the best way to approach it, like, I presume, Rudiger, and remember, I'm not a mainframe person, there's probably a subset of OpenTelemetry-supported languages that are typically used on mainframes? Is that…
**Ruediger Schulze (IBM)** 14:59 That's correct. Yeah, that's accurate.
**Morgan McLean** 15:02 So, I guess what I suggest is, like, We've put together.
not even necessarily a plan yet, but, like, a basic sort of paragraph describing which SDKs we think are in scope for this.
and the types of things they would need to do. Certainly one of those things would be adopt the new mainframe semantic conventions. Certainly another would be to take certain actions to ensure that their SDKs actually work properly for mainframe applications and can capture and export the right data.
From there, we probably reach out to the maintainers of those SDKs directly, just to give them a heads up.
And then we make this sort of a official… thing within OpenSelemetry and part of the specification.
**Ruediger Schulze (IBM)** 15:47 Yeah.
**Richard Nikula** 15:50 But for Java, we don't really need anything, but… Because that one's sort of… they're writing Java, they can…
**Morgan McLean** 16:00 Yeah.
**Richard Nikula** 16:01 API to do that, but for everything else that… Where that's actual code, they do need something.
**Morgan McLean** 16:07 Yeah, and that's sort of my question is, is, so instrumentation, open telemetry is usually… there's sort of two options, right? So, if I deploy an app on Linux.
I can either instrument it with an SDK, or I can, if it's a Java app, I can deploy, or most other languages I can deploy, say, the Java agent that can instrument it instead of the SDK, or in conjunction with the SDK.
I'm guessing… That on mainframes, there's… probably less appetite for, or there's blockers in the way for automatic instrumentation? Is that accurate?
**Ruediger Schulze (IBM)** 16:42 I think in Java, in case of Java, I would probably say probably not. You want to start with auto-instrumentation.
**Morgan McLean** 16:49 Okay. Okay, so it is feasible. Yeah.
**Richard Nikula** 16:51 Beautiful.
**Morgan McLean** 16:52 Okay, so in that case, then, we should actually pull this up a level from SDK, so we're really just talking about instrumentation.
And then, so for the target languages, we'll want to work with the language maintainers, or just give them the right requirements, so that they can build a plan for both the SDKs and for automatic instrumentation. SDK is usually pretty trivial, because as long as the person's code runs, I mean, we don't tend to pull in that many dependencies, the SDK tends to work.
And so, in terms of testing, it's really just making sure the exporters and things like that work. For capabilities, it's probably just adding the right semantic conventions for mainframes, those SDKs. That's pretty trivial.
**Richard Nikula** 17:31 I think the one thing is that GRPC… Dependencies are hard to…
**Morgan McLean** 17:38 Right, okay.
**Richard Nikula** 17:39 mainframe code, right?
**Morgan McLean** 17:41 And is that because gRPC has dependencies that just won't work on mainframes at all?
**Richard Nikula** 17:45 Yes.
**Morgan McLean** 17:46 Got it. So, like, fortunately, OTLP also is the HTTP version, but it might mean then… what I'm hearing from that is, like.
I mean, either we go into gRPC and fix all the mainframe dependencies, which doesn't sound likely, or we just ensure that there's a way that people can deploy the SDK without those dependencies for gRPC coming along, and, you know, they just don't… they're not able to use gRPC in that context.
This all… for the SDKs, this all seems pretty simple and straightforward. It's for automatic instrumentation, where I'm guessing running in a mainframe environment will add constraints that need, you know, various code changes and things, within automatic instrumentation to work around.
**Ruediger Schulze (IBM)** 18:30 I think it depends on… I think for Java, we are good.
**Morgan McLean** 18:35 Really? Okay.
**Ruediger Schulze (IBM)** 18:37 for Java, I'm actually… so, there are examples that actually instrumentation for Java works on CUS, so… Amazing. If you think about Liberty as an observer.
**Morgan McLean** 18:50 You… you can use their…
**Ruediger Schulze (IBM)** 18:53 There's the telemetry micro-profile, which is supporting open telemetry.
**Morgan McLean** 19:00 Yep.
**Ruediger Schulze (IBM)** 19:00 And then there's also a possibility to run with the Java agent itself, so that's, as well as a ported scenario. So, I think Java is actually… there's more, probably, this aspect of… From a community point of view, also validating, you know.
It's just… it's a… it's an SDK that generally works for… for CS or for Linux RNC.
**Morgan McLean** 19:29 Okay.
**Ruediger Schulze (IBM)** 19:29 And, There is… what Richard was just saying, right? So, take the C++ SDK. There are these dependencies which probably are hard to resolve, at least on the COS side.
when it comes to the gRPC libraries and getting those compiled, this code, and really being ported over to the platform.
But, on the other hand, So this survey, for instance, that showed us that there's an interest in Java and Python. Python, by the way, might also work well. I haven't really looked at Python on COS and OTel yet.
But, if you think about these other languages, like C++, then there are some use cases, obviously.
By the way, one question that I occasionally get, maybe this is something to very briefly discuss.
From a hotel perspective, there is no C.
SDK.
**Morgan McLean** 20:34 There's just C++, that's correct.
**Ruediger Schulze (IBM)** 20:35 Yeah, right. Do you know why the community so far just went for C++ and not C?
**Morgan McLean** 20:42 I don't know for certain, I… because I haven't been close to that SIG in several years. I think it is… it has some compatibility layer for PureC, but my main guess would be… C++ is not commonly used in backend services on VMs and Kubernetes. Like, I know Google uses a lot of C++, but outside of there, it's not.
The most popular language for distributed systems.
And so it was historic… it was not even an original language in OpenTelemetry was added, like, that process only kicked off, like, probably 2 years into the project's history.
I'm guessing the demand for pure C application instrumentation running on Kubernetes or VMs is relatively low.
**Ruediger Schulze (IBM)** 21:30 I see. Okay.
**Morgan McLean** 21:32 Like, and I say this, like, yes, I know the Linux kernel and various embedded systems, I mean, C was the first programming language I learned, and I still know it relatively well, but, like, it's… for the use cases that OpenTelemetry has historically focused on, it wasn't as relevant.
I do know that OpenTelemetry is now being used more and more in embedded systems. I don't know for those whether they're just using the C++ SDK, because I believe it has C bindings.
Or if just a lot of the embedded systems are not… you know, the ones that happen to use OTEL are just not using C as much.
**Ruediger Schulze (IBM)** 22:04 Or think about, let's call them the traditional systems, but they also get more and more these requirements to adopt open telemetry, and if you want to do this in a built-in way.
**Morgan McLean** 22:15 You need to have C support, yeah.
**Ruediger Schulze (IBM)** 22:17 Yeah, you…
**Morgan McLean** 22:18 Well, here's a perfect example in that I haven't seen the code, but, like, for two and a half years, a lot of the Microsoft contributors have been talking about how the Windows kernel includes geometry within it, so that Microsoft can gather this sort of performance data about customers' battery consumption things to try and better tune the operating system. Linux is written in C, and so unless our C bindings are absolutely magnificent, I don't, like, I don't even know. If you want to do the same project for, like, the Linux kernel, I don't even know if it would be feasible.
**Ruediger Schulze (IBM)** 22:45 Okay.
**Jim Porell** 22:47 I'm also thinking, too, is that… on Z, at least COS, not ZLinux.
most of the stuff is going to be done by transaction programs that you're going to want to instrument, and I think the subsystems themselves are going to provide that instrumentation. I'm guessing maybe there's 10 customers in the world, high-end finance, that might want to use an SDK, and they'll figure out how to use it.
**Morgan McLean** 23:10 what the languages you have. Yeah.
**Jim Porell** 23:12 Otherwise, you know, I am…
**Morgan McLean** 23:16 You probably just want to trace those high-level transactions rather than going into the code, but that sort of… that follows the way a lot of people use OpenTelemetry today.
**Jim Porell** 23:25 Right.
**Richard Nikula** 23:26 Although, it's interesting, because I was actually on a call today with a large financial institution, and one of their people was, in fact, using the SDKs to instrument some of their own custom interfaces, right? Which is exactly what you would expect, right?
**Morgan McLean** 23:45 Was it Wells Fargo?
**Richard Nikula** 23:47 I couldn't say.
**Morgan McLean** 23:49 Okay. I don't know why I called them out by name, I know most of the major banks at this point are using OTEL pretty deeply, so, yeah.
**Ruediger Schulze (IBM)** 23:58 Okay, good. Yeah, so why we look at semantic convention, let's not, you know, forget about the SDKs, because this obviously has been a topic at a couple of discussions in the last… Couple of weeks.
Right. In terms of semantic conventions, there, I think there's still a to-do on me to get progress with our PR. There were a couple of comments. I simply was booked with other activities recently, but I will come back to this.
And as we discussed metrics, we had an internal discussion around the entities, and I think the essence of this discussion is open PRs with the community and discuss what we need from a mainframe point of view.
And we have a conference next week, so I will be busy then the next week, but effectively, I would like to drive this forward then after this conference.
And I think this would help to… you know, get to specific results on this, and that's why also my question earlier on, you know, where we are with virtualization, I think this directly plays into it. If you think about the mainframe… There's, you know.
different, you know, layers of virtualization, obviously. Think about LPAR, or think about, then, also, browser representations through virtual machines.
And if we want to capture metrics for these different virtualization layers, then we need to have an understanding what the entities are and how to describe them. And this is one of the activities. And also, I think we touched on this on the previous meeting here, the… It's this question of then how to describe things like that you have different… processor types, for instance, on the mainframe. I think we can do a lot of guessing, but I think we need to open the PRs and get feedback on that, that what's the best approach is to do that. So, I would see this as one of the next steps in terms of semantic conventions, too.
Get this done.
**Antoine Toulme** 26:12 Yeah, it's a challenge.
This is where your expertise in mainframes is really important, because, frankly, I don't know what people would be looking for.
We just had the same discussion this morning on Kubernetes, semantic conventions. It's also a challenge.
And I would say, just to help maybe present about it, is one of the really useful properties of entities is that you can create relationships between them.
So, has one, has many. Think of it as a good old class diagram, right? If there is a way for you to think about it this way, then you're probably on your way to have a good shot at representing an entity.
I don't know how deep you want to go, and this is… this needs to be coupled with use cases still, right? So, having, let's say, a representation of, a CPU allocation or something like that, that might not actually be useful if there's no use cases with that. I don't know what, With the format of, like, again, like, we're talking about It's directly talking straight to your expertise, but, you know, if, If there's a notion of account, or a notion of a tenant, or something like that, that would be best represented as an entity, how would you go about it, and… Yeah, I'm talking out of my depth. I… for communities to talk about something I'm more familiar with, right, we have this notion of containers that are inside pods, that are inside, like, related to a deployment. Deployments may be working with a replica set.
All of that, they have a, horizontal pod autoscaling policy. All those things are kind of loosely related as objects. You want to be able to navigate from one to the other, so you can find your way into that system.
So…
**Ruediger Schulze (IBM)** 28:01 Yeah, right, and Antoine, actually, this is the discussion that we also started here on the SIG, so we have been also in contact with the entity SICK to get an understanding where they are.
current… I think my current understanding is that relationships is still to be done, but it's one of the interesting aspects also for us to think about.
in similar ways, like you just described it, right? You have a…
**Antoine Toulme** 28:29 You have a.
**Ruediger Schulze (IBM)** 28:31 a CUS subsystem, which is a transaction processing system, to have full-stack visibility, you need to understand, okay, this is running on an LPAR, this is maybe running on a certain CAC, but from this, the way how the mainframe works, there can be actually In certain scenarios, then also… constraints derive, so you want to understand, you want to have a full visibility, not just only on the application layer or on the middleware layer, otherwise you also need to understand what the underlying infrastructure is.
And a typical question, for instance, is.
As we have these different virtualization layers, is how much, you know, physical capacity is this, actually, that is behind these virtual resources that you have.
And, that's something that, you know, there needs to be ways of being able to express this.
The current view that we have is we start from the bottom to build this up, because, if you think about, you know, I just said processor types.
And utilizations on those, you know, then, you know, once we have laid out the basis from the platform perspective, then we can take this up and also understand where the common principles are. Obviously, the idea is to do this as you know… Where there's no need to define new metrics, new names, new attributes, then, you know, we should go with what is common, obviously, but… We would have to understand of how to fit some of these concepts into it.
**Antoine Toulme** 30:17 Okay, yeah, let's just…
**Ruediger Schulze (IBM)** 30:19 Yeah, true.
Okay, last topic, yeah, thanks, Antoine. Last topic, Richard, next week, I think we see us at… on Monday, right?
**Richard Nikula** 30:34 Yep.
**Ruediger Schulze (IBM)** 30:35 Okay, very good.
**Richard Nikula** 30:36 Afternoon.
**Ruediger Schulze (IBM)** 30:37 Yeah, yeah, very good.
Saying that, so, Obviously, I will be at the conference next week, Richard as well. Maybe, Morgan, we skip next week, and then we meet in 2 weeks.
**Morgan McLean** 30:55 I can remove it from the calendar.
**Ruediger Schulze (IBM)** 30:57 Yep.
**Morgan McLean** 30:58 All good. Alrighty.
**Ruediger Schulze (IBM)** 31:00 Okay, yeah, thank you.
**Morgan McLean** 31:02 See ya.
