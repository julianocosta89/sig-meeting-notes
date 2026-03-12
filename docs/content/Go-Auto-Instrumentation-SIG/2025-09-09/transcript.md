SIG: Go Auto-Instrumentation SIG
Date: 2025-09-09
Duration: 12 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn** 00:13 Hey!
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 00:18 Hey, how's it going?
**Tyler Yahn** 00:20 Good, how are you?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 00:21 I'm good. You?
**Tyler Yahn** 00:24 Yeah, just, chugging along, a lot of things to do, a lot of things to get done.
Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 00:31 I know the feeling.
**Tyler Yahn** 00:33 This is common, right? Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 00:35 Yeah.
**Tyler Yahn** 00:45 You guys have anything fun over the weekend?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 00:51 For me, it was just catching up on stuff, like, after vacation and so many things that…
**Tyler Yahn** 00:56 Yeah.
Yeah, it's, it's starting to cool down here in Oregon, so it's kind of nice not having, you know, high 80s or 90 degree days, so, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 01:11 I don't know what you mean I'm wearing my sweater.
**Tyler Yahn** 01:13 Yeah, I'm all about it.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 01:16 Yeah.
**Tyler Yahn** 01:16 Give me a few months and I'll be over it, but, yeah, right now.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 01:23 Yeah, humans are funny in that way.
**Tyler Yahn** 01:26 Right?
So I'm looking at the agenda, I don't have too much, I just, have some common ones. I'll look at some PRs and the milestone, I want to talk about that, but if you guys have things you want to talk about, go ahead and add them there as well.
If you, haven't yet, please go ahead and also add your name to the attendees list, and Yeah, we can jump in here in just a second. I'll start sharing my screen.
Cool.
Alright, well, I'm looking back over also the… past week that I wasn't able to attend, it doesn't look like there's anything carrying over, so we can probably just jump in here.
Starts off, just looking at the open pull request, so there's a few.
Going through some of the… Oh, excuse me, sorry about that. Gone through a few of the, open, Dependency updates right now, still working through those.
There's a few that require an update so that we don't support Go 123 anymore, so that's coming up. I think that that is kind of a question around the milestone, or I'm sorry, yeah, I guess the milestone, because it also requires a release.
with this release being the last release that we would support Go 123, and then the next release, we would drop it.
So, I think that that's kind of motivating us, looking into the milestone in just a second. I think the only other thing is this, testify, Lintz Rule here.
Oh, looks like I have a pending review that I haven't submitted.
I don't think it's that critical. I can take another look at this. So, it looks like this just looks like it needs a review from me at this point, so… If you haven't yet, you're welcome to take a look, but, yeah, it's probably just on me, to address this.
Okay, and then, yeah, these are the two that are blocked by CO123. These two are ready to merge, actually. So, deal with that after the meeting.
Going to the milestone, though, so I wanted to take a look at this. This is the thing that we wanted to get done. I'm hoping we can get this done this, this week. I think that there is a reason to just bump these last two. There's things that are active, but they're not, I think, ready.
Both of these issues, raphael, sorry, I see your hands up.
**Rafael Roquetto** 04:07 yeah, I saw that it merged the claim format one. Apologies, I couldn't get to that yet, we were in between release.
So it's been chaotic.
Weeks for me.
**Tyler Yahn** 04:20 the…
**Rafael Roquetto** 04:20 But…
**Tyler Yahn** 04:21 Yeah, what did you need to do on that? It looked like it was ready to go. I'm sorry.
**Rafael Roquetto** 04:25 No, but I think we wanted to do the Dockerization of that, right?
**Tyler Yahn** 04:32 Oh, sure, yeah, yeah, sure, that's fine. That's just a follow-up, we can, we can handle that.
**Rafael Roquetto** 04:37 Okay, cool.
**Tyler Yahn** 04:37 Sorry. Cool. Yeah, I probably should have made that clear. I saw that, yeah, let's do that as a follow-up. I totally forgot about that. I mean, I knew about it, but I forgot to mention it. Yeah, I don't think that there's anything blocking us having it as it is, and then we can just iterate on it.
**Rafael Roquetto** 04:52 Alright.
**Tyler Yahn** 04:53 I also think that it's, from looking at it, it's been applied, so, like, that's kind of, like, already in a good place, just from the coding standpoint, so we can just keep iterating and making the tooling better, but yeah, that's not… I didn't want to block on that. That looked like it was ready to go.
**Rafael Roquetto** 05:08 Okay, cool, cool.
**Tyler Yahn** 05:09 Yep.
**Rafael Roquetto** 05:10 Thanks.
**Tyler Yahn** 05:12 Okay.
Back to this one, though, the fixed other arch stubs, I don't think anything's been done here. Ron, are you okay if we move this to the next milestone?
**Ron Federman** 05:22 Yeah, sure.
**Tyler Yahn** 05:23 Okay.
Cool. This one is one that existed… Nicola was looking at it before he went on break, I was looking at it while he was on break.
I've got this half PR started on this that I just haven't pushed and finished up yet, But I don't, think I'm gonna get this, addressed, or have a PR up, I think, in the next, you know, few days. So, I'm wondering, if we could just move this to the next milestone, if there's any opposition to that?
I see Nicholas shaking his head, so… Yeah, I don't think it's too critical to get it out with this. It's not like a blocking bug would be great to fix it, but it's a rare bug, I think, so I think that we can probably try to… address this in the next one. So, like I said, I started working on it, I just, got 20 things going at the same time, so…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 06:14 You know?
**Tyler Yahn** 06:15 Hopefully, hopefully get this fixed in the next iteration.
Okay, cool. Alright, with that then, actually, Rafael, let me, track that, Docker issue as well.
Awesome.
Yeah, because otherwise I will forget about this as well.
Thanks for reminding me. Otherwise, I think that that's it, though, so this should be cleared. I think that we're good for the release. I've got a pull request that just merged for upgrading the semantic conventions, so we're on 1.37, which is the latest.
Which is, great. I don't think there was actually any change, so it really is kind of a no-op, actually. So no problem there.
I don't think there's anything else outstanding That's blocking this release, other than just… somebody going and doing it, so I'm happy to start working on that release, actually, after the meeting.
It will… oh, that's probably what we need to do. We need to add support for Go 125, I think, prior to the release, and then after the release, we can drop 123, so… I… God, did I make an issue for this?
Just dependencies or blocks. Okay.
I will also make an issue for this.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 08:12 Is that just an update to the docs?
**Tyler Yahn** 08:16 It's an update to the docs and the CI system. So yeah, it's very, very minor. Yeah, it essentially just starts running, actually.
The CI system might not actually need updates. I'd have to go take a look. If you're running with the SetupGo, action, you can tell it to just use, stable, and then the old stable, and so they automatically update, so it may actually be done, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 08:41 Okay. Yep.
I'm just curious, nope.
Not everywhere.
**Tyler Yahn** 08:45 Yeah, it's usually… I guess the correct answer is it's an audit of the repo to find out where we need to update, and then… and then, yeah, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 08:53 Gotcha.
**Tyler Yahn** 08:54 Yeah. But yeah, I'll… it's usually… I think what you just pointed out, like, the README is probably the only place that I would say.
We need to address that.
Okay, so I will fix that, and then try to do a release after the fact. So, yeah. It'll help, I think, also… all of our OpenSelemetry dependencies need to go get released, all of the, yeah, Go versions, so yeah, we're overdue for this, so, yeah.
Okay.
Alright, those are the only two, agenda items that I had here.
I can stop sharing my screen. Any other topics people wanted to discuss, or things that they aren't on the agenda?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 09:43 And I just wanted to ask who, anyone… I know you are going to KubeCon, anyone else? I forget. I'm week to week, and it's been two weeks.
Free, actually.
Ron, are you there?
**Ron Federman** 09:53 Meh.
Yeah, I'm probably going to be dumb, yeah.
**Tyler Yahn** 09:57 Oh, awesome.
**Ron Federman** 09:58 Cool.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 09:59 We'll see you there.
**Tyler Yahn** 10:00 Are you gonna be at the Maintainers Summit, on Sunday?
**Ron Federman** 10:05 I need to look it up, like, it's one day before the observability day, or one day before the day?
Okay, I need to… to see.
**Tyler Yahn** 10:16 Yeah, usually, if you're traveling internationally, likely you're flying in early enough, but, If you are, yeah, you should go for it. You just have to, like, it's free, but you have to be a maintainer. Register. And register, essentially. So, like, yeah, there's really no blockers, just other than you being there.
**Ron Federman** 10:35 Okay.
**Tyler Yahn** 10:36 Yeah.
But yeah, you know, I should be there as well. I will be there, that's my plan. And Nicholas, still a maybe on that one.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 10:46 No, no, I booked my tickets, sorry, yeah, I booked my tickets, I looked at the flights, and it was just like, no.
Yeah, so I'm arriving actually late on Sunday, so if you guys are maintainers gathering for some dinner activity, I'll join you, but Yeah.
**Tyler Yahn** 11:02 Okay.
Fair enough.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 11:04 But otherwise, I'll see you Monday morning, yeah.
**Tyler Yahn** 11:06 Yeah, yeah, definitely be there for that as well, too, so… Okay, yeah, yeah. So otherwise, I don't know if… do you know if Mike, Dame is coming, Ron?
**Ron Federman** 11:17 Yeah, I think it would be the Russell.
**Tyler Yahn** 11:19 Oh, okay, cool.
**Ron Federman** 11:20 I'm not sure about the maintainers today, but in KubeCon it would be.
**Tyler Yahn** 11:25 Okay.
Yeah, he's, like, you should motivate him to go there as well, but.
But yeah, otherwise, cool. Good to see you guys there. And Raphael, I'm guessing that's a no from you?
**Rafael Roquetto** 11:38 No, I… I'm gonna be in Brazil, or close to that, so…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 11:43 Family.
**Tyler Yahn** 11:44 I'm kind of jealous. Although, I guess Georgia's.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 11:47 Not too bad, but…
**Tyler Yahn** 11:48 Brazil sounds pretty great, yeah.
Yeah.
Yeah.
Well, cool. Yeah, I'm looking forward to seeing y'all there, so pretty exciting. Get a little bit of time, but yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 11:59 Yep.
**Tyler Yahn** 12:02 Well, awesome. Any other things people want to talk about?
Otherwise, we can end it early here.
Thanks, everyone, for joining. Probably I'll see y'all tomorrow morning. And then look out for the release PR and the, upgraded PR. So, yeah.
See you in a bit.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 12:19 See ya.
**Rafael Roquetto** 12:20 Thank you, bye. Bye, bye.
