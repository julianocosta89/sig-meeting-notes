SIG: Swift SIG
Date: 2026-08-13
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Ben Joseph (Raintank, Inc. – Grafana Labs)** 01:26 It was fun.
**Vishwan aranha** 01:28 Hey Ben, can you hear me?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 01:29 Yep.
**Vishwan aranha** 01:32 two non-IOS people working… talking in the non-IOS… in the iOS.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 01:38 Yeah.
**Vishwan aranha** 01:41 What is the agenda for today? Nobody added anything.
What is today's the 13th?
Should we add any topics?
PR.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 02:40 Just have one PR bump.
I mean, I would like somebody to, like, take a look at that metric issue that I reported. I also attached a PR For the solution.
**Vishwan aranha** 02:53 Can you add the link here? Like, I don't know if we mentioned names, but yeah.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 02:58 Yeah, let me add that.
**Vishwan aranha** 03:00 It… Why do I have so many tabs open?
Like, some days I forget what I'm doing, and I forgot what I did, so…
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 03:14 It's, it's a lot of context switching these days, and, like.
**Vishwan aranha** 03:20 I'm like… I was, like, I'm also running benchmark tests, so it's…
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 03:27 Hmm… Yasura has a couple of piers open.
**Vishwan aranha** 03:43 Yeah.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 03:57 Oh, mine was in draft. Yeah, I think I wanted somebody to take a look at it, and then…
**Vishwan aranha** 04:05 Yeah,
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 04:07 Yes, let's just move it out of draft, I think.
**Vishwan aranha** 04:12 I wonder if people are logging in as a guest, or… yeah.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 04:17 Bryce is here.
**Vishwan aranha** 04:19 Goodbye.
**Bryce** 04:21 Hey there.
Sorry, I forgot that the meeting link changed, and the… Yeah, the… the link in the, in the calendar event is still the same, so I'm not sure who updates that.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 04:37 Oh.
I think it changed for me,
**Nacho Bonafonte** 04:41 Sorry, I'm a bit late with the new Zoom link, I had to read that.
**Bryce** 04:46 Yeah, I had the same problem.
**Nacho Bonafonte** 04:50 Yeah, I'm not very sure about creating an account at Linux Foundation, but… You know, sometimes you have to.
**Bryce** 05:01 Here, let me share my screen here… Oh no, that one's working.
There we go.
Okay, let's just go over last week's topics quickly. New Zoom link… We have PRS review, I'm not sure… If any of these were actually reviewed.
Yeah, that's still open.
Oh, I guess there's some feedback from Nacho on that one.
That's good.
**Vishwan aranha** 06:09 There's another older PR, which, I think it was approved, like, 3 weeks ago, just needs merging.
**Bryce** 06:25 Oh, interesting, coquille feeling.
Yeah, that needs… yeah.
Okay.
And then… Met your kid, that was an issue, okay.
August 13th… Okay, I think we're good for… Topics from last week.
Alright, so… new topics. PR reviews, let's take a look.
Yeah, so this one, I think we just… Was this one of the ones in that list? No, this is a new one. Add OTLP, GPRS, TLC example. Cool, yeah, excellent.
Oops.
Yep, fabulous.
We can get that merged ASAP. Thank you for adding that. Was that,
**Vishwan aranha** 07:29 That's mine, yes.
**Bryce** 07:31 Great.
**Vishwan aranha** 07:31 And also, there's an older one, which is failing some CI checks, because I don't have the ability to rerun, because that time GitHub was messing up as usual.
**Bryce** 07:42 This one here.
**Vishwan aranha** 07:43 Yes, it just needs to rerun, and all the checks will pass.
**Bryce** 07:50 and GitHub.
**Nacho Bonafonte** 07:52 Yeah, but we can… I mean, we can merge that, right?
It was approved, we could merge without running.
**Bryce** 08:00 Oh yeah, we can. Yeah, so that's not a problem, we'll just merge that then.
**Nacho Bonafonte** 08:11 Yeah, I tried with running them, but I couldn't. With my account, I don't know why.
So, yeah.
**Bryce** 08:16 Yeah, sometimes, like, if they get too old, it won't let you rerun the job.
**Nacho Bonafonte** 08:24 Yeah, there is something strange there. I don't know how to reactivate or be able to run again.
Oh, sorry.
**Bryce** 08:32 My camera's not working. That's okay.
**Nacho Bonafonte** 08:35 Yeah, but, yep.
No problem.
**Bryce** 08:40 Okie dokie.
So I'll… I'll review that PR after the meeting.
And, also… Take some time for those other ones as well.
Okay, fixed metric kit.
So, oh yeah, okay, so this is the stack trace formatting.
By, by Ben. Thank you, Ben, for… Submitting this?
So this just, follows the, OpenTelemetry stack trace format rather than the Apple one.
Right, exactly.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 09:14 So the issue was that, like, when, when… what we expected, by, to be delivered by Metricit, like, we were expecting a different shape, and then we were not able to apply that transformation, and so we would just pass it through ASS.
So this change kind of, handles the two different representations that might be, delivered by Metricit.
That's… that's essentially the change.
**Bryce** 09:42 Fabulous.
It looks like there's tests, too. Excellent. Cool. Yeah, I'll take a closer look at this after the meeting as well.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 09:52 Yeah, I think there is a doc update, I'll make that right away after this.
**Bryce** 10:03 Okay.
Cool.
Alright, well, yeah, I really appreciate your contributions, that's awesome.
any other topics that anybody wants to discuss today?
**Yasura Dodo** 10:20 I, I created, through OPS, only one is open, others are still, like, dropped, because I need to review… sorry, my son is speaking to me.
**Bryce** 10:33 Yeah.
**Yasura Dodo** 10:33 Yeah, yeah, it's a… it's a dinner time, so it's a bit… a challenging time. Okay.
Okay, sorry. So, the… I added the, bumpy out… yes, that one.
So basically, like, I want to add asynchronous functionality with the HTTP exporter.
And as a first step, I added the async function and the HTTP HTTP client, or something like that. I don't remember the… oh yeah, HTTP client.
And this is the… I commented that this is a breaking change if someone is using this protocol.
But, I think it should be flying, like.
I don't… I… I didn't find the… the necessity to have, like, Therefore, implementation to avoid breaking change.
**Nacho Bonafonte** 11:35 Yeah, I think the only users of that protocol are ourselves, right? In the… in the… in the library. I don't expect external users of this protocol here.
**Yasura Dodo** 11:45 Yeah.
I had the same feeling, like, I didn't expect people using this protocol directory.
**Bryce** 11:53 Yeah, I… I agree as well.
Cool.
**Yasura Dodo** 12:03 So basically, like, after this, request, I can… I like to work on the, HTTP exporter to be able to use the async weight functionality.
To be able to, We've.
**Nacho Bonafonte** 12:20 generos.
**Yasura Dodo** 12:21 Yes, yes.
**Nacho Bonafonte** 12:24 Yeah, that's the, yeah, that's the correct approach, at least, or at least I think it's a… Easiest approach to not break anything.
**Yasura Dodo** 12:36 No.
Like, I don't need too much right now, but, like, I just wanted to, bring it to this discussion, because, if my approach… my… I mean, like, my direction is… I don't know, like, if it's correct or not, but it seems like it's a good direction.
**Bryce** 12:54 Yeah, this looks like the right course of action to me. My only concern is, the… the intermediate state, if, the… Exporters are depending on this protocol.
It's been a while since I've looked at this, so I don't know the exact chain, but if… You know, you're adding these new async methods, if that's gonna cause any problems before we add the implementations and the actual exporters.
**Yasura Dodo** 13:30 I don't think so, because, like, it just… we don't use it, like, right? Like, it's kind of like a dead, dead code.
We're not using it anywhere, so, like, it should be fine.
**Bryce** 13:40 Okay.
Cool. Yeah, excellent.
**Yasura Dodo** 13:45 And one more thing, I'm also going to work on the Core, because, I realized Corea and the OpenTeameter SIFT, they have different supported OS, So, the core are still using, like, let's say, like, iOS 12. So, like, we cannot use a single wait function.
Is there any reason?
Like, can we drop?
I opened the draft PL, by the way, if you open the call, like, you can see the changes.
Can you open the core?
**Bryce** 14:21 Yes.
**Yasura Dodo** 14:25 Yeah, thank you.
That one… oh, it's failing. Maybe because I added a cursor.
Yeah, I'm asking to remove it, but, like, somehow CASA doesn't listen my prompt well. Anyway, can you open the file changes?
It's basically, like, dropping the, the available, annotation and also supporting, platform versions.
**Bryce** 14:54 I… The, the issue here, and I think Ari is more, he, he more depends on these older versions. Yeah, so… if we have vendors that are relying on the API and SDK to produce their own artifacts, they depend on these older versions, so it might be a little bit of a sticky issue to bump these up here.
So… Yeah, we might need to see… like, I mean, supporting async await, that might be a strong enough reason to… to bump the versions. That might be able to convince Ari.
But we'll… we'll see.
**Yasura Dodo** 15:44 Fantastic.
Okay, much code, but, like, I saw, like, it's fine, because the… I saw, like, we are going to match the core and the open territory SIGT, right? So, in the case, like, I saw, like, okay, why they have different, supported platform, we can… we can sync it.
**Bryce** 16:02 Yeah, that's a good point. When we merge them back together, we're gonna have to reconcile that, which probably means that we're gonna have to bump the… Supported versions anyway.
Yep, yep, yep.
Do you have any thoughts, Nacho?
**Nacho Bonafonte** 16:19 Yeah, so… These are the versions that the non-core library has.
**Yasura Dodo** 16:25 12?
**Nacho Bonafonte** 16:26 For my question?
is MacOS… sorry, MacOS 10, sorry, MacOS 12.
He's the… Yeah, I have…
**Bryce** 16:36 I think so.
**Nacho Bonafonte** 16:38 It's been so many years that it keeps for me.
**Bryce** 16:42 12, 13, 13, 6, yeah, yep.
**Nacho Bonafonte** 16:45 Okay. Mmm.
Yeah, that's… that's true. So we need to change here… in this… didn't we have it in the Spanish portal already? Or in the… Didn't we have a sync await there?
With a conditional, with the availability.
**Yasura Dodo** 17:10 Yeah, we can have, but just, I was wondering, like, it's gonna be a lot easier if we just drop the, the… the supported OS.
**Nacho Bonafonte** 17:21 Yeah, that's my… yeah, that's… Yeah, the problem is use… this library is also useful, Ali.
Used by, by companies that have by contract to support very old versions. That was the main problem, and that's why we added so many, labels there.
I know it's much easier, but if… But usually, it's not only Directly the users of the library who has that Have to support that, but if they are middleware.
companies, I don't know where you work, but there are some middleware companies that just pack OpenTelemetry Swift in their own libraries, and they also have this.
Contracts with third-party companies that are supporting many versions, and… In the past, we tried to update some of this. Apparently, it's time.
I think it will be better… after next Apple release, so we… after iOS 27 or Mac OS 27. So we will have, like, one year or more of support, at least technically. We will be… Less, versions… before.
But if… I think we could… if we… if we can, we will leave it here until we mix this library again with the main library, until we move core to main library, if that's possible. I know it's much easier.
But also it, I think it… Yeah, it, it… it will be less breaking. We can't really… this breaking chains now, because we also have to release a version for last version of CocoPots, so… I would prefer if we can keep the versions right now, release cocoa pods, move.
**Yasura Dodo** 19:30 Okay.
**Nacho Bonafonte** 19:30 core to the main library, and then, simplify there.
If it's not very limiting. I mean, it's… we… We must try to.
**Yasura Dodo** 19:43 I think, like, we can, we can, we can still keep supporting the, the old OS, and, I can find out the solution. Maybe, like, just, available annotation could help, or, like, just, can import a concurrency or something like that.
**Nacho Bonafonte** 20:00 Let's try that, if possible, before. Yeah, because we have some, you know, the cocoa pots thing is something that We are just in the end of August, before we create that, So, try to keep compatibility there, not breaking anything.
For maybe some still users of CocoaBots now.
Yeah. And whenever we merge, as Bryce said, let's… let's update there.
I think it will be… If possible, we'll be much, much better.
**Yasura Dodo** 20:35 Okay.
**Nacho Bonafonte** 20:36 Sorry for,
**Yasura Dodo** 20:38 It's okay, it's okay, I just, I just, like, I… it was a kind of, like, quick, quick sort, like, when I was looking at the code, and then, like, looking with AI agent, and, like, oh, why not remove the, A variable stuff, and…
**Nacho Bonafonte** 20:52 Yeah, in my company, for example, I am using just iOS 18 and newer, so… I really would love… I mean, I love dropping old versions, because it simplifies everything and simplifies testing a lot, but at the end, yeah.
**Yasura Dodo** 21:10 Okay.
**Nacho Bonafonte** 21:11 This is, you know, this library is being used by so many people, different contexts that, yeah, we try to keep As… as much as possible, the… the versions.
Yeah.
You…
**Yasura Dodo** 21:26 Oh, okay.
**Nacho Bonafonte** 21:26 Yourself of the future might also, be grateful for this, maybe.
If we, you know, that's the point, yeah.
**Yasura Dodo** 21:37 Yeah.
Then, yeah, I will try to find a solution. I think, like, it's possible to do it without this one, and… and I will probably close this PL.
There's some context.
**Bryce** 21:52 Sounds good. Alright, thank you.
**Yasura Dodo** 21:55 No, thank you too.
**Bryce** 21:58 Okay… SwiftCore. Are there any other PRs that you wanted to look at?
Yasura?
**Yasura Dodo** 22:13 No, yeah, because I didn't review it by myself, the first one, that's why it's still a draft.
**Bryce** 22:22 Okay.
**Yasura Dodo** 22:22 Yeah, you can, we can review, but, like, don't complain anything.
**Bryce** 22:31 Okay.
Okay, yeah, I'll just leave it be then.
**Yasura Dodo** 22:37 Yeah, but, like, this one is, like, I need to, like, I couldn't use, like, some, like, stack PROs or so on, because, I was contributing from my arropically, and… So, it's a little bit mixed with the, HTTP async PR, like, the PL that I opened.
ready for review, but, like, this one is on the top of the PR.
So, it's a little bit mixed with others.
**Bryce** 23:10 I see, I see. Okay, so let's let the other one settle, and then we can come back to that one.
**Yasura Dodo** 23:15 Yes.
**Bryce** 23:16 Cool.
Okay, so that's… The docs there, we can get that merged in really quick.
And then that one as well… okay.
Any new issues?
Yep, so that one was the one that we added last week.
And… this is the one that you're working on trying to fix with the async await stuff, right?
**Yasura Dodo** 23:46 Yes.
Yes.
**Bryce** 23:48 Can I assign this to you? Does that make sense?
**Yasura Dodo** 23:50 Yes, please.
**Vishwan aranha** 23:53 Yeah, I was just gonna ask if it's possible to assign all the issues to people who are working on, then it will, like, avoid any duplication. Absolutely.
**Bryce** 24:04 Yeah, I'm not sure… are you able to assign tasks to yourselves?
**Vishwan aranha** 24:08 No.
**Bryce** 24:09 No, okay.
**Vishwan aranha** 24:10 need maintainer access, I guess, yeah.
**Bryce** 24:11 I see, okay, alright, Alright, so let's see here. Are there any issues that anybody's working on? Oh, here we go.
Alright, thanks, Yasura, have a good day.
Yeah.
**Yasura Dodo** 24:23 Thank you so much.
**Bryce** 24:26 Okay, so what I was saying is, Issues. Who's working on stuff that needs to get assigned to something so that we can keep track of that?
**Vishwan aranha** 24:36 I have my PR for 332, issue number 332.
**Bryce** 24:41 332.
**Vishwan aranha** 24:42 Assigned to me.
**Bryce** 24:46 33… oh, is that in core?
**Vishwan aranha** 24:51 Let me see…
**Bryce** 24:55 Maybe not.
**Vishwan aranha** 24:57 It's, I can send the link in the chat.
**Bryce** 24:59 Oh yeah, that's good.
Right here, so… Pure.
Okay.
Not me.
Okay, there we go. And… Not showing up in here.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 25:30 It didn't hear… It's the AARN.
**Vishwan aranha** 25:33 A-R-A-N-H-A.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 25:35 I-R-A-A, sorry, A-R-A-N.
**Bryce** 25:39 Oh, here, is it, this one here?
**Vishwan aranha** 25:41 Yes.
**Bryce** 25:42 Okay. There we go.
Okie dokie.
Alright, cool.
Any others? Anybody working on any…
**Vishwan aranha** 25:56 I remember commenting on a few, if I can't take those, but, I don't remember which ones were those. Maybe one of the good, first issue.
**Bryce** 26:06 Okay.
**Vishwan aranha** 26:07 What's…
**Bryce** 26:08 Yeah, so maybe going forward, what we can do is if, somebody wants to take an issue, you can just post it in, the, the Slack group, the Slack channel, the Swift Slack channel, and then we can, Okay, I'll sign this one to you as well.
And we can, assign you to it.
**Vishwan aranha** 26:31 There's also a question I had that I posted in there, if you could respond whenever you get a chance.
**Bryce** 26:36 Oh yeah, here, okay.
What a threadsafe headers provider on the config, evaluate before each export?
keeping the existing SIG behavior. I think, yeah, conceptually, that sounds good to me.
Like, it resolves it each time it, it accesses it.
Yeah, that way you could, yeah, be updating the headers. I think that sounds… that sounds totally fine.
**Vishwan aranha** 27:04 Okay, sounds good, so I can proceed with that.
**Nacho Bonafonte** 27:07 Yeah, probably adding a callback method that can be added there.
So you can fill that callback with your method. Could be, An easy way to add that, so the user of the library can just… Implement the callback to… To have, you know, control of what to put there.
**Vishwan aranha** 27:33 Sounds good.
**Bryce** 27:35 Yeah, that could work as well, yeah.
Cool.
Alrighty, so… We've looked at that, we've looked at… the new PRs… Let's take a look at…
**Vishwan aranha** 28:03 I need to drop in 2 minutes, but I just wanted to mention, like, is it possible to go through all the issues whenever you guys get a chance and, like, close out the ones that are obsolete now?
**Bryce** 28:15 Yeah, that's definitely some… something that we need to be doing. I might try to run, like, a LLM on it and see what it says, where we can, tidy things up. That might be the best way to do it.
**Vishwan aranha** 28:29 Sounds good, thanks.
**Bryce** 28:33 Okie dokie.
Anything else?
**Vishwan aranha** 28:39 That's all I got.
**Bryce** 28:45 Alright, Ben, did you have anything?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 28:49 No, not at this point. I'll also try to pick up some busty shoe.
**Bryce** 28:55 Okay.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 28:56 Yeah.
**Bryce** 28:57 Cool.
Alright, I guess, if there's nothing else to discuss, I'll hop in and start, working on some Pull request reviews and get some of that stuff merged.
Unless Nacho, did you have anything else you wanted to discuss?
**Nacho Bonafonte** 29:15 No, no, nothing.
**Bryce** 29:17 Very good.
Alright, then…
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 29:19 Sorry, one last question. Do you guys have any, any, you know, metrics that shows what, what is an SDK or API?
completeness in Porswift, with respect to the OpenTelemetry spec.
Just to get a sense of, like, what is missing, what needs to be worked on.
**Nacho Bonafonte** 29:43 I mean, we were feature complete when we do this test.
With what was then. And there are some… some issues there in the project that just mentioned, reviewing the spec and seeing if we are still following.
Because we followed the spec, and when we released version 1.0, but yeah, the spec has been updated, and we have not tracked all those changes, so there could be places where the spec has been expanded.
or even change, probably expanded more, usually. And we… Have not added those changes to our library.
There are some issues there in the, just… Bryce just closed that… that issues page, but there were some, lower in the page that just were about reviewing the span API, for example, and see if there are any new methods that we are not doing, or any method that now behaves a bit different, or some… constants that are not constants anymore, something like that. Yeah, we… we have not… Done that review for… For a long time now, so we could be a bit outdated.
With the latest changes on the spec. Yeah, that's true.
I mean, that's also a good first issues, if you want.
To get into the… Meetings work in some of those areas, so…
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 31:19 Yeah, just curious if you had anything.
Yeah, if we, like, with MondoTo, if we were, like, feature completer, I think that's good. I was just trying to do a, like, analysis of, like, where we stand, with respect to the spec, and I think the LLM just gave me, some gaps. Maybe those are, like, part of the more recent spec, so I can…
**Nacho Bonafonte** 31:41 Could be that. I mean, we definitely, when we released, we were, feature complete, we were reviewing… our spec, implementation was reviewed by the… committee?
Then, and, and so we, we, we were, When version 1.0 was released, it was feature complete. With what?
was the, all the specs. So yeah, probably those things that, that the LLM signaled as Differences are probably changes in the specs since then.
So we'll probably be additive changes.
Maybe there are some of… maybe some efforts, you know… It was not reviewed by LLMs then, so probably something could have been missed by the reviewers, but yeah, in theory.
It was, so the rest of things are just really additive.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 32:37 Understood.
**Bryce** 32:38 Yeah, the, the oldest… the oldest implementation we have is the spans, so that one's probably the most out of sync with the current spec, and that's why we have a whole array of issues to kind of review the current spec.
But if you had the LLM look at it, maybe you could go and update those issues just with what it found. That would be really helpful. Yeah, our second oldest is logs, and our most recent implementation is metrics, so that one should be the most… in line with the current spec. I know that there's some issues with, like, the exponential histogram stuff that is not quite completed.
I think there might have been an issue added for that recently, but that's generally kind of where the implementations stand right now.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 33:24 Garner.
Yeah, just, I was just curious if people are tracking it, somewhere.
**Nacho Bonafonte** 33:31 We, we, we… I think we also added some extra Features to the library.
That may… might not be in the SIG, but they were useful for iOS or Mac.
Apple, platforms.
But I don't think… None of them will be against the philosophy of the spec.
For example, we had one that was… Taking, environment variables, with a… with the parent span, for example.
But that was later moved to the spec itself.
So I don't know how that… I don't… I think now we move to the spec one in that sense also, but there could be other… other features that we added that was… were not in the spec one, but were needed for the uses of the library at the beginning, that…
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 34:28 Okay.
**Nacho Bonafonte** 34:29 couldn't… Not being displayed, but yeah, should be minor… very minor things.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 34:35 Understood.
**Nacho Bonafonte** 34:36 For completeness of the… of the evaluation.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 34:40 Yeah, I'll, I'll… anyway, I'm, like, just taking a pass at this, and I'll try to, you know, in the GitHub issues, I'll note any gaps that I identify. I'll see if there are existing issues, or, like, if new ones need to be created, at least, I think.
Would be good to have a, you know, an Epic or label linking them.
So I'll try and do that.
**Nacho Bonafonte** 35:06 Brilliant, yeah. Cool.
**Bryce** 35:07 Thank you.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 35:08 Thank you, guys.
**Bryce** 35:11 Alright then.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 35:12 Alright.
**Bryce** 35:13 Everybody have a nice rest of your week.
Yeah. Cool.
**Nacho Bonafonte** 35:17 Right.
