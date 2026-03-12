SIG: CI/CD SemConv SIG
Date: 2025-11-11
Duration: 18 minutes
============================================================

## Zoom Recording Transcript

**Christophe** 00:21 Hi, Advent.
**Adriel Perkins** 00:38 Hey, how are you?
**Christophe** 00:40 Fine, how are you?
**Adriel Perkins** 00:42 Doing good, thank you.
Not doing… not doing good.
Welcome back, how's, how's the new job been treating you?
**Christophe** 00:53 Very well.
**Adriel Perkins** 00:54 Awesome. I'm very happy with my team.
Fantastic.
**Christophe** 01:03 So… The new SICK has started.
**Adriel Perkins** 01:07 Yep.
Yep, this'll be, I guess, our first meeting with people… with more than one person.
**Christophe** 01:16 Yeah, I saw the recording of last week.
**Adriel Perkins** 01:19 Anyhow, So, it's good. Thank you for being able to attend. I think, I'm surprised anyone's coming this week since KubeCon's this week. I was supposed to be there, but I had to cancel my trip for some reason, so… I don't… I expect probably a few other are there, a few other folks are there.
The new project board… I was gonna do… if there was gonna… if there was gonna be, like, a lot of folks here and, like, new faces, I was gonna do some introductions and… and figure out what people were interested in working on.
But we can just hop directly into the board first, because this is the new one, all with outstanding issues that were on the old board.
That had, like, labels of Phase 2 have been migrated over to the new board.
Nothing is in progress.
And I think there's some, of course, based off of our charter… There's some stuff that we need to add, very likely.
**Christophe** 02:29 Were there any issues from the old boards that were not migrated to the new one?
**Adriel Perkins** 02:35 No.
Everything that was on the old board was closed out.
that could be closed out, and then that's… the stuff that hadn't been started was moved over, so I think that covered everything.
There's some work that needs to get outlined for the propagation.
So, there was a prototype example PR in Go, but it's been closed because it was solely there to inform a prototype, so now we need to actually open up, support. There's one for Python that's been opened that's not been received any feedback, so, I'll just need to add some information there.
For the… some… some tickets here, That's one of the things. Let's see… There is a, let me just write this down.
to SDK… There's a new… There's a pull request that's been opened in semantic conventions to try to unify workflow pipelines.
I think that's something that we probably want to, like, actively review.
and work with, because that, you know, does impact us quite a bit. I think the PR has been opened with that vein in mind, but I don't think we've talked about it as a SIG since it's been opened, so…
**Christophe** 04:24 I saw your recent comment on it.
And yeah, I thought about it at the time when it was first opened.
But, yeah, we didn't have any plan for how to go forward with it.
And I also remember the discussions we had in the semantic convention SICK.
Where they told us, yeah, let's start with… having it scoped to just CICD, And later, think about… Making it more general.
**Adriel Perkins** 04:58 Yeah. So, I think it's good that we will discuss it next Monday.
Yep.
So, yeah, we should definitely… I agree. Is it this one? No.
**Christophe** 05:10 No, I think it was.
**Adriel Perkins** 05:23 Oh…
**Christophe** 05:43 I think it was number 1688.
**Adriel Perkins** 05:46 1688.
**Christophe** 05:55 No, that's 2014.
**Adriel Perkins** 05:58 Oh, that was weird.
1688.
**Christophe** 06:08 Yep.
**Adriel Perkins** 06:17 Okay, that's an issue.
And then the new pull request is 146.
Let's review these… Debs.
Alright.
Thank you for finding that.
Most of this, I think, is incorporated, at least with some of the starting issues that exist on our new board.
These two are a little bit nebulous, so, like, it's kind of hard to define the work until, well, sorry, 4 is nebulous.
This we… is kind of being already done as part of collector contributions.
And then this one is working on that issue.
So those are, I think, the main things that we just need to start, like, prioritizing and working with folks.
To try to accomplish.
And these are all the ones that, like, this is the long-running trace one.
And then there's.
**Christophe** 07:42 Yeah, for that one, I think I will take a look at what Jagger is proposing.
**Adriel Perkins** 07:48 Okay. And how it aligns with the changes in.
**Christophe** 07:51 Specs… I think there were a few issues in the spec repo.
Is that what we put on?
**Adriel Perkins** 07:57 Yeah, there are.
For sure. Okay.
Cool, yeah, we've got people that have been asking on the collector side, too, of being able to omit spans, or partial spans.
So… because they have, again, long-running traces, so that's what they're asking for.
But until that's kind of, like, solved in the spec, it's kind of hard to… especially from the collector perspective, it's kind of hard to do that, because you're not reliant on… We're actually relying on an exporter, not necessarily just the receiver component itself.
**Christophe** 08:41 Yeah, I understand why they implemented it that way.
Josh explained it once in the SAMConf meeting.
It was based on HTTP traces, and yeah, there, it's all short.
**Adriel Perkins** 08:55 Yeah.
**Carlos Alberto Cortez** 08:58 How important do you think this is, or this will be.
I mean, I guess, I'm guessing it will be very important, but for the time being.
Like, how many issues or users have you seen that Have come and actually tell you that this is a problem for the existing components.
**Adriel Perkins** 09:19 That's a good question, because I live a little bit in a bubble. So, like, I'm not looking at it as a project as a whole. There's definitely multiple issues that have been long-standing in the spec that people are, like, still discussing.
And then there's been more recent issues in the GitHub receiver component.
that's, like, we want to emit these spans early, and there's other people that are doing it, like, Dagger.io does it with their stuff, and they can visualize it in that way. But, you know, in part, it's, I think, also a little bit of back-end support. Probably a little bit required.
But I don't know, like, beyond that, how widely important it is, but there is definitely a need, because Alan opened that issue originally because of Argo CD workflows, and they can be extraordinarily long-running, too.
And they can persist, they can be running in persist, controller restarts as well, so… I think it's important, I just can't say for the project as a whole.
**Christophe** 10:20 From my side.
it's in Jenkins, it's not really as an open issue for it, it's more that I talk with people.
And it can be an issue if Jenkins restarts at the work… the workflow loses its… a parent trace.
And it can also happen, yeah, it's later.
for reporting, You can have inconsistencies, so that you're missing traces, And you can… Only analyzed after your job is complete, so you can never really have visibility on running drops.
You could… Have a first stage with a checkout and analyze on that, because that would be a span of the trace that would be sent early.
But yeah, you are missing the full context.
**Carlos Alberto Cortez** 11:21 Okay, yeah, I will take a look offline. I'm very curious about how Jagger implements this, and you were talking about, Adriel, about the receiver. Which one is?
Specifically.
**Adriel Perkins** 11:33 The GitHub receiver?
gets…
**Carlos Alberto Cortez** 11:36 Alright.
**Adriel Perkins** 11:36 Yep.
**Carlos Alberto Cortez** 11:38 We'll take a look, yeah, offline after the call. I'm a little bit curious about this, probably can… Say what they think after, yeah, chewing that stuff.
**Adriel Perkins** 11:48 Sounds good.
Appreciate it.
**Christophe** 11:55 for the Phase 2 project goals, I had a thought about As a stabilization point.
If we are talking about the workflows.
And we plan to go in that direction, I guess.
We would need that first, before we can go towards stabilization of, the full CICD semantic conventions, I guess.
**Adriel Perkins** 12:22 I think… I think stabilization can probably… stabilization can probably occur in pockets.
For things like… like, for the long-running traces, as an example.
I don't think that blocks… attributes around VCS repositories, right? Like, from being… from being stabilized. So I think it can occur in pockets, I just… and I don't expect us to be able to… to stabilize all the things that we've done, but… But we probably should define, like, what we think is probably reasonable, before we start to tackle it, what's stable. Like, another thing is, like, the CI-CD pipeline stuff, that might not be able to be stabilized because of the unified workflow PR that's open.
That we need to review. So, like, we might need to figure out, like, how we want to proceed with that before we even try to stabilize it. But I think So, like, the VCS attributes are…
**Christophe** 13:18 enthusiast metrics, I guess we could stabilize those.
**Adriel Perkins** 13:22 Yep.
**Christophe** 13:25 Agreed, yeah.
**Adriel Perkins** 13:35 Cool, that's really all I had.
**Christophe** 13:38 I don't have any other points either.
**Adriel Perkins** 13:46 Did you have anything in particular, Carlos?
**Carlos Alberto Cortez** 13:50 No, no, just trying to catch up, you know, yeah, trying to… today, I had 3 hours.
Nice. I want to come check out what's happening, yeah. Yeah, most of the time, I am checking stuff offline, by the way.
**Adriel Perkins** 14:02 Appreciate it. I definitely appreciate the support there.
Real quick, one of the things that we have to do, actually, is add SDK support for the environment variable context propagation stuff. I have a PR that's been open for, like, a really long time in Python that's, like, never been looked at.
Robert Pajak just closed the Go one, because that one was just like, hey, he just wanted to build a prototype of what it could look like, not that it was actually working.
But do you have any suggestions on, like, getting PRs reviewed in the SDKs?
**Carlos Alberto Cortez** 14:36 I think we have, mentioned in the specification and explained to maintainers there why it's important that they review this.
**Adriel Perkins** 14:46 Okay.
**Carlos Alberto Cortez** 14:46 And basically, yeah, I think that for them, it's like, as you said, that Robert thinks that it was good to prototype, and that's good, but now we actually need to get that out as… unstable packages, or similar. Without that, we cannot make more progress. So, once, yeah, let's remind them and, let's say, kind of, we sing on that front, on this registration call.
Today, we won't have that call because of KubeCon.
But next week, let's push that. Actually, let's… let me add an item to the agenda, and mention the specific PR for Python and Go.
And yeah, let's try to make progress.
I can pro- I can probably write one or two for other languages as well.
For Python… for Java, sorry, Java or .NET, it didn't have one.
**Adriel Perkins** 15:33 No.
**Carlos Alberto Cortez** 15:36 Okay, I will do that now, yeah.
**Adriel Perkins** 15:38 Awesome.
**Carlos Alberto Cortez** 15:39 Like, filling… filling the, the issue for, yeah, next week's call.
**Christophe** 15:45 I guess we don't have to limit ourselves on those listed here. We can implement it in all the SDKs, if possible.
**Adriel Perkins** 15:52 Yeah.
**Carlos Alberto Cortez** 15:55 Yep.
**Adriel Perkins** 15:59 Perfect. Cool. Wrote that down in the notes.
Awesome. Well, thank you all for attending. It's good to see all those faces again, and hear your voices.
Respectively. Looking forward to, working with you on Phase 2. Y'all enjoy the rest of your day.
**Christophe** 16:14 You too. See you.
**Carlos Alberto Cortez** 16:15 View.
