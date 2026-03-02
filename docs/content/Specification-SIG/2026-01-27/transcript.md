SIG: Specification SIG
Date: 2026-01-27
Duration: 39 minutes
Zoom Recording URL: https://zoom.us/rec/share/X7LDUM8qIHrrpFfmnhmMaL94tofaafvKIwrLUMl0UzAH7lYc5W11cUGFHbiRY69n.AWNe_3u-eT6lIjsS
============================================================

## Zoom Recording Transcript

**Reiley** 00:52 Oh, bop.
Hey, Tingor.
**Tigran Najaryan** 01:45 Hey guys.
**Reiley** 02:09 Can you see my screen?
**Tigran Najaryan** 02:17 Yes.
**Reiley** 02:19 Thanks.
Let's give a couple minutes for folks to join.
Yeah, Ra, thanks for joining.
We'll wait for another minute before we start.
Okay, let's get started. Trust, you have the first topic.
Trust, can you hear me?
**Trask Stalnaker** 04:28 Yeah, I'm here. Thanks.
Yeah, so…
just wanted to follow up. We discussed this last week. I think we have,
Seems like we have our re… we have consensus here. It does… we got feedback from the collector folks.
That it essentially matches the collector, behavior, other than the,
Edge cases around, infinity minus infinity, and not a number, doubles.
Which this PR takes,
the ProtoJSON, values, formatted, string formatting for those specific values, so I think that's good.
Just wanted to give people a chance to,
Ask any questions about it, because…
On the Java side, we are, we're stabilizing complex…
attributes, in the upcoming release, in what, A week and a half.
And so we'd like to, we're hoping to get this merged and this behavior, solidified.
**Tigran Najaryan** 05:57 Should we also change the collector to handle the edge cases you found the same way?
**Trask Stalnaker** 06:05 I'll send a PR, yeah.
Makes sense to me.
**Tigran Najaryan** 06:10 Okay, yeah, thanks.
I don't know if anything in the collector relies on those things.
So, I guess collector maintainers will know.
Whether it's important or no.
**Trask Stalnaker** 06:24 Yeah, that's a good idea. That'll force their,
Them to look at it.
Pablo did, approve the PR, so I feel good, at least, that we're majority aligned there.
**Tigran Najaryan** 06:39 Yeah, I'll… when I looked, I found that experters, some experters use it.
to send data to, I don't know, some backends, third-party backends?
It may or may not be important for them, I don't know.
**David Ashpole (dashpole)** 07:01 Yeah, I think the Prometheus exporters definitely make use of the… To string libraries.
**Tigran Najaryan** 07:08 Yeah.
N.
given that the edge cases are handled correctly there. I don't know if anybody has ever tested those values.
**Trask Stalnaker** 07:19 The good thing with the current collector behavior is that, it's not like they picked
Plus inf, minus inf, that actually have a message in there that basically says it's unsupported value, in the string, so it's not like a… doesn't look like a literal value that hopefully anybody should be depending on.
**Tigran Najaryan** 07:45 Oh, the text unsupported value is part of the returned string. I didn't realize that. Okay.
**Trask Stalnaker** 07:51 Yeah. Okay.
Which is good.
Yeah. I mean, good for us, good for alignment.
**Tigran Najaryan** 07:57 That's for us, yes, yeah, yeah. Agreed.
**Reiley** 08:01 Hey, Trask, I have a question about the floating number precision. So I know, like, a lot of, like, JavaScript runtime and JSON libraries, when they convert a double floating number to a string representation, there's a precision loss.
do you expect, like, people have certain test coverage, or it's fine? I… I think for…
For logs, probably not a big issue, but for metrics, I can see some problem.
**Trask Stalnaker** 08:32 So these would be attributes… attribute values.
As opposed to, like, metric values themselves.
and I think we… we had kind of discussed last week, this format is ex… Like, is lossy?
We're losing the type of the, attribute value.
Already So I… I think it's okay, even if that's… even if there is some precision loss there.
**Reiley** 09:11 maybe call that out in the PR, because precision loss, I think it's a vague thing, like, how much precision loss? If, like, we lost 50%, then it seems like something users should be aware of.
Like, they… if they don't want the loss, then they probably shouldn't use double floating number. They should just put a string or whatever, like B6A4.
**Trask Stalnaker** 09:34 Sure, yeah, I'll check… I'll check it, I'll check that. I'm not sure that there is precision loss, since it's to a string anyways, so I don't know why they're…
Would be precision loss, necessarily.
**Reiley** 09:48 Okay, so, I, I can, send something to you offline. I know there are a couple libraries that have the precision loss, so when you convert back, you've got a different value.
**Trask Stalnaker** 10:00 Oh, okay. When… okay. Yeah.
**Reiley** 10:03 the… the one in .NET, I think, has that, and it's by design, because many JavaScript runtime and JSON libraries, they don't have that precision, so you can have a super precise, long string, but the reader wouldn't
Handle that as well, so…
**Trask Stalnaker** 10:22 Yeah.
And this, this is only the string representation, this is only the, marshalling side, not the unmarshalling side in this APR also.
**Reiley** 10:37 Okay, anything else for this topic?
Okay, then we can move for Carlos. Thank you, Charles.
**Carlos Alberto Cortez** 10:52 Yeah, yeah, sorry about this PR. I was supposed to send that last week, but I totally forgot to actually put that in the comment. It's for the resource attributes handling, just basically relaxing that.
If you could open that, please. Basically, it's making two small changes, which I'm wondering whether, that's an up or not. I hope it is.
The first one is that it will fail fast, as considered, with what some Sikhs have, which is that they try to recover, you know, in case there are some errors, try to recover values. In this case, we're, discard the entire value, which means failing fast.
Just reporting an error.
The second one is that, all the characters that are outside the baggage octet, which is a subset of ANSI, they should be decoded, which means that in…
like, current validation, discarding them, or something will not happen. They should be coming encoded, and that's what Six should do, but otherwise, you know, they should behave just fine. And this should go… this should be fine, because as we discussed last week, this could be considered a relaxation.
So hopefully it wouldn't break 6. I totally forgot, by the way, to discuss that with the C++ and ROS 6, so I need to double-check with them. But I will show them this PR, you know?
**Reiley** 12:11 Thanks, Carlos.
Any comment? If not, please take a look.
Okay, one tool. Josh?
**Josh Suereth** 12:26 Yeah, so, this is, an OTEP to support having multiple resources export from the SDK. This,
has been open for quite a while. There's a couple prototypes from it, there's some feedback on it that I think has been largely answered, and I don't see a lot of disagreement. But I would like to, make progress on getting this kind of approved and reviewed, because it's,
we were informed from the entity SIG that the browser SIG considers this a blocker. So, what I'm asking for is for folks to take a look at this, everything should be addressed that was, kind of there previously. The only comment that I would say isn't addressed on this was there was a concern about
If we drop entities, there should be some sort of dropped entity count in the protocol.
To match the, oh, actually, sorry, that's a different PR.
That's, that's the entity merge algorithm, sorry. This one is the, multi-resources. So, actually, David Ashpole was kind enough to provide a prototype in Go for this, so now we have a prototype in Go, we have a prototype in Java,
I think the only remaining open concern is kind of details about how to expose
where to expose the notion that you would have more than one resource, whether it is on the SDK, or whether it is on the API. And I think it needs to be on the API, and actually David Ashpel has a good comment about that, but I also think that that can be resolved as we further prototype and build out the specification.
Because it doesn't really change the shape of what's going on. So, kind of asking for folks to take a look at this and,
review. I'm not aware of any other,
Like, anything significant that would block this?
And but we're looking for feedback. We want to make sure, A, it unblocks the browser SIG, and B, it is the direction to go to have OpenTelemry kind of support.
a form of multi-tenancy where we allow reporting against multiple resources from the same SDK.
So, please take a look. Hasn't been a lot of…
Updates or approvals, even though, like, there's a new prototype.
**Reiley** 14:47 Okay, thanks, Josh. Is there a timeline that you're expecting? For example, catch the next release, or just generally trying to get more review comments?
**Josh Suereth** 14:56 This is an OTEP, so it's more about we agree on the direction, because there's a lot of work to do. What I'm hoping is that if the browser sig considers this a blocker, that effectively we could agree to this OTEP in this direction, and then we can let the browser sig decide how to make progress in the specification, bring it forward. But let's agree that this is, like, the right thing to do first.
So, timeline-wise, because this is just an OTEP and not specification work.
**Reiley** 15:21 Yet.
**Josh Suereth** 15:23 there's a lot to do, so I would say this is urgent, but there's no formal timeline, just the longer we delay, the more likely the browser group will actually be completely blocked.
**Reiley** 15:34 Okay, thanks.
Any comments, questions?
If not, please take a look at the PR this week.
Thank you.
Okay, David.
**David Ashpole (dashpole)** 15:50 Hi, so…
I was kind of surprised when I was looking at the metrics SDK exporters for push, and that they didn't have any way to limit the maximum batch size, like we do for logs and traces.
I…
Yeah, I'm kind of surprised that we haven't… that nobody has come across this yet, so right now I'm actually just looking to see if others… I know Google has this problem, and we would like to be able to limit the number of data points that people can send. I know the collector already has a…
way to limit this in the batch processor. But right now, I'm looking for others who are interested, or have, requirements around this.
The kite.
**Reiley** 16:31 I can share a bit from Microsoft. First, unlike the trace and log exporter, there's no such formal definition of a batch. Like, batch is more like a…
Her expel her thing.
In my mind. Like, we always do aggregation, and at the point of exporting, whether it's pull or push, we'll just, like, stop there, and we'll look at the in-memory storage, so there are a lot of things, and…
I wouldn't call it a batch, this is just an in-memory state. And then the in-memory state can be huge, right? Then you have to take the in-memory state and decide how to put things together in smaller pieces in order to export. And depending on the transport, it could be very different. Like, in OTLP,
I think we should have some limit, because the size of, like, HTTP, networking, timeouts, those things. But for other exporters, maybe that concept makes no sense. Okay, one example in the
Linux kernel, folks are leveraging user events, which is a relatively new thing, like I did a couple years back in the kernel, and user events has very rigid limitation.
So, I think that limitation wouldn't be on the SDK. Instead, it's a per exporter thing. But having that said, I think it totally makes sense for every exporter to have some mechanism so people can put limits, especially for RPC.
Yeah, definitely.
**David Ashpole (dashpole)** 17:59 I don't think it makes sense for pull. I thought maybe it would be generically useful for push, but, yeah, thanks, that's useful feedback.
**Reiley** 18:08 And even for Paul, I think premises don't have this mechanism, but I… I know some operating system primitives, you won't be able to send all the things in one single shot, so you will respond, and you will put an indicator saying there are more, you should come back, and there's some, like, session
management. In the kernel, it's more like you open a kernel object, and that object defines the session, so you know the state. But Promises has no such thing, I think.
Okay, anyone else? I… I don't see…
**jmacdonald** 18:43 I wanted to answer that I've seen this problem in the past, anytime you're using, let's say, a metrics SDK as a sort of funnel for other metrics data. So, like, you're collecting from an old metrics library, and you want to use the new metrics library, and it's just, like, taking in a lot of data, because you've got some sort of concentrator.
You hit the maximum request size very quickly, and there's no solution. Some of you may remember I was working on this thing called LightStep Metrics SDK in years past. It did solve this problem for this reason, and I had done it using collector components, which was, I'd say, a mess, and I wouldn't do it again.
So I bolted on the collector, exporter, and batch processor, and then used the support from those components to get the batching I wanted.
as I was doing that, I worried that somebody might call foul on the whole operation. I mean, somebody, who's that? But the idea that you're splitting metrics arbitrarily
what used to be an entire update was, like, a coherent set of, here's some metrics covering an entire time range. Now you have the potential for half, like, losing half your metric data and, like, not losing the other half your metric data. I worried about that, but I didn't do anything about it.
I'm wondering if you want us to, like, say something like, you may only split on scope boundaries, so you'll never tear apart a scope.
As an example. However, scopes can get too large as well. I'm just thinking out loud for you. Those are just some things I came across in this topic.
Thank you.
**Reiley** 20:23 Anyone else?
**David Ashpole (dashpole)** 20:24 That's valuable. That was all I was looking for.
**Reiley** 20:30 Okay, so, you mentioned the issue. Are you looking for creating a PR, or you're still, like, collecting
Feedback and deciding how important.
**David Ashpole (dashpole)** 20:42 I need to, like, maybe do a prototype before I… Open a PO.
I'm not sure yet where it would make most sense to put this.
I think Josh's points are valid. I do think the…
At least right now, the precedence of
Basically doing things the same way the collector does them.
Has, like, a nice…
consistency to it, so I may look into that path first, and maybe I'll be back next week with a…
a PR or a proposal to run by people.
**Reiley** 21:14 Okay, and one… one thing I remember from seeing some other explore implementation is for the limitation, do you want to limit on the actual serialized, like, size, like, in bytes?
or this is more like a… like, you know in the log and trees, it's possible, we literally say there's a limit of the batch size, like 100 items, 1,000 items, but one item could be huge. Here.
You can imagine a histogram with many buckets might be huge, so depending on which level, we're looking at individual point, or we're looking at some higher level thing, so that might be different.
**David Ashpole (dashpole)** 21:52 Yeah, so I can share that for Google's use case, I just need to be able to limit based on the number of metric data points.
But, that's partially why I'm bringing this up today, because if anyone has… I know that there's a separate issue for literal wire size and bytes that's been open for many years now, I think.
If people have other needs, I'm happy to…
To hear them, and maybe try and come up with something that could address that.
**jmacdonald** 22:25 So you probably are aware that the collector does now have byte-spaced batching.
**David Ashpole (dashpole)** 22:30 I was not, but that's…
**jmacdonald** 22:32 So it's, like, rolling out in a kind of hard-to-follow way, but there's this new support called Exporter Helper, and it's replacing the batch processor. Do not look at the batch processor, please look at the Exporter Helper Batch Sender if you want to look at anything.
But it's way more complicated, and I think every time any one of us looks at batching by bytes, we end up, like… it's just really hard to do that in a nice way.
**David Ashpole (dashpole)** 22:58 Do you know if it supports both bytes and number of elements, or is it… okay.
**jmacdonald** 23:03 Yeah, so they have this new sizer concept. You can batch by size of item count or by total bytes, and you could also imagine batching by request count, though that's a little bit awkward in that place where you find the code, so… But the sizer concept has 3 choices.
**David Ashpole (dashpole)** 23:23 Okay.
Fancy.
**jmacdonald** 23:26 And it's integrated with queuing, so you can queue based on item count, and then batch based on byte count. It's fancy, we'll say that.
**David Ashpole (dashpole)** 23:34 Yep.
**Carlos Alberto Cortez** 23:36 By the way, JMAGD, probably the collector should do some blog posting regarding those nice features, you know, I wasn't aware of that either, you know?
**jmacdonald** 23:44 We talk about batching a lot in the collector, maintainers. We just talked about it yesterday. So yeah, there's work to do, to finish the job.
**Reiley** 23:58 Okay, great. Any last comment?
Okay, let's move to Carlos.
**Carlos Alberto Cortez** 24:05 Yeah, this is just a PR that David Dashboard has, and it has been open for a little while.
This is, per, time series start time tracking.
It has, an overview, so please take a last look. Tyler, if we have you here, and you're here, it could be nice to get your, you know, finalized on that. There was a comment that you left.
And there was some clarification that David, provided. I don't know whether that's enough or not, but it would be great to make progress on that one, because we're very close.
And just to be clear, this is in development, so…
Yeah, if we are good with that, we can start experimenting.
**Tyler** 24:49 So… Can you just say if there is a definition of when The time starts?
**David Ashpole (dashpole)** 25:02 Is… That's a question to me.
**Tyler** 25:06 I don't know, Carlos said it was resolved, I was asking you or Carlos, I guess. Like, that was my concern.
**Carlos Alberto Cortez** 25:09 Yeah, I'm looking for that section, I think it's for you.
**David Ashpole (dashpole)** 25:19 I think you commented on the API spec?
Which… Has a fairly loose def… or no, you… did you comment on the data model?
**Tyler** 25:31 Yeah, so that's not really relevant. I'm not too concerned about, like, where it's defined.
It's more about whether it is defined.
Because I think that we've run into this question before with this exact problem. Like, it's really easy for people to say, like, it's just, you know, you use the start time.
But then it comes down to implementation, and then you have people in different languages defining the start time being wildly different.
To the point that, like, it is not consistent across implementations, so, like…
This needs to get nailed down before we say to everybody, like, this is how the start time is going to be used.
**David Ashpole (dashpole)** 26:06 So the way that this PR is structured is that there's a fairly generic definition in the data model.
Because…
we can't assume that stuff is being collected by an SDK or anything. So it just… I think… I forget what the exact language was now, but,
Something like the earliest possible
No, no, I'm gonna mess it up, but it's repeated, I think, throughout the thread. So there's generic language in the data model that says, like, a start time is…
something about the earliest possible time a measurement could have happened, right? Because it's meant to apply to everything. And that's just copying language that's already there. There's more specific language in the SDK,
that puts bounds on what is allowable and what is not allowable, so…
**Jack Berg** 26:55 Maybe… maybe, David, like, we could add some specific examples for there, because, like, I think the bounds are pretty well defined there, but, like, you know, some language to the effect of, okay, so I'm thinking of a specific case, so you have
a cumulative counter, and you're saying that this one series for this cumulative counter is going to be terminated. And then later, you have new measurements for that cumulative counter, and you're like, hey, what do I set the start timestamp for?
And, like, like, what are the options there? So you say in the spec, like, that the start timestamp has to be
Such that it, which best represents the first possible moment a measurement for this time series could have been recorded. So it could be… it could be that the start timestamp is, like, the timestamp that the series was terminated.
**David Ashpole (dashpole)** 27:50 So, the current… the current spec, right, so we can't terminate series yet, so that didn't make any sense to include here. Okay. So, the current… you can actually see it, Carlos is sharing it right now, it's in the current language is…
When an SDK observes a measurement for a time series it has no record of, it must use a timestamp that is later than or equal to the timestamp of the previous collection interval, meaning
Now, Like, time.now is a valid start time.
And… or if you…
cached the previous collection intervals timestamp, then that's also a valid one. Or, in theory, anything in between, but I'm not quite sure why you would use
One of those.
**Jack Berg** 28:30 Yeah, that seems kind of arbitrary. You're gonna go to one of the bones.
**David Ashpole (dashpole)** 28:33 Right, so…
We could… if people have a preference for being more specific and prescriptive, we could specify that we always use the previous collection interval.
or we can specify that you always use now. The previous collection interval is less accurate, because…
We know that no events happened between the previous collection interval and now, because we're recording the first one.
But it has more consistency with delta metrics, which always use the previous collection interval as the start and the
next one is the end, right? Regardless of when the first observation in the interval happened. So,
If there's a preference, and if people want that to be more specific, we can pick one.
I don't know if there are opinions on the call right now, but… I couldn't…
**Tyler** 29:25 Yeah, I think the company…
**Jack Berg** 29:27 Correct.
**Tyler** 29:27 Specificity of… time now sounds great. I'm happy to… just, like, I…
**David Ashpole (dashpole)** 29:33 Okay.
**Tyler** 29:34 the more specific we can be here, I'm also happy with the collection interval, but I, yeah, like, I do think that, like, having something specific here is going to pay dividends, in the long haul.
But whatever that choice is, I mean, I don't want to, like…
I agree with you, I think now it makes more sense, but I'm also just, like, more in line with, like, it being very specified in that we can avoid confusion of, like, different implementations choosing different things going forward.
**Jack Berg** 30:02 One thought that comes to mind for the now, recommendation is… so I think that in the implementation of that.
Every time a measurement is recorded, you essentially have to do, like, a little check to evaluate if you already have the timestamp for that, if this is, like, the first measurement, and if it is the first measurement, you have to get the current time.
Are there performance implications for those few extra operations that are… that are worth talking about?
**David Ashpole (dashpole)** 30:33 That was…
that was the concern I had in mind. I don't think there are actually any performance implications. Like, usually when the SDK encounters a new series it has no record of, it's doing, like.
a lot of allocating, it's building new stuff, right? It's storing a bunch of…
new things, right, because it's going to start tracking this until at least the next collection interval. So usually there's, like.
Some other things that are going on when you first
Record something for a series, and looking up the current time is not…
expensive compared to that stuff, usually. Yeah.
**Jack Berg** 31:06 Yeah, makes sense.
I buy that.
**Reiley** 31:18 Okay.
So please take a look at the PR, maybe. I think…
**David Ashpole (dashpole)** 31:22 I can make the update, yeah. Thank you.
**Reiley** 31:24 And… And take some improvements.
Okay.
Anything else?
Okay, then we've gone through all the topics. We still have 30 minutes left. Anyone has additional things you want to discuss? Otherwise, we're going to give 30 minutes back.
Okay, thanks, Ara. We'll see you next time.
**Jack Berg** 31:50 Take care.
**Trask Stalnaker** 31:51 Right.
**Carlos Alberto Cortez** 31:52 Nope.
