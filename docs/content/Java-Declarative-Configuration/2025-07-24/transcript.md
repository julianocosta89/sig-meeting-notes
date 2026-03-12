SIG: Java Declarative Configuration
Date: 2025-07-24
Duration: 57 minutes
============================================================

## Zoom Recording Transcript

**GZ Gregor Zeitlinger** 02:32 Hello!
**Jay DeLuca** 02:36 No.
**GZ Gregor Zeitlinger** 02:42 Okay, we're 3 min in.
I thought someone would say something, okay, great that you could. You could also make it. Laurie.
Let me share my screen, the trasks, or anything, if he is able to make it.
**Jay DeLuca** 03:14 See anything from him now.
**GZ Gregor Zeitlinger** 03:16 Okay, is he on vacation? I think he just was share.
**Lauri Tulmin** 03:27 In slack. It says that he is on vacation until 26.th
**GZ Gregor Zeitlinger** 03:33 Oh, okay, because I just read a message from him today about something that he wanted to look up.
But we have plenty of other things that are unrelated to this semantic convention thing.
So 24, th yeah, that's today.
So let's start with the config bridges. So, Jay, you already know that because we talked about it. And, Laurie, you've also read it today. So I think we're in a pretty good shape. I can actually show what it looks like. Maybe that's that makes it easier to see how we should first, st how we should name it, and then where we should place it. And if we should have duplicates, or if we should have a single version.
here! This is right where it's used.
so I have not renamed it yet, Laurie.
This is, I think, what Jay suggested.
And I think, Laurie, you said that it's confusing, because it's actually not a factory, right?
**Lauri Tulmin** 05:11 Or maybe I didn't find the correct method where it would build anything.
**GZ Gregor Zeitlinger** 05:17 And so what it builds is like this bridge object which is returned here.
and what I had now, as another suggestion is, no, that's the wrong one.
Why is it so slow?
Okay.
declarative config properties, bridge builder? Because it actually is a builder. It's but it's a very long name.
Hi, Robert.
**Robert Niedziela** 06:12 Hello! Hello! Sorry for being late.
**GZ Gregor Zeitlinger** 06:15 Yeah, no worries. We've jumped right into the most difficult things. How to name something.
**Robert Niedziela** 06:22 Oh!
**GZ Gregor Zeitlinger** 06:23 And in this case it's the declarative config property Bridge that is helping for translating entries in the configuration file to the old syntax for system properties and environment, variables and Jay and Laurie have already looked at the pull request. And and now, I have presented my next approach.
That is declarative config properties, bridge builder, or something that ends with builder because it really is a builder. Then you can, and you can do some configuration. And the last one, which is usually called build has a different name, because there are different flavors to it. So resolve. Config is.
It's 1 of the flavors and a different flavor would be all right here.
Yeah. So resolve, config or resolve, instrumentation, config or resolve config properties.
So in one case you get you give it the the return value of what you got from auto configuration, and in the other cases you give it some more specific object for different use cases.
Oh, and the agent we currently are we currently using, we're using one of them.
Yeah, instrumentation config. So the instrumentation config is what we get here. And in the contrap repository I have a use case where I give it a specific object, because it is. It is something from the SDK, where it does not have this object the instrumentation config for the 1st one. I don't have a usage, but this is what I, or what was already there before in the Instrumentation Repository.
This was from the previous point request.
**Robert Niedziela** 08:57 So I use this code in some areas as far as a member of our splunk proprietary code.
This translation.
**GZ Gregor Zeitlinger** 09:10 But it's brand new. Are you already using it, or is it something a different flavor?
**Robert Niedziela** 09:17 S.
Okay, let me, because all these bridges were similar in some areas. So I I use the the original declarative config bridge. That was it was in Java Hotel, I guess. Repo. Oh, no. It was in instrumentation repo. And yeah, I yeah, I took it and use it in in our code. After a few changes I needed. And I'm basically it was package protected. I couldn't use it outside the package as far as I remember. And it.
And yeah, it was actually the instrumentation config, mostly because I I needed the translation between the properties that didn't start with hotel instrumentation, because they were always returned null , and I needed it for our custom config properties. And then I modified this part where where the instrumentation config properties were trans were returned, and there's always null . If other prefix was used.
**GZ Gregor Zeitlinger** 10:31 Okay? Great. Yeah, this this logic is still there. So then you're using this that has been in the last release. I think.
**Robert Niedziela** 10:40 Yeah, yeah, I, this was per my request. Yeah.
**GZ Gregor Zeitlinger** 10:44 Okay. So you are already supporting the declarative configuration. In other words, cool love. It.
**Robert Niedziela** 10:52 I'm working on it, basically.
**GZ Gregor Zeitlinger** 10:55 Yeah, I have on my to-do list to try it out for our distribution, but it does not have to be ours. The goal here is to have a distribution with some real world feedback. So I would also love to have your feedback on that.
that is, and and the project still so slow.
Yep, I'll just take you there.
Oh.
**Robert Niedziela** 11:40 Rob Sunday, just.
**GZ Gregor Zeitlinger** 11:43 Okay.
**Robert Niedziela** 11:44 Hmm.
okay.
**GZ Gregor Zeitlinger** 11:53 Correct.
Okay, so what do you think about the name?
Okay.
**Robert Niedziela** 12:04 Hmm!
I got used to get to declarative config properties. Breach and it's not that bad. But now it's it's more than just.
**GZ Gregor Zeitlinger** 12:23 It is still a bridge, but
**Robert Niedziela** 12:25 Still a bridge.
**GZ Gregor Zeitlinger** 12:25 Configure it. That's the difference.
**Robert Niedziela** 12:28 No.
**GZ Gregor Zeitlinger** 12:29 And The configuration became necessary because of the changes in this Pr and also for the Contrip Repository. Yeah. So this suggestion was declarative config bridge builder is the one that that sticks most closely to the current name.
Laurie. What! That be less surprising for you.
**Lauri Tulmin** 13:04 I think the whole problem is that the class itself is confusing.
**GZ Gregor Zeitlinger** 13:11 Though the bridge or the builder.
**Lauri Tulmin** 13:16 There is this config properties factory that contains a builder.
That builder.
It doesn't produce the factory, but it produces the config properties similar to the factory. I think.
**GZ Gregor Zeitlinger** 13:32 Yeah. And with this approach, the.
**Lauri Tulmin** 13:35 Factory doesn't produce anything.
**GZ Gregor Zeitlinger** 13:40 Yeah, that's right. And with this approach the builder would be top level, and it would not be a sub. A child of the factory.
so the factory would be just on the in the same package, and it would be package protected, so you would not see it.
**Lauri Tulmin** 14:02 Well, that might work better, but can't say anything before actually seeing it.
**GZ Gregor Zeitlinger** 14:07 Okay.
Okay? Then I will give this a try.
the next question is, do. Is it a good idea to have one implementation that is used by both Contrip and Java agent, and then then probably also for distributions, because Robert is already using it.
and in the current place it can be consumed.
**Lauri Tulmin** 14:45 How do? How do you plan to use it in the contribut.
**GZ Gregor Zeitlinger** 14:50 Robert, can you explain that.
**Robert Niedziela** 14:52 In in conscript? No, in the distribution, right.
**GZ Gregor Zeitlinger** 14:56 Sorry in the distribution. Yeah, that's what I meant.
**Lauri Tulmin** 15:02 Is it easy? I can understand. But how do you use.
**GZ Gregor Zeitlinger** 15:05 Okay, got it? Yeah, I can show you how I'm using it there.
So I'm not using the builder pattern here yet, but that that is not the important part.
Yep, there it is. So here we have a different object that we give as an input. So we have a model, then we create a config provider, and then we call resolve, instrumentation, config.
and that in return is called from a declarative configuration customizer provider, that is, the new plugin mechanism for declarative configuration.
And it has a different input.
which is the model which represents a certain part of the Yaml file. And it depends on what you are working on. If you have a spend processor, then the yaml part would be from the part where the spend processor is defined, so you can have a child properties, and then you, then you get this part in in our case a part that we have as the model at model cost customizer is the entire Yaml file. So here we get the entire Yaml file, and here, with instrumentation config, we get like the bottom part of the Yaml file, where all the instrumentation properties are.
and that is return that is fed to the bridge, and looking at a concrete example.
Here it is so here it would be under instrumentation, then Java, and then Google. And this is where all the properties are.
so how we access them is we access them with Google dot cloud. So let's actually see how this looks like.
yeah, exactly. There it is.
Well, this is system property. No, this is the wrong usage.
There's there's another layer of indirection here, a config properties, and then then it says it has an extractor that is taking it from the config properties. But what is the name is taken from the enum? So this is a bit more complicated. But this was there before. So this is turned into a system, property, name.
**Robert Niedziela** 18:34 Google dot cloud, because underscore is replaced by dot.
**GZ Gregor Zeitlinger** 18:38 And Then we have our bridge. So this is a little bit more complicated. And this says.
take Google and replace.by the next indentation level and then project?
Does it make sense.
**Lauri Tulmin** 19:01 So the idea is to allow the same code to work with both system properties and declarative config.
**GZ Gregor Zeitlinger** 19:09 Right? Yeah, this is the same goal as in the agent.
**Lauri Tulmin** 19:14 One thing that might be a bit problematic is that I got the impression that the breach code doesn't rely only on the public Apis.
**GZ Gregor Zeitlinger** 19:28 Okay. Let's see.
Do you remember? Where the problematic pieces.
**Lauri Tulmin** 19:41 Of. I think you had something that accesses some stuff from the SDK.
**GZ Gregor Zeitlinger** 19:48 Oh, you! Maybe you mean that in the instrumentation.
**Lauri Tulmin** 19:53 I think you also had the same code in the contribut. At least I think I saw something.
**GZ Gregor Zeitlinger** 19:59 Okay? And I'm on the wrong track.
Is it? In the bridge itself?
**Lauri Tulmin** 20:06 No, maybe the config properties util class, or.
like this auto configuration, util.
**GZ Gregor Zeitlinger** 20:16 No! I think that.
**Lauri Tulmin** 20:18 That's an internal class.
**GZ Gregor Zeitlinger** 20:23 It is a class where you opt into using incubating things.
**Lauri Tulmin** 20:33 And that's why it is. We have to use reflections or config provider. But the class itself office internal Api.
**GZ Gregor Zeitlinger** 20:44 Yep. And that is because it is accessing, incubating things. So you're basically saying, I'm okay with using incubating things. So it's it's a little bit weird. It's an internal package, but it's meant to be used by users who are okay with using incubating Api. Maybe it also says, Here.
now, actually, this is not explained that this does not mean don't use it, but use it with care.
**Lauri Tulmin** 21:13 Well, like.
**Robert Niedziela** 21:14 And be prepared for failures. Right.
**Lauri Tulmin** 21:16 Generally using that kind of things inside. The agent is perfectly fine, because we can guarantee that our code aligns with SDK.
**GZ Gregor Zeitlinger** 21:25 Right.
**Lauri Tulmin** 21:25 But using it inside the country is well, if there aren't any alternatives, I guess that's that's fine. But it's something that we have to like Consider whether we want to do this, because if the versions don't align, then things will break.
**Robert Niedziela** 21:56 But once it goes out of incubator, will this internal cross go away.
**Lauri Tulmin** 22:02 Oh, most likely.
**GZ Gregor Zeitlinger** 22:04 Yeah, yeah, we already had a different method that was just promoted. And then the corresponding method here in this cloud.
**Lauri Tulmin** 22:10 Anyway, as the as the decorative conflict stuff is still like very much work in progress. It like it might be completely okay for now. But it's just something that you will need to eventually discuss with Jack Berg and see if there's going to be a public Api for this.
**GZ Gregor Zeitlinger** 22:29 Yeah, he has said so in the past that this is this is the way that the evolution of the declarative config works.
**Lauri Tulmin** 22:37 And that's fine.
**GZ Gregor Zeitlinger** 22:44 Now, the other thing is that like
**Lauri Tulmin** 22:49 I think you had in question like Where do we want to place this.
These classes.
**GZ Gregor Zeitlinger** 23:01 I mean, I'm fine for having 2 copies for now, because otherwise we have to wait for I just wanted to discuss it so that you're.
I'm surprised, for now.
**Lauri Tulmin** 23:13 Like I I guess they don't want it in the SDK repo, because it's not the spec thing.
**GZ Gregor Zeitlinger** 23:26 I have not even discussed this with Jack, so I don't know.
So I think contract would be the natural place.
**Lauri Tulmin** 23:42 The problem with contribu is that think like usually the like current dependency goes like.
so that the instrumentation is released 1st before Contrip.
**GZ Gregor Zeitlinger** 23:57 Oh, okay.
**Lauri Tulmin** 23:59 And it's kind of messy, I think if something is being actively developed, then it might be easier to have it in 2 places.
**GZ Gregor Zeitlinger** 24:13 And if we, we can also have it in the agent, and then Contrip can use it from there. Is there any problem with that.
**Lauri Tulmin** 24:24 Well, you'd need to find a place where to keep it in. The agent.
**GZ Gregor Zeitlinger** 24:28 It already has one.
This this was there before I changed anything. It is the version that Robert is using. I'm just making it more powerful.
**Lauri Tulmin** 24:43 Hey!
**GZ Gregor Zeitlinger** 24:49 So.
**Lauri Tulmin** 24:49 The thing is that the agent version currently is inside the Java agent extension Api.
**GZ Gregor Zeitlinger** 24:57 Module.
**Lauri Tulmin** 24:59 This is a module that is supposed to be used with the agent.
It's not something that you can just use in from any library instrumentation.
**GZ Gregor Zeitlinger** 25:09 But you can use it from a distribution.
**Lauri Tulmin** 25:12 Yes, you can use it then.
Oh, okay, we should.
It's it's a it's a dependency meant for developing agent extensions.
**GZ Gregor Zeitlinger** 25:20 Right.
So that means if we wanted to keep it in the agent, then we should probably put it in instrumentation. Api incubator. Would that be the right place.
**Lauri Tulmin** 25:36 Oh, it isn't. It isn't like a instrumentation Api concern. But I guess the config classes aren't either.
**GZ Gregor Zeitlinger** 25:46 Okay.
okay, should we just say that we keep 2 copies, and then we find a place later.
**Lauri Tulmin** 26:01 Oh, we could try that.
**GZ Gregor Zeitlinger** 26:04 Should I then, and remove the methods that are not needed.
and the agent that I added here only to have the same functionality as in contract, or would it be easier if I keep the same logic, so that we have a 1-to-one match.
**Lauri Tulmin** 26:27 Well, if you want to keep them, then you might need to add comments.
or like, make it more obvious.
**GZ Gregor Zeitlinger** 26:35 Yeah, that's totally fine.
**Lauri Tulmin** 26:40 Of course I could also remove them to simplify things.
**GZ Gregor Zeitlinger** 26:46 Whatever your preference.
**Lauri Tulmin** 26:49 Think it's probably easier to review when there is less code.
**GZ Gregor Zeitlinger** 26:52 Okay.
okay.
okay, cool.
Then let's skip the next one, because trust is already on that topic.
But the next one that's a good one testing strategy.
So a couple weeks ago.
we discussed how extensive we want to test the declarative configuration. But that was before we had a look at how this bridging technology actually works and back. Then Trask suggested that we should have a matrix test where we have a corresponding declarative config test for? Well, maybe not everything but a lot of things.
And I'm wondering how it looks now that we have this declarative config bridge that covers a lot of things, not everything.
But it's can show what it does not cover. To give you an idea.
Where is it?
Common config? Yeah, that's the only place, at least so far.
But that is not relying on the bridge, and that is because the bridge just can't do everything. And also Jack has created a utility method, get exactly out of the declarative config what we need.
So here.
this is a utility method that I created. So either take the 1st value from declarative configuration. Or take this other value if you don't have declarative configuration. And here this is a utility method from the SDK that is looking at the the structured values. So here a peer service is a list the same as for client and server request headers.
and the advantage is that since this is in the SDK, there are also tests for those methods.
Yeah, that's as far as I have thought about that.
Jay, do you have more thoughts on that.
**Jay DeLuca** 30:08 Really, I was just trying to think of what we're trying to test. Additionally, aside from the logic of the parsing and mean it, it seems like maybe it would make sense for instrumentations that have a lot of different configs just to make sure that they're all covered. But even that I don't. I don't think we do any existing tests for any of the other configs necessarily is, I guess. Well.
I guess we have different test suites that that exercise them.
**GZ Gregor Zeitlinger** 30:43 Well, so far we only have a test for things that have been developed.
particularly for declarative configuration. And there is one instrumentation that was actually the very, very 1st Pr that I made in this project. And that's the methods instrumentation.
And and this has a complete test suit. So it has a configuration file, and and that's actually very easy to understand.
**Jay DeLuca** 31:21 That's a question is.
**GZ Gregor Zeitlinger** 31:25 How many of those tests do we want to have to be confident enough that this won't break for the 1st user who actually tries to use it.
Oh, yeah. And then.
**Lauri Tulmin** 31:40 Since it's a new feature that, like it breaking for the 1st user isn't the like the end of the world.
It isn't the end of the world.
like, realistically speaking, we probably can't test all the properties.
or, even if we can like, does it make sense.
**GZ Gregor Zeitlinger** 32:03 Hmm!
I can also say that the test of the bridge is fine for us. Just have to ask Trask if he's also fine, since he raised the concern in the 1st place. But.
**Lauri Tulmin** 32:23 Unless, like like. Maybe one way would be like if we if we somehow manage to test like the little configuration part and somehow created. I could a separate suite for testing to declarative, configurable.
**GZ Gregor Zeitlinger** 32:43 You mean the logic here around the agent installer.
**Lauri Tulmin** 32:48 All this, and like we have a ton of places where, like the configuration properties, you start there.
**GZ Gregor Zeitlinger** 32:54 Oh, actually not.
**Lauri Tulmin** 32:55 Patience, for now.
**GZ Gregor Zeitlinger** 32:57 I actually showed you the only place where it's used so far.
And how can I prove that that this is true?
**Lauri Tulmin** 33:10 Yeah, well, I guess actually, like most of the instrumentation will will still like, keep using like whatever they are still currently using. And it will automatically work.
**GZ Gregor Zeitlinger** 33:24 Yeah, this. This is how the bridge is designed. And the bridge has.
**Lauri Tulmin** 33:30 I think the question was, probably the trust had was like whether we should like test the instrumentations so that they are configured with the declarative config instead of the system, properties.
**GZ Gregor Zeitlinger** 33:43 Hmm.
**Lauri Tulmin** 33:47 That could be like a bit too much, I think.
**GZ Gregor Zeitlinger** 33:50 Yep.
Okay. Then I'll write down
**Lauri Tulmin** 33:59 I don't know. Might need to ask to ask.
Yeah, we'll not skip him. Just just wanted to get what you're thinking.
**Jay DeLuca** 34:07 1 1 thing that we could so like with the the methods instrumentation, there's additional functionality that doesn't exist with system properties. So I think that that that's like a perfect test case, for.
like we get value out of the test there. So maybe it would make sense for us to just do additional declarative configuration test suites for instrumentations where the configuration options are different between the 2 approaches.
I don't know how many of those they will eventually be, but we already have one.
**GZ Gregor Zeitlinger** 34:44 Yeah, I guess Laurie will make sure that no new functionality for declarative configuration is added without such a test.
**Jason Plumb** 34:57 There's already really good coverage for the view stuff, right? Metric views.
**Lauri Tulmin** 35:04 In Asia.
**GZ Gregor Zeitlinger** 35:06 Feature. Yeah.
**Jason Plumb** 35:07 It is an SDK feature. Are we talking only about instrumentation? I apologize.
**GZ Gregor Zeitlinger** 35:12 Yes, specifically so in the SDK, I'm not currently changing anything. So if there is something lacking, then this is a bit out of scope for what we're discussing right now.
**Jason Plumb** 35:23 That's cool. I showed up late. Sorry.
**GZ Gregor Zeitlinger** 35:25 No worries.
Okay, shall we move on?
Yeah, we still have a bit of time. Follow up from last week.
yeah. There was one discussion about library instrumentation, and if they currently can unintentionally use system properties.
and I think I have found a place where that is used, and that is important, because the question is, if we need to enable those instrumentations to also use declarative configuration.
So let's see where that was where I think I found something.
Jd is here.
So here and create statement. Instrumenter calls a static method.
and that is directly checking system properties.
And then it. This is used by the library instrumentation.
Yeah, so statement instrument is created as the 1st thing when you create the library. And here this is in the library.
**Lauri Tulmin** 37:29 I think it isn't that straightforward.
**GZ Gregor Zeitlinger** 37:32 Okay.
**Lauri Tulmin** 37:33 Think you should like track like the specific point where it is called, like search search for references.
**GZ Gregor Zeitlinger** 37:40 Of this method you mean.
**Lauri Tulmin** 37:42 Yeah.
**GZ Gregor Zeitlinger** 37:42 Okay, connect. I think this is what I I mean.
So this is the connect method from the Api. So the driver Api and the the.
**Lauri Tulmin** 38:02 Do you understand? Do you now understand why it is done? That the way it is.
**GZ Gregor Zeitlinger** 38:07 Yeah, yeah, because this relies on global state.
At least, that's what I think. The reason is.
**Lauri Tulmin** 38:16 Well, the thing is that this is initialized when the Jtpc. Driver is initialized.
**GZ Gregor Zeitlinger** 38:28 Oh, I was on the wrong path then. Okay.
**Lauri Tulmin** 38:30 It's like,
**GZ Gregor Zeitlinger** 38:32 It's called.
**Lauri Tulmin** 38:33 The same way, like like the same kind of issues that we had with, like those logging frameworks like that, they couldn't get access to the open telemetry instance.
**GZ Gregor Zeitlinger** 38:43 Okay.
**Lauri Tulmin** 38:43 And it's it's the same way like it's initialized by something else that doesn't have access to the open telemetry. And we really don't have like don't necessarily have like access to to the configuration properties here.
**GZ Gregor Zeitlinger** 39:00 And why do we have this set open telemetry? Then.
**Lauri Tulmin** 39:06 It. It probably was added later.
**GZ Gregor Zeitlinger** 39:09 Oh, okay.
**Lauri Tulmin** 39:11 It was probably added later by and trying to mimic like what we did for the for the logging frameworks.
**GZ Gregor Zeitlinger** 39:22 Okay.
**Lauri Tulmin** 39:23 If you like. Look at the blame, then you'll probably see like when it was introduced, and.
**GZ Gregor Zeitlinger** 39:31 Good good idea.
**Lauri Tulmin** 39:33 It's it's kind of complicated here.
**GZ Gregor Zeitlinger** 39:36 Huh!
**Lauri Tulmin** 39:37 Like one way would would be to say that you have to call this set open telemetry method, or whatever, and only then you can get like like.
get access to the configuration properties. But
**GZ Gregor Zeitlinger** 39:55 What does a readme say?
Huh! It doesn't even mention that that you should set.
**Lauri Tulmin** 40:05 There are 2 ways, how how you can use the Jdbc instrumentation scrapping the data source. The other one is using the the driver approach.
**GZ Gregor Zeitlinger** 40:16 I think in the spring instrumentation, you're also using the wrapping the data source approach, because,
**Lauri Tulmin** 40:24 Because the driver one didn't fit well.
**GZ Gregor Zeitlinger** 40:28 Okay, okay. But if we step back a little and zoom out, then we if you like, at the end of the page there is the like a description, the driver way. If you scroll down and you can see how that one is used.
Alright.
**Lauri Tulmin** 40:43 And there is something about injecting the open telemetry also there.
although I don't know if, like just having access to the open telemetry, it's probably not enough even, for we're getting the properties out of it, is it?
**GZ Gregor Zeitlinger** 40:59 That's right, that is right, and that is the trigger point. From last week where I discussed an idea that Jack floated, which is to have an extended version of opentelemetry similar to how you already have extended versions of other Api objects, and that extended opentelemetry would have access to the the configuration as the config provider.
And Trask's reply was that this is a non-issue, because no instrumentation, no library instrumentation is using system properties.
**Lauri Tulmin** 41:51 Well, apparently there is one.
**GZ Gregor Zeitlinger** 41:53 Right. And that's that's why the discussion.
it's back to. Should we support declarative configuration for that.
**Lauri Tulmin** 42:14 Is it really the only one that's using it?
**GZ Gregor Zeitlinger** 42:17 Probably not. This is just one that I found.
I'm fine with having the confirmation that I was not wrong, and I think we can wait for Jack to review this. I have to to pull requests how to implement the extended open telemetry.
Didn't 1 of you review it, Jason? I forgot who reviewed it.
No, that's wrong.
So I have one implementation that uses and extends.
but that makes a final class extensible, and the other one as a solution that is a little bit more complicated.
but that does not have incompatible Api changes, and what it does is it has a pointer to the subclass. So a little bit of manual inheritance.
So you hear it adds extended open telemetry. SDK, but it does not have the the actual type and the places where it's needed. You have to cast. It looks a bit ugly, but it does not use incompatible Api changes. At least.
Yeah, that was actually the second to last. One last one was that tracks suggested that we should move some if we should move some instrumentations from contribute to to the agent repo, but since he suggested it, I don't know what the idea was, so it's probably better to defer that.
**Lauri Tulmin** 45:00 If you search for the usages of this config properties utility, you can quite easily find other instrumentations that are using it.
It's also used in some aws, instrumentations.
**GZ Gregor Zeitlinger** 45:12 Oh, right? Yeah.
**Lauri Tulmin** 45:13 Where the issue is like that. Those are those auto configured instrumentations that are loaded by some spi.
There's also the Kafka library instrumentation that has also 2 versions.
**GZ Gregor Zeitlinger** 45:32 2 reasons.
**Lauri Tulmin** 45:33 Like one is.
**GZ Gregor Zeitlinger** 45:34 One.
**Lauri Tulmin** 45:35 It's based on using the interceptors. This one has the problem and the other one doesn't have the issue.
but also log for Jmtc instrumentation seems to have the same thing.
There's also something in the server instrumentation, although that one should be.
**GZ Gregor Zeitlinger** 46:05 So does it mean that for some cases we just cannot solve the problem because of initialization order? Or do we have to become somehow more creative.
**Lauri Tulmin** 46:24 Well, if but most of those instrumentations.
I think they rely on global open. Therametric get.
So if the extended open telemetry would work.
then that would solve the issue.
**GZ Gregor Zeitlinger** 46:46 That is right. How can we see if that relies on global open telemetry?
Is it? Is this lock for Jason a good example, or is it a bad one to to check.
**Lauri Tulmin** 46:59 You're looking at the wrong globe. 4. J, instrumentation.
Okay, yeah, that the context data module.
This one probably doesn't have the issue. This gets all its configuration from the log, for Jxml. File.
Most likely.
**GZ Gregor Zeitlinger** 47:17 I'm looking at the usages from conflict properties due to.
**Lauri Tulmin** 47:22 Well, may. Maybe this one also has station. Then.
**GZ Gregor Zeitlinger** 47:28 Okay?
So then let's see, trace id key.
**Lauri Tulmin** 47:35 Yeah, this one was for Hostasia.
**GZ Gregor Zeitlinger** 47:39 How is it configured?
Says you should call install.
Okay?
Oh, here it's not the SDK on the receiving side. Okay, but this doesn't matter.
So no, it's not explicitly the global SDK, it's just up to the user. If they want to use the global. If I understand this correctly.
**Lauri Tulmin** 48:30 Well, I guess, for this instrumentation it's that way, but for some other it's others. It's it's some other way.
**GZ Gregor Zeitlinger** 48:41 In other words, not all hope is lost that we can fix this. If we have the extended open telemetry.
**Lauri Tulmin** 48:51 Yeah, but it definitely will require some. Some work.
**GZ Gregor Zeitlinger** 48:59 To have the extended open telemetry.
**Lauri Tulmin** 49:03 To make it work.
There will also be like this weird situation when, like the instrumentation is, you is embedded inside the agent, and the same code can also be run as standalone.
**GZ Gregor Zeitlinger** 49:21 Okay. Now I know what you mean. I have actually done a Poc for this, because I also wanted to know if this is possible.
Where is it?
Too many pull requests.
I have a pull request open in Pr, that is only very small use extended open telemetry right?
So this is an example for Jdbc, right? Because I was looking into that, and it gets the open telemetry, then makes an instance of.
and here it returns from the if clause and in the else clause. I'm just doing what I am doing before, which is based on the rationale that we're not making it worse for users who don't use declarative configuration.
We could also say that we're more ambitious, and we want to fix this for both use cases. Then I would have to rework this example, and then it would have to use the instrumentation config, which is the the bridge between oh, not bridge, which is the Api that is used to get configuration values from instrumentations.
They cannot use the config properties for some reason that I forgot about.
But instrumentation config can be used and instrumentation config has basically the same accesses as config properties.
And then, in addition, it also has this get declarativeconfig. This is the method that I added, and which lets you get properties that are not that are more complicated, like lists of scalars and stuff like that.
And we could also use the instrumentation config here.
if we find a way that we can also pass the config config properties for the old use case.
because there we cannot pass the open telemetry that wouldn't work. Then we would have to pass the instrumentation config and opentelemetry object, or we have yet another object that has both the instrumentation, config and opentelemetry object.
I wasn't sure if this is overkill or not.
and if we go down this route, then we actually would not need the extended open telemetry. Because then we're basically saying, here we have a new object. And all the library configuration needs this object instead of opentelemetry. When you initialize the Instrumentation Library.
**Lauri Tulmin** 53:14 One problem with some of those instrumentations is that is, is also like the ordering that you that you might need to like somehow delay the initialization to increase the chances that the open telemetry SDK. Is set up.
**GZ Gregor Zeitlinger** 53:37 But this is not different from the problem today. As soon as we have the open telemetry object, and we also have the configuration object.
**Lauri Tulmin** 53:50 Okay, like, one problem with the library instrumentations is that you could have multiple open telemetry objects. And how would you know like which one to use.
**GZ Gregor Zeitlinger** 54:04 Well, what I'm suggesting is that we have an object that holds both an instance to opentelemetry and whatever configuration objects we need.
So basic.
So basically we could use the auto configuration auto configuration.
What is it called auto configured? SDK, yeah, we could use this object. The only problem is that this prescribes away. How you get the object which is to use the auto configuration, you can also programmatically create it.
**Lauri Tulmin** 54:49 I think that's not going to fly.
**GZ Gregor Zeitlinger** 54:52 Too complicated.
**Lauri Tulmin** 54:54 Because because this is not the only one only thing that you can use to create the open telemetry instance.
**GZ Gregor Zeitlinger** 55:03 Exactly.
but we could have a copy of that class that has the same field and just a different name.
**Lauri Tulmin** 55:18 I don't know. I think this needs more thought.
**GZ Gregor Zeitlinger** 55:21 Probably.
But now you have some time to think about it. Next week I'm on vacation. Should we keep the meeting, or do you want to cancel it.
**Lauri Tulmin** 55:35 Well, I think I'll be away next week, too.
**GZ Gregor Zeitlinger** 55:38 Okay.
Jay, do you want to keep it?
**Jay DeLuca** 55:50 I don't think I have enough to fill a meeting, so yeah, probably cancel it until you come back.
**GZ Gregor Zeitlinger** 56:01 Okay.
Robert Jason, all's fine for you.
**Jason Plumb** 56:08 I'm okay with that canceling it.
**Robert Niedziela** 56:09 Yeah, that that's okay. At some point I would like to talk about these validators, but it may, it can wait. It's not something that I'm in rush right now.
**GZ Gregor Zeitlinger** 56:19 But feel free to put it on the topic. Queue, then we don't forget it.
**Robert Niedziela** 56:25 It. It was put as last week at the end. So but that that's okay. I still work on some other aspects, and I'm going to.
Maybe I will have some proposal how to and solve this on our next meeting. Then.
**GZ Gregor Zeitlinger** 56:45 Okay, cool alright. Then see you in 3 min.
**Jay DeLuca** 56:58 Check.
**GZ Gregor Zeitlinger** 56:58 Thanks a lot.
**Robert Niedziela** 56:59 Yeah, bye.
**GZ Gregor Zeitlinger** 57:01 Fine.
