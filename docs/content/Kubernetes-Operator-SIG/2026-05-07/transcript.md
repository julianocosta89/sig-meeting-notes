SIG: Kubernetes Operator SIG
Date: 2026-05-07
Duration: 57 minutes
Zoom Recording URL: https://zoom.us/rec/share/XDIzfCJVugnOGzbiMvSTtUG2tMb-78EuJmnvYHl_hrH5soFSV_6V-Mgh2u0Nf0E7.Xwh10tTfpNcRIBr7
============================================================

## Zoom Recording Transcript

**Mikołaj Świątek** 02:14 Hey.
**Israel Blancas** 02:19 Hey, how are you doing?
**Mikołaj Świątek** 02:22 I'm in a chain of fourth hour of meetings, but other than that, I'm doing pretty okay.
**Israel Blancas** 02:32 Oh, well, at least it's Thursday, right? So, we're closer to the weekend.
**Mikołaj Świątek** 02:38 Yeah, yeah, I also, I've also, like… what is even going on? What is Zoom doing?
Oh my god… Zoom is, like, the worst-behaved windowed application I have ever seen.
**Israel Blancas** 02:53 Yo.
**Pavol Loffay** 02:56 Hi, guys.
**Mikołaj Świątek** 02:58 Beautiful.
Mmm… Let's, join… Let's prepare… I'm really stutterbrained today, I'm not as prepared as I would like to be, unfortunately.
All of this.
But there are some things I kind of want to talk about. I just don't have these in the agenda.
**Pavol Loffay** 03:39 Yeah, I have some things as well.
**Mikołaj Świątek** 03:41 All right You know if Jacob's gonna be here?
My first request is actually immediate, and can you approve this thing?
As I merged the, the security bits, the cosine, SLSA, and so on, and it fails on main. And I tried to fix it, and it still fails, so I'm reverting it.
And it can wait until the contributor who submitted it Proves to me that it actually succeeds in this fork.
Thanks.
**Pavol Loffay** 04:36 approved.
**Mikołaj Świątek** 04:37 Thank you.
So yeah, that was the first announcement. The first announcement was that this was merged and then failed.
I am… I'm a little bit on the topic of those. Some of those GitHub actions are kind of… They look kind of… not as solid as I would like.
Which doesn't… which isn't, like, promising.
**Pavol Loffay** 05:06 Well, this one will… But… well, actually, the action is not that long.
**Mikołaj Świątek** 05:11 The SLSA GitHub action is not that long, but it behaves incorrectly. Like, it has steps which fail, but report success.
Which is why I spent, like, half an hour today trying to understand why it… what was wrong with it. Like, it had steps which just completely fail, but report green in… to GitHub, so… That's not… that's not very nice.
Alright, I think we can get started. Pavel, what do you have? Is one of the things that you have the view on Alpha 1?
**Pavol Loffay** 05:45 Y… yes.
I think we agreed on V1, Beta 1, the instrumentation CR. I'm working right now on, on the proposal, I want to outline all the changes that we want to commit to, and then start working on the on the CRV and all the parts that needs to be done. So, I will submit the RFC, It should be probably maybe ready tomorrow. Anyways, and then I wanted to talk about the HA for the instrumentation webhook.
So right now, we package the webhook into the operator, into the reconcil… into the controller, essentially.
The controller, is a single atom, because it owns the, It does the leader election, so there is always just one instance needed of the controller. But for the webhook, webhook can be scaled to multiple instances.
And then the API server talks to it through the Kubernetes service, right? So that's the… the normal kind of communication on Kubernetes. So, what I would like to do, is to decouple it from the operator, and… then we have, essentially, two approaches how to deploy it. The first one is… The… we would define the webhook deployment in the bundle, with… Let's say two instances of the webhook.
And the second approach would be the operator, once it starts, it would deploy the webhook.
I would prefer this second approach, because it gives us more control How the webhook is deployed, and we could as well support scaling the, the webhook deployment. So, a user that needs to have more instances, they would be able to scale it to more than two instances.
And people that don't want to have two instances, they could still run just a single instance.
**Mikołaj Świątek** 08:09 Wait, so when you say… when you say that… When you say the operator controls it, how… what do you actually mean? Does the operator, like, directly create a deployment and so on?
**Pavol Loffay** 08:23 Yes, the operator would create the deployment, would create the webhook, the mutation.
thing that hook objects, the pod mutation that hook object, Yeah, I think that's those two objects, and the service for the ebook.
**Mikołaj Świątek** 08:43 I don't… I don't like that, because I think that's gonna be cra… play… it's gonna make deployment super complicated, like, in the sense that… like, that service is something that the CRD has to be pointed, or the… not the CRD, but the… The admission webhook resource has to be pointed to that service.
Right, so if you're decoupling, it makes… it's, like, more convenient if you're… if you're, like, deploying with Helm, deploying the operator with Helm, or via Customize, or whatever. It's more robust if you have both of these things defined in your manifest directly.
So…
**Pavol Loffay** 09:25 All these objects would be created by the operators, so the operator would have full control.
**Mikołaj Świątek** 09:33 We want the operator to create the admission and rotating webhook.
**Pavol Loffay** 09:38 I think it's just the… I think it's just the mutating webhook. It's a mutating webhook service and the deployment.
**Mikołaj Świątek** 09:47 I also don't like it, because for me… Hey, Jacob, congratulations!
**jea** 09:56 Thank you. Thank you, thank you, thank you.
**Mikołaj Świątek** 09:58 You look good, you look rested, you look ready.
**jea** 10:02 I'm ready, I'm rested, I'm… I'm back with, with a vengeance.
**Mikołaj Świątek** 10:07 So this is good, because you walked into the, how to deploy webhook discussion.
**jea** 10:12 I know, I can tell. This is good.
**Mikołaj Świątek** 10:16 Something that I really like about the running the webhook in a separate deployment, is that… You're kind of… what's the right way to put it? When you're deploying the operator, you're essentially much, much more robust. Like, you can basically guarantee that the webhook is always online.
And so you don't get, like, weird disruptions in service when you're, like, deploying a new operator version or something. So that's, like, something I quite like about this, and also, like, you can scale it independently, you can make it faster, these are good things for me, and if you make the operator do it, it's gonna be weird. Like, for example, it's gonna be weird because… How does… upgrading the operator work. Like, the operator… you have to upgrade the operator, and then the operator has to upgrade… has to find the webhook resources that exist, it has to… it has to upgrade on its own. None of this stuff is, like, I think, very complicated.
But it's… like, I don't really see the benefit. Like, for most… for a lot of existing operators that I've seen, and the one that immediately comes to mind is Argo CD, They just have it as part of their deployment. They have, like, a webhook server.
kind of deployment in there, and I think that's perfectly… a perfectly valid and normal way to do. There's some additional complexity from having a separate binary for this, but we're already gonna pay that if we're doing a separate webhook.
But they.
**jea** 11:56 Yeah.
I think as long as we can keep the existing functionality and we don't require people to do it this way, I think it's alright.
I… I don't love… I think I'd be interested to hear what Antoine, thinks about this, because I know that his, sort of, recent mission is trying to get everything to be in, like, single operator binary, and the idea of, like, splitting something out Permanently is, like, not… ideal to me. I think that there is benefit to keeping it all together, in that it's, like, architecturally very simple, it is easy to understand, like, what is doing the work. It's more similar to, like.
general operator expectations, I think, from a user perspective. That being said, like, obviously from a scaling perspective, it is not… ideal, right? Like, it's not… I mean, part of this is because of our own, Mistakes, maybe? Or, past error of, like, how we designed this?
In terms of, like, not using the… Label selectors?
But… Definitely, like, splitting it out, it's going to scale better, and if a user is, like, experiencing the amount of churn that I know a bunch of users have with this, I think it would be valuable to split it out. I just don't want to make that the only way to run it.
I think is my only qualm.
**Pavol Loffay** 13:27 I think we had some Maybe as well from out to end, that there were some users that wanted to run just the instrumentation part of the operator.
**jea** 13:38 Is that right?
**Antoine Toulme** 13:40 Yeah, we only use that.
We don't use the target allocator, we don't use any fancy CREs, we just want to auto-instrument. Actually, the direction that the market is taking is that they want to auto-instrument everything all the time, all those label selectors and the eyes, but…
**jea** 13:59 You too.
**Antoine Toulme** 13:59 It's also, with the injector, the huge temptation to just, bake in all the SDKs at once, not just one, not even give you the option to pick just Java or Python, it's just gonna be, like.
We're gonna shoot everything that moves.
And we're going to see what's going on in your cluster, no matter what.
And the feedback from customers should be, you're sending us way too much, you know, rather than, we've been looking for this particular app, and it's still not showing in our dashboard.
And it works the first time, and I don't want to think.
**jea** 14:37 Yeah.
**Antoine Toulme** 14:38 undergoing…
**jea** 14:39 If that's what the user wants, then I think we should… we should give them the path.
I think that… My only concern is still just, like, I don't want, I want people to have the simplicity of single binaries still.
And if we can get best of both worlds, where somebody can, like, opt in to a separate webhook in a separate server, which I don't think should be that challenging, given that the code is, I think, well isolated, it should be building a separate main. Like, it's not that hard.
I think I would be okay with that.
**Antoine Toulme** 15:15 Yeah, I'm not… I don't have any, The effect to me is the same. Is there a reason to break it down in multiple binaries? I'm not following…
**jea** 15:25 Yeah, I mean, I think…
**Pavol Loffay** 15:27 I mean, we could still have a single binary, maybe like a subcommand for webhook. If you run the subcommand, it will just.
**jea** 15:33 Oh, okay.
**Pavol Loffay** 15:33 hook. So…
**jea** 15:36 We could do that.
**Mikołaj Świątek** 15:38 The only reason…
**jea** 15:39 under…
**Pavol Loffay** 15:40 I think the question is, like, what's gonna be the default, right? Like, how people… what people gonna deploy by default? Like, is it gonna be this… a single… thing that we run right now, or is it gonna be the controller and web move into different deployments?
**jea** 15:57 I think it would be the former, where just the default will continue to be what we have today, and then for people who want HA, or people who want different scaling characteristics, they can do that. Also, would we think about moving the, like, collector webhook for, like, validating and mutating?
**Pavol Loffay** 16:13 That doesn't make sense.
**jea** 16:14 No? Okay. Just checking that we're scoping this only to instrumentation.
**Pavol Loffay** 16:19 Yeah, I was looking at other operators, namely the cert manager and Istio, they both have the bot mutating webhook, and they deploy it as a separate deployment.
Their architecture is a little bit different, because the server manager and Istio are like a meta-operator.
and then you'd create a CR that defines The deployment for the controller and webhook.
Which is not the case for us. We have just the instrumentation CR defines the instrumentation behavior, it's even namespace scope, so it doesn't, you know, really correlate to… like, we shouldn't host the configuration how the Patbook should be.
**jea** 17:08 Yo.
**Pavol Loffay** 17:08 in the cluster.
**jea** 17:09 Yeah, I mean, if we could just get a subcommand in that makes it easy to just deploy the webhook server as its own thing, it sounds good to me. Architecturally, it's pretty… it's pretty easy, so…
**Pavol Loffay** 17:19 Yeah, one thing to call out on OpenShift, we would opt in for the decoupled architecture, because if we… If we go with a single component, there is no way how customers can scale it.
with OLM Because the OLM defines the operator deployment, and customers can't modify it.
**jea** 17:50 I'm not following.
**Pavol Loffay** 17:52 Yeah, so there are two ways how you can deploy OpenTelemetry Operator. One is through the Helm chart. The Helm chart creates the deployment of the operator, and the other deployment model is through the OLM, the Operator LifeLock in Manager. That is for OpenShift. The way it works on OpenShift with OLM is… the… Customers create a subscription object that comes from OLM, and subscription object deploys what we have in the bundle folder right now.
If you go to the open delivery operators bundle folder, you can see the deployment, yeah.
But once it's deployed, customers can't change it. Like, they can, like, increase the replicas of the operator. It's gonna get reverted by the OLM.
So our default deployment model, if you want to support scalability, would have to decouple those from the get-go, and then the operator would have to own the deployment.
**jea** 18:52 I think we could just default to the, the webhook separate command, like, the, like, just have… have it default to the, webhook server approach for OLM, and I think that that's fine. Given that, like, that sounds like what your customers want, I think that that's fine. My larger concern is just, like, I don't want… a user to upgrade the Helm chart for the operator, and then they see that there's, like, a new thing that they didn't know about, and it's just more complexity for them to manage. Like, I want the Helm chart to remain pretty stable in that way, if we can. But I'm fine with changing the bundle for OLM to just do this by default.
**Pavol Loffay** 19:46 Okay, I think that's all. I will work on the pull request, and we'll see how it goes with the subcommand as well.
**Mikołaj Świątek** 19:55 Yeah, subcommand's probably nicer, like, I would… I would be in favor of making a separate binary if there was, like, a gain.
But… the operator binary right now is, like, 20 megabytes, ever since we… I deleted the secret Prometheus dependency.
So, so it's like, whatever. It doesn't really gain much, we can just use a single binary with subcommands, I'm okay with that.
Okay, my next… my… the next fig is mine. If you're looking at the document, I am… I have filed the issue to drop support for V1 Alpha 1.
And the question is, I know we want to do it. The question is, like, how does the timeline look like?
I'm… More or less proposing to just use a feature gate, and the only thing the feature gate controls is whether the conversion webcook works or not.
Because the feature gate… there's a feature gate saying disable V1 alpha, and if a feature gate is on, the conversion webcook returns not implemented.
or whatever, returns an error, saying, hey, this is disabled, and that's it. And after, after that feature gate makes its way through all the stages, the feature gate gets removed, V1 alpha 1 gets removed, and then gets removed from the, from Helm and all the downstream stuff.
Does that make sense, like, as a process, at least, putting timelines aside?
**Pavol Loffay** 21:28 I… I'm just… maybe… I would like to understand… What benefits would give us the feature gate?
And it would benefit to the end user.
**Mikołaj Świątek** 21:41 Well, the benefit to the end user is that they get warning. Like, they… there's gonna be a feature gate, we enable the feature gate, they start getting errors under V1 Alpha 1, right? The errors tell them, the error tells them, hey, this is a feature gate.
You can enable this, you can disable this feature gate to get the old behavior, but know that we're going to be removing this soon. And then they get, like, you know, they can flip it to keep the old behavior for a time being while they migrate.
it's just kind of nicer. If we just delete it, then it's just gonna be… Like, they deploy a new operator, they didn't read the change log, because why would they? And suddenly, it's just not there. Like, if they use Helm, it's gonna just delete… delete their V1 Alpha 1 CRD, and that's just gonna… I mean, Helm is not gonna do that, but, like, in principle, right? It might just, like, delete their view on Alpha on CRD, and if you delete the CRD version, you delete everything from that CRD version.
**Pavol Loffay** 22:49 I don't think the Helm deletes the CRD. I think the CRDs, once they are installed, they are never deleted from the cluster.
**Mikołaj Świątek** 22:56 It depends on how, depends how. The operator Helm chart will delete it. The CubeStack one will not, because I think they are differently, they are deployed differently.
**jea** 23:10 Only sadly, but yes.
**Mikołaj Świątek** 23:15 I mean, if you don't want to do the feature gate, I'm okay with that, I just thought it would be nice.
**Pavol Loffay** 23:20 I just don't understand, like, what benefit does it have for the end user? Like, I deployed a feature gate that is enabled, and… then… if I have a collector stored in etcd in V1, Alpha 1, suddenly it's not gonna be reconciled? Is that the thing?
**Mikołaj Świątek** 23:41 It's not gonna be reconciled anyway, like, it just never gets reconciled.
We don't have a reconciler enabled for this version. What happens is we reconcileView on Beta 1, and Etsy can go and hit the… I mean, the API server, right? The API server can hit the conversion webcook, get the new one. In theory, this should all work.
Right? From the perspective of the user, the problem isn't really what is stored in SD, because the stuff that's stored in SD should already be converted.
Oh, sorry.
**Pavol Loffay** 24:13 Yeah.
**Mikołaj Świątek** 24:14 Yeah, yeah, the problem is new stuff, like, you create a new one view on Alpha 1.
collector. What happens, right? Normally, what happens is that the API server is going to call the conversion webhook, and once it gets the V1 beta one from the conversion webhook, it's just gonna use that. But if the conversion webhook fails, it's gonna return that error down to the user who's trying to create a new V1 Alpha 1 collector.
And, like, at that point, you deploy the new operator version, and suddenly you're trying to create something, and it doesn't work.
And so, then you might want… you can do a rollback, right? But rollbacks are kind of nasty.
unpleasant, you don't want to do that. So instead, there's a feature gate. You just flip the feature gate on, and you're still okay. And then you can go and whichever, go through your GitOps repository, wherever you're storing your resources, your manifests, and go convert everything.
and then test, re-enable the feature gate, you're good. Like, this just gives the user control over whether this works or not without messing with operator versions.
That's, like, my… that's my fainting, anyway.
Maybe I'm being too cautious about this, but… Mmm.
**Pavol Loffay** 25:33 I think it's better to be cautious if we are removing it.
conversion.
from the cluster. Yeah, I would put in the feature gates, I would maybe… Have a bit more time between… Making it a default and removing it.
**Mikołaj Świątek** 25:53 How many? I mean, I put two versions in there right now, which is a month, so how long would you like?
**Pavol Loffay** 26:01 I would like to check internal telemetry if I see… anyone creating V1, Alpha 1. I'm not sure if I can get it from OpenShift clusters, but I would like to check that.
**jea** 26:15 Is there a way that we could just block the upgrade if somebody tries to upgrade the operator and they still have VM and Alpha 1 running?
**Mikołaj Świątek** 26:21 We don't have that power now.
**jea** 26:24 Yeah, mostly.
**Mikołaj Świątek** 26:24 Thank you.
**jea** 26:25 Not as a, like, this is what we should do.
**Pavol Loffay** 26:28 But, like, how we would actually know that if they have W1 alpha only? Because, I think Nikolai… Well, it's like, it's only for the new objects that they fly.
**jea** 26:38 Well, yeah, we're not reconciling.
**Mikołaj Świątek** 26:41 No, no.
**jea** 26:41 ones anymore, right?
**Mikołaj Świątek** 26:42 No, that doesn't exist. It only exists as a… as a… it exists as a CRD inside the CRD, and it exists… there exists a conversion webhook. Those are the only things that exist. So, we can.
**jea** 26:56 I think…
**Mikołaj Świątek** 26:56 retail.
**jea** 26:57 I think… Start by disabling the conversion webhook?
And say, after this date, we will no longer convert, and then after this date, we will delete it entirely.
That way, it's, like, it's not a… it's disruptive, but it's not, like, Fully destructive, if that makes sense, right?
I think that that probably is a good staging for it. Then, when we actually delete it, the code for it will be a lot… it'll be, like, a safer thing to do, a safer operation.
Because we already know it's not even in there.
**Mikołaj Świątek** 27:30 Yeah, there's even gonna… I even wanna have, like, a single release worth of… Separation from setting the feature gate to stable, at which point you cannot disable it.
But the code and the CRD still exist, and then in the next release after that, we get rid of the CRD.
**jea** 27:54 Yup.
**Pavol Loffay** 27:55 Is this actually good practice to get rid of CRD? I thought we should never… Kind of…
**jea** 28:03 I think we can just not reconcile it. I think we could probably keep the… let me see what Prometheus does before I…
**Mikołaj Świątek** 28:08 Good news.
**jea** 28:08 I wish.
**Mikołaj Świątek** 28:09 I don't want to keep it, because it's a bunch of… like, the CRD… we're talking about the CRD, but in reality, we have both versions inside of a single CRD, so it doubles the size of our actual CRD. That's, like, a pretty big downside of having it.
Plus, also, people who are contributors keep adding stuff in there, and I have to keep telling them, don't. This is deprecated.
**jea** 28:36 So, it looks like Prometheus keeps around their old CRDs, but they probably just don't use them anywhere.
**Mikołaj Świątek** 28:44 Yeah, but, like, is that actually useful for anyone?
**jea** 28:48 Probably a compatibility thing, but… They're not used anywhere.
I think we should just keep… keep it in the APIs package, and then just… Set up a Go check to be like, don't touch this, essentially.
But I think we should just get rid of any references to it elsewhere. Like, it should not be used outside of the APIs package.
**Mikołaj Świątek** 29:14 It's already not used outside of the APIs package. The only thing that does happen in there is, like, schema registration, so it would have to unregister the schema.
And probably get rid of the Cube Builder markers, so it doesn't get stuck into any generation. I also would like to kick it out of the documentation, because the documentation markdown is also too big because of it.
**jea** 29:38 Yeah, we could probably do that. How does Prometheus do this? Because their stuff is way bigger than ours. Like, I don't know… They're suffering.
**Mikołaj Świątek** 29:47 They don't. Their stuff is big enough that you can't apply it, you have to create it.
**jea** 29:52 Oh, that's right, I remember now.
**Mikołaj Świątek** 29:54 Doesn't say…
**Pavol Loffay** 29:55 It's the same.
**Mikołaj Świątek** 29:56 No, no, not… and ours is not… ours still fits.
Not because of that.
**Pavol Loffay** 30:01 All the comments and everything that we could.
**Mikołaj Świątek** 30:04 It fits even with most of the comments, as, like, a recent pull request tried to do, and found that it, like, almost works. But if we get rid of V1 alpha 1, we could re-enable all the descriptions, and it would still fit.
**jea** 30:17 Does Kubernetes have any guidance on this?
Like, do they say anything about the best practice here? I always feel like…
**Mikołaj Świątek** 30:24 Don't make big CRDs.
Or you can also… you can also just make things more complicated and use, like, split your stuff into multiple CRDs and use references.
Good luck.
**jea** 30:42 Yeah.
**Mikołaj Świątek** 30:53 I would personally just delete all of it, if it was up to me. If you guys want to keep the V1 Alpha 1 structs in there, I'm not gonna… I'm not gonna fight for it, but I will, yeah, there's gonna be… I would add some winter check to make sure nobody modifies it, and make sure that it doesn't actually affect anything.
**jea** 31:15 Yeah.
**Pavol Loffay** 31:24 It's easy to keep it there, you just put one QBuilder annotation to skip the, Skip the degeneration, or whatever it is, and then it will not show up.
**Mikołaj Świątek** 31:36 No.
Alright, so we can do it that way. Pavel, I'm gonna hold you to figuring out how much time you need.
From the… from the beds, okay?
Alright, so… you can, you can read the issue for, like, the exact steps. I'm also gonna pin this issue once we decide on the exact timeline, and… and I merged, Feature flag request.
**jea** 32:05 Boop.
Right.
Other thing that I wanted to bring up, I don't know if I have it in the agenda.
**Mikołaj Świątek** 32:12 I have… I have one more point on the agenda, so you have to… There's another… there's another change in the collector, which is not released yet, but will be soon, in 1.52.
Which, again, breaks the telemetry.
It doesn't actually break the telemetry, it fixes a bug.
But the bug fix is such that.
**jea** 32:40 the.
**Mikołaj Świątek** 32:41 The bug was that their default configuration was different depending on whether you set the host explicitly or not.
If you didn't set the host explicitly, you got the normal defaults. If you did set the host, you get different defaults. And we do set the host, so we got the wrong defaults, and now the defaults are right.
And the defaults change the shape of all the telemetry.
like, there's stuff like Prometheus, are there units, is there scope info, is there a type suffix? So, if you had, like, something something total seconds, now the total disappears, and so on.
So the question is, what are we doing? Are we just setting our own defaults, so we keep the old behavior, or are we trying to do a breaking change where we normalize on what the collector is doing, is the question.
Or do we do a feature flag? If we're gonna break this, we should do it with a feature flag, definitely.
**jea** 33:49 I just feel like the last time we did this, it was fraught, and everybody was mad at us.
**Mikołaj Świątek** 33:56 I mean, no, no, in this case, the change for us is really, really simple.
Because we always just set the host, so we would also always just set the, whatever, free additional values, and our behavior is gonna stay the same. Like, this is, like, we would make explicit what is implicit right now, and the change would be simple, there wouldn't be, like, there's no need to convert this, okay?
**jea** 34:19 Yeah.
**Mikołaj Świątek** 34:20 It's only defaults.
**jea** 34:22 Okay, simple.
**Mikołaj Świątek** 34:23 for us. It's just a question of what do we want to do about this in the longer term.
**jea** 34:28 I think, initially, we should just default to… so that we continue the same behavior, and then if the user provides any values, then we override what we have, and that's probably enough.
Maybe we feature flag it, So that somebody can just disable it entirely, but… I don't know if anybody's really wanted to do that. To me, to me, like, them overriding their config would be a better way to override this behavior, but…
**Mikołaj Świątek** 34:56 I mean, yeah, I've… I ultimately kind of want to have the same behavior as the collector does.
It's just that I don't want to break users without, like, a very… or, I don't know, maybe the feature flag is stupid, like, they can just… I guess the feature flag has the benefit that you can set it once on the operator, and then don't have to go change all of your collectors everywhere.
**jea** 35:24 Hmm.
**Mikołaj Świątek** 35:26 So I would do a feature flag. I would do a feature flag which says.
You know, use actual collector defaults, or whatever, and then… If the feature flag is not set, which is right now, just set those things explicitly to the different values that we currently effectively have.
And if the feature flag is on, then just don't set them. Let the collector do what it wants. It's gonna be annoying, because this actually affects our integration… our end-to-end tests.
**jea** 36:01 Yeah.
**Mikołaj Świątek** 36:02 end-to-end tests, we check a bunch of those.
It's annoying.
But it is nice that our tests cut it this time, so this time we know ahead of time that there's breakage coming.
**jea** 36:16 Yeah, good to see our tests working.
**Mikołaj Świątek** 36:19 Pavel, do you have an opinion?
Nope.
**Pavol Loffay** 36:32 I was just… I had just one idea, going back to the splitting the instrumentation.
webhook. So we had, as well, users reporting that the instrumentation webhook kind of consumes More memory on large clusters.
If we split it and there are users that don't use… The instrumentation part, they could… easily disable it.
To have a leader, kind of, at least a collector, controller.
**Mikołaj Świątek** 37:03 And we should also make that webhook not use any, like… big, big, internal caches.
That would also improve the memory consumption a lot.
**Pavol Loffay** 37:18 Yeah, maybe that's another point, we could optimize it more for the… Injection use case, and don't… Kind of fill in the reconciler cache.
**Mikołaj Świątek** 37:29 Jacob wanted to do that with the… alongside the refactor, which is the time… the clock is ticking, Jacob.
**jea** 37:36 I know, that's my update, is I'm beginning the instrumentation refactor next week.
I have time, I have cycles, I can do it.
**Mikołaj Świątek** 37:45 You, you got, you got your, you got your coding agent fired and ready to go?
**jea** 37:50 It's, up and running. Not right now, but it will be.
Yeah, I'm reaching out to Arthur to, coordinate the larger, like, injector refactor as well.
So, because he wants to be involved with that.
**Mikołaj Świątek** 38:20 That's what you wanted to talk about when you… in the…
**jea** 38:22 Yeah, so I just wanted to say, hey, I am beginning this work, you will see PRs from me, because I knew that you were going to mention it.
**Mikołaj Świątek** 38:30 I actually wasn't going… you reminded me. You reminded me, but I wasn't going to.
**jea** 38:34 Yeah, right.
**Mikołaj Świątek** 38:38 So there's another thing I would like… I would like to humbly ask for assistance with the security advisories.
Because we have, like, two security advisories filed.
We have, like, an original report, which has two of them in the same report, and then separately someone else filed the same ones, but they filed them as separate, so I… I got pinged by someone about this, so I, like, redirected, added the new reporter to the older advisory, and so on. And so… the NGINX HTTPD thing is fixed as of the next release, because I fixed it. The only question there is, like, one of the reporters is asking for a CVE number, and I have no idea what the process for this is.
**jea** 39:25 I also don't know how to do that.
**Mikołaj Świątek** 39:28 And I don't…
**jea** 39:29 that other one?
**Mikołaj Świątek** 39:31 The other one is the fact that you can use the collector CRD to get a bunch of permissions, scary permissions, on the node.
Which is, in an intended use case, and it's probably, like.
If we're gonna do something about this.
I think that it should proceed kind of like… a documentation, like, put a warning in the documentation saying, hey, if you give someone the ability to create this, they might take over your node, you know, this essentially is the same permission as, like, making… letting them make arbitrary pods.
**jea** 40:09 Yeah.
**Mikołaj Świątek** 40:11 So be careful about that. I don't think a lot of our users are doing anything like that, so it probably doesn't… doesn't make that much of a difference, but the first part is, like, putting a warning, and the second part, which was, like, proposed by the reporter, was essentially… Make it so that you can set all these… the scary fields only in, like, a namespace that is specifically labeled.
For that.
**jea** 40:42 Yeah.
Something like that sounds good to me.
I think just docs would probably be useful.
I mean, maybe I trust people too much, but I feel like that they know when I was, like, an operator of a cluster, it's like, I know the security risks involved with installing things. I kind of assume that other SREs are smart enough to know that as well, but maybe I can make that assumption.
**Mikołaj Świątek** 41:07 Like, if they're doing something like running the operator and letting various users create their own collectors, they… they might get in trouble.
**jea** 41:15 Yeah.
**Mikołaj Świątek** 41:17 I agree with that.
But it's also the case that tons of operators do this exact same thing.
Like, they let you do, like, ads.
You know, host, whatever, whatever those volumes… host path? Host path volumes, right?
Yeah, I let you add host map volumes to your, like.
**jea** 41:42 Yeah, yeah, yeah.
**Mikołaj Świątek** 41:43 Damon set, and, and, you know.
That's enough to… to get all sorts of… all sorts of information about the node, for example.
But the question to me also is, we don't have to decide right now, but we can talk a little bit, like, if… if we're going to argue about, like, what the severity of all of this is, what should we argue? Because the guy put in critical, and I kind of disagree with that.
**jea** 42:13 I also…
**Mikołaj Świątek** 42:13 I don't think this is, like, something everybody should, like, immediately go, oh, no, no, no, no, my cluster is gone, right? It's like, be a little bit careful with this stuff, because it's powerful by default. It's essentially the takeaway, right? So it should be, like, a medium, maybe? Maybe.
**jea** 42:32 I think a lot of these CVEs, honestly, come from security researchers that are just throwing, like, AI agents at every operator in every Kubernetes project.
And a lot of them are just like, yes, of course, this is a critical vulner… congratulations, you've found a critical vulnerability. You know, it's like, I think there's an amount of this that is not done with, like, I don't want to say good intent, but it… it's not security research as much as it is, like.
Security automation, or, like… AI security slopification or something like that? You know, it's like… like, I got one that was… someone was like, if you use the operator to do this, if you give… if you choose to give this permission to the operator, then you have this permission. And it's like, it's not a vulnerability. Like, you gave yourself the permission, like…
**Mikołaj Świątek** 43:30 Kind of, and with the instrumentation one, it's also the case that Being able to do what they say, while it's kind of, like, sloppy that we let this happen, it doesn't actually let you really do anything you couldn't do anyway.
it's just, like, you could, you could have just, like, provided your own custom NGINX instrumentation image, which did the code, did whatever you wanted. It's just that, like, being able to use a shell script is, like, just way easier.
But the fundamental, like, the instrumentation CRDs exist to inject code into pods.
So yeah, if you have control over one, you can probably inject arbitrary code into a pod.
Right.
**jea** 44:19 Yeah.
**Mikołaj Świątek** 44:22 Right, my, my, my question, or my kind of request is basically so… so you, like, have a look, have a look at those advisories.
As well.
**jea** 44:34 Yep. Can you send them? I tried to find them in the issues tab.
**Mikołaj Świątek** 44:37 You're… If you go to Operator.
to the operator repo, and you go to… what was it? If you go into security.
**jea** 44:48 No, I went to, like, the security advisory thing, and I couldn't find them.
**Mikołaj Świątek** 44:52 I'm gonna send you a link where it's, like, where all of them are.
**jea** 44:57 No, I'm looking there, it's just that the organization of this is terrible.
Where I don't see, like, the one that I was just looking at, you know?
**Mikołaj Świątek** 45:11 I don't know, I don't know what… what… I don't know how to help you, Jacob.
**jea** 45:15 I'll show you. You show me where I'm… where I'm messing up.
**Mikołaj Świątek** 45:18 Okay.
**jea** 45:20 This one, yeah. Can you see my screen here?
**Mikołaj Świątek** 45:26 Yes.
Security… it's under Advisories, to the left below.
**jea** 45:34 There it is.
Thank you.
It was this one, right?
**Mikołaj Świątek** 45:42 Yeah.
But I feel like we should… this should exit triage for… for one. Like, we already know.
**jea** 45:52 We can have it at Exit Triage.
**Mikołaj Świątek** 45:55 But I don't know how to do any of this. I very definitely do not know how to assign a C… how to ask for anyone for a CVE number, for example.
**jea** 46:06 We can, you can change that. If you press the edit button.
You can change all these things.
**Mikołaj Świątek** 46:13 Alright.
So, what kind of… what kind of severity do we think we're looking at here?
**jea** 46:20 I think, like, low to moderate, probably.
Maybe moderate.
**Mikołaj Świątek** 46:28 Dave, what do you think?
**Pavol Loffay** 46:32 No doubt if he means, jacob.
12 to moderate.
**Mikołaj Świątek** 46:39 Alright, and I would… I would say both of them are moderate, honestly.
**jea** 46:43 Yeah.
**Mikołaj Świątek** 46:44 I think the NGINX one is honestly kind of low-ish, but also the… it makes messing with it… Much easier.
much easier. So, in that respect, I am okay with moderate.
Neither of them are critical. Neither of them are things that somebody needs to drop everything they're doing and, like, you know, go patch stuff.
**jea** 47:08 Yeah.
**Mikołaj Świątek** 47:23 And I'm just going to… so, like, the remediation for this finding after cluster node takeover is going to be that I'm going to file an issue about, like, restricting certain things.
Unless there's a namespace label, or whatever, and we're going to start with just going to update documentation saying that people should be careful about letting everyone in their cluster create OpenTelemetry Collector.
resources.
Does that sound about right?
**jea** 47:52 Yeah, yep.
**Mikołaj Świątek** 47:54 Okay.
I'm gonna… Note these.
in the… In the thing here.
Probably it might be… Might want to ask the original reporter to actually split his report into two different reports, because they are actually different, and one of them is already One of them is already fixed, while the other one is going to take more time, because it's more like a feature request.
that I think about it, I shouldn't be putting this in a private document, should I?
**jea** 49:04 Probably not.
**Mikołaj Świątek** 49:06 Deleted.
I'm gonna put it… I'm gonna put it in our Slack channel.
**jea** 49:14 Yep.
**Mikołaj Świątek** 49:20 Okay, do we have anything else we need to talk about?
**jea** 49:23 Do we go over all the disgusted sick things? Definitely not. Jeez.
**Mikołaj Świątek** 49:31 But some of them we have gone… like, the V1 Alpha one we have.
For example.
So, that's out… The nightly test we have talked about, because this is just… this is the collector.
Telemetry breaking change?
Webcook high availability, yes.
the supply chain security hardening. We might want to talk about this a little bit.
How do you guys feel about it, in general?
**jea** 50:11 Which one? The security hardening one?
**Mikołaj Świątek** 50:14 Yes, yes.
**jea** 50:15 I… I want this person to start with something a bit… I want them to finish up that.
What's it called first?
The… SBOM stuff that you had to revert?
**Mikołaj Świątek** 50:31 I mean, yeah, that's part of it. Like, that issue covers that, and, like, also a bunch of other things.
Yeah. My basic question was that, do we actually want to do this?
In the end.
**jea** 50:49 I think… person is, like, offering it. Yeah.
**Pavol Loffay** 51:05 Is this, like, a requirement from CNCF or anyone?
**Mikołaj Świątek** 51:09 No.
**jea** 51:10 No, it's just good security posture stuff that'd probably be good for us to do.
**Mikołaj Świątek** 51:16 Yeah, like, we sign images, we provide a bill of materials using some, like, standard tools, essentially.
I don't see any particular reason to say no if it, like, doesn't require us to do anything special.
**jea** 51:37 Yeah.
**Mikołaj Świątek** 51:38 Overall.
**Pavol Loffay** 51:39 It's releasing too much.
Hang with it.
**Mikołaj Świątek** 51:42 Yeah, it should all be automated, and I specifically asked in that pull request that at least as much of it as possible is also, like.
executable locally.
And it does work. I did check it. It's just that one of these things is, like, a weird GitHub Actions from, like, SLSA, which actually failed on main.
**Pavol Loffay** 52:04 there was as well, a bunch of tools used locally. I didn't run it, so maybe I'm wrong, but there's a bunch of tools with different versions, and… I would prefer if it was, like, simpler, maybe, like, one tool that I can run.
**Mikołaj Świątek** 52:21 I would prefer that as well, but I don't know if it exists.
I think maybe we can start with just a piece.
of this?
like, just… let's just do the signing, right? Let's just do… we… we publish, we sign the image, it goes into the SIG store.
**jea** 52:45 Yeah, I agree. I mean, I think it would be good for us to have that, regardless.
**Mikołaj Świątek** 52:52 And signing… doing signing locally is very simple. I try that.
**jea** 53:04 Yeah, and what was the problem with signing? I saw that you reverted it. It looks like it got past more steps than last time, though.
**Mikołaj Świątek** 53:11 I don't know what the problem is, actually. I think some of these… I think one of the… there's a GitHub action in there for the SLSA stuff, and that GitHub action is doing some weird stuff.
And… I'm not sure why it's failing, exactly.
Because it's the kind of funny GitHub action where it has steps which fail, but also shows up as green in the GitHub interface, so… it's not that easy to understand. And I had, like, an hour for it to try to fix this today, and in an hour, I failed, so I decided to just revert it, especially since I will do a release tomorrow.
There's… there's a phase 3 here.
in the supply chain security, because the rest of the stuff is kind of like, you know, pin your GitHub actions, run the OSSF scorecard, sign and do a bill of materials, whatever. Like, these are all things that are kind of, like, doable automatically.
There's just a bunch of tools that run.
Yeah.
The third part is, like, publishing… statements for non-exploitable CDEs.
And I'm like… I don't… I don't want to do that.
I have better things to do with my life than publish, like, a statement for every single CVE in the Go Standard Library, or whatever.
Like, it's already a pain enough to deal with the stupid Docker dependency, which is, like, literally, that CVE is completely not… exploitable in any, like, normal use of it. Like, there's a CVP in the server of Z, And everybody uses that package just for the client, and then there's, like, a bunch of people going, like, oh, my security scanner is flagging you, you know, why don't you update?
Alright.
I don't want to deal with that times 10.
**jea** 55:30 Yeah.
**Mikołaj Świątek** 55:32 So, I'm gonna… I'm gonna… for phase 3 of this, I'm just gonna ask this… Contributor to show me how that looks in practice.
**jea** 55:43 Yeah, yeah. I mean, this is something that would be good to have. I remember a while ago, I was like.
Sony reported the thing about the unknown unknown… Container image, and then this is, like, the real solve for that.
**Mikołaj Świątek** 55:56 Yeah.
Yeah, and I think that's it.
The rest of this is… Because, like, what I said right now, I already replied under that issue, so we don't really have to… do anything.
And the rest is, like, manage CRD feedback… Oh.
And the stupid go auto-instrumentation thing, which I just don't want to think about.
**jea** 56:35 Yeah.
**Mikołaj Świątek** 56:41 And that's it.
So, do you have anything else remaining?
**jea** 56:47 Don't think so.
**Mikołaj Świątek** 56:53 Okay, cool. In that case, we are done.
**jea** 56:56 Cool. Good stuff. Thanks, everyone.
**Mikołaj Świątek** 56:59 Thanks, have a nice evening, afternoon, rest of your day.
**jea** 57:03 Yeah, you too.
**Mikołaj Świątek** 57:04 Yeah.
**Israel Blancas** 57:04 But…
