SIG: OpenTelemetry on Mainframes Weekly Meeting
Date: 2026-04-08
Duration: 12 minutes
============================================================

## Zoom Recording Transcript

**Greg Shriver** 01:46 Blue.
**Richard Salac** 01:49 Boom.
**Morgan McLean** 01:57 8.
**Greg Shriver** 01:59 Hey, Marvin. Hey, Richard.
Today may be a short call, unless Richard has something for the agenda, or you, Morgan. I don't.
**Morgan McLean** 02:10 I do not.
**Richard Salac** 02:11 Not really. I hoped for Rodrigo to join. I wanted to ask about the current status of the Java agent offered.
By the upper clock for the open telemetry.
**Greg Shriver** 02:24 Yeah, okay.
Yeah, so Rudiga, I don't know if you saw his chat, but he said that he wasn't able to join today's call. He did have a couple things that he was, planning on moving forward.
But, but he's not able to join today's call.
So, and I don't have any of that… I don't have the, the status on the, selector.
Is that what you were asking about, the collect…
**Richard Salac** 03:02 Not actually a collector, but the Java agent collecting the metrics from the mainframe, and we discussed that it could possibly become part of the collector.
But after the initial discussion, you know, the… The whole activity kind of got silent.
**Greg Shriver** 03:27 Excellent.
Who's Jim?
**Richard Salac** 03:30 No problem, I will drop him a message.
**Jim Porell** 03:34 Sorry for being a few minutes late. I did ping Rudiger yesterday, just so you know, if you were looking for him, and he said he was traveling today, he was gonna see if he could make it, but never heard back. You know, he didn't confirm, so my guess is he's not making it.
**Greg Shriver** 03:53 Yeah, he, he sent something on the, on the chat.
And said that he wasn't gonna be able to make it today.
**Jim Porell** 04:00 Oh, okay. I didn't… I didn't look in the last… I looked at 11.15 or so, and he hadn't say… Yeah, 1145, right.
Sorry for the old news and being late.
**Greg Shriver** 04:19 No, no worries. Jim, do you have anything for today's agenda?
**Jim Porell** 04:23 No, nothing really. Other than he and I went over this stuff last week, so…
**Greg Shriver** 04:31 Okay, got it.
He mentioned something about, Well, he did mention in the blog post that he was… or, the blog post, he mentioned on the chat that he was working on a blog post for the TPS, I guess that's the TPS1898.
**Jim Porell** 04:50 Yeah.
This goes back to… you know, Ludmila was trying to… Present us as a separate namespace, and…
**Greg Shriver** 05:02 Yeah.
**Jim Porell** 05:02 he was trying to get… I think one of the things… his last meeting with the General SIG, semantic conventions folks was they needed more people to vote on what we're doing.
And… so part of the blog post was to inspire more people, to participate in the reviews.
**Greg Shriver** 05:38 Can't spell, am I?
So, sorry.
**Jim Porell** 05:43 Oh, no worries.
**Greg Shriver** 05:45 I'm watching me type. I'm not good at it.
**Jim Porell** 05:58 Hey, Morgan, question to you while Greg's typing. Do you own this call? Because you can see, last week, we tried to join the call, right at noon, and we were blocked until the prior call hung up. I don't know who owns this Zoom call, but…
**Morgan McLean** 06:14 I mean, I can manage it. It's owned by an OpenTelemetry, sort of, Zoom account that we have.
**Jim Porell** 06:19 Okay, dude, fine.
**Morgan McLean** 06:20 shouldn't be blocked by prior calls. The way we set them up is they have independent, call IDs.
**Jim Porell** 06:27 Yeah.
Yeah, Greg and I hit it one other time, because we ended up chatting on, on the Slack channel, saying we were blocked, but…
**Morgan McLean** 06:38 Interesting, and it said the previous model.
**Jim Porell** 06:41 Yeah, it was, like, 5 minutes. It says, Because the call, you know, I've tried to capture it there on the April 1st, you know, and it's not a joke.
**Morgan McLean** 06:51 Call owner is on a different call. Interesting. Let me just check here.
We're using Zoom account number 4. Oh, the technical committee uses the same Zoom account. That's probably why.
I can change the… well, no, because we've… That, actually, no, that should not make a difference.
**Jim Porell** 07:13 Okay.
**Morgan McLean** 07:14 Let me look into it, but this is surprising. I'm just looking at the ID, 9621… Because I believe.
**Greg Shriver** 07:24 It's only happened a couple times.
**Morgan McLean** 07:25 Yeah, it's like there's twice.
**Jim Porell** 07:27 that I can think of, yeah.
**Morgan McLean** 07:28 There's a call going on right now that also uses the same Zoom account, and given that we are meeting with no problems, I assume it's fine. Let me dig into this, but I actually don't know what would be causing us, because we actually set things up specifically so this wouldn't happen.
**Jim Porell** 07:41 Okay. Yeah, I'm just, Don't have a clue why, but… and it got resolved within about 5 minutes, but there wasn't…
**Morgan McLean** 07:49 I supplies that whatever other call it was conflicting with ran over.
**Jim Porell** 07:53 Probably, yeah, I ran over, right, right.
**Morgan McLean** 07:55 Yeah.
**Jim Porell** 07:56 Or maybe there's a limit as to how many simultaneous calls.
**Morgan McLean** 07:59 That's what I'm wondering. Yeah.
Alright, let me know if it happens again, and what I can do is just pick one of our.
**Jim Porell** 08:05 Yeah.
**Morgan McLean** 08:06 I'd rather hold off, just because, unless it happens again, just because a lot of people here copy the calendar invites.
**Jim Porell** 08:14 Exactly, sure, right?
**Morgan McLean** 08:15 So if we change it, we risk fracturing this group.
**Jim Porell** 08:19 Yeah, I agree with you on that, too, so, yep.
**Greg Shriver** 08:23 For sure.
**Jim Porell** 08:24 So it's worth So, thanks.
**Greg Shriver** 08:29 One other little tidbit, a couple meetings ago, we talked about possibility of having an open telemetry on mainframe SIG related session at SHARE Pittsburgh.
Since then, I don't think any… I posted something out on the Slack channel.
And, nobody… oh, nobody outside of this group responded.
And, Rudiger responded and said that he wasn't, you know, he wasn't going to be able to make share Pittsburgh due to holiday. So, and he furthermore suggested that we kind of regroup and suggested that we try GSUK.
in November, if we wanted to do a live you know, a live, in-person type session at a conference related to the mainframe SIG.
So, I don't know what my status would be in terms of being able to attend that, but I just kind of wanted to throw that out there. I mean, it was… On the last meeting, I think, Jim, both you and, Richard from BMC, said that you guys weren't going to be able to attend Share Pittsburgh.
**Jim Porell** 09:46 That's correct.
**Greg Shriver** 09:47 Yeah.
And Morgan, I assume you can't either.
**Morgan McLean** 09:52 at the SHARE conference. I mean, I… if I pull some strings, I'm sure I could be, but there's probably not much reason for me to be there beyond… beyond a talk or something. But, you guys go ahead.
**Jim Porell** 10:04 Well, the problem is nobody… there isn't anybody that's willing to do the presentation, so that's… that's the issue. It's not… That it's not worthwhile, it's… What… none of us as principals in this call are available to do it, so…
**Morgan McLean** 10:19 Because of your calendars, or you're just not interested in doing talks?
**Jim Porell** 10:26 Yeah, it's just mine's a calendar problem. Okay.
**Greg Shriver** 10:29 I think it's more of a calendar than it is.
**Morgan McLean** 10:31 Oh, okay. I mean, we could… you could… I imagine you can do one at a future conference, or did you want a specific Someone presented that conference.
**Greg Shriver** 10:39 Well, I mean, I am from Pittsburgh, so, I mean, I could certainly do it, but my goal was not to be the only one up there saying, hey, you know, our goal was to have a panel discussion.
**Morgan McLean** 10:49 I understand, yeah. Yeah.
who else do we have? Is Rudiger gonna be there? He goes to the SHARE conference a lot.
**Greg Shriver** 11:00 It does.
**Jim Porell** 11:00 Sweet.
**Greg Shriver** 11:01 He can't be… he can't make it, yeah.
**Morgan McLean** 11:04 When is this?
**Greg Shriver** 11:04 Yeah.
Oh, it's… oh, shoot. It's in August.
When is it? I don't…
**Jim Porell** 11:13 16th to the 20th.
**Greg Shriver** 11:16 Thank you.
**Morgan McLean** 11:16 fail to find someone.
Oh… We sometimes have people from Wells Fargo who join this call.
I don't… I know they haven't been controlled.
**Greg Shriver** 11:32 That's true.
**Morgan McLean** 11:33 a lot, but perhaps they'd be interested.
**Greg Shriver** 11:38 Maybe.
**Morgan McLean** 11:39 Yeah.
I can talk to Antoine on my team, who joins this relatively often.
Let me think about my own attendance. Travel for me can be tricky at times, but, let me… let me think.
**Greg Shriver** 11:53 Cool, sounds great.
**Morgan McLean** 11:55 Okay.
Huh?
**Greg Shriver** 11:59 I don't have anything else.
**Morgan McLean** 12:08 We can probably wrap it up.
**Greg Shriver** 12:10 I think we can probably wrap for today.
Alright.
**Morgan McLean** 12:15 Thank you all. All three of you later. Alright, bye.
**Greg Shriver** 12:17 Cheers.
**Jim Porell** 12:18 Care, guys. Bye-bye. Bye.
**Greg Shriver** 12:19 Bye-bye.
