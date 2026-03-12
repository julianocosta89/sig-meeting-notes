SIG: Kubernetes Operator SIG
Date: 2025-07-17
Duration: 34 minutes
Zoom Recording URL: https://zoom.us/rec/share/dKqrxoCliCV131pXN3HY16NoiOqMvM8T2EWT1c-3iSYJlzt7GmahSnuDkNIdlJns.b_XUUzaTumrSNnP6
============================================================

## Zoom Recording Transcript

**Mikołaj Świątek** 00:23 Hello!
**Benedikt Bongartz** 00:25 Long time, no see.
**Mikołaj Świątek** 00:27 Long time. No c, still no c right now.
**Benedikt Bongartz** 00:30 Yeah.
Wrong? Camera. Yes.
**Mikołaj Świątek** 00:39 Wasn't that other camera? Pointing.
**Benedikt Bongartz** 00:42 I guess the other camera is just closed. It's my laptop, which is.
**Mikołaj Świątek** 00:47 Okay.
yeah, I have my open. So sometimes when zoom gets mixed up, I I end up being shown from like from the side as well.
**Benedikt Bongartz** 00:59 Yeah, rejoin the team. Supposed to work on open telemetry things now, instead of.
**Mikołaj Świątek** 01:09 Sort of what?
**Benedikt Bongartz** 01:11 Instrumentation for manage control plane.
**Mikołaj Świątek** 01:17 Doesn't that involve open telemetry.
**Benedikt Bongartz** 01:20 It does involve open telemetry. Yes, but more just going through this pieces of code and adding stuff, and expect right and dealing with fluent bit.
**Mikołaj Świątek** 01:35 That's a good.
**Benedikt Bongartz** 01:36 Vector because that's what is set so.
But I learned a lot about fluent bit.
**Mikołaj Świątek** 01:45 My condolences.
**Benedikt Bongartz** 01:48 Hmm.
**Mikołaj Świątek** 01:49 My condolences. I feel sorry for your loss.
**Benedikt Bongartz** 01:53 Hello!
**Mikołaj Świątek** 01:58 Hey, Antoine, I think Jacob should be here.
**Benedikt Bongartz** 02:17 Oh, the last meeting looks like it was quite empty.
**Mikołaj Świątek** 02:20 Yeah, it was just me or a bit right. I was also I was hoping a little bit for or for Tyler as well because he has opinions on this topic.
In particular, the Htp. Convention. Do you know if Pavel's gonna be here today.
**Benedikt Bongartz** 02:52 I don't think so this week and next week he's not isn't here.
**Mikołaj Świątek** 02:58 Oh, cool. I'm gonna ping Jacob and get started. I think.
right? So. Topics topics. I'm a little bit afraid to share my screen, because last time I tried earlier today, it ended up just not working for arbitrary reasons. But we'll I'll try that. Now.
please tell me if you can see this cool.
**yurioliveirasa** 03:37 I can see your screen.
**Antoine Toulme** 03:38 Yep, I can see it.
**Mikołaj Świątek** 03:40 Okay, success. Alright. So we have this issue.
It is largely unresolved. I thought we kind of maybe resolved it quietly by just upgrading stuff and not caring, but apparently not so the to those of you who don't remember the the issue is that there is a breaking change in https, semantic conventions when they move to stable, and each instrumentation library is, of course.
moving at its own pace to adopt that putting in some, you know some escape hatches to for users to be able to use the older behavior. What we do for Java and.net have adopted it earlier is that on.net. We've just frozen the version and on Java we've also frozen it. But Java also actually released Java actually bumped their their big number on it, too.
So I would like to try to start resolving this somehow.
and the question is, how to do it the main problem, as I see it is that when we manage the instrumentation version, the instrumentation image per user and they upgrade, they won't see any immediate effect. Only when they start cycling their pods. Will they see pods with the new instrumentation version.
and only then will they see the breakage.
And that is a very painful thing, because then it's also difficult to revert from that once you do it.
So I'm wondering if there is any way for us to to do this breaking change in a way that doesn't, you know. Just make our users incredibly mad at us for good reasons. In this case.
**Jacob Aronoff** 05:35 So can. 1st off. Can you hear me? Okay.
**Mikołaj Świątek** 05:41 Yes.
**Jacob Aronoff** 05:42 Okay? Yeah. My, my thought was that we could couple this to bumping the version for the instrumentation Crds, so that it's clear that it's like A, you know, you're we don't do an opt in like migration like we did last time.
We just make a new instrumentation. Crd version like a v 1, beta one for it.
And people have to actually manually do the change which would actually force things into it so that they're very aware that this could be.
**Mikołaj Świątek** 06:19 That's 1 way. That's 1 way to do it. The only problem of this is that you would actually have to do the view on Beta. One migration.
**Jacob Aronoff** 06:26 Yeah, I I know this. But we we've also been talking about doing a new a new design for the instrumentation resource, anyways, and I don't. Is there a rush for us to upgrade this semantic convention? Or would it be worth us spending like a month or 2 doing some design for the new Crb.
And.
**Mikołaj Świątek** 06:50 I wouldn't say I wouldn't say there's a rush, but we like we ship like increasingly older and older versions of the.net and Java instrumentation by default.
and that is like an increasingly large problem.
**Jacob Aronoff** 07:08 Yeah.
**Mikołaj Świątek** 07:10 And I'm not sure if I want to couple this change with some redesign that will happen at some unspecified point in the future.
Like we can't we? Where we can't tell when we'll release it.
**Jacob Aronoff** 07:26 Are we able to do like a v 1 alpha, 2 of the same resource, and we just make that option.
Yes, we can.
**Mikołaj Świątek** 07:36 Whether that's a good idea.
I'm not sure I can tell you what I thought, what I thought of instead.
Yeah, yeah, we we.
I had a much simpler idea. So we do upgrades right? We we. What happens is that if you create an instrumentation Crd, and you don't set your images. Then what we're gonna do in our default or web hook, we're gonna A, we're gonna set the images to. What is the current default? And B, we're gonna set a bunch of annotations which basically say, Hey, automatically upgrade this image version.
And then we have, like an upgraded process that looks at instrumentation crds and Crs, it looks as instrumentation crs, and for each of them, where there's an annotation saying, Hey, upgrade the python version, it actually upgrades it to the new, to the version. That is the current default for the operator.
And I was thinking, whether we could do something like.
look, you know. Look at the look at the version, for example, let's say the.net instrumentation. Look at the version of the.net instrumentation. Somebody has said.
if they have set the current default, which is like 1, 2, 0, then leave it alone.
If it's a newer version, then upgrade.
and the effect of that is gonna be that we're not gonna break anyone, you know anybody, any existing installations, but for new instrumentations. We're gonna have the the latest as a default. So at least we're not like making the problem worse over time.
And this actually like lives
**Jacob Aronoff** 09:19 Yeah, I think the only worry with that is still the that you're ultimately gonna break their like downstream instrumentation, right? And if we're doing it as like an automatic upgrade. They might not be aware of that. And so things might just break on the up.
**Mikołaj Świątek** 09:32 No, no, no, no!
Strings can't break, because this would only like existing existing instrumentation. Crs would stay the same. Nothing would change.
It's only new one that would get the new version.
**Jacob Aronoff** 09:47 Oh, oh, I see! So like a new someone creates a new instrumentation, and we add a flag about. Is that the idea.
**Mikołaj Świątek** 09:57 Yeah. So basically for new instrumentations, we would use the version with the breaking changes.
But for but for ones which already exist, we would keep them as they are.
**Jacob Aronoff** 10:11 Okay.
I don't know anyone else have thoughts.
**Mikołaj Świątek** 10:24 Right now.
**Benedikt Bongartz** 10:25 This approach, so I was proposing to just add a flag to the crd, but having it with the versions this way.
just print the warning so that you're aware that it will not be upgraded automatically sounds good.
**Mikołaj Świątek** 10:40 It would be. It would be nice to put that in the status actually, not just print a warning right? Because who who reads operator logs.
**yurioliveirasa** 10:49 Yeah, yeah, you're right.
If you can personally start us, you know, would be great. Yeah.
**Mikołaj Świątek** 10:59 But also yes, when we upgrade the upgrade to when we bump the Crd version in some future.
then we can also change this then and say, You know, be aware of this breaking, change the the the problem with with planning to do that, though the problem with planning to do that is, that again, every instrumentation goes at its own pace for this, and we have only 1 point where we upgrade the the when we change the instrumentation. Crd version like, right now I tried to. I like I tried to compile who is where and what and it. And it seems like I was wrong about 2 of these things. Actually.
the I was. I was right about the go. The Go auto instrumentation already includes these changes. It looks like. But the python node version. Have you have to opt in via a flag? So I suppose we could also, when we.
when we introduce instrumentation view on instrumentation view on data. One will also start setting this environment variable if it's not default by that time.
But it's also. But it's still a little bit.
we're we want to do one breaking change. But this is, in fact, like 5 or 6 breaking changes spaced out. So it's not that easy to control, unfortunately.
but I, at the very least, for Java and.net. I think we can do what I said, and it's going to be safe to do this and and and it will at least stop the problem from becoming a bigger problem over time.
Antoine, do you have thoughts? You look you look you look as if I'm giving you a headache.
**Antoine Toulme** 13:11 No, not really any thoughts today on that. It's a it's a bit I didn't. I didn't think about it at all, so I don't have I have any insights.
Sorry.
**Mikołaj Świątek** 13:25 This is like this. We've known about this for a while now. So I think we should actually like stop start dealing with it somehow.
I wonder how how we can deal with things like this in the future. Hopefully, we won't have any like massive baking changes this way, because we like we as the operator, really just lack tools to do this.
We we don't have. We don't have any any good way of like. Normally, you know ship a breaking change. Whatever you ship a breaking change in the collector. Sure we can try to. We we can try to fix it by changing the collector configuration typically as we are doing right now. Anyway. But here it's like, at least, if you if there's a breaking change in the collector, you. You usually see very obviously immediately that you have a problem, whereas here it's
**Antoine Toulme** 14:26 It seems like a repeat of the ongoing issue where the operators ends up, being responsible for the disparate behavior of all instrumentations. And we're going to go into set discussion again about like how we end up being responsible for how they are delivering.
that we need to kind of go up to them and tell them that they need to kind of have a harmonized way of delivering those breaking changes, so we could do that through some flag or something.
**Mikołaj Świątek** 14:53 I don't I? I'm not even sure if there is a way from our perspective to to make this like, what would they do to make our life easier, like I guess I guess you know. Make it easier to do like. Make it easier to switch, I guess, but that that only makes our lives a little bit easier, right? We still have.
**Antoine Toulme** 15:11 They could, they could offer both support for both. Instead of making it a breaking change, they should offer a feature gate for this, and then we should be able to turn that on and off and do that at the level of the implementation as a whole or something like that I mean this is this is cut by cracked by discussions right there. This is not really suitable.
but the other thing is that the operator does not really have the like you said the tools, but also even the the ability to kind of orchestrate this type of changes across different presentations like this. But I'm also just guessing at the issue. I'm not familiar with this.
I would say that the injector project is going to have the exact same issue right.
**Mikołaj Świątek** 15:51 Probably I mean so I maybe not, because there's only one reason. There's only one reason. This is an issue in the operator, and that is that the operator ships defaults.
If the operator did not ship defaults, if the operator completely, you know the the.
you know, wash its hands, it's a much worse user experience for that, especially people who want to try for the 1st time. But if we washed our hands of that, then we don't have a problem because we don't have a breaking change like you just have to set it. And then it's up to you when you upgrade it right. It's the all the responsibility goes on. The user.
**Antoine Toulme** 16:34 I think we're doing we're going into a direction of having more opinions baked into the operator. And the experience, right? So we're actually
**Mikołaj Świątek** 16:44 I think this is better for users if we find a way to to handle this, and for for the collector, I think we've been actually doing it reasonably well, like the I just merged the Pr from Tyler, which fixes a a bug in in the recent collector. Release early. Actually, it's a bug in open telemetry. Go, but they like shipped it without noticing it.
So so this is fine, and we can do things as long as it's like reasonable, we can reasonably detect them, which in in this case we did.
But for for instrumentations here, it's it's again, it's due to the nature of the way the injection works.
It's like, difficult to tell users that they have to do something.
and you know I can write. However many pinned issues I want. But the majority of our user base are not. Gonna look at this.
anyway, like at at the very least, I think I think there's agreement that the upgrade solution is is like reasonable, like, it's not the solution to the whole problem, but it's like a way to make it less less impactful. And I think also, another thing that should happen is that we should like in our change log, we should just keep linking this Htp, we should, we should make it so that the instruct that the issue explaining this, this one has remediation, or at least it has. It links to some kind of guide, telling you what, whether this, how, how to tell. If this affects you, and what to do about this, and we should just keep keep linking it in in our release notes so to to try and try and to give it more visibility. I I can't really think of much else. And yeah, if we if we bump the if we bump the Crd version that actually does work. But that's like something that we can't really do very often.
but if we do do it we have to time it in a way where it's maximally impactful.
Anyway, I'll I'll write this down a little bit later we can move on to the second thing, which is also mine.
and it's related to what I said about the collector in the we've now had, like 2 recent collector releases which which contained bugs which were meaningful for us, and we actually skipped one release. We skipped oh, 1, 28 O, because they had a bug in Prometheus receiver, that it was actually a bug in Prometheus. They had a bug which we like couldn't really work around without making things incredibly hacky. And it just broke all the target allocator completely, basically as an application. So we just skipped it. And now we had a different one. I don't know if you, if you've looked at this, but this is the fix where and and the upstream issue is here in auto. Go! And the collector, the collector pulled that change in and shipped it without noticing it, and then, when we tried, when Tyler tried to do the release he noticed failing end to end test because the metric claims have changed.
So, putting aside, putting aside like the the fact that these things can slip through.
I think that's something we should do is just run our end-to-end tests daily on the contrip image, because both of these problems were detectable by our end-to-end tests, and if we had reported them earlier they could have been fixed before the release.
So and I don't think this is like a big lift for us.
**Jacob Aronoff** 20:55 Yeah, I I think it's a good idea. I also wonder if we should have a slack bot or something that I don't know if we see a failure, we'll just report it to us, or maybe open up an issue in the operator repo and like tag us, or something that's probably easier, because then we can give it to the collector people as well.
**Mikołaj Świątek** 21:13 Thank you.
**Jacob Aronoff** 21:14 I I just want it to be. I want the failure to be loud and actionable, not just like.
you know, theoretically, the thing that when it fails it should only fail on one of these changes, not just like a random failure. And if that's the case, we should be very loud about it, because we know that it will break something downstream.
**Mikołaj Świątek** 21:35 Yeah, I I thought an issue would be simpler as well.
**Jacob Aronoff** 21:39 Yeah, I think an issue as long as it like tags, like, you know, operator cruisers or something you don't want it to like, yeah, not tag anybody.
but otherwise that sounds good.
**Mikołaj Świątek** 21:51 Yeah. And and there's like a related related chain. So if we agree about this, then then I'll I'll create an issue about this and I also have like, maybe this is a question, because this this behavior actually predates my work on the operator.
Like, if I go to Tyler's release. Pr.
does anyone know why is it that we wait until the release? Pr to bump the the collector version in in versions txt.
**Benedikt Bongartz** 22:43 I haven't here in for a while, but as far as I remember, we discussed this, and we agreed. After the release. We can bump it immediately.
but I guess nobody did.
**Jacob Aronoff** 22:55 I think the ideal is that we bump it with the release, because oh, wait, wait! See, I have to think about this for a second.
You're you're saying you're asking, why can't we just bump this as soon as the collector bumps it, and then we release separately.
**Benedikt Bongartz** 23:18 Yes.
**Jacob Aronoff** 23:22 I'm trying to think if that would cause any issues with versioning.
**Mikołaj Świątek** 23:27 And then.
**Jacob Aronoff** 23:27 We don't publish an image ourselves. So we do the same thing for auto instrumentations, don't we? Oh, no, we don't. We dumped auto instrumentation versions with this, as well.
**Mikołaj Świątek** 23:38 Yes, but the difference for auto instrumentations. We well, until a recent change, until a recent change for auto instrumentations, we would bump them here as defaults.
Oh, no, you're actually right.
But for auto.
**Jacob Aronoff** 23:56 Because the images wouldn't get released until you know, this actually might be because we used to have a different release process.
And I think that we've gotten we've made. We've sifted the entire release process now to actually release the images with versions on the operator release. And I think before, we might have not been doing that. It might have just been constant, not the operator image, but the other images. I think we're just always existing.
**Mikołaj Świątek** 24:27 Yeah, because, like the difference between which latest image is released and which is the because this this file controls. What is the default in the operator?
**Jacob Aronoff** 24:39 Yeah, yeah.
**Mikołaj Świątek** 24:42 So I honestly think for a bunch of these images. We could bump them immediately as well, but because we now, because we now run tests on the latest instrumentation images. Anyway, that's like rest, less impactful like if something's broken, we know immediately after a new image is is like immediately after you change an image in a Pr, and you submit a pr, if you broke something by that, there's an end to end. Desktop profile.
Yeah.
**Jacob Aronoff** 25:11 I I think I'm for this. I mean I don't. I can't think of what could go wrong if we did this. Given the.
It's the release that would actually update the defaults for users.
**Mikołaj Świątek** 25:24 Yes, and and here you can even do this with with renovate pretty easily, because there's a the collectors releases repo. You can just go by by the releases on that repo.
**Jacob Aronoff** 25:36 Yeah, that's that sounds great to me. I I can't see why not? And I think that, combined with the with a runner for the daily things. We can do the same thing for instrumentation problems, too.
right? Where it's like we run it daily. And we report any failures to to an issue.
and if there's any instrumentation failures, it'd be the same thing.
**Mikołaj Świątek** 25:58 Maybe that's expanding the scope of it too much. But for instrumentation it's more complicated because the images are are artifacts. So we would actually have to find a way to build like the dev images for instrumentation on our own.
For contrib. We can just take the image that contribute publishes. So it's straight.
**Jacob Aronoff** 26:17 We building? The images for each button. Now.
**Mikołaj Świątek** 26:24 come again!
**Jacob Aronoff** 26:26 Aren't aren't we building the instrumentation images on each run for the end to end tests? Now.
**Mikołaj Świątek** 26:30 And like using them.
Yes, but those are still images that are actually released, like they have a pinned version of the stuff like you have an instrumentation image like for Nodejs. Then you have some version or some released version.
the of the SDK library in there.
I don't know how hard or easy it is to to have yeah depth image in there. And honestly, we haven't really had problems with instrumentations in this manner.
**Jacob Aronoff** 27:02 Yeah.
**Mikołaj Świątek** 27:02 Yet we've.
**Jacob Aronoff** 27:03 I mean, I think initially, it was initially with this instrumentation problem.
That's right, the one the one from the 1st part.
But either way, I think this is a good idea.
I actually have to drop right now. Unfortunately, I have another meetings to get to.
but I also think we're at the end of things. I don't have anything else to bring, but.
**Mikołaj Świątek** 27:27 Okay.
Sure. Thanks.
**Jacob Aronoff** 27:30 Thank you, Nikolai, for for running this.
Okay? See? You.
**Mikołaj Świątek** 27:35 So yeah, so you can just do a quick review of feature gate.
I see. I see Antoine already went. Does anyone have any feature guys to like to bump up here.
Maybe we should bump this to Beta Bennet. This one's yours.
**Benedikt Bongartz** 27:55 I did like to. Yeah, I have an open thing there with native sidecars.
I need to look. I have an issue that I would like to close up front.
I don't remember exactly what it was to be honest. Half a year ago.
**yurioliveirasa** 28:18 Yeah, but I remember that you've been working on it on the native sidecars, right.
**Benedikt Bongartz** 28:24 I guess it was discovering this automatically, so that the feature gate can be removed. So we check the Kubernetes version we check. If the feature gate is enabled.
**yurioliveirasa** 28:34 And if that's the case, we it's automatically a native sidecar.
**Benedikt Bongartz** 28:39 Or you can then turn it on, and it becomes a native site code or not. Something like this. I guess there is somewhere an issue for it. But since I was away for a while, I don't remember.
**Mikołaj Świątek** 28:50 I mean intuitively. The way it should work for me is that you should check the Kubernetes version, and if it supports native sidecars, then we use native sidecars, and and this whole thing is also controlled by the feature gate.
**Benedikt Bongartz** 29:02 Yep.
**Mikołaj Świątek** 29:02 Right?
But yeah.
**Benedikt Bongartz** 29:08 Because then we can safely enable this, no matter what version you're on, and it just automatically detects it. And if it causes trouble, you just disable it, and it works again.
**Mikołaj Świątek** 29:16 Yes.
I think I I will like open an issue about turning this into Beta. And this is like a pretty scary, scary thing, because it affects every single target allocator installation. Again, it's like we use Mtls to to communicate between target allocator and Prometheus receiver.
And it's important because when you okay, you have to go.
**Benedikt Bongartz** 29:44 Yep, see that there's the other one is already starting.
Sit in. Sorry.
**yurioliveirasa** 29:50 See you again.
**Mikołaj Świątek** 29:57 And then he froze.
**yurioliveirasa** 29:58 Yeah, yeah, yeah.
**Mikołaj Świątek** 30:00 Look! Look! Look at them! Look at them!
**yurioliveirasa** 30:02 Yeah.
**Mikołaj Świątek** 30:04 I wonder how long he's gonna stay this way.
**yurioliveirasa** 30:07 Yeah, the zoom, yeah. The zoom sometimes behaves like crazy.
All right.
**Mikołaj Świątek** 30:15 Alright. I think I think we can. I think we can conclude then.
**yurioliveirasa** 30:21 Okay.
**Mikołaj Świątek** 30:21 0.
**yurioliveirasa** 30:23 From my side. I don't have any any topics. I basically working. Yeah, I'm back working in a couple of issues because I'm quite out of the product. But now I'm back again.
Great.
Yeah, okay? And.
**Mikołaj Świątek** 30:44 Do you want? Do you want some? Do you want some issues that.
**yurioliveirasa** 30:48 Let me. Yeah, let me just finish one, and then I'll ask you. I'll ask you for some, because the one I work with. It's basically I don't know if you are catching up that. But the precedence of the mood, the the instrumentations, annotations are not working as expected, like when you have a SDK annotation set on your namespace, and you have a specific language set on your pod.
This part does not take precedence of the namespace annotation.
**Mikołaj Świątek** 31:29 There's a you have a Pr, which is also about multi container.
**yurioliveirasa** 31:34 Notation. Yeah, yeah, I'm trying to fix it.
**Mikołaj Świątek** 31:38 I don't understand. I don't i i'm not sure if I if you ask me right now how this actually worked, I wouldn't be able to tell you to be honest.
**yurioliveirasa** 31:45 No, it's yeah. It's it's like easy, because it's forget about the whole thing, about annotations, you know. Just keep in mind the precedence of pods. Namespace. If you have one specific annotation for instruments, all the applications present in one namespace. So which means you just basically just set an annotation, your namespace.
and the operator will take care of that. Otherwise, imagine you have a specific application, a python application, or Nodejs application that should be instrumented in a different way, you know. So this annotation set on this specific on this specific pod or specific deployment should take precedence of this namespace.
That's it, you know it's not. It's not a big deal. It's just about. It's just about fixing the proper, the proper way. When you have this this, this scenario of a much annotation, you know.
but anyway, it's not a complex one.
**Mikołaj Świątek** 32:56 So is is that why your pull request is plus 600 lines.
**yurioliveirasa** 33:01 Something like that. Yeah.
**Mikołaj Świątek** 33:04 So simple. It's so simple. Let me let me actually yeah, plus 6, 20 minus 92.
**yurioliveirasa** 33:10 Yeah, let me let me check because I I submitted that kind of update 2 days ago. If I'm not mistaken.
**Mikołaj Świątek** 33:22 All the instrumentation. End-to-end tests are failing.
**yurioliveirasa** 33:26 Yeah, it's week. Where is this? What is this?
Yeah.
it's the the concept is, yeah, you're right. But the concept is because the SDK, yeah, the SDK annotation is a different annotation of the the rest of the specific language annotation, you know. And then you have to test. If you have these different annotations and check what should takes precedence over what you know is, yeah, it's made it simple like that. But anyway.
**Mikołaj Świątek** 34:12 There you go!
**yurioliveirasa** 34:13 Okay, that's great. So we meet together in 2 weeks.
Thank you, man, bye, bye.
