SIG: Client Instrumentation SIG
Date: 2026-01-06
Duration: 11 minutes
Zoom Recording URL: https://zoom.us/rec/share/tRKz-xh-Xvo6og7QvSlJGkkr0J__NRwuJJ21MoOr3jgTxVMLNHz1VPVixmkb60Mh.TFkBxxsulHrybrbg
============================================================

## Zoom Recording Transcript

**Martin Kuba** 00:24 Hey, Jason.
**Jason Plumb** 00:27 Hey, Happy New Year, Martin.
Are you running this meeting, Martin?
Hopefully.
Maybe.
**Martin Kuba** 02:03 Hey, everyone.
**Jason Plumb** 02:05 8.
I've got nothing.
**Martin Kuba** 02:23 Can't hear you, Jason, for some reason.
**Jason Plumb** 02:25 Really?
**Martin Kuba** 02:25 It's probably my endo. Hold on just a sec.
**Jason Plumb** 02:29 Can anyone else hear me?
**Bee Klimt** 02:31 Yeah, I hear you just fine.
**Jason Plumb** 02:32 Okay.
**Martin Kuba** 02:33 Okay. That was my problem.
I can hear you now.
**Jason Plumb** 02:37 That's one of your problems.
**Martin Kuba** 02:39 Oh yeah, I've got money.
**Jason Plumb** 02:45 I was saying that I have nothing for this agenda.
I'm still just coming back from holidays and getting in the swing of things, but I thought I'd join.
**Martin Kuba** 02:58 Same for me.
Did you have a good… good holidays?
**Jason Plumb** 03:07 For me, it was pretty chill.
Didn't travel, stayed here, kept it pretty low-key.
Took some naps. That's pretty good. Yeah.
**Martin Kuba** 03:45 Well, it might be just us, and it doesn't seem like there's anything on the agenda.
Anything on your minds?
Coming into the new year.
**João Oliveira** 04:00 So everyone is mostly catching up.
**Jason Plumb** 04:06 Yeah, and that's… I think that's universal right now. I… I wonder if,
I thought I remembered seeing something that was closed in semantic conventions that was relevant to…
App start time, is that right?
Let me see…
Might have been closed.
I'm not gonna be able to find it now. Watch.
Well, here's what I'm really thinking now, is that I wish in semantic conventions, I wish we had a label that we could put on client stuff. I don't know that we do.
**Martin Kuba** 05:06 There is a… I'm looking right now, there's an area…
**Jason Plumb** 05:08 Are you a client.
**Martin Kuba** 05:09 Client, yeah.
**Jason Plumb** 05:11 Alright… How good are we about using that thing?
**Martin Kuba** 05:20 There are only 4 issues.
**Jason Plumb** 05:21 Yeah.
Well, let's try and get better at using it, if there's stuff that's specific. I can't find that… that thing I was thinking of.
Might have been in a different repo.
**Martin Kuba** 05:44 So then they're, like, there are… dedicated,
maintainers for this… for the semantic conventions, right? I mean, they apply these.
**Jason Plumb** 05:55 Yeah.
**Martin Kuba** 05:55 would apply these…
Yeah, so it's just a matter of, like, for us to pay attention to when new issues with those labors.
**Jason Plumb** 06:06 Yeah…
**Martin Kuba** 06:12 Okay.
I don't see the one that you were thinking about.
**Jason Plumb** 06:17 Yeah, I don't either. I'm probably confusing it with a different repo, so let's not belabor that.
**Martin Kuba** 06:22 Come.
Yeah, it seems like, the last meeting was… Bing of December, obviously.
And there wasn't much there either, just the breadcrumbs.
Discussion.
Alright, well, I guess we can…
We can just think about things for a couple more weeks, and… Bring out topics next time.
**Jason Plumb** 06:58 I found the one I was talking about. It's old, it's old, let me share.
This one.
So… Think…
Yeah, this person works for Amazon. I'm pretty sure it's a she, so I'm just going with she, but if I'm wrong, I apologize, because I think we've chatted before on Android.
Yeah, so this was,
Closed out just because it got stale over the holidays, and there was a lot of work done on this.
Which is why I'm kind of remembering it, and I was a little bit contentious. It's not a big change, but like all semantic conventions, it's, like, not usually a big change, but there's a lot of opinions on bike shedding. So…
I don't know, I…
I removed stale back then. I don't know if I can do it a second time, but, you know, there was holidays in here, and, you know, I… I've been trying to keep this alive, clearly, because I want to see it through, and I think having this convention would be useful.
But I would encourage others to maybe…
**Martin Kuba** 08:10 Chime in on this if you have an opinion?
**Jason Plumb** 08:14 Maybe I'll bump it one more time.
**Martin Kuba** 08:16 And does this apply only to… to mobile?
**Jason Plumb** 08:20 No, it does not look like it.
It's just app, and app spans. So, the actual convention here is under app.
**Martin Kuba** 08:33 And there's a spanned… a span…
**Jason Plumb** 08:40 Internal span, time to first draw…
And I think that's cool, because it has,
like, using a span for this allows you to have a start and end time, right? And so you can calculate duration. So it's not just, like, load time, it's, like, what time did it start loading, or drawing, I guess? What time did it stop drawing, and then some attributes.
this is pretty… pretty simple, like, pretty basic. There's not… I don't think there's a lot of…
I don't know, there's… I don't think there's too much to argue about in here, although…
you know, this is, like, maybe a good start. Like, this doesn't apply to web as much, and I don't know if that was some of the comments, but…
**Martin Kuba** 09:23 Yeah.
**Jason Plumb** 09:23 Alright, I think…
Thanks for humoring me and hearing… letting me just, like, talk about this. I think I've convinced myself to reopen this.
**Martin Kuba** 09:33 Okay.
Yeah, I'll take a look at it. It doesn't seem like this is something that would be…
Applicable to browser, but I'll take a look at it too.
**Jason Plumb** 09:46 Yeah, you… you don't get time to first paint.
**Martin Kuba** 09:50 We do, there's… There is… there is, like, some… Paints, paints… Durations or timestamps.
**Jason Plumb** 10:02 Yeah.
**Martin Kuba** 10:05 But, I mean, I don't…
like, we're trying to get away… we're trying to get away from spans in general. I'm not sure, like, how, like, spans are useful here, because… because we can't really parent things during…
This time, like, we get… we get those measurements after the fact they happen.
**Jason Plumb** 10:23 Yeah, so it would just be, like, a dangling, isolated span.
**Martin Kuba** 10:26 Yeah, yeah, exactly.
**Jason Plumb** 10:27 I mean, that's fair, and it could be modeled as an event.
Yeah.
Okay. Well, maybe in a month it'll time out again, and we can… Forget about it.
**Martin Kuba** 10:44 Well, I mean, if it's useful on the mobile,
**Jason Plumb** 10:47 Yeah, I don't think we have an implementation for this in Android yet.
**Martin Kuba** 10:51 I think there's some talk about it, but I don't think we have it.
**Jason Plumb** 10:54 Cool.
I won't drag this on any longer. I just… I found it right as we were closing up.
**Martin Kuba** 11:06 Cool. I don't have anything else to talk about, I guess.
**Jason Plumb** 11:10 Same.
Okay, I'll put a note of this in the… in the… in the meeting notes, and then I will see you in a couple of weeks if I don't see you in the comments.
**Martin Kuba** 11:20 Sounds good.
**Jason Plumb** 11:21 Okay.
**Martin Kuba** 11:22 See, everyone.
**Jason Plumb** 11:23 Bye.
