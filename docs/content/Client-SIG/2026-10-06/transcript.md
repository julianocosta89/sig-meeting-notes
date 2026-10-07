SIG: Client SIG
Date: 2026-10-06
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Martin Kuba (Raintank, Inc. – Grafana Labs)** 00:41 Hi, Ben.
**Ben Joseph** 00:45 Hey, Martin.
How are you?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 00:49 Doing alright, how are you?
**Ben Joseph** 00:51 Good, good. It's been a while since I joined this.
But I'll pop in, see what's going on.
**Michael Bushe (Mindful Software, LLC)** 01:24 Well, Ben, I don't think we've met.
**Ben Joseph** 01:28 Hi, Michael.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 01:30 Michael.
**Michael Bushe (Mindful Software, LLC)** 01:32 ever.
**Ben Joseph** 01:36 Hey, yeah, just want to introduce myself. I'm from Grafana. I primarily work on the Android side, I'm a little bit on the Swift side as well.
Are you part of the, Lutter Dart Repo, I think I've seen your name somewhere.
**Michael Bushe (Mindful Software, LLC)** 01:55 Yeah, that's right, that's right. I'm donating the, Mindful Software SDK and API to, it's in the process of donation now. We have a repo in OpenCollemerty Dart and a SIG that started last month, and so yeah, we're excited about that. We're working hard to get that.
donation and process, and I'm working with Robert Magnuson.
**Ben Joseph** 02:15 Yes.
**Michael Bushe (Mindful Software, LLC)** 02:16 Fellow maintainer on that.
**Ben Joseph** 02:18 Yeah, he's my colleague, so yeah.
**Michael Bushe (Mindful Software, LLC)** 02:20 Yeah, very good.
**Ben Joseph** 02:22 Nice to meet you.
**Michael Bushe (Mindful Software, LLC)** 02:23 Nice to meet you, too.
**Hanson Ho** 02:25 Hello?
**Michael Bushe (Mindful Software, LLC)** 02:27 Hey, Hanson.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 02:28 Hi, Hanson.
**Hanson Ho** 02:30 Sorry about the Red Sox.
Yankees are gonna go out too, so hey, maybe take comfort in that.
**Michael Bushe (Mindful Software, LLC)** 02:38 Yeah, Tampa Bay is gonna crush him. I'm very excited.
**Hanson Ho** 02:41 I want to raise Brewer's, World Series, just to shake it up.
**Michael Bushe (Mindful Software, LLC)** 02:48 Yeah, that'd be great.
**Hanson Ho** 02:50 You're really good.
Okay, I'm trying to… let's see, wrong doc.
I can share this. Someone else can help take notes.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 03:03 Yeah.
**Hanson Ho** 03:05 It's.
I haven't looked at your PR, Martin, but I'm very excited about accepting it.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 03:22 So, the browser one?
**Hanson Ho** 03:23 Yeah.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 03:24 Yeah.
**Hanson Ho** 03:33 Nice.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 03:35 Okay.
**Hanson Ho** 03:43 Let's see.
We can probably get started in about a minute.
I dialed into the Android meeting at 8 o'clock this morning, and I was like, oh my… and I couldn't get in. It's like, oh yeah, we changed it.
Still bad at remembering things.
like.
Things change.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 04:48 They do.
**Hanson Ho** 04:50 All right.
**Michael Bushe (Mindful Software, LLC)** 04:51 Moved my cheese.
**Hanson Ho** 04:53 Yeah.
Never read that. Never will read that.
Alrighty, no other topics, we can just talk about, semantic conventions.
So Morton opened up some issues and the PR, so these are just issues, on…
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 05:20 you.
**Hanson Ho** 05:20 Our repo.
So, yeah.
Hmm.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 05:28 Yeah, basically, so I went through the… The namespaces in the core.
Registry.
And just opened issues for each of them, for discussion. I think we probably want to migrate all of them, but… Yeah, I think we should probably have people look at that and think about it.
The… I also… the two other… that I was wondering about is, There is Android and Ios namespace as well. In in the Okay.
In the… code owners file in the core registry, those are assigned to different, set of approvers. So, like, the iOS goes to iOS approvers, and Android goes to Android approvers.
So… Obviously.
Hanson, you're here to represent Android, but I do wonder, like, if we should check with the iOS folks about migrating those iOS namespace.
And for Android specifically, I also wanted to, I guess, double-check, like, if… you kind of feel the same as what we made… what we thought for browser, in that… your existing registry in the Android SDK repo would also move here.
**Hanson Ho** 07:00 So we've opened up the discussion, but I think folks haven't, looked at it, in detail, so we're gonna talk about probably more in a couple days. But I think my proposal is that we… don't define a public registry for Android. We basically pull from Upstream.
And upstream being not… actually, that's a bad word, because this is federated. There's no upstream-downstream, per se. The dependencies, which includes this one, includes the core one.
And if there are attributes we have, we should put them in internal, make them semantic conventions, but not publish a version registry.
the Android namespace, I am not aware of any… continuing attributes that we want to maintain from that. I actually don't even recall a single Android attribute that we are using. So, for Android, unless there is something like that, I would be inclined to… Pull the namespace in.
Deprecate the existing ones, and simply not add it.
So, we technically own the Android namespace, but we don't have any attributes, unless we really, really, really need to. We as a client-side repo.
I haven't confirmed. I mean, Ben could probably speak to part… because he's a prover on Android as well now, so he could probably speak to that a little bit, but certainly be part of the discussion when we talk about it in the SIG, later this week.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 08:40 So do I understand correctly? Oh, sorry. Go ahead, Ben.
**Ben Joseph** 08:42 No, I just want to… yeah, there are no specific Android-specific attributes, as far as… I was just… Checking at the same time. Yeah, I don't think we have any.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 08:53 There is, so, like, you don't have… So you're saying that it's like you don't have any… conventions in the Android SDK repo.
**Hanson Ho** 09:03 We, we, we do, but, we're gonna… I've… so some… most of them are.
they're not published as semantic conventions, so to find the file so that we can do the generation, but they're not… they're not, like, a published semantic convention anywhere. So the goal, I think, my… my… what I think we should do, you know, again, pending, you know, everybody's, agreeing, is move all those ones into, the Semantic Connection Client side repo.
But they're gonna all have, I think they're all under app or device or something like that. And, app are the ones that are, I think, newer. Device.
and mobile, I think there may be a couple of them, or ones that were like, you know, they were added a couple years ago, we're not really sure if this is… we're gonna maintain that namespace. And if we are, we may just want to, like, port them, like, deprecate.
If device.something is, you know, exists in the core repo, we want to deprecate it and make new ones.
in the, in the client-side repo, and basically consolidate things under the app namespace. And what I was talking about, about the Android namespace, I meant, like, attributes, semantic conventions that… or attributes that are… that are Android dot whatever.
I don't think those exist, and if they do, we should really scrutinize, like, do they really, really need to exist?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 10:32 Okay.
**Ben Joseph** 10:33 Yeah, sorry, I think there are certain attributes, like Android power save mode, things like that, but I think they are nothing that is specific, or that we cannot migrate to a common Yeah, common attribute.
Common namespace, sorry.
**Hanson Ho** 10:53 Yeah, unless we want to tie it specifically to the implementation, the Android implementation, but I don't think people are using it… well, it depends what the actual.
instrumentation is. So, I'll be creating some issues there, and we'll be looking at the namespaces, or rather, instrumentation one by one on Android, and see where… which bucket fits. But I think this repo, if we have anything in Android, this client-side repo should own it. I'm hoping we don't, but unless we do, and then we just… we just put it over, so…
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 11:22 Okay.
So, okay, so, no issue for that. I'll just leave that up to you. I think the only thing that, there actually are two attributes in the core registry, and I don't know, like, if they're used anywhere. If you click on that link.
It's like, yeah, under Android 2 attributes. Yeah, that one.
**Hanson Ho** 11:46 Oh, yeah, I'm sure, I'm sure there are, so it's probably under mobile as well.
Oh.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 11:52 Okay.
**Hanson Ho** 11:53 Okay.
API level? Okay.
Okay, then I guess we'll just move this over, then. Make sense?
I don't know where specific… I thought we were using.
I thought we're using the, the general OS version, but I guess OS version, maybe we're talking about 16, versus API 37, or whatever, so…
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 12:18 I will create an issue for it, maybe just double check, and maybe we could… if you're not using it, we could just deprecate them.
**Hanson Ho** 12:25 No, I think that is… that is exactly the type of platform implementation-specific thing that would require, I think, an Android namespace. So, we probably then need to kind of pull it out and use it.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 12:42 Alright, yeah, I'll so I'll create 2 more issues for these 2 namespaces.
**Hanson Ho** 12:46 I think, somebody was gonna talk to, iOS… Was it Ted?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 12:55 Third, yeah, that was going to…
**Hanson Ho** 12:57 We'll ping them.
But yeah, I'm looking forward to finding the time to actually catalog all the ones that we're using, and then slot them into various buckets, because I think it's going to be either get rid of, we migrate the namespace and deprecate, or we, change the name and deprecate.
we are not… I don't… yeah, I don't think Android is going to want to publish, a separate registry. I think… I think people will be down for that, because That's another thing to maintain, and nobody wants extra things.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 13:37 No, no.
Okay.
**Hanson Ho** 13:44 Cool.
Cool, so we're done with that topic?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 13:51 Yeah.
**Hanson Ho** 13:51 All right, oops, where is it?
So I just posted about, publishing, artifacts, from repos.
literally 10 minutes ago, well, I guess it's 15 minutes ago now. So I haven't heard back, which is obviously not surprising, the correct thing. But we will be getting, I think we should make a decision by next week, one way or the other.
But we don't have to do that right now to get the browser namespace stuff in. We can always generate a version.
publish the, registry, stamp it, and then add the artifacts later. Even if we have to do version 2, 3, 4, before adding artifacts, we don't have to necessarily… I mean, we could always build, you know, artifacts for old versions, but.
I don't think we need to if we have the latest that contains things that people want to use. So, that decision doesn't block anything. So we can proceed with the, the client side. We're adding actual conventions.
And then doing tests on the builds and things like that. You can just clone it to your own repo, run a build there, delete the repo, you know, just, yeah, don't publish it from… From the main one, that's all.
And if we do it right now, yeah, it's probably fine too, because nobody cares at this point.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 15:24 Yeah, I mean, the artifacts… a kind of, secondary thing, right? Like, we… Yeah.
So.
And, like, we don't even need to.
do a release yet, I mean… I think… I don't… I don't know, like, if… I don't know that, like, even, like, the Gen AI semantic connection SIG actually has done a release.
**Hanson Ho** 15:45 Yeah, with the release, I think doing the release, is more like, especially the first few releases, is more like ironing out the kinks in the process.
We're gonna have a dev registry and a stable registry. It's based on the same YAML, but they're effectively different identities, right? So, we need to figure out, if we press the button, what happens, the versions, the, you know, how pinning is gonna work, and… So I almost… almost wanna just do a release and see where the… because I've tested this, but just not, like, officially. So I just want to see where the, the bad things lie. So.
And I think you would want a version to pin to, when you actually consume it, right?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 16:36 Yeah, yeah.
No, for sure.
Yeah, all I'm saying is that I don't… I don't think that, Like, it's been… it's been… doesn't seem like it's been a priority to do a release for the others.
**Hanson Ho** 16:49 That's… that's true.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 16:50 Yeah.
**Hanson Ho** 16:51 you.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 16:52 But yeah, sure, we can do that. I guess the question is, like, do we want to do it as soon as we have something, some conventions, or do we want to, like, get some of these other namespaces in first?
**Hanson Ho** 17:04 0.1 goes to 0.2 very easily, so I definitely… especially if we're just doing dev, like, I don't think we should have a stable release until there's a bigger, you know.
thing that others may want to use, especially if the browser conventions, by definition, are development right now, and there are no stable conventions.
the stable convention will be empty. But when we actually start porting, say, session, those were stable before, so we should probably keep the stability. Or, actually, are they stable?
They may not be. There are some that… in some namespaces that are stable, I think. And when that happens, that's when we have to decide whether we want to release, you know, zero point.
7-0 stable.
you know, with one attribute or something like that.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 17:55 Right.
I do wonder, like, I haven't thought about this, but I do wonder, like, if you have two different, Like, stable and development releases with different schemas.
For different versions, and we would want to, like.
Which one?
would the telemetry actually use?
I guess, I don't know if there's a way to, like.
use both. Anyway, it's… I have to think about that.
**Hanson Ho** 18:27 one sh… if… if the versions are the same, one should be a superset of the other. And when you are pulling in the registry to consume, or an artifact to consume.
you are saying dash dev or… or no suffix. So you are selecting one or the other. So if you're using the no suffix one, and you try to reference a dev one, they just… it just wouldn't be there.
at the same time, if you pull in the dev one, you're… immediately also getting the stable version of whatever that is. So hopefully, dev just gives you more, and it wouldn't… well, it should definitely not contradict, because on the same version.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 19:13 All right.
**Hanson Ho** 19:13 Dev and stable should be the same. So, which is why it's, I think, good to kind of keep the versions, in sync.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 19:20 Okay, okay, yeah, makes sense.
**Hanson Ho** 19:27 Cool. Alright, I guess I will submit PRs as I… as I get them done, for… for the info stuff. I don't know, I remember… which repo is where now, but, you know, you'll see them come in. I might want to enable stacks, because I think even the last one, I was, like, adding adding commits, and… doesn't feel good. But if I… but I also, you know, having PRs, I go into non-main, it's… so, if you guys don't, mind, I want to try to figure out how to enable, GitHub Stacks, and basically create, I don't know, an integration branch.
So I think as maintainers, we have the ability to create the integration batches.
Or branches directly on the repo, and basically have that as the route to stack against, and have that be merged in, or something like that.
Yeah.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 20:22 Sounds good.
**Hanson Ho** 20:23 Cool. All right.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 20:26 If you need any help with that, let me know.
I don't know, like, is everything that you're going to do captured now in issues, or…
**Hanson Ho** 20:36 Absolutely not. I will… I will try to do that. I am notoriously terrible when it comes to matching tickets with PRs, but I will… I will, for the sake of transparency, do that, much more here.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 20:51 Okay, yeah.
Yeah, and for me, the last thing for me is the… the browser namespace PR was in draft last week, and I took it out of draft. I don't think there's any reason to have it in draft anymore.
I did know that you… we merged the first… your first PR. It… it did… I did generate the docs from that as well, so that's now part of that PR as well.
So, yeah, take a look. And, like, all of this, all of this in this PR, all of these conventions are, experimental.
And they basically reflect what we have in the instrumentations. They're not documented anywhere else, so I kind of feel like there's… it's like a kind of no-brainer to just get them in, and we can iterate on that, so…
**Hanson Ho** 21:43 Yeah, I think we're looking at, you know, I think a similar issue in Android, where it's almost like dev… defined in dev gives you an expectation of what they are, so we explicitly say these are not forwarded, supported indefinitely. But when you don't define it, and it's just kind of in there.
the… the support statement is non-existent, so people have ideas. So I also agree that I'd rather have things in dev, even if they're wrong and poorly, kind of, you know, whatever, it does… it's better than not having it anywhere, so… Yeah.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 22:18 Exactly.
Just essentially just documenting the state, the current state, yeah.
**Hanson Ho** 22:23 Correct. The only exception is if there are namespace conflicts. So what I don't want is basically, you know.
Us defining a dev in a namespace we don't own, because then… that could be weird, but for browser, it's browser, there are no browser ones, or maybe there's a couple that you need to migrate. But it's, it's, it's gonna be here, right? So, unless, unless, less worried about that. Unless putting it, you know, OS or something like that.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 22:51 Yep.
**Hanson Ho** 22:55 Cool.
Michael, any thoughts about… about… want to get Dart into this, or, at least, maybe even just when we start thinking about artifact generation or consumption, or even, like, in your repo, the instrumentation, consume the YAML.
**Michael Bushe (Mindful Software, LLC)** 23:14 I'm thoroughly confused about how I'm gonna go about this, but I'll tell you that, the, our first step… so we're still donating, and we're gonna pull in from my Mindful Software repos into our new OpenTelemetry Dart repo. And we're gonna do it in at least 3, maybe 4 stages, maybe a couple more. But the first stage is getting our semantics out of what's now delivered inside the Dartastic API.
And so that will be delivered separately. I think from what I'm hearing, I'm not sure how to go about this, but, I think what I'm hearing is maybe just for a first cut, we'll just kind of do a simple rip that's… it's already… we've regenerated from you know, all the common semantic conventions.
Maybe we'll start with that. I don't think… I don't think there's any… letter… specific things in there right now. That was… that's for… that's really… it's a Dart library. So, for Flutter, which is what, you know, we're concerned about, I do have some to donate, from other work that I do, and that will probably be added in as proposed semantics, and then… or I can do that there or here.
In that process, as I go about that, I think what I'll also do is make sure that there are.
So, again, I'm worried about each platform, so there's app lifecycle, and that's specific to Android, specific to iOS, and so that's when the rubber will meet the road, and we'll have to figure out how to best.
how to best… again, I'm still confused. I have to think about… take some time to really think about how this could work and, you know, and get to a place where people are consuming it, and people are consuming it at a stable level.
**Hanson Ho** 25:16 So, the first thing you should do probably is just pulling it out into a local registry that you don't publish, so similar to what Android is doing, so it's at least in, like, the Weaver YAML v2 format. So when you actually do the migration and, you know, either move it here, it's, you know.
the YAML's valid, and it's just a block, and it's just about the content. And you know exactly what attributes you have, rather than, oh yeah, there's a hard-coded string somewhere in there. So that first step, doesn't make anything public. It's just, like, a code refactoring, so that, that… doing that is a prerequisite, probably.
**Michael Bushe (Mindful Software, LLC)** 25:58 Yeah, good point. I'm immediately thinking about publishing it, because once we pull it out, then the API that is published at it's got hockey stick growth, a lot of people are using it. You know, we have to take care of those folks, so, I don't… and I don't want to see too much drift, so I would like to depend on it very quickly by publishing just the semantics, to PubDev, that's the registry for Flutter, and And depending on it and the API.
I'm hoping that I could then publish it.
It's not stable, and then consume it right away. Why are you recommending not publishing?
**Hanson Ho** 26:37 Oh, no, I'm talking about if you're still trying to figure out where things are going, and whether the attributes are, like.
semantically means what you… we want it to mean going forward, especially if it's generic and also specific. So… So, eventually getting into dev makes sense if you're like, these are good, I want to support these going forward, and they don't clash with anything, and the definitions are shareable, all that stuff, then, yeah, make it go into dev. But, you know.
Yeah, so… So you can directly pull it up.
**Michael Bushe (Mindful Software, LLC)** 27:11 So the way it is now is, it's off the core convention, so if it's stable in there, it's stable. If it's not, it's not. And as things move out, then we can deprecate I don't know if then deprecating things that are stable. I got to think about this. I I take a deeper look at it.
**Hanson Ho** 27:31 It's getting to stable that is gonna be, like, measure three times, cut once. Getting into your local unpublished repo, whatever, do whatever you want, doesn't matter. Even if you're hijacking namespaces, changing the meaning of an existing one, that's… okay, because it's not real, per se. It's not, like, semantic convention's real. But getting into dev semantic conventions, even client-side.
it's a little bit real, especially clashes with the definition. If you want to redefine, like, you know, app.lifecycle.change or whatever, if that exists, you know, that is where it's like, you know.
Even Dev is a… is… is… needs a little bit of discussion, versus, if it's something on your own namespace.
Whatever.
**Michael Bushe (Mindful Software, LLC)** 28:17 I've got to take a few days and just focus just on this, just to see if I can come up with a plan. I don't have it yet, but yeah, thank you for the insight.
**Hanson Ho** 28:25 I think we're going to be running into different problems, but very similar on various different platforms. So, it's almost like we'll migrate one, and then, like, the other migrations are gonna be, like, similar, and then we'll take a look at the flowcharts of individual platforms, and where it goes. The paths are gonna be probably similar, unless you find a new Path, which could happen as well, so… Right.
**Ben Joseph** 28:55 Just, just before we wind up, Hanson, so how do we want to migrate, like, I understand, like, some of these are in core. Do we want to pull that into the Android repo and then, like, discuss how we should rename it to something generic, and then move that to the, client repo?
**Hanson Ho** 29:13 If they're defined in the core semantic conventions, and their names are not gonna change, then it's a matter of managing the deprecation in core, and publication in R1. The good thing is, deprecated things are still usable. You're just pointing it to a place that has, this is what the new one is. So we may want to have the, this is the new one, before we fully deprecate. But no one's gonna… if you use an old version, it's gonna still work. It's when you update to the new version that's gonna be a little bit problematic.
So managing the transition, honestly, it may just be a documentation and, like, getting people to be aware issue.
even naming is like that, until you change the implementation. And that's when we're like, oh, if we, you know, foo goes to bar, and it means slightly different thing.
Is that a major version change? And is that a major version change in terms of science conventions, or in the instrumentation? Like, this is where… this is where… because we can't… yeah, well, we can discuss when we actually get that, so I think… Taking one of these issues that Martin has written and, and seeing, how that migration is going to go, and if there's stuff for Android, that you want to kind of… specific instrumentation you want to pull out, and kind of take a look at in detail, I think that would be really helpful as well.
**Ben Joseph** 30:41 Okay.
Alright, alright.
**Hanson Ho** 30:44 But I guess we have a… the ones in Android are all under AppDot, so that's, like, the… the big one, or many of them are under AppDot, so that's going to be the big one.
**Ben Joseph** 30:53 Yeah, the other ones are like where I think we would need more probably Android SIG discussions also.
**Hanson Ho** 31:01 Yeah.
**Ben Joseph** 31:04 Got it.
**Hanson Ho** 31:06 Cool, let's get a foot in the door, and by checking in some real conventions, and then we go from there.
Alright, I'll take a look at the PR, and…
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 31:17 Cool.
**Hanson Ho** 31:18 All right. Thanks, folks. We're at time. Talk to you next week.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 31:22 Thanks, Hanson. Thank you, everybody.
**Michael Bushe (Mindful Software, LLC)** 31:23 Good week.
