SIG: CI/CD SemConv SIG
Date: 2026-05-12
Duration: 20 minutes
============================================================

## Zoom Recording Transcript

**Alan Clucas** 04:29 Morning!
**Adriel Perkins** 04:31 Hey, good day, how are you?
**Alan Clucas** 04:33 Alright.
Yay.
**Adriel Perkins** 04:36 Good.
Good, good, good, thank you.
Living the dream.
Way behind, though. Way behind. Always.
Just always too much stuff to do, man.
**Alan Clucas** 05:02 Yeah.
**Christophe Kamphaus** 05:05 Hello.
**Adriel Perkins** 05:06 Whoa.
Give everyone a minute to… Pop in some notes.
Go ahead and open the board.
And share the screen.
And I don't know why this is looking weird… Maybe it's just me.
Or maybe GitHub's broken again, I don't know.
I have not reached out to… Carlos, on this one, I need to… Make sure I do that. That was the action item I forgot to pick up from last time. I was traveling.
So… Last week was a wash for me.
I oughta put this down. I forgot about it.
A lot of people are still working on this. There's also a stabilization matrix now that's been put into the spec.
I think .NET has already been merged in as well, maybe?
But lots of folks are working on that, so it's awesome.
Yeah.NET's been done.
So I really think that leaves, like, Rust to JavaScript.
Maybe PHP and Erlay.
But good progress there.
Yeah, this is the compliance update.
For the compliance matrix.
Don't know how to actually see it.
Excuse me. Sorry for yawning.
So, crazy.
There we go, that's the compliance matrix.
Eyes are struggling to read, though, this morning.
Oh, maybe it's further down?
**Christophe Kamphaus** 09:10 Do they track all spec, Across all SDKs here.
And then, AntFARS is one line on it. Is that it?
**Adriel Perkins** 09:22 Oh, here we go. Yeah, okay, so… Environment variables as context propagators, yeah, they track a ton of stuff.
So go Java!
I think, and see… and .NET.
So… that was the change for this one. Looks like… I don't know if C++… I thought C++ was already… there, but… We'll check… I can probably take an action item, check Python and C++.
**Christophe Kamphaus** 09:53 there was, the change that, was done in the spec to simplify it and make it clearer.
**Adriel Perkins** 10:02 Yeah, good.
And I don't know that… I haven't looked at Python since we changed the spec, so… We can definitely… Check that.
Bye.
there was somebody who commented on this one.
I sent them your way, Kristoff, so I tagged you in it. Hopefully they'll reach out on Slack, but they were interested in picking this up, just someone from the community, so… I sent them your way, because I think you have the most experience with Context on this one.
And I think you've done a lot of supporting work for that. Yeah.
**Christophe Kamphaus** 11:10 It's, it's just, it's my old GitHub handle, so I didn't get the notification.
**Adriel Perkins** 11:16 Hmm.
Got it, okay.
Where did I go?
Oh, I shouldn't.
**Christophe Kamphaus** 11:26 Just compose.
**Adriel Perkins** 11:31 There we go.
Updated Sorry about that.
**Christophe Kamphaus** 11:38 No problem.
**Adriel Perkins** 11:42 Yeah, I think that's pretty much everything on the board. Does anyone have anything they want to chat about?
**Christophe Kamphaus** 11:55 How's the… Go ahead.
**Carlos Alberto Cortez** 11:58 No, you… you go. Huh, you over.
**Christophe Kamphaus** 12:01 Yeah, for me, it's very quick. Quick status update for Jenkins implementing the hotel.
Some conf… my PR is still open, and it's waiting for reviews. They had some turnover on, onboarding a new maintainer, so that's, ongoing, and I hopefully, as soon as he's ready, he will review my PR.
And thanks, Totan, for reaching out to him.
**Dotan Horovits** 12:29 Yeah, I wanted to, so I pinged him on the… just to compliment on that, so I pinged him on GitHub, and then on some other channels, just to make sure… I assume that he's probably, overflowing with the new role, so just wanted to make sure that we're on his radar.
Anyway, just let me know if he reaches out to you directly so I can back off. If not, then I will make sure that he has us In mind for the priority queue that he's managing, and .
**Christophe Kamphaus** 12:58 do.
**Dotan Horovits** 12:59 I was looking for him on on CNCF Slack, I wanted to add him to the group chat we had with the other maintainers, but I couldn't find him, so I don't know if he's not there or just missed him, but I… one of the other things I want is, as soon as he gets back to me, is to see if he's there, and then I can also look him on the Slack channel, because this… First, we'll give him all the context there on the discussion from the previous maintainers, and So anyway, just, here to support.
**Christophe Kamphaus** 13:27 All good, thanks.
**Adriel Perkins** 13:34 Cool, thank you for the update. Anything else?
**Carlos Alberto Cortez** 13:39 So, yeah, basically, I am still working on the lifecycle processor and expanding the spam processors part. I haven't… I have two prototypes now for that.
I am working in the specification part, which is the remaining one, before I can discuss that with the group. But one thing to point out is that, as you know, the way I'm doing this is that the spam processor interface at the SDK level.
We'll be adding either one or three more, operations for reporting first step.
This fund name has changed.
Second, that you were, like, a link was added.
And third, that an attribute was set.
if you set multiple attributes, you get one event per attribute. So, the only thing that is interesting here, and probably it's not a problem for anybody here, but in case you have some opinion, is that those… well, that's one way. The other one is that you have an unchanged genetic method that just lets you know what changed. Anyway, the thing is that, You… when you get this event at the spam processor level, you will only get a riddle of spam.
Which means that you cannot touch this panel.
The reason is that we don't want circular, you know, recursive situations. Like, you set that attribute, you get an onset attribute event, and then from that event, you set another attribute.
I think that would complicate things too much. For our very own purposes, I think it should be fine. But yeah, other than that, just working on that.
The prototypes themselves are very simple, you know?
**Adriel Perkins** 15:18 Sure.
I… I was mentioning earlier that I know I was supposed to reach out to you offline, and Josh and I, was traveling last week, so I did not do that, but I will. I put that back on my to-do list to make sure that I do it, so I'll be reaching out. Sorry for the delay on that one.
**Carlos Alberto Cortez** 15:34 Yeah, actually, that's complementary. That's on the OTLPM map, right? So that's a parallel effort, yeah.
**Adriel Perkins** 15:48 Cool. Anything else?
**Dotan Horovits** 15:52 I just want to ask quickly if there's any… I know we discussed in the previous meetings about the, like.
The path to, to, graduating it, like, But wondering, if we have any specific, action items, on that side, and if I can help with anything.
And sorry for missing the last meeting, so if it's been discussed, apologies.
**Adriel Perkins** 16:22 Yeah, there's, some items that have been created on the board for stabilizing of specific attributes, like, and conventions. That's where we're working towards stable by default, which is, I think, the larger initiative across, OTEL to stabilize things.
Those are… it's not stabilizing everything that we've created, but it is stabilizing things that have been around for a while, so those are the work items that we have for that.
Does that answer the question?
**Dotan Horovits** 16:51 Yeah, it's… and I've reviewed the board, so this looks good, first of all, scoping, because I know that some discussions wanted to take it way, way broader, broader maybe than even just CICD workflows. I'm glad that we're scoping it well, so we can really strive to stabilize, but Beyond the… these is, like, non-technical aspects that we need to, move with the, with the TOC, or with, I don't know, with the SIG, or whatnot to, to make sure that they have the, whatever they need to, to sign off on that, or is that just, these items? Just making sure that, if there's anything else that, That I might have missed.
**Adriel Perkins** 17:36 Yeah, I mean, I think there's still, like, more stuff to do, for sure, than just here, but these are the main critical ones that we feel are ready to work towards stabilization for for during this phase.
**Dotan Horovits** 17:50 Okay, sounds good.
**Adriel Perkins** 17:52 But if you think of something else, for sure, feel free to put it on there.
**Dotan Horovits** 17:56 Yeah, no, nothing that comes to mind, I don't know. Christophe, I know that you had a chat with them in person, so I don't know if anything else came on that discussion, or in any other channel, just to make sure.
**Christophe Kamphaus** 18:05 No, everyone I talked with, the message was basically, it's been around a while, it looks like there haven't been any major changes on it, so yeah, let's make it RC.
**Dotan Horovits** 18:17 Nice.
Thanks.
**Christophe Kamphaus** 18:23 And yeah, Adriel, there was an open question about, a corresponding See, duration metric… And, span someconf.
Right.
So…
**Adriel Perkins** 18:40 Was that a question from, the Semantic Conventions worker?
**Christophe Kamphaus** 18:43 No, you mentioned it a few meetings ago.
So, because of that, I didn't want to open a PR yet.
**Adriel Perkins** 18:55 Oh, are you talking about the queue and ZEX fans?
**Christophe Kamphaus** 18:58 Yes.
**Adriel Perkins** 18:59 Yeah, so I was supposed to do that last week, but I was traveling, so I didn't do it. I will open that issue this week, for sure.
With all the, condensed information from the community.
I put that back on the to-do list, so I moved that up here.
Just to make sure that I'm not losing it and keeping track of it.
**Christophe Kamphaus** 19:21 Yeah. If you want, I can prepare PRs to mark CR server.
Some confos RC.
**Adriel Perkins** 19:32 Sure.
**Christophe Kamphaus** 19:36 On white, I'll do that.
**Adriel Perkins** 19:46 Awesome. Thank you.
Anything else?
Give 45 minutes back to your day.
Awesome. Thank you all for coming, and I look forward to seeing you next week, and we'll talk offline.
**Dotan Horovits** 20:01 Thanks, everyone, have a good day.
