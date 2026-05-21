SIG: OpenTelemetry on Mainframes Weekly Meeting
Date: 2026-05-20
Duration: 17 minutes
Zoom Recording URL: https://zoom.us/rec/share/64wlo7xt0LFRgCspaipNJ5UxlNm-ojlc9EzXQH7bfSmBlFqp5tUdp6t_Fw8lJ-8w.1wjerrP-tmbgpda7
============================================================

## Zoom Recording Transcript

**Jim Porell** 07:03 Oh, there's a friendly face.
**Greg Shriver** 07:10 Hey.
**Jim Porell** 07:12 How are you?
**Greg Shriver** 07:14 I am… I am well, how are you?
**Jim Porell** 07:17 Survive it.
**Greg Shriver** 07:19 Yeah.
**Jim Porell** 07:20 That's what it feels like right now.
Jeez.
**Greg Shriver** 07:23 Fireflies.ai notetaker.
**Jim Porell** 07:26 That's some new thing that CNCF put in.
I think you have to have a Zoom ID, because I know Antoine went in and closed it, shut it down, but I tried to do it And you have to be able to have a Zoom sign-in to do that, I believe, so… Oh, maybe it's in the chat. Hold on, look in the chat.
I think it tells you how to do it. Yeah, there it is.
**Greg Shriver** 07:53 I mean, I wonder… Mmm.
**Jim Porell** 07:55 Slash SS.
No, we kept turning it off.
**Greg Shriver** 08:00 Oh, really?
Okay.
**Jim Porell** 08:02 There we go.
**Greg Shriver** 08:03 Yeah, it's gone.
**Jim Porell** 08:04 That worked, yeah.
**Greg Shriver** 08:05 FF leave. Oh, okay. Wow.
**Jim Porell** 08:12 So… I don't know, we had a good meeting last week, you know, a lot of stuff going on, but I know Antoine can't make it, and… Let's see… I don't see you rooting around line. I think he's on holiday, because.
**Greg Shriver** 08:26 Okay.
**Jim Porell** 08:26 Told me it was in the Nordics the other day.
**Greg Shriver** 08:28 Oh, wow.
**Jim Porell** 08:29 autonom.
Yeah, so in parallel to this, The Open Mainframe project.
**Greg Shriver** 08:36 Yeah, that's been so…
**Jim Porell** 08:38 sitting, you know, they're desperate, you know. All the sponsors have lowered their money, you know, Broadcom's still the big ones.
But everybody else is lowered their contributions, so they're, you know, John Murtech, that's how he's getting paid, I'm assuming. So he's like, let's create some more projects.
And one of them is a new package manager. Instead of using SMPE from IBM, you know, using RPM, like… Technologies, you know, so that… you know, and that would mean not only to have the package manager, because I guess IBM's ported a bunch of package managers, the problem is they're also language… dependent.
So, you know, you got NPM, RPM, and another one.
But anyways, trying to come up with a package manager that's a modern style versus this legacy SMPE nonsense. And then, but then also getting us as vendors to exploit it. So that was one project.
Another one came up was an open, telemetry collector, and it was interesting.
**Greg Shriver** 09:43 I think it's richer…
**Jim Porell** 09:45 Richard… but Richard Nikula from BMC, myself, and Rudiger were on the call with John Murtech, and I guess it was Richard that had suggested it, but he goes, no, that's not what I want. He goes, what I want is an agent.
that works, because we have vendor code, you know, middleware that we supply, and I can think about UK's IDMS, A database, you know, Datacom, that also wants to support OpenTelemetry, and… you know, has an SDK been developed that meets their needs? Like, is it… You know, will it run in key zero, you know, or weirdo keys? Will it run in the right programming language? So, kind of having an open collector, and then it could also be used to instrument your code, too.
So, anyways, that's kind of the idea behind that one. So, it's kind of related to this project, but similar people, but different.
**Greg Shriver** 10:46 Yeah, I, you know, I heard wind of that on last week's meeting, and I was curious, but yeah, so… So, a couple new projects for… okay.
A couple…
**Jim Porell** 10:58 So, I mean, you might…
**Greg Shriver** 10:59 Mainframe projects, yeah.
**Jim Porell** 11:01 Yeah, I think the idea is, let's… The first thing is, To get something going, To put a proposal together, and then solicit more… more people. Now, if you want to be part of the proposal.
It takes 10 seconds to fix that, you know, so I can add you to that for future meetings.
You know, to represent Broadcom in that.
It's up to you.
But the first thing is scoping it out, and there's a whole bunch of bureaucracy behind, you know, getting it defined as an approved project by the Open Mainframe Project.
**Greg Shriver** 11:39 I'm sure. I actually want to reach out to, Rose Sakache first.
before, because she may.
**Jim Porell** 11:47 Yeah, and Broadcom. I mean… Yeah, yeah.
**Greg Shriver** 11:48 I… yeah, you know, I know she's already very well plugged in with Open Mainframe.
So, yeah, and the… let me, I appreciate that.
**Jim Porell** 11:59 Yeah, do that. Yeah, yeah, yeah.
**Greg Shriver** 12:00 Let me talk to her.
**Jim Porell** 12:01 Hold on, let me… but I can give you the web link.
to the document, so at least you get a scope, too. Let me find that.
Yeah, cause this has all the… This has all the, the objectives, target users, and the proposal form, so at least you get a start of the scope.
I'll put that in the chat.
**Greg Shriver** 12:32 Actually, we might even just be able to put it in the meeting minutes, say, hey, this is a parallel project.
**Jim Porell** 12:38 Oh, yeah, yeah, alright, I'll do that. Go ahead.
**Greg Shriver** 12:45 Just so everyone who's looking here may want to go look there too, since it is sort of… At least a close second cousin, right? Or first cousin, whatever.
Who's fine.
Okay.
**Jim Porell** 14:17 Good.
**Greg Shriver** 14:19 Cool, yeah, thank you.
**Jim Porell** 14:21 Yep.
**Greg Shriver** 14:23 Yeah, that's… that's… that's good.
And it would be good to at least know, you know, what we're proposing, or what's being proposed.
And that's being proposed as an open mainframe project, right?
**Jim Porell** 14:38 Yeah, right.
**Greg Shriver** 14:39 project, yeah.
**Jim Porell** 14:40 Yeah.
**Greg Shriver** 14:40 Okay.
Cool, yeah.
Yeah.
**Jim Porell** 14:46 I mean, I mean, Greg has been in the higher level meetings, so there's no reason, you know, this isn't secret shit.
No reason not to tell you about it.
**Greg Shriver** 14:58 Oh, yeah, yeah.
**Jim Porell** 15:02 It's open.
**Greg Shriver** 15:04 It's… yeah, it's open, yeah.
So, alright.
Cool.
**Jim Porell** 15:11 I think we've got a quorum here, and I think we're done.
**Greg Shriver** 15:13 Yeah, I don't… I don't have anything else.
I don't have anything new for today.
**Jim Porell** 15:21 Okay.
**Greg Shriver** 15:21 Although, wait a minute.
**Jim Porell** 15:23 Oh, I did.
**Greg Shriver** 15:23 see that, OpenTelemetry graduated.
Which was… Well, it's now a graduated project under CNCF.
**Jim Porell** 15:35 Oh, okay, alright.
**Greg Shriver** 15:36 So… so… yeah, I mean, I don't know that that necessarily… I mean, I knew that we had known that, we had known that they were working towards that, because there were a bunch of questions of, you know, like, what's your roadmap? What do you see, you know, what are you… what are the major things that you're working on in the next 6 months, blah blah blah.
And I know that there was those questions that were… that were hanging out, but I saw… Actually, Angelica pointed me to it, on the, the OpenTelemetry I.O. website, you know, they're, they're… Okay. OpenTelemetry is now a graduated CNCF project, so… So that… I guess that's a good thing, right?
**Jim Porell** 16:18 Yeah, yeah, yeah.
And I gotta be honest, I love Antoine's energy, because…
**Greg Shriver** 16:24 Oh, me too.
**Jim Porell** 16:25 He's gonna make a difference here, and… You know, and really… You know, being a force behind getting this stuff Agreed to.
We, we've…
**Greg Shriver** 16:35 I agree.
**Jim Porell** 16:37 We've been going too slow, without a doubt.
**Greg Shriver** 16:40 No, you're right. You're right, and, you know, we have been. We have been. And the fact that, you know… I mean, it was funny when I made some comment to him, and he said, well, you're talking to the wrong guy because I'm impatient, and I'm like, you know, that's a good thing.
**Jim Porell** 16:56 That's what we need, yeah, that's what we need.
**Greg Shriver** 16:57 We need… we need a little impatience, you know? So, yeah.
**Jim Porell** 17:01 Yep.
All good.
**Greg Shriver** 17:04 Alright, cool, Jim.
**Jim Porell** 17:06 I realize I wasn't on video about all this time, but I… Oh, that's fine.
**Greg Shriver** 17:11 Hey.
**Jim Porell** 17:11 Yeah, all good.
Alrighty.
**Greg Shriver** 17:13 Okay.
**Jim Porell** 17:15 We'll talk to you next week, then.
**Greg Shriver** 17:16 Yep, talk to you next week. See ya. Bye-bye.
