SIG: Community Demo App SIG
Date: 2025-09-24
Duration: 30 minutes
Zoom Recording URL: https://zoom.us/rec/share/skpCut4di0vETiKD2afd9A8k0t8c87l_0VoxrpywaIaiPxwVxOIrtvLl5BwQwSCe.NdaLHj44TKiGfKfz
============================================================

## Zoom Recording Transcript

**Juliano Costa | Datadog** 00:18 Hello, hello!
**Cyrille Le Clerc** 00:19 Hello! Nice, meeting you in, video.
**Juliano Costa | Datadog** 00:24 Yeah, well, likewise. How do you think?
**Cyrille Le Clerc** 00:27 good.
**Juliano Costa | Datadog** 00:28 Good, good. Yeah, it's been a busy week.
But, yeah, and it's just Wednesday, so…
**Cyrille Le Clerc** 00:36 Oh, joke.
**Juliano Costa | Datadog** 00:38 Hey, Alessio.
Oh, he's gone.
Hmm.
Let's see here… see…
**Alessio** 01:02 Ken Heromino?
**Juliano Costa | Datadog** 01:04 Yes.
**Alessio** 01:06 Oh, no.
**Juliano Costa | Datadog** 01:09 Yes!
**Alessio** 01:09 I had the audio coming up from my main speakers.
**Juliano Costa | Datadog** 01:14 Okay.
**Alessio** 01:16 Where can I This is it.
This is it.
Okay.
**Juliano Costa | Datadog** 01:23 You change the camera, but yeah. If it works, I'm happy.
**Alessio** 01:29 No, I didn't change the camera, actually. Okay.
**Juliano Costa | Datadog** 01:31 Okay, so it was just a Zoom.
**Alessio** 01:34 Yeah.
**Juliano Costa | Datadog** 01:37 Cool.
So, I…
I have to leave a couple of minutes earlier, so maybe we should get things going. I see that we already have a couple of stuff on the… on the… on the agenda to discuss. Siri, is that you typing?
**Cyrille Le Clerc** 01:58 Yes.
**Juliano Costa | Datadog** 01:59 Okay, and for some reason, when I pronounced your name, my phone thought I was.
**Cyrille Le Clerc** 02:04 Oh, yeah, that's a game.
**Juliano Costa | Datadog** 02:05 Yeah. Okay, cool.
**Cyrille Le Clerc** 02:15 Oh, yeah.
And I am from Grafanael.
**Juliano Costa | Datadog** 02:18 Oop.
**Alessio** 02:21 Welcome.
**Cyrille Le Clerc** 02:23 Thank you.
**Juliano Costa | Datadog** 02:24 Oh, yeah, he's… he's been already contributing, for the demo for some time already, which is great. So we… I see a bunch of,
Rafana dashboards coming up, so this is cool. But I think it's your first time joining the scene, right?
**Cyrille Le Clerc** 02:42 Yeah.
**Juliano Costa | Datadog** 02:43 Cool. And now we have Shenoi and Roger. Awesome! So, we have a…
a bunch of folks. Cool.
**Cyrille Le Clerc** 02:53 Hopefully, later down the road, I can explain why I'm doing… what is my goal.
Because there is a goal.
**Juliano Costa | Datadog** 03:00 Okay, cool. So, one thing that I, that I, maybe…
Maybe we do not need to… to answer now, but just to put on everyone's radar.
radar. The first item on the agenda is about… so a guy accidentally opened a PR on the repo, and this PR was adding, or replacing a service with, Swift
Implementation.
And he closed and said, hey, sorry. And I was like, hey, no, come on, I want that now.
**Alessio** 03:34 Yeah.
**Juliano Costa | Datadog** 03:35 So, I think now that we have our elixir back, Swift is the only official hotel language that we do not have on the demo.
That would be cool, but in the discussion itself, he mentions that he's using an old tau Swift, and not the OpenTelemetry Swift.
So, I don't know what… what… what's the thing there. Maybe we should think about it, but yeah, just to put… just to think about, so…
So, on… regarding releases.
I could have released, but just for Docker at the moment, and when I was doing the sync with
all the environment variables that we updated for Docker.
in the latest release, I saw that we were missing a bunch of environment variables, just to streamline all the environment variables in the whole, Docker HomePoles YAML.
So, I'm gonna cut another release, just with these changes, that, should be good, as now I have the approval from Roger and Pierre, so maybe I'll just increase the Elixir, memory, and…
Hope it works. Yeah.
Terry, sorry about that.
Well, on my tests, I also got, like, 97 mechs of memory consumption.
I'm actually…
**Alessio** 05:07 I'm really worried because, like, 97 megs is, like, borderline, like, barely approaching the 100 megs, so…
Maybe it's worth it.
**Juliano Costa | Datadog** 05:19 Yeah, that's true, but like…
Yeah, I don't know why the difference is so big between, my system and Roger's system, so…
**Roger Coll** 05:33 Yeah, I have no idea. We can test on a Kubernetes cluster, maybe, and see how it…
But it's, yeah, it's weird, that big difference. But for now, we can just increase it, right? It's…
It's not requested, it's just a limit, so… What's funny.
**Juliano Costa | Datadog** 05:53 Cool. And another thing that I changed on that PR was that I, instead of using Postgres.
Upstream, I created a Docker file for Postgres.
Because with that, we can publish the hotel demo Postgres that has the init, init descript within it, so we do not need to configure volume in Kubernetes in Helm.
So, as we were just doing this init thing, and we needed to…
we needed this init script in Docker to start the… the database?
I thought about, like, why do we need that just for this? Like, if it was something that we actually have a volume that is increasing or whatever, but as it was just for the unit, I thought.
It would be better to have just a…
our own thing, and then, we do not need to touch all the persistent volume and stuff in Kubernetes.
Cool. Okay.
**Cyrille Le Clerc** 06:58 Sorry, you… you didn't inject a config map.
in Kubernetes, in the Kubernetes, in the Postgres container to do your stuff?
**Juliano Costa | Datadog** 07:09 No. Not at the moment.
**Cyrille Le Clerc** 07:12 Okay, because I did this and it worked for me.
on top.
**Juliano Costa | Datadog** 07:17 Okay. But the thing is that for post… for the Postgres that we have at the moment.
We are only copying the init file into the container.
Well, in Docker, we are passing that as.
**Cyrille Le Clerc** 07:34 amount of volume.
**Juliano Costa | Datadog** 07:35 volume, yeah? But we do not need that if we have our own container, and this init container… this init script is already part of the container.
**Cyrille Le Clerc** 07:45 Yeah, although I've done it, I can share, I have.
**Juliano Costa | Datadog** 07:49 Yeah, that would be cool.
**Cyrille Le Clerc** 07:51 I do it with a config map.
It took me time, but okay.
**Juliano Costa | Datadog** 07:57 Yup.
**Cyrille Le Clerc** 07:58 the example here, so maybe, so I can reuse the standard, Postgres.
I'm dropping it, in it.
On Kate.
Using.
**Juliano Costa | Datadog** 08:15 Okay, so you… you copy the whole init script?
In the config map. Okay, I see.
**Cyrille Le Clerc** 08:24 I think it's a Gitub Copilot who told me.
**Juliano Costa | Datadog** 08:29 I think that works fine, because once you have the config map, you can add the config map into the container, and then you'll have it.
**Cyrille Le Clerc** 08:37 What I like is that in my config map, I have a very easy-to-read init.sql file.
**Juliano Costa | Datadog** 08:43 Yep.
**Cyrille Le Clerc** 08:47 Maybe.
**Juliano Costa | Datadog** 08:48 Opinions, guys? I'm… I'm open to change the… well, I haven't opened the PR for Helm yet, so…
Happy to change the approach.
**Alessio** 09:02 I don't actually have a strong opinion about that.
**Roger Coll** 09:08 Yeah, me neither.
**Shenoy Pratik Gurudatt** 09:10 Yep, me neither. For the…
Docker custom image, do we have any overhead maintaining it in long time?
**Juliano Costa | Datadog** 09:18 Know what…
There is one thing that bothers me, personally, is that we have nightly releases, and those nightly releases are not being used, and we have…
Nightly releases every day, for…
like, ages. So, if you navigate to…
to hub.docker and search for the auto demo registry, you see that we have Hundreds of thousands of images.
Which I personally don't like, but yeah, maybe we could revisit that.
**Shenoy Pratik Gurudatt** 09:58 Yeah, for that, I think we can just change the cadence to weekly, maybe, if not nightly.
There you go.
**Juliano Costa | Datadog** 10:06 Yeah, that would reduce, yeah.
**Shenoy Pratik Gurudatt** 10:08 Yeah.
**Juliano Costa | Datadog** 10:08 But if we're not even using, maybe we can just drop, because…
Helm uses the… the latest release.
and Docker… uses whatever you have as latest, but the nightly release is not updated as latest, so…
**Shenoy Pratik Gurudatt** 10:30 You are, yeah.
**Juliano Costa | Datadog** 10:32 you're not using, unless you actually go and copy the image tag for the nightly release and…
**Shenoy Pratik Gurudatt** 10:39 Pull it.
**Juliano Costa | Datadog** 10:39 music.
**Shenoy Pratik Gurudatt** 10:40 Hmm.
**Juliano Costa | Datadog** 10:41 then…
Yes, Siri?
**Cyrille Le Clerc** 10:48 I have two questions, please, related to this. One, and I think Chenoy will have the same point coming from OpenSearch.
how do we consider bundling components in the demo, like on the… on Kubernetes? Sometimes some components recommend to use an operator, and maybe OpenSearch is recommended to… now recommends to use an operator to deploy OpenSearch.
For PostgreSQL, there is the same… there are handshards, operators. I know for Grafana now, we… we like to promote our operator. So, did the group
Put some thoughts, but there is a trade-off, because operators are often more for production-grade deployment than for demos.
On maybe consuming more resources. But did the group put some thoughts on…
The guiding principles to deploy some, off-the-shelf components.
**Juliano Costa | Datadog** 11:50 So, what we opted in since the beginning was to make it easy to people deploy locally, and with that, we chose to use Helm. So, if you check the Helm chart, you'll see that we are using the Helm chart for
we have our own helm chart for the demo, but we also use the helm chart for Jaeger, we use the helm chart for,
The conference?
**Cyrille Le Clerc** 12:20 limited.
And a couple of more that I could easily get.
But now the handshot can be directly for the container or for the operator that will start itself.
**Juliano Costa | Datadog** 12:34 Hmm, okay, so, you can use Helm to… to…
To configure the operator as well.
**Cyrille Le Clerc** 12:41 Yes.
**Juliano Costa | Datadog** 12:42 Okay,
**Cyrille Le Clerc** 12:43 But it will also be my next question, with the OpenTemmetry CubeStack.
Which I love to, deploy a hotel connector.
**Juliano Costa | Datadog** 12:53 Bye.
**Roger Coll** 12:53 Yeah.
**Juliano Costa | Datadog** 12:54 Never heard of that.
**Cyrille Le Clerc** 12:56 It's amazing.
**Roger Coll** 12:57 Actually, yeah, I would be in favor of… of using the CubeStack, and actually, this is what we use for the elastic demo fork.
**Cyrille Le Clerc** 13:07 It's, putting a lot of… it's contributing a lot to, the CubeStack,
**Roger Coll** 13:11 Yeah, because it's great. It just installs the operator very easily, all the permissions, etc, etc, and you have everything. Auto-discovery, all the host, Kubernetes metrics.
And that's actually the onboarding there. And then, for the demo, what we do is just…
Let's say we disable… we still use the OpenTelemetry demo Hemp chart, but we disable everything, and we just modify
let's say the collector endpoint to point to the one deployed by the KubeStack.
And we have, luckily with that, we have not only the hotel demo, let's say, metrics, traces, logs, but also, the node host and, let's say, all the other metrics from the Kubernetes.
And works pretty good, so… Maybe something we can… Yeah, take a look.
**Cyrille Le Clerc** 14:12 Yeah, yeah, and for me, I would add to Roger, so I… for me, I drop the benefits I see.
My gut feeling is that it will become the obvious default to install Hotel on Kubernetes soon, because it's so feature-complete.
We demo a turnkey setup, because it's just with one else chart, you have auto-instrumentation, auto-injection of config.
And you also enable… OpenTeametry-based infrastructure monitoring.
And it's what I've been contributing on the Docker Compose part.
Recently,
In my opinion, it's really time to showcase how Hotel is good at doing infra monitoring, and so it's good at unifying all the telemetry types, all the layers together.
**Juliano Costa | Datadog** 15:00 Cool. Yeah, I, I, I'm happy to…
**Cyrille Le Clerc** 15:04 I have a demo, I… Julie, I know I can demonstrate that it works. I have a branch.
**Juliano Costa | Datadog** 15:09 But the auto-injection, you would need to…
**Cyrille Le Clerc** 15:13 Of the configuration, but not of the binaries.
**Juliano Costa | Datadog** 15:17 Wait, wait.
Yep.
**Cyrille Le Clerc** 15:24 Hotel operator can inject either directly the binaries, like the hotel Java agent, the hotel.net libraries, or you can say it's called inject SDK, name is maybe questionable, but it will just inject the open telemetry configuration environment variable.
And it's already amazing.
**Juliano Costa | Datadog** 15:47 Okay, yeah, that helps a lot.
Okay, that makes sense. Yeah, I thought it was the… the auto-instrumentation, so, like.
Because we can also do that, but the demo is already instrumented. Okay.
**Cyrille Le Clerc** 15:59 For me, it will also be, we will raise the bar on the concept of auto-instrumentation. Auto-instrumentation is not only
Booking the right, proxies in your code to measure stuff, but it also injects with exactly the right naming conventions.
So that you can easily correlate your pod logs with your profiling that are external to your SDK, and also all your SDK stuff. You will have service instance ID right everywhere, and so on.
**Juliano Costa | Datadog** 16:30 Okay, and do you have an… do you have an example of the devil using that?
I'm working on it.
Okay, and I think Roger has?
Something like that, and…
**Roger Coll** 16:42 With Hustaf, do you mean?
**Juliano Costa | Datadog** 16:44 Yep.
**Roger Coll** 16:45 Yes, I can show.
**Juliano Costa | Datadog** 16:48 Because in your case, you disable the current AutoCollector, and then you use the CubeStack. But maybe we can make CubeStack the default, and if people want to use the auto collector Helm chart, then they disable CubeStack and do the other way around, because
From what I see here, CubeStack seems more… creates ready.
Yeah, no, I like that. I… to be honest, I wasn't aware of this new power chart. So, yeah.
Looks good to me.
**Roger Coll** 17:24 Yeah, so we will still need the demo handset to deploy the services.
But, a prerequisite, maybe, or a previous step would be to install the CubeStack one, and then just point to…
to the collector endpoint deployed by CubeStack.
**Juliano Costa | Datadog** 17:44 So, let's do this.
Okay, I think I need… I honestly don't know how we're gonna do that. So, I'm gonna add as a to-do here, so I organize myself.
**Cyrille Le Clerc** 18:01 I'll be happy to work with Roger to craft a branch on this, I think. Roger, if you have some stuff, I have some stuff as well.
**Roger Coll** 18:10 Yeah, sounds good.
**Cyrille Le Clerc** 18:13 There are some challenges.
that I highlighted.
**Roger Coll** 18:19 But then…
**Juliano Costa | Datadog** 18:21 Jesus Christ. Okay, I, I… My…
My skills here are not,
good enough. Okay, so first thing, I'm gonna… release, new version.
with, imparts.
I think that's actually… Maybe required for, for everything.
Then, second, I'm gonna release the Helm chart, because whoever is waiting to deploy the demo on latest is not able since last week, so…
And I think once I have the Helm chart merged.
I think we can start working on that.
So, I'm gonna open the HomeChart PR tomorrow, so this is gonna, hopefully be released soon.
And then, if you guys already have something, and maybe start,
work… working on the… I don't know, we can…
Because I think replacing the Helm chart dependency is not too much a fart, right?
Because it's a dependent helm, right?
**Cyrille Le Clerc** 19:52 No.
**Roger Coll** 19:53 There is one, subtle thing is.
**Cyrille Le Clerc** 19:57 Hotel operator has to be instantiated before your services, so it can annotate, it can enrich the metadata of your deployment.
Another thing that is a bit tricky, maybe Elastic is familiar with this, but
There are some things that don't work on Docker Desktop Mac.
Speaking.
**Roger Coll** 20:20 Okay, you mean in the macOS machine or something like that?
**Cyrille Le Clerc** 20:23 Yes, there is a… and we have attention because.
**Roger Coll** 20:26 doesn't they vote?
**Cyrille Le Clerc** 20:26 should work everywhere, and the hotel operator is more for, production, and…
**Roger Coll** 20:32 Yeah, we have seen some issues, right, when reading from the…
**Cyrille Le Clerc** 20:36 From a different system, yeah.
**Roger Coll** 20:38 Exactly, yeah, for the process, etc. Yeah, but I think for that, if we, for example, wanted to add the host metric receiver in the Octel demo of Handshot, we would have the same issues.
**Cyrille Le Clerc** 20:51 We will have to make it disabled.
**Roger Coll** 20:53 Maybe, yeah, yeah.
**Cyrille Le Clerc** 20:56 Auth metrics on pod logs are not possible when deploying on Docker Desktop Mac Kubernetes, but, possible on traditional Linux, and we have to test on Docker Desktop Windows, and I guess, on other Kubernetes
dev environment.
**Juliano Costa | Datadog** 21:15 I'm a huge fan of Kubernetes, but I hate the Docker desktop Kubernetes, so in my case, it's not even enabled. Like, I don't do that.
So, yup.
**Roger Coll** 21:30 Many times.
Yeah, just… I wanted to share, this is, let's say, the…
the Helm chart demo configuration that we… let's say, let in the… well, we specify in the Elastic Hotel demo, you see that we disable, basically, the hotel collector that the…
demo chart uses, and what we do instead if this override the collector
Name, but it's the endpoint, basically deployed by the… by the CubeStack concept.
And as easy as that, we… we are sending everything to the… to the collector. But…
what we could do is just, yeah, kind of similar approach, and then the CubeStack,
It allows to basically override everything.
in the…
of the deployed collector. For example, this is the values that, also we ship for the CubeStack Humpshark, and we overwrite basically everything of the collectors. It's a very large file, it's…
Yeah, 600 lines of code with our, let's say, our defaults, and our configs, but the really good thing is that it installs
the… everything that is needed in a real Kubernetes environment, right? All the…
roles, permissions, the… also the if-serve manager that's needed, etc, etc. So, that's… that's great.
**Cyrille Le Clerc** 23:04 Something that will be great education is we will be able to verify why Elastic did not choose the presets for Kubernetes attributes enrichment for host metrics.
Because we have presets on the end chart, on the Hotel Collectorium chart, or the hotel cube stack. On here, you have decided to not use them on that… for me, it's extremely interesting.
**Roger Coll** 23:27 Yeah, there's, yeah, there's… there are reasons, but it was, because, yeah, we were using, like, a custom processor for modifying those attributes because of some, data mappings that we had, but yeah, we can… we can discuss,
that offline, or I can share, yeah, more, more feedback on that. But yeah, the end goal would be to
to use the presets, because it will be a simpler configuration, more aligned with what Upstream does, right? And…
It would be great, but… yeah, yeah.
with Pine.
**Cyrille Le Clerc** 24:13 on, I guess, Alessio, you work at, rancher, or, Susan… no.
**Alessio** 24:19 Exactly, yeah. I'm working at Suze, yeah.
**Cyrille Le Clerc** 24:23 And your company produce a Kubernetes testing environment for developers, something like this, on which we could test?
**Alessio** 24:30 We have, Rancher Desktop, if you wanna… if you wanna download it and test.
It uses, basically, K3S underneath.
**Cyrille Le Clerc** 24:42 So, yeah, because we don't want to break the demo for a big fraction of the practitioners.
**Alessio** 24:49 I guess, yeah.
**Juliano Costa | Datadog** 24:59 So, I added here as to-do, that I'll release a new demo version.
Then the Helm chart, that the PR is almost ready. I'll just double-check, tomorrow morning and send the PR, and then Roger and Siri, will work on
sending a follow-up PR on how to replace the collector with the CubeSat.
**Cyrille Le Clerc** 25:24 Okay.
**Juliano Costa | Datadog** 25:26 I think for this last thing, the… The part that will… be more head-lifty is,
So, we're gonna need to bump the Helm chart, which is pretty simple, but then we need to, I think, adapt the dots.
on how to bring your own collector config, or something like that. I think that will change, because now the deploy is through our operator, so we need to figure out,
what to change. But I think, Roger has that, as you are already doing some stuff, for.
**Roger Coll** 26:11 If we make.
**Juliano Costa | Datadog** 26:12 Elastic?
**Roger Coll** 26:13 if we make the kube stack Henshart a dependency of…
the OpenTelemetry demo, maybe we don't need to, let's say,
tell the user to install the CubeStack before, and just, let's say, modify it, demo, but I need to.
**Juliano Costa | Datadog** 26:32 Yeah, no, the question is more… so, like, with our config, I think that will work fine. It's more about when you want to use the demo, but send to your backend.
So, like, where are you gonna change the config and everything? So, I think this… it's just a matter of documenting on where to do. We have our own… we have that on the docs at the moment, so…
**Roger Coll** 26:58 Boom.
**Juliano Costa | Datadog** 26:59 replacing that.
**Roger Coll** 27:00 Yeah, exactly. We'll be about commenting the collector config in the new values file, and just this info right as we do on Elastic. But yeah, that would be great, and I think very aligned with this issue that we have on the demo about simplifying the deployment.
for vendors just to point to an OTLP endpoint, and that's it, so… That's, that's… that's great.
**Juliano Costa | Datadog** 27:23 Yeah, whenever the vendor accepts OTLP, but I'll not talk about that.
**Roger Coll** 27:30 Home recording.
**Juliano Costa | Datadog** 27:32 Bye.
**Cyrille Le Clerc** 27:33 Yeah, I identified something here that I feel you're at the right point. So, for users, I'm confident it will just be tweakabbit values.yaml, and they will be able to tweak the stuff. But then vendors who have their own distro of the demo.
On here, I am thinking of, honeycomb.
We'll repackage the demo a bit.
because they want to demonstrate infrastructure monitoring, Kubernetes monitoring, so they enable loss metrics on a file log, or something like this, or a Kubernetes event. And we have to ensure that these vendors
We'll be able to hook their stuff.
**Juliano Costa | Datadog** 28:09 Elegantly.
**Cyrille Le Clerc** 28:10 With the new setup.
**Juliano Costa | Datadog** 28:13 Exactly. Yeah, this is going to be a big, I would say, breaking change to all the vendors that have instructions on how to deploy on Help.
on how to deploy in Kubernetes, so we need to… to maybe.
**Roger Coll** 28:28 Yeah…
**Juliano Costa | Datadog** 28:29 It will yield some noise around it.
**Roger Coll** 28:32 Yeah, make… maybe a blog post or something like that to read them sometime would be great.
**Juliano Costa | Datadog** 28:39 Cool.
Awesome.
Cool. Yeah, thank you. That was nice.
Boom.
I will… I have to go. I have a meetup to run.
But, the to-do is here, and I'll take a look on that.
**Alessio** 28:58 Do we want to merge the docs change on… at the… on the OpenTelemetry website about the…
**Juliano Costa | Datadog** 29:07 Oh, I need.
**Alessio** 29:07 the Elixir stuff, or you need to review. If you need to review completely, it's okay.
**Juliano Costa | Datadog** 29:14 I… I already saw the PR, I already reviewed the PR, it's just about, like, checking the latest.
**Alessio** 29:26 Okay, yeah.
**Juliano Costa | Datadog** 29:27 updates, because I, I added a bunch of, a couple of comments.
Where is it?
Ugh.
**Alessio** 29:39 No, go, go, I don't want to be guilty of… of chaining your desk.
**Roger Coll** 29:46 Send it to me, if not, I can give it a review as well.
**Alessio** 29:51 Fair.
**Roger Coll** 29:53 So…
**Juliano Costa | Datadog** 29:55 Cool, so I'll just paste here on the…
Oh, I already closed the SIG meetings. Pasting here on the chat.
If you want to take a look, Roger. I just… I just, updated the…
The branch, and approved the…
**Alessio** 30:14 Perfect.
**Juliano Costa | Datadog** 30:15 the checks, so we're gonna have, Deploy preview soon.
Oh, you can take a look.
**Roger Coll** 30:25 Awesome.
**Juliano Costa | Datadog** 30:26 Thanks, everyone.
**Roger Coll** 30:28 Thank you.
**Juliano Costa | Datadog** 30:29 babe?
**Alessio** 30:30 Thank you.
