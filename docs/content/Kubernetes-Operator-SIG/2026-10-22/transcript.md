SIG: Kubernetes Operator SIG
Date: 2026-10-22
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Kushagra Shukla** 02:31 Hey, Ervin, how you doing?
**Ervin Wallin** 02:34 Hello!
**Kushagra Shukla** 02:36 I have one question, like, I was thinking about speaking in KubeCon, so… what are the criteria? Like, should I be an, like, a maintainer of any open source project?
Or, like, what?
**Ervin Wallin** 02:51 Or can you repeat it? Because my…
**Kushagra Shukla** 02:56 Okay, okay, yeah.
**Ervin Wallin** 02:56 Very, it's very bad.
So…
**Kushagra Shukla** 02:59 Yeah, I'm saying, I wanted to speak, in KubeCon, so what are the criteria? Like, should I be an open source contributor to any project? Like, let's suppose an open telemetry Operator, or, like, what?
**Ervin Wallin** 03:14 I… I am active in, Helm chart projects.
**Kushagra Shukla** 03:21 Okay.
So, have you ever speak, like, in KubeCon?
**Ervin Wallin** 03:30 Whoa.
No, never.
**Kushagra Shukla** 03:33 Beautiful.
**Tyler Helmuth** 04:04 Hello, everyone.
**Ervin Wallin** 04:10 Hello.
**Tyler Helmuth** 04:25 Rook Kalsh said he wouldn't be able to make it today.
But hopefully… Pavol or Jacob will.
If they don't… We'll probably have to cancel, since we won't have any maintainers.
Hi, Pavol.
**Pavol Loffay (Red Hat LLC)** 05:37 Hello, hi everyone.
**Tyler Helmuth** 05:42 You may be our only maintainer today. It's Mikolaj said he couldn't… couldn't make it.
**Pavol Loffay (Red Hat LLC)** 05:48 Yeah, I thought he will join for a couple minutes.
In past weeks, I was… doing some internal stuff, so I don't have many updates.
On my end, but… It looks better now, and I should have time to focus on the instrumentation, and finish the network policies.
**Tyler Helmuth** 06:53 Cool.
Yeah, if you… when you start doing instrumentation stuff again, let me know. I kind of paused on the… Like, required image work, because… Like, the instrumentation work.
was paused, so… yeah, I can look at that again if we're… if we're doing it again.
**Pavol Loffay (Red Hat LLC)** 07:13 Awesome, I think I will start with, putting the declarative config into schema, I think that's the most important bit. We need to get there, and then… Slowly working on the… kind of the strategy, how we can enable it, and the webhook, and how we can enable the labels instead of the annotations.
Or probably have both for some time.
**Jacob** 07:48 Sorry, sorry I'm running late. I was coming from the injector group, where we were talking about injector entering Operator and, what's going on there. So… Exciting stuff.
I don't see any issues on the agenda, but I know we have a bunch of things in the discussant SIG, but before I get into that, is there anything that people want to bring up?
Tyler, I know that there's some Helm PRs that I need to review. This is my OTIL review day, and I started off with Balsy stuff, then I did injector stuff, now I'm doing Operator stuff and Helm stuff, so… it's on my list, but it…
**Tyler Helmuth** 08:24 Yeah, my wife.
**Jacob** 08:25 Awesome.
**Tyler Helmuth** 08:25 topic, which is related to what I need in the Helm charts, is, There's that cert bundle problem that happened this week, right, where we can't trust certain certs, and they were… we bundled them all up, because we use Go, but Go had a release.
there's, like, new CA bundles to AppGit and all that stuff. Collector released yesterday, I did the Collector release yesterday, so 163.2 has all the fixes. There's a Helm Chart PR that updates that.
Are we going to patch the operator? Are we going to do an operator release?
**Jacob** 09:01 I think we should do…
**Tyler Helmuth** 09:02 release.
**Jacob** 09:04 I think we do, and I think we should patch.
**Tyler Helmuth** 09:06 Okay.
**Jacob** 09:07 I will also say that that, we will not have this CERT problem anymore with that… with that particular CA.
They announced this… we won't have, a cert problem with that CA anymore, because they announced that they're getting out of the CA business.
**Tyler Helmuth** 09:21 Oh, really? Huh.
**Jacob** 09:23 Yeah.
**Tyler Helmuth** 09:25 Does that mean that, like… Does that mean that even the old compromised one doesn't matter anymore?
**Jacob** 09:31 I think it still matters.
**Tyler Helmuth** 09:32 check it with?
**Jacob** 09:33 But I think, like, we still… we should still do this, but they announced, like, earlier today that they're… Quote-unquote, getting out of the cert business.
So… But anyway, I think we should…
**Tyler Helmuth** 09:46 We added a lot to my plate this week.
**Jacob** 09:50 We should do a patch… well, are we due for, hold on.
**Tyler Helmuth** 09:57 If we're just due for a release, we could just do a.
**Jacob** 09:59 Then, I think we might be due for a release. It might be my turn, actually. GitHub issues is not working. That's great. That's super helpful.
I should say, I would say that we should move to GitLab, but GitLab also had a CD10 yesterday, so…
**Tyler Helmuth** 10:16 What was theirs?
**Jacob** 10:18 They had… someone discovered RCE on every version of GitLab since 2014.
**Tyler Helmuth** 10:26 Yikes.
**Jacob** 10:27 Yeah.
**Tyler Helmuth** 10:28 You are the next release manager, by the way, so if you want to do a 162, that…
**Jacob** 10:34 Or do…
**Tyler Helmuth** 10:35 versions in the build, and we should update our… I assume we have a Docker file that does an apt-get bundle. We do.
**Jacob** 10:41 Yep.
But yeah, I will, I will do it today.
I will update all our Go versions, and…
**Tyler Helmuth** 10:51 You need…
**Jacob** 10:52 Ghost.
**Tyler Helmuth** 10:53 I have time to do this today, because the person that I do work with at Grafana is on PTO and the stuff… I can't do a lot of stuff at Grafana today, because the person I need to review things is gone. So if you want me to do the… If you want me to do the Operator release, let me know.
**Jacob** 11:09 If you want to do the Go version and AppGets, I can do the release stuff.
**Tyler Helmuth** 11:14 Okay.
**Jacob** 11:15 supremely busy today. This is, like, I've… I'm basically in back-to-backs until, like, 5 o'clock my time.
Soap.
If you could do the… everything up to the release, I can do the release.
**Tyler Helmuth** 11:29 No problem.
**Jacob** 11:29 Get that through.
Thank you.
and then I'll review the Helm stuff as well, like, right after this, over lunch.
Okay, let's go to the Disgusted SIGs, because we have two of them.
Or 3 of them, I guess.
Allow… Holy Central Management.
So, sorry, let me share my screen.
Mikolai isn't here, which is a bummer, because he's on a bunch of these.
Let me just move this tab out.
There we go.
They're… Okay, can everyone see just this thing?
I'm gonna make it a little bit smaller, so that it's just not as large.
Okay, so this feature allowed the default collector image to be updated without restarting the operator.
It is interesting.
Is this person here, perchance?
No, don't think so.
What did Nicholas say?
**Tyler Helmuth** 12:52 How would that work?
**Jacob** 12:59 They're properly related energy.
Make sure to change the site, I think… This is basically asking if we could do, like, hot reloads of the Operator config.
**Tyler Helmuth** 13:17 Of the opera.
Oh, okay.
**Jacob** 13:20 Yeah, like, th-this is what this user wants.
Is so that they can set the… They can set the, Like, config flags or config file for… The operator, and then have a watcher on that file that then restarts it.
I'm not, like… I'm kind of in the same boat as Nikolai here, like, how much of this is a real problem? There are no good options. If I populate this, then using one or more controller tree to restart seems to be the only option when the config mark changes. The other option is to provide it and then restart. That doesn't answer the question.
I can't disagree, but if I keep, then what you're having.
**Tyler Helmuth** 14:06 With our move to… Instrumentation V1 Beta requiring… user-supplied.
images, or auto-instrumentation images.
We don't require that for the collector's Day.
The collector does technically have a ton of braking changes pretty frequently.
**Jacob** 14:27 I'm kind of surprised that somebody is doing this.
**Tyler Helmuth** 14:31 Yeah, I guess I'm wondering if in the future, if we're going to require the collector image to be set by the user, just like the other instrumentation images, in which case this becomes less… This feature would just go away.
**Jacob** 14:43 I think I understand why this user wants… uses this feature, right? Like, the idea that they have the operator managing the collector image, and then they only need to update the operator is beneficial, because it allows them to set the only collector image in one place, and then every collector will always use that image. I actually think that that's, like, a pretty solid use of the Operator, to be frank.
**Pavol Loffay (Red Hat LLC)** 15:05 I don't.
**Jacob** 15:05 Whereas…
**Pavol Loffay (Red Hat LLC)** 15:06 Honestly.
**Jacob** 15:08 I think what they're asking for, Pavol, is that they… they just don't like it that the operator has to restart when we change the conf… when they change the config for it. I don't think it makes sense to,
**Pavol Loffay (Red Hat LLC)** 15:19 But when I read a sentence, allowing the platform team to update the collector image without requiring every consuming team to update and redeploy its own resource.
**Jacob** 15:31 Yeah, so,
**Pavol Loffay (Red Hat LLC)** 15:32 He doesn't.
**Jacob** 15:33 boom.
**Pavol Loffay (Red Hat LLC)** 15:34 The issue is actually kind of restarting the operator.
**Jacob** 15:40 I think what they're saying is that right now what they do is all of the teams that they work with that, deploy their own collector CRDs?
Do not set the spec image.
And rely on the operator's, image.
Like, the one that the operator sets, right? And what they… want… It doesn't talk about the problem that they're actually, like, having with it, though.
Right. Is that what you're asking? Like, what is their actual issue with this?
**Pavol Loffay (Red Hat LLC)** 16:14 Exactly, because what they… like, the first sentence or paragraph is about the problem, right? And… It doesn't…
**Jacob** 16:22 It doesn't really say a problem.
Yeah.
**Pavol Loffay (Red Hat LLC)** 16:31 So, especially this allowing the platform team to update collector image without requiring every consuming team to update and redeploy. I understand the update, like, if… They want to have different images per team, they would need to manage it themselves.
But the… Image change will trigger update anyway, right?
**Jacob** 16:54 they're talking about updating and redeploying the CRD, not whatever underlying, like, replica set they have.
So… They want to avoid, every team that uses the collector CRD from needing to update their own collector CRD, and redeploying that collector CRD.
Not… like, they understand that we'll need to restart the collectors with the new image, that's fine, but what they don't want to do is mandate that, every team has to go in and now set their own image.
Which, I don't… I think that this just, to me, isn't a problem. I think that this is just, like.
they're mildly annoyed by needing to restart an operator, and that, I don't think, is reason enough for this feature to exist.
**Pavol Loffay (Red Hat LLC)** 17:45 Yeah, like, what is… what is the issue of restarting the operator? I don't understand.
**Jacob** 17:50 Yeah, we talked about this at the SIG meeting today, and it's still unclear to us the actual With restarting the operators… type of change… Could you provide a material use case or a problem with the operator?
Restarting.
necessitate… That's fine.
Look at this, this is Joe.
This is just sad.
Okay, enhancement. Unified manager configuration to a single source of truth.
This is for automatic delays in this, and this is the very first step.
I've opened up the Operator Library, but there isn't really… I'll try my own.
Okay.
So let's take a look at this Register flags are… Then we move… Yeah, yeah, you're, like, moving all this into the… Helpers here, we can get rid of all this.
Yeah, I mean, this doesn't seem too uncontroversial to me.
Certainly, I like the idea of, like.
Having the docs come from one place, and all of our config come from one place, because then we don't need to do all of this, which is great.
I like anything that deletes code, so this makes me happy.
Let's see, it was… Yeah, I think that's the only thing that's missing from this, is just some more test code.
It feels like, you know, we're adding in this fields thing, and there's no tests for it to verify that it does the thing that we expect.
And I think, I think that we should also have some tests To verify the sort of before functionality and after functionality is still, functionally equivalent.
Otherwise, I think this is great. I actually love to… would love to see this code go away.
I think that Antoine would feel the same, who wrote… who rewrote a lot of this recently.
So, I'm for it.
pavol, Tyler, either of you have any thoughts on this?
**Pavol Loffay (Red Hat LLC)** 20:39 I think I like it as well. I need to look in a bit more detail, but I think it's good.
**Jacob** 20:44 Yep, that is right.
We've talked about this during the SIG meeting, and are broadly In favor of the change, the only… Concern was around test coverage.
Clues, addison M for…
**Pavol Loffay (Red Hat LLC)** 21:04 And if there is, like, a check if he's not breaking anything, that…
**Jacob** 21:08 Yeah. Before and after.
Functionalities, to ensure… that everything… Yeah, I agree. I mean, I think it's just that it would be especially valuable to know that, like, all of the config flags are binding the way That we expect them to.
Also, be sure to add in a change load.
As well, please. Which is, for this type of thing, this is just, like, an internal thing, but I actually would like to see a changelog for this.
Even though it's, like, an operator-only thing, it's, like, a documents thing. I think it would be good to have a changelog for any Just for onlookers.
But yeah, it was great, so thank you very much.
**Mujib Ahasan** 22:00 Yeah, I mean, I intentionally avoided the test case for the first push, so I wanted to confirm the process first. I mean, I've been with the Kubernetes SIG CLI, so… I think I could have thought this in a more different way than realized it's not a… I mean, this CLI tool, yeah.
just…
**Jacob** 22:24 Forgive you.
**Mujib Ahasan** 22:24 on a single struct.
**Jacob** 22:26 The only other thing that I was thinking about that I'm aware of that does this is a language… is a library from Kelsey Hightower… go… n config, which I think does kind of a similar thing. This might just be for environment variables, though.
but… that… I know that this does something similar, so maybe just, like, check this out as well to see if there's anything interesting that's happening in there, just to be sure that, like.
the flags are working, or, like, Viper. We could use Viper, honestly.
**Mujib Ahasan** 22:59 Yes.
**Jacob** 23:02 this is quite good, actually. If we could move to be… to use Viper, I would also be very in favor of that, rather than needing to rewrite. I don't think it would be that difficult, too.
And we probably should… actually.
Can you look into using Viper to see if that solves our… solves this use case?
Let me… where's that tab?
**Pavol Loffay (Red Hat LLC)** 23:27 I liked it as well, more than, kind of, custom.
implementation. Yeah.
I think it's Cobra and Viper, because I'm not sure if Viper supports the flags.
**Jacob** 23:40 Yeah, is it… do you know which one it is? I always forget the difference between the two.
**Pavol Loffay (Red Hat LLC)** 23:45 I think Viper is for the config file.
Copra for the Flex, but it's been long.
**Jacob** 23:51 We want both, right?
I'll just say, I think, actually… Yeah, that'd be great, actually, if we could use one of those. They make life much, much easier, and I trust that code. So… Cool. Thank you.
**Mujib Ahasan** 24:25 Thanks.
**Jacob** 24:26 No problem, thank you.
Okay, back to it. Let's see… Let me get rid of that flag now.
But yeah, definitely great to see this, so thank you for the change.
Last one. Rejects immutable stateful set changes out of mission.
This is a pretty hairy one. I don't know if, Pavol, if you looked at this already?
I don't know if we have the author here. The idea here… This actually is a bit of a regression. We previously did this.
But, we had somebody that wanted the reverse of this, where we should just re- recreate the staple set.
If you change one of these, fields.
I think that this should just be a configurable behavior.
Rather than…
**Pavol Loffay (Red Hat LLC)** 25:25 What's the deal? Like, why do they want to reject?
**Jacob** 25:29 So… There's no good way to avoid this today.
Yeah, basically they just don't like this.
**Pavol Loffay (Red Hat LLC)** 25:41 distance.
**Jacob** 25:43 I would say to this person, why are you changing these immutable fields in the first place?
But… Yeah, I'm not… I don't love the idea of this behavior change.
Yeah, I would just say I would like this to be a behavioral thing. I think right now, as it is, changing this… For everybody is… is probably not good.
But, I don't know.
What do you think, Pavol?
**Pavol Loffay (Red Hat LLC)** 26:47 So the… I have to look at it, but… Is he introducing a braking change?
**Jacob** 26:55 This would be a breaking change.
**Pavol Loffay (Red Hat LLC)** 26:57 Yeah, then I think… We should avoid it, and… like, put it behind a, like, a feature flag, but I'm not sure about… That either, if this is, like, a… I don't understand why they… wanted.
If this is a.
**Jacob** 27:17 Yeah, I…
**Pavol Loffay (Red Hat LLC)** 27:19 Generally applicable, Use case, or is it something… More specific to, kind of, their needs.
**Jacob** 27:38 Necessary… I knew when you would… Do reject versus… Delete.
recreate. What exact issue?
This is both solving.
I'm gonna get rid of disguised SIG and put this on the issue, and just say.
And then link to my comment.
Collective comments on your… Assume, please follow.
Okay.
Okay, cool.
I think that's it. Do we have anything else from anybody in this meeting?
Any other topics du jour?
Shit, this one's…
**Tyler Helmuth** 28:47 say thanks for joining, Ervin, because we asked you to. And we're excited for you to be involved with the Helm Chart, and thank you for being here today.
**Jacob** 28:58 Yeah, thanks so much.
**Ervin Wallin** 29:00 I just would like to introduce myself. I'm Ervin, a platform manager in Erbeus in Hungary. I've been contributing the OpenTelemetry handcharts since August.
And I really enjoyed working on charts and reviewing PRs.
And I'm happy to join this meeting and meet everyone. And I'm interested in becoming more involved, and especially around the Helm charts projects.
And thanks for having me, and I'm looking forward to work together with you all.
**Jacob** 29:40 Yeah, thanks for joining.
**Tyler Helmuth** 29:42 Are you…
**Jacob** 29:46 Cool. Well, if that's all, we can… get another 30 back, and I can go have lunch, so…
**Pavol Loffay (Red Hat LLC)** 29:54 Enjoy.
**Jacob** 29:54 Yeah, thanks everyone. I'll see you later.
**Pavol Loffay (Red Hat LLC)** 29:58 It's fine.
