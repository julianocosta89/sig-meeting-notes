SIG: Swift SIG
Date: 2025-07-10
Duration: 21 minutes
Zoom Recording URL: https://zoom.us/rec/share/89QxdVtL4ngDeDnlaqAP-fdwiqph8L_UBlECXwU6bJVeU5cpWHa5Mv2NM2ptfvo9.gmcPZlEzDpkt4VYU
============================================================

## Zoom Recording Transcript

**nacho** 00:44 No.
**Martin Holman** 00:56 Hello!
**nacho** 00:56 Good morning!
**Martin Holman** 02:37 Who else are we expecting today?
Haven't checked in the slack.
**nacho** 02:44 Yeah, seems like she's logged in today.
For the rest, they don't know anything.
okay?
So yeah, let's let's start whenever you can remember, if you have any topic you want to talk about.
that's month.
In the topics already. Talk last week. So try, yeah. Just started.
Insert that document.
Okay?
So, topics from last week.
Yeah, we've had the data completion discussion that this was a
this was about the renaming of data compression that it was incompatible with some
with some employees that had spm.
so the decision was made to change it for version 2 dot 0. That will be coming soon also. And
it has been merged up here that changes it. To use the original data Compression Library from
original, that we didn't have a spm project when we started using that so we copied the file because it had
proper copyright copy. So but now we use the whole data compression that we
that will solve these problems. Because it will be the original one. And they can just link with the same thing if they use it.
So yeah, this is March, and it will come in the next version. That will
should be should come to
with all the changes, except if we need some quick fix Google.
**Martin Holman** 05:11 That included as part of the the breaking change.
We're gonna do or.
**nacho** 05:16 Yes, yes, as as it was a breaking change.
Major update. Oh, I mean, we didn't have to. But we want to keep that.
**Martin Holman** 05:27 Yeah.
**nacho** 05:28 As best as possible.
Also, cocoa ports are still failing
and it was going to be handled by.
**Arri Blais** 05:38 Thought. This was fixed.
**nacho** 05:40 It was fixed.
Okay.
**Arri Blais** 05:43 Yeah, cause we we it. We we said it was fixed last week. I thought.
**nacho** 05:52 Oh, yeah. Sorry. Sorry. Here. Yeah.
**Arri Blais** 05:55 Single word. Thing doesn't explain anything else. Just fix.
**nacho** 06:01 Okay. So yeah, thanks. I copied that. And I didn't. Yeah, I didn't.
yeah, I didn't catch that. It was already fixed. Thanks.
Also. Symmetric attributes generation for Swift 6 this is something that we talked about for a week. So quickly set
we plan to come with a 6 6 version eventually.
But and and there. There are some things that must come
in many areas of the code in order just to build 5, 6
at least for concurrency. That's what, including changes. But we also.
**Martin Holman** 06:47 L abi compatible, though, is that right?
**nacho** 06:50 Yes, yes, it's aba compatible.
**Martin Holman** 06:53 Oh, okay.
**nacho** 06:53 But yeah, the idea is that Swift 6 2 has some updates in the way that that's handled. So probably waiting for that is smarter
than trying to come early with something
given, also that it's coming in October, and all the new
easy concurrency changes that they brought. It would simplify some of the things
So yeah, that that can be a a good path to follow.
So we will be waiting for that. On the meantime, we have also talked about opening a branch
from Main probably after 2 0, or when we are really near to 2 0. So
people can start working in that branch updating things.
I don't know. Maybe package by package. I I don't know how we can handle that still, but
that that will be great.
It could also come some.
**Martin Holman** 07:58 For Swift 6. You're talking about.
**nacho** 08:00 Yes, yes, the idea is having that. Now that we already have
X code, the Beta versions have 6.2 even not the final version of it. We could start. But mo- most of the changes are so we could start working on that
and that branch. I'm trying to keep up there.
It could also be a nice moment to update the
the Api and the SDK. So we can have some asynchronous method that might externally be
nice for some users, and also internally could
simplify some of the stuff that we are doing.
But yeah, if
if it's additive, it would be great. So we don't have to change to 3.0. Or if not, maybe also having a 6% is good enough for a 3.0% of.
because we would have been like
too long just having a 1. That's ever so. Maybe we should be a bit more agile in that.
that's my opinion.
But yeah, I think that maybe it will be better
to keep up with new stuff.
**Martin Holman** 09:21 Yeah.
**nacho** 09:22 Also, yeah. For version 2. Also, the metrics were updated
so the old metrics are not there anymore. In the main brands. The new one
still have the stable name on them.
But I asked Bryce and Gritty up here, but it's still not building correctly
to rename them and use the values for
trying not to create much pain in the users, but
with a warning, so they can misuse those.
Also the plan for this version, 2 is 7th of August.
So yeah, we have like 3 weeks in order to the the breaking changes are basically version 2 changes, also,
renaming of the span of the
SDK span that it was record events readable span
type now will be a span SDK,
also similar to a Span Api, that we have sorry Spanish decay that I think it really covers what it is, and people will be probably
understand it better. What's the target span that we that should be good there.
Also, from the current state of the
main branch, running the test with threat sanitizer show some threat based conditions in the stable metrics. So they are not so stable.
So yeah, I I was working on fixing some of this still not finished. But yeah.
if anyone want to take us on this, just putting some notice and something like that, some blocks anyone wants to take a look on them.
please let me know, and I will.
I believe that you fix it for yourself. If you want
If not it, it it must be fixed before releasing 2.0 we cannot really metrics with face condition stuff that's not
beautiful.
And also another topic I wanted
here that this is my renewable topic.
He's who which version should we support
as we are breaking changes? Maybe it's a good time to also break some
OS versions that we are currently supporting the current version. We half mount east.
If I, Ios. 13, and my question.
**Martin Holman** 12:11 Right, yeah.
**nacho** 12:12 12th
open to, to, to comments open to opinions. What are your target?
OS versions there?
**Martin Holman** 12:31 I'm not actually sure about end users
of honeycomb. We could look into that Ari.
**Arri Blais** 12:37 Yeah, I'm not a hundred percent sure. What versions of OS they're targeting.
We could definitely ask.
**nacho** 12:51 I mean, we don't want to break support for people, but
are using it. We. We have always tried to be to support as old as possible.
**Martin Holman** 13:02 But currently I think that.
**nacho** 13:04 In order to upload apps, at least for Ios in the app store you need xcode 16 that I think the minimum.
The bookable version is, ios 15.
So I don't know if someone is supporting something lower than that, but they are probably not
uploading apps to appstock, because it doesn't build for them. So yeah, I don't know if that could work.
**Arri Blais** 13:36 Yeah, that that seems like a good enough
approximation to make again. I'll I'll I'll double check in. I can get back to you. I'll bring it up next week at the sake, but it's.
**nacho** 13:50 Okay, yeah, I can also open a question in the in the slack.
**Arri Blais** 13:55 I highly doubt that they're not uploading any apps to the app store and still targeting lower OS's. That seems unlikely to me.
**nacho** 14:06 Yeah, maybe, Mac, anyone using Mac, that's more open.
**Martin Holman** 14:10 True.
**nacho** 14:12 That's but definitely for Ios probably not.
**Arri Blais** 14:15 I think most of our customers are using it for Ios, but I can double check again.
**nacho** 14:22 Okay, yeah, we'll also ask in the
slack channel. But I think that's too now, recently
too many messages there about the peers, and now towards things that are
probably will. No one will notice that. But yeah, I will open up a question there.
Yeah, that was my my only topic I had for today. Do you have anything.
**Martin Holman** 14:55 This is my 1st day back from Pto, so I don't have anything with them pressing for me.
All right. Do you? Anything.
**Arri Blais** 15:02 Nope had nothing I needed to bring up.
**nacho** 15:07 Okay, then,
I don't think there are. I mean, we can review the project. But I don't think there are many
issues that definitely pull request. Not
I. I clean them up a bit. We are have some
automatic dependencies that want to update the Rpc. Swift to person 2
that I don't know if that will build for us. So I have left that
And the rest are also automatic, and this one is the one from Bryce. That is still just not built. So it's not Max.
From issues to recent issues. Oh, sorry did I.
**Martin Holman** 15:51 No, no, you're good.
**nacho** 15:52 Okay, yeah. From someone asking for the status of persistent exporters. Does the exporter that? Yes.
perhaps any other exporter to use an intermediate file.
So you can.
You can use that in a
authorization of of the of what you export.
so you won't have to keep that
in memory always come in case you quit or or cross it, or whatever it would skip.
someone asking for support for some more network information as android. First.st I know
we don't have this support. If anyone wants to add that.
Yeah, you think so from yet.
if anyone was to take it, something like that totally open for that change.
I think this is. Then this is close, right?
You said.
**Martin Holman** 17:07 I am.
Are you sure, are we? Are we 100%? Sure it's fixed all right.
**Arri Blais** 17:14 I remember we discussed, I remember we discussed it the last meeting. There was something I I remember it was a very short discussion. It was just like, yeah, we fixed it. It's working.
**Martin Holman** 17:25 I feel like coca pods has been a saga for a while of like it's working. No, it's not. It's working.
It's not.
**Arri Blais** 17:33 I guess we can open another issue, but still broken.
like the prairie dogs poking their head up and down from.
**Martin Holman** 17:39 Yeah.
**nacho** 17:42 Okay? So I think that's that
these are just development tasks that
issues that breaks open for the metrics stuff. And yeah, that these are one month. Also. Yeah, they are definitely.
**Martin Holman** 17:58 About 8 8 0, 2. Is that fixed now.
**nacho** 18:02 8 would.
**Martin Holman** 18:05 Internally defined data. Compression conflicts with externally can defined data, compression.
**nacho** 18:15 Yeah, yeah, this is the one that. Yeah, you can.
**Martin Holman** 18:18 Now.
**nacho** 18:20 Yes, I can. I can mark it as fixed.
Yeah, it is really, we need
7.
Yeah, that's true.
So
any other thing that you can see.
**Martin Holman** 19:37 It's jump!
**nacho** 19:38 So.
**Martin Holman** 19:39 We have the is the cocoapods release broken? Is that
looks like we can probably.
**nacho** 20:23 Yeah, I think that's consenting.
**Martin Holman** 20:29 It's good.
**nacho** 20:40 Yeah, I've seen that. Yeah, probably these are related to it. Issues that that I assume.
Yeah. And I think that's that's all. Then.
**Martin Holman** 20:53 Train.
**nacho** 20:57 Okay, so go.
**Martin Holman** 21:00 Thanks for running.
**nacho** 21:02 Mike.
**Martin Holman** 21:03 See you.
**nacho** 21:04 Thanks.
