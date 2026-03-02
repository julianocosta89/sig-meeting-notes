SIG: FAAS WG
Date: 2025-11-06
Duration: 10 minutes
Zoom Recording URL: https://zoom.us/rec/share/rIuuCHGysFpFLA-N9lNDi9u0RDK4y-l9oxwVBUriEneY09vdvja8qG3qLo3sTwyV.-O_ArNSwG2Vhk6mX
============================================================

## Zoom Recording Transcript

**Tyler Benson** 04:23 Good morning.
**Serkan Ozal** 04:26 Hello, good morning.
Seems such just too far.
**Tyler Benson** 04:31 I got rid of the spot.
**Serkan Ozal** 04:35 Yeah. Everybody will not be able to join?
**Tyler Benson** 04:39 Yeah, Rory said that he is not able to join.
**Serkan Ozal** 04:42 Yep.
okay, so shall we start and have a quick call?
**Tyler Benson** 04:51 That's true.
**Serkan Ozal** 04:52 Yeah.
There are a few, I mean, other than the dependable PRs, there are a few pull requests.
I have been looking into that, like, so… anyway, let me share my screen.
Yep.
the first one is… Related to the…
taking care of the AWS Lambda and the AWS SDK instrumentation while, handling the hotel not disabled instrumentation configuration.
But the… the main motivation for… for this change is… Disabling the open telemetry.
Lambda instrumentation entirely because of the context propagation issue, and actually not the issue, but customizing the context propagation.
And… creating the… the invocations again.
By, by himself, so, the changes seems okay, but first.
But I think it might be, like, I mean, not the real fix of that, because the real issue is the…
customizing the context propagation and fixing the context propagation issue. So I am not sure that that is the correct approach, so I will be looking into that.
And… also, there are some… some other…
two PRs for the collectors, one from, related to the, logging, log format, and another one is from Rafael.
for, identity…
AWS account ID, at the collector level, without, I mean, implementing the same thing on all SDKs.
And, yeah, these are the things I will be looking into that. Also, there are, pending Thunderbolt PRs.
I will be also looking into those.
**Tyler Benson** 07:12 So my recommendation on the Dependapot PRs is, at least what I generally do, is I just leave them until I'm about to do a release, and then, like, maybe the week before, you know, I'll try and get all the Dependabot PRs merged in.
Otherwise, it's a fair bit of noise.
I mean, I don't care if you want to do them, it's fine, it doesn't hurt.
But, I don't feel like it's as, urgent.
as other PRs.
**Serkan Ozal** 07:46 Yeah, that makes sense. Yeah. And also, I mean, once we merge those dependable peers, and then there might be new ones, and also
for the users' PRs, so that totally makes sense to…
To… just to take care of them before the release.
**Tyler Benson** 08:11 Bill.
I mean, I don't think it's bad to stay on top of it, I'm not criticizing that, it's just…
Yeah. So, another thing I was gonna mention is, I had, someone from,
Oh, let's see… Splunk? Reach out to me?
Ridvik, I think that's how you say his name. He mentioned that he was interested in being involved in the SIG. I don't know if he reached out to you, but…
**Serkan Ozal** 08:49 I told them, yeah, looking forward to working with them, so…
Yeah, that would be good, because, I mean.
mostly just three of us, you, me, Andy, Rory, are joining the meetings.
I didn't see, Ivan and Max, I mean…
Especially for the magazines long time, so it will be good for having more folks in the IndyC meetings.
**Tyler Benson** 09:16 Right.
Cool. Well, good job staying on top of all those,
I know the… in general, the SIG is pretty quiet, so I… I think that's fine. I don't have a problem with that.
I just feel bad that I don't have more time that I can commit to the SIG itself, in terms of development and whatnot.
**Serkan Ozal** 09:52 Yeah, actually, same for me, I mean… For the… for the last… 6 or 7 months.
**Tyler Benson** 10:00 I have been mostly working on the AI side in the company, so I'm not…
**Serkan Ozal** 10:05 I mean, OpenTelemetry is not one of my daily, daily jobs, and the instrumentation is not about one… not, my one of, daily tasks, so…
I also feel myself not, I mean, contributing too much time and effort to the open telemetry.
But hopefully, once, I mean, after the end of this year, I will… we have more time.
Because of my responsibilities in the company, but yeah, we'll see.
**Tyler Benson** 10:36 Okay.
Cool. Well, I don't have anything else to discuss.
**Serkan Ozal** 10:47 Yeah, same for me.
**Tyler Benson** 10:50 Have a great day.
**Serkan Ozal** 10:52 Okay, thank you, have a great day, take care, bye.
**Tyler Benson** 10:54 Cheers. Bye.
