SIG: Specification SIG
Date: 2026-02-24
Duration: 55 minutes
Zoom Recording URL: https://zoom.us/rec/share/tZ5b3NOrSqcQrFBgGH3mS8erFK5JIEPYPHZb8gG0t1pRLWBTb2xkh7V_rQxgM_B-.WZypOBpV_M9JH2s-
============================================================

## Zoom Recording Transcript

**Josh Suereth** 01:40 Hey, folks!
**Reiley** 01:52 Alright.
**Josh Suereth** 02:15 So, if anyone can add their topics and agenda and name, we'll get started in a little bit here.
Apologies, I'm coming off another meeting that ran long, so I'm a bit, bit slow.
**Jack Berg** 02:35 Hi, everyone.
**Josh Suereth** 02:53 Hmm.
Alright, I think we have enough folks to get started here.
Let's check. Ricardo, you're… you're here, right?
**Riccardo Magliocchetti** 03:10 Yep, hi.
**Josh Suereth** 03:12 Great. I will, do you want me to open the notes, or do you want me to open the issue?
**Riccardo Magliocchetti** 03:18 Please open the issue is enough. Thank you.
**Josh Suereth** 03:22 Okay.
Alright, do you want to talk us through this one?
**Riccardo Magliocchetti** 03:26 Yeah, so… Like, well, first of all, hi everyone, this is my first time participating in with SQL. I'm a maintainer in the Python SIG, so, like, maybe it's… I already know some one of you already.
I work at Elastic, and We are going, like, we are discussing internally on how to… implement, this feature that is here. It's called Controlling Context Propagation Boundary.
That we already implemented in our agent, like, pre-hotel agents.
And so… yeah, like, we would like to move this forward.
And… Yeah, like, I see that this is labeled as a lead sponsor.
I have no experience in doing, like, specification work.
And so… Yeah, trying, like, like, trying to see if there is interest.
In this…
**Jack Berg** 04:46 So, I can give some context about the needs sponsor label.
So, there's a team.
of, sort of, people that are trusted collaborators with the specification, that have done a lot of work in the spec in the past, and they're… this team is called Spec Sponsors, and it's composed of, like, the TC and a superset of the TC, a bunch of other maintainers from across the org.
And, you know, essentially, when we say that an issue means… needs a sponsor, what we're saying is, like, we think that this is a complex enough issue.
that somebody should be involved that has done spec work before. And the sponsor doesn't necessarily need to be the lead.
On this, but they need to… they can be the lead, and if somebody else is going to be working on it, then, you know, they should work closely with this sponsor, and the sponsor should sort of be the first review to make sure everything is kind of coherent and consistent.
With other spec work. So, that's the idea behind Spec Sponsor.
You know, if it's useful, I can, pull up the list of spec sponsors, so… and I don't know, maybe there's somebody you've worked with or interacted with that you think would be a good candidate to volunteer.
**Riccardo Magliocchetti** 06:05 Okay, thank you.
**Josh Suereth** 06:07 So, actually, Ricardo, we're dealing with this right now, ourselves, this problem, and I'm happy to actually be your sponsor, because it's something that I've been thinking about and doing some writing on.
Specifically how to do this, so I'd love to… I'd love to work with you on this. I need to look… I don't know if you have, if this is a proposal or just an issue to work on, but I'm happy to work with you on this. Yeah, we feel this pain a lot, with any kind of SaaS provider, I think you would.
**Ted Young** 06:39 I would suggest for something of this size, it would be creating a project as the next step. This is, like, an old issue that kind of predates some of that.
But it's not just the design, it's also figuring out, you know, who's going to agree to build the prototypes in a couple different languages. Those are some of the things we like to get squared away if we're gonna tackle something like this, just to make sure that the effort doesn't drag out.
overlonged, because we haven't figured out, you know, who's gonna do all the pieces. So…
**Carlos Alberto Cortez** 07:13 I have a small question on that front. Would you say that at least having a small prototype would be enough, or would you like to actually, even before that.
Agree on, like, people ready to create languages in multiple… prototypes in multiple languages.
**Ted Young** 07:30 I… something that I feel like we have right now in OpenTelemetry is, like, a lot of open projects, and we're trying to, sort of.
close the deal on things like graduation and getting everything installed and stabilized and configuration rolled out, and stuff like that. So, something that would be helpful with a project. For something like this, where we would like to do it, we could do it now if there's people available and energy available to do it.
But I would want to know that that energy is available to, like, get the whole thing over the finish line.
With everyone being able to sign off on it actually working.
**Josh Suereth** 08:13 So, we, we should, we should caveat, Ricardo, I actually think that this is going to be a one to two year effort just frankly, like, like, solving this. It's not… this isn't a fast thing, in my opinion. I think, like, I understand what you're saying, Ted. I'm willing to sponsor this in the sense of help you through the OpenTelemetry process, and I think we need to work on an OTEP first.
and then figure out projects from there. Because I don't think this is… this is a simple thing to just throw at OTEL, but also, acutely, this is, like, I need a solution to this immediately.
And we're building things internally to solve this problem. And I don't want to have it be a proprietary thing, I want, like, an open standard around it. So I'm willing to help sponsor this and work with you on what that looks like. Yeah.
**Ted Young** 09:01 And that's another thing, in order to get things done, we're really encouraging projects to try to think of, like, is there, like, a phase one of this project that would be much smaller in scope, but you would get something useful when you completed that first phase?
Right? Maybe there's something like that here, Josh, that… that would be solving that acute need, but avoids the ocean boiling that can happen with this kind of stuff.
Maybe.
**Carlos Alberto Cortez** 09:31 By the way, I had read this proposal in the past, and my impression is that there's agreement that this is needed, but there's… there's no enough discussion about the details, and this is something that Josh and, Ricardo, you would have to work in first, and that's why an OTEB would be a start, because, yeah, sure, there's a lot of information why this is important, why it's needed, but there's no actual, proposal on what would be the details, yeah.
**Josh Suereth** 09:57 Yeah, I'll call out that I think that, like, you're right, Ted, we could probably find something early to figure out here. The real problem we have is whether or not Service A understands if it's crossing a barrier or not. It might not know, and so it might actually be Service B's responsibility to know that something has crossed a barrier.
And that means that we need an interaction that doesn't exist in OTEL today. Like, there's a component that has to understand that. However, we might be able to do some quick wins here, and so I'd love to talk to you, Ricardo, and figure out, like, what you're thinking.
In terms of solving this problem, and figure out, like, you know, how to solve this end-to-end, in the long run.
But yeah, like, in terms of process, just to help guide you, like.
This needs spec sponsor means we need someone who will push it through the finish line. However, like, looking at this again, which I think you saw, it says perhaps this should follow up with OTEP's describing proposal. Absolutely. This is big.
this will impact a good bit of OpenTelemetry and has a lot of gnarly things to discuss. For example, you know, trace ID, baggage ID propagation are still kind of… awkward, I would argue, in our spec.
At least the baggage part. So, I think we need to… Anyway, I'm happy to help guide you with the problems we need to address, slim it down, and come up with a proposal. I might not be able to help you if this turns into a project in SIG, because I'm oversubscribed, but I'm happy to help you get to the point of an OTEP.
**Riccardo Magliocchetti** 11:34 Thank you.
like, by the way, like, I have that comment with, like, like, what… I would like to see, yeah.
So… but we can discuss offline about that, so thank you.
**Liudmila Molkova** 12:05 Ricardo, it sounds like you… Are not concerned about baggage, right?
**Riccardo Magliocchetti** 12:14 Not at the moment, like, not for our use case, but…
**Liudmila Molkova** 12:20 So, custom context propagator.
Would solve the need for you, it seems so.
**Riccardo Magliocchetti** 12:28 Well, we… I thought on adding a custom propagator, But what I'm missing is… like, first, a way to have this upstream, And true, Like, in our previous implementation, we have this detail of, Linking the previous span as the new root one.
And we would like to have also his behavior.
And I don't think I can implement that without, like, having this written in the spec, or at least, like.
It's like, yeah, like, I can introduce this kind of a behavior on the SDK part on my own, so…
**Josh Suereth** 13:22 Yeah, I think you can do this solely with instrumentation, but I get what you're saying, is you would have to, like, if it needs to work with zero-code instrumentation, you need a way to do that, because you don't control the instrumentation in that case.
**Liudmila Molkova** 13:35 Well, you control the declarative config, and you can have an implementation of a propagator that On the incoming request, Instead of using parent-child users link relationship.
And you would configure it on that specific public boundary.
**Josh Suereth** 13:54 I don't think the propagator interface works that way.
Right? Like, I don't think we can control whether or not something becomes a link or not. We just say… we actually just fill out the context with a span or not a span. But I like what you're suggesting, Lyudmilo. We'd have to update the spec to say, you can add a link into context that then the tracer would use when it makes a span to pull in contextual links.
That could work, but that doesn't, like, again, that would… we'd need a spec change for that.
**Liudmila Molkova** 14:30 Or all the instrumentations, yes, you're right. Yeah.
**Josh Suereth** 14:34 Yeah.
Yeah, that's why I think this is a bit bigger. The other thing, Well, anyway, let's take this, and we'll take this offline, and we'll add some comments. I'm gonna put a note… For myself, on here.
To help you out, alright?
**Ted Young** 14:52 I feel like there's actually a couple of different problems buried in this one concept that's part of the thing. There's security boundaries versus interoperation, right? They're two different issues.
**Carlos Alberto Cortez** 15:06 Yep.
**Josh Suereth** 15:14 Alright, so, Ricardo, I'm gonna say that we have a lot of follow-up there, and I'm gonna move on to the next topic, unless you had any other questions.
**Riccardo Magliocchetti** 15:24 No, it's fine, and thank you again.
**Josh Suereth** 15:27 Great. Alright, Carlos, do you want to talk about, stabilizing optional exception parameter?
**Carlos Alberto Cortez** 15:32 Yeah, these two ones are just for your information. The first one is something that was already merged last week, but we were talking about letting maintainers know, this is a new parameter, you know, passing an exception to the logger remit operation.
It's stable, so that's important for you maintainers, and unless there's a problem, we will include that in the next release for March, which should be in one or two weeks. So it's important for you to know.
Yeah, I think it's trivial.
From a review perspective, as you can see, all the approvals, but yeah.
Please, take a look.
The second PR is similar, because it's a PR that David Dashboard has been working on for a long time. Yeah, that one. It's basically, it's an in development section, but still important.
For, per time series start time, it's a change.
And, it has been discussed for the last 4 to 6 weeks, I think.
And it has enough reviews and all that, so we would go ahead and merge that today. We were waiting for the last days, so unless there's feedback, we would like to merge this after the call, or now, or whatever, you know?
Okay, that's all… that's all we said, yeah.
**Josh Suereth** 16:54 Yeah, we're… there… so you said it has enough approvals, and there's no… there's no, concerns on it left, right?
**Carlos Alberto Cortez** 17:01 Yeah, the concerns are, like, just… stuff that is passed, and maybe CEO, I saw that I… yeah.
I was asking CEO a few weeks ago, but he forgot, but I think that his issues were solved. We have CEO here.
Probably no can just… Yeah, you can just…
**Josh Suereth** 17:21 Just here, let's do a quick check. I don't know if he's here, though.
**Carlos Alberto Cortez** 17:25 No, he's not. No, I confused him, yeah. Okay, yeah, well, let's ping him, and otherwise… I mean, honestly, it's in development, we were, my impression is that, I don't remember the details, but this was, like, 4 weeks ago that I was reviewing that, or 3 weeks ago, but yeah, we can ping him just in case. Otherwise, we are good to go.
**David Ashpole (dashpole)** 17:47 Awesome, then…
**Josh Suereth** 17:48 Just waiting to see if anyone had anything they wanted to say.
**David Ashpole (dashpole)** 17:51 I was gonna move on to the next, next topic, if there's nothing else.
**Josh Suereth** 17:54 Yep, let's go.
**David Ashpole (dashpole)** 17:56 Cool.
So I'm reporting back, I think a couple weeks ago, I talked about batching in the metrics SDK, so we at Google would like to be able to limit the number of metric data points that are sent in a single export.
OTLP request.
So that we can… basically accept metric data from OpenTelemetry SDKs.
And, so I've done some research, my notes are in the issue, but the TLDRs that we can… Add a match export batch size configuration.
To the periodic metric reader, is what I'm proposing. This'll largely match the behavior of the trace and the logs SDK.
And match the behavior of the collector.
batch processor and batch exporter helper. So, I've mostly focused on… like, you can do batching in a variety of places, so I've mostly focused on making sure that this is consistent with the other signals and with what the collector does.
But yeah, there are other options if this one turns out to be problematic, but I'm mostly looking at this point for, other languages to… chime in if… if they don't think that this… that, the periodic exporting metric reader is the right place for them. And thank you to the people who've already provided feedback.
**Jack Berg** 19:27 I'm gonna dig into this, David, at least your details, but while we're synchronous on the call, I just maybe… I'm gonna ask a potentially obvious question.
**David Ashpole (dashpole)** 19:37 Go for it.
**Jack Berg** 19:38 Maybe other people have the same one, just so we can have a little discussion. But, so… What… so, okay, you have the periodic reader, it's reading these metrics, it has too many metrics to fit in one batch.
And so what's it going to do? Is it going to spin off, like, several requests to the delegate exporter?
Sequentially or in parallel?
**David Ashpole (dashpole)** 20:04 sequentially. So, the reason… The main reason for that is that currently the spec says that exporters Must not be called concurrently, so, we would have to… Open a large can of worm if we wanted to go that direction.
I… it for… the purposes that Google needs this for, sequentially should be just fine. It's just someone has 350 metrics, and we just want them sent in, you know, two batches instead of one. Like, I don't think anybody… at least the use cases that I'm trying to meet are not, like.
we need to send a million metric points concurrently in, you know, some super high throughput thing. This is just, like, we have the data, we want it… we need it split up in order to accept it.
**Jack Berg** 20:54 That's not to say that we couldn't do that in the future.
**David Ashpole (dashpole)** 20:56 But, like, I think that this is, like, as a first step, the simple, easy one to give a match.
Max batch size.
**Jack Berg** 21:04 Okay, and so by default, the batch interval is 60 seconds, and so unless you had to split it up into many, many, many batches, or you had, like, a really high latency connection, it would probably… you're probably not going to run into issues with, you know, the export requests interfering with the interval.
But suppose you do have, like, sort of, like, adversarial configuration, either, like, a tiny batch size or a small interval. What's the behavior when the, when the, like, sequential exports start to bump up against, like, the target interval?
**David Ashpole (dashpole)** 21:43 I think it's the same today if you somehow had an endpoint that took more than the target interval in terms of latency, right? Like, if you had a request that has a trillion metric points, and you sent it somewhere, and it tried to process it for some reason, like, if it came back every 3 minutes, then, yeah, you'd end up behind.
And presumably, that would just delay… Ideally, the SDK would simply delay the collection interval.
Okay. As a result, right?
**Jack Berg** 22:11 So the SDK sort of waits for the in-process export or exports to resolve one way or the other until it tries the next one?
**David Ashpole (dashpole)** 22:19 Yes, it should… there are a few sub-goals here. One of them is that we don't, like.
change the ordering of stuff, so I wouldn't want, like, export number… or, like, collect number 2 to start sending… like, I don't… I don't want… Different collection intervals to necessarily be, like, competing with each other.
for export space. So the idea is that just, you get your batch, you split it, you do them sequentially, and then whatever lock you're holding, or whatever on the exporter you release, is the way that I'd like to see this.
**Jack Berg** 22:55 Final question, what about… Is there any sort of language or thought or things we need to think about for, partial successes, right? Like, if some of the export requests succeed and some fail.
**David Ashpole (dashpole)** 23:14 But… I did look at the partial success language.
It's pretty light on the SDK side. I think the Go implementation just, like, logs a partial success message.
I can take another look, but I think as long as, like, Things are counted properly in… the self-observability metrics and stuff, I don't see any big issue with partial successes.
**Jack Berg** 23:39 Okay. Yeah, I don't either off the top of my head, and we treat partial successes, like, so loosely in the SDK, where we don't really do anything about them, we just, like… because there's nothing that's, like, really actionable, we just try to have, like, a footprint or a fingerprint in the logs that you can detect.
But yeah, I was just wondering if you had done anything additional beyond that for this BR.
**David Ashpole (dashpole)** 24:00 So I… in… at least in the Go prototype, I was able to just leave, like, almost everything the same, and just… Add a split, and then extra export calls.
Yeah, everything else seemed to just work out.
Rightly.
**Reiley** 24:15 Yeah, so first thing, I think partial success is orthogonal to this particular problem. Like, we would have the same problem if we sent that in a single big batch.
Secondly, I remember the current wording in the spec literally gave the, like, the retry and all this handling to the exporters. So the SDK essentially just called the exporter once and say, here's the data, your problem, and the exporter can decide, based on the protocol, what to do.
And the partial success is, like, partially defined for OTLP. So, you won't know there's a partial success, but if you want to look into the response and see, for the list of items I sent, which one is considered a success versus failure, then you probably don't have those details.
**Jack Berg** 25:03 Yeah, right. The periodic reader doesn't have those details, right? They're… they're obscured from it.
**Reiley** 25:09 Yeah, so the SDK entirely, like, it doesn't have the detail. It simply calls the exporter. The exporter would tell the SDK whether it acknowledged the problem or not. So the return value is essentially like a boolean, like yes or no.
If yes, then the exporter is accountable for all the data. So if there's partial success, the exporter wants to do some, like, partial retry, whatever thing, that's the exporter's problem.
So from the SDK perspective, it's literally, I gave you the problem, you acknowledged, then it's your problem, or you said no, then the SDK will say, okay, then I'll, like, internally log it, but I'm not going to retry anything. That's the current spec, I think.
Josh?
**Josh Suereth** 25:53 Yeah, I was basically gonna say the same thing, like, We… you know, the exporter can retry on failure, but we kind of designed metrics so that you can just drop data points and send them later, like for cumulatives, for example. The data comes later, so that's fine. If you're using deltas, you probably want to have a higher retry. I think as long as you have the configuration parameters in there, I think that's the important bit.
And I believe we have all of those anyway, it's just how you fragment them into each batch.
Probably just needs to… I don't know if you… I didn't look at your spec, but if it's already called out, it's great.
**Jack Berg** 26:32 This all sounds reasonable to me. Thanks for the discussion, David.
**David Ashpole (dashpole)** 26:36 Yep, thank you. Appreciate reviews.
**Josh Suereth** 26:43 Cool.
Alright.
I think that's it for the agenda on the books here.
So, Is there, anything folks want to discuss? We have another 30 minutes. I am happy to call it early, but I wanted… we had a good random discussion last time that we brought up, wanted to see if anyone had issues, concerns, things they want to discuss, things that they didn't put on the agenda because it was too formal, or… Anything like that. Go ahead, Riley.
**Reiley** 27:18 Yeah, just one minor thing, I want to continue the discussion about partial success. So I want… I want to know, like, from… from the community, how much interest would there be?
for, like, a better handling of partial success. This is around, like, people want to send telemetry from the SDK to the collector, then to some backend, and they want to see better data delivery. So currently, like, we literally have no promise or anything. Like, if you ask what's the expectation? Nobody knows the expectation, right? So, the ask is not to build a fully transactional system, like a SQL or something.
but somewhere in the middle where people can have certain expectations. And one thing you can imagine is in OTLP, if I send, like, 1 million items in a batch, I want to know which item has been successfully delivered and which item is not.
then I can retry. We… we currently don't have such information. We're just saying, like, if there's a partial success, you give an indication, and that leaves the option for the exporter to either decide to retry and deliver the entire batch, or not retry at all.
So it doesn't have the granularity to see amount of 1 million items, only, like, 1,000 filled, and for the individual items, which one should I retry? The answer might be, hey, for this item, the value doesn't make sense.
It's a… it's a wrong thing based on the data model or semantics, so you shouldn't retry. It's just like a bug in the SDK. Or, oh, the data, although, like, makes sense, but we have throttling or something, so you'd better retry later.
we… we don't have such information, and I… like, I think in Microsoft, people build a lot of solutions on top of OpenTelemetry using the extensibility. So that's not a blocker for Microsoft, but based on the customer's, needs, and… a lot of, like, internal need in Microsoft, I… I wonder if that's a common thing for other folks.
My guess would be yes, but it's kind of surprising, like, we haven't spent much time on this.
Okay, I'm done.
**Josh Suereth** 29:22 Jack, did you want to respond to that, or did you have another question?
**Jack Berg** 29:25 Separate, separate topic.
**Josh Suereth** 29:27 Okay. I wanted to add something, Riley. In our experience, handling the data is actually somewhat dependent on the use case. So, we have situations where you need to retry at all costs.
Or, not at all costs, but, like, there's a high value to the data. Audit logs, for example, people try to put them on the logging signal.
That one, you're more sensitive to. Certain metrics are more important than others. Some metrics… freshness is more important than anything. So if you retry, and you send a stale point that is worse.
Than just sending the next point.
And so, like, I don't think there's a zero-sum one way to handle this.
with partial success, and I think what you, what you see in OTEL is folks that, are okay with, like, freshest wins all the time are very successful.
Folks that need guaranteed delivery may struggle a little bit more.
And by guaranteed delivery, yeah, I know there's no such thing, but a high resiliency bar on getting things through, right?
**Reiley** 30:37 Yeah.
**Josh Suereth** 30:37 My opinion here is I'd like to see us have a, kind of… kind of a configuration-y experience of, like, I can say, this stream is really important, this stream is less important, and I have the controls to deal with that and adjust that, but I wouldn't say, Yeah, I wouldn't say that, like, we should improve partial retries, like, blanket for everyone, because even… even for the same OpenTelemptry SDK, like, in our experience, you can have some metrics that have a higher need than others for export. You can have some logs that have a higher need than others, and our ability to kind of handle that makes sense, you know?
I love… Ted, you should say that out loud.
**Ted Young** 31:29 What, that we… OpenTelemetry guarantees delivery, or your money back?
Yeah.
**Josh Suereth** 31:35 Yeah.
**Ted Young** 31:39 Talk to your vendor to redeem your coupon.
**Reiley** 31:53 Yeah, so Josh, like, in Microsoft, we're doing something similar to what you described, like, per stream, there's a different, way of, like, balancing the cost and the return. So for all the logs, we also, like, do… much higher, like, some telemetry are used for audit, for maybe, like, marrying the usage, and for troubleshooting. So, like, for anything that you require a proof of delivery, that, those streams, you're willing to spend more money just to get a better delivery.
like, SLA or something.
But for most of the logs, like, the default behavior is you try to optimize for a cheaper delivery option, and there's no guarantee. I think it's very similar to the… to how people deliver, like, mail, or, like, any, like, real-world delivery service.
**Ted Young** 33:01 Jack, you've had your hand.
**Reiley** 33:02 Jack, you've been…
**Jack Berg** 33:04 If we're ready to switch topics, I can go, but if anyone has any additional comments on that, you know, I think, you know, my summary of that discussion is, hey.
Is there enough people that are interested in, you know, additional delivery types of guarantees that want to get together and talk about how we might make that happen?
I hear Josh and Riley.
**Josh Suereth** 33:29 I'd also say that audit logging OTEP, Riley, you might want to reach out to them, because that was one of the things called out in that OTEP.
**Reiley** 33:38 We said no to them, so…
**Josh Suereth** 33:41 I mean, if you're looking for people who want that capability.
That would be the people, that I would say I would also reach out to.
**Reiley** 33:51 Yeah, I know SAP is interested, and I know in Microsoft we kind of delivered some solution on top of OpenTelemetry using extensibility, so we're not blocked at all.
And we're happy to contribute back if there's a broad interest. I just don't know if there's enough interest. Previously tried. The answer is no. There's not much interest besides companies who deal with, like, online transactions like ISAP.
And I'm fine if there's no such, like, interest.
**Josh Suereth** 34:24 So, Riley, I think it's more accurate to say there's interest, but there's not enough to top any of our existing priorities at.
**Reiley** 34:30 Right.
**Josh Suereth** 34:31 So, like, I… if we were keeping a roadmap that lasted beyond a year, I would have that on the roadmap somewhere, personally. But, like, I think there's… Other things that are… that are either you can't work around or can't do at all that are higher priority.
**Reiley** 34:49 Right.
**Josh Suereth** 34:54 Cool. Let's… let's move on to Jack, then. You want to talk about, next State of X presentations.
**Jack Berg** 35:02 Yeah, so last week's conversation, the agenda was thin, and we kind of had this impromptu update, status update, from the entity SIG that, Josh, you gave. I think I also talked longer than I should have about configuration, because I was talking about stabilizing that. But yeah, those turned out to be sort of impromptu status update style things, and we were riffing at the end of the talk about how we like that. It's for all the SIGs that that are spec sub-sigs.
It'd be good for them to loop back in into this parent meeting, and… you know, kind of socialize ideas and status with the rest of the maintainers and the specsig participants. And so, yeah, I'm kind of social… soliciting people to volunteer to do the next update, because I did like that idea.
Some… I'm in the community repo right now, and I'm scrolling through the other specs, and a couple of them that, I think would be good to hear from, I listed here. So, Prometheus interoperability, I know Prometheus, that group, is looking to stabilize some concepts. Like, what are you looking to stabilize? What are the blockers? What's your timeline for that? That would be good to hear about.
Opamp, you know, some of the things I've been hearing about with OpAmp are like, hey, we know how to control the collector with OpAmp, should there be standardization around controlling SDKs with OpAmp, and how does that interplay with this sort of telemetry policy, Zotep, that Josh opened up?
So that's, like, a cool topic that I think we could talk about.
Profiling. One of the hot topics right now is, should there be sort of reference-based, attributes in OTLP to accommodate profiles, high data volume and make it more compressed? So this is sort of like application level or protocol-level compression instead of, like, you know, generic GZIP-style compression. So that, that's a, A topic that I think the community could benefit from hearing more from.
Logs. What's the… what's the state of logs? We got a… we have an event API, log API, that is used for events.
We have stable record exception operation. What's next? What do we still… what are the things that we still need to do there? Sampling. One of the things that I'm familiar with in the configuration SIG is that there's this rule-based sampler that's pretty awesome, right? So, it allows you to do things like identify traces or spans that are low value and, you know, define predators advocates for accepting or rejecting them, and ties in with the trace ID ratio stuff and W3C Level 2 sampling. So, yeah, that'd be good to hear about and to get implemented in more places. And then finally, SEMCOMF. Like, what's the roadmap for SEMCOMF? Like, what are the conventions that are going to be stabilizing soon that other maintainers should hear about?
And be looking forward to updating their instrumentation to reflect. So, those are the ideas that came to my mind. If anybody could volunteer on the spot, that'd be great. We could see the… we could see the next conversation now.
**Liudmila Molkova** 38:11 I went to volunteer for RPC SEMConv. We reached RC status recently, and we're looking To stabilize as soon as we have.
Prototypes and feedback.
It seems, Trask, you support this?
**Trask Stalnaker** 38:29 Oh yeah, I'll be there.
I also wanted to volunteer us for, logs.
events.
**Liudmila Molkova** 38:41 Yep.
**Jack Berg** 38:43 Alright, and I see in the chat, Florian has volunteered to talk about profiling, so, so, okay, we don't want to do this every SpecSIG, but we talked about how we could do… these kind of on a more frequent basis, initially, to kind of catch the community up, and then kind of revert to some sort of more reduced schedule, like once a month or something like that.
Do we want to tentatively have a conversation like this next week, and who would volunteer first?
**Liudmila Molkova** 39:21 I can listen to it for… Oh, go ahead.
**Josh Suereth** 39:24 Go ahead, Lunella. If you're volunteering for next week, go for it. I had one comment about the next 20 minutes, but go ahead.
**Liudmila Molkova** 39:33 I would volunteer for RPC next week.
**Josh Suereth** 39:40 I was gonna suggest, Florian, if you're here and you're okay with this, the profiling protocol proposal is, we're, like, literally almost through the finish line of getting it in and getting it into alpha, or beta, or, you know, some kind of status. So it might be… I think it'd be worth, Florian, if you walk through what you've done.
what year… the proposal is on the collector, and how it works, and kind of the benchmarking, numbers that we're seeing around it. Would that… would you be comfortable with that?
**Florian Lehner** 40:13 Yeah, sounds good to me.
**Josh Suereth** 40:15 Okay, so not all of profiling, just specifically the protocol stuff. Cool?
**Florian Lehner** 40:22 So next week, Luke Miller, if I follow correctly, and the week after that, then profiling and reference-based attributes, right?
**Ted Young** 40:32 That's it.
**Jack Berg** 40:32 Sounds great to me.
**Florian Lehner** 40:34 Perfect, thanks.
**Jack Berg** 40:50 I'm gonna go ahead and update the meeting notes docs to fill out the agendas for a couple of weeks in advance, just so we have these notes items queued up.
**Josh Suereth** 40:59 Sounds great.
I also want to call out anyone who is interested in OpenTelemetry's protocol, there is a active PR that I would like to merge relatively quickly, but we're waiting for, two more approvals, from folks on travel.
And, that is actually committing to the, dictionary-based portions of the protocol. There's a bunch of stuff that Florian's done in the collector, a bunch of benchmarking, I, like, we'll review it and explain to everyone what's going on there, but if you want to actually see what's happening and make comments prior to it getting merged fully, please, please do so now. Because that PR, we're down to, I think, the last complaint.
and I think it's resolved, we're just looking for confirmation, and then I'd like to get that thing merged.
Thank you, Flora, and I'll throw that in the notes.
Hey, That might be a good stopping point, then, unless anyone has any other topics.
**Daniel Dyla (Dynatrace)** 42:32 Yeah, given that we have 20 minutes left, and I think this will only take, like, 3 of them, I wanted to quickly talk about the Trace Context Level 2.
Because there… I mean, there isn't a spec sub-sig for this, so… NET was looking to implement it, and because of the way .NET OpenTelemetry works, they needed to make runtime changes.
The OpenTelemetry specification says to implement Trace Context Level 2, but Trace Context Level 2 is still a candidate recommendation. It's not, like, an official recommendation yet.
A part of the W3C process is to have implementations in the wild.
Before you can call something a recommendation.
In this case, I think it's very unlikely to bite us.
But I would say… for the future, we should probably be careful about adding dependencies on, unstable W3C recommendations in stable documents, which is the situation we're currently in.
The W3C does not require those reference implementations to be stable. So it would have been totally fine for us to just have some prototype implementations.
That said, I think this case in particular is very unlikely to be a problem.
And… to be completely honest, open telemetry has more momentum than the W3C group does in this case.
So, if the W3C group made a decision that this group didn't like, They would have… Little to no power to force it through.
it's, you know… Hopefully, it would never come to that, but it is the reality.
And I also don't think there's likely to be a change like that. So for both of those reasons, I don't think it's likely to be a problem.
But I guess I'll just call this a PSA, for, that type of situation.
Yeah, Josh, you have your hand raised.
**Josh Suereth** 44:56 Yeah, for context, if I understand correctly, the main difference here is we're passing 2 bits instead of 1 bit.
In the specification, where one of the bits represents the randomness, but the specification previously required a byte to be sent, right? So, like, what are the odds that another language actually isn't passing along a full byte, and is instead passing along a full bit?
**Daniel Dyla (Dynatrace)** 45:20 The previous language said that any unknown flags should be set to zero.
So, if they're passing it through And don't… if they're an old implementation, and they're passing it through unmodified, they're not specification compliant.
**Josh Suereth** 45:40 Interesting, got it.
**Daniel Dyla (Dynatrace)** 45:44 Although, in this case, that would be fine.
**jmacdonald** 45:50 Yeah, and in this case, we had to just work around that behavior that was just described. Like, we can't really rely on that bit until every SDK, all the instrumentation in the world is upgraded to this new specification, which is pretty unrealistic. So we went ahead and wrote language in our spec, again, like Daniel described, like, just kind of moving past the W3C so that we could get what we need to work… working.
And so I would… I would just recommend that we move forward and… and… and sort of count on the W3C to ratify what they've got.
**Daniel Dyla (Dynatrace)** 46:25 Which I think is very likely.
Also, I guess I'll say in the interest of, Full disclosure, the W3C group has been… It is notoriously slow, and has been even slower.
there's not that many people showing very active interest in it, so… Yeah, for whatever it's worth, it's just a very slow group.
**Josh Suereth** 47:05 Cool.
I mean, not cool that it's slow, but cool that, I think we're… we know what to do here. Awesome.
I'll tell us captured as you trace context, in other words, yeah, okay.
Cool.
Let's, let's call it. What do we say? Anyone have any other topics?
**Ted Young** 47:26 Maybe not to dive in here, but, like, I'm excited to get these report backs from different SIGs. I feel like we have some more general organizing we need to do to meet some of our goals. I think it's, like, the GC's job to figure out how to promote that and structure that, but I think this is, like, our community meeting.
And so, we don't have to go through it all now, but one thing that I know is right on our horizon is, like, stabilization.
Right? Like, we have a bunch of SEMCOM we're trying to stabilize, but then we're also trying to, like, clean up and stabilize Contrib and get instrumentation.
up to date.
And kind of signed off on. That's something, like, project-wide that's helpful and, like, part of graduation. And it feels exactly like the kind of things we don't really have, like, tools to organize around, because it's, like, cross-cutting in a way that we're normally very independent.
So… How do we actually do that?
**Jack Berg** 48:35 This seems like a great call to give that type of update, and, like, where there's spec subsigs for some of these other topics, maybe the GC could take responsibility to come and give an update on graduation slash stability.
**Ted Young** 48:48 Yeah. Okay. I can, take, why don't you put me on the list for that, then?
**Josh Suereth** 48:58 If we have room, I'd love to hear about that next week, even.
But I know that that's a rush.
**Ted Young** 49:06 No, I mean, we can certainly talk about, yeah, I mean, I think we… if there's time next week, I can at least… Start slipping portions of this into our agenda.
**Josh Suereth** 49:17 Yeah, honestly, what do you think about just having… like, we used to do this when we had important sub-sigs, where we had an agenda that was, like, predefined with, a time box. Like, we had metric SIG timebox at one point.
To deal with metrics-related problems. I think graduation's kind of important enough that maybe we should just have a constant status update every week, and if there's nothing to say, great, we'd skip it. But, like, it'd be nice to just constantly get a refresh for us to know that we're driving towards it as a community.
**Ted Young** 49:50 You know, I think that's reasonable, and I also think it's not gonna end with graduation, because a lot of what y'all were talking about earlier looked to me around, like.
configuration, basically control plane stuff, and that's another area where we're being very piecemeal right now, but once we've got open telemetry in a state where you just install all of it, it's like, step one, you have all of OpenTelemetry, bam! Like, the operator or whatever is just giving you all these things.
And then our expectation is you would now manage all of that stuff through op-amp and a control plane.
But we've never really, like, sat down and coherently described How we think all that should work, and, like, what do people really want to control, and blah blah blah.
So, even after we get through all of our graduation stuff, I still think we'll have some of these bigger topics where it's not… I don't… maybe we end up spinning them out into projects, but I think we should start by talking about them as a big group.
**Josh Suereth** 50:49 Yeah, yeah, yeah.
But… but I'm thinking, like, things that, So, twofold, and I'll end this, because I'm being chatty. I love that we're doing sub-sig updates, where we're going to have an opportunity for SIGs to update. SIGs that are close to, like, releasing something, or that need a lot of integration across the board with other SIGs.
giving them dedicated sections here to talk through, like, what they're doing, and needs and where things are. That's kind of what I'm thinking. And right now, the graduation process, I think, involves a lot of stuff.
And so having just a place where we can actually just talk through it here, where, you know, this is dedicated for all the maintainers, folks in the spec, all the SIGs, this is a place where we can do a little bit of coordination to kind of talk through those things, just to, grease the wheels on getting this stuff out the door. That's my thinking.
**Daniel Dyla (Dynatrace)** 51:46 I was gonna ask…
**Josh Suereth** 51:48 Good.
**Daniel Dyla (Dynatrace)** 51:49 Is this the right meeting for that, or should we do the maintainer's meeting?
**Jack Berg** 51:53 Maintainers meeting got merged into this.
**Josh Suereth** 51:56 This is the maintainer's meeting now, Daniel, yeah.
**Daniel Dyla (Dynatrace)** 51:59 Oh, yeah, I'm sorry, I was… I was thinking of the Monday meeting, which is a SEMConf meeting. Sorry, I apologize for my morning brain.
**Josh Suereth** 52:08 No worries. But we… it's a great question, which is one reason we merged the maintainers meeting with this one, is so we had a meeting to do that kind of stuff.
And, yeah, and this is supposed to be it, so if this isn't working, that's good feedback, if, if, if folks don't feel it is. I'm only 6 months behind.
Cool. Great call-outs. I'm gonna call it here. I think this is… this is great discussion. I'm glad we had room for some of these, these things, you know, top of mind type things. And, next week, let's look forward to hearing about, a little bit about graduation, and a lot about RPC.
**Jack Berg** 52:50 Sounds good.
**Josh Suereth** 52:51 See y'all then. See ya, bye.
**Trask Stalnaker** 52:54 by…
