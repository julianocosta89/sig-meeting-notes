SIG: Kubernetes Operator SIG
Date: 2026-09-10
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Andy Keller** 00:34 I agree.
**Pavol Loffay (Red Hat LLC)** 00:35 Hello, Andy.
**Andy Keller** 00:41 Hi, Tyler.
**Mikołaj Świątek (Elasticsearch B.V.)** 01:26 Hello! Good morning, good afternoon.
**Pavol Loffay (Red Hat LLC)** 01:31 Hello, I'm Clay.
**Mikołaj Świątek (Elasticsearch B.V.)** 01:36 Wow, it's exciting! I think it's the first time I'm seeing you here, Andy.
I wonder… I wonder where… what the reason is for such a… for such an event.
**Andy Keller** 01:47 Yeah.
I've come a few times, but I ran into a specific issue that I should just open an issue, but I haven't gotten around to it, and I thought I would just ask a quick question, and then I can… Open the issue, and possibly even Submit effects, but, Just wanted to chat about it real quick. I'll add it to the agenda.
**Mikołaj Świątek (Elasticsearch B.V.)** 02:12 And I think we can,
**Jacob A** 02:15 Sorry, Injector SIG run over.
**Mikołaj Świątek (Elasticsearch B.V.)** 02:22 I think we can actually get started.
The first issue of the agenda is, I just wanted to… Decide, because we're… A week… more than a week behind releases, because we switched the network policy feature gates, and it turns out that those feature gates have Some amount of problems.
We're done.
I linked the issue in the doc, and the question is basically just this, and it's mostly a question, I think, to you, Pavol, because you have… the most contacts.
And this… What do we want to do? Because I kind of want to do the release, and my default would be to just say, flip these back to alpha.
Do the release.
And, and then work out.
All the kinks, and then…
**Pavol Loffay (Red Hat LLC)** 03:18 Yeah, so there was a patch or two merged recently, and there is one open PR to… Fix.
another issue for the network policies, which I don't think is related to the Helm chart issue that we had.
But it would be good if you could kind of preview it and get it in.
I would like to test it tomorrow morning, like, build the operator and kind of do artificial run of the end-to-end tests for the Helm chart with my build.
If it's easy to fix, go forward. If it's hard, then switch it back to alpha, so we can do the release.
**Mikołaj Świątek (Elasticsearch B.V.)** 04:04 Otherwise, if that goes in, is that enough?
Because there's, like, a list of 7 different problems in that issue.
**Pavol Loffay (Red Hat LLC)** 04:12 Yeah, it's not, I don't think that all of them are… necessary, like the… the DNS stuff, I don't think that, I think that's… yeah. Hallucination.
But we fixed that, I think.
Couple of these deaths.
Should be good. Maybe there is one more change on the end-to-end tests.
Because I think the end-to-end testing, the operator assumed the… the operator to be in a specific namespace, which is not the case in the Helm chart, but I'm not 100% sure. I'll run the end-to-end test tomorrow and see how it goes.
**Mikołaj Świątek (Elasticsearch B.V.)** 04:55 Maybe the solution to all this, and this is probably something Yupter should have done some time ago, is to actually just run In some capacity, at some level, the end-to-end test After installing using the Helm truck.
Because we might have this problem for the purpose of the end-to-end tests.
we use the customized manifest. The customized manifest has a preset namespace. You can change it, but we don't, right?
So… in general, like, there have been some similar problems in the past, where we would release something, and then it turns out that it broke the home chart in some not-so-obvious way.
So, maybe we should actually do that. I'm just not sure how to exactly, because I'm really not very keen on the idea of running all the end-to-end tests twice on every pull request.
Maybe they should just run on main every day, the same way we have the tests against Contrib.
which run… which run lightly and sometimes find stuff. It's not, like, a perfect mechanism, because they open an issue which nobody looks at.
later. But… it would be more detection that we have… than we have right now, and you could actually do something like where, when you have a release issue, then the issue automatically opened by the failed N21 tests against the Helm chart would link to that and count as a release blocker.
That, that I think this would be reasonable-ish.
a reasonable-ish compromise. What do you think?
**Pavol Loffay (Red Hat LLC)** 06:49 Yeah, I could maybe look at that as well.
Tomorrow.
**Mikołaj Świątek (Elasticsearch B.V.)** 06:53 That sounds like something… something an LLM could easily generate for you, to be honest. It's, like, very… Straightforward, and obvious if it works or not.
Okay, so in that case, we're waiting until tomorrow.
**Pavol Loffay (Red Hat LLC)** 07:13 Yeah, and… If it doesn't work, too much work, I won't be successful, I will open a pull request to switch it back to alpha.
**Mikołaj Świątek (Elasticsearch B.V.)** 07:27 I'm gonna make a note.
**Pavol Loffay (Red Hat LLC)** 07:38 Well, actually, do we need to switch it back to Alpha? Because we were able to release the Helm chart with the… Kind of… by overriding the config.
So we could continue for one more release.
Using that approach.
**Mikołaj Świątek (Elasticsearch B.V.)** 07:54 You tell me. I'm gonna be honest, I just got back from PTO yesterday. I don't really understand… I feel like I don't really understand where these issues are coming from exactly. Are they just coming from the fact that the Helm chart can be installed into a different namespace?
Or is there other stuff going on in there? Is it just Helm chart-related problems, or is it more generic, more general problems related to these network policies?
**Pavol Loffay (Red Hat LLC)** 08:24 The Helmuth Relators.
Mostly. And the, yeah, the different namespace.
Yeah, I think… so we have a workaround in the Helm chart that works. It just disables the… or overrides… it disables the… the Fisher gates.
For now, so we can continue with that approach.
**Mikołaj Świątek (Elasticsearch B.V.)** 09:02 Mmm… Okay.
**Pavol Loffay (Red Hat LLC)** 09:06 But I'll try anyway tomorrow to… I want to fix it, so it's, It works like it should work.
**Mikołaj Świątek (Elasticsearch B.V.)** 09:15 Okay.
Alright, so I am… I'm clear on that.
Tyler, you're next.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 09:26 Cool. This is the pull request that's adding… I guess the first of probably several PRs to… Implement… required images in the V1 Beta one.
Instrumentation object?
Just wondering, what's next for merging that PR?
**Jacob A** 09:54 I think it should be good to go. I wanted to wait to get, like, another person's review on it, if possible, given that it is… I think a more interesting change, the… Only concern that I have is more, like, good quality stuff, where the fields become, like, nillable.
Jay didn't love. I don't know if there's, like, a good way to get around that. That was the qualm that I raised in the PR. I don't know if there's, like, a way to get around that, though. It just almost seems… Antithetical… I understand why it's the case, but it seems antithetical to… The actual goal of the change, if that makes sense?
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 10:34 Yeah, so I think when we were discussing last SIG meeting, one option would have been to have some sort of enabled-disabled concept. But without that.
The nillable… milling out the type on the… On the upper level object.
**Jacob A** 10:53 Yeah.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 10:53 to say, like, it's not required, but if you do add it.
Then you have to have an image.
**Jacob A** 11:03 Yeah.
Well, could we make it so that if image… No, I see the problem.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 11:15 And this isn't released yet, so… If we do merge this, like, we have time to change it.
**Jacob A** 11:22 Yeah.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 11:23 Something that I want to start looking at is, like.
Well, I guess I don't know how close we are to, like, wanting to actually support, like, a mutating webhook for V1 Beta 1, or admission webhook. I don't know the name.
I don't know how long it is until we want to actually support someone installing V1 Beta 1, but before we would release that feature, we would have a lot of end-to-end tests, which, like, this PR doesn't add, because we haven't actually done anything with the with the V1 Beta 1 object yet, so…
**Jacob A** 11:55 Yeah.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 11:55 This can… we can always come back to it.
**Pavol Loffay (Red Hat LLC)** 11:59 Tyler, does this imply… That's… The image would be… required for V1 Alpha 1 as well?
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 12:10 No, so that was a takeaway from the last meeting, to investigate, like, if we switch the default storage to V1 Beta 1, what would happen to a user installing V1 Alpha 1 images? And based on my investigation, and I haven't actually run, like, a physical test to do this, although I can go make that happen if you'd like.
My understanding is, it is okay to have the storage be V1 Beta 1, as long as we continue to support a V1 Alpha 1 webhook. So the, like, what would happen would be The user submits the V1 Alpha 1 object.
the V1 Alpha 1's defaulting webhook would fire, and it would, like, fill in all those default images that the operator knows about today.
Then the object would be converted to a V1 Beta 1 with the conversion webhook.
I think it's the webhook. It would be converted to V1 Beta 1.
it would already have all the images, so that conversion would work, and then it would get… they would get saved, and then it could be read back out and converted back into V1 Beta 1, or V1 Alpha 1, and since it has images, nothing bad would happen.
So my understanding is, switching the storage is safe, as long as we keep the V1 Alpha 1 webhook. The second we remove the V1 Alpha 1 webhook.
which is, I think, is how we did it for the collector. We only supported the V1 Beta one. As soon as we removed the V1 Alpha 1 webhook.
then we would have a problem. That would be like a breaking change. Using B1-alpha-1 would kind of not be a thing anymore.
**Jacob A** 13:43 Yeah, because there would be no defaulting webhook to set those images.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 13:46 Yeah.
**Pavol Loffay (Red Hat LLC)** 13:47 And can we have a defaulting webhook for both versions?
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 13:52 Based on my research, we are allowed to have both versions.
for the… for the… for the webhook. Not for storage.
**Jacob A** 14:01 It'll…
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 14:02 But… but we can't.
**Jacob A** 14:03 But the whole point is that we don't default it, though, right?
**Pavol Loffay (Red Hat LLC)** 14:08 Maybe there's other fields that we default, I don't know. I don't think we…
**Jacob A** 14:12 Oh, oh, sorry, I misunderstood your question, Pavol. I apologize.
**Pavol Loffay (Red Hat LLC)** 14:15 Yeah, like, like, we might do some validation for… and defaulting for other fields.
**Jacob A** 14:25 I'd have to go into.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 14:26 again, I don't have it pulled up cleanly, like, quickly, but my understanding when I was looking through is, like, we define… this is… this is a URL, and this is a code, and, like, we could have multiple of those. We're not restricted to just one, was my understanding. So we can support the webhook for V1 Alpha 1 and V1 Beta 1 at the same time.
**Jacob A** 14:45 That tracks. We also should be using the, what is it, the cell, or the, like, code builder expressions for doing defaulting? Remember, like, that new… the new pattern that we… we have a few fields that we do this now. I, like, we should… Avoid doing stuff in the webhook when we can, because it would be great if we did not need to use the default in webhook for this pa… to, like, enable this behavior, because there are people that run the Operator with, default off.
Defaulting levels.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 15:11 Okay.
**Jacob A** 15:12 Soap.
I don't know, like, where we're at with that generally, but definitely we should be putting that in the, like, co-builder pattern rather than the, The defaulting webhooks, when possible.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 15:28 Okay, I have not looked into that yet, but as long as it's… like a Kubernetes pattern, I think.
**Jacob A** 15:35 It is, yeah. We already have it.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 15:36 In a few places.
**Jacob A** 15:37 Some… I think one of the, like, LFX fellows last year added it in to a couple of our.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 15:44 Okay.
**Jacob A** 15:45 So it's definitely there. We just have to know to look for it. Tyler, one more thing on your PR that I wanted to ask. I haven't looked at the code, like, recently. Do we already error from V1 Beta 1 if the, image is nil?
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 16:01 Yeah, so that's something that I… we would need to follow up with in another PR. Like, it'll… it'll error, but that error is… I'm pretty sure it's swallowed.
**Jacob A** 16:10 Okay.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 16:10 So, the thing… The thing that we need to do, and actually it's a problem today, and we discussed this on the last meeting, is that Today, in V1, Alpha 1. If you disable all the instrumentations.
like, you go into the flags, right, the command line flags, and you say, I don't want to support instrumentation, but for some reason, you've got, you know, the CRDs are in there, and someone makes an instrumentation object, And then someone throws an attrib… like, an annotation on their pod, like… Nothing will happen.
And it's really confusing, right? Like, there's no warning, there's no event, there's nothing.
Yup.
And so that's kind of a similar situation as what you can get into with V1 Beta 1, where, like, if you only define the Java image, and then someone throws on the Python annotation.
like… nothing will happen, right?
So, we want to… last time we were talking about surfacing that, because obviously the operator will know, right? The operator can.
**Jacob A** 17:12 Yo.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 17:12 Oh, you tried to specify.
**Jacob A** 17:13 We need to reject it, like, we can, reject with an error message. Like, there's a way to do that. We already do it for some things, so…
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 17:21 Cool. So we wanted to add that for V1 Beta 1. We talked about maybe even going back and adding something like that for V1 Alpha 1. It would be a good, like.
quality of life thing to add for V1 Alpha-1, although…
**Jacob A** 17:33 Yeah.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 17:33 prefer to just work on V1 beta one.
**Jacob A** 17:36 I think we should be confused.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 17:37 We also mentioned…
**Jacob A** 17:38 Yeah, we'd also…
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 17:39 I'll touch anyone else.
like, rising an event, although you gotta… we gotta kinda have to be a little careful, because, like.
If you deploy something with hundreds of pods.
that all are getting rejected, like, that could make a lot of events, so…
**Jacob A** 17:54 Yeah, you don't want to do it… you don't want to do it on the, On the pod's mutating webhook, you want to do it on the instrumentation's validating webhook.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 18:05 Yeah.
**Jacob A** 18:06 Because then that happens once per instrumentation, not once per injectable.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 18:10 Target.
**Jacob A** 18:11 But if we do that, I think that's fine. I just want to make sure that, like.
it is very visible that V1 Beta 1 requires this.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 18:19 Yes, so, like, if someone was making an instrumentation, and they defined Java, and they started setting up some environment variables or something in the Java spec.
but they didn't define an image, we should reject… that should be… that should fail validation when making the object. Yes. So that shouldn't even be allowed to get made, yes. My PR does not add that.
Because again, we haven't hooked anything… nothing's hooked up to anything yet. These are just, like, structs in Go. But yes, that is one of the requirements that we'll have to do in our validating code once we get to that… to that spot.
**Jacob A** 18:50 Cool. I'd want to be sure that, like, we have that known that this is the thing that we will need to do. Cool.
Oh, that sounds good to me. Pavols.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 18:58 Iron…
**Jacob A** 18:58 It is a shame.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 19:00 I'm curious, like, I don't know what the next step for V1… like, I don't know, kind of, really what V1 Beta 1 is at right now. Like, I'm adding these features, but it seems like we haven't even really hooked up the GO structs to anything meaningful in the Operator itself yet? Is that…
**Jacob A** 19:16 Yeah.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 19:17 Is there something blocking that work, or do we just need to, like, someone needs to go do it?
**Jacob A** 19:20 I think someone needs to go do it. I think it's been European summer, which means just things don't really get done. So, I think that we're coming back to it, and people are doing things. Once again, I'll just…
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 19:31 I'll follow up with Pavol, offline later and see what… where that works at.
**Jacob A** 19:36 He definitely is very interested in getting that done, so I think he's just been out, and Mikola's been out, and I've been out, so… Just how it is. Cool.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 19:45 And I owe back on the issue, I own that explanation for the V1 Beta 1 works in storage. I'll write up a comment about that.
**Jacob A** 19:54 Cool.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 19:54 I've got that tracked on the issue.
**Jacob A** 19:55 Yeah, it'd be good to confirm that as well, and Pavol wants some confirmation there.
Okay, I'm gonna go through feature gate stability real fast.
From version… 116. What's our current version? Anyone off the top of their heads?
we're at 158, which is fine. And we'll be at 159 soon, so I think we're all right for now.
We have two things that'll, be stable in 160, and we'll just need to get rid of those.
Cool. Andy, onto your bridge issue.
But it's definitely legit. I think that this was caused by… Some of the work that was done to enable the operator the bridge.
To work on raw, collector… Deployments and config maps, not just… The, accepts restart command.
And so… If you could give the issue report for how you installed There's a chance that what happened is that, I think that we added into the bundle that the bridge needs the elevated permissions, both here and in the Helm chart, but we might… we maybe missed that, so this might be a Helm problem. It also.
**Andy Keller** 21:17 We use our… we use our own, Sorry, we have our own role, so… Our role just didn't have that.
And so, it always worked fine without it, and then I went to bump the version to latest, and it wouldn't start.
And so my options were either add this permission to the role, or…
**Jacob A** 21:40 Let it crash.
**Andy Keller** 21:41 Or stay… or stay on 156, which is… a 156 right now.
I think that permission is, you know, gonna get some pushback from Customers?
**Jacob A** 21:53 Yeah, this was my, gripe with the change that was made.
is that this shouldn't be required, and so I don't think… that… I think that, like.
I thought that I had asked this guy to put this in so that we didn't need this.
Let me check one thing.
**Andy Keller** 22:13 I've got most of the issue written up, but I don't have the detail on… Kubernetes and Operator version, or collector version.
**Jacob A** 22:23 Yeah, I see it here.
**Andy Keller** 22:25 And they're required, so…
**Jacob A** 22:27 Yeah, no, I see this here. I think if you want to just open up a, what we should do is the pattern that the operator does, where if you're given the permission.
It will do it successfully, and if you're not given the permission, it will fail. It just won't… it won't, it won't have the capability added that it can accept, restarts.
I think that that's a reasonable change, and I think it's closer to user expectation. I'm definitely…
**Andy Keller** 22:54 So you're saying if you turn on the capability to restart, then… It should just… I mean, does it silently turn that off? Does it log a message?
**Jacob A** 23:07 I think what should happen is that if it has… When it does a… when it starts up and does a subject access review.
if it has the permissions to do restarts, then it will broadcast on the op-amp message that it can… that it accepts restart command, otherwise it won't broadcast that. I don't think that we need to have like, a two-flag thing. I think it should just be, if you give it permissions to do restarts, it should broadcast that it can do restarts.
But that also might actually be more difficult than I'm saying, and I think we should just not…
**Andy Keller** 23:47 I think it's okay to have it be explicit with the op-amp.
**Jacob A** 23:50 Okay.
**Andy Keller** 23:50 You know, fields.
Even though it is somewhat redundant, and then also… Has the potential of this conflict, where you say you accept it, but you can't do it, or you… Don't say you accept it, and you can do it, but if you say you… if you don't say you accept it, and It doesn't really matter if you can do it or not. I think you're explicitly saying I don't want people restarting my collectors.
Yum.
DR.
**Jacob A** 24:16 I think that's reasonable. If you want to just open the issue, this is a pretty easy fix. It's mostly just, like…
**Andy Keller** 24:21 figured as much, I just… like I said, haven't gotten to it, and I figured I would just come and chat about it, so…
**Jacob A** 24:26 No, you're fine.
**Andy Keller** 24:27 It's good to see you guys, anyway.
Yeah, you too.
**Jacob A** 24:31 Super reasonable fix. I'm not opposed to it. This guy was doing a bunch of work so that… the bridge could function on non-collectors, and I think that this was just part of it, where he wanted to be able to, do restarts off of the bridge. Because I think the way that we do this now with the… CRD route is very easy, where you just push a label change, and that will trigger the actual, like, operator to go do these things.
**Andy Keller** 24:58 Yeah, of course, yeah.
**Jacob A** 24:59 a much simpler process.
**Andy Keller** 25:01 Right.
**Jacob A** 25:03 But doing, like, the whole patching thing, this is one of the reasons that I didn't want to accept this in the first place, and I needed a lot of, convincing and strong-arming.
That this is, like, a thing that would be alright. Yeah, so if you open up an issue, I can tag this guy, he can do it, or, I can look into it.
I don't think it's long.
**Andy Keller** 25:26 I don't know what Operator version or collector version to state. Do you want to just put, like, X's in here, or…
**Jacob A** 25:32 Yeah, you can just put X's in there. If you just say the bridge version is 157, then that's.
**Andy Keller** 25:37 Yeah, I did.
**Jacob A** 25:38 Yeah, that's fine.
Given that this is just a bridge problem, not an operator problem, it's totally fine to just state that.
**Andy Keller** 25:47 Okay, I just created it, it should be at the top of the list, I'm happy to…
**Jacob A** 25:50 Great.
**Andy Keller** 25:51 a lot more as needed. I did leave a little bag, but… not vague, but, I think it's, like you said, it's very straightforward.
**Jacob A** 26:00 Yeah, I don't forward.
**Andy Keller** 26:02 on the law.
**Jacob A** 26:02 I'll get a fix up today. I just… this is annoying.
**Andy Keller** 26:10 Yeah, if we can get it into, 159, that'd be great to not be pegged to an old version.
**Jacob A** 26:16 Yeah, yeah, for sure.
Yeah, I'll… I'll send… I'll send my best people on it.
**Andy Keller** 26:26 Yeah, I mean, I imagine it'd be very easy for me, I just don't know the codebase at all.
**Jacob A** 26:31 None of them.
**Andy Keller** 26:31 Basically, Quad doing it for me, finding it and hashing it, and… I mean…
**Jacob A** 26:36 that's what will happen for me, but I think to the context of, like, I'm gonna just yell at it until it stops leaving the.
**Andy Keller** 26:43 You know what I mean.
**Jacob A** 26:43 There will be plenty. Yeah. Cool.
**Andy Keller** 26:48 Thanks.
**Jacob A** 26:49 Good to know, thank you. We have some Disgusted SIG, but without Pavol and… actually, we don't have any Disgusted SIG. Wow, that's the… that's a first.
Is there anything else from Mark, Ozzy, Tyler? Got anything else? Anything else in your mind?
Do you have a good Graf- Graf off site? Graf off site?
Offsite?
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 27:12 Called it Grafana Fest. Yeah, it was fun. Grafana Fest.
**Jacob A** 27:14 That's nice.
Very nice.
Ozzy, you're muted, by the way, if you said anything.
**Ozzy** 27:22 No, no, I don't have anything for Thursday, thank you.
**Jacob A** 27:24 Cool.
Nice. Mark, do you have anything you want to share with the group?
**Marc Schäfer (T&A SYSTEME)** 27:31 Nope.
**Jacob A** 27:32 Really appreciated, by the way, the issues that you've brought up, and the Helm repo. Those have been super valuable, and I've been going through those, bit by bit.
**Marc Schäfer (T&A SYSTEME)** 27:42 Take your time. Take your time.
**Jacob A** 27:44 Really, really appreciate that, that work, so thank you very much.
Cool. Well, if there's something else, Andy, I'm gonna get to this today.
I'll just have… again, I'll put my best people on it.
**Andy Keller** 28:00 Yeah, and it's not, super urgent for us, like, it's just…
**Jacob A** 28:05 It's annoying.
**Andy Keller** 28:06 Too late, okay.
**Jacob A** 28:07 Well, no, because this is definitely, like, a, It will break… if it's breaking you, it's breaking you.
**Andy Keller** 28:14 Feels like a regression, yeah.
**Jacob A** 28:16 Yeah, for sure. So, I think it's an easy fix.
**Andy Keller** 28:20 Yeah, thanks.
**Jacob A** 28:20 Cool, no problem.
Thanks, everyone.
Have a good day.
**Andy Keller** 28:25 Cheer.
