SIG: Collector SIG
Date: 2026-04-01
Duration: 49 minutes
============================================================

## Zoom Recording Transcript

**vojta.vojacek** 01:00 Hello?
**atoulme** 01:04 Good morning.
Alright, put your name down into this document.
If you'd like anything to discuss today, make sure you add it to the doc, into the agenda.
**Perk (Marcin Stożek) | Elastic Ingest** 01:47 Yeah, how are ya?
**atoulme** 01:48 Hey.
**Perk (Marcin Stożek) | Elastic Ingest** 01:53 Did you get your cube cold last week?
**atoulme** 01:57 Aye.
I did. I'm still recovering.
**Perk (Marcin Stożek) | Elastic Ingest** 02:00 Yes, I'm here.
**atoulme** 02:04 It's not that bad. It's like not… not a COVID, right? I've done worse.
**Perk (Marcin Stożek) | Elastic Ingest** 02:09 Fair enough.
**atoulme** 02:09 It's been, like, a good COVID after the conference.
So, joining everybody? Okay, so again… The dog is here.
You can write down your name, and you can add things that you'd like to talk about during this time.
We'll get studied in 15 seconds.
We'll just go from there.
Is Dekuta here?
Alright, and also Dakota here. We're gonna go through that item first.
We'll do a straight-through.
So, Dakota here has an item open, which is new log-specific component telemetry Measurement, and there is an issue here pointing to the OpenTelemetry collector.
**Alex Boten** 03:10 They just… they just joined.
**atoulme** 03:13 Hello, Dakota, how are you?
**Dakota Paasman** 03:15 Hello. Sorry about that.
Running a couple minutes late.
**atoulme** 03:19 Alright, enough time. Would you like to tell us about your issue, please?
**Dakota Paasman** 03:23 Yeah, yes, I would. So yeah, my issue here that I've linked, yeah, so… Basically, in this issue, I'm describing.
I think that there is a… There's a gap in the current component universal telemetry mechanism.
Around measuring the size of the telemetry data flowing through the collector.
I think the gap resides with the… with logs.
So the issue being, with metrics and traces, you know, those are signals generated into the OTEL data model.
You know, it makes sense for a metric to be defined within P data. Same thing with traces.
And measuring the size of that, you know, it makes sense. However, when we're measuring the size of a log, You know, the blog has a source that's outside of the hotel collector, And measuring the size of a log.
is not as accurate when you're measuring the size of it when it's wrapped in the P data structure.
And so this issue is just, you know, highlighting that issue.
Or that problem, and proposing a solution for how can we get a more accurate measurement of the… Log data being collected by the supervisor. Or, sorry, not by the supervisor, by the collector.
And yeah, that's the, you know, general summary of this issue. I proposed a solution.
Where we add a new metric to the universal component telemetry, specifically for components that are handling logs.
where we are, as, like, a best approximation for getting, like, a measurement as close to the actual log size as we can, we're going to measure, the bytes of the log body, rather than the entire log P data structure.
Yep, that is… the context around this issue, and I just wanted to bring it up here to try and get some discussion and community buy-in on this.
No.
At the very least, acknowledging that this is a problem.
And then we can work on a potential solution from there.
**atoulme** 06:07 Okay, any feedback, folks?
But I get two pieces of feedback for me. One is, naming is hard.
Hume… You have here… A number of namespace metrics, which are using dots.
And then you're using underscores.
For log body size.
**Dakota Paasman** 06:40 Sure, yeah.
**atoulme** 06:41 That's gonna be a bit of an issue. Is it size or length?
We'll sell some good.
You're transforming the body into a string. The body doesn't have to be a string.
That could be an issue.
So, you should try that with the map, and just mess up with it, and see if you like the results.
**Dakota Paasman** 07:04 Okay.
**atoulme** 07:07 Is there a way to get the size of a body in bytes according to some simple calculations? I don't know.
Yes, are we counting bytes, or are we counting runes? I'm guessing you want to count in Bytes.
Yeah. That would be the unit of this type of metrics, right?
Yeah.
So I think that would be the type of things that we would look for in this. The fact that it's detailed and it's not enabled by default, making it an opt-in behavior.
Makes it easier to accept, right?
To me.
**Dakota Paasman** 07:39 Sure, yeah.
**atoulme** 07:41 Yeah, a few miles away, then.
Looks good.
**Dakota Paasman** 07:44 Okay. Yeah, Mikolai.
**Mikołaj Świątek** 07:49 I would also ask how expensive this actually is.
I recall that various… Attempts at measuring the sizes of all of data passing through the collector in the past have sort of been blocked a little bit by the fact that it's not that cheap to determine.
How big something is, and the body as string in your example implementation is also setting off some slight alarm bells that If you're… if we have, like, logs which are really just nested documents passing through it, then what you might be doing internally is just serializing it to JSON every time, and that's, like, a non-trivial cost for whatever's going in there.
Yeah. So… Yeah.
That's not necessarily a reason to say… to say that we can do it, especially if it's opt-in, but we should have some sense of how expensive that actually is.
**Dakota Paasman** 08:44 Okay.
Cool alright, cool. No, that's all… Very valuable feedback, thank you. I will… yeah, take that and work through it on the PR, or work through it on it, and try and open it.
A PR.
**atoulme** 09:07 Yeah.
**Dakota Paasman** 09:08 and JMAC, the bite-sized method, yeah, I'll make a note of that as well and look into it.
Cool, that's all I… That's all I really have.
**atoulme** 09:19 I'm gonna comment up on, on the issue, based on our discussion. So, just a few things.
**Dakota Paasman** 09:26 Yeah, thank you.
**atoulme** 09:28 Sure.
All right, next up we have Mike. He's going to talk about the new component proposal for log drain. Mike, in the room with us. Yes.
**Mike Goldsmith** 09:38 Hello, everyone. Yeah, so this is a new proposal for a new log-specific component. It's specifically around doing, templating or pattern matching around logs that come through.
Excuse me, I've got both an issue and a reference PR. The issue describes what the problem is, how it works, what sort of benefit you can get from it. Big work… like, the workflows that are… I think, are impactful is that it can… Identify what log matches are, so then you can do some sort of filtering before it even has egress out of the collector, so if it's running in an infrastructure before it goes anywhere else, you can drop things that you don't care about that have got pattern matches in there.
Another one is that you can maybe do some analysis on it and maybe do some regexing on it, so if you've got, like, a flat body, you can do a template on it and then start pulling things out of it. So there's a few different use cases for it. It's based on the Python implementation, so I think the only thing in my reference PR that is a little unusual is that it's on an older… package. The package… it probably should need some… some work on it. I think the main thing that I wanted to bring up was, like, is there community interest in having this type of component there?
And then I'm looking for, like, community feedback on if it's something that people want, and if there's a sponsor for it, because I haven't got one of those yet, so it's just to try and raise awareness on it, and the reference PR is just sort of, like, show what it could look like, what it could do.
I think, from where I've seen it used is, I know something like, Loki does this, Loki on Ingest can do pattern matches.
So that was, like, one of the bigger ideas of, like, they've got their own, AGPL license tool. This would be… we couldn't use that, obviously, in the collector, so that's why we used a different package in the reference thing, but that's the idea of doing that sort of a pattern matching, but do it at the collector side.
**Mikołaj Świątek** 11:56 So I have, not necessarily, maybe two questions, or maybe two… Things that… Because this is the first time I'm looking at this issue.
Yeah, yeah.
**Mike Goldsmith** 12:06 I'm not in a… I'm not in a rush, so obviously, for feedback, welcome to have a look through it. There's quite a big issue there to read through in the reference material. Antoine, I think you might have been saying something, but I think you were muted as well.
**atoulme** 12:19 Oh, wow, okay. Yeah, questions for you. So… Another thing is that you are going to pattern match a number of logs against, static patterns, right?
And.
**Mike Goldsmith** 12:32 So it's a learning tree model, so as it… so it goes through the model, it'll do a… it'll read the tree and then try to figure out how many times it sees something and see where the variations are, build a tree map from that, and then once it's gone through a training period of time, the number of times it's seen things, then it can start to say, this is the template that I… that I believe it to be… to match against, and then it would add that as an attribute.
**atoulme** 12:55 Oh, interesting.
So, is it, learning over a window of time, and… Is that… that is… The max buffer for logs would be 5,000, for example, also your…
**Mike Goldsmith** 13:08 Yeah.
**atoulme** 13:09 Okay.
**Mike Goldsmith** 13:10 So you can… so… and there's… the way that I've… in the example that I've got is, you could either do it to where it will just automatically… it'll either skip annotating for a period of time, so it doesn't know what to give it until it's got a training model that's appropriate.
or it can buffer, and the buffer is, like, the first 500 logs, it would then not do something with, but I think that's probably not a good pass-through, because that's gonna introduce a latency of it passing things through.
But yes, there's configurations, that you would say, how long are you gonna buffer for, how long are you going to wait before you do annotations for before you actually put something on there, and that could be a period of time or a number of things that's recognized.
**Mikołaj Świątek** 13:49 you as.
**atoulme** 13:49 Between that, on logs.
Could you… do you do this against the body of the love only, or can you do it over an attribute, or a set of attributes?
**Mike Goldsmith** 14:01 I've got it set up so it'll default to look at the body, but you can override that to say, look at this particular key instead, and I've got that set up as one attribute, but I guess we could expand that to be, like, multiple.
**atoulme** 14:12 Interesting.
**Mikołaj Świątek** 14:15 Yeah, I wanted to say that the idea of holding logs in a buffer kind of… sounds scary. We have specifically taken great lengths to not have that. We even deprecated the most popular processor ever, the batch processor.
Because this is a problematic thing to do in the middle of the pipeline. You break various assumptions.
About the queuing model, by doing that. If you do that, you kind of immediately have the question of.
Okay, what happens if the collector gets killed in the middle? Have we just, like, lost? Like, if you're… if you put it in your buffer, and then you acknowledge to the rest of the pipeline that's in front of your processor that, yes, this has, you know, this was consumed, then, you know, you break the… delivery, assumptions that the rest of the pipeline might have. So I would caution against putting that in, like, if… Okay.
**Mike Goldsmith** 15:17 Yeah. Yeah, as I said, I think it's the… the main reason to bring it to the SIG today was, like, to get interest, see if there's people interested in the idea. I think the implementation that I've got there could… you know, it's not a… it's not a setting thing, and I agree, I think buffering is probably the… probably the most controversial thing that I've got in that PR there, so, I'm happy to remove that, or see if there's real interest before we even consider that really.
**Mikołaj Świątek** 15:41 Yeah, yeah. Yeah, I think it's better to see if anybody actually wants it.
We put it in.
The other thing I… sorry, go on.
**atoulme** 15:52 Let me ask you then, is it… is it working also in synchronous mode, if you don't buffer?
Is it completely synchronous otherwise?
**Mike Goldsmith** 16:01 So, yeah, if it doesn't do buffer, it'll just do pass-through, so it can tell you how well-trained the model is, and if the model doesn't think it can give you something, it'll say that there's no model for it, and then it'll just pass on.
**atoulme** 16:12 Gotcha.
Last question for me, is it able to persist the model to disk at some point, or is that something you would consider?
**Mike Goldsmith** 16:20 I would… I would like to do that. So, in the proposal, I've said that I haven't done that… I haven't said that that's probably the first level requirement. One of the packages that I've listed as things that… one of the Go packages does do a persistence model, and I think that would be nice to look at if somebody would like to do that, because then you'd get the better tree discovery across multiple instances of the collector, because then you could load it once and let it redo that, and then you would have a faster startup time.
from the training models, too.
Yeah, I think that's definitely something that… that is supported in the… The drain method that you can serialize the tree, and then reload it.
**atoulme** 16:58 Okay, I'm interested. Yeah, I'd like to sponsor this.
**Mike Goldsmith** 17:04 Okay.
**atoulme** 17:06 I have more questions for you, because, for example, I'd like you to do it with a cluster of collectors, and make sure they have a uniform model.
So, could you also stop the training?
At some point.
**Mike Goldsmith** 17:19 Yeah.
**atoulme** 17:20 That's just a question for you.
**Mike Goldsmith** 17:22 Yeah.
**atoulme** 17:25 I'll put my name down.
**Mike Goldsmith** 17:27 Okay, thank you.
**atoulme** 17:28 I do sponsor.
**jmacdonald** 17:30 Mike, this is really cool. I don't actually have a use for it, but I'm familiar with the problem space, and it looks like a good addition to the system here.
One thing you should know, I guess, is that there's been some interest and some discussion about storage extensions. If you were going to persist your model. It's interesting to look at whether the current storage extension is good enough, or whether you might want more. So there's been some sort of rumbling about how we'd like to have something that looks like a PebbleDB or a RoxDB, type of interface with a range scan in the storage interface, which we don't have today. So I'm curious if you've looked at storage. And then the other sort of connected remark here is that we as a group, because of the architecture of the Go collector here, are suffering that we don't have a way to put persistence down before a processor. You'd like to be able to say, I want to put my receiver and then persistence storage on the queue, or whatever it is, the storage extension.
and then go into my processor, just so that, to address Mikolai's comment about, like, loss of data, we would like to be able to put it on disk first, essentially, in some cases.
And that's something we don't have any plans for, and it's… it looks like a defect. You can imagine… creating a connector to simulate it, so you'd have your receiver go into a persistent queue, then to a connector, back to another processor, and so on, but it's kind of like making the user jump through hoops. So, the question is about a persistent queue before the processor. It's a little hard to set up. Anyway, this looks really cool, thank you.
**Mike Goldsmith** 18:59 Yeah, thank you. Yeah, I haven't looked too deeply into what storage models we'd need or what would be supported, but yeah, I definitely had the idea of seeing it something that we'd like to do, and then having that, That storage model be available to multiple instances concurrently would be very interesting, because then you would have a near-zero start, like, training phase, which means that it'd be much faster to actually get really accurate templates or patterns out of the logs.
But yeah, thank you everybody for the feedback. Feel free to come in and put comments or feedback on the issue, all the reference PR, and then we can keep going with that. Thank you.
**atoulme** 19:40 Awesome.
Okay, next up, vishta.
**vojta.vojacek** 19:46 Yes.
Okay, so I have a very similar issue as Mike, but Mike is many, many steps ahead. I am about to, or we are about to, in our company, start migrating from Telegraph to hotel. Not everything. We have most of our stuff in hotel, and some of the things we wanted to have in hotel are not available just yet.
And we want to create those components and then eventually donate them.
And such, components, from top of my head, DNS query.
and I think Varnish is up there as well. There's, like, I think 6 in total, so it will be… Quite a donation.
And this is just me, throwing my intentions out into the community, and potentially looking for some tips, or, Some lessons learned, if you've done this sort of thing before.
**atoulme** 20:47 Yeah, I can tell you, do not send 6 different things at once, we will not be able to take that.
**vojta.vojacek** 20:53 One at a time, gotcha.
**atoulme** 20:57 So, the idea is to socialize things as much as possible. I think Mike just showed, how it's done, just now. Like, you open an issue, he says, this is what I'm doing, this is why it's important, where it's coming from, here is some past usage of that.
And here's maybe even just a PR. If you look, the bar to contribute, to contribute above went up, because we… we need to really get to a better level in terms of being… having better code ownership and maintenance of some of the code. That said, things like DNS query is actually something that we need to… to deliver on my end, so I'll be interested.
So… Yeah, you're gonna have to go all that way. If you don't have a PR, If you don't have the code, do not hesitate to open the issue now, because it helps.
**vojta.vojacek** 21:46 Yeah, no.
**atoulme** 21:47 the conversation.
And so, there's a lot of things that you can do. It's like, something that, we've learned is, like, you want to go as parallel as possible. You don't just go with one thing, you go with six.
But you make them parallel, so that you can keep working on one of them at a… like, you can keep pushing, pushing different ways, right? Not all of them will make it, but that's okay, because by the time you're about, like, 2 or 3 in, it's already feeling better, and you have a better way to kind of go around it.
And then, yeah, make a PR, maybe host the receivers on your end to showcase it, and get people to kind of, plus one your stuff, and show up at the SIG meeting, and make a case for it.
You can also use Slack, judiciously to let people know about your development, and just be aware that at this point, given the flood of stuff that we have to deal with, we're not super receptive to issues and PRs as much, so it's… It's been done.
**vojta.vojacek** 22:50 I understand.
**atoulme** 22:54 What I'm busy, folks. Niklash.
**Mikołaj Świątek** 22:56 Hmm.
I don't know, there's some… I would also carefully look through Contrib to see if there's any components that are maybe not doing what you want, but in some way close to doing what you want.
Like, it's possible that what you want, for example, is some additional features in, say, the transform processor, if it's about transforming data. If it's DNS, maybe it fits into the lookup processor, that's still in development, but it's, like, kind of… A similar concept, and then it's much easier to go in and add features to an existing component than propose a new component at large.
**vojta.vojacek** 23:33 Yeah, no, I do agree with extending existing functionalities better than… Whole new components.
You know, thank you all for the feedback and tips.
**jmacdonald** 23:59 Hi, I'm gonna put myself next on the agenda, unless we're… there's more on that topic.
So, I've pulled up the, agenda here.
And it's… my screen is too large, but you can see this, right?
So, I go to many of these meetings, and occasionally I will show up in the APAC meeting, which is a Tuesday afternoon for me, right at the end of my workday. And it's rarely attended, and I last week promised I would rebroadcast, first of all, a couple of OTEP-type RFCs here. So I'm just gonna show you all what's hot on the other side of the world.
And hope for some help getting these things in. So here, for example, This is, Andrew Wilkins, with Elasticsearch, providing some, some updates, and some improvements for the scraper extension.
it looks good to me. The idea is you want… the current scraper extension runs on a timer, and you'd like to be able to maybe run it on a webhook or some other signal, and this is an extension interface, so that we can have, you know, arbitrary extensions defining random scrapers, which is cool. I'm very much in favor of extension interfaces, so I… that's how I got in this conversation.
Any conversation on this topic?
You're not required to, but it's a request to review this PR, if you will, please.
Especially if you know a lot about the scraper. The second of my two also comes from the Elastic team. I believe Blake has been to this group here once to advertise his work, but it's hard to reach the time zone.
For him.
**Mikołaj Świątek** 25:49 Josh, Josh, I already, I already talked people's ears off about this at KoopCon.
**jmacdonald** 25:55 Okay, great. I was gonna say, we're sort of benefiting from the KubeCon After Effects this week, so if you've already seen this one, don't let me talk to you about it, but it's one that's waiting for attention.
That was quick, but that's all I have on those two. There's one of mine, and since there's time left in the hour, I think probably we're benefiting from KubeCon exhaustion last week.
But I want to bring this up, because it's, kind of evergreen, in my opinion. So, the issue was filed, to say, essentially, the batch processor, either it's got to be fixed or thrown away.
And we're not… we've done neither of those yet, although I've got a PR that's been pending for almost a year to do some of this.
and this was… I kind of already touched on this a second ago when I was commenting on Mike's… Mike's topic, that we have no way right now to do persistent queue in the middle of a processor chain, and there's something that I want to say at the end of my little talk here about that same thing.
But the bigger idea here is that there are major problems with the batch processor. Why it's been deprecated for a while.
And the glaring points are that it never returns an error, it returns nil every time. It does support back pressure in a sense, but not entirely.
And so it also lacks concurrency.
So, I've, you know, there are 3 defects here, and they're pretty big. And so, this is one reason why we've been deprecating it, and we've put a lot of the functionality that… this same functionality has been reinvented in the Exporter helper.
And users really should switch to the exporter helper, in my opinion, though there will always be a reason why you might want to have something like a batch processor in your processor chain. And we've listed a few of them if you dig through these issues. Like, if you're the group by attributes processor, which is in Contrib, like, you want to have large batches coming into you, and if you need large batches coming into you, well, you need a batch processor, and the batch processor currently is on a deprecated list, so that's bad.
Better.
So let me show you the PR then.
This PR is essentially taking the observation that we've invested a lot in our Exporter Helper. We have a new implementation of a queue, a new implementation of a batcher, as well as the timeout and retry and deadline stuff that happens inside of Exporter Helper. That's been implemented.
And now we have it. So it's due… it's got new flags in the exporter helper called waitForResult to get that error propagation to work, and it's got a flag called block on overflow, which says I want to wait for the the exporter, which means that you get back pressure. So you need these two features to get back pressure and error propagation, and that's really important. So this is why the batch pressures have been deprecated, but I think it shouldn't go away. So what I have here is a PR that fixes it.
And the nice thing is it fixes it by using the exporter helper. So we've got this new piece of code that implements batching and queuing and so on, storage extensions as well.
we can plug this into a processor, and that's essentially what this does. It takes the old 500 lines of code that were broken, and replaces it with, like, a new 100 lines of code that just calls the exporter helper. Now… It's enabled by, it's using feature flags so that if currently we could merge this and nothing would change by default, you'd have to turn on those feature flags. If you turn them on, you get the exporter helper code path.
And so I think this is what we should do. We should merge this right away. There's one or two holdouts here. Why wouldn't we merge this? It gives metrics that look like an exporter is in the middle of your process or pipeline right now, and that's just, like, a minor issue that we ought to fix, and I would be glad to fix, but like, this has been sitting for a long time. I'm wondering if we should merge this first.
The second thing is that there's a potential here to embrace what we've done in the Exporter Helper, and actually improve the batch processor as a result. So I listed three defects, and my PR here only fixes two of them. It fixes the error propagation.
And it fixes, let's see, the other issue, but doesn't fix concurrency. So, concurrency is something that the exporter helper has a knob for. You can set num consumers, and that will mean more people are pulling from your queue, and the legacy batch processor has a fixed one consumer.
And that was a major problem with the batch processor, because it forced you to turn on queuing downstream, it meant you could never get batch… back pressure, and so on. So… so if you… if we accept this PR, what we can do is embrace the exporter helper feature set. We can turn up concurrency, which was always a defect in this component. We can also turn on the storage extension, which is what I was talking about with Mike. Like, we could have the batch processor, which is now using the exporter helper.
turn on any one of its features, meaning you could add a persistent QBatch processor.
right before your, drain algorithm, for example. These are opportunities… these are opportunities. And I did mention it, that we could, somewhere in this PR, that, like, non-consumers, the concurrency factor is the first obvious most thing to embrace, but then, you know, persistent storage in a processor Is also something we could do.
If any of this sounds good to you, you know, I need approvals. And I… I mean, I think that it would be best if we merged this first, and then I'll be glad to fix the export… the metric problem.
Are there any questions? I'm sorry if that was too much information.
Silence is… is okay, too.
Nikolai.
**Mikołaj Świątek** 31:40 So, so if you… If you actually enable the feature flag.
that changes the… that changes the behavior, right? Because the behavior of the original batch processor is that if you just send stuff to it in a loop, it's gonna accept and accept and accept and eventually send the batch from the other side. Like, that's the crux of the problem.
But from… I haven't read, like, what settings you've actually put in there by default, but my impression is that here, we're just gonna block.
Right?
Or are we, like… because we either have to… either have to block, or we have to have an in-memory queue, right?
**jmacdonald** 32:25 Right, so… so… so… literally all I'm doing is taking an exporter helper and stuffing it into a processor, so any one of those exporter helper settings could be set. What I did was set, first of all, block on overflow true, because that's how the batch processor has always been, so that's a legacy behavior. And then wait for result, that's the feature flag, where I'm saying, yeah, the old behavior is to, like, return as soon as the queue has accepted the data.
with a success code, not to wait for a result. And I believe that is a, like, kind of a major defect, like, but it is a change of behavior that you should have to elect.
Or we should have, like, slowly changed the default of. And I think that the default of the batch processor is dangerous and harmful, like, it loses… suppresses errors.
So, we shouldn't leave that default forever. That's why we were talking about removing the badge processor, but we could also just change that default. So this propagate errors flag, I would start off as the legacy behavior, which is false, and I would turn it to true eventually.
This is… ugh.
this is, I think users would have the same type of confusion. How do I set my consumers, or my queue size? But, nevertheless, either we remove the batch processor, or we do something like what I've done here.
This is a feature flag that we could add, or a configuration field that we could add, what I was mentioning, is that… and if you've been in this group for a while, you may know that I worked on a… concurrent bash processor as part of the OTL Arrow project years ago, and I kept trying to push it upstream into Contrib, and the argument was, no, no, no, we're going to do all that stuff in the exporter helper, which we now do, and I agree.
Good that we didn't push a new processor upstream.
But now we can either fix the old batch processor, or we remove it. And to fix the old batch processor, firstly, we have this propagation… error propagation behavior, but we also have this concurrency feature. And then, you know, you can imagine setting the storage setting as well.
**atoulme** 34:27 Oh, okay.
I have a question.
**jmacdonald** 34:29 Okay.
**atoulme** 34:31 So, let's say you do all this, and we make the best cluster behave better.
What that would mean is that when you are processing data, and you have the batch process around, which, you know, people just put on at this point as a matter of…
**jmacdonald** 34:44 just there, it's in all the legacy configurations, I understand.
**atoulme** 34:48 And so people just, you know, copy-paste configurations around, there's a batch processor. Now, you're having the batch processor, which is behaving exactly like the exporter helper, and then on top of that, you still have your exporter, so you still have the exporter helper. Are you… Are you creating memory hogs?
**jmacdonald** 35:06 Okay, so, okay, this is really good feedback. I think it's probably the reason why we shouldn't merge my PR, now that you mention it, is that this creates a tendency to easily enable multiple bashing steps, which means that you are capable of storing memory twice.
**atoulme** 35:21 Yeah.
**jmacdonald** 35:22 Yeah.
So, let's see. I've heard that feedback a couple times. Now that I've heard it from you, now I'm ready to accept. So, one thing we could do is, like, imagine some sort of, like.
heuristic configuration checker that, like, walks through your pipeline and says, aha, I see two instances of an exporter helper here. That's not… not advisable, unless you know what you're doing.
**atoulme** 35:46 It's a long…
**jmacdonald** 35:47 Because the example for this drain processor that we were just talking about, or the group by attributes processor, was, I really intentionally mean for this to be grouping in my processor pipeline, and I probably should disable batching in the next exporter step.
On the other hand, Well, okay, this deserves some investigation. Like, you could… you could argue that as long as the exporter helper is set correctly, it's going to pass these large batches through, and it's not going to add any more memory.
That might be the case.
There could also be bad configurations. So… I think, I still believe that we should modernize the batch processor. We also should call it deprecated, or, like, use at your own risk, or use in special circumstances only.
**atoulme** 36:38 But…
**jmacdonald** 36:40 I just… I know that so many people are still using the batch processor. You look at the list of PRs, it frequently comes up as, oh, here's a fix for the batch processor, and yet we've had a pending… like, so many fixes for the batch processor have been rejected because we were deprecating it, and that's what I'm worried. We're still deprecating it.
**Mikołaj Świątek** 36:56 I haven't…
**atoulme** 36:58 It's not deprecated, by the way, it's not. The status is not depicted.
**jmacdonald** 37:03 But, okay, we removed it from a bunch of documentation, and I think people think of it as deprecated, at least the people who are developing the exporter helper.
**atoulme** 37:12 My issue to deprecate the batch processor is still open a year in. If you get the status in the YAML, it says it's better. If you run a deprecated component, it logs a warning at start time, and it does not do that.
**jmacdonald** 37:26 I see.
**atoulme** 37:27 processor. So, I don't think we have actually done the job to deprecate this thing properly, even.
**Mikołaj Świątek** 37:33 Wasn't there, like, a blog post saying that it's deprecated? I could swear there was something like that.
**atoulme** 37:39 And we had a presentation at KubeCon where we said we are going to remove it, an exporter helper is here, and yet, the code does not match.
**jmacdonald** 37:48 Yeah.
**atoulme** 37:49 So that sucks.
**jmacdonald** 37:53 I would like to help, I just don't know quite what to do.
**atoulme** 37:58 I'm simbolt here, hey, Alex, you're a maintainer on Core. What's up, man?
**jmacdonald** 38:08 Not to put anyone on the spot, Evan can't…
**atoulme** 38:11 Thank you for the question.
**Alex Boten** 38:12 Call out.
**atoulme** 38:12 He's the only human core here, so he gets it.
**Alex Boten** 38:16 Yeah, I mean, I… I'm happy to open a PR to mark it as deprecated. I think that's probably the step number one.
We, as you said, we did present that we were going to do away with it on multiple different avenues, I suspect.
at the very least, if we open this PR, which I'm doing right now.
and people complain about it, then we can at least have that conversation then, and then we could make a different choice if we want to upgrade, if we want to fix all the bugs, but I suspect that we should just move forward with the plan that was to deprecate it and remove it.
And I love how immediately, as soon as I say I'm gonna open a PR to deprecate it, now people have comments.
**jmacdonald** 39:00 So…
**Mikołaj Świątek** 39:01 No, no, I… It's working.
My comment is actually not about the deprecation itself, it's, like, I'm looking at a published issue about removing references to it, and it's almost done. There's one PR in OpenTelemetry Helm charts open, apparently.
or not open, like, it's not done, so that's just… you should open it, I think, and concurrently, you should tag the charts maintainers.
in the issue, to see. Maybe this is already done, and it wasn't… just wasn't updated.
**jmacdonald** 39:30 My understanding is that the charts issue actually blocked us from removing from deprecation. Like, this is going to… this is… that's the route by which these complaints are going to arrive.
**Mikołaj Świątek** 39:41 given.
**jmacdonald** 39:44 I wish Tyler Helmuth was here, because I remember him commenting on this at one point in this meeting, to get the specifics, but basically, it… I think it boils down to the same as Antoine's comment, which is that the default chart has this, and if you remove it, then things break, and if you don't remove it, then things break, and if you make it behave like my PR, you need to cost twice as much. There's, like, not a great answer. Potentially, we have to solve this in a better way by checking configurations or something like that.
Evan, please.
Davos.
**Evan Bradley** 40:19 Okay. I got… I got tagged as well, so I figured I'd chime in. My question is, so, you've got this PR to modernize it, and you mentioned while talking about it that there might be some use cases for that. If we do deprecate it, are we… Are there use cases that we are now not covering? Are there going to be things that people are doing today that they can no longer do just using the exporter helper?
**jmacdonald** 40:39 Yeah, that's right, and I think they're small, but maybe they're real. Like, the one that I was mentioning was… Mike spoke about a processor that needs lots of volume of data, and it's… and if you… one way to get that is by batching ahead.
The one that's already in the contrib repo is called Group by Atchers, and it's like, it literally says, this works best if you put our batch processor before me in its README. I think there's one more that we're aware of, it's metric aggregation as well.
So, maybe a solution to this is to continue on the path of deprecating the batch processor, and eventually removing it while we recreate, essentially, what I've proposed as a modernized batch processor, but rename it, like, Inline Batch Processor.
so that you… you know what you're getting into when you use it. Like, you better not follow this with an exporter helper batch processor, or if you do, like, just… you set up two batch processors.
**atoulme** 41:33 I recalled…
**Mikołaj Świątek** 41:35 Sorry. I recall there was a proposal to, to, like, add a connector that did this?
**atoulme** 41:41 Yeah.
**Mikołaj Świątek** 41:41 It kind of makes a little bit more sense, because a connector is really also an exporter, so it's kind of natural to have exporter helper in it, and also it's, like, a more advanced component, in a way, so… and this sounds like you might want to do batch processor sometimes, but this isn't really what everyone should be doing. Like, you should be doing it very intentionally if you have a need.
to have matching in the middle of the pipeline, right? So maybe… I think that even exists in Contrapt somewhere. I remember reading an issue.
**jmacdonald** 42:11 Yeah, so I can… I can share what I know. I mean… I think… I think you're right, the connector pattern kind of fills in for a processor, if you use it correctly, and it makes the user kind of rearrange their configuration a bit, but… but it's sort of there. This was… the… going backwards in time, the history of me making this proposal was that somebody had proposed in Contrib a processor called the Q-Processor.
And it was essentially just an exporter helper with a queue enabled as a processor. And you dug into that a little bit. Okay, why are you doing that? Well, there's this failover connector, and I want the failover connector to have a queue before it.
But there are these existing settings on the failover connector, which interfere with the exporter helper. Like, now it's going to be pretty confusing if you throw an exporter helper on that connector, the failover connector, even though it's kind of what they need.
And it gave me the idea that we should just, like, actually create a processor, which is the entire exporter helper feature set, which I called Pipeline Processor. The idea is, like, any of those features, retry, timeout.
Persistent queue, memory queue, or retry, sorry, or batch, so 5 behaviors or so.
All of those belong in the exporter helper, naturally, but you could always find a case somewhere to use those in a processor.
But you're right, connector is essentially the same, with some syntax.
**Evan Bradley** 43:42 Could we document some of that in an issue somewhere, and maybe link it to the deprecation PR?
**jmacdonald** 43:49 The history of the queue processor, and the failover processor, and the connector idea?
**Evan Bradley** 43:55 Yeah, I mean, mainly just that, you know, we're deprecating this, but if we want some of these features available inline in a processor, this is, you know, some of the history of that, and where we think that could go.
**jmacdonald** 44:11 Yes, okay, so I can file a new issue. I will capture that. So the issue essentially says, we thought about modernizing it, we thought about deprecating it, none of those were the perfect answer. Now what we're thinking about is either a connector or a processor that re-exports the exporter helper facilities.
Yes. And it's a discussion, because there's some reason why failover doesn't quite fit the model, and that's actually where it was requested.
So, okay, I'll follow that. I will file that.
**Evan Bradley** 44:39 Thanks. I'm just thinking to capture this discussion and, pave a path forward in case there are people who… Have major complaints.
**jmacdonald** 44:50 I will do that. Thank you. And that's the end of my agenda. There was nothing after me when I first looked at it. We might have something now.
**atoulme** 44:58 Check… The last thing here is to go over high priority issues for Stability Phase 1 listed on the board, so… I don't know, that's… I'll just share my screen.
All right, again, so we're trying to go through Phase 1 for stability. We have 1, 2, 3, 4, 5, 6, 7 things that we want to stabilize.
How are we doing?
**Alex Boten** 45:38 I wonder if it makes sense to… Postpone talking about this topic, since most of… Many of the people that are running these issues are not present right now.
**atoulme** 45:50 Understood.
In any case, please be aware, this is ongoing work. Feel free to review if you'd like to contribute or help.
Please put the word in, and Let's get it done, folks. Thank you so much.
Anything else?
Alright, thanks all. Have a great day.
**Evan Bradley** 46:17 Bye, everyone.
