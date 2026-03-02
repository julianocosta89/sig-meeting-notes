SIG: Collector SIG
Date: 2025-07-30
Duration: 8 minutes
============================================================

## Zoom Recording Transcript

**Moritz Wiesinger** 03:54 Hello!
Shall we just kick it off and skip Antoine's points, for now.
**Evan Bradley** 04:11 I think that's fair.
**Douglas Camata** 04:13 Yeah, I think he might join soon, because I saw his cursor moving in the dock. So I think we can start.
**Moritz Wiesinger** 04:20 Oh, yeah, okay,
I'll just jump to my point, for now, since I'm right after I am finally done with my Pr. And the releases reboot to add nightly releases.
There was already some reviews happening.
but I finally moved it out of draft mode. And if if you guys want to have a look that would be great
that should really, hopefully cut down on on broken releases and stuff
and should make the process a bit easier.
I guess, handing over to Israel, for now.
**Israel Blancas** 05:14 Hey?
So the things that these days we have been discussing on different issues because we wanted to add an ottl function to do some kind of sanitization of the dB. Statements that could be added to. I don't know traces or even
things like the locks, right?
So the thing is that there are some instrumentations like the Java instrumentation
that allows you to do this in an automatic way, right? So like they implemented all the features right like
a parser for the SQL. And ready statements. So you can like mask those data right? So the idea of I mean, I created a pull request to use this directly as an Ottl function, and it was asked to do is as part of the
reduction processor. So I created a pull request this morning, right? Because I tried to get some feedback about what fields or what features do we think are interesting for doing this thing happen?
for making this happen. And and well, I just when you have some time, please take a look. It's something that we want to have
like soon, because it's causing us some trouble.
yeah. So I I would like to. I would love to have some of your feedback when you have some time.
**Jade Guiton** 07:12 We wait to see if Antoine shows up.
**Moritz Wiesinger** 07:26 I mean, his things are just announcements, anyways.
**Evan Bradley** 07:31 I I suspect he is just putting announcements in the
What do you call it? The itinerary? I don't think that he's necessarily going to actually.
verbally announce these. But
I think everybody should be just to make everybody aware that these are these are going to be stabilized shortly. Ish.
**Jade Guiton** 07:57 Alright!
**Evan Bradley** 08:10 I suppose if there's no other topics, then we can give everybody back the majority of the hour here.
**Jade Guiton** 08:25 Yep.
Makes sense.
**Douglas Camata** 08:28 Thank you, everyone.
Thank you. Bye-bye.
**Evan Bradley** 08:31 See you, everybody.
**Moritz Wiesinger** 08:32 Yeah.
