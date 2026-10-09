SIG: Kubernetes Operator SIG
Date: 2026-10-08
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Pavol Loffay (Red Hat LLC)** 00:21 Hello, I'm Chloe.
Can you hear me see me?
Hello! Hello!
I can hear you. Maybe it's your issue.
**Mikołaj Świątek** 01:10 Hey, Pavo, can you say something?
**Pavol Loffay (Red Hat LLC)** 01:13 Yes, can you hear me?
**Mikołaj Świątek** 01:15 Yeah, I can hear you now. Okay, good.
**Pavol Loffay (Red Hat LLC)** 01:17 Awesome.
I'll… we'll probably have to drop earlier, I.
**Mikołaj Świątek** 01:26 Yeah, sure.
**Pavol Loffay (Red Hat LLC)** 01:28 I wanted to know… I wanted to let you know that I will continue work on the network policies.
I think there are still some issues, and… Regarding the… the removal of the V1 Alpha 1. I'm asking some people from OpenShift what are our policies for the removal. I haven't got the answers yet.
**Mikołaj Świątek** 01:58 Okay, like, that's not super urgent, but every time somebody, like, submits a pull request adding a field, like, they also add a field to Alpha 1 and a migration, and I have to go and ask them to remove it, because we don't want it, and so on, so it's kind of, like, just a tax.
on contributions that I'd like to get rid of eventually. And it's also, like, makes our CRD twice as large, which is also a bit just, like.
Not very… not very nice.
But yeah, but it's not like critical to to figure it out. I think the network policy stuff, if we want to enable it by default, needs to be just like.
more carefully tested in a wider variety of environments. And unfortunately, like, the problems that we had with it were the kind of problems where you don't just see the problem if you deploy the operator into, like, a, you know, GKE cluster.
you only see that problem after you let it run there for a while, and Google, like, cycles the API server IPs. Just, like, you know, an event that you don't actually have any control over.
And, also, like, there's a there's a there's a issue. There's, like, a meta issue open for this stuff listing all the things that are wrong in there. I'm gonna unpin it, I think, because I I'm not sure if it needs to be pinned anymore.
But it lists, like, all the things that we need to address, and I think the biggest problem in there is psyllium.
And… Because apparently, doing it this way just cannot work.
on sodium. They do their own nut.
In a way that makes this… these, like, just… these are the wrong endpoints on Cilium.
So either we have to make it.
Like, either we have to detect psyllium and disable it, or we have to, like, document in, like, big, you know, big, scary words that if you're on psyllium, you need to disable. These network policies.
Maybe, maybe for Cilium, maybe for Cilium, like, the workaround where Like, if you are able to give… put your own cider blocks.
for the network policy. Maybe that will fix it.
But yeah.
It's, like, not very… it's not as simple as it seems.
Right, I think we can get started.
Hello, everyone.
**Jacob** 04:37 Yep, I think we're good to go.
**Mikołaj Świątek** 04:39 Yeah.
Okay, things which are on the agenda.
I put in a reminder to my fellow maintainers to look at the Ruby and PHP auto instrumentation pull requests, which are pretty close to just being very mergeable, in my opinion.
There's, like, various small bits of feedback going around, at least in the PHP one, but it's, like, fundamentally correct.
Yeah, and it's just, like, a question of, like… working through them, and then we can merge. The last time I looked at the Ruby one, like, I think… I think for Ruby, we now have the image published by the Ruby SIG as well, and otherwise, that pull request also, like, looked… looked fine to me last when I looked at it. So we just have to like I I want to have like at least 2 of our approvals on each of those, and and then we'll be good like we've We've kept the offers who are here, like, engaged for a long time, and I apologize for that. I think we can.
I think we're pretty close.
And… Yeah, I think… Yeah, sorry.
**Jacob** 05:51 I was looking at the Ruby one and the PHP one this past week, and they both look good. I was happy to see all the added sort of tests in multiple stages. That makes it a lot easier.
discussion topic later about some, like, injector stuff, which will also help, I think, move this along as, like, a follow-up. But I'm happy about both of these moving forward.
**Mikołaj Świątek** 06:14 Okay.
The other thing is that we had a bug report opened recently about supposedly there being… it's possible to cause an operator panic by submitting a pod with no containers. This is… Not true, it is not possible to do that.
Although the code change that the offer proposed is good either way. But I did ask… I did ask a smart AI model to try to review our webhooks, like, for similar issues, let's call them.
like, assumptions about, like… because, for the record, mutating webhooks on pods run before admission, okay? So you can't assume that things are correct in them.
And it found some stuff. I filed some issues. Those issues are substantially AI-written, but I tried really hard to make them, like, nice. So you can have a look at them and tell me how much I succeeded with them.
**Jacob** 07:16 I think you did a good job with them. I was just looking at them before, when I joined, and they all look legit. I mean, you can't… You can't technically have, like, a collector configuration without receivers or exporters is not valid, and so it makes sense that we didn't…
**Mikołaj Świątek** 07:30 I, I know, but like, yeah, but, but we shouldn't like panic where, where, when somebody submits it, right?
**Jacob** 07:36 Yeah.
**Mikołaj Świątek** 07:37 The biggest one I found was that our webhook is… Our pod mutation webhooks are incorrect in the sense that they swallow pod fields they don't know about. So if somebody uses a cluster that is newer than the Kubernetes library they have, we just delete odds fields that are unknown, which is a pretty serious bug.
**Jacob** 08:02 Yeah.
**Mikołaj Świątek** 08:04 And it's not very hard to fix, so that's, like, a priority. And it found some other stuff, like, the bug that we had filed for the instrumentation webhook actually is a bug on the Sidecar webhook.
**Jacob** 08:19 Yep.
**Mikołaj Świątek** 08:20 For example.
So, there we go.
**Jacob** 08:23 These are all legit, and none of them, none of the fixes seem challenging, right? Like, they're all pretty small, no.
**Mikołaj Świątek** 08:28 There is… there is, like, a question of how… what to do if… If the webcook panics.
whether you should recover, or whether you should, like, handle it at all in any kind of way. Because the problem is kind of that if you… if you panic in the webhook.
The result is that you send a rejection.
and effectively.
That's how Kubernetes… that's how the, kind of, the way the container runtime… controller runtime stack.
Deals with it, in the end.
**Jacob** 09:01 Yeah.
**Mikołaj Świątek** 09:01 That might not be what we want.
**Jacob** 09:04 I think we could use the recover, and then record the panic on… the… as an event on the CRD.
I think feels like the right answer there. Recover is, like, not… I mean, I rarely use Recover in Go, just because it's, like, far from best practices, I would say. Usually you're supposed to panic on purpose, but I think in this case, it would make sense to record the panic on the offending, collector CR and block it, so that somebody could open an issue with us. Like, we shouldn't… ideally ever see a panic. Obviously, that's not always gonna be the case, but, like.
**Mikołaj Świątek** 09:45 It's a bigger problem in mutation webhooks than in the admin.
**Jacob** 09:48 Yeah.
**Mikołaj Świątek** 09:48 Because in the mutation one, you're… somebody is creating a pod, and you panic because you have a bug, and you reject their pod, even if your webhook is, is, like, configured as ignore.
**Jacob** 10:01 Yeah, so I…
**Mikołaj Świątek** 10:03 problem there.
**Jacob** 10:04 I think it would be better as a result than to just write it as an error and not…
**Mikołaj Świątek** 10:08 Like…
**Jacob** 10:09 panic the request. I mean, Kubernetes is obviously set up to handle that type of thing, but we should be better.
stewards… Better operators.
Yeah. One might say.
**Mikołaj Świątek** 10:23 Yeah.
Yeah. And so that's what I have. And I see that the next one is yours, Jacob. Injector Beta.
**Jacob** 10:32 Yeah, I wanted to sort of check on where we're at with the injector, because I was just coming from the injector SIG And I think that, you know, the SIG… like, we would like to begin seeing the injector used in the operator. I know that we have the blocker of the S390X architecture, but I'm hoping that we could at least Begin using it as something opt-in.
So that because Pavol had that PR open, I believe, for the snow.
**Mikołaj Świątek** 11:05 It was… it was me, no.
**Jacob** 11:07 Owes you.
**Mikołaj Świątek** 11:08 Yes, but…
**Jacob** 11:09 How does Pavolo open the S390X problem?
**Mikołaj Świątek** 11:12 It's possible, if we just want to trial it, it's possible to use it, for example, in .NET. Because .NET doesn't support the S390X and whatever else is there, PPC64LE, right? Yeah.
the .NET doesn't support those either way, so we can actually just use the injector in there, and it's not super complicated to do it. There is something of an open question.
how we want to arrange it. My POC of this just put the injector in the… in the image.
And that was it. That's not really a very big deal, but… It does make the image a little bit bigger.
They buy 3 megabytes or something.
**Jacob** 12:02 In the, like, in the thing that we published for .NET?
**Mikołaj Świątek** 12:05 Yes, yes. So, there was, like… it would be nice-ish. It will also be nice-ish for… For people who eventually want to have custom images.
It would be nice if they didn't have to care about this. So, essentially, if there was, like, a injector container image.
And we could independently ask for an injector container image, and then for our own image, and use the injector from the container image. Then we don't have to actually bundle it with anything, and it's also the case that you can do at runtime upgrades of the injector image without having to rebuild our instrumentation container images, right? That is the… that's the trade-off. So that would be nice, but it's not really necessary for this. The only thing I am a little bit… like, the only thing that gives me a little bit of pause with adopting this is basically… I would like to use the opportunity of adopting the injector to also create a standard for custom images. Like, what do I have to do in order to create a custom instrumentation image? Like, what is… what do I have to put inside of it for it to work?
**Jacob** 13:20 I mean, I think that if we were to use… I think that we could start doing this with the injector, where it's very… I think the injector has a clear, like.
Input-output contracts that we could go off of, of our expectations, right?
and… I mean, I'm also… Kind of of the opinion that, like, if a user is going to write their own custom image and, like, their own fork of the injector or whatever.
You know, I think that our guarantees of safety should just be that the injector's, like, core functionality works, and nothing more. You know, we, like, we can't hold hand on it too much.
**Mikołaj Świątek** 14:01 That's fine. I I am personally actually very fine. I am very fine with, like, if users have very elaborate injection customization needs.
Putting in their own injector, to me, is, like, a valid thing to do.
I am okay with that. I would just like to… I want to define what the operator actually does.
I would… ideally, it would be the same mechanism for literally every instrumentation.
And, like, the language-specific bits would be, like, mostly… injector kind of encapsulated in it.
And then it is very simple for anyone. Like, we would say, we take the injector from this environment variable inside your container, and then we run it in this way to inject. And, you know, we put it in the LD preload with some configuration that you provided, and that's everything we do, right? And it's up to you. You can even… in your custom image, you can replace the injector with one you've written yourself.
as long as it does the things it needs to do. In this case that is okay with us.
Like, that's what I would eventually like to do. But this is, like, a larger project, and it's more complicated, so I think what we can do instead, we can just add the injector to the .NET image and use it that way. Because the .NET image, we actually do control.
Like, we can't easily do it… we actually cannot easily do it with, like, the PHP or Ruby images that we're adding, because those we, you know, their respective SIGs control them, which I think is a good thing.
But for dotnet, we can actually just do it.
And check what happens.
**Jacob** 15:45 Yeah. I mean, I think that, we can start this with .NET, and I can go from the injectors' guarantees of, like, the in and out.
And we can just write if you want to do… Your own custom image, this is… these are the boundaries of that.
**Mikołaj Świątek** 16:01 The custom image, we… let's just hold up on for now. Like, we can do.
**Jacob** 16:05 the.
**Mikołaj Świątek** 16:06 and we can note… I don't know, we could… we probably want to use… the way I think we want to do it is that we want to unconditionally add the injector to the .NET image, you know, let's eat the 3 megabytes that it adds to it, and then add a feature flag which uses the injector in the actual injection process. I think that's how it should go.
**Jacob** 16:25 I don't know, I think that we should just… I want to see if I can get the image published from the injector, and then we can just use that, and then we don't need to use… the, the .NET images at all, right?
**Mikołaj Świątek** 16:42 We don't have to change the OpNet images.
**Jacob** 16:48 But wait, hold on.
**Mikołaj Świątek** 16:51 We still have to, we need to have a .NET image because when.
**Jacob** 16:54 Yeah.
**Mikołaj Świątek** 16:54 have the actual injected artifact.
**Jacob** 17:00 Yes, yes, I see what you're saying.
**Mikołaj Świątek** 17:05 It's just that…
**Jacob** 17:06 I don't know, this should work.
**Mikołaj Świątek** 17:07 In my view, it's pretty straightforward. Like, you get the injector from somewhere, maybe it's inside the .NET image, maybe it's, like, a separate image that we pull.
We copy… again, we have this shared volume that we use for all of this, like, the shared volume that all the pod… that all the containers in the pod mount, right? We copy the injector in there, we copy the instrumentation artifact in there, and then we set the right environment. Maybe we create an injector configuration file, or maybe it's already, like, on the image that's, like, beside the point, I think.
**Jacob** 17:40 Yeah.
**Mikołaj Świątek** 17:40 It just sets the environment variables in the application pod. And that causes it to LD preload the injector. The injector sees the environment variable pointing to the config. It uses that config. Everything works.
**Jacob** 17:54 I guess what I'm wondering is, like, I… I don't… given that this should technically be, like, a no-op to the user, do we have to feature flag it?
**Mikołaj Świątek** 18:05 I would feature flag it just out of an abundance of caution, to be honest.
**Jacob** 18:09 That's fair. I mean… I think that'd be fine, to feature flag it, but I don't think we'll need… I think that this would be the sample case, and then we could use that to then… get it elsewhere. Is there a way to detect the… I… I would like to get around the need to wait for, like, the S390X Images, so that we can start using it for all the languages, because, like, the injector is… has… PHP and Ruby support already, I believe?
**Mikołaj Świątek** 18:45 Is there a way to detect? Well, this really just depends on the node architecture.
Can you see the node architecture from inside the webhook? I don't think so.
**Jacob** 18:57 I think so.
**Mikołaj Świątek** 18:58 Like, injection… injection happens before you, like, before you get scheduled.
obviously.
Yes.
**Jacob** 19:08 Yes, But… Couldn't we detect from the operator what… architecture the Operator is running?
**Mikołaj Świątek** 19:18 You can have mixed architecture.
**Jacob** 19:20 Yeah, you can have mixed architecture clusters.
**Mikołaj Świątek** 19:23 have.
**Jacob** 19:24 Yeah, it's pretty…
**Mikołaj Świątek** 19:24 No idea. At the moment you're injecting, you have no idea what it is and what's going… you can't even check by you… by looking at the container image of the application, because that can be, like, a multiplatform manifest.
**Jacob** 19:39 Yeah.
**Mikołaj Świątek** 19:39 I think in that case… Pulls the right thing, pulls the right thing, like, at, you know, at resolution time on the… by the… by kubelet of it, right? You don't know.
**Jacob** 19:49 Yeah, maybe what we would… we should do for the… for the S390X cases, is just have Make it clear that this will be a breaking change.
For them, At some point, and just say, like.
You need to manually disable the injector for now, or something like that.
**Mikołaj Świątek** 20:11 That's…
**Jacob** 20:14 Because I don't know how many of our users are on… I mean, I wish Pablo were…
**Mikołaj Świątek** 20:17 means.
**Jacob** 20:18 asking, but…
**Mikołaj Świątek** 20:19 That means you have to pub, you either have to publish two different versions of the image, or you have to publish one version where the injector is like some kind of ship. Disabled.
**Jacob** 20:29 Yeah.
Yeah, it's less than ideal. I mean, we could also just say that after this version, we are not supporting.
We are not supporting images without the… Injector, as well.
**Mikołaj Świątek** 20:45 I mean, we could, but we're doing a breaking change where we support something right now, but we don't support it. Like, we support the operator on these architectures.
**Jacob** 20:55 Yeah.
I just… I don't… I don't want to block, like…
**Mikołaj Świątek** 21:00 I know, I know, I know what you're, I know what you're thinking is, yeah.
**Jacob** 21:04 Yeah.
**Mikołaj Świątek** 21:05 The annoying part here is also just that… I mean, maybe, maybe, maybe the single image shim is the right idea, like, on S9TX and PPC64LE, the injector is just, like, an empty binary that does absolutely nothing, and if you try to actually use it, it errors.
And… and the error is telling you.
disable this option. But then it has to be an option that stays forever. And we have to keep the code that injects without using the injector forever, right?
**Jacob** 21:44 It wouldn't be for… it would just… no, no, it would just be until the injector supports S290X.
**Mikołaj Świątek** 21:52 Is this, like, an effort that has been, like… accepted by the injector maintainers like, do they actually wanna.
**Jacob** 22:01 I mean, I think it's more that we're waiting on infrastructure from IBM to be able to test it.
**Mikołaj Świątek** 22:05 I mean, yeah, yeah, I understood… my understanding was that there needed to be, like, IBM needed to contribute something to ZIG so that it can actually be built correctly. Is that… has that happened? Are we only waiting for testing now?
**Jacob** 22:20 I think we're waiting on a few things.
Yeah, I mean…
**Mikołaj Świątek** 22:26 I'm trying to… I'm trying to get them to get… to get a feel for how likely it is that this happens in the next year, let's say.
**Jacob** 22:37 I I.
I wish I had a good answer. I just…
**Mikołaj Świątek** 22:41 I have no idea. My point is that, like, a feature flag that's, like, kept in whatever beta for a year is also, like, not great.
**Jacob** 22:52 Yeah.
I agree.
**Mikołaj Świątek** 22:58 I am OK doing it this way, roughly, I think. I'm OK saying that the S390X and PPC64LE support is best effort, because it is.
**Jacob** 23:10 We.
**Mikołaj Świątek** 23:10 We don't run tests on these architectures. We don't even run tests on ARM.
Which we should.
**Jacob** 23:17 We don't.
**Mikołaj Świątek** 23:18 No. No.
**Jacob** 23:20 We should.
**Mikołaj Świątek** 23:20 Yeah, I know, but we don't.
We don't, like, largely we don't do anything that interacts with the CPU architecture in any way, so it just works, but…
**Jacob** 23:30 Yeah, but.
**Mikołaj Świątek** 23:30 So on ARM, we should run tests on ARM.
**Jacob** 23:34 Yeah.
**Mikołaj Świątek** 23:34 We cannot run them on these more exotic architectures easily, so it's like a best effort.
**Jacob** 23:41 Armand's.
**Mikołaj Świątek** 23:42 We.
**Jacob** 23:42 We should be able to run them on our own.
**Mikołaj Świątek** 23:43 Yeah.
**Jacob** 23:44 We have those images accessible.
**Mikołaj Świątek** 23:45 We can. We can just run it in Github actions like on a schedule on main.
**Jacob** 23:50 Yeah.
**Mikołaj Świątek** 23:51 I think that's fine, that's enough.
But I'm fine saying this is best effort.
you know, we might… you might have to flip a flag if you're on one of these architectures, so… so we, like, we will have to maintain both injection code paths, but we can, like, try to make this nice.
nicer in the code.
The main problem might be that.
depending on how different the code path actually is, and you can probably look at my POC, it's not very different.
So maybe this is okay, but the problem might be that, like, we'll… we'll also have to run tests with the… run tests with this setting disabled, right? Because otherwise it might break.
It might break silently on us.
So, this is gonna be, like, a bunch of additional maintenance.
For us.
**Jacob** 24:44 So we'll do this for .NET. I'm just writing down the decision here. We'll initially do this for .NET, with a feature flag.
that we hope To bring to stable quickly.
**Mikołaj Świątek** 24:57 Let me quickly check actually which images actually we do publish because I don't know off the top of my head. Which instrumentation images do we publish?
are these… architectures.
Oh… Apache HAPD I don't want to touch. This is, like… Don't know.
**Jacob** 25:27 I mean, I don't even think the injector supports that, so I think that's fine.
**Mikołaj Świątek** 25:30 Yeah.
Java does support these two, these additional ones.
**Jacob** 25:38 Yep.
**Mikołaj Świątek** 25:38 Node also does.
And Python… iPhone does as well, so unfortunately, Dot net.
**Jacob** 25:50 I mean, I think it's…
**Mikołaj Świątek** 25:51 isn't.
**Jacob** 25:52 I think it's fine, though, for us to just say, I think it's fine for us to just say that.
You know, these Intel architectures will be on their own or sorry, these IBM architectures will be on their own, and they'll need to figure it out.
we can't… we can't test it. Like, you know, if some IBM people complain about us not testing this, then we just have to ask them to give us the infrastructure, you know? Like, there's… there's kind of no other recourse, unfortunately. And I'm… Also, I'm, like, losing my patience a bit with it from them. Like, I don't think that we should stall on this. Like, there's… I think.
**Mikołaj Świątek** 26:32 I know, I know, I know, I understand, but I also don't want to break things for existing users.
**Jacob** 26:40 I understand.
**Mikołaj Świątek** 26:41 I don't want to put, like, I am… okay, so I am okay telling users on these architectures.
Sorry, we are on an architecture that we can't test. It's somewhat exotic. We do best effort. If you run on this and use these… this instrumentation, you might have to do something in addition.
Right.
**Jacob** 27:02 Yeah.
**Mikołaj Świątek** 27:03 that this is the best we can do. I am not fine telling them, from now on, you can't use the operator.
**Jacob** 27:09 Yeah, I agree, I agree.
**Mikołaj Świątek** 27:13 Okay, so I guess we agree.
**Jacob** 27:17 This sounds good. Would you be able to get your… inject your PR to match this goal, and then we can get that in, and then I can… review and work on the injector side. I mean, I could see… from the injector side, do you want… The injector to publish, like, just a single image with all of these packages that it loads in, and then we can just have a single injector.
**Mikołaj Świątek** 27:43 No. If we did that, we don't have to do anything special, but this is, like… If I just want to do it for .NET, then what I would do is I would just, I either… what I want from the injector is for it to publish a single container image containing only the injector and nothing else.
**Jacob** 28:03 Okay.
**Mikołaj Świątek** 28:04 That's the only thing I would like to have from the injector.
**Jacob** 28:08 I asked Bastian about that, and we'll see if he wants to do it. If not, I'll do it. It's like, you know, probably 10 lines of Docker. It's not very difficult.
**Mikołaj Świątek** 28:17 The operator can also publish that on its own, but I would rather, I would rather, I don't want to, I would rather the, yes, I would rather the actual injector.
**Jacob** 28:25 We, we should…
**Mikołaj Świątek** 28:26 much.
**Jacob** 28:27 With our requests that we've made to Ruby, we should try to… Thanks, Andy. Do you have anything you wanted to talk about on here? Just one.
**Andy Keller** 28:35 No, no, I just… I have that on my calendar and I just ended, ended a meeting and was gonna go get lunch and then this meeting was here and I wanted to join.
**Mikołaj Świątek** 28:46 A social call, do you wanna…
**Andy Keller** 28:47 No, I I care very much about the Operator and I wanted to I wanted to see what was going on.
**Jacob** 28:55 Also.
**Andy Keller** 28:56 Alright, so…
**Jacob** 28:57 You'll be happy to know that I updated my, Elixir server for the OpEmp Bridge, if you wanted to check that out.
**Andy Keller** 29:06 Oh, cool.
**Jacob** 29:07 I added in some nice UI improvements that make it look a lot better, so…
**Andy Keller** 29:12 I know Adriana's doing a talk, and she was mentioning it, so…
**Jacob** 29:17 Yeah.
**Andy Keller** 29:17 That's great.
**Jacob** 29:18 It's pretty neat. I think you'll like it.
**Andy Keller** 29:20 Cool, I'll check it out, alright.
**Jacob** 29:22 Yep.
**Andy Keller** 29:23 See you guys.
**Jacob** 29:24 See ya.
So, Mikolaj, getting back to it, I like what we have asked Ruby to do, and I think we should just make that the standard. I don't want us to, like, publish more… I mean, we already agreed on this, like, years ago, but, like.
We should just… ask the people to publish the images as much as we can, and given that I'm a maintainer for the injector, like, it's not… We don't have to pull any hair there.
So… I will handle that on the injector side. Don't worry about it.
**Mikołaj Świątek** 29:57 This is all okay.
with me. I also don't want to block the scroll effort on the exotic CPU architecture problem.
**Jacob** 30:07 Yeah, I think the injector goal that we just talked about is to get Injector to be 1.0 for KubeCon EU of next year in March. So we have basically, like, a 6-month timeline until then.
And I would like us to get… To use… to start using the injector for all of our.
injection purposes.
By then, whether it's by default… I mean, ideally by default, we would be doing this, by then, and then we'd be using their, like, candidate release for 1.0 for, like, a month, and then they can go 1.0, and then we can just bump it to a 1.0, and then we're done.
That's kind of the release timeline that I'm hoping for, which I think is reasonable. I don't, like, given that the… This should be mostly, internally… internal mechanics, and not, like, a user-facing thing. This should be relatively painless.
Is the hope. So…
**Mikołaj Świątek** 31:03 Well, my injector POCPR, just like everything works.
**Jacob** 31:07 Yeah, awesome.
So, let's… let's just do this.
And we can do a whole suite of feature flags again, like we did with the initial That migration that we did a while ago.
And then just… Bump them in series.
Every other release cycle for the next 6 months.
**Mikołaj Świątek** 31:31 Yeah.
I might even be convinced to do a single feature flag. I'm not overly.
**Jacob** 31:37 Okay.
**Mikołaj Świątek** 31:37 that.
**Jacob** 31:38 Then let's do a similar one.
**Mikołaj Świątek** 31:39 like, I don't know, like, I trust the injector project enough to do, like, the relatively simple use case that we're asking.
**Jacob** 31:48 Yep.
I think it should be good.
**Mikołaj Świątek** 31:52 And in .NET, the one big benefit of this is that we'll be able to get rid of the annoying perlibc annotations, because .NET has that.
**Jacob** 32:04 deal.
**Mikołaj Świątek** 32:04 The injector solves it.
**Jacob** 32:06 Yeah.
Cool. Well, that sounds good. Do we have anything else to go through?
**Mikołaj Świątek** 32:13 For feature gate stability.
There is the Golang Flags feature gate, which somebody asked us to do a carve-out for.
I'm wondering… it's stable, so we can remove it, but I'm wondering if we shouldn't change the GoMem limit to be, like, 0.9 or something, and that's annoying, because we can't actually easily do it, because what we do is just stick the downwards API in there.
**Jacob** 32:42 I think that's our best option. I don't think we can do anything else, unfortunately.
If somebody wants to… but you just say if anybody wants anything more advanced, they can use the collector.
Mem limit extension.
**Mikołaj Świątek** 32:55 Yeah.
Which we now explicitly, like…
**Jacob** 32:59 Which we support, yeah, no.
**Mikołaj Świątek** 33:01 I mean, we don't do anything if it's new.
Okay, so that's it.
One thing I kind of want to tell you that I tried doing with the power of Agentic coding.
Because I tried to do the whole experiment for.
doing all target labeling in the target allocator, if you recall what that was about.
**Jacob** 33:28 Yeah, I remember.
**Mikołaj Świątek** 33:29 Unfortunately, this cannot really work.
**Jacob** 33:32 should.
**Mikołaj Świątek** 33:32 Can only work in, like, a very… by coupling Prometheus receiver to the target allocator very, very tightly, and the problem is really that Prometheus receiver looks at meta-labels from the Kubernetes target discovery to do certain things.
**Jacob** 33:50 Yeah.
**Mikołaj Świątek** 33:51 So there's, like… and there's also, like, some things Prometheus does label in it whatever you, like.
Whatever you do, it always does it. So… Yeah. So it's like… it's just, like, kind of…
**Jacob** 34:05 Mechanically frustrating.
**Mikołaj Świątek** 34:07 Mechanically frustrating, but there is a, like.
So… the whole theory, because that… behind that initiative for me was the idea that we send a crapload of data down to these Prometheus receivers, and then they spend a lot of CPU and memory on, like, parsing and creating.
doing new scrapers, right? And this process is a lot.
And maybe that's, like, fixable with some kind of more targeted optimization.
In particular, I realized that we don't have, like, compression enabled in the target allocator, sir.
**Jacob** 34:49 We don't? That seems like a thing we should have.
**Mikołaj Świątek** 34:51 Yeah, I think so, or maybe…
**Jacob** 34:54 The compression between us and the collector?
**Mikołaj Świątek** 34:58 Collector, yeah.
**Jacob** 34:59 Really? I think most requests are compressed by default.
**Mikołaj Świątek** 35:04 Are you sure about that?
**Jacob** 35:06 When I was doing gRPC options from… well, this is HTTP, but when I was doing the default client options on the collector.
We ensured that compression was on by default.
So, unless…
**Mikołaj Świątek** 35:20 But you can send whatever you want to the server, but does the server actually support the compression and sends you back a compressed payload?
**Jacob** 35:31 Trust me. I am.
**Mikołaj Świątek** 35:34 I'm… I am not fully convinced that this is the case. I mean, Claude claims it doesn't, but that's not evidence that this is true.
it's just, like, might be done in a way where it's, like, not that obvious. Maybe it's worth.
But the compression doesn't actually solve the problem fundamentally, it just makes it so that you, like, spend less bandwidth on the thing, right? But… Yeah. Really, the bandwidth, that's the problem. The problem is that you give a crapload of labels that you then have to Process in each collector and do this whole churn, and you do that every half a minute, so it's actually pretty expensive.
**Jacob** 36:13 Yeah.
**Mikołaj Świątek** 36:13 At the end of the day. But maybe there's, like, some… like, you might be able to do some optimization in either Prometheus or Prometheus receiver to, like, make this… nicer.
Yeah. We'll see.
Either way, like, the naive way of doing it is, unfortunately, I think, off the table, because I really don't want to have a whitelist of labels that I have to send.
**Jacob** 36:36 I agree.
**Mikołaj Świątek** 36:36 to Prometheus receiver.
Something that we can do is, like, use the same scrape.
can't scrape the same label initialization that Prometheus does. That makes us like 30% slower.
and target allocator.
**Jacob** 36:51 That doesn't surprise me. I mean, they have to do a ton of initialization on startup.
For these maps that we kind of bypass by being clever.
**Mikołaj Świątek** 37:01 Yeah, and I think we should do it. Like, I think we should eat the performance.
**Jacob** 37:06 You think so?
**Mikołaj Świątek** 37:07 Yes, yes, I think… I think so. We have… we've had… right now, there's a difference between us and Upstream Prometheus, in terms of what we emit. There's some… some labels that we don't… that Upstream Prometheus does.
And those are labels, like, have to do with, like, some, like, native histogram, something, something, something, for example.
**Jacob** 37:26 Oh, sure, sure.
**Mikołaj Świątek** 37:28 But, like, there is… it is an incompatibility, and we've had, like, a history of bugs around this stuff.
So I would honestly, personally eat the performance problem. If it's, like, a very big performance problem that everyone hates, I would go to Prometheus and try to make them.
**Jacob** 37:46 And, yeah, make it upstream fix.
**Mikołaj Świątek** 37:47 more performance, right? Yeah.
**Jacob** 37:50 I mean, their code base is… difficult to work around, I would say.
**Mikołaj Świątek** 37:57 But, like, I really would like to just have Just have compatibility by construction rather than by conformance test, which it is right now.
Sure.
**Jacob** 38:11 I could agree with that.
If it's really, like, you know, 30… 30%, And users are experiencing the pain.
It's really tough, I don't know. 30% is a lot.
**Mikołaj Świątek** 38:28 I know, but we made it a lot faster earlier, so… We can, we can, there's, like, there's, like, some potential other ways to make this whole process faster as well.
**Jacob** 38:40 Yep.
**Mikołaj Świątek** 38:41 But I don't know, like, I think in this case, this is also, like, users, I think, care… like, you can always just scale target allocator, like, you can give it more… giving it more resources is, like, by far not the most resource-heavy thing running in your Kubernetes cluster, if you're even, like, seeing any kind of performance.
You have to have a lot of targets for that to be the case, right?
**Jacob** 39:07 But we'd have users like that, you know?
**Mikołaj Świątek** 39:09 We have users like that, yeah, but those users have really large clusters and can just, like, shard it horizontally.
**Jacob** 39:15 Oh.
**Mikołaj Świątek** 39:15 the.
**Jacob** 39:15 Yeah.
**Mikołaj Świątek** 39:17 Right?
**Jacob** 39:20 I don't know. I'm, I'm unconvinced by the trade-off currently. I think that I understand what you're saying, and I do agree that that is.
Probably a worthwhile trade-off, I would just need to know what it looks like at scale for a user. Because I would just worry that If it's 30% on your benches, I worry it's gonna be a lot worse on theirs.
**Mikołaj Świątek** 39:43 Our benches actually exercise the 800K scrape targets version.
**Jacob** 39:49 Yeah, I've seen… I've seen bigger, which is crazy, but they are out there, you know.
**Mikołaj Świątek** 39:56 I wonder sometimes how you get a million scrape targets in a single cluster.
**Jacob** 40:00 Oh, you don't want to know.
The one time that it happened to me was by accident, where GCP had a observability bug where they weren't… or they weren't expiring their certificate signing requests, so the… it had unlimited cardinality In a cluster, and as a result.
what was… that basically caused their own internal, like, GMP, like, their managed Prometheus, to, crash loop, which then crashed the… API server.
So it's pretty brutal.
And it was, it was over a million, Wow.
It was, like, over a million, series. It was huge.
Anyway, I have to go get lunch, unfortunately. But if… do you think you'll… for the injector PR, I'll work on getting the image by.
I'll work on getting the image done. I suppose.
Okay, I'm gonna talk with Bastian about it. We'll see what he says, but I'll work on getting the image, one way or another.
**Mikołaj Świątek** 41:15 Okay. I can cut out the .NET part out of my pull request and submit it. That's not a problem.
**Jacob** 41:25 Sounds good. Thank you.
If there's any… I've been appreciating all of your pings on the PRs, by the way. My GitHub notifications have been overwhelming as of late, and it's been very difficult to manage.
So, getting direct pings has actually been super helpful, so I really appreciate that.
Because it gives me an actual, like, push notification when you do that, and so it means that I can actually, like, prioritize effectively.
**Mikołaj Świątek** 41:58 Okay, so I think we're done with the things that we have in the agenda, right? Ilia and Kushagra, do you guys have anything you'd like to talk about?
I'm gonna take that as a no.
**Jacob** 42:25 I guess not.
**Mikołaj Świątek** 42:26 That's cool.
**Jacob** 42:27 Yup.
Well, have a good night for you. Thank you as always.
**Ilia Petrov** 42:33 Sorry, can you hear me?
**Mikołaj Świątek** 42:35 Yes.
**Ilia Petrov** 42:36 Okay, sorry, I was muted and I'm in the car. I wanted to tell you that I don't know if you remember, a few weeks ago I got one PR merged in Target Allocator, which was related to MTOS without Source Manager. Today, I tested a bit more in our setup, and I think I made one bug where I don't remove the volume and volume mounts from the auto collector, and basically it expects secret that is not there, and now I work on fix for that.
Yeah, probably this is something from my side, and when I have time, I will look, there's also one book in, Go instrumentation, when you use jobs, the sidecar container doesn't get removed when the job is done, so basically the job never finishes.
That's okay.
**Mikołaj Świątek** 43:38 It'd be really nice, because this has been, like, an issue open for a while.
**Ilia Petrov** 43:43 Okay, okay, I will try to give it a look a bit more seriously.
Tried to reproduce it, I reproduced it, and now I just… He has to troubleshoot a bit more. But okay, I mean, these are the two things I work on at the moment.
**Jacob** 44:06 Thank you.
**Mikołaj Świątek** 44:14 Alright, cool. Jacob, are you at Salt Lake City?
**Jacob** 44:19 No, I'm not gonna be going this year. I didn't have talks accepted. It seemed like very few people from The SIGs that we are a part of are gonna be there.
This time. Well, you'll be there, though.
**Mikołaj Świątek** 44:32 I am surprisingly going to be there this time because.
**Jacob** 44:35 like.
**Mikołaj Świątek** 44:35 We had a, we had a. I was not going to go and then somebody else from our contingent, from Elastic, dropped out and they said do you want to go? I was like sure, I've never been to an NA KubeCon, so there you go.
**Jacob** 44:49 I think I would have been more enticed to go where it's still in LA and not Salt Lake City, like, I would have made more of an effort, but… I actually have a really busy November now.
So it's actually probably good that I'm not going. I have a lot of things. But I will be at, KubeCon EU next year.
I'm submitting a lot of talks for that, so I'm hoping that at least one of them gets through.
But… That's the hope. Enjoy Salt Lake, though. It's a very beautiful place, if you can make it out to the mountains.
**Mikołaj Świątek** 45:25 Probably won't, but… Anyway.
I think we can, we're done. Yeah.
**Jacob** 45:37 Well, have a good night. I'll see you later.
**Mikołaj Świątek** 45:39 So, see ya.
