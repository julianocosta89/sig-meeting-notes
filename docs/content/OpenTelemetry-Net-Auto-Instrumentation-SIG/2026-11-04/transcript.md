SIG: OpenTelemetry .Net Auto Instrumentation SIG
Date: 2026-11-04
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Piotr Kiełkowicz (Splunk Inc.)** 04:49 Hi, guys.
**Igor Kiselev** 04:52 Oh.
**Zach Montoya** 04:54 Hello.
**eftiquar** 04:55 Yay.
**Piotr Kiełkowicz (Splunk Inc.)** 04:57 the Chrono Drive today? Sure.
Someone background task, too.
**Zach Montoya** 05:06 Yeah.
**Piotr Kiełkowicz (Splunk Inc.)** 05:07 Thank you.
**Zach Montoya** 05:33 Alright, yeah, let's get started. We can focus on this, this first, discussion topic.
Could've… config propagator schema… config spec says composite propagator is an array. Okay.
Yeah, that's…
**Carlos Alberto Cortez (Dash0)** 05:52 That's me. Basically, I wanted to double-check. I started to play with this, and I was comparing the implementation of this one with other languages, like Java or Python.
And it seems different to me, like, based on this, it should be a list, but I think it's treated as a map.
in .NET, you know?
Interesting. So that means… that means that the actual, declaration is different, you know?
**Zach Montoya** 06:21 Got it, so you're saying that… does that affect how it's, described in the YAML, is that what you're saying?
**Carlos Alberto Cortez (Dash0)** 06:28 Yeah, correct.
**Zach Montoya** 06:35 Okay, let's see… Where is… Do you have any links, into our repo at all? I can… I can go find it, but I'm just wondering if you have anything.
Okay, so in this example, this is a file-based configuration.
So you have propagators as a composite list.
So you can have a composite list, but it's string or null, and then you're saying that there's also just…
**Carlos Alberto Cortez (Dash0)** 07:40 Yeah, good for, yeah, not composite list, but composite, yeah.
**Zach Montoya** 07:44 Yeah, okay.
**Carlos Alberto Cortez (Dash0)** 07:49 I wanted to fill an issue on this, I just realized about this very recently, and wasn't sure.
**Zach Montoya** 07:55 Yeah, I think this is, yeah, I think this is definitely suitable to create an issue from.
Because I'm not sure… yeah, I mean, from this example, we use, We use, like, this file-based configuration to run through some of our integration tests for our implementation, but we may not be testing the, the propagators with, an array, so… I think that's worthy of creating an issue.
If you can… Like, summarize that.
**Carlos Alberto Cortez (Dash0)** 08:25 Perfect, okay. Yeah, if that's okay, I will do that then. I just wanted to double-check, not create, too many issues. But okay, I will do that, and I will publish in a PR later today or tomorrow, and see how that goes.
**Zach Montoya** 08:37 Okay, yeah, certainly.
**Carlos Alberto Cortez (Dash0)** 08:39 Thank you. Okay, I got to drop, I just wanted to come in and say hi about this. Thank you so much, Syrah.
**Zach Montoya** 08:44 Alright, yeah, thank you.
Alright, so let's… we'll have an issue created for this, Stokes… Cool. So now…
**eftiquar** 09:05 I just real one, we don't discuss the signal effects, issues here, right? It's… this is not the forum for that.
**Piotr Kiełkowicz (Splunk Inc.)** 09:14 Nope.
**Zach Montoya** 09:15 No.
**eftiquar** 09:16 Out of school. Okay.
**Zach Montoya** 09:19 Although if you want any input from me, I mean, I'm happy to provide.
**eftiquar** 09:23 Feedback. Okay, I can send it over to you.
I'll just send it in the chat, just take a look at it offline.
Oh, no.
**Piotr Kiełkowicz (Splunk Inc.)** 09:35 Particular now, the other meeting, the internal one.
**eftiquar** 09:43 Where should I send it?
**Piotr Kiełkowicz (Splunk Inc.)** 09:46 I'm telling that we have kind of internal meeting for this. This is kind of only Only for the open source stuff.
**eftiquar** 09:53 Nope.
**Zach Montoya** 09:56 But if you have… if it's based on this one, then yeah, I can still provide feedback if you, like, DM me or something.
**eftiquar** 10:04 dirt.
**Zach Montoya** 10:05 Take a look, but… Yeah.
**eftiquar** 10:07 Sure.
**Zach Montoya** 10:09 Okay, cool. So let's go through the open pull request. Let's see… So, we have some bumps, native compiler warnings. Yep, sure, we can, we can look at that.
ADONet's instrumentation issue.
Okay… And then we have a continuous profiler stack capture.
Is this from a, Codex?
Scan.
Yeah.
**Piotr Kiełkowicz (Splunk Inc.)** 10:41 As I remember, it is limited now to beef, 500, let's say.
**eftiquar** 10:50 No.
**Piotr Kiełkowicz (Splunk Inc.)** 10:51 Rows per stack, so…
**eftiquar** 10:54 So, Piotr, you want me to review these?
**Piotr Kiełkowicz (Splunk Inc.)** 10:56 Sure.
**eftiquar** 11:00 Boy.
**Piotr Kiełkowicz (Splunk Inc.)** 11:02 500 frames per stack, and kind of a couple other limits, so we'll be safe, and we'll not consume a lot of memory. But if the customer or a user have more than that.
In his process, it has probably a bigger problem than our continuous profiler.
It's kind of really hardening stuff.
**Zach Montoya** 11:33 Okay, yeah, I appreciate, maybe, yeah, F2 car to take a look. I'm not too familiar with the continuous profiler bits in this.
**eftiquar** 11:40 But, Piotr, did you request review from Bonsai? I didn't receive any notification.
**Piotr Kiełkowicz (Splunk Inc.)** 11:45 Not directly, it is kind of just OpenTPR on the GitHub, so if you're not watching it.
You can do that.
**eftiquar** 11:55 If you want me to look at it, it'll be good if you just explicitly… sometimes I just… Miss this.
**Piotr Kiełkowicz (Splunk Inc.)** 12:02 Sure.
**eftiquar** 12:03 If there is something in Continuous Profiler that needs my attention, please.
**Piotr Kiełkowicz (Splunk Inc.)** 12:08 Sure.
**eftiquar** 12:10 Thank you.
**Zach Montoya** 12:12 Wait, what's your GitHub?
**eftiquar** 12:15 EFTI.
Doesn't come?
**Zach Montoya** 12:19 No, for some reason it's not.
**Piotr Kiełkowicz (Splunk Inc.)** 12:22 is probably not OpenTelemetry contributor, so he cannot be.
**eftiquar** 12:27 But, yeah, why am I not a contributor?
**Piotr Kiełkowicz (Splunk Inc.)** 12:30 You are not part of OpenTelemetry organization, and… It is hard to assign to the reviewers such… such.
**eftiquar** 12:40 Oh, that is why it is not there, okay.
**Zach Montoya** 12:43 Huh?
Sounds like… sounds like we need you to join the OpenTelemetry community.
**eftiquar** 12:49 No worries, I'll buy 645, I'll take a look at it, no worries.
**Zach Montoya** 12:53 Okay.
Great. Yeah, I can take a look at the internet Instrumentation, and then the native compiler warnings, that seems… I'll take a look, but that should be fine.
**Piotr Kiełkowicz (Splunk Inc.)** 13:04 This PR is already merged, but GitHub has issues today.
**Zach Montoya** 13:09 Oh, okay.
**Piotr Kiełkowicz (Splunk Inc.)** 13:10 And it doesn't detect that it is merged already.
**Zach Montoya** 13:15 Interesting. Wait… Am I able to find it on… on Main?
Oh yeah, it's right there.
Huh, okay.
Well… I guess I don't need to look into that. Okay.
Yeah, GitHub has been having issues today.
So, yeah, that's fun.
Internet Instrumentation… Yes, so we can look through this.
Although… Is General with Claude, with System Boat, yep.
Okay, yeah, I'll take a look.
Definitely agree with having regression tests, and hopefully the contributor We'll be responsive to feedback, even though this was generated cloud code.
Dependency bumps, okay. And then, I think… So, from the backlog here, the resource attributes, I took a look, and I think it… I think it looks fine.
So not sure if anyone else wanted to chime in, essentially, and I think… Igor… requested changes, but I'm actually just gonna.
**Igor Kiselev** 14:22 Yeah, it will… it's old, it's old, I believe, clean it.
up.
Anything alright now, and I will pinch my review by the end of the day.
**Zach Montoya** 14:33 Okay, great, yeah, I'm just gonna just re-request, just so it doesn't show that anymore, but yeah, I mean, the main summary is that… and I think the PR description, the updated one actually provides a lot of context, but, instead of taking, app settings, implementing them to the environment variable.
or the resource attributes, we no longer do that. And this also codifies a couple other things and updates the documentation as such, but the environment variable We'll take priority over an app setting variable.
And then for hotel resource attributes specifically, we won't do a merge, we'll just take the one with the highest precedence, and then, like, service name.
has its own first-class environment variable, so that will take precedence over a potential service.name resource attribute. And yeah, it just has a couple tests to… with app domains to verify that.
So, yeah, I think it's in a good state.
Alright.
And then we have a couple Kafka ones. I have not looked at these. I don't know if I'll be able to take a look. I'm actually gonna be pretty swamped for the next couple weeks, so I… I don't intend to take a look at these.
But, I can take a look at other… Maybe higher priority ones.
But these seem… fine, because we've made progress on updated, like, semantic conventions, so… I think some of the blockers are now addressed.
Okay… And… for these ones that Alexei had, are we… intending to merge those before .NET 11, or what… What's the plan on these ones?
2 years now?
**Piotr Kiełkowicz (Splunk Inc.)** 16:28 I don't remember the status, to be honest.
**Igor Kiselev** 16:34 top isolation hook test, I believe there will be… so neither of them are really required, they just… Add some additional tests, some cleanup, and some other… the same as other changes formality to clean up.
Some issues, but… I will check with him if they are already preview and interviewed.
**Zach Montoya** 17:00 Okay. Yeah, I just want to make sure if we have any of this as, like, tracking for .NET 11 release.
**Igor Kiselev** 17:06 It's not required for .NET11 release.
**Zach Montoya** 17:13 Alright.
I guess any other, did you guys want to discuss any of these PRs at the moment, or just… Review async.
Alright.
Just continue on… okay. Issues, so… Yes, this is an issue documenting… well… this particular activity current issue, and this person also created a PR for it.
Okay.
Sure, I'll go take a look, just to validate the… The issue they reported, This one, it looks like, for the runtime async methods.
Is this… was this completely addressed by your… By the PR?
**Piotr Kiełkowicz (Splunk Inc.)** 18:16 It's ignored, basically, so it is not failing.
For some cases.
So, if I remember correctly, if the task is returning task.
it is completely ignored, if I… if I recall correctly, but I do not remember… exact details, it was kind of a week ago, and after that, I had kind of… A lot of other issues to verify.
**Zach Montoya** 18:47 Gotcha.
Okay, so there's still some follow-up work to address this, it's not completely resolved yet.
**Piotr Kiełkowicz (Splunk Inc.)** 18:56 I'm pretty sure that affects also DD.
**Zach Montoya** 19:00 Okay.
So if… Wait… Is it… Are you saying that if a runtime async method… If it actually returns a task object? Is that the scenario?
**Piotr Kiełkowicz (Splunk Inc.)** 19:18 I do not remember exactly, sorry, Zach. Okay, it was kind of a week ago when I was working with this, and Boom.
Okay, I need to repeat it once again.
**Zach Montoya** 19:29 Okay, yeah, we can re-review this at a later time.
**Piotr Kiełkowicz (Splunk Inc.)** 19:31 It was obvious when I was preparing the issue.
**Zach Montoya** 19:35 Alrighty.
Yeah, we can revisit that.
And then there's a couple more… couple small issues. I did want to take a look at these still, so, let me just assign myself.
**Piotr Kiełkowicz (Splunk Inc.)** 19:51 For sure, all three are affecting… are affected too, affecting also Datadoc repository.
**Zach Montoya** 19:58 Yeah, yeah, that's why I wanted to take a look at these.
I'll follow up here.
And, let's see for this one, Krista's saying that… we could easily do it on old managed C++ code. Not sure how much… not really sure if we can add something like that, right now, but that's good to know.
Okay. Yeah, I'll review these ones separately.
Okay, so for now, these are just kind of no milestone.
I think that's certainly fine.
Okay, no discussions.
Okay… And for these… Yeah, no changes.
Got it, let's… Is this… We just released 1.19? Yeah.
**Piotr Kiełkowicz (Splunk Inc.)** 21:02 Yes, today, and you can expect follow-up.
We have 36 in the contract repository a lot of security findings from…
**Zach Montoya** 21:11 Okay.
**Piotr Kiełkowicz (Splunk Inc.)** 21:12 Anthropic.
Today, just after the release, and let's say a couple of them… Looks as a real candidate for the security fixes.
**Zach Montoya** 21:23 Okay.
Well, I'll stay tuned for that.
Oh, that was the other thing. Okay.
Cool.
Anything else you guys wanted to discuss?
**eftiquar** 21:50 All good for myself.
**Zach Montoya** 21:55 Alright.
Yep, all good for me.
Cool.
I'll think yes, and I guess we'll stay tuned for, Getting a release out for the potential security fixes.
**eftiquar** 22:07 Thank you.
**Zach Montoya** 22:08 Alright, thanks.
