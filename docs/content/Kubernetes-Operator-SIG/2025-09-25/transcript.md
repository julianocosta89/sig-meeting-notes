SIG: Kubernetes Operator SIG
Date: 2025-09-25
Duration: 49 minutes
============================================================

## Zoom Recording Transcript

**jea** 01:40 Hello!
**Antoine Toulme** 01:42 Hey, man.
**jea** 01:44 How you doing?
**Antoine Toulme** 01:46 But every day.
**jea** 01:48 Better every day, that's good to hear.
Let's see…
**Antoine Toulme** 01:53 I got… I got crank in my neck or something, it's not fun, but…
**jea** 01:57 No?
That stinks.
**Antoine Toulme** 02:01 Not fun at all.
**jea** 02:03 I also hate… I hate when you also, like, sleep on your back weird, and then your back is just, like, you can't get comfortable all day, you know what I'm talking about?
**Antoine Toulme** 02:10 Yeah, no, there's no way you're gonna survive this life.
Like, you can try, but it's not… It's not gonna happen.
I'll see you at KubeCon, right? Yes, I will.
**jea** 02:22 Yes, indeed.
**Antoine Toulme** 02:24 the…
**jea** 02:26 When did the format for the meeting notes change?
**Antoine Toulme** 02:30 I'm sorry, I'm just not… I don't know.
**jea** 02:35 It just looks different. It looks like someone went in there and, like, messed with the formatting.
I don't know.
**Antoine Toulme** 02:40 Have you ever seen the JavaSig Notes documentary?
**jea** 02:43 and…
**Antoine Toulme** 02:44 It's a work of… it's a work of art. They use different fonts.
**jea** 02:49 But…
**Antoine Toulme** 02:49 They use different fonts for everything, it's so beautiful, oh my…
Someone is trolling lightly the SIG or something, like…
Hey everybody, hey, we see, people here.
It's great to see you, folks.
Welcome, welcome.
**Mikołaj Świątek** 03:06 That's tough.
Hmm.
Why do you want to wait, like, 10 more minutes or something?
**jea** 03:28 Yeah, we can wait 2 minutes, maybe.
**Antoine Toulme** 03:30 We got the notes somewhere?
What do we have to talk about today?
Okay, we got finalizer…
**jea** 03:49 Hmm.
**Antoine Toulme** 03:59 I've been hounding one of my devs, she's been working on the CRD that I…
blabber about for months now. I'm going to put up… a link…
To the work that she's been doing, because I don't understand why it's not already happening in the PR.
**Mikołaj Świątek** 04:22 Yeah, the finalizer's discussion was opened by Vincent de Bois.
What I don't see here, or, right, or is… is there a representative?
Is this, but that's me.
**Mátyás Végh** 04:37 Matthias.
Yes, hi. Hi, y'all.
**Antoine Toulme** 04:40 Hello.
**Mikołaj Świątek** 04:44 Alright then, please, you know… Okay.
**Mátyás Végh** 04:46 Yeah, okay, I wasn't sure how these go, so I didn't want to… okay, step on it.
**Mikołaj Świątek** 04:50 We are not… we are not very… we are not very formal, are we?
**Mátyás Végh** 04:53 Okay, okay, no worries, thank you. Yeah, so, I'm from Ericsson, and yeah, I work with, along with Vincent.
**Antoine Toulme** 05:02 Antira, who I think posted the, the, the, the, the issue, in the agenda.
**Mátyás Végh** 05:08 So, in essence,
Yeah, we… we have the… we're trying to take on the telemetry collector operator along… into a lot of our applications.
And the standard sort of deployment model that we have is that we go out onto, you know, to the customers, and they point us at a namespace, and that's the namespace that we get to use. So we don't get two namespaces, we don't get three namespaces, we don't get the entire cluster, we get a namespace.
So pretty much everything that we do is namespace-bound,
We can, of course, get our CRDs installed, but that's usually a little bit of a pain, because then we need to get a different team involved out on the customer site, who actually has the privileges to install the cluster-wide resources.
But we… but we can get that done, that's… that's fairly straightforward, and…
Because… because we're pretty much installing one thing at a time, the entire application at a time,
it's all installed and upgraded and uninstalled, if needed, together. So, one of the things that our customers are using and has thus far not given us any major headaches, is we should be able to delete the entire namespace.
And, so long as the operator and the custom objects all live inside of the same namespace, if you delete the namespace, that's going to be, essentially an unordered delete of these two things. So, it's going to be a race condition of which one is actually going to get deleted first.
You can play around a little bit with termination grace period seconds, but it doesn't really do the trick. It's still… it's still quite racy. You know, half of the time, the custom objects get deleted first, and half of the time the operators do, so… not ideal.
And so I'm sort of here to, you know, hopefully to understand better how the operator is employing finalizers, and assuming that my understanding of how that works today is correct, then hopefully I can argue against that type of use of finalizers, but…
We'll see how far I can go with that. Yeah, so…
My understanding today is that when the telemetry collector see, you know, when this telemetry Collector operator is running, and it notices that a custom object, I forget the name, but I guess it's going to be something like OpenTelemetry Collector gets created, then it will respond to that and create, you know, start creating the deployments and the config maps and everything that constitutes the actual telemetry collector, the, you know, the actual instance.
And then depending on mode, you know, it either patches sidecars, or it creates a deployment, or a stable fillet, or stuff like that.
And if it gets patched, if the custom object gets patched, then again, the operator will notice, and then it will apply those changes again. And if it gets deleted, then it would like to do some cleanup action, right? I mean, if it would like to uninstall the generated resources. So long as everything is namespace-bound.
Owner references would be straightforward enough for the newly created stuff, but it's obviously not sufficient for sidecars, because you can't… you can't garbage collect a sidecar.
But in the… but for the use case, at least, of a namespace delete.
Well, it doesn't really matter anyway, because it's… the whole thing's dead. But if you were just uninstalling the custom object, you would like to be able to get rid of the sidecars that have been rolled out everywhere. So there definitely is a need for cleanup, but I'm not seeing finalizers as actually being necessary to perform proper cleanup.
So, you know, you could scan all of the things that you've attached sidecars to and see, you know, is the sidecar
Sorry, is the custom object that required the installation of that sidecar still there? Because if not, then in the next reconciliation loop, you can just remove the sidecars. So even for that, I'm not seeing a…
a selling motivation for the finalizers. So, yeah, I'm wondering if I'm…
Understanding your use of finalizers today correctly.
**Mikołaj Świątek** 09:34 Agenda before.
**Mátyás Végh** 09:36 So I don't know if I have to say, you know, please interrupt me, whatever.
**Mikołaj Świątek** 09:40 So…
I don't think we actually do anything special for sidecars, because we are actually unable to clean up sidecars. We would have to… the only way to remove a sidecar from an existing pod is to recreate it.
And we're not gonna mess with, you know, other workloads in the cluster. So, sidecar… if you delete the sidecar CRD, it just stays until that pod is restarted, and that works.
In that respect, it works the same way as, like, anything that is injected via a mutating webhook.
So… so that's not actually a problem, and we don't wait for this, because it's… it's an unbound amount of time, completely.
The only reason we have finalizers right now, and the only thing they do, is basically just clean up,
Cluster-scoped resources.
And we do create some cluster scope resources conditionally. More specifically, if you enable an option to create, airbag.
resources, then those are sometimes cluster rows and sometimes cluster role bindings. These are bound to, like, an open telemetry collector CR, and
That's what it's used for. And I think that's the only thing it's actually used for.
And in that respect, I think it's…
Well, not exactly unavoidable, but it is…
correct that we should wait until everything is cleaned up before we complete the deletion of, like, a collector CR. But it is also true that if you uninstall the operator before you do that, then it's not actually gonna happen.
So…
I wonder… I wonder if there's, like, a fix. So, it's definitely possible for us to do something like, just don't add the finalizer if it's not needed, because right now it's added unconditionally.
**Mátyás Végh** 11:45 Yeah.
**Mikołaj Świątek** 11:45 Like, if you don't have that option enabled, it just does nothing.
**Mátyás Végh** 11:50 So…
Yeah, so the thing that, yeah, I don't know if I'm answering the question, so yes, the namespace delete hangs, I don't know if that's… if I made that obvious. The namespace delete hangs, because there are objects within the namespace, namely the custom object, that still have a finalizer present. You know, the modeling trying to be that the operator has not yet had a chance to perform the delete.
You know, and to do the recursive delete. And therefore, we don't… we want to inhibit the deletion from continuing so that the operator still has a chance.
This is fair enough, but the operator is already dead at this point, so it's not actually going to help.
Once the operator has died.
it's an entirely moot point of whether, you know, if it then ran again, whether it would actually be able to clean up. So, for my money at least, the finalizer has not really accomplished anything, because if the operator is still there.
because it survives, it would be able to clean up those cluster resources anyway.
Because the next time the reconciliation loop runs, it can see, okay, are there any further cluster scope resources that I have created that no longer have a reason for existing? So you could, you know, add a label or an annotation or something like that to the cluster role, saying, you know, this was created on behalf of the collector foo.
And then, if there's no such foo anymore, then, yeah, you can just clean up.
So, you still don't get immediate cleanup by adding the finalizer, because…
I mean, the custom object is kind of deleted anyway, but it's not been reconciled yet, so it's not immediate.
And when the operator sees, sees that deletion next, it will be able to reconcile… it will be… it would be able to clean up anyway, so I'm not really seeing how much better your, yeah.
you are with the finalizer, but it definitely makes things worse once it's gone. So I'm wondering if it wouldn't perhaps make more sense, because… so the thing that I'm thinking about here is.
And with normal, I say normal, so if it wasn't a cluster resource, if it was just a deployment, let's say, you had a deployment for the telemetry collector.
then an owner reference just solves the problem all on its own, right? The custom object disappears, and then you've got an owner reference, and garbage collection will take care of it, and it's nice. The only reason we can't use an owner reference here is because you can't have a cross namespace owner reference, which is okay, it's a pain, but…
When exactly is the operator, you know, dead, as it were? Because the only way that the telemetry collector operator was able to create that cluster role is if it already had another cluster role.
Right? Because you have to have a cluster role to create a further cluster role. And so I'm wondering if that more root cluster role shouldn't be the actual owner of all of the subordinate cluster roles. And so when you finally uninstall the operator by whatever mechanism that you might have that's perhaps more thorough than a namespace delete, that could clean up everything.
But again, I would… I would say when the operator runs again next, it can still clean up, even without the finalizer.
But I don't know if that…
**Mikołaj Świątek** 15:05 principle. In principle.
**Mátyás Végh** 15:07 I don't know if that's obvious of how that is, because I have the sketch in mind, but I don't know if I've explained that well.
**Mikołaj Świątek** 15:12 You do have to track it somehow.
**Mátyás Végh** 15:15 Yes. So, the finalizer slash on-delete approach has the benefit that's very simple.
**Mikołaj Świątek** 15:22 Because you implicitly know what you generate.
for a given collector. If you… if you don't know what that is, you have to have some kind of…
More elaborate mechanism for tracking what was actually created.
Which I am not against. I am personally, at least, I am not married to finalizers, and I also don't like them very much, for reasons that you've, you know…
elaborated upon. They're… they're kind of blocking in an unpleasant way, but it is also true, it is also true, that
If you delete the operator.
and you have non-namespaced resources created by it, those will not be cleaned up. Like, that is… that is still a leak that you have in your system. If… if you have that enabled, if the operator creates those, like, whether finalizer, non-finalizer, whatever mechanism, they're gonna
So…
**Mátyás Végh** 16:23 So, so let me…
**Mikołaj Świątek** 16:24 That is expected.
**Mátyás Végh** 16:26 Yes, that is true, but then let me ask, sort of turn the question around. If I… if I installed the operator itself, the operator itself is sitting in some namespace somewhere, right? It has its own deployment, or, yeah, for the operator itself. But the operator itself has a cluster role.
**Mikołaj Świątek** 16:43 Nope.
**Mátyás Végh** 16:44 Because otherwise, it wouldn't be able to provision further cluster roles. So if it has that cluster all, and I just delete the namespace of the operator, I've still leaked that cluster role.
So, by whatever mechanism I'm supposed to uninstall the operator properly.
you know, it could be a Helm uninstall, but it could be some other process, I don't know what is most common for, you know, in the community. But whatever deletion routine there works would necessarily need to delete that single cluster role.
And so, upon creation of the further cluster roles, those could be bound to that single cluster role.
And then, if there is a proper delete of the operator, that would create, you know, that would eventually remove all the indirect ones. But I don't have a strong opinion on how to clean up the clusterals, because…
you know, we're not using the cluster roles in the first place. For us, it's all namespace-bound anyway, so which direction you go on that is less exciting for us.
But then, yeah, I do think it makes sense that the finalizer be conditioned on, whether there are any cluster resources bound to it in the first place, because if not, then it's completely, yeah, it's just in the way.
**Mikołaj Świątek** 17:59 I'm absolutely okay with making the finalizer conditional.
**Mátyás Végh** 18:04 Personally. Okay. So, yeah, so the reason I want to make that
check is… because I think we are currently sort of playing with, patching out that finalizer, but it would be nice if we could express this more, you know, properly, and it's not so much that we want to disable finalizers, it's more that we want to disable cluster resources, and so it is a logical consequence from that, then, therefore, you don't need the finalizer. But yeah, I think I… I think I follow.
**Mikołaj Świątek** 18:31 Jacob, Antoine, opinions?
**jea** 18:35 I think it's fine if we disable the finalizers. I mean, we get a lot of, like, annoyances from them.
For sure. I definitely see a fair amount of people complaining about them. I think, as Mikolai said, like, we do need them for, like, you know, the reasons stated.
But, obviously, if we're not actually taking advantage of the features, there's no reason for us to use them. So, I am very okay with getting rid of them. I wish that we could just do owner references. That would make life so much easier, and, like, it fits into the logical system so much better. It's frustrating that we can't.
But that's the nature of it, right? Like, we can't do much about that, unfortunately. So, I think it's fine to get rid of them. Is that something that you would be able to contribute, or is that something that you're seeking, someone to contribute themselves?
**Mátyás Végh** 19:24 I don't… I'm not necessarily in a position to answer that question myself. I don't know, Eturo, if you can…
Say, but if not, if we can't say, then we'll get back to you on that question.
**jea** 19:35 I mean, it should be a small fix, more asking, like, are you looking for somebody else to, like, hop in here and do it, or is this something that… you said you already did a patch.
**Mátyás Végh** 19:45 I understand that we have kind of done that on our end anyway, but I don't… it's not… it's not for me to say. That's not my team, so I don't want to commit in that end, but I think it is likely that we should be able to do this, but I need to get back to you on that.
**jea** 20:00 Okay.
**Mátyás Végh** 20:01 Yeah, totally. I can have been sent a confirm on that, depending on which, yeah.
**jea** 20:06 Yeah, and obviously, I don't need an answer right now. More just, checking if that's, like, a thing.
**Mátyás Végh** 20:12 No, that's, that's fine, thank you, yeah.
**jea** 20:14 Cool. Well, yeah, just keep us up to date in that thread. I'll… You can tag one of us in there if you need anything else.
Anton, did you have thoughts?
**Mikołaj Świątek** 20:24 Actually, I'm actually… I didn't know that you could make… you could make a cluster role an owner of another cluster role.
**Mátyás Végh** 20:31 Can you know?
**Mikołaj Świątek** 20:32 I think you can, but I've never tried.
**Mátyás Végh** 20:37 I'm not trying to… yeah, I'll check, because the only restriction that I'm aware of is that you can't have cross-namespace owner references, but a cluster all… that wouldn't be a cross-net, that should be fine.
**jea** 20:48 I was pretty sure that you couldn't do owner references on cluster… on cluster scoped resources, but that might be an outdated, like, Kubernetes thing of my knowledge.
**Mikołaj Świątek** 20:57 I am quoting, I'm quoting documentation. Cluster scope dependence can only specify cluster scope owners, so… presumably you can. Presumably you can.
Like, that doesn't actually solve the problem. Like, that doesn't actually solve the full problem, right? Because that solves the problem that if you delete the whole thing, it will also delete everything else.
**Mátyás Végh** 21:18 Yes.
**Mikołaj Świątek** 21:18 But it doesn't solve the problem that if you delete a particular CR, it should also delete everything that CR created, right? Right, exactly. But it does… it does solve the… I delete… I, you know, I delete everything at once.
Yeah. Which is nice.
**jea** 21:34 But wait, what would the cluster resource… that would be the owner… because I don't think the operator, by default, has a cluster…
**Mátyás Végh** 21:40 Yes, it does, because it needs to have a cluster… it needs to have a cluster role to entitle itself to provision further cluster roles.
**jea** 21:48 True, true, true.
**Mikołaj Świątek** 21:49 That… that might not exist by default.
**jea** 21:52 Yeah, exactly.
**Mátyás Végh** 21:55 Yeah, yeah. And so this whole game…
**Mikołaj Świątek** 21:57 Love it.
I think there's some way to know from a program, like, what your,
some… whatever that API is called to be able to tell where your permissions are coming from. Like, there is something like that. So it should be possible to do it.
Yeah, but, I guess it sounds like… sounds like we're clear, at the very least, we're… we're in agreement that… that…
the finalizer shouldn't be used unless it's actually necessary. So, you could definitely… you're definitely free to submit a fix changing that.
Pretty simple.
**Mátyás Végh** 22:48 Okay, great, cool.
**Mikołaj Świątek** 22:51 Yeah.
**Mátyás Végh** 22:52 Just a paperwork question. Are you guys writing moms? Am I… I don't know what the,
code is here. I don't want to write in someone else's name in the… in the minutes.
**Antoine Toulme** 23:05 Oh, go for it.
**Mikołaj Świątek** 23:07 Feel free. Feel free to write in the minutes.
**Mátyás Végh** 23:10 Okay, thank you.
**Mikołaj Świątek** 23:11 Can't tell them.
**Antoine Toulme** 23:16 Yeah.
**Mikołaj Świątek** 23:16 Alright, second item is about cluster observability documentation, but I'm not sure who.
**Antoine Toulme** 23:22 Yeah, so, I mentioned to Gina that this meeting was ongoing, and she graciously,
accepted to join us. And so Gina has been working really diligently on this effort. This is an effort that we have been…
working on for a while. There's been an RFC about this, to just go about it from a product requirement point of view.
This is a bit more about the design, and if you look in that branch, you'll see that she's been working also on the actual, kind of, making that come together.
So, yeah, Gina, do you want to talk, or should…
Let me know.
**Jina** 23:59 Yeah, sure.
So, for now, I just have, like, I guess…
a somewhat running POC, controller. And, I think, like, my next step was going to be, you know, just…
start with the PR, with the design doc. I'm not sure if Antoine has that in the doc, but, like, I can just share a markdown I've written for the cluster observability thing.
**Antoine Toulme** 24:27 Yeah, I just shared the MD, the Markdown doc that you have, which I think is great for discussion.
**Jina** 24:33 Okay. And…
**Antoine Toulme** 24:35 Put it in there.
**Jina** 24:36 Yeah, and I mean, this is like a controller from scratch for something which is, you know, very, I guess it's going to take over your entire cluster's observability, so it's going to be very, opinionated, so it's difficult to design it, for sure. So I'm just…
like, I guess, how do you… how do you folks think we can, you know, make some, meaningful progress or meaningful discussions, about this? Like, should I just start creating PRs? Maybe I can put down whatever I have in the POC branch, bring it, you know, just.
**Antoine Toulme** 25:13 Absolutely.
If you bring PRs, I will approve them, and then, you know, Nikolaj and Jacob will slowly lose their minds, and they have to fix my stuff. That's how this has been working so far, and I think it really works well for me, I have to say.
So…
**Mikołaj Świątek** 25:31 Be careful, careful, Antoine, there's now a co-pilot reviewer. Pavel has been, like, very… or what was.
**Antoine Toulme** 25:36 Oh, that's true.
**Mikołaj Świątek** 25:37 something, some, there's some, some, some funny… It's pretty slow.
**Antoine Toulme** 25:41 Yeah.
**Mikołaj Świątek** 25:42 Not as fast as me, because I don't even read the changes before approving.
Yup.
**Antoine Toulme** 25:51 Yep, yep. But, yeah, no, that's true, that at least we should, wait, why not play and play and try Copalot? I think this is something we're trying to…
But if you're familiar with the concept of the RFC, right, we wanted to have a way to start to tell people, these are the best practices when you use the operator. Don't come up with your own way to deploy the collector, let's find ways to make it so that it works the first time around, and also kind of start to have the functional coverage that you get from the Helm chart for
Having some sort of an opinionated approach of what you would deploy by default.
So, do you know, do you mind if I share your document right here on the screen?
**Mikołaj Świątek** 26:32 Okay.
**Antoine Toulme** 26:34 Alright, so let's go and talk about that. So, we talked about this in a meeting, I think it was… you might have been out at the time, Mikaj, where we… we talked a bit with Pavel about some of the things, and some of the design considerations we should take.
And this is what, here Jenna has done, which is that instead of having something that defines a number of elements in Kubernetes, we are going to define a number of CRs, which are already part of the operator's ecosystem.
So we're not going to redeploy, like, a deployment of a collector, we're going to use the OpenTeometry collector CR directly.
Because that's a much cleaner approach, because you can have migrations between those different CRs, and from Pavel's point of view, it was less maintenance if we… if we continue to have the same functional coverage and testing that applies at that level. Does that make sense?
Okay.
So, now you have this CR, which is going to be, pretty much, this is… this is it, this is a view of this, right? And, then, that CR is going to define
using the controller here, which is the code component of it, it's going to define additional CRs, which then deploy all those components which are going to live in our cluster.
Right? So what that means also is that you may, if you want, or if you have a need to deploy additional CRs unrelated to this approach, you may want to, and you may have a use case where you'd like to have a separate OpenTime collector that has its own lifecycle as a separate CR.
But for the most part, if you're going to deploy this, then all of this stuff is deployed by default. Now, we're trying to…
We're trying to espouse a view where we have some opinions, so we are…
going for three types of deployments. One is the demand set deployment, which is going to be per node, to make sure that we are able to kind of get kibblet stats and, maybe logs and other things.
Another one is the cluster deployment, which is a deployment of one, usually, and that is going to be talking to the cluster API server. It's going to capture all the metrics and all the information, get all the events, all the objects.
**jea** 28:44 Do we still… sorry, do we still need that? I know that we have, like, the leader election extension now. We could probably keep everything in the Demon set, no?
**Antoine Toulme** 28:52 And the problem I have… I've been having when we talk about that is that some of our customers don't want those demand set at all.
But… you're right. So…
**Jina** 29:01 Gotcha.
**jea** 29:03 Can you expand on that?
**Antoine Toulme** 29:04 Yes, of course. Jeanette, go ahead.
**Jina** 29:06 But, like, even if, like, customers are okay with demon sets, I would argue…
It's better to have the cluster receiver, because, you know, you don't want, like, this one single, you know, daemon set pod to do everything for clusters, because that's a lot of, overload.
Right? You're watching for every object in the Kubernetes cluster, so… I think it's still better. You have leader election with, like, two replicas in the deployment.
But you still have a deployment for that.
**jea** 29:35 Yeah, for the record, like, I think that is the better approach.
I made the change in the KubeStack chart in Helm. Like, somebody wanted to do…
the solely demon set thing with a coupe stack chart, and I was, like, semi-opposed to it for the same reason, but other people were much more for it, because they just wanted to have a single, like, a single collector deployed.
And so… I mean, I see the reasons for and against. Like, I…
Didn't love… and Antoine has heard my rant about this, I think, about just general, like, leader election stuff. I don't love doing leader election if we can avoid it. I just think it's, like, extra work for not much gain. I would… and also, it's not a good scaling approach for, like, something like Coop State Metrics. I would have much rather preferred that we figured out a better way to, like.
actually shard… the cluster receiving in the first place, which they have, like, better…
**Antoine Toulme** 30:33 It'd be neat.
That would be very neat. Yeah, no, I think for now, the other problem we're having is the cluster receiver itself is a huge cache, it keeps everything in mem, so you have a very different requirement in terms of memory and performance for that cluster receiver compared to the demand set.
Yeah. Well, Luke, I mean, we're trying to…
We're not trying to innovate on that structure yet. I think we need to just also just land this so that it functionally works, but I'm happy to make sure we… In a sense, what's kind of neat about this is that since everything is controlled from here.
you can decide later to make some breaking change where you start, okay, no longer cluster deployment, and make it part of a demand set, and the customers don't care. It's just an update.
**jea** 31:15 Yeah, I think with that in mind, there is an interesting question in terms of, like, testing here. Maybe I'm getting ahead of myself, and you could say we're gonna get to this, but…
**Jina** 31:26 I just want to preface this, this is, like, a really, sort of, like, a dirty design. I just, like, took 3 use cases which I thought I could implement in a POC. Nothing is, like, set in stone, everything is, like…
We should discuss all of these design questions, etc. So, just FYI.
**jea** 31:43 Yeah, for sure, and I do appreciate the work here. This is, like, really helpful in understanding what, what is actually going to be done as well. The thing that I'm wondering is when it comes to testing, I think it would be great if we could
do some sort of, like, capture of, here are all of the… here's all of the telemetry that we expect for each of the, sort of, valid configs here, of which there aren't many, so that when we do a breaking change, it's clear what we're losing in between those versions.
**Antoine Toulme** 32:13 Yeah, you want functional tests that actually check that we still get the right things, if we change our minds about stuff. Absolutely, yeah. Actually, that's probably the… continuing the tradition of having good end-to-end tests.
we could probably… so we've done that for our own Hampton use cases, where we try to have kind of a functional coverage of what we do. It gets a bit unworldly, but we can talk about that there.
Gina's smiling. Okay, the last one is the good old instrumentation controller, right? Just making sure we have instrumentation so we can auto-instrument everything in the space.
there's some opinions there about, like, you know, all namespaces by default, or we don't really know any better than just nilly-willy, like, having every other language, Java, Python, Node.js, right now. Like, we can talk about that more, but the idea would be that if it's blessed and considered stable enough, then it would be part of that default set.
And that's… that's the main thing, like, there's then the actual controller, which is going to create the CR and watch for events related to the CR itself, is going to be kind of managing the objects themselves, and the objects it manages are CRs. So we're playing…
We're just having this controller manage the deployment of the other CRs and make sure they are being deployed properly, and keeping them stateful in the right way.
**Jina** 33:30 And that's, that's…
**Antoine Toulme** 33:32 So then, the interesting part, of course, is what is happening under the hood is what Gina has done is that she has a CR for a collector, and then there's a whole bunch of YAML about the configuration that goes into that collector by default. That is all inside the work that she has done.
And, she can actually, like, show exactly what that YAML looks like, and we can maintain that, and we can do all sorts of things around this to make sure it's maintainable over time.
And, what I've been telling, Gina is that
you know, you all are very welcoming and nice, and we should just start to open, like, even draft PRs.
I saw that, I wrote, oh my gosh. And, and…
We can start to have a discussion that's more, like, aggressive about, like, the merits of some of those changes.
So Gina's been kind of telling me, well, I would like to make sure we have good test coverage for this, which has never stopped me before, so… I'm just trying to level set with her, she's an actual engineer, I just cosplay one, so…
That's why we're not opening the PR yet. That's the only reason.
**Jina** 34:39 This is like Antoine forcing my hand.
**Antoine Toulme** 34:43 Very much so.
Yeah, I mean, nicely though, right? I mean, I don't know if that came across as aggressive as a Frenchman would be, but, like, you know…
Anyway… In Klesgroup.
**Mikołaj Świątek** 35:00 Yeah, so… Talking more about how to… Start doing things.
and maybe start getting some changes into the operator, or talking and reviewing about, you know, a specific proposal, putting aside. Like, I don't see anything I would find immediately objectionable in this document. I've only spent, like, 18 minutes reading it.
But… But it looks… looks pretty reasonable to me.
How to actually introduce it into the operator codebase?
is a slightly different question. I'm not even sure if a…
If a feature gate is necessarily needed.
Let me put it this way, because we've kind of gone through this.
question with the target allocator CRD?
And that CRD was introduced, and then it spent a lot of time in their repo with a bunch of controller code in there, and…
and it was just not included in any of the default manifests, or in the home chart, or anything, and it was just invisible to users, completely interacting with the operator. And it didn't need a feature gate for any of this. It was just completely new code paths. If you weren't actually using it, then
you didn't see any difference. So…
I'm fine with doing something like that, with an understanding that this is experimental, might change, you know, might be removed and replaced with something else. If we're clear about that in the README, then I am fine starting to actually review and accept.
code, implementing this.
**Antoine Toulme** 36:51 Yep. Okay.
Yeah, really, it's a simple set. It's not actually touching any of the existing code, which is the nice thing about this, right? So…
completely optional, no one needs to somehow bind into it for their reasons, and we really want to have as much feedback as possible from the community. We need to get that in front of people so they can try it and tell us how… what the tooth… what the soup tastes like, right? Unfortunately, nothing replaces the first impression.
So, yeah, we'll just continue to work on that.
**Mikołaj Świątek** 37:28 Yeah, and my first view of this proposal is that
You've already done most of the difficult work, assuming you want to try and implement this, because I don't think the implementation is actually going to be that complicated. If you already have the collector.
configurations that you want to use, and you've already, like, actually deployed them, and they worked, and they sent some data. I think that's, like, 90% there, and the actual operator code is going to be fairly…
mundane.
I mean, you're…
**Antoine Toulme** 38:03 you might not be the recipient, the best person, in a sense, like, you might not have that much of an opinion about what you enable by default in some of that collector configuration, but it's possible that someone comes to us and say, I hate that you have the host metrics receiver enabled in there.
That's entirely possible, and I want to get that feedback soon.
Because we want to kind of be able to dark food that.
**Mikołaj Świątek** 38:27 What happens if 50% of the users come in and say, we hate the host metric receiver, and the other 50% come in and love the host metric receiver?
**Antoine Toulme** 38:36 This is a very easy question. We look at…
What 50% of the customers have more money? And then we go with them.
**Mikołaj Świątek** 38:47 Wow.
It's a good thing for you that we're not recording this anymore, Antoine.
**Antoine Toulme** 38:52 I'm sorry, did you… was there not, like…
**jea** 38:55 still recorded.
**Antoine Toulme** 38:59 I'm sorry, you don't do this by body count, we do this by interest based on actual weight in how people are going to use it at scale, and that translates into dollars.
2.
**jea** 39:13 Either way, I think that, to maybe sum up, I think that, to Gina, I think you should just go for it. Like, I think that there's…
**Antoine Toulme** 39:21 I really appreciate the documentation that you wrote, and it all looks good to me.
**jea** 39:24 I think we should just go for it and start getting feedback on it, using it ourself. I think the really…
Tough thing, an important thing for this type of project is going to be the testing.
As Mikulai said, like, actually writing the code for this is gonna be very straightforward. Most of it is actually going to look…
a lot like what the target allocator CR looks like in the past, it should be relatively straightforward in that you're just going to be
Creating another CR, as far as I understand it.
Whereas I think the tough thing is the test harness, and I think that that's gonna be really important for users. Like, the thing that I…
found when I was, like, an actual cluster operator as super frustrating with Prometheus, with OTEL, with
Elastic, anything, is understanding, when I install this, what data am I getting out?
And how much…
How much of a guarantee do the maintainers make that the data that I'm getting out today will be the data that I'm seeing in
two months, right? Obviously there's, like, the stability work from all of the semantic invention sigs around that.
But I think that we should be building on that to give users very clear guarantees, to say that we're confident that these metrics will exist in this way, these ones might change, and these ones will definitely change. Similarly with, like.
traces and trace formatting, we should be able to give similar guarantees as far as, like, what semantic invention that we're adhering to. Metrics are the worst, like, if I'm being honest, like, metrics are really hard to do this correctly with.
And it's okay if we get it wrong a little bit, but we should still go for it, and, like, try and do our best effort to tell people what is in there, and that we're, like, trying to be consistent. I don't want a world, though, where we are constantly
Like, I don't want to make the…
Problem we have with instrumentation and semantic invention happen with metrics and semantic convention, where we have to guarantee backwards compatibility.
I would like it if we could just say.
These are the things we expect to change, these are the things that we don't expect to change, and if they break, we will call it out, but we are going to push a breaking version.
But, like, we should give a guide for what we're gonna… for how we say that.
I think is my…
**Mikołaj Świątek** 41:53 Totally.
**jea** 41:53 Certain recommendation.
**Mikołaj Świątek** 41:55 If you're doing something like that, though, then you really want to use, like, an automated tool, something Weaver-adjacent, maybe.
To be able to actually tell, to be able to run, to update your dependencies, and then run it, and say, okay, this changed here in this way, let me automatically generate, like, a changelog entry, say.
This isn't changed.
Yeah, right?
**Antoine Toulme** 42:20 So, yeah, we've done that for MChart, but we use something called Golden.
You know what? It would be kind of neat if I did a plantation to you about that, and I can also show you the limits of what we have. And, the problem is that if we invite Gina, she might actually tell you how much of a pain in the butt it's been to maintain. She's not happy with me about that, I'm sure.
the… I introduced it, and then I ran away, which is typical. So, I, we…
I think we have some very mature tooling around this, and it's a problem for OpenTeometry as a whole.
**jea** 42:54 Yeah. Yeah, for sure, for sure. And I'll also, like, I don't expect us to, or am hoping that we get it right on the first try. Like, I expect there to be pain with it, and I think we should start simple and just publish
the list of things that we saw the, the CRD emit. Just keep it really.
**Antoine Toulme** 43:16 Easy to see. Yeah.
**jea** 43:18 Good.
And then as we get more advanced, and as more people use it, then we could, like, add in more advanced tooling.
But initially, let's just keep it simple.
Just… but I do want that to be there.
**Jina** 43:32 Would, like, for a first iteration of this, just doing this in a kind cluster? Because, like, as, you know, Antoine keeps mentioning that we have this in our hand chart, and we literally have, like, a host of tests, like, we have tests for, like.
taking a dump from Istio, and, like, every… every time there's a change, we, you know, check, have we changed the metrics which are… which we are collecting from Istio, for example, on multiple different Kubernetes version and different, like, kind clusters. So we do this.
And if it's just, like.
you know, we can just replicate this in a kind cluster to begin with. The more interesting part would be the… right now, what I've written, I just… I've been testing it against OpenShift, specifically because, you know, it seemed like a more,
meaty use case, because you have to bring out, like, the security context and all that stuff also, right? So,
we can then, I guess, add cloud providers, because, like, data does change when it's run in different cloud providers, and, you know, we… we're also looking internally how to do that in our Helm chart, because…
Yeah, but we can start with Kangin.
**jea** 44:40 Yeah, let's just start with Klein, keep it easy. Once we want to do more advanced, like, running on various, types of infrastructure, I'm with the Project InfraSig, and we could work with, like.
some of the vendors that we have to get actual infrastructure spun up if we wanted to. But again, that's a discussion for the future.
**Antoine Toulme** 45:00 That would be neat. I think our friends at Red Hat, who will be watching this recording intently, should talk about getting some OpenShift cluster, configured for us, so we can do that on a variety of infrastructure for them.
Because I don't…
**jea** 45:12 some deal with Oracle on being able to run some info with them. I forget exactly what it is. I have my SIG meeting, like, in an hour, and I can ask them.
**Antoine Toulme** 45:24 Yeah, go for it as much as we can. Hey, we… sorry, Junai and I have to run more too late to another meeting, and it's been really lovely talking to you all.
I wish you a great end of week.
**jea** 45:36 as well.
I don't know if we have anything else in our notes. Thank you both very much. Oh, they left. That's okay.
Let me see…
Nothing recent, nothing that I don't think we've talked about before. Nikolai, is there anything that you want to say?
**Mikołaj Świątek** 45:55 should… We should, we should drop the discuss at SIG.
**jea** 46:00 No, I think it's useful. I still like the idea of using it. I just don't think that… I think it's been a pretty quiet summer overall.
**Mikołaj Świątek** 46:07 No, I mean by, like, we have… we haven't discussed the issue for the retraction of the… of the… of that one version. Is there actually anything to discuss?
**jea** 46:18 I think we just need somebody to do it. I, like…
**Mikołaj Świątek** 46:21 That's a different thing than discuss at SIG, Jacob. That's fair, no, it's fair.
I will say one… one kind… one slightly annoying thing right now, is that there is a namespace label update test in the Prometheus Watcher parts, which is quite flaky, and I don't understand how it can be flaky, looking at it.
it doesn't have any… I've seen a lot of flaky tests around coinidine farmers in my life, all right? And I know what the signs are now, but it doesn't exhibit any of them. It actually does everything correctly. It correctly waits for all the caches to synchronize before running.
And there's still some race condition in there that I don't understand. So, if you get a moment and, like, look at it.
Because I can't even reproduce this failure.
Locally.
**jea** 47:20 I, I…
**Mikołaj Świątek** 47:20 It only happens when, like… GitHub Actions.
**jea** 47:24 Yeah.
It could be just that the, like, underlying network is bad, and it's just crashing, and it doesn't tell us, maybe?
**Mikołaj Świątek** 47:32 No, no, but it's like a unit, it doesn't talk to anything over the network.
**jea** 47:37 Are you sure? Some of the unit tests do spin up actual, like, things on the network.
**Mikołaj Świątek** 47:43 don't.
**jea** 47:43 MR.
**Mikołaj Świątek** 47:44 That one does.
**jea** 47:45 env test, all the env tests, ugh.
**Mikołaj Świątek** 47:48 This is not an ENF test. No, no, it's not an ENF test. I don't count those as unit tests, those are integration tests, in my view, specifically because there's an… and that's not even over a network, it's like a local API server, so you talk to it over a UNIX domain socket.
But what I'm talking about is an actual factual unit test for the Prometheus Watcher, when you pass in a bunch of fake informers into it, and then check that if you,
If you update a label on a namespace, then you get a different set of… or a different set of targets for, like, a service monitor, or pod monitor, or something like that.
That's what it actually does.
And it sometimes fails. Fails relatively frequently in GitHub Actions, and I have no idea why.
**jea** 48:40 I wish I could have a better answer.
**Mikołaj Świątek** 48:43 I'm just bringing attention. I'm just bringing attention.
**jea** 48:50 Well, other than that, I don't think we have anything else. I have to go… I'm gonna go make lunch, because otherwise I will not be able to.
Anything else for the group, from our other onlookers? Pavel, do you have anything?
**PL Pavol Loffay** 49:07 I don't have… thank you.
**jea** 49:10 Sounds good. Well, thank you very much.
Matias… Matias? Is that correct pronunciation? Good enough?
**Mátyás Végh** 49:18 Yeah, thank you.
**jea** 49:18 Do let me know if you need any assistance with the finalizer stuff.
Well done, well done. We'll continue in the thread there.
Just tag me if you need to.
**Mátyás Végh** 49:30 Okay, yep, thank you.
**jea** 49:32 Okay, bye.
**PL Pavol Loffay** 49:33 you guys.
**Mikołaj Świątek** 49:34 Thank you, everyone. Have a great day. See you.
**jea** 49:36 Bye.
