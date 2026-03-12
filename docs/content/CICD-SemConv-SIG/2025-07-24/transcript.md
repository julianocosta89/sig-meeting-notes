SIG: CI/CD SemConv SIG
Date: 2025-07-24
Duration: 22 minutes
Zoom Recording URL: https://zoom.us/rec/share/HjYAhnWyeJVJauE9qYOnqePz8_dsLPFsLcORce3pJ4FNcknYJUxfVMTNEooUnaP5.6Pu-zGqbkRR0uhC7
============================================================

## Zoom Recording Transcript

**Adriel Perkins** 00:38 Good day.
**Martin Costello** 00:45 Hey!
**Adriel Perkins** 00:47 How is everyone doing?
**Martin Costello** 00:50 Good thanks.
**Adriel Perkins** 00:54 Good.
Here's the doc. Feel free to add any items she may want to discuss.
Give folks a few minutes to join.
Give everyone another minute.
**Dotan Horovits** 02:44 Everyone.
**Adriel Perkins** 02:46 Good day.
Alright. We can go ahead and get started.
Go ahead and share my screen.
Yeah, it's the right one again. Feel free to add anything as you think about it. It started with just a little bit of triage basically, everything is still waiting for responses. Haven't heard about Team City. This one is been reviewed and been approved. We're waiting for like a couple comments to be resolved, and then it can be merged in and closed.
And I haven't talked to Nicholas in a few weeks, so need to get back in touch with him. I'm thinking this probably and I'm gonna add the the label on it now, but I'm thinking it probably goes to phase 2 at this point in time. Gets recreated as broken down. Work in phase 2.
The to do's that were pretty important, but haven't been touched yet, are still pretty valid. I've started to add some labels on them. For, for example, the the draft of the data model for event types within Ci CD systems. I've gone ahead and put a label on them in Ci CD phase 2, so that we can sort on the board in that way. We can at least have a discussion around, like some of the tactical pieces. With regards to how we we work towards that phase. 2. Approach and I haven't reviewed and gone back through these yet. These need to get get reviewed and figure out if we wanna bring them to phase 2. Or if we wanna like, rethink about how we wanna accomplish those things?
any. It's a pretty good segue for phase 2 in general. But are there any before I segue to that? Are there any actual comments on this stuff that anyone wants to discuss.
**Dotan Horovits** 05:08 What was the cut off for phase? 2. Because sounds like everything that is there in the in these columns in particular, should probably be phase 2. Just to understand what's your criteria? Both time, wise and otherwise, for things not to be otherwise, I guess by default this should be switched over. But just to understand.
**Adriel Perkins** 05:26 Yeah, if it can close now, I would love to close it now. Before going to phase 2. But really, there's not like a ton of of folks like working on these things. Not of a lot of it's in progress. There's only a couple of things there in progress. So I don't have a hard cut off. The guess the cutoff would be whenever we create the new phase, 2 board and bring those things over to it. And that would be dependent on when we start. Phase 2 on that note I did open the pull request. Not that one.
This one which is in the doc for adding the phase. 2 proposal. It is a rough draft. I would love reviews and thoughts about how tactical we want to get. I did say. Phase 2 is like 6 months.
Gear ish geared towards the end of the year.
We can, you know. That's another piece of feedback I would love to have do we focus towards the what we can accomplish by end of year? Or do we focus what we can accomplish by end of 1st quarter in 2026. How do we want to approach that? Given that, we're already like past the half year, mark here in 2025 it does discuss the new meeting time as Wednesday at 6 Am. Pt. Based off of the current standing of the survey. But would love would love feedback on on this? Now that it's opened, feel free to take a review. Comment on it, rip it apart whatever I'm just happy to have eyes on it so, and and feedback so it is there, and that's that's the only call that I had for the day.
**Dotan Horovits** 07:22 I cannot happy to comment on the on the Pr. But the issue. But I can definitely say, like off the top of my head because we're past the half year, Mark, and also given that people probably have limited availability during the summertime. So through August, which will effectively probably start September.
So I'm I'm wondering that leaves us like from there to end of year. That's a pretty tight phase, I'm sure, if you want to make it that tight, or just give us a bit more leeway.
**Adriel Perkins** 07:55 Yeah, no, that's that's a good call out that would if we started if we targeted the start of September. That would give us and we move the phase 2 end date to the end of the 1st quarter of 2026. That'd be solid 6 months right there.
So I I like that. If if you all, if you're good with it.
**Dotan Horovits** 08:16 I'm good with that. I think it given that the the pace of progress we've seen phase one. Obviously things can change phase 2. Maybe we'll see some more, but I think it. It makes sense, and also, if you make it so tight, then you need to break it down also much finer, and you know it.
When someone comes suddenly and and focuses on an area, it shuffles the the priorities because just we have the the right folks for the for the job. So I I feel more comfortable given the previous space to to have a bit more room there.
**Adriel Perkins** 08:54 Fantastic.
**Dotan Horovits** 08:56 Yeah, thanks for going ahead and opening it, of course. And let's try and also solicit some feedback from Dan from the Governance Committee and the rest about how granular they expect us to be, or what's the convention there? If they have some sort of guidelines there.
just to understand that we're not wasting too many cycles internally to break it down when it's unnecessary. And again, just because we know that things change when things come out, so I don't. I'd rather not detail it overly when we don't have the the commitments around that, or the clarity that we can actually carry it in this order, or the.
**Adriel Perkins** 09:37 The rude in the phase. 2, doc. I did outline like what we've kind of like high level accomplished since being opened, and I only put 4 like main core goals.
Which is the implementation of the spec in a couple languages.
We already have, like a, you know, draft Pr. And go, thanks to Robert Payjack and we got draft in python as well. So those are things we can move forward and start to add additional languages, but we would want to scope down, like I think, which language was we'd want to to do first, st because it does require, like SDK Maintainer support there.
the enhancement to the attributes that we're missing. A lot of that is some of the stuff that was in the backlog today. And then Beta stabilization, stabilization of of various different things, mainly semantic conventions.
The Github receiver, as an example kind of lives outside of the the scope of the Sig. But you know, very related but that is at a point where it could start to get done it could have beta stabilization once it updates to the current attributes. So that is something that we could kind of stabilize on but again, it has its like own kind of life outside the Sig. So it's not necessarily directly the scope of the Sig.
And then focusing on some increased adoption, with maybe like one or 2 technologies was was what I was thinking. For phase, 2 goals.
Does that resonate, or your thoughts.
**Dotan Horovits** 11:23 Yeah, yeah, for sure. For sure. Actually, I'm thinking for 4, for the adoption, do we want to?
Because of the we, we also have, like internally, within hotel that you know, there's amazing achievement with the what what it was done. But we talked about seeing how we can expand this before, even having or not before, but in parallel to having other projects. So I'm wondering if we should stay that, and because we live inside auto. Maybe this will also generate some commitment from I don't know the the Governance Committee and others to to chime in, or or if they say, you know, this is too ambitious. At least we'll know their feedback on that. But sort of a way to solicit more engagement within auto in the adoption and maybe other Cncf projects where they have some cross lateral control or ability to influence.
because many of them are also like on on Prometheus side, or others again. Just. It's an open idea, happy to hear thoughts either way.
**Adriel Perkins** 12:30 Makes sense any ideas on how best to approach that having that conversation with them.
**Dotan Horovits** 12:38 So what I thought is is 1st maybe stated as the phase as a draft of the phase, like phase 4, let's say, break it down into, or have it to top level phase, so increase or expand adoption within hotel and and extended or or increase adoption to other projects. So it's sort of like breaking down 4 into 2 items, one squarely on hotel, which we can frame as expanding because there is already a 1st step done in phase one that we can call out as part of the statement there as reference. And and then stage 2 is saying as what you said just now, like key technologies, and maybe even naming, not not committing to these, but naming a few as as examples that we're targeting just.
**Adriel Perkins** 13:39 Sounds good.
**Dotan Horovits** 13:41 I can, therefore, just for reference, for example, that Percy's project recently got themselves listed by Prometheus as like yet another tool.
essentially the only other tool besides Grafana to for visualization. So I'm saying, and this really raises the the awareness and gives some sort of a recognition. So obviously, we're not a visualization tool. It's not the front end thing that you see visually, but saying, Hey, this is hotel has adopted it. Across the board will be a major statement. Obviously, we're we're not there yet. But I think this is the what I would like to solicit as part of the discussion phase 2 like piggyback on the phase, 2 discussion to to ask to ask for the buying from from the Governance Committee and for the for such a statement and the goal that expands beyond just our Sig. So sort of a lateral thing.
**Adriel Perkins** 14:43 Makes sense cool.
**Dotan Horovits** 14:46 And again, let's run it by, Dan. See that I'm not being too overly ambitious here, but I I see that as an opportunity, like the the phase, 2 discussions as an opportunity to also bring this up, because, I think it's a win eating our own dog food and showing the case, and also providing that, as a reference to other projects that might be hesitant, or wanting some some references that'd be cool, to have Otel as the reference for the Hotel Cicd. Semantic connections.
**Adriel Perkins** 15:28 Okay.
I'll make a post in the about the open pull request in the Ci CD channel for visibility.
**Dotan Horovits** 15:37 Makes sense.
**Adriel Perkins** 15:39 And maybe we can even put put one on Linkedin here in a little bit.
Once we get some feedback from from our our the main folks.
**Dotan Horovits** 15:49 Sounds good.
and I'll also comment on on some of these. I'll take the action item to comment on directly on the on the issue. So yeah, I'm just saying that to to hear your feedbacks, obviously. But if if that makes sense, I'll also make it more formal, so that other people can chime in.
**Adriel Perkins** 16:08 Yeah, absolutely. Please do. There is. I I took notes in the in the meeting, Doc.
**Dotan Horovits** 16:17 Yeah, so.
**Adriel Perkins** 16:17 If I missed anything, feel free to update it.
**Dotan Horovits** 16:21 Yeah.
**Adriel Perkins** 16:22 That was all. I had. Anyone have anything else.
**Dotan Horovits** 16:28 I can share. Briefly, I just came back from a cloud native summit. Munich and I had an interesting discussion with With the folks from Cisco about the the semantic conventions presented it, and they showed a lot of interest. And actually.
they they were surprised that that gitlab is not engaging in that, because they they see the value also as consumers of that. So I I am trying to see if I can raise again the the demand with with the gitlab folks through through them, and say so.
I hope to have some some some updates there. Maybe this will be a good way to to revive that channel with sort of end user demand.
and looking to see if we can get forward with the with the Jenkins folks. I really hope that actually, if we're talking about phase one, I need to check back with them. But this sounded like it might be close enough, maybe, even to to have something in phase one. Did you get different?
Read of that, Adrian?
**Adriel Perkins** 17:42 No, I I based on the original conversation. I agree with that. I'm not sure where it stands today, though.
**Dotan Horovits** 17:48 Okay, so I'll I'll ping them again just to actually, maybe I'll I'll use the again the excuse of Phase 2 to just ask them if we can.
converge on that for phase one or something like that. So I'll take the action item if you want to put it on me to follow up with them to see where it stands. But at least I I got the read back then that it sounded like it's it's it's it's mo. It's moving on nicely. So maybe we can even get that milestone done in phase one. And if not, definitely want to scope it into phase 2 even by name. Stating that I know you wrote like, generally work with Jenkins, Team City and so on. Maybe we can even put that as something more definitive that we can put
**Adriel Perkins** 18:40 Sounds good.
**Dotan Horovits** 18:42 The open tofu is, where does that stand? Can you remind me.
**Adriel Perkins** 18:48 I don't know. I haven't looked to see the adoption like how they've implemented tracing but open tofu does have Tracy now, and I know a couple of folks at at work took it took that to a client and implemented it, and we actually have it running in like some Cicd pipelines.
So it is. It's it's made. It's made really good progress. I don't know if it's spec compliant, but the fact that it works and provides value makes me happy, and that can always be updated to be spec compliant later. So I'm happy to see that they they made that progress quite quickly, and have have tracing support now.
**Dotan Horovits** 19:33 Nice. So just to make sure when you say spec compliance. So it's not it doesn't. The data model is not based on the semantic conventions.
**Adriel Perkins** 19:40 No, I I mean, I don't know how they're handling environment, variable context, propagation.
**Dotan Horovits** 19:45 Hmm.
**Adriel Perkins** 19:46 So.
**Dotan Horovits** 19:47 9. Okay. Gotcha.
**Adriel Perkins** 19:48 Yeah.
**Dotan Horovits** 19:51 Okay, I'm just again just wondering if we can sort of take that as a part of phase one. Or do you feel that it's something that will just carry over to phase 2. And then I would at least try and like scope. What's the achieve? The sub milestone that we did do with open tofu. It's not we. Obviously they did the implementation, but maybe just to state that as part of phase, one of of the Sig.
and we also escorted, let's say, open tofu through.
I don't know. Let's say, Beta, and then, phase 2 that they plan on making it fully compliant or whatever. So I'm just again. You'll probably phrase it better than me after you sync with them. Just wondering how to capture the very important milestone that was achieved in phase one, and see if we can wrap it up as phase one or so that something carries over to phase 2, and how to to spell it out.
**Adriel Perkins** 20:45 Cool. Yeah, no, I'll I'll reach out to my contact over there.
**Dotan Horovits** 20:49 Amazing.
**Adriel Perkins** 20:50 Have a chat.
**Dotan Horovits** 20:51 By the way, and if you manage to convince them, you know the the end user that you implemented for to want to share that story over a blog over a talk, Kubeco and whatnot. I'd love to see that on stage showing how they they actually worked it with with opentelf like to share for the sake, if if any one of them is willing to to to share that, and of course you may tell them that we're happy to help them if it's like on the on the side of helping to to write a blog post or any other means that they want talking to meet up or not, as long as they they have their will we'll we'll find a way together. But it'd be amazing case study, and hopefully to one that can resonate with others to encourage them to implement.
**Adriel Perkins** 21:42 For sure, cool.
**Dotan Horovits** 21:46 Cool, anyway, that's just want to share about the this week's discussions.
**Adriel Perkins** 21:51 Appreciate it. Welcome back.
**Dotan Horovits** 21:53 Yeah. Thanks.
**Adriel Perkins** 21:54 Glad it was a good trip.
**Dotan Horovits** 21:57 Yeah, yeah, it's like, just before Europe goes into the the summer holidays, and everyone disappears like the the final note. But it's just a solid community there, the cloud native community in Munich. It's been around We're going quite some time so good to catch up with them as well some Cncf ambassadors there and as always trying to plug in the see. I see this into conversation. See where we can win some more hearts and minds.
**Adriel Perkins** 22:28 Heck. Yeah.
cool. Well, if nobody has anything else, I'll give you back the rest of your time and enjoy your day. See you next week.
**Martin Costello** 22:38 Yeah. Thanks.
Bye.
**Dotan Horovits** 22:40 Thanks very much.
**Adriel Perkins** 22:40 Cheers.
