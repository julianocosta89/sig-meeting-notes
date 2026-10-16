SIG: Injector SIG
Date: 2026-10-15
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Jacob Aronoff** 02:10 Jack, it might just be you and me today. I think a bunch of Europe is on vacation.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 02:16 Oh yeah, I, I figured it was the, the classic, the packaging SIG before this, and everybody over at that, but…
**Jacob Aronoff** 02:26 Maybe? I know that, Nicola's out… Bastion is out.
Maybe they're still the packaging SIG, but I assumed that there's, like, something… some European, we're all out today type of thing going on.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 02:46 Yeah.
Why don't we wait till the 34 mark and just call it, unless you have topics? But like you know, even if you did, I think I'd be sort of like ill-equipped to make progress on them, just you and me.
**Jacob Aronoff** 02:57 Yeah, I mean, my only one is, that I'm trying to get the injector and the operator, and we just need an image for the injector for the operator.
To use, and I would like it if the operator weren't the people to build that image, and instead, like, the Injector were, there's an old issue that Bastion had opened a while ago about it, and so I either would like the injector to do that, or the packaging group to do that, one of those two things, and then we can align those release cycles with the operator's one. Like, we can take in whatever the injector releases into the operator, and then we don't have to manage, like, another image in the operator repo.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 03:38 Yeah, and I deleted all the images. I assume the operator wants all the images to ideally be, you know, published elsewhere as well.
**Jacob Aronoff** 03:45 Yeah, that's the goal. That's already happening now with PHP and Ruby, I think.
But that's why I want to bring it to the group, is just be like, hey, I can make a… here's Antoine.
But, like, you know, hey, I can make a Docker image.
In the Injector or the packaging repo for us to use, and let's just use that.
So.
That's my only agenda item. I think it'll be uncontroversial.
**Antoine Toulme (Splunk Inc.)** 04:16 So.
**Jacob Aronoff** 04:18 Hello.
**Antoine Toulme (Splunk Inc.)** 04:19 Mikita is at an offsite, so it's, It's not going to happen.
**Michele Mancioppi (Dash0 Inc.)** 04:24 Just drop by to say hi.
**Antoine Toulme (Splunk Inc.)** 04:27 Oh.
**Michele Mancioppi (Dash0 Inc.)** 04:29 Okay.
**Antoine Toulme (Splunk Inc.)** 04:33 Some names.
**Michele Mancioppi (Dash0 Inc.)** 04:34 What did they miss from the packaging SIG?
**Antoine Toulme (Splunk Inc.)** 04:37 So hold on.
Oh, man, come on. Real quick, we open… we follow up on the issue with, Austin to ask him where we are at on having access to a big storage in Cloudflare. He said he hasn't heard back yet. It's been a week.
That's what it is.
And we opened an issue in community to really ask Netlify access, so that we can go and change some of the settings for DNS and CAA, so we can coordinate that with Cloudflare, so it has a proper certificate and a delegation of domain, which we're not sure how to do.
So if we do all those things, we're good. Dennis is like, I got my stuff, it's kind of ready. I see Mikaela wants some changes, but once that's done, we're going to be in a good shape.
And then you ask if you want to make a fresh release, it's Sid Vikercom.
That's mostly… that's half an hour.
**Michele Mancioppi (Dash0 Inc.)** 05:30 Okay.
**Antoine Toulme (Splunk Inc.)** 05:32 Okay.
**Michele Mancioppi (Dash0 Inc.)** 05:33 Thank you.
**Antoine Toulme (Splunk Inc.)** 05:34 You're welcome. All right, Jacob, you got an issue open.
**Jacob Aronoff** 05:39 Yeah, this is probably gonna be brief, but yesterday, last week, when I brought the, goal of bringing the injector into the operator, the only blocker that we had identified is that we just need an image, for the injector.
To then use that to do all the injection, and the operator would rather not be the ones to, like, build, release that image, and rather than just align that with the injector releases that we do.
I can write up the Docker file. I know Destio already has a Docker file for this somewhere.
But… Yeah, that's kind of the only blocker that we identified, and so… If Bastion was, like.
unsure about it. His response to me was… Yeah, he's not sure, you know, given that, you know, we… what'd he say? We've been building system packages and moved that into its own sitting repo.
Yeah, he was saying that, you know, we could maybe put this in the packaging repo, and put it there as, like, the thing that is published.
But I'm open to any… any comments on this, on how it should be done.
**Antoine Toulme (Splunk Inc.)** 06:54 Interesting. Okay.
Yeah, is that a packaging thing or an Injector thing, right?
And so there's… the discussion that happened in the Injector back then is, like, we used to have an image per language, but this new image will have all the languages at once, because the Injector does not care and can find whatever is running on your Docker container.
And intercept it, and inject it.
So it's a bit of a difference in architecture.
Yeah. That's still okay from a security concern?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 07:32 So, sorry, were you talking about a, a sort of, an Uber image that contains all the instrumentations.
Yeah. I would advise against that, and the reason is, is because it couples all of the instrumentation versions together.
**Antoine Toulme (Splunk Inc.)** 07:49 Yes, that's… indeed, that's a…
**Jacob Aronoff** 07:53 Antoine, I think we were still going to do… The, like, our own images, and then… Just use the Injector to do the actual like mounting.
Rather than the operators and injection code.
**Antoine Toulme (Splunk Inc.)** 08:09 Oh, okay, so you want to base… You want to continue to use your operator instrumentation SDK images?
**Jacob Aronoff** 08:16 I believe that was the plan.
**Antoine Toulme (Splunk Inc.)** 08:19 team.
**Michele Mancioppi (Dash0 Inc.)** 08:20 That means that the customer still needs to go and annotate on each pod what they want.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 08:25 Yeah, just one… it's like one thing at a time, right? So, first.
**Jacob Aronoff** 08:28 the.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 08:29 The Injector present, and then you can adjust the instrumentation CR to have selection criteria.
**Antoine Toulme (Splunk Inc.)** 08:34 Oh, okay. So you want.
**Jacob Aronoff** 08:36 Exactly right.
**Antoine Toulme (Splunk Inc.)** 08:37 So, is Injector going to be the base image of the Java SDK image in the operator?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 08:44 No.
**Jacob Aronoff** 08:45 I.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 08:45 A separate standalone image is, like, would be the thing, just like, and, you know, the purpose of this image is just to, like, bundle up the Injector resources so it can be copied to the file system, essentially.
**Antoine Toulme (Splunk Inc.)** 08:57 Her mom.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 08:58 To the file system, let's say, not copied necessarily.
**Antoine Toulme (Splunk Inc.)** 09:01 Okay, that makes sense. Alright, so we're just here to do a delivery mechanism.
But you could have just as well have, instead of having a Docker image, a step in your build that says copy from the GitHub release.
the Injector so far, right? It's okay.
So we're.
**Jacob Aronoff** 09:18 That could also work.
When I was talking to Miguel about this, who… Miguel or Pavel said this last week. I forget who. Let me look at my, before I say anything incorrect.
Let me go to my notes.
**Antoine Toulme (Splunk Inc.)** 09:35 No worries, no worries. I know it's, Can't remember last week either, so…
**Jacob Aronoff** 09:40 I took terrible notes. That's great.
You sound like me.
**Antoine Toulme (Splunk Inc.)** 09:48 That's usually…
**Jacob Aronoff** 09:49 But initially, we're just gonna do this for .NET, because then we don't have to think about the S390X and PPC architectures, and that will then be sort of our, like.
Test bed to be sure that the actual path works, and then we can go and do it for the rest of the languages.
But we can start it off with one, just be sure that that works end-to-end, and we don't get any, like, massive complaints. We have people that we could, like, tell to flip this flag.
And then we can bring that all the way to stable, and then we can do that for all the other images, and then all of them will… Just go through the Injector at that point.
**Antoine Toulme (Splunk Inc.)** 10:26 Alright, so you want a Injector container, which just contains the shared library.
And you want it for every flavor that we're going to support, right? So all the different builds. And… and then you're based off that. Okay.
for you.
You'll use it as part of your own build as a multi-stage builder to copy it into your final image.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 10:52 No, there's this way that you can, And I don't know if this is what the Injector is plan… or the operator is planning on doing, but you can… you can mount, and images resources to a, like, a volume in Kubernetes.
**Antoine Toulme (Splunk Inc.)** 11:07 Yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 11:08 That's what we do for our our Grafana, you know, the the operator that we have that leverages the Injector right now, like, you know, while we while we while this capability doesn't exist in the upstream operator.
And, yeah, so you can… that's the best way to do it. It's like an image volume mount thing.
And that basically means that, like, whenever the image is, like, cached on each node, it takes, like, zero time, essentially, because you don't have to do this copy step every time the container starts up, so it greatly reduces startup time if you use this, but… That was only added in a certain version of Kubernetes, and so the fallback is to do the classic, you know, copy resources on Container Start.
**Antoine Toulme (Splunk Inc.)** 11:50 Yeah.
**Michele Mancioppi (Dash0 Inc.)** 11:51 It only takes zero amount of storage, additionally, because when you go on nodes that have a good amount of pods.
Those instrumentation files copied into every MTDR, which is back to file on the node, they add up.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 12:06 Yeah, it's really great when this, when Kubernetes supports this, so…
**Jacob Aronoff** 12:11 Yeah, I think that the operator has the flag to… Check for the volume.
Or, like, what's the, feature in Kubernetes call check? Is it image mounts, or is it volume mounts?
**Antoine Toulme (Splunk Inc.)** 12:25 It's.
**Michele Mancioppi (Dash0 Inc.)** 12:25 Some image volume.
**Jacob Aronoff** 12:27 An image. It was the verb.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 12:30 You would expect, I guess.
**Jacob Aronoff** 12:31 The other half of what I was thinking. Yes, the image volume.
the… I think we have a thing that's already doing an image volume check that Ben added for some feature earlier, so I think we'll probably want to take advantage of that, but we do have, like, our minimum Kube version for support is very old.
And so…
**Antoine Toulme (Splunk Inc.)** 12:52 What is… what is it? It's 127, right?
**Jacob Aronoff** 12:55 It's, like, 120… yeah, I think it's 127, maybe 128, we might have bumped it recently.
I figured.
I think that, Image volumes… When did this go stable? It's stable since 136, so it's, like, pretty newly stable.
But…
**Antoine Toulme (Splunk Inc.)** 13:17 Okay.
**Jacob Aronoff** 13:18 We'll definitely want to use that.
But that's the idea, is it's basically just doing this copy. I mean, really, like, my goal is to just get the injector in there to start.
And the more logic that we can remove from the operator, the better, and then the less that we have to do, the better, and then the more that we will, like, move towards this injector path that is… Totally, like, a no-op for users. Like, they'll already be using the Injector, and then we can just push more into what the Injector already does, is kind of the idea that I have.
**Antoine Toulme (Splunk Inc.)** 13:53 Okay, so, I'm going to take notes in the issue itself, right? So…
**Jacob Aronoff** 13:59 Thank you.
**Antoine Toulme (Splunk Inc.)** 13:59 We discussed this in SIG meeting on 1015. We want the first simple Injector Docker image with a multi-architecture setup, right? Because we… so, please, bear with me. You're going to have one tag, but it's going to work with whatever architecture you're working with, with the ARM.
AMD, what have you, right? Is that fair?
**Jacob Aronoff** 14:21 Yep.
**Antoine Toulme (Splunk Inc.)** 14:21 Okay.
**Jacob Aronoff** 14:21 And then what we said for the, just to confirm this decision back.
We had said about… the S390X and the, like, the, you know, weird architecture is what I'm gonna call them.
Yeah. Is that we essentially, you know, already can't test the operator on these architectures. We're, like, riding blind. Functionally, it's, like, kind of up to Red Hat to test that for us. And so… We're going to do… as we roll out the Injector is essentially just do best effort for when we think that we're on that architecture.
We'll disable this code path.
But otherwise, this will be the default going forward.
So… essentially, like, in a Red Hat release that we know It's gonna be on one of those architectures. We will default The gate to be disabled, or, you know, whatever operator config flag we're going to add in for this to be disabled, but otherwise it will be enabled by default, and it's gonna be an opt-out feature, so that we can essentially just cordon off this logic until We come to some, agreements, or whatever, about the S390X stuff.
But I'm… I do not want to block that stuff anymore, and I would rather this just go through.
**Antoine Toulme (Splunk Inc.)** 15:39 Okay, yeah, I think the operator decides how much it wants to… So anyway.
**Jacob Aronoff** 15:45 Yeah, I mean, I said very.
maybe too brash last week. I was like, you know, we can't test this, I don't really want to support it, and we can do our best effort, but we should not try and, like, hold up basically everybody else just for this, like, one unknown special path that we've never gotten any requests about.
Like, I was ready to just drop support for it, but, I was… Vetoed on that one.
**Antoine Toulme (Splunk Inc.)** 16:14 Pablo Pony's gonna not be happy with that, so… Okay. But that's the game, right? You gotta actually…
**Jacob Aronoff** 16:21 the.
**Antoine Toulme (Splunk Inc.)** 16:22 Okay, It's a scratch image, right? We were just going to have a scratch image with the .so file in it.
**Jacob Aronoff** 16:32 I think, yeah, I mean, I think it'll be distroless, not Scratch. I don't think we use Scratch anymore.
Right.
**Antoine Toulme (Splunk Inc.)** 16:39 We don't?
**Jacob Aronoff** 16:41 I thought that everything comes from distroless.
**Antoine Toulme (Splunk Inc.)** 16:45 Oh.
**Jacob Aronoff** 16:46 That might be wrong, but…
**Antoine Toulme (Splunk Inc.)** 16:48 Okay, so, sorry, maybe…
**Jacob Aronoff** 16:49 Check.
**Antoine Toulme (Splunk Inc.)** 16:50 Maybe what I mean to say here is that it's a single layer image with no base or anything. Like there is no OS, no nothing.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 16:57 Yeah, same as all the other instrumentation images as well.
**Antoine Toulme (Splunk Inc.)** 17:00 Right. I mean, they have the instrumentation images because of some crappy reasons are based off BusyBox and they come with CP.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 17:11 I just mean, like, the intent of them is just to be a holder for the resources.
**Jacob Aronoff** 17:15 Yep.
I mean, ideally, we will not need BusyBox after this. Like, once all of the things… once this work is done. We theoretically do not need that anymore.
**Antoine Toulme (Splunk Inc.)** 17:27 So it's a scratch image. Let me just single layer.
Nothing else.
**Jacob Aronoff** 17:35 Like actually for .NET specifically, I wonder when we do this change if we could just get rid of BusyBox.
As the base image.
**Michele Mancioppi (Dash0 Inc.)** 17:44 It would.
You could… you could literally go with a, We can literally do from scratch, and just put in there the.
**Jacob Aronoff** 17:56 Director.
**Michele Mancioppi (Dash0 Inc.)** 17:56 You need nothing, you do not need the, the time zones, you don't need anything, there's no user land.
**Jacob Aronoff** 18:04 Yeah.
That could work. I mean, I am not opposed to that, generally. I think that having this image gives us an out in case other people are not for it, and then worst case, we, like.
**Antoine Toulme (Splunk Inc.)** 18:17 you know.
**Jacob Aronoff** 18:17 are publishing a Docker image that few people use, but…
**Michele Mancioppi (Dash0 Inc.)** 18:22 Yeah, but it's… you need to be, I mean… the decision So it doesn't hurt to have it in the image, because it's in a volume image, it's inert.
Yeah. That's all.
So in that case, it's only, like, the… This kind of vanity metrics of CVEs against PCBox.
**Jacob Aronoff** 18:44 Sure.
**Michele Mancioppi (Dash0 Inc.)** 18:51 So I would say as long as there are, there are, like, I think we can remove BusyBox in three years from now. By then, most Kubernetes clusters are going to be 136 and above, but until then.
Yeah.
**Antoine Toulme (Splunk Inc.)** 19:04 Yes.
Okay, I posted a comment. It's very simple. Now, I have a question for you all, which is… Is the Injector project in charge of making this image, or should that be a packaging issue, or…
**Michele Mancioppi (Dash0 Inc.)** 19:18 Packaging, we should have it in packages.
**Antoine Toulme (Splunk Inc.)** 19:22 Yeah. Right?
**Michele Mancioppi (Dash0 Inc.)** 19:23 Yep.
**Antoine Toulme (Splunk Inc.)** 19:23 So packages can get in the business of doing docker images.
**Michele Mancioppi (Dash0 Inc.)** 19:27 Yes, it's like 95% the same.
Bits that we put in Debian and RPM archives. Come on.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 19:35 Hey, Miguel, would it be useful if I, if I contributed to the packaging repo these, like, some automation to publish these Docker images? Like, the idea in my head has been, like, you know, there should be an automation that for every new version of the Injector which is published.
The automation over in packaging detects that and publishes a new Docker image that contains that. And the same thing should be true for the instrumentations as well.
Like, basically, like.
**Michele Mancioppi (Dash0 Inc.)** 20:06 That would be great.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 20:06 unopinionated republication, repackaging up of these artifacts that are published elsewhere.
**Michele Mancioppi (Dash0 Inc.)** 20:12 Yeah, that'd be great. We already have a system built on, I think, Renovate.
To detect versions, so the real open question is… And that's something that… I mean, it's sitting on my desk since forever, and I'm sorry about that. Go and talk to the operator and the collector people to say, hey, can we use together, like, do you want to consolidate the registry under packaging? And we keep building the images the way to do it right now.
And then later on, there is a little bit of stuff that you can improve. But, like, if… Jack, if you could take over and say, look, I'll make sure that these projects, like, they move the container image building into packaging, then we take it from there.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 20:55 I think it's pretty reasonable to say that container image publishing is under the packaging SIG's charter, and, you know, the people that consume those images is, like, primarily the operator today, and I don't think they love the fact that they have to publish those images. It's just, like, it's a necessity, given, like, how things have developed, and so, like.
I don't think we need to ask permission. I think we start publishing those and communicate like, hey, operator, we're going to start publishing these images. When the time is right for you, you should migrate over to using these images with the first candidates being the injector.
**Michele Mancioppi (Dash0 Inc.)** 21:33 Yes, right.
**Antoine Toulme (Splunk Inc.)** 21:35 Oh, okay, I'm okay with that.
So here we're talking specifically about the operator use case, where we're going to do mounting volumes, we're going to do all sorts of things, and this is the reason why the Injector image is going to be extremely lean, and then there's going to be a separate image for the SDKs and whatnot, and we'll iterate on that.
But for… Sorry to bring this up, but I think I also want us to have some sort of a… Docker image that's, beefier, that is going to have, help us with ECS and Lambda-type use cases.
**Michele Mancioppi (Dash0 Inc.)** 22:13 Lambda is not going to help to shit on one.
Because Lambda images, they are going to need the runtime. So you're not using those images. You need to layer on top of the images from AWS.
**Antoine Toulme (Splunk Inc.)** 22:28 That's right. These are layers, and then you need to publish those.
**Michele Mancioppi (Dash0 Inc.)** 22:31 But then you have, in those cases, you have actually a much better route with system packages.
**Antoine Toulme (Splunk Inc.)** 22:38 So you want the layers to be based off installing the RPMs in each layer?
**Michele Mancioppi (Dash0 Inc.)** 22:42 They're not really layers, not in the case of Lambda, but adding the instrumentations is actually easier with APT than it is by layering another image on top of it.
**Antoine Toulme (Splunk Inc.)** 22:53 Oh, I see. Okay. Alright.
Well, the ECS case remains, but… You can try to ignore it.
**Michele Mancioppi (Dash0 Inc.)** 23:01 No, ECS, I'm very much of the opinion that the one mono image is the correct way to do these things, because asking customers to annotate pods or task definitions with the right thing is barbarism.
If the operator people want to take it slower, because it's a big scale change.
Okay.
But eventually, I mean, I'm with you. It's one chunky image.
**Antoine Toulme (Splunk Inc.)** 23:24 So, so, are we… okay, so then we should just prepare our plans that we're gonna have two flavors of an Injector image, one that is the simplest possible packaging of that image for all sorts of reasons, right, that we outlined in this call, and then another, which is going to be the all-in-one Uber… like, you drop this, you can base it off, or… I don't know, how to say it in a way that… This image is kind of going to be the base for ECS type deployments or stuff like that.
**Michele Mancioppi (Dash0 Inc.)** 23:57 And Kubernetes type deployments.
**Antoine Toulme (Splunk Inc.)** 24:01 Eventually.
So.
**Michele Mancioppi (Dash0 Inc.)** 24:03 one.
**Antoine Toulme (Splunk Inc.)** 24:04 Do we want to provision? Is there a separate issue for that or just I can edit my comment and add that we.
**Michele Mancioppi (Dash0 Inc.)** 24:10 It was waiting for somebody to pick up the job of setting up the container image creation.
**Antoine Toulme (Splunk Inc.)** 24:18 Yeah, indeed. No, I… and this is actually the reason why it should be in packages, too, because it's a conference of not just the Injector, but every single instrumentation SDK we care about.
**Michele Mancioppi (Dash0 Inc.)** 24:30 And besides, the funny thing is.
That, the operator is actually not gonna care.
whether it's single images put there or not, because the customer in the instrumentation CRD has a way of overriding the image. So the customer could say, use always the chunky one for all these languages, and then the operator will inject it.
**Antoine Toulme (Splunk Inc.)** 24:55 Yeah.
Yeah.
So, we'll have the container, the conveyor will contain the injector and all supported.
SDKs.
This work will happen… This issue will be fulfilled, implemented.
through the Becking SIG.
And, maybe we should transfer the issue.
Is that fair?
It looks like it can do it.
Vicky, you'll sing, yes.
No? Okay, alright, I'll wait.
**Jacob Aronoff** 25:49 Sorry, I'm… Distracted.
**Antoine Toulme (Splunk Inc.)** 25:53 No, I know.
It's okay.
Right, we're going to the end, we've got 4 minutes left. Anything else we should talk about?
This was nice.
**Jacob Aronoff** 26:03 Because it looks very, In a very relaxed place. I don't know where he is, but that looks like where I would like to be.
Yeah, I'd like to be there. I'd love to be there. That'd be great. That's Portugal.
**Michele Mancioppi (Dash0 Inc.)** 26:22 No, it is Croatia. We're in Dubrovnik.
**Jacob Aronoff** 26:25 Oh, that's beautiful.
Here you can see my incredible view. It looks very similar.
Let's see if you can… if it'll focus.
**Michele Mancioppi (Dash0 Inc.)** 26:34 So I appreciate the different colors of concrete you have, Nils.
**Jacob Aronoff** 26:39 Thank you.
I don't know how to turn off my focus. That's fine.
**Michele Mancioppi (Dash0 Inc.)** 26:44 No, no, leave the focus on for the love of God. It looks better like this.
**Jacob Aronoff** 26:52 Okay.
**Antoine Toulme (Splunk Inc.)** 26:54 Well, will you, is… are you all going to Salt Lake?
**Jacob Aronoff** 27:00 I don't think I'll be going, unless something changes, which I don't think will in the next month, but…
**Antoine Toulme (Splunk Inc.)** 27:07 Good.
Well, we'll be missing you, but if, if things change, please let us know, and then there's no…
**Jacob Aronoff** 27:14 I'll be an EU, hopefully.
**Antoine Toulme (Splunk Inc.)** 27:17 Okay.
**Jacob Aronoff** 27:18 Is the plan.
Barcelona in March sounds a lot better than Salt Lake in November.
**Michele Mancioppi (Dash0 Inc.)** 27:26 Yeah, but they're skipping the family reunion. I mean, how dare you, sir?
**Jacob Aronoff** 27:30 It's a good point. It's a good point.
Alright, well, I gotta, I gotta get going, but…
**Antoine Toulme (Splunk Inc.)** 27:37 Yeah, same.
**Jacob Aronoff** 27:37 Thank you, everyone.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 27:39 Yeah.
**Jacob Aronoff** 27:39 Can I enjoy…
**Michele Mancioppi (Dash0 Inc.)** 27:40 Hi, folks.
**Jacob Aronoff** 27:41 Enjoy your time.
**Antoine Toulme (Splunk Inc.)** 27:42 Thank you. Yeah, enjoy your weekend. Take care.
