SIG: Browser SIG
Date: 2026-10-22
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Maxime Quentin** 00:52 Hello, Martin?
**Martin Kuba** 00:53 How are you?
**Maxime Quentin** 00:54 Good, good, and you.
**Martin Kuba** 00:56 Alright.
Not too bad, not too bad. A little tired. It's getting towards the end of the week.
**Maxime Quentin** 01:05 Yeah, likewise.
I've just realized that there were, like, some, elections to, the hotel, like, contribution, board, or… I don't remember his name. Do you, like, participate usually, or…
**Martin Kuba** 01:31 You mean, like, the… the… the GC? The… subcommittee. It's next week. It's Monday through Wednesday, I think.
**Maxime Quentin** 01:40 Yeah, I mean, I realized that I needed to be part of a list so I could…
**Martin Kuba** 01:46 Oh, okay.
**Maxime Quentin** 01:48 Yeah, I'm not super, like, used to, all, like, organizations like this, so… I get pretty… Important to be part of, like, all those initiatives, right?
**Martin Kuba** 02:02 Yeah, yeah.
So I get… how long have you been part of the… Part of the Alto community.
**Maxime Quentin** 02:10 I think it's been, like, maybe, 7 months?
**Martin Kuba** 02:14 Okay, so this is your first time, like, seeing this alley.
**Maxime Quentin** 02:17 Yeah, yeah. For the first time, and also, I really like the fact that it is, like, a democratical, like, way of working, and, find it pretty cool. People are actually, like, doing… explaining what they're going… they're planning to do, and what are… will be their next focus and everything. It's… it's pretty cool.
**Martin Kuba** 02:37 Yeah, yeah.
Yeah, I think the GC is, The only place, like, where there are elections.
Yeah.
**Maxime Quentin** 02:48 Dang.
**Martin Kuba** 02:48 Hi, Cleo.
**Cleo Schneider** 02:53 We are in the same room today, which is a rare occurrence. Exciting stuff.
Chris, over here. Good to see y'all.
**Martin Kuba** 03:01 Good to see you.
I think people are still joining, so let's give it a couple more minutes. And we have… Two things on the agenda from people who are not here yet, so…
**Jared Freeze (Palo Alto Networks)** 04:16 Hey, everybody.
**Martin Kuba** 04:19 Hi, Jared.
Okay, yeah.
Hi everyone, If you have anything you want to talk about, please put it on the agenda. We have 3 things right now.
I think, Adi's not here yet.
So let's maybe start with, david's topic…
**David Luna Bistuer** 04:49 Okay, hello, everyone.
Well, this is something that, comes from the PR from Jared, about changing the instrumentation interface.
Which I think is good, so the, the, state machine that we have is simpler, so we create the instrumentations we enable or disable. There is another processing behind, and actually, I like the way that we are handling it with the errors, and we can throw… an error just to say that the instrumentation is enabled, and that's handled by the implementation base. But something that caught my attention was the configuration right now is… becomes static somehow. Of course, in JavaScript, you can do a lot of things, and you can do modifications.
But, kind of, it's… we're claiming that, okay, configuration should be, it's, set when the server edition, It's graded, and then, through the life of the SDK, until there is a hard reload.
Or a navigation, a hard navigation to another page, that stays the same all the time.
Just a question, so I'm not against it.
But just a question about… I wonder, don't know, do you think that's good, it's bad? Opinions, concerns, or whatever.
**Jared Freeze (Palo Alto Networks)** 06:10 I can go first, I thought about this a little bit. I guess I would want to see… like, specific cases of dynamic config, because I think it affects the lifecycle.
Right? So, if you… I think enabled, disabled is probably the easiest one to follow. So you're like, okay, set, config, disabled, whatever.
I don't think we should have two ways to do things, so I would say, okay, that's not part of this anymore, because you have an enabled-disabled command, you know, here. Okay, so what else would it be? So it would be something like…
**Martin Kuba** 06:52 Jerry, we lost your audio, I think.
It's not… it's not just me, right?
**Trent Mick** 07:02 No, I… yeah.
Is he… is video frozen now, too?
