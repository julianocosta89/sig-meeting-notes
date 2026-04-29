SIG: CI/CD SemConv SIG
Date: 2026-04-28
Duration: 18 minutes
Zoom Recording URL: https://zoom.us/rec/share/y43pmXgAJHCHIBMVkGbwQjRwLoVnyxrwaNgOfjEBur70WRhdh73rlgDqd1RsLhsV.uZYrHkL2IhnLB376
============================================================

## Zoom Recording Transcript

**Alan Clucas** 01:19 Hello!
**Christophe** 01:20 Hello?
**Alan Clucas** 01:27 How are you doing?
**Christophe** 01:30 Why aren't you?
**Alan Clucas** 01:31 Yeah, it's alright.
**Adriel Perkins** 01:39 Good day.
**Alan Clucas** 01:41 Oh!
**Adriel Perkins** 01:43 How are y'all?
**Christophe** 01:45 Why not you?
**Adriel Perkins** 01:48 I'm alive and kicking.
I see.
Alright, the agenda is up, feel free to add.
Alright, we can get… get started, I think.
Let's go into some board grooming as a first place to start.
I think I had a few to-dos from last, like, time.
Let's see, did I get them all done? I don't know if I did.
Maybe it was the time before.
Okay, I don't have a ticket for this one.
But I do have a ticket for these four.
Those tickets are right here.
At the bottom of the backlog.
We could… I guess we probably should move them into Titu? What do you think?
What do we want?
**Christophe** 05:52 Agreed.
**Adriel Perkins** 05:53 hour.
Alright.
Alright.
Now, I think we were going to have… did I… Yeah, I needed to open an issue for this exec span, didn't I?
That, I did not do, so I will leave that on my to-do list then. The other ones I did do.
I think we did kind of discuss it ad hoc, though.
Remember correctly?
So we're kind of like, it doesn't make sense, but we just need a document why that doesn't make sense. Does that sound right?
**Christophe** 06:51 I don't remember what we discussed exactly, so I think it makes sense to just create the issue and… Start discussing on it.
**Adriel Perkins** 07:01 Okay, sounds good.
I will.
Okay, I'll just move this up so it doesn't get lost.
Still need to do… this one.
All right, for any in-progress stuff, anyone wanna, Carlos, anything you want to talk about on, producing long-running traces issue?
**Carlos Alberto Cortez** 08:03 No, nothing much. Well, you may remember that last week, Robert was here, we were talking about, the different approaches, how to implement, how to update the spam processor interface.
So I was playing with some details there, what he proposed, which was, like, more explicit.
Actually makes more sense in my prototype. Having wrapped it up.
What basically we'll restore. But yeah, I think that, Yeah, I don't… I don't think this group will have an opinion about what way how to implement this, as long as it works, from the spam process or interface change perspective. But yeah, I'm still working on that.
**Adriel Perkins** 08:45 Okay.
Cool deal No, this one looks…
**Carlos Alberto Cortez** 08:54 One question, sorry, before we move to the, we move on, we move on. I have been working on this as a side project. I would like to know whether this is something that you think We'll have, like, priority, and I'm asking that because, I have been busy with other stuff, but still trying to dedicate some hours a week.
But now that one of the… that I was working on would emerge, probably will be more, like, we're having more cycles. I would like to know how important this is, you know? I think that, I guess that the question is, is mostly because this effort has been taking 2 months.
And it has been prototyping, back and forth with specification, and all that stuff. But how important do we think this is?
**Alan Clucas** 09:47 I would certainly, once there is an implementation I can implement against, I would… I would implement Argo workflows against it to prove it. At the moment, I've marked spans as beta, because… Or Alpha, I can't remember, just because there's… we haven't implemented CID SEMCOM either, but, because… mainly because of this, because I cannot… produce span… normally, the workflow controller is able to die whenever it likes, and everything carries on normally, but without this being done, spans do not Survive a reboot of the controller, and restarting the controller's normal.
behavior, so I would like to use it, Well, I'm just one person, and so…
**Carlos Alberto Cortez** 10:38 No, but I think that that's good to know, because, if… I guess that that was kind of my question, like, whether we have people that could be, like, you know, trying this out when it's implemented.
So that's good to hear, yeah. I was afraid that it's, like, something that we would like to have, but it's, like.
we don't have anybody ready, and then we will have to wait for months to get more feedback. But since we are… Yeah, trade that, that's… yeah.
**Alan Clucas** 11:06 I'm happy to implement the Go SDK side of this as well, if that's… Yeah, you know, I can put… contribute that to the SDK in OpenTelemetry.
Although it's… more people involved is obviously better, but, because I'll be implementing against my own interface. But the SD… your specification should be the prime goal as to what I'm implementing against. So, yeah, really happy to do that. I have to argue for time to do this, because as far as my company's concerned, I've delivered spans, so they're, you know, tracing is done. I usually get to persuade them what to do.
**Carlos Alberto Cortez** 11:47 Yeah, I mean, I would say, just to wrap this up, so I don't think more time is, like.
even if we get feedback, like, this is not working because of this and that reason, this is still useful, you know? But as long as… as I said before, we need people who can implement the other side of the puzzle, you know? Okay, good to know, perfect, yeah.
and they can move out. Yeah.
**Adriel Perkins** 12:07 There's also, too, like, I mean, the long-running trace issue has been, I think, an issue that's been opened in some form for a few years, and there have been people who have been asking about, for some of these things that run super long, is there a way to get this data live instead of, like, waiting for it to finish and populate?
Which is the way, you know, like, spans operate now, where you just, you emit, you emit the finished result, not the, like, in-between.
unless you're doing, unless you're in Dagger, and Dagger, what they do is they'll basically just send it twice, and they send it once on start, and then they're able to visualize that, and then they send it twice on the finish, and it just replaces that… that span.
But there have been people that have been, like, asking for that as well. I think, like, he would probably really like to use this in his company, because he's got a lot of issues that have been opened against the GitHub receiver.
If you need extra help on prototyping any of that stuff, let me know. I'm happy to try to, you know, move around my bandwidth, and show, and help there as well.
So, yeah, happy, happy to support in any way, you know, you feel necessary or would like.
**Carlos Alberto Cortez** 13:18 Yeah, in that regard, there's, as you may all remember, there's some overlap with this project that George Stewart has called,
**Adriel Perkins** 13:27 Yes.
**Carlos Alberto Cortez** 13:27 and maps, you know?
Yeah, I don't know, I think that could be… it could be super nice to explore that part, but at the same time, I know he's busy doing what Gio thinks, and we have only so many people to help here and there, you know? Also, I don't know how much cycles would be required to make that project part of hotel, if we were to actually, you know, to try to make it into… part of hotel. But anyway, that's, so people, in case they're interested, they can also try that.
**Adriel Perkins** 14:00 Okay. Yeah. If you feel good about it, I can just, like, spin up a group chat with me, you, and… And Josh, and Alan, if you'd like.
**Carlos Alberto Cortez** 14:11 Yeah, yeah, yeah, we can… we can, we can do that. I already talked to him a couple of times about this, and I think that… at least the initiative that he was providing was regarding, like, going with this approach based on what he, what he has. But we can always, of course.
Talk more about the… the potential of having his project, like, you know.
You're gonna see more love, yeah.
**Adriel Perkins** 14:37 Okay.
Okay.
Cool deal.
On the SDK support for spec change, I think there's a couple that Robert's going back through and checking, but there's definitely been more progress. I think, like.NET is looking at trying to implement it now.
This has been… I'm surprised at… how much support this has gotten. So this has been pretty cool to see, lots of implementations.
So… and then, of course, Robert's been heavily working on stabilization of the spec. He's been… He's been, doing a pretty dang good job on getting this stuff through, so, it's good to see, we've made… there's a lot of progress that's been made on this front. So, more implementations to come, but, you know, if you… if you see an item that's not checked here, and you would like to go try to implement it, have… feel free.
**Christophe** 15:30 Robert has also asked us to… do another review of C-Spec, just in case anything is missing.
**Adriel Perkins** 15:39 Good shout-out.
Alright, Alright, anything anyone has that they want to bring up?
**Christophe** 16:31 From my side, the consistent spelling PR has been merged.
There were a few that remain spelled as CICD, but that's because they are auto-generated from the namespace ID.
I would take a stop at, correcting that?
But I don't think it's that important, if it wouldn't work.
**Adriel Perkins** 16:54 Yeah, made sense.
Yeah, I guess if it's auto-generated from the namespace, it kind of is what it is.
**Christophe** 17:02 Yeah, we could always adapt Weaver, but that's a bit more complicated.
**Adriel Perkins** 17:07 Yeah, for sure, for sure.
And I'd hate to say, well, can we do CI hyphen CD?
And break the namespace name.
To try to get that behavior.
Oh, is that what?
**Christophe** 17:23 That'd be a big breaking change.
**Adriel Perkins** 17:25 Yeah, it would.
**Christophe** 17:26 would also be generated as CI space CD.
That's the namespace idea.
**Adriel Perkins** 17:33 Lovely. And then it would still lead to inconsistency. It almost might just be better to wait on, unification of pipelines.
**Christophe** 17:44 Oh, I will take a look what I can do.
**Adriel Perkins** 17:47 Alright, well, thank you for running through that.
**Christophe** 17:52 Other than that, I'm still working on adopting the CICD conventions in Jenkins.
that PR has stalled a bit, I will… Try to get, more reviews on that.
And that's it from my side.
**Adriel Perkins** 18:11 Is there anything you need help with on the stalling? I mean, I don't know that I could help in the jigging community.
**Christophe** 18:16 No, I'm in contact with the reviewers on Slack, so I will just ping them.
**Adriel Perkins** 18:22 Bye.
Okay, cool. Anything else from anyone?
Alright, well, we'll give some time back to everyone's day. Y'all have a good one.
**Alan Clucas** 18:41 You too?
**Christophe** 18:43 See you.
**Alan Clucas** 18:44 Bye.
