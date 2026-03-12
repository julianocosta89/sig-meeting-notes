SIG: CI/CD SemConv SIG
Date: 2026-03-03
Duration: 8 minutes
============================================================

## Zoom Recording Transcript

**Christophe Kamphaus** 01:04 Hi, Alan. How are you?
**Alan Clucas** 01:06 I… Not commuting today, then.
**Christophe Kamphaus** 01:12 Oh.
Was done earlier this time.
Let's create a new… B?
I seize that, the other two are… Cannot join today, Adrielle and Toton.
**Alan Clucas** 01:42 Yes. Yeah, I noticed.
**Christophe Kamphaus** 01:45 Probably today will be quick.
**Alan Clucas** 01:50 Yeah.
**Christophe Kamphaus** 02:18 I'm sharing my screen if you want to put something on the agenda.
**Alan Clucas** 02:23 I… I don't have anything, I was gonna… Chase Adriel about some questions on The environment carrier stuff that is currently blocking the Go merge, I think.
I haven't actually checked it today, but since he wasn't here, I didn't check, because… He's been tagged, so he's aware of it, but…
**Christophe Kamphaus** 02:49 Okay.
**Alan Clucas** 02:50 shipping, too.
**Christophe Kamphaus** 02:51 in Slack as well.
**Alan Clucas** 02:54 He's responded, but it doesn't… it's not sort of closed out the problem. It's about whether… Well, the environment carrier keys… Should be, Guaranteed safe for environment, as in… What should you do with a key that… is, not ASCII.
Things like that, so… Yeah.
I was just doing a bit of research on whether anybody's, like, said that… Propagators should be round-trippable, which sort of feels like a thing that might be.
A requirement, yeah.
**Christophe Kamphaus** 03:41 Roundtrippable, you mean that you should be able to set it for a new process, and that one should also be able to propagate it to a new process? Is that what you mean?
**Alan Clucas** 03:53 I basically mean that if you called extract on inject.
on something, you should get the same… exact same values out of it.
We're currently… we're currently saying that… Like, you'd normally inject something called trace parent, and what you get out at the other end would be catalyzed, trace parent.
But that's more… That's less of a concern than… Characters that just don't… Travel and environment variables very well.
What should we do about them? It wasn't my concern, so, yeah, it's… Unless you've got… incite them, I don't really know.
**Christophe Kamphaus** 04:45 No, I would say… Probably it should be round-trippable for ASCII characters, at least, but yeah, others, I don't know.
**Alan Clucas** 04:57 Oh, well, it could be, but… what do we do about it? What do we want to do about it?
Should they…
**Christophe Kamphaus** 05:06 You mean…
**Alan Clucas** 05:07 Well, should the.
**Christophe Kamphaus** 05:08 Should you…
**Alan Clucas** 05:09 Or… Yeah.
Specify how to travel, transport.
Things.
In a way that ensures they are more round triple than they are now.
**Christophe Kamphaus** 05:22 when would this be useful? It's if you can specify a… Key.
If you want to say trace pound in… with emoji.
**Alan Clucas** 05:37 Yeah, this is what's, like, I'm not really sure what the, What the real problem is here, because… The keys are kind of specified.
**Christophe Kamphaus** 05:54 I guess the… Spec does leave it open.
**Alan Clucas** 05:59 Yeah.
**Christophe Kamphaus** 06:00 But, yeah, so we could… Refine the spec on that point.
But now, specifically for trace parents, they're… I'm not sure if… That should really be blocking.
**Alan Clucas** 06:15 No, that's true.
Yeah, it's, robert Pajak, because I don't know whether I'm pronouncing his surname right.
Who's one of the goat hunt trip, maintainers.
has, rays that the spec is.
Loose on this, and… It works fine for transparent, trace estate and baggage, which is what people Probably care about mostly, but…
**Christophe Kamphaus** 06:45 Yep, it's… yeah.
Could you ask on your PR?
If this is really blocking, or if you could do it in a second step after the spec is refined on that.
**Alan Clucas** 06:59 Yes.
I'll do that, yeah.
**Christophe Kamphaus** 07:07 Yeah, so white.
Just took a quick look on our board, and I don't see anything.
Having changed, nothing new, so… I think we are good.
Unless you have something to discuss.
**Alan Clucas** 07:22 I don't, no, thank you.
**Christophe Kamphaus** 07:25 And it's a quick one today. The next two weeks, I'm not sure if I can make it.
It's always, when the time shifting occurs, there's one or two weeks where The usual times are off in Europe.
**Alan Clucas** 07:42 Yeah, I'm in Europe. I'll ask to shift the other meeting that I've got.
Slightly earlier in the day. In fact, I'll shift it, because I'm mostly in control of it.
Yeah.
**Christophe Kamphaus** 07:55 All right.
**Alan Clucas** 07:56 I will see you if I see you, or not if I don't.
**Christophe Kamphaus** 08:00 Yep.
**Alan Clucas** 08:00 But you can click on…
**Christophe Kamphaus** 08:02 Yes, I will come.
**Alan Clucas** 08:04 I will see you there, then, if I don't see you in a meeting.
**Christophe Kamphaus** 08:06 Crossing us, we'll see each other's there.
**Alan Clucas** 08:09 Alright.
**Christophe Kamphaus** 08:10 By buying.
**Alan Clucas** 08:10 Bye.
