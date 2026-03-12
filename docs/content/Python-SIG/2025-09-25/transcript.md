SIG: Python SIG
Date: 2025-09-25
Duration: 20 minutes
============================================================

## Zoom Recording Transcript

**Riccardo Magliocchetti** 04:32 Sorry, hello, everyone.
**Sergey Sergeev** 04:34 There you go.
**John Scancella** 04:35 True.
**Riccardo Magliocchetti** 06:27 Hello again, welcome to this week's Python SIG recall.
And we'll wait a few more minutes for more people to join. In the meantime, please add yourself, As an attendee to the… Notes.
And also, if you have any topic, please feel free to welcome.
Okay, I think we're gonna start, I guess.
This one will be, like, a quick one.
The first topic is from me.
And… I opened up VR some times ago.
on changing the logger emit interface, and adhering to the style of APIs we have already in… in the OpenTempt API.
And… this might be interesting for people writing Jenai.
semantic question, Gene Instrumentations?
And Dylan raised a concern about, do we really want to deprecate the interface with just a log record?
Yeah, I was waiting for, someone else.
To have an answer.
Like, my heart?
will, say, probably, no, we don't, but, like, I'm not sure we want to maintain the double interface in the future, so… I like… This is the right moment, we want to duplicate something.
But yeah, probably, like… We can ask the other maintenance and see.
What they think.
And, yeah, like, you can, like, handle this offline.
And the other thing is that I added support… I, I added, RST check in the pre-commit, and that means that, we will catch at, CI time.
When we have, like, issues in the… documentation files, or in the READMEs?
This is helpful.
For us, because… Sometimes, like, the release… failed because, PyPI, the Python registry, is validating, these files, the READMEs.
Sometime it wasn't correct.
And so, yeah, just, if for approval in the core repo, please take a look and approve so we can also cover I call, because I contribute… I merged, I contribute changes this morning.
**Dylan Russell** 11:25 One question about this, does it auto-format the It seems like it raises issues, but doesn't, like, auto-format the file for you.
**Riccardo Magliocchetti** 11:34 Nope, this is just, like, validates and print warnings.
**Dylan Russell** 11:41 Okay.
It's kind of annoying, but… I guess better than the alternative of just badly formatted file.
**Riccardo Magliocchetti** 11:50 Yep.
Yeah, like, it's not, like, rough where you… You have a formata? Or is it just, like, a checking in?
**Dylan Russell** 11:59 for issues.
Yep.
**Riccardo Magliocchetti** 12:08 And, yeah, this was the last topic, so… Anyone has, something to discuss?
**Keith Decker** 12:17 Dylan, I just made a change to that, that PR about the Gen AI utils to get rid of the generator concept for now, while we work on that proof of concept that we talked about yesterday, so if you want to just go take a look at that, that'd be great.
**Dylan Russell** 12:32 Sure.
**Keith Decker** 12:37 Sorry, last minute change. I should add it to the topic. Thank you.
I'll add the link there, Ricardo, so…
**Riccardo Magliocchetti** 12:47 Thanks.
**Dylan Russell** 12:47 Yeah, I… also have a PR in Contrib, which… I think it's pretty much ready to be merged.
I can drop a link to it in a sec.
Yeah, I guess the ask is for Emilio or Ricardo to take another look at it, and…
**Riccardo Magliocchetti** 13:19 Okay, is the credential one.
**Dylan Russell** 13:22 Yes, yeah.
**Riccardo Magliocchetti** 13:25 Okay, yeah, I can take a look.
But do I fear, Eve.
Sorry, sorry, go ahead.
**Dylan Russell** 13:55 I was just gonna say, I think… Last meeting, we talked about merging one of my… PRs to… Move one of the instrumentations off events.
Because we're planning to, like, eventually deprecate the event stuff.
But I think… Yeah, I guess we should decide on your thing with… If we want to let logger.emitlogRecord stick around.
**Riccardo Magliocchetti** 14:26 Yep.
**Dylan Russell** 14:27 Like, I was waiting for that before.
**Riccardo Magliocchetti** 14:30 Deciding on.
**Dylan Russell** 14:32 Always.
Okay.
Alright, yeah, that's all I had, I think.
**Riccardo Magliocchetti** 14:43 Thank you. By the way, like, for other people that are not… that I haven't seen this PR, I think this is the first PR that is leveraging a new system for, like, handling authentication.
In exporters, I think.
Yeah, so if you have issue with authentication, but you have to, I think, reload the… refresh the authentication.
This may be interesting for you, too.
**Dylan Russell** 15:13 Yeah, basically, like, injects auth into the exporter.
Which is useful for, like, auto-instrumentation.
into the OTLP exporter.
So… Yeah.
**Riccardo Magliocchetti** 15:35 Okay, any other topic?
Otherwise… Thank you, I'll see you next week.
**Dylan Russell** 15:48 Alright.
**Riccardo Magliocchetti** 15:49 Alright.
Bye, everyone.
**Dylan Russell** 15:53 Bye.
**John Scancella** 15:54 Thank you.
