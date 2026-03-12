SIG: RPC Sem Conv Stability SIG
Date: 2026-03-11
Duration: 12 minutes
Zoom Recording URL: https://zoom.us/rec/share/XlqblRQF8l9x69SPkSfdcfFQIIdO9vM7dpbgizrXrCQcuXQ03cG6ypzRTLKsCfs2.4tmTfsdfLhnYGoMD
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 03:55 Hey, Matt.
**Matthew Hensley / Grafana Labs** 03:57 Hello.
Just checking, CNCF Slack.
In case there was a cancellation I missed.
**Trask Stalnaker** 04:06 Yeah… I don't see any posts there.
Yeah, so let's just, let's just do a quick, status update on prototypes.
I think the Java one is…
For the most part, in the same place.
as last week, I've got two draft PRs, one of them…
I almost have out of draft.
So this is… these are for more, though, the advanced features, like the capturing
Unknown… gRPC capturing unknown requests.
**Matthew Hensley / Grafana Labs** 05:01 So the method underscore original stuff.
Which we didn't.
**Trask Stalnaker** 05:07 Previously have instrumentation coverage.
We just didn't capture.
**Matthew Hensley / Grafana Labs** 05:24 Well, it seems I, by not choosing the gRPC stuff, may have been correct, considering…
Seems we need to have another meeting, but I haven't worked much since our last meeting on the WCF.
metrics anymore. We had a hackathon week, so… Don't pan.
**Trask Stalnaker** 05:45 Cool, cool.
Yeah, I have not heard…
back from the GRPC folks, so…
Yeah, we'll… I'll have to follow up on that.
**Matthew Hensley / Grafana Labs** 06:06 Yeah. Alright. We'll see what happens there,
My issue right now is I have the implementation mostly done, it's just… testing… The different scenarios, since it's…
An older framework, and…
Definitely requires Windows and occasional, like, actual integration testing with the web server, so it's, yeah.
Things like the, like, unknown method and falling back and all that, it's…
Yeah, having to read some old documentation to make sure you understand the intents.
So…
**Trask Stalnaker** 06:43 Cool.
**Matthew Hensley / Grafana Labs** 06:47 Alright.
**Trask Stalnaker** 06:48 Well, let's just keep it short, then.
**Matthew Hensley / Grafana Labs** 06:54 Yep.
Guess so? Don't think there's too much else?
Yeah, absolutely. See ya.
**Trask Stalnaker** 07:01 Bye.
