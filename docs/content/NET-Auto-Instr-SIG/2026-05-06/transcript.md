SIG: .NET Auto-Instr SIG
Date: 2026-05-06
Duration: 43 minutes
Zoom Recording URL: https://zoom.us/rec/share/YrYm_PzSR8twqssOGtCrQPtmSzB49GW0rAmJDpK9Fpo-znR0K1mGtn0yCAgaNvZZ.XFxTW-fooZEVBhgc
============================================================

## Zoom Recording Transcript

**Piotr Kiełkowicz** 05:11 Hey, guys.
**Alexey Pukhov** 05:15 Bye.
**Zach Montoya** 05:22 Hello.
**Mateusz Łach** 05:37 Hello.
I can… I can share today. Second… Okay, Should we start with the usual agenda? I have only one thing, related to, opam and the initial support that Rasmus was working on. If Sieg would be okay with that, we'd like to make a better release.
So that, This is available to plugins as well.
So My name… Opinions? Any… are we fine with that?
So, once, Rasmus PR related to the… Oh… Related to the plugin extensions is merged. We would be interested in making a beta version released with initial support for Open.
**Zach Montoya** 06:52 Yep, no objections for me. Are there any other instrumentation libraries that have done this, or is this, kind of the first one to demonstrate it?
**Mateusz Łach** 07:05 I think there is a support in, in Java.
So… Yeah, I don't think we would be the first, but…
**Piotr Kiełkowicz** 07:15 I'm not sure if it is not a Splunk Distribution, the open client.
Okay?
for the Java, but I don't know details. So there is a chance that there are open telemetry in that kind of native distribution. It will be the first one.
**Mateusz Łach** 07:34 Okay, would that, would that change your opinion about the release, Zach? Oh, no.
**Zach Montoya** 07:38 I was just… I was just curious about, how much of it has been kind of explored, because I can imagine that, I mean, you guys have probably already encountered some differences or some expectations about, you know, what should be communicated or, like, the… Just, like, how op-amp would work with a SDK versus a collector, so… I mean, I just need to follow up if there's anything that's, you know, any changes or unexpected from trying to deliver this as an SD… in the SDK, but… Yeah, that's all. No real concerns.
**Mateusz Łach** 08:13 Okay, so, in that case, let me start with the open pull requests. So we have, we have… A lot of them, some of them are in draft for now, so… Yeah, so here we have one from Igor. So, Igor, any recent, In the recent changes in this one, do you want to discuss it?
**Igor Kiselev** 08:39 I have done some polishing based on that suggestion. Most of polishing was about adding few comments here and there.
And I think that it is ready to merge.
**Mateusz Łach** 08:52 Okay, so I see that Chris, proved it as well.
**Igor Kiselev** 08:58 So, the only exception would be if you'd like to take one more look and check if the documentation is good enough, or if you would like some improvements there.
**Zach Montoya** 09:09 Okay, yeah, I can, I can follow up with that today, and then, it's probably gonna be fine, and I can hit the merge button.
**Piotr Kiełkowicz** 09:17 If you can trigger the auto-merge and update the branches, when you are fine, it would be great if I need to make the batteries tomorrow.
**Zach Montoya** 09:28 Okay.
**Mateusz Łach** 09:30 Okay, so I'll skip the PRs that are in draft, unless someone wants to discuss their PR.
**Igor Kiselev** 09:41 So… Yes, I would like to… discuss a little bit more about, what we discussed previous time about Nuggets, so I, When you will open it. And my last one, PR, that is in draft today.
**Mateusz Łach** 10:02 Okay, so this one, right? Yes.
This one?
**Igor Kiselev** 10:06 Patience trampoline yep.
**Mateusz Łach** 10:09 Okay, so, yeah, so maybe I'll go from the bottom, So… And we'll come to your, here, Igor, if you don't mind.
**Igor Kiselev** 10:22 Ugh.
**Mateusz Łach** 10:23 So this one.NET Framework Redirection… redirection coverage.
**Igor Kiselev** 10:29 It's not ready, it will… if we can move it to a draft, it would be good, because it's currently draft, and… So…
**Mateusz Łach** 10:41 Okay, so…
**Igor Kiselev** 10:43 to add a test for already reverted change. So, an agreement right now that we will add a test, we'll see the test failed, and after it, we would start fixing.
Eat fruit, but we have a…
**Mateusz Łach** 10:59 Okay, so…
**Igor Kiselev** 11:01 Oof.
**Mateusz Łach** 11:02 So your suggestion was to move to draft for now, is that correct? Yes. Yeah. So let me add the comment, and I'll convert it to draft if I can.
Okay?
So then we have, Dependabot.
ER, nothing to discuss here? Have anyone had a chance to look into it? Okay, I see that Piotr started looking into it.
What about the failures? Pietro, did you have a chance to log into that?
**Piotr Kiełkowicz** 11:37 That's it.
**Mateusz Łach** 11:39 Yeah, I think I took a quick look, and and it was Ravid MQTest, yeah, so it seems like… There's a problem with this one. Okay, Piach, do you all… do you expect to have some time in a… probably tomorrow to look into that? What's the source of the failures here?
**Piotr Kiełkowicz** 11:58 I adapt, to be honest. There is kind of more important stuff that's playing with.
Okay.
**Mateusz Łach** 12:04 Okay, yeah, I'll try to miss Look in the next few days.
Okay, and then there is draft that you wanted to discuss, Igor, that we discussed last time, right?
**Igor Kiselev** 12:14 Yes, we discussed it last time, so, as I promised, I added a recommendation to original bug, so how it could be workaround, so my suggestion, either to close that and bug, as would not be… as… Would not be fixed.
Oh, still… take a decision at what time we would like to do what I suggested in my pull request. So, just to get some some… Agreement about should it be closed, should it be addressed later, and the same would be an answer for a bug.
Up to some level, or it would wait for iSpanner for us avoiding, reference ISPANT instrumentation at all after .NET 11 or .NET 12, I don't know, but still, it requires some communication with all levels.
So, not right now, but I'm just asking again that we need to take some decisions here.
**Mateusz Łach** 13:27 Okay.
Then we have… FT cars, PR… Sticker 1 to… Anything you'd like to… to add to what… whatever you already… Like described here.
**efshaikh** 13:47 No, so I'll try to add integration tests for… specifically for the native stack elements. That is the only thing missing. Do you think we should convert it to draft until that is there? What's the protocol?
**Mateusz Łach** 14:08 Yeah, not sure… what is, what is missing?
**efshaikh** 14:12 So, native stack work-specific integration tests will be needed. So, I'm exploring how to make the DSS fail, so that…
**Mateusz Łach** 14:23 Yeah.
Okay, yeah, so…
**efshaikh** 14:29 But in general, are there any questions, any feedback?
Anything that, you have any doubts, questions, queries around this? Because it's a big PR.
**Igor Kiselev** 14:42 I will definitely look and do a review for that pull request.
I'm… If anybody else would like to do it, it would be great, because a pull request is pretty complex, and require… So, knowledge a little bit beyond my normal knowledge.
**Mateusz Łach** 15:20 Yeah, so basically, it's like, what you are saying, Aptika, is that, like, It's almost ready, and you are right now working on a test, like, specifically.
**efshaikh** 15:30 intellect.
**Mateusz Łach** 15:30 Right.
**efshaikh** 15:31 Exactly.
**Mateusz Łach** 15:33 Yeah.
Okay, so if any of you had some time and could, To take a look and share some feedback, that'd be very, very helpful, definitely.
And Pietri commented about the missing integration test. Do we want to convert it to draft, or do we prefer to keep it as it is? I mean, this should be, like, ready to review, maybe not to merge without the test, but… And it should be ready to review, right? Yes. Maybe I'll leave it as it is.
Or no? No.
Okay.
Then we have something new from Igor.
**Igor Kiselev** 16:14 Small follow-up, mostly, I just resolved all issues that was pointed in a… in a late review.
So, the review has been done after the change was merged. So, most of them about using environment variables instead of direct string interpolation by CI, I applied it everywhere where it was reasonable in my pull request and in few other places where we use it, but I have not applied it Everywhere, because, when applying… when changing it from interpolation to environment variable would make, one, action split it into two.
just because we have different syntax in PowerShell for environment variables and Bash and otherwise, they are similar, and at the same time, that environment variables are just a way to pass data from one step to another step, and is not controlled directly from metadata… from pull request metadata. There is no actual risk.
So… Okay. We're ready for review.
Small, nothing critical.
**Mateusz Łach** 17:24 Thank you.
Yeah, then we have, this memory leak fix that was basically extracted from the previous PR from FTCA, right? So…
**efshaikh** 17:39 Yes, yes. So, I looked at the code, maybe, from ChatGPT, I like its idea, I'll just make that little change and we are good. It's… it's not related to the memory leak, but it's how we use the CCOM PTR, so I found those casts, their interpret cast and all that, a little dangerous.
So I fixed that. Okay. Yeah.
**Mateusz Łach** 18:01 Okay.
So I see that Piotr already approved that, so…
**efshaikh** 18:07 Yes.
**Mateusz Łach** 18:14 Yeah, so this is the plug-in extension point for a pump from Rasmus. We don't have Rasmus.
On the call at the moment, so this is, like, continuation… For the op-amp-related work that Rasmus is doing, so basically, giving the, the plugins a way to influence the configuration of Open client created, and then use the created Opum client, so… After this is merged, we would be, as I, mentioned at the start, we would be interested in making a Batteries, so that this can be… can be used in, In plugins, so… If you'd have some time to review, that'd be very helpful.
Okay, then we have another… Another Dependabot PR, which was not reviewed yet.
Should be straightforward, right?
Okay, then we have another draft from Igor.
And this is something new, right, Igor? Do you want to…
**Igor Kiselev** 19:37 Yes. So here is… I created a… review PR, let's say that, because I need a feedback. It is big and pretty complex. So, it continues of solving issues with up domains and with all the bad things that we have on .NET Framework. So, the most important thing, in .NET Framework, when we have a second wrap domain, in, by default.NET Framework try to optimize how it loads assemblies, and if, especially for SpanNet, if assembly is loaded from Gark, it tries to load only one copy of that assembly.
So, because we… different application may have a different redirection and other things, and we add additional reference to the GAC Assembly, we break the plan of .NET Framework, how it tries to load assembly, and that's why we have in previous, different types of issues with, NET application, and with iSpot application, that's why we applied previously the single domain, environment variable, and then I optimized it to make it all the time. So, in my new pull request, I created a way to, configure assembly binding, but it still not resolved any of that option still not resolved original problem. So, I… with both of that, each abdomain would have its own system web, or in some cases, the system web would be shared, and all other assemblies. So we still create much more memory, pressure on processors, than would be without our presence if a process is multi-host.
That hosts more than one website.
So, Android calls of it because we add assembly reference to, customer assemblies to GUC assemblies and other things.
So, here I thought, okay, maybe we could resolve it completely different way, and we don't need to add a reference at all to original assemblies. And we can do it, so it would, the cost of it would be a little bit slower, instrumented, of instrumented method. So, instead of reference.
instead of reference all assembly, I created the trampoline types in Mascot leap.
And that have the same shape as our, normal, as our normal, type to which we add reference to. And so, the trampline type would be a middle ground between our instrumented methods and our open telemetry auto-instrumentation code, called through reflection.
visit, I was able to verify that, So, now we don't add any reference to Gok assemblies, everything works all the time, it should work even without registering assemblies in GOC, even if we have not applied any hacks to up-domain creation. So, okay, my last option still may be useful, because in some cases, it may help, unify, and solve potential assembly conflicts, but Even in simple case, it would be not… even that would be not required.
and system web would have only one instance, and so on, so… please take a look, please share if you think it would be okay to merge. The main problem, it… it have a massive, change in different… in how we instrument, and it would make, upstream.
copy from Datadoc, even harder, and probably not possible in some cases at all. So, it's the main… worse, bad thing. Right now, it is, implemented only for .NET framework, just because for .NET Core, it is not needed at all, but I have a way how we could do it To make it more testable, and more… not a bump that works special way on .NET Framework, but an option that could be applied on either way, but with different defaults. And that code is mostly VIP-coded, so I done an architecture, I done a high-level guidance on what needs to be done. I have not… it was a… just a test of ideas that I have done in a Day and night. If we are interested in it, I would do a thoughtful review of it, and I would do some polishing on it, and after it, I would say that it is ready for review by anybody else. But right now, I need Not a review on a level how, if it works correctly, if it not works correctly, but on a level, yes, that approach may work, or no, we don't need that approach at all.
Thank you.
**Mateusz Łach** 24:57 Okay, thank you, Igor.
Yeah, and the last one is some actions cleanup. Okay, this one is… merged already.
Yes, moving on to issues, we have… Two new issues without… Without the milestone, this one seems simple enough.
Yeah.
Do we want to assign a milestone to this one?
**Igor Kiselev** 25:39 I don't have any preferences for it, and it… So… I'll blip.
**Piotr Kiełkowicz** 25:46 Vinix and help on that?
**Mateusz Łach** 25:50 Yeah, let's… Can do that.
**Igor Kiselev** 25:56 By…
**Mateusz Łach** 25:59 Okay.
Igor, you were saying some…
**Igor Kiselev** 26:03 Yeah. It was exactly… it was exactly that I'd like to ask you to set, to add something like help monitor, that anybody could pick it up.
**Mateusz Łach** 26:12 Okay.
And then this one.
Piotr, want to share some additional feedback, apart from.
**Piotr Kiełkowicz** 26:24 116, or 115, I do not remember that.
The closet, yeah.
**Mateusz Łach** 26:32 Okay.
**Piotr Kiełkowicz** 26:35 It is kind of… I… I was talking about this last time. There were some changes in the…
**Mateusz Łach** 26:43 Okay.
**Piotr Kiełkowicz** 26:44 internal SQL client code, and we need to adjust our reflection, and… I, of course, testing it this version manually, so… Okay, here is the results.
**Mateusz Łach** 27:02 Yeah, so that's all for the issues. We have no… New discussions, right? This one is probably pretty old.
Yeah.
Okay, this is closed, sorry.
And what else do we have?
So these are issues targeted for the next… For the next stable release, which are not assigned to the board, right?
So…
**Chris Ventura** 27:51 On the projects on the right-hand side, that's where you just need to add the project board.
**Mateusz Łach** 28:01 Yeah, so… Okay.
Do we want to assign it already?
Probably.
Right?
**Piotr Kiełkowicz** 28:13 It should be assigned, yes.
**Mateusz Łach** 28:15 Okay.
So… Yeah, so this one is already being worked on by Igor, right?
So… Assign it, and… this is in progress, Igor. Is that, correct?
Assumption, yeah, so… If you are open.
**Igor Kiselev** 28:35 request ready for review.
**Mateusz Łach** 28:37 Okay.
What about this one?
Something that we should clean up as well. Okay, I'll assign it to the board.
**Piotr Kiełkowicz** 28:48 And self-wanted?
**Mateusz Łach** 28:50 Yeah.
Done.
**Igor Kiselev** 29:07 Where you could also add ideal for previous, but ideal first commit.
**Mateusz Łach** 29:18 this one.
Out concept and good first issue.
Okay.
**Igor Kiselev** 29:26 Why? .
**Mateusz Łach** 29:28 Okay, and what about this one? Chris, you mentioned some specification issue.
Yeah…
**Chris Ventura** 29:45 Yeah, this is the long… Yeah. Debated, thing. Which one is our issue?
**Mateusz Łach** 29:54 Our issue is guidelines for stability.
**Chris Ventura** 29:59 Let's, take it out of 116.
At this point, I would say V-necks, while we're waiting for spec stability.
**Mateusz Łach** 30:13 Okay.
Should I add a comment?
**Chris Ventura** 30:21 Yeah, that's probably a good reminder.
**Piotr Kiełkowicz** 30:27 I don't think there is kind of good agreement on this auto plug, to be honest.
And the demand will be lower because we have go through the OpenTelemetry go through the process of moving to the… from the graduation to something else, or… I don't remember the exact names, but it was the main reason for this update.
**Mateusz Łach** 31:01 Okay.
This one needs proof.
Okay, and the last thing is to review the project board, so… And I think… That should be adjusted here.
Yeah, it seems to reflect the current states.
Anything else you'd like to discuss? Because I think that's… That's all for the standard agenda.
**Chris Ventura** 31:54 Yeah, I got a question. Pyotr, I don't… know if you remember what we had to change in our CI.
Because, Visual Studio 26 wasn't yet available on the Windows runner.
I'm asking because it's now the default on Windows Latest and Windows 2025?
**Piotr Kiełkowicz** 32:20 We are executing builds on Windows 2022.
Okay. And there is no… and there will be no Visual Studio 2016. Okay.
26.
**Chris Ventura** 32:32 Okay, so no changes until we update.
**Piotr Kiełkowicz** 32:35 Yes, and I'm not sure when it is going end of life.
Oops.
**Chris Ventura** 32:40 I read it, October of this year.
**Piotr Kiełkowicz** 32:48 So, I think it is dead.
No, sir, it is… security support is 5 years from now.
**Chris Ventura** 32:56 I… I thought I… so… regular support ends in October, and then I think GitHub had mentioned… They're removing the runner.
**Piotr Kiełkowicz** 33:12 Okay.
**Chris Ventura** 33:12 lately.
**Piotr Kiełkowicz** 33:14 If so, we need to update in this case.
**Igor Kiselev** 33:23 But then, from the previous screen, the board was named 114, and we already have 115 released, so I'm not sure if it was… Correct, not.
**Mateusz Łach** 33:33 Yeah, I think it's, like… Right, let me update the dots.
So, on the project board, right?
Okay, yeah, thanks, Gor, for… Or noticing that.
Okay, apart from that, anything else you'd like to discuss?
Okay, in that case, thank you all for attending, and, see you next week.
**Zach Montoya** 34:29 Thank you.
**Piotr Kiełkowicz** 34:29 Yeah.
**efshaikh** 40:25 Oh, yeah, mara.
