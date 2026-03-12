SIG: SIG Injector
Date: 2026-01-26
Duration: 59 minutes
============================================================

## Zoom Recording Transcript

**atoulme** 00:12 Thanks.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 00:15 Okay.
**atoulme** 00:17 I see this agenda.
Sebastian said he couldn't make it today.
Joined by Cal. Cal is, works with me. Hi, Cal.
What is this?
**Ted Young** 00:50 How's it going, y'all?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 00:52 Hi, Ted.
**atoulme** 00:53 It did.
How's, how's the, unplug thing going?
**Ted Young** 01:02 It's going well! I'm actually… after this call, I'm gonna go pack, because I fly out tomorrow.
**atoulme** 01:10 Nice.
You're doing the whole postdamn thing?
**Ted Young** 01:13 Yep, I'll be there for Fostom… I think we're looking at maybe something like 100 registrations at this point.
**atoulme** 01:22 That's true.
**Ted Young** 01:22 plug. So, that's feeling good.
**atoulme** 01:25 Okay.
Okay, I'm not… I'm not going, but we're sending Erwin from our team. He's a… he's a field person, so he's very close to deployments, and so he's gonna have some really good feedback from customers, which is great.
**Ted Young** 01:41 Yeah.
**atoulme** 01:42 I'm sorry, you can make it myself.
**Ted Young** 01:44 No worries.
**atoulme** 01:46 Alright, we got the notes, folks, put your name down.
If you get a chance.
the thing, the… In the chat.
Okay.
Anything worth talking about? Anything from, all over?
Nothing.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 02:14 I mean, I was gonna ask if Bastian was here, do they need any help with, the Python work.
**atoulme** 02:24 Yeah, they mentioned several times that there is a specific issue in Python they want to fix. Have you… have you identified that with them?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 02:30 Yeah, yeah, but I see, like, they started working on a PR to have an optional, Python support, so you can enable it in the injectory if you want to be you know, sort of, like, YOLO.
Or maybe you have a way to determine that this is not a problem with a target Python application somehow through another tool.
Then you may want to enable the Python in the config.
So I was just wondering if there was any help needed on that.
**atoulme** 03:03 Okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 03:04 And there was one other thing, related to the injector environment variables. I can open an issue, but I just wanted to find out if this is actually useful or not.
The injector right now… doesn't have all these environment variables, which are kind of really useful. I really like them that you have hotel underscore injector, and then service name.
Because that allows you to not override anything that is… maybe the application is setting up themselves.
**atoulme** 03:33 There is no one for node name.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 03:36 So… I was just wondering if… Any opposition to adding that?
**atoulme** 03:43 Interesting. Interesting slippery slope, right?
I don't really have a say about that one. The hotel injector stuff kind of came about, I think it looks like it's a… it's a bit of a… It's a missed number of configuration. We don't have a schema for it, we're not trying to comprehensively do anything at this time.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 04:03 Good.
**atoulme** 04:04 So yeah, you can open an issue for it first. I think we can add that, that's not… that's not the end of the world, at this stage. However… I was hoping that we would start not to invent anything with the injector, and that, you know, we would be able to use declarative configs and whatnot, and just pass that in without doing anything ourselves.
But that's… it may be too much to ask.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 04:31 I mean, it's possible, I… I find it, yeah, with a declarative config, there's such a thing that we can easily add these things in there.
I was just thinking of the state as it is right now.
I think these, Like, additional variables that sort of, like, hey, if the application didn't set up service name.
Then the injector can set up.
Its own service name.
Based on some other tooling that tells it what should it be, right?
**atoulme** 05:00 There we go. Alright, so then the slippery slope is accelerating, because now the service name based on actually running something like, let's say, a little thing in your Kubernetes cluster that's doing the actual review, or EC2 is going to start to look up using EC2 metadata model, all the stuff, right?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 05:18 But it's meant to be used by other tools, like, so if you think about the hotel operator.
has an algorithm to figure out what the service name should be. That's true. Based on… you know, attributes, or labels, and so on. So, it's nicer to have this being passed in down to the application.
In an environment variable that does not conflict with the auto service name, because if they have set it up somehow already, the customers… there's no conflict. At the time of the injection, or in the LD preload, you can check to see, oh, they've already done it. We don't have to do anything, they want to have this name, this.
If not, then we can supply this additional. So it's really useful when implementing something like an operator.
And one that I noticed was missing, which the operator does, is node name, and… I mean, there's the pod name, the pod UID, the container name, all that are available, just not the node name.
So.
**atoulme** 06:26 But the operator does that. Is that what you're saying?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 06:28 Yeah, the operator could inject the… it will set the node name as well, but it would be nice if the future operator could
**atoulme** 06:37 Yeah, did I get that to that?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 06:38 Yeah, we can actually use the same mechanism for no name as well. I think it's a minor thing, honestly, it's just, not the end of the world, but… It would be good if, we could inject that as well. It's the only one I found. I started looking at it, and the only one that I found missing was this.
**atoulme** 06:57 Okay, so let me just take a note of that.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 07:02 So it would be, like, go to Injector Kate's node name or something, just like we have pod name. I can put it in the notes, so…
**atoulme** 07:10 Yeah, I mean, the only problem I have with this is just, like.
How this allows us to do some computation, such as reviewing those variables and setting them, and how… How do you even do that.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 07:22 I think it's, for example, right now we have this… that copy-paste from VS Code did not end up too great.
**atoulme** 07:30 Listen.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 07:31 Let me… let me see…
**atoulme** 07:32 Come on, Shift-V.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 07:34 We have, like, hotel, an injector… It's… bar name.
exists.
And so does log UID or stuff, right? Or a namespace name.
Those exist currently, so I'm just like… so we had… Interesting.
**atoulme** 07:59 Let me see, how's that doing right now?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 08:06 Finance.
It's quite handy, I have to say. Like, I started looking into how we implement this in an operator in the future, and…
**atoulme** 08:27 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 08:28 It's… I like that. I started by setting these things directly, but then… I'm like, yeah, what if the thing… the application overrides it somehow, or it's pulling from an environment variable that's… you have to go and check all the environment variables, right? Because it's not… at the time the pod is created.
A lot of these things don't exist, right? You don't know the… it may be said.
**atoulme** 08:51 Yeah. It may be set with a reference.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 08:53 to something that's correct, so it will be correctly evaluated, but it may be that customer made a mistake, and it's set to a reference to something that doesn't exist. So you're gonna evaluate nothing, so the service name will not be set. So having this kind of, like, a side channel where the injector says, if you didn't set it, I can do it for you, it's… Pretty neat, in my opinion.
**atoulme** 09:15 But that's… That's not really what it does, does it? Because it's just assuming that this pod name variable is set.
It doesn't actually set it, it's not set anywhere in the injector code at this time, is it?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 09:27 Correct, no, but if you're an operator, you can inject these, and they will never conflict with whatever the developer initially intended to do with these variables.
**atoulme** 09:39 Okay, now that makes sense. Yes, so first off, yes, that makes sense, because the contract now makes more… it's more clear.
But this becomes an API for how the operator should be interacting with this as a… Almost like a… SPI-type interface, right? It's just, like, how do you configure the injector so that it does additional resource attributes passing?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 10:03 That's right, but it's already there in the code. I mean, I guess there's zero needed for their own operator, I imagine?
**atoulme** 10:08 Yeah, yeah, it's just a set list of things. Interestingly, you can also just use the auto-injector resource attributes, and you wouldn't need to have all those specific settings. Why do we have why do we have those specifically on top of the resource attributes? Which one is taking over the other one? And why do we care?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 10:29 I actually don't know. No.
**atoulme** 10:31 Because you can just say, okay, the operator's going to set auto resource attributes, here is one variable.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 10:37 Hmm.
**atoulme** 10:38 Never come back, right? Don't ask me for more. Why do we need to spell them out one by one?
Thank you.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 10:45 Alright.
That's a valid point, yeah, I don't know.
**atoulme** 10:49 Okay.
Alright, so, but anyway, it's missing right now because of this contract being very explicitly spelled out, and this particular option missing. Okay, fair enough.
**Ted Young** 11:00 Just some backstory, the reason, if you're talking about MVARs, it's, like, resource attributes is really for, like, programmatic You know, humans don't like to interface with that.
Humans want a program having a bunch of individual ones.
So, since we're doing programmatic stuff, just using resource attributes and stuffing everything to there when we can.
**atoulme** 11:24 Makes a lot of sense. Yeah.
Yeah, because you're… you have this surface of all those things, like… I can show my screen.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 11:31 Yeah, yeah, there's quite a bit of them, yeah.
**atoulme** 11:33 I can make it more poignant by showing this, I think.
So you have auto-injector resource attributes, where you can shift anything you want, right? Just key-value pairs of anything you want to set at the resource level. And then we go to the pane of listing all seven here.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 11:49 Hmm.
**atoulme** 11:51 And then we do some specific things for that, so I need to understand which one is taking over which.
It looks like…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 11:58 Yeah, I've looked at that. It's actually not there to not override anything said by the application.
**atoulme** 12:04 But you have… Yes.
Okay, I need to read this more carefully.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 12:11 Yeah, that one is quite clever, actually. It parses each pair, and then checks to see if the pair is available in the original resource attributes, and if not, then it sets it.
It's… quite neat, yeah.
**atoulme** 12:26 Well, that makes sense too, right? So, yeah, I really set this, keeping it pending, okay, fair. But the fine print here for me is more like, why do you have both auto-injector resources and auto-injector Kubernetes namespace name.
Where you could just set a key of Kubernetes namespace name under Autojector Resources Tributes and be done.
Why did you bother…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 12:50 Yeah.
**atoulme** 12:50 It is fair, yeah. That's… it's a point of detail, but it's just… it's creating this grating moment when you… you say, okay, we missed one. I'm like, okay.
What else can we miss?
Okay.
Okay, fair enough. Oliver, like, we could just add it for now, and make it happen so it's easy, and then later on, we can have maybe a different approach, but it's not… it's not the end of the world.
Anyway, that's the situation we're in for that.
I think this is… Yeah, it's very community-centric, that's fine.
Okay.
Okay, Nikolai, let's… let's do it, and then let's see you later how we… how we deal with this.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 13:34 Thanks.
**Ted Young** 13:35 I think, Jack, you had your hand up.
**Jack Berg** 13:37 Yeah, I… I'm still trying to understand what the point is of the… that class of environment variables, the hotel underscore injector ones. We have this other mechanism that seems, at least partially to overlap.
the, auto instrumentation ENV, or Default Auto Instrumentation ENV comp file, and, you know, the mechanism there is that any Environment variables, as expresses key-value pairs that you put in there, will be injected into the application.
You know, the point of that was to kind of solve what seems to be, like, a theme of that last conversation, which is like, hey, we don't want to have an explicit list of environment variables we're going to inject. We're going to support injecting all environment variables from a central place that have the hotel underscore prefix, and that's what that file facilitates. And so, like.
you know, I know these things didn't get developed at the same time, but do we need both mechanisms?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 14:36 I would say yes, and hear me out.
If you, say, want to practically implement this in an operator, right?
You would like that config file about what's instrumented to be done once.
You don't want to be injecting a separate config file to every pod that comes in. That requires a copy and all these things. Right now.
the operator does copy, but there's ways to make it without copy. So, you want the configuration about the SDKs and everything else, like, the defaults of what was happening, to be done once, and this config file is just part of what you give to every pod that's launching.
But with environment variables, you control things like this resource information that… to help the application name itself better.
So it's not called, like, unknown service.
**Jack Berg** 15:28 Yeah, but, like, why… so, like, you know, like, let's… I think there's two kind of separate issues that I'm detecting. Like, one is, okay, the injector, or the operator, wants to inject application-specific contacts into every pod, and, and so we have a mechanism for that with this you know.
default auto instrumentation ENV comp file, but then there's a separate issue about, like, hey, you don't want to, I think you were saying, like, you want to mount the same sort of config to all places, but then have the ability to have, like, some config, which is sort of application-specific?
Right?
You kind of want to have a layered approach, some config that's, like, common across everything, and then some that's, like.
Contextual to the specific application?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 16:19 Well, I should say files are problematic.
When it comes to operators.
The reason why they're problematic is because They need to exist in a volume, and this volume needs to be mounted, and this mount, you need to copy the thing.
And so, that creates, like, complexity around each deployment.
While environment variables, on the other hand, are just easy to add as you're mutating your.
bod, and those actually take an effect immediately through the application, right? So, it's much easier and much cleaner to do that.
So I'll give you an example. Right now.
**Jack Berg** 16:56 Yeah, no, I buy that. I buy that, right? Like, that, like, you know, files are inconvenient compared to EMVs, which are part of the, you know, the Kubernetes.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 17:03 Resource. Resource, right? Yeah. And it's so much easier, and you can easily make it per pod, right? This pod should get this name, whether config, copying to each pod, now individual config, and making it on the fly, it's a lot more complex for something like an operator That needs to fake up this file, cop-drop it somewhere, and so on, right?
**Jack Berg** 17:25 Yeah, so the injector is kind of used in two contexts. It's used in, like, bare Linux, and in bare Linux, it is useful to have this sort of, this default auto-instrumentation ENV comp file, so you don't have to modify the environment variables of all your processes, right? So that, you know, that comp file is optimized for the bare Linux case, and, you know, the other context that the injector operates in is in Kubernetes, and in that case, it's much easier to work with ENV.
environment variables. And so, I think, like, you know, the approach I'd advocate for getting towards is, like, you know, it's like the ENV side of things has actually fallen behind the comp file side of things, because with the configuration file, like the default auto instrumentation ENV comp file, every environment variable is supported, but for environment variables, it's just, like, a whitelist, or an allow list of, like, six or seven.
So that seems to be the problem, that you can't express all of your environment variables, it's just a subset of them.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 18:19 That's right, yeah.
I mean, it could be done better in a way that anything that's prefixed with hotel injector, but we can talk about that, yeah. Yeah, right. Yeah. Yeah.
**Jack Berg** 18:30 like, some sort of find replace. Find hotel injector, strip off the underscore injector, and inject that.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 18:37 Yeah, could be made more generic rather than what's happening right now, yeah.
**atoulme** 18:43 Lovely.
Did you got your own hand up.
**Ted Young** 18:46 Yeah, I mean, I was gonna say, I wrote the scheduling system for Cloud Foundry, and we hit the same deal. The file systems are poison, so you end up injecting everything you want to inject as, like.
you know, JSON-encoded environment variable thing, and if it's something simple, like… like, resources or something, that's easy enough, but when that Turned into, like, a hairball of, like, nested stuff.
it starts to become its own hell. But… I did want to raise my hand and just ask how much what we're doing is in line with the new comp file format.
That… that configuration SIG has been working on.
Because I almost wonder if there's a way to match what they're doing as far as, like, how our configuration works, and almost if we're gonna have to, like, inject that stuff through environment variables? Like, talk to that SIG about, like.
Because we're trying to go to a new world, also, and kind of abandon this old hairball of MVARs. So I almost would want to check in with them and be like, do we want a new MVAR, or a new, like, how do we deal with injecting this comp file?
When we can't use the file system.
Because that's just gonna come up… everywhere once we start switching to that form of, like, end users handing us their configuration. And if the answer is, like, you take that and have this, like, horrible matrix of trying to figure out how that maps to the old stuff.
Anyways, we should check in with them, because they've probably thought about this stuff. Man, we should all do it the same way.
**Jack Berg** 20:44 I'm here.
**Ted Young** 20:48 So, yeah.
**Jack Berg** 20:49 Let's… I guess let's get specific, because, You know, the… we were just talking about this default auto, or what's the… What's the file called? Man, it's named so… Strangely to me. But the… Sorry, what were you saying?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 21:19 There was a default end? Is that…
**Jack Berg** 21:21 Yeah, the default… default auto instrumentationenv.conf. So, like, anything you put in there will get injected into your, injected as environment variables. And the way that the declarative config mechanism works is there's an environment variable that points to the path of your conf configuration file, your configuration YAML file, and so, like.
there's nothing in the injector right now which is at odds with that. You could put in this, this, you know.
Default.
auto-instrumentation ENV file, the environment variable called hotel config file, and then point it to your path for your declarative config YAML, and it would just work. And so you could have a declarative config YAML file that is, like, you know, bundled in with the injector, if it became broadly, you know, or if, when it becomes broadly, adopted amongst all the languages, and maybe the default auto-instrumentation EMB comp file could, like, have that set up by default, right? So, you know, we're sort of pairing these together, and the out-of-the-box installation of the injector uses declarative convey.
**Ted Young** 22:40 Another thing that comes to mind on that subject is we're probably gonna end up in scenarios where there's more than one thing trying to drive all of this.
Right? For example, someone might… I'm even thinking in terms of Grafana Labs, right? Like, we might have some cloud product for adding and modifying instrumentation, and there may be some way to install this stuff through package management, and there may be, you know, the operator trying to do this stuff.
And we should probably make it work in a way where these things are either all driving the same stuff under… or they're all in agreement about where all that is, so they're at least aware of each other, or at least if they're all driving the same thing, you don't have multiple versions of it.
Running.
**atoulme** 23:29 That'll make sense.
**Ted Young** 23:30 Yep.
**Jack Berg** 23:31 in, the OTEP that was opened up back in December about, Packaging.
**Ted Young** 23:38 Yeah.
**Jack Berg** 23:39 proposal.
Yeah, did you see that?
**Ted Young** 23:43 I did. I did.
**Jack Berg** 23:45 There's some thought that's been given in there about, like, how packaging interacts between, you know, vendors and, you know, just sort of vanilla open telemetry situations, and how vendors can selectively override their own distributions for things, so I think it's pretty relevant.
**Ted Young** 24:03 I think we can take a very Linux-y approach to how we do all of this, and it will work fine. Like… It's not a… not a new problem.
**atoulme** 24:14 It's not. But yeah, it would be awesome if the Splunk distro was installing first the upstream version of something that is well-maintained and known, and then we add 5 files that make sense for us because we're special, and we just make it so that it's our own problem on top of it, so… If someone was to use OpenTemmetry natively before they adopt us, we would be saying things like, you can just keep using exactly what you had, we just install on top of it our distribution, so you can get, like, 20% more features, because we know better.
I don't know, right? And then it gives us the ability to kind of continue to work together. But having a no-fork policy for a vendor is probably going to be great for that, right?
If you start to fork the package, then we're dead. It's never gonna… this place is just balkanize. We'll just create… everybody's just going to have their own SDK for a .NET, and we'll never be able to make it happen.
So, yes.
But, anywhere.
Open source is needed, because I don't think we've won yet. I don't know if you… I was just putting myself through reading the article from Austin yesterday this morning, and it felt like we were pretty far from graduation, just reading it.
Just the amount… the challenge is huge, right? To… to have a proper story for the… for folks to continue to adopt us.
So…
**Ted Young** 25:49 I've got faith.
It's mostly cleanup.
But I haven't read his latest thing, so maybe he spun it in a way that sounds really intimidating.
**atoulme** 26:01 Yeah, it's just that one thing that I'm been repeating around the company for a while is that there is a hype cycle from Gartner.
And it's been defining every single interaction I've had with technology in my career, where you can get away with a lot of things in the first phase of the hype, where things are just exciting, and people are like, you couldn't do that before, now you can't.
And there is this moment where things are really, really, like, you know, are hyped up to the point where it's unreasonable. And I would argue that OpenTeometry has been like that, like, I've been really impressed with how far OpenTeometry has been able to get with it.
And then there's a slew of delusionment, which is somewhat like showing up in Reddit and Hacker News and some places like that, where people just tell you how bad things are because they tried it, and they, you know, the actual… Realization does not match the hype, and they got issues, and it's, you know, all the problems, the fragmentation, and then at some point, there is the actual utilization, right? So there's the first up, then way down, way too fast, and then overall, like, actual utilization, which is silent, and people just commoditize it, don't even think about it.
I'm worried about that. The slew of delusionment is where you can lose a lot of momentum, and things start to crystallize. People just, like, clam down on things and be like, okay, we're not gonna change that anymore, because we're worried that we did not deliver the thing that we said we would 3 years ago, and therefore people are going to kind of come after us.
**Ted Young** 27:28 So, so I see there being, like, 3 existential things that OpenTelemetry has to solve right now, and graduation solves 2 of them, and we solve the other one.
The first one is exactly the one you've talked about, this trough of disillusionment is absolutely coming to open telemetry if we don't do something about the installation experience.
If we launch a totally new take on how you install and interact with OpenTelemetry for the first time, especially one that addresses this kind of second audience that just wants it to kind of work, or has, like, an operator who kind of wants to manage it all for them, not the devs. Like, I really feel like we're providing that. And I do believe that if OpenTelemetry tried to trundle along for another year or two without providing that, that would create… Like, we… it's just like the forest with all the kindling, waiting for lightning to strike on social media is how that would feel to me if we didn't… Do what we're doing now.
The other part is, like, getting everything truly stable, right? So, this is just feedback we get from end users, is, like, we have all this stuff. Like, when you download it.
you get a mix of stable and unstable stuff, and if you cut out all the unstable stuff, that's, like, most everything. So just, that's actually the biggest thing for graduation, is just getting that straightened out.
And then… The third thing is just the actual quality of the data, of the telemetry. We've, like.
we're stabilizing all of our semantic conventions, all of that stuff is really getting dialed in, but I still think we have a lot of actual instrumentation packages out there scattered across the languages that are all in, like, various states of, you know, they emit whatever was around when they were first written.
And so, finding the resources to bring that part up to speed. I see those as, like, the things. And if we've gotten all of that battened down before the storm hits, then, you know, we trundle along and it's okay. But if we leave any of that hanging around.
For another year or so.
that's when… yeah, people start thinking, well, maybe there's something past OpenTelemetry we should be trying.
That's my personal take on… on where we're at from talking to lots of people.
**atoulme** 30:01 I have a twist for you, and maybe we can bring it up at that Hotel Unplug thing next week.
**Ted Young** 30:06 Yeah.
**atoulme** 30:06 I think we're missing a support SIG. I brought it up before. We want to be a product, and a defining feature of a product is that it has an avenue for support.
At this time, if you have an issue with anything, and I mean anything, just, like, you get a stack trace, or an exception or a panic in something that you run, which may or may not be open telemetry. Like, you don't even know anything, like, just look at this, it's an error.
You wouldn't know where to go in OpenTermity to get some feedback and get some help.
**Ted Young** 30:38 That's definitely true, right? We don't… we don't have an explicit way for, like, regardless of who you're going to support for, if you want hotel support.
What button do you push to cause open telemetry, whatever the hell that is, to, like.
cough up a file that you then hand to somebody, so there's some kind of standardized way of…
**atoulme** 31:01 Death.
**Ted Young** 31:02 We used to agreement on, like, what the data is.
**atoulme** 31:05 Yeah, so how would you want to do this? I think there's a SIG there, and I think that SIG is just triage.
And all it's doing is it's making sure it's going to the right SDK managed and somehow tagged with a stable release, timeline. So… Alright, this is a bug, this bug is in, you know, 25.3 of some, like, subcomponent of some .NET SDK. Between the moment that this bug is filed, then fixed in that SDK, then released, then managed with the injector, then open with the operator, then available for you to go.
How are you going to make that so that people can actually understand that the fix is available?
That's a really hopeless discussion for them.
**Ted Young** 31:48 This conversation is going into Support Nightmare Swamp, and I'm gonna try to, like, back the boat. Just because, like, this also runs into, like, why companies feel the need to have, like.
vendor forks of everything. A lot of it is related to, like, support contracts. So it's not just, like, how do we solve this in, like, OTEL? Like, there's, like.
Literal legal contracts, everybody's signing around who supports what, where, and how, and like… Part of what we have to figure out in OTEL is, like, how to support vendors who need to have this extra layer there, like, legally with their customers.
So…
**atoulme** 32:28 Yeah, but I mean.
**Ted Young** 32:29 Not simple.
**atoulme** 32:30 Even without a real support case, right? I was asking, okay, so we had a… There's a RabbitMQ enhancement which was made available to a beta release of a .NET instrumentation in September, which was then repackaged into the RC1 of that instrumentation, which was eventually released, which was eventually wrapped into our own distribution, was made available to customers.
**Ted Young** 32:54 Great.
**atoulme** 32:55 Feedback from customers, I have no idea what's in this release.
feedback to my developers, you need to inline every release notes of everything you depend on, so that people can understand what you've done.
feedback from my developers, go take a… go take a walk. We're not doing this.
How do we do that at the hotel level is a very important, poignant problem, because, you know, let's say you have a problem in your config sig, you want to fix something, and it needs not to permeate everything all the way, right?
**Ted Young** 33:24 Yes.
**atoulme** 33:25 So you…
**Ted Young** 33:27 I was just pointing out, the solution, unfortunately, isn't as simple as, let's get a triage SIG and get all the different vendors and organizations to, like.
staff it. I mean, I think that's a great idea, but you're gonna then run into, like, how these… all the organizations that fund OTEL have their own way of doing support, and we have to…
**atoulme** 33:48 I didn't say that we're going to stuff it with vendors. I didn't actually volunteer you guys, right? I'm not… I'm not trying. What I'm saying is that if you want to button the hatches, if you want your product… if you're… if hotels are supposed to fill, like, a product, and you want to button the hatches because of the slew of delusionment coming up, you'd better have a story about support.
That's all.
**Ted Young** 34:10 Yeah. I don't know that OTEL needs to feel like a product, though. It just needs to feel like… like a well-run open-source project. That's what people want. I think some…
**atoulme** 34:20 Cool.
**Ted Young** 34:20 People come to it, and they're like, it's way too hard to… You know, it doesn't have, like, that smooth experience that… Some open source projects have, when you get started.
**atoulme** 34:33 Yeah.
I…
**Ted Young** 34:35 The other part is the data that it puts out, and then the last part is performance and things going wrong and stuff like that, but that third part is, like.
That's people really using it, that's not people trying it and failing and walking away.
It's the installation and the data that are blocking people from trying it, and I think that's why we have an adoption gap between, like, hotel hype and hotel adoption. There's a lot of adoption, but I feel like there's a gap between the adoption and the hype.
Getting it back.
Anyways, we're pretty off-topic for this sake.
**atoulme** 35:16 Damn.
Okay, yeah.
**Ted Young** 35:18 I had one thing on the agenda, Real quick.
So, we've got Bostum, we've got Hotel Unplugged coming up this week.
What should I be trying to get people to try right now? I mean, Fostom in particular is a great place to get people willing to YOLO some Linux packages, right? So… Is there, something helpful for this SIG I can do while I'm there, as far as, like, poking people to try things and give feedback, or get involved?
**atoulme** 35:53 Yeah, so… we had to… when we did our demo at KipCon North America.
we actually had a demo from Jason Plum, And I think you could really just use that as, let me find it… Oh no, it's got 5 things. Let me find it.
So you could… you could just give people that to play with, right? It's all, like, container… actually little VMs-based. He went all the way to running actual VMs, because this way you could actually run the… the… the little integration we have, as a preloadso.
Let's see… Yeah, so I went back too far.
Injector demo. Here we go.
And what's interesting about that demo that's using both Java and Node.js.
So this is a really, like, cookie-cutter view of things that can be useful.
Do you want to see the… do you want to get a link to the slides as well?
**Ted Young** 37:26 Sure, yeah, if you got them.
**atoulme** 37:30 That might be a good compliment, otherwise.
Funded.
Yeah, I would assume I had these here, but it's all, of course, it's on my other… Count.
**Ted Young** 37:51 I feel like I have not just OTEL Unplugged, but sort of, like, a run of, like, places where I'm giving hotel talks coming up, talking about this stuff, so…
**atoulme** 38:01 Yeah, makes sense, right?
**Ted Young** 38:02 or the more easy-to-show demo stuff. We're kind of… we're hitting that phase of our hype cycle.
**atoulme** 38:10 So… Yeah, a lot of questions about OB too, right? So, a lot of people are conflating Injector and OB because they feel a bit the same.
And so there's a risk there, that people can be lost in a hole of mirrors when they're like, okay, what are we… Which one is it?
**Ted Young** 38:29 I feel like… but, like, Complete successes, no one has any idea.
**atoulme** 38:35 Yes.
**Ted Young** 38:35 Right? It's just Linux packages, and it works. So, in some sense, we want to lean into that, right?
**atoulme** 38:42 Absolutely. So… I'm sharing the slide here in the chat, and I just want… I mean, I'm so proud of this first slide, because I put the Pontamino and a Prius, and you know, trigger people properly.
So…
**Ted Young** 39:00 The CMCF may come after you for trademark.
**atoulme** 39:05 Yeah.
That's a terrible logo. I love it.
This is even worse. Someone afterwards made me think… told me, like, hey, did you see that the front wheel doesn't work?
This is terrible AI, what are you doing?
I'm like, oh, well, those slides came together really well.
Last minute.
**Ted Young** 39:27 It's also great.
**atoulme** 39:29 it's a stupid theme, but I put Fast and Furious Adoption because I was like, you know, the day before the CFP was closing, so I really did not put more thoughts into the title, and then I had to execute on a Fast and Furious franchise. So if you look at the demo, it's actually using Fast and Furious characters and Fast and Furious cars, and you can pair them. That's the demo.
That's what he did. And Jason had no idea what Fast and Furious was, so I had to explain to him what… who Vin Diesel was, which is a fun discussion to be had.
I think he forgot everything afterwards really quickly.
**Jack Berg** 40:04 Jason Plum has been living under a rock for 20 years. That's impressive, like…
**atoulme** 40:09 periods of power.
**Jack Berg** 40:10 pop culture.
**atoulme** 40:12 Yeah, it's in the 90s.
But, generally, he makes his own music.
He's making his own instrumental radio station on the web. He's a busy man.
Anyway, okay, with that, you should be well equipped to at least, have discussions at first them, and then show a couple of those slides. There's some discussions, yeah.
**Ted Young** 40:35 exactly what I wanted to direct people to. Thank you.
**atoulme** 40:39 You're welcome.
What else?
What things to try and unplugged?
I think you should just tell the SDKs people, like, I like what you did, like, you had a maintainer sync meeting where you came up with a… I think all SDKs should have a charter with renewals, all instrumentation SDKs should be kind of checking in with us, what is happening, and kind of get a direction and a roadmap. And, I think an item in the roadmap of each SDK should be, you need to abide by declarative config sig.
Because that's a prerequisite for the discussion we're having on the injector and the operator. And the next one is, you need to be playing along with what the injector SIG is trying to achieve. And kind of come in and make sure you support that, and give us ways to test that your stuff is working.
**Ted Young** 41:28 Great. But is it… is it only Python that… that we have a… an issue with right now, in terms of… Injection?
**atoulme** 41:37 Yeah, that's a big one. The others, I mean, Google will never really support this, because they don't allow that. Ruby is kind of immature, could use some help.
From the maintainers, but we never really asked for them to kind of stop what they're doing and come and help.
**Ted Young** 41:54 They're missing something that we need, or… or…
**atoulme** 41:59 So the Ruby guys, they came to the operator and said, we're ready, let's go, let's engage. The people from the operator said, we have absolutely no bandwidth for you, we cannot help you at all. You need to do all the work together. And so they made a PR, and the operator people were still bulking at the size of the PR and saying.
how do we maintain that stuff? This is too much work. So I took it up, and I tried to make it so I could actually test that, and I cannot build a program in Ruby to test this in a way that I like. When I asked them for guidance, they said, why don't you run Rails? I'm like, seriously? You want me to run… no, I don't… Nope. I'm not doing it.
find me a better way. So that's a problem we're having, is like, how do we make it so that the automation tests we want to run with Ruby are kind of off-the-shelf, easy for us to understand and maintain?
That's all. There's just this weirdness with rails that I cannot, you know, get over, with the spare time I have.
So there's a abandoned PR on the injector repo for Ruby. It's been sitting there for a while. I think we probably closed it at this point, because with the rewrite in Zig, everything kind of was, you know, redone.
**Ted Young** 43:13 Open.
**atoulme** 43:13 I think that's it. If you have, like, those… those programs are good enough to get the majority of SDKs on board.
Tell me, is there anything else we need to.
**Ted Young** 43:24 PHP.
**atoulme** 43:25 PHPR, yeah, PHP is a good one.
No idea.
Never tried.
I don't think the operator people ever tried.
So…
**Ted Young** 43:36 Potentially a weird one.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 43:38 Yeah, but also, like, I think Python is an important one, much more important than these other languages, right? I mean… I don't know how many people are on PHP and Kubernetes. Maybe a lot, but I don't think so. I mean, it's… It's not one of these apps that you scale up and down, and same for Rails, I don't know.
**atoulme** 43:56 These are going to be host-based things, like, this is going to be a WordPress on a host, not a… nothing else.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 44:05 Yeah, so it's important.
**Ted Young** 44:08 We've got 50 legacy apps that…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 44:11 No one's…
**Ted Young** 44:12 We have to touch, and we need them auto-instrumented, that's where a lot of.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 44:16 Right.
**Ted Young** 44:17 Sub.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 44:17 I keep, yeah, I keep thinking Kubernetes, man, I'm sorry, yeah.
**Ted Young** 44:21 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 44:22 They're not important for Kubernetes, but they're important for their host-based instrumentation a lot, yeah.
**Ted Young** 44:28 But I do agree with you, Python is still the most important thing for us to get working. It's kind of not real until it works with Python.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 44:35 Yeah, and the way that the world's going with this AI workloads and stuff, Python is… you can… you can say probably the most important one, right?
Apart from Java.
**atoulme** 44:47 Yup.
Yeah, if you manage to get a Python maintainer, you can have, commit to simplifying things and supporting JSON, that would be the best. I think that's what's missing the most.
We're not going to fix protobuf on Python anytime soon, so we should just use HTTP JSON for now, and be good.
Yeah, I think that's it. I think that's already a lot for that unplugged agenda, frankly. You have only one day.
**Ted Young** 45:20 Oh, yeah, for sure, for sure.
more… in terms of OTEL Unplugged, it'll be just kind of trying to communicate a roadmap to people. At Fostum, that'll be… I'll be, like, maybe poking people to try this stuff, but… Yeah. Yeah. As far as, like, roadmap, that's maybe if we've got a couple minutes.
**atoulme** 45:45 No, we should make a blog post about that. I saw Obi guys made a blog post on goals for 2026, and I think we should do the same thing, so… Yeah. I'm very late on making a bunch of blog posts happen, actually. Very lazy on that.
I mean, 1.0.
**Ted Young** 46:02 Yeah, kind of, like, letting people know what our expectations should be for kind of the injector, the operator, and package management. Like, because those timelines.
**atoulme** 46:13 Yeah.
**Ted Young** 46:13 Kind of different, right? And to also know where people can… can help out if they want to accelerate how fast it moves.
**atoulme** 46:23 I think the fast track is the operator.
And this is really where Dagio people are scaling at this point. They do not want to maintain their own version of everything, and they would much rather have the operator be, like, the place.
Which makes a lot of sense. And the best part of this is that the operator can accommodate those changes without, having a breaking change, or a… it may be either a different type of instrumentation, so people have to opt in, or it will be hidden under the hood and people won't see a difference. So that's good.
**Ted Young** 46:54 Don't they have, like, a big overhaul that they want to be doing right now anyways?
**atoulme** 46:59 So the big overhaul is the managed CRD, which is just also, the operator people have played LEGO. They say, okay, we're going to give you a bunch of construction. We'd like a collector? Okay, send some YAML, I will set the collector for you.
Would you like to set an instrumentation CRD with which language, what filter, how you want to apply it, and it's going to work the right way.
And I came in and said, hey guys, no one cares about you playing Legos, they want the cathedral.
tell them, and so the managed CRD is.
one CRD that says, because you designed that your cluster is now managed, we're going to define all the CRDs for you.
So, we're going to deploy collectors as Demon said, boom. We're going to deploy collectors as cluster receiver, boom. We're going to set all those limitations for you. It goes to the product experience again, where we say, we know what you want, we know you don't have time, install this one thing, and it does everything for you.
And it's composable, meaning that if you decide that you don't like what the CRD is doing, pull it out, and then start to customize your stuff, or do things on top, right? But for the most part, what we expect customers to do is to say, I actually don't care how things work under the hood.
And… I'll just deploy this and be done. And this is on par with the feature set you get from a Prometheus operator.
The Prometheus operator on OpenShift is default installed on every OpenShift cluster, and that's why people use Pometheus.
And it would make sense for us to get to the same level of parity of simplicity, not feature… the feature parity doesn't matter. How easy it is to use is what matters. And that's what we need to go to.
So that's a discussion that is… and frankly, thankfully, it's actually separate from this discussion about the injector, because you… you get to there however you want, right? Whether it's the injector underneath or whatnot. The interesting part of this is that the configuration section of your operator becomes, turn it on, be done.
So, you know, people complain, oh, I'm not seeing the exact same, you know, resource attribute I wanted, and I want to go, like, deep, like, 3 layers deep inside this. I'm like, okay.
Gloves off going there.
you're learning YAML.
I don't care about. You're already on your customization.
Okay, so… Yeah, for goals for this year, $1 release.
Operator integration is a big one. I would not hold my breath on having packaging for Linux being solved this year.
Unless there's a traumatic event, and someone just starts to make fun of us on HN for 3 weeks straight, and, you know, garners hundreds of points because they're like, upper telemetry is dogshit because it takes 5… 5 jars to install stuff, and I can't possibly run this, and I don't know, I got myself cut because I'm using the wrong version of Python, and those C dependencies didn't work the right way for that Unless we get to that level of bashing from the community, we will not see a wave of people telling us to standardize on our packaging.
I might be wrong.
But it feels like it's further away than the Kubernetes story.
**Jack Berg** 50:13 Yeah, the packaging OTEP is, I think, sort of indicative. It's like, I think there's several good ideas in there, and, like, I agree with the direction, but there's not a lot of people that are, like, engaged with it.
**atoulme** 50:25 Yeah.
Bye.
It's the difference between love to comment on it, and then, yeah, let's actually do it.
**Jack Berg** 50:34 Well, not even… not even very many commenters. Like… So, yeah, I think I'm kind of with you. I would like to see that happen, but I think we need to feel more of the problems more severely before people are motivated.
**atoulme** 50:54 We might even do a first cut that doesn't actually fit into everything he wants.
I think… I think it's actually asking too much of a first cut in that OTEP. The OTEP is drafting a very optimistic, like, multi-year level of consolidation of our stuff.
Whereas the first step could be, hey, here is an RPN that installs every single thing that OpenTentry has to offer.
It doesn't do anything else, but it just installs everything. The collector, all the SDKs you ever wanted and didn't want, and everything that you didn't ask for, like, we're just… we'll screen a target allocator in there, too. You don't know what it does? That's fine. Don't worry, just, you know, stick with us.
Well, we just made sure it somewhat works together, and that's our first pass at this.
**Ted Young** 51:42 Yeah.
**atoulme** 51:42 And then people are like, I hate you. I'm like, I understand. Would you like this to be better? Yes. Okay, come over here.
Let me introduce you to GitHub. Let's how it works.
**Ted Young** 51:52 I mean, I think we can build that thing and define how we want it modularized at the same time. Like, I think it's… Yeah. At least defining where we want the bits to go, but…
**atoulme** 52:04 Start with the experience, and then back out into the possibility over time as a justification for feedback from customers.
Yeah. Users.
Anyway.
Yeah, so that's a lot for goals already.
**Ted Young** 52:22 Okay, so… we're… Coverage, Java.NET, Python, Node.js, I think, we can cover as well, and we don't know about Ruby or PHP. Not saying we aren't going to cover these other languages, we're just saying that's all a question mark, but… If we could cover these four.
We're gonna get it working for the operator, and we're gonna issue Debian and Red Hat packages.
That… install all of this stuff. I guess, also, like.
Collector and OB, we're gonna say in here, as well.
We're gonna have all of that.
**atoulme** 53:01 Yeah, we could try that. I think we need an uber RPM that is just dependent, you know…
**Ted Young** 53:07 That's… that's what I'm thinking, that's in that… we're gonna build the… Kitchen sink one first.
And Kitchen Sync won't be everything, only because it won't contain some SDKs.
If we haven't gotten them.
Working in.
**atoulme** 53:25 I'm excited for that, because I think it would… it would bridge over a number of people who are just, like, sitting around and not… not coming… not committing yet.
**Ted Young** 53:35 This is, like… a little random, but I feel like getting this really working with Linux is great, and I think… people have so many opinions, and it's just gonna get worse in terms of where their bits come from, and I actually feel like going this route also unlocks a door into… Working with all these different big organizations in terms of how they want to manage security and scanning for all the bits coming and going.
**atoulme** 54:04 Yep.
**Ted Young** 54:06 So I think that this is going to be really helpful there, too.
But for, like, end users and getting them excited about OpenTelemetry, most people use a Mac as their… their, like, personal workstation. And I've been trying to figure out, like, what is the Mac… if the new getting open source, getting started with OTEL is, like, 3 buttons, Linux, Mac, Windows, right? And you click one of those, and somehow you then get started.
We've figured out the Linux one, but I've been a little bit like, what's the Mac one?
There's, like, getting things working with Docker for Mac seems like a big, important thing.
But people also develop… just… running Python on their local, and, like, what does it mean to install OpenTelemetry on Mac?
**atoulme** 54:56 Homebrew? The solution?
I think?
And it's actually a solution that would work for Linux 2, which is kind of neat.
Adding a tab for Homebrew is not that hard.
**Ted Young** 55:10 Hmm.
**atoulme** 55:11 So, we could do that, I would ask if people want to help on this.
And we could start with Collector and just simple things like, yeah, Python, Java, and…
**Ted Young** 55:22 Yeah.
**atoulme** 55:23 The problem is the, LD preload, hook that we have in the injector does not work on Mac, right, of course. Actually, I have an open issue on the injector SIG, to support Macs, and Bestie pushed, pushed back on me and said, yeah, I don't think this is in scope. I'm like, well…
**Ted Young** 55:39 Right. But I also, just to clarify, I think the difference between Linux versus Windows and Mac is we should be assuming with Certainly with Mac, it's a development environment, right? Which means the things that… what they want is gonna be different. You don't want the default is, like, instrument fucking everything on my Mac, right? Like, that's not what anyone is asking for when they say, install OTEL on my Mac.
Great.
They're saying, like, I want this ready to go because I'm going to be developing locally, or running something here, and somehow I want open telemetry.
To work on that stuff.
**atoulme** 56:16 I've seen a very IT-centric infrastructure monitoring use case for Macs.
where even at my job, right, we have people who reached out and say, hey, we have 3,000 developers using Macs, we'd love to see what's working, what's not working, and we just want to see, like, memory pressure over time, these type of things, and that being reported for IT to make better sense of how to manage their fleets of developer laptops. So, interestingly, there is some use cases for IAM, specifically for Macs, and you can see that in the work that I've done recently, we've added memory pressure management inside the host metrics receiver.
So there is maybe a feature, just to set it, so you know that maybe a collector would be a great little agent on the Mac, for that reason. But yeah, most of the time, you would actually want to be actually running the Mac inside your account, and be… sorry, the collector in the SDKs would be inside your account, and you as a developer, you might even have… like, talking to people who are practitioners, like Jason Plum, he actually runs low UI, right? So he's going to run the, maybe, the Jaeger UI, he's going to run Grafana, he's going to run the Tinyoli thing that came up.
And those things have been more useful on Macs, because you're like, okay, I'm just developing some stuff in Java, I'd like to see what my trace looks like, how do I do that?
So we don't have a dev SDK for people who want to play on Mac, that's true.
**Ted Young** 57:40 Yeah, it's… we don't need to solve it as… I think the main thing is, like, let's get this out to production, but in terms of, like, open telemetry attracting more end users, I feel like figuring out that Mac experience is the kind of thing… End users would, like, have an opinion about, but also feel like they could have some agency. You don't… you don't have to be some kind of crazy observability expert in order to… to help out.
curating, like, what… what a Mac experience would feel like, so…
**atoulme** 58:12 No, we could do here to… we could do, like, what people have done with RVMSH and all the things that they had done for Ruby or Node.js thing, where you just have a script in Homebrew that manipulates your DHH profile file.
and set the environment variables so that you can then load up the Java SDK when you start up.
Oh, it's a bit of a nightmare for people, but… yeah.
**Ted Young** 58:41 I mean, it's also just having a default of, like.
it works similar to Linux, but it's just scoped to, like.
You know, only target things in slash workspace, or, you know.
Some default work location, you know.
But maybe more important is a slick experience with, you know, Docker for Mac.
**atoulme** 59:05 Yeah, that's difficult.
**Ted Young** 59:07 hey, I'm doing all my Linux-y stuff, but I'm on a Mac, which means I'm doing it through Docker, so, like, how does… How does that experience work?
Anyways…
**atoulme** 59:18 Mr.
Okay, maybe some examples to start with.
Well, thank you, everybody. We're out of time. Good luck with your travels.
And let us know how that goes on the unplug side.
Have fun.
**Ted Young** 59:32 Yep.
Cool.
**Jack Berg** 59:34 See you later.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 59:34 Bye.
**Ted Young** 59:35 Yeah.
**Jack Berg** 59:35 But…
