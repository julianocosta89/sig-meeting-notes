SIG: Injector SIG
Date: 2026-10-01
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Jacob Aronoff (Tero)** 02:22 Hey.
**Bastian Krol (Dash0 Inc.)** 02:24 Hello, everybody.
**Jacob Aronoff (Tero)** 02:27 How are we doing?
**Bastian Krol (Dash0 Inc.)** 02:29 I'm fine, how are you?
**Jacob Aronoff (Tero)** 02:31 Doing well.
Do you have topics for today?
**Antoine Toulme (Splunk Inc.)** 02:38 It's gonna be pretty flat, I guess.
**Bastian Krol (Dash0 Inc.)** 02:41 A good question.
**Nikola Grcevski @ Grafana / OpenTelemetry** 02:49 Actually, I have questions. What happened last week? Did you guys discuss the 390?
Built?
**Antoine Toulme (Splunk Inc.)** 02:56 Why do you like this discussion so much, Ben?
**Bastian Krol (Dash0 Inc.)** 02:58 laughter.
**Nikola Grcevski @ Grafana / OpenTelemetry** 02:59 What'd you.
**Antoine Toulme (Splunk Inc.)** 03:00 Exist yourself.
**Bastian Krol (Dash0 Inc.)** 03:03 Okay.
**Antoine Toulme (Splunk Inc.)** 03:05 But if she must know.
**Nikola Grcevski @ Grafana / OpenTelemetry** 03:07 No.
**Antoine Toulme (Splunk Inc.)** 03:07 What is the latest on this? Let's go, let's take a look, right?
You wanna see what I've been reduced to, huh?
I'll share my screen. I will not spare you anymore. You've been asking for this way too much.
Yeah, who?
So… Hmm.
You can see the timeline here.
This is me on the 16th, asking where we are.
**Nikola Grcevski @ Grafana / OpenTelemetry** 03:40 Here.
**Antoine Toulme (Splunk Inc.)** 03:41 They went through a first follow-up with a lawyer. It didn't go anywhere.
Then they asked for… a week after, I said, when is the follow-up?
And she said she cannot really schedule the follow-up because it's PTO.
So then I said, maybe I should ask again in a week.
Then I said, okay, we looked into it, but they were good, we just got some edits, we need to talk to the Linux Foundation now.
Great, so now they need to set up a discussion with… this but next week would be better so then they pinged each other And then finally they were like, here are some items sometimes where I can talk.
And then she asked if the movie, else should be on that call, and I said, please do not put me on that call. And then I asked yesterday.
Did you guys get together? And she said, no.
Now they have to get more times to get together.
And this thing has been open since… December 4th, 2025. We're absolutely making sure we make this a year at this point.
**Nikola Grcevski @ Grafana / OpenTelemetry** 04:42 Yeah.
**Antoine Toulme (Splunk Inc.)** 04:43 I think we'll have a reunion after that, we'll just, you know… We'll just do it like a big festival every year.
**Bastian Krol (Dash0 Inc.)** 04:53 I want to make it a Christmas present for you, so it needs to be December.
**Nikola Grcevski @ Grafana / OpenTelemetry** 04:58 Yes.
Okay.
So.
**Antoine Toulme (Splunk Inc.)** 05:03 I'm not.
**Bastian Krol (Dash0 Inc.)** 05:04 We… I think we… More or less… said chemo is fine as an option.
**Antoine Toulme (Splunk Inc.)** 05:13 Yeah, it's fine.
**Bastian Krol (Dash0 Inc.)** 05:14 The only one that was arguing against it was Michele, and I think he was in the minority anyway.
**Antoine Toulme (Splunk Inc.)** 05:22 But the thing is, we could start now, we can get Timu, and then when we have proper Linux runners on S1NTX, then we swap.
**Bastian Krol (Dash0 Inc.)** 05:31 Yep.
**Antoine Toulme (Splunk Inc.)** 05:31 Exactly.
**Nikola Grcevski @ Grafana / OpenTelemetry** 05:33 Yes. Okay. So we, we made that decision. Yeah.
**Antoine Toulme (Splunk Inc.)** 05:37 We're not saying no, we're saying later.
**Nikola Grcevski @ Grafana / OpenTelemetry** 05:41 When we can.
**Antoine Toulme (Splunk Inc.)** 05:43 And I will continue. This, to me, is not so much for the Injector that I'm making this whole plea about IBM, it's because I need this for the collector. I don't really care. The Injector's gonna be fine, like, Zig is gonna be whatever. But, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 05:57 Collector, yes, you're right.
Although he probably is not.
Yeah.
**Bastian Krol (Dash0 Inc.)** 06:03 That makes sense.
**Antoine Toulme (Splunk Inc.)** 06:05 Okay.
Anything else? Any other open PRs?
**Bastian Krol (Dash0 Inc.)** 06:10 Yeah, I think we actually have 3 started PRs for that topic, and… Yeah, that's the key.
Somehow, a little bit…
**Antoine Toulme (Splunk Inc.)** 06:23 The FFBOs.
**Bastian Krol (Dash0 Inc.)** 06:23 At least two of them are open right now, or in draft. One from you, and one from… Bubbles… Lafayette?
**Antoine Toulme (Splunk Inc.)** 06:35 Yeah, I don't think we can, You could pick up the work for Pebble, but I think he butchered some stuff.
**Bastian Krol (Dash0 Inc.)** 06:41 Yeah.
**Antoine Toulme (Splunk Inc.)** 06:42 He went a little too fast.
**Bastian Krol (Dash0 Inc.)** 06:44 Okay.
**Antoine Toulme (Splunk Inc.)** 06:45 he, I mean, pretty much, OPRs look a little the same, because what he's done is that he's made it possible for you to swap out AMD to S390X. Then the actual testing… is he using QMU?
I think so. Yeah, set up QMU.
So we could pick up his, his, his PR.
I'm good with that for now.
**Nikola Grcevski @ Grafana / OpenTelemetry** 07:14 Sounds good.
**Bastian Krol (Dash0 Inc.)** 07:15 So… Just for me to understand this, the decision is chemo is fine, we could do this, it's just now a matter of who wants to invest time there, and… whether we get around to it. Is that… is that about correct? Okay.
**Antoine Toulme (Splunk Inc.)** 07:36 I'm gonna get yelled at. So, one thing, is we could possibly test it in CI and not release, the Injector for those architectures for now.
**Bastian Krol (Dash0 Inc.)** 07:45 Sure, can do it in steps, that's fine, yeah.
**Antoine Toulme (Splunk Inc.)** 07:49 Okay.
**Bastian Krol (Dash0 Inc.)** 07:51 I mean… If it runs fine on CI, I don't see why we wouldn't also build release artifacts soon after.
Right.
**Nikola Grcevski @ Grafana / OpenTelemetry** 08:02 Yeah, I mean, it's the same binary, really.
**Bastian Krol (Dash0 Inc.)** 08:05 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 08:06 It emulates the whole hardware, so I… Really does, does.
4.
**Antoine Toulme (Splunk Inc.)** 08:13 But, I mean, he's, so, let's see, he's worked 3… changes do not… He's not… he's not really trying to build for… The packages, right?
That's okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 08:28 We can, we can revamp that PR from scratch.
**Antoine Toulme (Splunk Inc.)** 08:31 Yes, for sure. Yeah.
**Bastian Krol (Dash0 Inc.)** 08:32 the.
**Nikola Grcevski @ Grafana / OpenTelemetry** 08:33 there.
**Antoine Toulme (Splunk Inc.)** 08:33 Why is it not passing build right now?
**Bastian Krol (Dash0 Inc.)** 08:36 I did not look at all into that PR because.
**Antoine Toulme (Splunk Inc.)** 08:39 Perfect.
**Bastian Krol (Dash0 Inc.)** 08:40 And I don't have an opinion if you should maybe start from scratch or reuse any of that work.
**Antoine Toulme (Splunk Inc.)** 08:46 noise.
**Bastian Krol (Dash0 Inc.)** 08:47 I think that's… I mean, he has abandoned it pretty much, probably saw that.
I mean…
**Antoine Toulme (Splunk Inc.)** 08:54 Pablo is from the operator. We told the operator, hey guys, why do you support S390X? You don't have the means to test it. And I think this was a very gentle response from an operator maintainer, it's like, you can support S390X, it's not that hard.
Look how we do it.
**Bastian Krol (Dash0 Inc.)** 09:10 talking.
**Antoine Toulme (Splunk Inc.)** 09:10 We do that as a stepping stone to move the injector to the operator. Because the operator supports Istrela TX, we've been in a holding pattern because we can't.
We don't support S386.
And that's why the operator is not moved to the Injector yet.
So, you know, who's gonna move first?
**Jacob Aronoff (Tero)** 09:32 I mean, it's… this is, like, such a Red Hat type of concern, too. You know, it's like…
**Antoine Toulme (Splunk Inc.)** 09:38 Yep.
**Jacob Aronoff (Tero)** 09:39 We do work on, you know, this old mainframe that… You know, probably… 10 companies in the world still use.
Therefore, we need to support instrumentation there, which is very Red Hat thought.
**Antoine Toulme (Splunk Inc.)** 09:56 Well, plus, I mean, he's an IBM employee, so one thing you could do is make Pavel pay for this fully, and make him responsible for this code moving forward.
**Jacob Aronoff (Tero)** 10:04 No, no, Pavel's Red Hat, not IBM.
**Nikola Grcevski @ Grafana / OpenTelemetry** 10:06 Same.
**Antoine Toulme (Splunk Inc.)** 10:08 So it's the same thing. Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 10:10 imply.
**Antoine Toulme (Splunk Inc.)** 10:11 Yeah.
**Jacob Aronoff (Tero)** 10:15 Oh, right.
**Nikola Grcevski @ Grafana / OpenTelemetry** 10:16 There we go.
**Jacob Aronoff (Tero)** 10:16 the.
**Bastian Krol (Dash0 Inc.)** 10:17 Yes. You missed the last 10 years of tech acquisitions.
**Jacob Aronoff (Tero)** 10:23 It was like.
**Antoine Toulme (Splunk Inc.)** 10:24 I mean… They really try hard not to make it look like it, but at the end of the day.
Someone with a button, I'm sure.
**Jacob Aronoff (Tero)** 10:31 Totally forgot that that happened.
**Nikola Grcevski @ Grafana / OpenTelemetry** 10:34 Yeah. But you'll know it's done once it's finally a blue hat instead of red hat.
**Jacob Aronoff (Tero)** 10:38 Ha ha ha.
**Antoine Toulme (Splunk Inc.)** 10:41 Slowly getting absorbed, but, so… sure, Okay.
Anyway, that's, personally, I'm more interested in my little drama with lawyers, but if you… If you want to get QMU so I can talk to the operators and get over the hump and actually move the injector to the operator finally by the next KubeCon would be kind of nice.
Does that make sense? Is that even possible?
**Nikola Grcevski @ Grafana / OpenTelemetry** 11:07 KubeCon EU.
**Antoine Toulme (Splunk Inc.)** 11:09 No, not for her.
**Nikola Grcevski @ Grafana / OpenTelemetry** 11:11 North America, 27 or 26?
**Antoine Toulme (Splunk Inc.)** 11:14 Okay, you're pushing it, so OSS Summit in Prague in 2 weeks.
**Jacob Aronoff (Tero)** 11:19 So.
**Antoine Toulme (Splunk Inc.)** 11:23 I'm actually going by the way, next Monday. It's Monday next week.
**Bastian Krol (Dash0 Inc.)** 11:27 Rock. Nice.
**Nikola Grcevski @ Grafana / OpenTelemetry** 11:29 Nice.
**Antoine Toulme (Splunk Inc.)** 11:31 Yeah.
**Jacob Aronoff (Tero)** 11:32 Antoine, you want to give me some of your, your budget so I can go?
**Antoine Toulme (Splunk Inc.)** 11:36 Thanks. We got zero.
I ate all of it.
**Nikola Grcevski @ Grafana / OpenTelemetry** 11:43 and.
**Antoine Toulme (Splunk Inc.)** 11:43 Okay, so Oh.
There is a really… There is a PR about signing stuff with SIGSTOR, does anyone care?
**Jacob Aronoff (Tero)** 11:55 I mean, we probably should do it, no?
Yeah. It's good to sign releases, it's good to…
**Antoine Toulme (Splunk Inc.)** 12:04 I think… I think you got a first… okay, so he got a request to change from Michaela, then he changed it, and then I think it would be great if someone else could take a look as well, make sure they're okay with it.
**Nikola Grcevski @ Grafana / OpenTelemetry** 12:15 Okay.
**Antoine Toulme (Splunk Inc.)** 12:16 Okay.
**Jacob Aronoff (Tero)** 12:17 You know.
**Antoine Toulme (Splunk Inc.)** 12:18 I think the feedback from Igor has been addressed.
**Nikola Grcevski @ Grafana / OpenTelemetry** 12:20 Yes, yeah, yeah.
**Antoine Toulme (Splunk Inc.)** 12:22 Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 12:24 Okay, we'll take a look.
I put one thing on the agenda.
Alright. Because I've been thinking about doing this, but I just wanted to make sure everyone was okay with that.
Michaela keeps saying about this… Java, old releases that are not supported.
And I think we have in the packaging SIG some support for Like, sanity checks?
say, Python.
I think Diego added that.
Oh, yeah. But I think, just like in .NET, I think for the JVM, I think it might be easiest to do the sanity check.
In the in the Injector.
So we detect that it's an old Java based on the libjvm maybe, if we can figure it out.
I'll do it, because I don't know if it can be done in the SDK. It's already loaded.
I mean, does old Java even load agents? I don't know.
**Antoine Toulme (Splunk Inc.)** 13:25 Huh.
**Bastian Krol (Dash0 Inc.)** 13:25 Jack would be the best person to know about that, I guess. And I think he talked about some protection within the SDK.
**Nikola Grcevski @ Grafana / OpenTelemetry** 13:36 convincing.
**Bastian Krol (Dash0 Inc.)** 13:36 I might misremember that.
But, I mean, in general, the idea is pretty good, I think, and I think for .NET, if that's possible, that would also be worthwhile, like… saying… Yeah, we don't support .NET.
**Nikola Grcevski @ Grafana / OpenTelemetry** 13:54 6.
**Bastian Krol (Dash0 Inc.)** 13:55 4.
**Nikola Grcevski @ Grafana / OpenTelemetry** 13:56 Whatever, yeah.
**Bastian Krol (Dash0 Inc.)** 13:57 Yeah, yeah, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 13:57 Yeah, don't that we have some checks that this guy Matt added.
But they're in the Injector, but I'm not just sure how to…
**Bastian Krol (Dash0 Inc.)** 14:06 Injector, we don't have any version checks.
**Nikola Grcevski @ Grafana / OpenTelemetry** 14:10 I think it just checks, oh.
I think it checked.
**Bastian Krol (Dash0 Inc.)** 14:13 We just check the lip C, version and stuff, and then we unconditionally… Nikola Grcevski @ Grafana / OpenTelemetry 14:21 I think we do check for conflicts or incompatibilities.
**Bastian Krol (Dash0 Inc.)** 14:26 Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 14:26 Injector there is code.
**Bastian Krol (Dash0 Inc.)** 14:32 Yeah. Maybe, maybe things develop there.
**Nikola Grcevski @ Grafana / OpenTelemetry** 14:35 Yeah.
**Bastian Krol (Dash0 Inc.)** 14:35 looked.
**Nikola Grcevski @ Grafana / OpenTelemetry** 14:36 The .NET one does have, Some additional checks. It checks for… I don't… I think it does check for version.
Hmm.
Right?
Yeah, minimum .NET major version, yeah. Runtime config target supported .NET, yeah, yeah, yeah. Because .NET is easy, they ship this file, always with executable, so if you can find the file… You can actually find out in there if it's compatible.
Okay.
So.
**Bastian Krol (Dash0 Inc.)** 15:11 That brings me to some idea, because… what we actually can support, the Injector might not know.
Because, of course, you can point it to entirely different .NET to ship it with an old .NET SDK framework that has support for farther back, or with your custom distro. So then you… if you want to do… I mean, that's… what's in there for .NET is in, that's fine, but if you want to do that for Java.
It might even need to be configurable, what the minimum version is.
I mean, maybe not. Nobody wants to support Java 6 or whatever.
**Nikola Grcevski @ Grafana / OpenTelemetry** 15:57 Yeah.
**Bastian Krol (Dash0 Inc.)** 15:58 but… Nikola Grcevski @ Grafana / OpenTelemetry 16:00 Yeah, Mike.
**Bastian Krol (Dash0 Inc.)** 16:01 The intricacies here.
**Nikola Grcevski @ Grafana / OpenTelemetry** 16:03 So you're saying that maybe somebody has like a proprietary SDK or outside of OTel SDK, they may want to use the Injector to inject?
**Bastian Krol (Dash0 Inc.)** 16:11 Yeah, pretty much. So right now we are building the Zero.net distribution and that has limited support for .NET.
6 and 7, as far as I understand. In addition to… so it's based on the latest upstream, which starts at .NET 8, but we have some… I don't know exactly, but we have made some tweaks for older .NET versions. And if you then… Cool. Block that in the Injector without any way to circumvent that.
**Nikola Grcevski @ Grafana / OpenTelemetry** 16:46 That's not great, yeah.
**Bastian Krol (Dash0 Inc.)** 16:47 So.
**Nikola Grcevski @ Grafana / OpenTelemetry** 16:47 We should probably then make this configurable or an optional, because right now… Which version of the.
**Bastian Krol (Dash0 Inc.)** 16:55 good.
**Nikola Grcevski @ Grafana / OpenTelemetry** 16:56 Yeah, so I think, I think we just went with what the OTEL supported, but I think it… if you guys are doing something different, then we should probably…
**Diego Hurtado (Dash0)** 17:07 I mean, in Python, what we do is, we kind of collect all the… Dependencies are installed.
Yeah. And check the versions, and pick the… highest minimum version.
**Nikola Grcevski @ Grafana / OpenTelemetry** 17:22 Yep.
**Diego Hurtado (Dash0)** 17:22 And all of them.
**Bastian Krol (Dash0 Inc.)** 17:24 But that happens in a site script after the Injector. That's not something that the Injector does, right?
**Nikola Grcevski @ Grafana / OpenTelemetry** 17:30 Yeah.
**Bastian Krol (Dash0 Inc.)** 17:33 It happens in packaging now, I think.
**Nikola Grcevski @ Grafana / OpenTelemetry** 17:35 Oh, okay, cool. It's configurable, so don't worry about it. Yeah. The config, there's a configuration for a minimum .NET version.
**Bastian Krol (Dash0 Inc.)** 17:42 Nice.
**Nikola Grcevski @ Grafana / OpenTelemetry** 17:43 Override it, yeah. Okay.
**Bastian Krol (Dash0 Inc.)** 17:45 Oh, okay, okay. Yeah, that's then a pattern that we should probably keep if we want to extend that to more runtimes.
**Nikola Grcevski @ Grafana / OpenTelemetry** 17:52 Yeah, Python is easy, Diego, because you have this site customized, right? Or the other customized, whatever. I don't know which one is which, but, But you can actually load that, and that can load other stuff. But .NET… Only one can be a profiler and can just load this up in advance, and there's… There's no chance after that point.
We would have to.
I guess it's possible, like, maybe you do, like, blow the DLL.
After. So you have to have a fake profiler, I guess?
And the fake profiler can roll the real profiler, but then we have to ship a fake profile… Sanitizer, something.
So it was simpler to do it in the Injector. This dependency checking is actually in .NET done in the Injector.
**Antoine Toulme (Splunk Inc.)** 18:43 Interesting.
**Bastian Krol (Dash0 Inc.)** 18:45 Yeah, and I think if you can detect it from inspecting what's loaded, which SLOs are loaded or are in play, that's a smart approach. Yeah, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 18:58 interesting.
**Bastian Krol (Dash0 Inc.)** 18:59 earlier, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 19:00 Yeah, so I mean, it's, I guess it's possible to do it for dotnet. It's just we need to build a dotnet.
filer that Acts as a profiler, gets loaded by the injector, and that one then… does all the sanity checks, you can probably query what other DLLs are loaded.
And maybe find that file the Injector does, and then do… Low chair library.
and then initialize the real profiler, and then I somehow switch them around.
I mean, it's doable, it's just…
**Bastian Krol (Dash0 Inc.)** 19:31 It's cumbersome, no. Just to be clear, what I meant to say was your initial idea of doing the check in the Injector by inspecting what's loaded sounds.
pretty smart, and it could be a mechanism that we can reuse for different runtimes. Runtimes. Rather cheaply.
Diego, you wanted to.
Come in.
**Diego Hurtado (Dash0)** 19:54 I just wanted to understand, Okay. Is the question… Should the injector be the one who does the dependency checking, or it should be something else? Is that… is that the question we're trying to answer?
**Nikola Grcevski @ Grafana / OpenTelemetry** 20:08 Yeah, I just wondered, like, how do we do Java 6, you know, or Java 7, because it's… if you try to load the… the SDK on Java 6, I think it will not work, and potentially crash the application. And… I mean, with Python and Node.js and even Ruby, you can take the original OTEL SDK, the one that's published, that the operator uses, and you can add additional scripts that run before it, like the site customizing Python, do all the checks you want, and then just simply do load, initialize the SDK. Those languages are pretty… amenable to that. So what I'm saying is that, for something like, if you want to take the OpenTelemetry agent jar.
for Motel. And so how do we do a Java 6 or later, earlier than 8 check.
It would have to be.
done in a jar, but then I don't even know if those JDKs can load an agent.
So, the question is, if they cannot load anything.
And I just fail if we add them this agent.
On the command line, or something, and they do something stupid.
**Diego Hurtado (Dash0)** 21:25 What… okay, my question is, like, if we make the SDK.
If… if checking the version.
It's, unfailing gracefully.
It's a feature of the SDK.
Yeah. Was a feature of the SDK.
then you could use that feature for Java.NET, and every other language, right? That's right?
**Nikola Grcevski @ Grafana / OpenTelemetry** 21:49 Yep.
**Diego Hurtado (Dash0)** 21:50 Okay, so should we bring this to the specification SIG so that we add this feature to every SDK?
**Nikola Grcevski @ Grafana / OpenTelemetry** 21:59 I'm not sure it's possible. Let's say, talk about Java specifically, right? So.
I don't think the Java agent itself can drop the SDK build requirement to go below eight.
**Antoine Toulme (Splunk Inc.)** 22:12 No, don't worry.
**Nikola Grcevski @ Grafana / OpenTelemetry** 22:13 So they just, it's impossible. Like Java 6 was so like, for example, or 7, it just doesn't support many of the things that you need.
And they will not rewrite the code to support.
You know.
**Diego Hurtado (Dash0)** 22:27 Yeah, I'm not… I'm not… sorry, I'm not… I'm not suggesting adding support for all versions. What I'm suggesting is Add… something… for every SDK that, checks whatever version.
It's needed, and if not, fails gracefully.
So that the Injector can use that feature uniformly among with any organization.
**Bastian Krol (Dash0 Inc.)** 22:54 That might not be possible in every SDK, and what I'm hearing, Diego, is that you would like to source this consistently for all runtimes. Either it's always the SDK's responsibility, or always the Injector, and I think… in my experience with these type of things, that's the wrong thing to optimize for very much. I think what we need in the field that we are acting here is a pragmatic and opportunistic approach.
If the SDK can do it, then let the SDK do it, because it is better at that, and for the runtimes where it's very hard, or maybe even impossible, if the Injector can.
do it, then the Injector does it, and that really needs to be decided on a case-by-case basis and differently for each runtime, even if that is entirely inconsistent, how these mechanisms work across all the runtimes.
we need to find the best matching approach per runtime. That's my…
**Diego Hurtado (Dash0)** 24:00 Okay, yeah, I don't necessarily disagree with you, but I also, if I remember correctly, weren't we working in… In some feature to be added to the specification.
That determines if some SDK is injectable or not.
**Nikola Grcevski @ Grafana / OpenTelemetry** 24:18 Yeah, in that.
**Diego Hurtado (Dash0)** 24:19 Can we also add this?
So that for an SDK to be determined injectable, it must support this feature that fails gracefully, blah blah blah, minimum version is not supported. If we're already doing that feature, that work, we could add this there.
**Nikola Grcevski @ Grafana / OpenTelemetry** 24:34 I think the… I think the Java SDK is actually quite good there. It will figure all these things out, but everything will have some sort of limitations. And what I was going after is.
If their main developer boundary is Java 8 right now, and all the code they've written is Java 8. So, you technically need to write another agent somehow that will have lower Java, like 6, because Java 8 bytecode will not even be loaded. The JVM will just reject it and fail it.
it will say that's a newer bytecode than I can support, because the Java class file has a bytecode version in there, and it won't, like, they won't even get to run any checks. Even if they wanted to add a check, are you Java 8 or above, they wouldn't even get to that point. The failure will be much earlier.
Umm.
So I think we'll have to find another mechanism for JAWA.
Which is the same issue that we had with .NET. It's already too late by the time they do that.
**Diego Hurtado (Dash0)** 25:37 Right, but if in… if the Java SDK had this feature of failing gracefully, would that solve your problem?
**Nikola Grcevski @ Grafana / OpenTelemetry** 25:47 It would, but then… What I'm saying is, like, really difficult for them Build that in a… Or there will be… consumable by the Injector.
**Diego Hurtado (Dash0)** 26:00 Okay, okay, I get your point, okay, I get your point. So, what you're saying is that it may be easy to implement that feature in Java, but it'll still… Nikola Grcevski @ Grafana / OpenTelemetry 26:11 How do we proceed?
**Diego Hurtado (Dash0)** 26:11 For the… for the Injector, right?
**Nikola Grcevski @ Grafana / OpenTelemetry** 26:13 Yeah, how do we consume it? Like…
**Diego Hurtado (Dash0)** 26:16 It doesn't matter, because Injector can just have to inject and carry on, like.
It doesn't care, the SDK will catch it and fail gracefully later, right?
**Bastian Krol (Dash0 Inc.)** 26:26 But maybe it won't fail gracefully, and that's the cases that we need to take care of.
And I think there are probably cases where no matter how hard we require.
**Diego Hurtado (Dash0)** 26:37 Oh, okay.
**Bastian Krol (Dash0 Inc.)** 26:37 from the SDKs, they won't fail gracefully. I mean.
**Diego Hurtado (Dash0)** 26:41 444.
**Bastian Krol (Dash0 Inc.)** 26:42 For Java 6, are there? Just curiosity, is Java 6 a realistic thing that still happens?
**Nikola Grcevski @ Grafana / OpenTelemetry** 26:51 I didn't think so. I, I didn't think so. But, Michaela claims that I don't, I don't know that he sees a lot of people still running Java six. And he mentioned it in a few, I think two weeks ago. Yeah. So it got me thinking.
I didn't think it was still real. Everybody moved to Java 8, I thought, but…
**Bastian Krol (Dash0 Inc.)** 27:12 Antonio Waltz or Laughing Hearts or.
**Diego Hurtado (Dash0)** 27:15 Yeah, but Bastian were.
**Jacob Aronoff (Tero)** 27:17 It was, like, over a decade ago. Yeah.
**Diego Hurtado (Dash0)** 27:20 Sebastian, the… the concern you have is that Users may end up.
With an injector that doesn't check.
this minimum version.
just… carries on, passes it to the SDK, and the SD… the particular SDK version that the users are using also doesn't check, and it… crashes the…
**Bastian Krol (Dash0 Inc.)** 27:45 No, no, that's not…
**Diego Hurtado (Dash0)** 27:46 What you're concerned about?
**Bastian Krol (Dash0 Inc.)** 27:48 No, that's not my concern. My concern is that even if… let's stick with the Java example, even if the… Java SDK has a lot of inbuilt checks that, handle a lot of situations and step down gracefully. There will be, as Nikola pointed out, limits to that with like Java versions from the Stone Age, that will not work, just because of bytecode incompatibilities, and there's nothing the SDK can do about that.
**Diego Hurtado (Dash0)** 28:19 But the SDK can fail gracefully in that case, like, it can detect, okay.
**Bastian Krol (Dash0 Inc.)** 28:24 No!
**Nikola Grcevski @ Grafana / OpenTelemetry** 28:25 No, we cannot check.
**Bastian Krol (Dash0 Inc.)** 28:26 You keep saying that, but no… Nikola Grcevski @ Grafana / OpenTelemetry 28:27 No, no, no, Becky.
**Diego Hurtado (Dash0)** 28:29 No, I'm sorry, I am not an expert in DIY. I don't know anything about DIY.
**Nikola Grcevski @ Grafana / OpenTelemetry** 28:32 I'll explain.
**Diego Hurtado (Dash0)** 28:33 you guys.
**Nikola Grcevski @ Grafana / OpenTelemetry** 28:33 I'll explain. Let's say you build the Java agent in Otto.
In the Java agent project itself, that builds that agent.
You have to specify what is your bytecode level.
And they have long time chosen Java 8 as the minimum version they will support as bytecode. So all the features they're using within the project to build the Java agent have that assumption baked in.
And each major Java version brings additional features.
That… You now have to, if you want to back… walk back that decision and change it to an earlier version, you have to rewrite your code and It breaks a lot of assumptions and so on.
So when the Java agent is produced as a file, this jar, all the classes inside have this byte code version hard coded. It says it's eight. So when you try to load that on an old JVM, say Java six.
**Diego Hurtado (Dash0)** 29:33 Yeah, yeah, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 29:34 It, it won't even get to load the SDK that JVM will reject. It says you have supplied us something that we can't even parse.
**Diego Hurtado (Dash0)** 29:42 Yeah, yeah, I get it, I get it.
Even the process of trying to detect will fail.
**Nikola Grcevski @ Grafana / OpenTelemetry** 29:47 fail.
Okay, okay, I get it. The verifier will reject it. There's a verifier in every JVM that will just… Walk the bike, and it says, no, no, this is not acceptable for us to load.
**Diego Hurtado (Dash0)** 29:59 Yeah, you can't even check, because that checker will fail.
**Nikola Grcevski @ Grafana / OpenTelemetry** 30:03 Failed to load.
**Bastian Krol (Dash0 Inc.)** 30:04 Your code won't load. Like, if you load a Python 3 script in Python 2.7 or something.
**Nikola Grcevski @ Grafana / OpenTelemetry** 30:12 If it's not compatible, it will just say, This is not Python, right?
**Diego Hurtado (Dash0)** 30:16 Okay, yeah, this is impossible. There's no solution for this.
**Bastian Krol (Dash0 Inc.)** 30:19 Yeah.
**Antoine Toulme (Splunk Inc.)** 30:20 Can we document this problem? Can we document it somewhere on the Injector repo, and then… Move on.
**Nikola Grcevski @ Grafana / OpenTelemetry** 30:26 Well.
**Antoine Toulme (Splunk Inc.)** 30:27 I mean.
**Nikola Grcevski @ Grafana / OpenTelemetry** 30:28 I would like to try to fix it, but I don't know if it's doable. So I'd like to see if we can peek inside the libjvmso and see if we can find the version. I think it's doable. We do that kind of stuff.
peek inside binaries, and if we notice, the version will be in there. So if it's not 8 or above, we just… It's like, no, they won't touch you.
**Antoine Toulme (Splunk Inc.)** 30:51 Do we have…
**Bastian Krol (Dash0 Inc.)** 30:52 Nobody is stopping you from giving it a try, I wish.
**Nikola Grcevski @ Grafana / OpenTelemetry** 30:55 Yeah, okay.
Okay.
**Antoine Toulme (Splunk Inc.)** 30:58 But even before that, like, if… do you have an open issue for this?
**Nikola Grcevski @ Grafana / OpenTelemetry** 31:01 No, I don't have, no.
**Antoine Toulme (Splunk Inc.)** 31:03 Okay, so, so, feel free to… Feel free to stop at any point. First stop is to say, we know it's broken, we know it's not supported.
Second stop is you open an issue for it and say, I think it would be doable, someone needs to go take the time, and then third stop is you actually do a POC and you try it out.
**Nikola Grcevski @ Grafana / OpenTelemetry** 31:24 Sounds good. So first you want me to make a PR to document that we're not supporting this, right?
Yep.
**Antoine Toulme (Splunk Inc.)** 31:29 I don't want to. I'm offering that you.
**Nikola Grcevski @ Grafana / OpenTelemetry** 31:32 Yeah, yeah.
**Antoine Toulme (Splunk Inc.)** 31:33 Be so willing. I think that would actually help to have a hedge and to, bring people to a bit of an understanding, because if it's failing, and we don't document that it fails in that case, then we are actually setting ourselves up for pretty much some hate mail, right, down the road.
**Nikola Grcevski @ Grafana / OpenTelemetry** 31:50 Yeah, yeah, you bet.
I think it's less. Yeah, I think it's less of an issue on Kubernetes. I don't know how many people are on Java below 8 or Kubernetes, but With the packaging, Linux SIG packaging, and you dump a package on a system, and there's some ancient Java there, we're just gonna nuke it.
**Bastian Krol (Dash0 Inc.)** 32:08 That could happen, totally, yeah.
**Antoine Toulme (Splunk Inc.)** 32:10 I find this to be very interesting because in this world that I'm living in, I'm constantly being badgered to do something about vulnerabilities and keep up to the latest and all that. And then there you go, you got these guys running on Java 5 over there.
**Bastian Krol (Dash0 Inc.)** 32:25 Yeah, yeah.
**Antoine Toulme (Splunk Inc.)** 32:27 How did you get that sweet deal? Like what stunt did you push?
How is that even sustainable, like, from an employment maintenance perspective? Like, you can't do anything with that code.
And
**Bastian Krol (Dash0 Inc.)** 32:41 Oh.
**Antoine Toulme (Splunk Inc.)** 32:41 This is.
**Bastian Krol (Dash0 Inc.)** 32:42 We lost the source code for this 10 years ago, and we only have the JAR file, and…
**Antoine Toulme (Splunk Inc.)** 32:48 Fetching the class file by hand. Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 32:51 You know, I think a lot of people don't realize these days that with an agent or something, you just rewrite all your old crappy stuff and modernize them.
**Antoine Toulme (Splunk Inc.)** 32:59 that's… Nikola Grcevski @ Grafana / OpenTelemetry 33:00 You know.
**Antoine Toulme (Splunk Inc.)** 33:01 Exactly, so you could have a… you can even decompile the code in Java, you can do that, like, you can take the bytecode, make it back to some… almost workable Java code and then you could do something right.
**Nikola Grcevski @ Grafana / OpenTelemetry** 33:11 Have the agent write it again, yeah.
With Modern Job, yeah.
**Antoine Toulme (Splunk Inc.)** 33:15 I wish, I wish I had a better feedback, but at least I want to be able to tell people like, have you thought about doing something about this instead of telling me?
**Nikola Grcevski @ Grafana / OpenTelemetry** 33:22 that.
**Antoine Toulme (Splunk Inc.)** 33:22 My problem?
**Nikola Grcevski @ Grafana / OpenTelemetry** 33:25 Yeah, we can put a, we can put a funny message in our rejection.
from the Injector to say, please use AI to rewrite this application in modern Java.
**Antoine Toulme (Splunk Inc.)** 33:38 I think that's a beautiful idea.
**Bastian Krol (Dash0 Inc.)** 33:41 Okay.
**Antoine Toulme (Splunk Inc.)** 33:42 Thank you.
**Nikola Grcevski @ Grafana / OpenTelemetry** 33:43 All right.
**Antoine Toulme (Splunk Inc.)** 33:44 but.
**Nikola Grcevski @ Grafana / OpenTelemetry** 33:45 here, folks.
**Bastian Krol (Dash0 Inc.)** 33:46 Bye-bye.
**Diego Hurtado (Dash0)** 33:46 And you, take care. Bye.
