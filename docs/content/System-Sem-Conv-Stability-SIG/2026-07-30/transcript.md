SIG: System Sem Conv Stability SIG
Date: 2026-07-30
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Pablo Baeyens** 01:31 Hello?
Whoa.
I think it's probably… going to be just us.
Today?
Because Dimitri is out, and Braydon is out.
on, I think, Igor is not joining today.
**Donal O'Sullivan** 02:01 Cool.
Yeah, I can make a start then.
So I, as discussed in the SIG, recently, we discovered there was a couple… there was three process metrics, that are not… that have been in the process scraper for a long time, that are… that are not in semantic conventions. So I opened a PR just to add those three metrics to semantic conventions.
I added them as release candidate with the idea that they've been in the wild for a long time.
in host metrics, but it looks like the Sem… Semantic Convention's maintainers are pushing back, and they want them to be marked as development.
I guess that's fair enough. I don't know, Pablo, Christos, what are your thoughts on that?
I think you might have chimed in, Pablo, on the pier.
**Pablo Baeyens** 02:59 Yeah, I… Sorry, I haven't read the comments from Lyud Milan.
**Donal O'Sullivan** 03:13 Yeah, I think she's more or less saying all new conventions should start as development Stability.
**Pablo Baeyens** 03:19 Yeah, I… I mean, if… they… quant…
**Donal O'Sullivan** 03:25 Yeah.
**Pablo Baeyens** 03:26 Let's do it, I guess. I don't… I don't see the point, but, like, I'm not a maintainer there, so… Oh.
**Donal O'Sullivan** 03:32 Yeah. Yeah.
**Christos Markou** 03:35 We do something… We didn't have exactly the same situation in the kids' conventions, but… The pro- the cage processor had some… attributes that were not part of Semat Conventions, so we added them in Semat Conventions, and then when we started the bumps, we did that all together, but the, the period between originally adding them and starting to bumping their version… Was short enough.
So, probably we can just start with development, and… wait for a release of some article measures, maybe, and then suggest it for a release candidate. Probably we could also communicate that, the plan is to have them in release candidate for some period of time, because I assume we will leave them there for… Until the host metrics processor, the host metrics receiver, use is actually them. I don't see any reason to bump them to stable, or to us bumping them to stable, so we can also highlight this.
**Donal O'Sullivan** 04:46 Yeah.
Okay, cool, so I'll update the PR, mark them as development, and just make a note that… We would like to… Marks them as release candidate, maybe in the, short-term, future.
Yeah, okay, cool.
I… yeah, go ahead, Pablo.
**Pablo Baeyens** 05:08 I was gonna say, like, have we checked if these metrics are implemented on, other places, other than… The host metrics receiver.
**Donal O'Sullivan** 05:20 I have not. I can… I can definitely do that, because I think that's a requirement, is it? To see if they're… if they are implemented elsewhere, like in an SDK or something?
**Pablo Baeyens** 05:30 Right, yeah, so, I think that's the only argument I would see for, like, waiting on… I see… the one in JavaScript does implement process?
metrics… So, maybe… We should trade that one.
**Donal O'Sullivan** 05:56 Cool. Yeah, I'll… I'll definitely… I'll make a note there.
I just had something else, real quick, if we're finished with that, so… Thanks for merging those pull requests for the bug fixes and mdataGen for the version metrics, so Pablo appreciate that.
So I'm hoping to open up a pull request really soon to… adopt the process release candidate metrics. There is one blocker, so I had to, add the Semantic Inventions release to the OpenTelemetry Go SDK, just to get that in, because the latest release contains the process release candidate. But that's still not available to us until the OTEL Go SDK does a release, and I was just wondering Do you guys know on what cadence they do a release, or… Because I don't want to kind of jump into…
**Christos Markou** 07:01 you could.
**Donal O'Sullivan** 07:02 Yeah, like…
**Christos Markou** 07:02 commit, you can pin the gold balance sheet to the latest commit from main, and you don't need to wait for a release.
**Donal O'Sullivan** 07:12 Okay, cool. So, just, Do you mean in the mod file, is it within the actual scrape, or just point that the latest commit, is it for OTelGo?
**Christos Markou** 07:21 Yes, they go to Badenshin, yes.
**Donal O'Sullivan** 07:22 Yeah, okay, cool. Yeah, okay, that's probably… yeah, so then we don't have to wait for a release from Hotel Go, right?
Yeah, you can just…
**Pablo Baeyens** 07:30 Ask them as well.
But I think we can use that command.
Yeah. It's been a couple months since the last release, right? So…
**Donal O'Sullivan** 07:38 Yeah, I was looking… so they seem to have done a release, like, once… near around once a month, but the last one has been in… hasn't been… they did their last one in May, so it's been a while, but anyway.
**Pablo Baeyens** 07:50 You can ask Robert, for example, if you want to, check, but otherwise, yeah, using the… The commit works.
**Donal O'Sullivan** 08:01 Yeah, cool, sure, yeah, I'll use the commit, and I'll get the PR open, and then I can just maybe ask, is Rob Roberts the maintainer, or is he, of the Hotel Go SDK?
**Pablo Baeyens** 08:11 Yeah, I mean, rubber door in the order of my internet.
**Donal O'Sullivan** 08:13 Yeah, yeah, cool, cool, yeah, yeah, sure, yeah, no, no hassle.
Thanks, guys.
That's how recently I had, anyway.
**Pablo Baeyens** 08:26 Okay.
**Christos Markou** 08:32 Well, next is mine. I just sent APR for reference, Donald, if you want to have a look. We did that in the past for the processor.
To avoid waiting, there is. Yeah, I just added this pull request here. It is the network interface name attribute, it is a shared attribute between system, containers and Kubernetes for the node, and the intention is to have this release candid because the next intention is to promote to release candidate the network metrics of Kubernetes.
So, we need it, and we will need it anyway for, the system network metrics as well.
Joe.
If you can have a look. Donal approved, Sean. Thank you, Donal.
And, yeah, that was it from my side.
**Pablo Baeyens** 09:37 Boom.
Check the network interface.
19.
Anything else?
**Christos Markou** 10:04 Nope.
**Pablo Baeyens** 10:07 Okay.
See you on the internet then.
**Christos Markou** 10:12 Folks, right?
**Donal O'Sullivan** 10:13 Thursdays. Bye-bye.
