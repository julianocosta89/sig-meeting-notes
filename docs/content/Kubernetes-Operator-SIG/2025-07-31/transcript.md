SIG: Kubernetes Operator SIG
Date: 2025-07-31
Duration: 57 minutes
============================================================

## Zoom Recording Transcript

**Jacob Aronoff** 02:10 Hey! Benny!
**Benedikt Bongartz** 02:12 Is, 3.rd
**Jacob Aronoff** 02:13 Be honest.
**Benedikt Bongartz** 02:15 Sorry.
**Jacob Aronoff** 02:16 It might just be you and me today seems like a lot of people.
**Benedikt Bongartz** 02:20 Is there a wrong? So did you join in the last few seconds, or is there a wrong link on the calendar? Invite.
**Jacob Aronoff** 02:32 No, I I just. I joined the one from the operator like meeting.
**Benedikt Bongartz** 02:39 Yeah, because I was previously in a zoom call, and I was all the time alone. And then I clicked here on the top on this.
**Jacob Aronoff** 02:46 I think we have the right call. I just don't think anybody's here.
**Benedikt Bongartz** 02:49 Okay.
**Jacob Aronoff** 02:53 I think it might. Yeah, I think it's just us this time.
Let me see.
Oh, my God!
How is this still broken.
**Benedikt Bongartz** 03:15 What?
**Jacob Aronoff** 03:15 The release is like still broken.
I'm gonna take off. My!
Oh, this is awful!
**Benedikt Bongartz** 03:36 What is it? It's python, oldest.
**Jacob Aronoff** 03:49 Oh, God!
**Benedikt Bongartz** 04:43 Which release do you mean.
**Jacob Aronoff** 04:45 Oh, God!
Tyler just keeps getting like screwed with this release.
**Benedikt Bongartz** 04:56 This one! I see!
**Jacob Aronoff** 04:58 Yeah.
**Benedikt Bongartz** 05:19 Also Freshman.
**Jacob Aronoff** 05:21 I think I might just write the Pr today. Oh, this is really annoying.
Either way. Have you looked at Antoine's issue yet?
**Benedikt Bongartz** 05:35 The last 5 min to be honest.
**Jacob Aronoff** 05:38 Okay, I wanna discuss it because I don't like I'm not. I'm not Sure. I like this approach.
It seems like we're just gonna create a lot more problems for ourselves.
But I don't really think we can discuss it without any like anyone else here, to be honest seems like we don't have a quorum today.
No?
So how do you spell that?
So I smelled it?
We don't have a quorum today.
okay, Tyler's gonna join. We can talk about his problems. Super annoying.
**Benedikt Bongartz** 07:02 I wonder what did cause it.
**Jacob Aronoff** 07:07 It just seems like they keep breaking the Prometheus receiver. Hey, Tyler, I 1st off. I want to just apologize you. You've been put through the ringer the past few weeks I can take over.
**Tyler Helmuth** 07:16 My as well. It's not my fault. It's the collector's fault, but actually it's Prometheus's fault.
**Jacob Aronoff** 07:21 Of course it is. It's always Prometheus as well.
**Tyler Helmuth** 07:24 Useful.
**Jacob Aronoff** 07:25 No, I know I don't. I wasn't joking. I was. I was being serious.
Oh.
**Tyler Helmuth** 07:30 So the problem is, it's the same problem. It's the exact same problem for 1 30, which is in 0 dot 59.0 of. I can give you the direct, the exact dependency, if you'd like, but of the Prometheus exporter from the Go hotel.
Go SDK.
This dependency right here.
What the hell's this? AI summary shit in my slack? Go away! I just opened up a thread, and it was like, Here's.
**Jacob Aronoff** 08:07 I think I've disabled all of those.
**Tyler Helmuth** 08:10 I'm gonna have to go find that. So this is the.
This is the dependency. So this hotel go hotel exported Prometheus. This version, version 0 point 5 9.0 brought in some like Otlp Prometheus translation stuff that had a bug that results in the units being included in metrics that they used to not be included in by default.
**Jacob Aronoff** 08:36 Yeah.
**Tyler Helmuth** 08:38 They did that as an attempt to fix some other stuff. And it did fix those other things. But it broke these things. So it's like they're playing whack-a-mole with what these names should be.
**Jacob Aronoff** 08:49 The.
**Tyler Helmuth** 08:50 So they are aware of that. And they're trying to continue to like solve the problem on their end. Our attempt to solve the problem was, okay, we need to go back to 0 point 5 8.1 or whatever the previous, whatever the version was. That was in 1 29 of the collector.
**Jacob Aronoff** 09:07 Yeah.
**Tyler Helmuth** 09:08 That is so in core collector, we reverted that dependency we tagged.
We released.
If you go into core version, if you go to the commit that's tagged 1 31, and you do the go y. Whatever command.
**Jacob Aronoff** 09:26 Yeah.
**Tyler Helmuth** 09:27 What the dependency is.
Go version, dash m whatever you can see that the dependency is version 0 58.1 or whatever.
So good. Okay, so core is correct. So what happened? We're still researching is in in the release artifacts.
There's some other dependency somewhere that had a dependency on that Prometheus exporter 0 point 5 9.0 and so go doing its thing. It took the latest dependency.
And so, even though Core was tagged at 58 with that dependency. Some other dependency brought it back up to 59. So all of our release artifacts brought it back up to 59. So.
**Jacob Aronoff** 10:17 What?
**Tyler Helmuth** 10:18 Yang is looking at right now is adding a replace statement into the manifest file, so that when we build, when we build.
**Jacob Aronoff** 10:29 The binaries.
**Tyler Helmuth** 10:31 It'll it'll like force it to be 0 58.0.
So we're probably going to have to release a 1 31.1 of the artifacts. We're not going to have to re-release core. We're not going to have to re-release contrib.
At least I have to go look at contrib. Again, we might have to re-release, contrib.
I'm not totally sure.
**Jacob Aronoff** 10:53 I am looking at. Oh, wait, let me let me be sure I'm on the right version here, but I do see in core 59 is still there.
**Tyler Helmuth** 11:02 Correct.
So 2 days ago, main encore, 2 days ago, bogged and merged a dependable Pr that bumped that version back up, we shouldn't have done that.
**Jacob Aronoff** 11:13 Yeah.
**Tyler Helmuth** 11:13 Yang has already opened, and I've already approved a revert of that bump.
**Jacob Aronoff** 11:18 Okay.
**Tyler Helmuth** 11:18 Back down.
But May, the latest of main encore doesn't matter so much, because it's not what.
**Jacob Aronoff** 11:23 Yeah, because.
**Tyler Helmuth** 11:24 We'll make sure that that's right. Before the next release.
**Jacob Aronoff** 11:26 Yeah.
**Tyler Helmuth** 11:26 Apparently the Prometheus group, and, like the Go Sig, is working on like a real fix for all of the a metric Prometheus metric name.
**Jacob Aronoff** 11:38 Yeah.
**Tyler Helmuth** 11:39 Problems. But right now, in operator land, I think the goal will be to take. The collectors re-released 1 31.1 artifacts that will hopefully go out today because I believe that the I believe that forcing the manifest file, it will like be a solution. And I'll have to test that later. I'm not the collector release manager.
I just keep finding this as the operator release manager.
**Jacob Aronoff** 12:15 Yeah, so.
**Tyler Helmuth** 12:16 I'll just deal with the collector release today, too, because I'm on call also. So like it's the week of of busy work.
**Jacob Aronoff** 12:23 Yeah.
thank you for doing all this. I mean, it's so this is so painful. This is appreciating. Like, go thing. Yeah. So it's it's very appreciated.
in terms of. So there, there are 2 things that we discussed I think, last meeting, which I don't know. If you saw the notes from from our last Sig meeting. But one of the things that I think we're gonna start doing is running the end-to-end tests that we have on the latest contrib image daily.
**Tyler Helmuth** 12:57 So the one that releases every night.
**Jacob Aronoff** 13:00 Yeah, exactly. I mean, we might be like a day behind, because I don't know.
**Tyler Helmuth** 13:04 Yeah, that's fine. But taking that frequent frequent image, yeah.
**Jacob Aronoff** 13:09 Yeah, that way with our releases there, we'll be able to know before we do a release. And before collector does feedback back fully broken because it seems like our end to end. Tests are.
I guess, more comprehensive because we're actually like running stuff.
**Tyler Helmuth** 13:27 Yeah, I mean the fact that you're just checking outputs. The collector has some end-to-end tests, but but not like, not like the operators, because the operators is well, especially not Prometheus end to end test, like, someone is working on adding those right now to core because of this problem. But yeah, I mean, I think that sounds like a good idea for the operator to do.
**Jacob Aronoff** 13:47 Yeah. So I'll maybe write up that Pr today. Just cause this has been such a frequent problem. I mean, this is played this for the past like 2 months, I think.
**Tyler Helmuth** 13:57 I know this these summer releases are like not going well.
**Jacob Aronoff** 14:00 I know they're brutal, especially everybody's out as well. And so it's really hard to like, get people to. Yeah.
**Tyler Helmuth** 14:06 I don't know what's happening in collector that's making me so bad right now. But.
**Jacob Aronoff** 14:11 Yeah.
**Tyler Helmuth** 14:12 I guess technically, this wasn't the collect. This is for me this fall, but where everyone feels the effects of it, because breaking breaking metric names is an incredibly bad breaking change that's very hard to catch.
**Jacob Aronoff** 14:26 Absolutely. I mean, we I think we all know that like that is.
**Tyler Helmuth** 14:29 I mean. That's why we're still stuck on the Java and.net versions that we default because of those changing semantic conventions.
**Jacob Aronoff** 14:39 Yeah. And I, I have a backlog item to like, begin the process of.
**Tyler Helmuth** 14:43 Yeah, I'm pretty sure we just need to do it.
But those yeah.
**Jacob Aronoff** 14:48 We'll need to. So I think what we talked about doing. I don't know if we came to a decision. This is a few weeks ago.
Oh, nobody took notes on it.
**Tyler Helmuth** 14:59 I did comment in the pinned issue the other day, because I think someone had messaged in it, and I saw it.
**Jacob Aronoff** 15:07 Yeah, yeah, Michael, I had commented in here, but the thing that I wanted to do was Mika had a few of his own ideas the thing that I wanted to do. I wish we I wish we wrote it down. I guess we could go through the the notes or the recording, I mean. But what I want to do is release a new version of the instrumentation Crds, and not do an automatic upgrade for those, and then just gradually deprecate the old ones, so that users need to manually upgrade to the new instrumentation objects. And then either one of 2 things will happen. They do that, and they know the breaking changes, and they're aware of it, and they can fix it. And we give a guide on like how to fix it.
**Tyler Helmuth** 15:56 Yeah.
**Jacob Aronoff** 15:57 Or they upgrade without reading the change log without reading the like, breaking changes between the version and then it breaks, and then they're like, what the hell and we're like, hey, we, you know.
Look here, we.
**Tyler Helmuth** 16:09 It is. Yeah.
**Jacob Aronoff** 16:09 Yeah, here it is, and then the 3rd option is they forget to upgrade their instrumentations. They upgrade the operator, and then the old instrumentation isn't there? And then all their instrumentation is broken. They revert, and then they come to us, and they're like what the hell happened here. And it's like we pinned it here. We pinned it here. We pinned a message here like.
**Tyler Helmuth** 16:27 Yeah, I mean, we've yeah. It's been pinned for a long time. So.
**Jacob Aronoff** 16:30 Yeah, so.
**Tyler Helmuth** 16:32 One thing that I like that Antoine mentioned, for the end to end tests is we would also solve a lot of our problems. If we weren't using Prometheus metrics which are difficult, for the reason that we're experiencing right now.
it would be really cool if we had Otlp. But I understand that that's hard for an end to end test, because it requires something to receive the otlp instead of scrape the otlp so.
**Jacob Aronoff** 16:56 Yeah. Earlier in the year we talked with Laurent and a few other people who are working on Weaver, and they're working on a thing that will be like a sort of in memory time series database, or like hotel database. That does checking against semantic convention, and we'll just use the output of that for validation rather than relying on ourselves to do that validation cool. But until that lands and I don't know when that's gonna be like we're kind of in a in a dead zone.
**Tyler Helmuth** 17:29 I know this would in the past use. Oh, go ahead.
**Benedikt Bongartz** 17:33 So for the end-to-end test, couldn't we just run an open time to collector and you send them all the data to the open time to collector having permitous exporter endpoint, and then you could also do the validation. There.
**Jacob Aronoff** 17:45 Oh, and see that the Prometheus scrape output is the same as the Prometheus exporter output.
Is that what you're saying.
Oh, oh, no! I see what you.
**Benedikt Bongartz** 17:56 No, you would export. Instead of having some in memory database, we just use the open time to collector. So you send all the telemetry data to a single instance of an open telemetry collector, and then you can scrape the parameters endpoint of this open time collector afterwards. So not the perimeters endpoint that is there to tell you how the collector behaves the exporter, the parameters exporter, which offers you an open endpoint.
**Jacob Aronoff** 18:22 I see, I think for now I actually think that, given that, we keep running into this problem, I think that's a good thing that we're like catching this, because otherwise it would be.
**Tyler Helmuth** 18:32 Gone unnoticed, if not for the operator, probably.
**Jacob Aronoff** 18:35 Yeah. So I think that there's value in us doing this for now. I think the value in doing the semantic convention thing is that we wouldn't need to write our own validations theoretically, like Weaver would just do the validation for us, and and check everything rather than like our sort of spot checking But I think that the idea of like using a collector to do the to receive Otlp and like do validation on. That is a good one, and it's something that we probably should do, especially for like instrumentation. We don't have any. I think we maybe have a few of them now, but we don't really have like instrumentation checks. I actually think there is a semantic invention receiver or something like that in the collector. Now, I might be misremembering. But I thought I saw something about that.
okay, either way, I'm gonna try and just get out a Pr today to begin running the contrib tests daily. Cause. I think that that would be really valuable for us to do and Tyler is on the release stuff. So he's gonna handle that.
Thank you to Tyler. I know he's away. And then hmm, oh, Sorry So I think we're good there. I wanted to move on to talk about Antoine's thing. If that's alright.
Pavel, have you looked at Antoine's Pr. Yet?
No, I think we I think it's worth us having, like an informed discussion on it, because it's pretty different than a lot of the approaches we've done in the past.
and I want to sort of get a informed consensus on it.
because the idea behind it is like, what if we could embed the instrumentation crds in like a yaml config that the operator uses to configure itself on startup but the I think that alone I might be okay with. But the way that we're doing. It is by recreating all of the instrumentation crs as separate go structs that we need to maintain 2 of now. And I really don't like that approach to it.
And so that that's the thing that I I'm hesitant about doing I think, actually just putting in the config file is relatively harmless. I I don't love it, but I I don't think I'm necessarily. I'm not like ideologically opposed to it. I think it's just the like. Don't don't repeat yourself. Aspect of it. That is dangerous to me.
**ploffay** 21:26 I think I don't understand the.
**Jacob Aronoff** 21:30 Okay.
**ploffay** 21:30 Pr, and proposal. Maybe. Can you explain again with like high, level.
**Jacob Aronoff** 21:37 Sure. Yeah. So the work that Antoine's been doing for the past few months is essentially like making it so that we could use a yaml file to configure the operator rather than sort of config flags right?
His stated goal is to make it so that a user can install only an operator, no Crds, and get auto instrumentation so that you don't need to do multiple stalls of things right?
And what he's trying to do now is sort of one of the later parts of that process which is making it so that you can configure the operator's instrumentations via the config file rather than installing a Cr but because it would cause a import cycle. He had to fork the structs that we use for the instrumentation, crs and then convert back from the fort version into the Cr version when the operator is doing its reconcile loop.
And so the thing that I don't like is that forking of the resources. That's the thing that I didn't like about the Pr. I think otherwise. It makes plenty of sense. I just don't like needing to fork.
Call it like 2,000 lines of code, you know.
**ploffay** 23:04 And I have follow up question. So yeah, I understand that he wants to configure the operator by a config file. I think there is no.
that that's a good approach, and I think everyone likes it. But I'm not sure about that. He wants to have the auto instrumentation capability without the instrumentation Crs installed in the cluster like how that would work? Would it like be? The operator would be configured at the startup? What instrumentation Cr should use for all the annotations that are out there. Something like that.
**Jacob Aronoff** 23:45 Yeah, I think the his idea is essentially is is essentially to like by fully embedding the crs in the Yaml file.
That is the same. It's like the exact same config as one would apply with the instrumentation. Cr like in the cluster.
Right?
And it would just be the exact same loop post installation. Essentially
**ploffay** 24:10 Where? Where is the instrumentation, Yaml like, is it?
Is it.
**Jacob Aronoff** 24:16 Oh, I I see what you're it! It's like fully embedded in the config file under like.
**ploffay** 24:24 Okay, so it's, it's like a global instrumentation. Cr.
**Jacob Aronoff** 24:27 Yeah, yeah, exactly.
And yeah, I I don't know if I'm like opposed to that. Necessarily, I think it's kind of odd. But I also don't. I'm like trying to think about the precedence of it.
Like, I think Prometheus has the idea of global scrape configs like the Prometheus operator has a concept of global scrape configs. And it's self configuration and a Dml configuration.
Things that get applied like, no matter what.
So I think there is some precedence for it.
I I just don't. I don't want to fork the code that that's the thing that I don't like.
but.
**ploffay** 25:11 Yeah, I think the the precedence gets bit more complicated here, because there will be some duplication like the instrumentation images. There is a dedicated flag on the operator. And now it could be as well configured in the Cr right? So so that's that's something to think about. We internally got requests for a similar or the same capability, like customers wanted to have kind of cluster, scope, instrumentation. Cr, that would be used.
Which I think there's direct correlation with this approach. But we would as well had to make the operator config work with the Olm deployment, which is always a bit problematic.
**Jacob Aronoff** 26:07 Yeah.
I'm just taking notes, Paul. So just give me a second to catch up this.
Okay, I I put that down in the notes.
Your! Do you have any thoughts on this? I know you just joined, but, I don't know if you got a chance to take a look at the issue yet.
Oh, you're muted.
**yurioliveirasa** 26:58 Not yet. But let me check.
**Jacob Aronoff** 27:00 Okay, I I can link it to you here as well.
**yurioliveirasa** 27:02 That's good.
I know the thing. Oh, sorry! Go ahead.
**Benedikt Bongartz** 27:11 No please. Go ahead.
**yurioliveirasa** 27:12 I was kind of paying attention about the configuration through the config file instead of the the instrumentation. Cr, because I'm working currently in a mood instrumentation precedence, and for that reason was kind of yeah, concerned about how we're gonna handle that, you know.
**Jacob Aronoff** 27:32 Hmm.
yeah, I I agree.
instrumentation. Precedence is is an interesting thing. Will we have to do something like priority levels? Do you think.
**yurioliveirasa** 27:48 Yeah, because right? Now we have. Yeah, it's it's not the same precedence that you are talking about precedence. I mean, yeah, between the config file and the instrumentation. Cr, but precedence more related to the annotations being set in the namespace and in the pods and annotations being related to to a specific program language or a SDK in general.
How should we do that, you know? And then I discuss it with Israel. And 1 1 agreement that we have is basically, if we have a annotation being set on the pod specific for a Java or a python app. It will take precedence over the namespace.
**Jacob Aronoff** 28:38 Hmm.
**yurioliveirasa** 28:39 You know, it's like that. And then I'm yeah. I'm working that pr to fix this this bug, because right now if you have both set.
then, the namespace will take precedence over the the application.
**Jacob Aronoff** 29:01 Yeah, this is also confusing.
**yurioliveirasa** 29:05 That is also confusing. Then my question, yeah, Pavel Pavel mentioned a very good topic, because, okay, we have to decide about this precedence. But this precedence also open opens a new, a new possibility about the precedence about the annotations on pod and annotation. The name space, like A guy can point a config file to instrument only for the namespace and acr only for the applications, or something like that, you know, and then can in in the end of the day.
can can turn to a mess, you know.
**Jacob Aronoff** 29:50 Yeah, I I do wonder if, like.
I mean, this is kind of the same discussion that we had, I guess, like a year and a half ago about the label precedence stuff, and like. How we determine that if you remember that conversation for determining like what we use for service, name right?
**yurioliveirasa** 30:08 Oh, yeah. Sure. Yeah.
**Jacob Aronoff** 30:10 This one is like fully in our realm, and not a like semantic invention thing, but as a result like I, I do wonder if we should have a a priority number on instrumentation resources so that users can set set it deliberately for the behavior that they want, and then we can assume we we can just mandate. This is the default priority. And then we say, if you want to override this, then set this number. Essentially, I don't know. Maybe maybe that's over complicating it. But.
**yurioliveirasa** 30:43 Yeah, I would say, probably is.
**Jacob Aronoff** 30:47 Is, a.
**yurioliveirasa** 30:47 Yeah, yeah, it's getting. It's getting more. Yeah, it's getting more complicated. Sorry about that. I would. Yeah, it's not yeah. It could. It could sound biased because I'm working that Pr, you know. But I would. But I would go with the precedence that we we should. That should work today, you know. Like, if we have an annotation on pod, it will take precedence of on on the namespace one.
Well, I don't know. It's it's the way I think.
**ploffay** 31:26 Yeah, I think this like overriding the precedents, either explicitly.
it's gonna create even more confusion. Probably like, I hate this with logging frameworks, with logging Apis like you can set any number, and you never know like what number should put in like and what are the other numbers used in the in the code base. And like, I have no idea if that log is gonna actually go out or.
**yurioliveirasa** 31:58 Yeah.
**Jacob Aronoff** 31:59 I do. Need. I also hate logging?
Yeah, I maybe that was a bad idea. So let's not do that.
But I think all this sort of relates to Antoine's original issue of like, How do we expect this to work? I also think that Antoine's proposal is not global, and it is just embedding the actual crs in the config, not something to be applied like, I don't think the the ones that he's embedded. Maybe I'm misunderstanding. Spr, but I think it's not instrumentations to be applied everywhere, but rather instrumentation resources that don't need to be applied by the user. If that makes sense.
Thank you, Tom.
**yurioliveirasa** 32:51 I don't understand you. Yeah. Yeah.
Oh, my God, sorry. Yeah.
**Jacob Aronoff** 32:55 No worries, so I'm pretty sure his proposal is like.
whereas so the thing that he's trying to avoid essentially is you do helm install O hotel operator, or whatever. And that user after that, does like a K apply instrumentation resource right?
Like that two-step process. He's trying to get that down to one step, and I think that he wants to do that by having Helm install hotel operator, and then you say you would embed the instrumentation resource in the Yaml file config for the operator. And it's the same thing that you would apply as a normal instrumentation.
**yurioliveirasa** 33:31 Well.
**Jacob Aronoff** 33:32 It.
**yurioliveirasa** 33:32 Well, but I would I would do that differently. I would keep. Yeah, I would keep the instrumentation one, and in the home chart. I would create template for the Crs. And then kind of work with status, you know, instrumentation, neighbor or not.
like.
**Jacob Aronoff** 33:51 You the other pattern that people do. That's actually a great point. The other pattern that people do is you have a what's it called? Not extra values. It's like extra templates or something.
**yurioliveirasa** 34:04 Okay.
**Jacob Aronoff** 34:05 In in a helm chart. Let me see if the let me see if we already do this for the collector. I remember seeing an issue.
Semi recently.
**yurioliveirasa** 34:19 Yeah, because, well, yeah.
thinking louder here is if we create a a kind of for loop in this instrumentation, cr template and then create like a values and options in the values for the helm chart, for the operator, for example. And then you can create like instrumentation enabled through a false, and then each like each each field of the instrumentations here, like in variables collector, host program language, and so on. And then the user can set this up and basically run the install.
it will be simpler right.
**Jacob Aronoff** 35:12 Yeah, is, are you suggesting that we do something like this? I linked it in the zoom chat here.
**yurioliveirasa** 35:18 Said.
but I don't know what this extra money 1st does.
Bye.
**Jacob Aronoff** 35:32 You would just input like the literal instrumentation Yaml, content that you want installed with this chart. Is that what you're talking about or no?
**yurioliveirasa** 35:43 No, no, this this no, no, no, no! A actually almost like this. But I would instead of doing this as we have the instrumentation cr natively defined on the operator side, I would create a proper template for this year, you know, I would not put like extra field for the instrumentation, you know. You can just define the instrumentation properly, you know.
Did you get my point.
**Jacob Aronoff** 36:19 Yeah, yeah, yeah. I'm I'm just writing it down.
**yurioliveirasa** 36:21 Okay.
**ploffay** 36:24 I I like the the notion of like operators. Default, instrumentation. Cr, I'm not sure I like the idea of having the instrumentation cr embedded in the config so that it would be applied to the cluster when the operator starts. That feels sort of like we're and should be handled by the packaging mechanism.
**yurioliveirasa** 36:51 No, okay, got it. But let's just display the idea. If it's possible.
I don't know, for example, how the user does the helm process. Because.
if the user installs only the operator per seat. Okay, it's 1 thing. But how the user operates, the open telemetry collector, Cr, how the user install that.
**Jacob Aronoff** 37:17 Hmm.
**yurioliveirasa** 37:18 It's it's through a a helm, or it's through like a pipeline, or I don't know another helm. Another application helm that install the operate, the the collector.
**Jacob Aronoff** 37:32 Yeah.
Yeah. I think the you know, I think, is where we'll need more context from Antoine about like, why he wants to do it this way, and not just bundle it, because I think I I think all of us are kind of converging on the idea that it should just be bundled with the install. Right?
Is that a fair summary.
**ploffay** 37:57 Hmm, yes and no.
ye yes, but at the same time I think the notion of of a default instrumentation that is set to be like cluster wide makes sense, and I have seen requests for it in the past.
**Jacob Aronoff** 38:13 Hmm.
**ploffay** 38:14 And this could be implemented in with the old one approach of having it embedded in the config and not as like a real cr like cluster scope. Cr, yeah, cluster instrumentation. Yeah.
Yeah.
But being directly in the in the operator conflict that would work as well.
**yurioliveirasa** 38:38 Yeah.
**Jacob Aronoff** 38:41 So Paul, just so, I'm getting this this note correct. You're you're saying it would be better to have a global instrumentation config that is, in that operator Yaml config.
and then that is like the the default.
That the operator would apply if no other instrumentation resources are found.
**ploffay** 39:00 Yeah, that I think that's feature makes sense to me.
**Jacob Aronoff** 39:04 Okay, yeah. I think feature. Oh, Yuri, go ahead.
**yurioliveirasa** 39:09 I have a a question I I just asked. That depends how the user deploys the the open telemetry, the open telemetry collector. But yeah, taking a look on the helm on the helm ripples. We have a helm for the operator. We have. We have the helm for collector, and so on. But we don't have helm to install the operator. Crs.
I mean the open telemetry collector and the instrumentation.
Do you think? I don't know would make sense choosing. Oh, we do have. Okay? Sorry this one. Yeah. But this one, it's it's like.
okay.
okay, like in the in the open telemetry cube stack.
**Jacob Aronoff** 39:59 Yeah.
**yurioliveirasa** 40:01 So if if we have that to to this open telemetry cube stack in order to install the open telemetry collector. Cr we should be able also to deploy the instrumentation. Cr, right.
**Jacob Aronoff** 40:18 Yes, I like, I think what you're saying is like this chart maybe technically solves the thing that Antoine wants to do.
**yurioliveirasa** 40:27 Yeah, yeah, because if we have a way to deploy open telemetry, collector instrumentation. Cr, it, it's all.
**Jacob Aronoff** 40:38 Can we not?
All these?
Maybe in this is where I really need, like Antoine's context, I do remember some of the work that he was doing was also to make it so. You didn't need to install any Crs or like any of the web hooks.
which doesn't mean I mean, I don't understand. Well, I understand. Not wanting to install all of the Crs, but not wanting to install any Crs. Doesn't make as much sense to me.
Well, I'll context for that cause.
**yurioliveirasa** 41:15 Yeah.
Yeah, the link that I posted. This is exactly what I what I need.
**Jacob Aronoff** 41:21 Yeah, that that's kind of what I what I was hoping you were referencing.
**yurioliveirasa** 41:25 Yeah.
**Jacob Aronoff** 41:28 I do need more help with maintaining that chart. By the way, if if you want to assist me.
**yurioliveirasa** 41:33 Yeah, for sure. Sure. Sure, you have built some issues there.
**Jacob Aronoff** 41:38 Yeah, anyway.
So I think all of this is good discussion. We'll all of Anto, Antoine said he was gonna review the recording for us. And then we'll probably just discuss on slack more. I'm sure Miko will also have some thoughts as well, so we'll maybe let him capture those. Are we good to move to the next one? Or do we have more things? We want to add to this discussion.
**yurioliveirasa** 42:05 Nope.
**Jacob Aronoff** 42:06 Good probably got anything else. I I know you're next on the list. But I mean anything else for this discussion.
Good. Okay, so you have this one. Introduce network policy.
**ploffay** 42:21 Yeah. So the.
**Jacob Aronoff** 42:22 There!
**ploffay** 42:23 The idea is to create network policies both for the operator and operands, meaning the collector, target elevator and oamp the reason is to be more secure, and the network policy should allow only required ingress or egress communication that that is needed. Right? So for the operator, it means enable scraping of the the metrics endpoint enable the web hook endpoint, so it's reachable and enable egress communication to the Api server. I think those 3 are only required for the operator and then for the collector. I wanted to start with the ingress, so get all the the receiver ports and enable them.
Oh, all of them and then maybe look at how the exporters are built. Parse them and allow only the those kind of explicitly. But we don't have any exporter purchases at the moment, so that would come separately.
yep.
yeah. But I I wanted to kind of work on this gradually 1st have the operator and then the collector with the receivers, then add the exporters, then look at detachable 8 and one.
**Jacob Aronoff** 44:05 I think this all makes sense. I'm definitely a fan of it, because it means that we can get rid of the What's it called kube r back proxy? Right?
I think that's the this is the thing that would allow us to remove, that. I actually don't even think we need coup our back proxy anymore at all. But this is the thing that would allow us to like really kill it. I think.
**ploffay** 44:26 Yeah, yeah. For the Arab proxy. There is as well a different feature. Request that it's kind of. I think it's deprecated. And there is, it can be directly configured on the Controller on time. I believe.
**Jacob Aronoff** 44:38 Oh, really.
**ploffay** 44:39 Think, so, yeah.
**Jacob Aronoff** 44:41 We should do that too. I I think that this is the this actually solves the goal of what we were using it for, though.
The one thing I the one question I had about the operator Pr, the collector, one makes a ton of sense. The operator one. I was wondering if, instead of because so in order to do this, we need to require the network policy permission.
Instead of doing that, I was wondering if We could just have it a flag as a flag, or something that we bundle with the operator on install, maybe in the helm chart, and maybe in the actual bundle as well.
Just for the that way. We don't need to add the elevated permission here yet for users who don't want it, and then for users, for when we do it for the collector itself, then we can add an optional permission from the helm chart and from the bundle to specify that they want this capability in the same way that we do for the There's another one that we do this for for the R back stuff.
**ploffay** 45:46 Service monitors, probably. Or, yeah, we there's.
**Jacob Aronoff** 45:48 Yeah.
**ploffay** 45:49 Yeah, so yeah, for the we package operators as a helm chart and as well as the oil and bundle. The oil and bundle doesn't support network policies. They are planning to support it for the next version. But it's it's not there at the moment. So yeah. But it's it's an excellent question like, How do we enable this this feature? And whether we enable it by default or not? We should talk about it.
So at the moment the operator has a flag to enable the the network policies, if the flag is on, it will create the network policy for the operator and then for the operands. I I was planning to have it in the Cr, so like.
**Jacob Aronoff** 46:38 Yeah.
**ploffay** 46:38 Cr, that would be flagged like, okay, I want to have network policy for my collector. And now the question is like, do we make it by default enabled on the Crs, or do we disable it? What's what's kind of the approach.
**Jacob Aronoff** 46:53 I think this feels like a good feature gate, because I think that everybody will want it. I think it's good security practice.
I don't know if we need to fully config flag it, but maybe that's just my own headcanon. I I remember we like wrote some guide about what is a feature gate versus? What is a like like? What do we feature? Flagged.
**ploffay** 47:14 Yes.
**Jacob Aronoff** 47:15 I kind of forget what that guidance is. I feel like that's Nicolas Department. He has a lot.
**ploffay** 47:22 If we eventually are planning to enable it by default. Right? Something like that.
**Jacob Aronoff** 47:28 Yeah. And I think everybody would want this. I don't know in what cases people wouldn't want like network policies unless they're too strict, right?
But.
**ploffay** 47:39 Yep.
**Jacob Aronoff** 47:41 I don't know. I think it makes sense for us to feature, flag it for the operator itself, and maybe add it to the Cr for the collector.
Because maybe someone who's using the collector has a custom exporter custom receiver. And our network policies are like too strict for them, and we're not like creating the right thing for them. Something like that I could imagine. But for the operator. Yeah, I I think my only the only thing that gives me pauses. It would be great if we could just make the resource as part of the bundle rather than having the operator create it. I just think it's a lower burden on the operator and easier like user experience.
But if you're saying.
**ploffay** 48:22 That will not work. Yeah, that can do that.
**Jacob Aronoff** 48:25 Yeah, if you're saying we can't do that, then that's that's another problem.
So I think I'm for it. I I don't see why I wouldn't for this definitely. Nicola will have thoughts on this, and I'm bummed he couldn't join, because I also wanted to hear his thoughts on Antoine's thing. But I definitely, I definitely am for this, and I think it'll be great also to eventually do it for the collector itself.
And yeah, I think that'd be really useful.
This does make me think this is a very like long term thought. Well, actually, before I go on a long term, thought Gary. Do you have thoughts on this that you want to share.
**yurioliveirasa** 49:05 Yeah, I. I also go for it. But I was just wondering about if we have any constraints about cloud kubernetes in different clouds like Tcp. That has a problem with a firewall port or or not.
I mean, it's just wondering if if it could generate any impact.
No.
**ploffay** 49:33 I I'm not sure I I don't know. I just checked if the network policies are supported on all the Kubernetes versions that we support.
**yurioliveirasa** 49:40 Yeah.
**ploffay** 49:41 That's that's fine. But I don't know if any distribution handles something differently that we could break.
**yurioliveirasa** 49:50 Yeah.
**ploffay** 49:50 It's it's a kind of standards. The Kubernetes objects so I think, should be uniformly supported.
**yurioliveirasa** 49:58 Oh, yeah, okay, yeah. Just just wondering if it will. It will will generate any impact on that, you know.
**ploffay** 50:10 So let's maybe talk more about the the configuration. So on the operator, we should have a flag better.
The operator should create network policies for itself and then for the collector or touched allocator, there will be field for network policy, right? Whether it's enabled or not. That it's a booing flat enabled, disabled.
would we default to false?
Maybe from the beginning, and and have a feature flag on the operator?
If you enable it, it would default it to to true.
does that make sense to you guys?
Yeah. So to summarize 2 feature flags on the operator, one controls the network policy for the operator itself.
Second feature flag controls the default value of the network policy for the operands like we would start with more relaxed condition, like default false, so don't enable it, but enable it later on to all deployments.
**yurioliveirasa** 51:25 Yeah, yeah, we can set a, let's say a milestone in a specific version, like, okay, on version one we, gonna we've revert it through, you know.
**ploffay** 51:38 This would give time to users to to test it out and see if they're using any custom receiver or or anything, any custom component that opens a port essentially.
**Jacob Aronoff** 51:50 One thing that I just put on the notes here is it'd be good to use a real end to end test, to verify that when it's when, like all of the conditions, allow it to be created. That it succeeds. And then we tested, the creation succeeded, but also that trying to access something that isn't in the policy fails. So that we're like, we have a lot of confirmation that the functionality of the network policy that we're creating works as well.
Does that make sense? I I don't know what the failure mode is for the or network policy. I haven't played around with them much.
but I think it'd be really cool to just. It'd be good for us to just confirm that they work as expected, so that we don't push something out that has some unknown edge that we forget.
I think that's my only the only thing that I don't think is in the pr right now, otherwise sounds good.
Cool any other thoughts.
No.
**yurioliveirasa** 52:58 Cool.
**Jacob Aronoff** 53:00 I'm gonna take a look at the let's just look at the feature gate. Stability.
let's see.
Yeah, we have a few in here that we could probably remove. But I don't wanna do that right now.
And then any discussion issues. We have Antoine's which we did pod disruption budget.
Where's this one?
Okay, this was from last month. I don't know if this was discussed already.
I'm gonna put it in the chat here.
**yurioliveirasa** 53:47 Right.
**Jacob Aronoff** 53:47 You can take a look at that.
**yurioliveirasa** 53:51 And sorry to to go back. But I just saw your annotation on the see, Doc Jacob, it's it's my concern that regarding the network policies, not about versioning, but about the cloud constraints. You know the Kubernetes running on Cloud run on cloud, because, for example.
in azure or aws, we don't. We don't see any problem. Problem. Usually, I mean, but, for example, specifically, in Gcp, we have to set some error rules in order to get the operator running. You know.
Then, as we are activating actually about network stuff, I was wondering if we we gonna see any any issue about that, you know.
**Jacob Aronoff** 54:41 Yeah.
**ploffay** 54:41 Is the is the book that is problematic.
Here we go.
**yurioliveirasa** 54:46 Yeah, yeah, it's the web hook that you have to set that. You have to open the fire. The port, if I'm not wrong. The 4. Sorry. 9, 4, 4, 3, something like that.
**Jacob Aronoff** 54:58 Yeah, we we have an old pinned issue for this, I think, somewhere, or or we have something in here about like, Gcp.
yeah, right here.
I remember this specifically. Yuri cause. I remember, like 3 years ago, I was helping a customer out that was on Gcp. That had this exact thing, and we had it in a like really like low down issue that was closed, and I copied it over to documentation.
**yurioliveirasa** 55:23 Yeah, sure.
**Jacob Aronoff** 55:25 So I remember this like really well.
I did add this to the to the re, like main readme.
**yurioliveirasa** 55:31 Oh, that's great. Yeah. Okay, yeah, yeah. This one. Yeah. I was, I was right about the port. Yeah.
**Jacob Aronoff** 55:39 Good documentation.
**yurioliveirasa** 55:40 Yeah, thank, you.
**Jacob Aronoff** 55:44 Cool anyway. So let's see.
citizen thing that can be defaulted.
So it looks like this user. And maybe we, we're kind of at time here, and I don't. I don't know if we have time to like discuss more.
**yurioliveirasa** 56:02 Whatever.
**Jacob Aronoff** 56:03 So maybe let's do this when we have more people around because we went over the hard stuff already.
Okay.
cool. Anything else that we want to discuss. I mean, we should discuss those issues. But we are kind of far from enough people to discuss effectively.
All good this year.
**yurioliveirasa** 56:29 Yeah or no, I'll be there.
**ploffay** 56:31 No.
**yurioliveirasa** 56:32 No, here he is. Yeah, you get 1 1 approved. Right? Jacob.
**Jacob Aronoff** 56:37 Oh, I did. Yeah.
**yurioliveirasa** 56:38 Yeah, congratulations.
**Jacob Aronoff** 56:40 Thank you.
**yurioliveirasa** 56:41 You too, Bob, or not?
Do you get in any any talk accepted or not?
**ploffay** 56:47 No, unfortunately no.
**yurioliveirasa** 56:49 Okay, got it? Yeah.
**Jacob Aronoff** 56:50 It feels so.
**yurioliveirasa** 56:51 As well.
**Jacob Aronoff** 56:52 I think they just pull it out of a hat. This is the proposal that I've spent like the least time anguishing over but it's the one that gets accepted where, like last year, I spent, I don't know 10 h like tuning my proposal to be like just right. And this time, I just like, you know, threw it together in like 30 min with crystal, and this is the one that works.
I don't know it. It seems very random, and the topic is like the same thing that we always submit to. It's like I. So I don't know, like I don't know what happened.
**ploffay** 57:25 I will submit it next year. Then.
**yurioliveirasa** 57:30 Exactly.
Oh, man, yeah, that's great.
**Jacob Aronoff** 57:35 Okay. Well, I'll see you there. Yeah.
**yurioliveirasa** 57:37 You're there, Paul.
Thank you. Guys. Bye.
**Jacob Aronoff** 57:40 Bye.
