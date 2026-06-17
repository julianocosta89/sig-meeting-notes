SIG: Event WG
Date: 2026-06-16
Duration: 11 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 02:57 Hey, Robert.
Thanks for waiting around for us.
**Pellared** 03:02 Oh…
**Liudmila Molkova** 03:09 Hello.
**Pellared** 03:11 Hello?
Initially, I considered to ask on Slack if there are any things discussed, because the agenda is playing, but I decided at least I will see… we will see each other.
**Trask Stalnaker** 03:26 I like how it took Lyudmil and I almost exactly the same amount of time to get from our last meeting to this meeting. I joined, like, 5 seconds before you joined.
**Liudmila Molkova** 03:39 Yeah, I'm sorry, this back-to-back is… difficult.
And my coffee basket broke today, so I'm… Hello, and…
**Pellared** 03:51 coffee maps and broke.
**Liudmila Molkova** 03:53 Yes.
**Pellared** 03:54 Always… Nightmare.
**Trask Stalnaker** 03:57 Wow, and that's not, like, priority one. You're still… Yeah, that's what I, did… always do between these meetings. Go refill.
**Liudmila Molkova** 04:22 Okay, so I… I don't have anything. I think there is a… there is a nice signal from… Lucas, who works on Python-seq to… Be interested in stabilize… in… trying out the…
**Trask Stalnaker** 04:40 Carnivor.
**Liudmila Molkova** 04:42 Yeah, exceptions. It's especially interesting in Python, because in Python, I think, is one of your, maybe the only one language that Record span events on spans that ended with exception?
Because you can kind of, like, wrap the span execution, like, with span annotation in Java, but is, more like the regular code-based approach.
Like, with this… Starts, Ben.
And, it would be interesting to see what comes out of it.
Sorry, what does pass…
**Trask Stalnaker** 05:21 Python do? I didn't quite follow.
**Liudmila Molkova** 05:23 So you can write something like, with, start span, Sorry, and it will… Start a span, and it will, catch any exceptions that happened during the.
**Trask Stalnaker** 05:37 succeed.
**Liudmila Molkova** 05:38 Yeah.
And if exception happens, it records exceptions by default as span events.
That would be extremely interesting to see, what happens, how it's handled in Python.
**Trask Stalnaker** 05:51 And so that's built into the SDK itself.
**Liudmila Molkova** 05:54 Yep.
**Trask Stalnaker** 05:56 Okay.
**Liudmila Molkova** 06:05 Yeah, I don't believe anything has happened so far, and if… Lucas has any concerns, I will make sure to… Share them.
**Trask Stalnaker** 06:21 Cool.
Robert, anything…
**Pellared** 06:26 Nothing comes to my mind.
I was formatting my machine, and I was playing off my laptop for today, so I do not remember, I was… I also formatted my brain. Probably by accident.
**Trask Stalnaker** 06:43 Roberto, are you… are you there?
Hey!
**Roberto DUARTE** 06:49 Hey, everyone. Hey, thank you.
**Trask Stalnaker** 06:51 As you can see, we're not, super, don't have a whole lot going on in this SIG anymore. We're kind of slowly winding things down, trying to stabilize last bits.
Anything, on your mind that you wanted to chat about?
**Roberto DUARTE** 07:11 Mmm… no, not really, to be fair. I, I'm following the projects for a while now, but I never decided to join any SIG reunion, so I just, I saw some light, and I… I came by, to be fair.
**Trask Stalnaker** 07:27 Cool.
Yeah, yeah, definitely check out, most of the other meetings are… have a lot more going on in them.
Probably more interesting, but yes, if you have anything event or log-specific, Let us know, we're also in the Slack channel.
**Roberto DUARTE** 07:48 Yeah, alright.
what make, this, SIG, I mean, not, talking so much, recently, though.
**Trask Stalnaker** 08:00 We've gotten most of the important… most of the stuff that we wanted to done.
We've stabilized, like, some of the basic shape around events.
And… So we're just kind of doing all… a few last things, and probably the last… I would say, like, the last big thing, at least that… in my mind.
Robert may have some others, is… The span event deprecation.
That's kind of, to me, the… the ultimate end goal.
**Pellared** 08:40 Yeah, so our current work is… mostly stabilizing these parts, which are right now in development state, and making sure we do not forget. So, it's double checking… checking the status, making sure that something does not get stale.
and not even… and I would say even not have too much work in progress, so that we are just getting, you know, the parts which are important stable right now. Because at least in my… if I remember correctly, most of the things which right now blocks us from getting rich and deprecating of span events and… What was more, recording events and spans is just stabilizing the stuff we already created since a few months.
Since the few months.
**Roberto DUARTE** 09:28 I see.
Yeah, I see.
**Pellared** 09:31 We're also working on systematic conventions, general semantic conventions for events, and it has been merged last week.
And we also haven't heard any, like, negative feedback regarding this as well.
**Roberto DUARTE** 09:47 Okay, yeah, I guess the rest of the work is more on the specific language SDKs to implement the The convention, right?
**Pellared** 09:55 But are there any questions that you have? Any concerns? Because… any issues that needs to be solved, and we are not… we are just not tracking properly?
**Roberto DUARTE** 10:06 No, not really.
It'll be fair.
**Pellared** 10:09 It's good to hear.
**Roberto DUARTE** 10:14 Yeah, I'm.
**Trask Stalnaker** 10:15 Alright.
**Roberto DUARTE** 10:15 somewhere.
stabilization of the specific SDK to… Or some developers that are waiting in it, but yeah.
**Pellared** 10:24 Any concrete language that you wait for?
**Roberto DUARTE** 10:28 I work mainly with people doing JavaScript and Java nowadays, so… mostly, mostly this one.
So, yeah, I guess JavaScript is gonna be a big one.
But yeah, yeah, nothing specific about it.
**Trask Stalnaker** 10:51 Alright, well, let's get some time back, and nice to meet you, Roberto.
**Roberto DUARTE** 10:56 Yeah, as well.
**Trask Stalnaker** 10:57 See you around!
**Liudmila Molkova** 10:58 Nice to meet you. Have a good day.
**Roberto DUARTE** 11:01 You as well?
