SIG: Java Declarative Configuration
Date: 2026-01-22
Duration: 53 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 00:14 Hey, Gregor!
Can't hear you yet.
**GZ Gregor Zeitlinger** 00:59 Can you hear me?
**Trask Stalnaker** 01:00 I can.
**GZ Gregor Zeitlinger** 01:01 Okay But you couldn't before.
**Trask Stalnaker** 01:07 No.
**GZ Gregor Zeitlinger** 01:07 Okay.
**Trask Stalnaker** 01:09 That explains why you didn't answer.
Alright, let's get into it.
If we have time, maybe we can just spend some time on this. I… sorry I haven't, but I, I… agree that we need to do something like this. I just haven't looked at the details. Let's start with…
**GZ Gregor Zeitlinger** 01:39 Something as what? Sorry?
**Trask Stalnaker** 01:41 Oh, we'll come back, we'll come back to this.
Okay.
Let's start here… Yeah, this is a good point.
**Jack Berg** 02:04 Hey, Trots.
**Trask Stalnaker** 02:05 Good luck!
Hey, welcome.
**Jack Berg** 02:09 Sorry, I haven't made it to more of these, I'm gonna try.
**Trask Stalnaker** 02:15 Cool.
Yeah, our format is basically just reviewing PRs together.
**Jack Berg** 02:25 Cool.
**Trask Stalnaker** 02:27 So, this one… Do we want…
**GZ Gregor Zeitlinger** 02:39 So what impact would this have? We don't have to support it, because declarative configuration is an explicit opt-in.
**Trask Stalnaker** 02:53 Right.
So, if somebody has an extension… Is using an extension.
they would… Not be able to move to declarative config.
Until that extension supports declarative config.
**GZ Gregor Zeitlinger** 03:16 Right.
**Trask Stalnaker** 03:21 Which isn't… That it's almost maybe… Preferable to if it… if we magically make it support declarative config, and then we… Remove that support in 3.0.
We're kind of… We're kind of saying…
**GZ Gregor Zeitlinger** 03:42 And there are already some corner cases that don't even work because, we just have not added this weird combination of, You having config properties access, and then also using, declarative configuration.
With the latest changes in distribution, at least.
And there may be more that I have not thought about.
**Trask Stalnaker** 04:08 and extensions… with declarative… supporting… declarative config and extensions is probably gonna require a good amount, like, work on the extension anyway, because of the SDK… Assuming that… a lot of extensions, or are you adding, like, span processors?
**GZ Gregor Zeitlinger** 04:31 Yeah, I think that's a fair assumption.
**Trask Stalnaker** 04:34 Okay.
**GZ Gregor Zeitlinger** 04:52 I'm wondering, though, before we go to the next issue, Drask, if we should try to single out if there's anything interesting for Jack.
And do that first, otherwise… We'll add them to…
**Jack Berg** 05:06 Don't do anything on my account, like, seriously, I'm gonna be here the whole time. If there's topics you think are particularly going to intersect with me, that's great. If they're gonna be focused on instrumentation, then I'll do PR review over in the core repo during this time, until it's relevant to me.
**Trask Stalnaker** 05:22 We'll say your… we'll say your name.
**Jack Berg** 05:24 I'll be listening, don't worry.
**Trask Stalnaker** 05:57 Okay, and we aren't removing the deprecated methods, because those are still used in non-declarative config.
**GZ Gregor Zeitlinger** 06:07 Right.
**Trask Stalnaker** 06:09 Alright, awesome. I will… oh, just… we might be able to just review it quickly, because it's… Just removing code, love that, love just, Declare it.
Yeah… All right.
**GZ Gregor Zeitlinger** 06:40 We still have to decide what to do about the bridge itself, but I think that's, like, a next step.
**Trask Stalnaker** 06:46 Cool.
Where… I know you asked me to look at this again, what was… Why am I… Holding on this… Add thread details…
**GZ Gregor Zeitlinger** 07:15 There's no open comments, I could only guess.
Maybe it's because of the location. Since we have moved some things to distribution.
This is some, is another candidate where… We could consider doing the same.
**Trask Stalnaker** 07:42 Yeah, I think that was…
**GZ Gregor Zeitlinger** 07:46 You can, go to the linked issue, because I have a summary of the current state of affairs there.
Yeah, that… No, no, no, in the description itself.
**Trask Stalnaker** 08:04 Oh, okay.
**GZ Gregor Zeitlinger** 08:08 Is it not here?
Let's see… And it's not, okay.
I thought it was here.
Let me look it up.
Oh, it's in their PR description. This, this?
Yeah, right, okay, then it's there.
Yeah, so in the old one, we started out with Java Agent, and then we settled on Common, But with your recent, comments about, enabled instrumentations, we could also say that Spring Starter and Agent have their own, place, each in the distribution.
Do you know what I mean?
**Trask Stalnaker** 09:05 Yeah, yeah, yeah, that's the direction I'm… Leaning… But I want to talk through it. So… the… Yeah, it feels like something… at least from an implementation perspective, it's like something the distro is adding support for.
The common… I guess the benefit of it being in Oh, yeah.
things under common Feel like things that… each… Instrumentation… is responsible for… is that true? I mean, we have a.
**GZ Gregor Zeitlinger** 09:57 Yeah, yeah, that's true, yeah.
And this is not the case here, so you're right.
for consistency reason, distribution, Java agent, thread details enabled, What actually makes sense, yeah.
**Trask Stalnaker** 10:16 Okay.
Let's… let's do that. I think that's at least, like, safer. We can always… If we… Yeah, I think that's a… safer… path. Do you want me to leave a comment? You…
**GZ Gregor Zeitlinger** 10:36 Yep, otherwise you're talking about the next PR, and then I'm losing.
**Trask Stalnaker** 10:40 Yes, yes, yes.
**GZ Gregor Zeitlinger** 11:21 Yep, perfect.
**Trask Stalnaker** 11:33 Alright, I gotta leave this one, this is a toughie.
I don't… I don't disagree with it, though, like, on the premise. Thanks for… I know we went back and forth on that.
The implementation's just tricky. Let's see, what do we got here? Config property util cleanup… Oh, yes, yes, yes.
Okay, so you tried… Some of this out.
**GZ Gregor Zeitlinger** 12:09 Yeah, I made the scope as small as possible, as, You, expressed, and now it's in the… Java agent tooling, and the only two exceptions are, the debug setting, which is also read an API, which you could say is, is cold smell, but at least, I… I reduced it to being package protected, so that it cannot be accessed outside, and it's in this debug util, and then the semconf Setting.
**Trask Stalnaker** 12:45 this… Sorry, just trying to page back into my…
**GZ Gregor Zeitlinger** 13:11 You can also ask questions.
**Trask Stalnaker** 13:14 Yeah… So… okay, so… We'd… Are renaming this… Because we are… going to… do we… instead of renaming it.
Can we just keep it with the same name and mark it deprecated now?
**GZ Gregor Zeitlinger** 13:41 No. We still have it, as you can see on the left side in, the… java Agent Bootstrap.
I mean, we could, but then we have… would have two classes with the same name, which can be confusing.
**Trask Stalnaker** 13:58 We've done worse.
**GZ Gregor Zeitlinger** 14:01 I always find that confusing when we have a bigger repository.
**Trask Stalnaker** 14:06 Yeah.
We could come up with a new name for…
**GZ Gregor Zeitlinger** 14:17 I'm not going to argue over the name, so I'm happy to just rename it.
**Trask Stalnaker** 14:24 Yeah.
What could we call it? So this one is… In Java Agent Bootstrap, it is only used for… Get Boolean… Just looking for its usages…
**GZ Gregor Zeitlinger** 14:57 Yeah, you also see the removed usages, it's.
**Trask Stalnaker** 15:00 Yeah.
**GZ Gregor Zeitlinger** 15:02 That can… I think in the usage, comment.
That I put there, there you can see it clearly.
**Trask Stalnaker** 15:17 Okay, so it's… Used by this guy and this guy. Oh, and maybe…
**GZ Gregor Zeitlinger** 15:23 Where I, I, I made it, and hard-coded. So this is not using the class anymore, those three.
**Trask Stalnaker** 15:32 Okay, that's using… Oh, debug util… oh, this is a new…
**GZ Gregor Zeitlinger** 15:37 new class, okay. That's one.
**Trask Stalnaker** 15:48 Right, right, okay, some conf stability, get string? That's a little odd.
**GZ Gregor Zeitlinger** 15:57 Yeah… I could have created yet another, ability to have this, but then we would have potentially 3 that are called the same, but, One way or the other. It's just this package-protected usage.
**Trask Stalnaker** 16:14 Usages. So, okay, so that's… Supportability metric… oh, that's the debug, right. Okay, and context propagation, this is also the same, it's using that… now it's using that debug…
**GZ Gregor Zeitlinger** 16:30 Right.
**Trask Stalnaker** 16:33 Okay, it's reading… this directly…
**GZ Gregor Zeitlinger** 16:41 Yeah, this is for all test settings, because there's no need to support environment variables.
**Trask Stalnaker** 16:47 Oh, yes, sorry, I missed that, yeah. And… this one… Got it, there, okay.
Let's a bank… Okay, so the… Where was I going with that?
Okay, and then… config… the new config properties util, I think that's what I was trying to find. Where… where is the new config properties util?
used from…
**GZ Gregor Zeitlinger** 17:38 This is from Java Agent Tooling and Bootstrap, because it's moved there, it cannot be used anywhere else.
**Trask Stalnaker** 17:49 Oh, I see. Okay, so… config file… And… early init config. So just these two places.
**GZ Gregor Zeitlinger** 18:04 It's also used by the early INIT.
**Trask Stalnaker** 18:09 Right, config file, so here…
**GZ Gregor Zeitlinger** 18:25 Can you tell me what you're trying to find out, or what you would.
**Trask Stalnaker** 18:31 Yeah.
**GZ Gregor Zeitlinger** 18:31 like to improve?
**Trask Stalnaker** 18:33 Yeah, so, if we're only… I'm wondering if we need it to be a generalized class?
even over in Java Agent Tooling, if it's only used very limitedly?
To free up bot.
Name.
Okay, for… let's… I think, I think I would prefer to keep the name, and… Deprecate it here, even though that creates two…
**GZ Gregor Zeitlinger** 19:22 the same.
**Trask Stalnaker** 19:22 name. I'll think on… I can think on if the other usages are needed.
Or any way to improve that.
**GZ Gregor Zeitlinger** 19:34 I also have opened it in my IDE now, so I can, walk you through the usages.
The first one is an agent class loader, which is for experimental initializer jar.
Second one is, in… Agent Initializer… And it's used for Experimental Security Manager support enabled.
Then we have it for the configuration file property, this is the third.
And the remaining are from… Early agent init config.
**Trask Stalnaker** 20:22 Okay. Yeah, let's just, let's just keep the name here and mark it deprecated, and we'll have one deprecated… I mean, we will have two with the same name, but one will be deprecated and one won't be deprecated.
**GZ Gregor Zeitlinger** 20:36 I think.
**Trask Stalnaker** 20:37 is reasonable.
Other than that, yeah, I think it's… Looking good, I… This is… .
**GZ Gregor Zeitlinger** 20:57 I could, I could, change it in a way that it does not offer the generic get boolean and getString.
But just have accessors for all the usages that we actually need.
**Trask Stalnaker** 21:14 the non-deprecated… the one in the Java agent tooling?
**GZ Gregor Zeitlinger** 21:18 Correct.
Yeah, I think I could move it to, to early initiate config.
Yeah, I think that… that would work.
And then it would be… Yeah, it would be part of early initiate config.
**Trask Stalnaker** 21:52 Okay, which makes sense, because configuration file, we are reading it early.
**GZ Gregor Zeitlinger** 22:00 We do.
**Trask Stalnaker** 22:02 Yeah, I think I like that, I like that, because that's kind of the whole… The… the only prop… the only properties we need to read Are the ones that we can't get through the declarative config that we're reading too early.
Yeah, I also, like, I just hadn't thought of that…
**GZ Gregor Zeitlinger** 22:21 Before.
**Trask Stalnaker** 22:27 I'll leave a comment.
**GZ Gregor Zeitlinger** 22:29 Nope, thanks.
And then we only have one class with that name. Yay! Probably.
**Trask Stalnaker** 22:42 solved.
Oh, yes, yes, the last thing I wanted to, I don't really care, since it's… Package protected here anyways.
**GZ Gregor Zeitlinger** 23:41 You want to have it in a different class.
Or you want to have it… was, hard-coded translation.
**Trask Stalnaker** 23:57 like I said, I don't really care because it's package protected, so I'm not gonna… you're welcome to rearrange it if you want. I'm not… I don't care enough to think… on it, though. Yeah, yeah, because it's packaged.
in… protected, we can… yeah, yeah.
Good.
Alright, great. Moving on… Declarative config for log back appender.
**GZ Gregor Zeitlinger** 24:39 This is getting into spring territory. Are you ready for that?
**Trask Stalnaker** 24:42 Yeah, let's do it.
Okay, so… We're removing… Okay, that just because it's not used anymore… Translate… Okay, we're removing that…
**GZ Gregor Zeitlinger** 25:06 It has been inlined, because it was the only usage.
**Trask Stalnaker** 25:09 Okay.
So… This looks super straightforward. Is there anything… worth calling out. It's still gonna support the… Oh, I think maybe my… Question is… Is this stuff happening too early?
**GZ Gregor Zeitlinger** 25:46 Yes, that is the issue.
**Trask Stalnaker** 25:48 Oh, it's getting it from the… okay, so it's not declared config, it's the… prepared event…
**GZ Gregor Zeitlinger** 25:56 Yeah, well, it's both. In the spring setup, you are also reading declarative configuration from the same place, just with a different path.
Because the declarative configuration is part of the YAML file of Spring, it just has a separate node called OTel, where it's reading everything from…
**Trask Stalnaker** 26:26 I see, and in OpenTelemetry Appender… Oh, I see, we're… oh, we're instantiating that… And it's… We don't have a OpenTelemetry instance yet.
**GZ Gregor Zeitlinger** 26:43 Right.
**Trask Stalnaker** 26:44 And we add the OpenTelemetry instance later.
**GZ Gregor Zeitlinger** 26:49 Right, we want to buffer all the log events from start.
**Trask Stalnaker** 26:54 Okay.
And… can we… Grab the configuration properties at that point.
**GZ Gregor Zeitlinger** 27:05 John tried to do that, and he was not successful.
I have not tried it out myself, but he explained to me that the order, is such that the beans have not been created.
And we rely on, the bean, beans being there,
**Trask Stalnaker** 27:26 to wire, up our hotel instance.
Oh, no, what I meant was, can we set… can we configure the OpenTelemetry appender Can we delay the configuration of the OpenTelemetry appender until the OpenTelemetry instance is set?
**GZ Gregor Zeitlinger** 27:48 then we would lose the log events from startup. This is what we are trying to avoid.
**Trask Stalnaker** 27:55 But we're caching those… We just wouldn't be applying the configuration to those… initial… cached logs. We'd have to kind of, like, retroactively, like.
Feed those back through our new configuration settings.
**GZ Gregor Zeitlinger** 28:17 Okay, I have not looked into that. I thought this was simply impossible.
**Trask Stalnaker** 28:23 It might be. I mean, it might not be worth it.
in the… in the light, although, I mean, it's worth looking at for the library.
instrumentation.
For Spring Boot Starter, do I understand correctly that You don't really have that problem because you can get declarative configuration Early via this?
**GZ Gregor Zeitlinger** 28:52 You're right, yeah. You get it via the environment object, you just have to know what the path is.
That's why we have this translate method.
**Trask Stalnaker** 29:02 Right, so we can't use the declarative config API okay.
**GZ Gregor Zeitlinger** 29:08 Right.
**Trask Stalnaker** 29:08 I understand.
And for the… for library instrumentation.
So we do have this… the same problem for library instrumentation exists, right? Like, we… Let me look at our…
**GZ Gregor Zeitlinger** 29:46 I mean, related to lockpack?
**Trask Stalnaker** 29:48 Yeah… And declarative configuration.
**GZ Gregor Zeitlinger** 30:05 I guess you would have the same problem, yeah.
**Trask Stalnaker** 30:10 Oh, I'm looking at the wrong one… Pender… So you do that, and then… Find… log back, yeah… Okay.
So… Let's… let's at least look, look at what that would take.
to… Handle the configuration.
lazily, when the OpenTelemetry instance is set.
**GZ Gregor Zeitlinger** 31:02 I mean, John already looked at this for quite a long time.
This is not a new problem with declarative configuration.
**Trask Stalnaker** 31:10 No, no. What I mean is, Setting the configuration up.
Right now, we… Set the configuration… When we instantiate the OpenTelemetry offender.
I assume… let's see. Well, let's look.
**GZ Gregor Zeitlinger** 31:39 Right, but, We could also have done it lazily without declarative configuration. I'm trying to say that this is… unrelated to change.
**Trask Stalnaker** 31:52 No, no, but there was no benefit to delaying it before.
Because system properties were available from the get-go.
**GZ Gregor Zeitlinger** 32:05 No, it already required special handling before.
**Trask Stalnaker** 32:09 for configuration.
**GZ Gregor Zeitlinger** 32:10 Yeah.
**Trask Stalnaker** 32:17 Let's see, how do we… Oh, library instrumentation doesn't support… System properties. That's… Nothing… Oh, library instrumentation… okay. I think, library instrumentation doesn't have this problem, because you set the configuration inside of the XML.
**GZ Gregor Zeitlinger** 32:58 Oh, yeah. It's more, like… Because we cannot do it better. Not because we particularly like it, I… So, assume.
It's…
**Trask Stalnaker** 33:13 I mean, it's kind of conventional.
**GZ Gregor Zeitlinger** 33:14 Either way.
**Trask Stalnaker** 33:16 Yeah, I think it's pretty conventional for… appenders… To be configured in… Here… Yeah, you have two conventions fighting, so…
**GZ Gregor Zeitlinger** 33:32 Want us to win.
**Trask Stalnaker** 33:34 Yeah.
Okay, okay, so… That's why we don't, so we don't necessarily have a problem with library instrumentation.
We have a documentation problem.
Maybe.
But right now, Library instrumentation doesn't support properties anyway, it's just… so I think we're… we're safe on the library instrumentation front.
And so spring… So, in spring, the problem is that we're doing… we're adding it for the user. We're not telling the user to add it to their XML here.
**GZ Gregor Zeitlinger** 34:17 Right.
It's like the Spring Boot, out-of-the-box-it-works experience.
**Trask Stalnaker** 34:23 I see.
Now… okay, okay.
And… if… I see, and we want to be able to control that.
automatic appender via declarative config.
In the same way that we… the Java agent work.
**GZ Gregor Zeitlinger** 34:50 Yep.
**Trask Stalnaker** 34:53 Okay.
Okay, okay.
And so this is just kind of… So we're bypassing… the… our declarative config API Do we lose anything by bypassing our declarative config API?
**GZ Gregor Zeitlinger** 35:14 Nothing I'm aware of.
the, processing and environment variable substitution should also work.
**Trask Stalnaker** 35:28 Okay.
Okay.
I think I'm sold. I'm gonna leave… I do think a… common… Okay, yes.
Is declarative config… Oh, haha, right, because we don't know, because we're reading so early, also. Okay, yes, yes.
**GZ Gregor Zeitlinger** 36:37 Hmm.
**Trask Stalnaker** 36:40 how we're doing… That translation… I would su… Just, can we move this… to early config… Mostly to centralize… So it don't… Forget about the slash development.
**GZ Gregor Zeitlinger** 37:25 Oh, I actually moved it from there.
Because it was only used there, but yeah, can move it back.
**Trask Stalnaker** 37:31 Oh, I see, right, right, right. Translate property name… okay.
And is this a case where… I mean, if it's actually…
**GZ Gregor Zeitlinger** 37:52 Has the… the slash development?
Documentation always has development in it.
**Trask Stalnaker** 38:02 Well, for now.
**GZ Gregor Zeitlinger** 38:06 Okay, hmm.
**Trask Stalnaker** 38:13 But I do… I do also like the idea of it being here, since it is very… like, we don't really want to use this general thing elsewhere. This is a very special case for LogBack.
**GZ Gregor Zeitlinger** 38:30 Pride.
**Trask Stalnaker** 38:32 I think that's okay, we're gonna, Our tests would catch this anyways.
once we… change.
**GZ Gregor Zeitlinger** 38:44 Truck yeah.
**Trask Stalnaker** 38:45 the YAML… Okay, yeah, I like it. Thank you.
Alright, distribution nude… Oh, we are coming up, Let's look at anything in the SDK repo.
**Jack Berg** 39:30 I'm looking at this PR right now.
7991, I like the direction of it. It's trying to align the extended open telemetry SDK pattern with what we've done elsewhere in the repo, where we have, like, extended tracer, extended meter, extended logger, and we have sort of common patterns for how those are organized and how they're initialized.
And, this is going towards that. I think there's just, like, a few things missing.
And I've been… I'm gonna… I'm gonna push a commit up to my own fork that kind of, I think, like, illustrates what it would take to kind of go all the way in this direction. And… it's… Like, what are the interesting bits about it?
I think the most interesting thing is, like, SDK config provider.
Right now, that lives in the, SDK extensions module, next to the rest of declarative configuration stuff, and that's… that kind of makes the pattern weird, because, the, how do I put this?
**GZ Gregor Zeitlinger** 40:55 Makes it look like this was only for declarative configuration.
**Jack Berg** 41:00 Right, right. We need to, like, and this has been on, like, my list for a long time, which is, like, find the final home for declarative config in the related utils. Like, you know, SDK config provider.
is related to declarative config, but, you know, as we've been discussing, like, should you be able to use it outside of declarative config? And, like, if yes or no on that, like, what… where does the final home where's the final home for that from, like, a module standpoint? And, like, what I'm doing on this branch that I'm working on locally is I'm sketching out what it looks like for now to put SDK config provider in the OpenTelemetry SDK module, in the same module that has OpenTelemetry SDK and OpenTelemetry SDK Builder.
And…
**GZ Gregor Zeitlinger** 41:54 violate that, you should not have, incubating stuff in stable modules.
**Jack Berg** 42:02 We do that all the time. We have, we put incubating stuff in stable modules. We just make sure that it is packaged in a way where, like, none of the incubating stuff is used unless you explicitly add an incubator module to your class path. And so, like, the gate for using SDK config provider has to be that, like, you have OpenTelemetry API incubator on your class path.
**GZ Gregor Zeitlinger** 42:34 I thought it would violate some other rule that, like, if you update your incubating, module that you cannot break, something, but I'm… I'm not sure what it was.
**Jack Berg** 42:52 Yeah, it's… it's pretty tricky and nuanced, and, like, I thought about, like, writing a comment describing what I was thinking, but, like, honestly, code is gonna be the best way to describe this. It's just one of those things, you just kind of have to see the arrangement.
And, yeah, I guess, like, I'll leave a comment with this commit and try to contextualize it a little bit, and we can talk about whether we want to, like, include that in this PR or… or pass on it.
But yeah, I'm aligned with this. I would characterize this as just trying to make extended open telemetry and Extended OpenTelemetry SDK aligned with our existing patterns for, you know, for, you know, extended tracer, extended log record builder, extended logger, etc.
I like it.
**Trask Stalnaker** 43:46 Cool.
So, let's… maybe one… maybe we have time for one more, and a break before the next meeting.
Let's see… It's a big one, so maybe not.
**GZ Gregor Zeitlinger** 44:02 You've already reviewed most of it.
**Trask Stalnaker** 44:05 Okay.
is distribution node…
**GZ Gregor Zeitlinger** 44:16 You can select the recent… Commit, maybe, that addressed Your last comment?
**Trask Stalnaker** 44:29 This one? What's this note?
Strongly… I don't remember what my comment was, sorry.
Generic access… oh, yes, yes.
Yes, I remember this now. Yeah, okay, so the YAML…
**GZ Gregor Zeitlinger** 44:48 Right, yeah, that was it. I also had to think about it.
**Trask Stalnaker** 44:52 So, you're not using the YAML… parsing… Anymore.
**GZ Gregor Zeitlinger** 45:02 Oh, right, and that means I'm marshalling to this custom DTO directly, but it comes at the cost that I now have to duplicate some logic when reading from config properties.
**Trask Stalnaker** 45:24 Okay, let's… Out.
the commit. So, it was… This is the one strongly typed.
Okay, so Agent Distribution Config, this is the… Strongly typed guy, and then let's look at where you're marshalling… Or rather, unmarshly distributed.
**GZ Gregor Zeitlinger** 46:02 Convert value, that's the line 40.
**Trask Stalnaker** 46:05 Okay… oh, okay, you're still using Jackson… Hmm…
**GZ Gregor Zeitlinger** 46:11 Right. That's the designated way.
And now you can ask Jack why this is the designated way.
If that was your question.
**Trask Stalnaker** 46:24 Yeah… so, Jack, we're trying to implement that ID, how to access distro.
configuration properties in the Java agent.
**Jack Berg** 46:40 Yep.
**Trask Stalnaker** 46:42 So what Gregor has done here is added a, declarative configuration customizer provider to capture the… the distribution node.
**Jack Berg** 46:58 Duh?
**Trask Stalnaker** 47:00 And then… Reading from… so we're… Then we're reading the distribution property model.
from that, from the Java agent.
And then… Is your thought… I haven't even looked at the API for this this guy.
is… this sort of the natural thing to do, use Jackson to bind it to our DTO.
Use this… API directly.
**Jack Berg** 47:42 So, distribution property model… is a, is like a pojo.
you know, a Jackson-style pojo with, like, getters and setters for all the properties.
And then… Let's see… Distribution.
**Trask Stalnaker** 48:01 I'll pull it up.
**Jack Berg** 48:03 You can't pull it up, it's generated.
Yeah, you'd have to…
**GZ Gregor Zeitlinger** 48:07 I only look at, at the, schema.
**Jack Berg** 48:15 I can… I can pull it up, I guess, because I have, I have the code checked out, so I can look at the generated source.
Sure.
But it's, like, kind of annoying, because it's like, I want to see some of the stuff that's on your screen.
Oh, I… I'll see some of the stuff on my screen.
**Trask Stalnaker** 48:33 This is… this is good.
**Jack Berg** 48:36 Okay, so…
**GZ Gregor Zeitlinger** 48:37 Let's have it open.
**Jack Berg** 48:40 Okay, we'll see, like, so we have these, these, this is, generated from the schema.
from the JSON schema, and every type in the JSON schema has a corresponding model class like this, and if I go to the, you know, we can see all of them. This is in a generated directory in the build, and, you know, just… these are all the types that appear in the declarative config JSON schema, right?
And so, these, these have, like, Sorry, go ahead.
**Trask Stalnaker** 49:12 Question, for the other ones, like the B3 propagator model, do you use Jackson to bind those to the SDK?
**Jack Berg** 49:23 to bind those to the SDK. I don't know what you mean by that.
**Trask Stalnaker** 49:27 How do you read from B3 propagator model?
**Jack Berg** 49:32 Yeah, so, So we… so we have… we have a YAML file, we read it in as a byte stream.
And then we bind it to one of these guys, one of these models, and so we use Jackson to do that.
And so, like, the top-level route is, you know, OpenTelemetry configuration model. So we say, like, hey, give me the bytes for the YAML, and bind it to this OpenTelemetry configuration model, and then it's like turtles all the way down, right? Because this references a bunch of these other model classes.
And so at that point, you have an instance of this OpenTelemetry configuration model, which, like, matches the schema. And we walk through this model and, you know, and look at each of the properties of this and return the corresponding SDK components.
**Trask Stalnaker** 50:18 And so the SDK, right, and the SDK is… has an explicit schema in… Configuration… declared a config, so you have… that's why you are able to read directly from there.
Right. And so, distribution model… yeah, what… what would be your recommendation for how to read from distribution model.
**Jack Berg** 50:43 So now that we have that shared context, can you share your screen again?
**Trask Stalnaker** 50:46 Yeah.
**Jack Berg** 50:55 Okay, so, okay, so you have, distribution property model, and at that case, that's, like, that's essentially just, like, a map, right? Because there's no…
**Trask Stalnaker** 51:08 Yeah.
**Jack Berg** 51:09 There's no schema to it, so the only… it has just, like, additional properties, and every additional property is a key-value pair of the map.
Yeah, and so, like, you're trying to bind that map to something that has a schema again, right? So, agent distribution config has a schema.
Right. And so, you know, I think… Like, there's the… You can, of course, take distribution property model, which is essentially a map, and convert it to declarative config properties, which is, like, our programmatic, generic representation of a YAML node.
But it doesn't really do anything different. It's like, in both cases, they're map-ish, right?
They're map-ish type things, and, like, no matter what, you have to take a map-ish type thing and bind it to another POJO, which has a schema, and that's your agent distribution config in this case. And so I, like, unless you know of a way to bind a map-ish thing to a POJO that isn't Jackson, like, I think, you know, you're stuck using Jackson.
**Trask Stalnaker** 52:13 Cool.
That seems very reasonable.
Alright, I like it, Gregor.
Just wanted to… Jack's blessing. Thank you, Jack. I mean, do you guys.
**Jack Berg** 52:29 like, can we build a schema binding thing in-house? Like, can we get rid of… like, I would love to not have to have a dependency on Jackson, but, like, I don't see a way, short of reinventing the world, the wheel.
**Trask Stalnaker** 52:44 Yeah.
Yeah.
**GZ Gregor Zeitlinger** 52:46 I have discussed with Jay how we could have only one use of Jackson and not repeat it by building a specific schema for the Java agent that would have also all of our settings, and then we would have everything strongly tied, but seems like this would be a separate step. But, we're already thinking about that.
**Jack Berg** 53:10 Yeah, okay, so still use Jackson, but use it in one place, and have just, like, you know, one big bound, strongly typed schema.
**Trask Stalnaker** 53:19 Cool. Well, let's get a break before the next meeting.
and Gregor, I will look at… so, for this one, next up is for me to give it a closer look, but, the direction is looking good.
**GZ Gregor Zeitlinger** 53:35 Alright.
See you in a few!
**Jack Berg** 53:38 Thanks for having me, guys.
**Trask Stalnaker** 53:39 Hey, thanks for joining.
