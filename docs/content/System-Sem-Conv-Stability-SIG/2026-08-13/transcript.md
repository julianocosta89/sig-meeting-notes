SIG: System Sem Conv Stability SIG
Date: 2026-08-13
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Donal O'Sullivan** 01:25 Bo…
**Braydon Kains (Google LLC)** 01:29 Hey, how's it going?
**Donal O'Sullivan** 01:32 Hey, Braydon.
Don't know, is anyone else gonna join? I know, Christos and Roger are out in PTO.
I think the pie blows out as well, is he?
**Braydon Kains (Google LLC)** 02:33 Oh, Pablo is also a,
**Donal O'Sullivan** 02:35 Yeah.
**Braydon Kains (Google LLC)** 02:36 So Oh, and Dimitri's out. Okay, we may not have anybody else.
**Donal O'Sullivan** 02:41 Yeah.
Yeah.
**Braydon Kains (Google LLC)** 02:44 That's fine. I… since I've been on… on PTO myself the last couple weeks, I don't actually have anything Cool. At the moment for… for this group.
**Donal O'Sullivan** 02:53 Cool.
Yeah, I just have a couple small things. So the… the process scraper release candidate adoption pull request is up.
**Braydon Kains (Google LLC)** 03:06 Oh yeah, I think I saw that in my notifications. I will… Add that to the top of the list, so I can make sure I can start looking at it.
**Donal O'Sullivan** 03:14 Cheers, thanks. Yeah, Roger's given a review, so, I think I've addressed all… like, he had some small feedback, I've addressed it all. He was asking about… adding the process network I.O, metric, I had… I had a look at that, so, goPsutil… process API doesn't have a way of gathering that information.
So we'd have to, like, read directly from, like, proc.
PID, NetDev.
Yeah.
I guess we probably don't want to do that in this PR, though, right? That'd probably be a lot of work just to manually… Read that, whatever.
**Braydon Kains (Google LLC)** 03:50 Yeah, probably not, because we also would… I'm pretty sure we would need to be able to get that information on… I think you can get it on other platforms, so we would need to implement.
**Donal O'Sullivan** 04:00 Yeah, yeah, yeah.
**Braydon Kains (Google LLC)** 04:01 Separately for each. So that is probably fine as a follow-up.
**Donal O'Sullivan** 04:05 Yeah, cool. Yeah, yeah, that's what I was thinking. Yeah, that's… I didn't… yeah, it's true about the cross-platform.
Cool. Okay, so… There was that.
There was another thing as well, just kind of came from discussions internally, for us, so the… the feature gate that I did on the PR is specific to the process scraper, but, like, thinking about, like, that… purely, like, from the host metrics perspective, it's probably not a good idea. I guess the feature gate should be done on, like, on the actual receiver itself, and then all scrapers can use that, right?
**Braydon Kains (Google LLC)** 04:40 Yeah, I wonder if we should maybe, like… Replicate the same… sort of… because I think there's some sort of… global Semcom feature gate at, like, the collector level.
at least that's how I thought it worked, and we could kind of do the same thing, so there could be one global host metrics one.
And if that's enabled.
then use the Semconv schema everywhere, and then there could be a specific scraper one.
**Donal O'Sullivan** 05:13 Okay, okay, so you think there is value in having one prescriber as well, yeah?
**Braydon Kains (Google LLC)** 05:18 I think so, cause…
**Donal O'Sullivan** 05:20 Okay.
**Braydon Kains (Google LLC)** 05:21 People might be more ready for, like.
Process… or it might be less… might be less important for them… for process for them, versus they might have, like, dash… they might not have dashboards for, like, process, and maybe it's not as big a deal, but they might have dashboards for things like network and file system that they aren't ready to migrate yet.
I could see that being feasible.
**Donal O'Sullivan** 05:41 Yeah, that makes sense. Yeah, that definitely makes sense. We were… yeah, we were just thinking about it from, like, a testing point of view, like, when we eventually… migrate all the scrapers would be a pain to have to, like, you know, have a feature gate per scraper that you'd have to switch on just to kind of do, like, a… Like, a test on our own dashboards.
**Braydon Kains (Google LLC)** 06:00 I think there could be both. There should be… there could be a global receiver-wide one that, like, overrides all of the other ones to be true.
**Donal O'Sullivan** 06:07 Yeah, yeah, yeah, okay.
That makes sense. Yeah, that's a good job. So, is it probably okay to leave the global one out of the current PR, then? And maybe that's something we can add down the line?
**Braydon Kains (Google LLC)** 06:19 Yeah, probably. I… I think the only thing is, like, the logic might be a bit unique, where, like, within Scraper Startup.
we check… we check if a particular… if the global feature gate is set, and then… so there might be some additional logic to it. We could probably do it in a follow-up, it's probably okay, but… And while we only have one feature gate, it doesn't really make much of a difference for there to be a global one, so I guess probably won't worry about it for now.
**Donal O'Sullivan** 06:47 Yeah. Yeah, maybe when we… eventually another scraper is being migrated, you know, if you have, like, then we'll have another feature gate, so then the global one might make more sense there.
**Braydon Kains (Google LLC)** 06:56 Yeah.
**Donal O'Sullivan** 06:57 Okay, cool.
Okay,
**Braydon Kains (Google LLC)** 07:01 Or maybe even go the other way, make the global one first, because we only have one scraper anyway, so the global is whatever, and then once we have two, that's the point where we introduce piecemeal ones, so, like, if you only want processed, then you can switch.
**Donal O'Sullivan** 07:14 Yeah.
**Braydon Kains (Google LLC)** 07:14 And the process won.
**Donal O'Sullivan** 07:16 Yeah, that's a good shout. Like, the PR is up right now with, like, the piecemeal one for the process scraper, I could change it, like, what… What way would you prefer?
**Braydon Kains (Google LLC)** 07:28 I'm just thinking from a perspective of… introducing… The feature gate to people, and as they start to set in what… I think Probably the global one is better.
And then… When… when we migrate the next scraper, We say, if… If you already set this feature gate, then you're already going to be migrated. If you're not ready to migrate that scraper, switch to the specific process scraper one to keep your other one, and then turn on the network one when you're ready.
Yeah. That sort of thing.
**Donal O'Sullivan** 08:06 Okay, yeah, that makes sense. I… yeah, I can make the change, because, yeah, there might… there… yeah, there might be a bit of logic as well, as you say, in the scraper, to handle the global one. When you say global one, Braydon, is that per receiver, or is it in the entire collector?
**Braydon Kains (Google LLC)** 08:19 I guess it's kind of an overloaded term, because I think there's a global one in the collector, but I'm also talking about a one in the receiver that then applies to all the sub-receivers.
**Donal O'Sullivan** 08:30 Yeah, makes sense, because, yeah, there's a manifest in… in, like, the base of the receiver, isn't there? And you can kind of specify the feature gate there, I guess.
**Braydon Kains (Google LLC)** 08:38 Yeah.
**Donal O'Sullivan** 08:39 Yeah, yeah, okay.
**Braydon Kains (Google LLC)** 08:40 And I think probably… probably all the feature gates will be, like, via mdataGen, and they'll be in the metadata YAML, but what… it'll be, like, hostmetrics.
Semconf, or whatever we call it, and then hostmetrics.processscraper.something, hostmetrics.networkscraper.something, etc, etc.
**Donal O'Sullivan** 08:58 Yeah, yeah, yeah, yeah, yeah.
**Braydon Kains (Google LLC)** 08:59 Yeah, they'll probably all be in the global mDataGen, maybe. Actually, I don't know, maybe it would be worth it to put… I don't know, we can cross that bridge when we come to it, but the… the host metrics receiver one that will apply to all scrapers.
would be in the root metadata YAML.
**Donal O'Sullivan** 09:18 Yeah, cool. Yeah, because I actually put the current one in the process scraper metadata YAML.
**Braydon Kains (Google LLC)** 09:25 Yeah, I guess the one thing is that the… the, Now that I think of it, maybe we do need to do both, because if you put it in the metadata, then it's in the internal package, which means the process scraper wouldn't be able to access, like, the root receiver's internal metadata package.
So maybe we… maybe we do it with, maybe we just introduce both Feature.
I think… actually, yeah, the way access between packages work, we kind of have to have this within the process scraper first.
**Donal O'Sullivan** 09:59 Hmm.
**Braydon Kains (Google LLC)** 10:00 So… Maybe we act… maybe I'm… I'm looping back around to maybe we do… have… both.
feature gates, and then the… if… the root feature gate is set, it will automatically set the process scraper one.
**Donal O'Sullivan** 10:16 Okay.
**Braydon Kains (Google LLC)** 10:17 So there will be two feature gates, technically. It won't matter that much that there's two feature gates.
we'll call it out in release notes, but… Basically, there would be a hostmetrics.
Semconv… And then, like, a hostmetrics.process.emconf.
And the, The hostmetrics. Semconf will set the process one under the hood, and right now, they'll be functionally the same thing, just because there's only one scraper, but eventually, when there are more scrapers, the global one will have more use.
**Donal O'Sullivan** 10:55 Yeah, yeah.
Okay, yeah. Okay, so yeah, I can take a look at that at the current PR then, so add, like, the global one, and also keep the current one.
**Braydon Kains (Google LLC)** 11:05 Yeah, I think it might need to be either a fast follow or in the same PR, just because, like, I think that whatever release includes the process scraper feature gate should include the, you know, global one as well.
**Donal O'Sullivan** 11:16 Okay, okay, yeah, Yeah, because I think we've… yeah, this PR… like, I don't… I can take a look at doing it in this PR, maybe I could just branch off it and do the global one, and when this one's merged, I can… Opened the other one. Maybe it would make it easier for reviews, I don't know.
**Braydon Kains (Google LLC)** 11:37 Yeah, probably. I think the amount of code added with the global feature gate isn't that heavy, but I know it's… people have strong opinions about keeping the PRs small and single purpose, so…
**Donal O'Sullivan** 11:50 Yeah.
**Braydon Kains (Google LLC)** 11:50 I'm fine with either.
**Donal O'Sullivan** 11:52 Okay, okay, yeah, I might… I'll make a comment on the PR saying we'll do a fast follow with, like, a global receiver feature gate.
That needs to go out before the… the release.
Cool. And I just had one other thing, I can't remember if we discussed it before, but I know, obviously, we've done process namespace, went release candidate. Can we do any other namespaces in semantic conventions, or are we blocked? I know there was a system, was there a couple of things that was blocking us? I can't remember.
**Braydon Kains (Google LLC)** 12:25 Yeah, for system, the big one is stabilizing the host entity.
Okay.
**Donal O'Sullivan** 12:30 Yeah, yeah, yeah, yeah.
**Braydon Kains (Google LLC)** 12:31 That's actually becoming more important to us, internally, too.
Cause we really want to stabilize some stuff in SDKs, and SDKs are actually going to be relying on the host entity and resource detection behavior that we define. So, I'm gonna be focusing a bit more on that in the next couple weeks.
And I think that's… that's sort of the big blocker for basically everything else we have, because the… a lot of the metric definitions I feel pretty good about, but we need to have the entity stabilized before we can stabilize the… the metrics, so…
**Donal O'Sullivan** 13:08 Okay, yeah, cool. Is there anything I can do around met… like, semantic convention stabilization? As you say, host entities blocking, so probably not then, I guess, is it?
**Braydon Kains (Google LLC)** 13:17 Probably not, but it might be useful to, like, do a… like, take an inventory of the metrics, that we have that maybe don't have an equivalent in the receiver yet, and what stuff like GoPS Util can and can't do, because we may run into more, kind of like we did with Process Network I.O.
That might be… might be a worthwhile exercise.
**Donal O'Sullivan** 13:42 Okay, so take inventory of metrics having semantic conventions and… are not in the host metrics, right? Yeah. They're not in host metrics.
Yeah, cool. And then, yeah, we might need a… That'll help a strategy how to, like, implement them, I guess.
**Braydon Kains (Google LLC)** 13:58 Yeah, we could… I think if we can get it upstreamed into GoPS Util, that's always going to be better. That's just harder, because getting things upstreamed into GoPS Util usually requires that the API you introduce, if it can be implemented in all the… all their, like, 12-plus platforms that you need to have it implemented in all of them.
**Donal O'Sullivan** 14:16 Yeah, yeah, yeah.
**Braydon Kains (Google LLC)** 14:17 So, it's… it's not as easy, but it's… it's generally… better for the receiver if we can get him to go PS Util first.
**Donal O'Sullivan** 14:26 Yeah, yeah, yeah, we don't have to do any crazy implementations or so.
Cool, and… Yeah, there was the other thing I know I was kind of… I was looking at the deprecation of the processes scraper. I think that's kind of… is that blocked on your work in Collector Core to kind of… Because I know, was it yourself, and Dimitri want… Dimitri wanted, like, a way of… disabling all metrics, and then enabling one or two, or something like that, wasn't it? A way of kind of filtering?
**Braydon Kains (Google LLC)** 14:57 I have to go, I have to catch up on the status of that PR, I think it was in… it was in decent shape, I think it may have had a comment on it that I'll address, but yeah, that work is underway, so we should be able to move ahead with deprecating the scraper once we have that in.
**Donal O'Sullivan** 15:14 Yeah, I guess, yeah, so it's essentially waiting on the collector core work, and then we can just do the… Yeah.
**Braydon Kains (Google LLC)** 15:21 Yeah, I think so.
**Donal O'Sullivan** 15:22 We can probably reopen your PR with just, like, the update for the actual disabling metric part.
**Braydon Kains (Google LLC)** 15:28 Yeah, it's old, but I actually don't think a lot of the code has changed that much in a way that it wouldn't be difficult to, like, de-conflict.
**Donal O'Sullivan** 15:36 Yeah, yeah.
**Braydon Kains (Google LLC)** 15:38 So, I'll probably, probably go that route.
**Donal O'Sullivan** 15:40 Nice. Yeah, I guess we're waiting on Dimitri to come back from holidays for approval. Yep, unfortunately. Yeah, yeah.
**Braydon Kains (Google LLC)** 15:47 He's sort of the only one who, approves stuff in mDataGen these days, so…
**Donal O'Sullivan** 15:52 Yeah, yeah, yeah.
Cool. Okay, so… Yeah, so I'll… I'll update the PR with a comment, and I'll… I might… I might credit GitHub issue just for that inventory of all the metrics that are in Semcom, but not in host metrics.
**Braydon Kains (Google LLC)** 16:08 Yep.
**Donal O'Sullivan** 16:09 Just a document. I'll put that as, like, a sub-issue we have for the Semcom transition.
**Braydon Kains (Google LLC)** 16:14 Yeah, that would make sense. That way we can keep track of what stuff we might… like, because we might have a bit of time until we can actually get it into Host Metrics Retriever anyway, so if we know that stuff, and people have spare cycles to try and contribute them to GoPS Util if necessary…
**Donal O'Sullivan** 16:29 Yeah.
Yeah, like, I, I, I might have, I may have, I suppose, yeah, I could make the argument. I probably would have availability to contribute to GoPsutil for, like, missing metrics.
Yeah, I just have to look at how… I haven't contributed there before, I'm sure… I'm sure it's okay, though.
**Braydon Kains (Google LLC)** 16:51 It's not too bad. They're somewhat slow at reviews, but it's because it's just, like, two people.
And, it's mostly just, like, you have to be pretty in-depth with… with the contribution, like, you gotta come… you gotta come ready when… once you open, that PR has to think about all.
**Donal O'Sullivan** 17:08 Oh, yeah.
**Braydon Kains (Google LLC)** 17:09 cases and stuff, yeah.
**Donal O'Sullivan** 17:11 Yeah, you have to have all the justification, I guess, as to why it's needed, and etc. Yeah, yeah, yeah, I getcha. Cool.
Okay, I don't have anything else anyway, I think that's our version.
**Braydon Kains (Google LLC)** 17:25 I don't think I have anything else, either. I… I did see that there's… Revived discussion on introducing… Hardware temperature in the hose venture.
**Donal O'Sullivan** 17:35 Is he right?
**Braydon Kains (Google LLC)** 17:36 but because of the way, I'm not… I'm really not sure about the hardware Metrics namespace.
It's kind of hard for me to… Want to say, okay, let's, let's just take those… those semantic conventions that we're not sure we're gonna keep and put them into the receiver. I don't know.
**Donal O'Sullivan** 17:55 Yeah.
Yeah, I think I saw there was, like, a couple… was there one or two PRs to add?
Was it hardware metrics or something similar, and there was no Sem Conv, and I think I might have… I think you commented to add the Sem Conv, was it?
**Braydon Kains (Google LLC)** 18:09 Yeah, that… there was a couple, there was… Network Bandwidth was one.
And there might have been a hardware one, too, I can't recall.
**Donal O'Sullivan** 18:20 Yeah.
Anyway, yeah.
**Braydon Kains (Google LLC)** 18:24 Okay, I think that's everything I have, though.
**Donal O'Sullivan** 18:28 Cool.
And… I think that host ID PR is approved as well, is it?
**Braydon Kains (Google LLC)** 18:34 I think so. Maybe I'll… I'll go and double-check that. I thought it was approved.
**Donal O'Sullivan** 18:40 Yeah.
Alrighty.
**Braydon Kains (Google LLC)** 18:43 Okay.
**Donal O'Sullivan** 18:43 We'll chat you next week, Braydon.
**Braydon Kains (Google LLC)** 18:45 Thank you. Have a good one.
**Donal O'Sullivan** 18:47 You too. Bye-bye.
