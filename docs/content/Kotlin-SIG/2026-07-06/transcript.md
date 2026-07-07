SIG: Kotlin SIG
Date: 2026-07-06
Duration: 20 minutes
============================================================

## Zoom Recording Transcript

**Jason Plumb** 04:37 Might be a small turnout today. Let's give it a few more minutes.
**Hanson Ho** 04:49 Hello?
Oh, how's it going?
**Jason Plumb** 04:58 Going all right. Ever farther behind every day.
**Hanson Ho** 05:02 Hahaha.
Yep. Yep, yep, yep.
**Jason Plumb** 05:07 We have a non-existent agenda today.
**Hanson Ho** 05:13 Yep.
**Jason Plumb** 05:13 But maybe some stuff will come up.
**Hanson Ho** 05:16 Yeah, there's some stuff from last week.
That we can probably discuss, a bit.
Where's my thing?
Jamie's coming back tomorrow, so… hallelujah…
**Jason Plumb** 05:35 Yeah, cool. That's great.
**Hanson Ho** 05:39 Yeah. And I started, I think. Where did I start?
A list of, yeah, I haven't done my… Yeah, I'll get that to. So, Yeah. This part.
**Jason Plumb** 06:01 Right, yeah.
**Hanson Ho** 06:03 Yes.
Cool. I think we talked about what we wanted, might have started an issue, I don't know if I did, But I was going to send them the list of the APIs that we want reviewed, basically.
**Jason Plumb** 06:20 Okay.
**Hanson Ho** 06:22 And basically, the trade-offs between Kotlin and OKIDMs, or OTel IDMs following patterns that were no longer recommended, especially for APIs.
iOS and JavaScript. Basically a sanity check and like an idiomaticness check.
But, specific files.
So I will get to that. Well, I'll get to that this week.
Okay.
**Jason Plumb** 06:51 Cool.
We have a lot of open PRs, and we need reviews on that.
**Hanson Ho** 07:01 Instead of, yeah.
**Jason Plumb** 07:02 I know. How many new issues? It looks like not really a ton of new issues, at least new to me.
Tvos being a target is interesting, and then… Min requirements, yeah, that's important. But the other thing I'm thinking about is that we haven't done release… So, we should probably just cut one, especially because I literally, just as this meeting was starting, I merged the… PR that makes attributes stable, even though the API module is not stable, but it, you know, it has the… It removes the, it's this right here, removes the experimental API. So I think we should probably cut a release. I could probably do that.
**Hanson Ho** 07:42 Sounds good.
**Jason Plumb** 07:44 Okay.
Just to kind of keep that momentum going.
I think the Android patch release was unblocked too, so that's also on my plate.
**Hanson Ho** 07:58 Oh, I thought you did already.
**Jason Plumb** 08:00 No, there was a PR… in Android, there was a PR… To implement the thing for the patch that we wanted, and it just sat out there unreviewed.
**Hanson Ho** 08:10 Oh.
**Jason Plumb** 08:11 So, it sounds like Cesar has merged it, so I can probably do that now.
**Hanson Ho** 08:15 Okay.
**Jason Plumb** 08:16 Okay.
Anyway, is there anything exciting in here? So, how are the patch versions looking?
I think one of these was.
This one's good. Okay, that's great.
I always get twitchy like when little patch versions break the build, and I've seen that a lot in other projects, so that's cool. This is an easy one to just get rid of.
**Hanson Ho** 08:44 I think, Fran, who's not here right now, was talking about last week, getting a PR for, minimum version verification for JS and iOS, which we don't have for Android.
**Jason Plumb** 08:59 Yeah.
**Hanson Ho** 09:00 This would be nice, because… But what I worry about is, you know, patching some JavaScript thing that I don't really know pumping minimum version, because, oh yeah, it seems innocuous, but it's not. So…
**Jason Plumb** 09:15 And you opened an issue, I think, for that, I saw.
**Hanson Ho** 09:18 Yep.
**Jason Plumb** 09:20 Interesting. Yeah.
Like, this is still related, right?
**Hanson Ho** 09:27 Yes, oh.
Efrain.
Okay.
Cool.
**Jason Plumb** 09:41 Yeah, and I don't think this person has submitted any pull requests yet.
I don't remember having seen it, but I'm also behind.
There's some good stuff in here.
**Hanson Ho** 09:55 Yeah, I need to go through all the issues.
It's been a few weeks.
**Jason Plumb** 09:59 Yes.
This thing, tell me what you think of this. So… Over in this PR… Yeah, okay, so this patch versions thing was big, and the build was breaking, and I had to, like, fiddle around with it to get it to pass.
And what it was is that I had to regenerate the yarn lock file, so I guess Renovate, by default, doesn't do that.
So what that means is there's then a mismatch between what's in the dependency declaration and what's in the yarn.
**Hanson Ho** 10:33 Mmm.
**Jason Plumb** 10:33 That makes sense.
So, like this, you know, we'll change a bunch of… Properties in here, and bump up versions and stuff.
But then it didn't come through and like increment this one, for example.
**Hanson Ho** 10:48 Oh, I see.
**Jason Plumb** 10:49 Like, somewhere, like, WS got bombed, right? So if we scroll down here, probably WS, hopefully is in here.
Or maybe it was a previous pull request.
**Hanson Ho** 11:01 WS, what's WS?
**Jason Plumb** 11:03 WebSocket, probably.
**Hanson Ho** 11:05 Oh, okay.
**Jason Plumb** 11:07 I mean, JavaScript picks the most terse names of all time.
But I, yeah, it looks like this was already a two one. It just hadn't. Anyway, this broke the build 'cause these were outta.
**Hanson Ho** 11:17 Okay.
Yes.
**Jason Plumb** 11:18 So the proposal here is to add a helper action so that you can type this into a pull request, and if the yarn lock is broken, then it will regenerate that yarn lock and push it to that PR branch.
The idea being to do that mostly for Renovate PRs, because I think Renovate doesn't handle it And, you know, it's a little more complicated, and this person, always very helpful, was like, we could just automate the full thing, and then you would have to type it. And I'm like… Yeah, maybe we baby step into it, though, you know.
Whatever… I didn't realize there was some feedback on this, because… We had a long weekend.
But base, yeah, the basic. It's a new workflow, and it's triggered by a command, right? It's triggered by this thing.
**Hanson Ho** 12:10 Mmhm.
**Jason Plumb** 12:12 And it's limited… To only maintainers and approvers being able to run it.
And yeah, so give that some consideration.
The idea was, I don't want those patch release PRs to, like.
Just be stuck, you know, and then.
**Hanson Ho** 12:28 Yeah.
**Jason Plumb** 12:28 For maintainers to have to, like, check out the remote branch, regenerate the yarn lock… well, first of all, determine that it's the yarn lock that's failing Check out the branch.
Do you rebuild the thing and then push it up is like kind of a lot of back and forth. And the idea was to be able to have a workflow that can just sort of like make it easier.
But, anyway… That's what I submitted. I don't think I have anything else in here.
Anyway, yeah, there's a lot of, a lot of reviewing that needs to happen.
Yeah, some of this stuff is old, and we just can't merge it yet.
**Hanson Ho** 13:12 Yep.
What do we do with, with that? It's like, oh yeah, you know, we can't do it yet, but we can do it when something else, like the, like, you know, CodeQL updates to Kotlin 2.4. Do we close this and have it bump back up? Or, or…
**Jason Plumb** 13:31 We…
**Hanson Ho** 13:31 Do we just leave it like this?
**Jason Plumb** 13:33 I think the move is to close it.
**Hanson Ho** 13:35 Okay.
**Jason Plumb** 13:37 I would like to close it, and then if we feel like we might forget about it, then… That's weird.
I guess when I merged that patch release, it sort of re… It probably rebased this PR. So why is it building?
And then if we're worried about forgetting it or renovate not coming up again, we can open an issue.
**Hanson Ho** 13:59 No, it's okay, we'll be, well, doesn't really matter, but… Whatever is easiest, to be honest, because 2.41.
We'll, we'll know, we'll, we'll come out eventually. They'll, they'll be a kick, so So if you just close this one.
**Jason Plumb** 14:19 I think the reason why we were not ready to merge this was because… I mean, I know 2.4 breaks CodeQL, but that probably wasn't the motivator here in Kotlin repo. It was probably something else, right? Like, it bumps a minimum version.
**Hanson Ho** 14:32 It shouldn't, because we're compiling down to, 2.0, for the language and the target, or the language and the standard lib. So, there, there shouldn't be any, there shouldn't be any issues.
Because we're just changing compile.
I think I did verify that we are, we are, locking that down.
**Jason Plumb** 14:54 So you think it was CodeQL.
**Hanson Ho** 14:56 It's entirely CoQL. Yeah, I verified it for this repo.
I verified for one of the repos. I'm pretty sure it's this one.
I linked to an issue, I think, as well, but that might just be on Slack.
**Jason Plumb** 15:14 And CodeQL has a fix in place, I think they just haven't released yet.
**Hanson Ho** 15:18 Yes.
So the next minor version of CoQL should have… well, patch version, even.
**Jason Plumb** 15:24 There is a lot in this release. Oh my God.
**Hanson Ho** 15:26 Oh yeah, 2.4 is beefy. This is their yearly minor tick up, so.
And again, this is this is mostly, well, I mean, some of this will affect how compile works, but, we're not using the features, language features or standard lib of 2.4 anyway, so we're we're we're should be safe.
**Jason Plumb** 15:48 So the whole thing is about CodeQL. So we should just sit on this until CodeQL is ready.
**Hanson Ho** 15:53 Basically, yeah. I think that's what I commented, on one of the… one of the ones that says Kotlin 2.4, maybe this one.
**Jason Plumb** 16:01 It was probably the Android one.
Okay, I'm happy to just let it sit out there, too. But, I mean, I expect us to see CodeQL within a couple of weeks.
**Hanson Ho** 16:14 Yep.
They… everyone's updated, like… Well, I checked last week, it was updated a few days ago, so it could even be this week. Hell, it could be now, like, for all I know, they could have released.
**Jason Plumb** 16:29 Well, hopefully we'd see a run of APR.
**Hanson Ho** 16:31 That's true.
**Jason Plumb** 16:34 Like, okay, so we don't have, we don't have a really big agenda, so I'm just gonna go through some of these while we're here.
**Hanson Ho** 16:41 Sounds good.
**Jason Plumb** 16:43 on a merge.
And maybe I will do the thing I've been putting off.
For a month at least, which is to use Env… Environment?
Configs, what's it called? Environment secrets.
**Hanson Ho** 17:04 Oh.
**Jason Plumb** 17:04 For… for this, and then use this release this week as, like, a guinea pig.
to see how far it can get, and if that breaks anything. Oh, no!
I think I can't. I think it's using Jamie's Sonaty.
**Hanson Ho** 17:17 Ha ha.
**Jason Plumb** 17:18 I think you have to put them into each… you do… so you have to put them into each environment that you create.
So I think I created the environment. Okay, let me just finish this. Sorry, scatterbrained.
I think I created the environment, and then I think I got stuck on… Yeah, I created it. And then there's secrets.
in here, but then I think I didn't continue because it is Jamie's publishing… Token versus sonotype, so…
**Hanson Ho** 17:57 Didn't… didn't for Android, didn't we have one that's… that's… that the maintainers have access to, so you and Cesar has… have… and I guess now Jamie.
**Jason Plumb** 18:05 It's just mine.
**Hanson Ho** 18:06 It's just yours? Okay.
**Jason Plumb** 18:09 Yeah, we.
**Hanson Ho** 18:10 Is this for all of these projects? Isn't there some sort of…
**Jason Plumb** 18:14 Yes, it's tied to a person. There's no… like, Sonotype doesn't have, like org tokens or anything? There's no, like, way within Sonotype to share a token between people, other than one person creates it and they can share it?
**Hanson Ho** 18:28 So…
**Jason Plumb** 18:29 The thing right now is if I get hit by a cement mixer tomorrow while I'm riding my bicycle, the way that we account for that is just someone else has to generate the publishing token that has the appropriate role.
Just replace it with theirs.
Like, Cesar can do that.
**Hanson Ho** 18:46 Yeah. Yeah, as long as you can replace the secret, then you just need the value.
**Jason Plumb** 18:49 Yeah.
**Hanson Ho** 18:49 So, yeah.
**Jason Plumb** 18:51 Yeah, and I haven't switched Android over yet to Environment Secrets either, but I think I have it set up to use them, we just have to Maybe I won't do it this time for Kotlin, because it requires changing all of the GitHub actions.
**Hanson Ho** 19:06 Oh.
**Jason Plumb** 19:08 Like, they're required to say what environment they target when they build, and so it's a bigger step.
So maybe I'll do it for Android, and I won't do it for Colin this time. I'll wait.
**Hanson Ho** 19:19 Okay.
**Jason Plumb** 19:25 Okay, well, Maybe we'll just call it at that, say a light meeting.
**Hanson Ho** 19:31 Mmhm.
You know, take out my action items so that they're ready for next week.
**Jason Plumb** 19:41 Cool.
**Hanson Ho** 19:42 But yeah, if there's any other Things that we want to ask, The JetBrain folks, now is the time. Although, you know, we can always come back with more.
**Jason Plumb** 19:54 I do feel bad because, like, they're willing to help out, and I'm just like, I haven't had any time to look through and give, like, topical areas even. It seems like you've got a good start, which I appreciate.
**Hanson Ho** 20:05 Yeah, so I have to actually write that quick doc or something. There's a quick issue.
**Jason Plumb** 20:11 Cool.
Alright, well, I don't think we have to drag it out for the whole 45.
**Hanson Ho** 20:16 Swe.
**Jason Plumb** 20:17 No, we all have other stuff we could be doing.
**Hanson Ho** 20:19 Yeah, like, catching up. I think I got some slacks. Yeah.
2 or 4. All right.
**Jason Plumb** 20:25 Yep. All right.
Take care.
**Hanson Ho** 20:28 See you tomorrow.
