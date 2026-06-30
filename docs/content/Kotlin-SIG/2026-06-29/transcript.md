SIG: Kotlin SIG
Date: 2026-06-29
Duration: 25 minutes
============================================================

## Zoom Recording Transcript

**Francisco Prieto** 01:41 Hello!
**Hanson Ho** 02:12 Hello?
**Francisco Prieto** 02:16 Yeah, and then.
**Hanson Ho** 02:19 My camera is not on. I don't know what's going on. Let's see You can hear me?
**Francisco Prieto** 02:30 Yes, but I can't see you.
**Hanson Ho** 02:33 No. Yeah. I can't I don't know what's going on either. Weird.
Well, let's see if I can present. If you can't see my face, but you can hear me, that's probably okay.
Let me see if I could find the OpenTelemetry. Okay.
So, Jason is not here today.
I can't see your video, Fran, but I don't know if that's deliberate.
Ch-ch…
**Francisco Prieto** 03:16 I'm having lunch, so I'll turn my camera on in a few minutes.
**Hanson Ho** 03:19 No worries.
That's okay. Can you see my screen, though, at least?
**Francisco Prieto** 03:26 Yep, yep.
**Hanson Ho** 03:27 Alright, cool.
Can wait a couple minutes, but so far, no agenda items. I have lots of reviews, to, to do.
Outstanding.
Jason's away for this week, so if we don't have a ton of stuff, we can talk through what we can and, end early.
So.
I have a couple.
**Francisco Prieto** 04:09 I could use the time to actually review some stuff.
**Hanson Ho** 04:12 Yeah, that's what I said last time.
Finalize questions for… So I want to talk a little bit about, what we want help on from the Kotlin folks.
But we'll wait a couple minutes.
And, did Jazz create any issues, or post on Slack?
But… About the Amazon use case?
And what they've been looking at.
I guess not.
Brash, I haven't seen.
Okay.
Alright, we're 4 minutes after, so we can get started, I guess. So, light agenda today, if anybody wants to put in more stuff, feel free.
But, so I think the things that I want, the JetBrains folks to help us with initially is, the project structure, so, Whether or not we are.
What stands out is something that doesn't comply with the project structure, the setup.
things like that. I think we… we did it.
at the point where it was correct, what, 6 months ago, or whatever it is, but I know they since have released a new, structure. So, what we could do is we could probably, look at what the structure right now is, and then try to update it, or propose a mapping to the new one, and then see if, it's correct. So this is basic… kind of basic.
Basic checks.
Another one, I have, is whether the API is, Is the API idiomatic… Kotlin idiomatic enough?
Because I think… We try to… make… it.
Of, you know, find the right balance between Kotlin idiomaticness.
And, just OpenTelemetry, Idiomateness, which a lot of it derives from Java. So whether… the decisions we've made for aesthetic or kind of, you know, personal preference reasons is correct. And if anything stands out, I don't think we necessarily need them to like completely approve of every decision. But certainly, if there are egregious things that, you know, stand out or be unnecessary, or we're copying an old Kotlin pattern that is no longer… preferred. We kind of want to know.
Let's see… So basically, does this look like a Kotlin API?
Is… is kind of my main, my main, yeah, tomo.
**Francisco Prieto** 08:36 I must be worried about multi-platform API, because I think we have Kotlin APIs pretty much.
Well.
internalized, but we haven't been working much. At least, I haven't been working much with multi-platform APIs, and I don't know if there's any kind of difference, especially for accessing them from iOS or from JavaScript.
**Hanson Ho** 09:00 Good.
Or is it, is it, is it, is it iOS or is it Swift?
Or is it…
**Francisco Prieto** 09:12 I said iOS, right? Yeah.
**Hanson Ho** 09:15 Yeah, yeah.
**Francisco Prieto** 09:16 So.
**Hanson Ho** 09:17 You're right.
I just don't know what the terminologies are. Like when they say platform, it's iOS, right? They're not.
Swift backend is, is like a diff… is a different target.
Maybe, I don't know.
**Francisco Prieto** 09:33 And also I think they should be interchangeable, like we should be able to support Objective-C or whatever they use, so.
Not sure.
**Hanson Ho** 09:42 Inde.
**Francisco Prieto** 09:42 I think the target is iOS, so like in multi-platform.
**Hanson Ho** 09:46 Yeah.
Yeah, we have JVM target and Android target, so it makes sense if there's, like, you know, an iOS target and, like, a, you know, a Swift target or something like that.
Amend version requirements for… yeah, we'll put this… yeah, I'll take that off, because we don't need it.
But yeah, any other things that we should kind of add? Those are my two… you know.
like, do we want to go down in terms of, like, detail, like, Kotlin implementation? like, are there… are there, like… like, at this point, do we… do we want to, like, improve, like… Minimize allocations and things like that.
**Francisco Prieto** 10:35 I'm not sure if they are going to be… Scrutinizing, like, are they actually going to be profiling stuff, and… getting deep into that. And also.
**Hanson Ho** 10:46 Probably not profiling, but like if there's like by visual inspection, if there are like some patterns like, hey, stick this like things that we were doing that is going to be slow because they are the compiler team. So I kind of almost want to like see.
hey, they're experts at this stuff. Can they go through this and be, yeah, this should be in line, or this shouldn't be in line, things like that.
**Francisco Prieto** 11:11 Yeah, that's probably going to be awesome. I'd be surprised if… Shamey.
Didn't catch that yet.
**Hanson Ho** 11:20 Oh, oh, for sure, but, you know, that should make it easy, then, if it all looks good. So…
**Juan Vega** 11:35 Delivery.
**Hanson Ho** 11:44 I won.
**Juan Vega** 11:46 Hello, guys.
**Hanson Ho** 11:50 So, Jason's out today, so, we're pretty, short on topics, if you have anything. Other than reviewing, PRs, cause I, I know that's one thing that, you know, Fran and I are gonna, gonna be doing. I know we're, we're, we're behind in a lot of our PR reviews, so…
**Juan Vega** 12:12 I was also reviewing Piers, but then I don't have permission, I just review for…
**Francisco Prieto** 12:19 There's actually one PR from you, I think, the v3 that I need to actually understand what's v3. So it's probably going to take me some time.
**Juan Vega** 12:29 Okay, don't worry. If you need to chat or whatever, I am on Slack.
Bye.
Actually the V. 3. It's better if we 1st merge the text mapper.
API change, you did, No, actually, who did the… it was… Awesome, maybe? Who did the… the API change on… on TextMap?
**Francisco Prieto** 12:55 I think it's the other approver which I don't remember the name.
**Juan Vega** 12:59 Okay.
**Hanson Ho** 13:00 Oh, yes. Misaki, I think.
**Francisco Prieto** 13:03 This side, you think?
**Hanson Ho** 13:05 Yeah, I have a PR to review from them too, so.
**Juan Vega** 13:11 Yeah, so if we match that first, then I will match, because I will update my PR, and then we can match. Otherwise, it's going to… to conflict.
**Hanson Ho** 13:21 Yeah, sounds good. I will do that later today. So we could.
Put that.
If you have signed PRs. So I'll put it here, actually, in the, in the actual doc.
So that we can go back and look at that.
That's true.
There's a lot of them.
Let me see… oh, right, you have it on Slack, I was putting it on Slack.
Cool.
**Juan Vega** 14:01 and down at the.
**Hanson Ho** 14:05 There's also the one…
**Juan Vega** 14:08 The one I was mentioning is linking on mine, so you can just navigate from there.
**Hanson Ho** 14:13 Perfect.
Okay.
**Francisco Prieto** 14:30 I think Masaki's PRs are approved, so we can merge those.
**Hanson Ho** 14:34 Sweet. Well, a maintainer can merge those, so, we'll wait till Jason comes back tomorrow, I think. But if we can get everything approved, and, and lined up, tomorrow, we should be okay.
Alright, any other PRs we should have paid special attention to?
**carlosalberto** 15:06 They're making attributes non-experimental, like kind of stable.
**Hanson Ho** 15:11 Yes.
**carlosalberto** 15:12 And the change itself, of course, is very small, but I think that probably, it could be good for people to review that. And actually, I wanted to say that, even though we discussed that a lot, probably it could be interesting to get that, you know.
Opinion from the call… from the, jetBrain folks on that front.
Mostly because attributes is used all over the place, like for metrics, traces, logging, profiling, and this was… something that, at least for the Java C, it took many iterations to get where they are now, you know? Like, optimization, near optimization, there are… Because at the pay level, you are providing de facto in implementation, you know?
**Hanson Ho** 16:00 Yep.
Oh.
All right, that is here.
Oops.
It's always… Do we want to wait till the Kotlin folks take a look before we… we… explicitly remove the X-ray rental, or do we just not release until they're done? Maybe.
Because as long as.
**Francisco Prieto** 16:31 The experimental PR is already there and I think it like, I can approve it. I will approve it, because it's just removing the experimental tiles. Then we can time out when we want to merge it, but I think it's okay.
**Hanson Ho** 16:46 Well, yeah, we'll have to wait for Jason to come back to Merchant anyway, so… But yeah, as long as we don't release, we could undo it if the JetBrain folks have comments.
Actually, Attributes API.
Yeah, we went through quite a bit of, of, back and forth, too, especially with the… well, that's actually how the Attributes API… it's a span API, whether we expose the attributes or not is readable, but… That's a different story.
But yeah.
I will… instead of say… I think for for For ease, I should send them, like, a link to, all the API, files, instead of saying, hey, just look at our API.
gather explicit links.
to Api files for them to review.
I can do that.
I'll probably create an issue and just attach it to there, so it just makes it easier to deal Okay, any other?
Outstanding PRs to have a look at?
I mean, we should look at all of them, but like… First, look at the ones that are most important, and then go from time or something.
All right, it's not.
**Francisco Prieto** 18:33 Oh, sorry.
**Hanson Ho** 18:34 Oh, go ahead.
**Francisco Prieto** 18:36 It pretty much, collides with the next item. The ones from, Renovate, I will wait until merging them, because I'm… Almost sure that our minimum requirements for iOS and JavaScript are not actually working correctly.
I mean…
**Hanson Ho** 18:56 Do we have tests for that?
**Francisco Prieto** 18:58 No, our minimum requirement tests only check for JVM.
So… I'm working on that.
I want to do two things. One is check if our minimum requirements also apply to iOS and JavaScript.
If they don't update them.
I'm not sure if I'll update them, but maybe Check if we can actually support.
So what wouldn't be working, I haven't got the time to test it yet, but what would not be working is a project, a multi-platform project with iOS and JavaScript targets using Kotlin 2.0. I think one of the dependencies we expose.
it fails to compile in that case, and we don't test that.
Once I verify if that's the case, I will update the tests to fail. So yeah.
**Hanson Ho** 20:03 Yeah, I think… We know that the iOS and JS support is fairly lacking in terms of coverage and everything. So since we know that, at least having tests that fail or having explicitly saying, hey, we don't… What we guarantee is very little. That would be at least — if we can't make it work, at least we tell people what works and what doesn't work. And right now, I don't think it's very clear.
**Francisco Prieto** 20:32 Yeah, I think that's going to be the end result. I don't think we are going to make much work to downgrade our dependencies to support Kotlin 2.0 in those scenarios. But maybe just add a disclaimer, hey, this is the minimum version we support for iOS and JavaScript. But yeah, we'll see. We can discuss it.
**Hanson Ho** 20:51 Yeah, I…
**Francisco Prieto** 20:52 More information.
**Hanson Ho** 20:54 I hope older Kotlin support is less necessary if effectively the Kotlin support they need is for KMP versus on Android and to lesser degree JVM. That support is tied to a legacy of older dependencies.
That wouldn't really be a problem for KMP, I don't think. Hopefully, so.
**Francisco Prieto** 21:16 Yep.
**Hanson Ho** 21:21 Cool, any other topics?
David, do you have any, PRs that are still waiting?
Because I think on Android you might, but I'm not sure if you have any on Kotlin Alright, if we don't have any other topics, we can get a bunch of time back and maybe use this to, do reviews.
Going once, going twice…
**Juan Vega** 21:57 One stupid question, if you don't mind.
**Hanson Ho** 22:00 Yeah, no.
**Juan Vega** 22:00 So, the concept of maintainer is like… someone outside of the repository that can only match. And then we have approvers. That is.
And at 12.
people working on implementation, or how does it work? And maybe I… this is documented somewhere, but just… I am just curious.
**Hanson Ho** 22:20 Oh, yeah. So maintainers are people who have rights to modify and merge PRs into the repository. And there's three of them right now.
Jason, Jamie, and, I think Misaki.
And then approvers are there with rights on the repo a little bit less than maintainers. I think approvers have the rights to tag, give explicit approvals that will allow maintainers to merge, and have rights to create issues and things like that.
And then everybody else is just, I think, a contributor. So they could work on PRs, comments, do all that stuff.
And I think the idea is that if you do enough contributions and you're willing to help out as an approver, then the maintainers will add you as an approver to be able to — approved PRs, and then for maintainers to merge. So,
**Juan Vega** 23:24 And I'm asking to be myself an approver or whatever. It's just because I was curious if a maintainer and approver could be the same person, and you say yes, no, because it could be Jason, for instance, no?
**Hanson Ho** 23:37 No, approver, think of approver as like a lesser maintainer. So maintainer is the one that has all the privileges. Approver is the one that, the one that, the one that they don't have is merging PRs. That's the most important one. So we're always…
**Francisco Prieto** 23:51 Oh, sorry. It's not really related to the tasks that you do, like the issues you solved or the like everyone works on everything as they see fit.
**Hanson Ho** 24:04 Maintainers have final say in terms of whether there's disagreements about architecture and things like that. It's up to maintainers to decide whether it's a direction they want to take the repo in.
Think of them as code owners. And think of approvers as like the code helpers.
**Juan Vega** 24:27 Okay.
**Hanson Ho** 24:27 It's.
**Juan Vega** 24:27 Okay, okay, great.
**Hanson Ho** 24:30 And everybody are co-doers, so…
**Juan Vega** 24:36 Great.
**Hanson Ho** 24:39 Alright, if there's no other things, we could, See you in a week, I don't know if it's a holiday in the US. It may be a holiday in the US because July 4th is Saturday. But I am Canadian, so I'll be here regardless. So I think most of you aren't American.
I think, European, Argentinian… where are you based, Juan?
**Juan Vega** 25:11 Spain.
**Hanson Ho** 25:13 Okay, there you go.
Europeans and South Americans and Canadians. No Americans other than Jason here, so… So,
**Francisco Prieto** 25:23 SI issues will be held in Spanish, Hansen, if you don't… Get more English.
**Hanson Ho** 25:29 David doesn't know Spanish either, as far as I know.
But yeah.
I still have to use translation, so… All right. Have a good week, folks.
**Juan Vega** 25:39 Thank you.
**Francisco Prieto** 25:40 Yeah, we.
**Hanson Ho** 25:41 Bye.
