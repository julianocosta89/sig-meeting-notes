SIG: CI/CD SemConv SIG
Date: 2026-11-10
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Christophe Kamphaus** 00:54 Hello?
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 01:00 Hey, how's it going?
**Christophe Kamphaus** 01:03 Quinn and you.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 01:04 Doing okay, thank you.
**Christophe Kamphaus** 02:29 Yeah, I saw your message in Slack. I haven't responded to the poll yet.
I will still do it today.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 02:41 Yeah, no worries. I just sent it out, like, 20 minutes ago, so no worries.
No worries at all.
**Christophe Kamphaus** 02:52 I also added Robert's message from Slack to the meeting notes.
No, he cannot make it, but if anyone reads some…
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 03:02 Yep. Good shout.
**Christophe Kamphaus** 03:03 We'll take a look at it later as well.
You also, put the… Something on the agenda? What is it about?
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 03:26 Just that I got up working time for the KubeCon talk, and then I found out that the KubeCon talk was on hold, so…
**Christophe Kamphaus** 03:33 Whoa.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 03:34 It's all good. But I do have, shared workflows instrumented.
using ENV contacts, and showing off on the deterministic spans from the GitHub receiver inside of the OpenSelemetry org.
So that's, neat.
**Christophe Kamphaus** 03:55 Yeah.
If someone wants to use it, do they have to do something… Right now…
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 04:03 no one… no one can use it because it's in a vendor, for what it shows up as. But once we have that meeting about, like, what… how do we make this stuff available for other people outside of a vendor, then people would be able to use it, yeah. From the perspective of using the telemetry, from using… The pattern, and, like, seeing a real example.
they could just look at the source code and say, oh, like, okay, I could do something very similar with, with it. Now, I can step through it if you wanna… if you wanna see it.
**Christophe Kamphaus** 04:35 Yeah, sure.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 04:37 Okay, I'll share my… my screen.
**Christophe Kamphaus** 04:39 So it's not just, People could use it today, it's just they couldn't see the telemetry in the back end.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 04:49 Yeah.
**Christophe Kamphaus** 04:51 Or Kutzer use it that way already?
Or do they need special access in order to also send out telemetry?
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 05:02 So they don't need special access, well… Let me rephrase that.
They do require a bearer token.
For OTLP, so the way this is set up is inside of… and all this stuff is gonna move once we have the meeting, is my suspicion.
But it works very similar to how, The GitHub receiver works in general. There is Cloudflare tunnels that have IP whitelisting for the runner ranges.
And then, there is, authentication via Bear TokenAuth for OTLP. So, those two things work together. Basically, and we'll… I'll show you the code here. On the shared workflows repository, there are repository secrets.
There's the GHA OTLP endpoint and the OTLP token.
Those would have to be in any repository that wants to within OpenTelemetry that wants to use this, they would have to have these secrets.
Available.
I don't know that this is how I want it to be in the complete end, but… For now, that's the way to do it.
**Christophe Kamphaus** 06:27 I guess we can discuss whether those should be organization secrets.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 06:33 Yeah.
And I have wondered, too, if I should just build a component that is, that uses, some type of OIDC federation.
So that we can have ephemeral tokens instead of long love secrets, based off of identity. That would be my preferred path, but, It is what it is, I'll just put it that way.
So, basically.
**Christophe Kamphaus** 06:58 how that would work is, it would take the identity of the CI job itself to get an ephemeral token.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 07:06 Yeah, and then if that… if that was an allowed identity, then we'd be good to go.
So, this right here… Is the job, the workflow that runs.
And, let me just zoom in a little bit here.
So we just set for the on-queue, we just set, some different… Values, environment values.
So, this is the main section here, where we're, like, We sent the step name, the run ID.
This step name is set so that we don't have to look it up, because it's not, like, available as an environment. It's, like, not available to the environment, so we just reset it.
It's… it's one of those, like, GitHub oddities.
We enable the feature flag for OTEL enabled, because the scripts themselves have a feature flagged, so that not everybody has it turned on by default.
Then we set the endpoint, the protocol, and the headers.
with that, secret. And then we just, run this little script that gets the GitHub trace parent, and creates that deterministic ID according to the way the GitHub receiver does it.
And then we just run the Python 3 script.
and a Python 3 script, because this is exported as a trace parent, the Python 3 script just… uses the SDKs for Python, ANV contacts the NV carrier, and gets that, and then sends out the traces.
And so we can see an example of that, probably.
Yeah, so right here, these are the normal ones. It's small. Alright, let me zoom in.
Is that better?
**Christophe Kamphaus** 09:03 Yeah, it's pat on.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 09:04 So these are the pull requests dashboard, huge rain job.
we can see, you know, all of these steps that look, you know, what we would normally see with the GitHub receiver, but then we can see here that we actually have, like, a draincube.py, and then these different, scripts that run in tandem with that, and all have EMV context propagation, with them.
So…
**Christophe Kamphaus** 09:27 Oh yes, that's really nice.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 09:29 Yep, and we can see, like, you know, the errors and all that stuff, like, where it failed, why it failed, it's just not, you know, as generic as before. So, and then, of course, we get all the other good stuff that comes with, attributes.
Tells us the revision, even on the lowercase stuff, and all that. So, that's… that's it!
So, we got…
**Christophe Kamphaus** 09:51 noise.
So, for now… my impression is that it's still pretty much manual. You need to add those environment variables yourself to any steps that needed.
Any thought about, making an… I don't know how it works with GitHub Actions.
Something you can reuse.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 10:17 Yeah, I mean… We could write a shared workflow that just… Does that for you, or an action that does it for you.
And that action, would be able to create those IDs and inject them into the environment automatically, and then you can just use the action as a wrapper.
That would be one way.
The best way would be that GitHub just injects those things for us. I'd no longer have to use events or anything like that, we can just put…
**Christophe Kamphaus** 10:47 Yeah.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 10:47 once that happened So the main way would be, like, creating an action that's published that people would be able to use.
But I just wanted to showcase an example of it first.
Similar to the… it'd be, like, similar to the run with telemetry action, right?
**Christophe Kamphaus** 11:04 Yeah, I was thinking of that one.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 11:07 Yeah.
That's, that's probably one of the best ways to make it easy for people to get.
**Christophe Kamphaus** 11:23 Yeah, really cool.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 11:29 That's… all I got for my update.
**Christophe Kamphaus** 11:32 Yeah, San, let's see, next week, if we can discuss it in a bigger round.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 11:42 Okay.
**Christophe Kamphaus** 11:44 I don't have anything else for now.
There was still the point on my side to discuss the long-running events in SemConv.
how to move forward, sir. It's still on my to-do, but this week, SemConv meeting was canceled due to KubeCon.
So, hopefully next Monday.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 12:14 Cool.
**Christophe Kamphaus** 12:15 On white?
See you next time!
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 12:18 Alright, take care.
**Christophe Kamphaus** 12:20 at all. I don't.
