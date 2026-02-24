SIG: OpenTelemetry on Mainframes Weekly Meeting
Date: 2026-02-11
Duration: 20 minutes
============================================================

## Zoom Recording Transcript

**Greg Shriver** 01:05 Hello.
**Jim Porell** 01:07 Come on.
I looked at Slack, I didn't see anything there, so…
**Greg Shriver** 01:14 Yeah, except for… Macau and… Macau and Grigors?
I didn't get his last name.
They said that they were going to be at the meeting to discuss the potential contribution from
Papa Gloyd?
**Jim Porell** 01:41 Okay.
**Greg Shriver** 01:46 So, I'm hoping Rudiger joins, because I know he, he had a discussion with
With… with Macau, I believe.
**Jim Porell** 01:56 Yeah, I see that now. I didn't look far enough back.
**Greg Shriver** 02:06 Yeah, I hope they join.
**Jim Porell** 02:24 I like Dylan Meyer's question. Out of curiosity, what kind of mainframe? You know, oh, it's a Burroughs. No. No, I'm just teasing.
**Greg Shriver** 03:02 So… Take a look at the…
Notes, we don't have a new… okay.
Give it out.
**Ruediger Schulze (IBM)** 03:54 Hi there, I realize I'm very dark here today.
Very dark.
**Jim Porell** 04:00 There you are, what are you, in a car?
**Ruediger Schulze (IBM)** 04:01 Yeah, actually, yeah, I'm sitting in the car. I have to get out, pick up my kids in half an hour, actually, so I can't stay too long today.
**Jim Porell** 04:12 Okay. -Oh.
**Ruediger Schulze (IBM)** 04:13 Okay…
**Jim Porell** 04:14 You can go off-camera if you want, if that helps you.
**Ruediger Schulze (IBM)** 04:17 Yeah, okay, yeah, so you have seen me… We know, we know who you are. Okay, good.
Okay, let's look at a couple of topics.
**Greg Shriver** 04:38 Rudiger, will you be able to share, or do you want me to share?
**Ruediger Schulze (IBM)** 04:41 Maybe if you could share, I had issues in the previous meeting.
**Greg Shriver** 04:44 Sure, okay.
Alrighty.
Alright, the agenda, I just copied this, so… Sure, what's going on here?
So, I was hoping that, Macau from Hoppock Lloyd.
was going to be able to join. They said they were gonna try and join.
But if not, then… Guess that's okay, too.
**Ruediger Schulze (IBM)** 05:27 Yeah, I think I can at least give a… give a brief overview of what we discussed, and as I also said on the Slack channel, so the asset…
that they have been working on, and that they are thinking about to contribute is a Java application.
that reads the RMF REST API and uses the Java OpenTelemetry SDK to translate the received input into OpenTelemetry protocol format.
So this is, like they described themselves, actually, it's pretty much straightforward, but they would like to have this component, you know, considered for contribution, and also for ongoing maintenance.
I think based on what was discussed,
On the Slack channel. I think there's different ways of looking at taking this in.
I think that was discussed about the potential rewrite in COBOL and making this an open telemetry receiver.
Yeah, a collector, receiver. Obviously, that's one way of looking at it.
But, might be actually also an option.
to…
And Richard, I see you are on from a SOE perspective. Maybe this is something that could have a home within the Open Telemetry project, or under SOE. I think this needs more… more discussion on… on how to approach this. I was just generally thinking…
If you look at the collector, then obviously it requires a rewrite in Go.
Let's leave this discussion around if it runs on platform, or off-platform, or…
on Unix system services aside for a moment, it would just require that, you know, a proper receiver is being created for this.
And from a…
from a Java point of view, and this is, in fact, something that I still wanted to check.
check, but, I mean, the Java SDK obviously has certain contributions.
It's more a gut feeling, but I suspect a component like this would not be…
something that, you know, would find a home in the Java contrape rep repository, or repositories.
So… if we would consider this, or if this would be considered for open telemetry project.
take in, I think we still would have to look at where this could land.
So… so maybe as an intermediate open telemetry, sorry, open mainframe project, as…
Could be a good landing zone.
**Jim Porell** 08:19 Yeah, I know, and John Murtech, I saw, he commented on the Slack channel.
They're looking for some new contributions, so that's interesting. I don't know… you know.
That's part of it, but the other part of it is…
How might… what have they done that would help us with the semantic conventions?
**Ruediger Schulze (IBM)** 08:40 Yeah, that's an interesting question as well, of how they took the data, and this is an aspect that I didn't discuss on the call with them.
Of how they took the, you know, what kind of transformations they applied to the data, getting it from the rest.
**Jim Porell** 08:59 Because I think what they want to do is kind of independent of what we've been thinking about here. We've been mostly focused on the naming.
**Greg Shriver** 09:09 Right. And if you take a look at the output from the ZOSRMF REST API, there's… I mean, honestly, there's really not a lot there in terms of metrics. It would be, you know.
**Jim Porell** 09:19 Correct.
**Greg Shriver** 09:22 But again, yeah, you're absolutely right. I mean, what…
How… once you get those, you know, limited set of metrics.
you know, from the REST API, what do you call them when you publish them?
**Jim Porell** 09:38 Yep. I think that would be really interesting.
**Greg Shriver** 09:41 Yeah, I would agree.
**Jim Porell** 09:43 I think, yeah, that might help us way more than anything.
**Richard Salac** 09:55 Can we ask them for some sample of the metrics, of the JSON that is sent to the OpenTelemetry collector?
**Ruediger Schulze (IBM)** 10:03 I suppose so. Maybe they could even create a…
Sample, you know, output from the…
From the collector that they sent to, yeah, I guess it's… it's a fair question. So,
Let's… I guess, as Michao couldn't join today, let's, you know, let's continue the discussion on the Slack channel.
**Greg Shriver** 10:53 I'm a lousy typer.
**Ruediger Schulze (IBM)** 10:56 But I appreciate it that you're doing it. Thanks, thanks, Greg.
Yeah, so I suppose we just… the discussion continues on… on the… on the Slack channel, dunn…
I'll just go from the top from the last meeting, Craig.
**Greg Shriver** 11:19 Yep.
**Ruediger Schulze (IBM)** 11:20 Yeah, we provided our input, update on the SICK approvals that also worked.
That… actually, yeah, that takes us to the topic…
So, I don't know if this is common practice, but currently we have, like, two…
Two persons assigned from a sick perspective as approvers, maintainers, and triagers.
Was cracking myself.
It's… it's a little bit a question of, you know, moving forward, we should have a soak person there.
If somebody would like to volunteer to be this person, I think we would be open for this.
This is essentially to avoid situations when Greg, myself, are not there, or when Greg and I offer something, but the other person is not there, then, you know, we have kind of, like, a blocking situation, because nobody can approve these
these PRs to move forward.
So, having assault person just joining, you know, these different roles, I think this will help us
from a Sikh perspective, to unlock some of the…
The blocking situations that we may have seen in the last couple of months.
**Jim Porell** 12:44 I'm willing to help out. I am not a developer. I've done Git a few times, and so if somebody wants… I don't want to do it now, but if somebody wants to…
give me a coaching lesson, I'd be happy to do it.
That's what I did last time when I was doing my Git development, wrote it all down.
But, if somebody else is more familiar, go ahead.
**Ruediger Schulze (IBM)** 13:08 Yeah, appreciate that, Jim. Let's do it like this, let's put the topic up here,
And, you know, on one of the next meetings, just, you know, if nobody else is…
comes, Jim. It's… we come to you.
**Jim Porell** 13:26 Alright, no problem.
**Ruediger Schulze (IBM)** 13:27 Thanks.
**Jim Porell** 13:28 I think everybody take a step backwards, and I'm standing there still, yeah, no problem.
I already put it in the notes, you're already willing, so…
**Greg Shriver** 13:40 So what was the net? We're gonna… we're gonna put it in the Slack channel, looking for volunteers?
**Ruediger Schulze (IBM)** 13:44 Yeah, let's put this to the slug channel.
Right.
**Jim Porell** 13:59 I'm gonna be, like, next thing I'll be doing, like, Aaron, well, I'd like to announce my retirement next week.
**Ruediger Schulze (IBM)** 14:10 Right. Then, just FYI, so I think the PR, the TPS PR is still sitting where it was. I left it in a good state, but I think…
There were also some people on the semantic convention stick, I think, unavailable.
I haven't checked it, but I think that's the situation that you're in.
**Greg Shriver** 14:35 Okay.
And I have no update for the dock PR. I know we went over the next steps, and I know they're on me to do, and I have not done them yet, so…
Unfortunately, my update is a no update.
**Ruediger Schulze (IBM)** 14:49 Okay.
Yeah, when, you know, next time, when time allows, just, let's… let's… Get it done.
**Greg Shriver** 14:57 Yeah.
**Ruediger Schulze (IBM)** 14:58 And kind of like, same applies for me. I wanted to open issues for… for the messaging and database, spans. I was starting to draft it, but I never submitted it.
So, I would…
I'm actually out next week, but, you know, it should happen in the next couple of days.
Right.
Yeah, I think this leads us to what we said. We want to encourage small PRs that should be easy to, you know, push… put forward and progress.
Yeah, I think that's… that's the general message that we keep sharing.
On the other topics, and it seems like this time is maybe not as good as it was before for…
Well…
Yeah, we had… the discussion around the collector, sorry, not the collector, we had the discussion around
Jitab Action Runners.
I think this is still with the CNCF, based on the messages that I have seen.
So… As soon as there's something coming, then I think we have a chance to look at
Working, for instance, on integrating the Jitap Action Runners into the collector build.
Obviously, the collector is already built for the platform, but that would then apply to update additional
workflows, so that,
For instance, also, unit testing is being performed.
Right.
Yeah, I think that's, on a high level, it's the current status.
Anything… Somebody wants to add.
**Greg Shriver** 17:42 I'm… I'm hearing nothing.
**Jim Porell** 17:44 Yeah. Yeah, me either.
**Ruediger Schulze (IBM)** 17:46 Yeah, so next week I'm unavailable, the week after I'm traveling, but I hope to join, actually, if…
Time allows.
**Greg Shriver** 17:55 Yeah, I should be here… I should be available for next week.
The following week, I believe I am at SHARE.
And I don't think I will be able to join.
**Ruediger Schulze (IBM)** 18:07 I see. Oh, actually, yeah, that's good.
I won't be at chair this time.
But yeah, keep the open telemetry flag up, and… Make advertisement for the sick.
**Greg Shriver** 18:22 Absolutely. We will. We will.
**Ruediger Schulze (IBM)** 18:25 Okay.
Good.
**Greg Shriver** 18:30 Alright.
**Jim Porell** 18:34 No, I'm a plumber for the rest of the afternoon, so, you know, you guys can keep talking, just delaying me from fixing all the frozen pipes here, but…
I came home from being away for 2 weeks. I'm actually really lucky. I was away for 2 weeks, my girlfriend's away for a week, and we have houses next to each other. Her pipes burst.
Mine did not, but neither one of our boilers are working, and it's like, oh my god.
So…
**Ruediger Schulze (IBM)** 19:01 Yeah, okay, then, yeah, hopefully this will be solved soon, Jim, and…
**Jim Porell** 19:08 Yeah, you got it quite cold there, right? Yeah, it was, yeah, it was, for you, it was minus 20 Celsius, so…
Yep.
**Ruediger Schulze (IBM)** 19:20 That's… that's quite… quite.
**Greg Shriver** 19:23 Quite a winter time.
**Jim Porell** 19:24 So yeah, I was in Vilnius last week, and everybody was asking me, well, what do you think of our weather? Because they were minus 20. I'm like, it's home.
So, which is zero in Fahrenheit, so,
No, it's been freaking cold here, and it's snowing right now. We got 2 feet of snow, 60 centimeters, whatever.
**Greg Shriver** 19:43 It's awesome.
**Jim Porell** 19:44 Winter Wonderland, and now I want to leave.
**Greg Shriver** 19:48 I'm gonna leave… Well, good luck with that, Jim.
**Jim Porell** 19:52 Yeah, thanks.
Alright.
Good.
**Greg Shriver** 19:57 Already.
**Jim Porell** 19:57 Okay, have a good one.
**Greg Shriver** 19:59 Thank you, everybody. Bye-bye.
**Richard Salac** 20:02 Bye-bye.
