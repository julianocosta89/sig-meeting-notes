SIG: Java Declarative Configuration
Date: 2025-11-24
Duration: 41 minutes
Zoom Recording URL: https://zoom.us/rec/share/dyLRmdprAnGDndL4zqF4nat6QNbendHgyoVLOqLVOFLc5aBLY9ojpcD6N5JWv1w.XLxKsDXa87a0Jhl7
============================================================

## Zoom Recording Transcript

**GZ Gregor Zeitlinger** 00:00 Requ.
**Trask Stalnaker** 06:49 Hey, Grigor!
Thanks for the ping.
**GZ Gregor Zeitlinger** 06:54 No…
**Trask Stalnaker** 07:01 My calendar never reminds me about anything.
**GZ Gregor Zeitlinger** 07:05 No worries, you have me.
**Trask Stalnaker** 07:10 So, like, if it's not in my regular brain of, like, oh, yes, I know I have a regular meeting, I've gotta figure out why my calendar doesn't work.
Alright.
What, do you have… did you put down topics already?
**GZ Gregor Zeitlinger** 07:28 I… think so?
**Trask Stalnaker** 07:31 Cool.
**GZ Gregor Zeitlinger** 07:32 Or did I? They're actually the open PRs that, we already discussed before, so…
**Trask Stalnaker** 07:42 Yeah, yeah, we can just jump to those.
**GZ Gregor Zeitlinger** 07:47 I think it's just easier than, doing the review asynchronously.
**Trask Stalnaker** 07:52 Yeah, yeah.
Alright, what shall we look at first?
**GZ Gregor Zeitlinger** 08:06 I wanted to look at this new instrumentation bridge. Let me actually see if I… Did I really not put that in the…
**Trask Stalnaker** 08:20 No, it's there.
**GZ Gregor Zeitlinger** 08:20 Gun duh.
**Trask Stalnaker** 08:21 remember.
Oh.
**GZ Gregor Zeitlinger** 08:25 Exactly, System Properties Bridge. So this is, now, the… The third attempt, we're getting there.
And I actually like, the… Your idea to, reverse, the bridging, And, now it is part of this config properties util. And if you look at the usages, then you see, that, it will look more like declarative config, because you… You see the different, hierarchy levels.
We're not.
**Trask Stalnaker** 09:10 Yeah, yeah.
**GZ Gregor Zeitlinger** 09:11 config directly, and the reason for that is, that the API is kind of clunky, I would say.
And… And also, the other reason is that it would be kind of… Overkill to create an object just to get one property out of it.
That was my, my take when I thought about this pull request.
**Trask Stalnaker** 09:45 Great, let me understand what that means. Showing configure property util… Got it.
So… I think… I think I didn't follow that part. Why… what do you mean by creating an object just to get one property? What object would we be creating?
**GZ Gregor Zeitlinger** 10:16 If you go back at this, place we just looked, where this implemented getString or fallback, then you can see that in the case of declarative config.
We are getting a node object, and this node object has, the type config, declarative config properties. So if we would be bridging, then I think we would be creating a declarative config properties object.
out of, system properties. So, probably system properties that have a prefix hotel. And if we did that, then we could use a declarative config API… And… Without knowing what it is.
But I did not… I wanted to save the step of creating this declarative config properties object, if we don't need it, and… This is in line 109, where we say to system property, and then we just call to getString, and getString is…
**Trask Stalnaker** 11:27 I see.
Can we create the declarative config node at startup?
like… create the whole declarative config structure at startup based on the system properties, then it's not like we're creating it each time we're asking for a config.
**GZ Gregor Zeitlinger** 11:56 Yeah, I see what you mean.
Then in line 109, you would also be Querying declarative config properties.
Is that what you're…
**Trask Stalnaker** 12:10 Same.
No, I think it would be the… let's see… Oh, yes, yes. So, in that case, you could… like, I'm trying to… See, how could we… use declarative config API directly here.
**GZ Gregor Zeitlinger** 12:39 If we had this node, So what you are doing is, you have this, OpenTelemetry object, and then you have to check if the OpenTelemetry object provides the declarative config, and otherwise you're getting the fallback. You always need to give it the OpenTelemetry object to see what you're getting back.
**Trask Stalnaker** 13:09 Do we need to check if it has declarative config?
Well, what if we just used… declarative config… What if we just use declarative config only?
API only here.
What would be the downsides?
**GZ Gregor Zeitlinger** 13:41 You mean if system properties were, ignored?
**Trask Stalnaker** 13:45 In the Java agent, we would, at startup of the Java agent, we would read all the system properties and Populate those nodes in declarative config?
**GZ Gregor Zeitlinger** 14:02 But what, what would the API look here? Would you look at the global to see, What the result of the parse at startup was?
**Trask Stalnaker** 14:12 Yeah, because in this… case, you would just do global… you would do… cast global open telemetry to extended open telemetry.
And get the config provider, and get the… use the declarative config API just normally…
**GZ Gregor Zeitlinger** 14:42 Okay.
**Trask Stalnaker** 14:43 That's where the… that's where the really big benefit comes from for us, if we can use… if we don't need to expose yet another config API.
And we can just lean entirely into declarative config.
And library instrumentation, will… Then only work with declarative config, not System Properties.
But we've tried not to use system properties in library instrumentation anyways.
And for Java Agent, we can do the initialization trick of… Converting the system properties into the declarative config nodes.
**GZ Gregor Zeitlinger** 15:43 So, this would be taking away capabilities where libraries are getting system properties. Are we prepared to make this, sacrifice?
**Trask Stalnaker** 15:56 We've… Try not to give libraries… system properties. We've tried to only do programmatic config.
**GZ Gregor Zeitlinger** 16:07 But it… but it has happened.
**Trask Stalnaker** 16:08 We have failed. Yeah, it has happened. So, in those cases, in those specific cases.
I think we could do, like, handle those specially, those cases, so that we don't break people until 3.0.
And… we could… Do our own fallback inside of those libraries.
to system properties.
**GZ Gregor Zeitlinger** 16:38 Okay, cannot tell you right now how much… How much is affected, and if that put, blow up the PR, but I can definitely check that.
**Trask Stalnaker** 16:53 For some reason, I had the number 4 in my brain, that there's 4 places that we've… that library instrumentation is using system properties.
But I could be…
**GZ Gregor Zeitlinger** 17:07 Is that in some… PR, maybe, that we talked about before.
**Trask Stalnaker** 17:13 Maybe.
But… Yeah, definitely take a look, and… for… I mean, even if we need to do something like call… Some shared thing from those… specific places… If we can, for all of the others, let's see, what is this? This is… Log… this is a library con… oh, yes! This is one of those auto-configure… auto-configure ones do use it.
So this is one of those legitimate, or… I mean, places where we have used System properties, let's see… Yeah, so this whole module is… This is a Java agent module, so that's fine.
This is… a library instrumentation.
This is an auto-configure instrumentation.
So… I mean, I would… maybe, as a step.
Right, we could leave this for… Places that are… Calling it from library instrumentation.
But let's change… the place… the other places… let's try to make the other places use declarative config… API only.
**GZ Gregor Zeitlinger** 19:04 Which would be Java agent, then, if you're saying library should stay.
**Trask Stalnaker** 19:09 Yeah.
Let's see, what do we got here?
Hahaha. Yeah, this was another one.
I'm curious how many, because definitely the ones you've Found here are many of the… Are actually a bunch of the library ones.
**GZ Gregor Zeitlinger** 19:37 This is already the complete list, so there won't be more.
And that…
**Trask Stalnaker** 19:43 Oh, this is the complete list.
Complete list of… We… but we read… properties… In a lot more places.
**GZ Gregor Zeitlinger** 20:03 Right. The most common one is where we already have our declarative config bridge.
And that is using, a… global for agent already, and that is handling, I don't know, 90% of the usages.
And then the… the rarest one is at a startup where we are reading system properties directly without this bridge because of reasons. And… That is why it's only, so few…
**Trask Stalnaker** 20:45 Let's look at an example of a Java agent.
Property… There's gotta be something in… yes.
So… Let's take one of these.
**GZ Gregor Zeitlinger** 21:15 Yeah, I don't.
Should find you something.
**Trask Stalnaker** 21:19 Haha, lots of them.
**GZ Gregor Zeitlinger** 21:23 Exactly. Agent instrumentation config get. This is the common pattern.
**Trask Stalnaker** 21:28 Yeah… Can we change the… like, this is… this is what I was thinking would be nice to update these to…
**GZ Gregor Zeitlinger** 21:41 Oh, yeah.
**Trask Stalnaker** 21:42 declarative Config API.
**GZ Gregor Zeitlinger** 21:46 Yeah, yeah, I've also thought about that. I've just… Park that for a later stage in my head, until we have, Completed the first phase of, being able to use declarative configuration.
**Trask Stalnaker** 22:02 Okay.
**GZ Gregor Zeitlinger** 22:02 It would be nice, I agree.
**Trask Stalnaker** 22:05 Okay.
So then, let's come back to here. What are… so for here… We're changing… Where we were… the config property util… I see, okay, okay.
So, yes, so this is now… It's the library… yes, we get this with the default, and here we are.
Now, converting it… to… More or less mimic… declarative config… And this will do the lookup of declarative config.
First, if it doesn't, then it will construct. Okay, yes, yes, yes, I like this. and this kind of starts to pave the path towards this anyways.
Right.
Yeah, using the declarative config API.
Cool.
**GZ Gregor Zeitlinger** 23:34 And I'm thinking that it would actually be nice to have away in the SDK with this var ar arc argument.
But that's also a follow-up.
**Trask Stalnaker** 23:48 Oh, yes, yes. I think this is good. I think by integrating… making these changes over here, it gives… when… it gives example usages and sort of user… usage feedback to Jack, and for… Right.
Showing, hey, look, we could really use, like… or how would you suggest we do this? We have this all over the place.
Okay And so, let's… see, anything… else… So… This incubator…
**GZ Gregor Zeitlinger** 24:35 I think one thing you touched is on when we should use system properties, and I have to double check if that is in line with what I have implemented here. So, I think you said if it is a library, then it should not look at System properties, is that right?
**Trask Stalnaker** 24:55 Yeah, so… What we want is for… this is fine for… because we've already committed to this, and we could… We don't want to break it at least mid-2X.
**GZ Gregor Zeitlinger** 25:10 But what we've…
**Trask Stalnaker** 25:12 can start doing now is we can start exposing more… Config to libraries.
But we should only use declarative config API for any new usages, because we don't want to fall back to system properties.
**GZ Gregor Zeitlinger** 25:31 Yeah, yeah, I agree.
**Trask Stalnaker** 25:32 those.
**GZ Gregor Zeitlinger** 25:36 I think there is no new property added in this PR, so everything that is covered here, we have already committed, or at least We have set, released unintentionally, at least.
**Trask Stalnaker** 25:53 Yes.
Yes, some of them… the auto-configure ones were… were intentional, because, like, there's no… programmatic… API…
**GZ Gregor Zeitlinger** 26:03 But the other ones…
**Trask Stalnaker** 26:06 Not so intentional.
Okay, yeah, this looks great. I will, go through… what do we got new? Oh, okay, just for the config properties… Test. And what kind of… Test coverage… It should be good test coverage, right? Because we already have… we're already testing these… properties…
**GZ Gregor Zeitlinger** 26:41 So, we don't have integration tests for all of these properties, but I have, added, unit test coverage in this PR.
**Trask Stalnaker** 26:53 I was thinking more about, regression testing. We do… I think we have the system property testing for these.
Let's see, Kotlin…
**GZ Gregor Zeitlinger** 27:07 That's what we usually do, yes.
**Trask Stalnaker** 27:09 Yeah, yeah.
So, yeah, I… That was… that was more my concern, was regarding testing.
Okay, great. I will give this a full review, but it looks… I understand it now, thank you.
**GZ Gregor Zeitlinger** 27:27 Okay, cool.
Yeah, let's look at, the, Spring Starter Logging Exporter. I think that's a small one.
And then we have a similar one for thread configuration.
Yeah, that is the original issue. This is where it originally came from.
**Trask Stalnaker** 28:03 I'm sorry, declarative config… declarative config logging exporter.
declarative config… logging… Exporter… I'm still trying to understand what.
**GZ Gregor Zeitlinger** 28:34 What we are trying to do.
**Trask Stalnaker** 28:35 Yeah, yeah, yeah.
**GZ Gregor Zeitlinger** 28:37 It's a shortcut for, adding a console exporter.
And it adds a property, that makes it shorter than having to configure The logging exporter in the list, and this is… by saying that you want to have debug configuration. So, in Spring Starter, it's called, Java Spring Starter Debug.
And, and Java agent, it's called, the same with, agent.
**Trask Stalnaker** 29:20 Okay, and we already have those… Support for this as a system property.
**GZ Gregor Zeitlinger** 29:26 Exactly.
So we… we don't have to support it in the same way. It's already called differently. This is just bringing, feature parity.
**Trask Stalnaker** 29:43 Okay, got it. Give me just a sec… Okay, so we get this is enabled… the collateral config, instrumentation… Okay, abstract span logging customizer Provider… Gotta love those long names.
**GZ Gregor Zeitlinger** 30:59 Add. Model…
**Trask Stalnaker** 31:01 Customizer… Maybe enable logging.
Exporter…
**GZ Gregor Zeitlinger** 31:11 Cool.
**Trask Stalnaker** 31:12 Okay, so this one… is mutating the… yes, it's a declarative config. It's mutating the declarative config.
**GZ Gregor Zeitlinger** 31:24 Model, yes.
**Trask Stalnaker** 31:27 Okay, and… oh, I see, you were designing… And this… does this extend?
That one is… I haven't quite… Figured out why we have both.
**GZ Gregor Zeitlinger** 31:48 One for Spring Starter, and one for Agent.
**Trask Stalnaker** 31:55 Oh, this is the one for the…
**GZ Gregor Zeitlinger** 31:58 This is, the SDK auto-configure support is the abstract one.
**Trask Stalnaker** 32:04 Okay… And where is that used?
**GZ Gregor Zeitlinger** 32:10 The first one?
**Trask Stalnaker** 32:11 Oh, I see, I gotcha. It's used.
to… Okay.
And what is the… so you're… Who else is going to implement this?
Oh, this guy here.
I see, you pushed all of this down into… sorry, just taken me a while here.
**GZ Gregor Zeitlinger** 32:34 Yeah, for sure.
**Trask Stalnaker** 32:34 All of this done. Okay, yep, yep, I understand. To… common… Okay, SDK Auto Configure Support. What else is in SDK Auto Configure Support?
**GZ Gregor Zeitlinger** 32:53 It looks like…
**Trask Stalnaker** 32:54 Both.
both the Spring Boot and Java Agent already Use that…
**GZ Gregor Zeitlinger** 33:02 So we have a resource provider, properties customizer that is making sure that we have an easy way to add cloud providers, but don't have them enabled by default.
And we have the… Threat Detail Span Processor.
**Trask Stalnaker** 33:26 Okay, so essentially.
**GZ Gregor Zeitlinger** 33:27 Absolutely.
**Trask Stalnaker** 33:27 This has become the… this is just a shared place for the Spring Boot and the Java agent?
**GZ Gregor Zeitlinger** 33:37 Exactly.
**Trask Stalnaker** 33:37 Basically, you… you've created this out of… in order to share stuff. Got it.
**GZ Gregor Zeitlinger** 33:44 Nope.
**Trask Stalnaker** 33:45 Okay.
**GZ Gregor Zeitlinger** 33:47 Quarkus could theoretically also do that if they have a similar setup, but we didn't discuss this.
**Trask Stalnaker** 33:57 Logging spin, exporter… Additional on class… Okay, yes, I… I… understand this, and… I'm going to approve it. I'm gonna ask, Jay… 10 years.
Very much.
But, yes.
**GZ Gregor Zeitlinger** 34:34 I usually give them the PRs first, but… I missed that one.
**Trask Stalnaker** 34:40 Oh, Norris.
Alright, what next?
The thread details. Thread details? Alright.
**GZ Gregor Zeitlinger** 34:57 We also discussed that before.
**Trask Stalnaker** 35:00 Yeah… Okay… Surrender Builder, okay… Should… Chicken… Declarative Config… Okay.
Add thread details attribute extractor… Dutch.
**GZ Gregor Zeitlinger** 36:00 Yeah, we discussed about that last time, Concerning the question whether this is… Only for starter, and Agent, or if native instrumentations should also benefit.
I think we landed on that. That's why it's not added as a… Customizer, but built in.
**Trask Stalnaker** 36:26 Right… So we get the instrumentation config… Check… the nodes… Okay, yes, yes, and this doesn't have system property fallback. Love it.
Okay… The details, attribute, extractor… Yes.
Test. Yes.
Docs.
Documentation…
**GZ Gregor Zeitlinger** 37:22 Yeah, how do we… I think, my plan is… To add this in… the docs page.
under… Beholder.
That's right.
**Trask Stalnaker** 37:41 Okay.
**GZ Gregor Zeitlinger** 37:43 Should it be under declarative configuration, or under threat details?
**Trask Stalnaker** 37:51 Wherever we have those common… I mean, I feel like we'll probably have… some common… Wherever we document the other common config options.
**GZ Gregor Zeitlinger** 38:08 Yeah, thing is, we don't do that for all, Let me see if, we have… Have it for, thread details.
It's not there.
So an agent configuration, that's where I'm looking.
Yeah, declarative configuration would not be a good place.
Because you wouldn't look there if you wanted to know what.
**Trask Stalnaker** 39:02 Right.
**GZ Gregor Zeitlinger** 39:03 Config our thread details.
Maybe under Instrumentation Config?
**Trask Stalnaker** 39:18 That sounds like a good place.
CU, is that under… Zero…
**GZ Gregor Zeitlinger** 39:25 under zero Java Agent.
But it has almost nothing compared to the amount of options that we actually have.
**Trask Stalnaker** 39:40 Okay, but it does have the common ones here.
So that's good.
Okay, yeah, just think about it. It doesn't have to block merging the PR.
**GZ Gregor Zeitlinger** 39:59 Maybe that's also a good option, a good thing to discuss in… Next weekend, the big meeting.
**Trask Stalnaker** 40:06 Yeah, definitely.
Yeah, it would be…
**GZ Gregor Zeitlinger** 40:09 on there.
**Trask Stalnaker** 40:09 Jack's thoughts on… yeah.
**GZ Gregor Zeitlinger** 40:12 Also, Jay, because he's working on automation.
**Trask Stalnaker** 40:16 Yes, yes, and the docs, yup.
Alright, anything else you want to look at?
**GZ Gregor Zeitlinger** 40:33 Let me just check if, from the last meeting notes, if I had anything else left over.
**Trask Stalnaker** 41:00 I will leave this up.
And…
**GZ Gregor Zeitlinger** 41:10 Oh, that's good.
**Trask Stalnaker** 41:12 Alright.
**GZ Gregor Zeitlinger** 41:12 I'm not ready yet for, like, distro, so we'll discuss it once I have more.
**Trask Stalnaker** 41:22 Awesome. Yeah, I will try to get to that system properties bridge.
And, yeah, thank you.
Good progress.
**GZ Gregor Zeitlinger** 41:30 giving.
**Trask Stalnaker** 41:31 Yeah, thanks.
Bye.
**GZ Gregor Zeitlinger** 41:34 Bye.
