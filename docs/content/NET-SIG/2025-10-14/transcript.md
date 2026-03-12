SIG: .NET SIG
Date: 2025-10-14
Duration: 17 minutes
Zoom Recording URL: https://zoom.us/rec/share/OF1L0bysdrMzJlTGSgQIwblZLiD50UtO9VgI1LGySFH58jqa93II6iZaTYhyU89c.aFF3u1esT2nwaKSg
============================================================

## Zoom Recording Transcript

**Rajkumar Rangaraj** 03:30 Hey, Hannah, I'm waiting for other folks to join, other approvers or maintainers to join, to… Oh.
start the session. If they don't… if we don't see them, if you have any topic, we can, I can help address those.
**Hannah** 03:47 Hi. Yeah, I was just joining, to see what it's like, because now I've made some contributions, and I don't have anything specifically, but… Maybe I'm waiting for some, Feedback from a few of my pull requests.
But, nothing specifically.
**Rajkumar Rangaraj** 04:14 Cool. Thanks, Anna. Thanks for your contribution, and also welcome to our repo. Like, we know there are a few, and you have been contributing since a while, I believe, and those PRs, we kept it internationally, because currently we are focusing on the the .NET tasks, so we want to merge those, and we will immediately jump on to all of the spending PRs in the coming days.
**Hannah** 04:41 Okay, yeah, no worries.
Thank you.
**Rajkumar Rangaraj** 04:47 Helen Rushant.
**Alan West** 04:51 Hey, how are you? Sorry to jump out late.
**Rajkumar Rangaraj** 05:01 Let me start.
So, are you able to see my screen?
Yeah?
**Alan West** 05:21 Yep.
**Rajkumar Rangaraj** 05:21 Yeah, cool. Then I think Pietro added this one, I believe, to add, as an… Martin as a maintainer in the contrib. I think, I merged the PR and I provided the maintainer permissions on the repo for him.
So, this is done, and done.
I have a small other topic, like, we did all the .NET 10-based merging, splitting up the target framework, and adding the .NET 10.
I think the .NET RC might… too, might get released today. We need to take the update and, do a… like, either a beta or an RC release, and take customers' feedback before we even make stable release along with, when the .NET gets released.
So the, I'll work with the other, like, Pyotr and Martin to see if we can do the release by end of this week.
Alan, any, from your past experience in the report, do you think, do we need to do any other… thing as a part of this one, like .NET 10 release, aligning with .NET 10 release.
**Alan West** 06:43 No, I don't think so.
I guess… My one piece of… Input may be that you know, choosing whether we do a beta or an RC, I'd probably lean for an RC, unless there's… unless there's recent features that I haven't been aware of that we feel would be better suited for a beta. Otherwise, I would lean for an RC. It'd be nice to just align with Aligned with the .NET release in that way.
**Rajkumar Rangaraj** 07:18 Okay. We just did the release last week, so we don't have any other thing pending, or with the .NET 10, there is, like, no big change, or the API like the previous version used to have it. I think we can align here with the RC version, in that case. Yeah.
**Alan West** 07:35 Sounds good.
**Rajkumar Rangaraj** 07:36 Yeah. I have another question for you, Ellen, here. So, I know you are driving the SQL instrumentation stabilization. Just want to understand, Where do we stand, or is it going to anywhere become stable sooner?
**Alan West** 07:55 Yeah, I… So… putting this into context a little bit, I have not had a lot of bandwidth to work on it, so I wouldn't really… I mean, I'm driving it still, but not really driving it, like, actively in the way that I'm like, doing the contributions. I met, face-to-face with… well, not face-to-face, but, like, synchronously with, Steve Gordon and Martin.
I don't know, some number of weeks back, maybe about a month ago or so.
And… brought them up to speed with where the instrumentation was at, and as you've seen, Steve has taken on some of the… some of the tasks.
He's… So far, mostly focused on, Working on the, sanitization.
A little bit more.
And besides that, I think that… I think that most of the small tasks are done, but until he gets a little more bandwidth to wrap that work up… It kinda depends on his schedule.
but again, I think we're close, it's just… it's just a bandwidth issue at this point.
**Rajkumar Rangaraj** 09:18 Got it.
**Alan West** 09:19 And last I heard from Steve was that he's gonna circle back to it soon, but he had gotten wrapped up in some other things, so he… let me just check Slack. When did he say that to me?
Yeah, I was going back and forth with… Dave, so last week.
Oh, no, this was actually 2 weeks ago that he said this. This was on October 2nd.
He said… It might be next week before I get back into this.
So, I haven't heard from him for a little over a week. I'll touch base with him, see… See what his, see what his plans are. But yeah, it's… it's primarily a bandwidth thing, so…
**Rajkumar Rangaraj** 10:11 Yeah, I was curious to know, like, to see, like, when we become stable, like, nothing, like, I mean, no.
Not waiting on that desperately, or something like that.
**Alan West** 10:22 Yeah.
Yeah, I mean, I'm… I'm looking forward to it. I'm excited to see that instrumentation go stable.
I think besides the task that Steve is working on, it's probably just about, like, squaring up the documentation.
and whatnot.
**Rajkumar Rangaraj** 10:43 Yep.
**Alan West** 10:43 Martin did a number of things, too, to kind of clean up some of the configuration and whatever, some of the… Remaining loose ends.
So, hopefully we'll have a… have an update in the next… A week or two.
**Rajkumar Rangaraj** 11:00 Yeah, it's good to have, like, we kept… we kept both the SQL and the ASP, classic ASP.NET instrumentation library.
It's good to have them marking it as stable. I know Pyotr is driving an effort of making the classic ASP.NET one the stable, So, I'll also follow up with Piotr, like, offline, because it's… this time won't work for him well.
So, I'll also check with him on that and see if… what's the status of it. Probably in the next SIG, I'll bring that as an update for everyone else.
**Alan West** 11:42 Yeah, sounds good. Yeah, that'd be a great… Great piece of instrumentation to get out there, too.
And then, I guess, just in that, I mean, since we're talking about instrumentation, I have not been… I… With the database instrumentation, I was actually attending, the database semantic conventions meeting that was going on.
And kind of keeping tabs on… Where it was at.
But there's a new group that started up just within the last few weeks for the GRPC, or I guess, more generally, the RPC conventions.
And… I've not been attending that meeting, but just, I guess, a heads up, that is also on the horizon.
And we, of course, have GRPC instrumentation, but we also have WCF instrumentation that probably would apply.
**Rajkumar Rangaraj** 12:48 Yeah.
**Alan West** 12:49 So… I might have some bandwidth sometime in the near future to just kind of get a sense for where that group is at, and maybe start to kind of see What our list of to-dos looks like, for… for our instrumentation, but, Anyways, I'm just saying that in case anybody else has bandwidth, that's a… that's something on the horizon.
**Rajkumar Rangaraj** 13:23 Yeah, so apart from all of this, there's a few OTLP, PRs that are pending in our repo, though even I have a limiter bandwidth, could not get to it. So, that's why, like, the priority at this point is we need to ensure that the SDK it supports the .NET 10, and there are no issues with it. That's what we are ensuring at this point. There are a few things here, like, the, there is a small issue, if then the headers, their value as in comma, we are not doing a great job. That fix is being proposed, and a ZZip compression, and that certificate, all of that. Probably, like, in the next few days, let me see if I can take a stab at one by one and see. A few of them touches the hot path also, so I want to ensure that it does not impact any path.
On this. And one of the PR also was blocked for the perfect reason in that one, so I want to pay very close attention when we take something in that area.
Because right now, it's designed in a way, like, it performs… it performs… it does not get… impact the performance at all. So, just want to ensure any changes that comes our way follows the same principle.
**Alan West** 14:50 Yeah, makes sense.
**Rajkumar Rangaraj** 14:54 That's all we had it, only the last week we had an issue with the release where we did not, with the latest CI changes, we just missed the… that, including the start to the, NuGet package, so we did fix that with the, mine, like, a patched version.
And that's all what happened, and nothing apart from that over here.
**Alan West** 15:23 Gotcha, cool. Yeah, that… I saw your note about that.
That seemed relatively minor, right? It just… it was just, like, it's the cert that's packaged in the… in the NuGet package or something?
**Rajkumar Rangaraj** 15:36 Yeah.
**Alan West** 15:36 Or the signature that is applied to the NuGet package, I mean.
**Rajkumar Rangaraj** 15:39 Our NuGet package includes two signature files. Both of them were missing.
So, as per the guidance, what is in our repo, we should be considering that as a security incident. That's why it marked this as a critical bug.
**Alan West** 15:57 Okay, okay.
**Rajkumar Rangaraj** 15:59 It says that that's a part of the digital signing, so we missed the digital signing part. So people cannot trust that Nuvigate package that we published.
**Alan West** 16:09 Yeah, okay, that makes sense. And so then the previous version, we delisted that or something?
**Rajkumar Rangaraj** 16:15 Yes.
**Alan West** 16:16 Gotcha.
Cool. Well, I mean, I guess it's fortunate that that was the only bump in it all, right? Because there was quite a few changes to the CI.
**Rajkumar Rangaraj** 16:26 Yeah, even last week, like, Blanche also warned before the release, something might break, there are many changes happened to it.
**Alan West** 16:37 Yeah. So we thought, everything went fine, and it took, like, a…
**Rajkumar Rangaraj** 16:42 Sometime Sean was doing an analysis to internally sign those libraries. That's when we figured out we are missing this one. If not, we could have even not got that at all.
**Alan West** 16:52 Gotcha.
Cool. Well, nice catch.
**Rajkumar Rangaraj** 16:58 Yeah.
I think that's all we have at… No other topics, I think we could end now.
**Alan West** 17:11 Alright.
Good to see y'all.
**Rajkumar Rangaraj** 17:13 Thanks, everyone.
**Hannah** 17:15 Thank you!
