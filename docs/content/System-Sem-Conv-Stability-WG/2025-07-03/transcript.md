SIG: System Sem Conv Stability WG
Date: 2025-07-03
Duration: 27 minutes
============================================================

## Zoom Recording Transcript

**Dmitrii Anoshin** 02:17 Hi folks.
**Roger Coll** 02:21 Thank you.
**Fraggle Rock (ca-wat-brt3)** 02:23 Chrysos. I thought you were on vacation already. No.
**Dmitrii Anoshin** 02:27 But generally.
**Christos Markou** 02:28 Next week is my last week.
**Dmitrii Anoshin** 02:31 So still, still around, enjoy.
**Christos Markou** 02:35 Thanks, thanks.
**Fraggle Rock (ca-wat-brt3)** 02:37 Pablo said. He'll be late, so I think we can get started.
**Dmitrii Anoshin** 02:40 Okay.
**Roger Coll** 02:44 Oh, good! Can I have the 1st topic?
Maybe it's not super related to the actual semantic conventions, but so it it deals with also the most probably with the host metric receiver.
And basically this came up because I was reviewing the actual metrics that we are using for memory in elastic in all our dashboards and comparing it basically with the ones that we are reporting in in the host metric receiver, at least for the let's say, for the used state and this metric, or this metric with that attribute.
Let's say that it's not an actual metric that the for in Linux that you have but a 1 that we derive from others.
and in the case of the host metric receiver, we drive it from the hook, Ops util, and the Ops utils, uses a formula that it's based on, the let's say, on the Free State, the catched one and the buffered one.
And this let's say that it was fine some years ago, and it was, let's say, the assumption that it was made to somehow tell how how much memory was left and and and could be used right.
But let's say that it was not. It's not accurate, and in that sense, the Linux kernel introduce a specific metric that it's the available memory that it's much more accurate here on on the link in computer, I think, I added, like a a few references of that.
And in, let's say, in which kernel version they added, etc, etc.
And let's say that the issue is that in gobs util this use. Calculation was based on the on the old formula that it was the the same user in many Linux tools like free top Ps.
But the thing is that once they realize that the memory level is much accurate, they change it. That formula in those tools to use available so derive it from the other the other one.
And let's say that actually, in elastic, we are using the available to derive the use metrics, but not in in whole the host metrics.
And if you test it out, there's an let's say, a noticeable difference. That's a 6% or 7% of of difference always.
And this morning I was just testing out. I can, I don't know later send you the gist or a small program that I was doing. And actually, if you let's say, rely on the current use metric of the host metric receiver. And you allocate that metric it will. Oh, and kill it. It's just it's let's say it's more memory than the the actual that you can use. And instead, if you rely on the available, it will just lie on the 99th or 99%.
So I think that, or probably what what I was proposing here in the cops util, or we can do it in already in the host metric receiver, because we have all the States is to change it to the more accurate one, and not sure. What do you? What do you think about this.
**Dmitrii Anoshin** 06:23 Roger. We have another metric for available right in host metrics. Receiver.
**Roger Coll** 06:28 Yeah, exactly. But it's yeah. Yeah. But it's, let's say, has a specific name. It's system dot memory dot linux dot available.
**Dmitrii Anoshin** 06:39 You want to use that value in the in derive usage from that value, instead.
**Roger Coll** 06:47 Yeah, correct. So instead of deriving it from 3 buffers and cuts, but it's also there at the moment used available.
**Dmitrii Anoshin** 06:58 In that case, we why would we need available then?
Separate Metric.
**Roger Coll** 07:07 Yeah, that's a solid point, probably underneath.
**Dmitrii Anoshin** 07:12 And in elastic you use available to calculate usage.
**Roger Coll** 07:18 Yeah, correct.
**Dmitrii Anoshin** 07:19 And you you mentioned that gops util changed something. I didn't get that that part. What did they change.
**Roger Coll** 07:25 No, so it's not changed at the moment. So maybe let me, I can share the screen. But so, okay, so this is the issue that I open in in gobs, utils in the used that we use in in the host metric receiver is based in this formula, but if you. Well, if you go through through it, it uses the free, the buffers, the catch, and actually the catch. It's not only the catch it, it assumes. It also adds up the reclineable. And this, let's say, if you go through the reasoning in cops utils, you will see that it. It was because they base it on the free Common Line tool in Linux that at that moment, let's say, it was also using the same, the same formula.
But in 2,022. Let's say, all those tools changed to let's the free, the top, whatever they change to use the available one because it's much more. Basically, it's much more accurate. And as we are already deriving from other states it gives more precision. No, no, nothing else.
**Dmitrii Anoshin** 08:50 Yeah, let's see what they what they reply to this one. But it kind of makes sense. We are aligned into the industry standards. Essentially, if we got.
**Fraggle Rock (ca-wat-brt3)** 09:01 Yeah, that mailing list thread actually does explain it pretty well that, like the the problem with that is that removing cached and and saying it's not used isn't really isn't accurate, because a lot of that cached memory is actually not usable. So it really should be included as part of the used calculation. That's sort of the the key, the key problem there.
So I definitely think if if go Ps util won't do it, we should.
**Roger Coll** 09:32 Thanks.
**Dmitrii Anoshin** 09:33 In that case we would remove, duplicate and remove available metric.
**Fraggle Rock (ca-wat-brt3)** 09:38 I don't know how we'd handle the the deprecation path, because we wouldn't literally deprecate the metric. We'd we'd we'd change what its value is calculated as, and I don't know how.
**Dmitrii Anoshin** 09:51 No, no, I'm talking about the additional available metric that we have.
**Fraggle Rock (ca-wat-brt3)** 09:56 Oh, the available metric. Yeah, I think we would. We would like.
I guess you could deprecate it.
because there, there probably wouldn't be much read like you could always derive that value back as long as we're doing the math the same way.
**Roger Coll** 10:12 Yeah.
**Dmitrii Anoshin** 10:12 That that metric was explicitly added, because we want to provide an option to use that available ex explicitly because it's a different value. And now.
if we align usage to that to that value kind of it doesn't make it useful anymore.
But anyway, we can, we can think about that separately. But yeah, I like, I don't have a strong opinion. But if industry like, especially as you mentioned, tooling was changed in 2,022 to use available. In that case it makes sense. Because I think we should. Collectors should always produce data that is like, let's say, kind of a standard that most of the tools provide other than just like relying on something that is considered old practice.
**Roger Coll** 11:07 Yeah, and and actually accurate, it's it's pretty simple to test this. But it's Just this morning I was using the let's say, the web studios, memory and just allocating, based on the basically on the available or the total minus use, that it's what we consider as as free at the moment.
and this gets Om killed. That wants it to finish allocating. And this one, it just goes to the to the top. So it's it's it's pretty much what I call it, so.
**Dmitrii Anoshin** 11:51 Probably you should past the past this gist somewhere in in the issues that you're posted.
**Roger Coll** 12:01 Yes, sir.
**Dmitrii Anoshin** 12:01 More consistent.
**Roger Coll** 12:06 Cool. Let's see if then it goes you till we get any reply there, and if not, I will also create. In issuing those metrics and and move from there.
**Fraggle Rock (ca-wat-brt3)** 12:17 Yeah, maybe our our simcom for the memory usage metric should also like say that this is the calculation you should use on Linux.
**Dmitrii Anoshin** 12:24 Right like.
**Fraggle Rock (ca-wat-brt3)** 12:25 Note.
**Dmitrii Anoshin** 12:26 Right. I believe it's a big enough change. We need to bring visibility to this change.
Not just decide within our circle, but bring visibility, and the best way to do it is going through semantic conventions, I guess.
**Roger Coll** 12:41 Yeah, probably. And actually, also what was suggesting. Inside, elastic was creating some open telemetry blocks around utilization metrics because it looks like, there's a lot of questions at the same of the same topic always, and something that we can reference in the end. And I just have some up-to-date information there at elastic. You also changed this new calculation at some point. Right?
Yeah. While a while ago in the yeah, yeah, in the let's say on the not, not in the open. Elementary agent.
**Dmitrii Anoshin** 13:17 Yeah, that's what I'm asking. Yeah, okay.
So you used to use the what we have currently in the collector before.
**Roger Coll** 13:26 Oh, we use so no, we use, let's say, the accurate one, the avail, the total available.
**Dmitrii Anoshin** 13:35 But it's something new that Linux kernel edit like. Not that long time ago.
**Roger Coll** 13:41 No, I think it's actually.
**Fraggle Rock (ca-wat-brt3)** 13:44 I think the the memory available States been available for a long time, but the the change to use that in in the common tooling is is relatively new.
**Dmitrii Anoshin** 13:51 Oh, okay.
**Roger Coll** 13:52 Yeah, yeah, it seems. Linux kernel 3 or 14 that it's maybe 10 years old already, or more.
**Christos Markou** 14:00 Maybe we could try to apply this change behind the feature gate. Similarly, to what we did for Cubet Stats Dimitri and probably advertise this with a blog post or something.
That could be another option. If we if we want to go straight through the collector instead of waiting.
**Dmitrii Anoshin** 14:23 Sounds good.
**Fraggle Rock (ca-wat-brt3)** 14:26 Yeah, I think probably if we make a Pr to semantic conventions, we make a feature gate change in collector based on that and and properly advertise why we do it and include a lot of that like the That Kernel Mailing List post is a pretty clear example of why we should do this, and why it's a good idea. So like including that stuff in the in the blog post would be a good idea.
**Roger Coll** 14:50 Oh, thank you. I'll just add this to the notes.
**Christos Markou** 14:58 I think. Then on next? So yeah. So yesterday there was a discussion in the collector gig about the plan that we have in general to move components to stable sematic conventions. And yeah, then I actually, I had forgotten that we had this long run discussion here for cost metrics receiver. So comments there. Thank thanks for summarizing the situation here. And just for reference. This came up in this other issue about which is about this Kubernetes specific metrics.
though these are already added. Th. These were added recently in cement conventions. And there was a suggestion to start like adopting them. But then I mentioned that we should do this altogether. Once we have stable cement conventions, and then, several folks like. So raised the question, how we're planning to do this actually within the collector, through one Pr or multiple prs, and then also Evan Evan Bradley raised that yesterday in the Sig.
So I think that right now this raises the question.
actually, this raises the fact that there are many unknowns that we need to tackle, and I guess it could make sense to probably start like thinking of those. And maybe Roger and myself, we are planning to like, internally, we're trying to allocate time for this working group. And these things could be something that we could prioritize from our side. So, but yeah, the the thing is that there are many unknowns here. So we would need to discuss those first.st yeah. So just raising this with you, I don't know how we could approaches.
**Dmitrii Anoshin** 17:13 Those allocatable metrics? Are they new, or we replace some existing metrics.
**Christos Markou** 17:20 We're replacing them, I think.
**Dmitrii Anoshin** 17:24 Okay, yeah, I would say that if it's something new that is added to the semantic conventions that is stabilized, we should just edit with no feature gate in that place. It's like, but if it's if we change something I I believe that should go through this migration process through the feature.
**Christos Markou** 17:41 Yeah, yeah, and we can, yeah.
**Dmitrii Anoshin** 17:43 Even start before behind the feature gate. When we have this like approach available, when we're sure how to do that, we would start that feature gating process earlier, even if not everything, is stabilized. But before switching feature gate to Beta, we need to ensure that all the semantic connections are stabilized.
**Christos Markou** 18:10 Yeah, yeah, I I totally agree. I also mentioned that here. If it is alpha, we can just use it like as a bucket and keep adding stuff there. My main question and concern is, yeah, what else is missing to start like doing this? And probably enter the or even I don't know if we should even consider like using weaver here. Yeah, I think that comes first.st
**Dmitrii Anoshin** 18:40 I'm not sure if we would need to. We were really, but we probably need some tooling in the Md. Agent to make it smooth and clear for for the users, because all, I believe, so far, all the approaches we had there. They have some pros and cons, and I'm not sure, if they provide clear visibility to the users, what what was changed was the difference between the 2 versions? That's probably the biggest priority we should have here, Braden, you may have some other input I maybe I'm missing something.
**Fraggle Rock (ca-wat-brt3)** 19:21 Yeah, the way I see it, we kind of have 3, 3 strat, 3 possible directions we could take with this. One of them is the one that I initially tried to push, which was having M. Data Gen. Produce 2 different packages, one being the original and one being the semcom version and and feature gate producing either one schema or the other the then other option was the one that you had brought up about like using conditions within one M. Data, Gen. File to produce different metrics or different attributes under different conditions, with feature gates.
And the 3rd option is to leverage weaver to generate collector code right now. It can generate, go code. But that's like, go metric SDK, stuff.
And so it would be. We would need to like make a new way for Weaver to generate collector code kind of like what M. Data Jen does. But that I think the if it were purely up to me like I would. I probably would stick to the the 2 package thing, and the reason I would do that is because then we'd have 2 very distinct files, one for the old and one for the new, rather than stuff being mixed together within one schema file. I feel like it's it would be easier to just compare the 2 in schemas independently than to try and like Suss out by looking at one yaml file.
which which stuff is going to be produced like the full. The full view of what's going to be produced.
**Dmitrii Anoshin** 20:57 Yeah, sorry I didn't want to interrupt you.
**Fraggle Rock (ca-wat-brt3)** 21:00 I. The downside is that there's a lot of code duplication. Yeah, it's it's it's quite a lot of code duplication. And it's generated code, but it's still. It looks a little bit ugly.
**Dmitrii Anoshin** 21:11 It's fine. It's generated code. So it's not a problem. I don't don't really worry about code duplication. What I worry is from the user perspective. How to understand what? What has changed?
If I look at 2 like, let's say Doc pages one for the all generated for the old semantic connection and the new. It's it's pretty hard to like. Understand? What's the difference? What's gonna change? So maybe if we go with the 1st option, maybe we can think about some extra tooling that would provide us some kind of a diff.
or at least we can maintain it like separately and manually.
**Christos Markou** 22:01 Yeah.
**Dmitrii Anoshin** 22:02 Maybe even like.
**Christos Markou** 22:03 Kind of yeah, sorry we kind of do it already, for Kate's metrics after Tyler suggested that.
So with whatever change that we introduce in Shaman conventions that diverges from the collector metrics. We try to maintain the diff here. Unfortunately, this is.
there's a manual thing. Yeah, I had the same concern how this could be automated. So probably that aligns with what you mentioned here. Yeah, that that could be an option as well.
**Dmitrii Anoshin** 22:40 If we keep. If we keep this same approach, if we just maintain that Doc separately.
we can just reference it. And it's fine. In that case we don't need to do anything, but we need to maintain it.
And I believe it's okay. And then we can have 2 separate packages. It's not a problem. We can even have some kind of helpers on top of that, like I don't know.
That would say, record CPU metric.
And that record CPU metric function would use either of 2 packages based on feature gate, or something like.
**Fraggle Rock (ca-wat-brt3)** 23:16 That's that's kind of what I was, what I was hoping like in my sort of like straw man hypothetical implementation. It was going to be essentially like.
make it so that the scrapers collect the collect all the like statistics that they need, and then at record time, based on whatever feature gate is on or off, or whatever logic you use for that produce one version of the metric or the other.
**Dmitrii Anoshin** 23:44 And that can maybe even be also generated. But it's not. It's not required like it, because it's it's not that hard to maintain. Yeah, I I think we're good. We can go with the 1st approach with this, and I believe that would be the quickest.
It's not. It's not. It's still significant work, but it's less unknowns and easier to proceed. I believe.
**Fraggle Rock (ca-wat-brt3)** 24:13 In that case the a lot of the work in Mdata Jen is done. There was a bug in my initial implementation that I had a Pr open for a long time ago. The fix. And then, once that once that's merged, then the M data gen, part of this is basically done.
**Dmitrii Anoshin** 24:27 Okay, if you have that Pr, and and with the with the bug fixed, please send it somewhere. It may be in the slack Channel system, semantic energy, slack channel, so we can review it and merge.
**Fraggle Rock (ca-wat-brt3)** 24:40 Sure I will. I think it might. It might have been closed in activity. So I'll go dig it up and reopen it.
**Dmitrii Anoshin** 24:46 Thank you.
**Christos Markou** 24:49 what about? Yeah, probably it's not a block here. But yeah, I think that would be nice to have a way to instead of like redefining everything in method that a yaml file to just somehow cross reference smart convention. I'm not sure.
**Dmitrii Anoshin** 25:14 That's what I was sorry. I think I.
**Christos Markou** 25:16 Go ahead!
**Dmitrii Anoshin** 25:16 Created the same issue some time ago. So.
**Christos Markou** 25:19 Oh, really, okay. Yeah, I'm not sure. I was going to say that I'm not sure. If it's feasible, or what changes that would require. But and probably it's not blocker. But it would be really nice to have this for the new. Let's say same, con metadata that we're going to have sort of like manually redefining everything. Or it will be quite messy, I think.
It's hard to maintain. Yeah, I can look for that issue that you mentioned, and probably yeah, either manage them or close one or another. Okay?
Yeah. So I guess. I think what I asked is mostly covered. Shall we wait? I assume we wait for Brighton to send this Pr. And then we can. Take this, a sync over this issue. Right?
Sounds sounds great. Okay? Thanks.
**Fraggle Rock (ca-wat-brt3)** 26:24 So, for my thing, I don't have much, much to say on this, because I just started, but I am finally writing the guidance for designing status metrics.
should hopefully be useful because it keeps on coming up for us of like metric designing a metric, for, like a thing is in a current state at a given time. And I think I think already there's some spots in in Kubernetes and in hardware that are already using the right design. So I'm essentially just like writing it down so that other places can follow along.
**Dmitrii Anoshin** 27:00 Sounds good. Thank you.
**Roger Coll** 27:01 Right.
**Christos Markou** 27:03 Thanks.
**Roger Coll** 27:03 Already some Kubernetes container status, metrics, right or something.
**Fraggle Rock (ca-wat-brt3)** 27:07 Yeah, I think there's like a status, and there's like phase or something like that, I forget. But they are using the right design already. I looked through.
**Roger Coll** 27:14 Okay. Cool.
Thank you.
**Christos Markou** 27:21 Okay, then see you next week then.
**Fraggle Rock (ca-wat-brt3)** 27:25 See you next week.
**Roger Coll** 27:26 Thank you.
