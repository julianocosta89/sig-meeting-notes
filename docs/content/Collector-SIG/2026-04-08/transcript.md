SIG: Collector SIG
Date: 2026-04-08
Duration: 20 minutes
============================================================

## Zoom Recording Transcript

**Pablo Baeyens** 04:32 Should we start?
**Damien Mathieu** 04:36 I think we can.
**Jade Guiton** 04:38 Yeah.
**Pablo Baeyens** 04:41 Okay, 4D… High priority issues, I think I should mention… PR by Ariana. Give me one second and I'll link it.
Sorry, I'm having trouble finding it.
Let me look at the notes on… Okay, here it is.
Didn't want to discuss anything in specific, just, ask people for… reviews.
**Blake Rouse** 06:01 Yeah, I had the one, that I put on there for… I'm looking for another review on the, RFC partial reload Support. I got one approved… approval, looking for, a second, hopefully.
But just more eyes on it would be great.
In any form. So, just trying to… Keep bringing attention to it, and hopefully get it over the line here at some point.
**Pablo Baeyens** 06:32 I talked with Mikulai about taking a look.
This, I can… Take a look.
But I'm not going to commit to a specific timeline, Let's say… my hope is within this week or next week.
**Blake Rouse** 06:54 Okay, yeah, that's great to hear. Yeah, thank you.
Yeah, just anyone that can look at it would be great. Appreciate it.
**Pablo Baeyens** 07:03 I believe this has been shared already on AutoCollector Dev, but if it hasn't, amazing.
**Blake Rouse** 07:09 us.
Let me share it there. Yep.
**Pablo Baeyens** 07:13 Cool, so then we are all good in terms of… Announcing it.
Yes.
**Evan Bradley** 07:28 I'll take a look this week as well. Sorry, Blake, I've been… Catching up since I got back. We'll probably need the majority, I think, of approvers to take a look at it before we're able to merge it, if I remember the process correctly. But we'll… we'll keep it, moving along here.
**Blake Rouse** 07:47 Yeah, I appreciate it, yeah. Just as long as we can keep it moving, that's great.
**Pablo Baeyens** 08:00 Okay, I guess we can move to… the next one, unless you want to discuss anything specific, like, about the RSC?
**Blake Rouse** 08:06 No, no, let's move on to the next one. I'm good.
**Pablo Baeyens** 08:23 So, that would be you, Dominique?
**Dominik Süß** 08:25 Oh, yeah, I just didn't want to… first time joining these calls, so I'm not sure of the order of things, so I didn't want to interrupt anyone. Yeah, I have two, one issue and one PR up.
That all revolve around improving the internal telemetry of the collector, reasoning being that we've built a POC of Using collector telemetry data to visualize how data flows from receivers, through processors, through exporters, and then to any OTLP destination.
I was just wondering if there's any specific thing I can do to get those, kind of triaged and reviewed, or anything else I should, work on.
**Jade Guiton** 09:19 Regarding your… your issue about reconstructing the graph, I don't know if someone's brought it up, doesn't look like it. Have you checked out the new pipeline telemetry feature gate?
There's, actually, I can send a link.
Right here, there's an RFC that describes some attributes and some new metrics that you can enable with a feature gate that I believe should allow you to reconstruct the graph purely from the metrics.
It's not perfect. If there's no data flowing, you're not gonna get a metric.
Overall, if you want to get accurate graphic construction, you're gonna need to get the… the collector's config, usually through op-amp.
But, I think with that feature gate, it should make it, It should make it a lot easier to reconstruct the graph in an accurate way.
**Dominik Süß** 10:23 Yeah, I haven't seen this before. I guess this wasn't around when I first looked at it. Yeah, no, I haven't seen this before. I'll definitely check it out and see if I can… Use that to build the entire thing just off of metrics.
**Jade Guiton** 10:39 Yeah, I've thought about this problem a little bit, and I think it's… I think you can get everything, Like, you have only one node per receiver per signal.
And one… Per exporter, per signal.
But, given that receivers… Emit the same data on… In all pipelines that they're in.
And that the exporters necessarily take their data from something else. I think you can reconstruct the entire data, the entire graph plus traffic data with that.
**Dominik Süß** 11:14 Sounds good, I'll try. And this is, something that is implemented, or this is just an RFC?
**Jade Guiton** 11:19 So it is implemented, but it is under a feature gate. I don't know if it's for, like, a document anywhere.
But, yeah.
**Dominik Süß** 11:31 Okay, yeah, but I should be able to find a feature gate based off of this.
Cool.
**Jade Guiton** 11:35 Yeah.
**Dominik Süß** 11:37 But, yeah, and the other point is just, I, adding an endpoint attribute to the, to the OTLP exporter to be able to see where in the world the collector is sending its data to.
I talked to the, SimConfig, around how those attributes should be named and implemented that feedback, so I'm just waiting on a review on that PR.
**Jade Guiton** 12:06 Nice, sounds good.
I think it's, I feel like it's kind of a slippery slope, because it's kind of exposing configuration.
As… as metric attributes, and, like.
I feel like that kind of overlaps with, with op-amp and config reporting, but… I think this particular use case is probably fine.
**Dominik Süß** 12:35 Yeah, that's all from my side.
**Jade Guiton** 12:47 Any other impromptu topics?
**Pablo Baeyens** 12:58 I guess I have a PR to remove usages of Docker and use Mobbi instead to deal with some… Security… stuff.
**Jade Guiton** 13:16 Muses of what?
**Pablo Baeyens** 13:17 Oh, shit.
Of Docker slash docker.
as a library, and instead using Moby slash mobby.
Because… There is, This, security advisory, and, There is no patched version for… Docker slash docker.
And that is causing some… CI failures.
Oh.
Michelie?
**Mikołaj Świątek** 13:56 So, essentially, what happened is that when you wanted… in the past, not so distant past, if you wanted to use a Docker client, you would import Docker slash Docker, but that would… that was a single module that also had the server component in it, and as of… half a year ago, roughly, I think, Docker started publishing, or in this case, the GitHub orgasmoby, started publishing a separate, client library, which is only the client part, and the server the Docker slash docker, the original package, is more or less deprecated, in the sense that they're not publishing any more versions after, like, 28-something-something.
That's essentially what's happening. We're getting some CVEs, and it's impossible to actually address them without switching to the new client libraries, because there's no new versions of the older one.
But, like, that's my understanding of what's actually going on. But it's quite annoying, because if you… if it comes from a dependency, then you can't just bump it.
Izzy, then you actually need to switch.
A completely different module.
**Pablo Baeyens** 15:17 Right. And so I have the PR, I just linked to do that on CollectorKidrip, and if there's any Prometheus or Prometheus-adjacent people here, there's another PR on the Prometheus side that Alex Filed.
That we also need to make scanners happy.
Happy air, because there's… Order… Things that we need to deal with, other vulnerabilities, but… At least We'll address this one.
Alright.
That's all I… any… Any other impromptu topics other than mine?
Okay, see you all on the internet.
**Evan Bradley** 16:28 Fire one.
**Damien Mathieu** 16:28 beer.
**Blake Rouse** 16:29 Bye, everyone.
