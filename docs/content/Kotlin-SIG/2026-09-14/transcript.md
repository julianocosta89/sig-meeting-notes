SIG: Kotlin SIG
Date: 2026-09-14
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Jason Plumb** 00:28 Hello, hello.
**Hanson Ho** 01:00 Hello?
**Jamie Lynch** 01:03 Hold on.
**Jason Plumb** 01:10 In the interest of transparency, I will continue to say that I have extenuating circumstances over here, probably for the next few weeks, that are really limiting my ability to contribute to the community correctly.
And for that, I'm sorry.
**Hanson Ho** 01:32 I always have that excuse, but also, mental, neurodivergence, and the inability to concentrate on too many things at once.
**Jason Plumb** 01:41 Yo.
**Hanson Ho** 01:42 I play Matt, actually, more.
**Jason Plumb** 01:46 In my case, it's strictly, top-down project priority stuff.
**Hanson Ho** 01:53 Who's that too, that you know?
I can always find a way around that sometimes, but my brain is, is, It's a tougher one.
**Jason Plumb** 02:03 I get it.
Yeah, the other challenge is, like, this stuff is also, like, really interesting compared to some of the other stuff, so… I'd rather be hacking on Kotlin.
**Hanson Ho** 02:40 Have we heard back from, the Kotlin folks, speaking of Kotlin, about, or JetBrain folks, I should say, about, Because I created that issue, and I pointed it to them, and I hope I did anyway.
I don't remember if they have… yeah, I'll just put it in one thing.
**Jamie Lynch** 03:06 Booming.
I've not seen anything, and I don't think they've… Had anyone… I don't think anyone from JetBrains has attended in the last few weeks, at least.
Do you know what the… where that was left… Where it was left at. I think I've basically missed all that.
**Hanson Ho** 03:33 Yeah, I created an issue and pointed at some general questions, and I sent it to, the person who was attending, and they said, oh, my colleague, is looking at stuff with OpenTeleventry, I'll forward it to them, and I don't recall… I think I… and I missed, like, the meeting after, or something like that, and I don't recall, where that was. I can find the issue that I created, and kind of follow… follow that thread again, and see where it lands.
I guess.
Yep.
I'll search the notes, to see if there are references to that.
**Jamie Lynch** 04:22 Cool.
I can also take a look and see if there's someone we can tackle, maybe, like, send an email to follow up on.
If you felt like that was… Enough interest on their side.
**Hanson Ho** 04:37 Yeah, well, it should be in the meeting notes somewhere. I can ping them.
I feel like, yeah, July, August was a bit… well, I mean, it was July, August, so, there was a lot of stuff going on, and I probably should have followed up earlier.
**Jamie Lynch** 04:58 Cool.
Oh.
We can fill out now, I guess.
**Hanson Ho** 05:03 Yep.
**Jamie Lynch** 05:03 Okay, feel free to add stuff to be addenda.
As we go, one thing I was gonna say is we should… probably consider a release this week. Let's see when it was last released.
Yeah, so the last release was about a few weeks ago.
And… In the process of opening a PR for OpenTelemetry Android, I noticed that there's not a way to override the clock instance.
Which normally wouldn't matter, but in OpenTelemetry Android, we're supplying a Custom clock, so it'd be nice to… ship that, and kind of unblock.
**Jason Plumb** 05:58 Did you find that when you were kind of prototyping some… usages of the Kotlin API?
**Jamie Lynch** 06:05 Yeah, I can show you the… PR, so basically… I think it goes in this one.
Possibly the old…
**Hanson Ho** 06:21 There's a… yeah, a couple of them, right?
**Jamie Lynch** 06:24 I think it's this one.
Yeah, so it was basically flagged up with this comment that… Basically… But just due to the way that interface works in OpenTelemetry Java, there isn't a way to get the clock instance.
So… Open telemetry Kotlin have been assuming, but we're just using a default instance.
So, it's just a case of adding a parameter to supply the correct instance there.
**Jason Plumb** 07:04 Cool.
That's another public API service point, though, right?
Which is probably fine.
**Jamie Lynch** 07:13 Yeah.
**Jason Plumb** 07:14 Yeah.
That's cool.
Yeah, it makes sense. That would be a good thing to have to be able to integrate with.
**Jamie Lynch** 07:26 Cool, so… yeah, I can aim to do that sometime mid-week, unless… Yeah, unless anyone else has capacity, which it sounds like… It's… not true, right now.
**Jason Plumb** 07:42 Ari…
**Jamie Lynch** 07:45 Oh, that's fine.
And… was there anything else that we needed to ship in that release?
I don't mean…
**Jason Plumb** 08:03 there's.
**Jamie Lynch** 08:03 bang.
**Jason Plumb** 08:05 Well, the couple of things that were very close to being stable, have they completed their stability yet? Like, are we still gonna publish them with alpha?
**Jamie Lynch** 08:13 So, yeah, I guess that…
**Jason Plumb** 08:16 It's all within one API module, right?
**Jamie Lynch** 08:19 Yeah, so we've got the baggage API and the context API. I guess it depends on whether What we feel like we can… mock those interfaces as not having an experimental API,
**Jason Plumb** 08:36 Oh, right, yeah.
**Jamie Lynch** 08:39 And that kind of depends on the propagators, which I've been in the process of, like, moving them out to a… separate module, it's just taking a while to kind of, like, unpick from the OpenTelemetry interface.
**Jason Plumb** 08:54 Okay, so it's a little farther out than probably will be in this release.
**Jamie Lynch** 08:59 Yeah, I think so, but I'd hoped to… Have it in the next one.
**Jason Plumb** 09:04 Cool.
I just wanted to mention it in case we were close enough to try and get that in, but it sounds like not, and that's fine by me.
**Jamie Lynch** 09:13 Yep.
**Hanson Ho** 09:14 We could have another one in a couple weeks. It's… time will pass, sooner, or quickly, or more quickly than we know, so…
**Jason Plumb** 09:21 Yup.
**Jamie Lynch** 09:27 Cool. Did anyone have anything else that we wanted to discuss?
**Jason Plumb** 09:39 I don't.
**Hanson Ho** 09:44 The client-side semantic convention repo is… is… should be… we should be adding stuff later, which should depend… which might affect what repos we pull in, eventually, here, to generate stuff. Wait, no, this is an Android. We don't use it. Never mind. This is the other one.
Nevermind, forget… just redact the last 30 seconds.
**Jamie Lynch** 10:08 Hmm.
Okay, cool. Well, if there's nothing else that folks want to discuss, then we can all get a bit of time back.
**Jason Plumb** 10:26 Cool, cool.
**Hanson Ho** 10:27 Cool.
**Jamie Lynch** 10:28 Cool.
Thanks, everyone.
**Jason Plumb** 10:30 Dang.
**Carlos Alberto Cortez** 10:31 See you.
**Jason Plumb** 10:32 Bye.
