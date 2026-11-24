SIG: Project triage - EU-friendly
Date: 2026-11-23
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Robert Pająk (Splunk Inc.)** 04:17 Hello, Pablo.
**Pablo Baeyens (Datadog)** 04:19 Hey!
Good morning. How's it going?
**Robert Pająk (Splunk Inc.)** 04:22 Good morning. Fine, how about you?
**Pablo Baeyens (Datadog)** 04:24 I'm doing okay. Bit of a cold, I think.
**Robert Pająk (Splunk Inc.)** 04:27 Yeah, I just wanted to ask if you have any flu or something like that, because a lot of people here in Poland are getting flus right now, because it's getting colder.
**Pablo Baeyens (Datadog)** 04:35 Yeah.
**Robert Pająk (Splunk Inc.)** 04:36 hotter, warmer, and yeah. Today we had even snow in Krakow.
**Pablo Baeyens (Datadog)** 04:40 Oh, nice. Now, here is nowhere that.
**Robert Pająk (Splunk Inc.)** 04:43 I know, I know. Don't often be doing yourself, right?
**Pablo Baeyens (Datadog)** 04:48 Yeah, no. I mean, we had a… Like, 3 or 4 years ago, we had snow, but not this year.
At least not at the city level, there's a mountain range nearby that does have a lot of snow.
It's where people come to ski in Spain.
**Robert Pająk (Splunk Inc.)** 05:05 Okay.
**Pablo Baeyens (Datadog)** 05:07 I don't know if… There will be anybody else joining, cause…
**Robert Pająk (Splunk Inc.)** 05:14 I know that's Severin, not sure about Dan, I do not remember.
**Pablo Baeyens (Datadog)** 05:17 I think Don is on vacation.
**Robert Pająk (Splunk Inc.)** 05:19 Yes, you are right.
**Pablo Baeyens (Datadog)** 05:23 Yeah, so…
**Robert Pająk (Splunk Inc.)** 05:25 If we want, you can just quickly go through the issues. I don't think there are a lot, hopefully.
**Pablo Baeyens (Datadog)** 05:31 Okay, yeah, I'll just do that.
**Robert Pająk (Splunk Inc.)** 05:35 Especially as we are, you know, December is coming, and we'll be cancelling the meetings anyway in… two weeks, so…
**Pablo Baeyens (Datadog)** 05:41 Yeah. Probably, yeah. Okay, let me… I mean, if you're ready to share your screen, feel free to do so. If not, I can…
**Robert Pająk (Splunk Inc.)** 05:51 you can share, I also need to double-check, our meeting on… Wednesday?
If I'll be able to join.
This is one.
**Pablo Baeyens (Datadog)** 06:03 Hmm.
This is… The blue one to shoot her right? Yeah.
Okay, can you see the list of issues?
**Robert Pająk (Splunk Inc.)** 06:18 It gives me sex.
I'm just checking, you know, did, our TC, TC, GC call.
That we are having, and I check if I can make it.
Okay, I may be late.
But I should be there.
Alright, so right now… yes, I can see your screen.
**Pablo Baeyens (Datadog)** 06:43 Cool. Yeah, I guess let's start with this one.
Okay, this is probably, SIG issue for the sampling SIG?
**Robert Pająk (Splunk Inc.)** 07:20 I'm just not sure, wire format OT equals ZC, Isn't OT.
Or…
**Pablo Baeyens (Datadog)** 07:32 for the trace state, I think, is, like, the…
**Robert Pająk (Splunk Inc.)** 07:39 Right.
**Pablo Baeyens (Datadog)** 07:40 Hi, I mean… Unless you think otherwise, I think… This is probably a simplistic thing that doesn't need… Yeah, okay, so then I'll put, say, the issue, and something… sick.
**Robert Pająk (Splunk Inc.)** 08:04 Do they have also some, some, Team, so that we can notify them, because otherwise they won't be notified.
**Pablo Baeyens (Datadog)** 08:16 Oh, well, I mean, JMUCD is one of the…
**Robert Pająk (Splunk Inc.)** 08:19 Okay.
**Pablo Baeyens (Datadog)** 08:20 Most involved, too.
**Robert Pająk (Splunk Inc.)** 08:21 you, okay.
**Pablo Baeyens (Datadog)** 08:22 Yeah.
**Robert Pająk (Splunk Inc.)** 08:22 Okay, awesome.
**Pablo Baeyens (Datadog)** 08:24 Yeah, so I think we can leave it like that. Okay, this is probably also SIG-specific for the Prometheus SIG.
**Robert Pająk (Splunk Inc.)** 08:34 Okay, yes, indeed.
**Pablo Baeyens (Datadog)** 08:37 Okay, so let's, seek issue. Is there a Prometheus label? Yeah.
Room, if you'll see… Cool.
Same thing… Notice the same thing.
**Robert Pająk (Splunk Inc.)** 09:10 Yes.
**Pablo Baeyens (Datadog)** 09:11 Yep.
Prometheus… Bromy fuse.
Mmm…
**Robert Pająk (Splunk Inc.)** 09:35 I don't think we have a special sick or self-observability, but I think it can be.
**Pablo Baeyens (Datadog)** 09:39 Hmm.
**Robert Pająk (Splunk Inc.)** 09:40 Who's sponsor?
**Pablo Baeyens (Datadog)** 09:42 With David being the sponsor.
**Robert Pająk (Splunk Inc.)** 09:44 David.
**Pablo Baeyens (Datadog)** 09:46 So, ready with sponsor.
Oof…
**Robert Pająk (Splunk Inc.)** 10:35 You can make me a sponsor, I can review it, I was changing it some time ago.
**Pablo Baeyens (Datadog)** 10:39 Okay.
**Robert Pająk (Splunk Inc.)** 10:41 You can double-check later.
It looks like clarification, but I'm not sure.
**Pablo Baeyens (Datadog)** 10:45 Yeah, it doesn't look like something that would be too controversial, but I don't… I'm not super familiar with that part of the spec. Should I put… Like, community feedback until you,
**Robert Pająk (Splunk Inc.)** 10:58 I can always change it. I can… you can make it an accepted, there's a… yeah.
No, cryptically.
**Pablo Baeyens (Datadog)** 11:04 community feedback, and you can put it,
**Robert Pająk (Splunk Inc.)** 11:07 Okay.
**Pablo Baeyens (Datadog)** 11:07 This is… probably protocol?
Yeah, either protocol or a common. I'll put protocol.
**Robert Pająk (Splunk Inc.)** 11:21 Okay.
Can you assign me? Or have you done?
**Pablo Baeyens (Datadog)** 11:30 Yeah, I already assigned you.
Deez.
Gay… This is yours…
**Robert Pająk (Splunk Inc.)** 11:52 I just… there was a long, a long-standing PR, which had even a lot of approvals. I decided to close it, especially that I personally, Yeah, I… I think it will still take a couple of months, or maybe longer, until we're really able to deprecate the…
**Pablo Baeyens (Datadog)** 12:14 Hmm.
**Robert Pająk (Splunk Inc.)** 12:14 API tracing, so I just thought I would just do not want to deal with the scalebot VPR at this stage, just to move it to, you know.
**Pablo Baeyens (Datadog)** 12:22 Yep.
**Robert Pająk (Splunk Inc.)** 12:23 But…
**Pablo Baeyens (Datadog)** 12:24 Okay.
**Robert Pająk (Splunk Inc.)** 12:24 It's kind of blocked.
I think it's also… And I'm not sure if it's possible… I recently saw that it's possible to do a relationship with Blocked in GitHub.
But…
**Pablo Baeyens (Datadog)** 12:38 You can mark as blocked by another issue.
**Robert Pająk (Splunk Inc.)** 12:41 Yeah, I'm not sure. So, we can do it even, I think, right now. Stabilized recording exception. You see that, Yeah.
**Pablo Baeyens (Datadog)** 12:51 this.
I don't know if you can do being blocked by another route.
**Robert Pająk (Splunk Inc.)** 12:55 I know.
I know.
That's right.
**Pablo Baeyens (Datadog)** 12:58 Yeah.
Okay, yeah, it seems like you can.
Zoom on deep… conventions, and then which one is it? 3554.
This one, right?
**Robert Pająk (Splunk Inc.)** 13:15 Yes.
releases.
**Pablo Baeyens (Datadog)** 13:18 We're close.
**Robert Pająk (Splunk Inc.)** 13:19 Okay.
**Pablo Baeyens (Datadog)** 13:20 That worked.
**Robert Pająk (Splunk Inc.)** 13:22 Or, I'm not sure.
Hard to say.
**Pablo Baeyens (Datadog)** 13:25 I mean, is this part of the OTEP?
**Robert Pająk (Splunk Inc.)** 13:28 Like… Yep.
**Pablo Baeyens (Datadog)** 13:29 Okay, then I would put, like.
accepted, ready with sponsor, with you as the sponsor, maybe?
I mean.
**Robert Pająk (Splunk Inc.)** 13:36 Yeah, I propose to put it in community feedback, so that someone does not recreate the issue, because it's still blocked, so… Okay. I'm not sure.
**Pablo Baeyens (Datadog)** 13:45 Okay, let's put… let's put community feedback then. I mean, you know, it's not ready in the sense that it's blocked by the other issue, right? So, yeah.
Okay, I think this is… Okay.
bills, like… Should it be controversial, but I don't know.
**Robert Pająk (Splunk Inc.)** 14:17 I don't think it's controllable, sure.
**Pablo Baeyens (Datadog)** 14:20 Okay.
Let's do… Ready, we sponsor, and oops. If it will be converted.
**Robert Pająk (Splunk Inc.)** 14:31 Certain people will just, you know, complain on the PRs.
**Pablo Baeyens (Datadog)** 14:37 Okay, alright.
**Robert Pająk (Splunk Inc.)** 14:38 I think he's already in development, this is about only stabilization.
**Pablo Baeyens (Datadog)** 14:43 Yeah, it's only about marking it as staple, yeah.
Can we… Okay…
**Robert Pająk (Splunk Inc.)** 15:18 Can you scroll down? Is somebody responded?
Okay.
That's what I thought. I think it's a CU show.
And…
**Pablo Baeyens (Datadog)** 15:27 Or the entity sig?
**Robert Pająk (Splunk Inc.)** 15:28 Entities, yeah, so I'm not sure what I told them, yeah.
these entities.
**Pablo Baeyens (Datadog)** 15:32 Is there an entities?
**Robert Pająk (Splunk Inc.)** 15:34 Yeah, buddy.
**Pablo Baeyens (Datadog)** 15:36 There's this… yeah, I'll… And then… I'll add it to the entities.
There's only entities Phase 1.
I'm not sure if it needs to be added to Phase 1.
**Robert Pająk (Splunk Inc.)** 15:53 So, maybe just let's ping them.
**Pablo Baeyens (Datadog)** 15:56 Yeah, okay.
Cool.
And I think that is… It, and then we should look at the ones with… follow up.
Cool. There's quite a few.
Okay, and these ones are probably… Okay.
**Robert Pająk (Splunk Inc.)** 16:45 this was something that if nobody cares, then probably it's going to be closed. I think we can close this one.
you can check the Slack message, and I… if I remember correctly, nobody In the last message I… or… oh, maybe I'll just find this right now.
On Slack.
Do some specification or maintainers?
**Pablo Baeyens (Datadog)** 17:09 Specification, there's a comment from Jay McD, but no… Reply, okay. There have been no… I think we can close it, so, I can say…
**Robert Pająk (Splunk Inc.)** 17:24 That's not planned. We can always reopen it.
**Pablo Baeyens (Datadog)** 17:27 Yep, so they're hoping… Mmm, yeah.
Discussion on the optimum.
Who's this, Just a blonde… And we can improve the… Okay, this is also an old one.
There's been no reply in more than a month.
More than 2 months.
I think…
**Robert Pająk (Splunk Inc.)** 18:47 Oh, cool.
**Pablo Baeyens (Datadog)** 18:48 Absolutely.
**Robert Pająk (Splunk Inc.)** 18:48 If I remember correctly, only Java did it, and I'm not sure why they did it.
**Pablo Baeyens (Datadog)** 18:54 I think we can close it, yeah. So… Oceans is still hospice.
Follow up.
Shouldn't… Okay… Did we close it? Yep.
Additional response status for cancellation.
Oh, I could tell.
**Robert Pająk (Splunk Inc.)** 19:55 row of 5 adults.
it was never discussed by the TC, or I…
**Pablo Baeyens (Datadog)** 20:04 Okay, and hustling.
**Robert Pająk (Splunk Inc.)** 20:05 Intentional.
What about semantic conventions? Yeah, that's a good question.
**Pablo Baeyens (Datadog)** 20:14 Their activity more recently.
Okay, I think telling… Sorry, not this one, this one.
Telling Thompson to… Bring it up on the specifications CA meeting, maybe a good idea.
**Robert Pająk (Splunk Inc.)** 20:50 Or semantic conventions are involved, yeah.
**Pablo Baeyens (Datadog)** 20:53 Okay Okay, and I'm going to remove the follow-up.
Hi, Dean.
**Robert Pająk (Splunk Inc.)** 21:29 But I think from the specification, if I know also the Mua, I would think that probably it will be just a type of the error, that's my guess.
**Pablo Baeyens (Datadog)** 21:41 So you mean…
**Robert Pająk (Splunk Inc.)** 21:42 No.
**Pablo Baeyens (Datadog)** 21:43 should…
**Robert Pająk (Splunk Inc.)** 21:43 It's a status error, it's not… It's not an attribute.
Yeah, that's problematic.
Because we also have an attribute.
Or errors, yeah.
Yeah, let's keep it… let's just keep it discussing.
Later.
**Pablo Baeyens (Datadog)** 22:05 Okay.
**Robert Pająk (Splunk Inc.)** 22:06 And let's go to the next one.
**Pablo Baeyens (Datadog)** 22:08 Next one… This one from David… wasn't David working on this?
Sundvanel.com.
**Robert Pająk (Splunk Inc.)** 22:18 Can you keep…
**Pablo Baeyens (Datadog)** 22:18 Yeah, this one.
Maybe I can ping David and tell him, like, If there are any updates… Okay… Next one… Any…
**Robert Pająk (Splunk Inc.)** 23:41 follow up. We are still discussing it with CAIC. You can consider putting it as CAICD or semantic convention. This is kind of…
**Pablo Baeyens (Datadog)** 23:56 Well, it feels a bit more general, right?
I would just remove the follow-up if you are discussing it on…
**Robert Pająk (Splunk Inc.)** 24:04 Yes, we are.
**Pablo Baeyens (Datadog)** 24:05 Okay.
Then I'll just remove the follow-up, and we can… Look at it later.
**Robert Pająk (Splunk Inc.)** 24:12 We're discussing it, like, almost at least each month, if not more frequently.
**Pablo Baeyens (Datadog)** 24:18 Okay.
Well, I'll follow up if it's… if it becomes annoying to review it every time we'll think about what to do.
**Robert Pająk (Splunk Inc.)** 24:37 Hmm?
**Pablo Baeyens (Datadog)** 24:41 Okay… Have you been discussing this in any way on the TC, or…
**Robert Pająk (Splunk Inc.)** 24:52 I never remember about it. I don't know. At least since I'm at EC, I never remember discussing this.
**Pablo Baeyens (Datadog)** 25:00 Okay, should I… pink JMOCD again, or just… close it until they might need to reopening it if it's…
**Robert Pająk (Splunk Inc.)** 25:12 I'll just cause it, to be honest.
It takes longer.
**Pablo Baeyens (Datadog)** 25:16 Okay.
Boom… Melinda quota.
**Robert Pająk (Splunk Inc.)** 25:25 I'm also not convinced on this one, because then, do we want to have flags if there's, I don't know, a lock related, you know, to S-PAN? I think, if there's a profile related to S-PAN, do you also do have flags? I think… I don't think it's a good idea to… To add these features, you know.
**Pablo Baeyens (Datadog)** 25:59 API definition for blank provider.
**Robert Pająk (Splunk Inc.)** 26:07 Configuration set.
**Pablo Baeyens (Datadog)** 26:09 Yeah.
GitHub reopen it.
Okay, yeah, I'm going to put configuration's sake.
And… Just limit to… Junk.
Sorry, this is the one we were just discussing…
**Robert Pająk (Splunk Inc.)** 26:44 I think this is accepted. Could you scroll down? I think… No? Okay.
**Pablo Baeyens (Datadog)** 26:51 Does it look like it?
I mean, if you think it's accepted…
**Robert Pająk (Splunk Inc.)** 26:55 I think there was a separate PR, but I think… no, it was not about sampling, I think.
**Pablo Baeyens (Datadog)** 27:03 Do you remember if the PR was by CJO?
**Robert Pająk (Splunk Inc.)** 27:08 If it was, then it was by Tyler. I remember Tyler was… or maybe he was just proposing an issue, but I think it was something different. It was also connected to something in the metrics.
also clarification, but I think it was a different thing.
No, it's all something different.
**Pablo Baeyens (Datadog)** 27:28 Okay.
Any idea what to do here? Should I tell CJ to go to SpecSeq?
**Robert Pająk (Splunk Inc.)** 27:40 Teacher will not have time, I think, right now.
**Pablo Baeyens (Datadog)** 27:46 Or, I mean, find somebody else who represents.
**Robert Pająk (Splunk Inc.)** 27:49 years.
**Pablo Baeyens (Datadog)** 27:49 a spec suit.
**Robert Pająk (Splunk Inc.)** 27:51 Yes, or metrics are perverse, or… yeah, exactly.
**Pablo Baeyens (Datadog)** 27:56 Or, I mean, I can just ping Metrics Approver again on…
**Robert Pająk (Splunk Inc.)** 28:00 You can also think a specification approvals as well.
Because…
**Pablo Baeyens (Datadog)** 28:05 Okay.
**Robert Pająk (Splunk Inc.)** 28:05 It's bigger.
**Pablo Baeyens (Datadog)** 28:09 Spec sponsors… what's the difference between spec sponsors and specs provers? I thought that was the same.
**Robert Pająk (Splunk Inc.)** 28:15 sponsors… I think spec sponsors… I don't know.
Question?
**Pablo Baeyens (Datadog)** 28:21 I think we're Sponsors is the one I want to ping?
**Robert Pająk (Splunk Inc.)** 28:25 Yep.
I think you're right.
**Pablo Baeyens (Datadog)** 28:29 Okay, I'll follow up.
Spotato.
**Robert Pająk (Splunk Inc.)** 28:41 I think this can be closed, can you check if I remember some of it?
**Pablo Baeyens (Datadog)** 28:59 So do you think this should be closed as, like…
**Robert Pająk (Splunk Inc.)** 29:02 Yes.
**Pablo Baeyens (Datadog)** 29:03 your answer…
**Robert Pająk (Splunk Inc.)** 29:04 Yes?
**Pablo Baeyens (Datadog)** 29:05 Okay.
**Robert Pająk (Splunk Inc.)** 29:06 Exactly.
**Pablo Baeyens (Datadog)** 29:07 This goes through your entry now.
**Robert Pająk (Splunk Inc.)** 29:17 Okay, kind of.
There is one thing, that units are only for metrics, but not for spun attributes.
But…
**Pablo Baeyens (Datadog)** 29:30 I think there's some discussion about,
**Robert Pająk (Splunk Inc.)** 29:34 Yes, I also.
**Pablo Baeyens (Datadog)** 29:34 cylinder.
**Robert Pająk (Splunk Inc.)** 29:35 I think there was a separate issue for it.
**Pablo Baeyens (Datadog)** 29:39 Maybe on…
**Robert Pająk (Splunk Inc.)** 29:40 Probably even a little.
**Pablo Baeyens (Datadog)** 29:41 tofu.
No, I don't see it here.
**Robert Pająk (Splunk Inc.)** 29:46 Specification, drink specification, I think using specification.
**Pablo Baeyens (Datadog)** 30:02 Nope.
Specifically… I would have sworn that the profiling SIG was interested on having units for attributes in general.
**Robert Pająk (Splunk Inc.)** 30:28 But this is, yeah…
**Pablo Baeyens (Datadog)** 30:32 Apparently that's not bad, See all the question, or Harvey.
**Robert Pająk (Splunk Inc.)** 30:39 still, it will be probably, right now, semantic conventions, in my opinion. If that will be solved, then probably it will be solved by, you know, semantic conventions, and not changing the attribute, you know, fields, etc. So…
**Pablo Baeyens (Datadog)** 30:51 Yeah.
**Robert Pająk (Splunk Inc.)** 30:52 Maybe it's… maybe it's there. That's a good question.
**Pablo Baeyens (Datadog)** 30:57 Mmm…
**Robert Pająk (Splunk Inc.)** 31:01 Woohoo.
**Pablo Baeyens (Datadog)** 31:02 There's a lot that mention units, and I don't know how to refine the search.
**Robert Pająk (Splunk Inc.)** 31:06 I know. Span?
Maybe this one delay?
**Pablo Baeyens (Datadog)** 31:13 Spawn unit.
Doesn't look like it.
**Robert Pająk (Splunk Inc.)** 31:23 No, we can take… it's everything, right?
Your normal pages.
**Pablo Baeyens (Datadog)** 31:28 No, that's everything, yeah.
Okay, I'm gonna say… We think this can be discussed in a more generic way, Sim.
What are use cases for this?
Sign.
Feel free to open an issue.
Does that sound… Yeah, reasonable. Okay.
Cool.
**Robert Pająk (Splunk Inc.)** 32:25 You can remove the follow-up.
**Pablo Baeyens (Datadog)** 32:28 Okay.
Look at this.
**Robert Pająk (Splunk Inc.)** 32:33 You can clo… you can probably mark it as spam or something like that.
Or remove.
It's a comment.
**Pablo Baeyens (Datadog)** 32:40 I think, yeah, I think they were just trying to translate the… comment to Spanish, I'm gonna say off-topic.
Generic opt-in mechanism for events.
**Robert Pająk (Splunk Inc.)** 33:01 A general request for events? Opti in my hand.
Oh, Jesus.
**Pablo Baeyens (Datadog)** 33:16 Okay…
**Robert Pająk (Splunk Inc.)** 33:17 follow up.
**Pablo Baeyens (Datadog)** 33:18 Yeah, I think, like… Since Lyudmila said we should wait, let's just remove follow-up.
Okay, two. As one format for OpenTelemetry, I mean, my hunch is that this is not a spec issue, but…
**Robert Pająk (Splunk Inc.)** 33:41 Yes, I recently was talking… I think I… discussed some time ago about really what this… why the security things are not in the specification repo, and he said that, in his opinion, this could be orthogonal, meaning that, you can evolve and have, you know, have, for example, V2 of the specification, and still have the same… and have some kind of criteria for security, and also the.
**Pablo Baeyens (Datadog)** 34:11 It's incredible.
**Robert Pająk (Splunk Inc.)** 34:12 criteria could be used in other places if you are not complying to this OPA telemetry specification. Like, I don't know, OPAMP, I don't know if OPAMP.
**Pablo Baeyens (Datadog)** 34:21 Yeah, or the collector, to some extent, yeah. Yeah.
But Ted's argument is that the SPOM definition would live in the spec?
**Robert Pająk (Splunk Inc.)** 34:42 I don't know why.
**Pablo Baeyens (Datadog)** 34:47 Maybe I can ping… Seek security…
**Robert Pająk (Splunk Inc.)** 34:53 Yeah.
**Pablo Baeyens (Datadog)** 34:55 Approvers, maybe?
Do you think this issue should… Sorry, I can't cry for some reason. Should be transferred to the… Does that sound reasonable, seeing here?
Okay.
Remove follow-up, then… And this sounds like a C issue from the title.
Well, is there… Is there a proxy option, actually, on the…
**Robert Pająk (Splunk Inc.)** 35:38 No, they don't have to ask.
exporter, yeah.
I'm in favor of this track.
Yeah, give up, I think.
**Pablo Baeyens (Datadog)** 35:49 Then… Probably I will just remote follow-up.
Chris.
There seem to be a few PRs related to this, you know.
Cool, I think we're done.
**Robert Pająk (Splunk Inc.)** 36:06 I see you.
**Pablo Baeyens (Datadog)** 36:13 Next week… Okay, yeah, I'm in.
I'll be here next week. I won't be able to make it the week after, but…
**Robert Pająk (Splunk Inc.)** 36:22 I have a question.
**Pablo Baeyens (Datadog)** 36:25 It's.
**Robert Pająk (Splunk Inc.)** 36:25 so kind of triage related, and also personally to you. Has Ruiz reached to you regarding the European, the European project meeting on Maintainer Summit, or not?
**Pablo Baeyens (Datadog)** 36:40 She mentioned it, so… you mean the… the project meeting submission? So, we discussed it on the… GC meeting, again, I think Ted… I think Ted is the one that replied to you, right? Like, Ted was more interested on having Prometheus plus OpenTelemetry.
**Robert Pająk (Splunk Inc.)** 37:03 Yes.
**Pablo Baeyens (Datadog)** 37:05 on… I don't know, I mean, honestly, I'm… I think we should have a project meeting, I don't mind particularly which format.
My understanding is that Reese would take care of the submission?
**Robert Pająk (Splunk Inc.)** 37:22 My understanding is similar, but she asked me just, you know, long story short, she asked me if she can do it, and add me as a co-author, and I said that.
**Pablo Baeyens (Datadog)** 37:30 Hmm, are you?
**Robert Pająk (Splunk Inc.)** 37:31 if you and Ted should be co-sourced, or she.
**Pablo Baeyens (Datadog)** 37:33 That's cute.
**Robert Pająk (Splunk Inc.)** 37:34 because these were your proposals, and I do not want to, you know, steal your ideas or do anything behind your.
**Pablo Baeyens (Datadog)** 37:41 Oh, I mean, nobody will be listed for that, so it doesn't really matter much.
**Robert Pająk (Splunk Inc.)** 37:46 I don't know, I never know, I just prefer to be careful, so that, you know, people are She is looking forward.
**Pablo Baeyens (Datadog)** 37:54 I mean, thanks for paying attention to that, but, like, the project meetings don't have, speaker listed, and they don't give you a ticket, so I don't think it matters much. It's more, like, the person, the point of contact. I will… chat with Reece, just to make sure that…
**Robert Pająk (Splunk Inc.)** 38:16 There is submitted, yeah.
**Pablo Baeyens (Datadog)** 38:18 Yep.
**Robert Pająk (Splunk Inc.)** 38:19 Okay.
**Pablo Baeyens (Datadog)** 38:21 And you make a note of that.
I assume you… did you have a talker or something? Will you be attending, for sure, Cube Con EU?
**Robert Pająk (Splunk Inc.)** 38:40 If they are accepted, then I'll be there.
**Pablo Baeyens (Datadog)** 38:42 Okay, huh?
**Robert Pająk (Splunk Inc.)** 38:43 If not… then it will be difficult, unfortunately. This is in Europe, so there's still a big chance that I'll go anyway.
**Pablo Baeyens (Datadog)** 38:51 Mmm.
**Robert Pająk (Splunk Inc.)** 38:51 So, I have more reasons to go there, but unless I'm the only cert… like, if I get my talks to be accepted, it's, like, 95%. If it's not, then it's, like, 60-70%.
Yeah.
**Pablo Baeyens (Datadog)** 39:05 Well… Well, sorry about that. I don't know. It's… I mean, I could understand, like, them not flying you to North America, but the European one seems…
**Robert Pająk (Splunk Inc.)** 39:18 Yeah, maybe it was more to North America, I wanted to go there as well. On the other hand, it's also, you know, it also motivates me to create talks, so… At least I have more motivation, so it's nothing better.
**Pablo Baeyens (Datadog)** 39:30 Freedom.
**Robert Pająk (Splunk Inc.)** 39:32 Yeah.
**Pablo Baeyens (Datadog)** 39:34 Alright.
Well, I'll keep you posted on whatever Reece tells me, but I think it should be fine. I think we had until December 1st, so I'll just remind her before Thanksgiving.
Okay, then… and actually, we have a meeting on Wednesday with the community manager, so maybe I'll just alert there.
**Robert Pająk (Splunk Inc.)** 39:56 Okay.
**Pablo Baeyens (Datadog)** 39:57 I will see you next week.
**Robert Pająk (Splunk Inc.)** 40:01 Yeah, that's this week, or next week.
**Pablo Baeyens (Datadog)** 40:04 Oh…
**Robert Pająk (Splunk Inc.)** 40:05 Will you be… yeah, because, on Wednesday, we have the joint CCGC meeting, or is it not this week?
**Pablo Baeyens (Datadog)** 40:12 No, that's… I think that's… later. That's on… December 9th is the GCTC meeting.
**Robert Pająk (Splunk Inc.)** 40:22 Oh, right.
Double checking, double checking.
Stick…
**Pablo Baeyens (Datadog)** 40:37 and we…
**Robert Pająk (Splunk Inc.)** 40:37 Okay,
**Pablo Baeyens (Datadog)** 40:39 And there's the December 2nd thing, yeah.
**Robert Pająk (Splunk Inc.)** 40:42 It's next week, alright.
**Pablo Baeyens (Datadog)** 40:43 Okay, yeah, that's next week, yeah. Okay, okay.
Yep, okay, yep, thank you. See you.
**Robert Pająk (Splunk Inc.)** 40:54 every cohort.
**Pablo Baeyens (Datadog)** 40:55 Looks good to you. Thank you. Bye.
Bye.
