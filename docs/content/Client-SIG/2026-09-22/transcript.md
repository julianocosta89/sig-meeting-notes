SIG: Client SIG
Date: 2026-09-22
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Hanson Ho** 00:23 Always have to unmute.
**Jared Freeze (Palo Alto Networks)** 00:25 Yeah, that's the new way.
**Hanson Ho** 00:29 Sure, I can configure it so that I don't have to always unmute, but it's… today is not the day I find that setting in Zoom.
Good morning.
**Martin Kuba** 00:37 Hi, guys.
**Ted Young (Raintank, Inc. – Grafana Labs)** 00:50 What up, y'all?
**Hanson Ho** 00:52 Hey, Tad.
Hi, Michael, I don't think I've met you. Nice to meet you.
**Michael Bushe (Mindful Software, LLC)** 01:16 Hi, Hanson. Yeah, I've chatted just a little bit on Slack, that's all.
I'm, new maintainer in a Dart and Flutter SIG that I bootstrapped with my, with my, SDK. So, it's Flutter, I'm on the client's side.
I'm here to check it out and make sure that we're all… I'm in line with the… With what everyone's doing.
**Hanson Ho** 01:39 Perfect. Excellent.
**Ted Young (Raintank, Inc. – Grafana Labs)** 01:42 I was gonna say, congrats on… on liftoff on all of that, Michael. It's…
**Michael Bushe (Mindful Software, LLC)** 01:47 Yeah, Defaro, this is a… I'm a huge, huge Red Sox fan. I saw The Steel, if anyone knows what that is, and, yeah, Red Sox season ticket holder. I'm not… I'm in France now, so unfortunately I'm missing it. But, this is a… I've been watching the Red Sox for a long time, and This is one of the most exciting seasons. It's been a… Currently.
**Ted Young (Raintank, Inc. – Grafana Labs)** 02:09 Considering.
**Hanson Ho** 02:10 I'm wondering how poorly it started.
**Michael Bushe (Mindful Software, LLC)** 02:13 Yeah, they were really terrible, and I'm glad I didn't watch too much of the beginning of the season, but I caught the rest of it.
**Hanson Ho** 02:19 Crochet's coming back, everybody's hitting… I'm sure the boos are working out. Not to delve into baseball talk, but, you know, I can go on.
**Michael Bushe (Mindful Software, LLC)** 02:28 Yeah, are you… so you must be a baseball fan if you follow it that close.
Amethy.
**Hanson Ho** 02:32 I'm a Blue Jays fan, I'm in Canada, so, by default, since they ripped the expos from us,
**Michael Bushe (Mindful Software, LLC)** 02:39 you know.
I'm looking for my Blue Jays hat. I actually have a Blue Jays hat. But my daughter and I were watching the Blue Jays last year, and she really liked the Blue Jays, and she thinks the hat's cool, so I went a little outside of my, you know, comfort zone, but it's okay, it's for my daughter.
**Hanson Ho** 02:57 2 inches, that's, that's all, that's, that's all.
**Michael Bushe (Mindful Software, LLC)** 03:00 Oh, I know, that was… I was certainly, open to thinking about that.
**Hanson Ho** 03:03 Less than a second. Anyway,
**Michael Bushe (Mindful Software, LLC)** 03:06 Yeah, yeah, about what's important.
**Ted Young (Raintank, Inc. – Grafana Labs)** 03:09 Yeah.
**Hanson Ho** 03:09 Less sad things.
**Ted Young (Raintank, Inc. – Grafana Labs)** 03:11 Yeah, add yourself to the meeting notes, please add your name under attendees if you're here, and if you've got anything to talk about, add it to the agenda.
**Hanson Ho** 03:27 wait… actually, we waited 4 minutes already. The baseball talk has eaten up all our waiting time, so people are around here. So we can get started. Who's presenting?
**Ted Young (Raintank, Inc. – Grafana Labs)** 03:43 Nobody.
**Hanson Ho** 03:44 Okay.
**Ted Young (Raintank, Inc. – Grafana Labs)** 03:45 You wanna present? It's your topic, Hanson.
**Hanson Ho** 03:47 Sure… I am just horrible at, taking notes and talking at the same time, so I don't mind presenting, but the notes will be sparse.
**Ted Young (Raintank, Inc. – Grafana Labs)** 03:59 I can take notes.
**Hanson Ho** 04:00 Sweet.
Right?
Cool! So, I finally had some time to… put up the PRs for the client-side repo, so out of the README, thanks for merging it, Martin. One of you merged it, I don't know who merged it, somebody merged it, the initial README.
So I have another PR out there that basically, tries to create doesn't actually add any of the semantic conventions, because, you know, I don't want to put in sample data and have that be like, ugh. So, but it contains the scaffolding, to process any data that's in the model, directory, and generate, READMEs, and etc. for it. I also have another one that I haven't put up. Well, I did put one up as a sample to go on top of the PR, that basically, hey, if you add these YAML files with the proper definitions, it'll generate the proper, markup files, or markdown files, for documentation.
And I also have another one that… that I want to talk about before putting up, about, cutting releases.
So, you know, we can test out, like, pinning to a dev release and things like that. I got some other PRs coming up to basically consume these as a test, just to see everything works. It worked before, it should work after, it's just a matter of changing some stuff.
So, that PR is out for review, just… hopefully unopinionated use of Weaver tooling, and some templates that, generate docs, feel free to, nitpick, on the wordings and things like that, because this is where… This is where we do it. If we… if we let something in there that is, like, it'll live, forever, so let's just, like.
You know, nitpick the hell out of the wording for the templates.
So after that, there's probably a few more things to decide before we actually make this, a living and breathing concern.
Which is, we need to release something that's pinned. But before that, we had to decide how we actually set this stuff up. So basics… include, well, what is going to be in here in terms of namespaces? So the idea is that, from the Semantic Convention, meeting I was at last week, we will own certain namespaces and deprecate existing you know, usages in the main one, and basically have it live in this repository. So, there are ones that are, like, out there that we're kind of using, but I don't know if we're alone in using. So app is one.
There are ones that start with session, is another one.
I think there's some old ones that are, like, Client or whatever, so they're… they're probably… we can probably come up with an exhaustive list of… of what… could be appropriate for us to take in here. And I'll… obviously, there's also the, the new ones. I don't know if browser exists right now, or if you want it to exist in that form. So we can talk about, you know, candidates for that. I don't believe there's an Android one.
We try to put everything in app, and thus far, we haven't needed an Android one, but eventually, we probably want to. And whether that's app.android, whether that's android.
again, something to be discussed. So, it's probably… you don't want to… we don't need to boil the ocean, but we need to figure out One or two that we should move right away, just so that we have some momentum going.
And yeah, let's… we can hear some candidates, for that.
Cloud Browser, I know there's a bunch of ones that, Martin, you have queued up to kind of go in. Are they net new, and are they a net new namespace?
**Martin Kuba** 08:12 No, so browser already exists in the course and the conventions, like, not a lot, but there's some.
But yeah, I mean, the goal was to move it out of there. The question for me has been.
should it go into here, or should it go along with the browser SDK? Like, I don't think that question we haven't resolved yet.
I think as a first candidate, maybe there's, like, something that's… that's, like, less controversial, like, or less, like, more obvious, maybe, like, the session one. We could just, like, move immediately, I think.
**Hanson Ho** 08:49 session or app,
**Martin Kuba** 08:50 Vision or rap, yeah.
**Hanson Ho** 08:54 Okay.
**Martin Kuba** 08:56 I mean, I would like.
**Michael Bushe (Mindful Software, LLC)** 08:57 How to get my hand up in Zoom here, but, if I may, so, both Flutter and KMP have multi-platform concerns. So, I can imagine that Flutter developers or KMP developers would want not only… Flutters, I hope I can contribute, I know I have a bunch of Flutter-specific things. And, for example, things like lifecycle, is different on every platform.
So Flutter has a lifecycle, Android has a life cycle, iOS does too. And a Flutter developer might, you know, they can say.
when I'm… when this is running on iOS, use this, and when I'm running on Android, use that. So I tend to think of the semantics as above everything else.
And the browser, too. Flutter does the web in WASI. So, putting them up a level so that they're, they can be used across, all the, all the platforms and all the UI SDKs would be… would be advantageous.
**Hanson Ho** 10:07 Dad?
**Ted Young (Raintank, Inc. – Grafana Labs)** 10:08 Yeah, I'm actually really glad that we have Flutter as part of this, when we're embarking, because it leads to precisely this question of, like, how generic are we trying to make things? You know, because we now have a cross-platform option.
But also, like, to what degree is the… the cross-platform thing actually flutter? You know, like, versus trying to make everything super generic so that there can be… you know, genuine cross-platform semantics. I think that's definitely something we have to… have to explore.
**Michael Bushe (Mindful Software, LLC)** 10:49 Well, that's a good point. So, so Flutter developers, I could, in the Dart SDK, pull in the client-side ones that are, So, for example, in the browser SDK, or an Android SDK, could pull in all the common ones from here, and then include… an Android would include Android, browser would include browser, Flutter would include semantics from all of them.
Because there will be times… for sure, there would be times for flooded developers where they want to respond to certain parts of the Android lifecycle, or the iOS life cycle.
**Ted Young (Raintank, Inc. – Grafana Labs)** 11:29 Because I think we're probably going to get into, I imagine, some brine zone, right? There's some things that are clear-cut, platform-specific, aka the dumps that we get directly from the platform, right? Like, the browser just dumps you page load.
And that's something that the browser gives you, and, like, we shouldn't try to generify things like that, obviously. But then you have things like clicks, you know, button presses, and stuff like that, where I predict it gets, like, a little messy.
You know, database semantic conventions are, like, the other place where… Where it's always, like… like, there's seemingly no perfect answer to generic versus platform-specific.
But… so I… it would be interesting to start maybe mapping out some of those spaces as well, in addition to, like, the platform-specific ones.
**Hanson Ho** 12:26 I think that's… that's where it becomes interesting, is we always like a generic rule to say, you know, it's either one way or the other way, but unfortunately, there's too much nuance in each of these use cases.
So, there has to be discussions. Like, ideally, things can be genericized in such a way that there is one semantic convention with optional attributes within it.
That, basically, you have a click event, but there may be different attributes for different, platform-specific things. Like, if Apple decides to invent a new way to measure pixels.
you know, I'm sure Apple developers are gonna need it, because Apple will do what Apple wants. Do we want to basically then have, like, a weird, you know, so, general coordinates are defined in certain ways for all platforms, but then for Apple, there's this unique type. Do we then spin up a new, like, Apple coordinates?
That is the kind of weird stuff that we're gonna have to discuss, but having everything, I think, centralized initially, like, in this client side space would be good. More to Martin's question about where, the things live, I've asked in the repo, or in the semantic convention Slack, we'll see what they say, but my read on it is that, they don't say platform, they say, implementation, specific, runtime, so it is, I think.
a lot more specific and generic, or specific to, you know, if it's a… if it's an, you know, I don't know, a Firefox one, maybe that belongs in its own repo, but if it's browsers in general, I think… I would like to think that we could put it in somewhere common, but it is a good idea to not move things until, you know, we get across all the T's and dot the I's and stuff, so that one we can wait, but hopefully we'll get an answer back. If we don't get an answer back, we should just decide, ourselves in this group.
one less repo to maintain is always good, and you're not bound to versions. Like, like right now, if we were to have, like, an Android semantic convention federated.
is the versioning going to be the same as, you know, our artifacts that, read the registry and generate the artifacts? Like, I think it's confusing enough as it is, like, what is a version of a registry, versus, and having it mingled in with, like, the Android, or, yeah, the Android, release Gradle modules that contain.
generated, numbers. Oh, you said it's 1.7. No, no, no, the registry version is 1.1. You know, then, you know, so separating that, I think, for Android, you know, I think that's what direction I want to push in. So, but we can certainly listen, to what they have to say and make a decision.
You know, in due time.
Okay, so…
**Ted Young (Raintank, Inc. – Grafana Labs)** 15:21 By the way, is that we should… Make it… make, like, a good college try to shove everything up into this… This shared repo, and just, like, try, and then if we're like, ugh, then, you know, pull back.
But, like… we won't know whether or not it's annoying unless we try, and my feeling is that it will be better, especially if later on, like you're saying, Firefox or Chrome or somebody comes along, and they're like, we would love to, like, take ownership of some some chunk of this, like, forking that out again from a main repo seems like a more sane way to do it than this, like, nested doll of Of semantic conventions.
So, if we could eventually get everything moved back up into this client-side repo, I think we should try to do that.
**Hanson Ho** 16:15 Yeah, I'm, you know, I'm biased towards lazy, so, having set up another repo, or another registry, at least, in the existing repo, and having another version, you know, managed, so, so, you know, if, you know, cross-platform, like React Native or Flutter needs to pull in different conventions, they don't have to, like.
what version of each I have to manage, you know, it's just… One less thing to worry about, but… and we could, you know, the path to moving it out is also just there. Like, we just do what we did, but, you know, move it to a different repo. And I do see a world where this repo is so big, in a couple years, fingers crossed, that's a champagne problem, that, oh yeah, the cadence and the velocity and the review groups, really, you know, certain things should be its separate registry. And at that point, spinning it off, I think would be… would be… you know.
Relatively, hopefully, easy, because we've done it once already, so… yeah.
And no one has, as far as I know, published, a federated semantic registry, a semantic convention registry. Gen AI and, and Mainframe are the most advanced ones.
But they have… because of all the migration stuff, they haven't actually published anything yet. So, if we go at the speed that I think I want us to go in, we will probably be the first. So let's make the first small, and, and kind of go iterate from there.
Okay, so, who's gonna take a look… who has the time, I should say, to take a look at, what… what appropriate ones, we should perhaps start moving over? app and session being probably the two candidates.
**Martin Kuba** 18:03 Yeah, I can make time for some of that, yeah.
**Hanson Ho** 18:05 Excellent.
**Martin Kuba** 18:06 And also, so it sounds like, to me, like, just to reiterate, it sounds like we have a decision on putting the browser and Android-specific ones into this repo as well.
Like, right? So…
**Hanson Ho** 18:20 Unless the folks come back and say, no, no, no, you read the thing right, and they should be in separate ones, and then we'll cross the bridge when we get there. I'm hoping that doesn't happen, because that means somebody… you have to set up another registry, and then publish it, and basically do everything we're going to be doing here, bootstrapping, so…
**Martin Kuba** 18:39 Yeah, the reason I'm saying that is because, like, we actually have an open PR in browser SDK to add semantic conventions, so if, you know, once we have that like, finalized, I can just move that PR over here, so…
**Hanson Ho** 18:51 Yeah.
And that's in the browser namespace, right?
**Martin Kuba** 18:56 Yes.
**Hanson Ho** 18:57 Okay, so that would be… that'd be pretty clean, then. Actually, that'd be… actually, that'd be ideal, but, you know.
Okay, cool. So Martin's gonna take that. I will write down action items… Oh.
**Michael Bushe (Mindful Software, LLC)** 19:20 Oh, we're switching, Martin. I kind of have done this work a little bit before. If you want to look at the DART API, where the semantic conventions are.
I have a pitch of what I've… what… as I've gone through them, what I thought were live and good, and what some of the ones that I've gone through over time have been deprecated, so it might help you.
I can send you a link.
Cool. One of the things is, what my… I have to move from Mindful Software repos into the OpenTelemetry repos, and my plan is to move piece by piece, SDK last, API before that, and then semantic conventions first, and they'd be their own Dart package. Is it the same for… I think Android, it's published separately, and is it true for the browser, too? Do you publish the semantics separately?
**Hanson Ho** 20:22 So, on Android, we have a registry defined with the repo. It is not, the OTAP484815 federated, you know, semantic convention shape.
It serves only as a place for us to basically define things in YAML and generate the Kotlin files.
That we use internally for it. The registry itself is not versioned, so there's no, there's no, you know, pinned version that says version 0.1 contains these attributes.
the version you get is 0.10, and it's whatever main points to. So, we don't consider the Android one to be a federated repo of any sort. And the artifacts that we publish, are pulling in artifacts, or registries from core, and also local, to generate the, Kotlin files for us to, to, you know, create logs and things like that with. So, in the regis… in the federated… in the semantic convention sense, Android doesn't have a public registry. It just has artifacts that contains, you know, Kotlin files of the core registry, and some, you know.
undefined ones.
in the future, when we have to settle this, I think, you know, this week, we want to basically, be a consumer of what's upstream here, and also the core.
So we will more or less be like that, except we're not gonna have this definition. Or if the definition that we have It, again, it's not going to be, you know, published outside of our project.
So… If what you have in the Dart repo is a registry definition, then we should talk about, how to migrate this, similar to what the browser folks have proposed. But if you're just talking about having Dart files, that are pulling in app.whatever, or the existing semantic conventions from the core repo, then you are free to do with that however you wish, inversion that however you wish. They become artifacts that are, I think, tied to that repo, and not necessarily a registry, that is published out. Unless it is, you know, a V2, Weaver's OTEP4815.
compliant, format.
**Ted Young (Raintank, Inc. – Grafana Labs)** 23:09 So… Yeah, I would suggest, Michael, like, giving it a shot to see if you can migrate your semantic conventions here.
And then, you know, use the… the semantic convention tool chain.
DART packages.
Oh, you're robotting. We've kind of lost…
**Hanson Ho** 23:32 If… Couldn't hear you.
Yeah.
Image is frozen, so…
**Ted Young (Raintank, Inc. – Grafana Labs)** 23:47 Yeah.
**Hanson Ho** 23:48 See if we can come back.
Sorry, we…
**Michael Bushe (Mindful Software, LLC)** 23:56 We…
**Hanson Ho** 24:00 We still couldn't hear you.
**Michael Bushe (Mindful Software, LLC)** 24:02 Can you hear me?
No.
**Hanson Ho** 24:08 Try… try closing your video, maybe just go audio only?
**Michael Bushe (Mindful Software, LLC)** 24:15 Let me try one more time.
Sure, not sure what I…
**Hanson Ho** 24:22 Oh, almost. Now you're mute.
**Michael Bushe (Mindful Software, LLC)** 24:26 I'll type.
Yeah.
**Hanson Ho** 24:30 The Wi-Fi in France.
Still couldn't.
**Michael Bushe (Mindful Software, LLC)** 24:42 Can you hear me now? No, you can hear me.
**Ted Young (Raintank, Inc. – Grafana Labs)** 24:45 Twitter.
**Hanson Ho** 24:46 Yes, that's better.
Oh, now… now he's gone. That's worse.
**Ted Young (Raintank, Inc. – Grafana Labs)** 24:52 Yes.
Okay.
**Hanson Ho** 24:58 So… Until before Michael comes back, we can talk about how to move that stuff. Another one is probably something that's probably easy to decide. Well, maybe. I never say that. How should we organize it? So, You could put… You could organize the directory any way you want.
But I think having an established convention is probably good, just for discoverability. And I don't mind the verbosity, of a directory structure, followed by an events or, like, a thing structure, but I also… I also am not, My tastes are different, so at least those here can have their input, like, how they want stuff to be organized. Directory slash concept YAML?
Just, or sorry, namespace slash concept. So I have a directory as the namespace, and then have concept as the YAML name.
have just everything stuffed into the namespace.yaml, everything stuffed in the concept.yaml, or something.
**Michael Bushe (Mindful Software, LLC)** 26:09 or something else.
**Hanson Ho** 26:11 Whoa, there's two Michaels now.
**Ted Young (Raintank, Inc. – Grafana Labs)** 26:13 We've got multiple Michaels.
Too many microph.
**Michael Bushe (Mindful Software, LLC)** 26:16 We only have one, only have one.
**Hanson Ho** 26:23 Oh, I think that goes. Yes.
Yes, yes, I think we can hear you.
**Michael Bushe (Mindful Software, LLC)** 26:27 I got a drawing from my browser, that was my problem.
very busy.
So, right, the dark convention is… are, generated by Weaver, just from the… some… the common, semantic conventions.
**Ted Young (Raintank, Inc. – Grafana Labs)** 26:43 That would be the suggestion, would be, if you're having to, like, reset everything up by moving it into OpenTelemetry and all of that, give it a shot to see about, like, putting the semantic conventions in this repo.
And using… like, see how well easy it is to adopt the existing toolchain that the semantic convention SIG is proposing we use for all of this stuff, as far as, like… having the conventions live in one repo, and using Weaver and things like that to generate the Dart packages.
**Michael Bushe (Mindful Software, LLC)** 27:16 I do that now with the main one, but you're suggesting I do it with the client one. Is that what you're saying?
**Ted Young (Raintank, Inc. – Grafana Labs)** 27:24 Exactly, exactly.
**Michael Bushe (Mindful Software, LLC)** 27:25 I'll be glad to take that… take that on. I have to… I have to anyway, and I've got a… I want to split… right now, it's part of the API, and I want to split it out anyway.
**Hanson Ho** 27:33 Actually, with the federated stuff, you can pull in one or many. So, you know, whatever you have, if you're looking at the… if you're using the V2 format, basically just pull in another, schema, and it'll pull in the right filtered, attributes you care about, or however you define your thing, and then you generate. So, it should be… it shouldn't be a migration, it should be, like, an addition.
So, when the browser stuff, or when the app stuff gets added into here, add a URL, And in theory, it should all… it should all work.
**Michael Bushe (Mindful Software, LLC)** 28:04 Cool.
**Hanson Ho** 28:07 Yeah, I found… I found… I had a really good experience with the tooling, as soon as I started running stuff locally, rather than having to… to do stuff on the images, because I had to do some workarounds to get Podman to work.
But anyway, that's… we don't have to do that, this is all local.
Cool. So yeah, back to the, the, the bike shedding.
How do we want to organize this? Anybody have strong preferences?
**Ted Young (Raintank, Inc. – Grafana Labs)** 28:40 Does this main semantic convention, SIG, have strong preferences?
Do they have regrets?
**Hanson Ho** 28:46 I don't know. I can… so, again, it's something I can, I can raise. I know, I think the other, the other semantics Convention Federated repos are doing directory, or the domain slash, kind of… events and then, you know, entities or whatever, just so that you can see, just by looking at the repo tree, what is defined in there. So that is nice. That's… partly why I like the verbosities, because it just shows what's there, so… Martin?
**Martin Kuba** 29:22 Yeah, and I was gonna say, I think if everyone else is doing it a certain way, I think we should be consistent.
**Hanson Ho** 29:28 I will find out how they're doing it, how everybody else… or how… if there's a recommendation, and then also, how others are organized by convention. I suspect, yeah.
And I'll report once we decide that, and we can just make a call on Slack, maybe. Again, we could always, like, do it one way, we can always change it, that's… I played some… yeah. The file names don't matter, so that's good.
Cool! And probably this is… we're at time right now, so we can talk about it a little further, is how we approve, new, conventions. So, just to preview, the main one has a lot of, infrastructure and rules about how to propose, and you put the thing, and the thing, the thing, and… I feel like we probably don't need all that, but we also do need more than someone says, looks good to me, boom, get it in. So at least having things reviewed here, with the three of us, maintainers, I think that's a minimum. that… or not, maybe not here, but maybe somewhere else. Like, I don't want to, you know.
make approval goes, like, every once a week and things like that. But, let's figure out this… formalize it next week, but if we have browser stuff that's ready to go, and it's already been approved, or, you know, three of us are okay with it, and others are given a chance to take a look, getting that sooner rather than later is my preference. Without, like, just, you know, ramming it through just the three of us. So… But we'll discuss that further next week.
Alright!
Thanks, folks!
**Martin Kuba** 31:12 Thanks, Hanson.
Good work.
**Hanson Ho** 31:15 Bye.
**Michael Bushe (Mindful Software, LLC)** 31:15 Makes sense.
**Ted Young (Raintank, Inc. – Grafana Labs)** 31:15 Thank you. Bye.
