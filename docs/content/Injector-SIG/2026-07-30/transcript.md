SIG: Injector SIG
Date: 2026-07-30
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Antoine Toulme (Splunk Inc.)** 00:15 D.
Alright, maybe we can talk real quick about this discussion with, Pavel?
So Pavel is saying that we could use QMU for stuff, which he said, well, no, I don't think so.
**Michele Mancioppi (Dash0 Inc.)** 00:33 Been there than that.
Broke my legs.
**Antoine Toulme (Splunk Inc.)** 00:37 Well, I mean, in any case, it doesn't… To me, it's like, whatever, just, he's up in the PR That's interesting.
Trying to understand if he picked up from IPR? He's done it himself, okay.
So, yeah, some interesting things he's doing.
Take a look…
**Michele Mancioppi (Dash0 Inc.)** 01:10 That doesn't build for shit. Oh, it's a change, look missing.
**Antoine Toulme (Splunk Inc.)** 01:18 He's made the same changes that I've made.
**Michele Mancioppi (Dash0 Inc.)** 01:22 It runs the injector integration tests, Architecture Western NTX.
And it works.
**Antoine Toulme (Splunk Inc.)** 01:35 Yeah… Doesn't bring that much, confidence into your test now, right?
**Michele Mancioppi (Dash0 Inc.)** 01:42 No, it's terrifying.
**Antoine Toulme (Splunk Inc.)** 01:46 Yeah, I'm trying to understand exactly what's going on here, but… Our tests themselves are using Docker.
Oh, okay. So he's using a Linux for Doc.
**Michele Mancioppi (Dash0 Inc.)** 01:56 Yeah, please passing down the S390X image.
And, and the PPC Image, and that assumes that all our base images also have No, they don't express.
That's so outlandish.
**Antoine Toulme (Splunk Inc.)** 02:14 PPC64 LE does not.
really exist for Docker anyway, does it?
Like, you won't ever find anyone with a flavor… I have a Docker image for X, because X does not support Docker.
So anyway, that's a moot point, I guess, but, it passes.
No.
**Michele Mancioppi (Dash0 Inc.)** 02:38 It's a change mode to crawl in there.
And that makes me really surprised.
So, which images do we use nowadays as foundations for our integration tests?
Because I cannot believe that it works out of the box.
Hope we can see an estimate, yeah.
**Antoine Toulme (Splunk Inc.)** 02:59 It's been a hot minute.
**Michele Mancioppi (Dash0 Inc.)** 03:02 Impossible.
**Antoine Toulme (Splunk Inc.)** 03:04 That's a blur.
**Michele Mancioppi (Dash0 Inc.)** 03:05 Node.js Pool Size Lim. Does this have a, he was using…
**Antoine Toulme (Splunk Inc.)** 03:19 So, I think it's not so much the technical discussion we're having here, right? It's a discussion we've been having last week that is continued.
Which is that your stance has been.
We cannot support A390X just because… Even if we compiled it, it wouldn't be enough.
Right.
We want to actually make sure this works all the way through.
we want to be able to debug, troubleshoot. We're not… we're not in business of… Saying that things work, and then close our eyes and hope for the best.
Do we agree on that?
**Michele Mancioppi (Dash0 Inc.)** 03:54 But if it comes along and it shows the full battery of tests.
Or it can go to the box?
**Antoine Toulme (Splunk Inc.)** 04:01 Well, I say we can always punish people by making them maintain that code.
And responsible for this.
**Michele Mancioppi (Dash0 Inc.)** 04:08 You don't make people maintain code Antoine. You can blame them if they don't maintain it.
**Antoine Toulme (Splunk Inc.)** 04:14 we can make them responsible for that, and if they don't maintain it, we remove support, saying, I'm sorry, Pavel's no longer active on the project, we will no longer support S390X, because that was his baby.
And if no one shows up and takes over, we'll remove all that stuff.
I've done it before.
**Michele Mancioppi (Dash0 Inc.)** 04:35 Well, I need to try our integration tests harder, because right now, the fact that it worked out of the box.
It's so far out of the left field that it's not even funny.
**Antoine Toulme (Splunk Inc.)** 04:46 Well, we could try to run it with a random architecture, The architectures you're spacing in.
**Michele Mancioppi (Dash0 Inc.)** 04:53 I think we're not testing hard enough.
For example, do we have… is the .NET… are the .NET people even publishing things for us 1080x?
**Antoine Toulme (Splunk Inc.)** 05:07 Ew.
**Michele Mancioppi (Dash0 Inc.)** 05:08 Because what I'm suspecting is that all integration tests do not verify that telemetry is actually produced.
**Antoine Toulme (Splunk Inc.)** 05:18 Oh, was that what he's thinking?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 05:21 Did they need to verify that telemetry was produced?
**Antoine Toulme (Splunk Inc.)** 05:24 Whoa.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 05:25 You know, because when we say we support a specific architecture, what's our job? Our job is to… detect if there is, like, a version of the instrumentation for the detected architecture and, and set the environment variables to point to that version of it. And so, like, maybe they're… they're… maybe it's, like, yes and no. The integration, like, the injector is doing its job, but it's effectively, like, a no-op, because, as you point out.NET doesn't support this architecture.
But it's not breaking, it's not blowing up, so that's something in itself.
**Antoine Toulme (Splunk Inc.)** 06:06 Yep.
Take a look.
**Michele Mancioppi (Dash0 Inc.)** 06:09 I mean, that's under our OT, Injector-centric point of view of the project, sure. On the point of view of the end user.
Right. Oh, so what?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 06:19 Yeah, exactly.
Yeah, it's like, yeah, we say we support this architecture, but, you know, when you dig into the details, we don't actually support it, because there's things,
**Michele Mancioppi (Dash0 Inc.)** 06:35 Because when it does not work.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 06:38 I guess in the same way, the operator doesn't support those architectures either.
**Michele Mancioppi (Dash0 Inc.)** 06:42 I used to…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 06:43 The same reason?
**Michele Mancioppi (Dash0 Inc.)** 06:44 Last week. I used very spicy words last week, and I said what I thought about that.
Don't want to repeat.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 06:51 You know what I mean, though? The argument that you just made, like, hey, are we actually testing that the injector works with, you know, this architecture and .NET? And, you know, we said, probably not, because we know that the .NET doesn't publish a version for this architecture. So, I mean, by the same reasoning, the operator can't work with .NET and this architecture either.
Or Python.
**Michele Mancioppi (Dash0 Inc.)** 07:16 Yep.
**Antoine Toulme (Splunk Inc.)** 07:17 Yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 07:20 There you go, you're muted.
**Michele Mancioppi (Dash0 Inc.)** 07:23 In the system packages.
We wrote tests that actually check that stuff is produced.
Using, what I call an OTLP sync, which is just a GoProcess built based on the collector, and then I assert on what it receives.
Maybe we should do it injector as well.
**Antoine Toulme (Splunk Inc.)** 07:44 I, I'm… I'm not sure what Pebble did, what he bought, he, He did a thing in the GitHub build where he's having two additional… things for S390XSPC64 early, instead of adding them to the matrix.
And,
**Michele Mancioppi (Dash0 Inc.)** 08:04 Because you need to set up QAM, right?
**Antoine Toulme (Splunk Inc.)** 08:06 But you can just do that with an if. So, what I've done in my build is that if you were to do that, you just keep your matrix build, but you have an if on the step for QMU, where you say, only set up QMU for platform if platform is That.
Makes sense.
So… he's done it in reverse, which is not very elegant, we can give him that feedback, at least, and see exactly why. Then he's also doing a few different things, like build binary via cost compilation is a little different, no longer calling make goals, he's doing things by hand.
Same for integration tests, also calling them by hand. What's going on here? Why did you do that?
That might just be a preference.
Or is there something that is bypassing because it didn't work?
That's my main questions, I guess, right now. So, just before we even go into it.
**Michele Mancioppi (Dash0 Inc.)** 08:56 Do you want to take the lead on, providing, providing tickets to this PR?
**Antoine Toulme (Splunk Inc.)** 09:00 Yeah, of course.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 09:02 I think… I think that's maybe the wrong order to, like, because that sort of gives it, gives the impression that if you, if you resolve these issues, then, the PR can move forward. But if there's, you know, higher order, issues with the, with the, like, with the concept, then, you know, you might work through the… the smaller things and, you know, still get blocked anyways.
**Antoine Toulme (Splunk Inc.)** 09:24 That's true, Jack, but… I mean, my stance here is that If this is good enough, and it works, and it's worth having.
then I would want to then have some sort of a discussion.
Where we would say, this looks like it's, acceptable. Right now, it's not quite ready.
And then, you know, go to Pavel and say, we would not merge that because we don't know that QMU is actually doing the work that we want it to do, and we need to take the integration test, frankly. But if you're really interested in having SVNITX support in Injector.
Would you like to come in and be the maintainer of that?
And I'm okay then.
Because in a sense, it's no longer my problem, right?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 10:07 But it's like… it's like, yes and. So, like, saying we… the Injector supports 390X is, you know, we have to caveat that, and we have to caveat that very loudly, to say, like, look, when we say we inject this, we support this architecture, it doesn't actually mean that we support, injecting .NET and Python, in applications that are running this architecture, because, you know, that's…
**Antoine Toulme (Splunk Inc.)** 10:31 He'll be dragons, right?
I, I…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 10:34 Right. So, yeah.
Right, so I guess, like, in the README, or wherever we're documenting that we support this architecture, add that qualification so it's loud and clear, and it's not like a rug pull or something like that.
**Michele Mancioppi (Dash0 Inc.)** 10:47 I mean, the easiest way to actually… do that properly is to add OTLP sync tests to our integration tests, and make sure the telemetry spits out.
Yeah, of course.
I mean, I'm still very skeptical about QMO, because… when I was making the big push to get the Injector to work with ELF, Cameo beat me in the ass, 50 ways to Christmas.
So, I… I don't trust it.
It's like, I had infinite pain. I have absolutely zero confidence that if it works okay, me to work on, on real, S390X.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 11:28 But you understand, Antoine, you not understand the consequence of what Michele is suggesting. If we adjust the integration tests to assert that telemetry data is actually coming through in the integration tests, then P90X cannot pass that. P390X cannot pass that bar, and it'll be rejected.
So, it's like…
**Antoine Toulme (Splunk Inc.)** 11:49 Let's do that first. Let's do that first. But if it does pass, what do we do?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 11:54 It can't pass.
Liking.
like, I mean, unless, like, are we making a logical… is there some sort of logical flaw here? Like.NET and Python do not support those architectures.
**Antoine Toulme (Splunk Inc.)** 12:05 No, but it just works for Java.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 12:09 Right, so then, like, okay, it would work for Node and Java, things that are not architecture dependent, and maybe Ruby in the future, I'm not sure. So, like, then you have to add, sort of, qualifications in those integration tests, which says, like, hey, you know, you don't have to worry about this assertion in these languages.
**Antoine Toulme (Splunk Inc.)** 12:29 That's right.
**Michele Mancioppi (Dash0 Inc.)** 12:31 Yeah, the point is that if I… There are two possible approaches to this.
One is… Us?
Minding the end-to-end experience for the user, and us, instead, mining in our own backyard.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 12:48 Right. That's exactly the question.
**Michele Mancioppi (Dash0 Inc.)** 12:57 the, From a purely technical perspective, the right place were to mine the point of view of the end user.
Is the packaging sick?
Not interact.
It's the packaging and the operator SIG, because they are the OpenTelemetry tool in the face of the user.
I have zero confidence that the operator is doing that, and that's why I feel compelled to engage in the injector instead.
**Antoine Toulme (Splunk Inc.)** 13:22 But that's not the right pacing. Yeah.
**Michele Mancioppi (Dash0 Inc.)** 13:24 It's not the ideal place, but it is at least a place, right?
**Antoine Toulme (Splunk Inc.)** 13:28 Well, I mean, look at it a different way. Right now, they are making the promise that it works on S390X.
Like, they're already making the prob… they're already making the mistake.
So… Another way to do this is we could also ask that the operator SIG have an NM approval on that operator, I can go help there, but once we have IBM history and ATX Gita burners, we should run the operator on that environment.
Before we politicize this work.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 14:02 To run it on that environment and verify end-to-end data flow.
**Antoine Toulme (Splunk Inc.)** 14:05 Yep.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 14:06 So just like the packaging SIG views, it's responsibility, like, it's the place to verify end-to-end data flow, the operators should do the same. They're at the same level of abstraction.
**Antoine Toulme (Splunk Inc.)** 14:14 The Injector can speed out binaries, but yeah, the way they're being consumed is important.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 14:21 There's sort of a philosophical question that we have to, you know, ask… answer for the injector, which is, like, you know.NET and Python each support two architectures today, and they're the architecture-dependent languages.
Should the injector, you know, limit itself, in terms of the architectures it supports, to the least common denominator of all languages it supports?
Or should it be sort of, like, unopinionated about architecture? And say, like, hey, you know, we only concern ourselves with setting environment variables, and, like, let's say that .NET and Python diverge someday, and .NET adds support for S390X and Python doesn't. Like.
You know, what do we do in that situation?
And so, like, you know, I think from a technical perspective, that's where I think, It would be better for the injector to only worry about what's in its backyard.
Because it's just…
**Michele Mancioppi (Dash0 Inc.)** 15:25 We actually went and precluded donet versions below 8 from being injected.
Because they barked.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 15:36 Maybe that was a mistake. Like, you know, if it doesn't… And I don't know, I think I'd probably have to evaluate those cases, like, what borked about them? What broke about those that caused us to reject them. But, you know, our job fundamentally is to detect the, you know, the version of libc that's bound, and to set environment variables.
**Michele Mancioppi (Dash0 Inc.)** 16:01 For example, I ended up… Forking the injector inside their ZRA and make configurable.
which version of .NET the Injector in chats? Because if you have a version without instrumentation old enough, you can support .NET 6.
You like it.
I've not opened the PR upstream because I'm ashamed of it, but… There is also the aspect… so there is… The reason why we did that back when.
It's because there was no way to safeguard proceed.
From being murderized by the wrong version of the net being injected.
And you end up crushing applications like a brick. And that's why we said, We do… We check .98 and above.
And, ideally, we… We would have kept track of what is supported by Hotel Upstream, but that is more a packaging problem, quite frankly, than it is an Injector one.
So, if we built configurable safeguards to say, This thing?
Refuses to, like, you need to opt in to configure on an architecture.
From the packaging perspective, we control that, because the configurations are shipped with Injector, right?
So, if the injector had enough Knobs to twist.
like, make configurable which version of .NET you're… comfortable injecting.
That could work, right? Then in the case, the injector becomes unopinionated, and if you go and try to inject something that will explode in your face, congrats, it explodes in your face.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 17:51 No defaults to worry about, but at least it's configurable.
**Michele Mancioppi (Dash0 Inc.)** 17:55 Yeah, I mean, both stances are valid.
One keeps the responsibility of making sure it works with us, and one delegates to others.
And sometimes it's us, again, in the packaging SIG, and sometimes it's the operator and other people.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 18:14 I think more and more, the injector isn't going to be, like, a standalone tool. It's going to be, you know, part of something higher order, like packaging or the operator, and so I think it's okay to delegate some of those decisions to others.
Go ahead.
**Michele Mancioppi (Dash0 Inc.)** 18:31 It's a valid point of view to have. I dread the moment that those people make terrible decisions, and then we get all the issues.
It is. It is going to happen.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 18:44 Yes.
Okay.
So where does that leave us? You know, I think the big question and a lot falls out from this is, you know, just how you framed it originally, Michele, which is like, hey, is the injector only going to be concerned about its own backyard, or is it going to be concerned about, like, the overall user experience?
And being concerned about the overall user experience, I sort of… like, you know, it inevitably leads to the rejection of S390X.
And so, we know the writing on the wall. If we take that point of view, S390X gets rejected.
**Antoine Toulme (Splunk Inc.)** 19:27 So, here's maybe some data, also, that the Linux Foundation has been working with IBM. I've been shaking that tree again. We should have, by end of day, an update from the LF developers to get us access to IBM S390x GitHub runners.
After… having to kind of escalate that all the way to the top of, of that org, last week. So… you know, maybe, maybe we get GitHub Action Runners that work in that environment.
in… We can actually… this dead out.
That… that would be the ideal outcome.
The second thing that we need to do is to add more insertions in your integration test, because now they pass with something that we don't think they should pass.
That's the second thing.
And the third thing is to maybe engage with Pavel and say, hey, whatever we're… but even if we were to add this S396x report, even if we had all of this covered.
I would like to have Pebble.
Help us maintain that moving forward.
Would that make sense for y'all?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 20:35 I think all the things that you laid out make sense, and I would just add one additional one that, like, you know, if we do add S390X support, if all these cards fall into place, we need to talk about it in a way that is,
**Antoine Toulme (Splunk Inc.)** 20:51 Yes.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 20:52 That is, like, realistic, which is, like, we don't support these languages because we can't.
And I guess I don't know that for a fact. I guess we're, like, 98% sure, or something like that, that, like.NET and Python will fail. We'll see if we… once we upgrade the integration test, to add more assertions, but…
**Michele Mancioppi (Dash0 Inc.)** 21:07 No, they put on a camera, you don't know.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 21:11 We'll see you.
**Michele Mancioppi (Dash0 Inc.)** 21:12 How many tickets.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 21:14 We'll see when we run the integration tests on the, like, the updated runners that Antoine is talking about.
**Antoine Toulme (Splunk Inc.)** 21:22 That would be a good start, right? Otherwise…
**Michele Mancioppi (Dash0 Inc.)** 21:24 Yeah, yeah, I, I could, I could take the stance. I could live with that. Then we, we moved, The battleground of the end-user experience in the operator and the packaging SIG.
**Antoine Toulme (Splunk Inc.)** 21:38 Yep, I like it too. This works for me.
**Michele Mancioppi (Dash0 Inc.)** 21:41 And in the past, we have… so, for example, the injection of languages is always conditional to a configuration that you will find that package there. If there is no .NET SDK to inject.
And you put a file that points to something that doesn't work, it explodes in your face.
Shit.
And if there isn't, it doesn't inject, so this is done that, but love, there is no Auto SDK for that.
So… I don't even feel that we would need to actually exclude architectures.
It's a matter of, do you put… the files pointing to the SDK, yes or no?
There is the aspect… Of, safeguarding versions of the runtime.
that are not being compatible, and I would like them to make also that.
configurable.
**Antoine Toulme (Splunk Inc.)** 22:34 Okay.
**Michele Mancioppi (Dash0 Inc.)** 22:35 Where you would say, yes, the Toulmann SDK is over there.
And you can inject version 8 and above, because that's the only one that the SDK will support on this architecture.
**Antoine Toulme (Splunk Inc.)** 22:48 I… And we're telling them, this is gonna be fun, because when is Java 8 finally going away, Jack?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 22:56 Whatever.
**Antoine Toulme (Splunk Inc.)** 22:57 Huh.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 22:58 Yeah, no, we, like, that question gets brought up every, like, 6 months in the Java SIG and continues to be an emphatic never.
**Antoine Toulme (Splunk Inc.)** 23:06 Okay, whatever's good. Alright.
**Michele Mancioppi (Dash0 Inc.)** 23:07 the, divide support.
There is no reason to remove Java 8 support. Nothing interesting is happening in terms of bytecode since Java 8.
Ain't nothing.
Hey, dude.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 23:19 At the BI level, there's lots of interesting things at the, you know, the garbage collector level there is, but, like, you know, it's not… it's not difficult, it's not painful for us to maintain Java 8 support, so…
**Michele Mancioppi (Dash0 Inc.)** 23:30 There are nice, new, shiny new toys, but there's nothing fundamentally broken. It's not IBM J6, yeah?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 23:37 I will say that the tooling is starting to go away. Like, various libraries that we depend on for… in testing are starting to say, like, no, we don't support below Java 11, or Java 17, or Java 21, like, JUnit. It stopped supporting below a certain version, and there's a couple of other dependencies we have that we have to, like, pin to a major version, because they bumped.
**Michele Mancioppi (Dash0 Inc.)** 24:02 Oh, wow.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 24:04 But, you know, there's no… There's no, like… it hasn't gotten… it hasn't gotten painful enough yet.
There's a little pain, but not super painful.
**Michele Mancioppi (Dash0 Inc.)** 24:16 So, I would like to, write down, then, the… implications.
Of what we just discussed.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 24:26 That's what I… yeah, I started taking notes in the notes doc, trying to do the same thing. So, you know, the fundamental question, whether we take a holistic approach, concerning ourselves with the overall user experience, or only concern ourselves with, like, the injector's backyard.
And where I think we sort of landed was only concern ourselves with the Injector's backyard, with some caveats.
**Michele Mancioppi (Dash0 Inc.)** 24:52 Hang on.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 24:53 And, you know, the caveats, so, like, the consensus is only… Sorry, our backyard with caveats.
And the caveats are, upgrade integration tests to verify end-to-end data flow.
We'll likely need to exempt, X, S390X.
For .NET.
And Python.
We need to have, proper… you know, GitHub runners.
S390X GitHub runners.
need to document the limitations of S390X. In particular, no, probably no support.
do you have support for .NET and Python?
Need, continued support is conditional on, on, on somebody committing to maintain this architecture.
Like, that's another thing we said.
Were there any other conditions that we talked about?
So the integration tests, proper GitHub runners, document the limitations,
**Antoine Toulme (Splunk Inc.)** 26:40 That's good news.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 26:41 contingent on the maintainer, and, like, I guess we also said, like, the operator should probably actually test the end-to-end data flow as well, because the operator is experiencing this, this issue that we talked about with .NET and Python, but silently.
**Antoine Toulme (Splunk Inc.)** 26:55 the…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 26:55 But that's… that's sort of not our problem.
**Antoine Toulme (Splunk Inc.)** 26:59 Operator has end-to-end tests, but just not on his 390X, so… and… You know, we could actually play that game. I think I should play that game. I will try that piece bevel. It's like, hey, QMU worked for your PR.
Can it work for the operator test?
And let's see it, cause, That would be interesting. And he might have those, so I wanna… I wanna ask him about that.
Genuinely, like, it's not a trap, but… That might be a good way to get us going, and then we swap them for proper GitHub action runners after.
But, by the way, so, if I get answers today about the timeline of integrations with GitHub Action Runners from IBM, it can really help us, like, make this a bit more real.
Instead of having these cramped discussions about what we can do and what we cannot, right?
I hope I have good news. I will let you know as soon as I hear. If you'd like to directly interface with the guy working on this.
I'm happy to put you into the discussion with them. There's nothing special about this, it's just, right now, it's just that, Morgan has been kind of, been spearheading the effort with me and, the guys from Matron SIG, but… you know, more people involved may help, I don't know.
Doesn't feel like it, but… If you… if you want to… Maybe getting front row, let me know.
**Michele Mancioppi (Dash0 Inc.)** 28:17 For the record, I have some item of concern of, No longer manning the ramparts.
Before others.
Set up the proper process.
Like, at the moment, you say, sure, configure your way to death in the injector.
Without the others picking up the slack.
Operator side, for example.
That's painful. We're letting the users down.
**Antoine Toulme (Splunk Inc.)** 28:50 Noted.
Not yet, man. Talk to you later, Mickey.
**Michele Mancioppi (Dash0 Inc.)** 28:54 Goodbye.
