SIG: OpenTelemetry .Net Auto Instrumentation SIG
Date: 2026-09-30
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Zachary Montoya (Datadog, Inc)** 03:37 Hey, everyone.
**Igor Kiselev** 03:44 It's not Chris, but…
**Zachary Montoya (Datadog, Inc)** 03:51 Alright, I guess, you can get started. I'll just go ahead and share my screen. Just give me one second.
All right.
Just gonna open all this up.
Alright, I guess before we kind of dig into the regular agenda.
Are there any topics that you guys… Head, to make sure we spend time on.
Alright, cool.
**Eftiquar** 04:39 Nothing from my side.
**Zachary Montoya (Datadog, Inc)** 04:40 Okay.
Alright, so let's go through, It's quite a quite a few.
We have… a bunch of dependency bumps. Alexi added this to bring back additional debts.
So, let's review this.
Other than that, we just have existing ones that are… that are open.
I still need to look at this, the runtime async.
Are there any… Any blockers on this?
**Igor Kiselev** 05:26 Oh.
I will do a second review after the rebasing on it, but it looked pretty good even on previous room.
Previous review, it was mostly about statistics and not about the implementation, so… Very, very close.
**Zachary Montoya (Datadog, Inc)** 05:48 Okay.
**Eftiquar** 05:49 I'll take a look at it too, Gus.
The core engine was the core engine of how we treat the async results.
That was reviewed initially by me, so I will make sure that everything is there in place.
**Igor Kiselev** 06:05 There is also the change that in the draft from Alexey, I will look and show it today. He shares that he updated all that we, both me and Etikar, asked what he deemed necessary. I'm not sure why he has not removed it from draft, but as we are closer and closer to November, it's probably good if anybody else will Take a look also, just… Get first.
Gosh.
**Zachary Montoya (Datadog, Inc)** 06:38 Okay, what was it?
**Igor Kiselev** 06:39 Give me a second.
Ugh.
Oh, what a crisis.
**Zachary Montoya (Datadog, Inc)** 07:02 This one, the unsafe accessor?
**Igor Kiselev** 07:05 Yes, yes, yes, yes.
Enable unsafe type access, yep.
Okay.
**Zachary Montoya (Datadog, Inc)** 07:20 Okay, yeah. Yeah, looks like he pushed it relatively recently, so… Yeah, if it's ready for review, yeah, you can… Market as such.
**Igor Kiselev** 07:29 Even… even if it is not absolute, or even if it will have some changes, it's already pretty close to final.
**Zachary Montoya (Datadog, Inc)** 07:38 Okay.
Sounds good.
Alright, and then… other PRs… Include… Some span attributes…
**Eftiquar** 07:53 The IBM MQ MXNet. I have, provided my feedback, just, let me know if you guys agree, but there are some bits in that which are useful for OpenTelemetry in general.
**Zachary Montoya (Datadog, Inc)** 08:08 Okay.
**Chris Ventura (New Relic, Inc.)** 08:09 Yeah, I think the feedback there was real good to be able to break it up and deliver things in smaller pieces.
**Eftiquar** 08:18 Yeah.
You're great, you're welcome.
**Zachary Montoya (Datadog, Inc)** 08:27 Yeah, this definitely seems like it could be wrapping up then.
**Eftiquar** 08:35 And I've asked them to get the semantic conventions fixed first, so that when they add the IBM-specific things, it's already there in the semantic conventions, and… There's no confusion about it.
**Zachary Montoya (Datadog, Inc)** 08:48 Okay.
**Eftiquar** 08:49 Make sense?
**Zachary Montoya (Datadog, Inc)** 08:50 Yep, sounds good.
**Eftiquar** 08:53 Thank you.
**Zachary Montoya (Datadog, Inc)** 08:59 Alright, and then we have the Kafka ones.
I think there is… Yeah, there's two, sorry.
Okay, so, this one… Okay, this one we'll need to review. Okay.
Yeah, so there's a couple of open PRs. I haven't had much time to review.
So, I'll try to take a look this week.
Are there any other… Any PRs in particular that you guys wanted to discuss, or, contact.
**Eftiquar** 09:49 No, I think I only had that IBM MXNet.
**Zachary Montoya (Datadog, Inc)** 09:58 Alright, okay.
**Chris Ventura (New Relic, Inc.)** 10:00 I think there was a question about the startup hook-only solution with the Kubernetes operator.
This was for, one of Alexi's PRs.
And I don't know if that question was answered in the PR yet.
**Igor Kiselev** 10:24 I was…
**Zachary Montoya (Datadog, Inc)** 10:24 Access to one?
**Igor Kiselev** 10:26 No.
**Chris Ventura (New Relic, Inc.)** 10:28 Yeah, it wasn't… The additional depths fall back.
**Zachary Montoya (Datadog, Inc)** 10:32 Oh, I see, okay.
**Igor Kiselev** 10:35 So… I don't know in details how operator works. On my top-level understanding, for operator, we use some prepared image that operator will add and install and… So it means that we could either, fix it inside an image installation. Second question, the much more important, do we need to support no-profiler solution for Kubernetes operator at all? Because that fallback mode is required only for no-profiler solution.
**Chris Ventura (New Relic, Inc.)** 11:09 Yeah, and so that's where I think we need somebody to take a look at, how that image is made.
Because behind the scenes, it's likely just copying files and setting up.
**Igor Kiselev** 11:20 the.
**Chris Ventura (New Relic, Inc.)** 11:21 environment variables.
And.
**Igor Kiselev** 11:24 From what I understand… I remember from last talk with Piotr, he said that it is currently Splunk internal… Splunk images used by operators, so we… we… Prepare yourself. I may be not wrong, I may be wrong.
**Chris Ventura (New Relic, Inc.)** 11:39 I think there's a couple of varieties, so I'm sure Splunk has their own images.
Because, they have their own vendorized distro for supportability, but then there's also the.
OpenTelemetry provided operator, which I assume has some images available.
**Igor Kiselev** 12:02 Yeah, that's what you… I believe, and that's why I asked him where that images comes from. He said that currently it's hard-coded to use… so by default, use Splunk images.
**Chris Ventura (New Relic, Inc.)** 12:14 Oh, interesting. Okay.
**Igor Kiselev** 12:16 So, I may be… I may be wrong, I have not looked deeper into it, I will look into it, so…
**Zachary Montoya (Datadog, Inc)** 12:23 Yeah, there should be, there is an OpenTelemetry one. I would have to go back to find out where that is, but there is an OpenTelemetry one, and yeah, it basically just sets the main… environment variables, rooted spats, the profiler information, additional debts, shared store, and the startup hooks. So, it already sets a startup hook to this location, so theoretically, we don't even need the.
**Igor Kiselev** 12:50 professor.
**Zachary Montoya (Datadog, Inc)** 12:50 session.
**Igor Kiselev** 12:51 No, we use a screen right now, a new solution, to restore additional depths from our distribution, so it needs to run a SAS script or PowerShell script, whatever, so install script. But that install script probably could be run at the time when we build image.
**Chris Ventura (New Relic, Inc.)** 13:11 But I think it's only a concern if the operator provides a way to set things up to a startup hook only mode for auto instrumentation.
If the profiler is available.
then those additional depths and .NET store settings are not necessary.
**Igor Kiselev** 13:35 And we see that the environment variable to profiler are provided by Poperator, so…
**Zachary Montoya (Datadog, Inc)** 13:45 Yeah, if we… So we can populate… So, when you create an image, like, this is just setting the additional dots and the store, so… That does do, like, file copying, in terms of… I forgot… Yeah, I think basically it… the image just basically expects to have Like these directories and so it's all about how we prepare the image so, we can have it built such that, I can… I think there was…
**Chris Ventura (New Relic, Inc.)** 14:21 Well, yeah, so there's an init container that runs before a container is Created, which allows you to mount.
directory, as well as setting environment variables. And so, as long as the profiler environment variables are always set, and we're not operating in startup hook-only mode.
**Zachary Montoya (Datadog, Inc)** 14:45 and.
**Chris Ventura (New Relic, Inc.)** 14:45 So as long as there's no Kubernetes configuration that allows the operator to only set up startup poke-only mode.
then in the operator, we don't need the, additional dabs and .NET Store script to run.
So, I believe that's the context.
**Zachary Montoya (Datadog, Inc)** 15:03 Okay.
Yes.
**Chris Ventura (New Relic, Inc.)** 15:06 So, it… you gotta… we'll have to see what configuration options are available for the index container.
To see if any of them, Enable a startup hook-only mode.
**Zachary Montoya (Datadog, Inc)** 15:22 Gotcha, yeah, as far as I know, there's only the, like, Musil one, and that's about it, because, like, that one will… If you are.
**Chris Ventura (New Relic, Inc.)** 15:33 I'm assuming there's two, the Musul and, ARM64 or X64?
**Zachary Montoya (Datadog, Inc)** 15:42 Well…
**Chris Ventura (New Relic, Inc.)** 15:42 Is it the architecture or is it?
Right.
**Zachary Montoya (Datadog, Inc)** 15:46 So, like, it will pull the version based on the target arch.
I'm not sure why this one… This file only has 64.
for example, this this PR added support for ARM64, so maybe I just… I'm not looking for it correctly.
But, so the target arch is sort of one… one matrix, or one kind of… Yeah. In the matrix. And then the other one is whether to do Linux or Musil, and that one is configured via a pod annotation, but I don't think there's anything else. I don't think there's any other things you can control. So, like.
This one assumed Musil, and that's, I guess, up here because you had… the Linux Muscle.
So inject.net and then OTEL.net auto runtime setting it to a Musil version.
I think these are the only ones.
Let me just search.
Sonjata.
Really.
Oh, wait, why is this under… oh, this is someone else's branch. That's why, that's why I'm not getting it, okay.
Sorry about that.
So at least the docs say that here.
You just have these 3, essentially.
**Chris Ventura (New Relic, Inc.)** 17:31 Okay, so I think that gives us enough to answer the question.
That.
We do not currently support out of the box a startup hook-only mode.
When using the operator.
So we don't need to, Have the operator support the script to.
generate the additional depths and .NET store structure.
**Zachary Montoya (Datadog, Inc)** 18:02 Yeah, that makes sense to me.
Cool. But yeah, I just.
We pull down the artifacts based on the version, and then the, the architecture, and then copy it over, and then we… The operator sets the environment variables, including a startup hook, and then… Just, ingest that into the app container, and then… yeah, it runs.
Alright, cool. Are there any other questions on this one?
Right thing, though.
We should clear up at the moment.
**Igor Kiselev** 18:51 So, looks like, in that case.
current solution.
is good enough.
Repress it.
**Zachary Montoya (Datadog, Inc)** 19:06 Alright, so let's go to the issues.
This RabbitMQ one… We left a comment on here, Okay, and then in RabbitMQ, there's… okay, so they responded… And then this is bringing it into the latest one. Okay. Okay, that's good, there's some progress there. We can follow up on that as… as that develops.
And there's a couple more plugin the Op Amp.
And then… a GitHub CLI. Okay, so let's look at the opamp one.
Okay, this is about just improvements… Okay.
I guess… If Matush wants to work on this, it's… Fine, I don't think we need to mark this with anything for now.
GitHub CLI install script.
Oh yes, we require the GitHub CLI now because we run different like attestation checks.
Description, the switching leg, not rely on GitHub CLI.
A.
**Chris Ventura (New Relic, Inc.)** 20:37 So, because we're using GitHub attestations, I think the GitHub CLI is the primary way to validate those attestations these days. I'm not sure that there's another way.
At this point…
**Zachary Montoya (Datadog, Inc)** 20:54 Yeah, I… Don't know… A better way around this at the moment.
**Chris Ventura (New Relic, Inc.)** 21:04 I mean.
even if you use their… the GitHub Web API, you still have to deal with.
rate limiting for anonymous access, which is why the GitHub token is required anyways.
So, I'm not sure that there's any other workaround other than… to have an opt-out for doing the validation as part of the install script, which I thought we had an opt-out.
**Zachary Montoya (Datadog, Inc)** 21:40 Yeah, it is in there.
**Igor Kiselev** 21:41 I'd only open a discussion if we need, by default, opt-out from it, or opt-in into it. I don't know other… other tools, but… I've… I don't think that lots of our customers have GitHub, toolkits by default installed. So, for most of them, it will still be, skip verification mode by default.
If so, maybe we should make it opt-in.
Unless we will find a way to run it with a minimum.
Yeah, I think that…
**Chris Ventura (New Relic, Inc.)** 22:20 Makes sense.
**Igor Kiselev** 22:22 Another thing what we can do, we could give some additional arguments for customers to manually provide hash code, SSH to validate, or something like that, so that they could do a protection not using GitHub attestation, but if they checked it manually, so it's, like, offline mode or something like that.
So, I would say that the ask is pretty reasonable, from my point of view.
Bye.
**Eftiquar** 23:08 was supposed to be.
**Zachary Montoya (Datadog, Inc)** 23:11 Yeah, let me just document that.
Okay, I'll post that for now. But yeah, definitely, definitely a reasonable ask.
we can… We can also spread.
So.
Yeah, we'll have to think about that one more. Yeah, I'd be interested to see if other repos are… doing, like, a strong verification by default, or, like, what the sort of general stance is across the… other… Sdks.
Like, if this is generally done across SDKs, then… Maybe it's just a pain that our users have to live with.
I don't…
**Chris Ventura (New Relic, Inc.)** 24:33 I don't know that it's necessarily done across the SDKs. I think it's more for the auto instrumentation side of things. Because with the SDKs, you're typically interacting with the package managers more.
**Zachary Montoya (Datadog, Inc)** 24:46 or.
**Chris Ventura (New Relic, Inc.)** 24:46 And… Downloading and installing.
So, I would say, like, the Java Auto Instrumentation and, Might be the most similar.
**Zachary Montoya (Datadog, Inc)** 25:02 Yeah, that one, and… Would Node.js, like the JavaScript one, also be an equivalent? Because you're bringing in a source file, right?
**Chris Ventura (New Relic, Inc.)** 25:12 Node… I think 99% of people use NPM.
And Python, use one of the Python package managers.
Ruby is in a similar boat.
**Zachary Montoya (Datadog, Inc)** 25:25 Okay.
**Chris Ventura (New Relic, Inc.)** 25:27 I really think it's just… Java.
And maybe some of the other… of… Well, no, it might just be Java.
**Zachary Montoya (Datadog, Inc)** 25:41 Yeah.
**Chris Ventura (New Relic, Inc.)** 25:42 you.
**Zachary Montoya (Datadog, Inc)** 25:43 Okay.
Yeah, I suppose we can check to see what Java's doing, and be on the same page with them.
Let's see, were there any other issues?
Okay.
No, no, besides that, no, no issues.
The project board… looks pretty similar.
I don't think we need a… Adjust much, Yeah, I don't think there's really any updates we need at the moment.
Okay, well, that is our agenda.
Is there anything else you guys wanted to discuss?
**Igor Kiselev** 26:39 On the GitHub attestation, I'm really interested in how it works in theory, because what we are protecting, we are protecting, with GitHub attestation. If we downloaded something from GitHub.
we're protecting that customer get what we publish to GitHub, and what GitHub written. So we are mostly… and we already downloaded RushTap S. So we are mostly protecting that customers have their own keys, and still have them in the middle, or GitHub have been hacked and provide something different. But in both that case, will GitHub Association will give us any good things at all? Because if Well, we already have a vulnerability in… when in the middle, between us and GitHub, or GitHub is hacked, Wood Attestation, still says that everything is great. So, I'm not yet proved even that it… improves anything in existing pipeline, so I'd say that the only way to improve existing pipeline is to provide a customer a way to give it from offline trusted channel.
Or he will have it encoded in a script, SSH or something like that, so if a script have been provided from a trusted channel, it knows what to download.
I'm just not sure about GitHub attestation in that case, if it gives us anything at all.
**Chris Ventura (New Relic, Inc.)** 28:05 Yeah, I mean, at the same time, in theory, if your release process publishes checksums for all of your artifacts. Those checksums are most likely going to be generated from a GitHub pipeline.
Which, Could suffer some of the same problems that you described.
So, I'm not sure if… Anyways, that's not my specialty area.
So yeah, I have to defer to others there too.
**Igor Kiselev** 28:41 Let's continue discussion if we need it at all in the current shape.
**Zachary Montoya (Datadog, Inc)** 29:00 Alright, anything else?
**Eftiquar** 29:04 Oops, all good.
**Zachary Montoya (Datadog, Inc)** 29:06 Cool, I think we're all set. Alright, thanks everyone.
**Eftiquar** 29:09 Have a good one.
