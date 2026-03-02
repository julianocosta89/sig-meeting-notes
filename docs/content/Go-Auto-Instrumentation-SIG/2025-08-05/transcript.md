SIG: Go Auto-Instrumentation SIG
Date: 2025-08-05
Duration: 13 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn** 01:00 Hey, Ron.
**Ron Federman** 01:04 Hey? How's it going.
**Tyler Yahn** 01:07 Going? Well, how about you?
**Ron Federman** 01:09 Yeah, same.
**Tyler Yahn** 01:11 Yeah.
**Ron Federman** 01:11 Usual stuff.
**Tyler Yahn** 01:14 Yep, yep, just usual.
What's up, Mike?
**Mike Dame** 01:19 Hey? How's it going.
**Tyler Yahn** 01:21 I was just wearing that shirt yesterday.
**Mike Dame** 01:23 That's a good shirt.
**Tyler Yahn** 01:25 Yeah.
How'd your backyard barbecue go, Mike.
**Mike Dame** 01:35 It was good. We actually had some nice weather. I was telling you guys how we've never had a good
good weather for an event. So
yeah, we'll had a good time. That's that's our son. Yeah, a lot of people other kids from to play with and stuff. So it's fun.
**Tyler Yahn** 01:51 No, it's great. I that's yeah. It's such weird to say that in August you wouldn't have good weather. But you know.
**Mike Dame** 01:58 Yeah, it's it's like, it's always either like 90% humidity and boiling hot. Or, you know, rainy and still hot and humid somehow. So there's just just a nice day, and it's it hasn't been too bad this week, either, so enjoy the nice weather here while we can.
**Tyler Yahn** 02:17 Yeah, yeah, I know. Right? And then almost right around the corner is fall.
**Mike Dame** 02:22 Yep, the rainy season.
**Tyler Yahn** 02:25 Yup, yup.
well, cool we could probably get started here in just a second. I will start sharing my screen. I don't know about attendees. I haven't added my name, but if you want to add your names any agenda items you guys want to talk about.
I added. One thing. It's pretty light right now. But
yeah, I think we can. We can jump in here in just a second
cool. Alright. So the only thing I wanted to talk about was kind of just like next milestone. So next release we're, I think, probably a month out from a release at this point.
Yeah. So,
yeah, I just wanted to like, kind of see and get a little plan together as to like what we're planning to include in this next release. Looks like there were some things that like I slipped through my priority queue. So I wanted to reprioritize. And so just maybe just do a review here in case others wanted to.
So
the thing I'm looking at, I think we can just maybe talk about this. This support is 0 code configuration for resource detectors. This is something we talked about as an enhancement a little while ago. The idea that was proposed is very aws specific here. But there's been a release upstream for using
this contrib auto detect functionality. So I'd like to incorporate that into the the code base here. So I've assigned that to myself. So I'm hoping to look at that in the next day or 2. So looking to take that on.
For what is also on here. So we also have.
How does append item to slice, handle the go, Gc, making the span cons, the marking for the span context. So I think this has something to do with the trace context mixups. Right? Nicola, if I remember correctly. Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 04:27 Yeah, this was the.
I think this is the crash reported by end user. And we believe this might be the the cause.
**Tyler Yahn** 04:36 Yeah, okay, is this still something we're planning to try to get done in this next release.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 04:46 I certainly won't have time to work on this because August I'm here for another week, and then I'm off.
**Tyler Yahn** 04:55 Yeah, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 04:56 So I can't touch this until September. But September I'm going to look into.
**Tyler Yahn** 05:02 Okay, so just based off of that, I'm gonna take you off the assignees just in case other people wanted to work on this. I'm not saying they shouldn't. But and then I think what we can do is we can also
Oh.
we can create a new milestone for the subsequent release. It won't. We'll bump it out of this release, at least, and so it'll be there. We won't lose track of this is kind of the idea.
So okay.
then, also, then I guess others on the call. If you're interested in trying to resolve this, please take a look. And we can. We can. We can always move it back into this milestone if you're looking to get this otherwise, in the next month, you know, looking for owners
on that note. Then, Nicola, you also own the ob integration. Phase one the unify, the Ebpf. So you're you said you're leaving in a day or 2. Right?
You're muted. By the way.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 06:03 Yeah, sorry about that. Yeah, I'm I'm leaving in about a week, and I'll be gone for the rest of August. So, and in this week. I got a bunch of things to hand off, and yeah, I won't have time to work on this year.
**Tyler Yahn** 06:17 So I'm going to do the same thing here. I'm gonna bump this into the next milestone. I think this one I might be more interested or more capable of looking into than the other one. So I think I might try to pick this up as well in that timeframe.
No promises. But yeah, like, I think this is, this is an important one, so that we try to get some more eyes on it. But yeah, I mean, let's
reality is reality. I want to make sure you don't feel burdened while you're gone as well getting this done. So yeah, so yeah, okay, we'll we'll do that, and I think you've also laid out a pretty good understanding of like timelines, and what you plan to do. So this is great. I think this is a great handoff, so
are there others, I mean, if anyone else is also on the call, wants to look into this.
please feel free to jump on as well, but I imagine in like the next week or so, I might have a bandwidth to take a look, and so I'll take a look at them.
Okay?
Grpc, client, trace id mixup. This is an issue, I think.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 07:24 Hi, I believe it's this one.
Yeah, this is actually, we can copy the code from Ob for this.
**Tyler Yahn** 07:35 Oh, really. Okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 07:37 Yeah, this is fixed in ob, we could maybe port it. I just have to find a change.
If you're.
**Tyler Yahn** 07:44 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 07:44 I can do that.
**Tyler Yahn** 07:46 If you could do that, that'd be great. I have no problem porting the the change. If you already have a fix.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 07:51 Yeah, the sporting Novi. I think they were waiting on here because the actual author of this issue was, we kind of asked them if they were interested, and they said they were. But there hasn't been much movement, so
they open the same issue in Bayla and
forget. There was before this donation after. I don't quite remember.
I think the same issue was opening bail. That's how we got got to it.
yeah, I'm gonna have to find the change. It might be in the Baylor repo, but it's all open source, anyways. So.
**Tyler Yahn** 08:35 Okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 08:36 There might be more stuff. I'll I'll point you exactly the code.
The reason is like there might be more changes in the ov repo than necessary for this to be working here, because
will be does support generic http. 2 as well. So the same bug existed there.
But you don't need the Http 2. You just need the Grpc.
**Tyler Yahn** 09:01 Okay, yeah. I think that makes sense.
I think that I should be able to
follow through that change and then
copy it over as well. So yeah, if you can. If you can just post the change, I'm happy to to do that porting. That sounds great.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 09:15 Yeah, I wrote it down. Yeah, I'll find it for you.
**Tyler Yahn** 09:21 Okay, talked about this, Ron, you've opened this issue for the other arch Stubs. I don't know
if you have any bandwidth. Is this something that you could try to get a Pr. For.
or or others on the call.
**Ron Federman** 09:38 I think I can. I don't fully remember like what was in the that Pr. Can have a look.
**Tyler Yahn** 09:47 Yeah, yeah, sure.
Github is also not happy earlier. So hopefully, it stays working. I think it had to do with like these things here where? Yeah.
I think there's just code that doesn't compile
is is what the ticket is for. I think also similar here, like this perf other. Oh, no, this is a different thing. This was, this is something we didn't want to have that. And then I think, maybe this.
yeah, like they get CPU. So just like, yeah, this other thing
based on my understanding of what you wrote here. This is what I was guessing.
**Ron Federman** 10:33 Yeah, I can. I can do it, you know.
**Tyler Yahn** 10:39 Cool. I will. I'll sign it to you then, and I'll pull this off of a lot of
a lot of sites that scrape that. Okay, cool. Then, last, one is standardization of C formatting.
I was looking at this one as well. I had added it a while ago.
I was hoping to try to also accomplish this. I was also hoping Raphael might be at the con this today, because he's been working a lot in this, and thinking the Ob space as well. So I wanted to sync with him. But.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 11:13 Yeah, he apologizes. He messaged me before the meeting. He's got to take his wife somewhere, so.
**Tyler Yahn** 11:19 Yeah, yeah, no apology needed. That's fair. Yeah. So I I no worries. I. I can also try to take a look at this. But I imagine within a week's time I'm not gonna get everything else done. So
hopefully, I'll talk with him next week about this. I'd like to get tooling as well as like, you know, linting and that kind of stuff set up. So that's kind of the idea. But
for right now, I think keeping it in the milestone seems reasonable and something we can accomplish in the next week or 2. So yeah.
oh, okay, cool. That's all that I've got for this milestone. I did go through quickly and picked up my favorites, but I don't know if any other people have open issues that they wanted to include in this milestone that they're looking to try to work on.
If you do, go ahead and shout them out.
Okay, so if not, or if you find them later. Obviously, you can add them
to people on the call. And if you're watching the recording, go ahead and comment on there.
If you wanted to add it in this next milestone? We can. We can make that happen.
Okay, cool, that's all I had for the agenda. I think that was productive. I can stop sharing my screen here. Any other topics people wanted to discuss.
Cool. Alright. Well, if that's the case, we can end early here. I got some prs to go make so yeah, happy to have the time back. Alright. Everyone good seeing you. Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 13:10 Good to see you, too.
**Tyler Yahn** 13:11 Nicola. I'll see you in a month, but otherwise I'll see everyone else in a week.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 13:14 Yeah, I might be here next week, I to see. But I think, yeah, my last day is Wednesday next week, so I think I'll be here for Tuesday. Yeah.
**Tyler Yahn** 13:22 All right. Well, then, I'll see you all in a week's time.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 13:24 Alright, bye-bye.
**Ron Federman** 13:26 Alright!
