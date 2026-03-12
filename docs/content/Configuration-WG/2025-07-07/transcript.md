SIG: Configuration WG
Date: 2025-07-07
Duration: 13 minutes
Zoom Recording URL: https://zoom.us/rec/share/RzzeUOBy851WjMn_hbrPAcmpA5Omy4ehgK8NcYgoXwShh6Ovx-pODL55oG6jyaN_.7DMe9Cn6J-KwNOtx
============================================================

## Zoom Recording Transcript

**GZ Gregor Zeitlinger** 00:31 Hello!
**Tyler Yahn** 00:37 Hey, Gregor, how are you?
**GZ Gregor Zeitlinger** 00:43 Good.
**Tyler Yahn** 00:47 Nice.
**GZ Gregor Zeitlinger** 00:54 I'm actually just working on declarative configuration in Java agent.
**Tyler Yahn** 01:02 Yeah, what are you working on.
**GZ Gregor Zeitlinger** 01:10 so many things I have to look in the Project board. I have one pull request for loading the declarative configuration early, so that you can disable the Java agent, and then I have pull request to support spring starter. Declarative declarative configuration.
**Tyler Yahn** 01:35 Hmm!
That's kind of cool.
**GZ Gregor Zeitlinger** 01:39 And that is a little bit complicated, because spring also has its own configuration system.
**Tyler Yahn** 01:51 Hmm, but it interprets our file format, though.
**GZ Gregor Zeitlinger** 01:59 I I embed the entire Json node in the spring starter, and then I'm reading it as Json, and then I serialize it to a string, and then I give it to the function that makes a declarative configuration model out of it.
**Tyler Yahn** 02:20 It's.
**GZ Gregor Zeitlinger** 02:21 Jumping through a couple of hoops. But the performance of reading a file is not so dramatic. So that's that's okay.
**Tyler Yahn** 02:31 Yeah, I gotcha. That makes sense.
**GZ Gregor Zeitlinger** 02:48 So do we have any?
No, we don't have any agenda. Jack is writing that he cannot attend.
**Tyler Yahn** 03:06 Yeah, I just saw that.
Well, yeah, I mean, I guess if we don't have an agenda and Jack's not here, I don't have everything to talk about. So I mean, I guess I can give a status update that like we're still looking at trying to evaluate the stabilization in the Go Sig. Through our implementation. But we haven't started on that. It's all on me. It's a blocked in my queue of things to do so.
Yeah. Still still more to come on that.
**GZ Gregor Zeitlinger** 03:33 Are you?
Do you have the same configuration file format that Jack created for a Java.
**Tyler Yahn** 03:45 Well, yeah, I mean, it's shared across all languages that's kinda its whole purpose. And so it's just more about looking at our implementation that interprets it and making sure that we're complying with what we're trying to stabilize in the specification.
**GZ Gregor Zeitlinger** 04:00 All right. I'm asking, because I want to add a new field that actually created a ticket for the Java Repository. But maybe this is also for the specification. So in Http, I want to add a known methods because it sounds like this is something cross. Language.
**Tyler Yahn** 04:25 What are known methods? Are they like paths.
**GZ Gregor Zeitlinger** 04:29 And stuff like that.
put get delete. And and the reason is that anything that is not in the list will be other to keep metrics. Cardinality constrained.
**Tyler Yahn** 04:47 I thought that was defined in the semantic conventions, though.
**GZ Gregor Zeitlinger** 04:53 Yep, that is, that is another angle of it. But you still need to have a field in.
and the general section of the instrumentation section of the Declarative Configuration, at least in Java. They are strictly type, and you cannot add anything to it unless you make a pull request to the SDK.
I don't know if that's also the way that you're doing it in goal.
**Tyler Yahn** 05:28 No, I in the semantic conventions, right like they state what is allowed and what isn't allowed.
and we just comply with what that is. It's not configurable.
**GZ Gregor Zeitlinger** 05:42 Well, what I mean is It will raise an exception when I load the file.
When I have known methods in the general section alright.
where you can see the where you can see everything like this is the kitchen sink. Example? Oh, it's actually in the configuration repository. So here you have, General, and then Http, and currently there is client and server and Java implementation will bail out if you put anything else in there. So it's like, not deferred to semantic conventions, because it is strictly checked before.
**Tyler Yahn** 06:26 Huh, okay, I think there's maybe 2 things there. So I think that the known methods thing is a specific. But what you're talking about is just adding something else to this configuration file causes an exception to be thrown.
**GZ Gregor Zeitlinger** 06:39 Exactly And I think Jack's idea was to keep this section in general clean, because it's cross language and requires more coordination than just having this up for the maintainers of Java or Python.
**Tyler Yahn** 07:00 That makes sense. Yep.
**tristan** 07:03 Right. Aren't you supposed to put something like that under the Java Key sub subsection? There.
**GZ Gregor Zeitlinger** 07:13 It is possible. It basically depends on whether we deem known methods to be a Java thing or a cross language thing. And it was thing. I'm proposing it to be cross language, and therefore, actually, it doesn't make sense that I put it in the Java Repository.
It should probably be 1st in the Configuration Repository and then in the Java Repository.
**tristan** 07:40 I meant that when it's not already in the Configuration repository, it has to go there. Otherwise it should cause an exception, because it yeah, goes outside the schema. And so you have to go through.
**GZ Gregor Zeitlinger** 07:53 So the 1st one configuration repository. I think that's a no-brainer. But if it should cause an exception, this is more like an architectural.
a decision.
He wants to have a new release of Java SDK, so that you can do this, or whether you say this is governed by the semantic conventions.
**tristan** 08:15 Gotcha.
**Tyler Yahn** 08:22 Yeah, I mean, I I don't think it's gonna be need to be going. The the general I know and go. We would not be using this.
So I think that this might just be a Java specific thing.
**GZ Gregor Zeitlinger** 08:37 You mean you would not use the general section.
**Tyler Yahn** 08:41 No, we'll use the general section. But this known methods thing is not something that we will be using.
**GZ Gregor Zeitlinger** 08:47 Oh, okay, simply because you don't have it or no sorry. What I mean is from my understanding. It would make sense to have it there. But maybe you have not implemented the feature that limits cardinality based on known methods.
**Tyler Yahn** 09:05 No, no, we have. I'm just saying that the the set of known methods is defined in the semantic conventions, and that's where we get that from. It's not user configurable.
**GZ Gregor Zeitlinger** 09:16 Right, and if it would be user configurable, it should probably be drawn from the general section.
**Tyler Yahn** 09:23 Right? Yeah.
I think that it may be specific to the Http instrumentation, though. So I might even say that it needs to be in that.
But I again like the configuration, doesn't seem like something we would implement. So I'm not exactly sure like, unless the semantic conventions comes across and says that like this should be user configurable.
I don't think we're planning on addressing that.
**tristan** 09:52 Well, I was actually curious if it doesn't, because it would be useful. If you have verbs outside of the common set and not have it be other if you define that you want it to not be other. So I'm surprised the semantic conventions don't say that like make it configurable.
So.
**GZ Gregor Zeitlinger** 10:12 Where would this actually be defined? Would the Semantic Convention say you should configure this? Or would the like configuration specification say that you should be able to configure this.
**Tyler Yahn** 10:30 Well, I mean, I think you can put it in the configuration. I think that they're separate, but it doesn't make much sense. If expensive conventions are saying that you shouldn't configure it. It should just be a static set of values.
**GZ Gregor Zeitlinger** 10:46 I guess what I'm asking is.
**Tyler Yahn** 10:50 Yeah. So it seems like the semantic convention says that, like the only methods that should be allowed are from Rfc. 9, 1, 1, 10 or 9, 1 0, and the patch method as well, otherwise it it should be other.
**GZ Gregor Zeitlinger** 11:09 So are you saying that this is actually a Java specific feature, because the semantic conventions don't say that it's configurable.
**Tyler Yahn** 11:18 They specifically say it's not configurable that it shouldn't. It shouldn't extend beyond Rfc. 9, 1 1 0 or the patch method.
**GZ Gregor Zeitlinger** 11:31 Interesting.
**Tyler Yahn** 11:36 Although, let me, I'm I'm sorry. I'm still just reading the rest of this, making sure that makes sense. But I guess it does say that there is a way.
Provide an override list.
**GZ Gregor Zeitlinger** 11:58 Are you looking just at the semantic conventions.
**Tyler Yahn** 12:02 Yeah, I am sorry.
**GZ Gregor Zeitlinger** 12:04 Yeah.
**Tyler Yahn** 12:06 Yeah, it does look like there's a way, and it's it is defined for an environment variable. So I think you are right, then, if that's the case, it should also be defined in the configuration file.
**tristan** 12:19 On the partial.
**Tyler Yahn** 12:20 Which makes sense. Then, yeah.
**GZ Gregor Zeitlinger** 12:24 Is that here am I right here?
**Tyler Yahn** 12:27 Yeah, correct. Yeah.
**tristan** 12:30 Yeah, I thought it allowed you to set ones that you would accept so that you wouldn't have to just throw them away makes sense. And yeah, these things do to go in the semantic adventure.
They go in there first, st I mean.
**GZ Gregor Zeitlinger** 12:47 Okay? And so we should create a Pr here that it says.
either this environment variable or this part of the configuration file.
**Tyler Yahn** 13:02 Right? Yeah, that makes sense.
**GZ Gregor Zeitlinger** 13:05 Okay, yeah, yeah. I learned something great.
**Tyler Yahn** 13:17 Cool. I'm probably gonna jump.
What's? Oh, I see. Yeah, I'm probably gonna jump off at this point.
Given the lack of agenda. So yeah. Good seeing. Y'all.
Bye.
**GZ Gregor Zeitlinger** 13:30 All right. See you.
