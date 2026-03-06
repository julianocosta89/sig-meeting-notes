SIG: System Sem Conv Stability WG
Date: 2026-03-05
Duration: 19 minutes
============================================================

## Zoom Recording Transcript

**Donal O'Sullivan** 00:30 Whoa…
**Dmitrii Anoshin** 00:34 I don't…
**Donal O'Sullivan** 00:38 Hi, Mitri, how are you?
**Dmitrii Anoshin** 00:40 Doing well. How are you?
**Donal O'Sullivan** 00:42 Good, good.
**Dmitrii Anoshin** 00:45 Where are you based off?
**Donal O'Sullivan** 00:48 I'm based in Ireland, so kind of Midwest place called Limerick, Ireland, so…
**Dmitrii Anoshin** 00:54 Nice, nice.
**Donal O'Sullivan** 00:55 How about you?
**Dmitrii Anoshin** 00:56 I'm in the Bay Area and the U.S, California.
**Donal O'Sullivan** 01:00 Nice.
**Dmitrii Anoshin** 01:01 I haven't been in Ireland. I want to at some point. I've been to, england.
And that's it.
**Donal O'Sullivan** 01:13 Cool.
**Dmitrii Anoshin** 01:14 summer, I'm gonna… I'm actually… probably will visit Iceland, hopefully.
**Donal O'Sullivan** 01:20 Whoa, nice.
**Dmitrii Anoshin** 01:24 There is a… bike ride there. I'm going to participate. Let's see if it plays out.
**Donal O'Sullivan** 01:33 Probably be cold.
**Dmitrii Anoshin** 01:36 In summertime, it should be fine, I guess.
**Donal O'Sullivan** 01:38 Yeah, yeah.
**Dmitrii Anoshin** 01:43 They're false.
**Christos Markou** 01:44 A…
**Dmitrii Anoshin** 03:50 We can start. There is not much from my side, I just, wanted to bring that… this aggregation, thing on my emulated genus,
Available, I want to…
wrap it up so it's enabled in all the receivers, and we can disable that feature again, because I'm doing some other changes, so it's, like, adds up, it's… increase the complexity, and for the CPU…
CPU scraper and host metrics receiver already merged. I mean, PR to enable regulation is merged, so I'll submit another PR to make CPU core
an optional attribute, as it is in semantic conventions, and CPU scraper will produce much less MTSs by default.
But user can still… enable CPU core if they want to, and they will get… Same matrix, pure core.
And, yeah, there are plenty of people making PRs, some of them
Real people, some of them not, but…
the… the, it's, like, it's still helping. So… and I have one PR for… to enable aggregation for memory scraper, just wanted to test it myself. So if you…
If you… if you can…
approve it, that would be perfect. And that's it from my side.
**Pablo Baeyens** 05:34 from my side, so, I missed the… Last two meetings, so…
I think you probably talk about this, BR.
But I was wondering if… Given the approvals…
We are ready to merge it, or if there's something else that needs to be discussed?
**Donal O'Sullivan** 06:06 Is this the… the process… updating the process attributes, PR and Spanish intervention? Yes, that's helpful. Yep. Yep.
I guess, for me, it looks good. We've got multiple approvals, and… Yeah.
**Dmitrii Anoshin** 06:27 Keep in mind, we'll have to apply this to the collector as well, and all the opt-in
attributes will not be emitted by default, just… I don't think they increase cardinality.
I guess,
It's still unique per process, so it will be just the same amount of metrics emitted with just less attributes, essentially.
And that makes sense to me.
**Donal O'Sullivan** 06:59 Yeah.
If that makes sense.
So are you saying, Mitri, I guess if we merge this, we'll have to work on the collector to update that then, right?
**Dmitrii Anoshin** 07:09 Yeah, we'll have to update requirements level there as well. Currently, in the collector, we don't even have the new semantic conventions, so they are, like…
old names, I guess.
**Donal O'Sullivan** 07:20 Yeah, yeah.
**Dmitrii Anoshin** 07:21 But still, I think it's better to apply.
the level on the old names as well. So, like, we…
We make users prepared for this change, I guess.
So…
We don't keep, like, this inconsistent state when the old names are all enabled and the new names are disabled.
What do you think?
**Donal O'Sullivan** 07:57 Yeah, makes sense.
Like, I think just looking at the…
like, for example, the host metrics receiver, that's using SEMCOM version 1.9, and if we make
This update, what's the version?
Like, we're not really updating our version here, are we? It's just literally the.
**Dmitrii Anoshin** 08:19 Yeah, we're.
**Donal O'Sullivan** 08:20 We're updating the attribute entities, isn't it?
**Dmitrii Anoshin** 08:23 Yeah, we're not updating the new version. We still use the old version with old naming. I mean, it's fine, we can potentially don't touch it and keep all of them enabled by default, so I guess it's alright.
It's just, whenever… we need to ensure that whenever we switch to the new name, we need to ensure that the new names have opt-in and disabled by default, so yeah, I guess it's…
**Donal O'Sullivan** 08:51 Yeah, makes sense. I can… I can create an issue for that in…
Any collector contrib, I guess, once we merge the semantic conventions, Pierre.
**Dmitrii Anoshin** 09:00 Yeah.
Sounds good.
For the CPU… for the CPU, I wanted to do this for a while, because it's… I've been hearing a lot of complaints that, hey, why you, like, emit metrics per core? It's, like, a lot of…
MTSs, and well, I saw a lot of configurations when you have leads, like, metrics.
matrix transform processor or something like that, when they just, like, disable that attribute and try to accumulate them, so I want to make it, like, default behavior.
**Donal O'Sullivan** 09:36 Yeah, it's like a… kind of too much information, I guess, is it?
**Dmitrii Anoshin** 09:39 Yeah, yeah.
**Donal O'Sullivan** 09:40 Yep.
**Dmitrii Anoshin** 09:40 But for the process, it's like, number of NTSS is the same, so just, like, the data presentation, I guess, it's fine, we can leave it up until we migrate to the new semantics.
**Donal O'Sullivan** 09:50 Yep.
Okay.
Cool. I… yeah, I think…
Yeah, so we're just… we just need a maintainer to… to approve, our… yeah, to… to merge it, I think. I think we have the approvals for it, right? So…
**Dmitrii Anoshin** 10:04 Yep.
**Donal O'Sullivan** 10:05 Yeah, cool.
Great.
Next one. Thank you.
**Pablo Baeyens** 10:16 Okay, and…
That would leave us with only one issue on the GA board, which is the process status metric.
I… I'm not sure if this is an attitude change or not. If it is an attitude change.
Would it make sense to… Postponed is.
**Dmitrii Anoshin** 10:46 And I think, yes, and also it's kind of controversial in terms of it can conflict with the entities. I mean, we do have status kind of metrics for Kubernetes as well, so we…
I'm not saying that we cannot add this metric, but it's just this information is probably better to be added as part of entities.
And even if we added an additional additionally as a metric, it would be…
I do agree it's gonna be an additive change.
So I don't… I don't understand why it's a blocker.
**Pablo Baeyens** 11:32 Okay.
**Christos Markou** 11:34 I think before this, though, we had this discussion about
Moving, process runtime into its own Entity, or something like this.
I think we discussed that last week. So, I think this is something that we should discuss before GA, for sure. And then there is this other thing that Briden wanted to implement. He had the PR that was closed to add requirement levels for process metrics.
I think these two are actually blockers. The first one, it's up to us to decide if we want it or not, but the latter, it's better if we can do it now.
**Pablo Baeyens** 12:21 So…
**Christos Markou** 12:23 Sorry, we need to do…
**Pablo Baeyens** 12:28 basically the PR that Radon did that is, similar to the one from Donald, but for metrics instead of…
Attributes?
**Christos Markou** 12:37 Yeah, Bradon's PR was only for metrics. Yeah, we need… we need this again.
And we need to catch this, actually, this time.
**Pablo Baeyens** 12:45 Right.
**Christos Markou** 12:47 And then, what…
**Pablo Baeyens** 12:48 What did you say that we needed to discuss?
**Christos Markou** 12:52 There was a thread,
in this… in this PR of Donald, there was a thread, who was that? James…
James Thompson. Thompson Tomo is the handle. There was a suggestion about moving…
Process executable, yeah, I was wrong before, it was not process runtime. To move process executable on… to its own
Entity, and we said last week that we can discuss it in a follow-up.
Yeah, it seems we don't have an issue for this yet, so…
**Pablo Baeyens** 13:34 Right, that's the thread where I commented? Is that… No, that's not.
**Donal O'Sullivan** 13:43 Yeah, I can put it there, Pablo. It was on the PR, I think you were… you were replying to a few of the comments, and
I think Thompson was… he was just of the opinion that process executable should be moved to its own entity, and I think we decided that we could do that afterwards, or at least discuss it.
**Pablo Baeyens** 14:01 Okay.
Yeah, outside of this PR, but if we want to discuss this…
**Christos Markou** 14:06 We should do it before GA.
**Donal O'Sullivan** 14:08 Okay.
**Pablo Baeyens** 14:11 Okay, I see it now.
And did you get to discuss this, or should we do it now?
**Christos Markou** 14:28 We're slightly… That's that last week.
I think people were positive in general about this, but yeah, it was a very early discussion.
**Donal O'Sullivan** 14:43 Yeah, agreed, yeah, I think it was… the consensus was it would be good to move to its own entity, but…
Not in the… not in the open VR.
**Dmitrii Anoshin** 15:05 Yeah, I think it's… it requires a deeper kind of investigation.
Like, what we will get from moving to another entity, and what
burden and overhead it would introduce, and…
Some kind of a dog, maybe.
who's asking for that? Maybe we can ask Thompson to present that somehow.
To summarize.
**Donal O'Sullivan** 15:46 Jesus.
Yeah, no, I… yeah, sorry, Dimitri, I agree. I can open an issue about it, and I can… I can try and bring Thompson into the conversation and get him to give some feedback, if that would work.
**Dmitrii Anoshin** 15:59 That would be perfect. I don't think… we don't even have an issue specifically for that question, right, and it's pretty significant.
Decision that we need to make, and for that decision, we need some, like, some more information.
**Donal O'Sullivan** 16:13 Okay, yeah, I can take that as an action, I'll… Yeah, I'm…
I'll open an assurance management conventions about it.
**Dmitrii Anoshin** 16:21 Awesome, thank you.
**Pablo Baeyens** 16:23 Okay.
Donald, could you also update your PR description so it does not fix…
864 just updates it, since we would need, the metric.
Requirement level here.
**Donal O'Sullivan** 16:40 Yeah, sure, can do it, Pablo, no problem. I'll… I'll do that, after this meeting.
**Pablo Baeyens** 16:47 Okay, and then… Going back to the process status thing,
I didn't get Krista's whether you agree that this can be done afterwards or not?
**Christos Markou** 17:01 The status metric? Yeah, I think it's fine. Yeah, I agree.
**Pablo Baeyens** 17:05 Okay, since Bradon was the one that added the… Blocker… label, I'm going to… Ping him to…
See what he thinks.
But, I think we can remove it if he agrees.
**Dmitrii Anoshin** 17:39 Sounding good?
Thinkable.
**Christos Markou** 17:45 So, do we think the SPR is ready to go? Because I just added… for some reason, the projects were not added.
And I think… Yacht.
if we mark this… if we add this in the project of Shemont Convention.
move it to ready to be merged. Mainers will see it at some point and will, take care of it.
Do we agree that, it's fine to merge it?
Okay.
**Dmitrii Anoshin** 18:22 process, recommendations, right?
**Christos Markou** 18:27 Yes.
**Dmitrii Anoshin** 18:27 level, yeah. I haven't looked deep into that, I just, like, quickly looked, and it looks good to me, but I can put in, like, extra approval.
After this call, I'll just… Take a deeper look.
**Donal O'Sullivan** 18:47 Gustav, I just updated the, the fixes, so I just said updates, issue, or what did I say? Related to issue. I removed that, so…
Should be good.
**Christos Markou** 19:11 Horizon.
**Pablo Baeyens** 19:18 Right.
See you next week, then?
**Dmitrii Anoshin** 19:24 Thank you, everyone.
Goodbye.
**Pablo Baeyens** 19:27 Thank you, my…
**Donal O'Sullivan** 19:28 There's guys, by the way.
