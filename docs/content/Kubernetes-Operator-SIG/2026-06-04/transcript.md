SIG: Kubernetes Operator SIG
Date: 2026-06-04
Duration: 64 minutes
============================================================

## Zoom Recording Transcript

Benedikt Bongartz 00:01:57 Blue?
Mikołaj Świątek 00:01:59 So, how is… how's… how's it going?
Benedikt Bongartz 00:02:05 So far, so good. How about you?
Mikołaj Świątek 00:02:08 Yeah, I'm feeling good as well.
Hmm. Is, is… is the baby still being a nuisance, or are you kind of sleeping normally?
Benedikt Bongartz 00:02:20 Yeah, that's usually… Fine. But what sucks is a bit it's sick quite often, so it's… yeah.
Pavol Loffay 00:02:31 Hey everyone.
Benedikt Bongartz 00:02:33 Hello?
Mikołaj Świątek 00:02:34 Clear that.
Is Jacob gonna… did Jacob say anything? He didn't say anything.
Benedikt Bongartz 00:02:42 still suffering from last KubeCon. She saw someone from Elastic, and since then she's shocked.
Mikołaj Świątek 00:02:51 Who was this? Who was this person who had such a profound effect on your daughter?
Benedikt Bongartz 00:02:57 I don't remember, she always stutters, and then she says, like, this guy is filling the agenda of all sick calls, and yeah.
Mikołaj Świątek 00:03:05 Wow.
Nasty. Sounds like a real nasty person.
Alright, let's get started. Jacob can join when I can join. I have… I added some topics… I think most of them are kind of trivial, and then we can… we can talk about the… the, Pavel's RFC, which I bet he wants to talk about.
So… Gonna share my screen… Hopefully this will work fine.
Do you see this?
Pavol Loffay 00:03:41 Yep.
Mikołaj Świątek 00:03:43 Alright.
So, the first thing is, I'm gonna try using CodeCoff.
To begin with, for tracking end-to-end tests, I am really annoyed to keep getting… keep being really annoyed by our end-to-end tests and how annoying it is to figure out what actually failed, and we used to have, like, a setup with this little GitHub action, but… this has problems. The problems have to do with the fact that if you submit a pull request from a fork, it runs in a different security context in GitHub Actions, and you're not allowed to comment on the PR directly, because your token doesn't have the permissions, but if you do it the other way, where it goes, like, a workflow dispatch, then… there's other problems, GitHub's API isn't perfect for this, and, like, the right way to do this is to just have an app.
And a lot of OpenTelemetry projects just use CodeCov, they use it for coverage, which we might eventually do as well, but it also kind of does what we would want for end-to-end tests. And this is in my fork.
I intentionally broke a test there, and I have this… comment here.
And if I start clicking, I'm gonna see that it's this test. I don't know why Chainsaw puts these two columns in here, but it doesn't really matter.
And I can even click here, and it gives the little stack trace thing, which says what actually broke. That's quite nice. I can also go to the… there's a dashboard, like, for example, this is… this, for example, a contributor can also click, because this… by the… you can upload these CodeCov reports without any kind of token, and it just kind of works as… by default for API… for, sorry, for open source projects this way, so this actually doesn't really even need any login or anything, you can just click and you'll see it for your own pull request, which is this… Ranch for me, showing how long the tests took, and so on.
But… I can switch to all branches, and it gives, like, a local dashboard about, like, what is most flaky, and so on.
So it's pretty nice, and it's pretty easy for us to use it, because, again, hotel already uses CodeGov, so we can just go to admin and ask them to give us a token, and that's it.
Benedikt Bongartz 00:06:15 This looks awesome.
Mikołaj Świątek 00:06:18 And the implementation is, like, shh, whatever.
not very… it looks really similar to what we have right now. It's like, hey, we look at the comets ahead here, and it's kind of, like, just… Deleted something, added a token to two places, and there's, like, an additional step here that… makes sure that we upload everything at the same time and not piecemeal, essentially.
Huh. So… Chat, anyone against?
jea 00:06:52 Sorry, I'm like this.
Mikołaj Świątek 00:06:55 Not a problem. I was just showing off the… I want to use CodeConv for tracking the end-to-end test errors.
jea 00:07:02 Boom, yeah, I like it.
Mikołaj Świątek 00:07:05 You haven't even looked, Jacob.
jea 00:07:07 I'm looking at an… no, I know what CodeCov is.
Mikołaj Świątek 00:07:09 Yeah, but I… did you know that it can… it can be used for this? I don't know.
jea 00:07:14 I didn't know it could be used for that, I just am a fan of CodeGov, generally.
Mikołaj Świątek 00:07:18 Yeah, and Auto already uses it, like, the collector repositories use it, so we can use it as well, and look, it does kind of what we want, like, this is a failed test, and it even gives this little trace here.
In a comment.
So, we good? Can we do this? Can we do this?
Benedikt Bongartz 00:07:46 Yes.
Mikołaj Świątek 00:07:51 Oh, bye.
It has to be thumbs up, and not… okay.
Alright, second thing.
there's this pull request. This pull request wants to fix a bug. The bug is that if we add… if you set that we should add Prometheus annotations.
We add them, but then if you disable that option, we don't remove them, because we never remove annotations that we don't recognize, essentially.
And you can't ca- you kind of can't naively just remove them, because these are, like, Prometheus annotations.
Or the scraping stuff?
So… If somebody could conceivably add them on their own, and then we'll remove them.
In that case. Incorrectly.
And something… I was thinking about whether we can solve this problem somehow. It, in principle, it could be solved by adding more context to, like, the mutator functions, but… I hate that.
I hate, injecting… you remember this code, Jacob, right? This is the manifest mutation stuff, and… I would hate to add more context in here, because in principle we could, if we could compare the two CRs and check whether something flipped one way or the other, but that's, like, really against the spirit of reconciliation, I feel like.
So, something I thought of was just… whenever we add this, add another annotation, which we own, which is… goes something like, Prometheus annotations added, or something, OpenTelemetry I.O. slash something slash… Prometheus annotations added, and then we know.
And if that annotation is there, then we know that we can remove the existing stuff, and if it's not there, then we leave things alone.
That's, like, the best thing I came up with to solve this problem. We could also say that we're not gonna solve this problem, and it's just like… A defect that we accept.
As the cost of… Or other logic, essentially.
Opinions? Does anybody have one? Or should I just decide on my own? I can do that.
jea 00:10:26 Take it.
Mikołaj Świątek 00:10:30 Because I don't want to keep this contributor waiting for us. I want to give them some kind of guidance on what they should be doing.
That's like the… honestly, that's the primary reason. I don't particularly care about this specific bug, it's kind of like a stupid edge case of stuff that I would… but if people… if somebody is annoyed and wants to fix it, I want to stop stringing.
jea 00:10:53 I think this is… I think this is fine. I understand why this is annoying. I don't think that there's a great… Clean way to do this, other than what they're doing already.
So… I think I'm okay with it. It's a bit gross, but, like, I don't know.
Mikołaj Świątek 00:11:12 What is a bit gross, exactly?
jea 00:11:15 Needing to, I don't know, needing to look at more annotations is not ideal.
Needing to modify annotations can also be fraught.
As we know from past annotation modifications.
Mikołaj Świątek 00:11:30 Honestly, I think this is… kind of how we should be handling it in general, like, we should just have some annotation that we own explicitly.
That we don't expect anyone to add manually.
On our own, and that annotation indicates whether we should be doing something or not.
jea 00:11:50 Deal.
Mikołaj Świątek 00:11:53 Bye, pavo.
Pavol Loffay 00:12:02 I'm fine with… the proofs.
Mikołaj Świątek 00:12:21 Publishing the API package. For some reason, we thought we didn't have to do this, but apparently we do.
Does anyone recall why we thought we didn't have to do this?
jea 00:12:31 I thought we did this recently. I thought that the PR that we ju- the PRs that we just merged should do this automatically.
Mikołaj Świątek 00:12:37 It turns out it doesn't. Like, or rather, you have to… Apparently…
jea 00:12:43 I think that this is because we have not published a release yet with the new API.
Mikołaj Świątek 00:12:48 Have.
jea 00:12:49 Have we?
I don't think since we merged that we have.
Mikołaj Świątek 00:12:54 That was less…
jea 00:12:55 We merged the APIs, like, recently. Go to APIs.
When did we add the GoMod? Two days ago.
Mikołaj Świątek 00:13:06 No, this has, been updating to 126.
On May 29th?
I could swear we did this before.
Let me check the tag.
Benedikt Bongartz 00:13:23 What did we?
Just here, Lenny.
Mikołaj Świątek 00:13:27 It's not here.
No, no, I was… I was… I was, just referring to a change you made.
So maybe you're right.
In order to be able to use a human-readable somewhere version for this module and other projects.
a API-sized version tag should exist. I… I am… not… 100% sure this is actually necessary?
I thought we already published this, but… Does anyone…
Benedikt Bongartz 00:14:12 During this change when… things got moved into the APIs version?
Mikołaj Świątek 00:14:22 Network.
Benedikt Bongartz 00:14:22 It was a perfect atmosphere.
Mikołaj Świątek 00:14:25 Yeah.
Benedikt Bongartz 00:14:27 I think there was a pull request where we moved from internal to… APIs?
Mikołaj Świątek 00:14:34 No, no, what happened is that… This is now its own module.
And the question is, if it's its own module, do we need to, when we publish a new release.
Do we need to add tags with, like, the paths?
I don't…
jea 00:14:57 we do.
I think once we do the release with the Go mod, you just have to trigger… When somebody goes to pull the package from package.go.dev.
it will, look at the latest release for the Go mods that we have.
Mikołaj Świątek 00:15:18 Because, for example… If you look at tags in Primepheus Operator, they do have tags for the separate.
They're separate modules.
jea 00:15:30 is… I think it's because they publish… these things separately so that they can patch separately. But I don't think we're gonna necessarily do that.
Benedikt Bongartz 00:15:42 Do they? Because the checksum's always the same?
jea 00:15:48 Yeah, I don't know that it matters. I also don't know how they do the tag per package.
Or why'd they do that.
Mikołaj Świątek 00:15:58 I thought this was nec- I thought this was necessary if you have multiple modules in the same type repository.
Benedikt Bongartz 00:16:05 How is it…
jea 00:16:06 be wrong, I didn't think…
Benedikt Bongartz 00:16:07 connected to it.
Because on the collector, they have tons of models.
And if this would be necessary, we would have at least 100 texts or something.
Mikołaj Świątek 00:16:19 They do.
jea 00:16:22 Do they tag per module? I didn't think… I thought…
Benedikt Bongartz 00:16:25 Go to the collector contract.
Mikołaj Świątek 00:16:27 Welcome, welcome, welcome, here you go.
jea 00:16:30 Oh. How does that happen?
Mikołaj Świątek 00:16:34 Here you go.
Benedikt Bongartz 00:16:36 Do they say the same thing on the collector contract? Because this should be massive.
Mikołaj Świątek 00:16:41 Yeah. Tags aren't very expensive.
There you go, 35,000 tags.
jea 00:16:47 Yeah.
Mikołaj Świątek 00:16:48 They absolutely do this, yeah.
jea 00:16:50 So, okay, then where's the… where in the release does this happen?
Mikołaj Świątek 00:16:56 I'm not, like, when they're… when they're publishing a new release, they also add a bunch of additional tags concurrently. It doesn't really matter, necessarily.
Well, we just introduced…
jea 00:17:08 They're following that, no?
Mikołaj Świątek 00:17:11 I mean, it has to be… in principle, we can do whatever we want, like, it should be the same… combat, right? But that's just kind of just convention.
if we really want to… if they really wanted to, they can publish any version of this on any commit they want, right? Like, I think for… this is for the Go proxy, and for the Go command in general, to be able to know Which, like, to be able to associate I think I know why this might not be the case. It's because… It's because there might be a difference Between the… tough.
Okay, so I recall why we thought we didn't need to do this. It's because I thought this is only necessary If the path inside the repository to your module is different than the import path you want to have for it.
So, for example, if you have this scraper slash zookeeper scraper, right, this is a… this is a module.
And you look at where this actually is, It's in, like, package slash… Where is it?
Is it just in slash scraper?
It is. Who the thought?
Or maybe it's just necessary? I don't know. Anyway, I don't want to spend an excessive amount of time on it. If we have to do it, then we should do it. If we don't have to do it, then we shouldn't.
This doesn't actually say, I don't think.
Anything. Anyway… I… I mostly wanted to bring this up so that we're… so that everyone here is aware that this is something that we might have to do.
My final thing is just this. There's a simple pull request that lets you set the command on the collector CR, And I think this is… Correct.
Putting aside, like, some minor test failures here.
The question's just… do we want to allow this? Because I still vaguely recall there was some reason we didn't want to allow this.
But I can't think of it, and the change is really simple.
jea 00:20:06 I think this was the same security, thing that we were worried about with the args to… Auto-instrumentations.
Mikołaj Świątek 00:20:21 What do you mean?
jea 00:20:23 As in, this is, like, we have to… I don't know if we're doing it in this, but we need to check the… ARGs to prevent that… remember the auto-instrumentation, like, security bug that somebody reported?
That we weren't, what was it?
there was, like, an injection method through the, args to the auto instrumentation, so you know what I'm talking about?
Mikołaj Świątek 00:20:52 Yeah, but this doesn't… this doesn't apply here.
jea 00:20:56 Pacific.
Mikołaj Świątek 00:20:56 No, this doesn't run through a shell.
By default.
jea 00:21:01 But doesn't it run in the, in the collector shell? Like, the actual, like, collector image will run these commands, no?
Mikołaj Świątek 00:21:08 Yeah, but that's just a binary. My point is that you can't just put You know, like, shell commands in here for this to work.
Benedikt Bongartz 00:21:20 Can go and just… use Ubuntu as your container base image.
And then place whatever command you would like to have there.
Mikołaj Świątek 00:21:32 If you can switch the image, then you can just have that.
jea 00:21:35 Yeah, you can do plenty of tanders.
Mikołaj Świątek 00:21:37 The image can just have an hotel script, so it doesn't actually change over much, I feel like.
the NGINX thing that we had had the problem where you could make it run arbitrary shell without changing the image. And that's, like, a significant escalation.
jea 00:22:03 I see. That… I misunderstood what the… what the bug was then.
Mikołaj Świątek 00:22:08 Yeah, I mean, if you… if you… Yes, you know, if you can set the image on this.
then you can run arbitrary code in the container. That is true.
I don't think that is actually a security.
Problem of any kind, in general.
Although, on the other hand, it's unclear whether we actually need this.
Because… it was, like, I think it was actually originally added, so you could use, like, the elastic agent images this way, because they, like, required an additional command.
In there, but that's not the case anymore. So, it's not necessary for the original use case.
So we could also just say no.
But I… but I'm personally okay with it. I don't see any… Problems. Move it.
I think another reason originally we didn't want to do this was just that… Is that we didn't want to open the… We didn't want to open… like, we didn't want to open the… Opened the possibility of… mounting a bunch of config maps into the collector CR, and then, like, passing several… Configuration files.
To the collector, because that kind of breaks a lot of our assumptions about being able to parse the config.
But I don't think this particular… And maybe, maybe you can do it, do it with this?
But there's a good argument that the Helm charts let you do it, and…
jea 00:24:32 Sorry about that. What was the… where are we at?
Mikołaj Świątek 00:24:36 Do we want to do it or not?
jea 00:24:38 I think it's fine. I mean, it makes sense to do this.
Given that… When you change the underlying image, the command changes.
Mikołaj Świątek 00:24:51 You have the opportunity to… like, the contributor has to fix the task, but…
jea 00:24:56 Yeah.
Mikołaj Świątek 00:24:57 We're… so we're accepting it, right?
jea 00:25:00 Yep, yep.
Mikołaj Świątek 00:25:02 Okay.
EcoGates.
Actually, Ozzy, because this stuff should go at the end. Do you wanna go next?
Ozzy 00:25:12 Yeah, okay, can you hear me okay?
Mikołaj Świątek 00:25:16 Yep.
Ozzy 00:25:17 Yeah, I was, investigating about ways that the, the operator could, you know, deploy the, Obi instrumentation. It's quite cool. Now, the only thing is, There are, it can be deployed as a sidecar, but I don't know if this is maybe… Such a good idea, or a place for a lot of users, because it's, it needs a lot of privileges and things.
I mean, that does fit the existing, kind of, instrumentation patterns, but, it can also be applied as a daemon set, and I did make a little, kind of a POC for that. I could also share my screen if you want to see it. I do have it where basically there's two… Yeah, I could do that if it works with Zoom.
Where's the little button?
Somewhere here, there, this green button.
okay.
Can you see that? That's Jaeger, yeah, is it working?
I hope so.
jea 00:26:25 Yep.
Ozzy 00:26:25 Yay.
Yeah. So, what this, deploys is… we have to… just a little silly go up, really, or… let's see, actually, this is the wrong… Is it true?
MPI Gateway.
Yeah, okay. So we just have this one little goat thing that just listens for hello, and it just calls another service, which is nice to illustrate that, or whatever, it'll call this other service that just waits for 200 milliseconds or something.
And then, I suppose the relevant bit, then, is in here.
So we've just got cert manager and the hotel operator.
And… We have a, that's Jaeger, but, we have first the demon set for this.
Now, this is the image that they built, so this is available.
it does require a number of different, privileges. You can either set privilege true, which works, but it's maybe not so nice, or you can specify these specific capabilities that it requires, and it runs as a daemon set, because it actually talks to the kernel and stuff, so you'd only really deploy one.
And, it can be kind of configured, so say I've told it that to look for things annotated with this.
In this namespace… And also the same in this other namespace.
And it can export those to my collector. It also has a service account, because I believe it, it needs to sometimes talk to the API server, so it can kind of enrich the traces and stuff like that.
Yeah, so what's cool, then, is if I run that, basically, neither of those two apps have any kind of, SDK in them or anything, but we get traces from both of them, and they also have… I don't know why it renders kind of weird on my browser for some reason. And they also get both the, all these nice things as well, the data, like, and stuff like that.
Yeah, what I always just wanted to raise for discussion was, I suppose, if… Basically, this… there is the sidecar as one option, and it can also be run as a demon set. I suppose a demon set might mean a new COR or something. And there is one other interesting option, which I think I just would like to bring up, that… Oh, it's documented somewhere else, but basically, there's a receiver as well for it, too. There is now… they have added a collector receiver, so in that case, then, you can deploy a collector, That has this receiver. It needs similar privileges on the daemon set for it to work.
The only thing about that, there isn't currently a kind of a distribution of the collector.
That has it built in. I looked into it, seems like they're working on that, but at the moment, you have to build this collector image yourself. I was just curious about what… What did anyone have any thoughts on how we should, do this?
Because, I mean, the collector one is interesting, I suppose, because you could just have the, the operator, similar to when there's a Prometheus receiver or something, and it, you know, configures the services and different things like that. It could also, configure the elevated privileges and things when this receiver is in the… the OB receiver is in the config, or alternatively, we… there's a new COR and it just deploys the daemon set.
Hmm.
Pavol Loffay 00:29:59 Could you share again the collective config, how it would look like?
Ozzy 00:30:05 Yeah… I just consider it.
So, I don't have that at the moment in my little POC yet. I want to add it, but they have a nice, They also have it documented as well. Somewhere here, let's see… that's not under…
Benedikt Bongartz 00:30:23 Collector just is similar to the OpenTeametry receiver. You just specify an HTTP port, and say, for example, on port 10,000, Traffic goes in, and then you can use the data coming from there.
So it doesn't really look special, so it's really, like, just something that receives data.
Pavol Loffay 00:30:46 And how do you define which kind of… Pots or namespaces.
It should… Receive.
Benedikt Bongartz 00:30:59 That's… so there is the receiver, which is getting the data from this, from this daemon that you deploy there, so you would just send it over. In that case, you wouldn't configure anything in the collector, but you can also emit OTOP.
And then there is also another version where you can specify different pieces, like, I think this one here, where you configure the eBPF stuff.
The reason, I guess, this is not in contrib, but that's just a guess, I don't know.
is potentially because it uses SQL, and it's only available for ARM and… Amd64.
Pavol Loffay 00:31:36 Right, like, a series config, and if I deploy it as a daemon set, how do I say which… namespaces or plots I want to instrument.
Ozzy 00:31:48 like, like this here, for example. So it has… you have lots of ways of doing it. Here I've chosen… that it will find anything in tenant alpha namespace with the… that particular annotation, and the same for beta, but it also supports a lot of other ways of doing it as well, like, by, you know, by process ID, or by the container name, or even by the language. It's quite flexible.
Pavol Loffay 00:32:16 Okay, so, but the discover field is in the receiver as well?
Ozzy 00:32:22 Yeah, so here's the documentation. This is for the receiver, so they're showing you how to actually build it, and… Yes, as far as I'm… basically, you pass the same things true. Here, they're choosing to, to listen for HTTP traffic on that port, but you can… you could do the same Things where you might say a namespace and an annotation.
And, that's work.
Pavol Loffay 00:32:47 delivery fields.
Ozzy 00:32:48 Yeah.
Benedikt Bongartz 00:32:49 in the comments.
Pavol Loffay 00:32:51 I think it was the distribution.
Or whether they want to, kind of, kind of, build it in the releases repo was discussed on the CollectorSik this week.
And… There was some pushback, because… the way, how they built the collector with OB, It's at the moment… Difference to how… the… Collector is built.
Without the obi. I'm not sure if the Obi kind of uses the collector builder, maybe it uses that, but maybe as well requires additional steps. So I think someone is looking into, kind of, simplifying the build process, aligning with the collector builder, and then They will maybe accept it, and we will have the build in the releases repo.
Benedikt Bongartz 00:33:51 I think the main problem is that they use Siegel.
So, which means it doesn't support, then, all the platforms it currently would support, because Go supports more out of the box, and this cross-compiling and all this gives you headaches. Currently, I think the build is also completely static.
And… Yeah, so that's, I think, the main pain point. So you need GCC or Clang or something like this installed to make it work.
jea 00:34:22 Yeah, I think for me, I don't quite understand the… Relationships between that config map that you showed, and the config that you showed on the docs?
And how those two things relate, and then also what the user experience would be for… actually… instrumenting, implementing, and using these things. Even beyond the release process, it's unclear to me The relationship between these documents.
Ozzy 00:34:53 So, let's see… I mean, the config map, basically, here is… you can configure it through environment variables, of course, but you can also pass it a config file, and I just happen to be loading that.
to a.
jea 00:35:10 But, but so…
Ozzy 00:35:10 That's convenient.
jea 00:35:11 That's injected into the application, correct?
Ozzy 00:35:15 This is injected into the, the demon set that runs OB.
jea 00:35:22 Like, on the note, right?
Ozzy 00:35:23 Yeah, on the node, yeah.
jea 00:35:24 This runs on the node, and then any applications on the node get these things, correct?
Ozzy 00:35:29 Yeah, they get… they can instrument any applications on the node, yeah.
jea 00:35:33 I see. And then, the thing below, the config map.
these instrument… this instrument list of KV pairs is for… Determining, like, which applications get the auto-intermentation, right?
Ozzy 00:35:54 Actually, that's a good question. I think, I could check in the logs, because I… I couldn't say, actually, because it… I don't know, actually, because I have to look at it a lot more, because I'm not sure if it just ignores them, because it can see everything, really, because it's on the.
jea 00:36:09 Yeah.
Ozzy 00:36:10 sure if it just filters and decides, like, I won't export these ones, or won't process them over to the OTLP endpoint, rather than… Yeah.
jea 00:36:18 Yeah, that would be useful to know. I'm just trying to understand how this would fit into our existing CRDs. Yeah.
To generate?
Pavol Loffay 00:36:26 You mentioned… you mentioned, Jacob, if, like, this dictates which Applications get injected auto-instrumentation?
jea 00:36:35 Yeah.
Pavol Loffay 00:36:36 I don't think it… like, the auto-instrumentation, let's say Java auto-instrumentation, Python?
I don't think that's what it does. I think…
jea 00:36:47 No, I know that. I'm just… I'm using the term to describe what this is doing, not to reference the auto-instrumentation libraries that people… that we already inject.
Pavol Loffay 00:36:59 Yep.
The way I understand this is this is the config for the OB binary.
And… What we saw on… in the… in the docs.
was the config when the OB binary is built into the collector?
So that one wouldn't have the config map.
jea 00:37:24 So… yeah, show that again.
Ozzy 00:37:27 The, collector one? Yeah, I have to… This one.
jea 00:37:32 So is this… you have to build this directly into the collector? Like, on… When you build a bill.
Ozzy 00:37:38 It's your own one, yeah.
jea 00:37:40 No, no, not that you have to build your own collector, but that collector configuration Has to be determined in advance.
Like, this thing?
Benedikt Bongartz 00:37:49 No, this is optional, and so the binary can emit OTLP, so if you are fine with sending your OTLP data to, for example, one specific service, and then from there, do fan-out, do post-processing, and all these things, then you're good with the first solution that was shown.
Only if you say, for example, you would like to do some processing, some batching, using the Splunk exporter or something on top.
In that scenario, you would use the collector, or this custom collector, then, with the Seagull binary.
Pavol Loffay 00:38:23 There's, like, two ways to deploy Obi. One is you build it into the collector as a receiver, and one is you deploy it as a standalone thing without the collector.
I see, I see. So there's, like…
Benedikt Bongartz 00:38:34 This is…
jea 00:38:36 Those two things are… I thought that this OB receiver was specifically to receive the data from the daemon set.
Ozzy 00:38:44 No.
Pavol Loffay 00:38:44 I think it's all the functionality of OB. The pieces of the collector are not… there yet. Like, it's not being released as part of the.
jea 00:38:55 Yeah.
Pavol Loffay 00:38:55 It's not part of the collector contive at all.
there is a way how to build it, but users have to do it on their own. There are discussions to… Put this into the collector releases repo, and maybe, over time, have it directly in the contract as a receiver.
jea 00:39:16 Yeah, I think maybe to give a… maybe to… I don't want to take up too much time, because it feels like this is a bit early.
to decide how this should be integrated until we have a binary to release. I don't want to build the release for this ourselves.
I think that… we… I think that we should punt on this until it's determined how… The collector is going to be released, as well as once we understand what the right pattern is for, deployment, once that's actually determined. I don't like there necessarily being two methods.
For this, that feels… Potentially confusing to the user. Thanks.
Benedikt Bongartz 00:40:07 The main point would be… So, if you would try to do testing with this one by today.
I would say that the instrumentation CR is potentially the thing that is the easiest to reuse.
And…
jea 00:40:21 Yes, but were we to use, were we to then use the collector release, we then have to… we have to maintain both of these paths.
And they're in different CRs entirely, right? It's… if we do the collector one, then we have to modify the collector CR, and that'll mostly just work.
But if we do it in the instrumentation one, then the collector one is invalid, right? And I don't think we should make a decision on either of those until it's clear what the release path is going to be.
Pavol Loffay 00:40:53 And the release path is already there. It's… they release it in the OB repo as a binary that people can use. I think that's gonna stay.
There is… there is gonna be maybe additional release, or additional part of… additional distribution that is gonna be part of the collector, right?
jea 00:41:12 Yeah, yeah.
Pavol Loffay 00:41:12 I think that the collector makes more sense for us, because we already have the collector CR, it can be deployed as a sidecar, and as a daemon set, so it covers well the… the use case of deploying COB. I don't know, maybe we will require additional configuration for the security stuff.
That part I don't understand, but, That makes more sense to me.
jea 00:41:40 Yeah, I agree, Pavel. I do think that the security aspect of this is worrying. It's the thing that has always worried me about eBPF instrumentation, and I don't want to be on the hook for… the security… Incidents that will come from this, inevitably.
And that's something that I would want to work out with the OB maintainers.
Because I don't want to maintain, security for eBPF, personally.
And I don't think that that should be our responsibility.
Pavol Loffay 00:42:19 I think that's clear that we don't want to maintain the build of Obi at all, we'll just…
jea 00:42:23 Not just the build bubble, but I mean that, like, the implementation of this is if we are the… distribution method for OBI, which we will become, there will be security incidents relating to eBPF.
And I, I don't want… To need to understand all of the deployment mechanisms and, like.
machinations of eBPF in order to maintain this code path.
Ozzy 00:42:51 I do just… it is… the… the image with the, that runs it standalone is available. I mean, they are building that, and it's on the registry and stuff, so if we were to ever support something using that, we don't have to build it I do think, I mean, yeah, you have to… it won't work if you don't really… give it these capabilities. I mean, that's… that's just, Yeah, it needs that. I mean, I suppose, surely if somebody wants to use it, like, in their cluster, they have to, like, it's also on them to kind of deploy it. Like, I would imagine it would say at the daemon set, you would probably… you would normally just deploy it where the cluster administrator is, and it's in an observability namespace, and things like that. I mean… I suppose… Yeah, I think the operator just… is just setting these… capabilities in the demon set that it needs to run. I mean, I don't know if that brings responsibility as well, maybe.
jea 00:43:52 Yeah, I think the reason that I bring it up, and really the, the source of my concern is that we've had more security incidents in the past 3 months reported than we have had in the past 3 years, and eBPF, to me, is a massive security vulnerability that I do not want to be responsible for Maintaining the security of.
certainly, if we are the distribution mechanism, I don't… want to be the one who has to respond to these security incidents, and I'd like a guarantee around the maintenance and security incidents from the OB group, rather than us just being their distribution.
Pavol Loffay 00:44:42 We are essentially control plane for the obi.
jea 00:44:46 Yes.
Pavol Loffay 00:44:46 Might be, yeah.
jea 00:44:50 That's right, I think until that is sort of agreed upon, and I don't want to move forward Without a good guarantee there. It's sort of similar to the conversations we're having with language implementation… language instrumentation libraries, where we're trying to have an agreement with them about maintenance and version updates, braking changes, security, because we are their distribution mechanism, and I see our role here is much the same. And I want to be sure that we start off on the right footing there.
Pavol Loffay 00:45:25 No, I think this is… better for Obi, because we will not be building the distribution. They will build it either in the releases repo, or there is already one built into Obi. We'll just take that.
And provide a way how to deploy it.
jea 00:45:43 Yeah, but it is just part of it, right? Like, whereas the language instrumentations don't require elevated permissions necessarily, this does require elevated permissions and requires some machination in the cluster to enable it correctly.
And… There will be security incidents with this.
Inevitably. Not on the release, necessarily, but on the distribution.
And… and that's the thing that I want to be… careful of.
Mikolai, do you have thoughts on this?
No further.
Mikołaj Świątek 00:46:36 I am, like… I… I see an argument in my future about how we're actually supposed to deploy this?
Yes. But on all this stuff, I don't have anything.
jea 00:46:52 Yeah, like, I'm happy.
Mikołaj Świątek 00:46:53 Yes, sir.
jea 00:46:54 I think that this stuff is net good. I think that, like, when it works and is effective, it's very powerful.
But, I also think that this is not our… forte, and I just want to be sure that There's somebody dedicated from the OB group that will… you know.
Maintain this part of the distribution.
Ozzy 00:47:29 Have you had any communication with them about this? It's just interesting, I did notice they have a SIG meeting or something, and it was yesterday, and I thought, oh, I should have joined it, but I missed it, I found out about it too late.
jea 00:47:38 I talked with, Tyler Jan, Josh Sareth, and a few others from the OB group.
And this was a topic of discussion where I sort of brought up some of these concerns, and they, I think, were very, open to it, but we didn't really get into the depth, I think, required, for that.
So… I think that it's known that this should happen. I think that there's a larger packaging conversation happening right now within OTEL that, this is a part of.
And I don't know if we've been… Antoine has sort of been our liaison for that, and he sort of knows Where we stand on these things.
And so he probably has the best… context.
For what is happening here.
Bummed that he's not here, but he's super busy, so… But, and Antoine is probably the person with the most context around this stuff, anyway.
Pavol Loffay 00:48:41 I think we should figure out what we are comfortable with.
jea 00:48:45 How… Yeah.
Pavol Loffay 00:48:46 What, like, kind of… How the control plane for this should look like, and then… Get agreement here, and as well… get the agreement, kind of validated with the OP folks, if they… Would support this, and as you mentioned, like, the… help us with the security.
related stuff for the… and, like, it's not only about security, right? We… we've seen that with the instrumentation.
jea 00:49:20 Yeah, I mean, there's definitely an ergonomics thing that's important here as well.
Are we good to move on, or… Was that not a full answer?
Ozzy 00:49:50 I'm good, anyway. I think it's good to just… I'm glad I got to look into it, at least, and to raise the topic or something, but I'm not, you know, I'm not personally embedded in it or anything, so…
Mikołaj Świątek 00:50:04 Okay, the other things we have are just feature gates and issues to discuss at SIG, which I believe… the issues we just discussed at SIG were already… covered. Zone-aware target allocation, we can move… to next time…
jea 00:50:25 That guy isn't here anyway, so…
Mikołaj Świątek 00:50:28 Yeah, it doesn't really matter. Supply chain security hardening again. We don't really have to talk about this, but you can have a look about what's going on in there, because I ended up asking on SIG security.
what… Is there some normalized way of doing this? And the answer is use cosine, we're using cosine. I had a concern that it was polluting the namespace, but apparently everyone does this, so whatever.
I would like to, and I filed an issue for this, I would like to start… stop, publishing the dev images in our current repositories, and create separate repositories for those, just to keep the… Normal repositories cleaner.
Then there's also less, less pollution.
that, but that's something of an aside. The, like, SLSA provenance and software bill of materials thing are not standardized.
But there is, like, a recommendation to use GitHub attestations, apparently, so we might end up doing that.
But I don't think there's really much to discuss about this, unless somebody is interested in talking about… the issue has, like, most… all the stuff that's, like, I think, relevant.
The manage CR feedback, I'll just remove to discuss sake, because I think it's just here for no good reason.
right now?
Zone where it can stay here. Oh, this is a good question. Are we… are we deprecating the Go instrumentation?
jea 00:52:12 Dennis is yes, I agree.
Mikołaj Świątek 00:52:22 How do we want to go about it?
Pavol Loffay 00:52:25 And what's… what's the rationale? Is it not maintained?
Mikołaj Świątek 00:52:30 Oh…
jea 00:52:32 I think it became what Obi is, no?
Benedikt Bongartz 00:52:38 Yes, so it's the underlying path, more or less, So I think OB is the way to do it.
Mikołaj Świątek 00:52:51 I thought it was unmaintained, but the last release was in… was at the end of April, which is not that, you know… Not that far away, it doesn't say anywhere that the project is… Project is deprecated.
Or archived, or anything like it.
But we also don't have it enabled by default, and we should probably say it that way. But I would keep it as long as… As long as the upstream project remains.
I don't know if we can, like… Articulate why we want to… deprecated right now. Or at least, if we want to say, use OB instead, then OB has to actually be usable for us to be able to say that.
jea 00:53:41 Yo.
Mikołaj Świątek 00:53:45 So I… I would keep it. As long as the… as long as the actual OpenTelemetry Go instrumentation repository doesn't say you know, doesn't say they intend to deprecate it and whatnot, I would not do anything.
Mmm… Avo, do you want to… do you want to talk about the RFC? Is there anything you should address here?
Pavol Loffay 00:54:20 I can… I would like to get some more reviews and approvals.
indirectly looking at Jacob, if you could… Have some cycles.
jea 00:54:36 Yeah, I need to, Pubble, it's hard. I've been going back and forth with this guy on this op-amp issue, and that's been a lot of my time, and then I also have all of my other duties, like, normal work duties.
But I will review it today. I need to. I apologize.
Pavol Loffay 00:54:55 Yeah, that's fine, thank you. I can… if you want, we can talk about it right now.
I can give you an overview, but from my point of view, I don't have any… open questions, I think I addressed everything on the PR.
jea 00:55:12 Yeah, I think it's… I think if it's, where we were at… I think if you incorporated the feedback from what we talked about last time, I think it's probably in a good place.
Mikołaj Świątek 00:55:23 Just be aware, be aware, Jacob, be aware, we're using the…
jea 00:55:29 The what?
Mikołaj Świątek 00:55:30 We're using the conversion webhook.
jea 00:55:34 If that's the decision, that's the decision. I'm, I'm… I'm…
Mikołaj Świątek 00:55:38 If you want to propose an alternative, propose an alternative.
jea 00:55:41 None of the alternatives are good. I think the alternative is let's fix Kubernetes to allow us to have two, stored versions, but I don't think that they're gonna like that. And I think that the cycle for that would take probably at least 5 years, so… We're gonna go with… if that's what you both… I am okay to not… be adamant. I'll just have to… I'll make the decision for the charts that, we will not use the conversion webhook, and you have to upgrade yourself manually.
Mikołaj Świątek 00:56:13 Or which chart?
jea 00:56:15 Through the operation.
for the structure.
Mikołaj Świątek 00:56:18 stock, yeah, okay. For the record, I am in favor of instead of doing all the stuff in the helm chart of doing the live patching approach, because every single bigger operator I've seen actually uses that. By which I mean, we don't add the service.
like, we don't, inject it into the CRD using the Helm chart. Instead, the operator does it at, like, startup.
jea 00:56:45 What would that look like?
Mikołaj Świątek 00:56:47 Like I said, the operator starts up, it looks at the… the operator has a parameter, a config parameter, that tells it whether it should do this, and if you tell it, yes, manage the CRD, then it, like, at startup, it looks at the CRD, it checks whether the conversion webhook stands are in there, and if it's not, then it just adds it.
It's an additional permission, but it's, like, the same process that, that Helm would do without all the pain of Helm, and with the ability to actually do, like, real conditional logic in there.
jea 00:57:25 So, just… I'm gonna confirm my understanding and tell me if this is incorrect. The operator starts up, it looks if the conversion webhook exists. It does not exist, and it's been given the permission to make the webhook.
Mikołaj Świątek 00:57:39 It makes the webhook. I mean, when you say make the webhook, this is, like, a part of the CRD.
jea 00:57:46 Yeah, sorry, yes. It makes the service for the webhook.
Mikołaj Świątek 00:57:51 Yes.
jea 00:57:53 The webhook then hits the service, the operator does its conversion, everybody's happy.
Mikołaj Świątek 00:57:58 Yes. One of the benefits of doing it this way is that there's no really annoying waste conditions in the chart.
As in, somebody tries to apply something before the operator is ready, and then weird stuff happens? Yeah, because there's a block on that.
jea 00:58:14 that's existing.
Mikołaj Świątek 00:58:15 Yeah, yeah, because we only add, like, the operator, we only, we only add the definition into the CRD once the operator is ready to actually serve to webhook, which actually… Yeah. Makes things.
More reliable rather than less.
jea 00:58:35 I think that sounds good to me. Certainly, it's a better… it sounds like that's more conventional, so…
Mikołaj Świątek 00:58:42 And you can go… Yeah?
Pavol Loffay 00:58:44 open a ticket for it, and maybe comment on my pull request, I think I can add it to… to the doc I have on the pull request with outlining the… The issues with the webhook.
Mikołaj Świątek 00:58:59 Yeah, sure, I have it, I have it somewhere.
jea 00:59:01 Thank you.
Mikołaj Świątek 00:59:02 I opened up.
jea 00:59:04 Otherwise, Babel, I'm gonna be going through it, like, in the next… Couple hours.
Pavol Loffay 00:59:11 Thank you.
jea 00:59:12 Yeah, apologies. I keep saying I'm gonna get to it, and I keep running out of time.
Mikołaj Świątek 00:59:17 You know, you know Jacob, this whole thing is still up against… the refactor.
jea 00:59:28 I know, I know, I know.
Mikołaj Świątek 00:59:31 What the hell?
jea 00:59:32 nude.
Mikołaj Świątek 00:59:33 You need help?
jea 00:59:35 No, I can do it. I… I can do it. I need to, like, dedicate, Some hack time, maybe this weekend. I'm gonna be on a train this weekend, so maybe that'll be a good time to do it.
Mikołaj Świątek 00:59:45 Why don't you just tell an AI to do it?
jea 00:59:48 Well, that's… that's what I will do, but I still need to do it.
I still need to, like, guide that and be like, this is how it should work. So…
Mikołaj Świątek 00:59:59 On… on which note, like, I… I don't think, Avol, you and Benny have seen this, so I wanna… I wanna show you quickly. I…
jea 01:00:08 I do have to drop to my next meeting, unfortunately, I have a hard stop.
Mikołaj Świątek 01:00:13 Alright, in that case, so just one thing, I'll probably put up an RFC to redo the documentation soon.
jea 01:00:20 Yeah, yeah. I really like what you did.
Mikołaj Świątek 01:00:23 And if you want to see how I kind of intended to look eventually, then you can look… Here.
The pull request is also up in this repository, but I think it's easier to understand how it looks by just clicking through it rather than looking at the pull request.
Yeah, that's all… that's everything from me.
jea 01:00:54 Cool.
Mikołaj Świątek 01:00:55 Alright, have a nice rest of your day.
jea 01:00:58 Yeah, you too. See ya.
Mikołaj Świątek 01:01:00 Yeah.
Pavol Loffay 01:01:03 Goodbye.
Ozzy 01:01:05 I don't know,
