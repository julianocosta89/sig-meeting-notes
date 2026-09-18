SIG: Injector SIG
Date: 2026-09-17
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Jacob A** 00:56 Hello.
**Bastian Krol (Dash0 Inc.)** 01:01 Hello!
**Jacob A** 01:04 I don't know, if you have anything on the agenda. Let me double check.
**Bastian Krol (Dash0 Inc.)** 01:09 Yeah, that'll…
**Jacob A** 01:10 Go back to something.
**Bastian Krol (Dash0 Inc.)** 01:11 Jack, exactly. Maybe we would wait one more minute or so.
Anyone else shows up? Yeah.
**Jacob A** 01:19 Is Michele gonna be here? Or is he out?
**Bastian Krol (Dash0 Inc.)** 01:23 I should know, but I don't know.
**Jacob A** 01:28 Was he at the packaging SIG right before this? I wasn't there, so I wouldn't know.
**Bastian Krol (Dash0 Inc.)** 01:32 So, no, I also wasn't at the packaging.
**Jacob A** 01:35 Oh.
Jack, were you?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 01:38 I don't… I don't go to that, SIG.
**Jacob A** 01:42 So maybe they're still in there. Just gonna maybe give them, like, more minutes.
**Bastian Krol (Dash0 Inc.)** 01:49 I could take a… I'll hope over there and see if they are still…
**Jacob A** 01:53 Okay.
**Bastian Krol (Dash0 Inc.)** 01:54 on…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 02:02 Yeah, they, they are over there.
**Jacob A** 02:05 There, oh.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 02:05 I can just tell because he's on the attendees list along with… Couple of other people.
**Jacob A** 02:12 Yeah.
**Bastian Krol (Dash0 Inc.)** 02:43 Yeah, the discussion over there still seems to be quite lively. Didn't look like they… so I'm not sure when they will… Show up.
Should we, should we get… Started, or shall we give it more minutes?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 03:07 Michele just commented in the channel saying, we're running late in packaging, implying, like, that they, you know, they're aware they're running late and are intending on not heading over, so…
**Jacob A** 03:17 You can just wait for them, then.
**Bastian Krol (Dash0 Inc.)** 03:19 Okay, that's fine.
Right.
**Nikola Grcevski @ Grafana / OpenTelemetry** 03:22 Hi.
But I can just think it was dragging on, so Michele is coming. I decided to do yours.
**Bastian Krol (Dash0 Inc.)** 03:30 Yep.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 03:32 It's always hard to be the… the time police.
**Bastian Krol (Dash0 Inc.)** 03:43 Actually, I just hopped into the packaging for one quick peek to see if they are on, and it was quite a crowd today. Lots of folks there.
**Jacob A** 03:54 What's the discussion?
**Bastian Krol (Dash0 Inc.)** 03:57 Pardon?
**Jacob A** 03:58 What are they, chatting about?
**Bastian Krol (Dash0 Inc.)** 03:59 To be honest, I was in there live for 15 seconds, not enough to actually understand what the topic is. Sorry.
**Nikola Grcevski @ Grafana / OpenTelemetry** 04:08 of the packaging thing?
**Bastian Krol (Dash0 Inc.)** 04:10 Yep.
**Nikola Grcevski @ Grafana / OpenTelemetry** 04:10 Yeah, I mean, a number of topics, I think. I think there's a lot of talk about adding PHP to an injection.
And how are we gonna split that?
I think SolarWinds, somebody from SolarWinds is working on that, wants to add PHP as an instrumentation target, primarily targeting operator, I think, at the moment.
But, Nikola believed that if we added the support in the injector, it would be easier.
And the rest of it is just about… Figuring out… packaging around, you know, differences between the Ubuntu and Debian, and Getting permissions for packaging and pushing to repositories and whatnot.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 05:01 Yeah, my topic here is probably gonna relate to that at least a little bit.
I'm trying to codify the… you know, we say things like, you know, Python, the auto-instrumentation can crash your app, it's not safe.
**Nikola Grcevski @ Grafana / OpenTelemetry** 05:17 When you say things.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 05:18 things like, hey, we're worried about that for Ruby as well. But, you know, we're sort of imprecise with our language.
And we're not… there's different types of failure scenarios that are not all the same level of severity.
And so, you know, what I've been trying to wrap my head around is, like, what are the different classes of how an auto instrumentation can fail? Like, put names to them, put words to them that are commonly applicable across all the languages, and then try to create, like, a catalog of examples of those, so that, you know, if we want to go to a language like, Python, or Ruby or PHP, and be like, hey, you know, we think your auto instrumentation needs to be more safe, this is what we think… these are the problems we've identified, you know, we can have reproducible examples, we can have, like, words to put to them, and, you know, a more nuanced discussion than just, like, hey, Ruby breaks your app.
So…
**Bastian Krol (Dash0 Inc.)** 06:19 Yeah, I think that that's really good. I think that that's a good… endeavor to have that. Also, to have just reproducers on their own, like.
everyone knows that, that a Python version conflict can break, but having it exactly in code, I think that's something that's worth having.
**Nikola Grcevski @ Grafana / OpenTelemetry** 06:45 I meant to ask, do you guys believe Node.js is okay? I mean, I… I think in all experiments that I've done, seems okay if you have its own instrumentation, and you add the auto instrumentation on top, but I don't know if hooks are doubled. I haven't actually checked for performance.
**Bastian Krol (Dash0 Inc.)** 07:01 Yeah, I know, I never… I mean, we had that… we discussed that via the M, I think, a couple months ago, and I never found the time to really look into it, so your experiments so far are probably the best source, information we have.
**Nikola Grcevski @ Grafana / OpenTelemetry** 07:16 There's no duplicate instrumentation, but seems to double the hook.
**Bastian Krol (Dash0 Inc.)** 07:21 We can duplicate spends, from a customer at some point.
**Nikola Grcevski @ Grafana / OpenTelemetry** 07:26 I see.
**Bastian Krol (Dash0 Inc.)** 07:27 That was with… the Injector, and they had their own instrumentation already, but… Nikola Grcevski @ Grafana / OpenTelemetry 07:34 I see. Okay, so maybe… Oh, let's hold…
**Bastian Krol (Dash0 Inc.)** 07:37 Yeah. It could also be that it's just for some instrumentations and not for others, or that there can be so many different scenarios.
**Nikola Grcevski @ Grafana / OpenTelemetry** 07:47 You're right.
**Bastian Krol (Dash0 Inc.)** 07:48 But, I mean…
**Michele Mancioppi (Dash0 Inc.)** 07:48 Oh, goodness.
**Bastian Krol (Dash0 Inc.)** 07:49 good if it…
**Michele Mancioppi (Dash0 Inc.)** 07:50 I'm super interested.
**Bastian Krol (Dash0 Inc.)** 07:51 Hmm… Generally, and… Nikola Grcevski @ Grafana / OpenTelemetry 07:54 Damn.
**Bastian Krol (Dash0 Inc.)** 07:55 Immediately, that's also okay.
That's what we're talking about.
**Michele Mancioppi (Dash0 Inc.)** 07:59 It sounds super interesting, which double spans.
**Nikola Grcevski @ Grafana / OpenTelemetry** 08:03 Yeah, I was just asking if we think that… I mean, I know Node.js, if we double instrument, does not actually break the application?
But… I was just discussing if it's 100% safe. This is a double instrument in some cases.
**Michele Mancioppi (Dash0 Inc.)** 08:18 It depends on the language. Trevor is SIG as well.
But, it, It depends on which technology has done the bicycle maniculation. For example, the neuralical agent was infamous for being incompatible with any other Java agent.
If… nowadays, we're all using BiteBuddy, which is… and the advice is mechanism of Bite Body, which is… It's solid tech, comparable with… Node.js when you remember, actually, to change the… what is this in the closure. So, I have not heard of incompatibilities among agents in a long while. The, I've seen a number of times the Datadog and the OpenTele agent tracing each other, which is always very fun.
Other languages, not so much. For example, I'm… I think that the technology that we use to do PHP would not work too well with multiple instrumentations, but I've not tried to break it that way.
Python is also more or less okay-ish.
It's, it's of course a terrible experience, but that's definitely a topic.
**Bastian Krol (Dash0 Inc.)** 09:31 Let's… let's go back to the… to the topic that… that Jack raised, which is on the agenda. Do you want… yeah, no, exactly.
**Michele Mancioppi (Dash0 Inc.)** 09:40 Oh, perfectly.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 09:40 Yeah, so it's kind of all intertwined with this, so, you know, Michele has… this spec PR open, which is specifying criteria for automatic injection. And we talked about this at the Spec SIG this week, but I called attention to this specific spot. Like, I want… I want the language maintainers and the folks that are maintaining these auto-instrumentation packages to be aware of this and to provide their feedback, because this is… This is an important clause in here. So, you know, on an unsupported or incompatible runtime, it must fail-safe, it must not crash.
the application. So this is like, you know, auto instrumentation should do no harm.
And, you know, we say things like, hey, Python can break your application, and we have similar concerns for PHP, for Ruby, you know, we're talking about a different failure mechanism for Node, like whether it double instruments, but, you know, at least people sort of be… seem to be in agreement that it won't break your application.
But, you know, I think this comment here underlies the tension. You know, Aaron just comments, like, do you have a specific one in mind? Python auto-instrumentation tends to fail-safe.
That's, like, sort of contradictory to our narrative. So, like, what's going on here? And I think the issue is that we're not… we don't have, like, a language established for what failing safe means, for what different types of crash scenarios can occur.
**Michele Mancioppi (Dash0 Inc.)** 11:08 Sorry. Python failing safely makes me laugh, because there is no failure more catastrophic than trying to inject Python 2.7.
It's… that's really funny.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 11:20 Yeah, so, so anyways, like, okay, I want to get some specifics back to Aaron, right? Like, I want to create some reproductions of the types of, like, failures that are in our minds, or that we've interacted with with customers, and put them in front of Aaron, you know, with a common set of language that we can all, like, agree on.
And then, you know, that creates, like, a target that Python can go and, like, you know, iterate against and try to solve.
**Michele Mancioppi (Dash0 Inc.)** 11:47 So, it's something that I've seen in the previous, in the previous call, in the packaging SIG, comes in directly from the PHP instrumentation.
And, effectively, like, he's working on Injection for Pryor, for HP.
And, he had not realized that when you inject PHP instrumentation into other things, you don't know if the version of PHP is compatible.
And the same problem is for Python. So, try to inject PHP auto-instrumentation in PHP 5, it's probably going to lead to very interesting results. Injecting the PHP SDK into, into the Python SDK into Python 2.7, it leads to catastrophic failure.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 12:33 Yep.
**Michele Mancioppi (Dash0 Inc.)** 12:34 Those are definitely things to try. Injecting, probably the other instrumentation gem for Ruby in version 3.2 and below, it's also probably very, very interesting for all the wrong reasons.
you inject the, the .NET SDK using the wrong binary for, collecting the process metadata, so the… the little bit for which we had to devise the, is it, GLIPC or… or muscle C?
And stuff doesn't work well. You get a whole bunch of strange errors, and it is incomplete. At least the last time I tried a few years ago.
Java, I don't know of any incompatibility like that. It'll just track along like a champ.
Node should not break, although… Yeah, no, no, it doesn't break me. We do not have binary dependencies that I'm aware of.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 13:26 So… If you could do a brain dump of those specific scenarios you laid out in this Slack channel, this Slack message, or Slack thread that I've linked here, that would be fantastic.
already embodied, and, like, a couple of them, though, like, you know, I can jot down notes quickly. I can go watch the recording of this to, like, you know, pull out those specific things, but that's exactly what I'm interested in. And, I guess what I can… what I want to show you all is, So, like.
what I've built, sort of, like, scratched together really quickly. So, there's this, there's this repository out there called Semantic Inventions Conformance, and it's new, and what they're trying to do is, you know, test whether different language library combinations past semantic conventions. And it was a convenient starting ground for me for this type of thing, because it has harnesses that allow you to, like, spin up many different, like, you know, app setups, like runtime language versions, instrumentation versions, whatever, and then, you know, run a particular set of scenarios against them and make assertions against the outcome. Like, you know, what was the exit code of the app? Like, did it emit telemetry?
what was its log output, things like that. So, like, I don't think that this is necessarily the, like, a final home for this, because, like, you know, it's about semantic conventions, and we have different goals in mind, but, you know, I just kind of cherry-picked its harness.
And what I did was I… I set up, like, a new kind of class of scenarios to test, and so far, I'm just looking at the Python language.
And, let's go down here to this vocabulary at the end. So, there's… these are the different outcomes that can happen. There's a successful instrumentation. So, the auto instrumentation attaches, and telemetry flows, and the app is happy. Like, that's the happy path, right? We all understand that.
Then there's silent degradation. So, this is like the instrumentation doesn't install, but the app, it doesn't crash as well.
So this is actually, like, okay. You know, this is, like, we didn't do any harm to the app, but we could do better. Like, the instrumentation, maybe it could be written more flexibly to account for more versions.
Or maybe it could degrade with a warning that is actually observable, so, like, you know that the instrumentation short-circuited.
So that's the next category here, loud degradation. So, like, the instrumentation didn't install, but it warned you loud and clear, so there's something actionable that you can go do, or that the instrumentation authors can go do, one or the other.
**Michele Mancioppi (Dash0 Inc.)** 15:58 I have some strong opinions about… so I love the distinction between silent degradation and loud degradation.
the, I think there is a third category in between, where it is an understandable silent degradation.
Where there is some cryptic warning that you'll know what it does, which is the more common use case.
In my experience.
Because when you say loud degradation, I expect a curated, understandable message.
with, ideally, a reason why. It's, it's something like the idea. For example, that's what we do in Python in the packaging SIG with the site customize. We tell you, yeah, love, the version of Python doesn't work, or the dependencies that you have are not compatible with the ones of the SDK.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 16:50 Yeah, yeah, totally. Yeah, like, there's, you know, I think those are various flavors of, like, like, of what we want, right? So we want to… we want to have a warning that indicates that instrumentation installation failed, and we want that warning to be actionable, to contain, you know, all the details, and not be cryptic.
**Michele Mancioppi (Dash0 Inc.)** 17:09 Yes.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 17:10 Go ahead, Bastian, sorry.
**Bastian Krol (Dash0 Inc.)** 17:13 No, no, yeah, I think there are, I mean, do you want to elaborate on crash first? And I also have some more potential categories or classes, maybe.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 17:26 Yeah, yeah, so Crash, so far, the two kind of subclasses within crashing is, like, you know, the… there's a dependency conflict in the, in the OpenTelemetry SDK. This is the one that… the popular one is, like, the Python's protobuf and gRPC dependency, which very often, like, conflicts catastrophically with the app's gRPC or protobuf dependency.
And, like, you know, the app crashes. Another version of this would be, like, this is, like, maybe a subversion of this, but, like, it's, like, the runtime, the runtime of the language conflicts, so, you know, it's a Python version that isn't supported by the auto instrumentation, and it crashes.
Class B of crashing is, like, there's bugs in the instrumentations themselves, which, like, so the instrumentation installs, and it's not until something at runtime occurs that exercises the instrumentation in a way that it crashes.
So these… Class B, I called this out separately because it's really hard to detect at initialization time, and you might… and in some cases, I think I'm starting to… you know, come to the conclusion that, you know, you might be able to reduce Class B, in a language like Python, but I don't think you can structurally eliminate it without, like, extreme trade-offs. Like, big performance degradations and things like that. So, like.
Anyways, these are the classes of things that I've identified, you know, and I've created different scenarios that embody each of these different, you know, cases, and the popular ones that we know of and talk about, and so they're now reproducible, and you can see them. But Bastian, like, going back to you, kind of, do you have any other kind of classes of failures?
**Bastian Krol (Dash0 Inc.)** 19:18 Yeah, so, It's basically the ones that are also named examples for in the Slack thread, so one would be partial instrumentation, which is also hard to debug, and maybe that's why it's worth its own class, like, somehow, instruments, only partials, you only get… some spans, but not others, or only metrics, but not spans, something like… like that. It's hard to understand, because if you look into your observability system, you see that something is coming, but it's not what you expect, so that's maybe one… one thing.
**Michele Mancioppi (Dash0 Inc.)** 19:58 Yes, and there is, the… so this is, It comes in two flavors. One is you instrument the library partially, because maybe the new version is changing the internal logic. The other one, which is, a super interesting one to troubleshoot.
is, you break trace context because the mechanism from the, the libraries of the runtime are not compatible. The example I have in mind is, coroutines in Kotlin.
Where, for example, at this time, it took us forever to get it right.
Where the instrumentations put a touch, but the trace would be broken, and the incompatibility was not with the light rays that were instrumented, but with the underpinning runtime mechanics.
It's a fabulous.
**Bastian Krol (Dash0 Inc.)** 20:48 Yeah, for the goal that we have here, it probably makes… it might make sense to… to throw a couple of things into the… into a wider bucket, like, for example, this could be just partial instrumentation, even if it has many different flavors. I'm also… maybe also for the crash. If it crashes the app, it crashes the app. The one is… the one… the two here are very different, and harder to… to handle, but for that common vocabulary, maybe… it crashes is… is enough, but that… that's… I,
**Michele Mancioppi (Dash0 Inc.)** 21:25 I have some, strong opinion loosely held.
About, so for me, the, the bugs and incompatibilities, between runtimes and applications.
From the end-user perspective, are different, because What you can do about it tends to change.
I mean, containers, cool, you've got the wrong JVM, maybe you can change it, maybe not.
If the reason is that, the FIPS module you have for the JVM is breaking your stuff, then good luck, you're not gonna change that. But if the code is, if you change… if you can fix it by changing the library that you use to talk to Kafka, maybe that works.
So I would, in my head, there is a strong difference between incompatibilities against the runtime versus against libraries and the application code itself.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 22:22 The distinction I make between these two types of crashes is, like, could the auto instrumentation maintainers have done something to structurally prevent it or not?
**Bastian Krol (Dash0 Inc.)** 22:36 Because that's the target audience for this vocabulary, right? It's not to talk to end users, but to SAK also, so that's what it needs to be…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 22:46 Yeah, I want everybody to be thinking the same way, like, you know, trying everything that they can to do, within reason, to do no harm. And right now, I don't think everybody believes that within OpenTelemetry, so…
**Bastian Krol (Dash0 Inc.)** 23:00 Yeah, that's a good point.
I mean, from the perspective of SDK maintainers, it's also, they come maybe from a different… point, like, yeah, we start out with manual instrumentation, and users know the runtime version, and they know what is compatible, and set it up specifically for that one app, and that's just a very different scenario from auto instrumentation, so that's where that gap comes from, I think, historically.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 23:33 Totally, totally. We need to get everyone, like, thinking that, you know, there's going to be a tool that's going to apply OTEL Auto instrumentations across entire workloads, across entire fleets.
And, you know, there's not somebody that's going and installing them on an app-by-app basis, and incorporating it into their build, and getting build time failures that they can, like, iterate against and fix.
you know, if you're installing it across the entire fleet in production, and if an app breaks in production, then, you know, it harms OpenTelemetry's reputation, it harms our ability to, like, have this story that, like, you can install OpenTelemetry, like, widely.
So,
**Michele Mancioppi (Dash0 Inc.)** 24:15 That is, that is one of our failure modes as a project.
Right. We, we, we, we poison our pool by, not enabling people to succeed in adopting it, or if they try to adopt it, we break their shit. That's how we fail.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 24:32 Right.
So, like, what I'm going to do with this is, like, you know, I'd love, I guess, a little bit of feedback on, you know, whether this language is directionally correct. I don't think this is going to be a permanent artifact, at least not in this form, so we don't need to belabor it too much.
But, like, if I'm missing anything conceptually, like, I guess I want to know about it. And I'm going to expand on these scenarios. Right now, I've done this for Python, and, like, you know, in my head, it'd be good to expand it to the other languages that, like, we have uncertainties about. Like, you know, I've heard some about Node, but, like, most… maybe some confidence there as well, so not really sure where that lands.
Definitely some questions about Ruby, definitely some questions about PHP, and, like, from Rob.
**Michele Mancioppi (Dash0 Inc.)** 25:18 on that.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 25:19 NET, yeah, there seems to be some questions about .NET as well.
**Michele Mancioppi (Dash0 Inc.)** 25:22 Effectively, the only language that I consider safe is Java.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 25:26 But maybe it's not as well. Like, the question is, is can you create an adversarial scenario that creates one of these outcomes?
**Michele Mancioppi (Dash0 Inc.)** 25:34 Sure, Java 7. Put it in Java 7.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 25:37 Put it in Java 7, see what happens. Like, will the app, like, you know, gracefully degrade where the instrumentation skips and the app proceeds, or will the app crash?
**Michele Mancioppi (Dash0 Inc.)** 25:44 I actually expect… That depends on the version of Bite Buddy you use, so that's gonna be fun.
**Bastian Krol (Dash0 Inc.)** 25:53 Yeah, but also, I mean, there's probably a gradient to this. I mean, if you need to make up a very contrived example with a, like, a Java version from 1999 or something, then I think…
**Michele Mancioppi (Dash0 Inc.)** 26:07 I wish.
**Bastian Krol (Dash0 Inc.)** 26:07 relevant.
**Michele Mancioppi (Dash0 Inc.)** 26:08 I wish it was contrived.
You know how many people have spoken in the last year that actually use Java 6? Not even Saturn 6.
**Bastian Krol (Dash0 Inc.)** 26:17 Yeah, yeah.
**Michele Mancioppi (Dash0 Inc.)** 26:17 It's more than fingers on my hand. It's depressing.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 26:22 Well, they didn't write those systems, they inherited them, and, you know, there's…
**Michele Mancioppi (Dash0 Inc.)** 26:27 I don't blame the individual, I blame the systems behind it.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 26:31 Yeah.
**Bastian Krol (Dash0 Inc.)** 26:32 Yeah, that somehow needs to be factored in, I think. At least it needs to be factored in to the reasonable requirements towards SDK authors.
not everything has the same priority, and not every… not working scenario.
**Michele Mancioppi (Dash0 Inc.)** 26:49 Like, Nancy American!
**Bastian Krol (Dash0 Inc.)** 26:50 likelihood.
**Michele Mancioppi (Dash0 Inc.)** 26:52 God.
**Bastian Krol (Dash0 Inc.)** 26:53 Yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 26:58 So it sounds like everybody's, like, you know, and I didn't expect anything else from this group, but people are, like, roughly aligned with this, and so, yeah, like, looking for high-level feedback and tips on, you know, specific scenarios and specific languages that you know to fail. And I can take on the task of sort of, like, curating this and putting it in a form that can be communicated in others, even if it's, like.
a temporary thing, right? Like, it'd be great to codify this someday and have like, a place in OpenTelemetry where, you know, we can… Have a conformance matrix for auto instrumentation, and, like, you know, have more confidence that for a bunch of adversarial scenarios, the, like, the auto instrumentation still don't crash apps, that they still have a decent outcome.
**Michele Mancioppi (Dash0 Inc.)** 27:48 Oh, I remember the cool one, Kafka Library for Java version, 0.10 and below.
It'll crash if you try to use the metadata to put trash context.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 28:03 I wrote it down.
So the app, the whole Apple craft?
**Michele Mancioppi (Dash0 Inc.)** 28:08 I… I don't remember, it's, there is a failure in serialization, and that depends how you catch it. That's how I remember it. And, it's… it was not… it was not just the library, it's also the version of Kafka itself, because… it was… like, if you use reversions of Kafka in the libraries, then it goes boom.
And that is one of the situations where you actually need to go and check the version of the library to decide whether to instrument it or not.
**Nikola Grcevski @ Grafana / OpenTelemetry** 28:36 Right? This is a fix to the Java instrumentation.
**Michele Mancioppi (Dash0 Inc.)** 28:42 Yes.
It's effectively a better sign to check, right?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 28:48 That's my Crash Class B.
Which is, like… You know, you can, if the instrumentation was written better, it would never happen, but maybe it's hard to add structural, checks that prevent it entirely. Like, you know, you're putting some trust in the instrumentation author to follow whatever, you know, techniques,
**Michele Mancioppi (Dash0 Inc.)** 29:09 And a couple of times, there is technically another Category of failures where the data is collected but cannot be exfiltrated.
And that happens, when, for example, there is in the application a built-in, like, a different global trace context, and then the tracers talk to the wrong one, and the data is collected, but doesn't get anywhere.
And that is a flavor of incompatibility with libraries when there are too many auto SDKs inside.
And whether or not it happens changes wildly language from language. I could reproduce it a couple of years ago in Java.
I have not tried since.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 29:57 We do have to be careful about, like, you know, how far we let this go, because, you know, you say more words and all of them get watered down. And so, like, if we… if the main message we want to convey to auto instrumentation maintainers is, like.
stop crashing apps. Like, we've got to kind of have a simplified story that is bounded around that. And once we get it to the point where apps don't crash, then we can sort of go to the higher hanging fruit of, like, hey, make sure, you know, the instrumentation always works. Make sure we fail loudly when instrumentation installation fails, or something like that, and the other things. But, like.
You know, we can't miss the main point, which is like, hey, stop crashing apps.
**Michele Mancioppi (Dash0 Inc.)** 30:39 I agree 100%.
**Bastian Krol (Dash0 Inc.)** 30:40 That's it for.
**Michele Mancioppi (Dash0 Inc.)** 30:41 I mentioned this for completion among like-minded people.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 30:46 Sure, sure. Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 30:47 Jack, there might be one model failure mode, I don't know if this… goes into your crashing scenario, but it could be just the application starts misbehaving. It's actually… it's not crashing, but it's not doing what it's supposed to do.
That is maybe more difficult to handle, and more subtle.
But… let's say this Kafka instrumentation starts to break the Kafka protocol, and messages are arriving on the other side, malformed, and then can be or Kafkas.
service crashes, not your current application, but the more receivers are.
Right. Because you're sending something that's… Wrong.
**Michele Mancioppi (Dash0 Inc.)** 31:27 Probio.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 31:28 And also, like, because those are pretty nuanced, they're hard to recreate. You need, like, a very specific bug report of somebody experiencing them in the wild.
**Nikola Grcevski @ Grafana / OpenTelemetry** 31:37 Yeah, so that I added instrumentation, and my application can no longer talk to my Kafka server or something.
**Michele Mancioppi (Dash0 Inc.)** 31:43 We are, out of time. I would like to bring up a super quick point. Jerry from the PHP, so I'm going to work with Jerry from the PHP, SIG.
To, for, defining the contract for injection auto-instrumentation.
And this could be ground zero for applying this principle here, at least. It's the next iteration for a major language that gets auto-instrumentation. It's probably going to require heavier lifting by the injector, because PHP is, one of those runtimes that is incredibly hostile to thought instrumentation, where you must have different builds based not only on the flavor of libc, but the… the SAPI sometimes, the… whether it's threaded or not, and a bajillion other silly things. So, we might end up… having to put a good chunk of PHP-specific logic in the injector.
I don't know yet.
**Nikola Grcevski @ Grafana / OpenTelemetry** 32:42 Yep, that's.
**Bastian Krol (Dash0 Inc.)** 32:42 Cool. Sounds good. I mean, sounds horrible, but sounds good.
**Nikola Grcevski @ Grafana / OpenTelemetry** 32:46 Yeah.
**Michele Mancioppi (Dash0 Inc.)** 32:47 But it's a good time.
**Nikola Grcevski @ Grafana / OpenTelemetry** 32:47 Go for all the good.
**Michele Mancioppi (Dash0 Inc.)** 32:49 That's the motto of PHP.
Bye, folks.
**Nikola Grcevski @ Grafana / OpenTelemetry** 32:54 Alright. Bye now.
**Bastian Krol (Dash0 Inc.)** 32:55 But…
