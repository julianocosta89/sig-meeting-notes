SIG: Java Declarative Configuration
Date: 2025-09-04
Duration: 56 minutes
Zoom Recording URL: https://zoom.us/rec/share/aEXJbH9NkNi9NkvAATWpHNw6ZPEfzNGGp6W1TV4FAojyzluivdIgI_cf6bTVX86h.Rgah494Ewfgnbakg
============================================================

## Zoom Recording Transcript

**GZ Gregor Zeitlinger** 01:05 Hello?
**Trask Stalnaker** 01:10 Hey, Gregor!
**GZ Gregor Zeitlinger** 01:16 Sorry I'm a bit late.
**Trask Stalnaker** 01:18 No worries.
A whole one minute.
**GZ Gregor Zeitlinger** 01:24 Yeah, yeah, okay.
**Trask Stalnaker** 01:26 Dock your wages.
**GZ Gregor Zeitlinger** 01:42 Not many people today.
**Trask Stalnaker** 01:50 They may still show.
**GZ Gregor Zeitlinger** 01:55 Hi, Trey!
**Jay DeLuca** 01:58 Hey, guys.
**Trask Stalnaker** 01:59 Good morning.
**GZ Gregor Zeitlinger** 02:29 Okay, I added… our template.
I would suggest we start with, PR review, that has proven to be A good idea.
**Trask Stalnaker** 02:49 Cool. I will share… H.
**GZ Gregor Zeitlinger** 03:02 Yeah, particularly the one about a config bridge, take-two.
That, It's only moving the package, so I hope we can get that done as a next thing.
**Trask Stalnaker** 03:17 Oh, yeah.
**GZ Gregor Zeitlinger** 03:20 Jay has also reviewed it today.
**Trask Stalnaker** 03:43 Oh yes, I remember I had just, let's see…
**GZ Gregor Zeitlinger** 03:50 Yes, yes, this was…
**Trask Stalnaker** 03:53 This was my bad. I've totally… got mixed up between API incubator and…
**GZ Gregor Zeitlinger** 04:01 It is easy to. I also had the same.
**Trask Stalnaker** 04:06 Oh, why do I have pending comments? I hate it when… That happens.
**GZ Gregor Zeitlinger** 04:12 I think you started the review and you did not hit submit.
**Trask Stalnaker** 04:16 Yeah.
Okay, okay… So, maybe we can just look at those together.
What did I… A, These exclusions here… Do we need them?
**GZ Gregor Zeitlinger** 04:47 I have to stop me.
They are part of the Bootstrap ClassPass, but let me open up, the… Project… To see if, how that, looks right now.
**Trask Stalnaker** 05:09 Yeah, I think this will get taken care of during packaging. I don't think you need to exclude these here.
for example… Oh god, I'm doing it again, and… reading these as the same thing. Okay, so… Instrumentation API incubator… OpenTelemetry API. Yeah, like, API itself… Right, is implementation… And I think that… carrying them apart into Bootstrap Class Loader is handled later. I suspect we don't need this.
**GZ Gregor Zeitlinger** 06:03 Yeah, I've, spent quite some time a week ago, so I… I know how this massaging can be done, so if you just hit on comment, then I can take care of that later.
**Trask Stalnaker** 06:14 Cool, cool.
Yeah, sorry, I didn't hit comment there. Yeah, and let's see, the… Gonna remove this… No, okay. Yeah, so I apologize for that. Yeah, just ping me. I think everything else looked good. I didn't have… it was just kind of some questions about the Gradle.
But yeah, everything else is very straightforward.
And I think we agreed on… Package name…
**GZ Gregor Zeitlinger** 06:51 Yeah, that was your suggestion, right.
**Trask Stalnaker** 06:53 Okay. Yeah, and that as well.
Okay.
**GZ Gregor Zeitlinger** 06:57 But do hit, comment now, so…
**Trask Stalnaker** 07:00 I did, I did now. It should be… yes, yes.
**GZ Gregor Zeitlinger** 07:06 Yeah, I'm seeing it.
**Trask Stalnaker** 07:08 Okay, great.
Declarative config, extract resource correctly.
Oh, yes.
**GZ Gregor Zeitlinger** 07:25 funer?
**Trask Stalnaker** 07:26 I just worked on that today.
**GZ Gregor Zeitlinger** 07:29 And that's an SDK issue, and this is, difficult because, Jack, Didn't like the idea that we would have to expose the resource at all. Now, it happens to be that we actually used the resource in the agent, because it was available before. So this is more like.
The debates to be had before we can look at the actual implementation.
**Trask Stalnaker** 08:03 So… I see. So, in… the auto-configure… We can access it, because we can call getResource…
**GZ Gregor Zeitlinger** 08:18 Right.
**Trask Stalnaker** 08:19 On the auto-configure… What is it called?
SDK…
**GZ Gregor Zeitlinger** 08:32 I mean, the class…
**Trask Stalnaker** 08:33 Yeah.
**GZ Gregor Zeitlinger** 08:34 That's okay.
**Trask Stalnaker** 08:39 Okay, this will give us the builder, and then that will get us…
**GZ Gregor Zeitlinger** 08:43 Check out OpenTelemetry SDK.
**Trask Stalnaker** 08:46 Yes.
Obviously.
And we have… Oh, but this is not public here.
**GZ Gregor Zeitlinger** 08:59 Right. It's one of those cases where it has become de facto public.
**Trask Stalnaker** 09:07 So we call it via reflection.
**GZ Gregor Zeitlinger** 09:10 no, we have an access class which we place in the same package.
**Trask Stalnaker** 09:23 Here.
**GZ Gregor Zeitlinger** 09:25 No, the agent.
**Trask Stalnaker** 09:28 Oh, in the agent, we do. Oh, we actually put one in the same package as the SDK's package?
**GZ Gregor Zeitlinger** 09:34 Kind of cheating, right?
**Trask Stalnaker** 09:39 Gotcha.
Okay… And let's see what our use case is. Do you have that name of that.
**GZ Gregor Zeitlinger** 09:52 Just a second…
**Trask Stalnaker** 10:02 Okay, here.
**GZ Gregor Zeitlinger** 10:04 Good.
**Trask Stalnaker** 10:05 It is. Here's the util.
**GZ Gregor Zeitlinger** 10:09 Alright, this is the util, but then we put it in a static, holder… Somewhere… Configured resource attribute… Attributes Holder, isn't that a nice name?
I'll put it in… Chat here.
If you look for that, then you can see where we actually excess.
**Trask Stalnaker** 10:40 Okay, and that's probably… From here or here… Yes, okay.
So we're getting it, and then we're putting it here, okay.
And how many people… where are we accessing that?
**GZ Gregor Zeitlinger** 11:05 Blogging-related, it seems.
**Trask Stalnaker** 11:13 Interesting.
So, MDC context data context, MDC… oh, specifically MDC instrumentation.
So not a Pender instrumentation.
Oh, we have a feature that puts… The… resources… into… MDC… So that people can… Add resources to their… logs.
Do we document this? Let's see… Resource attributes, yes. Is it exposed through MDC? Yes, we do.
I see we're putting awe… Where is that list? How are we filtering?
Resource attributes…
**GZ Gregor Zeitlinger** 12:29 Commerce separated, it seems.
**Trask Stalnaker** 12:31 Yeah, but where are we doing that? Because I'm just seeing… We don't know.
Korean news.
**GZ Gregor Zeitlinger** 12:43 All seems to suggest that we're not doing that.
**Trask Stalnaker** 12:46 Yeah, yeah.
Okay.
It's okay, but yes, so we have, so let's… add, comment… 2…
**Jay DeLuca** 13:32 Looks like, it does happen when the, configured resource attributes holder is initialized.
it looks for that.
environment variable.
And then it, like, filters out The one… only the ones that are included.
**Trask Stalnaker** 13:54 Oh, interesting. So this, even though this is in the bootstrap, and… Oh, because this is common. Got it.
Oh, interesting. So, you're saying if I go to this class…
**GZ Gregor Zeitlinger** 14:09 And the initialize method, yeah.
**Trask Stalnaker** 14:25 Got it, okay.
Add resources to…
**Robert Niedziela** 14:51 Yeah, I have some scenarios where I really need some resource attributes also in client code. I mean, in custom agent code, we have And… well, I don't have access to it right now.
And the issue with resources is that it actually can be built from multiple detectors, right, and config, and the final resource Content.
Let's say… Can really be… It's one year.
**GZ Gregor Zeitlinger** 15:32 too far.
**Robert Niedziela** 15:33 You know.
**Trask Stalnaker** 15:36 Okay… And is that in instrumentation?
Code… Like we're seeing here with logging instrumentation code, or is that in, like, SDK configuration… Sorry, can you, explain the use case?
You are asking me, Trask? Yeah, yeah.
**Robert Niedziela** 16:02 Yeah, so, for example, I have actually two cases. One use case is, we are doing some, validation if Well, just for user convenience. It's not critical stuff, but, you know, it's some convenience for a user, so he knows up front that something is not configured good enough.
Right? Like, service name, for example.
The second thing is copying…
**Trask Stalnaker** 16:30 Can we talk about that one first, before we move on?
For that one, can't that be done in the SDK? Like, that's a startup.
validation. That… can that be done… during startup.
like, I know with the auto-configure… Builder here, let's see… Like, you've got a.
**GZ Gregor Zeitlinger** 17:03 Access to that.
**Trask Stalnaker** 17:05 Yeah, so let's take it in two pieces. There's the… existing auto-configure, and then there's the future declarative configuration, right?
Today, is that possible, using a resource customizer?
**GZ Gregor Zeitlinger** 17:26 No, you cannot do that, it's write only.
You cannot see what is currently there.
**Robert Niedziela** 17:38 the customizer in, in auto-config, I think it can… it can get the current resource, but anyway… You would have to run the last one, but I'm still Comparing, rather, to declarative config scenario, because, yeah, that's where the pain is for me, actually. Okay.
**Trask Stalnaker** 18:03 And so, in declarative config, weeh… Right now, all we have… Or that's proposed is, like.
Hey, here's the model, the declarative config model that's going to be processed.
You don't get the end result.
**Robert Niedziela** 18:26 Yes, because the workflow, unless I'm mistaken, the workflow is, first we parse YAML to model.
Then we, give a chance to run customizers on top of it.
And then, research detectors are run.
**GZ Gregor Zeitlinger** 18:49 And user detectors can… The entire creation is run after you had the chance to modify the model.
**Trask Stalnaker** 18:58 I see, Fair, so… Validating… resource… resources… So… possible… And auto-configure… the, add resource customizer… in declarative… Config… Resource Detectors run after… YAML, model… Customization…
**Robert Niedziela** 20:24 Exactly, and they can actually change the attributes, right? Right, right.
And in detectors, you don't have access to current resource, you just can create a new one that is then merged with the others by framework.
**Trask Stalnaker** 20:52 Okay.
Okay, cool. I just want to get it down kind of clearly in a way that we can… Explain to Jack.
Did you have another use case?
**Robert Niedziela** 21:06 Yes, one more, I have custom span processor, that… which I… which is copying some resource attributes into, span attributes, and… yeah, I need the resource.
instance there as well.
**Trask Stalnaker** 21:28 So… Yeah, our resources really… read-only? I mean, write, not even read-only, like, in the SDK?
from the SDK, you can't get… Your resources.
Cause, like, I… this one… This one is different. This is actually, like, we want to expose resources to instrumentation.
Which is… a bigger deal, because resources are kind of SDK concept.
These ones, I feel like… Shouldn't be so hard.
Like, why…
**GZ Gregor Zeitlinger** 22:27 Are you asking, if you can get access to the resource from inside the SDK?
**Trask Stalnaker** 22:36 Yeah, or, like, if you have… like, I'm wondering why there's not a Git resources… Because it's the audience.
**GZ Gregor Zeitlinger** 22:44 down further, are the resources part of the individual provider, so tracer provider.
Has it, and if you use wild reflection, you can get access to it, and it's also done in tests, but, That's, a terrible solution, I think.
**Trask Stalnaker** 23:06 Yeah, I mean, we could… have OpenTelemetry SDK, could have a GetResources… method.
**GZ Gregor Zeitlinger** 23:18 That would be possible.
It's similar to how auto-configured SDK has it for, Many, use cases.
**Robert Niedziela** 23:49 It would be great.
**GZ Gregor Zeitlinger** 23:53 I managed to, create a PR today that, has the same functional behavior as without declarative configuration, so that you have it in the auto-configured SDK, and you don't have to call the resource provider twice.
So, I like the implementation, Cool. It's just the… the conceptual discussion that… that is, what we need first.
**Robert Niedziela** 24:20 So, you already created the PR with the changes?
Or you are going to… because… okay, I'll take a look at it.
**GZ Gregor Zeitlinger** 24:27 working.
I think you are… you also created a PR, Robert, but I found a better solution, I think.
**Robert Niedziela** 24:34 That's good, that's perfect.
**Trask Stalnaker** 24:38 What PR, Gregor?
**GZ Gregor Zeitlinger** 24:42 It's the one that is, that you just saw, just the link at the top of the screen.
Return… re…
**Trask Stalnaker** 24:51 Oh, did I just close it?
**GZ Gregor Zeitlinger** 24:53 Maybe.
**Trask Stalnaker** 24:55 Probably. Is it a Java agent?
**GZ Gregor Zeitlinger** 24:59 No, no, it's SDK.
**Trask Stalnaker** 25:00 SDK, okay.
**GZ Gregor Zeitlinger** 25:05 Was just the one linked to this issue.
**Trask Stalnaker** 25:09 Oh, this. Yes, I see.
Return resource…
**GZ Gregor Zeitlinger** 25:14 Yeah, this is the one from today.
**Trask Stalnaker** 25:17 Auto-configured…
**GZ Gregor Zeitlinger** 25:23 There's a lot of reflection going on. The actual logic is in the declarative configuration Java.
Now, this is a context object that is just for passing it around internally.
**Trask Stalnaker** 25:49 Okay.
**GZ Gregor Zeitlinger** 25:50 There's… here, there's a new method that is create with… yeah, exactly. That's the one that is,
**Trask Stalnaker** 25:58 Oh, I see. And you can return both.
Yeah, the… Open question… I have… is how… Does, upcoming entity… Work, affect this… Because… I think… The proposal is to have an entity provider, potentially, on that OpenTelemetry SDK.
And I… Yeah.
Josh Suresh has created a proof-of-concept pull request for entities.
**GZ Gregor Zeitlinger** 27:02 I've, looked at that because, for the extended open telemetry, I piggybacked on that.
And, I think the entities are in the hotel itself, using this extended open telemetry.
Idea.
Yeah, I think that's the one.
Can you look if there's an extended open telemetry?
**Trask Stalnaker** 27:29 Yeah, right here.
**GZ Gregor Zeitlinger** 27:31 app.
**Robert Niedziela** 27:31 Sorry, you're asking me something? I…
**Trask Stalnaker** 27:35 No, no.
**Robert Niedziela** 27:35 No, okay.
**Trask Stalnaker** 27:37 We're looking at, how entity provider If that will…
**Robert Niedziela** 27:44 I will have to drop off in 2 minutes, because I have a conflicting call, and… Yeah.
**GZ Gregor Zeitlinger** 27:49 Okay.
**Robert Niedziela** 27:50 Just for information.
**Trask Stalnaker** 27:52 Thanks.
**GZ Gregor Zeitlinger** 27:53 Thanks!
**Trask Stalnaker** 27:54 So the proposal is this is an actually an API concept.
Which… Elevates it even higher.
Question is, okay, so we can… Problem is, it looks like it's… Right… Only… Remove entity, attach, or update entity.
So it's not giving you a read view, which is what… You want… .
**GZ Gregor Zeitlinger** 29:00 I think, entities are opt-in, you can always… Stay on the resource.
Level, because entities are backwards compatible.
**Trask Stalnaker** 29:20 Yeah.
**Robert Niedziela** 29:24 See you guys, I'm dropping off. Bye.
**GZ Gregor Zeitlinger** 29:26 too.
**Trask Stalnaker** 29:38 Okay. Well, at least we captured… Some notes here… I… yeah, I think we'll… This is… I mean, makes some sense in my brain, but I… Don't know, yeah, we'll need to discuss with Jack.
Cool, let's move on.
More PRs that we should look at?
**GZ Gregor Zeitlinger** 30:21 Actually, for the next one, I have created a PR, and that's… it's just a question of how to… Get this right.
So here, after our discussion last week, I added an integration test, because there was no integration test for resource providers, and I… I put it somewhere where there is another instrumentation, which is not ideal, but I… I couldn't figure out a better way.
It's just, If you click on that, then you can see that I put it in the instrumentation API, which is kind of like a general thing, but it's.
**Trask Stalnaker** 31:09 Resource Task…
**GZ Gregor Zeitlinger** 31:20 It's in the OpenTelemetry API folder.
**Trask Stalnaker** 31:25 Oh, this is the bridge, yeah, or I would've…
**GZ Gregor Zeitlinger** 31:28 instrumentation for OpenTelemetry API.
**Trask Stalnaker** 31:30 Yeah, yeah, let's find a better… We should be able to find a better place.
So… what is it doing? It's… Just verifying the base… Resources that are added.
That are always added.
**GZ Gregor Zeitlinger** 32:00 I think you already reviewed it before, Trask, it's just the test that was added.
**Trask Stalnaker** 32:06 Yeah.
Just thinking where… Jay, you've been all around the tests lately. Any thoughts?
**Jay DeLuca** 32:20 I didn't even know about this particular directory.
**GZ Gregor Zeitlinger** 32:26 Your meeting was short, Robert.
**Robert Niedziela** 32:28 Yeah, actually, we agreed that probably there is no agenda anyway, and we canceled it, and yeah, I just got back here.
**Jay DeLuca** 32:38 What about, yeah, what about the Java agent tooling?
**GZ Gregor Zeitlinger** 32:42 Cannot hear you, can you hear me?
**Trask Stalnaker** 32:44 Hi, we can hear you.
**Jay DeLuca** 33:11 What else is in that tooling? I feel like I was in there recently for something else.
**Trask Stalnaker** 33:18 So the… I wonder if the problem with the tooling Does the tooling… When these tests run, do they pull in integration, instrumentations?
**GZ Gregor Zeitlinger** 33:33 Now I can hear you again, but I couldn't hear you before.
So, what is happening here is that the tooling is running a customizer.
And the customizer itself is not run in the resources, instrumentation, that's why the… All tests cannot be in the resources.
**Trask Stalnaker** 34:01 Why can't the resources… Does this run like a normal, full Java agent test?
**GZ Gregor Zeitlinger** 34:12 No, it's library. It's not Java agent.
**Trask Stalnaker** 34:16 Oh, library! Oh, okay.
And we could have a resources… Java agent testing.
No.
**GZ Gregor Zeitlinger** 34:31 Oh, it's… I didn't know that this is an option.
**Trask Stalnaker** 34:35 Yeah, I think we have a pattern, Java agent testing… Maybe. Maybe not.
**Jay DeLuca** 34:47 We usually have, like, a… a lot of times we'll have a Java agent, a library, and a testing… module within an instrumentation. Is that what you're thinking?
**GZ Gregor Zeitlinger** 34:56 No, it's more that if you only have a library instrumentation, but you have a Java agent test.
This… I have not seen this pattern before, but that does not mean it doesn't exist.
**Trask Stalnaker** 35:10 Yeah, I'm not finding it, so it probably doesn't… And the… the reason is because all you have to do is include that… there's zero bytecode instrumentation, you just… the agent just needs to include that.
module, the resource detector, and an.
**GZ Gregor Zeitlinger** 35:33 Customizer.
**Trask Stalnaker** 35:35 Yeah, automatically gets registered.
So… and… but you want to… Are you specifically wanting to test this library instrumentation under the Java agent?
**GZ Gregor Zeitlinger** 35:59 No, actually, I want to test the class under Java Agent Tooling.
But Java agent tooling does not have the capability to run integration tests.
**Trask Stalnaker** 36:11 Resource, okay…
**GZ Gregor Zeitlinger** 36:14 Because it does not have the right, Gradle plugin.
**Trask Stalnaker** 36:20 And so, what are… what is this doing here? Can you remind me? Oh, add.
**GZ Gregor Zeitlinger** 36:27 Two detectors if they're not present, because they're, like, basic detectors, so that, you have at least something to troubleshoot if the user has not provided anything at all.
**Trask Stalnaker** 36:41 I see, and how did we get these… on the… in the Java agent… How do we get them in the Java agent when declarative configuration's not used?
**GZ Gregor Zeitlinger** 36:54 Resource detection works in a different way, for short, so it's hard to compare.
**Trask Stalnaker** 37:01 I guess what I'm wondering is why, Can this… Declarative configuration support live in the library instrumentation itself?
So that people using… Library instrumentation also get declarative configuration support?
**GZ Gregor Zeitlinger** 37:26 We could, it's more a question of if we want, this is more… so this is a question of, is it a concern of the library to make sure that you have those detectors?
So this is the first question, and the second question then would be, Would we still want to have an integration test, if, we put it in, the… Resources project and run it as an… As a unit test.
**Trask Stalnaker** 37:57 So we definitely, I mean, as far as tests… It's where we have the smoke tests. That's a decent place to put this kind of thing.
Where, you know, it's like, hey, we wanna… Check the whole package.
**GZ Gregor Zeitlinger** 38:16 I looked there, I couldn't find anything. If you have a good place, then we could also put it there.
**Trask Stalnaker** 38:23 Let's see what we've got… smoke tests…
**GZ Gregor Zeitlinger** 38:27 I think I came to the conclusion that this is, doing a matrix test across a lot of, application servers.
**Trask Stalnaker** 38:37 Some of them are, like, the… Some of them are, but some of them aren't. Like.
This is just, like, a simple… Test that tests… it's kind of an integration test for this environment variable.
So you could… Add… just a new… Groovy, file here that is resource, detector smoke test.
**GZ Gregor Zeitlinger** 39:18 Okay, yep, I can do that.
**Jay DeLuca** 39:22 No groovy, no groovy, though.
**Trask Stalnaker** 39:25 Do we have.
**GZ Gregor Zeitlinger** 39:28 Yeah, groovy was also what put me off, to be honest.
**Trask Stalnaker** 39:32 Do we have… let's see… I'm sure…
**Jay DeLuca** 39:41 None of them are in Java, huh?
**Trask Stalnaker** 39:43 Nooooo…
**Jay DeLuca** 39:45 Interesting.
**Trask Stalnaker** 39:48 I… Do as you wish, Gregor.
**Jay DeLuca** 39:55 I'll convert it after if you threw it in Groovy.
**GZ Gregor Zeitlinger** 40:01 I'll check if there's an impediment for using Java.
I'll try to do it there. Okay, cool.
**Trask Stalnaker** 40:10 For… as far as the library, like, supporting declarative config.
I mean, I like the pattern that… is happening over in Contrib, where, you know, you're adding support for declarative config to the resource library instrumentation.
Very good.
**GZ Gregor Zeitlinger** 40:49 This… this is package.
I think you mean resources.
**Trask Stalnaker** 40:53 Whoa.
Oh, okay, so it's different. Let's see, do we have… that's a good…
**GZ Gregor Zeitlinger** 41:02 I think this was merged.
Yeah, I think that's the one.
**Trask Stalnaker** 41:19 Yeah, I mean, but essentially, I think, yes, it would… it is good if the library… if the declarative config support can be baked into the library instrumentation.
And then the Java agent can just piggyback on that support?
**GZ Gregor Zeitlinger** 41:43 Yeah, it's possible. As I said, it's a question of whether the resources library itself should have the responsibility to add distribution and service.
**Trask Stalnaker** 41:55 Oh, oh, I see it. That's the question. Gotcha.
**GZ Gregor Zeitlinger** 42:00 It's only about that.
**Trask Stalnaker** 42:02 Okay, so it's Distro Name… Yeah, so distro name, distro version, I agree, that's 100% Java agent responsibility.
This one… I'm a little more confused about… Because we have service resource detector…
**GZ Gregor Zeitlinger** 42:29 Yeah, the detector is there. Here, it's a question about adding it by default, if not specified.
**Trask Stalnaker** 42:34 the model!
Oh, sorry, I'm… yes.
It's amazing.
Because we don't… Oh, because it's not picked up.
Because the… the SPI only makes it available with a name.
That then users can use, but they're still not… it's not automatically picked up unless you explicitly add it.
Sorry, it took me a long time to catch up to you there. Okay.
Yes.
This makes sense.
Let's just, yeah, just if you can add, I do think the, smoke test is a good place for testing it.
And then, yeah, let's skip that.
merged.
Oh, lots of code.
What do we got?
Do we get a J approval on it already? Yes. Excellent. Okay.
Cool, I will merge it once the, Once the smoke test, you get that figured out.
**GZ Gregor Zeitlinger** 43:57 I'm moving down the next one down, because I think we don't have time enough for…
**Trask Stalnaker** 44:02 Okay. Discussing that.
**GZ Gregor Zeitlinger** 44:05 Maybe also not for the next one, but at least we have the right people in the room for that.
**Trask Stalnaker** 44:12 Map enabled and common enabled.
**GZ Gregor Zeitlinger** 44:15 Yeah, we discussed this already, and then we… decided to postpone it, but I have figured out that I want to have to settle for Milestone 1, so it doesn't make sense to postpone it indefinitely.
This is about the question how, we should say that, All instrumentations are enabled by default, so… a debug setting, mostly. And in particular, we were discussing whether this is really a common setting, or if it's a setting that is for Java agent, for Spring Starter.
Possibly for native instrumentation, and we did not arrive at a final Conclusion.
**Trask Stalnaker** 45:06 Did we have… yeah, oh, here we go, our… we were discussing, I think…
**GZ Gregor Zeitlinger** 45:13 Exactly, this common…
**Trask Stalnaker** 45:20 I just want to capture, at least we can capture so we can continue on.
the discussion, Okay, let's try to make sense of… Option 1… Java Commons… Agent… So in this case, we are saying, essentially… It is a agent… specific option…
**GZ Gregor Zeitlinger** 46:26 So, actually, two things. One is, Where the default setting should be, and we also, talked about where the per… Instrumentation setting should be, and I think this is where I, had an argument later, or I found an argument later, after our discussion, that it's good to have it in the instrumentation itself, because then native instrumentation Would be entitled, to pick this up.
**Trask Stalnaker** 47:04 Right, right.
**GZ Gregor Zeitlinger** 47:09 So, I think the default enabled, I… I have less an opinion about.
Because that's just one setting that you set once, and it's, it's easy to, exchange agent with Spring Starter there.
**Trask Stalnaker** 47:31 use… let's see, so we've got Java Agent… Spring Group Smarter… Native Instrumentation… .
**GZ Gregor Zeitlinger** 47:46 Quarkus, maybe, as well? I don't know much about Quarkus, but I think it… Probably also.
**Trask Stalnaker** 47:59 Although, almost consider cork… well, I guess Corccus is kind of maybe not native instrumentation. It's kind of native, kind of not.
Nice.
So… So, we're… For that to happen, we would not have… that…
**GZ Gregor Zeitlinger** 48:59 Are you changing enabled to disabled on purpose?
**Trask Stalnaker** 49:03 Maybe That's a different question, though, let's not… No.
So we've got… Default…
**Robert Niedziela** 49:24 Sorry for the question, but what do you mean by native implementation?
**Trask Stalnaker** 49:30 Library, like, Elasticsearch that uses, they have the OpenTelemetry instrumentation right directly in the…
**Robert Niedziela** 49:43 Oh, okay.
**Trask Stalnaker** 49:43 Library.
**Robert Niedziela** 49:44 Okay, okay, thanks.
**GZ Gregor Zeitlinger** 49:48 And they can access, this, YAML file using the config provider API.
**Robert Niedziela** 49:54 Okay, cool.
**Trask Stalnaker** 49:55 Which is a big, yeah, improvement.
That we didn't have a config available to them before.
**Jay DeLuca** 50:06 I don't want to derail, and maybe this isn't the… I don't know, a related topic, but… We also have instrumentations that, while they're enabled by default, they don't do anything unless an additional flag is set, so, like… drop wizard views, I think? Like, I don't think we… It doesn't do anything except for capture, like, the internal view spans, and then you have to also enable the view stuff.
I don't know if we want to consider those types of use cases when we're considering the semantics of enabled or disabled, but… Just, just came to mind.
**Trask Stalnaker** 50:48 Yeah, I think that… In my mind, at least, that still fits into kind of the same structure. I see it as, The common view config is… that's gonna be a common setting.
And… The instrumentation would Still, we would just still leave it as enabled.
Unless somebody disables it explicitly.
**Jay DeLuca** 51:18 Yeah, I guess that gives you the ability to turn it all on and then disable certain instrumentations.
So… Okay, but I think it's probably not applicable to this particular conversation at all.
**Trask Stalnaker** 51:35 What were some of the other… So we were thinking, do we want… Right…
**GZ Gregor Zeitlinger** 51:46 What the other dimensions of the question?
**Trask Stalnaker** 51:50 Just seeing if we had captured anything before that I wanted to keep.
I'm not sure, because I kind of… I agree with you, I'm… I think at first, I thought that… It didn't apply to native instrumentation.
But I think that was too Java agent focused.
of a perspective, and I… think it is actually nice to have that. Now, whether everybody… all the instrumentation to support that is… A different question, but it, But I like leaving that possibility open.
So, what did… so… okay, so we can do that… We still have, Default. Enabled.
And default… enabled? I don't know what we do.
Cause how is that?
It's still, like, instant default.
instrumentation…
**GZ Gregor Zeitlinger** 53:21 If you want to have it explicit, then default instrumentation enabled by default would be… easier to understand.
But it's very long.
I don't know if it's instrumentation or the instrumentations, but that's… It's more a general thing if we pluralize. I think we don't pluralize.
**Robert Niedziela** 54:11 Do we need this by default? Maybe just instrumentation is enabled?
**Jay DeLuca** 54:18 Do we think that there might be any more than one mode? Like, are these, like, modes, kind of, like, where we have all of, like, with the default mode, and then we have, like, what we've been kind of referring to as, like, the debug, or selective mode, where, like, everything's off by default, and then you have to select… new ones.
I don't know if that might be more… Like, mode default or mode selective.
Yeah.
Or, like, or Moe, verbose.
**GZ Gregor Zeitlinger** 54:55 That's easier to understand.
**Trask Stalnaker** 55:03 I… I kinda… I could… I could get… behind that.
Cool, let's leave it there. I think we got some good notes and some… Some good ideas there.
**GZ Gregor Zeitlinger** 55:29 Should we discuss it again, or… Should I create a PR, and we see where it takes us?
**Trask Stalnaker** 55:36 I'm… Why don't… Yeah, I mean, if it… what would…
**GZ Gregor Zeitlinger** 55:43 It's not a lot of work to create the PR, it's just a couple lines of code.
**Trask Stalnaker** 55:49 Okay, yeah.
Sounds good.
Let's…
**GZ Gregor Zeitlinger** 55:53 Okay.
**Trask Stalnaker** 55:54 Go for it.
We're… alright.
**GZ Gregor Zeitlinger** 55:58 That's time.
**Trask Stalnaker** 55:59 Yeah, see you in a few minutes.
**GZ Gregor Zeitlinger** 56:02 Dear.
