SIG: Community Demo App SIG
Date: 2026-11-25
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 00:40 Hey, how's it going?
**Srinjoy M** 00:46 Hi, yeah.
It's fine.
What about you?
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 00:57 Doing well, thanks.
**Srinjoy M** 01:01 Wait.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 01:08 We'll give everyone a minute to join.
I don't know if we've met, I… have you joined these calls before?
I haven't been out in a few weeks.
**Srinjoy M** 02:08 Oh, no, it's actually my first time, like, I'm a pretty new contributor to this.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 02:14 Oh, welcome.
**Srinjoy M** 02:16 Yeah, thanks.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 02:19 I just became an approver, this week.
So, Usually Juliano can join, who's one of the maintainers, but… I know he can't join today, I don't know if anyone else will join.
**Srinjoy M** 02:37 Okay.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 02:44 How's it been contributing so far?
**Srinjoy M** 02:48 I haven't actually contributed, like, I opened an issue that I personally faced.
Right.
Yeah, I'll start contributing after this. Actually, I requested, if I could contribute, and… I think Juliano, yeah, I think he said yes, so… Like, I'd been looking into it, and… from… from, like, this week. This week, I hope I can… Contribute, yeah.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 03:18 Great.
I'll be on the lookout for any PRs, if you want to put one in.
**Srinjoy M** 03:28 Yeah, great.
Is this the same time every week, or is it, like, rotating with time?
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 04:00 No, it's the same time every week.
**Srinjoy M** 04:04 Okay.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 04:05 Looks like someone else is joining… Hi, welcome.
Is it song?
Welcome. Can you hear us? Or can you hear me?
**Som Banerjee** 04:29 Oops, sorry, I…
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 04:31 No worries.
**Som Banerjee** 04:33 Hi, Matthew.
I Srinjoy…
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 04:40 How are ya?
**Srinjoy M** 04:41 Alright.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 04:47 haven't really gotten, good attendance today so far, so I think we might have to, Call the meeting, unless you had something to… to bring up.
**Shenoy Pratik** 04:57 iPhone.
I shouldn't know.
**Som Banerjee** 05:00 Hey, Pratik.
**Shenoy Pratik** 05:03 Sorry for joining late, I had.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 05:04 Oh, hey, Shaman.
**Shenoy Pratik** 05:05 Another meeting going on, yeah.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 05:08 No worries.
**Som Banerjee** 05:10 Yeah, I got late to it, too.
**Shenoy Pratik** 05:15 How's it going?
Doing good. Let me just start the mid, recording stuff, and then… Adding things here in the agenda.
Yep.
Do you guys have any agenda to start with? I don't have any. I'll just do the regular PR edging, if… Anyone has something?
I know, Som, you mentioned that, you would have some… PRs up for the issues that you raised last meeting.
**Som Banerjee** 05:50 Yeah, that's right. So, Juliano, was able to get to it, and I think it's been merged.
**Shenoy Pratik** 06:01 Awesome.
**Som Banerjee** 06:03 did check that he approved it, I didn't see whether he finally charged it.
But I think it's gone through.
**Shenoy Pratik** 06:10 I see one, PR for the repair the card and checkout tools part. Merge them.
**Som Banerjee** 06:18 That's right, yeah. So that was a lot.
**Shenoy Pratik** 06:23 Perfect.
You know…
**Som Banerjee** 06:26 I did put in a couple of, new issues, One of them, I happen to be working on a fork of the ripple.
The fork was, pinned to an older release.
And what I, what I thought is that the, The images that are pulled, tend to get stuck on latest. They… they don't pull the images, concurrent with the record.
So… so, sorry, with the… with the release stack.
So I, raised an issue, and I was hoping to… Talk through possible solutions, and probably work on one that we agree on.
Wayne.
**Shenoy Pratik** 07:23 C.
So you're saying, if you download a particular release zip, the composite still contains, the latest image.
Pull.
And that's an issue.
**Som Banerjee** 07:38 The Compose, the Compose tries to pull later still, yes.
Yes.
**Shenoy Pratik** 07:47 I see.
That makes sense. I've been trying to remember how we actually… request users to consume. Yeah. Do you have an issue for this as well?
**Som Banerjee** 08:01 It's 4386.
**Shenoy Pratik** 08:06 Okay.
**Som Banerjee** 08:07 No, sorry, sorry about that, no.
Poultry itself.
**Shenoy Pratik** 08:25 A good point.
I haven't checked it myself. What I usually do is go with the Helm chart.
Deploy it on Kubernetes.
But, yeah, if someone pulls a latest to release, then my… Latest image with the older release, it might be a problem, because code might have drifted.
**Som Banerjee** 08:48 L.
Yeah, I think that all remains fine if you're pulling main.
On, on latest, but yeah.
**Shenoy Pratik** 09:05 Yep. Got it.
Awesome.
Any other issues that you found out while you were going through the demos?
**Som Banerjee** 09:18 Not an… not an issue, but I was, I, I, I, I… Couldn't really find a very nice place to, to keep secrets.
So, so let's say, I'm… I don't want to use the VCR cassettes.
And I want to actually, run an LLM, where do I keep the secrets? Suppose I'm connecting to a backend that needs, credentials.
Where do I keep the secrets?
So… I was, Thinking of a pattern of… get ignored.
and secrets, files.
**Shenoy Pratik** 10:17 We have a .env file today.
But…
**Som Banerjee** 10:21 But that's… that's…
**Shenoy Pratik** 10:22 recommended in broad. Yeah, but if you change something, or… there is another one for .env.override.
**Som Banerjee** 10:32 Right? But that's just.
**Shenoy Pratik** 10:33 So you can use… you can use the override one.
And then keep changes there. Let me check if it is part of Gitignore or not.
Usually, overrides are part of getting. If not, you can just do it locally.
And you're getting node.
**Som Banerjee** 10:49 Right, right, yeah. I mean, of course, I… I do have a local way of doing it. I mean, I tend to add it to Git info exclude.
But the trouble is, you know, it stays local, number one.
If, if, if someone doesn't deliberately add it to exclude?
They might end up pushing it.
**Shenoy Pratik** 11:23 Yeah, so usually… For demo, we clearly mentioned this is not a production environment. If you are using production environment, you should go with Docker Secrets, or if you're using… I'll try to use Kubernetes secrets.
That's our point of view.
Yeah, Demo is not something that you put in as is in production.
But if you're developing something, you can have your local overrides, and… That should be good enough. I don't need to separate.
Flow on the demo for this.
change.
**Som Banerjee** 12:02 Okay, yeah, yeah, that's fair.
**Shenoy Pratik** 12:04 Let me know if, like, differ a lot of… Has something very pressing that will benefit all of the downstream consumers of the demo.
**Som Banerjee** 12:18 No, I mean, this is definitely something that, can be worked around, locally.
Plus, yeah.
**Shenoy Pratik** 12:36 Awesome.
Matt, did you have any questions or agenda items for today?
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 12:44 No, I… other than the, did you see the project I made in my own GitHub account with the issues and the recommendations?
**Shenoy Pratik** 12:51 No, I didn't get… Have you raised it somewhere, and any of the issues, or…
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 12:57 Let me… I've been commenting on issues and just trying to close ones that… are not needed, but the… the board that I created is basically with, like.
decision points. Just trying to trim back the number of issues we have and, like, address them, so… If you could just review that, that'd be great. It's a message I sent in the Hotel Community Demo Slack channel.
**Shenoy Pratik** 13:26 Okay.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 13:27 The ultimate goal there was to set up a backlog, so we could, you know, triage backlog items for people to work on.
**Shenoy Pratik** 13:40 Yeah, that would be interesting.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 13:42 It was Giuliano's idea, actually. I was just, you know, going through the… like, some of the issues were super old and needed to be, closed and all that, so, like, that was what I was trying to sift through, but, yeah, be curious on your take on… on that.
**Shenoy Pratik** 13:58 Yeah, I'm just looking through it.
Oh, are these all the issues that are there?
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 14:06 As of a few days ago, yeah, I've been, like, trying to keep it in sync.
**Shenoy Pratik** 14:11 It's super cool.
I think we can start using this as a triaging code as well, and then move it to the hotel.
I was gonna say, we have to move.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 14:23 Cause it's in… yeah, it's in my, But it was just the fastest way to get started was to move it into my… and then maybe we run a job that… Updates it.
**Shenoy Pratik** 14:33 Yeah.
We can also, I'm just adding some notes.
I have a few questions right here.
I didn't go through the Slack message, sorry for that.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 15:01 Oh, that's fine.
**Shenoy Pratik** 15:02 Yeah, but do we want to remove the stale Issues which are not relevant anymore.
I think we should…
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 15:14 Good, yes.
**Shenoy Pratik** 15:15 I see some stale ideas that you have added in, like, as one of the buckets.
If there are ideas, they're good, because they can still be updated.
But if it's, like, an implemented and done deal thing, we can just close it.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 15:34 Yeah, I commented on those issues, so that might give you more context into those.
**Shenoy Pratik** 15:39 Oh, good.
Okay.
Yeah.
And then we should also start adding some good first issue. Oh yeah, I see already one, And it's,
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 15:52 Oh, that's a good idea.
**Shenoy Pratik** 15:53 Yeah, the 27 line item already has a good first issue, I don't know if we added it or it's already there, but if it's not… They're in the older issues which look like good ideas, we can put our… put them as a good first issue.
And, like.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 16:08 It has it. Yeah, it has that tag, but it looks like there's been PRs for that.
**Shenoy Pratik** 16:19 might be that we need to re-review. Oh yeah, there was one PR recently for this one, the new business metric processor.
No.
So, this guy, Aditya, adds, the Az race, and we merged it.
A few weeks back.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 16:36 Yeah, I mean, my ultimate goal was just to, like, not necessarily get rid of issues, but, like, to categorize what's already there, so that we can start with, like, a cleaner base for a backlog.
But the good first…
**Shenoy Pratik** 16:49 It needs to be healthy. It needs to be healthy, the issue set. It's not, like, removing or cleaning things, but it should be healthy.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 16:55 Yep, exactly.
**Shenoy Pratik** 16:58 Yeah.
What did Juliano say? Like, should we… Get this in, or…
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 17:07 I didn't ask him directly, I asked him if I could be a triager, and he said he made… he added me as an improver, so… I was actually really happy about that.
**Shenoy Pratik** 17:18 Yeah, yeah, like, we can… we can get you in. Are you all.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 17:20 But,
**Shenoy Pratik** 17:21 an hotel member.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 17:23 Yes. I'm already an approver as well, he took care of that for me.
**Shenoy Pratik** 17:27 Oh, okay.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 17:28 But as far as this… this specific board, I think the next item would be, yeah, like, can we move it? So, I'll send a message in Slack then.
Okay.
**Shenoy Pratik** 17:40 Yeah, let me just check. There is a projects, board here I can see inside OpenTelemetry Demo. As an approver, can you look at the projects view?
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 17:50 Let's see… Gotcha… I see one closed project.
**Shenoy Pratik** 18:07 Yes, yes, yes, yes. But do you see the new project button there, on the top?
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 18:10 Yeah.
**Shenoy Pratik** 18:11 Yeah, then I think you have all the permissions to move the project altogether.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 18:17 I got… it says something went wrong, but that looks like a GitHub issue more than… I wouldn't be surprised if something's wrong with GitHub.
**Shenoy Pratik** 18:26 you know, I'm able to open the… older project.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 18:31 I can open the older one, but I get a 500 when I try to open a new project.
**Shenoy Pratik** 18:36 Oh yeah, even I'm getting good.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 18:38 Oh, okay.
**Shenoy Pratik** 18:40 That's super weird.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 18:43 Not really. Oh, they have an ongoing issue.
My database load.
**Shenoy Pratik** 18:52 Okay.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 18:54 I'll try again.
Whatever.
**Shenoy Pratik** 18:55 Yeah, and it's And then get that info.
Because ideally, I've seen some of the SIG and tag meetings, they start with, cries would.
And then this can be our charging board on the project.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 19:11 Yeah.
**Shenoy Pratik** 19:12 And once that is done, we can continue one of the pieces.
That is a really excellent, yeah.
Do you want me to look at the project, or do anything on it, before you move it into the demo, or I think…
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 19:31 If you don't mind, having to look through the issues, just because we can always move everything from my project to the… the demo, like, so if you make changes there, we can just do, like, a one-time cutover, and then I'll delete mine.
**Shenoy Pratik** 19:45 Okay.
Then let me take some time this week, and then get over this part of the border.
I might want to look deeper into the greater than one-year issues, and then try to see if they are still relevant or not.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 20:02 Yeah, that'd be great.
**Shenoy Pratik** 20:05 insight… Srin, hi, nice to meet you.
Want to introduce yourself to the group? I think the other.
**Srinjoy M** 20:17 There's no…
**Shenoy Pratik** 20:18 a bit, but then seeing you for the first time.
**Srinjoy M** 20:21 Yeah, yeah. I'm, I have joined this meeting for the first time, like, for the past one month or so, I think, yeah, I've looked into this project, and I've set it up locally.
And, I'm trying to find issues for which I can contribute to.
And, I think I, I think I can expect, to contribute, this week itself.
Okay.
**Shenoy Pratik** 20:44 But yeah, you're at the right time to join the meeting, because Matt has a collection of issues with good labels.
**Srinjoy M** 20:51 Yeah, I saw…
**Shenoy Pratik** 20:52 So you can start looking into it.
**Srinjoy M** 20:55 Yeah, that was a problem for me, like, because I couldn't find, relevant issues to contribute to. I had to search for the PRs linked to those issues.
**Shenoy Pratik** 21:05 Yes.
**Srinjoy M** 21:05 See if their work had been done on this.
So I think this would help me too.
**Shenoy Pratik** 21:11 Yep.
Let us know once you have any PR, or if you have issues running the demo itself, you know, so… ping me on the CNC of Slack channel, we also have an OpenTelemetry Demo, Slack channel, and, there.
So, yeah, let us know if you have any questions.
**Srinjoy M** 21:32 I think I haven't joined that, right now.
**Shenoy Pratik** 21:37 Yeah, that's how, like, all the conversations happen.
If you are doing a big… In general, like, if you're doing a big feature.
addition, please create an issue for it so we can discuss among ourselves, on the issue, and then maintenance can give you some guidance. If it is a small fix, directly raise a PR, and then we'll review it.
Thank you.
**Srinjoy M** 21:59 Sure.
**Shenoy Pratik** 22:02 Yeah, that's about it. Are you… interested in anything? Like you mentioned, you have been looking through the OpenTelemetry Demo for some time now.
Any particular thing that you're looking into?
**Srinjoy M** 22:14 I, I, mostly I've worked, like, I've looked at the collector part, different delivery.
And, apart from that, mostly it's this project only, like, how the pipelines are built for this project, and it's mostly.
**Shenoy Pratik** 22:26 Correct.
Got it, yeah.
there are some ideas as well that I had, Around how we can integrate with other SIG meetings, and then get some ideas from there.
But yeah, I think once you have a couple of PR, then we can discuss on the next steps and stuff.
Another meter.
**Srinjoy M** 22:48 Sure, sure.
Next week, I'll also join, this…
**Shenoy Pratik** 22:54 Yeah.
**Srinjoy M** 22:57 Sure.
**Shenoy Pratik** 22:57 Hmm.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 22:58 It's the second most forked project, right, Shenai?
**Shenoy Pratik** 23:02 No, it's the most folk project, I believe.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 23:04 the most.
**Shenoy Pratik** 23:05 United.
Yeah.
**Srinjoy M** 23:07 Oh.
Like, in OpenTelemetry, or…
**Shenoy Pratik** 23:11 OpenTelemetry.
**Srinjoy M** 23:14 Oh, yeah.
**Som Banerjee** 23:14 Didn't realize that.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 23:17 Didn't mean to say number two.
**Srinjoy M** 23:21 Okay.
**Som Banerjee** 23:24 Hmm.
**Srinjoy M** 23:26 Yep.
**Shenoy Pratik** 23:27 Awesome.
I think then… I don't have any other agenda items, I'll just do my regular backlog thing, and then go over it.
But yeah.
the journey.
Do you have any questions?
**Som Banerjee** 23:41 One quick thing, so I think last week you mentioned, wanting to take a look at, the Gen AI, telemetry. Did you have any more thoughts on it? Like, you know, what, what What part of, Genai telemetry, where you… Thinking of… Having better instrumented,
**Shenoy Pratik** 24:13 Yeah, so I looked at it. There are a few things around, like, very simple semantic convention thesis. One is the spans itself that the agents are generating. They don't have a conversation ID.
So… That's, like, that's, like, one of the P0s of, OTL GenAI semantic conventions.
If we have that, then we can correlate multiple spans into a particular ID across all their traces.
So… That's something that I would want.
It to be added.
icon to… start on it, but I'm trying to see a holistic list on things. The second part of the thing, I think, the second part of the agent side that we discussed, I think, was around evaluations itself.
So we don't have anything around evaluations, but the GenAI SIG has come with an evaluation result.
Data model, which is… very easy to store in our existing databases, like OpenSearch, and it's already there in the demo.
So we can store these evaluation results there, create a dashboard in Grafana.
And so I'll complete some of the Agentic missing pieces.
So I… I did, like, do a run-through on our current Demo's existing stance, and what does Gen AI isomantic conventions proposed, and then there are some diff items. I'm happy to create a holistic, issue tracker for this.
That helps.
Yeah.
Absolutely. I don't ex… yeah, I'm not expecting anyone to take it up right away, but I myself am interested in adding those things in, because it acts as a guidance for any new Gen AI observability or monitoring person coming in, looking at the demo, and then having an example to Play with it.
**Som Banerjee** 26:15 Correct, correct. Yeah, yeah, I'll be looking forward to it. I mean, so far, I think, most of the Gen AI ops, innovation is on the platform side, like.
you know, how all… how the logs are being, classified, issues figured out from the logs, but not really much on the actual instrumentation. So, I'd be very keen to know.
**Shenoy Pratik** 26:46 I was there, like, it's an interesting point, like, before we wind up. I was there at KubeCon two weeks ago, and there I saw… a lot of existing OpenTelemetry users, end users, didn't know that we had a good gen AI thematic conventions, which were still coming together. It's not stable, stable yet, but, there is something where people Can start looking forward, and… Taking that as a guidance to instrument, to instrument there.
agents. So, yeah. Again, I'm missing pieces that people are searching around, and this can be a good place for it.
Yeah, I added an action item on me for that, holistic issue.
Around pending ZNA semantic convention.
And then we can start on our queue.
Cool. I think we are about time as well. Thanks, everyone, for joining. See you guys in the next meeting. Bye-bye.
**Srinjoy M** 27:50 Thanks, mate.
**Som Banerjee** 27:51 Cool.
Good, thanks.
**Srinjoy M** 27:53 Take them safely.
