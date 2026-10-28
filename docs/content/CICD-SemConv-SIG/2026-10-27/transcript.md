SIG: CI/CD SemConv SIG
Date: 2026-10-27
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Robert Pająk (Splunk Inc.)** 01:41 I was muted, hello!
**Christophe Kamphaus** 01:43 Hello, can you hear me?
You're thinking?
**Robert Pająk (Splunk Inc.)** 01:45 How are you?
**Christophe Kamphaus** 01:46 Fine, aren't you?
**Robert Pająk (Splunk Inc.)** 01:49 Good.
I need to run, like, in 15 minutes on my daughters.
But I guess, that will be probably… will end, like, probably even sooner.
**Christophe Kamphaus** 02:00 Yeah, I saw that Adriel had some points he wanted to discuss.
I don't have anything from my side.
**Robert Pająk (Splunk Inc.)** 02:09 I have only one thing, I just try to find this igniting nose.
To add it for transparency.
Excuse me.
Sure.
Okay, Castle 27… Okay, I, I think… 27… Deuce.
Can you see? Am I editing the correct document?
**Christophe Kamphaus** 02:51 Yep, I can see you.
**Robert Pająk (Splunk Inc.)** 02:53 Right?
So I have only one.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 03:02 Good day.
**Christophe Kamphaus** 03:05 Hello, how are you?
**Robert Pająk (Splunk Inc.)** 03:07 Hello.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 03:07 Okay, how are y'all?
**Christophe Kamphaus** 03:10 Yep, point.
For me, it's an hour earlier than usual, because we have now the Winter time in Europe, but not yet in the US.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 03:23 Gotcha. Okay.
**Robert Pająk (Splunk Inc.)** 03:25 Yeah, that's also what I thought, what's wrong with the calendar? Because I usually go for my kids, and then I start joining the meetings. You're right, it's wonderful.
**Christophe Kamphaus** 03:37 No, that's so great.
**Robert Pająk (Splunk Inc.)** 03:37 Yep.
**Christophe Kamphaus** 03:38 one… one week, where this happens in ornament, I think it's two weeks in spring.
**Robert Pająk (Splunk Inc.)** 03:46 it's a chance that I have so much memory that I need always to look at the calendar, because if I know these hours by heart, then I'll probably skip this meeting.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 04:00 I think ours… we're gonna fall back here soon, and go back an hour.
I just wish time would stay the same.
**Robert Pająk (Splunk Inc.)** 04:12 That's true.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 04:14 I like your shirt, by the way, Robert.
**Robert Pająk (Splunk Inc.)** 04:17 Excuse me?
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 04:18 I like your shirt.
Grogu.
**Robert Pająk (Splunk Inc.)** 04:20 I can… yes, I can share my screen, if you want.
**Christophe Kamphaus** 04:23 Yep, go ahead.
**Robert Pająk (Splunk Inc.)** 04:27 Desktop.
Can you see my screen?
**Christophe Kamphaus** 04:31 Yes?
**Robert Pająk (Splunk Inc.)** 04:32 Adriel, do you want to add something?
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 04:35 Yeah, I probably could… could do that.
**Robert Pająk (Splunk Inc.)** 04:39 Okay.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 04:40 Guess I can follow the instructions.
**Robert Pająk (Splunk Inc.)** 04:42 Okay.
So… Mine will be probably within 2 minutes.
Okay, just… It's just about… stabilizing and VAR propagation discourage this document. 2nd of November is coming next week.
So, oh, right now, Codex created a draft PR.
Yeah, so… Yeah, this will be ready for review.
I'll just put it in the docs.
So, I don't know, during the meeting or after, you can just look at this.
Indeed.
It's here.
And, yeah. And that's all from my side, I think. There's also other thing. I remembered, the thing which Carlos was working on regarding this, long-living trace pants and adding this semantic conventions.
I start thinking about just asking Carlos if he still is pursuing this issue, or if I should take over him.
But probably I will start not sooner than in December, just my guess, but I think that that might be my next milestone for CAP that I may be pursuing, especially that during I'm not sure if in Prague, but for sure in Warsaw, when in cloud-native days, people were telling me that they have some very long, long, long-running spans, and it's an issue that they do not have any feedback when it's in process, and they just would like to know that some span has started.
So, yeah.
that's the background that even people are approaching me and telling about this issue in different conferences, so I think it's kind of important.
**Christophe Kamphaus** 06:42 Yeah, I was also thinking about that, if I could lend a hand on that topic.
**Robert Pająk (Splunk Inc.)** 06:48 For sure, I will need help even schematic conventions in the repo, you know, and also, you know, review, paralyze, etc.
**Christophe Kamphaus** 06:56 Or some prototypes, yeah.
**Robert Pająk (Splunk Inc.)** 06:59 Maybe prototypes, if you have some time, maybe for Python it will be easier. I do not know, I wanted to do it in Go, right now, If I remember correctly, the issue is that we are lacking a hook.
when something… I don't know if it's starting or ending, I do… I think when it's starting, I think we miss this hook that we can, you know, jump into using a processor.
So… Yeah.
**Christophe Kamphaus** 07:29 It could all… Also be, if I remember right, so hook if an attribute changed, Oh, can you hear me?
**Robert Pająk (Splunk Inc.)** 07:39 Yeah.
Yes, that right now, I can tell.
**Christophe Kamphaus** 07:43 If I remember right.
**Robert Pająk (Splunk Inc.)** 07:44 heard you before.
**Christophe Kamphaus** 07:45 Mmm.
Okay, but I was saying, if I remember right, there was a hook missing for on update of attributes.
But it could also be for the state.
**Robert Pająk (Splunk Inc.)** 07:58 Mjeev.
I think for… first initial version.
it might be good enough just to have a hook or start and end, because even if there's something in the middle, then maybe we'll just, you know… I think, like, the feedback I got right now is that many the problem is that they want to know that something started.
So I think that even information that, you know, something started with some attributes, even if it's modified in the middle, I think as long as we get the same output in the end span.
You know, as…
**Christophe Kamphaus** 08:35 with…
**Robert Pająk (Splunk Inc.)** 08:36 finishes, I think it could be good enough for the initial version, or the version.
**Christophe Kamphaus** 08:40 That it's… and that it's still in progress.
**Robert Pająk (Splunk Inc.)** 08:44 Excuse me?
**Christophe Kamphaus** 08:45 And said it is still in progress.
**Robert Pająk (Splunk Inc.)** 08:47 Yes, yeah.
It's not ideal, but at least it's something.
**Christophe Kamphaus** 08:53 Yeah, agreed.
**Robert Pająk (Splunk Inc.)** 08:56 Yeah, do you want me Adriel to still share, or do you want to share?
Yours?
**Christophe Kamphaus** 09:03 I'm not on my usual PC, so I cannot share at the moment.
**Robert Pająk (Splunk Inc.)** 09:10 Adriel, do you want me to share, or do you want to share?
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 09:13 We don't miss here, it's… it's fun.
The only two things that I had were, the DC elections. The link is in the thing. They close tomorrow, so the, Or we're asked to remind folks about that?
And then I started working on some pull requests to add instrumentation to the PR dashboard stuff. I don't have the pull request up yet, I'm working on the code, but, going to… We still have that. I need to respond to some of the comments on the… on the dock, for how we're gonna proceed long-term, but I figured I'm gonna go ahead and add the instrumentation and get the key things up and running so that we can have something, in time for… for when you need it. Which is, what date does QCon again?
**Robert Pająk (Splunk Inc.)** 10:02 November, like, middle, or 10?
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 10:05 Okay, alright.
**Robert Pająk (Splunk Inc.)** 10:06 Cool.
**Christophe Kamphaus** 10:07 And so that's pretty soon.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 10:10 Yes, yeah, yeah.
Yes, that's…
**Robert Pająk (Splunk Inc.)** 10:12 I've never…
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 10:14 It's not November 2nd, right?
Alright.
**Robert Pająk (Splunk Inc.)** 10:17 Second is your stability, so you can announce it if you want, at KubeCon, that environmental carriers are stable.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 10:24 Got you, yeah. Alright, I'm gonna try… I have been, out of pocket for a hot minute, so, I'm gonna focus on this this week.
Try to get as much done as possible. Hopefully, we can actually have it… have it working by end of week.
But, yeah, I just want to let you know that I've started opening, or writing, getting the code prepared for that, so…
**Robert Pająk (Splunk Inc.)** 10:50 Awesome.
**Christophe Kamphaus** 10:53 Yep.
**Robert Pająk (Splunk Inc.)** 10:56 This is the end of the written agenda.
Do you think… do we have anything else to discuss?
So…
**Christophe Kamphaus** 11:03 So the documents, the pulley request to Mark.
environment variable propagation as stable, it's pretty much just the two lines, the changelog entry and see Changing of the status, right?
**Robert Pająk (Splunk Inc.)** 11:16 Yep, correct.
**Christophe Kamphaus** 11:17 Okay.
**Robert Pająk (Splunk Inc.)** 11:18 I Yep.
I'll just remove the validation.
**Christophe Kamphaus** 11:27 Yeah, it's a pity that Rust hasn't, done anything on the PR yet.
**Robert Pająk (Splunk Inc.)** 11:33 Yeah.
**Christophe Kamphaus** 11:34 But I guess they will have to do it after it's marked as stable sand.
**Robert Pająk (Splunk Inc.)** 11:40 Maybe, you never know. I have a feeling for some time that even though we have AI, we just… We have a shortage of maintainers and people who have time working on maintaining our.
post doors.
**Christophe Kamphaus** 11:56 Yep.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 11:59 Yep.
That's true.
**Christophe Kamphaus** 12:05 From my site, okay, yeah, I remember right now. I created an issue two weeks ago.
I put it on the board, it's about defining spans for CICD run phases.
That should then also map pending, executing, finalizing of the metrics.
I will, I will put a link on the agenda.
**Robert Pająk (Splunk Inc.)** 12:34 Awesome.
**Christophe Kamphaus** 12:35 So it's just, if you want to… Comment on it, feel free.
it came up in some discussions, that's why I created it.
**Robert Pająk (Splunk Inc.)** 13:09 Quick question… CAD run phases.
These are for pipelines, or tasks, or for anything.
Or it's just a kind of, you use it where you want?
**Christophe Kamphaus** 13:35 Yeah, it's, you can use it for… Pipelines, or for tasks?
**Robert Pająk (Splunk Inc.)** 13:41 process as well, okay. Because you… it's written only phases in CAD high frame run duration metric, but I think it can measure.
**Christophe Kamphaus** 13:48 Yay!
**Robert Pająk (Splunk Inc.)** 13:49 to use it in tasks.
**Christophe Kamphaus** 13:50 Exactly, that's where it came from. The question came up there.
And I did some search where we used similar things before, and that was only in the pipeline duration.
That's why I mentioned that.
But it should also be for tasks.
**Robert Pająk (Splunk Inc.)** 14:08 Okay, so that's my only feedback.
For now.
Okay, I think we can end here.
And I go in for my daughters. See you!
**Christophe Kamphaus** 14:23 See you.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 14:24 Dude.
**Christophe Kamphaus** 14:25 But…
