SIG: Python SIG
Date: 2025-12-18
Duration: 13 minutes
Zoom Recording URL: https://zoom.us/rec/share/FSNobhgaGNTNMMxHIgV__hYkMVToZR_LePAuEZaqhi8maStguIGP5lywgpHUoLhg.fWzSt9CCHuN3PKeK
============================================================

## Zoom Recording Transcript

**Riccardo Magliocchetti** 01:29 Hello, everyone.
**Alex Boten** 01:35 Hello.
**Keith Decker** 01:38 Hello.
**Aaron Abbott** 03:00 Hey everyone, how's it going?
**Emídio** 03:06 you know.
**shuwpan** 03:09 Hello.
**Aaron Abbott** 03:24 Okay, I'll, I'll share then.
Alright.
Ricardo, does your, mic work? Like, we can wait a couple minutes. It looks like we have a pretty short agenda.
**Riccardo Magliocchetti** 03:46 Yeah, I think it's working now.
**Aaron Abbott** 03:48 Yes.
Oh. Hey, Alex.
**Alex Boten** 03:55 Hello.
**Aaron Abbott** 03:57 Hey, good to see you around here again.
**Alex Boten** 04:01 Thanks. Yeah, I've been… I've been around.
**Aaron Abbott** 04:04 Yeah.
Okay, cool.
Yeah, Ricardo, do you want to kick it off? I guess I can… this PSA, I think hotel is in kind of, like, a quiet… Period for meetings at the end of this week, so… This will be the last meeting of the year, I suppose. Yep.
**Riccardo Magliocchetti** 04:31 Yep.
**Aaron Abbott** 04:32 Yeah, I guess I'll see you all in the next… next year after this, but, Yeah. Ricardo, do you wanna… you wanna talk through the next one?
**Riccardo Magliocchetti** 04:40 Yeah, so if anyone is interested, or… have a chance to take a look at VPR. I've tried to implement, in development, a tracer configurator, spec.
Part of this break.
The idea, like… I would like to have a way to enable or disable instrumentation at runtime.
And this may be the… A mechanism in order to achieve that.
Again, the spec is still in development, so, I tried to… underscore everything, but I may have missed something.
Yeah.
That's it.
**Aaron Abbott** 05:33 Okay, cool.
Was there anything you wanted to call out, like, in the implementation? It seems pretty straightforward.
**Riccardo Magliocchetti** 05:43 Yeah, like, yeah, one missing… one thing I'm still missing is that working, the setup of this via the, The configurator we have for our instrumentation.
But… Yeah, like, the general idea is that, you can pass a function that takes the tracer instrumentation scope and decides how to configure, the tracer. At the moment, only one thing is configurable, that is if the tracer is enabled or not.
And, yeah, implementing this, I also implemented, the, what the Java people call a rule-based, also the spec call a rule-based, stuff.
This is like, After, like, this is a suggestion from Jack Berg, from… That implemented the spec, and also the… the Java implementation for this.
Yeah, like, the same thing is done also in the… in the samples.
And… Yeah, so, like, this every basic thing may be, like, generalize and move the ass over.
**Aaron Abbott** 07:10 But I think it's…
**Riccardo Magliocchetti** 07:12 Since this is, again, still… everything is, like, private.
We can experiment with that.
I guess. And reiterate over that.
**Aaron Abbott** 07:25 Are we?
**Riccardo Magliocchetti** 07:26 Okay.
**Aaron Abbott** 07:27 Yeah, I guess… I don't… it doesn't seem very contentious to me, like, it's pretty straightforward, Is the role-based thing… so the role-based thing is not part of the spec for the configurator, but it is for composable samplers, is that right?
**Riccardo Magliocchetti** 07:46 Yep.
And they'll select… Now, go ahead, please.
**Aaron Abbott** 07:52 Oh, I was just gonna ask, is this part stable, the compostable samplers?
**Riccardo Magliocchetti** 07:56 I think it is, and it has been made stable, like, recently.
**Aaron Abbott** 08:01 Okay.
Cool. What were you gonna say? Sorry.
**Riccardo Magliocchetti** 08:05 No, no, it's still in development. I think you have an old version of the spec, because, like, always sample, I think it has been made… Stable on the last spec.
**Aaron Abbott** 08:18 I can load the actual GitHub page, but… Let's see if we're…
**Riccardo Magliocchetti** 08:24 But maybe it's very least the 1.53, I think.
Would be that, yeah.
We'll say night, not just yet, but…
**Aaron Abbott** 08:39 Yeah, still…
**Riccardo Magliocchetti** 08:41 Cinderella, okay.
**Aaron Abbott** 08:45 But cool. I was gonna… I was gonna ask one thing, like, do we… how do we feel about this underscore stuff? Like, do we feel like it's scaling well?
Like, for logs, we've been doing it, and then things just kind of become de facto stable.
People start depending on it and all that, and Then when we have to actually make it stable, you know, we can leave these behind as a stub, but we would rename them and people would update their code if they're calling it as part of the public API.
Do you still feel good about it, or would you want to revisit?
**Riccardo Magliocchetti** 09:17 Like… I think, in this, like, in this specific case.
This is not something that a lot of people would like to… To poke with?
So… Like, this is everything inside the SDK?
And not on the pay side, so I think a lot less people will probably use that.
And… Yeah, I don't know. Like… we can avoid to document that, maybe, in the first version. I see how it…
**Aaron Abbott** 10:02 - Yeah, I know, I know, like, one thing I've seen Java does is they have like, an incubating… They have, like, a separate incubating package, and… I think they include the implementation of these experimental features, like, directly in the actual implementation of the SDK, but then, like, the user's expected to cast the type to the in-development one, or, like, the experimental or incubating thing, so they can actually call the methods, and obviously, this is Python. You can call whatever, but, It… we could look into something like that.
Drop a link if you like.
**Riccardo Magliocchetti** 10:48 Yeah, like, I've seen that… Like, looking at the Java source code, they… I don't remember, but yeah, I've seen it.
We're not exporting, like, the symbol, but we're doing something else in order to… to call it, yeah.
**Aaron Abbott** 11:05 Yeah, or we could do, like, We could do, like, a Boolean parameter when you call getTracer, which… With, like, an overload. So… so say, for example.
If they… we have it… not here, but in the get… see, get tracer… I'm assuming you updated it somewhere.
Oh, interesting. So how does the user get… How does the user pass this, parameter?
I'm not sharing the right tab, I'm sorry.
How does the user pass this perimeter?
**Riccardo Magliocchetti** 11:45 they usually don't. It's the trusted provider will pass that.
**Aaron Abbott** 11:51 Okay.
**Riccardo Magliocchetti** 11:53 So, if you go to Get Tracer, I think… We are calculating this value and passing it.
**Aaron Abbott** 12:02 This thing, right?
**Riccardo Magliocchetti** 12:03 like, by default, the tracer provider use, Tracer configurator, but… Enables the tracers.
And so, like, you have to call, like, I think it's called, like, update, Tracer configurator, stuff like that.
Or pass a different tracer configurator when creating the trustee provider.
**Aaron Abbott** 12:29 Okay.
**Riccardo Magliocchetti** 12:30 So, yeah.
**Aaron Abbott** 12:34 Okay, cool. Well, we can explore that, but otherwise, looks good to me. I don't have any… Concerns.
**Riccardo Magliocchetti** 12:44 Okay, thank you.
**Aaron Abbott** 12:48 Cool.
So that was all we had on the agenda. Does anybody else have anything, or… Be a short meeting before the holidays.
Alright.
Well, thanks all for joining, and I'll see you… see you next year.
**Riccardo Magliocchetti** 13:11 Zero. Thanks, everyone.
**Aaron Abbott** 13:14 Thank you.
