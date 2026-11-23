SIG: Browser SIG
Date: 2026-11-19
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Martin Kuba (Raintank, Inc. – Grafana Labs)** 01:49 Hi, everyone.
**Maxime Quentin** 01:52 Hello?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 01:53 Maxime, how are you?
**Maxime Quentin** 01:55 I'm good, good, and you.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 01:56 Alright.
Hi, Joaquin. Hi, Chris.
**Chris Chestnut** 02:40 Hey, hey, how's it going?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 02:42 Doing alright.
Alright, yeah, a couple things on the agenda.
So let me share my screen, and let's go through them.
Hmm.
Okay, addie, you have the first one.
**Aditya Reddy** 03:26 Yeah, sorry about that, no.
Pretty sick.
Not in a shape to share a camera.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 03:35 No worries.
So you're just looking for a review on this one.
I think Joaquin has some… some… More questions on this PR just now.
So,
**Aditya Reddy** 03:50 Yep, sounds good, I'll take a look.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 03:53 Alright, server size stitching… Okay, so this one is actually approved, I'm gonna merge it right now, Can I merge it?
Right, well, I'll merge this after the meeting.
**Aditya Reddy** 04:21 Thank you.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 04:23 And then… typing, even context.
Right.
**Aditya Reddy** 04:32 Yeah, this is the next part. Yeah, this… this will… just want someone to take a look.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 04:39 Okay, so this is the follow-up to the document spam. Yeah. Okay, great.
Correct, yeah, I'll take a look at this after.
**Aditya Reddy** 04:51 That's good, thank you.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 04:55 Cool. Dan, I have just a quick, quick follow-up on last week's discussion on the base URL. I think that's blocking some… some additional work, so I… I think we had an agreement last week.
Just to summarize… on Quick Start, we would keep the single base URL.
And in the Storm Browser SDK, we would not have it, and we would require the exact URLs per signal.
If you have any objections, please raise it now, otherwise I will tell the author on the PR to make these changes.
So we can move forward.
**Joaquin Diaz** 05:44 I think… I remember asking about, like, V1 logs and V1 traces. Is that something that never changes for any collector?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 05:58 Well, I'm not… yeah, I… I'm not aware of there being… like, I mean, obviously we're still on V1,
**Joaquin Diaz** 06:09 Yeah, that's fine anyways, like, you can still provide a full path if you need to, right?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 06:15 Yeah, yeah.
**Joaquin Diaz** 06:16 Okay, that's fine.
**David Luna Bistuer** 06:19 DV1 means the spec version.
of the RTLP protocol.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 06:25 Yeah.
**David Luna Bistuer** 06:26 I guess.
So, I guess… if… If it changes, maybe, and it requires an update on the SDK, at least on the exporters.
So, maybe it would require a brand new version, so I guess… Would it be possible… Yeah, I think it's finally.
Yeah, yeah. It would be possible that an SDK version is tied to the version of the protocol, so… We can say that at a certain point. Let's see… let's pretend that we're reaching a V2 of the protocol.
That means that, I don't know, the… 1.X version of the SDK.
works with Protocol D1.
And then, the next version, maybe a major, we don't know, but that freaking change.
That's the one that supports the V2 protocol.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 07:18 Yeah.
**David Luna Bistuer** 07:20 Yeah. Maybe just, you know, the version of the SDK, if the version of the SDK… that's a superposition, but if the version of the SDK is… Tied to a version of the protocol.
then this V1, V2 just changes on the next version.
On the next measure, and that's it.
**Joaquin Diaz** 07:39 you still have people working with older collectors, so I think, again, I think it's fine, given that this is a quick.
**David Luna Bistuer** 07:47 Pardon.
**Joaquin Diaz** 07:48 I think it's fine if the default case covers 90% of the cases, and then you… if you have an option to set whatever URL you use, then that's okay.
**David Luna Bistuer** 07:58 Yeah, okay.
Agree.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 08:05 Great, Right, so that's the, that's all we have. Does anyone have anything else?
Okay, so… so I think, David, you, you, you said… you mentioned that maybe we could look at the roadmap?
**David Luna Bistuer** 08:30 Yeah, could be a great idea.
lately we have many movement… a lot of movement in the fixing the SDK, doing a lot of things, and then also instrumentation, so I'm not… Okay, I guess I can check all of the issues, but don't know the… the exact point when we are in the migration. I think that we are close to the… finish it.
And then, if we have that, then I review in the roadmap what is next on the roadmap, maybe you can focus on something else, or… The code repository, the people in the node land, they had this… usually they set a milestone, and they set some… focused topics, so they reviewed from time to time, they review, and they did put things on top of the roadmap.
what's next? So, what's the appetite from the people from the SIG, so… And what's a hot topic for the next quarter or so.
So I think that maybe we can just have a look here and see… Like, something… something like that, so let's see.
But it's bad for the people that we are around here, and that's what we addressed of all of us and say, okay, that's… We should focus on this, we should focus on that, and… And, I don't know, maybe set a milestone or something like that.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 09:49 Okay, yeah.
So I guess our… Priority has been… this consolidation, that was, like, the number one priority so far, right? Would it make sense to, just go through… this is, like, the main tracker issue here. Would it make sense to go through the ones that are still open and see what's left, and if anyone is blocked, or… If you're looking for somebody to help here.
**David Luna Bistuer** 10:19 Yeah, it was good.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 10:21 Okay.
I don't see so much.
Okay, so this one… Okay.
So do we have, I don't actually added… do you know… Were you planning on working on the deprecation in the contrib? Is there… PR for that, oh, maybe this one.
So maybe this is still something that needs an owner for actually deprecating it in… Duplicate the navigation instrumentation in Contrib.
Okay, let's see…
**Maxime Quentin** 11:52 I can, have a look, I think. I don't know, I don't have any ATA, though, but, These are some, some tasks I can help. I was, planning to work on the longer task migration.
But if you think this one is more proprietary, I can look at it.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 12:13 Okay, yeah, it should be pretty easy.
Yeah, so I'll… Eddie, like, did you plan on working on this, or is it okay if I assign it to Maxime?
**Aditya Reddy** 12:23 Yeah, that's okay.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 12:28 Hmm… I think I might… you might have to, actually comment on this.
**Maxime Quentin** 12:37 Yeah, I'll try to find the issue when… Two, three eights.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 12:45 Okay.
Yeah, yeah, if you comment on it, I'll assign it too.
**Maxime Quentin** 12:49 No, I'll find it right now.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 12:54 Alright, this one… This is… okay, so this is, let's see… Also, this exists in… Okay, this is on me, so… I'll… I'll… Follow up on this one.
Alright, then we have WebCommon… Mmm…
**David Luna Bistuer** 14:00 It was migrated already, so I think it's the deprecation part that is missing. So I think that most of it, or all of it.
It just, requires the replication part.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 14:10 Okay.
**David Luna Bistuer** 14:14 But at least the GRETME file and deprecation warning, we should add it, and then… Run npm deprecate.
Maybe a question would be.
We just deprecate and, update now, and then in a future version, I don't know, maybe just plan it for… Couple of months, or quarter.
Then ask, to NPM deprecate to actually run the npm deprecate command for all of them.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 14:55 So, like, to plan the self-deprecation of all of these packages,
**David Luna Bistuer** 14:59 Yes, so… Yeah, so first, I think that for other packages I've seen that they just put, kind of, a notice first, and they read me file, and then a warning, and then they give you, kind of, an amount of time, so I think it happens with Fastify.
testified, they, just not duplicate, but they just remove the packets completely.
So first data deprecation.
They advise to change to the new native instrumentation, the distribution, diagnostic channels.
And then I think it was kind of, they announced that in 6 months, half a year, I think it took… then it took a little bit longer, but it was a half year. They just decided to… just removed completely. In our case, would be, well, deprecated and just not… published anymore.
Any other versions, Yeah, but they give you kind of a, you know, that period for people to migrate, and… To the new instrumentation, or, yeah, to using the… Relative institution, and so on, so maybe you can do something similar, so first… call the Redmi file, and then give it an amount of time to people for migration, and then just… Well, NPM Deplicator actually doesn't remove anything, it's just, you know, you get a warning when you're installing it.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 16:22 And, like, the, but, I mean, we could still deprecate it in NPM, right? So, like… Like, we could do that right now.
**David Luna Bistuer** 16:31 Yeah, whatever you like. So, yeah, the… Yeah, you get the message both sides, so you get the message when… when you're installing, and you get the message if you… if you use the data, and also… I think I watched this… PR, it's a smart PR that was from Comdrift.
What was it precaping the long task?
We just want something so when the installation is constructed, it's created.
It just deprecates.
If you look at the files.
You'll see that the… it's just… Just log in a warning in the construct, we'll say, go.
That's deprecated, just long elimination frames.
So, we can do this, we can do both.
Or we can do this first, and then… run npm deprecate a bit later.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 17:22 Yeah, I think, I think the, to call us to, to do the self-deprecation first, and then… then once… once the, when it's… it's released with the messaging and the README, then do… do the actual NPM deprecate.
And I guess the remaining question is, like, do we want to just remove those packages completely out from the repo, the source, at some point?
**David Luna Bistuer** 17:49 At some point, but I would say that, you know, not… not this year, for sure.
**Joaquin Diaz** 17:55 Eventually.
**David Luna Bistuer** 17:57 Maybe a Christmas gift for next year? Something like that.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 18:00 Yeah.
Yeah, I mean, that sounds good.
I guess, Maybe I'm… I don't have to go through all these, but
**David Luna Bistuer** 18:15 No, no.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 18:15 Yeah, does anyone, like, have… need to call out anything here that's blocking?
Alright, so I think… We should just, yeah, try to finish these, finish these up,
**David Luna Bistuer** 18:36 But then the status is that, so let's do the soft application or the log message in the constructor?
An updated arrhythmia of the… of the instrumentations?
So people get noticed when they update.
At least on the adapt tools, they get the warning, then… We can just, I don't know, maybe next year, next quarter, we can just, as for NPM deprecations.
So they don't get the… Yeah.
**Joaquin Diaz** 19:05 Did you add the ad deprecated on the exports?
**David Luna Bistuer** 19:11 I think I forgot that in that PR, maybe we should, yeah, update that PR.
**Joaquin Diaz** 19:17 I think we should also do that.
**David Luna Bistuer** 19:19 So they also get the degrees and the types, right?
**Joaquin Diaz** 19:23 Yeah, it's more basic.
**David Luna Bistuer** 19:24 Small.
**Joaquin Diaz** 19:25 on their IDE, I think.
Like, maybe they don't really beat me, or maybe they missed a log, but if you see, like, something crossed out on your IDE, I think that touches your eye more.
I'll be kudos for that.
**David Luna Bistuer** 19:42 Okay, I'll coordinate the pass through these once, and then, yeah.
See what's missing for all this, and… And maybe ping some people to help me.
Depending.
I'll do something in the Browser channel.
Okay, thank you.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 20:04 Thanks, David.
Alright, let me just go to the roadmap, Yeah, so what's… what's kind of the next… after the consolidation is done, what's… That's the main thing that we want to focus on.
There is… We've worked on the instrumentation, the Fetch NXHR, which is great, an instrumentation base.
So I think this is actually in… Connect in a good state.
The semantic convention stability, so the progress there, the main thing is the spin-off of the new registry.
And there's some progress happening there, and that's the dependency, that we have there.
But I… I can continue driving this, this part.
We have worked on the SDK, and we continue making, you know, improvements there.
Session tracking, resource detection… Configuration consolidation… Examples in Sandbox… we don't really have this documented, the browser's compatibility and support. I think that would be good to have.
I think there's a big, kind of, open… open question around, sessions and page context. I think… as far as, like, should they be entities, and, like, we need that prototype, for the entities, sessions as entities. There's potentially some spec work, so this is a big area, potentially still open.
metric strategy, an API surface, Yeah, we just introduced the API package, so, that kind of… if… if you need any new APIs that are browser-specific, we could… Gonna focus on that, Or metric strategy, which also would require spec work.
So, from all these… What do you think?
**Joaquin Diaz** 23:00 I think, like… most of them are in a good shape, separate sessions, which I think we've been talking about in the past, but we… Kind of stuck on the entity's implementation, so… If there is something that we can do to move forward on that front, or even… Not depending on entities, and thinking out about a way of… Having a better session and paid support without them.
At least, like… I know we always say that the idea of using MCC is to all the way, they… Tagging everything with session and page attributes, but… In the meantime, if that's the only way we have currently, it's better than nothing.
And it's also optional, so if users don't like that, they can skip it, but I think it's useful.
To have some sort of say of how we can tag things.
At least for now, with sessions and page.
We could also, like, if we have a model that works, I don't think it matters whether It's just attitudes on every… span our log of existing entity. If the model works, then we can move it.
from… arches to entity.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 24:30 Yeah, I mean, I think this is… this is kind of a big, big chunk of work in my mind, because it, requires, like, some… potentially some significant changes in the SDK.
And it might have to be spec'd out as well, And we do have a prototype, now, so I think it's… Yeah, there was a… there was a… Like, a couple of months ago, we had… we were talking about… maybe… There was a need to spin off, like, a separate working group to work on sessions in general.
Which I think would include this, this question of entities.
But also… you know, things like API around sessions, events around sessions… Like, if there's any more data modeling that needs to be done around sessions, like… In addition to session ID.
And then, like, bring that to the spec, because I think that's work that, you know, other clients SDKs would benefit from as well, like mobile.
**Joaquin Diaz** 25:51 So is that something that we want to go through, or… We can shift the focus to pages that we know that are browser-only.
So we don't need to go through other six, and that's also useful for every, like, Browser user.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 26:08 Yeah.
David, do you have any thoughts on this?
**David Luna Bistuer** 26:23 Well, sessions, it's quite complex, yeah.
Maybe all would separate some… well, sessions and place conflict zone. Thinking about entities, yeah, so kind of on the same category, but maybe we should split them.
I'm adding sessions as, okay. Topic at its own, and then page context on another… on another level.
Yeah, well, I'm thinking about it, maybe it's possible to… Well, first, on everyday roadmap that we have, kind of, we know that we are in a good shape, would be kind of a way of acknowledging that, or marking that we are in good shape.
maybe I'll update that document, and then on sessions, the other working group, if we want to share an API with, with other clients, like mobile, yeah, we should… we should, start a group again, and having conversations again with sessions.
I have something that maybe next week I'll show you.
I don't know, I'm a bit sad.
But yeah, maybe we could, we could serve, that could be kind of the… Just the material to just start that discussion, but this discussion.
So, as I see it right now, it's like, okay, so… You're, you're telling that the semantic message registers are still in progress?
Right.
Yeah, yeah. That's another topic that I think is interesting to consolidate in some of the conventions, a list of browsers, at least.
From the instrumentations.
we have, at least… at least we are in Elastic, we are… we are already using that, and I think that we… we have real use cases, and it makes a lot of sense to have these… some of the conventions from the… the different instrumentations.
So, starting to promote this as a… To stabilize those.
Would be a good idea.
And then, yeah, on sessions, maybe we can start discussing with this group.
**Joaquin Diaz** 28:36 I can take the lead on the page discussion, I work on that on our own SDK.
I think I will start with an issue with the use cases on why.
**David Luna Bistuer** 28:48 Exactly.
**Joaquin Diaz** 28:49 we will use pages and, like.
But that's a… I think we… This is something that we discussed at the beginning, like, what does a page means, and it was difficult, like, everyone has their own.
definition.
**David Luna Bistuer** 29:01 As I said, yeah, as I said.
**Joaquin Diaz** 29:04 Yeah. So I'll try… I think we should start with a consolidated definition that works for everyone, and think of, like, what do we need from pages, and what do we want to… give users on this, so I can start with that, start a discussion, and then we can see how it goes from there.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 29:24 Sounds good.
And I can continue owning or driving, like, the semantic elevation stability and, I'm not sure that I have… I would really like to work on the sessions, I don't know that I have Capacity, like, to drive that working group.
But maybe I could, pair with you, David, if you're interested.
**David Luna Bistuer** 29:47 Okay.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 29:48 on this, and… I also think that, maybe we can… still, like, we're still, like, kind of in an experimental state on… in the SDK, like, we could maybe, kind of drive a prototype, how we kind of think that it should work for… would work for us, and then we can… that would be, like, a beneficial thing for… to bring, to whatever that group is.
When it spins up, Hmm.
Yeah.
**David Luna Bistuer** 30:21 Okay, that sounds good, yeah. Ping me, and then we'll see how we can organize it.
Okay, so yeah, so… what I got it is, like, okay, we can work towards, deprecation and consolation of the packages.
So we can start already deprecating. I think we got already all of them, so we have even document load.
Which was temporarily gone and then back.
So we can work towards that, so that would be a focus on deprecating things, and then… Luring people to new implementations.
Then the sessions, definition, and working group, and then the, page, also page context, and then, The semantic conventions, so that could be… Kind of the thief.
Focus topics and all the… They're putting things together right now.
If you agree with that?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 31:19 I do. Okay. Yep.
**David Luna Bistuer** 31:21 Okay, good.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 31:25 Alright, sounds good, good discussion. We're at time, so any, any last comments before we… Closed for today.
Alright, alright, sounds good. I will see you on Slack, and…
**David Luna Bistuer** 31:41 Okay. Have a good day.
**Maxime Quentin** 31:43 Yep.
**David Luna Bistuer** 31:44 Bye.
**Chris Chestnut** 31:44 Good morning. Take care.
