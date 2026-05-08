SIG: Python SIG
Date: 2026-05-07
Duration: 57 minutes
============================================================

## Zoom Recording Transcript

**Surya Teja** 00:50 Hey, hi folks, how is your day going so far?
**Riccardo Magliocchetti** 00:55 Hello?
**davidperez** 00:56 Hi.
I'm doing well.
**Surya Teja** 01:01 Great, great.
**Riccardo Magliocchetti** 02:31 So, welcome, everyone, to this week.
Python SQL. We're waiting a few more minutes for more people to join.
In the meantime, please add yourself as an attendee to the… call notes. If you don't have the link attend, I'm sharing it in the chat.
And also, if you have any topic you want to discuss, feel free to add them as well.
Okay, it's a 5, think we can start?
Welcome again.
I see we are 12 people in the call, but only 5 in the attendees, so please add yourself, you can.
Okay, let's start with the triage.
Okay, we still have a lot of… stuff in the, you know, status column, this morning, for me, like, your afternoon, for most of you. I've looked at merging some dependable PRs, mostly the one in Contrib for the Docker test.
Since these are the… That doesn't need to change the OB log file, so… Can be merged?
Let's see if you're on your staff… From last week.
This one is new.
This one for containers, you know, this is from the panda, but… Dependable, dependable, dependable… Comprebra.
Please, I want to discuss it later.
So I'm talking… Yeah.
Hi, this is a little blasting… Okay.
Okay, I think I have seen this when trying to run the… the tip checker on the OSI SDK.
But, yeah.
Yeah, I can take a look later.
We have a swan from the whiskey.
Instrumentation… Okay.
Okay, okay, so, yeah, SyncViz.
Has been reported for the other, instrumentation as well.
Like, we are assuming in some instrumentation that the URL that we receive is well-formed.
And I think I've had a discussion, like, we have an open issue, like, and there is, I mean, this… this one.
Yeah.
Where, like, if you fast the, your application, and you have the WISC instrumentation.
it may crash in the WISC instrumentation.
So, not great. I can take a look.
Maybe.
Okay, this is documentation, but how CLI sign, so we're gonna skip.
I got?
Non, c'est les sign.
Okay, this is… DBAPI. So maybe, maybe we should wait for Tammy to be back?
**Lukas** 08:28 This one… I think it's just blocked on… the semantic conventions. Like, this PR wants to add commit and rollback spans, but there's no mention of that in the spec, so I told them to raise an issue in there.
**Riccardo Magliocchetti** 08:45 Okay, thank you.
**Liudmila Molkova** 08:46 Oh, sorry, I was going to comment on this and didn't, I will do it right now. I think these are… those are the operation names.
They don't need to be present.
And it kinda makes sense to use these operation names.
So anyway… Sorry?
**Lukas** 09:08 Sorry, I was just gonna ask, I thought that even, like, I mean, even span names… need to be, like, mentioned in the spec, right? Because… I mean… Like, they could change, right?
**Liudmila Molkova** 09:23 The format, yes, but the format in this case would be… the coming to a rollback, like, maybe database name, There could be caveats, but the value of the attribute is not necessarily part of the semantic conventions. The name of the attribute is, and the shape of the spread.
And for these two guys, it kinda makes sense, this proposal makes total sense, with some potential caveats. I… I don't think there is a… problem from semantic conventions, but it's still a good idea to create an issue so that it's documented in some shape, that it's done this way in this instrumentation, and maybe we will just clarify in semantic conventions that that's the approach to take.
**Riccardo Magliocchetti** 10:21 Thanks.
**Liudmila Molkova** 10:23 Yeah, thank you.
**Riccardo Magliocchetti** 10:24 And the show is that.
Okay, let me add it to the… Okay, maybe, maybe a bit later. Okay, so… We've done our 5-minute stage for today.
Thanks, Lucas, for adding a note on the… what you're working on.
So, I have a bunch of topic, easy ones.
The first one… Okay, it's this one? I think I added a regression, somehow.
Because, like, I've… OpenAPR, to stop, testing the… the weaver, helper.
inside the test duties package when, under PyPi.
Because, I think we don't have wheels for the GIJPC package.
for a dependency of gRPC, and so it would take, like, 50 minutes, and sometimes it would just raise, Some timeouts, or stuff like that.
And so, I created this one to skip it also on the free trading build for the very same reason, because you don't have gRPC builds.
And so this is working fine. The issue with that is that, I see we have a failure.
Awesome… dependable.
jobs.
And for some reason, It's not able to parse the test requirements anymore.
since, like, PIIP and UV are fine with the test requirements, I guess it's the issues on the PandaBot, but still… Like, if it's blocking the Panamo to work, maybe also our issue.
And so, I have no idea on how to fix that. I tried to… Like, from a suggestion from any media to… To split the… The constraint from the dependencies?
So, that may be, like, dependable to not… Save this one.
But unfortunately, like, this syntax does not work for constraints.
And so I cannot do that.
**Liudmila Molkova** 13:10 Oh, I stumbled upon it as well, I think, when we, first edited, that it's either minus C or the platform, but not together.
**Riccardo Magliocchetti** 13:21 Yeah.
Yeah, but, like, in this case, the problem is… isn't… I think it's… but on constraints, I have… To put, aversion here, like, as far as I understand.
I don't know if… We have the…
**Emídio** 13:45 Hikaru, I have a question. What is the reason we are skipping on Windows, and… And then PiPy, I'm… I'm used to that.
**Riccardo Magliocchetti** 13:57 Because on PyPi, it's flaky, and it takes ages to build the gRPC package.
And the windows… What was it? Leon Miller?
**Liudmila Molkova** 14:11 It's the same… well, it's… the gRPCIO is not available, it needs to be built, and there is a lot of, setup and work that needs to happen, but testing on Windows doesn't add any coverage to the Weaver life check that we are doing.
**Emídio** 14:34 Right.
I can take a look on this one, Ricardo, to see if, If using the pip compile with the universal resolver, if they can.
Provider.
some, requirements.txt files you can use.
**Riccardo Magliocchetti** 15:00 Okay… Okay, yep, thanks.
But otherwise, like, we can wait. I think that this… Job runs every week.
So maybe it was just… One-time error, I don't know.
But, yeah.
Like, we don't have many hints on what Dependable does not like about the file.
Everybody is fatal, but… So, like, it doesn't even pinpoint the exact requirement files, just, like.
It failed for the dependencies.
But, I think, like, my change was the only one in the… In the time frame between the last run of the… of this job, so… That's it.
Like, it's… I don't think we don't have any… Ari in fixing that, but… Hopefully, like… like, not hopefully, right? We need to take our eyes on it anyway.
Thank you for letting me out now.
**Aaron Abbott** 16:15 Real quick, I think we discussed it last week briefly, or the week before, but, Does Renovate handle this a little bit better?
**Emídio** 16:27 I think so. I saw, like, some other SIGs, they were using Innovate.
I think I have, open issue, and our HEPO to configure that, but I didn't have time to move forward with it.
But because I remember it was requiring a lot of updates.
**Aaron Abbott** 16:48 Yep.
**Emídio** 16:48 And it, it may need to sync, like, to a… Sync, on what we need to do on the first updates, which package we need to update first.
But, no.
**Aaron Abbott** 17:02 Okay, yeah, I mean, I'm… I think I'd be open to moving to Renovate. I find it a little bit easier to configure and less noisy.
So, if it also supports, like, the, you know.
weird mix of log files we have, better. That would be good, in my opinion.
**Emídio** 17:18 Yeah, I think I have a branch with a working configuration I can share it on Slack.
**Aaron Abbott** 17:24 Yeah, that'd be great. Thank you.
**Riccardo Magliocchetti** 17:30 Thanks. Also, like, also, like, the pandemic, but I don't think it handles where the… bumps in the UV locks. Like, I remember a lot of… bumping PR spot phase for… because, like, he forgot to add on now the… Other dependencies.
Anyway, next topic, also… from UA Media, I was wondering if… we're going, since, like, a mediopen APR that is, adding some UP rules for the rough lint.
And in some instances… We are changing, like, like here.
Some, type? Like, when importing the, the, the types we use.
from collection.abc instead of typing.
So, was wondering if this may be an issue for downstream users?
on changes on the API side, mostly.
**Aaron Abbott** 18:42 Sorry, are you saying we're not supposed to import from collections.ubc?
**Riccardo Magliocchetti** 18:48 No, like, since we are changing this, and… I was wondering if this may cause issues for… those streaming users.
Like, other movies.
typing to a collection and ABC.
**Emídio** 19:06 Do you mean only on type check, on type check, on time, or…
**Riccardo Magliocchetti** 19:10 Yeah, I expect to be the same, so yeah, Olean, we'll type checking.
**Aaron Abbott** 19:20 Yeah, I think it's supposed to be fine, like, they deprecated the versions in typing, right?
**Riccardo Magliocchetti** 19:25 clear.
**Emídio** 19:29 Yeah, if you are unsure, I can write a simple POC, and you can confirm.
**Riccardo Magliocchetti** 19:38 That would be great, thanks.
**Emídio** 19:40 Yeah.
**Riccardo Magliocchetti** 19:44 And thank you also for working on that.
**Emídio** 19:47 Probably.
**Leighton Chen** 19:49 Amidia, you want to put a comment on your PR, that we're waiting on that…
**Emídio** 19:54 Yeah, I left a comment saying that, with the results of the POC.
**Leighton Chen** 20:00 Nice.
**Emídio** 20:02 God, ridiculous.
**Riccardo Magliocchetti** 20:12 Okay, what's the last one for me?
This is a… silly ones? Like, when going through… Dependables PR.
I know, like, we have an issue where we can't upgrade some libraries.
And especially, especially the HTT ones.
Because we are using the Docker and Docker Compose packages from, From PIIP, and not the system ones.
And these packages haven't been updated in years.
So, we are stuck with… with this, valued version.
And so, yeah, since I had some free time, I played a bit with this, and… Should be… like, it's easy to move to the system provider Docker 1.
And this has the net benefit of removing quite a bit of dependencies.
From the Docker test?
And so… Wondering if you have any opinion, Arrow?
**Aaron Abbott** 21:21 Yeah, I mean, I think… I think this is good overall.
The only thing is maybe, like.
I think there was actually an issue open for this, where, because it runs sudo when you just, like, run talks.
which I kind of agree with, it's unfortunate, because if you're just trying to run the CI, It installs dependencies, so… I'd be okay to, like, we could add, like, a check here, and then print a warning.
Well, what do you think about, just, like.
Doing the dependency installation of these kind of external things inside of, the CI runner, the GitHub Action instead.
**Riccardo Magliocchetti** 22:02 Yeah, like, for this case, I added a test, so if you have Docker, it won't install anything.
But we still have the… the stall for the… Unix or DBC, microsoft ODBC driver.
**Aaron Abbott** 22:19 Yeah.
**Riccardo Magliocchetti** 22:20 Yeah, like, probably we could just… Check if the package is stored.
And avoid, the… ODBC test with the MySQL driver if it's not found. So, yeah.
Leave me in the comments.
**Aaron Abbott** 22:43 Trying to dig up… I think we have the same issue in Contrib.
**Riccardo Magliocchetti** 22:51 Hey, that piece is contributing.
**Aaron Abbott** 22:53 Okay, sorry.
Yeah, I just… I added it to the meeting notes, but… Yeah.
**Riccardo Magliocchetti** 23:01 Beto?
**Leighton Chen** 23:04 Will this require all contributors to have Docker installed?
**Riccardo Magliocchetti** 23:14 Well, I don't think anyone is running the Dockers test on their machine.
**Emídio** 23:21 Yeah, it doesn't work. Oh my.
**Riccardo Magliocchetti** 23:25 Usually, like, when I try this, I just comment this line.
**Leighton Chen** 23:30 Oh, I see.
**Emídio** 23:31 he…
**Riccardo Magliocchetti** 23:33 Yeah.
**Emídio** 23:33 Hikar, not sure if you have time, but do you think it's possible to… create a Docker image, like, with everything installed, and we just mount the docs.
talks directory with the dependencies inside the Docker container.
So, anyone care about that?
**Riccardo Magliocchetti** 23:59 Yeah, like… Yeah, we can't do that, but… I think that would be, like.
**Emídio** 24:08 Yeah, it'll be an extra effort, yeah.
**Riccardo Magliocchetti** 24:10 Thank you.
**Emídio** 24:11 So you… in case you ha- if you have time.
**Riccardo Magliocchetti** 24:15 Well, I'll just update this one to… to them… to stop using, sudo, and install the dependencies, so… On the CI side?
And so… Yeah.
Okay.
Move forward with this, thanks.
**Aaron Abbott** 24:38 Yeah.
I mean, if it… if it became a problem, we could do the, like, what the… Actually.
Nevermind. I don't think it'll be a problem. I think that's… that's probably okay.
**Riccardo Magliocchetti** 24:55 Yeah, like, also, like, this one, assume we are running a Debian-based distribution, and And select people on Windows or Mac OS.
can run these Docker's tests, so… I think it will be, like, net improvement, anyways.
And Windows people as well.
Okay, thank you.
Next topic is from Lucas.
Here's some questions?
**Lukas** 25:31 Yeah, this is, in response to your comment, Ricardo, if you scroll down… So you brought up that… We… so… I brought in an import from SDK that I, that I just added, the… just the utility function for parsing environment variables, and then you kind of brought up a good point, which is that if we remove it later, we would break, old versions of the exporter, right?
But… This is, like, also an issue, like, just in general. So, like, we currently import… like, some experimental environment variables from the SDK, so… essentially now, like, with our current… because the exporters have a loose requirement on the SDK versions, we basically can never actually remove that environment variable anymore without breaking old versions of the exporter.
So… I'd be potentially in favor of just pinning the SDK version for the exporters.
To kind of fix issues like these.
Yeah, I'm not sure, like, what other… People's thoughts are here.
**Riccardo Magliocchetti** 26:50 Yeah, I think we had this discussion, and I remember this because, I remember the discussion on other PR.
Or an issue, where someone reported that we were… we broke the… Like this, scenario.
In another PR, I don't remember which one.
And yeah, like… I… I also was in favor of just… Dropping this, You know, this promise, like, but… We are not maintaining, or looking at maintaining that.
Because, like, we don't test for that specific case.
And it will be, like, quite hard to test also all the… Exported version with newer SDKs.
But, yeah, maybe I can try to find a discussion?
**Liudmila Molkova** 27:52 Wait, this one, so we… Released.
internal SDK metrics, people potentially start using them.
And now we want to put them behind the feature flag, which makes total sense, except it breaks.
people.
**Riccardo Magliocchetti** 28:10 I understand the preference.
**Liudmila Molkova** 28:11 I'm right?
**Riccardo Magliocchetti** 28:12 No, no, like, it's not… the problem is just, like, implementation details.
From… from us, where, like, let me open the exported by project name.
Like, the exportable project does not depend on a specific SDK version.
I think it's common.
It's, small… like here, we don't depend on a specific SDK version.
But only on newer ones?
And so, like… If you update just to one package and not the other, Like, you can run, Older exporter with newer SDK.
And so, like, since we were importing an internal, symbol from the SDK. I worry is that we need to maintain that symbol forever, otherwise we are breaking this.
Scenario.
And in the past, we had, like, an issue reported of breaking this one.
I'm slow.
**Aaron Abbott** 29:48 What's, like, the concern of keeping the environment variable?
**Leighton Chen** 29:51 What's, like, the concern?
**Riccardo Magliocchetti** 30:00 Can you repeat, please? Because there was some…
**Aaron Abbott** 30:04 Yeah, yeah, that was me. I was gonna say, you mentioned, like, we have to keep the environment variable around forever.
**Lukas** 30:13 Yeah, I mentioned that, like… I think Ricardo's concern is that, at least, like, we added a… I… in the PR, I imported an internal function for just a utility function for, parsing Boolean environment variables.
By doing that, we basically can never remove it again without breaking the older versions of the exporter.
Because of that loose version requirement.
But the point I brought out now is that, like, I mean, that applies to everything else that we import from the SDK here. So, like, all those environment variables that we import, we can never, ever, like, change their names now. Essentially, they're… they're stable, I guess, like… So… Honestly, I'm… Like, my preference would just be to pin the version, even though it kind of makes things a little bit more annoying for users, but, it kind of eliminates scenarios like these.
From ever happening. So then we can freely import internal stuff from the SDK.
**Aaron Abbott** 31:32 Yeah, I mean, I think I'd like to avoid…
**Leighton Chen** 31:35 Yeah.
**Aaron Abbott** 31:41 Lynn, do you want to…
**Leighton Chen** 31:41 Sorry, Erin, Glenn.
Oh, yeah, I was gonna say, like, maybe it was what Aaron's gonna say, too. I would… I think pinning the SDK, it would introduce a lot of other problems, especially Because a lot of… A lot of distros, a lot of other, dependencies rely on the SDK, and we want to freely let users use whatever SDK version they want.
Especially if they're not in control of their dependencies, so… I think ideally, like, like, originally, when a PR came out to kind of use this internal utility, right? Ideally, what we wanted to do was to have, like, hey, this is the min version that this utility existed in, and we would have to bump up the SDK dependency min version Of the exporter, right? That's ideally what we wanted to… what we should have done, right?
And now we're just in this kind of hole of, like, we didn't do that, so… Theoretically, people can use older versions of the exporter.
And have this, kind of.
Weird dependency on this utils that… Might not have… that… symbol, or utility, and you're saying that it's the same thing for environment variables. And we have… we actually have that, yeah.
For environment variables, we kind of solved this a little bit for semantic conventions, because we have this, like, forever supporting this incubating kind of state.
So we either need to have, like, strict… stricter checks for, hey, you're using this Function or symbol, and you have to… For every new feature, we have to like, bump up a min version, or something like that. And that's going forward in the future, but right now, we have a lot of, like.
The blast radius for this is very large already. We already have a lot of, Lucas, like you said, the, environment variables that we use that we have to support forever.
And I'd rather do that than force people to use a certain version, or break… break someone.
Sorry, that was too convoluted, but yeah.
**Aaron Abbott** 34:25 Yeah, that's pretty much what I was gonna say, too. I just… I feel like, especially in Python, there's, like, this, Kind of bifurcated thing where some people pin, like, everything because it's a mess, and then other people pin… absolutely nothing, like Flask, and then… when things upgrade, they say, oh, you need to lock your dependencies and then test everything out. But, yeah, maybe we can… we could be in the happy medium, and… Yeah, like, if something is de facto stable, we should probably just expose it and make it stable. Like, we can… Rely on the semantic versioning requirements that we have and stop trying to play fast and loose like we've been doing.
At least that's my, opinion. Also, I don't know if Leighton and Ricardo agree with that, but… yeah.
**Riccardo Magliocchetti** 35:21 industrial copy.
**Leighton Chen** 35:22 I think we want to rely on semantic brick.
Oops, sorry.
**Riccardo Magliocchetti** 35:27 Right, right.
**Leighton Chen** 35:34 I was just saying, yeah, we want to rely on semantic versioning implications when we can, and then I think when we're forced to, because we, like, kind of missed miss certain upgrades or something, I'd rather not break people, so… Yeah.
maybe we can have… maybe, I don't know, maybe we'll always rely back on, like, toggling or something like that, you know? Like, if there's any… automatic or better way to catch these kind of things, rather than, like, the human eye, I guess.
**Lukas** 36:12 Got it, thanks, thanks for all the input here. So, yeah, it sounds like, yeah, I'll just update the PR. We might have to just have a little bit of code duplication for now, but I think that that's probably preferable than… You know, having to pin, so…
**Riccardo Magliocchetti** 36:30 Yeah, like, I think it would be fine to have just a bit of code duplication for this.
Is that the use case?
Thank you.
Next topic… is from… Redeema? Redema? Sorry, Sorry for my pronunciation of your names, but…
**Ridhima Satam** 36:54 Yeah, that's right. Yeah, it's Redhima.
Yeah, so this is the Langchain PR. I know there is this, another PR from Akumar, thanks for Leighton. Thanks for Leighton for pointing that out. So I spoke to him, and, there are other things as well in his PRs, like, I think he has few PRs for Langchain. And this is a very, like, a subset of… those, like, just workflow and basically supporting the chain, so workflow and invocation. And this is also using the generutels, so… I think Nark Commerce PR is not using that, so I'm just, Removing some part of it.
and implementing here. So, he was going to also, review this, but looks like he's on vacation, so I'm just asking for reviews on that.
**Liudmila Molkova** 37:49 Redeema, I took a look, it looks great, I want to try it out, today, and I'll approve it, right after, because I played with long-chain instrumentation a bit from up on inference, and I was… It was so far from what I think it would be. I'm curious how this one looks like.
**Ridhima Satam** 38:08 Okay, yeah, that's great then.
**Liudmila Molkova** 38:11 Yeah, thank you.
**Leighton Chen** 38:12 That's great, then.
Thank you. Yeah, thank you.
Thank you.
Yeah, Radim, I'll take a look at this today. I also think that, Natkomar's PRs right now, they're not utilizing… much of the logic, the new logic we have in GenAI Utils, so feel free to… Build off of this one, because it seems to be more updated.
**Riccardo Magliocchetti** 38:47 Alright, thanks.
Okay.
Adam, we have a bunch of topics.
**Aaron Abbott** 38:58 Yeah, so… I have another agenda item a little later for this one, but, I just… I just wanted to raise this one. So, I saw, like, this makes sense to me.
I left a comment in the issue, if you can click on that, it's a 4904, it's in the description there.
Yeah, so I was… I was basically just wondering, like, like, the… the PR looks fine, I think it's just a decision of, if we should support this. So I was wondering, I don't know, Lucas, if you know if any other languages already have this customization. And the reason I'm asking is just because it is pretty clear in the spec which Error codes are retryable.
**Lukas** 39:52 I'm not personally familiar with how the other languages handle this, but I can take a look.
Yeah, so… I think it would still be nice to add, at least in the… Export or constructor, maybe an argument to allow people to configure this, but… We could just decide to not expose the environment variable.
to produce, I guess, bloat.
**Aaron Abbott** 40:25 Debelieve.
**Leighton Chen** 40:32 Sorry, I didn't take a look at the PR too closely, but is this… An example of the exact scenario we talked about?
just now, Lucas, about supporting an environment variable.
**Lukas** 40:45 Oh yeah, I guess I didn't really think.
**Leighton Chen** 40:48 Oh, yeah.
**Lukas** 40:51 Yes.
But, yeah, I think the main… I think… We're asking, like, whether or not we should just add this functionality in general, right?
**Leighton Chen** 41:01 Oh, yeah, totally. Yeah, sorry, I didn't mean to derail that conversation. Definitely what Aaron says still applies, but I just wanted to… Point out the irony behind this, so…
**Aaron Abbott** 41:17 Yeah, lucas, I think… Yeah, I agree, maybe we could just go without the environment variable to start. I just… yeah, like, the concern is just the API bloat, and you know, obviously somebody needs this. I think they mentioned they're having 500 errors, and they want to retry them. I think Like, yeah, if it's a config option.
That's fine, but there's generally a good reason not to retry 500 errors, because it's like, you know.
It's not… not necessarily retryable.
No worries, Leighton.
So, like, in terms of, you know, Giving people a… Like, cohesive story.
I think it's kind of, you know, like a… what do you call it? Like a foot gun, maybe? So, But yeah, I guess I was just asking for… more context on… Yeah, does anybody else have thoughts on this one, if we should just go ahead and merge it, or if, Yeah.
**Mike Goldsmith** 42:21 I feel generally the same, like, it's…
**Leighton Chen** 42:25 Despite.
**Mike Goldsmith** 42:25 quite clear on what it wants to do, and what we should do, but having options is nice for people that do want to exercise those, but yeah, as long as it's not… a requirement to set, as long as it's totally optional and someone can opt into the behavior if they've got a particular need for it. I'm not against it, it's just, yeah, the same thing of, we don't want the API to come really cumbersome, so someone can't use it very easily.
**Aaron Abbott** 42:56 Okay, so maybe let's… let's go ahead with this one, I think. It's, like, a pretty direct change, but just to give an example of why I think the API bloat can be problematic, I don't know if we've got Dylan here, but we looked at one point into reusing gRPC's, like, built-in retry behavior, which is its own API surface, right? So, like, you could configure… I think you can configure the channel to do the retries, kind of, like, transparently. And the… the issue was the spec doesn't do the same thing as the gRPC retries spec says to do. It says to re… return… one of them says to return, like, a retry info protobuf, and then one of them says to do something else, maybe it was, like, a metadata key or something like that.
So if we do this, we kind of… I just hope we don't get stuck having to keep the like, code-based retry, because we expanded the API surface, for example.
**Liudmila Molkova** 43:54 I think some other languages allow to cost users to pass the fully constructed gRPC client, or HTTP client.
**Aaron Abbott** 44:06 Yeah, and I think… I think we do as well.
**Liudmila Molkova** 44:12 So then, this behavior is configurable, it's just hard.
**Aaron Abbott** 44:18 It doesn't…
**Lukas** 44:19 We support passing the gRPC client, but in HTTP, we do.
But… I think, yeah, HTTP is kind of another story, because we kind of do our own retry… Anyways… But…
**Aaron Abbott** 44:37 Okay, my bad, I thought we allowed people to pass the channel.
**Lukas** 44:44 I see channel options.
**Aaron Abbott** 44:48 Yeah. In any event, I guess, like, for the specific issue, it wouldn't help because the, we have the code doing the retries instead of the gRPC… I don't remember the exact details. I can actually try to share them on the issue if that's helpful, but, Yeah.
I think this one we could probably go ahead with. Oh.
Sorry, Lumo, go ahead.
**Liudmila Molkova** 45:12 So this is the layer above, they're a trice, they are not in this. Okay, I see, thanks.
**Aaron Abbott** 45:23 Okay, I think we can, we can probably just move on.
**Riccardo Magliocchetti** 45:32 This is also from you, Aaron?
**Aaron Abbott** 45:36 Yep, so this one, I apologize, Lucas, I think it got kind of stuck.
I… I know, like, we went to the spec, I think I had a conflict that day, and we discussed, some of the concerns.
I'm gonna just post this one here.
So I had opened this issue in the W3C repo because it was… Still kind of unclear to me whether or not there would be additional changes to the, to the thing that we implemented.
So I, I, I don't know if you got that link, Ricardo, yeah.
So, like, Daniel closed it out, but I still feel like the… if you just go to the last comment there, I still feel like this is very confusing, because the, the W3C spec says, vendors will only parse trace flags supported by the version of the spec, but we're not, like, revving the spec, we're just adding a new flag without revving it.
So… in any event, it sounds like it's not gonna change, so… I think I'm okay to merge this one now, but… Yeah, any… any other concerns from anybody?
**Riccardo Magliocchetti** 46:52 I'll be like, we'll find out if something breaks.
once we release, so…
**Aaron Abbott** 47:00 Yeah, I think… I think it's one of those things where people will just have to, like, downgrade their dependencies and be careful when they… when they take this upgrade, so… we didn't want to… I think, for context, we didn't release it, because it was after maybe, like, December, when a lot of people were out. We had about a 2-month period with no releases, so we wanted to put this in, like, a smaller, more normal release in case it did bring people.
**Lukas** 47:32 Yeah, I think the spec, it's a little ambiguous, but, like, I think for older versions, it… I mean, it kind of mentions that The extra flags should be zeroed, right?
So… So, like, you could kind of figure out what version you're on, kind of infer it based on that. I think that even with, like, going from trace context, this is V2, right? I think that people are actually basically using that random, trace ID flag as kind of an indication if you're on V2.
If you kind of read through the spec.
**Aaron Abbott** 48:11 I think it's still V1, though, that's the thing. Like, it's, like, level… W3C level 2, but we're not revving the, the version in the wire, or did you mean that.
**Lukas** 48:24 Sorry, yeah, I meant, I meant to say, like, level 2, yeah.
**Aaron Abbott** 48:30 Yeah, that makes sense.
I don't know, does anybody else have any concerns on this one, or should we just go ahead and merge it now? I think we talked it to death, like, a month ago, or a month or two ago.
**Riccardo Magliocchetti** 48:49 It's fine to mark.
**Aaron Abbott** 48:52 Okay.
Great. Thanks for your patience, Lucas.
**Riccardo Magliocchetti** 49:04 Okay, we have 10 minutes left.
I don't know if you have enough time for discussing this, Aaron?
**Aaron Abbott** 49:13 Yeah, probably not, should we…
**Riccardo Magliocchetti** 49:20 Well, what is more… What is more urgent, this one, or the Gen AI repo?
**Aaron Abbott** 49:29 I think let's… let's put mine last, and then we'll… we'll just keep moving on.
I can update. So, I think maybe Ludmilla grew up.
**Liudmila Molkova** 49:38 And we can apply whatever we decide in your topic to the new repo, right?
So, I'll keep the new repo quick, so… I… I've got some… I've got some feedback, but not much on the layout and anything, and the new repo. I don't think there is anything blocking.
So, I'd like to, oh, I'm making an assumption that we should just… Try to move on.
And, be iterative. There is no, no… finality in, like, making this repo life. We can change the layout if you don't like it, or we can definitely introduce a lot of Cool things there. The key question, though, is, how do we do this?
And what do we do with the existing PRs?
What I'd like to do, I've started looking in all of the open GenAI IPRs that we have, and there is a decent portion of them that we could try getting merged.
But it depends on the cooperation of PR Author to resolve some minor needs, and somebody hitting the merge button once we are happy with it.
So… I'd like to do this exercise tomorrow, and I'll start today.
And would I be able to grab, Leighton or Aaron one of your attention, and just send you PRs that I think are ready, and get your A rubber stamp, or, like, real review, and get it in, so that we can Sync it with the new repo, and then… Maybe next week, move on to the new repo.
And for some of them, I think, unfortunately, for some of the PRs that, let's say, set up scaffold new instrumentation for Cohere, I think it doesn't make sense in this repo, especially if it's just a scaffolding, or for the large PRs that didn't get any attention in, like, the past couple of weeks, and don't seem to be close. I'll probably just leave a comment saying.
That, if you still want to pursue it, here is the new repo. We will be setting it up soon.
Come back there.
**Aaron Abbott** 52:00 Yeah, I'm happy to… happy to help out. You feel free to just, you know, ping me the issues or PRs that are ready to go, and Should we… should we maybe do, like, a… Update the bug templates.
Also to help make it clear, or anything like that.
**Liudmila Molkova** 52:19 So when people open the people request, they know to go to the new repo? We should do it once there is a new repo, right? Like, for now.
I don't know how we should do it, but let's just make it fast so that we don't affect many people, at least.
Yeah.
Cool, so then I'll prepare today.
**Leighton Chen** 52:43 Feel free to be like… So then, I'll prepare today?
Oops, sorry. Yeah, feel free to be strict about, like, what we include and not include. I think it's better to communicate and move fast, rather than, like, ask for permission and, like, wait around.
**Liudmila Molkova** 52:59 Yep.
**Leighton Chen** 53:02 Yep.
**Liudmila Molkova** 53:08 Awesome. Then, I think we are good with this topic. If you have any feedback about the new repo, you know where to find me.
**Riccardo Magliocchetti** 53:22 Thanks… And then… less topics from 10 meme?
**Tammy Baylis** 53:30 Hi, Ricardo. Hi, everyone, I made it just late today. Yeah, just… PSA, or please take a look at this PR, it's been open for a while, got a couple of approvals already, and yeah, thank you again, Lucas, for… Some discussion a few times ago, the reason I'm doing it as an experimental contrib, entity, instead of doing it through baggage, is for ease of use, so that end users or instrumentations don't have to, bear the burden of so much context management, so… Yeah, please take a look. Thank you.
**Riccardo Magliocchetti** 54:15 Thanks!
Let me take a quick look.
**Aaron Abbott** 54:23 Actually, I'm wondering… I think this, PR might predate the context-scoped attributes, but there's maybe, like, a little bit of overlap?
Have you seen that proposal, Tammy?
**Tammy Baylis** 54:35 I have not, where is it?
**Aaron Abbott** 54:40 Let me dig up the link there. I don't know if the… it was an OTEP, I don't know if it's been merged yet.
**Riccardo Magliocchetti** 54:47 The link to the notes.
**Aaron Abbott** 54:49 Okay, perfect.
**Tammy Baylis** 54:50 Thanks, Ricardo.
**Mike Goldsmith** 54:54 Don't think the OTEP has merged yet, but it's getting closer.
**Liudmila Molkova** 55:00 Yeah, it's not, but I think if you… We'll leave a comment or two, if you read through it, and if you find anything interesting, or anything that doesn't work for… according to… it's just effectively what you've done counts as some form of a prototype.
So, your feedback on the setup would be great.
**Tammy Baylis** 55:18 Cool. Okay, I'll have a look at this. Thank you. I didn't know this was out.
**Riccardo Magliocchetti** 55:31 Patents, and now we have 4 minutes to discuss.
contributor experience, yeah.
**Aaron Abbott** 55:40 Should we… should we just call it there, and everybody gets their 4 minutes back? I think that the TLDR is… you know, I just wanted to get feedback from everybody on this. I know that there's a lot of PRs that are kind of waiting for maintainers, and I think we could clarify, like, the semantics.
The semantics between, like, you know, how approvers and maintainers operate, I guess, but let's… let's save it for next week, I think.
**Liudmila Molkova** 56:07 I've added a couple of links at the bottom, because I think Trask did something very related, and if you can open the… link to the Java instrumentation issue, you would see, And it's… I think it's not Java repo-specific, it's replaceable.
But it says who… what's waiting on maintainers, what's waiting on approvers, and so on.
There is a python scrape behind it.
**Aaron Abbott** 56:35 Oh, nice.
Of course, it's a Python script.
**Liudmila Molkova** 56:38 Yeah, and if you like it, it's totally possible to include it in, like, repo.
**Aaron Abbott** 56:45 Yeah, I mean, I'd be okay to just do also, like, we have the board, maybe this predates the GitHub projects that span across multiple, repos, but we… basically, like, I think it should be more clear once something's waiting for maintainers, and, like, also on issues, if they're open to contribution or not. So that, you know, people don't send PRs, and then we bike-shed whether or not it should exist in the first place after they've already contributed.
But yeah, let's save it for next week, I think it's a… probably… 5-10 minute topic, so…
**Riccardo Magliocchetti** 57:23 Yep.
**Aaron Abbott** 57:25 Alright. Thanks, everyone.
**Riccardo Magliocchetti** 57:28 Thank you.
**Liudmila Molkova** 57:29 Thank you.
**Riccardo Magliocchetti** 57:30 Bye, right.
**Leighton Chen** 57:31 Thank you.
Thank you.
