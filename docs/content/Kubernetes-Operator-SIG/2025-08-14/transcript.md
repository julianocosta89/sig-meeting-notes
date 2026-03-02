SIG: Kubernetes Operator SIG
Date: 2025-08-14
Duration: 51 minutes
Zoom Recording URL: https://zoom.us/rec/share/iEqZ3S3XSdWQL1-yJ0ncp9efeuCLG2IS4-mikncLLLQQj6dEUENIoIAlaTYf8s_s.F3HBePXxpUVKkFme
============================================================

## Zoom Recording Transcript

**Antoine Toulme** 00:26 Good morning, Jacob.
**Jacob Aronoff** 00:28 Hey, how are you?
**Antoine Toulme** 00:32 I'm okay, kids aren't school.
**Jacob Aronoff** 00:34 Ugh.
**Antoine Toulme** 00:35 That's that.
Yeah.
Alright, so… I know Mesh, Svetiak is, …
Sorry, Mikolaj is in, is on vacation.
**Jacob Aronoff** 00:49 Yep.
**Antoine Toulme** 00:50 Let's see what else shows up.
**Jacob Aronoff** 00:53 Yeah, I'm expecting a… like, last week was super light. I'm kind of expecting that this week is going to be the same. I think, you know, all the Europeans are out on their fun vacations having fun while we Americans toil.
**Antoine Toulme** 01:11 Yeah, …
I got a good smattering of folks, out of Karco at Splunk, and they're all working pretty hard, so….
**Jacob Aronoff** 01:23 Yeah.
**Antoine Toulme** 01:23 But yes, of course, people should take whatever time they need.
**Jacob Aronoff** 01:27 Oh, yeah, of course. It's more that I wish that I could take a… take a nice… Vacation.
**Antoine Toulme** 01:34 Yeah.
**Jacob Aronoff** 01:35 It's jealousy more than anything.
**Antoine Toulme** 01:37 It did take 3 weeks this summer, so….
**Jacob Aronoff** 01:40 Yeah? Where'd you go?
**Antoine Toulme** 01:42 France.
**Jacob Aronoff** 01:45 Nice.
**Antoine Toulme** 01:45 Yeah.
All over, winter, so for, like, meal friends, Vendee…
We went to… Girard, then I went up north.
Mostly, got a nice heat wave, mosquitoes, the whole shindings.
**Jacob Aronoff** 02:04 Yeah.
**Antoine Toulme** 02:04 Nope.
But, yeah, it was fun. …
It's 3 weeks is long per American standards, so I came back and people were like, who are you again?
Not a good idea.
**Jacob Aronoff** 02:15 ….
**Antoine Toulme** 02:17 But I do have… and that actually kind of disrupted a little bit what I wanted to make sure we would be getting to, which is the PR, which I opened, and I still have not had the time to re-watch the recording of last time when you guys talked about it.
**Jacob Aronoff** 02:32 Yeah, no worries. I actually don't even know where the recordings go anymore. I don't know if we… there's, like, a sheet, right? But I don't know if the sheet is updated.
**Antoine Toulme** 02:39 You have to… yeah, you have to really know where… yeah, you have to be motivated to find things, yes.
**Jacob Aronoff** 02:45 ….
**Antoine Toulme** 02:46 So….
**Jacob Aronoff** 02:48 I don't know if you read through the… did you read through the notes yet?
**Antoine Toulme** 02:51 The notes were interesting, and the comments from Kalash were saying things like, I'm not opposed, that's okay, what you're trying to achieve, but this duplication of the model code into the config folder is kind of not cool, because you're creating a bit of a tension where things will be harder to maintain.
If I understand correctly.
**Jacob Aronoff** 03:12 So we need to move that code out of the webhook into its own thing, and….
**Antoine Toulme** 03:18 kind of manage it from there, and then we can share it between those different usages, right? So it's not duplicated.
**Jacob Aronoff** 03:26 I think that'd be better for you anyway, right? If the goal.
**Antoine Toulme** 03:28 Most of you, yeah.
**Jacob Aronoff** 03:28 use, like… the operator code almost as, like, a library externally. Like, this… this would help enable that, right?
**Antoine Toulme** 03:35 Yeah, actually, I mean, the end goal for me would be, like, there are two things that I can do with this, right? One is, I can run this as a HUM chart without initialis.
just like we did for target allocator, I could take a slice of the operator and just make the autosomnotation hook
Deployed on its own in a nice little hemp chart that would just benefit customers, like ours, who don't need a whole operator for this.
And that would be really sweet. That would really play out well to the injector project as well, because we can start to find ways to kind of make this… I'm not sure yet, right? I'm just trying to go one step at a time into this, and make sure.
**Jacob Aronoff** 04:12 No, but I understand the vision. I mean, this all makes sense to me. I think in the next few months, I'm hoping to begin working on the design for the…
Instrumentation selectors, so that you can actually…
Just say, you know, instrument everything, and….
**Antoine Toulme** 04:31 That would be great.
**Jacob Aronoff** 04:32 Yeah, that's what I think we should be doing after this. Once I have time, like, that's… that'll be my contribution for injecting.
**Antoine Toulme** 04:41 If you see, like, the dash zero people also bringing the injector.
work into, like, they want to have this LD preload, so that also might change the way we think about injection, because instead of having this annotation system and doing it one, like.
We could just, like… nilly-willy just drop into any container this LD preload hook.
And it would do its job, and….
**Jacob Aronoff** 05:09 Yep.
**Antoine Toulme** 05:09 maybe we…
Maybe the operator needs to care less about how the stuff is done. I don't… it's kind of a big change, ….
**Jacob Aronoff** 05:17 Yeah, I mean, I think, I saw their comments earlier today, in the injector channel, and…
I think this all makes sense. I just think, like, our job, like, operator job to enable it is just let's…
Get a really good user experience down…
for how someone says, go to inject this thing. I like the idea of not needing to specify languages.
I remember you proposed that.
**Antoine Toulme** 05:44 works, yeah.
**Jacob Aronoff** 05:45 as well, and I think it should be, like, for everything that works, like, we have a few languages where it should just work, and then everything else will just say, just specify, you know.
some extra label on your pod, or some extra label on the instrumenter, and that's how we'll know to distinguish between, like, an NGINX thing, which LD preload I don't think would work for.
Who knows? I mean, I don't know, I haven't tested any of this, but….
**Antoine Toulme** 06:12 No, you have me.
**Jacob Aronoff** 06:13 That's the idea, is generally, like, I just want to provide.
**Antoine Toulme** 06:16 the actual Kubernetes mechanism.
**Jacob Aronoff** 06:20 To then pass off to the injector, and make it so that users don't need to think much about it at all. That, I think, is a good goal.
**Antoine Toulme** 06:27 Yeah, we are really being hit by customers who want to not think.
**Jacob Aronoff** 06:32 Yeah, oh, yeah, well that's… I mean, isn't that the story of our lives?
**Antoine Toulme** 06:37 We're, like, our business, the reason we have a business is because we try to commoditize, like, layers and layers of abstractions and interactions like this, and I think we're breaching the point where we tell people to put the label on their pods, and they go, I don't want to do one more thing today, can you just make it so? And….
**Jacob Aronoff** 06:56 Yup.
**Antoine Toulme** 06:57 I'm hitting hard, real enterprise customers on OpenShift who have the Prometheus operator and say, why isn't it, like, this? And it's unfair because this operator is installed by default, managed by OpenShift. The whole thing is just, like.
Right, out of the box, they don't need to do anything, total upgrades, everything's just fine.
You just plug your finger in, it just works. And, like, why can't you be like them?
The… okay.
**Jacob Aronoff** 07:24 I mean, Bene had a proposal last year that I think he's been working on every now and then to enable it so that the OTIL operator is, like, another default that you could install as part of OpenShift.
**Antoine Toulme** 07:36 That'd be great.
I don't know where the project is there. Hey, Pavel, I don't know if you're….
**Jacob Aronoff** 07:40 If you're around. Maybe you know.
**ploffay** 07:43 Yeah, yeah, no.
**Jacob Aronoff** 07:44 Understood.
**ploffay** 07:45 That's not happening. Like, the car is not accepting any… Observability components as a default.
**Antoine Toulme** 07:53 It's a box.
I mean.
**ploffay** 07:56 There is Prometheus, there is… there are more plans to actually exclude the Prometheus from the core.
Okay. And to have only, sort of, data collection in the core. The Prometheus is their single reason that we sent telemetry data back to Railhead.
And they need some aggregation, …
If that was not the case, we… It has…
It would have been removed still a long time ago.
I would say.
**Antoine Toulme** 08:29 Very interesting.
**ploffay** 08:31 Yeah, so I think there are more plans to kind of decouple the data collection for metrics from storage, maybe via Prometheus Agent or hotel collector, but most likely Prometheus Agent.
Yeah, but no plans to have the auto collector as the, kind of, main collector on OpenShift. We would like to do so, but…
That doesn't seem to be an agreement in place.
**Antoine Toulme** 09:00 That's interesting.
**ploffay** 09:01 Boom.
**Antoine Toulme** 09:03 Yeah, so what's happening to me is that I have customers who say, because this comes bundled by default as part of the OpenShift experience, then my security team does not profit when they see that we're using Prometheus to observe.
When we bring up OpenTelemetry, then security kind of, you know, comes alive and starts to, like, okay, so what's in that stuff?
And they always find things to say about it, right? One way or another. Oh, you're connecting to this, you've got this spot going on, what is going on with this thing? And so it becomes an appeal battle that they cannot really win.
Obviously, having a certified option, like, by Red Hat, is a great way to kind of get more penetration into the upper chief ecosystem, and we really want to do that.
But the fact is that replaying second fiddle to promethis operator, which is installed by default, makes it, like, the second distant option in anyone's mind.
So, if we're… if we're on a level footing between the Prometheus operator approach and OpenTelemetry, then I think we can actually have a shot at, you know, convincing people that this is just as good, or just as potent…
Let's say, as much potential between those two.
You're first to see it.
**ploffay** 10:17 would you mind maybe opening a Jira ticket against our JIRA and, like, explaining these concerns? Or not to mention…
talk with Jamie.
**Antoine Toulme** 10:27 I need to talk to Jimmy more. I mean, these are recent discussions I'm having with customers, and these are, like, kind of coming to light from there. And these are, I think, good things to come. But, you know, the fix is also just a roadmap item for us. It's like, we need to work on that managed type operation, where
Or… the other thing our customers say is that Prometheus operator just works out the box. I don't need to set anything on that thing, right? It just works. It's not really true.
But…
They think so, because they forgot, like, what the setup was. This is how easy it is for them.
So, we need for the operator to have somewhat of a similar story, where it's, like, maybe one step and done.
And it would be…
This is why I want us to kind of work on this managed CR. We'll get there, I'm confident.
That continues to be a bit of a challenge. And it's cool to have, …
It's cool to be able to have an option where you dictate kind of the best practices to the customer, in a sense.
Because it would create two experiences in the operator, right? You want to understand what you're doing, you want to actually have an understanding of, like, how you deploy your target allocator, your population of that, how you're doing the HPA for your collectors, all those things, no problem, right? Go… go your own way, Lego… Lego pieces, you build your own thing.
We manage the upgrades for you, we manage the configuration breaking changes for you, we're here to help you.
But, if you're just looking to not know anything about what's happening on Dozier Hood, I will take the wheel, and we'll drive a couple miles with your car, and make sure that things work the first time when you set that up.
I will just apply best practices, and we can make a bunch of calls, like how we're going to scrape metrics, how often, what we're doing with that, what type of scaling we're going to apply, how we're going to kind of do this. We can make informed guesses.
biased on best practices that would also help us build a very potent
product experience that I think will win over people in OpenShift environments, especially when they're starting up.
So, I do need, …
a solution at some point for brownfield-type environments, so we've had recently a customer, this is really interesting, who was saying, okay, I don't want to… I don't want to pull the Prometheus operator. I'm too attached to it, it's been running for years, we're not going to take care of it, but I do want an OpenTemmetry backend.
But I'm not ready to just, like, scrape… I'm not going to rip out Prometheus Operator, knowing that I know exactly what performance I have with it, how much it's taking for me, and all that.
But the thing that's reading from those Prometheus nodes, we can change that. So I instructed them to use a target allocator helm chart.
And in just a set of collectors behind it that they are deploying, not as a daemon set, but as a set of deployments, right?
And it worked beautifully. It worked the first time, they were very happy with it. They managed to replace a bunch of fleet of Prometheus, kind of backends to solutions towards this open telemetry-centric view.
And it was a… it was a good success for them.
So this is what working the target locator helm chart is because I had an actual
Customer that was kind of pushing on that.
**ploffay** 13:46 Did they as well replace the in-cluster Prometheus, the platform Prometheus with Target Locator?
**Antoine Toulme** 13:55 No, they did not. They just used this to manage, like, all the service monitors and pod monitor adaptations that were already in their cluster. So this stuff is just not easy for them to move away from.
**ploffay** 14:10 Yep.
**Antoine Toulme** 14:11 So… Later.
**ploffay** 14:14 A good… good thing is that there is… there is the Prometheus remote write receiver now in the collector, in the awful state, so people can remote write from the in-cluster Prometheus into collector, in case they want to OTLP somewhere else, then….
**Antoine Toulme** 14:33 That's true.
**ploffay** 14:33 Like, before, there was no even way how to get those metrics out in a scalable way.
**Antoine Toulme** 14:39 I mean, I know that they're making their way through it, it's just Prometheus from Outright has a fraught history for me, so it's been interesting to see that they tried and tried and tried. It's been…
I think Prometheus is also kind of throwing the towel and saying, we're just going to go for TLP for some of our
traffic, right, at some point, because there's just too much. …
Yeah, eventually it would be really cool.
is… this is an extension of that scenario, is that they're currently still running Prometheus as a bunch of scrapers.
to do the actual non-monitor type jobs, right? And…
It would be kind of nice if we were able to just replace those and still have them
fulfill pod monitor, service monitor type annotations, so continue to kind of give them the impression that you're fulfilling the Prometheus operator job, but instead of using Prometheus tools, you could run a collector and see if you get better with that. This is… this is…
Probably just not that useful, but… …
There might be something there to explore.
Anyway, … Yeah.
So… Is there anything else that's happening?
**ploffay** 15:58 I think I wanted to talk with you, Antoine, about the… Work you are doing, ….
**Antoine Toulme** 16:05 Yes.
What do you wanna know?
**ploffay** 16:08 Yeah, everything. Okay, so… But I forgot… I forgot what it… what… what was the PR, ….
**Antoine Toulme** 16:16 Oh, you want the PR?
**ploffay** 16:17 Yeah.
**Antoine Toulme** 16:17 I opened the thing, so I opened this thing in, what, July?
**ploffay** 16:23 Yeah, I think it was something about… and maybe I'm totally off.
**Antoine Toulme** 16:27 that you want to… Yeah, it was about the operator config, like, you wanted to embed the instrumentation into the collector config.
To make it sort of like a default….
**ploffay** 16:41 Option, ….
**Antoine Toulme** 16:43 I mean….
**ploffay** 16:44 Absolutely.
**Antoine Toulme** 16:45 Yeah, go ahead.
**ploffay** 16:46 My understanding is that, yeah, you want to essentially embed the instrumentation CR into the operator config, so that users don't have to create instrumentation in the cluster.
**Antoine Toulme** 16:58 Dip.
**ploffay** 16:58 Just put the annotation, and then the operator would take the… the default from the operator config.
**Antoine Toulme** 17:05 That's right.
**ploffay** 17:06 Is that the case?
**Antoine Toulme** 17:08 It's, it's the most… it's best RD's view of that. Actually, what happens is that you just don't even read CRDs, because I didn't know… I didn't know how to make that work really well, so I just went for it, and just find a way to make it work. I didn't know how to marry between…
I don't want to have default config coming from config, plus I'd like to read the CR. It's too much work, so I picked one way or another. Now, why am I doing this? You might have seen that I pushed the target allocator helm chart, right?
Because I managed to kind of extract a slice of functionality from the operator and say, this is, like, interesting on its own. It could be useful at setup and shift, could be useful without custom resources. You could… you could deploy this as a piece of software, it would be good.
And as I mentioned, I was doing that for a particular real engagement where there was a real need for that, and it fulfilled a very good need. We also made that part of our Helm chart for our phone distribution, and the target allocator just works.
So that's kind of cool. And now I'm like, we're having to deploy CRDs with Helm, which is a pain. You don't have this problem with OpenShift that much, but Helm has given up on CRDs, they don't upgrade them, you install them once, there's no uninstalling them on this deletion of the chart.
And just, like, there's this… this thing that comes from a helm. It's like, we don't want to deal with CRDs, you're making our lives difficult. We don't like having this type of dynamic configuration in the first place.
And Kubernetes is supposed to be this declarative mode where you say what you're going to do, you deploy it as you said, and this is exactly what you're getting, right? So there's a little bit of this indirection that is involved with CRs there, kind of a philosophical argument about what to do.
So, what I wanted to do is, right now, in our Helm chart, for the vast majority of the customers that we have that don't actually have OpenShift, don't need any of that.
we don't want to install the CRDs if we can, right? So, I currently have a PR in my repository, where I'm like, can we try to disable
all the CRDs that are coming from the operator. This is why I have a PR open as of yesterday, because I tried that, and it blew in my face.
And I have also a PR open in the ARM charts to see if we can expose… Jacob just actually merged it, which exposes the Boolean flag that says, do not look for collective CRDs.
At the end of the day, my Helm chart should run without CRDs, because that's what people expect, actually, right? It's too weird to have CRDs.
So, that's one… one point.
**ploffay** 19:38 What is the… what is the use case for running without a CRDs? Is it for the inst… for the collector, it doesn't make sense, right?
**Antoine Toulme** 19:45 The collector itself is deployed as a daemon set with a config map that has its YAML.
So we, we….
**ploffay** 19:52 But for that, you don't need any operator, like, you can define.
**Antoine Toulme** 19:56 Oh, we need… so the only reason we have the operator in our Helm chart is because we want the automation. We want the webhook to do the injection of Java, Node.js, Python, things like that. And, we had to pull the whole subchart of the operator into our Helm chart.
to get that done, and that came with a bunch of strings attached. One of them was, oh, now you need to install 4 CRDs. Like, that's a bit heavy, guys, we just need that slice.
**ploffay** 20:19 Can we just… can we just get that, right? So, I think this is a way to get there.
**Antoine Toulme** 20:24 ….
**ploffay** 20:24 Makes sense, maybe, to… Have the operator binary run only the webhook?
**Antoine Toulme** 20:33 Yes, and to do that, if you look at the work I've done for the last 6 months, in the webhook, what I found repeatedly is, like, there were assumptions, like, this year is going to be available.
And I had to say, no, actually, you need to be able to bypass. If you see in your webhook that the…
target allocator CRD is not there. Do not crash, because I was getting hard exit once from the manager on startup, he would just assume things, right?
**ploffay** 20:59 Yeah, what I meant is, like, we could maybe… change the domain?
and allow only installing the webhook, for the instrumentation without other parts of the operator. Yeah. So, like, a subcommand or something like that.
**Antoine Toulme** 21:16 That could have worked, …
But even then, it still requires the implementation CRD, right? So, we would want to also remove that, if possible. Make that the.
**ploffay** 21:25 That would be… yeah, I think that would be an easier job to do, maybe, because it's gonna be just a smaller codebase to… to look at.
**Antoine Toulme** 21:34 But you still need to take the instrumentation config and make it, kind of…
decorated from the… from the… from the CRD. That's the problem.
**ploffay** 21:43 Yep.
**Antoine Toulme** 21:44 It's not the end of the world, but we're gonna have to do something. If we decide to have those type of complex use cases where we can decouple, you know, Helm, no CRDs, CRDs in that operator, then we.
**ploffay** 21:56 But, like.
**Antoine Toulme** 21:57 do that.
**ploffay** 21:58 it's a YAML, right, and we could maybe embed it in some….
**Antoine Toulme** 22:02 Yeah, but I think you're using some generator to be… like, I think what started is you did the CRD definition in YAML, right? Using the best practices from… I'm not too familiar with that.
**ploffay** 22:13 to build a room, or….
**Antoine Toulme** 22:15 And then KubeBuilder actually generates a YAML of, like, the actual Go code that goes for that definition.
**ploffay** 22:19 You should.
**Antoine Toulme** 22:20 So, if I take that code and move it elsewhere, then KubeBuilder
it's not going to be that useful for you anymore. And you're going to come to me and say, well, I'm trying to change the CRD,
I can't anymore because you move the code elsewhere, so KubeBuilder doesn't do its job, and then I'm in pain because I have to add fields myself. We'll figure it out, but it's not… it's not 1-1.
**ploffay** 22:43 Yeah, no, what I just meant, we have this config struct that you created, I think, for the operator.
**Antoine Toulme** 22:48 And there, like, embed the instrumentation CR directly.
It could, but there's a….
**ploffay** 22:54 You have a….
**Antoine Toulme** 22:55 You have a recursive, I would say, a cycle in imports, if you do that, because the… the webhook package…
involved itself into the config as well. So…
Yeah, I mean, we can find a way. We'll figure it out.
**ploffay** 23:12 We had the same issue in other projects, and we ended up moving webhooks somewhere else.
Yeah, right. I mean, you triangulate. Eventually, we need to separate the codes so much more so that we can….
**Antoine Toulme** 23:24 So, I'm not too worried about… the overall goal is this.
And then, the managed CR. So, the managed CR is supposed to be this overall, just one step. You install the operator, and the managed CR is, like, you know, as I put in your RFC, there's two settings on it, right? The endpoint in OTLP, and maybe a token or password you put on your headers.
Beautiful, right?
So… that CR is going to somehow, like, run around your cluster and, like, define collectors.
to do scraping, right? To actually do all the work of collecting the data, select the instrumentations that we want to have by default, make a bunch of, like, very opinionated choices about, do you want all your Java pods to be there?
And say, yes, we want to, and we're going to use the latest, and we're going to use the default instrumentation profile for that.
And so the question that I'm not asking you all yet is, is that CR going to deploy CRs?
Which is kind of odd.
Or is that CR going to make config files
That get ingested into the webhook when it deploys.
Which one is easier? Which one do you prefer? Which one is more consistent over time?
And I'm not….
**Jacob Aronoff** 24:38 So.
**Antoine Toulme** 24:39 the discussion, but yeah, cool.
**Jacob Aronoff** 24:40 Yeah, there are, like, two ways that… I mean, you brought up both of the approaches. The way that we did this with the target allocator was by making…
internally, we made the CRDs for that thing. So, like, the way that Nikolai did the migration was by…
… enabling the operator to create the target allocator CRD
When the user wanted a target allocator, such that they would actually see, like, a target allocator in their cluster.
Okay. I think that there's, like, pro-con for both approaches, you know? It's like, I think there's benefit, personally, to being able to see the, like, chain, and theoretically, as long as you're setting the owner references, there's, like, no.
**Antoine Toulme** 25:26 Hmm.
**Jacob Aronoff** 25:27 Difference?
Right?
So I think I would lean towards just make the high-level CRs in the cluster for people.
Because then you could access, like, the individual things, and we… but there is, like… I mean, it'd be pretty easy to short-circuit that, right? We would just call the manifest method.
**Antoine Toulme** 25:50 And you would be able to then… so let's… so let's walk through that line. So, let's say you have a managed CR that you deploy, and then it does its job, which is deploying additional CRs, right? And it says, instrumentation is going to look like this, right? Because I know better
This is what Java implementation looks like. And you don't like that, or you want to have one more resource attribute on your Java pods.
**Jacob Aronoff** 26:10 Can you patch?
I actually just, realized why we need to do it.
where we create the CRDs, it's for… we would have to change a lot of other references for things. So, when you're doing the instrumentation work.
And you see an annotation on the pod, we do a lookup for the instrumentation resource.
And so, if…
we don't have that resource there, it'll just fail. So instrumentation wouldn't work. So you do need to make the instrumentation resources.
**Antoine Toulme** 26:43 Yeah, I mean, I… my PR is in the middle of that instrumentation code, making all sorts of calls about, hey, are you looking for the instrumentation CR or not? And I have this big if, this big ugly if in the middle, it's like, actually, no, don't do that, just read the config.
**Jacob Aronoff** 26:59 Oh, I….
**Antoine Toulme** 27:00 That's disgusting.
I mean, and what I like about the approach, if we do generation of CRs from a CR, is that we can do it now. We can actually parallelize the work between me doing games with my Hamchart-up approach, where I want to decouple stuff.
**Jacob Aronoff** 27:16 And we can still get the CR faster, because….
**Antoine Toulme** 27:19 We want to get to somewhere faster on that. So….
**ploffay** 27:22 I think that makes more sense, because there's already a lot of code that will make sure the…
the CR deploys the correct instance, like, handles upgrades, makes sure that the ports are exposed correctly, and things like that, so…
It's probably better to just create another abstraction that will use the building blocks that we already have in place.
**Antoine Toulme** 27:43 Okay, so specifically in the OpenShift space, you would be then able to do the upgrades and the unattended upgrades of this type of stuff, right? Like, collector upgrades, stuff like that.
Well, okay, I'm okay with that. In that case.
So we would be dictating a lot of things from that CR, such as, you know, what is a best practice type collector looking like in an Apache cluster, right? What does it have on by default?
Does it do cluster receiver? Does it go to kubelet stats? Does it have opinions about what's running around?
So, that could be more of a discussion that we can have moving forward about, like, the design. And I think we can go into more, like, discussing actual code changes on that.
So we can discuss, kind of, this, and I want us to take the time to just go through the development of this. This is not, … we cannot watch this, but…
There's a lot of expertise that will come out of What we want to see.
ideally, from an OpenShift cluster.
where we want to be able to kind of see what's going on. There's instrumentations in one play, but really, the collector itself, like, we have, you know, Helm chart, we have 700-odd lines of YAML in the config.
It's a lot of backward things and a lot of functionality that… I don't know if you want to bring all of that.
One of the biggest issues I've had is, we currently mount the node volumes for the daemon set to read the loads.
do you have that support? Because one of the biggest problems we're having with OpenShift folks is
They're telling us that our cluster is locked down, you're trying to do something on the node, accessing either the network host, the network mode of a host, or even connecting to, you know, mounting a folder is frowned upon.
meaningfully.
Right?
**Jacob Aronoff** 29:35 Yeah, good.
**Antoine Toulme** 29:36 Then how do you get the… how do you get the logs?
Oh, well, we have an Apunch-specific solution that can, kind of, out of band, does something else, and…
So, anyway, ….
**Jacob Aronoff** 29:51 Yeah, no, I… these are all annoyances. I mean, I remember dealing with them at my last job, and it was… it sucks. They're not fun.
It's just coordination. It's not enjoyable.
**Antoine Toulme** 30:03 the thing I was looking at is, like, there's ways, like, you can tell OpenShift, hey, make that particular volume or container available or different.
But you have to run, like, this snippet of a bunch of specific things that says, this is now executing in a highly privileged environment in its own thing.
And I wonder if that passes master when it comes to certification, or when it comes to… because I think the performance operator gets, again, gets away with a bunch of stuff, because it's installed by default.
So they have maybe more access?
Then, let's say the collector would….
**Jacob Aronoff** 30:37 Yeah.
**Antoine Toulme** 30:38 And I'm worried about that, because we… again, we can't compare in that case.
**Jacob Aronoff** 30:44 Yeah, I mean, they're certainly doing extra stuff. I mean, I think that we try to get around some of this with our custom bundle that we do. Like, there is some OpenShift-specific stuff in that bundle.
That's probably where we would need to put that type of logic, realistically.
**Antoine Toulme** 31:01 Yeah.
Okay, not in the CR, in the bundle. Okay, that makes sense.
**Jacob Aronoff** 31:07 Yeah, just because then it's, like, OpenShift… we used to put a lot of it in…
the operator, I think, and there's probably still some relics of that, but, …
I think that we moved to a bundle approach, so that we don't have as much OpenShift-specific stuff. No, am I wrong on that? Do we still have the OpenShift-specific stuff? Oh yeah, we do, we have the route stuff, yeah.
**ploffay** 31:30 Yeah, the bundle controls, just the installation of the operator.
So, what we do, we enable, like, we say, we have OpenShift bundle, where we enable, like, let's say the routes, or we enable some OpenShift-specific functionality, like creating the dashboards for the serve, for the collector.
But then, if we need to fix any additional permissions that OpenShift requires, we need to probably make the change in the operator itself when it's creating the objects that need the permission.
**Jacob Aronoff** 32:02 Oh, I thought that we would change that in the bundle on install, when you're like, oh, we need these extra permissions to do these operations.
**ploffay** 32:10 Yeah, you need to give it an RPAC, but then you need to as well maybe do something on the objects itself.
**Jacob Aronoff** 32:15 I see.
Yeah, so it's kind of a two-pronged, two-place thing. I see.
I'm not familiar enough with OpenShift, so I'm not claiming expertise here.
**ploffay** 32:27 To be It's just… It's annoying, the old shirts.
**Jacob Aronoff** 32:35 Yeah, it seems constrained. There's a lot of constraints in that environment, for sure.
**ploffay** 32:39 Like, it totally sucks that you get… you take, like, Kubernetes…
Helm or app that you deployed in OpenShield doesn't work. It's….
**Antoine Toulme** 32:48 Yeah.
It's a problem.
**Jacob Aronoff** 32:52 Yeah, my girlfriend works on OpenShift a lot, and occasionally these things will pop up, and she'll ask me for help, and I'm like…
Is it a Kubernetes problem, or is it an OpenShift problem? And if it's an OpenShift problem, then I have to say I don't know what is going on.
Like, she was dealing with, like, a cross-cluster…
routing issue, which was, like, not a thing that I knew
what the OpenShift language of this was.
… So, I was no help.
**Antoine Toulme** 33:24 I was teed to ask you a question, if possible, going off completely here, but just, I'm gonna share my screen for a sec.
…
So, I noticed something in the, in the code. The code itself, is the, the, like, the tiny point,
Need to allow that.
Let me know if you can see it. So I'm in GitHub, right? I'm in the documentator, go in this presentation.
We've had reports from customers that the mutation can actually overwhelm the
the community's client, right, the actual API server. What we found is…
I'm not sure exactly why we're doing this.
On every instrumentation, but we do list
And some mutations in the background namespace.
That is expensive.
Yeah.
**Jacob Aronoff** 34:16 Yeah, so, there are two… there are actually two problems here. One of them is this, that we do this list.
**Antoine Toulme** 34:23 And then there's a dip somewhere, right?
**Jacob Aronoff** 34:25 But the other one is the… is the webhook itself.
Yeah, that one. Well, sorry, that's the other one. There's 3 issues. That's the one that I thought you pointed to initially. That's the more problematic one, is doing that GET. And when I was doing some research earlier on, I actually don't think we need to do this anymore. We did that get before there was…
as much information in the downward API as you can get now.
You can actually access the fields that you need to without doing the call now, I think.
**Antoine Toulme** 34:58 Let's see.
That explains why that happened in the past. Okay.
**Jacob Aronoff** 35:03 But so that's part of it, though. That's not the entire issue. The other issue is that we call the webhook on every pod.
**Antoine Toulme** 35:10 Yes, that's right.
**Jacob Aronoff** 35:11 And that's what gets really expensive, is even if we, like, immediately reject it, we do have to… we check every single pod.
Which….
**Antoine Toulme** 35:20 Okay, right, so that's true.
**Jacob Aronoff** 35:22 huge problem.
That's also why, like, you want to do the label thing, because you can't do a webhook on an annotation selector. It's just, they don't allow that.
**Antoine Toulme** 35:33 Yeah, no, we had heard that discussion before.
But….
**ploffay** 35:37 Well, we're listing the instrumentation because…
If the value is true, we need to make sure there is only a single instrumentation in the namespace.
**Antoine Toulme** 35:50 Oh, but… so, could you, … I talked about it with my Kubernetes expert, she mentioned that
there used to be a way… there would be a way to use informers to create a cache of what's being deployed in terms of CRDs, with a, you know, initial spin-up where you read the state of things, and then you get informed whenever CR changes. And then, based off that, you can create your internal memory cache of what the space looks like.
And you could then, instead of having to call constantly, just keep up with that, and it will be cheaper, because you're… pretty much, you need to spare the Kubernetes API server as much as possible in that situation.
No, the type of spin-ups I'm talking about is, like, 2,000 instances in the next second that are just queued up for creation. So even what Jacob's mentioning could be potentially fatal, but this probably adds to the injury, right? Because those 2,000 pods want to be instrumented.
and… and then they don't get skipped on, then they go and each one of them is going to do a list, and each one of them is going to do a GET. You can actually probably crush your API server if you play that.
So… Aye.
**ploffay** 36:58 I think this client should be picked by the cache, so maybe if we initialize the cache properly at the control startup.
It should solve the problem.
**Antoine Toulme** 37:08 Yeah, are you folks working on that? Is there an issue about this, or is it something I can open?
**Jacob Aronoff** 37:14 There's definitely an issue on it. It's an old webhook thing.
That somebody opened up. Let me see if I can find it really fast for you.
I started on this when I was doing the instrumentation code refactor, but I never got to finish that work.
… I mean, the code is super hairy. It's, like, really hairy. We do have a cache already.
that we use. … I don't know if we're caching the right stuff in there.
Maybe a more important problem.
**Antoine Toulme** 37:46 The code is not fun. I would agree with that. Something has happened with that code that's, like, it's been tortured too many times, and it could use some love.
There's this… there's this, temptation to make it generic, or something like that, that seems to have, kind of.
not paid forward, and I can see how, …
I would need to look at the code coverage before I rumble in there like a bull in a china shop, but this is probably…
at least something that we could try to simplify. I mean…
It's not the end of the world, it's… It will work. ….
**Jacob Aronoff** 38:24 Yeah. I just sent you the issue, by the way, the older issue. …
It does talk about the exact thing that you were talking about, about too many pods overwhelming the operator, and then the API server.
….
**Antoine Toulme** 38:38 Excuse me.
**Jacob Aronoff** 38:39 there's not a ton of detail in there, and I don't even think I linked my PR to it.
**Antoine Toulme** 38:42 Yeah, that's… that guy's… that's the… that's our tester.
**Jacob Aronoff** 38:47 Yeah.
**Antoine Toulme** 38:48 The word is round, we just… yes.
**Jacob Aronoff** 38:52 But yeah, I mean, if you wanted to, like, work on that instrumentation code, power to you, but also, that's why I wanted to just rewrite it, and then delete the old stuff, because…
I think that the current mode is, like, so confusing, and I tried to, like, get the logic to be generic enough. Actually, I think I have that PR somewhere.
Let me see if I can find that.
**Antoine Toulme** 39:14 I see how it could be… yeah.
The complexity of the code increase every time you add, like, Ruby, right? It's like, oh my god, no, it's like 50 lines more of stuff that I have to think about, or….
**Jacob Aronoff** 39:26 Yeah, let me see if I can find this one. Oh yeah, here it is, instrumentation refactor.
Here, I'll share my screen real fast, and I can show you what I was trying to do.
**Antoine Toulme** 39:38 Sure.
**Jacob Aronoff** 39:38 …
So…
I split this up into, like, a V2 package, so the code would be a little bit easier to read on…
Nice. First time, so I made a bunch of helpers. One of the things that we also do that's really
really expensive, is that we do a lot of this, like, get index of env stuff.
Where we just do, like, a linear search.
Of…
an environment variable, and we do this, like, constantly. So, instead of that, let me collapse these for a second.
…
So instead of that, what I do is I just create a map of environment variable to index, and then use that, which is a little bit better. But then we have to do this triple thing, which is very annoying, because we're passing around a lot of stuff. But the idea here is this. You have a mutate thing.
We check if it's already instrumented. If it is, we find out what instrumentation should be used, get the container names, check for multi-instrumentation, and then do injection.
And then we need a list of tuples for each of these things, and so then we go into the actual injection. So, the triple that we have is the container index that we're trying to instrument, the instrumentation object that we're creating, and then the language that we're trying to instrument.
So we iterate through all of our languages, which is a map, that's passed in
To the mutator constructor.
**Antoine Toulme** 41:11 Yep.
**Jacob Aronoff** 41:11 And then we…
this is the generic part that I was able to, you know, sort of short-circuit there. We check for what instrumentation instance to get, we get the container names, and then we append to our triple list.
And then for each of our triples, we then go through, and then we call the languages from the language map to inject the pod itself. So, in that way, it's, like, a lot simpler, right? Like, this is a pretty clean function, I would say, overall.
**Antoine Toulme** 41:41 Yeah, it can grow without complexity, yes.
**Jacob Aronoff** 41:44 Yeah, so… but that's not really the hard part, right? The last part, which I didn't really get to, was trying to get
This is all the, like, this, and then it's where all of this logic that gets really fucked up. Setting common environment variables, checking for stuff.
Constantly getting, like, the right environment variables to put in the right place, figuring out the propagators, getting the container names, like, all of that stuff is really expensive.
You'll see that I did get rid of that .get… oh, I thought I got rid of it. No, this is getting the instrumentation. But, we still have to get the instrumentation instance, we could probably use a cache for that, but I got rid of the client get call for the metadata.
**Antoine Toulme** 42:27 Okay.
**Jacob Aronoff** 42:28 ….
**Antoine Toulme** 42:29 This is good, there's… I see how there's simple refactoring that we could… like, we could take a slice of your PR and just land it first, like renaming the… I think you rename a type first.
Then do just the refactor.
And just… let's go from… in small iterations on it, so we can keep the plot, right? Because….
**Jacob Aronoff** 42:48 Yeah, I mean, I did it this way because I mostly wanted to see if it could be done, like, I wanted to take it…
Because I was trying to piecemeal it initially, and I had a few prior attempts trying to piecemeal, and it just was, like, not fitting into the model that I wanted.
**Antoine Toulme** 43:05 Yeah, that's annoying, yeah.
**Jacob Aronoff** 43:06 Which really sucks, and so when that happens, I usually just, like.
cordon off the package, and see if I could get it to be the same, like, in and out, where we have plenty of tests for the outside, and then ideally you just swap the path.
**Antoine Toulme** 43:22 I mean, all the work that I've done on the operator when I had, like, those 6 PRs were just one huge spike one day. Yeah. And I figured there was no way in hell I was going to be able to explain that over the internet to anyone, so I took.
**Jacob Aronoff** 43:35 Good luck.
**Antoine Toulme** 43:36 A hundred lines of it at a time, so they could…
have a potential, like, even ability to even, like, work through it, and it was great, because it invited more feedback, it made it better, and…
I completely understand, like, this is great. I'm gonna… I'm gonna work with that. Thank you.
**Jacob Aronoff** 43:54 I'll send this to you as well. I'll put it in here. Yeah, check it out. I mean, you'll see where I stopped. It's pretty clear that I didn't do it.
…
But I think one of the things that's, like, the easy wins is just building the reverse index for the map.
It was, like, such an easy win. Yeah.
Let's do that. We do that constantly right now, and it frustrates the hell out of me.
**Antoine Toulme** 44:20 Yeah.
Let's do simple wins like that to kind of get 10% better here and there.
And then, …
These are good improvements that can help also, and I think it also will help because it would provide more… the simpler the code, the better it is to bring more people to maintain it, right? Yeah.
**Jacob Aronoff** 44:38 Yeah, the hard stuff… I think a good place to… the most difficult place, but also the best place to start, is figuring out, like.
Environment variables that we set, and, like, Figuring out how to decide The precedence of stuff.
is, like, a very fraught path that I don't like to touch.
You'll also see here that I…
brought out the, like, default things. Actually, let me find…
the exact… can I split window in this? What?
No, I can't. That's annoying.
I'm on a new browser, and so I'm, like, trying to learn what I can about it.
But let me see if I can find that.
I just want to understand the client go that I got rid of.
Where's the .got?
Prop 1.
pod mutator… Not that one.
Where was it? Where's that code that you, like, just linked?
**Antoine Toulme** 45:46 … podminturu.go, line… It's a long… it's a long class, ….
**Jacob Aronoff** 45:56 So it's not the instrumentation. I, I, there is a gap for the meta beta. Where is that?
**Antoine Toulme** 46:02 Get a supplementation instance, select a supplementation instance from namespace.
**Jacob Aronoff** 46:07 Oh, it's in here. It's the… it's this right here.
The, add parent resource labels.
….
**Antoine Toulme** 46:14 Wow, that must be bad.
**Jacob Aronoff** 46:16 Yeah, I think I just got rid of this. I think that I looked at this, and I was like, we're actually not getting any value from this, and all of it can just come from the, downstream stuff, was the decision that I had made.
**Antoine Toulme** 46:30 But is that something that we should do? Or….
**Jacob Aronoff** 46:33 I think so. I don't think that… I actually don't even think that these labels appear as of today.
**Antoine Toulme** 46:38 Whoa.
**Jacob Aronoff** 46:39 ….
**Antoine Toulme** 46:40 Okay.
**Jacob Aronoff** 46:40 And this is so expensive. I mean, you can see how expensive this is. It's like….
**Antoine Toulme** 46:45 I mean….
**Jacob Aronoff** 46:46 Word.
**Antoine Toulme** 46:47 I had no idea this was even there.
**Jacob Aronoff** 46:49 Yeah, so, like, you'll see what we do is we say, if it's… oh, yeah, yeah, this is the thing. It's, if we are in a replica set, so if it's, you know, a deployment, thing, then we're going to do a full get on the replica set.
To get the deployment, just so we could add the deployment name.
which feels so futile. It's like, why are we doing that, you know? And so, if we look here.
Where did I do this?
**Antoine Toulme** 47:22 Just gonna be late.
**Jacob Aronoff** 47:23 It might be in Helpers… resource?
Yeah, I think I just did it here.
Whereas just, like, we don't… we just get the things that we say we need to do.
And then I think I just didn't even do the owner resources, because I don't think that they're valuable.
**Antoine Toulme** 47:43 That's a very good point. I don't know that we recommend that to anyone these days.
**Jacob Aronoff** 47:48 No, I don't think so, and I also think that's what the, … what's it called? The, …
host environment detect… the, like, detectors on the views do now, right?
**Antoine Toulme** 48:02 Oh, no.
**Jacob Aronoff** 48:03 Can't you specify detectors in the OTelconfig format?
**ploffay** 48:07 There is Kubernetes Attribute Processor? That's what you mean?
**Jacob Aronoff** 48:11 No, but that's the, that's the attributes for internal… for the telemetry being sent to the collector. These are attributes for the collector itself.
… I'm trying to find….
**ploffay** 48:27 Antoine, you mentioned you don't recommend setting, like, deployment name?
**Antoine Toulme** 48:32 No, I think I did that, but I am a bit… lost.
No, it's just, like, we don't really talk about it at all in our deployments, …
when we say deployment, I need to look into that. This is, I know we said environment name.
No, I'm confused, so I'm not used here. This is taking me by surprise a little bit. I did not see that in my view of the code, and now I'm…
Unclear.
**Jacob Aronoff** 49:01 Yeah, no, it's spooky stuff. It's not…
I think there are detectors in here, right? Oh, they haven't added that yet.
**Antoine Toulme** 49:09 There might be some work there, because it takes a while to learn this type of stuff. Are you sharing still?
**Jacob Aronoff** 49:15 Yeah, I don't see it here. Maybe it's an OTEL Go…
Didn't merges in here yet, or is it in Contrib? I think it might be in Contrib.
**Antoine Toulme** 49:27 Are you talking about the resource detection processor?
**Jacob Aronoff** 49:30 No, not the resource, the, OTELConf file that they use now.
**ploffay** 49:38 Yeah, for the insta… for the….
**Antoine Toulme** 49:40 Oh… The actual, like, declarative config thing that we… We can do them?
**Jacob Aronoff** 49:47 Oh yeah, they have detectors, yeah, so this… you could actually just do it with detectors. You don't need to…
….
**Antoine Toulme** 49:53 Nice.
**Jacob Aronoff** 49:54 So I don't think we need to set that anymore.
I mean, I don't know what detectors are available to you here, but if they have a Kubernetes one, or even, like, a GCP one, that should be okay.
**Antoine Toulme** 50:08 There might be something to add.
It's interesting.
**Jacob Aronoff** 50:12 Yeah, I just don't know if it's valuable to do that get. Like, I don't think that that's a worthwhile endeavor, and I would just get rid of it, and use what you can get.
**ploffay** 50:22 Could we get the deployment name through, like, Downward API? Probably no, right?
**Jacob Aronoff** 50:28 Oh, and wait, actually, sorry, this is the… these are the resource attributes for the pods that we're injecting, that we're doing the calls for, so it's even more expensive than I thought.
And…
also not valuable. I… I think that those are not super useful, and you should just be able to get them from the Downward API, if somebody really wants them.
**ploffay** 50:50 Yeah, if it works through the onboard API, it would be awesome, like, we could inject new environment variable and reference it in the resource attribute environment variable.
I'm not sure if you can get the deployment name, I don't think you can literally….
**Jacob Aronoff** 51:05 town, we're, …
Let's see…
metadata….
**Antoine Toulme** 51:21 I want to catch the end of a jazzy, because I put a bomb in their agenda, but…
I'm… I'm gonna… sorry, folks. But this is a really… No, it's all good. I will try to catch up on that and follow up on those issues for the operator. The resource labels thing is…
A little daunting, but maybe there's some simple fixes that we can do.
I appreciate the time.
**Jacob Aronoff** 51:44 Good chatting. See ya.
Chloe, anything?
**ploffay** 51:50 Nope.
**Jacob Aronoff** 51:51 No, okay.
Zeo.
**ploffay** 51:55 Yeah, you too. Thank you, bye.
