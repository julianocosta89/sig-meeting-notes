SIG: OpenTelemetry C/C++ SIG
Date: 2026-03-09
Duration: 34 minutes
Zoom Recording URL: https://zoom.us/rec/share/t9GRs5O7-rSrSXywrFUTWlqoutZi2TWmWuLuHEptR2kQiZDDTYpT-Eq7xXCCWF2x.psCCLU4YVZGpHhw2
============================================================

## Zoom Recording Transcript

**Tom Tan** 03:12 Hi, Mark.
Good afternoon.
**malff** 03:35 Hi, Tom.
**Tom Tan** 03:40 Good evening, and Nalid will also join to this meeting.
**malff** 03:44 Okay, great.
I don't know if you noticed, but, We know of something which is broken in CI in the benchmark workflow.
And that seems to… To be related to the new benchmarks that were added recently.
**Tom Tan** 04:42 Okay.
**malff** 04:43 Let me show you.
Yeah, or from… All the builds have been failing consistently.
For a while.
**Tom Tan** 04:59 Right.
**malff** 05:00 after this thing was merged, so I don't know… Oh?
But depending on… Yeah, if you could take a look. I tried to…
**Tom Tan** 05:12 Could it put a quick.
**malff** 05:13 not find anything.
**Tom Tan** 05:15 Okay, maybe, yeah, you'd go to… take a timeout, could happen, because a new test could run long… longer than the previous one. But let me take a look. Yeah, thanks.
**malff** 05:27 Okay.
Trying to do a copy and paste, but no.
Sorry I could not make it last week, Was Doug, present? I saw him online.
**Tom Tan** 06:59 You mean the last week?
**malff** 07:01 list.
**Tom Tan** 07:02 Yeah, yeah, he attended the meeting the last Wednesday, and also Severin also joined the meeting.
**malff** 07:08 So, okay.
**Tom Tan** 07:11 And we mainly talked about, like.
Hey, several may introduce some new contributors to the C++ community, I think that is still going on, discussion with the company, I think Bloomberg, I mentioned.
**malff** 07:29 Well, I don't have any news on that. I mean, the person who knows the best is Severin. He was looking for, basically for people to work with them. I don't know the timeline for that. My understanding is that this is for… Spring, I don't know when.
**Tom Tan** 07:48 Yeah, I mentioned sometime, like, maybe starts from April or something, but no… No accurate time, yeah, on that.
**malff** 07:56 Yep.
My understanding was something like April to June, or something like that.
**Tom Tan** 08:00 Yeah, I think that's possible.
**malff** 08:03 Okay.
But no, I don't know what the… what the status of that is.
**Tom Tan** 08:09 Okay.
**malff** 08:25 So y'all… On the two things… I didn't prepare an agenda, but a few things to discuss, so there is this break on Maine.
And… another thing… So, we have two PRs related to Prometheus, and my understanding is that they are mutually exclusive.
Because they are basically to force a decision what we should or should not do.
Boom.
And, well, I don't know the probate use spec well enough to decide that, What is the popular wave here?
So I'm wondering if you have some knowledge in this area.
delete, maybe?
**lalitb** 09:20 Yeah, I'll have a look at both the piers.
I did see, in terms of implementation, but let me see why it has been reverted and what exactly was the behavior.
**malff** 09:31 Nope.
**lalitb** 09:31 Yeah.
**malff** 09:32 Yeah, see, because there was a revert already, so this thing is going back and forth, and .
**lalitb** 09:37 Yup.
**malff** 09:38 To me, it's unclear what we… what we need to do in the first place.
**lalitb** 09:42 Yep.
**malff** 09:44 And I think what this guy did is, basically prepare two PRs, for each solution, but we… We should not merge both, we should just pick one.
Oh… So, I was not here last week, but I saw that you did a lot of code reviews, so thanks for that.
This really unblocked things, because a lot of this was… There was some cleanup that was related to the Bazel build, with dependencies not being up-to-date and things like that, and doing the review on that really Unblocked a lot of changes, which have been merged since.
So, if you look at the closed PRs… Plc… Yeah, a lot of things have been bumped, all in the… in the basel area.
Improving things in general.
And that was… But was unlocked by this cleanup.
So, once… once that was approved, it just unlocked a lot of things.
**Tom Tan** 11:09 I'm wondering for such, like, version bump, or which part should we focus on, like, to review this?
Well, the…
**malff** 11:20 The version bump are just generated automatically by Renovate, but this assumes that it builds, and in our case, the… The dependencies are so, complicated that sometimes you need to upgrade many different things at once.
So that takes a manual, PR to just, update that.
**Tom Tan** 11:43 Yeah, I think we checked in our dependency version right into our repo, so…
**malff** 11:48 Yes, we are.
**Tom Tan** 11:53 Like, third parties.
**malff** 11:54 If you are in… if you are in this fire, yes.
**Tom Tan** 11:57 Oof.
Okay, I see.
**malff** 12:04 So, yeah, so this thing has changed a lot recently.
**Tom Tan** 12:08 That's cool.
**malff** 12:17 And also, I added some, In this big laundry list of things we need to do, I also added some sections related to the spec compliance itself.
**Tom Tan** 12:34 And for the version, like, a bump, like… How can we know if there's any incoming break and change? Like, I think a yearly update protobuf library could be risky right now, unless we… we know what we are expecting from the new version, or… I saw there's a…
**malff** 12:55 the renovate PR will do a build, so if there's a build failure or a test failure, we'll see…
**Tom Tan** 13:01 So we rely on the CI status to…
**malff** 13:04 Yeah.
**Tom Tan** 13:05 Sir.
**malff** 13:06 Yes.
**Tom Tan** 13:06 Okay, yeah.
**malff** 13:10 Yes, so… A while ago now, the spec component matrix has changed to YAML.
So, raised for… Instead of this huge file in Markdown, it's now a YAML file which is dedicated to C++.
And I took a look at it, and looked at all the parts which are still, Not covered, so sometimes a lot of them have just question marks, which means that we… in the spec, it's not even documented whether the feature is done or not.
Mostly because, the people changing that. It was a spec PR that just added an item, so… When an item is added, the person doing that in the spec report does not know the status of every implementation.
Which is where we have a question mark, and then it's up to us to actually change it.
And then there are a lot of things also where we still have things not implemented.
So this is the… from what I could tell, this is the list of things which are still not done in the spec itself.
So it's, I think we have some clear-up to do, because it's quite long, and it's very likely that a lot of things are, in fact, implemented, we just forgot to say it.
Oh.
But I think we should spend some time to… To fix the spec compliance metrics to… Document clearly where we are, so that we have a better picture.
And the second part, which I did also similar to that.
For the declarative configuration, there is also a YAML file.
which is in the configuration repo, that lists all the features that are supposed to be in YAML.
And, so, all the… all the features which are stable are implemented today.
And we… so we are, The configuration repo went to GA last week, so we are aligned with that. What is missing is all the things which are not stable, so every time something is not stable yet, it is named experiment or something.
And, you probably saw it, but there is already a PR from someone to actually fix those gaps.
So, I just find PRs for the missing part, and someone is actually implementing this one already.
So, I was pleasantly surprised, actually, to see some, Some people noticing and catching up on that.
Back to the question of, Seren and Bloomberg.
One question overall is, if we have certainly more people interested in the CPPR report.
to contribute to something. The big question is, for us to decide what we should, in which area we should focus on, so I'm looking for your input there to… to have some ideas of… What we need to do in general, so… Spec completeness is one thing, to file… fill the rules in this area.
But there can be others, like performance tuning, or code coverage, or things like that, I don't know.
Ritual… Do you have any general comment on that? Like, if we have certainly more contributors, what we should be working on?
**lalitb** 17:04 I'm not sure, like, if there are some contributors coming, is it something which would be affiliated to a given… to that company, like, if it's coming from Bloomberg or something.
Then probably they may be interested in prioritizing the things which probably their company needs first.
I mean, I'm not sure how it is going to…
**malff** 17:26 Franco?
being discussed.
Yeah, I've discussed that privately a bit with Severin. It was a bit unclear whether they have some specific goals, some specific things they want to do.
From what he told me, my understanding is that they… they just want to contribute to, OpenTelemetry CPP in… well, OpenTelemetry in general, so it's not only CPP.
They might be looking at, overseeing as well.
I think Java was mentioned, and maybe, something else also, I don't remember.
So they're looking to contribute to OpenTelemetry in general. I don't know… what for? Like, if it's, to implement a specific feature, or just to be… knowledgeable with the codebase and the… and the technology in general is so uneatering.
**Tom Tan** 18:23 Well, they'd like to consume our SDK into their… like, pertax, or they're doing that, or they will do that.
**malff** 18:31 I don't know if you're doing that already, I got that we are a C++ shop, so it's very likely that either they are already, or they will be.
But independently of that, I mean, the question still stands. If someone, like, a CS student or anyone this summer wants to do something in OpenTelemetry.
The question is if we can propose something interesting to do, so this is why I tried to expend, expand that list with more things.
Oh, this… This has been working not too bad, I would say, so far, because a lot of people noticed So… all those things were, advertised in that, that issue. So, all those things have been, have been picked up and done. So, overall.
people are finding it, finding interesting things are doing them, so I guess the… The more choice of projects we have there, the better, because then people can contribute, in an easier way, and we just saw that today, I mean… Two days ago, I did that, and we have a PR already for one item.
**lalitb** 19:58 Yeah, so in that case, Mark, I mean, we should Keep, keep adding more.
Things which probably we… we feel that something which… which… which are the gaps in the current implementation in this… Issue, and let them take it.
From here, right? Or you…
**malff** 20:16 Yes.
**lalitb** 20:16 To propose something to them that you take these other things.
**malff** 20:21 So, yeah, my question is, if you… If you know an area where we need to do something, to propose some topics.
Otherwise, the list of… one list of topics which is obvious is all the things missing from the spec.
**lalitb** 20:38 No.
**malff** 20:39 But it's, I mean, the spec is huge, so obviously, you need to know Prometheus to attend to do these parts, and you need to know… Tricing to do whatever, and things like that, so it's area, Bay Area, but…
**Tom Tan** 20:55 And how do we, like, add new items to the list, or, like, red?
I think I have one.
I think, one area is, like, for the metrics, that's the key performance, which that may be interesting, right? But right now, we… And then there's a… for our API, we have a log for our storage, which seems… The lock may be locked too broad, and could… Limit the performance from multiple threads.
And I checked it with the .NET SDK, which does a good job on them.
concurrent HashMap stuff, so on the recording side, the log is as minimal as possible, but for us, we… I think we… Currently, the lock in… could be improved.
Yeah. Well, so for things like this, I mean.
**malff** 21:49 I think we need an issue somewhere to capture the details.
And then, you can comment on this issue. I think some people have done that already, like… Yeah, something like this, like, okay, can you add this and that, and I will update the… the document on top.
**Tom Tan** 22:10 Yeah, sure, I can file an issue on this, and I'll append it here.
**malff** 22:17 Yes.
But for performance, ladies, a while ago, you were looking at implementing some… What was that?
**lalitb** 22:27 Yeah, yeah, I think I added.
And the benchmark.
**malff** 22:33 framework, yes.
**lalitb** 22:34 this would be useful, I mean, once, as Tom is saying, that if we are going to pro… at least we want to come up with some performance improvements which can be done by the people, then probably this would be helpful to really measure the gap and see if that's really… Helping.
**malff** 22:50 Yeah, see, yeah, see if it's going in the right direction or not, and also…
**lalitb** 22:54 Yeah, yeah.
**malff** 22:56 even ourselves, I mean, for… to… to test on different platforms, or to test different scenarios, and things like that, it's really helpful.
**lalitb** 23:04 Yeah, let me come back to this. I mean, I think probably we… I'll probably file… Try to find some time to release it, to make it complete.
**malff** 23:13 Yes.
**lalitb** 23:14 Yeah.
**malff** 23:28 What I've seen in general with new contributors is that, Sometimes, some guy's interested, Stays, like, one week or two weeks, does a PR, or comment on a few things, and then after that, we never see him again.
So it's.
**lalitb** 23:49 No.
**malff** 23:50 there are a lot of people, they just come and go, and once in a while, there's someone that comes out of nowhere and does a huge PR on something which was very… Complicated and that we absolutely need.
Like, recently, we had someone in Australia, I think, Who contributed the… The metric, reporting multiple metrics at once, multiple metrics, observing multiple instruments at once.
And that was some good change, for example.
**Tom Tan** 24:26 Like, for the summer and, like, intern stuff, maybe we can expect… Slight longer time a lot, maybe not just 1 or 2 weeks.
**malff** 24:39 I miss that, say that again?
**Tom Tan** 24:41 I mean, for the, like, if there's any… summer intern who is interested in our stuff, maybe. Hope that is more than one or two weeks.
Time on that.
**malff** 24:52 Then we can take a slightly larger work, I mean… Yes, in the summer, some students might have some better availability, maybe.
**Tom Tan** 25:04 Yeah.
**malff** 25:09 Yeah, so Trying to get, A list that we have… things that are identified that we need to do.
Which is ready for people to pick from.
I think that would, improve, contribution and, in, in general.
**Tom Tan** 25:38 Okay.
**malff** 25:56 Boom.
One thing also that was, what I added that was, discussed already.
with someone who also contributes. Lalit, you remember that we had all the boxes and documentation published elsewhere, like in Read the Docs?
**lalitb** 26:18 Oh, yeah.
**malff** 26:19 And this thing has been, basically running forever. I don't remember which one… which version is exported there, but it's, Far, far obsolete.
So, basically, the question is where… If we want to publish documentation again, where should we publish it? Do we keep trying to update that?
Or do we publish in GitHub, in Docision Pages somewhere? I don't even know how it works, but I'm assuming we can also host that somewhere in the… Maybe in the CPP report, or maybe in the… OpenTeametry, are you, or April?
**lalitb** 26:59 Yes, I think Severin did raise a PR. I mean, I probably have to… find out again, but he did some… raised some PR which brings all those documentation to Opentelementary.io, or somewhere, some… somewhere… Oh.
So, after that, I thought probably we should be doing that. Let me figure out, let me find out that PR. There was one PR from Severland, which did some changes to change the location of the API.
Documentation.
**malff** 27:34 Yeah, so if you, if you have some pointers, just please, please comment on this.
**lalitb** 27:42 Yeah.
I mean, if we really want to do deoxygen, then I think this is the right place, open delivery, I mean, the way we are doing it, read the talks.
Because that kind of, makes the deoxygen documentation much better, and publishes it there. But let me just revisit what Severin did.
**malff** 28:04 And probably then we can take it further here.
Yeah, thanks.
**lalitb** 28:10 Let's discuss it next, next week, I mean, let me, let me, let me just revisit you.
**malff** 28:28 So, apart from that, I don't have any specific items. I don't think I… Yeah, I didn't put anything on the agenda yet.
Do you have things you want to discuss?
**lalitb** 28:43 Not… not from my side.
Oof.
**Tom Tan** 28:46 I think from my side, I have one thing, it's about the new release. I think we got, as we get a regression for Windows RAM for them, Macs, macro, I mean, we… Maybe we could do our new release?
**malff** 29:01 Yes, we could.
**Tom Tan** 29:04 I think when was it? Maybe one month when we did the last release in February, maybe, also.
**malff** 29:10 Let me check…
**Tom Tan** 29:22 Most importantly…
**malff** 29:23 Doesn't see a date… Oh, God.
**Tom Tan** 29:29 Object commits, date was tail.
**malff** 29:46 Well, anyway, yes, we can… we can do an, A recent one.
Especially… We don't have… well, yeah, we have a few commits, a lot of them are, version bumps.
So…
**Tom Tan** 30:04 Yeah.
**malff** 30:04 automated things, like, But we also have, yes, there is the Windows fix.
And, in any case, some new things, like, yeah, new semantic conventions.
Things like that, so we can… we can do it in your ETS.
**Tom Tan** 30:21 Okay.
**malff** 30:22 Yeah, I can't… I can take care of that.
**Tom Tan** 30:25 Thanks.
That's awful on my side.
**malff** 30:29 Okay.
Yes, I will prepare an issue for that after the meeting.
**Tom Tan** 30:41 Sounds great.
**malff** 30:48 That's who, just… just a comment in general, I mean, There are a lot of things… Doug is also working on cleaning up, ceiling tidy, things like that. I'm also working on that.
For… For a lot of things which are, like, No priority, but still needs to be done, like some walling cleanup, for example, ceiling tidy cleanup.
I mean, to be efficient, it's important to have PRs making progress.
So, peacekeeping… Keep in mind, too.
look at PRs and do a review when you have time.
Because otherwise it's, it can get blocking if, If no one is looking at the PR itself.
**Tom Tan** 31:37 Sure.
I will try my best to review PR mark as ready for review.
**malff** 31:44 Yes, thanks.
**Tom Tan** 31:46 Thanks.
**lalitb** 31:49 Thank you.
**malff** 31:52 And, so… did… I did not talk to Duke recently, but Do you know how it is working at his new job, and if he's… if we'll have more time?
Nobody's settled.
Because he was away for a while, basically.
**lalitb** 32:10 No, I mean, I… the last I spoke with him was when we wanted… when we had interest of making him as a maintainer.
But, after that.
I think he just wanted to be in his job for some time and try to see how much involvement he can have, and then probably decide.
But yeah, I didn't talk after that.
**malff** 32:30 Okay.
**Tom Tan** 32:32 Yeah, same here.
**malff** 32:42 Well, it's nice to see he's back anyway, so…
**lalitb** 32:45 No.
**malff** 32:48 Okay, well, I don't have any… anything else.
Thanks for the discussion and the reviews in general.
**lalitb** 32:57 Sure, Mark, by any chance, are you going to this KubeCon in Europe? Just what… I just saw this announcement, so I'm just checking with you.
**malff** 33:04 No, I'm not going there.
Oh, okay. And I also misforth them as well, but…
**lalitb** 33:12 Okay. Yeah, some people from our, Microsoft, at least people who are working on OpenTelemetry are going there. I mean, they got their… At least some talks got approved.
in KubeCon, related to OpenTelemetry, so they are traveling for those talks.
**malff** 33:29 Oh, nice.
No, I was… I was wondering, whether or not to go to force them, but it didn't happen, and…
**lalitb** 33:43 Okay.
**malff** 33:44 And no, I'm not going to KubeCon.
**lalitb** 33:49 Okay.
**malff** 33:56 Alright.
But, it's getting leaked here, so we've, If there is nothing else to discuss, then we can close the call.
**lalitb** 34:06 Yeah, we can do that, yeah. Sure.
**malff** 34:08 Okay, thanks, thanks everyone.
**Tom Tan** 34:12 Talk to you later. Bye.
**malff** 34:13 That's good.
