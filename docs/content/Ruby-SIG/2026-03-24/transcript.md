SIG: Ruby SIG
Date: 2026-03-24
Duration: 8 minutes
Zoom Recording URL: https://zoom.us/rec/share/w0sCMy-NnuMZGJKniDSyoriCdI38DUMtNBf2w5m2LpXfLPFIECQzcuw33EMgmy0U.Sn8_LziZstDuTWYI
============================================================

## Zoom Recording Transcript

**Robb Kidd (he/him)** 03:46 I have just opened our agenda and relearned that we canceled this week's meeting because of KubeCon.
Which doesn't mean the three of us can't have a chat.
But there's nothing, like, on the agenda for us to discuss.
Or maybe it's just me talking to myself.
We could… we could cancel, if… if… if, neither of you have anything you want to chat about.
Sure.
For my… for me, I will go back into trying to review stuff. We got a lot of stuff open, and I've got a little time, and that I can devote attention to it. So, maybe in… if not here, in… the CNCF Slack. If there's something you'd like me to look at, my attention is available.
**Xuan Cao** 04:49 Yeah, I have one, if you can, ticks sometimes.
It's commutes, so… This one is sitting there for a long time.
**Robb Kidd (he/him)** 05:02 Which one's that?
**Xuan Cao** 05:04 The auto implementation for the auto operators, I have a conversation with Ariel.
For, like, almost, a year, and… I'll get his attention again.
to see if she can move… move forward on this PR, but again, I mean, if you can show some thoughts or support?
**Robb Kidd (he/him)** 05:31 Sure, like, yeah, the more people looking at it sometimes can help.
**Xuan Cao** 05:37 Yeah, sometimes.
**Robb Kidd (he/him)** 05:39 You get now 3 different opinions, instead of, You want to talk about it? Would you like to talk about it now? What's up?
**Xuan Cao** 05:46 This is okay.
**Robb Kidd (he/him)** 05:48 Okay.
**Xuan Cao** 05:50 Basically, Kayla already approved before, so she thinks it's okay, this is… this is the whole idea is actually… The, the, the… the mechanism is actually, borrowed from the Neurotic, which is from their company, and I also take a look as well.
So, yeah. I think, I think it is… is polished. And, again, this one doesn't affect anything inside of the contribute.
Because it's like a… but you will create a new gem, you will try to release a new gem.
**But anyway, it won't affect, like, the… the country at all? Because it will be in a separate, folder, so… Robb Kidd (he/him)** 06:41 It's, this is the first time I'm looking at it, but I see some keywords popping out.
let's see if just skimming some keywords, whether I'm at least looking in the right direction to understand what this is. It's a gem that facilitates using The hotel operator.
To wire up instrumentation into, Ruby services that are running in Kubernetes.
**Xuan Cao** 07:08 Yeah, yeah.
**Robb Kidd (he/him)** 07:08 As such, it's a gem that is not itself auto-instrumentation. It's like a facilitator of injecting the auto-instrumentation that's only used in the Kubernetes, OpenTelemetry operator context, so it's not gonna go in, like, instrumentation all. It's… Xuan Cao 07:25 Yeah, yeah.
**Robb Kidd (he/him)** 07:26 Okay.
I… I skimmed it, I see what direction you're going in, and I will… I'll review it and form an opinion, too. Yeah.
**Xuan Cao** 07:35 Okay, thank you.
**Robb Kidd (he/him)** 07:39 Cool.
Arjun, do you have any, Hot topics? Things you want us to look at?
**Arjun Rajappa** 07:48 No, no.
Nothing.
**Robb Kidd (he/him)** 07:51 Okay.
then I guess we'll call it. Joan, I'll… I'll take a look at this PR now.
**Xuan Cao** 07:59 Okay, thank you.
**Robb Kidd (he/him)** 08:00 I'll see y'all next week.
**Xuan Cao** 08:02 Yeah, thank you. See you. Bye.
**Robb Kidd (he/him)** 08:03 Bye!
**Xuan Cao** 08:04 Great.
