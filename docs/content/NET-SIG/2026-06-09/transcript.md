SIG: .NET SIG
Date: 2026-06-09
Duration: 29 minutes
============================================================

## Zoom Recording Transcript

**Rajkumar Rangaraj** 00:41 Hello, Martin.
**Martin Costello** 00:43 How's it going?
Can you hear me?
**Rajkumar Rangaraj** 00:58 Yeah, not only I could hear you, yeah.
**Martin Costello** 01:02 I wasn't sure if my microphone wasn't working.
**Rajkumar Rangaraj** 01:05 Oh, yeah, I had my, speakers on mute, just unmuted it. I did not know what… did you say something like me?
**Martin Costello** 01:12 But I just said hi.
Hey, Matt.
**Matthew Hensley / Grafana Labs** 01:19 Hello.
**Rajkumar Rangaraj** 01:27 Martin, just want to be… you… to be aware of, I'll send a note to all the approver and maintainer later, but I'll be on vacation starting June 20th, so I'll be… out till the first week of August, so I won't be joining the SIG during that time, or… you may expect very, or no zero to minimal activity in the repo from me during that time.
**Martin Costello** 01:54 Okay, no problem.
I hope you're going somewhere nice.
**Rajkumar Rangaraj** 02:07 Martin, would you be able to drive today, or…
**Martin Costello** 02:11 I feel?
**Rajkumar Rangaraj** 02:13 If you are not ready, I can take it. No, no issues.
**Martin Costello** 02:15 Yeah, I've got a whole ton of stuff running at the moment.
**Rajkumar Rangaraj** 02:18 Okay, cool. No reason, I'll, I'll take it.
Just one moment, I think we can get started.
Yeah.
In that mood.
I think we can… Martin, you have some topics, I think we can go in the order.
**Martin Costello** 02:58 Sure. So, the first one was that I was just wondering… If we wanted to plan… Doing a 1.16 release.
Because, There's a bunch of bug fixes, there's also some performance improvements, and there's also for the… an updated RC, or a new pre-release, rather, for all the Prometheus changes.
The main thing that made me think, oh, we should ship something, is I saw there was a… issue opened in the ASP.NET Core repo yesterday about a circular reference?
caused by… the… I forget what it was. Something updated the… App Insights SDK, And I remember you mentioned you'd had an issue in the App Insights SDK about circular references, which might have been related to the bug That we had to… roll back for the HTTB Client Factory.
thing, which has already been fixed, and then the first PR in this list that I haven't crossed through is the other fix.
that I linked to, because I think there was two different… Circular reference-related issues, and just one of them was more obvious.
When the other change went in, that's been… they've got reverted and has since been put back and fixed.
So I figured As that circuit reference bug seems to be cropping up in lots of places, we should probably ship a new release.
**Rajkumar Rangaraj** 04:32 I agree with you, Martin. I think this PR yesterday, I just reviewed and understood… I felt the same thing when I looked at this PR. Once we fixed that, we should do the release.
Pulled in Darek and Nova to just take a look at it. I think he ordered, addressed the feedback also. Today, I'll probably take a look right after the SIG, and we could get this merged. Yesterday itself, it was in a, like… I saw, even before the SIG, what the changes here have made.
I think we are in a good state there.
**Martin Costello** 05:09 Okay, cool, yeah, so other than, like, one of them's already been merged, so other than that, is there anything else that is important that we'd want, you know, 1.16 before, like, triggering the release?
**Rajkumar Rangaraj** 05:22 That is, like, if we look at… maybe we can go back, and after the agenda, we can go and take a look at all the PRs. I don't think there is anything that's very important that's waiting there, apart from this one.
**Martin Costello** 05:34 Okay, cool.
The next item is about the support policy.
Because I think there's some int… there's… some people comment… have commented on this issue since I posted it from… a different issue, I think it was. And also, Piotta put a message in Slack last week or the week before.
So I just thought I'd bring this up. We don't necessarily have to discuss it now, but it would be good to get some additional feedback on this, so we can at least give some indication of what we're gonna do.
To the people who are asking the questions?
Because I think the most recent comment on this issue I can understand why they would want us to support all the in-support .NET releases, but given we kind of shard by a minor version, it's not sustainable. It would be, like, we would have to backport security fixes to, like, 15 different minor versions, and that's just… not workable.
**Rajkumar Rangaraj** 06:46 I don't think we should be doing that unless and until, like, if it's some release like we do, add a… for example.NET 11 support we add, right? Which makes it difficult, people with cannot take that package at all, or something had been removed. That's when we can do it, because, I think this… we already have a principle well-defined here, because the support policy for this is also aligned with the support policy of the .NET lifecycle. If something goes out, we just remove it and say that, hey, this is where we stop.
And always it is recommended to take the latest version, if we go one level down and everything. I don't know in the… we know how the… frequently the softwares are getting released now, or things are getting patched with the help of AI and, all that. So, I think this is going to put us… more maintenance burden when we try to take care of that. So unless this has come back, and more of the customer come back and raise this as a concern, I don't think we should be creating anything apart from the latest only.
**Martin Costello** 08:02 So… I kind of agree, but, I think this issue's… the main motivation for this is actually to explicitly document it, because I couldn't find… Anywhere where it's written down.
that we do that, so I think we need, like.
something in… not saying stone, but something written down that we can point to, and then we can go from there, because I think the other thing that's created some… not confusion, but the people asking the loudest for this are actually people in Microsoft.
who… they're using older versions because they're using .NET 8 as the minimum dependency for .NET Framework.
And they don't want to take the changes.
To… they don't want to have to do the work to upgrade to 9 and then 10, and then… Because we had all those security releases the other month, that's now put them in an awkward position that they can't get the fixes because they don't want to upgrade to the version with the fixes in, which… Personally, I don't think that's really our problem, but I can see why it's creating the tension, which is why I think it's better to have it documented, so then we could just go to them, no, we won't backport it, you have to upgrade, that's your problem.
**Rajkumar Rangaraj** 09:24 Yeah, It's good to have the documented very strictly about what we plan to do, but in one odd scenario, we can be slightly flexible to help out the customers, if most of the people come and ask for it. We have done it in the past also, in this repo.
But we should not be, like, keeping that open and saying that, hey, we will… that this is the official process that we are going to do it. The moment we leave it open, It's going to increase the maintenance burden on us.
**Martin Costello** 09:59 I know, but I… what I'm saying is… If we just explicitly document We fix latest, and that's it.
**Rajkumar Rangaraj** 10:08 Yeah.
**Martin Costello** 10:08 But then that's fine, because I don't think that's explicitly written down anywhere.
**Rajkumar Rangaraj** 10:13 We will get that done as a part of this.
**Martin Costello** 10:15 I know.
**Rajkumar Rangaraj** 10:16 with this, with us. If you want me to just… Add a note here, my thoughts also, I'll just do… get that done after this, to this one.
**Martin Costello** 10:26 Okay, okay, yeah, that's fine, because yeah, I've just… for the sake of people who are going to read this discussion issue, that's why I've just put things we could do, but… My preference would be the top item, which is just what we already do, and if we had more flexibility, it would be to… and also patch one version previous, but… like, we have limited bandwidth as it is, and the most recent comment at the bottom is from someone saying, patch all the versions that support all the versions of .NET that are in support, and that's, like, 14 versions, and that's just ridiculous.
**Rajkumar Rangaraj** 11:08 So, I want to take a, like, some other, like, thought from yours, or I can check with Traska as well, as he does Java. Do you know any background how it's handled in other languages?
**Martin Costello** 11:21 I… I think the only one I've got a vague passing… knowledge of is, like, the way Node works, which is similar to how .NET does with their, like, the short-term and the long-term… I think they call them current and long-term, but alternate, they've got different support life cycles.
But also, I think there was another comment on this issue in Slack.
**Rajkumar Rangaraj** 11:46 Okay.
**Martin Costello** 11:47 Which was, like, someone was going, oh, but, Ubuntu, Canonical, they support .NET for longer than Microsoft does.
And you can get, like, paid support for, like, 15 years of support. And… I haven't replied to that comment, but my thoughts were, well, that's for Canonical to go above and beyond. Just because Canonical does it, doesn't mean we can.
Which I think is an extreme example to think that we need to support 15 years' worth of open telemetry.
**Rajkumar Rangaraj** 12:18 Yeah.
**Martin Costello** 12:19 Support when it has… the project's not even that old.
**Rajkumar Rangaraj** 12:22 Yeah.
And there is nothing that stops from, from them being forking for and getting the support for the unsupported version. So, Let me… let me write up my thoughts on this one, so in that way, it will be documented. Probably we should have this support policy in the document also, not only in the form of this issue, probably once we…
**Martin Costello** 12:45 Oh, sure, yeah. Sorry, yeah, if the… if… sorry if it was confusing. This issue… this issue is that we should document it. It isn't the document itself.
**Rajkumar Rangaraj** 12:55 Okay, cool.
**Matthew Hensley / Grafana Labs** 12:59 A real quick yes, if there was anything else that had the same issue.
It's like, not really. Most other runtimes have pretty clear lifecycle policies, and even, like.
Python and PHP that drag on forever have… accelerated things like modern .NET, I think we're getting these questions because there's a number of versions of .NET Framework that have no end of life.
at all, yet, like, it's somewhere 20, 40 or later, and so these are gonna keep coming up.
Definitely worth documenting, but I don't think these requests are gonna stop coming through, because those runtime versions are… not going anywhere, unlike, you know, Netcore 3.1 and Net6 are obviously out of scope at this point, but… What is it? .NET Framework 462 is… finally being dropped at the end of the year, I believe?
But for… Yeah, so I mean, but… and that only leaves, what, like, 3 or 4 other Net Framework versions that… Are gonna drag on, so… But it's kind of a unique problem here, besides, like, C.
that has really strong backwards guarantees, but as far as modern runtimes, the OTO support.
NET Framework is, definitely an outlier.
**Rajkumar Rangaraj** 14:31 Thanks for filling us in there.
I think Beatris left.
**Martin Costello** 14:49 Yeah, this one, I think… I can't remember if it was a DM to me, or if it was to all of us in Slack, but someone did the… hey, here's an issue suggesting a feature, and then immediately opened a PR implementing the feature with… there's not a draft, and… They're trying… they're adding… If this… essentially, if you parse the diff, it's a log enricher.
That logs unhandled exceptions at the process level.
And… I don't think we've got any precedent for having a login richer as a package in Contrib.
So I'm not sure how we would name it and organize it, and if we wanted to take it, but if we did want to take it.
They've called it an instrumentation, which it is not.
And I also don't know why they've just randomly picked some, cod owners who aren't them.
**Rajkumar Rangaraj** 15:48 Yeah, the reason is I'm seeing Sean as a co-owner here. Sean has nothing to do here, as far as I know. So…
**Martin Costello** 15:57 It's possible… it's possible they took the guidance to look at an old PR and copy it to get started? Too literally?
But, they opened a design discussion, and they just immediately opened the PR, and they just keep updating the branch.
Every time he goes in.
**Rajkumar Rangaraj** 16:18 I did not pay attention to this, like, so I have a few items. One is the PR… Second is the ratio there. This one also.
I think, if, if everyone in this call could also take a look at this and share your thoughts, it would be helpful to see if we need this feature, or if there is a customer… if only one customer needs it, we should not be entertaining that. They could rather have something, some implementation at locally. If we feel it's going to benefit a majority of the community, then we can.
Consider getting this one.
**Martin Costello** 17:03 My initial assessment is it's a case of something that's quite simple, and they're just trying to push it into a package to avoid copy-paste, rather than it being, like, a difficult problem.
That you want to solve in one place, or… Like, an innovative, new feature that would get wide adoption.
**Rajkumar Rangaraj** 17:27 Got it.
**Martin Costello** 17:28 But I didn't want to just, like, sort of comment on it immediately and, like, poo-poo the idea.
**Rajkumar Rangaraj** 17:33 Sure. So, I have some bandwidth today to take a look at all these things, so I'll also spend some time on this as well.
I think Julius is in another topic, like.
**Julius Koval** 17:54 Yeah, hi, it's the BR… yeah, it's this one.
**Rajkumar Rangaraj** 17:59 Yep.
**Julius Koval** 17:59 So I saw they responded to it. You mentioned some typed N-value API, so I was wondering what you meant by that.
**Rajkumar Rangaraj** 18:08 So, I did take a look at this yesterday, and I figured out that what we are trying to handle is also, in the… we have a NE value.
What I was trying to say is, if it is, mmm… So, even before we get into this, right, why are you doing this, Julius? You saw an issue, that's why you are trying to address it, or if there is really a critical need that it's in your project that you want to get this done.
**Julius Koval** 18:43 So it wasn't a critical need, just… Frankly, it seemed like an interesting thing to do. I don't have a deep reason for it.
**Rajkumar Rangaraj** 18:55 So, the implementation here in this, if you go back to the previous, PRs when we merged during the OTLP serialization and all, we… we just decided to park these things, not going through the key value list, especially to, loop in through that, because we want to avoid unnecessary, like, implications in the, OTLP exporter.
That was the idea to keep it, unless, if there is a very strong ask from the customer saying that, hey, really, we need this, this is acting as a blocker, that's when we decided to do this. There are several… apart from that, there are other reasons also.
there is any value in the spec, right? So, still.NET does not handle that very clearly, like, this is not only specific to the SDK, but also, we were in the talks with the .NET runtime team to see if they could help us somewhere in that.
With all of these conversations in picture, that's when this… this work Had been put on hold earlier.
To give you a slight background. So, I don't know, like, the current shape is good, or should we go ahead and do this? Probably, if someone is getting benefited out of it, I would invest the complete thing, and we can go with this one, but I don't think… it's going to benefit customers. So, unless we have that, like, part with us, how it's going to benefit customer, I don't think we should be pursuing in this one.
**Julius Koval** 20:40 Well, there was a guy asking for this, actually.
**Rajkumar Rangaraj** 20:43 Yeah, do we know why, and it cannot be done through this one? Yeah, I know one customer, we had an issue and all.
unless there is a customer, like, few, at least few customers saying that this is… but at least in my experience, I work in… day in, day out with customers, mostly with the OTLP only in the… nowadays, I haven't seen that anyone racing this one.
That's why, like, Martin, did you, Or, Matthew, you, any of you, like, heard this as a blocker in Grafana, like, anyone reported this one, this is a much-needed one.
**Martin Costello** 21:29 I haven't seen anything.
**Rajkumar Rangaraj** 21:31 Yeah. So, considering that, Julius, unless if there is a major ask, I don't think we should take this. The idea is not to have everything to put in the exporter and make it a heavyweight thing.
So we want to keep it confined and ensure that it is written in a perfect, efficient way. Even in a very critical workload, like container workload and everything, it works without any issues.
Those are the reasons, and when… and especially as I shared a background, this has few background to it, like, one is the perf, and another is the any value sorting things out.
I don't think we have sorted out that any value situation A. Probably we should do that, and then come back and revisit this one.
**Julius Koval** 22:16 And so… I mean, by… Well, like, is there a plan to introduce any value to .NET itself?
**Rajkumar Rangaraj** 22:29 Yeah, that was the talk that happened, like, since, like, the last few months have been slightly dissociated with the conversation with the .NET team. I need to go and pick back and see, based on this issue, if, where do we stand on that.
Earlier, Lunmilla was driving that with the .NET team, and And I don't know how and where it ended and everything.
**Julius Koval** 22:57 Sure, okay. Well, regarding perf, I feel like this would have a negligible impact on people who aren't actually… Using, you know, some kind of key-value lists already.
**Rajkumar Rangaraj** 23:10 Yep.
**Martin Costello** 23:15 I think there's something that can be measured.
Like, we have the benchmarks for it, or we can… or you can write some new ones, if the current ones don't cover it, to sort of…
**Rajkumar Rangaraj** 23:27 Yeah, that's also a right thing, like, Martin, you can… good suggestion Martin has given. You can… Julius, if you want us to consider this one, you can do a proper benchmark to let us know, like, if the list size is this one, what's the As the list size goes, how is the performance impact is going to happen with the help of benchmark? If we understand that, we can even accept this PR with that data, too.
**Julius Koval** 23:56 Sure, just what I meant was that if somebody isn't using key-value lists in attributes, then it wouldn't really have an impact, but…
**Martin Costello** 24:04 Oh, sure, I understood that, but… You…
**Julius Koval** 24:08 We were…
**Martin Costello** 24:08 I'd rather it be proved with a benchmark.
**Julius Koval** 24:11 Sure, sweet, sure. Okay.
**Martin Costello** 24:16 Just curious, Julius, because there isn't one linked on the tissue, was there a specific issue in the backlog that said that we didn't have this and we should add it, or did you just find that it wasn't implemented?
**Julius Koval** 24:30 I just found that it wasn't implemented.
**Martin Costello** 24:32 Okay, I was ju- I was just asking because… sometime in the 6 months, in the last 6 months, someone else opened a PR to do exactly the same thing.
**Julius Koval** 24:42 Oh, my…
**Martin Costello** 24:43 And then… they didn't interact with it, and it just got closed. So I was just wondering if there was an issue And we're having this discussion about maybe not taking the change. We should make sure that issue isn't, like, marked up for grabs or anything like that.
Because we wouldn't want… if we don't take this change, we wouldn't want different people constantly trying to implement it.
**Rajkumar Rangaraj** 25:11 Julius, definitely you will find some information if you go through the history, through the searching, you'll see some information related to this in the repo.
**Julius Koval** 25:20 Okay, sure.
And in terms of In terms of the benchmark, like, do you want to measure the performance of specifically the serialization?
**Rajkumar Rangaraj** 25:35 Yeah, serialization of… if the… The first thing is, like, I know we can accept the benchmark and everything, but just, I would… ask you to go through the historical data, why we shouldn't be doing this one, and what's the right way to do it. Just try and figure that information out here, or I can dig in and get the reference to that for you.
That should be the first step, but if you are doing this realization, if someone is having a list, how… With the current one, and with the list being considered, how is there… performance impacted, how is the allocation, and what's the time, or CPU time that it's going to take, is something we need to understand.
And with the list size also.
variable with slices.
**Julius Koval** 26:28 Yeah, sure.
Okay.
**Rajkumar Rangaraj** 26:34 Any other, like, agenda topics here? Nothing.
Okay, let me go through the PR. Like, Martin, I think we can now use the time, see if any other PR needs to be included in the.
**Martin Costello** 26:58 Yeah, there was nothing that immediately stood out to me, but as an open… and also both of these items I put on the list were mine, I figured… I figured I would open the question in case there were other things that others thought important.
**Rajkumar Rangaraj** 27:13 No, yesterday, yesterday I went through all of the PRs over here. I don't think there is any other thing that's pending apart from that review priority label one.
**Martin Costello** 27:24 Okay, cool. Yeah, I just thought I'd mention it in case there was anything that anyone particularly wanted, even if it wasn't important.
Because it sort of missed the boat, as it were.
**Rajkumar Rangaraj** 27:37 Yeah.
Yeah, I don't think we have one. I think we could keep it simple. Once this PR gets merged, we will start working on the release.
I think, do we have anything else? Like, let's take a look at the issues to see if they're… This is by Piotr, and this is 3 weeks ago. It's fine, I think, then.
I think that's all we have it for today.
If there is nothing else, I think we could end now.
**Martin Costello** 28:25 Oh, actually, Raj, before you go, there's been a couple of PRs today. I opened my… a Microsoft person, for Geneva.
So.
**Rajkumar Rangaraj** 28:36 Remember, clearing or closing off a study most of it?
**Martin Costello** 28:41 I know there's, like, 2 brand new ones today.
**Rajkumar Rangaraj** 28:44 Okay.
**Martin Costello** 28:46 So, not now, but, they'd be good for you to look at before you go away. Sure.
**Rajkumar Rangaraj** 28:52 Sure, so if you see, Sean is on this, SIG as well, so he's going to slightly be active in these repos and, helping with the reviews with the both the SDKs and the contrary repos. Not only specific to Geneva, but in general, in both the places.
I'll, I'll leave it.
**Martin Costello** 29:12 Cool.
**Rajkumar Rangaraj** 29:12 Take a look at this much.
Cool, I think that's all then. Thanks, everyone.
**Martin Costello** 29:27 See you next time.
**Julius Koval** 29:28 Thanks, bye.
