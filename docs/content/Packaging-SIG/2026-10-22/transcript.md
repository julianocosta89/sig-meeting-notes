SIG: Packaging SIG
Date: 2026-10-22
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Jack Berg (Raintank, Inc. – Grafana Labs)** 00:38 What's up, Dennis?
**Denys Sedchenko** 01:06 Hi, Jack, how are you?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 01:09 I'm good, how are you?
**Denys Sedchenko** 01:11 Fine as well.
Nice headphones.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 01:15 Thanks.
Do you recognize them?
**Denys Sedchenko** 01:18 Yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 01:25 So I've never been to this meeting. Is, Who are the typical attendees? Antoine… You, Michele…
**Denys Sedchenko** 01:36 And that…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 01:37 Ted, Ted comes.
**Denys Sedchenko** 01:39 No, today, no.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 01:41 Okay.
Well, if it's just you and me, we will… We will be lacking consensus to talk about anything in a meaningful way.
**Denys Sedchenko** 02:07 That's true, we need at least a third person.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 02:10 Yeah, especially considering I'm not… I'm not one of the usual people in this SIG.
We'll give it to the 5 aftermark, and if nobody else shows up, we can just talk asynchronously.
**Denys Sedchenko** 02:32 Yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 02:38 What does COPR mean?
**Denys Sedchenko** 02:41 Okay, so… I've been working on, like, investigating the packaging infrastructure options. Basically, when you need to build a package.
You need to sign those packages. We don't want to manage our… PGP or GPG keys.
And… We've been looking for existing solutions.
And, there is, like, one service that Kubernetes is using, which is, OpenSUS OBS.
which supports, like, all the distros, everything. It can build packages, generate repositories, sign it.
But I stumbled upon a very simple issue, I couldn't register it. Like, I registered it, but I had to wait, like, for a couple of days to actually receive a mail.
So, by the time it actually came, I switched to a different solution, basically use, like, every re… every distro provides, Service to build a pack and publish packages for themselves, like, ubuntu has their own PPAs.
And Fedora has a copper.
which is COPR.
And Ubuntu was working, like, we had the folks from Ubuntu that had been working, on their side.
And I was working on the Fedora site to actually get copper packages for all our PM repositories.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 04:13 So would, OpenSeus, would that, Would that option allow you to not have to… you know, go to the… I don't know what you call these things, the builder, the build services for.
**Denys Sedchenko** 04:25 all the different distributions.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 04:25 It would just be one.
**Denys Sedchenko** 04:26 Yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 04:27 money?
**Denys Sedchenko** 04:28 Yeah, yeah. Actually, considering returning back to OpenCust solution, because… ubuntu's build service, it builds only for Ubuntu.
And… actually, like, supporting Debian is critical.
like, either I repurpose Ubuntu builds for Debian.
Because, as far as I understand, we don't have, like, any dynamic dependencies.
Or, like, use OBS in the future.
this is, like, the part that is done. Now, we want to publish those packages under our own domain, like packages.opentelemetry.io.
And to do that, I need a storage S3 or a 3-compatible one.
And I need some kind of, like, a load balancer, something that will serve a correct SSL certificate.
And those are, like, two pieces that actually I got blocked at the moment.
But at least you can install… the packages from the copper repo.
At least we ship packages for RPM right now.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 05:44 That's cool.
So, a COPR, that's associated with Fedora, so that would just be, like, is… so then, can you automatically, if you're using a Fedora distribution, then, just, like, run something like RPM install open telemetry?
**Denys Sedchenko** 06:03 Yeah, yeah, basically, you need to use… Copper subcom… subcommand, one moment, let me… Find one thing… Yeah, you're basically… just go… like, here is the link to the package, you just enable our repository with one command, and then you can basically type DNF install OpenTelemetry, and you have injector and instrumentation for different languages.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 06:33 Nice, cool.
**Antoine Toulme (Splunk Inc.)** 06:40 Very nice. Thanks, Denise. So… Okay.
And I'm not sure if we got Cloudflare enabled yet, I need to log in.
They're doing it today, right?
Let me try…
**Denys Sedchenko** 06:57 I hope so. I hope so.
**Antoine Toulme (Splunk Inc.)** 07:03 So with that, we just need to get, like, Notify… Like, if I… thing going.
**Denys Sedchenko** 07:13 Yeah, and the SSL issue. Like, the SSL certificates has a list of… issuers that can issue SSL certificates, and in that list, only Netlify and Google.
**Antoine Toulme (Splunk Inc.)** 07:28 too.
**Denys Sedchenko** 07:28 And a third option.
**Antoine Toulme (Splunk Inc.)** 07:31 I don't love it, but there's a discussion on the community on this, and I offered to have us be temporary admin on Netlify.
And the answer was… Oh, but could you just tell us what you want, or we'll do it for you?
**Denys Sedchenko** 07:49 Okay, okay.
**Antoine Toulme (Splunk Inc.)** 07:51 Or, come on the call with us, and we'll do it together.
And, I didn't have time to… I didn't have time to go into it.
So, a week ago, Severin said it would probably be easier if you give me instructions what I can do to fix it.
I would jump on a quick call and do it together. I have no idea about the UI of Netlify. I, I don't know, stumbling through a web UI for DNS management is usually very difficult to describe, but very easy to do.
Right?
Because there is so many ways to enter records in DNS anyway, and I think we should want to test them in… with severing, if we do it together.
Denise is based out of Europe.
**Denys Sedchenko** 08:40 I'm in, in, in, United States.
**Antoine Toulme (Splunk Inc.)** 08:44 Oh, you are. Okay, seventh bit of Germany, so it doesn't help. So… We need to find a slot with Severrain to do this. My mornings are a nightmare.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 09:02 Aren't you West Coast?
**Antoine Toulme (Splunk Inc.)** 09:04 Me? Yes.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 09:06 Yeah, so… Yes.
**Antoine Toulme (Splunk Inc.)** 09:10 Because you're gonna…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 09:10 get any worse. You and Severin's alignment is the critical path.
**Antoine Toulme (Splunk Inc.)** 09:15 The overlap is, like, half an hour in the morning.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 09:18 Yeah.
**Denys Sedchenko** 09:19 To be honest, to get this shit done, I'm ready to wake up at 6 or 8 in the morning, to be honest.
**Antoine Toulme (Splunk Inc.)** 09:25 I agree, I… I see it, I just… I had to do that several times this week for customer meetings, so I'm not… you know, I do this for money. Okay.
Yeah, I agree. So, maybe we can find time, Mr. Van, We'll just do the old route on Slack, if that's okay, Denis. Maybe we can just start a meeting, a Slack chat between you, me, Severin, and Michelec?
**Denys Sedchenko** 09:54 Yeah, yeah, yeah, it's super good.
**Antoine Toulme (Splunk Inc.)** 09:56 So we'll just take it to Slack and then figure out a time.
**Denys Sedchenko** 09:59 Yeah, the problem, I don't know… what Cloudflare actually would want. For example, I know… how the approach would work, like, with GCP or AWS.
**Antoine Toulme (Splunk Inc.)** 10:11 God.
**Denys Sedchenko** 10:12 But I never connected a third-party domain or, like, something to a third-party bucket on a Cloudflare.
**Antoine Toulme (Splunk Inc.)** 10:19 So, without…
**Denys Sedchenko** 10:21 Yeah, without having a bucket working, I cannot say what actually I need, in addition to CAA record.
**Antoine Toulme (Splunk Inc.)** 10:31 Yep, exactly. So, that's why I wanted to wait for Cloudflare to be kind of figured out, so the fact that Austin is telling us that things are moving… Maybe we can… we can start to think about taking time with Severin to to go over the UI.
So, I'm just gonna… Start a little discussion on Slack right now.
what I mean there, 95 access… Is it Netlify? It's one more L.
**Denys Sedchenko** 11:08 L1L.
**Antoine Toulme (Splunk Inc.)** 11:10 Wow, okay.
Changes… Okay.
Okay, anything else that we should be doing? So, it looks like Jackie got some… He'd like, to discuss something with us about 10 minutes.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 11:40 Yeah, yeah, yeah. I'm gonna screen share if we're ready to move on.
**Antoine Toulme (Splunk Inc.)** 11:44 I think I can take this offline, yes.
Thank you.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 11:51 Alright, so, so I opened a PR against the packages repo, I'm dipping my toes, and what this PR does is it sets up the initial tooling for the packages repo to publish, images corresponding to the packages.
And the use case for this, Antoine's aware of this, Dennis, you might be able to intuit what this is for, but maybe not. So basically, the operator today it publishes its own images that it uses for auto-instrumentation, and so you go… if you go here, there's, like, images for Java, Node.NET, Python, etc, and Basically, they're in the business of curating packages in the form of images that encapsulate the various auto instrumentations that OpenTelemetry has, and they don't want to be in the business of this. They want to be in the business of, like.
you know, building and publishing an operator and, you know, just having an external dependency on the images which actually encapsulate those instrumentations. And so this is a natural fit for the packaging repository, is to extend the packages and just, you know, publish them in a new format.
And so, I want to talk synchronously about some of the features of how I've implemented this, and get some feedback on them. So, one, there's this config.json file, which determines which packages we are going to publish images for, and which architectures we're going to… we're going to publish multi-architecture images, and so which architectures we want to publish for.
And, Besides this, there's only one Dockerfile in here, and so the idea is that we… we're not going to have a Dockerfile per image. We are going to have… we're going to, like, have symmetry, and we're, like, you know, basically we're gonna have it be parameterized, where the parameter that changes is the package that we're bundling up, and maybe, like, the version and a couple of other parameters like that.
But, they all use the same underlying image definition. The same base image, the same… extraction process, etc. And so, yeah, it's… there's a config file and a single Docker image, and the rest of the Go files in here is tooling that, like, that facilitates this. There are make commands that say, if I go here.
there's, like, new make commands, and these basically call the various Go scripts, but, like, you can, say, make all your images, or make a specific, components image, or make a specific components image with a specific architecture. So, you know, basically these just, you know, decide which of the, Which of the entries in the matrix that are dictated by this config file you want to go and create an image for?
And the idea here is to be super unopinionated with how we take a package and bundle it up into an image. We just want to basically copy the resources into that image and nothing else.
And we also want to be unopinionated with the versioning scheme as well. So, we want to publish, you know, there's an injector package, a Java package, you know, we want to publish images that correspond one-to-one with the versioning scheme of the injector of Java and of all the other packages.
Such that when the Java agent publishes a new version, there's a new package that corresponds to that, and there's a new image that corresponds to that. And same with Injector, and same with all the other, you know, instrumentations that we'll add later. For now, I just, by the way, for now, I just did the injector in Java to prove out the concept, and, like, I'll expand this set later.
Okay. But… There's some automation in here that aims to… this is this images.yaml, this is a, you know, GitHub Actions workflow, and what this aims to do is, on any merge to main, it tries to detect whether a change happened that constitutes republishing of an image.
**Antoine Toulme (Splunk Inc.)** 16:12 Let's see.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 16:14 And so basically, the workflow is roughly, like, to, you know, suppose Java, publishes a new version of the Java agent. So, Renovate picks up on that, and Renovate opens a PR to the packaging repo that bumps the tag of the Java package.
And once that renovate PR is merged, then this, you know, this workflow will kick off on main, detect that there was a change in the Java package, and publish a new image corresponding to that.
**Antoine Toulme (Splunk Inc.)** 16:48 Nope.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 16:49 So I'm trying to think if there's anything else that's noteworthy about this. You know, I guess just in terms of scope, we're just publishing to GHCR for now. I didn't muck around with Docker Hub yet, that would be a follow-up step.
But this is just to sort of, like, prove out the process.
**Antoine Toulme (Splunk Inc.)** 17:10 Okay. Yeah.
Yeah, this is… this is fine as a first step. And then, I'm guessing… so you say you have one Dockerfile right now, we don't have… The two… the two flavors and the two architectures you want to support would be, Ubuntu-type… These are busy box-type things, so… You don't have a… You don't have a window strategy yet, right?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 17:38 Yeah, but, you know, we could… we could expand to that whenever. We could actually even start simpler if we just want to just start with, like, a single, architecture, right? And, you know, basically, as we… as we expand the packages, and we expand the architectures we want to support, the matrix just gets bigger, and we're publishing more versions of these things.
**Antoine Toulme (Splunk Inc.)** 17:57 Gotcha.
Denise.
**Denys Sedchenko** 18:00 Yeah, I have two questions. One question is, like, right now, basically everything using the same Docker file, but what if we have an edge case where, like.
For one particular… One particular image, you need to make some kind of extra customizations, like add a custom one or two layers.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 18:23 Yeah, exactly. That's a great question, and the way that I… so that's actually… that's a realistic thing, right? Because the way that packages organizes resources is not exactly the way that the operator organizes resources.
**Antoine Toulme (Splunk Inc.)** 18:39 Nope.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 18:39 Right? So, the way that I figured we would handle that is we would encode those customizations as, like, structured data in this JSON.
So if you want to map, and create, like, either, like, a sim link or a copy of any of the resources from the packages for the Java, you know, package, then, you know, you encode that in some sort of schema here.
**Denys Sedchenko** 19:01 Let's assume… I will take a complex example, let's take what BI, for example.
Obi, in order to properly function in a rootless environment, you need to stamp the binary with some, with some Linux capabilities.
for that, you need to run a command. Like, basically, are you going to, like, extend this schema and generate a Docker file from a template, because such things probably is not going to fit into Docker build arcs.
Or you allow us to basically overwrite the Docker file.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 19:36 That's a good question. We could do that, right? We could have this entire Docker file, you know, programmatically generated, and, you know, basically live as a templatizable thing. And, you know, the Go files first construct the Docker file.
And I think there's trade-offs, but, like, in my initial version of this, I had a Dockerfile per package, and it just felt too fragile, too inconsistent. Like, too much copy and paste that needs to be, like, manually maintained, and having a template, whether it's, like, you know, a hard-coded Dockerfile, or just, like, something like the precursor to a Dockerfile, a template that eventually becomes a Dockerfile, I think it just promotes More uniformity as a pattern, and it forces you to, like, you know, modify the structure of templatizing rather than, you know, trying to cheat and, you know, create little, like, exceptions for… on a per-package basis. So, yeah, I… I think we… we kind of, can… Take this config, and we can make it more elaborate and iterate as we go and we encounter more cases.
**Denys Sedchenko** 20:42 One final question. In architectures, assuming the architectures, I assume you're going to… you're going to have two separate parallel jobs running on a different GitHub runners, right?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 20:55 Let me see how that ends up.
**Denys Sedchenko** 20:57 Architectures, Jason, yeah, like, I see Runner Ubuntu and Ubuntu Arm.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 21:02 Yeah, I think the entire, images.yaml becomes, like, templatized by this, so that, you know, if we detect that Java has an update that requires a new build, well, we determine that we need a Java runner for Ubuntu ARM and Ubuntu AMD64, and this images.yaml, I think, spins off.
**Denys Sedchenko** 21:25 I.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 21:26 up.
**Denys Sedchenko** 21:26 I have a small concern regarding that.
As far as I know, like, in my experience at least.
it's quite hard to build the same image with the same tag on two different machines. For example, to basically split the physical machines. One machine builds ARM64 version of the same image, and another one is x86.
Usually, you have to do that in one docker buildX command, and you need to use QAMU under the hood.
Just to basically make one image for multiple.
architectures. It has to be done.
In one built transaction, let's say so.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 22:09 Well, that would certainly simplify things, so if we can accept QEMU, then I can definitely, like, adjust this to reflect that. Yeah, because it actually makes it easier.
**Denys Sedchenko** 22:20 I'm not just not sure that your approach is actually working. Like, this is what I had from my experience. You might actually need just to use QMU, and then use Docker BuildX under the hood, and it will basically… There is even an action on a GitHub that allows you to build for multiple architectures.
I have an example… I'll share it to you, just give me a second…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 22:47 Yeah, can you post it on the PR so I can… I.
**Denys Sedchenko** 22:50 Yeah, one moment.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 22:51 and have a perception.
**Denys Sedchenko** 22:52 I will DM you in Slack, okay?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 22:54 Okay, yeah.
**Antoine Toulme (Splunk Inc.)** 23:00 I mean, it's, you know, better than before, is, I think, my stance on things.
I think we can… review and discuss how we want to build this, and the way it's going to grow from there is an interesting discussion, I'm sure.
You won that by CubeCon, right?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 23:22 I don't… I don't have any rush for this. So, what this… what this facilitates is, like, there's an issue over in the injector.
Where… well, the injector wants its own images, so this would solve that, but then there's another… Yeah, over in the packaging SIG, the… Who was it?
**Antoine Toulme (Splunk Inc.)** 23:45 A little sweaty… yeah, so is the operator people.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 23:48 Yeah, the operator people don't, like, they want to start adding support for PHP, but they don't want to, like, you know, add a new PHP image for whatever reason, so I guess they're sort of treating this as a forcing function for packaging to start publishing container images, so…
**Antoine Toulme (Splunk Inc.)** 24:03 You know, that makes sense. And so… Yeah, so you want to start with Java, because that's the one that you're used to, the most mature, PHP would be maybe a close contender for second place.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 24:17 Well, it's really easy to extend it, right? So, like, once… I just want to make sure that the, like, the machinery works, and once the machinery works, then, you know, it's really easy just to open PRs, to just add new packages to this. And, you know, you can do those in quick succession.
**Antoine Toulme (Splunk Inc.)** 24:33 Yeah, okay, no problem.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 24:35 I don't necessarily want to keep it restricted to PHP and Java in the short term. I would like… the thing that I would advocate for after this is, like, expanding to all the packages we support and that are needed by the operator, and then, you know, trying to add shim layers so that the operator can reasonably get rid of its Docker files without, like, you know, breaking changes.
**Antoine Toulme (Splunk Inc.)** 24:58 It all makes sense. So… okay, alright.
I mean, there might be some stuff that could be done better, you know, but I don't see anything egregious. We… I can do a… I can do a review.
Let's get this merch, you know, with some… we can, you know, test it out and all that, even if it doesn't work the first time, it's okay, like, there's a lot of ins and outs of a release, so we can be, we can do a draft release or play with it as much as you like, Jack, right?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 25:34 Yeah, yeah, and I think this sets up a release cadence that's independent of the packages' releases themselves, right? Because it tries to publish images that are versioned in lockstep with the upstream components, right? So, one for one with each injector release, one for one with each Java release, etc.
**Antoine Toulme (Splunk Inc.)** 25:54 That's a valid point. So we need to think about this maybe a bit more, because the way Michele was thinking about packages was that the versioning of a package, it's really difficult, for example, to have any somewhere on a packaging repository, which itself is just repackaging other things.
Here, just a combination of all the versions of all the things you package.
if you look, we… we tried to really not do very much with our versioning so far. We have 3 tags, and they're just mostly for play.
We don't make them match a particular version of what's underlying.
And I think what we could do is just have, like, a fixed release schedule for the rest of the artifacts. I don't know, actually.
So… work with me here. Like, if you have a new Java Agent release, right, the day after the Java Agent release is made, you would love to be able to go to an RPM site and download your Java agent. It should be there. And the same goes for your Docker image and everything else.
So it's almost like the package repository in its entirety should be completely reactive to renovate changes.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 26:55 I think so. Like, that's how I thought about images, and I think it makes sense to do the same for the packages.
**Antoine Toulme (Splunk Inc.)** 27:01 Right here.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 27:02 The problem with that, though, is that you have this Uber package, which is a composite of all the other, like, packages as well, and, like.
**Antoine Toulme (Splunk Inc.)** 27:10 That one.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 27:10 That one, it's almost like it needs to be, like, not semantic versioned or something, like, it needs to be datetime versioned, or something like that.
**Antoine Toulme (Splunk Inc.)** 27:19 Yeah, we talked about that. Yeah, we should do that.
We, we were…
**Michele Mancioppi** 27:25 It'll be day timed.
**Antoine Toulme (Splunk Inc.)** 27:28 MK, what's up?
**Michele Mancioppi** 27:30 I finally managed to log in, bloody hell. Which package should be day-timed?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 27:36 We're just… we're talking about how, like, this new PR I opened to start publishing images corresponding to the packages, and the images are versioned in lockstep with the components that they encapsulate. So, you know, if the injector makes a release, there's a new image corresponding to that. If the Java agent makes a release, there's a new image corresponding to that. And the question is, like, should the underlying packages.
like, that are published to RPM, should those share that type of versioning scheme, where they're, like, one-for-one with the contents that they encapsulate?
**Michele Mancioppi** 28:11 It is not exactly one for one, so the following, the, upstream, injectable implementation, to use the language from the other people.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 28:21 Yep.
**Michele Mancioppi** 28:22 Correct, but there is additional logic in the packages where we need to have the possibility for a suffix.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 28:29 Yeah, right, you need, like, a fourth number there to indicate, you know, like, your own versioning scheme.
Totally agree. So, like, and we have that similar problem in places like semantic conventions Java, where we bundle up generated code from the semantic conventions, but we, like, have our own logic in there, so we, you know, we have our own version on top of that. So that's its own challenge, but, like, the thing that we were talking about, just to come back to your question about which packet should be a datetime version, that would potentially be… when we were just musing, but it was, like.
the Uber package that encapsulates all the other ones, right? So, if all the other sub-packages are versioned roughly in lockstep with the contents they encapsulate, then you kind of want the Uber package to be I don't know, something else that is just, like, not Sempher.
**Michele Mancioppi** 29:17 there is no Uber package, so the…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 29:19 There isn't.
**Michele Mancioppi** 29:19 The meta package is effectively a list of references, and that can have its own semantic versioning, and then it just pulls through the interface versioning, it pulls the other ones.
So the OpenTelemetry package is the one that needs the least versioning, because probably we issue maybe two versions of that.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 29:43 So, like, what happens then if, like, for the OpenTelemetry package, because it's just a list of references, but, like, what happens if the reference versions change?
**Michele Mancioppi** 29:53 Like…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 29:53 So the injector changes and the Java agent changes. Does it not.
**Michele Mancioppi** 29:56 I need to publish in.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 29:57 version?
**Michele Mancioppi** 29:58 What would change is not a reference of a specific version. The thing that would change is the interface.
So, the interfaces are not Open Territory Java, it's Open Territory Java 1.
So that you can have any number of packages implementing that packaging interface, and then if something fundamental changes in the contract, they have another series of packages that implement Java 2.
The, the Uber thing is actually, effectively, just a pointer to interfaces that you need to satisfy.
And that would change, that package would change, effectively only when we want to change its metadata. Like, it's no longer the OpenTelemetry alters, it becomes the regions of California, huh?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 30:47 Sure, sure. So yeah, so maybe… so probably no daytime version is required. It's just, like, a SEMVR version, which, you know, is published very infrequently.
**Michele Mancioppi** 30:57 Yeah.
**Antoine Toulme (Splunk Inc.)** 30:58 We're good then. Okay.
Well, okay, so, in case there's a PR from Jack that we need to review. It's, adding all the containers that we know and love from Spontaneous SDKs.
We should do that.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 31:16 Yeah, no pressure on the time, like, I'm not waiting on this or anything, but, like, you know, I'll be responsive and, you know, as soon as I.
**Antoine Toulme (Splunk Inc.)** 31:25 It's… we should… we should try to move it as fast as we can so that we can get something to talk about at KubeCon with the operator people.
Nothing.
**Michele Mancioppi** 31:33 I agree. So, I have it on, I have it on my to-do list, but I'm also off next week, so if somebody else wants to have a first look, then that's perfectly fine, and then I'll definitely have a look at it as soon as I can.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 31:51 Alright, we better hop over to the, the injector segment.
**Antoine Toulme (Splunk Inc.)** 31:53 Yep.
Thank you.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 31:55 See ya.
**Denys Sedchenko** 31:57 Ian?
**Michele Mancioppi** 31:59 Bye.
