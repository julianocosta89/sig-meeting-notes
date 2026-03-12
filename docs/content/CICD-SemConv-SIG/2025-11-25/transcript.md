SIG: CI/CD SemConv SIG
Date: 2025-11-25
Duration: 26 minutes
Zoom Recording URL: https://zoom.us/rec/share/xFOtUgtta_-ywmCTKGXUgr8sKdJYAuRSwXPYj2076k9wFKK4loJNiwutEFH8F5QV.xkLulWtcQt8bQRJ3
============================================================

## Zoom Recording Transcript

**Adriel Perkins** 01:12 Good morning, or afternoon, or evening.
**Martin Costello** 01:16 Hey.
Afternoon.
Cool.
**Adriel Perkins** 01:20 How are you?
**Martin Costello** 01:21 I'm good, how are you?
**Adriel Perkins** 01:23 Doing good, thank you.
**Martin Costello** 01:27 The first one of these I've made for Phase 2.
**Adriel Perkins** 01:30 Cool. I… there's only been 3, I think, so… It's 1 out of 3 that's doing good.
Give everyone a few minutes to hop on and put anything in the, document, if they'd like to.
**Martin Costello** 02:12 It looks like there's been at least one other person with you, or the Phase 2 so far.
**Adriel Perkins** 02:20 Yeah, and I wasn't actually here myself last week either, so I think Kristoff took the lead on that one. Appreciate it, by the way.
Good timing to come in there.
**Christophe** 02:30 Hello.
**Adriel Perkins** 02:32 How are you?
**Christophe** 02:33 Why not you?
**Adriel Perkins** 02:35 Alright, thank you.
Give everyone just a couple more minutes to enter anything they have in the board, if they'd like.
Or, the dock, rather?
I don't see anything in… The general section yet. But we can go ahead and take a look at least at the board.
Go ahead and share my screen.
Go over here.
Rich, So I don't see anything having been moved into in progress yet, but, I did see from last week's… Last week's set of information, it looks like a couple things that don't show up on the board.
Namely, the long-running trace issue.
**Christophe** 06:22 Yeah, we discussed it on…
**Adriel Perkins** 06:23 Good.
**Christophe** 06:24 Carlos said he would take a look at it personally.
**Adriel Perkins** 06:28 Okay.
Cool. Yeah, I'm wondering, because we've been getting a lot of asks for this, There's no status on this one, how is it not showing up?
**Christophe** 06:45 Yes, sir, it is. It sets, water.
**Adriel Perkins** 06:48 Yeah. Thank you.
My eyes were deceiving me.
Exertpython's PR Digest.
Interesting.
I don't know who… That is… we'll see if we can get this one moved over, but… We've been getting a lot of… asks, for… This, especially, like, in the GitHub receiver, they want to be able to see live submission data.
I don't think backends really support this. I mean, there might be a couple, like, Dagger built their own visualization that's able to show that pretty well, but, I'm not sure how well the rest of the backends would be able to support having a non-closed span show up in their backend, which is essentially what a live submission data is.
So it'll be… it'll be good to move forward on… on this to see if that's something that's possible within the spec, and if it can be possible in the spec, backends can… Support that more effectively.
**Christophe** 07:57 I linked to an issue from Jager, where they wanted to investigate that.
**Adriel Perkins** 08:07 Cool.
Well, thank you for, taking that last week, and… Moving that forward, and we'll see what Carlos is able to take a look at there for that.
It looks like now we do have a couple things, Dotan, do you want to speak to your first one?
**Dotan Horovits** 08:34 Yeah, just wanted to, bring up, since we're at the end of, November, I was… just wondering what the impact would be, towards the holiday season, if we need to make any adjustments to the, to the meetings. I personally am going to be, challenged, December, both on travels for conferences, and then, On the… on the holidays, but anyway, this is just me, but wanted to hear around the table, what… any thoughts about, Needing to adjust, are we keeping the usual, or any other thoughts?
**Adriel Perkins** 09:09 I think we should probably keep the usual up until the, like, last week or two, when I think all open telemetry meetings kind of fall off. I have a… I don't remember… I feel like last year, that they all just kind of canceled at the last two weeks.
**Martin Costello** 09:24 I think I saw an issue somewhere in the community repo that proposed.
**Adriel Perkins** 09:28 Ditching the last two weeks of me ink.
That sounds familiar. I think that's what they did last year as well, let's see.
**Dotan Horovits** 09:48 If you can… if anyone can locate the issue, wants to add it to the doc, anyway, I captured the… this, but if you want to connect it to either… But anyway, I do think that, you know, we run independently, and based on the voluntary participation of the folks here, so if something works better for this team than for other teams, I think you should just see what works for the team here, so… Anyway, good to have this reference, but let's see what works.
**Martin Costello** 10:17 My phone issue, I'm just gonna pop it in the dock.
**Adriel Perkins** 10:20 Thank you.
**Dotan Horovits** 10:21 Cheers.
Great. Thanks.
**Adriel Perkins** 10:28 I'd be largely fine with that. They'll just, Everything's normal up until those last two weeks.
**Dotan Horovits** 10:34 Okay.
Sounds good. Just, again, I personally, since I will be away for a couple weeks.
There's Open Source Summit Japan, and AI Dev, and some other things, so… not even time zones that I can even aspire to join in between things, so, that's why I wanted to see all the other folks, but sounds good, glad to have the continuity.
The other issue, again, I just wanted to see if anyone has heard back from TeamCity. I tried to reach out to KO. I know that we talked about it in previous meetings, and it was an outstanding action item.
Since the folks from JetBrains did not, I guess… Fell off, that opportunity, and I did remember that we had a good other lead, other person, not regard, not related to JetBrains, that showed interest. I don't know, Adriel, if you remember that we met him in person back at Cube last year.
So I tried reaching out to him to see if he'd be willing to look into that as part of Phase 2.
But anyway, just wanted to first update on this, but also to see if anyone else heard anything.
**Adriel Perkins** 11:52 Yeah, so I did, have a conversation, back in October 21st, finally was able to get ahold of Kale.
**Dotan Horovits** 12:01 Oh, okay.
**Adriel Perkins** 12:02 they had not dug into it at all. So, I'm… I'm just gonna say, you know, it… you know, it's really, like, it was their ask to support it, and they just haven't had that opportunity due to some circumstances that are going on their side that I'm not gonna, like, repeat on, like, a video camera. And so I would say that we just… Leave it be.
**Dotan Horovits** 12:25 sugar.
**Adriel Perkins** 12:26 And we prioritize… because I don't think we necessarily had it prioritized anyway for Phase 2, so I'd say that we focus on the things that we can control in Phase 2, and you know, if they get to it, they get to it. If they don't, they don't, but I don't have an issue tracking it on our board right now, because it's just, for all intents and purposes, close.
That makes sense.
**Dotan Horovits** 12:48 Yeah, no, I didn't plan on tracking it. There's a separate topic that we discussed last week, also… with Carlos about tracking, but let's put this aside, the tracking, and this is another aspect, more technical. I did think that we… at least it appeared on my action items that we, from previous meetings, that we wanted to follow, follow up, and I thought, for some reason, that I took on myself to follow up with Kale, sorry, I guess we had, Some duplicity there, so.
**Adriel Perkins** 13:15 Oh, it's.
**Dotan Horovits** 13:16 Sounds good that you managed to catch up with him back in October, and fair enough if it's not their priorities. So, good thing we're sitting with singing or not. Talking about the tracking, so there was a question that came up.
last week, Christoph was also part of the discussion. That is, I guess, broader question about, things. It also relates to the, to the, environment variable propagation, the implementation of these things, and… as a SIG, on the one hand, we don't control this, and on the other hand, sort of we, we want, at least for the first one, sort of the… let's say the initial mass, to escort it in some way, and we've tried to, get his insights, and maybe insights from other SIGs with similar concerns, how they track it when it's, again, not their ownership, but still they want to somehow For that, and, it was an interesting discussion, but, long story short, he did say that he wants to, to actually consult with the, with the TC and, and provide feedback, so, Also, not specifically for that, but I guess the broader thing, it'd be interesting to see what comes out of this.
**Adriel Perkins** 14:28 Oh, when he said the SIG doesn't… I haven't watched the last week, so that's on me, but, what do we mean by the SIG doesn't control it?
Exactly.
What, do they not control?
**Dotan Horovits** 14:40 it's we. No, the SIG is us, and since we don't, as you said now, we don't own these, integration pro- project, or there's, like, the, I don't know, Python for… I'm looking at the… by the way, this is… I'm highlighting on the, last week's note, if you want to follow it also on the doc.
So all sorts of, these… I guess, implementations that are part of other teams' responsibilities, but we champion them, in a way.
**Adriel Perkins** 15:12 So, so let me rephrase the ask, because I've read that.
**Dotan Horovits** 15:14 Okay.
**Adriel Perkins** 15:15 And what I'm saying is, is what do we not own with regards to it? Are we saying that we're not doing any work to open a pull request to support that?
propagation in each of those SDKs? And is that what we don't own? Like, we don't own a PR because we're not opening a PR? Or are we saying that, like.
In that situation, it's on… like, we would want to talk to each of those language SDK owners.
and ask them to open their own PR to support this spec, right? Because when we originally, like, outlined this, I… the thought was that we would do a combination. We're like… because I've already got a pull request open for Python.
And we can open a new one for Go, but actually we'd be opening pull requests to support that, environment carrier, context propagation, right? Not necessarily Asking for them to do it for us.
**Christophe** 16:12 Yeah, we can do that.
But I think what is meant here is that we would not create an issue on our board in our… in the semantic conventions project to track it.
We would directly open an issue or a PR in the respective project.
**Adriel Perkins** 16:29 Yeah, but we can still track that on our board, right? Like, we can put an issue on their project, and just have it tied back to our board.
**Christophe** 16:36 If it's under the OpenTelemetry organization, yeah. Yeah. Then we can.
**Adriel Perkins** 16:41 Yeah, absolutely.
**Christophe** 16:42 But for external projects, like Jenkins.
It's, it's not that easy.
**Adriel Perkins** 16:48 Right.
**Christophe** 16:50 And here, what is meant is we can track it as a GitHub issue.
We could have an issue for stabilizing Semantic conventions, or for stabilizing certain semantic conventions of ours.
Then, it can be on our board.
And on that issue, we could link to See, external projects where it's being used.
**Adriel Perkins** 17:18 Yeah, that makes sense. That's what we originally, The linking out, I think, is what we originally did in some circumstances.
Like, with the OTEL specification change for ENV carrier, right? Like, that's not a semantic conventions issue, that's a specification issue, but this is within org.
We had one that would track, like, us doing work on the board, and then, like, it linked… it was referenced into the actual issue changes within that, repository. So, I think the linking and the cross-tracking is pretty… straightforward within the same org, and that does make sense if we want to track an external projects work.
so that it's related in some way, we could certainly do it that way.
The problem that came for the Team City one is that, like.
you know, it was completely on their onus, not on us at all. So, like, we had an open issue that was just, like, on our board for forever, and, like, we couldn't get any traction on what the updates were or anything like that. So we just ended up closing it, and that's just because it's a completely external, like, vendor… Vendor thing that they're doing, so… we have the history of it, but just in those situations, you know, maybe not tracking work on our board. At least not… at least as part of, like.
Phase 2, we could also have that option. This is all I'm trying to say.
**Dotan Horovits** 18:51 I think it's not a black and white question, or a binary one. I think there's a spectrum of our engagement from the extreme side of, as you said, TeamCity or whatnot, they fully own it, and we have little to none to do with that, or to impact that, to the other extreme of we are the ones who are opening the PR, maybe even generating and contributing the implementation to it, and some in between, that we are the initiator of the issue, but someone else needs to implement. I think that it's a spectrum, and we will need to be flexible enough to think how we can, track it, and I agree with you that when it's not our ownership, then this… it's a bit annoying when you have this… stuck in your board, and you can't really move it forward and progress it. So, I'm not saying that what we've done in the past in Phase 1 is… needs necessarily to be the answer for Phase 2. I thought that it's a… For me, at least, as one of the leads, it didn't feel like it's fully resolved, to be honest, and I thought the opportunity of having Carlos on the call was a great one to ask for additional perspectives from the TC, and maybe other SIGs that have encountered similar types of You know, interaction, or dependency, or whatever you'd like to call it.
And yeah, I'd be happy to get more feedback and more perspectives on that, because there is value in visibility and traceability of things that are… as I said, at least when it's, like, the initial aspects, once we get a certain mass that things get their own motion and we don't need to track it, that would be a blissful moment that I'm looking for, but now it feels like we still need to nurture these things and score them, and then the question is how we can make sure that it doesn't fall off radar in any way. I hope I explained it better now, and I tried adding some additional notes to last week's, because you have fair questions that might not have been clear from the bullet there.
**Adriel Perkins** 20:59 Yeah, I think we have the optionality as well. So I'm taking an action item for this week to go ahead and add I don't want to call it an epic, but I mean, that's essentially what it is, right? Like, it's a… task with various different subtasks within it, that can track the, at least within our specific OpenTelemetry organization, that can help create a visualized tracker for the, various different environment carrier, aspects.
of work. So we can… we can do that, and we can open up some of those pull requests. I was gonna do Python and Go. You know, honestly, with AI today, it's kind of easy to do any language. It's always been kind of easier to do any language.
You know, if you can read one, you can read many. I've always kind of had that view, but it's even easier today, so, I'm gonna definitely at least do the Python go, but if we want to solicit, like, any specific language SDK maintainers to do it for us, because of no familiarity at all, and we don't feel comfortable doing that, then we can do that too, and still, like, at least have some type of tracking in place via opening issues and whatnot. So, we can do that. And I'll, I'll just take that action item to do, before next week's call.
**Dotan Horovits** 22:19 Thanks. And again, the idea is not to, add more, more, overhead or, or, like, paperwork. It's just for having the, the minimal one that, that will have.
The type of visibility we need, and as we said, this… we can apply judgment per case. If there's something that we see that we… it doesn't move, and we have no influence whatsoever, then tracking becomes just a procedural thing that doesn't contribute to anything, we can drop it off.
If there's something that we do see that we have collaboration and someone to work with, like we had with GitLab, and… or at least the receiver, not GitLab itself, but, like, the GitLab receiver and everything, then makes more sense. So, just per case basis, but just pointing out that there's, like, a range, a spectrum.
Hopefully to have more cases that will need resolution, because it'll be a positive problem to have.
**Adriel Perkins** 23:09 Sure.
Cool. Anything else?
Food today?
**Christophe** 23:23 I just wanted to say, on the 9th of December, I will be traveling, so that one I won't be able to attend.
**Adriel Perkins** 23:31 Cool, thank you for the heads up.
Enjoy your travels.
**Christophe** 23:37 Thanks. I'll be returning from Rome that day.
**Adriel Perkins** 23:40 Nice.
**Dotan Horovits** 23:43 I wanted to ask you if you're coming by any chance to Open Source Summit in Japan. No, you're in Europe.
**Christophe** 23:49 I've been in Japan before, but not this time.
**Adriel Perkins** 23:58 Alright, well, if we don't have anything else for today, we can call it a little bit early. It's good to see y'all.
**Dotan Horovits** 24:03 Enjoy the rest of your week.
You too. Bye-bye. Thanks, everyone.
