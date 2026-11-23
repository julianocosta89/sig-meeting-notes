SIG: JavaScript SIG
Date: 2026-11-18
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Trent Mick** 00:43 Hey. How you doing?
**Marc Pichler (Dynatrace)** 00:45 Hello?
What's it going?
**Trent Mick** 00:47 Until half a second ago, I was gonna say we have to do a get-out-the-vote thing or something, if it's just two of us showing it, but…
**Marc Pichler (Dynatrace)** 00:53 Alright, fantastic.
**Trent Mick** 00:54 stuff.
**Marc Pichler (Dynatrace)** 00:55 Everybody joins at the same time.
Yes.
**Jamie Danielson** 01:08 Hallelujah.
**Trent Mick** 01:08 Oh, no. Hello. Hey.
**Marc Pichler (Dynatrace)** 01:19 All right, welcome everybody, and it's go… So, it's done.
First thing on the agenda here, there are two new security advisories I think they also receive TVs already, so, Just so that everybody is aware, this is a continuation of one, advisory that we had for instrumentation HTTP, it's… Like, all the other… HTTP instrumentations also were affected by that, so… That's all fixed now in the latest version.
Just an FYI.
While we are talking about FYIs, I just wanted to let everybody know, I made some changes to the renovate config in core so that we get more dependency updates without actually having to click approve in the dependency dashboard. So if you notice any PRs that are… weirdly grouped, or not mergeable, because they are grouped in with some package that often changes, please let me know, and I'll try to, change the renovate config accordingly, so that we can Update a bit quicker in the future.
they should be all coming in on Monday, so… If you see a bunch of PRs on Monday, don't be alarmed, this is… The way it is now.
Moving on to the next one, This is just a general question for everybody, so… on the OTRP transformer package, when I did the rewrite, instead of Protopath.js.
We are now using this, custom hand-rolled implementation. I made a trade-off where I did a double pass, to, like, figure out what the size of the OTRP message in Protopuff is going to be, so that we don't over-allocate.
And so that we don't end up with a buffer that's, yeah, larger than what would be needed. But the trade-off was that doing this double pass, also takes more time.
Hang Chong, did hear, some tests and found that actually removing it makes everything a lot quicker. This was also, like, the same thing that I saw when I did the implementation. I was just wondering if anybody has any objections to us going with a naive growth approach, where we start with a 1KB buffer and then just keep doubling it.
As we write into the buffer.
One of the… Situations that might come out of that is that, As there are larger, OTRP requests being formed, if you have, let's say, a 32MB request, and that grows beyond 32MB, you could end up allocating another 32MB.
Which… could lend your service into a situation where it gets, OOM killed.
So… we gain some in CPU performance, but we lose some in, memory.
**Trent Mick** 05:15 This is… sorry, if we hit… is that the max size? You're saying we could hit double the… what the max size allowed is, or almost double if we get unlucky?
**Marc Pichler (Dynatrace)** 05:25 Yeah, it could, like, if we get unlucky, where a request is,
**Trent Mick** 05:31 Because the thing will serialize, and then later the max size is applied? Sorry, I… sorry to jump.
**Marc Pichler (Dynatrace)** 05:37 So the way that it works, let's see if that's… I think that's not touched here in this diff, Protobuff Writer is the one.
So just always doubters.
When it runs out of space.
So, ensure capacity is run here, and… Let's say the buffer is already at 32MB.
And you get a new span in that still needs to be serialized, and it's, like, 15 kilobytes or whatever.
It doesn't know that beforehand, so what will happen is it will go in and grow the buffer by 2X.
**Trent Mick** 06:18 Yeah, yeah, yeah.
Yeah, gotcha.
**Marc Pichler (Dynatrace)** 06:20 Yeah.
**Trent Mick** 06:23 I don't have a problem with it.
But I could see someone for some… really, I guess, constrained environment, but wanna… Have some cap there?
**Marc Pichler (Dynatrace)** 06:40 Yeah, and then…
**Trent Mick** 06:42 Yeah, go ahead.
**Marc Pichler (Dynatrace)** 06:43 when I did the rewrite, I just wanted to keep the behavior as closely to what we had before as possible.
And, that's why I went with the approach of actually doing a double pass.
Since then, Protobuff.js has actually also changed their implementation to not do a double pass anymore.
So… It seems that there's some precedent to… Leaving it out.
**Trent Mick** 07:15 So I would think the common case people would definitely take The speed. Win.
Or people, like, in general, most people would prefer that. If there are more constrained environments, then maybe they come back and we want some way to configure a… one that biases towards lower memory usage. I mean, there's always this trade-off, right?
Memory versus CPU.
**Marc Pichler (Dynatrace)** 07:41 Oh, really?
**Jamie Danielson** 07:42 I agree with that also, based on stuff that I've heard, the speed being important.
**Trent Mick** 07:48 Let's be honest.
**Marc Pichler (Dynatrace)** 07:50 I think with this in particular, you're also ending up This is all done in one go on the, event loop.
So, there's some event loop lag that you will run into with that not being fast, so I'm also fine with… button.
Actually, just going with the more performant… the more CPU-performant route here.
**Trent Mick** 08:23 Oh, this can cause… Okay, yeah.
**Marc Pichler (Dynatrace)** 08:27 Yeah, because there's this huge chunk of stuff that you need to serialize, and it tends to be quite a bit of work.
to do.
**Trent Mick** 08:35 Was that not the case with the current implementation?
**Marc Pichler (Dynatrace)** 08:38 Yeah, that's, that's exactly the case with the current implementation, and also was worse with, when we still used protobuf.js, because it, I think it was about 50% slower.
Yeah. So we gain another… I don't know how much… It is… We gained quite a bit. Yeah.
**Trent Mick** 09:00 Okay.
**Marc Pichler (Dynatrace)** 09:01 Then I will approve this PR, and… If anybody comes, our way with… One thing that, Different behavior, we could still look into bringing it back and making it configurable or something.
Oding.
**Trent Mick** 09:23 There was a… on the node-adding Core, or some hotel support to core, There was some debate.
That… On one of the issues on whether to have node… bundle OTLP transformer so that there's one shared implementation of the protobuf serialization.
And deserialization, but mostly serialization.
Chen Zong was on that side arguing.
Or considering having just one out there instead of Node having its own, and us… we having our own, so… If ECPR is coming in to accommodate that kind of thing. So, like, for example, one of the arguments against a node using OTPL Transformers. It has dependencies on core and on… One other module for two small… No, like, you could easily drop those dependencies if you wanted to, so… Just be aware of it.
if… if that does progress, I'm guessing the way it's gonna go is, no, it's just gonna say, we don't want to bother, but… Because it is just kind of a… a small… Small depth, so… anyway.
**Marc Pichler (Dynatrace)** 10:32 Yeah, also, just thinking out loud here. One of the reasons why the OTP transformer package is the way that it is, is also that we just want to accommodate our internal data model exactly as it is, without having to go through an intermediate transformation step.
And Node.js will end up having to do… what's… Like, having to do the thing that we got rid of.
So I would, see why they are not happy about taking that dependency as well.
Because they would have to change what they're passing.
To just make that happen.
**Trent Mick** 11:17 You're saying their span shape would have to be the same as our span implementation?
**Marc Pichler (Dynatrace)** 11:21 Yeah, exactly. And that might just add some overhead that…
**Trent Mick** 11:25 Yeah, yeah.
**Marc Pichler (Dynatrace)** 11:26 not be acceptable.
I also found that…
**Trent Mick** 11:32 Interesting. It might be the same shape, but then… compatibility down the road becomes kind of annoying, maybe.
**Marc Pichler (Dynatrace)** 11:38 Exactly, so if we want to go to 324. And we change the shape that we export, then Node.js would also have to change the shape, just to match what… whatever we came up with, what fits our implementation.
I guess that might add some overhead there.
**Trent Mick** 12:01 Okay, okay, noted, thanks.
**Marc Pichler (Dynatrace)** 12:11 Alright, moving on to the next one, if there's no comments or questions about the… Previous topic, is… this here… so I just had a brief look. It's kind of unrelated to your PR trend, because this already existed before this, before this PR. I… Was going over the types that are, being exported in, Like, these generated schema types, and found some issues that might cause us maybe a little bit of trouble in the future, mainly because of the TypeScript types being the way that they are, and Node.js being able to install two versions of the same package.
Or, like, with NPM, that's possible. So… I found… Break.
these few here. I think the main issue that we might run into in the future is that the experimental types, are now all together in the types that we see right now.
And… Once properties disappear, we might run into a problem where, like, there's a new minor version of our package that uses a newer config model.
And then it's not assigned a bird anymore to… An older version, and… That's essentially the same problem.
That occurs multiple times, with a few different categories of changes that the config SIG could make.
So I just wanted to bring it to everybody's attention. We probably won't be able to find a solution right now.
But I think, keeping that on the radar might be important.
**Trent Mick** 14:09 Okay.
Yeah, I saw this, thank you. So… I… first, I'll use that and create a separate issue, so we have a place so we can discuss it, because this is going to get closed, or merged.
So, to… talk about the different categories of things there. The experimental types, the versioning… dot MD that… lives in the config repo does basically say, like, no rules for things with experimental or development in them. So, I don't know if that absolves us.
you know, if… or if, like, we could help that situation a little bit by adding docs to our thing, saying, if you're using the experimental ones, like, it's gonna break into minor, and as well, this is JS, where… The diamond problem isn't a problem, which means the problem's your problem.
If you know what I mean.
so that people have to be aware of that, and, like, the warning that's in version.md, I'm sure you read that too, was that,
**Marc Pichler (Dynatrace)** 15:11 Yeah.
**Trent Mick** 15:12 like, be careful, you're gonna get breakages and minors if you're doing that. So I don't know if that absolves us for that issue. The other ones… Yeah.
**Marc Pichler (Dynatrace)** 15:22 Yeah, I think, it… Thus, if we structure the package in a way that it's a bit easier for people to consume just the stable ones.
So maybe via a different entry point, or having two different types.
death.
Only include properties that are typed with staber subtypes.
I don't know if that makes sense, but…
**Trent Mick** 15:57 I know what you're saying, but my head explodes a little bit, because… there are experimental nodes at different parts all over the place in there. So, like, a stable node at the top-level tracer provider deep down somewhere in there, there's a… a development thing? Do we want a top-level So, like, right now, the top-level type is configuration model, so do we want an experimental configuration model that is… The full thing, and then a configuration model that only has the stable bits, and… Is that really required, or… I don't know.
**Marc Pichler (Dynatrace)** 16:34 Yeah, I think that is, like, the fact that there's… different experimental types on each of the levers is… The main, the main difficulty that we're facing here, because… just types disappearing is actually not that bad. It's just that they are used in types that are already declared stable. That causes trouble when you're then trying to, When you then have a type that actually only uses Things that are stable, but also there's this experimental section of it that's in there.
You cannot… Assign them together later.
Yep. Because it will fail to type check exactly on the experimental parts that changed.
Even though people don't use them, maybe.
**Trent Mick** 17:24 So, do we… this is me being the naive… Devil's advocate here. Do we feel that it is… A problem that we need to solve, because… users will invariably get into the situation where they have two versions of the package installed, and there's not a meaningful solution for them. Is that…
**Marc Pichler (Dynatrace)** 17:46 Yeah.
**Trent Mick** 17:47 Experience.
**Marc Pichler (Dynatrace)** 17:48 that… that is the thing that we experienced in the past with, quite a few types. I don't exactly remember which ones they were, but, we went through the… or, issue where we had.
Classes and private properties on these classes that would cause a version mismatch.
it would cause a tight mismatch between two different versions.
And people ran into that all the time.
And I would think that something similar would also happen with, SDK config.
I'm not sure, like, how often it would happen.
I would think that it could happen more often with the config things, because it just changes more quickly.
Especially as new things are added.
And it's also out of our control, when it changes.
**Trent Mick** 19:01 Yep.
I mean, it's when a release for a new thing is, so… I mean, or for a new version of declarative Config.
But yes.
I just… I can't think of a solution that doesn't explode, right? So if we need configuration model and experimental configuration model, and configuration model is processed to drop any of the experimental bits.
then… the parse config file.
export from SDK Config needs Parse, an experimental parse.
and then start node SDK, and SDK node needs…
**Marc Pichler (Dynatrace)** 19:41 Ours of both, yeah.
**Trent Mick** 19:43 needs to… That, or you have the same export from two different… from the top level, and from an experimental or incubating entry point underneath, which is then confusing, because you probably want separate names, because otherwise… you get a bug report for using start node SDK, and it's which start node SDK are you using? Ugh.
Okay, I don't even… I don't have a good sense of how that shakes up.
**Marc Pichler (Dynatrace)** 20:13 It's…
**Trent Mick** 20:14 Or if, like, here's the naive guy, I just want to say, like, just… Please don't do that, and let's… Hope for the best and move on, like… hope is Trent's strategy, at least.
**Marc Pichler (Dynatrace)** 20:30 I guess we could, So one of the, things that makes this a bit more complex as well is that people usually don't run into this while the package is still experimental, because the way that NPM reserves the packages, the caret ranges.
They get stuck.
**Trent Mick** 21:01 on an older version for a long time and don't notice. And then 1.X comes up, and then they…
**Marc Pichler (Dynatrace)** 21:06 Is that what you're saying?
**Trent Mick** 21:07 Because it is a breaking release all the time, so while we're 0.x, it's all fine.
**Marc Pichler (Dynatrace)** 21:12 Yeah, at zero.xes are fine, because, like, even if they depend on a carat, range, they just… won't get, like, a newer version of the SDK pulled in.
**Trent Mick** 21:24 Right.
**Marc Pichler (Dynatrace)** 21:24 And then suddenly we release… we think it's not a problem. We release… A stable version of it, and then… 4 or 5 major versions in. We… Figure out that it actually is a problem. And then we would have to go To the next major version to actually clean all of that up.
Which is what I'm… A bit worried about.
I can… Prototype a few ways to maybe work around that and see if it would be Completely terrible, or, if there's… Maybe a better way to work around it.
**Trent Mick** 22:11 I'll do prototype, and we just drop TypeScript.
No DTS files, no TypeScript, nothing to…
**Marc Pichler (Dynatrace)** 22:21 That's true.
**Trent Mick** 22:21 Yes, that's it.
Fairly.
Okay, so, okay, so I'll… I'll merge this to another issue we can discuss, in… Er, open another sheet with this, and then merge this.
And… Yeah, okay, but we do have to be aware.
Yeah, okay, thank you.
**Marc Pichler (Dynatrace)** 22:51 Alright, moving on… To the next one…
**Trent Mick** 23:00 Yes, we should.
Go ahead, sorry, 3 weeks, go ahead and come back.
Yeah, that's me. I had, reviewed it earlier with Wolfgang, and then… delayed until 3.0, so… yeah. I or someone else is welcome to get on that.
**Marc Pichler (Dynatrace)** 23:19 I just stumbled over that one today, so, I guess it just needs an update to whatever is…
**Trent Mick** 23:30 I think an update to take a look. Yeah, I might appreciate your help on the release scripts, because we're gonna have to have a separate release category for that.
**Marc Pichler (Dynatrace)** 23:36 Right, yeah.
It's probably fine to merge this… As it is right now, and then I will follow up with, With a script tool.
Parcel.
**Trent Mick** 23:58 Or maybe… maybe we want to wait, like, we can get a release out, and then put this, so that we're not… Anyway, whatever. At most, this would cause a couple-day delay as we sort out the release process, but yeah.
**Marc Pichler (Dynatrace)** 24:09 Yeah, I think… oh, sorry, go ahead, Jamie.
**Jamie Danielson** 24:12 I was just gonna ask, is this, like, just the script and everything, but, like, doesn't run it yet?
Since the new release isn't out yet.
**Trent Mick** 24:24 The new release.
**Jamie Danielson** 24:25 Sorry, the Gen AI package… Like, the Gen AI semantic conventions hasn't done a release yet.
Though we are planning to finally do one.
**Trent Mick** 24:35 I think this one built on a GitHaw, because there wasn't a release yet. So, would love to know what the status is there.
**Jamie Danielson** 24:43 So, in yesterday's… SIG meeting, We decided we should just go ahead and do at least a dev release to start.
like, you know, using the release levers, see how those things go. So it'd be, like, a dev release, and then an RC release, instead of… Continuing to wait.
For more breaking changes.
**Trent Mick** 25:05 Do you know what version you're gonna use?
**Jamie Danielson** 25:08 It's gonna be something like 001.
dash dev.
Or something.
**Trent Mick** 25:13 Okay.
**Jamie Danielson** 25:14 like, one of those. I don't know, I haven't heard the last time… the last time I remember talking about version numbers was, like, 8 months ago, when we thought we were gonna, like.
Turn shit around real quick.
**Trent Mick** 25:25 Okay. So the only concern here about this one eventually mirroring the version of GenAI is if the upstream Gen AI SEMCOM repo is super stingy about new versions that were stuck ahead of it on… on a higher version number for a while until it gets past us, so we can sync up, if you know what I mean. So, like, if we released a 0.1 and you guys started with a 001.
**Jamie Danielson** 25:54 Yeah.
**Trent Mick** 25:54 Oh, oops, we're ahead of the… 8-ball or not, but,
**Jamie Danielson** 25:58 But at least if we're starting… 001. Although, even this, though, I guess, we would have…
**Trent Mick** 26:03 on dev, then we're gonna do dev. Oh my god.
**Jamie Danielson** 26:06 We would be better off having a dash dev or something, because 1001 official comes out.
now we're not matching, right? And then if another release doesn't come out for a while, we're not matching for a while.
**Trent Mick** 26:20 Yeah, so, okay, so if you guys definitely are considering just a pre-release, then we should probably do a pre-release here, too.
**Jamie Danielson** 26:26 Yeah, there's another meeting this afternoon, that I was gonna attend, and I can try to find out for sure at least what the version number is that we're thinking.
And then that way we can kind of release them.
Together.
**Trent Mick** 26:40 Okay.
**Marc Pichler (Dynatrace)** 26:45 Sounds good, yeah. One thing that I would note about, like, if we merge this as it is right now, then on the next release, no matter Which version it… gets bumped to in the meantime or not. It will just release.
Whatever's on main, at the point.
that we do the release. So, for example, if we do a core release.
Without including any of the SEMCOM stuff.
then Luna will detect this as an unreleased package.
And just publish it.
Because it's not there yet.
I guess the publish will fail anyway, because we haven't created it in NPM, so…
**Trent Mick** 27:37 Wait, that doesn't happen for…
**Jamie Danielson** 27:41 Do we have… is there, like.
**Trent Mick** 27:42 That doesn't happen for semantic conventions, does it?
Doesn't that one get incremented, or no, it doesn't.
**Marc Pichler (Dynatrace)** 27:47 So, semantic conventions doesn't get incremented, when we do a release.
**Trent Mick** 27:52 Yeah, no, I gotcha, I gotcha. So, if we put dash dev in there, does that suffice, or…
**Marc Pichler (Dynatrace)** 27:57 If we put dash def in there, it will, It will still get released, but as a, cannery, tag.
So it won't have made list, it would have a canary.
**Trent Mick** 28:21 That's cool, I think, for a pre-release. I think that would be fine, and someone could… At least use it locally, if not… yeah, okay.
Okay. I put a comment on the thing, but I'll put it back. I'll put this on my… On my radar to review.
**Marc Pichler (Dynatrace)** 28:37 Thank you.
Alright, I will keep an eye on that one, as well, over the next few days, if there's anything, that I can help with, please also let me know. I'll try to… Find my way around the release scripts again, and see if there's… if we can make that a bit more generic when we add more SemConf packages, because I suppose GenAI SEMConf is just the first one that's gonna pop up. There's probably gonna be more in the future.
**Jamie Danielson** 29:20 Yeah, the plan is to just start doing more federated SEMCOMF.
**Marc Pichler (Dynatrace)** 29:33 Brights.
I put here if there's some time left on the next topic, so Trent, if you…
**Trent Mick** 29:43 No, that one's… good. I… I want that one to go in. I was gonna pull it out of draft, just… Right before. So it's still in draft?
**Marc Pichler (Dynatrace)** 29:53 Yeah, I think I looked at it earlier today, and it, looks… looks good already, so if you… Now it's open, so I will just… Review that one, and Yeah, maybe one thing that was kind of a semi-open question was the comment that I put on the previous PR.
About… the override and warning part, where I had a concern that, if we allow Custom component registries, and people use a key that's then Being taken up by the built-in registry that would cause a breaking change.
**Trent Mick** 30:41 Does this answer your concern or not? There's still technically a break in that the users wanting.
**Marc Pichler (Dynatrace)** 30:46 Yeah.
**Trent Mick** 30:46 just warned away.
**Marc Pichler (Dynatrace)** 30:49 I think… so… I didn't know that the spec was… requiring us to actually throw in that case.
So when I read your comment, I was… A bit surprised about it.
Given that the spec says that we must return an error, I would maybe say that We throw, and just see what happens.
FD.
**Trent Mick** 31:30 So what I did say in another comment on this thing, and it… so it was a different one where I had a to-do, and I was asking opinions, on whether… sorry, what the behavior should be if a person calls start node SDK with this new option.
And passes in two registries that conflict. Right now, it throws, so that means Start Node SDK is gonna crash the app.
Yeah, if we start from a throw, then we can move to warn and give them a no-op SDK later as a behavior.
**Marc Pichler (Dynatrace)** 32:01 Zoom.
**Trent Mick** 32:01 That's kind of what you're saying, yeah.
**Marc Pichler (Dynatrace)** 32:03 Yeah, exactly.
**Trent Mick** 32:05 If we start from just Warren, we can't go to throw later, that's without a break and change.
Yeah, so… Okay, so yeah, if you're cool with that, I mean, review the comments that I had in up here, I think.
And this is a starting point.
**Marc Pichler (Dynatrace)** 32:21 Yeah, I think I'm… I'm okay with it growing for now, and… I'm not sure whether that part of the spec is stable already or not.
**Trent Mick** 32:33 It is not.
**Marc Pichler (Dynatrace)** 32:35 So Could be that this gets revisited anyway, and we might have to change it later, so… I think throwing now seems like the best course of action.
**Trent Mick** 32:49 know what Python does, having looked, because I think they support I think they spoke about providers?
I'm not sure, I'll have to ask. Java, I'm not adept enough to know whether, through the SPI interface that they're using for extensions.
Whether that will throw if there are two… Extensions added that both try to implement the same named Component type.
whether that actually throws, or what the behavior is in Java?
Like, does that crash at load time, or not?
**Marc Pichler (Dynatrace)** 33:25 It's been so long that I also don't remember anymore.
**Trent Mick** 33:29 So, yeah.
**Marc Pichler (Dynatrace)** 33:33 Erin.
I guess, in any case, throwing is… SPAC compliant, and fine.
**Trent Mick** 33:42 Okay, so I just pulled this fear out of draft. It looks like I still have an X on… oh, we'll see, on the CodeCov.
coverage. If that's dropped too low, then I'll look, see what lines aren't covered, and I'll add some more tests for it, but… Otherwise, I think that… Functionalities there.
**Marc Pichler (Dynatrace)** 34:01 Alright, sign myself.
Sure.
**Trent Mick** 34:06 And then the follow-up is I'll do a thing auto-instrumentations node. I think after this, we can get it supporting declarative config and using start node SDK.
**Marc Pichler (Dynatrace)** 34:16 Sounds good.
Right?
Yes, let's move on to… Next one, then.
**Trent Mick** 34:34 Yeah, so… With Jackson here, because Jackson has one implementation of this.
Let me try to find a PR.
You open up here.
Potentially. Go look at the changes.
And look for wildcard.
Oh, wait, there you go, duh.
Okay, so I haven't looked at the implementation, but this is a wildcard matcher, so star and… Question mark as the… That's the meta-characters for that.
Implementation that doesn't use Reg X. There's a wildcard matching pattern in SDK logs for supporting wildcard matching on the logger configurator, one of the attributes there. It does use Regx. We should not use REGX if we can avoid it, because you always get a RDOS from these things, so we'll get a vulnerability report in. I'm surprised we haven't had it for SDK logs already, but it'll come.
So, we should be using that. There are a number of, features in declarative Config that That require using a wildcard matching pattern. And so I'm wondering if throwing it in core would make sense?
**Marc Pichler (Dynatrace)** 36:05 Yeah, there's also one in… Sdk metrics.
Or the view, instrument name matching.
Oh, is that interesting?
**Trent Mick** 36:15 implemented already? Okay, yeah.
**Marc Pichler (Dynatrace)** 36:17 Yeah, so… Core is probably our best.
**Trent Mick** 36:24 I think there's… Because I think resources needs it, too. Yeah, it does depend on core already, so I'm thinking core is the best place.
**Marc Pichler (Dynatrace)** 36:35 It's one of those few things where a core is actually the right place for it.
**Trent Mick** 36:41 close to everything else in Core. Yeah.
**Marc Pichler (Dynatrace)** 36:44 Yeah. So I think I'm fine with it being in core. I think that's the best case for it.
**Trent Mick** 36:49 Okay, I don't know if it'll be exactly this function, or if it'll be something… because we also want… I think it'd be nice to have a little bit that generic thing for handling the includes-excludes.
Both of those… the whole interface, that's common in… at least a few of the declarative config things in a way that's shareable between them, so… Jackson, this is another way of me saying that I will finally get back to this PR.
I think we'll probably maybe merge this as is and have a separate PR that's looking at coming up with a common interface that all these places can use, because there's no reason that this PR needs to be changing SDK metrics and SDK logs.
As well, so…
**Jackson Weber** 37:25 Perfect, that makes sense. Nice, thank you. I really appreciate you taking a second look at this guy.
**Trent Mick** 37:31 For sure.
I think that's all I had.
What else?
**Marc Pichler (Dynatrace)** 37:43 So I guess we have a way forward for this one. Maybe while we're talking about, where to put Shared.
We could talk about, the… redact URL.
Bing.
That we added in each of the packages to fix the security advisory that we got, last week.
I've seen that there's one request open already, and they…
**Trent Mick** 38:25 Was that within 20 minutes of us opening up here? Anyway… I'm joking, I didn't… It was within 2 days.
**Marc Pichler (Dynatrace)** 38:35 Yeah.
It was quick.
there's some subtle differences between each of the implementations, in… foreign country.
having looked at the contrary one, I would prefer, Bringing that one over, and changing the things.
here to also match what Contrip does. Not sure if anybody has any references.
**Trent Mick** 39:11 You spent more time in the contrib one, I think, right?
**Marc Pichler (Dynatrace)** 39:14 Yeah, I…
**Trent Mick** 39:15 Or one faster, and then… yeah, okay.
**Marc Pichler (Dynatrace)** 39:17 Contrib had a few more packages that did things slightly differently, so I wanted to make more of a general utility. It's a bit stricter, in a sense. I haven't looked into exactly how much stricter it is.
But, yeah, it would slightly change the query string, that we see on… instrumentation, HTTP fetch, and, etc.
**Trent Mick** 39:49 Okay, and what do you think about putting it on instrumentation?
**Marc Pichler (Dynatrace)** 39:53 I think instrumentation is a good place for it, if… we end up with a lot of HTTP, instrumentation utilities in the instrumentation package. We can consider moving these out of instrumentation into their own separate package in the future, but I think for now, just having the functions there is… Good enough to deduplicate a bunch of the code that we see everywhere.
No.
So, instrumentation sounds good to me.
**Jamie Danielson** 40:34 So then, how did you want to handle… so you like the implementation of JSContrib better than, like, what's in here, so how did you want to handle this?
PR, like, merge it as is, and then make changes? Not as is, I mean, like, review and everything, but… would you want to change this particular PR to have that implementation, or…
**Marc Pichler (Dynatrace)** 40:58 I haven't really thought about it yet, would probably be fine to just merge this and then change it later.
**Jamie Danielson** 41:10 So the primary purpose of this one is, like, the deduping and using one shared one, and then a follow-up PR just to… Clean up the implementation.
**Marc Pichler (Dynatrace)** 41:22 Yep.
I think so.
**Trent Mick** 41:27 Had you looked at the sanitized URL that exists in the browser repo?
As well, when you're building one.
**Marc Pichler (Dynatrace)** 41:35 I have not looked into that one.
Oh.
**Trent Mick** 41:40 They also, I think for historical reasons, redact a whole bunch of other Query param, field names.
which I don't really want to get into it. I imagine there's a performance hit doing all that, but…
**Jamie Danielson** 41:52 There's sanitize URL function.
**Marc Pichler (Dynatrace)** 42:00 Probably that one, though.
**Trent Mick** 42:03 Yep.
If you scroll up again, that list that's just at the top there? Yeah, so it has all those other ones, and then they added… the last 5 are the ones that come… The lesson from the spec.
**Marc Pichler (Dynatrace)** 42:23 Interesting.
I think, A few of the… I think the user interaction one at least has all of these as well.
**Trent Mick** 42:41 Right, okay, so the history one.
**Marc Pichler (Dynatrace)** 42:42 Thanks, sister.
**Trent Mick** 42:42 and Contrib or Core, and then Browser started their own thing, and they started with Baseline 101, so yeah.
**Marc Pichler (Dynatrace)** 42:49 Yeah, if I recall correctly, one of the instrumentations in Contrip had already a pre-existing set of Things that would get redacted if you… Specifically opted into them.
getting rejected.
And it looks very similar to… What already existed there.
It might make sense to also start, redacting these.
I don't recall exactly, how strict the spec is on this.
I think it says something along the lines of, like, if you know that like… These are… Sensitive ones, you should reject them.
So maybe we go a bit stricter as well, and just add all of these.
**Trent Mick** 43:55 There's a potential birth concern, isn't there?
And…
**Marc Pichler (Dynatrace)** 43:59 There he is, yeah.
**Trent Mick** 44:08 Why can I not find it?
Where is this in the spec?
Let's run the spec repo.
**Marc Pichler (Dynatrace)** 44:18 It's on the semantic conventions repo.
**Trent Mick** 44:22 Okay.
**Marc Pichler (Dynatrace)** 44:31 Maybe it's somewhere in Ogot.
Not terrible.
**Trent Mick** 44:40 And it says query strings for the following should be redacted by default and replaced by the value redacted.
The list is subject to change over time.
And then, okay, so there's… there's a connection with… Actually, here's potentially a concern. There's, It says, in development part of the SEMCOM stuff is that down below, instrumentations may provide a way to override this list, the next one.
And this development tag down there.
by declarative config, so there's this declarative config thing that we'd want. So, almost makes it like you want the SDK to pass in Or to make available somehow? Or no, the instrumentations would have to do this themselves. So, like, an instrumentation being created would want to check Via the new mechanism that we have of the config provider.
They would want to create.
a sanitizer function from this configurable list of things to exclude, so now you kind of want… The instrumentation functionality to be build me a sanitizer function from this config.
Options, so that might impact what… The shared functionality they provide.
Okay, anyway.
**Marc Pichler (Dynatrace)** 46:15 I guess would be also utility in instrumentation, then? At least the type of the reduction function.
Or maybe what we, have as an option in the instrumentation. This is just a list of things to get redacted so that each, Instrumentation can kind of choose how… I don't know.
Anyway, we'll figure it out once we get there.
**Trent Mick** 47:00 So if we cared to, so what I would do is get instrumentations to support using that value in declarative config, and if you wanted to make that big knob available to people using code to set up instrumentations. And you could also add a config option To the… each instrumentation, that's basically the similar name, just… Different.
snake case versus Pascal case version of that same Name to config options, and then that's fine.
Hold on.
But I guess I wouldn't bother with the latter, unless people say, hey, I want to do it for the subway as well, just, like… I don't know, whatever.
I've decided what I think about declarative config yet.
Spent a year of my life, but… I'm not sure I want to write YAML files for the bike.
What have I become?
Someone's supporting YAML.
You hurt YAML. So I worked with the guy that created YAML. I was… we went… while he was creating YAML, Brian Ingersen, who changed his name to Ingi.net, interesting character, while I was there. I have friends that… that joke that I… I missed my chance to kill YAML way back when. I just could have stuffed Brian in a box, and that would have been the end of it.
And we could all just be doing… Jason with comments would be fine.
**Jamie Danielson** 48:32 For legal reasons, this is a joke. This meeting is being recorded. This is a joke, yes.
**Trent Mick** 48:38 I actually… I ran into Brian at, the only KubeCon that I've been to, and we chatted for a little while, so… no, I think we're good.
Yes, I'm kidding.
**Jamie Danielson** 48:47 I do like YAML, though.
I mean… Yeah, no, I said what I said.
**Trent Mick** 48:53 It's okay, it's okay, you don't have to, it's not…
**Jamie Danielson** 48:54 Do not apologize.
**Trent Mick** 48:55 You don't That's fine.
I don't think a lesson, yeah.
**Jamie Danielson** 49:03 But as a question, so when you were saying, not sure about the latter, were you referring to adding programmatic options for it?
**Trent Mick** 49:10 Yeah, I wouldn't… just because I'm not gonna… Basically, I'm arguing against what's the word? Proactively adding a whole bunch of options to our instrumentations, because… I think, far and away, the common usage is just list the instrumentations you want, you get the default config, and the mechanism now to configure things is declarative config if you want to tweak them, but most people just don't need to tweak these things, so… add them.
Lazily.
**Jamie Danielson** 49:41 Makes sense. I agree.
**Trent Mick** 49:43 I don't know, just to limit. I guess, kind of, the mostly limiting factor is maintenance time.
**Marc Pichler (Dynatrace)** 49:56 Does anybody have any more topics you would like to discuss?
**Trent Mick** 50:02 you'd… not… you're doing all the work here, so I feel bad, but you'd mentioned moving the… Focus topics thing to a file.
**Marc Pichler (Dynatrace)** 50:13 Yeah, I see…
**Trent Mick** 50:15 Not that we need to pick our focus topics right now, or… We're owed some.
some fluid time on that thing, but, yeah.
**Marc Pichler (Dynatrace)** 50:24 Okay.
**Trent Mick** 50:25 I'm curious if you're hoping to do exporter work at some point.
**Marc Pichler (Dynatrace)** 50:28 Yeah, I… I'm hoping we could define the focus topics as declarative config and exporters. But… Let's see, I am looking to get… the… PRs out for moving the focus topics to the docs.
order, and then, actually the few different proposals on the focus topics in separate PRs.
By the end of next week. So, we can get started picking those.
Done.
**Trent Mick** 51:09 On that, a thought that comes to me, and I know it's… I should have written down an agenda item for it, but, declarative config, I expect to, like, largely be there quite soon.
Then there are a number of issues that have been opened for little parts that we haven't done, so… Here and there, but generally we have to-dos and issues open for all those, so Find the Long Tail can deal with those ones.
On the other side, I think instrumentation probably needs to be dealt with fairly soon. A thing that I think pushes that is Node 27.
Which is now, if people aren't aware, the odd numbers are not gonna be… the odd numbers will be LTS versions now, so… 27 will be an LTS version, as opposed to, like, we used to just skip and not care about the odd versions. Node 27 is dropping… dash dash loader and dash dash experimental loaders, and is dropping module.register.
in favor of module.registerHook, which is a synchronous version. Module.register was a thing that When the loaders changed to doing a background thread for doing loading, which caused all kind of… kind of pain in the back end.
So what that will mean is that we're… like, we already know we're well behind on the advice provided for people for doing ESM instrumentation support.
I think we probably should be looking at tackling that this year. So, I think maybe that should be a focus topic as well.
And that we get to a point where the advice is use module.register hooks.
And that's the only way to do it, and not using dash dash experimental order.
So… Anyway. And maybe that's all it is, so maybe that's quick, and this doesn't mean redoing the whole instrumentation interface for dealing with other issues, but it's just that part, at least.
**Marc Pichler (Dynatrace)** 53:08 haven't looked into that whole thing for quite some time. There's… Lots of movement in that, in that part of Node.js, it seems.
**Trent Mick** 53:19 Yeah, there are other parts, so, like, the latest version of Express now, so the work that… I can't remember his name.
Abdel, or someone from Datadog has been working with a lot of the modules to switch to using tracing channel, diagnostic channels internally, so LaceVersion Express supports that, so… Eventually, we're gonna wanna… I think… I'm not sure what the migration path is. I think we would want, eventually, Instrumentation Express or Instrumentation Browder, because it's actually a router that does this, too.
Maybe… Detect when it's express.
version whatever that supports that stuff, and when it is, it doesn't actually install… doesn't actually monkey patch anything, it just says… Subscribe to diagnostic channels so that it's a little bit less invasive, but they still do require setting up hooks until we can get a user to say.
I'm good, I'm only using versions of things that support Dyson S3 channels, and then at that point, ideally.
No require in the middle or import in the middle hook is registered, but that's… that's down the road, so, yeah.
**Marc Pichler (Dynatrace)** 54:23 Yeah, I wanted to actually move the, utility that I had in my initial contacts attached, proposal to a package in… Or our country.
might be looking into that as well, in the… Next few weeks.
Hmm.
So maybe we can…
**Trent Mick** 54:47 And that's something that…
**Marc Pichler (Dynatrace)** 54:48 started on Deadpool.
**Trent Mick** 54:49 Stations would want to use, right?
**Marc Pichler (Dynatrace)** 54:51 Yeah, it would be…
**Trent Mick** 54:53 weird.
**Marc Pichler (Dynatrace)** 54:54 It could be in… instrumentation package, or… Like, the reason why I wanted to actually move it to a different package was that, If it's just a utility to actually instrument things.
then the public API would be fairly small, and if we know that it works, we could also stabilize it fairly quickly.
Whereas with instrumentation, we're kind of in a state where we don't know yet when we're gonna stabilize it, and if we start with a new package, that's just a whole lot easier.
**Trent Mick** 55:31 Fair.
We could have, instrumentation, the good parts.
This is the one that's actually…
**Jamie Danielson** 55:40 I was about to say, like, instrumentation-new, like, I want that one.
**Trent Mick** 55:45 Dash new final two last versions, yeah.
**Jamie Danielson** 55:49 Backup.
**Marc Pichler (Dynatrace)** 55:53 instrument, hurrah, hurrah.
**Jamie Danielson** 55:56 We did it.
**Trent Mick** 55:58 Good luck.
Yeah.
Okay.
**Marc Pichler (Dynatrace)** 56:06 Right.
I guess…
**Trent Mick** 56:13 To triage or not treat…
**Jamie Danielson** 56:15 we have…
**Trent Mick** 56:15 Yeah, it seems I know right at the front.
**Jamie Danielson** 56:17 We could take a little break before the next meeting.
**Trent Mick** 56:22 There are so many…
**Marc Pichler (Dynatrace)** 56:23 I agree.
**Trent Mick** 56:23 and PRs coming in these days, I feel bad.
**Marc Pichler (Dynatrace)** 56:25 Yeah.
I look into this after the meeting, that you have to break.
We can…
**Jamie Danielson** 56:31 We can look at it right now.
**Marc Pichler (Dynatrace)** 56:33 Oh, it's fine. This one is probably P2, and this one is… has been around for a long time. I think this is a duplicate of an issue that AMIA opened.
**Trent Mick** 56:47 But aborted handling, yeah.
**Marc Pichler (Dynatrace)** 56:49 Yeah, can you…
**Trent Mick** 56:50 I would like poker.
**Marc Pichler (Dynatrace)** 56:50 I'll go.
**Trent Mick** 56:51 Go poke Dan so he can just redo instrumentation HTTP based on the internal… I mean, there is potentially a template now. We could… copy instrumentation HTTP that, Brian English has written for Node Core.
Because it's built entirely on the diagnostic channels that NodeCore emits.
And I think that works back to the versions that we support, I'm not sure, because he only needs… they only need to worry about the latest node version, but… Duh.
Anyway, because instrumentation in HCP is often not a lot of fun to get into and try to work on.
**Jamie Danielson** 57:26 Pretty gnarly.
It's just big. There's just a lot in there.
And it's, like, one of the most critical instrumentations that exists.
**Trent Mick** 57:34 Add that to, right?
**Marc Pichler (Dynatrace)** 57:35 Yeah, that's why I don't like to touch it.
Because you're really screwing people.
**Trent Mick** 57:41 If you screw it up, yeah.
**Marc Pichler (Dynatrace)** 57:42 It breaks spectacularly, so… Alright.
Okay.
Yes, we…
**Jamie Danielson** 57:52 Do we have a meeting next week?
So, next week, Wednesday, is the day before U.S. Thanksgiving, so I don't know if that means a lot of people are out.
I might be out, I'm not sure, depends on how my family is that day, and if I want to get on a call.
But I don't know if there was plans one way or the other.
**Trent Mick** 58:16 the longest continuous stat holiday in the… or contiguous stat holiday in the U.S, right, of the year.
Two days off, and you want a third. You're greedy!
**Jamie Danielson** 58:27 We don't get many days off in the U.S.
**Trent Mick** 58:29 Yeah, I know, I know, I know.
**Jamie Danielson** 58:30 Let me have this one.
**Trent Mick** 58:34 There's David over in Spain leaning back. It's like, oh yeah, maybe, we get all of them.
For every religious thing.
I'll be around, but… Amazing.
**Marc Pichler (Dynatrace)** 58:48 Yeah, maybe we'll just cut the meeting short if there's, not many people here. Usually, we don't have a lot to talk about then, as well.
So…
**Jamie Danielson** 59:01 I'll keep it on my calendar.
We'll see. I'll let you know.
**Marc Pichler (Dynatrace)** 59:06 You don't have to join.
**Jamie Danielson** 59:08 No, I don't, but I might want to, so… Okay.
**Trent Mick** 59:15 Should we do a release that day, right before Black Friday?
**Jamie Danielson** 59:17 Oh, what a great idea!
**Trent Mick** 59:18 Let's see if someone's actually uptaking, yeah.
Screw instrumentation HD.
**Jamie Danielson** 59:23 It's the patch release.
**Marc Pichler (Dynatrace)** 59:28 Red.
**Jamie Danielson** 59:29 Bye.
**Marc Pichler (Dynatrace)** 59:30 Then, have a nice week, and maybe see you next week, or if I don't see you, happy, Early days there.
**Jamie Danielson** 59:38 Thank you.
**Jackson Weber** 59:41 Yep. Have a good one, y'all. Bye.
