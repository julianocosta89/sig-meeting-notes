SIG: Injector SIG
Date: 2026-10-08
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Michele Mancioppi (Dash0 Inc.)** 00:10 Hello again.
**Nikola Grcevski @ Grafana / OpenTelemetry** 00:12 Okay.
**Michele Mancioppi (Dash0 Inc.)** 00:16 Did you find anything cool in the Cilium instrumentation for HTTP?
**Nikola Grcevski @ Grafana / OpenTelemetry** 00:22 Yeah, it's cool. I mean, they… it's not they… yeah, they serve, also.
The HTTP, right? I mean, static page is straight out of EVPF.
**Michele Mancioppi (Dash0 Inc.)** 00:34 Cool stuff. It feels like running Doom on a toaster.
**Nikola Grcevski @ Grafana / OpenTelemetry** 00:37 Yeah, something like that, yeah.
of… I have to see how they pull it off, but seems a little bit it seems very interesting, yeah.
**Antoine Toulme (Splunk Inc.)** 00:49 Okay, I'm putting in.
**Michele Mancioppi (Dash0 Inc.)** 00:51 He's alive.
**Antoine Toulme (Splunk Inc.)** 00:55 There you go.
**Michele Mancioppi (Dash0 Inc.)** 00:57 And he's also very muted.
**Jacob** 01:01 Oh, I was here last week, no, I was here, yeah.
**Michele Mancioppi (Dash0 Inc.)** 01:05 I have not, I have not seen you in ages.
**Jacob** 01:09 How are you?
**Michele Mancioppi (Dash0 Inc.)** 01:11 You never write, you never call.
**Jacob** 01:13 You're not getting my letters.
**Antoine Toulme (Splunk Inc.)** 01:16 It's…
**Michele Mancioppi (Dash0 Inc.)** 01:16 Ha ha ha.
**Jacob** 01:19 My correspondence chain has, has failed. My pigeons need to be retrained.
**Michele Mancioppi (Dash0 Inc.)** 01:24 So you are shooting the messenger now.
**Jacob** 01:27 Very.
**Michele Mancioppi (Dash0 Inc.)** 01:28 Classic.
**Jacob** 01:29 Yeah.
**Antoine Toulme (Splunk Inc.)** 01:34 Okay.
Nikola, you want to talk to us about the Java 8 guard you just put in place?
**Nikola Grcevski @ Grafana / OpenTelemetry** 01:44 Yeah, yeah, I was, I mean, it was more than I thought I needed to do.
So, I just wanted to bring it up here.
Damn.
Yeah, it's a large PR. I don't know if… How could I… maybe I can split it and start adding support?
A bit by bit, because I had,
**Michele Mancioppi (Dash0 Inc.)** 02:06 I went through it, the overwhelming majority is tests.
Yeah. is also rather uncontroversial.
**Nikola Grcevski @ Grafana / OpenTelemetry** 02:15 Yeah.
**Michele Mancioppi (Dash0 Inc.)** 02:16 Why I've not pressed the plus one button is because I didn't have a chance to try it in local.
**Nikola Grcevski @ Grafana / OpenTelemetry** 02:21 Okay.
There's one thing that I just wanted to bring up, which I think I mentioned in the description, it sort of deviates from what we do today.
So… I, lo and behold, I added a check.
For… for the Java… version, and I tested it.
And I was like, okay, great. Or I can check that it's Java six.
ancient JVM, and so on. But when I tried it in our run script. I brought it in a shell, and of course, my test failed. And I was like, what's going on? Like, I detected Java 6, but it still fails. And the issue is that the shell, the injector, injected Java tool options.
So the environment variable is already there. So essentially, then the JVM got launched from within the child… as a child process from the shell, and inherited that thing, so… At that point, whether I find it, that it's Java 6 or not, it's pointless, because the tool options already set.
**Michele Mancioppi (Dash0 Inc.)** 03:29 No, I mean, technically, we can, we can sanitize it, so if you find it, we can remove it from the environment.
**Nikola Grcevski @ Grafana / OpenTelemetry** 03:35 Yeah, so I did something else. I thought about that solution. So I thought about a couple of solutions. So one thing I did was.
I what's in this PR?
Essentially, I looked and looked and researched, and all the JVMs that I could find, that… Run… that can load an agent, use this launcher, Jeb.
libjli that I saw. So I said, if the process doesn't have this in their maps, I'm not going to attempt Java instrumentation at all.
That was what is in here, but this is a question I have, which is deviates from our throw everything, On anything, and see what sticks.
**Bastian Krol (Dash0 Inc.)** 04:15 So, quick…
**Michele Mancioppi (Dash0 Inc.)** 04:16 you.
**Bastian Krol (Dash0 Inc.)** 04:18 Sorry, you weren't finished. I didn't want to interrupt.
**Nikola Grcevski @ Grafana / OpenTelemetry** 04:21 No, that's… that's it. And then I thought about maybe I can… if it's there, and I can detect that we've added it?
The Java tool options.
through a parent process that I can somehow mark.
That it was us, and then revert it.
essentially, but… Which is why I had, like, an open question. What I have here just relies on, if you don't find libjli, then you don't attempt Java tool options at all.
**Michele Mancioppi (Dash0 Inc.)** 04:50 I could bet that, IBM J6.
**Nikola Grcevski @ Grafana / OpenTelemetry** 04:57 So.
**Michele Mancioppi (Dash0 Inc.)** 04:58 That library?
**Nikola Grcevski @ Grafana / OpenTelemetry** 05:00 Yeah, everything. I tested J9, I tested Zing, I tested, I tested with Grawl.
Yep.
**Michele Mancioppi (Dash0 Inc.)** 05:08 Oh, no, I mean the J6.
**The IBM one, from… Nikola Grcevski @ Grafana / OpenTelemetry** 05:13 JDK6, yeah.
I think JDK6 and IBM would have this. I mean, I worked on that.
**Michele Mancioppi (Dash0 Inc.)** 05:19 that.
**Nikola Grcevski @ Grafana / OpenTelemetry** 05:20 Stupid thing, so… laughs.
**Michele Mancioppi (Dash0 Inc.)** 05:23 And the Java agent does not work there because the bytecode instrumentation is.
**Nikola Grcevski @ Grafana / OpenTelemetry** 05:29 Right, right. But so what I mean by that is that I need to detect this Java of some kind.
something that could potentially load it, and then I can actually find the JVM version. And if the JVM version, I can find it, I added J9 support, because J9 is the most complex.
Because they don't actually have a single symbol that says the version, they have the JDK version, they have the J9 version, they have the Linux version for it, and And so it's messy, but I did add J9 support.
Umm.
So I couldn't find the J nine JDK six build. So an old IBM build. I couldn't find one. I had to sign up, I guess for IBM.
some something support, and then they'll give it to me. They don't give it out. I couldn't test with it.
I don't know if anybody has an idea how to get it, but… For the OpenGen9, the ones that actually is available, I added support for that.
**Michele Mancioppi (Dash0 Inc.)** 06:29 Yeah, but OpenJ9, they had replaced on Temura, and I mean, it's a very different beast, right?
**Nikola Grcevski @ Grafana / OpenTelemetry** 06:36 Yeah, so I don't know how we get access to that bill.
**Michele Mancioppi (Dash0 Inc.)** 06:40 I'm also fine to say that if it's impossible to get access, then okay, then it's not supported.
**Nikola Grcevski @ Grafana / OpenTelemetry** 06:48 I did find old JDK, from Oracle that somebody posted for vulnerability purposes, so there's even a Docker image, so I was… I was able to use that one in the Docker test. But the only one I want to point out is that it's… Like, the shell, actually, I realized, defeats the .NET detection as well, because we will eject the .NET Actually environment variable for the profiler in the shell, and then it will pass it down. So whatever we find is the .NET version is now and rejected. Yeah, it's pointless because the environment variable is gonna get passed down no matter what.
**Michele Mancioppi (Dash0 Inc.)** 07:29 Yeah.
**Bastian Krol (Dash0 Inc.)** 07:30 So, this, this, this double instrumentation to… because it's, it's the, the init, or the entry point is a shell, that, that has come up in the past as well. I think that was… I don't know in which context. I think that was a major headache when we… Still had a different approach.
Like, not… not, overriding… Or not setting the environment variables the way we do right now, so… This summer rings a bell.
But for .NET… You said, you said, yeah, if you can find what is the parent process and market for .NET, it is kind of… Isn't it easier if we just say if… It's already set and this is a .NET process where we don't want to set it because it's too old. We could just compare the values.
**Nikola Grcevski @ Grafana / OpenTelemetry** 08:31 Yeah, yeah.
**Bastian Krol (Dash0 Inc.)** 08:33 If it's exactly the value that we would set, then it's probably safe to assume that it's.
**Nikola Grcevski @ Grafana / OpenTelemetry** 08:38 Yeah.
**Bastian Krol (Dash0 Inc.)** 08:38 have come from the cell double instrumentation layup.
**Michele Mancioppi (Dash0 Inc.)** 08:43 I have a proposal that is a breaking change, and we are still in time to do this.
And it is the following.
When we have in the configuration a minimum required version.
Then we must have a positive detection for the runtime.
And not add it to any process.
So, if it's… if you want .NET, at least 8, unless we're sure it's .NET 8, then we don't have it.
**Nikola Grcevski @ Grafana / OpenTelemetry** 09:15 Okay, yeah.
**Bastian Krol (Dash0 Inc.)** 09:17 That's a new requirement for us, specifically. For us, yeah. Yeah, yeah, yeah. That, that, I think, I mean, that's the direction we're moving here, so, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 09:24 Yeah, I think… I think that's actually a good idea. I mean, it's not how we behave right now. We're sort of… we're gonna try our best to find the version. If we find it and detect that it's old, then we're gonna be, like, not do it. But if we, for some reason, found something corrupted, we couldn't parse the version, we just say, okay, well, let's hope it works.
Yeah.
**Bastian Krol (Dash0 Inc.)** 09:45 Or fail close, that is the other alternative, like, but that's a design decision.
**Nikola Grcevski @ Grafana / OpenTelemetry** 09:51 Yeah.
So I agree with you.
**Michele Mancioppi (Dash0 Inc.)** 09:56 I'm having a very similar, need in the work for the automatic instrumentation for PHP.
Where… You break like a brick.
older versions of PHP, so you need to have a positive detection.
**Nikola Grcevski @ Grafana / OpenTelemetry** 10:14 Yeah.
**Michele Mancioppi (Dash0 Inc.)** 10:14 So I think, and honestly, when Bastian and I were first doing this version of the Injector, this technology back in DevZero, we settled on setting the environments variables as spray and pray because we were like, maybe we actually don't go and try to support every single runtime specifically.
But if we're getting there, then maybe we do it.
**Nikola Grcevski @ Grafana / OpenTelemetry** 10:38 I mean, for Java, it's deadly, right? I mean, there's nothing you can do. I thought about it, like, I even thought of, like, maybe I can write a Java 6 agent that somehow I preload, and then that somehow loads the JDK, and I was like, no, that's just not gonna work. I mean, it's just gonna be… Yeah, the class incompatibility is just deadly. As soon as it touches it, it just says, nope, I won't start.
**Michele Mancioppi (Dash0 Inc.)** 11:02 Yep.
**Nikola Grcevski @ Grafana / OpenTelemetry** 11:02 So, Bastian, I agree with you that the .NET is easier to do with, sort of, we know that it's us, and it matches exactly the string we have, so then we can just say, remove it for the child subprocess, once it's not compatible. That's the missing piece, and I think we should add that.
But for Java, I thought, like, I mean, people can modify tool options in the script itself. They can add stuff to it.
And then we have to go look, parse the options, and find us, and then take us out.
That's another.
**Bastian Krol (Dash0 Inc.)** 11:32 I mean, we have to… we have to pass tool options and amend it, or prepend ourselves anyway, so… Nikola Grcevski @ Grafana / OpenTelemetry 11:41 So maybe you're right, maybe that's a better way. I… I can look into that. I mean, if… if that's… rather than me kind of guessing that it's LibJLI must be there, I can just say, did somebody add this?
And it's exactly us, the same version that we're about to set.
**Bastian Krol (Dash0 Inc.)** 12:01 I think it's maybe worth looking into, although I must say, the decision to not detect which runtime it is, and just throwing just all of it at it, and… Hope for the best. It mainly came from the fact that we never had a good, reliable way of detecting the runtime.
If that is now different for Java, and that is a reliable mechanism, I mean, that also has value in itself, I'm… It's more complicated, but I mean, we had a couple of other design decisions, I think, where we said, yeah, it would be great if we would know that it is Node.js, Ruby, whatever, but we can't reliably tell.
**Michele Mancioppi (Dash0 Inc.)** 12:51 example.
**Bastian Krol (Dash0 Inc.)** 12:52 It's both good and valid approaches, I think.
**Michele Mancioppi (Dash0 Inc.)** 12:57 Yeah, I've always found an item of last resort, the fact that you set all the environment variables, because there is… a clear cognitive dissonance when you print the environment of Python, and you see Java under… underscore options and node underscore options, yeah?
**Nikola Grcevski @ Grafana / OpenTelemetry** 13:16 Yeah.
**Michele Mancioppi (Dash0 Inc.)** 13:17 So.
**Bastian Krol (Dash0 Inc.)** 13:18 That's… that's… that's one of the things. I think it's the less… important part of that, maybe. I've not seen any complaints about that, but yeah, sure, it also plays a role.
**Michele Mancioppi (Dash0 Inc.)** 13:32 But the moment that somebody notices, they're gonna scratch their heads really hard for a bit.
**Nikola Grcevski @ Grafana / OpenTelemetry** 13:36 Yeah, what are you guys doing? Yeah, sort of thing.
**Jacob** 13:38 I mean, there's so much that can be done in that.
**Michele Mancioppi (Dash0 Inc.)** 13:40 What's happened to this process?
**Nikola Grcevski @ Grafana / OpenTelemetry** 13:43 What happened?
Yeah, I mean, if we want to strengthen this, I think it's possible. This is, like, I mentioned in the comments here, it's not perfect.
I sort of had vaguely remembered that people did this alternative JVM and I looked it up and I wasn't dreaming about that. So that created a complication.
that I just decided I'm not going to support it, because apparently, I mean, OpenJDK, you can supply… you can run a Java 6 launcher and tell it, do not load my Java 6, load this alternative JVM path.
that's sitting over here, and will load Java 8 instead. But you can do the vice versa. You can run the Java 8 launcher and tell it to load the Java 6 VM.
I see.
**Jacob** 14:29 I think that in these cases where you have a user advanced enough to, like, flag these options, they should also be advanced enough to configure their instrumentation versions. Like, I don't think that we can support, like, every… We cannot always be perfect with auto-instrumentation, and you have to expect that a user that is, like, already outside of the happy path of their language is also willing to do the work to do instrumentation.
Like, otherwise, it is just way too complicated, as you're saying.
**Bastian Krol (Dash0 Inc.)** 14:57 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 14:57 Yeah.
**Bastian Krol (Dash0 Inc.)** 14:58 I mean, I wouldn't take that as a general argument, that's often different persons, the one who writes a Docker file with his option, and the one who runs the stuff, but… but for this specifically, yeah, let's not support that, that's totally… Nikola Grcevski @ Grafana / OpenTelemetry 15:13 Yeah, because I thought, okay, yeah, to get that one to work, I have to parse the options, and now… then I thought, okay, but Java C uses dash J, and then the dash X after, and then I'm like, where does this stop? Like, I can't… Like.
Okay.
Then I have to support all the tools, options, and yeah, and then…
**Jacob** 15:33 It is never ending.
**Nikola Grcevski @ Grafana / OpenTelemetry** 15:35 Yeah.
**Jacob** 15:36 It's a never-ending list.
**Nikola Grcevski @ Grafana / OpenTelemetry** 15:40 So yeah, take a look. I mean, I can, I can work on a POC to see if I can actually remove it from the options.
Instead of… If it was added by the show.
So if this Jli, I couldn't find one where it couldn't work.
to be honest, but that maybe my research wasn't. I mean, I thought, what other Jvms I know there's a tornado Jvm. Vm. That can run Java. But I don't know if that actually supports loading agents. Jack, do you know? Have you heard of that?
**Jacob** 16:13 6.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 16:14 Haven't heard of it, sorry.
**Nikola Grcevski @ Grafana / OpenTelemetry** 16:16 I don't like, from your experience, people come in and using hotel Java, like, have you heard of any bizarre VMs? I mean, I, I mean, hotspot, obviously grow, the non-native, the native is pointless. It makes it a binary. So, Azul, I know they have two JVMs, one is the Zulu, which is an OpenJDK clone, that one is OpenJDK. Then they have Zynq, which now they call Prime, apparently. That one I covered.
That's their own, they build and pitch as a higher performance, something that is better performing than OpenJDK, And then IBM with their J9.
**Michele Mancioppi (Dash0 Inc.)** 16:58 Technically, there's a… The sub-JVM, but it's… We're never gonna come across it.
**Jacob** 17:05 There's another, like… sorry, Mika, go ahead.
**Michele Mancioppi (Dash0 Inc.)** 17:09 And I'm not talking about the OpenStop machine, I'm talking the sub-JVM of your… Nikola Grcevski @ Grafana / OpenTelemetry 17:15 Okay.
Tim?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 17:17 So what's the behavior if you're unable to detect the Java major version? Like, if you run through this.
John E. this logic, and, you know, it's… you reach a case that you haven't considered.
**Nikola Grcevski @ Grafana / OpenTelemetry** 17:32 Yeah, okay, so there's two things.
**Michele Mancioppi (Dash0 Inc.)** 17:34 Because it did this IPO, it raised debt shortly afterwards. It has something like 90 billion.
Absolutely.
**Nikola Grcevski @ Grafana / OpenTelemetry** 17:40 Yeah, sorry.
**Michele Mancioppi (Dash0 Inc.)** 17:42 I'm overloaded, sorry.
**Nikola Grcevski @ Grafana / OpenTelemetry** 17:43 Yeah, yeah.
I… so there's two things.
One thing is detecting that we're at some Java.
And the second thing is detecting, can we find the major version?
So, if we cannot find a major version, I just say, let it go, which has been our… sort of approach until now. If you can't find a version, assume that it's okay.
Which means any weird JVM that build that has some special thing I haven't thought of that we couldn't discover the version, it will load And we will not actually detect.
That is some.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 18:18 Not actually inject, you mean, or not.
**Nikola Grcevski @ Grafana / OpenTelemetry** 18:19 It will inject, it will inject, it will inject.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 18:21 So the default is to inject if we don't if we can't determine that it's unsafe to inject.
**Nikola Grcevski @ Grafana / OpenTelemetry** 18:26 That's right. However, the one thing I added, which sort of deviates from our current behavior so far, is that I need to detect its Java to even Let it inject.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 18:35 and.
**Nikola Grcevski @ Grafana / OpenTelemetry** 18:37 And I say, how do you detect that something is Java?
So I was like, well, it must load the Java launcher, the one that can actually accept this.
agent argument. I don't know what else could it be like, but maybe somebody's written a different Jvm. With different launcher. That's not libjli.so.
And I won't be able to detect it.
**Michele Mancioppi (Dash0 Inc.)** 18:59 Maybe not.
**Nikola Grcevski @ Grafana / OpenTelemetry** 18:59 Low than agent, yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 19:02 I just… I just wonder if philosophically we should, like, invert it. Like, if the goal here is safety, like, you know, the opposite of what you're saying would be, don't inject until we know it's safe to inject.
And, like, maybe it's more reasonable to try to detect the situations that we know for a fact are safe to inject, and treat that as, like, sort of, like, a predicate that's a moving target as we learn more. So, like, we know Java 8 Plus and these particular JDKs.
are compatible.
And, like, we express that in a predicate. And if somebody comes along and says, like, hey, I'm using the Injector, and I'm using, I'm using this, like, Java runtime, and it's not working, because it's not part of that predicate, then we can update it.
But, like, you know, I feel like… is that… is that the better route than the opposite, which is like, hey, there's some old esoteric version of Java out there, and the injector is injecting, and it's crashing it? Like, what's… what's the lesser of the evils?
**Bastian Krol (Dash0 Inc.)** 20:10 And it's a hard question, because, the… the… if you take the safer route, and break people less.
The downside of that is that it results in a situation where you just don't have telemetry, and you don't know why, and you don't even know where to look. If it crashes the process.
At least that's a very strong signal, and you find it pretty much immediately. But it's a really hard trade-off.
**Michele Mancioppi (Dash0 Inc.)** 20:41 This is why my proposal is actually to implement the safe behavior.
Azok team.
When there is the additional configuration setting a minimum runtime version.
**Nikola Grcevski @ Grafana / OpenTelemetry** 20:55 Hmm, okay.
**Michele Mancioppi (Dash0 Inc.)** 20:56 That is my proposal.
**Nikola Grcevski @ Grafana / OpenTelemetry** 20:58 Okay, so you're saying…
**Michele Mancioppi (Dash0 Inc.)** 20:59 It is a breaking change, but we're still in time.
**Nikola Grcevski @ Grafana / OpenTelemetry** 21:03 I see what you're saying. So you're saying that if you explicitly said, I want to support Java 8 and above.
Then we enable the safety checks, and then we look for just that. And if we can positively match it, then we let it go.
If not, we don't inject.
**Michele Mancioppi (Dash0 Inc.)** 21:20 Correct.
**Bastian Krol (Dash0 Inc.)** 21:22 But wouldn't we always?
Sets this minimum version in packaging, for example?
**Michele Mancioppi (Dash0 Inc.)** 21:27 Yes.
**Bastian Krol (Dash0 Inc.)** 21:28 faults, and then… Nikola Grcevski @ Grafana / OpenTelemetry 21:29 Yeah.
**Bastian Krol (Dash0 Inc.)** 21:31 Yeah, and I mean, then most users will have it, and if it's a default somewhere.
**Michele Mancioppi (Dash0 Inc.)** 21:39 Packaging is a very different beast, because the… so we have two core use cases. One is containers and Kubernetes and, you know, interaction in there, and the other is, system packages.
In the world of containers.
you have no idea what's going on, yeah? And there, I think, a valid authoring decision, since the facilities to detect crashes are way better.
I… would feel less problems in actually inject everything than if you find the JVM J6 from, from, from Held, and boom. In system packages, on the other hand, the visibility when something crashes is Ray Charles' level of visibility, right?
So there, playing safe is something that I would much better like.
**Bastian Krol (Dash0 Inc.)** 22:34 Yep.
**Nikola Grcevski @ Grafana / OpenTelemetry** 22:36 Yeah, that was the use case I was going mostly concerned about. I think Kubernetes is also mostly modern software. I mean, yeah, you can have somebody running something old, but… People worry about… Like security and vulnerabilities being patched. And so things move, at least I, I would find we, I would think we find less JDK six or, or like earlier than JDK eight and.
Kubernetes. But system packages, like, I don't know, you drop it on somebody's machine, and There's some ancient, some tool from a vendor, and all of a sudden that stops working.
**Michele Mancioppi (Dash0 Inc.)** 23:12 Tiago can speak to the amount of backflips and belly twisting we need to do in the system custom… in the site customize to avoid breaking Python 2.7, 3.0.
and other stuff of Doom that is still installed and running.
In, in boxes out there.
Like, I have… I can… I… I used to be at canonical like there is stuff there.
That was put in production.
And I was still in the kindergarten, effectively. It's… It's insane.
**Diego Hurtado (Dash0)** 23:50 Do you mean in… In packaging?
**Michele Mancioppi (Dash0 Inc.)** 23:54 Yeah, when you deploy, like, Canonical does untold amounts of money in supporting versions of Ubuntu that were released, like.
16 years ago, huh?
Because people are incapable of updating, and the more the time passes, the least capable they are of updating, because now the world is entirely different, and nothing will ever work again.
So the chances that in system packages you find some truly ancient stuff.
And bizarre stuff.
is way higher than in containers.
**Diego Hurtado (Dash0)** 24:29 Right, right. Good evening.
**Nikola Grcevski @ Grafana / OpenTelemetry** 24:32 Okay, so then I can change the PR, then, to actually have the default version be 0.
So, we don't set it, in which case… We will not run any of these chips.
And then…
**Michele Mancioppi (Dash0 Inc.)** 24:46 We always add the 12 underscore 2 underscore options, and and the internet environment.
**Nikola Grcevski @ Grafana / OpenTelemetry** 24:53 But if somebody puts an 8, then I will… ensure that we have a positive match, and if we do find a positive match, it's only then that we inject.
**Michele Mancioppi (Dash0 Inc.)** 25:04 And we inject only the environment variables for the specific language.
**Nikola Grcevski @ Grafana / OpenTelemetry** 25:10 That's right. Yeah. Yeah. For Java, like, so it will not inject Java in anything that's not, doesn't look like Java. And we're going to, yeah.
**Michele Mancioppi (Dash0 Inc.)** 25:19 If we ask, if we ask for Java 8.
and we find Java 8, we're not going to put node underscore options either.
**Nikola Grcevski @ Grafana / OpenTelemetry** 25:28 What do you mean by that?
**Michele Mancioppi (Dash0 Inc.)** 25:30 Because today, we inject the environment variables for all languages in all processes.
**Nikola Grcevski @ Grafana / OpenTelemetry** 25:35 Right.
**Michele Mancioppi (Dash0 Inc.)** 25:36 At the moment, we start building in checks to validate that it's a specific runtime.
Yeah. What's the point of adding environment variables for a different runtime?
**Nikola Grcevski @ Grafana / OpenTelemetry** 25:45 That's right, yeah. Okay, sure.
Yeah, we know for a fact it's Java. We only need to put in Java. Yeah.
**Bastian Krol (Dash0 Inc.)** 25:54 I think where we need to be a little bit cautious is to not set expectations that we do this for every runtime, so that needs to be somehow clear that this is currently only in Java, and other runtimes might or might not follow suit at some Point, if we find a good detection mechanism.
**Michele Mancioppi (Dash0 Inc.)** 26:15 No, I would appreciate the PR to also cover .NET, because that is the other language where we have an option for the minimum runtime version, and they should behave the same.
**Nikola Grcevski @ Grafana / OpenTelemetry** 26:26 So put the .NET minimum default, which is 8 now to 0, and then if you specify it, then we actually look for a positive match and only then inject the .NET and do the same thing as Java. Okay, fine. Yeah, I can switch it to that mode.
And, yeah, and then I can document… Exactly, if you use that mode, what we support.
So… how the… I mean, it already documents, to some extent, how in my current README that I added, under sectional limitations, I already document how this check is being done for dotnet and Java. But I can specifically say, now, okay, we do support. And it's tested for this open Jdk.
6 and above.
OpenGen 9, 8 and above.
Zing, whatever, GraalVM, whatever.
If you're not one of those, then… Ask for a feature.
**Bastian Krol (Dash0 Inc.)** 27:30 So is this all these different changes, Nikola, that you asked for really be in that one PR or should that maybe be follow-ups? I mean, I guess it's up for you, Nikola, to decide.
**Nikola Grcevski @ Grafana / OpenTelemetry** 27:42 I mean, if you want… Yeah, I mean, most of the code that will do detection is already there, so we can… we can review this, and you can give me feedback on that, and then we can work to change the behavior, on the follow-ups.
We don't have to release.
**Bastian Krol (Dash0 Inc.)** 28:02 sounds… Good, I think.
**Michele Mancioppi (Dash0 Inc.)** 28:06 The, kuCoin is nigh upon us.
We, we're thinking of cutting version 1.0.
Where do we stand, folks?
**Bastian Krol (Dash0 Inc.)** 28:22 After the discussion from today where we change some substantial mechanics, substantial is maybe a big word, but we might hold out on that a bit longer maybe.
**Michele Mancioppi (Dash0 Inc.)** 28:34 We might read another Kubecon.
**Nikola Grcevski @ Grafana / OpenTelemetry** 28:37 I wouldn't be you.
**Bastian Krol (Dash0 Inc.)** 28:37 You never said which one.
**Michele Mancioppi (Dash0 Inc.)** 28:39 We did.
**Jacob** 28:40 the.
**Michele Mancioppi (Dash0 Inc.)** 28:40 So, we'll continue to forget. And to be perfectly honest, like, I, you know, I was thinking about it for a bit, and I would have a very… a much better feeling to have version 1.0 the moment that there is the injector, at least in beta, inside the operator.
**Jacob** 28:57 I agree.
I also think that we should, cut, like, a candidate 1.0 beta release as well, and have that run for at least, like, a month or something prior to us doing the full.
1.0, after this is Operator SIG, and I'm going to bring it up there so that we can get that merged in.
Because I I feel confident that it's like good to merge, good to use, and Pavel has a PR that's open. I think that we should just do this, as we said, without the.
What's it called? The S390X.
need, because I just… I want to get it in, and if, like, I don't think it should block that. We'll just not want to inject in those environments.
So that'll be my discussion at the next Operator SIG, which is in now.
But yeah, that'll be the goal. I do think… sorry, before we all go, I will say that, do the CFP for KubeCon EU closes on Sunday? Did we want to try and do… something either, like, you know, a talk about Injector 1.0 for… Oh, you already submitted it?
For Groupon to use.
**Michele Mancioppi (Dash0 Inc.)** 30:08 We have one, a submission. We discussed it a few times in the SIG and in the channel.
**Jacob** 30:15 I must have missed that.
**Michele Mancioppi (Dash0 Inc.)** 30:17 We have one with, let me check… Oh.
Wait, I was supposed to pass it over to Bastian, I passed it over to you, right?
**Bastian Krol (Dash0 Inc.)** 30:31 Yeah… no, no, to me,
**Jacob** 30:34 So.
**Bastian Krol (Dash0 Inc.)** 30:35 You said you wanted to submit it under my name, or something weird like that?
**Michele Mancioppi (Dash0 Inc.)** 30:41 I.
**Bastian Krol (Dash0 Inc.)** 30:42 anything.
**Michele Mancioppi (Dash0 Inc.)** 30:43 I have to submit it again, yes.
**Bastian Krol (Dash0 Inc.)** 30:45 But if you want me to submit it, that's also fine, but then please let me know, or hand over the proposal that you have, and I'll just submit it, or you submit it.
**Michele Mancioppi (Dash0 Inc.)** 30:56 I am a I… No longer… No, it works.
**Bastian Krol (Dash0 Inc.)** 31:04 Let's take that offline, we can discuss that between the two of us, I guess.
**Jacob** 31:09 I realized why I didn't see this. The thread was on my birthday, and I was not looking at my laptop.
**Bastian Krol (Dash0 Inc.)** 31:16 That's very good.
**Jacob** 31:17 Yes,
**Michele Mancioppi (Dash0 Inc.)** 31:19 Antoine.
**Jacob** 31:20 make.
**Michele Mancioppi (Dash0 Inc.)** 31:21 Antoine, I'm going to withdraw that submission, and then another one is filed with Bastian and, And whoever wants to be on it, you know it.
**Nikola Grcevski @ Grafana / OpenTelemetry** 31:31 I mean, two people max.
Unless one of us is a woman.
**Antoine Toulme (Splunk Inc.)** 31:34 No, I'm actually at my… for Cape Corneo, I'm at my max submissions, so don't worry.
**Bastian Krol (Dash0 Inc.)** 31:40 If anyone wants to join, otherwise I'll stop it alone, just let me know.
**Nikola Grcevski @ Grafana / OpenTelemetry** 31:45 Okay. Yeah, what's the proposal? I'll join you.
I.
**Bastian Krol (Dash0 Inc.)** 31:51 I'll ping you on that.
**Nikola Grcevski @ Grafana / OpenTelemetry** 31:52 Okay, okay, I want to see if it's something I can contribute, then I'll join you, yeah.
**Antoine Toulme (Splunk Inc.)** 31:57 Awesome. Cool. Good. Have a good one.
**Bastian Krol (Dash0 Inc.)** 31:59 Okay, see you around.
**Michele Mancioppi (Dash0 Inc.)** 32:02 Bye.
