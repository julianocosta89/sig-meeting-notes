SIG: OpenTelemetry on Mainframes Weekly Sync
Date: 2026-10-07
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Rüdiger Schulze (International Business Machines Corporation)** 01:27 Hi, Jim.
Good to see you.
**Jim Porell (Rocket Software, Inc.)** 01:43 I'm talking away and I'm on mute. Sorry.
**Rüdiger Schulze (International Business Machines Corporation)** 01:45 Okay. Hey there. Hey, Jim.
**Jim Porell (Rocket Software, Inc.)** 01:49 Yeah, driving with the kids again.
We're waiting for them.
**Rüdiger Schulze (International Business Machines Corporation)** 01:53 Yeah, right, yeah, I'm sitting again in the car. They are at the soccer training, so…
**Jim Porell (Rocket Software, Inc.)** 01:58 Oh, okay, good.
**Rüdiger Schulze (International Business Machines Corporation)** 02:00 Yeah, and so at the bottom of the hour, I have a hard stop today.
**Jim Porell (Rocket Software, Inc.)** 02:06 problem.
Okay.
**Rüdiger Schulze (International Business Machines Corporation)** 02:14 Yeah, so let's see who else we're joining to. I think Antoine did a good job promoting our work.
**Jim Porell (Rocket Software, Inc.)** 02:22 Oh, good.
**Rüdiger Schulze (International Business Machines Corporation)** 02:23 And… Yeah, let's talk about a couple of things today.
**Jim Porell (Rocket Software, Inc.)** 02:30 Okay.
Jot down camera since.
We get the benefit of just hanging out in my house.
Are you seeing my video?
**Rüdiger Schulze (International Business Machines Corporation)** 02:55 I see your video. Yeah. I see your good quality today.
**Jim Porell (Rocket Software, Inc.)** 03:01 Yeah.
That's just weird.
It's one of those things I want to see myself, but it's not allowing me to.
Okay.
**Rüdiger Schulze (International Business Machines Corporation)** 03:21 Yeah, so we are two minutes in into the meeting.
Maybe a couple of things, Jim, that I wanted to bring up today.
At Monday, we had a meeting with the Open Mainframe Project about this new project, Opleano.
which is about the OpenTelemetry conform APIs for the mainframe native languages.
And the question that I wanted to ask today to, you know, everybody here on the call is… We are setting up the project, we are setting up the technical committee as part of the Open Mainframe project.
And I just wanted to ask if there's an interest to join the committee.
The idea is to kick this off in November.
And not necessarily needs to be you, but maybe somebody from your company.
**Jim Porell (Rocket Software, Inc.)** 04:20 Isn't that the one, though, that was already on that? I don't know why.
**Rüdiger Schulze (International Business Machines Corporation)** 04:24 Yeah, right. You've been on that. Yeah.
**Jim Porell (Rocket Software, Inc.)** 04:27 Yeah.
**Rüdiger Schulze (International Business Machines Corporation)** 04:28 Yeah, I will appreciate if you join that.
**Jim Porell (Rocket Software, Inc.)** 04:31 Oh, yeah, not a problem. I'm just… did you guys… did you have a private meeting with them or something, or was it an open meeting?
**Rüdiger Schulze (International Business Machines Corporation)** 04:37 Yeah, this was really a private meeting, just to get things organized, you know?
**Jim Porell (Rocket Software, Inc.)** 04:41 No worries.
**Rüdiger Schulze (International Business Machines Corporation)** 04:42 Things like, you know, how do we set up the GitHub repo? How do we do… marketing stuff, right? So, how do we…
**Jim Porell (Rocket Software, Inc.)** 04:50 Okay.
**Rüdiger Schulze (International Business Machines Corporation)** 04:51 We get a logo, and obviously, May is in charge, Mayor from the OMP is in charge to help us with this, so it was really about, You know, more administrative questions.
**Jim Porell (Rocket Software, Inc.)** 05:05 Okay.
**Rüdiger Schulze (International Business Machines Corporation)** 05:07 But the real work would start in November, obviously.
**Jim Porell (Rocket Software, Inc.)** 05:12 Okay.
**Rüdiger Schulze (International Business Machines Corporation)** 05:14 Let me repeat this when Matt is on here.
**Jim Porell (Rocket Software, Inc.)** 05:18 Oh, finally. I found the control.
**Rüdiger Schulze (International Business Machines Corporation)** 05:22 Hey, Matt. Hello.
No matter.
Welcome.
I would just repeat what I just said to Jim. So, on Monday, we had a meeting with John Miltich from the Open Mainframe Project.
to kind of, like, talk the logistics for the Opleano project, for… the project which aims to provide OpenTelemetry conform APIs.
We are planning to kick off the technical committee.
in, in November.
And yeah, we are looking for, you know, people who want to join the community.
to, you know, be technical advisors and so on. And, just wanted to mention that here, and then you can, you know, either yourself or somebody from your company, I would make the same request also to Richard and… Any other, obviously, can join there.
**Matt Hogstrom** 06:25 Is there, Have you created a repo and how are you kind of having people connect with the project?
**Rüdiger Schulze (International Business Machines Corporation)** 06:35 Right, yeah, so the repo is there. It's currently empty. There is… I just said it, we discussed of, you know, things like, okay, we need to have a logo for the project, we need to have a website.
And May from the OMP will help us with us setting this up.
And then I think, you know, in November we will be ready to, you know, get more into a working mode where we then can really do things, right?
**Matt Hogstrom** 07:01 Okay.
**Rüdiger Schulze (International Business Machines Corporation)** 07:02 Okay, good.
The other topic, obviously, is semantic conventions for today, and last week, we looked at this kind of, like, big PR, and we discussed two slides around virtualization, and the mainframe entities. I also posted a couple of other documents there. Did you have a chance, maybe, to distribute this, or to get eventually some feedback on that?
**Matt Hogstrom** 07:30 I did, I… I did. I got… I did distribute it to various teams, but, I think, like you just said, it was so voluminous, they kind of got overwhelmed with, like, well… Everything? What are we… what are we doing? And they were, you know, worried about Not worried, processing it, the scope lights and whatnot, so.
honestly, I did review it with, like, the Sysview team and a number of others, but the feedback I got was quite minimal. And so… I don't think that was, you know, approval, it was more of, we don't have time to read all of this, and we didn't really get it, so I tried to… encourage them to do that. I think the one thing they were concerned about was.
I think some of the potential conflicts between the HMC and COS, and really consistency as we go forward, so… That's all I have. I don't I don't curious.
You know, I guess, from your perspective, Jim, what did you get on your side?
**Jim Porell (Rocket Software, Inc.)** 08:29 To be honest with you, I did nothing, so I gotta… I'm taking notes, I gotta go do that.
**Matt Hogstrom** 08:37 So, actually, what I did… I was doing this morning, Rudiger, is I was cloning the PR, so I could start making some comments in it.
Back to you. And I think you, you had cloned the, the, the actual repo and you're running out of your personal one.
**Rüdiger Schulze (International Business Machines Corporation)** 08:53 Right, yeah, so it's a clone, and I think it's… Not actually sure if the community is working much with branches. That's at least the way I'm used to, or I'm aware of how the community is running this.
And you can comment on the PR, and then… You know, we can process this from there.
Yeah. So, I think what I take from this is, We kind of, like, keep what we said the last week. We keep the PR for the moment as is.
And, and once there are initial comments and we, and we kind of like have clarity, we can split it up into more small granular PRs.
We then can, you know, for instance, look at specific attributes or specific metrics in a more… Defined way.
**Matt Hogstrom** 09:44 I was, I talked to Greg. I guess the way to manage the EZCLA and get connected with the repo is to do a commit.
And then open a PR for it, and I think it'll fail because there's no easy CLA for my ID.
Did you have something you would what error you'd like me to just want me to create a I'm committing something, or do you want me to just update the contributors MD and replace Greg's name with mine for Broadcom?
**Rüdiger Schulze (International Business Machines Corporation)** 10:12 So let me validate a few things, and I'm actually not sure if this ever completed. Did you actually… this issue to make yourself part of the… OpenTelemetry project, did this complete?
**Matt Hogstrom** 10:29 I think that's done, but I will go back. It's been a while.
**Rüdiger Schulze (International Business Machines Corporation)** 10:34 Okay, if this is done, I should be actually able to… to update the maintainer and approval lists. Let me check that later on.
**Matt Hogstrom** 10:44 Yeah, but I think it may not be done, because I think it was the same issue as, like, hey, create an issue and,
**Rüdiger Schulze (International Business Machines Corporation)** 10:51 Okay.
**Matt Hogstrom** 10:51 submit something, and then somebody gets to approve it, so I'm not… that was the process, it was a little confusing to me. I'll tell you what, let me follow back with Greg today. Okay. And I'll make sure I just get what I need done, and I'll… I'll send you an email, and we'll just sort that out.
**Rüdiger Schulze (International Business Machines Corporation)** 11:05 Yeah, and as soon as you are part of the organization, I can actually add you to the lists.
Okay, good.
I mean, in terms of.
You can just make it… I mean, there's already some minimal content in this repo. Just add a sentence to the README or something.
**Matt Hogstrom** 11:29 I was just going to do that in the contributor if you want to replace Greg with me and then.
**Rüdiger Schulze (International Business Machines Corporation)** 11:32 Yeah, right, yeah. And then it goes, you know, the regular approval way, and then we can process it. Okay. I'll do that this afternoon. Yeah, about the CLA, I suppose Greg went through this.
**Jim Porell (Rocket Software, Inc.)** 11:48 you.
**Rüdiger Schulze (International Business Machines Corporation)** 11:49 The.
In our company, there's a certain process for…
**Matt Hogstrom** 11:55 Yeah, we have the same.
**Rüdiger Schulze (International Business Machines Corporation)** 11:56 You probably have the same, just wanted to mention that.
**Matt Hogstrom** 11:59 Yeah, in fact, well, Greg has already taken care of it on our side, so there's the approval there, so that will flow through from a Broadcom perspective.
**Rüdiger Schulze (International Business Machines Corporation)** 12:07 Okay, good. Alright. Then I would suggest, you know, we come back next week, maybe with a little bit more feedback on this. Yeah. And, yeah, let's re-evaluate how we progress then. We can also split this up, it's not, you know, much, but I think right now it's probably better to… Just have an initial start, and then we can split it up when we're ready.
**Matt Hogstrom** 12:29 Yeah, okay, that sounds good.
**Rüdiger Schulze (International Business Machines Corporation)** 12:32 Okay.
Good. Then yeah, I think everybody gets back sometime. Thank you.
**Matt Hogstrom** 12:39 Okay.
**Jim Porell (Rocket Software, Inc.)** 12:40 Yeah.
**Matt Hogstrom** 12:41 See you later, John.
**Jim Porell (Rocket Software, Inc.)** 12:42 Thank you. See you guys. Bye.
