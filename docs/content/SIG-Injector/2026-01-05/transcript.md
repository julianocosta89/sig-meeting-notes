SIG: SIG Injector
Date: 2026-01-05
Duration: 47 minutes
Zoom Recording URL: https://zoom.us/rec/share/qC7h2PcYJEFtl9dWKfPIh2bfE80Fd9w3q5PyOEWCYCOOw6-YU-ihOJlDWWzejnFl.YYg7qqVrUVcw34Ij
============================================================

## Zoom Recording Transcript

**atoulme** 02:00 Hey, Monty.
**Ted Young** 02:03 Hello, hello!
**atoulme** 02:05 Happy New Year.
**Bastian Krol** 02:06 Hello, hello, Happy New Year!
**Ted Young** 02:08 New Year, welcome back. Y'all had a good break.
**Bastian Krol** 02:13 Yeah.
**atoulme** 02:14 Brain break.
I saw you had a… A little bit of a thing happen as well, right? You got your movie out.
**Ted Young** 02:24 Yes! Yeah, I finally was able.
**Bastian Krol** 02:27 movie?
**Ted Young** 02:28 On the internet. Yeah, I made a short film At this point, it's like… we filmed it, like, 2 years ago, actually, but it was in a festival circuit.
This whole time, and there's… most of the festivals have rules, you can't have it publicly available on the internet while that's going on, so it just doesn'.
**atoulme** 02:45 Brilliant.
**Ted Young** 02:46 It just, like, took forever for that, which was great, it was great it had a festival run, but it… I've been, like, sitting on this thing forever, so I was glad to finally be able to release it.
**Bastian Krol** 02:56 Cool stuff. But that's got nothing to do with tech or optimism, it's just completely different, okay? What kind of movies do you…
**Ted Young** 03:07 I got my start, actually, in animation and visual effects, and, you know.
Maybe animation, so it's technically computers, but… More recently, like.
you know, around when, like, LightStep got acquired, I was like, Alright, I need a hobby.
But I didn't want to get into it. I didn't want to get back into animation, because it's just, like, I don't want my hobby to be, like, glued to a computer. You know what I mean?
**Bastian Krol** 03:36 Yeah.
**Ted Young** 03:36 that's, like, go outside and meet people and, like, have an excuse to interact with cool artists and stuff, so… I was like, why don't.
**Bastian Krol** 03:43 We tried.
**Ted Young** 03:44 Some live-action movies.
**atoulme** 03:47 Nice, that's okay.
**Ted Young** 03:49 Awesome. Just a hobby.
**atoulme** 03:51 Well, that's cool. Yeah.
**Ted Young** 03:56 Nothing related to OpenTelemetry.
No. No open telemetry was used during the making of…
**atoulme** 04:05 That's a real honey. That's good.
**Ted Young** 04:07 Yeah.
**atoulme** 04:10 Okay.
**Ted Young** 04:11 Anyways…
**atoulme** 04:15 I'm just gonna, I only wanted to talk about one thing today, I don't really have anything, I know… You've been putting a lot of work into the next chapter, it looks like everything landed.
It should be riddies?
I can help with that.
**Bastian Krol** 04:31 Release, release, release, right. I remember vaguely, I did a release, but that was before Before we landed all those changes. Yeah, we probably should do a release. So, what I'm currently working on, and I think maybe I would like to do that first, is to… fix our… GitHub Actions a little bit, and I really would like to automate the release flow. Right now, the release flow is… it creates a PR automatically, once that is merged, you can create a tag, and then you build artifacts on your local machine and upload them to the GitHub release, and I'm not a fan of that, exactly.
**atoulme** 05:18 Okay, yeah, you wanna do… you should… okay, that's fair. So…
**Bastian Krol** 05:23 Yeah, so I would like to automate that first, and actually build the, artifacts, like the dev package and the, and the binary, first and foremost, on GitHub Actions, and then use that in the release.
**atoulme** 05:41 Alright, that's something that we, you know, I can help with, or… someone else. Doesn't have to be a Zeek specialist to do that.
**Bastian Krol** 05:48 No, sure, I mean, if somebody else wants to pick that up somewhat soon, then I'm all for it.
But, I think at this point… so, because I would really like to… You see at least the binary that we produce here in this project.
in our dash zero operator. So far, we still have a basically a fork, or this codebase is now a fork of our injector, however you want to phrase it, and I would like to consolidate that, and actually roll out the injector binary that we produce here to all our customers. That would also give it.
**atoulme** 06:37 Yep.
**Bastian Krol** 06:37 directly infinitely more usage than it has seen so far, because I think it has been zero actual production usage, and that would just roll it out to our few hundred customers, and yeah, that would be also a nice validation, but I'm not doing that with a release that anybody has built on the local machine, that's just… yeah.
**atoulme** 07:03 Well, that's definitely not fair. So, I'm in the same boat, for what it's worth, right? We… we need to update, to the latest, and we have not, You have done a lot of changes recently, so it's also warranting a little bit of a testing and…
**Bastian Krol** 07:19 Yeah.
**atoulme** 07:19 But, yeah, that's… we need to do it.
Cool.
**Bastian Krol** 07:24 Did you… have you used any of the stuff since the initial… the Zero Zik-based Draw…
**atoulme** 07:34 No, we didn't get to it. To be clear. We have been very busy, and we did not get a chance to do it.
**Bastian Krol** 07:39 Okay, yep.
**atoulme** 07:40 So, that's… that's on me to do that.
The stuff that has been most interesting for us, it's kind of a surprise for me, did not see it coming, is the work with Obi, right? So, I was not involved that much into Obi, and I went to KubeCon, I sat down for a talk by one of my colleagues.
And the guy goes, hey, we have found a new way to instrument using UVBF. I'm like, wait, what? What is this? So, what we're doing right now is we're, we've had a couple of those interactions now, right? At this SIG meeting even, where we had Obi folks come and say, well, here's the way it behaves, and it's slightly different from what you can do with the injector. And I think, about a month ago, I said, well, I think we should write a blog post, because if I'm confused, then I can guarantee a lot of people are confused. Yeah.
Let's talk more, not less, about this, and how we're going to play together. And that's on my… Task list of things to do.
So, that's, that's coming up.
But yeah, besides that, and having a good release, that'd be great. The other thing is, Obi does not have a good installation story itself, and I think we need to harmonize that, and I'm sure Jack and others, they're just going to… you know, bang that drum a lot harder about that type of, things that we need to do, but let's separate those things. Just first, let's say how they play nicely together, and how Obi is actually pretty good about finding out that there is something running so that they don't override or double publish what you already do with the injector, and how the injector is a better thing for SDKs, because SDKs have more granularity and do A lot better in terms of detection and stuff.
**Bastian Krol** 09:23 Yep.
**Jack Berg** 09:24 Are you all following the, there's a proposal from a person, Ivo, from Datadog, who, is proposing sort of an OTAP about, Resource sharing between processes?
**atoulme** 09:41 Like, so basically, what he wants is he wants for profiling.
**Jack Berg** 09:45 profiling purposes, he wants an eBPF profile to be able to access resource information from SDKs in a shared memory location.
So that he can make sure that profiling information is a consistent resource as, like, what is being emitted from the SDK. Doesn't that sound familiar with what we're talking about with OBI?
Right? Like, OBI wants to, like, emit, like, potentially supplemental Or potentially, I don't know, double counting, it depends on the context, information as what the SDKs emit, and we want to make these things work together, so OBI could benefit from accessing the same resource as what the SDKs are emitting.
**atoulme** 10:30 Yeah, okay. I… Yeah, I think that's… that's very close, but it's good to have standardization anyway. So, yeah, I'm…
**Bastian Krol** 10:39 have a link to that discussion somewhere handy, because I…
**Jack Berg** 10:42 I'll pull it up and put it in the notes.
**atoulme** 10:44 Thanks.
**Bastian Krol** 10:45 length.
**Ted Young** 10:47 And just a note, you know, something we determined from our prior discussions is that it's not even, like, how does Obi and the injector play nicely, because by the time Obi shows up.
it doesn't really matter whether the injector was used, it's, like, same, same, whether they manually installed the SDK, or used the injector, or what. And so it was more a question of, like.
If you're using the SDK, is there a reason to also be using Obi in the same process? Right.
Just subtle distinction, it's just, like, it doesn't matter how the SDK was installed. Is there a reason to use both at the same time? It seems like there might be, and if there is, like, yeah, how do we, like, make sure that.
**Bastian Krol** 11:28 Yeah.
The only aspect that is maybe related more to the injector than to using the SDKs manually, with something like the injector, you usually just roll out SDKs slightly blindly to a whole infrastructure landscape, and you are maybe not aware that OB is doing things somewhere, or vice versa, so if you install one process manually, then you… it's a more targeted action. But technically, of course, there's no difference, just from…
**Jack Berg** 12:03 I mean, OB9 could do something really naive and say, like, hey.
like, assuming this OTAP about resource sharing from SDKs manifests and becomes, like, a thing, like, OBI could have a policy that says, like, hey, when I'm considering instrumenting a process.
Check if it is exposing information about the resource. If it has a resource, don't instrument it.
**atoulme** 12:25 If it doesn't have a resource, instrument it.
**Jack Berg** 12:27 That's, like, the naive, simplest approach.
**Ted Young** 12:31 it already has a way of detecting whether an SDK is already running, but I don't think it… what I think is missing is that second piece you were mentioning, right? Like, it can detect it's running, but it can't ask it for any of the information it was loaded up with. It could… it could scrape environment variables and, like, hunt around and make a guess, but it doesn't have a way of saying, like, hey, SDK, like, tell me… like, give… give me… give me an API so I can interrogate you about stuff.
**Jack Berg** 12:58 Well, that's a good start, that it can at least detect that an SDK is running.
**Ted Young** 13:02 We can do that right now. Okay.
**Jack Berg** 13:04 Looks good.
**Ted Young** 13:04 And avoid double, like, double instrumenting.
**atoulme** 13:08 Yeah.
**Ted Young** 13:09 But I don't think it could… it could lift the resources or do something like that. It could… It could guess at where those were coming from and go grab them. That's the only thing it could do right now. It could guess at where the config file is, or look at the environment variables.
**atoulme** 13:26 Okay, sorry, I took us into this discussion, but just so you know, this is something that's on my mind. I think you're right that we need to narrow down the focus. It's not even about Injector at all, it's just instrumentation and OB. How do they play together? How do we make sure that we have a script message that we can explain in 2-3 sentences?
how things work, so that we reduce the level of confusion, because if… if we were to make a release of the injector right now, I know what the first comment's gonna be. Like, oh, how does that work with Obi? Oh, does that have obby in it? Or, I mean, scam.
**Ted Young** 13:59 Yeah.
**atoulme** 14:01 Just to organize.
**Ted Young** 14:03 we… I think something OpenTelemet… this is outside the bounds of this SIG, but something OpenTelemetry needs to do is kind of just… for the languages we can't use the injector for, Go being the number one language, like… blessing some other approach, whether it's OB or, you know, compile time set, like… I would be in favor of Obi for that, because it seems… like, better than a compile time approach in terms of what we're trying to provide for people, which is a way for an operator to stand all this stuff up without needing to, like, bother the application teams. And the problem with the compile time approach is you have to go bother the application teams to recompile all their stuff.
So, again, that's not the injector, but it would be great for OpenTelemetry to, like, figure that out so that we can have a more coherent installation story, which is what I would like us to be a part of. It's like, there's a new installation story that we want everyone to start following?
And you're gonna see some resistance, I think, from some people saying that the injector, Obi, all these things are, like, nice.
way to, like, bootstrap, but this is not the proper way. Like, the proper way… this is, like, a crutch you should use for a little bit, but the proper way is to, like, do it all. We're gonna encounter, like, a bit of that, so I actually think that's the area Where we need to evangelize and do more, like, political work to just convince people, like.
To come along with a new narrative about, like, the standard way of doing this, and this isn't… this isn't, like, a crutch that you should try to get rid of later.
**atoulme** 15:47 So I actually had this feedback from… when we did the first zero config stuff, there was C, naive, right? That was the first donation to this injector project. That's exactly the feedback we got. It's like, he probably can't actually run this in prod, right? We wouldn't do that.
You're just going to use it for discovery, and then you'll come back and tell us what you need to implement, and we'll do a really good job afterwards. Yeah, no, people just took this, ran with it, implemented it in prod, ran it on thousands of machines, and they were happy, and then they…
**Ted Young** 16:16 Yeah.
**atoulme** 16:16 Right? And it's, the people misunderstand how more important it is to have something that works the first time and is easy to install, compared to having a pure academic approach to doing things right.
Yep.
**Ted Young** 16:31 I think we'll get there, but I do think that we'll require a little bit of, like, human cultural… convincing.
**atoulme** 16:38 From who? From maintainers, or from users?
**Ted Young** 16:42 Both, both. More maintain… this is what I've noticed, is that our community is a lot of, like, practitioners.
**atoulme** 16:49 And…
**Ted Young** 16:50 And there's a lot of, like, Google DNA.
The Google DNA in particular takes the stance that there's no… like, all this automated stuff is, like, too much overhead, and you should manually instrument everything, and it's not really, like, that much work. That's kind of a historical attitude that came out of the big box codes.
Right? But that's because labor is cheap there, right? Like, for end users, right, the vendors haven't been pushing this stuff as much, so I think it's more having, I think, vendors come in and say, like, look, y'all, we've been doing APM this way for centuries at this point, like… This isn't weird.
Like, this isn't even a new idea, this is just, like, how this stuff works. Please believe us that, like…
**atoulme** 17:37 This is an installation story that users need, and we know this.
Okay, now that makes sense. Thank you.
**Ted Young** 17:50 I had to convince people we needed a Java agent at the very beginning.
Like, an agent? Why do you need that? I was like, are you kidding?
But that was many years ago.
**atoulme** 18:01 It's… is it before Neurotic kind of popped in on the radar, or was it Neuridic very popular back then?
**Ted Young** 18:06 They were… they were popular, but this was, like, getting its start from the tracing point of view, right? And in distributed tracing, it was more Zipkin and these other things that didn't have an agent, really. Anyway… anyways.
**atoulme** 18:21 Thank you.
**Ted Young** 18:22 It was more like an attitude that was different inside of Google and Microsoft compared to…
**atoulme** 18:28 End users, right?
From my discussions at CapeCon, I would say that this time has passed, even for them.
that there is a consideration for resources that is really compressed across everybody in the landscape at this point. No one has escaped this. Yeah. It's no longer, like, you cannot just have one more guy in the team who's going to just recompile the code in the right way, according to some framework.
It's awful.
**Ted Young** 18:52 I've just noticed that if you work at an APM company, right, you're very used to LD preload and all of this stuff. This is all just, like, another Tuesday as far as, like, using this stuff. But for whatever reason, everyone else is, like, sees this as kind of, like, black magic, and I've… even within Grafana.
from people who come from an infrastructure, I notice a reflexive… Like, well, that isn't safe to do. You wouldn't really do that. And so I think we just need to socialize the idea that this isn't even, like, a new concept. This is just how APM has worked forever, and it's, like, totally safe.
It's just, like, where people are coming at. Don't… we shouldn't presume everyone works at an APM vendor.
And the people who don't work at APM vendors actually have, like.
Like, pretty far-out ideas about this stuff.
**atoulme** 19:44 Okay.
**Ted Young** 19:46 All right, well, I still want to work on that blog post. I'll try to put a draft, but it seems… It would be very helpful. It would be very helpful. The more we can socialize this stuff, the better.
**atoulme** 19:56 Okay, it's just it's bigger than the injector, it's not even the injector. If the injector could just bow out of that discussion, that would be great, right, in a sense.
And, we'll be… okay.
**Ted Young** 20:08 I think it's, like, about Linux package management. I mean, that's part of it, right? We're saying, like.
We're not really saying you're using the injector, right? We're saying we think you should use Linux package management, and the operator.
**atoulme** 20:22 Yes. And this is a way to improve the operator and…
**Ted Young** 20:25 But that's, like, the biggest change is, like.
how you install this stuff, right? Like…
**atoulme** 20:31 And trying to convince people that our docs should be this. This is where I think that…
**Ted Young** 20:36 Right, like, I want our docs to be like, are you using Linux? Just like… just install OTEL on your box, and you're done, you know?
**atoulme** 20:44 Well, yeah, when you were talking earlier, I had a use case diagram show up. I was like, start here, what are you trying to do?
**Ted Young** 20:50 And then have boxes, too. Yeah.
**atoulme** 20:52 stressful, because we don't have that, right, as far as I can tell.
**Ted Young** 20:55 That's where we… it'll be, like, kind of a community-wide discussion, right? To agree to say, we want this to become the normal way that people get started. This is… this is the starting point.
And you shouldn't dig into that other stuff unless you're trying to do something more complicated, like you wrote your own plugins or something that this thing can install for you.
**atoulme** 21:18 Makes sense.
**Ted Young** 21:19 That's my opinion, at any rate.
**atoulme** 21:23 Cool.
There's, well, it's a good segue, maybe. Let's, let's move on to the next item, the agenda that… is it from Jack, around this rows?
**Ted Young** 21:34 Oh, I put that in there. Oh, you put that… Same question, we don't have to answer this immediately, but something I noticed is, like, we want to have a way of installing this, but of course… the flavors of stuff that people want installed are gonna change, right? Especially… I mean, this is part of where we need this story, is like, does this thing install the collector? Or do you, like, install the collector, and, like, the collector helps? Like, there's a bit of confusion there, but the collector's definitely one place where we have lots of distros.
Right? We have different… vendors have distros, right? Like, at Grafana, we'd want people to install Alloy, because it… we still have a bunch of, like, legacy crap in Alloy that we want people to use if they're…
**atoulme** 22:19 Yep.
**Ted Young** 22:20 working with Grafana Cloud, and… and they might, even if it's open source, like, do they want the stable stuff, the unstable stuff, the kitchen sink?
You know, what do they want?
And I know we thought about breaking it down by language, but I was curious if you all had ideas about that. Because that's probably something proprietary Vendor versions of this didn't have to deal with.
**Jack Berg** 22:47 Versions of this, versions of the injector, like…
**Ted Young** 22:49 Yeah, like, the end user being like, I want… I want to, like, Linux package install… like, what will probably happen if we don't solve it through, like, there's a way to customize this, is, like, probably at Grafana, we'll just make our own you know, Linux packages that are, like, a flavor of this, so it could be, like, a build… we all use the same build tools to make our own flavors, but that… that's something that's just gonna happen, I guess is what I'm saying, and so you should have a story about it, rather than vendors all inventing Their own answer to this problem.
**Bastian Krol** 23:27 I mean, it's.
**Jack Berg** 23:28 about… go ahead.
**Bastian Krol** 23:30 Go ahead, Chick.
**Jack Berg** 23:31 I was saying, we're kind of… We're kind of poking at, like, what is the scope of the injector?
like… Like, in one… in one… Side of the spectrum.
you know, the injector could not concern itself with, you know, the distributions of the auto instrumentation packages at all. It could just be the mechanism that installs them, and, like, it's really, like, lightweight, and, you know, it's the requirement of the user To somehow, obtain, you know, whatever packages, whatever auto-instrumentation packages, and put them on your file system, and the injector will just inject them, and that's all it does.
**Ted Young** 24:11 Yeah. Like…
**Jack Berg** 24:12 The other end of the spectrum is, like, the injector gets, like, really opinionated and has lots of tools to manage, you know.
which… the packages for the auto instrumentation libraries, and has, like, you know, tools to support, you know, accessing different vendor distributions of them, tools for upgrading, all that type of jazz. Like, where does the injector lie here? Where do we want to take this thing?
**Bastian Krol** 24:37 I mean, right now, it already has configuration mechanisms to… use different SDKs that can… is in a config file, that can be… but I guess the question is more about the packaging, if we package it together as an RPM, DBIN package, whatever other distribution mechanism we can… imagine, and then how do these bundles… because these bundles then come with a fixed set of SDKs and… Stuff.
**Ted Young** 25:10 Yeah.
That's… Sweet… Sorry. Sorry, go ahead.
**atoulme** 25:17 There is, oh, here we go. I found it. So, Michael, shared a… thing on the spec repo. I kind of agree with what he's trying to achieve here, which is… We want to make it so that, we have a story that is easy to tell, and history kind of crystallized on APT install OpenTelemetry.
Right? And then it's what you install. And whatever's happening underneath.
It's kind of irrelevant for the customer, because we're going to install everything.
from the Node.js SDK, your .NET, Java, what have you, whatever, everything. If you don't like it, then you can… you get to go and pick and choose inside the Debian, like, ghost, open up the cover and get in there. So, eventually, that becomes what vendors should then also bundle in. Like, they bundle this OpenTeometry… standard, and then on top of that, you add your own customizations by having a, let's say, a Grafana RPM that is going to customize the configuration file.
**Ted Young** 26:21 Yeah. And that's it.
**atoulme** 26:23 If you manage that, we're good, we're… this is great, right?
**Ted Young** 26:29 I agree with you that this is kind of like a packaging-level thing.
And we've talked about maybe spinning up a separate packaging SIG.
**atoulme** 26:42 Never did, yeah. It's funny.
**Ted Young** 26:43 I would kind of prefer, until we end up with, like, two groups of people, and there's, like, a bunch of people who care about packaging, don't care about the injector, I would kind of… Prefer it to all get run out of this one sig for at least a bit, but…
**Bastian Krol** 26:58 I think that's fine, and I think, before we make… really… any… any really real decision on… on whether we want to offer more tooling around having different distros or different packaging to… to maybe see some real-world use cases for that.
**Ted Young** 27:21 I think we can be elaborate Grafana, at least, because we're gonna need this, like, to make it work for us. Like, there's some future, you know, where we could say, like, use the upstream collector and it's fine, but… For the foreseeable future, we're gonna want people to… T.
use… at least… at least if this thing is installing the collector. That's actually.
**Bastian Krol** 27:44 Yeah, that's where you were losing me, why… Why would the injector or the package with all the SDKs and the injector, why would that also bundle the collector? I don't see that… Yes. What's the advantage or disadvantage of not doing that?
**Ted Young** 28:03 That's where Obi and everything else is potentially gonna live, but Jack, you've got some ideas.
**Jack Berg** 28:08 Yeah, let me just jump in here. We're calling… what's our RPM package name right now?
**atoulme** 28:13 For the injector.
It's gonna be a no release, let me see you.
**Jack Berg** 28:23 It's like, if we're calling the RPM package the OpenTelemetry injector, then we can have a narrower scope. If we're calling it the OpenTelemetry package, then we need to think broader.
**atoulme** 28:33 It's a metric injector. We definitely don't think bigger than what this project does.
**Bastian Krol** 28:39 At least right now. Maybe there is a place for an all-in-one package with injector, SDKs, and collector. Maybe, maybe there's a good use case for that, but right now… it's finished.
**Ted Young** 28:52 I like that we're taking a tiered approach to the packages, right? You know, we're already taking that approach of, like, the injector package isn't gonna have everything, right? You'll have language-specific package… sub-packages, you know, and so yeah, you could then just have a… a higher, higher level one that's just, like, install OTEL. I think I… I think I want us to go there, right? Because, like, it would be nice to get the collector, just OB, profile, like, whatever we add, like, all the different facilities, like, you just get them all.
But, of course, that also involves, like.
that thing running its startup, and all these other things, so I don't know.
**Jack Berg** 29:35 It's like… We have the operator, which ostensibly is what you're describing, but for a Kubernetes environment.
**Ted Young** 29:43 Exactly.
**Jack Berg** 29:44 And the things that it doesn't install right now that were in your list were OBI.
And maybe profiling, like a profiling tool at some point. But, like, the operator won't install those for you, and so it's like.
like… It's like, the easy open telemetry button in a Kubernetes environment is to install the operator.
**atoulme** 30:03 Hmm.
**Jack Berg** 30:04 The easy Kubernetes button in a Linux environment is just to install the OpenTelemetry RPM package.
**Ted Young** 30:11 Yeah.
**Jack Berg** 30:11 And, like, what, like, that could be the, like, the, like, the North Star, the thing we follow is, like, the OpenTelemetry RPM package is just trying to do what the operator does, but, you know, without Kubernetes.
**Ted Young** 30:29 And I think what we do at Grafana is, you know, we bundle OB up in our… along with profiling, like, all of that gets bundled up in our collector distro.
I don't think Upstream currently does that, but… In my ideal… my ideal world, OpenTelemetry only has one agent. You know, as long as we can keep writing everything in Go.
**atoulme** 30:54 You know, really nice for us to not be like, and then you install, like, 3 or 4 different things.
**Ted Young** 31:01 But that's… anyways, we're really outside the domain of your collector biz and Obi biz.
**atoulme** 31:08 Yeah.
Good point. Maybe the collector will do more things moving forward. We don't know. The shape of this software is such a weird middleware thing, but… Yeah, done.
**Ted Young** 31:20 How… I'm curious, how did you historically do it?
at, like, Splunk and Instana and other places.
Like, was there… did you have, like, package management for installing all this instrumentation stuff? And then when they wanted to install some kind of agent or something, that was just totally separate, and…
**atoulme** 31:42 I can talk to it. I mean, everything we do is open source.
**Ted Young** 31:46 Yeah, I'm just curious what…
**atoulme** 31:47 So we're bleeding… we're bleeding time into maintaining our own version of everything. We have our own Ansible, our own, Chef, Puppet, Salt, Chocolatey, Bash Standalone installer, our own Helm chart, all those things. We are spending a lot of time doing a lot of work that we would want to stop doing. And this… this is why we gave the code for the injector in the first place. Like, we were, like.
What's the point of this? What does it give us? Versus how could we… benefit from having a committee around it so it can be better supported, right? Yeah. So, we have a lot of this type of stuff.
We get some value because if we play nice with vendors, for example, in some specific context, like Cloud Foundry or, let's say, Ansible, you want to have a marketplace offering so that you can have a bit more of a in for some customers.
And then you can get certifications and good things. But, I want that to be a separate thing from having to maintain it, because maintaining it is absolutely taking too much time from the engineering team, which should be dedicated to making things better, innovation, R&D, working with community, building things in the open. So, right now, yeah, this is kind of the work that we're trying to achieve.
And… I don't like it. I don't think it's, even our customers, right, are coming back to us at this point, saying, we believe in what you're selling us with OpenTeametry. Like, forget Splunk.
**Ted Young** 33:12 Right.
**atoulme** 33:13 OpenTeometry has said that they have a vendor-neutral approach to do open observability, Now we're gonna test that And then they fall into pitfalls, and I… well, and like, yeah, we did that in our distro so that we could avoid this pitfall, and you walked straight into it, and now I'm… mmm, now everybody looks bad. We look bad, open temperature looks bad, and the customers got, like, you know, a bit of a knockout. It's like, okay, I'll come back in 6 months, maybe… or maybe I'll go with some vendor. I'm done talking, right? And that's bad for everybody.
So…
**Ted Young** 33:47 100%. 100%. I really don't want the innovation moving into the distros. I think it's totally fine for distros to exist, and for everyone to have, like, a bunch of legacy junk, you know, that they just have to deal with.
But if we go to the point where, like, the innovative stuff has to happen in various distros rather than upstream.
Yeah, and the installation story is, like, this perfect example of it, so I'm really appreciating you all pushing this upstream and us all kind of agreeing on a way to do it.
But I was just curious, in your old-school way of doing it, do you… is it that there's one button they push to get everything, or is it that there's two… a couple of buttons?
**atoulme** 34:27 They push one button.
**Ted Young** 34:28 One thing to get the instrumentation, another thing to get the agent, you just don't worry about…
**atoulme** 34:33 Yeah, again, so there's no secret sauce here. Everything's public, open source, you can take it for yourself, but we have two things, right? We have an in-product experience where people can go and say, I'd like to compose the way I'm going to install this, and they got toggles, like Java.NET, Splunk.
Node.js, and I would like this on Kubernetes, or I want this on my host.
And based off that, it gives them options, like, install this bash installer that will then… which has those parameters and will do the install for you, or install a Helm chart and pass those values, right?
So everything is done through that, and then our bash installer is that as well, right? It's just doing all sorts of wrappers for… what it's doing underneath is it's calling RPM install, right? It's not online.
So, it's composable in the sense that if we had a good OpenTemmetry story with a good packaging story, then I could tell them, hey, this bash installer is just calling OpenTeometry install.
Great.
the injector, and we are not going to have to have a separate support agreement with you on our own distribution of the injector, that's way too much work. Instead, we will support you if you installed it using our Supported methods of installation.
**Ted Young** 35:43 Right. I see.
**atoulme** 35:45 So, yeah, that's…
**Ted Young** 35:47 So it's basically a package, but you did it as more just like a bash hairball, because that allows you enough optionality and…
**atoulme** 35:55 It's just people just creating, like, the synthetic sugar. It's… think of them as developers, they don't want to deal with, like, compu… installing an RPM is… And every single one of the engagements you have with people are people who have no time, right? And I've ingrained that into every scenario and use case we have, is that I say, here's the baseline, right? It's 4 p.m. on a Friday.
That's it.
**Ted Young** 36:20 We'd be great.
**atoulme** 36:21 So, if you don't have that in mind when you think about the experience of a customer.
then you missed something, right? So, for Injector, it's gonna be the same thing. It's like, it needs to work the first time without people thinking. Otherwise, you just opened up, like, a thousand hosts for config files, right? Because people, like, engineers are like, it's easy, just go to the config files, just change your YAML, what's the big deal? I'm like, no.
This is the best.
**Ted Young** 36:46 I think, yeah, honestly, I think you just defined crossing the chasm for us.
As well, right? And this is why there's a cultural shift. All the early adopters, observability is this super important thing that's underutilized that you're supposed to really care about, right? And of course, you'd want to do all this work and, like, care. But, like, when you cross the chasm, now everyone's like.
I don't care. I have no time.
**atoulme** 37:12 No time.
**Ted Young** 37:13 I just want it to work.
I don't want to learn anything.
And, like, that's a tough pill for, like, observability fanatics to swallow, right? The idea that everything we care about to other people is just a chore.
But that's really the attitude once you cross the chasm. It's like, this is a chore, and I want it to succeed.
100% of the time, and just work.
**atoulme** 37:37 Yeah, I mean, you can… you can add a few tennis balls, like, a few… a few damning questions when people push back on me on that. It's like, how about windows?
You really want to go manage Windows machines yourself? Like, what are you doing? Just install this thing, it better work the first time.
I know it doesn't count for the injector, that's easy. But, yeah, we do this all the time. I… we… this is where we spend most of our time.
I don't like it. I don't think it's useful. I would much rather work on the intricacies of the MySQL receiver, and how we're going to get, like, the Nest version of that working, and how we get more metrics out of it, and how we innovate, like… I get sometimes, like, some surprising requests on, like, I would like to get memory pressure from Darwin systems so I can see that, wow, this is cool.
we get those once since Blue Moon, when most of the time it's like, I installed this thing, and I foobarred the config file, and now things are just out of whack, and I don't like it, and… There's… the biggest issue that our customers have is the security teams, right? So they… this also is a good factor into this, is that the reason it needs to work the first time in less than 15 minutes is because it gives them hope.
And leverage, to go talk to their security team and say, can you lay off on us a little bit here? Because it worked.
it worked, and I can see it, and I want this now. And if you give them anything and tells them, hey, by the way, you've got 10 more steps to do, that gives the security team ample time to come back and say, you know what, I think we should just shut that down. You seem to be toying on your computer in a way that is not compliant.
And we don't. We don't want to have that conversation. Can you take a ticket in the queue, and now you're in the back, and we'll see you in 6 months.
**Ted Young** 39:16 Hmm.
**atoulme** 39:17 So… These are… these are real problematics, the… We will need to do a lot of work in our RPM and Debian packages to discuss the permission system. We did not do that. We don't know how to do that. This is very difficult, but the packaging SIG will have to deal with that.
And, giving fine-grained permissions and documenting them has become a bit of a… side job for me as well, right? So… We just did that on Windows, you can see it on our docs, we just had to publish, like, fine-grained permission models for Windows, because people were like, we will not even install your stuff until you document it so that we can know it's supported, so we can rely on you.
**Ted Young** 40:00 Yeah. The packaging SIG is just us in a different sim call, though, so…
**atoulme** 40:06 Yeah, it's, it's, we're, we're, in a sense, like, besties, like, okay, all this is great, but… injectors… Find what… we're talking about, like, bigger scope stuff all the time.
Yeah, yeah. We'll sort it out.
**Ted Young** 40:23 Something that would help speed things, you know, when we get to that level of packaging, probably getting some kind of history from from Splunk and Instana and, like, other places would probably help.
Like, if you want to really make sure it works one way versus the other, based off of… You know, having done this for a while.
That really helps influence these discussions and will avoid us bike-shedding, probably, if you can just bring customer stories around why you want it to work a certain way when it comes to that packaging stuff.
**atoulme** 41:05 Yeah, I could even, I think one thing that we're not doing is we could make a call for saying, hey, if you're a vendor, and you were to adopt OpenTeometry right now, like, Azure is, in a sense, has this insane advantage where they came in a bit later, they don't have as much crap that is lying around.
Why and how do you interface with your OpenTeometry ecosystem? And the first thing you do is, please don't fork.
Right? Come in, help out, and then adopt, and then augment, right? Wrap it around, right? Take the RPM for the injector, run it, and then if you really need to add more stuff, then Bring it into the injector code if you need to, but most of the time it's going to be a configuration setting. So just add the right source attributes by doing some work.
Outside of this, on the… as a rapper.
So if we could give that… it might even be, like, a new class of users of OpenTeometry, which is the vendors, and we start to give them best practices and tell them, hey, you can't just come to the OpenTeometry project and just fork all the code and claim it your own and run with it. Here is how you work with OpenTeometry to be an OpenTeometry vendor.
Not satisfied, right, not going there, but… OpenTeometry vendors should have some level of standard, and that is also going to help us kind of have end users, because I see it, right? End users come and push on me and say, are you really OpenTeometry, or you're just cosplaying, right? What are you doing?
**Ted Young** 42:31 Yeah.
**atoulme** 42:32 And I have to tell them, like, I have to remind them constantly, I'm like, I'm a maintainer, like, I work on this stuff all day, what are you talking about, right? They go, yeah, that's fine, I guess, we'll go with that.
For now.
**Ted Young** 42:44 Yeah.
**atoulme** 42:44 with us.
**Ted Young** 42:46 Yeah, it would be great to control the language about that stuff a little bit more.
But…
**atoulme** 42:52 That's very controversial, but…
**Ted Young** 42:55 We…
**atoulme** 42:55 Okay.
**Ted Young** 42:57 Luckily, the… I will say the vendors have… Jesus Christ.
We'll bet.
Yeah. Telegram.
The vendors have mostly been playing nicely with OpenTelemetry. I am happy on that front. We haven't really seen… We've mostly seen vendors do kind of what you're doing, and Grafana is doing, which is, like, we need OTEL to work, but we need our legacy stuff to work, so usually in the collector is somewhere else, there's some distro that… Makes it all limp along.
Even the vendors who like to, like, be really loud about their dislike for open telemetry, like Datadog sometimes, still, like, contributes quite a bit, and generally doesn't… Maybe we wish they'd contribute more, but luckily we haven't seen vendors doing something where we're like, hey, stop that. Stop doing that. You're doing something that's really, really negative in the community. So I feel very happy. I think part of it's we structured the project in a way that incentivizes people to… To not do that?
**atoulme** 44:05 But…
**Ted Young** 44:07 But I do think we have this new… where I see the change happening is OTEL used to be this box of Tinker toys, right? And now what we're saying is, like.
There's an installation experience, and then there's op-amp as a control plane for running this thing.
In some ways, getting vendors to be aware of OpAmp and adopting that might be part of… what you're talking about, too. It's just… Okay. Yeah. I think anyways, we're… we're just gabbing at this point, but…
**Jacob Aronoff** 44:36 Ted, I have some more thoughts on that, for later. Yeah, I don't know if we talked about this at, KubeCon, I don't know if I… were you there? I think I saw you…
**Ted Young** 44:46 That's KubeCon, unfortunately.
**Jacob Aronoff** 44:47 Not this last one. There's a thing that Josh, Surath and I are working on in that realm, but not a discussion for this group.
**Ted Young** 44:58 Great.
**atoulme** 44:59 Yeah, okay.
**Ted Young** 45:00 Yeah. But anyways, this is an area where traditionally, you've seen vendors want to kind of package things up, the installation experience and the agents and stuff, so… Anyways, yeah, it's another… you're right, though, that it's kind of a new round of talking to the vendors and seeing… If we can get some agreement on an approach.
It's probably worthwhile to be proactive about that, and not just build it…
**atoulme** 45:27 Yeah, I think…
**Ted Young** 45:28 It's what everyone's doing.
**atoulme** 45:29 We had a couple vendors come to the Collector Contribository, and I don't know if you know this, but the collector contribute repository is starting to harden its rules for new components.
**Ted Young** 45:37 Builder count, it's just too much.
**atoulme** 45:40 And, they were adding an exporter for their own stuff, and we pushed back, and they came back and said, if we can't add our own exporter to the contrary repository, then I don't think we can actually be in the OpenTemmetry space.
**Ted Young** 45:54 Yeah.
**atoulme** 45:55 Right? And we're like, wait, you have OTLP right here? Why don't you just have OTLP support? And they kind of Communication at that point.
I was thinking that if we had this type of best practices, we could avoid ourselves a lot of trouble in the first place, which is that we want all vendors to be able to help me, we don't want vendors to… we want vendors to be all going for these parts… type of, you know, approach, so they can really maximize what they get back from the community, and present that as a value add. Not a… not a straight and narrow guideline of, like, you must be compliant, but more like.
If you do this, you're gonna have a good time, right? It's more like, hey, we really think you will have a lot more fun with the space if you play along.
**Ted Young** 46:43 Yeah.
But at the same time, telling some vendors they can have their exporters in standard lib, and some vendors aren't allowed to have their exporters in standard lib isn't great.
**atoulme** 46:54 Well, I can underst…
**Ted Young** 46:56 I can easily see how that's a bad experience.
**atoulme** 46:58 Yeah, and that's something that we will need to square away, so we're working to just get rid of that, but, you know, as you always said, that takes a while.
We will do that. We've already removed our trace exporter, which was, you know, just .CLP at the end. We'll do the rest as well, and hopefully we can stop having so many custom things that are specific to us.
So, yeah, we'll see… we'll see how other vendors feel about that, but it would be great if we could do that.
**Ted Young** 47:30 Yeah.
**atoulme** 47:36 Okay, anything else for the injector? Anything else popped up, sorry.
**Ted Young** 47:41 I think we're good.
**atoulme** 47:42 Okay.
Alright, I'm gonna go. Have a good one, folks.
**Ted Young** 47:47 Yep.
**Bastian Krol** 47:47 Ew.
**atoulme** 47:48 Hi.
