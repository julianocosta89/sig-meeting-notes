SIG: Java Declarative Configuration
Date: 2025-09-18
Duration: 49 minutes
Zoom Recording URL: https://zoom.us/rec/share/oAoTY_uP3TSgb9VaAld_4ELxTdzMqQ4WPdO1CdCF4XXHnC5nULY_zRXfKSN3zUld.yJSKczg6yJU6pgEo
============================================================

## Zoom Recording Transcript

**GZ Gregor Zeitlinger** 00:00 Rep.
**Robert Niedziela** 00:11 Hi, girl, girl.
**GZ Gregor Zeitlinger** 00:13 Hello! Hello.
Robert, I've put your discussion point already on the Agenda.
**Robert Niedziela** 01:08 Oh, okay, about, duration, or something else?
**GZ Gregor Zeitlinger** 01:13 Exactly.
**Robert Niedziela** 01:14 Thought it would be easier for me.
**GZ Gregor Zeitlinger** 01:16 to understand Hi, Trask.
**Trask Stalnaker** 01:23 Beautiful.
**Robert Niedziela** 01:24 So…
**GZ Gregor Zeitlinger** 01:25 Before I forget, Jay reminded me that we should cancel next one, because we have a company meeting.
**Trask Stalnaker** 01:34 Oh, okay.
And we'll do that right now.
**GZ Gregor Zeitlinger** 01:38 Thanks.
Okay, two minutes in… I guess we can start.
Ross, do you wanna…
**Trask Stalnaker** 02:16 Yeah, yeah.
**GZ Gregor Zeitlinger** 02:16 fair.
**Trask Stalnaker** 02:18 Just a second… Alright, what we got here? Declarative config, alright.
**GZ Gregor Zeitlinger** 02:47 Yeah, first one is, just to let you know, because we, we're so fast that we already got the documentation, but I'm.
**Trask Stalnaker** 02:54 Merged! Alright!
**GZ Gregor Zeitlinger** 02:56 Yep.
Still looking for, feedback if I missed something.
**Trask Stalnaker** 03:03 I started… I started looking at it, the only feedback I had was mentioning, at the top that it's still experimental.
**GZ Gregor Zeitlinger** 03:16 That's a good one, yup,
**Trask Stalnaker** 03:18 Maybe… Kind of moving this, up to the top, saying this… Or… Or not, just like a call-out.
What is it?
**GZ Gregor Zeitlinger** 03:32 What is our, wording, actually, so not too, Make it more confusing. Experimental, unstable, alpha, what is it?
**Trask Stalnaker** 03:43 Hahaha eww… Not stable or experimental. I guess I, I would… Yeah.
I would go with experimental, I guess. What do we do? Do we do anywhere else? Let's see… What would… I know, let's search experimental…
**GZ Gregor Zeitlinger** 04:29 Yeah, experimented it.
is fine.
I'll just do that.
**Trask Stalnaker** 04:34 Yeah, yeah.
**GZ Gregor Zeitlinger** 04:35 On both pages, actually, we have the general one, and we have the Java one, I thought.
would make sense to start with a distinction instead of putting everything just on the Java page.
**Trask Stalnaker** 04:54 Oh, I didn't even catch that.
**Jay DeLuca** 05:01 If you click on SDK Config on the left?
There's a drop-down.
**Trask Stalnaker** 05:07 SDK…
**Jay DeLuca** 05:08 Yep, so I clicked that one.
**Trask Stalnaker** 05:10 Okay.
**Jay DeLuca** 05:11 And then open the top level one.
And then this is the third one down on the left, Kevian.
**Trask Stalnaker** 05:19 Oh, okay, okay, yeah, I hadn't even… I hadn't even seen this, okay.
So… We've got, Java Guinness, Started… Is this… So this is very Java-specific.
**GZ Gregor Zeitlinger** 05:36 Oh, yeah, that's a bug. Yeah, thanks for catching that.
**Trask Stalnaker** 05:43 Okay, and then for Java, I think it was under zero code?
**GZ Gregor Zeitlinger** 05:48 You have a link right there from the other page.
**Trask Stalnaker** 05:52 Of course.
Bye-bye.
Okay.
**GZ Gregor Zeitlinger** 06:04 And so I moved the Java option there, I just forgot to remove it from the other page.
**Trask Stalnaker** 06:09 Sure, sure.
That's very technical.
**GZ Gregor Zeitlinger** 06:25 It is, but I couldn't think of a way how to take that complexity away.
**Trask Stalnaker** 06:32 Yeah, I think it's fine for, and it's… Mmm, I think it's… fine for… a new experiment, like, this is new, like, people who are taking this probably are wondering, like, how do I migrate from one to another? How do I do all this?
at some point, We'll want to kind of revamp things to be maybe, like, declarative config first.
**GZ Gregor Zeitlinger** 07:07 Yeah, also.
**Trask Stalnaker** 07:08 Not now.
**GZ Gregor Zeitlinger** 07:09 Also, just, integrating things more instead of having it on a single page,
**Trask Stalnaker** 07:14 I've already discussed with Jay how we could.
**GZ Gregor Zeitlinger** 07:17 For example, make tabs, so that where you have environment variables, you have… could have 3 tabs. System properties and declarative configuration.
But, I'm not sure if this is the right time to do it, or if we want, wait a little bit until we have a little bit more user feedback, that's why it is currently just on this single page.
**Trask Stalnaker** 07:44 Yeah, no, I think this is a great starting place and, can progress whenever you're… feeling… like it.
**GZ Gregor Zeitlinger** 07:56 Yeah, so this is what I have planned for milestone 1. So this is the first one where we can Point users to, To actually try out the new features. Yeah.
Notice that our bestseller feature is not even included, this filtering of health checks. I just created a Puerto Request, and it's merged, but it's not in this PR, so we'll have to wait until the next one.
**Trask Stalnaker** 08:25 Yeah, yeah.
Yeah.
Cool.
Yeah, it was, that was a good idea to bring that in now.
Alright.
Onto… PRs… let's see…
**GZ Gregor Zeitlinger** 08:51 Yeah, this is, from Robert. We already discussed it, but.
**Robert Niedziela** 08:56 I…
**GZ Gregor Zeitlinger** 08:57 Still, I'm unable to, understand, What the scenario is where this problem occurs.
**Robert Niedziela** 09:09 Yeah, so, basically, if, in declarative config, if I specify, some property in Java instrumentation, node, with… And what does the.
**GZ Gregor Zeitlinger** 09:24 What's the user doing? This is my first question. In this… to have this problem, is the user using environment variables, or the declarative configuration?
**Robert Niedziela** 09:34 configuration.
**GZ Gregor Zeitlinger** 09:35 higher.
**Robert Niedziela** 09:36 Yes.
**GZ Gregor Zeitlinger** 09:37 Okay.
**Robert Niedziela** 09:39 So, yeah, specifying, something, some, property, as a time with time unit, right? And then trying to, call get duration on current implementation of declarative config bridge.
Causes, a parsing issue, and number for that exception, I guess.
**GZ Gregor Zeitlinger** 10:03 Can you make a concrete example what, what property it would be, and what the value would be in the declarative?
**Robert Niedziela** 10:10 Okay, let me share the screen, then.
**Trask Stalnaker** 10:15 Sure.
**Robert Niedziela** 10:23 So, for example, this one.
**GZ Gregor Zeitlinger** 10:26 Okay, so it's in the instrumentation section.
And this profiler, is this something.
**Robert Niedziela** 10:34 That's Planck-specific. Okay, it's our extension to… Okay.
Java agent.
**Trask Stalnaker** 10:42 I was trying to see… look in the configuration repo, Do… has the configuration… Defined unit support.
**Robert Niedziela** 10:56 So, as far as I remember, I can double-check it, but the interface for config properties says that.
That it should support.
**Trask Stalnaker** 11:08 Oh, yeah, but more… I'm kind of going back to what, a little bit… what should we be doing there from a declarative configuration perspective? I totally support… I think unit… time units are great. I would just want it to be defined by the.
configuration SIG, so that it's the same across languages.
**Robert Niedziela** 11:37 Yeah, so to be honest, I didn't check it.
**GZ Gregor Zeitlinger** 11:40 I've actually filed a bug report about this too, unrelated to what Robert was doing.
And the feedback was, that it is defined as integers, even though nobody is against, units, It seems to be a good idea, it's just not in the specification, and that's why the… SDK part, so everything that's not under instrumentation development does not support strings. So, for example, the exporter timeout.
It has to be an integer.
I'll also find the issue.
**Trask Stalnaker** 12:20 Fine… yeah, I'm looking for that.
**GZ Gregor Zeitlinger** 12:23 It is in our big, declarative config board.
Or it should be there.
Hmm. Okay.
**Trask Stalnaker** 12:53 I'm not finding anything in the config repo.
**GZ Gregor Zeitlinger** 12:59 No, then I… I probably failed to link it. I think it's… In the configuration repository.
Huh, so many repositories.
**Trask Stalnaker** 13:21 Yeah, I was expecting it to be in there also, but I'm just not finding… There's one called Document Time Value Unit.
**GZ Gregor Zeitlinger** 13:32 know where it is, we discussed it on Monday.
I just have to go to the meeting notes, then I can find it.
**Trask Stalnaker** 13:41 Cool.
**GZ Gregor Zeitlinger** 13:49 Yeah, there it is. I'll just put it in our doc.
Are we… The 27 is what we're discussing right now, isn't it?
**Trask Stalnaker** 14:05 Sorry, what?
**GZ Gregor Zeitlinger** 14:06 I put it in our meeting notes now.
**Trask Stalnaker** 14:09 Gotcha.
Configuration issue… Migration scheme… .
**GZ Gregor Zeitlinger** 14:20 Yeah. Did I share, or do you want to share again, trust?
**Trask Stalnaker** 14:24 Sure, sure.
**GZ Gregor Zeitlinger** 14:27 It was an either-or question.
**Trask Stalnaker** 14:29 Oh.
**GZ Gregor Zeitlinger** 14:30 Second off. Yeah.
**Trask Stalnaker** 14:39 So… Yes, good, okay.
I mean, I would… yeah, so I guess, did they… so you discussed this on Monday with the config folks, did they… Were they amenable to taking this in prior to stability?
Addressing this issue prior to stability?
**GZ Gregor Zeitlinger** 15:11 We did not discuss that. My question was whether this is a bug or not, and, The answer was no, it's not a bug, because it has never specified to be a string, so duration has never been specified to be a string. It seems that this was a Java extension.
**Trask Stalnaker** 15:34 Gotcha.
Okay.
**GZ Gregor Zeitlinger** 15:38 And that if we want to have continued to support, we would have to find a workaround in JavaSpace. I have not explored how we could do that.
Because I wasn't sure if it's really needed. I mean, from what I'm hearing from you, Robert, it's a convenience, because as soon as the user is translating their system property into a file, we could give them the guidance that they have to convert the value. So, it would technically not be breaking, we would just make the Instructions for the user, longer.
**Robert Niedziela** 16:21 Yes, however, still it is specified as a number of milliseconds.
And sometimes, some libraries or products, use higher resolution, like nanoseconds.
So, how it can be done then?
**GZ Gregor Zeitlinger** 16:42 You mean somebody is automatically creating this configuration file instead of writing it manually? I don't understand.
**Robert Niedziela** 16:49 No, I mean, if we are fixed to nanoseconds unit, I mean, milliseconds unit, right? Because that's how I understand. If we have no option to specify time unit, it is the number of milliseconds, right?
**Trask Stalnaker** 17:04 Is it an integer value?
In the configuration schema?
**GZ Gregor Zeitlinger** 17:12 I think so, yes.
**Robert Niedziela** 17:12 Yeah, probably, yes.
**Jay DeLuca** 17:18 Yeah, so you couldn't do, like, fractional…
**Robert Niedziela** 17:20 Oh, for… okay.
**Trask Stalnaker** 17:23 Wondering what… okay, no, like, it's delay is a integer, for example.
I mean, you could define it differently and do fractional.
Oh, okay, and so these are… I see, so these are in this JSON schema, they are defined as integers, so there's not really… a path forward.
Or… units.
**GZ Gregor Zeitlinger** 17:58 Only going through the spec, and then going all the… Way to have it amended in the spec, and then here.
**Trask Stalnaker** 18:07 But how would… I mean, it would need to… Wouldn't that be a breaking change, or…
**GZ Gregor Zeitlinger** 18:14 Yes.
**Trask Stalnaker** 18:14 out.
Okay.
So…
**GZ Gregor Zeitlinger** 18:31 Robert, I wanted to ask you about this nanosecond thing. Is this, a use case that you currently have, or was this more a general, thought?
**Robert Niedziela** 18:40 I've seen some time reported in milliseconds. When working on JMX stuff.
I'm not sure if Hadoop is not reporting in nanosecond something, or some other library.
You know, it's not just for configuration. I saw that sometimes it may be necessary to support more than just the nanoseconds. By the way, the default implementation of config properties It supports up to milliseconds, probably. I'm not sure about our code. I have seen somewhere a higher resolution, but I'm not sure where now, so I would have to dig.
Again, and find it.
**GZ Gregor Zeitlinger** 19:23 This use case would be, really good, because then we can take this as a starting point.
To change or have an exception to the specification.
I think all the use cases in the SDK don't require anything with a higher resolution.
**Trask Stalnaker** 19:44 Yeah, Dewey… Trying to decide if we need… guidance… I mean, what would be nice is… to have… Agreement in the… config… Repo that if you do want to, like, for custom, for instrumentation, Like… instrumentation properties.
If you do want to support units, these are the unit values. Oh, do we… that should just be, Wouldn't it be just the, our standard… Can we lean on this?
**GZ Gregor Zeitlinger** 20:36 we could all to have a full enumeration, I mean, it's not that many values that are relevant.
**Trask Stalnaker** 20:44 Right, do we like the… Seconds…
**Robert Niedziela** 20:57 And by the way, my PR actually supports both forms, so the first attempt to parse Value is to just parse the long value, and if it fails, it tries to split the string. If it string, it tries to split for number and unit.
And… If it's possible, it's converting to…
**GZ Gregor Zeitlinger** 21:25 So, as it stands right now, we have to decide if we want to support units in the instrumentation section. That's all we can decide here. We cannot decide about the SDK, because that is something that we would have to do at the specification level.
**Robert Niedziela** 21:44 Yeah, and this, the clarity properties config bridge is for custom instrumentation only, right?
However, it can be used also for others.
Yes, if necessary.
After your PR, right?
You did this builder.
It can be used also in other areas.
**GZ Gregor Zeitlinger** 22:10 It is also used, for contract extensions.
**Robert Niedziela** 22:14 Huh.
**GZ Gregor Zeitlinger** 22:16 I guess the question we have is, are we fine to tell users that units are available in the instrumentation section?
And also, in some parts of the SDK, so basically the parts that are untyped from the SDK point of view. So, like, you have a custom SPAN processor, and then in the SPAN processor, you have a unit, and then you can have sorry, you have a duration, and this can have a unit, but in the typed parts of the SDK, units are not allowed.
And… I think this could be confusing. That's why I'm hesitant.
**Robert Niedziela** 22:57 Yeah, I think it should be consistent here and there.
I agree.
**GZ Gregor Zeitlinger** 23:05 Our task is… Adding all the units.
**Trask Stalnaker** 23:12 So that's my only, I think that's a good point, though, Gregor, about If we support units in instrumentations, that might make it look like we support them in the SDK config, also.
**GZ Gregor Zeitlinger** 23:35 Additionally, we have the… We have this thing that in some parts of the SDK… Like, for a custom spend processor, you can have a… And this would be parsed according to our Java, and then it would even have Like, we have the baggage span processor, and that is, that is using the, declarative config bridge, and then this could We could add parsing durations there.
Yeah, but I al- I think it's too confusing.
**Jay DeLuca** 24:21 What if we used a different… Description, so, like, duration with unit.
Or something. It's not clean, but it might be a little bit more explicit that it's, like, a separate concern with a potentially different format from a duration used elsewhere.
**GZ Gregor Zeitlinger** 24:42 That's a cr- that's a… new angle, like, you could have… A composite type, and then you would have something like amount and unit, so you would not have this with unit suffix, but have it as a complex type.
**Jay DeLuca** 25:01 I don't know if that adds complexity around precedence, if, like, multiple are set, or whatever, but just a… just a thought to throw out there.
I don't know if we have any precedence for… Something similar.
**Trask Stalnaker** 25:20 I think… My preference would be… If we think that a particular property Is better described in terms of Seconds, or minutes, or hours, if we want that.
We could just… Perfect.
Like… duration… Min equals… And that's just the name of our property, and we just have to decide on a property-by-property basis.
But I think the… how bad is it, Robert? I mean, like, in the example you were showing, 15 seconds… I mean, it's… That one's not so bad, like, 15,000, it's still readable.
**Robert Niedziela** 26:27 Yeah, I didn't know that… well, this is against the specification, actually. I based on our old implementation we have.
**Trask Stalnaker** 26:37 It seems like an easy problem to solve at first, I agree.
**Robert Niedziela** 26:43 Yeah, if this is something that we agree not to change, then I will implement some recalculation on my side, so it should be okay.
**Trask Stalnaker** 26:55 Okay.
Yeah, I think it's… I think…
**Jay DeLuca** 26:59 It is interesting, though, that, like.
anything other than a millise… like, below a millisecond is unsupported, and I don't know if there are actual use cases, like, I don't… can't imagine someone would want a span exporter to… to be… Going into nanoseconds, but… Are there other settings that would make sense to have nanoseconds?
**Trask Stalnaker** 27:24 microseconds, potentially.
**Jay DeLuca** 27:26 Or microseconds?
**Trask Stalnaker** 27:28 Yeah.
I mean, I could see, like, a threshold, like, report my spans that take over 500 microseconds.
But in that case, I mean, we could either do threshold… Micros, if we… But that's… or we could just support… I would kind of assume we could just support… This doesn't seem too…
**Robert Niedziela** 28:03 Yeah, but then we have to change the schema, right? Because it's… currently, it's in.
**Trask Stalnaker** 28:07 Whoa.
Is, this would be in our instrumentation.
**Robert Niedziela** 28:13 We don't have a schema for the instrumentation. Okay.
**Trask Stalnaker** 28:17 properties.
**Robert Niedziela** 28:18 Yeah, that's right. For instrumentation, there's no scan.
**GZ Gregor Zeitlinger** 28:22 The declarative config bridge does not support, fractional numbers currently, but we could add that.
Or maybe we would just directly, access the YAML node, because, If it's a new thing, then we don't have to support it for environment variables.
**Trask Stalnaker** 28:43 Hmm, So, I think there's options when we… When we hit that, problem.
But hopefully we won't hit it for a while.
Actually, we could look. The one place where I could see it being useful is… in the… Stack trace, ground stack trace, let's see what they… Min duration defaults to 5 milliseconds.
Yeah, they also use… the MS… So, might be worth… calling that out. I think you have a… PR open right now.
This one… Might be worth calling that out here.
**GZ Gregor Zeitlinger** 29:57 Or recalling what out?
**Trask Stalnaker** 29:59 That the, right now, they are supporting Time unit.
**GZ Gregor Zeitlinger** 30:10 Oh, okay, yeah, right. Yeah.
**Trask Stalnaker** 30:13 And so we wouldn't support time unit here.
And it would be pinned to milliseconds, and it might be worth, I don't know if… It might be worth asking if… A… Have customers who are users who are using less than a millisecond, in which case we would need to solve the double problem Sooner.
**GZ Gregor Zeitlinger** 30:42 But who would we ask?
**Trask Stalnaker** 30:44 Jack Shirazi.
And Jonas and Sylvain.
**GZ Gregor Zeitlinger** 30:52 Yeah, that's a good, good one, huh?
**Trask Stalnaker** 30:54 Because they have customers using this, that's why they ported it from their distro upstream.
**Jay DeLuca** 31:05 I don't think I see the use of a double anywhere in the schema, which is interesting.
**Robert Niedziela** 31:29 I have one more concern, since the… OpenTelemetry Java implementation of the interface that is the default config properties supports time units.
It means that time units are supported also in environment variables.
and system properties. And we have this functionality of, environment variable substitution in YAML.
So, it will not be compatible weakness.
**Jay DeLuca** 32:06 Yeah, this feels like something we should probably include a big call-out in the documentation.
**Trask Stalnaker** 32:14 Or Java, but that would be, yeah, Java-specific, since the time unit support was Java-specific.
**GZ Gregor Zeitlinger** 32:22 I have added a section… And the document, and the Java.
section already.
**Trask Stalnaker** 32:29 About time music.
**Jay DeLuca** 32:30 time unit.
**GZ Gregor Zeitlinger** 32:31 About duration.
**Jay DeLuca** 32:33 Alright, great.
**GZ Gregor Zeitlinger** 32:42 I'll just… Added here for reference.
**Trask Stalnaker** 32:51 Yeah, I mean, it's unfortunate that the… declarative con… that migration… The migration… what did I have? Examples… the SDK migration config.
won't work.
or Java… Because of this.
**GZ Gregor Zeitlinger** 33:18 Yeah, this is exactly what I, filed in my buck report.
**Trask Stalnaker** 33:29 Yeah, I think the best we can do, is… in the… maybe we could, in the SDK, we could detect… This, and, log a really clear warning, message for users.
**GZ Gregor Zeitlinger** 33:51 So… And we do that… Robert, did you try out what happens now? Do you get an exception?
**Robert Niedziela** 34:01 I'm just looking into the code, and it probably is compatible. I mean, well, when… when the… Value has no unit.
It will, it will work, right?
Because even current code in default config properties will handle it.
It looks like it will.
Scale… Let me check the scale value… Hmm… Hmm… I would, have to check it, actually, because it looks, on the… at first glance, it looks like it should work without a time unit as well, but if, any, any duration will have, environment variable with duration will have time unit. The current implementation, in my opinion, will throw exception.
But I can double-check it.
After, after our call. I mean, tomorrow, probably.
**Trask Stalnaker** 35:20 Yeah, and my thought, especially for the SDK ones, because I think it's going to be very common for people to grab this SDK migration config and throw it in there.
is… just to make sure that we… I mean, it's gonna throw an exception, or it's gonna do something, let's just… it would be good if that's a really clear… One to users.
**Robert Niedziela** 35:47 Not the…
**GZ Gregor Zeitlinger** 35:48 I just found the code. It says long or null , so it will implicitly give you the default value, that's not the best experience.
**Trask Stalnaker** 36:00 Yeah, I mean, the default, at least is not crashing, right? I do support that, but it should log a warning message.
I think for users, so they can fix it.
**GZ Gregor Zeitlinger** 36:13 That's at the SDK level, so we have to convince Jack that this is a good idea.
**Trask Stalnaker** 36:21 I think his… I would imagine his amendment would be amenable to, you know, improving warning messages for users.
This is not changing behavior, right?
**GZ Gregor Zeitlinger** 36:33 Yeah, that's easy to argue, you're right.
**Trask Stalnaker** 36:36 Yeah.
**Robert Niedziela** 36:43 Yeah, but you are talking about SDK section, right? Not about implementation section.
So, for instrumentation section, for example, I got, exception, and my agent didn't start.
**Trask Stalnaker** 36:57 So we should fix that, yeah.
**GZ Gregor Zeitlinger** 37:00 Oh, maybe I'm… I'm misinterpreting what I'm reading in the code, if you are getting an exception. I thought you would not.
I have to run the code, actually, to be sure.
**Robert Niedziela** 37:13 Okay.
**Trask Stalnaker** 37:15 Robert was talking about the instrumentation.
**Robert Niedziela** 37:19 Yeah, yeah, I'm talking about instrumentation.
**GZ Gregor Zeitlinger** 37:22 Right, and my…
**Robert Niedziela** 37:24 And instrumentation was… the values from instrumentation was going through declarative config properties.
Right? We are talking about the implementation of the clarification config.
**GZ Gregor Zeitlinger** 37:35 Yeah, and I was looking at the implementation, yeah, yeah. I was thinking the same, and I was reading that it's long or null , but if you're getting an exception, then I'm probably wrong.
**Trask Stalnaker** 37:54 Alright, so that's some good follow-up.
Shall we… Move on…
**GZ Gregor Zeitlinger** 38:03 Yep.
**Trask Stalnaker** 38:05 Extract resource correctly. Alright, so let's see what Jack says.
**GZ Gregor Zeitlinger** 38:12 I already wanted to respond, but then I wasn't sure.
**Trask Stalnaker** 38:21 Yeah. So, I mean, I think… He's basically saying yes, We should figure out if Entities solves this.
**GZ Gregor Zeitlinger** 38:41 That's all good. I'm still thinking about whether I… my stance is that it's a regression, and we should avoid a regression.
Or, if this is a good opportunity to, like.
Do the big loop, and, discuss this at a general level.
Because right now, for users, it is a regression, and I would like to avoid that and make this a separate discussion, but I don't know if that is a defensible option.
**Trask Stalnaker** 39:15 Which, which… Where, what's the specific regression? Let's talk about, like, the specific use case, like, MDC…
**GZ Gregor Zeitlinger** 39:30 Yeah, this is the one, setting MDC resource, exactly. This is, going to… Stop working, let's say, like that.
**Trask Stalnaker** 39:43 I see, and the reason was that previously in the agent, we sort of hacked it.
And we grabbed the… because, like, this… Jack's point is that we're sort of bypassing it as a… we're… the agent is grabbing it out of the SDK and exposing it via its own sort of API to instrumentation to use.
**GZ Gregor Zeitlinger** 40:11 Yeah, you could say it like that, yeah, that's fair.
**Trask Stalnaker** 40:14 So… is there a way for us to hack it in the agent… Again, with the new… Structure, or is it just not hackable anymore, and that's the problem?
**GZ Gregor Zeitlinger** 40:32 It is, it is under, I don't know, 5 or 6 layers, of, Fields, but we could hack it out of there.
I'm doing that and tests, yeah.
**Trask Stalnaker** 40:51 Exactly. By reflection. Reflection.
**GZ Gregor Zeitlinger** 41:20 So previously, it was not actually a hack. It was a field in the auto-configured SDK Builder, which is package local, but it's kind of like the recommended pattern for incubating Things that, that they are packaged private, and then you have, A field access to do that.
Because they are.
**Trask Stalnaker** 41:44 Oh, it was an internal… oh, okay.
Do we know where that, Where that is… let's see…
**GZ Gregor Zeitlinger** 41:59 Let me give you the, class name.
**Robert Niedziela** 42:18 I have to step away from my computer for a minute, and I'll be back, so…
**GZ Gregor Zeitlinger** 42:23 Yep, sure.
Here it is.
And we have worked around that by creating an access class in the same package, where it's readable.
**Trask Stalnaker** 42:52 Oh, we did that on the… This thing.
Okay, and then in the MDC, I just want to paint the picture for Jack so that he… can understand, Where are we?
Let's see, it should be in here, right?
**GZ Gregor Zeitlinger** 43:41 No, it's a… it's an X.
**Trask Stalnaker** 43:44 No, this is the appender.
**GZ Gregor Zeitlinger** 43:47 I'll give you the one.
**Trask Stalnaker** 43:56 I guess I can look.
**GZ Gregor Zeitlinger** 43:59 I already have it open.
**Trask Stalnaker** 44:00 Okay, great.
**GZ Gregor Zeitlinger** 44:11 Yeah, it's in the, docker now.
**Trask Stalnaker** 44:18 Oh, this one… I had found this one. What I'm looking next is the, How… where were you reading that from MDC?
**GZ Gregor Zeitlinger** 44:29 Oh, okay.
Mmm… C.
**Trask Stalnaker** 44:41 Damn…
**GZ Gregor Zeitlinger** 44:47 Yep, bye.
Also have that.
Here it is.
**Trask Stalnaker** 45:10 Yes, thank you. Comparison, actually.
Okay.
So… The story is… Let me grab this… It's a startup.
Exposing them via our own API.
That is… This guy… June… Let me access it… Here… Alright.
Cool.
Alright, we're getting close to next meeting. Anything else?
We wanted to look at here?
**GZ Gregor Zeitlinger** 49:11 We could look at PRs, but… I also feel like we deserve 10 minutes.
To the next meeting. Agreed. All right.
**Trask Stalnaker** 49:22 See you there.
**GZ Gregor Zeitlinger** 49:22 See you there.
**Robert Niedziela** 49:24 Leo.
