SIG: OpenTelemetry .Net Auto Instrumentation SIG
Date: 2026-09-09
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**eftiquar** 02:25 Hey.
**Piotr Kiełkowicz (Splunk Inc.)** 03:33 Hey, guys.
**Mateusz** 03:38 Hello?
**eftiquar** 03:40 Hey, Piotr.
**Zach Montoya** 05:52 Hey, everyone!
D.
**eftiquar** 05:57 How are you?
**Zach Montoya** 05:59 Pretty good, how are you?
**eftiquar** 06:00 All good, all good. Thank you.
**Zach Montoya** 06:03 I guess I can, get started with the agenda.
A couple of minutes past. Let me share my screen… Alright, cool.
So I don't see any main topics for today, so I'll just go through the agenda, but if anything comes up, just let me know.
In terms of open pull requests, we have a bunch of, renovate ones. I think the more interesting ones that have come up have been, so the continuous profiler.
I'm not sure, the progress on this one at the moment.
**eftiquar** 06:49 The condensed profiler, I'm working on it, I… Saw the Codex feedback, there are a couple of P1 issues, so it's been actively worked upon.
**Zach Montoya** 07:02 Okay.
Cool. Anything else needed at the moment?
**eftiquar** 07:07 No.
**Zach Montoya** 07:10 Cool.
**eftiquar** 07:12 So, I'll just, request a review, but allow me to first nail down all the outstanding review feedback.
And I'll post a comment on it, and it'll be helpful for… Your insights and inputs.
**Zach Montoya** 07:29 Sounds good.
We also have support for Quartz 4, so I think we'll just need to give this a review.
Corona Piotr, has some more changes, so… Lots of… Update that… oh yeah, major change, okay.
So that'll be separate.
**Piotr Kiełkowicz (Splunk Inc.)** 07:53 Good news, Quartz has native support for traces and metrics.
**Zach Montoya** 07:58 Oh.
Awesome.
That's good to hear.
**Piotr Kiełkowicz (Splunk Inc.)** 08:04 So… I've put information that the support for branch tree is deprecated.
I'm not sure how long we'll have packaged on the consweb site, so…
**Zach Montoya** 08:19 Gotcha, okay.
**Piotr Kiełkowicz (Splunk Inc.)** 08:20 refresher, but I've made a note that this is deprecated.
**Zach Montoya** 08:24 Got it, okay.
Cool.
We also have an IBM MQ Traces Instrumentation I haven't engaged with this one yet.
**Piotr Kiełkowicz (Splunk Inc.)** 08:38 I also didn't check, but… I've checked internally with our PMs, and… If this coach is kind of… Good quality, we should consider merging this.
We have some requests from the customers.
**Zach Montoya** 08:54 Okay, yeah, I can take a look. I know we also have… the Datadog one has an IBM MQ, so if they share any similarities, I can also… Provide a look there, and see if there's any similar, like.
Call target locations. So… I'll take a review of that.
**Piotr Kiełkowicz (Splunk Inc.)** 09:13 from the… just looking into this PR, there… I've seen some suspicious changes in the duck typing.
**Zach Montoya** 09:24 Let's see, so there's new duct types… oh, duck type methods… Yes, okay.
**Piotr Kiełkowicz (Splunk Inc.)** 09:36 So, it is kind of… Strange to me.
**Zach Montoya** 09:40 Yeah.
**Piotr Kiełkowicz (Splunk Inc.)** 09:41 fully understand it yet.
**Zach Montoya** 09:43 Yeah, this one… so there's a similar change in the Datadog repo right now, or I think we introduced it maybe… Hmm, 2 or 3 months ago.
Actually, did it get merged? I'm not sure if it got merged. But the idea is that if a type declares an implementation, but it's, an interface implementation, like the explicit interface implementation, then, just going over its own methods, won't identify it.
So you would have to, iterate the methods and do, like, a full name search.
In order to, determined that, yes, it implements that. So yeah, if any of these types, actually just declare it, not as just a general, method on that type, but a… it's supposed to interface implementation, then you would need something like this.
**Piotr Kiełkowicz (Splunk Inc.)** 10:36 Okay.
So, if so, I would kind of recommend to create separate PR for this, instead of just coupling with new… feature button, yeah?
**Zach Montoya** 10:48 Yeah, that would be ideal.
Yeah, this is pretty easy enough to break out, so, I'm sure we could… we could ask for that.
Let's see, what else we got?
It's like this one's already approved, kind of ready to go for verifying the… The bash script for the installation.
And then a small one to just… Update our… our native profiler check to .NET 8.
Very simple.
Then a bunch of renovate PRs.
Are there any other PRs that you guys wanted to… Discuss right now, or just, raise awareness for?
**Piotr Kiełkowicz (Splunk Inc.)** 11:39 NET SDK update, but nothing fancy there, so… I cannot prove it myself, and… Don't merge it, when all those are bussing.
**Zach Montoya** 11:53 Cool Alright.
So let's go on to open issues.
Let's see… done at 8 failure… I got the traces, I'll just close it out for now.
Have we responded to this one yet?
Okay.
Okay, yeah, so they have some details, but it'd be helpful to have a… Something we could deploy to… Reproduce it immediately.
Okay.
We can wait on that, and you responded… Bogiego? Okay, that's fine, we can check in again the next SIG meeting.
Let's see, and then the other one is holidays configuration… okay.
So, just creating a tracking issue.
Cool.
Is this resolved by this, or is this just related?
**Mateusz** 13:01 No, it's not resolved, I just noticed the issue in some other PR, so that's what's mentioned here, yep.
**Zach Montoya** 13:08 Got it. Okay.
Sounds good. Do you plan to tackle this immediately? Like, should we put it on a… Milestone, or…
**Mateusz** 13:17 Yes, I talked to Yevgeny, and he mentioned he might have some time, so we'll be tackling it right now. I mean, you can definitely add a next release milestone.
**Zach Montoya** 13:31 Let's put it on 117 for now.
Put this on here… Cool.
If I refresh this, that should be gone from this view, okay.
We're still waiting on this one, and then for the traces, yeah, I guess… This is tracking that PR.
Oops, we can probably listen unassign for now.
yeah, this was the issues view for milestones.
I don't think we need to share anything else at the moment.
Open discussion items, there are none.
Nothing there.
And then for the board, we'll just add that one for the file-based… It's committed… How did this Kafka one go? This one… Is this still… In progress.
Oh, I need to review this.
So, there's two things. One… We're waiting for… A stable release…
**Piotr Kiełkowicz (Splunk Inc.)** 15:23 It is already in place.
**Zach Montoya** 15:25 Okay, great, okay. So, let me… I will revisit this one.
So we can review this.
Yeah? Okay.
Cool, so that's in progress.
done it alone support, not sure if there's been any… Any adds on this one yet? Rc1 just came out, so that's pretty cool.
**Piotr Kiełkowicz (Splunk Inc.)** 15:55 Not tested yet. Last time I've checked with previous 7, and it was working without any issues.
**Zach Montoya** 16:05 Okay, we can keep updating this as needed.
Any other updates to the board?
Alright.
So we got a couple piers, I'll be reviewing this one.
And then there's another one I was gonna review as well.
Okay, cool. So that is our general agenda.
Is there any other topics or PRs you guys wanted to discuss while we're here?
Yeah?
Sounds like we're good.
Alright, cool. Well, thanks, everyone. Thank you. See you guys next time.
**Mateusz** 17:01 Thank you. See you.
