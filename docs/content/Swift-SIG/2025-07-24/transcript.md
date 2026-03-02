SIG: Swift SIG
Date: 2025-07-24
Duration: 20 minutes
Zoom Recording URL: https://zoom.us/rec/share/-w_WGkwML3-GiJOJRpSpGI0iRBE1OEO94Q7zpz78-igVTv1IWbUUhSO1ueOxT4nc.zDjL_coFlGpUJUkk
============================================================

## Zoom Recording Transcript

**nacho** 02:00 Morning.
**Bryce Buchanan** 02:02 Hey, Nacho, good afternoon!
How are you doing.
**nacho** 02:11 Yeah, fine. Yeah.
Starting my holidays just after this meeting.
**Bryce Buchanan** 02:16 What's that starting your holidays.
**nacho** 02:18 Yeah, to tomorrow. So.
**Bryce Buchanan** 02:20 Oh, nice!
**nacho** 02:21 My last. Yeah, yeah, I will be 3 weeks out. But yeah, I will try to connect.
**Bryce Buchanan** 02:28 Oh, yeah, no, don't worry.
Good.
**nacho** 02:30 Yeah, yeah, yeah.
**Bryce Buchanan** 04:10 Hello!
**Martin Holman** 04:11 Blue.
**nacho** 04:59 Yeah, I, think we.
**Bryce Buchanan** 05:02 Yeah, shall we get started?
**nacho** 05:05 Yeah, I think we can start, okay. So
do you want to handle it? Or should I, Bryce? Whatever you prefer.
**Bryce Buchanan** 05:19 Why don't you take this one.
since you so kindly offered it.
**nacho** 05:28 Okay, so then let me share the document.
Okay.
yeah. So last, I have just copied what we had here. So so from from last week bastion 2 dot 0
remove a stable from ethics is done. So
yeah. So all the things that we wanted to have for the version 2 dot 0
at least on the code. Changes are finished.
So we should really think about yeah. So let's use a new topic about release
**Bryce Buchanan** 06:25 I think the only thing that is hanging us up at the moment is deciding our our minimum.
our our target version, minimum deployment target version
and it looks like embrace is still targeting 13 dot O
and we wanted to bump it to maybe 15.
But yeah, I'm I'm curious. I don't know if any yeah. Ariel's here. Oh, and Alex.
were you? You were the one who made the note, weren't you?
**Alex Cohen** 07:01 Yeah, I made the note just to to be able to link it to to to the rest of the team and embrace, because I couldn't make it to specific meeting. I didn't know how to link it otherwise.
**Bryce Buchanan** 07:10 Right right
**Alex Cohen** 07:12 Could you spell.
**Bryce Buchanan** 07:13 Little bit about your your support, for ios. 13.
**Alex Cohen** 07:18 So so Ari Ari knows the numbers. I just know that. We're probably not not there yet. We'll be there soon enough, but I don't think we're gonna be there at at to hotel 2 point O and, to tell you the truth, it would be a pretty like. It would be a pretty big problem for us if we had to to fork it and not use the the main the main repo and stuff it would.
I mean, we. We've always strived to to try and use the the main repository as much as possible, and not go off the beat and pass, and we would love to continue that like I don't know. Maybe
maybe we could talk about something where, like in 6 months or something. We we could. We could drop like 13, and maybe 14
but like at at 2 point. Oh, it'd be very last minute for us to to start the process of convincing everyone with an embrace that we can do it because there are still customers running on those versions, and we don't want to cut them out right away.
**Bryce Buchanan** 08:20 Okay, yeah, I think that's that's reasonable. Yeah, maybe. Now is not the time to bump that. Let's revisit this in a couple of months and see see where we're at. Then.
**Ariel Demarco** 08:32 Sounds great, thank you.
said internally. We'll we'll probably talk to see which of the peer customers are on on those versions, and see also if they have plans on, on migrating, on, on start supporting other versions and stuff like that, I share that our plans with them, because
it's, it's, it's a bummer. But we have to support what they support. That's basically what happens today.
**Bryce Buchanan** 08:59 Yeah, okay.
cool. Alright. Well, I'll I'll I'll do a release today. Then without those changes. Just leave it the way it is
And yeah.
**Alex Cohen** 09:20 That's awesome. You're gonna do a release 2 point O today, or release and just a beta or something or.
**Bryce Buchanan** 09:27 Yeah, I mean, I guess I'll do. Do a release. 2 point. Oh,
**Alex Cohen** 09:31 Awesome.
That's great.
**Bryce Buchanan** 09:34 There are a couple of Prs that are
that are open that we could possibly merge. Maybe we can discuss them later.
**nacho** 09:45 Yep, yeah, there are a pair for the euro session instrumentation, both of them, I think.
Yeah, we we should think if we must put them in
2.0 or not, because I don't think there are any more peers to to that. So
yeah, let's go with that. Maybe
in the new topic here. Okay? So we handle also entirely.
Prometheus, exporter back that you reported
**Charlie** 10:22 I think it's all good.
Well, actually, there are other issues
related to the Prometheus Exporter, but I haven't created them yet.
**nacho** 10:34 Okay.
**Charlie** 10:36 But this is just one of them.
**nacho** 10:39 Okay, so this would, this is, this is fixed, then, for you.
**Charlie** 10:44 Yeah, yeah.
**nacho** 10:46 Okay, so there are other bugs. But yeah.
**Charlie** 10:53 Yeah, I'm surprised. They haven't been
reported yet, because it's been around for like a while right like this Prometheus Exporter.
**nacho** 11:05 Yeah, the thing with this is, I don't think there are many Prometheus user currently.
**Charlie** 11:10 Yeah.
**nacho** 11:11 Or even the past and people is using mainly otlp collector, and and reporting through that, and probably exporting after in the collector.
instead of exporting directly from the tracer. Yeah, that that will explain it.
**Charlie** 11:29 See.
Okay, I just wonder if it's worth
maintaining, like the exporter for Prometheus, if it's not being used much.
**nacho** 11:41 Yeah, that that's a point that we.
The spec says that we must support it.
That's the reason there is an export. We?
Yeah, it it. Yeah, we. We must also support other things like open tracing seems something like that, because
the spec says that we must.
That are probably not very much tested.
They have been somewhat tested. But yeah, we
must keep them. And and we, we are focused on on fixing whatever appears or or at 13 prs, definitely, that fixes whatever
comes with these exporters. But yeah, that's true that
there is no much use of it. And yeah, not even oh, re purchasing problem.
**Charlie** 12:38 Good to know. Thank you.
**nacho** 12:47 Okay? So then, yeah, that
that's all for the topics from last week. So now for the release of version 2, today, you set
Bryce to. There are a pair of
They're up pretty.
**Bryce Buchanan** 13:06 I'm looking at these Prs here, and it looks like there's some feedback on on both of them that need to get resolved that just haven't gotten resolved yet, so I think that we can. We can wait on those and just start release.
So again we have the crash fix with swizzling Alamo fire, and the one below that.
**nacho** 13:27 Yeah, that's right.
Yeah, both these, this one you asked for the
for the spaces here and the indentation. Okay.
okay, yeah. This one once. Yeah, I approved, because it looked good, right? But waiting for for your approval. And your changes.
**Bryce Buchanan** 13:50 Reason it's still failing. I'm not. I didn't look too closely at it.
**nacho** 13:56 Okay.
**Bryce Buchanan** 13:57 OS! O vision! OS.
**nacho** 13:59 Yeah, that.
**Bryce Buchanan** 13:59 That, who added that in there.
**nacho** 14:05 Yeah, I, yeah, we we.
It doesn't actually look like, look if it's a a.
**Bryce Buchanan** 14:10 It looks like it might just be a and.
**nacho** 14:13 Sorry.
**Bryce Buchanan** 14:14 An errant error. I'm just gonna rerun it.
**nacho** 14:18 Yeah, maybe a a flicky test, something like that. We have some.
**Bryce Buchanan** 14:23 It, didn't. It? Didn't look like there was any test errors. It just was like one of those exit.
**nacho** 14:29 Oh!
**Bryce Buchanan** 14:30 65.
**nacho** 14:30 I was running.
**Bryce Buchanan** 14:31 Yeah.
**nacho** 14:34 Okay, yeah. And the other, it's also about an another Switzerland in the euro session upload task
that basically the issue is that when using swift it? Yeah, the tape safety is is not correctly handled
because it uses. Yeah, they were pointers playing pointers in objective. C, and yeah, and also. Ari reviewed it and asked for some test.
**Bryce Buchanan** 15:06 Yep.
**nacho** 15:08 So I, yeah, I also have also approved because the changes make sense.
But yeah, I mean, this will be great. I don't know.
He will provide them or not, because I.
**Ariel Demarco** 15:23 It's.
**nacho** 15:23 Approval was like 2 days ago. And so, yeah, I don't know.
**Ariel Demarco** 15:28 Yeah, the thing is probably this bug. It's because there was no test for these methods.
**Bryce Buchanan** 15:34 Yeah.
**Ariel Demarco** 15:34 So to ensure this doesn't happen.
**Bryce Buchanan** 15:38 Yeah, I think that's.
**Ariel Demarco** 15:38 A bummer to create that test for each of the methods of URL session. We've done that, and it's painful, but
it it kind of helps on the road.
**nacho** 15:51 Yeah. Anyway, both are valid and are good. So if we want to release, we can merge.
I mean, with the forest spaces that's
and with without this, because it fixes a real bug so we could merge it and release a version. 2.
**Ariel Demarco** 16:10 And maybe that comment for for a test later. And that's basically.
**nacho** 16:17 Yeah. So we are free there. If we want to release with.
**Bryce Buchanan** 16:21 Are they?
We won't. The test won't ever get written if we merge it without the test.
**nacho** 16:28 I think we can do something that it also.
will be I I we can release a beta maybe.
Ask for these changes to come in.
and if they arrive, let's merge it. And in the in the in the meantime we we can test if there are any issues with 2.0 changes.
**Bryce Buchanan** 16:56 Okay.
**nacho** 16:57 That. Do you think that's a good approach?
**Bryce Buchanan** 17:01 I think that's fine. Yeah, I can. Just I can leave it as like a a pre release. Build.
**nacho** 17:08 Yep.
And we yeah, probably we can do that.
Keep us a pre-release and maybe ask I don't know his name. Sorry, Tomer, he
to update his peers, to be in the 2.0 version, and maybe that cannot jump
positive feedback on him to to merge that correctly.
But yeah, definitely, this one could could also
come if he, some text or not, tests or not, I don't know.
It will be great having them definitely.
**Bryce Buchanan** 17:57 Here, let me let me ping him on. There.
**Ariel Demarco** 18:00 If if we are in a rush, I can do them today, merge it. And I do the those tests today. So we don't forget about them.
We can do 2.0 as soon as possible.
**nacho** 18:12 I I don't know if we are in a rush.
**Bryce Buchanan** 18:15 It's very easy to release a hot fix. It's not a big deal.
**Ariel Demarco** 18:19 Cool.
**Bryce Buchanan** 18:20 Okay.
**nacho** 18:21 But it's yeah, like having a major version
and having to release a back fees. Release just.
**Bryce Buchanan** 18:30 You know.
**nacho** 18:31 Are they after? A you know I.
**Bryce Buchanan** 18:35 Yeah. But I mean, like we've been, we've been beating around the bush about this re release for almost a month, and it like, there's always just another pr that comes in right? So.
**nacho** 18:44 Yeah, that's true. We we promise we we work. I think we had a promise of the 7th of August. So we are.
**Ariel Demarco** 18:53 We'll try.
**nacho** 18:55 I'm definitely on track on that. But yeah, we we can release now as you as you as
q. 1. Yeah, I don't have anything against that.
**Bryce Buchanan** 19:21 Cool alright. Well, I've got I just spinned up a a release. Pr, so yeah.
**nacho** 19:59 Okay.
any other topic. Anyone.
Okay. So then I think we can ended up here.
Cool? Yeah. Great.
**Bryce Buchanan** 20:21 Have a good vacation, aren't you?
**nacho** 20:23 Yeah, thanks. I. Yeah. I don't know if I will join following meetings.
**Bryce Buchanan** 20:28 I'm doing.
**nacho** 20:29 Will try to. But yeah.
**Bryce Buchanan** 20:30 Okay.
**nacho** 20:32 We are in person, too. I am fine.
**Bryce Buchanan** 20:34 Yeah, we'll let you know if there's any problems
be like I'm nacho come back
alright. Have a good weekend, everybody.
**Ariel Demarco** 20:46 Guys.
**Charlie** 20:49 Thanks, bye.
