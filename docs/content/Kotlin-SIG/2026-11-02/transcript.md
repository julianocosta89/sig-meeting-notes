SIG: Kotlin SIG
Date: 2026-11-02
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Viorel Alexandrescu** 00:32 Hey, Jason.
**Jason Plumb (Splunk Inc.)** 00:33 Hey, my background is outdated now that Halloween's over, let's see…
**Hanson Ho** 00:41 It's always Halloween in Portland, isn't it?
**Jason Plumb (Splunk Inc.)** 00:43 Every day's Halloween.
**Hanson Ho** 00:46 For some reason, you can't see me.
**Jason Plumb (Splunk Inc.)** 00:49 No, you're hiding.
**Viorel Alexandrescu** 00:51 yet.
**Hanson Ho** 00:53 What's going on?
Don't see any video… This is weird… Been sick all last week, so… my computer is sick too, I guess.
**Viorel Alexandrescu** 01:14 Seems like that's been going around a lot lately.
**Hanson Ho** 01:17 Oh, man, I was out for, like… three and a half, four days, I… I wasn't out that long for COVID.
I have no idea, and it wasn't COVID either, so…
**Jason Plumb (Splunk Inc.)** 01:28 Fam.
**Hanson Ho** 01:31 I guess you don't get to see me today.
**Jason Plumb (Splunk Inc.)** 01:35 Do we know if Jamie's joining?
**Hanson Ho** 01:38 He should be, I wonder if, yeah, I'll ping him.
He's around.
**Jason Plumb (Splunk Inc.)** 01:45 He's also got babies, so that's a wild card.
**Hanson Ho** 01:48 It's true.
**Viorel Alexandrescu** 01:50 Newborn.
**Hanson Ho** 01:52 New-ish.
Few months.
I don't know what's going on… I'll ping him.
**Jason Plumb (Splunk Inc.)** 02:20 I mean, or I can run it, there's no agenda yet, so I figure…
**Hanson Ho** 02:23 I did, like, 20 reviews today, this morning, so,
**Jason Plumb (Splunk Inc.)** 02:28 Already, that's great. Okay.
**Hanson Ho** 02:30 That's because I have an extra hour. We're on.
**Jason Plumb (Splunk Inc.)** 02:33 Oh, that's right! 10 o'clock.
**Hanson Ho** 02:36 I wonder if Zoom is confused right now, because my camera seems to be on, but nothing is being… Nothing is being.
**Viorel Alexandrescu** 02:43 What do you mean you have an extra hour?
**Hanson Ho** 02:46 Oh, so Western Canada decided not to move back to standard time.
So, Saskatchewan, I think, was always like this, so Alberta and BC, are on, basically, Denver time now, so we're… UTC minus 7, for the next 6 months.
**Viorel Alexandrescu** 03:05 When did they decide this?
**Hanson Ho** 03:07 Earlier this year, so, it was long talked about and finally executed.
**Viorel Alexandrescu** 03:16 Hello?
**Hanson Ho** 03:20 So it's gonna be weird, certain software is updating correctly, others aren't. Certain software is partially updated, and others aren't.
**Viorel Alexandrescu** 03:30 Wow.
That's gonna be a headache.
**Hanson Ho** 03:34 Yeah, for a little while, but… I'll just use it as an excuse, I'm late to something.
I wonder if… because I think… yeah, no, England switched times a couple weeks ago, so this shouldn't be different to him.
He did not indicate that he wasn't coming, so I assume… This is just, either an emergency or something,
**Jason Plumb (Splunk Inc.)** 04:03 I'm gonna have to dip in 15 minutes, regardless.
**Hanson Ho** 04:06 Okay.
**Jason Plumb (Splunk Inc.)** 04:07 Sorry.
**Hanson Ho** 04:08 Is there an agenda?
**Jason Plumb (Splunk Inc.)** 04:11 There is not. I can share. I can just… I can drop… well… If I have to dip in 15 minutes, maybe someone else should share? Hanson, do you want to?
**Hanson Ho** 04:19 I don't know what I can and can't, because my video is kind of screwed up, so…
**Jason Plumb (Splunk Inc.)** 04:24 Yeah, I'll just… I'll just do it, and then if I… Yeah. Yeah. I'm gonna have to drop as soon as they get here, though.
**Hanson Ho** 04:30 That's okay.
**Jason Plumb (Splunk Inc.)** 04:31 Yeah, I was… I was pulling up maps, because I'm like, yeah, Vancouver is, like, directly above.
**Hanson Ho** 04:35 vendors today.
**Jason Plumb (Splunk Inc.)** 04:36 And we're not in the same time zone anymore. It's real sad.
**Hanson Ho** 04:39 Oops.
**Jason Plumb (Splunk Inc.)** 04:40 Jamie's here. Okay, I'm gonna let you share. Are you… are you okay sharing, Jamie?
**Jamie Lynch (Palo Alto Networks)** 04:45 Yeah, okay.
**Jason Plumb (Splunk Inc.)** 04:46 I'm gonna stop then.
**Jamie Lynch (Palo Alto Networks)** 04:47 I just need a minute to get set up.
**Jason Plumb (Splunk Inc.)** 04:50 Yeah, no worries. The agenda's very light.
**Hanson Ho** 04:56 Is it a time zone thing for you, or, like, a last-minute emergency thing?
**Jamie Lynch (Palo Alto Networks)** 05:02 Authentication thing. We've… Switched all our authentication stuff, so…
**Jason Plumb (Splunk Inc.)** 05:09 Oh, yeah.
**Hanson Ho** 05:10 I logged on as guests. I've been logging on as guests. I don't know what to log on as, so I have to type every time, but…
**Jamie Lynch (Palo Alto Networks)** 05:20 Right. Folks, see that okay?
**Hanson Ho** 05:23 Yes.
**Jamie Lynch (Palo Alto Networks)** 05:26 Awesome.
Cool, I guess we can just make a start on the first topic, and if folks have other issues, they can add them to the agenda as we go.
**Viorel Alexandrescu** 05:41 Well, from my point, there's not much to add, it's just an update that I can continue work on the support for OTLP JSON protocol format. I think it's a mapping issue, yeah.
That I'm gonna tackle, but, anyway, my issue is with the local setup. It's… pretty resource intensive to manage to build a project locally, and because of that, the IntelliG tends to crash, so… I'll get it… I'll get it done one way or another, but I should be able to pick this up pretty soon. But that's about it from my end, not much.
**Jamie Lynch (Palo Alto Networks)** 06:20 Okay, are you able to… maybe share how IntelliJ is crashing, and… What sorts of resources you have available locally.
**Viorel Alexandrescu** 06:34 Well, it's an M1 Mac Mini with 8GB of RAM, so anytime I run a build.
it won't really do much. Like, if you remember last time when I first jumped in on the project, I ran a build on my laptop, which is the same configuration, and it took 4 hours to run it.
Yeah, it's… I mean, it's all I have for now. I can switch to something different if you guys have more potent machines, and it'll take less.
**Jamie Lynch (Palo Alto Networks)** 07:05 I was just thinking there might be, like, some tweaks that you could make to… like, the JVM marks, because I think that… Kind of assuming, but, you've got more… more of a negative fan, so potentially that might make a difference. I'm not really sure, though.
**Viorel Alexandrescu** 07:25 Yeah, I'll make a change, I'll try and do that.
**Hanson Ho** 07:29 If you could, post your, Gradle, like, upload your Gradle to Gradle Central, or whatever.
thing is called, you can analyze the build and see if it's, like, hitting, like, you know, GC thrashing or some weird stuff. Usually, 4 hours indicates that something is wrong, and either, like, reducing parallelism or tweaking JVM arcs, like Jamie said, would help.
Yeah. Built scan.
**Jason Plumb (Splunk Inc.)** 07:58 The CI builds are taken, you know.
An hour, maybe 50 minutes sometimes.
So, I mean, it is resource intensive, but it's, like, it's not 4 hours.
**Jamie Lynch (Palo Alto Networks)** 08:13 Yeah, the CI builds also have Caching disabled, which has slowed them down quite a bit compared to what they're used to.
**Jason Plumb (Splunk Inc.)** 08:25 Yeah.
**Jamie Lynch (Palo Alto Networks)** 08:27 I think one thing I would add on this is what task are you using to run the build?
I've recently added in a task that aims to just kind of, Basically.
kind of do the bare minimum you'd need for local development, and skips for more intensive stuff, unless you're on CI.
So I think the task for that would be grade all, verify.
**Viorel Alexandrescu** 08:57 I'll have a look over that.
**Jamie Lynch (Palo Alto Networks)** 08:59 Compile the code and, like, run analysis on it.
**Viorel Alexandrescu** 09:04 Most of the time, I just let Gradle do its own importing thing.
**Jamie Lynch (Palo Alto Networks)** 09:10 Yeah.
Cool.
I guess, on my side, I mean, continuing on with the propagation API changes.
I've got a proof of… concept bench, kind of locally, that's… That's it.
implementing the context storage changes that we'd want, but I've not got that to… the point where it can be reviewed yet, so I'm just… Hoping to continue on that this week.
**Jason Plumb (Splunk Inc.)** 09:52 Looks like someone just 10 minutes ago put in a, fix for, that propagator's thing.
The… sorry, the… The dropping of multiple values.
**Jamie Lynch (Palo Alto Networks)** 10:03 Yep.
That's good.
**Jason Plumb (Splunk Inc.)** 10:06 That's fast.
**Jamie Lynch (Palo Alto Networks)** 10:07 I also, did a few scans, with Claude to try and find anything that might have crept in.
Over the last few weeks, and I've opened up some issues on the repo.
**Jason Plumb (Splunk Inc.)** 10:23 Cool.
**Jamie Lynch (Palo Alto Networks)** 10:27 So I think I had one other thing, which is, I think we last released about 3 weeks ago.
So… Is everyone I gave of us releasing sometime this week?
**Hanson Ho** 10:44 Sounds good.
**Jason Plumb (Splunk Inc.)** 10:45 Sounds good to me. Naturally, after 0.9 comes 1.0, right?
**Hanson Ho** 10:51 December…
**Carlos Alberto Cortez (Dash0)** 10:53 Was it a joke or not? That's a joke, yeah.
**Hanson Ho** 11:00 We don't want to go 1.0, but… numbers and stuff.
**Jamie Lynch (Palo Alto Networks)** 11:08 Cool. That's all I had. Did anyone else have anything they wanted to share?
**Carlos Alberto Cortez (Dash0)** 11:14 Oh, yeah, Jamie, sorry, having… A little bit busy with, work stuff, but if there's anything important, like PR, specifically the propagation, for example, part, just let me know. Like, I will spend some time notes there.
**Jamie Lynch (Palo Alto Networks)** 11:33 Sure.
Yeah, I don't think there's anything blocking, but there were some changes, But it'd probably be worth just, like, reviewing on main, to get your thoughts on…
**Carlos Alberto Cortez (Dash0)** 11:48 Sounds good.
**Jamie Lynch (Palo Alto Networks)** 11:51 And, yeah, I think the context bit is the main thing that I'll probably want your input on. That should hopefully be coming within the next week or two.
Okay, awesome. Thanks for coming, everyone.
**Jason Plumb (Splunk Inc.)** 12:14 Yeah, Thanksgiving. Take care.
**Hanson Ho** 12:16 Sunday. Bye.
