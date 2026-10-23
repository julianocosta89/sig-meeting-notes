SIG: Injector SIG
Date: 2026-10-22
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Jack Berg (Raintank, Inc. – Grafana Labs)** 00:37 What's up, Jacob? I came over from the injector, or the packaging SIG, and Antoine and Michele are either way.
**Jacob** 00:46 I'm a late addition to GoToCoopOn this year, so I will see you there.
**Antoine Toulme (Splunk Inc.)** 00:55 Cool.
Okay, so… let's open the dark… Where is the… Here we go.
I see everybody's in there already. Cool.
Okay, so maybe it's actually, just a quick note, is that in Packaging SIG, we just discussed something from Jack. I'll just push the PR into the notes.
Since this happens to be related, so… Crossover, packaging.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 01:39 Yeah, for Nikola, Bastian, and Jacob, I opened a PR against packaging to, that will start publishing, container images for all of the packages that are there. So, the basic idea is the… To be unopinionated, to basically copy the contents of the package, unadulterated to the image.
And, to be, like, you know, pretty, pretty uniform, so there's… they all use the same Dockerfile, and it's, like, parameterized or templatized which package you're going to extract the contents of.
And, And, you know, I understand that the operator has, has requirements or, like, assumptions that it makes about the locations of certain resources, and so, the, the way that I plan on reflecting that is with, like, like, structured shims, like, essentially. So, like, a structured shim that says, like, okay, the package's contents are arranged this way, and we want to copy or sim link this particular file to this location for operator backwards compatibility.
And yeah, pack… container images would be published automatically whenever the versions of the underlying components are updated. So each time the Injector publishes a release, a new injector image would be published. Each time the Java agent is released, a new Java agent image would be published, and the versions are in lockstep with those underlying components.
like, there's version 2.32.0 of the Java agent. There's a 2.32.0 version of the image.
**Michele Mancioppi** 03:27 Which, incidentally, it is the same target for system packages as well.
We have not been doing that yet, because we do not have yet the reputable way of hosting packages, where we can keep multiple versions of things, and people wanted to be able to lock packages by referencing specific versions.
the moment we have the staff in Cloudflare or Netlify, I assume that is what we're gonna start doing anyhow.
**Bastian Krol (Dash0 Inc.)** 03:59 How does the operator consume the… so it… does it use an init, container and copy over things? And then it would just… if you… if you need… like, Injector and Java and something else, you would just, add more init containers?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 04:21 Yeah, so it's an init container and a copy.
And so I think that necessitates that the base images that we publish, what is it? I think we use, BusyBox?
Yeah, I think the base image is busy box because of that operator copy requirement. But in the far…
**Bastian Krol (Dash0 Inc.)** 04:43 Copy, yep.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 04:44 In the far future, we could start publishing, you know, even slimmer images that, you know, weren't based on BusyBox, and were purely the components from the respective packages.
**Bastian Krol (Dash0 Inc.)** 04:57 No, my more…
**Jacob** 04:58 Interesting.
**Bastian Krol (Dash0 Inc.)** 04:58 in… because the way I'm doing that in the JSDR operator is it's just one big Instrumentation images has all of it, so.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 05:09 You will…
**Bastian Krol (Dash0 Inc.)** 05:09 I mean, smaller is probably better, then you can combine and mix and match. I'm just, thinking about how the operators… it would then need to attach a couple of these Container images, To have multiple artifacts.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 05:28 Yeah, and, exactly. So, Grafana actually also has, like, an Uber image right now for our operator, which is a composite of all the instrumentation images, but, like, as you know, the operator, the OpenTelemetry operator, it does use images that are, like, you know, per instrumentation, not.
**Bastian Krol (Dash0 Inc.)** 05:45 Oh, okay.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 05:45 Uber image, and you know, the advantages of that are many, because, you know, you can cherry-pick and only use the instrumentations that you need, and you can do things like mix and match the versions however you… however you want.
**Bastian Krol (Dash0 Inc.)** 05:59 Yeah, okay.
That's good, nice.
**Michele Mancioppi** 06:01 The Injector is safe in that regard, because of the fact that we check if the instrumentation exists before injecting it.
Which was one of the reasons why we went all the way to SIG can input output, so that it would be fine. If you have an Uber image, you assume that the stuff always exists, so you just dump it in there.
**Nikola Grcevski @ Grafana / OpenTelemetry** 06:25 Yeah, I had a question, would it be possible to… Maybe it's just not… not even an issue. Would it be possible to be… all… each individual image for every programming language uses a different directory?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 06:39 It does do that by, by, because of the fact that it just is extracting the package contents, and the packages use directories that include the language name.
**Nikola Grcevski @ Grafana / OpenTelemetry** 06:51 Okay.
Yeah, the reason I'm asking, because newer Kubernetes does allow you to mount images directly rather than doing a copy, which is… which is nice.
**Jacob** 06:59 Yeah, we.
**Nikola Grcevski @ Grafana / OpenTelemetry** 07:00 spend.
**Jacob** 07:01 We want to do that, but our minimum version doesn't support that. I think what we'll probably do is for… clusters where we detect that that feature is GA, we will do that. I think that we already have logic in the operator for doing that today.
I do think, Jack, I don't know if we'll need to use BusyBox for… this image, because we'll be able to use the injector to do the copying and not CP.
Oh, so we're gonna…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 07:28 Oh, wait. You'll be able to use the injector to do the copying, or do you mean the operator to do the copying, and the operator has, like, some base, init image or something?
**Jacob** 07:38 in the… I have to think about the chain of this, but I was… my understanding of it was that we wouldn't need to have The injector's container used that?
And if we mount the images on the file system correctly, the injector could do the moves.
But maybe I'm… I'm incorrect. I have to think about the chain a bit more.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 08:02 Alright, I'll tag you on the place where we're using BusyBox as just, like, a follow-up, because it'd be really great if we could start with less.
**Jacob** 08:10 Yeah, if we could start with just Scratch, I would be a lot happier. I have to run a few… I have to go off of what, I've already written in what Pavel's already written, to check that stuff.
**Michele Mancioppi** 08:22 Yeah, that Scratch will work only if, you have image volumes.
**Nikola Grcevski @ Grafana / OpenTelemetry** 08:32 Yeah.
**Michele Mancioppi** 08:32 Oh, huh?
If you, if you go to the boulder of recreating CP, But weird and self-contained.
**Jacob** 08:40 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 08:41 Recreating CP is probably a bad idea, that's what I was gonna say, if you do it in Go.
**Jacob** 08:44 That's fair.
**Nikola Grcevski @ Grafana / OpenTelemetry** 08:44 Much lower, yeah, more memory, kudos, right?
**Jacob** 08:48 Yeah, maybe not.
**Michele Mancioppi** 08:48 I would not advise doing that, but it could create a program that has enter point to the fact that you're doing a glorified CP, yeah.
**Jacob** 08:56 Yeah, yeah. Okay, so maybe not, Jack. I was thinking that, like, we could be clever and do some smart things, but it seems that other people…
**Michele Mancioppi** 09:06 I don't know if it is so clever.
**Nikola Grcevski @ Grafana / OpenTelemetry** 09:09 Yeah, I don't know, like, use an agent, say, rewrite the CP in Rust, and make it my own.
**Michele Mancioppi** 09:15 Funny you should say that, because…
**Jacob** 09:17 I think someone did that.
**Michele Mancioppi** 09:18 what Canonica has been doing with the rusty location of the user land, so it actually exists.
**Nikola Grcevski @ Grafana / OpenTelemetry** 09:23 There you go.
**Bastian Krol (Dash0 Inc.)** 09:26 So, the only way I know is that you attach an entry point or a CMD to the final container image that does a copy over, and that then necessitates like you said, boozybugs, or having a DP comment, and also to basically have the files available, or set them via environment available, so if you have a cleverer way, or a smarter way in the operator to do that.
I'm all ears.
**Jacob** 10:00 I think right now, my best bet was to do some, like, SIG magics, and try and see if I could, like, hack something around there, but…
**Bastian Krol (Dash0 Inc.)** 10:10 Wow, okay. That is maybe smarter, but maybe not more robust. Yes.
**Jacob** 10:16 Yeah, probably not, unfortunately. I think once you have the image volumes, then we won't be able to… we won't need to do this, but…
**Bastian Krol (Dash0 Inc.)** 10:22 Image volumes will be great for this, but I think until they are… until we can rely on that most people have them, it will be a few years, realistically.
**Jacob** 10:33 Yeah, I know, it's just… I… we are really at the behest of, like, this minimum version support. The other thing that, like, makes this really challenging is the minimum Go version support, which prevents us from, like, upgrading Go versions as often as we would like to.
Which makes this extra frustrating.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 10:51 Did you see the JavaScript is publishing a V3 of their SDK?
**Jacob** 10:57 I also saw Java is doing that as well.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 10:59 No, that's of the Java agent, but, which is just, like, you know, instrumentation and stuff, but Java.
**Jacob** 11:04 transcript.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 11:05 gotten in the pattern of, like, yearly major version bumps for their SDK. Not their API, their SDK. And, like, the part of it is, like, they don't necessarily… they're not waiting until they have a bunch of big breaking changes that, like, really disrupt things, but they just want to get users to, comfortable with the idea of major version bumps once a year, so that they can do, more mundane things, like bump the minimum version requirements of things like Node, and I wonder if, like, the operator could, like, adopt a similar stance.
**Jacob** 11:37 I would be for that. It's not something that we've really talked about. More of what we've talked about is how we can think about the actual, like.
I mean, how we can be clever about version support, and how we can try and push for better version support from, like, Red Hat, but we haven't really thought about… I mean, a lot of this was also deferred waiting for Collector to reach 1.0.
Given that, like, our current versioning system is in line with theirs, and so it felt odd to, like.
think about… diverging from that initially. So, I think… I mean.
I mean, I think that's probably going to be the main argument against it, is staying with collector version is a thing that is useful for users.
But… I don't know. I think the idea of doing a major version each year and allowing us to then build out more support is good. The hard part is, like, how we will backport features, if at all.
Because there's some things that, like, Red Hat wants for their OpenShift flavor of the operator.
which… it has to have that, like, older version support, and so I just worry about that headache.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 12:56 Yeah.
**Michele Mancioppi** 12:57 The operator already did a number on the configuration… the collector did a number on the configurations of the operator in two ways recently.
One is, Chao Chao Batch Processor in January, some point in 2027.
**Jacob** 13:12 Yeah.
**Michele Mancioppi** 13:13 all the default configurations in the world. And the second is the renaming of a bunch of processors, receivers, to be a snake case.
Yeah.
**Jacob** 13:24 Some of those.
**Michele Mancioppi** 13:24 It's still working, but I don't know until one.
**Jacob** 13:27 Both of those were easy to fix, because we can do, it was easy to add an alias support into what the operator does.
And the batch one, I forget what we did for that.
I'm thinking of what we did for that.
**Michele Mancioppi** 13:44 That the correct answer is exporter cubes, but…
**Jacob** 13:47 Well, no, I know that. I mean, I forget, like, what we did to support the in-between phase there.
I think that we gave people deprecation warning.
And then just did, like, a pass-through. And then for the default that we did, we changed it to exporter queues.
**Michele Mancioppi** 14:04 By the way, I feel compelled, since this is the Injector SIG, to make the point that if you were to reinvent CP as an entry point of the instrumentation image, you would do it in SIG.
**Jacob** 14:16 I would do it in SIG. Yeah.
**Michele Mancioppi** 14:19 That actually would help you to go around the Zoom version, because… How'd it go?
**Jacob** 14:24 No, I know. That was the idea, is that when I alluded to being clever, that was the clever thing. It's like, I could do this in SIG as part of the injector, and then ship it with that as a command.
**Bastian Krol (Dash0 Inc.)** 14:37 But you would need it independent from the Injector.
It would not.
Yeah, it wouldn't need to be separate from the Injector, because you also need it for all the instrumentation,
**Jacob** 14:48 Yeah, yeah.
**Bastian Krol (Dash0 Inc.)** 14:49 like a… it's also in ZIK, and that's the only commonality with the Injector. That would…
**Michele Mancioppi** 14:54 Yeah, you cannot really have a system library that also has a main thing to invoke.
**Jacob** 14:59 Yeah.
Well, you can do, like, multiple publishing from… I mean, you could publish more than one, maybe you don't want to, but…
**Michele Mancioppi** 15:07 I mean, coming from somebody who decided SIG as the language of the Injector, I think that even that is a bit much.
Truth.
**Jacob** 15:15 Antoine, I remember.
**Michele Mancioppi** 15:17 Pretty much.
**Antoine Toulme (Splunk Inc.)** 15:18 So, just a couple things that came up during the… when we tried to do that.
There's an 8 or 10 for me back in… Felt old, like, 2 years ago, almost.
And, the feedback was, actually, you need to support recursive copy, Oh, yeah.
a couple of things. So… But I wasn't that far off, like, you can just take SIG, apply some, you know, cloud on it, and just go.
**Michele Mancioppi** 15:48 Yeah, that would be… I mean, there is, like, the actual CP command.
does a million things with respect to how you deal with inodes and optimize those things, and I understand maybe 5% of it.
**Antoine Toulme (Splunk Inc.)** 16:00 But we're not trying to do.
**Michele Mancioppi** 16:01 Whereas badly, it's easy.
**Antoine Toulme (Splunk Inc.)** 16:04 we're really just trying to move bytes, like, into the thing and done. So… we… I tried to keep the CP boundary of having, like, a common line that looked like what they had, so that it would be less impacting, but… You could have a bigger stance. You say, no, no, no, no, anything in that folder moves over to that new place, and that's it.
So… We could've… I didn't pursue that because I didn't have time, but someone else, they want to do some SIG, and That works.
**Michele Mancioppi** 16:33 So technically, since we're dealing with, No, we still need to be a bit smart about fast system layout. Let's all just swap a fast. Nevermind.
**Antoine Toulme (Splunk Inc.)** 16:46 All I'm saying is, yeah, just con… This doesn't have to be, like, a complete replacement. It doesn't have to be fancy. It needs to be… Working, and it can actually probably, like, skip a few things just to get to where it needs to go and be done.
So.
**Michele Mancioppi** 17:02 The easiest thing is that you don't call it CP at all, you just call it init or something, and then you can do whatever you want.
**Antoine Toulme (Splunk Inc.)** 17:08 Yup.
**Bastian Krol (Dash0 Inc.)** 17:08 But I also think it's, I mean, having a busy box dependency is also not the end of the world, so I'm not sure, is that the top priority? I would challenge that.
**Antoine Toulme (Splunk Inc.)** 17:19 thing, right? Like, two years ago, this used to be seen as a really bad thing. It was a big stain on some projects, and I think there was also related to BusyBox.
Have you heard about that?
I don't know anymore. It's been a while.
**Bastian Krol (Dash0 Inc.)** 17:37 I honestly don't know.
**Antoine Toulme (Splunk Inc.)** 17:39 So…
**Bastian Krol (Dash0 Inc.)** 17:40 Yeah. Okay.
Outrageous.
**Jacob** 17:44 It's because of a licensing problem, right? It's BusyBox's GLPv2.
**Bastian Krol (Dash0 Inc.)** 17:52 Oh, that's a bummer.
**Jacob** 17:53 Yeah.
GPL, not GLP.
**Michele Mancioppi** 17:57 Yep.
Who's going to bring an argument?
**Jacob** 18:00 Pass.
**Michele Mancioppi** 18:01 about that thing having viral implications for the content of OpenTelemTele, come on.
That's insane.
**Antoine Toulme (Splunk Inc.)** 18:08 Well, maybe that's stupid, but you could see a company saying, we just have a policy that we don't want GPL software.
What… what is this shit?
**Bastian Krol (Dash0 Inc.)** 18:18 Yeah, yeah, yeah.
Absolutely.
**Jacob** 18:20 Yup.
**Antoine Toulme (Splunk Inc.)** 18:20 Sorry.
**Jacob** 18:21 I mean, I guess our answer for that is going to be, like, you know, use an image volume, then you don't have to use BusyBox, you don't have to use CP, right?
**Antoine Toulme (Splunk Inc.)** 18:29 Sure, but, you know, sir, we run men's frames, like… Please take a ticket, and sit in the back of the queue. We'll get to you, you know, by your time.
**Jacob** 18:39 Yeah.
**Antoine Toulme (Splunk Inc.)** 18:40 That's okay, it's okay. Just one poem at a time, right? But, yeah.
**Jacob** 18:44 Yes.
I think… all that being said, Chuck, thank you for doing this work. I think that, like.
an improvement in this way is, you know, we're working towards a future, right? And I think that that's always going to be good. I would love to be able to delete the stuff that we have, and get to the point that, you know.
the, feature is, like, our minimum version has GA support for image volumes, and then all of this gets a lot simpler. I do like the idea, Michele, and I'm going to bring it up. We have our operator SIG in 10, and I'm going to bring it up there, and then bring it up at KubeCon about doing what a major version Would look like, just to actually… Like, allow us to push forward a bit?
I worry and just think about what feature support is going to look like in that world.
**Michele Mancioppi** 19:42 But I… I need to ask. So.
**Jacob** 19:44 Yep.
**Michele Mancioppi** 19:45 Why is the operator version?
The Mantra 10. Well, in reality, what we're talking about is versioning of CRDs.
**Jacob** 19:55 This would not just be a CRD thing, though, because the operator is… it, like, the APIs that it has access to. I mean, we could make it so that later versions of the CRDs can only be run on later versions of Kubernetes.
And then the operator would be able to have that as a guarantee to make it so that only image volumes are used. But then we're still kind of in this dual state, right?
**Bastian Krol (Dash0 Inc.)** 20:28 Your concern for a major version is to drop support for all Kubernetes versions, that's the main… Intent for the braking version, is that right?
**Jacob** 20:38 kind of. The worry that I have is behind that, which is by dropping support for these previous versions, or, you know, by sort of bisecting the code paths further along the lines of a version change like this.
We make it challenging to push any new features that we need to push to all versions, which is… which does happen, actually, quite frequently.
And so… I think, like, you know, we could say, as the Injector group.
that, you know, we only want the injector to work with image volumes, because we don't want to dependency on BusyBox. In which case, we could make it so that, you know, the injector only works on versions of Kubernetes that have support for image volumes.
**Michele Mancioppi** 21:22 I believe that the Injector itself has a horse in this race.
It's what I'm sorry.
**Jacob** 21:28 That's what I agree. I… that's what… sorry, like… That is what I'm saying. I'm saying that, like, we shouldn't do that because the Injector group shouldn't, like… that's not the mandate of this group, right?
And so… the challenge is that I don't want to, like, further entangle The rollout of the injector for the operator by needing to figure out A more complex versioning strategy.
**Antoine Toulme (Splunk Inc.)** 21:56 Okay.
**Jacob** 21:59 But, I mean, ideally, this would all go away if we could just stop supporting the minimum version, but it's like…
**Michele Mancioppi** 22:06 I mean… I expect.
that in the CRD for the instrumentation CRD.
Injector is an opt-in flag.
Yes?
**Jacob** 22:16 we're just gonna… we're just gonna do it for people. They… it's gonna just happen, like… The… we're gonna make this an opt-in feature flag on the operator, but we're going to replace This as a functional, like, no-op.
For users, so that eventually they'll just be using the injector, and they don't even have to think about it.
**Michele Mancioppi** 22:38 acquire… what are you going to do with the… annotations for .NET and Python for the.
**Jacob** 22:45 Those are… those are all separate concerns. Those are all things that are happening also in parallel to this, but we want to move all of the code paths to use the injector initially.
**Michele Mancioppi** 22:57 Because those, those annotations They no longer need to exist.
**Jacob** 23:06 Well… Yes and no. The Injector is…
**Michele Mancioppi** 23:09 Wait a second, do you plan to have two different images per Python, For each flavor of libc.
**Jacob** 23:17 No.
Wait, what?
**Michele Mancioppi** 23:22 Python and .NET, you need to, in the operator, you need to add an additional annotation to tell which flavor you want.
The Injector doesn't have a hoop.
**Jacob** 23:32 Yeah, like, lives here are Muslim.
**Michele Mancioppi** 23:34 Work subversion, right?
**Jacob** 23:36 Yes, yes.
**Michele Mancioppi** 23:37 So, in the images that you want in the operator, are both libc versions In the same, in the same, image.
**Jacob** 23:50 this is getting ahead of where we are, but I think, realistically, no, they will not be. I would like them to be in the same one, because they don't need to be in two different ones.
But… like, we can… those annotations just become ghosts in the future, right? They'll just be no-ops. They won't… people can set them, but they just won't do anything.
And that's fine. Again, like, I'm trying to… Get the Injector into the codebase as much as possible, and then we can begin to swap out the actual, like.
user experience here, with everything becoming no ops that are just no longer needed, because they just don't need to set anything. It's the same experience for them, but these flags just won't do anything, because they don't need to do anything.
Right.
And to me, that's a better user experience than asking them to go in and change to use the Injector. I don't think it should be an opt-in thing. I think they should just use it, because it's better.
**Michele Mancioppi** 24:45 I still have problems wrapping my head around the fact that the operator wants to, despite the Injector, wants to make separate images for every single language, so the user still needs to go and annotate. Like, I really have difficulties with that.
**Jacob** 24:59 And you're… you're conflating two things here, where it's like… I would like us to start using the injector so that eventually they won't need to do that.
**Michele Mancioppi** 25:09 Damn.
**Jacob** 25:10 the, like, you know, we have to be careful about the rollout here, and I would rather get the injector in prior to needing to stage that.
**Michele Mancioppi** 25:18 I don't understand rationale, it's just in my head.
**Jacob** 25:21 Excellent.
**Michele Mancioppi** 25:22 time. I completely do the obvious end state of the uber image.
**Jacob** 25:26 Yeah.
**Michele Mancioppi** 25:27 It's hard-coded, I'm sorry.
**Jacob** 25:29 Yeah, it's not ideal, and I'm not disagreeing, but it's…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 25:34 Wait, so Michele, you don't like the… you don't like the annotations, once the injector's there? Yeah, I like…
**Michele Mancioppi** 25:40 I find that the end user having to know which language is used in which specific pod.
**Nikola Grcevski @ Grafana / OpenTelemetry** 25:47 And which Glibsy version, muzzle or Glibsy?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 25:50 So, the way I think about it.
**Michele Mancioppi** 25:52 Okay, that screams vengeance, but the other one, also the other one, I have issues with.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 25:57 the way I see this is, like, the adding Injector support, like, enables centralized selection.
So, like, once you have the injector, you can have a centralized selection predicate that describes, like, where you… but, like, that doesn't stop it from being potentially useful to have an annotation-based approach. So, like, even if you had centralized, like, selection predicate, like, you still might want to support a standardized annotation approach, so you can very… anybody that wants to can very selectively cherry-pick and control this thing. And so, like, I agree with Jacob. I think these things are… Orthogonal to each other, and, like, you know, the next step after adding the injector is to update that contract to have centralized selection.
And then you don't have to use the annotations, but you can.
**Michele Mancioppi** 26:41 I do not disagree, it's just intermediate steps of family. It's just my problem.
**Jacob** 26:46 It's my girlfriend.
I mean, I wish… again, like, all of this sort of stems from… You know, trying to not break the user contract, and also trying to not, like, like, it's so… every time that we've pushed, even, like, the… anytime that we have to do a CRD change, it is such a pain in the ass. And so, like a breaking CRD change. And so all of this I'm trying to do with little to no CRD changes, so that when we do one of those, it is, like, we are getting exactly the thing that we want out of it, and we don't have to worry. We break the people once, you know?
I think that that's the right experience.
But it's far from ideal.
I mean, ideally, everybody updates their software frequently, and our release cycles could be faster with…
**Michele Mancioppi** 27:39 Yes, that's, of course, what the world has proven with the new PHP CVs that Titik Sakhino.
**Jacob** 27:46 I have a feeling that, the, like, probably, you know, billions of servers out there still running, like, PHP3 or something, or still gonna be running PHP3 tomorrow and for the next 3 years.
**Michele Mancioppi** 27:59 I would say, like, the 4 and 5 was very much the inflection point of adoption, so those there.
Are exploitable until the end of time.
**Jacob** 28:07 Yeah.
Yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 28:11 The exploitable, it's a feature, not a bug.
**Jacob** 28:17 One thing that I.
**Michele Mancioppi** 28:18 It's a lot for J people who had a very similar bug.
And they've been hunting to death to this day about it.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 28:28 PHP3, just because it's exploitable. That's…
**Michele Mancioppi** 28:31 By the way, for the record.
I, I, I welcome the universe's irony.
of making the only saved versions of PHP, also those that are auto-instrumentable with auto.
I think I… I like to think that there was a design behind it.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 28:52 It is poetic.
Yeah.
**Jacob** 28:54 So, Michele, you're saying that you were behind this, then?
**Nikola Grcevski @ Grafana / OpenTelemetry** 28:57 Yeah.
**Jacob** 28:57 Because you sold your sword.
Yeah, no, no, you told your swarm of agents, go find a way for everybody to upgrade to the latest PHP version for.
**Michele Mancioppi** 29:08 How do you get…
**Jacob** 29:09 of instrumentation.
**Michele Mancioppi** 29:10 Are you giving me very ill-advised ideas about getting rid of language versions I don't like? Like Node with CommonJS? Is that what you're advising? Because I might be listening.
**Jacob** 29:23 Did you… did you see the… there was a funny joke that I saw online that was, like, You know, this all started because somebody told Claude that they wanted to update all PHP code to Rust, and so Claude's best option of doing that was getting RCE on every PHP server.
**Michele Mancioppi** 29:43 I mean, if the guy of, if Dan of ChainGuard was right, and the issue could be found by asking an LLM to find bad bugs in PHP, which I don't… I don't know about that. I don't know about that one.
If that is the case, then sure.
**Jacob** 30:01 Okay, I gotta run to, to… Nikola Grcevski @ Grafana / OpenTelemetry 30:04 Yeah, I had a question for you, Jacob, I mean, sorry.
**Jacob** 30:06 Yes.
**Nikola Grcevski @ Grafana / OpenTelemetry** 30:06 put it on the agenda, so I guess the status right now is that you're working on getting the injector through another way, because that one issue was closed.
Where that was proposed to add the injector into the operator.
**Jacob** 30:20 Yeah, once, this, this was, Nikolai's, proof of concept, and there's… Pavel also wrote one, and once we have the images in the packaging SIG, then we're just gonna pick it up from there, with the actual images as usable.
And then do all the swaps that we're talking about. But all of these are sort of, like, we operator maintainers, like, running proofs of concept for experience, to see how it feels, to, like, see what the code looks like, just get a feel for what the actual, like.
both user experience is going to be in, like, our developer experience, but it is… it is going to happen, and I am mentioning it literally in every operator SIG meeting going forward, until we are… until the code isn't there.
**Nikola Grcevski @ Grafana / OpenTelemetry** 31:06 Okay. So, go ahead.
**Jacob** 31:07 But it's… Nikola Grcevski @ Grafana / OpenTelemetry 31:08 It is the thing that…
**Jacob** 31:09 Yes.
**Nikola Grcevski @ Grafana / OpenTelemetry** 31:10 Yeah, the reason I'm asking is because I have a KubeCon talk, where I'm just demoing how cool the Injector is, and how it works well with Obi. But yeah, I was hoping that maybe I can demo with the operator, but I think we're just gonna write…
**Jacob** 31:25 Probably not yet.
**Nikola Grcevski @ Grafana / OpenTelemetry** 31:27 Yeah, I'm gonna write a demo operator, that's all. Yeah.
**Jacob** 31:30 Yeah, yeah. I mean, if you want to, you know, vibe up the solution once Jack merges in that PR, I will… I will review it.
**Nikola Grcevski @ Grafana / OpenTelemetry** 31:40 I mean, no, for the demo, we're just gonna wipe code something that just is an operator that uses the injector, using the approach that, I mean, we have so far. I mean, it's a shame that it seems like everybody's duplicating this effort. Apparently, Splunk also has an operator that does this, Dash Zero has now, Grafana has, we're all kind of… We're writing our own, because we want this kind of automated… automatic,
**Michele Mancioppi** 32:04 To be perfectly honest, the Z01 is the OG.
Good for you, Tony.
**Nikola Grcevski @ Grafana / OpenTelemetry** 32:09 I agree, I agree, I agree.
**Jacob** 32:11 And the…
**Michele Mancioppi** 32:12 So let's dot the I's and cross the T's. Everybody's copying their table, that's a different topic.
**Jacob** 32:16 Okay, fair enough.
**Nikola Grcevski @ Grafana / OpenTelemetry** 32:17 Fair enough, fair enough, fair enough.
**Jacob** 32:19 Okay, I gotta run, guys. I'm running late. So, I'll see you later, and I'll see you at KubeCon probably next time, so…
**Michele Mancioppi** 32:26 Sounds great.
**Nikola Grcevski @ Grafana / OpenTelemetry** 32:27 Yep. Me too. Bye.
**Bastian Krol (Dash0 Inc.)** 32:29 Goodbye.
**Nikola Grcevski @ Grafana / OpenTelemetry** 32:31 Bye.
