SIG: Collector SIG
Date: 2025-09-03
Duration: 57 minutes
Zoom Recording URL: https://zoom.us/rec/share/sEr4ThggOk42l6y1tt6sgj3l9HNntOfTK2gjTzavdXaX4aQeocgqNWKQbR1xhUU.Q51R67xzZZLT5v_1
============================================================

## Zoom Recording Transcript

**Pablo Baeyens** 02:32 Hey.
**Evan Bradley** 02:38 Hi, everybody.
**Andrzej Stencel** 02:42 Hello.
Looks like we have a packed agenda.
Pablo, do you want to start?
**Pablo Baeyens** 03:57 Yeah, sure. So, yeah, I wanted to talk about the release that 0.134.0 released.
First to see if there's any immediate things we should do. I think some of the automation regarding nightly releases.
Misbehaved, so we probably need to…
to fix that, and then, yeah, I think the auto-schedule release took a few people by…
surprise. The other scheduled minor release took a few people by surprise. I had a proposal for that.
There's a ER… Link there…
Which, yeah, I would also like to discuss and understand what people think.
So… yeah, I don't know. I don't know if the release is finished, 0.1.34.
I don't know, Pogdan, are you still working on…
**Bogdan Drutu** 05:04 Yeah, I asked you guys what you want me to do. I propose two options, and I need your input on what do you think we should do between the two.
**Pablo Baeyens** 05:16 Where are those two options?
**Bogdan Drutu** 05:20 In this stack.
**Pablo Baeyens** 05:38 Sorry, this is… Taken a bit too… Load.
For me, if you want to, like, describe the options right now.
**Bogdan Drutu** 05:46 Yeah, so… So, first of all, the problem happened
when I… let's discuss about the problem, not minor versus patch release, that's… that's a.
**Pablo Baeyens** 05:57 Sure, yeah, we can… we can keep that coordinator.
**Bogdan Drutu** 05:59 So the problem happens the following. At 2PM, I merged the upgrade PR. Then I had a lot of meetings and everything, so I couldn't put any tag or anything. And at 7, the nightly build came and put a tag on that PR.
Before I was able to put my tag, because I was having work to do.
Okay? So the nightly started to do a lot of work, blah blah blah blah blah. I did not check that the nightly was there.
And then, I came… I did a small mistake, but that doesn't affect that. So, there was a tag on the main commit that I wanted to release. So, when I put a tag on that commit.
Now, the automation… one of the automation reads the other tag, not my tag, as the current tag on that PR. So…
Yeah, so… so… that's the problem, and then I had… I propose the fix, I merged the fix in the automation, because there is only one place where we don't use the…
a reference that triggered this action, we use the… we read the current tag from the commit. I fixed that, now we use the reference, so now it should work. The problem is, this fix is after the tag, so I cannot rerun the automation with this fix.
So my problem right now is I don't know what to do besides either I move the tag.
to the new thing, 134.
But that's the problem, is there are a couple of artifacts already released with that, so it will create a bit of a mess for that. So, the proposal is to add 0.341 on the fixed tag, fixed commit, the commit with the fix, so that we'll release the right things. So that's… that's where we are, and that's why it happened.
And I explain in the… in the… so you can see the issue, the PR that I…
merging the release, I had the explanation there with the… with the steps or minutes when… when things happen.
**Pablo Baeyens** 08:15 So, we do reserve the rights to move DACs if we wanted to, I'm…
Fine with either, to be honest, personally.
**Bogdan Drutu** 08:27 So the problem… the problem, Pablo… Pablo, sorry, not Paolo, Pablo, the problem is…
we already released two… two things with 0.134, and if we move the tag, we re-release those, and that is the problem that I…
**Pablo Baeyens** 08:41 Oh, right, because we released the supervisor on the builder, right? Yes. Okay.
Then, yeah, 030… 134.1 makes more sense, I guess.
**Bogdan Drutu** 08:51 Correct.
Okay, so I will go ahead and do that. I was waiting for you guys to tell me if you are okay with that. That's why I… I waited for you. And that's why I didn't do it. So…
That's… that's all what we need to do.
Here.
**Pablo Baeyens** 09:09 Okay.
Okay, and then one thing that maybe we should change in the process is that we need to make the night lease sort of resistant to…
A low period of time between tagging and, PR and untugging, right?
**Bogdan Drutu** 09:29 It's not the nightly, it's the release that is broken, but I fixed it. So the nightly was happily working.
But it just made the fact that it added first the tag, the release read that nightly tag instead of reading my tag.
**Pablo Baeyens** 09:46 Oh, okay, so it's not the…
Yeah, okay, I understand that now. And is that fixed, then?
**Bogdan Drutu** 09:52 Yeah, yeah, read the, read the issue, read the PR, I linked here the PR with the explanation of things, and…
**Pablo Baeyens** 09:58 1158. Okay. Yes. I'll break that. Okay, so that's…
That's fixed now. So that explains the releases… Din… Yeah, Antoine?
**Antoine Toulme** 10:16 So, we've had this before, right, where we would have a successful core release, contribute release, and then the releases repository fails. This was my experience last time, and I had to do 4 patch releases.
Sweet by Sweeties, and I gave up.
Actually, someone else did the fourth one. The fifth one, even, to get where we needed to be. And I have no problem, if we want to do .1 for this, then let's just do another patch release on top. It's okay, right?
And it doesn't have to be bogged on, by the way, it could be, just let's have someone do it, right? And…
Thanks for the fix.
**Bogdan Drutu** 11:00 Okay.
Last one, by the way, Pablo, if you want to discuss anything with me, I'm… I have to leave at 9.30, so if… if I need.
**Pablo Baeyens** 11:08 Okay, yeah, I guess I'm interested in hearing your take about the, like.
not making minor releases outside the scheduled PR, so… I mean…
Share that again on the Zoom chat.
I… you asked for the reasons I posted a comment there.
**Bogdan Drutu** 11:26 Yeah, for me, for me, for me, the biggest problem is why it's so important to respect this schedule if we have a problem, or if we need something to do, why is so…
**Pablo Baeyens** 11:40 We have an alternative solution?
Which is the bug fix releases, and there's some benefits for all the schedule.
**Bogdan Drutu** 11:47 Yeah, again… what I did… so…
let's separate the two discussions. Why I did that? I did it because it was easier to do a minor release than a patch release. So, a patch release, it was harder for me, I couldn't cherry-pick easily the whole thing, I should have done a lot of changes, so I said, okay, easier, it's Friday evening, let me do it just so that customer can benefit.
Nope.
Is that the right thing or not? We can discuss about that. But…
Now, just for having or not having
minor releases out of schedule, I don't know if that's so important. As long as we keep a cadence of every two weeks, if we have one in between, I don't think it's a problem, but if you guys believe that this is the end of the world, because that's how it seemed to me from your comments.
I'm like, sure, let's not do it, but I got, like, a lot of questions and everything for something doing in a Friday evening, like, I don't know. For me, it's… it's a bit of…
we all know this is open source, we are not paid for this, a lot of the… us, and I'm not sure I understand this thing…
**Pablo Baeyens** 12:59 So I'll let Antoine speak first on…
**Antoine Toulme** 13:01 I'd say, first, Bogdan did this release by himself, I approved it, right? So, I will take also responsibility for making this release happen.
I would say that I'm very supportive of having more releases, more often, all the time, because we want to make things available to people, so I actually am okay with making releases as needed based on needs, and I think this is good, right?
I would say that it could have been a patch release, sure. It was, like, a lot of changes as well, so I didn't think twice about it at the time. I was also on my way out, and I had only a few hours to review, so I appreciate that Bogdan also kind of made that happen quickly, and
It's always challenging to make a release on a Friday anyway, so maybe that's also a learning for us as humans, is that, you know, making releases on Friday is the stressful situation, we should avoid that for ourselves.
I, I think, so, making a minor versus patch release and messing with the schedule
maybe not as much of a big deal. We can definitely recover from that. The community expectations should be that we release at most every two weeks, and maybe we can set some more flexible guidelines around that.
The only thing I would ha- I would say is that
the minor releases right now also kind of rhythm… have a rhythm related to deprecations and additions of new things. So, for example, to move from beta to stable, you're supposed to wait two minor releases before you make a call.
So if we start to gamble a little bit and we make two minor releases in one week, well, then that's a problem. So that's actually a valid thing that we need to address in some sense, but maybe we can decorate that from
We can just say, okay, is it two minor disease or a month, right? Whichever comes first, or whatever you want.
But besides that, I think it's great to have more releases, and actually exercising main as if we were going to make a release every single hour is always a good idea, because that proves that our stuff is ready to release at any point.
So…
**Pablo Baeyens** 15:09 Right. So, okay, I want to reply, and there's a lot of things. One of them, which I agree with, is the Fridays thing. I think, yeah, probably, like.
not making a release on Fridays is probably, like, less stressful for everybody, and we can… we can take a less than I…
I think that that makes sense. Then, I feel like not everybody feels the way, you do about, releases, myself included. I laid out the reasons why I…
would like to have a predictable release schedule. I'm completely fine with bug fix releases whenever, we need to do them.
Making them easier seems like a…
important thing to do based on this. But, you know, I want to clarify the expectations, because there's…
Myself included, and other people that feel like
Yeah, I mean, a predictable release schedule has more benefits than drawbacks.
And we do… that's kind of the status quo, we haven't documented it
too well, but I would say, like, we should follow the status quo until we make a decision on this.
on, shot.
**Jade Guiton** 16:24 Yes, to respond to the point that we want to exercise the release process as much as possible, that's definitely the case, and that's what the nightly releases are for. So, if the nightly releases
Are fundamentally different.
from the real releases, in a way where the real release might break, but not the nightly release, then we have to fix that. It means they're not properly exercising the release process.
And that without, causing…
Additional issues with coordination, or understanding the schedule.
Hogan.
**Pablo Baeyens** 17:04 program?
**Bogdan Drutu** 17:06 Yeah, for me, for me, I was reading, the arguments that
when, for example, people have predicted versions. If it's a bug… if it's a patch release or a minor release, people have to upgrade anyway. If we have to do a… in-the-middle patch release.
you as a vendor, or you as a final user, will have to do that weekly upgrade. You cannot wait if there is a bug that we… we were forced to do a new release. It doesn't matter for me if it's minor or patch, I have to upgrade it, because I have a bug, correct? Like, there is no…
**Pablo Baeyens** 17:47 I mean, no, because the difference is the amount… the set of features that are in a minor release is different from the ones in a bugfix release. There's no new features, there's no new deprecations on a backfix release.
There are no new features, it's easier, but I still have to do a new release.
**Bogdan Drutu** 18:06 Correct? Like.
If there is a bug in my code that runs, I still have to do a new release.
It may be easier, but I still have to do all the work to release.
**Pablo Baeyens** 18:22 Sure, I don't understand how that relates to the…
to the arguments I was making on that comment.
**Bogdan Drutu** 18:29 like the first one, the component owners can provide roughly timelines versions when things will be available. I mean.
You have to make available patch releases anyway.
**Pablo Baeyens** 18:43 Right, but if I'm developing a new feature, and I say, like, it will be available on 0.134, like, it causes less confusion if I know when 0.134 is going to be released, and there's… that there's not going to be a 0.134, like, before schedule.
That's…
**Bogdan Drutu** 19:00 And you think we are so mature and so well-funded that we can… we care about that more than
When people can do the work and benefit of that.
**Pablo Baeyens** 19:13 I think we should aim to be that mature, yeah. And, I think we have the alternative, which is bug fix releases, so, we can… we can do it. If we didn't have bug fix releases as an option, then…
**Bogdan Drutu** 19:27 But we have, but who is willing to put the more work?
Are we having enough resources to put on more work that is needed everywhere?
**Jade Guiton** 19:37 I think a big part of the problem here is not really… is just that the patch releases are hard to do. That seems to be the core issue here. If they were as easy to do as a regular release, I don't think we would be having that debate.
**Pablo Baeyens** 19:57 Okay, so, like… then… well, I'll let Andrei talk first, and then I can…
**Andrzej Stencel** 20:04 So, I commented on this, and I proved this PR from Pablo previously, because I thought it's good for users. This predictability is good. But now, Antoine got me thinking, but maybe if we drop this predictability thing, Collector is still…
0, version zero anyway, right? So maybe we could, rethink it and
remove this every two-week cadence, and just say that release… as I said, maybe at most at every two weeks, but maybe as…
And when people are not
when people stop expecting the bi-weekly cadence, that might not be a problem that we're not sticking to it. The biggest problem for me is when we say that we release every two weeks, and then we don't. But…
I think it could be a good idea to rethink whether we actually want to stick.
**Pablo Baeyens** 21:07 So,
I want to ask the question of if we were able to make bug fix releasing easier, then…
Would people, that are… Against my proposal being in favor of it? Or is that not enough?
**Andrzej Stencel** 21:27 bug fixes… bug fix releases will be harder, because you need to, like, do it from a branch and, pick whatever you need to pick for that bug release.
**Pablo Baeyens** 21:39 I've done the yards.
I guess.
I…
**Andrzej Stencel** 21:42 Well, that was… Baghdad?
**Bogdan Drutu** 21:46 No, I wonder if you finish, I don't want to interrupt, that's why I was waiting.
Okay. Yeah, so I think I would do, probably, patch release, but also, on this productivity thing, I still fail to understand, because your things, if you merge things
on top of 133, your things will be 1.34. Does it matter if it's Monday, July 1st, versus Monday, June…
23rd. For me, it doesn't matter that much. So I have the predictability in which version it will be.
I don't have that exact date that…
is when this will be available. I don't care that much, but again, it's my personal opinion, and I'm…
I'm gonna stick with that personal part of it, but if others tells me that this is so critical for them, that it's exactly that date, and that's why we have 20 people, 30 people here debate about this, I'm fine, like, but…
It's not as big of a deal for me. So, if you really want to go with patch releases, let's go with that, but I'm not gonna be willing to do them if it's the amount of work I have to do today.
With the amount of work I have to do today, I'm not going to be willing to do it.
I'm not paid for this work, I'm working on a company that we are just using this.
Today, so definitely my company doesn't pay me for working on this.
**Pablo Baeyens** 23:19 My company definitely doesn't pay me also for fixing the bug fix release procedure, but we are both maintainers, and we should both strive to improve the project, and this is part of improving the project.
**Bogdan Drutu** 23:31 Okay, I do agree that.
I do agree with that, Pablo, but also, I think there is a list of priorities, and this is the least… based on my judgment, this is a least priority compared with fixing other problems in the project.
**Pablo Baeyens** 23:47 You can unblock the PR then, and the rest of the people that are interested in it can't discuss it, but I think it's legit that I bring this up. And I agree, like, we've spent, maybe too much time on this, so I'll let Shad speak, and we can move on to the next topic and continue the conversation on the PR.
**Jade Guiton** 24:05 Yeah, I mean, it's mostly redundant with what's said on the PR as well, but
People have been discussing in this meeting a lot of
Does it matter if customers know exactly when a feature is released? Maybe not. Maybe we can… they can get used to it not knowing exactly when it happens, but…
for developers that need to coordinate changes across different repos, I think that use case is a bit more… is a bit clearer, because if you make a change in Core Collector that requires changes in Contrib.
Not knowing when Core or Contrib will, be released can be a problem.
**Bogdan Drutu** 24:45 But… We did a full release.
So, so I'm not suggesting that we should do them independently, I'm just saying…
We can do it at any moment, the full thing.
**Jade Guiton** 24:59 Yes, but what I'm saying is that if you've made a change in core, but you haven't done the change in… the corresponding change in contribib yet.
Not knowing by when you have to make the change in contribib, To have everything match.
Can be a bit of a… a bit of a problem.
Again, it's maybe not the biggest deal, but… the… having…
A periodic schedule probably helps with that.
**Pablo Baeyens** 25:26 Alright, just one more…
**Jade Guiton** 25:29 Yeah, it's an argument that's being brought up on the PR anyway, so…
That's not a number I want to rehash it further here.
**Pablo Baeyens** 25:34 Sorry to cut you off, I just… there's a lot of topics. So, yeah, let's continue on the PR, and yeah, thank you for the comments. So, Andres…
**Jade Guiton** 25:53 They don't seem to be here.
**Pablo Baeyens** 25:58 Right.
Oh…
Right. I guess…
if somebody's interested in sponsoring that component, please take a look, and I will comment on the issue that
Would be helpful for them to join and explain what it does.
So… Yatten…
**Yaten Dhingra** 26:33 Yeah, Emil.
**Pablo Baeyens** 26:40 Yep, we can hear you.
**Yaten Dhingra** 26:42 Yeah. So, basically, I am, working on the cluster info command PR. Basically, this is, for the Redis receiver component, and I wanted to ask regarding this, that currently what the Redis receiver does is that it, uses only the info command of the Redis.
And,
The enhancement proposed for this was that we can also add some metrics from the cluster info command.
Like, cluster state and slot, etc, into this, so that they can also be provided to the user.
So, the issue which I am facing in here is that if we check the Redis scraper func- Redis scraper file, we have
A structure, ready scraper, and in this, we have a metrics builder.
So, this matrix… the issue is that the metrics filter is automatically generated, and this is not written by anyone.
So, I wanted to ask that, is there any way by which we can generate some fields for the cluster info, command metrics?
So, cluster info field.
**Jade Guiton** 27:52 It sounds to me like this is a question very specific to the Redis receiver. I don't know if there are code owners for that component here today.
**Dmitrii Anoshin** 28:04 I think I'm listed as a code owner there, but I'm not very involved into that anymore, so I don't even understand the question right now, so I'll probably take a look at your PR and reply offline.
Yeah, that's okay.
And.
**Yaten Dhingra** 28:21 Yeah, sure. So, I will… yeah, sorry.
**Dmitrii Anoshin** 28:24 Go ahead.
**Yaten Dhingra** 28:27 I'll update this question in the… should I update this in the GitHub PR itself, so that you can review that?
**Dmitrii Anoshin** 28:36 Like, you can…
post a question in DPR and… and tag me as well. I already tagged as a reviewer, so you can just post a question, or you can do continued discussion on the issue as well.
**Yaten Dhingra** 28:51 Yeah, yeah, sure, sure, sure, definitely. We can continue the conversation on the PR or the issue.
**Dmitrii Anoshin** 28:56 Yeah, I just need to get, like…
Get up to speed on that receiver.
It's been a while, I'll… I'll look at that code.
Yeah, I think we can go next.
Thank you, Jatin, by the way, for helping with that. If you want to proceed working on that receiver and help with maintaining it.
It would be great if you can get, code ownership there as well.
**Yaten Dhingra** 29:38 Oh, yes, he's right.
Yeah, I'm definitely… I'm interested in that. I think, I was, talking to Slack on Slack also with someone, I forgot. So, I think there is, the AWS cloud log exporter, so there's a major bug in that. I am trying to fix that.
So, I think for the Redis receiver and the AWS,
cloud, exporter. These two are the main,
components that require some code owners.
So, I'm surely interested in this. I will fix some issues, and then maybe, if possible, we can… I can also be a co-owner for this.
**Dmitrii Anoshin** 30:16 Sounds great. Sounds great. And feel free to ping me in Slack regarding code ownership for the registry server. We can, like, get in touch there.
**Yaten Dhingra** 30:26 Yep, sounds good.
**TH Tiffany Hrabusa** 30:33 I'm next.
And I won't take up much time.
A couple months ago, I came to this meeting and proposed refactoring the collector docs architecture and filling in some gaps.
progress has been a little slower than I would have wanted, but I do have a proposal for a new information architecture, which I've linked in the notes document. If anyone has feedback now, I'd be happy to take it, or I've also posted in Slack, and you can just leave your feedback in the thread.
Thanks.
**Andrzej Stencel** 31:12 From the first look, I just said, this looks definitely so much better than the mess we have currently. I'm just thinking, where would the troubleshooting go? Yeah, that's the only thought.
**TH Tiffany Hrabusa** 31:25 Okay, great. I'll make a note. Thank you.
**Andrzej Stencel** 31:29 Awesome, thanks.
**Jade Guiton** 31:35 I think the troubleshooting is under the Manage the Collector in Production.
Category in the new architecture.
**TH Tiffany Hrabusa** 31:45 It might also make sense to have separate troubleshooting sections for different parts, maybe installation troubleshooting, and basically anywhere people can encounter problems, you can create a troubleshooting page, so…
Sure, Antoine.
**Antoine Toulme** 32:04 Tiffany, did you talk about this with the folks who manage OpenTeometry.io?
**TH Tiffany Hrabusa** 32:10 I'm the maintainer in OpenTelemetry.io, so yes, we have… yeah, yeah, so we've talked about it,
Okay. And I'm actually going to bring it up at the meeting today, but I wanted to get some stakeholder approval first from the collector folks to make sure that it makes sense to you.
**Antoine Toulme** 32:34 Sure.
Yep.
**Pablo Baeyens** 32:46 Yeah, well, definitely we talk about this, but I think it looks great.
I think it's… It's a big improvement.
**TH Tiffany Hrabusa** 32:55 Thank you.
**Pablo Baeyens** 32:56 So I'm next, just announcing that I want to stabilize the module exporter.
notably, this does not include the exporter helper, just the…
Interfaces that define what an exporter is, similar to what we did for other component kinds.
So if you have any… Concerns, any…
issues that we would need fixing before marking the exporter module as 1.0.
Juice.
liberty on the… on the issue. Thanks.
So, watch…
**Raj Nishtala** 33:48 Yep, I can go. I'll try to keep it brief here, everyone. So…
So I've been working on that, putting together… discussing about that OTTL function, which essentially mutates a JSON slice into multiple log records, records, something very similar to what the… I think the unrolled processor does in a different distribution.
In a distribution of the hotel collector, so,
So, as we've talked on that issue, it seems like we're tending towards this not being well, well ideal for an OTTL function, but rather be its own processor, because of the complexity of interleaving something that,
mutates a JSON slice into multiple log records, you know, how does… how will that work with other functions in the transform processor, right? There's some com… how many… will it apply to all the log records, or only a few?
there's some complexity that's been discussed previously around this, so the discussion has tended towards this being its own processor, right? Like, very similar to what the unrolled processor does in the bind plane distribution.
So I was… I guess, the question I put in one of the comments there is, is it possible that we start with… by upstreaming the unrolled processor? Because there seems to be a common,
need for that. At least, you know, we want to use it, and yeah, or… or would it be a new processor?
altogether, if that's the way… that's the direction we decide to go in. So, yeah, I just wanted to put that question out there.
Any thoughts?
Huh.
**Jade Guiton** 35:42 For what it's worth, I do think it makes sense to have it as its own processor.
it sounds to me like OTTL is meant for making changes within a specific
piece of telemetry. It's not really designed to turn one into multiple, or vice versa, so…
It does seem like it would make sense.
**Raj Nishtala** 36:04 Okay.
Would the unroll processor be a good starting point, or…
Sorry, Dimitri, you want to say something?
**Dmitrii Anoshin** 36:13 Yeah, I just wanna ask, how you want to…
Seeing the output of that processor.
So, you have JSON as one log record.
But it'll be separate log records within the same scope logs, right? So we don't, like… we don't emit separate resource… resource log records.
**Raj Nishtala** 36:38 It does make sense.
What's.
**Dmitrii Anoshin** 36:40 Except pieces of telemetry being sent, right?
**Raj Nishtala** 36:43 Right, separate log records being sent under a resource.
**Dmitrii Anoshin** 36:47 Okay, under the same, under the same resource. So, essentially, it's, still change…
Of the same piece of telemetry under a scope.
log… logs, scope, logs… how's it called? I don't remember. Under… anyway, like, the same log records, under the same scope, so potentially if the context is set to scope…
I…
personally, I don't see big problems of why it can be OTTL, but I'm not an expert, and I wish we had
someone from OGTO on this call. Maybe everyone can talk more, but… So…
**Raj Nishtala** 37:33 So, just a thought on that, so that it might be, across multiple… a different resource, across, multiple resources, because you have…
Yeah, because some of these JSON slices, what happens is they are logs that are essentially grouped together from multiple resources at the origin. So CloudTrail, I think, does this to save on egress costs, where they just batch up logs from
different services before sending it out to, to a destination. So it could potentially, yeah.
**Dmitrii Anoshin** 38:09 It can be possible to split between different resource monks.
**Raj Nishtala** 38:12 Right.
**Dmitrii Anoshin** 38:13 Oh, okay, in that case, it makes sense as a separate processor.
**Raj Nishtala** 38:18 Right.
So… so… so I guess, we do… there is something out there that does this, I just wanted to understand if we should leverage that,
To start with, or just start with something new, a new processor altogether.
**Dmitrii Anoshin** 38:37 I would also think if we can have one processor that would make this kind of split capabilities kind of generic, not only for logs, but you can split some, I don't know.
potential metrics, spans, I don't know, something like that. And if we can re…
maybe to ICOTL to some extent.
**Raj Nishtala** 39:03 Yeah, okay, something more generic across all segments.
**Dmitrii Anoshin** 39:07 Yes.
**Raj Nishtala** 39:07 That is something… that is definitely a… increases the scope a lot, but I was thinking about starting with logs.
**Dmitrii Anoshin** 39:14 I'm not saying to go from the beginning with that approach, just keep it in mind. Maybe we can take rollout process, but keep in, like, make the configuration interface in a way that it can be extended going forward, something like that.
**Raj Nishtala** 39:29 Okay.
Makes sense, but we don't…
do we need to… has it happened that we upstream a processor from a distribution? I mean, we do this all the time, right? From a distribution to… is that something… that's the really core of my question, is that can we use that processor as the starting point for this feature?
**Dmitrii Anoshin** 39:53 I personally don't see anything wrong with that. We do it occasionally, we just need to have a sponsor for that processor. The procedure is the same. You submit an issue, you get a sponsor, and how do you bring it, whether it's donation, or you bring… you build it from scratch, it doesn't matter.
**Raj Nishtala** 40:12 Okay, got it, alright.
Makes sense. I'll create a new issue and look for a sponsor then, yeah. Sounds good.
I think that's all I had, thank you. The next speaker, please.
**Israel Blancas** 40:29 Oh, hi?
So, well, all the things that, I would like to ask for some reviews on this PR that I linked there. It's a PR to add, some URLs, an additional feature.
To the reduction processor.
The things that we have been trying to figure out a way, right, to…
To do in an automated way.
Finding issues with… you know, those URLs that sometimes are part of the, for instance, the spam names, right?
When you're using things like, I don't know, for instance, the span metrics, connector, right, the, the race, right, the, the cardinality.
Causing a lot of cardinality problems.
So, the things that we are… What's…
We're talking with the… with some Grafana people, Jorge, who has been contributing a similar thing to the OBI project.
Yeah, the things that they extract that logic to one library, we do… did a proposal about… well, in that PR, right? About importing the library,
And yeah, well, we received some comments, because I think that that library was importing one… another library, right? Another transit dependency.
But it was archived, like, 6 years ago, or something like that. So I think that the Grafana people had,
a vendor in that scene, right? So now the transitive dependency is not there.
So yeah, we would like to get some feedback, right, on the PR, and try to move forward with that, because it's important for our… for us as vendors, and it's something that we would like to include as part of the OpenTeometry Collector.
**Dmitrii Anoshin** 42:19 I think we discussed that in Slack. I would like to maybe see some…
What we gonna pay, for having this huge
Of, like, data set being added as a dependency.
It's, like, essentially a huge dataset with some, I believe, machine learning applied to it, and that company is pretty slim.
It just does plain replacement of the strings, and now it becomes…
pretty big, so I would like to understand what we… what's the result of that donation? Like, do we… is their binary size gonna increase?
like, I don't know, maybe latency of the processor gonna increase, or something like that.
**Israel Blancas** 43:11 Well, in the case of the… in the case of the latency, right, this… I mean, this feature is something that we… you will enable just if you want, right? So, it should not… if you are not interested into the feature, right, should not affect you, or at least in the… in the way it's…
**Dmitrii Anoshin** 43:25 The binary size can be affected regardless of if it's being used or not.
**Israel Blancas** 43:30 Yeah, but the thing is that, it's just 14 kilobytes, right?
the JSON thing that is being included, apart from the code, that is not something…
**Dmitrii Anoshin** 43:41 Is that the binary size increase? Are you sure about that?
If you can prove that this is going to be exact binary increase, that…
That's what I'm asking, like, to get some idea, because, again, this is a simple processor, and now we are bringing huge complication, like, with ML and everything to it, so it would be good to understand.
How it's gonna impact the process.
**Israel Blancas** 44:09 Okay. Yeah, I will provide the numbers.
**Dmitrii Anoshin** 44:11 Okay, thank you. Brandon?
**Fraggle Rock (ca-wat-brt3)** 44:14 I guess you kind of already said it, but yeah, it depends on how this data is brought in, because the two patterns that I see are either the data's loaded on package init.
like, within the init function, there's a few dependencies of the collector that do this, and they, you know, basically instantly add data to the heap when they do it that way, and it doesn't matter if you have enabled the processor or not.
And the other pattern is when you… when the processor starts, the data loads. That's a little better. And then the last thing is, like Dimitri said, if it's in the binary size, that also…
nominally increases your memory usage, because the larger the binary is, the more RAM that is used to load the binary.
So, you know, like, that still has an impact. If it increases the binary size, that has an impact regardless of whether it's enabled or not.
**Israel Blancas** 45:08 Yeah.
**Fraggle Rock (ca-wat-brt3)** 45:09 That's why… I think that's why we're… we want to investigate this.
**Israel Blancas** 45:41 Any other comments, or something?
**Dmitrii Anoshin** 45:54 I think we can go to next.
Item.
About Windows.
**Jean-Hadrien DAMAY** 46:02 I think it's me, right? Yeah, okay, can you hear me correctly?
Nice. So, basically, I'm trying to manage
a set of hosts, which are both Windows and Linux.
I'm able to build a custom, collector,
versions, I mean, binaries for those hosts, based on a list of components.
And, in this building process, I include the Windows, event log receiver.
Which is not compatible with Linux.
But I'm still able to build binaries for Linux with this component included.
But then, when I include in my configuration a reference to this component, of course, the collector crashes on Linux, because the component is not compatible.
So, my question is basically, is this normal that I can include a Windows-only component in my Linux build?
On notes, first.
And, basically, how should we handle, cross-platform, like, multiple platform, builds a home.
Mayor is… does that make sense?
I don't know if I'm being ace, I'm not trying to… Makes myself understood.
**Fraggle Rock (ca-wat-brt3)** 47:29 So there's two questions, right? There's whether it's okay to be able to include the component even in a non-Windows build.
**Jean-Hadrien DAMAY** 47:37 Yeah.
**Fraggle Rock (ca-wat-brt3)** 47:38 I think the answer is yes.
what… we sort of want to allow the possibility when you're using OCB or building your own collector or something, to have the same list of components and then cross-build, like, on any platform, and it shouldn't fail when using some GoOS values and some when you're not. So, we actually do want that to be the case.
As for whether the…
the receiver should fail when included on an unsupported platform, we have largely used that pattern everywhere. So I think, like, the answer is, like, kind of… it's… the answer is yes that it's expected.
I don't know if we've specifically audited that choice at all, or if it's just something we have done, but that's… as far as I've been involved in platform-specific components, that's been the modus operandi.
Okay.
There might be space to debate that, though.
**Jean-Hadrien DAMAY** 48:32 So, basically, my option will be to manage specific configuration for specific platforms, right?
**Fraggle Rock (ca-wat-brt3)** 48:38 I, I think that would be the only option.
**Jean-Hadrien DAMAY** 48:43 Okay.
**Fraggle Rock (ca-wat-brt3)** 48:43 with the way it works right now. Now, that's a fair counterpoint to the way that we've been doing it. I think the… if I had to, like, guess what the reasoning is for why we do this, is that we generally try to fail fast on configs that we know won't work.
So, that's why we error out and stop the collector. In, like…
**Jean-Hadrien DAMAY** 49:06 Yeah, if it's not me, in this specific case, my thought process is basically, okay, Linux doesn't have the Windows Event Log receiver, I mean, the Windows Event Clog at all, right? So it's okay for me that it cannot receive data, right? Like, I'm expecting it not to get data anyway.
But I'm not expecting it to crash, right? I'm just expecting it to go, okay, it doesn't work, and that's it, right?
**Fraggle Rock (ca-wat-brt3)** 49:36 I think that's a fair point, and I agree with you, and, like, I've implemented components in, like, our own company's collector that do it this way instead, that, like, just run in no-op if you're on an.
**Jean-Hadrien DAMAY** 49:47 Hmm.
**Fraggle Rock (ca-wat-brt3)** 49:47 platform, basically. Run a no-op forever. It's… there's… there's upsides and downsides to that, where, like.
you need to make sure you spin it up in a very different code path to, like, not use a bunch of heap space, allocating a bunch of stuff that it then doesn't need, because it's not on the right platform, or whatever. Like, there's… there's some considerations there, but, like, it's a… it's a fair… it's a fair point, and I don't know where… at what side I land on here.
I can say at least that it's… it's expected what you're seeing right now
whether it's the right choice, I don't know. Maybe we… maybe there's space to debate that, though.
**Jean-Hadrien DAMAY** 50:22 Okay.
**Dmitrii Anoshin** 50:24 And this is something that we need to potentially decide regarding all of the compliance, not specifically this one.
**Fraggle Rock (ca-wat-brt3)** 50:33 Yeah, this lines up with, like, stabilizing these components and stuff. We need to, like, decide.
and then apply the practice across any that have this problem. Like, most of the host metrics receivers have some manner of this problem, too.
**Dmitrii Anoshin** 50:48 Yeah, we might… Might want to make it configurable, actually.
And by default, I would say that this behavior is probably…
More reasonable by default, but we can have an option in the collector to just B&O. Paulo?
**Paulo Janotti** 51:09 Yeah, no, I was gonna basically say the same that you just did. We… I think we… because we have this behavior that we already have for a long time, we should not change, but I think the ask for our option to kind of, hey, ignore this platform not supported, seems very reasonable to me, you know?
Oh, yeah, the same thing that you just said.
**Dmitrii Anoshin** 51:34 And.
**Fraggle Rock (ca-wat-brt3)** 51:34 It makes me think if we should have a more… sorry, sorry, you can go ahead first.
**Dmitrii Anoshin** 51:38 No, go ahead. I probably want to say the same as you wanted.
**Fraggle Rock (ca-wat-brt3)** 51:42 Right now, the way that we handle platform support and exclusivity is actually not unified. Like, the way we behave.
is unified, but, like, if there was something in Collector Core that was, like, managing platform support that all these components could hook into to, like, like, are we on the right platform? What's our current, like, default behavior, like, like, error behavior or whatever, like.
Having some sort of core thing like that that all the components could hook into would be useful for this, because we've had some inconsistencies in how the different components are handling this, even within the host metrics receiver alone.
**Dmitrii Anoshin** 52:15 Yeah, potentially it can be just a command line argument.
Optional, saying, like, ignore, unsupported.
**Paulo Janotti** 52:26 platforms.
Yeah, we already have on the…
any data gen, attribute to, say, unsupported platform, then we can do the test on lifecycle checking, kind of, oh, if it's unsupported platform, must be this error.
Then it becomes relatively easy for the core to have an option saying, hey, ignore these errors, or skip, something like that.
It's large scale. It's simple, but large scale. That's a bunch of things that don't support our platforms.
**Dmitrii Anoshin** 53:10 Yeah, so we can probably move this issue to core and generalize it.
No, not specifically this one, but maybe create another issue in Corinne to, like, to discuss it and decide.
**Fraggle Rock (ca-wat-brt3)** 53:26 I can file that.
**Dmitrii Anoshin** 53:27 Okay, awesome, thank you.
**Jean-Hadrien DAMAY** 53:34 So, yeah, okay, cool. So I just need to find out, at a lot of time, the issue is reassuring, right?
Some… some kind of follow-up on this.
**Fraggle Rock (ca-wat-brt3)** 53:47 Yeah, I'm gonna… I'm gonna file a more general issue in the collector core repo about, like, potentially ignoring platform unsupported errors and, like, how we can handle that, and I'll link it to your issue.
**Jean-Hadrien DAMAY** 53:59 Oh, Chicago.
Awesome, thank you.
**jmacdonald** 54:07 So I think I'm next on the agenda. I've put a link to a PR that I wrote a couple weeks ago, to improve the print command. So we've discussed this at least once in this meeting before. There is a glaring concern about security, but I want, you know, so I want everyone to look at it.
The idea is that I had a pretty rough debugging session once a month ago or two, and it turned out to be a combination of things involving
the way we deal with map structure, the squash attribute, as well as a couple of choice bugs in the upstream code, the GoViper map structure.
All of it was terrible, and so by the time I had gotten to the bottom of it, I had ripped apart the print command and made it do what I needed. I then discovered some issues that had been filed, and there was an existing command that had a bug, at least one, so I had put together this PR.
The bottom line here is that this PR will make it possible to print any configuration that the collector has for itself. If you have the capability to load from the config provider.
The configuration, this will print it.
The default mode is to print the redacted, a redacted string anywhere we use the config opaque, which is a sort of sanctioned mechanism for having
secrets in the configuration that are not revealed by default. So… but the point of the command I had seen already written by another contributor was actually to reveal the secrets, because if you're having trouble debugging the secret itself.
it's nice to know that you're sane and that you're actually passing a value that you think you are. And so, I've added a mode to
Print the unredacted content.
Altogether, that is essentially the question, is whether we're willing to accept this security, like, feature. It'll print the redacted content by default. If you ask it to print unredacted, it will, and that's the feature. The command was behind a feature flag. It still is.
The feature flag was named print initial config, and the reason why the word initial appeared there is for the same reason as the redaction concept.
the initial meant to say before it's resolved and configured as an object, because at that point, it's going to hide the detail from you. So,
I've removed the word initial from the command, I don't think it helps the user. Now you'd have a single command called print command.
a Boolean flag called validate, because I consider it an additional security protection to say I'm only going to print a valid configuration. So then, I also thought it would be nice, and I threw it in, because it's, like, three lines of code, to have an option to print JSON for those of us who would rather not parse YAML.
Just to consume the configurations. It's kind of common to have a command line tool print JSON. So, altogether, that's, like, one command under the same feature flag with a couple options.
redacted or validated, or JSON'd, and that's it. Thank you.
I have no more to say on that, but please take a look. Thank you.
And since I'm the last on the agenda, as far as I know, I will say thank you all for this great meeting. I appreciated the early conversation. It was tough. I appreciate everyone who puts in their emotional energy here.
Thank you.
**Dmitrii Anoshin** 57:42 Thanks, folks.
**Pablo Baeyens** 57:43 Thank you.
