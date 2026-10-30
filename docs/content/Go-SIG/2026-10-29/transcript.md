SIG: Go SIG
Date: 2026-10-29
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn (Splunk)** 00:33 Hey.
**Puneet Singh** 00:35 Hello.
**Tyler Yahn (Splunk)** 00:37 How you doing?
**Puneet Singh** 00:40 Good overall.
**Tyler Yahn (Splunk)** 00:43 Nice.
Where you,
**Puneet Singh** 00:47 busy… yeah, I mean, I saw the… I mean, I see usually a lot of traffic that… number of PRs I haven't reviewed, or, you know, need a review, but yeah, I'll be available more by next week, I think.
**Tyler Yahn (Splunk)** 01:03 Oh, cool. Yeah, yeah, yeah. Yeah, I mean, no worries, yeah. That sounds good. Yeah.
Yeah, definitely, it's gonna probably slow down, Next week and the week after.
**Damien** 01:15 Hey!
**Tyler Yahn (Splunk)** 01:15 with KubeCon? Hey!
Oh, dear.
**Damien** 01:19 Sorry, I'm on my phone.
**Tyler Yahn (Splunk)** 01:23 So, yeah, I mean, it's actually not a bad time there, to… taking a break there, pretty… I see David… Looks like Robert's not able to attend today. I don't know if Sam's joining either.
But, I don't… Okay.
I guess we do have agenda items. Maybe.
You're muted, David.
**David Ashpole (Google LLC)** 02:20 I pasted in what I had, but I think it's a little bit too much, so… I can… all I have is I spent some time looking at all of the 2026 goals.
**Tyler Yahn (Splunk)** 02:32 Did you want to share your screen, or did you want me to take a look?
**David Ashpole (Google LLC)** 02:38 Is it okay if I… Mmm.
**Tyler Yahn (Splunk)** 02:40 You can just paste what you had in, I'm happy to share it.
**David Ashpole (Google LLC)** 02:43 I'll paste some, okay.
**Tyler Yahn (Splunk)** 02:44 Yeah, yeah.
**David Ashpole (Google LLC)** 02:45 Let's do that.
**Puneet Singh** 02:48 Is it going to be in the chat, or…
**Tyler Yahn (Splunk)** 02:51 No, he had it in the… it's in the doc, yeah.
Okay, cool.
So, Core Exporters has one… needs second approval. There's a bunch of PRs, actually.
Actually, I don't know if.
**Damien** 03:19 Yes.
David has opened a lot of PRs in the past… Two days?
**David Ashpole (Google LLC)** 03:26 Yes.
**Damien** 03:28 Both thank you and not thank you.
**David Ashpole (Google LLC)** 03:32 Yeah.
Thank you, Damien.
Because I think Damien's reviewed a lot of them. I'll give, like, a super high-level update, and then, like.
Obviously, people can go. They're mostly small. That'll be my defense, is that they're mostly, like, 30 to 50 line fixes.
And I don't Yeah, I don't think they're too controversial, they're just things that I never had gotten around to until… past two days. So, some fixes for the Prometheus exporter, None of them huge.
But small things that I found.
Some fixes for the Prometheus Bridge as well.
And then I was able to get up.
the bound sum implementation. This is not everything wired together, but that's up.
I have the next PR for, Lockless exponential histograms, which is A circular exponential buckets implementation.
And then… I did end up merging the spec PR around the opt-in, experimental, advisory parameter, so I have an implementation of that out.
I took… went back and looked at, Go runtime metrics, and there's some small fixes for the package, like schema URLs and, Removing something that was deprecated, or the old ones that we've had around for quite a while.
And then I'd never actually added the… CPU and memory detailed attributes that we merged in the semantic conventions, so that's up.
A little rename, I guess.
And then I went through OTL RESTful and mostly copied all of the… mostly copied all the improvements that we had made to OTel HTTP, so… There was some bug with multi-part forms.
And we had also, in OTEL HTTP, deprecated the… with public endpoint.
And, this was still using, like, the really old semantic convention for, HTTP span names.
And then I have a PR out to add metrics as well, which I didn't realize wasn't even supported.
And then I found some other… I've been trying to move the… There's the timestamp section in the spec.
for how to set per-series timestamps that we added a while ago, and I thought we'd implemented, but it turns out we actually never implemented it for Asynchronous instruments.
So I have a PR out for that.
And… I have a PR out to deprecate the Open Census propagator.
**Tyler Yahn (Splunk)** 06:36 Okay, that makes sense.
**David Ashpole (Google LLC)** 06:37 some other random things, and I'm working towards… it looks like we should be able to stabilize Z pages pretty quickly as well.
I did an audit and basically didn't find much.
**Tyler Yahn (Splunk)** 06:48 Yeah.
Is that used?
**David Ashpole (Google LLC)** 06:51 In the collector, yes.
That's the only use case I know of, so…
**Tyler Yahn (Splunk)** 06:56 It's the one that matters, so, yeah.
**David Ashpole (Google LLC)** 06:59 Yep.
**Tyler Yahn (Splunk)** 07:00 Yeah, cool, alright. That looks good. Looks like there's a lot of… request for reviews here. I can get on it. This actually helps a lot in,
**David Ashpole (Google LLC)** 07:11 Okay.
**Tyler Yahn (Splunk)** 07:12 and understanding, like, what to prioritize, I've been… heads down, trying to work on talks for KubeCon, so…
**David Ashpole (Google LLC)** 07:20 Yeah, yeah, no, that's good. This is all driven… I just, like, started with the 2026 roadmap, and it turns out I signed up for a lot of things, but… You know.
**Tyler Yahn (Splunk)** 07:32 Yeah, right.
**David Ashpole (Google LLC)** 07:35 We'll get him landed.
**Tyler Yahn (Splunk)** 07:39 Cool. Let's… maybe also I could take a look at the, Pull request dashboard here as well, see if there's anything that stands out that needs maintainer attention.
Waiting on maintainers.
Quite a lot, actually.
Yeah, hmm.
This… I don't know what's going on there, but Yeah, let's maybe double-check on this. This looks like it should be ready to go.
Oh, we may just be waiting on Robert on this one.
**David Ashpole (Google LLC)** 08:23 Hmm.
**Tyler Yahn (Splunk)** 08:24 Got him.
Mr. Celeste, you… Three days ago.
Let me re-request a review on that. Okay, and then… Pss… This looks ready to go.
Any reason to not merge this?
**David Ashpole (Google LLC)** 08:50 No, let's do.
**Tyler Yahn (Splunk)** 08:51 Okay.
**David Ashpole (Google LLC)** 08:52 I think it was pretty non-controversial.
**Tyler Yahn (Splunk)** 08:59 Okay.
Yeah, and the other ones just need another reviewer, actually.
We're a cleanup.
Okay, yeah, it looks good, and then let's maybe also take a look at, contrib here.
Yeah, again… You know, the review from Robert… So… This one may be ready.
I wonder if there's a way you can figure… Can you figure the, like, number of reviews required?
for the…
**David Ashpole (Google LLC)** 09:55 No, I wish.
**Tyler Yahn (Splunk)** 09:56 Yeah.
That'd be cool.
Yeah, I think maybe…
**David Ashpole (Google LLC)** 10:04 review.
**Tyler Yahn (Splunk)** 10:05 It's just, yeah, maybe just a review from you, David.
If you'd rather take a look at this.
**David Ashpole (Google LLC)** 10:11 Yeah, I'll take a look today, probably, so… as long as we're okay waiting.
**Tyler Yahn (Splunk)** 10:17 Agreed. Yeah, let's do that.
I could probably try it as well, but Okay, cool. Yeah, that looks… that looks good.
Yeah, I've got PRs as well for the, finished stuff that David's already reviewed that needs another review, but, I just updated and it looks like it… The update broke a few things, I'm still… Trying to clean those up, but… yeah, it's not a huge rush either on that. So, yeah.
Looks like we're just looking for… looking for some reviews and some merging, as we're coming up to KubeCon. Speaking of KubeCon, I don't know if there's anything we wanted to do, I think, prior to the events in a week and a half?
I'm guessing we could try to get a release out, but there's not, like, really, like, big things that we'd be announcing in that release.
I guess, David, you're on the TC, like, usually there's, like, TC updates and announcements. Is there, like, anything that stands out that we want to try to get in at the… last week here, I mean, we have the log signal as one of the big announcements we're trying to make, so… I think.
**David Ashpole (Google LLC)** 11:28 Yeah, we didn't finish the logs OTLP export, right? I think Robert found a bunch of stuff.
**Tyler Yahn (Splunk)** 11:34 No, yeah. Okay, that's…
**David Ashpole (Google LLC)** 11:37 That's fine, then, we shouldn't rush it. Just keep coming.
**Tyler Yahn (Splunk)** 11:40 Yeah, yeah.
It's just, yeah, API and SDK stabilized, though. It's just the exporter stuff, yeah.
Which is kind of the meat and potatoes anyway, so… But technically, we still haven't stabilized all the exporters for metrics, so… Oh, really? Yeah.
Yeah, Prometheus, yeah.
**David Ashpole (Google LLC)** 12:01 That, right. I mean…
**Tyler Yahn (Splunk)** 12:02 Yeah, yeah. That's the technical part of that. But, yeah, so, like, it's not, I think, super critical, but yeah.
Cool. Okay, then I don't think there's a big rush to get a, like, a release out next week, then. In fact, it might just be, like, an, after KubeCon release.
**David Ashpole (Google LLC)** 12:22 Do we want to do… have we signed up for an in-person SIG meeting?
**Tyler Yahn (Splunk)** 12:29 Not that I know of. I know we don't have the observatory this year.
**David Ashpole (Google LLC)** 12:33 We don't, oh no.
**Tyler Yahn (Splunk)** 12:36 No. Okay, it breaks my heart.
Yeah.
So, yeah, and I think that we only have, like, one day of, like, the, you know, like, the… Free, dished out, CNCF booths.
So, again, it's just, like, kind of like last time, where it's just kind of… we'll have to find maybe, like, an ad hoc table or something where we can hang out, but, yeah.
Yeah.
**David Ashpole (Google LLC)** 13:04 Cool, well, we'll make it work.
**Tyler Yahn (Splunk)** 13:06 Yeah, yeah, definitely. I mean, I'm happy to… to sync. I know… I think it might just be you and me there.
**David Ashpole (Google LLC)** 13:15 Really? Okay.
**Tyler Yahn (Splunk)** 13:16 Yeah, Robert's not coming this year.
**David Ashpole (Google LLC)** 13:18 Lots of important decisions, then.
**Tyler Yahn (Splunk)** 13:21 Yeah, right, yeah.
So…
**Damien** 13:24 Should we keep next week's bidding, or should we cancel, or move it back an hour as it is now, so that it's better for Europeans?
**Tyler Yahn (Splunk)** 13:36 I think we should keep it… Next week's not KubeCon.
**Damien** 13:42 Yeah, sorry, I meant KubeCon's meeting.
It's… oh, the week after, okay.
**Tyler Yahn (Splunk)** 13:48 Yeah.
**Damien** 13:49 Kip it, not keep it?
**Tyler Yahn (Splunk)** 13:52 That, I think…
**Damien** 13:54 I'll be there.
**Tyler Yahn (Splunk)** 13:56 then, yeah, I guess we can keep it. I guess it's up to you and Robert, and if you are all wanting to…
**David Ashpole (Google LLC)** 14:03 trailer night that are gonna.
**Damien** 14:04 I mean, if it's likely there are going to be two maintainers, let's skip it.
**David Ashpole (Google LLC)** 14:10 Okay.
**Tyler Yahn (Splunk)** 14:10 Yep. Okay.
Well, cool. Yeah, any other topics folks had that they wanted to talk about?
I guess maybe just a call out, like, start thinking about goals for the 2027, year.
It's, sounds like it's far away, but… all the vacations coming up, like, January's kind of mixed up.
**David Ashpole (Google LLC)** 14:39 I think, just stabilized, so…
**Puneet Singh** 14:42 Yeah, those semantic conventions. That was, like, a surprise for me as well.
**Damien** 14:49 It's a side thing, it's a side thing, but I'll be off from mid-December to mid-January. So the two weeks of, like, the two usual weeks of vacation, plus the week before and week after.
A month.
**David Ashpole (Google LLC)** 15:05 Yeah, things slow down at the end of the year anyway, so I wouldn't… yeah, but thanks.
**Damien** 15:10 I know, it's just that it's, yeah, double that.
I'm waiting for Tyler to say, I envy Europeans.
**Tyler Yahn (Splunk)** 15:23 No, I mean, I'll…
**Damien** 15:25 Take your time.
**Tyler Yahn (Splunk)** 15:25 At the end of the year, too. Yeah, yeah.
I won't be here.
Yeah, I mean, I do envy you, but, yeah.
Yeah.
Well, cool, alright, cool.
**David Ashpole (Google LLC)** 15:43 I guess that'.
**Tyler Yahn (Splunk)** 15:44 the case?
What's that?
**David Ashpole (Google LLC)** 15:45 Yeah.
Anything else? Quiz? We can end it.
**Tyler Yahn (Splunk)** 15:49 We can end it here, yeah.
Sounds good. Alright, I'll talk to you all later.
Bye.
**David Ashpole (Google LLC)** 15:54 See ya. Bye.
**Puneet Singh** 15:55 Nope.
