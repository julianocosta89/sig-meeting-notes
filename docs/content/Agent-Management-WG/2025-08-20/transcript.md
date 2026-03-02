SIG: Agent Management WG
Date: 2025-08-20
Duration: 8 minutes
============================================================

## Zoom Recording Transcript

**Jack Peterson** 00:56 Hey, Evan, how's it going?
**Evan Bradley** 01:00 Hey there.
Funny seeing you here.
**Jack Peterson** 01:03 Right, I figured, well, I'm doing some work around…
you know, remote management and op-amp, so I wanted to get more involved with the SIG.
**Evan Bradley** 01:13 Cool, glad to have you.
**JM Juande Manjon** 02:01 Hi guys, this is Wandi. This is the first time joining to this meeting.
**Michel Laterman** 02:10 Loam.
**Evan Bradley** 02:14 Do you have a link to the, … The agenda?
Or the, the….
**JM Juande Manjon** 02:20 Yes, I do, huh?
**Evan Bradley** 02:22 Great.
We'll wait a few more minutes and see if anyone joins, and then, kick it off here.
Okay, 3 minutes after the hour, so I think we can probably kick it off here. …
I've got the only agenda item right now. This is just an FYI.
These are two supervisor PRs that have been open for a while, but I'm hoping to get to them soon. I was just…
Putting them here in case anyone wanted to take a look before… before they go on, in case you have any opinions on supervisor observability.
no… further notes on these. So, …
Anyone have any other topics they would like? I've got the only item on the agenda right now.
**Michel Laterman** 04:31 Oh.
Not really, but I… I'll make an issue, and… Go ahead and implement the… CA distribution mechanism that…
we thought of, and I… originally had in the TLS.
settings spec change that we decided to strip out, because it was…
Out of scope, and we didn't have any mechanisms to indicate failures, but…
Now that all that's done, adding…
CA distribution should be pretty straightforward.
Cool. So there'll… there'll be something I do in the coming weeks.
**Jack Peterson** 05:12 Was there a RFC or anything that I can read and get context?
**Michel Laterman** 05:16 … Yes, but… the goal is to make an RFC. It was originally included in The spec change for…
Ring TLS connection settings.
**Jack Peterson** 05:33 an order.
**Michel Laterman** 05:34 Goddard.
**Jack Peterson** 05:34 Yeah, I'm not asking for more work, I'm just, you know, trying to get context.
**Michel Laterman** 05:39 Yeah, no, this is me announcing that I now have time to go back and do that.
To make the RFC an actual standalone item.
**Evan Bradley** 05:53 So, Jack, I don't know how familiar you are with the, layout of the op-amp repos, but basically the spec repo is where pretty much anything that would resemble, like, a collector RFC goes, and then the Go
repo is kind of where that implementation lives. Usually what we'll do is we want, like, an implementation alongside, the spec change so that we
Can, like, you know, see the actual outcome of what the spec change would entail.
**Jack Peterson** 06:19 Right, if that makes sense.
**Evan Bradley** 06:21 And then that's the… the Go library is a… is the client and server implementation for Go.
And then those are implemented in the collector, in the contrib repo, in the supervisor and op-amp extension.
… And in the future, I expect there'll probably be an op-amp provider, so that you can do, …
collector configuration through OpAmp without the supervisor, but there's just a lot more involved there, so that's kind of, …
Down the ways a little bit.
**Jack Peterson** 06:52 Right. I guess I can also introduce myself, Jack, work at Datadog, been involved in, Collector mainly for the last year or so, but yeah, trying to get more involved, I was telling I've been trying to get more involved with, OpAmp, since it aligns with some of the work that, I'm doing here.
**JM Juande Manjon** 07:13 Okay, maybe it's a good time to introduce myself. So, I'm working at Intuitive Surgical here in Sunnyvale.
We are not yet in production, but in our system lab, we are collecting metrics using,
Castle receiver in a… And telemetry collector, and also we are sending
We are running the Alpan server in a kind of POC.
And we are sending… collector state to the OPAN server.
Been very interesting on custom messages to send
state from the medical device to the OPAM server.
But I would like to, step by step, to start collaborating, assume maybe fixing some bugs, and see what I can have.
**Evan Bradley** 08:00 Cool. Glad to have you.
Okay, I think that's, it. I think it's a short meeting today. So, thanks everyone, and I'll, hopefully see you at the next one.
**JM Juande Manjon** 08:19 Bye.
