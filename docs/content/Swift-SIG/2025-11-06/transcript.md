SIG: Swift SIG
Date: 2025-11-06
Duration: 18 minutes
============================================================

## Zoom Recording Transcript

**Ariel Demarco** 01:43 Hey, Ellen.
**Bryce Buchanan** 01:46 Hey, how's it going?
**Ariel Demarco** 01:50 Just initiating, so… No, I'm okay. Nice.
**Bryce Buchanan** 02:02 No, man.
You know, you have too many windows open when you can't find the meeting notes in the list when you're trying to share on Zoom.
Here it is.
Where did it go now?
There it is.
**nacho** 03:18 Sorry, I'm a bit late.
**Bryce Buchanan** 03:20 Hey, no problem.
Shall we get started?
**Ariel Demarco** 03:27 Sure.
**Bryce Buchanan** 03:28 Alright, so let's take a look at topics from last week.
Cocoapod issue in Slack, oh, of course, as usual.
One.
**Ariel Demarco** 03:41 It's like a…
**Bryce Buchanan** 03:42 Okay, go ahead.
**Ariel Demarco** 03:43 I didn't fix… I didn't fix the issue, it was… It was a problem.
Regarding the way we manage versioning, semantic versioning, I already fixed that and did the release.
**Bryce Buchanan** 03:57 Excellent.
**Ariel Demarco** 03:59 also communicated to… the… the reporter that… They can now use all the bot specs.
**Bryce Buchanan** 04:07 Thank goodness.
Alright, so, deploy OS version.
Already… Yeah.
**Ariel Demarco** 04:22 Yeah, I know it's already played.
**Bryce Buchanan** 04:23 That's, I guess, topics from last week's, topics from last week's. summary on issues… Doesn't look like Billy's here.
**Ariel Demarco** 04:34 Nope.
**Bryce Buchanan** 04:35 That's okay.
And… Next release date? Was that release made?
**Ariel Demarco** 04:47 Yeah.
**Bryce Buchanan** 04:48 Okay, cool. And then, the real, real topics.
from last week. Metrichead PR.
**Bee Klimt** 05:01 Yeah, so I think the only big thing left to discuss in that PR that's still… sort of undecided is the exact format of the… of the exception stack traces. I did the, simplified flattened JSON that Alex recommended last time. But yeah, I don't know if there's consensus on it or not.
There is a doc describing the format and the changes versus Apple's JSON format.
**Ariel Demarco** 05:35 I haven't read, to be honest, the doc with the new format, but… I'm glad they do it.
But yeah, if you flattened, I think that's the most… important thing.
to be done.
**Bryce Buchanan** 05:56 Cool. I'll take a look at this after the meeting. I haven't had a chance to look at it yet.
But, yeah.
Oh.
And, okay, alright, any… I guess there's no… nothing else to discuss there.
So the new topics… sorry, go ahead.
**Ariel Demarco** 06:32 Yeah, so one of the dependencies that dependable goes and changes in OpenTelemetry Swift is whenever OpenTelemetry Swift code changes.
But it changes the from.
On the base of it, to the new version.
We enable the from, so we can accept multiple versions.
So, AWS EXACT, Or we use from.
Or… I don't know, seems like we are, like, constantly updating.
Unless it's necessary to the OpenTelemetry shift.
Or new versions.
And at the same time, this updates SPMs. It doesn't update Googlebots.
So, it would be good to… I don't know if there's a way to configure Dependable to also add a node or something like that, saying, okay, aside of this, you should do that.
Or we should use this PR and always include the Genesis and CocoaPods.
Or not even take into consideration Dependable and be able to remove To track this dependency, because we do it In the SIG meeting.
**Bryce Buchanan** 07:46 Yeah, I think, Yeah, if we can configure Dependabot to just ignore this one, I think that would be okay. We could make it a little bit more… Intelligent, like, maybe only do it if there's a major version change.
But then again, I think that we pretty much cover it in this meeting as it's part of, you know, the things that we talk about.
I don't know, does anybody else have any thoughts?
Okay.
**nacho** 08:15 Okay.
Yeah, these dependable, too.
Too noisy, right.
**Bryce Buchanan** 08:22 So annoying, so annoying.
Yup.
I'll look into this.
**nacho** 08:38 I think if you close that, Pierre, And not merge, it won't… Ask you again for that.
dependency. Yeah.
**Ariel Demarco** 08:47 that version of that dependency. If you bump open dependencies Rift Core again to 2.3.1 or 2.4, it's going to reopen a new PR. Oh, really? That new version, yeah.
**nacho** 08:58 Even if you close this one.
**Ariel Demarco** 09:00 Yeah, yeah, it's… it's a pain.
**nacho** 09:04 Okay. Bye.
**Ariel Demarco** 09:05 You can try it out, like, whenever you close it, it will add a message at the end of the… of the PR saying, okay, I realize you closed this, I won't… I won't bother you anymore with this version.
But… Then I'll do.
**nacho** 09:18 Okay, I thought it was referral to that package, like… But yeah, it's…
**Ariel Demarco** 09:27 Because you… yeah, there, renovating our notification.
If you will see the bottom of it.
Because we are merging, Renault will ignore this update from 2.3.0.
**Bryce Buchanan** 09:42 Oh, here we go.
**Ariel Demarco** 09:42 Once a newer version is released.
**nacho** 09:46 Oh, wow.
**Ariel Demarco** 09:46 There's… there's a help there.
with.
**Bryce Buchanan** 09:49 There we go. Alright, well, I'll, I'll, I'll add that in. I can do that after the meeting.
**Ariel Demarco** 09:55 Okay.
Awesome.
**Bryce Buchanan** 09:57 Cool.
**nacho** 09:59 Yeah, I must say about something related to this, the nightly builds with the core, with the main branch of core.
I am not finding a way to do that, really, because you have to modify the package.
That you have just checked out and SPM.
Continue saying that you have a folder there, and it doesn't update, and it fails constantly. With a package edit, Yeah, I'm trying to get there. I have been, like.
2 hours now, or even a bit more, trying to have a solution, and committing and committing, changes, because you have to in a fork that they have, because you have to run that on main.
Yeah, it's been challenging, to say, yeah.
**Bryce Buchanan** 10:56 What… what if we had a, I know this is probably not a great solution, but what if we had, like, a template, package? Swift.package?
That uses just, rather than using a version, uses a reference, like a branch reference.
for, core…
**nacho** 11:17 And then it just… But then you…
**Bryce Buchanan** 11:18 When we run the job, just overwrite the package in the root folder with that… with that template package.
**nacho** 11:28 Yeah, but then you have to modify the package, right? The default package that the user will use.
You know what I mean? I mean.
We have a package.suite in the project that the users just use?
**Bryce Buchanan** 11:44 Yeah.
**nacho** 11:45 And if we… have to modify that once you have done the checkout. It has already downloaded everything and doesn't allow you to.
Change the dependency.
**Bryce Buchanan** 11:55 Oh, okay, interesting.
**Ariel Demarco** 11:58 Oh.
**nacho** 11:58 I mean, if we had another package, right, we could have had… the back package, I don't know, maybe? Something… yeah, I'm still trying to edit that, but yeah, it's… It's not easy.
**Ariel Demarco** 12:14 that they have?
**nacho** 12:14 Forgotten about it, right?
I am still on top.
**Ariel Demarco** 12:19 And if we… Provide an environment variable, or two.
So, let's say you…
**nacho** 12:29 Yeah, we haven't write that, right?
**Ariel Demarco** 12:32 Yeah, and you have one environment variable to either use, like.
Use the normal way, or nightly way.
Or it's nightly bill, or something like that, that basically… Yeah, like that.
At the bottom.
And another one that is the hash, the commit hash, as the value of the other variable.
So, you can replace the…
**nacho** 13:00 Yeah, that…
**Ariel Demarco** 13:00 revision.
**nacho** 13:01 Yeah.
Yeah, I can… I can try something like that, yeah. That's a good, good idea, thanks.
Yeah, so we can set that environment variable and download a different… Yep.
**Ariel Demarco** 13:14 It will only work on… CLI.
Runs, probably, so it's useful for your use case.
**nacho** 13:23 Yeah, yeah, because reading the package is… I think it's a noble.
I have, like, 25 comments now?
**Bryce Buchanan** 13:32 Trying to fix it, and… Ouch.
**nacho** 13:34 There is no way. Yeah.
**Ariel Demarco** 13:36 Squash merch.
**Bryce Buchanan** 13:39 Yeah, nobody will know, it's fine.
**nacho** 13:42 Yeah.
**Ariel Demarco** 13:48 Try one, try two, try three.
**nacho** 13:52 Yeah, you can… I mean, if you… if you've seen my fork, you can see that my main, committees, like.
Yeah, I don't know how many.
Yeah, 13 commits ahead.
**Ariel Demarco** 14:08 So yeah, 13.
**nacho** 14:10 Thrice.
with something that you can only try when it's running on the GitHub action.
**Bryce Buchanan** 14:19 Okay. Are there any other topics before we review?
Issues in PRs?
**Ariel Demarco** 14:27 Not from my side.
**Bryce Buchanan** 14:28 Okay.
I was thinking we'd just go over everything really quick. Yeah, so, Chores, as usual, filling up again.
**Ariel Demarco** 14:42 And I noticed some of them.
But they keep coming.
**Bryce Buchanan** 14:47 I know, it's so… yeah, it's crazy.
Okay, interesting. I thought that that got merged already, that's weird. Okay, so nothing… nothing new, just some things that need to get merged.
**Ariel Demarco** 15:06 Neither here.
**Bryce Buchanan** 15:08 And dock update. Oh, okay.
Yep, nothing, nothing crazy here.
**Ariel Demarco** 15:29 Yeah.
**Bryce Buchanan** 15:33 I see you just have one bit of feedback.
**Ariel Demarco** 15:36 Yeah.
**Bryce Buchanan** 15:37 Okay, any issues?
This one that… hopefully we can close this one.
With the metric kit.
that, that B has been… B's PR, because I think that that's kind of related there, so I'll take a look at that and see if that's actually the case.
**Ariel Demarco** 16:01 Yeah, the thing is, they are trying to use metrics.
I, I see… I think they, they kind of initialize something.
B, on the other hand, it's using Svens.
For some, and lots for the other.
**Bryce Buchanan** 16:20 Okay, and nothing new on the issue front here, just some… To do tasks that need to get… need to get taken care of.
Okay, next week, I'll spend more time working on OpenTelemetry stuff. This week, I'm on, like, support duty, so I don't really have a lot of free time in my daily activities to work on.
openTelemetry, so… hopefully I'll be able to get Through some of these issues.
Alright, any other… Anything else for today?
**Ariel Demarco** 17:01 I mean, not really.
**Bryce Buchanan** 17:02 Alright, cool.
Lucas, I don't think that… I've seen you visit before, are you just visiting, or, Did you have anything you wanted to discuss, or any questions?
**Lucas Marçal** 17:18 No, just, joining as a listener for, like, the first time, but I, I went to, like, maybe… add some contributions, or participate more actively on the OpenTelemetry SDK development, so… Yeah, I guess that's… that's it. Just, learning… How things work, and… yeah.
**Bryce Buchanan** 17:54 Right on. Are you in our… in the, CNFC Slack?
**Lucas Marçal** 18:00 Yeah.
**Bryce Buchanan** 18:01 Cool, yeah, we have a, we have a channel in there for this, SIG and SDK, so if you have any, like, if you're looking through stuff and don't understand how things work, just send a message in there and, you know, somebody will… will help you out.
Probably myself, or Nacho, or Ari.
**Lucas Marçal** 18:21 Perfect, thank you.
**Bryce Buchanan** 18:23 Yeah, right on. Alright, well, I guess, sounds like there's not really anything else to discuss today.
I guess I'll see you all next week!
Bye.
**Ariel Demarco** 18:36 Bye, guys.
**nacho** 18:37 Mate…
