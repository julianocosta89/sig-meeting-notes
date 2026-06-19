SIG: Kubernetes Operator SIG
Date: 2026-06-18
Duration: 66 minutes
============================================================

## Zoom Recording Transcript

Mikołaj Świątek 00:00:28 I can't hear you, but I…
Benedikt Bongartz 00:00:31 you're here.
Mikołaj Świątek 00:00:32 I am. What's… what's so surprising about that?
Is it surprising?
Benedikt Bongartz 00:00:44 Kind of.
jea 00:00:45 Yo.
Benedikt Bongartz 00:00:48 Boom.
Mikołaj Świątek 00:00:58 I should wait, wait for a few moments.
Let's see who else arrives.
Are you really copy-pasting your own name from the previous meeting?
jea 00:01:13 No, I did that.
Mikołaj Świątek 00:01:16 Are you copying Bene's name from the previous.
jea 00:01:18 Yeah, I'm putting it there.
Mikołaj Świątek 00:01:21 Wow. Wow.
Benedikt Bongartz 00:01:23 I was going to say that my browser is still loading the document, so…
Mikołaj Świątek 00:01:30 What do you… how do you know he wants to be, you know, on the record as being here? You know?
jea 00:01:36 You're so right, I'll remove it now.
Benedikt Bongartz 00:01:40 How can you know my company? Maybe I switched in the meantime.
Mikołaj Świątek 00:01:43 Yeah.
jea 00:01:43 A lot of people have switched companies in the past couple of, like, weeks. Tyler is at Grafana now, My old colleague Matt Weir from LightStep is at Dash Zero now.
And I think.
Mikołaj Świątek 00:01:58 Or, oh, Matt.
jea 00:01:59 Yeah, because that's…
Mikołaj Świątek 00:02:00 Mattis does zero, maybe he's gonna continue his work in, like, auto-collector status stuff.
jea 00:02:07 I would like that.
Benedikt Bongartz 00:02:09 I think he's maintaining…
jea 00:02:11 I think he's gonna do Python and Ruby instrumentation, though.
Didn't.
Benedikt Bongartz 00:02:16 Half Elastic quit their job recently?
Mikołaj Świątek 00:02:19 Really?
Benedikt Bongartz 00:02:22 I just saw on LinkedIn some folks, like, goodbye.
Mikołaj Świątek 00:02:27 Those are all executives.
It doesn't really matter.
jea 00:02:30 Goodbye, executives.
Benedikt Bongartz 00:02:33 It makes it just…
Mikołaj Świątek 00:02:34 I guess one person in there who was actually an auto-contributor was Alex Ward, who was, like, a SEMCOM.
Maintainer, I wanna say?
That's quite sad, but I think he's gonna stay as an commenter, so… No.
Benedikt Bongartz 00:02:49 I go to some other vendor, and they just…
Mikołaj Świątek 00:02:52 I have no idea, I have no idea how often are going.
You notice…
Benedikt Bongartz 00:03:02 Weird parties that people play on, On weddings, where you have the chairs in the middle, and then they just… Run around, and… You exchange it?
jea 00:03:15 Yeah.
Musical chairs?
Benedikt Bongartz 00:03:19 I don't want to know the German names.
jea 00:03:21 Okay.
Benedikt Bongartz 00:03:22 I'm sometimes surprised when there is this time, somehow all these companies start hiring, and then everyone is turning around and… This happens every 2 to 3 years.
Mikołaj Świątek 00:03:33 I know.
Benedikt Bongartz 00:03:33 No logic, they leave, and…
Mikołaj Świątek 00:03:36 You know what, you know what, kind of…
jea 00:03:41 Why is it called this in German? Is this what it's called in German?
Benedikt Bongartz 00:03:47 Yes.
jea 00:03:48 Why?
It doesn't make any sense.
Mikołaj Świątek 00:03:55 Remember, Ben, a common wisdom says that the main way you can increase your compensation is by moving.
There you go.
jea 00:04:03 Bye.
Benedikt Bongartz 00:04:04 I move a lot.
jea 00:04:05 Why…
Benedikt Bongartz 00:04:06 5 kilometers a day, but… Nobody pays me for it.
Mikołaj Świątek 00:04:11 Is that a lot?
Benedikt Bongartz 00:04:13 No.
Mikołaj Świątek 00:04:20 I'm sorry if I'm a little bit loopy, by the way, I recently got one of my teeth removed, and I'm on pain medication, so… I'm a little.
Benedikt Bongartz 00:04:32 So you…
Mikołaj Świątek 00:04:32 Hmm, yeah.
Benedikt Bongartz 00:04:34 You went to a football game and you said you were a loser, or…
Mikołaj Świątek 00:04:39 I actually… if I actually did that and started airing my opinions, I might, that might actually happen, but no, this was a professional doing this. Not unrelated, unrelated to football.
Slash soccer, for those of us of different, you know, cultural spheres.
Probably there?
Pavol Loffay 00:05:04 If I'm here, yeah.
Yeah, hi everyone.
Mikołaj Świątek 00:05:11 I think we can get started. Right now, we only have two topics in the agenda which are mine, but since we're only all maintainers here, I might also add a secret topic, which just has to do with the security advisory that we have open for way too long.
But… Let's get… Let's… let's get… let's do this stuff first. I'm actually gonna try sharing my screen.
Zoom on Linux is a shockingly unusable application.
It's actually quite amazing.
How unusable it is.
Okay, there it goes.
I mean, you see this?
Alright, so… First thing.
I have an RFC for a documentation rework. Some of you have already reviewed, I'm putting it up there in case.
you haven't seen it, you're not aware of it, or if there's something you'd like to discuss. This is pretty short, and it's not… I don't think it's, like, especially… controversial in its aims. It basically wants to take the existing content, restructure it, add some content that we're missing, and also maybe introduce some automation, auto-generation for stuff like feature flags, command line flags, maybe for telemetry, and such. So… and you can see there's a link here somewhere.
Which defines… I have a link here for how this might actually look.
Somewhere.
Where is it?
Here.
We can actually go here, and go to… The actual branch, and… can see, in a practical sense, how the documentation works. So there's a README, And it has… it's divided into these sections, and then… I think you can click around and see how it goes. Basically, there's, like, a tree here in… In docs, and… there's, rEADMEs at every level, so it's, like, reasonable.
reasonable navigation, or as reasonable as you can do in GitHub. And this, like, this phase basically doesn't add any content, so it's, like, oh, most of these are pretty small, because it's basically our current lead-need re-partitioned.
In this way.
But I still think it's, like, a pretty much… it's a pretty significant improvement, and once it's up there, you can also, kind of imagine what else we might add to it, because this has, like.
things which we have planned, and which we have had planned for a while. So, for example, things… so, for example, Reference architectures, which you wanted to add.
There's, like, a security section, which we don't have and really should have, and so on.
Any questions about this?
Pavol Loffay 00:08:44 I have a question, because there is as well documentation on the OpenTelemetry website, And… I wonder… how we could maybe streamline the website and the docs that we will host in the repo. Or, like, if there's other projects that kind of thought about this and… And make it work.
Mikołaj Świątek 00:09:10 I very explicitly don't have that in my scope.
Benedikt Bongartz 00:09:14 I think…
Mikołaj Świątek 00:09:14 Because…
Benedikt Bongartz 00:09:15 discussed this at KubeCon, two, three years ago, and the approach we wanted to have was a GitHub action which can create a pull request on a docs repo based on our docs, and we wanted to discuss this once we restructured our docs.
This is what I…
Mikołaj Świątek 00:09:31 They're here.
This is what I… this is my idea here. I want… first, I don't want to make this a really big project that's just going to get bogged down in, like, questions about what should go here, and what should go there, and how it should be structured in total. I want to make good documentation in GitHub, or at least better than what we have right now, and, like, reasonably navigable. And after this is done, and it also has the content that it needs, because right now we are missing some stuff that we should add.
Then we can kind of open a separate thing where we're gonna ask.
what should be the relationship with OpenTelemetry I.O, right? How… which… what should live here? What should live here? Is it okay if there's duplication? I think it's okay that there's duplication, but I also kind of want to pull in someone from the docs maintainers to tell us How… how they'd like it to be done, and how they do it for other projects.
as well.
I, I am…
Pavol Loffay 00:10:28 That's fine, I mean, I like that we will improve it here first, and then… Kind of figure out other distribution channels.
Mikołaj Świątek 00:10:36 That's the idea.
I don't know, like, I can… I feel like when it comes to OpenTremetry I.O, I can be convinced to do all sorts of stuff, and feel like I have very strong opinions about where… what should live.
I just want to do it in a way where it's going to be not really annoying to update, and that we, like, can reasonably update around the, you know.
So it's not like… so there's a single source of truth for most things, or at least there is a canonical source of truth for a given piece of information.
But anyway, check it out. I think what's in there is, again, not very controversial.
The other thing I had was just… this.
This is really stupid.
Because I'm really annoyed about… Flaky multi-instrumentation end-to-end tests.
And I have debugged it, and the reason those are flaky is actually really simple and really annoying. It's the fact that those tests go like this. Create instrumentation, create instrumented pod.
Go.
And the problem is, if the instrumentation… if the instrumentation you created is not yet in the operator's cache.
then you get nothing, and the test fails. And there's no way to… no way to wait for this, in general.
So, what this change does, is just put SLEEP1 everywhere.
And this fixes it incredibly consistently. I have not managed to make this fail, and I ran, like, many loops of riffing.
In the future.
What I would like to do, I think, because this is useful anyway, in my opinion, is to do something like just emit an info log whenever there's a change to an instrumentation CR.
Because that doesn't happen very often, and it's useful to know when the operator sees it.
And then just use that in tests.
Whether it happened. But that's, like, more work, and this is really simple, even though it's very stupid.
And the reason you can't do, like, kind of… You can't go off of stuff like observed status, or some… or generation, or similar things, is that the webhook might be in a separate binary than the operator, and there might be, like, multiple replicas of the webhook server.
So you don't really know where your request is gonna go.
In order to actually, like, check this, you would have to, like, poll all of them somehow.
And, like, this is a problem for end-to-end tests, but it's not a problem in, like, normal execution.
Like, normally…
jea 00:13:30 Yeah, that's…
Mikołaj Świątek 00:13:31 And, you know, sorry.
jea 00:13:32 That was my next, questions, like, can we just use, Like, status or something?
Mikołaj Świątek 00:13:39 Because status is on the CRD, so it's a single thing, but the fact that it's in there doesn't actually guarantee you anything.
Pavol Loffay 00:13:48 We could not, like, we could pull… like, the operator could put something on the status that it has seen the object.
Mikołaj Świątek 00:13:55 I mean, but what does it mean that the operator's in the object? The manager and the webhook server might be different binaries, and there might be multiple replicates. You don't know which of them your, you know, your webhook, your mutating webhook request is going to go to.
Like, they might have different, they might be caught up to a different point.
At any given month in time.
So this would, like… fix the pests, But it wouldn't actually… Like, guarantee anything.
In a general sense. And I don't think this is actually a problem in production.
Honestly. Like, this is… Kubernetes is a… distributed system. It is eventually consistent, so if you make a change to an instrumentation and start creating a bunch of pods, some of them might not see that change.
That's just life.
Pavol Loffay 00:14:53 Yeah, we have users complaining about that. They want to be sure That instrumentation is always injected.
Mikołaj Świątek 00:15:05 There is one solution to this. Use an uncached, you know, uncached client, but then you're… significant performance.
Pavol Loffay 00:15:17 Yeah, I think there's maybe as well, like.
Change the policy on the webhook that it will block the web creation until it's up.
the…
Mikołaj Świątek 00:15:27 I mean, the problem isn't that the webhook is up or not, the problem is that… the webhook is there, and it runs, but you tell it to give you instrumentation X, And it's not that.
Pavol Loffay 00:15:42 Have you checked this one, actually? Like, did you check the logs? Like, maybe…
Mikołaj Świątek 00:15:47 Yes.
Pavol Loffay 00:15:48 Yep.
Mikołaj Świątek 00:15:49 Yes. What happens is that it just doesn't see it.
And you don't really know, unless you use, like, a synchronous client, and actually do a request to an API server.
You have no idea whether this doesn't exist because it doesn't exist, or whether it doesn't exist because… Because you haven't gotten the update over the watch yet.
And more importantly, more importantly, you have no idea whether the version that you get is the latest version.
Pavol Loffay 00:16:21 Yeah, I think this is fine. We could as well do, like, a restart of the pod, and check, like, two times if it's injected or not, but I think this is… If this works, let's go with one second.
Mikołaj Świątek 00:16:35 I mean, there's just.
Pavol Loffay 00:16:35 Thank you.
Mikołaj Świątek 00:16:36 tests.
Pavol Loffay 00:16:37 took the.
Mikołaj Świątek 00:16:37 tests, right? If there's a problem that users have, that's a different conversation.
Yeah.
Pavol Loffay 00:16:43 I'm working on the double split. I ran into a bunch of issues, but I hope to finish it probably… Next week, or the week after.
I was doing some internal stuff, but yeah, I want to split the webhook, and I was trying to make the… The failed policy is well configurable.
Mikołaj Świątek 00:17:07 It is configurable, like, we just ship a manifest, anybody can change it to whatever they want.
Pavol Loffay 00:17:13 Yeah, I think the biggest, kind of, issue I see with… configuring these things is, like, the OLM distribution. Like, with OLM, you can't change these things easily.
Benedikt Bongartz 00:17:27 With OLM, we can set environment variables for the operator.
So if… we can't…
Pavol Loffay 00:17:35 Yeah, but then the operator needs to change the web objects.
Benedikt Bongartz 00:17:40 Yes.
Mikołaj Świątek 00:17:41 That's probably… Okay, we already agreed that it's gonna change the CR… life patch the CRD.
Pavol Loffay 00:17:49 Yep.
Mikołaj Świątek 00:17:50 I might as well live patch the mutating webcook, if you really want to. I have given up that line of… I've accepted that this is something that we might do.
Pavol Loffay 00:18:02 it's… Yeah, I think… What might be problematic?
is… If the operator is installed with OLM, and we keep the CRD as part of the, kind of, bundle, or manifests in the bundle, then OLM might, kind of, repet it afterwards.
I'm not sure how that's gonna work.
Mikołaj Świątek 00:18:26 You can check how it works with, like, other operators that do this kind of thing.
Pavol Loffay 00:18:31 Yeah, but I think for the CRD, we might kind of do… with OLM, we don't have this issue, so we will continue shipping it as it is, and with the help distribution, we will kind of allow this behavior, so it might be actually fine.
Mikołaj Świątek 00:18:50 Yeah, anyway, this is not that interesting at the end of the day. But it does fix this, so… It's worth… Painfully accepting.
Okay, bye-bye.
Josh?
Benedikt Bongartz 00:19:08 Yes, so the question was more or less how to proceed. So since the cluster observability CR itself is behind the feature gate, and we… potentially modify it.
This was resolved, I think?
Yeah, the question is more or less, like, if we go, for example, to… just go to this point here… second… chat… There. If you open this one… you get the sense what this is all about. So I got this inspiration, basically, from Envoy. So when I deploy Envoy, I cannot configure all the details, and I had to, in my home setup.
to deal with, mounting the tailsate socket and whatever, and I looked how to modify this, and they have this patch CR, and I thought, okay, so this might be a good approach to not expose anything.
But give you all the flexibility to do at least yeah, minor stuff you want to do. So when should it be used and when not? So it's not there to replace the collector CR, It's not meant to be used with… highly complex things, because then you could just go to the collector CR and change it there.
It's more like you have to default off the cluster observability piece.
And you just want a tiny, different configuration.
you're happy with the CR, how it works, but for example, just… Changing the resource limits.
Or… you want to… increase the replicas of the cluster collector, which is this guy connecting to, your cluster API.
this is currently not possible, and if we start opening up the CR with all these options.
it could become tricky. So the idea would be, in the CR, we just expose Would we think… a user will regularly change. So, for example, if we have something like HA mode or not.
This might be something you can enable or disable, and then… We configure this with the operator for you.
And this here is more like, yeah, if you have really some needs, for example, tweaking the resource limits because you have tons of locks you need to process, and it does… it's not sufficient what we ship.
Then you do this one.
Yeah, and you don't need then to start over and learn all the internals just because you need to flip one thing. And the other idea was, like.
we've… we had this discussion for the exporter, currently we have the OpenTelemetry exporter, and we have no settings. And Splunk wanted to have all the settings of the collector.
And there was the question, do they change over time? Potentially they don't too, but… you never know, and this way, for example, Splunk could just provide a patch and say, like, this is our cluster observability patch for Splunk backend.
Apply this patch and apply, the collector.
OpenTeametry, Cluster Observability CR, and you're good to go.
So, one comes from the vendor, and one comes from… Yourself, we just say, like, send it to this one.
yeah, that's the idea behind it, and I was curious what your thoughts are, and if we should just start experimenting with it. So, like, not accepting or denying whatever is proposed here, but just building some POC and play with it and see how people like it.
I've seen that in the Helm repository, maybe in Mikulai, or… who pinged me, someone pinged me, there was a request also where Tyler got… Feature requests where people already allow… installing the cluster Observability CR, yup.
So it seems like some people are using it already, and I got pinged on Slack from one guy too, he had some complaints and was like, it's not ready for use, but… Yep.
Pavol Loffay 00:23:11 I haven't read the proposal yet, but, what is kind of maybe… misleading to me at the moment is… It's… it's a cluster observability patch.
And then I… am referencing the… the cluster of celebrity CR in the charger.
And then I have patch for collector.
Benedikt Bongartz 00:23:39 Yes, so the.
Pavol Loffay 00:23:41 Why do I need to, kind of, reference both?
Benedikt Bongartz 00:23:48 Maybe we don't need to do both, you could directly go and… Go for the agent.
Yeah, so currently you can create multiply cluster observability, CRs, so you could have one which is named Bin and one which is named Pavel, and this would then deploy two daemon sets on each node, Basically, it will just replicate the work. And… we could… Both want to patch the agent, but in different ways.
And that's where you go and you reference the object, and then the associated agent to it. Because currently, if I just go with… yeah, so we could also use something like a label selector or something. This is basically… it's set up similar to how Envoy does it, that's… the thing. So if you scroll up a bit, on top, I was also linking this in the summary, the first sentence.
their NVY patch policy.
And you scroll down a bit, they have, apply standard in or apply from file, doesn't matter.
Oh no, this is something… that's the config map, sorry, this is… Yeah, a bit further down, like, testing, and then there you see it.
there they… reference the gateway, and then they reference the type, and yeah, so since we had this two-level thing, but we can also do a… Open Teammatory, collector patch CR, and then just patch the collector.
But the collector has everything exposed, so… but yeah.
So the thing I want to solve, more or less, is, like, how can we… Provide an option to change everything underneath the… or… cluster observability thing, if you have some small need, I don't want to expose it and have some… Checks, and whatever, and maintenance for it.
On the other hand, yeah.
Mikołaj Świątek 00:26:03 What is the benefit of this being a separate CR, rather than just putting patches inside the cluster observability CR?
Benedikt Bongartz 00:26:12 If you go back to the original pull request and then jump to the issue.
And then you see, like, this… describe the solution you did like, This was the first thing that I had, was just embedding the entire spec, which is, you can see there's the exporter, we go to agent, patch, and then in agent, you would then provide the processor and whatever.
Write this one.
And, this turned out to… yeah, having thousands of fields directly on the cluster CR again.
Which… I wasn't sure about, especially because we have this generic configuration with the, processors, and… Yeah.
Mikołaj Świątek 00:27:07 I mean…
Benedikt Bongartz 00:27:08 pipelines, and it becomes tricky in any way, so I would avoid patching things in general. It was just, like, this is a generic way where people can patch at least a few things.
Mikołaj Świątek 00:27:19 At the age.
Benedikt Bongartz 00:27:20 For example, sorry, if you want to remove something, you go and you remove Or you add another processor, adding it to the processor pipeline lists It's also a thing for itself, because you would override the entire list, so which means you need to check first what kinds is there, because you cannot easily merge it.
Mikołaj Świątek 00:27:44 Okay, I'm not sure if that actually answers my question, because… From my perspective, It's like, why can't we put this syntax here.
Somewhere.
Because this is already gonna be an untyped map of some sort at the end of the day, right? The stuff that's under value is gonna be, like, an untyed, like, some arbitrary… arbitrary nested map.
Essentially, maybe API extension JSON.
Mmm.
Benedikt Bongartz 00:28:20 sort of.
go and say patches, and then I would start with a new entry, which is either agent or cluster, basically the two kinds of collectors we create.
And then I can configure whatever I want, and I can patch.
They're in place.
Mikołaj Świątek 00:28:36 Yeah, so, like, is the reason this is a separate CRD? Because you want to, like.
Like, you don't want to tell users… like, you don't want to… you don't want you for… you don't want users who are reading the definition of the CRD to know that they can do it.
like, you want to keep the functionality outside of it, to here? Like, that's kind of the main thing. I'm not actually sure I understand.
I understand what the functionality is for. Like, it's even, in some respects, quite elegant to just do, like, adjacent parts. I was…
Benedikt Bongartz 00:29:17 thinking about it, like, for example, the HA thing, I learned about recently that, yeah, so there is an extension in the collector to, do the leader election between multiple replicas when you get data from the cluster API, and the question was, like, so how do I configure this? I could go with the, I could go and provide an option inside of the CR.
And then I will manage this for you. And I thought at that point, yeah, this makes sense to have an option for this one to enable and disable, because if you're on a single-node cluster, you potentially don't want to have free replicas running around.
But then I was like, okay, there's other options. You don't want to expose anything, and we noticed this with the Open Temperature Collector CR, where I don't know, we almost expose anything, and if someone comes along and has a new request, it's often valid, and since we expose a lot, we expose it too. And I think the original idea with the cluster observability CR in itself was to keep it as minimal as possible, and this was, like, this is an extension we can use, but we don't have to use.
Oh.
Mikołaj Świątek 00:30:32 So this is a way to make it extremely configurable while pretending it's not configurable at all.
Benedikt Bongartz 00:30:37 More or less, yes.
Okay, so basically the core functionality, what is supported, where we can say, like, this feature you can enable or disable and it works, it's there. But if you go at some point and say, like, I want to tweak some small knobs that because I'm happy with the overall setup, but I just want to tweak a few knobs, I configure it somewhere else.
Instead of in place.
Mikołaj Świątek 00:30:59 Isn't there something built into Kubernetes now called, like, a mutating admission policy, or something?
Benedikt Bongartz 00:31:07 No clue.
Mikołaj Świątek 00:31:15 Abel in 136, even.
jea 00:31:19 Yes.
Mikołaj Świątek 00:31:25 Yeah, so basically this is like a… this is, like, a more limited, but more generic Kyverno.
Right? So this is, like, something that allows you to write a policy that says what should happen if, for example, somebody tries to create or update.
Particular resource, in a particular namespace.
Benedikt Bongartz 00:31:48 So, I could go and say, like.
If there's the API version, the kind.
Mikołaj Świątek 00:31:59 For example, this is… This is for creating pods.
And it adds a sidecar if there's not a sidecar.
Benedikt Bongartz 00:32:12 And I can do something similar with the underlying structure, but… for example, what I could do is also patch things Afterwards with customize, but then the operator will reconcile again.
Goes into conflict.
Mikołaj Świątek 00:32:29 Yeah, that's also true. My point is that there is some, like, prior art.
In this form. So it might be worthwhile to actually have a look.
Like, this isn't exactly for what we're talking about, right? It's not for patching, for, like, customizing stuff that an operator might emit for you, it's more, like, for… like, what this is actually for is for if you create an OpenTelemetry collector.
Sorry, it's like, you're a cluster admin, and you want your OpenTelemetry collectors in your cluster to have some default set, all of them.
And this is a way for you to enforce that on a cluster level, by just modifying things as they come through the API server.
So it's not… doesn't solve the same problem.
as you have right now, but it's like, I might… since this is already stable, and so Kubernetes, like.
Benedikt Bongartz 00:33:23 Yeah, so what I was thinking, if I go and say, I create a cluster observability CR, And this will create… open time to collector CRs.
And now this… Admission policy controller will go and change the collector CR.
Will the OpenTeometry operator then go after the CR, and just change it again, or revert it, because it.
Mikołaj Świątek 00:33:50 It should. It should, by all measures. By all accounts, it should.
If the water.
Benedikt Bongartz 00:33:58 Because that's what I had here in the first situation, where I just go and say, like, I apply a patch afterwards, and then the operator just reconciled.
Mikołaj Świątek 00:34:07 Yeah, so it has to be something, yeah.
Pavol Loffay 00:34:10 I think there are probably different solutions how we can Apply the changes on the underlying objects.
Maybe we could do, like, this server-side apply, and the operator would own only certain fields, and the other fields could users… critically modified.
Then maybe we could have, like, this managed and managed mode, where users switch it to unmanaged, they'd be on their own to make modifications.
But I… what I like about this proposal is… is not this part, it's kind of the distributing the configuration, so…
Mikołaj Świątek 00:34:52 Is it actually distributed? I mean, it's a series of patches. You have to… you have to decide what the order is, because they might interact with each other, right?
Benedikt Bongartz 00:35:02 Yeah, so the thing here is that… that's a good point, but the idea with this one was, like, you can provide… I have this also in the proposal.
you could provide an OpenShift patch or something, which makes this cluster observability CR work on OpenShift as expected. You can provide a different patch for, for example, Splunk, if they need specific research attributes, or they need to process the data, I don't know, we need to ask Antoine, but, they can pro… or they had this with the transport, like, a specific compression. They can do this for that… for you. So you just go, and whatever you use currently, you just point it to a different endpoint and apply a different patch, and you're there.
And then… that, like, they're potentially becoming more stable options to the original cluster observability CR, like HA, enable or disable, valid point.
And then we should carefully adjust High-level things, like, as also was discussed, enable or disabling lock collection.
Maybe on a namespace level or something, but be careful with what we add there, and if you have specific needs, you can try to patch it.
And if this doesn't work, you can still fall back and configure the OpenTime2 Collector CR. So like this.
three different levels. So one is, like.
You need to know at least how the collector works to configure it, and whatever.
And then this cluster observability CR is more like you don't need to know how this works at all, you just apply something, and then it appears, for example, in Splunk or in OpenShift.
And the patch one is just, like, I have a small need, I'm quite happy with what I have already, but I need to tweak something small.
And then I would advise you to do a patch. If you have a series of patches, of 20 patches or whatever.
I think… it's… the best approach would be avoid cluster observability CR and just create open TMT collector CRs.
Mikołaj Świątek 00:37:11 I can, I can see. I can see.
The needs for this.
I'll review it at some point. I don't… I'm not that involved in cluster observability in general right now, but as you described this to me.
I can, I can see how it's useful.
Benedikt Bongartz 00:37:37 And we can potentially, if we see there is tons of people who always patch resource attributes or whatever, and we say, like.
This somehow is important?
we potentially put this into the CR directly at some point.
Yup.
Mikołaj Świątek 00:37:58 Okay.
Abel, Jacob, you want something? Do you have any more comments?
jea 00:38:08 None for this. I've been, like, looking at this from afar, mostly on the Helm side of things, but… I'm a fan of most of this. I… I've been more focused on instrumentation stuff as of late, and I'm trying to get feedback from some other people in OTEL on Pavel's, RFC.
For that. So, that's been more of my focus recently.
Mikołaj Świątek 00:38:34 Is that why Michelle is commenting on that RFC? As you asked him?
jea 00:38:39 Yeah, he and, Jack Berg both have a bunch of thoughts, and I'm talking with Jack right now, like.
in Slack, and apparently Grafana is working on their own light.
their own operator for hotel instrumentation, which I don't know why they're doing that, and so I'm trying to just tell him to upstream now, and give the feedback of what they want, rather than forking the ecosystem? It just doesn't make any sense to me.
So… I would like for him to not do that, and I'm trying to convince him to not do that, currently.
Mikołaj Świątek 00:39:22 Okay, cool. I think Michelle is worth listening to, because Dash Zero actually has, like, A lot of users.
Of instrumentation in their own operator, so…
jea 00:39:33 Yeah, I agree. His feedback is going to be super useful here. It's unclear… like, Jack opened up an issue earlier in the year about what they want to see.
Over here. I'm gonna put it in the chat.
And it seems like we're hitting all of them. It's just very unclear why they're doing this. I mean, this is like… Are we still recording these calls, or are they not recorded anymore?
Mikołaj Świątek 00:40:01 The… there was a… being recorded.
jea 00:40:05 I think it's still being required.
I'm not going to share more of my thoughts, though. But…
Mikołaj Świątek 00:40:15 I don't know if it's accessible anywhere after it being… after having been recorded.
jea 00:40:20 unclear.
Either way, I… I'm not a fan of them doing this, and I'm going to try and convince them otherwise.
Mikołaj Świątek 00:40:32 I'm honestly not really sure why, either.
jea 00:40:36 I don't know.
I mean, I'm saying to him, like, he's like, yeah, we're doing this with the goal of upstreaming in the future, and I'm like, that's just not gonna ha- it's just… Upstreaming, upstreaming, like, operator features and CRDs is gonna be a nightmare.
And, like, trying to merge that is gonna be really hellish, and I just don't think we should do that.
I think that if they're gonna make changes, then we should just add them into this fold.
Mikołaj Świątek 00:41:09 Would help if he came, came on… came on the sign meeting, and… and explained.
jea 00:41:14 Yeah.
Mikołaj Świątek 00:41:15 Hmm, you know.
Or just their general motivation?
Pavol Loffay 00:41:24 Thank you for sharing, Jacob.
I was going through your comments, And… I think the only one that… that I… When my attention is the… how the exporter endpoint is… configured. You suggested that we should allow users to reference the collector CR instead of providing the endpoint.
I was thinking about that. It works in Kubernetes, but it doesn't work when users would like to export to a third-party OTLP endpoint.
jea 00:42:11 Yeah, yeah, I think we should just accept both. I don't think it's a… it's a one… like, only collector reference, it's that I think for… when you're exporting intra-cluster, it's really useful to be able to have the validation.
from the SDK to the collector that I am actually exporting to the correct place.
Mikołaj Świątek 00:42:34 It's awkward, though, right? It's awkward because we want to use the clarity config, and in the clarity config, this is just a text field.
So…
Pavol Loffay 00:42:43 So this would be… this would be for the environment configuration.
Mikołaj Świątek 00:42:50 Yeah, because if we're using declarative conflict, then… either… either we accept that the declarative config the user puts in is not exactly what they might get, which is honestly already the case in the collector CR, so maybe that's not a big deal, but for example, we could decide that the user can provide a declarative contract where they don't have the exporter set, or they have it set to a placeholder, and then they externally define that they would like this to go to AutoCollector X.
And then we just replace it inside the collector config. That's something we already do for the collector config in a bunch of ways, so it wouldn't be anything new.
For us, and then it could be implemented that way. Because right now, we're just taking, literally, the declarative config, which means that they have to put it there themselves.
Right?
Pavol Loffay 00:43:47 Yes, although… In my proposal, the exporter field… It's under the environment config.
Mikołaj Świątek 00:43:59 So…
Pavol Loffay 00:44:00 really separates the… the environment configuration from the declarative one. If we want the exporter to be configured for both, then we need to move it directly under the spec.
So, for instance, we have a resource configuration that is directly under the spec, And… Because we want to inject some things into the resource, even when Users are using the declarative content.
So, we could do it, it's just we would need to change the structure.
Mikołaj Świątek 00:44:45 Is that worth doing?
jea 00:44:53 Hey Jack, glad you joined. I just want to, like, chat about this in… in this meeting, so that we can just get it done. I just want to understand more… About, like, what operator you all are building, and why, and sort of what the staffing looks like for that.
And the timeline for that?
Jack Berg 00:45:14 What operator we're building. We're building an operator that has the capabilities That we need, to, you know, to have, like, a compelling product story for our customers. And notably, that can't include an annotation-based approach.
It needs to be able to have broader brushstrokes to install instrumentation across a Kubernetes cluster that doesn't require, you know, going and touching all of the individual pod definitions and adding annotations to opt-in.
And it also can't require the annotation-based thing where, you know, you have pre, pre-knowledge of the version of CLIB which is used in your application, whether it's Musil or GCLib. And, you know, these are the types of capabilities that are unlocked by the injector. So, you know, the injector, you can, you can do something like you mount the injector and instrumentation resources to Either all resources in a… workloads in a cluster, or some predicate that you express.
And, you know, it's smart enough to be able to, only… to mount the version of the instrumentation that is correct based on the version of libc, which the application uses, so that's pretty cool. And, you know, it will… like, if there's things like the application is already instrumented with a Java agent, it'll skip that.
So, that's, like, one of the requirements is, like, no annotations. Like, that's just… it's just not good enough.
jea 00:46:57 Yeah, what's unclear to me, and I'd like more context here, is why this isn't being done with our group, because this is all stuff that we've talked about for, like.
Two years in, sort of what we want for our next version.
And this is the first that I'm hearing of any of these problems, other than the issue that you brought earlier in the year. I haven't seen any contributions or issues or any comments on any of the other instrumentation things that we have going on.
in this group currently, and my… my concern here is that, were Grafana to actually, like, make their own operator for this, it fractures the ecosystem and documentation for users. It… actually hinders our ability as a SIG to provide, like, the thing that we do, and it sort of brings the… yeah, that fracturing is really the main concern here.
Jack Berg 00:47:54 Yeah.
jea 00:47:54 I don't think anything that you said is particularly controversial for what we would want to see for the next version. It's just unclear to me, like, why not bring the people into the fold here, and, like, we could all spend our time together on this effort.
Jack Berg 00:48:07 It is our intent to, you know, to develop within OpenTelemetry, but as, you know, I'm sure you know, you know, like, OpenTelemetry, progress is not as fast as it can be within, like, a vendor, and so, like, we kind of have two problems. Like, one, the people that are available to work on this within Grafana you know, do not have the capacity to… to… at this moment, to come and join, like, the operator sig. Like, we all have conflicts. Like, myself, I just dropped the JavaSig to come and attend this.
And I think… I think the other thing that's… that's pretty crucial is, like, there's some ideas here that we're, like.
we're not sure about yet, and so we want to actually solidify these ideas and, you know, sort of test them out, and once we're more confident about them, like, you know, bring that proposal to the operator group. I think one thing that's sort of unfortunate about the timing is that, it seems like the operator group, and I haven't been following the operator group very closely, but I think there's, like, sort of in the midst of trying to promote, the instrumentation CRD to beta, and so, like, you know, that's… that's… that's… that's not great, like, because, you know, the instrumentation CRD has been sort of at alpha for a long time, and if there wasn't, like, an, you know, a desire to promote that to beta, and it was just, like, status quo, then it'd be fine if we were developing something over here with the intent of upstreaming it. I think, like, the problem is that, like, we're developing something over here.
while the operator is trying to mature its instrumentation CRD, and the thing we're developing over here is sort of like in conflict with the, you know, the instrumentation CRD that's trying to be matured.
jea 00:50:00 But at the same time, we would not need to… like… I have two issues with that. Maybe I'll let Mikolai go first, though.
Jack Berg 00:50:12 Yeah, yeah.
Mikołaj Świątek 00:50:13 They're just… so… Just to be clear about something.
Yeah. At least what you described.
is mostly orthogonal to the beta effort. It's like, we actually have had, like, not exactly what you proposed in the issue that you filed, but a similar proposal for being able to, let's say, couple instrumentations to instrumented pods in a way that doesn't involve annotations, that the proposal was there first to involve selectors, and then it evolved to using, like, a series of rules.
That's… that's, like, an… a non-breaking incremental addition.
We could add that to both the V1 Alpha 1 and to the V1 Beta 1 instrumentation, and it wouldn't actually break anything.
And it's kind of the same thing, in my view, with the… with using the injector. Like, we have two possible ways, it's probably both are gonna happen, of adopting the injector, and one of them is literally just stick the injector in our existing instrumentation images, and just have it do work that currently kind of happens haphazardly in the operator code. And that is also not a breaking change in any respect.
Jack Berg 00:51:34 Yeah, I don't think it should be breaking, I think it should be just, like, a net enhancement of capabilities.
Mikołaj Świątek 00:51:39 Yeah, so it's like, I don't think you should feel like you, like you're stomping on top of View on Beta 1. And Benny, view on Beta 1? No. View on Beta 1 was not… involved in the injector. The main thing with the injector is actually the declarative config.
that is, like, the primary breaking change that's happening in there, and the other one is that we actually want to go from annotation to label for performance reasons. But in some way, adding more ways of of, selecting instrumentation for a given pod that's being instrumented is, like, in some way, alleviates the… annotation problem.
Jack Berg 00:52:23 Yeah, I can totally buy that, right? So right now, the, you know, the current way that you do selection is on the pod label side, and you know, you could evolve that to change the instrumentation CRD to have, you know, a centralized selection criteria if you want.
Mikołaj Świątek 00:52:37 Yeah, and that's… that's, you know, that's not… that doesn't break anything, and it's kind of even… really, it's quite… The scope of interaction with the whole system is actually very limited. It just comes into play in, like, a single, single point.
So, it's pretty easy to change that, or to add things to it without messing with anything else. So, like, neither of the things that you're describing right now are, like, feel like… Feel very controversial to me.
Like, not having seen anything specific. And yeah, sorry, I…
Jack Berg 00:53:13 That matches what I've heard, like, you know, I think we've talked in different conversations, sometimes asynchronously in GitHub, sometimes synchronously in, like, other meetings. I've never attended this meeting.
And yeah, like, I think, like, everybody's sort of, like, on the same page of the types of capabilities they want to see, like, long-term. It's just, like, how do we sort of navigate to getting there. And just like, Pavel, I see your hand up, but, you know, it is Grafana's intent to, like, use the OpenTelemetry operator, like, when the capabilities that we need are available. And it is our intent to, you know, you know, sort of help the OpenTelemetry operator, you know, get to the point where it has the capabilities we need. We're just sort of, like.
prototyping and doing, you know… I wanted to call them proofs of concepts. We do intend on shipping them, but, you know, we're doing this in a way where we can replace all this with the hotel operator, like, once we have the chance to take these concepts and work with you all to upstream them.
jea 00:54:12 Paula, I'll let you go, and then I'll go.
Pavol Loffay 00:54:13 Hi, Jake. I have one question on the… about the… how we want to implement the selectors. I was looking at it because I'm working on the Wieman Beta 1 RFC, the request is there, and right now, with the annotations, users have to… Can… they have option to specify even the container and which language runs in the container. How would that work with the, kind of, centralized label selector?
Jack Berg 00:54:49 So, yeah.
Pavol Loffay 00:54:51 Any ejector as well, maybe, I think maybe you can do, like, automatic… .
Jack Berg 00:54:57 One of the things you have to kind of become comfortable with, not you, just, like, if you're gonna go with this sort of centralized definition where you're taking broad brushstrokes and saying, like, we want to instrument everything in this cluster, rather than everything that's annotated with, like, pre-existing knowledge, is, like, the way that the injector works like… It doesn't know the language that it's working with.
So, like, you… and you don't know that ahead of time when you have, like, this centralized instrumentation CRD. So you need to mount the injector and all the instrumentation resources to every workload, every pod that would be, like, a candidate for instrumentation.
And, like, if you can imagine, the injector plus all the instrumentation resources, it's like a lot of bytes. It's like… it's like, you know, hundreds of megabytes, maybe even approaching, like, a gigabyte, depending on how you count it. And, so one of the things that we had to prove out is, like, the init containers approach.
Like, we treat that as a fallback.
There's this, there's this alternative way of mounting resources in pods, which is called Image Volume Source.
It was, like, yeah, it came in, you know, Kubernetes 1.31, it was… it reached beta in 1.33, and it's GA in 1.35. And so when that's available, you can mount the injector and, you know, all of your instrumentation resources instantaneously, extremely cheaply, without doing any, like, copy action for, like, a gigabyte's worth of files. So, like, that is part of our approach.
approach, is like, you know, we're looking forward to this image volume source, and, you know, that basically makes the tax that you're paying when you try to load the injector and all the instrumentation resources everywhere, it makes it very cheap.
Mikołaj Świątek 00:56:43 On which note, we should really get to implementing that on newer Kubernetes.
Benedikt Bongartz 00:56:51 If there is even an issue for exactly this one.
Mikołaj Świątek 00:56:53 Of course there is. But right now, you know, when… I don't know at which time, at which time, like, the least supported OpenShift version is gonna be on 1.33, it's probably gonna be many years from now.
Benedikt Bongartz 00:57:09 It was there to have it, like, separated.
Mikołaj Świątek 00:57:12 I know.
Benedikt Bongartz 00:57:13 older Kubernetes versions, it works differently.
Mikołaj Świątek 00:57:15 I know, I'm joking. I know.
Pavol Loffay 00:57:19 Check my assumption is, like, if it matches the selector, you just instrument everything that runs into both, like, you wouldn't pick a container.
Jack Berg 00:57:27 So, we've sketched out both approaches. We've sketched it out where, like, all the containers within the pod get, like, instrumented, so the injector and the instrumentation gets mounted to all those containers, and also, like, adding selection criteria that allows you to select a container within a pod, like, as part of your… but that starts to look, like, pretty annotation-oriented, right? If you're, like, getting down to the level of granularity in your selector rule.
Where you're specifying, you know, this pod and this container within the pod, you know, you're better off just with annotations.
Or maybe not better off, but it's like, it's.
Pavol Loffay 00:58:01 No, no, no. Yeah, it's just… I think both are ugly, just needs some nice design, like how you want to structure it in CR.
Yeah.
like, how do you represent this in the CR, right, in the selector?
jea 00:58:18 We only have 2 minutes left, and I want to be cognizant of schedules.
But, Jack, is there a place that we can actually see this work being done, and sort of follow this experimentation that you're talking about?
Jack Berg 00:58:31 Yeah, I think the repository is public.
Let me check right now.
jea 00:58:45 And so while you find that, the other thing that I would say is it would be really useful, I think, if the people from your end were to maybe open or share some of the learnings. You don't need to come to this meeting. We have a lot of contributors that are in time zones that don't align well with this, align well outside of, like, Europe and, the Americas. So, like, I would just like to see and understand more about The progress being made there, and what we can do to sort of align with that future, so that we don't need to, like, have a fracturing in that way.
Yeah.
Jack Berg 00:59:23 It's, and, you know…
jea 00:59:24 Let me, let me just explain.
Jack Berg 00:59:25 Yeah, go ahead.
jea 00:59:26 Sorry. We've gone through a couple of… like, CRD migrations, and they are very painful. Like, they are really not fun for users, they are not fun for us maintainers, and anything that we can do to avoid that, I think, is going to make everybody's life a lot better.
And so, what I would like to avoid is needing to do Like, massive migrations in the next year.
if that is the… like, our time horizon for the instrumentation work that we're doing is sometime this year, right? And so, I would really like to avoid needing to do another migration after this work that you're doing is sort of aligned with what we have, because that's just going to create a lot of pain.
Jack Berg 01:00:09 Well, I agree with Mikalaj that, like, this seems like it is just an alternative way to select which workloads are candidates for instrumentation, and so it is, like, a net addition rather than, like, a breaking change. And, like, it's like, choose your own adventure. Annotations, or centralized CRD, Or maybe both. Maybe, like, the annotations and the centralized CRD, like, interact with each other. Like, you have, like, a catch-all rule in your central CRD, and you explicitly exclude pods with annotation… with labels, sorry. Labels, I know that's the new thing. So, it… if everyone, like, nods along to that, then I don't think that there is… even if you, like, agree with my ideas, which I don't think is, like, a guarantee, but, like, even if you agree with them, I don't think it's, like, a big… breaking change.
The one thing I would say could be an opportunity for a breaking change is, like… and I… this was another thing I mentioned to you in DMs, Jacob, and we should probably take this offline, but, like, I think that users should be forced to specify their instrumentation version in their… in the central CRD.
I don't think that there should be a default. I think that's caused, like, a lot of problems.
For folks. Probably mostly the people on this call.
jea 01:01:26 Yeah, dude.
Jack Berg 01:01:27 If you're gonna make a breaking change, like, that's a good one to make.
jea 01:01:32 Yeah, I agree. That's one that I really would like to… to do away with, as well. But… It… again, it's like, anything that we can do to make it so that it's one breaking change one time for users, and not… Like, one breaking change every 3 months.
Is a good thing to me. And I just want to align with you and, you know, Grafana people to ensure that we are sort of hitting that as a goal.
Because again, the more breaking changes that we introduce… I mean, I've spoken to a bunch of users in New York, and it's like, every time that we push a braking change, it… makes people very frustrated with us. And we get it from, like, users and issues, and we get it from, like, SIG meetings as well. So anything that we can do to not do that is really my goal here.
I just want to understand what, like, how we can work best together to ensure that.
Jack Berg 01:02:26 Yeah, so what's… what's the Slack channel for this? I'll, we'll pick up this conversation async.
jea 01:02:32 Yeah, yeah, that sounds good. Yeah, if you want to just bring it into Ocel Operator, or if there's stuff that… You want to do privately, where you just open, like, a… Side channel, and then talking there.
Jack Berg 01:02:46 I think it needs to be private, and the repo is private.
jea 01:02:49 Yup.
Mikołaj Świątek 01:02:51 while I'm here, and we're all here.
and Jack is here, I wanna… I wanna shamelessly take advantage and say, Avo, Jacob, look at the security advisory.
At the very least, at the very least, make your opinion known on whether what I want to do is what you agree with.
I'm also new to this process, okay? I'm trying my best, but I'd like you to make it clear. You can click on Security Advisories in the GitHub UI, and then go in there and see, because it's technically a critical. I don't think it's a critical, but we need to make it clear what we think about this, and what we think the actual severity should be, and how we're gonna handle it exactly.
I think the way we're gonna handle it is just… add a note to the documentation saying, if you can create an OpenTelemetry collector CR, that means the same thing as creating a pod. Be aware of the implications of that.
And also, we're going to add a feature where you can specify which namespaces this is allowed in via an operator flag, and just use the pod security policy library to do that at admission time. That's kind of my point.
jea 01:04:05 Yeah, that… that sounds good to me. I… M… I mean, a lot of these security things have been very frustrating. This process is, like, so annoying, and I appreciate…
Mikołaj Świątek 01:04:16 advantage of Jack, because he called us out in there. I don't know if you even noticed, but I.
jea 01:04:21 I saw.
Mikołaj Świątek 01:04:22 I…
jea 01:04:22 My GitHub notifications have been terrible the past, like, year. I don't get half of them anymore.
Which is very frustrating. And so it's, like, a lot of things have been slipping through, and it's… I just don't know how to… how it's, like, how other people manage this. Like, Jack, have you found another system for this?
Jack Berg 01:04:43 No.
Mikołaj Świątek 01:04:45 Email.
Jack Berg 01:04:46 What do we call it? We say that we have notification bankruptcy.
jea 01:04:51 Yeah.
Jack Berg 01:04:52 notification bankruptcy, and I, for some… like, I… some things bubble up to the top when I'm explicitly mentioned, and, you know, advisories, my eye catches those somehow.
But, yeah, I don't have any good system.
jea 01:05:07 Yeah, I talked to somebody a bit ago, I think maybe Jurassi told… gave me a tip about some, like, GitHub inbox thing, but I forget. That was, like, 3 years ago at this point.
So I forgot. But, anyway, Yeah, I'll take a look at that.
Mikołaj Świątek 01:05:23 I just want more… I just want more eyes on that. I am… I'm…
jea 01:05:27 Yeah.
Mikołaj Świątek 01:05:27 Broadly, I have an idea of what we're doing, but with, like.
I think we should change the severity on that report, and I don't want to do it myself.
Is, is more or less, you know… the gist… the gist of what I'm asking for.
jea 01:05:47 Yo.
I'll take a look at that today.
Yeah, thank you. And thanks, Jack, for joining. I appreciate you dropping.
Mikołaj Świątek 01:05:55 Yeah.
jea 01:05:56 Java call, and, excited to, like, continue the discussion.
Jack Berg 01:06:00 Yeah, yeah, we'll pick it up async. Alright, see you all on Slack.
jea 01:06:03 Cool. Cheer.
Mikołaj Świątek 01:06:04 Yeah.
Pavol Loffay 01:06:05 Bye.
