SIG: CI/CD SemConv SIG
Date: 2025-10-23
Duration: 13 minutes
Zoom Recording URL: https://zoom.us/rec/share/vi_Mmr_pAyfbtYgnxx-vFartzip3ijAK3fr-gKOF_8DIb3yYTjXcNF0j9QqCx8J0.o8dopF9xs--D7mx1
============================================================

## Zoom Recording Transcript

**Dotan Horovits** 03:54 Hello, everyone.
**Martin Costello** 03:57 8.
**Zach** 04:01 If…
**Dotan Horovits** 04:06 Okay, I'm just pinging to see if Adrude is joining us.
Okay, in the meantime, let me, paste here the… sorry, the… Link to the… Meeting doc…
Hey, Zach, thank you so much for the message, that's very… Very nice of you.
Turn on the camera so I can see if we, got the chance to, meet anywhere. Recognize the face behind the name.
**Zach** 05:13 Sure.
**Dotan Horovits** 05:16 Oh, now I see the face.
Have you had the chance to, to meet?
**Zach** 05:21 No, not yet. I think I found you on LinkedIn through all the different conferences that you do, so I just followed you out of interest.
**Dotan Horovits** 05:28 Okay, thanks, that's great. That's how you found out about the, the CICD SIG as well, or did you know it from other contexts?
**Zach** 05:37 I think I knew from another context I'm subscribed to the OpenTelemetry and Kubernetes calendars.
**Dotan Horovits** 05:42 Okay, yeah.
It could be overwhelming, so it's nice that you spot… manage to spot a single thing inside this mess, but
Yes, sir. Very nice.
Yeah, yeah, very good.
Well, I suggest we start, and if other folks join us, then it'd be good. Actually, you know, Zach, if you want to take the opportunity and introduce yourself, and maybe your background, and why you find this SIG interesting, it's always good to see new faces in the group.
**Zach** 06:15 I've been doing SRE, DevOps, DevSecOps for 5 years, and I have 10 plus years of IT experience. And, like I mentioned, I'm subscribed to a couple of different open source calendars, so I saw this one, I'm just chillin' here at the airport before a cruise, and figured I'd join.
**Dotan Horovits** 06:31 That's one way of passing the time at the airport before boarding time.
Yes, sir. I've done a few of those, not just passing the time, even leading, it's very interesting to be a lead of a meeting when you're from the airport and hoping that the, network doesn't jitter or anything, so, yeah. May I ask where you work at, if that's okay, obviously, only if it's something you're comfortable answering.
Oh, you go to the sheet.
**Zach** 06:56 I actually work for a few different people, so it's…
Can you guys hear me now?
**Dotan Horovits** 07:02 Yeah, yeah, we can hear.
**Zach** 07:06 Yeah, so I work for a few different people, so it's, kind of long to list.
**Dotan Horovits** 07:11 No worries.
Even good, you get to influence, many organizations. Cool, so I think, great to have you with us, and I hope it will be, just the beginning of more,
And just out of curiosity, beyond, obviously, you said that you've been… you had the extensive experience with SRE at a specific angle that you find interesting, specific,
feedback that you have for the SIG. Actually, we're in a very interesting junction point where we're about to start a new phase, so even better of a timing to interject with feedback. So, if you have anything that is top of mind for you with regards to the SIG, happy to hear that as well.
**Zach** 07:56 Thank you, sir. Nothing at the moment, but if anything comes to mind, I'll let you know.
**Dotan Horovits** 08:01 Sounds good, sounds good. There is, by the way, I don't know where you're based, because when you're not at the airport or traveling, but there is a questionnaire open, Stropol, that is about the, I guess, timing for Phase 2 meeting, so this is the current timing, but
If this is something that you would like to also, state your opinion and your preference, assuming that you plan on joining us further, then feel free to, check out the,
the Slack group, and there's the link there for the questionnaire. So, again, it's mostly, obviously, for people who come on a regular basis, but I hope to see you on a regular basis, so.
**Zach** 08:38 Yes, sir, sir.
**Dotan Horovits** 08:39 Amazing. I appreciate it. Great, good to have you, good to have you. So, I guess it could be a rather short meeting, because as I said, we're sort of between the phases, so we're wrapping up Phase 1 and starting phase two.
So a lot of that goes about, actually, more cleanup of the, the board, about some requirements that we have from the,
From the governing committee to, on how to.
structure the Phase 2, what needs to be included, lots of also bureaucracy, so I won't, bother all of you with this, but essentially, there's the PR there on the, open…
You're welcome to have a look and see. I think there's actually quite just a couple of loose ends there, so I think we're very, very close to getting that merged and be able to kick it off. The idea is to kick it off beginning of November, so if nothing changes, I hope that we can meet this timeline.
Adriel is the owner of that PR, so that's why I was hoping that he'll be here, just to know if there's anything… any blocker that I can help with, or we can help with.
And yeah, we'll have probably a clean board, we'll migrate all the items, the tasks that have not been completed or in the backlog to the new board, and then we can start fresh.
There. So, just to share the status on that one, so let's less of a triage elements here, that I know of, at least.
Anyone has any other items that they want to share?
By the way, Martin, I saw that you just… you asked for a correction of your,
your handle there, so, it's one of the trivial things that I was saying, that was probably just merged, so I just need to get,
Adriel to approve that, but, yeah, a good, catch on the, on the employer name.
Yeah, sorry, so any other items that, that you would like to bring up?
Around the table?
Nothing.
Okay, Zach, anything for you?
**Zach** 10:50 Nothing from my end at the moment.
**Dotan Horovits** 10:53 Sounds good. One other note, maybe if we're already here, we're going to have KubeCon in North America just around the corner. I, unfortunately, probably will not be able to attend, which is very disappointing, but I'm curious if any of you is going to be there, or planning, or might?
**Martin Costello** 11:11 Not me, no.
**Zach** 11:14 Yeah.
**Dotan Horovits** 11:14 Gotcha.
**Zach** 11:15 I don't… I don't think so.
**Dotan Horovits** 11:17 Okay, so…
I'll spare the briefing of where I can hook you up with relevant folks, but, yeah, I guess we'll get the updates afterwards on the good things that happened there. So, I think if that's the case, we can wrap it up for today, and we can carry on on the Slack if…
If anyone missed it and can chime in async.
Thank you very much for joining, and yeah, I look forward to seeing you at, Phase 2.
**Zach** 11:45 Yes, sir. Thank you.
**Martin Costello** 11:46 Thanks, Tom. Bye.
**Dotan Horovits** 11:47 Thank you, bye-bye.
