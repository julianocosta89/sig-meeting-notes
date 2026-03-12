SIG: CI/CD SemConv SIG
Date: 2025-11-18
Duration: 23 minutes
Zoom Recording URL: https://zoom.us/rec/share/b2D9p8ibawfr8yxGPS0Zwd49Tu6dTW78v8cuf_vcHcUkrNjhnGvmsdv05X6Pqq0O.2HHhnW-KSvPWeRUu
============================================================

## Zoom Recording Transcript

**Christophe Kamphaus** 00:42 Hello?
**Dotan Horovits** 00:45 Hey, Christoph, how's it going?
**Christophe Kamphaus** 00:48 Fine, aren't you?
**Dotan Horovits** 00:50 I'm fine. Great to, great to, see you. It's been, it's been a while.
**Christophe Kamphaus** 00:55 Yeah, it's been a while.
**Dotan Horovits** 00:56 Yeah, how are things with you?
**Christophe Kamphaus** 00:59 Fine.
**Dotan Horovits** 00:59 You started a new job, right?
**Christophe Kamphaus** 01:01 Yeah, some time ago, that's why I couldn't join the last few months.
**Dotan Horovits** 01:06 Yeah, yeah, no, I know, I'm just, well, first of all, happy for you for the new, for the new gig, and, yeah, glad that, You can join, and you said that you'll be able to carry on here, so it's even better, so, glad to see that.
**Christophe Kamphaus** 01:25 Do you know if anyone else will join?
**Dotan Horovits** 01:27 I see someone is joining now, and let me also, One second, Want to, ping the fold? Oh, okay, there's the auto-reminder, so, people should have seen that.
I'll have to, it'd be shorter, because we're hosting a meetup today, so… Need to get, Set all the things up, and .
**Christophe Kamphaus** 02:02 Yeah.
**Dotan Horovits** 02:03 Get ready before people, come. So actually, if you want to, Christoph, if you want to lead this one.
more than happy and appreciative if you, if you want to take that. I know that you… you haven't been here for some time, but, you're still,
**Christophe Kamphaus** 02:16 Yeah, I think it's, we don't have much triaging to do, since there are not many new issues, or if any at all.
**Dotan Horovits** 02:29 Integrated some of the, you know, the backlog to the new board, so… Yeah, I saw some new board.
Hey, Carlos, I see you.
**Carlos Alberto Cortez** 02:43 Yeah, hey, hello.
**Dotan Horovits** 02:45 Hey, we can hear, we can hear you now.
**Carlos Alberto Cortez** 02:50 Sweet.
**Dotan Horovits** 02:52 Great.
Well, I think it's 5 minutes past the hour, so I think we can start, and Yeah, thanks everyone for, for joining, and We're finally at, Phase 2.
Beginning of Phase 2.
For, for the, SIG, a very important milestone, and, We have a new clean new board, we have the updated, goals and scope for the, for the Phase 2, everything, of course, is on GitHub, if you're, for those who are interested, also for the recording, I guess, for those who hear the recording. And yeah. So, the regular thing is that we just, do a quick round, around the table, just if we have new faces. Carlos, I'm not sure if we, if we had you… the honor of having you on the… on the call, and I can't see the face, so I can't say if I recognize or not, but, do you want to take the opportunity and present yourself?
**Carlos Alberto Cortez** 04:07 Yeah, actually, I am the TC sponsor. I was mostly… Keeping an eye on what the group has been doing, just reviewing stuff.
But yeah, now, yeah, I took the time to actually come and, you know, participate in the meeting. Yeah, previous time is a good, usually good follow-up with the notes offline.
Yeah, but today I have some time to, you know, be checking what's happening.
Actually, I was here last week, as well.
**Dotan Horovits** 04:36 Okay, I missed last week, I was traveling, I was, Actually, it's KubeCon, in Atlanta, so it was a bit difficult for me to join, but, yeah, so it's actually, it's not the opening of the Phase 2, it's just me, missing the, the grand opening. So, you said that you're… you're the sponsor from which, which side?
**Carlos Alberto Cortez** 04:57 the DC.
**Dotan Horovits** 04:58 Okay, the TC, okay.
**Carlos Alberto Cortez** 04:59 dick.
Yeah, go ahead. Yeah, the technical committee. No, I'm just wondering, because I think we also had the… we have a new.
**Dotan Horovits** 05:06 liaise from the GC,
**Carlos Alberto Cortez** 05:09 Oh, yeah.
Correct, yeah. Marilla, right? Gutierrez?
That's correct.
**Dotan Horovits** 05:14 Yeah, yeah, so, I hope that we have an opportunity also to, to get to, know her and introduce her to the group, Yeah, so do you… maybe, actually, it's a good opportunity, do you want to, again, also for the recording, sort of the scope.
of your role And the TC, with regards to the SIG, I think it's a good opportunity as we start a new phase.
**Carlos Alberto Cortez** 05:39 Yeah, so basically the idea is that, I help, the Sikh to make progress, especially helping where You know, in the times when the progress cannot be made, because prototypes are not being reviewed, or something like that. And Also, in the specification side, when you are doing or adding new stuff to the specification.
or do the semantic conventions, I should be able to, review And likewise, help you, you know, with any blocker, you know?
The most common, as I said before, is when people are not reviewing.
The arts and off, or when there's no agreement.
And somebody needs to come and, you know, make a hard call, or even bring some topic back to the TC so we can decide, you know, on behalf of the community.
So far, things have been going relatively smooth, I think, so it has been mostly me foreseeing, that things go well, you know?
**Dotan Horovits** 06:40 Yep.
Thankfully enough. Again, I guess the most, the biggest challenge we've encountered, and We've shared that, but, just to reiterate is, really getting more folks involved. By the way, Christopher has been a tremendous contributor to the, to the group. He's also a reviewer and everything, so… but I'm saying, definitely this is something that we've faced, and if you have… Any advice, any tricks, any strings to pull to help us increase the exposure, the visibility, and garner attention? Anything in that regard will definitely be helpful. Not new, but just using the opportunity to reiterate.
**Carlos Alberto Cortez** 07:27 Makes sense.
**Dotan Horovits** 07:29 Yep.
Anyway, sorry, Christoph, I saw that you went off mute, anything that you want to add? Yeah.
**Christophe Kamphaus** 07:34 I joined the General SumConf meeting yesterday, and I brought up the unified workflow semantics there.
**Dotan Horovits** 07:43 Oh.
**Christophe Kamphaus** 07:44 feedback I received was that probably We would need to create a SIG for that, separate from CICD, because it's actually a lot more involved. We would gather… need to gather more people also from other domains.
probably it would make sense to create a SIG for it.
**Dotan Horovits** 08:03 Yeah, actually, it's great that we have Carlos here on the call for that. Do you want to give a bit more context, just for Carlos to understand, and maybe then we can ask, revert back to Carlos on how we can support.
**Christophe Kamphaus** 08:14 Yeah, I can share my screen for it.
**Dotan Horovits** 08:17 Yeah, great.
**Christophe Kamphaus** 08:19 So we had an issue open for it for some time.
And we had a PR created for it, which was based on the CI-CD semantic conventions.
But, yeah.
What, the feedback we received yesterday was that probably Because OpenTelemetry is going towards stabilization.
That this would rather not be a priority for now.
And we would have to create a SIG, find more people for workflows.
To also, invite some from business process modeling, And, Similar.
Task conscience Also, kayak, for example.
**Dotan Horovits** 09:15 Yeah, sounds good. Carlos, do you have any questions to ask? Just first of all, to make sure that you have the full scope and context, and then I'd probably be asking you how you think will be the best way forward, and how you can support?
**Carlos Alberto Cortez** 09:29 No, I didn't see the answer from yesterday. Could you scroll down to the actual PR, so I can take a quick look?
**Dotan Horovits** 09:39 Maybe, maybe…
**Christophe Kamphaus** 09:39 Hey, Crystal Village.
**Dotan Horovits** 09:40 I want to also throw the link also on the, on the Slack channel, and we also documented.
**Christophe Kamphaus** 09:44 Yeah, yeah.
**Dotan Horovits** 09:45 It was…
**Christophe Kamphaus** 09:45 was, brought up here in the semantic conventions meeting notes, but I can also add it to today's ones.
**Dotan Horovits** 09:55 Yeah, yeah, let's, let's do that again, just to trace, because this is an important milestone that you presented it, and the feedback that they got, so I think it's definitely worthwhile.
Putting it on the notes.
**Carlos Alberto Cortez** 10:10 Yeah, I will be taking a look at that. I hadn't seen what was answered yesterday, or posted.
in this, PR.
Then I can tell you what I think, and we can discuss whether there's something we can do.
**Dotan Horovits** 10:26 Sounds good.
**Christophe Kamphaus** 10:28 Neo.
Also, some said, maybe the big points where Carlos could help us in, Or sick would be.
Yeah, in Phase 1, we implement the… we merged the… specs, PRs for, context propagation.
Of environment variable, carriers.
And now in Phase 2, we will have to implement some in the different SDKs.
Probably, there will be somewhere coming there.
And we have one open issue that might also, need some spec. It's the one for producing long-running traces, so we might need to, Have some changes in the specs.
**Carlos Alberto Cortez** 11:22 Yeah, that's a complex one, and I was thinking about taking that myself.
It's, it's, it's a, it's a issue that has been long-standing in the spec.
And we have been postponing.
They work on that, because it could be… we don't know how complex this can become, how many parts can be affected.
**Christophe Kamphaus** 11:42 And so on.
**Carlos Alberto Cortez** 11:44 Yeah, so, I… I could personally say that I would like to have this We have these ones solved.
as an optional item, as part of the Phase 2, you know? It's, like, something great to have.
But, and the work should be started as part of this Phase 2, of course.
But there's a chance that it will not be wrapped up, you know? But yeah, it needs to start. Actually, I was talking to both you and Adriel last week, and I do remember that there were some actual users who had been rolling into this case, you know, like, practical users, you know, not, like, in theory, but in practice.
**Christophe Kamphaus** 12:24 Yo.
**Carlos Alberto Cortez** 12:24 So I think this… yeah, this would… would be nice. I think I will… I will take a second look.
And think… but I think… I think it would be good for me to take this one on. Yeah.
**Christophe Kamphaus** 12:37 Should I assign it to you?
**Carlos Alberto Cortez** 12:40 Yeah, for now, at least.
So I can make a decision or not, yeah. So that will help me, you know.
Keep my mind on this one for now.
**Christophe Kamphaus** 12:58 Yeah, thank you very much.
Yeah, we discussed it a bit, last week as well.
Right?
I don't have any other topics for now.
**Dotan Horovits** 13:21 Okay, sounds good.
**Carlos Alberto Cortez** 13:22 I have a… I have a question, by the way. Last week, likewise, we were discussing… Adriel, at least, mentioned that there are some PRs for the prototypes for environment propagation.
That haven't been merged, and what can we do?
To make, you know, progress on that front.
So I was checking some of the PRs.
And, I found a very old Titan one, which was closed.
I don't… and I saw the one in Python. Like, in Python, currently, there's, environment propagator, and there's a prototype that Adriel wrote for environment carrier, which is the other option. Like, you either choose propagator or a carrier, or both.
So, that's okay, but for Go, yeah, I don't know what's the current status, I will double check, because I would like to talk about that in the spec call in… 40 minutes, I think. 44 minutes.
But, yeah, if you know about any other, that comes from the top of your mind, just let me know. But yeah, so far, I have only seen the Python one.
For environment carrier, and the one from Go, which is Environment Proprietor.
The one from… that was written in… for Swift, I can't… I couldn't find anymore. I don't know whether it was moved around, it went to contrip, or it was removed, or what.
**Christophe Kamphaus** 14:47 Yeah, I don't have a list of such PRs.
We would have to ask Cartriel.
**Dotan Horovits** 14:53 Yep.
**Carlos Alberto Cortez** 14:54 Yep.
**Dotan Horovits** 14:55 By the way.
I put the, Carlos, you have the, the meeting minutes, doc on the, chat here.
in the Zoom, so I took, you know, brief notes from what you're saying, but if you have any… anything to add, and if I, like, to properly capture everything that you found, feel free to augment the bullets that I wrote, so… If you have some conclusions from your check, links, or anything else, just… Making sure that we adequately capture, because it sounds like you've been looking into that and put some research on.
**Carlos Alberto Cortez** 15:31 Yeah, yeah, yeah, yeah, totally.
**Dotan Horovits** 15:32 Also for you, of course, Carlos, if you have any… sorry, Christophe, if you have anything to add. Just doing a short notation here, but feel free to add, because it's really, really short.
Yeah, thanks, the link is useful. Yeah, Carlos, thank you so much for joining, both last time and this time, and for following up on these, because we can definitely use on the ones that are pending merge and things like that. And we can ask, async from Adriel to, At least, just to make sure that you have everything on your radar, and you can look into that beyond the Python and Go ones.
**Carlos Alberto Cortez** 16:13 Yeah, perfect. Let's do that.
**Dotan Horovits** 16:17 Sounds good.
I would suggest just going briefly over the updated, board. Christophe, do you want to, open it on your own?
**Christophe Kamphaus** 16:27 I have it open here.
**Dotan Horovits** 16:29 Yeah, we can see it now.
**Christophe Kamphaus** 16:32 So, there was no work done on these.
And I don't think there's any new ones here.
Okay. This is a unified semantic convection.
That was discussed.
**Dotan Horovits** 16:47 Exactly.
**Christophe Kamphaus** 16:51 I think that's it.
**Dotan Horovits** 16:53 By the way, the, the ones that are… the PRs that are, pending the merge, are these, mapped here, or is that from the old board?
**Christophe Kamphaus** 17:02 No, it… we never tracked Sam on the board.
The only thing, if I remember right, in Phase 1 that we tracked on the board was for the spec changes.
**Dotan Horovits** 17:13 Hmm.
**Christophe Kamphaus** 17:14 and some, the GitHub and GitLab.
**Dotan Horovits** 17:17 Yeah, GitHub, GitLab receivers, yes.
**Christophe Kamphaus** 17:19 Receivers, yes. We link to those.
**Dotan Horovits** 17:23 just wondering, is that something that we would… just going around the table, is that something that we would like to otherwise capture now in Phase 2? Like, I know that we've done certain things, certain way, Phase 1, but just rethinking if this is something that we want to capture, or maybe if not on the board, in other… like, what's the best way, or… Any thoughts?
**Christophe Kamphaus** 17:47 It's a question I ask myself as well.
Especially for implementations of these semantic conventions, because we need more than one or two prototypes now for stabilizing them.
**Dotan Horovits** 17:59 Yep.
**Christophe Kamphaus** 18:01 And since those are usually not, OpenTelemetry projects, or would we track some?
**Dotan Horovits** 18:07 Yeah, also, like… like, we don't own them, usually, like, you put on the board things that we can… so, it's like, actually, Carlos, do you have any feedback on this, like, from other SIGs, from other working groups? What would be the best way to capture things that… We don't own on the one hand, but on the other hand, they're very important to our work, in some cases, even preconditions for, you know, maturization, stabilization, and so on.
**Carlos Alberto Cortez** 18:35 What's the problem with putting them in total?
**Dotan Horovits** 18:40 So, a separate doc dedicated for these? That's, like… and I'm just asking, what's the best practice that you see around you for similar things in other working groups or SIGs?
**Carlos Alberto Cortez** 18:48 Yeah, I don't think there's any standard way to do this for these specific tasks. I can go and double-check what's happening in others.
But I think that, yeah, there's no standard way to do this.
**Dotan Horovits** 19:04 I'm just thinking, any SEMCON will face the same thing. You need the implementations.
implemented across the board. You don't own it as the one defining the spec, but… but you want to see the downstream, this is getting… so I'm just wondering, and we… we are sort of the smaller ones, I'm sure that others had a far wider, distribution.
So I'm just wondering what was the way that they handled it, and if we can learn from that.
**Carlos Alberto Cortez** 19:32 So, if you're talking specifically about implementations, actual implementations of what you are writing, Usually, we keep track of that in issues.
And then just update the issue, yeah.
**Dotan Horovits** 19:46 So, but it's the issue… the issue is opened on the… on the, like, the SIG, although it's implemented by the downstream, I don't know.
**Carlos Alberto Cortez** 19:56 Java, SIG, or some other group… working group.
**Dotan Horovits** 19:59 Right.
**Carlos Alberto Cortez** 20:01 Yeah, the spec, usually, the spec, the specification, or semantic conventions, depending on which one you go for.
And then you…
**Dotan Horovits** 20:08 Okay, so in our case, sort of, you would have expected to see, like, an issue documenting the fact that, about the Python, thing, for example.
**Carlos Alberto Cortez** 20:18 Yeah, correct. Yeah, correct.
**Dotan Horovits** 20:19 Okay, okay.
That's, that's a good feeling.
**Carlos Alberto Cortez** 20:22 And to be clear.
Yeah, to be clear, I think that's an interesting kind of an egg and chicken problem, because the beauty of the SIGs, is mostly to grade Something in the spec or semantic conventions.
That then, once it becomes stable, SIGs are… Motivated to implement.
But that's, in theory, not our duty anymore. Once we have worked with them, so they have prototypes.
and we have enough prototypes, which is at least a couple of them, in different languages. That's on us. That's on us, and once that's done, that's on them.
In our case, if we want to to make sure that this is actually implemented across the board, then that's something that most SIGs don't do. If you feel that's important for our specific use case.
then, of course, we can, actually, that's a good point that I can bring back to the TC, because as I said before, most 6, once you have finished your stuff and the semantic conventions or specification site, that's it, you know? Then that's on the six.
**Dotan Horovits** 21:25 So, I would actually appreciate if you can bring it up, because, yeah, it's sort of an interesting beast here. I'm just wondering, what would be the thoughts around the table on the TC, and any guidance on just providing the right level of Transparency, of visibility, observability, whatever you'd like to call it, but keeping in mind that, like.
we, as the SIG, we sort of… we don't own it, but we… it's important that… that we have the visibility and all… so, just, what's the best way that we'll… be able to track that, but still keep it on the… with the owners while we have the visibility. So, any feedback that the forum can provide?
**Christophe Kamphaus** 22:08 When you mentioned tracking it on a GitHub issue, I was thinking, yeah, for sure, we would create one for stabilizing a certain semantic.
Convention of ours, and then we would list the prerequisites that we would like or need In order to be able to stabilize it. So that would be a good way to track it, I guess.
**Carlos Alberto Cortez** 22:32 Yeah, but if you want to track it after, you have made some… you have made something stable, then that's something different, yeah. Something we don't usually do.
And we should, I mean, technically we do, because usually in the specification, you add something to the compliance matrix.
So, basically, seeks no, and what's the status?
But it's not quite, like, a total list, you know, the way it should be.
**Christophe Kamphaus** 23:00 Yep.
**Carlos Alberto Cortez** 23:02 Okay, but yeah, good point. Let's, I will… let me bring that to the TC, so I can discuss that with them, and probably provide some feedback on whether there's something we can do to make this, simpler.
More obvious and more visible.
**Dotan Horovits** 23:18 Yeah, sounds good. Thanks for, for checking it out and following with that, Carlos. Yeah, I think so, all in all, this is, These are the main things that we have outstanding.
Anyone has anything else?
**Christophe Kamphaus** 23:38 Not from my side.
**Dotan Horovits** 23:42 Okay, sounds good. So, I'll give you back your time, and, yeah, thanks everyone for, for joining us.
**Carlos Alberto Cortez** 23:50 Perfect, see you around.
**Christophe Kamphaus** 23:51 You too. Have a good day. See you.
**Dotan Horovits** 23:53 Bye-bye.
