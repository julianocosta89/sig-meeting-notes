SIG: Android SIG
Date: 2026-11-19
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Vishwan aranha** 01:50 Hey Cesar, how are you doing?
**Cesar Munoz** 01:53 Hey, Vishwan, all good, and you?
**Vishwan aranha** 01:55 Pretty good, just getting ready for the holidays upcoming soon.
**Cesar Munoz** 01:59 Oh, yeah.
Yeah, I'm looking forward to it as well.
**Vishwan aranha** 02:04 Next week is Thanksgiving, so I'll be off the whole week.
**Cesar Munoz** 02:08 Nice.
**Vishwan aranha** 02:10 And then, for December, 2 weeks for Christmas and New Year.
**Cesar Munoz** 02:15 I think that's the same for me as well, actually.
Usually, I save some… you know, a lot of people take vacation time in summer, But I always save… A lot of days, just for December.
I really love the… Taking vacations in that month.
See ya?
It was good to know, thanks for letting me know.
Probably… We might need to… Probably skip.
weeks in December for the overall meeting.
But let's see.
**Vishwan aranha** 02:51 Is everybody at some conference or convention today? Usually by this time, they join.
**Cesar Munoz** 02:58 Yeah, not that I'm aware of. I know that that was the case last week, but…
**Vishwan aranha** 03:03 Yeah.
**Cesar Munoz** 03:05 Not sure what's going on today. I will probably… I can wait up until 5 minutes fast, or something.
Yeah.
In the meantime, I know that Jason is not joining. I think he mentioned that.
It's got a… Yeah, he's got another meeting right now.
Yeah.
**Vishwan aranha** 03:33 I'm wondering if Ben on our side might join? He is mostly sick last, two days, so, he might not join, I don't know. Here he is, so…
**Cesar Munoz** 03:44 IRS.
**Vishwan aranha** 03:47 Hey, Brad.
**Cesar Munoz** 03:48 Hello, Ben, hey, Jason.
**Ben Joseph** 03:53 Sorry, we had a company meeting that was running a few minutes later.
**Vishwan aranha** 03:58 I dropped on time soon.
**Ben Joseph** 04:01 Yeah, there was nothing that chopped us.
**Vishwan aranha** 04:03 Yeah.
**Cesar Munoz** 04:06 Okay, let me… Okay, let's share my screen.
Yeah Okay, very light agenda.
Let's see… Evident hasn't added my name.
So the next release… Well, probably we can leave that.
for, for later.
Right. To the end of the meeting, just in case somebody has something.
They would like to raise… In the meantime… Let's see… Or if there's anything that you see on screen that you would like to discuss.
Otherwise, I think so far… I mean, there has been a lot of… a lot of PRs created, and… and there has been a lot of… There's been a lot of activity in the issues, but… I think so far, we've managed… a lot of stuff offline quite well, I will say.
Well, of course we can do probably better, especially myself.
this week has been quite busy, but I know I've seen Especially Jamie.
And, and, and Vishwan as well.
Very active there.
So… But I mean, if you would like to discuss something here… You know, just let me know.
Let's see…
**Vishwan aranha** 06:17 Not much, like, every day I try to keep up, but yeah, I'm… I hope I did not miss any PRs.
**Cesar Munoz** 06:24 No, and thanks for that. I mean, I think it's… Frankly, I think it's… like, when you say that every day you try to keep up, like, I felt that, you know?
**Vishwan aranha** 06:34 Yes.
**Cesar Munoz** 06:35 I, I, I, I, I, I think I understand that perfectly.
Of course, every, every… ever since the AIPR is starting to come up, which is great, in a way, we're making progress, but… There's a lot of stuff going on.
**Vishwan aranha** 06:56 Which may be partly our fault from Grafana, because when we put out our new role, the job description, we sent out, like, anybody who has experience with hotel, so they might have come just to, you know,
**Cesar Munoz** 07:10 But that's fine, that's fine.
Yeah, it's just part of the… They work.
I wonder if this is merged.
Yeah.
I'll take a look at these slides.
Well, one thing that I would like to mention, though, I don't know if I'm the only one I'm definitely not the only one.
just mentioned this before, is that I've seen some issues Created that look like… They hyper-focus on some potential errors.
That seem a bit… too specific. I don't know if I… Like, something like, well, if the device sits in idle mode, and then… It loses internet connectivity, and then this other thing happens, then this might cause an issue.
So, I think the way Jason mentioned.
this somewhere in Slack, I think.
Is that it seems like there are some issues that are created based on You know, just letting an agent take a look at the codebase and see what could go wrong.
Which, not all… not all of the time, are… You know, it comes up with issues that are actually, realistically happening.
So, maybe we can take a look at… Skip an eye on those, but… but… I mean, it's always fine. If, if, if… To address it if the fix is not huge, in my opinion.
That's fine, but that would be the only thing that I would say.
Quite strangely happening, from my point of view.
**Ben Joseph** 09:13 Cesar, are you finding that, like, such, defensive programming, is that, like, adding to the complicate… like, complicating the, maintenance, or, like… you know, adding… adding so many diff… That thing for the project. Is that… is that the reason? Or… How… what?
**Cesar Munoz** 09:34 Yeah, exactly.
**Ben Joseph** 09:34 do you feel? Is it, like, too many PRs? Or unnecessary PRs?
**Cesar Munoz** 09:39 No, I mean, anything that… help the… helps the project, it's fine. I guess my concern is… When it comes to… I guess… You know, trying to… trying to… Trying to add too much code.
for… I guess it's the… I guess my… my issue is when… when… When the issue is small and very unlikely to happen.
that we have to create a huge PR, or, like, a lot of defensive code, as you said.
For something that… that's very unlikely.
My concern, I guess, would be about… maintenance and… and… And probably performance usually are the two things affected when we add more code.
But… I mean, so far, the stuff that I've seen… I think has been… fine most of the time, so it's not… there's nothing that I could tell you right now.
you know, the point that, you know, look at this PR, this is too much, or something like that. But yeah, I've just noted that Probably in the future, we're gonna get maybe more of these kind of defensive PRs.
And… And I guess it's fine if we feel like… Maybe it's something we can add to the co-pilot instructions?
If we feel like the changes are… overly… I don't know… Focusing on something that it's unlikely to happen, and making the project too complex, probably we can pushback.
in those, but… but yeah, no, so far, I haven't seen a… specific example that I can tell you.
**Ben Joseph** 11:39 Understood.
Yeah, I think, like, there is, like.
I think, at least me, Historically, I've just looked at, like.
Is the issue, like, not so much focus on the issue of what is the probability of, you know, this happening in production, or how much we can reproduce this.
But, like, okay, there is an issue, and then, like, that's the fix, how the PR fixed that. So I think, like, maybe we can also pay some more attention to the issue in itself.
The likelihood… likelihood of that happening, and… maybe we, we, you know, we just don't check the PR and also the issue and, like, validate that as well.
Would that help?
**Cesar Munoz** 12:24 Yeah, yeah, and probably, yeah, I think that could help, and also maybe… Maybe finding a way that we event… that we, over time.
it's probably easier for us to flag these kind of PRs, maybe, as I mentioned, with maybe some instructions in the co-pilot.
reviewer… reviewer stuff.
So that… Because I guess… I mean, this hasn't happened, and I'm just… speculating here.
But if it becomes a problem, then I guess one risk of it… of these kind of things going on.
Could be that… we might miss important PRs, or PRs that actually have to get merged quickly, because, you know, we have to go through a lot of stuff that It's just defensives, bRs.
That might not be… Urgently needed, or something like that.
But yeah, I mean, we haven't gotten to that point. I'm just…
**Ben Joseph** 13:31 Yeah.
**Cesar Munoz** 13:32 Just think it out loud, mostly.
**Ben Joseph** 13:34 Just my concern with, like, putting up some sort of automation or, like, co-pilot instructions is that, like, it can discourage any sort of… Say we have a multi-threading issue, and, like, that requires significant re-architecture, like, should we discourage some… those sort of PR?
I'm not sure, like, how we can… differentiate.
those well-meaning PRs from… Somebody… I don't know, late.
bug, you know, GitHub for… working for GitHub credits, or maybe, I don't know.
That's…
**Cesar Munoz** 14:12 Yeah, I… I get what you're saying, yeah. I don't have an answer right now.
**Ben Joseph** 14:18 I know.
**Cesar Munoz** 14:19 But if somebody does… yeah.
Ideas are welcome.
It's still not a problem. Yeah, Hanson.
**Hanson Ho** 14:27 Yeah, I think as maintainers and approvers, we have to keep an eye out on this, manually, because There are… there are trivial bugs that… or issues that we wouldn't really want to deal with, but if it comes with a fix that is, modular, that doesn't change the architecture, and doesn't mess up the code, it's probably fine to merge.
If they're taking care of an esoteric problem with a rearchitecture, the juice may not be worth the squeeze. So it really is not… ideally, all issues are fixed, but it's the matter in which they are fixed that is potentially bad or good, and I don't know how we can have co-pilot instructions or anything like that, to kind of evaluate. We almost have to look at it, and if the issue is that the volume is too much for, one maintainer to kind of sort out, maybe this is the kind of thing that we do during the SIG, or we have a rotation where we do triaging. But… while this may not be a problem now, I think as the project gets higher priority and higher kind of visibility, it's so easy to stick Claude onto this and say, hey, find some issues and fix some issues, and the fixes sometimes are… They do what they are supposed to do, and the code looks kind of fine, but things get kind of messy architecturally, and entropy builds up and makes things bad.
And I don't know how to gate this other than with people being diligent. So maybe… maybe we just have to, especially for first-time contributors. So I feel different if one of us, like, added a bunch of fixes that are kind of relatively minor, but if it's somebody's first commit, and they come here with 10 small bug fixes that require tons of architecture changes, I would judge that differently than if it came from, you know, Ben or Jamie or me or something like that.
So… being vigilant is, I think, the only way of… Of handling this, and if… if the volume gets too much, we have to find a way to, share the load.
**Cesar Munoz** 16:39 Yeah.
Yep.
Makes sense.
Yeah, I agree with that. I guess the… Yeah. Hopefully it won't… I guess to come to a point where there's just so many that we… Can't even check if they don't change much for the architecture or stuff, but again, we haven't… Got into that point.
So… It's just that it looks like… A plausible future.
Based on the historical… events recently.
Bam.
**Hanson Ho** 17:39 I would also say the R is probably higher now, because we have these newfangled tooling to help us find issues that we would otherwise have not found, especially with edge cases, with multi-threading, and all that stuff. So, I think… It's hard for me to…
**Cesar Munoz** 17:55 Yeah.
**Hanson Ho** 17:56 know that there's an issue there, there's a fix, and not merge it, but at the same time, I completely understand, the amount of one-offs that could just mess up the entire architecture. So, it's almost like we need to get the project to a place where we don't have that, and maybe do it in a concerted way.
So that you can't just stick Claude on there and find 10 issues that require 10 different fixes and 10 different architecture changes. Maybe we have to do this proactively.
**Cesar Munoz** 18:25 That's true. I also wonder if there's something that maybe we can add here that… at least will make us trust the environment a little more.
Such as, you know, okay, I know that we have really well-configured, Lynch stuff, so that… I know people won't… won't mess up on… on… how to write good code, or AI.
or… I think we used to… I don't know if we already introduced… okay, we have instrumented tests.
Because I remember we used to have emulator tests running on every PR, and then we removed them because those were making the, this take quite long, but it wasn't that bad, so… I think we discussed about reintroducing them, and I don't remember if we did.
But that would be nice, just to have something running on an emulator.
But I don't remember if it's this.
suspect.
**Hanson Ho** 19:27 You can also add to theagent.md to basically give instructions about, how, when, you know, when more minor bugs are found, how they should be fixed, and what approaches they should take.
But we have to come up with what we want, which is… which is a fairly opinionated thing. But if we have some good ideas, we could probably help because the people aren't going to do this by hand. People are gonna… who do this, we're going to be doing it via agents. So if we have hints and instructions in our AgentMD, that might go a long way into kind of reducing the amount of, changes that are so big, and fixing things that are not worthy of that big of a change.
**Cesar Munoz** 20:20 Yeah.
So, for example, well, just to give an example of maybe something that you just mentioned.
So I'm working on a repo that… It's not this one, but essentially, Every… the release notes, it's something that you only update while creating a release.
And I know that this changes depending on the repo. Some repos, they… they prefer release notes to be updated on each PR that changes something.
So… I… I wonder… I guess this is the thing, because I was going to say, okay, maybe we can add a co-pilot instruction that says something like, well, if it was the case here, we will say.
There's not, I don't know.
release notes on HBR, unless it's for a release.
But then… I… I immediately… immediately thought, okay, but does an AI have to do this, or, can… can it just be a linked check? You know, things like that. I guess it's also a bit tricky to find the… the… I mean, I guess, using AI… It seems so easy at the beginning that it's probably… It feels like the first option, but… Yeah, I guess we should also try to find other main stuff, measuring stuff.
But yeah, Agent Instructions, I think it's fine. Any ideas are welcome, any PRs are welcome if you feel like there's something missing there. And of course, if we feel like there may be something going on a lot in different PRs. Over time.
Maybe that could be an idea of… What to add to the instructions.
Which, let's be honest, it's difficult to keep track of this events across many PRs, across time.
But maybe… that's the kind of thing an agent can help with. It's like, well, just check these past months of PRs and see what As being a recurring issue.
But yeah.
**Hanson Ho** 22:46 Yeah, so anything we can fix with deterministic tooling and Lynch checks, we always should prefer that, because AI isn't good at that. But I guess the AI instructions I was talking about is more towards giving hints to the person submitting the fix, and that agent, so not necessarily using AI to check their work, but making sure that their AI is prompted properly to do the fix in the correct way, because, you know, this is software. The same issue could be fixed 5 different ways, right? And if we could find a way to lead them down the path that we prefer. It's… it'll be preferred. So instructions will say something like, prefer to fix an issue with existing infrastructure without major re-architecture. Look for common patterns that have been reviewed and established, and use them to fix the same issue that happened elsewhere. Things like that, that are, that are additive, and not… not, you know, transformative, destructive, for first-time contributors especially, that would be… that would be useful.
com.
**Cesar Munoz** 23:54 Yeah, definitely.
Sounds good. I guess aside from that.
Again, if somebody would like to discuss something ad hoc, Please, let me know.
So far… Yep.
**Ben Joseph** 24:18 Yeah, sorry, if nobody has any topics, I just wanted some feedback on two different items.
**Cesar Munoz** 24:25 Sure.
**Ben Joseph** 24:26 one… one was mostly about, like, release, and, like, how do we do major version releases? Like, say, in… in one of the PRs, I think, that you had open. There… there is a potential, I mean, the ideal fix would mean that there is some sort of, signature change.
And we don't want to do that in the minor releases, right? So, if you are making such compromises, like, do we track that separately?
what is the criteria to do a major release so that, like, we can break APIs?
Yeah, looking for any guidance on that.
**Jamie Lynch (Palo Alto Networks)** 25:11 I don't think we got any written guidance that I'm aware of. I would say it would depend on the API, but my preference would be If we really do need to duplicate an API, then we'd… Depregate it, had to replace it with… annotation, so it was a green upgrade path, and then… When we do.
dump a major version, we could release, remove the old symbol, but I guess that would depend on… What sort of making change?
We're after.
**Cesar Munoz** 25:46 Yeah, mostly it depends, and… I was just gonna say that for the modules, it depends, but I guess for a high-level idea, the modules that have… that have this property then we must never break the APIs.
There, we could, for modules that don't have this.
But again, it kind of depends, because I know that in the past.
We still had some doubts about breaking Stuff, even in non-stable modules.
Not from my side, though, that's all I gotta say. I mean, if it's not stable, I'm fine with breaking it.
But if it's stable, then probably what Jamie just mentioned Probably the first path is just to… Annotated as deprecated, and then… From then on, Just… just remove it in the next version.
I don't know if that helps. Sorry, Hanson, you were gonna say something.
**Hanson Ho** 26:48 Oh yeah, I was saying, Jason and I were talking about this a year ago, about cutting a 2-0, or… 3-0? Or… 2-0, right?
Yeah, a 2.0 as a separate branch, almost, to basically make the API the way we want it to be, because I feel like the 1X API had just existed because it existed, for several years, and there's a lot of, not a lot of delateness to how stuff was introduced initially, and a lot of the patterns we don't want, especially now that we have Kotlin. We want to kind of expose a Kotlin API. And that is obviously a major API change. So it's… it's almost like… there is so much that we can't change in 1X, until we get a 2X. We should almost gather all of that and start thinking about what we want the 2.0 API to look like.
And basically, start working towards that. So it's… it's… if we release a 2.0, there are so many things we can change that we haven't, because we said, oh yeah, this is API breaking, we can't do that. Even for things that are not necessarily, like, even for unstable modules, we've been reluctant to change the attributes that is being recorded, for backwards compatibility reasons, we had, like, the legacy mode, and things like that. And… in theory, we should be able to change that in 1X, because it's, it's, you know, it's not an API break. And we… But the previous version wasn't really semantic invention or anything. But we were very careful about that. So, it's almost like we need to figure out A new baseline?
That we can then be actually careful about. And, That will take a lot of planning. So Ben, if you have issues that you think we should fix that will break API, we should start, maybe even, like, create a milestone that's, like, 2.0 API, and start tagging issues with them, and say, hey, we can't really fix these until we bump the major version API. And when we bump the major version API, we're going to be dropping a lot of old stuff that existed, based on Java, based on whatever.
And I think there are certain things that I think we definitely want in 2.0 API, which is Kotlin.
So, we want the Kotlin API to be stable, so that we can just bind directly to the Kotlin API, and maybe still support the compat mode in the SDK. Yeah, if we have a milestone, that's perfect, although we have no issues.
Yes.
**Cesar Munoz** 29:36 shot.
Alright, so, go ahead.
**Hanson Ho** 29:39 Oh, I'm talking for a lot, but… but basically, we should start just populating this milestone, and see what we need. Because it's high time we do this, because it's… there's a lot of things here that we're maintaining that are instrumentation that kind of sort of works, and it has different meaning, and there's no semantic conventions bound to it, and an API is Java, and all that stuff. If we can figure out what we want 2.0 to look like, then we can start building towards it, and basically make one X maintenance.
**Cesar Munoz** 30:12 Yeah, I agree with that. Ideally.
I would… I mean, I think it's clear that at some point.
we are gonna create a version 2.0, and that it should be based on the Kotlin SDK. At least that's the things that I had in mind so far.
I guess another thing that it should include is the, probably the new… Semantic conventions, Changes from the new repo, things like that.
So, so… Well, right now, we're waiting for… for those two things to be ready, the Catherine SDK and semantic conventions.
But I'll say that it doesn't look like it's… it's… Far away.
So, yeah, I think it's a great idea.
Ben, if you can, as Hanson mentioned, add The things that you would like to see that are breaking changes into this, into this milestone?
I'll probably add a couple of stuff, too, as the ones that I just mentioned.
And, it sounds good. So… Ideally, we should just… Create this based on… Koteling, and we have a lot of decisions to make, actually, because… We're probably gonna… but that's maybe a discussion for another time.
I'm pretty sure some people are gonna ask for… what's… what would be about the Java support?
Maybe… The solution to that is just to… Direct them to the version 1 row.
Broadly, that's… So, at the beginning… at the end, sorry, we'll have to kind of support these two.
versions, but… but I think it's… it's best not having to tie, I guess, too much.
this… this new version to… to Java-specific stuff.
Given that everything is moving to Kotlin.
So… but yeah.
**Hanson Ho** 32:29 Jamie's Python.
**Cesar Munoz** 32:30 Redirects up here.
**Hanson Ho** 32:32 Sorry, I was gonna say, Jamie's probably thought about major version upgrades, more than anybody here, so he probably has, you know, something to add, either here or, you know, in the issues.
**Jamie Lynch (Palo Alto Networks)** 32:47 Yeah, I'd also say that… I don't think it should be, like, a big, scary thing. Like, if we need to bump a major version, then… My preference would generally be… Let's try and batch up a few issues, or a few things we need to change, but, We don't need to change absolutely everything at once.
I think off the top of my head, I think we probably will end up needing to drop support for lower versions of Kotlin soon.
as, I think, 2.0 is… Deprecated, and has been for quite a while, so… as newer versions of Kotlin get released, we're gonna have to do a major version bump anyway soon.
**Hanson Ho** 33:37 Another thing we can do proactively is probably start marking stuff as deprecated, in the 1X line, so things that we don't want to take forward, we just mark it deprecated now, and then we will have, more license to remove it in 2X.
But yeah, we've… I think we've… we've traditionally been very careful about those major release day, because OpenTelemetry is so backend oriented. Cutting a 2X line seems like we are saying we are also going to support 1X and 2X concurrently, and I think for us, 2X is more like, this is the next version that we're gonna have, and unless it's a security thing, I don't think we're gonna backport anything to 1X. So that may be another reason why we should do this sooner and smaller than Than we would want, more than we have traditionally been.
doing, so… I'm all for getting.
**Cesar Munoz** 34:32 True, also…
**Hanson Ho** 34:33 Some 2-0 out there, so…
**Cesar Munoz** 34:36 That makes sense. I mean, we… I guess we're talking about all this… all of the stuff that the current APIs… I guess, lack.
And I can… I can spend the rest of the meeting explaining why I got to where it is today, and… And… and why I actually believe it's… it's actually way better than how it started.
But at the end of the day, we still have to… Add new stuff that sometimes we don't… Know exactly how much Would it be used, or… How exactly would it be used until we release it, and then people start giving feedback?
So… So, I guess… with this is, like, we have this opportunity to create this new API that will be cleaner for the version 2.0, But it definitely doesn't have to be perfect, and it probably shouldn't be complete.
Either, because… I guess the best… the best way to create an API is kind of organically. As people ask for new functionality, we add it.
So, I guess the challenge is to have something that is… that can grow.
Cleanly.
And so I'm a big fan of… You know, having this… Abstractions and these, you know, hooks to extend stuff.
I'm a big fan of this kind of, patterns, because I just don't know what people would need.
it should be flexible, but that doesn't mean it has to be, I guess.
thorough in the first release, as probably it's what Hanson was mentioning, and Jamie, so… so… I guess, Ben, if you have an idea of what you like.
definitely, let's create issues and add it in the 2.0 milestone. I was gonna ask, Hanson, do you think this is… is this related to the, new… client, SEMCOM migration, or is it something else?
**Hanson Ho** 36:58 No, this is… this is unrelated, and really… Got it.
Related semantic conventions, I think what we should do is make sure all the instrumentation report attributes are included in some semantic invention. But where those semantic conventions lay, either in the client-side repo or the core one, it doesn't really matter.
that is not being exported. What we're exporting is the instrumentation, and the Android repo will never have its own registry, that exports and is consumed outside.
So this is probably more of an implementation detail. The actual change is actually in the instrumentation, and we may already be using all the right keys, I believe, but Jason's already kind of done that. Some of them aren't using, keys, but we also should take a look at whether those instrumentation is something we want to carry forward as they are.
**Cesar Munoz** 37:56 But my understanding is that there are some keys that… We're planning to change.
When moving them to the new repo, right? To the new client CENCOM.
**Hanson Ho** 38:09 Yeah, and I think we have changed a bunch already, so, I want to say that the current instrumentation, a lot of it report keys that are, correct, that either are, part of a semantic convention or need to be submitted and accepted into a semantic convention. So, that is something we should probably do, but I would say that's the PR you looked at. That's more… that's more kind of internal implementation details.
We're swapping.
**Cesar Munoz** 38:39 Guys, well, this is an issue.
Yeah. Okay.
Okay, no, that's fine. I was just gonna add it to the milestone as the first issue there.
But it's fine if it's not there. I mean, we can do it offline.
**Hanson Ho** 38:53 There's probably a minimum bar we should add, like, you know, if we release 2.0 tomorrow, like, or… what should it, at minimum, contain? And I think the Kotlin API is one of them. And if we can achieve the minimum, then we can probably release, and if we have additional things that we can put in there, if people want, I think that would be… that would be helpful too, but as long as we can achieve whatever minimum we think, would constitute 2.0. Let's just do that, to what Jamie was saying. Let's not make this as scary as… as we're trying to build it up to be, that we've been traditionally treating it as.
**Cesar Munoz** 39:32 the lab.
It probably doesn't even need to have like, a fancy description or anything like that. We can change it later.
But yeah.
**Hanson Ho** 39:45 Yeah, I mean, this… this API as well as SDK, probably, but this will take probably a… a lot of sub-issues, because there's a lot of API.
**Cesar Munoz** 39:59 I mean, feel free, you know, to add them, but I really like the idea, so… I'm glad we discussed this.
Does that help you, Ben, with your question? Absolutely.
**Ben Joseph** 40:12 Yeah.
**Cesar Munoz** 40:14 Awesome.
What else?
**Ben Joseph** 40:20 But…
**Cesar Munoz** 40:21 Nothing. Yeah.
**Ben Joseph** 40:22 Sorry, sorry, I had one more, very open-ended, question, like, just wanna hear your thoughts on this.
**Cesar Munoz** 40:30 Sure.
**Ben Joseph** 40:31 how do we… like, I'm kind of thinking about, like, sampling.
But… More, more of a, tail sampling than head sampling.
And if that's possible on the client side, like, I've been looking at the current design, like, we don't have any way to do that, like, everything is based on, like.
We can decide for each signal at the time, and only when it's being generated.
But, like, I think there is a lot of value in you know, deciding… like, having some sort of tail sampling for, like, signals combined. So, just to explain what I mean, say, like, you're generating all sorts of signals on the client.
This might not be immediately relevant, to, you know, send it, export it to the collector, and, like, analyze this data. But, like, if we observe an anomaly on the client, and We decide that this session has become interesting, and, like, this can, you know, offer some sort of insight into an issue on the device, then all of that telemetry becomes relevant, and then we export it.
So, this is some sort of, like, something I've been thinking of, like, besides seeing with some other, products as well.
Is that something we can support, on the Android project, like, whenever I look at all the sampling kind of, support that we have.
it's not exactly designed for clients, like, right, all the Java, that's where we have all the seams or, like, APIs for this. It's on a per… signal and, like, at the time of generation. There's no tail, sampling support. Can we do this? I'm ready to, you know, create a design and, like, a proposal. But, like, just want to understand, what… if we have an appetite for this, or if we would kind of consider this valuable.
**Cesar Munoz** 42:44 I think it makes sense. So, first of all, I would like to just make sure that I understand What do you mean?
Because… I think, generally speaking.
The thing is that you mentioned tail sampling, and the first thing that comes to my mind is sampling that the backend does.
But the… the… I guess you're… based on how you phrase it.
It's… it's a sampling that is… built around this… the definition of a session, I guess, right? Because you're mentioning if something happens within a session that is interesting, then we decide to sample it.
Or not.
**Ben Joseph** 43:23 It may not necessarily be tied to a session, it can be, you know, last 5 minutes, like, so I… I… I write all the signals, instead of exporting them, I write them to a rolling buffer.
And maybe it holds 5 minutes or, like, 10 minutes of, signals. And if at all, at any point, something interesting happens, say an error happens, the last 10 minutes of signals get exported. Otherwise, like, we drop the rest of it, like, that's sort of, like, a crude design. That makes sense?
**Hanson Ho** 44:02 So that… so… that type of sampling is extremely useful, I think, for client devices, but… I don't know if it's compatible with how OTEL considers sampling, because as you said, the head sampling is about representative data. You're getting 1% of all traffic, and it's supposed to represent, be projected out, the 100%.
Once you start introducing tail sampling, you're basically selectively introducing additional data into the stream. So… how you make tail sampling compatible with, like, a percentage-based head sampling depends on how the percentage-based head sampling is implemented. So… if we are saying chopping by session, chopping by device, say, so sampling by device probably is the most prevalent way of reducing client data. So you have devices that report, those that don't report. So, are we seeing that for head sampling? We will just turn on 1% of devices to track.
And then for tail sampling, we will track the other 99% as well, and report the last 5 minutes, if something bad is happening? Or are we saying, within the 1% had sampled.
devices, we add more telemetry to the payloads if something else is turned on.
**Ben Joseph** 45:34 of the former, actually. Yeah.
**Hanson Ho** 45:38 So basically, 99% will be dropping data unless, a tail… something that will invoke its tail sampling. So if… if you're using, the data set to calculate DAU, you're gonna be overrepresented if a bunch of your previously not head-sampled, devices, start you know, reporting telemetry. so…
**Cesar Munoz** 46:04 what?
Yeah, sorry, Hanson, go ahead.
**Hanson Ho** 46:07 So, I mean, that could be done, but it would just have to be encoded in the data somehow that, you know, I want to use the dataset for a representative random sampling to project metrics, or I want to use individual devices or sessions to basically do deep investigations onto what is happening there. So… Somehow, something that has both head sampling and tail sampling, we have to kind of… be able to tell from the dataset that gets recorded. And I think Hotel does a good job supporting the former, and it may do a good job supporting the latter, too. I just haven't looked at it in detail.
So… So, maybe some investigations in how OTEL does tail sampling would… and then how to do tail sampling along with head sampling would be, you know, a good… a good thing to investigate. Like, how do we encode the data? Like, is it… is it… is it… part of, you know, the OTLP headers or something, so that we can tell, hey, don't include this data that's included because of tail sampling into how you calculate metrics, based on how you sample with Head Sapling.
**Ben Joseph** 47:23 Okay, like, so it's… the primary concern is good metrics. Other than that, like, if you can… say, If your, you know, crash rate, your sessions, and, you know, those kind of metrics are, you know, they are not sampled out, or, like, you are still, you know, sampling 1%, or, like, being consistent about that.
Can we, is there any concern with the rest of the data? Say, maybe just log statements, like, if you have, like, you know, plain logs that… ADB logs, or, like, the console logs, if you have… if you are sampling that kind of, data, or, Yeah, any, any, any, any part, any subset of that, that does not alter, like, the… the metrics that you actually care about. I understand, like, this might be very open-ended, like, people care about different things.
If we can filter that out, or somehow alleviate that concern, do you see any other problems? Other than, like.
Changing the, you know, one-person metric.
Sorry, Cesar, I think you were saying something.
**Cesar Munoz** 48:33 Yeah, okay, well, I just wanted to mention the… sampling, sampling.
I think it's an overloaded term, at least on what we do in clients, and compared to what's done in OpenCelementary, as Hanson was mentioning, I think everything about sampling that OTEL does right now, it's only for traces.
My understanding is that it only covers traces. I don't know if it already… Supports logs or other signals.
But the kind of sampling that I've seen, it's based on, and this is something that I think Hanson mentioned earlier.
On how the backend does.
sampling, and it's mostly oriented towards.
traces. We kind of do… I mean, we can do some hacks in Auto Android to… Sample all kinds of data.
But… The metric signal, it's quite difficult to sample.
It's not impossible, but it's kind of awkward. And we also kind of, like, in the client side, we don't like… worry too much about sending metrics anyway, so… so we haven't thought about much about it. So, I guess… what I'm trying to say is that what you're saying, I don't think it's impossible.
it's just that I don't have a clear… Vision of what it's, like.
I will need some details, like, when you're talking about sampling, are you talking about all of the signals?
as one thing. Then, if you're saying that, then we're kind of talking about a session. Like, grouping them by session and sampling the entire session is something that we've already discussed previously, but then they're mentioning, well, it doesn't necessarily have to be part of a session, it's mostly about, like, a window of time Before the interesting… Event happened.
So, so then, we're talking about time-based batches of data.
I don't know if you're talking about, okay, if it's time-based.
We still want to exclude some signals.
Not because we're not using sessions, then that doesn't mean that we… we… we want all of the signals in this, in this, you know, sampling or stuff. Like, you're talking about something very custom, but at the end of the day, it's… I'm just trying to grab my head around how can it become something generic, you know, something that is useful For, like, most apps, and configurable enough.
And if it's too specific, I guess if it's way too specific, then… probably we should not add it into Autel Android, but I think I still don't understand, well, the… the… I guess, the requirements.
So, yeah, I don't know if Hanson… Yeah.
It's my name.
**Ben Joseph** 51:43 Good.
**Hanson Ho** 51:43 I think OTEL's tail sampling, requires, I think the… maybe the root span to be saying, am I sampled out and am I not sampled out? And then you basically have the child spans, add additional context to it, and then when we export, and this is assuming it's on, basically, for every device, 100%.
So, the sampling happens at the time of export. So, we drop it, or we keep it.
If we want to do, kind of, tail sampling, with the 99%, then… there's some logic, I guess, that has to exist being exported to say, oh, this is important, even though technically this whole trace is not sampled, or is not supposed to be exported, I'm gonna export it anyway. And that's the, that's the last, you know, 5 minutes of data. And that's assuming you can put everything in this, in the trace. So adding, you know, child spans to that trace so that you can have that kind of extra detail. You know, to what Cesar is saying, I don't know if… I don't know how that would… interact with metrics. I don't know how that would interact with, logs, or how that would interact with, kind of, server-side derivations of metrics via, the telemetry we send. So, with spans and stuff like that. So, if you're saying a device never sends telemetry, and basically 99% always when we export, we just drop it.
Suddenly there's gonna be a bunch of these guys that are not supposed to send, but you're receiving telemetry because of tail sampling.
how would the backend account for that? Maybe they could do that by looking at the trace header and say, hey, this is not supposed to be there, and just drop that, you know, device from consideration. So, there are probably things that can be done, but probably the scope of what can be sampled in and out We'd have to consider, and also any implications of deriving metrics on the back end from telemetry that we send.
Would have to also be considered. But… Yeah, I would take a look at what… How to do this with, with… The way the backend does tail sampling, and how we… what things we have to do to adapt it to client.
Because if it's only tracing, then… then… We'll only have tracing to consider.
**Ben Joseph** 54:12 Yeah.
**Cesar Munoz** 54:12 Yeah, true.
**Ben Joseph** 54:15 Yeah, I get, I think I get the, at least the bigger areas of concern, so… I'll come back with a more… so, basically, the general idea here is to… reduce telemetry volume, but still keeping meaningful data. That's… that's… that would be the high-level goal. I am trying to figure out the specifics, so I… that's so… that's why it was very open-ended, but I think I understand their concern, so I'll… I'll come back with more specific questions, probably.
**Hanson Ho** 54:47 I think the use case that you described is going to be very, very popular, because…
**Cesar Munoz** 54:53 It sounds really good.
**Hanson Ho** 54:54 So, it's… someone… we need to figure out how to do it in the client with Hotel. So, that's that.
**Cesar Munoz** 55:00 And probably in a… in a fairly generic… Way, or at least configurable enough.
So, yeah.
**Ben Joseph** 55:12 Thank you.
**Cesar Munoz** 55:14 Thank you.
Okay, so we have 5 minutes left, the… I guess this is something that Jason added.
So the last release was, I think, 2 weeks ago.
But it was a patch.
So… I don't even know if the upstream has released recently.
Probably they did.
Yeah, I think it's… it's due for a new release.
So… I can probably just… Started.
Right after the call, and then whoever's available to Give some approvals.
I'll mention it in the… in the Android.
group in Slack.
But yeah?
I'll create one.
And if there's anything… I don't know, you think should be in the release?
At least not something that I'm aware of, just let me know.
But yeah.
I think we're… basically on time.
If there's nothing else, I'll say… can grab out here?
**Ben Joseph** 56:33 Hi, Cesar. I think, like, we have a new member on the call, like, I don't know if they want to introduce themselves, say hi.
I don't know if they're joining, but…
**Cesar Munoz** 56:43 Gosh.
**Ben Joseph** 56:44 Yeah.
Yes.
**Cesar Munoz** 56:47 Welcome.
**Yash Raghubanshi** 56:48 Hi, I, I saw some eye self Yash, and it's my first meeting.
So… Like, I want to know the path… I want to know the path, and what's going on, like… In the milestone or something.
**Cesar Munoz** 57:07 Yeah, yeah.
Welcome, you know, well, usually the process is… As essentially we, we… Add ourselves into the meeting notes. If you have specific questions, add them to the agenda.
And… and everything else we can just discuss over… over Slack, the CNCF Slack.
I don't know if you were joined there, but yeah.
**Yash Raghubanshi** 57:34 I joined.
**Cesar Munoz** 57:34 And, and… So yeah, feel free to… well, first of all, welcome, and feel free to ask any questions.
There.
**Yash Raghubanshi** 57:43 No.
Not any question, like, I just want to know the process and everything.
**Cesar Munoz** 57:50 Fair enough.
Awesome.
Okay.
If that's it, then, I guess, thanks for joining.
Thanks.
**Ben Joseph** 58:07 Bye.
**Yash Raghubanshi** 58:07 Thank you, sir.
**Cesar Munoz** 58:09 Hey.
