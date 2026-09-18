SIG: Python SIG
Date: 2026-09-17
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Aaron Abbott (Google LLC)** 00:39 Hey, everyone.
**Tammy Baylis** 00:46 Erin, hey everyone.
**Riccardo Magliocchetti** 00:51 Hello?
**Aaron Abbott (Google LLC)** 00:52 8.
**Leighton** 01:28 Hello.
**Tammy Baylis** 01:39 Hey, Leighton.
I think I might as well just get started. Welcome back to the Python SIG meeting. I'll link to this docs in the chat.
Lots of familiar faces today. We'll just do some triage till 9-10.
These are the boards. We'll start with Contrib today.
We'll start with waiting on reviewers.
I know what this one is. This is someone trying to add a community instrumenter, and… this kind of came at the start of when a lot of new ones came in, and it hasn't been reviewed, but I think it'd be good to wait.
Until Diego's policy, gets sorted out, and it's not being closed anyway, so we'll leave that.
Mmm… I might go bottom up, actually, because these are the old ones.
These are the new ones.
Okay, I know what this one is, it's actually the first topic I listed, so we'll come back to that.
Oh, Joey's PR for a Botto 3SQX fix.
Oh, sorry, Joey's the reviewer. This person's the OP.
Mmm…
**Lukas Hering** 05:07 I can take a look and… But the… I'm more familiar with the AWS stuff.
**Tammy Baylis** 05:14 Okay.
Yeah, thank you, Lucas. There's some issues cited, but it would be nice if it wasn't its own issue, but… Yeah, I'll park this… I think I'll put this in ready to review, might as well.
Oh, no, this one, I believe, was just cited in the other PR.
Yeah… This one has an issue.
Oh, and OP commented here.
Yeah, thank you, Lukas, for looking at this one, too.
That was the issue, right?
Simcom utilities to support messaging stability opt-in.
Medio, thank you.
**Emídio Neto** 06:31 Yeah, this one has some reviews already, but, it's gonna need another look.
reviewers…
**Tammy Baylis** 06:42 Cool.
**Emídio Neto** 06:43 Yeah.
**Tammy Baylis** 06:44 Yeah, awesome.
**Emídio Neto** 06:47 Yeah, there's… comment, I appreciate a fix, so just waiting.
For… Another review.
**Tammy Baylis** 06:58 Awesome.
Right place on the triage board, right place on the digest there.
Another one from Tree Craw.
Linked issue this time, excellent. Someone named Henry has reviewed, excellent.
Cool.
Does it still need fixes?
**Emídio Neto** 07:34 Yeah, I could take a look at this one.
**Tammy Baylis** 07:36 Yeah.
Thank you.
Hmm.
Docs requests… Clarifying hookmutation and propagation order.
Yeah, it should be in the Read the Docs there.
Yeah, nice. I can… Take a look at that. Note for later.
Thanks, Lukas, for looking at this one, too.
And tests, yes, more tests. Already approved by Diego, thank you.
Oh, that's a very old issue. Oh my goodness.
Hi.
Sounds still relevant, for sure.
Give a review.
Oops, sorry.
Do… One more… GRPC AIO client hanging.
Wouldn't be good if this was an issue… linked to it… Okay.
Let's stop triage for now, and… We'll move to our regular topics.
Leighton, you have an important announcement.
**Leighton** 10:21 Yeah, hey everyone. Everyone can hear me properly?
**Tammy Baylis** 10:25 Yes.
**Leighton** 10:28 Yeah, so, the maintainers and I, Aaron and, Riccardo and I were discussing, that we were always, in need for more, assistance and help on the maintenance duties, and, I've reached out, and, I'm… excited to announce that, Lukas and Emidio would be joining us On the maintainer side for the Python sake.
They've been with the… with us for a while now, and they have some great contributions and, you know, leadership, in the SIG, so we're very happy to have you guys, on board, so… I should probably write their names down in the…
**Aaron Abbott (Google LLC)** 11:15 Yeah.
**Leighton** 11:16 Sorry.
**Aaron Abbott (Google LLC)** 11:17 Guys, thanks for all your contributions, and yeah, it'll be good having, This is the most Python maintainers we've ever had, so… Welcome, welcome, and thanks for all the help.
**Emídio Neto** 11:30 Yeah, thank you, folks. Really appreciate it.
**Lukas Hering** 11:34 Yeah, thanks as well.
**Leighton** 11:41 Yeah, that's awesome. Yeah, I didn't want to take up too much time on that.
We will, schedule a meeting with, everyone. And, yeah, this was just a, introduction, so thanks.
**Tammy Baylis** 11:57 Awesome, congrats, and so glad it's you, too. It's so great working with you both.
My topic's next, feel free to add other topics after this. I don't want to take up too much time, And it's about DB metrics… And how they mostly don't exist, but there's also a few, kind of, outdated ones.
So… this issue, 1158, another old issue, I… re-triaged it because I was looking for good first issues for somebody else, who wasn't here.
But then I realized, it's still relevant. The DBAPI kind of shared UTIL instrumentation.
And almost all of the, like, concrete database instrument or libraries, like for SQLAlchemy, PsychoPG, etc, don't emit any of the metrics that are defined in… The pretty up-to-date SEMConf.
So I'm like, yeah, this is still important.
Ahmed, I think they're a student. They've decided to take it on, which is awesome. They have a lot of great ideas. This is just some talk about how they think most of it should be in the concrete instrumenters, and I think that's fair. It's… the DB API instrumenter might not be appropriate, and it's kind of a weird place anyway.
Yes, Lucas.
**Lukas Hering** 13:38 Yeah, just for some context, I added a link to the doc to the PR that I opened a few months ago that actually adds those two metrics to the DB API?
Okay. Anything that is using the DB API, which I believe, like.
like, Postgres is doing should automatically inherit those metrics.
But the… yeah, so, but… I left out the connection pool ones.
Since, yeah, that doesn't belong in DBAPI, but I do think we should probably, maybe, add utilities, So we don't have to duplicate the full logic in each… database client, because I would imagine that it's almost identical in all cases, it's just… Hooking into the specific, connection pool logic.
**Tammy Baylis** 14:39 Yeah, thank you. Yeah, I was thinking the same thing.
Then I also… Thought it might be easier for… a new-ish contributor to do it concrete first, like, say, in one instrumenter, then add, like, utils later.
We can keep talking about that.
I think the question I wanted to bring up today… Oh, we need to do a SEM gen, that's just a small note, because one metric was renamed.
Right, my question was, if we start adding these new metrics.
which are on the new SEMconv, should they be gated by something like the opt-in, like we do for span attributes?
Or should it just always be emitted with the next release? If we don't emit all modern metrics at all times, do we need to do, like, backwards compatibility for the old SEMconf, and… I don't think we should do that… that backporting, but just wondering… and I… I don't quite remember the prior art.
if we want this opt-in to apply the metrics or not. Oh, I think… I think, Lukas, you were first.
**Lukas Hering** 16:13 Yeah, I guess quickly, my impression for this, for the opt-in and bars is, if… It's only needed if you previously had telemetry you're emitting, so I think, like, with metrics, we could just start emitting the new one and just… have our meter specify the schema URL it's using.
**Tammy Baylis** 16:35 Okay.
**Lukas Hering** 16:35 if others, interpret it the same way. I guess the only… potential edge case with that is that then you might have your tracer and your meter provider have different SENCOM versions.
So…
**Tammy Baylis** 16:51 Mmm.
Okay.
**Lukas Hering** 16:55 Well, I think for that reason, actually, the DB API requires you to Set the flag, otherwise it just emits nothing.
If you don't have… opt-in sets to DB or DB… DVD dupe.
Currently.
But we could maybe consider changing that.
**Tammy Baylis** 17:17 Yeah, that's kinda what I.
**Leighton** 17:18 Is that…
**Tammy Baylis** 17:19 Yeah.
Sorry, Leighton, go ahead.
**Leighton** 17:22 if, nothing is set for the 7 column for DB, no attributes are sent.
I misheard what you said, Lucas.
**Lukas Hering** 17:35 Yeah.
Since there is… since we didn't have, like, unstable… I can double check, but… Yeah, so, like, because we didn't previously support, like, unstable database attributes.
It just does nothing.
**Leighton** 18:04 Yeah, I think the opt-in was for migration purposes, so I'm all for just sending the new attributes.
**Tammy Baylis** 18:17 As in always, always admit the modern metrics, whether opt-in or not.
**Leighton** 18:28 Yeah, but I think Riccardo has her hand up.
**Riccardo Magliocchetti** 18:31 Yeah, like, I was… going to ask the very same Tammy question. Like, as far as I remember.
on HTTP, we have some… Different behavior regarding the… Like, if the opt-in is set or not.
And, like, reading this issue, I think we may have the very same issues, like.
At least the metric name is different, right?
Like, is this an attribute, or… is a metric name, like, DBK9… Metric name.
**Tammy Baylis** 19:10 Oh, sorry, it's for a metric… this is metric name, not span attributes.
**Lukas Hering** 19:21 These are all net new, though. We don't have any existing… metrics of these sort, I guess, just to clarify.
**Riccardo Magliocchetti** 19:31 Yeah, but the last…
**Leighton** 19:32 I guess, I guess the only underlying… Oh, sorry, go ahead.
**Riccardo Magliocchetti** 19:36 Not, like… I'm reading this comment.
And I understand it, but we already have something, or… Like, I don't… Yeah, we've…
**Lukas Hering** 19:49 We have the two metrics, but these are the latest… these are using the latest CENCOM. Actually, those two might actually be stable on that. I would need to check.
**Riccardo Magliocchetti** 20:03 Okay, so, like, what I meant is that… We should probably already introduce The opt-in, right?
**Emídio Neto** 20:15 I believe they are already under the optical.
in the B API.
Those two, right?
But there are some miss… some others that are missing.
**Tammy Baylis** 20:32 These are gated with an opt-in.
Otherwise, they're not emitted. Is that correct, Lucas?
**Lukas Hering** 20:41 Yeah, let me look and just triple check. Yeah, we probably should fix that, I don't think that that should be how it should be, because, yeah, those two metrics are stable.
From what I'm looking at in the… the spec…
**Leighton** 20:59 If they're both stable, didn't we… isn't that kind of already decided? That we're not going to be using… the opt-in?
semantic conventions?
**Lukas Hering** 21:11 Yeah, sorry, I'm actually wrong. The… one of them's stable, one of them is development.
But… That being said, the point is, the ones that are implemented, those… adhere to the very latest semantic conventions, 1.44. So if we were to add those other metrics, they would also be on 1.44.
So… I think that… I think the general consensus is we don't need an opt-in, since we didn't have any… Previous database metrics from older semantic convention versions.
That have breaking changes.
Is that right?
**Leighton** 21:57 Yeah, I think the, only point of contention is what you raised earlier, is when… If someone is opting into, like, old semantic conventions for other signals, like tracing, and they're getting… Quote-unquote stable semantic conventions for database.
Like, is that an issue or not?
**Lukas Hering** 22:21 Yeah, that's why I originally…
**Leighton** 22:22 My opinion is… Yeah, yeah. In my opinion, that's not a big deal. I kind of treat these signals as separate.
So I'm, I'm totally okay for, Not having this behavior depend on whatever the Sorry, sending the, stable or up-to-date, semantic conventions, regardless of what the, opt-in is said.
Open to other opinions, though.
Okay, yeah, if… everyone is in agreement. I'm assuming just silence, Is this the main issue, Tammy?
**Tammy Baylis** 23:19 Yes, this is the main issue. I was gonna, capture what we talked about, and respond to them, but if… If anyone else wanted to jump in, then… I'll add… oh, it's in the minutes, but I…
**Leighton** 23:32 Yeah, I think.
**Tammy Baylis** 23:33 God.
**Leighton** 23:33 I think your… your other… your other concern was, and I think we kind of glossed over this, was that, like, we wanted to decide whether or not we want to add this to a concrete instrumenter versus, like, a utility abstraction in the DV API. Yes.
I think, obviously, like, the utility is better, but I think you were saying that Because they're… they're probably a new contributor, or, like, a student?
it'll probably affect a bunch of, instrumentations, and… it might take some due diligence to kind of verify all of them? Is that kind of, like, something you were thinking, or…
**Tammy Baylis** 24:14 Yes, yeah, that's what I was thinking, because you have to… you have to test… we do have unit tests, etc. We don't have a lot of Docker tests, though, for the database instrumenters, so it… it would be a.
**Leighton** 24:26 Right.
**Tammy Baylis** 24:26 Due diligence to make sure.
changing the util doesn't, like, screw up all the concrete instrumenters. But I was thinking somewhere in the middle where they do their SQL alchemy changes first.
and then maybe use that as a starting point for a DBAPI util change later, instead of doing, like, the full fan out and editing all the other concrete instrumenters.
**Leighton** 24:58 Yeah.
**Tammy Baylis** 24:59 I'm fine either way, I'm… Yeah, I'm not married to any approach, so I… Wanted… just wanted to get people's thoughts.
**Leighton** 25:07 No, I think, I think you're… Yeah, I think your concern is valid, for sure.
And I always like to welcome contributions, so I don't want to, like, block them on… You know, just because they're maybe newer. But we just have to… Yeah, I think your idea is good. I'm okay with it.
**Tammy Baylis** 25:32 Yeah, thanks, Leighton. Lukas?
**Lukas Hering** 25:34 Yeah, sorry, one last comment, and then we can move on. If we do, like, generalize this, it probably doesn't belong in DBAPI, though, in my opinion, since those extra ad… those extra metrics are connection pool specific.
Which the, like, Python database API has no concept of.
**Tammy Baylis** 25:53 Yes.
**Lukas Hering** 25:54 Throw it out there.
**Tammy Baylis** 25:56 Yeah, thank you.
I got a, yeah, exactly what you said.
Okay, yeah, I really appreciate those thoughts. Thank you, everyone.
Yeah, Lucas, when you're finished, we can move on to your next topic. Much appreciate your notes.
**Lukas Hering** 26:27 Oh yeah, also, also off-topic, but, is it… can we enable the AI note-taking for this meeting?
Is that… I don't know if anyone knows the logistics on that, but it would be nice so people don't have to… Mostly, yeah, so we don't have to actually type anything.
**Aaron Abbott (Google LLC)** 26:52 Is that a… a thing, like a no-tel? I haven't…
**Lukas Hering** 26:55 Oh, no, it's just a Zoom… a Zoom feature.
**Aaron Abbott (Google LLC)** 26:59 Okay.
**Lukas Hering** 27:00 I mean, we've, like, it'll… I mean, I've used it at my employer, and it'll just kind of give you, like, a pretty good summary, actually, of the whole meeting.
**Aaron Abbott (Google LLC)** 27:13 Yeah.
**Lukas Hering** 27:14 Okay, yeah, we can maybe… I don't know who to reach out to for that question, but…
**Aaron Abbott (Google LLC)** 27:20 Yeah, yeah, I think we need to reach out to someone, but sounds good if we can do it.
**Lukas Hering** 27:30 Okay, yeah, the last point I add, or… If you click, whoever's sharing, click on that PR.
This is, actually, an issue that… that this is, like, one of the remaining gaps that we have in the Python implementation.
Which is adding a schema URL to resource detectors.
And, I left a comment, and it's mostly around… I'm actually not sure if we want to implement this, because… In my opinion, it'll make it an absolute pain to use resource detectors if we start adding these schema URLs, mostly because if… The… the spec states that if… There's an incompatibility in the, schema URLs, then all of the attributes should be dropped.
Which… I mean, the intention makes sense, right? You don't want to have incompatible, semantic conventions, but I guess the issue is that Like, between version 143 and 144, the chance of actually something taking effect. Like, even if you have different SEMP versions for Resource Detector, they could actually still be compatible, so I feel like the spec is kind of… Maybe not correct here. Like, I don't know what the correct way is to solve it, but I'm just kind of curious what others think.
Yeah, Aaron?
**Aaron Abbott (Google LLC)** 29:12 Yeah, no, I mean, could you share, if you happen to have a link to the spec thing? Because that also seems a bit surprising to me, like.
I… I know that there's this… the schema URLs are supposed to have a… Was that an issue for what you just said, by the way?
Other tab.
**Lukas Hering** 29:34 Sarah, what was that?
**Aaron Abbott (Google LLC)** 29:36 Yeah, that… I think, Tim, you're sharing… Okay, sorry, never mind. No, what I was gonna say was, I wonder if incompatibility is, like.
Wouldn't that only be if there's conflicting attributes when you merge, or is it… does it literally just mean If the version numbers are different, you just drop the data.
**Lukas Hering** 29:57 Yeah, so here, actually, if I can share quick, I have the spec, pulled up.
Sorry.
Okay, I guess I don't… I didn't give Zoom permission, Here's the link, if, whoever was sharing can reshare.
**Aaron Abbott (Google LLC)** 30:32 Yeah, you should be able to share, Lukas, like, I don't think…
**Lukas Hering** 30:34 Oh, no, I just… my… I… for some reason, it's asking me to, I have to give it permission, and I need to.
**Aaron Abbott (Google LLC)** 30:41 Oh, okay, okay, okay.
**Lukas Hering** 30:43 It's a me issue. Yeah, it says that… Yeah, the merge behavior is…
**Aaron Abbott (Google LLC)** 31:03 If old resource empty.
**Lukas Hering** 31:14 Yeah, if there's a merging error, which is the case when the schema URL of the old and updating resources are not empty and are different, the resulting resource is undefined.
And its contents are implementation-specific.
**Aaron Abbott (Google LLC)** 31:27 Yeah.
**Lukas Hering** 31:29 So, I guess if it doesn't say that we have to get rid of everything, but… I think that, actually, the… as we have it implemented, and I have to double check, I think we do just drop the… if the… the schema URLs mismatch.
We drop, the new ones being added.
**Aaron Abbott (Google LLC)** 31:56 Yeah, that's…
**Leighton** 31:57 Yeah, I think there's…
**Aaron Abbott (Google LLC)** 32:01 Go ahead, Leighton, sorry.
**Leighton** 32:06 Yeah. I think, yeah, it's one of those things where the spec is deliberately big.
I think it's good that it's not explicitly stating you have to drop the entire attribute. That would be kind of… Very defensive to me.
But going back to the original issue, sweet.
Yeah, like, specifically adding the schema URL to a resource detector, like, outside of the, you know, the schema URL conflict, right?
Could you go over the reasoning, like, the original description?
This is just, like, a… like, I'm hesitant in adding behavior that's not, like, explicitly defined by the spec, just for, like, You know, like, one-off feature requests like this.
Especially when it touches, like, the SDK like this.
**Lukas Hering** 33:09 Yeah, it's pretty clearly outlined if you go back to that page under the resource creation… create section.
Well, actually, well, it says it's optional, but, it specifies that the schema URL should be recorded in the emitted resource.
So, I think it's a suggested.
Thing to do.
**Aaron Abbott (Google LLC)** 33:42 Yeah.
**Leighton** 33:42 Oh, sorry, do we not do this today already, or… I forgot.
**Lukas Hering** 33:51 We handle the merging logic, but we don't… populate the schema URL in any of the SDK Internal resource detectors.
Or from any of the ones you didn't treat.
**Aaron Abbott (Google LLC)** 34:08 So I guess I'm just wondering, like, it feels a little weird to me that we're not implementing this feature just because… or rather, we're not implementing this part of the spec just because it's kind of, like.
clunky, so, I mean… I'm not saying we should implement it, but it feels like we're kind of just getting by on a technicality, because we're not setting it, and then… the… obviously, the result of that is that there's no schema URL in the resource that downstreams see, so… I don't know, it seems like an issue with the spec, like you said, Lukas. Is there already an issue, or something we can get some clarity on before… maybe just before we merge this?
Or before we, you know, heard feedback on the PR.
**Lukas Hering** 34:50 Yeah, that's kind of what I was gonna ask. If we think that it's something we should raise in the spec, then we should definitely raise it.
I guess the tricky… What's really tricky about it is, Basically, we need to determine programmatically if there exists some schema URL that is compatible with, like, all the resource detectors, basically.
Yeah. I mean, it's… yeah, it's just, like, we have to have some sort of, like, resolver. It would not necessarily be Trivial.
**Aaron Abbott (Google LLC)** 35:29 Yep.
No, I understand, and I think the data is technically there, because the… Like, all the differences between the schema versions are recorded somewhere in the spec in some file, but, like.
Yeah, I agree, I don't want to implement that in Python, so… It sounds like we're on the same page, though, Lukas. Maybe let's get… see if we can get some clarity in the spec before we… Proceed with this one.
**Lukas Hering** 36:01 Gotta take a la opening this year.
**Aaron Abbott (Google LLC)** 36:05 Okay, cool, and it would be interesting also to see what maybe, like, other languages do.
I think, java has, like, this auto-configure module, which has… I assume there's an SPI.
Which is probably the closest to what we have, where things can be versioned separately, and… See how it handles.
This case, since it's not defined in the spec.
**Tammy Baylis** 36:51 Thank you. No more topics, unless anyone has anything to say.
We could just end early, if we like.
**Aaron Abbott (Google LLC)** 37:09 Yeah, sounds good to me.
**Leighton** 37:12 Nice, nice.
**Aaron Abbott (Google LLC)** 37:16 Alright.
**Leighton** 37:16 Hey, awesome. Alright, thanks, everybody.
**Tammy Baylis** 37:18 Thank you, everyone. Thank you. Thanks for sharing, Tammy No problem.
**Leighton** 37:22 Nice.
