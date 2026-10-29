SIG: OpenTelemetry on Mainframes Weekly Sync
Date: 2026-10-28
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Matt Hogstrom (Broadcom Corporation)** 06:00 Hey, Santiago, how are you?
**Santiago Ortega** 06:04 Hey, Matt, doing okay, how are you?
**Matt Hogstrom (Broadcom Corporation)** 06:07 I'm doing well.
This happened, actually, the last weak, last time I was on.
there was no notice that we weren't meeting, but nobody showed up, so we'll just give it a few minutes and see if, Jim or Rudiger are going to join today.
**Santiago Ortega** 06:28 Okay.
**Matt Hogstrom (Broadcom Corporation)** 06:31 And just a heads up, you probably already know it, but the call's being recorded.
For your awareness.
**Santiago Ortega** 06:40 Okay.
**Matt Hogstrom (Broadcom Corporation)** 09:38 Personally, I'm gonna give them 4 more minutes, and then call it.
Have you been tracking the, work, and do you have access to the repository for OpenTelemetry Mainframe?
**Santiago Ortega** 09:57 I, this is the first meeting that I joined.
And I started looking into this this week, so…
**Matt Hogstrom (Broadcom Corporation)** 10:05 Okay.
**Santiago Ortega** 10:08 I don't have that… Much access or information just yet.
**Matt Hogstrom (Broadcom Corporation)** 10:12 Okay, I'll just give you a little background since we're both here.
So, the… the, openTelemetry Mainframe Special Interest Group is focusing on Defining the semantic conventions, for… Mainframe metrics and other data.
And… there's a pull request out in the repository. Do you have the access to the repository? Do you know what it is… where it is?
**Santiago Ortega** 10:40 I think so.
**Matt Hogstrom (Broadcom Corporation)** 10:41 Okay.
And so, there was actually a pull request that was opened by Rudiger Probably about 3 months ago.
And… I believe the goal that he had was, IBM is coming out with a new version of their REST API.
And so he had proposed a number of changes. It's pull request number 20, I think.
And… We're… We're gonna be discussing the content of it, and it's a fairly large PR.
So, we… we talked about breaking it into some smaller pieces.
And just for consideration, I think, the namespace that he was using was Mainframe.
And I was suggesting that we Change that to align better with the architecture.
of… the rest of the OpenTelemetry SIGs.
And change it from Mainframe to S390X.
And, you know, basically then say, dot.
zOS.hmc.ZVM, etc. And so, the architecture really defines the overall composition of the different operating systems that you could run, just like you have x8664, ARM64, etc.
And so it would be familiar from that standpoint.
And then the next thing was to… Really start thinking seriously about who the consumers of the data are gonna be.
I think, so far, We really thought about the volume of data that we have available to us.
from, you know, all of the different products, SMF, In ZOS, we have… you know, VSE, we've got all these other pieces, so let's really focus on what SREs would like to get.
And specifically, not just Blow all possible data, because my… my expectation has been That the workflow would be more like… An SRE would be looking for indicators of changes in behavior, monitoring of, say, transactions, performance, and things of that, you know, ilk.
And what they would end up doing is, if they were drifting out of expectations.
they would end up contacting the appropriate platform, so OpenTelemetry gives them an indication that, hey, this is going on in kicks on the mainframe.
those SREs would probably contact The domain expert, whether it would be on the mainframe or in the networking area, etc.
And then those SMEs would probably use their specific monitoring tools and capabilities to really do the deep dive. So you don't have to export all the possible data, you have to… we should be exporting the data that is most meaningful from that standpoint. I could be totally wrong, but that's kind of how I see it going, because to try to export all the data that's coming off would just be… Kinda crazy.
**Santiago Ortega** 13:46 too much.
**Matt Hogstrom (Broadcom Corporation)** 13:47 Yeah.
So, anyway, it doesn't look like Jim or Rudiger are gonna make it today, so I'll send them both a note, and I'll copy you, since you joined. And, ask them if we're continuing to meet or what the current plan is. All right?
**Santiago Ortega** 14:05 Okay.
**Matt Hogstrom (Broadcom Corporation)** 14:06 All right, thanks, Santiago. I'll talk to you later.
**Santiago Ortega** 14:08 Bye. Bye bye.
