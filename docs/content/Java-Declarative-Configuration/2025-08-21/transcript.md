SIG: Java Declarative Configuration
Date: 2025-08-21
Duration: 48 minutes
Zoom Recording URL: https://zoom.us/rec/share/J1YOWLP7DyDt_-A5kBbnfiHgTdvnZbJ5xXp4K2S3KUloclKfr_Hagc4E6mJdB_iN.ULpc4BwrPEUmM8Lo
============================================================

## Zoom Recording Transcript

**GZ Gregor Zeitlinger** 00:06 Bolts are beginning to stand, okay?
**Trask Stalnaker** 01:00 Hey, Krugger!
**GZ Gregor Zeitlinger** 01:05 Hello! Morning.
**Trask Stalnaker** 01:08 Good afternoon.
Evening….
**GZ Gregor Zeitlinger** 01:17 Afternoon, yeah. That is, right.
You've been quite active reviewing all the different pull request tasks. Thanks a lot.
**Trask Stalnaker** 01:41 Brian, yes. Thank you.
… Let's see… okay, this is for… oh, okay, this is for declarative config. Okay, cool.
So, what do we have? Alright.
Too many meetings. ….
**GZ Gregor Zeitlinger** 02:07 I actually hope that we don't need this meeting much longer, and we can fold it into our main meeting.
with the current, progress, I think… We will get there soon.
**Trask Stalnaker** 02:21 Cool. Yeah, I mean, this meeting has been very helpful. It's been helpful for me to get engaged and understand what's going on, and that helps me then to review the stuff.
Okay, true, true, … Is this one… oh yeah, both of these ICR4.
declarative config….
**GZ Gregor Zeitlinger** 02:47 Yeah, I have, still a topic queue, where is it?
**Trask Stalnaker** 02:53 I'm moving it down right now.
**GZ Gregor Zeitlinger** 02:56 Okay.
**Trask Stalnaker** 02:59 Yeah.
**GZ Gregor Zeitlinger** 03:00 Yeah, before we start on that, … Do you have any question on, something that I'm currently working on, a PR, that is… Better discussed here.
So that.
**Trask Stalnaker** 03:12 Yeah, let's… Let's… let's do that. Let's just go through, because I haven't… looked, or I looked at some of the follow-ups.
**GZ Gregor Zeitlinger** 03:24 Are you presenting, Trask?
**Trask Stalnaker** 03:26 Yeah, is it not showing?
**GZ Gregor Zeitlinger** 03:28 Yeah.
I just… Okay. Yeah, right, it says Trask up there, right?
**Trask Stalnaker** 03:33 Cool.
… So, let's… Actually, let's just go to… Okay, repo, pull requests… Let's start at the top. Oh, no, this is a new one, okay.
….
**GZ Gregor Zeitlinger** 04:01 So it usually says declarative config in the title.
I try to make that clear.
**Trask Stalnaker** 04:08 Bridge. Oh, yes, this was the config bridge. Okay, this is… let's see… So I copied from the agent… We can reuse it in the agent later. I see.
True, adoption.
Yeah, so let's talk through my concern… is… … So, just trying to avoid using internal, or at least long-term internal stuff.
… But I… that makes sense if it's… if we are… We could make the bridge… public in the instrument. So you're saying that there's a copy of this in the instrumentation repo already?
**GZ Gregor Zeitlinger** 05:14 Exactly, and I just added an additional constructor that was not needed in In the agent, but it's fully backwards compatible.
**Trask Stalnaker** 05:27 What's the declarative config? It's probably the same name over here.
**GZ Gregor Zeitlinger** 05:33 Yeah, it is.
**Trask Stalnaker** 05:35 Cool.
Okay, so….
**GZ Gregor Zeitlinger** 05:38 And….
**Trask Stalnaker** 05:38 is… Oh, it's in the extension API, okay. And it will be….
**GZ Gregor Zeitlinger** 05:46 And it will be moved to somewhere where the spring starter can access it, because it's also needed there.
Unless we are faster to move it into contrape.
**Trask Stalnaker** 06:02 Right. Now, would… so… it seems like it's not only Spring Starter, but we're saying, like, basically anybody who's writing a kind of reusable… … Resource provider would benefit from this?
**GZ Gregor Zeitlinger** 06:25 Yeah, I have implemented about 5 to 10 of those objects, and they all fit the bill. I was even thinking if this is something that should be part of the specification, but I think that's a little bit too early.
**Trask Stalnaker** 06:44 Yeah, … Yeah, I had a similar thought, like, that… Maybe it could be… in core, but I guess I'm okay with it not being in core, like, because people who are just… like, we do… the future really is declarative config.
So this is sort of a stepping stone.
Supporting both.
And so, okay, I like that. I like that plan. Yeah, I didn't… I didn't feel like… I don't feel like Contrib is the right place for the bridge, but as long as we have a long-term plan to move it to the instrumentation repo, I like that.
**GZ Gregor Zeitlinger** 07:34 Yeah, I guess….
**Trask Stalnaker** 07:35 That would be free.
**GZ Gregor Zeitlinger** 07:36 I guess I cannot use it right now, and from… from the instrumentation, because it's not accessible there. But later we could.
**Trask Stalnaker** 07:45 Oh, yeah.
Yeah, I think it would be okay, unless we can add it to, … the later agenda to just check with, Lori… move… Okay.
**GZ Gregor Zeitlinger** 08:37 Courtney?
**Trask Stalnaker** 08:38 … So, I'm good with that. We don't need to change anything here. Let's see if I had any other… … Okay, yes, so we're good here.
Okay, cool. I will look over it, Ian, I forget if I had completely… Reviewed everything.
Jeez.
Okay, so that was that. Let's look at… Declarative config for baggage.
Yes, that's good.
Yeah, I added a comment over here, we'll… have to discuss with, them. Okay, we can resolve that.
I declared a config for… oh, okay, I approved it already, so we are good to go there. Oh, except… We've got a lot of… Test… we've got test failure problems in this repo right now.
**GZ Gregor Zeitlinger** 09:52 I, I, I created a different pull request to address, the… Blakey test.
**Trask Stalnaker** 09:58 Oh, cool. So let's try to get that in, and then we can rebase this one.
**GZ Gregor Zeitlinger** 10:05 Yeah, this is the first one. That is fixing it, hopefully.
**Trask Stalnaker** 10:11 Jeez.
Given requirements. Expected actual to be empty.
Actual, which is empty, to contain… Key… key, key. Got it. Okay.
Let's been processor first.
**GZ Gregor Zeitlinger** 10:45 So we have a very, low… frequency for exporting, and I'm thinking, that the order actually matters And because we're adding… we have been adding the baggage processor last.
We did have situations where the item was exported before the baggage could have been added.
If I understand this correctly.
**Trask Stalnaker** 11:17 But I mean, the order of the span processor here won't… effect.
what gets exported, right? Because all the span processors are going to be run before export, regardless of their ordering.
**GZ Gregor Zeitlinger** 11:36 If that is true, then we have a different problem, right?
**Trask Stalnaker** 11:45 One thing I do for trying to reproduce these, sporadic failures, I was working on this yesterday also just because there's… there's some other… there's another failure that, could be related to Jacoko… I create, like, a… Stress test, and just add, like, a huge matrix.
So it'll run, like, a hundred of these in parallel.
So it's more likely to exhibit the flakiness.
….
**GZ Gregor Zeitlinger** 12:22 That's a good idea.
**Trask Stalnaker** 12:24 They're painful to debug. … What was this error? It's, like, actual, so… Mackage Customizer test… Line 92… 92… oh, that's probably… Different now… So, okay, you do have a weight.
Yeah, usually, like, await helps… Okay.
Yeah… do we think… let's, … Let's go back to the PR that we actually want to merge.
Let's just rerun… These, and see if we get lucky.
Oh, while we're here, oh, I'm doing… Let's see… Let me add this to… Oh, this is not… Prestonita, let's try to get that.
This was the more annoying thing, because when I've been putting things into MergeQ, They've been getting kicked out.
Okay, so we've got this one, we've got this one… end-to-end for… AWS….
**GZ Gregor Zeitlinger** 14:33 This is still a work in progress. It should have been actually a trial.
**Trask Stalnaker** 14:37 Okay.
Cool.
Let's go over to… misjudgmentation.
Shinar Repo… so I've got a… a couple of… Declarative configs… … Missing declarative config… Let's see… Okay, so that's… then… Let's see… Okay, let's look out, so… Attribute Resource Provider….
**GZ Gregor Zeitlinger** 15:27 Yeah, there were some questions about, visibility and style.
**Trask Stalnaker** 15:35 So, create… Oh, okay, yes, yes, so you ended up adding these… I think when I was reviewing it, there was… Maybe there wasn't this one yet.
And this was just deferring, but yes, that looks good. Private… ….
**GZ Gregor Zeitlinger** 15:53 I just wanted to point out that this is not the style used by all of the providers, because some have the pattern that they statically initialize the resource, and Then I did not add a create resource.
I wasn't sure if… If, you also want to have this, in the same way for all of them.
**Trask Stalnaker** 16:20 … Let's see, create resource… No, I think it's okay. I think one of… no, this looks fine to me. … the… I did, … Oh, I think my comment, … Down here, about… was actually… Okay, yeah, so that makes sense.
Oh yeah, this one was actually… I meant to call out this line, not this line.
On the conditional resource provider.
Which is internal right now.
**GZ Gregor Zeitlinger** 17:11 Oh, okay, that's why I was confused.
**Trask Stalnaker** 17:15 Yeah, and the reason why I was kind of… drawn to that was this… it looked odd to me like this one is an override, because it's coming from Conditional Resource Provider, but this one is not an override.
At first I thought, oh, conditional resource provider was something in this repo.
….
**GZ Gregor Zeitlinger** 17:38 Hmm.
**Trask Stalnaker** 17:41 But yeah, just… I'm kind of… as we go through declarative config, I want to try to make sure that we have a… … Strategy, at least, for getting away from using internal stuff.
Once it's stabilized.
Since we would want other people implementing These are kind of templates for other people to implement resource detectors.
**GZ Gregor Zeitlinger** 18:12 Right, but I mean, traditional resource providers, nothing changed.
**Trask Stalnaker** 18:19 You're breaking up.
**GZ Gregor Zeitlinger** 18:24 Oh.
The conditional resource provider was not added in this PR.
**Trask Stalnaker** 18:29 Yeah, yeah.
… I just noticed it in this PR as I'm thinking about internal.
**GZ Gregor Zeitlinger** 18:37 Okay.
**Trask Stalnaker** 18:37 Package stuff.
So just as, so that we can consider it. I probably won't consider it until Jack is back, but as part of stabilizing declarative config.
I think it would be good to consider… This, and if we want A to be public and used. If we do, should we also add declarative config?
CreateResource method into it.
… But mostly just internal, whether it can be… non-internal, or if we should just duplicate this functionality, and I don't really remember… What… how critical this is.
If it's just a convenience class or not.
**GZ Gregor Zeitlinger** 19:30 It is really a small convenience class.
Let's see if I can… Just copy it here.
**Trask Stalnaker** 19:40 I can, I can pull it up.
**GZ Gregor Zeitlinger** 19:44 Okay, it just has a shouldApply method, that's all.
**Trask Stalnaker** 19:59 Okay, but the question is, is it being used… Like, do we need to… Is it imp… do we… Can we remove this usage over here?
Can we implement the resource provider over here without using conditional resource provider?
**GZ Gregor Zeitlinger** 20:29 So for declarative configuration, it's not needed, but for… for the… Legacy, it is needed, because, the SDK is actually, Checking for this, interface using instance of… So that's, maybe an unusual pattern, but this is what's happening here.
**Trask Stalnaker** 20:55 I see here… So, if it should not apply….
**GZ Gregor Zeitlinger** 21:10 Right.
**Trask Stalnaker** 21:12 Okay, so… yeah, I guess then, I mean, it looks like this is sort of intended to be used by… Third-party people?
Yep. Is that your understanding? Okay, so let's just open an issue, if you don't mind, about, making it, you know, public.
Or, you know, a path… having a strategy for making it public in the future.
**GZ Gregor Zeitlinger** 21:43 But is it really the right way? Because this is not related to declarative configuration.
I thought we would be moving to declarative configuration.
**Trask Stalnaker** 21:55 I see.
Yeah, so maybe we… maybe the right path is just to remove it, then.
Right, because it's not really necessary. You can… you can do the condition inside of createResource, right?
And just return an empty… resource.
If you want.
**GZ Gregor Zeitlinger** 22:21 That's… that's a difficult question. I know that, … I spent some time thinking about it, but I cannot give you the answer, but we can… I can create an issue where we can discuss this. That's… that's certainly possible.
**Trask Stalnaker** 22:35 Yeah, yeah, so I think, … Yeah, yeah, let's do that, and I'll think about it also.
But that makes sense, that helps me. Yeah, it's not declarative. We wouldn't… so we wouldn't do this at all. We don't need a conditional resource provider for declarative config.
**GZ Gregor Zeitlinger** 22:59 I guess that kind of surprises me, like….
**Trask Stalnaker** 23:02 Why do we only need it for… why is it useful for… The legacy config, but not for declarative config.
**GZ Gregor Zeitlinger** 23:11 Oh, I can answer that, … There, … no, it's not easy to answer. It's working in a totally different way.
**Trask Stalnaker** 23:21 Okay, okay.
Fair.
So, let's go… Back… oh, I see. Let me just add a comment. Sorry, I'm gonna… Okay… Missing declarative config providers….
**GZ Gregor Zeitlinger** 23:57 I'm wondering if maybe, your confusion is because the declarative configuration is reusing classes that are used before, maybe It would have been better to structure it in a way so that there is one common logic that is not implementing any interfaces.
Is that…?
That is usually a good pattern, and that's why I'm thinking that I should have done it here as well.
**Trask Stalnaker** 24:27 Can you explain that again?
**GZ Gregor Zeitlinger** 24:31 So, in the config provider, we have, code regard… related to both the old and the new interfaces, and that is making things harder to understand for the reader. And I could extract a common logic that is not related to the configuration part at all.
**Trask Stalnaker** 24:51 Config provider, that lives… that's in the….
**GZ Gregor Zeitlinger** 24:55 commission.
**Trask Stalnaker** 24:55 Instrumentation repo?
**GZ Gregor Zeitlinger** 24:58 Yeah, exactly.
Sorry, no….
**Trask Stalnaker** 25:03 Or do you mean component provider?
**GZ Gregor Zeitlinger** 25:12 So, the old interface is, … … It's a resource detector, and I think the new one is, … component provider. And, then we have the logic that is actually doing the extraction, like here, reading from the manifest. And having all those three aspects in the same classes It's probably confusing.
I just have to open it up how it actually works.
Let me just think about it again.
**Trask Stalnaker** 26:11 Okay.
**GZ Gregor Zeitlinger** 26:12 Can make it easier to understand.
**Trask Stalnaker** 26:50 Cool, cool. Okay. … Let's see… Okay, so I think we covered… Or somebody's taking notes, thank you.
Add missing… okay.
Okay.
**Jay DeLuca** 27:08 Yeah, those are all We've already looked at.
**Trask Stalnaker** 27:11 Awesome. Thanks.
So, moving instrumentation from contribib to Instrumentation repo.
Baggage… inversion stack trace….
**GZ Gregor Zeitlinger** 27:30 Yeah, I just listed all that we, have, … Based on your idea a couple of weeks ago.
**Trask Stalnaker** 27:43 So… the… things that I would prefer to stay in Priv would be stuff that is, sort of… The component… because we have the component ownership model over there.
So, like, GCP, AWS, Azure… … I could definitely… see baggage coming over.
… the rule-based sampler, especially after… I don't know… Either any of you have seen the, … Looked at simpler… I forget if this is updating the existing… Okay, no, it's a different… Sampler in addition to the rule-based one. Okay.
… But the rule-based one… I'll just highlight my favorites, or the ones that I think are most… Useful.
… This one, maybe eventually, after it.
the spec stabilizes, but for now, I like the component ownership model, because there's some folks with good expertise over here.
**GZ Gregor Zeitlinger** 29:17 Let's what pronounce books over here?
**Trask Stalnaker** 29:27 Stock Trace… Birds fans… This would probably be the… First, the two that I would most specifically Feel good about moving over.
Especially with, with declarative config, this is gonna be really awesome, really useful for people, the declarative, rule-based sampling.
Does that align, Gregor, or were you wanting to move more stuff? Was there an advantage for moving more stuff over?
Oh, I think Gregor froze.
**Jay DeLuca** 30:23 Yeah, I think so.
**Trask Stalnaker** 30:38 Alright, now we got 2 Gregers.
**Gregor Zeitlinger** 30:59 Yeah, can you kick the other one out?
**Trask Stalnaker** 31:02 Oh my god.
**Gregor Zeitlinger** 31:03 ….
**Trask Stalnaker** 31:04 I mean, I can, but it would take a couple minutes. I gotta… Pull up the, … meeting… owner ID thingy. Can we just leave… we'll just leave it. It's not harming anything.
So I was asking Gregor,
**Gregor Zeitlinger** 31:27 Just kidding.
**Trask Stalnaker** 31:28 So… Were you wanting… was there an… is there an advantage to moving more stuff over?
Were you wanting to move more stuff over?
**Gregor Zeitlinger** 31:39 It was your suggestion.
**Trask Stalnaker** 31:43 ….
**Gregor Zeitlinger** 31:47 I guess for easier maintenance, but I can't remember.
**Trask Stalnaker** 31:52 Okay.
So I like… I mean, we… I like moving baggage and sampler over. I would support that today.
We can ask… in general… Okay.
Yeah, I guess, … Whoa… I do like the component. I mean, we would need to probably add component ownership model in instrumentation. I think it's fine, until… until I remember what my prior self … why I wanted to move them.
We're gonna leave it as is.
How JWC uses system properties implicitly?
What does this… is this… You, Gregor?
**Gregor Zeitlinger** 33:14 It's restarting my computer.
**Trask Stalnaker** 33:17 Oh, okay.
**Gregor Zeitlinger** 33:20 Oh, yeah, now I remember. Couple weeks ago, … We discussed, … how the JDBC driver is a little bit special, because it relies on global open telemetry.
… And, … I was making the claim that it's also using system properties, and if it does.
Then it also should support declarative configuration.
And I double-checked, and it actually does, and we have not discussed further until that… Oh, since then.
**Trask Stalnaker** 34:02 Okay, yeah, so the JDBC, instrumentation, supports… also injecting not using the global as well. Like, there's kind of, the global is just a fallback if you are using SPI and don't have a chance to inject the OpenTelemetry instance.
… So, in that case… It's… Going to be… I don't know how to use declarative config, or in that case.
But we definitely could support declarative config in the… What we would consider normal approach, which is… injecting the OpenTelemetry instance into the instrumentation.
**Gregor Zeitlinger** 35:03 … Yeah, and… what, I… picked up from Jack is that we could have an extended global open telemetry.
And that extended global open telemetry would give access to the config provider, so regardless of how you pass this, … Extended open telemetry? No, not extended global, extended open telemetry.
How you pass it, global or directly, the instrumentation could get the declarative config data.
Out of it.
**Trask Stalnaker** 35:49 I see. So, the global open telemetry, if it's instantiated by the SDK, It will look for the system property that says where declarative configuration YAML lives, and then it would… and then it loads the YAML and instantiates it from there.
**Gregor Zeitlinger** 36:09 Right.
And with the extended global open telemetry, it would return an open telemetry, where you can extract, the… Configuration data out of.
And I have created, two pull requests in, the SDK repository.
Which, both, achieved the goal. … And, yeah, they have not been reviewed so far.
**Trask Stalnaker** 36:43 Okay, so we've got this one… this one?
**Gregor Zeitlinger** 36:52 Recording in progress.
**GZ Gregor Zeitlinger** 37:00 Now I'm back.
**Trask Stalnaker** 37:02 Okay.
Let's see if you're criteria with….
**GZ Gregor Zeitlinger** 37:05 And this is my first attempt.
And this, … is making, an API change, and, … then I figured out a way how this can be done without an API change. This is the second one, the alternative. It's a little bit… Harder to… Understand?
… But it doesn't need an API change.
**Trask Stalnaker** 37:34 Okay, so we've got… Extended open telemetry, yep, that makes sense.
**GZ Gregor Zeitlinger** 37:41 Yeah, this part is easy, but the SDK, the SDK… cannot be extended, because it is final, so you cannot have an extended OpenTelemetry SDK.
**Trask Stalnaker** 37:56 Okay.
So I assume you're doing, like, a delegation model, then, to it?
**GZ Gregor Zeitlinger** 38:05 It's, it's storing, the… the… The extended one in… An object that is typed with object, and then you have to make a cast to it.
This is, from OpenTelemetry SDK, exactly what you're looking at.
**Trask Stalnaker** 38:26 Yeah, let me unsee… Oh, I see. OpenTelemetry SDK is… I think that's what you're saying. It's a… final class.
**GZ Gregor Zeitlinger** 38:50 Right. Because we don't want users to implement their own I think that was the idea.
**Jay DeLuca** 38:58 Are you in the right repo?
**Trask Stalnaker** 39:00 iron.
Thank you.
Final class, I see, so we can't… Oof.
Okay, so we… So instead….
**GZ Gregor Zeitlinger** 39:27 You should see, the change that I did to the base class, if you go to, … OpenTelemetry SDK, I think it's on the left side.
Yep Yeah, okay, it does not have an object, but with shutdown, because the shutdown part needs to be called.
So it's, implementing, … Inheritance manually for this class.
**Trask Stalnaker** 40:14 Indeed.
So we've got… So, what does somebody do… how do they get access to the extended… 1… So this is exactly the problem.
**GZ Gregor Zeitlinger** 40:34 from method.
**Trask Stalnaker** 40:40 So the… you have extended open telemetry.
Okay, so… you… and you cast it to… Why….
**GZ Gregor Zeitlinger** 41:09 So you cannot make an instance of, that is, the problem.
You have to say, from, … SDK, and then you have to see if NUT is returned or not.
**Trask Stalnaker** 41:22 So, I'm not seeing anything that implements… Extended open telemetry.
So we've got this new interface.
Does anybody… Implement this interface?
**GZ Gregor Zeitlinger** 41:48 I think you just headed over, … So I have to open it again.
**Trask Stalnaker** 41:56 Oh, I see, sorry, sorry, yes, I see it. Extended open telemetry SDK… Extends… Extended open telemetry… Got it, okay, and… from… Should this… This should implement… this, … git config provider.
Right.
**GZ Gregor Zeitlinger** 42:30 Yep.
**Trask Stalnaker** 42:32 Okay, that's just a to-do still.
**GZ Gregor Zeitlinger** 42:38 That's basically what you have it for.
**Trask Stalnaker** 42:42 Right, what I'm saying is I was expecting to see… … This, implementation of this method over here.
**GZ Gregor Zeitlinger** 43:15 Okay, now I have my IDE, … Open, so it's an obfuscated extended open telemetry SDK, there it's implemented.
**Trask Stalnaker** 43:25 Oh, because this is still an interface.
I see.
Okay, so… that's still an interface.
**GZ Gregor Zeitlinger** 43:33 Do you have it on the left side, the….
**Trask Stalnaker** 43:36 Yes, and so, git config provider is over here. I see, okay, okay, thank you.
And….
**GZ Gregor Zeitlinger** 43:43 It's a little bit, contrived, I admit.
**Trask Stalnaker** 43:48 Okay, … Now, what about, … … Instead of… extended… I know we… we kind of… we talked about having this extended OpenTelemetry instance, which was nice, a nice idea.
But….
**GZ Gregor Zeitlinger** 44:12 Given the complexity there.
**Trask Stalnaker** 44:14 What about just adding, … So, we've got… Open telemetry… SDK… Oh, I see, we can't cast… OpenTelemetry is up.
… interface. I was… Thinking we could make, We could add a, like, a private, you know, package-protected method over here for git config provider, and just… To make people call it via reflection.
Or have one of those utilities, like we do in the instrumentation repo, internal… Yeah, that's all you work, ….
**GZ Gregor Zeitlinger** 45:08 Because we have the separation of incubating and staple.
And we don't want to add an API surface area for incubating Things.
And, Jack has established a pattern, where you, … do a call to an internal class, and that internal class uses reflection, and I'm also using the same pattern … Because this is, the established pattern.
**Trask Stalnaker** 45:50 What about, so we've got extended open telemetry, interface… … What if we… didn't do… this, and we… this… can… We make this extend… we can't make this extend that, is that…?
Problem with this new pattern.
We're ST….
**GZ Gregor Zeitlinger** 46:23 You mean why we cannot, extend OpenTelemetry SDK?
**Trask Stalnaker** 46:29 No, I'm… Could we add in here… could we make this implement our… OpenTelemetry, X.
Extension.
**GZ Gregor Zeitlinger** 46:42 Oh, no, this is an anti-pattern. Jack has done this a couple of times, but then he has been getting rid of it, because stable artifacts should not, depend on incubating artifacts, because that leads to problems. And this is… Nothing be avoided.
**Trask Stalnaker** 47:04 Yep, no, you're right, you're right.
Oof.
Yeah, this is… I… So, how much is this… is this blocking stuff today?
**GZ Gregor Zeitlinger** 47:28 No, it's not. This is, more like, … the icing. What do you say? The… the cherry on top?
**Trask Stalnaker** 47:36 Yeah.
**GZ Gregor Zeitlinger** 47:36 ….
**Trask Stalnaker** 47:37 Because… Icing on the cake, yeah.
**GZ Gregor Zeitlinger** 47:39 Icing on the cake, exactly. It's not a central part, but it's a complicated one, so it's good to discuss it so that we eventually find a solution for it.
**Trask Stalnaker** 47:51 Yeah.
Yeah, I don't… We can keep talking about it, definitely, … Maybe next week, if we've got time, we can go through it in some more… detail, because, yeah, it would be good for me to understand the… as I continue to understand the trade-offs.
and, how it works, and I can… I don't think we'll get it merged without Jack, But we can at least… Maybe iron out what we… Get some consensus before he's back.
**GZ Gregor Zeitlinger** 48:34 Huh?
**Trask Stalnaker** 48:37 Okay.
Cool.
Anything else, or shall we break?
**GZ Gregor Zeitlinger** 48:45 I think we can break, since we have another meeting in 10 minutes.
**Trask Stalnaker** 48:49 Sounds good. See you there.
**GZ Gregor Zeitlinger** 48:51 See you!
