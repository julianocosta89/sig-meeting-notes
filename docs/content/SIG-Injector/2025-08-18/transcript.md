SIG: SIG Injector
Date: 2025-08-18
Duration: 51 minutes
============================================================

## Zoom Recording Transcript

**Antoine Toulme** 04:17 Hello!
**Bastian Krol** 04:18 Hello, nice to meet you!
**Antoine Toulme** 04:22 Sorry, just a sec, playing with the camera.
Nice to meet you. I see you have a draft pier open.
**Bastian Krol** 04:30 Yeah, just in time, I wanted to get it out before the meeting today, although….
**Antoine Toulme** 04:37 Awesome.
**Bastian Krol** 04:37 It doesn't really matter, but yeah, yeah.
IF.
**Antoine Toulme** 04:43 I'm gonna… Little… And here, on the injector.
Beaching…
I'll do now…
Okay.
Alright, so let's talk about that. So, …
Yeah, he got your name down… … Glory class… Okay.
Should we start with that?
**Bastian Krol** 05:25 Yeah, I mean, initially, this is the second time, for this meeting? Are there usually more folks around, or…?
**Antoine Toulme** 05:33 This is very much a second meeting, yes.
What's his name? I think….
**Bastian Krol** 05:39 There was someone.
**Antoine Toulme** 05:40 Jacob. Jacob wanted to join.
**Bastian Krol** 05:43 Okay, shall we give him a vote?
**Antoine Toulme** 05:45 I'm gonna ping him. We're starting the injector.
**Bastian Krol** 05:55 Chili cook.
I'll just drop… Yeah, but we can also just start.
Talking about this.
**Antoine Toulme** 06:03 He's joining. He's joining.
**Bastian Krol** 06:05 Excellent.
**Jacob Aronoff** 06:21 Sweet.
**Bastian Krol** 06:24 Hello?
**Jacob Aronoff** 06:26 Can you hear me okay?
**Bastian Krol** 06:28 Yep.
**Jacob Aronoff** 06:29 I'm just making lunch right now, so I'll be up.
**Antoine Toulme** 06:33 Alright.
Okay.
**Jacob Aronoff** 06:36 around you.
**Antoine Toulme** 06:38 No problem.
… So let's, … do you want to go over your PR, man?
Do you want to share your screen, show us a little bit what's, what's happening?
**Bastian Krol** 06:49 Yeah, sure, we can do that… let's see….
**Antoine Toulme** 06:54 Okay.
**Bastian Krol** 07:00 Okay.
Can you see my screen?
**Antoine Toulme** 07:04 I think? Yep. Yes.
**Bastian Krol** 07:05 Okay, excellent. Okay, let me get this out of the way here.
Oh, yeah. Okay.
So, maybe since… since we all haven't met, or I at least haven't met you, maybe, maybe before we start with that, a little bit of context. So, this… this original injector, this came from, from you, Antoine, from… from Splunk, is that…?
Right.
**Antoine Toulme** 07:34 Yeah, that's correct.
**Bastian Krol** 07:36 Gotcha.
**Antoine Toulme** 07:37 I think I wrote that code.
**Bastian Krol** 07:38 Pardon?
**Antoine Toulme** 07:39 I think I wrote the C code that you are replacing, so… That's a relief.
Yep.
**Bastian Krol** 07:46 I hope that doesn't cause any, any hard feelings.
**Antoine Toulme** 07:49 No, it's, …
It served its purpose, got us where we needed to be so we could have this discussion now, right?
**Bastian Krol** 07:57 Yeah, excellent. Was it heavily used in… with Splunk's customers? Okay, interesting, okay.
**Antoine Toulme** 08:07 Very much so. It's very specifically used for legacy host-based monitoring, so think of it as Linux VMs in maybe EC2 environment, but most of the time, like, bare metal or proxmox-step VMs.
**Bastian Krol** 08:23 Okay.
**Antoine Toulme** 08:24 This is where it's used the most, because these are really difficult environments to instrument.
It gets them off the ground pretty quickly compared to having to do it themselves.
**Bastian Krol** 08:34 Yeah.
Understood. So where I'm coming from, or where the thing that Michaela and me have been collaborating on is coming from is… is more humanities environments, so we are also using, this, or our customers are using this, but right now it's exclusively
on Kubernetes, though, I mean, in the end, it doesn't matter, your injector was
I think package so that it was injected via ETC, early preload. We are mainly using the early preload environment variable. I think that's basically not super much of a difference, has the same effect, basically.
I think we have a kind of good overlap of features, although some things are different. So maybe before we go into the actual code, …
So here is a list of
Pros and cons of the current…
injector and the new injector, and there are pros and cons in both directions. There might be things here in this list that are wrong, because I just had a basically cursory look at your existing injectors, and maybe I understood
things wrong. One thing that I wondered about is, how did… I think you are binding ellipsy, right? How did you handle systems that, like, like Alpine, that are using muzzle?
**Antoine Toulme** 10:07 Yeah, but, so, just kind of…
because we're doing this mostly on hosts, and we're really targeting, you know, Red Hat and Ubuntu.
Okay. Don't have to think too much about Alpine-type use cases, and that has not come up in our environmental customers. Okay. Again, because we're targeting legacy-type customers who don't have this type of luxury. So, the moment you.
**Bastian Krol** 10:30 Okay.
**Antoine Toulme** 10:30 to, like, that was the… a presentation by me, Charlie, at KubeCon, for example, was showing to me, like, you thought about a lot more general use cases than we had, right?
So, this is not, … yeah, you're valid in your approach, you're saying, okay, there's more… we should think about those, and yeah, we did not think about those.
**Bastian Krol** 10:50 No, no, no, that's fine. But then I read that right. So that's one, I guess, advantage of our injector, because we do not bind to a libc, so it can be used independent of libc, but it's still, obviously, since we still use LD preload, can only be used with
binaries that do… that are dynamically binding at startup anyway, so if you have a completely static binary that our injector also does not work, but that's a use case that I think I wouldn't know how to cover that at all.
**Antoine Toulme** 11:28 Yep.
**Bastian Krol** 11:29 Right.
What else is maybe noteworthy? Yeah, there's a little bit of difference in how we handle it.
**Antoine Toulme** 11:37 paragraph is asking, like, do we overwrite whatever's been written? So….
**Bastian Krol** 11:42 Yeah.
**Antoine Toulme** 11:42 No, we don't. There is a… the logic in the C code is looking for whether the value is already present. Oh, okay.
**Bastian Krol** 11:52 You know.
**Antoine Toulme** 11:53 Yeah, it's a little bit of a weird of a sleight of hand, toward the end, when you're about to set it.
So, if… If strive, compare… Oh, it's not.
**Bastian Krol** 12:05 That checks whether it's in the allowed list.
**Antoine Toulme** 12:07 Let's done it. It's the line below, line 100. When you set nth, we pass a zero flag.
**Bastian Krol** 12:14 Alright.
**Antoine Toulme** 12:15 That is the meaningful bit. It says, if it's already said, do not override. Now.
**Bastian Krol** 12:20 Oh, okay, that's… that's a nice part of C, where….
**Antoine Toulme** 12:25 Yeah, no, I… I mean, I learned that for this, and I forgot it since, right? So you're jogging my memory.
**Bastian Krol** 12:31 Yeah, cool. No, that's good to know, yeah.
**Antoine Toulme** 12:34 The problem with this is that it's also not consistent, because let's say you set not options, like you're saying, right? Or you said other things, you can have a broken experience, because you could have half of the environment variable set. But the thing that was important to us is to, to keep…
the existing behavior of the app running as it should, meaning if they have said things, then we will be broken, but not them, rather than breaking the experience. We don't know how to…
And this is something you seem to have a better handle of. You know how to merge values. We did not know how to.
**Bastian Krol** 13:05 Yeah, yeah, my… I mean, this could probably be also done here, if you do a getenv before, and then kind of do string merging, but yeah. So we… we… we already do that merging, I think that's probably, definitely an advantage, so look at the existing value, and then
then merge whatever is necessary. Although the setEnf also has
one specific advantage, specifically when it comes to runtimes that do not use getEnv to read.
**Antoine Toulme** 13:39 the environment variable, and that is… that is something that I… that I listed down here, so specifically .NET,
We can inject the tracer there with a get and override.
**Bastian Krol** 13:51 But everything that is then… because that…
CLR bootstrap code is written in C++, uses getEnf, that's fine. Everything that then inside the C-sharp runtime, or whatever you're using there, the .NET runtime happens, they read differently, they just copy the underscore, underscore, and we run at startup, and then
Have it as a hash map, and we don't catch those, so… that's a bit of a bummer.
not solved right now, but that… it doesn't… would not affect your set end, …
I guess because you just override it, and then….
**Antoine Toulme** 14:32 No, yeah, he works…
We have integration tests that check that this is working, so we know… we know it works okay, that's it.
Even for the .NET approach, we are… we're doing some very basic things in that C code, where we check that the first parameter in the program invocation is .NET.
**Bastian Krol** 14:50 Hmm, yeah.
**Antoine Toulme** 14:52 Maybe we're… maybe we're letting loose a lot of options. …
We don't know. We haven't heard anyone coming to us and saying, hey, I really wanted to run this .NET program on that Linux box.
really frustrated that it didn't work the first time automatically, right? No one has had that type of expectations.
Java? Sure, it better work the first time. Node.js? Okay. .net has been a third, very, like, distant cousin of this, and for Windows, we have a very different approach, where we use a registry on Windows machines, where most of the .NET
Stuff runs anyway.
**Bastian Krol** 15:28 Okay.
**Antoine Toulme** 15:29 And for that approach, things just work much better because you can register profilers in the registry that will call out to your module.
**Bastian Krol** 15:38 Okay, interesting.
**Antoine Toulme** 15:39 We have a separate approach for that. This approach does not extend… I mean, unless you manage to make your approach work on Windows, for Windows, we have a different thing that's going on.
**Bastian Krol** 15:51 Oh, no, Windows is super out of scope, so… at least from my perspective. I mean, this is…
all based on early preload, and that's not a thing on Windows, so I think that would be a different project, more or less, right?
**Antoine Toulme** 16:05 Okay.
**Bastian Krol** 16:06 Yeah, that's… that's at least my view. Yeah, I guess… guess that's… that's…
That, … what else is here? Yeah, that's just more to do, so this is not complete yet, what I put up today, so there are a couple of things that I still need to…
take care of, but I wanted to have it up there, so you could take an early look if you want, and we can also discuss high-level
questions in which direction we want this to involve, if it is
if there are any showstoppers, before I hash out these details here.
….
**Antoine Toulme** 16:46 That makes sense.
**Bastian Krol** 16:47 Yeah. Right, but that one thing that I noted in your code was what you just mentioned with you always check the executable name. We don't do that. I'm not sure if it's…
super… and it's super important. I think both strategies are fine. I mean, you will probably not find a lot of other executables that ask for node options, so…
Check for the accusable name is a little bit…
I don't know if it's needed, but we can discuss. I don't have a strong opinion either way. We can bring it back or leave it out.
**Antoine Toulme** 17:24 … Yeah, no, I'm not sure I care that much, …
the only problem we could have is possibly, like, if someone was to place a secret in one of those variables, and then you could sweep in into any host, but that's stupid. Like, that's not… it's not a big deal. ….
**Bastian Krol** 17:45 Well….
**Antoine Toulme** 17:45 I've heard some complaints. When we started doing this, right, one of the things is, oh, we don't want to pollute every process with some environment variables that are not used.
I'm not sure there is a point there either, but… Yeah.
**Bastian Krol** 17:59 But that's, of course, more relevant if you do setEnds, then you only overwrite GETEND.
Nobody asks ever for that environment, rather than this point is somewhat moot.
**Antoine Toulme** 18:09 You got it. Okay, that's great then, sir. Alright.
**Bastian Krol** 18:11 Yeah, okay, so I'm not sure how deep we want to go into the details of the code, so, just let me know what you want to have a look at, or what you….
**Antoine Toulme** 18:23 Maybe you can, … so, I mean, I think for any… any enhancements where we want to…
We want to make it so that we can stepwise increment toward… like, we can have, like, looks like you have a lot of changes, so maybe we can incorporate them
As we go through them, ….
I haven't looked at the code right now.
**Bastian Krol** 18:43 I mean, I just put it up, like, 14 minutes ago, so….
**Antoine Toulme** 18:46 So… so maybe we can take a… this week I can take some time. I think Jacob too, Evan, please feel free to just review the code, make sure that it looks good.
**Bastian Krol** 18:54 Okay.
**Antoine Toulme** 18:55 Is there… What would be important?
… No, I think, … We need to do that this week.
**Jacob Aronoff** 19:06 One thing that I had a question about is, I was looking at the, like, "-0 operator code, and, like, how… the relationship between that and this, and I'm also wondering if there's an opportunity to sort of donate slash merge some of that code into the operator itself?
Such that we don't need to… we've been… Antoine and I have been talking a lot about, like.
the refactoring slash revamping of our instrumentation CRs, because I'm not happy with them, I don't think users are happy with them.
**Bastian Krol** 19:40 You're talking about the open telemetry operator now?
**Jacob Aronoff** 19:43 Yeah.
**Bastian Krol** 19:44 Yeah, yeah. Okay.
**Jacob Aronoff** 19:45 And after looking at some of the code that you have, I'm wondering if there's an opportunity to, as part of this donation, to also do, sort of, I don't know, we want to do, like, a V1 Beta 1 for instrumentation, and that'll…
With a bunch of changes, and…
I was wondering if that's a thing that you'd be open to doing, and or sort of demoing, how we can improve that experience.
**Bastian Krol** 20:12 That's… that's a very good, but also very broad question. So, I mean, … we… we…
Yeah. I think, so, so conceptually, we are open to, to that, to contributing also oper… things on the level of the operator upstream.
I think I would see that…
quite separately from what we are doing here with the Injector, just also to keep the scope under control, so I would.
**Jacob Aronoff** 20:44 Yeah.
**Bastian Krol** 20:44 Basically, you live, leave.
But embedded in a more general sense, so right now, I'm the only one maintaining the…
operator code at dash0, so operator at Injector, trying to hire a second person, but so far it's been a little bit difficult, so just time-wise, I guess it would be really hard for me to also contribute operator things upstream in a sustainable
manner in the next few weeks or months, that's….
**Jacob Aronoff** 21:16 No, yeah, I wouldn't say that there's, like, a real rush on it. I'm planning on beginning the instrumentation refactoring probably in September, mid-September, realistically. Antoine's gonna start to do some of that
soon, I think, if I'm… that's not me signing you up for work, right? That's the thing that we talked about.
**Antoine Toulme** 21:36 Right. So, yeah, we had a good discussion about it at the SIG meeting for the operator last week, but… so there's two things that I'm engaged on. One is, I want to make sure that we can, …
It's gonna be counterintuitive, but the operator currently mandates that we use a custom resource definition for all instrumentation definitions. We have a need to be able to operate from a helm chart perspective without CRDs, because CRDs just…
make our life difficult.
**Bastian Krol** 22:04 Okay.
**Antoine Toulme** 22:05 their lifecycle well, does not like to upgrade them, does not like to uninstall them properly when people take them out.
**Bastian Krol** 22:11 So it's all sorts of headaches for us, and I think overall, we….
**Antoine Toulme** 22:15 We would much rather have our people have very, like, consistent results, and like, you get this in, and this is exactly what happens when you get that. So, the problem is the code is a bit intertwined between the custom resource definition and the configuration of the instrumentation, all that, so we need to kind of find a way to make that work.
If we can do that, we're gonna have a great time with our customers, because one of the sources of performance issues we're seeing with the operator is that it's doing a lot of checking on those implementation CRDs, and we think we can just let go of all that and be very happy in pod without having any of that type of stuff going on.
That's one. The other is, we want to have a certified operator with Red Hat, which is going to create a managed experience for our customers, which is going to take over most of the configuration that they have to think about right now.
So…
Right now, they have to do all sorts of work after installing the operator, such as setting the configuration of the collector, setting the configuration of, …
you know, the cluster receiver, or the implementations, and all that, and the reality of it is that 99% of customers would like this to behave just like the Prometheus operator, which is shipped by default with OpenShift. When they start things, it just works the first time, it will just auto-scale, it will work its way out of problems.
And, it will to upgrade nicely.
And….
**Bastian Krol** 23:35 That's.
**Antoine Toulme** 23:35 That's what our customers have been clamoring for.
**Bastian Krol** 23:38 Yeah.
**Antoine Toulme** 23:38 We're working toward that. One of the aspects of all this is that, in general, the instrumentation code in the operator is very opinionated and is doing exactly what you see in that C code. Well, it's actually doing more, right?
It gets in the middle of the pod definition, it looks for the environment variables, like, that Python path looks, ….
**Jacob Aronoff** 23:59 Pretty good, but that's not what we want. Takes it. The prefix before, suffix after.
**Antoine Toulme** 24:05 There's all sorts of…
We'd much rather have one way to do everything that works for all SDKs, that is tested in isolation from the operator use case, and we could just inject into a Docker image.
That would work for Alpine and Libsy and whatever flavor of the day of C you want to have, and would allow us to simplify the story as a whole, because the next thing we would be able to do is go back to all the SDKs and tell them, hey, we have tested this behavior.
This is the standard behavior by which you will abide to do auto transportation.
Moving forward. And, you're not… you're not meeting the bar. You need to do, you know, make this available to us, so we can have the same experience across all languages.
And that's… that's where we are.
**Bastian Krol** 24:54 Yeah, that's, that's, … so, I, I'm not… Do, … how much…
of that, we at Tashiro have already solved. So we started out with a different…
philosophy in general. I mean, the OpenTelemetry operator was already in place. I think the philosophy behind the OpenTelemetry operator is mostly you…
At least have to put a label on each of the workloads that you want to instrument, so you have to opt in per workload.
What we are doing in the zero operator is, by default, if you don't configure anything, we will just
instrument all workloads, everything that you deploy into the cluster. So that's already a little bit of a conceptual
difference. I mean, both are valid, and some users would like this, and others like that, so that's just one.
thing. We've started with the injector-based instrumentation relatively early on.
**Antoine Toulme** 26:01 Yep.
**Bastian Krol** 26:01 …
But apart from that, yeah, I say… but we can… we can definitely talk about our experiences with our approach, and how that differs from…
The current, so that, that, that's, definitely always, …
We can always do that. I didn't get that part about the custom resources and… and how….
**Antoine Toulme** 26:32 Yeah, sure, we can explain.
**Bastian Krol** 26:34 Yeah, so what exactly… I… I don't work with the OpenTelemetry criter, really, in detail. What does the instrumentation custom resource definition do exactly?
And why is it hard to upgrade with Helm?
To a new version.
**Antoine Toulme** 26:53 Well, okay, so first, Helm has a very, opinionated stance about CRDs. Are you familiar with that?
**Bastian Krol** 26:59 To some degree, but so, I also did a version upgrade of one of our custom resource definitions recently, and I think it kind of….
**Antoine Toulme** 27:09 Worked out of the box, but… Okay, let me show you.
**Bastian Krol** 27:14 I added a new version to one of the CIDs, so… but that seems to be supported.
Alright, so here's… here's a link that has information that you're looking for.
In the chat as well, I put it in the doc.
**Antoine Toulme** 27:29 … where is this?
We have any shows, discussion…
So, what he says from Helm is, …
you can install the CRD before the Helm chart installs using a special trick, where you place the CRD folder.
But, there's no support at this time for upgrading or deleting CRDs using Helm.
**Bastian Krol** 27:58 Right.
**Antoine Toulme** 27:58 It was an explicit decision after much communication due to the danger for unintentional data loss.
Yeah, that makes sense, right? Because those CRDs are actually very, like, flexible, you would make… you would want to change them.
So, what Helm is telling us is, if you're going to deploy CRDs, they should be done by hand, out of band, not through a Helm install.
Does that make sense?
**Bastian Krol** 28:23 Yeah, I… right, I remember this paragraph, I've read it a couple of times already. I need to go back and see how we did that. I think we don't have it in a separate, …
repository, and so it's not treated in any specific way by our handshot. And I think what this is mostly about is also when you have a heart precondition that you need your CAD
installed before anything else, and I think we don't have that, because our Helm chart does not install custom resources of these type.
**Antoine Toulme** 29:01 So, that makes it quite easy for us. We just installed the CRDs, and they can be upgraded by hand, if I'm not mistaken.
**Bastian Krol** 29:08 Unless you have them in that special CID.
**Antoine Toulme** 29:11 repository. What you cannot rely on, then, is the CID is….
**Bastian Krol** 29:16 already installed when all the rest of your handshot runs, but that's something that we luckily don't need, so that's maybe why we don't have that problem.
**Antoine Toulme** 29:26 In really, really large environments, when you do a Helm install, we have seen that the CRD might take longer than we like to install.
**Bastian Krol** 29:35 And the operator would try to start before the CRD is done.
Hmm.
**Antoine Toulme** 29:39 It starts to become more, much more difficult, because when the.
**Bastian Krol** 29:43 Okay.
**Antoine Toulme** 29:43 It installed itself as a webhook.
hooks that's going to stop the creation of any pods, and there are two options there, which are difficult. One of them is, if the webhook fails for any reason, ignore.
Right? Ignore the failure, just keep going, keep, and start the pod without instrumenting it, right?
**Bastian Krol** 30:04 Hmm.
**Antoine Toulme** 30:05 You can make it so that the pod deployment actually fails.
Which is what customers actually want, because they want to make sure that the stuff is instrumented, or it's not running.
**Bastian Krol** 30:15 Oh, okay, I see, yeah.
**Antoine Toulme** 30:16 And now you're in a really bad situation, because now your operator did not start.
**Bastian Krol** 30:22 Because the CRD is not installed.
**Antoine Toulme** 30:24 it's… it's blocking the deployment of any other pod from your Helm chart, even, right? So your collectors don't start, nothing starts, everything's broken, the customer's pissed off to no… to no end.
And you just put yourself into the crosshairs of everybody in plot.
**Bastian Krol** 30:40 Yeah.
**Antoine Toulme** 30:40 So, we cannot have that. The CRDs are a bad idea for a bunch of people who use Helm charts, and the vast majority of the people out there, they use Helm.
the reality of it is that the operator user base has been mostly OpenShift, which is vastly different when it comes to CRDs and management. First, they don't install with Hamchard, they install with operators.
The operators have a much better lifecycle handle over a CRD. They do all sorts of lifecycle, like, preventions, and they will manage the CRD installation cycle the right way.
And second is, they actually do a lot of auto-upgrades if they're in OpenShift environments, which is really sweet.
Right, I installed a… I installed the operator on my cluster 6 months ago.
I didn't look at it for 6 months, opened it the other day, it had had 5 auto-upgrades without me having to do anything.
And all that is the work of the operator maintainers. They actually, like, blood and tears go into this quite a bit, because
This is really difficult. Like, this is… you have to take care of all the breaking changes from the collector, you have all sorts of issues coming up from that, and, yeah, I think, in general, we're not…
We're not giving ourselves a whole lot of leeway. So, for example, the work that Jacob wants to start is to take a cut of the current supplementation CRD and build another version, because this way does not conflict with the current version, right?
But there's an upgrade that could be happening afterwards, right? It's not… it's not easy. So… …
I think we need to… if we're able to separate the concerns a little bit, things get much easier.
…
So, if we're able to kind of have, pretty much this injector project becomes kind of the… how you're going to instrument things, and it should have its API, right? Its API is going to be, like, the configuration of what you can set inside those things. It should be as standard and driven by the configuration SIG as possible.
Meaning, just passing in SDK values, right? And we're just a pass-through, we don't have any opinions about what is being passed in, but we're very….
**Bastian Krol** 32:45 Closely attached to what they agree with.
**Antoine Toulme** 32:49 And, the implementation SDK should become more like, I… I'm just applying…
the standard configuration coming from all those SDKs.
And we're just passing that on to the injector, which is going to use this LD preload hook to do all its work, and things take care of themselves. Right now, we're not in that situation. What's happening is that the operator has to do everything. They have to take the current SDKs.
bundle them into Docker images, make them available so that they can be copied, the Docker image can start as a prenat container, as part of a pod deployment, copy.
**Bastian Krol** 33:28 We do that.
**Antoine Toulme** 33:28 over… Very expensive, very expensive stuff, because you… you are asking people to know everything about the ecosystem.
So it's much better if we… the injector can take care of the… all the way to the darker image, maybe?
Right? In a way that is standard, that is well understood, and then works… it works on host, it works on Docker, and then the operator kind of steps in after that and says, we're going to use whatever artifacts are built by the injector project, and we'll… we'll play with that.
The problem is every time I mention Kubernetes to an Instrumentation SDK person.
they start to look for the exits, like, really quickly. Like, in the second I mentioned to… have you ever tried this? This is a good trick to make a Java person very unprofitable. You tell them Kubernetes three times. They will look for a way to get out of the room as fast as possible. It's really…
It's really too much for them. And I get it, right? I was a judge of opera for 10 years. So, they…
it's too much, there's too much in terms of cognitive load for them to think about that, but if you tell them, hey, I got this little LD preload.
And it's going to take your SDK and inject it using Java tool options into a process. Okay, I understand what you just said, right? That actually makes sense to me than when you mentioned thoughts, right?
**Bastian Krol** 34:45 I think that, that is, that is…
That's also something that I think about, so I think the current project has, is packaged as an RPM and as a Debian package, and I think a very straightforward way would be a third packaging that is basically targeting Kubernetes. So currently, my best idea would be the init container. We also use that, and
A lot of other operators are also doing that strategies.
that has its downsides, but it's the best we currently have. I think one…
one thing that is on the experimental Kubernetes Verizon are, what's it called? Image something?
**Antoine Toulme** 35:32 Yeah, images, volumes, yes.
**Bastian Krol** 35:33 image as volumes, so that would be super sweet, but I mean, that's….
**Antoine Toulme** 35:37 Yeah.
**Bastian Krol** 35:38 not happening right now, it's just a few years out, I guess.
Don't.
**Antoine Toulme** 35:43 Yeah, we… Yeah, we, we caught that, it was, it was cool. I don't know. ….
**Bastian Krol** 35:50 Yeah.
But I think, adding a third packaging, targeting Kubernetes, that would be super reasonable for the injector project, and that would maybe go a little step in the right direction.
**Antoine Toulme** 36:07 We do have this as an issue right now on the repository, so….
**Bastian Krol** 36:10 I put that up based on the discussion I had with Michele, with Jacob. I think this is valuable as an output for this project.
**Antoine Toulme** 36:18 And, …
I'm actually pushing on the other side of the equation now. I went to the Java people and said, it's really great that you're pushing Java jars outside, can you give me a RPM?
This is not… is this… is this… like… and I'm asking them, like, why is it that you're not… you feel like you don't have this responsibility to the community to make it easy for you… for others to consume your artifacts?
**Bastian Krol** 36:43 Hmm.
**Antoine Toulme** 36:44 Why is it so hard for you to understand that? And they give me…
okay reasons, but they're not very valuable. So, the other thing is, is this… this injector project right now, when it bundles its RPM and its Debian package, it's also downloading Java, Node.js, Python, and, you know, bundling that into the actual.
**Bastian Krol** 37:03 The auto instrumentation agents, or the whole runtime?
**Antoine Toulme** 37:06 the autonomous Transition Agents, the….
**Bastian Krol** 37:09 Okay.
**Antoine Toulme** 37:10 So that means we're doing their jobs. So, in a sense, like, the Java guys are like, I don't care anymore, I don't need to know about this.
And, only half.
**Bastian Krol** 37:18 Yeah, I'm not sure. I think maybe it is the right place, on the right interface, to actually… I mean, all these agent developers.
provide their agents in their native runtimes, like JARS or GAMs for Ruby or whatever, and I think it might not be too bad to have one place that bundles all of them, like, like….
**Antoine Toulme** 37:45 I don't mind, we just need….
**Bastian Krol** 37:46 Product.
**Antoine Toulme** 37:47 It needs to be discoverable, though, because I think that's the last thing you look at. Like, let's say you're a Java developer.
**Bastian Krol** 37:53 You're told by your boss, I need you to install the JAR… the OpenTeamatory JRS support on 10,000 machines tomorrow.
**Antoine Toulme** 38:00 Are you going to go for some weird hotel injector project? That's not the first move, right?
**Bastian Krol** 38:04 That's right. That's absolutely right. I mean, at least the documentation could…
Point out, yeah, you don't necessarily need to do that manually, you can always use….
**Antoine Toulme** 38:17 Right.
**Bastian Krol** 38:18 M, or… An operator, or whatever.
**Antoine Toulme** 38:21 Yeah, so we're gonna have to kind of dig ourselves out of a hole to make sure people know about this.
Which is good, because I got my KubeCon implementation approved, so I will talk about that and make sure that people know. I'm just not sure how much traction we'll get, but…
It's better than nothing. … So….
**Bastian Krol** 38:42 Food.
**Antoine Toulme** 38:42 In the meantime, like, if we're able to kind of, … I'll continue to document this mapping, and those responsibilities, because I think this is a big evolution of the operator, the system injector and all that. It's also not going to happen anytime soon, right, to be clear.
**Bastian Krol** 38:57 The operator's done this for, what, 3, 4 years of managing people's images?
**Antoine Toulme** 39:02 But once your stuff is in, I would love to make it so that we can try it out first, into the operator with the Docker image, learn from this, see if the performance is different, better, worse.
**Bastian Krol** 39:13 Yep.
**Antoine Toulme** 39:13 What's the scalability of that? I suppose it's going to be really good, because just for the reason that the operator has to do less in that very synchronous grow code when you're at speed, trying to rotate, like, create all those pods at the same time.
**Bastian Krol** 39:28 So.
**Antoine Toulme** 39:30 Yeah.
Yeah, it's doing a lot, but that's the nature of what it has to do.
**Bastian Krol** 39:36 I mean, one thing that is, clear is that you can anyway only target…
dynamic runtimes, like JVM or the .NET runtime, so…
go, everything that's compiled to a binary is out of the way, or we cannot have that in scope anyway.
Yeah, you're on.
**Antoine Toulme** 40:01 Yes, I agree.
I'd be happy if we have a new BPF story at some point, but I don't know. Someone else needs to come and help.
**Jacob Aronoff** 40:11 I'm not… I'm not holding my breath, that was ridiculous.
**Antoine Toulme** 40:15 Yeah, I mean, yeah, we have… I have some really good colleagues who, like, you know, really experts in the field of Go instrumentation who are working on Go auto-instrumentation. I don't know how far we'll… they'll be able to take it.
**Jacob Aronoff** 40:32 I think when I was talking to a lot of the pros, Customers past 2 years.
None of them were even close to saying that they're, like, entertained looking at it, just because of…
Security concerns.
**Antoine Toulme** 40:45 Oh, yeah.
**Bastian Krol** 40:46 Okay.
**Jacob Aronoff** 40:47 But… and that was a response from Lightburn. I think 6 different enterprises we talked to, they all were like…
And it wasn't… and it wasn't, like, a…
you know, this is gonna get to the point that we will. It was more of a, like.
We just can't get that level of access on Earth.
on our instances.
**Antoine Toulme** 41:06 Okay.
**Jacob Aronoff** 41:07 I mean, it's very possible that that attitude has changed, and has sustained a little bit more in the writing.
You know what's changed?
Popularity, right?
But that was certainly a bit of thought that we got from everybody we talked to.
**Antoine Toulme** 41:24 We have… we have a lot of work to get to… to this. I…
you know, I think we need to kind of think about what a first release would look like.
Given the… the work and all that that we have. And the thing that has the…
It gave me some grief, and I had a hard time kind of making sure that this SIG meeting was on the map and all that, that we were in the calendar, that we were on the community with me, and I would like us to kind of start to attract a little bit of community, people who care about this type of problems, so that we can start
to have a bit more of this type of feedback, and I don't want this to be just, you know, vendors pushing this. I'd like to… for people to kind of
try it out. I've already got feedback that people have tried what we have out, and they're happy.
**Bastian Krol** 42:10 no.
**Antoine Toulme** 42:10 this code, it works for them in their limited use case, but let's, I want to keep a…
it's a good time to break things first off, like your zip code comes at the right time. Let's break things if we have to. If we can have regressions, like .NET support can suffer, that's… it's what it takes to get us to the next phase, that's fine.
So, it's also great because we have no expectations of maturity at this point, right? And it's a good time to experiment with things, but I want us to attract people who can play with this code, tell us what's working, what's not, and use that very successfully, and give us a… give us a piece of their mind.
**Bastian Krol** 42:47 Yep.
I mean, what would be really great and valuable to have, to have someone with really strong
system low-level skills, like, who knows their way around a linker, that is not me, unfortunately, so before we donated that code, I mean, I think you heard from Michaela, we tried to move our code into a different direction, where it directly reads, the underscore, underscore, and we run it, and we… I spent, like, 6 weeks on that without any success, and that's also just
Because my skills in that area are limited, so… But… no.
We'll see.
**Antoine Toulme** 43:27 That's, … I'm sorry that you had to dig into that, that sounds very complex.
But, okay.
**Bastian Krol** 43:36 Yeah.
**Antoine Toulme** 43:37 So… Yep.
… yeah, is there…
I'm gonna put it slow, let's see a little bit. So we have your code. We're going to review that. In terms of issues on the repository itself.
Is there anything that we should spend time on? I think we actually covered most of that discussion just now.
…
So we have five open issues. The first one is the dependency dashboard, which is a renovate issues, not something we need to think about. Another one is the Ruby Swantation package, which I copied from the desperate attempt of the Ruby maintainers on the operator SIG.
I think it would work, but I can't make it work, and…
I don't know anymore. I haven't had time to look into it, so maybe I'll just close that.
The next one, so creating a Docker image with the artifact, that is exactly what we just talked about. It's like, just like a Debian.
**Bastian Krol** 44:35 Yep.
**Antoine Toulme** 44:35 We could just package this as a Docker image, see if it helps anyone.
….
**Bastian Krol** 44:40 I mean, obviously, because I'm using that as a container image, we have stuff for that already in place over at the Shiro operator repository. I can maybe, in a later step, I would
keeps that as separate PRs, … moves some of that stuff over as well.
**Antoine Toulme** 44:58 Okay.
That makes sense.
… It's… yeah, it's very much tentative thinking. The….
**Bastian Krol** 45:07 The next one is adding Python….
**Antoine Toulme** 45:09 support, so Python support is not there in the C code. We don't know how to deal with the fact that we need to manipulate Python path instead of just replacing it.
So I'm sure your Z code's going to do better than we had, because you just have better fine handle, grain handle over the data.
**Bastian Krol** 45:28 Yeah, Python is unfortunately another, one that exhibits a behavior like I, …
explained for .NET, so I think also Python does not read environment variables via getEnf.
But I think Michaela had some ideas around that, so… yeah, but that's… That's something where we can…
look into.
**Antoine Toulme** 45:52 Okay.
**Bastian Krol** 45:52 NATO.
**Antoine Toulme** 45:54 … Yeah, so it's not there, so it's not like we're missing it, I mean, there's no regression.
So the last one is creating a release workflow.
Which isn't clear. So I started to work on a really script, and Michele was saying, well, I don't think this is the right idea, we should not have tags which are going to be some wear-type versions.
And I said, okay, maybe we should talk about that, in a bit more detail.
I don't know.
**Bastian Krol** 46:28 I don't have context on that. I don't know.
**Antoine Toulme** 46:31 I'm a kid.
**Bastian Krol** 46:31 Why would you not have versions… techs that, I don't know.
**Antoine Toulme** 46:37 Thinking ahead, let me see… let me share my screen.
**Bastian Krol** 46:42 Yep.
**Antoine Toulme** 46:42 So, the thinking here is that I'm not sure what is the value of SEMVR for something that is effectively a delegation of a bunch of upstream packages with separate SEMVRs. It seems.
**Bastian Krol** 46:51 Okay.
**Antoine Toulme** 46:52 me, we'll be able to have any specific semantics in the versioning of this repo.
I'll just make an index starting from 1. Okay. I mean…
So, that's fine by me, especially if we don't know anything, we're just playing out things, but do you want a V in front of that one, or just want to have one? Like, is it, like, you know, it can be 1.2.current quarter, it could be whatever you want. …
I… so, I think one way to make peace with that is to say, I actually don't care at this point, I just want this to work on tags. Is it okay if it works on any tags?
And I think he said yes, so maybe I'll just change my code to make that happen. You can see there's some… some stuff around, like, picking up whether it's a tag or whether it's dev.
we can probably change that. I can look for if the current ref is main, then we're going to go for version equals dev, or something like that. And then we build it, we pass the version around.
And then, if we find out that we are inside a tag.
then we can actually do a little bit of work. And so that work is to build the packages, Debian RPM, and then make them available on a release, right? So you create a GitHub release, you download the artifacts you built previously.
We create the release notes, which is just a bash script that is running something called the changelogin with the.
putting everything to changelog.md, and then we make the release and we push the artifact as part of the release artifact.
What's cool about this is, okay, now you get an RPM and a Deviant package on your GitHub release page, and…
you're better off, right? You have a… you have a way to kind of make releases on a regular basis, because
we're only going to get feedback and user commitments from people, and really, like, some community also, if we are able to put out some actual deliverables. And people don't want to build the RPM by hand by doing.
**Bastian Krol** 48:50 Nope.
**Antoine Toulme** 48:51 Yeah. So, we need to make it available to them, …
So, if you're okay with this, I will just remove the requirement and just put it on any tag.
And we can make a…
We can make a dumb release first to try out more, is the release script and anything else?
And then we break everything, and we bring your Zeke stuff, or… I don't know even, like, we can… we can bring your Zeek changes first into it, so we don't even set a release out, so we don't put any….
**Bastian Krol** 49:21 I think it might not be bad to have one C release out first, but I also… I don't have any opinion on that, really.
Nope.
**Antoine Toulme** 49:33 Okay, well, just so you know, right, this is the work that was ongoing. I passed it, I went on vacation, …
we didn't really get a chance to catch up on that. This is finally… we're finally having a SIG meeting that is well established, so we can have those discussions. So, we'll continue… I will update that, put it up for review, feel free to review, let me know what you think.
And we can… we can lend that. Once your Z code is in there, I'm sure it's going to be the exact same approach. Maybe we'll pick up the artifact some other way, but that's the exact approach we have to take.
So….
**Bastian Krol** 50:08 Yep. Cool. Okay.
**Antoine Toulme** 50:11 Alright, I promise to get you a review by next week, and we can talk some more.
**Bastian Krol** 50:16 Yeah, I mean, review, it's a work in progress, right? So you might want to….
**Antoine Toulme** 50:21 Sure.
**Bastian Krol** 50:22 Keep that in mind while reviewing.
**Antoine Toulme** 50:24 Well, one thing I may do is, if I like a portion of your stuff, we could also just slice it as a separate PR, so you can get into main faster, especially if, like, you had changes you wanted to make on contributing MD, things like that, …
I'm in favor of just whatever we can get in that's safe, right? Okay.
Cool, cool. Sounds good.
**Bastian Krol** 50:47 Excellent, thank you very much.
**Antoine Toulme** 50:49 Oh, thank you. Thank you for your work. It's been, long running for you, so happy to see that in the…
In public, it's awesome.
**Jacob Aronoff** 50:58 Yeah, thank you very much for the work, and I don't know if you saw the, comment. I will also review. I'm eating lunch, so…
Didn't want to subject you to my, ASMR.
**Bastian Krol** 51:14 Okay.
**Antoine Toulme** 51:16 Alright.
**Jacob Aronoff** 51:16 Thank you both.
**Antoine Toulme** 51:17 Take care.
**Jacob Aronoff** 51:18 Yeah, have a good day.
**Bastian Krol** 51:19 50 rounds, bye-bye.
