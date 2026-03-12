SIG: .NET SIG
Date: 2026-01-20
Duration: 22 minutes
============================================================

## Zoom Recording Transcript

**Alan West** 02:08 Hey, friends.
**Matthew Hensley** 02:12 Blue.
**Zach Montoya** 02:14 Hey, everyone.
**Alan West** 02:18 Sorry, I actually need to jump off and then back on. My computer is… acting.
laggy or something. Hold on.
**Rajkumar Rangaraj** 03:32 Play everyone.
Share my screen.
Blue on that.
**Alan West** 03:50 Hey.
**Rajkumar Rangaraj** 03:53 Today we have only one agenda I added. I don't know if anyone has any other topic, please go ahead and add it.
So, so we wanted to do the, release, next release, starting today. Pietro has reached me out offline also about this, so I thought it's better to add it to the SIG and take a look at the public API review before releasing it. So if we are fine with it, we can just quickly scan through the public API release.
And so, like, I, like, Pyotr has agreed to do the, this time's release, so we can have him do the release.
Any objection from anyone here on the release?
**Alan West** 04:48 Nope, I think that sounds good.
**Rajkumar Rangaraj** 04:50 Good.
**Alan West** 04:51 Did you just say you wanted to go over the public API during this meeting, or…
**Rajkumar Rangaraj** 04:55 Yeah, we can just take a quick look through that, what changed in all of them.
I don't think anything went here in the… provider extension, so I'm just going to take a quick look at the API.
So we added a schema URL support to the, Tracer. I don't know which is the right way to do it, do a public API directly, and…
**Alan West** 05:27 Yeah, looking through the public API unshipped, It's probably the easiest way to get a… high level.
**Rajkumar Rangaraj** 05:37 Yeah.
I don't know whether, Is there an easier way to get this? Anyone knows, like, how to list all of them?
**Alan West** 05:51 Not really. The, starting the release process?
You, I think you get an opportunity.
**Rajkumar Rangaraj** 06:04 Yeah, that's…
**Alan West** 06:05 R to look at the changes.
**Rajkumar Rangaraj** 06:07 We can do that, like, Yeah, that's how I think we read you last time. Also, Blanche…
**Alan West** 06:14 Yeah.
**Rajkumar Rangaraj** 06:15 Asked me to do the same thing.
we had… Release folder… My memory is really bad. We had a release folder here, that's where we had that dock.
**Alan West** 06:35 You're just basically wanting to, like, Kick off the PR.
**Rajkumar Rangaraj** 06:38 Yeah.
**Alan West** 06:40 Yeah, it's been a while since I've done it, but yeah, essentially it's, yeah, here we go. Just creating a new release, and… Giving it the correct version and all that.
**Rajkumar Rangaraj** 06:51 Yeah.
I'll run this workflow, so at least we will have something To check, you know.
Minimit.
Let me switch back to the PR.
Let's give it a minute for the workflow to run. If we have any other things for discussion, we could take that now.
**Alan West** 07:47 I don't personally have… anything. The database instrumentation has been… out in RC for about a week now. I figure maybe wait another… I actually haven't checked to see if there have been any open issues, but…
**Rajkumar Rangaraj** 08:06 Let's take a look at it. Even I did not see anything. Let's take a look at it to confirm, like, we did not miss any email or anything.
Nope, nothing. I think we are looking good.
We could wait till the end of this month and do a release, either end of this month or the first week of Feb, anything is fine with me.
**Alan West** 08:33 Yeah, I think that sounds good.
**Rajkumar Rangaraj** 08:38 Does anyone else have any other question or any other topics for discussion?
It looks like everyone is quiet, so… Okay, here we go. The PRSCAM.
Yeah, no changes to the… Provide a builder extension that's do that.
And this one is, like, you know, the schema URL support, the nothing apart from that. It looks like this, but it's not a big public API change or something. We have an additional attribute, schema URL.
This also looks fine.
Come on.
**Alan West** 09:30 And I forget, you know, I didn't actually track that work, The schema URL, is that now also supported by the Activity API and the meter API?
**Rajkumar Rangaraj** 09:43 That's correct, yes.
**Alan West** 09:44 Gotcha.
**Rajkumar Rangaraj** 09:45 And, we changed even… there are many changes happened to the exporter also to emit that information. For example, OTLP exporter and the console exporter also emits the telemetry schema URL from the activity source.
**Alan West** 10:01 Great.
**Rajkumar Rangaraj** 10:05 So, this calls about that changelog, we can review that in depth. Yeah, this is what I said, like, this is the change that we did. Added the support for the telemetry schema, URL property, and all the exporters.
So, as a part of that, we had a change in the public API also. This is for the test we have… this has been introduced. I hope this is fun.
**Alan West** 10:37 When you say it's for the test.
What was that? That was the metric snapshot.
Right.
That we were just…
**Rajkumar Rangaraj** 10:45 We just exposed this here, mostly in-memory. This is for the in-memory.
**Alan West** 10:49 Yeah, yeah, yeah, yeah, yeah, that's right.
**Rajkumar Rangaraj** 10:55 The changelog covers that, so this is fine, looks good. The other public API is…
**Alan West** 11:02 Oh, yeah, right, you can set that now. That's… that's a good thing to get out.
**Rajkumar Rangaraj** 11:05 Yeah.
**Alan West** 11:09 and user agent product identifier, I mean, I assume that that's…
**Rajkumar Rangaraj** 11:13 The prefix that we could add it, like.
**Alan West** 11:16 Yeah, right, but that's the… The spec didn't have, or did it have any, like… Specifics about, like, what to call that.
**Rajkumar Rangaraj** 11:28 It follows the spec asset as whatever it calls, it's the name that it uses, I believe.
**Alan West** 11:35 Yeah, fair enough. Okay.
**Rajkumar Rangaraj** 11:43 So here, like, just to show when the many changes went into this one, just opening it to understand how many changes.
So, definitely the telemetry schema URL for the… Activity source and the meter.
And there was a bug that we fixed it for this program.
And one of the environment variable support, plus the MTLS configuration for the OTMP exporter. These are the things it's going. This is where it's a heavy in this release, the OTLP exporter perspective, even though there is no public API, but slightly heavier from this aspect.
**Alan West** 12:23 Did we, It looks like the answer might be no, which is fine, but the environment variable, the histogram aggregation, did we expose, Like, a way to do that programmatically as well?
**Rajkumar Rangaraj** 12:37 No.
**Alan West** 12:38 No, okay.
That might be something that we'd want to consider at some point. Yeah. Because typically we've had, kind of.
Symmetry between those two things?
**Rajkumar Rangaraj** 12:46 Yes. So, I did the work for this one. It's slightly complex, but we have to expose many things and change… we need to do it in a… refactor everything to get that done in a proper way.
**Alan West** 13:00 Yeah, I can… I can imagine. I looked at that issue a long while back, and yeah, it wasn't straightforward, I understand.
**Rajkumar Rangaraj** 13:07 Yeah.
So, Zipkin also… This is also better to take a look at it, like, this is what we are saying it here. I think, hopefully, we are fine with this one.
**Alan West** 13:29 Yeah, that's fine. At what point do we just remove those from this repository entirely?
Or do we?
**Rajkumar Rangaraj** 13:40 I think prop… like, I would say once this is done, we should remove it from the repo, so that we don't maintain… we don't need to maintain this. So if anything is needed, we have a tagged version already, we can do a security releases from there.
**Alan West** 13:54 Okay, yeah, perfect. Yeah, that makes sense.
**Rajkumar Rangaraj** 14:05 Yeah, hosting has no changes.
In the propagator, also the similar story, but it's not a whole package, but a small… like, part of it is going off, agar propagator. Like, then it's calling… will be removed in the future version also.
**Alan West** 14:28 Yeah, that one will probably be more long-lived, because if we do actually remove it, then we'd have to talk about what a major Persian bump would look like.
**Rajkumar Rangaraj** 14:38 Yeah, I won't recommend doing that unless we're considering the 2.0 or something like that. People may have a dependency on it. Yeah.
Here is the another one, like… two things that got added to this public API of the metric part. One is the metric schema URL, and another one is we started supporting the low memory Template.
Which is a good thing. It's a long-pending stuff, I believe.
Let's take a look at our goal, what it does.
This is a long-pending ask, so this… we started supporting this, Autel SDK disabled and load bit variables now.
**Alan West** 15:37 Yeah, low memory temporarily is the… another one, trick schema URL.
**Rajkumar Rangaraj** 15:43 Yeah.
Some improvement in the, memory consumption of this program, and… We had an issue in the, resource attribute, how it's decoded, so we fixed that, too.
**Alan West** 16:03 That was a bug.
**Rajkumar Rangaraj** 16:04 Yeah, that was a bug, yes.
**Alan West** 16:08 Cool, it's a good release.
**Rajkumar Rangaraj** 16:09 Yeah, it's good, everything. Maybe, you know, like, we can take a look at it offline and review it. From a family KPA review, it looks good to release this one.
Let's take a look at any PRs.
the last one I went, back to the… NET team. Looks like the .NET team, the Blazor team is very supportive, and they did a review of this PR already, and looks like one of the engineering managers from the Blazor team itself, reviewed this and, left, a few of the comments and all here. And on top of that, Noah also came and, like, provided as… yeah, he's the engineering manager for the… The laser.
**Alan West** 17:09 I saw Noah's comment here.
**Rajkumar Rangaraj** 17:10 Yeah.
**Alan West** 17:11 It's interesting, yeah, I don't… he basically raises the concern that I was curious about. Yeah.
Which is, it might be one.
At the time, but… oh, we know, whatever.
**Rajkumar Rangaraj** 17:24 Yeah.
**Alan West** 17:25 Maybe, since it's… it's not like it's, it doesn't require any exposed public API, I mean, you know, that… That check, if it turns out to be… not quite right. It might be something that we can… Improve or fine-tune in the future, if necessary.
**Rajkumar Rangaraj** 17:46 Yeah, I will ask, or also ask, ping him, Larry, to see if he can take a look into the, Noah's comment and like, provide the response. In that way, we understand what's… what do we need to do it in the future, or, like, we can add an additional comment or things in the file, so we know what we are doing here.
**Alan West** 18:09 Right. You know, I, I'm not… thought super deeply about this comment that Noah's left, but, like, just… Just a thought, like, the previous check was using that isBrowser.
**Rajkumar Rangaraj** 18:27 Yeah. That came out of, like, feedback that I left, you know, really, like, a long, long time ago.
**Alan West** 18:34 in this world where we need to, like, improve this check somehow, you know?
I wonder if there's an advantage to going back to an approach like that, because what that would mean is that Browser… Scenarios would work. It would, you know, begin leveraging the new functionality of this PR, And then if there were other scenarios that were to surface that Weren't a browser, it was whatever, something else.
Then, you know, it would continue to use the, approach that uses threads, and… inevitably, I would expect somebody would open an issue, right, and say, hey, it doesn't work for this… this new scenario. So it allows us to, like, incrementally improve, whereas the approach that the PR is currently taking, in checking, you know.
Thread pool max size equal to 1.
Potentially cast a wider net and might capture use cases, that, whatever, are benefiting from the fact that it's using tasks.
And then we go in and try to improve that, maybe, like, you know, we need to improve it because it turns out it's… there's a bug, it shouldn't use the task-based approach in some scenario that we discover. We go and fix that bug somehow, but then we might end up breaking it for somebody else.
That was benefiting from the behavior.
**Rajkumar Rangaraj** 20:23 I agree with you there.
moving it incrementally would be the right… at least the best approach here, even… I agree with you on this one.
**Alan West** 20:33 Yeah.
I mean, anyways, I can leave… I can leave that thought on… on this PR, and just kind of pose it as a question. I don't… I mean, I don't know how cautious or, you know, whatever conservative that we need to be, I'm just kind of posing the thought.
**Rajkumar Rangaraj** 20:50 Yep. That makes sense.
So, this was marked as draft last week, so just left it. Looks like now, again, it's been marked as ready for review. So, not sure what has changed in the… Oh.
Yeah, looks like the summary and all is up-to-date now, like, for us to take a look.
Yeah, the other things are all new, we can take a look at it offline.
Yeah, I don't know where this is coming from, like, probably we may need to raise a question Man, this is coming.
How did they figure out this?
**Alan West** 21:37 Hmm.
**Rajkumar Rangaraj** 21:38 This is a threat safety, and what Issue it caused.
They have an issue already created.
Yeah, we need to understand this, and I think we can do this offline and SIG, and then bring it up in the next SIG or the future SIG needed.
Any other topics, if…
**Alan West** 22:10 Not for me.
**Rajkumar Rangaraj** 22:11 Cool. If there is nothing else, I think we could end the meeting, though. Thanks, everyone. Bye.
**Alan West** 22:15 Alright, take it easy, y'all.
