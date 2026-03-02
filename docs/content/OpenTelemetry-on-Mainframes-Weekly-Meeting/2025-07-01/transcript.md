SIG: OpenTelemetry on Mainframes Weekly Meeting
Date: 2025-07-01
Duration: 22 minutes
============================================================

## Zoom Recording Transcript

**Jim Porell** 04:39 Oh, hello! Everybody!
**Aaron Young** 04:45 Hello, Jim!
**Jim Porell** 04:47 How you doing, Aaron?
**Aaron Young** 04:48 Doing, good.
**Jim Porell** 04:50 Good. So I did see Rudiger is not making it today.
But I also. I also saw a whole host of things.
including, do you want to move the meeting to Wednesdays at this time.
**Aaron Young** 05:04 Okay.
**Jim Porell** 05:06 From the last time I the last meeting.
**Aaron Young** 05:11 Okay.
Hello. Greg.
**Greg Shriver** 05:18 Hello!
Hey, Aaron! I don't know if you saw or not, but Rudiga won't be able to make it.
**Jim Porell** 05:26 Yeah, we already, yeah.
**Greg Shriver** 05:27 Oh, okay.
**Aaron Young** 05:29 No, I think I didn't see it.
**Greg Shriver** 05:31 But yeah, Jim, let me know.
**Jim Porell** 05:35 I'm doing the edit right now for this meeting.
**Greg Shriver** 05:38 Oh, cool. Thank you.
**Jim Porell** 05:40 Yeah.
**Richard Nikula** 05:41 Wednesday would work for me.
If we do. If we do move it.
**Greg Shriver** 05:47 Okay.
**Richard Nikula** 05:58 Not a lot of meetings. For some reason. Hmm.
**Aaron Young** 06:03 Happens a lot.
**Greg Shriver** 06:09 So I think last time I think Morgan said that he would change the calendar entries
and open telemetry so that everyone would get a new, a new calendar series.
moving it to Wednesday. But Morgan's not here.
Cool.
**Jim Porell** 06:53 Anybody else.
**Greg Shriver** 06:56 Yeah, we might be able to do that. I don't know how, though.
to actually update the open telemetry shared open telemetry calendar.
I don't know how to do that.
**Jim Porell** 07:06 I don't either.
Is that on Google? Yeah, it is. Looks like.
**Greg Shriver** 07:12 Yeah.
**Jim Porell** 07:20 My bet is, you looks like it's actually on zoom, the meeting.
**Greg Shriver** 07:32 I don't know.
**Jim Porell** 07:32 There. Yeah, I don't know either. So.
**Greg Shriver** 07:34 Oh no!
**Jim Porell** 07:38 But if, Greg, why don't you put a response and and Tag Morgan that we agreed in this meeting to move it.
**Greg Shriver** 07:45 I can do that for sure. Yeah, I'll I'll I'll take that.
**Jim Porell** 07:49 Yeah tag him on slack, and then he'll see that.
**Greg Shriver** 07:52 Yeah. And if he sees that, then maybe we'll get it moved, because I suspect I mean, I don't know. But I I know Rudiga last week shared that Wednesday or Tuesday doesn't really work for him for some reason, I mean, I think he has some.
It was a personal reason. So I I don't. I don't. That might be why he's not able to be here today.
**Jim Porell** 08:13 Yep.
**Greg Shriver** 08:13 So so, okay, cool. Yeah, I'll I'll update the the chat.
**Jim Porell** 08:21 I don't know what else. I'm just looking at the meeting notice from last week.
looks like you, you, Aaron, and he are gonna do tech exchange and gse Uk.
and then just a list of work to do. Still.
**Greg Shriver** 08:38 Yeah, I do have one update yesterday last night was the I guess the the
deadline for the call for papers or Kubecon.
I did throw in a couple. I I put in 2 sessions, one
for me, for a lightning talk, and then another one
for a longer talk, and I was hoping that we could get someone else from the Sig to co-present
so and it's who knows whether whether it will be accepted or not.
But.
**Aaron Young** 09:28 And when is that Greg.
**Greg Shriver** 09:29 That is November in Atlanta. Cubecon is November in Atlanta.
**Jim Porell** 09:40 Wow!
**Greg Shriver** 09:42 So we'll see. I mean, they usually have. I've been to observability day at cube con before, and they usually
it's usually a packed agenda.
So an observability day is just one right after another. So I don't know how much room they're gonna have in the agenda, but we'll see.
And maybe Morgan can help there, too. So I think he's involved in the scheduling of those sessions.
So that's all I had to share.
**Aaron Young** 10:17 Okay.
Are you hinting at something, Greg?
No, not at all, Aaron.
So I was hoping Ritter and Morgan would be here. But
I don't know. Maybe I'll see if I can join next week, too.
**Greg Shriver** 10:35 Okay.
**Aaron Young** 10:35 So Greg already knows this. But Jim Richard Terry
Monday was my last day at Broadcom.
**Jim Porell** 10:42 Oh, no. Kidding. Wow!
**Aaron Young** 10:43 I officially retired.
**Jim Porell** 10:46 Wow!
**Aaron Young** 10:47 Yeah. So my my wife's been retired a couple of years, and
she's been patiently waiting for me to join her on some adventures, and
we thought now was a good time. So I'm a
I'm joining you as a civilian today. I'm I'm no longer employed.
**Jim Porell** 11:06 Okay, well, good for you.
**Aaron Young** 11:08 Yep.
**Greg Shriver** 11:09 Where? Where are you gonna bike first? st Aaron?
**Aaron Young** 11:12 So tomorrow there's a bike park
in the mountains of North Carolina, called Rocky Knob. So I'm gonna go check that out tomorrow morning.
**Greg Shriver** 11:22 That sounds awesome.
**Aaron Young** 11:24 Yup, Yup, that's great.
So in along with that announcement, Greg is going to be taking over any of the duties I had from a focal point of broadcom, so
he'll he'll be carrying this forward.
**Jim Porell** 11:41 Okay.
**Greg Shriver** 11:42 Yeah, you will be missed, Darren, for sure.
**Jim Porell** 11:44 Yeah, definitely.
**Aaron Young** 11:46 Oh, I miss all to you as well.
Thanks, Sherry.
**Greg Shriver** 12:00 Wow! Now I'm seeing it in in public notes.
It's official now, Aaron.
**Aaron Young** 12:05 It's for you.
**Greg Shriver** 12:07 It's real.
**Jim Porell** 12:09 Okay.
**Aaron Young** 12:10 I was I was in a meeting Friday with
one of the people from Plano Greg and.
**Greg Shriver** 12:21 Yeah.
he he said, something like, Oh, so you've given up. And I I think I'm gonna change my linkedin profile to. I gave up
like you.
**Jim Porell** 12:32 Can relate to that on occasion.
It's really funny cause.
I decided not to retire, made the conscientious decision to go that way, because still having fun stirring up, stirring the pot up. And
I'm gonna take more time off for sure, and you know, and enjoy myself as I'm doing it, and I'm only choosing to travel
if there's a personal tie in for me. So I have annual meetings, and I have kids in Charlotte and San Francisco and Richmond, Virginia. And then I like going to Australia and Lithuania. So.
**Aaron Young** 13:13 You know. I'll I'll do that kind of stuff, but share. Gsc, you know, less like a weasel. Some other.
**Jim Porell** 13:21 Been personal benefit out of it.
**Greg Shriver** 13:23 I probably don't want to put that in the notes, though.
**Jim Porell** 13:28 Manager is really good. I already asked to go part time.
and he goes, how many hours of work do you? Week and I go. 60, he goes. Well, I'm not paying you for 20 of them. So just work, just work 40. Why do you want to take a pay cut? I'm like, all right, I'll start there.
This is typically my last meeting of the day, anyway. So take most afternoons off.
**Aaron Young** 13:53 That's good, that's great.
**Jim Porell** 13:56 But not really. You know, Aaron, it's been a pleasure working with you both while you were at Ibm, and
you know, going through that trauma of you going to broadcom. So you know best of luck to you. You're an awesome person and really appreciate it.
**Aaron Young** 14:09 Thanks, Joe, I appreciate it. It was pleasure working with you as well and hopefully. We'll cross paths.
**Jim Porell** 14:15 So.
**Aaron Young** 14:16 Some time.
**Jim Porell** 14:18 So. Yeah. And you know your old team like, it's getting worse if you don't, if you're not aware. So.
**Aaron Young** 14:25 Murdo Murdad was let go.
Okay.
**Jim Porell** 14:29 You know, it's really it's pretty sad.
**Aaron Young** 14:31 Okay, yeah, I I I meet with some of the my older Ollie team.
occasionally, you know. Maybe once a quarter and.
**Jim Porell** 14:42 Yeah, yeah.
**Aaron Young** 14:42 So yeah, I I hear little little snippets.
**Jim Porell** 14:46 Yep.
**Aaron Young** 14:46 Yeah.
**Jim Porell** 14:49 Alright! I don't know anything else.
Throw in there.
**Greg Shriver** 14:55 Well, I had just one thing just to share, and maybe we don't wanna discuss it today, but just giving you guys a heads up. So
we
We were looking at some of the stuff that got the original. Not the Tps pull request, but the thing was the 1471 pull request the the base one
where we had and I believe that's where we talked about process id
and process id process.id, I think, was one of the examples, was the the 4 character, hex. 4. Character hexadecimal, asid.
And and there there was some consternation over. Well, what does that mean?
You know, when you also have unix system services, pids in one or more address spaces, because the top pid and I understand the top down, and everybody understood the top down where Asid made the most sense to be the route.
But even the root
the parent pid, or even the root. Pid doesn't match the Asid. So we have some disharmony there between between zos unix system services and the the hotel spec that's already been merged.
you know, into open telemetry. So
we haven't really figured out
what to do with that
And I suspect other people will have, you know, similar issues trying to decide
wh, which Pid to use when you're in an address space, that is, you know, both has unix system, services, workload and all, and is an address space with an asid, because they all have that.
So.
**Jim Porell** 16:40 I think those that might be related to the other conversation, which how many different process models do we have? Because you can start now looking at kicks. Ims batch uss. And so what do they inherit? You know? Maybe the process id is still the asid at the top.
But
there's a lot of unique things for each of those you know, different styles that might not might not be true in a unix windows, you know, Linux windows, environment.
**Greg Shriver** 17:11 And then someone even brought the the topic of underscore Bpx share, as which, of course, changes everything right.
Cause. Then when you wait, cause, then you get another address space and another, add asid, right for a spawned process. So that
that's just like, Wow, yeah. And I think it just goes back to your point. Jim, of
you know how many different process models do we have.
**Jim Porell** 17:35 Yeah. So I don't know. I don't know.
Same thing in Linux world. If you fork something. Is that a new process, id, or is it under the master
cause? That's kind of like what you just described.
**Greg Shriver** 17:48 Yeah.
**Aaron Young** 17:49 Yeah. So yeah, I mean, you know, normally, yeah, if you fork, you'll have a new process. Id, but it'll have a parent. Id.
**Jim Porell** 17:58 So it's still gonna be under the parent.
Yeah.
**Aaron Young** 18:00 Yeah.
**Greg Shriver** 18:02 And the parent id stuff works in unix system services, too. But the problem is, there's a parent, there's a common parent, but it's not the asid, you know. So that's.
**Aaron Young** 18:11 Yeah.
**Greg Shriver** 18:12 Where where do we put that parent process? Id when it is you? A unix system services workload. So
maybe that's something we can just kind of stick in the back of our minds and noodle over
cause I I suspect that, you know, just like with any standard as what we're trying to, you know, work on here with any standard. Different vendors and different users are probably gonna interpret it differently, and some are, gonna choose the asid, and others are, gonna choose the parent Pid, and that's probably gonna be a kind of a
you know.
It's not not that it's the end of the world.
you know, because we already have those those disharmonies. Now, right.
**Jim Porell** 18:49 Alright.
I can get some guys on our side to talk about it to see what they think. So.
**Greg Shriver** 18:55 Cool. Yeah.
**Jim Porell** 18:56 Hey? I'm I'm thinking out loud, too. I was looking at the last meeting notes. Sorry to go back to Aaron again. So you're gonna do these presentations with Rudiger at tech Exchange and gsc, or is that gonna be Greg? Now.
**Aaron Young** 19:09 I I think that's gonna be Greg. Now, if he is able in in your schedule to do it.
**Greg Shriver** 19:16 Yeah.
I looked at Gsa, uk, I think. I mean, I think I can do that one. I didn't know what's tech what's text check exchange?
**Jim Porell** 19:25 That's in Orlando in the beginning of October, I think the second week in October.
**Greg Shriver** 19:31 Oh, my son's getting married on the 11th of October, so I'm thinking that that's a no go for me.
**Jim Porell** 19:37 And I have a big party at whatever the 13, th the Sunday of that weekend. So.
**Greg Shriver** 19:42 Yeah.
**Jim Porell** 19:43 I'm I'm not available.
**Richard Nikula** 19:44 I. I am kept currently somewhat scheduled to be there, so I could help out if needed.
**Greg Shriver** 19:51 Oh, that's good.
Yeah, thanks, Richard.
**Jim Porell** 19:56 So I'm gonna make a note. I'll I'll copy that from the last meeting up.
**Greg Shriver** 20:02 Cool.
Yeah, thanks for bringing that up.
Yeah.
Survey. Blog. Beginning of July.
**Aaron Young** 20:37 Yeah. I don't think that.
**Greg Shriver** 20:38 Virtue.
**Aaron Young** 20:39 Don, anywhere.
**Greg Shriver** 20:42 Virtualization self hosted Github actions, hotel collector support tier 2.
Yeah. And there was a an entities discussion. I don't know.
I don't think I don't think we ever ran that one to ground, but
we'll probably want to defer that until we have Rudiga.
**Jim Porell** 21:07 Yeah.
**Greg Shriver** 21:10 Cool. I don't have anything else for today.
**Jim Porell** 21:15 Okay.
I'm good.
**Greg Shriver** 21:22 You, Aaron? Do you have stuff that you.
**Aaron Young** 21:26 I have nothing else.
**Greg Shriver** 21:28 Nothing else.
How about you?
**Jim Porell** 21:31 Enjoy it.
**Richard Nikula** 21:34 Nothing.
**Greg Shriver** 21:36 Okay.
**Jim Porell** 21:37 Alright!
**Greg Shriver** 21:38 Oh, man, maybe we can. Maybe we can call it a wrap. Then. Sorry.
**Jim Porell** 21:41 Sounds good. No, no. I was just gonna say, you know, yeah, with a wrap. And again, best of luck to you, Aaron, enjoy.
**Greg Shriver** 21:48 Enjoy this new life for yourself absolutely.
**Aaron Young** 21:51 Alright thanks. Appreciate it.
**Greg Shriver** 21:52 Enjoy that bike, ride.
**Aaron Young** 21:54 I will, and I'm sure I'll be lurking here and there, so.
**Greg Shriver** 21:58 Good.
**Aaron Young** 21:59 Alright. I'll see you later.
Good to see you.
Okay, bye, bye.
**Greg Shriver** 22:02 Alright, bye.
