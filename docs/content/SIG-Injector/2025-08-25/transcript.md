SIG: SIG Injector
Date: 2025-08-25
Duration: 23 minutes
============================================================

## Zoom Recording Transcript

**Bastian Krol** 02:45 Hello, Antoine.
**Antoine Toulme** 02:47 Hey.
How are you?
**Bastian Krol** 02:51 I'm fine, how are you?
**Antoine Toulme** 02:53 It's Monday, yeah.
Got binged about a little bit. ….
**Bastian Krol** 03:00 Oh, I'm sorry to hear that.
**Antoine Toulme** 03:02 Yeah, it's tough. It's life. …
Yeah, I'm taking another look at the…
Seek PR… I really have nothing to say about the Sikh code itself, because it's… it's vague, so I don't know anything about this. It seems to compile, I guess.
**Bastian Krol** 03:18 Same as me, like, two months ago, so….
**Antoine Toulme** 03:21 Okay, yeah.
It's an awful amount of code, actually. It's, it's quite a bit.
**Bastian Krol** 03:27 Yeah, it's quite a bit more than the previous…
Version that's set for sure.
I'm… yeah, that's… actually, that's something that I thought about, how we should…
handle a review for this, because it's basically a full rewrite, so it's just a lot of stuff all at once, and going through every line of code.
like you would for a smaller PR, maybe? I don't know if that's productive or efficient. If you have any ideas, we can, at some point, walk through it together, or whatever comes to your mind.
**Antoine Toulme** 04:05 I would say it's not a bad state to… in the life cycle of this project is a great time for this type of PR, right? If it were two years from now, and we're supposed to be stable, and things are supposed to be, you know, hunky-dory, then I think we'd have a very different discussion, but given that we're just starting out.
and we're just trying to move forward. This is a great way to get something in, start to get some community, get more people to look at things, and when they run… when things live in PR, sometimes they get less attention, so…
we would need to… I think it would be much better if we land this PR and break something, if we don't land this PR and don't get the attention that this code requires.
Is that….
**Bastian Krol** 04:47 Yeah, no, I'm on board with that. Just… still, we want to land it, and you probably
we just don't want to lend it just blindly, completely, so… somehow we need to handle that part, but….
**Antoine Toulme** 05:04 Sometimes you gotta take a gamble a little bit, because….
**Bastian Krol** 05:07 Oh, okay.
**Antoine Toulme** 05:07 You know, even if I do an excellent job of reviewing every single line of that code.
I can't think of every use case or anything like that.
**Bastian Krol** 05:16 No, no, I don't mean review in the sense of we are absolutely sure that this will work in 100% of all cases for all scenarios, so that…
Anyway, if you have any…
Suggestions or anything, how we should approach that, or how that makes it easier for you also, then just let me know.
**Antoine Toulme** 05:40 I think we should… …
I'm gonna ask for others, like, you know, besides me, there's… I should not make a decision by myself.
**Bastian Krol** 05:51 Hmm.
**Antoine Toulme** 05:51 But I feel… I feel good about it.
Getting this in and dealing with the consequences, versus not dealing this in and having a lengthy discussion about reviews that don't land anywhere.
**Bastian Krol** 06:02 Okay, sounds good. I still want to tackle, …
the open points that I mentioned in the PI description first, I think, just so that…
Sure. So I think the main part… last week, the state was that .NET was not yet really in, that's… that's done now, and they're also….
**Antoine Toulme** 06:24 Cool. This, this configuration mechanism….
**Bastian Krol** 06:28 wasn't in last week, so there is now a configuration mechanism that can read from a file in ETC. It's a little bit different than what you had before, before you had just, I think.
Files per runtime, and then environment variable key-value pairs.
**Antoine Toulme** 06:48 But that makes sense. Your new approach takes every language at once.
**Bastian Krol** 06:52 Yeah, right, so this new configuration file is just one single file, and it just says at its moment where the main instrumentation agent is for that runtime. So there's a property for Node.js, and tells you where the node module is.
So, same for JVM, for the Java agent, etc.
**Antoine Toulme** 07:14 Yeah, so I'm looking at the checkpoints that you have. It's like the hard work is done of having .NET working, the .com file kind of figured out, and the rest of this could be separate follow-ups, which is that adding.
**Bastian Krol** 07:29 stroke.
**Antoine Toulme** 07:29 Adding checks around this is kind of a…
I think I had maybe some of that before, maybe I'm wrong, but pretty much, for daily and RPM package types test, we would just run it inside a Docker environment where we would simulate having the RPM being available, right? We package it, we install.
**Bastian Krol** 07:50 No, I didn't… I saw tests where the binary was used, but I….
**Antoine Toulme** 07:55 Oh, shit.
**Bastian Krol** 07:56 test where the actual RPM or depth packages were used, but maybe I overlooked that.
**Antoine Toulme** 08:02 Well, I might also be misremembering things, because we do that for other things.
**Bastian Krol** 08:07 Yeah, that would be super nice to have at some point, to also have integration tests with the packaging included, because that can also go wrong, but I don't think those existed yet.
**Antoine Toulme** 08:20 Well, so I think that's an issue that can be tackled separately from this PR.
**Bastian Krol** 08:24 Yeah, but I still would like to… and I think that's not too much work. I would like to get the… so, right now, the packaging is definitely broken, so I would…
kind of like to fix that before we land it, so I… but that shouldn't take super long.
So, and some… some… and I think then there's some READMEs and contributing MD, which I just need to follow up on, so that wouldn't yet now take, like, months, but maybe a week more of work, and then it… I think it's in a slightly better shape to be merged.
**Antoine Toulme** 08:59 Okay. If you think… You want to do that, bump out to you, for sure.
**Bastian Krol** 09:05 Okay.
**Antoine Toulme** 09:06 So… merging Renmies… Thing like that. Okay. So, at this time, are you a member of OpenTeometry?
**Bastian Krol** 09:18 I…
Actually, not entirely sure. So, me personally, I'm, … you, you mean the contributor agreement? Yeah, I, I contributed other stuff already.
**Antoine Toulme** 09:32 Oh, yeah.
**Bastian Krol** 09:33 the….
**Antoine Toulme** 09:34 You're a member. That's it.
**Bastian Krol** 09:35 Yeah, okay, no, no. Sorry, I was, I was…
I was somewhere else. I was thinking about, … I'm also in…
in the WCC community a little bit, and there you… your company needs to be a member, and we don't have that, but that's not the case for….
**Antoine Toulme** 09:52 No, not for Cynthia. No, that's it. I think it would make sense to… so, in a sense, …
this contribution is so big that it rewrites pretty much the whole repository anyway, right? So, I would want to make sure that as you make this contribution, it also puts you in a place where you can continue to maintain that contribution, right? So….
**Bastian Krol** 10:13 Right.
**Antoine Toulme** 10:14 I'd much rather have you also join us as a maintainer as part of that.
**Bastian Krol** 10:18 Absolutely.
**Antoine Toulme** 10:19 reason anybody, but I think that would make sense.
**Bastian Krol** 10:21 Yeah, no, no, for sure.
**Antoine Toulme** 10:24 So, that would, that would give you the, the, …
the rights, per the OpenTeometry project, the way things work, right, is that you have multiple levels of ladder. Because this is a new project, you would move directly to Maintainer. Maintainer.
**Bastian Krol** 10:38 Okay.
**Antoine Toulme** 10:38 and, approve. You can merge, but you need an approval from another approver or maintainer.
**Bastian Krol** 10:47 Oh, yeah, that's a good point. So, just for me to understand the formalities of that, but maintainer is per project, so that would be maintainer for… specifically for the injector.
**Antoine Toulme** 10:58 Yes.
**Bastian Krol** 10:58 Yeah, okay, no, that makes sense.
**Antoine Toulme** 11:01 And then, so there's some branch protection rules, which is that a maintainer is not supposed to merge their own stuff without a first in approval for someone else. I might be wrong about this, but I think that's the case. So…
….
**Bastian Krol** 11:18 Is that managed via GitHub teams, or how is that… does that work?
**Antoine Toulme** 11:24 Yeah, I think if you become a maintainer, you'll be able to access the admin project, which is another project under OpenTeometry, which is a bit more protected, because we don't want.
**Bastian Krol** 11:37 Two minutes.
**Antoine Toulme** 11:37 actually seeing others, but what you would see is that there's a terraform approach that they've taken at this point, because there are so many projects. Yeah, yeah, sure. And this is kind of encoded as a standard, where you have, like, the maintainer team being, yeah, able to merge, but needs approval, but branch protection rules are kind of standard across everybody.
So, yeah, in some cases, some projects actually have a two approvals requirement.
I….
**Bastian Krol** 12:07 Might be too small for that, but….
**Antoine Toulme** 12:10 Yeah, it's very much too small for that.
**Bastian Krol** 12:11 Fuh.
**Antoine Toulme** 12:12 Yeah, so I want to make sure that you understand, like, getting this code in is also tying you to this project.
**Bastian Krol** 12:20 That assumption is absolutely clear to me. I mean, just dropping that off and then saying goodbye, that would be a not-so-great move.
**Antoine Toulme** 12:32 If you say, look, I just want to make this contribution, but then my job, my day job is elsewhere, and I have other things to do.
That's fine, right? But we…
me and other maintainers, then we need to make a call. It's like, okay, not only are we getting this code, but we need to understand that. If you're saying, no, I'm here to stay, and I will maintain that and help out.
I mean, okay, great, right? It's much easier for us. I… I don't need to drop everything I'm doing, go and learn Zig tomorrow to kind of get on top of it.
**Bastian Krol** 13:01 Yeah.
**Antoine Toulme** 13:01 Which would have been a bigger expenditure of energy, so….
**Bastian Krol** 13:05 Sure.
**Antoine Toulme** 13:06 Yeah, okay, so you're saying, okay, let's, let's take another week, go through the RPM Debian package, maybe do a little bit of that README consolidation.
**Bastian Krol** 13:15 Yeah.
**Antoine Toulme** 13:15 You feel pretty good about everything otherwise, and… Yeah, Phil, let me know…
What else I can do here? It feels pretty good about all of this, and…
… what would be the next step?
the thing that is also on the… in the open issues was to build, eventually a Docker image with this. So, once we have…
a sense of what the Debian RPM package looks like.
we could pretty much replicate what the operator is doing, so here's what I have in mind, is we…
We land your code in a week or two.
Make it so that Debian RPM works, great. Maybe we make it really is… I don't know. Maybe, maybe not. We still… the point is, to me, is to try to have more people join our meetings.
try it out, tell us more about, like, a use case or a weird idea, or maybe have some guy from the RubySync come and tell us, hey, this didn't work. Who knows, right?
**Bastian Krol** 14:16 Yeah. ….
**Antoine Toulme** 14:17 But then the next step for me would be, we take exactly what you have, and we make it into a Docker image, and we replicate what the operator was doing by
copying the content into… as a Unit container into another Docker image.
And run it and see if it actually plays out the way we would think.
**Bastian Krol** 14:35 Yeah, so, my thoughts around that is I would very much like to consume… so once we have that container image in place, I don't think that necessarily the OpenTelemetry injector is a place for the
init container mechanics, I think it should build the container image, and then others, like, like an operator, can take it from there.
**Antoine Toulme** 15:02 Okay.
**Bastian Krol** 15:02 Because that's…
more and more Kubernetes mechanics, attaching an init container to an existing Kubernetes workload, that's maybe something else. But anyway, I'm getting off track. What I wanted to say was, I want to…
obviously replace the specific dash zero inject drawer that I have in… over in our dash zero operator repository, and consume it from here. That… that's…
That way, I think that that gives us two benefits. A, it gets a bit more test coverage. B, it makes sure that I stay around, because if I want to see a bug or I need to change something, I will need to change it here.
**Antoine Toulme** 15:45 Right. And, see, it's a proof of….
**Bastian Krol** 15:50 Concept that it can be used in that way, so….
**Antoine Toulme** 15:54 Yeah, yeah, absolutely. Also, we can start to kind of engage with the different SIGs, like the Java SIG, and tell them, hey, we're building this image of yours, and we'd like to also make you cod owners of this particular code path, so that if you break something, you can go and fix it in the injector project.
So you can also not have to maintain all of this yourself.
Because for any vendor, right, even from Splunk, or Cisco, or Azure, or whoever, having the burden of building all those Docker images is not fun, not useful. Yeah.
Yeah. So, okay, but, yeah, so the… that's… that's a discussion I'm having with you, OperatorSig, is where…
this injector code right now lives in the operator, it's kind of intermingled with the CRDs. It's been difficult for me to make it possible to use it without the CRDs, and that's a bit of a fight I've had. I've finally managed to explain that in a concise way to people.
**Bastian Krol** 16:49 Okay.
**Antoine Toulme** 16:50 And, … I… yeah, what I'm trying to do here is to…
to see if I can, …
find a middle ground. The point that I made at the last operator-seq meeting was.
We have a Helm chart, and we should not have any CRDs in that Helm chart, because Helm does not like CRDs.
how do we fix this so that the configuration can be passed in as Helm configuration, just YAML, values, config maps, whatever you want? And how do we make it so it's somewhat agnostic to all this?
So….
**Bastian Krol** 17:23 Yep.
**Antoine Toulme** 17:24 No, no.
**Bastian Krol** 17:24 Yeah, … I mean, we discussed it a little bit, last time, and I was wondering why Z-0 operator has not had that issue, and I think afterwards, I'm pretty sure now that what the
Main difference is, is that, we never…
deploy any custom resource based on our own custom resource definition via the hand chart. What we do, though, is, we give a user… so maybe that's something that you might want to
consider as an option. What we do is we let users specify, basically, all the configuration values for one of these custom resources.
And that is then passed as comment line arguments, basically, or you could also….
**Antoine Toulme** 18:16 That's what….
**Bastian Krol** 18:16 And then, at startup, we wait until the webhook is ready, and everything is ready, we pull it until everything is
fine, and the resource is… the custom resource definition is there, and in a retry loop, and then we… the operator process, the manager, installs the custom resource. And that seems to work.
quite nicely.
**Antoine Toulme** 18:41 Yeah, it makes sense. The issue I've had in the past is that the operator would do something, a bit of a knucklehead move, would be to look for CRDs to be there.
**Bastian Krol** 18:50 Yeah. It would fail if the CRG was absent, for some reason.
**Antoine Toulme** 18:54 And then, because this thing is registered as a webhook, it would then fail the invocation and creation of any pods moving forward in your community's cloud.
**Bastian Krol** 19:02 That's… that's not a great user experience.
**Antoine Toulme** 19:04 Yes.
I explained that to the guys last time. I was like, this has been a bit of a wrenching moment, where you have to tell them, like, I think you just build on the whole cluster now, and nothing can work.
Don't want it.
And my engineer's like, oh, but you can just mark the errors ignore. I'm like, okay, that's not better. That's actually what you…
you don't know what's what, right? You don't know if it works, if it doesn't.
**Bastian Krol** 19:28 We'll just fail at a later stage, probably then.
**Antoine Toulme** 19:32 There's more communication on that, because you could also make the point that this injector would work very well in Lambda environments.
And so we haven't talked about that.
**Bastian Krol** 19:41 at all.
**Antoine Toulme** 19:43 But think about…
or use cases like this, right? So it could be, you know, there are more esoteric things that we have to support, like Nomad. We have to support… Nomad is really out there.
We have to support, Fargate, CCS type things.
It's somewhat non-community-centered, what Lambda is actually a…
I think a big one that could be targeted by these type of things.
**Bastian Krol** 20:09 Oh, I'm… is that… yeah, I don't know. I mean, I… I was quite engaged in Lambda instrumentation back at my previous, previous company at Instana. I mean, Lambda has probably moved a lot.
And then… so back then, you wouldn't have been able to use something like the injector, because you didn't get any access to the underlying container or processes, or anything.
But that's, like, a long time ago. Of course, now you can build Lambdas as container images, then you can use that, but I think the other way is still around it by just uploading a zip. I'm not sure if anybody's still using
That, but that would make it harder, because you don't have access to the… underlying, …
Yeah, operating system level stuff.
… Okay. Yeah.
**Antoine Toulme** 21:03 I'm just putting it out there because the moment you have this type of content environment, I want to make sure….
**Bastian Krol** 21:08 Yeah, for container-based Lambdas, it could be a thing, but Lambda is also, I mean, it's very different from everything else, because just everything freezes once the cord has been processed, potentially, and you have to make sure your telemetry has been sent out.
Beforehand, and you don't have anything still from the last invocation when your process is sorted again, that makes it really….
**Antoine Toulme** 21:34 I think people complain about that.
**Bastian Krol** 21:36 mute.
**Antoine Toulme** 21:37 Yeah, there were some complaints about that recently from, from Mosers, and so we've seen two ways to do that, mostly using a collector, which happens to be either in the Lambda layers.
**Bastian Krol** 21:48 That's true.
**Antoine Toulme** 21:49 full shutdown moment where you get 5 more seconds to kind of exit.
**Bastian Krol** 21:52 Yeah.
**Antoine Toulme** 21:52 War….
**Bastian Krol** 21:53 Lambda layers are the way to go for instrumentation, I think. At least that was, like, 4 or 3 years ago, not sure what has changed.
**Antoine Toulme** 22:02 No, nothing has changed.
**Bastian Krol** 22:03 Yep.
**Antoine Toulme** 22:04 It's been very much a frozen technology in time, as far as I can tell.
**Bastian Krol** 22:07 Because we see the same thing over and over. The only problem has been maintenance is expensive, because you have to automate.
**Antoine Toulme** 22:14 Again, the Docker image creations.
in their publication. So, to me, it's more like a commodification of the stack. How do we make it easier for people to consume the SDKs out there? Right now, what we're having is multiple ways to publish those Docker images, right? At the SDK is going to do their own, plus now we have ours, so…
I think it makes this easier overall, like…
You know, maybe our… maybe this injectory Docker image could be just drawing from all the Docker images from all those
SIGs.
And then copy the contents into a final image that has, like, all those things in there.
Maybe that's the way.
**Bastian Krol** 22:55 What have you.
**Antoine Toulme** 22:55 Name.
**Bastian Krol** 22:58 Cool, okay, … Yeah.
Not sure what else….
**Antoine Toulme** 23:04 I think we're good. I'm gonna keep you.
Thank you so much. Thanks for your work.
**Bastian Krol** 23:10 Okay, yeah, let's just keep talking, at latest next week on Monday, and if I have anything in between.
But by the way, if you… that's not urgent right now, but if you say you have some setups where you test stuff with RPM and Debian packages that are built in the same repository, that might be interesting to carry over at some point.
**Antoine Toulme** 23:37 And be renters, yes.
**Bastian Krol** 23:40 Cool. Okay.
Excellent. See you around. Bye-bye.
**Antoine Toulme** 23:45 Bye! Talk soon.
