SIG: .NET SIG
Date: 2025-09-23
Duration: 28 minutes
Zoom Recording URL: https://zoom.us/rec/share/ibwoQ8p5EVsKDUzz3qoLZMweuX-3lq5r5WNgVwMYr2dU8YGmnXDRIxowC-G9U_8n.5a8LNWl30s6nF0oO
============================================================

## Zoom Recording Transcript

**Julius Koval** 03:18 Hi, do you know if Rosh… do you know if Rosh has come? Oh, he is here, okay.
**Rajkumar Rangaraj** 04:11 Hello, everyone.
Just want to check if anyone else wants to drive. If not, I will share this tweet.
It's very quiet, I don't even know whether people are able to hear me.
**Martin Costello** 06:28 Yeah, okay…
**Rajkumar Rangaraj** 06:31 Cool.
Let me show my… Best job.
I think, there are a few topics that's been added for today.
I think the second and third one would be much simpler to discuss, and then I think we can jump onto the first one over there.
To, like, let me open that PR, which, Martin is discussing about.
So, this peer… I feel we should get it merged at the, The only thing is that, Martin, like, I don't have any problem merging this, so we discussed about the small release before this one, so that's why I did not merge those PRs.
this one and the other one. So it's better to get one of the release out with all the OTLP work, what we have it, and then start merging these PRs and do the… kind of, RC release, for the .NET 10 release part. Do you have any concerns with that?
**Martin Costello** 08:06 No, that's fine. It's just, this has been hanging around for a long time now, and it's got all the approvals, so I didn't know what was holding it up.
**Rajkumar Rangaraj** 08:14 Yeah, I don't think this has any concern. This is our direction, so it was made very clear in the previous six. So we should merge this one, and you have another PR after this. We should follow up and merge that one, too.
But let's, make sure we do one more release before we get these PR smudged.
**Martin Costello** 08:36 Which was the other one?
**Rajkumar Rangaraj** 08:38 The last one in the list, like, where you add the .NET 10 runtime.
Support.net.
**Martin Costello** 08:47 Oh, right, yeah.
Yeah, I… yeah, I don't expect that to be merged until this has been released, yeah.
**Rajkumar Rangaraj** 08:54 Yeah.
No.
So, the plan is to have, something, by end of, this week released, and then keep merging these PRs. All of these PRs are already in a good, place. We can, I think we can start merging, approved and start merging. Thanks.
**Martin Costello** 09:15 Okay.
**Rajkumar Rangaraj** 09:16 Let me move on to the next topic. Julius, this is a… I don't know whether you were able to join, like, we had a discussion in one of the… I think you were not there, and we had a follow-up, the… The next week after you joined.
So, the plan is to get to the LogsBridge API once after the .NET 10-based release is done. We can consider changing the experimental, like, APIs, what we have for LogsBridge, and we can, Try and move that to the… Stable lowers.
**Julius Koval** 09:55 Yeah, okay, so I guess that was most of my questions, so… Yeah, I guess I don't have anything else.
**Rajkumar Rangaraj** 10:04 Okay. Now, that's why I know, like, the last two, I said it's going to be easy and everything.
So I, I, then, like, we can, jump… last week, I also got, like, a small topic, it's not here, the small update I just want to say here.
Last week, I said I will reach out to Pietra to see if he is interested in becoming a maintainer for this repo, so he's fine becoming one of the maintainers, so I'll be going ahead and creating and Today, I'll be going and creating a PR, promoting as a maintainer for the SDK repo.
we had already had a discussion with Alan offline also, so he's also, he… last week, he was good here too, but he also, invited Pietro to become a maintainer, so we… both the maintainers are supportive in bringing him there.
Hmm… So that's the information I wanted to pass on. I think the third thing is that, like, Robert has Provided the feasibility of providing… supporting the new attributes.
So, I… Does anyone have any context here to fill in, like, what this is?
So, I'm not following this in the specification. I may need time to take a look at it before we make a decision on it. So, just wondering if any of you have any clue about what it is.
So it looks like, like, no one has got anything. Just, let's try, take a look at it. If not, we can, read and get back to this, like, in the next week also, so that, We will have a concrete answer for the robot instead of, Providing some, loose answers at this point.
**Martin Costello** 12:21 Yeah, I'll try and read the issue in the linked spec.
**Rajkumar Rangaraj** 12:25 Yeah.
**Martin Costello** 12:26 by next week.
**Rajkumar Rangaraj** 12:27 Yeah, so I think, like, I'll update,
**Mike "Blanch" Blanchard** 12:49 I could tell you, Raj.
**Rajkumar Rangaraj** 12:52 Yep.
**Mike "Blanch" Blanchard** 12:53 Go to his… the issue.
Scroll down a little bit.
So he's, like, linked to this… handwriter.
And saying, like, oh, it's possible, and… That's, like… Not even remotely the issue with supporting this.
Because you look at something like a log.
you know, we have iLogger to deal with, it doesn't give you much contract at all, so…
**Rajkumar Rangaraj** 13:27 Yeah.
**Mike "Blanch" Blanchard** 13:27 Take some random object.
If we want to support a complex… Type as a log attribute.
And that's always been part of the spec for logs. We don't support it today, because What do you do with that object? You know, do you traverse it reflectively?
where do you put those values? How deep do you go on those values? What if there's an infinite loop? You know, there's, like, so many issues there, and the performance is going to be terrible.
So we never supported it for long. So, like, in order… this code that's linked that writes it out, you know, this essentially takes our DTO and spits out OTLP. That's the easy part. The hard part is.
How do you capture the data?
So remember that a log, when you call, like, iLog or log.
It's only good at that call site, so if you're gonna batch that thing, you have to do all that work to copy it to, like, our pool storage so that it's available when this code fires.
Otherwise, if it's not, if it's like a normal, you know.
synchronous processor. You could maybe pass it along, but then you have to have two sets of code.
You have to have one that knows how to write out, serialize our capture data, or one that does it off a live object, which would just be another mountain of reflection. It's probably a problem there. That's just logs.
Off the top of my head, it seems much easier to do it for traces.
Because we have an activity, It's gonna stick around.
metrics… I don't know how you would do that, like… Your dimensions are part of the aggregation.
I just popped open the spec issue, and it says it's… this should be done on… Metrics, resources, instrumentation scopes, fan events, like, all over the place.
I don't know how it would be done on metrics. You'd have to, like, rewrite the whole aggregator That's like a… a huge undertaking.
Those are just my thoughts on it for you.
**Rajkumar Rangaraj** 15:53 So, if I understand you clearly, then I know the stance you explained on the logger part, Blanche. Especially, like, there were several discussions happened earlier also, I believe.
Because even in the .NET, it's all string, and we did not want to invite new problem perf issues to the SDK. That's why it stays that way.
So, looking at it, like, it's going to invent more problem, perf problems to the SDK than doing any more benefit here. So, probably we might need to understand from a, like, where the… need to review the spec, or to understand what's the real user use case for…
**Mike "Blanch" Blanchard** 16:42 The kind of interesting thing here is… We don't see a lot of users asking for this.
So I wonder what… why it's coming from the spec.
**Rajkumar Rangaraj** 16:51 Yeah.
**Mike "Blanch" Blanchard** 16:52 It was something I had always intended to support.
Because it is… it has always been part of the log spec. The log spec's a little bit different, where it explicitly says complex types are supported.
where… in tracing and metrics, that has never been the case. It has its, quote, standard attributes, which is like a subset of what OLTP supports.
what I was intending to do with logs… is in the LogBridge API, We can put our contract.
if we go with what the spec says the bridge should be, right? You have a logger provider, you get a logger, it has an init log, it has a contract. We may be able to introduce something there where you can say, like, I explicitly want this complex thing And it could have an interface.
It could be an any value type of thing. There's more options there. It's much harder to do with iLogger, if that makes sense.
But it's still a big, big undertaking for logs.
**Rajkumar Rangaraj** 18:02 Got it, Blanche. So, probably, like.
Later, I either summarize and write my response in here.
instead of just one. It'd be super easy for tracing, I feel. Metrics, I wouldn't even go there.
Yeah, I think metric is very, very trickier situation to have these kind of stuff there.
**Mike "Blanch" Blanchard** 18:25 I don't even know what it means.
**Rajkumar Rangaraj** 18:27 Yeah.
**Mike "Blanch" Blanchard** 18:30 Like, what would you aggregate on with some… complex structure.
**Rajkumar Rangaraj** 18:42 No, like, what's the status of this spec? Is it already stable, or is it experimental?
**Martin Costello** 18:51 I think they've… it… I forget the terminology, but because it's only implemented for Go, it can't be stable because two of their SDKs have to implement it first.
**Rajkumar Rangaraj** 19:02 Okay.
**Martin Costello** 19:04 So I think they want to use .NET as one of the other three.
**Rajkumar Rangaraj** 19:08 Okay, so with the complexity, I… I would… Say that we have to hold back until it is proven to be good in the other repos. I understand, let's see, like, if you could wait. But still, before taking any decision, I will go ahead and read the spec very clearly. And, we have the inputs from Blanche, he's the subject matter expert in that area, too. So, we will… Get back to this once again.
**Mike "Blanch" Blanchard** 19:43 I think, Raj, there was an issue that Sam created A while back, about… complex logging in .NET runtime.
We were talking to, like, Noah and Tarek about doing something in iLogger.
It seems like Noah's a bit apprehensive about that.
**Rajkumar Rangaraj** 20:07 Yeah.
I think Ludmila was also part of this, and, like, A big conversation went on, on that.
**Mike "Blanch" Blanchard** 20:20 It's definitely… things we've talked about and worked on before. Like, 3 years ago, I did a whole proof of concept in runtime for iLogger to do it.
Noah didn't go for it.
**Rajkumar Rangaraj** 20:39 I just want to copy his alias like it's… I do remember that.
I do remember a big conversation happened in the issue in the .NET runtime. I don't know whether he created it or someone created it, and he started supporting that. I'll just go ahead and.
**Mike "Blanch" Blanchard** 21:18 Yeah, he might… you could try pinging Lyudmila, I don't know if she's still around.
She was kind of pushing for it, because… They wanted, like… events… So the event spec for logs for, like.
some kind of AI thing, where they want to log, like, a bunch of the AI details.
as, like, an event with a complex structure. I don't think it went anywhere, but that was sort of the push for it.
**Rajkumar Rangaraj** 21:49 I'll try and figure that out also. I remember that issue. I'll be able to get that. I'll ping normalized mode now, so let me see, like, if I can get, catch her over Slack and have that discussion.
**Mike "Blanch" Blanchard** 22:10 If you look, just real quick.
The last thing on logs, if you look at our log record structure, it has attributes, Which is… What, a read-only list of key-value pairs?
So even if we… if we solved… If we had a solution for, like, serializing and storing the complex types.
**Rajkumar Rangaraj** 22:35 You'd have to do something in this…
**Mike "Blanch" Blanchard** 22:39 API so that exporters can get at it and not have to inspect, like, objects.
That's gonna be… Tricky to do in a non-breaking way.
Like, scroll up a little bit to where you have all the public fields.
Exception, you see attributes…
**Rajkumar Rangaraj** 23:02 Okay, this is state values.
**Mike "Blanch" Blanchard** 23:07 So that object.
**Rajkumar Rangaraj** 23:08 There we go.
**Mike "Blanch" Blanchard** 23:10 The object is a problem.
**Rajkumar Rangaraj** 23:12 Yes.
**Mike "Blanch" Blanchard** 23:14 I think what the issue is essentially saying for the spec is.
That should be, like, an any value.
which I think in some languages, is no problem. They just expose the OTLP structures, but in .NET, we have iLogger in front of us.
And we've built that into this contract.
Just something to think about.
**Rajkumar Rangaraj** 23:59 Okay, that's something we will just need some more… I'll try and take the summary here, Blanche, after the meeting, the meeting recorder can pull your summary, and I'll add it here. I think that would be enough.
To summarize, I believe, at this point, or this one.
don't think we have any other important things that are pending, apart from whatever that we discussed. There are other PRs, I think.
We can do an offline review on them.
**Martin Costello** 24:38 There's a quick one that could be merged. There was a PR I did for the renovate config, but I accidentally did it as not a fork, so it wasn't mergable, so I had to open a new one.
If that can be merged, then we should be able to run.
**Rajkumar Rangaraj** 24:55 renovate…
**Martin Costello** 24:56 And have it update everything properly on the next run tomorrow.
**Rajkumar Rangaraj** 25:00 Is this the one you're…
**Martin Costello** 25:03 Yes, that's the one.
**Rajkumar Rangaraj** 25:05 Okay, I'll try and merge it immediately.
For this item, taking a look at it yesterday itself, and approving it.
**Martin Costello** 25:14 Yeah, that was a different PR, but it wasn't from the fork, so I couldn't update it because of the branch rules.
**Rajkumar Rangaraj** 25:19 Okay, I understood. I know that branch one is causing a problem, Martina. I thought we had a discussion here. The very simple thing is that if we open up the small, small loose end, you say, right, all the small drops will create a big problem at the same time.
So that's why we are not even allowing all this small… things there. The small, small things will become big at some point, and really, slightly makes it slightly unmanageable. That's why we have those things. I know this is the second time, you're running into this issue, second or third time, if I recall.
**Martin Costello** 25:58 Yeah, it's just the GitHub UI does not make it easy. Like, if I open the code in upstream, this repo.
to make a teeny change, the GitHub UI, because I have right access, just goes, oh, just edit it here. And I have to jump through lots of hoops to definitively try and… try and do it in a fork. And even in this case, I failed.
It's like It feels like we're fighting against GitHub for reasons that I don't think are really problems.
Because, like, it occurred to me this morning, if I just named the branch Copilot Slash.
It would then not be scooped up in the rules.
**Rajkumar Rangaraj** 26:42 Yep.
**Martin Costello** 26:43 And it would work, but it's just me putting the word co-pilot in.
I don't think it's really protecting against anything, but it's just creating friction, so… That's my two pence on it.
**Rajkumar Rangaraj** 27:03 I got that merged, Martin. Hopefully, I think Renovitch should kick in now and start working on it, I believe.
The only thing I don't know now was, like, I think we have both.
Deepana bought and renovate now, right?
**Martin Costello** 27:21 Dependabot should… if I… let me check.
Because I did raise a PR, but… yeah, Dependabot's basically off now.
**Rajkumar Rangaraj** 27:30 The file to configure it is still there.
**Martin Costello** 27:34 But it's only doing GitHub Actions, and on a yearly schedule.
**Rajkumar Rangaraj** 27:39 Okay. Which is basically just a hack.
**Martin Costello** 27:41 to make automated tools that scan repositories, seeing if they use Renovate. Think we use… sorry, think we use Dependabot? Think we use Dependabot.
In practice, we're not using DependBot, but it looks like we are for things like OSF Scorecard.
But for all intents and purposes, it's now renovate.
**Rajkumar Rangaraj** 28:04 Got it.
That's all… On the agenda and the, data perspective, I think we… as I said, we might need to drive the release.
probably next Tuesday is something we need to target, as it's going to be a stable release. We will do an API review in the, SIG, and then we will continue with the release.
Cool. There it is.
That's all I think we could end now.
Thanks, everyone.
**Martin Costello** 28:53 Bye.
