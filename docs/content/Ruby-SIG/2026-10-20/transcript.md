SIG: Ruby SIG
Date: 2026-10-20
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Kayla Reopelle (New Relic, Inc.)** 00:31 Hi, Rob.
**Robb Kidd (he/him)** 00:35 Hello!
**Kayla Reopelle (New Relic, Inc.)** 00:38 Okay, I'm outside, so it's a little windy.
**Robb Kidd (he/him)** 00:42 Can make you out, but yes, it's a little windy.
**Kayla Reopelle (New Relic, Inc.)** 00:46 Okay, good to know. Alright, I'll cut it aside then.
Okay, how's this?
**Robb Kidd (he/him)** 01:26 Very clear.
**Kayla Reopelle (New Relic, Inc.)** 01:28 Wonderful.
Here, the meeting notes… Okay, let's go ahead and get started.
I did not attend a spec site this morning. Did anyone else here attend the meeting?
**Robb Kidd (he/him)** 02:25 I did not.
**Kayla Reopelle (New Relic, Inc.)** 02:29 Let's see, it looks like a new version.
Coming out… And… Maybe some exporters, OTLP, exporter timeout work… They're planning to merge today.
Take a look at just what is included in the release.
Adding sampler shutdown… Unending, not a lot after shutdown.
Shutdown includes force flush… Since we're working on declarative config, that one should gracefully degrade.
So, I don't think anything… SIG that we need to do right now.
Okay, gee.
And… great, we have something on our agenda.
Okay.
Sean, do you want to, talk about this one?
**Xuan Cao** 04:08 Yeah, my background is clear, no, so I don't get very much.
Okay, I'm about to hear.
So if you look at plumbing's, the name… the name section I have is, If something happened, we should really, like, use the arrow and, like, just a good book.
applications, so we just love the… everyone, So, I think NAS preference is to allow to do this arrow.
My preparation sticks to the log driver, so… I just want to get a bit more, more opinions from the group.
**Kayla Reopelle (New Relic, Inc.)** 06:12 Whoops, I was muted. I was saying that I… I think I like to use errors generally when We are trying to… signal that the SDK or API itself had some sort of error processing? Like, error… Within its own handling, and then using… logger warnings when… We have something that… Impacts the way the user is inputting data.
But that doesn't Work in all cases. Most definitely.
We also don't want to, like, raise and cause a problem in the customer's application unless it's… it's dire.
It does seem like in the specification, more and more I'm reading that Warnings are preferred over errors.
But those are just some thoughts I've had lately. Nothing is really a rule.
What do other people think?
**Robb Kidd (he/him)** 07:21 I agree with that statement Like, if… if the SDK is gonna carry on and do something.
Like, warn that it might be unexpected.
Like, the user's given some config that… If… if here… I guess, what are… what are we logging?
Because I… this is the first time I'm looking at this, so… that keys appeared both in included and in excluded? Is that the… the… I would say it's a warning, and… for safety's sake, treat it as excluded. That seems like a warn, not an error, because the SDK can do something useful.
**Kayla Reopelle (New Relic, Inc.)** 08:11 And we're just explaining the behavior that is…
**Robb Kidd (he/him)** 08:14 Yeah.
**Kayla Reopelle (New Relic, Inc.)** 08:15 You know… Taking over instead.
**Robb Kidd (he/him)** 08:18 Given conflicting config.
They are warning them that we have done the conservative interpretation of that CAIC. Seems… Beautiful.
Is that the… is that the question before us on this line? Like, what level should we be logging this at?
I'm reading Matt's comment here to… Okay, well, we definitely need to define overlap.
Which I think, Xuan, you said you've done.
Or will do.
**Xuan Cao** 08:58 The ONAP line is, is fiscal.
**Robb Kidd (he/him)** 09:02 Still logged the warning, because the, like, turn… Don't wanna… No, we should not raise the error. I would… I would agree. Don't raise the error. That is in the spec. Like, SDKs and instrumentations should not… Throw errors that are not handled, because… Misconfiguring the instrumentation is not an application exception.
**Kayla Reopelle (New Relic, Inc.)** 09:27 Okay, yeah, not even on startup, when someone could feasibly fix it.
I guess that is still taking down somebody's app when they met.
running, yeah.
Okay, yeah, I think that makes sense then, using a Warren-level log here as well.
So, it sounds like there might be also a documentation mismatch?
On the front, can we make sure that those docs connect with… the choice here to continue to use the warn level log, or… or am I missing something?
**Xuan Cao** 10:09 Locus, is, is updated, so…
**Kayla Reopelle (New Relic, Inc.)** 10:14 Okay.
Wonderful. Alright, do you need anything from us? Like a… like a comment, or can you comment?
Summarizing our discussion.
**Robb Kidd (he/him)** 10:25 I…
**Xuan Cao** 10:25 I can cut it.
**Robb Kidd (he/him)** 10:26 Go ahead, sorry.
**Xuan Cao** 10:28 Sorry, sir, no, I mean, that's okay. Yeah, I can't…
**Robb Kidd (he/him)** 10:30 Well, I made some comments here in this meeting, so I can write down what I said on a comment and say, like, I agree that we should make sure that overlap is defined so that we don't accidentally raise an exception, and that logging makes sense. Logging at worn with the conservative interpretation of this overlap makes sense.
**Xuan Cao** 10:49 And also, I just, I just wanted to, you know, in general, for the SKK, it shouldn't, like, lose the arrow at all, better, because, you know, any arrow is very zero for each application.
**Kayla Reopelle (New Relic, Inc.)** 11:04 And we do use, kind of, open telemetry handle error, I think, to get around that, generally, when we want to, like, raise something, but that is… more like a log message, unless it's… the error handler is doing something different, if I remember correctly.
You can… Yeah.
**Robb Kidd (he/him)** 11:23 I think it's, we have the raise option, so long as we know that it's going to get caught by our own handler, and that handler generally logs.
So it's, if you would raise an exception in a case where you know that you have some, higher level scope to catch that exception, and maybe do something with it, and maybe not, and then the maybe not has the option to log, so, I'll channel Abdi Grimm and say exceptions should be exceptional, and it, I… in this particular comment of finding an overlap, or keys existing… being… keys in the, I'm sorry.
Values in these config arrays.
might overlap.
Shouldn't be exceptional.
Human's human, and sometimes make mistakes. We shouldn't.
If we can mourn and then do the right thing here.
It makes sense to do that.
if it doesn't make sense to address the inconsistency here, we would raise and then handle the inconsistency at a higher level, but I think it's… Am I correct in that it's appropriate to handle the situation here? And so we don't really need to raise it to a higher level abstract for handling?
Is that right?
**Kayla Reopelle (New Relic, Inc.)** 12:46 I think that makes sense, because we can handle it here, without looking at the specification. We have a clear path forward that… That seems to make sense.
**Robb Kidd (he/him)** 12:57 you might raise for error conditions in cases where your more specific scope doesn't have enough information to know how to handle it, to know what action to take. But if you know what action to take, it's that… Treat overlap values as excluded, because that's the conservative interpretation.
And then warn the user that you might be missing. When you go and look at this, you might be missing information that you thought you'd have.
Did that answer your questions, Rob?
**Xuan Cao** 13:28 Yeah, yeah, they're not counters.
**Kayla Reopelle (New Relic, Inc.)** 13:34 Any other questions on this one?
**Xuan Cao** 13:39 Yeah, fingers, thanks.
**Kayla Reopelle (New Relic, Inc.)** 13:41 Okay.
Let's see, so we're still kind of trekking along, since we don't have any other core topics.
Take a look at the milestones.
Metrics, we're now at 38% complete. Still have a whole lot of PRs.
That have been open for a while, and need some review.
That's the call. So, continue to work on those.
**Robb Kidd (he/him)** 14:13 We need reviewers.
**Kayla Reopelle (New Relic, Inc.)** 14:15 Yes, yeah, if you have time to review metrics PRs, that would be a big help. Okay. I think Matt and I… Have left some comments on things, yeah, and Xuan… You know, you opened a lot of these, so… Thanks for addressing the comments as they come up.
But we're getting… we're getting a lot closer.
Here's… Kind of 6 clear ones that are open that it would be nice to knock out.
One other question that's maybe more of, like, a… Slightly different topic, maintainer type of question.
That's somewhat related, is we have two pull requests now to fix the same logs Issue?
One of them has gone… Or is maybe going stale?
Down here, it's been open for a while.
We're missing some feedback, there's some… some failing tests, I think, or a merge conflict, something like that.
And then there's also this new PR that's, you know, solving it in a slightly different way.
I… my inclination is to kind of wait a little bit longer on the first one. Once it goes stale, then take a look at the second one.
But I'm… I'm curious about how other… People think about handling multiple pull requests for the same issue from different contributors.
**Robb Kidd (he/him)** 15:46 Hmm.
I don't necessarily have a rule.
Well, I guess our options are, we could review the newer one, and decide if it's… if it's sufficient.
except… like, if it… I see that it has a red X, so it maybe needs work, too?
**Kayla Reopelle (New Relic, Inc.)** 16:22 Yeah, yeah.
**Robb Kidd (he/him)** 16:28 So I guess the first… First thing we could do on the more recent one is, Okay, an option. The more recent one, give the same feedback of, like, address the issues in CI?
**Kayla Reopelle (New Relic, Inc.)** 16:42 if…
**Robb Kidd (he/him)** 16:42 If they're legit, sometimes we gotta throw a red X on things that… Pardon?
So confirm that CI is appropriately failing, and then save.
Before we review this, could you address the failures?
And then see which one gets a response from the contributor first?
**Kayla Reopelle (New Relic, Inc.)** 17:02 Yeah, yeah, that works, and then from there, review.
Review the one.
active.
**Robb Kidd (he/him)** 17:08 Attack on that, though, is if we were to read one or the other and review it for consideration, and disagree with the approach, asking them to resolve CI stuff, and then following up and saying that we don't like the approach.
**Kayla Reopelle (New Relic, Inc.)** 17:23 True, true.
**Robb Kidd (he/him)** 17:24 This is a little rude.
Yeah.
Was the reviewed one, the older one, was it reviewed and, like, seems fine, except just needs,
**Kayla Reopelle (New Relic, Inc.)** 17:39 I think…
**Robb Kidd (he/him)** 17:39 Comments addressed, or…
**Kayla Reopelle (New Relic, Inc.)** 17:41 Thank you.
**Robb Kidd (he/him)** 17:41 It's like, what are you doing here?
**Kayla Reopelle (New Relic, Inc.)** 17:45 I think there's just a small comment, but there are some concerns with the merge conflicts, and also the failing tests, because… this was created before a different PR that does touch similar things was murdered.
So, there is a bit of work that needs to be done on it, I think, before it's really ready.
I…
**Robb Kidd (he/him)** 18:10 First-time contributor, too.
**Kayla Reopelle (New Relic, Inc.)** 18:12 I believe so. Let's see… It was at the time, but I think we've now merged.
**Robb Kidd (he/him)** 18:18 Oh, okay.
**Kayla Reopelle (New Relic, Inc.)** 18:18 webinars.
So, yeah, I was trying to dismiss my approval, but I can't seem to be able to do that when there's a merge conflict, and… Some failing tests, so it's also still approved, but, Yeah, we've been waiting on… on about 2 weeks, so… We can…
**Robb Kidd (he/him)** 18:42 is a legit bug that needs addressing? Like, both of these are closing an issue that we have open.
**Kayla Reopelle (New Relic, Inc.)** 18:47 Yeah, both of these are closing… I mean, I wouldn't say probably a bug, necessarily. I think bug is maybe a bit strong. It's more like a misalignment with the specification that… you know, I… it's hard to know what to label it. It's a bug with the spec, but it's not actually breaking anything.
**Robb Kidd (he/him)** 19:08 Yeah, it's a spec complex.
**Kayla Reopelle (New Relic, Inc.)** 19:09 Third. Yeah.
**Robb Kidd (he/him)** 19:11 I have another category. It's not a bug.
**Kayla Reopelle (New Relic, Inc.)** 19:12 Yeah.
**Robb Kidd (he/him)** 19:13 spec compliance issue.
**Kayla Reopelle (New Relic, Inc.)** 19:15 Yes, yes.
**Robb Kidd (he/him)** 19:17 And certainly, it's about logging something, like, it's…
**Kayla Reopelle (New Relic, Inc.)** 19:22 Yeah, yeah.
**Robb Kidd (he/him)** 19:23 The telemetry output is not any different, it's just logging that.
**Kayla Reopelle (New Relic, Inc.)** 19:28 Exactly. It's just the log message that you get when attributes are dropped, or when other things are dropped due to limits or invalid… Classes, things like that.
**Robb Kidd (he/him)** 19:42 Okay.
**Kayla Reopelle (New Relic, Inc.)** 19:45 Yeah, but I think roughly what you had suggested are kind of… reviewing…
**Robb Kidd (he/him)** 19:52 Rev- probably review the new one.
A quick skim of, like, yeah, this implementation seems fine.
Can you resolve the break… the CI issues? And then… Probably doesn't have the merge conflicts that the other does, and…
**Kayla Reopelle (New Relic, Inc.)** 20:05 Yeah.
**Robb Kidd (he/him)** 20:07 It'll be less work all around, too.
To carry on.
Yeah.
**Kayla Reopelle (New Relic, Inc.)** 20:16 Yeah. Okay, nice.
Sounds good. Thank you.
Let's see, we don't have anything else… On the agenda… oh, we were gonna look at logs, possibly, too. I don't think we've made much progress on logs right now. Yeah, we're focusing mostly on metrics, so… I think that's fine that everything is… Staying steady there.
**Robb Kidd (he/him)** 20:43 We will do what we can with the resources we have.
**Kayla Reopelle (New Relic, Inc.)** 20:47 Indeed. That's all we can do.
Okay, any other conversations people want to have about CORE before we move on?
**Robb Kidd (he/him)** 21:01 Oops, bye.
**Kayla Reopelle (New Relic, Inc.)** 21:02 One last update that I just remembered is, I did close the release that was auto-generated this morning because there's one more pull request to fix a bug on the config gem that, that Matt had done some follow-up on this morning, and so it is ready to go in now. So I'll merge that and then reopen the releases and get those going.
**Robb Kidd (he/him)** 21:28 Oh, I have to drop, I'm getting pulled into an incident.
**Kayla Reopelle (New Relic, Inc.)** 21:31 Oh, no, okay.
**Robb Kidd (he/him)** 21:32 I'll see y'all later.
**Kayla Reopelle (New Relic, Inc.)** 21:33 See ya! Thanks for coming.
Alright, contrib!
Take a look… Yeah, thank you for taking a look at this, Xuan. There's one other comment that I feel like I need to… I'd be curious to hear other people's thoughts on how to address it, this comment about, semantic conventions in the code, or in the tests, or not at all using those constants. I'm open to using the constants. I think that it can sometimes make things A little more difficult to read, but we do have them, and it is a way to make sure that the correct string is in there without any sort of typos.
But I think we have really inconsistent use of the semantic conventions right now.
So, I'm curious if anyone here today, Has thoughts or preferences about using them or not using them.
Or… Postponing their use, and maybe doing a larger… Overhaul to bring consistency, Yeah, what are the thoughts of the people here?
**Xuan Cao** 23:00 Well, to speak from my point of view, I actually… I haven't looked at those, like, semantic instance.
a long time, because last time why… Time to do this inner work.
I never get it… I never get outside how those, work, because most of them are incubating, I'm not sure if that inhibiting means that we are not, stable, or we can change in the future, or… I don't know, so basically, I don't know what's the meaning for those constants.
**Kayla Reopelle (New Relic, Inc.)** 23:34 Mmm,
**Xuan Cao** 23:36 I know I sound a youth constants, Although, I, I forgot it is, is there, also in incubating lots, So, so, to be honest, before we start this out, like, using this, like, the spring will be fine, and then two coffins will be the SGS.
**Kayla Reopelle (New Relic, Inc.)** 24:02 You're cutting out a little bit for me there, but, I think… one of your first comments was, about the incubating constants. So those… that category of constant, yes, is… The constant itself will never go away, but that value may not eventually become a stable constant. So we don't want to ever break those constants. Like, you can… you can use them in instrumentation, and they will be considered stable.
The goal is for every incubating constant to eventually Become stable, and when it is stable, kind of like in our… SEMCOM opt-in transition.
you can then, change the constants from the incubating ones to the stable ones with the same string. So in a lot of instances, we may have More than one constant that points to the same string.
Since, fortunately, this is, like, a stable specification, like, we will just be able to use the stable constants here.
And then… I think your second point was about using them or not using them, and that got a little fuzzier for me. Could you… Summarize that again?
**Xuan Cao** 25:18 Oh, sorry, I'm just saying, I mean, I don't, I don't guess using the, this is just the screen, not the process, for this PR.
And then… We can just, replace those constants, those stable constants.
In the Bluetooth.
**Kayla Reopelle (New Relic, Inc.)** 25:38 Okay.
That sounds good.
Alright.
Let's see, and then this one was posted about in the channel… Anthropic now has native instrumentation.
For OpenTelemetry, and so, we can likely retire this gem. I do want to test it out before we do, because I know this was added specifically for some context propagation, just to make sure that the context propagation is still working.
But, but yeah, this is kind of exciting news to get.
More native instrumentation instead of things we need to maintain ourselves.
Let's see, is there anything… In contriv, that's not on the agenda that people would like to talk about today?
Oh, I see something in the chat.
Oh, thank you, Joseph, for talking with Mike. That's unfortunate that he doesn't like hotel.
So, I guess we'll have to… Think about those conventions on our own.
Could you pass that along to Rob, or maybe add it somewhere?
maybe, or I guess maybe message Rob instead of just saying it outright.
To let him know, since he's been driving that one.
Thank you.
Okay, well, we keep moving along. This is exciting. The auto-instrumentation was merged into the operator.
So, after that releases, then we update the Helm charts, and then… Does that… clear the path for the TracePoint PR, or do we still need to wait on that one for a little longer?
**Xuan Cao** 27:45 Oh… I mean, we can merge the different, yeah.
Right now, because, the images itself are…
**Kayla Reopelle (New Relic, Inc.)** 27:53 Mmm.
**Xuan Cao** 27:54 So, and it was basically when you update those, even if we just update, operators editor folds.
**Kayla Reopelle (New Relic, Inc.)** 28:04 Yeah.
**Xuan Cao** 28:04 Yeah, one thing is that you can, basically prefer to use the SDK version.
For the image version, not the version, not the, you know, the I'm doing.
Oh, so… Industrial use, well, Allow those authentication to make… version 2, same as SDK, SDK version, yeah.
**Kayla Reopelle (New Relic, Inc.)** 28:31 Okay.
Sounds good.
Alright, awesome.
**Xuan Cao** 28:41 Oh, and then, and then it's, it's, it's, disabled by default.
So, they're not ready to have a, AMO, identification.
Not mine. It's disabled.
Yeah, but you can enable it by itself.
Okay.
**Kayla Reopelle (New Relic, Inc.)** 29:06 Okay, nice, so we can… we can flip that.
Sounds good.
Okay, well then, I guess we can keep this a little shorter today, since there isn't a whole lot on the agenda, and there's… a lot of… Work to review and such. So, unless anyone else has anything they want to talk about… I am… Good to wrap up here. Any other topics?
Okay, great. Thank you all for coming, and I'll see you online, and see you next week.
**Xuan Cao** 29:50 Nice. Cool.
