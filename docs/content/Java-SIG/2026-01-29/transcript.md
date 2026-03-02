SIG: Java SIG
Date: 2026-01-29
Duration: 65 minutes
============================================================

## Zoom Recording Transcript

Robert Niedziela 00:00:53 Whoa.
Gregor Zeitlinger 00:01:11 Hello?
Trask Stalnaker 00:01:12 Hey, everyone!
Peter Findeisen 00:01:14 Hello?
Trask Stalnaker 00:01:57 Nooooo!
Jason, what are you doing?
Jason Plumb 00:02:07 I'm fixing it!
Trask Stalnaker 00:02:16 Alright, let's jump in. Jack.
Jack Berg 00:02:22 Yeah, I suppose that was the first topic. Senders.
And, and major version compatibility.
So, what's going on here?
It's hard to know for sure, but there's a user that seems to be a maintainer or some sort of contributor to the Google
Cloud SDK? Is that the… is that the name of the repository?
Trask Stalnaker 00:02:56 storage, I think.
Jack Berg 00:02:58 Cloud Storage SDK, and, you know, this is a project which depends on the OpenTelemetry API, and they also have, I think, an exporter bundled with the project as well, and so it depends on the SDK as well. And,
through their dependency management, they… they have sort of a version conflict for OKHTTP. Somehow, our BOM and their dependencies
ends up, you know, our OTLP exporter has the default OKHTTP sender, and the default OK HTTP sender depends on OKHTTP version 5.
And this conflicts with a version of OKHTTP they depend on, which is version 4, and something about their build tooling is making it hard to, you know, instruct
it to resolve to their 4.X version of OKHTTP.
And I guess, like, additional context is that, we have tested our OKHTTP sender with both major versions 4.x and 5.x.
And so, like, you know, the position that I've taken in similar issues to this has been, hey, it doesn't matter which version of OKHTTP you need to use.
We have, you know, testing that validates we work with both, and so, you know, for that reason, it's okay for us to have a single
OKHTTP sender implementation that targets multiple major OKHTTP versions.
But, you know, this person's running into some friction, and .
Trask Stalnaker 00:04:48 point out, Jack, it looks like we have Blake on the call today.
Jack Berg 00:04:53 Blake, what's going on?
Blake Li 00:04:56 Hey, everyone.
Trask Stalnaker 00:04:56 Thanks for joining.
Blake Li 00:04:58 Yeah, thanks for having me here. Yeah, I got the invitation from Josh, actually.
And yeah, just want to give a little bit more background, if I'm not interrupting.
Jack Berg 00:05:08 Please, yeah, that would be fantastic, because I'm just fumbling around, and I don't fully understand, you know, your side of the picture, but I understand parts of it, but not the full thing, so yeah, let's hear it.
Blake Li 00:05:20 Okay, so, yeah, so first, I'm from, Google, and our team manages the
Cloud Java SDK, and in this case, we have a large, enterprise customer, and they are using our latest SDK. And we just recently upgraded OpenTelemetry to 1.52.
And, however, they are still using 1.51 and OKHTTP4, in their repo. So when… after they upgraded their, our cloud SDK to our latest, they found their internal, maybe reinforcer plugin found this issue, and they reported back.
So now we are, actually, in the progress of, downgrading OpenTelemetry to 1.5D1.
not only us, but, in, gRPC, Java as well. So, after we downgrade… we're in the progress of downgrading, after we downgraded our, customer,
use our, downgraded version, then they should… they can proceed, with, you know, using the latest SDK. So that's the current situation.
And, yeah, I think the reason they are, they run into this memory force error is…
they… they still… they're still using OKH2P4, and it's a, breaking change for them to upgrade to OKHP5, and they need some time to, upgrade. So they really want us to downgrade it, so to give them a little bit more time, to…
you know, migrate their own repo to OKHPI.
So yeah, that's actually the… maybe the…
High-level overview of the situation, where we are.
Yeah, any specific questions?
Jack Berg 00:07:09 I guess the… a question that I have that was related to your last message in this issue is, so, okay, I understand why Google Cloud Storage depends on the API, and it also why it depends on the SDK, because it has a, you know, a custom exporter.
Blake Li 00:07:27 How does…
Jack Berg 00:07:29 Where does the dependency on, the OKHTTP sender come into play? Because if you just need those two dependencies, then…
Yeah, actually, they don't.
Blake Li 00:07:40 So we… both us and the gRPC, we don't use the OKHP sender, dependency. However, the reason they're, relevant, because they are in the BOM, in the open telemetry BOM.
And our customer used… tried to use the BOM to manage all of their OpenTelemetry dependencies. So they are… they, import OpenTelemetry BOM, and they use both OpenTelemetry API, SDK, and this OKHP sender.
And, and then we…
the storage, storage, artifact includes, only includes open… I mean, even without, let's not talk about storage, maybe just some, like, a… there are some other client libraries that only depend on Open TeleMature API. Even if you only depend on Open TeleMature API,
Our version is 1.52.
So, their internal mail enforcer plugin will, try to check that, oh.
this version, this Google Cloud, client library actually includes 1.52 OpenTelemmetry API,
And we are… we are still using 1.51, and, that caused that upper bound,
Upper boundary arrow.
So… and then when they tried to upgrade to 1.52, they found, okay, 1.52 actually brings in OKH54. I mean, I'm sorry, OKH25, and we cannot upgrade to OKH55 at this point.
Jack Berg 00:09:09 So it's not, it's not the Google,
Google Cloud Storage that has this conflict with OKHTTP, it's sort of a, you know, an end-user application that is, you know, depends on Google Cloud Storage and, you know, also depends on OpenTelemetry.
And, I guess so… and they're struggling in their, in their build system to instruct it to, you know, not
upgrade to OK HTTP5, because, you know, so they have a dependency on Google Cloud Storage that is lifting their dependency on OpenTelemetry, API and SDK, and the sender, and, you know, to the point where this compatibility issue arises.
But, and so they can't just, like, tell their build system, I think it's Maven in this case, to, like, hey, I know that, based on the version of Google Cloud Storage.
the version of OpenTelemetry used in Google Cloud Storage, it would suggest that we need OKHTTP5, but, like, you know, we know better than you, build system. You should use OKHTTP4, and we know that it will be compatible.
Blake Li 00:10:25 So, it's possible. However, like, as I mentioned, in my comment, or maybe I was not clear enough, that sometimes their customer's internal system is complex.
say they have, like, 3,000 internal repos. And, so yeah, that is possible for them to maybe… to,
downgrade this, okay, like, or force downgrade this OK shit before.
With using OpenTelemetry 152. It's possible, yes.
However, it's a lot of work for, the customer, and they…
Prefer not to do that, if we can downgrade it, because it seems…
easy for us to, downgrade, the OpenTelemetry version from our site. It's…
it's a one-line change, and then we just release latest, and that's all. If they want to… if they have to make changes to their build file, or, like, migrate OKHP425, it's a large effort.
Jack Berg 00:11:27 Yeah.
Trask Stalnaker 00:11:28 alert?
I mean, I would like to kind of jump to the… options… Basically, to…
You know, talk about, kind of, concrete things.
Jack Berg 00:11:43 But can I just… can I just say one more thing, one more observation before we jump into the options? So, like.
Trask Stalnaker 00:11:48 Yeah.
Jack Berg 00:11:48 The sort of… the…
the desire that Blake has articulated so far is for, you know, us to kind of take the posture to depend on the minimal version of a dependency that works. So, like, you know, don't stay on the head of OKHTTP5, instead stay on the lowest version, OKHTTP4.
you know, acts that still meets our requirements, that, like, doesn't have any security vulnerabilities or anything like that.
And so, I guess, like, I'm just noticing a little bit of asymmetry, because Google Cloud Storage is trying to stay on the head of open telemetry, but they want OpenTelemetry to stay on the tail of OKHTTP.
And so, like, ideally, we would like both to be sort of symmetric with the postures we take on our dependencies, either, like, staying on the head, or the lowest version that works.
Trask Stalnaker 00:12:46 I think the difference there, though, is minor version bumps versus major version bumps.
They're staying on the head of… the 1X major version.
Jack Berg 00:13:01 So that… okay, so… Okay, so stay on the… so then the generalization would be, hey, we should stay on the lowest ma… the lowest major version that works for us, and the latest minor version of the lowest major version.
Trask Stalnaker 00:13:16 I think that's, yeah, that's what… Essentially the request, yeah.
Blake Li 00:13:21 Unless it's, required to use it later. For example, if you really need a new feature from OKShoot 5, yes.
That would be a good argument for upgrading.
Trask Stalnaker 00:13:33 Oh, you're on mute. We don't hear you.
John Watson 00:13:35 I have one more question.
Could this also be solved by Google Cloud?
Or whatever, storage library.
manual, like, forcing OKHTTP4 as its dependency.
Jack Berg 00:13:49 It doesn't have a transitive dependency on OKHTTP.
Trask Stalnaker 00:13:52 I understand, I understand, but could you.
John Watson 00:13:56 could this also be solved that way? Because this is a pretty unusual case, right? Like, most of these intermediate libraries don't have SDK dependencies.
So, this is a relatively unusual
case for a library to have an SDK dependency.
Blake Li 00:14:14 Yeah, but without SDK dependency, even with only OpenTelemetry API, it will produce the same error.
John Watson 00:14:21 No, I know, but I'm saying if you pull… if you force a dependency on OKCP4 in your library, that would then get pulled in by the customers?
build system and be a dependency that would get resolved, perhaps?
Blake Li 00:14:38 that… I think, maybe, by hybrid.
John Watson 00:14:43 I agree.
I don't know how you test it, but…
Blake Li 00:14:46 Yeah, but we don't use OK3,
In our client libraries, so we…
It would be weird if we, like, force a version that we don't use.
So, the… our covenant workaround is we are downgrading OpenTelemetry to 1.51, in our leverage. That should work for now. However, let's say,
In the future, at some point, we may want to use a new feature from Open Telemat Show 1. Let's say, 1.50… 1.60.
Then… We're coming to this problem again, that, okay, can we upgrade or not?
Jack Berg 00:15:26 Okay.
Let's get into these possible solutions.
they've been on screen for a while. We could read through them.
Or we can maybe just take a targeted approach to say which ones won't work and why.
Maybe just filter the… filter the group first.
Trask Stalnaker 00:15:49 Yeah, I can make… I can attempt to, walk us through them.
So, updating the docs, I think is… Like.
an amazing idea. At least then, for example, this customer, like, if we had clear steps there, this customer
Could find that, and even if they have to apply at lots of places, at least it's a clear…
explanation of how to update their Maven or Gradle file.
This one, I think that… let's… let's, come back. This is, I think, the… what,
Blake is really asking for, and but let's come back to this one, because I think it's maybe the trickiest.
This one seems… I think we… there was kind of general agreement that
They're kind of no harm.
In doing this, other than an extra, you know, artifact.
Jack Berg 00:17:00 The customer in this case, the end user, still has to, you know, update in a lot of places.
to indicate that the default sender should not be the OKHTTP5 variant, it should be the OKHTTP4 variant. So, to me, this is like…
it's not that different from option one, because they still have to go touch a lot of places. But, like, I think this is sort of… I think having to go touch a bunch of places is sort of… I think a consequence of using a library that hasn't had an update in 3 years.
Trask Stalnaker 00:17:34 So do you… do you think this would… if we did this, would it make the instructions any simpler? I guess was kind of what I was…
imagining, but I did…
Jack Berg 00:17:47 Yeah, like, what's easier to, like, I think it depends on your build system and the plugins and the configuration you've had for it, but, like, you know, is it easy to exclude one dependency and include another one than it is to force the resolution version to be a particular thing?
I don't know, it's probably not, like…
It's probably a subjective argument, but maybe a little easier.
Trask Stalnaker 00:18:17 Okay, this one, yeah, is essentially back to this. It's kind of what our default… the question is what our default is.
I… does anybody…
want to do shade it? I wish, man, I wish.
Jack Berg 00:18:38 Joshareth did. I wish that…
Trask Stalnaker 00:18:41 There was, like, a simple… HTTP library that was, built on supported Java 8, but, worked.
Jack Berg 00:18:55 Right, yeah, the first thing I did with this is I went and checked the version of Google Cloud Storage, which… what was it using? Was it using Java 8 or Java 11? And it has compatibility with Java 8 as well. But I wonder if the end user's applications are Java 8 or Java 11.
Like, that's actually an interesting question. So if they're using Java 11+, we would advise them to use the JDK sender implementation instead of OKHTTP, and then, like, that's actually not that different from
Option 3, because they still, like, you know, even if we publish two different senders, they would still have to go and adjust all of their
you know, their build systems in a bunch of places to, you know, exclude one sender and use another. So what does it really matter if they're… if they have to do that anyways, if they're just including the JDK one?
Blake Li 00:19:50 So yeah, in this case, they are using, I think, at least Java 17. They're not using, 8 or 11. That's… I think that's not a… definitely not a bad suggestion. It could… We may still need option 2, but this, suggestion just made this…
I think maybe something we may want to recommend to the customer anyway.
If it's better than, the OKHP one.
Jack Berg 00:20:16 Yeah, what I like about Option 2 is, like, it gives us a sort of position that we can use now and going into the future, because, like, for now, we're compatible with both HTTP 4 and 5, but it's sort of, like.
it sort of feels like we got away with something. Like, it doesn't seem like in the next major version that we would be guaranteed to be able to support, with one sender implementation, version 4, 5, and 6. Like, it feels like we got lucky, and this is a more…
forward-looking policy that, you know, allows us to, you know, have a good strategy regardless of what OKHTTP does.
John Watson 00:20:55 I would… I would also like to suggest, just as a side path, we should freakin' deprecate the OKHTTP exporters.
Because Java 8 is no longer officially supported. Like, unless you pay money, let's deprecate those things, and then people who use them will at least see
That this is not the path forward that they should be using.
Jack Berg 00:21:17 That's so tough, John, because that means that, like, our default sender is deprecated.
Because if we say that we are Java 8 plus compliant at the SDK level, then, you know, we have to have a default, sender implementation for OTLP, which is Java 8 plus compliant.
John Watson 00:21:34 Yeah, but if… that's only if people aren't explicitly
using a sender that they… like, if they explicitly say, we're… I'm using the OKHCP sender, not they're just getting the default, then they should be flagged that this is one that we don't recommend if you have any option to use something else.
Jack Berg 00:21:54 What I would love to be able to do is detect if we're running on Java 11+, and if so, just use the JDK sender.
John Watson 00:22:01 Also a good move, yeah.
Jack Berg 00:22:04 I don't know how we would do that, off the top of my head. Maybe, maybe there's a way.
Trask Stalnaker 00:22:09 Let's, can we move that topic to the side? I think it's…
Coming back to… okay, so the main…
question that I have about this option is, how do we know… When…
a… the… like, okay, it should be for…
X goes out of support. Like, as you said, they haven't made a release on this for 3 years?
Lauri 00:22:45 Yeah. That's a hint, it probably already is out of support.
Jack Berg 00:22:49 But they have another page, Lori, that says that it is supported. So it's like they have contradictory evidence. They've never patched it, and they… but they also say it's supported.
Trask Stalnaker 00:23:03 But I don't love, like… I mean, like, dependency management tools will typically flag, like, if a dependency hasn't been updated in a year, saying that, hey, this may not be…
maintained anymore.
Right, like, that's… That is the obvious worry.
Jack Berg 00:23:27 I mean, we could specifically look at that page that says what their support status is, and we could also open an issue against that repo to get them to reaffirm that 4.x is supported.
Right? So then, like, our posture becomes, like, hey, while they indicate that they still support 4.x, we will have a 4.x sender artifact that targets 4.X, and as soon as that status changes, then we just stop publishing it.
Right? So, and, you know, and we simultaneously adopt a posture that says that, like, the default sender that we're selecting is the head. And so, like, you know, when 4.x becomes unsupported, and it will.
like, you know, we're not kind of stuck then. It's just like, you know, things just kind of keep moving along, because
the default sender was always… was already 5.x.
Trask Stalnaker 00:24:24 So, I wouldn't want to do that across, like, a lot of dependencies.
Jack Berg 00:24:28 But I think given that this is…
Trask Stalnaker 00:24:32 This repo… luckily, this is, like, the only.
Jack Berg 00:24:36 External dependency?
Trask Stalnaker 00:24:38 that, that we have.
I'm… I would be okay with, you know, doing something special like that.
Jack Berg 00:24:51 Man, if only John.
Lauri 00:24:52 I didn't…
Jack Berg 00:24:53 gotten the JDK client in.
Lauri 00:24:57 One thing I didn't understand is that,
For this to be an issue.
there needs to be the sender OK HTTP dependency somewhere. Who has that dependency? Does Google SDK have it, or does the user application have it?
Jack Berg 00:25:12 The user application.
Blake Li 00:25:14 Yeah, the user application has opened telemetry exported OTLP.
Trask Stalnaker 00:25:26 Do we have… is that in our BOM?
The OKHTTP.
Jack Berg 00:25:30 It doesn't show up in the bomb. I looked at that same thing. You have to kind of walk the bomb down to the palm of OTLP,
or OpenTelemetry Export, or OTLP, before you find that.
Lauri 00:25:42 Basically, Maven picks the latest dependency that you depend on.
Trask Stalnaker 00:25:47 But the problem would be…
Lauri 00:25:49 Users could easily solve it, by… by just saying, exclude the OKHTT dependency that they get through the OTLP exporter.
Jack Berg 00:26:00 That goes back to they have to touch a lot of things.
I don't think there's a way around that, by the way. Like, you know, short of us taking this sort of… having a default dependency on 4.x.
which I am really going to struggle to wrap my head around. I think I'm opposed to that, just because, like, even if they say it's supported, like, not having updates in 3 years, that's just… that's a really tough pill to swallow. So, like…
as the default dependency. So I'm okay accommodating it, but the default is a different story. So, and if it's not the default, then it seems like the end user is going to have to be updated a lot of places regardless. It's just a matter of making it a little bit easier for them.
Alright, so, it seems like two and one combined. Like, update the docs.
we can explicitly tell people… and the DACA update is going to be a few things, right? Because if we do number 2 as well, then, you know, what we're essentially saying is, like, hey, if you're using, you know, Java 11+, use the JDK sender.
If you're using Java 8+, and for some reason you can't use OKHTTP5, then use this new OKHTTP4 sender artifact.
Trask Stalnaker 00:27:34 Jack, you're saying 2 and 1, but I think you mean 3 and 1?
Jack Berg 00:27:39 Oh, yes, 3 and 1, I'm sorry.
Trask Stalnaker 00:27:42 Okay, okay.
Jack Berg 00:27:43 Yeah, I'm sorry.
Trask Stalnaker 00:27:58 Actually, from our point of view, three.
Blake Li 00:28:01 And it's not that much different, I think, as you also mentioned, because customers still have to touch their,
a lot of places in your internal bill system.
However, it may prevent, like, this kind of issue from happening again in the future.
Trask Stalnaker 00:28:22 Let's start with the docs.
And see, you know, what it…
looks like, actually, like, for both Maven and Gradle, how much… Trouble that is.
And then… Maybe in the future.
We can kind of discuss based on how horrible or not horrible that looks.
Because if it's not, Not bad, and there's not much difference.
then I'm not sure that… Oh, I guess the point of this is, like, it's a little bit more explicit, saying, yes, we actually… we officially support both major versions. Oh, and that's what you were saying, Jack. Sorry, I got lost earlier, because you were saying two also, but you were talking about,
The forward-looking posture of… HC… okay, CP6.
Jack Berg 00:29:28 Yeah, that's right. Like, 3 sets us up better for the future. Gotcha.
Yeah, I don't think that they're, like… I've said this a couple of times, but I just don't… if…
If we say that we cannot have the default dependency be on OKHTTP4 because they just haven't released a patch in 3 years, then I don't think that there is a solution that doesn't involve the user updating a lot of things.
I think that's, like, the impasse right there.
So, one of those two things has to give.
Lauri 00:30:09 For me, it's kind of surprising that the user would need to update multiple things.
It will mean that they have tons of projects that depend on the OKHTTP sender.
We're lucky.
Jack Berg 00:30:23 If they have, if they have…
Lauri 00:30:24 Or we have, like, only one, like, one sort of library project that sets up the Open Telemetry or something like that.
Blake Li 00:30:34 Yeah, they also use OKHTP directly in their applications.
Trask Stalnaker 00:30:41 So, let's, we're at half past, let's, call time here, and, Okay, it sounds like…
Like, this is a good…
Sounds like there's agreement on this.
John, Lori… Anyone… Oh, shit.
Yes.
Blake Li 00:31:07 I just want to maybe,
understand a bit more that what is the main concern of option 2? Is it a concern that, because it seems low risk at this moment, I guess the concern is that in the future, we…
don't know when to upgrade, when the OKH34 is out of support.
Jack Berg 00:31:26 The issue with option 2 is that they haven't pushed any patch releases to the 4.X.
branch tags in 3 years. And if you look at the changelog from, you know, of all the things that have included in 5.x.
there's… I think I saw, like, 60 to 90 different, like, changelog entries that are called fix. They have the prefix of fix. And so, like, even if they say 4.x is supported.
I mean, like, I don't… I don't trust that all of those fixes that have occurred since the last release are irrelevant to us.
So I actually don't think that staying on 4.X is, in fact, that safe of an option.
I think it exposes us to unknown unknown risks.
Trask Stalnaker 00:32:15 as a default, yeah, as our default for all users. Yeah, like, I think this is a good… your comment here, I found.
So the last release from… on the 4X series was…
Jack Berg 00:32:32 Two and a half years ago, sorry.
Trask Stalnaker 00:32:33 Two and a half years.
2 plus years ago.
But yeah, I mean, there's a lot of…
fixes on the 5X series, that…
John Watson 00:32:47 Does that mean that they're… does that mean their Kotlin dependency is also two and a half years out of date?
On 4?
Jack Berg 00:32:57 Yeah, but I don't know how the Kotlin dependency, like, maybe that transitive dependency can upgrade to the latest version safely without breaking that runtime.
But the default…
Trask Stalnaker 00:33:09 one that our users would get if they're not already using Kotlin.
Jack Berg 00:33:15 Fair.
Trask Stalnaker 00:33:17 That's a good… that's a… I think, also very… Good point.
Because we're talking about our default stance for what will all of our users be getting as their defaults.
Really should be… an up-to-date
version of the Kotlin library without them having to go and opt in to the latest.
Okay, well, let's move on. If there's… if you have any… if anyone has more thoughts, please feel free to leave them on this issue.
Mr.
Jack Berg 00:34:10 Coming, Blake, by the way.
Trask Stalnaker 00:34:11 Yeah, yeah, for sure.
Jack Berg 00:34:12 This is really helpful to… Have this synchronous back and forth.
Blake Li 00:34:18 Yeah, no problem.
Yeah, actually, I do have… if you don't mind, I have one quick follow-up question. So, regarding the BOM, what exactly is the, criteria for including one library in the BOM?
So this is more like a long-term strategy.
Like, is it possible to…
Maybe move this exposure out of the bomb?
Jack Berg 00:34:42 The BOM exists, you know, the… right now, just every component that we publish is in the BOM.
And, for reasons that we've discussed in previous calls, but you're definitely not caught up on, we have this sort of problem
which requires, or strongly suggests that our versions of OpenTelemetry libraries need to be aligned. Like, if you're using OpenTelemetry Exporter OTLP 1.52.0,
you should probably be using OpenTelemetry SDK 1.52.0 and, OpenTelemetry SDK Metrics 1.52.0, because
we use shared internal code, and there's an issue tracking that, I'm trying to get rid of it, but, like, it's got it here.
Trask Stalnaker 00:35:34 I got into that.
Jack Berg 00:35:35 long tail there. So yeah, for those reasons, it's important for, like, you know, your ver…
all of the components used of the OpenTelemetry Java project to be aligned, at least for now, and so that's the function of the BOM, is to enumerate all of the different projects to assist in aligning them.
Blake Li 00:35:58 Okay, yeah, sounds good. I think…
Yeah, I can put a follow-up, because I do think if… for anything that includes BOM, we may want to be a little bit more conservative in terms of dependency upgrade.
But yeah, we can follow up later.
Jack Berg 00:36:14 The OK, this sender really is sort of unique. Somebody mentioned this earlier. It's one of just a few places where we depend on an external library. By and large, we try to avoid external dependencies, which, you know, largely helps us avoid these types of issues, but this is sort of an exception.
Blake Li 00:36:34 Okay, yep.
Alright, thanks everyone.
Jack Berg 00:36:38 Thanks.
Trask Stalnaker 00:36:40 Pranav, you've got the next topic.
Pranav Sharma 00:36:45 Hey folks, hi. I had a quick question about this internal JUL.
mapping.
So it stems from this issue that was opened against one of our repos by a user, and they seem to think that when we use the auth extension, the GCP auth extension, with the OpenTelemetry Java agent, it leaks all the tokens, the secret tokens and the auth credentials. And initially, they thought that it was because of our exporters, but my…
investigation led me to this piece of code here, and the library… the logs are actually coming from Google HTTP Java client library, which makes the HTTP calls, and what's happening is that this library is logging all the request and response objects directly, but at a config level.
But the JUL bridge in the Java agent seems to promote that to info-level logs.
And that's why, by default, it just shows up in the log… in the logs. And I was wondering, two things. Like, main, I want to fix this issue, but before that, I wanted to ask, was there a special reason why we promoted the config
to the info level, like, looking at the documentation on the Oracle docs for JUL levels, I feel config should not have been,
Promoted to info.
I can… I can share the documentation link which I was referring.
Trask Stalnaker 00:38:18 Great.
Pranav Sharma 00:38:19 Yeah.
Where's the gym?
Yeah, just posted the link in the chat.
It's the bottom.
It's in the…
Trask Stalnaker 00:38:42 Hmm…
Pranav Sharma 00:38:43 Bro, it's at the bottom of the page.
There.
Trask Stalnaker 00:38:47 I see, so there's already an info… Config. Aha.
I have… I have no objection to changing this.
Laurie.
Any thoughts?
Lauri 00:39:04 No objections.
I guess it's just because there wasn't a straightforward mapping, so…
Whoever wrote it just chose info.
Trask Stalnaker 00:39:16 Probably me.
Yeah, send a PR printout.
Pranav Sharma 00:39:21 Okay.
Lauri 00:39:22 There is a… there is also, I think, another option is,
For some bloggers that are too chatty, we configured, like, the default level That is accepted.
So, if you wish, you could, like, basically exclude logging from certain classes.
Pranav Sharma 00:39:46 Yes, yeah, that was one of my thoughts, but if I understand correctly, that if I modify the login configuration in my library, which is GCP auth extension, at the application level, the user could still override it, right?
Lauri 00:40:04 This applies actually only to the agent.
Pranav Sharma 00:40:07 I see.
Trask Stalnaker 00:40:08 Yeah, I think we've got some, like, because we have some third-party, you know, we have some internal libraries we use that are too chatty and, like, emit warning messages that we don't want to, pass along, so somewhere, I don't remember where, there's some…
logic there. But in… in this case.
Sounds very justifiable to… makes sense to me to make this info.
Pranav Sharma 00:40:38 Okay, so basically, if logging level is greater than or equal to info, then map it to info. So info maps to info. Alright, sounds good.
Trask Stalnaker 00:40:46 Yep, here and here.
Pranav Sharma 00:40:48 Yep.
Trask Stalnaker 00:40:49 Cool. Alright, easy.
Pranav Sharma 00:40:51 Thank you, folks.
Trask Stalnaker 00:40:52 Yeah.
Serbi…
Surbhi Agarwal 00:40:58 Hello?
I had two questions regarding this PR. So, it adds network timing attributes as a standalone log record, to gather metrics in the backend regarding the durations of various network phases.
So we started with, OKHTTP3 library in the Java Instrumentation repo.
So my question is, like, here I add the event listener, where the event callbacks happen for the various network phases. That was introduced in OKHTTP 3.11, so I bumped the version to 3.11.
But, if we go a little below, I got the feedback that it would be better if I separated my test suite to just depend on 3.11.
And instead, the library could be compiled only 3.11, and the original tests could use 3.0.0, so we still support 3.0.0 for those users that don't need the metrics
Right?
But, let me share my screen quickly.
Trask Stalnaker 00:42:13 Yeah.
Surbhi Agarwal 00:42:25 Do you see my screen?
Trask Stalnaker 00:42:28 Yes.
Surbhi Agarwal 00:42:29 Awesome.
So, yeah, so basically, what is happening is, I am running into an issue right now. I tried that, like, I separated my test suite to use 3.11, and the library itself, is…
compile only 3.11, but the tests that were originally there, they are 3.0.0 right now. But I run into an issue here. So, basically, there are common classes that were changed. So there was this new
API that was introduced, right, that adds the new listener to the OKHTTP builder. So, this class is also loaded when the original tests happen, so it looks for the event listener, which it doesn't find, so I get an issue there. So, I was…
Wondering if…
it was possible to bump the minimum version here to maybe 4 or 5, or is there a way around to deal with this issue, right?
Trask Stalnaker 00:43:41 Sue, I was just looking up,
The release dates, so 3.11, was released
A long time ago, like, 7… Plus… Years ago?
So, on the… what I don't know, because I haven't looked at your
the PR is whether this would… we're… we have some flexibility on bumping…
A minimum version for library instrumentations?
But less flexibility on bumping them for a Java agent.
instrumentations.
Because Java Agent is very often, users use them on… throw it at very old applications where they can't touch the code.
So we need to maintain that version support.
But for library instrumentation, not so much, but… the…
And I don't remember if… it's likely, though, that our Java agent instrumentation is built on top of this library instrumentation, so that…
Could be.
another.
trick.
Lauri 00:45:01 I think the library tests are probably passing, and it's the agent tests that are failing.
Surbhi Agarwal 00:45:11 No, the library, this… the tests written in the library are failing.
I'm not able to go back now. Yeah, here.
Okay, if Java agent depends on this library, that we… then we can't bump.
Otherwise, it's possible to bump, right?
And, like, what would be the version that it should be bumped to? Would there be any suggestions there?
Trask Stalnaker 00:46:01 The minimum version that you need. So, in your case, it sounded like 3.11.
Surbhi Agarwal 00:46:07 Yaw.
Okay.
It looks like probably it's separate.
I'll take a look at that and upgrade the version to 3.11. That would be helpful. I had another question, where's my PR at?
So, basically, right now, I use system.nanotime, because I require… I don't require a point in time.
Specifically, but these timestamps would be used to calculate duration in the backend. So, NanoTime gives me nanotime level precision.
This could be replaced with, instead, using…
system.currentTimeMillis, or system. Or instant.now, right? That also gives me, time since the epoch time, and also millisecond level precision. So that gives me…
If I were to calculate duration out of those, that would give me millisecond level precision, as compared to nanosecond-level precision, but also that gives me additional data
which I probably don't need right now, like, knowing the actual instance in time when certain, when these callbacks happened, right? So, yeah, I wanted to, get the opinion of the group here about…
Like, there are different timing attributes, right, here for the different network callbacks that happen. So, is there any suggestion regarding what we should use as the timestamp to go in the attributes?
Jack Berg 00:48:06 What attributes are being populated with this? Is it an event, or…
Surbhi Agarwal 00:48:11 Yeah, it's sort of an event, like, when the DNS start, when the DNS ended, when the connection started, secure connection started, so…
In the backend, right now, the use case is to subtract these two and calculate the duration the TLS took, and the duration the connection took.
So nanosecond level precision could be obtained using system.nanotime, but it doesn't give you the time, absolute time, right, when the event happened, if that were needed. That's not needed right now, but is it better to use this
Or this, so we also get the instant in time, along with duration with millisecond level precision.
Lauri 00:49:01 Neither of these are suitable because they don't use monotonic time source.
Surbhi Agarwal 00:49:09 What would be a alternative that would work?
Jack Berg 00:49:18 It's our clock due again? I always have to re-remember this.
Trask Stalnaker 00:49:24 So, it's a… it's an interesting… I don't think we've, in semantic conventions, we've,
Modeled anything like this yet.
where sort of… and Jason, it sounds very much kind of like a browser-y, client-side event, where you, like, I'm thinking especially browser, where you want to capture
Here's… the page was… Viewed, and here's the different stages along it.
Jason Plumb 00:49:57 Yeah, it is definitely a client-side concern. There is also a semantic conventions PR that Serbia's opened that's related to this, and how to model this data.
Trask Stalnaker 00:50:09 That's good. That, Siri, I would suggest that we focus on the semantic convention.
PR and with that group of how to model this.
First…
Surbhi Agarwal 00:50:24 Okay.
We did discuss it in detail, and the idea was to have an example implementation to begin with.
So we started with the Java Instrumentation repo HTTP3 library.
Oh… Okay, but, like, is there anywhere we are leaning towards? Like… would,
So, if we were to find a monotonic source similar to how the span and lock timestamps are, span and lock timestamps also, by the way, use this, right?
So I think this should work.
Lauri 00:51:10 Pun and log timestamps, I don't think they use that.
Surbhi Agarwal 00:51:15 But they do…
Lauri 00:51:15 DK has an internal clock implementation.
That provides nano… nanosecond precision.
And, does it in a monotonic way. Like, system nanotime is a monotonic time source.
Basically, what it does is it, it captures, like, one timestamp, At the start.
And then, also captures the system. None of time.
And on subsequent calls, it just captures the normal time and adds the time to the initial timestamp.
Surbhi Agarwal 00:51:53 Right, but why do I saying it's not monotonic? It should be still monotonic.
Lauri 00:51:59 Well, because it just uses the system time, you could update your system time at the… between capturing two timestamps.
Peter Findeisen 00:52:07 Oh, okay.
Trask Stalnaker 00:52:09 And leap effectiveness.
Peter Findeisen 00:52:12 Yeah.
Surbhi Agarwal 00:52:14 Okay… but two epoch millis, does this guarantee that it's a monotonic source?
Like, if we cover to consider this…
Trask Stalnaker 00:52:24 Servi, I think we're getting too… into too much detail here. I think what I would want to see is a semantic convention proposal. What attributes, what data should be represented in those attributes?
And then we can come back and we can…
help you, like, how to implement that in Java.
Jack Berg 00:52:48 Probably where this might go is that, like, because I don't… I don't remember any prior art of recording timestamps, epoch timestamps, as attributes, and I think where the semantic conventions will ultimately lead is, like.
Probably don't do this because of these clock issues.
Trask Stalnaker 00:53:04 I mean, I could see semantic conventions saying, you know, capture the event start time, and then you could have.
Jack Berg 00:53:13 A duration.
Trask Stalnaker 00:53:14 Delta, deltas… After that, for different attributes.
But that's what I'm looking for from semantic conventions.
Before I think we would really want to move forward with this PR.
Surbhi Agarwal 00:53:30 Okay.
Lauri 00:53:31 Since it's currently just a prototype, then using the nanotime would be fine, or, like…
Or maybe even, like, capture the amount of time at the start, and in subsequent calls, subtract the start time.
To get, like, meaningful numbers.
Olik.
that it would be easier for you to read the numbers, I guess.
Surbhi Agarwal 00:53:55 Okay, use maybe the call start nano time.
And subtract the others to store delta, and then subtract each of them to get the durations.
Okay, I'll take a look at that.
And what, Trask also suggested, right, I'll try to bring it up in the semantic convention repo and see what they agree with, and then I can see how it can be implemented in the Java instrumentation and bring it up again if needed. Thank you so much.
Jack Berg 00:54:29 Yeah, so you asked… they asked you, I think, to provide, like, a prototype when you brought this up in SumConf, and so this counts as a prototype, right? So a PR doesn't have to be merged to move… to, like, meet that requirement and to move that conversation forward, so…
Surbhi Agarwal 00:54:46 That makes sense.
Trask Stalnaker 00:54:48 Yeah, sorry, I didn't want you to… yeah, didn't mean that you're stuck in a feedback loop here.
Jason Plumb 00:54:55 And a lot of times, people will leave them as draft, just as an indicator as well.
Surbhi Agarwal 00:55:01 Okay.
Jason Plumb 00:55:03 It's not that important, I'm just calling that out.
Surbhi Agarwal 00:55:06 Yeah, okay. Then let me, circle back and see, what they approve, yeah.
I'll stop sharing. Thank you so much.
Trask Stalnaker 00:55:25 Cool, we're at, more or less, our time box,
Wanted to just call out, that starting to,
think a lot about, the 3.0 release. I'm hoping…
that we can… I'm hoping to be, like, sometime in the first half of this year.
I think there's a bunch of… big…
Breaking things that we want to bring in there.
Semantic conventions, there's a couple more here. Service…
Peer.service was renamed to Service… dot peer.name…
There's also, I'm hoping we'll get clarity on, And, except log.
based exceptions… Instead of span event.
Since the direction is to deprecate span events,
And so that would be, obviously, a significant breaking change, so I'm kind of pushing on,
Trying to get clarity on that so that we could potentially include that in our 3.0
Not gonna happen, sorry.
Jack Berg 00:57:18 Jason?
Jason Plumb 00:57:20 You don't know me.
Yeah, we're gonna be stuck with it forever.
And ever.
Trask Stalnaker 00:57:35 So, yeah, yeah, just start the… just start thinking, trying to wind down,
the… the database stuff is getting there. There's not too much left, thank you. For all the reviews.
This one's pretty straightforward. This one, yeah, need clarity. This one, Gregor's taking on. Thank you, Gregor.
This one's getting there.
John Watson 00:58:12 So the… I think… you know, I know… I know Jason was trolling a little bit, but…
Jason Plumb 00:58:19 Only a little bit.
John Watson 00:58:20 If we're… I mean, if we're… if someone's still on Java 8, are they really going to be updating their agent to 3? Like, I just wonder whether that's… like, is that really something… if they're so stuck in the mud that they're still on Java 8, are they really aggressively updating their… their Java agent library to new versions? Like, I'm guessing they're still probably on 1.
Gregor Zeitlinger 00:58:40 So, if a customer is asking me, like, there is something not working, context is not propagated, or however they describe it, then I'm asking them, are you using the latest Java version?
I'm an agent, sorry.
Jason Plumb 00:58:55 Yep, every time.
Gregor Zeitlinger 00:58:57 That's why, it is a very realistic scenario, but I've never asked anyone to update Java 8.
Jason Plumb 00:59:08 Yeah, to Trask's earlier point, I mean, the people that are stuck on Job 8 are often the same people that need help with observability.
Like, they're like, I'm stuck on this old app that I can't change or even rebuild, I need to know what's happening with it.
But yeah, I'm just also reminded, like, Java JUnit 6 took the plunge to Java 17. Like, they don't even support 11 anymore.
John Watson 00:59:33 Same with Spring.
Jason Plumb 00:59:34 Yeah, I mean, it's… there's a trend.
Yeah.
Jack Berg 00:59:38 I feel at some point we might have to consider, you know, having the test modules use Java 17 source.
John Watson 00:59:47 Let me tell you, I don't want to upgrade the API and SDK to 2, but if it meant we could drop Java 8, drop Java 8, I would do it in a freaking heartbeat.
Bruno Baptista 00:59:58 So, just for fun, at some point last month, there was a PR that set JPA on the Jakarti spec to drop Java 17.
And they rolled it… rolled it back, after… after a while.
So, yeah, there's.
Jason Plumb 01:00:16 It'd be cool to get numbers from the cloud vendors to, like, know what people are actually using, if that's something we can get, just to see what the ecosystem is doing these days.
I haven't seen numbers in a while.
Jack Berg 01:00:27 We have this conversation roughly once every 6 months, and I feel like the arguments kind of, repeat themselves a bit, and I think, like, the question in my head is, like, what would it take? Like, what… hypothetically, if we wanted to do this, what would the signals need to be for us to consider it? And, yeah.
Trask time.
Stop.
Trask Stalnaker 01:00:52 Time on multiple fronts.
Alright folks, good to see you.
Jack Berg 01:00:59 See ya.
Jason Plumb 01:00:59 Thanks, everyone.
Pranav Sharma 01:01:01 Thank you.
